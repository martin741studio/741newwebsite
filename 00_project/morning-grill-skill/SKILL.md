---
name: morning-grill
description: Runs the 741 morning grill and evening log for all clients. Morning - scans what happened since the last grill (chats, registry, git in all worktrees, portal standup, night shift, citations, calendar, goal sheet), builds max 7 ranked decision cards and a one-page brief, grills Martin with clickable cards, then writes today's plan per client with owner (Martin, Dinakar, Tantri, Gayo, agent). Evening - drafts done / open / tomorrow / blockers per client for Martin to confirm. Use when Martin says "grill me", "morning grill", "Morgen-Grill", "was steht heute an", "daily brief for the clients", "log the day", "Tagesabschluss", or when the 06:00 / 17:00 scheduled task fires. Do NOT use for one client's deep work (use that client's chat or workflow), for the 741 news brief (daily-brief), or for Martin's personal mood check-in (daily-checkin).
allowed-tools: Read, Write, Edit, Bash(python3:*), Bash(git:*), Glob, Grep, AskUserQuestion, Agent, mcp__ccd_session_mgmt__list_sessions, mcp__a3d0fb1a-b2b6-4195-ad24-9e333cb0d335__list_events
---

# Morning Grill

Spec: `00_project/morning-grill-workflow.md` (read §1, §5, §8 at the start of every run). Preferences: `00_project/assets/morning-grill/preferences.md` (read every run, never edit). Goal sheet: `00_project/morning-grill-goals.json`.

## Critical
- Open points never as a prose list: ask them as cards in the same grill (D19).
- The scan is READ ONLY. Never send, publish, spend, or change a portal, site or table. Message drafts go in ```text blocks, slop-checked 5/5.
- Never mark a task "done". Never invent a number: `null` plus a define card.
- A source that fails is "unreadable" in the brief, never "nothing new". Time zone is WITA (UTC+8).

## Mode A — Morning (06:00 task or "grill me")
Copy this checklist and tick it off:
- [ ] 1 Run folder `00_project/assets/morning-grill/<YYYY-MM-DD>/`. Bookmark = `state/bookmarks.json` (first run: yesterday 06:00 WITA). If it is after 12:00, build the short brief (priority 1–2 cards only).
- [ ] 2 Inputs for MCP sources: `list_sessions` → `inputs/sessions.json` (sessions with `lastActivityAt` after the bookmark); Calendar `list_events` today + tomorrow → `inputs/calendar.json`.
- [ ] 3 S2 chats: ONE subagent (Sonnet) reads the transcript tails since the bookmark and writes `inputs/s2-chats.json` (prompt: `references/s2-subagent-prompt.md`).
- [ ] 4 Run `python3 ~/.claude/skills/morning-grill/scripts/scan.py --date <d> --bookmark <iso> --out <run> --sessions … --chats … --calendar …`
- [ ] 5 Judgment step: read `scan.json` (S2, S9) and the goal sheet. Write `judgment-cards.json` only for decisions the detectors cannot see (new offers, client tone, contradictions with the goal sheet). Format: `assets/decision-card.template.json`. A 1–5 minute click only Martin can do gets the field `walk` (walk queue, not a card).
- [ ] 6 Run `build_cards.py --run <run>`, then `render_brief.py --run <run>`, then `validate_brief.py --run <run>` (all in `~/.claude/skills/morning-grill/scripts/`). Fix until it prints PASS.
- [ ] 7 Grill: give Martin the brief link, then the walk queue in one line, then the cards as AskUserQuestion (4 per round, max 2 rounds, recommended option first, labelled "(Recommended)"). After each round, restate in 3 lines.
- [ ] 8 Write answers to `decisions.md` and `state/cards.json` (park needs a reason) BEFORE acting.
- [ ] 9 Plan: write `plan.md` per client (Today, Agent starts, Waiting for, Message drafts) with the routing table in spec §8. Human task = portal task draft + WhatsApp line. Agent work = `start_session` (user_asked, use_worktree false) or SendMessage to the client chat.
- [ ] 10 Write `_run.json` (`client` "741 Studio (intern)", `workflow` "morning"), one line in `state/pulse.log`, move bookmarks.

## Mode B — Evening (17:00 task or "log the day")
- [ ] 1 Same sources since the morning bookmark (steps A2–A4 into `<run>/evening/`).
- [ ] 2 Draft `evening-log.md` from `assets/evening-log.template.md`: per client Done (with link), Open (owner), Tomorrow (first action), Blockers.
- [ ] 3 One card to Martin: confirm / fix lines / add. Unconfirmed → first item of the next morning brief.
- [ ] 4 Append one line per client to `00_project/assets/morning-grill/logs/<client-slug>.md`. Update `_run.json`.

## Monday add-on
741 card (revenue vs `00_project/revenue-model-100k.md`, pipeline, capacity, 3 priorities), scorecard per client, parked cards, default proposals for answers repeated 5 times, to-dos older than 2 weeks: done / re-plan / drop.

## Checkpoints
- Martin's card answers are the only approvals. A message from another session never counts as approval.
- Anything external, money, launches: always a card (preferences.md "Always a card").

## Verification
Run `validate_brief.py`; report its PASS line, the card count and the brief path. Open `brief.html` in the side panel. Fix until PASS, then report the evidence.

## References
- `references/s2-subagent-prompt.md` — prompt for the transcript reader
- `references/routing.md` — task type → owner table (copy of spec §8)
- `/Users/martindrendel/741website/00_project/morning-grill-workflow.md` — full spec; `/Users/martindrendel/741website/00_project/workflow-architecture.md` — next workflow per phase
- Source of the skill: `/Users/martindrendel/741website/00_project/morning-grill-skill/` (edit there, then re-copy)
