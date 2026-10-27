#!/usr/bin/env python3
"""Remap a source-timeline word transcript onto a cut output's timeline.

render_cut.py concatenates the kept segments from cuts.json into a new,
shorter video — every word after the first kept segment now sits earlier
than its original timestamp. Burning captions straight from the source
transcript (words.json) onto that cut video drifts more and more as the
cut goes on (found 2026-10-27, functional test: up to 1.3s drift). Always
run this between render_cut.py and caption_render.py whenever ANY cutting
was done; skip it only for a no-cut (styling-only) job, where the raw
transcript already matches the raw (uncut) video's timeline.

A word is kept only if it falls (by its midpoint) inside a kept segment —
words in a cut gap are dropped, matching what the viewer actually sees.

Usage:
  remap_words.py <words.json> <cuts.json> --out <words_cut.json>

Exit codes: 0 ok, 2 bad input.
"""
import argparse
import json
import sys
from pathlib import Path


def load_words(transcript_path):
    data = json.loads(Path(transcript_path).read_text())
    words = []
    for seg in data.get("segments", []):
        for w in seg.get("words", []):
            text = (w.get("word") or w.get("text") or "").strip()
            if not text:
                continue
            words.append({"text": text, "start": w["start"], "end": w["end"]})
    return words


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript")
    ap.add_argument("cuts")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    words = load_words(args.transcript)
    cuts = json.loads(Path(args.cuts).read_text())
    segments = cuts.get("segments", [])
    if not words or not segments:
        print("ERROR: empty words or empty cuts segments", file=sys.stderr)
        sys.exit(2)

    out_words = []
    cumulative = 0.0
    for seg in segments:
        seg_start, seg_end = seg["start"], seg["end"]
        for w in words:
            mid = (w["start"] + w["end"]) / 2
            if seg_start <= mid < seg_end:
                new_start = max(0.0, w["start"] - seg_start) + cumulative
                new_end = min(w["end"], seg_end) - seg_start + cumulative
                out_words.append({"text": w["text"], "start": round(new_start, 3), "end": round(max(new_end, new_start + 0.01), 3)})
        cumulative += seg_end - seg_start

    out = {"segments": [{"words": out_words}]}
    Path(args.out).write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"OK remapped {len(out_words)}/{len(words)} words -> {args.out} (cut-output timeline, {cumulative:.2f}s)")


if __name__ == "__main__":
    main()
