# Site findings: Bestattungsinstitut Pinkert und Partner, Riesa (agent B, 2026-10-13)

Site: https://bestattung-pinkertundpartner.de/ (CMS and hosting by CTH Riesa GmbH, per /impressum/).
Evidence files: `evidence/site.json`, `evidence/site-pages.json`, `evidence/comp-pages.json`, `evidence/site-urls.json`. curl copies: scratchpad only.
Branch: service (not health). HWG check skipped. A wording check for grieving families is in section 7.

## 1. Structure
- Sitemap has 6 URLs (`/sitemap.xml`): `/`, `/unser-haus/`, `/leistungen/`, `/kontakt/`, `/impressum/`, `/datenschutz/`. All return 200.
- Menu has 4 items: Home, Unser Haus, Leistungen, Kontakt. There is no page for one service, one burial type, Vorsorge, or one town.
- Word counts (`evidence/site-pages.json`): home 172, /leistungen/ 146, /unser-haus/ 385 (rendered, mostly image captions), /kontakt/ 346 (rendered). The curl text of /unser-haus/ is about 157 words and /kontakt/ about 118 words.
- Duplicate pages: none (`duplicate_pages: []`). `/home/` and `/index.php` return 404.
- Canonical tags are correct on all pages.
- Dead links from home: none.

## 2. Technical checks
| Check | Result | Source |
|---|---|---|
| http to https | Yes. `http://bestattung-pinkertundpartner.de/` returns 301 to https. www also returns 301 to the bare domain. | curl -I |
| tel: link, home | Yes, `tel:+493525735814`, one link in the header ("Rufen Sie an: 03525 735814"). | `/` source |
| tel: link, contact | Yes, same single header link. The two numbers in the contact text (03525 735814 and 03525 733889) are plain text, not links. | `/kontakt/` source, lines 60, 106, 147 |
| tel: link, service page | Yes, same header link on `/leistungen/`. | `/leistungen/` source |
| Contact form | Yes, on every page (home, contact, services, imprint) and also in the footer block "Kontaktieren Sie uns". Fields: name, email, message, privacy checkbox, honeypot. No phone number field, no callback option. | `evidence/site.json` `form_on_contact: true`; `/kontakt/` source |
| 24-hour phone shown | Only on `/kontakt/`: "Tag und Nacht sind wir telefonisch dienstbereit unter Telefon (03525) 735814." (bold, italic, 1.2 em). Not on the home page and not next to the header phone. | `/kontakt/` line 118 |
| Opening hours | "Montag - Freitag 8.00 - 17.00 Uhr" on `/kontakt/` only. | `/kontakt/` |
| Meta descriptions | Empty on home, services, house, contact. Only the imprint has one. | `evidence/site-pages.json` |
| Titles | Pattern "Home / Pinkert & Partner", "Leistungen / Pinkert & Partner". No town, no "Bestatter" or "Bestattungsinstitut" in any title. | `evidence/site-pages.json` |
| H1 | Home has no H1 (`pages_no_h1: 1`, `home_h1: []`). The home headline "Gemeinsam durch schwere Zeiten" is an H2. Other pages: /leistungen/ "Unsere Leistungen für Sie", /unser-haus/ "Ihr Vertrauen - unsere Erfahrung", /kontakt/ "Wir sind für Sie da". No H1 names the town or the trade. | `evidence/site-pages.json` |
| Schema | None. `jsonld_blocks: 0`. | `evidence/site.json` |
| Analytics | No GA4 and no GTM id found. | `evidence/site.json` |
| Image alt text | All content images on /unser-haus/ and /kontakt/ have empty `alt=""`. | `/unser-haus/` source |
| Speed (server wait) | 0.82, 0.85, 0.84 s. | `evidence/site.json` |
| Mobile | Viewport meta present. | home source |
| Cookie banner | Present ("Cookie-Einstellungen bearbeiten"). | home source |

## 3. Addresses (both locations)
- Goethestr. 1, 01589 Riesa: on `/kontakt/` ("Sie erreichen uns in unserem Büro", access via Dr.-Külz-Straße) and in the imprint (`/impressum/`, only this address). The map on home and contact points at 51.30059505, 13.312447144395364 (the Goethestr. area).
- Riesaer Straße 40: on `/kontakt/` only, under "Unsere Trauerhalle", with its own phone 03525 733889. The site writes "01589 Oelsitz". Google panel 2 writes "01594 Riesa-Oelsitz" (`evidence/google-panel-2-2026-10-13.md`). The postcode and the town name do not match.
- Riesaer Str. 40 is not in the imprint and not on the home page.
- Google has two listings (`evidence/google-panel-2026-10-13.md` and `evidence/google-panel-2-2026-10-13.md`). Both use the same website and the same phone 03525 735814. Panel 1 (Goethestraße 1) has 5,0 with 4 reviews. Panel 2 (Riesaer Str. 40) has 3,2 with 5 reviews, an "Als Inhaber eintragen" prompt, and its pin sits on open land. The site says Riesaer Str. 40 is the Trauerhalle, not the office. Panel 2 is therefore a second, unclaimed listing for the chapel with the same phone as the office.
- Directory listings (Gelbe Seiten, Das Örtliche) show Riesaer Str. 40 in 01594 Riesa-Oelsitz (`demand.md` section 5).

## 4. Prices
There is no price on any page of the site. Evidence: `price_mention: false` on all 6 pages in `evidence/site-pages.json`; a grep for "€", "Euro", "Kosten", "Preis" finds only "in jeder Preislage" on /leistungen/ ("Vielfältige Auswahl an Sarg-, Urnen- und Deckengarnituren in jeder Preislage"). There is no Vorsorge price, no Kostenübersicht and no price example.
- For the calculator: no `val` from the site. Use a market figure with a source, or a neutral figure.
- Demand for cost pages is large (`demand.md`): "was kostet eine beerdigung" 4.400 searches per month and "bestattung kosten" 1.900. No competitor page in the length check shows a price either (`price_mention: false` for all 5).

## 5. Content and trust signals on the site
- Founded 1991 by the families Pinkert and Eisner (home page). Owner: Conny Pinkert-Stockert (imprint). The site never names a person on the page itself, and shows no photo of the team.
- Claim "Fachgeprüfte Bestatter" (/unser-haus/) and the logo `logo-bestatterhandwerk.png` on the home page (alt empty). The Bestatterinnung Sachsen lists her (`demand.md` section 5). The review page may use these two items as trust signals. The page must not claim more than "Fachgeprüfte Bestatter".
- "Seit nun mehr als 30 Jahren" (home): the 1991 start means 35 years. The text is out of date.
- No reviews, no testimonials, no rating on the site (`rating_mention: false`). Google has 4 reviews at 5,0 for panel 1.
- Services on /leistungen/ (13 items): Erd-, Feuer-, Wald- und Seebestattung (one line, one sentence), Sarg-/Urnen-/Deckengarnituren, Überführungen, Trauerfeier und Beerdigung, Aufbahrung in der Trauerhalle, Träger, weltliche Rednerin, Drucksachen, Blumenschmuck, Zeitungsanzeigen, Bestattungsvorsorge-Verträge, Behördengänge. Each is one line. There is no text on what happens first, what a family must do within the first days, or what Vorsorge costs.
- The page then lists documents the family must bring (Totenschein, Personalausweis, Stammbuch, and others). This is useful content but sits under a list of services with no heading.

## 6. Competitor page length (second pass, `evidence/comp-pages.json`)
Tool: `content-pool-skill/scripts/page_metrics.py`. It counts visible words and removes script, style, noscript, nav, footer, header, svg, form and iframe. It does NOT remove `aside` or sidebar blocks. Sidebar text would count. No sidebar was confirmed in the 5 pages. Fritsche (1525 words) is the long page and has a gallery and a location block.

| Competitor URL | Words | H1 | Notes |
|---|---|---|---|
| https://trauerhilfe-wuensche.de/bestattungen-riesa/ | 491 | "Bestatter in Riesa" | Rank 1. Title "Bestatter Riesa: Bestattungen im Bestattungsinstitut Riesa". Meta description set. Schema: AggregateRating, Service, Organization, WebSite, BreadcrumbList and more (no LocalBusiness type listed). No tel: link. |
| https://www.bestattungshaus-fritsche.de/ | 1525 | "Willkommen bei Ihrem Privaten Bestattungshaus Fritsche in Riesa" | Rank 2. tel: link yes. Sections Dienstleistungen, Bestattungsvorsorge, Wichtige Dokumente, Galerie, Standorte, Anfrage. |
| https://riesa.krematorium-meissen.de/agentur-riesa.html | 202 | "Städtisches Bestattungswesen Meißen" | Rank 3. Chrome-rendered. Short page. |
| https://www.bestatter-riesa.de/ | 366 | "Bestattung Riesa" | Rank 1 and 2 on several terms. tel: link yes. No form. |
| https://www.bestatter-riesa.de/bestattungsarten/tree-of-life-baumbestattung | 237 | "Tree of Life Baumbestattung Riesa" | Service sub-page. |

- Mean: 564 words over 5 pages. Without the Fritsche page: 324 words over 4 pages. Median: 366 words.
- Her home page has 172 words, her services page 146 words. Her pages are shorter than the median, but not by a large amount compared with 3 of the 5 competitors (202, 237, 366). Page length is not the main gap.
- What the data shows: every competitor H1 names the town (Riesa) or the trade. Her home page has no H1. Her title shows no town. Two of the five competitors have a service sub-page with the town in the H1 (bestatter-riesa.de). She has none.
- Her site ranks organic 5 for "bestatter riesa" and 12 for "bestattungsinstitut riesa" anyway (`demand.md` section 2). The ranking comes from the domain and the Google listing, not from page text.

## 7. Wording check for grieving families (non-health branch)
No healing promise, no disease claim, no price claim. Notes for the review page and the homepage draft:
- Do not write "rund um die Uhr erreichbar" as a promise of arrival times. The site says "telefonisch dienstbereit" (phone only). Use the same limit.
- Do not write "günstig", "Festpreis" or "schon ab ... Euro" for a funeral. The site gives no price, and prices are sensitive for families.
- Avoid sales words such as "Angebot", "jetzt buchen", "Termin sichern" and urgency copy. Use "Rufen Sie an" or "Wir rufen Sie zurück".
- The review page should speak of "Familien, die in den ersten Tagen Hilfe suchen", not of "Kunden" or "Leads".
- /unser-haus/ shows many photos of arrangements (40 images on the page) with surnames in the file names (`/media/web_300w/siemens8.jpg`, `zuchantke6.jpg`, `harzbecker4.jpg`, `horv_th2.jpg`, `zeppan2.jpg`, `weser4.jpg`, `jaehnig8.jpg`, `dusemond3.jpg`, `seifert6.jpg`, `allich9.jpg`). The file names expose family names publicly. Do not copy these images or names into the review page. Flag it to Martin as a privacy point, in neutral words.
- Text errors on the site that the page should not repeat: "kompetender Ansprechpartner" (home), "soviel wie möglich, oder Sie es möchten" (/unser-haus/), "Telefax" and "GEZ", "Telekom" (old terms, /leistungen/).

## 8. Summary of gaps for the review page (facts only)
1. No H1 on the home page. No page title or H1 names Riesa or the trade.
2. Empty meta descriptions on 5 of 6 pages.
3. No schema, no analytics.
4. No price anywhere, no Vorsorge page, no page per burial type.
5. The 24-hour phone line is shown only on `/kontakt/`, not on the home page.
6. Two Google listings: Goethestraße 1 (5,0, 4 reviews) and Riesaer Str. 40 (3,2, 5 reviews, unclaimed). The site names Riesaer Str. 40 only as chapel, and the postcode differs (01589 on the site, 01594 on Google).
7. Image alt text empty on all content images.
8. Brand-name search "bestattung pinkert": her site is not in the top 10 (`demand.md` section 5).

## 9. Blockers
None. All steps ran without errors.
