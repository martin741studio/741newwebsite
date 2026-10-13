# Self-heal allow-list

One attempt only, per incident. Verify every fix with the external check (the monitor result), never with the fix call's own 200 OK. Anything not on this list is NOT self-heal: escalate with a decision card instead.

`scripts/allowlist.py check <action-id>` reads this file and returns OK or FAIL. Add an action here only after Martin approves it on a card; log the approval date.

## Allowed (no go needed — read-only or reversible-and-logged)
- `recheck` — run the failed check again (confirm before acting on one failure).
- `refresh-cache` — reload a cached list (e.g. Zapier's field cache) before giving up.
- `read-run-history` — read a Zap/scenario/workflow run log (read-only).
- `read-ads-status` — read Google Ads campaign/billing/policy status via a script or the UI (read-only, never `mutate`).

## Allowed with Martin's go (G2) — writes into a client system
- `zapier-replay` — replay failed Zap runs, but ONLY after the root cause is already fixed (else it just fails again and wastes tasks). Approved 2026-10-14 (C9/decisions.md), case: Marcel Gewinnspiel.
- `zapier-turn-on` — switch a Zap back on after Zapier auto-paused it and the cause is fixed.
- `restore-paused-db` — Supabase `restore_project` for a project paused on the free tier. Approved pattern: automation-workflow.md self-heal list.

## Never allowed (always escalate, no exceptions)
- Any Google Ads mutation (pause/resume campaign, change budget, edit bids, edit conversions) — hard limit, reasoned go only, never by the canary.
- Any website content/theme/plugin change.
- Any message to a client or their contact (email, WhatsApp, SMS) — canaries alert 741 only.
- Entering a password, API key or token into any field.
- Creating an account or signing in on a client's behalf.
- Deleting data of any kind.

## Log
- 2026-10-14: Martin approved `zapier-replay` and `zapier-turn-on` for Marcel's account in principle (decisions.md C9); not yet exercised live.
