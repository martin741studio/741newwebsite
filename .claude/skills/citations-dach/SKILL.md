---
name: citations-dach
description: Audits and synchronizes local business directory citations across the 44 major DACH directories (Gelbe Seiten, DasÖrtliche, 11880, Apple Maps, Bing, Jameda, etc.). Reads canonical NAP from client_locations, checks live listings in client_citations, generates submission runbooks, imports BrightLocal orders, and writes _run.json telemetry. Use when Martin says "prüfe die Citations", "/citations-dach", "Verzeichnis-Abgleich", or "Citations für <Kunde>". Do NOT use for authority editorial backlinks from press or blogs (use backlink-dach), on-page content (use content-write), or Google Ads management.
disable-model-invocation: true
context: fork
allowed-tools: Read, Write, Edit, Bash(node:*)
---

# Citations DACH Workflow (`citations`)

Spec: `00_project/workflow-architecture.md` §4.1 · Registry ID: `citations` · Phase: P4 (Build-up)

## Critical Rules
1. **Canonical NAP Invariant:** Never modify business name, address, or primary telephone number. Use the locked values in `public.client_locations`.
2. **Zero Paid Spend Without Go:** Never purchase external BrightLocal citation packages without Martin's explicit Go-B approval.
3. **Primary Phone Consistency:** Never replace the main telephone number with call-tracking numbers on directory submissions.
4. **Universal Telemetry:** Every run must emit `00_project/assets/<client>/citations/<YYYY-MM-DD>/_run.json`.

---

## Execution Checklist

Copy this checklist into your response and tick each step:

### Phase 1: Ingestion & NAP Lock
- [ ] **1.1 Canonical NAP Verification:** Read `public.client_locations` in Supabase for `<client>`:
  - Verify exact business name, street address, postal code, city, primary telephone, and website URL.
- [ ] **1.2 Run Directory:** Initialize run folder at `00_project/assets/<client>/citations/<YYYY-MM-DD>/`.

### Phase 2: Transformation & Audit
- [ ] **2.1 Live Directory Audit:** Run the automated citation monitor:
  ```bash
  node .claude/skills/citations-dach/scripts/citation-monitor.mjs --client <client_slug>
  ```
  Audits live status, HTTP response, and NAP agreement across the 44 directories.
- [ ] **2.2 Status Summary:** Output status counts to `<run_dir>/status.md`:
  - `live`: Active listings with verified correct NAP.
  - `submitted`: In progress / pending verification email.
  - `planned`: Awaiting submission.

### Phase 3: Submission Preparation & Order
- [ ] **3.1 Group A (741 Priority):** Generate direct submission data for core platforms (Google, Apple Maps, Bing, 11880, Das Örtliche):
  ```bash
  node .claude/skills/citations-dach/scripts/submission-runbook.mjs --client <client_slug> --group A
  ```
- [ ] **3.2 BrightLocal Order Draft (Check Go-B):** If ordering directory submissions, prepare CSV batch and present cost to Martin. *Wait for Go-B approval.*
- [ ] **3.3 BrightLocal Sync:** Once processed, import order results into Supabase:
  ```bash
  node .claude/skills/citations-dach/scripts/import-brightlocal.mjs --client <client_slug> --file <csv_path>
  ```

### Phase 4: Expression & Telemetry
- [ ] **4.1 Telemetry Emission:** Write `_run.json` to `<run_dir>/_run.json`:
  ```json
  {
    "client_id": "<client_slug>",
    "workflow_id": "citations",
    "checkpoint": "cp2",
    "status": "passed",
    "metrics": {
      "total_directories": 44,
      "live_count": 38,
      "submitted_count": 4,
      "planned_count": 2
    },
    "evidence_file": "<run_dir>/status.md",
    "result": "38/44 directories live and verified.",
    "error_signal": null,
    "updated_at": "ISO-TIMESTAMP"
  }
  ```
- [ ] **4.2 Registry Auto-Sync:** Confirm Stop hook executes `workflow_registry.py sync` to update `~/Desktop/Workflow-Uebersicht.xlsx`.

---

## Verification Step

Before closing, verify that:
1. `<run_dir>/status.md` exists and contains live/submitted/planned counts.
2. `<run_dir>/_run.json` exists and validates cleanly against JSON schema.
3. Database table `public.client_citations` reflects the latest crawl timestamps.
