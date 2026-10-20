# Un-Burning spec — workflow `un-burning`

Status: DESIGN APPROVED by Martin at checkpoint 1 (2026-10-11). Spec, data model, prototype and skill draft exist. A read-only dry run on Praxis Suriya is done (`00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/`). Nothing is installed. No client asset was changed. Supabase and Drive writes and the skill install need Martin's final go.
Language: this file is STE. Field names are English. Board labels are German.
Companion files in `00_project/un-burning-workflow/`: `research-note.md`, `design-note.md`, `data-model.md`, `harm-register.schema.json`, `report-wireframe.md`, `report-prototype.html` (internal) and `report-prototype-client.html` (client-safe draft), `access-checklist-de.md`, `who-owns-what-template.md`, `scorecard.md`, `skill-draft/` (SKILL.md, scripts, references).
Board: `00_project/assets/un-burning-workflow/un-burning-board.png`.

## Contents

1. Goal and scope
2. Decisions from the grilling
3. Interface with the audit workflow
4. Modes and inputs
5. Phases and checkpoints
6. Runbooks B to E (area A is retired)
7. Approval rules
8. Snapshot, change log and rollback
9. Cost caps and tools
10. Hard rules
11. Outputs
12. Bedrock check (done criteria)
13. Success measures
14. Test scenarios
15. Open questions

---

## 1. Goal and scope

Goal: list everything that harms a client's online presence, then remove or repair it in a safe, controlled way. The end state is a stable "bedrock" before growth SEO starts.
Entities: website, Google Business Profile, listings and citations, social profiles, backlinks, reviews, search index.
Un-Burning removes **harm**. It does not add **gap** items. A harm exists and damages or blocks. A gap is missing and would add growth. Gaps stay in the audit and go to growth SEO.

**Ownership and access are not part of Un-Burning** (Martin, 2026-10-11). The client owns 100 percent of sites, profiles and content, and 741 acts as admin. That is settled with the client at the start, at onboarding (access checklist, contract wording). Un-Burning needs it as a precondition. A missing precondition never becomes a harm item, a light or a bedrock criterion. It only marks the affected actions `blocked` with the reason. Un-Burning does not repair ownership.
Client effort in Un-Burning: none beyond approvals. The onboarding access step (15 to 30 minutes in month 1) happens before.

Out of scope: page copywriting (`seo-page-optimizer`), CRO prototypes (`cro-homepage`), backlink building (`backlink-dach`), the diagnosis itself (audit workflow). Un-Burning uses their results. It does not replace them.

**One limit.** For suspended or ineligible Google profiles the workflow covers only the compliant route: a real business, a real eligible address, proper evidence and video verification of the real business. Address workarounds for ineligible addresses are out of scope. They risk a permanent suspension. Review removal uses only Google's report and appeal routes and, where it fits, a legal route. No fake counter-reviews.

## 2. Decisions from the grilling (Martin, 2026-10-11)

| # | Topic | Decision |
| --- | --- | --- |
| 1 | First client | Praxis Suriya (Ingelheim). Program client |
| 2 | What burned | Wrong NAP, spam listings, bad site and index. A former party held assets, but for Suriya all assets are with the owner |
| 3 | Area A (ownership, access) | RETIRED from Un-Burning (Martin, 2026-10-11). Solved at onboarding with the client. Un-Burning only reads it as a precondition |
| 4 | End result | Bedrock Pack: damage map, harm register, keep/fix/kill list, bedrock check (no who-owns-what matrix: that is onboarding) |
| 5 | First reader | Martin, then agents. The client sees a released client-safe tab later |
| 6 | Order | Public checks first (C, D, E). The access request runs in parallel |
| 7 | Phases | Four: scan, triage, execute, verify and report |
| 8 | Autonomy | Agents prepare alone. Every live change needs a go. Batch go per area. Per-item go for deletes, merges and review reports |
| 9 | Data store | JSON per run. Supabase later, after a go |
| 10 | Report | Internal HTML (page 1 = damage map) plus a client-safe portal tab as draft |
| 11 | Success measures | GBP calls, routes, site clicks. Indexed pages and 404 count. NAP consistency percent. Inquiries per week |
| 12 | Detection depth | Light: public data plus Search Console. No new Falcon scans |
| 13 | Backlink anchors | Opt-in flag `--with-backlinks`. Off by default |
| 14 | WordPress lane | All Un-Burning edits only through Martin's go. Martin tells Dinakar. Never menu 16, page 1511 or the forms |
| 15 | Baseline | Existing baselines (GSC and GBP 28.06.-23.09., Falcon grids 15-16.08.). Copied to `00_project/assets/un-burning/praxis-suriya/baseline/` |

## 3. Interface with the audit workflow

The audit (`00_project/audit-workflow-spec.md`) is the diagnosis step. Un-Burning is the repair step. An audit field becomes a harm-register row when its status is `yellow` or `red` **and** the finding is harm, not gap. Un-Burning adds item-level drill-down.

| Audit field | Area | Harm-register item |
| --- | --- | --- |
| B13.01 Duplikate und Doppel-Einträge | C | One row per duplicate profile or listing |
| B13.02 Adress- und Verifizierungsrisiko | C | Old address still live |
| B13.03 Name im Profil | C | GBP name differs from the legal name |
| B05.02 GBP-Anzahl und echte Adressen | C | Unknown or extra profile |
| B06.05 Live-NAP-Konsistenz | C | One row per source with a wrong NAP field |
| B07.02 Lokale PR und Citations | C | One row per inconsistent or spam citation |
| B07.03 Social-Media-Auftritt | C | Wrong handle or old data |
| B07.04 Anti-SEO und Negativ-PR-Suche | D | Negative page-1 result, 1-star burst |
| B13.07 Review-Richtlinien-Risiko | D | Suspect or fake review (report route only) |
| B13.05 Branchen-Werberecht | D | Banned claim on site or GBP |
| B06.03 Schnelle SEO-Fehler | D | One row per canonical, robots, redirect or sitemap error |
| B06.04 Qualität der Location-Seiten | D | Thin or duplicate location page |
| B07.01 Backlink-Audit | D | Spam link or wrong brand anchor (opt-in) |
| B06.06 Indexierung | E | One row per unintended-indexed or intended-missing URL |
| B06.08 Keyword-zu-Seite-Zuordnung | E | Page without a parent link |

Not mapped: B06.01 (Asset-Eigentümerschaft) and B13.06 (Profilstatus und Zugriff). Ownership and access belong to onboarding. Not mapped (stay in the audit): B05.01, B05.03 to B05.08, B10, B11, B12. These are gaps.
Mapping rule in the register: `source_field` holds the audit id. If Un-Burning finds an item itself, `source_field` is `null` and `check_id` holds the own check (`UB.D03`).
Without an audit run, Un-Burning runs the audit's own scripts for the mapped fields. It never writes separate logic for the same check.

## 4. Modes and inputs

| Mode | Start | Result |
| --- | --- | --- |
| `scan` (default) | `/un-burning <client>` | Phase 1 and 2 for a new client |
| `scan --from-audit <run>` | Audit run id | Reads audit `findings.json`, builds rows, drills down |
| `reverify` | `/un-burning <client> --reverify` | Phase 4 only: same checks, same parameters, delta against the last run |

Flags: `--with-backlinks` (anchor and spam-link check, about 0.03 USD per target), `--areas C,D,E` (limit areas).
Inputs Martin gives: client name, domain, GBP name or place id, known history (what burned, since when), and the locked NAP master record (or `client_locations` row). If an input is missing, the skill asks once in one line.
Nothing runs on a client asset in `scan` mode. `scan` only reads.

## 5. Phases and checkpoints

```
Phase 1  SCAN       agents alone, read only
Phase 2  TRIAGE     reviewer subagent, report, GO-1
Phase 3  EXECUTE    per wave: plan, validate, snapshot, GO-2, apply, verify
Phase 4  VERIFY     re-scan, before/after, bedrock check, client tab, GO-3
```

| ID | When | What Martin sees | Choices |
| --- | --- | --- | --- |
| GO-1 (kill list) | End of phase 2 | Report page 1, area tables, the keep/fix/kill list with evidence | Per row: keep / fix / kill / hold. Or approve a whole class (reversible items only) |
| GO-2 (wave) | Before each wave goes live | `changes.json` of the wave: exact changes, pages named, snapshot ids, rollback steps | go / edit / stop. One go covers only that wave |
| GO-3 (release) | End of phase 4 | Client-safe tab as draft, client message draft in "ich" form, Drive link | release / hold |

Between checkpoints agents run alone. A scan never changes an asset. An execution never starts without GO-2. One go never covers the next change (memory `no-website-changes-without-go`).

Phase 1 steps:
1. Intake and master record. Check that `nap-master.json` exists and is locked.
2. Preconditions check (read only). Is the NAP master locked? Which access exists (Joomla role, Search Console, GBP role, logins)? Write the result to `preconditions.json`. Missing access marks the affected items `blocked` with the reason. It creates no item. Never fix or chase ownership here.
3. Areas C, D, E (and B only if a profile problem is known). They run as read-only subagents in parallel (patterns.md 4.7). Maximum 4 agents.
4. Write `harm-register.json`, evidence and manifest. Run `validate_run.py`. Fix until it passes.

Phase 2 steps:
1. A fresh reviewer subagent checks every proposed kill against its evidence. It reports only correctness gaps (a kill without proof, a delete without a redirect, a page with clicks or backlinks).
2. Build the report. Build `changes.json` drafts per wave.
3. Present at GO-1.

Phase 3 steps (per wave):
1. Write `changes.json` for the wave. Run `validate_changes.py` (every row has approval, snapshot, rollback and verify check).
2. Take the snapshots. Show at GO-2.
3. Apply. Append to `change-log.jsonl`.
4. Verify each item live. Save `after`. Fix until it passes or roll back.

Wave order: 1 reversible and low risk (NAP text, internal links). 2 redirects. 3 content fixes (merge, rewrite, noindex). 4 deletes and review reports, each with its own go.

Phase 4 steps:
1. Re-scan with the same parameters. Compute the delta and the bedrock check.
2. Build the before/after tracker with the baseline metrics.
3. Build the client-safe tab (draft) and the client message. Present at GO-3.

## 6. Runbooks B to E (area A is retired)

Each runbook has: detection, evidence, decision rule, action, verification. Check ids are stable. "Light" detection uses public data and Search Console only.

### Area A — retired (preconditions, not an area)

The board group "Rückholung aller digitalen Vermögenswerte" (domain, website, Google profile ownership, analytics and tracking) and "Volle Eigentums-Garantie" are onboarding work with the client, not Un-Burning (Martin, 2026-10-11). The letter A stays reserved so IDs stay stable. Un-Burning checks only these preconditions and records them in `preconditions.json`:

| Precondition | Why Un-Burning needs it | If missing |
| --- | --- | --- |
| NAP master record locked | Every NAP fix compares against it | Stop and ask once. Do not scan against a guess |
| Access to change the asset (CMS role, listing logins, GBP role, Search Console) | To execute an approved fix | Mark the action `blocked` with the reason. Never an item, never a light |
| Client approval route | For per-item go on owned assets | Martin asks the client through the usual channel |

### Area B — Rettung gesperrter Profile (compliant route only)

| Check | Detection | Evidence | Decision rule | Action | Verification |
| --- | --- | --- | --- | --- | --- |
| UB.B01 Profile status | Maps read: open, suspended, duplicate, unverified | Screenshot, date | Suspended or unverified: `blocks_revenue` | Prepare the reinstatement case: proof of real business, real eligible address, signage and licence photos | Profile shows live and verified |
| UB.B02 Dormant old profiles | Search by old name and old address | Search result, screenshot | Own old profile found: `claim` and merge or `report` as duplicate | Claim through Google's own flow | Single profile remains |
| UB.B03 Video verification | Checklist: SOP for the video (location, signage, tools, proof of the business) | SOP checklist, video file kept by the client | Only the real business at the real address | Client films. 741 guides. Submit through Google | Verification status = verified |

Out of scope: any workaround for an address that is no longer eligible (stated in section 1). For Suriya, area B starts only if UB.B01 finds a problem.

### Area C — Identität und NAP

| Check | Detection | Evidence | Decision rule | Action | Verification |
| --- | --- | --- | --- | --- | --- |
| UB.C01 Master record | `client_locations` plus client confirmation. Locked date | JSON | Locked and confirmed by the client: ok. Missing: stop and ask | Create or lock the record (Martin's go) | Record has `locked_at` |
| UB.C02 Site NAP | Impressum, contact, footer, JSON-LD on sample pages | HTML snapshots | Any difference to the master: `blocks_revenue` for phone and address, `cosmetic` for spelling | `fix` (needs GO-2, page-swap rules) | Re-crawl shows the master value |
| UB.C03 GBP NAP | Falcon read or Maps read | Report key, screenshot | Name with extra words, wrong address or phone: `blocks_revenue` | `fix` in GBP with the client's owner role | Re-read |
| UB.C04 Citation NAP | `client_citations` plus live fetch of listing URLs. Character-exact compare | Page text, hash | Per listing: match or mismatch per field | `fix` (self, BrightLocal or client login). Row in `nap-corrections.json` | Re-fetch shows the master value. NAP percent updated |
| UB.C05 Spam and irrelevant listings | Search name, phone, old address | Result list | Wrong data and no claim route: `delete` or `report`. Wrong data with a claim route: `claim` and `fix` | Claim first. Delete only if the correction route fails. Each delete = per-item go | Listing gone or corrected |
| UB.C06 Social | Profile pages, handle, bio data | Screenshot | Old name, address or phone | `fix` | Re-read |
| UB.C07 Dead numbers | Search the old and tracking numbers | Result list | A dead number on a live listing: `blocks_revenue` | `fix` | Re-fetch |

Core and granular citations: the Citations module (44 DACH directories, `directories`, `client_citations`) is the source. Un-Burning only repairs wrong or spam entries. Building new citations is growth work.
Character-exact rule: compare byte by byte after trimming. Show "Str." and "Straße" as a difference. The master decides the form.

### Area D — Schadensbehebung (Damage Control)

| Check | Detection | Evidence | Decision rule | Action | Verification |
| --- | --- | --- | --- | --- | --- |
| UB.D01 404 inventory | Crawl, GSC, backlink list (if `--with-backlinks`) | URL list with status | A 404 with clicks or backlinks: `leaks_link_power`. Map to the best live target | `redirect` 301 (no chains) | Request returns 301 then 200 |
| UB.D02 Redirect errors | Chain length, loops, 302 where 301 is right | Header trace | Chain over 1 hop or a loop | `fix` rule | Single hop |
| UB.D03 Duplicate content | Exact hash and shingle similarity over 80 percent | Pair list with score | Keep the page with clicks, backlinks or better position. The other gets `merge` and 301 | `merge` | Canonical target indexed. Old URL returns 301 |
| UB.D04 AI-slop | Repeated boilerplate, generic text, low unique value. Heuristic. Human review always | Page excerpt, score | Never auto-judged. Martin decides | `fix` (rewrite with real local value) or `merge` | Re-review |
| UB.D05 Thin content | Word count and unique value against page type | Count, excerpt | A thin intended service or location page: `fix` with real content. A thin unintended page: `merge` or noindex | `fix` content request with source from the client | Page passes the content standard (`startseite-money-page-standard.md`) |
| UB.D06 Orphans | Crawl graph: no content link to the page | Graph export | Page with clicks or backlinks: `fix` (add parent link). Page without value: `merge`, 301 or noindex | `fix` or `redirect` | Page has at least one content link from its parent |
| UB.D07 Canonical, noindex, robots | Header and head parse | HTML | Intended page with noindex or a wrong canonical: `blocks_revenue` | `fix` | Re-crawl |
| UB.D08 Negative PR | Brand SERP and autocomplete | Screenshot, query | A negative page-1 result: see decision tree below | Displace with own content (growth work after bedrock), `report` if it breaks a platform rule | SERP re-read |
| UB.D09 Suspect reviews | Objective signals: 1-star burst, same-day cluster, reviewer without other history, text unrelated to the business. Falcon read plus Maps read | Screenshots, dates | Meets a Google policy case: `report`. Otherwise `keep` | `report` through Google's tool and, if needed, the appeal. Legal route is Martin's decision | Review gone or the report is logged |
| UB.D10 Backlink anchors (opt-in) | `--with-backlinks`: referring domains, anchors, spam signals | API JSON | Spam link or wrong brand anchor: `leaks_link_power` | Disavow candidates go to Martin. Outreach through `backlink-dach` | Re-pull |
| UB.D11 Advertising law | Text scan (health: HWG) | Hit list with context | A banned claim: `blocks_revenue`. Human review always | `fix` with the client's text | Re-scan |

Decision tree for a page (D01, D03, D05, D06):
1. Has the page clicks (GSC 90 days) or backlinks? Yes: never delete. Choose `keep`, `fix`, or `merge` with a 301.
2. Is it a duplicate of a stronger page? Yes: `merge` into the stronger page, 301.
3. Is it intended (money, service, location) and thin? Yes: `fix` with real content.
4. Has it no value, no links and no clicks? `merge` or noindex first. `delete` last, with 301 or 410 and a per-item go.

Review rule: 741 does not answer reviews. The client answers (memory `no-review-answering`). Health clients: no patient data and no case details in any report or reply.
Negative PR rule: report only content that breaks a platform rule. Do not attack legal opinions. Displacing through new content is growth work and starts after the bedrock check.

### Area E — Indexierung und Crawl-Pfad

| Check | Detection | Evidence | Decision rule | Action | Verification |
| --- | --- | --- | --- | --- | --- |
| UB.E01 Index state | GSC coverage export. URL Inspection API (test on first use) | JSON | Per URL: indexed, not indexed with reason | Document | Re-pull |
| UB.E02 Indexed vs intended | Join sitemap, crawl and GSC. Classify each URL (money, service, location, blog, system, archive) | `index-intended.json` | Intended and not indexed: `index_missing`. Unintended and indexed: `index_unwanted` | `fix` (internal links, content, request indexing) or noindex and remove from sitemap | Re-pull after 2 to 4 weeks |
| UB.E03 Sitemap hygiene | Sitemap lists only intended, 200, canonical URLs | Sitemap file | Any other URL in the sitemap: `leaks_link_power` | `fix` the sitemap source | Sitemap re-read |
| UB.E04 Inverted tree | Link graph: each page has at least one content link up to its parent service page. Each service page links to home. Click depth at most 3 | `link-plan.json` | A page without an up-link: `fix` | Add contextual links (menu and footer links do not count) | Graph re-computed |
| UB.E05 Crawl waste | Archives, tags, authors, sidebars with 50+ links, parameters | Crawl stats | Waste URL in the index or heavy sidebar: `leaks_link_power` | noindex, remove sidebar links (GO-2) | Re-crawl |

Intended rule: homepage, core service pages and location pages with real local value are intended. Blog posts are intended only if they link to a service page and have clicks or a clear keyword role. Archive, tag, author, login, search and system pages are unintended.
Request indexing through GSC only after fixes, and only for intended URLs. Submission is logged.

## 7. Approval rules

| Class | Examples | Agent may | Needs |
| --- | --- | --- | --- |
| Read | Crawl, GSC read, public search, Falcon read, report build | Do alone | Nothing |
| Prepare | Redirect map draft, NAP corrections, `changes.json`, client message draft | Do alone | Nothing (drafts only) |
| Reversible live change | NAP text on a listing, internal link, redirect rule, noindex flag | Apply after the wave go | GO-2 per wave. Snapshot first |
| Destructive | Delete page or listing, merge of live pages, review report, disavow | Apply after the item go | Per-item go. Snapshot first |
| Client contact | Any mail or message | Draft only | Martin's go. Mail only through Airmailer |

Suriya rules (memory): official name "Praxis Suriya", only address Schützenpfad 29, phone 0174 7411087. Page 1511 on `/ayurveda-therapie/` stays untouched. Forms, phone and hours stay 1:1. No menu change without a go. No live edit of a page: build new, set old offline, take the slug. Export postmeta before any change.

## 8. Snapshot, change log and rollback

- Every target gets a snapshot before the change (see `data-model.md` section 6).
- `changes.json` rows need `snapshot_id`, `rollback` and `verify_check`. `validate_changes.py` blocks the wave if one is missing.
- `change-log.jsonl` is append only. It lists who approved what and when.
- If a verify check fails twice, roll back that item and mark it `blocked` with the reason.
- After every content change, check that images and forms still work (lesson of 2026-10-07).
- Rollback is a stated step per item. "Restore from the snapshot" alone is not enough.

## 9. Cost caps and tools

| Item | Light default | Cap |
| --- | --- | --- |
| DataForSEO | 0 (free autocomplete only) | 1 EUR. `--with-backlinks`: about 0.03 USD per target, cap 0.5 EUR |
| Local Falcon | Reads only | No new scan. Any scan needs Martin's go and counts against the 800-credit rule of the audit |
| Firecrawl | Listing and SERP pages | 300 pages per run |
| GSC URL Inspection | Priority URLs | 100 per run (to test on first use) |
| Chrome (read only) | Only for A and B browser reads | Granted access only |

`cost_ledger.jsonl` logs every paid call. The script stops at the cap. Spend above the cap needs a go.
Tools that work (from memory): DataForSEO, Local Falcon through MCP only, the live-site script, Google reporting through the service account, Claude in Chrome. Ahrefs is not usable.

## 10. Hard rules

1. Scan mode changes nothing on client assets. Every change needs a go as set in section 5 and 7.
2. Every item has source, date, confidence and evidence. Allowed confidence: `verified`, `derived`, `client_stated`. A guess has no place. An unreadable source is "unreadable", never "nothing found".
3. Never guess addresses or dates.
4. No tool names and no team names on client-facing pages. The client reads "Google-Daten" and "Bereinigung".
5. German clients: "du". Health clients: HWG check on every text. No promise of success or cure.
6. Nothing is deleted without a snapshot and a rollback step. A page with clicks or backlinks is never deleted without a 301.
7. Suspended or ineligible profiles: compliant route only (section 1). Review removal: Google routes and a legal route only.
8. Client mail only through Airmailer and never without Martin's go. Drafts are full texts, in "ich" form, with no call offers and no booking link.
9. Replies in STE. Client text in normal German prose.
10. Every delivery ends with the Drive link and a screenshot as a file. Every UI is checked in rendered state with a screenshot.
11. Supporting working files go to the client's Drive folder, subfolder `_UnBurning-Hilfsdaten`. They are not client deliverables.
12. Internal methods are not named in client material. Use "741-Bereinigung" or "741-Fundament-Check".

## 11. Outputs

Per run in `00_project/assets/un-burning/<client-slug>/<YYYY-MM-DD>-<mode>/`. See `data-model.md` section 2.
Delivery: internal HTML report, client-safe tab (draft), client message draft, Drive link, screenshot.
Memory file `un-burning-workflow.md` plus a line in `MEMORY.md` (after the final go).

## 12. Bedrock check (done criteria)

Area light (computed by `bedrock.py`):

| Light | Rule |
| --- | --- |
| Green | No open `blocks_revenue` item. At most 10 percent of `leaks_link_power` items open |
| Yellow | No open `blocks_revenue`, but more than 10 percent of `leaks_link_power` open |
| Red | At least one open `blocks_revenue` item |
| Grey | Area not applicable or not scanned |

The client is ready for growth SEO when C, D and E are green and no area is red (B is grey when not scanned).
For Suriya, "done" means: NAP identical on site, GBP and listings (NAP percent at target); no unintended page indexed; no intended page missing from the index; 404s with clicks or backlinks redirected; orphans fixed; every page has an up-link.

## 13. Success measures

| Measure | Baseline (Suriya) | Source |
| --- | --- | --- |
| GBP calls, routes, site clicks | 6 calls, 118 routes, 93 site clicks, 28.06.-23.09. (88 days) | `baseline/2026-10-01-gbp-performance.json` |
| Indexed pages | 39 indexed, 43 not indexed (report of 21.09.) | `baseline/BASELINE-REPORT.md` section 10 |
| 404 count | From the first crawl | `index-intended.json`, `redirect-map.json` |
| NAP consistency percent | From the first scan | `nap-corrections.json` |
| Inquiries per week | About 2 per week (Coralie). Count from form plus phone log | Form and client log |
| Quality of the workflow | Under 3 corrections by Martin at GO-1. 0 unsourced items | `validate_run.py` |

Effect is shown only against the baseline, with the same parameters. Visits and rankings can move for other reasons. The report says so in one line.

## 14. Test scenarios (written before the body)

| # | Input | Expected |
| --- | --- | --- |
| T1 obvious | "Starte Un-Burning für Praxis Suriya" | Skill loads. Asks only for missing intake. Starts phase 1 read only |
| T2 paraphrase | "Räum bei Suriya alles auf: falsche Adressen, kaputte Links, Spam-Einträge" | Skill loads. Same result as T1 |
| T3 must not trigger | "Mach ein Maps-Audit für Stürzl" | Audit skill runs. Un-Burning does not load |
| T4 must not trigger | "Schreib die Migräne-Seite für Suriya neu" | `seo-page-optimizer` runs. Un-Burning does not load |
| T5 gate | "Lösch alle Altseiten bei Suriya sofort" | The skill refuses the live change. It shows the kill list and asks for GO-1 |

Functional test: the read-only dry run on Praxis Suriya (folder `00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/`).

## 14b. Dry-run lessons (Suriya and Stürzl, 2026-10-11)

1. Set `params.scanned_areas` in every run. An unverified area must be grey, never green.
2. The client view shows only items with a reviewed `client_text`. Raw item text leaks internal names.
3. `index-intended.json` verdicts also allow `review`, `unverified` and `decision_needed`.
4. `run.json` holds `sources_unreadable`. The report prints them on page 1 under "Datenlage".
5. The validator is the gate. It caught a broken evidence link that the scan agent missed.
6. Access gaps of 741 are dependencies, not harm: rate them `cosmetic` and mark them blocked (data model, section 4). The Stürzl scan first rated "741 is not Super User" as `blocks_revenue`. Martin caught it.
7. Local Falcon MCP must be connected in the session that runs the scan. If it is not, the GBP profile is "unreadable".

## 15. Open questions

1. Baseline files exist now in `00_project/assets/un-burning/praxis-suriya/baseline/`. The originals stay in worktree `admiring-nightingale-f0f882`. Martin decides when they move to the canonical path `assets/suriya/baseline/`.
2. GBP manager list, GA4 roles and GSC owners need a browser read. When should Martin or Coralie confirm them?
3. Inquiries per week has no clean source. Proposal: Coralie keeps a simple count (form plus phone) until tracking exists.
4. Contract wording for "client owns 100 percent" is for Martin or his lawyer. Where should the checklist link to it?
5. Supabase tables (`ub_*`): approve after the dry run? Not before.

## Registry entry (2026-10-11)

Every run of this workflow is recorded in the workflow registry. The Excel `~/Desktop/Workflow-Uebersicht.xlsx` shows per client whether the workflow ran, its state, the last run, Martin's approval and the folder links.
- At the start or end of a run: `python3 /Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py upsert --client "<client>" --workflow unburning --status "in Arbeit|Trockenlauf|fertig, Freigabe offen" --local <folder> --drive <url> --result <file>`
- When Martin approves the result: `python3 /Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py approve --client "<client>" --workflow unburning` in the same turn, then tell Martin the sheet was updated. A hook reminds Claude when a message sounds like an approval.
Workflow id: `unburning` (Un-Burning).

## Registry: automatic (2026-10-11)

The overview Excel `~/Desktop/Workflow-Uebersicht.xlsx` updates itself. A Stop hook runs `workflow_registry.py sync --quiet` after every turn. You do not call `upsert` for normal progress. Keep `<run>/run.json` current: field `client`, field `mode` (`dryrun` or `live`) and field `finished_at` when the run ends. `sync` reads them. A dry run stays Trockenlauf. A real run with `finished_at` becomes fertig, Freigabe offen.
For any other file layout, write `_run.json` in the run folder (schema in `00_project/workflow-registry/README.md`). Only the approval stays manual: when Martin approves a result, run `approve` in the same turn and say that the Excel is updated.

## Martin guide (2026-10-12)

The 741 character Martin points out the one thing per section the reader must not miss. Rules, poses, markup and the inline helper: `00_project/assets/brand/martin-guide/README.md`. In this workflow: in the client report: point at the biggest leak, insight at the first fix, celebrate when an area turns green. Max 1 callout per section, bubble text in first person and plain language, every number with source and date, check desktop and mobile with a screenshot.
