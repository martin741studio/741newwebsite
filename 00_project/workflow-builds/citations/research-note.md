# Research Note: Citations DACH Workflow (`citations`)

* **Workflow ID:** `citations`
* **Phase:** P4 (Build-up)
* **Building Block:** Project Skill (`.claude/skills/citations-dach/`) wrapping deterministic Node.js scripts.

## 1. Relevant Rules (rules.md)
* **Rule R1.7 (Degrees of Freedom):** Fragile directory scraping, BrightLocal API imports, and database upserts are strictly encapsulated in executable scripts (`reporting/citation-monitor.mjs`, `reporting/import-brightlocal.mjs`, `reporting/submission-runbook.mjs`).
* **Rule R2.1 (Frontmatter):** `disable-model-invocation: true`, narrow `allowed-tools`, strict negative trigger against authority backlinks.
* **Rule R6.3 (State Ledger):** Writes status records to Supabase `client_citations` and emits `_run.json` in the client's asset folder.

## 2. Existing 741 Assets Reused
* Database table: `public.client_citations` (273 rows across 5 clients already verified in Supabase).
* Canonical NAP Source: `public.client_locations`.
* Monitoring script: `reporting/citation-monitor.mjs`.
* Submission generator: `reporting/submission-runbook.mjs`.
* BrightLocal parser: `reporting/import-brightlocal.mjs`.
