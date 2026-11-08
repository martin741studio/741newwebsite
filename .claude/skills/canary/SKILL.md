---
name: canary
description: Runs the 741 canary (outage watch): adds a check for a client system (website, form/funnel, Zapier/Make/n8n, Google Ads), handles a canary alert (diagnose, one safe self-heal, escalate), gives the daily status for the morning grill. Use on "canary", "set up a canary for <client>", "überwache <system>", "sag mir sofort wenn <X> ausfällt", "canary alarm", "was ist down". Read-only; not for building the automation.
disable-model-invocation: false
allowed-tools: Read, Glob, Grep, Bash(python3:*), Bash(curl:*)
---

# Canary (Ausfall-Wächter)

## Critical

- This skill triggers on natural language because an outage report needs a fast response. That is safe only because every write is gated below. Never loosen those gates to compensate for easier triggering.
- Canaries read and alert. They never change a client's website, Google Ads (budget, bids, campaigns, conversions), or send a message to a client. Any write into a client system (Zapier replay, re-enabling a Zap, creating a tag) needs `allowlist.py check <action>` to say "needs Martin's go" AND Martin's go on that specific incident.
- Never type a password, API key or token into any field. Credentials come from Martin (or his go to another session), saved by a script into a 600-mode file under `.secrets/`.
- A failed read is "unreadable", never "down" and never "ok" (R6.2). Do not alert on one failed check: confirm with a 2nd check or a 2nd location first.
- SEV1 (a live client's lead path is broken right now) pages Martin 24/7. Everything else waits for the morning grill, unless Martin's card for that client said otherwise.

Design, decisions (C1–C13) and the hand-run proof on Marcel Rosenbach's real outage: `00_project/workflow-builds/canary/`. Read `decisions.md` before changing escalation, channel or runner choices. They are Martin's calls.

## Mode A: add a canary ("set up a canary for X")
1. Read the client's lead path from memory and the client chat (page → form → automation → CRM/ESP → Ads).
2. Pick checks from `references/check-catalogue.md` (types L/S/E/R/A). Prefer E (platform push) over polling when offered.
3. Draft a row per check matching the schema in `00_project/canary/canaries.json` (`_schema` key). SEV1 only for a live lead path.
4. Self-heal: an id from `references/allowlist.md`, or `self_heal: null` if nothing safe applies.
5. A check that creates something in a client account (a Zapier Manager Zap, an Ads script) needs Martin's go first: show the proposal, wait for the card. Zapier push build steps: `references/zapier-manager-setup.md`.
6. Save: write the row to a temp file, then `python3 scripts/registry.py add --file <row.json>` until it prints `OK added <id>`.
7. Run the check once by hand if possible (curl for L, run history for S/E, a read-only API call for R/A). Show Martin the result.
8. Send ONE test alert and prove delivery: `python3 scripts/alert.py send --severity <SEV> --client "<name>" --what "Test" --since "<now>" --impact "kein echter Ausfall" --fix "keine Aktion, nur Test" --check-id <id> --no-wait`. Paste the `sent ...` line and ask Martin to confirm he saw it in Telegram.
9. Write `00_project/assets/<client-slug>/canary/<date>/_run.json` (client, workflow=canary, status, mode, last_run, result, note) for the next registry `sync`.

## Mode B: handle an alert ("canary alarm X", alert payload, forwarded error)
1. Find the check (`scripts/registry.py list --client "<name>"`), read its runbook in `references/runbooks.md`.
2. Re-check the signal before acting (R6.2/R6.4). A stale or single failed read is not an incident.
3. Diagnose read-only: run history, error text, last good time, who is affected, since when.
4. If a fix applies, check it first: `python3 scripts/allowlist.py check <action-id>`.
   - Not allowed: escalate (step 6).
   - Allowed, no go needed: do it once, verify with the external check (not the fix call's own success).
   - Allowed, needs go: one card (what broke, since when, impact, proposed fix); on yes do it once and verify.
5. Fix worked (external check confirms): log the incident (step 7), tell Martin it is resolved with the evidence.
6. No fix, not allowed, or failed: escalate. `python3 scripts/alert.py send --severity SEV1 ...` pages Martin first. No ack within `--escalate-after-min` (default 10): it posts the same information to the "741 Canary" Telegram group with @Dinakar and exits 4 (`ESCALATED`). Exit 3 (`NO_ACK`) means no escalation target was configured or `--no-escalate` was passed; that should not happen in normal use.
7. Incident log: copy `assets/incident-log.template.md` to `00_project/canary/incidents/<date>-<check-id>.md`, fill in detect/alert/ack/restore times and whether the 1-hour goal held.
8. Post-incident: propose one new or changed check ("every outage becomes a canary") via Mode A, or a note why the existing check did not catch it sooner.

## Mode C: daily status ("canary status", or the 06:13 morning grill)
1. `python3 scripts/registry.py list`, and `python3 scripts/registry.py list --status planned` for gaps.
2. Read `00_project/canary/incidents/` for anything from the last 24 h not yet reviewed.
3. Report (short, STE): checks live vs planned per client, open incidents, client lead-path systems with no canary (coverage gap), blockers without an owner older than 1 hour.
4. This feeds the morning grill's S8 slot. When wiring it in, read `00_project/morning-grill-skill/scripts/scan.py` first and extend S8 rather than duplicating the grill's card/ledger logic.

## Verification
`python3 scripts/verify.py` must print `ALL CHECKS PASSED` before you report anything done. Never report "done" on a FAIL line.
