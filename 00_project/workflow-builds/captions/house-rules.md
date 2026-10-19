# 3.6 741 house rules applied (captions)

- Verified data only: the dump is the only source. `validate_captions.py` checks numbers. `beats.md` proves every word. Critical rule 1.
- STE: SKILL.md, references and replies in STE. The captions are plain English prose (the one artifact, as the CLAUDE.md exception allows for content).
- Slop check: `deslop.py` 5/5 required, `cleanse.sh` after 2 rounds (SKILL.md step 6).
- Drive link at the end: step 8 reports the local path and the Drive `viewUrl`.
- Per-change "go": one AskUserQuestion card before the only side effect (the Drive copy). No website, no client, no YouTube.
- `disable-model-invocation`: off, as the canary build found (2026-10-14): with it on, the natural triggers never fire. The go card is the gate. Noted in Critical rule 2.
- No method sources named. The story shape is "hook, the day, insight, close", no guru names.
- Telemetry: `_run.json` by `intake.py` at start and finish, same keys as the other workflows.
- No HTML in the text (validator). No dashes (validator).
- Not client-facing: no Martin guide (5.3b skip).
