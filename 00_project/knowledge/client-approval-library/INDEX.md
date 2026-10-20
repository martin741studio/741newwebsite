# Client-Approval Library — Index

Built 2026-10-13 for the client-approval workflow (`00_project/client-approval-workflow/`). Freshness rule: sources published on or after 2026-07-13. Living help pages count as current on the fetch date (2026-10-13). Refresh before the next build if older than 6 weeks.

| Folder | Topic | Sources | Date range | Extract |
| --- | --- | --- | --- | --- |
| `01-approval-tools-ux/` | Approval / proofing tools and UX (Filestage, Ziflow, Figma, Markup.io, Pastel, Assembly …) | 16 | 2026-07-29 – 2026-10-06 + help pages 2026-10-13 | `extract.md`, 30 rules |
| `02-agency-client-process/` | How agencies involve clients | 14 | 2026-07-15 – 2026-10-12 | `extract.md`, 30 rules |
| `03-decision-psychology/` | Choice architecture, defaults, decision fatigue | 15 | 2026-07-15 – 2026-10-09 | `extract.md`, 30 rules |
| `04-gbp-seo-change-risks/` | GBP and website change risks, lock table | 16 | 2026-07-15 – 2026-10-08 + Google pages 2026-10-13 | `extract.md`, 30 risk rows + 20 rules |

## Known gaps
- No fresh source tests before/after text comparisons (03).
- No fresh source on approving images or branding in page context, German-market practice, or client photos (02).
- No tool documents auto-approval after a deadline; the 7-day rule is our own design (01).
- No fresh test on removing a keyword from a title or H1; the lock is an inference from tests that add keywords (04).
- No fresh data on bulk photo uploads, description keywords or edit frequency (04).
- Reddit threads were not readable with the tools (02).

## Search
`grep -ril "<term>" 00_project/knowledge/client-approval-library/` — read `extract.md` first, then the source file.
