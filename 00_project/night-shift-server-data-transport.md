# Night Shift + Server — data transport and server size (2026-10-13)

Draft for Martin's decision. Nothing bought, nothing copied.

## 1. Hetzner Cloud offer (live page, fetched 2026-10-13 ~19:10 WITA)

Prices excl. VAT, incl. IPv4, EU locations (Nuremberg NBG1 / Helsinki HEL1; some also Falkenstein FSN1). 20 TB traffic included. Hourly billing with a monthly cap.

| Plan | Family | vCPU | RAM | Disk | EUR / month | Fit for 741 night + browser work |
|---|---|---|---|---|---|---|
| CX33 | Cost-Optimized (shared, Intel/AMD) | 4 | 8 GB | 80 GB | 8.99 | minimum; 1–2 browsers at a time |
| **CX43** | Cost-Optimized (shared) | 8 | 16 GB | 160 GB | **16.49** | **recommended start**: agents + 3–4 headless browsers in parallel |
| CX53 | Cost-Optimized (shared) | 16 | 32 GB | 320 GB | 29.99 | if browser work grows (many parallel crawls/screens) |
| CAX31 | Cost-Optimized (Arm Ampere) | 8 | 16 GB | 160 GB | 21.49 | Arm: Chrome/Playwright work, but some tools lack Arm builds → avoid |
| CPX32 | Regular Performance (shared, newer AMD) | 4 | 8 GB | 160 GB | 35.99 | faster CPU per core, higher price |
| CPX42 | Regular Performance | 8 | 16 GB | 320 GB | 69.99 | same size as CX43, about 4× price |
| CCX13 | General Purpose (dedicated AMD) | 2 | 8 GB | 80 GB | 43.49 | dedicated cores; not needed for night batches |

Add-ons: daily backups from about EUR 1.20 / month (20 % of the server price class), snapshots EUR 0.0143 per GB / month.

**Warning:** on 13.10. every plan on the public page showed "currently unavailable / not available". This can be a real capacity shortage or a page default. The Hetzner Console shows the real stock per location when Martin creates the server. If NBG1 is sold out: try HEL1 (Finland, still EU/DSGVO) or FSN1. If all are sold out: wait a few days, or pick another EU provider (decision card).

Why CX43: Chromium uses about 0.3–0.5 GB RAM and one core per busy tab. Two agent runs plus 3–4 browsers fit in 16 GB with headroom. Shared vCPUs are fine for night batches (no live users). Upgrade later in the console in minutes (CX43 → CX53, disk can stay).

## 2. What must move (measured on the laptop, 13.10.)

| Data | Size | Already in the cloud? | How it moves |
|---|---|---|---|
| Supabase (portal, tasks, cards, clients) | — | yes (Frankfurt) | nothing to move; the server reads it with the bot user |
| Google Drive, GA4, GSC, Ads data | — | yes | nothing to move; read by API with read scopes |
| Repo `741website`, tracked files | ~1.0 GB + `.git` 378 MB | GitHub has it up to the last push | `git clone` on the server |
| 67 local commits not pushed | in `.git` | no | `git push` (Martin's go) |
| Untracked files (9,615 files, ~1.44 GB: client media in `00_project/assets` 1.06 GB, text in `00_project/assets` 0.12 GB, knowledge 34 MB, prospects 27 MB, site output `dist/` + `04_site` + `07_social/output` ~160 MB) | ~1.44 GB | no | Martin decides: commit what the night needs; the rest by `rsync` over Tailscale (one time), or not at all |
| `.claude/worktrees/` (copies of the repo for chat branches) | 5.9 GB | branches partly pushed | do NOT copy; the server works on its own clone |
| `node_modules` | 277 MB | — | do NOT copy; `npm ci` on the server |
| Personal skills `~/.claude/skills/` | 5 MB | no | `rsync` copy of the skills the night needs (night-shift, seo-page-optimizer, slopmonster, content-writing rules) |
| Claude memory `~/.claude/projects/.../memory/` | 1.4 MB | no | read-only mirror on the server, refreshed by the 17:00 run (`rsync` push from the laptop) |
| Secrets `.secrets/`, `.env` | 44 KB | no | **Martin only**: new (rotated) read keys, copied by Martin with `scp` over Tailscale. Write keys never move |

Total first transfer: about 1.5 GB by git (tracked + committed text) plus up to 1.1 GB media by rsync if Martin wants the media on the server. Over a home line in Bali this takes about 15–45 minutes. Commit proposal: `workflow-builds/nightshift/commit-proposal.md`.

## 3. Ongoing sync (after the first copy)

```
LAPTOP  ── git push main ──────────────►  GitHub  ──── git pull (17:30) ────►  SERVER
LAPTOP  ◄── git fetch nightshift/<date> ──  GitHub  ◄── git push nightshift/<date> (05:00) ── SERVER
LAPTOP  ── rsync memory + skills (17:00 run, read-only mirror) ──────────────► SERVER (Tailscale)
SUPABASE ◄──── both read; server writes only night cards + pulse ────►
```

Rule: one writer per place. The laptop owns `main`. The server owns `nightshift/*` branches and its run folders. No two machines edit the same file.

## 4. Browser work on the server

| Level | What | Works on the server? | CPU / RAM | Risk |
|---|---|---|---|---|
| B1 Headless public | Playwright + Chromium headless: crawl, screenshots, visual QA, Lighthouse | yes | medium (CX43 fits) | low |
| B2 Logged in, own server identity | a separate Chrome profile on the server, logged in with a **741 agent account** that has read roles (GA4/GSC viewer, GBP manager read), driven by Playwright MCP with a persistent profile | yes, with a one-time login by Martin over a remote desktop (noVNC via Tailscale) | medium–high | medium: Google may challenge logins from a German datacenter IP; the server holds live sessions |
| B3 Claude in Chrome on the server | the Chrome extension + a visible Chrome on a virtual desktop | possible, but needs a full `claude /login` on the server (not setup-token) and is not documented for Linux servers | high | high: Martin's main logins on a rented box (lesson from the infostealer of 13.10.) |

Recommendation: B1 now, B2 as phase 2 with a separate least-privilege account. Never Martin's main Google, LinkedIn or bank logins on the server.

## 5. Existing servers found (read only, 13.10.)

- `srv1782758.hstgr.cloud` (187.127.103.222): Hostinger VPS. Probably the trading Telegram bot (memory `trading-collaboration`). Not checked.
- `hub.741-studio.com` (35.193.14.30) and 34.122.73.91: Google Cloud VMs, gcloud project `studio-apis-503306`. The gcloud login on the laptop is expired, so the agent cannot list them.
- AltusHost cPanel `mail.741.studio` (128.127.111.40): client production sites. Never for agents.
