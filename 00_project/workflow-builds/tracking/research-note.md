# Research Note: P6 Proof Tracking (`tracking`)

Date: 2026-10-16
Owner: Martin Drendel
Workflow: Proof Tracking + Quarterly War Room (`tracking`)

---

## 1.1 Building Block Selection
- **Chosen Block:** **Skill (`~/.claude/skills/tracking/`) with isolated CLI scripts in `scripts/`**.
- **Reason:** Tracking combines qualitative editorial strategy (weekly Loom talking points, quarterly war-room synthesis) with strictly deterministic data math (delta error calculation, Local Falcon grid parsing, GSC aggregation, CPA computation). Per Rule R1.7, math lives in `.py`/`.mjs` scripts while synthesis lives in the skill checklist.

## 1.2 Library Search
- Grep in `00_project/knowledge/workflow-library/`:
  - `rules.md`: §2 (Verification & Gates), §6 (Unattended and Scheduled Rules, cron scheduling, error-signal alerting).
  - `patterns.md`: §4 (Pipelines: Weekly, Monthly, Quarterly checkpoints), §5 (Folder Structure).
  - `scorecard.md`: Scoring standards for tracking accuracy and verification.

## 1.3 Freshness Rule
- Master knowledge library `INDEX.md` dated 2026-10-11 (< 1 week old, fresh). Local Falcon and Search Console APIs verified active on 2026-10-12. No third-party data obsolescence.

## 1.4 Existing 741 Assets Check
- Spec: `00_project/tracking-workflow.md` (27 KB master spec).
- Metrics: `00_project/tracking-metric-catalog.json` (34 metric definitions, 31 in v1).
- Coverage Map: `00_project/tracking-coverage-map.md`.
- Prototype: `00_project/assets/tracking-workflow/prototype/` (Board 5 & Board 6 layouts).
- Database Schema: `public.client_goals`, `public.geo_grid_scans`, `public.gsc_daily_performance`, `public.leads` in Supabase `741-portal`.

## 1.5 Open Questions & Architecture Decisions
1. **Pilot Client:** Praxis Suriya (Coralie Suriyapperuma).
2. **Weekly Cadence:** Runs Monday 07:30 Berlin time. Produces draft card in portal tab + Loom talking points for Martin.
3. **Telemetry Contract:** Writes `00_project/assets/<client>/tracking/<YYYY-MM-DD>/_run.json` with processed metric counts and discrepancy deltas.
