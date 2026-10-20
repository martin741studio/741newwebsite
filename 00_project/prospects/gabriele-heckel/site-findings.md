# Site findings: gabriele-heckel (agent B)

Date: 2026-10-15. Site: https://www.heilpraxis-heckel.de/. Status: done, one sub-step blocked (step 5). Cost: 0.00 USD (no paid calls).

## Summary

The site runs on WordPress. The home page answers in about 1.1 seconds (time to first byte). The phone number is not a clickable link. The contact form exists on /kontakt only. Prices sit on several pages, and two price pairs conflict. Several pages make health claims. The sitemap lists 28 old event pages. No meta descriptions and no structured data exist.

## Step 1: Site collection

Run: collect_site.py, complete. 30 pages measured. Result file: evidence/site.json.

- Home status: 200.
- Time to first byte: 1.10 s on average (1.06 s to 1.11 s, three runs).
- Sitemap: 54 URLs.
- Duplicate pages by the rule (same title and word count): none.
- Dead link from the home page: /xmlrpc.php (405). This is the WordPress default endpoint, not a broken page.
- Pages with two H1 tags: 11. Page with no H1: /elpi-freebie/.

## Step 2: curl checks

Full output: evidence/curl-checks-2026-10-15.txt.

- Telephone links: none. The number "Telefon(+49) 09622 – 70 31 90" is plain text on the home page and on /kontakt/.
- HTTP to HTTPS: works. Both http:// and the non-www domain redirect with 301.
- Internal http:// links: three on the home page, to /psychotherapie/, /heilsame-beruehrungen/ and /coaching-fuer-mehr-lebensenergie/. They redirect, but they should use https://.
- Mixed content: the images on /psychotherapie/ and /heilsame-beruehrungen/ load over http://.
- Contact form: on /kontakt/ only. It has Name, E-Mail (both required) and Nachricht. No phone field.
- Home page: has a search form only.

## Step 3: Prices (for the calculator)

Full list with exact quotes: evidence/site-prices-claims-2026-10-15.md, section A.

- Introductory talk: 45 minutes for 35 € (home, /psychotherapie/, /coaching-fuer-mehr-lebensenergie/).
- Psychotherapy: 60 minutes for 70 € (/psychotherapie/).
- Energy coaching: 6 sessions for 540 € over three months (/coaching-fuer-mehr-lebensenergie/).
- Energy coaching: 1 hour for 60 € (/energiecoaching/).
- Naturcoaching: 60 € per hour (/naturcoaching/).

Two conflicts need a decision from Martin before the calculator uses them:

1. 60-minute session: 70 € on /psychotherapie/, but 60 € on /therapie-und-beratungsgespraeche/.
2. Energy coaching: 60 € per hour on /energiecoaching/, and 540 € for 6 sessions on /coaching-fuer-mehr-lebensenergie/. The site does not say how these relate.

## Step 4: Werberecht row

Werberecht: several sentences name conditions or describe healing-type effects. Examples: "Ängste", "depressive Stimmungen", "Erschöpfungszuständen", "Burn-Out", "heilendes Energiemuster", "Selbstheilungskräfte". The list is in evidence/site-prices-claims-2026-10-15.md, section B. This row is a review input. It is not a legal finding.

Two of the strongest examples sit on pages that the home page does not link: /energiecoaching/ and /therapie-und-beratungsgespraeche/.

## Step 5: Competitor page metrics (blocked)

page_metrics.py was not run. Reason: demand.md (agent A) has status failed. DataForSEO returned "IP not whitelisted". demand.md lists no competitor URLs. Unblock: whitelist the IP in DataForSEO, rerun agent A, then rerun step 5.

## Other findings

Metadata and structure:
- No meta description on any of the 30 measured pages.
- No JSON-LD structured data on any measured page.
- Home H1 is "Herzlich willkommen!". It names no person, service or city.
- /psychotherapie/ H1 is "Psychotherapie". It names no city.
- /leistungen/ has 5 words, a heading only. The menu item "Leistungen" is a dropdown parent with href="#".
- /kontakt/ has 40 words.
- Canonical tags exist on the main pages.

Pages and sitemap:
- 28 of the 54 sitemap URLs are /Veranstaltung/ event pages. The home page shows no upcoming events.
- Titles repeat. "Naturspaziergang" appears on 3 pages (62, 61 and 57 words). "Mit einem Naturspaziergang die Lebensenergie wecken" appears on 2 pages (119 and 124 words).
- The sitemap has a typo slug next to the correct one: /Veranstaltung/seminar-fuer-gesundheit-udn-lebensenergie/.
- Six service pages are not linked from the pages checked. They appear in the sitemap only: /energiecoaching/, /therapie-und-beratungsgespraeche/, /herzenskommunikation/, /naturcoaching/, /gesundheitscoaching/, /therapieplatz-ueberbrueckung/.
- Overlap: /energiecoaching/ (153 words) and /coaching-fuer-mehr-lebensenergie/ (275 words) cover energy coaching.

Tracking and third parties:
- No Google Analytics 4 ID and no Google Tag Manager ID in the static HTML.
- No cookie or consent banner code in the static HTML. The 1440 px home screenshot shows no banner.
- Jetpack Stats loads on the home page and on /psychotherapie/ (stats.wp.com).
- This check reads static HTML only. Tags added by JavaScript would not show.

Form of address and copy:
- "Sie" is used on all pages except /vita/. The Vita page uses "du" throughout (14 du-forms, 0 Sie-forms).
- The form success text says "Vielen Dank für deine Antwort. ✨" (du).
- Typos: "zusammen mit mit gehen" (/psychotherapie/ and /coaching-fuer-mehr-lebensenergie/); "Als Heilpraktikern für Psychotherapie" (/vita/); a stray "?" in "gefordert.?Ich vergebe" (/meine-kunden-ueber-mich/).
- Lowercase formal pronouns: "für ihren Lebensweg" and "mit Freude ihr Leben" (home); "Ihr Körper und ihre Seele" (/heilsame-beruehrungen/).
- No use of "Psychotherapeut/in" as a title found. The site uses "Heilpraktikerin für Psychotherapie und Coach".

Name, address and phone (NAP):
- Phone on the site matches the Google profile: 09622 70 31 90 (+49 9622 703190).
- Street spelling differs: the site uses "Strasse", the Google profile uses "Straße".
- The fax number on /kontakt/ uses area code 03222, not 09622 as the phone does. Check whether it is still in use.

At 1440 px, the home page shows the menu and a hero photo above the fold. No phone number and no call to action appear in the first screen. Evidence: evidence/home-today-1440.jpg.

## Blockers

1. Step 5 (competitor page metrics) is blocked. See Step 5.
2. Shared scratchpad: other agents write files with generic names (for example home.html) to the same folder. Two of my fetched files were overwritten during the run. I used a private folder for later checks. The evidence files in this folder are not affected.

## Evidence files

- evidence/site.json
- evidence/site-pages.json
- evidence/site-urls.json
- evidence/site-page-urls.txt
- evidence/site-menu-2026-10-15.txt
- evidence/curl-checks-2026-10-15.txt
- evidence/site-prices-claims-2026-10-15.md
- evidence/home-today-1440.jpg
