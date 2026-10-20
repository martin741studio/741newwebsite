# Tracking coverage map (v2, after the grilling)

Workflow: Proof Tracking + Quartal (registry id `tracking`, not registered yet).
Date: 2026-10-12. Status: v2 after 5 grilling rounds. Decisions D1–D20 are in [tracking-workflow.md](tracking-workflow.md) section 1.

Legend: ✅ covered · 🟡 partly · ❌ missing. "Asset" = the file, table or tool that exists today.

## Facts found in the homework (read-only, 2026-10-12)

| Fact | Source |
|---|---|
| Local Falcon MCP has GBP read tools: `getLocalFalconGbpPerformanceMetrics` (impressions, calls, website clicks, routes), `listLocalFalconGbpReviews`, `getLocalFalconGbpGoogleUpdates`, `getLocalFalconGbpProfile`. They work only for profiles that are connected in Local Falcon. | MCP `tools/list` |
| Suriya GBP performance (28.06.–23.09.) was pulled through Local Falcon: 1.531 views, 118 routes, 93 website clicks, 6 call clicks. | worktree `admiring-nightingale-f0f882/.../suriya/baseline/BASELINE-REPORT.md` §11 |
| Local Falcon credits: 63 left in the Starter package (7.500 per cycle), 589 usable in total. Cycle ends about 19.10.2026. | `viewLocalFalconAccountInformation` |
| Scheduled scans today: Stürzl campaign monthly (5 keywords, 7×7, 5 mi); Bali Healing autoscan weekly ("ozone therapy"). Dumann and Bali campaigns were one-time. | `listLocalFalconCampaignReports`, `listLocalFalconAutoScans` |
| Falcon Guard watches 0 profiles. | `listLocalFalconGuardReports` |
| Portal `741-portal`: table `scans` has rows for Suriya (10) and Stürzl (8). Table `leads` has 0 rows for all clients. `client_reports` has 1–6 rows per client. | SQL count, read-only |
| GA4: the service account reads all 36 client properties at account level. Search Console: per property; Suriya, Dumann have access, others give 403. | memory google-reporting-api-access, suriya-baseline-tracking, content-pool handover |
| DataForSEO jobs must run from a whitelisted IP (VPS), not from the laptop. | `reporting/citation-monitor.mjs` header |
| No call tracking exists for any client. | grep, memory |

## Board 5 · Beweis zum Nachprüfen

| Board item | Status | Asset today | Data access | Gap |
|---|---|---|---|---|
| Messung echter Leads | 🟡 | portal `leads` table + tab "Anfragen" (staging, Stürzl, 0 rows); GBP call clicks via Local Falcon; GA4 `generate_lead` only on 741.studio | GBP: Local Falcon (connected profiles only). Website forms: GA4 per client, quality varies (see `physiokraft-tracking-fix.md`). Phone and mail leads: only the client knows them. | No lead count per client per week. No form or call event standard on client sites. |
| Filterung von Spam-Anrufen (CallRail) | ❌ | none | CallRail is US-first. DACH providers exist (to check after the grilling). GBP call clicks have no spam filter. | Provider, consent and NAP rule not decided. |
| Kosten pro gebuchtem Auftrag | ❌ | `leads.Mandatswert` field (staging); manual ad cost in `monthly-client-report.mjs` (Kamil) | Booked jobs and revenue: only the client. Fee: 741 invoices. Ad spend: Google Ads / Meta. | No booked-job input, no formula, no rule for missing data. |
| Raster-Scans | ✅ | `ranking-tracking-master-prompt.md`; Local Falcon; table `scans` | Local Falcon MCP (scans cost credits, reports are free) | Only 2 clients have a schedule. |
| Lückenlose Konsistenz | 🟡 | master prompt rule "same 5 keywords" | Local Falcon campaigns keep settings fixed | Radius drifted (Stürzl 5 km vs 5 mi). No locked scan config per client. |
| Keine Vanity-Keywords | 🟡 | master prompt step 1 (keyword must match the real service); memory keyword-must-match-service | DataForSEO volume, GSC | No locked keyword list per client with date and reason. |
| Roh-Screenshots statt Agentur-Dashboards | 🟡 | Suriya GBP raw JSON; dated grid images | Local Falcon (data), Chrome screenshot of the client's GBP (image) | No routine for dated raw screenshots. |
| Unabhängiges SERP-Tracking | 🟡 | master prompt step 3 (DataForSEO SERP, manual) | DataForSEO (VPS IP) | Not scheduled. |
| Kunden-Prüfung im Google-Profil | ❌ | none | The client opens own GBP "Leistung" view | No client guide "so prüfst du die Zahlen selbst". |
| Laufende Velocity-Prüfung | 🟡 | playbook §11 "Bewertungs-Analyse monatlich"; Local Falcon reviews analysis | `listLocalFalconGbpReviews` (own, connected); competitor review counts from scan competitor data | No stored monthly count vs top competitors. |
| Frühwarnsystem bei Engpässen | ❌ | none | all sources above | No thresholds, no alert. |
| Schneller Asynchron-Support | ✅ | portal support chat (`messages`); standup shows unread messages | Supabase | — |
| Wöchentliche Looms & Claude-PDFs | ❌ | monthly GA4 HTML report (Kamil only); weekly-mail cron stopped | — | No weekly client report. |
| Ungefilterte Roh-Walkthroughs | ❌ | Loom by hand | — | No rhythm, no checklist. |
| Monatliche Strategie-Calls | ❌ | not in the system | calendar | No record, no agenda. |
| Kernprinzip: nie im Unklaren | 🟡 | portal activity feed; daily standup | Supabase | No "last update to client" check. |
| Automatisierte KI-Frühwarnsysteme | 🟡 | daily standup flags (programme state); citation-monitor (NAP, needs VPS); Supabase keepalive | — | No metric watch. |
| Sofortige Benachrichtigung | 🟡 | Resend `alerts@741.studio` planned (automation-build); Telegram bot `@Socials741_bot` | Resend, Telegram | No alert wiring for metrics. |
| Abgleich von Leads und CRM | ❌ | portal `leads` (staging) | client CRMs differ (Stürzl: none) | No reconciliation step. |
| KI-Agenten für Finanz-Reconciliation | ❌ | invoicing memory (741 side only) | — | No booked-job ↔ revenue check. |

## Board 6 · Die Quartals-Strategierunde

| Board item | Status | Asset today | Data access | Gap |
|---|---|---|---|---|
| Wer hat Boden gutgemacht / verloren / ist neu | 🟡 | Local Falcon competitor report per scan; audit competitor block; content-pool competitors | Local Falcon (free reads), DataForSEO | No quarter-to-quarter diff. |
| Welche Links wurden aufgebaut | 🟡 | backlink-dach workflow; DataForSEO backlinks | DataForSEO | No quarterly snapshot of competitor and own links. |
| Anpassung an neue Marktlandschaft · Reaktionsprüfung | ❌ | none | — | No decision log that checks last quarter's actions. |
| Ranking-Sättigung | 🟡 | scan trend (SoLV, ATRP) | Local Falcon trend reports | No saturation rule. |
| Content-Sättigung | 🟡 | GSC exports; content pool | GSC (per property) | No rule. |
| Entfernungs-Grenze & Autoritäts-Plateau | 🟡 | grid images | Local Falcon grid points | No metric "radius where rank drops". |
| Kapazitäts-Check | 🟡 | audit asks capacity once | client | No quarterly recheck. |
| Inhalte stutzen · verdoppeln · Refresh | 🟡 | GSC page data; content pool; content-writing revise mode | GSC | No candidate list per quarter. |
| Neue Geopockets | 🟡 | weak grid cells | Local Falcon | No CRM geo data. |
| CRM-Daten-Abgleich | ❌ | none | client CRM | — |
| Zusätzliche GBPs / Gewerbe-Expansion | ❌ | maps-playbook gates (partly) | — | No expansion check. |
| Standort-Recherche · saubere Verifizierung · Syndizierung vor Verifizierung · Review-Verteilung & Wirtschaftlichkeit | 🟡 | un-burning white-hat verification rule; citations module (44 DACH directories) | Supabase, BrightLocal | No location-prep template. |
| Saison-Aktionen 2–3 Quartale voraus | ❌ | none | DataForSEO volume history; GSC | No season radar. |
| PPC- & Keyword-Feinabstimmung | 🟡 | Google Ads (Kamil, Bali); Meta tab | Ads APIs | Not linked to the quarter. |
| Demografische Trends & lokale Gegebenheiten | ❌ | none | public data | — |
| Algorithmus-Updates & KI-Trends | 🟡 | Local Falcon AI scans (SAIV); SEO knowledge base | Local Falcon, library | No quarterly digest. |

## Summary

- Strong today: grid scans, raw GBP data through Local Falcon, async support, programme standup.
- Weak today: real leads, booked jobs, cost per booked job, CRM reconciliation, client-facing rhythm, early warnings, quarterly diffs.
- Biggest blocker: data that only the client has (phone leads, booked jobs, revenue). The second blocker: Local Falcon credits (63 left in this cycle).

## After the grilling: how version 1 closes each gap

| Board item | v1 answer (decision) | Metric ids |
|---|---|---|
| Messung echter Leads | form webhook → portal `leads` + client entries for phone/mail (D5) | M05–M07 |
| Spam-Filterung (CallRail) | no call tracking in v1; client marks spam / "passt nicht" in the lead tab (D4) | M07 |
| Kosten pro gebuchtem Auftrag | (741 fee + ads) / booked jobs; empty when data is missing (D6, D7) | M08–M12 |
| Raster-Scans · Lückenlose Konsistenz · keine Vanity-Keywords | monthly Local Falcon campaign with a locked config and 5 locked keywords (D9) | M13–M16 |
| Roh-Screenshots · unabhängiges SERP · Kunden-Prüfung | proof layer with source line per number, dated grid images, raw JSON, guide "So prüfst du die Zahlen selbst", monthly DataForSEO check | M23, proof layer |
| Velocity-Prüfung · Frühwarnung bei Engpässen | daily review pull, monthly competitor delta, rule Y4 | M17–M19 |
| Asynchron-Support · Looms · Roh-Walkthroughs · nie im Unklaren | portal chat; weekly card released by Martin + raw Loom (D8, D18); rule Y8 | M29 |
| Monatliche Strategie-Calls | only on request (D15); notes in the decision log | — |
| KI-Frühwarnsysteme · sofortige Benachrichtigung | rules R1–R6 by email, Y1–Y9 in the standup (D10–D12) | M24–M28 |
| Abgleich Leads und CRM · Finanz-Reconciliation | monthly agent reconciliation; fee check against the 741 invoice | M05–M12 |
| Board 6 (all groups) | quarterly pack built from tracked data, agent draft T-5, Martin edits, portal page + decision log (D13, D14) | spec section 11 |

Still missing after v1 (by decision): call tracking numbers, CRM sync for external CRMs, scheduled DataForSEO, automatic AI-visibility and backlink tracking between quarters.
