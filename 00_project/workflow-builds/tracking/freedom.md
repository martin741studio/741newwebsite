# 2.5 Degrees of Freedom: P6 Proof Tracking (`tracking`)

Date: 2026-10-16
Workflow: Proof Tracking + Quarterly War Room (`tracking`)
Standard: Rule R1.7 Separation of Deterministic Math vs Qualitative Synthesis

---

| Pipeline Step | Nature | Implementation | Rationale |
|---|---|---|---|
| **Step 1: Data Ingestion** | Deterministic | `scripts/fetch_tracking_data.py` | Querying Supabase `leads`, `gsc_daily_performance`, `geo_grid_scans` requires exact SQL and JSON parsing. |
| **Step 2: Metric Delta Math** | Deterministic | `scripts/compute_weekly_metrics.py` | WoW and MoM percentage calculations, goal discrepancy ($\Delta = \text{Actual} - \text{Goal}$), and CPA math must never be left to LLM hallucination. |
| **Step 3: Alert Rule Engine** | Deterministic | `scripts/check_alert_rules.py` | Checking Red rules (R1–R6: phone change, downtime, zero leads) and Yellow rules (Y1–Y9: -25% traffic) requires boolean logic. |
| **Step 4: Card Copywriting** | Qualitative | `SKILL.md` (Prompt Heuristics) | Crafting clear, encouraging, plain-language updates for German business owners requires editorial finesse. |
| **Step 5: Loom Talking Points** | Qualitative | `SKILL.md` (Prompt Heuristics) | 3 bullet talking points tailored to the client's current emotional state and progress. |
| **Step 6: War-Room Strategy Deck** | Qualitative + Data | `SKILL.md` + template | Synthesizing strategic renewal recommendations and packaging value for the 90-day review. |
| **Step 7: Telemetry Emission** | Deterministic | `scripts/write_run.py` | Emitting standardized `_run.json` with processed counts and status. |
