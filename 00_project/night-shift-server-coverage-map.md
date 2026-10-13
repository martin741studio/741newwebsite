# Night Shift + Server — coverage map (what 741 already has)

Status: read-only inventory, 2026-10-13. Design chat "Night Shift + Server" (registry id `nightshift`, not added yet).
Rule: reuse before build. Each row says what exists, its real state, and what the night shift + server needs from it.

## 1. Correction to the brief

The brief says the old night shift is "built, not armed". This is not correct.

- `launchctl list` shows `studio.741.night-shift` and `studio.741.night-shift-sleep` as loaded.
- The night shift runs Mon–Fri at 20:00 WITA on the MacBook, window 20:00–22:59, auto-sleep at 23:02.
- Run folders exist for 20 nights, 2026-09-15 to 2026-10-12. The last run ended 20:43 on 2026-10-12.
- The OAuth problem from 2026-09-15 is gone. The `claude -p` calls run.
- The memory file `night-shift-agent.md` says "SCHARF seit 2026-09-15". The memory is correct; the brief is old.

## 2. Inventory

| # | Asset | Where | Real state (verified 13.10.) | Use for night shift + server |
|---|---|---|---|---|
| 1 | Night shift runner | `reporting/night-shift.sh`, skill `.claude/skills/night-shift/`, blueprint `00_project/night-shift-blueprint.md` | Armed on the laptop. Planner → Executor → Critic → Reviewer, fresh `claude -p` per page, Sonnet 5, 14 calls, 40 turns, `--permission-mode acceptEdits`, mkdir lock | Keep the pattern (fresh context per item, Critic, REVIEW.md). Port the runner to Linux. Fix the bugs in row 2 first |
| 2 | Night shift known bugs | `reporting/night-shift/LOG.md` | (a) `processed-feedback.json` never written: the same 5 feedback items re-run 8 nights in a row. (b) plan count bug `len(p)` vs `len(p["plan"])` (named 09-22, not fixed 10-01). (c) `invocations_used` undercounts; 10-12 shows "15/14", so the breaker let one call through. (d) Rabenmütter items blocked 10 nights: no DataForSEO tool + WebFetch 404. (e) Critic sometimes not called on attempt 2. (f) nobody reads REVIEW.md (grill O6) | Fix before any move. Moving a broken loop to a server makes it run broken 24/7 |
| 3 | Morning grill | skill `~/.claude/skills/morning-grill/`, source `00_project/morning-grill-skill/`, spec `00_project/morning-grill-workflow.md` | Installed. Desktop scheduled tasks `morning-grill-0600` (06:13) and `morning-grill-1700` on the laptop. Reads night shift REVIEW.md as source S6 (Q11: unread > 1 day or same blocker 3× → card) | Hand-over point. 17:00 log → night queue. Night results → 06:13 scan |
| 4 | Command Center | clients.741.studio admin, tabs Today / Decisions / Tasks / Clients; tables `grill_snapshots`, `grill_answers`, `work_items` | Live, admin only. Cards have own answer and change answer. `pull_answers.py` reads, `publish_snapshot.py` writes one row | Best phone surface: it already works on mobile, it is admin only, it already has cards. Night cards can use the same tables |
| 5 | Client approval cards | Freigabe tab in the portal (`client-approval-workflow`) | Live for client decisions | Pattern for card shape. Do not mix client cards with Martin's night cards |
| 6 | Automation build safety | `00_project/automation-workflow.md`, hooks in `00_project/automation-workflow/hooks/` | Designed, tested 95/95 in sandbox, NOT installed. Classes free / test_write / G / M. Layers L0–L6. PreToolUse guard + Stop done gate | Reuse the class model and `automation_guard.py` as the night-shift guard on the server |
| 7 | Workflow registry | `00_project/workflow-registry/`, Excel `~/Desktop/Workflow-Uebersicht.xlsx` | Stop hook in `.claude/settings.local.json` runs `sync` with a fixed macOS Python path | On a Linux server the path fails silently ("never fails a turn"). The Excel lives on the Mac Desktop. Server runs write `_run.json` only; the Mac sync picks them up after `git pull` |
| 8 | Daily standup | LaunchAgent `studio.741.standup` 08:05, `reporting/daily-standup.sh`, bot user `standup-bot@741.studio` | Runs on the laptop | Pattern for a machine user with its own login. Easy to move (curl + RPC) |
| 9 | Listings poller | LaunchAgent `studio.741.listings-poller` | Loaded on the laptop | Candidate for the server later. Not in the pilot |
| 10 | Dev VPS plan | memory `dev-vps-setup-plan` | Plan only (2026-07-23): Tailscale + tmux/mosh, Claude Max login, separate from the AltusHost cPanel VPS (client sites, CSF vs Docker). Then changed to "Docker on the desktop" | Decisions still valid: separate box, no open SSH port, never the cPanel VPS |
| 11 | Desktop PC | memory `desktop-ssh-access`, `madredao@192.168.0.3` | SSH works only on the same Wi-Fi. Tailscale not set up | Option "home box". Same-network limit and power/uptime risk |
| 12 | Existing bot VPS | memory `trading-collaboration` | A Telegram bot (Claudetotradingview, pm2) runs on a VPS. Host not recorded. No git there | Proves Martin can run a pm2 service. Do not share that box with client work |
| 13 | Telegram bot creds | `.secrets/telegram-741.env` | File exists (contents not read) | Possible push channel for "card ready" pings |
| 14 | Secrets | `.env`, `.secrets/` (apify, cpanel, dataforseo, ga-sc-reporting-bot.json, kraft-ftp, listings-imap, meta-741, standup, stuerzl-artfiles, telegram-741, youtube-api) | Mix of read keys and WRITE keys (FTP, cPanel, Meta) | Server gets a reduced copy: read keys only. FTP, cPanel, Meta write keys stay on the laptop |
| 15 | Repo | `martin741studio/741newwebsite` on GitHub | 1,173 uncommitted paths (296 modified, 875 untracked, mostly `dist/` and `04_site/review`). 67 local commits not pushed. `.git` = 378 MB | A server or cloud routine sees only what is pushed. Git hygiene is a migration step 0 |

## 3. Tool access: laptop vs server

| Tool / connector | Works on a Linux server? | Note |
|---|---|---|
| `claude -p` headless | Yes | Needs a non-interactive login (`claude setup-token` or an API key). Martin does this |
| DataForSEO, Apify, Google APIs (service account), Supabase REST | Yes | Plain HTTP with keys from `.secrets/` |
| claude.ai connectors (Drive, Calendar, Supabase MCP, Gmail etc.) | Only in cloud sessions / routines, not in a self-hosted `claude -p` | Self-hosted runs must use REST + keys instead |
| Local Falcon MCP | Yes (remote MCP at mcp.localfalcon.com) | Needs its key in the server config |
| Novamira WordPress MCPs | Technically yes | Exclude at night: they WRITE to live client sites |
| Claude in Chrome | No | Uses Martin's logged-in Chrome on the Mac. No headless mode |
| Control_Chrome, computer-use | No | macOS only |
| Playwright / headless Chromium | Yes | Only for public pages without login (QA, screenshots, crawl) |
| Desktop scheduled tasks, Remote Control push, Dispatch | No (Mac app) | Remote Control also runs from a Linux `claude remote-control` process |
| Registry Excel | No | macOS Desktop file. Mac rebuilds it after `git pull` |

## 4. Hard constraints of moving off the laptop

1. **Chrome-bound work stays on the Mac.** GBP edits, Local Falcon UI, LinkedIn CRM, logged-in portals, visual checks with Claude in Chrome. The night shift cannot do these. They go to the 06:13 grill as "Your click" cards.
2. **Connectors differ by host.** A self-hosted server has no claude.ai connectors. Anthropic cloud routines have connectors but no local repo, no local MCP and no `.secrets/`.
3. **Usage limits.** A weekly limit stopped a chat on 2026-10-11. Night runs on the same Max plan eat the day budget. A separate budget (API key with a hard spend cap, or a second seat) protects the day.
4. **Repo state.** 1,173 uncommitted paths and 67 unpushed commits. The server sees none of it until Martin commits and pushes. Concurrent writes from laptop and server need one rule: the server writes only into its own folders and its own branch.
5. **Registry hook and Excel.** The Stop hook path is macOS-only. On the server it does nothing. The Excel stays a Mac view.
6. **Time zone.** Martin is WITA (UTC+8). 17:00 WITA = 11:00 CEST (10:00 CET after 25 Oct). The Bali night (20:00–06:00) is the DACH afternoon and evening. Clients are awake and may write while the night shift runs. The server clock must be set to `Asia/Makassar` or every prompt must name the zone.
7. **Write keys.** Any key on the server is a key an injected prompt can reach. The server gets read keys plus write access only to its own output folder, its own branch and one admin-only card table.
8. **Laptop sleep.** Today's night shift needs the laptop awake 20:00–23:00. This is the main reason to move.

## 5. Gaps (nothing exists yet)

- No night queue file or table. The 17:00 log does not hand work to the night shift. The night planner reads only portal tasks and `report_feedback`.
- No phone check-in moment. Nothing pings Martin in the evening.
- No hard money cap. Only an invocation count.
- No kill switch other than `launchctl unload` on the laptop.
- No server, no Tailscale, no server login token.
- No registry entry for the night shift.
