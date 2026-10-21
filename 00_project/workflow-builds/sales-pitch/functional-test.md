# Step 4.2 Functional Test Record: Sales Pitch Architecture (`sales-pitch`)

Date: 2026-10-17  
Workflow ID: `sales-pitch`  
Test Subject: Dr. Korinna Heintze (`korinna-heintze`)  

---

## 1. Execution Trace
- **Input Command:** `/sales-pitch korinna-heintze`
- **Audit Data Ingested:**
  - Prospect Domain: `korinnaheintze.de`
  - Review Page: `https://741.studio/review/korinna-heintze/`
  - Prior touchpoints: LinkedIn outreach, 3 WhatsApp audio/text checkpoints
  - Weaknesses detected: Single-Page-App with only 9 words in raw HTML, missing H1/H2, missing Google Analytics / GTM tracking.
- **Output Generated:**
  - `00_project/prospects/korinna-heintze/sales-cockpit.md` (Complete 60-minute live call guide).
- **Linter Execution:**
  - `python3 .claude/skills/sales-pitch/scripts/verify_pitch.py 00_project/prospects/korinna-heintze/sales-cockpit.md`
  - **Result:** `VERIFICATION PASSED: All 4 invariant checks succeeded.`

## 2. Invariants Verification
- [x] Zero prohibited guru names in deliverable.
- [x] All 6 chronological phases (Min 00–60) clearly articulated.
- [x] 3-Tier Offer Stack exact numbers verified (1.999 €, 3.699 €, 7.999 €).
- [x] Performance Guarantee explicitly framed before the price.

**Status:** PASS.


---

## Re-run 2026-10-21 (v1.1 offer update)
- **Input:** `/sales-pitch ulrike-roeth` (Martin chose this prospect in the card on 2026-10-21). Phases 1–3 kept, Phases 4–6 rebuilt with the new offer.
- **Output:** `00_project/prospects/ulrike-roeth/sales-cockpit.md`.
- **Linter:** `python3 .claude/skills/sales-pitch/scripts/verify_pitch.py 00_project/prospects/ulrike-roeth/sales-cockpit.md`
  - First run: `VERIFICATION FAILED` (1 error: the word "Starter" in a Phase 4 note). Fixed.
  - Second run: `VERIFICATION PASSED: All 10 invariant checks succeeded.`
- **Negative tests:** old cockpits `korinna-heintze` and the pre-update `ulrike-roeth` fail with 14 errors each (old prices, Starter, money-back, missing bonuses). A sample with the price before the anchor, value stack and guarantee fails with 3 order errors.
- **German script lines:** `deslop_de.py` 5/5 (after 2 dashes removed and the unsourced "44 Verzeichnisse" dropped; 40.000 € passed as a claim from the cockpit's own anchor math).

### Invariants (v1.1)
- [x] Zero prohibited guru names.
- [x] 6 phases with headings.
- [x] Power Engine 7.999 € before 4.999 € in Phase 4.
- [x] Value stack 15.000 € and Ergebnis-Garantie (Top 3 Google Maps, ohne Zusatzkosten weiter) before 4.999 €.
- [x] No Starter / 1.999 / 3.699 / −10 % / struck-through prices / money-back.
- [x] Bonuses 397 € and 48 h, full payment default, 60 % fallback.
- [x] Referral photo ask only in Phase 6; Gebietsschutz named.

**Status:** PASS.
