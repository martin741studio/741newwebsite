# Content Pool: Data Model

Status: proposal, tested on the Dumann dry run (2026-10-11). The exact schema is `00_project/content-pool-item.schema.json`. This file explains it.
Nothing is created in Supabase or Drive from this file. A portal table is a later option (see section 6).

## 1. What one pool item is

One item is one thing to put on the website, or one thing to decide about. It belongs to one of four pillars. It has a page tag, a score, proof and a status.
An agent can go from an item to its raw data. The field `evidence[].file` is a path inside the run folder. The field `evidence[].ref` is the key, keyword or URL inside that file.

## 2. Files of one run

```
00_project/assets/<slug>/content-pool/
  _status.md                 one line per step
  spend.jsonl                every paid call and its cost (cap check)
  01-client/                 client-baseline.md, client-form-<slug>-de.md
  02-competitors/            serp-N.json, metrics.json, site_urls.json, urls.txt
  03-demand/                 volume*.json, autocomplete.json, trends.json, ranked-<domain>.json
  04-pool/                   candidates.json (judgment), pool.json (built), summary.json (findings)
  05-report/                 content-pool-report.html, content-pool.xlsx
```

## 3. Fields of one item

| Field | Type | Meaning |
| --- | --- | --- |
| `id` | `CP-LOC/SVC/BRD/AUT-nnn` | Stable key. Never reused. |
| `pillar` | location, service, brand, authority | The four pillars. |
| `audience` | patient, trainee, both | Who the item serves. Needed when a client has two audiences. |
| `page_tag` | text | `homepage`, `service:<slug>`, `place:<slug>`, `authority-page`, `blog-faq`, `offsite`, `later`, `cut`. |
| `section_hint` | text or null | Homepage items only. One of the 10 CRO P0 rows. |
| `item_type` | block, faq, keyword-target, proof, entity-schema, link-target, page, cut-log | Kind of content. |
| `topic`, `question` | text | The item in short, and the searcher's own question. |
| `keywords[]` | list | `kw`, `scope` (local or national), `volume` (null = no data), `volume_source`, `volume_date`. |
| `service_ref` | key or null | The client service this item serves. |
| `fit`, `fit_reason` | 0 to 3, text | See section 4. |
| `adjacent`, `client_confirmation` | flags | Set for fit 1. The client must confirm. |
| `demand` | object | `volume_max`, `autocomplete_hits`, `paa_hits`, samples, `client_signal`, `trend_note`, `basis`, `date`. |
| `competitor` | object | `set`, `denominator`, `covering`, `share`, `covering_domains`, `table_stakes`, `note`. |
| `compliance` | object | `mode` (hwg, brao, none), `flag` (ok, review, block), `note`. |
| `conversion`, `effort` | 0 to 3, 1 to 3 | Judgment inputs for the score. |
| `score` | object | Five parts and `total`. All computed by `build_pool.py`. |
| `priority` | A, B, C, cut | From the total and the rules in section 4. |
| `status` | draft, needs_client, adjacent_review, approved, cut, done | Where the item is in the process. |
| `live_status`, `live_url` | present, weak, missing, n/a | Existing-site mode only. Auto check. A human confirms. |
| `needs_client[]` | list of text | One `[FEHLT]` fact per entry. Feeds the client form. |
| `decision_note`, `owner` | text, agent/martin/client | Why cut or flagged. Who acts next. |
| `evidence[]` | list | `type`, `file`, `ref`, `date`. At least one. |

## 4. Scoring (computed by script, never typed)

`total = 0.30 x demand + 0.25 x gap + 0.25 x fit + 0.15 x conversion + 0.05 x effort`. Each part is 0 to 100.

| Part | How it is computed |
| --- | --- |
| demand | The best of: volume score `100 x log10(v+1) / log10(1601)`; autocomplete (35, or 45 from 5 hits); People Also Ask (45, or 55 from 3 hits); client signal (60); client GSC queries (see R-S5); expectation (100 x share of competitors that have it). |
| gap | `100 x (1 - share)`. Share = competitors with the topic divided by readable competitors in the set. |
| fit | 0 = 0, 1 = 33, 2 = 67, 3 = 100. Set by judgment against the client's real services. |
| conversion | 0 to 3 mapped to 0, 33, 67, 100. Judgment: does the item help a visitor to contact the practice? |
| effort | 1 (text only) = 100, 2 = 67, 3 = 33. Higher means less work. |

Rules found in the dry run:

- R-S1 A keyword with no place name is national. Its volume score is multiplied by 0.6.
- R-S2 If 50 % or more of the set has the item, demand has a floor of 100 x share (table stakes).
- R-S3 A gap without demand is not an opportunity. If demand is under 30, the gap is halved.
- R-S5 Client GSC queries count as demand: 80 from 100 impressions, 70 from 30, 60 from 10, else 50. The queries are matched by patterns in `candidates.json` (`gsc_patterns`). Training queries must not count for patient items: use exclusion patterns.
- R-S6 If fewer than 5 items reach A, the best quarter of the live items (fit 2 or 3) with a total of 65 or more becomes A. Found in the law-firm run, where nearly every item is table stakes and scores cluster between 60 and 74. The Dumann pool is not affected (14 A).
- R-S4 Priority: A at 75 or more, B at 55 or more, else C. Table stakes never stay C. Fit 1 is never A. Fit 0 is cut. Compliance block is cut.

Fit scale:

| Fit | Meaning | Example (Dumann) |
| --- | --- | --- |
| 3 | The client offers exactly this. | Aderlass page. |
| 2 | Education, question or comparison around a real service. | Aderlass cost and duration questions. |
| 1 | Adjacent topic. The client must confirm. Martin decides. | Hildegard medicine by complaint. |
| 0 | The client does not offer it. Cut. | Colon-Hydro-Therapie (6,600 searches). |

## 5. How an agent drills down

1. Read `04-pool/pool.json`. Find the item by `id`.
2. For a number, open `evidence[].file` and look up `evidence[].ref`. Example: `03-demand/volume.json`, ref `aderlass berlin`.
3. For a competitor claim, read `competitor.covering_domains`. Open `02-competitors/metrics.json` (page measures) and `02-competitors/site_urls.json` (their sitemaps).
4. `scripts/validate_pool.py` checks that every volume in an item equals the raw file. A typed number that does not match fails the run.

## 6. Sitetree node (sitemap step)

Fields of one node in `05-sitetree/tree.json` (judgment) and `sitetree.json` (built): `id` (ST-nn), `parent`, `title`, `status` (Bleibt, Überarbeiten, Neu, Vorschlag), `origin` (bestand, kunde, programm, vorschlag), `module`, `job`, `path` (existing URL) or `slug` (new URL), `kind` (page, hub, system, group), `audience`, `kw`, `pool_tag` or `pool_items`, `needs_client[]`, `note`. The script adds GSC clicks and impressions, words today, the keyword volume, and the pool items with their priority. Rules S1 to S8 are in the spec, section 15.

## 7. Later options (not built, needs Martin's go)

- A Supabase table `content_pool_items` with the same fields, plus a Portal tab, so the client can confirm adjacent items.
- A `status` write-back from the copy step (`done` when the text exists).
- Rank tracking per item after launch.
