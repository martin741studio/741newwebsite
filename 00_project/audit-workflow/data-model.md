# Data model — Maps audit database (PROPOSAL)

Status: proposal. No table exists. Martin must say "go" before I run `schema.draft.sql` on Supabase 741-portal (`galjmtozcgxcwtzkzbpi`).
Language: STE. Field names are English.

## Contents

1. Principles
2. Tables
3. Finding metadata (agent drill-down)
4. Run folder and JSON export
5. Re-audit comparison
6. Access and privacy
7. Links to existing tables

## 1. Principles

- One finding = one row. A finding answers one catalog field (`B05.03`) in one run.
- Every finding points to evidence. Evidence points to a raw file and the exact call that made it.
- The field catalog (`audit_fields`) is data, not code. The agent reads it to know what to collect. The scorer reads the rule from it.
- Agents write JSON first. A loader upserts JSON into the tables. The database can be rebuilt from the run folders.
- The client never reads the tables. The client reads a static `client.html` through the existing `client_reports` row.

## 2. Tables

| Table | One row is | Key columns |
| --- | --- | --- |
| `audit_fields` | One catalog field | `field_id` (PK, `B05.03`), `block`, `label_de`, `input_type` (C/A/B/D/M), `tool`, `weight`, `critical`, `light`, `rule` (jsonb), `client_safe`, `active`, `catalog_version` |
| `audit_runs` | One audit run | `id`, `client_id` (nullable, FK `clients`), `subject_slug`, `subject_name`, `subject_type` (client/prospect), `mode`, `depth`, `status` (planned, collecting, scored, reviewed, released), `params` (jsonb: keywords, grid, radius, competitor ids), `previous_run_id`, `score_total`, `score_coverage`, `verdict`, `verdict_reason`, `cost_eur`, `cost_credits`, `corrections_count`, `catalog_version`, `started_at`, `finished_at`, `released_at` |
| `audit_findings` | One answer to one field in one run | `id`, `run_id`, `field_id`, `status` (green, yellow, red, grey, unknown), `value` (jsonb), `finding_de`, `why_de`, `severity` (1-5), `impact` (1-5), `effort` (S/M/L), `owner`, `action_de`, `confidence`, `evidence_ids`, `source_tool`, `source_ref`, `refetch` (jsonb), `depends_on`, `drilldown_hint`, `client_safe`, `priority_rank`, `collected_at` |
| `audit_evidence` | One raw artifact | `id`, `run_id`, `kind` (falcon_report, api_json, screenshot, html_snapshot, form_answers, drive_file, file), `storage_path`, `drive_file_id` (for `drive_file`), `sha256`, `tool`, `request` (jsonb, no secrets), `cost_eur`, `cost_credits`, `collected_at`, `refetch_after` |
| `audit_answers` | One client answer (append-only) | `id`, `subject_slug`, `client_id`, `question_id`, `answer` (jsonb), `version`, `answered_by`, `answered_at`, `source` (form/martin/sheet_import) |
| `audit_keywords` | One keyword in one run | `run_id`, `keyword`, `priority` (1-3), `cluster`, `service_ref`, `volume`, `volume_source`, `falcon` (jsonb per platform: report_key, solv, arp, grid, radius, scanned_at), `credits` |
| `audit_competitors` | One competitor in one run | `run_id`, `rank`, `name`, `place_id`, `domain`, `reviews`, `rating`, `categories` (jsonb), `solv`, `arp`, `ref_domains`, `backlinks`, `first_seen`, `weakness`, `pick_reason` |
| `audit_actions` | One proposed action | `id`, `run_id`, `finding_ids`, `action_de`, `owner`, `impact`, `effort`, `go_required` (default true), `status` (proposed, approved, done), `task_id` (FK `tasks`, set after Martin's go) |

View `audit_run_deltas`: joins findings of a run with the findings of `previous_run_id` on `field_id`. Columns: `field_id`, `status_before`, `status_now`, `value_before`, `value_now`, `comparable` (true only when keywords, grid and radius match).

## 3. Finding metadata (agent drill-down)

Each finding carries these keys. An agent can go from the one-line finding to the raw data without asking.

| Key | Purpose |
| --- | --- |
| `field_id` | Stable id from the catalog. Never renamed. |
| `status`, `severity`, `impact`, `effort`, `owner` | Triage in one look. |
| `confidence` | `verified` (live this run), `derived` (computed from verified fields), `client_stated` (form). No other value is valid. |
| `source_tool`, `source_ref` | Tool name and the URL or report key. |
| `collected_at` | Time of the pull, ISO 8601, Europe/Berlin. |
| `evidence_ids` | Rows in `audit_evidence` with the raw file. |
| `refetch` | The exact call to repeat the pull: tool, parameters, expected cost. The agent repeats it with one command. |
| `depends_on` | Other `field_id` values this finding uses (for derived fields). |
| `drilldown_hint` | One sentence: what to look at next (for example "scan sub-keyword X for leader Y"). |
| `client_safe` | False hides it from `client.html` (fit, cost, internal flags). |

Evidence metadata: `sha256` proves the file did not change. `request` holds the parameters. `refetch_after` says when the data is stale (Falcon: 30 days, reviews: 14 days).

Example finding (JSON):

```json
{
  "field_id": "B05.03",
  "status": "red",
  "value": {"own_reviews": 14, "leader_reviews": 82, "own_new_90d": 2, "leader_new_90d": 9},
  "finding_de": "Bewertungstempo liegt bei 22 % des Marktführers.",
  "why_de": "Bewertungen entscheiden in Maps stärker als Links.",
  "severity": 4, "impact": 5, "effort": "M", "owner": "client",
  "action_de": "Bewertungsanfrage nach jedem Mandat einführen.",
  "confidence": "verified",
  "source_tool": "local-falcon", "source_ref": "place:ChIJyVGAdikEaW8RUOWpEJs-2XA",
  "collected_at": "2026-10-12T09:14:00+02:00",
  "evidence_ids": ["ev_0007"],
  "refetch": {"tool": "local-falcon:listLocalFalconLocations", "params": {"query": "STÜRZL Steuerstrafrecht"}, "cost": 0},
  "depends_on": [], "drilldown_hint": "Compare review text of leader for service words.",
  "client_safe": true
}
```

## 4. Run folder and JSON export

Path: `00_project/assets/audit/<subject-slug>/<YYYY-MM-DD>-<mode>/`.

```
run.json  findings.json  keywords.json  competitors.json  actions.json
manifest.json            # index of evidence: id, file, sha256, tool, request, cost, date
evidence/                # raw files (falcon reports, api json, screenshots, html snapshots)
report/internal.html  report/client.html
cost_ledger.jsonl
sheet-view.json
```

`scripts/load_run.py` upserts the folder into the tables (after the tables exist). `scripts/validate_run.py` checks the folder before any load.
The HTML report also embeds the findings as `<script type="application/json" id="audit-data">`. An agent can read one page and find every `field_id`.

## 5. Re-audit comparison

- The catalog ids, the keyword list, the grid size and the radius stay fixed in `audit_runs.params`.
- A new run sets `previous_run_id`. The view marks a delta `comparable` only for equal parameters.
- The report shows per block: arrow (better, same, worse) and the date of the last run.
- Answers are append-only. A re-audit asks only for answers older than 90 days or flagged "changed".

## 6. Access and privacy

- RLS: admin and team read and write. The client has no access to the audit tables.
- `audit_answers` can hold business figures. Law and health clients: no names of clients or patients. The form says so. The CRM upload is anonymized before it is stored.
- Evidence files hold no credentials. `request` is stored without keys.
- Retention: evidence of prospects who do not sign is deleted after 90 days (Martin to confirm).

## 7. Links to existing tables

| Existing table | Link |
| --- | --- |
| `clients` | `audit_runs.client_id` (null for a prospect) |
| `client_locations`, `client_master_data` | NAP truth for B06.05. Form answers B08.02-B08.04 can write to `client_master_data` after Martin's go |
| `scans` | The loader can copy Falcon reports into `scans` only after Martin's approval (playbook rule 2) |
| `visibility_prompts`, `visibility_results` | B12.04 reads them. B12.01 can fill `visibility_results` later |
| `client_citations`, `directories` | B07.02 and B06.05 |
| `access_grants` | B06.01 and B13.06 |
| `client_reports` | Release (Go-C) inserts the row that points to `client.html` |
| `tasks` | `audit_actions.task_id` after Martin's go |
