# 741 Workflow Architecture Map

Version 0.1 · 2026-10-13 · Owner: Martin · Written by the morning-grill design chat (⚙️🏗️ chat base family).
Language: STE. Registry ids and file paths are exact. Sources: `00_project/workflow-registry/registry.json` (read 2026-10-13), the workflow specs, memory files, the session list.

Purpose: one page that shows every 741 workflow, where it sits in the client journey, what starts it, what it needs, what it gives, who runs it, and how mature it is. The morning grill reads this map to know which workflow is the next step for each client.

## 1. The client journey in 8 phases

```
P0 Prospect ─► P1 Onboarding ─► P2 Audit ─► P3 Un-Burning ─► P4 Build-up ─► P5 Content ─► P6 Proof + Quarter
                                                              (citations,      (pool,         (tracking,
                                                               phone, links,    writing)       war room)
                                                               CRO)
Cross-cutting:  P7 Operations = morning grill, evening log, night shift, daily standup, automation build, lockout (incident)
```

Rules of the sequence (from the specs):
- The audit is the diagnosis. Un-Burning repairs harm. The maps playbook adds growth. Harm comes before growth (`maps-playbook-workflow.md` §2).
- Growth measures that touch a harm item wait until Un-Burning clears that item.
- The content pool decides what to write. Content writing writes it. The CRO workflow builds the page.
- Tracking proves the result and feeds the 90-day war room.

## 2. Workflow table

Status words: **installed** = skill in `~/.claude/skills/` or `.claude/skills/`. **draft** = spec and skill draft, not installed. **spec** = spec only. **live module** = runs in the portal, no skill.

| # | Workflow | Phase | Registry id | Trigger | Inputs | Outputs | Owner (agent / human) | Status | Chat |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Prospect review page (v2.1) | P0 | `prospect` | "Review page for <name>", LinkedIn card, prospect URL | Name, website, Maps link | `741.studio/review/<slug>/`, Loom script, WhatsApp message with email ask | Agent builds. Martin records Loom and sends | installed (`.claude/skills/local-seo-review-page`) | ⚙️📄 Review page v2 test; ⚙️🎬 10-minute scripts |
| 2 | Client access lockout | P1 / incident | `lockout` | `/client-access-lockout <client>, <what was removed>` | What access was lost, contract, run history | Client letter (PDF), evidence pack, Drive filing after send go | Agent drafts. Martin sends | installed, 96.3 % | ⚙🛡 Client access lockout workflow |
| 3 | Maps audit (Maps-Readiness) | P2 | `audit` | "Starte den Maps-Audit für <client>" | GBP, website, 5 keywords, 5 competitors, client form | Audit report, score 0–100, traffic lights, run.json | Agent. Martin approves (Go-C) | spec (design go 2026-10-11), no skill | ⚙️🔍 Client audit workflow |
| 4 | Un-Burning | P3 | `unburning` | "Starte Un-Burning für <client>", red audit fields | Audit fields, harm checks | `harm-register.json`, bedrock light A–E, client report | Agent finds. Dinakar / Tantri fix. Client does logins | draft (design go 2026-10-11) | ⚙️🧯 Un-Burning workflow |
| 5 | Citations DACH module | P4 | `citations` | "Prüfe den Citation-Status für <client>" | Canonical NAP (`client_locations`), 44 directories | `client_citations` status, BrightLocal order, self-service tab "Sichtbarkeit", submission runbook | Agent prepares. Martin buys. Client does group B. Tantri / Dinakar do group A | live module (portal), no skill, no run folder | ⚙️🖇️ Build DACH citations module + Coralie BrightLocal order (moved into the ⚙️🏗️ group 2026-10-13) |
| 6 | Maps playbook ("Get the phone to ring") | P4 | `phone` | "Maps-Playbook für <client>" | Audit fields, harm register, pool items | Measure matrix (77 measures), task list with phase `d1-30` / `m2+` / `later` | Agent plans. Team executes | draft (design go 2026-10-11) | ⚙️📞 Get the phone to ring check |
| 7 | Backlink DACH | P4 | `backlink` | `/backlink-dach <client>, <city>, <budget>` | Competitors (min. 8), link library, budget | Google Sheet target list with approval boxes; outreach batch; buy path | Agent researches. Martin approves rows and buys. Gayo can do outreach | installed, 47.8 % (not ship-ready). **Kept as own workflow (Martin 2026-10-13)** | ⚖️ Stürzl — Backlink-Workflow (client run, no ⚙️ chat) |
| 8 | CRO Homepage Track A | P4 | `cro` | `/cro-homepage <name>, <URL>, <GBP>, <channel>` | Site scrape, pool, GBP | Desktop prototype, GPT mockup, handoff, Drive folder | Agent builds. Dinakar implements in the CMS | installed, 43/54 (fix first) | ⚙️🏠 CRO Homepage workflow setup |
| 9 | CRO Track B (design-intense) | P4 / P0 pitch | `cro_b` | "Track B für <client>" | B0 questionnaire, element pool | Showpiece prototype | Agent + Martin | spec, no skill | none |
| 10 | Content pool | P5 | `pool` | "Content-Pool für <client>" | Competitors, demand data (DataForSEO, GSC), client form | Ranked pool, sitetree, xlsx report | Agent. Martin approves pool and sitetree | draft, not installed | ⚙️🗂️ Content pool workflow |
| 11 | Content writing | P5 | `copy` | `/content-write <client> <page>` | Pool items, live voice, brief | Page text (portal page at the node), slop gate 5/5 | Agent writes. Martin approves. Dinakar publishes | installed | ⚙️✍️ Content writing workflow |
| 12 | Proof tracking + quarter | P6 | `tracking` | Weekly read, early warning, quarter end | GBP performance (Falcon MCP), GA4, scans, reviews | Portal tab "Ergebnisse", early warnings, quarterly war-room pack | Agent reads. Martin runs the war room | spec + prototype (design go 2026-10-12) | ⚙️📈 Proof tracking + quarterly strategy round |
| 13 | Automation build | P7 | `automation` | `/automation-build` | Spec, test plan, credentials | Tested automation, runbook, go-live checklist | Agent builds. Martin gives go per layer | draft, hooks not installed | ⚙️🧪 Automation build workflow |
| 14 | Night shift | P7 | none | `reporting/night-shift.sh` or "run the night shift" | Open content tasks from the portal | Markdown page specs and audits for the morning | Agent, unattended. Never publishes | installed skill (`.claude/skills/night-shift`), OAuth token open | none |
| 15 | Daily client standup | P7 | none | LaunchAgent weekdays 08:05 | Supabase DB function | Admin standup page | Agent, unattended | live | none |
| 16 | Morning grill + evening log (new) | P7 | `morning` (proposed) | Morning: "Grill me" / schedule. Evening: "Log the day" | This map, registry, git, sessions, portal, tracking | Daily brief, decision queue, plan per client, evening log | Agent prepares. Martin decides | design (this chat) | ⚙️🧭 Morning grill (proposed) |

Also in use but not workflows: `seo-page-optimizer` (page specs, used by night shift), `behandler-seite` (practitioner pages), `imagery-audit`, `slopmonster` (gate).

## 3. What each phase needs before the next phase starts

| From → to | Gate (must be true) | Who checks |
|---|---|---|
| P0 → P1 | Signed offer, first payment, client in portal | Martin |
| P1 → P2 | Access to GBP, website, GSC / GA4 confirmed; NAP fixed | Agent checks, Martin confirms |
| P2 → P3 | Audit report exists, harm vs gap split done | Agent |
| P3 → P4 | Bedrock light green for the areas a growth measure touches | Agent (harm register) |
| P4 → P5 | Sitetree approved; citations group A submitted | Martin |
| P5 → P6 | First pages live; tracking baseline saved | Agent |
| P6 → next quarter | War-room pack done, next 90-day goals set | Martin with client |

## 4. Citations and backlinks as proper workflows (proposal)

Martin asked to put both into the architecture. Today both lack a run folder, so the overview Excel shows them only through manual `upsert`. The proposal below makes them normal workflows. **Nothing is built. Each step needs Martin's go.**

### 4.1 Citations DACH (`citations`)

| Item | Today | Proposal |
|---|---|---|
| Spec | Memory `citations-listings-module.md` only | `00_project/citations-workflow.md`: phases NAP lock → aggregator self-service → group A (741) → BrightLocal order → group B (client) → niche (jameda, Doctolib) → live checks → monitor |
| Skill | none | `/citations-dach <client>` with `disable-model-invocation: true`. Scripts exist: `reporting/citation-monitor.mjs`, `reporting/import-brightlocal.mjs`, `reporting/submission-runbook.mjs` |
| Run folder | none | `00_project/assets/<client>/citations/<YYYY-MM-DD>/_run.json` + `status.md` (counts live / submitted / planned from `client_citations`) |
| Registry | id exists, manual upsert | `sync` reads `_run.json`. No code change |
| Chat | ⚙️🖇️ Build DACH citations module + Coralie BrightLocal order | Done 2026-10-13 on Martin's word: renamed with ⚙️ and moved into the group ⚙️🏗️ Chat-based workflow architecture |
| Daily signal for the grill | none | Count of `planned` rows older than 14 days per client; BrightLocal live checks; unhandled rows in `listing_emails` |

### 4.2 Backlink DACH (`backlink`)

Martin (2026-10-13): keep both workflows; they have different outcomes. Citations = the same NAP data live on Google, Apple, Bing and ~90 DACH directories. Backlink DACH = authority links from associations, chambers, press, sponsors, suppliers, PR and a strict buy path (≥ 8 new referring domains in 90 days). Border: free niche directories (jameda, Doctolib, theralupa …) belong to citations. The maps playbook only tracks O01–O20.


| Item | Today | Proposal |
|---|---|---|
| Spec | Was only in worktree `great-easley-4f6970` | DONE 2026-10-13: doc and `00_project/knowledge/link-library/` copied to `main` (unchanged) |
| Skill | installed, 47.8 % | Finish trigger tests and baseline; rescore to ≥ 80 % |
| Run folder | Google Sheet only | `00_project/assets/<client>/backlink/<YYYY-MM-DD>/_run.json` with the sheet link in `result` and approved / live counts in `note` |
| Chat | ⚖️ Stürzl — Backlink-Workflow | new ⚙️🔗 Backlink DACH workflow chat for the workflow itself; client runs stay in client chats |
| Daily signal for the grill | none | Rows with approval box ticked but status not `live`; outreach replies; buy decisions waiting |
| Rule from memory | Second client only after the first live link at Hüwel | The grill asks this as a gate question |

## 5. Gaps found while mapping

1. ~~Backlink doc and link library are not on `main`~~ fixed 2026-10-13.
2. Citations and backlinks write no `_run.json`, so the Excel cannot see their progress.
3. Audit has no skill. Pool, Un-Burning, Maps playbook, tracking and automation are drafts. Only 6 workflows are installed.
4. The 90-day program file is outside the repo (`~/Downloads/741-studio-portal-90-tage-programm.md`). The maps playbook spec says "file is missing".
5. Many client chats run in their own worktrees. A scan of `main` alone misses their work. The morning scan must read all worktrees and the session list.
6. No workflow defines per-client goals, KPIs and leading indicators in one place. Tracking has the metric catalogue, but the goal per client is not stored.

## 6. Maintenance

- Update this file when a workflow changes status (installed, approved) or a new workflow is added with `add-workflow`.
- The morning grill flags a row as stale when the registry says something different from this table.
