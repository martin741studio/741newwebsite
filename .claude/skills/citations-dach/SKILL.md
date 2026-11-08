---
name: citations-dach
description: Audits and synchronizes local business directory citations across the 44 major DACH directories (Gelbe Seiten, DasÖrtliche, 11880, Apple Maps, Bing, Jameda). Reads canonical NAP from client_locations, checks live listings in client_citations, builds submission runbooks, imports BrightLocal orders. Trigger on "prüfe die Citations", "/citations-dach", "Verzeichnis-Abgleich", "Citations für <Kunde>". Not for editorial backlinks (backlink-dach).
disable-model-invocation: true
context: fork
allowed-tools: Read, Write, Edit, Bash(node:*)
---

# Citations DACH (`citations`)

Spec: `00_project/workflow-architecture.md` §4.1 · Registry ID: `citations` · Phase P4.

## Critical

1. **Canonical NAP.** Never change business name, address or primary phone. Use the locked values in `public.client_locations`.
2. **No paid spend without Go-B.** No BrightLocal packages without Martin's explicit Go-B.
3. **Primary phone only.** Never put a call-tracking number on a directory entry.
4. **Telemetry.** Every run writes `00_project/assets/<client>/citations/<YYYY-MM-DD>/_run.json` (sample: `references/run-json.md`).

## Steps

1. Read `public.client_locations` for `<client>` (name, street, postal code, city, phone, URL). Create the run folder `00_project/assets/<client>/citations/<YYYY-MM-DD>/`.
2. Audit: `node .claude/skills/citations-dach/scripts/citation-monitor.mjs --client <client_slug>`. Write counts `live` / `submitted` / `planned` to `<run_dir>/status.md`.
3. Group A (Google, Apple Maps, Bing, 11880, Das Örtliche): `node .claude/skills/citations-dach/scripts/submission-runbook.mjs --client <client_slug> --group A`.
4. BrightLocal order: prepare the CSV batch, show the cost, **wait for Go-B**. After processing: `node .claude/skills/citations-dach/scripts/import-brightlocal.mjs --client <client_slug> --file <csv_path>`.
5. Write `_run.json`. The Stop hook runs `workflow_registry.py sync`.

## Verification

`status.md` has the three counts, `_run.json` exists and is valid, `public.client_citations` shows the new crawl timestamps.
