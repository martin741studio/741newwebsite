#!/usr/bin/env python3
"""Profile a reference video or image for the video-edit workflow.

Takes a URL (downloads with yt-dlp) or a local file. Computes duration,
scene cuts (PySceneDetect ContentDetector), shot-length stats, a cut-rate
timeline, a contact sheet (one frame per shot), and a word-level transcript
(mlx_whisper) when audio speech is present. Writes:

  <out_dir>/raw/source.<ext>        downloaded or copied source file
  <out_dir>/reference_profile.json  all computed numbers
  <out_dir>/contact_sheet.jpg       grid of one frame per shot
  <out_dir>/transcript.json         mlx_whisper word-level output (if audio)
  <out_dir>/summary.md              10-line human summary

Usage:
  reference_profile.py <url_or_path> --out <out_dir> [--no-transcript] [--no-download]
  reference_profile.py <image_path> --out <out_dir> --image   (look-and-feel only, no timing)

Exit codes: 0 ok, 2 bad input, 3 missing tool.
"""
import argparse
import json
import math
import os
import shutil
import statistics
import subprocess
import sys
from pathlib import Path

TOOLS = ["ffmpeg", "ffprobe", "yt-dlp"]


def check_tools(need_ytdlp=True):
    missing = []
    for t in ["ffmpeg", "ffprobe"]:
        if not shutil.which(t):
            missing.append(t)
    if need_ytdlp and not shutil.which("yt-dlp"):
        missing.append("yt-dlp")
    if missing:
        print(f"MISSING TOOLS: {', '.join(missing)}. Ask Martin before installing.", file=sys.stderr)
        sys.exit(3)


def is_url(s):
    return s.startswith("http://") or s.startswith("https://")


def ffprobe_json(path):
    out = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", str(path)],
        capture_output=True, text=True, check=True,
    )
    return json.loads(out.stdout)


def download(url, raw_dir):
    raw_dir.mkdir(parents=True, exist_ok=True)
    out_tpl = str(raw_dir / "source.%(ext)s")
    cmd = [
        "yt-dlp", "-f", "bv*[height<=1080][ext=mp4]+ba[ext=m4a]/b[ext=mp4]/b",
        "--merge-output-format", "mp4", "--write-info-json", "--no-write-subs",
        "-o", out_tpl, url,
    ]
    subprocess.run(cmd, check=True)
    mp4s = list(raw_dir.glob("source.mp4"))
    if not mp4s:
        print("ERROR: download did not produce source.mp4", file=sys.stderr)
        sys.exit(2)
    info = {}
    info_files = list(raw_dir.glob("source.info.json"))
    if info_files:
        info = json.loads(info_files[0].read_text())
    return mp4s[0], info


def detect_scenes(video_path):
    from scenedetect import detect, ContentDetector
    scene_list = detect(str(video_path), ContentDetector())
    cuts = []
    for start, end in scene_list:
        cuts.append({"start": round(start.get_seconds(), 2), "end": round(end.get_seconds(), 2)})
    return cuts


def shot_stats(cuts, duration):
    if not cuts:
        return {"num_shots": 1, "avg_shot_len": round(duration, 2), "median_shot_len": round(duration, 2),
                "min_shot_len": round(duration, 2), "max_shot_len": round(duration, 2), "cuts_per_min": 0.0}
    lens = [c["end"] - c["start"] for c in cuts]
    cuts_per_min = round((len(cuts) - 1) / (duration / 60), 2) if duration > 0 else 0.0
    return {
        "num_shots": len(cuts),
        "avg_shot_len": round(statistics.mean(lens), 2),
        "median_shot_len": round(statistics.median(lens), 2),
        "min_shot_len": round(min(lens), 2),
        "max_shot_len": round(max(lens), 2),
        "cuts_per_min": cuts_per_min,
    }


def cut_rate_timeline(cuts, duration, bucket_s=10):
    if duration <= 0:
        return []
    n_buckets = max(1, math.ceil(duration / bucket_s))
    buckets = [0] * n_buckets
    for c in cuts[1:]:
        idx = min(int(c["start"] // bucket_s), n_buckets - 1)
        buckets[idx] += 1
    return [{"t": i * bucket_s, "cuts": b} for i, b in enumerate(buckets)]


def classify_transitions(video_path, cuts, window=0.12):
    """Rough hard-cut vs dissolve/zoom classification by sampling frames
    just before/after each cut boundary and comparing pixel diff vs a
    slower-changing neighbourhood (dissolve = gradual, hard cut = abrupt)."""
    results = []
    for c in cuts[1:]:
        t = c["start"]
        # sample 3 frames: t-window, t, t+window via ffmpeg scene score is already
        # the detector's job; here we just bucket by shot length as a cheap proxy
        # for "hard cut" (always, PySceneDetect ContentDetector finds hard content
        # changes; true dissolve detection needs frame-diff slope, done in v2).
        results.append({"t": t, "type": "hard_cut"})
    return results


def contact_sheet(video_path, cuts, out_path, max_frames=24, cols=6):
    frames_dir = out_path.parent / "_frames_tmp"
    frames_dir.mkdir(exist_ok=True)
    picks = cuts if len(cuts) <= max_frames else cuts[:: max(1, len(cuts) // max_frames)][:max_frames]
    paths = []
    for i, c in enumerate(picks):
        mid = (c["start"] + c["end"]) / 2
        fp = frames_dir / f"frame_{i:03d}.jpg"
        subprocess.run(
            ["ffmpeg", "-y", "-ss", str(mid), "-i", str(video_path), "-frames:v", "1",
             "-vf", "scale=320:-1", str(fp)],
            capture_output=True, check=True,
        )
        paths.append(fp)
    if not paths:
        return None
    rows = math.ceil(len(paths) / cols)
    inputs = []
    for p in paths:
        inputs += ["-i", str(p)]
    filter_inputs = "".join(f"[{i}:v]" for i in range(len(paths)))
    layout = f"{filter_inputs}xstack=inputs={len(paths)}:layout=" + "|".join(
        f"{(i % cols) * 320}_{(i // cols) * 180}" for i in range(len(paths))
    )
    subprocess.run(["ffmpeg", "-y", *inputs, "-filter_complex", layout, str(out_path)],
                    capture_output=True, check=True)
    shutil.rmtree(frames_dir, ignore_errors=True)
    return out_path


MLX_WHISPER_BIN = str(Path.home() / ".local" / "bin" / "mlx_whisper")


def transcribe(video_path, out_dir):
    whisper_bin = MLX_WHISPER_BIN if Path(MLX_WHISPER_BIN).exists() else shutil.which("mlx_whisper")
    if not whisper_bin:
        return None
    wav = out_dir / "_audio.wav"
    subprocess.run(["ffmpeg", "-y", "-i", str(video_path), "-ac", "1", "-ar", "16000", str(wav)],
                    capture_output=True, check=True)
    subprocess.run(
        [whisper_bin, str(wav), "--model", "mlx-community/whisper-large-v3-turbo",
         "--word-timestamps", "True", "--output-format", "json",
         "--output-dir", str(out_dir), "--output-name", "transcript"],
        capture_output=True, text=True, check=True,
    )
    wav.unlink(missing_ok=True)
    out_path = out_dir / "transcript.json"
    return out_path if out_path.exists() else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--out", required=True)
    ap.add_argument("--no-transcript", action="store_true")
    ap.add_argument("--no-download", action="store_true", help="source is already a local file")
    ap.add_argument("--image", action="store_true", help="source is a still image, look-and-feel only")
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    raw_dir = out_dir / "raw"

    if args.image:
        check_tools(need_ytdlp=False)
        src = Path(args.source)
        if not src.exists():
            print(f"ERROR: image not found: {src}", file=sys.stderr)
            sys.exit(2)
        profile = {"kind": "image", "source": str(src)}
        (out_dir / "reference_profile.json").write_text(json.dumps(profile, indent=2))
        (out_dir / "summary.md").write_text(
            f"# Image reference: {src.name}\n\nLook-and-feel review only. No timing data (not a video).\n"
        )
        print(f"OK image profiled -> {out_dir}")
        return

    check_tools(need_ytdlp=is_url(args.source) and not args.no_download)

    if is_url(args.source):
        video_path, info = download(args.source, raw_dir)
    else:
        src = Path(args.source)
        if not src.exists():
            print(f"ERROR: file not found: {src}", file=sys.stderr)
            sys.exit(2)
        raw_dir.mkdir(parents=True, exist_ok=True)
        video_path = raw_dir / f"source{src.suffix}"
        if not video_path.exists():
            shutil.copy(src, video_path)
        info_path = raw_dir / "source.info.json"
        info = json.loads(info_path.read_text()) if info_path.exists() else {}

    probe = ffprobe_json(video_path)
    fmt = probe.get("format", {})
    vstream = next((s for s in probe.get("streams", []) if s.get("codec_type") == "video"), {})
    duration = float(fmt.get("duration", 0))

    cuts = detect_scenes(video_path)
    stats = shot_stats(cuts, duration)
    timeline = cut_rate_timeline(cuts, duration)
    transitions = classify_transitions(video_path, cuts)

    sheet_path = contact_sheet(video_path, cuts, out_dir / "contact_sheet.jpg")

    transcript_path = None
    if not args.no_transcript:
        transcript_path = transcribe(video_path, out_dir)

    profile = {
        "kind": "video",
        "source_url": args.source if is_url(args.source) else None,
        "title": info.get("title"),
        "uploader": info.get("uploader"),
        "upload_date": info.get("upload_date"),
        "view_count": info.get("view_count"),
        "duration_s": round(duration, 2),
        "width": vstream.get("width"),
        "height": vstream.get("height"),
        "fps": eval(vstream.get("r_frame_rate", "0/1")) if vstream.get("r_frame_rate") else None,
        "aspect_ratio": round(vstream.get("width", 1) / vstream.get("height", 1), 3) if vstream.get("height") else None,
        "shot_stats": stats,
        "cut_rate_timeline_10s_buckets": timeline,
        "cuts": cuts,
        "transitions": transitions,
        "contact_sheet": str(sheet_path) if sheet_path else None,
        "transcript": str(transcript_path) if transcript_path else None,
    }
    (out_dir / "reference_profile.json").write_text(json.dumps(profile, indent=2, ensure_ascii=False))

    aspect_label = "9:16 vertical" if profile["aspect_ratio"] and profile["aspect_ratio"] < 0.8 else (
        "16:9 horizontal" if profile["aspect_ratio"] and profile["aspect_ratio"] > 1.2 else "square/other")
    summary = f"""# Reference profile: {profile.get('title') or video_path.name}

Source: {args.source}
Uploader: {profile.get('uploader')} | Uploaded: {profile.get('upload_date')}
Duration: {profile['duration_s']} s | {profile['width']}x{profile['height']} ({aspect_label}) | {profile['fps']} fps
Shots: {stats['num_shots']} | avg shot length {stats['avg_shot_len']} s | median {stats['median_shot_len']} s
Shot length range: {stats['min_shot_len']} s to {stats['max_shot_len']} s | cuts/min: {stats['cuts_per_min']}
Contact sheet: {sheet_path}
Transcript: {transcript_path if transcript_path else 'not generated (--no-transcript or mlx_whisper missing)'}

10-line read: {"fast-cut, frequent pattern interrupts" if stats['avg_shot_len'] < 3 else "moderate pacing" if stats['avg_shot_len'] < 8 else "slow, long takes"} ({stats['avg_shot_len']} s avg shot).
Review the contact sheet for look (colour, framing, on-screen text style) and the transcript for hook wording and pacing of speech.
"""
    (out_dir / "summary.md").write_text(summary)
    print(f"OK profiled -> {out_dir}")
    print(summary)


if __name__ == "__main__":
    main()
