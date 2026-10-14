# 1.4 Coverage map — what 741 already has (2026-10-14)

| Asset | Path | Reuse |
|---|---|---|
| Reference hand-run (Martin's brief + result) | `00_project/prospects/korinna-heintze/whatsapp-sequence.md`, scheduled tasks `korinna-whatsapp-2-24h`, `korinna-whatsapp-3-15min` | template for file layout, message shape, reminder prompt |
| Review-page workflow v2.1 | `.claude/skills/local-seo-review-page/`, `00_project/prospect-mini-workflow.md` (steps 0-13) | where the prospect data lives; link the new skill after step 13 |
| Prospect data v2.1 | `00_project/prospects/<slug>/prospect.json`, `demand.md`, `site-findings.md`, `homepage.md`, `competitors.md`, `evidence/` | "old findings" baseline for "what is new" |
| Old review pages (v1, no prospect folder data) | `04_site/review/<slug>/index.html` only (e.g. korinna-heintze) | read the visible page text as baseline |
| DataForSEO wrapper with cap + ledger | `00_project/prospect-mini/scripts/dfs.py` (cap arg, `cost_ledger.jsonl`) | all paid calls |
| Site facts (free) | `00_project/prospect-mini/scripts/collect_site.py` | optional full re-check; the quick curl check is enough for one new insight |
| Proof cases | `00_project/prospect-mini/case-library.json` (5 cases with start/changes, `more` with jumps) | message 2 success story, facts only |
| German slop linter | `00_project/content-writing-skill/scripts/deslop_de.py --claims` | 5/5 gate per message |
| Scheduled tasks MCP | `mcp__scheduled-tasks__create_scheduled_task` (fireAt) | 2 reminders |
| Registry | `00_project/workflow-registry/workflow_registry.py add-workflow`; sync reads `00_project/prospects/**/_run.json` | BUT the prospect folder `_run.json` belongs to workflow `prospect` → booking runs write `prospects/<slug>/booking/_run.json` |

Memory rules that apply (feedback files):
- always-du-with-prospects, client-emails-ich-form (Ich-Form as Martin), deliver-messages-ready, message-format-copy-safe (```text block, • bullets), message-links-https.
- no-booking-link-in-messages (only the review link / no cal.com link), no-call-offers-to-clients (n/a: the call is booked).
- no-tool-names-in-client-messages (no DataForSEO, Local Falcon, BrightLocal …).
- claims-need-real-data, review-page-plain-language (no SoLV, H1, Schema, NAP without translation).
- hwg-fallstudien-guideline (health prospects: no healing promises; success stories as visibility results only).
- review-scan-show-the-gap / prospect workflow lesson: never claim the Google profile is "unclaimed" (Martin's brief).
- video-message-transcript-and-email-ask: never call it "Ablauf/Prozess/Workflow" in the message.
- email-sending-rules + no sending without Martin's go: the workflow sends nothing.
- always-external-chrome-browser: Chrome only if a browser is needed (not planned; curl is enough).

Gap: no skill exists for post-booking follow-up. Nothing to rework; build new, reuse the scripts above.
