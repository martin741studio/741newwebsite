# Johni Jaya Motor: decision card queue (13 Oct 2026)

Result: 30 candidates checked, 7 kept, 23 dropped or moved to other tasks. All 7 cards are draft in `drafts.sql`. Nothing was inserted. Nothing was released.

## (a) Client facts

- Client id: b84427b9-57bc-4145-83fc-ec284d2de785. Contact: Pak Johni. Language: English. Form of address: "you". Martin writes in first person.
- Business: Bengkel Johni Jaya Motor, car repair, Jl. Raya Cilincing No.7, Lagoa, Koja, Jakarta Utara. Site: https://johnijayamotor.com (WordPress, Elementor, Yoast). 30 URLs in the sitemap.
- Not a health client. HWG does not apply. `health_client` = false.
- DB state on 13 Oct: 0 rows in `approval_items`. No row in `client_approval_settings`. `drafts.sql` inserts one (`ON CONFLICT DO NOTHING`).
- Approver: MISSING. `approver_user_id` stays NULL (brief rule). A client login exists: user `ccb8d800-a54e-4439-b74a-2b4c0273ba8d`, display name "Johni Jaya Motor". Martin created it by SQL. The login data went to nobody yet. Until Martin sets the approver and sends the login, Pak Johni cannot decide.
- Program: running since 17 Aug 2026, week 9 (ends 15 Nov 2026). The module UI in English is live per commit 7350ede. I did not test it.

## (b) All candidates

Verification date for all checks: 13 Oct 2026. "curl" means a read of the public page. "Maps" means the public Google Maps page in Chrome. "Form table" means a read-only SELECT on the website database through the read-only Novamira use.

| ID | Idea | Verification | Result | Reason |
|---|---|---|---|---|
| C1 | Opening hours: one set of hours everywhere | Maps weekly hours: Mon to Sat 9.00am to 4.30pm, Sunday closed. Site footer and schema: same. Owner post of 11 Aug on Maps: "Buka setiap hari, 09.00-18.00". Maps search, 9 workshops: 7 close after 16.30 | KEEP (E1) | Real conflict. The 8 Aug note "ask the client" was never answered. The 11 Aug post repeats the wrong wording after the 8 Aug fix |
| C2 | Booking form: spam protection or WhatsApp only | Form table: 1,603 rows, 9 May 2025 to 13 Oct 2026. 0 rows with an Indonesian phone number or email. 0 real enquiries found. No captcha key, no honeypot field | KEEP (E2) | Strong data. Real impact on enquiries |
| C3 | Expired offers on the home page | curl of all 30 sitemap URLs: "EXP 01.03.2026" twice on home. Same offers without end date on 3 service pages. "Lihat Semua Promo" has href "#" | KEEP (E3) | Visible error on the first page. Price class: active yes |
| C4 | WhatsApp button on the home page | curl: 1 wa.me link on home (footer number text, with a "+" in the URL). Service pages have buttons with a typed message | KEEP (E4) | Real design choice with 3 variants |
| C5 | Home H1 with the main search word | curl: H1 "Servis Mobil Cepat, Berkualitas, dan Terpercaya di Jakarta Utara". Search data 90 days: 38 of 65 impressions contain "bengkel", 1 contains "servis" | KEEP (E5) | SEO lock text item. Small numbers, said so in the card |
| C6 | "From" price or fixed price | curl: home and 4 service pages say "Mulai"; balancing page says "Rp50.000 / ban" with no "from". GBP side from Martin's pass today (memory): 3 fixed prices, 2 "from" | KEEP (E6) | Real inconsistency. GBP side not visible in Maps yet. Confirm before release |
| C7 | Method to ask for reviews | Maps: 31 reviews, 5.0. Maps search: 8 of 9 workshops have more (24 to 406, middle 131). Owner replies to reviews: seen in Maps | KEEP (E7) | Reviews are a top lever. Client team does the asking, so the client must agree on the method |
| C8 | GBP secondary categories | Martin's pass 13 Oct, pending Google review | DROP | Done today |
| C9 | GBP services and descriptions | Same pass | DROP | Done today (price type moved to E6) |
| C10 | GBP business description | Same pass | DROP | Done today |
| C11 | GBP booking link to WhatsApp | Same pass | DROP | Done today |
| C12 | GBP name in capital letters | Maps: "BENGKEL JOHNI JAYA MOTOR" | DROP | Name is a locked field (agency only, suspension risk). No ranking proof. Martin decides alone |
| C13 | GBP address shows lowercase "jakarta" | Maps address line | DROP | Address is a locked NAP field. No client choice |
| C14 | Home FAQ section | curl: no FAQ on home. 28 service pages have FAQ | DROP | No variants. Agent can reuse service FAQs. Needs Martin's go for the website change |
| C15 | Real certificates on the home page | curl: no "sertifikat" text on home | DROP | A request for files, not a choice. Goes in the next client message (open item 2 in memory) |
| C16 | Workshop and team photos | Maps shows exterior, inside, video. Home shows 2 detail photos and a logo | DROP | A request for material (task w9, owner client). No variants |
| C17 | English version of the site | GA4 since 1 Jul: 78 sessions, 16 from Indonesia, 28 US, 10 Iran | DROP | No demand data. The traffic looks like bots |
| C18 | Brand spellings (joni, jhony) in the text | Search data: 24 of 65 impressions are brand searches with other spellings | DROP | Numbers are too small. Idea for Martin only |
| C19 | Sunday opening | Part of C1 | MERGED | In E1 |
| C20 | GA4 events for WhatsApp, call, form clicks | GA4 events since 1 Sep: only page_view, first_visit, session_start, user_engagement | DROP | Technical task. Owner Dinakar (needs GTM access, still open) |
| C21 | Submit the sitemap to Search Console | Search Console API: sitemaps list is empty. URL inspection: home "indexed"; spooring, ganti-ban, servis-rem and the hub page "URL is unknown to Google" | DROP | Not a client choice. This is the biggest SEO gap. Needs Martin's go (see section e) |
| C22 | WhatsApp link written as `wa.me/+62...` | curl of home footer | DROP | Technical fix. Owner agent |
| C23 | Booking form time slots (12:00, 01:00, 01:00, 02:00 to 05:00) | curl of the form | DROP | Technical fix. 17:00 slot is after closing. Look at it when E2 is answered |
| C24 | Review replies | Maps: owner replies on the first 4 reviews | DROP | Client does this himself. 741 never replies (rule) |
| C25 | GBP post rhythm and photos each month | Plan task w10 and w11 | DROP | No variants. Plan work |
| C26 | Citations: Indonesian directory set | Plan task w9 | DROP | 741 task. No client choice |
| C27 | Insurer partner links | Plan task w10, owner client | DROP | A request for names, not a choice |
| C28 | Hero and section photo order on home | No data | DROP | Cannot verify. Weak |
| C29 | Home story section ("Dari Garasi Kecil") | curl: text is live and personal | DROP | Works. No reason to change |
| C30 | Trustindex first review is a question about WhatsApp | curl of home | DROP | Tiny. Not a choice |

## (c) Ranked KEEP list

1. E1 Opening hours. Wrong hours send customers to a closed door and hurt the Maps ranking. Three sources disagree.
2. E2 Booking form. The only form on the site is full of spam. Real enquiries can get lost.
3. E3 Expired offers. Old end dates show on the first page. Price class.
4. E4 WhatsApp button. WhatsApp is the booking channel in the Google profile. The home page hides it.
5. E5 Home H1. The home page is the only page that Google shows. The main word "bengkel" is missing in the heading.
6. E6 Price type. Website and Google profile must say the same. Price class.
7. E7 Review method. Reviews drive Maps rank. It needs the team to act.

Ask first: E1, E2, E3.

## (d) Dashboard readiness

Pattern: `client-dashboard-redesign/02-data-readiness-bali.md`. All reads were free reads on 13 Oct 2026.

| Source | Ready | Evidence | Gap | Owner |
|---|---|---|---|---|
| Search Console | YES | The reporting bot is `siteOwner` of `https://johnijayamotor.com/`. Export ran: 90 days to 11 Oct, daily rows since 1 Jun 2025 (497 days). Page data: 408 impressions, 8 clicks, position 7.4, all on the home page | Volume is tiny. Only 65 impressions carry a search term. The sitemap was never submitted. 28 service pages (live since 8 Aug) are unknown to Google | Martin (go for sitemap), agent |
| GA4 | PARTIAL | The bot reads property 488665039. Sessions per month: Jul 28, Aug 19, Sep 20, Oct (1 to 12) 11. Spike of 840 and 858 in Nov and Dec 2025 (likely bots) | Only events page_view, first_visit, session_start, user_engagement. No WhatsApp, call or form events. Since 1 Jul: 78 sessions, 16 from Indonesia. The stream list shows only G-XZCKK6Z6BJ ("JJM"). The tag G-XVWBX0VCMM on the site is NOT in this property. Memory says it is. Check in the GA screen | Martin, Dinakar (GTM), agent |
| Local Falcon free reads | NO | No Local Falcon tools in this session. Memory: connector disconnected, baseline scan blocked. Old scan of 8 Aug (81 points, "bengkel mobil", found on 3, average rank 14, 0% top 3) exists as image and page text only | Reconnect the connector. No stored point data | Martin, then agent |
| Google profile actions (calls, clicks, directions) | NO | Not readable by the bot. Chrome with the 741 login could read the Performance screen. Not tried | Needs the connector or a Chrome read | agent |
| Google profile facts (reviews, hours, posts) | YES | Maps read: 31 reviews, 5.0, hours, owner post of 11 Aug | Count of unanswered reviews not checked | agent |
| Google Ads | NO | No Ads account or spend found in memory or portal | Ask Martin if ads are planned | Martin |
| Leads | NO | Website form is spam only (E2). WhatsApp and call clicks are not tracked | A tracking plan for WhatsApp and calls | Dinakar, agent |
| Portal | YES | 44 tasks (9 done), 1 report, 12 activity rows, 0 decision items | None | none |

## (e) Open gaps

1. Approver is missing (see section a).
2. The 28 service pages are unknown to Google two months after launch. Search Console shows an empty sitemap list. A sitemap submission needs Martin's go, because it changes the client's Search Console account. The robot has owner rights.
3. GA4 tag mismatch (see section d). Fix before the dashboard reads "sessions".
4. E6: the Google profile side comes from today's dashboard pass. The public Maps view did not show the new services yet. Check the price type in the Business Profile Manager before release. If the profile is not as described, rewrite the "why" line.
5. E1 and E4 say what the profile shows. The hours are verified in Maps today. The booking link to WhatsApp is not visible in Maps yet (pending Google review).
6. E2: I scanned all 1,603 rows with filters and read samples. I did not read every word of each row. I found no Indonesian phone number and no Indonesian email. Nobody can see if the owner reads the mail address that receives the form.
7. E5 data is small: 65 impressions with a term. Most search terms are hidden by Google. No search volume was bought (no paid calls).
8. Not checked: how Pak Johni reads the module UI, and the real opening hours (only he knows).
9. Ideas for Martin, not cards: brand spellings (joni, jhony), `wa.me/+62` link, booking-form time slots, certificates request in the next client message.
