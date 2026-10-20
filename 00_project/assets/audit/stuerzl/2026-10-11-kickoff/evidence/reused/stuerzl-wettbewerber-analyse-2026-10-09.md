# STÜRZL Steuerstrafrecht: Competitor reverse-engineering and 90-day roadmap

Date: 09.10.2026. Internal. Not for the client. All numbers have a date and a source.
Sources: DataForSEO (Maps SERP, Reviews, Backlinks), our Local Falcon scans of 17.09. and 01.10.2026, live fetch of the competitor sites on 09.10.2026.
Raw data: scratchpad `comp/` (maps_*.json, reviews_*.json, bl_*.json, home_*.html).

## 0. Scope and assumptions

The prompt had open fields. I filled them like this.

| Field | Value |
|---|---|
| Trade | Steuerstrafrecht (tax criminal law), law firm |
| Markets | Frankfurt am Main and München |
| Our site | stuerzl-steuerstrafrecht.de |
| Frankfurt outlier | RA Michael Hepp (anwalt-steuerrecht-frankfurt.de). Chosen because he has 13 reviews and still wins. |
| Frankfurt benchmark | DREYENBERG Rechtsanwälte Steuerberater (dreyenberg.com). Most reviews among the tax specialists, best SoLV. |
| München outlier | Kanzlei WILD, Dr. Katharina Wild (wild.legal). 14 reviews. Rank 1 for "anwalt steuerhinterziehung münchen". |
| München benchmark | Kanzlei Günther (kglaw.de). Rank 1 for "anwalt steuerstrafrecht münchen". 136 reviews. |

Limits of this audit:
- We have no GBP access. Services, description, posts, attributes and Q&A of all profiles are not readable.
- We have no München grid scan. München data are point rankings from DataForSEO, not a grid.
- Domain age is estimated from the first backlink seen. The Wayback Machine was offline.
- A correlation is not proof. "Outlier factors" are the most likely drivers, not certain ones.

## 1. Competitor breakdown and key outlier factors

### 1.1 Frankfurt

Our scan data (Local Falcon):

| Provider | 17.09. "anwalt steuerstrafrecht" SoLV | 01.10. best keyword | Reviews |
|---|---|---|---|
| DREYENBERG | 61,7 % | 100 % "anwalt steuerhinterziehung" | 83 |
| Hepp | 56,8 % | 85,7 % "anwalt steuerhinterziehung", 73,5 % "fachanwalt steuerrecht" | 13 |
| STÜRZL | 14,8 % | 63,3 % "anwalt steuerhinterziehung", 2,0 % on four others | 14 |

GBP signals (DataForSEO 09.10.2026, Reviews task same day):

| Signal | Hepp | DREYENBERG | STÜRZL Frankfurt |
|---|---|---|---|
| Name | "Rechtsanwalt Michael Hepp - Fachanwalt für Steuerrecht" | "DREYENBERG Rechtsanwälte Steuerberater" | "STÜRZL Steuerstrafrecht" |
| Primary category | Anwalt für Steuerrecht | Anwalt für Steuerrecht | Rechtsanwalt (Lawyer) |
| Other categories | Strafverteidiger, Anwalt, Rechtsanwalt | none | none |
| Reviews / rating | 13 / 5,0 | 83 / 5,0 | 14 / 5,0 |
| Reviews last 12 months | 3 | 20 | not retrieved (API error) |
| Reviews last 3 months | 1 | 5 | not retrieved |
| Owner replies in last 40 | 0 | 3 | not retrieved |
| Photos | 2 | 3 | 7 |
| Review text mentions "steuer" | 3 of 13 | 20 of 40 | n/a |

Authority (DataForSEO backlinks, 09.10.2026):

| Domain | Rank | Backlinks | Ref. domains | First seen | Real links |
|---|---|---|---|---|---|
| anwalt-steuerrecht-frankfurt.de | 132 | 330 | 125 | 01/2019 | Almost none. A sister domain, hepp-steuerstrafrecht.de (5 links). The rest is spam. |
| dreyenberg.com | 204 | 959 | 817 | 06/2022 | Few: steuer-berater.de, steuerarbeit.de, directories. One site gives 107 links. |
| stuerzl-steuerstrafrecht.de | 122 | 100 | 58 | 01/2024 | bestlawyers (13), anwaltauskunft (4), tax-talents. About 40 spam domains. |

**Key outlier factors, Frankfurt (most likely first):**
1. **Category match.** Hepp and DREYENBERG have "Anwalt für Steuerrecht" as primary category. STÜRZL has "Lawyer". All top-4 providers in the 17.09. scan had "Tax attorney". This is the same finding as in the first scan, and it still holds.
2. **Hepp has a cheap, complete topic set.** The category pair "Tax attorney + Criminal justice attorney" covers both "steuer" and "straf" queries. His GBP name carries "Fachanwalt für Steuerrecht". His home title carries "Anwalt für Steuerrecht + Steuerstrafrecht in Frankfurt". Both match the query words.
3. **Hepp's money page is deep.** `/fachgebiete/steuerstrafrecht/` has about 2.000 words with five question headings (Strafe, Verjährung, Selbstanzeige). Title: "Rechtsanwalt für Steuerstrafrecht in Frankfurt | Michael Hepp".
4. **Exact-match domain** since 2019 plus a sister domain on steuerstrafrecht.
5. **Not the cause:** photos (Hepp has 2), reviews (13), links (spam), schema (Hepp has none beyond WebPage).
6. DREYENBERG adds review velocity (20 in 12 months, text mentions "steuer" in half of them), a large firm site with 101 internal links, JUVE, Chambers and Legal 500 badges, and DE/EN hreflang.

### 1.2 München

Maps SERP, 09.10.2026, center Marienplatz, DataForSEO (point ranking, not a grid):

| Query | 1 | 2 | 3 | STÜRZL |
|---|---|---|---|---|
| anwalt steuerstrafrecht münchen | Kanzlei Günther | Heindl Fachanwälte | ROSE & PARTNER | not in top 10 |
| anwalt steuerhinterziehung münchen | Kanzlei WILD | ROSE & PARTNER | Glock Liphart Probst | **rank 8** (1 review) |

| Signal | WILD | Günther | STÜRZL München |
|---|---|---|---|
| Primary category | Strafverteidiger or Anwalt für Steuerrecht (changes per query) | Strafverteidiger | Rechtsanwalt |
| Other categories | Anwalt, Anwaltskanzlei | Anwaltskanzlei, Rechtsanwalt | none |
| Reviews / 12 months | 14 / 4 | 136 / 23 | 1 / 1 |
| Owner replies | 0 | 17 of 40 | 0 |
| Photos | 6 | 12 | 1 |
| Ref. domains | 90 | 167 | 58 (shared domain) |
| Real local links | **muenchen.de (84 backlinks, rank 56), in-muenchen.de (16), ra.de, bestlawyers, brainguide** | directories, spam | see Frankfurt |

**Key outlier factors, München:**
1. **WILD has local authority links.** muenchen.de and in-muenchen.de are city portals. This is the only clear local-link advantage in our sample.
2. **Topic depth.** The WILD sitemap has 132 URLs: 58 news articles (Selbstanzeige, Durchsuchung, Rechtshilfe, FAQ Steuerstrafrecht) plus a full English copy. The home page names Handelsblatt, WirtschaftsWoche and F.A.Z. Institut.
3. **Title and meta match the query.** Title: "Anwalt Steuerstrafrecht München | Kanzlei Wild". Meta lists Selbstanzeige, Steuerhinterziehung, Betriebsprüfung.
4. **Günther wins on volume and conversion.** 23 reviews in 12 months, owner replies, WhatsApp button (12 mentions), contact form, sticky CTA, FAQPage and LegalService schema with `areaServed`. The home page says "München" 18 times.
5. STÜRZL München already ranks 8 for "steuerhinterziehung" with one review. The brand name carries it. The profile has almost no other signals yet.

## 2. Technical and on-page gap matrix

Fetched 09.10.2026. "Home" means the home page only.

| Signal | Hepp | DREYENBERG | WILD | Günther | **STÜRZL** | Gap |
|---|---|---|---|---|---|---|
| Title tag | "Anwalt für Steuerrecht + Steuerstrafrecht in Frankfurt \| …" | "DREYENBERG – Startseite" | "Anwalt Steuerstrafrecht München \| Kanzlei Wild" | "Strafverteidiger in München \| …" | "Stürzl Steuerstrafrecht – Home" | **High.** No service, no city. |
| H1 | service + city | focus statement | firm statement | "Ihre Strafverteidiger in München" | "Kanzlei" | **High** |
| Home words | 318 | 1.021 | 1.399 | 1.156 | 410 | Medium |
| Service pages | 3 (Steuerrecht, Steuerstrafrecht, Betriebsprüfung) | many | Steuerrecht, Strafrecht + 58 articles | many | 9 + 17 sub pages, thin (114–376 words), 2×H1 | **Quality gap, not a count gap** |
| Money page depth | ~2.000 words, FAQ headings | big | news depth | FAQ block | none above 376 words | **High** |
| Nav label "Steuerstrafrecht" | top level | submenu | top level | submenu | only inside "Leistungen" | Medium |
| München page | – | – | Munich in title and text | Munich 18× | Munich only in schema text and footer | **High** |
| Schema | WebSite, WebPage, Breadcrumb | Organization, Person, Article | Breadcrumb only | LegalService, FAQPage, `areaServed`, Person | LegalService (Frankfurt only), `areaServed`, `geo`, hours 09–18 | Medium: add München, fix hours, add FAQ |
| Image alt text | none | 10 of 10 | 9 of 77 | 9 of 13 | 3 | Low |
| Contact form | link to form | link | none on home | form + 7 tel links + WhatsApp | **none** | **High** |
| Sitemap | yes (2 files) | yes | yes (132 URLs) | yes | **404** | **High**, quick fix |
| Hreflang / EN | no | DE/EN | DE/EN | no | no | Low (bundesweit/International wish) |
| Response time (TTFB, one fetch) | 1,8 s | 3,0 s | 2,0 s | 2,4 s | 2,6 s | Same level. Our LCP of 7,2 s is the real issue. |
| GBP link tracking | UTM on GBP link | UTM | – | – | not set | Quick fix |

**Hidden or unconventional signals.** I looked for keyword stuffing in alt text, footers and hidden elements. I found nothing unusual in the five sites. The hidden elements are normal menus. Two things stand out instead:
- Hepp puts profession and topic into the **GBP name** and the **title**, and owns a keyword domain. DREYENBERG does not (its title is "Startseite"), so this is not a rule.
- Kanzlei WILD shows a different primary category per query in Maps. Google chooses the label from the categories on the profile. Several matching categories widen the query range.

**Do not copy:** Hepp's emoji in the meta description, WILD's split headings ("steuer recht", "straf recht") and hidden JavaScript notices. They add risk and no proven value.

### Gaps against our own site

**Content and page gaps**
- No München page with the real office (Oberanger 32), team contact and local context.
- No page that matches "Steuerfahndung / Durchsuchung" as an acute-case page. Demand: "steuerfahndung" 6.600 per month nationwide, 210 in Frankfurt.
- Service pages are thin and have two H1 each. Hepp's single deep page beats our nine thin ones.
- No articles that match WILD's 58-article base. We have a strong FAQ (6 pages) that is not linked from the service pages.
- Suburb pages (Offenbach, Wiesbaden, Bad Homburg): no competitor in our sample has them. **I do not recommend them.** One office and no real local presence would look like doorway pages.

**Local authority gaps**
- No city-portal links (muenchen.de, in-muenchen.de). WILD has 84 from one portal.
- 15 unlinked press mentions exist (LTO ×4, JUVE ×2, ZRI ×2, RWS, azur, Capital, BMF-PDF, IWW, C.F. Müller, R&W and others). None is a link yet. This is our cheapest authority win.
- Citations carry the old address and some errors (Infobel "Frankfurt (Oder)", Cylex München wrong street, anwalt.de "RAK Köln").
- About 40 spam backlinks since 07/2026.

**Conversion and UX gaps**
- No contact form and no callback. Günther has a form, a sticky mobile call button and a WhatsApp button.
- Opening hours conflict: GBP 09:00, website phone 09:30–14:30, schema 09:00–18:00.
- No emergency path on the page for "Durchsuchung läuft gerade". The two emergency mobile numbers sit on the contact page only.
- LCP 7,2 s on mobile (892 KB images, 35 JS and 13 CSS files).
- Tracking is now fixed: tel, mailto and chat clicks (GTM version 4, 09.10.).
- Do not copy the WhatsApp button without a legal check. Mandate data in WhatsApp is a confidentiality and GDPR risk (§203 StGB).

## 3. Rules for every action (law firm)

- No success promises, no "Spezialist" or "Experte" claims unless the title is formally held. Check §43b BRAO, §7 BORA and the Fachanwalt rules (FAO) before every text.
- Add "Fachanwältin" to the GBP name or site **only** if Dr. Stürzl holds that title. Not verified. Ask first.
- No keyword stuffing in the GBP name. The name "STÜRZL Steuerstrafrecht" already contains the topic and is the real firm name. Keep it.
- Reviews: no incentives, no gating, no fake reviews. Anonymity matters to the client. Owner replies can reveal that a person is a client. The client answers reviews herself, or not at all.
- Lead data: contact data, source and status only. No case details.
- No change on the website, GBP or Ads account without Martin's go **per change**.

## 4. 90-day roadmap (Day 1 = start of program week 1)

Gate marks: **[GO]** needs Martin's go. **[ACCESS]** needs access we do not have. **[CLIENT]** needs a client answer.

### Days 1–30: Foundation and technical fixes

| Week | Actions | Gate |
|---|---|---|
| 1 | Freeze the address: Untermainkai 26 is the proposed canonical address. Ask Frau Jilg for final confirmation. Confirm that Dr. Stürzl is primary owner of both GBP profiles. Record the GBP baseline (categories, services, hours, photos) as soon as access is there. | [CLIENT] [ACCESS] |
| 1 | GBP Frankfurt and München: primary category "Anwalt für Steuerrecht". Add "Strafverteidiger" and "Rechtsanwalt" as secondary. Check each against real practice. | [GO] [ACCESS] |
| 2 | GBP: move the address to Untermainkai 26. Risk: an address change can trigger re-verification and a short suspension. Do it in one planned step, with video verification ready. | [GO] [CLIENT] |
| 2 | GBP: services list (Selbstanzeige, Steuerfahndung und Durchsuchung, Steuerstrafverfahren, Betriebsprüfung, Wirtschaftsstrafrecht, Compliance), 750-character description with no claims, one hours value everywhere, UTM on the website link, 15+ real photos for Frankfurt (entrance, rooms, with consent) and 10+ for München. | [GO] [ACCESS] |
| 2 | Site: add `sitemap.xml`, add the sitemap line to robots.txt, fix the 404 `/schwerpunkte` and 4 dead links. | [GO] |
| 3 | Site: new title, H1 and meta for the home page. Example: "Anwalt für Steuerstrafrecht Frankfurt und München | STÜRZL". Single H1 on every page. | [GO] |
| 3 | Schema: LegalService for Frankfurt and for München as separate entities, Person with real credentials only, `sameAs` (anwalt.de, RAK, LinkedIn), one opening-hours value. | [GO] |
| 3–4 | CRO: contact form and callback request that write into the portal "Anfragen" tab (already built on staging). Sticky call button on mobile. Emergency block "Durchsuchung / Festnahme: sofort anrufen" with the emergency numbers. Speed: compress images, remove unused JS and CSS. | [GO] [CLIENT] |
| 4 | Review workflow starts: a short, neutral, consent-based request card, handed over personally after a finished mandate. Goal: steady flow, not a number. | [CLIENT] |
| 4 | Day-30 scans: Frankfurt 7×7 at the new address, plus the first München scan, same eight keywords. Local Falcon credits are used. | [GO] |

### Days 31–60: Content and architecture

| Week | Actions | Gate |
|---|---|---|
| 5 | Build the "Steuerstrafrecht" pillar page (1.500–2.000 words, real FAQ, own H1, case flow, costs, no promises). Rebuild it as a replacement, not an in-place edit. | [GO] |
| 5–6 | Acute-case page "Steuerfahndung und Durchsuchung": what to do in the first hour, rights, emergency number. | [GO] |
| 6 | Page "Selbstanzeige" (anwalt.de is the main lead source here, so match its questions). | [GO] |
| 6–7 | München page: office at Oberanger 32, access, contact person Lea Wimmer, services. Unique text, not a copy of the Frankfurt page. | [GO] [CLIENT] |
| 7 | Merge the thin pages: nine areas into six strong pages (Steuerstrafrecht, Selbstanzeige, Steuerfahndung/Durchsuchung, Betriebsprüfung, Wirtschaftsstrafrecht und Compliance, Zoll/Schwarzarbeit/Sozialversicherung). Keep URLs or add 301 redirects. | [GO] |
| 7–8 | Internal linking: home → pillar → sub pages. Each FAQ page links to its money page with a descriptive anchor. "Steuerstrafrecht" becomes a top-level menu label. Footer links to the six pages and both offices. | [GO] |
| 8 | Two articles from real demand: "steuerhinterziehung strafe" (4.400/month) and "steuerhinterziehung verjährung" (2.400). Text by Dr. Stürzl or Dr. Glogger, checked for Berufsrecht. | [CLIENT] |
| 8 | Day-60 scan, same setup. Compare to day 30. | [GO] |

### Days 61–90: Authority, reviews and AI visibility

| Week | Actions | Gate |
|---|---|---|
| 9 | Link reclamation: write to the 15 unlinked mentions (LTO, JUVE, ZRI and others) with a friendly request to add the link. | [GO] |
| 9–10 | City portals and directories: muenchen.de and in-muenchen.de listing (check cost and rules), ra.de, anwalt.de profile (fix "RAK Köln"), Frankfurt and München directories with the new address. Fix Infobel and Cylex entries. | [GO] [CLIENT] |
| 10 | Publication plan: one guest article or interview per month in a professional outlet. Sponsoring only if it passes the Berufsrecht check. | [CLIENT] |
| 10–11 | Spam links: collect the list (Tab 08 of the sheet). Disavow only after a manual check. Google ignores most of it, so this is low priority. | [GO] |
| 11 | AI visibility: `llms.txt`, FAQPage schema on the six pages, short answer blocks under each question, same name and address everywhere. Test 10 queries in Google AI Overviews, ChatGPT and Perplexity and record the result. | [GO] |
| 12 | Review check: count, speed, wording. Adjust the workflow. | – |
| 13 | Day-90 scans and the final report. Tracking review: chat, phone and email clicks, form leads, lead statuses in the portal. Return signed mandates to Google Ads as offline conversions (only through `gclid`, no audience lists). | [GO] |

### What we measure (baseline today)

| Measure | Baseline | Source |
|---|---|---|
| SoLV "anwalt steuerhinterziehung" Frankfurt | 63,3 % | Scan 01.10. |
| SoLV "anwalt steuerstrafrecht" Frankfurt | 2,0 % (7×7), 14,8 % (9×9, 17.09.) | Scans |
| München "anwalt steuerhinterziehung" | rank 8, 1 review | DataForSEO 09.10. |
| Organic position, "anwalt steuerstrafrecht" | 27 (Frankfurt) | SERP 08.10. |
| GA4 key events | phone_click 19, email_click 40 in 28 days | GA4 09.10. |
| Reviews | 14 Frankfurt, 1 München | Maps 09.10. |

I make no promise about results. The plan removes the gaps we can show with data.

## 5. Open questions for Martin

1. Does Dr. Stürzl hold the Fachanwalt title? This decides the name, title and schema text.
2. Is the München office in the paid package? The portal lists one location.
3. Local Falcon credits for the day-30 München scan: go?
4. Should I retry the Frankfurt review fetch for STÜRZL (it failed with an API error)?
