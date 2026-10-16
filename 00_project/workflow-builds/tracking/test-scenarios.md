# 2.2 Test Scenarios: P6 Proof Tracking (`tracking`)

Date: 2026-10-16
Workflow: Proof Tracking + Quarterly War Room (`tracking`)

---

## Scenario 1: Obvious Trigger (Weekly Card Draft)
- **Prompt:** `/tracking weekly suriya`
- **Expected Action:**
  - Skill activates in `weekly` mode.
  - Loads client data for `suriya` from Supabase tables (`leads`, `gsc_daily_performance`, `geo_grid_scans`).
  - Emits weekly card draft and Loom talking points.
  - Writes telemetry to `00_project/assets/suriya/tracking/2026-10-16/_run.json`.
  - Prompts Martin for GO-W approval before portal push.
- **Expected Deliverable:** Weekly card text block + Loom bullet points.

## Scenario 2: Paraphrased Trigger (Quarterly War Room)
- **Prompt:** "Bereite die 90-Tage Quartalsrunde und den War-Room für Praxis Suriya vor"
- **Expected Action:**
  - Skill activates in `quarter` mode.
  - Pulls 90-day aggregate metrics across search, maps, calls, and form leads.
  - Builds executive war-room pack with performance vs baseline comparison.
  - Highlights open strategic decisions (budget, campaign targets, renewal scope).
  - Prompts Martin for GO-Q1 approval.
- **Expected Deliverable:** Quarterly war-room deck and client review pack.

## Scenario 3: Negative Trigger (Must NOT Trigger)
- **Prompt:** "Mach einen neuen Maps-Scan für Hüwel über Local Falcon"
- **Expected Action:**
  - Skill must NOT trigger.
  - Running an isolated on-demand Local Falcon scan belongs to `ranking-tracking-master-prompt.md` or the Maps Playbook, NOT the recurring proof tracking workflow.
- **Expected Result:** Rejection or routing to the appropriate single-scan script without invoking the tracking skill.
