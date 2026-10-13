# V06 — you need to try Paperclip RIGHT NOW!

- Channel: NetworkChuck
- URL: https://www.youtube.com/watch?v=7RVf25Rg0Mc
- Type: hands-on demo with sponsor, 28m 48s
- Upload date: 2026-09-24
- Views: 1,344,473 (at fetch)
- Fetch date: 2026-10-13 (Apify discovery + `johnvc/YoutubeTranscripts`, dataset `jkrUikamYc0lfnl76`. Raw transcript not stored here.)

## Extract (own words)

1. Paperclip is an open-source "meta harness": a web app that manages many agents (Claude Code, Codex, Hermes, local models) as employees. Each agent has a role, a manager and a budget, and a human approves key steps.
2. Host: he installs it on an Ubuntu VM with two commands (download script, run it). It serves on port 3100. Mac, Linux or WSL2 also work for a trial.
3. Each harness runs on the Paperclip server. He had to install and log in Claude Code on that box before the CEO agent worked.
4. The human is "the board". New hires and key steps need board approval in an inbox.
5. Agents talk only through tasks, not an open chat room. A blocked agent escalates to its manager agent first, then to the human.
6. Decisions inbox: the lead agent posts short questions (example: replace the part today, skip a test, open a ticket). He answers them like cards.
7. Task controls: pause a subtree, cancel, reviewers, approvers, monitors, watchdogs. He pauses an agent that started work he did not want.
8. Routines: scheduled tasks with triggers (example: daily storage check at 10:00 that creates a decision only when space is low). He runs a daily 17:00 stand-up routine where each agent reports and asks the others questions.
9. Secrets: stored in settings and granted per agent. An agent without the grant cannot use the key.
10. Traceability: activity timeline, artifacts (reports, maps) and import/export of the whole org.
11. Honest result: agents timed out at times and could not name the root cause at first. The final answer came after more runs over days.

Short quote: "Our agents are the employees. We're calling the shots."

## Setup details

- Host: own VM (Proxmox) or a VPS. Port 3100.
- Tools: Paperclip (open source), Claude Code, Codex, Hermes, Pi harness with local models. Optional API integrations via secrets and skills.
- Commands: install script (two lines, shown on screen, not in transcript). Exact commands in the project README.
- Cost: not stated. Each harness bills on its own plan or API.

## IF/THEN rules for 741

1. IF a night agent hits a block, THEN it escalates to a coordinator first, and only open decisions reach Martin's morning grill.
2. IF a routine checks something (rankings, uptime, citations), THEN it creates a decision card only on a threshold breach, not a daily "all fine" note.
3. IF a night agent needs a key, THEN grant the key per agent, not to every agent.
4. IF night work starts on something Martin did not want, THEN he needs one pause control for that task tree from the phone.
5. IF 741 tries a multi-harness tool like Paperclip, THEN test it on internal work first, never on client sites.

## Caveats

- Hype tone and a long sponsor segment (Flare). The "IT department" demo is a fun case, not client work.
- It is a single demo. Reliability over weeks is not shown. Agents timed out during the demo.
- It runs Claude Code under a third-party orchestrator. Check that this use fits Anthropic's terms for subscription logins before production use.
- In the Flare part, agents started password resets he did not ask for. That shows the need for hard limits on write actions.
