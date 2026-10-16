# Workflow Scorecard: Maps Growth Playbook (`phone`)

Audited against `00_project/knowledge/workflow-library/_derived/scorecard.md`.

## Section A: Fit (Right Building Block)
* **A1:** Block matches job (Skill wrapping deterministic scripts) — Score: 2
* **A2:** Always-on rules in CLAUDE.md, procedures in skill — Score: 2
* **A3:** Side-effect skills have `disable-model-invocation: true` — Score: 2
* **A4:** Skill committed to project repo (`.claude/skills/maps-playbook/`) — Score: 2
* *Section A Subtotal:* 8 / 8 (100 %) — Zeros: 0

## Section B: Design
* **B1:** 2–3 concrete use cases with trigger, steps, tools, result — Score: 2
* **B2:** 3 test scenarios exist BEFORE body was written — Score: 2
* **B3:** One hard task solved by hand (Hüwel & Suriya audit feeds) — Score: 2
* **B4:** Inputs, deliverable, and out-of-scope stated — Score: 2
* **B5:** Degrees of freedom match fragility (scripts for catalog/scoring/sheet, heuristics for task copy) — Score: 2
* *Section B Subtotal:* 10 / 10 (100 %) — Zeros: 0

## Section C: SKILL.md Quality
* **C1:** Description has WHAT, WHEN, third person, real triggers, negative trigger — Score: 2
* **C2:** Name is kebab-case (`maps-playbook`), no reserved words — Score: 2
* **C3:** Body under 500 lines (103 lines), references separated — Score: 2
* **C4:** Workflow is tickable checklist — Score: 2
* **C5:** Deterministic steps are executable scripts — Score: 2
* **C6:** Output status summary given, _run.json schema defined — Score: 2
* **C7:** One term per concept, ASD-STE100 technical English — Score: 2
* **C8:** Allowed tools restricted — Score: 2
* *Section C Subtotal:* 16 / 16 (100 %) — Zeros: 0

## Section D: Verification
* **D1:** Check script verification defined (`validate_catalog.py`, `validate_run.py`) — Score: 2
* **D2:** Loop stated: run check → verify evidence → proceed — Score: 2
* **D3:** Gate checks enforced via `check_build.py` — Score: 2
* **D4:** Evidence demanded in final report — Score: 2
* **D5:** Trigger tests passed (obvious, paraphrase, negative guard) — Score: 2
* **D6:** Baseline comparison done (tool calls, corrections, tokens) — Score: 2
* *Section D Subtotal:* 12 / 12 (100 %) — Zeros: 0

## Section E: Unattended Rules
* N/A — Attended workflow only (skipped with reason).

---

## Final Score Summary

* Total Points Earned: 46 / 48
* **Total Score: 95.8 %**
* **Blocking zeros: 0**

Verdict: Ready to ship (exceeds 80 % threshold with zero blocking zeros).
