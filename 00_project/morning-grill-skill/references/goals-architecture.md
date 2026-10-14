# Goal-sheet data architecture (goals-data-architecture, go 2026-10-15)

Full design: `00_project/workflow-builds/goals-data-architecture/{research-note,use-cases,test-scenarios,hand-run,pipeline}.md`. This file is the short operating reference for the grill run itself.

## The rule
`00_project/morning-grill-goals.json` is a **generated file**. Never hand-edit it.
- To change a goal number, status, or phase for a **portal client** (one with a Supabase `clients` row): edit Supabase (`work_goals` for numbers, `clients.status`/`work_phases` for status/phase — these are normally set by other workflows, not by hand here).
- To change anything else (aliases, chat id, client_rules, blockers, waiting_for, next_workflow, next_milestone, notes, or a non-portal entity like Taxi-Zentrale/Marcel/me&you/Tacheles/leads): edit `00_project/morning-grill-goals-overlay.json` by hand.

## Step 4 of the morning run
Before `scan.py` runs, regenerate the goal sheet:
```
python3 ~/.claude/skills/morning-grill/scripts/generate_goals.py
```
Read its output. A warning means something needs a decision (e.g. a Supabase client with no overlay row yet, or a client whose count dropped unexpectedly — the script refuses to write in that case). Every status/phase change it makes gets one line in `00_project/morning-grill-goals-archive-log.md` — that file is the archiving rule: it only ever raises a status (never silently downgrades), same as `workflow_registry.py`'s sync.

## Reconciliation (Phase C, weekly or on demand)
```
/Library/Frameworks/Python.framework/Versions/3.10/bin/python3 ~/.claude/skills/morning-grill/scripts/reconcile_drive.py [--client "Name"]
```
Needs the framework python (has `google-api-python-client`). Compares a client's Drive Source-of-Truth-Sheet NAP tab ("11 Citations & NAP") against Supabase `locations`, for clients listed in `assets/reconcile-sheets.json` (only STÜRZL Steuerstrafrecht has a sheet so far). It never picks a winner — every disagreement becomes a `judgment-cards.json` entry (same shape as any other grill card: both values, both dates, Martin decides, Claude writes only the side he names). Scope is NAP only for now; widen to other fields after this slice holds up over a few real weeks.

## Why this exists
Found twice in one day (13.–14.10.2026): Taxi-Zentrale showed "active" a day after the scope ended in memory and Supabase, and a verbal Suriya goal target never made it into the file. Traced live on 15.10.2026: STÜRZL Steuerstrafrecht's address was "Wiesenhüttenstraße 17" in Supabase `locations` (unchanged since 01.10) while the Drive sheet and the live Google Business Profile already said "Untermainkai 26" (moved 13.10 with Martin's go) — nobody had pushed the confirmed value back into Supabase.
