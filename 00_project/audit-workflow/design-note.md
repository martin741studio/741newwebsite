# Design note — `maps-audit` (checkpoint 1)

Process: `00_project/workflow-creation-workflow.md` section 2. Language: STE.
Spec: `00_project/audit-workflow-spec.md`. Data: `data-model.md`. Report: `report-wireframe.md`. Form: `interview-form-de.md`.

## 1. Use cases (rule R1.1)

| # | Trigger | Steps | Tools | Result |
| --- | --- | --- | --- | --- |
| UC1 Pre-sale call | `/maps-audit <prospect> call` | Resolve prospect and GBP. Read free data. Go-A. 1 keyword scan + 2 competitors. Score. Go-B | Falcon, DataForSEO (1 EUR), site script, form short set | One-page report for the call. Verdict Ja / Noch nicht / Nein |
| UC2 Kickoff | `/maps-audit <client> kickoff` | Form status. Free pulls (parallel subagents). Go-A. Paid pulls (5 keywords, 5 competitors, all platforms). Score. Reviewer check. Go-B. Client tab draft. Go-C | All tools in spec section 4 | Internal report, client-safe draft, action list, client message draft |
| UC3 Re-audit | `/maps-audit <client> reaudit` | Load last run. Reuse keywords, grid, radius. Ask only changed answers. Pull data blocks. Compare | Same as UC2 | Report with arrows per block and delta list |

## 2. Pipeline (patterns.md 4.1 + 4.4 + 4.6)

```
Intake ─► Phase 1 free pulls ─► GO-A ─► Phase 2 paid pulls ─► Phase 3 score ─► Review ─► GO-B ─► Client tab draft ─► GO-C
(slash)   (parallel readers)   (spend)  (Falcon, DFS, caps)   (score.py)       (fresh    (Martin   (client.html)      (release +
                                                                                 subagent)  reviews)                       message)
```

| Phase | What happens | Freedom (R1.7) | Check |
| --- | --- | --- | --- |
| Intake | Parse mode and subject. Find prior run. Load catalog. Create run folder | Low: script `init_run.py` | Run folder exists |
| 1 Free pulls | 5 read-only subagents: GBP and competitors (Falcon reads), website (script, PageSpeed, schema, index), off-page and reputation (autocomplete, Firecrawl, `client_citations`), analytics (GA4, GSC), form answers. Write JSON + evidence | High for judgment, low for formats (schemas) | `validate_run.py --phase 1` |
| Go-A | Show plan and cost. Wait | — | Martin's word |
| 2 Paid pulls | Falcon scans in sequence, never retry. DataForSEO volume and backlinks. Cost ledger. Stop at cap | Low: scripts `falcon_scan`, `dfs_pull` wrap MCP and API | Ledger under cap. Evidence hash set |
| 3 Score | Compute block scores, coverage, verdict, actions rank | Low: `score.py` reads catalog rules | Same input gives same score (determinism test) |
| Review | Fresh subagent checks findings against evidence. Reports only correctness gaps (R5.5) | High | Gap list. Fix, then re-run validator |
| Build | `build_report.py` writes internal and client HTML. `check_client.py` blocks tool names, team names, price, verdict | Low | Checks pass. Screenshot in Chrome |
| Go-B | Show internal report, validator output, screenshot. Count corrections | — | Martin's word |
| Go-C | Insert `client_reports` draft row. Show client message draft ("ich" form, no call offer) and Drive link | — | Martin's word |

Parallelism rule: subagents look (read). The main agent decides and writes the verdict. Subagents get the hard rules in their prompt (R9.6), because they do not read CLAUDE.md.

Intake question (added 2026-10-11): ask `--strategy maps|paid|balanced` before phase 1. See spec 5.2b.

## 3. Test scenarios (rule R1.2, written before the skill body)

The skill has `disable-model-invocation: true`. Only `/maps-audit` starts it. So "trigger" tests check what the skill does with different argument styles. Scenario 3 checks the scope guard.

| # | Input | Expected output |
| --- | --- | --- |
| T1 Obvious | `/maps-audit stuerzl kickoff` | Resolves client Stürzl. Mode kickoff. Creates run folder. Reads prior Falcon reports for free. Starts phase 1. Stops at Go-A with plan and cost. No scan before Go-A |
| T2 Paraphrase | `/maps-audit Stürzl nochmal komplett prüfen, wie letztes Mal` | Detects reaudit (a prior run or baseline exists). Reuses keywords, grid and radius of the prior run. States this in one line. Stops at Go-A |
| T3 Must not run | `/maps-audit Seite /steuerstrafrecht optimieren` | Detects a single-page content job. Does not start. Says in one line to use `seo-page-optimizer`. Creates no folder and spends nothing |
| T4 Cap guard | Kickoff with 12 keywords | Refuses over 5 keywords. Asks which 5. States the credit estimate |
| T5 Missing data | Kickoff where the form is empty | Runs the data blocks. Marks B01-B03, B08, B09 as "offen". Score coverage drops. Verdict shows "Offen". No guess |

## 4. Hand-solved real task (rule R1.3)

Real task: Stürzl, kickoff-style audit. Why Stürzl: two locations (Frankfurt, München), an address move on 05.10., law-firm advertising law, existing baseline and competitor data.
Dry run uses existing data first (free): baseline 01.10., Falcon campaign 09.10., competitor analysis 09.10., source-of-truth sheet. These sit in worktree `.claude/worktrees/unruffled-darwin-e68a19/`.
I note every piece of context I must supply by hand. That context becomes the skill body.
The dry run needs Martin's go for any new scan.

## 5. Skill plan (deliverable 6, after Go on this design)

```
~/.claude/skills/maps-audit/
  SKILL.md                    # Critical, Inputs, checklist, checkpoints (under 500 lines)
  scripts/init_run.py  falcon_scan.md (MCP recipe)  dfs_pull.py  site_check.py
         score.py  validate_run.py  build_report.py  check_client.py  load_run.py
  references/catalog.md       # copy of spec section 6 as machine table (audit_fields seed)
  references/rules-detail.md  # fit check, scoring, compliance profiles
  assets/report-internal.html assets/report-client.html assets/message-templates.md
```

Frontmatter: `name: maps-audit`. `disable-model-invocation: true`. `context: fork`. Narrow `allowed-tools`. Description with WHAT + WHEN + NOT (neighbour skills named).
Scorecard: I score the draft with `_derived/scorecard.md` (ship at 80 %, no zero in A or D). Install only after Martin's final go.

## 6. Build order after Go on this design

1. HTML prototype of page 1 and one block, rendered and checked in Chrome (screenshot).
2. Stürzl dry run on existing data. JSON only. No tables.
3. Skill draft + scorecard.
4. Memory file `maps-audit-workflow.md` + one line in `MEMORY.md`.
5. Ask Martin for the table go (`schema.draft.sql`) and the portal form build.
