# Functional test (2026-10-15) — the real task from 2.3, run by the built scripts instead of by hand

## Task A (goal-sheet generation), via `generate_goals.py`
Ran for real (not check-only), writing the live file:
```
WARNING: Johni Jaya Motor: overlay status_override='restart' overrides Supabase clients.status='active' (expected — Supabase has no matching state)
written /Users/martindrendel/741website/00_project/morning-grill-goals.json · 13 clients · 0 archive-log lines · 1 warnings
```
Verified against the hand-run (2.3):
- All 13 clients preserved (9 portal, matched by `supabase_name`/name; 4 non-portal, from the overlay). No client silently dropped.
- Every field the 7 consumer scripts read (`client`, `registry_name`, `status`, `grill`, `phase`, `program_start`, `program_end`, `quarter_goal`, `goal_numbers`, `leading`, `next_milestone`, `blockers`, `waiting_for`, `client_rules`, `chat`, `next_workflow`, `notes`, `aliases`) present on every client — checked programmatically, zero missing.
- Suriya's `goal_numbers` round-tripped through the backfilled `work_goals` rows exactly (baseline/target/due/source text all intact).
- Taxi-Zentrale status `done`, Johni status `restart` (via `status_override`, since Supabase has no such state) — both correct, matching what Martin actually decided, not what Supabase alone would say.
- Ran `scan.py`'s own `goal_gaps()` and `match_client()` functions against the generated file: `match_client("the dumann site")` → `Daniela Dumann` (alias match through the overlay, works); `match_client("taxi nuernberg issue")` → `Taxi-Zentrale Nürnberg` (non-portal overlay client, works); `goal_gaps()` correctly does NOT flag Dumann's agreed review goal as a gap (one real bug found and fixed during this test — see "where it stalled" below).

**Where it stalled / needed a fix (per R4.2 functional test purpose):** `work_goals.status` has a DB check constraint (`proposed`/`agreed`/`reached`/`dropped` only — no `confirmed`), but the existing `scan.py:goal_gaps()` checks `status != "confirmed"` to decide whether a goal number is still an open gap. Without a translation, every "agreed" goal (Dumann's Google-reviews target, which Martin already confirmed) would have shown up as a false gap. Fixed in `generate_goals.py` (`GOAL_STATUS_OUT` map: `agreed`/`reached` → `confirmed` on the way out). This is exactly the kind of context-gap R1.3 asks to extract from a hand task into the script — a human doing this by hand would have hit the same mismatch.

## Task B (reconciliation), via `reconcile_drive.py`
Ran for real against Stürzl (the only client with a Drive Source-of-Truth-Sheet so far): found the same disagreement as the hand trace in 2.3 (Supabase "Wiesenhüttenstraße 17" vs. Drive "Untermainkai 26"), using the live Google Sheets API instead of the Drive MCP's header-only snippets. One real fix needed here too: the framework Python (needed for `google-api-python-client`) had no CA bundle wired up (`SSL_CERT_VERIFY_FAILED`) — fixed by pointing `SSL_CERT_FILE` at `certifi`'s bundle inside the script, so it needs no manual environment setup at the call site.

## Verdict
Both scripts, run standalone, reproduce the hand-run results exactly, plus catch two real bugs (status-value mismatch, SSL bundle) that the hand-run did not surface because it used MCP tools and ad-hoc SQL rather than the actual code path the scheduled run will use. No corrections needed from Martin in this test; all fixes were caught by running the real thing, per R4.1 ("give Claude a way to verify its work").
