# Site findings: StressFrey-Akademie (agent B, 2026-10-15)

Website: https://stressfrey.de/
Method: live HTML fetched with curl. Read only. No Chrome. No deploy. No messages sent. No paid API call (cost 0 USD, 0 credits).

## Status

- Step 1 (collect_site.py): done. Output: `evidence/site.json`, `evidence/site-pages.json`, `evidence/site-urls.json`, `evidence/site-page-urls.txt`.
- Step 2 (curl checks): done. Output: `evidence/site-curl-checks.txt`.
- Step 3 (price page): done. The shop page lists two prices. No coaching price is on the site.
- Step 4 (health claims): skipped. The brief says this prospect is not a health practice.
- Step 5 (competitor page metrics): blocked. `demand.md` has no competitor URLs. DataForSEO returns error 40207 (IP not whitelisted). No competitor run was made.

## Findings

Priority: H = fix before the review page, M = should fix, L = note only.

| No. | Finding | Priority | Evidence |
|---|---|---|---|
| 1 | No clickable phone number on any of the 11 pages checked. The number is plain text: +49 (0)221 6086438. | H | `site-curl-checks.txt` (tel column), `site.json` (`tel_links_home`, `tel_links_contact`) |
| 2 | The first main menu item "Willkommen" links to `https://stressfrey.de/?page_id=4510`. That URL returns 404. The link is in the menu of 8 of 11 pages. | H | `site-curl-checks.txt` (menu check), `site.json` (`dead_links_from_home`) |
| 3 | The home page has no H1. The hero headline is an H2. Five pages checked have no H1: home, /shop/, /selbstbestimmt/, /vortraege/, /gesund-im-stress-blog/. | H | `site-curl-checks.txt` (per page), `site-visible-text.txt` |
| 4 | The home title is "StressFrey.de - StressFrey-Akademie" (35 characters). It names no service and no city. | H | `site-curl-checks.txt`, `site.json` (`home_title`) |
| 5 | The home meta description has 359 characters. It repeats the hero text. Search results cut long descriptions. | M | `site-curl-checks.txt` |
| 6 | "Köln" appears once in the visible home text, in the footer ("Markus Frey, Köln"). No service and city pair appears on the home page. | H | `site-visible-text.txt` (home) |
| 7 | Three brand forms appear: "StressFrey.de" (home title), "StressFrey-Akademie" (page titles), "Stressfrey Institut" (footer). The footer shows "Copyright 2017" on most pages. /selbstbestimmt/ shows "©Markus Frey, 2026". | M | `site-visible-text.txt`, `site-curl-checks.txt` |
| 8 | The home page has two offers with two targets. "Kostenloses E-Book sichern!" goes to /selbstbestimmt/. "Kostenloses Kennenlern-Coaching sichern!" goes to /termin/. | H | `site-visible-text.txt`, `site-curl-checks.txt` (booking section) |
| 9 | /termin/ has no text about the free call. The visible text is the title "Termin", the "Über mich" block and an iframe from etermin.net. | H | `site-curl-checks.txt` (booking section), `site-visible-text.txt` (termin) |
| 10 | The home page has no contact form. Its two forms are search forms. The contact form exists only on /kontakt/ (Contact Form 7: name, email, subject, message, consent). | M | `site.json` (`form_on_home`, `form_on_contact`), `site-curl-checks.txt` |
| 11 | The shop page lists two prices: "Den Stress im Griff" 21,80 EUR and "Mit Stress zu Spitzenleistung" 49,90 EUR. The coaching has no price on the site. | L | `site-curl-checks.txt` (price section), `site-visible-text.txt` (shop) |
| 12 | The sidebar on /kontakt/ shows theme leftover categories: Jacket, Mens, Scarfs, Shirts, Womens, Unkategorisiert. They do not fit the business. | L | `site-visible-text.txt` (kontakt) |
| 13 | The portrait on the home page has no alt text. The logo has alt text. | M | `site-curl-checks.txt` (per page, alt column), `site.json` (`images_home`) |
| 14 | The home page has one JSON-LD block with the types WebPage, ImageObject, BreadcrumbList and WebSite. It has no Organization, Person or LocalBusiness type. | M | `site-curl-checks.txt` (JSON-LD line), `site.json` (`jsonld_blocks`) |
| 15 | The home HTML has a Meta Pixel (id 1268688827965746). It has no GA4 id and no GTM id in the static HTML. A Cookiebot setup is present. Not checked in a browser. | L | `site-curl-checks.txt` (tracking section) |
| 16 | The sitemap lists 882 URLs. 291 are tag archives, 21 are category archives and 1 is an author archive. About 152 are child paths, such as attachment pages. | M | `site-urls.json` (count 882) |
| 17 | The site sends a server response in 2.07 to 2.29 seconds (3 runs). | M | `site.json` (`ttfb_secs`) |
| 18 | The blog sample has 29 posts. Mean length 691 words, median 636 words, range 220 to 1455 words. Titles and word counts are unique. No duplicate page pair was found. | L | `site-pages.json`, `site.json` (`duplicate_pages`: none) |
| 19 | The old offer post "Kölsches Sonderangebot am 11.11.11" is still live. It has 282 words and is in the sitemap. | L | `site-pages.json` |
| 20 | The http and www versions redirect to https with a 301. The page sets lang="de" and a viewport. | L | `site-curl-checks.txt` (redirects), `site.json` (`http_redirects_to_https`) |
| 21 | Form of address: the site uses "Sie" on all pages checked. | L | `intake.md` (18 "Sie" forms, 0 "du" forms) |

## Notes for the review page

- The top three gaps are findings 1, 2 and 9.
- The home page has no city and no service in the title or H1 (4, 6). The gap keyword work needs this context.
- Length of the prospect's own pages: the 29 blog posts average 691 words. This is the baseline. The competitor comparison (step 5) is still open.

## Blockers

- Step 5 (competitor page metrics) is blocked. `demand.md` has no competitor URLs. Cause: DataForSEO error 40207, IP 179.65.207.101 not whitelisted. This is an account setting and needs Martin. Agent A and the orchestrator own the fix.
