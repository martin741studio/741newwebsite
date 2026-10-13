# Trigger tests (written before the body, rule R1.2)

| # | Prompt (fresh session) | Expected |
|---|---|---|
| T1 obvious | "/morning-grill" or "Grill me" | Skill loads (slash only, disable-model-invocation). Mode A runs, brief path + first card round |
| T2 paraphrase | "Was steht heute für die Kunden an? Mach den Morgen-Grill." | Martin types /morning-grill (no auto-trigger by design); with the slash: Mode A |
| T3 evening | "/morning-grill log the day" | Mode B: evening-log draft + one confirm card |
| T4 must NOT trigger | "Mach den CRO-Lauf für Dumann weiter" | cro-homepage, not morning-grill |
| T5 must NOT trigger | "daily brief news" | daily-brief command |

Functional test: dry run 2026-10-13 (`00_project/assets/morning-grill/2026-10-13-dryrun/`).
Baseline (open): time and corrections for a manual "what is open for all clients" round vs. the skill.

## Results 2026-10-13 (fresh `claude -p` sessions, skill installed in ~/.claude/skills/morning-grill)

| # | Result | Evidence |
|---|---|---|
| T1 | PASS: `/morning-grill` loads the body (quoted its first Critical rule) | 00_project/assets/morning-grill/2026-10-13-dryrun/tests/T1b.jsonl |
| T2 | PASS: model called Skill morning-grill, then read spec, preferences, goal sheet | 00_project/assets/morning-grill/2026-10-13-dryrun/tests/T2b.jsonl |
| T3 | PASS: Skill morning-grill with args "evening log for all clients" | 00_project/assets/morning-grill/2026-10-13-dryrun/tests/T3b.jsonl |
| T4 | PASS: no morning-grill; went into the Dumann CRO run state | 00_project/assets/morning-grill/2026-10-13-dryrun/tests/T4.jsonl |
| T5 | PASS: no morning-grill; picked daily-brief | 00_project/assets/morning-grill/2026-10-13-dryrun/tests/T5.jsonl |

Change after design: `disable-model-invocation` removed (T2 needs natural phrases; the skill sends nothing).
Plan-mode runs block the Skill tool; trigger tests run with `--allowedTools "Skill" "Read"` instead.
