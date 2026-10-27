# Hand-run — video-edit step 2.3

**Date:** 2026-10-27
**Task:** Martin's own clip, real request in chat (not a staged test).

## Input
- Raw footage: `/Users/martindrendel/Movies/CapCut/User Data/Cloud files/C0929.MP4` — 1920x1080, 50fps, 183.36s, talking-head, German.
- Reference: a screenshot (pasted image), look-and-feel only — white rounded title badge top, word-highlight captions center-center, yellow active word. No timing data (not a link).
- Martin's instruction (verbatim): "dieses video bitte so einstellen und captions drauf (whisper) das es am ende so aussieht wie auf dem bild hier title on top, caption center center. the play button nich integrieren"

## Reading the request
No cut instruction was given — Martin asked to style and caption the clip as a whole, not re-cut it. Treated as a styling+captions job: keep the full clip, no span editing. This is a real variation the skill's workflow didn't explicitly cover (it assumes a cut plan exists) — the fix is noted below.

"Play button nicht integrieren" meant: the reference screenshot shows a paused-video play icon (platform UI chrome, not part of the edit) — don't render a fake play icon into the output.

## Steps actually run
1. Run folder: `00_project/assets/741/video-edit/2026-10-27-c0929-captions/`.
2. Transcribed with mlx_whisper (word-level) — model already cached from reference 1's run, finished in well under a minute for a 183s clip.
3. Title text was not given — derived 3 candidate titles from the transcript's own opening line and thesis, asked Martin via a card, got "Die gefährlichste Marketing-Aussage".
4. Found `caption_render.py` had no title-badge capability (only word-highlight captions) — added `--title` support (white rounded-rect badge, Georgia Bold, wraps to fit, full-duration overlay) rather than building a one-off script.
5. 9:16 pad (blurred background) applied first, since the source is 16:9 and the reference is vertical — Martin didn't say 9:16 explicitly but the reference image is vertical, so this was read from the image, not asked as a separate question.

## Friction for the workflow write-up
- The skill's step 4 (edit plan / cuts.json) assumes cutting is always needed. A no-cut styling job should skip straight from step 3 (transcribe) to step 6 (captions/look) — SKILL.md needs a line making this explicit so a future run doesn't force an unnecessary cut plan.
- `caption_render.py` only did bottom/center word captions, no title badge — now extended. This should be documented as a permanent capability, not a one-off hack.

## More friction found running it for real
- A first ffmpeg render (`bye016xzr`, the 9:16 blur pad) was still writing when I checked it with `ls`/`ffprobe` instead of waiting for its completion notification — the file existed and had a plausible size, but the moov atom wasn't written yet. Fed into the next step, it failed. Fix: wait for the actual background-task notification, never treat file existence as done — documented as R-BUILD.5.
- First caption render used 4 words/line at font-size 64 on a 1080px frame — German compound words ("abzulesen", "Marketing-Aussage") overflowed both edges on long words. Fixed by making `group_lines()` width-aware (measures rendered text width incl. stroke, breaks before it would overflow 90% of frame width), not just word-count-based. This is now a permanent capability of `caption_render.py`, not a one-off patch.
- Added `--title` support to `caption_render.py` (white rounded-rect badge, wraps to fit, full-duration overlay) since the reference needed a static title card and the script only did word captions before.

## Outcome
Export delivered: `00_project/assets/741/video-edit/2026-10-27-c0929-captions/export/c0929_captioned_9x16.mp4` (1080x1920, 183.4s, -14 LUFS). Shown to Martin for his go (checkpoint 2).

## Pipeline change this run surfaced
Step 4 (edit plan / cuts.json) should be explicitly skippable when no cutting is requested — a styling+captions-only job goes straight from transcribe (step 3) to captions/look (step 6). SKILL.md step 7 workflow text should say this rather than imply every job needs a cut plan.
