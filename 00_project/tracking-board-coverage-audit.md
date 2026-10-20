# Board coverage audit: every card vs what the client really sees

Date: 2026-10-12. Trigger: Martin: "really check if we cover all points of the two boards; competitors are difficult to see; more is missing".
Method: I compared each card on board 5 and board 6 with the spec and with prototype v1 (what is visible on the page, not only what the spec says).
Result v1: the spec named every card, but the prototype showed only 9 of 25 board-5 cards and 1 of 25 board-6 cards. Competitors were one footnote line.

Status: ✅ visible in prototype v2 with real data · 🟡 visible, data starts after a go or after the next scan · ❌ not visible.
Every row in v2 has a source link ("Quelle öffnen") so the reader can go to the original.

## Board 5 · Beweis zum Nachprüfen (25 cards)

| # | Card | v1 | v2: where in the tab | Real data in v2 (source link) |
|---|---|---|---|---|
| 5.1 | Anrufe statt Ranking-Mythen (group) | 🟡 | Section 1 "Anfragen und Termine" comes first, rankings later | — |
| 5.2 | Messung echter Leads | ❌ "fehlt" | Tile "Anfragen" + section 1 table per channel (Formular, WhatsApp, Telefon-Klick, Google-Anruf, eingetragen) | Google calls: real (Google profile). Form, WhatsApp and phone clicks: the site already sends `s741_form_submit`, `s741_whatsapp_click`, `s741_phone_click`; nobody stores them yet (see fix F1). |
| 5.3 | Filterung von Spam-Anrufen | ❌ | Section 1: column "davon Spam / passt nicht" | Client marks spam in "Anfragen". No call tracking in v1 (D4). |
| 5.4 | Kosten pro gebuchtem Auftrag | ❌ | Tile + section 1 "Rechnung" line: 3.699 € / 90 Tage = 1.233 € pro Monat ÷ gebuchte Termine | Fee real (Martin 12.10.). Booked jobs only from Coralie (no booking system on the site). |
| 5.5 | Koordinaten-genaue Kartensichtbarkeit (group) | ✅ | Section 3 "Google Maps" | Maps measurement 15./16.08. |
| 5.6 | Raster-Scans | ✅ | Section 3 table + dated grid images | link to each original scan report |
| 5.7 | Lückenlose Konsistenz | ❌ | Section 3 box "Messregeln": same 5 search terms, 49 points, 5 km, monthly, change log | locked config (tracking-metric-catalog.json) |
| 5.8 | Keine Vanity-Keywords | ❌ | Section 3: each term with "warum dieser Begriff" (real searches, real service) | DataForSEO volume + service list |
| 5.9 | Unverfälschte Belege & Drittanbieter-Daten (group) | 🟡 | Section 5 "Belege" | — |
| 5.10 | Roh-Screenshots statt Agentur-Dashboards | ❌ | Section 5: dated raw screenshots of her Google profile "Leistung" view, unedited | Chrome screenshot per month (manual step in the Loom run) |
| 5.11 | Unabhängiges SERP-Tracking | ❌ | Section 4 "Normale Google-Suche": place per term + link to the same search | DataForSEO 12.10.: place 4 / – / – / 3 / 3 |
| 5.12 | Kunden-Prüfung im Google-Profil | ✅ | Section 5 guide "So prüfst du es selbst" + link | Google profile |
| 5.13 | Bewertungs-Metriken & Geschwindigkeit (group) | 🟡 | Section 2 "Mitbewerber" + tile | — |
| 5.14 | Laufende Velocity-Prüfung | ❌ | Section 2 "Bewertungs-Rennen": total and new since the last measurement, per competitor | 15.08. → 12.10.: Suriya +1 (12→13), Naturheilpraxis Ingelheim +1 (36→37), Zentrum Monika Zeller +1 (19→20), Saurin 0, Physio Rhein Nahe 0 |
| 5.15 | Frühwarnsystem bei Engpässen | ❌ | Section 6 "Was wir für dich überwachen": each guard with last check and status | rules R1–R6, Y1–Y9 |
| 5.16 | Kommunikations-Kadenzen & Berichts-Formate (group) | 🟡 | Section 7 "So halten wir dich auf dem Laufenden" | — |
| 5.17 | Schneller Asynchron-Support | ❌ | Section 7: link to the portal chat, reply promise | portal chat |
| 5.18 | Wöchentliche Looms & Claude-PDFs | 🟡 | Weekly card + Loom (no PDF, D3) | — |
| 5.19 | Ungefilterte Roh-Walkthroughs | 🟡 | Loom = unedited walk through her own profile and the grid | — |
| 5.20 | Monatliche Strategie-Calls | ❌ | Section 7: "Gespräch auf Wunsch" (D15) + log of past talks | decision log |
| 5.21 | Kernprinzip: nie im Unklaren | ❌ | Section 7: date of last update, next update, timeline of all updates | tracking_cards |
| 5.22 | Dauerhafte Überwachung & automatisierte Frühwarnung (group) | ❌ | Section 6 | — |
| 5.23 | Automatisierte KI-Frühwarnsysteme | ❌ | Section 6 list (website, form, profile data, verification, reviews, tracking) | edge-function checks |
| 5.24 | Sofortige Benachrichtigung | ❌ | Section 6 line: "Bei einem roten Befund weiß Martin es am selben Tag" | alert email |
| 5.25 | Die Attributions-Kette (group) + Abgleich Leads/CRM + KI-Finanz-Reconciliation | ❌ | Section 1 chain graphic: Sichtbarkeit → Kontakt → Anfrage → Termin → Wert, with the gap per step | monthly reconciliation |

## Board 6 · Die Quartals-Strategierunde (25 cards)

In v1 only a 5-line teaser existed. In v2 the tab has a page "Quartalsrunde" (prototype section 8). It shows every card with a status:
- "gesammelt": data exists
- "sammeln läuft": data is collected
- "zur Entscheidung": a question for the meeting

| # | Card | Data source, collected continuously | Status 12.10. |
|---|---|---|---|
| 6.1 | Wer hat Boden gutgemacht und warum? | competitor top-3 share + rank per scan; review delta; categories | 1 scan (15.08.) → comparison after the next scan |
| 6.2 | Wer hat Boden verloren oder ist verschwunden? | same, diff of the top-10 lists | sammeln läuft |
| 6.3 | Wer ist neu eingetreten oder wurde übernommen? | new place ids in the top 10; name changes | sammeln läuft |
| 6.4 | Welche Links wurden aufgebaut? | referring domains own + top 3 (quarterly snapshot) | first snapshot in the quarterly run |
| 6.5 | Anpassung an die neue Marktlandschaft | decision log | zur Entscheidung |
| 6.6 | Reaktionsprüfung | decision log: done? effect? | first round = baseline |
| 6.7 | Ranking-Sättigung | terms with top-3 share ≥ 90 % (ayurveda 47/49, akupunktur 45/49) | gesammelt |
| 6.8 | Content-Sättigung | pages with impressions but no clicks (GSC) | sammeln läuft |
| 6.9 | Entfernungs-Grenze & Autoritäts-Plateau | grid edge cells where rank falls (heilpraktiker: found in 49/49 but top 3 in 38/49) | gesammelt |
| 6.10 | Kapazitäts-Check | client question: free slots per week (max 12–16 patients) | question in the portal |
| 6.11 | Inhalte stutzen | pages without clicks in 90 days | sammeln läuft |
| 6.12 | Verdoppeln | pages and terms that grow | sammeln läuft |
| 6.13 | Content-Refreshes statt blinder Neuerstellung | losing pages with old content | sammeln läuft |
| 6.14 | Neue Geopockets | routes and lead towns; weak grid cells; Bingen, Mainz, Wiesbaden | sammeln läuft |
| 6.15 | CRM-Daten-Abgleich | lead table vs Coralie's bookings | starts with "Anfragen" |
| 6.16 | Zusätzliche GBPs / Standorte | decision question, only with demand data | zur Entscheidung |
| 6.17 | Gewerbe-Expansion | new services with demand (content pool) | zur Entscheidung |
| 6.18 | Standort-Recherche | only if 6.16 = yes | — |
| 6.19 | Saubere statt riskante Verifizierung | rule: real address, video verification (un-burning rule) | rule |
| 6.20 | Off-Page-Vorbereitung (Syndizierung vor Verifizierung) | listing plan before verification | template |
| 6.21 | Review-Verteilung & Wirtschaftlichkeitsrechnung | reviews needed per location × cost per booked job | template |
| 6.22 | Vorausplanung von Saison-Aktionen | 24-month search volume per term | quarterly run |
| 6.23 | PPC- & Keyword-Feinabstimmung | ads account (none today) + terms not reachable organically (migräne behandlung: not in top 100, info results + AI overview) | gesammelt |
| 6.24 | Demografische Trends & lokale Gegebenheiten | public data (population, age 45–65 women share) | quarterly run |
| 6.25 | Algorithmus-Updates & KI-Trends | AI answers (ChatGPT recommended the practice 7/9 points on 15.08.; Google AI overview 0/9); AI overview on 2 of 5 terms (12.10.) | gesammelt |

## Additional gaps found (not on the boards, but needed)

- G1 Source link per number: added (Martin 12.10.).
- G2 Competitor names: v1 used short labels ("Ternes", "ZAM"). v2 uses the exact profile names from Google.
- G3 The Google profile name still shows the old long name "Praxis Suriya - Ayurveda & Naturheilkunde" in the search result (12.10.); master = "Praxis Suriya". Feeds rule R3 (profile vs master).
- G4 Lead events already exist on the site but are not stored anywhere readable (only two Google Ads conversion tags). Fix F1.
- G5 The GA4 property `G-B93S7ZWNNR` is not visible to the service account (not in the "741 Clients" account). Fix F2.

## Fixes that need Martin's go

- F1 GTM container `GTM-K9MDDN7P`: add one GA4 event tag for the three existing events (form, WhatsApp, phone click). No site code change. Then the tab counts all inquiry clicks automatically.
- F2 Add `reporting-bot@studio-apis-503306.iam.gserviceaccount.com` as viewer to the GA4 property of suriya-praxis.de (or move it into "741 Clients").
- F3 Read Fluent Forms entries (form requests) read-only from WordPress as the exact count of form inquiries (cross-check for F1).
- F4 Booked appointments: there is no booking system. Coralie ticks "gebucht" in "Anfragen" (D5). Alternative: she marks the Fluent Forms entry; we read the status.
