---
name: cro-track-b
description: Run the 741 CRO Homepage Track B (Design-Intense Showpiece) workflow for premium clients (boutique law firms, design agencies, high-ticket studios, SaaS) where brand prestige and competitive differentiation demand an elevated visual statement and interactive choice. Transforms a brief and brand inventory into an interactive Element Pool, approved concept storyboard with signature idea, 1440px desktop HTML prototype with code motion layer, X-ray switch, and local handoff pack. Trigger on "CRO Track B for <name>", "Track B für <client>", "Design-intensiver Prototyp für <client>", or "/cro-track-b <client> <url>". Do NOT use for standard conversion runs (use cro-homepage / Track A), health practices under HWG (unless Martin expressly overrides in writing), plain SEO content briefs (seo-page-optimizer), or review pages (local-seo-review-page).
---

# cro-track-b: CRO Track B (Design-Intense Showpiece)

## Critical Rules

1. **Prototypes Stay Strictly Local:** Never upload prototypes to external staging or production servers. Remote upload commands are intercepted by `scripts/guard_upload.py`.
2. **Never Skip the Live Element Pool:** Step B4 (Concept) is strictly blocked until Martin has voted on the live Element Pool in `00-element-pool/index.html` (served via `scripts/serve_pool.py`) and `votes.json` exists.
3. **No Moving Parts Without Purpose:** Every animated or kinetic element must have an explicit conversion or brand rationale. Maximum 4 interactive components from the component catalog.
4. **Performance & Accessibility Budget:**
   - First screen weight: < 2.5 MB.
   - Total page weight: < 12 MB.
   - Video loops: < 2 MB, muted, loop seamlessly (last frame = first frame), paused when off-screen.
   - `prefers-reduced-motion` media query must render static fallback / poster images with zero broken layouts.
   - Primary CTA must remain visible at 701px viewport height during any intro animation.
   - Text contrast over motion/video layers must maintain ≥ 4.5:1 ratio at every frame.
5. **Strict Compliance Guardrails:**
   - **HWG (Health):** Prohibited by default. Do NOT run Track B for medical/health practitioners without Martin's explicit written override.
   - **BRAO (Legal):** Formal address ("Sie"), strict Anwaltswerbe-Check (no unproven specialist claims, no fear graphics, no scales/handcuffs).
6. **Universal Telemetry:** Emit `_run.json` at every milestone and on completion.

---

## Run Kit & Tools

- **Serving Element Pool:** `python3 scripts/serve_pool.py <port> 00-element-pool`
- **Verification Script:** `python3 scripts/verify.py <cro-dir> [--proto 07-prototype]`
- **DOM Measurement:** Paste `scripts/measure.js` into Claude in Chrome DevTools console.
- **Drive Staging:** `python3 scripts/stage_drive.py <cro-dir> --version v1`
- **Registry Sync:** `python3 00_project/workflow-registry/workflow_registry.py upsert --client "<client>" --workflow cro_b --status "in Arbeit"`

---

## Step-by-Step Execution Checklist

```
[ ] B0: Grill-Me Brief Intake
    - Run 3-round questionnaire from `00_project/cro-track-b-questionnaire.md`.
    - Record answers in `00-brief-b/brief-b.md`. Reject vague answers ("modern", "clean").
    - Gate B0: All blocks answered; emotional landing state and brand limits defined.

[ ] B1: Brand & Data Inventory
    - Ingest live site branding (SVG logo, hex colors) and verified facts into `02-data/dataset.md` and `02-data/brand.md`.
    - Every claim must trace to verified records or carry `[FEHLT]`.

[ ] B2: Reference Board & Elements Catalog
    - Curate 5 reference websites (Refero, Mobbin, Awwwards) with explicit "take" and "leave" rationale in `02-data/elements-catalog.md`.
    - Document 2 anti-references.

[ ] B2b: Live Element Pool (Human-in-the-Loop Gate)
    - Compile 20–35 live interactive components into `00-element-pool/index.html` styled with client branding.
    - Launch local server: `python3 scripts/serve_pool.py 8815 00-element-pool`.
    - CHECKPOINT 1: Martin interacts and votes (Ja / Vielleicht / Nein).
    - Ensure `00-element-pool/votes.json` is saved.

[ ] B3: Approved Copy
    - Ingest approved copy from Track A (`04-copy/approved-copy.md`) or run through `content-writing` skill.
    - Ensure H1 contains primary entity and target city.

[ ] B4: Concept & Storyboard
    - Formulate 1 signature idea (e.g. "Der digitale Briefbogen").
    - Select maximum 4 interactive components from the "Ja" and "Vielleicht" pool votes.
    - Write section-by-section storyboard in `05-gpt-design-doc/concept/concept.md`.

[ ] B5: Design Doc & Media Plan
    - Finalize technical design document in `05-gpt-design-doc/design-doc.md`.
    - Detail media slots (stills, SVG loops, canvas animations) in `06-gpt-assets/media/MEDIA-PLAN.md`.

[ ] B6: Media Generation & Mockup
    - Generate full-page visual mockup and high-resolution stills.
    - Verify loop continuity (last frame equals first frame).

[ ] B7: HTML Build with Motion Layer
    - Code 1440px desktop HTML prototype in `07-prototype/index.html`.
    - Implement code-based motion layer (SVG / Canvas / CSS).
    - Integrate hidden X-ray switch (`key 'x'` and `?xray=1`) outlining code vs media layers.
    - Implement full `prefers-reduced-motion` CSS overrides.

[ ] B8: QA Suite & Verification
    - Execute 10-point Track B QA checks (T1–T10).
    - Measure DOM via `scripts/measure.js`.
    - Run deterministic verify script: `python3 scripts/verify.py <run-dir>`.
    - Complete `07-prototype/visual-check.md` with report line:
      "Visual check done in Chrome, N items checked, N fixed, N open".
    - Complete `07-prototype/self-check.md` with total score.
    - CHECKPOINT 2: Martin final prototype review.

[ ] B9: Handoff & Drive Mirror
    - Compile `08-handoff/handoff.md` with component inventory and CMS feasibility notes.
    - Stage Drive files: `python3 scripts/stage_drive.py <run-dir>`.
    - Upload files to Google Drive folder using Chrome browser upload.
    - Record run completion in `_run.json` and sync `workflow_registry.py`.
```

---

## 10-Point Track B QA Table (Step B8)

| # | Check | Requirement |
|---|---|---|
| **T1** | Frame Rate | Zero visible stutter; zero long tasks > 100 ms during full scroll. |
| **T2** | Video Loops | Seamless looping without jump; last frame equals first frame. |
| **T3** | Off-Screen Media | Video and canvas animations paused when scrolled out of view. |
| **T4** | Reduced Motion | `prefers-reduced-motion` renders clean layout with static poster images. |
| **T5** | Component Isolation | Prototype functions cleanly with interactive components disabled. |
| **T6** | Weight Budget | Above-the-fold < 2.5 MB, full page < 12 MB, loops < 2 MB. |
| **T7** | X-Ray Switch | Working toggle (`x` key) displaying layer boundaries and labels. |
| **T8** | Above-the-Fold CTA | CTA clearly visible at 701px viewport height during intro animation. |
| **T9** | Keyboard Navigation | All interactive components, drawers, and forms reachable via Tab. |
| **T10** | Dynamic Contrast | Text over motion/video maintains ≥ 4.5:1 contrast at all times. |

---

## Verification & Telemetry

On every run, before marking complete:
1. `python3 scripts/verify.py <run-dir>` must output `VERIFICATION SUCCESSFUL (Track B rules satisfied)`.
2. `_run.json` must be written with status `COMPLETED`, listing artifacts, gate timestamps, and visual check results.
