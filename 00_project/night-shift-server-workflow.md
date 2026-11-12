# Night Shift + Server — workflow spec v0.1 (design, checkpoint 1)

> **Stand 11.11.2026: Entscheidung N52 in §15.** Die Nachtschicht zieht auf den Server `741-agents-01`. §1–§14 sind Design-Stand 13.10.

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

## 15. Entscheidung N52 (11.11.2026): Nachtschicht auf den Server 741-agents-01

**Martins Antwort (Karte „Nacht-Host“, Abend-Grill-Folge 11.11.):** „Server 741-agents-01 (Empfehlung)“. Zweite Karte „Live-Check“: „Ja, starten + prüfen (Empfehlung)“.
Die Karten-Antwort ist eine Richtungsentscheidung. Sie ist kein Bauauftrag. Jeder Bauschritt unten braucht Martins eigenen Auftrag, Live- und Config-Schritte zusätzlich sein Go.

### 15.1 Was nachts auf dem Server läuft
- Alle 4 Queue-Klassen aus `build_night_queue.py`: `draft`, `research`, `public_audit`, `build`. Keine Klasse braucht per Definition einen Login oder Martins Chrome.
- Gleicher Runner wie am Laptop: `reporting/night-shift-v2/run.py` mit `claude -p`, Caps 14 Läufe / est. USD 10, `--permission-mode dontAsk`, Schreiben nur unter `reporting/night-shift/**`.
- Ausdrücklich nicht: senden, veröffentlichen, deployen, Live-Writes (WordPress, Portal, Supabase außer Night-Cards), Ads, Geld, Arbeit mit Martins Chrome-Logins. Diese Punkte bleiben Tagesarbeit mit Go je Änderung.

### 15.2 Live-Stand des Servers (read-only geprüft 11.11. ~20:10 WITA)
| Punkt | Stand |
|---|---|
| Host | `741-agents-01`, Hetzner CAX31 Arm, Falkenstein, Tailscale `100.124.61.26`, up 28 Tage, Disk 14 / 150 GB |
| Tailscale am Laptop | war gestoppt; am 11.11. auf Martins Karte gestartet |
| Claude Code | 2.1.299, User `nightshift`, `setup-token` vorhanden (`~/.claude-oauth-token.env`, 600) |
| Browser-Layer | Xvfb, Fluxbox, x11vnc, noVNC, Chrome (CDP 9222) laufen |
| Health-Check | **PARKED seit 15.10. 13:14** (3× „exit 1“, kein Grund geloggt). Timer läuft weiter und meldet alle 10 min „skipped“ |
| Remote Control | **aus seit 15.10. 13:14** (`claude-remote-control.service` dead) |
| Drill | 01.11. FAIL: Remote Control lief schon vorher nicht |
| Heartbeat | pingt alle 30 min „OK“ an Healthchecks.io, **obwohl** der Health-Check geparkt ist. Der Canary sieht darum kein Problem |
| Repo-Klon | `main` auf `88ad0b69` vom 14.10. Laptop: 56 Commits nicht gepusht, `origin/main` vom 27.10., 859 offene Pfade |
| Nacht-Runs | auf dem Server nie gelaufen; kein Nacht-Timer vorhanden |
| Secrets | voller `.secrets/`-Ordner (13 Dateien) seit 14.10., also auch Schreib-Keys (`cpanel.env`, `kraft-ftp.env`, `meta-741.env`, `stuerzl-artfiles.env`). Widerspricht §6.6 (nur Lese-Keys) |

### 15.3 Was eingerichtet werden muss (Reihenfolge, nichts davon gebaut)
N53 (11.11.): Martin will zuerst die Schritte 1–2 (Sicherheit + Health). Start erst auf seinen eigenen Auftrag.
1. **Secrets reduzieren (M + Go):** Schreib-Keys vom Server entfernen. Nur Lese-Keys bleiben (DataForSEO, Apify, GSC/GA4-Service-Account read, Healthchecks, Telegram nur für Pings). Prüfen, ob die Keys nach dem Infostealer vom 13.10. rotiert sind (S0).
2. **Health-Check reparieren:** Grund für „exit 1“ am 15.10. finden, PARKED-Marker erst danach löschen, einmal von Hand laufen lassen. Heartbeat an den Health-Status koppeln, damit „parked“ nicht als „OK“ pingt.
3. **Git-Transport (Martins Go für Push):** 56 Commits pushen; Queue-Eingaben, die die Nacht braucht (Abend-Logs, `00_project/assets/...`-Texte), committen oder per Sync auf den Server. Regel aus `night-shift-server-data-transport.md` §3 bleibt: Laptop besitzt `main`, Server nur `nightshift/*`.
4. **Queue zum Server:** Die 17:00-Karte schreibt `reporting/night-shift/queue/<date>.json` lokal. Weg zum Server festlegen (Push der Queue-Datei auf einen Branch, Server `git pull` 17:30). Ohne Queue-Datei kein Lauf (N34 bleibt).
5. **Runner portieren:** `run.py` auf Linux testen (Pfade, TZ `Asia/Makassar`, Deadline). Neues Fenster möglich (N6: bis 05:00), da kein 23:00-Internet-Limit mehr gilt. Fenster = Martins Entscheidung.
6. **Tests T1–T8 auf dem Server** (`workflow-builds/nightshift/test-scenarios.md`), dann ein Hand-Lauf, dann Timer **deaktiviert** anlegen.
7. **Go für die erste Server-Nacht** → Timer an. Laptop-LaunchAgent `studio.741.night-shift-v2` erst danach entladen (Martins Go). v1-Runner lief am 27.–30.10. noch lokal (Quelle unklar, Plist fehlt jetzt): vor dem Umzug klären.

### 15.4 Zugänge und Secrets, die das berührt
- Server: `.secrets/` (Reduktion), `setup-token` (bleibt), GitHub-Zugang des Klons (nur `nightshift/*` pushen).
- claude.ai-Connectors sind über das volle `claude auth login` auf dem Server aktiv (Drive, Supabase, Gmail …). Der Runner nutzt `--strict-mcp-config`, darum sieht der Nacht-Lauf sie nicht. Interaktive Server-Sessions sehen sie.
- Browser-Profil auf dem Server: Logins (Google `741studio18`, ChatGPT, LinkedIn …) waren am 14.10. nur vorbereitet. Für die Nacht nicht nötig.

### 15.5 Veraltete Doku (nicht geändert)
`night-shift-server-hosting-options.md` (CX43 Nuremberg „chosen“), `night-shift-server-runbook-draft.md` („nothing done yet“), `night-shift-server-pilot-plan.md` (N14) und `night-shift-blueprint.md` (v1) zeigen den Stand vom 13.10. Der echte Stand steht in `workflow-builds/nightshift/decisions.md` N35–N51 und in diesem §15.


### 15.6 Zugangscheck auf dem Server (12.11.2026, read-only, vom Morgen-Grill-Chat per Tailscale-SSH)
Modell-Regel (Martin 11.11., HARD): Nacht-Läufe und Subagents nur mit Sonnet (`claude-sonnet-5-5`). Kein Opus, kein Fable, kein Hochstufen. Kann Sonnet ein Item nicht lösen, ist es BLOCKED.

| Quelle | Ergebnis | Status |
|---|---|---|
| Claude Code 2.1.299 + Sonnet (`claude -p --model claude-sonnet-5-5`) | Antwort „OK“ | geht |
| Google Service Account `reporting-bot@studio-apis-503306` | Token OK, GSC 9 Properties, GA4 41 Properties | geht (Python-Lib `google-auth` fehlt, JWT per openssl geht) |
| DataForSEO | „Access denied. Your IP is not whitelisted“ (Task 40207) | **geht nicht**: Server-IP `162.55.46.13` muss in die Whitelist (app.dataforseo.com/api-access) |
| Supabase `741-portal` | REST erreichbar, Login Standup-User OK | geht (nur mit RLS-Rechten des Standup-Users) |
| Local Falcon | API erreichbar, **kein Key auf dem Server** | geht nicht ohne Key |
| Google Ads API | keine Zugangsdaten auf dem Server | geht nicht (für Planungsläufe nicht nötig) |
| Browser / Chat / MCP | Runner nutzt `--strict-mcp-config`, keine Logins im Server-Chrome | nachts nicht verfügbar, per Design |
| Schreib-Keys auf dem Server | `cpanel.env`, `kraft-ftp.env`, `meta-741.env`, `stuerzl-artfiles.env`, `listings-imap.env` liegen dort | widerspricht §6.6, Entfernen = Schritt 1 (N53), braucht Go |

**12.11.2026, Martins Go (Karte „Schreib-Keys“):** `cpanel.env`, `kraft-ftp.env`, `meta-741.env`, `stuerzl-artfiles.env` und `listings-imap.env` vom Server entfernt (`shred -u`). Kein Server-Dienst, Timer oder Cron nutzte sie (vorher geprüft). Backup byte-gleich geprüft: `.secrets/server-removed-2026-11-12/` (Laptop, chmod 700). Auf dem Server bleiben: apify, canary-telegram, dataforseo, ga-sc-reporting-bot.json, healthchecks-uuid, standup, telegram-741, youtube-api.
**Local Falcon (Martins Go „Key auf den Server“):** offen. Lokal gibt es keine Key-Datei in `.secrets/`; Local Falcon läuft nur über den MCP-Connector.

**12.11.2026, Health-Check repariert (Martins Go, Karte „Health-Fix“):** Ursache für PARKED seit 15.10.: `health_check.py` entfernte `CLAUDE_CODE_OAUTH_TOKEN`. Claude fiel auf das abgelaufene Voll-Login zurück („OAuth session expired and could not be refreshed“, exit 1). Fix: Token aus `~/.claude-oauth-token.env` laden, Modell `claude-sonnet-5-5`, Remote Control wird nur neu gestartet, wenn der Dienst enabled ist (bleibt aus). `heartbeat_ping.sh`: sendet `/fail` bei PARKED, fehlgeschlagenem letztem Check oder Heartbeat älter als 30 min. Backups `*.bak-2026-11-12`. Handlauf 14:17 WITA: ok, $0.015. Heartbeat-Ping OK. Der `/fail`-Zweig ist nur syntaktisch geprüft, nicht live ausgelöst (würde einen Canary-Alarm senden). Kosten: Check alle 10 min ≈ $0.015 → ca. $2.2/Tag.

### 15.7 Schritte 3–6 erledigt (12.11.2026, Martins Go „Schritte 3–6 jetzt“)
- **Git-Transport:** 56 Commits gepusht (`7b22445d..6c3df3b3`), Server per `--ff-only` auf `main`. Weitere Commits `99f76358`, `e17b48ec` und Prompt-Fix ebenfalls auf dem Server.
- **Runner-Port (`run.py`):** Claude-Pfad per `shutil.which`, Standardmodell `claude-sonnet-5-5`, **harte Sperre: startet nicht, wenn `NIGHT_MODEL` kein Sonnet ist** (lokal mit `claude-opus-5-5` getestet: verweigert). `stdin=/dev/null` für jeden Lauf. `Bash(cd:*)`, `Bash(echo:*)` erlaubt; Prompts: Shell-Befehle nur einzeln, ohne Ketten.
- **Tests auf dem Server:** Trockenlauf ok · T8 STOP-Datei: „not starting“ · Kappung: stoppt ohne Lauf · T5 „Mail senden“: nicht gesendet, nur Entwurf + Hinweis an Martin · Handläufe: Executor + Critic pass, 0 Verstöße, 0 gesperrte Befehle im letzten Lauf, Modell nur `claude-sonnet-5-5`, ca. $0.15 pro Item. T1–T4 sind Chat-Trigger-Tests (Skill-Laden), nicht serverrelevant. T6 (Injection) und T7 (echtes Plan-Limit) nicht live ausgelöst.
- **Timer:** `~/.config/systemd/user/night-shift.service` + `night-shift.timer` (täglich 17:45 WITA, holt vorher `main`). Status: **disabled, inactive**. Fenster bleibt 17:30–22:45 (Runner-Standard).
- **Transport-Skripte (Laptop):** `reporting/night-shift-v2/server/push_queue.sh <datum>` (Queue zum Server) und `pull_results.sh <datum>` (Ergebnisse + Heartbeat nach `reporting/night-shift/server-<datum>/`). Selbsttest ok.
- **Offen bis zur ersten Server-Nacht:** Timer-Go; Abend-Grill ruft `push_queue.sh` nach `build_night_queue.py --write` auf und Morgen-Grill ruft `pull_results.sh` auf (Skill-Änderung); Laptop-LaunchAgent `studio.741.night-shift-v2` entladen, damit nicht beide laufen; DataForSEO-IP; Local-Falcon-Key.
