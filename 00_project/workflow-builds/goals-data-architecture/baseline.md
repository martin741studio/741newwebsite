# Baseline — with vs. without this build (2026-10-15)

## Without (the status quo that caused this build)
- Taxi-Zentrale showed "active" in `morning-grill-goals.json` for a day after Martin ended the scope in memory and Supabase — caught only because Martin happened to notice it, with no detector in the loop. Zero tool calls catch this automatically; it takes a human re-reading the brief against their own memory.
- A verbal Suriya goal target never got written anywhere machine-readable — it lived only in a chat message until someone remembered to hand-edit the JSON file (or never did).
- Stürzl's address mismatch (Supabase `locations` vs. the Drive sheet vs. the live GBP profile) was invisible until this research session traced it by hand across 4 separate lookups (Supabase SQL, Drive MCP read, memory grep, cross-checking dates) — roughly 6 tool calls and real judgment to assemble, and it would not have been found without someone specifically going looking for it.

## With this build
- `generate_goals.py`: one script call, ~2 seconds, 0 corrections needed from Martin in the functional test. Automatically prevents the Taxi-Zentrale-style drift (status/phase are read fresh from Supabase every run, overlay-only fields are explicitly the hand-maintained surface) and the verbal-goal-target gap (`work_goals` is now the single write target, picked up on the next regeneration).
- `reconcile_drive.py`: one script call, ~3 seconds (one Sheets API read + a few Supabase REST reads), finds the Stürzl mismatch directly — the same finding that took ~6 manual tool calls to assemble by hand in the research phase now takes one command.
- Both scripts print warnings rather than silently fixing or silently passing — the one new "corrections needed" surface is Martin's card answers, not code debugging.

## Numbers
| | Without | With |
| --- | --- | --- |
| Tool calls to catch a stale portal-client status | 0 (relies on Martin noticing) | 1 script run, every grill run |
| Tool calls to catch a Drive-vs-Supabase NAP mismatch | ~6, manual, only when someone looks | 1 script run, weekly + on demand |
| Where a verbal goal number is written | sometimes nowhere | always Supabase `work_goals` (single target) |
| Manual JSON edits needed per grill run | unknown (ad hoc) | 0 for portal-client fields; overlay edits only for genuinely new facts Supabase can't model |
