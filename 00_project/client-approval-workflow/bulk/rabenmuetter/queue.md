# Rabenmütter Shop: decision card queue (13 Oct 2026)

Internal file. Style: ASD-STE100. Client text lives in `drafts.sql` only.

## (a) Client facts

- Client: Rabenmütter Shop (Franziska Poerschmann). client_id `fbcc70d1-4c56-437c-b5fb-8056e48d3f62`. lang `de`. mode `program`.
- Form of address: **du**. The portal reports, the 4 live guides and the shop newsletter use du. The live homepage mixes forms: "Sie finden hier" (text), "findet Ihr" (meta description), "Habt Spaß" (button), "Du willst" (newsletter). Legal pages use Sie (63 times in the AGB). Cards use du.
- Live site: https://rabenmuetter-shop.com (Shopify, Basic, 366 active products, 25 collections, 16 pages, 1 blog "News" with 4 guides).
- Type: publisher and card shop (e-commerce). NOT a health client. `health_client=false`. No HWG check. `risk_class` is `none` on all cards.
- Approver in the DB: **missing**. No `client_approval_settings` row exists. No `approval_items` rows exist. One client login exists in `profiles`: user_id `8f1dff6f-4c72-476f-96ad-2c4a1b81389e` (Franziska Poerschmann). `drafts.sql` inserts the settings row with `approver_user_id` NULL, as the brief says. The main session must set the user id before the client can decide.
- Shopify access: read works (token has `read_products`, `read_content`, `write_products`, `write_content`). The agent made GET calls only. No write.
- Search data: Search Console URL-prefix property `https://rabenmuetter-shop.com/` holds data from 29 Aug 2026 only. Last data day: 11 Oct.

## (b) All candidates

| ID | Idea | Verification (what, source, date) | Result | Reason |
|---|---|---|---|---|
| C1 | Standard text on product pages: fix typos, write own texts for most-seen cards | Shopify GET of all 366 products (13.10.). Search Console pages 29.08.-11.10. 348 products carry typos "Weihnachen", "kontinuirlich". 265 pages with impressions show it (2,998 impressions). 36 pages with 20+ impressions (1,866 impressions, 21 clicks). Earlier note "rest of catalogue has no value" is out of date | KEEP (E1) | Biggest reach. Real choice between 3 scopes. Uses the batch the client approved on 04.09. as the pattern |
| C2 | Texts for the 6 Trauerkarten (pillar of the plan) | Shopify GET (13.10.): only "Träne" has its own text. 5 cards carry "Und machmal fehlen einem die Worte..." (typo). Search Console: Ballon 54 impressions, position 10.4. Live review on Sternschnuppe: customer expected a fold-out card. Picture of Ballon viewed | KEEP (E2) | Pillar topic. Real wording choice. Fixes the format confusion |
| C3 | Homepage: links to the 4 guides | Homepage HTML (13.10.): only 2 links to `/blogs/news` (menu, drawer), 0 to a guide. Search Console 14.09.-11.10.: homepage 11 of 50 clicks | KEEP (E3) | Strongest page. Three scopes from small to bigger |
| C4 | Menu: place of "Trauerkarten" | Menu HTML (13.10.): 12 sub-items under "Postkarten", Trauerkarten is last. Volume 90,500 from the 30.08. site-tree report. Client approved block 5 "Kategorien & Navigation" on 30.08. | KEEP (E4) | Real structure choice. Stays inside the approved plan |
| C5 | Name of the guide index page ("News") | Live `/blogs/news` (13.10.): title "News – Rabenmütter Shop", H1 "News", no meta description. Menu text "Ratgeber" | KEEP (E5) | Cheap, visible, 3 clear variants |
| C6 | Next guide topic | Volumes 30.08. (site-tree report): Geburt 27,100, Hochzeit 40,500, Trauerkarte Textvorschläge 18,100. Collection "Geburt" has 4 products and no intro. No product mentions "Hochzeit". Guides live: 15.09. and 10.10. | KEEP (E6) | New decision, not in the approved plan. Data 44 days old, inside 3 months |
| C7 | English heading above reviews on the homepage | Homepage HTML (13.10.): H2 "Let customers speak for us". Product pages: "Customer Reviews", "Write a review" | KEEP (E7) | Small, certain, one click. Lowest rank |
| C8 | Form of address across the shop (du / ihr / Sie) | Homepage text and meta (13.10.), pages API (Sie on legal pages) | DROP | No effect on rankings or enquiries that we can show. No data. Ask only if Franziska raises it. Re-open as optional card if Martin wants it |
| C9 | Hand-written card service (Pensaki idea) | Memory 10.10.: Martin has not yet sent his answer. 4 facts missing (who writes, character limit, lead time, surcharge) | DROP | Not ready. Needs a price decision. Martin said the route is a collaboration request. A card now would run ahead of his answer |
| C10 | Etsy as sales channel | `report_feedback` 30.08.: client declined Etsy. Night shift 12.10. confirmed | DROP | Client said no. Task "Etsy-Shop prüfen / aufsetzen" (week 11) is still open in `tasks`. Close it |
| C11 | Pinterest and TikTok shop | Memory 10.10.: both channels "Active", pixels connected (checked in Shopify admin) | DROP | Already done. No choice left |
| C12 | Google Merchant Center / Free Listings | Plan block approved 14.09. Search Console shows 17 product URLs with `product_sync` and `sag_organic` (23 impressions, 4 clicks, 29.08.-11.10.). Page HTML holds Google tags (`AW-798052631`) | DROP | Not a client choice. Listings seem live already. Task week 7 needs a check inside Merchant Center (login needed) |
| C13 | Instagram / Facebook shop reactivation | Plan block approved 14.09. No new data | DROP | No variants to choose. Needs the client's account access |
| C14 | Homepage title, meta description, H1 | Live homepage (13.10.): title "Rabenmütter Shop - Postkarten, Bücher, Papeterie & mehr", H1 is the logo link. Search Console: homepage position 5.5, brand query "rabenmütter verlag" position 2.3 | DROP | Home already ranks well for the brand. No data shows a gain. Block "Startseite" was approved on 30.08. |
| C15 | Weihnachten collection intro | Collection text (13.10.): 97 words, same standard text with the same typos, 23 products. Search Console: 0 impressions for any "weihnacht" query since 29.08. | DROP | Typo fix is inside E1. No demand number in hand. A volume check costs money (DataForSEO). Needs Martin's go. Season starts now |
| C16 | Intro texts for empty collections (Postkarten, Danke, Geburt, Entschuldigung, Gute Besserung) | Collections API (13.10.): 0 words each. Search Console: 1 to 9 impressions each | DROP | Too small. Revisit after E1 |
| C17 | Title "Trauerkarten ohne Worte" for the hub collection | Collection (13.10.): title and H1 "Trauerkarten ohne Worte", 36-word intro with 2 guide links. Search Console: 6 impressions, position 6.8 | DROP | No saved volume for the head term "trauerkarten". Cannot give a real "why" line |
| C18 | Rename blog URL `/blogs/news` to `/blogs/ratgeber` | The site-tree report names `/blogs/ratgeber/…`, the live guides sit in `/blogs/news/…` | DROP | A URL change needs 301 redirects. The guides are 4 weeks old. Risk is higher than gain. Fix the report text instead |
| C19 | Make "Trauersprüche" longer (395 words, average position 45) | Shopify articles API (13.10.): 395 words. Search Console: 48 impressions, position 45.2 | DROP as card | Not a client choice. 741 work item for the agent (memory: guides must be long for topic strength) |
| C20 | Image alt text for the full catalogue | Plan task week 4 | DROP | No choice. Plan task |

Counts: 20 candidates, 7 kept, 13 dropped.

## (c) Ranked KEEP list

1. **E1** Standard text on product pages. Widest reach: 36 cards with 1,866 impressions still carry the typos.
2. **E2** Trauerkarten texts (Ballon as pattern for 5 cards). Pillar topic. Fixes a real customer confusion.
3. **E3** Homepage links to the 4 guides. The homepage is the page with most clicks and has no direct guide link.
4. **E4** Menu place of "Trauerkarten". Sitewide internal link. Needs the client's taste.
5. **E6** Next guide topic. Future gain. Data is from 30.08.
6. **E5** Name of the guide page ("News"). Cheap and visible.
7. **E7** English heading above reviews. Trust detail. One click.

Note: codes follow the order in `drafts.sql` (E1 to E7). The rank above differs for E5 and E6. Martin may re-order the grill.

## (d) Dashboard readiness

Read today, free reads only, 13 Oct 2026.

| Source | Result | Evidence | Gap | Owner |
|---|---|---|---|---|
| Search Console | **yes** (partial history) | Reporting bot is `siteFullUser` on `https://rabenmuetter-shop.com/` (sites list, 13.10.). Daily rows from 29.08. to 10.10.: Sep 72 clicks and 3,096 impressions, 1-10 Oct 12 clicks and 1,103 impressions. Queries and pages read | The bot has no access to the domain property `sc-domain:rabenmuetter-shop.com` (HTTP 403). That property holds the 16 months of backfill. Monthly report 1 shows 60 clicks (28 days) and the bot shows 50: the two properties differ. Memory note "bot is not shared" is out of date for the URL-prefix property | Martin: add the bot to the domain property |
| GA4 | **no** | Property 324012581 ("Rabenmutter Shopify"). Bot gets HTTP 403 on `runReport`. The bot sees 40 properties and none is this one. We hold only the Editor role | Sessions, purchases and bot filtering are not readable. Manual read in Chrome is the only way today. The page HTML holds 2 GA4 IDs (`G-WV1CKP6TB8`, `G-XCYT2YZQ3J`): not checked which one is the property stream | Martin: ask Franziska for Admin, or a Viewer grant for the bot |
| Shopify orders and revenue | **no** | Orders count call returns 403: "requires merchant approval for read_orders scope". Same for customers and marketing events. Current scopes: read and write products and content | Revenue, order count and average order value are not readable. This is the key metric for a shop | Martin: re-authorize the "741 SEO" app with `read_orders` (flow in memory `shopify-admin-api-rabenmuetter`) |
| Shopify products and content | **yes** | 366 products, 25 collections, 16 pages, 4 articles read via Admin API | None | agent |
| Google free product listings | **partial** | 17 `product_sync` URLs, 23 impressions, 4 clicks in Search Console (29.08.-11.10.) | No view into Merchant Center | Martin (needs login) |
| Local Falcon | **no (not relevant)** | Online shop. No Google Business Profile was checked | Nothing to feed | none |
| Ads account | **no** | No Ads account is known. Page HTML holds tag `AW-798052631` | Not checked if an account exists or spends | Martin |
| Rank per keyword | **partial** | Search Console gives average position per query. DataForSEO is paid. Memory: the server IP `179.65.205.159` is not whitelisted | No weekly keyword tracker | Martin (whitelist IP, then paid go) |
| Backlinks | **partial** | Old snapshots in the monthly report (53 referring domains in Sep) | New numbers need a paid call | Martin (paid go) |
| Social channels (Pinterest, TikTok) | **no data feed** | Channels active (memory, 10.10.) | No API read | none |
| Portal state (tasks, reports, feedback) | **yes** | 30 tasks, 4 reports, 16 feedback rows read | Tasks hold stale rows: "Etsy-Shop prüfen / aufsetzen" (client said no) and "GA4-Tracking einrichten" (GA4 exists). | Dinakar or agent |

## (e) Open data gaps and things I could not verify

1. **Approver missing.** Set `approver_user_id` to `8f1dff6f-4c72-476f-96ad-2c4a1b81389e` after Martin agrees. Until then, Franziska cannot decide.
2. **"Nicht zum Aufklappen" (E2).** This wording comes from one review and the entry "A6 - Postkarte". We did not hold the card. The card asks Franziska to confirm. The review is from 2025 (older than 3 months). The live page check on 13.10. is the data date.
3. **Volumes for E4 and E6** are from 30.08. (DataForSEO, 44 days old). No fresh volumes. No paid call was made.
4. **Weihnachten.** No demand number. Season starts now. Martin decides on a paid volume check.
5. **Google Merchant Center.** Cannot see inside it. The `product_sync` URLs suggest it works.
6. **GA4 stream.** Two measurement IDs on the page. Not checked which one belongs to the property.
7. **The 20 products approved on 04.09.** Only 8 have a rewritten body text. 12 got title, meta and alt text only. E1 label says "wie bei den 20 Karten vom 4. September". The wording is true for title and meta. It is not true for body text on 12 of them.
8. **Site-tree report (clients.741.studio/r/5a409bfd9db5)** still lists Etsy and `/blogs/ratgeber/` URLs. It needs a correction.
9. **Standup 13.10.** flags: client asked for help 1 time (answer open), 6 overdue tasks, onboarding 2 of 6, "no NAP data". NAP does not apply to an online shop.
10. **Guide strength.** "Trauersprüche" has 395 words and average position 45. Treat as a 741 work item.
11. The bot fetch of live pages was blocked once at the end ("Verifying your connection"). All numbers above were read before that block.
