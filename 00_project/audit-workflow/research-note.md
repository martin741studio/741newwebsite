# Research note — Maps audit workflow (2026-10-11)

Process: `00_project/workflow-creation-workflow.md` section 1. Read-only research. No client asset changed.

## Building block (patterns.md section 3)

Choice: **Skill** `maps-audit`, `disable-model-invocation: true`, `context: fork`. It uses read-only subagents for the free data pulls and scripts for the fragile steps.
Reason: Martin starts it by hand (decision tree step 3). It spends Local Falcon credits and writes to a database, so it needs side-effect protection.
Not a routine yet. A scheduled re-audit can come later (rule R0.7).

## Rules used (rules.md)

- R1.2 / R1.3: test scenarios first, one hard real task (Stürzl) before the body.
- R1.7: scripts for scoring, validation and report build (fragile). Heuristics for findings text (open).
- R8.3 / claims-need-real-data: every finding has source, date and confidence. No guesses.

## Pattern

`patterns.md` 4.1 (sequential workflow with gates) plus 4.4 (plan-validate-execute for the paid pulls) plus 4.6 (fresh reviewer checks the run before Martin sees it).

## Reuse (do not rebuild)

- Playbook `00_project/local-seo-program-week1-playbook.md`: tool recipes, hard rules, detail benchmarks.
- Blueprint `00_project/gbp-visibility-blueprint.md`: target numbers for categories, services, keywords, AI prompts.
- Supabase 741-portal tables: `clients`, `client_locations`, `client_master_data` (has `boundaries`), `scans`, `visibility_prompts`, `visibility_results`, `client_reports`, `access_grants`, `client_citations`, `directories`.
- Sheet template "741 Client Requirement Sheets" (tab `02 Audit` becomes a generated view).
- Skills `local-seo-review-page`, `seo-page-optimizer`, `imagery-audit`, `backlink-dach` (sibling pattern: gates and scripts).
- Stürzl data: baseline 01.10., competitor analysis 09.10., Falcon campaign 09.10. They sit in worktree `.claude/worktrees/unruffled-darwin-e68a19/`.

## Facts that shape the design

- Falcon field `claimed` is unusable (false for all). Use `access_grants` and a browser read for ownership.
- Falcon radius differs between runs (5 km vs 5 mi). Runs are comparable only with equal parameters. The run stores them.
- Prospects are not in `clients`. The audit run needs a nullable `client_id`.
- Health clients use HWG. Law and tax clients use their own advertising law. The compliance check needs a niche profile.

## Open questions

See `00_project/audit-workflow-spec.md` section 12.
