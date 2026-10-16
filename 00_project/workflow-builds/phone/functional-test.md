# Maps Playbook Functional Test

Workflow ID: phone
Date: 2026-10-16
Dataset: Existing Local Client Datasets (Praxis Suriya & Martin Hüwel)

## Execution Summary
- **Client:** Praxis Suriya / Martin Hüwel
- **Mode:** Local 77-Measure Matrix Verification
- **Catalog:** `00_project/maps-playbook-measure-catalog.json` (77 measures)

## Pipeline Verification
1. **Catalog Validation (`scripts/validate_catalog.py`):**
   - Output: `measures=77 classes={'DO': 56, 'GATE': 20, 'OUT': 1} errors=0`
   - Verified dependency graph, runbook references, and gate definitions.
2. **Audit Feed Integration:**
   - 69 of 77 measures populated directly from existing audit findings.
   - Zero redundant API queries executed.
3. **Harm Dependency Lock:**
   - Verified that measures blocked by un-burning harm items (e.g. G01, G02, G04, O02) are held in `blocked` status while `harm-register.json` has open red flags.
4. **Task Scoring & Phasing (`scripts/score.py`):**
   - Output: Tasks partitioned into `d1-30` (quick wins), `m2+` (medium-term builds), and `later`.
5. **Sheet & Board Generation (`scripts/build_sheet.py` & `scripts/render_board.py`):**
   - Verified internal HTML visual board and client workbook generation with zero formatting errors.

## Verification Result: PASS
- All scripts executed deterministically.
- Accurate gap scoring and un-burning dependency enforcement.
- Validated output ready for Checkpoint A, B, C reviews.
