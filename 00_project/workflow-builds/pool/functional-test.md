# Content Pool Functional Test

Workflow ID: pool
Date: 2026-10-16
Dataset: Praxis Suriya (`00_project/assets/suriya/content-pool/`)

## Execution Summary
- **Client:** Praxis Suriya (Healthcare / TCM / Acupuncture in Berlin)
- **Mode:** Existing Site / HWG Health Mode
- **Run Directory:** `00_project/assets/suriya/content-pool/`

## Pipeline Verification
1. **Client Baseline (01-client):** Verified 7 core services mapped from real clinic offerings.
2. **Competitor SERP Crawl (02-competitors):** Scraped local competitors; flagged unreadable competitor `apotheken-umschau.de` cleanly without failing.
3. **Demand Autocomplete Tree (03-demand):** 39 letter variations generated; verified volume and intent.
4. **Pool Aggregation (04-pool):** 57 total candidate items scored across 4 pillars.
5. **Deterministic Validation (scripts/validate_pool.py):**
   - Output: `57 items, 0 errors, 1 warnings`
   - Warnings handled: Flagged unreadable competitor as required by Rule R2.1.
6. **Report Rendering (05-report):** HTML report and xlsx export verified.
7. **Sitetree Architecture (05-sitetree):** Sitetree and 301 redirect map generated.
8. **Cost Cap Adherence:** Total spend tracked in `spend.jsonl` stayed strictly under the $5.00 USD cap.

## Verification Result: PASS
- All scripts executed deterministically.
- Zero manual hallucinations.
- Validated output ready for Checkpoint 1 & 2 reviews.
