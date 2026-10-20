# 04. Pre-Ship Quality Scorecard

Every new or reworked workflow must be scored against this checklist before going into active operational use.

**Scoring Key:**
- `0`: Missing / Not implemented
- `1`: Partially implemented / Inconsistent
- `2`: Fully implemented and verified

**Passing Threshold:**
- Overall score: **$\ge 80\,\%$**
- Hard block: **ZERO 0s in Section A (Fit) or Section D (Verification)**. Any single `0` in A or D blocks release.

---

## Section A: Architectural Fit (Right Building Block)

| # | Check Item | Score (0–2) |
|---|---|:---:|
| **A1** | Primitive matches the job (Skill, Subagent, Hook, Routine, MCP) per `patterns.md`. | |
| **A2** | Always-on rules remain in global files; procedures are inside `SKILL.md`; enforcement is in hooks. | |
| **A3** | Any skill with side effects (file write, delete, API commit, deploy) has `disable-model-invocation: true`. | |
| **A4** | Workflow is tracked inside the repository (`.claude/skills/<id>/` or `.agents/skills/<id>/`). | |

---

## Section B: Design & Pre-Build Preparation

| # | Check Item | Score (0–2) |
|---|---|:---:|
| **B1** | 2–3 concrete use cases defined: trigger phrase, steps, tools, and expected output. | |
| **B2** | 3 test scenarios documented BEFORE writing the skill body (direct, paraphrase, negative). | |
| **B3** | At least one real task solved manually step-by-step, with edge cases documented. | |
| **B4** | Input contract, deliverable schema, and out-of-scope boundaries are clearly specified. | |
| **B5** | Degrees of freedom match fragility (exact scripts for math/APIs; prompts for copywriting/strategy). | |

---

## Section C: Implementation Quality (`SKILL.md` & Code)

| # | Check Item | Score (0–2) |
|---|---|:---:|
| **C1** | Frontmatter `description` states WHAT it does AND WHEN to use it, with a negative trigger (`NOT:`). | |
| **C2** | Skill name is lowercase `kebab-case`, max 64 characters, no XML tags. | |
| **C3** | Body is under 500 lines; references are linked 1 level deep; TOC included if reference > 100 lines. | |
| **C4** | Workflow is formatted as a tickable markdown checklist the agent copies into responses. | |
| **C5** | Deterministic steps are executable scripts in `scripts/`; scripts handle errors and return exit codes. | |
| **C6** | Strict output templates provided, with 2–3 input/output example pairs where style matters. | |
| **C7** | Zero hardcoded usernames or system paths (dynamic path resolution using `Path(__file__)`). | |
| **C8** | Required MCP tools are fully qualified (`Server:tool_name`) and documented. | |

---

## Section D: Verification & Automated Quality Loops

| # | Check Item | Score (0–2) |
|---|---|:---:|
| **D1** | Workflow contains an automated check the agent runs (`scripts/validate.py`, test suite, diff check). | |
| **D2** | Execution loop is defined: run check $\to$ inspect errors $\to$ fix $\to$ repeat until 100% pass. | |
| **D3** | Unattended runs are gated by strict stopping conditions. | |
| **D4** | Real evidence is demanded in final report (file paths, tool exit status, verification output). | |
| **D5** | Trigger tests verified: triggers on direct and paraphrased prompts; rejects unrelated tasks. | |
| **D6** | Output runs cleanly on multiple machines / operating systems. | |

---

## Section E: Unattended & Scheduled Jobs (If Applicable)

| # | Check Item | Score (0–2) |
|---|---|:---:|
| **E1** | Prompt is self-contained and states explicit success criteria and timezone. | |
| **E2** | Source reads utilize stateful bookmarks, not sliding time windows. | |
| **E3** | Failed reads are reported explicitly as unreadable (never "nothing found"). | |
| **E4** | External publications/posts recorded only after destination confirmation. | |
| **E5** | Read-only credentials used where applicable; spend cap enforced per run. | |

---

## Section F: Operational Invariants & House Rules

| # | Check Item | Score (0–2) |
|---|---|:---:|
| **F1** | Human confirmation checkpoint enforced before applying live production changes. | |
| **F2** | Every metric or data point is validated; zero hallucinated claims. | |
| **F3** | Standardized `_run.json` telemetry emitted upon completion. | |
| **F4** | Clear `.env.example` provided with zero credentials or tokens in code. | |

---

## Scorecard Result Summary

- **Total Score:** ____ / ____ $\to$ **____ %**
- **Blocking Zeros (in Section A or D):** ____
- **Final Decision:** [ ] **SHIP** (Score $\ge 80\,\%$, zero blocking zeros) / [ ] **FIX & RETEST**
