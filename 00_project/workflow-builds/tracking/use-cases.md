# 2.1 Use Cases: P6 Proof Tracking (`tracking`)

Date: 2026-10-16
Workflow: Proof Tracking + Quarterly War Room (`tracking`)

---

### Use Case 1: Weekly Progress Card (Monday 07:30 Berlin)
- **Trigger:** `/tracking weekly <client>` (e.g. `/tracking weekly suriya`) or automated Monday morning routine.
- **Steps:**
  1. Fetch fresh weekly metrics: GBP calls, form leads from `leads`, search impressions/clicks from `gsc_daily_performance`.
  2. Compute weekly conversion delta against `client_goals`.
  3. Generate weekly summary card draft for the portal "Ergebnisse" tab.
  4. Generate concise 3-bullet Loom talking points for Martin.
  5. Emit `_run.json`.
- **Tools:** Supabase client, GSC performance fetcher, `write_run.py`.
- **Deliverable:** Draft weekly card, Loom talking points, telemetry log. Requires Martin's GO-W release before publishing to client portal.

### Use Case 2: Early Warning & Alert Check
- **Trigger:** Automated daily health check or `/tracking check <client>`.
- **Steps:**
  1. Evaluate the 6 Red rules (R1: profile phone changed, R2: site down, R3: zero leads in 14 days, R4: tracking container missing, R5: suspension notice, R6: verification revoked).
  2. Evaluate Yellow warning rules (Y1–Y9: impressions dropped > 25%, grid SoLV dropped, negative review received).
  3. Red: send immediate email alert to `martin@741.studio`.
  4. Yellow: surface on 08:05 daily standup board.
- **Deliverable:** Alert record, immediate mitigation steps.

### Use Case 3: 90-Day Quarterly War-Room Pack
- **Trigger:** `/tracking quarter <client>` (5 working days before quarterly meeting).
- **Steps:**
  1. Roll up 90-day performance vs baseline: total leads, booked jobs, customer acquisition cost (CAC), Local Falcon rank distribution progression.
  2. Reconcile revenue impact vs 741 fees + ad spend.
  3. Compile war-room presentation pack for Martin with 3 strategic renewal options.
  4. Record decisions in client strategy log.
- **Deliverable:** War-room executive pack, client proof page draft. Requires Martin's GO-Q1 / GO-Q2 approvals.
