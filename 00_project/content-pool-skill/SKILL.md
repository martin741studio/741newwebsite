---
name: content-pool
description: Build the 741 content pool for a client website, then the sitemap from it. Turns real competitor data and real search-demand data into a ranked list of content items in four pillars (location, main service, brand, authority), built on the client's own services and facts, with proof for every item, an HWG or BRAO flag, an HTML report and an xlsx. Use when Martin says "Content-Pool für <Name>", "welche Inhalte braucht die neue Seite von <Name>", "Content-Pool prüfen", "Wettbewerb und Suchnachfrage für die Startseite auswerten", or runs /content-pool <client>. Works for new sites and existing sites. Do NOT use for writing page copy (seo-page-optimizer), the CRO homepage prototype (cro-homepage), the sitetree and catchment report (structure playbook), a single practitioner page (behandler-seite), review pages (local-seo-review-page) or backlink work (backlink-dach).
---

# content-pool

## Critical

1. Every number comes from a script and a raw data file. Never type a volume, a count or a share into a note. Run `scripts/validate_pool.py` and report only when it exits 0.
2. Fit first. A keyword or topic enters the pool only if it matches a service the client really offers (or is education around one). Competitor keywords for services the client does not offer are cut and logged, never targeted.
3. Never send, publish or change a live site. The client form is a draft until Martin says "go". Ask for the cost cap before the first paid call (default 5 USD). Stop at the cap.
4. A page or competitor that cannot be read is reported as "unreadable". It is never read as "nothing found". A claim that depends on it carries the caveat.

## Inputs Martin gives at the trigger

Client name, URL (or "new site"), city, GBP link, mode (new or existing), industry mode (HWG, BRAO, none), cost cap. Ask once, in one line, for what is missing.

## Run kit

Source of truth: `00_project/content-pool-workflow.md`. Read it fully at the start of every run. Data model: `00_project/content-pool-data-model.md`. This file only tells you how to operate it. Paths below are relative to this skill folder. The run folder is `00_project/assets/<slug>/content-pool/`.

Copy this checklist into your first reply and tick it off:

- [ ] Step 0 Readiness: inputs, folder, DataForSEO balance, GSC access (403 = `[FEHLT]`), cap
- [ ] Step 1 Client baseline → `01-client/client-baseline.md` (reuse the CRO `dataset.md` and `brand.md` if they exist)
- [ ] Step 2 Seeds from real services × places × question words; check each against the service list
- [ ] Step 3 Competitors (cities need `location_code`, not `location_name`; a site without a sitemap is crawled by `site_urls.py`): `python3 scripts/dfs.py serp/google/organic/live/advanced <payload> <out> --run-dir <run>` per key search; choose the set (local, niche, topic; portals become link targets); `python3 scripts/page_metrics.py --urls-file <urls.txt> --out 02-competitors/metrics.json --places "<places>"`; `python3 scripts/site_urls.py --out 02-competitors/site_urls.json <domains>`; retry failed pages (gate A0)
- [ ] Step 4 Demand: volume call(s), `python3 scripts/autocomplete_tree.py --letters --out 03-demand/autocomplete.json "<seed>" …`, ranked keywords of own and competitor domains, Trends for seasonal terms, GSC if available
- [ ] Step 5 Write `04-pool/candidates.json` from `assets/candidates.template.json` (judgment only)
- [ ] Step 6 `python3 scripts/build_pool.py --run-dir <run>`; write `04-pool/summary.json` (see `assets/summary.example.json`)
- [ ] Step 7 `python3 scripts/validate_pool.py --run-dir <run>`; fix until 0 errors; check each typed claim in notes against the data
- [ ] Step 8 `python3 scripts/render_report.py --run-dir <run>`; open the HTML in Claude in Chrome; check desktop width, a narrow width and one opened card
- [ ] CHECKPOINT 1: show Martin the report. Wait for "go". He decides adjacent items and the audience split
- [ ] Step 9 Hand off: Drive upload (browser method as in the CRO skill), `04-pool/pool-top.md`, Drive link + screenshot + draft client message

Sitemap (after checkpoint 1, section 15 of the spec):
- [ ] Step 10 Inputs: own page measures (`page_metrics.py` on the real service URLs), GSC pages, backlink summary of client and 3 competitors (`dfs.py backlinks/summary/live`)
- [ ] Step 11 Write `05-sitetree/tree.json` (judgment). Read the target page before you propose a redirect
- [ ] Step 12 `python3 scripts/build_sitetree.py --run-dir <run>`; fix until 0 errors; check the HTML in Chrome
- [ ] CHECKPOINT 2: show Martin the sitemap. Wait for "go"

Steps 0 to 8 run without asking. Stop at a failed gate, at the cap, and at the checkpoint.

## Degrees of freedom

- Fixed (scripts): all numbers, scores, priority, validation, report. Do not change a score by hand. Change the judgment value in `candidates.json` and rebuild.
- Open (agent judgment): topics, fit, conversion, effort, HWG flag, search patterns, summary findings.

## Rules to apply while judging

- Fit: 3 exact service, 2 education or question around a real service, 1 adjacent (client confirms, Martin decides, never priority A), 0 not offered (cut).
- A keyword without a place name is national (volume counts 0.6). Volume "no data" is not zero demand: check autocomplete and PAA.
- A place page enters the pool only with demand, a catchment signal and unique local facts. Otherwise name the place in text.
- A client with two audiences (for example practice and school): set `audience` and keep the homepage for the main audience.
- Competitors that are portals (doctolib, jameda, …) are link targets for `backlink-dach`, not competitors.
- HWG: no healing promises, no disease lists, no before/after, no fear wording. BRAO for lawyers: no title claims without proof.
- Replies and working files in STE. Client text is normal German with "du". Never name tools or method sources in client material (call it "741 Content-Pool-Raster").

## Output

HTML report and xlsx (`render_report.py`), `pool.json`, `pool-top.md`, a draft German client form from `assets/client-input-form-de.md` (only the open `[FEHLT]` points). End the run with: the Drive link, the report screenshot as a file, the validator output, the spend, and the list of decisions for Martin.

## Checkpoint

After step 8: show Martin the findings, the pillar cards and the homepage map. Wait for "go". Changes: revise only the named items and rebuild.

## Not enabled elsewhere

`~/.claude/skills/` is not read by Cowork or routines. Enable in Customize > Skills if ever needed.

## Registry entry (2026-10-11)

Every run of this workflow is recorded in the workflow registry. The Excel `~/Desktop/Workflow-Uebersicht.xlsx` shows per client whether the workflow ran, its state, the last run, Martin's approval and the folder links.
- At the start or end of a run: `python3 /Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py upsert --client "<client>" --workflow pool --status "in Arbeit|Trockenlauf|fertig, Freigabe offen" --local <folder> --drive <url> --result <file>`
- When Martin approves the result: `python3 /Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py approve --client "<client>" --workflow pool` in the same turn, then tell Martin the sheet was updated. A hook reminds Claude when a message sounds like an approval.
Workflow id: `pool` (Content Pool).

## Registry: automatic (2026-10-11)

The overview Excel `~/Desktop/Workflow-Uebersicht.xlsx` updates itself. A Stop hook runs `workflow_registry.py sync --quiet` after every turn. You do not call `upsert` for normal progress. Write one line per step into `00_project/assets/<client>/content-pool/_status.md` (date at the start of the line). Report plus Drive upload marker makes the run fertig, Freigabe offen.
For any other file layout, write `_run.json` in the run folder (schema in `00_project/workflow-registry/README.md`). Only the approval stays manual: when Martin approves a result, run `approve` in the same turn and say that the Excel is updated.

## Martin guide (2026-10-12)

The 741 character Martin points out the one thing per section the reader must not miss. Rules, poses, markup and the inline helper: `00_project/assets/brand/martin-guide/README.md`. In this workflow: in the client version of the pool report and the sitemap: present at each pillar, point at the A priorities, think at client questions. Max 1 callout per section, bubble text in first person and plain language, every number with source and date, check desktop and mobile with a screenshot.
