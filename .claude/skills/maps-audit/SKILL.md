---
name: maps-audit
description: Runs the 100-point Google Maps readiness audit and harm diagnosis for a local business. Reads GBP profile data, website, citations and local competitor assets, scores them with deterministic scripts, and builds an internal audit report with harm separation. Trigger on "starte den Maps-Audit", "/maps-audit", "Maps-Readiness prüfen", "audit client X". Not for single-page content (seo-page-optimizer) or weekly proof tracking (tracking).
disable-model-invocation: true
context: fork
allowed-tools: Read, Write, Edit, Bash(python3:*)
---

# Maps Audit (`audit`)

Spec: `00_project/audit-workflow-spec.md` · Design: `00_project/audit-workflow/design-note.md` · Language: STE · Registry ID: `audit` · Phase P2.

## Critical

1. **Existing data first.** Use `00_project/assets/<client>/` before any external API call.
2. **No paid scan without Go-A.** No paid DataForSEO or Local Falcon credits without Martin's explicit Go-A.
3. **Harm vs. gap.** Every red finding is *Harm* (penalty risk, toxic links, NAP conflict) or *Gap* (missing optimisation). Harm is cleared in P3 before growth in P4.
4. **Deterministic math.** Scores come only from `scripts/score.py` reading `references/catalog.json`, never from the prompt.
5. **Telemetry.** Every run writes `00_project/assets/<client>/audit/<YYYY-MM-DD>/_run.json` (sample: `references/run-json.md`).

## Steps

1. Intake: check client slug, canonical domain, GBP place ID and 5 target keywords. Create the run folder `00_project/assets/<client>/audit/<YYYY-MM-DD>/`. Strategy `--strategy maps|paid|balanced` (default `maps`).
2. Assemble local data: Local Falcon scans (`00_project/assets/<client>/` or Supabase `geo_grid_scans`), `brightlocal_audits`, `gsc_daily_performance`, and `python3 scripts/site_check.py --url <client_url> --out <run_dir>/site.json`.
3. **Go-A:** if paid scans are needed, show plan and cost. Wait.
4. Score: `python3 scripts/score.py --catalog references/catalog.json --input <run_dir>/data.json --out <run_dir>/score.json`
5. Drivers: `python3 scripts/analyze_drivers.py --score <run_dir>/score.json --out <run_dir>/drivers.json`. Extract red items to `<run_dir>/harm-register.json`.
6. Report: `python3 scripts/build_report.py --run <run_dir>` (writes `audit-report.md` and `audit-report.html`).
7. Client safety: `python3 scripts/check_client.py --file <run_dir>/audit-report.html` (no tool names, API costs or contractor names).
8. **Go-B:** show the score (0-100), top 3 harm drivers and the report link. Wait.
9. Write `_run.json`. The Stop hook runs `workflow_registry.py sync`.

## Verification

`python3 scripts/validate_run.py --run <run_dir>` must print `VALIDATION PASSED`. Fix schema errors until it does.
