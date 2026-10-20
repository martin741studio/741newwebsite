# Scorecard: Co-Marketing & Backlink Collaboration Workflow (`collab-content`)

Date: 2026-10-16
Raster: `00_project/knowledge/workflow-library/_derived/scorecard.md`
Workflow ID: `collab-content`

---

## Detailed Evaluation Table

| # | Check | Score | Evidence / Rationale |
|---|---|---|---|
| **A1** | Right building block | 2 | Skill (`collab-content`) + isolated deterministic scripts (`lint_collab.py`, `write_run.py`) |
| **A2** | Rules in CLAUDE.md, procedure in skill, enforcement in hooks | 2 | Workflow procedure in `.claude/skills/collab-content/SKILL.md`, rules in `inputs-grill.md` |
| **A3** | Side-effect skills set to manual only | 2 | Gated by Checkpoints 1 & 2 before any file dispatch or CMS publishing |
| **A4** | Enabled for Cowork or routines | 2 | Multi-surface support: Antigravity IDE and Claude Code |
| **B1** | Use cases written | 2 | 3 use cases in `use-cases.md` (End-to-end, Synergy Screening, Inbound Review) |
| **B2** | Test scenarios BEFORE the body | 2 | 3 scenarios (Obvious, Paraphrase, Negative boundary) in `test-scenarios.md` |
| **B3** | One hard task solved by hand first | 2 | Bali Healing x Ayurvedagram Bali pilot documented in `hand-run.md` |
| **B4** | Inputs, deliverable, out-of-scope | 2 | Defined in `inputs-grill.md`, `pipeline.md`, and `spec.json` |
| **B5** | Degrees of freedom | 2 | Rule R1.7 separation strictly mapped in `pipeline.md` |
| **C1** | Description WHAT, WHEN, negative trigger | 2 | Comprehensive frontmatter in `SKILL.md` with explicit negative trigger |
| **C2** | Name rules | 2 | Lowercase hyphenated `collab-content` |
| **C3** | Body under 500 lines, references one level deep | 2 | `SKILL.md` is 75 lines (< 500 ceiling), references 1 level deep |
| **C4** | Checklist | 2 | Step-by-step checklist Phase 1–6 with explicit gates |
| **C5** | Scripts run, not read | 2 | Deterministic logic isolated in `scripts/lint_collab.py` and `scripts/write_run.py` |
| **C6** | Output templates and examples | 2 | Starter template in `assets/collab-template.json` and real pilot pair in `00_project/assets/balihealing/collab/` |
| **C7** | One term per concept, no time-sensitive text | 2 | Consistent terminology (Mini-Pool, Angle, Co-Marketing Guide) |
| **C8** | MCP tools fully qualified | 2 | Fully qualified tool names where applicable |
| **D1** | Check Claude can run | 2 | `lint_collab.py` and `write_run.py` executed cleanly |
| **D2** | Loop stated | 2 | Cybernetic regulation loop documented in `collab-content-workflow.md` |
| **D3** | Unattended runs gated | 2 | Checkpoint 1 & 2 human-in-the-loop decision cards |
| **D4** | Evidence in the final report | 2 | Telemetry `_run.json` emitted at checkpoint |
| **D5** | Trigger tests passed | 2 | 3 trigger tests verified in `trigger-tests.md` |
| **D6** | Baseline with and without | 2 | Documented in `baseline.md` (-95% ideation time, zero HTML errors) |
| **F1** | Client message and Drive link | 2 | Deliverables mapped to client assets and staging folders |
| **F2** | Per-change go before live changes | 2 | Strict staging isolation; execution gated before live CMS or partner handoff |
| **F3** | Data verified | 2 | Real partner crawl from `ayurvedagrambali.com` and authentic baseline from `balihealing` |
| **F4** | STE in replies | 2 | Architectural specifications written in ASD-STE100 |
| **F5** | No method sources in client material | 2 | Internal procedural references separated from client deliverables |

---

## Summary Result

**Total Score: 56 / 56 = 100 %**
**Blocking zeros: 0**

### Gate Compliance
- [x] Overall score $\ge 80.0\%$ (Actual: 100 %)
- [x] Blocking zeros: 0 (No zero in any section)
- [x] Trigger tests verified (Section D5 = 2)
- [x] Baseline documented (Section D6 = 2)
