# Export specs — video-edit

Full detail and confidence labels: `00_project/knowledge/video-editing-library/sources/002-retention-and-platform-specs.md`. [verified] = platform's own page read directly. Everything else is a house default or vendor estimate — never state it to a client as platform law.

## Short-form (Reels / TikTok / Shorts) — house default

- 1080x1920, 9:16, H.264, MP4, recording frame rate (commonly 30 or 60fps).
- Max length: 3 minutes for most accounts on all three platforms (TikTok [verified] 2026-08-04; Instagram/YouTube partial/secondary).
- Loudness: -14 LUFS, true peak ≤ -1 dBTP (Spotify's verified anchor, applied as house default — see ffmpeg-cookbook.md).
- Safe zones (1080x1920, conservative union of vendor estimates — verify in-app before a real client deploy): keep text and faces out of the **bottom 400px, right 150px, top 150px, side margins 65px**.
- Captions: word-by-word, active word highlighted, white default / yellow for high-energy, black stroke, max 4 words/line (house choice, `_derived/video-edit-rules.md` R-CAP.1/.2).

## Long-form (YouTube, 16:9) — verified bitrate table

Source: support.google.com/youtube/answer/1722171, [verified], fetched 2026-10-27.

| Resolution | SDR 24-30fps | SDR 48-60fps |
|---|---|---|
| 1080p | 8 Mbps | 12 Mbps |
| 1440p | 16 Mbps | 24 Mbps |
| 2160p (4K) | 35-45 Mbps | 53-68 Mbps |

Container MP4 (fast-start), H.264 High profile 4:2:0, AAC-LC 48kHz (stereo 384kbps).

## LinkedIn (if ever needed)

16:9 / 1:1 / 4:5 recommended (9:16 accepted), MP4, 30fps, 1920x1080 max — [snippet, not independently verified].

## Pacing (house default, not a verified platform rule — R-CUT.4)

A visual change every 3-5 seconds is a test-start for fast-cut formats. **Prefer the reference's own measured average shot length** (`reference_profile.json` → `shot_stats.avg_shot_len`) over this fallback whenever a reference is available.
