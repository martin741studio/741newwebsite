# Workflow spec: Proof Tracking + Quarterly Strategy Round

Registry id: `tracking` · Label: "Proof Tracking + Quartal" · Version 0.1 (design for checkpoint 1) · Date 2026-10-12
Boards: 5 "Beweis zum Nachprüfen" (blue) and 6 "Die Quartals-Strategierunde" (orange), in `00_project/assets/tracking-workflow/`.
Related files: [tracking-coverage-map.md](tracking-coverage-map.md) · [tracking-metric-catalog.json](tracking-metric-catalog.json) · prototype `assets/tracking-workflow/prototype/`.

## 0. Purpose

The workflow measures what matters for each client: calls, real leads, booked jobs, Maps grid visibility and reviews.
It shows the numbers as proof that the client can check in her own Google profile.
It warns 741 early when a number drops or something breaks.
It collects all inputs for the 90-day strategy round, so that the war-room pack builds itself.
It must be easy for 741 (30 minutes or less per client per week) and easy for the client to understand.

## 1. Decisions from the grilling (Martin, 2026-10-12)

| # | Topic | Decision |
|---|---|---|
| D1 | Pilot | Praxis Suriya (Coralie Suriyapperuma). |
| D2 | Version 1 scope | All four areas: calls + real leads; booked jobs + cost per booked job; Maps grid + reviews; early warning + weekly update. |
| D3 | Client home | Portal tab only (clients.741.studio). No PDF. |
| D4 | Calls | No call tracking in version 1. Google-profile call clicks + the lead log. The main number stays the primary number. |
| D5 | Lead input | Website form leads flow into the portal tab "Anfragen" automatically (site change, needs go). The client adds phone, mail and WhatsApp leads and sets "gebucht" + value. |
| D6 | Missing client data | Show "fehlt seit <Datum>" + one reminder. Never estimate. Cost per booked job stays empty. |
| D7 | Cost basis | 741 programme fee + paid ads spend of the same month. |
| D8 | Weekly rhythm | Weekly card "Wochen-Update" in the tab (agent draft) + Martin's raw Loom. |
| D9 | Grid | Monthly scan, 5 locked keywords, locked config. About 245 credits per month for Suriya. |
| D10 | Alerts | Red: email at once, `alerts@741.studio` → `martin@741.studio`. Yellow: the 08:05 standup. |
| D11 | Client and warnings | The client sees a warning only after Martin checks it and writes a note. |
| D12 | Reaction time | Red: same working day. Yellow: within 1 week. |
| D13 | Quarterly pack | Agent draft 5 working days before the meeting; Martin edits. |
| D14 | Pack format | A dated "Quartalsrunde" page inside the proof tab, with decision log. Internal version for Martin. |
| D15 | Monthly call | Only on request. No fixed monthly call. |
| D16 | Data store | New Supabase tables in `741-portal` + JSON and `_run.json` per run. Tables only after Martin's go. |
| D17 | Runner | Supabase pg_cron + edge functions (cloud). Agent runs (weekly card, monthly, quarterly) as Claude sessions or routines. |
| D18 | Card release | Martin releases each weekly card with one click. |
| D19 | Cost cap | 5 EUR per client per month (DataForSEO + model tokens), plus Falcon credits (D9). |
| D20 | Success | Client checks numbers herself; 741 sees red problems first; Martin ≤ 30 min per client per week; renewal after 90 days. |

## 2. Scope

In version 1 (pilot Suriya): metrics with `"v1": true` in the catalogue (31 of 34). The client tab "Ergebnisse" with three layers. The weekly card. Early-warning rules R1–R6 and Y1–Y9. The lead intake from the website form. The attribution chain to cost per booked job. The quarterly pack for the first round (about 01.12.2026).

Not in version 1: call tracking numbers; automatic review requests; CRM sync for other CRMs (Pipedrive and others: phase 2); AI visibility, backlink snapshot and season volume history run only inside the quarterly agent run (M30, M31, M33); DataForSEO on a schedule (needs a fixed-IP runner).

## 3. Use cases and test scenarios

Use cases:
1. Weekly (Monday 07:30 Berlin): data is fresh. The agent drafts the weekly card for each active client. Martin releases it and records a Loom. Trigger: `/tracking weekly <Kunde>` or the scheduled run.
2. Alert: a red rule fires (for example, the profile phone number changed). Martin gets an email with the evidence and the rollback hint. He fixes it the same working day and writes the client a short note.
3. Quarterly: 5 working days before the strategy round, the agent builds the war-room pack from the tracked data. Martin edits it, meets the client and records decisions in the decision log. Trigger: `/tracking quarter <Kunde>`.

Test scenarios for the skill (before the body is written, rule R1.2):
| # | Prompt | Expected |
|---|---|---|
| T1 | "/tracking weekly Suriya" | Skill loads. Reads data from the tables or the JSON run, drafts the card, writes `_run.json`, shows the draft to Martin. No portal write without the release click. |
| T2 | "Bereite die Quartalsrunde für Coralie vor" | Skill loads in quarter mode. Builds the pack sections from section 11, marks data gaps, lists decisions to take. |
| T3 | "Mach einen neuen Maps-Scan für Hüwel" | Skill does NOT load. A single scan belongs to `ranking-tracking-master-prompt.md`. |

## 4. Pipeline and cadence

```
DAILY  (pg_cron, Berlin time)            WEEKLY (Mon)                    MONTHLY (1st Mon)                 QUARTERLY (T-5 working days)
06:07 collect GBP perf, reviews,        07:07 compute week values        agent: read grid campaign report   agent: build war-room pack
      profile, verification (LF)        07:30 agent drafts weekly card   agent: competitors + reviews delta  Martin edits (GO-Q1)
06:17 collect GA4, GSC                  → Martin: release (GO-W)         agent: SERP check (DataForSEO)      meeting → decision log
06:27 site + form check (hourly too)    → Martin: Loom link              agent: reconciliation (leads ↔     client page released (GO-Q2)
06:37 run rules → alerts                                                  booked ↔ cost)
08:05 standup shows yellow                                                → monthly section in the tab (GO-M)
```

Cron times follow rule R6.9 (minutes past the hour). Every job states `Europe/Berlin` (rule R6.6).
Local Falcon campaign for the grid: monthly, on the first Monday, locked config (section 5.3).

Checkpoints (Martin's go):
- GO-W: release of each weekly card (one click in the admin view).
- GO-M: release of the monthly section (grid, competitors, reconciliation).
- GO-Q1: Martin approves the internal pack. GO-Q2: release of the client page after the meeting.
- GO-SITE: once per client, for the form webhook on the client website.
- GO-DB: once, for the new tables and the edge functions.
- GO-SPEND: any new scan or spend outside the locked monthly campaign.

## 5. Collectors

### 5.1 Sources and access (checked 2026-10-12)

| Source | Metrics | Access | Status for Suriya |
|---|---|---|---|
| Local Falcon MCP, GBP tools (free reads) | M01–M04, M17, M18, M20, M27, M28 | `mcp.localfalcon.com`, Bearer key in `.env`; only for profiles connected in Local Falcon | Works. Live read 2026-10-12: data until 09.10. |
| Local Falcon campaign scans (credits) | M13–M16, M19 | campaign with locked config | Last scans 15./16.08.2026 (7×7, 5 km). No scan since. |
| Portal table `leads` | M05–M09, M12, M34 | Supabase `741-portal`, RLS per client | Table exists, 0 rows. Tab "Anfragen" only in staging. |
| Client website form | M05 | edge function `lead-intake` (to build); webhook from the form (site change) | Form at `/termin-buchen/`. Webhook needs GO-SITE. |
| 741 invoices + ads | M10 | fee per client in `clients.billing` (empty today); ads APIs | Suriya: no ads. Fee: Martin enters once. |
| Search Console | M21, M22 | service account, per property | Works for `https://suriya-praxis.de/`. |
| GA4 | M24 | service account, account-level viewer | Property ID for Suriya to confirm. |
| DataForSEO | M23, M31, M33 | `.secrets/dataforseo.env`; whitelisted IP | Agent run only. |
| Website fetch | M25, M26 | edge function | — |

### 5.2 Collector rules (rules.md section 6)

- Each source has a bookmark (last day read). The collector reads from the bookmark, never "the last 24 hours" (R6.1).
- Google profile data has about 3 days delay. A day counts as final after 5 days. Weeks compare only when complete.
- A failed read writes status `unreadable` with the error. The tab shows "nicht lesbar seit <Datum>", never 0 (R6.2).
- A value counts as stored only after the database confirms the insert. Bookmarks move only after that (R6.3).
- Collectors use read-only credentials where the source allows it. The Local Falcon key can write to Google, so the edge function calls only an allow-list of read tools (L1 guard from the automation workflow).
- Spend cap per run: 3–5× a normal run (R6.5). Falcon scans run only from the locked campaign.

### 5.3 Locked scan config

One config per client: grid, radius, platform, keywords, cadence. A change needs Martin's go and a log row with date and reason. A scan with another config is stored but never compared. This fixes the radius drift found at Stürzl (5 km vs 5 mi).
Suriya proposal (from the 15./16.08. baseline, all 7×7, 5 km): heilpraktiker ingelheim, migräne behandlung, schmerztherapie ingelheim, akupunktur ingelheim, naturheilpraxis ingelheim. Open: "ayurveda ingelheim" (rank 1 already) or "vagusnerv therapie" instead of one of them.

## 6. Metric catalogue

See [tracking-metric-catalog.json](tracking-metric-catalog.json): 34 metrics, each with definition, source, collector, cadence, owner, layer, client visibility, warning thresholds and the quarterly question it feeds.
Client names are plain German ("Anrufe über dein Google-Profil", "Kartenpunkte mit Platz 1–3"). No tool names, no SoLV, ARP or NAP in client text.

## 7. Early-warning rules

Baseline = the frozen client baseline (Suriya: 28.06.–23.09.2026). After 12 weeks of programme data, the rolling 8-week median replaces it for yellow rules.

Red (email at once, same working day):
| Id | Rule | Source |
|---|---|---|
| R1 | Homepage or booking page not HTTP 200 in 2 checks in a row | M25 |
| R2 | Booking form marker missing | M26 |
| R3 | Live profile field (name, address, phone, website, hours, primary category) differs from the locked master | M27 |
| R4 | Profile unverified or suspended | M28 |
| R5 | Tracking broken: GA4 0 sessions while 7-day average > 5, or a source unreadable 2 days in a row | M24, all |
| R6 | New review with 1 or 2 stars | M17 |

Yellow (08:05 standup, within 1 week):
| Id | Rule | Source |
|---|---|---|
| Y1 | Profile views of the last complete week < 70 % of the baseline week | M04 |
| Y2 | Calls + website clicks + routes of the last complete week < 70 % of the baseline week | M01–M03 |
| Y3 | Grid: top-3 share drops ≥ 15 points or average rank worse by ≥ 2 on a locked keyword | M13, M14 |
| Y4 | 0 new reviews in 60 days, or own 3-month average below the top-3 competitor median | M18, M19 |
| Y5 | 0 form leads in 14 days while website clicks > 0; or no client lead entry for 14 days | M05, M06 |
| Y6 | Search Console clicks 28 days < 80 % of the previous 28 days | M21 |
| Y7 | Pending Google suggestion on the profile | M27 |
| Y8 | Weekly card not released by Wednesday 12:00, or > 10 days without client update | M29 |
| Y9 | Cost cap 80 % reached, or Falcon credits below the next campaign run | runs |

Each alert has: rule id, client, value, threshold, evidence (raw value + source + read time), first seen, status (open, seen, fixed, false alarm). The same alert fires once and then repeats only in the standup until it is closed.
Client view (D11): never automatic. Martin closes the alert and, if relevant, writes a note in the portal.

## 8. Client tab "Ergebnisse"

Three layers, one page. Wireframe and rendered prototype: `assets/tracking-workflow/prototype/`.

1. 30-second view ("Auf einen Blick"): six tiles with a traffic light per area:
   - Anfragen
   - Gebuchte Termine
   - Kosten je gebuchtem Termin
   - Kontakte über Google (calls, website clicks, routes)
   - Sichtbarkeit in Google Maps
   - Bewertungen

   Each tile shows the value, the comparison with the baseline, the date range and "fehlt" or "nicht lesbar" when data is missing.
2. Weekly card ("Wochen-Update"): numbers of the week, 3 short sentences (what moved, why, what we do next), the Loom link, release date.
3. Proof layer ("Belege"):
   - dated grid images per keyword
   - competitor table
   - weekly chart of Google-profile actions
   - a source line under each number ("Quelle: dein Google-Profil, abgerufen am …")
   - the guide "So prüfst du die Zahlen selbst" (steps in her own Google profile: Leistung → Zeitraum → Anrufe)
4. Raw data ("Rohdaten für Prüfer", collapsed): the JSON of the last run with metadata (source, read time, bookmark, run id). Agents use the same JSON.
5. "Quartalsrunde" pages (dated) with the decision log.

Martin guide (`00_project/assets/brand/martin-guide/README.md`, rule from Martin 2026-10-12): the 741 character points out the one thing per section that the reader must not miss.
- point: at calls and the lead chain / cost per booked job; at the competitor gap
- think: at early warnings and open or unreadable data
- celebrate: only at real wins, with source and date in the same section
- insight: at the next quarter's lever

Max 1 callout per section, about 5 per page. The bubble is Martin in first person, "du", at most 2 sentences, plain words, no tool names, HWG-safe. The text sits in HTML. Self-contained files run `inline.py`. The same rule applies in the weekly card view and the quarterly pack. Never on the client's own website.

Language: "du" for Coralie. Plain words. No jargon without translation (memory review-page-plain-language). Health practice: no healing promises, no patient case text (HWG).

## 9. Lead intake and attribution chain

Chain: Google profile action or website visit → lead (form or phone) → status "gebucht" → value → cost per booked job.

- Lead events that already exist (found 2026-10-12): the Suriya site pushes `s741_form_submit` (Contact Form 7 + Fluent Forms), `s741_whatsapp_click` and `s741_phone_click` to the dataLayer. GTM `GTM-K9MDDN7P` forwards only form and WhatsApp to Google Ads (`AW-18502523090`). GA4 `G-B93S7ZWNNR` gets none of them, and the service account cannot read that property.
- Version 1 lead count (preferred, no site code change): F1 one GA4 event tag in GTM for the three events + F2 service account as GA4 viewer → automatic daily count of form, WhatsApp and phone clicks. F3 Fluent Forms entries (read-only from WordPress) give the exact form count as a cross-check.
- Booked appointments: the site has no booking system (the form is a request). Only Coralie knows if a request became a booking (F4: tick in "Anfragen", or the Fluent Forms entry status).
- Form leads with contact data: the website form posts to the edge function `lead-intake` (to build, pattern of `notify-lead`). It inserts into `leads` with channel `formular`, page and UTM. The form keeps its current email to Coralie, so nothing breaks if the function fails (memory suriya-conversion-paths-must-stay).
- Phone, mail and WhatsApp leads: Coralie adds them in the tab with 3 fields: Kontaktweg, "Wie hast du uns gefunden?", Ort.
- Status: neu → in Kontakt → gebucht / nicht gebucht / passt nicht / Spam. Value in EUR when "gebucht".
- Data rule: only contact data, channel, origin, town, status, value. No symptoms, no diagnosis, no free-text case details (health data, Art. 9 GDPR; same rule as the Stürzl lead CRM, §203 StGB).
- Monthly reconciliation (agent): counts form leads in the table against GA4 form events and against the form emails Coralie confirms; lists leads without status for 14 days; computes M07–M12; shows each gap openly ("3 Anfragen ohne Status").
- Cost per booked job = (741 fee of the month + ads spend of the month) / booked jobs of the month. Empty when booked jobs are missing (D6).
- Finance reconciliation for 741 (board item "KI-Agenten für Finanz-Reconciliation"): the monthly run also checks that the fee in `clients.billing` matches the 741 invoice of the month (read-only, invoice workflow unchanged).

## 10. Communication rhythm ("nie im Unklaren")

| When | What | Who |
|---|---|---|
| Async, always | Portal support chat; the standup flags unread messages | client ↔ 741 |
| Weekly (Mon draft, release by Wed 12:00) | Weekly card + raw Loom walkthrough (unedited screen recording of her own Google profile and the grid) | agent drafts, Martin releases and records |
| Monthly (first Monday) | Monthly section: new grid images, competitor table, review comparison, lead reconciliation | agent drafts, Martin releases (GO-M) |
| On request | Strategy call (D15); notes go into the decision log | Martin |
| Every 90 days | Quarterly strategy round with the pack | Martin + client |
| On a red alert | Short portal note after the fix | Martin |

## 11. Quarterly war-room pack

Data is collected continuously, so the pack only assembles it. The agent builds the draft 5 working days before the meeting (first Suriya round: programme end 01.12.2026 → draft on 24.11.2026; Martin confirms the date).

| Pack section (board 6) | Built from |
|---|---|
| 1 Ergebnis in Zahlen | M01–M12 per month of the quarter vs baseline; data gaps listed |
| 2 Konkurrenz & Marktdynamik: gained, lost, new, gone, links built | M16 per scan (diff first vs last scan of the quarter), M19, M31 |
| 3 Anpassung & Reaktionsprüfung | decision log of the last quarter: decision, done?, effect in the data |
| 4 Plateau & Sättigung: ranking, content, distance limit, capacity | M13–M15 trend (no gain in 2 scans = plateau signal), grid edge cells, M22, M32 |
| 5 Kürzen & Verdoppeln, refresh before new | M22 pages: losers (cut or refresh), winners (double down); content-pool items not yet built |
| 6 Geografische & wirtschaftliche Expansion | weak grid cells, M03 routes, M34 lead towns, catchment area (Suriya: Ingelheim, Bingen, Mainz, Wiesbaden) |
| 7 Vorbereitung neuer Standorte (only if section 6 says yes) | checklist: research, clean verification, listings before verification, review distribution, economics |
| 8 Saison- & Markt-Radar, 2–3 quarters ahead | M33 volume history, GSC impressions by month, known algorithm and AI changes (M30) |
| 9 Agenda + decisions to take | 3–5 decision questions with options and data; empty decision-log rows |

Output: internal HTML (all data and sources) + client page in the tab (plain language) + `decisions.json`. Decision log fields: date, decision, owner, due date, metric to watch, review date.

## 12. Data model (draft, nothing created before GO-DB)

All in `741-portal`, RLS: the client reads only own rows and only `released = true`; admin reads and writes everything.

| Table | Key fields |
|---|---|
| `tracking_config` | client_id, place_id, ga4_property, gsc_site, baseline_from, baseline_to, fee_eur_month, scan_config (jsonb: grid, radius, platform, keywords, cadence), locked_at, change_log (jsonb) |
| `tracking_metric_values` | client_id, metric_id (M01…), period_start, period_end, grain (day/week/month), value, status (ok/unreadable/missing), source, read_at, run_id |
| `tracking_bookmarks` | client_id, source, last_day_read, last_ok_at, last_error |
| `tracking_alerts` | id, client_id, rule_id, value, threshold, evidence (jsonb), first_seen, status, closed_by, note |
| `tracking_cards` | id, client_id, kind (week/month/quarter), period, body (jsonb), loom_url, released, released_at, released_by |
| `tracking_decisions` | id, client_id, quarter, decision, owner, due, metric_id, review_date, outcome |
| `tracking_runs` | run_id, client_id, kind, started_at, finished_at, status, cost_eur, credits, notes |

Existing tables reused: `leads` (lead chain), `scans` (grid scan rows keep their format), `messages` (notes), `programs` (dates). Proof images go to the storage bucket `materials` under `<client_id>/proof/<date>-<slug>.png`.
Local copy of each run: `00_project/assets/tracking/<client>/<date>-<kind>/` with `data.json`, `card.md` or `pack.html`, and `_run.json` (registry).

## 13. Interfaces to other workflows

| Workflow | Gives to tracking | Gets from tracking |
|---|---|---|
| Onboarding / week-1 playbook | GBP connection in Local Falcon, access, NAP master, baseline | — |
| Maps audit (`audit-workflow-spec.md`) | first scores, keywords, competitors | quarterly re-audit input |
| Un-burning | NAP master and fixed listings | R3 profile-change alerts protect the clean state |
| Maps playbook | measures done with dates | effect per measure (before/after) for section 3 of the pack |
| Content pool + content writing | pages built with dates | M22 cut/double/refresh candidates |
| Automation build | safety layers L0–L6, test gate, alert channel | the edge functions and crons of this workflow are built under its rules |
| Ranking tracking master prompt | scan method | locked config replaces the manual 2-week rhythm for clients in this workflow |
| Daily standup | — | yellow alerts as new `pruefen[]` lines |
| Portal | tab, RLS, release pattern, staging first | — |

## 14. Safety layers (automation-build applies)

Every edge function and cron in this workflow is built with `/automation-build` rules:
- read-only classes for all collectors
- G class (go needed) for portal releases and site changes
- test gate with readback before anything runs unattended
- a canary on the first real day
- the alert channel `alerts@741.studio`

Portal changes follow `portal-single-file-workflow`: fetch live → backup → staging → live only after Martin's go.

## 15. Cost caps

| Item | Cap |
|---|---|
| Falcon credits | locked monthly campaign only (Suriya 245 per month); any extra scan needs GO-SPEND. Today 63 credits remain in the cycle (589 usable): the first campaign run needs Martin's credit decision. |
| DataForSEO + model tokens | 5 EUR per client per month; the run stops at the cap and asks. |
| Edge functions + cron | Supabase free tier; check the `741-portal` keep-alive stays green. |

## 16. Hard rules

1. Every number has a source and a read date. No number without both. Missing = "fehlt", failed read = "nicht lesbar".
2. Never estimate booked jobs, revenue or calls.
3. Nothing reaches the client without Martin's release (GO-W, GO-M, GO-Q2).
4. Client systems stay read-only. Site change only with GO-SITE. Google profile writes are never part of this workflow.
5. No tool names, team names or jargon in client text.
6. No health details in the lead table.
7. Scan config is locked; changes are logged.
8. Client emails only via Airmailer and never without Martin's go. This workflow sends no client email in version 1.
9. Each run writes `_run.json` for the registry.
10. STE for internal text; plain German, "du", for Coralie.
11. Every result has a link to where it comes from (Martin 2026-10-12): Google profile, original scan report, the same Google search, competitor profile, the website form, or the raw JSON. The reader can always go to the source.

## 17. Done criteria

- Version 1 is done when Suriya has run 4 weekly cycles. Each cycle needs a released card, a Loom and no unread red alert older than one working day.
- One monthly section is released, and the first quarterly pack is drafted from tracked data alone.
- The scorecard is ≥ 80 % with no zero in A or D. The trigger tests T1–T3 pass, and a baseline with and without the skill is measured.
- Success metrics (D20) are reviewed at the first quarterly round:
  - Coralie found the same numbers in her own profile.
  - Every real problem was flagged by 741 first.
  - Martin's time log shows 30 minutes or less per week.
  - The renewal decision is recorded.

## 18. Pilot findings so far (read-only, 2026-10-12)

| Finding | Evidence | Rule |
|---|---|---|
| Profile views fell: week 28.09.–04.10. = 53, week 05.10.–09.10. (5 data days) = 44; baseline 29.06.–27.09. = Ø 120 per week (median 110) | Local Falcon GBP performance, read 2026-10-12, raw JSON in `assets/tracking-workflow/prototype/data/` | Y1 fires (53 < 70 % of 120). Cause unknown. |
| Contacts over Google rose: calls + website clicks + routes in week 28.09.–04.10. = 29 (0 + 8 + 21); baseline Ø 17.2 per week | same | Y2 does not fire. Views down, real contact actions up: the client card must explain both. The relaunch started 24.09. |
| No Maps scan since 16.08.2026 | `listLocalFalconScanReports` for the Suriya place id | locked monthly campaign missing |
| 13 reviews, 5.0 stars, about 1 new review every 2 months (2026: May, July, October) | `listLocalFalconGbpReviews` | Y4 check needs competitor deltas |
| Portal programme dates 03.09.–01.12.2026; memory says start 14.08.2026 | `programs` table, memory praxis-suriya-client | open question O2 |
| `clients.billing` is empty for Suriya | SQL | fee needed for D7 (O3) |
| `leads` has 0 rows; tab "Anfragen" only in staging | SQL, memory portal-leads-crm | GO-SITE and portal go needed |

| Search Console access for `https://suriya-praxis.de/` is gone (403; the property is not in the service-account list; it was granted 01.10.) | `scripts/gsc-client-export.mjs --list`, 2026-10-12 | R5 "nicht lesbar" |
| Profile name in the owner view: "Praxis SURIYA - Nervensystemregulation · Schmerztherapie · Ayurveda-Massage"; Google public: "Praxis Suriya - Ayurveda & Naturheilkunde"; master: "Praxis Suriya" | `getLocalFalconGbpProfile`, `getLocalFalconGbpGoogleUpdates` | R3 (known as H-C-101 in un-burning) |
| Competitors (15.08. → 12.10.): Naturheilpraxis Ingelheim 36→37 reviews, Zentrum Monika Zeller 19→20, Neurologen Ingelheim 21→22, Saurin 8→8, Physio Rhein Nahe 14→14, Suriya 12→13 | Local Falcon scan competitor data + business search | M18, M19 |
| Independent Google search (mobile, 12.10.): heilpraktiker ingelheim place 4, akupunktur place 3, naturheilpraxis place 3, migräne behandlung and schmerztherapie ingelheim not in the top 100 | DataForSEO, 0,07 USD | M23 |

Board coverage check card by card: [tracking-board-coverage-audit.md](tracking-board-coverage-audit.md).

## 19. Open questions

- O1 Answered 12.10.: the 5 proposed keywords are locked.
- O2 Programme start for the quarterly date: 14.08. (memory) or 03.09. (portal)?
- O3 Answered 12.10.: 3.699 € for 90 days = 1.233 € per month.
- O4 Answered 12.10.: the first campaign runs after the cycle reset (about 19.10.).
- O5 GA4 `G-B93S7ZWNNR` is not in the "741 Clients" account: add the service account as viewer (F2).
- O7 Fixes F1–F4 (lead count) need Martin's go, see the coverage audit.
- O8 Search Console access for suriya-praxis.de must be granted again.
- O9 Original scan report links use the neutral domain localrankingtracker.com. The page may show the tool brand. Keep the link (Martin wants sources) or link only our own dated image?
- O6 Form webhook: the Suriya site is edited in parallel by Dinakar; GO-SITE is needed and the form must stay as it is.
