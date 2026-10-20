# Baseline: what Manuela already saw (https://741.studio/review/manuela-stetter/, page file 2026-10-14)

```json
{
 "status": "OK",
 "slug": "manuela-stetter",
 "review_url": "https://741.studio/review/manuela-stetter/",
 "page_date": "2026-10-14",
 "website": "https://heilpraktikerin-manuela-stetter.de",
 "first_name": "Manuela",
 "company": "Naturheilpraxis Manuela Stetter",
 "city": "Essenbach",
 "country": "DE",
 "branch": "health",
 "health": true,
 "health_reason": "branch=health",
 "data_files": [
  "prospect.json",
  "intake.json",
  "demand.md",
  "site-findings.md",
  "homepage.md",
  "competitors.md",
  "evidence/site.json",
  "evidence/dfs-volumes-ads.json"
 ],
 "version": "v2.1 (prospect.json)"
}
```

## demand.md (first 60 lines)

# Demand: Manuela Stetter (agent A, 2026-10-14)

Evidence files are in `evidence/`. Volumes are Google Ads monthly searches, Germany (2276), language de. Cost: 0,1498 USD (cap 0,30).

## 1. Her real services (site menu, `/leistungen/`, `/naturheilkunde/`, `/coaching/`)
Frauenheilkunde and Hormone, Menstruationsbeschwerden, PMS, Wechseljahre, Kinderwunsch, Endometriose, PCO, Hormonspeicheltest, Ernährungsberatung, Coaching, Kurse.

## 2. Volume table (evidence: `dfs-volumes-ads.json`)
| Term | Searches per month |
|---|---|
| heilpraktiker landshut | 320 |
| heilpraktikerin landshut | 320 |
| naturheilpraxis landshut | 10 |
| heilpraktiker essenbach | 20 |
| heilpraktiker dingolfing | 70 |
| kinderwunsch heilpraktiker | 480 |
| hormonspeicheltest | 210 |
| hormonspeicheltest kosten | 40 |
| heilpraktiker kosten | 880 |
| menstruationsbeschwerden naturheilkunde | 10 |
| pms naturheilkunde | 20 |
| frauenheilkunde naturheilkunde | Google gibt keine Zahl heraus |
| wechseljahre heilpraktiker landshut | Google gibt keine Zahl heraus |
| hormone heilpraktiker landshut | Google gibt keine Zahl heraus |

Merged variants (never add up): "heilpraktiker landshut" and "heilpraktikerin landshut" are one demand. Google shows 320 for each. Count it as 320, not 640. The two SERPs share 7 unique URLs (18 and 20 unique organic URLs) (`dfs-serp-1.json`, `dfs-serp-2.json`).
No women's-health term with a town has a number. This is a data limit, not proof of zero demand.

## 3. Gap keyword
**heilpraktikerin landshut: 320 searches per month (merged with "heilpraktiker landshut").**
- Town in keyword: Landshut. Scan centre = Landshut centre (48.5372, 12.1522).
- Her site is not in the organic top 20 for "heilpraktikerin landshut" (`dfs-serp-2.json`, 20 organic hits) and not for "heilpraktiker landshut" (`dfs-serp-1.json`).
- Caveat 1: this is the provider term, not her women's-health focus. No women's-health term with a town reaches 30 searches (see table).
- Caveat 2: Essenbach is about 12 km from the Landshut centre. A 7x7 grid with radius 5 km around Landshut will probably not cover her practice. Orchestrator and agent D must decide: radius, or a second scan.
- Other options: "kinderwunsch heilpraktiker" 480 (no town, no SERP checked). "heilpraktiker dingolfing" 70 (town, SERP not checked, no paid call made).

## 4. Competitor provider URLs (no directories), from `dfs-serp-1.json` and `dfs-serp-2.json`
- https://heilpraktikerin-silviahensel.de/ (Altdorf bei Landshut, TCM)
- https://www.praxis-funktionsmedizin.de/
- https://naturheilpraxis-eigl.de/therapien-fuer-kinder/
- https://www.heilpraxis-muehleninsel.de/leistungen/
- https://www.heilpraxis-muehleninsel.de/diagnostik/
- https://www.naturheilpraxis-andrea-stig.de/
- https://www.heilpraktiker-bieringer.de/ueber-mich/
- https://www.maluweber.de/
- https://eike-seibert.de/akupunktur-und-coaching-in-landshut/
- https://natuerlichgsund.de/therapie-angebot.html
- https://www.knau-coaching-therapie.de/

Excluded: jameda, doctolib, doctify, doctena, theralupa, aerzte.de, dastelefonbuch, pflegesuche, osteopathie.de, erleben.landshut.de, branchen-info.net, silvamed.de (clinic group).
Page-length check candidates for agent B: the first 6 URLs.

## 5. Name searches (Landshut coordinates, depth 10)
- "manuela stetter heilpraktikerin" (`dfs-serp-name.json`): her site is #1. Jameda is #2, Theralupa #3, GoLocal #4, werkenntdenbesten #5, ablefy #6, 11880 #7. SERP shows knowledge_graph, google_reviews and third_party_reviews.
- "naturheilpraxis stetter" (`dfs-serp-name2.json`): her blog `/blog/` is #2 (rank_absolute 3). First hit is an unrelated Osteopathie page. Facebook page is #7. SERP shows knowledge_graph and google_reviews.
- Finding: she is easy to find by name. She is not found by town and service.

## 6. Spam links (evidence: `dfs-backlinks-summary.json`, `dfs-refdomains-spam.json`)
- Summary: 67 backlinks, 39 referring domains (38 main domains), 13 nofollow domains, domain rank 127, profile spam score 41.
- **Spam: 20 of 39 linking domains have a backlink spam score of 60 or more.** Each has 1 or 2 links.


## site-findings.md (first 60 lines)

# Site findings: Manuela Stetter (agent B, 2026-10-14)

Site: https://heilpraktikerin-manuela-stetter.de/ (WordPress, Elementor, Yoast, Usercentrics). Evidence: `evidence/site.json`, `evidence/site-pages.json`, `evidence/comp-pages.json`. Read only, no browser, no paid call.

## 1. Technical checks (curl)
| Check | Result |
|---|---|
| http to https | OK: `http://heilpraktikerin-manuela-stetter.de/` returns 301 to https, final 200 |
| Server wait (3 runs) | 0.16 / 0.22 / 0.23 s |
| `tel:` link | OK: `tel:+4917652099985` on home (4x) and on every page checked: `/termine-buchen/`, `/leistungen/`, `/manuela/`, `/coaching/`, `/naturheilkunde/`, `/referenzen/` (4x each). No broken tel link. |
| Contact page | None. No page with "kontakt" in the URL or menu. Menu: Willkommen, Naturheilkunde, Coaching, Leistungen, Kurse, Referenzen, Manuela, Termine buchen. |
| Contact form | No own form. `/termine-buchen/` embeds a booking iframe `conversiontoolbox.net/book/iframe/1016893508682362` (online booking) and a Brevo newsletter iframe (`sibforms.com`). Text offers booking portal, e-mail, or WhatsApp. Home has only the Brevo newsletter iframe. |
| Booking | Yes: "Termine buchen" page with online booking widget. Free 15 minute Kennenlerngespräch is named on `/termine-buchen/` and `/coaching/`. |
| Duplicate pages | `/termine/` is not a duplicate. It returns 301 to `/termine-buchen/` (canonical is right). The home CTA buttons still link to `/termine/` (extra redirect hop). Real duplicates: 4 demo pages `/title-with-an-average-of-8-9-words/` (and `-2/`, `-3/`, `-4/`), same title "Title with an average of (8/9) words", all 242 words. |
| Sitemap | `/sitemap.xml`, 28 URLs, all measured. |
| Tracking | No GA4 and no GTM id in the home HTML. Usercentrics consent banner is present. |
| Schema | 1 JSON-LD block (Yoast graph: WebPage, WebSite, Organization, BreadcrumbList, ImageObject). No LocalBusiness, no Physician or MedicalBusiness type. |
| Headings | 6 pages with two H1, 10 pages with no H1 (sitemap pages). Home has 1 H1: "Naturheilpraxis für Frauenheilkunde (HPG), Live- und Online-Coachings in Landshut, Essenbach und Umgebung". |

## 2. Sitemap clutter (agency leftovers)
- 4 demo pages "Title with an average of (8/9) words" plus `/blog/` with the same H1, and 3 demo category archives `category-1/2/3` (131 to 177 words).
- 9 author archive pages that show agency e-mail names in the title: `drtolentino@spotzer.com`, `anoble@spotzer.com`, `tduong@spotzer.com`, `prodriguez@spotzer.com`, `kzmagay@spotzer.com`, plus users "migration", "siteowner", "partner", "copywriter", "wpthemedev", "design". They are in the sitemap (28 URLs: 14 real pages and 14 clutter pages).
- Her name search shows `/blog/` at rank 3 for "naturheilpraxis stetter" (demand.md). The page is demo text.

## 3. Titles and meta descriptions
- Each page has a title that names a different single keyword, not the page:
  - `/`: "Menstruationsbeschwerden | Essenbach | Naturheilpraxis Manuela Stetter"
  - `/leistungen/`: "Schmerztherapie | Essenbach | ..."
  - `/manuela/`: "Phytotherapie | Essenbach | ..."
  - `/naturheilkunde/`: "Ernahrungsberatung | Essenbach | ..." (typo, missing "ä")
  - `/referenzen/`: "Heilpraktik | Essenbach | ..."
  - `/coaching/`: "Lebensthemen | Essenbach | Manuela Stetter"
  - `/termine-buchen/`: "Online Beratung | Essenbach | ..."
- Home meta description: "Willkommen in der Naturheilpraxis Manueal Stetter in Essenbach. Ich helfe Ihnen Menstruationsbeschwerden und andere Beschwerden zu lindern." Problems: typo "Manueal", "Sie" form while the page uses "du", grammar ("helfe Ihnen ... zu lindern"), and "lindern" is a Werberecht word (see 5).
- Mixed address: the page mostly says "du" but `/termine-buchen/` and `/naturheilkunde/` switch to "Sie" and "Ihnen" in some sentences. Mixed "Dir/Du" capitalisation.
- Contact data: the footer shows `manuelastetter@manuela-stetter.de`. The mailto link on home and the Impressum use `kontakt@heilpraktikerin-manuela-stetter.de`. Two different addresses.

## 4. Prices (for the calculator)
| Service | Price | URL |
|---|---|---|
| Kennenlerngespräch, 15 min (video or phone) | 0 € (free) | `/termine-buchen/`, `/coaching/` |
| Naturheilpraxis, Stundensatz 60 min | 150 € ("Mein Stundensatz für 60 Minuten liegt bei € 150") | `/termine-buchen/` |
| Erster Termin (Anamnese), 90 to 120 min | 150 € per hour, so about 225 to 300 € (derived, the page says "pro Stunde € 150,00") | `/termine-buchen/` |
| Folgetermine, 60 to 80 min | 150 € per hour; "bei Erstellung eines Behandlungsplans kann sich dieser Betrag entsprechend erhöhen" | `/termine-buchen/` |
| Körperorientierte Traumabegleitung, 1 hour | 150 € incl. MwSt. | `/coaching/` |
| Personal Coaching, 1 hour | 150 € incl. MwSt. | `/coaching/` |
| Hormon-Selbsttest (Hormon-Quiz) | 0 € | `/leistungen/` |
| Hormonraum (monthly membership) | 24,99 € per month, monthly cancellable | `/leistungen/` |
| Kurse (Hormon-Check, Wechseljahre Wandelzeit, Energie & Balance, Lymphsystem) | No price on the site; sold on elopage.com and myablefy.com | `/`, `/leistungen/` |
| Hormonspeicheltest (lab) | No price on the site | `/naturheilkunde/` |

Calculator value: 150 € per session is the single price for all 1:1 services. Insurance note on the page: gesetzliche Kassen pay nothing in general, Selbstzahler can claim "außergewöhnliche Belastungen" for tax.

## 5. Werberecht (HWG) quotes (neutral, no claim of illegality)
Disease names and symptom lists (URL, quote):
- `/leistungen/` list: "Myome und Zysten", "Schilddrüsenerkrankungen", "Akute und chronische Blasenentzündung", "Endometriose", "PCO / Polyzystisches Ovarialsyndrom", "Kinderwunsch", "Schlafstörungen", "Post Pill Syndrom". Intro: "Hierzu zählen:".
- `/naturheilkunde/` list "Meine Fachbereiche": same list incl. "Endometriose", "Schilddrüsenerkrankungen", "Akute und chronische Blasenentzündung". Also "Herz- und Kreislaufprobleme", "Unruhe, Depressionen und Konzentrationsschwierigkeiten".
- `/` : "Ich konnte nicht mehr schlafen. Depressionen begleiteten meinen Zyklus." and "Hilfe bei Zyklus- und Menstruationsbeschwerden, Hormonschwankungen, Schmerzen im Bewegungsapparat, Schlafstörungen und mehr".
- `/leistungen/` (Lymph course): "Herpes simplex, verstopfte Nase oder dein Stoffwechsel ist langsam wie eine Schnecke?" and "Ohne eine gesunde Basis werden immer wieder dieselben Krankheitsthemen auftauchen."
- `/leistungen/`: "Magen-Darm/Leber Galle und was haben meine Gallensteine mit einer Östrogendominanz zu tun".


## homepage.md (first 60 lines)

# Homepage: Manuela Stetter (agent C, 14.10.2026)

## Score today

**12 / 44** (Prio A: 8 / 24). Details: `evidence/scorecard-today.md`.
Item 22 (HWG) = 0. The course block on the homepage says "Bye-bye Erschöpfung" and "Alles, was dir wirklich hilft!".

## 5-second test (today, `evidence/home-today-1440.jpg`)

- Was? Naturheilpraxis "für Frauenheilkunde (HPG)" and coaching. The H1 says it, in capitals on a flower photo.
- Wo? Landshut, Essenbach und Umgebung (H1). The address in Mirskofen is only in the footer.
- Warum du? Not visible. No Google stars (5,0 · 39), no "10 Jahre", no "über 600 Frauen" on the first screen.
- Wie zum Termin? Not clear. The visible button goes to the courses ("Zu den Kursen"). "Termine buchen" is only a menu item in the second menu row. The phone number is visible.
- Wer? Not on the first screen. Her face and name come in section 2 ("Hi, mein Name ist Manuela").

## Draft (`draft/index.html`, `evidence/home-draft-1440.jpg`)

- H1: "Deine Heilpraktikerin in Essenbach bei Landshut." Her H1 names Landshut.
- Subline: "Zyklus, Hormone, Wechseljahre? Ich schaue auf dich als ganze Frau, mit Naturheilkunde und Coaching, in meiner Praxis in Mirskofen oder online."
- Stars: 5,0 bei Google · 39 Bewertungen (`evidence/google-panel-2026-10-14.md`).
- Button: "Termin buchen" (header and hero, large). Note under it: "Zuerst sprechen wir 15 Minuten, kostenlos." (/termine-buchen/).
- Trust row, all from her site: Seit 10 Jahren eigene Praxis (/manuela/) · Über 600 Frauen (/manuela/) · Kennenlernen kostenlos, 15 Minuten (/termine-buchen/) · Vor Ort oder online, per Buchungsportal oder WhatsApp (/termine-buchen/).
- Images: logo = her emblem logo (`image0-removebg-preview.png`, margins cropped). Main photo = `Z82A0618.jpg` (she on a sofa). Portrait chip = face crop of `Z82A9892.jpg`.
- Colours: her Elementor kit, primary #2C7E94, beige #EDE3D9.
- Slop check (deslop_de.py with claims file): 5/5.
- Not used: "Frauenheilkunde" (sounds like a medical specialist title), disease names in the headline, any healing promise.

## Fixes to the draft_home.py output (run time 4.4 s in the script, 4 s wall)

1. `python3` (Homebrew 3.15) has no PIL. `/usr/local/bin/python3` (3.10) fails on a nested f-string in line 212. It ran with `/opt/homebrew/bin/python3.14`.
2. The script took the logo (`image0-removebg-preview.png`) as the portrait and said "logo: NONE". The portrait.jpg was the logo on a black background.
3. "praxis.jpg" was a stock photo (two daisies, `Stetter-Manuela-Naturheilpraxis_pod4.jpg`). Replaced with a real photo of her.
4. Colours came from the WordPress default palette (#ff6900 orange). Her site uses #2C7E94 (Elementor kit `post-1011.css`).
5. Headline had no Landshut. Subline was generic ("Du suchst eine Heilpraktikerin in Essenbach?").
6. No stars, although the Google panel file has 5,0 · 39.
7. Button "Ersttermin vereinbaren" changed to "Termin buchen" (her wording). The reassurance line was generic.
8. Trust row had the raw phone "+4917652099985" and a services box. Replaced with 4 facts from her site. Phone now as on her site: "0176 520 999 85".
9. Nav had "Willkommen". Now her menu items without it.

## Note

- No real practice room photo is on the site. All photos of her are from a studio shoot. The stock photos (daisies, yoga at the beach, bench, "HORMONES" blocks, calendula hero) were not used.
- Strip photos: `foto-1.webp` (Z82A0104), `foto-2.webp` (Y98A3858), `foto-3.webp` (Z82A9386). Only she is in them.


## Visible review-page text

Private Website- & Sichtbarkeits-Analyse | Naturheilpraxis Manuela Stetter, Essenbach | 741.Studio {{> header_de}} 🔒 PRIVATE WEBSITE- & SICHTBARKEITS-ANALYSE Manuela, so finden dich Frauen aus Landshut bei Google. Du hast mehr Bewertungen als jede Praxis vorn. Bei „heilpraktikerin landshut“ stehst du an 0 von 49 Messpunkten unter den ersten drei. Hier ist dein Plan. Du hast 5,0 Sterne bei 39 Bewertungen, die vier Praxen vorn in Landshut haben 11 bis 31. Doch in der Stadtmitte von Landshut zeigt Google dich nicht unter den ersten 20. ▶ Dein persönliches Video folgt in Kürze – die Analyse unten steht schon komplett. Zeig mir meinen Markt → 30 Minuten, kostenlos: Ich zeige dir live, wer in deinem Markt oben steht – und warum. Martin Ich habe mir heilpraktikerin-manuela-stetter.de und deinen Google-Eintrag genau angesehen. Hier zeige ich dir, was ich gefunden habe. Google-Karte · Sichtbarkeits-Check Unter den ersten drei an 0 von 49 Punkten. Sichtbar nur am Nordrand, in der Stadtmitte nicht unter den ersten 20. Wir haben gemessen, wo deine Praxis bei der Suche „heilpraktikerin landshut“ in der Google-Karte erscheint: an 49 Punkten im 5-km-Umkreis um die Stadtmitte von Landshut (Messung vom 14.10.2026). Deine Praxis liegt rund 8,3 km nordöstlich davon, außerhalb der Karte. Jede Zahl ist dein Platz an genau diesem Ort. ● Heute – echte Messung Unter den ersten drei an 0 von 49 Punkten. Zu sehen bist du nur am Nordrand der Karte: zweimal Platz 6 im Nordosten Richtung Essenbach, dazu 12, 15, 18 und zweimal 19. An 42 Punkten nicht unter den ersten 20, auch in der Stadtmitte. Naturheilpraxis Mühleninsel steht auf rund 100 % der Karte unter den ersten drei. ● Das Ziel – so kann es aussehen 4 3 3 3 3 3 4 3 2 2 2 2 2 3 3 2 1 1 1 2 3 3 2 1 1 1 2 3 3 2 1 1 1 2 3 3 2 2 2 2 2 3 4 3 3 3 3 3 4 Ziel-Szenario (Simulation) Ziel: unter den ersten drei auch in Landshut, wo Google 320 Suchen im Monat zählt. Die Praxen vorn haben 11 bis 31 Bewertungen, du hast schon 39. Martin Du hast 39 Bewertungen, mehr als jede der vier Praxen vorn. Trotzdem zeigt Google dich in Landshut an keinem der 49 Punkte unter den ersten drei. 📞 Anrufe direkt aus der Google-Karte 🧭 Frauen aus Landshut finden deine Praxis 🤝 Mehr Anfragen für ein Kennenlerngespräch Wer in der Google-Karte unter den ersten drei steht, bekommt den Großteil aller Klicks, Anrufe und Routen. Ist der Sprung realistisch? Andere Praxen hatten ähnliche Lücken im Google-Eintrag. So hat sich ihr Platz verändert. Ausgewählt nach deiner Lage: Heilpraktiker in Regensburg und Freiburg, eine Familienberatung bei Stuttgart und ein Betrieb aus Wien. Bei jedem fehlte etwas, das auch bei dir fehlt: die passende Einordnung bei Google oder Leistungen im Eintrag. Naturheilpraxis Veronika Schlirf Heilpraktikerin · Regensburg Platz 85 → 1 Nachher: echte Kartenmessung · Platz 85 → 1 Bernd Laserstein Heilpraktiker · Freiburg → Platz 1 Nachher: echte Kartenmessung · → Platz 1 Maria Abel Familienberatung · Raum Stuttgart 0 → 100 % Nachher: echte Kartenmessung · 0 → 100 % Astrid Lengauer Innenarchitektur · Wien Platz 18 → 1 Wer dahintersteht Martin Drendel Gründer und CEO von 741.Studio Ich leite 741.Studio, ein kleines Remote-Team aus Designern, Entwicklern, Media Buyern und Growth Marketern in Indonesien, Deutschland und Australien. Mein Grundsatz: Komplexität ist der Feind der Ausführung. Wir suchen die wenigen Schritte, die bei dir am meisten bewirken. 10+ Jahre Erfahrung mit lokaler Sichtbarkeit bei Google 250+ Unternehmen unterstützt Martin So sieht es aus, wenn es klappt: Veronika Schlirf, auch Heilpraktikerin, kam bei „Heilpraktikerin“ von Platz 85 auf Platz 1. So haben wir es gemacht – 4 Fälle ansehen Fälle schließen ▾ Naturheilpraxis Veronika Schlirf Heilpraktikerin · Regensburg Platz 85 → 1 „Heilpraktikerin“, 5.400 Suchen/Monat Auch Heilpraktikerin, vorher: Leistungen nicht im Google-Eintrag, keine Bewertungen, Website nicht fürs Handy gebaut. Name und Beschreibung im Google-Eintrag mit den echten Suchbegriffen Alle Leistungen eingetragen, je mit passender Seite Bewertungen von 0 auf 5,0 Sterne – mit Nachfass-Vorlage, jede beantwortet Website fürs Handy gebaut, neue Hauptüberschrift Gleiche Adresse in allen Branchenbüchern, Apple Karten und Bing Vorher Nachher Ganze Fallstudie → Bernd Laserstein Heilpraktiker · Freiburg → Platz 1 „Körperpsychotherapie“, vorher um Platz 6 Vorher: Ungenaue Einordnung bei Google, Leistungen nicht eingetragen, keine Bewertungen, keine Messung. Einordnung im Google-Eintrag präzisiert Leistungen eingetragen: Körperpsychotherapie, Biosynthese, Hakomi Bewertungs-Routine von null aufgebaut Leistungsseiten untereinander verlinkt Ergebnis: an 91 % der Karte sichtbar – bei 109 Mitbewerbern Vorher Nachher Ganze Fallstudie → Maria Abel Familienberatung · Raum Stuttgart 0 → 100 % der Karte unter den ersten 3, in 8 Wochen Vorher: In der Karte unsichtbar, Einordnung und Leistungen unvollständig, langsame Website, keine Einträge in Branchenbüchern. Richtige Einordnung: Erziehungs-, Psychologische und Beziehungsberaterin Website schneller gemacht, klare Überschriften mit Suchbegriffen Einträge in Branchenbüchern von null aufgebaut Bewertungs-Routine eingeführt Ergebnis: im Schnitt Platz 1,8 im ganzen Gebiet Nachher Ganze Fallstudie → Astrid Lengauer Innenarchitektur · Wien Platz 18 → 1 „Interior Design Wien“ Vorher: Google ordnete den Betrieb unvollständig ein, Leistungen fehlten, keine Seiten für die einzelnen Leistungen und Orte. Zusätzliche Einordnungen im Google-Eintrag ergänzt Sechs Leistungen eingetragen (Moodboard, Konzept, 3D-Darstellung …) Eigene Seiten je Leistung und je Einzugsgebiet Rund 100 Verweise von lokalen Seiten aus der Region Feste Routine für Bewertungen und Antworten Ganze Fallstudie → Weitere Ergebnisse Claudia Irmscher Heilpraktikerin Psychotherapie ▲ Platz 11 → 2 Karoline Hengst Homöopathie ▲ Platz 28 → 2 Nachher: echte Kartenmessung · ▲ Platz 28 → 2 Sven Böhme Heilpraktiker · Stuttgart ▲ Platz 17 → 4 Nachher: echte Kartenmessung · ▲ Platz 17 → 4 Torsten Menge Psychotherapie ▲ Platz 117 → 3 Nachher: echte Kartenmessung · ▲ Platz 117 → 3 Angelina Everitt Hypnosetherapie · Stuttgart ▲ Platz 21 → 3 Was nach der Karte kommt Drei Hebel für mehr Termine, und bei jedem fehlt heute ein Schritt Für deine Praxis haben wir drei Dinge geprüft: wonach Menschen bei Google suchen, warum andere Praxen in der Karte vor dir stehen und ob deine Startseite aus Besuchern Termine macht. Jede Zahl unten stammt aus echten Messungen. Im Rechner sind nur Budget, Anfrage- und Buchungsanteil Annahmen. Schritt 1 Wonach deine Patienten suchen Welche Leistungen sie bei Google eingeben und welche Fragen deine Seite noch nicht beantwortet. 320 Suchen/Monat: heilpraktikerin landshut Schritt 2 Damit das Telefon klingelt Warum andere Praxen in der Google-Karte vor dir stehen. unter den ersten 20 an 7 von 49 Punkten Schritt 3 Startseite, die Termine bringt Ob ein Besucher in 5 Sekunden versteht, was du anbietest und wie er einen Termin bekommt. heute 12 von 44 Punkten Schritt 1 · Wonach deine Patienten suchen Für „heilpraktikerin landshut“ zählt Google 320 Suchen im Monat. Deine Website steht dafür nicht unter den ersten 20 Treffern. Wir haben deine Website mit den Seiten verglichen, die bei „heilpraktikerin landshut“ oben stehen, und mit dem, was Menschen in Deutschland wirklich eingeben. Was Menschen bei Google eingeben Suchen pro Monat in ganz Deutschland (Mittel der letzten 12 Monate, Abruf 14.10.2026) heilpraktiker kosten 880 kinderwunsch heilpraktiker 480 heilpraktiker landshut 320 hormonspeicheltest 210 heilpraktiker dingolfing 70 hormonspeicheltest kosten 40 heilpraktiker essenbach 20 pms naturheilkunde 20 naturheilpraxis landshut 10 menstruationsbeschwerden naturheilkunde 10 Gelb = Fragen und Themen, grün = Suche nach einer Praxis. „heilpraktiker kosten“ und „kinderwunsch heilpraktiker“ sind Suchen ohne Ort, gezählt in ganz Deutschland. Mit Ort zeigt Google „heilpraktiker landshut“ mit 320 Suchen im Monat. Google zählt „heilpraktikerin landshut“ bei „heilpraktiker landshut“ mit, darum steht die Zahl nur einmal da. Für Wechseljahre oder Hormone mit Landshut gibt Google keine Zahl heraus. Ohne Zahl bei Google: „frauenheilkunde naturheilkunde“, „wechseljahre heilpraktiker landshut“, „hormone heilpraktiker landshut“. Google gibt für viele Begriffe keine Suchzahlen heraus – das heißt nicht, dass niemand sucht. Die Länge passt. Es fehlt Landshut in deinen Seitentiteln. Deine Startseite ist fast so lang wie die Seiten vorn. Keiner deiner Seitentitel nennt Landshut, 7 nennen Essenbach. 477 Wörter auf deiner Startseite 0 von 7 Seitentiteln deiner Praxis nennen „Landshut“ Deine Startseite 477 Seiten vor dir (Mittel aus 5) 516 Eine der fünf gemessenen Seiten vor dir nennt Beruf und Ort in der Hauptüberschrift. Deine Hauptüberschrift nennt Landshut und Essenbach, aber nicht das Wort „Heilpraktikerin“. Dein Seitentitel bei Google lautet „Menstruationsbeschwerden | Essenbach“. Martin Für Wechseljahre oder Hormone mit Landshut gibt Google keine Suchzahl heraus. Im Gespräch schauen wir, mit welchen Anliegen Frauen am häufigsten zu dir kommen. Die 6 wichtigsten neuen Inhalte für deine Website 1 Seitentitel „Heilpraktikerin in Essenbach bei Landshut“ Ort Heute heißt deine Startseite bei Google „Menstruationsbeschwerden | Essenbach“. Landshut steht in keinem deiner 7 Seitentitel. 2 Seite „Deine Heilpraktikerin für Landshut“ Ort „heilpraktiker landshut“: 320 Suchen pro Monat. Eine eigene Seite für Frauen aus Landshut gibt es nicht, deine Website steht dafür nicht unter den ersten 20 Treffern. 3 Seite „Was kostet ein Termin bei der Heilpraktikerin?“ Leistung „heilpraktiker kosten“: 880 Suchen pro Monat in Deutschland. Deine Preise stehen schon auf „Termine buchen“ (150 € für 60 Minuten), aber keine Seite beantwortet genau diese Frage. 4 Seite „Hormonspeicheltest: Ablauf und Kosten“ Leistung „hormonspeicheltest“: 210 Suchen pro Monat, „hormonspeicheltest kosten“: 40. Der Test steht auf deiner Seite „Naturheilkunde“, ohne Preis. 5 Seite „Kinderwunsch: wie ich dich begleite“ Leistung „kinderwunsch heilpraktiker“: 480 Suchen pro Monat in Deutschland. Bei dir ist Kinderwunsch ein Punkt in einer Liste, ohne eigene Seite. 6 Kontakt-Seite mit Anfahrt Profil Im Menü gibt es keine Kontakt-Seite. Deine Adresse in Mirskofen steht nur ganz unten auf der Seite, ohne Karte und ohne Zeiten. Schritt 2 · Damit das Telefon klingelt Du hast 39 Bewertungen, mehr als jede Praxis vorn. In Landshut zeigt Google dich an keinem Punkt unter den ersten drei. Wir haben die Google-Einträge der Praxen verglichen, die bei „heilpraktikerin landshut“ oben stehen. Zwei der vier ersten sind an allen 49 Messpunkten unter den ersten 20 zu sehen. Deine Praxis an 7. Praxis So ordnet Google sie ein Google-Bewertungen Oben in der Karte bei „heilpraktikerin landshut“ Naturheilpraxis Manuela Stetter Naturheilpraktiker 39 0 % Naturheilpraxis Mühleninsel - Heilpraktikerin Birgit Busch Alternativmediziner 31 100 % Heilpraktikerin Landshut - Agata Block - Praxis für Microkinesitherapie und Naturheilkunde Heilpraktiker 20 93,9 % Heilpraxis Diana Neumaier Alternativmediziner 11 36,7 % Naturheilpraxis für Traditionelle Chinesische Medizin - Ströhm Alternativmediziner 11 16,3 % ← Tabelle seitwärts wischen → Prozent = an wie vielen von 49 Messpunkten im 5-km-Umkreis um die Stadtmitte die Praxis unter den ersten drei der Google-Karte steht. Gemessen am 14.10.2026. Was das heißt: Bewertungen sind nicht deine Lücke: Die vier Praxen vorn haben 11 bis 31, du hast 39. Diese Praxen liegen rund 0,2 bis 2,2 km von der Stadtmitte, deine Praxis rund 8,3 km. Naturheilpraxis Kornelia Zettl in der Altstadt hat dieselbe Einordnung wie du und 3 Bewertungen, sie ist an 44 Messpunkten unter den ersten 20. Die Nähe zur Stadt kannst du nicht ändern, aber du kannst Google klar sagen, dass deine Praxis für Landshut da ist. Martin Der größte Hebel ist, Google klar zu sagen, dass deine Praxis auch für Landshut da ist. Das geht über Seitentitel, eine eigene Seite für Landshut und deinen Google-Eintrag. Was wir an deinem Google-Eintrag konkret ändern Einordnung prüfen (Google heute: Naturheilpraktiker) Agata Block steht als „Heilpraktiker“ eingeordnet und ist an allen 49 Punkten unter den ersten 20. Bei dir steht nur „Naturheilpraktiker“, als einzige Einordnung. Alle Leistungen eintragen Zyklus und Hormone, Wechseljahre, Kinderwunsch, Hormonspeicheltest, Ernährungsberatung, Coaching und Kurse, je mit kurzer Beschreibung und Link zur passenden Seite. Neue Bewertungen Deine neueste Bewertung ist rund einen Monat alt, 7 Bewertungen sind jünger als ein Jahr. Eine kurze Bitte nach dem Termin, mit direktem Link zum Eintrag, bringt laufend neue. Auf jede Bewertung antworten Das machst du schon: 29 von 39 Bewertungen haben eine Antwort von dir. Ohne Antwort sind nur ältere, 6 bis 9 Jahre alt. Fotos von dir und deiner Praxis Bilder von dir, vom Praxisraum und vom Eingang zeigen neuen Patientinnen, wohin sie kommen. Kurze Beiträge im Eintrag Ein Beitrag zu einem Kurs oder zum kostenlosen Kennenlerngespräch zeigt Besuchern im Eintrag, was bei dir gerade los ist. Vorher aufräumen: was dich heute Anrufe kostet 20 / 39 Websites, die auf deine Seite verlinken, haben einen hohen Spam-Wert, darunter Casino- und Wettseiten. Wir melden sie Google als „nicht von uns“. 9 echte Seiten Google bekommt von deiner Seite 28 Adressen, nur 9 davon sind Praxis-Seiten. Der Rest sind Demo-Seiten wie „Title with an average of (8/9) words“ und 11 Autoren-Seiten, 5 davon mit fremden E-Mail-Namen. 4 doppelt Vier Demo-Seiten zeigen denselben Titel und gleich viele Wörter (242). Wir nehmen sie aus dem Netz. 2 E-Mail-Adressen Unten auf der Seite steht manuelastetter@manuela-stetter.de, im Impressum kontakt@heilpraktikerin-manuela-stetter.de. Eine Adresse überall ist klarer. ✓ Die gute Nachricht: Wer „manuela stetter heilpraktikerin“ sucht, findet deine Website auf Platz 1. Dazu hast du 5,0 Sterne bei 39 Bewertungen, mehr als jede der vier Praxen vorn in Landshut. Darauf baust du auf. Schritt 3 · Startseite, die Termine bringt Besucher entscheiden in 5 Sekunden. Deine Startseite zeigt ihnen heute ein Blumenbild und den Button „Zu den Kursen“. Wir prüfen jede Startseite an 22 Punkten, die darüber entscheiden, ob jemand einen Termin anfragt, bei Gesundheitsberufen inklusive Werberecht. Im zweiten Bild siehst du einen Entwurf des ersten Bildschirms mit deinem Logo und deinen Fotos. ● Heute 🔍 Zum Vergrößern antippen 12 / 44 Deine Nummer oben rechts und Landshut und Essenbach in der Überschrift sind gut. Im ersten Bildschirm fehlen deine 5 Sterne, ein Button für den Termin und dein Foto. ● So sollte es aussehen 🔍 Zum Vergrößern antippen Ziel: 36+ / 44 Dein Foto und dein Name, dazu in 5 Sekunden klar: Heilpraktikerin in Essenbach bei Landshut, 5,0 bei 39 Bewertungen und ein Button „Termin buchen“, zuerst 15 Minuten kostenlos. Der 5-Sekunden-Test: was dein erster Bildschirm heute nicht beantwortet Was? „Naturheilpraxis für Frauenheilkunde (HPG), Live- und Online-Coachings“ in großen Buchstaben auf einem Blumenbild. Wo? Landshut, Essenbach und Umgebung stehen in der Überschrift. Das passt. Die Adresse in Mirskofen steht erst ganz unten. Warum du? Deine 5,0 Sterne bei 39 Bewertungen stehen nicht im ersten Bildschirm, auch keine Zahl und kein Zitat. Wie zum Termin? Der sichtbare Button heißt „Zu den Kursen“. „Termine buchen“ ist nur ein Punkt in der zweiten Menüzeile. Deine Nummer ist zu sehen. Wer? Dein Foto und „Hi, mein Name ist Manuela“ kommen erst unter dem Blumenbild. × Wachstums-Rechner · Sichtbarkeit in Zahlen Was eine neue Patientin aus Google für deine Praxis wert ist Sichtbarkeit bei Google hat zwei Quellen: bezahlte Google-Anzeigen ganz oben und unbezahlte Plätze in der Karte und in der Suche. Der Rechner zeigt beide getrennt. Zieh an den Reglern – die Startwerte sind vorsichtige Annahmen, im Gespräch setzen wir deine echten Zahlen ein. Echte Google-Suchen pro Monat (ganz Deutschland, Mittel der letzten 12 Monate): heilpraktikerin landshut 320 · hormonspeicheltest 210. Ein Anzeigen-Klick auf „heilpraktikerin landshut“ kostet bei Google rund 1,00 US-Dollar (Google-Angabe in Dollar; der Regler startet ohne Umrechnung bei 1,00 €) (Abruf 14.10.2026). Startwert Umsatz: zwei Termine zu je 150 € für 60 Minuten laut deiner Seite „Termine buchen“. Budget, Anfrage- und Buchungsanteil sind Annahmen. Gefunden in Karte und Suche (unbezahlt) Google-Anzeigen (bezahlt) Aus Besuchern werden Patientinnen – Besucher / Monat – Anfragen / Monat – neue Patientinnen / Monat – Mehrumsatz / Jahr Woher die Anfragen kommen ● Karte + Suche ● Google-Anzeigen Werbebudget je neuer Patientin: – ⚡ Google-Anzeigen: ab dem ersten Tag Anzeigen stehen über der Karte und den Suchergebnissen. Sie bringen Anfragen sofort – solange das Budget läuft. Du zahlst pro Klick. 📍 Karte und Suche: baut sich auf Plätze in der Google-Karte und in der Suche kosten pro Klick nichts. Sie brauchen ein paar Monate – und wirken dann dauerhaft. 🧲 Die Website entscheidet Beides bringt Besucher. Ob daraus eine Anfrage wird, entscheidet deine Startseite – siehe Schritt 3 weiter oben. Alle Werte sind Annahmen zum Selber-Einstellen. Das Werbebudget zahlst du direkt an Google. Der Website-Check Was deine Website heute richtig macht und wo sie Anfragen verliert 4 Bereiche, jeder Punkt an deiner echten Seite geprüft. Fahr über einen Bereich oder tipp ihn an, um ihn zu öffnen. + (01) Deine Website 1 ausbaufähig · 4 passt Passt Telefonnummer antippbar Auf jeder gemessenen Seite ist deine Nummer ein Link. Ein Tipp am Handy, und es klingelt. Passt Immer verschlüsselt Deine Seite öffnet sich immer mit dem Schloss-Symbol im Browser, auch die Adresse ohne „https“ leitet richtig weiter. Passt Ladezeit gut Deine Seite beginnt nach rund 0,2 Sekunden zu laden. Passt Termin online buchen Auf „Termine buchen“ gibt es ein Buchungsportal, dazu das kostenlose Kennenlerngespräch von 15 Minuten. Ausbaufähig Keine Kontakt-Seite Es gibt keine Kontakt-Seite und kein eigenes Formular. Anfragen laufen über das Buchungsportal, E-Mail oder WhatsApp. + (02) Was Google liest 1 dringend · 3 ausbaufähig · 1 passt Dringend Seitentitel Deine Startseite heißt bei Google „Menstruationsbeschwerden | Essenbach“, deine Leistungsseite „Schmerztherapie | Essenbach“. Jeder Titel nennt ein einzelnes Wort statt der Seite, keiner nennt Landshut. Ausbaufähig Hauptüberschrift Heute: „Naturheilpraxis für Frauenheilkunde (HPG), Live- und Online-Coachings in Landshut, Essenbach und Umgebung“. Landshut und Essenbach sind drin, das Wort „Heilpraktikerin“ fehlt. Ausbaufähig Demo-Seiten Google bekommt von deiner Seite 28 Adressen, nur 9 davon sind Praxis-Seiten. Vier Demo-Seiten zeigen denselben Titel und gleich viele Wörter (242), 10 Autoren-Seiten haben keine Hauptüberschrift. Ausbaufähig Beschreibung bei Google Heute: „Willkommen in der Naturheilpraxis Manueal Stetter in Essenbach …“. Dein Name hat einen Tippfehler, und der Text siezt, während deine Seite duzt. Passt Ausführliche Texte Deine Startseite hat 477 Wörter, die gemessenen Seiten vor dir im Mittel 516, deine Leistungsseite 1.346. Die Länge ist also nicht deine Lücke. + (03) Was du messen kannst 1 dringend · 1 ausbaufähig Dringend Keine Besucher-Statistik Auf der Website ist keine Besuchermessung zu finden. Mit einer Messung siehst du, wie viele Besucher von Google kommen. Ausbaufähig Daten für Google Deine Seite beschreibt sich für Google als Website, nicht als Praxis mit Adresse, Zeiten und Leistungen. + (04) Dein Ruf im Netz 1 dringend · 1 ausbaufähig · 3 passt Passt 5 Sterne 5,0 Sterne bei 39 Bewertungen. Passt Mehr Bewertungen als die Praxen vorn 39 Bewertungen, die neueste vor rund einem Monat. Die vier Praxen vorn in Landshut haben 31, 20, 11 und 11. Passt Antworten auf Bewertungen 29 von 39 Bewertungen haben eine Antwort von dir. Dringend Links mit hohem Spam-Wert 20 von 39 Websites, die auf dich verlinken, haben einen hohen Spam-Wert, etwa bestnz-poker-casinoslot.com und betwinnermirror.com. Ausbaufähig Werberecht Einige Sätze nennen Krankheitsnamen oder klingen nach einem Erfolgsversprechen, etwa im Kurs-Block der Startseite „Bye-bye Erschöpfung“. Für Gesundheitsberufe gelten dafür enge Werberegeln, die Stellen gehen wir gemeinsam durch. 4 Bereiche · 17 Punkte Sofort-Maßnahmen Sechs Schritte, die du schon nächste Woche umsetzen kannst, ohne neue Website 6 Schritte, die sofort wirken – ohne neue Website. ✓ Landshut in den Seitentitel „Heilpraktikerin in Essenbach bei Landshut“ statt „Menstruationsbeschwerden | Essenbach“ als Titel deiner Startseite. ✓ Button „Termin buchen“ nach oben Im ersten Bildschirm steht heute „Zu den Kursen“. Ein Button „Termin buchen“ mit dem Satz „Zuerst 15 Minuten kostenlos“ führt direkt zu deinem Buchungsportal. ✓ Deine 5 Sterne zeigen 5,0 bei 39 Bewertungen gehört in den ersten Bildschirm, dazu einige Zitate weiter unten. ✓ Demo-Seiten löschen Die vier Seiten „Title with an average of (8/9) words“, die Demo-Kategorien und die 11 Autoren-Seiten, 5 davon mit fremden E-Mail-Namen, aus dem Netz nehmen. ✓ Beschreibung bei Google neu Tippfehler „Manueal“ korrigieren und den Text in deinem „du“ schreiben, mit Essenbach und Landshut. ✓ Einordnung und Leistungen im Google-Eintrag „Heilpraktiker“ als Einordnung prüfen und deine Leistungen eintragen, je mit Link zur passenden Seite. Priorisierter Plan Dein Plan für die nächsten 8 Wochen, Schritt für Schritt Schritt für Schritt zu echter Sichtbarkeit für deine Praxis. Maßnahme Priorität Aufwand Warum Woche 1–2 · Aufräumen Demo- und Autoren-Seiten löschen, Seitentitel und Beschreibung bei Google neu, eine E-Mail-Adresse überall, unseriöse Links melden Hoch Gering Erst aufräumen, dann ausbauen Woche 1–3 · Telefon klingeln Google-Eintrag: Einordnung prüfen, Leistungen eintragen, Fotos, kurze Beiträge, neue Bewertungen Hoch Gering Du hast mehr Bewertungen als jede Praxis vorn, Google zeigt dich in Landshut aber an keinem Punkt unter den ersten drei Woche 2–4 · Startseite Erster Bildschirm mit „Heilpraktikerin in Essenbach bei Landshut“, 5 Sternen, Telefon und Button „Termin buchen“ Hoch Mittel Aus Besuchern werden Termine Woche 3–8 · Neue Inhalte Seiten für Landshut, „Was kostet ein Termin bei der Heilpraktikerin?“, Hormonspeicheltest und Kinderwunsch, dazu eine Kontakt-Seite mit Anfahrt Hoch Mittel Seiten für die Fragen, die Menschen wirklich googeln Laufend · Messen Besucher, Anrufe und Anfragen plus monatliche Kartenmessung Mittel Gering Jede Maßnahme muss sich in Zahlen zeigen Deine Ausgangslage auf einen Blick 🌿 Naturheilpraxis Manuela Stetter Heilpraktikerin · Naturheilkunde für Frauen · Coaching · Kurse · Essenbach bei Landshut 5 ★ bei 39 Bewertungen 📍 Dein Google-Eintrag „heilpraktikerin landshut“: unter den ersten drei an 0 von 49 Punkten In der Stadtmitte von Landshut nicht unter den ersten 20 ⭐ Google-Bewertungen Du: 39, die neueste vor rund einem Monat · Naturheilpraxis Mühleninsel: 31 29 von 39 beantwortet 🔍 heilpraktikerin-manuela-stetter.de Erster Bildschirm: Blumenbild, Überschrift mit Landshut und Essenbach, Button „Zu den Kursen“, keine Sterne Startseite heute: 12 von 44 Punkten Unser ganzer Ablauf Was Agenturen verstecken: von Anfang bis Ende, nichts versteckt In diesem Video zeige ich dir jeden Schritt, den wir für einen Betrieb wie deinen gehen. So weißt du vor dem Gespräch genau, was passiert. Lass uns in 30 Minuten anschauen, wer in Landshut oben steht und wie deine Praxis dorthin kommt. 30 Minuten, kostenlos: Ich zeige dir live, wer in deinem Markt oben steht, und wie aus diesen Punkten mehr Anfragen werden. Unverbindlich. Zeig mir meinen Markt → ✉️ E-Mail schreiben {{> footer_de}} {{> consent}}
