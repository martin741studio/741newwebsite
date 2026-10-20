# Workflow Scorecard: Sales Pitch Architecture (`sales-pitch`)

Date: 2026-10-17  
Workflow ID: `sales-pitch`  
Result: 46 / 46 (100 %) · ZERO BLOCKING ZEROS · READY TO SHIP  

---

## A. Fit (Right Building Block)

| # | Check | Score (0-2) | Evidence |
|---|---|---|---|
| A1 | Block matches job per `patterns.md` §3 | 2 | Skill (`.claude/skills/sales-pitch/SKILL.md`) for repeatable procedure |
| A2 | Always-on rules in CLAUDE.md, procedures in skill | 2 | Procedures contained in skill, CLAUDE.md clean |
| A3 | Side-effect skills bounded | 2 | Read-only analysis, creates local brief file |
| A4 | Committed to repo | 2 | Tracked in `.claude/skills/sales-pitch/` |

**Section A Score: 8 / 8 (100%) — Zero blocking zeros.**

---

## B. Design

| # | Check | Score (0-2) | Evidence |
|---|---|---|---|
| B1 | 2–3 concrete use cases written | 2 | `00_project/workflow-builds/sales-pitch/use-cases.md` |
| B2 | 3 test scenarios before body | 2 | `00_project/workflow-builds/sales-pitch/test-scenarios.md` |
| B3 | One real task solved by hand | 2 | `00_project/workflow-builds/sales-pitch/hand-run.md` (Korinna Heintze) |
| B4 | Inputs, deliverables, out-of-scope stated | 2 | `00_project/workflow-builds/sales-pitch/inputs-grill.md` |
| B5 | Degrees of freedom match fragility | 2 | `00_project/workflow-builds/sales-pitch/decisions.md` (R1.7 separation) |

**Section B Score: 10 / 10 (100%).**

---

## C. SKILL.md Quality

| # | Check | Score (0-2) | Evidence |
|---|---|---|---|
| C1 | Description WHAT + WHEN + negative trigger | 2 | `.claude/skills/sales-pitch/SKILL.md` frontmatter |
| C2 | Kebab-case name, valid format | 2 | `sales-pitch` |
| C3 | Body under 500 lines, references 1-level deep | 2 | 72 lines in body, references in `references/` |
| C4 | Workflow is a checklist Claude copies & ticks | 2 | Operational checklist embedded |
| C5 | Deterministic steps are scripts | 2 | `scripts/verify_pitch.py` |
| C6 | Output template given | 2 | Structured 6-phase cockpit format |
| C7 | One term per concept, internal 741 terminology | 2 | "741 Call-Raster", zero external guru names |
| C8 | Dependencies listed | 2 | Standard Python 3, no third-party package requirement |

**Section C Score: 16 / 16 (100%).**

---

## D. Verification

| # | Check | Score (0-2) | Evidence |
|---|---|---|---|
| D1 | Deterministic check script exists | 2 | `scripts/verify_pitch.py` |
| D2 | Verification loop enforced | 2 | Passed on real output |
| D3 | Gated procedure | 2 | On-demand run with Martin Go |
| D4 | Evidence demanded in final output | 2 | Recorded in `functional-test.md` |
| D5 | Trigger tests passed (T1-T3) | 2 | Recorded in `trigger-tests.md` |
| D6 | Baseline comparison done | 2 | Recorded in `baseline.md` |

**Section D Score: 12 / 12 (100%) — Zero blocking zeros.**

---

## Total Evaluation
- **Total Points:** 46 / 46 (100 %)
- **Threshold:** ≥ 80 % (Passed)
- **Hard Blockers:** None (Section A: 0 zeros, Section D: 0 zeros)
- **Recommendation:** Proceed to Checkpoint 2 (Martin Ship Go).
