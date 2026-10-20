# FIX-F report: ST-40, ST-41, ST-42, ST-33 (2026-10-11)

Basis: REVIEW-F.md, content-writing-stuerzl-fixes.md, content-writing-stuerzl-batch.md. Nothing is live. Only the four page folders and this file were changed. Backups: `05-final/page-vorreview.md` in each folder. New drafts: `03-draft/draft-v3.md`.

## Summary table

| Page | Words (was) | Seller layer (limit 550) | Answer block | G1 to G6 | Cleanse calls | Visible placeholders (was) |
| --- | --- | --- | --- | --- | --- | --- |
| ST-40 Kontakt | 776 (771) | 548 | 44 words, 3 sentences | PASS | 1 (no change, diff pass) | 1 (5) |
| ST-41 Standort Frankfurt | 822 (1021) | 539 | 43 words, 3 sentences | PASS | 1 (one line taken, diff pass) | 0 (3) |
| ST-42 Standort München | 796 (906) | 549 | 44 words, 4 sentences | PASS | 1 (not taken: diff failed, see below) | 0 (2) |
| ST-33 Aktuelles | 98 (51) | 98 | 54 words, 4 sentences | PASS | 0 (only 98 words, lint 5/5) | 0 (0) |

Link network (copy of all 30 pages in the scratchpad, the shared `LINK-NETWORK.md` was not touched): highest 5-word overlap of my pages is 17 % (ST-40 with ST-44). ST-40/ST-41 14 %, ST-41/ST-42 15 %, ST-40/ST-42 16 % (limit 25 %). Before: ST-40/ST-41 would have been 27 % after the new address block and list, so I reworded the NAP, cost, confidentiality and hedge sentences page by page (Fixes §2.10). One open warning outside my scope: ST-33 has only 1 incoming text link from other written pages (the menu and the start page link to it).

G4 warns for one long sentence on ST-41 and ST-42 (the § 388 Abs. 1 AO text). I kept it: it follows the saved law text word for word.

The Cleanse on ST-42 changed the postal code of Frankfurt in the address block to 60331 and the hero. `diff_claims.py diff` failed (new number, lost required claim C23). I did not take it. Files: `03-draft/cleansed-v3.md` and `cleanse-notes-v3.txt` in each folder.

## Decisions for this batch (points 1 to 6 of the order)

1. **Services per office:** One neutral list "Unsere Leistungen" (six areas of the approved start page, section 4) is on ST-40 (S04), ST-41 (S04) and ST-42 (S04), same words and same links. Hedge on the search item: "Beratung, Begleitung vor Ort im Einzelfall". The old office-specific lists (Compliance and Zollstrafrecht only in Munich) are gone. Flag in OPEN-FLAGS A7 or A8 and in `placeholders.md` item 1 or 5: the firm must say what each office does.
2. **"sechs Finanzämter" in ST-41:** Cut. The claim rested on a data-protection notice. New fact, from a Finanzamt directory: the Finanzamt Frankfurt am Main has its address at Gutleutstraße 118 bis 124, 60327 Frankfurt am Main, about 5 minutes on foot from Hauptbahnhof (Ausgang Süd). Source: https://finanzamt.hessen.de/Frankfurt and the list https://finanzamt.hessen.de/service/finanzaemter-in-hessen, read 2026-10-11; cross-check frankfurt.de/adressen. Saved in `st-41-standort-frankfurt/_work/finanzamt-frankfurt-verzeichnis.txt`. The directory names no Steuerfahndung and no Bußgeld- und Strafsachenstelle, so the page does not say they sit there. The directory lists two Verwaltungsstellen (Frankfurt, Frankfurt-Höchst), so the text says "seine Anschrift". New finding: the data-protection notice and the city portal still say "Frankfurt am Main I", the directory only "Frankfurt am Main" (OPEN-FLAGS B8). The notice stays only in the FAQ, for the Steuerfahndung sentence, with "Nach den Datenschutzhinweisen …".
3. **Staff:** Same people on ST-40, ST-41, ST-42: Frankfurt = Dr. Anja Stürzl; Munich = Lea Wimmer (Standortleitung) and Dr. Monika Glogger. Source: live contact page, `nap.json` contacts, Source of Truth. **Thorben Hoppe is removed from ST-41** (and was never on ST-40/ST-42). His live profile says "Frankfurt am Main und München", but `nap.json`, the live contact page and the Source of Truth do not name him as contact. Differences to the other agents (not edited): ST-44 names Hoppe (line 43 and line 59 "an beiden Standorten tätig", link `/thorben-hoppe/` is not in `slugs.json`) and Florentine Jilg; ST-43 line 102 says "Thorben Hoppe berät an beiden Standorten"; ST-49 lists the RWS Verlag press item about him. Either the main agent removes him there, or all pages carry him with the live-profile source and one slug. ST-44 line 59 about the offices matches my pages.
4. **Lea Wimmer's title:** The visible text says "Rechtsanwältin und Fachanwältin für Steuerrecht" (live profile title line). The year "seit 2017" is removed. The unconfirmed state is in OPEN-FLAGS A2, `placeholders.md` item 2 and the FLAG comment (not in the visible text). Dr. Glogger's "Zertifizierter Compliance Officer (Univ. Münster)" is handled the same way.
5. **ST-33:** New short CTA block S03 "Vertraulich anfragen" with "Nennen Sie uns nur Ihr Thema, keine Einzelheiten." The intro links `/ratgeber/` and `/kontakt/` (also `/dr-anja-stuerzl/` and `/publikationen/`). OPEN-FLAGS A1 lists the live teaser risk: JUVE-Rankings, "erfolgreiche Gründerin", "Spezialisierung, Personal Brand", and "Influencer*innen … Jetzt vor Strafverfolgung schützen!" (protection promise, fear wording), plus the Capital title and "Kluge Köpfe" as lower risk. It asks for retitling before the CMS list goes live.
6. **Location schema:** Checked. `schema_tool.py make` writes the right addresses for both offices on every page (München: Oberanger 32, 80331 München, +49 89 72444170; Frankfurt: Untermainkai 26, 60329 Frankfurt am Main, +49 69 298028870; no old address). `check` passes. A per-office node is **not possible** with the tool. Needed change (for the main agent, I did not edit the tool):
   - In `make()`, give each `department` entry an `@id` (for example `base + "/#" + L["id"]`, giving `…/#frankfurt` and `…/#muenchen`) and an `areaServed`.
   - Add `contactPoint` (`@type` ContactPoint, `telephone`, `contactType` "customer service", `availableLanguage`) from `nap.json`. No `openingHoursSpecification` (hours are not agreed).
   - For `page_type` location: add `"about": {"@id": <office @id>}` and `"mainEntity": {"@id": <office @id>}` to the WebPage, taken from a new brief field such as `brief.office_id`. For `page_type` contact: set the WebPage `@type` to `ContactPage` and list both offices as `mainEntity`.
   - Add `areaServed` and (once confirmed) `geo` per location to `nap.json`. The firm says "deutschlandweit", so `areaServed` is either `Country: DE` or a list of cities Martin picks.
   - For news hubs (ST-33): add a `CollectionPage` with `hasPart` or `mainEntity` as `ItemList` for the CMS list. Article markup stays with the single posts.
   - `check()`: warn when a location page does not reference its own office node.

## ST-40 Kontakt

| Review point | Result |
| --- | --- |
| 1 H "Wir sind persönlich erreichbar, auch außerhalb der klassischen Bürozeiten" | behoben. Sentence cut. Now: "Termine und Erstberatungen sind auch außerhalb der Telefonzeiten nach Absprache möglich." No 24/7. |
| 2 M Emergency numbers without hours | behoben. Numbers are stated as facts ("nennen wir zwei Notfall-Rufnummern"), no "Sie erreichen uns", no placeholder. Hours question moved to OPEN-FLAGS A2 and `placeholders.md` item 2. |
| 3 M Pauschale without "üblicherweise" | behoben. Cost block of the Fixes file in own words: "nach Zeitaufwand, in Sechs-Minuten-Einheiten", "üblicherweise gegen Pauschale", "Vergütung … zu Beginn des Mandats in Textform". No amount. The amount placeholder is gone. |
| 4 M "Auf Wunsch schreiben wir Ihnen zuerst per E-Mail" | behoben. Cut. Question in `placeholders.md` item 7. |
| 5 M Confidentiality for the inquiry | behoben. FAQ cites § 43a Abs. 2 BRAO ("alles, was ihm in Ausübung seines Berufes bekanntgeworden ist") and § 203 StGB. No statement about inquiries before a mandate. |
| 6 L "Beide Büros sind gleichrangig" | behoben. Cut. |
| 7 L "ich" in four FAQ questions | behoben. All questions use "Sie". |
| 8 L Parking spaces 148 and 146 | behoben. Numbers cut. Question in OPEN-FLAGS B2 and `placeholders.md` item 6. |
| Gap: schema 55 | bewusst offen. Tool limit (see decision 6). The TECH block states the wanted type and nodes. |
| Gap: E-E-A-T, no trust line near the form | behoben. S08: owner Dr. Stürzl, "Fachanwältin für Steuerrecht seit 2021 und Zertifizierte Beraterin für Steuerstrafrecht (DAA) seit 2022" (CV and live profile; no Kammer proof, flag A6) and "Gesetzliche Verschwiegenheit nach § 43a Abs. 2 BRAO". |
| Gap: no Frankfurt public-transport route and no entrance rule | bewusst offen. No source exists for Untermainkai 26 (the live route was for the old address). OPEN-FLAGS B2 and B3. |
| Gap: 5 visible placeholders | behoben. One remains: the consent text for the form (a client fact that does not exist yet). The other four are open questions in `placeholders.md`, the text makes no claim on them. |
| Fixes §2.5 address block | behoben. Three exact lines at the end of S08. |
| Fixes §2.9 | answer block 44 words, seller layer 548. |
| New: S04 neutral services list | added (decision 1). |

## ST-41 Standort Frankfurt

| Review point | Result |
| --- | --- |
| 1 M "sechs Finanzämtern", "Das schreibt die hessische Finanzverwaltung selbst" | behoben und belegt. Cut. Replaced by the Finanzamt directory fact (decision 2). |
| 2 H Services listed as office facts, different from ST-42 | behoben. Neutral list, same on ST-40/41/42 (decision 1). Flag A7. |
| 3 M Thorben Hoppe only from the live profile | behoben. Removed (decision 3). Flag A10, `placeholders.md` item 2. |
| 4 M "Wir begleiten Durchsuchungen und Beschlagnahmen" unconditional | behoben. List item: "Beratung, Begleitung vor Ort im Einzelfall". FAQ: "Eine Begleitung vor Ort hängt vom Einzelfall ab …". |
| 5 M Pauschale wording | behoben. "Für die Erstberatung gilt üblicherweise eine Pauschale", own words, no amount, placeholder gone. |
| 6 L § 386 Abs. 2 only, Abs. 3 missing; § 388 point 2 drops "zur Zeit der Einleitung" | behoben. § 386 Abs. 1 to 3 and § 399 Abs. 1 follow the saved text (Absatz 2 summarised with the reference). § 388 Abs. 1 follows the saved text completely, including "zur Zeit der Einleitung des Strafverfahrens" in points 2 and 3. Abs. 4 was dropped for length. |
| Gap: schema 48 | bewusst offen. Tool limit (decision 6). Address checked: Untermainkai 26. |
| Gap: Einzugsgebiet and Frankfurt route | bewusst offen. The firm says "deutschlandweit"; the 5-km radius and the district list are Martin's Maps priority, not a client statement (OPEN-FLAGS B10). No ÖPNV source for Untermainkai 26 (B3). |
| Gap: no Frankfurt court or Staatsanwaltschaft fact | bewusst offen. No gelesene source (B11). |
| Gap: services and staff unassigned, no photo | bewusst offen. Open questions to the firm; photos are a development task. |
| Fixes §2.1 quote | The quote "Jedes Mandat und jeder Mandant ist anders." has no source line on the page (allowed). |
| Fixes §2.5 address block, §2.9, §2.10 | behoben. Block added, answer 43 words, seller layer 539, text blocks reworded per page. |
| Parking spaces 148 and 146 | Cut (same reason as ST-40). |

## ST-42 Standort München

| Review point | Result |
| --- | --- |
| 1 H Lea Wimmer "Fachanwältin für Steuerrecht" and "seit 2017" | teilweise behoben, bewusst offen. Only the live-profile wording stays, the year is cut. Unconfirmed state in OPEN-FLAGS A2 (action before go-live: written confirmation or BRAK search, else cut the title). |
| 2 H Six services with Compliance and Zollstrafrecht assigned to Munich | behoben. Neutral list (decision 1). Flag A7. |
| 3 M "Beide beraten und verteidigen Privatpersonen und Unternehmen" | behoben. The sentence about client groups now covers the firm only. The persons have their "Rechtsgebiete" in the profile words. |
| 4 M "oft Begleitdelikte" | behoben. The Wirtschaftsstrafrecht card with this text is gone; "oft" no longer appears. |
| 5 L Dr. Glogger as first contact (50 % Teilzeit) | bewusst offen. The live contact page and `nap.json` name her. The text gives no hours. Flag A8 and `placeholders.md` item 3. |
| 6 L Hoppe omitted | behoben. Consistent across ST-40/41/42 (decision 3). |
| 7 M Pauschale wording | behoben. "üblicherweise gegen Pauschale", own words, no amount. |
| Gap: schema 48, no office node | bewusst offen. Tool limit (decision 6). Address checked: Oberanger 32, 80331 München. |
| Gap: catchment and court | teilweise. "Altstadt am Oberanger" added (Source of Truth Tab 09 Z12, flag A10). Other districts and courts have no source (B8, B9). |
| Gap: person titles unproven, no photos | bewusst offen (A2, B5). |
| Cross-page 8: same FAQ "Was tun, wenn die Steuerfahndung in … vor der Tür steht?" | behoben. ST-42 now asks "Gibt es Notfall-Rufnummern für eine laufende Durchsuchung?"; the sections S03 to S05 differ in structure from ST-41. |
| Access text from the firm, not checked with MVV | The text says "Als Haltestellen nennt die Kanzlei …" (flag B3). |
| Fixes §2.5, §2.9 | block added, answer 44 words, seller layer 549. |

## ST-33 Aktuelles

| Review point | Result |
| --- | --- |
| 1 M No CTA | behoben. S03 "Vertraulich anfragen" with the reassurance line. Intro links `/ratgeber/`, `/kontakt/`, `/publikationen/`, `/dr-anja-stuerzl/`. |
| 2 M Teaser risk missing in OPEN-FLAGS | behoben. OPEN-FLAGS A1 lists all teasers, including "Jetzt vor Strafverfolgung schützen!", and asks for retitling before the list goes live. Decision for Martin: how to tell the firm. |
| 3 L "aktuelle Beiträge" | behoben. "Beiträge und Hinweise". |
| 4 L `/ratgeber/` depends on ST-34 (proposal) | bewusst offen. Flag B1 stays: remove the link if the Ratgeber does not come. |
| Gap: depth 25, no topics | teilweise behoben. A topic line (Steuerfahndung, Steuerhinterziehung, Schenkungen unter Ehepartnern, Steuerstrafverfahren und Besteuerungsverfahren) and the post types (Interviews, Fachbeiträge, Podcast-Folgen, Vorträge, Seminare, Webinare) from the live list. The CMS list stays a CMS task. Flag A2: the topic line must follow the list. |
| Gap: no CollectionPage/ItemList schema | bewusst offen. Tool limit (decision 6). |
| Address block | Not added (Fixes §2.5 excludes Aktuelles). |

## What I could not fix or verify

- All client facts marked open in OPEN-FLAGS and `placeholders.md` need the firm: services per office, Glogger's role, entrance and visitor parking in Frankfurt, ÖPNV route for Untermainkai 26, emergency-number hours, video call, response time, consent text.
- The title of Lea Wimmer and Dr. Glogger: only live profiles.
- The Finanzamt directory fact needs a yearly check ("Rechtsstand: Oktober 2026" is in the text).
- Frankfurt address on Google, anwalt.de and the live site is still the old one. Do not publish ST-40/ST-41 before Martin's go on the switch.
- Suggestion for the skill: in `link_network.py` the URL tokens in link targets count as words, which raises the overlap of pages with the same link list. Compare only visible text.
