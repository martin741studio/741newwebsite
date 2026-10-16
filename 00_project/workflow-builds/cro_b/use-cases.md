# Use Cases: P4/P0 CRO Track B Design-Intense Showcase (`cro_b`)

Date: 2026-10-16
Workflow ID: `cro_b`

---

## Use Case 1: High-Ticket Client Choice Pitch (Dr. Stürzl Steuerstrafrecht)
- **Context:** Client Dr. Stürzl pays €7,999 + Ads and is presented with two distinct directions: Variant A (calm, classical legal editorial) and Variant B (design-intense Briefbogen aesthetic with subtle kinetic touches).
- **Trigger:** `/cro-track-b stuerzl https://stuerzl-steuerstrafrecht.de` or Martin prompt "Track B für Stürzl".
- **Execution Steps:**
  1. Intake B0 questionnaire (`brief-b.md`) confirming client context, audience stress state, and strict Anwaltswerbe-Check boundaries.
  2. Inventory brand assets (SVG logo, anthrazit/salbei palette) and verified facts.
  3. Curate reference board (5 references with take/leave notes, 2 anti-references).
  4. Build and serve live Element Pool (`00-element-pool/index.html`) on local server; Martin votes Ja / Vielleicht / Nein on 24 micro-interactions.
  5. Assemble concept & storyboard (`05-gpt-design-doc/concept/concept.md`) featuring signature idea ("Der Briefbogen") and max 4 interactive components.
  6. Code 1440px desktop HTML prototype with SVG/canvas motion layer, reduced-motion fallbacks, and X-ray toggle (`x`).
  7. Run 10-point Track B QA suite (`verify.py`, `measure.js`, visual check in Chrome).
  8. Stage Drive mirror and handoff pack.
- **Tools:** Terminal, Firecrawl, Claude in Chrome, `serve_pool.py`, `guard_upload.py`, `verify.py`, `measure.js`.
- **Deliverable:** Local working prototype (`07-prototype/index.html`), handoff documentation (`08-handoff/handoff.md`), component shoot list, Drive mirror.

---

## Use Case 2: Premium Prospect Showcase (Phase 0 Pitch)
- **Context:** Pitching a high-ticket agency, architectural practice, or boutique advisory where standard conversion templates feel generic and fail to win the mandate.
- **Trigger:** `/cro-track-b <prospect> <url> --mode prospect`
- **Execution Steps:**
  1. Autonomous scrape of prospect branding and visual language.
  2. Generation of targeted B0 brief based on industry tier.
  3. Interactive Element Pool generation emphasizing bespoke typography and kinetic dividers.
  4. Martin review and vote.
  5. High-speed prototype compilation highlighting X-ray code inspection to impress technical decision-makers during pitch calls.
- **Tools:** Chrome, local server, `verify.py`.
- **Deliverable:** 1440px showpiece prototype demonstrating technical and aesthetic mastery.

---

## Use Case 3: Retainer Brand Refresh (Phase 4 Retainer Client)
- **Context:** An established 741 client in Phase 4 whose search rankings are secure wants to upgrade their digital flagship to dominate competitor prestige.
- **Trigger:** `/cro-track-b <client> <url> --refresh`
- **Execution Steps:**
  1. Ingest existing Supabase dataset and verified conversion metrics.
  2. B0 questionnaire confirms refresh scope and preserve-list (proven headlines, phone placement).
  3. Element Pool vote filters out intrusive animations.
  4. Build prototype ensuring full compliance with performance budget (<2.5 MB above fold) and accessibility standards.
- **Tools:** Supabase, Chrome DevTools, `guard_upload.py`, `verify.py`.
- **Deliverable:** Approved prototype ready for production CMS migration by agency developer (Dinakar).
