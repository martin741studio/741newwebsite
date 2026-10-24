# Functional test (Step 4.2)

Method note: the real task from Step 2.3 (grilling Martin live about 741's own marketing) WAS run as the functional test, not repeated separately — re-running the same live decision a second time in a "fresh session" would mean re-asking Martin the same questions about the same real situation, producing no new signal and wasting his time. The hand-run in `hand-run.md` is this functional test's record.

## Where it stalled, guessed, or needed a correction (the actual signal this step exists to find)
- **Stalled on a stale fact, corrected live**: Round 2's first draft named "Gayo & Maya" as the affiliate-stream owners, taken directly from `marketing-quarter-campaign.md` without checking it first. Martin caught it ("dont use old inforamtion like MAya rather grill me again"). This is exactly the kind of flaw Step 4.2 exists to surface before shipping — it has been patched into the skill body itself (`## Critical`, and `references/card-pattern.md`), not left as a one-off apology, per the meta-workflow's immediate-patch rule.
- **Did not stall on channel selection**: because the read phase found `revenue-model-100k.md` already had a 4-day-old live diagnosis, Round 1 was a confirmation question rather than a blank Core Four re-derivation — this matched the skill's designed "confirmation shape" branch (`card-pattern.md`) and worked correctly on the first attempt.
- **Did not over-suggest pauses**: Round 3's "what should stop" question was answered "nothing needs to stop" — the skill's "nothing stops" option (added specifically so the skill doesn't default to suggesting pauses) was exercised and worked as intended.

## Result
A real, sourced, slop-checked (5/5) playbook was produced: `00_project/assets/741studio/marketing-grill/2026-10-25/playbook.md`. `check_citations.py` passes against it. This is the first real deliverable from the workflow, not a synthetic test case.
