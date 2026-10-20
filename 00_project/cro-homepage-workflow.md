# CRO Homepage Workflow – Local Businesses, Healing Practices first (v2)

Stand: 2026-10-11 · Owner: Martin · Runner: Claude Code (this repo)
Replaces the draft from 2026-10-10. Decisions from the priming session are applied.

---

**Table of contents**

- [0. Purpose and outcome](#0-purpose-and-outcome)
- [1. Operating rules](#1-operating-rules)
- [2. Storage](#2-storage)
  - [2.1 Local working folder (source of truth)](#21-local-working-folder-source-of-truth)
  - [2.2 Drive folder: the complete, resumable home of a run (Martin, 2026-10-11)](#22-drive-folder-the-complete-resumable-home-of-a-run-martin-2026-10-11)
  - [2.3 Folder rules](#23-folder-rules)
- [3. One-time setup: the CRO library](#3-one-time-setup-the-cro-library)
- [4. The run](#4-the-run)
  - [Step 0 — Readiness gate](#step-0--readiness-gate)
  - [Step 1 — Data collection → `02-data/dataset.md`](#step-1--data-collection--02-datadatasetmd)
  - [Step 2 — Diagnosis and ideal outcome → `03-diagnosis/diagnosis.md`](#step-2--diagnosis-and-ideal-outcome--03-diagnosisdiagnosismd)
  - [Step 3 — Copy → `04-copy/copy.md` → **Checkpoint 1**](#step-3--copy--04-copycopymd--checkpoint-1)
  - [Step 4 — Design data and GPT design doc → `05-gpt-design-doc/design-doc.md` → no checkpoint](#step-4--design-data-and-gpt-design-doc--05-gpt-design-docdesign-docmd--no-checkpoint)
  - [Step 5 — GPT image generation → `06-gpt-assets/` → no checkpoint](#step-5--gpt-image-generation--06-gpt-assets--no-checkpoint)
  - [Step 5b — High-resolution image assets → `06-gpt-assets/images/` → no checkpoint](#step-5b--high-resolution-image-assets--06-gpt-assetsimages--no-checkpoint)
  - [Step 6 — HTML prototype → `07-prototype/index.html` (a rebuild goes to `07-prototype/v2/`, never overwrite) → **Checkpoint 2**](#step-6--html-prototype--07-prototypeindexhtml-a-rebuild-goes-to-07-prototypev2-never-overwrite--checkpoint-2)
  - [Step 7 — Handoff package → `08-handoff/handoff.md`](#step-7--handoff-package--08-handoffhandoffmd)
- [4b. Other page types (first used for the Über-mich page, 2026-10-11)](#4b-other-page-types-first-used-for-the-über-mich-page-2026-10-11)
- [5. Templates](#5-templates)
- [6. Decisions on the open points](#6-decisions-on-the-open-points)
- [7. Sequence of first use](#7-sequence-of-first-use)

---

## 0. Purpose and outcome

The workflow turns the current homepage of a local healing practice into an approved, optimised homepage prototype. The prototype is built to turn local visitors into WhatsApp contacts. It is a sales artifact for leads and a bonus for clients. It is not a paid deliverable for now.

The output is a clickable HTML prototype plus a handoff package. The rebuild of the live site runs in a separate workflow.

**Done (all must be true):**

1. Every scorecard item is scored 2, or has a written reason why it does not apply.
2. On a 1440 px desktop viewport, the primary CTA is visible in the first screen without scrolling.
3. The CTA repeats at least every 2 sections.
4. The first 3 sections answer: who it is for, what helps, how the first visit works, where the practice is, why to trust the practitioner.
5. Every claim, price and credential traces to `02-data/dataset.md`. Nothing is invented. Gaps carry the flag `[FEHLT]`.
6. Zero healing promises. The HWG check passed.
7. Martin approved all 3 checkpoints.

---

## 1. Operating rules

1. Martin triggers a run with: practice name, website URL, GBP link, and the preferred contact channel of the practice (WhatsApp, phone, booking form). The channel is asked per client before the run. It is not always WhatsApp. The doc says "WhatsApp" as the default example.
2. The runner is Claude Code in `~/martindrendel/741website`. The skill is `cro-homepage` (written after Martin confirms this doc).
3. Tools: Firecrawl (scrape, screenshots), Claude in Chrome (screenshots, GBP read-out), DataForSEO (keywords), Google Search Console and GA4 via the 741 service account where 741 holds access, Google Drive MCP (work docs), Claude in Chrome (ChatGPT image generation, NotebookLM export). No Ahrefs. No Local Falcon. No Apify.
4. Language: all produced files are German. The address form is **du**, unless the brand uses Sie on its live site.
5. The agent stops only at the 3 checkpoints and at a failed gate. Between checkpoints it runs without asking. Checkpoints: copy (Step 3), GPT images (Step 5), prototype (Step 6). The design doc (Step 4) runs straight through with no approval.
6. The client fills in nothing. All facts come from the live site, the GBP, and existing 741 portal data. One exception: the content pool (row 1.0) may write a short German client form for open facts. It is a draft. Martin decides if and when it goes out.
7. Competitors are analysed only through the content pool (Step 1, row 1.0). They show what visitors expect and where the gap is. They are never a design reference and never a text source. The target for the layout is the ideal outcome from the CRO library.
8. Method sources are never named in client-facing files. The library is called "741 CRO-Raster".
9. Nothing goes live from this workflow. The prototype stays local. The rebuild is a separate decision.
10. **Industry mode.** The workflow is built for local healing practices first, but it works for any local business. Health practices run in HWG mode: no healing promises, no before/after, no fear wording (rules L8/L9, scorecard item 22). Other industries skip the HWG items. Result claims are then allowed when the dataset backs them with real data.
    **Lawyers (law firms):** scorecard item 22 becomes the **Anwaltswerbe-Check** (BRAO § 43b, BORA § 6, UWG). Never write "Fachanwalt/Fachanwältin" unless the Kammer title is proven (a Fachanwaltslehrgang is not the title: use the exact wording of the client and "Interessenschwerpunkt"). No result promises, no superlatives, no "spezialisiert" without proof, no "kostenlos" unless true, no price claims. Client quotes only about communication and way of working, cut result parts with [...]. Practice areas the client does not prove (for example criminal law) stay out. Write a conflict table in the dataset for every claim on the live site that breaks this.
11. **Run tooling (2026-10-11).** The skill folder `~/.claude/skills/cro-homepage/` holds scripts for the repeatable checks (`verify.py`, `measure.js`, `check_text.py`, `check_prompt.py`, `shot.sh`, `stage_drive.py`, `check_drive.py`), templates for every work file, an optional fresh-reviewer prompt and an upload guard hook. Use them. The visual check in Chrome (Step 6b) stays manual.

---

## 2. Storage

### 2.1 Local working folder (source of truth)

```
00_project/assets/<slug>/cro/
  00-lead-info.md        name, practitioner, website, CMS, GBP link, contact channel, source, status
  _status.md             run log: one line per step (date · step · output file · next step)
  01-input/              logo (every variant, largest version), real photos at full resolution, INVENTORY.md
  02-data/               dataset.md, brand.md, scrapes, screenshots, keywords, reviews
  03-diagnosis/          diagnosis.md (scorecard + gaps + ideal-outcome plan)
  04-copy/               copy.md (v1, v2 …), approved-copy.md
  05-gpt-design-doc/     design-doc.md (global style block + section prompts)
  06-gpt-assets/         full-page mockup(s); images/ = high-resolution single images for the prototype, with SLOTS.md
  07-prototype/          index.html + assets/, self-check.md, visual-check.md, screenshots/. A rebuild goes to v2/ (v1 stays).
  08-handoff/            handoff.md, before-after-score.md
```

`<slug>` = lowercase practice name, e.g. `dumann`.

The content pool and the sitemap live next to this folder in `00_project/assets/<slug>/content-pool/` (own Drive folder `Content Pool`). This folder only links to the pool. The sitemap is saved there as its own output (`05-sitetree/`, `05-report/content-pool-sitetree.html`).

### 2.2 Drive folder: the complete, resumable home of a run (Martin, 2026-10-11)

Drive folder: `Local SEO/<Practice name>/CRO Homepage/` inside the existing client folder. A new lead gets `Local SEO/<Practice name>/` first, same pattern. No separate `Leads` folder exists; Martin decides if one should.

**The Drive folder holds all finalised work of the run.** Anyone can open it later and continue from where the run stopped, without the local computer. It contains:

- Every work document, current version, flat names with the step number in front: `00-lead-info.md`, `_status.md`, `01-input-INVENTORY.md`, `02-data-dataset.md`, `02-data-brand.md`, `03-diagnosis.md`, `04-copy-approved.md`, `05-gpt-design-doc.md`, `06-gpt-assets-SLOTS.md`, `07-prototype-self-check.md`, `07-prototype-visual-check.md`, and later `08-handoff.md`.
- All images: the final mockup and every image of `06-gpt-assets/images/`.
- The prototype as one zip file (`07-prototype-<version>.zip` with `index.html` and `assets/`) and the final screenshots (`07-prototype-<version>-screenshot-full.png` and `...-first-viewport.png`).

**When the agent uploads:** at every checkpoint, and again at the end of the run, so the folder always matches the local folder. `_status.md` is part of the upload, so the Drive folder always shows the next step.

**How the agent uploads:**
- Markdown, zip and images go through the browser (Claude in Chrome) with the upload method in Step 5. The Drive tool cannot replace file content, and it must never carry binary files.
- An older version of a document is not deleted and not overwritten. The agent moves it into the subfolder `_archiv/` (create it once) and uploads the current version under the normal name. Moving needs the Drive tool: `update_file` with the new `parentId`.
- Upload in calls of at most about 10 MB each.

**Resuming a run** (in a new session, or after a break): read `_status.md` and `00-lead-info.md` first, from the local folder if it exists and otherwise from the Drive folder. Continue at the step named as next. If the local folder is missing, download the Drive files first (`07-prototype-<version>.zip` unpacks to the prototype). Never start the run again from Step 0.

### 2.3 Folder rules

1. At run start, read `00-lead-info.md` and `_status.md`. Continue from the step named as next. If the folder does not exist, create it.
2. After every step, append one line to `_status.md`.
3. Never overwrite. Revisions get `v2`, `v3` next to the original.
4. Status values in `00-lead-info.md`: `Lead → Daten erfasst → Copy freigegeben → Design-Daten freigegeben → Bilder freigegeben → Prototyp freigegeben → Übergeben`.

---

## 3. One-time setup: the CRO library

Source: NotebookLM notebook "Landingpages CRO" `7feaa152-c4dd-43cf-984f-3b65bf1769eb` (Martin's video knowledge base on homepage optimisation). This replaces the YouTube pull from the draft.

**Status: exported 2026-10-11.** 65 of 66 sources in `00_project/knowledge/cro-library/` (source 26 has no content in the notebook). The export method is documented in the memory `cro-library-local`.

**Export (same method as the Hormozi library):**

1. Open the notebook through Claude in Chrome. Read each source with the `source-viewer`. Save one Markdown file per source to `00_project/knowledge/cro-library/`, with `INDEX.md`.
2. Timers in background tabs are throttled. Use the MessageChannel yield and ~30 s chunks per JavaScript call, as documented in the Hormozi export memory.

**Derive three files in `00_project/knowledge/cro-library/_derived/`:**

| File | Content |
| --- | --- |
| `rules.md` | Every principle as an if/then rule, with source file and timestamp. SaaS and e-commerce-only rules are dropped. Local rules are added: city in the hero, practitioner face early, first-visit steps, Google rating, map and parking, WhatsApp as primary CTA, HWG limits. |
| `patterns.md` | At least 5 example page layouts described section by section: hero layout, trust strip, section rhythm, CTA design, typography hierarchy. |
| `scorecard.md` | 15–25 items, each with "how to check" and score 0/1/2. Priority A/B/C marked per item. |

**Status 2026-10-11:** the three derived files exist in `_derived/` (rules.md with 100+ rules in 12 groups plus 10 local rules, patterns.md with the blueprint and 10 patterns, scorecard.md with 22 items). The raw per-group extracts are kept in `_derived/extracts/` as evidence.

**Gate:** Martin approved the three derived files on 2026-10-11. Later runs only read them.

**Update rule:** After each prototype, the agent appends a short "Learnings" entry to `rules.md`. A rule that fails on 2 or more clients gets reviewed.

---

## 4. The run

### Step 0 — Readiness gate

| Input | Required | Check |
| --- | --- | --- |
| Website URL | Yes | Loads over https. CMS detected and noted. |
| GBP link | Yes | Resolves. Name, category, rating, review count readable. |
| Preferred contact channel + number/link | Yes | Martin names it at the trigger. If unknown: note `[FEHLT: Kontaktkanal]`, use a placeholder, list it in the handoff. |
| Logo and colours | Yes | If no brand files: extract from the live site and flag it. |
| Real photos | Recommended | Pull from site and GBP. If none: placeholders plus a shoot list in the handoff. |
| GSC / GA4 | Optional | Use only if 741 holds access. Otherwise skip. No setup work in this workflow. |

**Gate:** All required rows filled or flagged → go to Step 1. Otherwise stop and list what is missing.

### Step 1 — Data collection → `02-data/dataset.md`

| # | What | Tool | Output |
| --- | --- | --- | --- |
| 1.0 | **Content pool.** Run or reuse the content pool of this client: competitors, search demand, own search data and a ranked list of content items in four pillars (location, main service, brand, authority). Reuse it when `00_project/assets/<slug>/content-pool/04-pool/pool.json` is not older than 30 days and the checkpoint "go" is recorded. Otherwise run the skill `content-pool` first (spec: `00_project/content-pool-workflow.md`). It can also run alone, before this workflow starts | Skill `content-pool`; output stays in `content-pool/`, it is not copied | `content-pool/04-pool/pool.json`, `pool-top.md`, link in `dataset.md` |
| 1.1 | Current homepage: full text, section order, CTAs, images, alt texts, title, description, H1 | Firecrawl scrape (markdown + links) | Section-by-section map |
| 1.2 | Screenshots desktop 1440 px, full page | Claude in Chrome | PNG files in `02-data/` |
| 1.3 | Desktop first-screen check: is the first CTA visible, broken layout, text under 16 px | Claude in Chrome | Numbers and notes |
| 1.4 | Site structure: all pages, which ones get traffic | Firecrawl map; GSC pages if available | Page list |
| 1.5 | Search demand: top 15 keywords "[Leistung] [Stadt]" with volume | **From the content pool (row 1.0):** pool items with their volumes, autocomplete and People Also Ask evidence. Run the old DataForSEO calls only if no pool exists | Keyword table, copied from the pool with the item IDs |
| 1.6 | Current rankings of the homepage | **From the content pool (row 1.0):** own ranked keywords and GSC queries and pages (`03-demand/`). Run the old calls only if no pool exists | Ranking table |
| 1.7 | GBP facts: rating, review count, categories, hours, photos | Built-in browser on the GBP / Maps page | GBP block |
| 1.8 | Review language: all Google reviews of the practice | Built-in browser, Maps reviews tab, scroll to end | Raw reviews + top 10 phrases for problem and result |
| 1.9 | Existing 741 data: portal texts, NAP record, earlier page drafts, reports | Supabase 741-portal, memory, `00_project/assets/<slug>/` | Links and extracted facts |

**1.10 Brand → `02-data/brand.md`**

- Colours: primary, secondary, background, CTA, as hex.
- Typography: fonts or closest Google Fonts match, headline and body weights.
- Logo: file and placement rules.
- Imagery style: light/dark, warm/cool, natural/studio, with/without people.
- Shapes and textures: corners, organic/geometric, recurring textures.
- Mood words: 3–5 words.
- Real photo inventory: every usable photo with a one-line description and source URL. Every photo is opened and viewed before it enters the inventory. These photos are the reference for the GPT images in Step 5.

**1.11 Asset download → `01-input/` (Martin, 2026-10-11).** The prototype build needs the real files, not screenshots of them. At the start of every run, download into `01-input/`:

- **The logo, every variant** (wordmark, icon, favicon, social avatar), each in its largest available version. If the site only serves a thumbnail, look for the original (for Wix sites: remove the `/v1/fill/...` resize suffix from the media URL to get the original file). If only a small version exists, flag `[FEHLT: Logo-Original]` and ask Martin for the source file.
- **Every usable real photo** from the website and the GBP, at full resolution, not the compressed thumbnails.
- **`01-input/INVENTORY.md`:** one row per file with file name, source URL, pixel size, and a one-line description of what the picture shows.

Step 5 attaches the logo and photos from here, Step 6 builds with them.

**Gate:** All 10 rows (1.0 to 1.9) filled and 1.11 done (logo in `01-input/` at 800 px or more on the long side, or flagged). A row with no data gets "keine Daten, Grund: …". Never empty.

**1.12 Design reference site (only when Martin names one, 2026-10-10).** Open the reference in Claude in Chrome at 1440 px, scroll the whole page and take screenshots, read the section list and the computed styles (H1 size, button radius) with `javascript_tool`, and scrape the HTML with Firecrawl (`formats: markdown, html, branding`; the result can exceed the output limit, then read it with `jq`). Write the elements into `02-data/brand.md` under "Muster aus <Referenz>": layout, button shapes, headline treatment, section types, motion. Copy structure only, never text, images or brand marks. The client's own colours, fonts and content stay. The GPT global style block names the reference site and each element. Motion elements that break the motion spec (loops, colour scroll effects) go into `07-prototype/motion.md` with the reason and the allowed replacement (rotation only on hover, brightness by opacity, one-time line draw).

### Step 2 — Diagnosis and ideal outcome → `03-diagnosis/diagnosis.md`

Pool input (row 1.0): `content-pool/04-pool/pool-top.md` lists the content items per CRO row, best first (A, B, C), with the `[FEHLT]` facts and the HWG notes. Use it when you write the one line per section in item 4. Items with the status `needs_client` stay drafts. The pool never removes one of the 10 rows. The sitemap is a separate output of the content pool and is not an input here.

1. **Score the current homepage** with `scorecard.md`. Each item gets 0, 1 or 2 plus one line of evidence (quote, screenshot name, number).
2. **List the gaps:** every item with 0 or 1.
3. **Rank the fixes** by impact on contacts through the client's primary channel (WhatsApp, phone or booking form):
   - Priority A: hero, CTA, first-visit clarity, trust above the fold.
   - Priority B: proof, offer, location.
   - Priority C: everything else.
4. **Ideal-outcome plan:** pick the layout pattern from `patterns.md` that fits the brand. Write the target section order with one line per section on its job. **Default order is the full P0 blueprint from `patterns.md`, 10 sections, not a shortened list:**
   1. Hero: visitor's problem and outcome, city, practitioner photo, primary CTA, Google rating.
   2. Beweis-Leiste: a second, short proof placement right after the hero (big rating, one highlighted quote), separate from the full review section lower down. This row is the one most often dropped, it does not repeat, it is a compact appetiser for the full review wall in row 7.
   3. "Ist das etwas für mich?": 3–5 complaints the practice works with.
   4. Leistungen: cards, each linked to its service page.
   5. Der erste Termin: 3–4 steps, duration, price.
   6. Über die Behandlerin: photo, credentials, why she does this work.
   7. Bewertungen: Google rating and selected reviews, within HWG limits.
   8. FAQ: Kosten, Krankenkasse, Vorbereitung, Absage.
   9. Standort: map, address, parking, hours.
   10. Abschluss-CTA: primary channel, phone as secondary.
5. **Fact gaps:** every fact the plan needs but the dataset lacks → `[FEHLT: …]` list for Martin.

**Gate:** Every 0 or 1 score has an evidence line. Any score without evidence is redone. **Section-coverage check (Martin, 2026-10-11, added after a real miss on the Dumann run):** before Step 3 starts, the agent lists the 10 P0 rows from `patterns.md` against the ideal-outcome plan above, one line each, either "included as section N" or "deliberately dropped, reason: …" (a reason grounded in real data or the niche, e.g. "no comparison table, no real competitor data and a comparison reads as salesy for a solo practitioner"). A row silently missing, with no explicit drop reason, fails this gate and the plan is redone. This check is mandatory on every run, not a one-off fix.

### Step 3 — Copy → `04-copy/copy.md` → **Checkpoint 1**

Inputs: `dataset.md`, `diagnosis.md`, `rules.md`, review language (1.8), `content-pool/04-pool/pool-top.md` (the homepage items per row; write the A items first), the 741 headline prompt file `00_project/prompts/direct-response-copy-prompts.md`, the HWG guideline. If an approved 741 page text exists for the homepage, it is an input and gets rewritten with the CRO rules.

**SEO, GEO and writing gates (Martin, 2026-10-11). Mandatory for Step 3.** The copy is written through the `content-writing` workflow (skill `~/.claude/skills/content-writing/`, spec `00_project/content-writing-workflow.md`). The 10 rows of the P0 blueprint are the homepage template of that workflow (IDs S00 to S10). Do this, in this order:

1. **Rules and voice.** Read `references/copy-rules.md`, `seo-geo-rules.md`, `legal-rules.md` and `fact-rules.md` of the skill. Build or reuse the client voice sheet from the client's live website (`assets/<slug>/voice.md`).
2. **Gate A0 (homepage = money page, full).** Bestand text counted by script, benchmark of local competitor homepages (the content pool holds it), real PAA, autocomplete. A row without a source stops the step.
3. **Required SEO and GEO parts of the homepage copy.** One H1 with the primary keyword and the city. Title up to 60 and meta up to 155 characters. A direct-answer block of 2 to 4 sentences near the top (it may sit in the hero as `hero+answer`). FAQ row from real PAA, the client's own FAQ kept. Named entities (method, city, nearby areas). Internal links to every service page in the Leistungen cards. Person block with proven credentials. Local texture from a verified fact. Technical block with the schema plan (business type, FAQPage, Person, BreadcrumbList).
4. **Write, then run the gates.** `python3 ~/.claude/skills/content-writing/scripts/run_gates.py <run-dir>` must pass G1 facts, G2 legal (HWG or BRAO), G3 SEO and structure, G4 style (no dashes, one address form), G5 slop (German lint, rival-model cleanse, claim diff) and G6 coverage (subtopics, entities, statutes, PAA, schema, link network). Then a fresh reviewer, and an SEO audit with the `seo-page-optimizer` rubric.
5. **Evidence.** Save the gate report as `04-copy/gates.md` (result line `Result: **PASS**`). The verify script checks this file for runs started on or after 2026-10-12.
6. **Mapping.** The CRO fields (up to 3 headline variants per section, CTA text, channel prefill) stay in `copy.md`. The page wording in `05-final/page.md` of the content-writing run is the source of the body text. After Checkpoint 1 `approved-copy.md` carries exactly that wording.

Per section the agent delivers:

- the section's job in one line;
- up to 3 headline variants, one marked as recommended;
- body copy;
- CTA text and the prefilled message for that section (WhatsApp prefill, or the equivalent for the client's actual channel).

Plus: title tag (max 60 characters), meta description (max 155), H1 with primary keyword and city.

**Every one of the 10 sections from the Step 2 section-coverage check gets written, including the Beweis-Leiste.** `copy.md` is not considered complete with 9 sections unless Step 2 explicitly recorded why a 10th row was dropped.

**HWG check before the checkpoint** (the G2 gate runs it by script; the lawyer variant is the BRAO check): no healing promises, no guaranteed results tied to conditions, no before/after framing, no fear wording. Grey areas are flagged for Martin.

**Brief (top of `copy.md`):**

```markdown
# Brief — <Praxis> Startseite
Conversion-Ziel: WhatsApp-Nachricht — Vorbelegung: "…"
Besucher: <wer> sucht <Keywords> mit <Problem in Bewertungssprache>
Einwände → Antworten: 1. … → … 2. … → … 3. … → …
Beweise: <Bewertung> / <Anzahl> Bewertungen · <Qualifikation> · <Jahre>
Lokal: <Stadt, Bezirk, Parken, ÖPNV>
Keywords: primär <…> · sekundär <…>
Sektionsreihenfolge: 1… 9…
Stimme: <…>
Nicht: HWG-Liste · keine erfundenen Fakten · keine Stock-Personen · ein primärer CTA
```

**Checkpoint 1 — Martin approves the copy and picks the headlines.**

- Approved → `approved-copy.md`, status `Copy freigegeben`, go to Step 4.
- Changes → revise only the named sections, save as `copy-v2.md`.
- After 2 rounds without approval → stop and ask for a 20-minute call.

### Step 4 — Design data and GPT design doc → `05-gpt-design-doc/design-doc.md` → no checkpoint

Runs straight through from the approved copy to the first GPT image. Martin decided (2026-10-11) that the design doc itself needs no separate approval; the first real checkpoint after copy is Checkpoint 2, once the GPT images exist.

Inputs: `approved-copy.md`, `brand.md`, the pattern chosen in Step 2.

**Doc structure:**

1. **Global style block** (pasted at the top of every GPT prompt): brand colours as hex, fonts, mood words, imagery style, chosen layout pattern, image format rules.
2. **One prompt per section**, in page order: layout pattern, exact headline and CTA text, where the real photo goes, background and texture, spacing.
3. **Full-page prompt:** the whole homepage as one tall reference image.
4. **Image rule:** the real photos are the reference. GPT creates the ideal images for the prototype, including people and rooms, in the look of the real practice. This is part of the improvement. The handoff lists a shoot list so the client can replace them with real photos later. Do-nots: no stock-photo look; no generated text as final copy; one CTA colour only.

**Image format rule:** ChatGPT returns fixed sizes. Sections are generated portrait 1024×1536. The full page is a stitched reference, not a 1440 px export. Text in images is a placeholder; `approved-copy.md` stays the source of truth.

**Gate:** Every section in `approved-copy.md` has a prompt. Every prompt contains the global style block. No Martin approval needed, go straight to Step 5.

### Step 5 — GPT image generation → `06-gpt-assets/` → no checkpoint

The agent runs ChatGPT through Claude in Chrome in Martin's logged-in session.

**Default (Martin, 2026-10-11): one full-page image, one message, done.** Generate the
whole homepage as one tall reference image from a single, complete prompt. No
section-by-section prompts, no draft rounds, no follow-up edit messages in the same
thread (ChatGPT's edit flow on a prior image has repeatedly stalled at 95–98% and
cancelled itself, see Learnings below). If a redo is needed, start a fresh chat and send
one new complete message, never a follow-up on the old one.

**Exact procedure, tested and confirmed working on the Dumann run:**

1. Start a **brand new chat** (full page navigation to `chatgpt.com`, not just the
   sidebar "New chat" button, which can leave a stale composer draft or land in "Work"
   mode instead of "Chat" mode — always check the top toggle shows "Chat" selected).
2. Attach the real reference images first (`Attach photos` in the composer), confirm
   with a screenshot that thumbnails actually appear before typing anything. If no
   thumbnail appears, the upload silently failed, re-find the attach button fresh and
   retry rather than typing into a broken composer. **Attach both the practitioner
   reference photos AND the real logo files** (icon + wordmark from `01-input/`), not
   photos alone. Say so explicitly in the prompt text, e.g. "the attached logo files
   are the real brand logo, reproduce this exact logo in the header, do not invent a
   different one." Without this the model draws its own invented logo text instead of
   the client's real mark (seen on the Dumann run, fixed from the next run on).
3. Set image effort to **High** (the effort slider next to the model row).
4. Type **one single message with everything in it**, as one block with no blank-line
   paragraph breaks (a literal blank line in this composer can submit the message
   early, mid-type, while a response is already streaming): the global style block
   (colours, fonts, mood, layout pattern), AND every section's exact headline, body
   text, CTA label, FAQ question and answer, review quote, in full, not shortened,
   taken verbatim from `approved-copy.md`. This is the same content that used to be
   split into "design doc" and "copy", sent together in one go.
5. Verify with a screenshot that the composer shows the full text intact and the
   photos are still attached, then click the send button explicitly (do not rely on
   the Enter key for a long multi-paragraph message).
6. Wait for completion (High effort takes 1–2 minutes on a 10-section page). Open the
   full image in the lightbox and download it from there.
7. Download to `06-gpt-assets/`, named `full-page-v<n>-final.png` once approved.

**Drive upload, mandatory step (Martin, 2026-10-11): the final approved GPT image
always goes into the client's Drive CRO folder, every run, not just on request.**
Do this through the visual browser (Claude in Chrome). **Never use the Drive MCP
tool for images or any binary file** — it needs the full content inline as one
literal parameter value, which is impractical past a few hundred KB. The MCP tool
stays for the markdown work docs only (rule 2.2).

**Tested, working procedure for the browser upload (2026-10-11):** clicking Drive's
"File upload" menu item with a normal trusted click opens a native macOS file picker
that no tool can see or interact with — don't do that. Instead:

1. Open the Drive folder, click "New" to open the menu.
2. Run a JavaScript click on the menu item instead of a real mouse click:
   `[...document.querySelectorAll('[role=menuitem]')].find(e =>
   e.innerText.trim().startsWith('File upload')).click()`. An untrusted,
   script-dispatched click cannot open the native OS picker (browsers block that for
   security), but it still makes Drive create its real `<input type="file">` in the
   DOM and does not block anything.
3. `find` with a query like "hidden file input element" to get that input's ref
   (it only exists after step 2, there is none on the page before).
4. Call `file_upload` with that ref and the local file path. Drive's own "Uploading…"
   toast appears and the file lands in the current folder, confirmed by a green
   "upload complete" checkmark.
5. If step 2 or 3 ever stops finding the input (Google can change this), fall back to
   delivering the file to Martin with `SendUserFile` and naming the Drive folder, but
   try the steps above first — they are the real, working path, not a last resort.

**Learnings from the Dumann run (2026-10-11):**
- A multi-paragraph `type` action with blank lines between sections can trigger an
  early send after the first paragraph in this composer; the rest of the text then
  sits unsent in the box. Avoid blank lines in the typed message, or verify with a
  screenshot before sending.
- ChatGPT's chained "edit this image" follow-ups in the same thread (recognisable by
  "Interpreted the edit" appearing above the generation) have repeatedly stalled at
  95–98% and self-cancelled ("Image generation stopped"), even after "Try again". A
  fresh, complete, single-message generation in a new chat does not have this problem
  and should be preferred over iterative follow-ups.
- A very long prompt (about 12,000 characters, whole page copy) typed with the `type` action makes the page busy for about 1 to 2 minutes, and the tool reports a timeout and screenshots fail meanwhile. The typing still completes. Wait, then check with `javascript_tool` that the composer text length equals the prompt length and ends with the last words (`document.querySelector('#prompt-textarea').innerText`). Then find the Send button with `find` and click it. Do not retype.
- **Fast prompt insertion (2026-10-10, tested):** write the prompt to a file, run `LC_ALL=en_US.UTF-8 pbcopy < prompt.txt`, click the composer, press `cmd+v`. ChatGPT turns a long paste (about 15,000 characters) into a chip "Pasted text" within seconds, no freeze. Click "Show in text field" on the chip, then check the length with `javascript_tool` (`document.querySelector('#prompt-textarea').innerText.length` must equal the file length), then find the Send button and click it. This replaces the slow `type` action.
- The "+" menu's "Add photos & files" item can trigger a native OS file picker that
  the agent cannot see or interact with; use the dedicated "Attach photos" file input
  instead, found fresh via `find` right before uploading (a stale element reference
  from an earlier screenshot can silently fail to attach).

Martin decided (2026-10-11) that once the brief is solid, one good full-page image is
enough and needs no separate approval round, the agent proceeds straight to Step 6. Status
goes to `Bilder freigegeben` and the build uses the image only as a layout/style reference,
never as a copy source, the approved copy stays the source of truth for every word on the
prototype.

**Standing rule (Martin, 2026-10-11): the single GPT prompt carries the FULL content of
`approved-copy.md`, not a shortened version.** Every headline, every body paragraph, every
step description, every FAQ question AND its answer, every review quote in full, the full
address block, all nine sections in full text, not abbreviated labels. The goal is one
image that is as close as possible to the finished page, generated once, with no
in-between draft rounds and no section-by-section pass. If the first image still misses
real content, the fix is a fuller prompt, not a second round of smaller images.

### Step 5b — High-resolution image assets → `06-gpt-assets/images/` → no checkpoint

**Why (Martin, 2026-10-11):** crops cut out of the full-page mockup are only about 100 to 330 px wide and look soft when the prototype shows them larger. The mockup is the design reference, not the image source.

Run this after the final mockup exists:

1. **Read the final mockup in detail and list every image slot (Martin, 2026-10-11).** Open the final mockup at full size and zoom into each section. Write `06-gpt-assets/images/SLOTS.md` with one row per image the prototype must show: section number, what the picture shows, shape and display size at 1440 px (for example 480×320 card), and the decision. The decision is one of three:
   - **Real:** a photo from `01-input/` fits the slot in subject, colour and light. Use it, even if the mockup shows a different picture. A real photo that clashes with the other images (for example a cold blue photo among warm ones) does not fit: choose Regenerate.
   - **Regenerate:** no real photo fits. Make a clean high-resolution version of what the mockup shows (step 2).
   - **None:** the slot is a logo, icon or text. Use the real logo file or live HTML.
   Include the hero portrait, card photos, second portraits, room or entrance photos, and decorative botanicals or icons. A slot missing from the list will later show a soft crop, so check the list against every section of the mockup before you go on.
   **Gate:** the prototype build (Step 6) does not start until every slot has a file in `06-gpt-assets/images/` or `01-input/` and a row in SLOTS.md.
2. **One fresh chat per image.** Never a follow-up in the mockup thread: edit follow-ups stall at 95 to 98 percent (see Step 5 learnings). Attach the final mockup (it shows style and slot), the practitioner reference photos if she appears in the image, and the logo only if it appears. Send one single message: the subject of this one image, "same style, light and colours as the attached mockup", the practitioner likeness rule if she appears, "photograph only, no text, no UI, no logo, no frame", the format (landscape 1536×1024 for card and wide images, portrait 1024×1536 for portraits, square 1024×1024 for icons and textures), High effort.
3. **Download each from the lightbox** and name it `06-gpt-assets/images/<nn>-<section>-<subject>.png`, with `<nn>` the section number in the mockup. Open every file and check it: the long edge is at least 1024 px and the content is right.
4. **Size rule:** a prototype image must be at least the size it is shown at on a 1440 px screen. A GPT image at 1024 px or more satisfies this for card and portrait slots.
5. **Run several chats at once:** one browser tab per image, up to three at a time, is faster and works. If an upload to the composer fails with a lost connection, find the file input again and upload again, then check that the thumbnail shows before sending. After the download, copy (never move) the file into `06-gpt-assets/images/`.
   **Likeness when the only real photo is unusable (2026-10-10):** if the real photo hides the face (sunglasses) or is a private holiday photo, attach the final mockup first (its person is the face of the page) and the real photo second as reference for hair, build and skin tone. Write "she must NOT wear sunglasses". Every person image of the page then shows the same woman as the mockup. Record in the handoff that the face is invented and a real portrait is needed.
6. **Upload** the finished files to the client's Drive CRO folder with the browser method in Step 5. The browser upload accepts about 10 MB per call, so send large sets in two calls.
7. **Shoot list:** every generated image that shows the practitioner or the practice goes on the handoff shoot list, so the client can replace it with a real photo later.

### Step 6 — HTML prototype → `07-prototype/index.html` (a rebuild goes to `07-prototype/v2/`, never overwrite) → **Checkpoint 2**

**Desktop only (Martin, 2026-10-11).** The workflow starts from the desktop mockup, so the prototype is a desktop build at 1440 px that matches the mockup as closely as possible. A mobile version is not part of this workflow; it belongs to the later rebuild workflow and goes on the handoff as an open item.

Inputs: the GPT mockup as layout and style reference; `approved-copy.md` as exact text; `brand.md` as design system; **`00_project/cro-homepage-motion-spec.md` as the fixed motion and highlight spec (Martin, 2026-10-11)**; the real logo files and real photos from `01-input/`; the high-resolution images from `06-gpt-assets/images/` (Step 5b). Never use crops of the mockup as page images.

1. **Desktop 1440 px:**
   - primary CTA visible in the first screen;
   - body text at least 16 px.
2. **Rebuild each section** to match the mockup section by section (layout, spacing, proportions, colours), with live text. No text baked into images.
3. **Motion:** build exactly the spec: one highlight per section, calm reveal once, breathing CTA in hero and closer only, reduced-motion respected, nothing from the spec's "does not move" list.
4. **Clickable:** CTAs open the client's primary channel (`wa.me/<number>?text=<prefill>` for WhatsApp, the booking link for a booking form, `tel:` for phone); service cards link to `#` placeholders; FAQ uses accordions.
5. **Logo is always the real file** from `01-input/`. Real photos are used wherever they match; Step 5b images fill the gaps and are on the shoot list.
6. **Anything not in the approved copy stays visibly flagged** (`[FEHLT]` badge in the page and in `self-check.md`), never silently filled in.
7. **Build the `?shot=1` mode** (shows all reveal states) for headless screenshots at 1440 px. These screenshots are for the record. They do not replace the visual check in Step 6b. Compare each section with the mockup side by side and note differences. Save the screenshots to `07-prototype/screenshots/`.

**Step 6b — Visual check in Chrome (mandatory, Martin 2026-10-11).** Before the self-check and before any report that the prototype is done, the agent opens the prototype in Claude in Chrome, scrolls it from top to bottom at 1440×900, and checks every item in `00_project/cro-homepage-visual-check.md`: measured checks, global visual items, per-section items, and interaction checks. Everything found wrong is fixed and checked again. The result goes to `07-prototype/visual-check.md`. The agent may not write "done" or "ready for Checkpoint 2" without the line "Visual check done in Chrome, N items checked, N fixed, N open". This applies to every prototype build and every later change to the prototype.

**Self-check → `07-prototype/self-check.md`:** re-score the prototype with `scorecard.md`. Pass condition: every Priority A item scores 2, and all "Done" conditions from section 0 hold. If it fails, fix and re-run. No checkpoint before the check passes.

**Gate for Checkpoint 2:** `visual-check.md` exists and has no open item that the agent could fix. Open items that need client data are listed as `[FEHLT]`.

**Checkpoint 2 — Martin approves the prototype.** Approved → status `Prototyp freigegeben`, go to Step 7. This is the only remaining checkpoint after copy, since the design doc and the GPT image round both run without a stop now.

**Build learnings (Dumann run, 2026-10-11):**
- Cut out portraits with the `rembg` Python API (`new_session('u2net')`, `alpha_matting=True`), not the `rembg` command line, which fails on a missing `watchdog` module. Run it with the Python that has `rembg` installed (`/Library/Frameworks/Python.framework/Versions/3.10/bin/python3` on this Mac).
- Cut an icon sheet apart by labelling the non-white regions (scipy). Make the white background transparent by flood fill from the border, then blur the alpha by 1 px. A white box shows around icons on white cards otherwise.
- A line drawing on a solid purple image goes onto a band of nearly the same purple with `mix-blend-mode: lighten`. Do not use `screen`, it brightens the whole rectangle.
- A real photo cut out at the image edge shows a hard edge. Fade that side with a CSS `mask-image` gradient.
- A cutout has a pale fringe from the old backdrop. Fix it by edge unmixing: for every semi-transparent pixel, subtract the known backdrop colour (taken from the nearest fully transparent pixel of the source photo) and divide by the alpha. Do not fill edge pixels with the nearest solid colour: that makes blocky hair. Check the result on the real band colour at 100 percent.
- Always set `height:auto` on an `<img>` that has `width:100%` in CSS. A leftover `height` attribute stretches the picture (found on the about portrait; measured by M4b).
- Turn automatic hyphenation off in narrow cards (`hyphens:manual`). For one unavoidable long German word add a soft hyphen (`&shy;`) at the compound break.
- A portrait on a 3:2 card is cropped from the top of the original, with the hairline visible. Check the crop at card size.
- Serve the folder with `python3 -m http.server <port>` for the live check. Port 8765 can be taken by an older process. Check with `curl` first.

**Build learnings (law firm run, 2026-10-10):**
- Chrome's real viewport is about 1440×757 (sometimes 1421×701 with scrollbar). The first screen must hold H1, one proof line and the CTA at **701 px height**. Put the rating line between the sub-headline and the buttons so proof and CTA are visible together. Check `getBoundingClientRect().bottom` of the CTA.
- A hero with three buttons or a long label wraps in a 700 px column. Use `flex-wrap:nowrap`, drop the arrow icon in the hero button and set padding to 24 px.
- `text-wrap: balance` on all headings removes single-word last lines.
- A fixed side rail with dark buttons vanishes on a dark band. Give the buttons a 2 px ring in the page colour.
- A "grey to ink while scrolling" paragraph: wrap each word, lighten words with `opacity` as a function of scroll position, never darken them again. Make the formula reach 100 percent while the paragraph is still well inside the screen.
- A hand-drawn wave under a headline line: a `::after` with a repeating SVG background, `transform: scaleX(0)` to `1` once on load. `white-space:nowrap` on the line, otherwise the wave stretches over the wrapped box.
- Numbers of the type 01, 02, 03 in stacked service rows keep links on one line when the item is a flex column and the link has `margin-top:auto`.
- Text check by script (M11): parse the HTML text nodes, normalise, and test each against the normalised `approved-copy.md`. Expect only the prototype notice to differ.

### Step 7 — Handoff package → `08-handoff/handoff.md`

For the separate rebuild workflow:

1. Path to the prototype, the design doc and the GPT assets.
2. `approved-copy.md` with title, description, H1.
3. Image assets plus shoot list for missing real photos.
4. Tracking spec for the client's primary channel: event `whatsapp_click` on every wa.me link, or `booking_click` on every booking link, or `phone_click` on every tel link, each with a `section` parameter. For WhatsApp also the prefilled message per section. Setup itself is not part of this workflow.
5. `[FEHLT]` list: every fact Martin must get from the client before go-live.
6. Before/after score table.
7. Learnings entry appended to `rules.md`.

**The final report always carries the direct link to the client's Drive folder of the run (Martin, 2026-10-11), and the full-page screenshot of the prototype sent as a file, so Martin can open the result at once.** **Register (Martin, 2026-10-11, updated):** after every new page and every new prototype version, add or update the entry in `00_project/cro-registry/registry.json` (fields as in the existing entries, `approved: false`) and run `python3 00_project/cro-registry/build.py`. It rebuilds `~/Desktop/Workflow-Uebersicht.xlsx` for all workflows (sheets Übersicht, Links, Workflows; plain-text links, no hyperlink objects). When Martin approves a prototype: `python3 00_project/workflow-registry/workflow_registry.py approve --cro-id <id>` in the same turn. Keep the sheet simple. Prototypes are opened locally as files, never uploaded to a server unasked. Status → `Übergeben`. Last action of the run: mirror the whole run to the Drive folder as described in 2.2 (all documents in current version, all images, the prototype zip, the final screenshots, `_status.md`), and check the folder listing against the local folder.

---

## 4b. Other page types (first used for the Über-mich page, 2026-10-11)

The same steps run for a single other page of the same client, for example a practitioner page ("Über mich"). Apply these differences. Everything else stays as written.

1. **Folders.** Local `00_project/assets/<slug>/cro/<page-slug>/` with the same subfolders (01 to 08, plus `_status.md` and `00-lead-info.md`). Drive: a subfolder `<Seitenname>` inside the client's `CRO Homepage` folder, with the same upload rules as section 2.2. The client's assets and brand are shared: link to `../01-input/` and `../02-data/brand.md`, do not copy them again. The design system and reusable assets of the finished homepage prototype are the base for the build.
2. **Step 1 data.** Scrape the current page and every page it links to for facts (qualifications, memberships, teaching, location, history). Keep the exact wording with its source URL. Record a table of conflicts and compliance findings (for example a fact that differs between two pages, or a sentence with a healing claim). Use only the newer and safer statement on the new page and write the conflict in `[FEHLT]` and in the handoff. Check the technical state of the current page: schema, title, H1, headings, alt texts.
3. **Step 2 scorecard.** Skip scorecard items that only belong to entry pages (sub-headline with the situation, first-appointment section, situations section, service cards). Add the items of the page type. For a practitioner page: A1 name, role and city in title, H1 and meta; A2 Person schema; A3 career is proven and readable. Plan the sections from the proven pattern of the page type (skill `behandler-seite` and library pattern P1) and run the coverage check against the 10 rows of the P0 blueprint with a reason for every row left out.
4. **Step 3 copy.** Same rules. For health clients add the mandatory notice box. Rewrite any personal story so that it states the motivation and no treatment result. Every quoted text in the final prompt must be found in `approved-copy.md` (check by script before sending).
5. **Step 5 mockup.** Attach the finished homepage mockup as style reference, so both pages look like one website. If the page needs photos of the person at work, plan them as photo slots in the mockup. Generate them later with the portraits attached as the face reference (Step 5b) and put them on the shoot list.
6. **Step 6 prototype.** Add the schema of the page type as valid JSON-LD in the head (for a practitioner page a Person with credentials, work place and expertise). Leave `sameAs` empty until verified profiles exist. Add `noindex,nofollow` while the page is a preview.
7. **Step 7 handoff.** Add: the new URL and the redirect from the old URL, the menu and internal links that must point to the new page, and any correction the new facts force on other pages (for example a statement on the homepage that the new data proves outdated).

## 5. Templates

**`_status.md` line:**

```
2026-10-11 · Step 1 done · 02-data/dataset.md · next: Step 2
```

**`00-lead-info.md`:**

```markdown
# <Praxis> — Lead-Info
Praxis: · Behandler/in: · Website: · CMS: · GBP: · Kontaktkanal (WhatsApp, Telefon oder Buchungsformular): · Quelle: · Status: Lead
```

**Scorecard row (`scorecard.md`):**

| # | Regel | Prüfung | Prio | Score 0/1/2 | Beleg |
| --- | --- | --- | --- | --- | --- |
| 1 | Hero nennt das Problem des Besuchers und die Stadt | H1 + Subline lesen | A |  |  |
| 2 | Primärer CTA im ersten Bildschirm sichtbar | Screenshot 1440 px | A |  |  |
| 3 | Gesicht und Qualifikation der Behandlerin above the fold oder in Sektion 2 | Screenshot | A |  |  |
| … | 15–25 Items aus der CRO-Library |  |  |  |  |

**GPT section prompt skeleton:**

```
[GLOBAL STYLE BLOCK]
Sektion <n> — <Name>. Layout: <Pattern aus patterns.md>.
Headline (exakt): "…" · CTA (exakt): "…"
Echtes Foto: <Beschreibung + Position> · Hintergrund: … · Textur: … · Abstand: …
Format: Hochformat 1024×1536. Look der echten Praxis (Referenzfotos anhängen). Eine CTA-Farbe.
```

---

## 6. Decisions on the open points

| # | Point | Decision (Martin, 2026-10-11) |
| --- | --- | --- |
| 1 | Claude Design or HTML | HTML only |
| 2 | Browser for ChatGPT | Claude in Chrome, Martin's logged-in session; portrait 1024×1536 per section |
| 3 | NotebookLM export | one time, done now, into `00_project/knowledge/cro-library/` |
| 4 | Drive folder | `Local SEO/<Name>/CRO Homepage/` |
| 5 | Contact channel | asked per client before the run; not always WhatsApp |
| 6 | Existing homepage text | used as input when one exists |
| 7 | Images | real photos as reference, GPT creates the ideal images for the prototype |
| 8 | Pass condition | all Priority A = 2, all Done conditions (default kept) |
| 9 | Skill location | `~/.claude/skills/cro-homepage/SKILL.md` (default kept) |

---

## 7. Sequence of first use

1. ~~Agent exports the NotebookLM notebook and derives `rules.md`, `patterns.md`, `scorecard.md`.~~ Done and approved 2026-10-11.
2. ~~Agent writes the skill `cro-homepage`.~~ Done 2026-10-11.
3. Martin names the practice, the URL, the GBP link and the preferred contact channel, and says "go". Agent runs Step 0 to Checkpoint 1. No pilot is set yet.

## Registry: automatic (2026-10-11)

The overview Excel `~/Desktop/Workflow-Uebersicht.xlsx` updates itself. A Stop hook runs `workflow_registry.py sync --quiet` after every turn. You do not call `upsert` for normal progress. Step 7 writes the line `Step 7 done` into `_status.md` of the page folder. `sync` then shows the page as fertig, Freigabe offen. Pages that already have an entry in `cro-registry/registry.json` stay manual (approval, version, archive).
For any other file layout, write `_run.json` in the run folder (schema in `00_project/workflow-registry/README.md`). Only the approval stays manual: when Martin approves a result, run `approve` in the same turn and say that the Excel is updated.

## Martin guide (2026-10-12)

The 741 character Martin points out the one thing per section the reader must not miss. Rules, poses, markup and the inline helper: `00_project/assets/brand/martin-guide/README.md`. In this workflow: only in the presentation wrapper around the prototype (insight next to the change rationale). Never inside the prototype markup. Max 1 callout per section, bubble text in first person and plain language, every number with source and date, check desktop and mobile with a screenshot.
