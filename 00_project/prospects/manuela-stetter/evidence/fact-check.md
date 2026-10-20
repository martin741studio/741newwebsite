# Fact check (agent F, fast run): Manuela Stetter, 14.10.2026

Checker: agent F. I did not write the page. Start 14:26:42.
Input: `prospect.json`. Evidence read: `evidence/factcheck-auto.md`, `evidence/scan-grid.png` (image), `evidence/home-today-1440.jpg` (image), `evidence/google-panel-2026-10-14.md`, `evidence/falcon-report-0e90f7a9f4d310d.json`, `evidence/site.json`, `evidence/site-pages.json`, `evidence/scorecard-today.md`, `evidence/dfs-volumes-ads.json`, `competitors.md`, `demand.md`, `site-findings.md`, `homepage.md`, `draft/index.html`, `prospect-mini/case-library.json`.

## 1. Rows from "For the fresh agent"

| Field | Claim | Verdict | Evidence |
| --- | --- | --- | --- |
| `grid.h2` / `headlines.grid_h2` | Sichtbar nur am Nordrand, in der Stadtmitte nicht unter den ersten 20 | SUPPORTED | scan-grid.png: top row 20+,19,18,15,12,6,6; row 2 far right 19; all others 20+; centre 20+ |
| `grid.caption_today` | nur am Nordrand, Richtung Essenbach | SUPPORTED (note) | scan-grid.png. Best points (6, 6) are north-east, toward Essenbach. The 19 and 18 in the top row are north-west, not toward Essenbach. |
| `system.step1.demand_note` | Zahl steht nur einmal da | SUPPORTED | demand.md section 2 (both 320, merged); no "640" in prospect.json |
| `system.step1.items[5].why` | Adresse in Mirskofen nur ganz unten, ohne Karte und ohne Zeiten | SUPPORTED | scorecard-today.md item 18 (footer "84051 Mirskofen/Essenbach", no map, no hours); site-findings.md section 1 (no contact page in menu) |
| `system.step2.lead` | Zwei der vier ersten an allen 49 Punkten unter den ersten 20; du an 7 | SUPPORTED | falcon report: Mühleninsel found_in 49, Agata Block found_in 49; own found in 7 (competitors.md) |
| `system.step2.changes[0].text` | Agata Block "Heilpraktiker", an allen 49 Punkten | SUPPORTED | falcon: `heilpraktiker_alternative_practitioner`, found_in 49 |
| `system.step2.changes[0].text` | Bei dir nur "Naturheilpraktiker", einzige Einordnung | SUPPORTED (note) | falcon location.categories = only `naturopathic_practitioner`; panel shows "Naturheilpraktiker". The public panel does not show secondary categories. |
| `system.step2.changes[1].title` | Alle Leistungen eintragen | OK (advice, no claim) | services list matches demand.md section 1 |
| `system.step2.changes[3].text` | Ohne Antwort nur ältere, 6 bis 9 Jahre | SUPPORTED | google-panel: 29 of 39 replied, unanswered ones 6 to 9 years old |
| `system.step2.cleanup[1].text` | 28 Adressen, nur 9 Praxis-Seiten | SUPPORTED | site-pages.json: 28 URLs, 9 practice pages, 19 clutter. site-findings.md section 2 says 14/14, which is wrong against the page list. |
| `system.step2.cleanup[1].text` | 11 Autoren-Seiten mit fremden E-Mail-Namen | **WRONG** | site-pages.json: 11 author pages. Only 5 show e-mail names (`…@spotzer.com`). 6 show user names (migration, siteowner, partner, copywriter, wpthemedev, design). |
| `system.step2.cleanup[3].text` | Eine Adresse überall | OK (advice) | site-findings.md section 3: two e-mail addresses, as stated |
| `system.step3.five[3].a` | "Termine buchen" nur ein Punkt in der zweiten Menüzeile | SUPPORTED | home-today-1440.jpg (second menu row); scorecard item 4 |
| `check[0].rows[1]` | Immer verschlüsselt, http leitet weiter | SUPPORTED | site.json: https, `http_redirects_to_https` true, 301 |
| `check[1].rows[2].text` | 28 Adressen, nur 9 Praxis-Seiten; 4 Demo-Seiten, 242 Wörter; 10 Autoren-Seiten ohne H1 | SUPPORTED | site-pages.json (10 author pages with 0 H1; `/author/design/` has 1); site.json duplicate_pages 242 |
| `roadmap[0].what` | eine E-Mail-Adresse überall | OK (plan) | site-findings.md section 3 |
| (text) | heilpraktiker landshut + heilpraktikerin landshut never added | SUPPORTED | demand_note says Google counts them together; no 640 anywhere |

## 2. Map claims against scan-grid.png and competitors.md

| Claim | Verdict | Evidence |
| --- | --- | --- |
| Top 3 at 0 of 49 | SUPPORTED | image: no point at 1 to 3; competitors.md SoLV 0 % |
| Found (top 20) at 7 of 49 | SUPPORTED | image: 6 points in top row + 1 in row 2 |
| zweimal Platz 6, dazu 12, 15, 18 und zweimal 19 | SUPPORTED | image: 6, 6, 12, 15, 18, 19 (top row), 19 (row 2 right) |
| In der Stadtmitte und an 42 Punkten nicht unter den ersten 20 | SUPPORTED (wording) | image: 42 points 20+, centre is one of them. "und an 42" can read as 43. |
| 49 Punkte, 5-km-Umkreis, Mitte Landshut, 14.10.2026 | SUPPORTED | competitors.md scan setup |
| Praxis rund 8,3 km nordöstlich, außerhalb der Karte | SUPPORTED | competitors.md (8,3 km NE, outside radius). demand.md says "about 12 km": superseded by the measured falcon distance 8,29 km. |
| Mühleninsel auf rund 100 % der Karte unter den ersten drei | SUPPORTED | falcon solv 100.00 |
| Table shares 100 / 93,9 / 36,7 / 16,3 % and reviews 31 / 20 / 11 / 11 | SUPPORTED | falcon report; competitors.md |
| Category labels "Alternativmediziner" / "Heilpraktiker" / "Naturheilpraktiker" | SUPPORTED | falcon categories; German label "Alternativmediziner" as in google-panel "Wird auch oft gesucht" |
| Praxen vorn 0,2 bis 2,2 km von der Mitte | SUPPORTED | competitors.md (0,2 / 0,4 / 2,2 / 0,6 km) |
| Kornelia Zettl, Altstadt, gleiche Einordnung, 3 Bewertungen, 44 Punkte | SUPPORTED | falcon: Altstadt 29, `naturopathic_practitioner`, 3 reviews, found_in 44 |
| The image contradicts nothing on the page | SUPPORTED | – |

## 3. Non-number claims in prospect.json

| Field | Claim | Verdict | Evidence |
| --- | --- | --- | --- |
| `hero.cards[0].sub` | Heilpraktikerin · Naturheilkunde für Frauen · Coaching · Kurse · Essenbach bei Landshut | SUPPORTED | site menu (site-findings.md section 1); Impressum title (section 5) |
| `hero.cards[2].sub` | neueste Bewertung vor rund einem Monat | SUPPORTED | google-panel ("vor einem Monat") |
| `hero.cards[3].sub` | Blumenbild, Überschrift mit Landshut und Essenbach, Button "Zu den Kursen", keine Sterne | SUPPORTED | home-today-1440.jpg; homepage.md |
| `system.step1.h2`, `items[1]` | Website nicht unter den ersten 20 Treffern | SUPPORTED | demand.md section 3 (dfs-serp-1/2.json) |
| `system.step1.depth.sub`, `items[0]` | Keiner der 7 Seitentitel nennt Landshut, 7 nennen Essenbach | SUPPORTED (note) | site-pages.json: 7 keyword titles with Essenbach. She has 9 practice pages; Impressum and Datenschutz have plain titles. None names Landshut. |
| `system.step1.depth.note` | Eine der fünf Seiten nennt Beruf und Ort in der H1; deine H1 ohne "Heilpraktikerin"; Titel "Menstruationsbeschwerden \| Essenbach" | SUPPORTED | site-findings.md section 7 (Silvia Hensel H1); site.json home_h1, home_title |
| `system.step1.items[2].why` | Preise auf "Termine buchen" (150 € für 60 Minuten), keine Seite zu Kosten | SUPPORTED | site-findings.md section 4 |
| `system.step1.items[3].why` | Hormonspeicheltest auf "Naturheilkunde", ohne Preis | SUPPORTED | site-findings.md section 4 |
| `system.step1.items[3].why` | "ohne Ablauf" | **UNSUPPORTED** | No evidence file says the page has no description of the procedure. |
| `system.step1.items[4].why` | Kinderwunsch ein Punkt in einer Liste, ohne eigene Seite | SUPPORTED | site-findings.md section 5 (list on /leistungen/); site-pages.json (no such page) |
| `system.step2.changes[2].text` | neueste rund einen Monat, 7 jünger als ein Jahr | SUPPORTED | google-panel review ages (1+1+1+2+1+1 = 7 under one year) |
| `system.step2.cleanup[0].text` | Spam-Links, darunter Casino- und Wettseiten | SUPPORTED | demand.md section 6 (bestnz-poker-casinoslot.com, betwinnermirror.com) |
| `system.step2.cleanup[2].text` | Vier Demo-Seiten, gleicher Titel, 242 Wörter | SUPPORTED | site.json duplicate_pages |
| `system.step2.cleanup[3].text` | manuelastetter@manuela-stetter.de unten, kontakt@… im Impressum | SUPPORTED | site-findings.md section 3 |
| `system.step2.good` | Name-Suche Platz 1 | SUPPORTED | demand.md section 5 |
| `system.step3.note_today` | Nummer oben rechts, Landshut und Essenbach in der Überschrift; es fehlen Sterne, Termin-Button, Foto | SUPPORTED (note) | home-today-1440.jpg. The top edge of her photo starts at the bottom of the 770 px screen; the photo is not in the hero. |
| `system.step3.five[0..4]` | 5-second answers | SUPPORTED | home-today-1440.jpg; homepage.md |
| `system.step3.note_draft` | Foto, Name, Heilpraktikerin in Essenbach bei Landshut, 5,0 / 39, "Termin buchen", 15 Minuten kostenlos | SUPPORTED | draft/index.html text |
| Draft trust row | "Seit 10 Jahren eigene Praxis", no "600 Frauen" | SUPPORTED | site-findings.md section 6 (/manuela/); draft has no 600/400 count |
| `check[0].rows[0]` | Nummer auf jeder gemessenen Seite ein Link | SUPPORTED | site-findings.md section 1 (home + 6 pages) |
| `check[0].rows[2]` | lädt nach rund 0,2 s | SUPPORTED | site.json ttfb 0.16 / 0.22 / 0.23 |
| `check[0].rows[3]`, `rows[4]` | Buchungsportal, 15 min kostenlos; keine Kontakt-Seite, kein Formular; Portal, E-Mail, WhatsApp | SUPPORTED | site-findings.md section 1 |
| `check[1].rows[0]` | Leistungsseite "Schmerztherapie \| Essenbach"; jeder Titel ein einzelnes Wort | SUPPORTED | site-findings.md section 3 |
| `check[1].rows[1]` | H1 wording, "Heilpraktikerin" fehlt | SUPPORTED | site.json home_h1 |
| `check[1].rows[3]` | Meta "Manueal", siezt | SUPPORTED | site.json home_meta |
| `check[2].rows[0]` | Keine Besuchermessung | SUPPORTED | site.json ga4 [], gtm [] (home HTML) |
| `check[2].rows[1]` | beschreibt sich als Website, nicht als Praxis | SUPPORTED (note) | site-findings.md section 1: WebPage, WebSite, Organization, no LocalBusiness |
| `check[3].rows[1]` | Praxen vorn 31, 20, 11, 11 | SUPPORTED | competitors.md |
| `calc.volumes_line` | CPC rund 1,00 US-Dollar | SUPPORTED | dfs-volumes-ads.json cpc 1 for both terms |
| `calc.val_label` | zwei Termine à 60 Minuten = 300 € | SUPPORTED (assumption labelled) | site-findings.md section 4 (150 € / 60 min) |
| `system.intro` | "die Werte im Rechner sind Annahmen" | SUPPORTED (note) | Volume, CPC and 150 € are real values; calc.volumes_line labels only budget, inquiry and booking share as assumptions. Small mismatch. |
| `proof.lead` | Heilpraktiker Regensburg und Freiburg, Familienberatung bei Stuttgart, Betrieb aus Wien; jedem fehlte Einordnung oder Leistungen | SUPPORTED | case-library.json (schlirf, laserstein, abel, lengauer; all have gap "leistungen", 3 have "kategorien") |
| `guide.celebrate` | Schlirf, "Heilpraktikerin", Platz 85 auf 1 | SUPPORTED | case-library.json schlirf "Platz 85 → 1" |

## 4. HWG, "unclaimed", jargon, promises

| Check | Verdict | Evidence |
| --- | --- | --- |
| No healing or success promise in our copy | SUPPORTED | No promise found. Draft subline is neutral ("Ich schaue auf dich als ganze Frau"). |
| No disease names as advertising | SUPPORTED | Disease-type terms appear only as search terms in the demand table. The new home title drops "Menstruationsbeschwerden". "Kinderwunsch" and "Hormonspeicheltest" are her service names. |
| No protected titles | SUPPORTED | "Heilpraktikerin" is her licensed title (Impressum, site-findings.md section 5). The draft avoids "Frauenheilkunde" and "Traumatherapeutin". |
| Werberecht row neutral | SUPPORTED | `check[3].rows[4]`: names an example, no claim of illegality, matches site-findings.md section 5 |
| "unclaimed" | SUPPORTED (absent) | The page never says the entry is unclaimed. Falcon says `claimed: false`, but the panel shows 29 owner replies and no claim prompt. Keep it out. |
| Jargon | SUPPORTED | No SoLV, NAP, schema or H1 term in visible copy. "Einordnung" is used for category. |
| Marketing goals | OK | `grid.chips` and `final.p` name goals ("Mehr Anfragen"). They make no health promise. |

## Must fix

1. `system.step2.cleanup[1].text`: "11 Autoren-Seiten mit fremden E-Mail-Namen" is WRONG. Only 5 of the 11 author pages show e-mail names. Fix: "11 Autoren-Seiten, 5 davon mit fremden E-Mail-Namen". Apply the same idea to `quick_wins[3].text` ("die Autoren-Seiten mit fremden E-Mail-Namen" → "die 11 Autoren-Seiten, teils mit fremden E-Mail-Namen").
2. `system.step1.items[3].why`: "ohne Ablauf" is UNSUPPORTED. Delete "ohne Ablauf und", or verify the /naturheilkunde/ text first. Safe form: "Der Test steht auf deiner Seite „Naturheilkunde“, ohne Preis."

## Should fix (wording, low risk)

- `grid.caption_today`: "In der Stadtmitte und an 42 Punkten" can read as 43 points. Better: "An 42 Punkten nicht unter den ersten 20, auch in der Stadtmitte."
- `grid.caption_today`: "Richtung Essenbach" fits only the north-east points. Better: "am Nordrand der Karte, am besten im Nordosten Richtung Essenbach".
- `system.intro`: "die Werte im Rechner sind Annahmen" → "Budget, Anfrage- und Buchungsanteil im Rechner sind Annahmen", to match `calc.volumes_line`.
- `site-findings.md` section 2 says 14 real / 14 clutter. The page list gives 9 / 19. The page uses 9 / 19, which is correct.

Claims checked: 17 flagged rows, 11 map claims, 33 non-number claims, 7 HWG/jargon checks (68 in total).
