# Scorecard (Step 4.5) — agent-job-descriptions, 2026-11-03

Scored against `00_project/knowledge/workflow-library/_derived/scorecard.md`. 0 = missing, 1 = partly, 2 = done. Section E (unattended) excluded: the skill runs only with Martin present (write mode in chat, review mode from the grill with cards); the unattended rules apply to the agents it describes and sit in the block template.

## A. Fit
| # | Check | Score | Note |
|---|---|---|---|
| A1 | Block matches the job | 2 | Skill with two modes, chat-triggered, Martin present (patterns §3 step 3) |
| A2 | Always-on rules in CLAUDE.md, procedures in skill, enforcement in hooks | 2 | The skill maps every gate onto the existing hook + cards; procedures in SKILL.md; no new always-on CLAUDE.md line needed |
| A3 | Side-effect skills have `disable-model-invocation: true` | 2 | Set: it places files other agents load |
| A4 | Cowork/routine enablement | 2 | N/A — project skill, committed to the repo |
**A: 8/8**

## B. Design
| # | Check | Score | Note |
|---|---|---|---|
| B1 | 2–3 use cases | 2 | UC1 write, UC2 review, UC3 client template |
| B2 | 3 test scenarios before the body | 2 | T1–T4 written before SKILL.md |
| B3 | One hard task by hand, approach extracted | 2 | Web Developer description grilled in 3 rounds; Night Shift as runner example |
| B4 | Inputs/deliverable/out-of-scope stated | 2 | inputs-grill.md, SKILL.md Inputs, negative trigger |
| B5 | Degrees of freedom match fragility | 2 | 4 scripts (roster, validate, place, evidence); drafting and rung decision as heuristics |
**B: 10/10**

## C. SKILL.md quality
| # | Check | Score | Note |
|---|---|---|---|
| C1 | Description WHAT+WHEN+negative trigger | 2 | 5/5 trigger tests |
| C2 | Kebab-case name | 2 | |
| C3 | Body < 500 lines, references one level deep | 2 | 58 lines; 5 reference files |
| C4 | Tickable checklist | 2 | write 8 steps, review 5 steps |
| C5 | Deterministic steps are scripts Claude runs | 2 | roster.py, validate_jd.py (14 checks), place.py (refuses unvalidated input), collect_evidence.py (reports unreadable) |
| C6 | Output template + example pairs | 2 | block-template.md, review-template.md, task-file-template.md, examples.md (2 real descriptions) |
| C7 | One term per concept, default + escape hatch | 2 | "rung", "card Go", "description" used consistently; memory rung as the escape hatch for chats without paths |
| C8 | MCP tools fully qualified | 1 | The description template asks for fully qualified names; the webdev example names "Novamira abilities" and "Wix MCP" by product, not `Server:tool`, because the ability names differ per site server |
**C: 15/16**

## D. Verification
| # | Check | Score | Note |
|---|---|---|---|
| D1 | A check Claude can run | 2 | validate_jd.py structure + `--copies` drift check; both ran on the real description |
| D2 | Loop stated | 2 | Step 5: validate → fix → repeat → only proceed at PASS; place.py re-runs the validator |
| D3 | Unattended runs gated | 2 | N/A for the skill; for described agents the template demands caps and the runner rung |
| D4 | Evidence demanded in the final report | 2 | Verification section: paste PASS outputs and roster diff; review without evidence file is not a review |
| D5 | Trigger tests passed | 2 | 5/5 |
| D6 | Baseline comparison done | 2 | baseline.md |
**D: 12/12 — no zero**

## F. 741 house rules
| # | Check | Score | Note |
|---|---|---|---|
| F1 | Client message + Drive link where a client deliverable exists | 2 | N/A, internal deliverable |
| F2 | Per-change go before any live site change | 2 | The skill never touches a site; every placed file needs a card Go; the Web Developer description itself encodes the per-change Go |
| F3 | Every data point verified or asked for | 2 | Descriptions drafted from the real prompts/skills/memories; validator rejects creator names; "[unverified]" marker in the functional test |
| F4 | STE replies and artifacts | 2 | English STE, German only for client-facing quotes (Martin 03.11.) |
| F5 | No method sources in client material | 2 | Validator rejects Tyler/Phillips/Grok Bot/12-block in descriptions |
| F6 | Shows up in the overview by itself | 1 | place.py writes `_run.json`; registry entry is Step 5.3a, next gated step |
| F7 | Martin guide for client-facing work | 2 | N/A |
**F: 13/14**

## Result
Total: 58 / 60 → 96.7 %. Blocking zeros: none (A and D complete).
Decision: ship (after Checkpoint 2 go).
