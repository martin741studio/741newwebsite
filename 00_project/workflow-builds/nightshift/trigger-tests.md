# 4.1 Trigger tests (2026-10-13 ~19:55 WITA)

## A. Skill draft `night-shift-v2` — fresh `claude -p` sessions (Sonnet 5) in a scratch project with only this skill + a morning-grill stub; tool use read from stream-json
| # | Prompt | Expected | Result |
|---|---|---|---|
| T1 obvious | "Run the night shift tonight with the confirmed queue - what is the status?" | night-shift-v2 loads | night-shift-v2 ✅ |
| T2 paraphrase | "Nachtschicht: lass über Nacht die FAQ-Entwürfe für Maria Brasse laufen." | night-shift-v2 loads | night-shift-v2 ✅ |
| T3 must-not | "Publish the Brasse FAQ to the live site." | no night-shift skill | none ✅ |
| T4 must-not | "Grill me" | morning-grill, not night-shift | morning-grill ✅ |

## B. Runner triggers (deterministic) — `runner-trigger-tests.txt`
R1 no queue → no run ✅ · R2 outside window → no run ✅ · R3 STOP file → no run ✅ · R4 lock held → no run ✅ · R5 run cap → stops, and (after fix) never starts an Executor without room for its Critic ✅ · R6 unconfirmed item → skipped ✅

## C. Permission test (real `claude -p`, same flags as the runner)
curl → DENIED ✅ · Write outside `reporting/night-shift/**` → DENIED ✅ · Write inside → ALLOWED ✅ (first try without `--setting-sources user` let the outside write through because `.claude/settings.local.json` allows Write/Edit; fixed).
