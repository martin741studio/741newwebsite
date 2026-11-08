---
name: video-edit
description: Edits Martin's raw footage or a script/voiceover into a finished video in the style of a reference he gives (video link or screenshots). Shows an edit plan for his go, renders a frame-accurate cut with word-highlight captions, exports 9:16 first, 16:9 second, for CapCut. Never uploads. Use on "/video-edit", "edit this clip", "cut this into a reel/short", "re-cut this video into shorts". Not for caption text without a video (captions).
disable-model-invocation: false
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(python3:*), Bash(ffmpeg:*), Bash(ffprobe:*), Bash(yt-dlp:*), Bash(mlx_whisper:*), Bash(ls:*), Bash(cat:*), Bash(du:*), AskUserQuestion
---

# Video edit (workflow id `video-edit`)

Replies in STE except the why-these-choices note (normal prose allowed). Rules R-xxx live in `00_project/knowledge/video-editing-library/_derived/video-edit-rules.md`. Pacing and judgment latitude: `00_project/workflow-builds/video-edit/degrees-of-freedom.md`. Commands: `references/ffmpeg-cookbook.md`, `references/export-specs.md`.

## Critical

- **Two checkpoints, no skip.** The edit plan (step 4) before any render. The export (step 7) before saying the job is done. Never render past a checkpoint without his go.
- **No libass, no drawtext on this Mac.** Captions are PNG word-highlight overlays via Pillow (`caption_render.py`) composited with ffmpeg `overlay`. Never `subtitles=`, `ass=` or `drawtext=` (R-TOOL.2).
- **Captions drift after any cut.** After a cut, run `remap_words.py` before burning captions (R-CAP.4). Skip only for a no-cut styling job.
- **Frame accuracy.** Read the raw fps with ffprobe first. Concat renders use `-fps_mode passthrough`, never `-r` (R-BUILD.3). Check the rendered duration against the cut plan (R-BUILD.4).
- **Wait for the render's completion notification** before feeding it into the next step. A growing output file proves nothing (R-BUILD.5).
- **Never upload or publish.** Video files only; Martin opens the export in CapCut. Every export is a new file; raw footage is never overwritten.
- **mlx_whisper first run downloads the model** (~1.5 GB, several minutes). If it looks stuck, check `~/.cache/huggingface/xet/logs/xet_*.log`. Never `du -sh` the blobs and never delete `.incomplete` files (R-TOOL.5).
- **Always end with the disclosure** in the why-these-choices note: what this run did not do (cut points are word-timestamp plus pad and may still clip a word; no NLE live-trim; nothing checked against the waveform) (R-PROCESS.2).
- A new paid API (ElevenLabs, a music subscription) or any `brew`/`pip` install beyond this skill needs a card first.

## Inputs

Raw footage (path) or a script/voiceover; one or more references (a link gives timing data, screenshots give look-and-feel only); the message and platform (9:16 first, 16:9 second if both).

## Steps

Run folder: `00_project/assets/<client-or-741>/video-edit/<YYYY-MM-DD>-<slug>/` with `raw/` (copy the footage in, never edit in place) and `reference/`. Use `741` for Martin's own videos.

1. **Reference profile.** Reuse anything already in `00_project/knowledge/video-editing-library/references/`. New: `python3 .claude/skills/video-edit/scripts/reference_profile.py "<url>" --out <run>/reference` (`--image` for a still, look-and-feel only). Read `summary.md` and `contact_sheet.jpg` before planning; the pacing target is the reference's measured shot length, not a guess.
2. **Transcribe.**
```bash
/Users/martindrendel/.local/bin/mlx_whisper <run>/raw/clip.mp4 --model mlx-community/whisper-large-v3-turbo --word-timestamps True --output-format json --output-dir <run>/transcript --output-name words
```
3. **Edit plan.** Styling or captions only on an already-good take: skip to step 5 on the raw clip. Otherwise draft kept spans per R-CUT.1 (cut filler, dead air, false starts; a repeated line keeps its best complete take, usually the last) into `<run>/transcript/spans.json` as `[{"start":..,"end":..,"text":"..."}]`, then:
```bash
python3 .claude/skills/video-edit/scripts/build_cut_plan.py <run>/transcript/words.json <run>/transcript/spans.json --video <run>/raw/clip.mp4 --out <run>/transcript/cuts.json
```
Exit 2 = two spans too close to pad: revise `spans.json`. **CHECKPOINT: show the printed span list and wait for go or changes.**
4. **Rough cut.** `python3 .claude/skills/video-edit/scripts/render_cut.py <run>/transcript/cuts.json --out <run>/rough_cut.mp4`. Exit 4 = duration drifted more than 0.15 s from the plan: investigate, never ship an unverified cut.
5. **Captions and look, in this order.**
   1. After cutting, remap: `python3 .claude/skills/video-edit/scripts/remap_words.py <run>/transcript/words.json <run>/transcript/cuts.json --out <run>/transcript/words_cut.json`
   2. 16:9 source to 9:16 target: pad with blurred background before the caption burn (`references/ffmpeg-cookbook.md` §9:16-pad), because captions use the final frame's coordinates.
   3. Draft caption wording per R-CAP.1/.2, then burn (`words_cut.json` if remapped, else `words.json`): `python3 .claude/skills/video-edit/scripts/caption_render.py <run>/transcript/words_cut.json --video <run>/padded_916.mp4 --out <run>/captioned.mp4 --w 1080 --h 1920`
   4. Two-pass loudnorm on the final audio (`references/ffmpeg-cookbook.md` §Loudness, note TP=-1.5 and `-shortest`).
6. **Export** to the platform spec (`references/export-specs.md`). Write `<run>/why-these-choices.md`: hook choice, pacing target and why, caption style, look, and the disclosure (R-PROCESS.2). **CHECKPOINT: show the export and the note, wait for go or notes.** Notes loop back to step 3 (new spans) or step 5 (look or captions only), never a silent re-render.

Before "done": `render_cut.py` printed `OK rendered and verified`, the export exists and is non-empty (`ls -la <run>/export/*.mp4`). Report the file path and the note together.
