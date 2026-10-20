# Content Writing Workflow (workflow id `copy`, skill `content-writing`)

Status: design v1, **design go from Martin 2026-10-11 (checkpoint 1)**. Build done: templates, scripts, skill draft, dry run. **Installed 2026-10-11** (`~/.claude/skills/content-writing/`). Date: 2026-10-11. Owner: Martin.
Coverage map: `00_project/content-writing-coverage-map.md`. Skill draft (later): `00_project/content-writing-skill/`. Not installed.

**Contents**
0. Purpose and done criteria · 1. Decisions from the grilling · 2. Scope and trigger · 3. Interfaces · 4. Storage · 5. Inputs and blockers · 6. Steps and checkpoints · 7. Rules · 8. Slop gate · 9. Review loop · 10. Output formats · 11. Page scorecard · 12. Cost caps · 13. Hard rules · 14. Use cases and test scenarios · 15. Dry run · 16. Interface to CRO Step 3 · 17. Registry · 18. Open questions

---

## 0. Purpose and done criteria

The workflow writes finished website copy for 741 clients and for 741.studio. It writes new pages and blog posts. It also rewrites an existing page when the Bestand (current live text) exists. The copy must convert, rank, sound human, and contain only true facts.

The content pool decides WHAT goes on a page. This workflow decides HOW it is written.

**Done (all must be true):**
1. The brief passed the pre-flight gate (section 6, step 2).
2. Martin approved the outline (checkpoint 1) and the final copy (checkpoint 2).
3. All scripted gates passed: facts, legal, SEO, style, slop (5/5 after the cleanse).
4. The page scorecard is at 85 or more, with no blocking zero.
5. The output files exist: Markdown master with section IDs, CMS plain-text blocks, gate report, `_run.json`.
6. Every open client fact is a yellow `[von Kunde bestätigen]` marker and sits in the placeholder list.
7. The Drive link and a client message draft (Ich-Form) are ready, if the copy goes to the client.

## 1. Decisions from the grilling (Martin, 2026-10-11)

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Copywriting source | "Our copywriting skill" = headline prompts (`00_project/prompts/direct-response-copy-prompts.md`) plus CRO copy rules (R2, R3, R4, L-rules). The workflow merges them into one rule page. |
| 2 | Page types | Startseite, service and location pages, about, cost and FAQ pages, blog posts. |
| 3 | Sites and languages | DACH client sites in German. English client sites. 741.studio in German and English. |
| 4 | Slop gate | New German tell list. Rival cleanse (GPT via codex) on the final copy. Then re-lint. |
| 5 | Voice capture | Live site text, Google reviews, 5 voice questions in the client form. Voice sheet in the client folder. |
| 6 | Blockers | Block on core data. Client facts become yellow placeholders. |
| 7 | Checkpoints | Outline, then final copy. |
| 8 | Output | Markdown master with section IDs. CMS plain-text blocks. |
| 9 | Blog topics | Pool items plus demand data. Martin approves a ranked list. |
| 10 | Blog author | The practitioner or lawyer, first person. The client reviews before publish. |
| 11 | Blog gate | Lighter A0. Money pages keep the full A0. |
| 12 | Slop limit | 5/5 after the cleanse. Maximum 2 rewrite rounds. Then stop and show Martin. |
| 13 | Reviewer | Fresh Claude subagent, then Martin. |
| 14 | Dry run | Stürzl, one service page. Local files only. |
| 15 | Trigger | `/content-write <client> <page or topic>` |
| 16 | Success | Few change requests per page (target 2 rounds or fewer). Scorecard and slop score. |
| 17 | Dash rule | No dashes (— and –) in any copy. Gate checks by script. |
| 18 | Batch | Version 1 writes one page per run. Batch later as a loop of single runs. |
| 19 | 741.studio voice | Decide later. Own site stays out of the dry run. |

## 2. Scope and trigger

Trigger: `/content-write <client> <page or topic>`. Also triggers on "schreib die Seite für …", "Blogbeitrag für …", "Text für die Ortsseite …".

Do NOT use it for: the content pool (`/content-pool`), auditing an existing page (`seo-page-optimizer` AUDIT), the CRO prototype (`cro-homepage`), a review page for a prospect (`local-seo-review-page`), social posts, emails.

Martin gives: client, page or topic, page type, language, mode (new, rewrite of Bestand), and optionally the pool item ids. The agent asks once, in one line, if a field is missing.

## 3. Interfaces

| Neighbour | Direction | What passes |
| --- | --- | --- |
| Content pool | in | Pool items for the page (`pool.json`), `pool-top.md`, sitetree node (`05-sitetree/sitetree.json`). Field map in coverage map section 5. Items with status `needs_client` stay draft. |
| Audit workflow | in | Conflicts and findings on the live page (for rewrite mode). Only read. |
| Un-Burning (D11 text scan) | in and out | Shares the legal word list. A banned claim found there can start a rewrite run. |
| CRO Step 3 | out (later) | CRO passes its brief. The workflow returns `copy.md` in the CRO format (section 16). Not applied now. |
| `seo-page-optimizer` | partly replaced | CREATE mode content spec is covered by steps 2 to 5. AUDIT mode stays there. |
| `behandler-seite` | partly replaced | Its structure and Person schema become the template for practitioner pages. The build and preview deploy stay there. |
| Registry | out | `_run.json` per run. Workflow id `copy`. |

## 4. Storage

Local: `00_project/assets/<client-slug>/content-writing/<page-slug>/`

```
_run.json                 registry record
_status.md                step log, next step
00-voice.md               link or copy of the client voice sheet
01-brief/brief.json       machine-readable brief
01-brief/brief.md         human brief (German)
01-brief/gate-a0.md       pre-flight table with sources and dates
02-outline/outline.md     checkpoint 1 file
03-draft/draft-v1.md      working draft
04-gates/                 reports: facts, legal, seo, style, slop, reviewer
05-final/page.md          Markdown master with section IDs
05-final/cms-blocks.txt   plain-text blocks per section
05-final/placeholders.md  open client facts
```

Voice sheet: `00_project/assets/<client-slug>/voice.md` (one per client, reused by every run).
Drive: `Local SEO/<Client>/Texte/<Seite>/` with the final files. Old versions go to `_archiv/`. Give Martin the Drive link at every delivery.

## 5. Inputs and blockers

**Brief fields** (template `content-writing-brief-template.md`, schema `content-writing-brief.schema.json`):
client, page type, language, address form (du or Sie), speaker (ich, wir, third person), legal mode (HWG, BRAO, none), pool item ids, primary keyword and cluster with volume and date, search intent, reader and question, CTA goal and channel, word range, section plan, proof assets, internal link targets, benchmark data, Bestand text (rewrite mode), byline (blog), forbidden words, voice sheet path.

**Blocks the run (stop and ask Martin in one line):**
- No pool item or keyword for the page. (Run the content pool first or give a keyword with data.)
- Money page without a verified benchmark after all retries (A0 point 1).
- No legal mode for a health or law client.
- No locked NAP for a local page.
- No voice sheet and no live text to build one.
- Rewrite mode without a readable Bestand.

**Becomes a yellow placeholder `[von Kunde bestätigen: …]` and goes to `placeholders.md`:**
prices, years of experience, credentials not yet proven, quotes, review counts without release, awards, team names, opening times not in the locked record.

## 6. Steps and checkpoints

Copy this list into `_status.md` and tick it off. The agent runs steps 0 to 2 and 4 to 7 without asking. It stops at a failed gate, at the cost cap, and at the two checkpoints.

- [ ] **Step 0 Readiness.** Check inputs and blockers. Create the folder. Read `_status.md` of the client. Test the pool age (not older than 30 days, else warn). Check the cap.
- [ ] **Step 1 Voice sheet.** Reuse `voice.md` if it exists. Else build it from the client's live website (Martin, 2026-10-11): home, about, FAQ, person page and service pages. Read Google reviews and the voice answers in the client form as side sources. Live-site words that break HWG or BRAO stay out of our copy and go to `OPEN-FLAGS.md`. Write `voice.md` (section 10.4). If voice answers are missing, add the 5 voice questions to the client form draft. The sheet is a draft until Martin confirms du or Sie.
- [ ] **Step 2 Brief and pre-flight gate A0.** Build `brief.json` from the pool, sitetree and voice sheet. Fill the A0 table (`page-content-qa-checklist.md` phase 0). Count words by script (`scripts/wordcount.py`). Full A0 for money pages. Light A0 for blog posts: top 5 SERP reads, 2 successful word counts, real PAA, all facts verified, word floor 70 % of the median. Every row needs a source and a date.
- [ ] **Step 3 Outline → CHECKPOINT 1.** Write `outline.md`: section IDs and order, the job of each section in one line, up to 3 headline variants per section (one recommended), the claim list with source for each claim, the placeholder list, the word target. Martin approves, or names the sections to revise. After 2 rounds without approval, stop and ask for a 20-minute call.
- [ ] **Step 4 Draft.** Write the full copy per section from the page template and the rule page. Write sentence by sentence from the claim list. No claim outside the list.
- [ ] **Step 5 Scripted gates (run `scripts/run_gates.py`).** G1 facts, G2 legal, G3 SEO, G4 style, G5 slop (section 8). Fix until all pass. A fix rewrites only the flagged lines.
- [ ] **Step 6 Fresh reviewer.** A subagent with no writing context gets brief, claim list, final draft and the scorecard. It reports correctness gaps only (rule R5.5). Fix the gaps. Re-run step 5.
- [ ] **Step 7 Package.** Write `05-final/page.md`, `cms-blocks.txt`, `placeholders.md`, the gate report and `_run.json`. Render a check (section 10.5).
- [ ] **CHECKPOINT 2: Martin reads the final copy and says "go".** Changes: only named sections are revised, then steps 5 and 6 run again on them.
- [ ] **Step 8 Deliver.** Upload to Drive. Give Martin the Drive link, the placeholder list and, if the copy goes to the client, a message draft in Ich-Form. Update `_run.json`. After "freigegeben": registry `approve` (the hook reminds).

Nothing goes to a live site, a CMS or a client without Martin's "go".

## 7. Rules

All rules live in the skill's `references/` (one level deep). Each rule is IF/THEN with the reason and the source file. The rule pages are:

1. `references/copy-rules.md`. The merged headline and body rules. Sources: DR-Prompts (hero headline = dream outcome + benefit + mechanism, sub-headline pain first, PAS body, pain headline mix, value-prop formula, CTA) and CRO R2, R3, R4. Conflict resolution: a time frame in a headline is allowed only for service facts (CRO R2.2), never for a healing time. Pain first. One primary CTA, with a reassurance line. Sentences of 15 words or fewer in scan blocks. At most 2 sentences per paragraph in scan blocks. Words the reader uses, taken from reviews (CRO R0.4). No dashes (— and –). No wordplay.
2. `references/seo-geo-rules.md`. From the money-page standard D and E and the SEO skill: one H1 with keyword (and city when local), title up to 60 characters, meta up to 155, direct-answer block of 2 to 4 sentences under the H1, definition box, FAQ from real PAA with FAQPage schema, named entities, internal links inside the visible body, local texture from a verified fact (not name-dropping), word count rule (never thinner than the Bestand, 70 % of the competitor median as the floor for money pages).
3. `references/legal-rules.md`. HWG mode, BRAO mode, with the word lists. Sources: `hwg-fallstudien-guideline`, CRO rule 10, pool flags. One list, used by the G2 script and by Un-Burning D11.
4. `references/fact-rules.md`. Claims-need-real-data, the placeholder format, the claim list format, the rule "a number in the text must exist in the data".
5. `references/page-templates.md`. One template per page type with section IDs: Startseite (CRO P0 10 rows), service page, location page, practitioner page (from `behandler-seite`), cost page, FAQ page, blog post. A page type without a proven pattern is marked "draft template, first use".
6. `references/blog-rules.md`. Topic list from the pool, intent match, structure (answer first, then depth), byline with credentials and review date, update date, link to the money page, CTA, client review before publish, medical or legal review note when the legal mode needs it.
7. `references/voice-rules.md`. Voice sheet fields, du or Sie, speaker, how to keep the client's own phrases, harmony rule for target groups ("Schwerpunkt nennen, dann genauso bist du hier richtig, wenn …").
8. `references/de-tells.md`. The German AI tell list for the slop gate (section 8).

Elements, not text columns: sections whose content is a list, a process or a comparison are marked with a content element (`check-list`, `el-grid`, `step-flow`, `stat-badge`, `table`), as in the money-page standard D2 and the memory "real website sections". The template says which element each section uses.

## 8. Slop gate (G5)

Finding: `deslop.py` of slopmonster has an English word list. A German test text full of tells scored 5/5. So the gate has two parts.

1. **German lint.** New script `scripts/deslop_de.py` (in our skill, slopmonster stays unchanged). It reads `references/de-tells.md`: vocabulary ("ganzheitlich", "nahtlos", "Reise", "eintauchen", "maßgeschneidert", "in der heutigen schnelllebigen Welt", "es ist wichtig zu beachten", …), constructions ("nicht nur …, sondern auch …", "es geht nicht um X, sondern um Y", "mehr als nur …"), rule of three, rhetorical question that answers itself, closing summary, Gedankenstrich, stacked hedges, invented proof (number plus noun without a source). Five groups, one point each, like the English tool. English copy uses the original `deslop.py` through the same wrapper.
2. **Loop.** Lint → rewrite flagged lines → cleanse with the rival model → lint again.
   - Cleanse: `cleanse.sh` with a German prompt variant (`prompts/cleanse-de.txt`): same three passes, German word list, keep every fact, length within 10 %, keep placeholders and HTML exactly, no new numbers.
   - The cleanse runs on the final copy only, once per round. The model is GPT-5.6 via `codex exec` (installed and logged in).
   - The re-lint also checks that every placeholder, number and legal marker of the claim list is still present (script `scripts/diff_claims.py`). A cleanse that drops a claim or adds a number fails.
   - Pass: 5/5. Maximum 2 rewrite rounds. After round 2 below 5/5: stop, show Martin the open hits.
   - If `codex` is missing or fails: the run does not pass G5. Fallback is a fresh Claude subagent cleanse, labeled "weaker, same family" in the report, and Martin decides.
3. **Privacy note.** The cleanse sends the draft text to OpenAI. Names, addresses and claim text are in it. Martin accepted this on 2026-10-11 for final copy. Client documents (not the draft) never go to the cleanse.
4. **Human read.** A lint pass does not mean the copy is good. The scorecard line "human read" (section 11) checks one specific number per claim, varied sentence length and one concrete detail from the client.

## 9. Review loop

- The fresh reviewer gets the brief, the claim list, the draft and `scorecard`. It has read-only tools. It reports gaps that affect correctness: untraced claim, legal hit, missed brief item, wrong du or Sie, hook that breaks the rules, section missing from the plan. It does not give style opinions.
- Max 2 reviewer rounds. After that Martin sees the open items.
- Martin's change requests at the checkpoints are counted in `_run.json` (`rounds`). Target: 2 or fewer per page.
- A repeated correction from Martin becomes a rule edit in `references/`, not a one-off (workflow-creation section 6).

## 10. Output formats

### 10.1 Markdown master `05-final/page.md`
Frontmatter: client, page, type, language, address form, keyword, URL slug, title, meta, H1, word count (by script), gate results, date. Then sections with IDs:

```
<!-- S01 hero | element: hero | cta: primary -->
## [H2 or H1 text]
Text …
<!-- /S01 -->
```

Notes for design sit in a comment line per section (`<!-- design: … -->`). Placeholders are `[von Kunde bestätigen: …]`. A technical block at the end (title, meta, schema JSON-LD, alt texts, internal links) is marked "für 741, nicht Teil des sichtbaren Textes".

### 10.2 CMS plain-text blocks `05-final/cms-blocks.txt`
One block per section, separated by a line `=== S01 | hero | headline ===`. Plain text only. No HTML, no Markdown. Fields are named like the CMS fields (Titel, Untertitel, Text, Button). Placeholders stay visible in square brackets.

### 10.3 Reader order
Martin first sees: the summary (page, type, word count against the benchmark, gate table, open placeholders, decisions needed), then the copy by section. The designer sees the section IDs and design notes. The developer sees the technical block.

### 10.4 Voice sheet `voice.md`
Fields: client, language, address form with proof (quote from the live site), speaker, tone in 5 words, own phrases to keep (with source), words to avoid, how the clients speak in reviews (3 quotes with source), target-group harmony line, example paragraph from the live site, status (draft or confirmed). Template: `content-writing-voice-template.md`.

### 10.5 Render check
For HTML previews of the copy (portal page, design check), open the page in Chrome and take a screenshot before it goes to Martin (memory "verify UI in rendered state"). Markdown output needs no render, but the length, the section order and the placeholders are checked by `scripts/validate_page.py`.

## 11. Page scorecard

Score 0 to 100. Pass: 85 or more and no blocking fail. Template: `content-writing-scorecard.md`.

| Block | Points | Checks |
| --- | --- | --- |
| Copy craft | 25 | Hook per rule page. Pain before solution. One primary CTA with reassurance. Objections answered. Scan format (short sentences and paragraphs). Elements instead of text columns. |
| SEO and GEO | 20 | One H1. Title and meta limits. Direct-answer block. FAQ from real PAA. Entities. Internal links in the body. Word count: not below the Bestand, at least 70 % of the median (money pages). |
| Facts | 20 | **Blocking.** Every claim traced to the claim list and the source. Numbers match the data. Open facts are placeholders. |
| Legal | 15 | **Blocking.** G2 script clean. Human review of grey areas listed. Mandatory notice box where the mode needs it. |
| Slop and style | 10 | **Blocking at under 5/5.** German or English lint 5/5. No dashes. Address form consistent. |
| Human read | 10 | Voice sheet matches. One concrete detail per section. Sentence length varies. Read by the reviewer. |

A blocking fail means no delivery, whatever the total.

## 11b. Gate G6: SEO and GEO coverage (added 2026-10-11)

Martin asked how the workflow assures that a page has all SEO and GEO parts. G6 was built, then checked against the 741 SEO library and 2025/2026 research. Result: hard checks only where the library and Google guidance support them (PAA answered, early answer block, information gain per Vertiefung block, own headings, no keyword stuffing, visible date on legal pages, visible credential, matching JSON-LD, no keyword clash, no near-duplicate own pages). Term, entity and statute coverage stay advisory. Full table with evidence: `content-writing-skill/references/seo-geo-rules.md` section 9. Scripts: `seo_coverage.py`, `schema_tool.py`, `link_network.py`, `measure_plan.py`. The CRO homepage workflow calls the same gates at its Step 3.

No gate can guarantee a ranking. What stays outside the page: Google Business Profile, off-site mentions and backlinks, speed and indexing, and the time a page needs (weeks to months). The measure plan covers 30, 60, 90, 180 and 365 days plus a monthly AI-answer prompt set.

## 12. Cost caps

| Item | Cap |
| --- | --- |
| Paid data per page (DataForSEO) | 1 USD. The pool already holds most data. A new pull is only for the A0 benchmark. |
| Rival cleanse | 3 calls per page (2 rounds plus 1 retry). 180 s timeout per call. |
| Subagents | 1 reviewer per round, 2 rounds. |
| Local Falcon | Not used. |

Spend is logged in `_status.md`. A cap breach stops the run.

## 13. Hard rules

1. Real data only. No guessed fact, price, volume, award or credential. Unknown client facts are yellow placeholders.
2. Never name method sources (Hormozi and others) in anything a client can see. The method is called "741 Content-Raster".
3. Health clients: HWG mode. No healing promise, no before/after, no fear wording. "kann", "Ziel", "unterstützen". Harmonious target-group sentences. Law clients: BRAO and UWG as in CRO rule 10.
4. One H1 per page. One address form per page and per client.
5. No dashes (— and –) in any copy.
6. Real website sections and elements. Never one long text column.
7. Never thinner than the Bestand. Never below 70 % of the competitor median on a money page.
8. Elementor and CMS fields get plain text. No HTML.
9. Nothing goes live, to a CMS or to a client without Martin's per-change "go". Rewrites never edit a live page in place (memory "page-swap").
10. The client is "ich" in client messages. No call offers to clients. No questions to the client that the data can answer.
11. Replies and working files in STE. Client copy in normal prose.
12. The cleanse sends text to OpenAI. Only the final draft goes, never client source documents.

## 14. Use cases and test scenarios (written before the skill body)

**Use cases**
1. New service page: "Schreib die Seite Selbstanzeige für Stürzl." Trigger → readiness → brief from the pool → A0 → outline → checkpoint 1 → draft → gates → reviewer → checkpoint 2 → files and Drive link.
2. Blog post: "Blogbeitrag zu Verjährung der Steuerhinterziehung für Stürzl." Same path with the light A0, byline of the lawyer, review note for the client.
3. Rewrite: "Überarbeite die Über-mich-Seite von Dumann." Bestand is an input. The new text is never thinner. Conflicts in the Bestand are listed.

**Scenarios**

| # | Type | Input | Expected |
| --- | --- | --- | --- |
| T1 | Obvious trigger | `/content-write stuerzl Selbstanzeige Leistungsseite` | Skill loads. Readiness table. Brief built from pool items. Stops at checkpoint 1 with an outline. No page text before the outline is approved. |
| T2 | Paraphrase | "Schreib mir bitte den Blogartikel zur Verjährung bei Steuerhinterziehung für Anja Stürzl" | Skill loads, blog path, light A0, byline rule shown, topic checked against the pool list. |
| T3 | Paraphrase, health | "Ich brauche den Text für die Ortsseite Berlin-Mitte von Dumann, du-Form" | Skill loads, HWG mode, location rule (demand, catchment and local fact required). If one is missing: blocks with a one-line question. |
| T4 | Must NOT trigger | "Prüf die bestehende Seite von Hüwel gegen unseren SEO-Standard" | Skill does not load. `seo-page-optimizer` AUDIT does. |
| T5 | Must NOT trigger | "Content-Pool für einen neuen Kunden" / "CRO-Prototyp für die Startseite" | Skill does not load. `/content-pool` or `cro-homepage` does. |
| T6 | Gate test | Draft with "ganzheitlicher Ansatz", "nicht nur …, sondern …", a Gedankenstrich and "Schmerzen heilen" | G5 fails on tells, G4 on the dash, G2 on the healing promise. None passes. |
| T7 | Blocker test | Run for a client with no pool item and no keyword | Run stops in step 0 with one line, no copy. |

## 15. Dry run

Page: Stürzl, Selbstanzeige (Säulenseite, sitetree node ST-14, status Überarbeiten, so the Bestand check is tested). Mode: rewrite of an existing page, BRAO. Pool: `00_project/assets/stuerzl/content-pool/04-pool/pool.json`. Voice: Sie, ruhig, sachlich (from the approved homepage brief). Output only to `00_project/assets/stuerzl/content-writing/selbstanzeige/`. No upload, no CMS write. Martin can name another node (for example ST-18 Akutseite, new).

Pass criteria: all gates green, scorecard 85 or more, G5 at 5/5 with the German tells list proven by test T6, claim diff clean after the cleanse, reviewer report with no open correctness gap.

## 16. Interface to CRO Step 3 (proposal only, CRO file unchanged)

| CRO Step 3 element | Writing workflow field |
| --- | --- |
| Brief block (`copy.md` top) | `brief.json` fields: conversion goal, visitors, objections, proof, local, keywords, section order, voice, "Nicht" list |
| 10 section plan (Step 2 coverage check) | `section plan` with IDs `S01 … S10` (P0 template) |
| Pool input `pool-top.md` | `pool item ids` |
| Headline prompt file | `references/copy-rules.md` |
| HWG check | G2 report |
| `copy.md` with 3 headline variants, body, CTA, title, meta, H1 | `outline.md` (variants) and `page.md` (body) mapped to the same layout |
| Checkpoint 1 (copy and headlines) | Checkpoint 1 and 2 of this workflow, merged into one when called from CRO |
| `approved-copy.md` | `05-final/page.md` after "go" |

**Applied 2026-10-11 on Martin's request** ("make sure the SEO and GEO writing is in the CRO homepage workflow when it goes through the writing"): `cro-homepage-workflow.md` Step 3 has the block "SEO, GEO and writing gates". The skill `cro-homepage` has rule 3a, a run-kit line and a quality-gate line. `verify.py` checks `04-copy/gates.md` (Result PASS) for runs started on or after 2026-10-12. Steps 4 to 7 stay. Backups of the three CRO files from before the change: `/tmp/cro-*-backup-2026-10-11.*` (session scratch).

## 17. Registry

After the design go: `python3 00_project/workflow-registry/workflow_registry.py add-workflow --workflow copy --name "Content Writing"`. Each run writes `_run.json` at each checkpoint and at the end: client, workflow `copy`, status, mode, last_run, result (path or Drive link), note (page, rounds, score). Approval stays manual (`approve --client "<name>" --workflow copy`). Scorecard line F6.

## 18. Open questions

Resolved on 2026-10-11 (Martin): a portal review page is an optional third output, on request. The dry-run page is Stürzl ST-14 Selbstanzeige.

Still open:
1. Trigger tests T1 to T5, T7 and the baseline (need a fresh session; the skill is installed).
2. Martin's vetoes on the German tell list (for example "auf Augenhöhe", "individuell", "transparent").
3. 741.studio voice (decided later).
4. Checkpoint 1 and 2 of the Stürzl dry run (outline and final copy). The outline was not waited for in the dry run.
5. Grey zones for BRAO in the dry-run copy: FAQ question "straffrei?", "Strafbefreiung", H1 "Anwalt für Steuerstrafrecht", "langjährige Praxiserfahrung".
6. Cost model conflict on the Stürzl homepage ("RVG") against the newest client text.
7. Only the `codex` CLI is used for the cleanse. The `claudex` and `codex` skills are not needed.

## 19. Build status (2026-10-11)

| Deliverable | File |
| --- | --- |
| Coverage map v2 | `content-writing-coverage-map.md` |
| Spec | this file |
| Brief template (German form) and schema | `content-writing-brief-template.md`, `content-writing-brief.schema.json` |
| Voice template | `content-writing-voice-template.md` |
| Output templates | `content-writing-page-template.md`, `content-writing-blog-template.md` (Markdown, no HTML preview) |
| Page scorecard | `content-writing-scorecard.md` |
| Tests, dry run, workflow scorecard | `content-writing-tests-and-scorecard.md` |
| Skill draft | `content-writing-skill/` (SKILL.md, references, scripts, prompts, tests, assets) |
| Dry run | `assets/stuerzl/content-writing/selbstanzeige/` |
| Registry | `add-workflow --workflow copy` done, `_run.json` synced |
| Memory | `content-writing-workflow.md` and one line in MEMORY.md |

## Martin guide (2026-10-12)

The 741 character Martin points out the one thing per section the reader must not miss. Rules, poses, markup and the inline helper: `00_project/assets/brand/martin-guide/README.md`. In this workflow: NOT used. This workflow writes the client's own page copy, and Martin never appears on the client's website. Max 1 callout per section, bubble text in first person and plain language, every number with source and date, check desktop and mobile with a screenshot.
