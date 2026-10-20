# Weekly refresh job: client dashboard feeds

This job builds `dashboard.json` for one client from real sources. It only reads. It does not upload and does not touch the live portal.
Each client has one config file: `clients/<slug>.json` (built so far: `bali`, `huewel`, `dumann`, `johni`, `stuerzl`). New client: copy `clients/huewel.json` and its `.base.json`, set the ids, the domain (the job stops if the Search Console site does not belong to it) and the program start. Hand-written blocks live in the base feed of the client (Bali: `../src/feed-bali.json`, Hüwel: `clients/huewel.base.json`).

## Run

```bash
node 00_project/client-dashboard-redesign/portal/feed/build.mjs --client bali     # build, print diff against the Bali snapshot (src/feed-bali.json)
node 00_project/client-dashboard-redesign/portal/feed/check.mjs --client bali     # schema check + render check (same test as src/smoke.cjs)
node 00_project/client-dashboard-redesign/portal/feed/build.mjs --client huewel   # German feed, Google products only (no Local Falcon)
node 00_project/client-dashboard-redesign/portal/feed/check.mjs --client huewel   # structure check (render check waits for a generic dsh.js)
```

Options for `build.mjs`: `--client <slug>`, `--as-of YYYY-MM-DD`, `--base <file>`, `--out <file>`, `--ads-file <file>`, `--no-points`.
Exit code 0 = all sources read. Exit code 2 = a source failed. The failed block keeps the value of the base feed and is listed in `meta.refresh.failed`.

## Files

| Path | Content |
|---|---|
| `out/<slug>/dashboard.json` | The new feed. Same schema as `src/feed-bali.json`, plus extra keys under `meta` (`refresh`, `filling`, `sources`, `derived`). |
| `out/<slug>/diff.txt` | Diff against the snapshot of the client (Hüwel: the previous run). |
| `out/<slug>/refresh-log.json` | Failed blocks and warnings. Internal. |
| `data/<slug>/` | Stored raw reads: daily Google profile actions, WhatsApp taps, Search Console days, review dates (no names), scan index, and the 49 grid points of each map scan (`data/scans/<report_key>.json`). Scan files never change. The job skips a scan that is already saved. |

## Sources (all free, read only)

| Block | Source |
|---|---|
| `nhc`, `beauty` (calls, website visits, directions) | Google profile performance data, per profile |
| `wa` | GA4 property 428850764, event `contact_whatsapp`, from 2 Aug 2026 (before: `null`) |
| `gsc` | Search Console, property `https://www.balihealing.com/`, service account |
| `rev` | Live review list of both profiles. Leader review count from the latest "ozone therapy" map scan |
| `map`, `beautyMap` | Latest map scan per keyword (7x7 grid, not older than 60 days). Top-3 count comes from the 49 saved grid points |
| `ai` | Latest AI answer scan per keyword and AI tool |
| `ga4_events` (Hüwel) | GA4 events `whatsapp_click`, `phone_click`, `email_click`, `generate_lead`, from the tracking start. `wa` = `whatsapp_click` |
| `citations` (Hüwel) | Portal table `client_citations`, count per status (read only) |
| `reports` (Hüwel) | Portal table `client_reports` (title, period, link) |
| `ergebnisse` (Hüwel) | 30-day before/after block: Search Console windows from `clients/huewel.json`, one query, review count and star rating from the stored measurement (`work_outcomes`, client-visible row only), live citation count |
| `ads` | Saved file `assets/audit/balihealing/2026-10-11-kickoff/evidence/ads-read-*.json` (newest). Not read live |

## Rules in the job

- A value that cannot be read stays `null`. The job never estimates.
- A missing day makes the month `null`. A missing day is not a zero.
- The newest 3 days of Google profile numbers can still grow. They are listed in `meta.filling`. `meta.derived.running_month_settled` holds the running month without these days.
- The Ads file is not live. `meta.derived.ads.age_days` shows how old it is. The job warns after 7 days.
- Blocks written by hand are carried over from the base feed (`meta.refresh.carried`): banner, guide, needs (except the review line), work, decisions, tracks, tree, reports, funnel.
- The job calls only read tools of Local Falcon. It cannot run a scan (`lf.mjs` refuses every other tool).
- A client config with `"local_falcon": false` makes no Local Falcon call at all. No profile actions, no review list, no map, no leader, no AI block. Those keys are `null` in the feed.
- Portal reads (`supabase.mjs`) are GET only. The job never reads rows with `visibility = internal`.
- The feed file is public. It holds no tool names and no reviewer names.

## Promote to staging (manual, needs Martin's go)

1. Read `out/diff.txt`.
2. Copy `out/dashboard.json` to `src/feed-bali.json`.
3. Upload to `clients.741.studio/r/a331bf716f08/dashboard.json`.

## Clients without a feed yet

- Praxis Suriya, Maria Brasse: Search Console is not shared with the service account (`reporting-bot@studio-apis-503306.iam.gserviceaccount.com`). Martin must add it as user.
- Rabenmütter (shop), Kamil (mode "reports"), Testpraxis (test): no dashboard feed planned.
- Dumann: GA4 has data since 30 Sep. Someone must decide which event counts as an enquiry.
- The Google profile numbers and the map need a Local Falcon location per client (`local_falcon: true` and a `place_id` per profile). Only Bali uses them.

## Upload (manual step, `deploy.mjs`)

```bash
node 00_project/client-dashboard-redesign/portal/feed/deploy.mjs feeds [--client huewel,dumann]   # feed files to clients.741.studio/r/<feed_hash>/dashboard.json
node 00_project/client-dashboard-redesign/portal/feed/deploy.mjs portal <file.html> <backupName>  # backup of the live index.html, then upload to staging and live
```

- The folder name comes from `feed_hash` in the client config. The script checks that the client id in the feed equals the config. It reads the file back from the server and compares it.
- Portal file: build it with `portal/src/build.py <fresh live copy> <out.html>` on a FRESH copy of the live file. Check that the live file did not change before the upload.
- To switch the new dashboard on for a client: add the client id to `DSH_FEEDS` in `portal/src/dsh.js`, upload the feed, then upload the portal file.
- `preview.mjs --client <slug>` builds a local preview page (`out/<slug>/preview.html`) from the real module and the real feed. Nothing is uploaded.

## State 14 Oct 2026, 18:57 (Bali time)

Live for Bali, Hüwel, Dumann, Stürzl, Johni. Backup of the portal file: `clients.741.studio/backup/index-20261014-1857-before-dashboard-all-clients.html`. The weekly run is not scheduled yet: someone must run `build.mjs` and `deploy.mjs feeds` each week.

## Weekly refresh with one command (`refresh.mjs`)

```bash
node 00_project/client-dashboard-redesign/portal/feed/refresh.mjs                    # build + check all 9 clients, summary table, uploads nothing
node 00_project/client-dashboard-redesign/portal/feed/refresh.mjs --only bali,huewel # only these
node 00_project/client-dashboard-redesign/portal/feed/refresh.mjs --deploy           # also upload the feeds of the clients that built and checked clean
```

A missing grant (403) is a known gap: the block stays empty, `meta.refresh.gaps` and `out/<slug>/refresh-log.json` list it, the run is not a failure.
Clients: bali, huewel, dumann, stuerzl, johni, suriya, maria, rabenmuetter, kamil. Live today: the first five. Suriya, Maria: Search Console is a gap. Kamil: no program and no data source, reports only.

Null rules added 14 Oct (late): a month before the first day of Search Console data, or only partly covered, is `null` (`gsc.aug`, `gsc.jul`, `gsc.posJul`). `gsc` is `null` when the whole source is a gap. `meta.week` and `meta.weeks` are `null` without a program. `source_note` names only real sources and can be an empty text.

## Google profile data per client (state 14 Oct, evening)

`local_falcon: true` plus a `place_id` per profile in the client config switches on: monthly calls, website clicks and direction requests (`main`), reviews (`rev.main`) and, unless `map_enabled: false`, the map list (`map`). Place IDs in use: suriya, maria, stuerzl, huewel (no map: Martin's choice), dumann (the connected listing `...HMgI`; the other listing of the practice is permanently closed). Johni and Kamil: no place ID known yet. Bali keeps its own two-profile setup (`nhc`, `beauty`).
