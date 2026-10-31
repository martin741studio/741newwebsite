# Site findings: Thorsten Schmidt (agent B, 2026-10-31)

Site: https://kanzlei-schmidt.online/ (GoDaddy Website Builder 8.0, `meta generator` in `evidence/home.html`). Branch: legal (no HWG pass). Form of address on the site: "Sie".
Status: done, both passes (second pass: section 10).

## 1. Pages and word counts
Source: `evidence/site-pages.json` (page_metrics via `collect_site.py`), `evidence/site.json`, `evidence/rendered-start.md`, `evidence/rendered-berater.md`.

| URL | Title tag | Words | H1 | In nav |
|---|---|---|---|---|
| `/` and `/start` | Start | 297 | 2 (same text twice) | yes |
| `/ihr-berater` | Ihr Berater | 246 | 1 | yes |
| `/impressum` | Impressum | 561 | 1 | yes |
| `/datenschutzerklärung` | Datenschutzerklärung | 3216 | 1 | yes |
| `/hinweise` | Hinweise | 134 | 1 | NO (only in the sitemap; no link on the site) |
| `/m/login`, `/m/reset`, `/m/create` | Anmelden, Passwort zurücksetzen, Passwort festlegen | 97 / 82 / 90 | 1 each | no (GoDaddy account pages) |

- The real content of the site is two pages with about 540 words together (start 297, ihr-berater 246). Word counts include menu, footer and cookie text.
- curl does show the text. The page is server-rendered (118 KB HTML). The brief expected JS rendering; that is not the case here. Firecrawl text matches curl (`evidence/rendered-start.md`, `evidence/rendered-berater.md`).
- No service has its own page. All services are one bullet list on the start page (13 bullets under 3 headings: Steuerberatung, Rechtsberatung, Buchhaltung / Jahresabschluss / Steuererklärungen).
- Sitemap: `sitemap.xml` is an index with two files. `sitemap.website.xml` lists 8 URLs (`evidence/sitemap.website.xml`). `sitemap.ola.xml` returns HTTP 400. `robots.txt` contains only `Disallow: /404` (`evidence/robots.txt`).

## 2. Technical checks (curl)
| Check | Result | Evidence |
|---|---|---|
| http -> https | OK: `http://` gives 308 to `https://kanzlei-schmidt.online/`. `www` gives 301 to http, then 308 to https (two hops) | curl -I, `evidence/site.json` `http_redirects_to_https: true` |
| Server time | TTFB 0.20 to 0.22 s (3 runs). A first collector run timed out once on curl (transient), the second run was clean | `evidence/site.json` |
| Duplicate page | `/` and `/start` are byte-identical (cmp), same title "Start", 297 words, no canonical tag. `og:url` says `/start` | `evidence/home.html`, `evidence/p-start.html`, `evidence/site.json` `duplicate_pages` |
| Home title | "Start" (no firm name, no keyword, no city) | `evidence/home.html` |
| Meta description | Missing on all pages. Only `og:description` "Ich freue mich, Sie persönlich kennenzulernen" and `twitter:description` "Interdisziplinäre Beratung auf den Punkt". `og:title` = "Kanzlei Schmidt", but `<title>` = "Start" | `evidence/home.html` |
| `og:image` | Points to a video URL (`img1.wsimg.com/isteam/videos/5ZQADOw`), not an image | `evidence/home.html` |
| Canonical / robots meta | None | `evidence/home.html` |
| JSON-LD | 0 blocks on all pages (no LegalService, Attorney, LocalBusiness or Person schema) | `evidence/site.json` `jsonld_blocks: 0` |
| H1 | Start page has 2 H1 with identical text (GoDaddy desktop and mobile variant); no H3 level, headings jump H2 to H4 | `evidence/site-pages.json` |
| Images without alt | 1 on start, 2 on ihr-berater; hero alt is the URL string `https://img1.wsimg.com/isteam/videos/5ZQADOw` | `evidence/home.html`, `evidence/p-ihr-berater.html` |
| Dead links from home | 0 of 6 internal links | `evidence/site.json` |
| Viewport meta | present | `evidence/home.html` |

## 3. GoDaddy artefact (visible in the page source and in the rendered text)
- The header of every page contains "Angemeldet als: filler@godaddy.com" (twice per page: desktop and mobile menu) plus "Anmelden", "Mein Konto", "Abmelden" links to `/m/account`.
- Evidence: `grep filler@godaddy.com` hits in all 6 HTML files in `evidence/`; also in `evidence/rendered-start.md` and `evidence/rendered-berater.md`.
- It sits in the menu markup (hidden state in the browser, but visible in the source and in the text that Firecrawl returned). A normal visitor probably does not see it; crawlers and AI tools read it. Not confirmed by screenshot (no Chrome used in this role).
- The GoDaddy login/reset/create pages (`/m/login`, `/m/reset`, `/m/create`) are in the sitemap and have no noindex tag in the HTML.

## 4. Contact path
- Phone: `href="tel:022412407450"` exists ONLY on `/ihr-berater` (in the contact block). NO tel link on the start page, the Impressum or the Datenschutzerklärung. The start page shows no phone number at all. Evidence: `grep tel:` per file in `evidence/`.
- Start page: one button "Kontakt aufnehmen" = `mailto:kontakt@kanzlei-schmidt.online` with a prefilled subject and text. No form, no phone, no address on the start page. (`evidence/rendered-start.md`)
- Contact form: only on `/ihr-berater`. Fields: Name, E-Mail (required), Nachricht, button "Senden", reCAPTCHA notice (`evidence/p-ihr-berater.html`). There is no separate contact page. `collect_site.py` reports `contact_url: null` because the home page has no "Kontakt" link to a page; this is correct for this site.
- Address: Sieglarer Straße 2C, 53840 Troisdorf, shown on `/ihr-berater` and the Impressum. No opening hours, no map, no appointment link.
- E-mail addresses differ: `kontakt@kanzlei-schmidt.online` (button, Impressum) and `info@kanzlei-schmidt.online` (Impressum text, Datenschutzerklärung).
- Social: Instagram `@steuerjurist`, LinkedIn `thorsten-schmidt-104174203` (footer).

## 5. Tracking and cookie banner
Source: `evidence/home.html`.
- Google tag: loads `googletagmanager.com/gtag/js?id=UA-196799898-1` (old Universal Analytics ID) and the GA4 ID `G-BF2FDR6KMM`. No GTM container.
- Meta Pixel: `fbq('init', '282429905966327')` and `fbq('track', 'PageView')` are in the page code.
- Cookie banner: yes, "Ablehnen / Annehmen". The accept handler sets `analytics_storage` and `ad_storage` to "granted". Wording typo in the banner: "Wenn Sie Cookies akzeptierst" (Sie and du mixed).
- Observation only, no legal assessment, not for the page: the Datenschutzerklärung (3216 words) names Facebook plugins (Like and Share button) but has no hit for "Google Analytics" or the Meta Pixel (`evidence/p-datenschutzerkl%C3%A4rung.html`: "Google Analytics" 0 hits, "Pixel" 0 hits). The site shows no Facebook Like button. The prospect is a lawyer, so Agent E should not use this point in the copy.

## 6. Impressum wording (observation, not for the page)
Source: `evidence/p-impressum.html`.
- Cites §§ 7 to 10 TMG (the TMG was replaced by the DDG in 2024).
- The OS platform link is malformed (`https:/ec.europa.eu/consumers/odr`, one slash).
- The Impressum is complete in structure: RAK Köln and StBK Köln, Berufshaftpflicht, USt-IdNr, BRAO/RVG/BORA/StBerG/BOSt. This is a trust signal that the page can repeat without claims (names of the chambers).
- The Impressum mixes "ich" and "wir" ("werden wir diese Inhalte umgehend entfernen").

## 7. Content on the page (what exists, for the homepage draft)
Source: `evidence/rendered-start.md`, `evidence/rendered-berater.md`.
- Hero: "Interdisziplinäre Beratung auf den Punkt", subline "Ich freue mich, Sie persönlich kennenzulernen", hero video (og:image video id 5ZQADOw).
- Person: Thorsten Schmidt, "Rechtsanwalt - Steuerberater". Rechtsanwalt since 2016, Steuerberater since 2018 (Werdegang, `/ihr-berater`). Studied Betriebswirtschaft and Rechtswissenschaften.
- Position: "interdisziplinärer Berater ... an der Schnittstelle von Gesellschaftsrecht und Steuerrecht". Tagline "Ihre Vision ist mein Ansporn".
- Services: Steuergestaltung, Immobilienbesteuerung, Internationales Steuerrecht, Erbschaft- und Schenkungsteuer, Steuerstreitführung; Gesellschaftsrecht, Gesellschafterstreit, Unternehmenstransaktionen, Internationales Gesellschaftsrecht, Steuerberaterhaftung; Buchhaltung, Jahresabschluss, Steuererklärung (Unternehmen und Inhaber).
- Target group (implied): business owners, company shareholders, real estate investors. Not private-person tax returns.
- Missing: reviews or testimonials, client names or case examples, number of clients, a photo caption, a FAQ, location pages, Fachanwalt title (not claimed; none shown), opening hours, price information, any blog or guide.
- Page names are not search terms: "Start", "Ihr Berater". No page contains the words "Steuerberater Troisdorf" or "Rechtsanwalt Troisdorf" as a heading. Troisdorf appears only once in the body: "vor Ort in Troisdorf" (`/ihr-berater`).

## 8. Prices and fee logic
- No price page and no price on any page. For the calculator: "no prices on the site".
- Typical fee logic, as background only (not on the site): lawyers are paid by RVG or by agreement; tax advisers by StBVV or by agreement. The Impressum only lists the RVG and the StBerG as professional rules, with no amounts (`evidence/p-impressum.html`). The site mentions "Allgemeine Auftragsbedingungen" and "Widerrufsbelehrung" as PDF downloads on `/hinweise` (an unlinked page, 134 words).

## 9. Superlatives and promises (legal branch: note only, no HWG)
Quotes from `evidence/rendered-start.md` and `evidence/rendered-berater.md`:
- "Dabei ist es mir wichtig, dass ich den besten Weg für Sie finde." (`/ihr-berater`)
- "Beratung und Umsetzung von Möglichkeiten zur Verringerung Ihrer Steuerbelastung" (outcome wording)
- "Konzeptionierung von Strukturen zur Optimierung Ihrer Zahlungsflüsse"; "Optimierung des Übergangs von Vermögen auf die nächste Generation"
- No "führend", "einzigartig", "Nr. 1", "Spezialist" or "Fachanwalt" on the site. Nothing here needs a warning row.

## 10. Second pass: competitor page lengths
Done after `demand.md` was rewritten by agent A (status DONE, 15:13). Evidence: `evidence/comp-pages.json` (page_metrics.py, 6/6 pages readable). URLs: the six Steuerberater provider pages from `demand.md` section 4 (gap keyword "steuerberater troisdorf"). The law sites in `demand.md` cover Straf-, Familien- and Arbeitsrecht, so they were left out. Directories were left out.

| Competitor page | Words | H1 | H2 |
|---|---|---|---|
| steuerkanzlei-nrw.de (SERP rank 1) | 120 | Steuerberatungskanzlei Krauthäuser | Heinz Josef Krauthäuser |
| steuerberaterin-leineweber.de (rank 3) | 393 | Steuerberaterin Rosi Leineweber in Troisdorf, Troisdorf - Niederkassel - Bonn | Steuerberaterin Rosi Leineweber |
| datax-gmbh.de/erstellung-von-jahresabschluessen/ (rank 6) | 755 | Steuerberater aus Troisdorf mit 30 Jahren Erfahrung | Erstellung von Jahresabschlüssen (6 H3 on single services: Buchhaltung, BWA, EÜR, Bilanzen, Betriebsprüfung, Rechtsbehelfe) |
| stb-saelker.de (rank 10) | 12 (page is rendered by Chrome; almost no text) | Steuerkanzlei Sälker | none |
| schaefer-stb.de/team (rank 13) | 381 | none | Wir stellen uns vor (H3: names of 6 team members) |
| hess-steuerberater.de (rank 18, home page) | 133 | Hess & Partner - Ihr kompetenter Partner in Troisdorf; Unser Tipp | none (H3: Sie sind uns wichtig!; Wir sind Ihr zuverlässiger Ansprechpartner.) |

- **Mean word count: 299** (6 pages; median 257; range 12 to 755). Without the near-empty Sälker page the mean is 356 (5 pages).
- Own pages: start 297 words, ihr-berater 246 words. The prospect is at the competitor mean. Only one competitor page (datax-gmbh, 755, a single service page) is clearly longer.
- "Troisdorf" is in the title tag of 3 of 6 competitor pages (Leineweber, datax, Hess) and in the H1 of the same 3. The prospect's title is "Start" and the town is in no heading.
- Other signals on the competitor pages: tel link on 2 of 6 (datax, Schäfer), form on 1 of 6 (datax), JSON-LD on 3 of 6 (datax, Sälker, Schäfer), meta description on 5 of 6, no FAQ, no price on any page. The prospect has a tel link and a form (on one page), but no JSON-LD and no meta description.
- The competitor pages are short too. The data does not support "longer text" as the main advice (lesson 4).

## 11. Evidence index
`evidence/site.json`, `evidence/site-pages.json`, `evidence/site-urls.json`, `evidence/site-page-urls.txt`, `evidence/home.html`, `evidence/p-start.html`, `evidence/p-ihr-berater.html`, `evidence/p-impressum.html`, `evidence/p-datenschutzerkl%C3%A4rung.html`, `evidence/p-hinweise.html`, `evidence/robots.txt`, `evidence/sitemap.website.xml`, `evidence/rendered-start.md`, `evidence/rendered-berater.md`, `evidence/comp-pages.json`.
