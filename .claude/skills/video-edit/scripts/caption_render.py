#!/usr/bin/env python3
"""Render word-highlight caption overlays from an mlx_whisper transcript and
burn them onto a video with ffmpeg. No libass/drawtext dependency (this
Mac's ffmpeg build has neither, see research-tooling.md) — captions are
drawn with Pillow into transparent PNG frames, grouped into short-lived PNG
"cards" (one per caption line), and composited with ffmpeg's overlay filter.

Style defaults follow 00_project/knowledge/video-editing-library/_derived/
video-edit-rules.md (word-by-word, white text + black outline, bottom-safe
position, max ~4 words per line) — pass --style to override.

Usage:
  caption_render.py <transcript.json> --video <video.mp4> --out <out.mp4> \
      [--max-words-per-line 4] [--font <path.ttf>] [--position bottom|center] \
      [--w 1080] [--h 1920] [--title "Title text"] [--title-font <path.ttf>]

A --title renders a fixed white rounded-rect badge with black bold text near
the top of the frame for the whole clip (matches a reference screenshot's
"title on top, caption center" look). Omit it for captions-only.

Exit codes: 0 ok, 2 bad input.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("MISSING: Pillow. pip install --user Pillow", file=sys.stderr)
    sys.exit(3)

DEFAULT_FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
DEFAULT_TITLE_FONT = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"


def ffprobe_duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return float(out)


def wrap_title(text, draw, font, max_width):
    words = text.split()
    lines, cur = [], []
    for word in words:
        trial = " ".join(cur + [word])
        if draw.textbbox((0, 0), trial, font=font)[2] <= max_width or not cur:
            cur.append(word)
        else:
            lines.append(" ".join(cur))
            cur = [word]
    if cur:
        lines.append(" ".join(cur))
    return lines


def render_title_frame(text, w, h, font_path, size):
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, size)
    pad_x, pad_y, line_gap = 48, 28, 10
    max_text_w = w * 0.78
    lines = wrap_title(text, draw, font, max_text_w)
    line_sizes = [draw.textbbox((0, 0), ln, font=font) for ln in lines]
    line_w = max(b[2] - b[0] for b in line_sizes)
    line_h = max(b[3] - b[1] for b in line_sizes)
    box_w = line_w + pad_x * 2
    box_h = line_h * len(lines) + line_gap * (len(lines) - 1) + pad_y * 2
    box_x = (w - box_w) / 2
    box_y = h * 0.06
    radius = min(40, box_h / 2)
    draw.rounded_rectangle(
        [box_x, box_y, box_x + box_w, box_y + box_h], radius=radius, fill=(255, 255, 255, 255)
    )
    y = box_y + pad_y
    for ln, b in zip(lines, line_sizes):
        lw = b[2] - b[0]
        x = box_x + (box_w - lw) / 2
        draw.text((x, y), ln, font=font, fill=(10, 10, 10, 255))
        y += line_h + line_gap
    return img


MIN_WORD_DURATION = 0.12  # mlx_whisper can return a zero-length word; it would never show (found 2026-10-27).


def load_words(transcript_path):
    data = json.loads(Path(transcript_path).read_text())
    words = []
    for seg in data.get("segments", []):
        for w in seg.get("words", []):
            text = (w.get("word") or w.get("text") or "").strip()
            if not text:
                continue
            start, end = w["start"], w["end"]
            if end - start < MIN_WORD_DURATION:
                end = start + MIN_WORD_DURATION
            words.append({"text": text, "start": start, "end": end})
    return words


def group_lines(words, max_words=4, max_gap=0.6, font_path=None, size=64, max_w=None):
    """Group words into caption lines, breaking on word-count, a speech gap,
    or (if font_path/max_w given) when the line's rendered width — including
    the stroke outline — would overflow the frame. German compound words can
    blow a 4-word line past 1080px at font-size 64, so width is checked too,
    not just word count (found 2026-10-27, hand-run)."""
    measure = None
    if font_path and max_w:
        font = ImageFont.truetype(font_path, size)
        stroke_w = max(2, size // 18)
        img = Image.new("RGBA", (10, 10))
        d = ImageDraw.Draw(img)

        def measure(text):
            bbox = d.textbbox((0, 0), text, font=font, stroke_width=stroke_w)
            return bbox[2] - bbox[0]

    lines, cur = [], []
    for w in words:
        would_break_gap = cur and w["start"] - cur[-1]["end"] > max_gap
        would_break_count = cur and len(cur) >= max_words
        would_break_width = False
        if measure and cur:
            trial_text = " ".join(x["text"] for x in cur + [w])
            would_break_width = measure(trial_text) > max_w
        if cur and (would_break_count or would_break_gap or would_break_width):
            lines.append(cur)
            cur = []
        cur.append(w)
    if cur:
        lines.append(cur)
    return lines


def render_line_frame(line, active_idx, w, h, font_path, position, size):
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, size)
    text_parts = [wd["text"] for wd in line]
    gap = " "
    full_text = gap.join(text_parts)
    bbox = draw.textbbox((0, 0), full_text, font=font)
    total_w = bbox[2] - bbox[0]
    x = (w - total_w) / 2
    stroke_w = max(2, size // 18)
    if position == "bottom":
        # Keep clear of the house safe-zone bottom margin (export-specs.md: bottom
        # 400px of a 1080x1920 frame) — the old fixed h*0.78 sat inside it with a
        # default font size (found 2026-10-27, functional test).
        safe_bottom = h * (400 / 1920) + h * (20 / 1920)
        text_h = size + stroke_w * 2
        y = h - safe_bottom - text_h
    else:
        y = h * 0.5
    cx = x
    for i, wd in enumerate(text_parts):
        colour = (255, 214, 10, 255) if i == active_idx else (255, 255, 255, 255)
        draw.text((cx, y), wd, font=font, fill=colour, stroke_width=stroke_w, stroke_fill=(0, 0, 0, 255))
        word_w = draw.textbbox((0, 0), wd, font=font)[2]
        cx += word_w + draw.textbbox((0, 0), gap, font=font)[2]
    return img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript")
    ap.add_argument("--video", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--max-words-per-line", type=int, default=4)
    ap.add_argument("--font", default=DEFAULT_FONT)
    ap.add_argument("--position", choices=["bottom", "center"], default="bottom")
    ap.add_argument("--w", type=int, default=1080)
    ap.add_argument("--h", type=int, default=1920)
    ap.add_argument("--font-size", type=int, default=64)
    ap.add_argument("--title", default=None)
    ap.add_argument("--title-font", default=DEFAULT_TITLE_FONT)
    ap.add_argument("--title-font-size", type=int, default=54)
    args = ap.parse_args()

    words = load_words(args.transcript)
    if not words:
        print("ERROR: no words in transcript", file=sys.stderr)
        sys.exit(2)
    lines = group_lines(
        words, args.max_words_per_line,
        font_path=args.font, size=args.font_size, max_w=args.w * 0.9,
    )

    frames_dir = Path(args.out).parent / "_caption_frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    overlay_clips = []

    if args.title:
        duration = ffprobe_duration(args.video)
        title_png = frames_dir / "title.png"
        render_title_frame(args.title, args.w, args.h, args.title_font, args.title_font_size).save(title_png)
        overlay_clips.append({"png": str(title_png), "start": 0.0, "end": duration})

    for li, line in enumerate(lines):
        line_start = line[0]["start"]
        line_end = line[-1]["end"]
        for wi, active in enumerate(line):
            png = frames_dir / f"line{li:03d}_word{wi:03d}.png"
            img = render_line_frame(line, wi, args.w, args.h, args.font, args.position, args.font_size)
            img.save(png)
            overlay_clips.append({"png": str(png), "start": active["start"], "end": active["end"]})

    # Build one ffmpeg filter_complex: overlay each PNG only during its [start,end)
    # window using enable='between(t,start,end)'. For long videos, chain in batches
    # to stay under ffmpeg's argument limits (batches of 200 overlays).
    video_in = args.video
    tmp_out = args.out
    batch_size = 150
    cur_input = video_in
    for b in range(0, len(overlay_clips), batch_size):
        batch = overlay_clips[b: b + batch_size]
        step_out = f"{Path(args.out).with_suffix('')}._step{b}.mp4"
        inputs = ["-i", cur_input]
        for c in batch:
            inputs += ["-i", c["png"]]
        filt_parts = []
        last_label = "0:v"
        for i, c in enumerate(batch, start=1):
            out_label = f"v{i}" if i < len(batch) else "vout"
            filt_parts.append(
                f"[{last_label}][{i}:v]overlay=0:0:enable='between(t,{c['start']},{c['end']})'[{out_label}]"
            )
            last_label = out_label
        filt = ";".join(filt_parts)
        cmd = ["ffmpeg", "-y", *inputs, "-filter_complex", filt, "-map", f"[{last_label}]",
               "-map", "0:a?", "-c:v", "libx264", "-crf", "18", "-c:a", "aac", step_out]
        subprocess.run(cmd, check=True)
        cur_input = step_out

    Path(cur_input).rename(tmp_out)
    print(f"OK captions burned -> {tmp_out} ({len(lines)} lines, {len(overlay_clips)} word frames)")


if __name__ == "__main__":
    main()
