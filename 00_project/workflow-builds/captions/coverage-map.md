# 1.4 Coverage map: existing 741 assets (2026-10-19)

Checked: `ls ~/.claude/skills/ .claude/skills/`, memory grep for youtube, caption, subtitle, celine, vlog, `ls 00_project/assets/`.

| Need | Existing asset | Reuse? |
|---|---|---|
| Read a Drive file by link | Google Drive MCP (`read_file_content`, `search_files`, `create_file`) | yes, Claude reads the dump and writes the Drive copy with it |
| English slop check | `.claude/skills/slopmonster/tools/deslop.py --text` and `cleanse.sh` | yes, final gate, 5/5 required |
| Run folder + `_run.json` telemetry | pattern from content-writing, backlink (`_run.json` with client, workflow, status, mode, last_run, local, result, note, drive) | yes, same keys |
| Registry entry | `00_project/workflow-registry/workflow_registry.py add-workflow` | yes |
| Voice rules for copy | `~/.claude/skills/content-writing/references/copy-rules.md` (no dashes, one idea per sentence) | partly: the no-dash rule and the short-sentence rule |
| YouTube channel facts | memory `youtube-thumbnail-workflow.md` (channel UCQtithGJcnjr0W_iVFXMoIw, upload gotchas), `741-youtube-channel-avatar.md` | context only. This daily vlog is Martin + Celine, not the 741 lead-gen channel. No upload step. |
| Social visuals | `07_social/` templates, `social-visuals-workflow.md` | no, images are not in scope |
| Subtitle file with timecodes (SRT) | none | not needed. Output is on-screen caption blocks without timecodes. |
| Caption validator (word count, lines, numbers against the dump) | none | build: `scripts/validate_captions.py` |
| Intake script (run folder, dump.md, _run.json) | none | build: `scripts/intake.py` |

Gap: no existing skill writes video captions from a thought dump. Build a new skill `captions`.
