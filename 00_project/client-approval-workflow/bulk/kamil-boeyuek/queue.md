# Kamil Böyük: decision card queue (13 Oct 2026)

Draft only. Nothing is inserted, released or visible to the client.

## (a) Client facts

- Client: Kamil Böyük, id cc5ad406-d06d-4b5a-a33c-3386b9e3de60, lang de, mode `reports`, status active.
- Two practices, two WordPress sites. Do not mix them.
  - Physio Anatomie GmbH = physiotherapieoberhausen.com (Oberhausen, Marktstraße 163-165).
  - Physiotherapie Kraft = physiotherapiekraft.de (Gelsenkirchen, Hausbesuche in Ruhrgebiet).
- Health client: yes. HWG applies. Settings row in DB: none (drafts.sql inserts it with `health_client = true`).
- Form of address. Live sites use "Sie" toward patients. The 13 Oct draft report to Kamil uses "du". Rule: always "du" with clients. Decision: card text to Kamil in "du". Website copy inside variants has no pronoun. Martin: confirm "du".
- Approver. `approver_user_id` is NULL in drafts.sql (brief rule). A client profile exists: user_id 1384d5b2-4e9d-4912-86d9-296fd893717c, name "Kamil Böyük", role client. Martin decides if this user becomes the approver. A comment in drafts.sql holds the one update.
- Portal: 0 approval items, 0 tasks, 0 programs, 0 access grants, 0 locations, 0 master data. 2 reports (July). 1 work item (Aug + Sep numbers, internal). The module tab works for `reports` clients through the deep link `?view=decisions`.

### Can 741 change a website for Kamil?

- Technical access exists. Dinakar set the GA4 tag on Kraft through a plugin in Aug 2026 (memory kamil-physio-client). Novamira is connected for Anatomie since 13 Oct. Novamira for Kraft is NOT connected yet.
- Contract scope is not set. No program, no tasks, no page change requests, no access grants in the portal. 741 runs the Google Ads account and the monthly reports.
- Every website change needs Martin's go per change (rule no-website-changes-without-go).
- Result: 741 can probably edit both sites, but website work is not part of a set program. The three website text cards and the placeholder card are real choices for Kamil. Martin must first decide if 741 offers this work. No card touches the Ads account.

### Urgent finding, not a card

physiotherapiekraft.de is actively compromised, checked 13 Oct with `curl`:
- The home page holds hidden casino and betting links (about 170 hits for casino words) in off-screen divs, including a Polish casino text under an H2 "Test za dychę".
- Inner pages show Turkish betting text near the top and a casino sentence in the footer.
- `/wp-sitemap.xml` and the sitemap index list fake `/goods/detail/...` URLs, updated hourly.
- With a Googlebot user agent the casino words did not show on the home page (0 hits). Normal browsers see them.
- This is the "casino-spam injection" from memory kamil-novamira-connections. It is still live. Owner: Martin, Dinakar. No client choice. It must be cleaned before any budget increase on Kraft.

## (b) All candidates

| ID | Idea | Verification | Result | Reason |
|---|---|---|---|---|
| C1 | Kraft: remove placeholder texts (fake quotes, "Physio Pathologie", Lorem ipsum, "Dr. James Anderson, D.C." team) and decide what replaces them | `curl` on /leistungen/hausbesuche/, /uber-uns/, home, 13 Oct. Visits: GA4 property 468424260, host physiotherapiekraft.de, /leistungen/hausbesuche 427 visits, 1 Sep - 12 Oct | KEEP (E1) | Verified live. Real choice: what stands in his name. High legal and trust risk. Ads send traffic here |
| C2 | Anatomie /leistungen/ H1: remove "das Nonplusultra" | `curl` 13 Oct. H1 text exact. GA4: /leistungen 918 of 1,229 visits | KEEP (E2) | Verified. Biggest entry page. Real wording choice |
| C3 | Anatomie home title: add the city | `curl` 13 Oct: title "Physio Anatomie – Individuelle Physiotherapie". GA4: organic 107 of 1,229 visits | KEEP (E3) | Verified. Title has no city. No search volume used |
| C4 | Anatomie home H1: remove "Schmerzfrei bewegen" promise | `curl` 13 Oct. GA4: home 201 visits | KEEP (E4) | Verified. HWG-sensitive wording. Lowest traffic of the four |
| C5 | Kraft home H1 "Willkommen bei Physiotherapie Kraft." rewrite | `curl` 13 Oct. GA4 calls: 209 of 821 home visits had a phone-tap event (25.5 %), against 44 of 427 on the Hausbesuche page (10.3 %) | DROP | The home page already gets the most calls. A rewrite can lower that. Minimal-change rule |
| C6 | Kraft ads: change landing page to /leistungen/hausbesuche (idea from physiokraft-tracking-fix.md, 14 Aug) | Same GA4 numbers: home 25.5 % call rate, Hausbesuche 10.3 %. Ads currently split: 560 home, 402 Hausbesuche paid visits | DROP | Ads choice is Martin's, not Kamil's. The data argues against the switch. Note for Martin below |
| C7 | Budget test for both campaigns | Draft report 13 Oct (other Kamil chat) says both are limited by budget. Aug spend Kraft 1,041, Anatomie 1,020; calls 217 and 91. I did not re-read the Ads account. Current daily budgets unverified (16 Aug: 40 and 38 per day) | DROP (hold) | Martin said on 13 Oct: no Ads change before a reasoned go. Kraft ad is under review since 11 Sep. Kraft site is compromised. Raise the budget only after both are clean. Re-raise as a card when Martin asks |
| C8 | Kraft ad disapproval (health policy) | Draft report 13 Oct: under review since 11 Sep, appeal running | DROP | 741 work in progress. No choice for Kamil |
| C9 | Mark phone tap, mailto and form start as GA4 key events | GA4 events 1 Sep - 12 Oct: `tel` 124 (Anatomie) and 373 (Kraft), `mailto` 5, `form_start` 3. Key events: 0 on every row | DROP | 741 measurement task in the 741 Clients GA account. No choice for Kamil. Feeds the dashboard |
| C10 | Clean the Kraft spam injection | See urgent finding | DROP | Security task, not a choice. Top priority for Martin and Dinakar |
| C11 | Extra income streams (self-pay services, second location, more home visits) | No saved demand data. The claim "Kassentermine are capped" in the 13 Oct draft report has no source I can open. No paid pull allowed | DROP | Cannot verify. A strategy talk for Martin first |
| C12 | GBP cards (categories, services, hours, phone, name) for either practice | Web search returned no profile data. Local Falcon is not connected. No saved profile files for Kamil | DROP | Cannot verify any profile fact |
| C13 | Anatomie /leistungen/ body text ("heilend bei Schmerzen", "Selbstheilungskräfte", "Bobath wirksam") | Live text seen 13 Oct | DROP as own card | Merged into the note of E2. Next card after Kamil answers E2 |
| C14 | Anatomie /profil/: duplicate degree entry ("Tourismus und Hotelfachkunde" twice, "Master noch im Studium") | Live text seen 13 Oct | DROP | Typo fix and CV wording. Kamil gives the real CV. A 741 task |
| C15 | Kraft name error "Physio Pathologie" on home, Hausbesuche, Über uns | Live text seen 13 Oct | DROP as own card | Part of E1 |
| C16 | Kraft tel links: three formats (`tel:020994786665`, with a trailing %20, `tel:+4920994786665`) | HTML 13 Oct | DROP | 741 task. Not a choice |
| C17 | 741 proof wall says Physio Anatomie rank "12 to 2 for Physiotherapie Stuttgart" | `04_site/de/pages/local-seo.html` line 780. Practice sits in Oberhausen | DROP | Internal. Martin: check the city on the proof wall |

Counts: 17 candidates, 4 kept, 13 dropped.

## (c) Ranked KEEP list

1. E1 Platzhalter-Texte auf physiotherapiekraft.de entfernen? Highest legal and trust risk. Paid traffic lands on these pages. Only the owner can supply real names and quotes.
2. E2 Überschrift der Seite "Leistungen" bei Physio Anatomie. 75 % of all visits enter here. The H1 makes a claim that is hard to prove.
3. E3 Titel der Startseite bei Physio Anatomie. The title has no city. Organic search brings only 9 % of visits. No HWG risk.
4. E4 Hauptüberschrift der Startseite bei Physio Anatomie. Promise "Schmerzfrei bewegen". Only 201 visits, so it ranks last.

Risk classes: E1 legal, E2 health, E3 none, E4 health. E1, E2 and E4 need an active yes. `hwg_checked` stays false.

## Notes for Martin (not card content)

- Kraft ads landing page. The 14 Aug fix note proposed /leistungen/hausbesuche. GA4 from 1 Sep to 12 Oct shows the opposite. Home page: 821 visits, 209 with a phone tap (25.5 %). Hausbesuche page: 427 visits, 44 with a phone tap (10.3 %). Anatomie /leistungen: 918 visits, 77 with a phone tap (8.4 %). Do not switch the Kraft final URL on the old engagement-rate argument.
- Kraft call rate is higher than Anatomie on every landing page. Kraft: 1,392 visits and 373 phone taps. Anatomie: 1,229 visits and 124 phone taps. Both sites get about 1,000 paid visits.
- The Kraft Hausbesuche page, which has the fake quotes, gets 402 paid visits. It also gets the lower call rate. Removing the placeholders is a CRO test, not only a risk fix.
- Account number. `physiokraft-tracking-fix.md` writes 992-981-4093. Memory and the policy file write 992-981-4693. The 13 Oct report uses 4693.
- An extra host `n766932.websitebuilder.online` shows 5 visits in Aug and Sep in the shared GA4 property. Old staging URL.

## (d) Dashboard readiness

| Source | Ready? | Evidence | Gap | Owner |
|---|---|---|---|---|
| GA4 (property 468424260, both sites, split by `hostName`) | yes | `reporting-bot` read OK on 13 Oct, data to 12 Oct. Sessions Aug/Sep: Anatomie 953/869, Kraft 751/938. Channels, landing pages, cities, device, events all readable | Key events = 0. `tel` is not a key event. Kraft Jul-Aug jump is a tracking fix, not growth (fixed mid-Aug). Both sites share one property | Agent reads. Martin gives go to mark key events. Dinakar or agent sets them |
| Search Console | no | `--list` shows 6 properties. Neither Kamil site is in it | Add `reporting-bot` as user. Both sites need an owner-level path. Verification by file or tag needs site write access | Dinakar (site access), agent (API workflow). Martin go for any site write |
| Local Falcon free reads | no | Connector disconnected in Claude Code (plan.md 13 Oct). No Kamil place IDs on file. Only two proof images in `04_site/public/review-assets/proof/` (Kraft "Krankengymnastik" rank 8 to 1) | Reconnect connector. Get both place IDs. A free read of old reports needs no credits. New scans cost credits and need Martin's go | Martin (reconnect), agent |
| Google Ads (account 992-981-4693) | partial | No API (developer token missing). Aug and Sep totals were read in the Ads UI on 13 Oct for the draft report: spend 2,061.94 / 2,152.28, conversions 326 / 281, calls 308 / 214 | Sep clicks, Sep spend and calls per practice, weekly series, current daily budgets. Needs a Chrome read with the 741studio18 login | Agent via Chrome. Martin for the API token |
| Portal data (`leads`, `client_locations`, `client_master_data`) | no | 0 rows each. Daily standup flags "no NAP/location data" | Phone, address, hours for both practices | Gayo or agent, from the live sites |
| Booked appointments, patient value, cost per patient | no | Not stored anywhere | Only Kamil knows. Phone taps are a proxy | Martin asks Kamil |
| Google profile (calls, directions, reviews, replies) | no | No read possible (see C12) | Profile access or Falcon reads | Martin, agent |

## (e) Open data gaps

- Keyword demand for "Physiotherapie Oberhausen", "Krankengymnastik" and Hausbesuche terms. Needs one paid pull with Martin's go. Without it, E2 to E4 do not carry a volume claim.
- Current state of the Kraft ad (approved or still under review) and current daily budgets for both campaigns.
- Who built the Kraft site and who has WordPress admin. Novamira for Kraft is not connected, so I did not read the WordPress side. I used public `curl` only.
- Whether Kamil takes insurance patients, self-pay patients or both. The "Kassentermine are capped" line in the 13 Oct report is unverified.
- Real team names, qualifications and photos for Kraft (answer to E1, option B).
- Approver user for the portal (see above).
- Practice city on the 741 proof wall for Physio Anatomie.
