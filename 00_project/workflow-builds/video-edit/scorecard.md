# Scorecard — video-edit (step 4.5)

Scored 2026-10-27, before Checkpoint 2. 0 = missing, 1 = partly, 2 = done. Ship at ≥80%, no 0 in A or D. Section E excluded (not applicable — on-demand only, never scheduled/unattended).

## A. Fit
| # | Check | Score | Note |
|---|---|---|---|
| A1 | Block matches job | 2 | research-note.md: skill, chat-triggered |
| A2 | Rules/procedures/enforcement in the right place | 2 | all in SKILL.md; no always-on CLAUDE.md rule needed, on-demand only |
| A3 | `disable-model-invocation` decided | 2 | set `false` — natural triggers work; the two in-skill checkpoints are the real gate |
| A4 | Committed / enabled | 2 | will commit at step 5.2, standard for this skill category |
**A: 8/8**

## B. Design
| # | Check | Score |
|---|---|---|
| B1 | 2-3 use cases | 2 |
| B2 | 3 test scenarios before the body | 2 |
| B3 | One hard task solved by hand | 2 |
| B4 | Inputs/deliverable/out-of-scope stated | 2 |
| B5 | Degrees of freedom match fragility | 2 |
**B: 10/10**

## C. SKILL.md quality
| # | Check | Score | Note |
|---|---|---|---|
| C1 | description WHAT+WHEN+negative trigger | 2 | |
| C2 | kebab-case name | 2 | |
| C3 | Body <500 lines, refs one level deep | 2 | body ~95 lines |
| C4 | Workflow is a tickable checklist | 2 | |
| C5 | Deterministic steps are scripts, errors handled, no magic numbers | 2 | constants named and documented (PAD_BEFORE, MIN_WORD_DURATION) |
| C6 | Output template + 2-3 example pairs | 1 | template exists (why-these-choices-template.md); only one real worked example so far, not 2-3 style pairs |
| C7 | One term per concept, no time-sensitive text | 2 | |
| C8 | MCP tools fully qualified, deps listed | 2 | |
**C: 15/16**

## D. Verification
| # | Check | Score | Note |
|---|---|---|---|
| D1 | A check Claude can run | 2 | render_cut.py duration+frame check |
| D2 | Loop: check → fix → repeat → only proceed when it passes | 2 | exit codes 2/4 documented as fix-and-rerun |
| D3 | Unattended runs gated | 2 | never unattended; vacuously satisfied |
| D4 | Evidence demanded in final report | 2 | file path + why-these-choices note, both required |
| D5 | Trigger tests (obvious/paraphrase/negative) | 2 | 4/4 passed, trigger-test-results.md |
| D6 | Baseline comparison | 1 | qualitative discovery-cost comparison done (baseline-comparison.md); no literal tool-call/token counts, no twin "without" run was possible to stage |
**D: 11/12**

## F. 741 house rules
| # | Check | Score | Note |
|---|---|---|---|
| F1 | Client message + Drive link where a client deliverable exists | 1 | skill always closes with file path + why-these-choices note; no explicit Drive-link/client-message step yet for a future client-video run |
| F2 | Per-change go before any live website change | 2 | never touches a website; vacuously satisfied |
| F3 | Every data point verified or asked for | 2 | title text asked via card, all profiling reads real data |
| F4 | STE / artifacts | 2 | SKILL.md slop-linted 5/5 after fixing em-dash density |
| F5 | No method sources named in client material | 2 | source 003's attribution kept internal-only, paraphrased |
| F6 | Shows up in the overview Excel by itself | 0 | not yet registered — done right after Martin's CP2 go (step 5.3a), not before |
| F7 | Client/prospect deliverables use the Martin guide where it fits | 2 | N/A deliverable type (video file, not a page); vacuously satisfied |
**F: 11/14**

## Result
Total: 55/60 → **91.7%**. Blocking zeros (A or D): **none**. F6's 0 is expected at this stage (registration happens right after CP2 go) and does not block.

**Decision: ship**, pending Martin's Checkpoint 2 go.
