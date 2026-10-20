# Scan brief (common) — Un-Burning, client STÜRZL Steuerstrafrecht

Date: 2026-10-11. Mode: `scan` (read only). Repo: `/Users/martindrendel/741website`. Run folder: `/Users/martindrendel/741website/00_project/assets/un-burning/stuerzl/2026-10-11-scan/`.
Client: Dr. Anja Stürzl, law firm "STÜRZL Steuerstrafrecht", Frankfurt am Main (main office) and München (second office, Lea Wimmer). Website `https://stuerzl-steuerstrafrecht.de` (Joomla, Helix Ultimate, SP Page Builder, hosting Artfiles). Portal client id `b6f6e303-50e4-4afb-a343-337206cec316`. GBP Frankfurt place id `ChIJyVGAdikEaW8RUOWpEJs-2XA`.
This is a LAW FIRM. Professional secrecy applies (§203 StGB): never name a client or a case. Professional advertising rules apply (BRAO, BORA, UWG). Address form with the client: Sie.

## Absolute rules

1. READ ONLY. Change nothing on any client asset: no website edit, no Joomla write, no GBP or listing edit, no email, no Supabase write, no Drive write, no GSC submission or disavow upload, no Local Falcon scan, no form submission on any site, no account creation, no login. Do not use the built-in browser or Chrome automation. Do not call any DataForSEO endpoint (0 EUR spend). Firecrawl and curl are allowed.
2. Write ONLY inside the run folder (and only the files named in your scope). Keep scripts in `scripts/<your-area>/` inside the run folder. Run Python as `python3 -I`.
3. Every item needs evidence saved under `evidence/<area>/` (raw file), a manifest row (id, file, sha256, tool, request without secrets, collected_at), `confidence` (`verified` = read live in this run, `derived` = computed from verified data or from older stored data with its date, `client_stated` = from a client call or mail), and `collected_at` (Europe/Berlin ISO). Never guess. A source that fails is recorded as "unreadable" with the error, never as "nothing found".
4. Evidence ids start with `EV-<AREA>-` where AREA is the area letter of the item (A, C, D or E). Item ids are `H-<AREA>-NNN` starting at 001 per area.
5. No tool names, no client names, no case details in `client_text` (plain German, Sie-form is NOT needed in client_text: write neutral sentences).
6. Re-verify before you reuse. Older stored data (see `baseline/`) is `derived` and must carry its original date. If you re-read it live and it still holds, mark `verified`.

## Inputs already in the repo (read these first)

- Schema (your output must follow it): `00_project/un-burning-workflow/harm-register.schema.json` and `00_project/un-burning-workflow/data-model.md` (sections 3 to 5).
- Spec runbooks: `00_project/un-burning-workflow.md` section 6 (areas A to E) and section 7.
- Provisional master: `00_project/assets/un-burning/stuerzl/2026-10-11-scan/nap-master.json` (NOT locked; compare every source against both the OLD and the PROPOSED address and report which one it shows).
- Existing data: `00_project/assets/un-burning/stuerzl/baseline/` — `stuerzl-woche1-befunde-2026-10-01.md` (sections 1, 3, 9, 10, 11 hold earlier findings), `stuerzl-umsetzung-backlog.md`, `disavow-liste-2026-10-09.md`, `crawl.json`, `backlinks_summary.json`, `bl_anchors.json`, `bl_refdomains.json`.
- Memory notes (context): `/Users/martindrendel/.claude/projects/-Users-martindrendel-741website/memory/anja-stuerzl-client.md`.
- A finished example of the same kind of run for another client: `00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/` (look at `harm-register.json` item style, `manifest.json`, `nap-corrections.json`). Match its depth and style. Its `scripts/` folder holds crawl helpers you may read and copy into your own scripts folder.
- The validator you must pass: `python3 -I 00_project/un-burning-workflow/skill-draft/scripts/validate_run.py <folder>` works on a folder with `harm-register.json` + `manifest.json`. Build your partial files as `part-<area>/harm-register.json` (with a `run` header copied from the example, `params.scanned_areas` set) and `part-<area>/manifest.json`, and validate each part folder with that script.

## Item fields (short)

`id, area, entity, item (German, one sentence), why (German, one sentence), check_id (UB.A01 ...), source_field (audit id or null), target, severity (blocks_revenue | leaks_link_power | cosmetic), action (keep | fix | merge | redirect | delete | report | claim), action_detail, actor (client | 741 | google), effort (S|M|L), destructive (true for delete, report, merge), approval (always "proposed", or "blocked" if it needs access you lack), confidence, collected_at, source_tool, evidence_ids (min 1), refetch, drilldown_hint, client_safe, client_text (only for items safe to show a client)`.
Severity rubric: blocks_revenue = clients cannot find, trust or reach the firm, or the client lacks control. leaks_link_power = search value lost. cosmetic = untidy, no measurable loss.
Checked-and-fine results are also rows with `action: keep` (so the register shows what was verified). Keep them short.

## Reply format

Final message under 40 lines: counts per area and severity, the 5 biggest items, tools that failed, what you could not verify, and the path of your part folders. Do not write a summary .md file; the caller writes it.
