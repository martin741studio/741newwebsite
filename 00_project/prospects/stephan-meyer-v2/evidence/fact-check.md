# Fact check (agent F): Dr. Stephan Meyer, prospect.json (2026-10-12, 15:24 to 15:30)

Scope: the rows in `factcheck-auto.md` ("For the fresh agent"), the map claims, the non-number claims in `prospect.json`, and the flags (place, "unclaimed", promises, jargon, medical words, tone).
Method: local files only. One curl to `/about/` returned 403 (site firewall). No more requests. No browser. No paid call.
Verdicts: SUPPORTED (file + value), UNSUPPORTED (no evidence), WRONG (evidence says something else).

## 1. Rows from factcheck-auto.md

| # | Field | Claim | Verdict | Evidence / note |
|---|---|---|---|---|
| 1 | `calc.val`, `calc.volumes_line` | 1500 / 1.500 € | SUPPORTED as assumption | site-findings.md §5: no price on the site. The page labels it "eine Annahme". See tone note T3. |
| 2 | `grid.h2`, `headlines.grid_h2` | "an allen 49 Punkten andere Anbieter vor dir" | SUPPORTED | falcon report: found_in 0, arp 21; scan-grid.png: 49 × "20+" |
| 3 | `grid.intro` | "nur ein Nebenbefund", rund 10 Suchen | SUPPORTED | demand.md: business coach jena 10 |
| 4 | `grid.caption_today` | "An allen 49 Punkten „20+“" | SUPPORTED | scan-grid.png (checked by eye: 49 red "20+" markers, centre too) |
| 5 | `grid.caption_goal` | "nur zur Veranschaulichung" | SUPPORTED (label) | Content of the same caption: see #34 |
| 6 | `grid.chips[0]` | "nicht nur als Unternehmensberater" | SUPPORTED | google-panel: Unternehmensberater; falcon: 3 categories, none coach |
| 7 | `system.step1.items[1].why` | Begriff "nur in Blogbeiträgen" | SUPPORTED | site-findings.md §4 |
| 8 | `system.step1.items[2].why` | Seite heißt bei Google "nur „Coach \| Dr. Stephan Meyer“" | SUPPORTED | dfs-serp-name2.json rank 8, url /de/coach/ |
| 9 | `system.step1.items[4].why` | /de/coach/ fehlt "wie alle deutschen Seiten" in der Liste | WRONG | The sitemap holds 500+ German blog posts (site-findings.md §1, §4). Only the pages under /de/ are missing. |
| 10 | `system.step2.lead` | vier ersten "an allen 49 Messpunkten unter den ersten 20" | SUPPORTED | falcon: found_in 49 for all four |
| 11 | `system.step2.changes[0].text` | "nur Unternehmensberater, Dienstleister und Personalberatung" | SUPPORTED (with note) | falcon categories. "Dienstleister" is our translation; competitors.md says "Dienstleistungsbetrieb". |
| 12 | `system.step2.changes[1].title` | "Alle Leistungen eintragen" | UNSUPPORTED premise | No evidence file records the services list of his Google entry. google-panel file is silent on it. |
| 13 | `system.step2.changes[5].text` | "alle zwei Wochen" | SUPPORTED (advice) | No fact claim |
| 14 | `system.step3.five[2].a` | "Nur „Dr.“ im Kopf der Seite" | SUPPORTED | scorecard-today.md #8, homepage.md |
| 15 | `system.step3.five[3].a` | Buchung "nur auf der Kontaktseite" | SUPPORTED | scorecard-today.md #9 (website only) |
| 16 | `system.step3.five[4].a` | Name "nur im Kopf der Seite" | SUPPORTED for first screen only | site.json home_h1 #3 "Dr. Stephan Meyer – Outstanding in his field" lower on the page. Add "im ersten Bildschirm". |
| 17 | `check[0].rows[1].text` | "use the form below", darunter "nur die Buchung" | SUPPORTED | site-findings.md §2 (/contact/) |
| 18 | `check[0].rows[4]` | "Immer verschlüsselt" | SUPPORTED | site.json http_redirects_to_https true |
| 19 | `check[3].rows[0].text` | drei Stimmen "nur mit Kürzeln" | SUPPORTED | scorecard-today.md #12 (B.L., J.S., S.R.) |
| 20 | `quick_wins[4].text` | "Für alle, die…" | SUPPORTED (no fact) | |
| 21 | `guide.point` | "nur rund 10 Mal im Monat" | SUPPORTED | demand.md |
| 22 | (text) | executive coach + executive coaching | SUPPORTED | demand_note: "Google zählt … mit". Calc shows 210 once. Never added up. |

## 2. Map claims (scan-grid.png, competitors.md, falcon report)

| # | Field | Claim | Verdict | Evidence |
|---|---|---|---|---|
| 23 | Required | Page says Jena keyword has about 10 searches a month | SUPPORTED | Said in `grid.intro`, `hero.cards[1].badge`, `step2.lead`, `guide.point`, `demand_note` |
| 24 | `hero.cards[1].sub`, `steps[1].kpi` | 0 von 49 unter den ersten drei / ersten 20 | SUPPORTED | falcon solv 0, found_in 0 |
| 25 | `hero.cards[1].badge` | "Auch in der Stadtmitte nicht unter den ersten 20" | SUPPORTED | scan-grid.png centre (row 4, col 4) "20+" |
| 26 | `grid.intro` | 49 Punkte, 5-km-Umkreis, Stadtmitte Jena, 12.10.2026 | SUPPORTED | falcon: 7×7, radius 5.0 km, centre 50.9271/11.5892, date 10/12/2026 |
| 27 | `grid.caption_today` | Eintrag rund 53 km von Jena verortet | SUPPORTED | draft-facts.json me_km 53.35; falcon lat 50.44971 / lng 11.51357 |
| 28 | `grid.caption_today` | Spantzel rund 91,8 % unter den ersten drei, 39 Bewertungen | SUPPORTED | falcon solv 91.84, reviews 39 |
| 29 | `step2.table` | names, reviews 0/39/3/23/1, shares 0/91,8/83,7/77,5/24,5 % | SUPPORTED | falcon places |
| 30 | `step2.table` cats | "Life Coach", "Coaching-Zentrum, Unternehmensberater" | SUPPORTED (with note) | falcon: English labels. German labels are our translation (competitors.md "Open points"). Lists are shortened: #2 also "Psychotherapist", #3 also "Health consultant". |
| 31 | `step2.fine` | Prozent = Anteil der 49 Punkte unter den ersten drei | SUPPORTED | falcon solv definition; 91.84 % = 45/49 |
| 32 | `step2.meaning` | 0,4 bis 1,7 km von der Stadtmitte; du rund 53 km | SUPPORTED | competitors.md distances 0,44 to 1,69 km |
| 33 | `step2.meaning` | "Vorn stehen Einträge, die Google als Life Coach oder Coaching-Zentrum einordnet. Dein Eintrag ist als Unternehmensberater eingeordnet." | WRONG (as written) | Only 3 of 4. SP Training & Consulting (24,5 %) is only "Unternehmensberater", the same as him. #2 and #3 also carry "Unternehmensberater". The table directly above shows this. |
| 34 | `grid.caption_goal` | Gemeinsam vorn: "eine Einordnung als Coach oder Berater" | WRONG (logic) | He is "Unternehmensberater", so "Berater" is no difference. The real difference: 3 of 4 have a coaching category, all 4 have reviews and a Jena address. |
| 35 | `step2.h2`, `changes[2]` | vier vorn 1 bis 39 Bewertungen, du 0 | SUPPORTED | falcon reviews; draft-facts reviews_range [1, 39] |
| 36 | `step2.lead` | Suche klein (rund 10 im Monat) | SUPPORTED | demand.md |

## 3. Non-number claims in prospect.json

| # | Field | Claim | Verdict | Evidence |
|---|---|---|---|---|
| 37 | `hero.sub`, `headlines.hero_sub` | Promotion, Diplom der RWTH Aachen, über 25 Jahre Erfahrung mit Wandel | SUPPORTED | homepage.md trust-row quotes from /about/ ("doctorate degree … 2019", "RWTH Aachen … Diplom-Psychologe", "more than 25 years of coordinating successful transformations"). Re-check of /about/ not possible today (403). |
| 38 | `headlines.hero_h1` sub-line | Website steht bei "führungskräfte coaching" nicht unter den ersten 20 | SUPPORTED | dfs-serp-1.json (DE, 19 organic, no stephanmeyer.com) |
| 39 | `headlines.hero_h1` sub-line, `step1.demand_note` | Website steht bei "business coach" nicht unter den ersten 20 | UNSUPPORTED | No SERP for national "business coach" exists. cost_ledger.jsonl: serp-1 = führungskräfte coaching, serp-2 = business coach jena (Jena). |
| 40 | `system.step1.lead` | Verglichen mit Seiten, die bei "führungskräfte coaching" und "business coach" oben stehen | WRONG | comp-pages.json: 3 pages from "führungskräfte coaching", 2 from "business coach jena" (dianawalther, vorwerg). None from "business coach". |
| 41 | `hero.cards[0]` | 0 Bewertungen, eingeordnet als Unternehmensberater | SUPPORTED | google-panel-2026-10-12.md |
| 42 | `hero.cards[3].sub`, `step3.note_today`, `five[0]` | Erster Bildschirm englisch, "Are you a visionary?", kein Angebot, Kopf abgeschnitten, "Start Now" / "Read More" | SUPPORTED | scorecard-today.md #1, #5, #8; site.json home_h1 |
| 43 | `step1.depth`, `check[1].rows[4]`, `step2.good` | Startseite 2.166 Wörter, mehr als Mittel 1.616 | SUPPORTED | site.json home_words; site-findings.md §8 |
| 44 | `step1.depth.note`, `items[0]`, `check[1].rows[1]` | 3 Hauptüberschriften, keine nennt Coaching / Angebot; H1-Beispiele der Wettbewerber | SUPPORTED | site.json home_h1; comp-pages / site-findings.md §8 |
| 45 | `step1.items[0]`, `five[1]` | Startseite englisch, deutsche Fassung unter /de/ | SUPPORTED | site-findings.md §1 |
| 46 | `step1.items[3]` | Anzeigen-Klick "change management beratung" rund 17,63 US-Dollar | SUPPORTED | dfs-volumes-ads.json cpc 17.63 |
| 47 | `step1.items[4].title` | Seite /de/coach/ "bei Google bekannt machen" | WRONG (implied) | Google already shows /de/coach/: dfs-serp-name2.json rank 8, url https://stephanmeyer.com/de/coach/. The page itself says "Platz 8" in `step2.cleanup[2]`. Only the sitemap entry is missing. |
| 48 | `step1.items[5]`, `check[1].rows[3]` | rund 1.940 Adressen, 10 echte Seiten; drei Beiträge Hannover; du/Sie gemischt | SUPPORTED | site.json sitemap_urls 1940; site-findings.md §3, §4 |
| 49 | `check[1].rows[0]` title + text | "Deutsche Seiten nicht an Google gemeldet"; Liste "enthält 10 Seiten, keine davon deutsch" | WRONG (as written) | The full list has 1.940 URLs with 500+ German posts. Only the 10-page sub-list has no /de/ page. The text also contradicts `check[1].rows[3]` (1.940). |
| 50 | `guide.insight` | "In der Liste … steht heute keine deutsche Seite." | WRONG | German blog posts are in the sitemap (site-findings.md §1, §4) |
| 51 | `quick_wins[1]`, `roadmap[0]` | "Deutsche Seiten an Google melden" | WRONG (wording) | Same as #49. Say "die Seiten unter /de/". |
| 52 | `check[1].rows[2]` | Google-Text für Startseite englisch ("change management consultant & executive coach …") | SUPPORTED | site.json home_meta; google-panel web result |
| 53 | `check[0].rows[0]`, `step2.cleanup[3]` | 0 antippbare Nummern; "Ruf mich einfach an" führt zur Kontaktseite; dort Videocall + Download-Formular | SUPPORTED | site.json tel_links []; site-findings.md §2 |
| 54 | `check[0].rows[1]` | keine E-Mail im Impressum | SUPPORTED | site-findings.md §2 |
| 55 | `check[0].rows[2]` | Seite beginnt nach rund 3,3 s zu laden | SUPPORTED (with note) | site.json ttfb 3.18/3.48/3.16. This is server response time from our location. Say so. |
| 56 | `check[0].rows[3]`, `step2.changes[4]`, `step2.good` | Videocall direkt buchbar; Eintrag hat Buchungslink | SUPPORTED | site-findings.md §2; google-panel (bookme.name) |
| 57 | `step2.changes[4]` | Eintrag ohne Nummer, "Telefonnummer hinzufügen" | SUPPORTED | google-panel |
| 58 | `step2.changes[5]` | letzter Beitrag 15.09.2026 | SUPPORTED | google-panel owner post |
| 59 | `step2.changes[1].text` | Leistungen: Executive Coaching … Business Wargaming | SUPPORTED | site-findings.md §5; demand.md |
| 60 | `roadmap[1].why` | Eintrag "ohne Leistungen" | UNSUPPORTED | Same as #12 |
| 61 | `check[2].rows[0]` | Besuchermessung eingebaut | SUPPORTED | site.json ga4 G-C1N1DP2T75 |
| 62 | `check[2].rows[2]` | Daten für Google zur Person, keine zu Leistungen | SUPPORTED | site-findings.md §9 (Person, WebPage, WebSite) |
| 63 | `check[3].rows[3]` | Zitate "verkürze die Transformationszeit um 50%", "Millionen von Euro an zusätzlichem Gewinn" | SUPPORTED | site-findings.md §6 (/de/, /de/coach/). See tone note T1. |
| 64 | `step2.cleanup[0]`, `check[3].rows[4]` | 63 von 1.139 unseriös; Beispiel bestnz-poker-casinoslot.com | SUPPORTED | dfs-refdomains-spam.json total_count 63; demand.md §6 |
| 65 | `step2.cleanup[1]`, `check[3].rows[2]` | "doctor change": Website nicht unter den ersten 8; englische Seiten über Arztwechsel | SUPPORTED (with note) | dfs-serp-name.json: 8 organic. 7 of 8 are about changing doctors; #5 is about doctors changing careers. Say "fast nur". |
| 66 | `step2.cleanup[2]`, `check[3].rows[1]` | stephanmeyer.biz Platz 1 und 2, anderer Stephan Meyer (Logistik); deine Website Platz 8 | SUPPORTED (with note) | dfs-serp-name2.json; site-findings.md §7. For fairness: Xing (#4) and his keynote site (#6) are his. |
| 67 | `step3.lead` | 22 Punkte; Entwurf mit Logo und Fotos | SUPPORTED | scorecard-today.md (22 rules); homepage.md |
| 68 | `grid.intro`, `hero.cards[0].sub` | Angebot "online per Videocall" | SUPPORTED (with note) | google-panel "Onlinetermine"; contact page. Keynotes and workshops are not online: say "dein Coaching läuft auch online". |
| 69 | `proof.lead` | kein Coach in der Fallsammlung; "eine Dienstleisterin, eine Beraterin und zwei Selbstständige" | SUPPORTED / MISLEADING | case-library.json: no coach. The "zwei Selbstständige" are schlirf ("Naturheilpraxis", Heilpraktikerin) and laserstein (Heilpraktiker, "Körperpsychotherapie"). The cards show this. |
| 70 | `guide.celebrate` | Lengauer "Interior Design Wien" Platz 18 auf 1 | SUPPORTED | case-library.json lengauer jump "Platz 18 → 1" |
| 71 | `guide.hello` | "mit einer Quelle zu jeder Zahl" | UNSUPPORTED | build_page.py does not render `sources`. The page does not show a source for each number. |
| 72 | `system.intro` | "Jede Zahl unten stammt aus echten Messungen" | SUPPORTED (with note) | Exceptions exist: target 36+/44 and roadmap weeks. Both carry a label ("Ziel", plan). |
| 73 | `calc.volumes_line` | 210 / 2.900 / 2.900, 6,94 US-Dollar, Abruf 12.10.2026 | SUPPORTED | dfs-volumes-ads.json |
| 74 | Draft image (`draft/index.html`) | "Promotion 2019 University of Gloucestershire, zu radikalem Wandel" | UNSUPPORTED (topic) | Year and university: homepage.md quote. The topic "zu radikalem Wandel" is in no evidence file. |
| 75 | Draft image | "Diplom-Psychologe RWTH Aachen", "Wirtschaftspsychologe", Kunden Allianz, Audi, Mercedes, PwC | SUPPORTED | homepage.md /about/ quote; site.json logo images |

## 4. Flags

| Flag | Result |
|---|---|
| Place claims (Wurzbach, Thüringen, Zypern) | PASS. None in prospect.json. "rund 53 km von Jena" comes from coordinates (draft-facts.json). |
| "unclaimed" / "nicht beansprucht" | PASS. Not on the page. Keep it off: falcon says claimed=false, but the panel shows an owner post (15.09.2026) and no "Als Inhaber eintragen". The old page (chat message 5) said "unclaimed"; that was not safe. |
| Jargon (H1, SoLV, Keyword, SERP, Backlink, Sitemap, Snippet, Schema) | PASS. None in visible text. Plain words used ("Hauptüberschrift", "Liste, die deine Website an Google meldet", "Daten für Google"). |
| Medical words in prospect.json | PASS for the text. FAIL for the rendered proof section (see Must fix 6). |
| Result promises | FAIL (soft): `headlines.hero_h1` "so finden Unternehmen … dein Führungskräfte-Coaching bei Google"; `grid.chips[2]` "Mehr gebuchte Erstgespräche per Videocall"; `final.p` "wie aus diesen Punkten mehr Anfragen werden". Lower risk: `headlines.system_h2` "für mehr Erstgespräche", `roadmap[2].why` "Aus Besuchern werden Erstgespräche". |
| Tone to an experienced consultant | T1: `check[3].rows[3]` "Auf skeptische Leser wirken sie unsicher." judges his own copy. T2: `step2.changes[3]` "Hier hört jemand zu" (to a coach) reads as a lesson. T3: `calc.val` 1.500 € per package is a low anchor for a coach who names VW, Audi, Novartis. T4: `calc.volumes_line` "der Regler startet ohne Umrechnung bei 6,90 €" mixes USD and EUR; this looks careless to a professional. T5: `headlines.step3_h2` "Besucher entscheiden in 5 Sekunden" has no source. |

## Must fix

1. **"business coach" national top 20 (UNSUPPORTED).** `headlines.hero_h1` sub-line ("bei beiden nicht unter den ersten 20") and `system.step1.demand_note` ("Bei „führungskräfte coaching“ und „business coach“ …"). No SERP exists for national "business coach". Limit the claim to "führungskräfte coaching", or run one SERP call (paid, Martin go).
2. **`system.step1.lead` (WRONG).** The 5 compared pages come from "führungskräfte coaching" (3) and "business coach jena" (2), not from "business coach".
3. **"keine deutsche Seite" (WRONG).** `guide.insight`, `system.step1.items[4].why` ("wie alle deutschen Seiten"), `check[1].rows[0]` title and text, `quick_wins[1].title`, `roadmap[0].what`. The sitemap holds 500+ German posts. Correct claim: no page under /de/ (/de/, /de/coach/, /de/trustedadvisor/, …) is in the list. Also remove the contradiction "Liste enthält 10 Seiten" vs. "1.940 Adressen".
4. **`system.step1.items[4].title` "bei Google bekannt machen" (WRONG).** Google already shows /de/coach/ (dfs-serp-name2.json, Platz 8). The page itself says Platz 8. Change it to "in die Liste für Google aufnehmen".
5. **Category logic (WRONG).** `system.step2.meaning` ("Vorn stehen Einträge, die Google als Life Coach oder Coaching-Zentrum einordnet") and `grid.caption_goal` ("Einordnung als Coach oder Berater"). SP Training & Consulting is only "Unternehmensberater", like him. #2 and #3 are also "Unternehmensberater". Write: "Drei der vier vorn haben eine Coaching-Einordnung. Alle vier haben Bewertungen und eine Adresse in Jena."
6. **Proof section shows health cases.** Featured `schlirf` ("Naturheilpraxis Veronika Schlirf", Heilpraktikerin) and `laserstein` (Heilpraktiker, "Körperpsychotherapie"). More: `menge` (Psychotherapie), `irmscher` (Heilpraktikerin Psychotherapie), `everitt` (Hypnosetherapie), `kuch` (Physiotherapie). This puts "Praxis" and therapy words on the page. `proof.lead` calls two Heilpraktiker "zwei Selbstständige", which reads as hiding it. Use non-health cases: lengauer, abel, mediaberater (Werbeagentur), doerfler (Kanzlei). Then rewrite `proof.lead` to match.
7. **Services in the Google entry (UNSUPPORTED).** `roadmap[1].why` ("ohne Leistungen") and `system.step2.changes[1].title` ("Alle Leistungen eintragen"). No file records his services list. Check the panel (free operator job) or write "Leistungen prüfen und ergänzen".
8. **`guide.hello` "mit einer Quelle zu jeder Zahl" (UNSUPPORTED).** The page does not render sources. Write, for example: "Alle Zahlen stammen aus Messungen vom 12.10.2026."
9. **Result promises.** `headlines.hero_h1` ("so finden Unternehmen …" → "so können Unternehmen … finden"), `grid.chips[2]` (remove "Mehr gebuchte Erstgespräche" or mark it as a goal), `final.p` ("wie aus diesen Punkten mehr Anfragen werden können").
10. **Draft image: "zu radikalem Wandel" (UNSUPPORTED).** The topic of the doctorate is in no evidence file. Remove it or verify on /about/ (site blocks curl today, 403).
11. **Tone T1.** Remove "Auf skeptische Leser wirken sie unsicher." from `check[3].rows[3]`. Keep the two quotes and the fact "ohne Beleg", or drop the row.

## Should fix (minor)

- `system.step3.five[4].a`: add "im ersten Bildschirm" (his name is in the 3rd H1 further down).
- `grid.intro`: "dein Angebot läuft online" → "dein Coaching läuft auch online" (keynotes and workshops are on site).
- `step2.table` / `changes[0]`: German category names are our translation. Use Google's German labels (competitors.md uses "Dienstleistungsbetrieb", not "Dienstleister").
- `step2.cleanup[1]`: "englische Seiten über einen Arztwechsel" → "fast nur" (7 of 8).
- `check[0].rows[2]`: say that 3,3 s is the server answer time in our measurement.
- `calc.volumes_line`: give the click price in one currency. Reconsider the 1.500 € start value (T3).
- `step2.cleanup[2]` / `check[3].rows[1]`: mention that Xing (#4) and his keynote site (#6) are his.
- `step2.changes[3]`: drop "Hier hört jemand zu".
- `headlines.step3_h2`: "Besucher entscheiden in 5 Sekunden" has no source; soften it.
