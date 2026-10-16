# Step 0.0 Inputs Grill Record: P4/P0 CRO Track B Design-Intense Showcase (`cro_b`)

Date: 2026-10-16
Owner: Martin Drendel
Workflow ID: `cro_b`
Status: Confirmed

---

## 1. The Job (Objective & Scope)
- **What enters:** Client name and website URL; B0 Grill-Me questionnaire (`00-brief-b/brief-b.md`); brand assets and verified colors; reference board shortlist (`02-data/references/`); voted element pool results (`00-element-pool/votes.json`).
- **What transforms:**
  1. Scrapes live brand identity and copies verified facts into dataset.
  2. Generates live interactive element pool (`00-element-pool/index.html`) featuring 20–35 animated/interactive components in client brand styling.
  3. Records Martin's votes (`Ja`, `Vielleicht`, `Nein`) via local server (`serve_pool.py`).
  4. Synthesizes concept and section storyboard (`05-gpt-design-doc/concept/concept.md`) with 1 signature idea and maximum 4 selected interactive components.
  5. Implements desktop 1440px HTML prototype featuring SVG/CSS/canvas motion layer, hidden X-ray switch (`?xray=1` or `x`), and `prefers-reduced-motion` fallbacks.
  6. Executes rigorous 10-point Track B QA verification (`perf.md`, `visual-check.md`, `self-check.md`) and packages local handoff and Drive mirror.
- **Who uses output:** Martin (for high-stakes pitch / A vs B client comparison), premium client / partner (e.g. Dr. Anja Stürzl), agency developer (Dinakar).

## 2. Runtime Surface
- **Primary surface:** Terminal (`/cro-track-b <client>` or `cro_b`), Claude in Chrome (for visual check, pool voting review, Drive upload), local HTTP server (`python3 -m http.server`).
- **Enforcement surface:** `scripts/guard_upload.py` (strictly intercepts remote deployment), `scripts/verify.py`, `scripts/serve_pool.py`.

## 3. Cadence / Frequency
- **Turnus:** On demand per client during Phase 4 (Build-up) or Phase 0 (High-ticket prospect showcase) where market and brand demand an elevated design statement.

## 4. Hard Limits (Failure Boundaries)
- **Zero Remote Server Uploads:** Prototypes remain strictly local. Remote server uploads (`rsync`, `scp`, `curl`, `sftp`) are blocked by `guard_upload.py`.
- **Zero Unjustified Motion:** Every moving component must have an explicit conversion or brand rationale. Maximum 4 interactive components from the component catalog.
- **Strict Compliance:** Health practices (HWG) are prohibited from Track B unless Martin overrides in writing. Law firms (BRAO § 43b, BORA § 6) require strict Anwaltswerbe-Check and formal address ("Sie").
- **Performance Budget:** First screen < 2.5 MB, whole page < 12 MB, video loops < 2 MB. Zero long tasks > 100 ms during full scroll.
- **Accessibility & Contrast:** `prefers-reduced-motion` must show static fallback/poster images. Primary CTA must remain visible at 701px viewport height during intro animations. Text contrast over video/motion layers must maintain ≥ 4.5:1 ratio at every frame.
