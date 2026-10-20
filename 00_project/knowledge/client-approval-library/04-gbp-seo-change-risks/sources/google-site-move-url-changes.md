# Site moves with URL changes (Google Search Central)

- URL: https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes
- Type: Google official documentation (living page), last updated 2026-08-20
- Fetch date: 2026-10-13

## Key points

- The guide covers all URL changes: domain changes, HTTP to HTTPS and path or slug changes.
- Change one thing at a time. Plan the change for a low-traffic period.
- Build a full list of old URLs (sitemaps, analytics, logs, Search Console, CMS). Map every old URL to one new URL.
- Use server-side permanent redirects (301 or 308). Redirect straight to the final URL. Avoid chains.
- Do not send many old URLs to an unrelated page such as the homepage. Merging several old pages into one relevant new page is fine.
- Return 404 or 410 only for content that is really gone.
- Update internal links, canonicals, hreflang and the sitemap to the new URLs.
- Keep redirects for at least one year. Google suggests keeping them for good.
- Rankings fluctuate during a move. This is normal. Medium sites need a few weeks or more.
- Common mistakes: noindex or robots.txt blocks left in place, redirects to URLs that do not exist, crawl error spikes that nobody checks, old sitemaps.

## Relevance for 741

- A slug change on a ranking page is a high-risk edit. The client may change wording, but not the URL, without agency work.
- Every URL change needs a redirect map, a test and a monitoring window of several weeks.
- Removing a page without a redirect to a relevant page loses its signals. Homepage redirects are not a safe default.
