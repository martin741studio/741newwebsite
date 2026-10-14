# Decisions — goals-data-architecture

## 2026-10-15, checkpoint 1 (relayed via the orchestrator, Martin's words)

Martin's answers, all per the recommended option:

1. **Design:** "Go — generated-from-Supabase + overlay, as designed." (option 1, recommended)
2. **Backfill `work_goals.baseline/target/due_on` now from the current JSON:** "yes, go ahead." (option 2, recommended)
3. **`aliases`/`client_rules`:** "keep in the overlay file for now, no schema change." (option 3, recommended)

This is the checkpoint 1 go. Proceeding into build (section 3 onward) per `00_project/workflow-creation-workflow.md`.

## 2026-10-15, checkpoint 2 (relayed via the orchestrator, Martin's words)

Martin's go: "ship it". Scope: commit, registry entry, memory file, first scheduled run by hand, install gate.

Evidence at this gate: scorecard 95.9 % (scorecard.md), functional test (functional-test.md), trigger tests (trigger-tests.md), baseline (baseline.md).
