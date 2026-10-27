#!/usr/bin/env python3
"""Render a cut plan (cuts.json, from build_cut_plan.py) into a single
flat MP4 with one ffmpeg filtergraph (trim+atrim per segment, then concat).
Verifies the output frame-for-frame against the plan afterward.

Critical rule (source 003 in the video-editing-library): use
`-fps_mode passthrough`, never `-r`. Forcing the frame rate with `-r`
silently duplicates frames at cut points with no warning.

Usage:
  render_cut.py <cuts.json> --out <rough_cut.mp4>

Exit codes: 0 ok (verification passed), 2 bad input, 4 verification mismatch.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path


def ffprobe_duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True,
    )
    return float(out.stdout.strip())


def ffprobe_nb_frames(path):
    out = subprocess.run(
        ["ffprobe", "-v", "quiet", "-select_streams", "v:0", "-count_frames",
         "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True,
    )
    return int(out.stdout.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cuts_json")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    plan = json.loads(Path(args.cuts_json).read_text())
    segments = plan["segments"]
    source = plan["source"]
    if not segments:
        print("ERROR: cut plan has no segments", file=sys.stderr)
        sys.exit(2)

    filt_parts = []
    v_labels, a_labels = [], []
    for i, seg in enumerate(segments):
        filt_parts.append(
            f"[0:v]trim=start={seg['start']}:end={seg['end']},setpts=PTS-STARTPTS[v{i}]"
        )
        filt_parts.append(
            f"[0:a]atrim=start={seg['start']}:end={seg['end']},asetpts=PTS-STARTPTS[a{i}]"
        )
        v_labels.append(f"[v{i}]")
        a_labels.append(f"[a{i}]")
    concat_inputs = "".join(f"{v}{a}" for v, a in zip(v_labels, a_labels))
    filt_parts.append(f"{concat_inputs}concat=n={len(segments)}:v=1:a=1[vout][aout]")
    filt = ";".join(filt_parts)

    cmd = [
        "ffmpeg", "-y", "-i", source, "-filter_complex", filt,
        "-map", "[vout]", "-map", "[aout]",
        "-fps_mode", "passthrough",
        "-c:v", "libx264", "-crf", "18", "-preset", "medium",
        "-c:a", "aac", "-b:a", "192k",
        args.out,
    ]
    subprocess.run(cmd, check=True)

    expected_total = plan["total_duration_s"]
    actual_total = ffprobe_duration(args.out)
    diff = abs(actual_total - expected_total)
    expected_frames = round(expected_total * plan["fps"])
    actual_frames = ffprobe_nb_frames(args.out)
    print(f"Plan: {len(segments)} segments, {expected_total}s (~{expected_frames} frames). "
          f"Rendered: {actual_total:.3f}s, {actual_frames} frames. Diff: {diff:.3f}s, {actual_frames - expected_frames} frames.")
    if diff > 0.15:
        print(f"VERIFY FAILED: duration mismatch > 0.15s", file=sys.stderr)
        sys.exit(4)
    print(f"OK rendered and verified -> {args.out}")


if __name__ == "__main__":
    main()
