---
name: acceptance-criteria
description: Builds an acceptance-criteria contract for one module, feature, page or tool before an agent team builds it - a short grill with Martin, online research of the current best-practice standard for that kind of module (OWASP, WCAG, Core Web Vitals, DSGVO/TDDDG, EU AI Act, HWG and others), measurable criteria with a test method and a source each, milestones, and a task split with file ownership per worker. Validates the contract with a script, freezes it on Martin's go, and at the end checks every criterion with evidence before the work counts as done. Use when Martin says "Akzeptanzkriterien für <X>", "acceptance criteria for <X>", "Vertrag für <Modul>", "was muss <X> können", "plan <X> for the team", "/acceptance-criteria", or when the team-orchestrator Task Manager starts a new build. Do NOT use for client body copy (content-writing), page structure (cro-homepage), or a one-line fix.
---

# Acceptance criteria contract (741)

Idea from the TokenMade podcast (Alexander Weipprecht, 2026-11-05, "Goal Engine"): a task is not "build a login". A task is a contract with measurable acceptance criteria from current best practice. The team builds against the contract. The work is done only when every must criterion passes with evidence.

## Critical

- Every criterion is measurable. It has a test method and at least one source. No "schnell", "sicher", "benutzerfreundlich" without a number or an observable result. The script rejects them.
- Research comes before writing. At least 3 sources, at least 1 primary standard or law. Record the URL and the date you checked it. Prefer the official text over blogs.
- Questions to Martin only as AskUserQuestion cards (max 4 per round). Check the source of truth first (repo, memory, Supabase). Do not ask what you can read.
- As a teammate (Task Manager) you cannot ask Martin. Send your questions to the lead (`main`) with SendMessage. The lead asks Martin with cards and sends the answers back.
- An approved contract is frozen. A change is a new version (`bump`). Never edit an approved file.
- Pareto rule: max 15 must criteria per milestone. A criterion that fails after 2 fix rounds goes to Martin (keep, lower to should, or change). No endless loops.
- Replies in STE. Delivered text goes through the slop check (CLAUDE.md).

## Steps

```bash
C=.claude/skills/acceptance-criteria/scripts/contract.py
python3 $C new <slug> "<Title>"          # creates 00_project/contracts/<slug>/contract-v001.json
```

1. **Intake grill.** Fill `context` in the contract. Ask only what is still open, as cards:
   - Who uses it? (only Martin / team / clients / public) - decides login, roles, rights.
   - What must be better after it is done than today? - decides the goal and the metrics.
   - How does the user reach it? (browser page, WordPress, CLI, API, mobile) - decides the module types.
   - Limits and out of scope? (budget, deadline, hosting, data that must stay in the EU, what we do NOT build).
2. **Module types.** Set `module_types` from `references/standards.md` (for example `auth`, `form`, `landing-page`, `api`, `tracking`, `ai-feature`). Each type lists the standards you must check.
3. **Research.** For each module type, search the current standard and 1-2 strong practice sources (firecrawl_search or WebSearch; fetch the page, do not trust a snippet). Check that the version is current (a newer ASVS, WCAG or law version replaces the old one). Add each source to `sources` with `id`, `title`, `url`, `type` (standard | law | vendor | guide), `checked`.
4. **Criteria.** Write each criterion in `criteria`:
   - `text`: Given / When / Then, or one clear sentence of the required behaviour.
   - `measure`: the number or the observable result (e.g. "LCP <= 2.5 s on mobile at p75", "6th wrong password within 15 min -> account locked 15 min").
   - `verify.method`: unit | e2e | command | review | manual, and `verify.how`: the exact test, command or check.
   - `category`: functional | security | privacy | performance | accessibility | legal | seo | ops.
   - `priority`: must | should | could. `sources`: source ids.
   Also think about the gaps that a plain request forgets (the login example: password reset, lockout after failed tries, session timeout, remember-me risk).
5. **Milestones.** Group the criteria into M1..Mn. Each milestone has an `exit` condition. M1 is the smallest version that works end to end.
6. **Validate.** `python3 $C validate <contract>`. Fix every error. Show the warnings to Martin.
7. **Review for Martin.** `python3 $C md <contract>` writes `contract-v001.md`. Show the summary (milestones, must count per category, open risks) and ask for the go with a card. On the go: `python3 $C approve <contract> "<Martin's words>"`.
8. **Task split.** Fill `tasks`: one task per coherent piece, with `owner` (worker1, worker2), `criteria` ids, `files` (paths or globs that only this owner may change), `depends_on`. Run `validate` again: it fails when a must criterion has no task or two owners share files. `python3 $C tasks <contract>` prints the list for the shared task list (TaskCreate).
9. **Acceptance.** When the workers report done, the Task Manager runs every `verify.how` and writes `results-v001.json` (`{"AC-001": {"result": "pass", "evidence": "test output / file / screenshot", "rounds": 1}}`). `python3 $C verdict <contract> <results>` prints the table. Done means: every must criterion passes with evidence. A fail with `rounds >= 2` goes to Martin.

## Files

- `00_project/contracts/<slug>/contract-v<NNN>.json` - the contract (source of truth)
- `00_project/contracts/<slug>/contract-v<NNN>.md` - human summary for Martin
- `00_project/contracts/<slug>/results-v<NNN>.json` - acceptance results with evidence
- `references/contract-template.json` - field reference with one filled example
- `references/standards.md` - module types and the standards to check for each

## Limits

- The script checks form, not truth. A criterion can be measurable and still wrong. The research step and Martin's review catch that.
- Legal criteria (DSGVO, HWG, BFSG, EU AI Act) state what the module must do. They are not legal advice. Flag open legal questions to Martin.
