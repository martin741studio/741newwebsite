---
name: maps-audit
description: Runs the 100-point Google Maps readiness audit and harm diagnosis for local businesses. Reads client GBP profile data, website, citations, and local competitor assets, runs deterministic scoring scripts, and generates an internal audit report and harm separation. Use when Martin says "starte den Maps-Audit", "/maps-audit", "Maps-Readiness prüfen", or "audit client X". Do NOT use for single ranking scans (use ranking-tracking), single-page content optimization (use seo-page-optimizer), or ongoing weekly proof tracking (use tracking).
disable-model-invocation: true
context: fork
allowed-tools: Read, Write, Edit, Bash(python3:*)
---

# Maps Audit Workflow (`audit`)

Spec: `00_project/audit-workflow-spec.md` · Design: `00_project/audit-workflow/design-note.md` · Language: STE.
Registry ID: `audit` · Phase: P2 (Audit & Diagnosis)

## Critical Rules
1. **Existing Data First:** Always use local assets in `00_project/assets/<client>/` before requesting any external API calls.
2. **Zero Paid Spend Without Go-A:** Never execute paid DataForSEO or Local Falcon credit scans without Martin's explicit Go-A.
3. **Harm vs. Gap Separation:** Every red finding must be categorized into either *Harm* (active penalty risk / toxic links / NAP conflict) or *Gap* (missing optimization). Harm must be cleared in P3 before growth in P4.
4. **Deterministic Math:** Scores are computed strictly by `scripts/score.py` reading `references/catalog.json`. Never calculate scores inside the LLM prompt.
5. **Universal Telemetry:** Every run must emit `00_project/assets/<client>/audit/<YYYY-MM-DD>/_run.json`.

---

## Execution Checklist

Copy this checklist into your response and tick each step:

### Phase 1: Ingestion & Boundary Filter (Intake)
- [ ] **1.1 Intake Validation:** Verify client slug, canonical domain, GBP place ID, and 5 target keywords from `00_project/assets/<client>/`.
- [ ] **1.2 Run Directory:** Initialize run folder at `00_project/assets/<client>/audit/<YYYY-MM-DD>/`.
- [ ] **1.3 Strategy Mode:** Note strategy mode (`--strategy maps|paid|balanced`). Default is `maps`.

### Phase 2: Transformation Core (Data Assembly & Scoring)
- [ ] **2.1 Local Asset Assembly:** Collect existing data:
  - Local Falcon geo-grid scans from `00_project/assets/<client>/` or Supabase `geo_grid_scans`.
  - Citation audits from Supabase `brightlocal_audits`.
  - GSC daily baseline from Supabase `gsc_daily_performance`.
  - On-page technical checks: run `python3 scripts/site_check.py --url <client_url> --out <run_dir>/site.json`.
- [ ] **2.2 Checkpoint Go-A:** If paid scans are needed, show plan and cost estimate to Martin. *Wait for Go-A.*
- [ ] **2.3 Deterministic Scoring:** Run score calculator:
  ```bash
  python3 scripts/score.py --catalog references/catalog.json --input <run_dir>/data.json --out <run_dir>/score.json
  ```
- [ ] **2.4 Driver & Harm Analysis:** Run driver analysis:
  ```bash
  python3 scripts/analyze_drivers.py --score <run_dir>/score.json --out <run_dir>/drivers.json
  ```
  Extract all red items to `<run_dir>/harm-register.json`.

### Phase 3: Delivery & Expression (Report Generation)
- [ ] **3.1 Build Report:** Generate internal and client-ready audit reports:
  ```bash
  python3 scripts/build_report.py --run <run_dir>
  ```
  Produces `<run_dir>/audit-report.md` and `<run_dir>/audit-report.html`.
- [ ] **3.2 Client Safety Guard:** Run client text sanitization check:
  ```bash
  python3 scripts/check_client.py --file <run_dir>/audit-report.html
  ```
  Ensures no internal tool names, API costs, or contractor names appear.
- [ ] **3.3 Checkpoint Go-B:** Present Martin with overall score (0–100), top 3 harm drivers, and audit report link. *Wait for Go-B approval.*

### Phase 4: Feedback & Telemetry
- [ ] **4.1 Telemetry Emission:** Write `_run.json` to `<run_dir>/_run.json`:
  ```json
  {
    "client_id": "<client_slug>",
    "workflow_id": "audit",
    "checkpoint": "cp2",
    "status": "passed",
    "score": 78,
    "harm_items_count": 2,
    "evidence_file": "<run_dir>/audit-report.md",
    "updated_at": "ISO-TIMESTAMP"
  }
  ```
- [ ] **4.2 Stop Hook Sync:** Confirm registry status syncs cleanly via `workflow_registry.py sync`.

---

## Verification Step

Before reporting completion, run the audit validator:
```bash
python3 scripts/validate_run.py --run <run_dir>
```
Fix any reported schema errors until it outputs `VALIDATION PASSED`.
