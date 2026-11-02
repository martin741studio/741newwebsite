# Coverage map — agent-job-descriptions (1.4, 2026-11-03)

| Need from the brief | Existing 741 asset | Verdict |
|---|---|---|
| Approval gate on send/spend/delete/publish | `.claude/hooks/live_change_gate.py` + `go_marker.py` + `go_card.py` (FTP, Novamira writes, Porkbun, config files); memory rules for ads, DB writes, e-mail, website changes | REUSE. The job description names which never-lines the hook covers and which are card-enforced. No second gate. |
| A manager | Morning grill (06:13 cards, 17:00 evening log, `state/cards.json`, Command Center admin tab) | REUSE as the manager's inbox; the weekly review is one card per agent on the review day. |
| Weekly self-review with grade | none per agent (evening log is daily, per client) | BUILD: review mode of the skill + template + grade from outside. |
| Roster of agents | sessions list, scheduled tasks, registry — no joined view | BUILD: `roster.json` + `roster.md` from the derived roster. |
| Where a description is loaded | scheduled-task `SKILL.md` (only text a run sees); `.claude/rules/` with `paths:` (project); memory files via MEMORY.md (advisory); skills (on demand) | REUSE the mechanism; Martin picks the rung at CP1 (Q2). |
| Telemetry per run | registry `_run.json` per workflow; night shift `validate_night.py`; grill ledger | REUSE: the review reads these as evidence. |
| Slop / STE on artifacts | `slop_gate.py`, deslop scripts | REUSE. |
| Change control of the description | none | BUILD: agent writes proposals to its run record; only Martin's go edits the description. |
| Adjacent skills not to duplicate | `workflow-create` (builds skills), `canary` (outage checks), `night-shift-v2` (queue), `morning-grill` (cards) | Route into them; this skill writes descriptions and reviews, it does not run the agents. |
