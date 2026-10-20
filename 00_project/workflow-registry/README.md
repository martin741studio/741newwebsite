# Workflow registry: how the overview Excel stays current

Excel: `~/Desktop/Workflow-Uebersicht.xlsx`. Source of truth: `registry.json` (this folder) and `../cro-registry/registry.json`.

## What happens automatically (since 2026-10-11)

A Stop hook in `741website/.claude/settings.local.json` runs after every Claude turn in this repository:

```bash
/Library/Frameworks/Python.framework/Versions/3.10/bin/python3 00_project/workflow-registry/workflow_registry.py sync --quiet
```

`sync` scans `00_project/assets/` and `00_project/prospects/` and reads the files the workflows already write, updates the registry, and rebuilds the Excel when something changed. It takes about 0.3 seconds. It prints nothing and never fails a turn.

| Workflow | File that `sync` reads | Status rule |
| --- | --- | --- |
| Client Audit (`audit`) | `00_project/assets/audit/<client>/<run>/run.json` and `report/` | report files exist: fertig, Freigabe offen. Score and verdict go into the note |
| Un-Burning (`unburning`) | `00_project/assets/un-burning/<client>/<run>/run.json` | mode dryrun: Trockenlauf. Real run with `finished_at`: fertig, Freigabe offen |
| Maps Playbook (`phone`) | `.../matrix.json` (field `client`) | path has dryrun: Trockenlauf, else in Arbeit |
| Content Pool (`pool`) | `00_project/assets/<client>/content-pool/_status.md` | report html and Drive upload marker: fertig, Freigabe offen |
| CRO Track B (`cro_b`) | `00_project/assets/<client>/cro-b/_status.md` | line with "handoff": fertig, Freigabe offen |
| CRO Track A (`cro`) | `00_project/assets/<client>/cro/[<page>/]_status.md` | "Step 7 done": fertig, Freigabe offen. Pages in `cro-registry` stay manual |
| Prospect Review-Page (`prospect`) | `00_project/prospects/<slug>/_run.json` (written by `validate.py`) | as written in the file |
| any new workflow | `_run.json` in the run folder (schema below) | as written in the file |
| Citations, Backlink | no run folder (Supabase, Google Sheet) | manual `upsert` only |

Rules `sync` follows:
- It only raises a status (in Arbeit, then fertig, Freigabe offen). It never lowers one.
- It never changes an approved run (`freigegeben`) or an archived run.
- A run marked Trockenlauf stays a test until a real run is detected.
- It creates a missing run, a missing client (type Lead, note "bitte prüfen") and a missing workflow automatically.
- Approval stays manual on purpose: Martin says "freigegeben", then `approve` runs (UserPromptSubmit hook reminds).
- The Excel must be closed and reopened in Excel to show new data (the file is replaced, not edited live).

## `_run.json` (for every new workflow, no code change needed)

Put one file in the run folder and update it at each checkpoint and at the end:

```json
{"client": "Name as in the Excel", "workflow": "<workflow id>", "status": "in Arbeit | Trockenlauf | fertig, Freigabe offen",
 "mode": "Echt | Trockenlauf", "last_run": "YYYY-MM-DD", "result": "path or link to the main result",
 "drive": "Drive folder link", "note": "one line"}
```

## Commands

```bash
PY=/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
$PY 00_project/workflow-registry/workflow_registry.py sync          # show what changed
$PY 00_project/workflow-registry/workflow_registry.py list
$PY 00_project/workflow-registry/workflow_registry.py approve --client "<Name>" --workflow <id>
$PY 00_project/workflow-registry/workflow_registry.py add-workflow --workflow <id> --name "Label"
```

Backup of the state before the sync was added: scratchpad `backup-registry` of the session of 2026-10-11.
