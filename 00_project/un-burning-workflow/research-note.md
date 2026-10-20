# Research note — Un-Burning workflow

Date: 2026-10-11. Language: STE. Step 1.5 of `00_project/workflow-creation-workflow.md`.

## Block chosen

Skill `un-burning` with `disable-model-invocation: true`. Shape: sequential workflow with gates (patterns.md 4.1) plus plan-validate-execute (4.4) for every change.
Reason: the job repeats per client, Martin triggers it, and it has side effects on client assets. A routine or project does not fit. Phase 1 may fan out read-only subagents per area (patterns.md 4.7). It stays under 10 agents, so no dynamic workflow.

## Three rules that shape the design

- R1.8: a destructive batch needs a plan file, a validator, the execution and a verification. The harm register is the plan file.
- R8.2 + memory `no-website-changes-without-go`: every live change needs Martin's "go". One go does not cover the next change.
- R8.3 + memory `claims-need-real-data`: every harm item has evidence, source, date and confidence. A guess is not allowed.

## One pattern

Writer / reviewer (patterns.md 4.6). A fresh subagent checks the kill list against the evidence before Martin sees it. It reports only correctness gaps.

## Reuse (what 741 already has)

- Audit workflow `00_project/audit-workflow-spec.md`: diagnosis input. Un-Burning does not repeat its checks.
- Citations module: Supabase `client_locations`, `client_citations`, `directories`; `reporting/citation-monitor.mjs`.
- GSC export: `scripts/gsc-client-export.mjs`. GA4 and GSC read through the service account.
- Skill `backlink-dach` for anchor and link work. Memory `page-swap-never-edit-live` for redirects and page changes.
- Suriya baseline: `BASELINE-REPORT.md` (see open questions: it exists only in worktree `admiring-nightingale-f0f882`).

## Open questions

See `design-note.md`, section 9.
