# Inputs grill — video-edit

Date: 2026-10-27. Martin's answers (AskUserQuestion, 2 rounds).

## Job
Input: Martin gives (a) raw footage (phone clips, screen recordings, talking-head, b-roll) or a script/voiceover, (b) one or more references (a YouTube/Instagram/TikTok link, or screenshots/clips) that show the target format, pacing, transitions, look and feel, and (c) the message and the platform.
Transform: profile the reference (cuts, shot length, transitions, caption style, look), write an edit plan, cut the footage to that plan, add captions, look and sound, export.
Output: an edited video in the reference style (short-form 9:16 first, long-form 16:9 second) plus a short "why these choices" note. Martin reviews, gives notes, the workflow iterates.
Who uses it: Martin, for 741's own videos and later for client videos.
Martin's answer: "Yes, that is the job (Recommended)".

## Runtime Surface
Claude Code skill at `.claude/skills/video-edit/`, command `/video-edit`. Same architecture as `captions`, `personal-posts`, `content-format-board`.
Martin's answer: "Claude Code skill, on demand (Recommended)".

## Cadence
On demand. Martin starts it per video. No schedule, no auto-run.

## Hard Limits
Martin selected one limit: "Never post or upload (Recommended)". No YouTube, Instagram or TikTok upload. Martin publishes by hand.
Not selected by Martin (so not a hard limit of this workflow): a card before every paid API, a card before every install, never overwrite raw footage.
House rules still apply: this build asks by card before an install (done 2026-10-27, Martin: "Yes, install both"), before any paid API, and before each export Martin reviews. Originals are never overwritten by design (every export is a new file).

## First reference (for the profiler proof)
URL: https://www.youtube.com/watch?v=mn-I3AojJzQ&t=389s (YouTube long-form, Martin points at 389 s).
Install go for yt-dlp and PySceneDetect: "Yes, install both (Recommended)", 2026-10-27.

## Finishing app (added 2026-10-27, from Martin's pasted starter-prompt reference)
Martin's words: "just change we use mainly capcut".
Decision: the workflow renders a finished MP4 (ffmpeg render path), the same path a CapCut-only or no-NLE editor gets in the reference prompt Martin shared. No live NLE connector (Premiere/Resolve/Final Cut) is built in this version. Martin opens the exported MP4 in CapCut for any final touch-up or upload. Live NLE driving is noted as a future extension in the knowledge base, not built now.
