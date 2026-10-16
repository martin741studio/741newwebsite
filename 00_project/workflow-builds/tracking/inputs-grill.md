# Step 0.0 Inputs Grill Record: P6 Proof Tracking (`tracking`)

Date: 2026-10-16
Owner: Martin Drendel
Workflow ID: `tracking`
Status: Confirmed

---

## 1. The Job (Objective & Scope)
- **What enters:** Google Business Profile performance metrics, Local Falcon grid scans, Search Console daily rollups, website form submissions from `leads`, client billing/ad spend, Google reviews.
- **What transforms:** Aggregates and reconciles lead-to-booked conversion chains, computes cost per booked job, identifies performance discrepancy deltas ($\Delta = \text{Actual} - \text{Goal}$), flags early warning signals (red/yellow), and synthesizes the 90-day quarterly war-room pack.
- **Who uses output:** Client (portal tab "Ergebnisse"), Martin (weekly Loom review + quarterly meeting), and operations team (daily standup early warnings).

## 2. Runtime Surface
- **Primary surface:** Terminal (Claude Code `/tracking`), Portal tab (`clients.741.studio`), and morning grill / daily standup.
- **Enforcement surface:** Programmatic verification scripts in `scripts/`, `_run.json` telemetry, and checkpoint approval gates.

## 3. Cadence / Frequency
- **Weekly:** Monday 07:30 Berlin (weekly card draft + Martin Loom).
- **Monthly:** First Monday of month (grid scan reconciliation + monthly progress review).
- **Quarterly:** 5 working days before 90-day client strategy meeting (war-room pack synthesis).

## 4. Hard Limits (Failure Boundaries)
- **Zero Guessed Metrics:** Missing client data displays as "fehlt seit <Datum>" with one reminder; cost per booked job stays blank rather than estimated.
- **No Direct Call Tracking Numbers:** The primary business phone number remains intact on the GBP profile; call clicks and lead log track calls.
- **Zero Unapproved Client Publishing:** All client portal cards and war-room sections remain draft until Martin's explicit release (GO-W, GO-M, GO-Q2).
- **Spend Ceiling:** Strict 5 EUR per client per month cap on third-party APIs (DataForSEO + model tokens) plus locked monthly Local Falcon credits.
- **Safe Alerts:** Red alerts immediately sent to `martin@741.studio`; clients never see raw alerts without Martin's review.
