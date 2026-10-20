# 04 GBP and website change risks: extract

Research date: 2026-10-13. Sources: 16 files in `sources/`. Dated sources range from 2026-07-15 to 2026-10-08. Google help and Search Central pages are living pages, fetched on 2026-10-13.

Evidence levels used below:
- **Official**: Google help or Search Central text.
- **Test**: agency test or case with before/after data (mostly Sterling Sky).
- **Anecdote**: forum threads and news reports without controlled data.

## Risk table

### Google Business Profile

| Change type | Risk | What can happen | Lock? | Safe procedure | Source slug(s) |
|---|---|---|---|---|---|
| Primary category | High | Ranking drop overnight (case: position 1 to 31). Re-verification. Suspension reports after category switches. | Yes | Agency only. Ranking grid scan before. Change one field only. Scan again after 3 to 7 days. Revert fast if the drop is large. | sterlingsky-gbp-category-and-url-tests, google-gbp-edit-help, lsf-suspension-threads-2026 |
| Secondary categories (add or remove) | Medium to high | Re-verification possible. Lost relevance for removed category terms. Categories used as keywords break guidelines. | Partial (removal locked, additions reviewed) | Agency review. Use only categories that describe what the business is. One change per batch. | google-gbp-guidelines, google-gbp-edit-help |
| Business name | High | Re-verification. Suspension if keywords or cities are added. Google can reject the edit or remove words. User edits can also change the name. | Yes | Change only to the real-world name on the sign and the website. Update sign, website and citations first. Agency submits. | google-gbp-guidelines, google-gbp-edit-help, ser-gbp-suggested-edits, ser-gbp-sept-2026-changes |
| Address / move | High | Re-verification is mandatory. Rankings shift to the new area. Profile problems on long moves. Duplicate profiles. | Yes | Written move plan. Update website, schema and citations. Save review count, IDs and ranking grid. Edit the existing profile; do not create a new one. | sterlingsky-gbp-address-move, google-gbp-edit-help |
| Show / hide address, switch to service area | High | Suspension for visible home address. Re-verification. Ranking change. | Yes | Agency decision only. Check eligibility (staffed location with signage). Prepare proof documents before any change. | google-gbp-guidelines, lsf-suspension-threads-2026 |
| Map pin | High | Ranking change by proximity. Pins can also move through Google bugs. | Yes | Agency only. Check the pin in monthly monitoring and after every address edit. | ser-gbp-sept-2026-changes, sterlingsky-gbp-address-move |
| Website URL (GBP link) | Medium to high | Local pack ranking change (up or down). Linking to the best organic page can cost the organic result. "Accepted" edit can show late. | Yes | Agency only. Keep the homepage as default unless tested. Add UTM tags. Confirm the live link on Maps. | sterlingsky-gbp-category-and-url-tests, lsf-suspension-threads-2026, google-gbp-edit-help |
| Primary phone number | Medium to high | Re-verification reported for core fields. Mismatch with the website weakens trust. Number must be under the business's control. | Partial | Agency review. Use a local number the business controls. Change the website at the same time. | google-gbp-guidelines, google-gbp-edit-help |
| Hours (regular) | Low to medium | Wrong hours confuse users. Longer real hours can help rankings. AI-converted hours can be wrong. | No | Client may edit. Agency checks the result on Maps. Website hours must match. | google-gbp-guidelines, sterlingsky-gbp-category-and-url-tests, ser-gbp-sept-2026-changes |
| Special / holiday hours | Low | Little ranking risk. Wrong data annoys users. | No | Client may edit freely. | google-gbp-guidelines |
| Services list | Medium | Services influence ranking. Odd service names hurt relevance. Forum reports of suspension during service edits (pre-window, anecdote). | Partial (ranking services locked) | Client can add services with review. Removal of a ranking service needs agency approval. | sterlingsky-gbp-category-and-url-tests, lsf-suspension-threads-2026 |
| Description | Low to medium | Edit can be rejected for links, prices, promotions or gimmicky text. No 2026 evidence that keyword use in the description causes suspension. | Partial (core keyword kept) | Client may reword. Max 750 characters. No URLs, prices or offers. HWG check for health clients. | google-gbp-guidelines, google-gbp-edit-help |
| Google Posts | Medium | Post removed for unverified phone, email or social handles, or unrelated links. Repeated rejections can lead to restrictions (anecdote). | No (pre-check) | Client may draft. Pre-check: no contact data in text, use buttons, link to own site only, HWG check. | ser-gbp-posts-and-content-policy |
| Photos (incl. bulk uploads) | Low to medium | Photos must meet guidelines. No 2026 in-window evidence for suspension from bulk uploads. | No | Client may upload real photos. Spread large uploads over days. Storefront photo with the exact name sign helps verification. | ser-gbp-sept-2026-changes |
| Many edits in a short time | Medium | Older forum advice: fast, simultaneous core edits look suspicious. No in-window test data. | n/a (process rule) | Batch only one core field per batch. Wait for "live" status before the next core edit. | lsf-suspension-threads-2026, google-gbp-edit-help |
| Managers and owner accounts | High (structural) | An account-level restriction can hit all profiles on that account. Removing the last user can lose the profile. | Yes | Client stays primary owner. Agency is manager on one trusted account. Never remove the last owner. | lsf-suspension-threads-2026, google-gbp-guidelines |
| User-suggested edits by the public | Medium | Google may publish a user edit after 4 days without owner answer, if the website supports it. | n/a (monitoring) | Check notifications at least every 2 to 3 days. Keep the website current, because Google uses it as evidence. | ser-gbp-suggested-edits |
| Support requests and appeals | Medium | "Misuse of support channels" policy: repeated unfounded requests can block all future support. Appeals are scarce. | Yes | Agency only. One well-documented appeal. No repeat tickets. | ser-gbp-sept-2026-changes, lsf-suspension-threads-2026 |

### Website

| Change type | Risk | What can happen | Lock? | Safe procedure | Source slug(s) |
|---|---|---|---|---|---|
| URL / slug change | High | Lost rankings and links if no redirect. Weeks of fluctuation even with redirects. | Yes | Agency only. 301 map from old to new URL. Update internal links and sitemap. Keep redirects at least one year. Monitor for several weeks. | google-site-move-url-changes |
| Page removal | High | Lost signals and rankings. Redirect to the homepage is not a safe default. | Yes | Agency decision. Redirect to the most relevant page or merge content. Delete only as last resort. | google-site-move-url-changes, google-core-updates-and-ai-content |
| Title tag: remove keyword or location | High | Title keywords and location terms have measured ranking effect. Removal likely costs rankings (inference). | Partial (keyword locked, wording free) | Client may reword around the locked keyword. Agency checks before publish. | sterlingsky-title-tag-test |
| H1: remove keyword | Medium to high | Same logic as the title. No in-window test data for H1 alone. | Partial | Same as title: keyword locked, wording free. | sterlingsky-title-tag-test (inference) |
| GBP landing page content (homepage or linked page) | High | The page feeds GBP relevance and the AI version of the GBP panel. Old facts appear in AI summaries. | Partial | Keep NAP, hours and services identical to GBP. Agency review for every change. | ser-ai-overviews-ai-mode-sept-2026, google-ai-features, sterlingsky-gbp-category-and-url-tests |
| Full content rewrite | Medium | Can help or hurt. Google warns against quick fixes. AI-written text needs a fact check. | Partial | Section-by-section changes. Keep locked keywords and entities. Measure 14+ days. HWG and legal check. | google-core-updates-and-ai-content |
| New location / city pages | High | Thin pages with swapped city names match the doorway and scaled-content patterns. | Yes | Agency builds them. Each page needs unique local facts. No mass AI pages. | google-spam-policies, google-core-updates-and-ai-content |
| Internal links (nav, footer, removal) | Medium | Internal links help discovery, also for AI features. Keyword-rich footer link blocks look like link spam. | Partial | Client may add contextual links. Removal from navigation and footer changes need agency review. | google-ai-features, google-spam-policies, google-site-move-url-changes |
| Backlinks and press releases with keyword anchors | High | Site-wide demotion in core and spam updates. No message in Search Console. Recovery can take very long. | Yes | No exact-match anchors. No paid links without nofollow or sponsored. Agency controls all link work. | sterlingsky-core-updates-local, google-spam-policies |
| noindex, robots.txt, nosnippet, AI opt-out | High | Page or site disappears from Search or AI answers. | Yes | Agency only. Check after every plugin or theme update. | google-ai-features, ser-ai-overviews-ai-mode-sept-2026, google-site-move-url-changes |
| Structured data (LocalBusiness schema) | Medium | Mismatch with visible text or GBP data. Wrong address or hours spread to AI answers. | Partial | Update together with GBP and visible text. Validate after change. | google-ai-features, sterlingsky-gbp-address-move |
| Small wording changes outside locked elements | Low | Little ranking risk. | No | Client may edit with normal approval. | google-core-updates-and-ai-content |

## Rules for the client approval workflow

1. **Lock the primary category, name, address, pin, service-area setting and GBP website URL.** The client can request a change. Only the agency applies it.
2. **One core GBP field per batch.** Wait until the edit shows "live" on Maps before the next core edit. Google review can take up to 30 days.
3. **"Accepted" is not "live".** Confirm every critical change on Google Maps and Search, and log the confirmation date.
4. **Save the old value before every locked change.** A fast revert restored rankings in the category case. The change log must make a revert possible in minutes.
5. **Take a baseline before every high-risk change.** Ranking grid, review count, profile ID and CID, and Search Console data for the affected URLs.
6. **Use a monitoring window.** GBP: check after 3 to 7 days and after 4 weeks. Website: compare at least 14 days before and after. URL changes: several weeks.
7. **Mark Google update windows in the change calendar.** Do not ship high-risk changes during a running core or spam update. Do not blame a client edit for a drop inside an update window without Search Console proof.
8. **Confirm drops in Search Console before any rollback.** Rank trackers showed false changes in the September 2026 spam update.
9. **Change the website and GBP together.** Name, address, phone, hours and services must match. Google uses the website as evidence for user edits and for the AI version of the GBP panel.
10. **SEO lock on titles and H1s means "keyword stays, wording is free".** The client can rewrite the sentence. The locked keyword and the location term must stay.
11. **No slug change and no page removal without a redirect map.** 301 to the most relevant page. Keep redirects at least one year.
12. **No new city or location pages from the client side.** Each location page needs unique local facts and agency review, or it risks the doorway policy.
13. **Pre-check every Google Post.** No phone numbers, emails or social handles in the text. Links only to the client's own site. HWG check for health clients.
14. **Watch user-suggested edits.** Check profile notifications at least every 2 to 3 days. The owner has only 4 days to reject a suggestion.
15. **Protect account structure.** The client stays primary owner. The agency manages from one trusted account. Never remove the last owner. An account restriction can hit every profile on that account.
16. **One appeal, fully documented.** Prepare proof (sign photo, documents) before the first appeal. Do not send repeat support tickets; Google can now ignore a user who misuses support.
17. **No link work under client control.** No keyword-rich anchors, no paid links without nofollow or sponsored, no keyword press releases.
18. **Technical index settings are agency-only.** noindex, robots.txt, nosnippet and the Search Console AI opt-out can remove a site from Search and AI answers.
19. **Track Maps and organic separately.** A site-wide organic demotion can leave map rankings intact, and the reverse. The cause of a drop is different in each channel.
20. **Low-risk fields stay open.** Special hours, photos and normal copy edits outside locked elements do not need agency approval, only a log entry.

## Evidence gaps (July to October 2026)

- No in-window controlled data on bulk photo uploads, description keywords or edit frequency. The table uses guidelines and older forum consensus for these rows, marked as anecdote.
- No in-window test on removing a keyword from a title or H1. The lock is an inference from tests that add keywords.
- No in-window study that measures AI Overview or AI Mode citation loss after website edits. Google's own guidance (text content, crawl access, current GBP data) is the best available basis.
