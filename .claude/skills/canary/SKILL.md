---
name: canary
description: Runs the 741 canary (outage watch) workflow — adds a check for a client system (website, form/funnel, automation like Zapier/Make/n8n, Google Ads), handles an incoming canary alert (diagnose, one safe self-heal, escalate), and gives the daily canary status for the morning grill. Use when Martin says "canary", "set up a canary for <client>", "überwache <system>", "sag mir sofort wenn <X> ausfällt", "canary alarm", "was ist down", or a client reports a silent outage. Also use at the end of Automation Build's go-live step (L6) to add the monitor. Do NOT use to build the automation itself (use the automation-build workflow), for performance/reporting questions with no outage ("wie lief Ads diese Woche"), or for any website/Ads change — canaries only read and alert, they never change a client's live site or Ads account.
disable-model-invocation: false
allowed-tools: Read, Glob, Grep, Bash(python3:*), Bash(curl:*)
---

# Canary (Ausfall-Wächter)

## Critical

- **Pre-send sweep (Martin, 5th repeat 2026-10-14):** before the final reply, every item that waits on Martin (open points, go, his own steps, a message to send, a login, a delete) is an AskUserQuestion card, never a prose list.
- This skill triggers on natural language (an outage report needs a fast response, not a remembered slash command). That is safe only because every write is gated below — never loosen those gates to compensate for easier triggering.
- Canaries read and alert. They never change a client's website, Google Ads (budget/bids/campaigns/conversions), or send a message to a client. Any write into a client system (Zapier replay, re-enabling a Zap, creating a tag) needs `allowlist.py check <action>` to say "needs Martin's go" AND Martin's go on that specific incident.
- Never type a password, API key or token into any field. Credentials come from Martin (or his go to another session), saved by a script into a 600-mode file under `.secrets/`.
- A failed read is "unreadable", never "down" and never "ok" (rule R6.2). Say so explicitly and do not alert on one failed check — confirm with a 2nd check or a 2nd location first.
- Questions to Martin only as AskUserQuestion cards, with a recommendation first. Any text delivered to Martin or a team message goes through the AI-slop check before it is shown.
- SEV1 (a live client's lead path is broken right now) pages Martin 24/7. Everything else waits for the morning grill, unless Martin's card for that client said otherwise.

## Design and build record
Full design, decisions (C1–C13) and the hand-run proof on Marcel Rosenbach's real outage are in `00_project/workflow-builds/canary/`. Read `decisions.md` before changing escalation, channel or runner choices — they are Martin's calls, not defaults to improvise on.

## Mode A — Add a canary ("set up a canary for X")
1. Read the client's lead path from memory + the client chat (page → form → automation → CRM/ESP → Ads).
2. Pick checks from `references/check-catalogue.md` (types L/S/E/R/A). Prefer E (platform push) over polling when the platform offers it.
3. For each check, draft a row matching the schema in `00_project/canary/canaries.json` (`_schema` key). Severity: SEV1 only if it is a live lead path.
4. Self-heal: pick an id from `references/allowlist.md`, or leave `self_heal: null` if nothing safe applies.
5. Any check that creates something in a client account (a Zapier Manager Zap, an Ads script) needs Martin's go before you build it — show him what you propose, wait for the card answer. Build steps for the Zapier push pattern: `references/zapier-manager-setup.md`.
6. Save the row(s): write to a temp file, then `python3 scripts/registry.py add --file <row.json>`. Fix until it prints `OK added <id>`.
7. Run the check once by hand if possible (curl for L, read run history for S/E, a read-only API call for R/A). Show Martin the result.
8. Send ONE test alert and prove it was delivered: `python3 scripts/alert.py send --severity <SEV> --client "<name>" --what "Test" --since "<now>" --impact "kein echter Ausfall" --fix "keine Aktion, nur Test" --check-id <id> --no-wait`. Paste the `sent ...` line to Martin and ask him to confirm he saw it in Telegram.
9. Write `00_project/assets/<client-slug>/canary/<date>/_run.json` (fields: client, workflow=canary, status, mode, last_run, result, note) so the workflow registry picks it up on the next `sync`.

## Mode B — Handle an alert ("canary alarm X", or an alert payload/forwarded error)
1. Find the check in `canaries.json` (`scripts/registry.py list --client "<name>"`). Read its runbook section in `references/runbooks.md`.
2. Re-check the signal before acting (R6.2/R6.4) — a stale or single failed read is not an incident.
3. Diagnose read-only: run history, error text, last good time, who/what is affected, since when.
4. If a fix applies, check it first: `python3 scripts/allowlist.py check <action-id>`.
   - Not allowed → skip straight to escalation (step 6).
   - Allowed, no go needed → do it once, then verify with the external check (not the fix call's own success).
   - Allowed, needs go → ask Martin on one card (what broke, since when, impact, proposed fix); on yes, do it once and verify.
5. If the fix worked (external check confirms): log the incident (step 7) and tell Martin it's resolved, with the evidence.
6. If it didn't work, isn't allowed, or there is no fix: escalate. `python3 scripts/alert.py send --severity SEV1 ...` pages Martin first; if he doesn't ack within `--escalate-after-min` (default 10), it auto-posts the same information to the "741 Canary" Telegram group with @Dinakar and exits 4 (`ESCALATED`). Exit 3 (`NO_ACK`) means no escalation target was configured or `--no-escalate` was passed — that should not happen in normal use.
7. Write the incident: copy `assets/incident-log.template.md` to `00_project/canary/incidents/<date>-<check-id>.md`, fill in detect/alert/ack/restore times and whether the 1-hour goal held.
8. Post-incident: propose one new or changed check ("every outage becomes a canary") — a new row via Mode A, or a note on why the existing check didn't catch it sooner.

## Mode C — Daily status ("canary status", or the 06:13 morning grill)
1. `python3 scripts/registry.py list` for all checks; `python3 scripts/registry.py list --status planned` for gaps.
2. Read `00_project/canary/incidents/` for anything from the last 24h not yet reviewed.
3. Report (short, STE): checks live vs planned per client, any open incident, any client lead-path system with no canary at all (coverage gap), any blocker without an owner older than 1 hour.
4. This feeds Morning Grill's S8 slot (currently a placeholder in `scan.py`) — when wiring that in, read `00_project/morning-grill-skill/scan.py` first and extend S8 rather than duplicating the grill's own card/ledger logic.

## Verification (always last)
`python3 scripts/verify.py` must print `ALL CHECKS PASSED` before you report anything as done. Fix failures, re-run, never report "done" on a FAIL line.

## Open items (not yet built — tell Martin when they become relevant)
- Tally + Pipedrive read-only API keys for reconciliation (decision C10) — message drafted at `00_project/assets/marcel/canary/msg-marcel-read-keys.txt`, waiting on Marcel.
- 741-agents-01 (the night-shift Hetzner server) now exists. Its own heartbeat check is designed (`741-server-heartbeat`, decision C17, Healthchecks.io) but BLOCKED on Martin creating the Healthchecks.io account — nobody but Martin may create that account.
- Escalation group ("741 Canary", chat id in `.secrets/canary-telegram.env` TELEGRAM_CHAT_ID_GROUP) and Dinakar's handle are live and tested (auto-escalation on no-ack, exit code 4). If Dinakar ever needs to be swapped or a second backup added, update TELEGRAM_DINAKAR_HANDLE and the group membership, not the script.
