# Test Scenarios: P4/P0 CRO Track B Design-Intense Showcase (`cro_b`)

Date: 2026-10-16
Workflow ID: `cro_b`

---

## Scenario 1: Obvious Case — High-End Law Firm Showpiece (Dr. Stürzl)
- **Input:** `/cro-track-b stuerzl https://stuerzl-steuerstrafrecht.de` with complete brand assets, Anthrazit/Salbei palette, and approved B0 questionnaire.
- **Expected Behavior:**
  1. Pipeline initiates B0 intake, validates against BRAO rules (formal Sie address, no Fachanwalt claim without certificate).
  2. B2b compiles and serves live Element Pool on local HTTP server (`localhost:8080/00-element-pool/`).
  3. Halts at Checkpoint 1 for Martin's votes; reads `votes.json`.
  4. Synthesizes B4 concept: 1 signature idea ("Briefbogen"), max 4 interactive components.
  5. Assembles 1440px HTML prototype with X-ray toggle and reduced-motion fallback.
  6. Passes `verify.py` and Chrome visual check.
- **Expected Output:** Working local prototype, zero blocking errors, complete handoff pack.

---

## Scenario 2: Paraphrase Trigger — Elevated Brand Pitch Request
- **Input:** "Martin: Bau eine design-starke Showpiece-Startseite für Stürzl, die wir gegen Track A vergleichen können."
- **Expected Behavior:** Paraphrase correctly resolves to `cro_b` workflow, activates B0 questionnaire and prepares live Element Pool.
- **Expected Output:** B0 brief drafted and pipeline initialized.

---

## Scenario 3: Negative Trigger (Must-Not-Trigger) — Standard Practice / Health Practice (HWG)
- **Input:** `/cro-track-b suriya https://praxis-suriya.de` (Medical Practice) OR standard local conversion run without design-intense need.
- **Expected Behavior:**
  1. This workflow **MUST-NOT-TRIGGER** for standard conversion homepages, local practices, or health practitioners bound by HWG.
  2. The membrane boundary check detects health practice keywords and triggers the negative filter: `MUST NOT TRIGGER cro_b for health clients (HWG) or standard local practices. Route to standard Track A (cro-homepage).`
  3. Halts with zero state pollution.
- **Expected Output:** Refusal to trigger `cro_b`; clean delegation to `cro-homepage`.
