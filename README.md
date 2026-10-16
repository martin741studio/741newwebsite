# 741 Studio Developer & Operations Playbook

Welcome to **741 Studio**. This repository contains the digital agency infrastructure, automated marketing and SEO pipelines, web applications, and client delivery systems for 741 Studio.

This playbook is the primary onboarding and operational guide for developers (Dinakar, Tantri, and engineering team members), AI agent operators, and agency partners. It explains how our workflows operate, where data lives across our dual-storage substrate, how decisions turn into client deliverables, and how to use the Client Dashboard and **Kundenarbeit** view.

---

## Table of Contents

1. [The 741 Operating Model](#1-the-741-operating-model)
2. [Dual-Storage Substrate: How to Read & Access Data](#2-dual-storage-substrate-how-to-read--access-data)
   - [Primary Source of Truth: Supabase](#primary-source-of-truth-supabase)
   - [Extended Operational Layer: Google Drive](#extended-operational-layer-google-drive)
   - [Resolving Client Workspaces Programmatically](#resolving-client-workspaces-programmatically)
3. [The Client Journey in 8 Phases (P0 to P7)](#3-the-client-journey-in-8-phases-p0-to-p7)
4. [Workflow Catalog: What to Use & When](#4-workflow-catalog-what-to-use--when)
   - [Complete 16-Workflow Matrix](#complete-16-workflow-matrix)
   - [CRO Track A vs. Track B Selection Guide](#cro-track-a-vs-track-b-selection-guide)
5. [The Client Dashboard & Decision Flows](#5-the-client-dashboard--decision-flows)
   - [Decision Flow: Client Approvals vs. Agency Decisions](#decision-flow-client-approvals-vs-agency-decisions)
   - [From Decision to Actionable Work Item](#from-decision-to-actionable-work-item)
6. [Kundenarbeit (Client Work View)](#6-kundenarbeit-client-work-view)
   - [Core Principle: Goal-Oriented Task Management](#core-principle-goal-oriented-task-management)
   - [The Goal-Oriented Overview: Connecting Work to Targets](#the-goal-oriented-overview-connecting-work-to-targets)
   - [Task Schema & Status Lifecycle](#task-schema--status-lifecycle)
   - [Accountable Person vs. Doer Agent](#accountable-person-vs-doer-agent)
   - [The Strict Proof Link Rule & Decision Exemption](#the-strict-proof-link-rule--decision-exemption)
   - [Step-by-Step Developer Daily Flow](#step-by-step-developer-daily-flow)
7. [Compliance & Non-Negotiable Guardrails](#7-compliance--non-negotiable-guardrails)
   - [HWG Compliance (Healthcare Practices)](#hwg-compliance-healthcare-practices)
   - [BRAO Compliance (Law Firms)](#brao-compliance-law-firms)
   - [Upload Security Guard (Local Prototypes Stay Local)](#upload-security-guard-local-prototypes-stay-local)
8. [Developer Cheat-Sheet & Daily Routines](#8-developer-cheat-sheet--daily-routines)
   - [Daily Rhythm](#daily-rhythm)
   - [Essential Commands](#essential-commands)

---

## 1. The 741 Operating Model

741 Studio operates on a **Cybernetic Loop Model**:

```
[ Real-World Agency Context / Client Need ]
                      │
                      ▼
     [ 1. Ingestion Membrane & Boundary Filter ]
     • Strict 4-parameter contract: Job, Surface, Cadence, Limits.
     • Fails fast on ambiguity before any work starts.
                      │
                      ▼
     [ 2. Transformation Core (Degrees of Freedom) ]
     • Rule R1.7: Strict separation of scripts vs creative heuristics.
     • Deterministic logic (APIs, math, DB) = isolated scripts in scripts/.
     • Strategy & copywriting = guided prompts and skill instructions.
                      │
                      ▼
     [ 3. Delivery & Expression (The Dual Substrate) ]
     • Supabase records live state, metrics, and canonical pointers.
     • Google Drive hosts collaborative Docs, Sheets, and client assets.
                      │
                      ▼
     [ 4. Sensor Loop & Discrepancy Detection (Gates) ] ◄────────┐
     • Δ = Actual Performance - Client Goal.                     │
     • Automated checkpoints (CP1, CP2) block progression.       │
                      ▲                                          │ (Calibration)
                      │ (Governance)                             │
     [ 5. Governance & Invariant Schemas ] ──────────────────────┘
     • Invariant Postgres schemas, ASD-STE100 technical standard.
```

### Key Principles for Developers
1. **AI-First Execution, Human-in-the-Loop Review:** AI agents draft copy, crawl data, and code prototypes; human engineers (Dinakar, Tantri, Martin) verify, approve, and deploy.
2. **Never Edit Live Directly:** Prototypes are built locally or in preview sandbox environments. Live client websites are only updated after explicit sign-off and backup.
3. **Decoupled Architecture:** Meta-rules (how we build workflows) are strictly separated from client-level data collection (Google Tag Manager, call tracking, Google Ads scripts).

---

## 2. Dual-Storage Substrate: How to Read & Access Data

741 Studio uses a **Dual-Storage Substrate** so that any developer, AI agent (Claude Code, Antigravity, OpenAI/ChatGPT, Gemini, Cursor), or automation tool (n8n, bash scripts) can find and manipulate data seamlessly.

```
 ┌────────────────────────────────────────────────────────┐
 │           PRIMARY SOURCE OF TRUTH: SUPABASE            │
 │  • Authority Anchor: Client IDs, Canonical NAPs        │
 │  • Discrepancy & Telemetry: _run.json, client_goals    │
 │  • Pointer Index: drive_folder_url, stammdaten_url     │
 └───────────────────────────┬────────────────────────────┘
                             │ Authoritative Pointers
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

### Primary Source of Truth: Supabase
- **Database:** Supabase project `galjmtozcgxcwtzkzbpi` (Frankfurt region).
- **Core Tables:**
  - `public.clients`: Master client registry (`id`, `name`, `status`, `client_stack`, `stammdaten_sheet_url`, `drive_folder_url`).
  - `public.client_locations`: Canonical NAP (Name, Address, Phone), categories, and services. **Once locked, this NAP is immutable.**
  - `public.client_goals`: Target KPIs per channel (monthly leads, rank targets, CPA ceilings) for automated error tracking.
  - `public.client_drive_assets`: Catalog of all files, Docs, Sheets, and PDFs with SHA256 checksums, MIME types, and categories.
  - `public.gbp_daily_actions`: Daily phone calls, direction requests, website clicks, and messages from Google Business Profiles.
  - `public.work_item`: Central task repository feeding the Kundenarbeit dashboard.

### Extended Operational Layer: Google Drive
- **Master Account:** `741studio18@gmail.com`
- **Location in Drive:** `741 Clients / <Client Name> /`
- **What Lives Here:**
  - **Google Docs:** Intake briefs (`00-brief.md`), Tone of Voice sheets, practitioner biographies, copy drafts.
  - **Google Sheets:** Client Stammdaten master sheet, content pool keyword matrices, link targets, audit matrices.
  - **PDF Deliverables:** Client proposals, signed contracts, monthly visibility reports, and CRO handoff packs.

### Resolving Client Workspaces Programmatically
To find where a client's work lives, query Supabase via SQL or REST:

```sql
SELECT 
    name,
    client_stack->>'drive_root_folder' AS drive_folder,
    client_stack->>'drive_folder_url' AS drive_url,
    stammdaten_sheet_url
FROM public.clients
WHERE name ILIKE '%suriya%';
```

Developers can also run the local synchronization utility:
```bash
# Sync local client drive assets into Supabase
node scripts/import-drive-assets.mjs --apply

# Sync Google Drive folder roots into Supabase client records
node scripts/sync-gdrive-clients.mjs --apply
```

---

## 3. The Client Journey in 8 Phases (P0 to P7)

Every client project advances strictly through eight chronological phases:

```
P0 Prospect ─► P1 Onboard ─► P2 Audit ─► P3 Un-Burning ─► P4 Build-up ─► P5 Content ─► P6 Proof ─► P7 Operations
```

| Phase | Name | Focus & Mandatory Activity | Transition Gate Rule |
|---|---|---|---|
| **P0** | **Prospect** | Initial audit, review page (`741.studio/review/<slug>`), Loom video. | Signed contract + initial payment confirmed. |
| **P1** | **Onboarding** | Client access acquisition (GBP, GSC, CMS, GA4); NAP locking. | Full access verified via `reporting/verify-access.mjs`. |
| **P2** | **Audit** | 100-point Maps-Readiness Audit; separating harms from gaps. | Audit report published; Bedrock Light calculated. |
| **P3** | **Un-Burning** | Remediating critical harms (suspensions, duplicate listings, toxic links). | **Bedrock Light GREEN.** Zero active harm items on touched channels. |
| **P4** | **Build-up** | Citations DACH, backlink outreach, CRO homepage prototypes. | Sitetree approved; prototype reviewed; citations submitted. |
| **P5** | **Content** | 4-pillar keyword pool, content writing, on-page SEO integration. | Content passes 5/5 slop gate and deployed live. |
| **P6** | **Proof** | Proof tracking, quarterly war room, rank & conversion verification. | 90-day war room completed; client targets re-calibrated. |
| **P7** | **Operations** | Daily standup, Morning Grill, Night Shift, automation maintenance. | Continuous unattended execution. |

> **Golden Rule:** **Harm repair comes before growth.** Never run citation campaigns or backlink outreach on a suspended or penalized profile.

---

## 4. Workflow Catalog: What to Use & When

### Complete 16-Workflow Matrix

| # | Workflow | Trigger Command | When to Use | Output Deliverable |
|---|---|---|---|---|
| **1** | **Prospect Review** | `/local-seo-review-page <client>` | Pitching a prospective client | Review page, Loom script |
| **2** | **Access Lockout** | `/client-access-lockout <client>` | Client revokes access or terminates | Evidence pack, formal client letter |
| **3** | **Maps Audit** | `/maps-audit <client>` | Beginning Phase 2 diagnosis | 100-point audit report, score 0–100 |
| **4** | **Un-Burning** | `/un-burning <client>` | Phase 3 harm remediation | `harm-register.json`, Bedrock Light |
| **5** | **Citations DACH** | `/citations-dach <client>` | Phase 4 local listings | 44 directory submissions, BrightLocal |
| **6** | **Maps Playbook** | `/maps-playbook <client>` | Phase 4 growth acceleration | 77-measure phased execution matrix |
| **7** | **Backlink DACH** | `/backlink-dach <client>` | Phase 4 link building | Vetted targets, outreach pipeline |
| **8** | **CRO Track A** | `/cro-homepage <client> <url>` | Standard conversion homepage build | 1440px desktop HTML prototype |
| **9** | **CRO Track B** | `/cro-track-b <client> <url>` | High-ticket / design-intense showcase | Interactive element pool, showpiece build |
| **10** | **Content Pool** | `/content-pool <client>` | Phase 5 keyword architecture | 4-pillar keyword pool, sitetree `.xlsx` |
| **11** | **Content Writing** | `/content-write <client> <page>` | Writing landing pages & money copy | Finished page copy, slop gate 5/5 |
| **12** | **Proof Tracking** | `/tracking <client>` | Phase 6 weekly & quarterly tracking | Local Falcon rollups, war-room pack |
| **13** | **Automation Build** | `/automation-build` | Creating scripts/crons/hooks | Verified code, test suite, runbook |
| **14** | **Night Shift** | `reporting/night-shift.sh` | Daily at 03:00 (unattended) | Fresh Supabase sync, daily page specs |
| **15** | **Daily Standup** | Weekdays at 08:05 (unattended) | Team morning overview | Standup board, blocker alerts |
| **16** | **Morning Grill** | Daily at 06:13 / 17:00 | Daily agency steering | Decision queue, daily brief |

### CRO Track A vs. Track B Selection Guide

When assigned a homepage conversion task, developers choose between Track A and Track B using this standard:

| Criterion | Track A (`cro-homepage`) | Track B (`cro-track-b`) |
|---|---|---|
| **Primary Use Case** | Standard conversion optimization | Design-heavy showcase & competitive pitch |
| **Target Industries** | Local healthcare, physiotherapists, trades | Boutique law firms, design agencies, SaaS |
| **Interactive Element Pool** | No (calm classical spec) | **Mandatory** (`00-element-pool/index.html`) |
| **Motion Layer** | Subtle CSS transitions | Custom SVG/Canvas/CSS + X-Ray Switch (`x`) |
| **Turnaround Time** | Fast (~3–4 hours) | Elaborate (~8–12 hours) |
| **HWG Health Clients** | **Default & Mandatory** | **Prohibited** (unless Martin overrides) |

---

## 5. The Client Dashboard & Decision Flows

The **741 Client Portal & Dashboard** (`clients.741.studio`) serves as the single glass pane through which both clients and the 741 agency team collaborate.

### Decision Flow: Client Approvals vs. Agency Decisions

```
[ AI Agent / Developer proposes change (e.g. new headline, GBP category) ]
                                 │
                                 ▼
                     Is this an internal task or 
                     does it require client sign-off?
                                ╱ ╲
                    Internal   ╱   ╲   Client-Facing
                              ▼     ▼
┌─────────────────────────────────┐   ┌─────────────────────────────────┐
│     AGENCY DECISION QUEUE       │   │    CLIENT APPROVAL WORKFLOW     │
│  • Handled in Morning Grill     │   │  • Visible in Client Portal     │
│  • Martin reviews in chat       │   │  • Client votes: Approve / Edit │
│  • Direct release via SQL       │   │  • HWG check mandatory first   │
└────────────────┬────────────────┘   └────────────────┬────────────────┘
                 │                                     │
                 └──────────────────┬──────────────────┘
                                    │ Approved
                                    ▼
┌───────────────────────────────────────────────────────────────────────┐
│                     KUNDENARBEIT TASK BOARD                           │
│  • Task created with Accountable Person, Doer, and Due Date           │
│  • Developer/Agent executes work                                      │
│  • Task completed ONLY with an attached Proof Link                    │
└───────────────────────────────────────────────────────────────────────┘
```

1. **Client Approvals (`approval_items` in portal / "Entscheidungen"):**
   - Visible to the client in their portal view.
   - Present curated cards with 2–3 variants (e.g., choice of headline angle, team photography selection, or Google review response strategy).
   - The 741 agency recommendation is highlighted as **Recommended**.
   - The client selects a variant or adds a revision request.
   - Approved items automatically emit a corresponding `work_item` row in Supabase (`source = 'approval'`).

2. **Agency Decisions (Morning Grill / "Command Center"):**
   - Internal decisions evaluated by Martin during the Morning Grill or planning sessions.
   - Evaluates performance deviations: $\Delta = \text{Actual Performance} - \text{Client Goal}$.
   - For example: if Google Ads CPL rises above the target ceiling, an agency decision creates a task: "Negative keyword purge on Search Campaign".
   - Generates actionable `work_item` rows with `source = 'grill'`, an assigned Accountable developer (Dinakar, Tantri), and a due date.

### From Decision to Actionable Work Item
Once a decision is approved:
- A task is automatically emitted or queued in `public.work_item`.
- If deterministic (e.g. data ingest or audit crawl), an automated script executes.
- If it requires design, code, copy, or CMS work, it lands on the **Kundenarbeit** task board for Dinakar or Tantri.

---

## 6. Kundenarbeit (Client Work View)

The **Kundenarbeit** view (accessible in the dashboard under the *Kundenarbeit* tab or `adminSub='work'`) is our goal-oriented execution engine. It replaces static to-do lists with verified, outcome-driven task tracking.

### Core Principle: Goal-Oriented Task Management
Every entry in Kundenarbeit answers four questions:
1. **What is the task?** (Clear technical action and Definition of Done).
2. **Who is responsible?** (Accountable human vs Doer agent/person).
3. **Where is the proof?** (Verifiable link, file, or screenshot).
4. **What is the outcome?** (Impact on the client's goal).

### The Goal-Oriented Overview: Connecting Work to Targets
In the dashboard, work is not displayed as a disconnected pile of tickets. Instead, tasks are grouped under **Client Goals** (`public.client_goal`):

- **Goal Card Example:**
  - **Goal:** Reach 35 monthly patient appointment inquiries.
  - **Metric Key:** `monthly_conversions` (Baseline: 12 · Current: 24 · Target: 35).
  - **Active Phase:** $P_4$ Build-up.
  - **Associated Tasks:**
    - `[IN PROGRESS]` Implement click-to-call mobile sticky bar on Praxis Suriya.
    - `[NEEDS CHECK]` Add chiropraktik schema markup to doctor subpage.
    - `[DONE]` Fix broken contact form webhook.

This guarantees that developers (Dinakar, Tantri) and clients always know exactly *why* a piece of work is being executed.

### Task Schema & Status Lifecycle

All work items are stored in `public.work_item`:

| Column | Type | Purpose |
|---|---|---|
| `title` | Text | Short, descriptive action title |
| `definition_of_done` | Text | Exact criteria required to finish |
| `phase_id` | Text | Phase code ($P_0$ through $P_7$) |
| `goal_id` | UUID | Foreign key to `client_goal.id` |
| `status` | Enum | `intake`, `planned`, `in_progress`, `waiting`, `needs_check`, `done`, `dropped` |
| `waiting_on` | Enum | Required if `waiting`: `client`, `martin`, `team`, `google`, `external` |
| `accountable_id` | UUID | Always a human (Dinakar, Tantri, Martin) |
| `doer_id` | UUID | Human engineer, AI agent, or script |
| `due_on` | Date | Target completion date |
| `evidence_link` | Text/FK | URL or hash verifying the completed work |
| `outcome` | Text | Human-readable result in client language |

```
[intake] ──► [planned] ──► [in_progress] ──► [needs_check] ──► [done]
                                 │                 ▲
                                 ▼                 │
                        [waiting (waiting_on)] ────┘
```

### Accountable Person vs. Doer Agent
To ensure complete reliability, every task separates accountability from execution:
- **Accountable (Always a Human):** The team member (Dinakar, Tantri, Martin) who guarantees that the work is correct, compliant, and delivered on time.
- **Doer (Human or AI):** The entity performing the keystrokes (e.g. `Agent`, `Dinakar`, `Tantri`, `Martin`, `Google`).

### The Strict Proof Link Rule & Decision Exemption
> **Rule 02-8 / 03-9:** **An AI agent is strictly forbidden from marking a task "DONE".**
> - When an AI completes an action, it sets the status to **`needs check`**.
> - Only the **Accountable Person** may change the status to **`done`**, and **ONLY** after attaching a verifiable **Proof Link**:
>   - Live URL (e.g. `https://praxis-suriya.de/team/`)
>   - Screenshot link (stored in Google Drive or preview hash)
>   - Verified report link (e.g. `https://clients.741.studio/r/...`)
>   - Git commit hash or completed `_run.json` record
>
> **Decision Task Exemption:** For internal decision tasks (e.g., agreeing on a date or choosing Option A in a strategy meeting) where no external URL exists, the task may be marked `done` by the accountable person with a clear text resolution note (e.g., `"Decided live 14.10: Proceed with Variant B"`).

### Step-by-Step Developer Daily Flow
For developers like **Dinakar** and **Tantri**, the daily routine is straightforward:

1. **Open Kundenarbeit:** Filter by your name under `accountable_id` or `doer_id`.
2. **Select Priority Task:** Pick the highest priority task in the active phase ($P_0 \to P_7$). Move status to `in_progress`.
3. **Inspect the Dual Substrate:**
   - Query Supabase for canonical NAP, tracking numbers, or target IDs.
   - Open Google Drive (`741 Clients / <Client Name> /`) for copy briefs, tone sheets, or image assets.
4. **Build & Verify Locally:**
   - Write code or build prototypes locally (`04_site/` or `00_project/assets/`).
   - Run verification scripts (`verify.py`).
   - Follow HWG / BRAO compliance rules.
5. **Attach Proof & Complete:**
   - If using an AI agent, let the agent set status to `needs_check`.
   - Inspect the work yourself, add the `evidence_link` (Proof Link), and mark status as `done`.
   - Document the before/after impact under `outcome`.

---

## 7. Compliance & Non-Negotiable Guardrails

### HWG Compliance (Healthcare Practices)
For doctors, alternative practitioners (*Heilpraktiker*), and physiotherapists under the German Healthcare Advertising Act (*Heilmittelwerbegesetz*):
- **Zero Healing Promises:** Never use words like "heilen", "Garantie", "schmerzfrei in X Tagen", or "dauerhafte Beseitigung".
- **Zero Fear Framing:** Never frame symptoms as life-threatening or induce anxiety.
- **No Before/After Photos:** Strict prohibition on medical before/after imagery.
- **Calm Editorial Aesthetic:** Use quiet, trustworthy colors (Sage, Charcoal, Cream) and restrained typography.

### BRAO Compliance (Law Firms)
For legal clients under the Federal Lawyers' Act (*Bundesrechtsanwaltsordnung*):
- **Formal Address:** Always use the formal German address (**Sie** / **Ihnen**).
- **No Unproven Specialist Titles:** Never call a lawyer "Fachanwalt für X" unless certified in verified records.
- **Zero Superlatives:** Avoid "beste Kanzlei", "führender Anwalt", or unverified success rates.
- **No Cliché Imagery:** Strictly forbid scales of justice, gavels, handcuffs, or courtroom drama imagery.

### Upload Security Guard (Local Prototypes Stay Local)
- **Hard Rule:** CRO prototypes and test sites stay strictly on local machines.
- **Enforcement Hook:** `scripts/guard_upload.py` intercepts any shell command attempting to run `rsync`, `scp`, `curl -T`, or `sftp` to remote servers without explicit written confirmation from Martin.

---

## 8. Developer Cheat-Sheet & Daily Routines

### Daily Rhythm
- **03:00 (Night Shift):** Headless background jobs sync fresh GSC and Google Ads data into Supabase.
- **06:13 (Morning Grill):** Martin reviews daily brief, error signals ($\Delta$), and makes strategic decisions.
- **08:05 (Daily Standup):** Automated standup report generates in `reporting/standup/` highlighting blockers and open tasks.
- **Workday Execution:** Dinakar, Tantri, and developers pick up tasks from the **Kundenarbeit** board in priority order.

### Essential Commands

```bash
# Check build status of any workflow
python3 .claude/skills/workflow-create/scripts/check_build.py status <workflow_id>

# Run verification on a standard CRO Track A prototype
python3 .claude/skills/cro-homepage/scripts/verify.py 00_project/assets/<client>/cro

# Run verification on an advanced CRO Track B prototype
python3 .claude/skills/cro-track-b/scripts/verify.py 00_project/assets/<client>/cro-b

# Catalog local client drive files into Supabase
node scripts/import-drive-assets.mjs --apply

# Sync Google Drive folder links to Supabase client profiles
node scripts/sync-gdrive-clients.mjs --apply

# Sync Workflow Overview Excel
python3 00_project/workflow-registry/workflow_registry.py sync --quiet
```

---

*Authored by 741 Studio Architecture & Martin Drendel · Version 2.1 · October 2026*
