# Decision queue: STÜRZL Steuerstrafrecht (13 Oct 2026)

Internal file. Not for the client. Cards are DRAFT only. Nothing is released.

## (a) Client facts

- Client: STÜRZL Steuerstrafrecht, Dr. Anja Stürzl. ID b6f6e303-50e4-4afb-a343-337206cec316. Status onboarding. Language de.
- Form of address: du. Martin said on 12 Oct 2026: "Wir sind alle beim Du". Text for the website inside variants stays in Sie form, like the live site.
- Live site: https://www.stuerzl-steuerstrafrecht.de (Joomla). Law firm. Not a health client. No HWG. BRAO 43b, BORA 6 and UWG apply.
- DB state (13 Oct): 0 approval_items, 0 client_approval_settings, 0 profiles. The client has no portal login.
- Approver: MISSING. drafts.sql inserts a settings row with approver_user_id NULL and approver_name "Dr. Anja Stürzl". The client cannot decide until a login exists. Martin must create the login and set approver_user_id.
- Codes start at E1.
- Contact data: contact_email is empty in clients.

## (b) All candidates

| ID | Idea | Verification (source, date) | Result | Reason |
|---|---|---|---|---|
| C01 | Start page title and H1 | Live curl 13 Oct: title "Stürzl Steuerstrafrecht – Home", H1 "Kanzlei". GSC export 13 Oct (16 months): "anwalt steuerstrafrecht frankfurt" 3.600 impressions, position 8,6, 6 clicks. Variants from `cro/04-copy/approved-copy.md` (Martin approved 11 Oct). | KEEP (E1) | Still open and live. Strong data. Wording is legal-sensitive. |
| C02 | GBP categories, Frankfurt and München | Chrome read of public Maps 13 Oct: both profiles show only "Rechtsanwalt". Competitor categories from analysis 9 Oct and source of truth tab 02 row 17. | KEEP (E2) | Not done. Maps impact. Primary category stays 741-only (lock). |
| C03 | Start page: Entwurf A or B, or keep the old page | Both drafts return 200 on clients.741.studio (13 Oct). Mail draft of 12 Oct asks the client to choose. No answer found in memory or files. Live page has no form (checked). | KEEP (E3) | Open client choice. Martin must set the recommendation. See gap 3. |
| C04 | Merge four Selbstanzeige pages, 301 redirects | Live curl 13 Oct: all 4 URLs return 200, 3 carry the same H1. Overlap 74 % and 97 % from sitetree.json (11 Oct). Redirects need the client's consent (sitetree note). | KEEP (E4) | Real structure choice. Needs consent for redirects. |
| C05 | Compliance page: name Tax Compliance as a service | `/compliance/` returns 404 (new page). Client text has no "Tax Compliance". Search volume 590 (11 Oct). The question is also in the compliance comparison page sent on 12 Oct. | KEEP (E5) | Only the firm knows if it offers this. Compliance is the highest-margin service (source of truth). Avoid asking twice. See gap 4. |
| C06 | Price of the Erstberatung | Live page "Kanzlei" says "zum Festpreis", no amount (13 Oct). Kostentext (9 Oct) says Pauschale 250 to 350 Euro, "üblicherweise". Mail of 12 Oct asks for price and duration. | KEEP (E6) | Two different statements are live or planned. Price card. Active yes. |
| C07 | How to ask for Google reviews | Google Maps 13 Oct: Frankfurt 14, München 1. anwalt.de 79 (9 Oct). Source of truth: no process, confidentiality is the obstacle. | KEEP (E7) | Real process choice. Confidentiality makes it sensitive. |
| C08 | Google Ads start time (early or after new pages) | Backlog says the client decides. Email of 12 Oct already put the question to her. | DROP | The table needs a recommended_key. Martin's rule: 741 gives no recommendation here, and Ads decisions need Martin's reasoned go. Handle in mail or Loom. If Martin wants a card, he sets the recommendation. |
| C09 | Contact form fields and consent text | Both drafts contain a form (grep 13 Oct). Consent text (DSGVO, 203 StGB) is a legal task of the firm. | DROP | The form comes with E3. Field list and consent text are a review task, not a choice. |
| C10 | Emergency numbers on the start page | Numbers are on the live contact page (13 Oct). Martin released them on 11 Oct. Both drafts show them. | DROP | Already decided. No promise about answer times is allowed (stuerzl-kosten-fakten). |
| C11 | Place of the KI text block | Mail draft of 12 Oct already states the decision (end of cost page plus short FAQ answer). | DROP | Already communicated. No open choice. |
| C12 | Remove cost part from the FAQ | The firm asked for it itself (11 Oct). Live FAQ still shows 380 to 450 / 330 to 400 / 280 to 350 Euro. | DROP | Task for 741 with Martin's go, not a choice. |
| C13 | Rechtsschutz paragraph on the cost page | Live FAQ has the heading "Kosten/Versicherung" but no insurance text (checked 13 Oct). Nothing is lost when the cost part leaves. | DROP | Nice to have. Ask in the next mail. Fact belongs to the firm. |
| C14 | Fachanwalt title, Dr. title | Confirmed by Dr. Stürzl's CV on 11 Oct. Martin released "Dr." and anwalt.de numbers. | DROP | Already confirmed. |
| C15 | München location page | Client asked for it (source of truth). Martin closed the package question on 11 Oct. | DROP | No choice. |
| C16 | Opening hours | Martin 12 Oct: Google profile is the source. Never ask the firm. | DROP | Rule. |
| C17 | New Frankfurt address Untermainkai 26 | Canonical NAP, confirmed many times. Live site and GBP still show Wiesenhüttenstraße 17 (13 Oct). | DROP | Not a client choice. Switch waits for Martin's go. |
| C18 | Wording of the firm's own live pages ("Spezialisierung", "Expertise", "Festpreis", "Straffreiheit" in H1) | OPEN-FLAGS A6, live curl 13 Oct confirms the words. Martin has not decided whether and how to tell the firm. | DROP for now | Martin decides first. Not a card until then. |
| C19 | Publication list: "Heidelberger Kommentar (3. Auflage, erscheint 2024)" | Live Dr. Stürzl page 13 Oct still says "erscheint 2024". | DROP | Fact correction. Put it in the next question mail. It is not a choice with variants. |
| C20 | Ask editors (LTO, JUVE, ZRI) to add links | 15 mentions without a link (source of truth tab 12). | DROP | Outreach task for 741. No design choice. Ask by mail if needed. |
| C21 | Disavow group C: were links bought? | Disavow of 37 domains uploaded 13 Oct. | DROP | Fact question. 741 can check the 6 domains by hand. |
| C22 | Cookie banner covers 60 % of the mobile screen | Source of truth tab 02 row 22 (8 Oct). | DROP | Technical fix by 741. Consent rules, not a client choice. |

Counts: 22 candidates, 7 kept, 15 dropped.

## (c) Ranked KEEP list

1. E1 Start page H1. Reason: 3.600 impressions at position 8,6 and 6 clicks. The page title says "Home". Direct effect on rankings and clicks.
2. E2 GBP categories. Reason: both profiles lack the categories that the leading profiles use. Direct effect on Maps.
3. E3 Entwurf A or B. Reason: biggest page decision. Both drafts have a form and the emergency strip. The live page has neither.
4. E4 Selbstanzeige pages. Reason: four pages compete for one topic. A merge needs the client's consent.
5. E5 Tax Compliance. Reason: 590 searches a month and the firm's highest-margin service. Only the firm can answer.
6. E6 Erstberatung price. Reason: the live "Festpreis" claim and the new "Pauschale" text disagree. Price card, active yes.
7. E7 Google reviews. Reason: 14 and 1 reviews. The 741 reading is that reviews are not the main ranking cause (09 Oct analysis), so the card ranks last.

Top 3 to ask first: E1, E2, E3.

Open points inside the cards:
- E3: recommended_key "A" is a placeholder. Martin sets A or B. Self-scores: A 37/44, B 38/44. The scores are not fully comparable (different checks).
- E1: the H1 chosen here also applies to the draft that the client picks in E3. Draft B currently uses H1 variant B. Release E1 and E3 in one round.
- E5 repeats question 1 of the compliance comparison page sent on 12 Oct. Release E5 only if the question did not go out by mail, or tell the client that the card replaces it.
- All 7 cards use risk_class legal or price, except E3 and E4. Legal and price cards need an active yes (no 7-day rule). auto_approve_consent stays false.

## (d) Dashboard readiness (checked 13 Oct)

Read-only probes. Method: service account `reporting-bot` through `feed/google.mjs` (key not printed), public Maps read in Chrome, saved files.

| Source | Status | Evidence | Gap | Owner |
|---|---|---|---|---|
| Search Console | partial | Property `https://www.stuerzl-steuerstrafrecht.de/` verified 13 Oct (HTML tag). 16 months of data seen in the UI: 7.040 clicks, 97.700 impressions. API probe: HTTP 403 for URL prefix and for sc-domain. Saved export: `gsc-16m-2026-10-13.tsv` (top 100 only). | Service account is not a user of the property. | Martin: add `reporting-bot@studio-apis-503306.iam.gserviceaccount.com` as full user. Agent then builds the feed. |
| GA4 | partial | Property 483853149 delivers data (226 users in 28 days on 9 Oct; email_click 40, phone_click 19). Key events set on 9 Oct. API probe: HTTP 403 "insufficient permissions". Access exists only for account 741studio18. | Service account has no role on this property. | Martin: add `reporting-bot` as Viewer on property 483853149 (or on the account holding it). |
| Local Falcon (free reads) | partial | Baseline 1 Oct (8 keywords, 7×7, 5 km) saved in `baseline/`. Campaign 56d95fc22d54bef started 9 Oct: 5 keywords, monthly, 7×7, radius 5 miles. The two radii do not compare. The LF MCP is not connected in this agent. | Not read live today. Whether the GBP is connected for profile metrics (calls, clicks, directions) is not verified. München has no baseline grid. | Agent (read), Martin (go for any new scan). |
| Google profile data (reviews, categories) | yes | Public Maps read in Chrome on 13 Oct: Frankfurt 5,0 / 14, München 5,0 / 1, category "Rechtsanwalt" on both. | Profile actions (calls, directions) need the LF GBP link or the Business Profile API. München owner is unknown (Linkemann has no access). | Martin and the firm. |
| Google Ads | no | No account, no ads tag on the site (source of truth tab 02 row 20, 8 Oct). No API developer token. | Ads access was requested and is still open. | Martin. |
| Portal data | partial | `client_reports` and `scans` rows exist since 1 Oct. `leads`: no form on the site, so no rows. | The form comes with the new start page. | Dinakar. |

Result: the feed cannot be filled today from the API. It can be filled after two grants (GSC user, GA4 viewer). Maps metrics need one more check.

## (e) Open data gaps

1. No approver login. `profiles` has 0 rows for this client. Without it the client cannot answer any card.
2. contact_email is empty. The digest mail has no address.
3. E3: Martin has no stated preference for A or B in my sources. I could not verify whether the client answered the 12 Oct mail. Check mail before release.
4. E5: unclear if the compliance questions went out by mail. Check before release.
5. München profile: owner unknown. The category change in E2 can only run for Frankfurt until this is solved.
6. Erstberatung in E6: net or gross is open. The card asks for it in the comment field. Duration of the Erstberatung is also open.
7. Ads start time (C08): needs Martin's decision about form (card without a recommendation is not possible).
8. OPEN-FLAGS A6 (the firm's own wording): Martin decides how to handle it. It may become a card later.
9. Not verified: whether anyone changed the GBP categories after 13 Oct 10:00. The Maps read is from 13 Oct.
10. "Irsch" appears in the redirect notes of the sitetree ("Klärung mit Irsch"). I did not find who this is. It does not block E4.


## Main-session edit (13 Oct 2026)
- C05 / E5 (Tax Compliance) dropped. Reason: the question may already be in the 12 Oct mail, and the card would ask the firm to claim a service that nobody verified.
- Old E6 (Erstberatung price) is now E5. Old E7 (Google reviews) is now E6.
- E3 recommendation stays a placeholder (A). Martin sets A or B in the grill round.

- 13 Oct 2026: E3 recommendation changed to B in the DB (Martin's answer relayed by the Morning Grill session). Release and login creation NOT done: run limit, see INDEX.md section 3.

## Release 13 Oct 2026 (Martin's go in this chat)
- Login created: user 4a02fc1f-dc10-412f-83e2-5ad1bc1cce22 (first created with a googlemail address; corrected by Martin 13 Oct: the login email in the database is now stuerzl@stuerzl-steuerstrafrecht.de), role client, approver of the client. No mail sent, no notification, digest stays off.
- The password is random and unknown. Nobody has it. Martin sets one or uses a reset when he sends the welcome mail himself.
- E1 to E6 released (status open) at 13 Oct 07:52 UTC, reminder 16 Oct, due 20 Oct. Six approval_decisions rows (kind admin, action released, actor Martin (via Claude)).
- Backup before the change: bulk/stuerzl/backup-pre-release-2026-10-13.json.
- Facts re-checked before release: start page title "Home", H1 "Kanzlei", "Festpreis" on /index.php/kanzlei, /kosten/ is 404 (new page), both draft links return 200.
