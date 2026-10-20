# Praxis Suriya: re-check of E1-E5 and new cards E6, E7 (13 Oct 2026)

Internal file. Not for the client. Nothing here is in the database yet except E1-E5 (draft). The SQL is in `drafts.sql` (same folder).

## (a) Client facts
- Client: Praxis Suriya, Coralie Suriyapperuma. client_id `3f71ef33-8c74-4ea1-b2d3-0273c2e99649`.
- Language: German (`clients.lang` = de). Form of address: du. The live site uses du in the page text. Sie appears in the footer, the cookie text, the booking form text and some old pages.
- Live site: https://suriya-praxis.de (54 pages in `page-sitemap.xml`, all answer 200 on 13 Oct).
- Health client: yes. HWG applies. Price, treatment and health items need an active yes.
- Approver in the database: Coralie, `approver_user_id` is set (SELECT, 13 Oct). `health_client` = true. No settings INSERT is needed.
- Database state: E1-E5 exist, all `draft`. Nothing is released.
- Coralie's hard rules since 12/13 Oct: no address changes, nothing deleted or devalued in Google, no big changes without talking first, backup before changes, only existing images, access only for agreed work.
- Blocker for any live change: the WordPress app password gives 401, and Martin's WordPress role is too small. Search Console access is gone. Cards can still be answered. Nothing can go live yet.

## (b) All candidates

| id | idea | verification (what, where, date) | result | reason |
| --- | --- | --- | --- | --- |
| E1 | One price for one single session (80 / 85 / 95 EUR) | curl 13 Oct, 54 pages. `/kosten-abrechnung/` "Behandlung 80 EUR / 60 min". `/nacken-schulter/` 85 EUR (H3) and 95 EUR (FAQ). `/hexenschuss-ruecken/` 85 EUR (text) and 95 EUR (FAQ). 95 EUR on schmerztherapie, frozen shoulder, kiefer, Mainz, Wiesbaden. Memory: Coralie called 95 EUR fine in a voice note on 15 Sep. | KEEP, small correction | Still valid. New fact: `/hexenschuss-ruecken/` also shows two prices. Note text lacks this page. Variant B (85 EUR) is weak because she already accepted 95 EUR. |
| E2 | H1 of `/massage-ingelheim/` | curl 13 Oct: H1 "Massage in Ingelheim" (unchanged). Search Console file to 9 Oct: massage queries 2,804 of 4,809 impressions = 58.3 %; "massage ingelheim" 802 impressions, position 10.4, 17 clicks. Volume 480/month (volume.json). Memory 12 Oct: the new page ranks before Coralie's `/ayurveda-therapie/` for "ayurveda massage ingelheim". | KEEP, correct variant A | Numbers are right. Variant A puts "Ayurveda" in the H1. That feeds the cannibalisation with Coralie's own page, which must stay untouched. Replace A. |
| E3 | Click-to-call button | curl 13 Oct: 0 `tel:` links on 54 pages. Number is text in footer and FAQ. Competitor file (11 Oct): 7 of 11 local practices have a tel link. Header already has "Termin über WhatsApp". Home FAQ says "telefonisch montags 12-14 Uhr". Hero text and CTA in the card match the live home. | KEEP, add note | Still valid. A call button promises more than "Monday 12-14". The note must say this. |
| E4 | Merge Migräne-Analyse and Cranio-Neuro-Analyse (GBP + website) | Both pages live (200). Since 7 Oct the Migräne-Analyse page says "Überblick" and has the FAQ "Ist diese Seite dasselbe? Nein". Neither is in the menu. GBP: public Maps shows no service list. The planned service list in `client_locations` has no "Migräne-Analyse". Claim "both are services in the profile" is not proven. Coralie's rule: no address changes. | KEEP, rewrite | The GBP part is not provable and the "two entries" reason is outdated. Real question left: one page with a 301, or two pages. Martin said yes to merge on 13 Oct (06-abgleich point 6) but Coralie must agree to the 301. |
| E5 | New guide `/ratgeber/vagusnerv-nervensystem-beruhigen/` | `/ratgeber/...` answers 404 (as in the card). But: `/blog/` (Gesundheitsjournal) exists. Post `/nervenregulation-vagusnerv/` (Oct 2025, about 1,000 words on the page) exists. `/nervensystem-vagus-beruhigen/` has "Nervensystem beruhigen" in title and H1. Martin 13 Oct: "more blog posts not needed". Coralie 7 Oct: menu and page count too big. Volume 6,600 is a national figure; top results are health portals. | DROP | Duplicates existing content, new section against Coralie's wish, against Martin's 13 Oct line. An optional rewrite (extend the existing post) is in `drafts.sql` as a comment. |
| E6 | Block "Wer behandelt dich?" on service pages | curl 13 Oct on the 19 target pages of `07-umsetzung`: only 4 have the line "Heilpraktikerin seit 2010 ..." (neuro-migräne, cranio-neuro-analyse, schmerztherapie, nervensystem). 15 have none. Facts (Erlaubnis Wiesbaden 2010, Diplom SUWAHASA 2012, CMD FOMT Frankfurt 2016) read on live `/heilpraktikerin-ingelheim/`. Martin said yes on 13 Oct (point 7). | KEEP (new) | Real choice with 3 variants. It adds content only, no address change. `07-umsetzung` says "on no service page": that is outdated (4 pages have a short line). |
| E7 | Booking form intro: du or Sie | curl 13 Oct: the intro "Lassen Sie mich wissen ... bei Ihnen ... für Sie" is on 32 pages. The text above it is du ("deiner Versicherung"). The form came 1:1 from the old site (Martin 24 Sep: keep as it was). | KEEP (new) | Tone break at the conversion point. One text block (WP option `_741_form_block_elementor`). Form fields stay the same. Coralie may prefer Sie, so it is a real choice. |
| N1 | GBP name | Public Maps 13 Oct: still "Praxis Suriya - Ayurveda & Naturheilkunde". Memory: Martin decided 1 Oct "name stays". New name is pending in the manager (12 Oct). | DROP | Decided. |
| N2 | Opening hours | Maps 13 Oct: Mon-Sat 07:30-20:00, Sun closed. Same on footer, `/termin-buchen/`. Coralie confirmed 23 Aug. | DROP | Fact, not a choice. The one wrong place is in housekeeping (see below). |
| N3 | GBP services and categories | Public Maps shows primary category "Naturheilpraktiker" only. No service list, no secondary categories visible. Local Falcon not connected in this session. | DROP | Cannot verify. Live list must be read in the manager first. |
| N4 | Answer Google reviews | Rule `no-review-answering`: 741 does not answer. QR card exists (point 8), Martin sends it. | DROP | Ruled out. Not a client choice. |
| N5 | Gift voucher path | `06-abgleich` point 9: Martin did not choose it. | DROP | Ruled out. |
| N6 | 301 of old pages (HWG old post, `/behandlungsangebot-2/`, `/meinayurvedaangebot/`) | `/suriya-praxis-fuer-naturheilkunde-ingelheim/` is live (200), keyword list, 0 clicks. Martin yes for this one, unsure for the others. Needs Coralie (address rule). | DROP (reserve) | Over the cap of 2 new cards. First reserve if Martin wants a third. Facts above are verified. |
| N7 | Impressum / privacy text | Live: tax placeholder `DE999999999` still in the Impressum. Privacy page names Raidboxes as host. Martin 1 Oct: do not raise the tax ID again. | DROP | Fact fix, not a choice. See housekeeping. |
| N8 | GBP appointment link target | Owner post (7 Jul) links to `/termin-buchen/`. No proof that the link is the cause of fewer clicks. | DROP | No evidence. |

Count: 15 candidates (E1-E5, E6, E7, N1-N8). Kept 6: E1, E2, E3, E4 (all four with a correction) and the new E6, E7. Dropped 9: E5, N1, N2, N3, N4, N5, N6 (reserve), N7, N8.

## (c) Ranked KEEP list
1. **E3 Call button.** Enquiries: Coralie has had no web enquiries for weeks. 0 of 54 pages have a tap-to-call link. Martin already said yes to tel links (point 5).
2. **E2 Massage H1.** Massage is 58 % of impressions and 29 of 57 query clicks. Correct variant A first.
3. **E1 Price.** Easy yes, she called 95 EUR fine on 15 Sep. It removes a trust gap on 4 pages. Needs an active yes (price).
4. **E6 "Wer behandelt dich?".** Trust on health pages, 15 pages, content only.
5. **E7 Form intro du or Sie.** Small text, but at the exact moment of the enquiry.
6. **E4 Merge analysis pages (rewritten).** Last, because it changes an address right after the 12 Oct trust incident. Martin must decide whether to ask now.

## (d) Dashboard readiness

| source | ready | evidence (13 Oct) | gap | owner |
| --- | --- | --- | --- | --- |
| Search Console | no | `scripts/gsc-client-export.mjs https://suriya-praxis.de/` returns 403. Coralie removed 741studio18 and the service account on 12 Oct. Saved data: 90 days to 9 Oct (`03-demand/gsc-api.json`), baseline 30 Sep and 1 Oct (worktree `admiring-nightingale-f0f882`). | No data after 9 Oct. | Martin (ask Coralie for a targeted re-grant, her rule: access only for agreed work) |
| GA4 | no | Service account lists 40 properties under "741 Clients", "741 Studio Main", Johni Jaya, Balihealing. None is Suriya. The site sends to G-B93S7ZWNNR (memory). | No readable property. | Martin (add the account to the GA4 property, or ask Coralie) |
| Local Falcon free reads | partial | The Local Falcon tools are not connected in this session. Memory: GBP linked on 1 Oct. Scan 12 Oct "ayurveda ingelheim" ARP 1.0 / SoLV 100 %. GBP baseline file `2026-10-01-gbp-performance.json` (28 Jun-23 Sep). Public Maps today: 5.0 stars, 13 reviews, Mon-Sat 07:30-20:00. | No live read today. Calls, routes, website clicks after 9 Oct not read. | agent (in a session with the Local Falcon connection) |
| Google Ads | partial | Campaign "Suriya - Lokal Ingelheim (Search)" paused since 9 Oct. Conversion tags live in GTM-K9MDDN7P. | No API developer token. Only UI reads in Chrome. No spend yet, so little to show. | Martin (decide start), agent (UI read) |
| Form enquiries | no | Forms go to Gmail. Nothing is counted. Enfold forms may not trigger the tag (dossier point 5). | No count. | Dinakar (needs WordPress access), Martin |

## (e) Open data gaps and housekeeping (not cards)
Housekeeping items need Martin's go per change and working WordPress access.
1. `/contact-2/` says "Mo.-Sa. zwischen 9.oo & 20.oo Uhr". Everywhere else (footer, Maps, `/termin-buchen/`) it is 07:30-20:00.
2. Name typo: "Prof. Gret" on home, `/heilpraktikerin-ingelheim/`, `/nervensystem-vagus-beruhigen/`, `/suriya-neuro-migraene/`. Other pages say "Prof. Greten". Memory: name check is still open before go-live.
3. Impressum: `DE999999999` placeholder is live. Privacy text names Raidboxes as host (memory: host is Cyon). Martin said not to raise the tax ID again. Raidboxes is a separate text fix.
4. Booking form labels: "Telefonummer:" (typo) and "Anliegen:" twice.
5. Google profile shows "Rollstuhlgerechtes WC". Memory (23 Aug) says the toilet attribute was set to "Nein". Accessibility is Coralie's stated priority. Check in the manager.
6. The planned GBP service list in the database still has "Faszientherapie". Coralie does not offer it (8 Sep). Read the live list in the manager.
7. Website review widget shows 12 reviews. Maps shows 13.
8. Home page: the WhatsApp line under the hero button (6 Oct) is not in the live HTML today. Cause unknown.
9. `07-umsetzung-2026-10-13.md` point 7 says the "Wer behandelt dich?" line exists on no service page. Four pages have a short one.
10. Portal still shows 21 Sep tasks as done (dossier section 10). Not part of the cards.
11. Not verified: live GBP service list and secondary categories; live reply status of the 13 reviews; reason for removal of the home card "Nervensystem & Vagusnerv" on 11 Oct (live home still has a text block with that heading).

## Grill result 13 Oct 2026 (Martin in chat)
- E1-E4, E6, E7 all released as drafted, recommendation A on every card. hwg_checked set on all six (Martin confirmed the wording).
- E5 stays deleted (see main-session edit above).
- Coralie can now see and decide these six cards in the portal.
