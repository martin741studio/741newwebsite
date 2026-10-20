# Dumann decision cards: queue (13 Oct 2026)

Client: Naturheilpraxis Daniela Dumann. Client id d01f4236-8674-45fe-a347-0751fa7b24de.
Output: `drafts.sql` (7 draft cards, E1 to E7). Nothing is released. Nothing is visible to the client.

## (a) Client facts

- Language: de. Health client. HWG applies.
- Live site: https://www.danieladumann.de (Wix, 34 pages in the pages sitemap).
- Address form. The website speaks to patients with "Sie". The portal speaks to Daniela with "du" (messages, mails, report titles). Daniela writes "Du" to Martin. Decision: card text uses "du". Variant text for the website uses "Sie" (the website voice). Martin can flip this in one pass.
- Approver in the DB: missing. No `client_approval_settings` row existed. `drafts.sql` inserts one with `approver_user_id` NULL (as the brief says). A client profile exists (user_id 34937572-ec83-4c1e-ac45-88c4cb2b60c9, role client, "Daniela Dumann"). The main session must link it before Daniela can decide.
- Existing cards: none. Codes start at E1.
- Dashboard readiness inputs: see section (d).

## (b) Candidates

| ID | Idea | Verification (source, date) | Result | Reason |
|---|---|---|---|---|
| C1 | Ernährungsberatung: remove 3 claims (tumours, cancer risk, "80 %") | curl /ernährungsberatung 13.10.: all 3 sentences live. The 80 % claim is also in the meta description | KEEP (E1) | Live HWG exposure. Needs an active yes. |
| C2 | Schilddrüse H1 wording | curl 13.10.: H1 still says "Ihr Schilddrüsenspezialist Berlin". Search Console API 13.07.-11.10.: 37 clicks, 569 impressions, rank 3 by clicks | KEEP (E2) | Health wording on a top page. Needs an active yes. |
| C3 | One set of opening hours | Maps public view 13.10.: no hours. Website: "Termine nach Vereinbarung". NAP lock: by arrangement, status unconfirmed. Directory order 09.10.: Tue to Fri | KEEP (E3) | Three versions in use. Directory entries are being placed now. |
| C4 | Name behind every Google title | curl 13.10.: 21 of 34 titles end on "hildegardbingen". Plan item 0.1 is open ("Absprache Martin") | KEEP (E4) | Brand choice for 21 pages. Daniela owns the brand. |
| C5 | Name video consultation on the website | report_feedback 17.09.: Daniela proposed it. Live site: 0 hits for "Video" | KEEP (E5) | Her own idea. Legal risk class forces an active yes. |
| C6 | Herb garden: Schorfheide or Schöneberg | curl 13.10.: /behandlungen says Schorfheide. /kräuterheilkunde and /workshops say Schöneberg, 3 times a year | KEEP (E6) | Live pages contradict each other. |
| C7 | Hide ended course cards | curl 13.10.: 11 cards "Beendet" on /kurse-seminare. That page has 53 clicks, rank 4.4 | KEEP (E7) | Real choice. Weakest impact of the seven. |
| C8 | Remove "Hausbesuche" from footer | curl 13.10.: footer H2 now reads "Termine nach Vereinbarung". Only /behandlungen mentions it ("nicht mehr") | DROP | Already done. |
| C9 | Homepage H1 and intro paragraph | curl 13.10.: new H1 and intro text are live | DROP | Already done (Martin go 09.10.). |
| C10 | Homepage title and description | curl 13.10.: title is the OLD one ("Hildegard von Bingen Ausbildung Seminare ..."). The 09.10. change was reverted | DROP | Martin already decided. This is a re-apply job, not a choice. See flags. |
| C11 | Wording of the GebüH sentence (Daniela, 17.09.) | curl 13.10.: homepage has no GebüH sentence. /behandlungen and /aderlass-therapie already state the 1985 point | DROP | Applies to the draft homepage text only. The plan does not put that text live. |
| C12 | Über-mich corrections (Daniela, 17.09.: "unter anderem", Lachesis, Viriditas founded) | curl 13.10. /lebenslauf: "Lachesis" 0 hits, "gegründet" 0 hits | DROP | Her instruction, not a choice. Still open. See flags. |
| C13 | Herbal medicine and Aderlass as Google categories | Memory 25.09.: neither exists as a Google category. Both are listed as services | DROP | No valid variants. Her question has no answer on record in the portal. |
| C14 | Use the free category slots (7 of up to 9 secondary set) | Cannot verify valid category names without a paid or signed-in read | DROP | Cannot verify. |
| C15 | New pages (Fasten Berlin, Arthrose, Ernährungsberatung training, pillar, menopause) | Work plan 09.10.: "keine neuen Seiten". Listed under "Nicht mehr im Plan" | DROP | Martin rule. Her 3 questions from 04.09. stay unanswered. See flags. |
| C16 | Remove 2 duplicate menu links ("Milta", "Ausbildung Gesundheitsberaterin") | curl 13.10.: both pairs point to the same URL | DROP | Verified, but low impact and no data. Martin decides (rule: no menu renaming). |
| C17 | Redirect /fasten to /hildegard-fasten | curl 13.10.: /fasten returns 200, no H1 | DROP | Technical job for the API owner. |
| C18 | noindex for system pages (/members, /file-share, /challenges, /kurse) | curl 13.10.: all return 200 | DROP | Technical job. |
| C19 | Call button and booking button | curl 13.10.: 2 tel: links and a "Termin buchen" link on every page | DROP | Already present. |
| C20 | One price for the first appointment | curl 13.10.: 220 EUR (60 min, general) and 150 EUR (Aderlass pre-talk, 40 min) are different services | DROP | No proven contradiction. See open facts. |
| C21 | Two audiences (patients and school) | Pool item CP-BRD-004. Daniela approved the patient-first homepage sections on 17.09. H1 and intro are live | DROP | Decided in practice. |
| C22 | Cancellation rule, parking, access, catchment | Pool items marked "needs client" | DROP | Fact questions. Variants would invent policy. |
| C23 | Patient review quotes on the homepage | Maps 13.10.: 9 reviews, all about courses | DROP | Needs patient consent. Not a choice. |
| C24 | Telefonsprechstunde (phone hour) display | Daniela 17.09. | MERGED | Part of E3. |
| C25 | Website name vs Google profile name | Pool item CP-LOC-006 | MERGED | Part of E4. |
| C26 | "Do new talks come?" (open question, 09.10.) | curl 13.10.: /vortraege shows 2 of 3 cards ended | MERGED | Part of E7. |

Counts: 26 candidates, 7 kept, 16 dropped, 3 merged.

## (c) Ranked KEEP list

1. E1 Ernährungsberatung claims. Live legal exposure, also in the Google text.
2. E2 Schilddrüse headline. Health wording on the third-best page by clicks.
3. E3 Opening hours. Maps and directories need one version now.
4. E4 Name behind titles. Affects 21 of 34 pages.
5. E5 Video consultation. Her own idea. Real chance for enquiries, real legal risk.
6. E6 Herb garden. Wrong place on a live page.
7. E7 Ended course cards. Real choice, small impact.

## (d) Dashboard readiness

| Source | Ready? | Evidence | Gap | Owner |
|---|---|---|---|---|
| Search Console | yes | Service account is full user on `https://www.danieladumann.de/` (list call 13.10.). 13.07.-11.10.: 372 clicks, 6,786 impressions, position 31.0. September: 159 clicks, 1,976 impressions. Daily rows read from 2026-06-01 (132 days, 548 clicks, 11,923 impressions). | Query rows show only 121 of 372 clicks. Google hides the rest. Show totals and pages, not query sums. URL-prefix property only. Data before June not tested. | agent |
| GA4 | yes, young | Property 556758063 "Naturheilpraxis Daniela Dumann - GA4" is readable (13.10.). Data starts 30.09.: 2 to 18 sessions per day, 120 sessions in total. Events: begin_checkout 27, schedule 6, purchase 5, form_start 7. | No history before 30.09. Which event means "enquiry" is not defined. Wix event names are unverified. | agent, Martin confirms events |
| Local Falcon | partial | Not connected in this session, so no live read today. Saved: scans 01.10. (report keys fc58366779fb5da, 77db56c6e18d130), both share of local voice 0 %; profile impressions Jul 148, Aug 171, Sep 182 (read 30.09.). Maps public view 13.10.: 5.0 stars, 9 reviews. | No calls, clicks or directions read today. No unanswered-review count. Scans not stored as 49-point data. | agent (needs the connection) |
| Google Ads | no | Ads account "www.danieladumann.de" (523643026) seen on 30.09. Status and spend not read. No developer token. | Needs a browser read. Unknown if ads run. | Martin |
| Portal data | partial | 44 tasks, 5 work items, 6 reports (last 09.10.), 0 leads, 0 visibility prompts, 5 tracked citations (1 live, 4 inconsistent) plus 90 planned rows. | No lead path in the portal. Citation status is a hand count. | Dinakar, agent |
| AI answers | partial | Saved AI report 09.10.: share of AI voice 0.00 % for all 5 keywords. | One run. No stored prompts. No trend. | agent |

## (e) Open data gaps and flags for Martin

1. Approver missing. Link profile 34937572-ec83-4c1e-ac45-88c4cb2b60c9 as `approver_user_id` before release.
2. Homepage title and description were reverted. Live title (13.10.): "Hildegard von Bingen Ausbildung Seminare | Daniela Dumann | Hildegard von Bingen Naturheilkunde". Apply the SEO write again after the last editor publish.
3. The work plan (09.10.) says "heilpraktiker für schilddrüse 320 per month". The pool data (DataForSEO 11.10.) shows no value. E2 uses Search Console numbers only.
4. E2 recommends variant B. The work plan target H1 is variant A. Martin picks.
5. Hours conflict. The NAP lock says "nach Vereinbarung" and "Hausbesuche möglich". Home visits are no longer offered (/behandlungen). The directory order used Tue to Fri hours. E3 asks Daniela to settle it. Fix the NAP lock note after the answer.
6. Maps public view (13.10.) still shows the name "Daniela Dumann", not the renamed profile name. It may be a cached view or a pending edit. Not verified.
7. Open client requests that are no cards. Über-mich: "unter anderem" for the training list, Lachesis as association, Viriditas founded by her (not live). Her 04.09. questions (who rewrites the homepage, whether she writes the Hildegard texts, own page for nutrition training) have no answer on record.
8. Wix cannot be checked from here for E7. Dinakar must confirm that ended cards can be hidden before the go.
9. Open facts for Daniela, no card: cancellation rule, parking and access, catchment districts, first appointment length ("60 minutes" vs "about 2 hours" on /behandlungen).
10. Could not verify: Yelp hours (bot block), Google Business Profile hours behind login, Wix feature limits.

## Correction 14 Oct 2026: another session already extended and partly released this client on 13 Oct

Found at the start of today's grill: another Claude session had already grilled Dumann directly with Martin on 13 Oct (same release-from-chat protocol, actor "Martin (via Claude)"). It expanded the candidate set far beyond my original 7 (to 27: E1-E27), covering more pages (Behandlungen, Kräuterheilkunde, Darmsanierung, Aderlass, Hildegard-Fasten, four training pages, Über mich, four more pages, a Behandlungen restructure) and released E1-E11, E22, E23 (13 cards), while deliberately holding back E12-E21, E24-E27 (14 cards) on Martin's own "not too many at once" instruction.

My attempted release of my original E1-E7 today was a no-op (those rows were already open, so my UPDATE/DELETE matched 0 rows — confirmed via approval_decisions, no duplicate rows).

I then grilled the 14 real waiting drafts with Martin today (14 Oct) and released all of them:
- E12-E15: Darmsanierung, Kräuterheilkunde, Aderlass-Therapie (healing claim removed, recommendation A), Hildegard-Fasten.
- E16-E19: Ausbildung Gesundheitsberater/in, Ausbildung Kräuterheilkunde, Ausbildung Fastenleiter/in, Ernährungstherapie + Rezepte.
- E20, E21: Lebenslauf → Behandlerseite, four more pages (Oligoscan, Homöopathie, Massage, Kurse & Seminare).
- E24: Über mich, three additions from 17 Sep — card itself asks Daniela to confirm the names (Dr. Wighard Strehlow, Germann, Lachesis-Verband, Viriditas 2021) before they go live.
- E25, E26: new FAQ answers (costs/insurance/referral; Hildegard-Fasten FAQ without the "Entgiftung" claim).
- E27: Behandlungen page split into four subheadings, no text change.

Result: all 27 cards for Dumann are now status open (released). 0 drafts remain. hwg_checked true on every card (health client).
