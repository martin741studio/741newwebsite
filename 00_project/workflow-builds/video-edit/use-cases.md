# Use cases — video-edit

## Use case 1: Talking-head clip → 9:16 reel with animated captions
**Trigger:** "edit this into a reel", "/video-edit", "cut this talking-head clip in the style of [reference]".
**Steps:** resolve run folder → profile the reference (if new) → transcribe the raw clip (mlx_whisper) → Claude reads the transcript and drafts kept spans (cut filler/false starts/best-take-of-repeats) → `build_cut_plan.py` pads+snaps+validates → **checkpoint: show cut plan, wait for go** → `render_cut.py` renders+verifies the rough cut → Claude designs caption lines from the transcript (word groups, hook wording) → `caption_render.py` burns captions → 9:16 crop/pad (blurred background if source is 16:9) → loudnorm two-pass → export → **checkpoint: show the export + why-these-choices note, wait for go/notes**.
**Tools:** ffmpeg, PySceneDetect (on the reference only), mlx_whisper, Pillow.
**Deliverable:** one `export/short_9x16.mp4`, `why-these-choices.md`, the cut plan and transcript kept for iteration.

## Use case 2: Screen recording walkthrough → 60-second explainer
**Trigger:** "turn this screen recording into a short explainer", "cut my walkthrough down to a minute".
**Steps:** profile the reference for pacing (screen-recording references usually have fewer, longer shots — pattern interrupts come from zoom/highlight overlays, not cuts) → transcribe the voiceover → Claude drafts kept spans prioritising the 2-3 moments that answer the stated message, cutting dead air and redundant explanation → `build_cut_plan.py` → **checkpoint** → `render_cut.py` → optional zoom-pan on key screen regions (ffmpeg `zoompan`) → captions (screen-recording voiceover is usually clearer audio, captions can be sparser) → 16:9 or 9:16 per platform asked → loudnorm → export → **checkpoint**.
**Tools:** same as use case 1, plus `zoompan` for screen emphasis.
**Deliverable:** one export at the requested aspect ratio, why-these-choices note.

## Use case 3: Re-cut an existing long video into 3 shorts
**Trigger:** "cut 3 shorts out of this video", "pull the best moments from [long video] into shorts".
**Steps:** profile the long source for shot/pacing structure → transcribe the full source once (reused across all 3 cuts) → Claude identifies 3 self-contained moments (each needs its own hook-worthy opening line) and drafts 3 separate span lists → `build_cut_plan.py` run 3 times (one per short) → **checkpoint: show all 3 cut plans together** → render all 3 → captions + 9:16 export for each → **checkpoint: show all 3 exports together**.
**Tools:** same stack, run per-short.
**Deliverable:** 3 exports, one combined why-these-choices note covering all 3 selections.

## Must-not-trigger cases (negative scenarios, confirmed before the body)

1. **"Write the captions for today's video"** (daily voiceless YouTube caption text from a thought dump) → this is the `captions` skill's job, not `video-edit`. `video-edit` burns captions onto an already-cut video; it does not write the daily dump-to-caption-text pipeline.
2. **"Build a thumbnail for this video" / "make a social image template"** → thumbnails (`youtube-thumbnail-workflow`) and static image templates (`social-visuals-workflow`, `personal-posts`) are not `video-edit`. No video file is involved in either.
3. **"Give me video content ideas for [client]"** → that is `content-format-board` (ideas + concept stills), not editing an actual footage file.
