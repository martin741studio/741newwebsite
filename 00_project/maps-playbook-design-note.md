# Maps growth playbook: design note (checkpoint 1)

Date: 2026-10-11. Status: waiting for Martin's "go". Author: design chat for workflow `maps-playbook`.
Process followed: `00_project/workflow-creation-workflow.md`, sections 0 to 2.
Language: STE. German labels are the board's own words.

---

## 1. Research note

- **Building block** (`patterns.md` section 3): a **skill** `maps-playbook`. Martin starts it with `/maps-playbook <client>`. It reads many files and sources, so it runs in a fork (`context: fork`). It is not a routine. A scheduled monthly refresh is a later option.
- **Pattern** (`patterns.md` 4.1 and 4.4): sequential workflow with gates, plus plan-validate-execute. The plan file is `tasks.json`. A script checks it before any task is released.
- **Rules that matter most:**
  - R1.4: the design comes from a 4-round interview with Martin.
  - R1.7: fragile steps are scripts (status assignment, scoring, validation). Open steps are heuristics (task wording, outreach drafts).
  - R1.8: batch changes use plan, validate, execute, verify.
  - R2.10: side effects need a gate. Martin chose natural phrases as triggers. So the gates sit inside the body, not in a frontmatter flag. The scorecard checks this.
  - R4.1 and R4.6: every run ends with a validator output and a rendered screenshot.
  - R8.1 to R8.3: the run ends with a client message draft and a Drive link. Every data point is verified or marked `unknown`.
- **Reused, not rebuilt:** audit fields B01 to B13 (diagnosis), content pool items (page content), `backlink-dach` (links and buy path), Citations module (directories), `seo-page-optimizer` (page specs), `cro-homepage` (homepage), WK1 playbook (tool recipes, monitoring rhythm).
- **Sibling update (11.10.2026):** `un-burning-workflow.md` exists. Its first client is also Praxis Suriya. Its bedrock check is the readiness gate for growth work. The playbook reads its harm register and does not repeat its checks.
- **Open:** four source files live only in worktrees (see the coverage map, finding 8). The 90-day program file is missing.

## 2. Martin's decisions (grilling rounds 1 to 4)

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Shape | Matrix with evidence per measure **and** a short runbook per gap that creates the approved task |
| 2 | First client | Praxis Suriya (health). Dry run is read only |
| 3 | Risk sorting | Accepted as in the coverage map: 56 DO, 20 DO WITH GATE, 1 OUT (bonus per 5-star). Gates 10 (abandoned forms, GDPR) and 11 (own best-of lists) added |
| 4 | Evidence age | By type: live data 30 days, scans 60 days, documents and legal facts 180 days |
| 5 | Executor | Mixed. Agent prepares. Agent edits GBP and site only with access and a go. Humans send outreach by Airmailer. Client gives photos, review asks and decisions |
| 6 | Go unit | Client approves a bundle on the report page. Martin gives one go per execution batch. Every change is logged |
| 7 | Priority | Impact score from the audit driver result, divided by effort and risk. Fixed 30-day start |
| 8 | Storage | Supabase tables (master), JSON per run, Sheet view, HTML one-page board. Tables need a separate go |
| 9 | Niches | Health (HWG), trades and local services, law and tax |
| 10 | G22 | Only reclaim the client's own old profiles. No takeover-defence task |
| 11 | Cadence | Monthly matrix refresh. Falcon every 2 weeks after changes, AI check monthly, quarterly trend. Baseline = last audit run |
| 12 | Success | Falcon SoLV gain, calls and route requests, review pace against 2x leader. Plus under 3 corrections per matrix (my default) |
| 13 | DACH mapping | Accepted. Each tool is verified during the build |
| 14 | No audit yet | Read Drive audits and sheets, check live where stale, flag age. Suggest an audit re-run if key fields are red or missing |
| 15 | Trigger | `/maps-playbook <client>` and natural phrases |
| 16 | Cost cap | Monthly refresh: 2 EUR data and 200 Falcon credits. Scans only after Martin's go. Never retry a scan |

Defaults I set (Martin can change them): status values (section 5), score formula (section 6), the catalogue field list (section 7), no per-star incentive in any niche.

## 3. Use cases

**UC1: first matrix for a client.** Trigger: "/maps-playbook Praxis Suriya" or "Maps-Playbook für Suriya". Steps: readiness, evidence, matrix, validate. Result: one-page board and Sheet, with the top 5 next tasks. Martin reads it and says "go" or corrects.

**UC2: monthly refresh.** Trigger: "Maps-Playbook Refresh Hüwel". Steps: re-check only stale or changed cells, update the status, compare with the last run. Result: delta board (what moved, what is new, what is overdue).

**UC3: quick-win question.** Trigger: "Was fehlt, damit Hüwel auf Maps Platz 1 kommt? Prüf auch, was schon erledigt ist." Result: top quick wins, ranked by score, each with evidence and gate.

**UC4: new measure from Martin.** Trigger: "Neue Maßnahme: ..." Result: catalogue entry with all fields, a new catalogue version, a diff for client instances.

## 4. Pipeline

```
Step 0  Readiness gate     client, niche, portal ID, Drive folder, audit evidence, un-burning state
Step 1  Evidence harvest   Drive audits and sheets, audit run JSON, Falcon reports (free), portal, GSC and GA4; live checks where stale
Step 2  Status matrix      script assigns status from audit fields and rules; agent fills measures without an audit field
Step 3  Validate           script: every cell has evidence, date, age within rule; gate flags set; no guess
        == CHECKPOINT A: Martin reads the one-page board (corrections are counted) ==
Step 4  Gap to tasks       tasks.json: measure, action, owner type, gate, score, effort, dependency, cost; script validates
Step 5  Client bundle      client-safe report page with approval boxes. No tool names, no team names. HWG check for health
        == CHECKPOINT B: Martin releases the bundle to the client ==
        (client approves the bundle)
        == CHECKPOINT C: Martin gives one go for an execution batch ==
Step 6  Execute and log    agent-executable tasks run with access. Outreach and review asks stay with humans. Each change is logged with before and after
Step 7  Re-check           evidence for changed cells, status update, Falcon by rhythm
Step 8  Deliver            Drive link, screenshot as file, client message draft (ich form, no call offers)
```

Unattended: Steps 0 to 4. Stops: a failed gate, a missing access, or a spend over the cap.
No client asset changes before Checkpoint C. Gate measures (section 8) need their gate proof before Step 6.

## 5. Status logic

| Status | Meaning |
| --- | --- |
| `done` | The measure is in place and evidence is fresh |
| `partly` | A part is in place. The cell names what is missing |
| `missing` | Not in place |
| `n/a` | Not relevant. The cell names the reason (niche, no premises, not allowed) |
| `unknown` | No data, or evidence older than the age rule. Never a guess |

A task has its own state: `proposed`, `approved`, `blocked` (names the blocker), `in_progress`, `done`, `verified`. A measure is `done` only after the evidence shows it.
Evidence types and age rules: `live` 30 days, `scan` 60 days, `document` 180 days. Confidence: `verified`, `derived`, `client_stated`.

## 6. Priority score

`score = impact x confidence / (effort + risk)`

| Part | Scale | Source |
| --- | --- | --- |
| impact | 1 to 5 | Effect on Maps rank and calls. For a P1 measure the audit driver result (field `B11.09`) sets it. A measure with a controllable driver gap gets 5 |
| confidence | 0.5 to 1 | `verified` 1, `derived` 0.75, `client_stated` 0.5 |
| effort | 1 to 5 | S = 1, M = 2 to 3, L = 4 to 5 |
| risk | 0 to 3 | DO = 0. Gate = 1 to 3 by gate (name, address, paid link = 3) |

Dependencies override the score. Examples: G08 (services) needs W09 (page). Gate 1, 7 and 8 measures need the clean-up from `un-burning` first. O13 (buy) needs review pace and on-page to be solid.
**Days 1 to 30:** clean-up check, profile basics (G01 to G03, G05 to G08; G04 follows in month 2), review engine (G14, G15, G17, G18), citations (O01 to O05). **From month 2:** pages (W09 to W15, W26 to W31) and links (O06 to O12).
**Top-of-Maps quick wins** = the top 5 by score among P1 measures with a controllable audit driver.

## 7. Catalogue and data model

One master catalogue `00_project/maps-playbook-measure-catalog.json`. Fields per measure: `id`, `pillar`, `group`, `label_de`, `source` (board or text), `dach_adaptation`, `niche_rules` (health, trades, law and tax), `risk_class`, `gates`, `gate_text`, `alternative`, `audit_feed`, `evidence_sources`, `age_rule`, `automation` (A check, B agent prepares, C agent edits with go, D human, E client), `linked_asset`, `effort`, `owner_type`, `dependencies`, `cadence`, `status_rules`, `unburn_overlap`.
Versioning: `catalog_version` as `major.minor.patch`. A measure is never deleted. It gets `deprecated_in`. A client instance stores its `catalog_version`. An upgrade writes a diff.
Client instance: `playbook_runs`, `measure_status` (status, evidence id, date, owner, task id), `tasks`, `evidence`, `change_log`. Draft SQL only. No table is created before Martin's go.

## 8. Risk gates (one line each)

| Gate | Rule |
| --- | --- |
| 1 DBA name | Only a real legal business designation that also appears on signage, imprint and site. Never a profile-only trick. Audit field B13.03 stays red until proof exists |
| 2 Reviews | Ask every customer. No filter. No per-star bonus (OUT). Requests by mail or SMS need a legal basis (consent): checked in the build |
| 3 Reddit | Burying is OUT. Watch and answer with real help. Own positive content |
| 4 Paid links | Only through the `backlink-dach` buy path. Paid articles carry a label. Donation for a link counts as paid |
| 5 Health | HWG check on photos, offers, prices, project reports and embedded reviews. No cure promise |
| 6 Spam reports | Only genuine, documented violations. Evidence log first |
| 7 Profiles | Only the client's own real locations and former profiles |
| 8 Address | Only a real eligible address. No virtual or coworking address. Service-area profiles keep the real setting |
| 9 Tracking number | Main number stays primary NAP. Tracking number secondary only. GDPR consent on the site |
| 10 Abandoned forms (new) | No data is stored before consent. Health data: off by default |
| 11 Best-of lists (new) | Neutral rules, no fake rankings, labelled as own list |

## 9. Test scenarios (written before the skill body)

| # | Type | Prompt | Expected |
| --- | --- | --- | --- |
| T1 | Obvious trigger | "/maps-playbook Praxis Suriya" | Skill loads. Runs Step 0. Finds portal ID and Drive folder. Lists evidence found. Asks nothing that exists in files |
| T2 | Paraphrase | "Was fehlt noch, damit Hüwel in Nürnberg bei Google Maps auf Platz 1 kommt? Prüf auch, was wir schon gemacht haben." | Skill loads. Builds a status matrix and a top-5 quick-win list. Marks stale evidence |
| T3 | Must NOT trigger | "Mach ein Maps-Audit für Stürzl" | Skill does not load. The audit workflow handles it |
| T4 | Must NOT trigger | "Trag Hüwel bei Gelbe Seiten ein" | Skill does not load. The Citations module handles it |
| T5 | Must NOT trigger | "Schreib den Text für die Leistungsseite Ayurveda-Massage" | Skill does not load. `seo-page-optimizer` handles it |

## 10. Done criteria for this session

1. Coverage map, final version (after the go).
2. Master measure catalogue (JSON, 77 measures, validated by script).
3. Workflow spec `00_project/maps-playbook-workflow.md`.
4. Sheet design (columns, formatting, validation, tabs). Nothing is created in Drive without a go.
5. Report wireframe and a rendered HTML prototype, checked with a screenshot.
6. Read-only dry run on Praxis Suriya.
7. Skill draft in `~/.claude/skills/maps-playbook/SKILL.md`, scored with `scorecard.md`. Not installed live before the final go.
8. Memory file and a line in `MEMORY.md` after the ship go.

## 11. Open questions (none block the design go)

1. Four source files live only in worktrees. Martin merges them into `main`, or confirms the worktree paths.
2. The 90-day program file is missing. Martin gives the path.
3. Review requests by mail or SMS: the legal basis is checked in the build. If a lawyer opinion exists, Martin gives it.
4. Tracking number provider for DACH: not chosen. Optional for v1.
