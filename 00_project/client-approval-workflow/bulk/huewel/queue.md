# Praxis Hüwel: decision cards queue (13 Oct 2026)

## (a) Client facts

- Client: Praxis Hüwel, Martin Hüwel. client_id `f0a6730f-8f56-4c61-8085-1955f3bb285a`. Mode program. Status active. Nuremberg (Südstadt, Nürbanum).
- Language: de. Form of address in cards: du. Reason: Martin's rule "Du-Form" for this client, and the open card E1 uses du.
- Live site: https://www.praxis-huewel.de (GitHub Pages, live since 6 Oct). The site speaks to patients in Sie (57 Sie-words, 0 du-words on the home page, checked 13 Oct). The PDF "Wartezeit-Vermeider" uses du (6 du-words, 0 Sie-words, checked 13 Oct). Text variants for the site use neutral or Sie wording.
- Health client: yes. HWG applies. Hüwel got a warning (Abmahnung) in 2018. He wrote this himself on 31 Aug 2026.
- DB state: `approval_items` has 1 row: E1 (Datenschutz-Abschnitt Google Analytics), status open, released 13 Oct 05:02, `remind_at` and `due_at` empty, `hwg_checked` false. `client_approval_settings` has NO row. `profiles` has one client user: `8a596070-1f02-4452-810d-4d3d738df1c7` ("Martin Hüwel", role client).
- Approver: missing. See section (e), gap 1.

## (b) All candidates

Sources: content pool 11 Oct (`assets/huewel/content-pool/`), site tree ST-xx, client feedback in `report_feedback` (31 Aug, 14 and 17 Sep), live crawl 13 Oct (22 pages + 5 articles), memory files.

| # | Idea | Verification | Result | Reason |
| --- | --- | --- | --- | --- |
| C01 | Hero, title, H1 "Heilpraktiker Nürnberg" (CP-LOC-001) | Live 13 Oct: title "Heilpraktiker & Homöopath Nürnberg \| Praxis im Nürbanum", H1 "Heilpraktiker in Nürnberg – Ursachen finden statt Symptome verwalten" | DROP | Already done. |
| C02 | Location block (CP-LOC-002) | Live home page has address, hours, map, "Parkplätze sind vorhanden", transit sentence | DROP | Already done. Free parking and barrier-free access are not confirmed. |
| C03 | Neighbour towns in one sentence (CP-LOC-003) | Live home page names Erlangen, Fürth, Schwabach. Hüwel confirmed patients from there (31 Aug) | DROP | Already done. |
| C04 | Own town pages Fürth, Erlangen, Schwabach (CP-LOC-004) | Pool status "cut" | DROP | Cut in the pool. Hüwel says Schwabach patients are rare. |
| C05 | Correct NAP in directories, Doctolib old address (CP-LOC-005, AUT-007) | DB `client_citations`: 38 live, 29 planned. Doctolib needs Hüwel's own login (bot check) | DROP | Task for the citation module, not a choice. |
| C06 | Structured data: hours, sameAs, services (CP-LOC-006, AUT-008) | Technical change | DROP | No choice for the client. Agent task. |
| C07 | "Vier Werkzeuge, ein Ziel" block (CP-SVC-001, BRD-005) | Live on home | DROP | Already done. |
| C08 | Process and first appointment (CP-SVC-002) | Live: 3 steps on home, page "Termine & Ablauf" | DROP | Already done. |
| C09 | Prices and reimbursement block (CP-SVC-003) | Live: 90 € single session is the same on home, FAQ, PSE and Gesundheitscheck pages | DROP | Already live and consistent. Rule: no price cards without a conflict. |
| C10 | Packages and Ursachen-Klarheitsanalyse as offer (CP-SVC-004) | Live on home with prices | DROP | Price topic. No conflict found. |
| C11 | Expand FAQ, short direct answers (CP-SVC-005, 025) | Live: 4 FAQ questions with markup | DROP | Content work. No client choice. |
| C12 | Frequenztherapie main page (CP-SVC-006) | Live 660 words. Main term must never change (2018 warning) | DROP | No choice. |
| C13 | Magnetfeldtherapie wording on the Ondamed page (CP-SVC-007, ST-12) | Live H1 "Ondamed-Therapie (PEMF)". Word "Magnetfeld" is on none of the 27 pages checked. Volume 9,900 (DE), 10 (Nürnberg), 11 Oct | KEEP | E5. |
| C14 | PSE page (CP-SVC-008) | Live 780 words, term rarely searched | DROP | No choice. |
| C15 | Homöopathie main page (CP-SVC-009) | Live title "Homöopathie Nürnberg \| Heilpraktiker Martin Hüwel", H1 "Homöopathie in Nürnberg". Keyword is already in both | DROP | Already done. |
| C16 | Five homeopathy articles: check and tidy (CP-SVC-010, AUT-005, ST-51) | Read all 5 live on 13 Oct. 3 have claims of proof or treatment | KEEP | E6. |
| C17 | Gesundheitscheck page (CP-SVC-011) | Live 751 words | DROP | Merged into E3 (naming). |
| C18 | Expand the Bioscan page (CP-SVC-012) | Hüwel wrote on 31 Aug that he is careful with the word "Bioscan" (2018 warning) | DROP | Blocked until E3 is answered. |
| C19 | Vitalstoffanalyse (CP-SVC-013) | Live 466 words | DROP | No choice. |
| C20 | Mikronährstoff page, keyword "mikronährstoffanalyse" (CP-SVC-014) | Volume 2,900, competition HIGH, "mikronährstoffanalyse nürnberg" 20. The lab service is called "Vitalstoffanalyse" on the site | DROP | Seventh-card limit. Weak local value. Review in the next round. |
| C21 | Nebennierenschwäche page (CP-SVC-015) | Live title and H1 already carry the keyword | DROP | Already done. |
| C22 | Chronische Erschöpfung page (CP-SVC-016) | Live 490 words | DROP | No choice. |
| C23 | PostVac and Long Covid page (CP-SVC-017, ST-25) | Page returns 404 (not built). Pool decision 11 Oct: waits for the talk Martin Drendel and Hüwel. Highest HWG risk | DROP | Waiting for the talk. No card before. |
| C24 | Concern pages "Schmerzen und Verletzungen", "Stress, Erschöpfung und Psyche" (CP-SVC-018, ST-31, ST-32) | Both URLs return 404 (proposals). Old page had 7 clicks, 71 impressions in 90 days. Martin decided on 11 Oct | KEEP | E8. |
| C25 | Bioresonanz explanation page (CP-SVC-020) | Decision 11 Oct: stays as explanation | DROP | Decided. |
| C26 | Page for entrepreneurs 45+ (CP-SVC-021) | Pool: waits for the pivot talk | DROP | Waiting for the talk. |
| C27 | Schwermetalle (CP-SVC-022) | Hüwel 24 Aug: only "abklären", no Ausleitung | DROP | Not offered as a page. |
| C28 | Detox, Darmsanierung, histamine test, training keywords (CP-SVC-023, 024) | Not offered by Hüwel | DROP | Cut in the pool. |
| C29 | Contact path: form first (CP-SVC-026) | Live: form on home, phone, sticky "Anrufen" and "Termin" bar. Hüwel confirmed form first (31 Aug) | DROP | Already done. |
| C30 | Positioning and target groups (CP-BRD-001, 002) | Live on home | DROP | Already done. |
| C31 | About page and intro video (CP-BRD-003) | Video transcript read 13 Oct. Two sentences claim effect | KEEP | E7 (video part). |
| C32 | Sie or du in the PDF (CP-BRD-004) | PDF live 13 Oct is in du. Site is in Sie | DROP | Seventh-card limit. Low impact on enquiries. Ask in the next round. |
| C33 | Qualifications with proof (CP-AUT-001) | Live list on home. More proof needs documents from Hüwel | DROP | Needs files, not a choice. |
| C34 | Proof bar with Google rating (CP-AUT-002) | Google profile: 10 reviews, 4.9 (13 Oct) | DROP | Folded into E2, variant B. |
| C35 | Build reviews, review kit (CP-AUT-003) | Programme task | DROP | Not a text choice. |
| C36 | Patient testimonials: check and rebuild (CP-AUT-004) | Live 13 Oct: 5 testimonials on `/` and `/heilpraktiker-nürnberg.html`. 3 describe a treatment success | KEEP | E2. |
| C37 | Memberships and logos (CP-AUT-006) | No logo files | DROP | Needs files. |
| C38 | Which page stands for "heilpraktiker nürnberg" (ST-01, open question in site tree) | Both pages live, each with its own canonical. Volume 1,000 (11 Oct). Search Console 90 days: 62 of 72 clicks on `/` | KEEP | E4. |
| C39 | Naming of the Bioscan (new, from Hüwel's note of 31 Aug) | "Bioscan" in title or heading on 4 live pages (13 Oct) | KEEP | E3. |
| C40 | GBP: remaining services, 8 FAQ, attributes, review replies | Hüwel approved all 7 GBP sections on 20 Aug and the selection on 14 and 17 Sep. Review replies are excluded by rule. Parking fact not confirmed | DROP | Already decided by the client or not verifiable. |
| C41 | GBP business name | Local Falcon scan data of 18 Aug shows the keyword name "Heilpraktiker & Homöopath Nürnberg - Gesundheitspraxis im Nürbanum Martin Hüwel". Memory says the agreed name has no keywords | DROP | Business name is an agency-only lock. Martin decides. Not re-checked on Google today. |
| C42 | Call button placement (design) | Live sticky "Anrufen" bar on every page | DROP | Already done. |
| C43 | Opening hours and NAP | Confirmed by Hüwel 29 Aug. Profile and DB match | DROP | Already done. |
| C44 | Homeopathy for menopause, Ernährungsberater, Banerji for cancer | Hüwel said no or HWG forbids (31 Aug, 11 Oct) | DROP | Ruled out. |
| C45 | Datenschutz section on Google Analytics | Exists as E1, status open | DROP | No duplicate. |

Counts: 45 candidates, 7 kept, 38 dropped.

## (c) Ranked KEEP list

Ranking rule: first the cards that protect the pages with the most traffic from legal risk, then the cards that move rankings. The home page gets 62 of 72 search clicks.

1. E2 Erfahrungsberichte auf der Startseite. Main page, 3 of 5 quotes describe a success. Hüwel was warned in 2018.
2. E3 Messverfahren "Bioscan". Hüwel raised the risk himself. It blocks the planned expansion of two pages.
3. E4 Welche Seite steht für "heilpraktiker nürnberg". Biggest local keyword (1,000 per month). Two near-identical pages compete.
4. E5 Magnetfeldtherapie in der Überschrift. 9,900 searches per month in Germany. The word is missing on the site. Local value is small (10 for Nürnberg).
5. E6 Drei Blog-Beiträge mit Wirkaussagen. Same legal risk as E2, but low traffic.
6. E7 Vorstellungsvideo. Same legal risk, but the video has 6 views.
7. E8 Anliegen-Seiten. Good rankings potential, but it needs texts first. The decision unlocks the writing work.

Top 3 to ask first: E2, E3, E4.

The recommended variant ("741 empfiehlt") is always A.

## (d) Dashboard readiness

Checked on 13 Oct 2026 with free reads only. No scan, no paid call.

| Source | Ready? | Evidence | Gap | Owner |
| --- | --- | --- | --- | --- |
| Search Console | yes | Service account is full user on `https://www.praxis-huewel.de/` (property list, 13 Oct). Daily read works: 28 days to 10 Oct = 32 clicks, 1,057 impressions. 90-day export of 11 Oct is saved in `content-pool/03-demand/` | The data mixes the old and the new site until 6 Oct. Newest days are 2-3 days late. Only the URL-prefix property with www | agent |
| GA4 | no | Property "HP-Praxis Hüwel" 288143997 (account "Martin Hüwel" 127216899). The service account gets 403 on it. Account summaries show 4 accounts, none with Hüwel. Events (generate_lead, phone_click, whatsapp_click, email_click) are live only since 13 Oct, and only after cookie consent | Add `reporting-bot` as viewer on the account "Martin Hüwel". Key events are not marked yet (work item "planned"). No history before 13 Oct. Counts only visitors who consent | Martin (GA admin in the 741studio18 login); then agent |
| Local Falcon: Google profile actions | yes | `getLocalFalconGbpPerformanceMetrics` for `ChIJP9pcB-1Wn0cREo1vNZHFGC8`, daily from 1 Oct 2025 (378 days). Totals: 19 call clicks, 150 website clicks, 574 direction requests. 1 Sep to 13 Oct: 0 calls, 26 website clicks, 33 directions | We store nothing. The newest 2-3 days fill late | agent |
| Local Falcon: reviews | yes | 10 reviews, 4.9. 7 with a reply, 3 without | Rule "no review answering" stays. Show the count only | agent |
| Local Falcon: map ranking | partial | 9 saved scans. Last Maps scan 18 Aug (7x7, 5 km). Frequenztherapie 87.76 % share of local view, Homöopathie 28.57 %, Heilpraktiker 6.12 %, Bioresonanz 0 %. One older scan on 3 Aug uses another setting (9x9, 2.5 km) | No rescan since 18 Aug, so no trend. Each rescan costs credits (49 per 7x7 scan). The 49 grid points are not saved in our files | Martin (go for a rescan); agent (save points) |
| Local Falcon: AI answers | partial | 2 AI scans of 18 Aug (5x5 = 25 points): ChatGPT 0 of 25, Google AI 4 of 25 | One run only. Show "x of 25 spots" with date. No trend | agent |
| Portal leads | no | `site_form_submissions` has 0 rows. `leads` has 0 rows for this client. Forms run since 6 Oct | Unknown if no enquiry came or if the flow does not store. Test the form path once | agent; Martin confirms with Hüwel |
| Google Ads | no | No Ads account or campaign for this client found in memory or files. Not checked in the Ads UI | Not applicable unless ads start | Martin |

## (e) Open data gaps and risks

1. **Approver missing.** No `client_approval_settings` row exists. E1 is open and visible to the client, but nobody can decide it. The drafts file inserts a row with `approver_user_id` empty. Candidate: user `8a596070-1f02-4452-810d-4d3d738df1c7` ("Martin Hüwel", role client). Martin confirms before it is set. Owner: Martin / main session.
2. **E1 breaks when `health_client` becomes true.** The guard trigger blocks every update of a non-draft row with `hwg_checked` false. A client decision on E1 would fail. Before the settings insert, set `hwg_checked` on E1 (Martin says the wording is checked), or insert the settings row later. Owner: Martin / main session.
3. **E1 has no reminder or due date.** `remind_at` and `due_at` are empty on the open row. Owner: main session.
4. **GA4 not readable** by the service account (see section d). Owner: Martin.
5. **No form submissions stored** since 6 Oct. Cause unknown. Owner: agent.
6. **No Maps rescan since 18 Aug.** Owner: Martin (go).
7. **GBP business name** may still be the keyword version (scan data of 18 Aug). Not checked on Google today. Owner: Martin.
8. **Not verified:** whether Hüwel accepts the word "Magnetfeldtherapie". He did not list it in his service selection of 14 and 17 Sep. The GBP report listed it earlier. E5 asks him.
9. **Not verified:** the exact legal status of the quoted sentences. All texts stay `hwg_checked` false until Martin checks them.
10. **Not covered:** the 10 "Änderungswünsche" in work item intake (13 Oct). The report feedback of 31 Aug was read. Banerji, PostVac and menopause points are already decided.

## Review round 13 Oct 2026 (Martin in the Claude chat)
- Released (open, due 20 Oct, reminder 17 Oct): E2, E3, E5, E6, E8, and E7 (rewritten, see below). E1 was already open: HWG check set, reminder and due date added.
- E4 deleted: Martin says the homepage is the main page. The second page `heilpraktiker-nürnberg.html` becomes a 741 job (merge and redirect), only after Martin's go for the site change.
- E7 rewritten by Martin's idea: the video is already embedded; the card now asks whether it moves large into the hero (A), stays (B), or is re-cut first (C). The legal note about "sehr effektiv" stays in the card.
- Approver set: `client_approval_settings.approver_user_id = 8a596070-1f02-4452-810d-4d3d738df1c7` (Martin Hüwel, info@praxis-huewel.de). No email goes out on release (digest not active). Martin tells Hüwel himself.
- hwg_checked = true set on E1, E2, E3, E5, E6, E7, E8 with Martin's yes ("Martin (via Claude)").

## Grill result 13 Oct 2026 (Martin, in the main chat — done there, not here)
- E1, E2, E3, E5, E6, E7, E8 released (status open, due 20 Oct, hwg_checked true). Approver set: info@praxis-huewel.de.
- E4 ("Welche Seite steht für Heilpraktiker Nürnberg") deleted. Reason: Martin says the homepage is the main page, so no merge question.
- E7 rewritten: now asks whether the existing intro video moves large into the homepage hero (A, recommended), stays where it is (B), or is re-cut first to remove the two effect-claim sentences (C).
- This client is DONE. Do not open or change his cards again from this session.
