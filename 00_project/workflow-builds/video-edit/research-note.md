# Research note — video-edit

Date: 2026-10-27.

## 1.1 Building block
Skill, chat-triggered (`/video-edit`), no schedule, no daemon. Matches `captions`, `personal-posts`, `content-format-board`. Side effects (export, future NLE drive) stay behind Martin's per-run review, so `disable-model-invocation` can stay off (natural triggers) — the review gate is the actual control, same pattern as `captions`.

## 1.2 Library search
`grep -ril "video\|caption" 00_project/knowledge/workflow-library/` found no existing video-editing workflow precedent — this is new ground for 741. Closest architectural precedent: `content-format-board` (reference research + verification script + Martin go pattern) and `captions` (run-folder + intake.py + validator pattern). Both reused.

## 1.3 Freshness
New library built today (2026-10-27). Next refresh due 2027-01-27 (3-month rule). Several sources in the retention/specs research did not render (Instagram Reels help, TikTok ad specs, YouTube Shorts safe-zone) — flagged as gaps in source 002, re-check on refresh.

## 1.4 Existing asset check (full detail: coverage-map.md)
`captions` (on-screen text only, never touches video/audio), `content-format-board` (idea board + concept stills, never cuts footage), `personal-posts`/`social-visuals-workflow` (static image templates), `youtube-thumbnail-workflow` (one still image). None of these cut, grade, caption-burn, or export video. No duplicate. `design-video-notes/` held one unrelated transcript (motion-design website framework, not video editing) — not reused.

## 1.5 Three relevant rules + one pattern
- R1.7 (degrees of freedom): deterministic steps (cut timing, ffprobe, frame snapping, export encode) → scripts; qualitative steps (which take to keep, hook wording, look choice) → prompt heuristics reading the reference profile.
- R1.3: solve one real task by hand first, extract the winning context — done via the reference profiler proof on Martin's own reference link before any skill body was written.
- R1.8 (plan-validate-execute): write the cut plan, validate it (frame-accurate, no overlap), execute the render, then verify the output against the plan — exactly the pattern in `build_cut_plan.py`/`render_cut.py`.
- Pattern: run-folder + checkpoint-before-render, same shape as `content-format-board`'s board-then-go and `captions`' intake-then-go.

## 1.6 Knowledge base
Library: `00_project/knowledge/video-editing-library/` (new, built today).
- Local now: `sources/001` (tooling), `sources/002` (retention + platform specs), `sources/003` (cut-selection and frame-accuracy patterns from a starter prompt Martin shared), two reference profiles under `references/` (`mn-I3AojJzQ`, `REAOFI534lk`) with `reference_profile.json` + `contact_sheet.jpg` + transcript + summary each.
- Still to export: nothing named by Martin yet (no NotebookLM notebook named for this topic). If Martin later wants a running notebook of reference videos, export method = same `reference_profile.py` script run per new link, logged in `references/INDEX.md`.
- Derived layer: `_derived/video-edit-rules.md` + `_derived/video-edit-questions.md`, one source citation per line, written next.
- The skill body greps this library at run time (`grep -ril <term> 00_project/knowledge/video-editing-library/`); it never carries the knowledge itself.
