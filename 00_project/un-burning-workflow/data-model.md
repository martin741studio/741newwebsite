# Data model — Un-Burning (PROPOSAL)

Status: proposal. No table exists. Martin must say "go" before any Supabase or Drive write.
Language: STE. Field names are English. Machine-readable schema: `harm-register.schema.json`.

## Contents

1. Principles
2. Run folder
3. Harm item (the core object)
4. Severity rubric
5. Companion tables (NAP, redirects, index, link plan)
6. Snapshot and change log
7. Bedrock check (computed)
8. Re-scan comparison
9. Draft Supabase tables
10. Privacy

## 1. Principles

- One harm item = one row. Every row has evidence. Every evidence file has a hash and the call that made it.
- Agents write JSON first. A loader can rebuild the database from the run folders.
- The check catalog is data. Check ids (`UB.C04`) never change. Audit field ids (`B06.05`) are kept in `source_field`.
- A change never happens without a snapshot, a verify check and a rollback step.
- The client never reads the register. The client reads a released `client.html`.

## 2. Run folder

Path: `00_project/assets/un-burning/<client-slug>/<YYYY-MM-DD>-<mode>/`.

```
run.json                    # header: params, cost, bedrock result
harm-register.json          # items (schema in harm-register.schema.json)
preconditions.json           # onboarding facts (ownership, access, master). Not harm. Not scored
nap-master.json             # single source of truth
nap-corrections.json        # one row per listing to correct
redirect-map.json           # old URL, backlink count, target
index-intended.json         # indexed vs intended
link-plan.json              # inverted-tree internal link plan
changes.json                # plan file of the current wave (validated before execution)
change-log.jsonl            # one line per applied change (append only)
snapshots/ + snapshots.json # backups made before changes
manifest.json + evidence/   # raw files: id, file, sha256, tool, request, cost, date
report/internal.html        # damage map, area tables, evidence index
report/client.html          # client-safe, draft until GO-3
baseline/                   # frozen before-values (copied once)
cost_ledger.jsonl
```

## 3. Harm item

See the schema. Fields in short:

| Group | Fields |
| --- | --- |
| Identity | `id` (`H-C-014`), `area`, `entity`, `check_id`, `source_field` |
| What | `item`, `why`, `target` |
| Decision | `severity`, `action`, `action_detail`, `actor`, `effort`, `destructive` |
| Approval | `approval`, `approved_by`, `approved_at`, `wave` |
| Safety | `snapshot_id`, `rollback`, `verify_check` |
| Proof | `before`, `after`, `done_at` |
| Provenance | `confidence`, `collected_at`, `source_tool`, `evidence_ids`, `refetch`, `depends_on`, `drilldown_hint`, `client_safe` |

An agent drills down in this order: `item` → `evidence_ids` → `manifest.json` → raw file → `refetch` to repeat the pull.
Rule: `approval = done` is valid only with `snapshot_id`, `before`, `after`, `done_at` and `approved_at`. The validator rejects it otherwise.

## 4. Severity rubric

| Value | Meaning | Examples |
| --- | --- | --- |
| `blocks_revenue` | Customers cannot find, trust or reach the business, or the client lacks control | Wrong phone on listings. Missing form. Page 1 negative result. Intended money page not indexed |
| `leaks_link_power` | Search value is lost or wasted | 404 with backlinks. Redirect chain. Orphan page. Duplicate pages that split signals. Spam links |
| `cosmetic` | Visible or untidy but no measurable loss | Mixed spelling of the name on a minor directory. Old social banner |

**Ownership and access are not harm** (Martin, 2026-10-11). A missing owner role, Super User right, Search Console access or an unlocked master record is an onboarding precondition. It is not a register row, not a light and not a bedrock criterion. It marks affected actions `blocked` and goes to `preconditions.json`. Rate every item by its real effect on the client: `blocks_revenue` only if customers cannot find, trust or reach the business.

Action meaning: `keep` (checked, no change), `fix` (edit in place), `merge` (combine pages or profiles), `redirect` (301), `delete`, `report` (report to Google or a platform), `claim` (take ownership of a listing or asset).
Destructive = `delete`, `report` and `merge` of live pages. Each needs its own go.

## 5. Companion tables

**preconditions.json** (onboarding artefact, not part of the register): access status per asset and the master record status. Template: `who-owns-what-template.md`.

**nap-master.json**: name, address, phone, website, email, opening hours, categories, legal form, `locked_at`, `locked_by`, `old_values` (list of known old names, old addresses, dead numbers). Source: `client_locations` plus the client's own confirmation. Never guessed.

**nap-corrections.json**: per listing: `directory`, `url`, `field`, `old_value`, `correct_value`, `method` (self, brightlocal, client_login), `status` (found, planned, submitted, live, verified), `last_checked`.

**redirect-map.json**: `old_url`, `status_now`, `backlinks` (count and source), `gsc_clicks_90d`, `target_url`, `reason`, `type` (301), `approval`.

**index-intended.json**: per URL: `indexed` (yes/no/unknown, source), `intended` (yes/no), `class` (money, service, location, blog, system, archive), `verdict` (`ok`, `index_missing`, `index_unwanted`), `action`.

**link-plan.json**: inverted tree. Per page: `parent` (service page), `grandparent` (home), `inbound_content_links`, `outbound_to_parent`, `missing_links` (anchor and target). Navigation and footer links do not count.

## 6. Snapshot and change log

| Target | Snapshot method | Rollback |
| --- | --- | --- |
| WordPress page, menu, redirect rule | Export post and postmeta to `snapshots/<id>.json` before the change (the 26.09 backup pattern) | Restore the exported JSON through the same route |
| Listing field | Screenshot plus text of the old value in `snapshots/` | Re-enter the old value |
| GBP field | Screenshot plus values from the Maps read | Re-enter the old value |
| DNS or registrar record | Zone export | Restore the export |
| Robots, sitemap, noindex | File copy | Restore the copy |

`change-log.jsonl` line: `ts`, `item_id`, `wave`, `actor`, `approved_at`, `snapshot_id`, `action`, `target`, `before`, `after`, `verify_result`, `rollback`. Append only. Never edited.
Rule from the Hüwel lesson (2026-10-07): export media references before any content change. Check that images still load after the change.

## 7. Bedrock check (computed)

Script `bedrock.py` reads the register. Per area:

| Light | Rule |
| --- | --- |
| Green | No open `blocks_revenue` item and at most 10 percent of `leaks_link_power` items open |
| Yellow | No open `blocks_revenue` item but more than 10 percent of `leaks_link_power` items open |
| Red | At least one open `blocks_revenue` item |
| Grey | Area not applicable or not scanned |

`ready_for_growth` is true only when C, D and E are green and no area is red. Area A is retired. "Open" means `approval` is not `done` and not `keep` or `rejected` with a written reason.

## 8. Re-scan comparison

- A re-scan uses the same `params` (sitemap, directory list version, GSC property). A changed parameter marks the delta "not comparable".
- The tracker joins items by `check_id` plus `target`. States: fixed, still open, new, regressed.
- Metric tracker (before/after): GBP calls, routes, site clicks; indexed pages; 404 count; NAP consistency percent; inquiries per week. Baseline files sit in `baseline/`.
- NAP consistency percent = listings with name, address and phone identical to the master, divided by listings checked.

## 9. Draft Supabase tables (not applied)

| Table | One row is |
| --- | --- |
| `ub_runs` | One run (client_id, mode, params, cost, bedrock) |
| `ub_items` | One harm item (columns as in the schema, jsonb for before/after/refetch) |
| `ub_evidence` | One raw artifact (sha256, tool, request, storage_path) |
| `ub_changes` | One applied change (change log line) |

RLS: admin and team read and write. The client has no access. A view `ub_deltas` compares two runs. A SQL file is written only after the go.

## 10. Privacy

- Evidence holds no passwords or tokens. `request` is stored without keys.
- Health clients: no patient data in evidence. Review exports hold only the public text.
- Account logins found during access checks go to the existing `client_credentials` vault, never into the register.
