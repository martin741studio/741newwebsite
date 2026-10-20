# Site findings: CONTIQ Rechtsanwaltsgesellschaft mbH (contiq.de)

Agent B (site), 2026-10-15. Branch: legal. Read only. No Chrome, no deploy, no messages.
Firm framing: a multi-partner firm. These findings describe the firm site, not Stephan Brenner alone.

## Summary

- HTTPS works. HTTP reaches HTTPS in one redirect.
- The site has no click-to-call. None of the 7 pages checked has a tel: link.
- The site has no contact form on the pages checked. Contact runs by phone text and email link.
- Gesellschaftsrecht has no own page. It is one section on /unsere-expertise/.
- The home H1 and title name no service and no city.
- The site has no price list. Pricing data for a calculator is not available.

## 1. Technical checks

| Check | Result | Evidence |
| --- | --- | --- |
| Home status | 200 | evidence/site.json |
| HTTP to HTTPS | 301, one hop | evidence/site.json (http_redirects_to_https) |
| Server response time (3 runs) | 1.70 s, 1.73 s, 1.71 s | evidence/site.json (ttfb_secs) |
| tel: links on the 7 pages checked | 0 | evidence/site-checks.md |
| Contact form on home | none | evidence/site.json (form_on_home) |
| Contact form on contact page | none | evidence/site.json (form_on_contact) |
| Broken tel: links | 0 | evidence/site.json (pages_with_broken_tel) |
| Dead internal links from home (18 checked) | 0 | evidence/site.json (dead_links_from_home) |
| Sitemap | /sitemap.xml, 17 URLs, all measured | evidence/site.json, evidence/site-pages.json |
| H1 per page | one on every page (0 pages with two or none) | evidence/site.json |
| Duplicate pages (same title and word count) | none | evidence/site.json (duplicate_pages) |
| /kontakt/ | 301 to home, no own page | evidence/site-checks.md |
| GA4 or GTM id in static HTML | none found | evidence/site.json (ga4, gtm) |
| Structured data | Yoast: WebPage, WebSite, Organization | evidence/site.json (jsonld_blocks) |

Structured data gap: the Organization block has name, URL, logo and image only. It has no address, phone or legal service type.

## 2. Price page

No price page. No visible fee, price or "€" on the home, service, contact or profile pages. Calculator input from the site: none.

## 3. Health branch

Skipped. This is a law firm.

Light check, law firm: no "Fachanwalt" title found on the 4 pages grepped. One comparative phrase on the home page: "führenden Wirtschaftskanzleien". It describes earlier employers, not the firm.

## 4. Page structure and links

- The firm lists 8 practice areas on one page: /unsere-expertise/ (760 words). Each area has an anchor link.
- The Gesellschaftsrecht section on that page is about 160 words (approximate).
- The home page links to the same anchors. No dedicated area page and no city page exist.
- The sitemap lists 7 German lawyer profile pages, plus English copies. German word counts run from 166 to 475.
- One "Mehr" button on the home page links to a Wix Studio address (marizat2.wixstudio.io), not a contiq.de page.
- The home page has 16 "Mehr" buttons. The link text does not name the target.

## 5. Local signals

- Stuttgart appears once on the home page and once on the service page. Both times it is the footer address.
- Home title: "CONTIQ Rechtsanwälte". Home H1: "CONTIQ – die Corporate Boutique". Neither names a service or a city.
- Home meta description: no city and no service.
- Profile meta description (Stephan M. Brenner): "berät Unternehmen und Anteilseigner in Fragen des Handels- und Gesellschaftsrechts". No city.

## 6. Competitor pages (step 5)

Source: evidence/comp-pages.json. URLs from demand.md section 4.

| Page | Words | H1 |
| --- | --- | --- |
| MTR Legal, Gesellschaftsrecht Stuttgart | 1,874 | "Gesellschaftsrecht Rechtsanwalt für Stuttgart" |
| MTR Legal, GmbH-Recht Stuttgart | 3,115 | "Rechtsanwälte für GmbH-Recht für Mandanten aus Stuttgart" |
| HWS, Stuttgart location page (English) | 693 | "HWS RECHTSANWALTSGESELLSCHAFT MBH - BUSINESS-ORIENTED LEGAL ADVICE, IN THE HEART OF STUTTGART." |

Sample H2 headings:

- MTR Gesellschaftsrecht: "Gründung einer Gesellschaft und Entscheidung zur passenden Rechtsform", "Gesellschaftsrechtliche Haftungsfragen", "Unternehmensnachfolge erfolgreich regeln", "M&A - ... in Stuttgart".
- MTR GmbH-Recht: "GmbH gründen ... in Stuttgart", "Unterstützung bei Konflikten im Gesellschaftsrecht", "GmbH verkaufen oder umwandeln", "Handelsregisterangelegenheiten ... in Stuttgart meistern".
- HWS: "Our expertise", "Close to our clients", "Open positions in Stuttgart", "FAQ - Frequently asked questions".

Mean word count of the 3 pages: 1,894 (median 1,874). Two of the 3 pages belong to one firm. Read the mean as a range: 693 to 3,115 words.

What the data shows:

- Both MTR pages name Stuttgart in the H1 and several H2s. The CONTIQ pages do not.
- A dedicated Gesellschaftsrecht page from a competitor is about 1,900 words. CONTIQ gives this area about 160 words on a shared page.
- The gap is topic depth and city signals. Word count alone does not decide it. The prospect's pages can be longer (lesson 4), so do not claim length as the only fix.
- HWS shows that a shorter page with a city H1 and a FAQ block exists. Its rank is not measured here.

## 7. Blockers

None for site work. Search volume and SERP data are missing (demand.md, status PARTIAL, DataForSEO IP not whitelisted). The gap keyword stays provisional until agent A reruns.

## 8. Files

- evidence/site.json, evidence/site-pages.json, evidence/site-urls.json, evidence/site-page-urls.txt (collect_site.py)
- evidence/comp-pages.json (page_metrics, competitor pages)
- evidence/site-checks.md (curl and text checks, this run)
- Cost: 0 USD (free fetches only).
