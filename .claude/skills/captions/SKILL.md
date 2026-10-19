---
name: captions
description: Writes the on-screen caption text for Martin and Celine's daily voiceless YouTube video from their thought dump of the day. Reads the dump from the Drive folder "Captions Celine Martin" or from pasted text, lists every fact as a beat, orders the beats into a story (hook, the day, insight, close), writes English "we" caption blocks (max 12 words, max 2 lines), validates format and numbers against the dump with a script, runs the slop lint to 5/5, shows Martin the captions for his go, then puts a copy as a Google Doc into the Drive folder. Use when Martin says "/captions <link or text>", "captions for today", "caption text for the video", "here is our dump for today's video", "make the captions from the dump", "Untertitel-Text für das Video", "Text fürs Video von heute". Do NOT use for YouTube subtitle files or SRT files with timecodes, for subtitles on a client video (Hüwel, Suriya or any 741 client), for uploads or thumbnails, for 741.studio channel scripts, or for social posts and carousels (social-visuals).
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(python3:*), Bash(bash:*), Bash(ls:*), Bash(cat:*), ToolSearch, AskUserQuestion, mcp__a53bd814-aee8-40e6-992f-1f4efc20f127__search_files, mcp__a53bd814-aee8-40e6-992f-1f4efc20f127__read_file_content, mcp__a53bd814-aee8-40e6-992f-1f4efc20f127__get_file_metadata, mcp__a53bd814-aee8-40e6-992f-1f4efc20f127__create_file
---

# Captions for video (workflow id `captions`)

Replies in STE. The captions are the one artifact in plain English prose.

## Critical

- **The dump is the only source.** Every number, place, name, price, date and plan in a caption is in the dump. Nothing is added, not a day of the week, not a location, not an opinion. `scripts/validate_captions.py` checks the numbers. You check the words against `beats.md`.
- **Never upload or publish.** This skill writes text. It never touches YouTube, never uploads a video, a thumbnail or a subtitle file. The only side effect is one Google Doc in the Drive folder, and only after Martin's "go" card. `disable-model-invocation` is off so the natural triggers work; the go card is the gate.
- **Never edit the dump.** The Drive doc stays as it is. `dump.md` is a copy of what came in, spelling and all.
- **Format is fixed.** English, "we" voice, numbered blocks, max 12 words, max 2 lines, max 42 characters per line, no dashes, no HTML. ALWAYS use the template in `assets/captions-template.md`. Only proceed when the validator prints PASS and the slop lint prints 5/5.

## Inputs (Martin gives)

- A Google Docs link, the folder link, or pasted text. Nothing else. No link and no text: look in the folder (`references/drive.md`). Empty folder: one card, never a sample.
- Date: today, unless Martin names a date.

## Workflow

Copy this checklist into the reply and tick it off:

```
Captions <date>:
- [ ] 1 get the dump text (Drive connector or pasted), intake.py start → run folder, dump.md, _run.json
- [ ] 2 beats.md: one line per fact, dump words in quotes
- [ ] 3 story order (references/story-rules.md): hook, the day, insight, close
- [ ] 4 captions.md from assets/captions-template.md (style: references/examples.md)
- [ ] 5 validate_captions.py → PASS (loop: fix, re-run)
- [ ] 6 slop lint → 5/5 (loop, max 2 rounds)
- [ ] 7 CHECKPOINT card: captions + validator line, wait for "go"
- [ ] 8 Drive copy (create_file), intake.py finish, report local path + Drive link
```

**Step 1 Dump and intake.** Get the text as `references/drive.md` says (Docs link, folder search, or pasted). Then:

```bash
python3 .claude/skills/captions/scripts/intake.py start --source - --date <YYYY-MM-DD> --drive-url "<doc link or empty>" <<'DUMP'
<the dump text, unchanged>
DUMP
```

It prints `RUN_DIR 00_project/assets/youtube-captions/<date>`. Exit 2 means the dump is empty: stop with one card. A second run on the same date keeps the old captions as `captions-v<n>.md`.

**Step 2 Beats.** Write `<run>/beats.md`: a table with one row per fact (number, place, name, plan, feeling, idea). Columns: id, beat in English, the dump words in quotes, type (day, money, idea, insight, plan, note). The dump column is the proof for every caption word. A fact that is not in the table does not go into a caption.

**Step 3 Story.** Order the beats with `references/story-rules.md`: hook (strongest number or decision), the day in time order, the insight or idea, the close with the plans for tomorrow. Write the order as a short list at the end of `beats.md`.

**Step 4 Draft.** Write `<run>/captions.md` with the exact template. One beat per block. 1.5 to 2.5 blocks per dump line. Style and worked pairs: `references/examples.md`. Lint flags a dump number as "invented proof": write one to nine as a word (story-rules section 6). English number format (2,500), "k" as in the dump (150k), dates as "4 November", times as "6 am". Hook and close lines may carry no fact. They never add one. Unclear dump words, tense and note beats: story-rules section 7.

**Step 5 Validate (loop until PASS).**

```bash
python3 .claude/skills/captions/scripts/validate_captions.py <run>/captions.md --dump <run>/dump.md
```

Fix every FAIL line in `captions.md`, run again. Only proceed on `PASS`.

**Step 6 Slop lint (loop, max 2 rounds).**

```bash
python3 .claude/skills/slopmonster/tools/deslop.py --text "$(cat <run>/captions.md)"
```

Needs `score 5/5`. Below that: rewrite the flagged lines in plainer words, keep every fact, run step 5 again, lint again. After 2 rounds without 5/5: `bash .claude/skills/slopmonster/tools/cleanse.sh <run>/captions.md > <run>/cleansed.md`, check the cleansed text against `beats.md` (no new fact, no lost fact), validate, lint. Still below 5/5: show Martin the open hits at the checkpoint.

**Step 7 Checkpoint.** Show Martin the whole `captions.md` in one ```text block, then the validator PASS line, the slop score and the open "?" words from `beats.md` (one line each). One AskUserQuestion card: "Go (Drive copy)" or "Change". A change goes back to step 4. No Drive write before "go".

**Step 8 Deliver.** After "go": `create_file` as `references/drive.md` says (title `<date> captions`, parentId of the folder, `text/plain`, the full `captions.md`). Then:

```bash
python3 .claude/skills/captions/scripts/intake.py finish --date <YYYY-MM-DD> --result "<viewUrl>"
```

Reply: local path, Drive link, block count. Nothing else is sent anywhere.

## Output template

`assets/captions-template.md`. ALWAYS this format: a `# Captions <date>` heading, then numbered blocks `1. text`, a blank line between blocks, a second line indented by three spaces when the block has two lines.

## Checkpoints

- After step 6: Martin sees the captions and gives "go" before the Drive copy (step 7).

## Telemetry

`intake.py` writes `<run>/_run.json` (`client`, `workflow: captions`, `status`, `mode`, `last_run`, `local`, `result`, `note`, `drive`) at start ("in Arbeit") and at finish ("fertig"). The Stop hook syncs the overview Excel.

## Verification (end of every run)

Paste in the final reply:
1. The last two lines of `validate_captions.py` (`<n> blocks checked`, `PASS`).
2. The slop line (`score 5/5  CLEAN`).
3. The local path `00_project/assets/youtube-captions/<date>/captions.md` and the Drive `viewUrl`.
A run without these three is not done.

## References

- `references/story-rules.md`: the 4-part shape, hook rules, what stays out, voice.
- `references/examples.md`: 4 dump-to-block pairs and one anti-example.
- `references/drive.md`: folder id, connector tool names, read and write steps.
