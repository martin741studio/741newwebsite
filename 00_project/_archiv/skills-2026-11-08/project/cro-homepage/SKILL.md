---
name: cro-homepage
description: Run the 741 CRO Homepage Workflow (Track A, the standard) for a local business: healing practices (Heilpraktiker, Physio), law firms and other local companies. Turns the current homepage or one page of a client into an approved, conversion-optimised desktop HTML prototype with a GPT mockup, a Chrome visual check, a handoff and a Drive folder. Trigger on "CRO homepage for <name>", "run the CRO workflow", "Startseite optimieren (CRO)", "homepage prototype for <practice>", "prototype for <firm>", or Martin naming a client with the URL and saying go. Do NOT use for Track B design-intense runs ("track B", showpiece, motion-heavy pitch), SEO content specs (seo-page-optimizer), review pages (local-seo-review-page), backlink work (backlink-dach), or copy for one practitioner page without a prototype (behandler-seite).
---

# cro-homepage

## Critical

1. Prototypes stay local. Never upload one to a server unless Martin asked. A hook asks for confirmation on such commands (`scripts/guard_upload.py`).
2. Never write "done" without (a) `python3 ~/.claude/skills/cro-homepage/scripts/verify.py <cro-dir>` passing and (b) the Chrome visual check line "Visual check done in Chrome, N items checked, N fixed, N open".
3. Every fact traces to `02-data/dataset.md` or carries `[FEHLT]`. Never guess a price, a duration, a title or a claim.
3a. **Step 3 copy runs through the `content-writing` skill (Martin, 2026-10-11).** Before Checkpoint 1: voice sheet from the client's live site, gate A0, SEO and GEO parts in the copy (H1 with keyword and city, answer block, FAQ from real PAA, entities, internal links, schema plan), then `python3 ~/.claude/skills/content-writing/scripts/run_gates.py <run-dir>` with G1 to G6 PASS, fresh reviewer and SEO audit. Save the report as `04-copy/gates.md`. Details: workflow doc Step 3, block "SEO, GEO and writing gates".
4. Score strictly: only 0, 1 or 2, never "2 with reservation". A score of 2 needs the scorecard's own check met. When a run has no stops (Martin waived the checkpoints), the fresh reviewer (`assets/reviewer-prompt.md`) is mandatory before the report. First test on the Adel run: 12 real gaps, 3 inflated scores.

## Run kit (scripts, templates, checks)

Copy `assets/templates/run-checklist.md` into your first reply of a run and tick it as you go. Ask the intake once (`assets/templates/intake.md`, defaults included). Use the templates in `assets/templates/` for every work file.

| Step | Run this |
| --- | --- |
| 3 copy | `python3 ~/.claude/skills/content-writing/scripts/run_gates.py <run-dir> --page <copy page>` (G1 to G6) and save the report as `04-copy/gates.md` |
| 4 design doc | `python3 scripts/check_prompt.py <prompt.txt> 04-copy/approved-copy.md` (every quoted text must exist in the approved copy) |
| 6 screenshots | serve the folder (`python3 -m http.server <free port>`), then `bash scripts/shot.sh "<url>?shot=1" 07-prototype/screenshots prototype` |
| 6b measured checks | paste `scripts/measure.js` into `javascript_tool` on the open page in Claude in Chrome; it returns M1 to M10 as JSON |
| 6b / 7 verify loop | `python3 scripts/verify.py <cro-dir> [--allow "<allowed text part>"]`. Fix every FAIL. Run again. Only report when it passes. It does not replace the visual check |
| 6c optional | fresh reviewer agent with `assets/reviewer-prompt.md` at Checkpoint 2. Fix real gaps, run `verify.py` again |
| 7 Drive | `python3 scripts/stage_drive.py <cro-dir> --version v1`, upload the `_drive/` files with the browser method (about 10 MB per call), copy the titles from the Drive listing into a text file, `python3 scripts/check_drive.py <cro-dir>/_drive/MANIFEST.json titles.txt` |
| 7 metrics | one line in `00_project/cro-registry/run-metrics.md` (minutes, Martin's corrections, score) |

`scripts/` paths are relative to this skill folder. Python for rembg, scipy and PIL: `/Library/Frameworks/Python.framework/Versions/3.10/bin/python3`.

Trigger tests and the first function test: `tests/test-scenarios.md`. Workflow score: `00_project/cro-registry/workflow-scorecard-cro.md`. Re-score after every 5 real runs.

Not enabled for Cowork or routines: `~/.claude/skills/` is not read there. Enable it in Customize > Skills on claude.ai if that is ever needed.

Step 1 row 1.0 (2026-10-11): run or reuse the content pool (skill `content-pool`, spec `00_project/content-pool-workflow.md`) before the other Step 1 rows. Rows 1.5 and 1.6 then come from the pool. Step 2 and Step 3 read `content-pool/04-pool/pool-top.md`. The sitemap is not an input.

Source of truth for the process: `00_project/cro-homepage-workflow.md`. Read it fully at the start of every run. This skill only tells you how to operate it.

## Inputs Martin gives at the trigger

1. Practice name.
2. Website URL.
3. GBP link.
4. Preferred contact channel of the practice (WhatsApp, phone, booking form) plus number or link. Ask for it if missing. It is not always WhatsApp.

Nothing else. The client fills in nothing.

## Fixed decisions (do not re-ask)

- Tools: Firecrawl, DataForSEO, GSC/GA4 only where 741 holds access, Google Drive MCP (markdown work docs only, never binary files, see below), **Claude in Chrome (external, logged-in) for every browser task including GBP/Maps reads, ChatGPT and any Drive upload** — never the Claude Code built-in browser pane (it has no logins). No Ahrefs, no Local Falcon, no Apify.
- **Binary files (images) never go through the Drive MCP tool** — it needs the full content inline and chokes on anything past a few hundred KB. To upload an image to Drive, use the browser: open the folder, click "New", then run a JavaScript click (not a real mouse click) on the "File upload" menu item to make Drive create its real file input without opening the native OS picker, find that input, and `file_upload` to it directly. Full exact steps are in `00_project/cro-homepage-workflow.md` Step 5. This is a real working path, tested, not a fallback.
- No competitor analysis. No intake form. No CMS or tracking setup work.
- All produced files in German, address form **du** unless the live site uses Sie.
- Headlines: `00_project/prompts/direct-response-copy-prompts.md`, max 3 variants per section.
- Industry mode: health practices run in HWG mode (no healing promises, no guaranteed results, no before/after framing, no fear wording; flag grey areas). Other local businesses skip the HWG items; result claims need real data in the dataset.
- Law firms: item 22 is the Anwaltswerbe-Check (BRAO § 43b, BORA § 6, UWG): no Fachanwalt title without proof, no result promises, no superlatives, no "spezialisiert" without proof, no "kostenlos" unless true. Address form Sie. Details in the workflow doc, section 1 rule 10.
- Reference site (Martin names one): Step 1.12. Crawl it in Chrome and with Firecrawl, copy the structure only into `brand.md` "Muster aus <Referenz>", motion exceptions into `07-prototype/motion.md`.
- Long GPT prompts: `pbcopy < prompt.txt`, click the composer, `cmd+v`, click "Show in text field", check length by JavaScript, send by button.
- First screen is judged at 701 px viewport height: H1, one proof line and the CTA must fit.
- Images: real photos are the reference. GPT creates the ideal images for the prototype, including people and rooms. Logo is always the real file.
- Prototype: HTML, **desktop only at 1440 px, matching the GPT mockup as closely as possible**. Mobile is not part of this workflow (Martin, 2026-10-11). Local only. Nothing goes live. Motion and highlights follow `00_project/cro-homepage-motion-spec.md` exactly (approved by Martin 2026-10-11).
- Library: `00_project/knowledge/cro-library/_derived/` (`rules.md`, `patterns.md`, `scorecard.md`). Read them, never re-pull the notebook. In client-facing files call it "741 CRO-Raster". Never name method sources.

## Drive is the resumable home (Martin, 2026-10-11)

All finalised work lives in the client's Drive folder `CRO Homepage`: every document in its current version, all images, the prototype as a zip, the final screenshots, and `_status.md`. Upload at every checkpoint and at the end of the run (workflow section 2.2, browser upload, old versions moved to `_archiv/`). To resume a run, read `_status.md` and `00-lead-info.md` and continue at the next step. Never restart at Step 0.

## Folders

- Local (source of truth): `00_project/assets/<slug>/cro/` with the subfolders from the workflow doc section 2.1.
- Drive mirror: `Local SEO/<Practice name>/CRO Homepage/` (create inside the existing client folder; new leads get `Local SEO/<Name>/` first). Upload the step's markdown and images at every checkpoint.

## Run procedure

1. Read `00-lead-info.md` and `_status.md` in the local folder. Continue from the step named as next. If the folder is missing, create it from the workflow doc.
2. Follow the workflow doc steps 0 → 7. Append one line to `_status.md` after every step. Never overwrite; use `v2`, `v3`.
3. Stop only at a failed gate and at the 2 checkpoints:
   - **Checkpoint 1** after Step 3: `04-copy/copy.md` complete, HWG check passed.
   - **Checkpoint 2** after Step 6: prototype self-check passed, screenshots at 1440 px saved.
   Step 4 (design doc) and Step 5 (one GPT reference image, no further iteration) both run
   straight through with no checkpoint (Martin, 2026-10-11). The GPT image is a layout/style
   reference only, never a copy source, the approved copy is always the source of truth for
   the prototype's text.
   At a checkpoint: give Martin the file path, a 5-line summary, and the open `[FEHLT]` list. No question lists.
4. After Checkpoint 2: write the handoff package (Step 7), append a Learnings entry to `rules.md`, set status `Übergeben`.

## Register on the Desktop (Martin, 2026-10-11)

Every new page or prototype version gets an entry in `00_project/cro-registry/registry.json` (`approved: false`). Then run `python3 00_project/cro-registry/build.py`. That rebuilds `~/Desktop/Workflow-Uebersicht.xlsx` (all workflows per client: state, last run, approval, folder links). When Martin approves a prototype, run `python3 00_project/workflow-registry/workflow_registry.py approve --cro-id <id>` in the same turn. A hook reminds you when a message sounds like an approval. Prototypes are opened locally, never uploaded to a server unless Martin asks.

## Final report always has the link (Martin, 2026-10-11)

End every run and every delivered change with the direct Drive link to the folder (or file) and send the full-page screenshot of the prototype with `SendUserFile`, so Martin can open it straight away.

## Visual check (mandatory, Martin 2026-10-11)

Before reporting that a prototype is done, open it in Claude in Chrome, scroll top to bottom at 1440×900, and work through every item in `00_project/cro-homepage-visual-check.md`. Fix what is wrong, check again, write `07-prototype/visual-check.md`. The report to Martin must contain the line "Visual check done in Chrome, N items checked, N fixed, N open". Never write "done" without it. This also applies after any later edit of the prototype.

## Quality gates to self-check before every checkpoint

- Every fact traces to `02-data/dataset.md` or carries `[FEHLT]`.
- Copy gates G1 to G6 passed and `04-copy/gates.md` exists (SEO, GEO, HWG or BRAO, facts, style, slop).
- Every scorecard score of 0 or 1 has an evidence line.
- Every copy section has: job line, headlines (≤3, one recommended), body, CTA text, prefilled message.
- Every GPT prompt starts with the global style block.
- Prototype: CTA in the first screen at 1440 px, body ≥ 16 px, live text only, matches the mockup section by section, verified by screenshot in rendered state.

## Assets (Martin, 2026-10-11)

- **Start of run (Step 1.11):** download the logo in every variant at its largest size, plus all usable real photos at full resolution, into `01-input/`, and write `01-input/INVENTORY.md`.
- **After the final mockup (Step 5b):** generate high-resolution single images, one fresh ChatGPT chat per image, into `06-gpt-assets/images/`. Never use crops of the mockup as page images. Upload to Drive with the browser method.

## ChatGPT operation (Step 5)

Use Claude in Chrome in Martin's logged-in ChatGPT session. Full exact procedure is in `00_project/cro-homepage-workflow.md` Step 5, follow it precisely: fresh chat, attach reference photos AND the real logo files together, verify thumbnails appear, High effort, ONE message with the complete style block plus every section's exact copy from `approved-copy.md` (no blank lines in the typed text), verify the composer before sending, download from the lightbox. Never send a follow-up edit message in the same thread, start a new chat instead if a redo is needed. After download, verify the saved file actually matches what was shown in the chat (open and look, don't assume), then deliver it to Martin and name the Drive folder for him.

## Registry: automatic (2026-10-11)

The overview Excel `~/Desktop/Workflow-Uebersicht.xlsx` updates itself. A Stop hook runs `workflow_registry.py sync --quiet` after every turn. You do not call `upsert` for normal progress. Step 7 writes the line `Step 7 done` into `_status.md` of the page folder. `sync` picks up pages without a `cro-registry` entry. Pages with an entry stay manual.
For any other file layout, write `_run.json` in the run folder (schema in `00_project/workflow-registry/README.md`). Only the approval stays manual: when Martin approves a result, run `approve` in the same turn and say that the Excel is updated.

## Martin guide (2026-10-12)

The 741 character Martin points out the one thing per section the reader must not miss. Rules, poses, markup and the inline helper: `00_project/assets/brand/martin-guide/README.md`. In this workflow: only in the presentation wrapper around the prototype. Never inside the prototype markup. Max 1 callout per section, bubble text in first person and plain language, every number with source and date, check desktop and mobile with a screenshot.
