# 741 Data Brain — Master Spec & Build Prompt

> Goal: one central "brain" that every 741 data source feeds into, so the systems
> stop being isolated channels and can be queried, correlated, and acted on together
> — the way a real data platform (warehouse + semantic layer + agent) works.

---

## 1. The problem (why we're doing this)

Right now 741 data lives in ~15 disconnected channels. Each was built for one job and
can't see the others. You can't ask a single question like *"which prospects from the
LinkedIn pipeline are also in a live Local Falcon scan, have a GA4 property, and haven't
been invoiced?"* — because no system holds all of that at once.

A "brain" fixes this: a **single source of truth** (central warehouse) that all sources
sync into, a **semantic layer** that gives everything shared meaning (a client is the
same client across Supabase, GA4, Drive and Local Falcon), and an **AI/agent query
layer** on top that can read across all of it and (optionally) act.

---

## 2. Inventory — every data source that must plug in

### Owned databases (Supabase — Frankfurt)
- **741-leads** — advertorial_leads, giveaway_entries (advertorial + Google-Ads + giveaway funnels)
- **741-portal** — client portal (clients.741.studio), provision_client flow, weekly-mail cron
- **phone_leads** — AI inbound voice agent (Twilio→ElevenLabs→n8n)
- Edge functions: notify-giveaway, Resend notify pipeline

### Marketing / rank / SEO data
- **Local Falcon** — ~49 locations, rank grids, review analysis, Falcon Guard, trend reports
- **GA4** — 36 client properties (service-account read via reporting-bot)
- **Google Search Console** — 741.studio
- **Google Ads** — DE + Bali/EN campaigns, conversions, health-policy keyword rules
- **Meta Ads** — DE campaigns (attribution gap: conversions happen off-platform)

### Ops / business
- **Google Drive** — invoicing "2026" folder, master ledger sheet, offer PDFs (2 entities: US LLC / PT Amana)
- **Notion** — weekly/daily check-ins, business metrics
- **LinkedIn CRM** — pipeline (NAD/overdue/replied states)
- **Client sites** — 741.studio (Vite/Handlebars), WordPress clients (e.g. Johni Jaya Motor)

### Automation / delivery glue
- **n8n** — orchestration hub (already wired to phone agent, story automation)
- **Resend** — transactional email
- **Telegram** — alert/delivery channel (stories, trading)
- **Social visuals + Story automation** — 07_social, headless-Chrome PNG pipeline

### Separate domain (keep isolated, don't merge)
- **TradingView / trading** — ICT workflow, TV bridge, alerts. Different concern; do NOT
  pull into the business brain unless explicitly asked.

---

## 3. Target architecture (recommended)

```
   SOURCES                    PIPES                 BRAIN                 SURFACES
 ┌───────────┐          ┌──────────────┐     ┌────────────────┐    ┌──────────────┐
 │ Supabase  │          │              │     │  CENTRAL WH     │    │ AI agent /   │
 │ Local     │          │  n8n +       │     │  (Supabase PG   │    │ chat ("ask   │
 │  Falcon   │──ingest──▶│  Airbyte/    │────▶│   or BigQuery)  │───▶│  the brain") │
 │ GA4 / GSC │          │  scheduled   │     │                 │    │              │
 │ Ads/Meta  │          │  jobs        │     │  + semantic     │    │ Dashboards   │
 │ Drive/    │          │              │     │    layer        │    │ (Metabase)   │
 │  Notion   │          │              │     │  (unified IDs,  │    │              │
 │ LinkedIn  │          │              │     │   dbt models)   │    │ Automations  │
 └───────────┘          └──────────────┘     └────────────────┘    └──────────────┘
```

**Recommended core:** central **Supabase Postgres** (you already run it, Frankfurt, RLS,
edge functions) as the warehouse; **n8n** as the primary pipe (you already run it);
**dbt or plain SQL views** for the semantic layer; **an entity resolution table** (the
"client registry") as the keystone; a **RAG + tool-calling agent** as the query surface;
**Metabase** (or Supabase's own SQL) for dashboards.

> Alternative if data volume/analytics grows big: BigQuery as the warehouse (you already
> have GA4 + service-account access, and GA4→BigQuery export is native). Postgres-first is
> simpler to start; note BigQuery as the escape hatch.

### The keystone: the Client Registry
One table that gives every entity a single canonical `client_id`, with a mapping to its
IDs in each system:

| canonical_client_id | name | supabase_lead_id | ga4_property_id | falcon_location_id | gbp_id | drive_folder | notion_page | linkedin_urn | wp_site | entity (LLC/PT) |
|---|---|---|---|---|---|---|---|---|---|---|

Everything else joins through this. This is what makes the databases "communicate."

---

## 4. Requirements

- **Idempotent ingest** — re-running a sync never duplicates (known dup-invoice issue must not spread).
- **Incremental** where the API supports it (GA4, Falcon, Ads); full-refresh only where cheap.
- **Timestamps in UTC**, stored raw + normalized; keep a `_synced_at` on every row.
- **Raw → staging → marts** layering (never query raw directly).
- **Secrets** stay where they are (.secrets/, Supabase vault) — brain reads via service accounts, never hardcodes.
- **Read-first**: brain reads everything; writes/actions are opt-in per source and logged.
- **RLS/least privilege** — the agent gets a read-only role scoped to marts, not raw PII.
- **Trading stays out.**

---

## 5. Phased build plan

**Phase 0 — Foundation**
- Stand up (or pick) the central Supabase project = the warehouse.
- Create the Client Registry table + seed it from the source you trust most (Drive ledger or Supabase leads).

**Phase 1 — Ingest the owned DBs**
- Sync 741-leads, 741-portal, phone_leads into the warehouse (or, if same instance, expose via views + registry joins).

**Phase 2 — Ingest marketing data**
- GA4 (36 props) → daily job via reporting-bot service account.
- Local Falcon → scheduled pull of scans/trends per location.
- GSC, Google Ads, Meta Ads → daily.

**Phase 3 — Ingest ops**
- Drive ledger + invoices (parse), Notion check-ins, LinkedIn CRM export.

**Phase 4 — Semantic layer**
- dbt/SQL marts: `client_360`, `pipeline`, `rank_performance`, `spend_vs_leads`, `revenue`.
- Wire everything to `canonical_client_id`.

**Phase 5 — Query surface**
- RAG + tool-calling agent with read-only SQL access to marts + a schema/description catalog.
- Metabase dashboards for the recurring views.

**Phase 6 — Actions (optional)**
- Let the brain trigger n8n flows (draft outreach, flag overdue NAD, alert on rank drops via Telegram).

---

## 6. THE MASTER PROMPT (hand this to a builder / new session)

> You are building the "741 Data Brain": a central data platform that unifies every
> 741 Digital Solutions data source into one queryable brain. Read
> `00_project/data-brain-plan.md` for full context.
>
> **Architecture (decisions LOCKED):** a NEW dedicated Supabase Postgres project (Frankfurt),
> separate from the live 741-leads/741-portal prod DBs, as the warehouse; n8n as the ingestion
> pipe; raw→staging→marts layering with dbt or SQL views; a Client Registry table
> (canonical_client_id) as the keystone, **seeded from the Drive master invoicing ledger**,
> that maps each client's IDs across every system; a **read-only** RAG + tool-calling agent as
> the query surface; Metabase for dashboards. **v1 is read-only — no writes or actions.**
>
> **Sources to integrate (in priority order):**
> 1. Owned Supabase DBs: 741-leads (advertorial_leads, giveaway_entries), 741-portal, phone_leads.
> 2. Marketing: GA4 (36 properties, reporting-bot service account), Local Falcon (~49 locations),
>    Google Search Console (741.studio), Google Ads (DE + Bali), Meta Ads (DE).
> 3. Ops: Google Drive invoicing ledger (2 entities: US LLC + PT Amana), Notion check-ins,
>    LinkedIn CRM pipeline.
>
> **Rules:** idempotent + incremental ingest (never duplicate — respect the known
> dup-invoice risk); UTC timestamps + `_synced_at` on every row; secrets read from
> existing stores (.secrets/, Supabase vault), never hardcoded; agent gets a read-only
> role scoped to marts, not raw PII; RLS on; **exclude all trading/TradingView data.**
>
> **Deliverables per phase:** (0) warehouse + Client Registry schema + seed;
> (1) owned-DB sync; (2) marketing sync jobs; (3) ops sync; (4) semantic marts
> (client_360, pipeline, spend_vs_leads, rank_performance, revenue); (5) query agent +
> dashboards; (6) optional n8n action triggers.
>
> Start with Phase 0: create the new dedicated Supabase warehouse project, read the Drive
> master ledger to derive the canonical client list, then show the Client Registry schema
> for approval **before** creating the table. Do not build any sync until the schema is approved.

---

## 7. Decisions — LOCKED (2026-08-13)

1. **Warehouse home** → **New dedicated Supabase project** (Frankfurt), separate from the live
   741-leads / 741-portal prod DBs. Clean separation, no risk to production.
2. **Registry seed** → **Drive master ledger** — the invoicing ledger is the authoritative list
   of real paying clients. Prospects/leads get merged in later (Phase 3) and deduped against it.
3. **v1 scope** → **Read-only first.** v1 = unify + query + dashboards. The brain answers
   questions across everything; it does not write or trigger anything. Actions (Phase 6, n8n
   triggers) are explicitly out of v1.
4. **Warehouse tech** → **Postgres-first** (the new Supabase project). BigQuery remains the
   documented escape hatch if GA4 analytics volume demands it later.

### Immediate next step for Phase 0
- Create the new Supabase project (the warehouse).
- Read the Drive master ledger → derive the canonical client list.
- Draft the Client Registry schema and get it approved **before** creating the table.
