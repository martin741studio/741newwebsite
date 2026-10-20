# Evidence index: Praxis Suriya dry run (as of 2026-10-11)

Read-only run. No write to Drive, Supabase, site, GBP or portal. Type = live, scan or document. Age is counted from the date to 2026-10-11.

| Source | Ref | Type | Date | Age (days) | Measures supported |
|---|---|---|---|---|---|
| S01 | 00_project/maps-playbook-measure-catalog.json — Catalogue v0.1.0 (rule source: niche rules, gates, status rules) | document | 2026-10-11 | 0 | G01, G04, G10, G11, G13, G16, O07, O11, O12, O13, O15, O17, W24 |
| S02 | /Users/martindrendel/.claude/projects/-Users-martindrendel-741website/memory/praxis-suriya-client.md (SOURCE OF TRUTH block, locked 02.09., updates to 10.10.) — Memory: locked NAP, categories, services, boundaries, decisions | document | 2026-09-08 | 33 | G03, G05, G07, G08, G09, G10, G16, G21, O09, O11, O13, W13, W26 |
| S03 | Supabase 741-portal client_locations id cfec507f-81f3-461e-afc2-ad02961410ef — Master NAP row, nap_status locked 2026-09-02 (still holds old name and Faszientherapie) | document | 2026-09-02 | 39 | G01, G02, G06, G08 |
| S04 | Supabase 741-portal client_master_data client_id 3f71ef33-8c74-4ea1-b2d3-0273c2e99649 — Master data row (old name, www host, 'Nervenregulationsmassage ohne Öl') | document | 2026-09-02 | 39 | none (read, not needed) |
| S05 | Supabase 741-portal client_citations (56 rows) + directories — 31 rows 'live', 25 planned; 1 row has listing_url; last_checked 2026-09-30 is a bulk stamp | document | 2026-09-30 | 11 | O01, O02, O03, O04 |
| S06 | Supabase 741-portal scans, maps scans report_keys 9b942025edb71d0, ae5ddc4676cabd7, dc3220cfb36ede2, 97071ac0503b0eb, cf58fb272adc758, ffdbed859265703, 4dbf7b0b1fd55fc — Local Falcon baseline scans 15./16.08.2026 | scan | 2026-08-15 | 57 | none (read, not needed) |
| S07 | Supabase 741-portal scans, ai_baseline report_keys 2f91c5b0a241a41 (ChatGPT 77.78%), b533aa3d9ec1256 (AI Overviews 0%) — AI visibility baseline, one prompt, 9 points | scan | 2026-08-15 | 57 | O20 |
| S08 | Supabase 741-portal tasks (client 3f71ef33...) 45 rows — 90-day task list; many weeks 1-6 closed in bulk on 2026-09-21 (claims, not proof) | document | 2026-09-21 | 20 | G09, G12, G14, O04, W01, W11, W30 |
| S09 | Supabase 741-portal access_grants (8 rows) — GBP, GA4, GSC, WP access granted | document | 2026-08-17 | 55 | none (read, not needed) |
| S10 | Supabase 741-portal client_reports (6 rows) — Report pages list; Stammdaten page 2026-09-03 | document | 2026-09-03 | 38 | none (read, not needed) |
| S11 | Supabase 741-portal visibility_prompts / visibility_results / visibility_summary (0 rows) — SELECT today: no AI prompts stored for this client | live | 2026-10-11 | 0 | O20 |
| S12 | https://clients.741.studio/r/8dbd937730d2/praxis-suriya-woche1-2026-08.html — Week-1 report (state of 14.08.: 7 photos, last post 07.07., PSI 1.3 s, old hours) | document | 2026-08-14 | 58 | G09, G10, G12, G17, G18, W01 |
| S13 | Drive 1aLjDeuHWP5QUlezjnbSwFvJcPqX9PnyZJJgG2zHkpfk (Änderungsprotokoll GBP + Website) — GBP changes 23.08.: description 669 chars, hours, 23 services, 5 categories | document | 2026-08-23 | 49 | G05, G06, G07, G08 |
| S14 | Drive 1fmn3ZbPwyzT-CXJb-l9n0UOFUkBeUcNd9xWC_v3CAN4 (Coralie_Suriyapperuma_Analyse) — Original analysis sheet of 20.07. (old hours, no schema, no reviews) | document | 2026-07-20 | 83 | none (read, not needed) |
| S15 | Drive 1MGNd-AiY9MC12FvZMhK1IC5Lbk6CkTiWtF9ISLHZK8E (Suriya Praxis, page/meta list) — Dinakar page list with meta data, 31 pages | document | 2026-09-29 | 12 | none (read, not needed) |
| S16 | Drive 1ogvG1qphDcwhIp4cgNy8F8etenIvXoCbrlplWEcO9pI (LinkedIn und Kollaborations-Outreach v1) — Partner outreach plan (article swap, link in return); not yet sent | document | 2026-09-21 | 20 | O06, O17 |
| S17 | Drive 1uqGjjDYpRDu3o81KgpkY55JFBjRiyNW-xgfdzR0rm30 (Keyword & SEO Matrix) — Listed only, content not read (not needed for any status) | document | 2026-08-28 | 44 | none (read, not needed) |
| S18 | https://suriya-praxis.de/ (curl, 2026-10-11) — Homepage: H1, title, meta, JSON-LD MedicalBusiness, Trustindex widget 12 reviews, form, WhatsApp, GTM | live | 2026-10-11 | 0 | G02, G03, G04, G14, G17, W02, W06, W07, W08, W20, W23, W24, W27, W32, W33 |
| S19 | https://suriya-praxis.de/impressum/ (curl, 2026-10-11) — Imprint: name, address, phone, VAT placeholder, social handles | live | 2026-10-11 | 0 | G01, G02, O07, W33 |
| S20 | https://suriya-praxis.de/termin-buchen/ (curl, 2026-10-11) — Booking page: 4 H1, no meta description, form | live | 2026-10-11 | 0 | none (read, not needed) |
| S21 | https://suriya-praxis.de/robots.txt, /sitemap_index.xml, /page-sitemap.xml, /llms.txt (curl, 2026-10-11) — robots ok, sitemap 54 pages, llms.txt 404 | live | 2026-10-11 | 0 | G08, W09, W12, W13, W16, W29, W30, W35 |
| S22 | https://suriya-praxis.de/heilpraktikerin-ingelheim/ , /ayurveda-therapie/ , /massage-ingelheim/ (curl, 2026-10-11) — Spot pages: schema, H1, alt, map | live | 2026-10-11 | 0 | none (read, not needed) |
| S23 | 00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/evidence/area_d/crawl-sitemap.json + pages/*.html (un-burning crawl, 54 sitemap pages, UB.D01-D07) — Crawl of all sitemap URLs 2026-10-11T01:22-01:25 (+02:00); parsed by this run for H1, meta, alt, FAQ, trust, map, form | live | 2026-10-11 | 0 | O08, W07, W09, W10, W16, W21, W22, W23, W26, W27, W28, W31, W32, W34 |
| S24 | 00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/evidence/area_c/listings/ + listing-fetch-status.json (un-burning listing fetches, UB.C04) — Live fetch of 20 listing URLs 2026-10-11T01:31 | live | 2026-10-11 | 0 | O02, O19 |
| S25 | 00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/nap-corrections.json (UB.C04: 16 listings, 32 corrections, strict NAP match 0 percent) — Un-burning NAP check; no harm register file exists yet, so no harm row IDs | live | 2026-10-11 | 0 | G01, G02, G20, G22, O01, O02, O03 |
| S26 | 00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/nap-master.json (UB.C01) — Un-burning master NAP and 4 conflicts inside master sources | document | 2026-10-11 | 0 | G22 |
| S27 | 00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/index-intended.json (UB.E02: 64 ok, 7 index_unwanted, 1 index_missing, 3 decision_needed, 44 unverified) — Indexed vs intended | live | 2026-10-11 | 0 | O05, W34 |
| S28 | 00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/link-plan.json (UB.E04: 32 of 54 pages without link to parent, 49 missing links) — Inverted-tree link plan | live | 2026-10-11 | 0 | W15, W18, W19 |
| S29 | 00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/evidence/area_e/inspect-results.json (GSC URL Inspection, 25 URLs) — Index state per URL, collected 2026-10-10T23:28Z; rich results: breadcrumbs + review snippets PASS on / | live | 2026-10-10 | 1 | W02, W33 |
| S30 | 00_project/assets/un-burning/praxis-suriya/baseline/BASELINE-REPORT.md (sections 11-13: GBP state 30.09., 12 reviews, name change pending) — GBP name still with suffix, hours Mo-Sa 07:30-20:00, 5.0 stars, 12 reviews; requests are counted nowhere | document | 2026-09-30 | 11 | G01, G02, G04, G17, O18, O19, W13, W25, W33 |
| S31 | 00_project/assets/un-burning/praxis-suriya/baseline/2026-10-01-gbp-performance.json (Local Falcon GBP performance, pulled 2026-10-01) — Views, calls, directions, website clicks 28.06.-27.09. | live | 2026-10-01 | 10 | none (read, not needed) |
| S32 | 00_project/assets/un-burning/praxis-suriya/baseline/internal-linking-audit-2026-10-10.md — Content-link audit of 89 URLs (blog out-links 0, city pages 1 inbound, sidebars) | live | 2026-10-10 | 1 | W08, W18, W19 |
| S33 | 00_project/coralie-aggregator-pack.md — Aggregator pack: OLD name with suffix, OLD hours Di-Fr 09-19 | document | 2026-08-25 | 47 | O04 |
| S34 | 00_project/coralie-brightlocal-brief.md — BrightLocal brief: old name 'Praxis Suriya – Ayurveda & Naturheilkunde', hours 09-19, 15 directories | document | 2026-08-25 | 47 | none (read, not needed) |
| S35 | 00_project/coralie-submission-runbook.md — Runbook: old name 'Praxis Suriya - Ayurveda & Naturheilkunde', 22 self-submit directories | document | 2026-08-26 | 46 | none (read, not needed) |
| S36 | 00_project/loop-signals-playbook.md — Loop-signal rules (image names, geotag, co-citation) | document | 2026-08-26 | 46 | none (read, not needed) |
| S37 | 00_project/gbp-visibility-blueprint.md — Targets: 1+9 categories, 20-50 services, 40-60 keywords, 10-30 AI prompts | document | 2026-08-20 | 52 | G07 |
| S38 | reporting/night-shift/2026-10-06/feedback/praxis-suriya/ and 2026-10-09/ (drafts) — Night-shift drafts still use Di-Do 07:30-18:00 hours (client note of 17.08.) | document | 2026-10-09 | 2 | G05, G21 |
| S39 | https://www.googleapis.com/pagespeedonline/v5/runPagespeed (free, 1 call 2026-10-11) — HTTP 429 quota exceeded, no result | live | 2026-10-11 | 0 | W01 |
| S40 | 00_project/startseite-money-page-standard.md (section E: 11 checks) — SMP checklist E | document | 2026-09-13 | 28 | W06 |
| S41 | 00_project/un-burning-workflow.md — Un-burning spec: check ids UB.A01-E05, harm classes | document | 2026-10-11 | 0 | G19 |
| S42 | 00_project/maps-playbook-design-note.md — Status and age semantics | document | 2026-10-11 | 0 | none (read, not needed) |
| S43 | /Users/martindrendel/.claude/projects/-Users-martindrendel-741website/memory/suriya-elementor-dinakar-set.md, suriya-conversion-paths-must-stay.md, suriya-ayurveda-massage-page-untouchable.md, suriya-baseline-tracking.md, no-review-answering.md — Memory: page set, menu, conversion paths, untouchable page 1511 | document | 2026-10-07 | 4 | G13, G18, W02, W03, W08, W15, W20, W25 |
| S44 | 00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/evidence/area_c/listings/EV-C-listing-allgemeine-zeitung.html (article dated 2023-09-28, link to suriya-praxis.de) — Local press article, link live when fetched 2026-10-11; article date 2023-09-28 | live | 2026-10-11 | 0 | O09 |
| S45 | 07_social/templates/bewertungs-anleitung/suriya-bewertungs-anleitung.pdf (+ suriya-bewertung-whatsapp.png) — Review guide with QR (writereview placeid link) | document | 2026-09-04 | 37 | G14, G15 |
| S46 | Local Falcon MCP (listAllLocalFalconLocations, listLocalFalconScanReports, getLocalFalconReport): NOT connected in this session — Tool missing; all live GBP field reads unavailable | live | 2026-10-11 | 0 | G03, G06, G11, G18 |
| S47 | Search of repo, Drive folder 1Hg7S3n1HyZmYmk4HLFmWfdTDtbI9NBis and Supabase for monitor, CRO prototype, content pool, sponsor, watch artefacts (2026-10-11) — Absence search: no such artefact found for Suriya | live | 2026-10-11 | 0 | G19, G20, G22, O05, O06, O08, O10, O12, O15, O16, O17, O18, O19, W03, W04, W05, W09, W11, W12, W14, W17 |
| S48 | /Users/martindrendel/.claude/projects/-Users-martindrendel-741website/memory/praxis-suriya-client.md section 'Stand 01.10.2026 (Entscheidungen)' (GBP name stays, tax ID stays) — Martin decision 01.10.: GBP name stays as is; imprint tax ID not to be raised again | document | 2026-10-01 | 10 | G01 |
| S49 | 00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/evidence/area_c/listings/EV-C-listing-golocal.html (+ jameda, aerzte-de, theralupa-*, infobel-*, work5) — Listing pages as fetched (phones 06132 ..., old names) | live | 2026-10-11 | 0 | O01 |
| S50 | Supabase 741-portal scans, backlinks_manual report_key ahrefs-free-2026-08-15 (Ahrefs Free, Martin) — DR 5, 575 backlinks, 430 domains, 6 quality links | scan | 2026-08-15 | 57 | O14 |

## Drive files used (all read only)

| Drive file id | Title | Read | Used for |
|---|---|---|---|
| 1aLjDeuHWP5QUlezjnbSwFvJcPqX9PnyZJJgG2zHkpfk | Änderungsprotokoll (GBP + Website) | yes | G05-G08 |
| 1fmn3ZbPwyzT-CXJb-l9n0UOFUkBeUcNd9xWC_v3CAN4 | Coralie_Suriyapperuma_Analyse | yes | background only (old state 20.07.) |
| 1MGNd-AiY9MC12FvZMhK1IC5Lbk6CkTiWtF9ISLHZK8E | Suriya Praxis (page/meta list) | yes | W09, W34 context |
| 1ogvG1qphDcwhIp4cgNy8F8etenIvXoCbrlplWEcO9pI | LinkedIn und Kollaborations-Outreach v1 | yes | O06, O09, O17 context |
| 1uqGjjDYpRDu3o81KgpkY55JFBjRiyNW-xgfdzR0rm30 | Keyword & SEO Matrix | listed only | none |
| 1Hg7S3n1HyZmYmk4HLFmWfdTDtbI9NBis | Client folder (listed, 12 docs, 1 sheet, 1 image folder) | listed | find audit docs: none exist from the audit workflow |

## Not available in this session

- Local Falcon MCP tools (list locations, list reports, get report): not connected. All live GBP field reads set to unknown or stale.
- Ahrefs and paid DataForSEO: not used (rules). PageSpeed API: quota error.
- Audit run for Suriya: does not exist. Audit fields B04-B13 are therefore missing.
- Harm register of the un-burning chat: not present yet; no harm row IDs. Cited their result files instead (S25-S29).
