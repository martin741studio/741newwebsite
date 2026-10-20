# Content Writing Workflow: Coverage Map (version 2, after the grilling)

Date: 2026-10-11. Status: draft. Owner: Martin. Author: design chat "content writing".
Purpose: show which parts of "write a page or a post" 741 already covers, where the rules are duplicated, and what is missing.
Version 2 adds section 9 (how the spec closes each gap). Spec: `00_project/content-writing-workflow.md`.

## 1. The assets I read

| Short name | Path | What it is |
| --- | --- | --- |
| DR-Prompts | `00_project/prompts/direct-response-copy-prompts.md` | Martin's "Headline-Prompt". 7 prompts: hero headline, sub-headline, PAS body, pain headline, value props, value-prop headlines, CTA. English prompts. No dashes rule. |
| CRO rules/patterns | `00_project/knowledge/cro-library/_derived/rules.md`, `patterns.md` | IF/THEN rules R2 (headlines and copy), R3 (CTA), R4 (proof), L-rules (local, HWG). 10-row homepage blueprint P0. |
| CRO Step 3 | `00_project/cro-homepage-workflow.md` Step 3, section 4b | Copy per section: 3 headline variants, body, CTA with prefill, title, meta, H1. Brief block. HWG check. Checkpoint 1. |
| Money-page standard | `00_project/startseite-money-page-standard.md` | Process A, gate A0, hard rules B, data package C, structure D, content elements D2, local minimum E, lessons I to K. |
| QA gate | `00_project/page-content-qa-checklist.md` | Phase 0 pre-flight (data points, retry rules, word count by script), Phase 1 writing rules, Phase 2 QA double check. |
| SEO skill | `.claude/skills/seo-page-optimizer/` | CREATE and AUDIT. Content spec, GEO layer, schema, rubric. Calls slopmonster at the end. |
| Behandler skill | `~/.claude/skills/behandler-seite/` | Practitioner page, E-E-A-T, Person schema, HWG box. Calls slopmonster. |
| Content pool | `00_project/content-pool-workflow.md`, `content-pool-item.schema.json`, `assets/<client>/content-pool/04-pool/pool.json`, `pool-top.md`, `05-sitetree/` | WHAT goes on a page. Ranked items, evidence, `[FEHLT]`, HWG or BRAO flag, sitetree. |
| Slopmonster | `.claude/skills/slopmonster/` | Lint (`deslop.py`), rewrite, cleanse with rival model (`cleanse.sh`), re-lint. |
| Marketing plugin skills | `marketing:content-creation`, `marketing:draft-content`, `marketing:brand-review` | Generic channel drafting and brand review. No 741 rules. No German. |
| Other | `pseo-city-service-prompt.md`, `programmatic-pages-playbook.md`, Hormozi and SEO libraries (`knowledge/`) | Programmatic pages and source libraries. |

## 2. Shortlist for "our copywriting skill" (Martin picks in round 1)

1. **DR-Prompts** (`direct-response-copy-prompts.md`). Martin's own headline prompt set, memory "headline-copy-framework". Best match for the words "our copywriting skill". It is a prompt file, not a skill. It covers headlines, PAS, value props and CTA only.
2. **CRO copy rules** (R2, R3, R4 and L-rules in the CRO library). Evidence-based IF/THEN rules. Tied to homepage conversion.
3. **CRO Step 3 + Brief template.** The only place that has a full per-section copy procedure with a checkpoint.
4. **Money-page standard + QA gate.** The SEO and fact rules. Not a voice or hook framework.
5. **Marketing plugin skills.** Generic. No 741 rules.

My proposal: the new workflow uses 1 as the hook and headline engine, 2 as the page-level conversion rules, 4 as the SEO and fact gate, and 3 as the model for the brief.

## 3. Coverage map

Legend: COVERED = a usable rule or template exists. PARTIAL = exists but only for one page type, or only as advice. MISSING = nothing exists. DUP = the same rule sits in 3 or more files.

| # | Part of "write a page or post" | Existing asset | Status | Gap or duplication |
| --- | --- | --- | --- | --- |
| 1 | Research inputs (demand, competitors, PAA, autocomplete) | Content pool (all page types), money-page standard C, QA gate 0.2, SEO skill step 1 | COVERED, DUP | Four files describe the same data package. The pool is the newest and the only one that runs as a workflow. Writing should read the pool and never re-pull data. |
| 2 | Brief (what a writer needs before the first line) | CRO Step 3 brief block (homepage only), SEO skill content spec "Target" part, pool item fields | PARTIAL | No brief for blog posts, service pages, location pages, FAQ pages. No machine-readable schema. No client-facing German form for the writing side. |
| 3 | Structure and outline (sections, H1 to H3) | CRO P0 blueprint (homepage), money-page standard D, `behandler-seite` structure, pSEO prompt | PARTIAL | Only homepage and practitioner page have a proven section order. Service page, location page, cost page, FAQ page and blog post have none. |
| 4 | Headline and hook rules | DR-Prompts 1, 2, 4, 6; CRO R2.1 to R2.5 | COVERED, DUP | Two rule sets that overlap and partly conflict (DR-Prompts allows time frames in headlines, CRO R2.2 forbids healing times). Needs one merged rule with the HWG filter. |
| 5 | Body copy rules (voice, rhythm, readability) | DR-Prompts 3 (PAS format), CRO R2.9 to R2.11, money-page standard B | PARTIAL | No voice profile. No rule for German register or du/Sie per client in one place. No rule for practitioner first person versus "wir". |
| 6 | CTA copy and rhythm | DR-Prompts 7, CRO R3.x, L6 | COVERED | Written for WhatsApp homepage. Needs a variant per channel and per page type. |
| 7 | SEO rules (title, meta, H1, word count, entities, internal links) | Money-page standard D and E, QA gate A0, SEO skill, rubric | COVERED, DUP | A0 targets money pages. No relaxed gate defined for blog posts. |
| 8 | GEO rules (answer-first block, definition box, FAQ schema) | Money-page standard D.4, SEO skill GEO layer | COVERED | Not tested on blog posts. |
| 9 | Fact and claim check | Claims-need-real-data memory, QA gate Phase 0, pool `[FEHLT]` | COVERED, DUP | No script that checks each claim in the copy against the dataset. CRO 4b has one idea: "every quoted text must be found in approved-copy.md". |
| 10 | HWG, BRAO and legal check | CRO rule 10 and L8, pool flags, `hwg-fallstudien-guideline`, `behandler-seite` rule 2, money-page B | COVERED, DUP | Six places. No single word list or script for DACH health and law copy. No scan tool in this repo. (Un-Burning UB.D11 has a text scan for live pages: reuse.) |
| 11 | E-E-A-T proof (credentials, reviews, byline) | `behandler-seite`, CRO R4.x, pool authority pillar | PARTIAL | Nothing for blog author byline, review of medical or legal content, update date. |
| 12 | AI-slop check | Slopmonster, called as a soft step in SEO skill step 2 and `behandler-seite` step 5 | PARTIAL | See section 4. The linter is English only. German slop scored 5/5 CLEAN in my test. |
| 13 | Voice capture per client | Scattered: `brand.md` in CRO dataset, memory per client, `client-form` in pool | MISSING | No voice-profile template. No rule where it lives. |
| 14 | QA gate and scorecard for copy | QA gate Phase 2, CRO scorecard (layout and conversion, not copy craft), workflow scorecard (the workflow, not the page) | PARTIAL | No page-level copy scorecard with pass thresholds. |
| 15 | Independent review | CRO optional reviewer prompt, `claudex` skills, workflow rules R5.2 | PARTIAL | No copy reviewer prompt. |
| 16 | Delivery format | Client-textdraft memory (portal page at the node), money-page G, Elementor plain text memory, CRO `copy.md` | PARTIAL, DUP | No single output template with section IDs. No CMS-ready plain-text export. No blog template. |
| 17 | Blog posts (topic choice, format, byline, update cadence, link to money pages, CTA) | Pool tag `blog-faq`, internal-linking plan, pSEO prompt | MISSING | No blog workflow at all. |
| 18 | Batch mode (many pages from one sitetree) | Night-shift (CREATE specs), sitetree from pool | PARTIAL | Night-shift writes specs, not final copy. |
| 19 | Registry and run record | `_run.json` pattern, `workflow_registry.py` | COVERED | Needs `add-workflow --workflow copy`. |
| 20 | Own 741 site and English copy | `741studio-design-system`, Bali memories | MISSING | Every rule above assumes DACH client, German, du/Sie. English and 741 voice are not covered. |

## 4. The slopmonster check (can the gate run here?)

| Question | Finding |
| --- | --- |
| Where is it | `.claude/skills/slopmonster/` in this repo. Scripts `tools/deslop.py`, `tools/cleanse.sh`, prompt `prompts/cleanse.txt`. |
| Does the linter work on German | **No.** I tested one German paragraph full of tells ("ganzheitlicher Ansatz", "nahtlos", "Reise", "nicht nur …, sondern", "Tauchen Sie ein"). Result: 5/5 CLEAN. The same text in English scored 3/5. The word list and the constructions are English only. |
| Consequence | A gate that uses `deslop.py` as it is would pass German AI copy. Almost all 741 client copy is German. The gate needs a German tell list. I would add it as a NEW script in our workflow folder. I would not edit the slopmonster repo. |
| Rival-model cleanse | `codex` CLI 0.154.0 is installed at `/opt/homebrew/bin/codex` and is logged in with a ChatGPT account. So `cleanse.sh` can run here: Claude writes, GPT cleanses. The `claude` CLI is also present. |
| Cost | No per-token API bill: the call uses the ChatGPT subscription limits. Time: up to 180 s per call (script default timeout). I did not run a real call yet. I will test with dummy text only, never with client text, before Martin decides. |
| Privacy | The cleanse sends the draft to OpenAI. Draft copy of a client page is not secret before it goes live. Client facts such as name and address are in it. Martin should decide this in the grilling. |
| Weak points | The cleanse prompt lists English words only. For German I would add a German prompt variant. The cleanse can delete a closing line (the notes show it). The re-lint after the cleanse must run on the final text. |
| Existing wiring | `seo-page-optimizer` and `behandler-seite` already call slopmonster as a soft step. The new workflow makes it a hard gate. |

## 5. Interface with the content pool (proposed input contract)

Pool item fields that become the writing brief (source: `content-pool-item.schema.json`, `pool.json`, `pool-top.md`):

| Brief field | Pool source |
| --- | --- |
| Page and section target | `page_tag`, `section_hint` |
| Topic and reader question | `topic`, `question`, `audience` |
| Keywords with volume | `keywords[]` (kw, scope, volume, source, date) |
| Search patterns and PAA | `demand.autocomplete_samples`, `demand.paa_samples` |
| Competitor benchmark | `competitor` block (set, denominator, medians) |
| Allowed claims and gaps | `fit`, `fit_reason`, `client_confirmation`, `[FEHLT]` list |
| Legal mode | `compliance` (HWG or BRAO flag with wording rule) |
| Proof assets | `evidence[]`, authority pillar items |
| Priority | `priority`, `score`, `status` (`needs_client` stays draft) |
| Site position and links | `05-sitetree/sitetree.json` (parent, siblings, internal link targets) |

What the pool does not give, and the brief must add: voice profile, CTA goal and channel, page type template, target word range, tone examples, forbidden words, byline person.

## 6. Interface with CRO Step 3 (proposal only, CRO file is not changed)

| CRO Step 3 today | Later call to the writing workflow |
| --- | --- |
| Brief block at the top of `copy.md` | CRO passes `dataset.md`, `diagnosis.md`, pool-top and the 10-row section plan as the brief. |
| Per-section copy, 3 headline variants, CTA with prefill | The writing workflow writes the 10 sections with the same section IDs and returns `copy.md` in the CRO format. |
| HWG check before checkpoint | The writing workflow runs the HWG, fact and slop gates and returns the report. |
| Checkpoint 1 (Martin approves copy) | Stays in CRO. The writing workflow has its own checkpoints for stand-alone use. |
| Design doc, images, prototype | Stay in CRO. They only read `approved-copy.md`. |

## 7. Duplicates to resolve (one source of truth each)

1. HWG and BRAO rules: six files. One rule file plus one script is the target.
2. Headline rules: DR-Prompts versus CRO R2.x. One merged page of headline rules.
3. Data package: four files. Pool is the source. Others link to it.
4. Word count and benchmark rule: money-page A0 and QA gate. Same content twice.
5. Delivery rule: money-page G, client-textdraft memory, CRO. One output template.

## 8. Open points for the grilling

Which copywriting source is "ours". Page types in version 1. English and 741's own site. Voice capture. Blocking inputs versus placeholders. Where Martin approves. Slop threshold and the German word list. Rival-model use and the privacy question. Blog rules. Output format. Dry-run page.

## 9. How the spec closes each gap (version 2)

| Map row | Gap | Closed by (spec section) |
| --- | --- | --- |
| 2 Brief | No brief for other page types, no schema | Section 5 and brief template/schema |
| 3 Structure | Only 2 proven page orders | Section 7 item 5 (page templates, marked "draft template, first use") |
| 4 Headline rules | Two overlapping rule sets | Section 7 item 1 (one merged rule page) |
| 5 Body and voice | No voice profile | Step 1, section 10.4 (voice sheet) |
| 9 Fact check | No claim script | Step 5 G1 and `diff_claims.py` |
| 10 HWG and BRAO | Six places, no script | Section 7 item 3 (one list), G2 script, shared with Un-Burning D11 |
| 11 E-E-A-T | No blog byline rule | Section 7 item 6 (blog rules) |
| 12 Slop | English only linter | Section 8 (German tell list, German cleanse prompt, claim diff) |
| 13 Voice capture | Missing | Step 1 |
| 14 Scorecard | No page-level copy scorecard | Section 11 |
| 15 Reviewer | No copy reviewer | Section 9 |
| 16 Delivery | No single template | Section 10 |
| 17 Blog | Missing | Section 7 item 6, light A0 in step 2 |
| 18 Batch | Specs only | Out of version 1 (loop of single runs later) |
| 20 Own site, English | Missing | English rules by the same templates. 741.studio voice decided later. |

Not closed in version 1: batch mode, 741.studio voice, ranking and conversion measurement after launch (dropped from success measures by Martin).
