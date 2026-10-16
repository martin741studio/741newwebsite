# Scorecard: CRO Homepage Track A (`cro`)

Date: 2026-10-16 (Re-evaluation after trigger tests and baseline resolution)
Raster: `00_project/knowledge/workflow-library/_derived/scorecard.md`
Prior Score: 43 / 54 (80 %, with blocking zeros D5, D6)

---

## Detailed Evaluation Table

| # | Check | Score | Evidence / Rationale |
|---|---|---|---|
| **A1** | Right building block | 2 | Skill + isolated verification scripts + upload guard hook |
| **A2** | Rules in CLAUDE.md, procedure in skill, enforcement in hooks | 2 | `guard_upload.py` hook active; verified via test harness |
| **A3** | Side-effect skills set to manual only | 1 | Prototypes local only; upload requires Martin's confirmation |
| **A4** | Enabled for Cowork or routines | 1 | Terminal CLI & Claude Code |
| **B1** | Use cases written | 2 | 3 use cases in `use-cases.md` (Practice, Law firm, Resumable) |
| **B2** | Test scenarios BEFORE the body | 2 | Documented in `test-scenarios.md` with negative trigger |
| **B3** | One hard task solved by hand first | 2 | Dumann & Adel pilots documented in `hand-run.md` |
| **B4** | Inputs, deliverable, out-of-scope | 2 | Strict 4-parameter intake; Track B out of scope |
| **B5** | Degrees of freedom | 2 | Rule R1.7 mapping in `freedom.md` |
| **C1** | Description WHAT, WHEN, negative trigger | 2 | Strict WHAT + WHEN + negative trigger in frontmatter |
| **C2** | Name rules | 2 | Lowercase hyphenated `cro-homepage` |
| **C3** | Body under 500 lines, references one level deep | 2 | `SKILL.md` is 127 lines (< 500 ceiling) |
| **C4** | Checklist | 2 | Run checklist template in `assets/templates/` |
| **C5** | Scripts run, not read | 2 | Isolated `.py`, `.js`, and `.sh` in `scripts/` |
| **C6** | Output templates and examples | 2 | Templates and worked examples provided |
| **C7** | One term per concept, no time-sensitive text | 1 | Documented concepts |
| **C8** | MCP tools fully qualified | 1 | Fully qualified tool paths |
| **D1** | Check Claude can run | 2 | `verify.py`, `measure.js`, `check_prompt.py` |
| **D2** | Loop stated | 2 | Verification loop in `SKILL.md` |
| **D3** | Unattended runs gated | 1 | Fresh reviewer agent at Checkpoint 2 |
| **D4** | Evidence in the final report | 2 | Drive link, screenshot, visual check report |
| **D5** | Trigger tests passed | **2** (↑) | **Resolved:** T1–T6 executed and verified in `trigger-tests.md` |
| **D6** | Baseline with and without | **2** (↑) | **Resolved:** Baseline documented in `baseline.md` (~85% time savings) |
| **F1** | Client message and Drive link | 2 | Mandatory Drive mirror and screenshot in final report |
| **F2** | Per-change go before live changes | n/a | Prototypes local only |
| **F3** | Data verified | 2 | Every fact cited to dataset or marked `[FEHLT]` |
| **F4** | STE in replies | 1 | Agent instructions in STE; client deliverables in German |
| **F5** | No method sources in client material | 2 | Enforced via `verify.py` and visual check |

---

## Summary Result

**Total Score: 47 / 54 = 87.0 %**
**Blocking zeros: 0** (Prior blockers D5 and D6 both upgraded to 2/2).

### Gate Compliance
- [x] Overall score $\ge 80.0\%$ (Actual: 87.0 %)
- [x] Blocking zeros: 0
- [x] Trigger tests verified (Section D5 = 2)
- [x] Baseline documented (Section D6 = 2)
