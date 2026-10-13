# V02 — put your claude code on a vps, it's the best decision I made

- Channel: João Nina Matos
- URL: https://www.youtube.com/watch?v=ntTq41lAa2w
- Type: practitioner walkthrough (not a step-by-step tutorial), 7m 14s
- Upload date: 2026-07-24
- Views: 6,915 (at fetch)
- Fetch date: 2026-10-13 (Apify discovery + `johnvc/YoutubeTranscripts`, dataset `jkrUikamYc0lfnl76`. Raw transcript not stored here.)

## Extract (own words)

1. He runs Claude Code on a rented VPS for about one month. The session keeps going when the laptop closes or loses Wi-Fi.
2. He claims one run of 19 hours without a break. Before, his longest unattended run was 1–2 hours.
3. Host: Hetzner (he picks it as the cheapest). He names Hostinger, AWS and DigitalOcean as options. No price given.
4. Access: Tailscale private network joins the VPS, the laptop and the phone. He turns off public SSH, so only devices in the tailnet can connect.
5. Client: Termius (desktop and phone app) saves the hosts. He checks and answers the session from the phone.
6. He let Claude and an LLM guide the server setup. He says he does not understand all of the DevOps.
7. Long-run method: he spends about one hour with Claude to write 9–13 plan documents, one per task. Then Claude works through them in order.
8. Loop per task: Claude opens a pull request. A separate reviewer (Claude code review in GitHub Actions) approves or rejects. Claude fixes and repeats until approval, often 4–5 rounds. Then it merges and moves to the next plan.
9. He keeps builder and reviewer separate on purpose: the reviewer wrote no code, the builder reviewed no code.
10. He also deploys apps from the same VPS and lets Claude handle `.env` secrets. He admits this is a security risk, more so with clients.
11. If you fear auto-merge, he suggests that deploys run from a separate production branch, not from main.
12. Sometimes the session stops with a question. He answers it from the phone.

Short quote: "I got it to work for literally 19 hours straight."

## Setup details

- Host: Hetzner VPS (Linux). Cost not stated.
- Tools: Tailscale (account + phone app), Termius, Claude Code CLI, GitHub, a Claude code-review GitHub Action.
- Commands: none shown on screen in the transcript. He says to ask Claude for provider-specific commands.

## IF/THEN rules for 741

1. IF 741 rents a server for night runs, THEN put it behind Tailscale and close public SSH before Claude Code goes on it.
2. IF a night run must last many hours, THEN prepare one written plan file per task in the day, and let the night agent work the list in order.
3. IF a night agent changes code or page content, THEN let a separate reviewer agent check it. The builder never approves its own work.
4. IF the work touches a client website, THEN the night agent stops at a draft, PR or staging. Merge and deploy stay with Martin's go (matches the 741 rule "no website changes without go").
5. IF the server holds client secrets, THEN do not deploy client sites from the same box where the agent runs with broad rights.

## Caveats

- One person's account. The 19-hour run is not shown in full and not verified.
- He auto-merges to main and deploys from main. That conflicts with 741 go-rules. Copy the loop, not the auto-merge.
- No cost, no usage-limit numbers, no data on how many runs failed.
