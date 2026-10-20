# Workflow scorecard — pre-ship gate for every new 741 workflow

Use before a skill, routine, scheduled task or workflow goes into daily use. Score each line 0 (missing), 1 (partly), 2 (done). Ship at 80 % or higher, with no 0 in section A or D.

Derived 2026-10-11 from `rules.md`. Internal document.

## A. Fit (right building block)

| # | Check | Score |
| --- | --- | --- |
| A1 | The block matches the job (skill / subagent / hook / routine / project / managed agent) per `patterns.md` section 3 | |
| A2 | Always-on rules are in CLAUDE.md, procedures are in the skill, enforcement is in hooks | |
| A3 | Side-effect skills have `disable-model-invocation: true` | |
| A4 | Skills for Cowork or routines are enabled on the claude.ai account or committed to the repo | |

## B. Design

| # | Check | Score |
| --- | --- | --- |
| B1 | 2–3 concrete use cases written with trigger, steps, tools, result | |
| B2 | Three test scenarios exist BEFORE the body was written | |
| B3 | One hard task was solved by hand and the winning approach was extracted | |
| B4 | Inputs, deliverable and out-of-scope are stated | |
| B5 | Degrees of freedom match fragility (exact scripts where fragile, heuristics where open) | |

## C. SKILL.md quality

| # | Check | Score |
| --- | --- | --- |
| C1 | `description` states WHAT and WHEN, third person, with real trigger phrases and a negative trigger | |
| C2 | Name is kebab-case, no reserved words, no XML brackets | |
| C3 | Body under 500 lines; detail in `references/` one level deep; TOC in files over 100 lines | |
| C4 | Workflow is a checklist Claude copies and ticks | |
| C5 | Deterministic steps are scripts Claude RUNS; scripts handle errors and have no magic numbers | |
| C6 | Output template given (strict or default) and 2–3 example pairs where style matters | |
| C7 | One term per concept, no time-sensitive text, one default with one escape hatch | |
| C8 | MCP tools fully qualified `Server:tool`; dependencies listed | |

## D. Verification

| # | Check | Score |
| --- | --- | --- |
| D1 | Claude has a check it can run (script, diff, screenshot compare, validator) | |
| D2 | Loop stated: run check → fix → repeat → "only proceed when it passes" | |
| D3 | Unattended runs are gated (`/goal`, Stop hook, or reviewer subagent) | |
| D4 | Evidence is demanded in the final report (command output, screenshot, link) | |
| D5 | Trigger tests passed: obvious task, paraphrase, unrelated task does NOT trigger | |
| D6 | Baseline comparison done (tool calls, corrections, tokens with vs. without) | |

## E. Unattended and scheduled (only if applicable)

| # | Check | Score |
| --- | --- | --- |
| E1 | Prompt is self-contained and states what success looks like and the time zone | |
| E2 | Per-source bookmarks, not fixed time windows | |
| E3 | Failed reads are reported as unreadable | |
| E4 | Posts count as sent only after confirmation; ledger updated after that | |
| E5 | Read-only credentials where it only reads; spend cap per run | |
| E6 | Preferences re-read every run from a store the agent cannot edit | |
| E7 | Runs are opened and read, not judged by the green status | |

## F. 741 house rules

| # | Check | Score |
| --- | --- | --- |
| F1 | Ends with the client message draft and the Drive link where a client deliverable exists | |
| F2 | Per-change "go" checkpoint before any live website change | |
| F3 | Every data point verified or asked for; no guesses | |
| F4 | Replies and artifacts in STE (CLAUDE.md of 741website) unless the artifact is client prose | |
| F5 | No method sources named in client material; call the frameworks "741-…-Raster" | |
| F6 | Runs show up in the overview Excel by themselves (`_run.json` or a detected run file, workflow added with `add-workflow`) | |
| F7 | Client- or prospect-facing deliverables use the Martin guide where it fits, per `00_project/assets/brand/martin-guide/README.md`; never on the client's own site | |

## Result

Total: __ / __ → __ %. Blocking zeros: __.
Decision: ship / fix first / redesign.
