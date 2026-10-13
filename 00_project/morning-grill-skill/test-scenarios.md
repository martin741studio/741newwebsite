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
