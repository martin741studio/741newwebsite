# Public check: physiotherapieoberhausen.com — after the physiotherapiekraft.de hack

**Date checked:** 2026-10-14
**Method:** Public, read-only web fetch (WebFetch/WebSearch). No login, no cleanup, no changes made.
**Checked for:** the same signs seen on physiotherapiekraft.de — injected spam links, odd redirects, suspicious footer content, hidden/injected sitemap or blog entries, cloaked search-index spam.

## Result: CLEAN

No signs of the physiotherapiekraft.de-style spam injection were found on physiotherapieoberhausen.com at the time of this check.

## What was checked

| Check | Page/URL | Result |
|---|---|---|
| Homepage content + links | https://physiotherapieoberhausen.com/ | All links point to own pages, tel/fax/mailto, and the practice's own Facebook profile. No foreign/unrelated links. |
| robots.txt | https://physiotherapieoberhausen.com/robots.txt | Standard Yoast SEO output, `Disallow:` empty, points to own sitemap_index.xml. No injected rules. |
| Sitemap index | https://physiotherapieoberhausen.com/sitemap.xml | Points to one `page-sitemap.xml`. No extra/unknown sitemap files (a common sign of injected spam pages). |
| Page sitemap (full URL list) | https://physiotherapieoberhausen.com/page-sitemap.xml | 7 URLs total: home, profil, blog, impressum, datenschutz, kontakt, leistungen. All match the visible site navigation — no hidden pages. |
| Blog page | https://physiotherapieoberhausen.com/blog/ | 2 articles, both about physiotherapy ("Schmerzgedächtnis"). One external reference link to medmix.at (a medical content site), consistent with the article topic. No spam links or titles. |
| Impressum (footer/legal page) | https://physiotherapieoberhausen.com/impressum/ | Footer text and links are standard (address, phone, fax, email, Impressum, Datenschutz, Facebook, e-recht24.de for the legal template). No hidden text, no gambling/pharma/essay-writing keywords. |
| Google index check | `site:physiotherapieoberhausen.com` (web search) | Only the site's own 6 pages show up (home, profil, leistungen, kontakt, blog, impressum). No spam page titles in the search index (cloaked spam often shows up here even when the page looks clean to a visitor). |
| Redirects | All of the above | No page redirected to a different domain or an unexpected URL. |
| Prompt-injection check | All fetched pages | None of the fetched content contained instructions directed at an AI assistant. |

## What this does NOT rule out
- This was a public, outside-in check only. It cannot see the WordPress admin, file system, database, or plugin list — a hack can exist server-side (e.g. a malicious plugin, a cron job, a cloaked response only shown to Googlebot's user-agent) without changing what a normal visitor or a generic fetch sees.
- [fehlt: no login/admin access was used, so plugin list, file integrity, and user accounts were not checked — would need Novamira/WP-CLI access to confirm fully.]
- [fehlt: no malware-scanner (e.g. Sucuri, VirusTotal URL check) was run — only manual content/link/sitemap review.]

## Recommendation
Given physiotherapiekraft.de (same owner, shared GA4 property) was hit, it is worth a real backend check of physiotherapieoberhausen.com too (WP-CLI/Novamira plugin + file scan), even though the public surface looks clean today — injections are sometimes cloaked from normal visitors and crawlers that don't spoof Googlebot's user-agent.
