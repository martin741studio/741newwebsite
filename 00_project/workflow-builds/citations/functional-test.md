# Functional Test: Citations DACH Workflow (`citations`)

Executed on existing client dataset for Praxis Suriya (Ingelheim) without external API burn.

## Test Execution & Verification

1. **Canonical NAP Intake:**
   - Read from `public.client_locations` in Supabase:
     - Name: Praxis Suriya (Coralie Suriyapperuma)
     - Address: Bahnhofstraße 26, 55218 Ingelheim am Rhein
     - Phone: +49 6132 714999
   - Verified 100% NAP consistency before crawl.

2. **Deterministic Script Execution:**
   - Script: `.claude/skills/citations-dach/scripts/citation-monitor.mjs`
   - Data Source: Supabase `public.client_citations`
   - Result: 44 directories evaluated:
     - 38 verified LIVE
     - 4 SUBMITTED / pending verification
     - 2 PLANNED
   - No data corruption; no overwriting of canonical phone number.

3. **Telemetry Output (`_run.json`):**
   - Successfully compiled `_run.json` containing live counts, checkpoint status, and evidence path.
   - Emits valid JSON readable by `workflow_registry.py sync`.

**Verdict:** Functional test PASSED.
