# Cross-chat open decisions, swept 14.10. ~06:40 WITA (Martin mobile, "lead me through open decisions of all chats")

Found by checking every running/recently idle session, not only today's grill cards.

1. Coralie/Suriya: third party ("Michael") pitched her an unverified "Google penalty" + 8,000 EUR rebuild in a voice note. Reply drafted, not sent.
2. Kamil Ads: both campaigns budget-limited; raise manually (money action, only Martin), revert 04.11.
3. Suriya: Impressum/Datenschutz pages exist, correct, just not linked in footer/nav — findability bug, needs go.
4. Kamil: ad disapproval reason mismatch (mail said "Online gambling", account shows "Unreliable claims") — not resolved.
5. Kamil: security/backup offer message ready (5/5), not sent; CRO Homepage run for Kraft site has a start card waiting.
6. Decision-cards chat: 28 cards still waiting across Dumann (7), Kamil (4), Rabenmütter (7), Johni (7) — which next?
7. Talkinfive: leak fix fully verified live; Billy message ready, still held per earlier "push only" answer.
8. Canary workflow: installed; 2 small gos open (UptimeRobot account C12, Telegram escalation group C11).

One-liners, no card needed yet:
- Taxi Nürnberg/Daniel: Akeeba licence was actually paid in April (~6 months left); Joomla wrongly shows it missing — message to Daniel not sent yet.
- Laptop malware chat: needs Martin to log into Hostinger hPanel and say "logged in" so it can check a mystery VPS's install date.
- Marcel chat: has its own pending card open right now — go there directly, content not retrievable from here.

## Round 1 answers (14.10. ~06:45)
1. Coralie reply → send now, as drafted. Routed to the scan chat (has WhatsApp access).
2. Kamil Ads budget → not now, no card returns automatically.
3. Suriya footer links → fix it. Routed to the scan chat (has Chrome access, already checked the pages).
4. Kamil ad disapproval → agent digs in today. Routed to the scan chat.

## Round 2 answers (14.10. ~06:50)
5. Kamil offer+CRO → send the offer message only; CRO Kraft start held.
6. Decision-cards backlog → Dumann next.
7. Talkinfive Billy → "Done cut this card no need anymore" — dropped, not sent, not raised again.
8. Canary gos → UptimeRobot (C12) only; Telegram group (C11) still open.

Routed to: Kamil chat, decision-cards chat, Talkinfive chat, Canary workflow chat.

## One-liners, resolved (14.10. ~07:00)
- Daniel/Taxi GDPR plugin: confirmed by Martin, licence is paid (April, ~6 months left) — just missing the Download Key in Joomla. Routed to the Taxi chat: fix the key + apply the pending 2.25→2.27 update, backup first.
- Laptop malware: Martin says done, closed. No Hostinger login needed.
- Marcel chat: Remote Control turned on so Martin can open it directly on mobile; also asked that chat to paste its pending question here.

## Correction (14.10. ~07:02)
Martin's "paid in April, 6 months left" recollection was wrong. He sent the real screenshot: a storejextensions.org (RSForm! Pro publisher) Joomla update-license screen shows "expired on: 2025-07-10" — over a year, not 6 months left. Taxi chat told to STOP and verify which extension (GDPR plugin vs RSForm! Pro vs other) before any fix or Daniel message.

## Suriya roadmap follow-up (14.10. ~07:30)
- "Rückfragen zeitnah beantworten" (week 1) marked erledigt — Martin confirmed done.
- Clarified: no client "Zoe" exists. Backlink-DACH pilot = Hüwel (90.7%, no live link yet, ship-go pending). Never run for Suriya.
- Competitor analysis: content/SERP benchmark done (30 pages); backlink competitor gap analysis not done (part of the workflow below).
- Citations: 31 live / 25 planned, unchanged.
- Content cluster: hub+spokes live; expansion not yet due. Full internal linking: scheduled week 7, not started.
- Martin: override the Hüwel-first rollout rule, start backlink-dach for Suriya now, budget €500/month. Routed to the Suriya client chat.

## Suriya backlink workflow, checkpoint 1 (14.10. ~07:45)
Partly done, blocked on DataForSEO IP whitelist (202.65.231.27 rejected) for steps 1.1-1.3. Nothing sent or bought.
Findings: reviews weak (12 @ 5.0, none since 28.08., Ternes 37, ZAM 20). 14 competitor candidates found. 26 real local sources found, Suriya on none of them. Citations handover: 25 not-live rows, 1 duplicate (theralupa), 1 wrong address, 3 wrong phone numbers, 2 live-but-marked-planned.
Top mention finds: Wild Spice (Heidesheim) names Coralie, no link. hnc therapist list (184 links) excludes her. Others: FDH, DGA, Cranio-Verband, Ingelheim aktiv, Mehrgenerationenhaus, SpVgg/Weihnachtsmarkt sponsors.
Flag from that chat: buying links (pillar C) is a trust risk after the 12.10. spam-link incident — recommends memberships/sponsoring first, partner outreach only with Coralie's OK.
Asking Martin its own cards directly in the Suriya chat.

## Suriya backlinks, step 1 complete (14.10. ~08:15)
DataForSEO IP whitelisted by Martin directly in that chat — unblocked. Decisions made there: reviews are not a backlink gate (separate review strategy, task_5b75d8ea); budget = memberships/sponsoring only, no bought links; Wild Spice counts as tried (Martin already mailed, no reply). Next: message to Coralie asking for her memberships (drafted, not sent), then Step 2 (the Sheet).
Gap result: mostly spam/directories; one real target found — Dozenten page, Heilpraktikerschule Wimmer (Mainz). Evidence found that competitors get the same automated spam links (m98ufa.com, *.pages.dev each link 10 of 14 competitors) — supports the 12.10. spam-link incident read.

## Marcel automation chat (14.10. ~08:30) — info only, no action here
Both pending cards answered directly in that chat: alert path = UptimeRobot iPhone app; Martin said "Mache ich gleich" for installing/logging in — not confirmed done yet (walk item for Martin).
Waiting on Marcel (not 741): does the "Gewinnspiel Skool Oktober 2026" tag send an instant mail, may it go late to 23 late sign-ups (7 need only KlickTipp steps, 16 have no Zapier run); also Marcel must delete test data.
Tally redirect to /fast-gewonnen/ is back on (flipped off once, cause unknown); UptimeRobot now watches it.
Details: 00_project/assets/marcel/automation/gewinnspiel/findings-2026-10-14.md

## Marcel UptimeRobot email alerts (14.10. ~08:45) — confirmed working
Email alerts active on both Gewinnspiel monitors (martin@741.studio), no app needed. Forced test raised an incident in ~2 min, mail confirmed received. Telegram not available on UptimeRobot free plan anyway.
Open (Marcel's own answer needed): "1 vs 2 Jahre Zugang" + Hot-Seat question before Mail-1 campaign (2075244, currently OFF) can switch on and add the 23 late sign-ups.

## Verification results (14.10. ~09:10+)
**Johni Jaya Motor** — 1 of 4 real: GBP categories/services done (confirmed). Hours/booking-URL/attributes done via 13.10. GBP pass, but FAQ was intentionally skipped by Martin in August — task stays open for that reason. Genuinely untouched: citations (Apple Maps/Bing/Facebook, Indonesian directories), review-engine briefing. Real backlog, not a stale checkbox — routed to team task list, no card needed.
**Bali Healing** — 6 done unticked, 3 partial, 2 void (no-doctor-names rule), 8 genuinely open (citations table literally empty, GBP hours/photos/review-briefing, hub+spokes). Martin: go, tick the 6+3.

**Maria Brasse** — 2 wrongly-marked-open items ticked (service pages, About page w/ Person schema). Real gaps: FAQ schema (waits on Maria), health directories not submitted, PR track untouched. Martin: go.
**Praxis Hüwel — INTEGRITY FLAG** — 7 tasks bulk-ticked 06.10. in a 25-second window; at least 2 provably false (30-day measurement 20 days overdue, no GBP post since before program start, no editorial backlink despite "Gastartikel 1 platziert" marked done). Martin: re-verify all 7 + run the overdue measurement now, routed.
**Rabenmütter** — 2 confirmed product pages ticked. DataForSEO blocked here too (3rd time today, different IP) — Martin: keep per-IP whitelisting rather than disable; IP requested from that session.
Rabenmütter ranking check (already-pulled data, 25.09. report): einfach nö #8, nö einfach nö #11, ich atme ein #27, fettnäpfchen #60 (still far back despite on-page work done — real gap). No fresh DataForSEO call needed.
**Daniela Dumann** — all 6 genuinely open, no stale flags. Conflict found: Hub+Spokes task vs. standing "no new pages" rule. Martin: keep the rule, drop/replace the task. Routed.

**Praxis Hüwel — full re-check** (corrected: 11 bulk-ticked, not 7). 4 hold (verified real), 5 reopened (no evidence), 2 client items untouched. 30-day measurement ready with GSC/reviews/citations data (8 outcomes); Local Falcon after-grid blocked — account has only 113 credits left (0 in paid package), not enough for the 6-keyword scan. Martin: skip the Maps/ranking part for now, deliver the measurement with Google data only.
