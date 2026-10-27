# Functional test — video-edit (step 4.2, fresh session, real task)

**Date:** 2026-10-27. A fresh agent (no context of this build) was given a real 15s clip and told to follow `.claude/skills/video-edit/SKILL.md` exactly: cut the clip's meta-commentary opening, burn bottom captions, export 9:16. Not a dry run — it did the real work end to end.

## What it found, unprompted
All 4 scripts exited 0 and passed their own checks, but the agent surfaced 7 real defects a clean exit code didn't catch:

1. **Caption/cut desync (the big one):** captions burned straight from the raw transcript onto a CUT video drift up to 1.3s out of sync — the skill doc never had a step to remap word times onto the cut's shorter timeline.
2. Step 6's write-up didn't say padding-before-caption clearly enough — the agent had to infer the order.
3. The default bottom caption position (`h*0.78`) sits inside our own `bottom 400px` safe-zone rule (R-CAP.3) — self-contradicting.
4. `build_cut_plan.py` didn't clamp a span's end time to the source's real duration.
5. `render_cut.py` only ever checked duration, not frame count, despite having an unused frame-count function.
6. loudnorm at TP=-1 overshoots to about -0.87 dBTP after encoding — misses the -1 dBTP ceiling.
7. loudnorm's output audio can end up longer than the video (needs `-shortest`); mlx_whisper can return a zero-length word, which would never show as a caption highlight.

## Fixes made (same day)
- New script `scripts/remap_words.py` — remaps source-timeline words onto the cut's output timeline; dropped if they fall in a cut gap. Wired into SKILL.md step 6 as a required sub-step whenever cutting happened (R-CAP.4, new rule).
- SKILL.md step 6 rewritten as an explicit ordered sub-list: remap (if cut) → pad to 9:16 → caption burn → loudnorm.
- `caption_render.py`: bottom position now computed directly off the safe-zone margin instead of a fixed fraction; added a 0.12s minimum word duration guard.
- `build_cut_plan.py`: clamps span end times to the source's real ffprobe duration.
- `render_cut.py`: verification output now also reports frame count (informational, not a hard gate — small rounding diffs are normal).
- `ffmpeg-cookbook.md`: loudnorm pass 2 now specifies TP=-1.5 (not -1) to actually land at/under -1 dBTP, and adds `-shortest` to the export command.

## Re-verification (same clip, fixed scripts)
Re-ran `build_cut_plan.py` → `render_cut.py` → `remap_words.py` → `caption_render.py` on the same real clip and transcript:
- Cut plan clamped correctly to the source's 15.02s (no more overshoot).
- `render_cut.py` now prints frame counts: 685 rendered vs ~686 expected (−1, within normal rounding) alongside the duration check.
- `remap_words.py`: 42/42 words remapped cleanly.
- Caption frame grabbed at the "jetzt" word's exact timestamp (2.15s) shows it correctly highlighted in yellow, in sync, sitting with clear margin above the bottom edge (no longer clipped off-frame, which an initial dimension-mismatch test — captioning a 16:9 clip with 9:16-sized overlays, before padding — had shown; fixed by confirming the documented pad-before-caption order).

Artifacts: `00_project/workflow-builds/video-edit/functional-test/` (`captioned_v3.mp4`, `verify_frame3.jpg`).

## Verdict
Real, substantive defects found and fixed before this ever reaches Martin on a real job — exactly what this step is for. The skill's documented pipeline, as it now stands, was followed start to finish without further guesswork by either the test agent or the fixes.
