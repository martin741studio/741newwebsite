# Fact check: Sabine Schwarz (agent F, 2026-10-12, 15:14 to 15:21)

Input: `prospect.json`. Start point: `evidence/factcheck-auto.md` (numbers matched mechanically, not checked again).
Evidence read: `evidence/scan-grid.png` (image), `evidence/falcon-report-5544ec2c473e732.json`, `competitors.md`, `evidence/maps-entries-2026-10-12.md`, `evidence/google-panel-2026-10-12.md`, `demand.md`, `site-findings.md`, `homepage.md`, `evidence/scorecard-today.md`, `evidence/comp-pages.json`, `evidence/dfs-serp-1.json`, `evidence/dfs-serp-name.json`, `evidence/dfs-serp-name2.json`, `evidence/dfs-refdomains-spam.json`, `evidence/dfs-volumes-ads.json`, `evidence/home-today-1440.jpg`, `evidence/home-draft-1440.jpg`, `prospect-mini/case-library.json`.
Live check: curl of all 15 HTML pages in `evidence/site-page-urls.txt`, `http://www.therapie-sasch.com/` (200, no redirect) and `/sitemap.xml` (404). No browser. No paid calls.

Image read of `scan-grid.png` (row 1 = north, column 1 = west, centre = row 4 column 4):

| Row | C1 | C2 | C3 | C4 | C5 | C6 | C7 |
|---|---|---|---|---|---|---|---|
| 1 | 14 | 20+ | 20+ | 20+ | 20+ | 20+ | 20+ |
| 2 | 11 | 20+ | 20+ | 20+ | 20+ | 20+ | 20+ |
| 3 | 10 | 12 | 19 | 20+ | 20+ | 20+ | 20+ |
| 4 | 6 | 9 | 18 | **20+** | 20+ | 20+ | 20+ |
| 5 | 2 | 2 | 10 | 19 | 19 | 20+ | 20+ |
| 6 | 3 | 3 | 8 | 14 | 14 | 20 | 20+ |
| 7 | 3 | 5 | 7 | 9 | 10 | 14 | 18 |

Top 3: 5 points (rows 5 to 7, columns 1 to 2). "20+": 23 points. Found in the top 20: 26 points. Centre: "20+".

## Claims

| # | Field | Claim (short) | Verdict | Evidence (file + value) |
|---|---|---|---|---|
| **A. Rows from "For the fresh agent"** |||||
| 1 | `calc.val` | 300 | SUPPORTED | Derived: 2 x 150,00 € "Beratungsgespräch für 2 Personen: 1x 75 Minuten" (curl `preise.html`, also `Paar.html` JSON-LD Offer 150.00). `system.intro` says calculator values are assumptions. |
| 2 | `system.step2.changes[1].text` | eine von sechs | SUPPORTED | falcon `location.categories`: 6 values, one is "Marriage or relationship counselor". |
| 3 | `grid.h2`, `headlines.grid_h2` | ... alle im Südwesten | SUPPORTED | scan-grid.png: all 5 top-3 points in rows 5 to 7, columns 1 to 2. |
| 4 | `grid.caption_today` | Alle fünf im Südwesten, rund um Schorkendorf und Witzmannsberg | SUPPORTED | scan-grid.png: labels "Schorkendorf" and "Witzmannsberg" sit between these 5 points. |
| 5 | `system.step1.items[5].why` | Alle 15 Bewertungen 5 Sterne, auf der Website keine | SUPPORTED | google-panel: "15 mal 5 Sterne". curl of 15 pages: 0 hits for Bewertung, Rezension, Sterne. |
| 6 | `system.step2.lead` | Die vier vorn an allen 49 Punkten unter den ersten 20, du an 26 | SUPPORTED | falcon `found_in` 49 for Bernklau, Bartsch, Lösungsraum, Wittmann; hers 26. |
| 7 | `system.step2.meaning` | Bartsch sitzt auch in Ahorn, 3 Bewertungen, alle 49 Punkte | SUPPORTED | falcon: "Buchenweg 22, 96482 Ahorn", reviews 3, found_in 49. Note: Bartsch is 2,68 km from the centre, she is 4,26 km (see Optional). |
| 8 | `system.step2.meaning` | FRIEDA-Eintrag an allen 49 Punkten, Mitte Platz 4, ohne Bewertung | SUPPORTED | falcon "Sabine Schwarz Paartherapie": found_in 49, reviews 0. Centre rank 4 only in competitors.md (the JSON has no per-point data). |
| 9 | `system.step2.changes[1].text` | nur als eine von sechs, dazu Internet-Marketing und Feng-Shui-Berater | SUPPORTED | falcon `location.categories`: "Internet marketing service", "Feng shui consultant". |
| 10 | `system.step2.changes[2].title` | Alle Leistungen eintragen (implies: services are missing) | UNSUPPORTED | No evidence file reads the services ("Leistungen") of any of her 3 entries. maps-entries-2026-10-12.md has no services row. |
| 11 | `system.step2.good` | alle 15 Bewertungen 5 Sterne, jede mit Antwort | SUPPORTED | google-panel: "Owner replies: 15", "15 mal 5 Sterne". |
| 12 | `system.step3.note_today` | Ort, 5 Sterne, Nummer fehlen; Button nur „Kontakt“ | SUPPORTED | home-today-1440.jpg; scorecard-today.md #1, #5, #7, "no phone number in the first screen". |
| 13 | `system.step3.five[3].a` | Erstgespräch nur im halb durchsichtigen Knopf unten rechts | SUPPORTED | home-today-1440.jpg (first screen); scorecard #6. |
| 14 | `check[0].rows[1].title` | Nicht immer verschlüsselt | SUPPORTED | curl `http://www.therapie-sasch.com/` = 200, no redirect; site.json `http_redirects_to_https: false`. |
| 15 | `check[3].rows[0].text` | 5,0 bei 15, alle mit 5 Sternen | SUPPORTED | google-panel. |
| 16 | `quick_wins[4].title` | Immer verschlüsselt, eine Startseite | SUPPORTED (basis) | site.json `duplicate_pages` "/" and "/index.html"; curl: both 48712 bytes. |
| 17 | `roadmap[1].what` | drei Einträge zusammenbringen, ..., alle Leistungen | UNSUPPORTED (part) | "alle Leistungen": see #10. "drei zusammenbringen" conflicts with `changes[0]` (one entry per place, so two remain). |
| 18 | `proof.lead` | Bei jedem fehlte etwas, das auch bei dir fehlt: Einordnung oder alle Leistungen | UNSUPPORTED (part) | case-library.json: Schlirf gaps = leistungen, bewertungen, mobil, verzeichnisse (no kategorien). Her services gap is not in evidence (#10), so for Schlirf the link is not proven. |
| 19 | `proof.lead` | alle Leistungen im Eintrag | UNSUPPORTED | Same as #10. |
| **B. Map claims** |||||
| 20 | `headlines.hero_h1`, `hero.cards[1]` | 5 von 49 unter den ersten drei, Mitte nicht unter den ersten 20 | SUPPORTED | scan-grid.png; falcon solv 10.20. |
| 21 | `grid.caption_today` | In der Stadtmitte und fast im ganzen Norden und Osten steht „20+“ | WRONG | scan-grid.png: north-west shows 14, 11, 10, 12, 19 (rows 1 to 3). South-east shows 19, 19, 14, 14, 20, 10, 14, 18 (rows 5 to 7, columns 4 to 7). Only the north-east block (rows 1 to 4, columns 4 to 7) is "20+" at all 16 points. |
| 22 | `grid.caption_today` | An 23 Punkten nicht unter den ersten 20 | SUPPORTED | scan-grid.png count 23; draft-facts `not_top20` 23. |
| 23 | `grid.caption_today` | Bernklau auf rund 61,2 % unter den ersten drei | SUPPORTED | falcon solv 61.22. |
| 24 | `grid.caption_goal` | Ziel Stadtmitte. Die Praxen vorn haben 0 bis 11 Bewertungen, du hast 15 | WRONG (misleading) | competitors.md: rank 1 at the centre point is Duygu Doganay. falcon: Doganay reviews 19, solv 22.45 (ahead of her 10.20). In the centre, the first place has more reviews than she has. |
| 25 | `system.step2.meaning` | Bewertungen sind nicht deine Lücke: die vier vorn 0 bis 11 | SUPPORTED (for the four in the table) | falcon: 11, 3, 0, 1. Same Doganay caveat as #24. |
| 26 | `system.step2.meaning` | rund 1 bis 2,7 km; deine Praxis 4,3 km | SUPPORTED | competitors.md 0,99 / 2,68 / 1,92 / 1,92 km; hers 4,26 km. |
| 27 | `system.step2.table` | Names, categories, reviews, shares | SUPPORTED | falcon: Bernklau Counselor 11 61.22; Bartsch Counselor 3 48.98; Lösungsraum Family counselor + Marriage counselor 0 48.98; Wittmann Family counselor + Consultant + Marriage counselor 1 26.53; her primary category "Alternativmediziner" (maps-entries). |
| 28 | `system.step2.changes[1].text` | Lösungsraum und Wittmann als „Ehe- und Paarberater“ | SUPPORTED | falcon categories (see #27). |
| 29 | `system.step2.changes[0].text` | FRIEDA-Eintrag rund 33 %, ohne Bewertung, ohne Zeiten | SUPPORTED | falcon solv 32.65, reviews 0; maps-entries entry 3: "none (Google shows Öffnungszeiten hinzufügen)". |
| 30 | `quick_wins[5].text` | Coburger Eintrag „Coaching Center“; Ahorn: Internet-Marketing, Feng-Shui streichen | SUPPORTED | maps-entries entry 3 category "Coaching Center"; falcon `location.categories`. |
| 31 | `system.step2.cleanup[3].text` | 3 Einträge mit Website und Nummer, Bewertungen nur in Ahorn-Schorkendorf, Zinkenweg vs. Zinkenwehr | SUPPORTED | maps-entries: same website and phone on all 3; reviews only on entry 1; entry 3 "Zinkenweg 5"; site footer and `Paar.html` JSON-LD "Zinkenwehr 5". |
| 32 | `system.step2.h2`, `roadmap[1].why`, `guide.point` | Bewertungen auf dem Eintrag, der in der Mitte nicht unter den ersten 20 ist; Coburger Eintrag hat keine | SUPPORTED | scan-grid.png centre "20+"; maps-entries entries 2 and 3 no reviews. |
| 33 | whole page | Claim status | PASS | No "nicht beansprucht", no "unclaimed". (falcon `claimed: false` conflicts with visible owner replies; the page correctly says nothing.) |
| **C. Other non-number claims** |||||
| 34 | `hero.sub`, `system.step2.good` | Website für deinen Namen auf Platz 1 | SUPPORTED | dfs-serp-name2.json "sabine schwarz heilpraktikerin coburg": therapie-sasch.com rank 1. |
| 35 | `hero.cards[2].sub` | neueste vor rund 1 Jahr; Bernklau 11 | SUPPORTED | google-panel "newest review about 1 year old"; falcon Bernklau 11. |
| 36 | `hero.cards[3].sub` | „Willkommen bei Sabine Schwarz“, Button „Kontakt“, kein Ort | SUPPORTED | home-today-1440.jpg. |
| 37 | `system.step1.h2`, `depth.big[1]`, `quick_wins[1]` | Paar-Seite: Coburg nicht in Titel und Überschrift, „Online“ ja | SUPPORTED | curl `Paar.html`: title "Online-Paarberatung & Paartherapie \| Sabine Schwarz – Heilpraktikerin", H1 "Online-Paarberatung & Paartherapie". |
| 38 | `system.step1.depth.title` | Die Lücke ist nicht die Länge, sondern Coburg in der Überschrift | UNSUPPORTED (cause) | comp-pages.json: H1 with "Coburg" 1 of 5 (coburg-psychotherapie.de), title with "Coburg" 2 of 5. Bernklau ranks with H1 "Paartherapie" and title "Praxis Rudi Bernklau — Paartherapie". `depth.note` itself says none of the 5 has Paartherapie + Coburg in the H1. The evidence does not show that the H1 is the cause. |
| 39 | `system.step1.depth.note` | Keine der fünf nennt Paartherapie und Coburg zusammen in der H1 | SUPPORTED | comp-pages.json h1 values; draft-facts `h1_keyword_pair` 0/5. |
| 40 | `system.step1.items[1].why` | steht nicht unter den ersten 20 Treffern | SUPPORTED | dfs-serp-1.json: 20 organic results, therapie-sasch.com absent. |
| 41 | `system.step1.items[2].why` | Preise da (150 € für 75 Minuten zu zweit), keine Seite zu genau dieser Frage | SUPPORTED | curl `preise.html`; no page or blog on cost (blog title "Wie hilft Online-Paarberatung wirklich?"). |
| 42 | `system.step1.items[3].why` | Ausbildung in Mobbing-Beratung, keine eigene Seite | SUPPORTED | curl `about.html`: "2016-2018 Weiterbildungen zur Burnout-Beraterin und Mobbing-Beraterin"; site-findings "no Mobbing page". |
| 43 | `system.step1.items[4].why` | Seite heißt „Psychotherapie (HPG)“, ohne Ort | SUPPORTED | curl `praxis.html` title and H1. |
| 44 | `system.step2.changes[3].text` | neueste Bewertung rund 1 Jahr alt | SUPPORTED | google-panel. "bringt wieder neue" is a certainty (see Optional). |
| 45 | `system.step2.changes[4].text` | 15 von 15 beantwortet | SUPPORTED | google-panel "Owner replies: 15". |
| 46 | `system.step2.cleanup[0].text`, `check[3].rows[3].text` | 38 Websites sind unseriös, zum Beispiel Casino- und Wettseiten | WRONG (misleading) | dfs-refdomains-spam.json: 38 domains with spam score 60 to 75 (a DataForSEO value). Only 2 are casino or betting (bestnz-poker-casinoslot.com, betwinnermirror.com). Most are SEO-checker and web2.0 domains. demand.md section 5 asks for the wording "hoher Spam-Wert (60 oder mehr)". |
| 47 | `system.step2.cleanup[1].text`, `check[3].rows[2]` | „therapie sasch“: Website nicht unter den ersten 9; vor allem jameda und doctolib; Titel „Name ‚Sasch‘ noch schwach“ | SUPPORTED (organic part) / UNSUPPORTED (title) | dfs-serp-name.json: 9 organic, own rank none, 7 of 9 jameda or doctolib. But the same result has `item_types` ai_overview, google_reviews, knowledge_graph, and organic starts at absolute rank 2. Google can show her own panel for this search. demand.md: "Treat as a finding to check, not as proof." |
| 48 | `system.step2.cleanup[2].text` | 2 Startseiten | SUPPORTED | site.json `duplicate_pages`; curl identical. |
| 49 | `check[0].rows[0].text` | Auf jeder gemessenen Seite Nummer als Link | SUPPORTED | curl: `tel:` on all 15 HTML pages. |
| 50 | `check[0].rows[2].text` | beginnt nach rund 0,5 Sekunden | SUPPORTED | site.json ttfb 0.35, 0.5, 0.51. |
| 51 | `check[0].rows[3].text` | Formular und Buchungsseite | SUPPORTED | site.json `form_on_contact: true`; `Buchung.html` exists. |
| 52 | `check[0].rows[4].text` | 56 Wörter, „uns“ | SUPPORTED | site-findings; curl `kontakt.html` H1 "Kontaktieren Sie uns". |
| 53 | `check[1].rows[0].text` | H1 ohne Ort | SUPPORTED | site.json `home_h1`. |
| 54 | `check[1].rows[1].text` | index.html gleicher Titel, 1.040 Wörter | SUPPORTED | site.json. |
| 55 | `check[1].rows[2].text` | Paar-Seite: Studio FRIEDA; Google-Eintrag und Impressum: Krebsmühle 5 | SUPPORTED | `Paar.html` JSON-LD "Zinkenwehr 5, Coburg"; Impressum body "Krebsmühle 5, 96482 Ahorn-Schorkendorf". Note: "Dein Google-Eintrag" is singular, she has 3 (see Optional). |
| 56 | `check[1].rows[3].text` | Beschreibung mit Leistung und Ort | SUPPORTED | site.json `home_meta`. |
| 57 | `check[1].rows[4].text` | 614 vs. 421 | SUPPORTED | factcheck-auto + comp-pages.json. |
| 58 | `check[2].rows[0].text` | Keine Besuchermessung; du siehst nicht, wie viele Besucher von Google kommen | SUPPORTED (sentence 1) / UNSUPPORTED (sentence 2) | curl of 15 pages: no gtag, GTM, Matomo, Plausible, Umami, Clarity, etracker. Not checked: Google Search Console or Cloudflare analytics (the site runs on Cloudflare). |
| 59 | `check[2].rows[1].text` | Startseite ohne Daten für Google; „Deine Paar-Seite hat das schon“ | WRONG (part) | curl `Paar.html` JSON-LD: LocalBusiness with address, Service, 3 Offers. No opening hours. The sentence says address, hours and services. |
| 60 | `check[2].rows[2].text` | Keine Seitenliste, „Nicht gefunden“ | SUPPORTED | curl `/sitemap.xml` = 404. |
| 61 | `check[3].rows[4].text` | Werberecht: Reiki-Seite „in der Nachsorge bei Krebserkrankungen“ | SUPPORTED | curl `besuch.html`: "Weltweit gesehen, ist REIKI vor allem in der Nachsorge bei Krebserkrankungen / REHA ...". Page H1 "Alternativmedizin", menu "Energiearbeit (Reiki)". Wording is neutral. |
| 62 | `system.step3.five[0..4]`, `note_draft` | 5-second test today and draft | SUPPORTED | home-today-1440.jpg, home-draft-1440.jpg ("5,0 bei Google · 15 Bewertungen", "Kostenloses Erstgespräch buchen", "in Coburg und Ahorn"). |
| 63 | `quick_wins[0..3]` | Hauptüberschrift, Paar-Seite, Sterne, Button; Buchungsseite gibt es | SUPPORTED | site-findings; `Buchung.html` curl 200. |
| 64 | `calc.volumes_line` | Mittel der letzten 12 Monate; 1,96 US-Dollar | SUPPORTED | dfs-volumes-ads.json (DataForSEO CPC is in USD; series mean 100, Google value 110). Note: demand.md table header says "CPC (EUR)". That is an error in demand.md, the page is correct. |
| 65 | `proof.h2`, `headlines.proof_h2` | Andere Heilpraktiker hatten ähnliche Lücken | WRONG (part) | case-library.json: abel = "Familienberatung · Raum Stuttgart", lengauer = "Innenarchitektur · Wien". 2 of 4 featured cases are not Heilpraktiker. `proof.lead` says this correctly. |
| 66 | `proof.lead` | Freiburg, Regensburg, Familienberatung bei Stuttgart, Betrieb aus Wien | SUPPORTED | case-library.json `sub` of laserstein, schlirf, abel, lengauer. |
| 67 | `proof.labels.laserstein`, `guide.celebrate` | Auch Heilpraktiker mit Psychotherapie; „Körperpsychotherapie“ Platz 1 | SUPPORTED | case-library.json laserstein: "Heilpraktiker · Freiburg", branch psychotherapie, jump "→ Platz 1", "„Körperpsychotherapie“". |
| 68 | `proof.more` | irmscher, menge, everitt, hengst, boehme | SUPPORTED | all 5 ids exist in case-library.json `more`. |
| 69 | `guide.think`, `step1.demand_note` | keine Suchzahl für Psychotherapie, Traumatherapie, EMDR, Burnout in Coburg | SUPPORTED | dfs-volumes-ads.json search_volume null. |
| 70 | `guide.insight` | Bewertungen zeigen, dass deine Klienten gern bewerten | UNSUPPORTED (interpretation) | google-panel: 15 reviews over about 5 years, newest about 1 year old. |
| 71 | `system.intro` | Jede Zahl unten aus echten Messungen, Rechner = Annahmen | SUPPORTED | Only non-measured value outside the calculator is `score_draft` 36, labelled "Ziel: 36+ / 44". |
| 72 | `roadmap[0].what` | Adresse auf der Paar-Seite angleichen | Recommendation, check | Couple sessions happen in Studio FRIEDA, Coburg (site-findings section 5). The Coburg entry is the visible one. Moving `Paar.html` to Krebsmühle 5 would work against it (see Optional). |
| **D. Health law, jargon, title** |||||
| 73 | whole page + `draft/index.html` | Never „Psychotherapeutin“ | PASS | 0 hits in prospect.json text and in draft/index.html. Title used: "Heilpraktikerin für Psychotherapie". |
| 74 | whole page | No healing or success promise | PASS | No "heilt", "Heilung", "garantiert", "wirksam". Promises in `hero_h1` and `grid.chips` are about Google visibility, not health. |
| 75 | `check[3].rows[4]` | Werberecht row neutral | PASS | Names the sentence, says "enge Werberegeln", offers to review together. No claim that the page is illegal. |
| 76 | whole page | Jargon | PASS | No SoLV, H1, Schema, NAP, Pool, Keyword, Backlink in visible text. Minor: "Hebel" (2x); "Patienten" (`steps[0].title`) vs. "Klienten" (`guide.insight`). |
| 77 | whole page | Image contradicts a claim | FAIL | Only #21 (north and east). All other grid claims match the image. |

Claims checked: 77 rows (covering about 110 fields). SUPPORTED or PASS: 58. UNSUPPORTED (full or part): 9. WRONG (full or part): 6. Other: 4 (1 recommendation check, 1 FAIL that repeats #21, 2 split verdicts counted once).

## Must fix

1. **`grid.caption_today` (WRONG, image contradicts).** "fast im ganzen Norden und Osten steht „20+“". The north-west and the south-east show ranks 10 to 20. Fix: "In der Stadtmitte und im ganzen Nordosten steht „20+“."
2. **`grid.caption_goal` (WRONG, misleading).** The goal is the centre. At the centre, rank 1 is Duygu Doganay with 19 reviews (more than her 15). Fix: "Die vier Praxen mit dem größten Anteil der Karte haben 0 bis 11 Bewertungen, du hast schon 15." Do not connect this sentence to the centre.
3. **`system.step1.depth.title` (UNSUPPORTED cause).** The evidence does not show that the H1 is the gap. The pages in front also lack Paartherapie + Coburg in the H1 (0 of 5). Fix: "Die Länge ist nicht die Lücke. Coburg in Titel und Überschrift ist eine einfache Chance."
4. **`check[2].rows[1].text` (WRONG part).** `Paar.html` has address and services in Google form, but no hours. Fix: "Deine Paar-Seite hat Adresse und Leistung schon in dieser Form, aber keine Zeiten."
5. **`check[3].rows[2]` title and `system.step2.cleanup[1].text` (UNSUPPORTED title).** The search result also holds a Google panel with reviews, which can be hers. Fix the title to "„therapie sasch“ führt nicht zu deiner Website" and the text to "... nicht unter den ersten 9 normalen Treffern". Or check the panel in the next Chrome job and keep "schwach" only if the panel is not hers.
6. **`system.step2.cleanup[0].text` and `check[3].rows[3].text` (WRONG, misleading).** Only 2 of 38 are casino or betting sites. "unseriös" is our reading of a third-party score. Fix: "38 von 1.018 Websites, die auf dich verlinken, haben einen hohen Spam-Wert, meist automatische SEO-Prüfseiten, dazu eine Casino- und eine Wettseite."
7. **`proof.h2` and `headlines.proof_h2` (WRONG part).** 2 of 4 featured cases are not Heilpraktiker. Fix: "Andere Praxen hatten ähnliche Lücken im Google-Eintrag. So hat sich ihr Platz verändert."
8. **Services gap not in evidence: `system.step2.changes[2]`, `roadmap[1].what`, `proof.lead` (UNSUPPORTED).** No file shows the "Leistungen" of her 3 entries. Fix: check the services tab of entries 1 and 3 in the next Chrome job. If not checked, change `changes[2].title` to "Leistungen prüfen und ergänzen", and end `proof.lead` with "... das auch bei dir fehlt: die passende Einordnung bei Google."
9. **`check[2].rows[0].text` sentence 2 (UNSUPPORTED).** We did not check Search Console or Cloudflare analytics. Fix: replace "Du siehst nicht, wie viele Besucher von Google kommen." with "Mit einer Messung siehst du, wie viele Besucher von Google kommen."

## Optional (wording, not facts)

- `system.step2.changes[0].title` and `roadmap[1].what`: "drei Einträge zusammenbringen" reads as one entry. The text keeps one entry per place (two). Use "Deine drei Einträge ordnen".
- `roadmap[0].what` "Adresse auf der Paar-Seite angleichen": couple sessions are in Coburg, and the Coburg entry is the visible one. Better: "Schreibweise Zinkenwehr / Zinkenweg bei Google und auf der Website angleichen".
- `system.step2.changes[3].text` "bringt wieder neue" → "kann wieder neue bringen".
- `guide.insight` "dass deine Klienten gern bewerten" → "dass deine Klienten zufrieden sind" or delete. 15 reviews in about 5 years.
- `system.steps[0].title` "Patienten" vs. `guide.insight` "Klienten": use one word.
- `check[1].rows[2].text` "Dein Google-Eintrag" → "Dein Haupteintrag bei Google" (she has 3).
- `system.step2.meaning`: say that Bartsch is 2,7 km from the centre and she is 4,3 km, so the reader sees the gap is not the same.
- Side note (draft, not page): `about.html` says "2020 ... Zulassung", Impressum says "Erlaubnis vom 18.11.2019". The draft uses 2019 (Impressum). That is correct.
