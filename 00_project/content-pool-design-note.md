# Content Pool Workflow: Design Note (Checkpoint 1)

Date: 2026-10-11. Status: waiting for Martin's "go". Owner: Martin. Author: design chat.
Process followed: `00_project/workflow-creation-workflow.md`, sections 0 to 2.

---

## 1. Research note

- Building block (`patterns.md` section 3): a **skill** `content-pool`. Martin starts it. It reads many sources, so it uses subagents for the competitor reads. It is not a routine and not a hook.
- Pattern (`patterns.md` 4.1 and 4.4): sequential workflow with gates. The pool is a plan file (`pool.json`), checked by a script before any report is built.
- Rules that matter most:
  - R1.4: the design came from an interview with Martin (5 rounds).
  - R1.7: fragile steps are scripts (validate, score, render). Open steps are heuristics (topic ideas).
  - R4.1 and R4.6: every run ends with a validator output and a rendered screenshot.
  - R8.3: every data point is verified or marked `[FEHLT]`. No guesses.
- Reused, not rebuilt:
  - Data calls and catchment levels: `website-struktur-master-prompt.md` (steps 3 and 5). It exists only in worktree `.claude/worktrees/admiring-nightingale-f0f882`, not on `main`.
  - Page-content gate A0 and standards: `page-content-qa-checklist.md`, `startseite-money-page-standard.md`.
  - Data package fields: `.claude/skills/seo-page-optimizer/references/data-package.md`.
  - CRO homepage data and copy: `cro-homepage-workflow.md` (Steps 1 to 3).
- Open: AI-answer prompt checks have no API in this setup (Ahrefs is not usable). They run by hand in Chrome and stay optional.

## 2. Martin's decisions (grilling rounds 1 to 5)

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Position | Own step. Martin can run it alone. CRO Step 1 also calls it, before it gathers its own data. |
| 2 | Pool format | Ranked list of content items per page. Not finished copy. Not a brief per page. |
| 3 | Scope | New sites and existing sites from day one. |
| 4 | First client | Dumann (danieladumann.de, Berlin-Charlottenburg, Hildegard von Bingen). CRO dataset and brand file exist. |
| 5 | Competitors | Maps top 3 and organic top 5 in the client's city. Plus 2 to 3 national topic sites. |
| 6 | Relevance | Adjacent topics with demand are allowed. Each one is flagged for Martin and needs client confirmation. |
| 7 | Client input | Read site, GBP, portal data, client docs and reviews first. A short German form asks only for gaps. |
| 8 | Cost cap | 5 USD per run for paid data. Spend report at the end. No Local Falcon scans without Martin's go. |
| 9 | Output | HTML report (one-page summary per pillar, then detail, then raw data links) plus formatted xlsx. Both in a Drive folder. |
| 10 | Authority | Credentials, reviews, consented case studies, link and citation targets (hand over to `backlink-dach`). |
| 11 | Location | Homepage names the places. A place page enters the pool only with demand, a catchment signal and unique local facts. |
| 12 | Checkpoint | One go, on the draft pool. |
| 13 | Demand signals | Autocomplete tree and PAA, DataForSEO, client GSC and review language, Trends and AI-answer prompts. |
| 14 | Scoring | Demand 30, Gap 25, Fit 25, Conversion 15, Effort 5. |
| 15 | Trigger | Skill `content-pool`: `/content-pool <client>` and natural phrases. |
| 16 | Success | Dumann dry run: Martin keeps 80 % of the top 20 items. |
| 17 | Brand pillar | Client story, method, difference, voice. Outside data only shows where the client differs. |
| 18 | Page types | Every item gets a page tag. Homepage items get full detail. Other tags stay one line. |

## 3. Use cases

**UC1: standalone, new site.** Trigger: "Content-Pool für <Name>, <URL>, <Stadt>". Steps: baseline, competitors, demand, pool, score, report. Result: HTML report and xlsx in Drive. Martin says "go". The pool waits for the sitetree and CRO runs.

**UC2: called by CRO Step 1.** Trigger: CRO run starts. CRO Step 1 checks for a fresh `content-pool/pool.json` (not older than 30 days). If it is missing, it runs the pool first. Then Step 1 reads the pool and skips its own rows 1.5 and 1.6. Result: `dataset.md` holds a pool block, and diagnosis and copy use the homepage items.

**UC3: existing site.** Trigger: "Content-Pool prüfen für <Name>" with a live site. Same steps. Step 5 adds a status per item: `vorhanden`, `schwach`, `fehlt` (against the live pages). Result: the pool shows the gap to the live site.

## 4. Pipeline

```
Step 0  Readiness gate        inputs, access check, cost cap, folder
Step 1  Client baseline       (auto) site, GBP, portal, docs, reviews -> client-baseline.md, [FEHLT] list
        -> German input form  only if [FEHLT] items block pillars (Martin sends it)
Step 2  Seeds                 services x places x brand terms; keyword must match a real service
Step 3  Competitor set        Maps top 3, organic top 5, 2-3 topic leaders; measure content and proof
Step 4  Demand                autocomplete tree, PAA, DataForSEO, GSC, reviews, Trends, AI prompts
Step 5  Build items           per pillar: candidates, dedupe, fit test, HWG/BRAO flag, adjacent flag
Step 6  Score + page tags     script; homepage section hint for homepage items
Step 7  Validate              script: schema, evidence, dates, fit minimum; fix until pass
Step 8  Render report         HTML + xlsx; rendered screenshot check
        == CHECKPOINT: Martin reads the draft pool and says "go" ==
Step 9  Hand off              Drive upload, pool-top.md for CRO, status line
```

Unattended: Steps 0 to 8. Stops: a failed gate, or a spend over the 5 USD cap.

## 5. Interface to existing workflows (no duplicated steps)

| Existing document | What the pool does | Change needed there |
| --- | --- | --- |
| `cro-homepage-workflow.md`, Step 1 | Pool replaces rows 1.5 (keywords) and 1.6 (rankings). Rows 1.1 to 1.4, 1.7 to 1.11 stay. Pool reuses the scrape and the GBP data when they exist. | New row 1.0 "run or reuse the pool". Rows 1.5 and 1.6 point to the pool. |
| `cro-homepage-workflow.md`, rule 7 ("No competitors are analysed") | The pool analyses competitors for content, not for design. | Rule 7 reads: "Competitors are analysed only through the content pool." |
| `cro-homepage-workflow.md`, Step 2 and 3 | Diagnosis ranks the gaps and uses pool items for section jobs. Copy writes the top homepage items. | Inputs list gets `content-pool/pool.json`. |
| `website-struktur-master-prompt.md` | Pool reads the sitetree report and the catchment levels when they exist. It uses the same data calls and reuses cached JSON. | None. The pool does not build the sitetree. |
| `page-content-qa-checklist.md` gate A0 | Competitor reads follow A0: retry failed fetches, verify benchmark numbers, word counts by script. | None. |
| `seo-page-optimizer` | Later page runs read the pool items of that page as their data package. | Optional: add the pool as an input. |
| `backlink-dach` | Authority link targets go to it as a list. | None. |

These changes are proposals. This chat does not edit the CRO file or the other chat's files. Martin applies them, or says "apply".

## 6. Where files live

- Local: `00_project/assets/<slug>/content-pool/` with `_status.md`, `01-client/`, `02-competitors/`, `03-demand/`, `04-pool/pool.json`, `05-report/`.
- Drive: `Local SEO/<Client>/Content Pool/`. Same upload rules as the CRO Drive folder (no overwrite, old versions to `_archiv/`).
- Nothing in Supabase. A portal tab is a later option.

## 7. Test scenarios (written before the skill body)

| # | Type | Prompt | Expected |
| --- | --- | --- | --- |
| T1 | Obvious trigger | "Content-Pool für Dumann, danieladumann.de, Berlin" | Skill loads. Runs Step 0. Asks for the cost cap and the mode (new or existing). Writes the folder. |
| T2 | Paraphrase | "Welche Inhalte braucht die neue Seite von Dr. Adel, damit sie lokal vor den Wettbewerbern landet? Daten aus Wettbewerb und Suchnachfrage." | Skill loads. Applies the Anwaltswerbe-Check instead of HWG. |
| T3 | Must NOT trigger | "Schreib den Text für die Leistungsseite Hildegard-Medizin Berlin." | Skill does not load. `seo-page-optimizer` or `cro-homepage` handles it. |
| T4 | Must NOT trigger | "Mach den Seitenbaum mit Einzugsgebiet für Suriya." | Skill does not load. The structure playbook handles it. |

## 8. Done criteria for this session

1. Spec `00_project/content-pool-workflow.md`.
2. Data model `00_project/content-pool-data-model.md` plus `content-pool-item.schema.json`.
3. Output template (HTML, rendered check) and client form (German).
4. Skill draft in `~/.claude/skills/content-pool/SKILL.md`, scored with `scorecard.md`. Not installed live and not run before Martin's final go.
5. Dry run on Dumann after the design go. Memory file after the ship go.

## 9. Open questions for Martin (none block the design go)

1. Dumann: is the garden address (Schorfheide or Schöneberg) settled? The open point is in `dumann-ueber-mich-page`. The dry run needs one place list.
2. AI-answer prompts: manual in Chrome, optional, about 10 prompts per client. Is that acceptable?
3. May the pool reuse existing Local Falcon reports for Dumann? Reading is free. New scans stay out.
