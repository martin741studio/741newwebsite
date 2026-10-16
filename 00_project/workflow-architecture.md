# 741 Workflow Architecture Map

Version 1.0 · 2026-10-16 · Owner: Martin · Approved Cybernetic Architecture.
Language: STE. Registry ids and file paths are exact. Sources: `00_project/workflow-registry/registry.json`, workflow specs, Supabase marketing schema, `check_build.py`.

Purpose: the definitive master specification for all 741 workflows, mapping how each workflow operates within the client journey ($P_0 \to P_7$), its cybernetic regulation loop, its input membrane, telemetry outputs, and phase gate enforcement.

---

## 0. The Universal Cybernetic Meta-Pattern

Every 741 workflow operates as a **recursive regulation loop** across five structural checkpoints:

```
[ Context / Client Real-World Environment ]
                 │ (Search, Ads, Ranking, Outreach Signals)
                 ▼
    [ 1. Sensory / Ingestion Membrane ]
    • Filter: Rejects unstructured entropy, unverified inputs, and prompt hallucinations.
    • Scope: Core 5 quantitative channels in Supabase (GSC, Local Falcon, Google Ads, BrightLocal, DataForSEO).
                 │ (Normalized State)
                 ▼
    [ 2. Processing / Transformation Core ]
    • Degrees of Freedom (R1.7): Fragile/math steps = deterministic scripts (.mjs/.py).
    • Heuristics: Editorial tone, strategy, and CRO wireframes = guided LLM prompts.
                 │ (Actionable Deliverable)
                 ▼
    [ 3. Expression / Output ]
    • Client artifacts: review pages, Drive folders (SHA-256 hashed), portal tabs.
                 │
    [ 4. Feedback / Telemetry Sensor ] ◄─────────────────────────┐
    • Error Signal: Δ = Actual Performance - Client Goal.       │
    • Status: Universal _run.json written at every checkpoint.  │
                 ▲                                               │ (Calibration)
                 │ (Governance)                                  │
    [ 5. Governance / Schema (Meta-Controller) ] ────────────────┘
    • Invariant Postgres schemas, CLAUDE.md, ASD-STE100 technical standard.
    • Gate scripts: check_build.py (builds) and check_phase.py (client stages).
```

### The 7 Implementation Parameters
1. **Membrane Contract:** Explicit input schema. Only validated data enters. Unstructured noise fails fast.
2. **State vs. Ephemeral Flow (Dual-Storage Substrate):** **Supabase (`741-portal`) is the primary Source of Truth** for structured records, canonical NAPs, metric rollups, and system pointers. **Google Drive (`741studio18@gmail.com` under `741 Clients/<Client Name>/`) is the extended secondary operational database** for working Google Docs, Sheets, PDF proposals, and asset handoffs. Chats and scratchpads are strictly transient.
3. **Idempotence:** Every script run on the same client and date updates cleanly without duplicate rows.
4. **Single Source of Truth:** `registry.json` for workflow states; Supabase for all canonical client records, performance targets, and pointers to Google Drive folders/sheets; `_derived/rules.md` for prompt guidelines.
5. **Definition of Done:** Mandatory checkpoint gates with evidence files before downstream consumption.
6. **Error Telemetry:** Universal `_run.json` emitted at every stage; Morning Grill surfaces lagging indicators.
7. **Coupling & Multi-Model Portability:** High modularity. The data layer is decoupled from any single compute agent. Any LLM provider or automation platform (Claude Code, Antigravity IDE, ChatGPT/OpenAI, Gemini, Cursor, n8n) queries Supabase (`public.clients` and `public.client_drive_assets`) to instantly discover the client's working Drive folder, master docs, and sheets.

### Strict Decoupling: Meta-Architecture vs. Client-Level Operations
- **The Meta-Architecture (Governing System):** How 741 Studio creates, validates, gates, installs, and recalibrates workflows (`workflow-creation-workflow.md`, `check_build.py`, 3-gate pipeline). It sets the immutable cybernetic structure.
- **Client Data Gathering (Downstream Applications):** GTM containers, call tracking, GBP conversion actions, Google Ads reporting scripts, and Supabase client performance tables belong strictly inside execution workflows (specifically $P_2$ Audit and $P_6$ Tracking). They are client-level data inputs and must never dilute or divert the meta-system.

---

## 1. The Client Journey in 8 Phases

```
P0 Prospect ─► P1 Onboarding ─► P2 Audit ─► P3 Un-Burning ─► P4 Build-up ─► P5 Content ─► P6 Proof + Quarter
                                                               (citations,      (pool,         (tracking,
                                                                phone, links,    writing)       war room)
                                                                CRO)
Cross-cutting:  P7 Operations = morning grill, evening log, night shift, daily standup, automation build, lockout (incident)
```

### Rules of the Sequence
- The audit is the diagnosis. Un-Burning repairs harm. The maps playbook adds growth. **Harm repairs come before growth measures** (`maps-playbook-workflow.md` §2).
- **Channel-Decoupled Gate:** Only growth measures that directly touch an active harm item are blocked (e.g. if a client has a GBP address suspension, halt citations and GBP edits, but allow content pool keyword research and sitetree drafting to proceed in parallel).
- The content pool determines target topics. Content writing creates the text. The CRO workflow builds the page.
- Tracking proves results and feeds the quarterly 90-day war room.
- Data channels: We standardize on **GSC**, **Local Falcon**, **Google Ads**, **BrightLocal**, and **DataForSEO**. Ahrefs is deprecated; Meta Ads is currently paused.

---

## 2. Workflow Master Table

Status words: **installed** = skill active in `~/.claude/skills/` or `.claude/skills/`. **draft** = spec and draft ready. **spec** = spec only. **live module** = runs in portal/CLI, no skill wrapper needed.

| # | Workflow | Phase | Registry id | Trigger | Inputs (Membrane) | Outputs (Deliverable) | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | Prospect review page (v2.1) | P0 | `prospect` | "Review page for <name>", URL | Name, website, Maps link | `741.studio/review/<slug>/`, Loom script, WhatsApp ask | Agent + Martin | installed (`.claude/skills/local-seo-review-page`) |
| 2 | Client access lockout | P1 / incident | `lockout` | `/client-access-lockout <client>` | Revoked access, contract, run history | Client letter (PDF), evidence pack, Drive filing | Agent + Martin | installed (96.3 %) |
| 3 | Maps audit (Maps-Readiness) | P2 | `audit` | "Starte den Maps-Audit für <client>" | GBP, site, 5 keywords, 5 competitors | Audit report, score 0–100, traffic lights, `_run.json` | Agent + Martin (Go-C) | installed (`.claude/skills/maps-audit`) |
| 4 | Un-Burning | P3 | `unburning` | "Starte Un-Burning für <client>" | Audit findings, harm checks | `harm-register.json`, bedrock light A–E, client report | Agent + Team | installed (`.claude/skills/un-burning`) |
| 5 | Citations DACH | P4 | `citations` | "Prüfe Citations für <client>" | Canonical NAP (`client_locations`), directories | `client_citations` status, BrightLocal order, `_run.json` | Agent + Martin | installed (`.claude/skills/citations-dach`) |
| 6 | Maps playbook ("Ring Phone") | P4 | `phone` | "Maps-Playbook für <client>" | Audit fields, harm register, pool items | 77-measure matrix, task list (`d1-30`, `m2+`, `later`) | Agent + Team | installed (`.claude/skills/maps-playbook`) |
| 7 | Backlink DACH | P4 | `backlink` | `/backlink-dach <client>, <city>` | Competitors, DataForSEO backlink API, budget | Target sheet with approval boxes; outreach batch; `_run.json` | Agent + Martin + Gayo | installed (.claude/skills/backlink-dach) |
| 8 | CRO Homepage Track A | P4 | `cro` | `/cro-homepage <name>, <URL>` | Site scrape, content pool, GBP | Desktop prototype, handoff pack, Drive folder | Agent + Dinakar | installed (`.claude/skills/cro-homepage/`) |
| 9 | CRO Track B (Design-Intense) | P4 / P0 | `cro_b` | "Track B für <client>" | B0 questionnaire, element pool | Showpiece interactive prototype | Agent + Martin | installed (`.claude/skills/cro-track-b`) |
| 10 | Content pool | P5 | `pool` | "Content-Pool für <client>" | Competitors, DataForSEO demand, GSC queries | Ranked keyword pool, sitetree, xlsx export | Agent + Martin | installed (`.claude/skills/content-pool`) |
| 11 | Content writing | P5 | `copy` | `/content-write <client> <page>` | Pool items, tone guide, brief | Page text, portal node entry, slop gate 5/5 | Agent + Dinakar | installed |
| 12 | Proof tracking + quarter | P6 | `tracking` | Weekly trigger / Quarter end | Local Falcon grid, GSC weekly rollups, reviews | Portal "Ergebnisse" tab, early warning flags, war-room pack | Agent + Martin | installed (`.claude/skills/tracking/`) |
| 13 | Automation build | P7 | `automation` | `/automation-build` | Spec, test plan, credentials | Verified script/cron, runbook, test logs | Agent + Martin | installed (`~/.claude/skills/automation-build/`) |
| 14 | Night shift | P7 | none | `reporting/night-shift.sh` (03:00) | Open tasks, GSC/Google Ads APIs | Fresh Supabase tables, daily page specs | Agent (unattended) | installed (`.claude/skills/night-shift`) |
| 15 | Daily client standup | P7 | none | LaunchAgent weekdays 08:05 | Supabase standup function | Admin standup board | Agent (unattended) | live |
| 16 | Morning grill + evening log | P7 | `morning` | Morning: "Grill me" / Evening: "Log" | Master map, registry, Supabase goals, git | Daily brief, decision queue, error signals | Agent + Martin | live procedure |

---

## 3. Strict Phase Gates & Verification Criteria

Clients advance to the next phase only when the gate conditions evaluate to true:

| Transition | Strict Gate Requirement | Verification Method | Owner |
|---|---|---|---|
| **P0 → P1** | Signed offer received, first payment confirmed, client created in Supabase `clients`. | Financial/Admin confirmation | Martin |
| **P1 → P2** | Full access confirmed (GBP manager, GSC, site CMS); Canonical NAP locked in `client_locations`. | `reporting/verify-access.mjs` | Agent + Martin |
| **P2 → P3** | Maps audit complete; score 0–100 calculated; distinct Harm vs. Gap separation filed. | `00_project/assets/<client>/audit/report.md` | Agent |
| **P3 → P4** | **Channel Bedrock Light GREEN.** All red items in `harm-register.json` cleared for channels touched by growth (unaffected channels may advance). | `scripts/check_phase.py <client> p3-to-p4` | Programmatic Gate |
| **P4 → P5** | Sitetree approved by Martin; Citations Group A submitted; prototype reviewed. | Checkpoint approval log | Martin |
| **P5 → P6** | Target pages live on client domain; baseline search metrics logged in Supabase. | URL 200 HTTP check + DB scan | Agent |
| **P6 → Next** | 90-day war room completed; client goals vs actual performance audited; new targets set. | War room executive summary | Martin + Client |

---

## 4. Telemetry Standard: Universal `_run.json`

Every workflow execution must emit a standardized telemetry record at each checkpoint and at completion:

```json
{
  "client_id": "balihealing",
  "workflow_id": "citations",
  "checkpoint": "cp2",
  "status": "passed",
  "mode": "production",
  "metrics": {
    "units_processed": 44,
    "units_live": 38,
    "discrepancy_delta": 0
  },
  "evidence_file": "00_project/assets/balihealing/citations/2026-10-16/status.md",
  "result_summary": "All 44 directories audited. 38 verified live, 6 awaiting indexing.",
  "error_signal": null,
  "updated_at": "2026-10-16T07:35:00Z"
}
```

* **Storage Paths:**
  - **Client Workflows ($P_0 \to P_6$):** `00_project/assets/<client>/<workflow_id>/<YYYY-MM-DD>/_run.json`
  - **Internal / Operations Workflows ($P_7$):** `00_project/workflow-registry/runs/<workflow_id>/<YYYY-MM-DD>/_run.json`
* **Auto-Sync:** The repository Stop hook executes `workflow_registry.py sync`, updating `~/Desktop/Workflow-Uebersicht.xlsx` automatically without manual data entry.

---

## 5. Invariant Schema: `public.client_goals` (The Error Sensor)

To close the cybernetic loop, Supabase maintains client performance targets so the Morning Grill calculates the error signal automatically:

$$\Delta = \text{Actual Performance} - \text{Client Goal}$$

```sql
CREATE TABLE IF NOT EXISTS public.client_goals (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES public.clients(id) ON DELETE CASCADE,
    metric_name TEXT NOT NULL, -- e.g. 'cpa_ceiling', 'target_monthly_leads', 'target_avg_position'
    channel TEXT NOT NULL,     -- e.g. 'google_ads', 'gsc_search', 'local_falcon'
    target_value NUMERIC NOT NULL,
    warning_threshold NUMERIC NOT NULL, -- Delta triggering an alert
    period TEXT NOT NULL DEFAULT 'monthly', -- 'weekly' or 'monthly'
    is_active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE(client_id, metric_name, channel, period)
);
```

---

## 6. Gaps Resolved & System Maintenance

### Gaps Resolved (2026-10-16):
1. **Telemetry Blind Spots (Gap 2):** Citations and Backlinks now possess strict `_run.json` requirements mapped to their asset folders.
2. **Data Scope Clarified (Gap 1 & 6):** Toolstack standardized on Core 5 (GSC, Local Falcon, Google Ads, BrightLocal, DataForSEO). Ahrefs and Meta Ads removed from active pipeline.
3. **Goal Tracking Defined (Gap 6):** `public.client_goals` established as the invariant schema for discrepancy calculations.
4. **Phase Progression Gated:** Programmatic gate rules defined to prevent premature execution of growth measures on damaged clients.

---

## 7. The Dual-Storage Substrate: Supabase & Google Drive

To support multi-model, multi-agent, and human-in-the-loop workflows, 741 Studio operates a **Dual-Storage Substrate**:

```
 ┌────────────────────────────────────────────────────────┐
 │           PRIMARY SOURCE OF TRUTH: SUPABASE            │
 │  • Structured Entities (clients, client_locations)     │
 │  • Performance Telemetry (_run.json, client_goals)     │
 │  • System Pointers (drive_folder_url, stammdaten_url)  │
 └───────────────────────────┬────────────────────────────┘
                             │ Authority Pointers
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │   EXTENDED SECONDARY DATABASE: GOOGLE DRIVE ("741")    │
 │  • Account: 741studio18@gmail.com                      │
 │  • Root Directory: "741 Clients / <Client Name> /"     │
 │  • Google Docs: Briefings, Tone Sheets, Copy Drafts    │
 │  • Google Sheets: Stammdaten Master, Keyword Pools     │
 │  • PDF Deliverables: Proposals, Audits, Contracts      │
 └────────────────────────────────────────────────────────┘
```

### 1. Architectural Roles
1. **Supabase (`galjmtozcgxcwtzkzbpi`):** The authoritative anchor. Stores immutable client IDs, relational mappings, canonical NAPs, metric rollups, and the primary URL/ID pointers to external Google Drive assets.
2. **Google Drive:** The collaborative operational working layer. Google Docs and Sheets allow real-time human editing, client reviews, and direct file manipulation.

### 2. Multi-Model & Cross-Platform Discovery
Because Supabase exposes standardized REST and SQL interfaces, any AI provider or compute agent (Claude Code, Antigravity IDE, OpenAI/ChatGPT, Gemini, Cursor, n8n automations, or background bash workers) can immediately locate a client's working assets:

```sql
-- Retrieve the operational workspace for any client
SELECT 
    c.name,
    c.client_stack->>'drive_root_folder' AS gdrive_folder_name,
    c.client_stack->>'drive_folder_url' AS gdrive_url,
    c.stammdaten_sheet_url,
    COUNT(a.id) AS total_cataloged_assets
FROM public.clients c
LEFT JOIN public.client_drive_assets a ON c.id = a.client_id
WHERE c.name ILIKE '%stuerzl%'
GROUP BY c.name, c.client_stack, c.stammdaten_sheet_url;
```

### 3. Cataloging & Checksums (`public.client_drive_assets`)
- **Asset Indexing:** Run `node scripts/import-drive-assets.mjs --apply` to crawl client `_drive/` folders and catalog files with SHA256 checksums, MIME types, and categories (`sheet`, `doc`, `cro_asset`, `offer_pdf`, `content_export`).
- **Root Sync:** Run `node scripts/sync-gdrive-clients.mjs --apply` to ensure every client's Google Drive root folder pointer is synchronized between Google Drive and Supabase.
- **Migration:** Staged in `scripts/migrations/003_gdrive_secondary_database_and_client_links.sql`.

