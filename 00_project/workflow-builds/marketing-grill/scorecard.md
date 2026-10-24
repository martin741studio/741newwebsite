# Scorecard (Step 4.5) — marketing-grill, 2026-10-25

Scored against `00_project/knowledge/workflow-library/_derived/scorecard.md`. 0=missing, 1=partly, 2=done. Section E (unattended/scheduled) does not apply — this workflow is on-demand, chat-triggered, never scheduled — and is excluded from the total, matching the scorecard's own "only if applicable" note.

## A. Fit
| # | Check | Score | Note |
|---|---|---|---|
| A1 | Block matches the job | 2 | Skill, chat-triggered, matches R0.1/R0.2 |
| A2 | Always-on rules in CLAUDE.md, procedures in skill, enforcement in hooks | 1 | House rules live in `## Critical`, not a hook — acceptable for a non-destructive, document-only workflow, but not hook-enforced |
| A3 | Side-effect skills have `disable-model-invocation: true` | 2 | Correctly NOT set — this skill has no side effects (R2.10) |
| A4 | Cowork/routine enablement | 2 | N/A — project skill, not needed for Cowork |
**A: 7/8 (87.5%)**

## B. Design
| # | Check | Score |
|---|---|---|
| B1 | 2-3 use cases | 2 |
| B2 | 3 test scenarios before the body | 2 |
| B3 | One hard task solved by hand, approach extracted | 2 |
| B4 | Inputs/deliverable/out-of-scope stated | 2 |
| B5 | Degrees of freedom match fragility | 2 |
**B: 10/10 (100%)**

## C. SKILL.md quality
| # | Check | Score | Note |
|---|---|---|---|
| C1 | Description WHAT+WHEN+negative trigger | 2 | 897 chars, verified by 5/5 trigger tests |
| C2 | Kebab-case name, no reserved words | 2 | |
| C3 | Body <500 lines, references one level deep | 2 | 45 lines |
| C4 | Workflow is a tickable checklist | 2 | |
| C5 | Deterministic steps are scripts Claude runs | 2 | `check_infra_state.py`, `check_citations.py`, `run_log.py` |
| C6 | Output template + 2-3 example pairs | 1 | Template given; no separate worked example pair in the skill body beyond the one real playbook it already produced |
| C7 | One term per concept, one default + escape hatch | 2 | |
| C8 | MCP tools fully qualified | 2 | N/A, no MCP tools used |
**C: 15/16 (93.75%)**

## D. Verification
| # | Check | Score | Note |
|---|---|---|---|
| D1 | A check Claude can run | 2 | Both scripts verified working against the real playbook |
| D2 | Loop stated: run check -> fix -> repeat -> only proceed when it passes | 2 | Step 7 |
| D3 | Unattended runs gated | 2 | N/A, never unattended |
| D4 | Evidence demanded in the final report | 1 | Step 9 reports the playbook but doesn't explicitly tell Claude to paste the check output to Martin |
| D5 | Trigger tests passed (obvious/paraphrase/negative) | 2 | 5/5, see `trigger-tests.md` |
| D6 | Baseline comparison done | 2 | See `baseline.md` |
**D: 11/12 (91.7%) — no zero, gate requirement met**

## F. 741 house rules
| # | Check | Score | Note |
|---|---|---|---|
| F1 | Client message + Drive link where a client deliverable exists | 2 | N/A, internal-only deliverable |
| F2 | Per-change go before any live site change | 2 | Skill never touches a live site |
| F3 | Every data point verified or asked for | 2 | `check_infra_state.py` + citation check |
| F4 | STE replies | 2 | Stated in `## Critical` |
| F5 | No method sources in client material | 2 | N/A, no client-facing output; internal playbook names no source in its own prose |
| F6 | Shows up in the overview Excel by itself | 1 | Not yet registered — Step 5.3a (registry) is the next gated step, not skipped |
| F7 | Martin guide character for client/prospect-facing work | 2 | N/A, not client/prospect-facing |
**F: 13/14 (92.9%)**

## Result
Total (A+B+C+D+F): 56 / 60 → **93.3%**. No blocking zero in Section A or D.
Decision: **ship** (proceed to Checkpoint 2), with two open partials carried forward and not treated as blocking: C6 (add a worked example pair if a second real run shows the template needs it) and F6 (resolved by the still-pending Step 5.3a registry step).
