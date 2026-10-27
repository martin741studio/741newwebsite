#!/usr/bin/env python3
"""Turn a word-level transcript + a list of kept spans into a frame-accurate,
non-overlapping, padded cut plan (cuts.json). Padding and no-overlap rules
follow 00_project/knowledge/video-editing-library/sources/003-claude-video-
editor-starter-pattern.md: ~0.08s before the first word, ~0.12s after the
last word of each kept span, never reaching into a cut word; when two padded
spans would overlap, the gap between them is split instead.

This script does NOT decide what to keep — that is a qualitative judgement
(cut filler/dead air/false starts, keep the best complete take of a repeated
line) made by Claude reading transcript.json and writing a draft spans list.
This script only pads, deduplicates, snaps to frames, and validates.

Usage:
  build_cut_plan.py <transcript.json> <spans.json> --video <raw.mp4> --out <cuts.json>

spans.json: [{"start": 1.24, "end": 4.60, "text": "..."}]  (unpadded, in source-clip seconds)

Exit codes: 0 ok, 2 bad input (e.g. a span could not fit after padding).
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

PAD_BEFORE = 0.08
PAD_AFTER = 0.12


def ffprobe_fps(video_path):
    out = subprocess.run(
        ["ffprobe", "-v", "quiet", "-select_streams", "v:0", "-show_entries",
         "stream=r_frame_rate", "-of", "csv=p=0", str(video_path)],
        capture_output=True, text=True, check=True,
    )
    num, den = out.stdout.strip().split("/")
    return float(num) / float(den)


def ffprobe_duration(video_path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(video_path)],
        capture_output=True, text=True, check=True,
    )
    return float(out.stdout.strip())


def snap(t, fps):
    return round(round(t * fps) / fps, 4)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript")
    ap.add_argument("spans")
    ap.add_argument("--video", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--pad-before", type=float, default=PAD_BEFORE)
    ap.add_argument("--pad-after", type=float, default=PAD_AFTER)
    args = ap.parse_args()

    spans = json.loads(Path(args.spans).read_text())
    if not spans:
        print("ERROR: no spans given", file=sys.stderr)
        sys.exit(2)

    fps = ffprobe_fps(args.video)
    source_duration = ffprobe_duration(args.video)
    spans = sorted(spans, key=lambda s: s["start"])

    padded = []
    for s in spans:
        start = max(0.0, s["start"] - args.pad_before)
        # Clamp to the source's real duration — a transcript end time can run
        # a little past the actual last frame (found 2026-10-27, functional test).
        end = min(s["end"] + args.pad_after, source_duration)
        padded.append({"start": start, "end": end, "text": s.get("text", "")})

    # resolve overlaps by splitting the gap between the two original (unpadded) boundaries
    for i in range(1, len(padded)):
        prev, cur = padded[i - 1], padded[i]
        if cur["start"] < prev["end"]:
            mid = (spans[i - 1]["end"] + spans[i]["start"]) / 2
            prev["end"] = min(prev["end"], mid)
            cur["start"] = max(cur["start"], mid)
            if prev["end"] <= spans[i - 1]["start"] or cur["start"] >= spans[i]["end"]:
                print(f"ERROR: spans {i-1} and {i} are too close to pad without cutting into a kept word", file=sys.stderr)
                sys.exit(2)

    cuts = []
    for p in padded:
        cuts.append({"start": snap(p["start"], fps), "end": snap(p["end"], fps), "text": p["text"]})

    total = round(sum(c["end"] - c["start"] for c in cuts), 3)
    plan = {"fps": fps, "source": str(args.video), "segments": cuts,
            "num_segments": len(cuts), "total_duration_s": total}
    Path(args.out).write_text(json.dumps(plan, indent=2, ensure_ascii=False))
    print(f"OK cut plan written -> {args.out} ({len(cuts)} segments, {total}s total, {fps} fps)")
    for i, c in enumerate(cuts):
        print(f"  {i+1}. {c['start']:.2f}-{c['end']:.2f}s  \"{c['text'][:60]}\"")


if __name__ == "__main__":
    main()
