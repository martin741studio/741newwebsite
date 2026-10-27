# Video Editing Library — state of the art for the `video-edit` workflow

Built 2026-10-27 for workflow id `video-edit`. Freshness rule: nothing older than 3 months without a re-check note. Last refresh: 2026-10-27. Next refresh due: 2027-01-27.

Internal library. Source 003 is credited internally only (a starter prompt Martin shared) — never name its creator or community in client-facing or default Martin-facing output, per `no-method-sources-in-deliverables`.

## How to use

1. Follow `00_project/workflow-creation-workflow.md` for how this library plugs into the build.
2. `grep -ril "<term>" 00_project/knowledge/video-editing-library/` and read hits in this order: `_derived/` (the rule, one line, cited) → `sources/NNN` (the fuller write-up) → the full research file named at the top of that source, if you need every raw URL.
3. Derived layer: `_derived/video-edit-rules.md` (one cited rule per line, grouped R-TOOL/R-CAP/R-CUT/R-BUILD/R-EXPORT/R-PROCESS), `_derived/video-edit-questions.md` (open gaps, re-check on refresh).

## Sources

| # | File | What it covers | Pulled |
|---|---|---|---|
| 001 | `sources/001-tooling-stack-research.md` | ffmpeg/PySceneDetect/yt-dlp/mlx_whisper/Remotion/MoviePy tested locally; Claude Code video-editing skills on GitHub; music/SFX licensing | 2026-10-27 |
| 002 | `sources/002-retention-and-platform-specs.md` | Hook/pacing/pattern-interrupt evidence, caption conventions, safe zones, loudness, export specs per platform, transition taxonomy, colour, long-form structure | 2026-10-27 |
| 003 | `sources/003-claude-video-editor-starter-pattern.md` | Cut-selection rules (filler/false-start/repeated-take), padding and no-overlap logic, frame-accurate build + verify pattern, live-NLE-connector reference (not built), transparency-disclosure pattern | 2026-10-27, Martin-shared |

Full (unpruned) research-agent output kept for audit: `00_project/workflow-builds/video-edit/research-tooling-full.md`, `research-retention-specs-full.md`.

## Reference profiles (Martin's own examples, look/pacing/style)

| Slug | Source | What it is | Profiled |
|---|---|---|---|
| `mn-I3AojJzQ` | youtube.com/watch?v=mn-I3AojJzQ (AlexanderTheCreate) | Long-form (16:9), 9.4 min, 93 shots, 6.1s avg shot — Martin's first reference, used to prove `reference_profile.py` | 2026-10-27 |
| `REAOFI534lk` | youtube.com/watch?v=REAOFI534lk (Duncan Rogoff, "I taught Claude how to edit videos and it's INSANE") | Direct tutorial on Claude-driven video editing — profiled for both its cutting style AND its spoken content (workflow/checkpoint/token-saving advice), see `references/REAOFI534lk/summary.md` and the transcript-derived notes once extracted | 2026-10-27 |

Each reference folder holds `raw/source.mp4` (+ `info.json`), `reference_profile.json`, `contact_sheet.jpg`, `transcript.json` (word-level), `summary.md`. `raw/` and `_audio.wav` are gitignored (large third-party downloads, not 741's own content) — re-fetch with `reference_profile.py "<url>"` if missing; the derived files (profile, contact sheet, transcript, summary) are what's actually committed and used.

## Still to export

Nothing named by Martin yet — no NotebookLM notebook exists for this topic. If Martin names one later, export it the same way the Hormozi/Content-Format libraries were exported (see `marketing-grill-workflow` memory for the method) and add it here as a new numbered source.

## Refresh method

Re-run the two research tracks (tooling, retention+specs) via the same prompts used 2026-10-27 (kept in `00_project/workflow-builds/video-edit/` as `research-tooling-full.md` / `research-retention-specs-full.md` for the question list), re-check the `[gap]`-flagged pages in `_derived/video-edit-questions.md`, and bump the dates here.
