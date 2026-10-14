# Baseline — with vs. without the skill (step 4.3)

Same real task both times: build a call-prep brief for Korinna Heintze's booked call.

## Without the skill (the 2.3 hand-run, before SKILL.md existed)
A cold attempt (no skill, just "write a call-prep note for this prospect") needed 3
corrections caught only by manually re-reading source files and a failed verification run —
documented in `hand-run.md`:
1. A first pass repeated the Leipzig-volume insight that had already gone out in WhatsApp
   message 2 — caught only by rereading `m1.txt`-`m3.txt` by hand.
2. A first pass picked "zu teuer" as the lead objection — wrong for this profile; caught only
   by cross-reading `sales-einwandbehandlung.md`'s capacity-objection pattern against her
   actual positioning.
3. The deslop/claims check failed twice before passing: once for an em dash (punctuation
   rule), once for two correctly-sourced numbers flagged as "invented proof" because the
   check was run without `--claims <claims.json>`.
Corrections: **3**. Verification passes: **3** (2 fails + 1 pass). No scripted lookup — the
booking folder had to be found and read file by file with no fixed order.

## With the skill (the 4.2 functional test, fresh subagent, SKILL.md + scripts + references)
- Tool calls: **9** (per the subagent's own usage report).
- Corrections needed: **0** — no AskUserQuestion, no stalled step, no invented fact.
- Verification: **1** run, `RESULT: PASS` on the first try (the fixed `verify_brief.py` script
  always calls `deslop_de.py` with `--claims`, so the step-2 mistake class from the hand-run
  cannot recur).
- The one new judgment call (stale worked-example risk, see `functional-test.md`) was
  resolved correctly WITHOUT a correction cycle, because the skill's fixed read order (step 2)
  already told it to check `booking/` for source files before drafting — it found and used
  `site-recheck.json` on its own.
- Subagent tokens for the whole run: ~117k (includes reading this skill's files, the booking
  folder, and writing + verifying the output — a one-shot prep task, not a cheap lookup, which
  matches its `context: fork` design so this stays out of Martin's main chat).

## Reading
Going from "no skill" to "skill" took the correction count from 3 to 0 on the identical real
task, and the verification step now passes on the first try instead of needing 2 fix-and-retry
cycles. The skill's fixed-order reading (step 2) and the always-`--claims` verification script
are exactly what removed the two correction classes that mattered (repeating a shown insight;
an unscored/wrongly-flagged number).
