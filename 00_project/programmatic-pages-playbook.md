# Programmatic City × Service Pages — 741 Playbook

> State-of-the-art programmatic SEO ("pSEO") for local service-area pages, built on **our own Vite + Handlebars + FTP pipeline** (not Arvow). Runs as a repeatable **agency service per client**, piloted first on **741.studio itself**.
> Companion file: the generator prompt at `00_project/prompts/pseo-city-service-prompt.md`.

---

## 0. The bet (what we're copying, and why it works)

One page per **[service] in [city]**, at scale. The teardown that inspired this: one Texas trade site, ~100 pages (`/frisco-plumbing/`, `/plano-air-conditioning/`…), ~93k monthly visits, 3,800 keywords, **domain rating only 40**. The structure — location + service in the URL, matched to how people actually search — carries almost all the traffic.

**Two truths from it:**
1. **Authority is not the barrier.** DR 40 is nothing special. Every domain starts at zero; backlinks lift it over time. Low DR = reason to start building links, not skip pages.
2. **The barrier is uniqueness.** One template with a single word swapped ("plumbing"→"air conditioning", 99% identical) *stopped ranking years ago*. The pages must be **genuinely different**. That used to be too much manual work — now AI produces distinct pages in minutes. **The gap between "simple" and "easy" is exactly our margin.**

---

## 1. The only thing that matters in 2026: genuine uniqueness

Google's **March 2024 "scaled content abuse"** spam policy and the long-standing **doorway-page** policy both target mass-produced, low-value, near-duplicate pages. Getting this wrong = manual action / deindexing. So uniqueness isn't a nicety, it's survival.

**A page passes only if a human in that city would find it genuinely useful.** Our uniqueness comes from **real local + service specifics**, not spun synonyms:

- **Local reality per city:** districts/Stadtteile, postal codes, landmarks, neighbouring towns, travel/service radius, local seasonality/climate as it affects the service, local regulations/norms, typical local price ranges, local response times.
- **Service depth that varies per service:** process, what's included, timeline, materials/methods, service-specific FAQs.
- **Structural variation:** rotate section order, vary H2 wording and intro angle, vary FAQ sets, so pages don't share a boilerplate fingerprint.
- **Local proof:** real reviews/case refs from that area when they exist; a "we also serve nearby …" block (also internal links).

Rule of thumb: **≥ 40% of each page's body must be city-specific or service-specific text that could not be copy-pasted onto a sibling page.**

---

## 2. Architecture on our stack (mirrors the review-page pipeline)

We already generate data-driven pages (review pages via `PROSPECT_DATA` + a master). Same idea, cross-product instead of one-off.

**Data model** (three layers → the generator does the cross-product):
```
business.json   → name, USP, phone, booking URL (cal.com DE / calendly EN),
                  trust signals, voice, lang ("de"|"en"), schema base
services[]      → { slug, name, h1noun, intro_angle, process[], included[],
                    price_from, timeline, faqs[], synonyms[] }
cities[]        → { slug, name, region, districts[], postal[], landmarks[],
                    neighbours[], population_band, local_notes, radius_km }
```

**Generator** = a script (Python/Node, like our `build_*` scripts) that, for each `service × city`:
1. calls the LLM once with the merged context (business + that service + that city) to produce **fresh, unique body content** for that specific cell (never find-and-replace),
2. injects it into the master template,
3. writes `04_site/<url>/index.html`.
Then `npm run build` + `npm run deploy` (incremental FTP), exactly as today.

**URL structure** (city + service, both in the slug — the whole point):
- DE (741 pilot): `/local-seo-nuernberg/`, `/google-maps-optimierung-fuerth/`, `/webdesign-erlangen/`
- EN (Bali/clients): `/plumbing-frisco/` style → `/[service]-[city]/`
- Keep it flat and consistent. One canonical pattern, forever.

**Reuse our design system** (never hand-roll): `{{> header }}`/`{{> header_de }}`, `{{> footer* }}`, `{{> consent }}`, `weavy.css`, the `seo_*` classes. CTAs use our **booking-link convention** (DE → `cal.com/741-studio-simjzw/30min`, EN → `calendly.com/martin-233/15-minute-meeting`).

---

## 3. Page anatomy (conversion above the fold, depth below)

Most traffic lands above the fold and never scrolls — so **convert there**, and give Google depth below.

**Above the fold (for humans):**
- H1 = `[Service] in [City]` (exact-match, natural).
- One-line local promise + trust bar (jahre am Markt, bewertungen, lizenziert/garantie, 24/7 if true).
- Primary CTA (call / book) + secondary (quote). Phone click-to-call.

**Below the fold (for Google + the ready-to-buy 20%):**
- Why locals in [City] choose [Business] (local specifics).
- The service, done properly: process, what's included, timeline.
- Areas we serve around [City]: districts + neighbouring towns (internal links).
- Local proof / reviews.
- Service+city FAQ (feeds FAQ schema + captures long-tail).
- Final CTA.

---

## 4. The uniqueness engine (the levers, concretely)

For each cell, the generator must weave in **at least 4** of these, drawn from the city/service data:
1. Named **districts & neighbouring towns** ("von der Altstadt bis Langwasser; auch in Stein, Zirndorf, Feucht").
2. **Local seasonality/context** affecting the service.
3. **Service-specific process & inclusions** (varies by service).
4. **Local price band & typical timeline.**
5. **3–5 FAQs unique to that service+city.**
6. **Rotated structure** (section order / H2 phrasing chosen from a variation set, keyed off the slug so it's deterministic but varied).
7. **Local proof** where available.

If a city has thin data, **don't publish that cell yet** — better 40 strong pages than 300 thin ones.

---

## 5. Schema & technical SEO (every page)

- `LocalBusiness` (or the right subtype) with `areaServed` = the city, `telephone`, `priceRange`, `aggregateRating` if real.
- `Service` node linked to the business, `serviceType` + `areaServed`.
- `FAQPage` from the page's FAQ block.
- `BreadcrumbList` (Home → Service hub → City page).
- Unique `<title>` + meta description per page (city + service), self-referencing `canonical`, one `<h1>`, `og:*`.
- Fast (our stack already is), mobile-first, `hreflang` if a page exists in DE + EN.

---

## 6. Internal linking (this is what makes the cluster crawl & rank)

Ties directly into the internal-linking system we just shipped. Structure:
- **Service hub** (`/local-seo/`) → links down to every `local-seo-[city]` page.
- **City hub** (optional `/standorte/nuernberg/`) → links to every `[service]-nuernberg` page.
- **Sibling links:** each city page links to 3–5 **neighbouring-city** pages of the same service ("Auch in Fürth, Erlangen, Schwabach").
- **Cross-service:** each city page links to the other services in the same city.
- Every page ≥1 link to a money/conversion page. Add all pages to the XML sitemap.

No orphans — an unlinked programmatic page won't get crawled or rank.

---

## 7. Trust, E-E-A-T & backlinks (DR is not the excuse)

- Real business identity, author/owner, address, reviews, licences — on-page and in schema.
- **Backlinks lift DR over time** and are the actual long game: local citations (branchenbücher, jameda/Doctolib for practices), local press, partnerships, the client's existing links. Start link-building in parallel; don't wait for it before publishing.
- Don't fake reviews/ratings in schema — manual-action risk.

---

## 8. Rollout & indexation (phased, monitored, pruned)

1. **Start small:** top ~5 services × top ~8 cities by search volume = ~40 pages. Prove it ranks before scaling.
2. **Publish in batches** over days/weeks (a 300-page dump on a DR-low domain is a spam signal). Our autoblog-equivalent = staged FTP deploys.
3. **Submit sitemap**, watch **GSC Coverage/Indexing**. If Google indexes but doesn't rank a cell → thicken it. If it refuses to index → the page is too thin; fix or `noindex`.
4. **Prune losers** after ~8–12 weeks. Merge or kill cells that never gained impressions.
5. Expand to more cities/services once the pattern proves out.

---

## 9. Measurement (use what we already have)

We have service-account read access to **GA4 (all client props)** + **Search Console (741.studio)** (`google-reporting-api-access`). Track per URL-pattern: impressions, clicks, avg position, indexed count, conversions. Monthly: which cells win, which to thicken/prune, where to add cities.

---

## 10. Productizing it per client (pilot = 741.studio)

**Pilot on ourselves first** to harden the system, then sell it:
- **741 pilot:** services = Local SEO, Google-Maps-Optimierung, Webdesign, Google Ads, Meta Ads. Cities = Nürnberg + Franken metros (Fürth, Erlangen, Bamberg, Würzburg, Regensburg, Ingolstadt, Schwabach, Zirndorf…). Target searches: "local seo nürnberg", "google maps optimierung fürth", etc.
- **Per client:** run the prompt with their CLIENT SITE URL → get their business.json + services[] + cities[] → generate → deploy to their site (their CMS or a subfolder). Offer as a productized package (setup + monthly expansion + link-building retainer).

**Offer framing:** "Wir bauen dir ~40–100 einzigartige Standort-Seiten, die genau die Suchen abfangen, die deine Kunden eingeben — [Leistung] in [Stadt]. Der Klempner im Beispiel zieht damit ~93.000 Besucher/Monat auf DR 40."

---

## 11. Pitfalls — do NOT

- ❌ One template, one word swapped (doorway/scaled-content = penalty).
- ❌ Publishing cities where you have no real presence/data (thin, and misleading).
- ❌ Fake ratings/reviews in schema.
- ❌ Mass-dumping hundreds of pages on day one.
- ❌ Orphan pages (no internal links).
- ❌ Same FAQ block on every page.
- ✅ Instead: fewer, genuinely-local, well-linked, phased, measured pages.

---

### TL;DR
Location + service, one canonical URL pattern, **genuinely unique per cell** (real local + service specifics, ≥40% non-reusable body), on our own pipeline, hub-and-spoke internal links, phased rollout, measured in GSC, links built in parallel. The idea is simple; producing 100 *distinct* pages is the hard part — and that's the part AI now does in minutes. Pilot on 741, then sell per client.
