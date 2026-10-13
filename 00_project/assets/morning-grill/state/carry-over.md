# Carry-over for the next grill (written 2026-10-13)

Walk queue (start dates, D23, one item per client):
- [ ] Praxis Suriya: which start date counts, 14.08. (memory) or 03.09. (portal)? Program end 01.12. depends on it.
- [ ] Praxis Hüwel: paid 16.08., portal start 25.08. Which counts?
- [ ] STÜRZL: no start date. Start = rate-1 payment; has it been paid?

Cards from the dry run 2026-10-13 that were not answered (re-check facts before showing them):
- see 00_project/assets/morning-grill/2026-10-13-dryrun/brief.md (7 cards, 4 walk items, 11 below the line)

Added 2026-10-13 after the first real grill:
- [ ] Card for next grill: Suriya listing emails (00_project/assets/morning-grill/2026-10-13/suriya-listing-emails.md): 28 emails from 13 senders, most from 26.08.; 31 citations are already live. Check which senders are NOT live in client_citations, then mark the rest handled (needs a go: write to listing_emails).
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
