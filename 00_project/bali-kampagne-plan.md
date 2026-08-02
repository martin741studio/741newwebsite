# Bali Campaign — Google Search for SEO & Web Development

Updated: 29 Jul 2026 · Segment: **expat / foreign-run businesses in Bali** · Budget: **€10–15/day** · Services: **Local SEO + Web Development** (Paid Ads added later)

---

## 1. Where we actually stand

| Component | Status |
|---|---|
| EN landing page `/pages/visibility-audit.html` | **live** (HTTP 200), quiz works, H1 is right |
| Supabase `advertorial_leads` + Resend notification | **working** |
| Local Falcon scan → review page → Loom | **working** (industrialised via `scripts/prospect-pipeline/`) |
| Bali / Indonesia references | **strong** — see section 2 |
| Google Ads campaign for Bali | **exists on paper only** — never created, never ran |
| Tracking on both quiz landing pages | **COMPLETELY MISSING** |

That last row is the blocker. `google-ads-kampagnen.md` claims "Meta Pixel: PageView / QuizOpened / Lead" on both pages. The deployed HTML contains **none of it** — just two placeholder comments. No GTM, no GA4, no Meta pixel, no `AW-` tag. The homepage has all three (GTM-PW3B9LZJ, G-FZG9BNPQXK, pixel 1028202146617964); the landing pages have nothing.

If we spent budget today, Google would not know what a lead is, could not optimise, and you could not tell afterwards which keyword worked. Supabase currently holds exactly **1 lead**, and it came from the advertorial, not from these pages.

**No ad spend until section 6 is done.**

### What the previous Bali work turned out to be

There are **20 blog pages targeting Bali keywords**, built in both the EN and DE paths (`/pages/blog/` and `/de/pages/blog/`) — `seo-agency-bali`, `best-local-seo-bali`, `web-design-bali`, `web-designer-bali`, `website-design-bali`, `best-web-design-bali`, `web-design-cost-bali`, `web-development-pricing-bali`, `seo-retainer-price-bali`, `reputation-management-bali`, `n8n-developer-bali` and more. They target almost exactly the keyword set proposed for the paid campaign.

**Search Console, last 90 days (30 Apr – 29 Jul 2026), verified via the reporting-bot service account:**

| | |
|---|---|
| Whole site | 27 clicks · 1,015 impressions |
| All Bali queries combined | **3 impressions, 0 clicks** |
| Bali pages with any impressions | 2 of 20 |
| `web design bali` | position 13 · 1 impression |
| `web development bali` | position 20 · 1 impression |
| Top click country | **Indonesia** (13 of 27 site-wide clicks) |

So the organic Bali play has produced effectively nothing in three months. The likely reason is visible in the pages themselves: **~470 words each, and five near-identical pages for a single intent** (`web-design-bali`, `web-designer-bali`, `website-design-bali`, `best-web-design-bali`, `best-web-designer-bali`). That is the doorway-page pattern Google suppresses. The DE copies correctly canonicalise to the EN versions, so duplication across paths is not the problem — thinness and cannibalisation are.

**What is still usable:**
- **The keyword research itself.** Someone already identified the same commercial intents I proposed independently. That is corroboration, not waste.
- **Position 13 for "web design bali"** means Google already considers the page somewhat relevant. Consolidating those five thin pages into one strong page would very likely move it.
- **Indonesia is already the top click source** for the site, tiny as the numbers are.

**What this changes strategically:** it strengthens the case for paid. Organic delivered nothing in 90 days; paid returns usable data in three weeks. And the paid search-terms report will show which Bali queries actually carry volume — which then tells us which of the 20 blog pages are worth consolidating and rewriting. **Paid buys the data that fixes the organic play.**

---

## 2. The proof stack — this is the campaign's biggest asset

The Bali and Indonesia work maps almost perfectly onto the verticals we are targeting. This is unusual and it should carry the landing page.

| Reference | Vertical | What we did |
|---|---|---|
| **Single Fin, Uluwatu** — Bali's iconic cliffside beach bar | Restaurant / bar | Full WordPress redesign and rebuild, then stayed on: tracking, analytics, supporting the in-house marketing team, running paid advertising |
| **Reload Sanctuary, Canggu** — premium gym & recovery club | Wellness / fitness | SEO, website optimisation, backlink building |
| **Avli Uluwatu** — modern Greek restaurant | Restaurant | Designed and built the responsive site: menu, location, table reservations |
| **Yacht Charter Indonesia** | Tourism / booking | Booking platform with advanced filtering and a structured fleet catalogue |
| **Villa Ventures** | Villa / property | Supported the brand through its growth phase — **the company was acquired by a larger company** |
| **Marugame Udon** | F&B chain | Tracking, newsletter integration, information architecture |

Four points worth building on:

**Single Fin is the anchor.** It is one of the best-known venues in Bali. A Canggu restaurant owner reading "we rebuilt Single Fin's website and run their paid advertising" needs no further explanation of whether you are competent. Nothing else on the page will do as much work.

**Reload Sanctuary is the SEO proof.** SEO, site optimisation and backlink building is exactly what ad group A sells — and it is a current, high-profile Canggu venue. That is proof of the specific service, not just general credibility.

**Villa Ventures is the exit story.** "We supported them through growth, and the company was ultimately acquired" is a much stronger signal than any testimonial, because it says the marketing was part of something that worked commercially. Your portfolio already states this publicly, so it is safe to repeat.

**Avli needs careful wording.** It was delivered with your partner agency **Talkinfive** (Celine), and the account sits with them now, not with you. So it belongs on the page as *work we built*, not as a current client. Phrase it as "Avli Uluwatu — built with our partner agency Talkinfive." That is accurate and the partnership itself reads as a plus.

Beyond Bali, the wider portfolio backs up the second service line: Numero Quattro (neighbourhood Italian — tracking plus paid ads), IMMOKAUF.AT, Anna Nussbaumer, Karin Lorenz, Vertrauenszentrum, Protex Textiles, IGR, WBG, Versance.ai, Tacheles, Stil Gefährten, Vesta Noris.

> **Before launch:** Single Fin, Avli, Villa Ventures, Yacht Charter and Marugame are already public on your portfolio page. **Reload Sanctuary is not.** Confirm you may name them publicly before putting them on the landing page.

---

## 3. The lead magnet — recommendation and reasoning

### Recommendation: the personalised video audit. No PDF, no guide, no ebook.

The evidence in agency direct response is consistent here, and Hormozi puts it most sharply: **the most valuable thing you can give away for free is a diagnosis, not knowledge.** A guide makes the prospect smarter and makes you replaceable. A diagnosis surfaces a specific, quantified problem they did not know they had, and positions you as the person who fixes it.

Why not a generic magnet:
- "10 SEO tips for Bali businesses" as a PDF collects email addresses and produces almost no conversations. The reader got what they came for and is done with you.
- An audit is **personalised** (their name, their competitors, their ranking), **visual** (the grid image is impossible to argue with) and **visibly effortful** — which triggers reciprocity before you have even spoken.
- You have already built this machine. Local Falcon → review page → Loom *is* this magnet, industrialised. That is your edge; a new asset would not be.

### Two variants, one system

Someone searching "web designer bali" does not want a Maps ranking grid. So the content adapts per ad group while the form, pipeline and delivery stay identical:

| Ad group | Audit content |
|---|---|
| **A — SEO** | Local Falcon grid (49 points), top-3 visibility share, the three strongest local competitors, three concrete actions |
| **B — Web** | 5-point teardown: speed, mobile, booking/conversion path, SEO basics, trust signals — plus what competitors do better |

One extra form question ("What do you want to fix first?") routes it. Everything downstream is unchanged.

### The consultation is not the lead magnet

An important distinction that a lot of agencies get wrong: "Book a free strategy call" as the **primary** CTA on cold traffic converts noticeably worse than an audit. The call costs the prospect time and commitment; the audit costs them 60 seconds.

Correct order: **the audit is the entry point, the call is the next step.** The call gets offered inside the audit video and on the results page.

A **secondary** CTA still belongs on the page: "Or skip the audit — book a call directly." Part of search traffic is already ready to buy, and there is no reason to slow them down. Two CTAs, clearly weighted.

---

## 4. The real risk: the magnet does not scale by itself

Honest arithmetic at €12/day:

| | |
|---|---|
| Monthly budget | ~€360 |
| CPC in Bali, English, these terms | roughly €0.40–1.20 — **estimated, must be validated** |
| Clicks/month | ~450 |
| Landing page conversion (audit request, high intent) | 8–15% |
| **Audit requests/month** | **~45** |

45 audits a month is **about two Loom videos every working day.** That is where this system breaks — not at the budget.

**So the form needs a qualification gate.** Not to lose leads, but to point your time at the people who can invest €2,000+. Four or five fields, no more:

1. Business name + website
2. Business type (dropdown: Restaurant & Bar / Villa & Accommodation / Wellness & Fitness / Clinic & Health / Retail / Real Estate / Other) — job seekers and freelancers self-select out here
3. "Do you already have a Google Business Profile?" (Yes / No / Not sure)
4. "How many more customers per month would make a real difference?" — this is the budget question without asking about budget
5. WhatsApp number (more important than email in Bali)

Anyone choosing "Other" in field 2 and giving nothing concrete in field 4 gets a short written summary instead of a personal video.

Chain onwards: 45 audits → ~10–13 calls → **2–4 clients/month**. Against your package structure (€1,999 / €3,699 / €7,999) that pays for itself on the first close. These are experience-based figures, not a forecast — after three weeks we replace them with real ones.

---

## 5. Landing page

Base is the existing `/pages/visibility-audit.html`. At 23 KB it is lean and the H1 already works. What needs adding:

**Above the fold**
- H1 stays close to: "How visible is your business on Google when customers search nearby?"
- Subhead with the offer in one sentence + "Free. No strings. Delivered on WhatsApp within 24 hours."
- Primary CTA: *Get my free audit* → form
- Secondary, smaller: *Or book a 20-min call directly*

**Proof — the most important block for this segment**
- A real grid scan image as preview. That is the asset that sells. An anonymised real scan, never a stock image.
- **Single Fin, Reload Sanctuary, Avli Uluwatu, Yacht Charter Indonesia** with mockups. Ideally logos in a row plus one sentence each.
- The **Villa Ventures exit** as a separate line — it earns its own space.
- Numbers bar from the growth-plan page (2,500+ / 100+ / 30+)

**Trust block — "I live here"**
For expat operators this is the difference between you and any agency in Jakarta or Manila. You are on the island, reachable in their time zone, you speak their language. Put it on the page explicitly, with a photo.

**What you get (3 points)**, **Who it's for**, **FAQ** (Is it really free? What happens to my data? How long does it take? Am I too small for this?)

**Second CTA at the foot of the page.**

---

## 6. Campaign structure

**Settings**
- Type: Search only. Display Network and Search Partners **off** — otherwise the budget burns instantly in Bali.
- Geo: **Bali**, targeting option must be *Presence: People in or regularly in your included locations*. Not "interest" — that buys tourists.
- Language: English
- Budget: €12/day
- Bidding: start on **Maximise clicks with a €1.20 CPC cap**. Switch to *Maximise conversions* after 15–30 conversions.
- Ad rotation: even, until there is data

### Yes — English keywords only, and that is a deliberate choice

You asked to confirm this. English is right, for two reasons:

1. The segment we picked searches in English. Expat owners in Canggu, Uluwatu and Seminyak do not search "jasa seo bali".
2. Indonesian-language keywords would pull in exactly the local-price segment we deliberately excluded — businesses that will not pay €2,000+. Same reason the Indonesian **negatives** below matter so much: they keep that traffic out.

### Ad group A — Local SEO

```
"seo agency bali"          "local seo bali"
"seo bali"                 "seo consultant bali"
"google maps ranking bali" "google business profile bali"
"digital marketing agency bali"
"marketing agency canggu"  "seo seminyak"
"get found on google bali"
```

### Ad group B — Web Development

```
"web design bali"          "website designer bali"
"web developer bali"       "website design canggu"
"wordpress developer bali" "webflow developer bali"
"restaurant website design bali"
"villa website design"
"website redesign bali"
```

All **phrase match** at the start. Broad only once the negative list is built and smart bidding is running.

### Negative keywords — decisive in Bali

Bali has enormous search volume from job seekers, freelancers and digital nomads who offer these services *themselves*. Without this list you pay for all of it:

```
job, jobs, hiring, vacancy, lowongan, kerja, karir, career, internship, intern,
salary, gaji, freelance, freelancer, remote, work from bali, digital nomad,
course, kursus, training, belajar, tutorial, certification, bootcamp, class,
cheap, murah, gratis, free tool, template, plugin, theme, wordpress hosting,
how to, what is, diy, do it yourself, login, adalah, pengertian
```

The Indonesian terms (`lowongan`, `kerja`, `murah`, `kursus`, `gaji`, `adalah`) matter more than the English ones — without them that traffic arrives in volume.

### Ad copy

**Ad group A — headlines (≤30 chars)**
```
Free Google Visibility Audit
Where Do You Rank in Bali?
Local SEO for Bali Business
Get Found on Google Maps
Personal Video Audit — Free
We Work With Single Fin
Trusted in Canggu & Uluwatu
Beat Your Local Competitors
More Guests From Google
Sent to WhatsApp in 24h
Based in Bali, Not Offshore
Free & No Strings Attached
```

**Descriptions (≤90 chars)**
```
Free audit with a personal video: your Maps ranking, competitors & 3 clear next steps.
Takes 60 seconds to request. Sent to your WhatsApp within 24 hours. No cost, no pitch.
We do SEO and backlinks for Reload Sanctuary and paid ads for Single Fin, right here.
See exactly where you show up when customers search nearby — and who outranks you.
```

**Ad group B — headlines**
```
Websites for Bali Business
Free 5-Point Site Teardown
Web Design in Bali
Your Site, Honestly Reviewed
Built to Get You Bookings
Restaurant & Villa Websites
We Built Single Fin's Site
See What's Costing You Leads
Free Video Review — 24h
Based in Bali, Not Offshore
```

**Descriptions**
```
Free video teardown: speed, mobile, booking flow & trust — and what to fix first.
We rebuilt Single Fin and Avli Uluwatu. Same care, whatever your size.
Request in 60 seconds. Personal video to your WhatsApp within 24 hours.
A site that loads fast and turns visitors into bookings. Not just a pretty page.
```

**Extensions:** sitelinks (Free Audit / Our Work / How It Works / About) · callouts (100% Free · Personal Video · Based in Bali · 24h Turnaround) · call extension · location extension if 741.Studio has a Bali GBP

---

## 7. Tracking — must be in place before the first euro

1. **Add GTM container `GTM-PW3B9LZJ` to both quiz landing pages.** It already carries GA4 and the Meta pixel and respects the Consent Mode v2 setup live since 23 Jul. Three problems solved in one step.
2. **Create the Google Ads conversion action:** "Lead – Free Audit Request", category *Submit lead form*, count *One*, value left empty for now.
3. **Fire on quiz submit**, alongside the existing Supabase insert — and only once the insert succeeded. No fire-and-forget on click.
4. **Turn on Enhanced Conversions** (hashed email/phone). Materially improves attribution, costs nothing.
5. **Verify with Tag Assistant in preview mode** before the campaign starts — exactly as we did for Kraft. Do not rely on "should be fine".
6. Phase 2: **offline conversion import** for calls actually booked and deals closed. That is when Google starts optimising for customers instead of form fills, and that is when campaigns get genuinely good.

---

## 8. Follow-up — WhatsApp first

In Indonesia WhatsApp is the default channel and email is second choice. The page already asks for the number.

| Timing | Message |
|---|---|
| Immediate, automated | Confirmation: "Got it — your audit lands here within 24 hours." Sets expectation and secures the channel. |
| Within 24h | Link to the personal review page + video. One sentence, no selling. |
| +2 days | "Did you get a chance to watch it? Happy to walk you through it — 20 minutes." |
| +5 days | **One** concrete finding from their audit as the hook. Add something, don't repeat. |
| +10 days | Soft close: "I'll leave it here — the audit is yours to keep. Ping me whenever." |

The 24-hour promise is a promise. If volume makes it unrealistic, change it to 48 hours in advance rather than break it.

---

## 9. Order of work

**Phase 1 — before any spend**
1. ~~Build the two service landing pages~~ **DONE 29 Jul** — `/pages/bali-local-seo.html` and `/pages/bali-web-design.html` are live, noindex, with the Bali proof block, the Villa Ventures exit line, the "I live here" block, the qualification question and the secondary call CTA. Supabase insert verified end-to-end (HTTP 201) including the new `ziel` column.
2. ~~Confirm public naming rights for Reload Sanctuary~~ **DONE — confirmed by Martin**
3. Set the booking URL on the `[data-call]` links (currently `href="#"`, so the secondary CTA hides itself until a real calendar link exists)
4. Add a real grid-scan preview image to the Local SEO page
5. GTM container `GTM-PW3B9LZJ` into both new pages, verified with Tag Assistant
6. Create the Google Ads conversion action, drop the tag at the marked spot inside `submit()`, run a test submit

**Phase 2 — launch**
6. Create campaign: 2 ad groups, phrase match, negative list, presence targeting, €12/day
7. Automate the WhatsApp confirmation
8. Go live

**Phase 3 — after 7–14 days**
9. Review the search terms report and sharpen negatives — expect a long list the first time in Bali
10. Compare real CPCs and conversion rate against the estimates in section 4
11. Switch to *Maximise conversions* after 15–30 conversions

**Phase 4 — expansion**
12. If ad group A carries: add paid ads as a third ad group
13. Second campaign for searches **outside** Indonesia using geo-modified keywords ("seo agency bali" typed from Australia or Singapore — villa and restaurant owners often are not on the island)
14. Offline conversion import

---

## 10. Deliberately left open

- **The CPC and conversion assumptions in section 4 are estimates.** I have no reliable first-party Bali data. They exist for capacity planning, not as a promise — we replace them after three weeks.
- **Whether 741.Studio has its own Google Business Profile in Bali** — not checked. If it does, the location extension belongs in the campaign and strengthens the "based in Bali" argument considerably.
- **Naming rights for Reload Sanctuary** — not yet in the public portfolio, unlike the others.
- **No pricing on the landing page** — consistent with the rule that numbers only come up on the call.
