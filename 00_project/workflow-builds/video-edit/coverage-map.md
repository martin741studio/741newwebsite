# Coverage map — video-edit

Checked 2026-10-27 against `.claude/skills/*` and the memory files named in the build brief.

| Existing asset | What it does | Overlap with video-edit? |
|---|---|---|
| `captions` | Writes on-screen caption TEXT for the daily voiceless YouTube video from a thought dump. Never touches the video file, never cuts, never burns text onto frames. | No overlap. `video-edit` could reuse its caption TEXT once written, but burns it onto an actual cut video — a different job. Documented in `video-edit`'s own negative trigger. |
| `content-format-board` | Idea/format board + reference research + AI-generated concept STILL FRAMES for a content pitch. Never cuts footage, never produces a video file. | No overlap. Different output type entirely (ideas + stills vs. an edited video file). |
| `personal-posts` / `social-visuals-workflow` | Static image templates (PNG) via HTML + headless Chrome. No video. | No overlap. |
| `youtube-thumbnail-workflow` (memory) | One still thumbnail image via rembg + HTML render. No video editing. | No overlap. |
| `00_project/knowledge/design-video-notes/` | One transcript on motion-design WEBSITE building (Jack Roberts video), unrelated to cutting footage. | Not reused — wrong topic. |
| `00_project/90-sekunden-video-framework.md`, `evergreen-video-skripte.md` | SCRIPT text for Martin's personal intro/explainer videos (what to say), not editing instructions. | Not reused — these are script-writing references, not editing tooling. Could feed a future "script to voiceover" use case, noted as a possible v2 extension. |
| `00_project/videographer-editor-leads.md` | A lead list of human videographers/editors in Bali for hiring. Unrelated to this workflow. | No overlap. |

**Conclusion:** no existing 741 asset does video cutting, caption burn-in, colour/look application, or video export. `video-edit` is new ground. Nothing is rebuilt that already exists.
