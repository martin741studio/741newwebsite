# 2.1 Use Cases: P4 CRO Homepage Track A (`cro`)

Date: 2026-10-16
Workflow: CRO Homepage Track A (`cro`)

---

### Use Case 1: Standard Healing Practice / Local Business Homepage Prototype
- **Trigger:** `/cro-homepage "Praxis Dumann", https://osteopathie-dumann.de, https://maps.google.com/..., WhatsApp`
- **Steps:**
  1. Scrape live site content, branding colors, and logo.
  2. Ingest content-pool keywords and site structure (`content-pool/04-pool/pool-top.md`).
  3. Write conversion copy through `content-writing` skill; run HWG compliance check.
  4. Generate GPT mockup visual style reference.
  5. Code 1440px desktop HTML prototype with 701px above-the-fold hero, proof hover, and conversion CTA.
  6. Run Chrome visual check (`00_project/cro-homepage-visual-check.md`) and verify script.
  7. Stage and upload deliverable pack to Google Drive (`CRO Homepage`).
- **Deliverable:** Approved HTML prototype, Drive package, full-page screenshot.

### Use Case 2: Law Firm Homepage Prototype (BRAO Compliance Mode)
- **Trigger:** `/cro-homepage "Kanzlei Leichsenring", https://leichsenring-bauanwaelte.de, ..., Telefon`
- **Steps:**
  1. Ingest practice specialties, court admissions, and attorney credentials.
  2. Run Anwaltswerbe-Check (BRAO § 43b, BORA § 6, UWG): suppress unproven superlative claims, use formal address (Sie).
  3. Build authoritative, restrained editorial layout with architectural spacing.
  4. Complete visual check and handoff pack.
- **Deliverable:** BRAO-compliant legal prototype with verified credential badges.

### Use Case 3: Resume Existing In-Progress Run
- **Trigger:** "Mach den CRO-Lauf für Dumann weiter"
- **Steps:**
  1. Read `00-lead-info.md` and `_status.md` in local asset folder or Drive mirror.
  2. Identify last completed checkpoint (e.g. Step 3 copy approved).
  3. Resume immediately at next step (Step 4 design doc) without re-scraping or restarting.
- **Deliverable:** Continued run output updated in `_status.md`.
