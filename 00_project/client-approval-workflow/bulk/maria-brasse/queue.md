# Maria Brasse (ShuiGuru): decision card queue, 13 Oct 2026

## (a) Client facts
- Client: Maria Brasse, ShuiGuru, client_id `444ac77b-747d-4855-89e5-12ac97d2363c`, mode program, status active, lang `de`.
- Address form: Martin writes "du" to Maria. The live website speaks to visitors with "Sie" (checked on 15 URLs). Card text is "du". Website variants are "Sie".
- Live site: https://shuiguru.de (WordPress, GeneratePress). All 11 pages from the rollout of 25 Sep are live. `/feng-shui-grundriss/` is 404 (Martin: later, 25 Sep).
- Health: `health_client = true` as a precaution. Reason: the live site has therapy wording ("Quantenheilung", "heilender Prozess", "Heilrituale", "Heilpraktikerin für Psychotherapie", case study with "psychohygienische Gespräche"). Maria offers room consulting, not treatment. Martin can set it to false. No variant makes a healing promise or a success guarantee.
- Approver: NOT set. No row in `client_approval_settings`. A client profile exists (user_id `44edf23a-c80a-4c49-90d9-58fcc42f4c19`, role client, "Maria Brasse"). The brief says approver NULL. Without an approver Maria cannot decide. The main session must set it.
- Existing cards in `approval_items`: 0. Codes start at E1.
- Tools used: curl on public pages, Supabase SELECT only, the reporting-bot token (read only, no write). No paid call. No scan.
- Novamira `novamira-shuiguru-de`: not used. The live pages gave all the facts.

## (b) Candidates (16)

| ID | Idea | Verification | Result | Reason |
|---|---|---|---|---|
| C1 | Review incentive box on /kosten/ and /online-beratung/ | Live pages 13.10.: box "Kostenlose Online-Beratung gegen Google-Bewertung" until 15 Oct. Feedback 02.09. and 21.09. (Maria's own idea and text). Google rule: no reviews for a gift or a service. | KEEP (E1) | Real risk to the profile. Real choice, 3 options. Ends 15 Oct. |
| C2 | FAQ "Was macht eine Feng-Shui-Beraterin?" on Über mich | Live page 13.10.: no such question. Volumes 320 / 260 (31.08. analysis). PAA seen 08.10. (report page `maria-faq-fragen-2026-10`). | KEEP (E2) | Money terms. Maria has not answered the 08.10. page. |
| C3 | FAQ garden: neighbours | Live /feng-shui-garten/: grep "Nachbarn" = 0. 90 searches (08.10.). | KEEP (E3) | Garden cluster is the biggest niche (720). Garden Local Falcon 08.10.: ARP 2.10, 85.7 %. |
| C4 | Startseite "5 Schritte" | Live 13.10.: block unchanged. Maria 17.09.: wants to rethink. No later change in DB or memory. | KEEP (E4) | Her own open point. Status after 24.09. not fully proven (see gaps). |
| C5 | FAQ office: Reichtumsecke | Live /feng-shui-in-der-arbeitswelt/: no answer. /feng-shui-arbeitszimmer/ has one (her text). 320 searches. | KEEP (E5) | Variant A copies her own Homeoffice answer. |
| C6 | FAQ Plancheck: "wissenschaftlich belegt?" | Live /plancheck-vor-baubeginn/: no such question. 260 searches. | KEEP (E6) | Needs her stance. The 741 draft of 08.10. had an unsourced claim ("deckt sich mit dem, was heute messbar ist"). Removed. |
| C7 | Wording "Positive Resultate sind vorprogrammiert" and "Heilrituale" on /kosten/ | Live 13.10. (grep: 1 hit each). Text is from her feedback 22.09. | KEEP (E7) | Success guarantee. Low effect on enquiries. Protects against a warning letter. |
| C8 | Garden FAQ: fountain, small garden | Not live. 40 / 110 searches. | DROP (merged) | Near-duplicate of C3. Said in the E3 note. Next round. |
| C9 | Name: "Feng-Shui-Beraterin" or "schamanische Raumberaterin" | Maria's doubt is from 14.09. Live H1 on Über mich still "Feng-Shui-Beraterin". She approved the live pages (24.09.). No search volume for the other term. | DROP | Not proven open. No data for a recommendation. Martin talks to Maria. |
| C10 | Header tagline "Lern- und Arbeitsverbesserung durch Raumoptimierung" | Live header 13.10. Martin 08.10.: sitename stays. | DROP | Decided. |
| C11 | Hero photo of the Startseite (glasses) | Live hero image read on 13.10.: glasses, eyes down. | DROP | Done. |
| C12 | "Käffchen vereinbaren" button in hero | Live 13.10.: button is in the hero. | DROP | Done. |
| C13 | Grundriss page (4 directions) | /feng-shui-grundriss/ = 404. 50 searches. Martin 25.09.: "Grundriss → später". | DROP | Deferred by Martin. Low volume. Plancheck covers it. |
| C14 | GBP photo set (9 images, 6 AI portraits) | Folder `gbp-fotos-2026-10`. Martin 05.10.: Maria may use AI images. Martin uploads. | DROP | Decided. No client choice. |
| C15 | GBP posts, categories, hours, services | Done 30.09. (categories, hours 10 to 19, 17 services). Posts: "nicht freigegeben". | DROP | Done or ruled out. |
| C16 | City pages Munich / Hamburg, testimonials block | Volumes 50 / 20. "Das sagen Kund:innen" has no quotes to choose from. | DROP | Low impact. Needs content from Maria, not a choice. |

Also seen, not a card (site defects for Martin): `/kaeffchen/` shows the line "E-Mail – Und hier gehts direkt zur Tipselwelt" (old text). `shuiguru.de` has no SPF record (Martin 25.09.: later). Instagram link stays (Martin 25.09.).

## (c) Ranked KEEP list

1. E1 Kostenlose Kurzberatung "gegen Google-Bewertung". Reason: legal risk for the profile, and the action ends on 15 Oct.
2. E2 FAQ "Was macht eine Feng-Shui-Beraterin?". Reason: the two money terms (320 and 260) are the biggest commercial terms.
3. E3 FAQ garden: neighbours. Reason: garden is the best niche (720 searches, map share 85.7 %).
4. E4 Startseite "So läuft die Beratung". Reason: she asked for it. It helps the enquiry path.
5. E5 FAQ office: Reichtumsecke. Reason: 320 searches, no answer on the page.
6. E6 FAQ Plancheck: "wissenschaftlich belegt?". Reason: 260 searches, needs her stance.
7. E7 Wording "vorprogrammiert" / "Heilrituale". Reason: protects against a warning letter. Little effect on enquiries.

Ask first: E1, E2, E3. E2, E3, E5 and E6 are the same ask as the open report page of 08.10. (6 questions, no answer from Maria). Martin should take that page out of the portal after release, so Maria does not answer twice.

## (d) Dashboard readiness (13 Oct 2026)

| Source | Ready? | Evidence | Gap | Owner |
|---|---|---|---|---|
| Search Console | partial | `reporting-bot` does NOT see shuiguru.de (list of 6 other sites, 13.10.). Chrome read 30.09. under 741studio18: 90 days = 2 clicks, 17 impressions, 2 pages indexed. Sitemap index sent 30.09.; indexing asked for 11 pages (30.09.) and Über mich (08.10.). | Add `reporting-bot` as full user on `https://shuiguru.de/`. New numbers need a fresh Chrome read. | Martin |
| GA4 | partial | Tag `G-8B0M7DXENR` is in the homepage HTML (13.10., after consent). Property 271568278. Reporting-bot gets 403 on the property; the account is not in the account list (4 accounts). Data only since 30.09. | Give `reporting-bot` Viewer on the property. Mark `generate_lead` as key event after the first real form lead. Little traffic so far. | Martin |
| Local Falcon (free reads) | partial | Local Falcon is not connected in this agent. Saved values (memory): garden 08.10. ARP 2.10, SoLV 85.7 %, 49 of 49 spots (report `cb390c619f7c04b`); 30.09.: beratung berlin 9x9 ARP 1.52, SoLV 92.6 %; hausbau 7x7 ARP 1.53, SoLV 91.8 %. Heatmap file `00_project/assets/maria/falcon/garten-2026-10-08-cb390c619f7c04b.png`. | Büro report `70019e154a403a7` is gone (not found). Büro and beratung need a new scan (credits, Martin's go). The profile is not connected by OAuth, so there are no call or click numbers. Review count today: not read (3 unanswered on 30.09.). | Martin (go), agent |
| Google Business Profile numbers | partial | 264 interactions Apr to Sep, Aug 51, Sep 57 (Chrome read 30.09.). | No stored series. Not connected. | Martin |
| Ads account | no | No Ads account for Maria in memory or in the DB. Not part of her plan. | None. | n/a |
| Portal leads | no | `leads` 0 rows, `site_form_submissions` 0 rows (13.10.). The contact form (WPForms Lite) mails to Maria and stores nothing. | No lead capture. GA4 `generate_lead` is the only trace. | Dinakar |
| Listings | yes | `client_citations`: 25 submitted, 31 planned, 1 live (13.10.). | Live check from about day 7. | agent |
| AI answers | partial | ChatGPT beratung berlin: rank 21 to 2.5, share 0 to 44 % (30.09.). `visibility_prompts` 0 rows. | No stored prompts. | agent |
| Programme state | yes | 2 `work_items` (one intake: "45 Änderungswünsche aus Reports sichten (Status unbekannt)"). Week 5 on 14.09. start. | The intake item is open. | Dinakar |

## (e) Open data gaps and things I could not verify
- Google review count and rating today: not read. Local Falcon is not connected here. Public Google Maps gave no data by curl.
- Whether Maria settled the "5 Schritte" order after 24.09. by phone or mail. The 28.09. mail is not in the DB.
- Whether the 15 Oct action still runs. The page says yes. A card released later than 15 Oct needs a new look at E1.
- Volumes for E2, E5, E6 come from the 31.08. and 08.10. data runs. They were not re-run (no paid call).
- Google's review rule is stated from the public Google Maps policy. I did not open the policy page in this run.
- Approver for the decisions is missing (see (a)).

## Grill result 13 Oct 2026 (Martin in chat)
- Maria is NOT a health client any more (health_client = false). Approver set (portal login Maria Brasse).
- E2, E3, E4 released 09:01 UTC, E5, E6, E7 released later the same hour. All with the recommended variant A as drafted.
- E1 (review box) taken out, no card. Reason: Martin does not want it as a topic. The box is Maria's own text and ends 15 Oct. Optional cleanup: remove the box on 16 Oct.
- The client sees codes E2 to E7 (E1 is a gap, display only).
- Loose end: E2, E3, E5, E6 repeat the open FAQ report page of 8 Oct in the portal. Take that page out after Maria answers.
