# Fact check, agent F: Claudia Maria Steifensand (2026-10-13)

Start 12:58:09 · End 13:01. Input: `prospect.json`. No browser, no paid calls. Only this file was written.
Scope: (1) the "For the fresh agent" rows of `factcheck-auto.md`, (2) the map claims against `scan-grid.png` + `competitors.md`, and the claims about the two Google entries against both panel files, (3) the non-number claims against evidence/, demand.md, site-findings.md, homepage.md, competitors.md and case-library.json, (4) the tone flags.

## Image read (scan-grid.png, 7 x 7, row 1 = north)

| Row | Col 1 to 7 |
|---|---|
| 1 | 4 4 4 3 2 2 2 |
| 2 | 3 3 3 2 2 2 1 |
| 3 | 3 3 4 2 2 2 2 |
| 4 | 3 3 3 **2** 2 2 2 |
| 5 | 3 3 3 2 1 2 2 |
| 6 | 3 3 3 2 2 2 2 |
| 7 | 3 3 2 2 2 2 2 |

Count: rank 1 = 2, rank 2 = 26, rank 3 = 17, rank 4 = 4. Top 3 = 45 of 49. Centre (row 4, col 4) = 2. This matches `competitors.md` exactly.

## 1. Rows from "For the fresh agent: check only these claims"

| Field | Claim | Verdict | Evidence |
|---|---|---|---|
| `calc.val` | 1500 | UNSUPPORTED (labelled assumption) | No price on the site (site-findings.md section 4). It is labelled "Annahme" on the page, so it can stay as an assumption. |
| `calc.volumes_line` | "1.500 Euro, eine vorsichtige Annahme" | UNSUPPORTED | No file shows that 1.500 Euro is low or "vorsichtig". The word "vorsichtige" claims more than the data. See Must fix 6. |
| `grid.caption_today` | Platz 4 nur an den 4 Punkten im Nordwesten, um Strehla und Gröba | SUPPORTED | scan-grid.png: rank 4 at row 1 col 1-3 (Strehla, Lorenzkirch, Zschepa) and row 3 col 3 (Gröba label). competitors.md: "Rank 4 at 4 points". |
| `system.step1.demand_note` | Für Riesa nur bei „bestattungsinstitut riesa“ eine Zahl: 20 | SUPPORTED | demand.md section 1 ("only town term with a number", 20); dfs-volumes-ads.json. |
| `system.step1.items[5].why` | Nummer für Tag und Nacht nur auf der Kontakt-Seite | SUPPORTED | site-findings.md section 2 ("Only on /kontakt/", line 118). |
| `system.step2.changes[1].title` | Alle Leistungen eintragen | SUPPORTED (recommendation) | The listed items are all on /leistungen/ (site-findings.md section 5). The list names 8 of 13 items; acceptable for a recommendation. |
| `system.step2.cleanup[3].text` | nur auf der Kontakt-Seite, nicht auf der Startseite | SUPPORTED | site-findings.md section 2; scorecard-today.md item 6. |
| `system.step3.five[0].a` | Nur der Name „Bestattungsinstitut Pinkert & Partner“ oben, darunter Rosenfoto, keine Überschrift | SUPPORTED | home-today-1440.jpg; homepage.md 5-second test ("Brand text … only. No H1"). |
| `system.step3.five[1].a` | Adresse und Trauerhalle stehen nur auf der Kontakt-Seite | WRONG | The Goethestr. address is also in the imprint (site-findings.md section 3). The Trauerhalle is also named on /leistungen/ ("Aufbahrungen in unserer Trauerhalle", homepage.md trust table). See Must fix 3. |
| `system.step3.five[2].a` | Nur das Zeichen des Bestatterhandwerks am unteren Rand | SUPPORTED | home-today-1440.jpg (badge at the lower edge); scorecard-today.md item 7. |
| `system.step3.five[3].a` | Tag und Nacht nur auf der Kontakt-Seite; oben 03525 735814 | SUPPORTED | home-today-1440.jpg ("Rufen Sie an: 03525 735814"); site-findings.md section 2. |
| `check[0].rows[2].title/text` | Immer verschlüsselt, immer mit dem Schloss-Symbol | SUPPORTED | site.json `http_redirects_to_https: true`; site-findings.md section 2 (http and www both 301 to https). |
| `check[0].rows[3].title/text` | „Tag und Nacht sind wir telefonisch dienstbereit“ nur dort | SUPPORTED | site-findings.md section 2, exact sentence on /kontakt/. |
| `check[1].rows[2].text` | Nur das Impressum hat eine eigene Beschreibung | WRONG | evidence/site-pages.json: /datenschutz/ also has a meta description ("Datenschutzrechtliche Information zur Be- und Verarbeitung …"). site-findings.md section 2 has the same error. See Must fix 2. |
| `quick_wins[0].text` | Heute steht das nur auf der Kontakt-Seite | SUPPORTED | site-findings.md section 2. |
| `quick_wins[2].text` | Heute hat nur das Impressum eine | WRONG | Same as `check[1].rows[2]`: Impressum and Datenschutz have one (site-pages.json). The four pages named (Startseite, Leistungen, Unser Haus, Kontakt) do have empty descriptions: correct. |
| `roadmap[1].what` | zweite Einordnung, alle Leistungen, Fotos, Antworten | SUPPORTED (plan) | Plan text, no fact claim. |
| `guide.point` | 45 von 49, an 2 auf Platz 1, nur im Nordwesten Platz 4 | SUPPORTED | scan-grid.png count above; competitors.md. |

## 2. Map claims and the two Google entries

| Field | Claim | Verdict | Evidence |
|---|---|---|---|
| `hero.cards[1].sub`, `grid.h2`, `headlines.*`, `system.steps[1].kpi`, `step2.good` | unter den ersten drei an 45 von 49 Punkten | SUPPORTED | scan-grid.png (45 points at rank 1 to 3); competitors.md (SoLV 91,84 % = 45/49). |
| `hero.cards[1].badge` | In der Stadtmitte Platz 2, Platz 1 an 2 Punkten | SUPPORTED | scan-grid.png centre = 2; two points at rank 1. |
| `grid.caption_today` | Stadtmitte und Osten meist Platz 2 | SUPPORTED | scan-grid.png: columns 4 to 7 are rank 2 except row 1 col 4 (3) and two rank-1 points. |
| `grid.caption_today` | im Westen um Canitz, Weida und Mautitz Platz 3 | SUPPORTED | scan-grid.png: columns 1 to 3, rows 2 to 7 are rank 3 except row 3 col 3 (4) and row 7 col 3 (2). |
| `grid.caption_today` | Platz 1 bei Glaubitz und bei Poppitz | SUPPORTED | scan-grid.png: row 2 col 7 (north-west of the Glaubitz label), row 5 col 5 (at the Poppitz label). |
| `grid.intro` | 49 Punkte im 5-km-Umkreis um die Stadtmitte, 13.10.2026, „bestatter riesa“ | SUPPORTED | competitors.md (7x7, 5 km, centre 51.3080/13.2960); falcon report date 10/13/2026. |
| `grid.caption_goal` | Die beiden Bestatter vor euch haben 4 und 1 Bewertung | SUPPORTED | competitors.md (Wünsche 4, Städtisches 1). |
| `step2.h2` | Zwei Bestatter vor euch, keiner hat mehr Bewertungen | SUPPORTED | competitors.md (SoLV 100 % and 97,96 % vs 91,84 %; reviews 4 and 1 vs her 4). |
| `step2.lead` | Wünsche und Städtisches fast im ganzen Umkreis unter den ersten drei | SUPPORTED | competitors.md (100 %, 97,96 %). |
| `step2.table` | names, categories, reviews, shares | SUPPORTED | competitors.md table; falcon report (her category only "Funeral home"). 98 % = 97,96 rounded. |
| `step2.fine` | Riesaer Str. 40 an keinem Messpunkt unter den ersten drei | SUPPORTED | competitors.md (SoLV 0 %, ARP 5,00). |
| `step2.meaning` | 0,7 km Wünsche, 1,4 km euer Büro; Wünsche H1 „Bestatter in Riesa“ | SUPPORTED | competitors.md; comp-pages.json (Wünsche h1). |
| `step2.changes[0]` | Städtisches: Bestattungsinstitut + Bestattungsunternehmen; euer Eintrag eine Einordnung | SUPPORTED | competitors.md; falcon report `categories: {funeral_home}` for her place. |
| `hero.cards[0].badge`, `check[3].rows[0]` | Goethestraße 5,0 bei 4 Bewertungen, neueste rund 1 Jahr | SUPPORTED | google-panel-2026-10-13.md. |
| `hero.cards[2].sub`, `check[3].rows[2]` | Riesaer Str. 40: 3,2 Sterne, 5 Bewertungen, neueste rund 3 Jahre | SUPPORTED | google-panel-2-2026-10-13.md. |
| `hero.cards[2].badge`, `step2.changes[4]`, `check[3].rows[3]` | Keine Antwort auf eine Bewertung, in beiden Einträgen | SUPPORTED | Both panels: "Owner replies: 0". |
| `step2.changes[2]` | Riesaer Str. 40 zeigt „Öffnet um 08:00“, Goethestraße „Rund um die Uhr geöffnet“ | SUPPORTED | panel 2 "Geschlossen · Öffnet um 08:00"; panel 1 "Rund um die Uhr geöffnet". |
| `step2.changes[2]`, `check[3].rows[2]` | Google bietet diesen Eintrag zur Bestätigung durch den Inhaber an | SUPPORTED (neutral, allowed) | panel 2 "Als Inhaber eintragen". Panel 1 has no prompt; the page claims nothing about panel 1. Correct. |
| `step2.cleanup[2]` | Zwei Einträge mit derselben Nummer; Website 01589, Google 01594 | SUPPORTED | both panels (+49 3525 735814); site-findings.md section 3. |
| `step2.changes[2]`, `quick_wins[3]`, `system.steps[1].text` | Riesaer Str. 40 = Trauerhalle | SUPPORTED | site-findings.md section 3 ("Unsere Trauerhalle, Riesaer Straße 40" on /kontakt/). |
| `step2.changes[3]` | neueste Bewertung Goethestraße rund 1 Jahr | SUPPORTED | panel 1. |

## 3. Other non-number claims in prospect.json

| Field | Claim | Verdict | Evidence |
|---|---|---|---|
| `hero.sub`, `headlines.hero_sub` | Auf der Startseite fehlen eine Überschrift mit Riesa, **ein Button** und der Hinweis auf Tag und Nacht | WRONG (button part) | The homepage has buttons: "Zu den Leistungen", "Unser Haus", "Anfrage absenden" (scorecard-today.md items 5 and 11). Only the first screen has no button (item 4). See Must fix 1. |
| `hero.cards[0].sub` | Erd-, Feuer-, Wald- und Seebestattung, eigene Trauerhalle | SUPPORTED | homepage.md trust table; site-findings.md section 5. |
| `hero.cards[3].sub`, `step3.note_today`, `headlines.step3_h2` | Rosenfoto, Nummer oben, keine Überschrift mit Riesa, kein Button im ersten Bildschirm | SUPPORTED | home-today-1440.jpg; scorecard-today.md items 1, 2, 4. |
| `step1.h2`, `step1.organic` | Startseite Platz 5 bei „bestatter riesa“; Seiten zu Vorsorge und Kosten fehlen | SUPPORTED | demand.md section 2; site-findings.md sections 1 and 4. |
| `step1.demand_sub` | ganz Deutschland, Mittel 12 Monate | SUPPORTED | demand.md (location 2276); sources.step1.demand. |
| `step1.demand_note` | „bestatter oschatz“ Nachbarstadt, rund 25 km | SUPPORTED | demand.md section 1 ("neighbour town, 25 km"). |
| `step1.depth.note` | Jede der fünf Seiten nennt Riesa oder den Beruf in der Hauptüberschrift | SUPPORTED | comp-pages.json h1: "Bestatter in Riesa", "… Fritsche in Riesa", "Städtisches Bestattungswesen Meißen" (trade word, no Riesa), "Bestattung Riesa", "… Baumbestattung Riesa". |
| `step1.depth.note`, `check[1].rows[0]` | Keine Hauptüberschrift; erste Überschrift „Gemeinsam durch schwere Zeiten“ | SUPPORTED | site-pages.json (home h1 [], first h2). |
| `step1.items[0].why` | Kein Seitenname nennt Riesa oder Bestatter; jede der fünf Seiten vorn nennt eines davon | SUPPORTED | site-pages.json titles ("… / Pinkert & Partner"); comp-pages.json: all 5 titles contain "Riesa". |
| `step1.items[1].why` | Vorsorge: eine Zeile auf der Leistungsseite | SUPPORTED | site-findings.md section 5; homepage.md ("Abschluss von Bestattungsvorsorgeverträgen"). |
| `step1.items[2].why` | kein Preis und kein Beispiel | SUPPORTED | site-findings.md section 4 (`price_mention: false`; only "in jeder Preislage"). |
| `step1.items[3].why`, `items[4].why` | Seebestattung in einer Zeile; keine eigene Seite je Bestattungsart | SUPPORTED | site-findings.md sections 1 and 5. |
| `step1.items[5].why` | Unterlagen-Liste ohne Überschrift auf der Leistungsseite | SUPPORTED | site-findings.md section 5; scorecard-today.md item 9. |
| `step2.changes[5]` | echte Fotos von Haus, Trauerhalle, Ausstellungsraum auf der Website | SUPPORTED | homepage.md (goethestr-_1.jpg, bild_trauerhalle2.jpg, 20230304_110116.jpg). |
| `step2.cleanup[0]` | Spam-Links, Casino- und Wettseiten, 28 seit August 2026 | SUPPORTED | demand.md section 6. |
| `step2.cleanup[1]` | „bestattung pinkert“: nicht unter den ersten 10; **davor stehen andere Bestatter aus Riesa** | WRONG (second sentence) | dfs-serp-name2.json: own site absent (correct). But the top 10 also hold bestattungen-frankenwald.de (Frankenwald), roga-pietaet.de and dasoertliche.de; bonitz-pech.de has no Riesa evidence. See Must fix 4. |
| `step2.good`, `check[3].rows[1]` | „pinkert und partner riesa“: Platz 1 | SUPPORTED | dfs-serp-name.json rank 1 = bestattung-pinkertundpartner.de. |
| `check[0].rows[0]` | Nummer oben auf jeder Seite ein Link | SUPPORTED | site-findings.md section 2 (header tel: link on /, /kontakt/, /leistungen/). |
| `check[0].rows[1]` | Formular auf jeder Seite, Kontakt-Block im Fuß | SUPPORTED | site-findings.md section 2; site.json `form_on_home`, `form_on_contact` true. |
| `check[0].rows[4]` | beginnt nach rund 0,8 Sekunden zu laden | SUPPORTED | site.json ttfb 0.82 / 0.85 / 0.84. |
| `check[1].rows[1]` | „Home / Pinkert & Partner“ | SUPPORTED | site.json `home_title`. |
| `check[1].rows[4]` | Fotos auf Unser Haus und Kontakt ohne Bildtext | SUPPORTED | site-findings.md section 2. |
| `check[2].rows[0]` | keine Besuchermessung zu finden | SUPPORTED | site.json `ga4: []`, `gtm: []`. |
| `check[2].rows[1]` | Daten für Google fehlen | SUPPORTED | site.json `jsonld_blocks: 0`. |
| `step3.lead` | 22 Punkte; Entwurf mit Namen und echten Fotos | SUPPORTED | scorecard-today.md (22 items, 44 max); home-draft-1440.jpg (house photo Goethestr., Trauerhalle card). |
| `step3.note_draft` | Entwurf: Bestattungsinstitut in Riesa, seit 1991, 5,0 Sterne, Tag und Nacht | SUPPORTED | home-draft-1440.jpg. |
| `step3.five[4].a` | kein Foto von Haus, Trauerhalle oder Team; echte Fotos erst auf Unser Haus und Kontakt | SUPPORTED | homepage.md; scorecard-today.md item 8. |
| `quick_wins[5]` | 1991, „mehr als 30 Jahren“, „kompetender“ | SUPPORTED | site-findings.md section 5; homepage.md. |
| `calc.volumes_line` | CPC 10,27 US-Dollar | SUPPORTED | dfs-volumes-ads.json (DataForSEO Google Ads cpc). Note: demand.md labels the column "CPC EUR"; internal only. |
| `proof.featured` | lengauer, abel, more mediaberater exist | SUPPORTED | case-library.json. |
| `proof.lead` | zwei Dienstleister, Einordnung und Leistungen unvollständig **und eigene Seiten für einzelne Leistungen fehlten** | UNSUPPORTED (for abel) | case-library.json: lengauer gaps include "unterseiten" (correct); abel gaps = kategorien, leistungen, ladezeit, verzeichnisse, bewertungen (no "unterseiten"). Abel branch also includes "gesundheit", against sources.proof "Health … cases left out". See Must fix 5. |
| `guide.celebrate` | Lengauer, „Interior Design Wien“, Platz 18 auf Platz 1 | SUPPORTED | case-library.json `jump: Platz 18 → 1`. |
| `system.intro` | Jede Zahl unten stammt aus echten Messungen | SUPPORTED with note | The target "36+ / 44" and the week ranges are not measurements, but the page labels them "Ziel" and as a plan. Acceptable. |
| `headlines.video_p` | In diesem Video zeige ich jeden Schritt | OPEN | `loom_url` is empty. Fill it before deploy. |

## 4. Flags (owner, "unclaimed", promises, tone, image)

| Check | Result |
|---|---|
| Claudia called owner | None. No sentence gives her a role. "Inhaber" only appears in the neutral Google note on entry 2. Correct, because the imprint names Conny Pinkert-Stockert. |
| "unclaimed" / "nicht beansprucht" | None in prospect.json. (site-findings.md sections 3 and 8 use "unclaimed", internal only.) Falcon lists `claimed: false` for panel 1, but the page states nothing about it. Keep it so. |
| Cold words (Kunden, Patienten, Praxis, Umsatz, Leads, Termin) | None found (grep). |
| Sales tone | `headlines.hero_h1` "was eure Website noch verschenkt" (Must fix 7). `headlines.cleanup_h3` "was euch heute Anrufe kostet" (Must fix 8, also an unsupported cause). |
| Promise | `step2.changes[3]` "Eine ruhige Bitte … reicht dafür." claims the request is enough (Must fix 9). |
| Jargon | None. "Einordnung" replaces category; "Spam-Wert" is explained. |
| Image contradictions | None. All map claims match scan-grid.png. |

## Must fix

1. `hero.sub` + `headlines.hero_sub`: "Auf der Startseite fehlen … ein Button" is wrong; the homepage has buttons (scorecard items 5, 11). Write: "Im ersten Bildschirm fehlen eine Überschrift mit Riesa, ein Anruf-Button und der Hinweis auf Tag und Nacht."
2. `check[1].rows[2].text` + `quick_wins[2].text`: Datenschutz also has a meta description (evidence/site-pages.json). Write: "Nur Impressum und Datenschutz haben eine eigene Beschreibung." and "Heute haben nur Impressum und Datenschutz eine."
3. `system.step3.five[1].a`: the address is also in the imprint, and the Trauerhalle is also named on /leistungen/. Write: "Riesa steht nicht im ersten Bildschirm. Adresse und Trauerhalle stehen nicht auf der Startseite."
4. `system.step2.cleanup[1].text`: "Davor stehen andere Bestatter aus Riesa." is not true for all hits (dfs-serp-name2.json: bestattungen-frankenwald.de, roga-pietaet.de). Write: "Die ersten Treffer zeigen vor allem andere Bestatter aus Riesa."
5. `proof.lead`: abel has no "unterseiten" gap and carries the branch "gesundheit". Either drop "und eigene Seiten für einzelne Leistungen fehlten", or replace abel with a non-health service case that has the "unterseiten" gap.
6. `calc.volumes_line`: drop "vorsichtige". Write: "Startwert pro Bestattung: 1.500 Euro, eine Annahme, denn eure Website nennt keine Preise."
7. `headlines.hero_h1`: "Hier ist, was eure Website noch verschenkt." is sales tone for a funeral home. Write: "Hier seht ihr, was auf eurer Website noch fehlt."
8. `headlines.cleanup_h3`: "was euch heute Anrufe kostet" has no source and sounds like sales copy. Write: "Vorher aufräumen: was heute noch im Weg steht."
9. `system.step2.changes[3].text`: "reicht dafür" is a promise. Write: "Dafür hilft eine ruhige Bitte einige Wochen nach der Trauerfeier, mit direktem Link zum Eintrag."

## For Martin to decide (not errors)

- Calculator labels ("Familien, die euch beauftragen / Monat", "Wert pro Jahr (Annahme)", "Honorar … pro Bestattung") put a money value on bereaved families. They are labelled as assumptions, but the tone is close to revenue copy for a funeral home.
- `final.h2` / `final.p` ("was euch noch von Platz 1 trennt", "kostenlos … Unverbindlich") is the standard closing. It is mild sales tone.
- `loom_url` is empty while `headlines.video_p` refers to a video.
