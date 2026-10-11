# Rollback plan: <client> · <automation>

Written before checkpoint B. Every step names who does it, how long it takes, and how we prove it worked.

## Stop the damage (target: under 5 minutes)

| Step | Who | How | Proof |
|---|---|---|---|
| 1 | agent after go / Martin | <Zap OFF / campaign inactive / `live_send_enabled=false` / `launchctl unload`> | readback shows off |
| 2 | | <stop queued mails or sequence for affected contacts> | |

## Restore the state

| Object | Snapshot file | Restore method | Class |
|---|---|---|---|
| <Zap version> | `snapshots/<…>.json` | Zapier version history → restore v<n> | G |
| <KlickTipp campaign> | `snapshots/<…>.png` | | G |
| <records created by mistake> | `changelog.md` lines | Martin deletes (list IDs) | M |

## Tell people

- Martin decides if and how the client hears about it. Draft in Ich-Form.
- Never message the client's contacts without Martin's go.

## Known risks of the rollback itself

- <for example: a tag removal does not stop mails already sent>
