# Carry-over for the next grill (written 2026-10-13)

Walk queue (start dates, D23, one item per client):
- [x] Praxis Suriya: start = 03.09. (portal). DECIDED by Martin several times, last 13.10. 14:45. Goal sheet + memory fixed; never ask again.
- [x] Praxis Hüwel: start = 25.08. (portal). The '16.08.' was the Only Inside CMS invoice to Hüwel, not a 741 date: false conflict, fixed 13.10. 14:50.
- [ ] STÜRZL: no start date. Start = rate-1 payment; has it been paid?

Cards from the dry run 2026-10-13 that were not answered (re-check facts before showing them):
- see 00_project/assets/morning-grill/2026-10-13-dryrun/brief.md (7 cards, 4 walk items, 11 below the line)

Added 2026-10-13 after the first real grill:
- [x] (13.10. 14:45: Martin chose 'agent only lists them' — no portal write; per-sender decision later) Card for next grill: Suriya listing emails (00_project/assets/morning-grill/2026-10-13/suriya-listing-emails.md): 28 emails from 13 senders, most from 26.08.; 31 citations are already live. Check which senders are NOT live in client_citations, then mark the rest handled (needs a go: write to listing_emails).
- [ ] Check: portal reply drafts (session ✉️ Portal-Antworten 13.10.) sent by Martin?
- [ ] Check: Bali Ads verification result + status reply sent?
- [ ] Portal write order (Martin 13.10.): Freigabe-Dashboard → outreach numbers per client → Command Center on staging. One writer at a time. Before starting the Command Center build: check that both earlier chats say their portal work is done.
- [ ] Command Center → admin panel (D29, plan 00_project/morning-grill-portal-plan.md): start when Freigabe + outreach chats report their portal work done; then cards for GO-DB, GO-PORTAL staging.
- [x] Outreach-numbers chat: portal work DONE 13.10. (staging + live, backups in clients.741.studio/backup/*before-outreach-accounts*). Next in the portal order: Freigabe-Dashboard must pull fresh before any upload (warned 13.10.), then the Command Center build. Re-patch script if lost: 00_project/portal-outreach-accounts/patch_portal.py.
- [ ] Bali: audit Go-B done (45/100); client page waits for Go-C after the status reply. Pool + sitemap approved; Drive files staged, Martin drags them in. Next: pool items for the 2 doors, 'naturopathy removal' needs client OK.
- [x] Command Center on staging built + tested 13.10. (GO-DB + GO-PORTAL staging given). Open: live upload go; snapshot write + answer pull in the scheduled runs go. Two open cards (Johni restart, Kamil reports) can be answered in the page.
- [x] Command Center LIVE in the admin panel (13.10.); runs pull answers + publish a snapshot. Check at the first scheduled run (tomorrow 06:13): pulse.log shows snapshot=<id>, the tab shows the new date.
- [ ] Johni + Kamil: Martin answered in the portal (own answers, 13.10.). Start the agent work: Johni access list + re-plan; Kamil dashboard numbers + recommendations. See plan.md QUEUED.
- [x] D33 live 13.10.: walk items are cards now (type 'Your click'); the 13 click cards of 13.10. are open in the page.
- [ ] Tasks (D34): 23 tasks of 13.10. in 00_project/assets/morning-grill/2026-10-13/tasks.json. Tomorrow: carry the open ones over, update statuses, add new ones from today's answers. Team drafts: Dinakar (Suriya speed, waits for the WordPress role), Gayo (Bali CRM clean-up) in team-tasks-drafts.md; Martin forwards the WhatsApp lines.
- [ ] Waiting for the Freigabe chat's task-model schema (D35). Do not create task tables. When it arrives: map tasks.json fields to it, switch publish + Tasks tab, ask Martin for GO-DB at that time.
- [ ] Task writes in the scheduled runs are NOT approved (Martin dismissed the card 13.10.). Until he says go, run publish_tasks.py only inside the chat grill. Tasks tab reads work_items; check it shows the new date after a grill.
- [ ] Taxi Nürnberg (Daniel, 13.10.): Akeeba download key missing + 900 spam mails. Findings in 00_project/assets/morning-grill/2026-10-13/taxi-akeeba-findings.md. Needs Martin: Akeeba account check + key in Joomla (own login), sample spam mails from Daniel, go for captcha changes.
- [ ] Dumann: status page + 20 draft cards ready (00_project/assets/dumann/status-2026-10-13/). Check 5 mismatches the session found: Startseite title/description reset live; 3 Wix fixes not visible live (/ausbildung-vor-ort); design approval dated 11.10. and the email not in emails_log; Maps name; reviews 9 not 15 (goal sheet fixed). Release cards in waves; Daniela's approver_user_id is empty.
- [ ] Card 14.10. morning (priority 2, money): Bali Google Ads top-up — amount + payment way (GoPay / manual), account 239-394-2913, login 741studio18@gmail.com. Balance IDR 103,892 ≈ 5 days (13.10.). Skin tag campaign live since 13.10. (Learning); Ozone paused on purpose — never re-enable. Healthcare certification: not applicable.
- [ ] Night queue live from the 17:00 run (D37). First real card: tonight if Martin is at the grill; a hand-made queue for 13.10. exists (reporting/night-shift/queue/2026-10-13.json). Tomorrow 06:13: read reporting/night-shift/2026-10-13/REVIEW.md + state.json, show pass items as release cards.
- [ ] Night shift workflow: Martin asked the Night Shift chat (13.10.) to run the workflow-creation check (scorecard, registry row, research note). Waiting for its score. Goal sheet gaps for the night queue: no next_milestone for Dumann, Brasse, Bali, me&you; no next_workflow for Johni, Kamil, Taxi.
- [ ] Night 13.10. result (v2, verified from state.json: 4 items, 3 pass, 1 needs_martin, $4.23, no violations): all 4 already handled (state/night-routed.json). Tomorrow's 17:00 night card must offer the pending candidate brasse-faq-live-check (state/night-pending.json, Martin's pick at the 21:30 check-in); it still needs his tick on the card.
