# 741 Bali Google Ads — Performance Report

**Report date:** 2026-08-05 · **Data window:** Jul 9 – Aug 5, 2026 (28 days) · **Source:** Google Ads UI, account **741 Acc** (534-995-9699), live pull · GMT+02:00, reporting not real-time.

> **Headline:** Delivery has finally kicked in. Impressions jumped from **75 (Jul 31)** to **332 (Aug 5)** — most of it in the last ~5 days (see trend). Still tiny absolute volume, and **still 0 tracked conversions** because conversion tracking isn't set up in this account yet. That's the #1 fix.

## Campaign setup
- **Name:** Bali – Local SEO & Web Design (EN)
- **Type:** Search · **Language:** English · **Location:** Bali (Presence)
- **Bidding:** Maximize Clicks (€1.20 CPC cap) · **Budget:** €12.00/day
- **Status:** Eligible **(Limited)** — "Bid setting limited" · **Optimization score:** 77.5%
- 6 drafts still in progress (retargeting / Demand Gen layer not live).

## Headline metrics (Jul 9 – Aug 5)
| Metric | Value |
|---|---|
| Impressions | 332 |
| Clicks | 13 |
| CTR | 3.93% |
| Avg. CPC | €1.07 |
| Cost | €13.85 |
| Unique users | 155 |
| Conversions | 0 *(tracking works & is live — 0 = no form submissions yet, see note)* |

**Budget usage:** €13.85 spent over 28 days against a €12/day budget = ~**€0.49/day actual** (~4% of budget). The ceiling is search demand, not budget.

## By ad group
| Ad group | Clicks | Avg. CPC | ~Cost | Conv. |
|---|---|---|---|---|
| Web Design | 7 | €1.16 | ~€8.12 | 0 |
| Local SEO *(named "Ad group 1")* | 6 | €0.96 | ~€5.76 | 0 |

Web Design pulls slightly more clicks; Local SEO is cheaper per click. Both Eligible.

## What it means
1. **The ramp is real but small.** ~4× impressions and ~4× clicks vs Jul 31, concentrated in the final days — the campaign is warming up. But 13 clicks over 4 weeks is still noise-level for conclusions.
2. **Budget is not the constraint — demand is.** Spending ~4% of the daily budget confirms there simply isn't much English-language search volume for these terms in the Bali geo per day (structural, matches the Jul 31 read).
3. **CTR is healthy (3.93%).**
4. **Conversion tracking IS set up and live — the 0 is real, not a broken tag.** Verified in the served HTML on **both** Bali landing pages: base tag AW-564129015 (via consent partial) + a conversion event `"Lead – Free Audit Request"` (`gtag('event','conversion',{send_to:'AW-564129015/c-PSCOG1utgcEPfZ_4wC'})`) firing in the form `submit()` handler. Google Ads shows 0 because **no one has submitted the form yet** (13 clicks = almost no traffic). Google's "Set up conversion tracking" nag is the standard prompt for a conversion action that has never recorded a conversion; it clears on the first real or test lead. **VERIFIED 2026-08-05 via live test submit:** the page dataLayer confirmed `gtag` loaded, Consent Mode v2 = all granted (ad_storage/ad_user_data/ad_personalization/analytics_storage), and the conversion event `{event:'conversion', send_to:'AW-564129015/c-PSCOG1utgcEPfZ_4wC'}` was pushed on submit. Tracking fires correctly end-to-end — the earlier "consent could swallow it" caveat does NOT apply. The one test lead (name "TEST Conversion Check") should appear in Google Ads conversions within a few hours and will clear the nag.
5. **"Bid setting limited"** flag + 77.5% opt score — the €1.20 CPC cap under Maximize Clicks may be throttling reach.

## Recommended actions
- **Set up conversion tracking (Priority 1).** Track form submits / calls / WhatsApp so the 13 clicks become measurable. Without this the campaign runs blind — same gap we fixed on the Bali Healing account.
- **Activate the 6 drafts (retargeting / Demand Gen).** Search volume is capped in this small market; reach growth has to come from the retargeting/Demand Gen layer.
- **Loosen the bid** (raise/remove the €1.20 CPC cap) to clear the "bid setting limited" throttle, or test Max Conversions once tracking has data.
- **Broaden keywords** toward how the market searches: `digital marketing agency bali`, `marketing agency bali`, `social media agency bali`, `agency bali` (from Jul 31 search-term learnings).
- **Add image assets** to the RSAs (Google flags a ~+4.1% CTR opportunity).

*Next report: re-pull ~mid/late August once tracking is live and the drafts are running, for a meaningful lead trend.*
