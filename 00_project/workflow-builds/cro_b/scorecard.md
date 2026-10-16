# Scorecard: CRO Track B Design-Intense Showcase (`cro_b`)

Date: 2026-10-16
Raster: `00_project/knowledge/workflow-library/_derived/scorecard.md`
Workflow ID: `cro_b` (`cro-track-b`)

---

## Detailed Evaluation Table

| # | Check | Score | Evidence / Rationale |
|---|---|---|---|
| **A1** | Right building block | 2 | Skill (`cro-track-b`) + isolated scripts (`serve_pool.py`, `guard_upload.py`, `verify.py`) |
| **A2** | Rules in CLAUDE.md, procedure in skill, enforcement in hooks | 2 | `guard_upload.py` hook active and verified via test harness |
| **A3** | Side-effect skills set to manual only | 2 | Prototypes stay local only; upload commands intercepted by hook |
| **A4** | Enabled for Cowork or routines | 1 | Terminal CLI & Claude Code environment |
| **B1** | Use cases written | 2 | 3 use cases in `use-cases.md` (High-ticket client, Pitch, Refresh) |
| **B2** | Test scenarios BEFORE the body | 2 | Documented in `test-scenarios.md` with explicit must-not-trigger |
| **B3** | One hard task solved by hand first | 2 | Dr. Anja Stürzl pilot documented in `hand-run.md` |
| **B4** | Inputs, deliverable, out-of-scope | 2 | B0 questionnaire, element pool, strict out-of-scope boundaries |
| **B5** | Degrees of freedom | 2 | Rule R1.7 mapping in `freedom.md` |
| **C1** | Description WHAT, WHEN, negative trigger | 2 | Strict WHAT + WHEN + negative trigger in frontmatter |
| **C2** | Name rules | 2 | Lowercase hyphenated `cro-track-b` |
| **C3** | Body under 500 lines, references one level deep | 2 | `SKILL.md` is 135 lines (< 500 ceiling) |
| **C4** | Checklist | 2 | Sequential step-by-step checklist B0–B9 with gates |
| **C5** | Scripts run, not read | 2 | Isolated `.py` and `.js` in `scripts/` |
| **C6** | Output templates and examples | 2 | Templates and worked examples from Stürzl pilot |
| **C7** | One term per concept, no time-sensitive text | 2 | Standardized terms across all documentation |
| **C8** | MCP tools fully qualified | 1 | Fully qualified paths |
| **D1** | Check Claude can run | 2 | `verify.py`, `measure.js`, `serve_pool.py` verified |
| **D2** | Loop stated | 2 | Verification loop in `SKILL.md` |
| **D3** | Unattended runs gated | 1 | Checkpoint 1 & 2 human-in-the-loop gates |
| **D4** | Evidence in the final report | 2 | Drive link, screenshot, visual check report line |
| **D5** | Trigger tests passed | 2 | T1–T6 executed and verified in `trigger-tests.md` |
| **D6** | Baseline with and without | 2 | Baseline documented in `baseline.md` (~78% time savings) |
| **F1** | Client message and Drive link | 2 | Mandatory Drive mirror and screenshot in final report |
| **F2** | Per-change go before live changes | n/a | Prototypes strictly local |
| **F3** | Data verified | 2 | Every fact cited to dataset or marked `[FEHLT]` |
| **F4** | STE in replies | 2 | Agent instructions in STE; client deliverables in German |
| **F5** | No method sources in client material | 2 | Enforced via `verify.py` and visual check |

---

## Summary Result

**Total Score: 50 / 54 = 92.6 %**
**Blocking zeros: 0**

### Gate Compliance
- [x] Overall score $\ge 80.0\%$ (Actual: 92.6 %)
- [x] Blocking zeros: 0
- [x] Trigger tests verified (Section D5 = 2)
- [x] Baseline documented (Section D6 = 2)
