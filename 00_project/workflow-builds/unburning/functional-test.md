# Un-Burning Functional Test

Workflow ID: unburning
Date: 2026-10-16
Dataset: Praxis Suriya Dry Run (`00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/`)

## Execution Summary
- **Client:** Praxis Suriya (Ingelheim)
- **Mode:** `scan` / Read-Only Dry Run
- **Run Directory:** `00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/`

## Pipeline Verification
1. **Preconditions Check:**
   - Evaluated locked NAP master: `Schützenpfad 29, 55218 Ingelheim am Rhein`.
   - Access verified; Area A ownership decoupled and marked precondition.
2. **Multi-Area Scan & Merge:**
   - Scanned Areas C (GBP & Citations), D (Website SEO & Content), and E (Google Index).
   - Executed `scripts/merge_parts.py` across part folders.
   - Identified 56 total harm items.
3. **Deterministic Validation (`scripts/validate_run.py`):**
   - Output: `VALID: 56 items` (0 schema errors).
4. **Bedrock Calculation (`scripts/bedrock.py`):**
   - Area C: RED (22 open items, 11 blocking revenue, e.g. old address on 11 directories).
   - Area D: YELLOW (12 open items, 8 technical leaks).
   - Area E: YELLOW (8 open items, 7 index leaks).
   - `ready_for_growth: false` (accurately enforces gate that Area C growth measures are blocked until old address is cleared).
5. **Report Generation (`scripts/build_report.py`):**
   - Internal HTML damage map and client-safe draft generated.
6. **Change Safety & Rollbacks:**
   - Changes staged in `changes.json` with pre-validation via `validate_changes.py`.
   - Zero live destructive actions executed without explicit GO-1 and GO-2.

## Verification Result: PASS
- All scripts executed deterministically.
- Accurate harm vs. gap classification.
- Validated output ready for Checkpoint 1 & 2 reviews.
