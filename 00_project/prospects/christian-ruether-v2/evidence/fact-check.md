# Fact check (agent F): Christian Ruether v2, 2026-10-12

Checker: agent F (did not write the page). Start 10:14:28, end 10:19:21. 86 claims checked. No browser. No paid call.
Input: `prospect.json`. Base: `evidence/factcheck-auto.md` (162 numbers, 0 mechanical errors).
Extra live checks (curl, free):
- All 128 sitemap URLs (page + post sitemap): 0 pages with `href="tel:`. 1 page with a `<form>` (`/anmeldung/`). Only `/2015/08/willkommen/` links to `/angebote/`.
- Live quotes found: "++43-699-11114398" (home footer), "Mein neues Buch ist jetzt draußen.", "Derzeit biete ich selbst keine offenen Workshops an", "Ihre Kontaktdaten einfügen" (Impressum), "werktags 8-17 Uhr", "07./08. Oktober 2025" (`/anmeldung/`), "derzeit keine Angebote" (`/termine/`). The word "Wien" occurs 0 times in the home HTML.
- Scan time: timestamp 1791770707 = 12.10.2026 04:05 Wien time. "Messung vom 12.10.2026" is correct.

## 1. Table "For the fresh agent: check only these claims"

| # | Field | Claim | Verdict | Evidence |
|---|---|---|---|---|
| 1 | `hero.cards[1].badge` | An allen 49 Punkten nicht unter den ersten 20 | SUPPORTED | scan-grid.png: 49 of 49 pins red "20+"; competitors.md found_in 0 of 49 |
| 2 | `grid.caption_today` | An allen 49 Punkten „20+“ | SUPPORTED | scan-grid.png (49 red "20+", no other colour) |
| 3 | `system.step1.items[4].why` | Tagessätze auf einer Seite, zu der nur ein Link führt, aus einem Beitrag von 2015 | SUPPORTED | site-findings.md §1; curl of 128 sitemap URLs: only /2015/08/willkommen/ links to /angebote/ |
| 4 | `system.step2.lead` | EFS steht nur auf rund 16 % der Karte unter den ersten drei | SUPPORTED | competitors.md SoLV 16,33 %; best SoLV in report |
| 5 | `system.step2.changes[0].text` | Alle vier vorn als „Unternehmensberater“ eingeordnet | SUPPORTED | competitors.md table (all 4: Unternehmensberater) |
| 6 | `system.step2.changes[1].title` | Alle Leistungen eintragen | SUPPORTED (advice, not a fact) | Services listed match site-findings.md §2a, §2d |
| 7 | `system.step2.changes[4].text` | Eintrag zeigt nur ein Street-View-Bild | SUPPORTED | google-panel-2026-10-12.md ("only a Street View / 360° photo") |
| 8 | `system.step2.cleanup[2].text` | Nummer im Fuß jeder Seite nur als Text, Tippfehler „++43“ | SUPPORTED | site-findings.md §1; curl home footer "++43-699-11114398"; 0 of 128 pages with tel link |
| 9 | `system.step2.good` | „Er führt nur noch nicht zu Anfragen.“ | UNSUPPORTED | No file has data on his enquiries. We cannot know that the reputation brings no enquiries |
| 10 | `system.step3.five[0].a` | Was? Nur aus dem Menüpunkt „Was ist Soziokratie?“ | SUPPORTED | scorecard-today.md #1; home-today-1440.jpg |
| 11 | `system.step3.five[1].a` | Wien nicht im ersten Bildschirm, Adresse nur im Impressum | SUPPORTED | scorecard-today.md #18; curl: "Wien" 0 times in home HTML |
| 12 | `system.step3.five[3].a` | „Nur ‚See More‘. Kein Button, keine antippbare Nummer.“ | WRONG (part) | home-today-1440.jpg and scorecard #4: "See More" IS a button (scroll button). "Keine antippbare Nummer" is correct |
| 13 | `check[0].rows[4].title/text` | Immer verschlüsselt, immer mit Schloss-Symbol | SUPPORTED | site.json `http_redirects_to_https: true`; site-findings.md §1 (non-www also ends on https) |
| 14 | `check[1].rows[1].text` | Bei Google heißt sie nur „Soziokratie“ | SUPPORTED | site.json `home_title: "Soziokratie"` |
| 15 | `check[1].rows[3].text` | Nur ein Link aus einem Beitrag von 2015 führt hin | SUPPORTED | as #3 |
| 16 | `quick_wins[2].text` | Heute führt nur ein Link von 2015 dorthin | SUPPORTED | as #3 |
| 17 | `quick_wins[4].text` | Heute zeigt er nur ein Street-View-Bild | SUPPORTED | as #7 |
| 18 | `guide.point` (1) | An allen 49 Messpunkten nicht unter den ersten 20 | SUPPORTED | as #1 |
| 19 | `guide.point` (2) | Erster Anbieter nur auf rund 16 % unter den ersten drei | SUPPORTED | as #4 |
| 20 | (text) | konsent moderation + konsent entscheidung | SUPPORTED | demand_note says "Google zählt … mit". No sum. Demand list shows "konsent moderation" only once |
| 21 | (text) | was ist soziokratie + soziokratie ausbildung | SUPPORTED | Same as #20. Demand list shows "was ist soziokratie" only once |

## 2. Map claims (scan-grid.png + competitors.md)

| # | Field | Claim | Verdict | Evidence |
|---|---|---|---|---|
| 22 | `grid.h2`, `headlines.grid_h2` | An keinem der 49 Punkte unter den ersten 20 | SUPPORTED | scan-grid.png; competitors.md |
| 23 | `grid.intro` | 49 Punkte, 5-km-Umkreis, Stephansplatz, 12.10.2026, „organisationsberatung wien“ | SUPPORTED | competitors.md (7x7, 5 km, 48.2085/16.3731); report time 12.10.2026 04:05 Wien |
| 24 | `grid.intro` | „Jede Zahl ist dein Platz an genau diesem Ort.“ | SUPPORTED (note) | All pins show "20+", not a place number. Acceptable, because caption explains "20+" |
| 25 | `grid.caption_today` | Gilt auch in der Stadtmitte und rund um die Neustiftgasse | SUPPORTED | scan-grid.png: centre pin (Vienna) and Neubau/Josefstadt pins all "20+"; competitors.md centre rank 20+ |
| 26 | `grid.caption_today` | EFS rund 16 % unter den ersten drei, 34 Bewertungen | SUPPORTED | competitors.md (16,33 %, 4,6 / 34) |
| 27 | `grid.caption_goal` | „Unter den ersten drei im ganzen Umkreis.“ | SUPPORTED as goal only | It is the goal caption. It must carry a visible "Ziel" label (see Should fix) |
| 28 | `grid.caption_goal` | Kein Anbieter über rund 16 %; vier vorn 15 bis 60 Bewertungen | SUPPORTED | competitors.md (best 16,33 %; reviews 34/15/60/29) |
| 29 | `system.steps[1].kpi` | „an 0 von 49 Punkten überhaupt zu sehen“ | WRONG | The scan measures the first 20 places only (competitors.md: arp 21 = report default for "not found"). "Überhaupt zu sehen" claims more than the data shows |
| 30 | `hero.cards[1].sub` | unter den ersten drei an 0 von 49 Punkten | SUPPORTED | competitors.md SoLV 0 % |
| 31 | `hero.cards[2].sub` | Du: 0 · EFS: 34 | SUPPORTED | google-panel (0); competitors.md (34) |
| 32 | `system.step2.h2` | Vier vorn: 15 bis 60 Bewertungen und eine klare Einordnung; dein Eintrag beides nicht | SUPPORTED | competitors.md; google-panel (0 reviews, no category); falcon report `claimed: False` is NOT used on the page (correct) |
| 33 | `system.step2.table` | Names, categories, reviews, 16,3 / 12,2 / 10,2 / 10,2 % | SUPPORTED | competitors.md; draft-facts.json top4 |
| 34 | `system.step2.fine` | Prozent = Anteil der 49 Punkte unter den ersten drei | SUPPORTED | 16,33 % = 8 of 49 points; competitors.md |
| 35 | `system.step2.meaning` | Allgemeine Unternehmensberater, keiner auf Soziokratie spezialisiert | SUPPORTED | competitors.md notes |
| 36 | `system.step2.meaning` | Deine Adresse rund 2 km von der Stadtmitte, vier vorn 0,7 bis 4,6 km | SUPPORTED | draft-facts.json me_km 2.02, km_range 0.71–4.6 |
| 37 | `check[3].rows[2].text` | Google zeigt „in: Cult Café“, Neustiftgasse 89-91 | SUPPORTED | google-panel-2026-10-12.md |

## 3. Text claims (not numbers)

| # | Field | Claim | Verdict | Evidence |
|---|---|---|---|---|
| 38 | `hero.sub`, `headlines.hero_sub` | „christian rüther soziokratie“ → Website auf Platz 1 | SUPPORTED | demand.md §5; draft-facts names own_rank 1 |
| 39 | `hero.sub` | Eintrag hat 0 Bewertungen und keine Einordnung | SUPPORTED | google-panel; maps-match.md |
| 40 | `hero.sub` | „auf der Website fehlt ein Weg zum Erstgespräch“ | UNSUPPORTED as worded | site-findings.md §1: mailto link and phone as text exist. A direct path (button, form, tel link) is missing, not every path |
| 41 | `hero.cards[0].sub` | Soziokratie-Beratung · KonsenT-Moderation · Workshops · Wien | SUPPORTED | homepage.md (real offer); Impressum address Wien |
| 42 | `hero.cards[3].sub` | Erster Bildschirm: Foto-Collage und „See More“, kein Telefon | SUPPORTED | home-today-1440.jpg; scorecard #1, #4 |
| 43 | `headlines.hero_h1` | Bei „soziokratie“ Website auf Platz 1 | SUPPORTED | demand.md §2 (dfs-serp-1.json pos 1, /was-ist-soziokratie/) |
| 44 | `system.step1.h2` | Erklärseiten auf Platz 1; Seite für Organisationsberatung in Wien fehlt | SUPPORTED | dfs-serp-1 (pos 1), dfs-serp-3 (pos 1); dfs-serp-4: soziokratie.org 0 hits |
| 45 | `system.step1.demand` | 9 terms with volumes, merged variants shown once | SUPPORTED | demand.md §1 |
| 46 | `system.step1.demand_note` | „moderation wien“: vor allem Moderatoren für Feiern und Fernsehen | SUPPORTED (wording) | dfs-serp-2.json: event and fair hosts, TV/radio, job boards, training. "Feiern" is not exact; "Events" is the correct word |
| 47 | `system.step1.depth.title/sub` | „Deine Seiten sind lang genug.“ | UNSUPPORTED | site-findings.md §4: about 600 words per page are sidebar. Main text of offer pages is 119–343 words, below the competitor mean 700 |
| 48 | `system.step1.depth.note` | Keine der fünf Seiten nennt Organisationsberatung und Wien zusammen in der Hauptüberschrift | SUPPORTED | site-findings.md §4 H1 list; draft-facts h1_keyword 0/5 |
| 49 | `system.step1.depth.note` | Startseite hat keine Hauptüberschrift, erste heißt „Willkommen“ | SUPPORTED | site.json `home_h1: []`; scorecard #2 |
| 50 | `system.step1.items[1].why` | Website nicht unter den ersten 20 für „organisationsberatung wien“ | SUPPORTED | dfs-serp-4.json (0 hits for soziokratie.org) |
| 51 | `system.step1.items[2].why` | Von „Was ist Soziokratie?“ kein Formular, keine antippbare Nummer | SUPPORTED | curl 128 pages: 0 tel links; only form on /anmeldung/ |
| 52 | `system.step1.items[3].why` | „konsent moderation“ Platz 1; „Die Seite endet heute bei einer E-Mail-Adresse“ | SUPPORTED (wording) | dfs-serp-3 pos 1. Main text ends with the offer list, not with an e-mail. The only written contact path is the e-mail (site-findings §3 #12) |
| 53 | `system.step1.items[5].why` | Vier Seiten „derzeit keine Angebote/Termine“; Formular bietet Oktober 2025 | SUPPORTED | site-findings.md §3 #2–#5; curl /anmeldung/, /termine/ |
| 54 | `system.step2.changes[1].text` | Coaching und Mediation als Leistung | SUPPORTED | site-findings.md §2a (/angebote/ price list) |
| 55 | `system.step2.changes[5].text` | „Öffnungszeiten hinzufügen“; Impressum werktags 8 bis 17 Uhr | SUPPORTED | google-panel; curl Impressum "werktags 8-17 Uhr" |
| 56 | `system.step2.cleanup[0]` | 47 / 319 unseriös, z. B. Casino- und Wettseiten | SUPPORTED | demand.md §6 |
| 57 | `system.step2.cleanup[1]` | „soziokratie.org“: nicht unter den ersten 9; davor vor allem Soziokratie Zentrum | SUPPORTED | dfs-serp-name.json: 9 organic, 7 of them soziokratiezentrum.org |
| 58 | `system.step2.cleanup[3]` | Mustertext „[Ihre Kontaktdaten einfügen]“ | SUPPORTED | site-findings §3 #14; curl Impressum |
| 59 | `system.step2.good` | Website Platz 1 bei Name, „soziokratie“, „konsent moderation“ | SUPPORTED | demand.md §2, §5 |
| 60 | `system.step3.lead` | 22 Punkte; Entwurf mit Name, Foto, Buch | SUPPORTED | scorecard-today.md; home-draft-1440.jpg |
| 61 | `system.step3.note_today` | Großes Foto mit vielen Gesichtern, keine Überschrift, kein Telefon, Cookie-Fenster unten | SUPPORTED | home-today-1440.jpg |
| 62 | `system.step3.note_today` | „kein Button im ersten Bildschirm“ | WRONG | home-today-1440.jpg: the "See More" button is in the first screen |
| 63 | `system.step3.five[2].a`, `five[4].a` | Buch/Masterthesis weiter unten als Links; Foto in der Seitenleiste | SUPPORTED | scorecard #8, #14 |
| 64 | `calc.volumes_line` | Klick „rund 5,35 US-Dollar“, „der Regler startet bei 5,30 €“ | WRONG (unit) | dfs-volumes-ads.json: 5.35 is USD. The page turns it into € without conversion |
| 65 | `calc.volumes_line` | Startwert 1.200 Euro = untere Grenze Tagessatz Non-Profit | SUPPORTED | site-findings.md §2a |
| 66 | `check[0].rows[0]` | Auf keiner gemessenen Seite ist die Nummer ein Link | SUPPORTED | site-pages.json; curl 0 of 128 |
| 67 | `check[0].rows[1]` | „Keine Kontakt-Seite, kein Formular“; „Jeder Weg endet bei einer E-Mail-Adresse“ | UNSUPPORTED as worded | Title says "kein Formular", text says one form exists (/anmeldung/). The phone is also shown as text. Correct: no contact page, no enquiry form |
| 68 | `check[0].rows[2]`, `[3]` | Oktober 2025 im Formular; rund 1,4 s | SUPPORTED | curl /anmeldung/; site.json ttfb 1.31–1.40 |
| 69 | `check[1].rows[2]` | Beschreibung „Umfassende Materialsammlung …“, ohne Beratung in Wien | SUPPORTED | site.json home_meta |
| 70 | `check[1].rows[4]` | status ok „Ausführliche Texte“: 966 Wörter vs. Mittel 700 | UNSUPPORTED (misleading) | site-findings.md §4: about 600 of the 966 words are the sidebar. Main text is about 366 words |
| 71 | `check[2].rows[0]` | Besuchermessung eingebaut | SUPPORTED | site.json ga4 G-B1S9LNDXG4 |
| 72 | `check[2].rows[1]`, `[2]` | Keine Anfrage-Messung; Daten nicht in maschinenlesbarer Form | SUPPORTED | site.json (gtm [], no tel, no form); site-findings §1 (no LocalBusiness data) |
| 73 | `check[3].rows[3]` | Casino-, Wett- und nachgemachte Nachrichtenseiten | SUPPORTED | demand.md §6 (forbesstories.com, theforbestimes.com) |
| 74 | `quick_wins[3].text` | „Derzeit keine Angebote“, Oktober 2025, „Mein neues Buch“ aus 2022 | SUPPORTED | site-findings §3 #2, #5, #9; curl home |
| 75 | `quick_wins[5].text` | „Heute endet jeder Weg bei einer einzigen E-Mail-Adresse.“ | UNSUPPORTED as worded | Phone text in the footer and the workshop form exist (see #67) |
| 76 | `guide.think` | Für „soziokratie wien“ keine Suchzahl | SUPPORTED | demand.md §1 no_data |
| 77 | `guide.celebrate` | Lengauer, Wien, „Interior Design Wien“ Platz 18 → 1 | SUPPORTED | case-library.json lengauer (jump "Platz 18 → 1", city wien) |
| 78 | `proof.featured` | lengauer, abel, schlirf, laserstein exist | SUPPORTED | case-library.json |
| 79 | `proof.lead` | Ein Betrieb aus Wien, eine Beratung, zwei Selbstständige | SUPPORTED | case-library.json (lengauer wien; abel Familienberatung; schlirf, laserstein) |
| 80 | `proof.lead` | Bei denen Einordnung, fehlende Leistungen UND fehlende Bewertungen der Engpass waren | WRONG (part) | case-library.json gaps: lengauer has no "bewertungen"; schlirf has no "kategorien". All three gaps fit only abel and laserstein |
| 81 | `headlines.proof_h2` | „Heute stehen sie oben.“ | UNSUPPORTED | case-library.json gives results at the end of the work, not today's position |
| 82 | `roadmap`, `headlines.roadmap_h2`, `hero_h1` | Plan für 8 Wochen | SUPPORTED | roadmap weeks 1–8 plus "Laufend" |

## 4. Promises, jargon, claim status, medical words

| # | Check | Result |
|---|---|---|
| 83 | Result promises | No hard guarantee. Soft outcome wording: `grid.chips` ("Organisationen aus ganz Wien finden dich", "Mehr Anfragen für ein Erstgespräch"), `grid.caption_goal` (no "Ziel" word in the text), `steps[1].title` "Damit das Telefon klingelt", roadmap "Telefon klingeln", `final.p` "wie aus diesen Punkten mehr Anfragen werden", `final.h2` "wie du dorthin kommst". Flag: Should fix |
| 84 | Jargon (Pool, H1, SoLV, Schema, Keyword, SERP, Backlink, NAP) | None in visible fields. "H1" occurs only in `sources` (internal). One minor term: "B2B-Dienstleister" in `step2.table[1].cats` |
| 85 | "unclaimed" / profile not claimed | None. The page does not say the profile is not claimed (falcon report `claimed: False` and "Als Inhaber eintragen" are not used). OK |
| 86 | Medical words for him ("Praxis", "Patient") | None in prospect.json. The draft image has "Praxisleitfaden" (book subtitle), which is OK. Note: 2 of 4 featured cases are Heilpraktiker (schlirf, laserstein); their cards show that word about them, not about him |

## Must fix

1. `system.steps[1].kpi` "an 0 von 49 Punkten überhaupt zu sehen" → "an 0 von 49 Punkten unter den ersten 20". The scan measures the first 20 places only.
2. `system.step2.good` "Er führt nur noch nicht zu Anfragen." → remove, or "Von dort führt aber noch kein direkter Weg zum Erstgespräch." No data on his enquiries exists.
3. `check[1].rows[4]` (status ok, "Ausführliche Texte", 966 vs. 700) and `system.step1.depth.sub` "Deine Seiten sind lang genug." About 600 of 966 words are the sidebar (site-findings.md §4). Change the row to warn or remove it. Change the sub to "Viel Text, aber rund 600 Wörter davon stehen in der Seitenleiste." Keep the bar "966" only with this note next to it.
4. `calc.volumes_line` "5,35 US-Dollar … Regler startet bei 5,30 €". Do not change the unit without conversion. Show the slider in US-Dollar, or convert and give the rate.
5. `system.step3.note_today` "kein Button" and `system.step3.five[3].a` "Kein Button": "See More" is a button. Write "kein Button für eine Anfrage".
6. `proof.lead`: not all four cases had all three gaps (case-library.json). Write "bei denen Einordnung, Leistungen oder Bewertungen im Google-Eintrag fehlten".
7. `headlines.proof_h2` "Heute stehen sie oben." → "Danach standen sie oben." (results at the end of the work, case-library.json).

## Should fix

- `hero.sub` "auf der Website fehlt ein Weg zum Erstgespräch" → "fehlt ein direkter Weg zum Erstgespräch (Button, Formular, antippbare Nummer)". He is sceptical ("Verkaufsmasche", chat 28.09.). He can disprove the absolute version.
- `check[0].rows[1]` title "kein Formular" → "kein Anfrage-Formular". Text "Jeder Weg endet bei einer E-Mail-Adresse" → "Für Anfragen gibt es nur eine E-Mail-Adresse und die Nummer als Text". Same fix in `quick_wins[5].text` and `system.step1.items[3].why`.
- `system.step1.demand_note` "Moderatoren für Feiern und Fernsehen" → "Moderatoren für Events und Fernsehen" (dfs-serp-2.json).
- `grid.caption_goal`: start with "Ziel:" so the reader sees a goal, not a promise.
- `step2.table[1].cats` "B2B-Dienstleister" → "Dienstleister für Firmen".

## Notes (no change needed)

- Falcon report: the Google entry links to `soziokratie.org/impressum/`, not to the home page. This is a possible extra quick win. It is not on the page today.
- Chat 09.10.: Christian wrote "Ich habe noch die Seite ‚Soziokratie‘, die für Soziokratie-Beratung steht." This can also mean the Google entry named "Soziokratie". The message of 05.10. said that no Google profile exists. The v2 page correctly says that an entry exists.
- `sources.step1.depth` calls the 5 competitor pages "homepages". They are sub-pages. Internal only.
