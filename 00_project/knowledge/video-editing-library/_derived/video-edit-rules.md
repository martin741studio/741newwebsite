# Derived rules — video-edit

One source citation per line. Built 2026-10-27 from `sources/001`, `sources/002`, `sources/003` and the two reference profiles under `references/`.

## R-TOOL — tooling
- R-TOOL.1: Cut, concat, speed ramp, crossfade, zoom-pan, loudness, 9:16 pad, and export all run on local ffmpeg 8.0.1. Src: `sources/001-tooling-stack-research.md` §"What is confirmed local and working".
- R-TOOL.2: This Mac's ffmpeg has neither libass nor libfreetype — the `subtitles`/`ass`/`drawtext` filters do not run. Captions use a Pillow PNG-overlay renderer instead (`caption_render.py`), never ASS. Src: `sources/001` §"Confirmed MISSING".
- R-TOOL.3: Scene cuts come from `scenedetect.detect(path, ContentDetector())`. Src: `sources/001`; proven on `references/mn-I3AojJzQ` 2026-10-27 (93 shots found, 6.1s avg).
- R-TOOL.4: Word-level timing comes from the `mlx_whisper` CLI (`--word-timestamps True --output-format json`), not the Python import (the import path is not on the system Python; the CLI runs in its own pipx venv). Src: `reference_profile.py` build note, 2026-10-27.
- R-TOOL.5: The FIRST run of mlx_whisper on a new machine or after a cache clear downloads the model (~1.5-1.6GB for large-v3-turbo) from Hugging Face via its chunked "xet" backend; this can take several minutes and the CLI's own progress line ("Fetching N files: 0%") barely moves because xet reassembles chunks only at the end. **Do not judge progress from `du -sh ~/.cache/huggingface/hub/*`** — xet downloads live in an internal chunk cache invisible to that check. Check `~/.cache/huggingface/xet/logs/xet_*.log` instead (its "observed bytes sent so far" line shows real progress) before assuming a stuck run is broken, and never delete `.incomplete` blobs to "fix" an apparent hang — that throws away real progress and restarts the download. After the first successful run the model is cached and transcription itself is fast (Apple GPU via MLX). Src: build incident, 2026-10-27 — an apparent hang was actually a healthy ~8-10MB/s xet transfer, confirmed via the xet log after a wasted restart.
- R-TOOL.6: yt-dlp and reference downloads are for own clips or explicitly permitted reference material only — most platforms restrict downloads in their ToS. Src: `sources/001` §"Evaluated, not installed" / yt-dlp legal note.
- R-TOOL.7: own/paid APIs (ElevenLabs, music subscriptions) need Martin's go card before any spend; Pixabay (no attribution) is the default free music source. Src: `sources/001` §"Music/SFX licensing".

## R-CAP — captions
- R-CAP.1: Word-by-word captions with the active word highlighted; house default white text, yellow for high-energy moments, black outline/stroke. This is a house choice (vendor-sourced, not a verified platform rule) — never state it to a client as platform law. Src: `sources/002` §"Caption conventions".
- R-CAP.2: Max 4 words per caption line (house default, no verified source gives this number). Src: `sources/002` §"Caption conventions" [gap, house choice].
- R-CAP.3: Keep captions out of the bottom 400px, right 150px on a 1080x1920 export (conservative union of vendor safe-zone estimates). Src: `sources/002` §"Safe zones". Enforced in `caption_render.py`'s bottom position math directly off this margin, not a fixed pixel guess — a fixed `h*0.78` default was found to sit inside the margin at normal font sizes (2026-10-27, functional test).
- R-CAP.4: If ANY cutting was done (render_cut.py ran), always run `remap_words.py` between the cut render and `caption_render.py` — burning captions from the raw source-timeline transcript onto a cut video drifts further out of sync after every cut (found up to 1.3s drift, 2026-10-27 functional test). Skip only for a no-cut styling-only job, where the transcript already matches the uncut video's timeline.

## R-CUT — cutting and pacing
- R-CUT.1: Cut filler, dead air, false starts and restarts from talking-head footage; when a line is said more than once, keep the best complete take (usually the last), never a trailing fragment. Src: `sources/003` §"Patterns adopted" item 3.
- R-CUT.2: Pad each kept piece ~0.08s before the first word and ~0.12s after the last word, never reaching into a cut word; split the gap between two kept pieces if padding would make them overlap. Src: `sources/003` §"Patterns adopted" item 3; implemented in `build_cut_plan.py`.
- R-CUT.3: Show the cut plan for approval before rendering anything. Src: `sources/003` item 3; this is the "edit plan" checkpoint in `pipeline.md`.
- R-CUT.4: A visual change every 3-5 seconds is a tunable test-start for fast-cut formats, not a proven rule — no primary study measured average shot length for short-form video. Src: `sources/002` §"Cut rate and pacing" [gap].
- R-CUT.5: One deliberate pattern interrupt (zoom, b-roll insert, on-screen text, sound effect) roughly every 8-15 seconds in clips over 30s — vendor estimate, tune per client. Src: `sources/002` §"Pattern interrupts" [estimate].

## R-BUILD — frame-accurate rendering
- R-BUILD.1: Read the raw footage's real fps/size/orientation with ffprobe before building; the output matches the source, never a hardcoded default. Src: `sources/003` item 4.
- R-BUILD.2: Snap every cut point to a whole frame (`build_cut_plan.py` does this via `fps` from ffprobe). Src: `sources/003` item 4.
- R-BUILD.3: Use `-fps_mode passthrough`, never `-r`, when exporting a concatenated cut — forcing the frame rate with `-r` silently duplicates frames at cut points. Src: `sources/003` item 4; implemented in `render_cut.py`.
- R-BUILD.4: After rendering, verify the output's duration (and, where practical, frame count) against the cut plan's sum before calling the cut done — do not rely on a visual check alone. Src: `sources/003` item 5; implemented in `render_cut.py`'s post-render check.
- R-BUILD.5: An ffmpeg render writes its output file progressively — the file exists and grows on disk long before the render is done (worse with an expensive filter like `boxblur`). `ls` showing the file, or `ffprobe` returning data on an earlier check, is not proof the render finished. Never read, `ffprobe`, or feed a render's output into the next step until its own background-task completion notification has arrived; checking by `ls`/polling leads to feeding a half-written (moov-atom-missing) file into the next tool and a wasted re-run. Found 2026-10-27, hand-run (C0929.MP4 9:16 pad).

## R-EXPORT — export specs
- R-EXPORT.1: Short-form (Reels/Shorts/TikTok): 1080x1920, 9:16, H.264, MP4. Src: `sources/002` §"Export specs" (Instagram/TikTok/Shorts rows, mixed verified/estimate).
- R-EXPORT.2: YouTube long-form 1080p SDR: 8 Mbps at 24-30fps, 12 Mbps at 48-60fps, H.264 High profile, AAC-LC 48kHz. Src: `sources/002` §"YouTube long-form bitrate table" [verified].
- R-EXPORT.3: Loudness target -14 LUFS, true peak ≤ -1 dBTP, via ffmpeg two-pass `loudnorm`. The -14 LUFS anchor is Spotify's verified rule (the only fully-official loudness page read this round); YouTube's own -14 LUFS figure is secondary-sourced only. Src: `sources/002` §"Loudness".
- R-EXPORT.4: Hard limit — nothing in this workflow uploads or posts. Every export is a new file; originals are never overwritten. Src: inputs-grill.md, Martin's go 2026-10-27.

## R-PROCESS — how this workflow runs
- R-PROCESS.1: Finishing app is CapCut — the workflow renders a flat finished MP4, never drives a live NLE (Premiere/Resolve/Final Cut) in this version. Src: Martin, inputs-grill.md, 2026-10-27.
- R-PROCESS.2: Every run ends with an explicit "what this run did not do" disclosure (cut points may still clip/trail a word; no NLE live-trim; nothing checked against the waveform) — stated plainly every time, not only on request. Src: `sources/003` item 6.
