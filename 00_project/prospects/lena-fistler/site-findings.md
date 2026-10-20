# Site findings: lenafistler.de (agent B, 2026-10-15)

Site: https://www.lenafistler.de/ (WordPress, IONOS site builder, cookie banner). Form of address: "du".
Method: `collect_site.py` (curl, read only), plus manual curl checks. No browser. No paid call.
Cost: 0 EUR. Evidence files are named at each finding.

## 1. Summary

- Main problem: the address in the structured data is wrong. It differs from the address on the site and in the Google profile.
- Headings: the home page and 15 of 17 pages have no H1.
- Price: one treatment price, 99 EUR. Other fees are listed as well.
- Health: the site names some conditions and uses a few effect claims. One neutral "Werberecht" row is below.
- Competitor page metrics: blocked. Agent A has no competitor URLs yet.

## 2. Technical checks

| Check | Result | Evidence |
|---|---|---|
| http to https | OK. `http://lenafistler.de/` and `http://www.lenafistler.de/` both end on `https://www.lenafistler.de/`. | `site.json` (`http_redirects_to_https: true`), curl -L |
| Server speed | TTFB 0.81 to 0.87 s on 3 runs. Acceptable. | `site.json` (`ttfb_secs`) |
| Sitemap | 17 URLs. All 17 measured. | `site.json` (`sitemap_urls: 17`), `site-pages.json` |
| Duplicate pages (same title and word count) | None. | `site.json` (`duplicate_pages: []`) |
| `href="tel:` on home | 1 link, `tel:+4915565365753`. | curl, `site.json` |
| `href="tel:` on contact page | **0.** The phone number is plain text on the contact page. A visitor on a phone cannot tap it there. | curl of `/informationen/kontakt/` |
| Contact form | On the contact page: 1 form, 2 text fields, 1 checkbox (privacy wording), submit button. Not on the home page. | `site.json` (`form_on_contact: true`, `form_on_home: false`), curl |
| Booking | Two "Termin buchen" buttons on the home page. Both link to `https://zeeg.me/lenafistler`. | curl, home HTML |
| Dead internal links from home | One real defect: `href="${findUrl}"` returns 400. A template placeholder is left in the HTML. Probably a hidden widget. Check it. Other hits: `/wp-json/` and `/wp-json/wp/v2/pages/494` return 403 (blocked on purpose). `/xmlrpc.php?rsd` returns 404. | `site.json` (`dead_links_from_home`) |
| Analytics tags | No GA4 ID and no GTM ID in the HTML. The cookie banner lists "IONOS SiteAnalytics" as an analytics service. A tag that loads after consent cannot be seen with curl. Martin must check the analytics set-up in the account. | `site.json` (`ga4: []`, `gtm: []`), curl, home HTML |
| Google Maps | Cookie banner lists "Google Maps" as a service. | home HTML (consent config) |

## 3. Headings and metadata

| Check | Result | Evidence |
|---|---|---|
| H1 on home | **No H1.** The only heading tag is one H2, "Hin zu Balance und Aufrichtung". | curl of home (`<h1` count 0), `site.json` (`home_h1: []`) |
| H1 on all pages | **15 of 17 pages have no H1.** The two with an H1 are the legal pages (Datenschutz, Impressum). Checked by curl on the service pages too: 0 H1. | `site-pages.json` (`pages_no_h1: 15`), curl |
| Two H1 on one page | None. | `site.json` (`pages_two_h1: 0`) |
| Home title | "Balance & Aufrichtung: Ganzheitliche Körpertherapie München", 60 characters. Has the city. | curl, `<title>` tag |
| Home meta description | 114 characters. "Begleitung bei Rückenschmerzen und Stress. Ganzheitliche Körpertherapie mit Heilpraktiker Lena Fistler in München." | curl, meta tag |
| Price page title | "Behandlungskosten", 17 characters. No city and no service keyword. | curl, `<title>` tag |
| Other titles | Stress page 42 characters. Contact page 51 characters. Therapy overview 50 characters. | curl, `<title>` tags |
| Word counts (page_metrics) | Home 253. Price page 395. "Über mich" 594. Service pages 243 to 335. The counts include menu and footer text. | `site-pages.json` |
| Structured data | One JSON-LD block of type LocalBusiness, on the home page and 13 more pages. See section 4. | `site-schema-localbusiness.txt` |

## 4. Address conflict (structured data)

| Source | Address shown |
|---|---|
| JSON-LD LocalBusiness, on 14 pages | streetAddress "Augustenstraße 79 RG", München |
| Visible address on the contact, price, and service pages | Nymphenburgerstr. 166, 80634 München |
| Impressum | Nymphenburgerstr. 166, 80634 München |
| Google profile (intake) | Nymphenburger Str. 166, 80634 München |

Other faults in the same block:
- No `name` field.
- `sameAs` holds 6 empty strings and 1 Instagram URL.
- `url` is `https://lenafistler.de` (no www). The canonical URL uses www.

Evidence: `site-schema-localbusiness.txt`, curl of 14 pages (grep count of "Augustenstra" is 14).

## 5. Price page

Source: `https://www.lenafistler.de/informationen/behandlungskosten/`. Full text: `site-price-page.txt`.

| Service | Price | Note on the page |
|---|---|---|
| Termin (55 min, incl. 5 min rest) | 99 EUR | The page says "Der Termin". It does not name a service. Basis: GebüH. |
| Consultation by e-mail | 20 EUR per request | Very long requests can cost more. Appointment booking and follow-up questions are free. |
| Consultation by phone or Zoom | 25 EUR per started quarter hour | Only after a first personal contact. |
| Missed appointment | Full fee | Cancel at least 24 hours before. |

Calculator input: 99 EUR per treatment session (55 min). No other treatment price is listed.

## 6. Werberecht row (health branch)

Quotes are in `site-health-quotes.txt`. Neutral note only. No claim of illegality.

- Named conditions on the site: chronic back pain, stress, Burnout, Tinnitus, Angst und Panik, Herzrasen, Bruxismus, Skoliose.
- Effect wording: "Dein Nervensystem und Dein Rücken können ins Gleichgewicht kommen." (home)
- Correction goal: "Die Intention ist es, die Wirbelsäule dreidimensional zu korrigieren." (Skoliose page)
- Effect claim: "So kann unter anderem der Blut- und Lymphfluss positiv beeinflusst werden." (taping page)
- Unsourced statistic: "Die Zahl der Menschen in Deutschland, die darunter leiden, nimmt immer mehr zu." (Stress page)
- Positive: 7 treatment pages say that some methods are not recognised by evidence-based medicine. The home page does not say this.

## 7. Competitor page metrics (sub-step 5): blocked

- `page_metrics.py` was not run. No competitor URL list exists.
- `demand.md` (agent A) has status failed: DataForSEO task 40207, IP not whitelisted. Competitor provider URLs are "not retrieved".
- When the list exists, run: `python3 content-pool-skill/scripts/page_metrics.py --out prospects/lena-fistler/evidence/comp-pages.json --lang de <competitor URLs>`.
- Then add the mean word count and each competitor heading here.

## 8. Not checked by agent B

- Mobile rendering: agent G (`mobile_check`, operator job).
- Desktop look: agent C (`home-today-1440.jpg`).
- Images: agent C.
