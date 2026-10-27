# 003 — Patterns from a published "Claude video editor" starter prompt

Internal reference only. Source: a starter prompt Martin pasted into chat 2026-10-27, credited there to a named creator and a paid community (do not repeat either name in client-facing or even Martin-facing default output — `no-method-sources-in-deliverables`). This file paraphrases the technique, not the original wording, and is cited here for internal traceability only.

## What it covers that our brief did not originally cover

A full editor-replacement prompt: cuts talking-head footage, drives a live NLE (Resolve/Premiere) or writes an XML (Final Cut) or renders a flat MP4 (CapCut / no app). Martin confirmed 2026-10-27 that 741 uses CapCut, so only the flat-MP4-render branch applies now. The live-NLE-connector branches are recorded below as a **future extension**, not built.

## Patterns adopted into this workflow (in our own words, in `_derived/video-edit-rules.md` and the scripts)

1. **Ask before installing anything, every time** — matches our own house rule exactly. Confirms our approach is correct, not a gap.
2. **One run folder per job**, with raw footage, transcript, and the cut plan kept separate — matches our `00_project/assets/<client>/video-edit/<date>/` run-folder convention (see pipeline.md).
3. **Cut-selection rules for talking-head footage** (adopted into `build_cut_plan.py`):
   - Cut filler, dead air, false starts, restarts.
   - When a line is said more than once, keep the best complete take — usually the last one said, never a trailing half-sentence.
   - Pad each kept piece: ~0.08s before the first word, ~0.12s after the last word, never reaching into a word that was cut.
   - When two padded pieces would overlap, split the gap between them so no two kept pieces ever overlap.
   - **Show the cut list for approval before building anything.** This is the "edit plan" checkpoint in our pipeline — never skip straight to rendering.
4. **Frame-accurate build rules** (adopted into `render_cut.py`):
   - Read the raw footage's real frame rate, size and orientation with ffprobe first; the output matches the source, never a default.
   - Snap every cut point to a whole frame.
   - After building, verify what actually landed against the cut plan: clip count, each clip's length, and the total — frame for frame, not just "looks right."
   - For an ffmpeg flat render (our CapCut-path default): one filtergraph, `trim`+`atrim` per kept piece then `concat`, encode once. **Critical: use `-fps_mode passthrough`, never `-r`** — forcing the frame rate with `-r` silently duplicates frames at the cut points with no warning. This is now a hard rule in `render_cut.py`.
5. **Verification step, not just visual review**: ffprobe the rendered output and confirm its frame count and total duration match the cut plan's sum, before calling the cut done.
6. **Explicit "what this run did not do" disclosure** at the end of every job — adopted as the closing section of our own "why these choices" note (see `assets/why-these-choices-template.md`): cut points are word-timestamp-plus-pad, so some may still clip or trail a word and need Martin's eye; no NLE live-trim (CapCut path is a flat render); nothing is checked against the waveform. Say this plainly every time, never only on request.

## Future extension, not built now (recorded so it is not silently lost)

- **Live NLE driving**: Resolve Studio 21.1+ has a built-in Claude Code connector (File > Setup AI Assistants, no install). Premiere needs a third-party MCP bridge (community project, CEP panel, Node build step). Final Cut takes an FCPXML import (frame-accurate rational-time XML, library/event/project/sequence/spine structure). None of this is built in v1 — Martin uses CapCut, which takes a flat rendered MP4. If a client or Martin later asks for a trimmable timeline instead of a flat render, re-open this source before building that branch.
- **WhisperX** (cross-platform, GPU-agnostic) is the alternative to mlx_whisper for transcription in a cross-OS tool. On this Mac, mlx_whisper is faster (Apple GPU via MLX) and already installed, so it stays primary. WhisperX is worth revisiting only if this skill ever needs to run on a non-Mac machine.
