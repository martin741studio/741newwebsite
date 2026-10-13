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
