# 2.1 Use cases: Captions for video (2026-10-19)

## Use case 1: Drive link (the standard day)
- Trigger: `/captions https://docs.google.com/document/d/<id>/edit`
- Steps: read the Drive doc with the Drive MCP, `scripts/intake.py` makes the run folder and `dump.md`, Claude writes `beats.md` (every fact from the dump), Claude orders the beats into a story, Claude writes `captions.md` from the template, `scripts/validate_captions.py` runs until PASS, slopmonster lint 5/5, checkpoint card to Martin, after "go" the Drive copy in "Captions Celine Martin" (Drive id 1heXhO-CGVpM2bLp5f8T-nizTf7kmXnGm), `_run.json` updated.
- Tools: Google Drive MCP (read, create), Bash(python3), Read, Write.
- Deliverable: `00_project/assets/youtube-captions/<date>/captions.md` plus the Drive link.

## Use case 2: Pasted text (no Drive)
- Trigger: `/captions` followed by the pasted dump, or "captions for today:" plus text.
- Steps: same as use case 1. `intake.py` takes the text from a file Claude writes first. No Drive read.
- Deliverable: same.

## Use case 3: Second run of the same day (dump grew)
- Trigger: `/captions <link>` on a date that already has a run folder.
- Steps: `intake.py` keeps the old `captions.md` as `captions-v1.md`, saves the new dump, the run continues as in use case 1. The last run wins.
- Deliverable: new `captions.md`, Drive copy replaced.

## Result in every case
- Ordered caption blocks in English, "we" voice, max 12 words, max 2 lines per block.
- Every number in a caption is in the dump. Nothing added.
- Never an upload to YouTube.
