# Audit: physiotherapieoberhausen.com (public, read-only)

Context: sister site physiotherapiekraft.de was hacked (fake "Verify you are human" / ClickFix pattern). This check looks only at the public pages of physiotherapieoberhausen.com. No login, no form submits, no changes made.

## Verdict

**Signs of compromise: no** (based on the public pages checked below).

No fake captcha / "verify you are human" prompts, no injected scripts, no unexpected redirects, no spam content, and no unknown external script hosts were found on any checked page. One notable oddity is flagged below (TikTok link target) — it is not evidence of a hack on *this* site, but it does create a path from this site to the already-hacked sister brand's social account.

Caveat: WebFetch reads the page as rendered text/markdown through a model, it does not show raw HTML/JS or test with multiple user agents. Cloaked injections that only fire for Googlebot, for a specific referrer, or on a second visit (a common ClickFix/SEO-spam trick) would not be visible this way. A real scan (Search Console "URL inspection" with "view crawled page", Sucuri/VirusTotal site check, or a server-side file diff/malware scan) is still needed to fully rule this out — this audit only covers what a normal visitor sees.

## Findings table

| Page | Finding | Severity | Evidence |
|---|---|---|---|
| Homepage (`/`) | No fake "verify you are human" / captcha text found | Info (clean) | Full body text reviewed, none present |
| Homepage, Kontakt, Profil, Leistungen, Impressum, Blog, Datenschutz | No injected `<script>`/iframe to unknown third-party hosts detected | Info (clean) | Only expected refs seen: Facebook, Instagram, TikTok, Pinterest, Tumblr, IONOS WebAnalytics (ionos.de), e-recht24.de, medmix.at (one blog source cite), stocksy.com (one stock-photo credit), wp-content/uploads (own WordPress media) |
| Homepage, Kontakt, Profil, Leistungen, Impressum, Blog, Datenschutz | No gambling/pharma/foreign-language spam content detected | Info (clean) | All visible body text is physiotherapy-related German content |
| robots.txt | Clean, no spam paths | Info (clean) | `User-agent: *`, no Disallow, `Sitemap: https://physiotherapieoberhausen.com/sitemap_index.xml`, Yoast SEO markers |
| sitemap_index.xml | Only one sub-sitemap, page-sitemap.xml, no foreign/odd URLs | Info (clean) | — |
| Homepage / Impressum / Profil | **TikTok footer link points to `@physiotherapie_kraft`** (the hacked sister brand's TikTok handle), not an own-brand handle | Medium — worth checking | Quote: footer social links list "TikTok: tiktok.com/@physiotherapie_kraft" on homepage, repeated on Impressum and Profil |
| Homepage / Impressum / Profil | Instagram footer link points to `@alovedan_muenster`, an account name unrelated to either physio brand | Low — worth checking | Quote: footer social links list "Instagram: instagram.com/alovedan_muenster/" |
| Homepage, most subpages | No `<meta description>` detected on any page checked | Low (SEO gap, not security) | Checked homepage, Kontakt, Profil, Leistungen, Blog — none returned a visible meta description |

## SEO notes

- Title tags: present and reasonable length on subpages (Kontakt page title was not visible in the fetch, worth a manual check). Example: "Physiotherapie Leistungen Oberhausen – Physio Anatomie" (Leistungen page).
- Meta descriptions: not visible on any page checked — `[fehlt: meta description content, if any exists in page source it was not returned by the fetch]`. Recommend a manual view-source check or Search Console check to confirm whether these are actually missing or just not rendered to the fetch tool.
- H1: one clear, keyword-relevant H1 per page, consistent with "Physiotherapie Oberhausen" positioning.
- robots.txt + sitemap: correctly configured (Yoast SEO), no crawl blocks.
- Broken links: none found on the pages visited (nav links, footer links, social links, Impressum, Datenschutz all resolved in the fetch). A full broken-link crawl of every blog post was not done — only the blog index page was checked.
- Blog: only one post title was visible on the blog index at fetch time ("Das Schmerzgedächtnis im zentralen Nervensystem …"), no publish date shown — `[fehlt: publish date, additional post count]`.

## What was NOT checked (scope limits per the task brief)

- No login to WordPress admin, hosting panel, or DNS — that is the Kamil chat's server-side cleanup track.
- No raw HTML/JS source diffing, no malware scanner (Sucuri/VirusTotal), no check from multiple user agents or geographies — a cloaked injection would not be visible to this method.
- No full link crawl of every blog post.
