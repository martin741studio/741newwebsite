---
name: content-writing
description: Write finished website copy for a 741 client or for 741.studio. New pages (homepage, service, location, practitioner, cost, FAQ) and blog posts, or a rewrite of an existing page. Builds a brief from the content pool, runs the A0 gate, writes an outline for Martin's go, drafts, runs scripted gates for facts, HWG/BRAO, SEO, style and AI slop (German tell list plus rival-model cleanse), has a fresh reviewer check it, and delivers a Markdown master with section IDs and CMS plain-text blocks. Use on "/content-write <client> <page or topic>", "schreib die Seite für …", "Blogbeitrag für …", "Text für die Ortsseite …", "Seitentext überarbeiten". Do NOT use for the content pool (content-pool), for auditing a page (seo-page-optimizer AUDIT), for the CRO prototype (cro-homepage), for prospect review pages (local-seo-review-page), or for social posts and emails.
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(python3:*), Bash(bash:*), Bash(ls:*), Bash(curl:*), Agent
---

# Content Writing (workflow id `copy`)

Spec: `00_project/content-writing-workflow.md`. Coverage map: `00_project/content-writing-coverage-map.md`. Replies and working files in STE. Client copy in normal prose.

## Critical

- **Real data only.** Every fact and number is in `01-brief/claims.json` with a source. Unknown client facts are yellow `[von Kunde bestätigen: …]` placeholders. Never guess.
- **Two checkpoints, no skipping.** Checkpoint 1 on the outline. Checkpoint 2 on the final copy. No page text before checkpoint 1 is approved.
- **Nothing goes live.** No upload to a site, CMS, portal or client without Martin's "go". Files stay local until checkpoint 2.
- **Gates are scripts.** Run `scripts/run_gates.py`. Fix until it passes. The slop gate needs the rival-model cleanse (`scripts/cleanse_de.sh`) and the claim diff. German copy is never checked with slopmonster's English linter alone.
- **No dashes** (— and –) in any copy. One address form (du or Sie). No method sources named in client text.

## Inputs (Martin gives)

Client, page or topic, page type, language, mode (new or rewrite), pool item ids if known. Ask once, in one line, if one is missing. Do not ask what the pool, the sitetree or the client folder already holds.

## Workflow

Copy this list into `00_project/assets/<client-slug>/content-writing/<page-slug>/_status.md` and tick it off.

- [ ] **Step 0 Readiness.** Read the client's Source-of-Truth sheet first (`scripts/read_sot.mjs`, all tabs; rule F11) and save the text snapshot. Do not mark address, phone, hours, team or title facts open before that. Check inputs and blockers (spec section 5). Create the run folder (spec section 4). Check pool age (30 days). Read the client's `_status.md`. Write `_run.json` (status "in Arbeit").
- [ ] **Step 1 Voice sheet.** Reuse `<client>/voice.md`. If missing, build it (`references/voice-rules.md`, template `content-writing-voice-template.md`). The live website is the source of the voice. Status stays "Entwurf" until Martin confirms the address form.
- [ ] **Step 2 Brief and gate A0.** Build `brief.json` (schema `content-writing-brief.schema.json`) and `claims.json` (`references/fact-rules.md`) from the pool items, sitetree node and voice sheet. Fill the A0 table (`references/seo-geo-rules.md` section 1): full for money pages, light for blog posts. Count words only with `scripts/wordcount.py`. Retry failed fetches across all SERP results. Read the client's whole live site on the topic, including the FAQ page and the person page, not only the target page: existing client FAQ and phrases are kept (fact-rules F8, copy-rules C9.2). A blocker stops the run with the escalation line.
- [ ] **Step 3 Outline.** Write `02-outline/outline.md`: section IDs and jobs from `references/page-templates.md`, up to 3 headline variants per section with one recommended, claim list with sources, placeholder list, word target. **CHECKPOINT 1: show Martin, wait for "go".** After 2 rounds without approval, stop and ask for a call.
- [ ] **Step 4 Draft.** Write `03-draft/draft-v1.md` in the page template (`content-writing-page-template.md` or `content-writing-blog-template.md`). Rules: `references/copy-rules.md`, `references/legal-rules.md`, `references/blog-rules.md` for posts. Write from the claim list. No claim outside it.
- [ ] **Step 5 Gates.** Run `python3 ~/.claude/skills/content-writing/scripts/run_gates.py <run_dir>`. The report has G1 to G6 (G6 = SEO/GEO coverage plus schema; it needs `_work/bench-metrics.json`, `brief.paa_questions`, `brief.nap_file`). Fix flagged lines until G1 to G4 and G6 pass; read the advisory hints of G6 and answer each with a fix or a reason. Then the slop loop (below).
- [ ] **Step 6 Fresh reviewer and SEO audit.** Also one fresh subagent applies the `seo-page-optimizer` rubric (8 dimensions, `references/scoring-rubric.md`) to the page in AUDIT mode with the benchmark data. Any dimension under 85 goes back to the writer.
- [ ] **Step 6 Fresh reviewer.** Spawn a subagent with brief, claims, draft and `content-writing-scorecard.md` only. It reports correctness gaps only. Fix. Re-run step 5. Maximum 2 rounds.
- [ ] **Step 7 Package.** Write `05-final/page.md`, `cms-blocks.txt` (`~/.claude/skills/content-writing/scripts/make_cms_blocks.py`), `placeholders.md`, scorecard, final gate report. Run `python3 ~/.claude/skills/content-writing/scripts/measure_plan.py <run_dir>` (30/60/90 day plan) and write `05-final/schema.jsonld` (`schema_tool.py make`). After several pages of one client exist: `python3 ~/.claude/skills/content-writing/scripts/link_network.py <content-writing-dir> --final` (G6c link network, similarity, keyword clashes). Update `_run.json`. If grey zones or conflicts remain, write `OPEN-FLAGS.md` in the run folder (legal grey zones, conflicts in client material, who decides), add `flags: see OPEN-FLAGS.md` to the page frontmatter and a FLAG comment above S01. The next agent reads it first.
- [ ] **CHECKPOINT 2: show Martin the summary and the copy, wait for "go".**
- [ ] **Step 8 Deliver.** Upload to Drive only after "go". Give the Drive link, the placeholder list and, if the copy goes to the client, a message draft in Ich-Form. After "freigegeben" run the registry `approve` command.

## Slop loop (gate G5)

1. `python3 ~/.claude/skills/content-writing/scripts/deslop_de.py <draft> --claims claims.json` (English text: the same script calls slopmonster's linter).
2. Rewrite the flagged lines in plainer words. Keep every claim.
3. `bash ~/.claude/skills/content-writing/scripts/cleanse_de.sh <draft> > cleansed.md 2> notes.txt` (GPT via codex, 180 s). Read `notes.txt`.
4. `python3 ~/.claude/skills/content-writing/scripts/diff_claims.py diff <draft> cleansed.md claims.json` must pass. A cleanse that adds a number, drops a claim, a placeholder or a section marker is rejected.
5. Lint again. Pass at 5/5. Maximum 2 rounds. Then stop and show Martin the open hits.
6. If `codex` is missing or fails: G5 does not pass. Offer the fresh-subagent cleanse, labeled "weaker, same model family". Martin decides.

Only the final draft goes to the cleanse. Never client source documents.

## Output

`05-final/page.md` (Markdown master with section IDs), `05-final/cms-blocks.txt` (plain text per section), `05-final/placeholders.md`, `04-gates/gates.md`, scorecard, `_run.json`. Templates are in `assets/`. Reader order: summary first (page, type, words against benchmark, gate table, placeholders, decisions needed), then copy by section.

## Registry

`_run.json` in the run folder: `{"client","workflow":"copy","status","mode","last_run","result","note"}`. Update at each checkpoint and at the end. Status values: "in Arbeit", "Trockenlauf", "fertig, Freigabe offen". The Stop hook syncs the Excel. Approval stays manual.

## Verification (end of every run)

Run `python3 ~/.claude/skills/content-writing/scripts/run_gates.py <run_dir>` and `tests/run_tests.sh` if a script changed. Report with evidence: gate table, word count line, score, screenshot for any HTML preview. Fix until it passes, then report.

## References (one level deep)

`references/copy-rules.md` · `seo-geo-rules.md` · `legal-rules.md` (+ `legal-terms.json`) · `fact-rules.md` · `page-templates.md` · `blog-rules.md` · `voice-rules.md` · `de-tells.md` (+ `de-tells.json`)

## Martin guide (2026-10-12)

The 741 character Martin points out the one thing per section the reader must not miss. Rules, poses, markup and the inline helper: `00_project/assets/brand/martin-guide/README.md`. In this workflow: NOT used on client page copy. Max 1 callout per section, bubble text in first person and plain language, every number with source and date, check desktop and mobile with a screenshot.
