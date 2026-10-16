# Functional Test: Maps Audit Workflow (`audit`)

Executed using existing local dataset without third-party API spend (as instructed by Martin: "use what we have").

## Test Execution on Stürzl Existing Dataset

1. **Intake & Local Data Assembly:**
   - Canonical NAP loaded from `client_locations`.
   - Local Falcon historical grid scans loaded from `00_project/assets/stuerzl/` and Supabase `geo_grid_scans`.
   - Citations loaded from Supabase `client_citations` (44 directories).
   - Website technical parameters loaded from baseline audit records.

2. **Deterministic Math Verification:**
   - Script: `.claude/skills/maps-audit/scripts/score.py`
   - Catalog: `.claude/skills/maps-audit/references/catalog.json` (100 total potential points across 6 categories).
   - Execution: Scored cleanly across categories (Profile, Website, Reviews, Citations, Local Signals, Engagement).
   - Result: Deterministic score calculated identically on repeated executions (no LLM hallucination).

3. **Harm vs. Gap Separation:**
   - Identified 1 critical Harm item: Address discrepancy following the move to Untermainkai 26.
   - Identified 2 optimization Gaps: Incomplete review response velocity and missing primary category secondary keyword in title.
   - Harm correctly separated into `harm-register.json` to block premature growth measures in P4.

**Verdict:** Functional test PASSED. Workflow executes strictly using local data and produces deterministic scoring without external token/credit burn.
