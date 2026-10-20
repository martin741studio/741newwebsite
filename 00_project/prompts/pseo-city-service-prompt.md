# 741 · Programmatic City × Service Page Generator — Master Prompt

> Paste into Claude (with web access). Replaces the Arvow prompt. Produces genuinely-unique location+service pages for **our Vite/Handlebars + FTP pipeline**.
> Fill the two inputs at top. Run **Phase A once per client**, then **Phase B in batches**.
> Companion strategy: `00_project/programmatic-pages-playbook.md`.

---

```
CLIENT SITE URL: <<PASTE URL>>
OUTPUT LANGUAGE: auto   # auto = match the site's language; or force "de" / "en"

You are a senior local-SEO strategist and an expert at building programmatic
"[service] in [city]" service-area pages that genuinely rank in 2026 — i.e. pages
that survive Google's scaled-content-abuse and doorway-page policies because each
one is genuinely useful and distinct, not a template with one word swapped.

You are producing assets for the 741.Studio pipeline (Vite + Handlebars + FTP).
Reuse our design system, never invent layout: partials {{> header }}/{{> header_de }},
{{> footer }}/{{> footer_de }}, {{> consent }}, weavy.css, and the seo_* classes.
Booking CTA: DE pages → https://cal.com/741-studio-simjzw/30min ,
EN pages → https://calendly.com/martin-233/15-minute-meeting?back=1 .
Detect the site language from the URL's content and write ALL page copy in that
language (OUTPUT LANGUAGE above overrides if not "auto").

Work in phases. Do not skip research. Do not fabricate facts — if a fact isn't on
the site or verifiable, leave it out or mark it TODO. Never invent reviews/ratings.

════════════════════════════════════════════════════════════════════════
PHASE A — RESEARCH & VARIABLES  (run once per client)
════════════════════════════════════════════════════════════════════════

STEP 1 — RESEARCH (before writing anything)
Fetch the homepage + key pages (services, about, a location/area page, contact).
Extract and note:
- Business name, phone, booking/quote/contact URL, address, languages
- Industry + the core service lines they offer
- Cities/towns/region they serve + the region's climate/seasonality
- Trust signals: years in business, licensed/insured/bonded, awards, review count,
  guarantees, financing, 24/7 emergency, memberships
- Brand voice (formal vs casual, "Sie" vs "du", any taglines)

STEP 2 — EXTRACT VARIABLES  → output three JSON blocks exactly in this shape:

business.json
{
  "name": "", "lang": "de|en", "phone": "", "bookingUrl": "",
  "address": "", "usp": "", "voice": "formal-Sie | casual-du | ...",
  "trust": ["<verified trust signals only>"],
  "priceRange": "", "taglines": []
}

services.json   // one entry per real service line
[
  {
    "slug": "local-seo",                    // kebab, language-appropriate
    "name": "Local SEO",
    "h1noun": "Local SEO",                  // as used in "[H1noun] in [City]"
    "synonyms": ["google maps optimierung", "lokale suchmaschinenoptimierung"],
    "intro_angle": "<the one problem this service solves>",
    "process": ["step","step","step"],
    "included": ["deliverable","deliverable"],
    "price_from": "", "timeline": "",
    "service_faqs": ["Q?","Q?"]             // service-level, city-agnostic
  }
]

cities.json     // ONLY cities where the business has a real presence/service radius
[
  {
    "slug": "nuernberg", "name": "Nürnberg", "region": "Mittelfranken/Bayern",
    "districts": ["Altstadt","Langwasser","..."],
    "postal": ["90402","..."],
    "landmarks": ["..."],                   // used sparingly, for local realness
    "neighbours": ["fuerth","erlangen","schwabach"],  // slugs → sibling links
    "population_band": "300k+",
    "local_notes": "<anything locally true that affects the service>",
    "radius_km": 25
  }
]

STEP 3 — DEFINE THE REUSABLE TEMPLATE (once)
Output a single Handlebars-style page template consistent with our design system.
It is the SKELETON only — the unique body text is generated per cell in Phase B.
Requirements the template must satisfy:
- <head>: unique <title> and meta description ("[Service] in [City] | [Business]"),
  self-referencing canonical, one <h1> = "[Service] in [City]", og:*, hreflang if
  a sibling exists in the other language, robots index,follow.
- Reuse {{> header* }}, {{> footer* }}, {{> consent }}, weavy.css, seo_* classes.
- ABOVE THE FOLD (convert here): H1, one-line local promise, trust bar, primary CTA
  (call/book using our booking link) + secondary (quote). Click-to-call phone.
- BELOW THE FOLD (depth): {{unique_body}} slot with sections:
  why locals in [City] choose [Business] · the service done properly (process +
  what's included + timeline) · areas served around [City] (districts + neighbour
  links) · local proof · FAQ (service+city) · final CTA.
- JSON-LD: LocalBusiness (areaServed=city, telephone, priceRange), Service
  (serviceType + areaServed), FAQPage (from the page FAQ), BreadcrumbList.
- Internal links: link up to the service hub, sideways to 3–5 neighbour-city pages
  of the same service, and across to other services in the same city.
- URL/file path: 04_site/[service-slug]-[city-slug]/index.html  (both in the slug).

════════════════════════════════════════════════════════════════════════
PHASE B — GENERATE UNIQUE PAGES  (run in batches; specify which cells)
════════════════════════════════════════════════════════════════════════

Input for this run:  GENERATE = [ (service-slug, city-slug), ... ]   // a batch, e.g. 10

For EACH (service, city) pair, write the {{unique_body}} FRESH from that service's
and that city's data. This is NOT find-and-replace. Hard uniqueness rules:

1. ≥ 40% of the body must be text that could NOT be pasted onto a sibling page
   (city-specific or service-specific). If you can't hit that from the data, output
   "SKIP: thin data for <cell>" instead of a weak page — do not pad.
2. Weave in ≥ 4 local levers from cities.json: named districts, neighbouring towns,
   local seasonality/context, local price band, local timeline, local proof.
3. Rotate STRUCTURE deterministically by a hash of the slug: vary section order,
   H2 wording, and intro angle across a variation set, so no two pages share a
   boilerplate fingerprint.
4. Write 3–5 FAQs UNIQUE to this service+city (never the same FAQ block twice).
5. Match the brand voice exactly (Sie/du, formal/casual).
6. Natural keyword use — "[service] in [city]" in H1, title, first paragraph, once
   or twice more; no stuffing. Add semantic variants/synonyms naturally.
7. No fabricated facts, no fake reviews, no invented certifications.

OUTPUT per cell, ready for the pipeline, as:
--- FILE: 04_site/[service]-[city]/index.html ---
<full HTML using the Phase-A template with {{unique_body}} filled + all schema>

After the batch, output a short QA line per page: word count, % city/service-specific
(estimate), local levers used, and any SKIPs — so we can spot thin cells before deploy.

════════════════════════════════════════════════════════════════════════
DEPLOY (outside the prompt): npm run build && npm run deploy (incremental FTP).
Add all new URLs to the sitemap. Publish in staged batches, not all at once.
Then monitor GSC Coverage + rankings; thicken cells that index-but-don't-rank,
noindex/fix cells Google refuses to index, prune losers after 8–12 weeks.
```

---

## How we run it (our workflow)

1. **Phase A** for the target site (741.studio first). Save the three JSON blocks to
   `04_site/_pseo/<client>/{business,services,cities}.json` and the template to
   `04_site/_pseo/<client>/template.hbs`.
2. **Phase B** in batches of ~10 cells → a `build_pseo_<client>.py` generator (same
   shape as our `build_*` scripts) writes each `04_site/[service]-[city]/index.html`.
3. Wire internal links (service hub → city pages; sibling neighbour links) — reuse the
   internal-linking approach from `00_project/internal-linking-plan.md`.
4. `npm run build` + `npm run deploy`. Verify at 375px + check schema. Stage batches.
5. Track in GSC/GA4 via our reporting API. Expand cities/services once it proves out.

## 741 pilot inputs (starting set)
- **Services:** Local SEO · Google-Maps-Optimierung · Webdesign · Google Ads · Meta Ads
- **Cities (Franken first):** Nürnberg · Fürth · Erlangen · Schwabach · Zirndorf ·
  Bamberg · Würzburg · Regensburg · Ingolstadt
- Start with ~5 services × ~8 cities ≈ 40 pages, prove, then expand.
