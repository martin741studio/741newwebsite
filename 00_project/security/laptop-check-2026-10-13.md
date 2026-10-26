# Laptop check after the infostealer incident (2026-10-13)

- Device: MacBook Pro M1 Pro (MacBookPro18,3), macOS 15.7.7 (24G720), user `martindrendel`
- Incident: 2026-10-13, 13:49 WITA. A fake Cloudflare "verify" page made Martin paste a command into Terminal. The command ran a macOS infostealer (AMOS family).
- Check done: 2026-10-13, 18:10 to 18:40 WITA, read-only. It is a second, independent check.
- Changes made during this check (each with Martin's go):
  1. Removed the stale "Atomic BI" login item.
  2. Moved `/tmp/39494` to `~/QUARANTINE-malware-2026-10-13/staging-tmp-39494` and set mode 000. Nothing deleted.
- No secret values are in this file. It lists names only.

## Verdict

**Laptop clean enough to create new server keys and a new setup-token: YES.**

Both conditions are met (18:22 WITA):
1. The stealer staging folder `/tmp/39494` is moved into the quarantine and locked (mode 000).
2. Martin confirmed that he installed TeamViewer himself on 2026-10-08.

Reasons:
- No malware process runs. No connection to the attacker address 178.62.247.40 exists.
- No persistence: no new LaunchAgent, LaunchDaemon, login item, cron job, profile, shell-file change, browser extension or system extension since the incident.
- All launch items and new apps have valid Developer ID or App Store signatures.
- SIP, Gatekeeper and FileVault are on. XProtect is current (5366, 2026-10-07).

The stolen data is a different problem. The laptop is clean, but the stolen credentials stay valid until Martin rotates them. See "Credentials to rotate".

## Earlier knowledge (session "Kamil Website-Audit + Local-SEO Add-on")

- 13:49: stealer binary ran from `/tmp/.hk3ug2dm`. It packed data into a zip and uploaded it to `178.62.247.40` for about 2 minutes.
- 13:53: the session killed the stealer (PID 13294) and the upload processes. It moved the binary and the archive to `~/QUARANTINE-malware-2026-10-13/`.
- 14:27: a live check found no malware process, no attacker connection and no persistence.
- Gap in that check: it searched `/tmp` only for `.hk3` and `87B3o`. It did not find the staging folder `/tmp/39494`.

## Findings

Status: **clean** = no risk found. **suspicious** = needs Martin's answer or a hygiene fix. **malicious** = malware or malware output.

| # | Item | Status | Evidence | Command |
|---|------|--------|----------|---------|
| M1 | Stealer staging folder `/tmp/39494` (created 13:49:46–13:49:55, 320 files, 325 MB). Holds plain copies of: Chrome and Brave `Cookies`, `Login Data`, `History`, `Web Data` (24 profiles); `login.keychain-db`; SSH keys; `gcloud/credentials.db`; Discord token store; `zsh_history`, `zshrc`, `bash_history`; Safari history. No program files inside. | **malicious** (malware output, not malware) | `ls -laTR /private/tmp/39494`; `find /private/tmp/39494 -type f -perm -u+x` → 0 | `ls`, `find`, `du` |
| M2 | Quarantine `~/QUARANTINE-malware-2026-10-13/`: `hk3ug2dm.bin` (mode 000), `stolen-archive.zip` (132 MB, mode 400) | **malicious**, contained | Binary cannot run (mode 000). Archive list read with `unzip -l`, not extracted. | `ls -la`, `unzip -l` |
| C1 | User LaunchAgents: 4 × `studio.741.*`, Elgato CameraHub, GoogleUpdater, Google Keystone (2 empty plists), Steam `steamclean`, Homebrew MariaDB | **clean** | All programs signed (Corsair, Google, Valve) or known 741 scripts. CameraHub plist rewritten 12:30, before the incident, by the signed Elgato app. | `ls -laT ~/Library/LaunchAgents`; `plutil`; `codesign -dv`; `spctl -a -vv` |
| C2 | 741 jobs | **clean** | Loaded: `studio.741.standup`, `studio.741.listings-poller`, `studio.741.night-shift-sleep`. `studio.741.night-shift` is not loaded, as intended (unloaded 13.10. 18:10). | `launchctl list \| grep studio.741` |
| C3 | `/Library/LaunchAgents` + `/Library/LaunchDaemons` + `/Library/PrivilegedHelperTools`: Epson, TeamViewer (4), Zoom (3), Microsoft Teams updater, Wireshark ChmodBPF | **clean** (TeamViewer see S2) | All signed: TeamViewer Germany GmbH (H7UGFBUGV6), Zoom, Microsoft, Wireshark Foundation, Seiko Epson. No AMOS backdoor files (`~/.helper`, `~/.agent`, `~/.pass`, `~/.username`, `com.finder.helper.plist`). | `ls -laT`; `codesign -dv`; `ls ~/.helper …` |
| C4 | Background task database | **clean** | Only known vendors. Stale entry "Atomic BI" pointed to an app that is no longer in the Trash. | `sfltool dumpbtm` |
| C5 | Login items (before): Atomic BI, Claude, Loom, Google Chrome, Fathom, Notion | **clean** | "Atomic BI" (bundle `bi.atomic.companion-app`, team TT5SR2JM9L) is a BI app, not the AMOS stealer. **Removed on Martin's go.** "Fathom" points to a missing app (stale, harmless). | `osascript … login item` |
| C6 | Cron | **clean** | 2 known jobs: `run-forex-events.sh` (Sunday 23:00), watch-face health export (21:30). No `at` jobs, no emond rules. | `crontab -l`; `atq` |
| C7 | Shell startup files | **clean** (no tampering) | `.zshrc` last changed 2026-05-29, `.zprofile` 2024-10-23. No `.zshenv`, `.zlogin`, `.bash_profile`. `/etc/zshrc`, `/etc/profile` from 2026-04-30 (OS install). `/etc/hosts` default. `/etc/sudoers.d` empty. | `ls -laT`; masked read |
| C8 | Configuration profiles | **clean** | 2 user profiles from 2025 (Screen Time "ManagedSettings", date-time). No MDM, no DEP. | `profiles list`; `profiles status -type enrollment` |
| C9 | Processes | **clean** | No process from `/tmp`, `/Users/Shared` or a hidden folder. All processes started after 13:40 are Terminal shells, Claude Code sessions, the Kraft clean-up script and Apple services. | `ps -axo pid,ppid,user,lstart,command` |
| C10 | Network (established) | **clean** | 0 connections to 178.62.x.x. Connections go to Anthropic, Google, OpenAI, Notion, WhatsApp, Wispr, and to 185.2.31.101 (741.studio host: Airmail + Kraft clean-up script). | `lsof -nP -iTCP -sTCP:ESTABLISHED`; `lsof -nP -i @178.62.247.40` |
| C11 | New executables/scripts since 2026-10-13 12:00 in `~/Library`, `/tmp`, `/private/var/folders`, `~/Downloads`, `/Users/Shared` | **clean** | Only app preference files, Claude "Services" workflows (from 2026-09-11), signed Notion native host, Codex launcher script. | `find … -newermt '2026-10-13 12:00'` |
| C12 | `~/Downloads` newest files | **clean** | Akeeba/Admin Tools zips (17:23, Taxi job), images, PDFs, a WhatsApp audio. No `.dmg`, `.pkg`, `.app` or script. | `ls -laTt ~/Downloads` |
| C13 | Browser extensions: 37 in Chrome (22 profiles) and Brave | **clean** | All from the Chrome Web Store. None unpacked. None installed or updated after 2026-10-09. | `ext_list.py` (reads `manifest.json` + Preferences) |
| C14 | System extensions, kexts, Safari extensions | **clean** | Elgato camera extension, OBS camera extension. No third-party kext. No Safari extension. | `systemextensionsctl list`; `kmutil showloaded`; `pluginkit` |
| C15 | Apps added or updated since 2026-10-01 | **clean** | 13 apps. All signed (Developer ID or App Store). | `find /Applications -newermt`; `spctl -a -vv` |
| C16 | SIP, Gatekeeper, FileVault, XProtect | **clean** | SIP on, Gatekeeper on, FileVault on, XProtect 5366. No XProtect detection log after 13:00. No unified-log line names `hk3ug2dm` or `178.62`. | `csrutil status`; `spctl --status`; `fdesetup status`; `log show` |
| S1 | Staging folder `/tmp/39494` | **contained** (was suspicious) | Newest write inside: 13:49:55. No activity after the stealer run. Moved to `~/QUARANTINE-malware-2026-10-13/staging-tmp-39494`, mode 000, on Martin's go (18:22). | `find … stat`; `mv`; `chmod 000` |
| S2 | TeamViewer installed 2026-10-08, full module, starts at boot, runs now (PID 1653) | **clean** (Martin confirmed he installed it) | Signed and notarised. Installed before the incident, so not from the stealer. Remote-access tools are a common second step after a stealer. | `ls -laT /Applications/TeamViewer.app`; `sfltool dumpbtm` |
| S3 | macOS firewall off; MariaDB listens on `*:3306`; Vite dev server on `0.0.0.0:3000`; a prototype web server on `*:8992`; ARDAgent (Remote Management) active | **suspicious** (hygiene) | Other devices on the same Wi-Fi can reach these ports. Not malware. | `socketfilterfw --getglobalstate`; `lsof -iTCP -sTCP:LISTEN` |
| S4 | `.secrets/apify.env`, `meta-741.env`, `telegram-741.env` are mode 644 (other users can read) | **suspicious** (hygiene) | Others in `.secrets` are 600. | `ls -laT ~/741website/.secrets` |
| S5 | SSH keys not rotated yet | **suspicious** (open task) | `id_ed25519` (2026-01-25), `id_rsa` (2026-02-19), `google_compute_engine` (2026-02-11) are still the stolen keys. | `ls -laT ~/.ssh` |

## What the attacker has (from `unzip -l` of the archive and the staging folder)

Stolen:
- Chrome: `Login Data` + `Cookies` from 24 profiles. Saved passwords per profile: Default 200, Profile 59: 182, Profile 55: 75, Profile 65: 14, Profile 53: 11, Profile 64: 9, Profile 67: 8, Profile 66: 7, Profile 36: 5.
- Brave Default: 29 saved passwords + cookies.
- Extension vault data: MetaMask (Default, Profile 1, Profile 67), LastPass (Default, Profile 1, Profile 67), 1Password (Default, Profile 71).
- `login.keychain-db` (offline copy). Chrome passwords and cookies are encrypted with a key in this keychain. The keychain opens with the Mac login password. The archive holds no password file, so the attacker must crack that password offline.
- SSH keys: `id_ed25519`, `id_rsa`, `google_compute_engine` (+ `known_hosts`).
- `gcloud/credentials.db` (Google Cloud CLI login).
- Discord token store (`leveldb`, 12 files).
- `zshrc`, `zsh_history` (1,780 lines), `bash_history`. These hold API keys and passwords as plain text.
- Safari history, system info, user name.

Not stolen (folders exist but are empty): Telegram, Binance, TonKeeper, Bitwarden, AWS, Docker, FileZilla.
Not in the archive: `~/741website/.secrets/*`, `~/.claude.json`.

## Credentials to rotate (names only)

### A. Stolen. Rotate now.
1. **SSH keys** `id_ed25519`, `id_rsa`, `google_compute_engine`. Make new keys. Remove the old public keys from all hosts below.
   - Hosts in `known_hosts` and history: `187.127.103.222` (root login, a VPS), `github.com`, `hub.741-studio.com`, `56863247.ssh.w1.strato.hosting`, `access1013340746.webspace-data.io`, `s103.cyon.net`, `[128.127.111.40]:6121`, `34.122.73.91`, `35.193.14.30` (Google Cloud), `185.2.31.101` (741.studio).
   - **Check 187.127.103.222 for intrusion before more use.** The history shows root SSH logins there, so the attacker knows the address and has a matching key.
2. **Google Cloud CLI login** (`gcloud/credentials.db`). Revoke the gcloud sessions and remove the old Compute Engine key from project metadata.
3. **API keys in `.zshrc`**: `BRAVE_API_KEY`, `GEMINI_API_KEY`, `OPENAI_API_KEY`, `CLAWDBOT_GATEWAY_TOKEN`.
4. **Keys in `zsh_history`**: 3 OpenAI keys (`sk-…`), 2 Google API keys (`AIza…`), `GEMINI_API_KEY`.
5. **WordPress application passwords in `zsh_history`**: `shuiguru.de` (user "741 Studio - Martin", `WP_API_PASSWORD`) and `leichsenring.wab-dev.de`. Also update the copies in `~/.claude.json` (Novamira MCP entries).
6. **FTP account `agent_deploy@741.studio`** (`ftp.741.studio` / 185.2.31.101). 22 history lines hold its password.
7. **Mac login password.** The keychain copy is offline. A new Mac password protects the next keychain, not the stolen copy.
8. **All passwords saved in Chrome and Brave** (about 540 entries). Start with Google accounts, hosting, registrars, banking, Meta/Ads, client CMS logins. Then sign out all sessions (cookies are stolen).
9. **Password managers**: LastPass master password (session destroy was done earlier), 1Password master password.
10. **MetaMask**: move funds to a new wallet with a new seed phrase. The stolen vault can be cracked offline.
11. **Discord**: change password (this logs out stolen tokens).

### B. Not stolen, but rotate before they go to the new server
Martin's rule: only keys rotated after a clean check go to the server. Files in `~/741website/.secrets/`:
- `standup.env` (`STANDUP_PASSWORD`, used by the night shift)
- any other file the server will use: `apify.env`, `cpanel.env`, `dataforseo.env`, `ga-sc-reporting-bot.json`, `listings-imap.env`, `meta-741.env`, `telegram-741.env`, `youtube-api.env`, `stuerzl-artfiles.env`
- `kraft-ftp.env`: the Kraft FTP password was also pasted into a chat. Rotate it after the Kraft clean-up.

## Open decisions for Martin

1. Done: `/tmp/39494` moved into the quarantine. Martin can delete `~/QUARANTINE-malware-2026-10-13/` himself when he no longer needs the evidence.
2. Done: TeamViewer confirmed.
3. Atomic BI Chrome extension (Default profile): Martin can remove it at `chrome://extensions`.
4. Hygiene (S3, S4): firewall on, MariaDB bound to `127.0.0.1`, `.secrets` files to mode 600. These are settings changes for Martin.

## Third check (2026-10-14, 06:25 WITA, read-only)

Martin asked for one more check. I compared everything with the state of 2026-10-13, 18:20. **Result: still clean. Verdict unchanged: YES.**

| Item | Status | Evidence |
|------|--------|----------|
| New LaunchAgent `studio.741.night-shift-v2` (2026-10-13 19:30) | **clean** | Runs `caffeinate -i python3 ~/741website/reporting/night-shift-v2/run.py` Mon–Fri 17:30 and 20:30. Built by the night-shift v2 sessions (commits `c2308d7`, `49f3a9a`). |
| `~/.ssh` changed (2026-10-13 18:41) | **clean** | New `id_ed25519_nightshift` + `config` (Host `nightshift-01`, User root). Made after the clean verdict, by the night-shift sessions. The old stolen keys are still there and still need rotation. |
| Other launch items, AMOS backdoor paths, cron, profiles, shell files, `/etc/hosts`, `sudoers.d` | **clean** | No change. No `~/.helper`, `~/.agent`, `~/.pass`. |
| Login items | **clean** | Claude, Loom, Google Chrome, Fathom, Notion. "Atomic BI" stays removed. |
| Quarantine | **clean** (contained) | Binary mode 000, staging folder mode 000, archive mode 400. |
| New files in `/tmp` | **clean** | HTML, JSON, text, WAV and `mcp-call*.py` files from Claude sessions (WordPress calls to shuiguru.de). No binaries. |
| Processes started since 18:20 | **clean** | None outside Claude Code, Node, known apps and Apple services. |
| Network | **clean** | 0 connections to 178.62.x.x. New remote groups: Telegram API (149.154.167.99, from Claude Code) and Hetzner (213.133.105.29, 213.239.246.x, from Chrome). Both expected. |
| Browser extensions | **clean** | 37 in total, none new or updated since 2026-10-09. The Atomic BI extension is still installed. |
| Apps, Downloads, new executables in `~/Library` and `/private/var/folders` | **clean** | Nothing new since 18:20. |
| SIP, Gatekeeper, XProtect | **clean** | On, on, 5366. No XProtect detection since 2026-10-13 18:00. |
| Hygiene (firewall off, MariaDB `*:3306`, Vite `*:3000`, `*:8992`, ARDAgent) | **suspicious** (hygiene, unchanged) | Same as S3. |

## Server 187.127.103.222 (2026-10-14, 06:45 WITA, no login)

| Item | Finding | Command |
|------|---------|---------|
| Owner | Hostinger VPS, reverse DNS `srv1782758.hstgr.cloud` | `dig -x` |
| History | An Antigravity agent set up "VPS Night flow" on this server on 2026-03-20 to 2026-03-25 (root SSH, `repo_init.sh`, `dashboard/backend`). Local copy: `~/Desktop/VPS Night flow/`. | `grep` in Antigravity logs, Desktop |
| **Host keys** | **All 3 host keys (ED25519, RSA, ECDSA) differ from the keys in `known_hosts`.** The machine was reinstalled, or the address now belongs to another machine. | `ssh-keyscan` + `ssh-keygen -F` |
| Now runs | Ubuntu 24.04 (OpenSSH 9.6p1), Caddy web server. Open ports: 22, 80, 443. Port 80 redirects to HTTPS. No certificate for the bare IP. | `nc`, `curl -I`, `openssl s_client` |
| Login | **Not done.** SSH stopped at the host-key warning. I did not override it. If the machine belongs to another person now, a login is access to a third-party system. | `ssh -o BatchMode=yes` |
| Hostinger account | Chrome (Default profile) has 1 saved Hostinger login, last used 2026-05-04. It was in the stolen `Login Data`. | `sqlite3` on `Login Data` (URL only) |

Status: **suspicious / unknown.** Only the Hostinger account (hPanel) can show if VPS `srv1782758` is still Martin's.
- Not in the account → the server is not Martin's any more. No action on the server. Rotate the old SSH keys (done list A1).
- In the account → someone reinstalled it. Change the Hostinger password, turn on 2FA, check the account log, then decide: delete or rebuild.

## Atomic BI Chrome extension
Martin gave the go to remove it (Default profile, "Person 1"). Claude in Chrome cannot open `chrome://extensions`, so I could not remove it. Martin removes it himself.

## Closed (2026-10-14, ~07:00 WITA)

Martin, in the Morning Grill chat: "Laptop malware is done." The investigation is closed. The hPanel check is dropped.

Server 187.127.103.222: last use 2026-03-25 (Antigravity logs). All host keys changed after that date. The SSH package on it was published 2026-09-03. Most likely the Hostinger VPS expired and the address went to a new customer. Not verified in hPanel.

Still open (not part of the malware check):
- Rotate the stolen credentials in list A, starting with the SSH keys `id_ed25519`, `id_rsa`, `google_compute_engine`.
- Change the Hostinger password. It was in the stolen Chrome data.
- Remove the Atomic BI Chrome extension (Default profile) at `chrome://extensions`.
- Delete `~/QUARANTINE-malware-2026-10-13/` when the evidence is no longer needed (Martin himself).

## REOPENED: website infection wave (2026-10-15)

Martin reports: sites get infected one after another. So far: Tacheles, Kraft Physiotherapie, Katharina Kisser.

### Confirmed facts (2026-10-15, ~14:40 WITA, read-only)
1. **All 3 infected sites had saved logins in the stolen Chrome data** (checked against the quarantined copy, names only): tacheles-beratung.de (1), physiotherapiekraft.de (2 + SharePoint), katharinakisser.at (1).
2. **katharinakisser.at is actively infected now.** robots.txt lists 20 planted sitemaps. sitemap.xml holds spam entries with lastmod 2026-10-15 (today), thousands of fake `/item/<id>/detail` URLs. All normal pages return HTTP 500. Same pattern as Kraft.
3. **The infected non-Strato sites sit on the 741 server 185.2.31.101** (mail.741.studio): katharinakisser.at, physiotherapiekraft.de, physiotherapieoberhausen.com, 741.studio. Tacheles sits at Strato (w02.rzone.de).
4. **The stolen data holds server-level logins:** `741.studio:2087` (WHM = whole server), `physiotherapieoberhausen.com:2096` (cPanel webmail), 741.studio `/wp-login.php`, `clients.741-studio.com`, `hub.741-studio.com/setup`, plus hosting accounts: IONOS (5 entries, users kam…/phy…/964…/inf…/616…), Strato (www + webmail), Hetzner, Hostinger, GoDaddy-NS domains. Also stolen earlier: FTP `agent_deploy@741.studio` (password in zsh_history) and WP app passwords shuiguru.de + leichsenring.wab-dev.de.
5. Surface scan of 20 client sites (homepage + robots.txt): no spam signatures on the others right now. tacheles-beratung.de homepage is clean again; its `/wp-login.php` returns 503. physiotherapiekraft.de is live again (HTTP 200).

### Conclusion
This is a credential-driven campaign from the 2026-10-13 infostealer theft. Site cleanups alone fail while the attacker keeps server passwords (Kraft reinfection on 14.10. proves it). Rotation of hosting and server credentials must come first.

### Response plan (order matters)
1. **Lock the 741 server (185.2.31.101):** change WHM root password, then every cPanel account password, then FTP `agent_deploy`, end all active WHM/cPanel sessions, check for attacker-created accounts, SSH keys, and cron jobs.
2. **Rotate hosting accounts:** Strato (Tacheles), IONOS (both accounts), Hetzner, Hostinger, GoDaddy/registrar. Turn on 2FA everywhere.
3. **Then clean katharinakisser.at** (same runbook as Kraft: backup, remove droppers/planted files, clean core, new salts, check robots/sitemaps, Search Console removal).
4. Then rotate WP admin passwords on all client sites and force logouts.
5. Keep the full list-A rotation from this report running (browser passwords, API keys, SSH keys).

## Fourth check (2026-10-26, 09:35 WITA, read-only)

Martin asked for a fresh check, 12 days after the last one and 6 days after the server-side reinfection campaign (`wp-incident-2026-10-20-kisser-physiokraft`, same attacker group, still probing as of 23.10). **Result: laptop still clean of malware. One standing risk not yet closed: the original stolen SSH keys.**

| Item | Status | Evidence |
|------|--------|----------|
| Launch items changed since 14.10. | **clean** | `homebrew.mxcl.mariadb.plist` renamed to `sh.brew.mariadb.plist` (Homebrew's own rename, 15.10.); TeamViewer plists updated 22.10. (vendor auto-update, signed). No unknown entries. |
| AMOS backdoor paths, cron, shell files | **clean** | No `~/.helper` etc. Cron unchanged (2 known jobs). `.zshrc`/`.zprofile` mtimes unchanged since before the incident — no tampering. |
| Login items | **clean** | Claude, Loom (listed twice, harmless UI duplicate), Google Chrome, Fathom (stale, points to a missing app), Notion. Atomic BI stays removed. |
| Quarantine | **changed by Martin, expected** | `stolen-archive.zip` is gone (folder mtime 25.10.) — matches the open item "delete when no longer needed." `hk3ug2dm.bin` (mode 000) and the staging folder (mode 000) remain. |
| Processes | **clean** | 4 long-running orphaned `cat` processes (since 14.10.) are leftover log-pipe readers from an earlier Claude Code session's own scratchpad (`remote-login.log`, `rc-login.log`, `setup-token4.log` — server-setup logging), not malware: no network, no suspicious file access. |
| Network (established) | **clean** | 0 connections to any of the 5 known attacker IPs from both incidents (178.62.247.40, 195.2.76.117, 193.24.211.10, 20.194.45.183, 109.172.87.198). All connections go to expected apps and to 185.2.31.101 (741 server). |
| Listening ports | **improved** | MariaDB now bound to `127.0.0.1:3306` only (was `*:3306`). `node *:3000` (Vite) and ARDAgent still open to the network — unchanged hygiene gap. |
| Firewall | **still off** | Unchanged since 13.10. (S3). |
| New executables/scripts since 14.10. in `~/Library`, `/tmp`, `/private/var/folders`, `~/Downloads`, `/Users/Shared` | **clean** | Only the known `mlx-whisper` pipx install, the known Codex launcher, and Apple's own Translation-feature hotfix files. |
| `~/Downloads` newest files | **clean** | Client work (CRO mockup, Loom script, WhatsApp media, an Elementor add-on folder, a LinkedIn export zip). No installer, no script. |
| Browser extensions | **clean** | 37 total, all Chrome-Web-Store-verified, none unpacked. One new since the last check: ChatGPT (23.10., store-verified). Atomic BI confirmed removed. |
| SIP, Gatekeeper, XProtect | **clean** | SIP on, Gatekeeper on, XProtect 5368 (newer than the 5366 seen on 14.10.). |
| **SSH keys** | **NOT ROTATED — standing risk** | `id_ed25519` (25.01.), `id_rsa` (19.02.), `google_compute_engine` (11.02.) are unchanged since before the theft — the attacker's copies from 13.10. still work on any host that has not removed the matching public key. A new key `id_ai_server` was added 19.10. for other work; it does not address this. |

**Conclusion: no new malware or persistence on the laptop.** The open risk is not on the laptop itself — it is that the stolen SSH keys from 13.10. were never rotated, 13 days later, while the same attacker group is still actively probing 741's infrastructure (confirmed 23.10.).

**Martin, 26.10. ~09:50 WITA: the SSH key risk is "already handled elsewhere."** He did not specify how. The key files on this laptop (`id_ed25519`, `id_rsa`, `google_compute_engine`) are unchanged, so either their matching public keys were removed from the remote hosts, or new keys were issued through another session/machine. Not independently verified on the laptop side.
