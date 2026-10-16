---
name: backlink-dach
description: Runs the 741 Backlink Workflow DACH for one local client, pillars B to E only - competitor backlink gap (8+ competitors), local ecosystem targets (Verbände, Vereine, Presse, Sponsoring, Hersteller and Lieferanten), digital PR and unlinked mentions, a strict backlink-buy path with Kennzeichnung, and the AI-citation check. Produces a target list as a Google Sheet with a Freigabe box per row. Never sends outreach, never buys. Use when Martin says "Backlink-Workflow für <Kunde>", "Linkaufbau für <Kunde>", "welche Links können wir für <Kunde> bauen", "backlinks for <client>", "run the backlink workflow", or names a client and budget and says go for this workflow. Do NOT use for any directory or citation entry, also not niche directories (Gelbe Seiten, Das Örtliche, jameda, Doctolib, theralupa - that is the Citations module), not for page content (seo-page-optimizer) and not for a homepage prototype (cro-homepage).
context: fork
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Bash(node:*), Bash(python3:*), Bash(uv:*), Bash(git:*)
---

# backlink-dach

Source of truth for the process: `00_project/backlink-workflow-dach.md` (v1.1). Read it fully at the start of every run. This skill tells you how to operate it.

Scorecard: `00_project/backlink-scorecard-2026-10-13.md`. Re-score after every 5 real runs.

## Critical

- Start gate (Martin, 2026-10-13): when this skill loads without the `/backlink-dach` command (Claude loaded it from Martin's own words), run Step 0 read-only and stop. Show the Step 0 result and ask for "go". No DataForSEO call, no Drive file, no `_run.json` before that go.
- The agent never sends outreach, never polls for replies and never pays. A human sends through Airmailer and pays after Checkpoint 4.
- Pillar A is not part of this workflow (Martin, 2026-10-13). All directories, also niche directories (jameda, Doctolib, theralupa, Heilpraktiker.de …), belong to the Citations module. This workflow only lists them as a hand-over (doc section 3.0). `scripts/build_sheet.py` refuses a Säule-A row.
- Every Sheet row needs a traceable Quelle and a Kontakt. Run `scripts/build_sheet.py`. It refuses to write a Sheet with a gap. Fix the CSV until it passes.
- Finish Hüwel to at least one live non-directory backlink before a second client starts with this workflow, unless Martin overrides.
- The Hüwel pilot folder is only in the worktree `.claude/worktrees/great-easley-4f6970/00_project/assets/huewel/backlinks/` (state 2026-10-13). Read it there. Do not create a new empty `huewel/backlinks/` on main. The local `02-targets/targets.md` is v2; the Sheet is v5 and is the current list.

## Inputs Martin gives at the trigger

1. Client slug and name. The client must already have `client_locations` and `client_citations` in Supabase. This workflow does not onboard a client.
2. City and industry. Usually in `client_locations`. Confirm, do not re-ask.
3. Monthly budget in €. 0 is valid. Then only the free pillars B, D and E run.
4. Named competitors, if Martin knows some. Otherwise find them per Process B.

Nothing else. Check memberships, client-intro possibility and review/on-page readiness against existing data first. Ask only what is not findable, as `[FEHLT: …]`.

## Fixed decisions (do not re-ask)

- No outreach by the agent (2026-10-11). It drafts every mail and marks the row "ready to send". A human sends manually through Airmailer and updates Status.
- Pillar C (buy) stays, strict: `[KENNZEICHNUNG]` on every paid placement, price bands in doc section 3.2, never a subscription.
- Pillar A border (2026-10-13): hand-over list only, never Sheet rows. Berufsverband member listings stay in pillar B, because they need a membership.
- Competitor analysis is mandatory. Minimum 8 competitors. `scripts/gap-analysis.mjs` enforces it.
- Fixed local priority, not blended with the score: IHK/HWK (only if the profession is `Gewerbe`-pflichtig) → Berufsverband → everything else by distance to the client address. See `link-library/_derived/rules.md` RH.4/RH.5.
- Before scoring a raw referring-domains export, run it through `00_project/knowledge/link-library/_derived/local-backlink-classifier-prompt.md`.
- Readiness gate: check on-page keywords (`rules.md` RH.1). Reviews are NOT a gate (Martin, 2026-10-14): backlinks and reviews are separate topics. Weak reviews never pause backlinks. Name them once as a separate review-strategy task, then continue. Backlinks come mainly from collaborations with local businesses.
- Library: `00_project/knowledge/link-library/_derived/rules.md`. Read it before research, every run. In client-facing files call it "741 Link-Raster". Never name method sources.
- All produced files in German. **du** for Vereine, Blogger, small business. **Sie** for IHK, Kammern, Verbände, Presse, Behörden, and AT/CH by default.
- Tools: DataForSEO Backlinks + SERP (via `scripts/gap-analysis.mjs`), Firecrawl search/scrape, `claude-in-chrome` for the Sheet check, Supabase 741-portal via `execute_sql` (SELECT only, never INSERT/UPDATE/DELETE), Google Drive MCP for the Sheet, Airmailer (human only). No Ahrefs. No auto-buy marketplaces.

## Result format — the Sheet is the deliverable

One Google Sheet per client: `Local SEO/<Client name>/Backlinks/Backlink-Ziele <Client>`.

Columns (Martin, 2026-10-11): `#, Domain, Säule, Taktik, DR (approx.), Kosten, Quelle, Kontakt, Status, Freigabe`. No Score column, no Form column. DR (approx.) = `round(min(rank/10, 100))` from the DataForSEO rank. Say once in the legend that it is not an official DR figure.

Default output at each checkpoint (strict order):

```
Checkpoint <n> — <Kunde> — <Datum>
1. Was neu ist: <max 5 Zeilen>
2. Ergebnis: <Pfad oder Sheet-Link>
3. Übergabe an das Citations-Modul: <Liste oder "keine">
4. [FEHLT: …]: <Liste oder "keine">
5. Beleg: <Script-Ausgabe, Screenshot-Pfad>
6. Frage: go für Step <n+1>?
```

## Scripts (run them, do not rewrite them)

- `scripts/gap-analysis.mjs` — Process B: competitor backlink pull, gap, spam flag, DR conversion. `node`, needs `.secrets/dataforseo.env`. Enforces 8+ competitors. Writes `profile.md` and `gap.md` into `01-baseline/`.
- `scripts/build_sheet.py` — builds the xlsx from a CSV with XlsxWriter (Drive-safe, memory `well-designed-sheets.md`). Run: `uv run --with xlsxwriter python3 scripts/build_sheet.py --title "Backlink-Ziele — <Kunde>" --rows rows.csv --out <file>.xlsx`. Exit 1 lists every bad row (missing Quelle/Kontakt, Säule A, unknown Status).
- `scripts/write_run.py` — writes `00_project/assets/<slug>/backlink/<YYYY-MM-DD>/_run.json` for the overview Excel. Run at each checkpoint and at the end.

## Run procedure

Copy this checklist and tick it off:

- [ ] Step 0: Readiness gate (doc Step 0), read only. Weak on-page → stop and say so. Weak reviews → note as a separate task, do not stop. Loaded without `/backlink-dach` → stop here and ask for go (start gate). After go: write `_run.json` (`--status "in Arbeit" --note "Step 0"`).
- [ ] Step 1: Baseline. Read `00-client-info.md` and `_status.md` in `00_project/assets/<slug>/backlinks/` (create from doc section 6 if missing). Run `scripts/gap-analysis.mjs`. Do the hand-over check (doc 1.4, read only). Work the local tactics RB.3–RB.9 as a full checklist, not stop-at-first-hit.
- [ ] **Checkpoint 1** — show the raw baseline as plain lists: profile, gap, hand-over list, local finds. No score, no Sheet. Update `_run.json`. Wait for "go" or a named correction.
- [ ] Step 2: Score internally, build the CSV, run `build_sheet.py` until exit 0, upload with Drive `create_file` (do not set `disableConversionToGoogleType`), `trash_file` the old version, open in `claude-in-chrome` and screenshot.
- [ ] **Checkpoint 2** — Sheet link, diff to the last version, open `[FEHLT]` list. `write_run.py --status "fertig, Freigabe offen" --result <Sheet-Link>`. Wait for "go".
- [ ] Step 3: Draft outreach mails for rows with Freigabe ☑. Mark "ready to send" in the Outreach tab.
- [ ] **Checkpoint 3** — Martin or the team tick Freigabe per mail and send manually. The agent's work on that row ends here.
- [ ] Step 4 (only if budget > 0): buy shortlist. **Checkpoint 4** — explicit go before any money moves.
- [ ] After every step: one `_status.md` line. Never overwrite a file; use `v2`, `v3`.

Step 5 (monthly report) is not scheduled yet. It starts when a client has live links.

## Verification loop (before every "done")

1. Run `build_sheet.py`. Exit 1 → fix the CSV → run again. Proceed only at exit 0.
2. Check the target list against `rules.md` RB.3–RB.9 as a list and against the hand-over check. Both are easy to half-do. Both found real free targets on Hüwel that a thin pass missed.
3. Open the Sheet in `claude-in-chrome` and screenshot it. Two of the first three Hüwel rebuilds had conversion faults that only the screenshot showed.
4. Put the evidence (script output, screenshot path, Sheet link) in line 5 of the checkpoint output.

## Trigger

Claude may load this skill from Martin's own words (Martin, 2026-10-13: lock removed, start gate added instead). `/backlink-dach <Kunde>, Budget <€>` starts it directly and skips the start gate.

Test scenarios, run 2026-10-13 in fresh `claude -p` sessions (evidence in `00_project/backlink-scorecard-2026-10-13.md`):

1. Obvious: "Backlink-Workflow für Hüwel starten, Budget 0" → loads.
2. Paraphrase: "schau mal, welche Links wir für Suriya noch bauen können" → loads, names the Hüwel-first rollout rule.
3. Must not trigger: "trag Hüwel bei Gelbe Seiten ein" → Citations module.
4. Border: "trag Hüwel bei jameda ein" → Citations module.

When triggering goes wrong, fix the description, not the body.

## When Martin says the list is thin

This happened three times on the Hüwel pilot: a 7-row list without Quelle, a library that was built but not read, and a process that was only ad-hoc calls. Before you report a list as done, run the verification loop above.
