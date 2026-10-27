# 001 — Video editing tooling for Claude Code on macOS

Research run: 2026-10-27. Full detail (commands tested, every source URL and date): see the research agent's output, archived at `00_project/workflow-builds/video-edit/research-tooling.md`.

## What is confirmed local and working on this Mac

- **ffmpeg 8.0.1** (Homebrew). Confirmed working: precise cuts (re-encode and stream-copy), concat (demuxer and filter), speed ramps (`setpts`/`atempo`), crossfades (`xfade`/`acrossfade`, full transition list in `ffmpeg-filters.html`), zoom-pan (`zoompan`), loudness two-pass (`loudnorm`), 9:16 crop with blurred background (`split`/`scale`/`crop`/`boxblur`/`overlay`), H.264 and HEVC export (`hvc1` tag needed for Apple players). Source: ffmpeg.org/ffmpeg-filters.html, fetched 2026-10-27.
- **Confirmed MISSING on this Mac's ffmpeg build: libass AND libfreetype.** The `subtitles`/`ass` filters and even `drawtext` do not run. Homebrew's current ffmpeg bottle does not depend on libass (verified: `brew deps ffmpeg` lists no libass, no freetype). **Decision: captions are rendered as Pillow (PNG) word-highlight overlays, composited with ffmpeg `overlay`, not ASS/drawtext.** This sidesteps the missing dependency entirely and gives tighter control over word-by-word highlighting than ASS karaoke tags. See `_derived/video-edit-rules.md` R-CAP.
- **PySceneDetect 0.7.2** (pip, user install 2026-10-27, Martin's go). `scenedetect.detect(path, ContentDetector())` returns a scene list with start/end timecodes. Used by `reference_profile.py`.
- **yt-dlp** (brew, 2026.10.21, Martin's go 2026-10-27). For own clips and permitted references only — most platforms restrict downloads in their ToS. Used by `reference_profile.py`.
- **mlx_whisper** (pipx venv, already installed before this build). CLI flags confirmed: `--word-timestamps True --output-format json`. Runs on Apple GPU via MLX, model `mlx-community/whisper-large-v3-turbo`. First run downloads ~800 MB. Used by `reference_profile.py` and `caption_render.py`.
- **Pillow 13.0.0** (pip, user install 2026-10-27, no system changes — pure Python, zero cost, installed without a separate card). Used by `caption_render.py`.

## Evaluated, not installed

| Tool | Verdict | Why |
|---|---|---|
| Remotion | Use later, for branded motion graphics only | Free up to 3 employees; React/TypeScript learning curve is high; FFmpeg covers plain cuts faster |
| MoviePy | Skip | Raw ffmpeg commands do the same job with less overhead |
| auto-editor | Candidate for v2 (silence-cut on talking-head) | Not installed yet; `pip install auto-editor`, exports XML for Resolve/Premiere too |
| ElevenLabs | Only if Martin wants AI voice-over, needs a card (paid API) | Pricing conflicts between page and FAQ — confirm before any spend |
| `kajisho5/ffmpeg-skill` (GitHub, 3,065 stars, MIT, pushed 2026-10-26) | Reviewed, not adopted wholesale | 42 FFmpeg tools + MCP server; our own scripts cover the same ground and stay auditable in-repo |
| Premiere/Resolve/Final Cut live connectors | Documented as a future extension only (see source 004) | Martin confirmed CapCut as the finishing app 2026-10-27 — no live NLE connector needed now |

## Music/SFX licensing (commercial social video)

- **Pixabay**: free, no attribution required, no resale, no trademark use. Use as the default source.
- **YouTube Audio Library**: terms vary per track; CC-BY tracks need credit. YouTube-only use until verified further.
- **Epidemic Sound / Artlist / Uppbeat**: subscription, prices unverified in this research round (pages blocked/empty) — confirm official pricing before any spend, needs a card.

## Export specs confirmed from this research

See source 002 for the full platform spec table (Reels/TikTok/Shorts/YouTube long-form/LinkedIn).

Freshness: this source is current as of 2026-10-27. Re-verify ffmpeg version (8.x→9.x available) and Remotion/ElevenLabs pricing before the next refresh (3-month rule, due 2027-01-27).
