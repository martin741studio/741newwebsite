# Degrees of freedom — video-edit (Rule R1.7)

## Low freedom (exact script, no parameters)

- **Scene detection** on the reference — `reference_profile.py`, `scenedetect.detect(path, ContentDetector())`. Deterministic.
- **Cut-plan padding/snapping/overlap-resolution** — `build_cut_plan.py`. Fixed padding values (0.08s/0.12s), fixed overlap rule (split the gap). Exact math, no judgement.
- **Render + verify** — `render_cut.py`. Fixed filtergraph shape, fixed `-fps_mode passthrough` rule, fixed post-render duration check. No judgement calls.
- **Caption PNG rendering** — `caption_render.py`. Fixed style constants (font, stroke width, position) unless Martin asks for a different look; the word-timing source is the transcript, not a guess.
- **Loudness normalisation** — ffmpeg two-pass `loudnorm`, fixed target values from R-EXPORT.3.
- **Export encode settings** — fixed per platform from R-EXPORT.1/.2 (resolution, codec, bitrate range).

## High freedom (heuristics, prompt judgement, 2-3 examples to anchor)

- **Which spans to keep** from the raw footage (cut filler/false starts, pick the best take of a repeated line) — qualitative, reads the transcript and Martin's stated message.
- **Hook choice** (first 1-2 seconds) — reads the reference's own hook (from its transcript + first shot in the contact sheet) and Martin's message, proposes a hook line/visual, not a formula.
- **Caption line grouping and wording** (not the burn-in mechanics, the actual word grouping and which words to highlight) — judgement call per clip, anchored to R-CAP.1/.2 as defaults, not a rigid rule.
- **Pacing target** (how fast to cut) — anchored to the reference's own measured avg-shot-length (`reference_profile.json`), not a fixed number; R-CUT.4's "3-5s" is a fallback only when no reference pacing data exists.
- **Look/colour choice** — reviewed from the reference's contact sheet, described in words (e.g. "clean and bright" vs "teal-orange"), not auto-applied from a fixed LUT list (no verified LUT taxonomy exists per R-002 gap).

## Why this split

Everything that is "fragile or must run in exact order" (frame math, padding, concat, verification) is a script — a wrong heuristic here silently breaks sync or duplicates frames (R-BUILD.3). Everything that is "many valid approaches" (what footage is worth keeping, what hook lands, how a caption reads) stays a judgement call Claude makes and Martin reviews at the two checkpoints — forcing these into a rigid script would make the output generic and remove the point of having Claude do the edit.
