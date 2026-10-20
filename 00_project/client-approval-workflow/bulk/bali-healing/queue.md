# Bali Healing: decision queue (13 Oct 2026)

## (a) Client facts
- Language: English. Martin writes in first person. HWG does not apply (Indonesia). Google health policy and the client rules apply.
- Live site: https://www.balihealing.com (Wix). 58 URLs in the sitemap.
- Health client: `client_approval_settings.health_client = true`. This setting forces `hwg_checked` before release, although HWG does not apply. Martin sets `hwg_checked` at release with a note "HWG n/a". The row was not changed.
- Approver: set. Row exists (shared client login, name "Bali Healing Team", auto_approve_consent false). Checked by select on 13 Oct.
- Items in the database: 0. Decisions: 0.
- Client rules: no prices, no doctor names, no country references, no disease promises. Peggy and Pasha are the contacts.
- Blocker before release (not verified today): the client-facing decision module may show German text only. The English text is in `client-approval-workflow/portal/src/ap.js`. Check this before "An Kunde geben".

## (b) All candidates

| ID | Idea | Verification | Result | Reason |
|---|---|---|---|---|
| C1 | IV page name "IV Drip" | curl 13 Oct: title "IV Drip Therapy & Infusions", H1 "IV Drip Therapy & Infusions in Canggu, Bali" | DROP | Already live (Pasha). |
| C2 | Business name in the Google profile | `bali-client-facts-2026-10-13.md` | DROP | Done. Not a question. |
| C3 | Category "Medical clinic" | Same file | DROP | Not important for now (Martin). |
| C4 | Remove naturopathy and live blood analysis | Same file. Pages `/naturopathyconsultations` still in the sitemap (13 Oct) | DROP | "Not important anymore". The redirect stays with Martin (site tree, redirect_proposals). |
| C5 | Prices on treatment pages | Same file | DROP | Client rule: no prices. |
| C6 | Doctor names and profiles | Same file | DROP | Client rule: no names. Flag: site tree node ST-31 `/our-doctors/` and the homepage proof strip still assume names. Martin must reframe them as "team without names". |
| C7 | Sound healing page | Same file | DROP | Not confirmed. |
| C8 | Breathwork page | `/breathwork` is live (200) with noindex. Offered (Martin 13 Oct) | MERGE into B8 | The page exists. The open question is visibility. |
| C9 | Bali belly page | Volume 1,300 and 720 (volume2.json, 11 Oct). No page in the sitemap. No query in Search Console (90 days). Offered (Martin 13 Oct) | KEEP (B10) | New page, real choice. |
| C10 | Show hidden IV drip and acupuncture pages | curl 13 Oct: all three pages carry noindex. Sitemap lists none. Search Console pages export has no row for any of them. Audit B06.03 and B06.08 (11 Oct) agree | KEEP (B8) | Biggest open lever. The roadmap of 13 Oct told the client "after your OK". |
| C11 | Ask for reviews: method | Review list 13 Oct: 100 reviews, 15 new in 2026. WhatsApp 321 (Aug), 313 (Sep). Leader 128 | KEEP (B9) | Client task, method is a real choice. 741 does not post. |
| C12 | Reply to the 21 unanswered reviews | `no-review-answering.md` (25 Aug). Handover: 21 reviews without reply since 4 Nov 2025 | DROP | 741 does not answer reviews. It is a client task. The dashboard "Needs you" line already shows 21. Not a choice. |
| C13 | Is "Bali ThetaHealing" a Bali Healing profile? | Audit B05.02 (open). Site tree ST-1A | DROP | A fact question for the client form. No variants, no honest recommendation. |
| C14 | IV drip at home, general doctor | Pool CP-SVC-024, CP-SVC-025. Martin 13 Oct: not confirmed | DROP | Stay out until the client says yes. |
| C15 | Merge short duplicate pages (`/gynecoaesthetic`, `/infusions`, `/infusionstreatment`) | Site tree redirect_proposals (13 Oct) | DROP | Technical work for 741. Needs only Martin's go. The two IV redirects wait for B8. |
| C16 | Homepage with two doors (Wellness, Beauty) | Pool CP-BRD-002. Roadmap: prototype week of 27 Oct | DROP | Pages go through the CRO workflow. Design cards come from that run. |
| C17 | Restart ads, which campaign first | `balihealing-google-ads-setup.md`. Account paused since 1 Oct | DROP | Ads rule: Martin decides with a reasoned go. Not a client card. |
| C18 | Directories (LocalBizNetwork, Bali-Wellness-Guide) | Both submit pages return 200 (13 Oct). Portal `client_citations` has 0 rows for Bali | DROP | Standard listing task for 741. Yes or no only. Low impact. One of two has spam score 39. |
| C19 | Magazine pick (every 2 months) | Roadmap 23 Sep: list approved | DROP | Already approved. |
| C20 | Phone number next to WhatsApp, parking, reply time | Pool CP-LOC-002, CP-SVC-021 | DROP | Facts for the client form. Not choices. |

Counts: 20 candidates. 3 kept. 17 dropped (one of them merged into B8).

## (c) Ranked KEEP list
1. **B8 Show your hidden pages on Google?** Three finished pages are invisible to Google. "iv drip bali" has 1,300 searches a month. Maps top-3 share for "iv drip therapy" is 0 percent (scan 11 Oct). Risk class health: the client must say yes.
2. **B9 How should patients be asked for a review?** Reviews decide the Maps ranking. The ozone share fell from 57.1 to 34.7 percent in 14 days. The leader has 128 reviews, the client 100. WhatsApp is the only booking path.
3. **B10 New page for Bali belly treatment?** 1,300 and 720 searches a month with no page. Lower rank: it needs the doctor's wording first. Risk class health.

Open points for Martin before release:
- B8 variant B covers the unproven acupuncture status. The roadmap of 23 Sep calls an old acupuncture scan "service dropped". The roadmap of 13 Oct and the site tree say show it. Ask once. I recommend A.
- Live text on `/acupuncture` has treat and prevent wording ("treats a broad range of symptoms", "preventing complex disease patterns"). The client rule and Google health policy forbid disease promises. Fix the text before the noindex tag is lifted.
- The dashboard "Needs you" lines and the decisions list in the new dashboard feed still show the old B1, B6 and B7 topics ("Name of the IV page", "Prices and doctor names"). Roadmap v3.1 on the server lists the same. They contradict the facts of 13 Oct. Dashboard owner must update them.

## (d) Dashboard readiness (Bali)
Source: `client-dashboard-redesign/02-data-readiness-bali.md` (13 Oct) and the feed handover in the shared notes (13 Oct, `feed-refresh-job-handover.md`).

| Source | Fill today? | Evidence | Gap | Owner |
|---|---|---|---|---|
| Search Console | Yes | Service account is full user on `https://www.balihealing.com/` (checked 13 Oct). Clicks: Jul 653, Aug 609, Sep 599, 1-10 Oct 191. Daily rows 1 Jan to 10 Oct | 3-day lag. URL-prefix property only. Brand queries lead (234 of 874 query clicks in 90 days). Position per query is not a true rank | agent |
| GA4 (property 428850764) | Yes | Event `contact_whatsapp`: Aug 321, Sep 313, 1-13 Oct 123 (daily from 2 Aug). The older note "service account cannot read it" is stale | Counts clicks, not chats. Nothing before 2 Aug. `generate_lead` 34 and `form_submit` 1 are unclear | agent |
| Local Falcon free reads | Yes, with limits | Profile calls, website clicks, directions, views for both profiles (daily, from 1 Oct 2025). Reviews: main 100 (4.7), 21 without reply, Beauty 10 (5.0), 2 without reply. 18 keywords with a current scan; 49 grid points can be read | The old scan files hold no grid points; save `data_points` at each scan. Three scan settings are mixed; only "ozone therapy" has a same-setting series (57.1, 53.1, 34.7, 38.8). AI scans: one run on 23 Sep, 9 samples per cell. Last 2-3 days fill late | agent; Martin for new scans (49 credits each) |
| Google Ads | Partial | Paused since 1 Oct (verification open). All time: 685 impressions, 61 clicks, IDR 571,785, 14 WhatsApp conversions, IDR 40,842 each. Read by Chrome on 13 Oct, file `evidence/ads-read-2026-10-13.json` | No API developer token. No weekly series. Billing is 13 percent above campaign cost. Do not sum GA4 ad metrics. Skin tag campaign: 2 unpublished drafts | Martin (NIB upload, token); agent (Chrome read) |
| Booked jobs and money | No | Only the client's WhatsApp Business holds them | Ask Peggy and Pasha for one monthly booked-job count | Martin |
| Backlink funnel, listings | Partial | Funnel numbers from the Drive CRM sheet (12 Oct): 149 requests, 38 messages, 14 in talk, 0 links live. Portal `client_citations`: 0 rows | Sheet not re-read on 13 Oct. "38 accepted" and "38 messaged" may be different groups | agent; Martin confirms |
| Feed refresh job | Built | 13 Oct run: no failures. Fixes: 21 reviews without reply (not 8), September position 12.2 (not 10.8), scan dates in Bali time, Beauty history back to January, 18 map keywords, 14 Beauty keywords at 0 of 49 | Texts hard-coded in `dsh.js` stay wrong when months change ("September", "1-13 Oct", "19 of 49", "79 of 100", "45 of 100") | Dinakar / agent (follow-up session) |

Corrections that already hold: the September "flatline" in profile website clicks was a Google data delay (224 clicks for the full month). "45 of 100" is the audit readiness score, not a rank against clinics. Review replies: 21 without a reply, not 8.

## (e) Open data gaps
1. Booked jobs, value, cost per job: no source until the client sends a monthly count.
2. Ads: no API token, no weekly history, account paused.
3. Acupuncture: not proven whether it is still offered (see B8).
4. Beauty profile: leader and competitor review counts not read.
5. Backlink funnel: 38 accepted versus 38 messaged not confirmed.
6. Client-facing English text of the decision module: not verified as live.
7. No new Local Falcon scan, no paid call and no write to the database was done for this queue.


## Main-session edit (13 Oct 2026)
- Draft B10 (Bali belly page) deleted. Another session had already released B10 "Which new page do we write first?" (status open, released 13 Oct 06:33 UTC). It covers the same topic.
- Note for Martin: the open B10 offers "Breathwork in Canggu first" as a NEW page. A page /breathwork already exists and is noindex (see B8). Check this when B10 is answered.

- 13 Oct 2026 (Martin): Bali does NOT offer acupuncture. B8 rewritten (IV drip and breathwork only). Any acupuncture candidate in the table above is DROPPED. The open question about acupuncture is closed.

## Grill result 13 Oct 2026 (Martin in chat)
- B8 (hidden pages) deleted as a client card. Martin: the pages must be indexed, this is not a client question and must not be mentioned to the client.
- FIX TASK (not a card): balihealing.com is a Wix site. /iv-drip-therapy-infusions, /breathwork and /acupuncture return meta robots noindex (checked 13 Oct). Most likely cause: Wix page setting "Let search engines index this page" is off. Fix in the Wix page SEO settings (needs Wix access and Martin's go per change). /acupuncture: Bali does not offer acupuncture, so that page must not be shown; decide separately. After the fix: re-submit the pages in Search Console. Owner: Dinakar or Pasha.
- B9 (review ask) released, recommendation A.
- B10 (open, from another session) stays as it is.
