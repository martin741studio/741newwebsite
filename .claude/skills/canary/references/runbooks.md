# Incident runbooks — read in incident mode (UC2) before acting

General order for every incident: re-check the signal → diagnose read-only → allow-listed fix (one attempt, verify with the external check) → else escalate with a decision card. Never act on one failed read; "unreadable" is not "down" and not "ok" — say so explicitly.

## Zap error (type E/S, Zapier)
1. Open the Zap Run Link from the alert. Read the failing step and the exact error text.
2. Common causes seen so far: a tag/field ID in the Zap does not exist in the target system (Marcel 2026-10-13: a KlickTipp "Label" was mistaken for a "Tag" — same mistake can recur), an expired OAuth connection, a changed form schema.
3. If the cause is a missing tag/field: this needs a write in the client's system (e.g. create the tag) → `allowlist.py check <action>` will say "needs Martin's go" or "not allowed" — act accordingly. Canaries don't create tags/fields themselves.
4. If the Zap is simply off and the cause is already fixed: `zapier-replay` (needs go) replays failed runs on the current published version, then `zapier-turn-on` if needed. Replay only AFTER the fix, never before — a replay on a broken Zap just fails again.
5. Verify: re-run the L/R check for the same client, confirm new runs succeed.

## Site or form not reachable (type L)
1. Re-check from a second path (different tool/IP) before trusting one failed read — matches the "2 consecutive or 2nd location" rule.
2. Read hosting status (cPanel, Wix, WordPress host) if accessible read-only.
3. No self-heal allowed for website content/config — always escalate with a card. Exception: `recheck` and `read-run-history` need no go.

## Reconciliation gap (type R)
1. Confirm the read itself is not the problem (expired token, rate limit) before reporting a real gap.
2. Identify which step of the chain lost the record (source has it, first system doesn't → that hop is broken).
3. This is usually SEV2, not a page — unless the gap means the current live lead path is broken right now (then SEV1).

## Ads anomaly (type A)
1. Read-only always. Never pause, resume, edit budget, edit bids, or touch conversions.
2. Present findings as a card: campaign, primary_status_reasons, what changed, proposed action (e.g. "top up balance" or "fix the disapproved ad text") — Martin or the client acts.

## Server / runner down (meta-monitoring, when it exists)
1. No outside watcher was set up at launch (decision C6) — the grill's "last canary run" age is the only signal until a server outage happens once.
2. On the first real server outage: revisit C6 with Martin (add a Healthchecks.io heartbeat, per the architecture research).
