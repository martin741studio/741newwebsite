---
name: video-edit
description: Edits Martin's raw footage (talking-head, screen recording, b-roll, phone clips) or a script/voiceover into a finished video in the style of a reference he gives (a YouTube/Instagram/TikTok link, or screenshots for look-and-feel only). Profiles the reference (cuts, shot length, transitions, caption style) with scripts/reference_profile.py, drafts and shows an edit plan (kept spans, hook, pacing) for Martin's go, renders a frame-accurate cut, burns word-highlight captions, applies look and loudness, and exports (9:16 short-form first, 16:9 long-form second) for Martin to finish in CapCut. Two mandatory checkpoints: the edit plan before any render, the export before calling the job done. Never uploads or posts. Use when Martin says "/video-edit", "edit this clip", "cut this into a reel/short", "make this talking-head footage into a video", "re-cut this video into shorts", or pastes raw footage plus a reference link/screenshot. NOT for writing the daily on-screen caption TEXT from a thought dump with no video file involved (that is the `captions` skill) and NOT for video-content ideas or concept stills with no footage to cut (that is `content-format-board`).
disable-model-invocation: false
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(python3:*), Bash(ffmpeg:*), Bash(ffprobe:*), Bash(yt-dlp:*), Bash(mlx_whisper:*), Bash(ls:*), Bash(cat:*), Bash(du:*), AskUserQuestion
---

# Video edit (workflow id `video-edit`)

Replies in STE except the why-these-choices note, which may use normal prose.

## Critical

- **Two checkpoints, no skip.** The edit plan (step 4) before any rendering — padding and span choice are expensive to undo once captions and look are layered on top. The export (step 7) before telling Martin the job is done. Never render past a checkpoint without his go.
- **No libass, no drawtext on this Mac.** Captions are PNG word-highlight overlays via Pillow (`caption_render.py`), composited with ffmpeg `overlay`. Never try `subtitles=`/`ass=`/`drawtext=` filters — they are confirmed missing (`_derived/video-edit-rules.md` R-TOOL.2).
- **Captions drift after any cut.** If step 5 cut anything, run `remap_words.py` before burning captions — the raw transcript's timestamps no longer match the cut video (R-CAP.4). Skip only for a no-cut styling-only job.
- **Frame accuracy matters.** Read the raw clip's real fps with ffprobe before building anything. Use `-fps_mode passthrough`, never `-r`, when rendering a concat — forcing the rate silently duplicates frames at cut points (R-BUILD.3). Verify the rendered output's duration against the cut plan before calling a cut done (R-BUILD.4).
- **Never feed a render into the next step before its own completion notification arrives.** An ffmpeg output file exists and grows on disk long before it is done — `ls`/`ffprobe` finding it proves nothing (R-BUILD.5). Wait for the actual background-task completion event.
- **Never upload or publish.** This skill writes video files only. Martin opens the export in CapCut himself. Every export is a new file; raw footage is never overwritten.
- **mlx_whisper's first run on a new cache downloads the model** (~1.5GB, several minutes over Hugging Face's "xet" backend). If it looks stuck, check `~/.cache/huggingface/xet/logs/xet_*.log` for an active transfer — never `du -sh` the blobs folder (misleading for xet) and never delete `.incomplete` files to "fix" an apparent hang (R-TOOL.5).
- **Always end with the disclosure.** State plainly what this run did not do (cut points are word-timestamp-plus-pad so some may still clip/trail a word; no NLE live-trim; nothing checked against the waveform) — every time, in the why-these-choices note, not only if asked (R-PROCESS.2).
- Any new paid API (ElevenLabs, a music subscription) or any `brew`/`pip` install beyond what is already in this skill needs a card first.

## Inputs (Martin gives)

- Raw footage (a file path) or a script/voiceover to work from.
- One or more references: a link (YouTube/Instagram/TikTok — gives timing data) or screenshots/clips (look-and-feel only, no cut-rate data).
- The message and the platform (which decides aspect ratio — 9:16 first, 16:9 second if both are wanted).

## Workflow

Copy this checklist into the reply and tick it off:

```
Video edit <slug>:
- [ ] 1 run folder: 00_project/assets/<client-or-741>/video-edit/<date>-<slug>/raw+reference/
- [ ] 2 reference profile (skip if already in 00_project/knowledge/video-editing-library/references/)
- [ ] 3 transcribe the raw footage (mlx_whisper, word-level)
- [ ] 4 edit plan: draft kept spans, build_cut_plan.py → cuts.json
- [ ] CHECKPOINT: show the cut plan, wait for go
- [ ] 5 rough cut: render_cut.py (verified against the plan)
- [ ] 6 captions + look: caption_render.py, 9:16 pad if needed, loudnorm
- [ ] 7 export: ffmpeg final encode per references/export-specs.md
- [ ] CHECKPOINT: show the export + why-these-choices.md, wait for go/notes
```

**Step 1: run folder.** `00_project/assets/<client-or-741>/video-edit/<YYYY-MM-DD>-<slug>/` with `raw/` (copy Martin's footage in, never edit in place) and `reference/`. `<client-or-741>` is `741` for Martin's own videos.

**Step 2: reference profile.** Check `00_project/knowledge/video-editing-library/references/` first — a reference already profiled is reused, never re-downloaded. New reference:
```bash
python3 .claude/skills/video-edit/scripts/reference_profile.py "<url>" --out <run>/reference
```
For a screenshot/still image: add `--image` (look-and-feel only, no timing). Read `summary.md` and look at `contact_sheet.jpg` before drafting the edit plan — the pacing target comes from the reference's own measured shot length, not a guess (`degrees-of-freedom.md`).

**Step 3: transcribe.** 
```bash
/Users/martindrendel/.local/bin/mlx_whisper <run>/raw/clip.mp4 --model mlx-community/whisper-large-v3-turbo --word-timestamps True --output-format json --output-dir <run>/transcript --output-name words
```

**Step 4: edit plan.** If Martin only asked for styling/captions on an already-good take (no cutting requested), skip straight to step 6 on the raw clip — don't force a cuts.json for a job with no cuts. Otherwise: read `<run>/transcript/words.json`. Draft kept spans per `_derived/video-edit-rules.md` R-CUT.1 (cut filler/dead air/false starts; a repeated line keeps its best complete take, usually the last). Write `<run>/transcript/spans.json` as `[{"start":..,"end":..,"text":"..."}]`, then:
```bash
python3 .claude/skills/video-edit/scripts/build_cut_plan.py <run>/transcript/words.json <run>/transcript/spans.json --video <run>/raw/clip.mp4 --out <run>/transcript/cuts.json
```
A `build_cut_plan.py` exit 2 means two spans are too close to pad — revise `spans.json` and rerun. **Show the printed span list to Martin as the checkpoint.** Wait for his go or his changes before step 5.

**Step 5: rough cut.**
```bash
python3 .claude/skills/video-edit/scripts/render_cut.py <run>/transcript/cuts.json --out <run>/rough_cut.mp4
```
Exit 4 means the rendered duration drifted from the plan by more than 0.15s — investigate before continuing (never ship an unverified cut).

**Step 6: captions and look, in this order.**
1. If any cutting happened in step 5, remap the transcript onto the cut's timeline first (R-CAP.4). Captions burned straight from the raw transcript drift out of sync after a cut:
```bash
python3 .claude/skills/video-edit/scripts/remap_words.py <run>/transcript/words.json <run>/transcript/cuts.json --out <run>/transcript/words_cut.json
```
Skip this for a no-cut styling-only job — `words.json` already matches the raw clip's timeline.

2. If the source is 16:9 and the target is 9:16, pad with a blurred background **before** the caption burn (ffmpeg command in `references/ffmpeg-cookbook.md` §9:16-pad) — captions are drawn in the final frame's coordinates.

3. Draft caption line wording per R-CAP.1/.2 (word groups, hook wording) from the transcript, then burn captions onto the padded clip (use `words_cut.json` if step 6.1 ran, otherwise `words.json`):
```bash
python3 .claude/skills/video-edit/scripts/caption_render.py <run>/transcript/words_cut.json --video <run>/padded_916.mp4 --out <run>/captioned.mp4 --w 1080 --h 1920
```

4. Apply loudnorm two-pass (`references/ffmpeg-cookbook.md` §loudness — note the TP=-1.5 and `-shortest` details there) to the final audio.

**Step 7: export.** Encode to the platform's spec (`references/export-specs.md`: 1080x1920 H.264 MP4 for short-form; the verified YouTube bitrate table for 16:9 long-form). Write `<run>/why-these-choices.md`: hook choice, pacing target and why, caption style, look, plus the mandatory disclosure (R-PROCESS.2). **Show the export and the note. Wait for Martin's go or notes** — notes loop back to step 4 (new spans) or step 6 (look/caption only), never a silent re-render.

## Verification

Before reporting a job done: `render_cut.py`'s own duration check must have printed `OK rendered and verified`, and the final export must exist and be non-empty (`ls -la <run>/export/*.mp4`). Report the file path and the why-these-choices note together — never one without the other.
