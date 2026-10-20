# Site findings: soziokratie.org (agent B, 2026-10-12)

Site: https://www.soziokratie.org/ (WordPress, Yoast SEO, GA4 G-B1S9LNDXG4). No browser used. No paid call.
Evidence files: `evidence/site.json`, `evidence/site-pages.json` (30 pages of 136 sitemap URLs), `evidence/comp-pages.json`, `evidence/own-commercial-pages.json`. Other proof is a curl check. The URL is named at each finding.

## 1. Technical checks

| Check | Result | Evidence |
|---|---|---|
| http to https | OK. `http://www.soziokratie.org/` gives 301 to `https://www.soziokratie.org/`. | `site.json` (`http_redirects_to_https: true`), curl |
| Non-www | `http://soziokratie.org/` gives 301 to `https://soziokratie.org/`, then 301 to `https://www.soziokratie.org/`. Two hops. Minor. | curl -IL |
| `href="tel:` | **0 on all pages.** Checked: home, Impressum, /termine/, /konsentmoderation/, /agbs/, /begleiterinnen/, /was-ist-soziokratie/, /fallbeispiele/, book page. 0 of 30 measured pages have a tel link. | `site-pages.json` (`tel_link` false on all 30), curl |
| Phone number | The number is in the footer of every page as plain text: `++43-699-11114398` (double plus, typo). Impressum has `Tel.: +43(0)699-11114398`, `werktags 8-17 Uhr`. A phone icon `telefon.jpg` has no link. | home HTML, https://www.soziokratie.org/impressum-soziokratie-christian-ruether/ |
| Contact page | **None.** No page called Kontakt. `contact_url` is null. The only way to reach him is the footer e-mail `chrisruether@gmail.com` (shown as `chrisruether[ad]gmail.com`, link is `mailto:`) and the plain-text phone. | `site.json` (`contact_url: null`), sitemap |
| Contact form | **None** on home, Impressum, Termine, Angebote, Konsentmoderation. The only form is the workshop sign-up form on https://www.soziokratie.org/anmeldung/ (1 `<form>`). Impressum says "Das Formular versendet lediglich eine Email an mich", but the Impressum has no form. | `site.json` (`form_on_home: false`), curl, `own-commercial-pages.json` |
| Duplicate pages (same title and word count) | **None.** Checked on 128 sitemap URLs (page and post sitemap). `duplicate_pages` is empty. | `site.json`, curl of sitemap |
| Duplicate title (different content) | 1 title is used twice: `Soziokratie, Beratung, Konsent, Christian Rüther, Christian Ruether, Wien` on /elemente/. /angebote/ has `Soziokratie, Beratung, Konsent, Christian Rüther, Christian Ruether` (nearly the same, keyword list). | curl, `own-commercial-pages.json` |
| Title format | 116 of 128 titles end with ` -` (empty site name), for example `Fallbeispiele -`, `Anmeldung -`, `KonsenT-Moderation -`. Home title is only `Soziokratie`. | curl of 128 pages; `site-pages.json` (29 of 30) |
| H1 on home | **No H1.** Only H2 `Willkommen`. 1 of 30 measured pages has no H1 (the home page). | `site.json` (`home_h1: []`) |
| Meta description | 1 of 30 measured pages has one (home). 29 have none. Most measured pages are newsletters and "Elemente" pages. | `site-pages.json` |
| Schema | Yoast graph only (WebPage, WebSite, BreadcrumbList). No Organization, no LocalBusiness, no ProfessionalService, no Course/Event. `Person` is on 1 page only (/2015/08/willkommen/). | `site-pages.json` (`jsonld_types`) |
| Dead links from home | None real. `xmlrpc.php` gives 405, which is normal. | `site.json` |
| Speed | Server response (TTFB) 1.3 to 1.4 s on 3 runs. Slow for a static WordPress page. | `site.json` (`ttfb_secs`) |
| Orphan commercial page | https://www.soziokratie.org/angebote/ (the consulting offer with day rates) has **1 internal link**, from a 2015 post (/2015/08/willkommen/). The home page and the main menu do not link to it. | curl link check on 128 pages |

## 2. Price page

There are three price places. They do not agree in structure, and no page shows all prices.

### a) https://www.soziokratie.org/angebote/ (consulting prices, orphan page)
"Preise (als Orientierung für eine individuelle Abmachung, alle Preise zzgl. 20% Umsatzsteuer)"

| Service | Price |
|---|---|
| Tagessatz Profit-Unternehmen | 1.800 – 2.400,– Euro (300–400 Euro pro Stunde) |
| Tagessatz Non-Profit-Unternehmen | 1.200 – 1.800,– Euro (200–300 Euro pro Stunde) |
| Coaching / Mediation / Kurz-Gigs | 200–400 Euro pro Stunde |
| Vorbereitungszeit und Arbeiten ohne direkten Kundenkontakt | 100–200 Euro pro Stunde (halber Satz) |

Sentence on the page: "Wenn das Projekt „spannend" ist, arbeite ich auch zu einem geringeren Stunden-/ und Tagessatz. Es soll nicht am Geld scheitern!"

### b) https://www.soziokratie.org/termine/workshop-konsent-moderation/ and https://www.soziokratie.org/termine/workshop-soziokratie/ (all plus 20% USt)

| Service | Price |
|---|---|
| Workshop KonsenT-Moderation, 2 days, Privat-Personen | 290 Euro |
| Workshop KonsenT-Moderation, NPO-Mitarbeiter | 490 Euro |
| Workshop KonsenT-Moderation, Profit-Mitarbeiter/Berater | 690 Euro |
| Frühbucher | 10% off, if paid 2 months before start |

### c) https://www.soziokratie.org/anmeldung/ (form options) and the schnuppern pages

| Service | Price |
|---|---|
| Schnupper-WS KonsenT-Moderation, Privat / NPO / Berater Profit | 50 / 100 / 150 Euro (https://www.soziokratie.org/termine/schnuppern-konsent-moderation/) |
| Schnupper-Soziokratie, Privat+NPO / Profit | 120 / 240 Euro (https://www.soziokratie.org/termine/schnuppern-soziokratie/) |
| Form option "anderer Preis - individuelle Vereinbarung" | no number |

### d) https://www.soziokratie.org/konsentmoderation/ (product ladder)

| Service | Price |
|---|---|
| Buch "KonsenT-Moderation" (Hardcopy) | 19 Euro |
| Brettspiel "Keep-the-Balance" | 45 Euro |
| Workshop "KonsenT-Moderation" | 290 – 690 Euro zzgl. Ust |
| Buch als PDF via Leanpub (book page) | ab 7.99 $ (Spende, PDF is free on site) |
| Supervision "Team-Sitzung" | no price |
| Team-Experiment Entscheidungs-Poker (1,5 h) | no price |
| Team-Experiment KonsenT-Moderation (3 h, "ca. ein Berater-Tag") | no price |
| Ausbildung "KonsenT-Moderation" (5 days over 3 months) | no price, "noch in der Designphase" |
| Lernweg KonsenT-Moderation (6 months, "ca. fünf Berater-Tage") | no price |
| Supervision "KonsenT-Moderation" (online) | gratis |

Finding: the day rate is on an orphan page (1 link, from 2015). The "Lernweg" and "Team-Experiment" have a time size but no price. A visitor cannot see the price of the 5-day product anywhere.

## 3. Outdated sentences and sentences that block enquiries

| # | Quote | URL | Why it blocks or is old |
|---|---|---|---|
| 1 | "Derzeit biete ich selbst keine offenen Workshops an. Wenn Sie mehr über die Soziokratie oder die KonsenT-Moderation erfahren möchte, freue ich mich über eine Anfrage." | https://www.soziokratie.org/ | First sentence under "Workshops" on the home page. It says no offer. It has no link or button for the enquiry. Typo "möchte". |
| 2 | "derzeit keine Angebote" | https://www.soziokratie.org/termine/ | The Termine page is an empty table. The only content is links to other providers (Soziokratie-Zentrum, Emcra, The Sociocracy Group). |
| 3 | "derzeit keine Angebote" (under "Daten") | https://www.soziokratie.org/termine/workshop-konsent-moderation/ | The workshop page has a full price list but no date. Next to it: "Anmeldeformular". |
| 4 | "derzeit keine Termine" / "derzeit keine Termine geplant" | https://www.soziokratie.org/termine/schnuppern-soziokratie/ and https://www.soziokratie.org/termine/schnuppern-konsent-moderation/ | Same problem. |
| 5 | "Online Workshop KonsenT-Moderation am 07./08. Oktober 2025" | https://www.soziokratie.org/anmeldung/ | The sign-up form still offers a date that is one year past (today 12.10.2026). |
| 6 | "Derzeit funktioniert die Online-Anmeldung leider nicht, daher mir einfach eine Email an" | https://www.soziokratie.org/newsletter/ | The newsletter sign-up is broken. The home page still sends visitors to "Newsletter-Anmeldung". |
| 7 | "Ausbildung „KonsenT-Moderation" = fünftägige Lernreise über drei Monate (noch in der Designphase)" | https://www.soziokratie.org/konsentmoderation/ | The main paid offer is not ready. |
| 8 | "Ich schau mal, was mehr angenommen wird und lösche den anderen Ende Juni 23." | https://www.soziokratie.org/konsentmoderation/ | Slack/Discord test from June 2023. Old. |
| 9 | "Mein neues Buch ist jetzt draußen." (book is from 08/2022) | footer of every page, for example https://www.soziokratie.org/ | "Neu" is 4 years old. |
| 10 | "Begleiter*innen (eine Liste … – noch im Aufbau)" and "Austauschforen (eher noch im Aufbau)" | https://www.soziokratie.org/ and footer | Menu items marked as unfinished. |
| 11 | "Amazon hat noch einige Bücher vorrätig, ist aber böse." and "Aktuell muss man als Gast leider vorher den Browser-Cache leeren, bevor die Bestellung dort abgeschlossen werden kann." | https://www.soziokratie.org/konsentmoderation/konsentmoderation-buch/ | The order path asks the buyer to do a technical step. |
| 12 | "Wer eingeladen werden möchte bitte Email an mich" | https://www.soziokratie.org/konsentmoderation/ | Every route ends at one e-mail address. There is no form. |
| 13 | "Stand 04/2023" | https://www.soziokratie.org/agbs/ | AGB are 3 years old. |
| 14 | "Datenschutzerklärung … durch den Websitebetreiber [Ihre Kontaktdaten einfügen]" and the text cites German law (BDSG, TMG) for an Austrian e.U. in Wien | https://www.soziokratie.org/impressum-soziokratie-christian-ruether/ | Template placeholder is still in the text. Trust and legal risk. |
| 15 | "Normalerweise antworte ich innerhalb von 48 Stunden. Sollte das nicht passieren, bitte beharrlich nachfragen!!" | https://www.soziokratie.org/anmeldung/ | Slow reply promise. A buyer may leave. |

Not blocking, but note: the consulting offer (Angebote) and the price list are not reachable from the home menu. The home page offers Termine (empty), Fundus, Fallbeispiele and others, but no "Beratung" or "Angebote".

## 4. Competitor page length (from `demand.md`, gap keyword "organisationsberatung wien")

Tool: `content-pool-skill/scripts/page_metrics.py`. Evidence: `evidence/comp-pages.json`. 5 of 5 pages readable.

| Competitor URL | Words | H1 | tel link | Form | FAQ |
|---|---|---|---|---|---|
| https://systworks.com/organisationsberatung/ | 885 | "a systemic approach​systemische Organisationsberatung | Coaching" | no | no | no |
| https://www.wonderwerk.com/change-management/ | 621 | "ChangeManagement" | no | no | no |
| https://diebusinesscoach.at/organisationsentwicklung-changemanagement/ | 745 | "ORGANISATIONSENTWICKLUNG & CHANGEMANAGEMENT" | yes | yes | yes |
| https://www.inspiringleaders.at/de/organisationsentwicklung | 922 | none (no H1) | yes | no | yes |
| https://www.janesconsulting.com/beratungsfelder.html | 328 | "Beratungsfelder" | no | no | no |

**Mean word count: 700** (range 328 to 922). None of the 5 shows a price.

His pages, same tool (`evidence/own-commercial-pages.json`): /angebote/ 978, /konsentmoderation/ 959, /termine/ 754, /termine/workshop-konsent-moderation/ 997, /anmeldung/ 723. The tool counts the sidebar text on his pages ("Über mich", "Wichtige Materialien", about 600 words on every page). The main text alone is much shorter. My count of the main text (curl, text before "Über mich"): /angebote/ about 343 words, /konsentmoderation/ about 329, /workshop-konsent-moderation/ about 270, /termine/ about 119.

What the data shows:
- Length is not his gap. With the sidebar his offer pages (723–997 words) are at or above the competitor mean (700). Without it they are at 119–343 words, below the mean.
- Two of 5 competitors have a tel link (diebusinesscoach.at, inspiringleaders.at). His site has none on 0 of 30 pages.
- His pages can be longer in main text, but the first fix is structure: one clear consulting page, with H1, a price and a contact path. The 1 competitor with the most direct contact path (diebusinesscoach.at) has tel, form and FAQ on one 745-word page.
- Page length alone does not explain rank. The data has no rank-to-length link; 5 pages are too few.

## 5. Summary for the review page (facts only)

1. No tel link and no contact page or form on any measured page. Phone is text with a typo (`++43`).
2. No H1 on home. Title is one word. 29 of 30 measured pages have no meta description.
3. Home page sentence "Derzeit biete ich selbst keine offenen Workshops an" and 4 more "derzeit keine ..." pages. The sign-up form lists a past date (Oktober 2025).
4. Day rates (1.800–2.400 Euro) are on an orphan page with 1 internal link, from 2015. Workshop prices (290/490/690 Euro) exist, but without a date.
5. Newsletter sign-up is broken (own sentence on /newsletter/).
6. Impressum has a template placeholder and German law references for an Austrian business.
7. Non-www redirect takes 2 hops. Server response is 1.3–1.4 s.
