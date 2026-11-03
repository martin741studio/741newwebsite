# Sales Library — knowledge base of the 741 Sales Director agent

Built 2026-11-03 for the agent `sales-director` (description `00_project/agent-jobs/sales-director.md`). Freshness: external sources younger than 3 months, re-check after 6 weeks; next refresh due 2026-12-15. Internal library. Never name guru or vendor sources in anything that reaches a prospect or the team.

How to use:
1. `grep -ril <term> 00_project/knowledge/sales-library/` and read hits in this order: `_derived/` → `sources/04` (741's own files, always fresh) → extracts 20–22 → external notes 01–03 → the raw Hormozi files in `../hormozi-library/` only when a quote is needed.
2. Derived layer: `_derived/sales-director-rules.md` (S1–S6, 44 rules, one source each), `_derived/sales-director-questions.md` (5 open, 5 answered, 2 later).
3. The Hormozi library (`../hormozi-library/`, 120 sources) and the marketing playbook knowledge (`../hormozi-library/_derived/`, `../content-format-library/`, the 25.10. playbook) stay where they are; this library points at them and distils the sales part.

## Sources
| # | File | Type | What it gives |
|---|---|---|---|
| 01 | `sources/01-pipeline-hygiene-and-weekly-review.md` | external, 4 vendor guides 2026 | three questions, stale rule 1.5×, five questions per priority deal, coverage 3–5× |
| 02 | `sources/02-linkedin-outreach-benchmarks-2026.md` | external, 5 sources incl. one measured dataset | acceptance / reply / booked bands; acceptance is the expensive stage |
| 03 | `sources/03-managing-a-small-outreach-team.md` | external, 4 SDR guides | output = booked meetings, 1:1 shape, variance diagnosis, activities per meeting |
| 04 | `sources/04-741-own-sales-assets.md` | internal pointers | pricing, revenue model, Call-Raster, objections, prospect flow, CRM sheet, playbook, benchmarks, house rules |
| 20 | `sources/20-hormozi-closing-and-sales-extract.md` | extract of 8 Hormozi files | closing, discovery, proof, price review, hiring and paying salespeople |
| 21 | `sources/21-hormozi-leads-and-service-business-extract.md` | extract of 7 Hormozi files | outreach volume, follow-up, setter vs closer, referrals, retention |
| 22 | `sources/22-marketing-playbook-adapted-for-sales.md` | extract of 9 playbook and 741 files | how content and outreach feed sales, lead-magnet role of the review page, benchmark transfer, one CONFLICT in 741's own files |

Still to export: nothing required. Optional later: the Hormozi files not yet read for sales (038–041 "building a business for a stranger" episodes) and a German-market source on selling to practices (the search found only agency marketing pages).
