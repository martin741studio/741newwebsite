# Client-Work Library — Index

Built 2026-10-13 for the client work view (`00_project/client-work-visibility/`). Freshness rule: sources published on or after 2026-07-13. Living help and API pages count as current on the fetch date (2026-10-13). Refresh before the next build if older than 6 weeks.

| Folder | Topic | Sources | Extract |
| --- | --- | --- | --- |
| `01-agency-task-delegation-ux/` | Task lists, ownership, delegation, "waiting on", client health in agency tools | 16 | `extract.md`, 30 rules |
| `02-ai-agent-work-visibility/` | Agents as doers, run logs, evidence, "needs review", "waiting on you" | 16 | `extract.md`, 30 rules |
| `03-work-data-model/` | Work-item schema, status machine, actor model, events, evidence, outcomes, RLS | 16 | `extract.md`, 30 rules + schema sketch |
| `04-dashboard-visualization/` | Admin portfolio view, client view, task display, proof, cadence | 16 | `extract.md`, 30 rules |

Related libraries (not duplicated): `ops-library/` (morning grill, approval queues, 23 sources), `client-approval-library/` (approval UX, 61 sources).
Own data inventory: `00_project/client-work-visibility/research/05-inventory-741.md`.

## Known gaps
- Most sources are vendor docs or vendor blogs. No independent client survey exists after 2026-07-13.
- No fresh NN/g, Baymard or Smashing dashboard research. No fresh mobile dashboard source.
- No DACH or health-sector source. No source covers one owner list that mixes people, agents and the client across many clients.
- No dated source after 2026-07-13 compares event sourcing with CRUD. No current source covers RACI or agency time and budget models.

## Search
`grep -ril "<term>" 00_project/knowledge/client-work-library/` — read `extract.md` first, then the source file.
