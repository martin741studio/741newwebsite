# Degrees of Freedom Audit: P4/P0 CRO Track B Design-Intense Showcase (`cro_b`)

Date: 2026-10-16
Workflow ID: `cro_b`
Rule Reference: Rule R1.7 (Strict Separation of Deterministic Scripts vs Creative Heuristics)

---

## 1. Allocation Matrix

| Step | Task Description | Type | Execution Mode | Tool / Script | Freedom Degree |
|---|---|---|---|---|---|
| **B0** | Grill-Me Brief Intake | Qualitative | Heuristic Prompt | `SKILL.md` guidance | Low (Strict template) |
| **B1** | Asset Scrape & Fact Inventory | Deterministic | Heuristic + Web Scraping | Firecrawl / Chrome | Low |
| **B2** | Reference Board Curation | Creative | Heuristic Research | Mobbin / Refero / Awwwards | Medium |
| **B2b** | Element Pool Compilation | Mixed | Template + Dynamic Coding | `00-element-pool/` generator | Low-Medium |
| **B2b** | Element Pool Serving & Vote Save | Deterministic | Isolated Script | `scripts/serve_pool.py` | Zero (Strict HTTP/JSON) |
| **B3** | Copy Review & Gates | Mixed | Gate Script + Qualitative | `content-writing/run_gates.py` | Low |
| **B4** | Concept & Storyboard Synthesis | Creative | Heuristic Prompt | `SKILL.md` guidance | Medium (Bounded by votes) |
| **B5** | Design Doc & Media Plan | Mixed | Heuristic Document | Markdown template | Low |
| **B6** | Media Asset Generation | Creative | External API / Image Gen | ChatGPT / DALL-E / SVG | Medium |
| **B7** | HTML Prototype Implementation | Mixed | Heuristic Code | HTML5 / CSS3 / SVG / Canvas | Medium (Strict 1440px rules) |
| **B7** | Remote Upload Interception | Deterministic | Security Guard Hook | `scripts/guard_upload.py` | Zero (Binary block) |
| **B8** | Performance & Metric Measurement | Deterministic | Browser JS Script | `scripts/measure.js` | Zero (Raw DOM metrics) |
| **B8** | Visual & Gate Verification | Deterministic | Verification Script | `scripts/verify.py` | Zero (Binary pass/fail) |
| **B9** | Drive Staging & Packaging | Deterministic | Packaging Script | `scripts/stage_drive.py` | Zero (Deterministic copy) |

---

## 2. Invariant Guardrails
1. **Zero Math in Prompts:** Calculations for viewport heights, contrast ratios, asset byte sizes, and voting tallies MUST run through deterministic scripts.
2. **Deterministic Vote Storage:** Votes from the element pool must be saved directly to `votes.json` via HTTP POST, never parsed manually from conversational chat text.
3. **Binary Safety Hooks:** The upload guard hook (`guard_upload.py`) operates unconditionally outside the model's discretion.
