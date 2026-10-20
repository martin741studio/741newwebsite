# Audit spec — Maps-Readiness-Audit (workflow `maps-audit`)

Status: DESIGN APPROVED by Martin at checkpoint 1 (2026-10-11), with all proposed defaults in section 12. Nothing is built or installed. Tables need a separate go.
Language: this file is STE. Field labels are German, as on Martin's board. Field keys and metadata names are English.
Companion files in `00_project/audit-workflow/`: `research-note.md`, `design-note.md` (use cases, pipeline, tests), `data-model.md` + `schema.draft.sql`, `report-wireframe.md`, `interview-form-de.md`.

## Contents

1. Goal and scope
2. Decisions from the grilling
3. Modes and depth
4. Input types and tools
5. Scoring and verdict
6. Field catalog (13 blocks)
7. Cost and caps
8. Checkpoints
9. Hard rules
10. Outputs
11. Success measures
12. Open questions

---

## 1. Goal and scope

Goal: show, with real data, what stops a client from ranking #1 on Google Maps, and what to do first.
The audit **collects only**. It changes nothing on client assets (website, GBP, Ads, directories).
It covers the board "2 Das Audit" (9 blocks) plus 4 new blocks. It serves three situations: pre-sale call, program kickoff, re-audit.
Out of scope: page copywriting (skill `seo-page-optimizer`), prospect review page (skill `local-seo-review-page`), backlink outreach (skill `backlink-dach`), CRO prototype (skill `cro-homepage`). The audit feeds them. It does not replace them.

## 2. Decisions from the grilling (Martin, 2026-10-11)

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Funnel position | All three modes: call, kickoff, re-audit |
| 2 | Readers | Martin, agents, team (Dinakar, Tantri). The client reads only a released client-safe tab |
| 3 | Client types | Health (HWG), other local services, multi-location. Test client: Stürzl |
| 4 | Database | Supabase 741-portal tables are the master. JSON export per run. The Requirement Sheet (tab `02 Audit`) is a generated view |
| 5 | New blocks | Add all four: GBP quality depth, competitor benchmark, AI answers + Apple Maps, suspension and duplicate risk |
| 6 | Client answers | Portal form only (blocks 1-4, 8, 9). No interview call |
| 7 | Score | Traffic light per block + one 0-100 Maps-Readiness score. Fit check separate: Yes / Not yet / No |
| 8 | Report | Internal HTML page + client-safe portal tab (draft first) |
| 9 | Depth | Deep default: 5 keywords, 5 competitors, all platforms, DataForSEO cap 8 EUR. Falcon cap 800 credits, ask before more |
| 10 | Start | Slash command. Agents run alone until the first checkpoint. Falcon scans start only after Martin's go |
| 11 | Modes | Call: blocks 1-5, 9 + data blocks, light. Kickoff: all. Re-audit: data blocks + changed answers |
| 12 | Fit check | Only "#1 is unrealistic in the market" changes the verdict. Capacity, ROI, compliance and asset flags show as red flags on page 1 |
| 13 | Block 6 | Agent checks only. No screen-share call. Unprovable ownership stays "unconfirmed" |
| 14 | Sharing | Never automatic. Portal tab is a draft. Martin releases it with a go |
| 15 | Language | German labels and findings. English field names and metadata |
| 16 | Success | Under 3 corrections per audit. Every claim has a source link and a date |

Assumption to confirm: "Deep" is the default for kickoff and re-audit. Mode "call" uses the light profile (section 3). Martin can override with a flag.

## 3. Modes and depth

| Mode | Blocks | Client form | Falcon | DataForSEO cap | Competitors |
| --- | --- | --- | --- | --- | --- |
| `call` | B01-B05, B09, B10-B13 light, B06 and B07 light | Short set (B01, B03, B09 minimum) | 1 keyword, Google only, 7x7 (49 credits) + free reads | 1 EUR | 2 |
| `kickoff` | all 13 | Full | 5 keywords, all platforms + Apple, 7x7 (about 700 credits, cap 800) | 8 EUR | 5 |
| `reaudit` | B05, B06, B07, B10-B13 + changed answers | Only changed or stale answers (older than 90 days) | Same keywords, same grid, same radius as the last run | 8 EUR | Same 5 as last run |

"Light" means: only fields marked `L` in the catalog run.
Keyword rule: 5 keywords. Max 3 have priority 1. Keywords come from services (keyword must match the service). Volume 0 means no data, not no demand.
Falcon default grid: 7x7, radius 5 km. The run stores grid and radius. A re-audit with other values is marked "not comparable".

## 4. Input types and tools

| Code | Meaning |
| --- | --- |
| C | Client answers in the portal form |
| A | Agent pulls the data with a tool |
| B | Agent reads in a browser with granted access (Chrome, as `741studio18`). Read only |
| D | Derived: a script computes it from other fields |
| M | Martin decides or types it |

| Tool | Used for | Status | Cost |
| --- | --- | --- | --- |
| Local Falcon via MCP `mcp.localfalcon.com` | GBP basics, categories, reviews, competitor sets, scans, AI scans, Apple scan | Verified (playbook, Stürzl) | Reads free. 49 credits per 7x7 Google scan. Never retry a scan |
| DataForSEO (`.secrets/dataforseo.env`) | Search volume, backlinks summary (one target per call), Labs ranked keywords | Verified | About 0.09 USD per 25 keywords. About 0.024 USD per backlink target |
| DataForSEO Business Data and Maps SERP | GBP photos, posts, Q&A, review timeline | **To test in dry run** | Unknown. Test with one call first |
| Live-site script (free) | Title, meta, H1, JSON-LD, GA4/GTM, canonical, OG, alt, NAP from Impressum | Verified | Free |
| Google reporting service account | GA4 and Search Console read | Verified for granted properties | Free |
| GSC URL Inspection API | Index state per URL | **To test** | Free |
| PageSpeed Insights API | Core Web Vitals | **To test** | Free |
| Google Autocomplete | Keyword check, brand queries | Verified | Free |
| Firecrawl search and scrape | Competitor sites, social profiles, directory pages, brand SERP | Available | Per plan |
| Supabase 741-portal | `client_citations`, `client_locations`, `access_grants`, master data | Verified | Free |
| Chrome (Claude in Chrome) | GBP insights, Ads account, Maps listing view, screenshots | Per memory: external Chrome only | Free |
| Ahrefs | — | NOT usable (plan) | — |

## 5. Scoring and verdict

### 5.1 Field status

Each field gets one status: `green` (1.0), `yellow` (0.5), `red` (0), `grey` (not applicable), `unknown` (no data yet).
Grey and unknown fields leave the score. They lower the **coverage**.
Rule type: relative beats absolute. Measure against the market leader and the blueprint, not against a fixed number from nowhere.

### 5.2 Maps-Readiness score (0-100)

Only data blocks count. Business-fit blocks (B01-B03, B08, B09) do not enter the score.

| Block | Weight |
| --- | --- |
| B05 Google-Profil & lokale Rankings | 25 |
| B10 GBP-Qualität | 15 |
| B11 Wettbewerber-Benchmark | 15 |
| B06 Live-Technik | 15 |
| B07 Off-Page, PR & Reputation | 10 |
| B13 Risiko | 10 |
| B12 KI-Sichtbarkeit & Apple Maps | 5 |
| B04 Geografischer Fokus | 5 |

Block score = weighted mean of its fields. Default field weight 1. Critical fields weight 3 (marked `!`).
Total = sum(block weight x block score) over blocks with coverage of at least 70 %. Re-scale to 100 over the counted blocks.
Report always shows **score and coverage** ("42 von 100, Datenlage 86 %"). A block under 70 % coverage shows "unvollständig" and is not counted.
Cap: one critical B13 finding (suspension, duplicate profile, wrong address) caps the total at 50.

Block light: green at 0.75 or more, yellow at 0.40-0.74, red below 0.40.

### 5.2b Strategy profile (added 2026-10-11, Martin: "741 is more get traffic via ads, less SEO")

The intake asks one question first: **How does the client get traffic?** `maps` (local SEO and Maps first), `paid` (ads first) or `balanced`. The slash command takes `--strategy maps|paid|balanced`. The answer sets the block weights and the meaning of some findings. It is stored in `run.json` (`params.strategy`).

| Block | `maps` | `paid` |
| --- | --- | --- |
| B05 Google-Profil und Rankings (incl. Ads audit B05.07) | 25 | 20 |
| B06 Live-Technik (landing page, tracking) | 15 | 30 |
| B03 Lead-Volumen und Abschlussquoten | 0 | 10 |
| B04 Geografischer Fokus | 5 | 10 |
| B10 GBP-Qualität | 15 | 5 |
| B11 Wettbewerber | 15 | 5 |
| B07 Off-Page | 10 | 5 |
| B13 Risiko | 10 | 10 |
| B12 KI und Apple | 5 | 5 |

Rules for `paid`: a `noindex` on an ads landing page is intended, not an error (note it, do not score it red). Missing organic rank is not a finding by itself. Tracking (key events, internal traffic, one canonical GA4 property), paid sessions in GA4, landing-page conversion and the proof behind the promises count most. Action ranking puts those first. `balanced` uses the `maps` weights.

### 5.3 Fit check (separate from the score)

Verdict values: `Ja` / `Noch nicht` / `Nein`. Display `Offen` (grey) when inputs are missing. `Offen` is not a fourth result.

**Design change D1 (2026-10-11, found in the Stürzl dry run).** The first rule used only the review gap to the leader (2 x leader reviews - own reviews, divided by a monthly velocity). The Stürzl data showed this rule is wrong for some markets. In 11 Falcon reports of the Stürzl market the review count did not explain visibility (Spearman rho between -0.16 and +0.26, below the 0.30 limit). Review data coverage is 82 to 96 % after the best count per profile is merged across all reports (a first version showed profiles with 0 reviews in the lead; that was missing Falcon data, see section 13). Profiles with only 13 to 32 reviews led (Pohl 13, Tikbas 32). Profile categories explained it better: in 9 of 11 reports a top-10 profile was 2 to 5 times more likely to hold "Tax attorney" or "Criminal justice attorney" than an average profile. The two broad keywords ("strafverteidiger", "anwalt wirtschaftsstrafrecht") showed no lift. So the audit first finds the **driver**, then judges what the client can change.

Per priority-1 keyword, script `score.py` reads `drivers.json` (script `analyze_drivers.py`, computed from the full Falcon report, free):

| Driver test | Meaning |
| --- | --- |
| `rho_reviews` (Spearman, reviews against SoLV, only if 50 % or more of the profiles have review data) | Reviews are a driver if rho is 0.30 or higher |
| `category lift` (share of top-10 profiles holding a category / share in all profiles; a category must exist on at least 5 profiles and in at least 30 % of the top 10) | A category is a driver if lift is 2.0 or higher. Only categories that fit the client's real services count (`params.relevant_categories` in `run.json`) |

| Result per keyword | Rule (proposal) |
| --- | --- |
| realistic | A controllable driver gap exists and the fix has effort S or M: a missing driver category, a missing service, a missing page. Or reviews are a driver and the gap closes in 9 months or less at the stated velocity (`velocity` = form answer, default 4 per month, flagged yellow) |
| slow | Reviews are the main driver and the gap needs 9 to 18 months |
| unrealistic | Reviews are the main driver and the gap needs more than 18 months with no other controllable gap. Or no controllable driver exists |

`review_gap = 2 x leader_reviews - own_reviews` and `months = review_gap / velocity` stay as facts in B11.03. B11.03 turns yellow (not red) when reviews are not a driver.
Verdict from the priority-1 keywords: `Ja` if at least half are realistic. `Nein` if all are unrealistic. Else `Noch nicht`.
The verdict text names the keyword, the driver, the client gap and the effort. One sentence. It states the limit: a category lift shows a link in the data, not proof of cause.

Red flags on page 1 (do not change the verdict): capacity (B09.01), ROI (B03.03), compliance (B13.05), asset access (B06.01), call handling (B09.03), suspension risk (B13).

## 6. Field catalog

Columns: `ID` | Feld | Type | Source and tool | Rule (status proposal). `L` = runs in light mode. `!` = critical. Rules are proposals. Martin edits them at checkpoint 1.
Every field stores: value, status, finding sentence, evidence id, source, date, confidence (data model, section 3).

### B01 Leadgenerierung & Marketing-Historie (business fit, no score)

| ID | Feld | Type | Source | Rule |
| --- | --- | --- | --- | --- |
| B01.01 L | Aktuelle Lead-Kanäle | C + A | Form (channel list, share %). GA4 channel split via service account as cross-check | red if stated and GA4 differ by over 25 points |
| B01.02 | Bisherige Marketing-Performance | C + A | Form (past agencies, spend, result). GA4 and GSC 12-month trend | grey if no data. Else trend arrow only |
| B01.03 L | Aktuelles SEO-Setup | A + C | Live-site script (CMS, plugins, GTM/GA4). GSC access. Form (who runs it) | yellow if GSC or GA4 missing |
| B01.04 | Alternativplan | C | Form | text only |
| B01.05 L | Grund für diesen Call | C | Form | text only. Shown on page 1 as one line |

### B02 Profitabilität & Ticket-Größen (business fit, no score)

| ID | Feld | Type | Source | Rule |
| --- | --- | --- | --- | --- |
| B02.01 | Profitabelste Leistungen | C | Form (top 5, ranked) | text |
| B02.02 | Durchschnittliche Ticket-Größe | C | Form (EUR) | text |
| B02.03 | Leistungen mit höchster Marge | C | Form (top 3) | text |
| B02.04 | Customer Lifetime Value | C | Form (EUR or repeat count) | text |
| B02.05 ! | Margen-Leistung sichtbar? | D | B02.03 against B10.02 (GBP services), B06.08 (pages), B05.06 (keywords) | red if a top-margin service has no GBP service, no page and no keyword |

### B03 Lead-Volumen & Abschlussquoten (business fit, no score)

| ID | Feld | Type | Source | Rule |
| --- | --- | --- | --- | --- |
| B03.01 L | Monatliches Lead-Volumen | C | Form (total and per channel) | text |
| B03.02 | Abschlussquote je Kanal | C | Form | text |
| B03.03 ! | ROI-Tragfähigkeit | D | Break-even = program fee / average ticket (or CLV). Compare with current leads per month. No forecast | red if break-even needs more new clients per month than current total leads x closing rate |

### B04 Geografischer Fokus & CRM-Daten (score weight 5)

| ID | Feld | Type | Source | Rule |
| --- | --- | --- | --- | --- |
| B04.01 | Ziel-Stadtteile und Einzugsgebiete | C + A | Form (list). Agent maps them to the Falcon grid and to GSC queries | green if all target areas lie inside the scanned grid. Else yellow or red by share |
| B04.02 | CRM-Datenauswertung | C + A | Form upload (anonymized export: postcode, service, date, source). Script summarizes | grey if no upload. Else text and top 5 postcodes |
| B04.03 | Expansionsabsicht | C | Form (new location, new service, 12 months) | text. A new location sets a flag for B13.01 |

### B05 Google-Profil & lokale Rankings (score weight 25)

| ID | Feld | Type | Source | Rule |
| --- | --- | --- | --- | --- |
| B05.01 L | GBP-Abhängigkeit der Leads | C + B | Form (share of leads from Google profile). GBP insights (calls, routes, site clicks, 90 days) | text. Red flag if share over 40 % and profile is weak |
| B05.02 L ! | GBP-Anzahl und echte Adressen | A + C | Falcon list by name, address, phone. Form (confirm real addresses). Master data | red if a profile has no real service address or an unknown profile exists |
| B05.03 L ! | Bewertungstempo und -prozess | A + C | Falcon review data (count, rating, new per 90 days and 12 months). Form (how reviews are asked) | green if own velocity at least 50 % of leader's. Yellow 25-49 %. Red below 25 % |
| B05.04 | Review-Antwortquote | A | Falcon or Maps read (share answered, median delay) | green at 90 % or more. Yellow 50-89 %. Red below 50 %. Health: neutral thanks only |
| B05.05 | Aktuelles Ranking-Wissen | C + D | Form (what the client believes). Delta against B05.06 | text. Red if belief is top 3 and measure is not |
| B05.06 L ! | Messung je Keyword (SoLV, ARP) | A | Falcon scan 7x7 per keyword (Google). Existing reports first (free) | green: SoLV 40 % or more. Yellow 15-39 %. Red below 15 % |
| B05.07 | Google-Ads-Audit | C + B | Form (runs Ads? budget). Ads account read: conversion tracking, location setting, search terms, cost per lead | grey if no Ads. Red if no conversion tracking or location setting too wide |
| B05.08 | Maps-Verlauf (Trend) | D | Last run against this run (only same grid and radius) | arrow. Grey on first run |

### B06 Live-Technik-Check (score weight 15, agent only)

| ID | Feld | Type | Source | Rule |
| --- | --- | --- | --- | --- |
| B06.01 L ! | Asset-Eigentümerschaft | A + B + C | Domain registrar (WHOIS), DNS and hosting, `access_grants`, form (who owns GA4, GTM, GSC, Ads, GBP). GBP manager list (browser read) | green if client is owner of domain and GBP. Yellow if unconfirmed. Red if a third party owns domain or GBP |
| B06.02 L | Startseite und Conversion-UX | A | Desktop and mobile screenshot. Checklist: H1 matches keyword, CTA above fold, tap-to-call, form, trust proof, tracking events fire | by checklist share (green 75 % or more) |
| B06.03 L | Schnelle SEO-Fehler | A | Live-site script: title, meta, H1, canonical, JSON-LD, OG, alt, robots, sitemap, HTTPS, redirects | green: no error. Yellow: 1-3. Red: 4 or more |
| B06.04 | Qualität der Location-Seiten | A | Per location: own page, unique text (similarity), NAP match, map, LocalBusiness schema, link to and from GBP | by checklist share |
| B06.05 ! | Live-NAP-Konsistenz | A | Site (Impressum, footer, schema) against GBP against master data against `client_citations` + 10 live directory checks | red if any core NAP field differs on site or GBP |
| B06.06 | Indexierung | A | GSC URL Inspection and coverage. Fallback: sitemap against `site:` search via Firecrawl | green: 95 % or more of sitemap URLs indexed |
| B06.07 | Tech-Stack und Analytics | A | GTM, GA4, Ads tag, consent mode, key events, call tracking. PageSpeed (mobile) | red if no conversion events. Yellow if mobile LCP over 2.5 s |
| B06.08 | Keyword-zu-Seite-Zuordnung | A + D | Each priority keyword and each GBP service against site pages | green if every one has a matching own page |

### B07 Off-Page, PR & Reputation (score weight 10)

| ID | Feld | Type | Source | Rule |
| --- | --- | --- | --- | --- |
| B07.01 L | Backlink-Audit | A | DataForSEO backlinks summary: client + competitors (rank, backlinks, referring domains, dofollow share, first seen) | relative to leader: green at 50 % of leader's referring domains or more. Yellow 20-49 %. Red below 20 % |
| B07.02 | Lokale PR und Citations | A | `client_citations` status (270 rows in DB), core DACH directories, niche directories | green if 80 % of core directories are live |
| B07.03 | Social-Media-Auftritt | A | Profile found, last post date, followers (Firecrawl) | green if active in last 60 days |
| B07.04 | Anti-SEO und Negativ-PR-Suche | A | Brand query autocomplete ("name + erfahrungen / abzocke / bewertung"). First-page results. Review spikes of 1-star | red if a negative result sits on page 1 or a 1-star burst exists |

### B08 Betrieb & Kommunikationsregeln (business fit, no score)

| ID | Feld | Type | Source | Rule |
| --- | --- | --- | --- | --- |
| B08.01 | CRM und Umsatz-Zuordnung | C | Form (system, can leads link to channel and revenue) | yellow if not possible |
| B08.02 | Ansprechpartner | C | Form (name, role, decision maker, approver) | text. Writes to master data |
| B08.03 ! | Tabu-Bereiche der Website | C | Form (what nobody may change) | text. Writes to `client_master_data.boundaries` |
| B08.04 | Kommunikationspräferenzen | C | Form (channel, reply time, address form du or Sie) | text. Writes to `clients.lang` / mode |

### B09 Eignungsprüfung "Nein sagen können" (business fit, no score)

| ID | Feld | Type | Source | Rule |
| --- | --- | --- | --- | --- |
| B09.01 L ! | Operative Kapazität | C | Form (new clients per month possible, waiting time, staff) | red if capacity is below the leads needed for break-even |
| B09.02 L | Finanzielle Tragfähigkeit | C | Form (budget range, ad budget, payment readiness) | red if budget is below the offer. No price is shown to the client |
| B09.03 L ! | Realitäts-Check der Anrufannahme | C + A | Form (who answers, hours, missed calls). Site and GBP phone hours. Optional test call logged by Martin (M) | red if site hours and GBP hours differ, or answered share is under 70 % |
| B09.04 | Fit-Verdikt | D | Section 5.3 | Ja / Noch nicht / Nein / Offen |

### B10 GBP-Qualität im Detail (score weight 15, new)

Target numbers come from the blueprint. Rule for small practices: coverage beats volume.

| ID | Feld | Type | Source | Rule |
| --- | --- | --- | --- | --- |
| B10.01 L ! | Kategorien (primär + sekundär) | A | Falcon list, against leader categories | green if primary equals leader's primary and gaps are 0-1. Red if primary differs from the main service |
| B10.02 L | Leistungen im Profil | A | Falcon list or Maps read: count, each with own page | green if every listed service has a page and count is in 20-50, or full coverage in a small practice |
| B10.03 | Produkte | A | Maps read | grey if not relevant |
| B10.04 | Attribute | A | Maps read | yellow if relevant attributes missing |
| B10.05 | Beschreibung | A | Length (max 750), main keyword, advertising-law words | red if empty or breaks advertising law |
| B10.06 | Fotos | A | Count, last upload date, against leader | green at 70 % of leader's count and upload in 90 days |
| B10.07 | Beiträge (Posts) | A | Last post date, posts in 90 days | green: 1 or more per 14 days |
| B10.08 | Fragen und Antworten | A | Count, answered share | yellow if none |
| B10.09 | Öffnungszeiten | A | Complete, special hours, match to site | red if differs from site |
| B10.10 | Inhalt der Bewertungen | A | Share of reviews that name a service or place. Sentiment | green: 40 % or more name a service |
| B10.11 | Link-Ziele (Website, Termin) | A | Link target is the best page. UTM tagged | yellow if link goes to a weak page |

### B11 Wettbewerber-Benchmark (score weight 15, new)

| ID | Feld | Type | Source | Rule |
| --- | --- | --- | --- | --- |
| B11.01 L | Wettbewerber-Auswahl und Begründung | A | Top 5 (light: 2) from the Falcon report of the priority-1 keyword. Reason per pick | text. Must state why these |
| B11.02 L | Vergleichstabelle | A | Per competitor: SoLV, ARP, reviews, rating, category count, service count, domain, referring domains, first seen, niche page yes/no | table |
| B11.03 L | Review-Lücke | D | Section 5.3 formula (facts) | green if gap 0. Yellow up to 9 months or if reviews are not a driver. Red above 9 months when reviews are a driver |
| B11.04 | Autoritäts-Lücke | D | Referring domains against leader | as B07.01 |
| B11.05 | Kategorien-Lücke | D | Leader categories the client lacks | green 0. Yellow 1-2. Red 3 or more |
| B11.06 | Inhalts-Lücke | D | Leader service pages the client lacks | same scale |
| B11.07 ! | Schwäche des Marktführers | A + D | Lowest rating, no niche page, old profile, few posts | text. Output yes/no for "angle" |
| B11.08 ! | Realismus für Platz 1 | D | Section 5.3 (D1), per priority-1 keyword | realistic / slow / unrealistic |
| B11.09 ! | Treiber-Analyse | D | `analyze_drivers.py` on the full Falcon report: rho reviews, category lift | green if the client holds all driver categories. Yellow if one is missing. Red if two or more are missing |

### B12 KI-Sichtbarkeit & Apple Maps (score weight 5, new)

| ID | Feld | Type | Source | Rule |
| --- | --- | --- | --- | --- |
| B12.01 | KI-Sichtbarkeit je Plattform | A | Falcon scans: ChatGPT, Gemini, AI Mode, AI Overviews. Per keyword | green: mentioned in 40 % or more |
| B12.02 | Zitierte Quellen | A | Falcon AI scan source list | text. Shows which domains win |
| B12.03 | Apple Maps | A | Falcon Apple scan or listing check | red if no listing |
| B12.04 | KI-Money-Prompts | A + D | Own prompt list in `visibility_prompts` against blueprint (10-30) | green if 10 or more active prompts |

### B13 Risiko: Sperrung und Duplikate (score weight 10, new)

| ID | Feld | Type | Source | Rule |
| --- | --- | --- | --- | --- |
| B13.01 L ! | Duplikate und Doppel-Einträge | A | Falcon list and Maps search by name, address, phone, old addresses | red if a duplicate exists |
| B13.02 L ! | Adress- und Verifizierungsrisiko | A + C | Storefront or service-area. Virtual office or coworking hint. Recent move (form). Verification state | red if address moved and GBP or site is not updated |
| B13.03 | Name im Profil | A | GBP name against legal name. Keyword stuffing | red if extra words |
| B13.04 | Kategorie- und Attribut-Risiko | A | Restricted categories | yellow if borderline |
| B13.05 ! | Branchen-Werberecht | A + M | Niche profile: health = HWG, law = BRAO/BORA and UWG, tax = StBerG and UWG, other = UWG. Scan site and GBP text for banned claims | red if a banned claim exists |
| B13.06 | Profilstatus und Zugriff | A + B | Open or closed flag. Manager list. `access_grants` | yellow if no manager access for 741 |
| B13.07 | Review-Richtlinien-Risiko | A | Incentive or gating hints. 1-star bursts (links to B07.04) | red if gating hint found |

Field total: 75 fields. Light mode runs the fields marked `L`.

## 7. Cost and caps

| Item | Kickoff (Deep) | Call (light) | Cap |
| --- | --- | --- | --- |
| Falcon, Google 7x7, 5 keywords | 245 credits | 49 credits (1 keyword) | 800 credits total, ask before more |
| Falcon, 4 AI platforms + Apple, 5 keywords | about 430 credits (derived: Stürzl run cost 673 in total, Apple scan extra and untested) | 0 | included in cap |
| DataForSEO volume (about 5 calls) | about 0.45 USD | 0.09 USD | 8 EUR (call: 1 EUR) |
| DataForSEO backlinks (client + 5 competitors) | about 0.15 USD | 0.07 USD | included |
| DataForSEO Business Data (to test) | unknown | unknown | included |
| Other tools | free | free | — |

`cost_ledger.jsonl` logs every paid call. The script stops at the cap. It never retries a scan. Spend above cap needs Martin's go.
Existing Falcon reports are read first. Reading is free.

## 8. Checkpoints

| ID | When | What Martin sees | Choice |
| --- | --- | --- | --- |
| Go-A (spend) | After phase 1 (free pulls) | Subject, mode, 5 keywords with priority and volume, 5 competitors with reason, cost estimate, form coverage | go / edit keywords / stop |
| Go-B (review) | After scoring and report build | Internal HTML report, validator result, list of open inputs | corrections (count logged) / go |
| Go-C (release) | After Go-B | Client-safe tab as draft, client message draft in "ich" form, Drive link | release / hold |

Between the checkpoints agents run alone. No scan, no table write and no client-visible change happens before its checkpoint.
The workflow ends with: client message draft (see Martin's rules: full message, no call offers, "ich" form), Drive link and screenshot as file.

## 9. Hard rules

1. Collect only. Change nothing on client assets. Any fix needs a separate per-change "go".
2. Every finding has source, date and confidence. Allowed confidence: `verified`, `derived`, `client_stated`. A guess has no place. Missing data shows a yellow `[von Kunde bestätigen]` or `unknown`.
3. Volume 0 means no data. Run the autocomplete check.
4. Client-safe output: no tool names, no team names, no price of the offer, no fit verdict, no cost. Use "Google-Daten" and "Maps-Messung". Address form from `clients.lang` / B08.04.
5. Health clients: HWG check. No promise of success or cure. Law and tax clients: own advertising law (B13.05).
6. Falcon: only via MCP. Never retry a scan. Same grid and radius within one client series.
7. CRM data from the client is anonymized. Law clients: no client names (professional secrecy).
8. Agents write JSON first. Database load happens only after tables exist and Martin approved them.
9. Replies in STE. Client text in normal German prose.
10. Supporting files (Docs, Sheets) go into the client's Google Drive folder, subfolder `_Audit-Hilfsdaten` (added 2026-10-11 by Martin). Name pattern: `[Audit-Hilfsdaten] <Typ> <YYYY-MM-DD>`. They are working files for later search. They are not client deliverables and nobody shares them. The run logs every Drive file id in `manifest.json` (`drive_file_id`). Unused or wrong files are moved to trash (never deleted for good) when Martin says so. Drive MCP creates files. It cannot write cells. Use Chrome for cell edits.
11. Review numbers of the client come only from the client's own Google account (profile read in Chrome as `741studio18`). Falcon review counts are incomplete (0 can mean no data). They serve only as a hint for competitors and carry the note "teils unvollständig" (Martin, 2026-10-11).

## 10. Outputs

Per run, in `00_project/assets/audit/<subject-slug>/<YYYY-MM-DD>-<mode>/`:

| File | Content |
| --- | --- |
| `run.json` | Run header: mode, params, caps, cost, score, verdict |
| `findings.json` | All fields with status and metadata |
| `competitors.json`, `keywords.json` | Market data |
| `evidence/` + `manifest.json` | Raw files with hash, tool, request, date |
| `report/internal.html` | Martin and team. Page 1 summary, block detail, raw data index |
| `report/client.html` | Client-safe. Draft until Go-C |
| `cost_ledger.jsonl` | Paid calls |
| `sheet-view.json` | Rows for tab `02 Audit` |
| Drive: `_Audit-Hilfsdaten/` | Supporting Docs and Sheets of the run (rule 10). Ids in `manifest.json` |

Details: `data-model.md` and `report-wireframe.md`.

## 11. Success measures

| Measure | Target | How measured |
| --- | --- | --- |
| Corrections by Martin at Go-B | under 3 per audit | Count in `audit_runs.corrections_count` |
| Unsourced claims | 0 | Validator `validate_run.py`: every finding has source, date, confidence, evidence |
| Baseline | Stürzl manual work (week-1 findings, competitor analysis, Falcon campaign) | Compare corrections and time against the manual path |
| Later | Falcon SoLV gain at re-audit | `B05.08` trend, same grid |

## 12. Defaults accepted at checkpoint 1 (2026-10-11)

Martin said "go" with the proposed defaults. Items 5-8 still need a separate go or a test in the dry run.

1. Fit thresholds: 9 months realistic, 18 months unrealistic, default velocity 4 reviews per month. Do you accept them?
2. Score weights in section 5.2. Do you accept them?
3. Light profile for the pre-sale call (1 keyword, 2 competitors). Do you accept it, given Deep is the default elsewhere?
4. Falcon radius default 5 km. The Stürzl campaign of 09.10. used 5 mi. Which one stays?
5. Tool tests in the dry run: DataForSEO Business Data, GSC URL Inspection, PageSpeed API, GBP insights read in Chrome. Agree to test them with one call each?
6. Supabase tables: approve `schema.draft.sql` before any table is created?
7. Portal form: build it after the dry run? For the dry run, I fill the answers from the Stürzl sheet tab `01 Erstgespraech`.
8. Niche profiles for B13.05: health (HWG), law (BRAO/BORA), tax (StBerG), other (UWG). Missing a niche?

## 13. Dry-run learnings (Stürzl kickoff, 2026-10-11)

Run folder: `00_project/assets/audit/stuerzl/2026-10-11-kickoff/`. Validator: 0 errors. Result: score 28/100, coverage 83 %, verdict Ja.

| Tool test | Result |
| --- | --- |
| Local Falcon GBP API tools (profile, services, posts, photos, reviews, performance) | NOT usable. They need the On-Demand API (not in the Starter plan). Use a browser read of the profile instead |
| Local Falcon `searchForLocalFalconBusinessLocation` | Returned 0 results for the Frankfurt profile (known tool limit). It found München. Never read "no result" as "no profile" |
| Local Falcon `listLocalFalconScanReports` pagination | Parameter `next_token` repeats page 1. Only 10 unique reports came back. Fix before the next run |
| Local Falcon credits | Account showed 797 usable credits on 11.10. (261 package credits + 526 extra). The package gives 7,500 credits per cycle and the cycle ends on 19.10.2026, so the low balance was the end of a cycle, not an empty account (first note in this row was too strict). Check credits and cycle end at intake |
| PageSpeed Insights API without key | HTTP 429 quota. Needs an API key. Fallback: rendered LCP from a browser run |
| GA4 and Search Console via service account | HTTP 403 for this client. Access was given to the 741studio18 account, not to the service account. Use the browser (741studio18) or add the service account |
| DataForSEO backlinks summary | Works. 7 targets cost 0.17 USD |
| DataForSEO Business Data | Not tested (Martin chose "no extra purchase") |
| GSC URL Inspection | Not tested (no access) |
| Business Profile Manager and profile view in Chrome (741studio18) | Works for read. Gives categories, services, photos, performance (calls, directions, website clicks), review list. Slow but complete |

Design changes from the dry run:

1. **D1 (section 5.3):** the fit check finds the market driver first (reviews or categories). Reviews were not a driver in the Stürzl market.
2. **Reused data:** a run may reuse earlier evidence. The manifest marks it `REUSED` with the original date. Findings keep the original `collected_at`.
3. **Run-specific builder:** `scripts/build_run.py` in the run folder holds the curated findings. A later run needs a generic collector. The catalog, scoring, validator and report scripts are generic: `00_project/audit-workflow/scripts/`.
4. **Review data (found 2026-10-11):** Falcon shows 0 reviews when it has no data (Pohl 13 and Tikbas 32 real Google reviews). `analyze_drivers.py` now merges the best count per profile across all reports. Competitor review counts for the report come from the public Google panel (Chrome). The first D1 claim "profiles with 0 reviews lead" was wrong. The conclusion (reviews are not a driver) still holds with the corrected data.
5. **Access status (Martin, 2026-10-11):** Joomla access exists (role to check: Super User). The München profile and Search Console access are expected at the start of the week of 12.10.2026. Until then, München is read from public data only and indexation stays `unknown`. The re-audit adds them. The run keeps these fields open and does not guess.
6. **Privacy:** the Business Profile Manager lists all client profiles. Never copy other clients' data into a run.

## Registry entry (2026-10-11)

Every run of this workflow is recorded in the workflow registry. The Excel `~/Desktop/Workflow-Uebersicht.xlsx` shows per client whether the workflow ran, its state, the last run, Martin's approval and the folder links.
- At the start or end of a run: `python3 /Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py upsert --client "<client>" --workflow audit --status "in Arbeit|Trockenlauf|fertig, Freigabe offen" --local <folder> --drive <url> --result <file>`
- When Martin approves the result: `python3 /Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py approve --client "<client>" --workflow audit` in the same turn, then tell Martin the sheet was updated. A hook reminds Claude when a message sounds like an approval.
Workflow id: `audit` (Client Audit).

## Registry: automatic (2026-10-11)

The overview Excel `~/Desktop/Workflow-Uebersicht.xlsx` updates itself. A Stop hook runs `workflow_registry.py sync --quiet` after every turn. You do not call `upsert` for normal progress. At the end of a run, set `status` to `done` in `<run>/run.json` once the report files exist in `<run>/report/`. `sync` then shows the run as fertig, Freigabe offen and adds score and verdict to the note. Keep the field `subject_name` equal to the client name in the Excel.
For any other file layout, write `_run.json` in the run folder (schema in `00_project/workflow-registry/README.md`). Only the approval stays manual: when Martin approves a result, run `approve` in the same turn and say that the Excel is updated.

## 14. Dry-run learnings (Bali Healing kickoff, 2026-10-11)

Run folder: `00_project/assets/audit/balihealing/2026-10-11-kickoff/`. Validator: 0 errors. Result: score 46/100, coverage 90 %, fit check Offen. Cost: DataForSEO 0.31 USD, Falcon 196 credits (4 new scans, Go-A).

1. **D2 (fit check):** a keyword where the client already leads (SoLV 40 % or more) is `strong`. A keyword without a controllable driver is `unknown`, never `unrealistic`. A profile name that holds the search words is shown as a market driver but never advised (Google name rule, see B13.03). If all priority keywords are `unknown`, the verdict is `Offen` and says where the real blockers are.
2. **Generic scripts:** `analyze_drivers.py <run> <own name tokens>`, `collect_falcon.py <run> <placeIds>`, `dfs_pull.py`, `site_check.py <run> <base> <paths>` now run for any client. The driver categories are found in the data, not fixed. `params.relevant_categories` limits them to the client's real services.
3. **Falcon fixes:** the pagination parameter is `nextToken` (not `next_token`). Reports must be sorted by real date, not by text (a text sort put 9/28 before 10/5).
4. **Multi-profile client:** Bali Healing has two profiles at one address. The run reads profile 1 in depth and profile 2 in part. The catalog needs findings per profile (same gap as per location for Stürzl). Open design item.
5. **Tool limits:** Chrome blocks ads.google.com, so the Ads block uses dated reports. Search Console showed the URL-prefix property only, not the domain property. Falcon Reviews Analysis had no report for either profile. Review counts of competitors stay "teils unvollständig" (Falcon).
6. **Found by the audit, not by the tools alone:** `noindex` on money pages, a profile name with service words, a profile text that contradicts the client's own decision, and a spam-link wave across the whole niche. Each needs a human check before any change.

## 15. Dry-run learnings (741 Studio self-audit, 2026-10-11)

Run folder: `00_project/assets/audit/741studio/2026-10-11-kickoff/`. Validator: 0 errors. Result: score 39/100, coverage 59 %, fit check Offen. Go-A was "nichts kaufen": cost 0 USD and 0 credits.

1. **Free tools carry a lot.** Search Console API (service account, URL-prefix property), GA4 Data API (account-level viewer), URL Inspection API (16 sample URLs) and the profile read in Chrome gave belt-and-braces evidence at no cost. URL Inspection finds pages Google does not know. Add `inspect_urls.mjs` to the generic scripts.
2. **A free-only run is valid but incomplete.** Without Falcon scans the blocks B05.06, B11 and B12 stay `unknown`, the verdict stays `Offen`, and coverage drops (59 %). The report says so and names the cost to close the gap (245 credits, 0.17 USD).
3. **Self-audit mode:** subject is the agency itself, `client_id` null, no client-safe page (`client_lang: none`). Business-fit blocks stay open until the owner answers.
4. **Found by the audit:** noindex on the Bali landing pages, a core service page unknown to Google, a sitemap with 5 of about 450 URLs, a profile with 8 interactions in 5 months, and unproven result promises in the H1.
5. **Open design item:** the GA4 property of the live tag cannot be read by the service account. Decide the canonical property, then remove the other tag.

## Martin guide (2026-10-12)

The 741 character Martin points out the one thing per section the reader must not miss. Rules, poses, markup and the inline helper: `00_project/assets/brand/martin-guide/README.md`. In this workflow: in the client report: point at the score and the top 3 findings, insight at the first lever, think at missing data. Internal report: none. Max 1 callout per section, bubble text in first person and plain language, every number with source and date, check desktop and mobile with a screenshot.
