# Step 0.0 Inputs Grill Record: Client Roadmap & Goal Engine (`roadmap`)

Date: 2026-10-16
Owner: Martin Drendel
Workflow ID: `roadmap`
Status: Confirmed via Interactive Decision Cards

---

## 1. The Job (Objective & Scope)
- **What enters:**
  - Client technical and strategic audits (PageSpeed, TTFB, media analysis, SEO audits).
  - Competitor scrapes and verified market benchmarks (best-practice baselines for the specific niche).
  - Existing client goals, contracts, and status quo from Supabase (`public.clients`, `public.client_goals`, `work_goals`) and Google Drive master sheets.
- **What transforms:**
  1. Executes a reality check: Discrepancy analysis between client baseline and top competitor benchmarks.
  2. Synthesizes a structured, sequential client roadmap: 1 North Star Goal + 3–4 achievable Milestones ($M_1 \to M_4$) with explicit task breakdowns.
  3. Formats and persists the roadmap as dual-storage data: Primary record in Supabase (`client_goals`), local operational mirror in `00_project/assets/<client>/roadmap.json`.
  4. Generates an Agent Pre-Flight Briefing block that informs any compute agent (Antigravity IDE, Claude Code) of the active milestone, rules, and blockers before starting work.
- **Who uses output:**
  - Active Chat-Agents in Antigravity IDE and Claude Code (ensures agents never work without seeing the big picture and intermediate steps).
  - Martin Drendel (for strategic milestone sign-offs and client alignment).
  - The Client (transparent progress reports without technical jargon).

## 2. Runtime Surface
- **Primary surface:** Multi-Surface Agent Skill in Antigravity IDE and Claude Code (`/client-roadmap <client>` or conversational trigger).
- **Data substrate:** Hybrid Dual-Storage Substrate:
  - Supabase (`public.client_goals`, `public.clients`) as the relational, queryable Source of Truth.
  - Local repository mirror in `00_project/assets/<client>/roadmap.json` for zero-latency agent ingestion and Git history tracking.
- **Reporting surface:** Automated synchronization into Morning Grill (`morning-grill-goals.json`) and Standup board.

## 3. Cadence / Frequency
- **Turnus:** Hybrid Event & Lifecycle Trigger:
  1. *Creation:* Initial creation during Onboarding ($P_1$) or Deep Audit ($P_2$).
  2. *Pre-Flight:* Executed at the beginning of every agent session touching client assets to orient the agent on active milestone priorities.
  3. *Checkpoint Transition:* Triggered upon completing a milestone task to update telemetry, record `_run.json`, and unlock downstream steps.
  4. *Reconciliation:* Weekly review during Morning Grill ($P_7$).

## 4. Hard Limits (Failure Boundaries)
- **Zero Unapproved Strategic Drift:** No agent may unilaterally alter core client goals, target KPIs, or contractual commitments without Martin's explicit written Go via Decision Card.
- **Zero Hallucinated Numbers / Factual Anchoring:** Every baseline, target, and benchmark metric must cite an immutable source (audit file path, GSC API, Local Falcon scan, Lighthouse report). No placeholder estimations.
- **Zero Uncontrolled API Credit Burn:** External scrapers and paid audit APIs (DataForSEO, BrightLocal) must obey hard caps and require explicit operator confirmation before bulk runs.
- **Strict Read-Only Isolation During Roadmap Generation:** The roadmap workflow is diagnostic and planning only. It is strictly forbidden from directly editing live client CMS instances, modifying production DNS, or touching live ads. Execution is handed off to dedicated execution workflows ($P_3, P_4, P_5$).
