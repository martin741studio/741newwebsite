# 002 — Retention drivers and platform specs for short- and long-form video

Research run: 2026-10-27. Full detail with every URL, date and confidence label: `00_project/workflow-builds/video-edit/research-retention-specs.md`.

Confidence labels used throughout (carried over from the research run): **[verified]** official platform page read directly; **[OLD]** published before 2025-10-27; **[estimate]** a number from a secondary/vendor source, not a platform rule; **[vendor]** a tool or agency selling to creators, treat as marketing; **[gap]** no source found.

## Hook (first 1-3 seconds)

- No platform publishes a numeric swipe-away window. Third-party guides estimate 1-2 seconds **[estimate]**.
- YouTube Studio's own retention report defines "Intro" as the share still watching at 30 seconds, and advises testing different openings in that window **[verified]**, support.google.com/youtube/answer/9314415.
- YouTube Shorts' "Viewed vs. swiped away" metric has no published benchmark or confirmed ranking effect **[gap]**.
- TikTok's only current official statement on ranking is from 2020 **[OLD]**: interactions, video information, device/account settings; finishing a longer video is a strong signal; follower count is not a direct factor.
- Instagram's most recent public signal statement (Mosseri, watch time + likes/reach + sends/reach) is from January 2025 **[OLD]**; no 2026 primary statement found.

## Cut rate and pacing — largely unverified

- **No primary study measured average shot length for TikTok/Reels/Shorts [gap].** Vendor guides suggest a visual change every 2-5 seconds as "a test start," not a rule **[estimate][vendor]**.
- Average TikTok video length (not shot length) reported at ~42.7 s, up from 39 s in 2023 **[estimate]**.
- No sourced timing rule exists for punch-ins or jump-cut frequency in talking-head video **[gap]**.

## Pattern interrupts

- Four named types, vendor-sourced: sudden zoom (~200% crop, 2-3 s), sound effect, b-roll insert, on-screen text **[vendor][estimate]**.
- Suggested frequency: one deliberate interrupt every 8-15 seconds in clips over 30 s **[estimate][vendor]** — treat as a tunable starting point, not a rule.

## Caption conventions — mostly vendor-sourced, treat as house defaults not platform law

- Word-by-word with the active word highlighted is the vendor consensus (no peer-reviewed study found) **[vendor][estimate]**.
- TikTok: white text + black outline, or yellow + black outline. YouTube Shorts: white default, yellow for high-energy, 2-4px black stroke **[vendor]**.
- No source gives a verified font family, font size ratio, or max-words-per-line value **[gap]** — our default (max 4 words/line, white/yellow highlight, black stroke) is a house choice, documented as such in `_derived/video-edit-rules.md`.

## Safe zones (percentages verified, exact px per-platform mostly estimate/vendor)

- Meta ad guidance (third-party quoted): keep text/logos out of top 14%, bottom 35%, 6% per side on a 1080x1920 frame → **top 269px, bottom 672px, sides 65px** (agent arithmetic from the %, not an official px table) **[estimate]**.
- YouTube Shorts: no official safe-zone spec exists **[gap]**. Vendor estimate for 1080x1920: bottom 350-400px (title/channel row), right ~120px (action icons), left 40-60px, top 120-380px **[vendor][estimate]**.
- TikTok: top ~120px (UI bar), right ~150px (action column), bottom 250-480px (caption/sound area, sources disagree) **[vendor][estimate]**.
- **House default** (conservative union of the above): keep all text and faces out of the bottom 400px, right 150px, top 150px, and side 65px margins on a 1080x1920 export. Verify in-app before a real client deploy.

## Loudness

- Spotify's own page (the only platform-official loudness page actually read): **-14 LUFS integrated, true peak ≤ -1 dBTP (≤ -2dB if master is louder than -14 LUFS)** **[verified]**, support.spotify.com.
- YouTube's -14 LUFS figure comes only from secondary sources; no official YouTube page was found stating it **[estimate]**. No YouTube true-peak value is confirmed.
- EBU R128 defaults (-23 LUFS programme target, -1 dBTP) and ffmpeg `loudnorm` defaults (I=-24, LRA=7, TP=-2) are carried from general knowledge, not independently re-verified this round **[unverified, carry with caution]**.
- **House default** for social export: target -14 LUFS, true peak ≤ -1 dBTP (Spotify's verified rule, the closest confirmed anchor), via ffmpeg two-pass `loudnorm`.

## Export specs (platform-official where marked verified)

| Platform | Resolution/AR | Codec | Max length | Max file size | Source |
|---|---|---|---|---|---|
| Instagram Reels | 1.91:1 to 9:16, min 720p, 30fps; **recommended 1080x1920** | H.264, MP4/MOV | 3 min (since 2025-01, OLD) | 1-4GB, sources conflict | help.instagram.com [partial], threads.com/@mosseri [OLD] |
| TikTok (Content Posting API) | 360-4096px each dim | H.264 preferred (H.265/VP8/VP9 OK), MP4 | most accounts 3 min, some 5-10 min | 4GB | developers.tiktok.com, 2026-08-04 **[verified]** |
| YouTube Shorts | vertical/square, **recommended 1080x1920** | — | 3 min | — | support.google.com community FAQ [partial, OLD rollout date] |
| YouTube long-form | 1080p-4K | H.264 High, 4:2:0, AAC-LC/Opus 48kHz | — | — | support.google.com/youtube/answer/1722171 **[verified]** |
| LinkedIn | 1920x1080 max, 16:9/1:1/4:5 recommended, 9:16 accepted | MP4, 30fps | 3s-30min (ads) | 75KB-500MB (ads) | business.linkedin.com [snippet] |

**YouTube long-form bitrate table (verified, the one fully-official table found):**

| Resolution | SDR 24-30fps | SDR 48-60fps | HDR 24-30fps | HDR 48-60fps |
|---|---|---|---|---|
| 2160p (4K) | 35-45 Mbps | 53-68 Mbps | 44-56 Mbps | 66-85 Mbps |
| 1440p | 16 Mbps | 24 Mbps | 20 Mbps | 30 Mbps |
| 1080p | 8 Mbps | 12 Mbps | 10 Mbps | 15 Mbps |

## Transition taxonomy (editor-practice sourced, not platform-sourced)

J-cut (next scene's sound starts first), L-cut (previous scene's sound continues), jump cut (time removed from a continuous shot, signals urgency), match cut (shared shape/colour/movement/idea links two shots), punch-in (digital zoom, pattern interrupt). Hard cut, whip pan, dissolve, dip-to-black, speed ramp, mask transition, glitch — editor practice, no study sourced.

## Colour

Teal-orange separates skin (orange range) from background (shifted teal); protect skin tones with an HSL secondary mask before grading the background. Vendor-sourced, not a platform rule.

## Long-form (8-20 min) structure

YouTube's own retention-curve shapes (flat / gradual decline / spikes / dips) are the one verified mechanism **[verified]**, support.google.com/youtube/answer/9314415. Teaser-every-2-3-minutes and best-moment-at-two-thirds are vendor heuristics, not platform-sourced **[estimate]**.

## What this means for the skill's defaults (house choices, documented as such — never stated to a client as "platform rule")

1. Hook: strongest visual or line in the first 1-2 seconds of every edit.
2. Export: 1080x1920 9:16 H.264 MP4 for Reels/Shorts/TikTok; YouTube long-form per the verified bitrate table above.
3. Safe zones: keep captions/faces out of bottom 400px, right 150px, top 150px, side 65px (1080x1920).
4. Loudness: -14 LUFS, true peak ≤ -1 dBTP, two-pass ffmpeg `loudnorm`.
5. Captions: word-by-word, active word highlighted, white default / yellow for energy, black stroke, max 4 words/line (house default, not a verified platform rule).
6. Pacing: 3-5 second visual-change test-start for fast-cut formats; tune against real retention data per client once available — never state these numbers as platform-proven to a client.

Freshness: due for refresh 2027-01-27 (3-month rule). Re-check the Instagram Reels help page, TikTok ad specs page and YouTube Shorts safe-zone status — all failed to render this round.
