# Night Shift + Server — runbook DRAFT (nothing done yet)

Owner marks: **M** = Martin does it himself (accounts, payments, logins, keys, terms). **A** = agent does it after Martin's go, over Tailscale SSH, no secrets typed by the agent.
Order matters. Do not skip S0.

## Phase 0 — clean base

| # | Who | Step | Done when |
|---|---|---|---|
| 0.1 | M (+A check) | Laptop malware double-check (session card "Laptop malware double-check after infostealer") | findings file says "clean enough for new keys: yes" |
| 0.2 | M | Rotate the keys that were on the laptop on 13.10. (list comes from 0.1) | each key in `.secrets/` replaced; old keys revoked |
| 0.3 | A → M | Agent lists uncommitted files the night needs; Martin says which to commit | `git status` clean for those paths; pushed to GitHub |
| 0.4 | A | Fix the 6 night-shift bugs in a new server runner (branch `nightshift/setup`), sandbox tests T1–T8 | tests pass on the laptop in dry-run mode |

## Phase 1 — accounts (Martin only)

| # | Who | Step |
|---|---|---|
| 1.1 | M | Hetzner Cloud account; create project "741-nightshift"; add payment method |
| 1.2 | M | Create server: **CX43** (8 vCPU, 16 GB, 160 GB, EUR 16.49/mo excl. VAT), location Nuremberg (Helsinki if sold out), Ubuntu 24.04, add Martin's SSH public key, backups on (≈ 20 % extra). Data plan: `night-shift-server-data-transport.md` |
| 1.3 | M | Tailscale account; install Tailscale on laptop + phone; join the server (`tailscale up` with an auth key Martin creates) |
| 1.4 | M | GitHub: add a deploy key (write) for the repo; protect `main` (no direct pushes from that key) |
| 1.5 | M | Supabase: create user `nightshift-bot@741.studio` (password into the server env file by Martin) |
| 1.6 | M | Resend: create a send-only key restricted to `alerts@741.studio` |
| 1.7 | M | Run `claude setup-token` on the clean laptop; paste the token into `/etc/nightshift/claude.env` on the server (agent never sees it) |

## Phase 2 — server setup (agent, after Martin's go)

| # | Who | Step |
|---|---|---|
| 2.1 | A | Harden: close public SSH (Tailscale only), firewall default deny, unattended-upgrades, timezone `Asia/Makassar` |
| 2.2 | A | Create user `nightshift` (no sudo); install node LTS, python3, git, Claude Code, Playwright + Chromium (headless only, level B1; B2 agent login = phase 2) |
| 2.3 | A | Clone the repo; install the `night-shift` v2 skill, runner, guard hook, settings (dontAsk + allowlist + deny rules), sandbox network allowlist |
| 2.4 | A | Install read keys from Martin's env files (Martin places them; agent checks names only, never prints values) |
| 2.5 | A | Command Center: night card section + stop flag (portal change → staging first, then Martin's go for live) |
| 2.6 | A | Morning grill: night-queue card at 17:00 + read night report at 06:13 (morning-grill chat, Martin's go) |
| 2.7 | A | systemd timer 17:30 Mon–Fri — created **disabled** |

## Phase 3 — test and arm

| # | Who | Step |
|---|---|---|
| 3.1 | A | Test gate on the server: T1–T8 with TEST items; report + fresh verifier |
| 3.2 | A | One manual night run by hand (short window), open and read every output |
| 3.3 | M | Go for the first scheduled night → agent enables the timer |
| 3.4 | A | Read nights 1–3 fully; then weekly check against success criteria N15 |

## Rollback

- Stop: Command Center stop card, or `sudo systemctl disable --now nightshift.timer` (Martin) / STOP file.
- Remove: Martin deletes the Hetzner server and revokes the deploy key, the Supabase bot user, the Resend key and the setup-token (claude.ai settings).
- The laptop LaunchAgent (paused 13.10.) stays unloaded; its plist stays in `~/Library/LaunchAgents/` for reference.
