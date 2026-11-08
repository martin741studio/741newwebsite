---
name: captions
description: Writes the on-screen caption text for Martin and Celine's daily voiceless YouTube video from their thought dump (Drive folder "Captions Celine Martin" or pasted text): English "we" blocks, max 12 words, script-checked against the dump, slop lint 5/5, Martin's go, then a Google Doc in Drive. Use on "/captions <link or text>", "captions for today", "Untertitel-Text für das Video", "Text fürs Video von heute". Not for SRT files or client videos.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(python3:*), Bash(bash:*), Bash(ls:*), Bash(cat:*), ToolSearch, AskUserQuestion, mcp__a53bd814-aee8-40e6-992f-1f4efc20f127__search_files, mcp__a53bd814-aee8-40e6-992f-1f4efc20f127__read_file_content, mcp__a53bd814-aee8-40e6-992f-1f4efc20f127__get_file_metadata, mcp__a53bd814-aee8-40e6-992f-1f4efc20f127__create_file
---

# Captions for video (workflow id `captions`)

Replies in STE. The captions are the one artifact in plain English prose. Format: `assets/captions-template.md` (heading `# Captions <date>`, numbered blocks, second line indented by three spaces).

## Critical

- **The dump is the only source.** Every number, place, name, price, date and plan in a caption is in the dump. Nothing is added, not a day of the week, not a location, not an opinion. `scripts/validate_captions.py` checks the numbers. You check the words against `beats.md`.
- **Never upload or publish.** This skill writes text. It never touches YouTube, never uploads a video, a thumbnail or a subtitle file. The only side effect is one Google Doc in the Drive folder, after Martin's "go" card.
- **Never edit the dump.** The Drive doc stays as it is. `dump.md` is a copy of what came in, spelling and all.
- **Format is fixed.** English, "we" voice, numbered blocks, max 12 words, max 2 lines, max 42 characters per line, no dashes, no HTML. Proceed only when the validator prints PASS and the slop lint prints 5/5.

## Inputs (Martin gives)

- A Google Docs link, the folder link, or pasted text. Nothing else. No link and no text: look in the folder (`references/drive.md`). Empty folder: one card, never a sample.
- Date: today, unless Martin names a date.

## Workflow

Steps: 1 dump → intake, 2 beats, 3 story order, 4 draft, 5 validate (loop to PASS), 6 slop lint (loop to 5/5), 7 CHECKPOINT card, 8 Drive copy.

**Step 1 Dump and intake.** Get the text as `references/drive.md` says. Then:

```bash
python3 .claude/skills/captions/scripts/intake.py start --source - --date <YYYY-MM-DD> --drive-url "<doc link or empty>" <<'DUMP'
<the dump text, unchanged>
DUMP
```

It prints `RUN_DIR 00_project/assets/youtube-captions/<date>`. Exit 2 = empty dump: stop with one card. A second run on the same date keeps the old captions as `captions-v<n>.md`.

**Step 2 Beats.** `<run>/beats.md`: one row per fact. Columns: id, beat in English, the dump words in quotes, type (day, money, idea, insight, plan, note). The dump column is the proof for every caption word. A fact not in the table does not go into a caption.

**Step 3 Story.** Order the beats with `references/story-rules.md` (hook with the strongest number or decision, the day in time order, insight, close with tomorrow's plans). Write the order at the end of `beats.md`.

**Step 4 Draft.** Write `<run>/captions.md` with the exact template. One beat per block. 1.5 to 2.5 blocks per dump line. Style: `references/examples.md`. If the lint flags a dump number as "invented proof", write one to nine as a word (story-rules section 6). Number format 2,500; "k" as in the dump (150k); dates "4 November"; times "6 am". Hook and close lines add no fact. Unclear dump words, tense and note beats: story-rules section 7.

**Step 5 Validate (loop until PASS).**

```bash
python3 .claude/skills/captions/scripts/validate_captions.py <run>/captions.md --dump <run>/dump.md
```

Fix every FAIL line and run again until `PASS`.

**Step 6 Slop lint (loop, max 2 rounds).**

```bash
python3 .claude/skills/slopmonster/tools/deslop.py --text "$(cat <run>/captions.md)"
```

Needs `score 5/5`. Below that: rewrite flagged lines in plainer words, keep every fact, redo step 5 and the lint. After 2 rounds without 5/5: `bash .claude/skills/slopmonster/tools/cleanse.sh <run>/captions.md > <run>/cleansed.md`, check the cleansed text against `beats.md` (no new fact, no lost fact), validate, lint. Still below 5/5: show Martin the open hits at the checkpoint.

**Step 7 Checkpoint.** Show the whole `captions.md` in one ```text block, then the validator PASS line, the slop score and the open "?" words from `beats.md`. One AskUserQuestion card: "Go (Drive copy)" or "Change". A change goes back to step 4. No Drive write before "go".

**Step 8 Deliver.** After "go": `create_file` as `references/drive.md` says (title `<date> captions`, parentId of the folder, `text/plain`, the full `captions.md`). Then:

```bash
python3 .claude/skills/captions/scripts/intake.py finish --date <YYYY-MM-DD> --result "<viewUrl>"
```

Reply: local path, Drive link, block count. Nothing else is sent anywhere.

## Run record and proof

`intake.py` writes `<run>/_run.json` at start ("in Arbeit") and finish ("fertig"); the Stop hook syncs the overview Excel. The final reply carries three proofs: the last two lines of `validate_captions.py` (`<n> blocks checked`, `PASS`), the slop line (`score 5/5  CLEAN`), and the local path `00_project/assets/youtube-captions/<date>/captions.md` plus the Drive `viewUrl`. Without all three the run is not done.

## References

- `references/story-rules.md`: the 4-part shape, hook rules, what stays out, voice.
- `references/examples.md`: 4 dump-to-block pairs and one anti-example.
- `references/drive.md`: folder id, connector tool names, read and write steps.
