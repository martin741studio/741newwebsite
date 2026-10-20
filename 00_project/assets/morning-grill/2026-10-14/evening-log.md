# Evening log 2026-10-14 (WITA) · draft 17:00 · status: draft

Sources since the morning bookmark (05:44 WITA): S1–S13, 32 sessions, 34 transcripts read (unreadable: S8_tracking — tracking workflow not built yet).
Command Center tab "Today" shows the same 5 checks (snapshot id=21, evening).
Tasks: `evening/tasks.json` (46 total; 9 statuses updated from today's chats: t15, t25, t27, t29, t35, t38, t39 → done; t08 → in_progress; t33 → waiting). Live with Martin afterward: t14, t32, t42 → dropped (stale/not needed, see client sections below); t13 was already dropped live as a duplicate.

## 1. Roadmap — where each client stands
| Client | Phase | Week | Track (OFF = overdue portal tasks) | Next step |
|---|---|---|---|---|
| Bali Healing | P1 Onboarding | 5 | OFF (22 overdue portal tasks) | Next workflow: audit follow-up, pool |
| Praxis Suriya | P4 Build-up | 6 | OFF (5 overdue portal tasks) | First Falcon scan after cycle reset ~19.10. |
| Daniela Dumann | P4 Build-up | 5 | OFF (4 overdue portal tasks) | Next workflow: pool → sitetree, copy |
| Praxis Hüwel | P4 Build-up | 8 | OFF (2 overdue portal tasks) | GBP round 2 (FAQ, review replies, ~19 services) |
| Maria Brasse | P4 Build-up | 5 | OFF (15 overdue portal tasks) | Next workflow: citations live checks |
| Rabenmütter | P4 Build-up | 5 | OFF (6 overdue portal tasks) | not set |
| Taxi-Zentrale Nürnberg | P4 Build-up | – | UNKNOWN (no portal program) | Akeeba key still not pasted; spam source traced to RSForm! Pro, fix confirmed live |
| Marcel Rosenbach | P0 Prospect | – | UNKNOWN (no portal program) | Landing page → Martin's intro video → prototype → Ads (paused on his text choice) |
| me&you / Pauspapier | P4 Build-up | – | UNKNOWN (no portal program) | Next workflow: cro checkpoint 3 |
| Kamil (Physio Anatomie + Kraft) | P6 Proof + Quarter | – | ON (no overdue portal task) | Move the monthly numbers into his dashboard, prepare recommendations |
| STÜRZL Steuerstrafrecht | P1 Onboarding | 0 | ON (no overdue portal task) | Rate-1 payment = start date |
| Johni Jaya Motor | P1 Onboarding | 9 | ON (no overdue portal task) | Access: GA4, GBP, GSC — GBP setup is what is left |

## What agents did while you were away
- Suriya chat — WordPress access reconfirmed, DB backup run, WebP conversion started (timed out mid-batch); Backlink-DACH workflow started (€500/mo, your override go) [b88add01]
- Suriya chat — checked Coralie's "Google penalty" claim: no real penalty found, almost certainly a scare-tactic upsell pitch; reply drafted but held back for your direct word, not a relay [c6d4a4c5]
- Hüwel chat — dashboard feed built from GSC+GA4+citations (Bali pattern, per-client now); results verified against Google (clicks 14→33, position 17.9→6.6); Local Falcon after-scan: 2 of 6 keywords both improved [8ccce35e, e8aede79, 29457cca]
- Dumann chats — "Dein SEO-Fahrplan" status page published live; all 25 decision cards (E1–E25) released across today's approval rounds; 3 mobile cutoff fixes published live [065572cb, 0d991c89, c02ee9da]
- Bali chats — all 10 Beauty landing pages got the Similar Treatments section, published and link-checked; program checklist re-verified (6 genuinely done of 19 flagged) [76ee66f6, e9c4af07]
- Kamil chat — yearly security/backup offer (€500/year) drafted and sent same day; CRO homepage start card proposed, held since he didn't pick it [e418e89f]
- Taxi Nürnberg chat — spam source traced to the RSForm! Pro licence (not the GDPR plugin), now updated to 3.4.10; cookie-banner updater email fixed; everything tested live [c072bfc1]
- Stürzl chat — confirmed no existing Google Ads account anywhere; decision card E8 released recommending a new account under the client, 7-day deadline [5a89f936]
- Marcel chat — NLP campaign test mail sent and forwarded with 2 contradictions flagged; UptimeRobot alert path finalised (email, not Telegram) [c4cdeb06, 395e0ce8]
- Talkinfive chat — the Meta pixel leak on the Opt-out button (SubscribedButtonClick firing wrongly) found and fixed, tested live [687c567d]
- Rabenmütter chat — DataForSEO IP whitelist confirmed already working; 2 product-page items correctly re-split and ticked [7b5d9fd7]
- Johni Jaya Motor chat — checklist re-verified: hours/booking actually done too, FAQ still the real gap [701c3ead]
- 741 internal — laptop malware check closed (Hostinger VPS likely reassigned after expiry, not an active breach — still needs your password/SSH rotation); Google Drive verified end-to-end on the server; booking-sequence workflow installed (29/29 gate); command-center board deduplicated (19 duplicate rows removed) [035ae64f, 06e79636, aa2e132e, 30889ca1]
- Prospects — review page for Manuela Stetter built, fact-checked and live; follow-ups sent to Zubair and Adel [76b92d80, fea2ab3e]

## Praxis Suriya (P4, active, week 6)
- **Done:** Backlink-DACH workflow started, €500/mo (your go) [b88add01]; WordPress access + DB backup + mobile speed check (60) [b88add01]; review strategy built, card E8 released with the QR materials page live [c455b423]; footer Impressum/Datenschutz fix done and verified live, 18:58 WITA (fresh UpdraftPlus backup first) [c6d4a4c5]
- **Open:** Dinakar — backup/image-optimisation/caching/CSS-JS cleanup; agent — WebP batch needs resuming after the timeout; agent — PR/guest-article slots (weeks 3–5) still fully untouched
- **Tomorrow:** resume the WebP batch, keep going on PR/guest-article slots
- **Blockers / waiting for:** Tantri (directory verify links), client (GSC access, since 12.10.)
- **Resolved tonight:** the Coralie scare-tactic reply — not sent. You called it old news/not needed, both in the Suriya chat (18:58 WITA) and again here when I asked. Portal task dropped.

- **Late update 21:30 (from the Suriya chat):** live today with Martin's go: image/WebP + LiteSpeed (mobile PSI 85); decisions E1–E7 applied, Migräne-Analyse page 301 → Cranio page; GTM v3 with GA4 event anruf_klick. BrightLocal + 28 directory emails = day work 15.10. in the Suriya chat (login via 'eingeloggt?' card). Search Console row → 'ausstehend', 741 restores it itself.

## Praxis Hüwel (P4, active, week 8)
- **Done:** Dashboard feed built and verified against Google (clicks 14→33, position 17.9→6.6) [8ccce35e, e8aede79]; Local Falcon after-scan: heilpraktiker + bioresonanz both improved [29457cca]
- **Open:** agent — mark phone_click + email_click as GA4 key events
- **Tomorrow:** mark the 2 GA4 key events — owner agent
- **Blockers / waiting for:** your approval on the pool result since 2026-10-11; 4 Local Falcon keywords still unscanned until credits renew 19.10.

## STÜRZL Steuerstrafrecht (P1, active, week 0)
- **Done:** confirmed no existing Google Ads account anywhere (GA4, site tag, 741 managers) [5a89f936]; card E8 released recommending a new Ads account, 7-day deadline [5a89f936]
- **Open:** your decision on card E3 (A or B, recommendation B)
- **Tomorrow:** your E3 decision — owner Martin
- **Blockers / waiting for:** your approval on 4 results since 2026-10-11 (audit, cro, pool, cro_b); client's answer on card E8 (since today)
- **Resolved tonight:** the "program start date still not set" card was stale — the goal sheet already had program_start = 2026-10-07 (rate-1 payment landed about a week ago, as you said), it just never cleared the old blocker. Fixed the goal sheet and dropped the stale portal task; the 52 program tasks and 8 Ads-setup tasks are no longer blocked on this.

## Daniela Dumann (P4, active, week 5)
- **Done:** "Dein SEO-Fahrplan" status page published live, all 25 decision cards (E1–E25) released across 2 approval rounds [065572cb, 0d991c89]; 3 mobile cutoff fixes published live [c02ee9da]
- **Open:** agent — route the design-approval record and the Maps-name mismatch to her as dashboard items (no self-fix, new rule 14.10.); Martin — send her the portal message pointing at the new status page; Martin — grill her 7 waiting decision cards next
- **Tomorrow:** send the portal message, then the grill round — owner Martin
- **Blockers / waiting for:** your own Wix-publish click for the 3 saved subpage fixes is still held — the new rule says her feedback comes first

## Bali Healing (P1, active, week 5)
- **Done:** all 10 Beauty landing pages got Similar Treatments, published and link-checked [76ee66f6]; tracker sheet updated [e9c4af07]
- **Open:** agent — drag staged content-pool files into Drive; agent — Pasha's tracker (video testimonials still open); Martin — answer Pintor's questions then send the status reply; Martin — Go-C for the English audit page
- **Tomorrow:** your status reply to Pintor/Pasha, then the Ads top-up — owner Martin
- **Blockers / waiting for:** client — NIB PDF of PT Amana (deadline 2026-10-15); your Ads top-up (GoPay, IDR 500,000) deferred to "later today" by you, still not done; Google — verification 1–10 days after the NIB upload

## Maria Brasse (P4, active, week 5)
- **Done:** FAQ drafts for the 4 pages with no FAQ, from last night's queue
- **Open:** Martin — answer the question on card E1 (E2–E4 release already started)
- **Tomorrow:** your E1 answer — owner Martin
- **Blockers / waiting for:** your approval on the prospect result since 2026-10-13

## Rabenmütter (P4, active, week 5)
- **Done:** DataForSEO IP whitelist confirmed already working, no new entry needed [7b5d9fd7]; 2 product pages correctly re-split and ticked [7b5d9fd7]
- **Open:** none new today
- **Tomorrow:** no action queued — quiet beyond today's confirms
- **Blockers / waiting for:** none new

## Kamil (Physio Anatomie + Kraft) (P6, active)
- **Done:** yearly security/backup offer (€500/year) drafted and sent same day [e418e89f]; CRO homepage start card proposed, held since not picked [e418e89f]
- **Open:** agent — cleanup of physiotherapiekraft.de + full scan of the Oberhausen site; agent — find the real ad-disapproval reason (mail says "online gambling", account says "unreliable claims")
- **Tomorrow:** your Ads decision (pause or keep Kraft Ads while the hacked site is closed) — owner Martin
- **Blockers / waiting for:** your Ads pause/keep decision, no date given yet

## Taxi-Zentrale Nürnberg (P4, active)
- **Done:** spam source traced to the RSForm! Pro licence, now updated to 3.4.10; cookie-banner updater email fixed; site/calculator/forms all tested live [c072bfc1]
- **Open:** none — you called it done for now
- **Tomorrow:** nothing queued
- **Blockers / waiting for:** none
- **Resolved tonight:** you said Taxi-Zentrale is basically done. The Akeeba-key task was already dropped live as a duplicate; the Daniel-reply task is now parked at your word too.

## Marcel Rosenbach (P0, active)
- **Done:** NLP campaign test mail sent, forwarded to Marcel with 2 contradictions flagged [c4cdeb06]; UptimeRobot alert path finalised [395e0ce8]
- **Open:** Martin — the landing page → video → prototype → Ads sequence
- **Tomorrow:** nothing starts until Marcel answers which campaign text is correct
- **Blockers / waiting for:** team — Marcel's answer on the campaign text (1-year vs 2-year access, hot-seat sessions in/out), since today

## Johni Jaya Motor (P1, restart, week 9)
- **Done:** checklist re-verified — hours/booking genuinely done too, FAQ confirmed the real gap [701c3ead]
- **Open:** agent — access check + client message draft + re-plan of the 25 overdue tasks; Martin — enable the Local Falcon connector (2 switches in claude.ai); agent/Tantri — citations + review-engine briefing, confirmed genuinely untouched
- **Tomorrow:** enable the Local Falcon connector — owner Martin
- **Blockers / waiting for:** none new today

## me&you / Pauspapier (P4, active) — quiet
- **Open:** Martin — record the Loom, send the ready message to the group, set the go-live date for meandyou.de
- **Tomorrow:** your Loom recording — owner Martin
- **Blockers / waiting for:** none new; next workflow is cro checkpoint 3 whenever you start it

## 741
- Mac/laptop security: malware check closed (Hostinger VPS likely reassigned after expiry, not an active breach) — still needs your password + SSH-key rotation and the Atomic BI extension removed yourself [035ae64f]
- Google Drive verified end-to-end on the server; booking-sequence workflow installed (29/29 gate passed); command-center board deduplicated (19 duplicate rows removed, 8 marked genuinely done)
- Abmahnung RA Hirsch: 455,71€ payment decided, bank flagged an IBAN/name mismatch — your confirmation still needed before it's sent
- Parked since 2026-09-23: the other Abmahnung (pay 0€) still waiting on the lawyer's reply
- Review pages ready, not sent: Claudia Tiemann, Ana Violeta Fredel, Stephan Meyer, Claudia Maria Steifensand, Manuela Stetter, Sabine Schwarz, Catja Grieshaber, Christian Ruether
- Lead follow-up: Eri Trostl overdue (>7 days)
- Decisions taken today: 4 cards decided live with you on the phone at 06:00 (see `decisions.md`); 3 cards from the morning brief were not reached and stay open: `2026-10-14-741-messages`, `2026-10-14-deadline-coldemail-sending-in`, `2026-10-14-suriya-gsc-row`

## Portal-Updates (from the server-access chat [0307589a])
- 14.10.: Daniela Dumann's portal login (daniela.dumann@live.de) was reset, because her own password was unknown and was overwritten during a check. The new password is in the client vault (client_credentials, label "Portal-Login Kundin") on her client page. Martin sends her the new access today; she can change it in her profile. No message sent yet.
- 13.10.: STÜRZL login (stuerzl@stuerzl-steuerstrafrecht.de) got a password; it is in the client vault. The intro video for STÜRZL is hidden (client_stack.hide_intro).
- No passwords in this log.

## Carry-over to tomorrow's grill
- The 3 unreached morning cards: 741-messages, deadline-coldemail-sending-in, suriya-gsc-row
- Stürzl: your E3 decision
- Bali: Ads top-up still not done despite "later today"; NIB PDF deadline tomorrow (2026-10-15)
- 741: password/SSH rotation after the malware check, Hirsch payment confirmation
- Portal: "Erledigt" still forces a Nachweis-Link even for decision-type tasks (no deliverable to link). Documented in `00_project/client-work-visibility/data-model.md` — DB already allows a label-only evidence row, the task-card UI needs the actual fix.
