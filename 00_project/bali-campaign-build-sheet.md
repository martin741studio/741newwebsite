# Bali Campaign — Google Ads Build Sheet

Ready to paste into Google Ads. Every asset was character-checked against Google's limits — all pass.
**No client names appear anywhere in the ads.** Updated 29 Jul 2026.

---

## Keyword search volume — checked in Google Keyword Planner (29 Jul 2026)

Location **Bali, Indonesia** (matches the campaign's Presence targeting), all languages, Google. Raw export saved at `00_project/bali-keyword-volume-2026-07-29.csv`.

| Keyword | Avg. monthly searches (Bali) | Competition | Top-of-page bid |
|---|---|---|---|
| **web design bali** | **~500** | Low | €0.40–2.80 |
| **digital marketing agency bali** | **~500** | Medium | €0.58–2.15 |
| seo agency bali | ~50 | Low | €0.49–1.37 |
| seo bali | ~50 | High | €0.53–1.92 |
| seo consultant bali | ~50 | Medium | — |
| website designer bali | ~50 | High | €0.99–3.29 |
| web developer bali | ~50 | Medium | €0.35–1.72 |
| wordpress developer bali | ~50 | Low | — |
| villa website design | ~50 | Low | — |
| local seo bali | **< 10** | — | — |
| google maps ranking bali | **< 10** | — | — |
| google business profile bali | **< 10** | — | — |
| marketing agency canggu | **< 10** | — | — |
| seo seminyak | **< 10** | — | — |
| get found on google bali | **< 10** | — | — |
| website design canggu | **< 10** | — | — |
| webflow developer bali | **< 10** | — | — |
| restaurant website design bali | **< 10** | — | — |
| website redesign bali | **< 10** | — | — |

**Verdict — thin but real, and cheap.** Only two head terms carry meaningful volume (~500/mo each); seven more sit at ~50; **ten of the nineteen are below 10 searches/month in Bali**. Competition is mostly Low, and top-of-page bids are €0.35–0.99 at the low end — clicks here are cheap. The risk is **volume, not cost**: at €12/day this market may not spend the full budget from these exact terms alone.

What this means for the build:
- **Phrase match stays** — it captures the long-tail variants ("web design bali price", "best web designer canggu", etc.) that individually read < 10 but add up. The sum of real reach is higher than the table's exact figures.
- **The near-zero keywords are kept but not relied on.** On phrase match they simply won't serve if nobody searches them; they cost nothing to leave in.
- **Web Design (ad group B) is the stronger of the two** — its volume is spread across web design / developer / designer / villa terms. Local SEO (ad group A) leans almost entirely on the single term `digital marketing agency bali`, since `local seo bali` itself is < 10.
- **Consider broad match on the two head terms** (`web design bali`, `digital marketing agency bali`) once conversion tracking is live and Smart Bidding can steer it — that's where the hidden variant volume is.

**Important caveat:** this is Bali-*presence* data — people physically on the island. A real slice of this audience (villa owners, restaurateurs setting up) searches from **abroad** before they arrive, which this query does not count. That undercounts true demand and is exactly what the Phase-4 "second campaign for searches outside Indonesia" is for. Worth running that geo check before writing the market off.

### Broader service terms also checked (e-commerce, WordPress, general SEO, other platforms — 29 Jul)

Ran a second batch to cover the full service range, not just local SEO. Raw export: `00_project/bali-keyword-volume-expanded-2026-07-29.csv`.

| Keyword | Searches/mo (Bali) | Competition |
|---|---|---|
| **digital agency bali** | **~500** | Medium |
| seo services bali | ~50 | Medium |
| seo indonesia | ~50 | Medium |
| web design indonesia | ~50 | Low |
| web development bali | ~50 | Low |
| ecommerce website bali · online store bali · shopify bali · shopify developer bali · woocommerce bali · wordpress website bali · website builder bali · squarespace developer bali · ui ux designer bali · landing page design bali · google ads agency bali · web design uluwatu | **all < 10** | — |

**The pattern is now unmistakable.** In Bali people search **generic head terms** — `web design bali`, `digital agency bali`, `digital marketing agency bali` (each ~500/mo) — and **not** platform- or service-specific terms. Every e-commerce, Shopify, WooCommerce, WordPress-site, Squarespace, UI/UX and landing-page keyword is < 10/mo locally. Even `web design uluwatu` is < 10 (the town names don't get typed; "bali" does).

**What this means for the build:**
- **Add `digital agency bali` (~500) to ad group A** — it's a third real head term and a strong fit for the full-service positioning.
- **Do not add platform-specific keywords** (shopify/woocommerce/ecommerce/squarespace/landing-page). They're dead weight in Bali. The landing pages sell the specific services; the *ads* should bid the broad terms that people actually type.
- **Three head terms carry the whole account:** `web design bali`, `digital agency bali`, `digital marketing agency bali`. Everything else is long-tail that phrase/broad match will mop up. This is a **lean, broad-term campaign**, not a big keyword list.
- The e-commerce / WordPress / platform demand is real for the *business* — it just isn't searched under those names in Bali. It lives in the head terms and, more so, in the **abroad audience** (Phase-4 worldwide campaign) still to be checked.

---

## Campaign settings

| Setting | Value |
|---|---|
| Campaign type | **Search** |
| Networks | Google Search **only**. Search Partners **OFF**, Display **OFF** |
| Google Maps | Not targeted for now — needs a Bali Google Business Profile, which Martin will add later |
| Locations | **Bali** |
| Location option | **Presence: People in or regularly in your included locations** (never "interest" — that buys tourists) |
| Language | English |
| Budget | €12/day |
| Bidding | **Maximise clicks**, CPC cap **€1.20**. Switch to Maximise conversions after 15–30 conversions |
| Ad rotation | Even, until there is data |
| Ad schedule | All hours to start; trim later from the hour-of-day report |

Nothing below depends on the Maps/GBP piece. Search-only runs fine on its own.

---

## Ad group A — Local SEO

**Final URL:** `https://741.studio/pages/bali-local-seo.html`
**Display path:** `/local-seo/bali`

### Keywords (phrase match)
```
"seo agency bali"            "local seo bali"
"seo bali"                   "seo consultant bali"
"google maps ranking bali"   "google business profile bali"
"digital marketing agency bali"
"marketing agency canggu"    "seo seminyak"
"get found on google bali"
```

### Headlines (15 — max 30 chars)
```
Free Google Visibility Audit    (28)
Where Do You Rank in Bali?      (26)
Local SEO for Bali Business     (27)
Get Found on Google Maps        (24)
Personal Video Audit, Free      (26)
200+ Businesses Audited         (23)
Based in Bali, Not Offshore     (27)
Beat Your Local Competitors     (27)
More Guests From Google         (23)
Sent to WhatsApp in 24h         (23)
Only 3 Spots on the Map         (23)
Free, No Strings Attached       (25)
Canggu, Uluwatu & Seminyak      (26)
See Your Real Map Ranking       (25)
Book a Free Consultation        (24)
```

### Descriptions (4 — max 90 chars)
```
Free audit with a personal video: your Maps ranking, competitors & 3 clear next steps.   (86)
60 seconds to request. Sent to your WhatsApp within 24 hours. No cost, no pitch.   (80)
Made by hand by an analyst who lives in Bali, not generated by an automated tool.   (81)
See exactly where you show up when customers search nearby, and who outranks you.   (81)
```

---

## Ad group B — Web Design

**Final URL:** `https://741.studio/pages/bali-web-design.html`
**Display path:** `/web-design/bali`

### Keywords (phrase match)
```
"web design bali"            "website designer bali"
"web developer bali"         "website design canggu"
"wordpress developer bali"   "webflow developer bali"
"restaurant website design bali"
"villa website design"
"website redesign bali"
```

### Headlines (15 — max 30 chars)
```
Websites for Bali Business      (26)
Free 5-Point Site Teardown      (26)
Web Design in Bali              (18)
No Templates, Built Custom      (26)
Built to Get You Bookings       (25)
Restaurant & Villa Websites     (27)
Your Site, Honestly Reviewed    (28)
Based in Bali, Not Offshore     (27)
Free Video Review in 24h        (24)
Stop Losing Direct Bookings     (27)
Fast, Mobile, Bookable          (22)
See What Costs You Leads        (24)
WordPress, Webflow, Custom      (26)
Book a Free Consultation        (24)
Cut Your OTA Commission         (23)
```

### Descriptions (4 — max 90 chars)
```
Free video teardown: speed, mobile, booking flow & trust, and what to fix first.   (80)
Built and run from Bali, in your time zone, by someone you can actually meet.   (77)
Request in 60 seconds. Personal video to your WhatsApp within 24 hours.   (71)
A site that loads fast and turns visitors into bookings. Not just a pretty page.   (80)
```

---

## Shared assets (campaign level)

### Sitelinks — none point to an external booking page
| Text (≤25) | Description line 1 (≤35) | Description line 2 (≤35) | URL |
|---|---|---|---|
| Free Visibility Audit | See where you rank on Maps | Personal video in 24 hours | `/pages/bali-local-seo.html` |
| Free Website Review | Speed, mobile, booking path | Free video within 24 hours | `/pages/bali-web-design.html` |
| How It Works | Six questions, then a video | No cost and no obligation | `/pages/bali-local-seo.html` |
| Our Portfolio | Web builds and local SEO | Beach clubs to practices | `/pages/portfolio_full.html` |

### Callouts (≤25)
```
100% Free Audit · Personal Video · Based in Bali · 24h Turnaround · No Long Contracts · WhatsApp Delivery
```

### Structured snippet — header "Services" (≤25 each)
```
Local SEO · Google Business Profile · Web Design · Web Development · Google Ads · Tracking & Analytics
```

### Call asset
Indonesian WhatsApp / phone: **+62 878 6043 0975** — add if you want click-to-call in the ads.

---

## Negative keywords — campaign level

Bali carries heavy job-seeker and freelancer volume. The Indonesian terms matter more than the English ones.

```
job, jobs, hiring, vacancy, lowongan, kerja, karir, career, internship, intern,
salary, gaji, freelance, freelancer, remote, work from bali, digital nomad,
course, kursus, training, belajar, tutorial, certification, bootcamp, class,
cheap, murah, gratis, free tool, template, plugin, theme, wordpress hosting,
how to, what is, diy, do it yourself, login, adalah, pengertian
```

---

## Where the traffic lands

Both landing pages are live and offer three routes, deliberately ordered:

1. **Free audit / site review** (primary) — the 6-step form, writes to Supabase, triggers the Resend notification.
2. **Chat on WhatsApp** (secondary) — straight to +62 878 6043 0975, which is how people actually get in touch in Bali.
3. **Book a 20-minute call** — shown **after** the form is submitted, not before. Cold ad traffic sent directly to a booking page loses everyone who is not ready to pick a slot; capturing the contact first means the follow-up is still possible.

Legal pages for the Indonesian entity are live: `/pages/legal-notice.html` and `/pages/privacy-policy.html` (PT. Amana Events Indonesia, NPWP 84.750.732.4-903.000). The German Impressum and Datenschutz are untouched and still serve the DACH side.

---

## Before you switch it on

1. **Google Ads conversion action** — "Lead – Free Audit Request", category *Submit lead form*, count *One*. The tag goes at the marked spot inside `submit()` on both pages; it fires only after a successful Supabase insert.
2. **GTM container `GTM-PW3B9LZJ`** into both pages (brings GA4 + Consent Mode v2).
3. **Enhanced conversions** on (hashed email/phone).
4. **Verify with Tag Assistant** in preview before spending a cent.

Lead pipeline is verified end-to-end: Supabase insert returned 201 with the `ziel` qualification field, Resend notification fires off the same table.

---

## LIVE STATUS (published 29 Jul 2026)

Campaign **"Bali - Local SEO & Web Design (EN)"** was published to account **741 Acc (534-995-9699)** and is in Google's review queue. Built and live:
- Search only · Bali + Presence · English · Maximise clicks, €1.20 cap · €12/day
- One ad group **Local SEO**: 12 phrase-match keywords + complete RSA (15 headlines, 4 descriptions), final URL `/pages/bali-local-seo.html`, path `/local-seo/bali`

**Account Google tag (gtag.js) surfaced at publish: `G-NC042XTGEZ`** — this is the base Google tag for the 741 Acc Ads account (distinct from the site's existing GTM-PW3B9LZJ / GA4 G-FZG9BNPQXK). The base tag alone does NOT track conversions; a conversion **action** (AW-… + conversion label) must be created and fired on quiz submit.

### ✅ Conversion tracking — DONE & LIVE (29 Jul 2026)
Conversion action **"Lead – Free Audit Request"** created in 741 Acc:
- Category *Submit lead form* · Primary (used for bidding optimization) · Count *One* · same value €1 · click-through window 90 days · data-driven attribution · enhanced conversions on.
- **Google Ads tag: `AW-564129015`** · **conversion label: `c-PSCOG1utgcEPfZ_4wC`** · **send_to: `AW-564129015/c-PSCOG1utgcEPfZ_4wC`**
- Base `AW-564129015` config added to the shared **consent partial** (`04_site/components/consent.html` → `loadGoogleTags()`), so it loads consent-gated (Consent Mode v2) on every 741.studio page and enables remarketing too.
- Event fires in `submit()` on both Bali LPs via `gaLead()` — after a successful Supabase insert **and** on the mailto fallback (both = real lead). Deployed live; verified present in page source + queues in dataLayer.
- Google Ads will show status "Unverified / No recent conversions" until the first real lead — normal. (The account pre-filled `www.balihealing.com` as the data-source label; irrelevant — the event snippet fires from 741.studio.)

### ✅ Web Design ad group — DONE & LIVE (29 Jul 2026)
Second ad group **"Web Design"** added to the live campaign (campaignId 24075426150), status **Eligible**:
- 9 phrase-match keywords (`"web design bali"`, `"website designer bali"`, `"web developer bali"`, `"website design canggu"`, `"wordpress developer bali"`, `"webflow developer bali"`, `"restaurant website design bali"`, `"villa website design"`, `"website redesign bali"`).
- Full RSA: 15 headlines + 4 descriptions (from this doc), Final URL `https://741.studio/pages/bali-web-design.html`, display path `web-design/bali`. Ad reviewed — **no policy issues**.
- Campaign now has **2 ad groups / 21 keywords total** (12 Local SEO + 9 Web Design), verified in the keywords view ("1-10 of 21").
- ⚠️ UI gotcha for next time: the streamlined "new ad group" flow uses an **autocomplete dropdown on headline fields** — press **Escape after typing each headline** or a Google suggestion silently overwrites it. Also the keyword textarea can clear on first "Save and continue" without saving; re-enter keywords and Save again (it does NOT create duplicates — the ad group only commits on the successful save).

### ✅ Sitelinks, callouts, structured snippet — DONE & LIVE (29 Jul 2026)
Added at campaign level (Assets → +), all "Pending under review" → will go Eligible:
- **4 sitelinks:** Free Website Review→bali-web-design.html · Free Visibility Audit→bali-local-seo.html · Our Portfolio→portfolio_full.html · How It Works→bali-local-seo.html (each with 2 description lines).
- **6 callouts:** 100% Free Audit · Personal Video · Based in Bali · 24h Turnaround · No Long Contracts · WhatsApp Delivery.
- **1 structured snippet:** header **"Service catalog"** (English) — NOTE: Google has no plain "Services" header; "Service catalog" is the right one. Values: Local SEO · Google Business Profile · Web Design · Web Development · Google Ads · Tracking & Analytics.
- UI note: the Assets "+" button opens a type menu (Sitelink/Callout/Structured snippet/…) — click it and pick the type; it sometimes defaults straight into Call/Text-disclaimer, so if the wrong editor opens, Cancel and reopen the "+".

### Still to do on the LIVE campaign (in priority order)
1. ✅ **Negative keywords** — done (40-term list added; verified "1-10 of 40").
2. ✅ **Web Design ad group** — done.
3. ✅ **Sitelinks, callouts, structured snippet** — done (see above).
4. **Sitelinks, callouts, structured snippets** — from the shared-assets section above.
5. Business name (needs approved-name verification) — currently a placeholder.
