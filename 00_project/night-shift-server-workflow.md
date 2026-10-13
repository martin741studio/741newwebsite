# Night Shift + Server — workflow spec v0.1 (design, checkpoint 1)

Registry id: `nightshift` (not added yet). Build folder: `00_project/workflow-builds/nightshift/`. Decisions N1–N16: `decisions.md` there. Pipeline + freedom: `pipeline.md`. Use cases: `use-cases.md`. Tests: `test-scenarios.md`. Hosting: `00_project/night-shift-server-hosting-options.md`. Runbook: `00_project/night-shift-server-runbook-draft.md`. Coverage: `00_project/night-shift-server-coverage-map.md`.

## 0. Job and done

After the 17:00 evening log, agents work through the evening and night on a server. Martin checks his phone at 19:30 and 21:30 and answers prepared cards. Results feed the 06:13 morning grill.
Done per night = REVIEW + night report exist, every item has a verdict (pass / needs_martin / skipped with reason), pulse line written, nothing sent or changed outside the server branch.

## 1. Preconditions (nothing runs before all are true)

- S0 Laptop malware check passed (N13). Keys and the setup-token are created only after it. Old keys that were on the laptop on 13.10. are rotated first.
- S1 The 6 known night-shift bugs are fixed in the server version (coverage map row 2).
- S2 Git: the files the night needs are committed and pushed (Martin decides what; agent prepares the list).
- S3 Test gate (automation-build L5 pattern) passed on the server with T1–T8 (`test-scenarios.md`).
- S4 Martin's go for the first scheduled night.

## 2. Task classes and gates

| Class | Night? | Examples | Gate |
|---|---|---|---|
| research / data pull | yes | DataForSEO, GSC/GA4 reads, Local Falcon **read** tools, public crawl | read keys only |
| draft | yes | page specs, FAQ, copy blocks, report drafts, feedback answers | files on the server branch; release by day |
| server build + QA | yes | prototypes on server localhost, headless screenshots | no upload, no deploy |
| public audit | yes | SEO/CRO audit of pages without login | read only |
| Chrome / login work | no → "Your click" card at 06:13 | GBP, Falcon UI, LinkedIn, portals with login | laptop by day |
| never | no → day card | send, message, publish, deploy, FTP, live site or portal write, ads, money, credit-spending scans, delete | Martin's per-change go by day |

Unconfirmed queue at 17:30 → only research and public audit items run (N10).

## 3. Night queue (hand-over from the 17:00 log)

- The 17:00 run adds a "Night queue" card: ≤ 8 items, each with client, class, inputs, done-definition, due date. Rank: due date, then the client's roadmap step.
- Item source: open tasks with owner "agent" in `tasks.json` plus Martin's ad-hoc items (UC3).
- Martin ticks or removes items (phone or chat). Answer stored in `grill_answers` (existing).
- Morning-grill side: adds the card and a `night_class` field per agent task. That change belongs to the morning-grill chat and needs Martin's go there.

## 4. Phone check-ins (N4, N5, N16)

- 19:15 and 21:15: the runner sends one mail to martin@741.studio: "Night shift: n cards ready" + Command Center link. No client data. Sent by a fixed script, never by Claude.
- Cards live in the Command Center (admin only), section "Night". Max 5 per check-in. Overflow waits for the next check-in or 06:13.
- Card shape (one tap must be enough): headline in plain words (client · what was made · why now) · evidence link (file on the server branch, screenshot) · Critic verdict in one line · options A approve draft / B redo with note / C park with reason / own answer · 741 recommendation · deadline "answer by 21:30 or it waits for 06:13".
- "Approve" means "draft accepted". Nothing goes live from a night card.

## 5. Caps and limits (N2, N7)

- Auth: Max plan login via `claude setup-token` → `CLAUDE_CODE_OAUTH_TOKEN` (env file on the server, mode 600, created by Martin). Note: the docs name setup-token for CI and scripts; the terms speak of "ordinary use" and say logins must not be shared. One login, one owner, low volume keeps us in that frame.
- Per night: 14 `claude -p` runs · `--max-turns 40` · est. USD 10 (runner sums `total_cost_usd` from `--output-format json`; `--max-budget-usd` per run as a second wall).
- Plan-limit error → stop at once, `resume.json`, no retry. The day keeps its own budget.
- Model: Sonnet 5 for Executor and Critic (as today). Switch only with Martin's go.

## 6. Safety layers on the server

1. Box: Hetzner VPS Nuremberg, Ubuntu LTS, Tailscale only (no public SSH), unattended security updates, firewall default deny inbound.
2. User: `nightshift`, non-root, no sudo. Claude Code never runs in bypass mode.
3. Permissions: `--permission-mode dontAsk` + exact allowlist; deny rules for `ftp`, `lftp`, `scp`, `rsync`, `ssh` (outbound), `git push` to `main`, `curl -X POST|PUT|PATCH|DELETE` to anything but the runner's own endpoints, WordPress MCPs, Local Falcon scan tools. Deny rules hold in every mode.
4. Hooks: `automation_guard.py` (from the automation-build workflow) as PreToolUse guard with the class table above; Stop hook writes the pulse line.
5. Bash sandbox (bubblewrap) with a network allowlist: anthropic, dataforseo, googleapis, supabase (741-portal), localfalcon, apify, github.
6. Keys: read keys only (DataForSEO, Google service account read scopes, Apify, Local Falcon). No FTP, cPanel, Meta, Resend-full, Novamira keys. The mail ping uses a send-only key readable only by the notifier script's user.
7. Supabase: machine user `nightshift-bot@741.studio` (Martin creates it) with RLS: read queue answers + kill flag, insert night cards. No other table.
8. GitHub: deploy key; the server pushes only `nightshift/*` branches; branch protection blocks pushes to `main`.

## 7. Kill switch (N9)

- "Stop night shift" card/button in the Command Center sets a flag row. The runner reads it before every run. Backup: file `/srv/nightshift/STOP`. Martin can also say "stop the night shift" in any chat (agent sets the flag).
- Effect: the current run ends, no new run starts, pulse line "stopped by Martin <time>".

## 8. Logs Martin reads in the morning

- `reporting/night-shift/<date>/REVIEW.md` (on branch `nightshift/<date>`): per client, per item verdict + link.
- `night-report.json`: machine version for the 06:13 grill (source S6).
- `night-shift.log`: one line per run with role, item, cost, exit.
- `pulse.log`: one line per night. Missing line at 06:13 = "night did not report" card.
- `_run.json` in the night folder → registry sync on the laptop after `git fetch`.

## 9. Hand-over to the 06:13 grill

- The laptop grill fetches `nightshift/<date>`, reads `night-report.json`, and shows: what passed (release cards), what is `needs_martin`, what waited for 06:13, cost and runs used, stop reason.
- Q11 rule stays: unread REVIEW item > 1 day or same blocker 3× → card.
- Night results never count as done. Done = Martin's click + evidence (ops rule 26).

## 10. Failure handling

| Failure | Action |
|---|---|
| Source unreadable | write "unreadable", never "nothing new"; item continues if possible |
| Item fails Critic twice | `needs_martin` card with the fail list; no third try |
| Same blocker 3 nights | morning card "needs data from Martin", item leaves the queue |
| Plan-limit hit | stop, `resume.json`; stop mail if before 22:00 |
| Crash / server down | systemd restarts once; else stop mail (before 22:00); 06:13 shows missing pulse |
| Kill switch | stop within one run |
| Injection text found | Critic flags it; item `needs_martin`; deny rules block the action |

## 11. Bugs to fix in the server version (S1)

1. `processed-feedback.json` never written → write it from Martin's card answers (day side), and plan only unprocessed items.
2. Plan count bug (`len(p)` vs `len(p["plan"])`) → planner becomes a script that reads the queue.
3. `invocations_used` undercount and "15/14" → one counter in the runner, checked before every run.
4. Rabenmütter blocker 10× → DataForSEO via script (no tool needed), site fetch via Playwright; 3× rule moves it out.
5. Critic not called on attempt 2 → runner always pairs Executor + Critic.
6. Nobody reads REVIEW.md → cards in the Command Center + 06:13 grill.
7. v1 skill has no "Do NOT use" line and no verification step → v2 SKILL.md gets a negative trigger and an end check (`validate_night.py`: every item has a verdict, counters match the log, no guard violations).

## 12. Success after one week (N15)

5/5 nights without crash · ≥ 5 items pass per night · fewer open morning cards than the week of 13.10. · zero sends, deploys or live writes (checked in `night-shift.log` and guard log).

## 13. Hard limits

Never: send, message, publish, deploy, live site or portal writes (except the night card rows), ads, money, credit-spending scans, deletes outside the server's own run folder, push to `main`, bypass mode, root. Martin does all accounts, payments, logins and key entry.

## 14. Phase 1 = laptop (decision N27–N31, 13.10. evening)

Martin: prove the night shift on the laptop first, server after 5 clean nights. Runner v2 `reporting/night-shift-v2/run.py` (queue mode, script planner + reviewer, exact run counter, cost from `total_cost_usd`, deadline kill at 22:45 WITA, STOP file `reporting/night-shift/STOP`, write check via `git status`). Claude flags: `--permission-mode dontAsk --setting-sources user --strict-mcp-config`, Write/Edit only under `reporting/night-shift/**`, deny list for curl/ftp/scp/rsync/ssh/git push/rm. LaunchAgent `studio.741.night-shift-v2` Mon–Fri 17:30 + 20:30 (20:30 = resume slot); no queue file → no run. Old v1 agent stays unloaded. Open: 17:00 night-queue card (morning-grill chat), Command Center night section for the 21:30 check-in, mail ping. Known gap: `python3` is allowed for the agents and could write outside the folder; the git check logs it as a violation.
