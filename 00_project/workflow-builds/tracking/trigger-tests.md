# 4.1 Trigger Tests: P6 Proof Tracking (`tracking`)

Date: 2026-10-16
Skill: `.claude/skills/tracking/SKILL.md`

---

## Scenario 1: Obvious Trigger (Weekly Card Draft)
- **Prompt:** `/tracking weekly suriya`
- **Result:** **PASS**.
- **Execution Log:**
  - Frontmatter matched description (`/tracking <mode> <client>`).
  - Loaded checklist in `weekly` mode.
  - Executed `scripts/compute_weekly_metrics.py --client suriya`.
  - Emitted weekly draft card, Loom talking points, and telemetry to `00_project/assets/suriya/tracking/2026-10-16/_run.json`.
  - Stopped at GO-W approval gate without unauthorized database write.

## Scenario 2: Paraphrased Trigger (Quarterly War Room)
- **Prompt:** `Bereite die 90-Tage Quartalsrunde und den War-Room für Praxis Suriya vor`
- **Result:** **PASS**.
- **Execution Log:**
  - Matched prompt keywords ("Quartalsrunde vorbereiten", "War Room").
  - Loaded checklist in `quarter` mode.
  - Aggregated 90-day progress vs baseline and computed cost-per-booked-job attribution.
  - Prepared war-room pack draft.
  - Stopped at GO-Q1 approval gate.

## Scenario 3: Negative Trigger (Must NOT Trigger)
- **Prompt:** `Mach einen neuen Maps-Scan für Hüwel über Local Falcon`
- **Result:** **PASS (Correctly Rejected)**.
- **Execution Log:**
  - Frontmatter negative trigger evaluated: `Do NOT use for one-off Local Falcon ranking scans (use ranking-tracking-master-prompt)`.
  - Skill execution suppressed; prompt routed to single scan routine.
