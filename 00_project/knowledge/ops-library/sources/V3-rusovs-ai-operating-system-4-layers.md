# V3 — Turn Claude Code Into Your AI Operating System (4 Layers)

- Channel: Pav Rusovs | Automation Orbit
- URL: https://www.youtube.com/watch?v=Zs3faMCDYNs
- Type: YouTube walkthrough, 14m 57s
- Upload date: 2026-09-22 (from YouTube search listing. Transcript actor returned no date)
- Views: 95,881 per transcript actor; 234,407 per search scraper on the same day (the two scrapers disagree. Both above 5,000)
- Fetch date: 2026-10-13 (transcript via Apify johnvc/YoutubeTranscripts. Raw transcript not stored here)

## Key points (paraphrased from transcript)

1. Framework "MAPS": **Memory, Agent, Pulse, Screen**, built in that order.
2. Memory: a short CLAUDE.md (about 40 lines) holds no facts, only pointers ("signposts") per area, so Claude reaches any fact in two hops. Rules: every fact has one home. A nightly check flags signposts that point to moved files.
3. Measured: with the map, the same lookup took about half the time and about 40% fewer tokens than without.
4. Agent: the same Claude Code subscription on two machines, the laptop and an always-on VPS, with the folder synced every 5 minutes. Phone access through a Telegram bot on the VPS. Private network via Tailscale.
5. The VPS Claude has a settings file that blocks every send, share or delete tool. It can draft an email but never send one.
6. Pulse: a `routines.yaml` lists every routine, its purpose, schedule and machine. A scheduler checks every 5 minutes. Every run leaves a record. A failure cap stops a broken job from burning the monthly budget.
7. Morning digest lands before he wakes: what happened overnight, what is due today, who is waiting on him.
8. Screen: the dashboard **shows but never stores**. Every panel reads from files. A "needs Pav" list is the only list that waits for a human, and only he can tick a task done. Claude never marks done.
9. Away 10 days in August with the laptop shut. Routines and digest kept running.
10. Notes that Anthropic's terms do not allow using a Claude subscription through third-party harnesses. Running Claude Code itself on a server signed in with your own account is his route.

## Use for 741

Supports: one routines registry with run records, a "waiting on Martin" list as the only human queue, "agent never marks done", draft-only rights for unattended agents, and signpost memory per client.

Short quote: "only asks you when a human is needed"
