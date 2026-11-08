---
name: backlink-dach
description: Runs the 741 Backlink Workflow DACH for one local client, pillars B to E: competitor backlink gap (8+ competitors), local ecosystem targets, digital PR, backlink-buy path with Kennzeichnung, AI-citation check. Produces a target Sheet with Freigabe per row. Never sends outreach, never buys. Trigger on "Backlink-Workflow für <Kunde>", "Linkaufbau für <Kunde>", "backlinks for <client>". Not for directory or citation entries (Citations module).
context: fork
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Bash(node:*), Bash(python3:*), Bash(uv:*), Bash(git:*)
---

# backlink-dach

Process: `00_project/backlink-workflow-dach.md` (v1.1). Read it fully at the start of every run. Scorecard: `00_project/backlink-scorecard-2026-10-13.md` (re-score every 5 real runs).

## Critical

- **Start gate (Martin, 2026-10-13):** when the skill loads without the `/backlink-dach` command (from Martin's own words), run Step 0 read-only and stop. Show the result and ask for "go". No DataForSEO call, no Drive file, no `_run.json` before that go. `/backlink-dach <Kunde>, Budget <€>` skips the gate.
- The agent never sends outreach, never polls for replies, never pays. A human sends (Airmailer) and pays after Checkpoint 4.
- Pillar A is not part of this workflow. All directories, also niche ones (jameda, Doctolib, theralupa, Heilpraktiker.de), go to the Citations module as a hand-over list (doc section 3.0). `build_sheet.py` refuses a Säule-A row.
- Every Sheet row needs a Quelle and a Kontakt. `build_sheet.py` refuses gaps; fix the CSV.
- Finish Hüwel to at least one live non-directory backlink before a second client starts, unless Martin overrides. The Hüwel pilot folder lives only in the worktree `.claude/worktrees/great-easley-4f6970/00_project/assets/huewel/backlinks/`; never create an empty `huewel/backlinks/` on main. The Sheet (v5) is current, not `02-targets/targets.md` (v2).

## Inputs

Client slug and name (needs `client_locations` and `client_citations` in Supabase), monthly budget in € (0 is valid: only free pillars B, D, E run), named competitors if known. City and industry come from `client_locations`. Ask only what is not findable, as `[FEHLT: …]`.

## Fixed decisions (do not re-ask)

- The agent drafts every mail and marks the row "ready to send". A human sends through Airmailer and updates Status.
- Pillar C (buy) stays strict: `[KENNZEICHNUNG]` on every paid placement, price bands in doc section 3.2, never a subscription. No auto-buy marketplaces.
- Competitor analysis is mandatory, minimum 8 (`gap-analysis.mjs` enforces it).
- Fixed local priority, not blended with the score: IHK/HWK (only if the profession is `Gewerbe`-pflichtig) → Berufsverband → everything else by distance to the client address (`link-library/_derived/rules.md` RH.4/RH.5).
- Run a raw referring-domains export through `00_project/knowledge/link-library/_derived/local-backlink-classifier-prompt.md` before scoring.
- Readiness gate: on-page keywords (`rules.md` RH.1). Reviews are NOT a gate (Martin, 2026-10-14): name weak reviews once as a separate task, then continue. Backlinks come mainly from collaborations with local businesses.
- Read `00_project/knowledge/link-library/_derived/rules.md` before every run. Client-facing: call it "741 Link-Raster", never name method sources.
- All files in German. **du** for Vereine, Blogger, small business; **Sie** for IHK, Kammern, Verbände, Presse, Behörden, and AT/CH by default.
- Tools: DataForSEO via `gap-analysis.mjs`, Firecrawl, `claude-in-chrome` for the Sheet check, Supabase `execute_sql` (SELECT only), Drive MCP, Airmailer (human only). No Ahrefs.

## Deliverable: the Sheet

One Google Sheet per client: `Local SEO/<Client name>/Backlinks/Backlink-Ziele <Client>`. Columns (Martin, 2026-10-11): `#, Domain, Säule, Taktik, DR (approx.), Kosten, Quelle, Kontakt, Status, Freigabe`. No Score, no Form column. DR (approx.) = `round(min(rank/10, 100))` from the DataForSEO rank (legend: not an official DR).

Checkpoint output, in order: `Checkpoint <n> — <Kunde> — <Datum>`; 1 Was neu ist (max 5 Zeilen); 2 Ergebnis (Pfad/Sheet-Link); 3 Übergabe an Citations; 4 [FEHLT: …]; 5 Beleg (Script-Ausgabe, Screenshot); 6 go für Step <n+1>?

## Scripts (run, do not rewrite)

- `scripts/gap-analysis.mjs`: needs `.secrets/dataforseo.env`; writes `profile.md` and `gap.md` into `01-baseline/`.
- `uv run --with xlsxwriter python3 scripts/build_sheet.py --title "Backlink-Ziele — <Kunde>" --rows rows.csv --out <file>.xlsx`: exit 1 lists every bad row (missing Quelle/Kontakt, Säule A, unknown Status).
- `scripts/write_run.py` (`--status`, `--note`, `--result`): writes `00_project/assets/<slug>/backlink/<YYYY-MM-DD>/_run.json` at each checkpoint.

## Run procedure

- [ ] Step 0: readiness gate, read only. Weak on-page: stop and say so. Weak reviews: separate task, do not stop. Without `/backlink-dach`: stop for "go". After go: `write_run.py --status "in Arbeit" --note "Step 0"`.
- [ ] Step 1: baseline. Read `00-client-info.md` and `_status.md` in `00_project/assets/<slug>/backlinks/` (create from doc section 6 if missing). Run `scripts/gap-analysis.mjs`. Hand-over check (doc 1.4). Work local tactics RB.3-RB.9 as a full checklist.
- [ ] **Checkpoint 1:** raw baseline as plain lists (profile, gap, hand-over, local finds). No score, no Sheet. Update `_run.json`. Wait for "go" or a named correction.
- [ ] Step 2: score internally, build the CSV, `build_sheet.py` until exit 0, upload with Drive `create_file` (no `disableConversionToGoogleType`), `trash_file` the old version, screenshot in `claude-in-chrome`.
- [ ] **Checkpoint 2:** Sheet link, diff to the last version, open `[FEHLT]` list. `write_run.py --status "fertig, Freigabe offen" --result <Sheet-Link>`. Wait for "go".
- [ ] Step 3: draft outreach mails for rows with Freigabe ☑, mark "ready to send". **Checkpoint 3:** Martin or the team tick Freigabe and send manually; the agent's work on that row ends.
- [ ] Step 4 (budget > 0): buy shortlist. **Checkpoint 4:** explicit go before any money moves.
- [ ] After every step one `_status.md` line. Never overwrite a file; use `v2`, `v3`.

## Verification loop (before every "done")

1. `build_sheet.py` exit 0.
2. Check the list against `rules.md` RB.3-RB.9 and the hand-over check (both found real free targets on Hüwel that a thin pass missed).
3. Open the Sheet in `claude-in-chrome` and screenshot it.
4. Evidence goes into line 5 of the checkpoint output.

A thin list happened three times on the Hüwel pilot; run this loop before reporting any list as done.
