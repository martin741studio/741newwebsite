# Incident <check-id> — <date>

- Client: <client>
- Check: <check-id> (<type>, <severity>)
- Detected: <ISO timestamp WITA> — how: <monitor/push that caught it>
- Alert sent: <ISO timestamp WITA>
- Acknowledged: <ISO timestamp WITA> by <who> (<seconds since alert>)
- Diagnosed: <what broke, since when, root cause>
- Self-heal tried: <action id from allowlist.md, or "none — not on the allow-list">
- Restored: <ISO timestamp WITA> — verified by: <which check, what it showed>
- Total outage: <minutes, detect-to-restore>
- Within 1-hour goal: <yes/no>

## What happened (plain)
<2-4 sentences, STE>

## Follow-up
- New or changed check: <id, or "none needed">
- Owner: <who>
- Done by: <date>
