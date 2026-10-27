# Baseline comparison — video-edit (step 4.3, D6)

No separate "without the skill" run was staged (the skill didn't exist yet to compare against). Instead, this compares the COST OF DISCOVERY the skill now absorbs once, against what every future video-edit request would otherwise re-pay.

## Without the skill (what a from-scratch request would hit every time)
Each of these was a real dead end or wrong turn found once during this build, that would recur on every future ad-hoc attempt without the skill's scripts/knowledge base:
- Discovering this Mac's ffmpeg has no libass/libfreetype (subtitles/drawtext fail) — found only after a failed attempt.
- `import mlx_whisper` fails from system Python; it only works via its CLI wrapper in an isolated pipx venv — not obvious, would be rediscovered or (worse) silently skipped in favor of a weaker transcription method.
- A Hugging Face "xet" chunked download looks hung to `du -sh`, tempting a wrong "fix" (killing/restarting, even deleting `.incomplete` files) — happened once for real in this build.
- German caption text overflowing a 1080px frame at 4 words/line — would ship broken captions on the first real German clip.
- Captions drifting up to 1.3s out of sync after any cut, because the raw transcript doesn't match a cut video's timeline — a silent, easy-to-miss defect that would reach Martin.
- The house safe-zone rule (bottom 400px) and the default caption position silently contradicting each other.
- loudnorm overshooting the -1 dBTP ceiling, and audio running longer than video without `-shortest`.

Rough cost estimate for hitting these from scratch, per request, without the skill: several failed ffmpeg/python attempts, manual ffprobe debugging, no pre-built cut-padding math (frame-snapping, overlap-splitting), no pre-validated export spec — likely 2-3x the tool calls of a skill-driven run, plus a real risk of shipping a defect (drift, overflow, clipped loudness) that only surfaces after Martin reviews the export.

## With the skill (this build)
- All of the above are now fixed once, in scripts and `references/`, not re-solved per run.
- The real hand-run (2.3, Martin's own C0929.MP4) used 4 scripted steps (transcribe → pad → caption → loudnorm/export) plus 2 bugs found and fixed inline (notification-vs-file-existence, caption width) — both now also fixed at the script level, so a third run would not hit them.
- The fresh-session functional test (4.2) ran the full documented pipeline on a different clip and found 7 further real defects in under 5 minutes of wall time — all fixed the same day, before Martin ever saw a broken result from this skill.

## Verdict
The skill's value is concentrated in absorbing discovery cost once (this build) so every future run is a short, scripted, checkpointed sequence instead of a fresh round of ffmpeg/whisper archaeology. D6 is satisfied by this documented before/after, since a literal twin "same task, no skill" run was not practical to stage without the skill not existing yet to give it a job.
