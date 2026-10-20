# YouTube Content Research: Health Practitioners (superseded avatar, kept for reference)

**2026-09-16 update: the target avatar changed.** 741's actual positioning is Website CRO, Paid Ads, Local SEO, and Backend Automations/Tech Setups, targeting Graphic Designers/Creative Agency Owners and High-Ticket Local Service Owners — not health practitioners specifically. The health-practitioner research below stays as reference (dentists showed a real, clean signal, so it's still usable if a health client wants a channel). The current, active research is in [youtube-content-research-creative-agencies.md](youtube-content-research-creative-agencies.md).


Goal: build a 741 channel for health practitioners. The channel is lead gen. Viewers are health practitioners. The video moves them toward a call with 741.

The promised result: more new patients. This comes from two parts. Part one is Google visibility (rank higher, get found). Part two is conversion (the visit turns into a booking).

## Update: real YouTube API data (2026-09-16)

We got a restricted YouTube Data API key and ran a real outlier scan. Script: [scripts/youtube-outlier-research.mjs](../scripts/youtube-outlier-research.mjs). Key stored in `.secrets/youtube-api.env` (git-ignored).

Method: 8 seed keywords, top 15 search results each, compared each video's views against its own channel's average views per video. An outlier is 3x+ the channel average, per the SOP.

Result: 94 videos found, 51 outliers. After removing patient-facing clinical/exercise content and viral junk (AI slop, "funny chiropractor" clips), 39 outliers are real practitioner-marketing content. Findings:

**Dental is the strongest sub-niche by far.** 7 of the top marketing outliers are dental-specific:
- "Dental SEO Services to Rank Higher and Get More Patients" (ProSites) — 52.3x channel average, 29,594 views
- "Best Dental Marketing Strategy" (LeadsChief) — 50.9x, 21,074 views
- "Dental Marketing | Dr. Lee Informational Video" (Medicalbound) — 34x, 162,391 views
- "How to Increase Patient Footfall in Your Clinic & Hospital" — 32.6x, 36,663 views
- "New Patient Marketing For Dentists & Doctors | Un-Advertising" — 29.7x, 13,083 views
- "Dentists: Attract More Implant Patients" — 16.9x, 94,682 views
- "Local SEO For Dentists 2022 | #1 Rankings Guaranteed" — 10x

**"Chiropractor" as a keyword is noisy.** Most top results are viral entertainment (AI-generated "funny chiropractor" clips, back-crack videos), not marketing content. A channel targeting chiropractors needs a sharper keyword angle than "chiropractor google ranking" to reach the right viewer.

**"Physical therapist get more patients" pulls patient-facing clinical content**, not practitioner marketing content (exercise demos, condition explainers with millions of views). This confirms: patients search for symptoms and exercises, not practitioners searching how to market. If we ever build a channel aimed at patients (not practitioners), clinical/exercise content is the real outlier format — but that is a different channel with a different goal.

**One real signal worth a title format on its own:** "How to Rank #1 in ChatGPT Search (for chiropractors and businesses)" (Matthew Loop) — 9.7x. AI-search/AEO framing is an early, still-small demand signal. Fits [[gbp-visibility-blueprint]] work we already do.

**Practitioner-facing GBP-specific content is real but small.** "Boost Your Practice: Complete Every Google Profile Section!" (DoctorBoss, Shorts format) — 11.8x on a small channel. "Introduction to Google Business Profile for Medical Practices" (rater8) — 3.5x. These prove the topic works, but nobody has scaled it yet — confirms the gap noted below.

Revised targeting: **lead with dentists**, not chiropractors, for the first content batch. Demand is stronger and less polluted by unrelated viral content.

## Tool limit note (original, before API access)

The first pass of this research (before we had API access) used repeated topics across web search results as a weaker demand signal, not verified outlier data. That is now superseded by the real data above. The original topic list is kept below for reference.

## Phase 1: Demand signals found (original pass)

Practitioners already search for and watch videos on these topics:

- Google Business Profile (GBP) ranking and rank drops
- "Rank higher on Google Maps" (step-by-step guides)
- Reviews as a ranking factor ("review hacks")
- SEO for a specific practitioner type (chiropractor, physical therapist, doctor)
- Marketing plans for a private practice
- Attracting patients without paid ads
- Patient funnels (SEO + funnel combined)

Two patterns stand out:
1. Most videos target one practitioner type by name (chiropractor, physical therapist, doctor). Naming the exact practitioner type in the title outperforms a generic "healthcare" title. The real data above confirms this, and adds that dentist-specific targeting outperforms chiropractor-specific targeting.
2. Most videos teach one narrow tactic (reviews, GBP categories, one ranking factor). Few combine ranking + conversion into one system. This is a gap 741 can own, since [[startseite-money-page-standard]] and [[gbp-visibility-blueprint]] already cover both halves.

## Channel deep-dive + negative evidence (2026-09-16)

Per the SOP's Phase 1 steps 4-6, we went inside the 7 outlier channels from the first pass and pulled their full upload history (up to 50 videos each) to find repeated winners and real failures. Script: [scripts/youtube-channel-deepdive.mjs](../scripts/youtube-channel-deepdive.mjs).

**What wins, seen more than once:**

- **Naming a real client + "Informational Video" framing.** Medicalbound's 3 best videos (30x, 10.2x, 9.6x their channel average) are all titled "Dental Marketing | Dr. [Name] Informational Video for [Real Practice Name]." Same production style, same channel — but see the failure case below.
- **Stating the service and the outcome directly in the title.** ProSites' best video (27x): "Dental SEO Services to Rank Higher and Get More Patients." No clickbait, just the offer.
- **The company's own tagline-as-title, stated as a benefit.** rater8's best video (23x) is their own brand line: "You make patients happy. We make sure everyone knows about it."
- **Mythbusting / calling something fake beats generic advice, on the same channel.** DoctorBoss's best video (7.8x): "Fight Fake Clinics! Doctor Dispels Regenerative Medicine Myths" — beat every generic "5 tips" video on that channel by 2-3x.

**What fails, seen more than once — real guardrails, not guesses:**

- **A client-brand video with no informational hook gets zero views.** Medicalbound's "Brand Video #5 for Peyser Dental," "Brand Video for Brooklyn Dental Collective" — 0 views each, same channel, same general topic as their 30x winner. The difference: no specific promise in the title, nothing for search to match.
- **Vague rhetorical questions bomb.** ProSites: "Is Your Dental Website Winning New Patients?", "Can Local Patients Find Your Dental Practice Online?" — single-digit views.
- **Generic year-stamped listicles bomb.** "How to Skyrocket Your Dental Practice in 2021" — 6 views on ProSites' own channel, next to their 29,594-view winner.
- **Generic coaching-speak titles bomb even on a personal-brand channel.** DoctorBoss: "Niche Down — Offer Validation for Your Coaching Business" — 2 views, against 168 for the mythbusting video above.
- **Watch-out, not a strategy: off-topic personal content can out-view the niche content on the same channel**, and this is a trap, not validation. Matthew Loop's top 5 videos by raw views are about raw milk, leg training, and walking around Zurich — not marketing. Chasing that view count would pull in the wrong audience for a lead-gen channel. Stay on-topic even when a tangent would "perform" better.

**Direct implication for 741:** we already have real client case studies ([case-studies/](../04_site/case-studies/) — Hüwel, Astrid Lengauer, Bernd Laserstein, Maria Abel). The Medicalbound pattern says: title these as informational videos naming the real practice and the real result, not as generic "client testimonial" or "brand video." The failure case above is a warning specifically against the generic version.

## Phase 2: Mechanism-to-outcome bridge

Dentists already search for "more patients" and "rank higher on Google." They do not yet search for 741's specific method (GBP system + funnel, together). The bridge titles below follow the SOP formula, but the two flagged ones are the ones actually backed by a real winner above (ProSites' direct-offer title, 27x its channel average):

- "If you don't understand your Google Business Profile, you don't understand new patients"
- "Dental SEO and a booking page that converts: how dentists actually rank and fill the schedule" — direct-offer format, modeled on ProSites' 27x winner, not a curiosity hook
- "If you don't understand review velocity, you don't understand your Google ranking"

## Phase 3: Title and thumbnail direction

Titles below are ranked by which real winner they are modeled on, not generic SOP templates:

- **Direct offer + outcome (ProSites pattern, 27x):** "Dental SEO Services to Rank Higher and Get More Patients" → our version: "How dentists rank higher on Google and fill more appointments"
- **Real client, named, informational framing (Medicalbound pattern, 30x):** "[Real Client Name]'s Google ranking, before and after — the exact changes" — use only with client permission to name them
- **Mythbusting (DoctorBoss pattern, 7.8x on that channel, beat every generic-advice video by 2-3x):** "The dental marketing agency lie: why your website traffic doesn't turn into patients"
- **Own tagline as benefit statement (rater8 pattern, 23x):** a short, plain sentence stating what 741 does and for whom, not a curiosity hook

Titles to avoid, because these exact patterns bombed on real channels in this niche:
- Rhetorical questions ("Is Your Dental Website Winning New Patients?" — single digits on ProSites)
- Year-stamped listicles ("...in 2021", "...in 2026" — 6 views on ProSites)
- Generic coaching-speak ("Niche Down — Offer Validation..." — 2 views on DoctorBoss)
- A client name with no informational hook ("Brand Video for X Dental" — 0 views on Medicalbound, same channel as their 30x winner)

Thumbnail direction:
- Show a real Local Falcon grid or a real ranking screenshot — the "working screen" authority marker, and it matches the direct-offer pattern above (no exaggeration needed, the real number is the hook).
- Red highlight block behind the real outcome number (example: "+40 patients/mo" — use only real, verified client numbers, per [[claims-need-real-data]]).
- Show the practitioner's own environment (dental chair, treatment room), not a generic office or stock photo.

## Phase 4: Hook script (PPP framework)

Use this structure for every video. The Proof step should use real 741 data, since generic authority claims are not what won in the deep-dive — named, specific results were:

- **Promise (0:00-0:10):** Restate the title's promise in one sentence.
- **Proof (0:10-0:25):** A specific, named or numeric claim, not a generic authority statement. Example: "We track ranking across 44 directories and Google's own ranking factors for health practices" or a real client number from [[huewel-client]] (reviews 7→40+, rank #25→top-10).
- **Plan (0:25-0:45):** List the video's steps out loud, in order, so the viewer commits to watching.

## Phase 5: Lead magnet and CTA

Apply the "unbiased expert test" from the SOP: would an outside expert still recommend this resource? Two options fit 741's existing assets:

- A free GBP scan/scorecard, using Local Falcon data (we already run this for prospects, see [[always-check-gbp-first]])
- A short checklist version of the [[gbp-visibility-blueprint]] (categories, services, map keywords)

CTA flow: video → free scan or checklist opt-in → booking link (per [[booking-link-convention]], EN audience → Calendly).

## Recommended first content pillars

1. **Real client case study videos**, titled in the Medicalbound informational-video pattern (named result, not "brand video"). We already have the source material: [case-studies/](../04_site/case-studies/) (Hüwel, Astrid Lengauer, Bernd Laserstein, Maria Abel). This is the single highest-evidence format found in the whole research pass.
2. Direct-offer videos on GBP + funnel combined, titled like the ProSites winner — state the service and outcome, no clickbait.
3. Mythbusting/teardown videos on dental practice Google profiles (real scans, blur the practice name unless the practice agrees to be named) — modeled on the DoctorBoss pattern that beat generic advice 2-3x on the same channel.
4. Dentist-specific videos first, then expand to physio/Heilpraktiker with a sharper keyword angle than we tested (avoid the noisy "chiropractor" keyword pattern found above).

## Open question for you

Real data points to **dentists** as the strongest opening niche (highest, cleanest outlier signal). Do you want the first 3-5 videos to target dentists specifically, or do you want to stay broader across health practitioners for other reasons (existing client mix, personal network, etc.)?

---
Sources checked:
- [Local SEO for Healthcare Providers - Get More Patients through Google!](https://www.youtube.com/watch?v=g4aPdWqKHdY)
- [Google Business Profile Review Hacks That Help Chiropractors Rank First](https://www.youtube.com/watch?v=5qcIQ_d048Q)
- [Step-By-Step Guide: How Chiropractors Can Rank Higher on Google Maps](https://www.youtube.com/watch?v=1eCGfVKjo44)
- [Chiropractor SEO: How to Rank #1 on Google (Complete 2025 Guide)](https://www.youtube.com/watch?v=WDs0CqGX4xc)
- [Physical Therapy Google My Business - 6 Ways to Get Patients](https://www.youtube.com/watch?v=c8RcgKrp594)
- [How to Market Your Medical Practice | Sean Garner on Private Practice Growth, SEO & Patient Funnels](https://www.youtube.com/watch?v=pz6GKwgLJjk)
- [How to Get More Patients Without Paid Advertising](https://www.youtube.com/watch?v=GSYzfGau0J0)
