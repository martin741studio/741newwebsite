# Site findings: Claudia Breuer (agent B, 2026-10-31)

Site: https://www.breuer-psychotherapie.de/ (Wix, 13 URLs in the sitemap). Branch: health (HWG).
Method: `collect_site.py` output from 30.10. (reused, not rerun: `site-pages.json` has 13 valid pages) plus curl checks of 2026-10-31.
Evidence folder: `evidence/`. Raw curl copies and text extracts: `evidence/raw/*.html` and `evidence/raw/*.txt` (the file names with `C3A4` and `C3BC` are the URLs `/ängste`, `/über-mich`, `/über-meine-arbeit`).
Word counts are the `collect_site.py` counts (main content, no menu or footer). Every finding names its evidence file.

## 1. Technical checks

| # | Finding | Evidence |
|---|---|---|
| 1 | No `href="tel:` link on any page. Checked on home, `/kontakt`, `/ängste`, `/stress`, `/honorar-ablauf`, `/über-mich`, `/über-meine-arbeit`, `/lebenskrisen`, `/behandlungsfelder`, `/erschöpfung`. The phone number `+49 152 25699074` is plain text in the footer, on `/kontakt` ("Tel.: +49(0)152 25699074") and in the Impressum. Only a `mailto:info@breuer-psychotherapie.de` link exists on every page. No WhatsApp link. | `evidence/raw/home.html`, `evidence/raw/kontakt.html`, `evidence/site.json` (`tel_links_home: []`, `tel_links_contact: []`, `pages_with_broken_tel: []`), `evidence/site-pages.json` (`tel_link: false` on 13 of 13) |
| 2 | http to https works. `http://www.` answers 301 to `https://www.breuer-psychotherapie.de/`. `https://breuer-psychotherapie.de/` (no www) answers 301 to the www version. `http://breuer-psychotherapie.de/` answers 301 to `https://breuer-psychotherapie.de/` and then to www (two steps, no error). | curl on 2026-10-31, `evidence/site.json` (`http_redirects_to_https: true`) |
| 3 | The contact form is on `/kontakt`, not on the home page. Fields: Vorname, Nachname, E-Mail, Telefon, Adresse, "Termin (Tag/Uhrzeit)" (date picker). Button text "Einreichen". The home page has no form (`has_form: false`). The `/kontakt` page says "Termine nach telefonischer Vereinbarung". | `evidence/raw/kontakt.html` (`<form id="comp-kw3op70x">`), `evidence/site.json` (`form_on_home: false`, `form_on_contact: true`) |
| 4 | No duplicate pages. No two pages share title and word count. `duplicate_pages: []`. | `evidence/site.json`, `evidence/site-pages.json` |
| 5 | `site.json` lists 4 "dead links" from home (`/über-meine-arbeit`, `/über-mich`, `/erschöpfung`, `/ängste`, status `null`). This is a false alarm: the script did not percent-encode the umlauts. With and without encoding, all four answer HTTP 200. No real dead link found. Do not use this on the page. | curl on 2026-10-31, `evidence/site.json` (`dead_links_from_home`) |
| 6 | GTM container `GTM-PRR7RB69` is on the site (script and noscript). No direct GA4 tag in the HTML (`ga4: []`). What the container fires is not visible from outside. The site has no JSON-LD on any page (`jsonld_blocks: 0`, `jsonld_types: []` on 13 of 13). No FAQ markup. | `evidence/site.json`, `evidence/site-pages.json`, `evidence/raw/home.html` |
| 7 | H1 problems. 5 pages have no H1: `/ängste`, `/stress`, `/erschöpfung`, `/lebenskrisen`, `/honorar-ablauf`. These are the main service pages. `/über-meine-arbeit` has 5 H1 (one per section). `/impressum` has 2 H1, `/datenschutz` has 16. The home H1 is "Sorgen Sie für Ihre seelische Gesundheit" (no service, no city). | `evidence/site-pages.json` (`h1`), `evidence/site.json` (`pages_no_h1: 5`, `pages_two_h1: 3`) |
| 8 | Title tags. Home: "breuer-psychotherapie - Lebensberatung - Bonn" (45 characters, brand string first, the word "Psychotherapie" only inside the domain name). `/agb`, `/impressum` and `/datenschutz` have the Wix default title "… \| My Site 4". Meta descriptions are 356 to 490 characters (Google shows about 155). The `/kontakt` meta shows the e-mail as `info@breuer-psychotherapie` (without `.de`). | `evidence/site-pages.json` (`title`, `meta_description`) |
| 9 | Old content. Footer "© 2021 Claudia Breuer". The home page and `/honorar-ablauf` have a Corona paragraph ("Damit Sie sich auch Zeiten von Corona sicher fühlen können, garantiere ich Ihnen die Einhaltung höchster Hygienestandards …"). The Impressum cites "§ 5 TMG". The Impressum names "Gesundheitsamt Bonn" as authority. `/über-mich` says the permit came from "Gesundheitsamt Köln". | `evidence/raw/home.txt`, `evidence/raw/honorar-ablauf.txt`, `evidence/raw/C3BCber-mich.txt`, Impressum text (curl) |
| 10 | Images. Home: 10 img tags, 2 without alt text. Alt texts are file names ("STRESS.jpg", "Claudia-1225_quadrat.jpg", "Diary and 2021 Calendar desk for Planner"). The person photo is a professional shoot (credit in the Impressum: PPC Photography Cologne). Stock photos (shutterstock, Unsplash) on the topic pages. | `evidence/site.json` (`images_home`), `evidence/raw/home.html` |
| 11 | Trust items on the site: member of "Verband freier Psychotherapeuten, Heilpraktiker für Psychotherapie und psychologischer Berater" (footer, with logo `vfp_logo2.gif`). Qualification list on `/über-mich` (Paracelsus schools). No review or rating widget, no Google reviews on the site. A cooperation link to Charlotte Zaum (`praxis-charis.de`). | `evidence/raw/C3BCber-mich.txt`, `evidence/raw/home.txt` |

## 2. Prices and services (input for the calculator)

Two pages show different prices. Both are live today.

| Service | Home (`/`) | `/honorar-ablauf` |
|---|---|---|
| Erstgespräch | kostenlos, 30 Minuten | Kostenlos (no length given) |
| Einzelgespräch | **100 €**, 60 Minuten | **80 €** (no length given) |
| Paargespräch | not listed | 120 € (no length given) |

- Evidence: `evidence/raw/home.txt` lines 78 to 81, `evidence/raw/honorar-ablauf.txt` (price block "Erstgespräch Kostenlos / Einzelgespräch 80 € / Paargespräch 120 €").
- Agent A wrote 80 EUR / 120 EUR in `demand.md` (source: `/honorar-ablauf`). The home page shows 100 EUR for 60 minutes. I cannot tell from the site which page is newer. The home text reads like the more recent copy. The two pages also give different minimum times: home says "Zwei bis drei Stunden sollten Sie jedoch mindestens für eine Beratung oder ein Coaching einplanen"; the price page says "Eine Stunde sollten Sie jedoch mindestens einplanen".
- Open point for the orchestrator: the calculator `val` depends on which price is current (80 or 100 EUR). Agent E must not pick one silently. Check with the Google profile or ask Claudia.
- Payment: Selbstzahler only. "Mein Honorar wird in der Regel nicht durch die gesetzlichen Krankenkassen übernommen." Cash at the end of the session against an invoice or receipt. The invoice is tax deductible as "außerordentliche Belastung" (her wording).
- Offer in her words: "Beratung | Coaching | Therapie". Four topic pages: Stress, Erschöpfung, Ängste, Lebenskrisen. No package price, no session pack.
- Contact path: "Termine nach telefonischer Vereinbarung" (`/kontakt`), "Sie erhalten kurzfristig Termine - auch in den Abendstunden" (home). Address: Wurzerstr. 100, 53175 Bonn.

## 3. Word counts (`collect_site.py`)

| Page | Words | H1 | Evidence |
|---|---|---|---|
| Home `/` | 745 | 1 | `evidence/site.json` (`home_words`) |
| `/über-meine-arbeit` (Beratung, Coaching, Therapie) | 1198 | 5 | `evidence/site-pages.json` |
| `/ängste` | 705 | 0 | same |
| `/lebenskrisen` | 455 | 0 | same |
| `/honorar-ablauf` | 433 | 0 | same |
| `/erschöpfung` | 388 | 0 | same |
| `/stress` | 339 | 0 | same |
| `/über-mich` | 361 | 1 | same |
| `/behandlungsfelder` | 130 | 1 | same |
| `/kontakt` | 70 | 1 | same |

Mean of the 4 topic pages (Stress, Erschöpfung, Ängste, Lebenskrisen): (339 + 388 + 705 + 455) / 4 = 472 words. The topic pages have no heading structure (`h1: []`, `h2: []`, `h3: []`). There is no page for a service plus the city (no "Psychotherapie Bonn" page) and no page for Paarberatung, although she lists a Paargespräch. There is no page for Burnout or Panikattacken, although both words appear in the text.

## 4. HWG pass: sentences for the neutral "Werberecht" row

The site is the site of a Heilpraktikerin für Psychotherapie. She holds the permit ("Erlaubnis zur Ausübung der Heilkunde auf dem Gebiet der Psychotherapie", `/über-mich`). The title "Heilpraktikerin für Psychotherapie" is correct for her. No protected title found: the words "Psychotherapeutin", "Psychologin", "Psychologe" and "Dipl." do not appear on the site (grep over all 10 text extracts). The site says "Psychologische Beraterin" and "Psychologische Beratung" (not a protected title).

Use these quotes for one neutral row "Werberecht". Do not state that any sentence is illegal.

Healing or success wording (quote, page):
1. "Lebenskrisen unterschiedlichen Ausmaßes können sehr gut mit systemisch-lösungsorientierten und verhaltenstherapeutischen Methoden behandelt werden." (`/lebenskrisen`)
2. "Je früher die Behandlung beginnt, desto besser stehen die Chancen für eine deutliche und nachhaltige Besserung." (`/ängste`; same sentence with "eine Behandlung" on `/lebenskrisen`)
3. "Die Dauer einer Stressbewältigungstherapie ist recht unterschiedlich und kann bereits nach wenigen Therapieeinheiten Erfolge zeigen." (`/stress`)
4. "Das Verbessern Ihrer kommunikativen Fähigkeiten, unterschiedliche Entspannungstechniken sowie Sport oder Bewegung wirken zusätzlich heilsam …" (`/ängste`)
5. "… ist die am besten wissenschaftlich überprüfte psychotherapeutische Methode mit sehr guten therapeutischen Effekten und einer sehr hohen Wirksamkeit." (`/über-meine-arbeit`, Verhaltenstherapie list)
6. "… führt durch gezielte praktische Übungen bereits frühzeitig zu ersten Erfolgen." (`/über-meine-arbeit`)
7. "Das macht es Ihnen möglich, sich selbst aus einer schwierigen Situation zu „befreien“, sich zu verwirklichen und in Ihrer Persönlichkeit zu wachsen." (`/über-mich`)
8. "… um schnellstmöglich eine Entlastung zu erreichen." (`/über-meine-arbeit`, Psychologische Beratung)
9. "Dies verbessert nicht nur die jeweilige persönliche oder berufliche Situation, sondern führt auch zu mehr Zufriedenheit und Wohlbefinden." (`/über-meine-arbeit`, Coaching)

Sentences that name serious diseases or a diagnosis (quote, page):
10. "Menschen, die unter Burnout, Panikattacken oder einer Angststörung leiden, finden in der Psychotherapie einen geschützten Raum, um ihre Probleme zu bearbeiten und neue Bewältigungsstrategien zu entwickeln." (`/über-meine-arbeit`)
11. "Dabei reicht mein Behandlungsspektrum von der psychologischen Beratung bei leichten Formen der Angst bis hin zur Therapie von Angsterkrankungen und Panikstörungen." (`/ängste`)
12. "Wenn Symptome einer psychischen Störung die Lebensqualität verschlechtern und für Leid sorgen." (`/über-meine-arbeit`, Therapie)
13. "Auch wenn Burnout kein eigenes medizinisches Krankheitsbild darstellt, so handelt es sich doch um einen ernstzunehmenden Risikozustand, der die Entwicklung von erheblichen Stress-Folgeerkrankungen, wie Depressionen, wahrscheinlicher macht. Daher ist es von Vorteil, wenn eine Diagnose möglichst früh gestellt wird …" (`/erschöpfung`)
14. "Erschöpfung, Panikattacken oder Angststörungen können die Folge sein. Kurz gesagt: Der Stress wird gefährlich für unsere Gesundheit." (`/stress`)
15. "Gelingt es nicht, sich an ein belastendes Lebensereignis anzupassen, kann eine psychische Störung entstehen." (`/lebenskrisen`)
16. "Während der ersten Sitzungen steht neben der Diagnostik der Aufbau einer produktiven und persönlichen Arbeitsatmosphäre … im Vordergrund." (home, `/honorar-ablauf`)

Other claims to check with her before our page repeats them (not HWG):
17. "Verhaltenstherapie … wird als eine der drei staatlich anerkannten Therapieverfahren von den Krankenkassen finanziert." (`/über-meine-arbeit`) next to "Mein Honorar wird in der Regel nicht durch die gesetzlichen Krankenkassen übernommen." (`/honorar-ablauf`). A reader can mix the two up.
18. "Der Zusammenhang zwischen Stress, Belastung im Arbeitskontext und Burnout ist wissenschaftlich belegt." (`/erschöpfung`). No source given.
19. "garantiere ich Ihnen die Einhaltung höchster Hygienestandards" (home, `/honorar-ablauf`). The word "garantiere" refers to hygiene, not to a result.

Evidence for 1 to 19: `evidence/raw/*.txt` (text of each page, curl 2026-10-31).

## 5. Second pass: competitor page lengths (done 2026-10-31)

Input: the 12 competitor provider URLs in section 4 of `demand.md` (6 from "psychotherapie bonn", 6 from "heilpraktiker psychotherapie bonn"; no directories, no schools). Command: `page_metrics.py --lang de`. Result: 12 of 12 readable. Evidence: `evidence/comp-pages.json`.
Note: 11 of the 12 URLs are home pages, one is a team page. Her home page is the fair comparison.

| Competitor page | Words | Headings (H1, then H2/H3 as found) |
|---|---|---|
| privatpraxis-psychotherapie-bonn.de/therapeuten/ | 328 | H1 "Ihre Psychotherapeutinnen und Psychotherapeuten in Bonn und Köln"; H2 Team Bonn-Beuel, Team Köln, Kontakt; H3 names of the team |
| psychotherapie-schlottner.de | 133 | no H1; H2 Anschrift, Telefon, E-Mail |
| therapie-schumacher.de | 1279 | H1 "Psychotherapie in Bonn"; H2 Freie Psychotherapieplätze, Behandlung, Organisatorischer Ablauf, Kostenübernahme, Kompetenzen, Kontakt; H3 Anmeldung, Privatpatienten, Gesetzlich Versicherte, Selbstzahler |
| psychotherapie-gippert.de | 376 | H1 "Therapie über den Dächern von Bonn / Psychotherapeutische Praxis Sabrina M. Gippert"; H2 Willkommen; H3 Wer ich bin, Was ich anbiete, Aktuelles, Kontakt |
| raasch-psychotherapie.de | 130 | H1 "Herzlich Willkommen auf der Homepage meiner Praxis für Psychotherapie und Beratung in Bonn"; no H2, no H3 |
| pmp-schoepf.de | 1426 | H1 "Praxis für Psychiatrie und modulare Psychotherapie im Herzen von Bonn"; 12 H2 (news, Terminbuchung, Telefonate, Unser Behandlungsangebot, Supervision …) |
| praxis-august-renner.de | 297 | H1 "Psychotherapie Bonn-Bad Godesberg" and "Psychotherapie in Bonn"; H2 Ihr Heilpraktiker, Gesprächstherapie wirkt, Entwicklung, Vortragscoaching, Behandlung psychischer Beschwerden und Erkrankungen, Psychotherapie Verfahren und Methoden |
| psychotherapie-sprick.de | 1017 | H1 "Privatpraxis" (plus 9 more H1); H2 Was Sie bei Ihrem Besuch erwartet, Psychologische Leistungen, Coaching, Indikationen für eine Therapie, Kosten, Über mich, Kontakt; H3 Einzeltherapie, Paartherapie, Angststörungen … |
| zurueck-in-dein-leben.de | 514 | no H1; H2 "... zurück in dein Leben - in Leichtigkeit, Fröhlichkeit, Unbeschwertheit!"; H3 Kontakt |
| heilpraktiker-bonn.de | 727 | H1 "Heilpraktiker Bonn - Ihre Privatpraxis" (3 H1); H2 Praxis Theuerzeit GbR (twice) |
| karinstuehn.de | 319 | H1 "Psychotherapie & Jobcoaching"; H3 Über mich, Psychotherapie, Jobcoaching, Honorar, was meine klienten sagen |
| psychotherapie-zaehr.de | 990 | H1 "Praxis für körperorientierte Psychotherapie, Traumatherapie und Hypnose in Bonn"; H2 Matthias Zähr - Heilpraktiker beschränkt auf das Gebiet der Psychotherapie, Mein psychotherapeutisches Angebot, Kontakt - Praxis Bonn |

Numbers (from `evidence/comp-pages.json`):
- **Mean word count of the 12 competitor pages: 628** (sum 7536). Median: 445. Range: 130 to 1426. 6 of 12 pages have 500 words or more; 6 of 12 have fewer than 500.
- Her pages: home 745 words, topic pages mean 472, longest page 1198 (section 3). Her home page is longer than the competitor mean (745 against 628) and longer than 8 of the 12 competitor pages. Her topic pages are close to the competitor median. Page length is not her gap. Do not write that her pages are too short.
- Structure is the difference. 10 of 12 competitor pages have at least one H1; 10 of 12 have H2 headings. Her 4 topic pages have no H1 and no H2. Only 2 competitors have a service-plus-city H1 close to the keyword ("Psychotherapie in Bonn", "Psychotherapie Bonn-Bad Godesberg"). Her home H1 has no service and no city.
- Technical comparison: 7 of 12 competitor pages have JSON-LD (her site: 0 of 13). 4 of 12 have a `tel:` link (her site: 0 of 13). 3 of 12 have a form (she has one, on `/kontakt`). 1 of 12 has an FAQ signal.
- Closest like-for-like competitors (Heilpraktiker for Psychotherapie in Bonn): praxis-august-renner.de (297 words), psychotherapie-zaehr.de (990), heilpraktiker-bonn.de (727), zurueck-in-dein-leben.de (514). Mean of these 4: 632.

## 6. Summary for agent E (facts only)

- No tap-to-call link, the phone number is plain text (finding 1).
- Form only on `/kontakt`, with 6 fields (finding 3).
- No H1 on 5 pages, no schema on any page, GTM present (findings 6, 7).
- Price conflict: 100 EUR (home) against 80 EUR (price page) for the Einzelgespräch (section 2).
- 19 quoted sentences for the "Werberecht" row (section 4).
- Competitor mean is 628 words (12 pages); her home has 745. Length is not her gap, structure is (section 5).
- Home has 745 words. Topic pages have 339 to 705 words (section 3).
- The four "dead links" in `site.json` are false alarms (finding 5).
