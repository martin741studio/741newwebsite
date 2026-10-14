# Decisions — Night Shift + Server (Martin's answers, AskUserQuestion cards)

## Round 1 (2026-10-13)
- N1 Hosting: "Hybrid: VPS Germany (Recommended)" — Hetzner VPS Nuremberg for headless night work; Chrome tasks stay on the laptop as morning click cards.
- N2 Budget: "Plan login (setup-token)" — night runs use the Max plan limits (not the API credit). Consequence: night caps must protect the day budget (invocation + turn + estimated-USD cap, stop on limit, resume file).
- N3 Night task classes: all four — research + data pulls · drafts · builds on the server (localhost) + QA · audits of public pages. Never: sends, deploys, live site/portal changes, ads, money, client messages.
- N4 Phone: "Command Center + one ping (Recommended)" — cards in the existing admin Command Center; one short ping "cards ready", no client data in the ping.

## Round 2 (2026-10-13)
- N5 Check-ins: "2×: 19:30 and 21:30 (Recommended)" — max 5 cards each, about 5 min.
- N6 Window: "17:30 to 05:00 WITA (Recommended)" — stops at 05:00 before the 06:13 grill.
- N7 Night cap: "Low: 14 runs, est. USD 10" — max 14 fresh agent runs per night, 40 turns each, est. USD 10 (client-side estimate), stop at once on a plan-limit hit + resume file.
- N8 Alerts: "Only a crash or stop alarm (Recommended)" — never after 22:00; after 22:00 it waits for 06:13.

## Round 3 (2026-10-13)
- N9 Kill switch: "Stop card in Command Center (Recommended)" — server checks before every run; backup flag file on the server.
- N10 Hand-over: "Log proposes a queue, you confirm (Recommended)" — 17:00 log adds a 'Night queue' card (≤ 8 items, class + client); no answer by 17:30 → only read-only items run.
- N11 Pilot: Martin's own answer: "I would wish to run a night shift, but we don't have it set up on the server yet." → read: the pilot is the night shift itself; it cannot run on the server before the server exists. Clarify in round 4.
- N12 Bugs: "Fix first, 3 clean nights, then move (Recommended)" — fix the 6 bugs on the laptop runner, 3 clean nights, then the same runner moves; laptop job stops when the server job starts.

## Round 4 (2026-10-13, 18:10 WITA)
- N13 Hand-run night queue (design test, nothing ran): Martin ticked all 4 — Kamil Oberhausen audit · Brasse FAQ drafts 4 pages · Bali copy 10 Beauty pages · Stürzl 35 GSC opportunities. Plus own text: "Also, my laptop needs to be double-checked now. If there was any malware activity happening, that would be deleted before."
  → New precondition S0: laptop malware check + cleanup BEFORE any server setup, before any key or token moves to the server. Only keys rotated after the clean check go to the server.
- N14 Pilot: "No night runs until server" — REVISES N12. The laptop night shift is paused now (launchctl unload studio.741.night-shift, 18:10 WITA, plist kept at ~/Library/LaunchAgents/). Bugs get fixed in the server version; first night run = server night 1.
- N15 Success after one week (all 4): 5/5 nights without crash · ≥ 5 items pass per night · fewer morning cards · nothing sent or changed without go.
- N16 Ping channel: "Email to martin@741.studio" (via the Resend alert address alerts@741.studio, automation-build pattern). No client data in the mail; link to the Command Center.

## Checkpoint 1 (2026-10-13, ~18:40 WITA)
- CP1 Design go: "Go, as designed (Recommended)" — build the server runner with the 6 bug fixes, guard and tests on a branch. Nothing armed or bought. Next go = checkpoint 2 (tests + scorecard).
- N17 Cap week 1: "Keep 14 for week 1 (Recommended)" — after week 1 show runs used, passes, weekly-limit impact; then Martin decides.

## Round 5 — server purchase prep (2026-10-13, ~19:20 WITA)
- N18 Size: "CX43, EUR 16.49/mo (Recommended)" — 8 shared vCPU, 16 GB, 160 GB, Nuremberg (fallback Helsinki if sold out).
- N19 Server: Martin's own answer: "There is no connection to a server. ... No, there's no other connection to a server." → new, separate Hetzner box. Note: the laptop's known_hosts lists a Hostinger VPS (srv1782758.hstgr.cloud) and two Google Cloud VMs (hub.741-studio.com, project studio-apis-503306) that Martin does not know about → check if they still bill (walk item, not part of this build).
- N20 Browser: "Headless now, agent login later (Recommended)" — B1 headless Playwright now; B2 separate 741 agent account with read roles in phase 2; never Martin's main logins on the server.
- N21 Untracked files: "Commit what the night needs (Recommended)" — agent lists untracked folders, Martin ticks what goes to GitHub.
- N22 Commit groups: G1 only (workflow + knowledge text, ~60 MB). G2 client text, G3 media, G4 build output stay on the laptop for now. Commit + push = runbook step 0.3, after the laptop check (S0) and a secret scan.

## Round 6 — setup clicks (2026-10-13 evening)
- N23 SSH key: "Agent makes it now" → `~/.ssh/id_ed25519_nightshift` (ED25519, SHA256:dtSuknhHK79tTNVE9eMJorCA2FX2XS0suK8oOnTkHVA), random passphrase stored only in the macOS keychain; `~/.ssh/config` host `nightshift-01` (HostName added when the IP is known). Public key copied to the clipboard.
- N24 Server: "I buy it now" — Martin buys CX43 Nuremberg himself.
- N25 Tailscale: "With the server setup".
- N26 Hostinger VPS 187.127.103.222: Martin: "i dont use hostinger" → not his; left as is. Laptop history shows root SSH logins there with a now-stolen key → owner unknown; not part of this build.

## Round 7 — laptop first (2026-10-13 evening)
- N27 Martin's own answer (instead of buying Hetzner): "We do make runs only till 11 pm now, my time, on my laptop, so that can run. At 11 pm, the internet will shut off anyway, so we do it here. I don't want to do it on a server yet until we haven't figured out the night shift properly and whether it's even working properly."
  → REVISES N1 (server now) and N14 (no runs until server): phase 1 = night shift v2 on the LAPTOP, window ends before 23:00 WITA (internet off at 23:00). Server (Hetzner CX43, plan unchanged) only after the night shift is proven. No Hetzner account created; tab closed.
- N28 Tonight: "Quick-fixed run 20:30–22:45 (Recommended)" — v2 runner built (reporting/night-shift-v2/run.py, review.py, prompts/), queue reporting/night-shift/queue/2026-10-13.json (4 hand-test items), LaunchAgent studio.741.night-shift-v2 (Mon–Fri 17:30 + 20:30, caffeinate, runs only when a queue file exists, hard stop 22:45). Dry run OK (8 runs, exact counter). Permission test OK: curl denied, write outside reporting/night-shift/** denied, inside allowed (--setting-sources user, dontAsk, scoped Write/Edit, --strict-mcp-config).
- N29 Window from tomorrow: "17:30–22:45 WITA (Recommended)".
- N30 Server move: "After 5 clean laptop nights (Recommended)".
- N31 Check-ins in the laptop phase: "Only 21:30" (one check-in; needs the Command Center night section + 17:00 queue card).
- N32 Queue card: "Morning-grill chat (Recommended)" — spec sent to the morning-grill chat 13.10. (needs Martin's go there).
- N33 21:30 check-in: Martin's own answer: "Nah need on a chat here somewhere so i can access on my phone" → check-in happens in THIS chat (Night Shift chat) with Remote Control ON (set 13.10. ~19:40) so Martin opens it in the Claude app. Cards via AskUserQuestion here. No portal change.
- N34 (via morning-grill chat, Martin's card there): no answer to the 17:00 queue card = no queue file = no night run. Replaces the N10 fallback. Queue writer: 00_project/morning-grill-skill/scripts/build_night_queue.py (first gate: classes, ids, inputs, forbidden actions, confirmed_by).

## Checkpoint 2 (2026-10-13 ~21:40 WITA)
- CP2: "Go, keep it running (Recommended)" — v2 stays armed Mon–Fri (17:30 + 20:30 resume, stop 22:45), runs only with a ticked 17:00 queue card; install the skill; count 5 clean nights toward the server (N30).

## Server bought (2026-10-14)
- N35 Martin: "Alone [also] for canaries, I think we need one" → server now (revises N30 "after 5 clean nights"); one box for night shift + canary checks.
- N36 Bought by Martin: 741-agents-01 · CAX31 (8 Arm vCPU, 16 GB, 160 GB) · Falkenstein · 162.55.46.13 · SSH key 741-nightshift · about EUR 25.57/mo incl. VAT (+ backups 20 % if ticked). CX43 was sold out in NBG/FSN/HEL; CAX31 not in NBG. Image came up as Ubuntu 26.04.1 LTS (aarch64), not 24.04. Login test OK (root, key auth, 15 GiB RAM, 143 GB free, TZ UTC). Agent did not add the key (auto-mode classifier blocked it); Martin clicked.

## Scope change (2026-10-14)
- N37 Martin: "we're not only doing it for the nightshift... we're doing it so that this whole setup that we have in here can run on the server (the whole Claude setup), because I don't want to always use my laptop and use a lot of the CPU power for it, so the task can run easily and steadily."
  → 741-agents-01 is NOT a night-shift-only box. It is the general-purpose server for Claude Code work (headless agent runs, canary checks, and over time other chats' heavy/steady tasks), freeing the laptop from CPU load. Night shift v2 is the FIRST tenant, not the only one. Implication: server setup (phase 2) should stay general (users, repo layout, resource limits per tenant) rather than night-shift-specific; naming already reflects this (741-agents-01, not nightshift-01).
- N38 Rebuild: skipped. "Skip the rebuild, use 26.04 (Recommended)" — server stays on Ubuntu 26.04.1 LTS as delivered. Setup proceeds on 26.04; fix issues if tools (Playwright/Chromium) need workarounds there.
- N39 Base setup DONE (14.10., 07:10 WITA, script `reporting/night-shift-v2/server/setup-phase2.sh`, fixed for Ubuntu 26.04's socket-activated ssh.service): firewall (22/tcp only), unattended-upgrades active, fail2ban active, SSH password auth off, swap 4G, user `nightshift` (no sudo), TZ Asia/Makassar, Node v22.23.3, Python 3.14.4, Claude Code 2.1.296, Chromium+ffmpeg for Playwright — all for user `nightshift`. Server is general-purpose per N37, not night-shift-specific.
- N40 Tailscale: "Yes, set it up now (Recommended)" — close public SSH once joined.
- N41 Claude auth: "I'll run setup-token myself (Recommended)" — Martin runs `claude setup-token` as the nightshift user via SSH.
- N42 Tailscale DONE (14.10.): Mac already joined (martins-macbook-pro, 100.88.46.7). Server joined as 741-agents-01, 100.124.61.26, Tailscale SSH enabled. Public SSH (162.55.46.13:22) closed via ufw (now allow-in only on tailscale0); verified public IP times out, Tailscale IP still connects. ~/.ssh/config on the laptop repointed to 100.124.61.26. Auth key used once, not stored in any repo file or log.
- N43 Claude auth DONE (14.10.): `claude setup-token` completed via SSH + Chrome OAuth flow (Martin approved in browser). Token stored at /home/nightshift/.claude-oauth-token.env on 741-agents-01 (chmod 600, owned by nightshift, sourced from .bashrc). Verified with a live `claude -p` call (result "OK", $0.042). Token never written to any repo file, never shown to Martin twice, all local plaintext logs and remote bash history scrubbed after use.

## Scope expansion: persistent server session (14.10. afternoon)
- N44 Martin: "ideally we have the core claude running over there and we just connected to it from laptop and phone" → second layer added, parallel to the batch runner: a persistent interactive Claude Code session on 741-agents-01, reachable via Claude app Remote Control AND raw SSH+tmux from phone.
- N45 Repo scope: "Full repo clone (Recommended)" — git clone (not scratch-only).
- N46 User: "Same 'nightshift' user (Recommended)" — shares tools/config with the batch runner.
- N47 Timing: "Set it up now (Recommended)".
- Found: origin/main was 94 commits / ~2 months stale (last push 9 Aug). Martin: "Push everything now (Recommended)" — pushed 6e4ee2d..88ad0b6, verified secret-free first. 1,223 uncommitted/untracked files (mostly dist/, generated output) intentionally left out, laptop-only for now.
- Server side done: tmux installed, repo cloned clean (896 MB, commit 88ad0b69). Raw SSH+tmux interactive `claude` session confirmed working (auto-authenticates via the setup-token env var already installed — token covers interactive chat too, not just `-p` batch calls).
- **Found: weekly plan usage already at 80%, resets 19 Oct 7am WITA** — shared pool across Desktop app, all laptop client chats, Night Shift, and now this server. Flagged to Martin; not yet a hard blocker but worth watching given more server usage is being added on top.
- Remote Control needs a SEPARATE full login (`claude auth login`, broader OAuth scope incl. sessions/MCP/plugins) — the setup-token does NOT cover it (confirmed via `claude remote-control --help` error). Login flow started, URL opened in Chrome, waiting on Martin's approval code.
- N48 Martin asked about the SEPARATE problem of client-site logins (GBP, LinkedIn, WordPress) for chats that would run on the server — these need an ongoing logged-in browser, not a one-time account login. Proposed: persistent Chrome + virtual display + noVNC on the server, reachable from any device over Tailscale, as the generic "clear the blocker" mechanism. Scoped as separate next build, not started. Martin: "Finish Remote Control first (Recommended)".

## Remote Control: live (14.10. afternoon)
- Fixed a real bug along the way: the CLAUDE_CODE_OAUTH_TOKEN env var (set globally in nightshift's .bashrc for the batch runner) silently overrides/blocks full-scope login for `claude remote-control` ("Long-lived tokens are limited to inference-only"). Fix applied for this session: `unset CLAUDE_CODE_OAUTH_TOKEN` before launching remote-control. Needs a permanent fix (see below) so this isn't a manual step every restart.
- Full account login done via `claude auth login` (separate from setup-token), approved by Martin in Chrome after a Tailscale hiccup (his Mac's Tailscale had logged itself out mid-task; relogin fixed via tailscale.com browser approval).
- Remote Control running in tmux window `main:remote` on 741-agents-01, spawn mode same-dir, repo 741website on main, capacity 1/32. Connected and confirmed via `claude remote-control --help` + live tmux capture showing "Connected · 741newwebsite · main". Martin asked to verify from phone app / claude.ai/code.
- OPEN: make this survive a server reboot (systemd service or tmux auto-start), and make the OAUTH_TOKEN-unset permanent/scoped so it doesn't block future remote-control (re)starts — not done yet, next step.

## Browser-blocker build started (14.10.)
- N49 Martin pushed back on "finish on laptop" framing: "that's what we literally try to avoid" → building the real fix now, not a laptop-fallback workaround. Mechanism: Playwright (not Claude-in-Chrome, which is Desktop-app-paired and can't run against a remote server) driving a real Chrome in a virtual display (Xvfb) on 741-agents-01, visible to Martin over noVNC (web link, Tailscale-only). One-time logins per service (Google, ChatGPT, LinkedIn), then agents automate without him present; he reconnects via noVNC only for logins/2FA/CAPTCHA.
- N50 Drive fix: "Yes, set it up (Recommended)" — Drive service account instead of the risky browser-click upload method. Removes Drive from the "needs Chrome" list permanently.
- Wrote 00_project/workflow-builds/nightshift/server-access-inventory.md (sections A done / B easy-API / C hard-browser) per Martin's ask to front-load the whole access list in one sitting.

## Browser layer live (14.10.)
- Xvfb (1440x900, :1) + fluxbox + x11vnc (localhost-only, port 5901) + websockify/noVNC (port 6080) installed and running on 741-agents-01, script `reporting/night-shift-v2/server/start-browser-display.sh` (idempotent, re-run safe).
- Real Chrome (not headless) launched with persistent profile `/home/nightshift/browser-profile`, CDP debug port 9222 (localhost-only) for Playwright MCP to drive later, window 1400x870.
- Verified end-to-end from the Mac: http://100.124.61.26:6080/vnc.html reachable directly over Tailscale, confirmed visually — live Chrome window on the server, "Connected (unencrypted) to 741-agents-01:1".
- Security: noVNC/x11vnc reachable only via tailscale0 (ufw default-deny covers the public interface already); no VNC password set (-nopw), matches the existing Tailscale-is-the-perimeter trust model. noVNC connection itself is unencrypted (plain websocket) — acceptable since it never leaves the Tailscale tunnel, but flagged as a minor hardening item (could add TLS or a VNC password later).
- NOT yet done: systemd/reboot-survival for this stack (currently plain background processes, lost on reboot); Playwright MCP wired to CDP port 9222 so agents can actually drive it; first login (Google/ChatGPT/LinkedIn) into the persistent profile.

## Reboot-survival proven (14.10.)
- 6 systemd --user units (browser-xvfb, browser-fluxbox, browser-x11vnc, browser-novnc, browser-chrome, claude-remote-control) at reporting/night-shift-v2/server/systemd/. Fixed claude binary path bug before deploy (/opt/homebrew is Mac-only; server uses /home/nightshift/.local/bin/claude). `loginctl enable-linger nightshift` so the user bus starts at boot without a login session.
- claude-remote-control.service deliberately does NOT set CLAUDE_CODE_OAUTH_TOKEN (would block Remote Control, same bug as before); `--spawn=same-dir` flag passed explicitly so no interactive prompt on restart; confirmed the "Enable Remote Control?" consent is remembered, no re-prompt.
- Actually rebooted the server (not just trusted the config) — all 6 services, CDP port 9222, and noVNC port 6080 confirmed back up automatically, unprompted, within ~25s of the server returning.
- Full stack now reboot-proof: display + Chrome + Remote Control all self-start.
