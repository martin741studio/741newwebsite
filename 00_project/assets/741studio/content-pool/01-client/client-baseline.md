# Client baseline: 741.Studio (own run)

Date: 2026-10-11. Mode: existing site (`741.studio`, static pages built with Vite and Handlebars, 116 pages checked live). Compliance mode: none. Own rules apply (section 3). Health examples on the site follow the HWG rules.
Rule: facts only. Every fact has a source. A gap carries `[FEHLT]`.
Sources reused (not collected again): the 741.studio audit of 2026-10-11 (`01-client/audit-reused/`: `findings.json`, `keywords.json`, `gbp-read-2026-10-11.json`, `ga4-read-2026-10-11.json`, `gsc-url-inspection-2026-10-11.json`). Field ids like B06.03 point to `findings.json`. Memory notes on pricing and design system.

## 1. Services (ground truth for the fit test)

Source: site navigation and pages (crawl 2026-10-11).

| Key | Service | Pages |
| --- | --- | --- |
| localseo | Local SEO and Google Maps ranking (90-day programme) | `/pages/local-seo.html`, `/de/pages/local-seo.html` |
| gbp | Google Business Profile optimisation and reviews | inside the Local SEO pages |
| webdesign | Website design and development | `/pages/website-design.html`, `/de/pages/website-design.html` |
| googleads | Google Ads management | `/pages/google-ads-1.html`, `-2`, `-3` and the DE copies |
| metaads | Meta Ads management | `/pages/meta-ads-1.html`, `-2` and the DE copies |
| audit | Free visibility audit | `/pages/visibility-audit.html`, `/pages/sichtbarkeits-analyse.html`, `/de/pages/google-maps-fix.html` (all noindex) |
| growth | Growth subscription (keep and extend rankings) | `/de/pages/wachstums-abo.html`, `/pages/wachstums-abo-de.html` (noindex) |
| grant | Visibility grant (Sichtbarkeits-Förderung) | `/pages/visibility-grant.html`, `/de/pages/sichtbarkeits-foerderung.html` (noindex). The terms are not reviewed. |
| circle | 741 Circle community (free, invite only) | `/pages/741-circle.html`, `/de/pages/741-circle.html` |
| bali | Local SEO and web design for businesses in Bali | `/pages/bali-local-seo.html`, `/pages/bali-web-design.html` (noindex) |

Three packages exist (foundation setup, 90-day programme with the only guarantee, power engine plus ads). The numbers stay out of public pages and out of messages (Martin's rule: numbers only in the call).
**Not proven as services:** WhatsApp and n8n automation, review removal, social media management, e-commerce (blog posts or the profile description only). They become adjacent items.
**Off-topic content on the site:** posts on VPNs, photo metadata, secure data wiping, a serverless digital life, the right to be forgotten.

## 2. Markets, places, audience

- Two markets (B04.01): expat and foreign-run businesses in Bali (Canggu, Uluwatu, Seminyak, Ubud), in English; German-speaking practices, clinics and law firms (DACH), in German.
- The Google profile is a service-area business without a public address. Posts name bases in Berlin and Bali (B05.02). `[FEHLT]` Is Berlin a base?
- GA4 over 28 days to 10 October: 197 sessions; Organic Social 106, Direct 81, Organic Search 8. Indonesia 93 (the own team), Germany 61, Austria 4, Switzerland 3 (B01.01).
- Bali references with naming rights open: a beach bar, a gym, a Greek restaurant built with a partner agency, a booking platform, a F&B chain. Use only what Martin confirms.

## 3. Brand and own rules

- Name: "741.Studio". The name is ambiguous in search (autocomplete shows other businesses, B07.04). The Google profile name is "741 Studio Marketing" (B13.03).
- Rules: no tool names, no team names, no method sources in client material; no invented numbers; changes only after Martin's go (B08.03). A guarantee only for the 90-day package. No success promise without proof next to the claim (B13.05).
- Booking: cal.com (German and English calendars) and WhatsApp. No form on the home page (B06.02).

## 4. Proof (authority)

| Proof | Status | Source |
| --- | --- | --- |
| Google 4.5 stars, 17 reviews | newest 3 weeks old, no owner reply | B05.03, B05.04 |
| Seven case-study pages (Lengauer Vienna, Laserstein Freiburg, Abel, Schlirf) | one page carries noindex | page crawl |
| LinkedIn as the strongest channel | 106 of 197 sessions | B07.03 |
| Directory listings | not checked | B07.02 |
| Backlinks | not read (no purchase in the audit) | B07.01 |

## 5. Own site (measured 2026-10-11)

- 116 pages, all HTTP 200. The sitemap lists 5 URLs and no sitemap is submitted in Search Console (B01.03). 20 pages carry noindex (legal pages, private previews, the Bali pages, the audit pages, the grant pages, one case study). 38 pages have no canonical link.
- Home page: 787 words, three H1, title "741.Studio | Architecting Digital Growth & Local SEO Automation...". German home page: 741 words. No JSON-LD on the start and service pages (B06.03).
- Blog: many English posts of about 360 to 600 words with the same title pattern ("Best ... Bali", "... Bali"). A German-path copy exists for most. Most /de/ blog copies are English text.
- Own rankings (DataForSEO, 2026-10-11): two keywords with volume, both unrelated ("747 studios").
- Indexing: 12 of 16 sampled URLs indexed; the Bali pages and the web design service page are unknown to Google (B06.06).

## 6. Search Console

The 741 service account reads the property `https://741.studio/` (`https://www.` and `sc-domain:` return 403). Export of 2026-10-11 for 2026-07-11 to 2026-10-09: 59 queries (32 clicks, 798 impressions) and 27 pages (57 clicks, 1,958 impressions). Files: `03-demand/gsc-api.json`, `gsc-queries-90d.tsv`, `gsc-pages-90d.tsv`. The base is small: read patterns, not single numbers.

## 7. [FEHLT] list (decisions for Martin, no client form)

1. Cost page: no numbers, a "from" hint, or a range?
2. Is the law-firm vertical a goal, and may the Stürzl case be named?
3. Automation, review removal, social media, e-commerce: offered or not?
4. Off-topic posts and the near-identical Bali posts: keep, merge, noindex or remove?
5. Visibility grant: when are the terms reviewed?
6. Is Berlin a base?
7. Which noindex pages should be indexed (Bali pages, audit pages)?
8. Naming rights per Bali reference.
