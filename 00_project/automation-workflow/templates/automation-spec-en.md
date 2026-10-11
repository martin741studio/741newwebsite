# Automation spec: <client> · <automation name>

Date: <YYYY-MM-DD> · Run folder: `00_project/assets/<client>/automation/<slug>/` · Status: draft, waits for `go spec`

## 1. Goal

<One sentence: what happens automatically, for whom, with what result.>

## 2. Trigger

| Field | Value |
|---|---|
| System | |
| Event | |
| Type | polling / webhook / schedule (time zone!) |
| Account / ID | <logged-in account, group URL, account ID> |

## 3. Systems and accounts (from the inventory, all IDs checked)

| System | Account (as shown) | Object IDs | Access through | Read only? |
|---|---|---|---|---|

## 4. Field map

| Source field | Target system | Target field | Format / transform | Required | If empty |
|---|---|---|---|---|---|

## 5. Flow step by step

1. <step> → expected result → how we read it back

## 6. Error paths

| Error | Detection | Reaction | Alert to |
|---|---|---|---|
| Required field empty | | | martin@741.studio |
| Bad format | | | |
| Auth expired | | | |
| Target down | | | |
| Duplicate trigger | | dedupe on <key> | |

## 7. Actions that need approval

| ID (later) | Class | Action | Who is affected | Rollback |
|---|---|---|---|---|
| | G | | | |
| | M (Martin) | | | |

## 8. Test environment

- TEST record: name contains `TEST-741`, email <test…@741.studio>
- Flow stays draft / off until go
- Test settings to reset before go-live: <…>

## 9. Tests (flow_class: messages / crm / internal)

- [ ] e2e with TEST record, every field read back in every target
- [ ] error paths (mandatory for messages / crm)
- [ ] run twice, no duplicates (mandatory for messages / crm)
- [ ] alert test (mandatory for messages / crm)

## 10. Operation after go-live

- Owner: 741 (monitoring in the retainer)
- Alerts: platform error alert + daily reconciliation <source count vs. target count>
- Emergency rollback: <one sentence>

## 11. Open points (only what nobody can answer from docs or systems)
