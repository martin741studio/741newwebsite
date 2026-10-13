# Portal area B: outreach numbers per account

Status 13.10.2026: design ready. No change applied to the database or to the live portal. Martin's go is necessary.

## Problem

`daily_reports` holds one row per person per day. The row mixes several LinkedIn accounts (Peggy/Bali Healing, Celine, 741 seats). There is no "accepted" field. For the Bali Healing status on 13.10., the counts came from the client CRM sheet.

## Decisions (Martin, 13.10.2026)

| Topic | Decision |
|---|---|
| Structure | Account list + one child row per account per report |
| Accepted | Daily count per account, entered in the evening |
| List owner | Gayo in the portal (Martin can also edit) |
| Old total fields | Auto-sum from the account rows |
| Fields per account | requests_sent, accepted, pitched, follow_ups, replies, interested |
| Morning plan | Targets per account (requests, messages) |
| Start list | Martin Hüwel, Coralie (Praxis Suriya), Felix Meinhardt, Peggy (Bali Healing), Celine, 741 Main/Second/Third |

## Schema ([migration.sql](migration.sql))

- `outreach_accounts`: label, client_label (free text), kind (client/741), active, sort. No FK to `clients`, so area B gets no path into area A.
- `outreach_account_members`: which person works which account.
- `daily_report_accounts`: report_id (cascade delete), account_id, 6 numbers.
- `daily_plan_accounts`: plan_id (cascade delete), account_id, requests_target, messages_target.
- Trigger `sync_report_totals`: fills `messages_sent` (= pitched + follow_ups), `follow_ups`, `new_replies`, `interested` and `connection_requests` ({account label: requests}). Board, history and `team_period` keep working without a change.
- RPCs `submit_daily_report` and `submit_daily_plan`: save the report or plan and its account rows in one call. They run as the caller, so RLS decides.
- RPC `team_period_accounts(from, to)`: manager only. One row per account with sums, accept rate, reply rate and people.

RLS stays the same: manager (Gayo, admin) sees all. Staff see and write only their own rows and only on the accounts that Gayo assigns to them.

## Test (13.10.2026, in a transaction that rolled back)

All 14 checks passed. The database had no trace after the test.

- Rias sees only her 2 assigned accounts.
- Report with 2 accounts: totals 25 messages, 3 replies, 1 interested, connection_requests {"Peggy LinkedIn": 40, "Celine LinkedIn": 20}.
- Update of one account row: messages total changes from 25 to 33.
- Rias writes on an account she does not have: blocked by RLS.
- Rias calls `team_period_accounts`: blocked ("team manager only").
- Rias adds an account: blocked by RLS.
- Rias and Gayo read `clients`: 0 rows.
- Plan with targets: `targets` = {"messages": 15, "connections": {"Peggy LinkedIn": 40}}.
- Gayo period: Peggy 40 sent, 9 accepted (22.5 %), 20 pitched. Celine 20 sent, 4 accepted (20 %).
- "Change" button (report delete): child rows go with it.

## Mockup

https://clients.741.studio/staging/outreach-accounts/ (static page, example numbers, nothing saves). Source: [mockup/index.html](mockup/index.html). Screenshots: [screenshots/](screenshots/).

The shared file `clients.741.studio/staging/index.html` is not touched. It holds other sessions' staging work.

## Rollout after Martin's go

1. Apply `migration.sql` (one migration).
2. Pull the live portal fresh, back it up to `clients.741.studio/backup/`.
3. Patch the team area in `index.html`:
   - `renderMyDay`: load `outreach_accounts` (RLS gives the assigned ones). Show the plan and report cards per account as in the mockup. Show the work card per account.
   - `saveDailyPlan` / `saveDailyReport`: call `submit_daily_plan` / `submit_daily_report`.
   - `renderPeriod`: add the per-account table and the "Status line" button below the person view (`team_period_accounts`).
   - New manager card "LinkedIn accounts" (add, edit, deactivate, assign people).
   - Fallback: a person with no assigned account sees the old form, so nobody is blocked on day one.
4. `node --check`, upload to staging, test as Rias and as Gayo, then live after Martin's go.
5. Send [gayo-brief.md](gayo-brief.md) to Gayo.

Old reports stay as they are. There is no backfill: the seat names "Main/Second/Third LinkedIn" do not tell which client account they were.
