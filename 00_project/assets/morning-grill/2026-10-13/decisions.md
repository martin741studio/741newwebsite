# Decisions 2026-10-13 (first real grill, Martin in chat)

1. **741 (all clients)** — 5 clients have unread portal messages or help requests. Who answers today?
   → a: Agent drafts every reply; Martin sends
2. **741** — Deadline 2026-09-23 from memory has no 'done' note (20 days overdue): Demand: sign strafbewehrte Unterlassungserklärung 
   → other: Martin answered with his own letter (based on the agent's recommendation) demanding to pay 0 €; waiting for the lawyer's reply
3. **Bali Healing** — Deadline 2026-10-01 from memory has no 'done' note (12 days overdue): **2026-09-07 ROOT CAUSE for blocked skin-tag publi
   → a: Still open: agent prepares next step today (read-only Ads check + document list)
4. **Praxis Suriya** — Suriya: 5 approved site changes are blocked. The WordPress app password fails (401) and Search Console access is gone. R
   → a: Martin sends the ready reply today and asks for both accesses; backup + speed first
5. **Bali Healing** — Bali Healing: onboarding 1/6, Ads blocked, and the 8-point status reply cannot go out: it still needs outreach counts an
   → a: Martin gives the two numbers today; agent finishes the reply + Ads checklist
6. **Marcel Rosenbach** — Marcel wants to come to 741 fast: new website with monthly subscription plus Google Ads. Which offer goes out this week?
   → other: Sequence: landing page (in progress now) -> Martin's intro video -> prototype for Marcel -> Ads
7. **Praxis Suriya** — Praxis Suriya: 28 directory confirmation emails are unhandled. Verify links can expire.
   → b: Agent lists the 28 emails first; Martin decides

## Round 3 (after the Command Center, 12:40)
- **741 (workflows)** — Where should the Command Center live? → Portal admin view on staging, after the Freigabe-Dashboard chat finishes (one writer per portal file)
- **741 (all clients)** — Set stale portal flags after the replies are sent? → Yes, after Martin sent the 5 replies
- **Bali Healing** — Continue Bali audit + content pool? → Go for both
- **Praxis Hüwel** — Add GA4 (with consent) to the Hüwel website? → Yes, prepare on a test branch; live change needs a per-change go

## Round 4 (status check 14:40, Martin in chat)
- Sent today: Stürzl email, Bali group message, Coralie role ask. NOT sent yet: the 5 portal replies.
- Clicks done today: Dumann Wix Publish. NOT done yet: Bali NIB upload, Stürzl GSC user, Local Falcon toggles.
- **Kamil** — Aug + Sep report → into his dashboard (Reports tab); agent drafts a 2-line message for Martin.
- **STÜRZL** — 7 drafted decision cards → put them live now (with backup).

## Round 5 (14:45)
- **Talkinfive** — Meta Pixel: split by region (fire at once outside Europe, wait for Accept in Europe).
- **Praxis Suriya** — listing emails: agent only lists them (list: suriya-listing-emails.md); no portal write; Martin decides per sender.
- **Praxis Suriya** — start date = 03.09. (portal). Martin: answered several times already. Cause: the answer was never written back; goal sheet held "conflict", memory said 14.08. Fixed in goals.json + memory.
- **Bali / Gayo** — Martin asked why. Source: the 'Progress' and 'Reports' tabs are template copies from another client with no Bali data; real numbers are in Leads + Pipeline and now per account in the portal. Agent drops task t20 (no value now).
- **Praxis Hüwel** — start date: false conflict. '16.08. paid' came from the Only Inside invoice RE0826093 (CMS cost), not from 741. Goal sheet set to portal date 25.08. (agent fix; Martin can overrule).
- **Process fix** — the grill now writes start-date answers into goals.json + memory at once, so the detector does not ask again.
- **STÜRZL (15:00, correction)** — Cards were NOT released (decision-cards chat: drafts only; 6 cards E1–E6, Tax Compliance card dropped as unverified). Martin: E3 recommendation = Entwurf B (no reason given). Login: create Stürzl portal login + approver now, NO welcome mail; Martin sends the mail later via Airmailer. Then release E1–E6.
- **Bali Healing (15:10)** — Pasha's request (tracker sheet, video testimonials + Similar Treatments per landing page, blog SEO later; due Fri 16.10.) routed to the Bali client chat. Live Wix changes need a per-change go.

## Round 6 (15:30, Martin on phone)
- Bali NIB: Martin does not have it → WhatsApp request to Peggy drafted (slop 5/5), Martin sends.
- Portal replies: GO to post all 5 in the portal ("just do it") → portal-replies chat, with fact re-check (Hüwel GA4 now live, Suriya GSC removed); then stale flags.
- Stürzl GSC user: GO ("just do it") → Stürzl chat via Claude in Chrome.
- Local Falcon: NOT in this account's connector list at all (status check 15:30) → toggles cannot fix it; needs to be added as a connector by Martin.
- Stürzl login + E1–E6: decision-cards chat accepts the go only typed in its own chat; text given again.
- Mac restart: no.
- Prospects (Claudia Loom, Gunkel send): later.
- **Rule (15:45)** — client requests go onto the client dashboard, not as WhatsApp texts for Martin. NIB request → Bali dashboard (Bali chat). Stürzl GSC: already done (Martin) → Stürzl chat told to stop.
- **STÜRZL (done)** — login created (anja.stuerzl@googlemail.com, approver, no mail sent), E1–E6 live, due 20.10., reminder 16.10. Backup: 00_project/client-approval-workflow/bulk/stuerzl/backup-pre-release-2026-10-13.json. Open: Martin sends the welcome mail (Airmailer) with password reset.
- **Portal replies (16:00, done by grill chat on Martin's live go)** — 5 posted as sender '741': Suriya 005b0cc2, Hüwel e3777559 (updated GA4 text), Dumann 995b0017, Brasse 7d041abf, Rabenmütter 16913676. Flags: Dumann + Rabenmütter domain → entfaellt; Suriya Search Console + Website → angefragt (Coralie removed / viewer only). Suriya FB message marked read. Backup: backup-portal-replies-2026-10-13.json (rollback = delete the 5 message ids, restore rows).
- **STÜRZL login (16:15)** — Martin: address = stuerzl@stuerzl-steuerstrafrecht.de. Changed auth.users + identity + clients.contact_email (was anja.stuerzl@googlemail.com, never signed in). No mail sent.
- **Talkinfive (16:10)** — GO live with Opt out → Talkinfive chat pushes + tests live.
- **Kamil (16:10)** — one message: report in dashboard + website malware incident; Kamil chat drafts it from confirmed facts only; Martin sends.
- **Bali NIB (16:30)** — Martin uploaded the NIB here (stored 00_project/assets/balihealing/docs/PT_AMANA_EVENTS_INDONESIA_-_NIB.pdf). Dashboard request cancelled; Bali chat uploads it in Google Ads (client verification) on Martin's go.
- **Bali Ads verification (status)** — not submitted by agent: Google also needs a personal ID of the submitter (stop point). Martin finishes it in the open Chrome tab (Advertiser Identity, new payments profile Indonesia/Organization, PT Amana Events Indonesia, address from NIB). New Google deadline 31.10.2026. No dashboard item created.
- **Bali Ads verification DONE (13.10.)** — under 741studio18@gmail.com: existing verified org payments profile 'PT. Amana Events Indonesia' selected; 'Advertiser identity verified'. Pause banner gone; 'Ozone – Search – Bali' Eligible (limited by bid strategy). Remaining funds IDR 103,892. Next decision (card): Google 'Apply for healthcare certification' for skin tag / mole removal ads.
- **Bali Ozone (16:45)** — Martin: Ozone campaign must STAY PAUSED (it became eligible again after verification). Go to pause → Bali chat. Skin tag campaign: Bali chat checks if it still exists (read-only) and brings cards.
- **Bali Ads final (13.10.)** — Skin tag campaign 24355357384 PUBLISHED (Martin's go): Eligible (Learning), Max clicks cap IDR 12,000, budget IDR 19,766/day, 14 phrase keywords, 1 RSA, landing /skintagandmoleremoval. Ozone paused (Martin). Old IDR 90,000 draft discarded. Healthcare certification not applicable. Balance IDR 103,892 ≈ 5 days.
