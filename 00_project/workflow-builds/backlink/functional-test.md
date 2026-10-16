# Backlink DACH Functional Test

Workflow ID: backlink
Date: 2026-10-16
Dataset: Martin Hüwel Pilot Dataset (`00_project/assets/huewel/backlink/`)

## Execution Summary
- **Client:** Martin Hüwel (Nürnberg)
- **Mode:** Pilot Backlink Prospecting
- **Sheet Deliverable:** `https://docs.google.com/spreadsheets/d/14vAGfgq1CzwkTaU3RKr9RUNeFG8HEvywJbsuH2EQseI/edit`

## Pipeline Verification
1. **Pillar A Border Separation:**
   - Evaluated candidate link list; verified that all general and niche directories (Jameda, Doctolib, Gelbe Seiten) were routed to the Citations module.
   - `build_sheet.py` enforced 0 Pillar A rows in the backlink sheet.
2. **Local Ecosystem Prospecting (Pillar B):**
   - Identified regional Chambers (IHK/HWK) and professional associations with membership-linked directory pages.
3. **Traceability & Proof Check:**
   - Every row contains a verified Quelle, Kontakt, and DR approximation formula (`round(min(rank/10, 100))`).
4. **Approval Box Integration:**
   - Every row equipped with an explicit `Freigabe` checkbox for Martin's review before outreach.
5. **Telemetry Adherence:**
   - Verified that `_run.json` is logged in `00_project/assets/huewel/backlink/2026-10-11/_run.json`.

## Verification Result: PASS
- All scripts executed deterministically.
- Strict human-gated outreach boundary enforced.
- Validated output ready for Checkpoint 0 & 4 reviews.
