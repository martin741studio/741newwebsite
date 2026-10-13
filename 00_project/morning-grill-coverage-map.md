# Morning Grill — Coverage Map (what 741 already has)

Version 1 · 2026-10-13 · Read-only research by the morning-grill design chat. Sources: memory files, repo files, LaunchAgents, registry. No system was changed.
Use: section per existing asset, then the client table, then the data sources for the morning scan.

# Coverage research: "Morning grill + daily client command" (raw, read-only)

Date of research: 2026-10-13, 07:40 WITA. Repo: `/Users/martindrendel/741website`.
Memory dir: `/Users/martindrendel/.claude/projects/-Users-martindrendel-741website/memory/` (= `$M` below).
Internal research notes for the parent agent. Not linted with deslop. No credentials copied.

---

## 1. Daily Client Standup

**Files**
- Memory: `$M/daily-client-standup.md` (built 2026-08-18).
- Job: `reporting/daily-standup.sh` (21 lines). Logs in as `standup-bot@741.studio` (creds `.secrets/standup.env`), calls RPC `daily_standup()` in Supabase `741-portal`, writes `reporting/standup/<date>.json` + `.txt` + `latest.txt`.
- Renderer: `reporting/render-standup.py` (90 lines). Blocks per client: blocker (missing access), help requests, unread messages, overdue tasks, onboarding bar, "WIR — delegierbar" (`heute_741`), "KUNDE — nachfassen" (`heute_kunde`), "Zu klären" (`pruefen[]`), last activity. Ends with "TAGESFOKUS" (1 access, 2 reply, 3 count of 741 tasks).
- Schedule: `~/Library/LaunchAgents/studio.741.standup.plist`, Mon–Fri 08:05, `RunAtLoad=false`, log `reporting/standup/cron.log`. Loaded (`launchctl list` shows `studio.741.standup`, exit 0).

**Output freshness**
- Latest: `reporting/standup/2026-10-12.txt` / `latest.txt` (Mon 12.10. 08:05). Today (13.10.) not yet run at 07:40.
- Gaps: no file for 07.10., 09.10. (`2026-10-09.json` is 0 bytes, renderer crashed with JSONDecodeError in `cron.log`), 13.–15.09., 24.09., 01.–04.09. partly. Laptop asleep / offline = no run, no catch-up.

**JSON fields per client** (`2026-10-12.json`): `name, mode, kunde_status, programm_status, start_date, woche, ob_fertig, ob_gesamt, ob_naechster, zugaenge_offen[], hilfe_angefragt, ungelesen, ueberfaellig, heute_741[], heute_kunde[], letzte_aktivitaet, pruefen[], sortkey`.

**Snapshot 12.10.** (9 clients): Johni Jaya Motor wk 9 (25 overdue, 3 access, last activity 17.08.), Praxis Suriya wk 6 (GTM missing, 1 help, 1 unread, 5 overdue, last 21.09.), Praxis Hüwel wk 7 (GTM, 1 help, 2 overdue), Bali Healing wk 5 (onboarding 1/6, 24 overdue, last 19.08.), Dumann wk 5 (3 access, 4× help, 4 overdue), Maria Brasse wk 5 (GTM, 15 overdue), Rabenmütter wk 5 (onboarding 2/6, 6 overdue, no activity ever), STÜRZL (program pending, no start date, onboarding 0/6), Kamil (reports mode).

**Missing for grill/plan/log**
- No "what happened yesterday": `letzte_aktivitaet` reads only portal `activity_log`. Claude work (WP edits, reports, CRO runs) never writes there. Suriya shows "last 21.09." despite daily work.
- Overdue counts are inflated: tasks are not ticked when work is done in chats (Rabenmütter memory notes a manual resync on 10.10.).
- No decisions/questions for Martin. No goal/KPI per client. No owner beyond `owner` 741/kunde (no person, no human vs agent).
- No evening log. No link to registry runs, night-shift REVIEW.md, or tracking alerts (tracking spec plans yellow alerts as new `pruefen[]` lines, not built).
- Clients missing from standup: Tacheles, Marcel Rosenbach, me&you/Pauspapier, Adel, Meerblick, Eri Trostl (not in portal as program clients).
- Output is plain text in repo; nobody is pushed (no mail/Telegram).

## 2. Night-shift agent

- Memory: `$M/night-shift-agent.md`. Skill: `.claude/skills/night-shift/SKILL.md` (repo, not `~/.claude/skills`). Blueprint: `00_project/night-shift-blueprint.md` (15.09.).
- Runner: `reporting/night-shift.sh` (135 lines). Mon–Fri 20:00 via `~/Library/LaunchAgents/studio.741.night-shift.plist`; window 20:00–22:59, hard stop 23:00; lock dir; model `claude-sonnet-5`, max 14 invocations; node@22 path. Sleep agent `studio.741.night-shift-sleep.plist` 23:02 (`pmset sleepnow`). Both loaded.
- Data fetch (REST, standup-bot): `programs?status=eq.running`, `tasks?status=neq.done&track=eq.B`, `report_feedback?verdict=eq.aenderung`, `client_locations?nap_status=eq.locked`.
- Output: `reporting/night-shift/<DATE>/` with `REVIEW.md`, `plan.json`, `state.json`, `context.json`, `specs/`, `audits/`, `critic/`, `feedback/<client>/`. Run log `reporting/night-shift/LOG.md`; raw `night-shift.log`, `launchd.out.log`.
- Runs: daily dirs 16.09.–12.10. Latest `2026-10-12/REVIEW.md`: 6 planned / 5 pass / 1 needs_martin (3 Suriya feedback items, 2 Rabenmütter feedback, 1 Rabenmütter audit blocked).
- Known defects (LOG.md, repeated): `processed-feedback.json` still `[]` (8 runs in a row) so the same Suriya/Rabenmütter feedback is redone nightly; plan-length bug (`len(p)` vs `len(p["plan"])`) flagged 22.09. and 01.10.; invocation counter undercounts; Rabenmütter site WebFetch-404 + no DataForSEO tool, 10× needs_martin.
- **Missing for grill**: nobody consumes REVIEW.md in the morning. The checkboxes ("[ ] freigeben") are never ticked and never written back to the ledger. This is a ready-made grill input: "approve these 5 drafts y/n" and "fix ledger".

## 3. Workflow registry + overview Excel

- `00_project/workflow-registry/README.md`, `workflow_registry.py` (25 KB), `registry.json` (38 KB, updated 13.10. 07:36), `approval_hook.py`, `.registry.lock`. Second source: `00_project/cro-registry/registry.json`.
- Hooks in `.claude/settings.local.json`: Stop hook runs `workflow_registry.py sync --quiet` after every turn; UserPromptSubmit hook reminds to run `approve` when Martin says "freigegeben".
- Commands: `build`, `list`, `add-client`, `upsert`, `approve` (= upsert with approve flag, under file lock), `sync` (scans `00_project/assets/` + `00_project/prospects/`, only raises status, never lowers, never touches approved/archived, auto-creates missing client as type Lead "bitte prüfen"), `add-workflow`.
- `_run.json` schema: `client, workflow, status (in Arbeit | Trockenlauf | fertig, Freigabe offen), mode (Echt | Trockenlauf), last_run (YYYY-MM-DD), result, drive, note`.
- 13 workflow ids: `cro`, `unburning`, `phone`, `audit`, `pool`, `citations`, `backlink`, `cro_b`, `copy`, `automation`, `tracking`, `prospect`, `lockout`.
- 16 clients in registry: Kunde = Dumann, Suriya, Hüwel, Maria Brasse, STÜRZL. Lead = Adel, Bali Healing, 741 Studio (Eigen-Audit), Marcel Rosenbach, Meandyou, + 6 prospects (Claudia Tiemann, Catja Grieshaber, Ana Violeta Fredel, Christian Ruether, Sabine Schwarz, Stephan Meyer). 43 runs.
- Not in registry: Kamil, Rabenmütter, Johni Jaya Motor, Tacheles, Pauspapier (as such), Meerblick, Eri Trostl. Bali Healing and Marcel are typed "Lead" although they are running clients.
- Excel `~/Desktop/Workflow-Uebersicht.xlsx` (22 KB, 13.10. 07:36), sheets: `Übersicht` (21 rows; cols Kunde, Typ, then one col per workflow, cell = "status · date"), `Links` (81 rows; Kunde, Workflow, Seite oder Lauf, Status, Freigabe von Martin, Letzter Lauf, Ordner Drive, Ordner lokal, Ergebnis, Notiz), `Workflows` (14 rows; Workflow, Auch genannt, Reife, Freigabe, Slash-Befehl, Stand, Satz im Chat, Weiterarbeiten, Ergebnis ansehen, Installieren, Dokument, Skill, Läufe, davon freigegeben), `Befehle` (14 rows).
- **Missing**: no "next action" or "waiting for" per run; ~25 runs in "fertig, Freigabe offen" = an approval queue nobody is asked about; no daily view; no goal/KPI; no owner field.

## 4. Portal (clients.741.studio, Supabase `741-portal`, `galjmtozcgxcwtzkzbpi`)

Memories: `$M/client-portal-infra.md`, `$M/portal-single-file-workflow.md`, `$M/team-outreach-area.md`, `$M/portal-leads-crm.md`.
- One hand-written `index.html` (live = source), staging `clients.741.studio/staging/index.html`, go needed for live.
- **Area A (client care) tables**: `profiles` (role admin/client/delivery), `clients` (mode program|reports, lang, status, billing, stammdaten_sheet_url, contract_path), `locations` / `client_locations` (street, postal_code, city, country, phone, primary_category, nap_status), `client_master_data` (NAP, services[], focus, boundaries, open_points[]), `programs` (client_id, start_date, end_date, status pending|running), `tasks` (client_id, week, track A–D, title, status, owner 741|kunde, sort), `onboarding_steps` (kind), `access_grants` (ausstehend→angefragt→erteilt→geprueft, hilfe_angefragt), `activity_log`, `messages` (support chat), `materials` + bucket, `emails_log`, `scans`, `subscriptions`, `client_reports`, `report_feedback` (verdict, comment), `admin_notifications` (digest queue), `client_credentials` (admin only), `client_citations`, `directories`, `avv_signatures`, `week_videos`, `portal_settings`, `visibility_prompts/results`, `leads` (0 rows, staging only), `contacts`, `client_stack`, `assistant_messages`, `page_change_requests`, `site_form_submissions`. Templates: `template_onboarding_steps`, `template_access_grants`, `template_tasks` (13 weeks, tracks A–D, 43–44 tasks, de/en).
- RPCs/crons: `daily_standup()`, `provision_client()`, `send_weekly_mails('monday')` (pg_cron Mon 05:00 UTC, weekly task mail to clients), `send_admin_digest()` (pg_cron).
- **Area B (outreach & sales, live since 24.08.)**: `team_members` (seats, lang), `daily_plans` (intent checklist + targets jsonb), `daily_reports` (messages_sent, new_replies, interested, follow_ups, connection_requests per seat, progress, blockers, next_plan, hours_worked), `team_notes`, `team_settings`; RPC `team_standup(day)` with `plan_missing` flag, `team_period(from,to)`. Strategy tables `campaigns`, `offers`, `sales_plays`, `pitch_targets`. Gayo = manager; Rias = outreach member (since 02.09.); Farzana deactivated. Gayo's own login was still open in the memory.
- **This is the closest existing "plan in the morning / report in the evening" pattern** (Gayo format), but only for outreach staff, not per client, not for Martin.
- **Missing**: no per-client goal/KPI table (tracking spec proposes `tracking_config`, `tracking_decisions`, etc., not created, needs GO-DB); no daily client log table; tasks lack person owner and agent/human flag.

## 5. Tracking workflow (`00_project/tracking-workflow.md`, v0.1, 12.10., 329 lines)

- Status: design approved 12.10. ("proof tracking confirmed"), dry run only (`00_project/assets/tracking/praxis-suriya/2026-10-12-design-dryrun/_run.json`). Pilot Suriya. Nothing built; tables need GO-DB.
- Daily (planned, pg_cron Berlin): 06:07 GBP/reviews/profile, 06:17 GA4+GSC, 06:27 site + form check, 06:37 rules → alerts, **08:05 standup shows yellow alerts**.
- Red rules R1–R6 (site down, form marker gone, profile field differs from master, profile unverified, tracking broken, 1–2 star review): email at once, same working day.
- Yellow rules Y1–Y9 (views < 70 % baseline, actions < 70 %, grid drop, review drought, no leads 14 d, GSC −20 %, pending Google suggestion, weekly card not released by Wed 12:00, cost cap 80 %): in 08:05 standup, react within 1 week.
- Weekly: Mon 07:30 agent drafts "Wochen-Update" card per client, Martin releases (GO-W) by Wed 12:00 + raw Loom. Monthly (1st Mon): grid scan, competitors, reconciliation (GO-M). Quarterly: war-room pack 5 working days before meeting (Suriya: draft 24.11., meeting ~01.12.), 9 sections, ends in "3–5 decision questions" + decision log (date, decision, owner, due, metric, review date).
- Success D20: Martin ≤ 30 min per client per week.
- **Connection points for the morning grill**: (a) yellow alerts as grill questions; (b) Monday = "release weekly cards" question; (c) decision log format is reusable for grill answers; (d) open questions O2 (Suriya start 14.08. vs 03.09.), O5, O7, O8, O9 are grill material now.
- Live pilot facts (12.10.): Suriya profile views down (53 vs Ø 120), GSC access gone, no Maps scan since 16.08., `leads` 0 rows, `clients.billing` empty.

## 6. 90-day program

- `~/Downloads/741-studio-portal-90-tage-programm.md` **does not exist on disk** (checked; no copy found under `~` depth 4). Program structure is only known from memory + portal templates: 13 weeks, tracks A–D front-loaded, 43 (de) / 44 (en) tasks, onboarding 6–7 steps (Vertrag+AVV, Zugänge, Stammdaten, Material, Fragebogen, Kickoff, Start), 7–9 access grants.
- Modules named in memory: Modul 5 (scaled content / Einzugsgebiet), Modul 6 (Behandlerseite).
- Week 1: `$M/week1-playbook.md` → `00_project/local-seo-program-week1-playbook.md` (31.08.): 10 steps (live check → competitor factors → volumes/topic tree → baseline scans → report page with approval JS → GBP texts → partner list 25+ → named method → deploy → handover message + Loom), acceptance checklist.
- Structure page: `$M/client-structure-page-playbook.md` → `00_project/client-structure-page-playbook.md`, master prompt `00_project/website-struktur-master-prompt.md`.
- Rules: `$M/program-deliverable-rules.md`: review target = 2× market leader with interim "overtake"; HWG; methodology on page; no team names; never build without explicit "build/implement" in that moment; outreach is always 741's job; no automatic data into the dashboard; flag topics not from the client; "Ausgangslage" report in dashboard.
- Customer journey boards: `00_project/client-journey-boards.md` (7 boards, v1 22.09.).
- **Missing**: the canonical 90-day doc is gone; no per-week "definition of done" per client; no week-by-week target numbers; week 13 / renewal step not visible.

## 7. Team

- `$M/team-roster.md` (02.09.): Dinakar (dev/implementation, also Tacheles white-label, Suriya Elementor, Dumann pages), Tantri (website, Drendel site), Gayo (PT Amana employee, outreach + talent sourcing), 2 new hires from 07.09. (1 SEO → Hüwel, 1 content → Johni Jaya Motor; names not in memory), Defina (image retouch), open role funnel/automation builder (blocks Marcel + Pauspapier). No "Anicka".
- Other names in memory: Rias (outreach, afternoons–evenings), Maya (marketing streams S1/S3), Izzy (Bali Healing analysis), Bondan (media buyer; Martin never messages him), Aulia (failed implementation attempt).
- Gayo: `$M/gayo-employment-contract.md` (employment start 01.10.2026, trial to 31.12., 40 h/week Mon–Fri, KPI "ramp toward 2–4 booked qualified calls per week", 5 % commission). `$M/gayo-unit-economics.md` (month 1: 2 clients, 7.000 €).
- Channels: portal area B (daily plans/reports), WhatsApp (Gayo's original format), Loom for Dinakar briefings (Dumann 09.10.).
- **Missing**: no hours/capacity per person in one place; no names for the 2 Sept hires; no per-client assignment table; roster last updated 02.09.

## 8. Business

- `00_project/revenue-model-100k.md` (11.10.): goal 100.000 €/month. Baseline (last verified month): 7.400 € revenue, 2 deals, Ø 3.700 €, 1 LinkedIn seat, acquisition cost 1.200 €. 27 deals/month needed at 3.699 €. Main path 10–12 LinkedIn seats + higher deal value. Bottlenecks: Martin is the only closer, delivery capacity (plan 10–15 active clients per delivery person), one-off revenue (track MRR separately). Section 8 "Track these numbers every week" (sent, replies, calls booked/held, deals, CAC, total delivery cost, active clients, clients per delivery person, margin) → "feed into weekly check-in". Options C (retainer) and D (website care) added 10./11.10.; Meta ads model 11.10. (benchmarks only).
- `$M/revenue-model-100k.md` (17.08.), `$M/741studio-pricing.md` (1.999 / 3.699 with result guarantee / 7.999 + ads fee; no prices in mails), `$M/marketing-quarter-campaign.md` (12-week plan from 17.08., streams S1 affiliate Gayo+Maya, S2 Meta Martin, S3 reactivation, S4 giveaway; Sheet `1plGDwUBN9DmXnvBx45wwzKVoErszjxUOYpH8RO5U7TA`, week numbers Fridays), `$M/hubspot-leads-segmentation.md` (portal 19710059, ~65k cold contacts, segment by `hs_object_source_detail_1`).
- **Missing**: section 1 of the model not updated since August numbers; no current month revenue, MRR, active-client count, or pipeline value anywhere machine-readable; weekly-checkin does not read this file.

## 9. Data Brain

- `$M/data-brain-project.md` → `00_project/data-brain-plan.md` (13.08.). Plan: separate Supabase warehouse, Client Registry (`canonical_client_id`) seeded from Drive invoicing ledger, read-only v1. **Status: spec only, not built.**
- Relevance: the morning scan needs exactly the client registry that does not exist (names differ: "Praxis Suriya" / "suriya" / "praxis-suriya"; "Meandyou" / "meandyou" / "me&you").

## 10. Skills and commands

- Repo `.claude/skills/`: archify, claudex-loop, claudex-route, codex-build, codex-review, imagery-audit, local-seo-review-page, night-shift, seo-page-optimizer, slopmonster.
- `~/.claude/skills/`: backlink-dach, behandler-seite, client-access-lockout, content-writing, cro-homepage, `synced/<id>/` (anthropic-skills: built-in-browser, chrome-browser, computer-use, deep-research, docs, docx, google-workspace, import-memory, **morning**, pdf, pptx, skill-creator, xlsx).
- `~/.claude/commands/`: `daily-brief.md` (news briefing from `martin_info.md`, saves to Notion), `daily-checkin.md` (7 personal questions → `/journal/daily/YYYY-MM-DD.md` + reflection), `weekly-checkin.md` (asks metrics → `/metrics/metrics-history.md`, Notion). No repo `.claude/commands/`.
- Usage evidence: `~/journal/daily/` has only 2025-09-16 files; `~/metrics/metrics-history.md` exists; `~/martin_info.md` dated 16.09.2025 (stale: "741 Digital Solutions LLC", trading). These commands are effectively unused and know nothing about clients.
- `morning` skill (`~/.claude/skills/synced/8f740622-…/morning/SKILL.md`, 152 lines): renders a calendar/email/chat morning brief as HTML artifact; can be set up as recurring weekday task; sorts "Needs attention" vs "Resolved". Generic, no client/program logic.
- `schedule` (anthropic-skills:schedule) is listed as available but no SKILL.md on disk under synced (only `morning`). Non-741 morning skills exist outside: `~/clawd/skills/morning-rollup`, `~/.clawdbot/sandboxes/.../morning-email-rollup` (Telegram email rollup, other setup).
- Plugin skills available in session: `sales:daily-briefing`, `sales:end-of-day`, `sales:weekly-wrap` (CRM-oriented, not wired to 741 data).

## 11. Clients (memory + portal + assets)

Asset folders: `00_project/assets/{suriya,huewel,dumann,maria,balihealing,stuerzl,adel,marcel,meandyou,meerblick,audit,un-burning,tracking}`. Several paths named in memory (e.g. `assets/suriya/baseline/`, `assets/suriya/incidents/`, Stürzl baseline) are in worktrees (`.claude/worktrees/*`, 10 worktrees), not in the main checkout.

**Praxis Suriya (Coralie)** — `$M/praxis-suriya-client.md` (81 KB, upd. 13.10.), `suriya-baseline-tracking.md`, `suriya-elementor-dinakar-set.md`, `suriya-ayurveda-massage-page-untouchable.md`, `suriya-conversion-paths-must-stay.md`. Active program; start 14.08. (memory) vs portal 03.09.–01.12. (conflict O2). Positioning 3 pillars; baseline frozen (GSC 28.06.–23.09., GBP 122 views/week, ~2 requests/week). No explicit review target or KPI targets; tracking catalogue M01–M34 designed. Blockers: GSC access removed 12.10. (trust incident, closed 13.10. with PDF; hard client rules: no backlink/disavow, no big changes without backup, no URL changes); GTM access open in portal; 1 help request + 1 unread message; Google Ads campaign paused. People: Martin, Dinakar (Elementor set, parallel), Defina (images). Workflows: citations, unburning (dry run), phone (dry run), pool, tracking (dry run), lockout (approved 13.10.), night-shift feedback nightly.

**Praxis Hüwel (Martin Hüwel)** — `$M/huewel-client.md` (19 KB, upd. 03.09.) + `huewel-nap`, `-website-live-state`, `-site-workflow`, `-repo-ai-rules`, `-newsletter-build`, `-onlyinside-ersatz`, `-banerji-subtitles`. Active program; payment 16.08., portal start 25.08. (week 7). Goal implied: grow radius (reviews, full GBP, 40 directories), bioresonanz 0/49. Client pivot to B2B. Revenue 0 since June (sensitive). New site live on GitHub Pages since 06.10. Open: GBP round 2 (FAQ, review replies, ~19 services), root domain 404, AVV for forms, GTM access, 1 help request. People: Martin; planned SEO hire. Workflows: citations, backlink pilot (23 rows), pool.

**STÜRZL Steuerstrafrecht (Dr. Anja Stürzl)** — `$M/anja-stuerzl-client.md` (upd. 13.10.) + `stuerzl-source-of-truth-sheet`, `-backlog-no-implement`, `-cro-run`, `-kosten-fakten`, `-local-falcon-keywords`. Client since 26.09.; 7.999 € in 2 rates; project start = payment of rate 1 (not tracked in memory); Ads launch ≤ 2 weeks after start. Portal: program pending, no start date. Baseline 01.10. (8 scans). No numeric goals. Blockers: start date, GSC (to verify), GBP München owner unknown, Google Ads access, client login + welcome mail (needs go), backlog "no implement" (09.10.), copy approval queue. People: Martin; contacts Linkemann, Jilg, Glogger. Workflows: audit (32/100), cro (37/44), cro_b, pool (54 items), copy (≈30 page `_run.json`, all "Freigabe offen", one approved), unburning folder, backlinks folder.

**Naturheilpraxis Daniela Dumann** — `$M/dumann-client.md` (51 KB, upd. 09.10.), `dumann-ueber-mich-page.md`. Active program; portal start 14.09. (week 5); account from 28.08. Goal: review target 104 (2× Lemke), milestones 15 → 53. GA4/GSC baseline 30.09. Blockers: 3 access (GA4, GSC, GTM per portal, although memory says GA4/GSC set up 30.09. = stale portal data), 4 help requests, open question on /vortraege. People: Martin, Dinakar (page work, Loom 09.10.). Workflows: citations, pool (dry run), cro (2 pages), cro_b (approved), SEO work plan `00_project/dumann-seo-arbeitsplan-2026-10.md`.

**Maria Brasse (shuiguru.de)** — `$M/maria-brasse-client.md` (56 KB, upd. 09.10.), `maria-brasse-nap.md`. Active program; portal start 14.09. (week 5). 11 pages live 25.09.; tracking live 30.09.; BrightLocal 25 listings bought 08.10. No goal/KPI targets. Open: `[Maria: ergänzen]` placeholders, 15 overdue tasks, GTM access, 1 help request. People: Martin. Workflows: citations; `assets/maria/falcon`.

**Bali Healing (Peggy/Pasha, Izzy)** — `$M/balihealing-local-seo.md`, `balihealing-google-ads-setup.md`, `bali-market-and-references.md`. Portal: EN program running, start 14.09.; onboarding 1/6; 24 overdue; last activity 19.08. Registry types it "Lead". Ads blocked (billing/tracking incomplete, publish suppressed). Gap: acupuncture 4 % SoLV. No goals/KPIs. Workflows: audit (46/100), pool (in Arbeit).

**Rabenmütter (Franziska Poerschmann)** — `$M/franziska-rabenmuetter-client.md` (upd. 10.10.), `shopify-admin-api-rabenmuetter.md`. 3-month package from 500 €/month, start on first payment; portal program start 14.09.; onboarding 2/6; no activity_log entries. KPIs "Baseline→Ziel" exist inside a report page. Open: Merchant Center, DACH directories, Trauerkarten hub, Pensaki outreach (waits for go), night-shift item blocked 10×. Not in registry. No asset folder.

**Johni Jaya Motor** — `$M/johnijayamotor-client.md` (upd. 27.08.). Portal: program running since 17.08. (week 9), 25 overdue, 3 access missing, last activity 17.08. Planned owner: content hire. Open: FAQ section, certificate logos, password rotation/2FA. Not in registry. Looks stalled.

**Kamil Böyük (Physio Anatomie + Physiotherapie Kraft)** — `$M/kamil-physio-client.md` (upd. 16.08.). Reports-mode client; Google Ads 741-managed; monthly GA4 report pipeline (`reporting/monthly-client-report.mjs`, outputs `reporting/out/physio*-2026-07.html` = last July). No KPI target. Memory 2 months old. Not in registry.

**Marcel Rosenbach (NLP, Skool funnel)** — `$M/marcel-rosenbach-client.md` (upd. 06.10.), `marcel-message-in-martin-voice.md`. Automation project; Zap + KlickTipp campaign active since 03.09. Registry: automation dry run 11.10. (`00_project/assets/marcel/automation/skool-funnel/_run.json`). Blocked by missing funnel/automation builder role. No KPI.

**Tacheles (Denise / Miriam)** — `$M/tacheles-client.md` (upd. 01.09.). White-label rebuild, cap 33 h / 2.145 €, Dinakar 35 h budget. Open since 01.09.: product-page button question, Zoom with Denise. Status unknown since September. Not in registry.

**Pauspapier / Michael Ehlers (me&you)** — `$M/pauspapier-michael-ehlers.md` (35 KB, upd. 13.10.). Partner Tajan; end client Ehlers. Only explicit goal: reduce no-show rate; "KPIs must be set in the kickoff" (still not set). Very active: copy (9 runs, 8 approved), pool approved, ~10 CRO runs (LP Overlooked/Undersold to Checkpoint 2 on 12.10.). Open: Framer access, photos (Phil), setter person unknown.

**Aydan Adel** — `$M/adel-client-cro.md` (upd. 11.10.). Lead; CRO prototype 37/44 as sales artifact; open points in `00_project/assets/adel/cro/08-handoff/handoff.md`.

**Meerblick (Klaus-Dieter Sachs)** — `$M/meerblick-klaus-dieter-sachs.md` (upd. 07.10.). Potential partner; 2 homepage artifacts; source `00_project/assets/meerblick/build.mjs`. No next step recorded.

**Eri Trostl** — `$M/eri-trostl-prospect.md` (upd. 29.09.). Prospect; paid strategy proposed; PDF 29.09. No follow-up recorded.

## 12. Activity signals for "what did we do yesterday"

- Git (`git log --since="2 days ago"`): 9 commits (11.10. 18:22 → 13.10. 06:55). By area: `00_project/assets/meandyou` 301 file touches, `00_project/automation-workflow` 23, `.claude/hooks` 7, `00_project/assets/marcel` 6. Commit 3f06c2f adds proposed hooks (go-gate, config protection, slop gate), not active.
- Uncommitted: 1.131 dirty paths (`dist/review` 206, `04_site/review` 206, `04_site/public` 114, `dist/review-assets` 111, `04_site/pages`/`dist/pages` 56 each, meandyou 52, `.claude/skills` 10). Git alone misses most work; Suriya/Hüwel/Brasse WP and GitHub-Pages work is outside this repo.
- Worktrees: 10 (`git worktree list`); branches touched recently: `main` 13.10., `claude/friendly-franklin-dc8c6b` 11.10.
- `_run.json`: 50 files (prospects 6, Stürzl copy ~30, meandyou copy 9, Marcel 1, tracking 1). `last_run` all 2026-10-11 or 2026-10-12. Registry `runs[].last_run` also covers `_status.md`-based runs; latest entry Suriya lockout 2026-10-13.
- Chat transcripts: `~/.claude/projects/-Users-martindrendel-741website/*.jsonl` = 230 files; 48 modified in last 2 days, 46 in last 24 h (largest 170 MB). Plus 9 worktree project dirs under `~/.claude/projects/-Users-martindrendel-741website--claude-worktrees-*`. Side-session notes: `~/Library/Application Support/Claude/side-session-notes/` (6 dirs, latest 13.10. 06:51).
- Memory: 43 memory files changed in last 2 days (incl. praxis-suriya-client, anja-stuerzl-client, pauspapier-michael-ehlers, tracking-workflow, client-approval-workflow, new `feedback-no-named-task-owners.md`).
- `reporting/`: standup (12.10.), night-shift (12.10. 20:43), listings poller log (`reporting/standup/listings-poll.log`, every 10 min, last 07:40 today, "Geprüft: 0").
- Portal: `activity_log`, `messages`, `report_feedback`, `admin_notifications`, `access_grants.hilfe_angefragt` (via `daily_standup()` or REST with standup-bot).
- Excel/registry: `00_project/workflow-registry/registry.json` mtime 13.10. 07:36.

## 13. Scheduled jobs

- `~/Library/LaunchAgents/`: `studio.741.standup.plist` (Mon–Fri 08:05), `studio.741.night-shift.plist` (Mon–Fri 20:00), `studio.741.night-shift-sleep.plist` (Mon–Fri 23:02), `studio.741.listings-poller.plist` (every 600 s, RunAtLoad). Non-741: elgato, google updater/keystone, steam, mariadb. All four 741 agents loaded, last exit 0.
- `crontab -l`: Sun 23:00 `/Users/martindrendel/run-forex-events.sh`; daily 21:30 `741-watchface/health export_health.py`.
- Supabase pg_cron (from memory): `portal-weekly-monday` (Mon 05:00 UTC weekly client mails), `portal-admin-digest`.
- Claude scheduled tasks (`mcp__scheduled-tasks`): 1 task `launch-physio-campaign`, one-time 01.09.2026, disabled. No morning/evening task exists.
- Draft hooks not active: commit 3f06c2f (`.claude/hooks`).

---

## Client table

| Client | status | goal defined? | KPIs defined? | phase | blockers | owner | workflows run | missing |
|---|---|---|---|---|---|---|---|---|
| Praxis Suriya | active program (portal 03.09.–01.12.; memory start 14.08.) | partly (3 pillars, baseline frozen) | designed (tracking M01–M34), not live | wk 6, relaunch done, trust repair | GSC access gone; GTM; client hard rules; Ads paused | Martin, Dinakar, Defina | citations, unburning*, phone*, pool, tracking*, lockout ✓ | start-date conflict, numeric targets, review target, renewal plan |
| Praxis Hüwel | active program (paid 16.08., portal 25.08.) | implied (radius, bioresonanz) | no | wk 7, new site live | GTM; GBP round 2; root 404; AVV | Martin (+ SEO hire planned) | citations, backlink, pool | targets, KPIs, end date, B2B pivot decision |
| STÜRZL | client since 26.09., program pending | no numeric goal | no | onboarding / content | no start date (rate 1 payment), GSC check, GBP München owner, Ads access, approvals | Martin | audit, cro, cro_b, pool, copy (~30), unburning, backlinks | start date, Ads launch date, KPIs, approval of ~30 copy runs |
| Dumann | active program (portal 14.09.) | review target 104 | partly (milestones 15→53) | wk 5, pages + citations | portal shows 3 access (stale?), 4 help requests | Martin, Dinakar | citations, pool*, cro, cro_b ✓ | other KPIs, task sync |
| Maria Brasse | active program (portal 14.09.) | no | no | wk 5, site live, citations | 15 overdue, GTM, Maria placeholders | Martin | citations | goal, KPIs, task sync |
| Bali Healing | program running (EN, 14.09.), registry says Lead | no | no | onboarding 1/6, stalled | access/onboarding, Ads publish blocked | Martin, Izzy (client side) | audit, pool | goal, KPIs, activity, registry type |
| Rabenmütter | active (3-month, from 500 €/mo; portal 14.09.) | in report ("Baseline→Ziel") | in report only | wk 5 | site fetch 404 for night shift, Merchant Center, outreach go | Martin, night shift | night-shift feedback only; not in registry | registry entry, KPIs in data, end date |
| Johni Jaya Motor | program running since 17.08. (wk 9) | no | no | stalled since 17.08. | 3 access, 25 overdue | content hire (planned) | none recorded | owner, status decision (active/paused?) |
| Kamil | reports client (Ads) | no | no | ongoing Ads + monthly report | report pipeline last July | Martin (+ Bondan?) | none in registry | KPIs, recent memory, report cadence |
| Marcel Rosenbach | automation project | flow defined | no | funnel live 03.09., automation dry run | missing automation builder | Martin | automation* | KPI, next step, registry type |
| Tacheles | white-label rebuild (cap 2.145 €) | scope defined | hours cap 33 h | unknown since 01.09. | button question, Zoom | Dinakar (hidden), Martin | none | current status, hours used |
| Pauspapier / me&you | partner + end client | no-show reduction only | not set | CRO LPs at Checkpoint 2 | Framer access, photos, setter unknown | Martin, Pauspapier (Tajan, Phil) | copy ✓, pool ✓, cro (≈10) | KPIs, contract/role split |
| Aydan Adel | lead | n/a | n/a | prototype done | open handoff points | Martin | cro | next sales step |
| Meerblick (KDS) | potential partner | n/a | n/a | 2 drafts 07.10. | none recorded | Martin | none (artifacts) | next step |
| Eri Trostl | prospect | n/a | n/a | PDF sent 29.09. | none recorded | Martin | none | follow-up date |

(* = Trockenlauf/dry run, ✓ = approved)

## Activity data sources for the morning scan

| Source | Path / access | Freshness (13.10. 07:40) |
|---|---|---|
| Standup JSON/TXT | `reporting/standup/<date>.json`, `latest.txt` | 12.10. 08:05; today pending 08:05; gaps when laptop off |
| Live standup RPC | Supabase `741-portal` `select daily_standup();` (MCP or `reporting/daily-standup.sh`) | live |
| Night-shift review | `reporting/night-shift/<date>/REVIEW.md`, `LOG.md` | 12.10. 20:43 |
| Workflow registry | `00_project/workflow-registry/registry.json`, `~/Desktop/Workflow-Uebersicht.xlsx` | 13.10. 07:36 (Stop hook) |
| Run files | `find 00_project/assets 00_project/prospects -name _run.json` | last_run 11.–12.10. |
| Git | `git log --since=yesterday --stat`, `git status --porcelain` | 13.10. 06:55; 1.131 uncommitted paths |
| Chat transcripts | `~/.claude/projects/-Users-martindrendel-741website/*.jsonl` (+ worktree dirs) | 46 files touched in 24 h |
| Memory changes | `find $M -name '*.md' -mtime -1` | 43 files in 2 days |
| Portal tables | `activity_log`, `messages`, `report_feedback`, `admin_notifications`, `access_grants`, `tasks` | live; activity_log misses Claude work |
| Team board | `team_standup(day)`, `daily_plans`, `daily_reports` | live (outreach only) |
| Listings poller | `reporting/standup/listings-poll.log` | 07:40 today, every 10 min |
| Tracking (planned) | `tracking_alerts`, `tracking_cards` | not built |
| Side-session notes | `~/Library/Application Support/Claude/side-session-notes/` | 13.10. 06:51 |
