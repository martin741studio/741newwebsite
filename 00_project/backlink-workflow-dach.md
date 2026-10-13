# Backlink Workflow DACH – Local Businesses, Healing Practices first (v1.1)

Stand: 2026-10-13 · Owner: Martin · Runner: Claude Code (this repo)

**Border (Martin, 2026-10-13):** Backlink DACH stays its own workflow. It is not merged into the Citations module. All of pillar A belongs to the Citations module, also the free niche directories (jameda, Doctolib, theralupa …). This workflow owns pillars B–E. Section 3.0 has the hand-over rule.
Pattern: same shape as `cro-homepage-workflow.md`. Draft for the priming session. Open points are in section 7.

Contents: 0 Purpose · 0.1 Use cases · 1 Operating rules · 2 Storage (2.4 run file) · 3 Pillars (3.0 hand-over to Citations) · 4 Link library · 5 The run (Steps 0–5, Checkpoints 1–4) · 6 Templates · 7 Open points · 9 Pilot readiness · 8 First use

---

## 0. Purpose and outcome

The workflow builds and keeps a backlink profile for a local client in DACH. The goal is the largest ranking gain per euro and per hour. It covers pillars B–E (section 3). Pillar A (all directories, general and niche) is the Citations module. This workflow only hands pillar A finds over to it (section 3.0).

The output per client is a **target list**, an **outreach run**, a **buy shortlist**, and a **monthly link report**. All links are tracked in Supabase and shown in the client portal.

**Done per client (all must be true):**

1. The target list has at least 40 scored targets. At least 25 are local or niche-relevant to the client.
2. Every target has a pillar, a tactic, a DR value, a relevance score, a cost estimate, and a status.
3. Martin approved checkpoints 1–3.
4. The outreach run sent at least 20 first contacts. All mails went out through Airmailer.
5. At least 8 new referring domains are live after 90 days. At least 5 of them are DACH domains with DR 20 or higher.
6. Zero links from link farms, PBNs, or sites outside the client's language and region.
7. The monthly report shows new links, lost links, DR trend, and the next 10 targets.

### 0.1 Use cases

| # | Trigger | Steps | Tools | Result |
| --- | --- | --- | --- | --- |
| 1 | New client: `/backlink-dach <Kunde>, Budget <€>` | Step 0 gate → Step 1 baseline → Checkpoint 1 → Step 2 Sheet → Checkpoint 2 | DataForSEO (`gap-analysis.mjs`), Firecrawl, Supabase read, Drive, Chrome | Sheet with Quelle + Kontakt per row, hand-over list for the Citations module, `_run.json` |
| 2 | Resume a run: "wo stehen wir bei den Backlinks für <Kunde>" | read `00-client-info.md` + `_status.md` → name the checkpoint → next step | Read only | checkpoint report in the fixed format (skill), open `[FEHLT]` list, decisions for Martin |
| 3 | Buy path: budget > 0 after month 1 | Step 4 shortlist per section 3.2 → Checkpoint 4 | DataForSEO, Firecrawl | `04-buy/shortlist.md` with `[KENNZEICHNUNG]`; Martin pays |

---

## 1. Operating rules

1. Martin triggers a run with: client name, website URL, city, industry, and the monthly link budget in euro. Budget 0 is allowed. Then only the free pillars B, D and E run.
2. The runner is Claude Code in `~/martindrendel/741website`. The skill is `backlink-dach` (written after Martin confirms this doc).
3. Tools: DataForSEO Backlinks API (profile, competitors, anchors, new/lost), DataForSEO SERP API (target discovery), Firecrawl (search, scrape, contact pages), built-in browser (verify pages, read sponsor pages), Supabase 741-portal (tracking), Google Drive MCP (work docs), Airmailer (every outreach mail). No Ahrefs. No link marketplaces with auto-buy.
4. Language: all produced files are German. Outreach to German sites uses **du** for Vereine, Blogger, and small businesses. It uses **Sie** for IHK, Kammern, Verbände, Presse, and Behörden. Austria and Switzerland default to Sie.
5. The agent stops only at the 3 checkpoints and at a failed gate. Between checkpoints it runs without asking.
6. **Competitor analysis is required.** This is the opposite of the CRO workflow. The top 5 local competitors give the link gap. Competitor link sources are the first targets.
7. Method sources are never named in client-facing files. The library is called "741 Link-Raster".
8. **The agent never sends outreach.** It drafts every mail and prepares the batch in the Sheet. Martin or the team approves per row and sends manually (decided 2026-10-11, after the Hüwel pilot) — through Airmailer, each from the address decided in section 7. The agent's job ends at "ready to send"; a human updates the Status column after each real send and reply.
9. **No payment without Martin's go.** The agent prepares the buy shortlist. Martin pays. The agent then tracks delivery.
10. **Legal in DACH:** a paid link or a sponsored article must be marked as Werbung or Anzeige where the law requires it. The agent flags every paid placement with `[KENNZEICHNUNG]`. A seller who refuses the mark is dropped.
11. **Health mode (HWG):** for health clients, no guest post or PR text makes a healing promise. The HWG check from the CRO workflow applies to every text that leaves the agent.
12. One link per domain per client in the first 90 days. More links from one domain give little extra value.
13. The agent never creates fake profiles, fake reviews, or forum spam. Reddit and forum work is monitoring and honest reply only.

---

## 2. Storage

### 2.1 Local working folder (source of truth)

```
00_project/assets/<slug>/backlinks/
  00-client-info.md      name, website, city, industry, budget/month, competitors, status
  _status.md             run log: one line per step (date · step · output file · next step)
  01-baseline/           profile.md, competitors.md, gap.md (DataForSEO exports as csv)
  02-targets/            targets.md (scored list), targets-v2.md …
  03-outreach/           templates.md, batch-01.md (per mail: target, contact, text, date, reply)
  04-buy/                shortlist.md, orders.md (seller, price, URL, anchor, live date, mark)
  05-pr/                 pitches.md, mentions.md (unlinked mentions found + reclaim status)
  06-ai-citation/        entity-check.md, llm-structure.md
  07-report/             report-YYYY-MM.md
```

`<slug>` = lowercase client name, e.g. `suriya`, `huewel`.

### 2.2 Supabase (741-portal)

Two new tables. Admin writes. Client reads own rows. Same RLS pattern as `client_citations`.

| Table | Purpose | Key columns |
| --- | --- | --- |
| `backlink_targets` | master list of link sources, reused across clients | id, domain, name, pillar (A–E), tactic, country (DE/AT/CH), region, industry_tags[], dr, dofollow, cost_eur, contact_url, contact_email, address_form (du/Sie), notes, last_checked |
| `client_backlinks` | one row per client × target | id, client_id, target_id, status, url_from, url_to, anchor, link_type (dofollow/nofollow/sponsored/ugc), found_at, live_at, lost_at, cost_eur, submitted_via, notes |

Status values for `client_backlinks`: `identified → contacted → replied → agreed → live → lost → rejected`.

The portal tab "Sichtbarkeit" gets a second block "Backlinks" under the Citations block. It shows: referring domains total, DR trend, new links this month, and the status list. Build is a separate decision (section 7).

### 2.3 Drive mirror

Drive folder: `Local SEO/<Client name>/Backlinks/`. At every checkpoint the agent uploads the markdown files of that step. Reports go there every month.

### 2.4 Run file for the overview Excel

Every run writes one run file: `00_project/assets/<slug>/backlink/<YYYY-MM-DD>/_run.json`. The date is the start date of the run. The schema is in `00_project/workflow-registry/README.md`. The Stop hook runs `workflow_registry.py sync` after every turn and reads the file. Then the run shows in `~/Desktop/Workflow-Uebersicht.xlsx` by itself.

Write it with the skill script, not by hand:

```bash
python3 ~/.claude/skills/backlink-dach/scripts/write_run.py --slug <slug> --client "<Name as in the Excel>" --status "in Arbeit" --note "Checkpoint 1: Baseline gezeigt"
```

Update it at each checkpoint and at the end. After Checkpoint 2, `--result` is the Sheet link. Approval stays manual: `workflow_registry.py approve --client "<Name>" --workflow backlink`.

### 2.5 Folder rules

1. At run start, read `00-client-info.md` and `_status.md`. Continue from the step named as next. If the folder does not exist, create it.
2. After every step, append one line to `_status.md`.
3. Never overwrite. Revisions get `v2`, `v3` next to the original.
4. Status values in `00-client-info.md`: `Start → Baseline → Ziele freigegeben → Outreach läuft → Kauf freigegeben → Monatslauf`.

---

## 3. The five pillars (from the planning board)

| Pillar | Tactics | Who runs it | Cost |
| --- | --- | --- | --- |
| **A · Branchenverzeichnisse** | Kern-Verzeichnisse · Lokale Verzeichnisse · Nischen-Verzeichnisse · Datenaggregatoren · Indexierung | Citations module only (BrightLocal + self-service + Gruppe A/B). Not part of this workflow. | see `citations-listings-module` |
| **B · Lokales Ökosystem** | IHK/HWK · Berufs- und Branchenverbände · Lokale Presse & Blogger · Vereins-Sponsoring · Event-Sponsoring · Gemeinnützige (.org) · Hersteller & Lieferanten | 741 outreach + client intro where needed | 0–300 € per link |
| **C · Gezielter Backlink-Kauf** | Quell-Domain-Auswahl · Linktext-Auswahl · Strategischer Kauf · DR-Überwachung & Indexierung | 741 prepares, Martin pays | budget-driven |
| **D · Digitale PR & Erwähnungen** | Journalisten-Anfragen (DACH) · Unverlinkte Erwähnungen · Reputation & Reddit-Beobachtung | 741 | 0 € + time |
| **E · KI-Zitierung** | LLM-Strukturierung & Zitate · Entity-Konsistenz | 741, overlaps with `seo-page-optimizer` | 0 € |

**Order of work per client:** A (Citations module, runs on its own) → B → D → C → E. Free and local first. Paid last, only to close the gap that B and D cannot close.

### 3.0 Pillar A — hand-over to the Citations module (border 2026-10-13)

The Citations module (`citations-listings-module`) owns all of pillar A: the general DACH directories (Gelbe Seiten, Das Örtliche, Cylex …), the aggregators (GBP, Bing, Apple) and the free industry-specific niche directories (jameda, Doctolib, theralupa, Heilpraktiker.de …). Martin decided this on 2026-10-13. Before that date, this workflow owned the niche part.

This workflow does not research, score or list directories. It does one read-only hand-over check:

1. At Step 1, read the client's `client_citations` rows for the industry category in Supabase. Read only.
2. List every row that is not `live`. Show the list at Checkpoint 1 under the heading "Übergabe an das Citations-Modul".
3. A directory that the backlink research finds by chance (for example in the competitor gap) also goes on that hand-over list. It never goes into the backlink Sheet. `build_sheet.py` refuses a row with Säule A.
4. Pillar B keeps the Berufsverband member listings (BDH, FDH, VDH, VPT, IFK …). A member listing needs a membership. A directory needs only a self-registration. That is the line.

**Hand-over from the Hüwel pilot (2026-10-10/11), for the Citations module:**

- 7 `health` rows in `client_citations` on status `planned`, none live: jameda, Doctolib, theralupa, arzt-auskunft, DocInsider, sanego, Heilpraktiker.de.
- 3 niche directories found by the old Process A: `naturheilkunde.de` (Arzt-/Heilpraktikersuche), `dornsteintabelle.de/heilpraktiker` (free self-registration), `aponeo.de` Heilpraktikerverzeichnis.
- The old Process A (search templates for niche directories) moves to the Citations module. The query templates were: `"[Branche]" Verzeichnis kostenlos eintragen Deutschland` · `[Branche]suche OR Therapeutensuche [Spezialisierung] Verzeichnis` · `"[Branche]" Verzeichnis Krankenkasse OR Zusatzversicherung` · `inurl:verzeichnis OR inurl:suche [Branche] [Bundesland]`.
- `bdh-online.de/patienten/therapeutensuche/` is a Verband member search. It stays in pillar B. Dedupe check against `bdhn.de` is still open.

### 3.1 Pillar B — local ecosystem, DACH specifics

**Fixed priority (`rules.md` RH.4) — do not blend with the score, rank in this order first, score within each tier second:**

1. IHK / HWK — only when the client's profession is actually a `Gewerbe` requiring membership. For a `freier Beruf` (Heilpraktiker, Arzt, Architekt, …) this tier does not exist — it is not replaced by the Berufsverband, which stays tier 2.
2. Berufsverband / niche directory with both trade AND local relevance.
3. Everything else local, ranked by proximity to the client's own address — closer beats a bigger but farther organisation, because the map pack itself is proximity-based (`rules.md` RH.5).

| Tactic | Where to look | Link type | Note |
| --- | --- | --- | --- |
| IHK / HWK | Firmendatenbank of the regional IHK; HWK only for Handwerk | dofollow, high trust | Tier 1 only if the profession is actually `Gewerbe`-pflichtig — check before assuming. |
| Berufsverbände | Mitgliederliste of the Fachverband (BDH, FDH, VDH for Heilpraktiker; VPT/IFK for Physio) | dofollow, E-E-A-T | Tier 2 always, never promoted to tier 1 even when IHK does not apply. Needs the client's membership number. |
| Lokale Presse | Wochenblatt, Stadtmagazin, Lokalteil der Tageszeitung, regional online portals | editorial dofollow | Pitch: opening, expert quote, local event, health day. |
| Lokale Blogger | "[Stadt] Blog", "[Stadt] Mama Blog", "[Region] Gesundheit Blog" | dofollow or sponsored | Mark sponsored posts. |
| Vereins-Sponsoring | Sportverein, Kulturverein, Freiwillige Feuerwehr, Schulförderverein | Sponsoren-Seite, dofollow | 100–300 € per year. Cheapest real local link. |
| Event-Sponsoring | Stadtfest, Gesundheitstag, Lauf, Weihnachtsmarkt | event page + press | Time-bound. Plan 3 months ahead. |
| Gemeinnützige (.org) | Local Hospiz, Tafel, Tierheim, Selbsthilfegruppe | Unterstützer-Seite | Often needs a real donation. Honest only. |
| Hersteller & Lieferanten | Product brands the client uses or sells (Ayurveda oils, Praxis equipment, software) | "Anwender" or "Partner" page | Ask for the therapist locator. |
| Stadt / Wirtschaftsförderung | Stadtportal Branchenbuch, Gewerbeverein, Wirtschaftsförderung | member listing | Free or small fee. |
| VHS / Akademien | Dozenten page if the client teaches | dofollow | Only if true. |

### 3.2 Pillar C — buy rules

1. Source domain must pass: DACH language, real organic traffic (DataForSEO ranked keywords > 100), topical or regional fit, no "write for us" spam footprint, outbound links per page under 20.
2. Price bands: DR 20–35 up to 150 €, DR 36–50 up to 350 €, DR 51+ case by case. Above band → Martin decides.
3. Anchors: 60 % brand or URL, 30 % partial match ("Heilpraktikerin in Ingelheim"), 10 % exact match. Never the same exact anchor twice.
4. Every bought placement gets the `[KENNZEICHNUNG]` flag and the live URL in `04-buy/orders.md`.
5. Indexing check at day 7 and day 30 with `site:` search and DataForSEO new-links. Not indexed at day 30 → ask the seller or request a refund.

### 3.3 Pillar D — digital PR, DACH channels

| Channel | Use | Note |
| --- | --- | --- |
| Journalisten-Anfragen DACH | Expert quotes for health, wellness, local economy | Channels to verify in setup: Presseportal, OpenPR, Recherche-Plattformen, #Journalistenanfrage on X and LinkedIn. `[prüfen]` which ones still deliver in 2026. |
| Unverlinkte Erwähnungen | Find brand and practitioner name mentions without a link | DataForSEO Content Analysis API, Google search with quotes, Firecrawl search. Reclaim with a short mail. |
| Reputation & Reddit | Watch r/de, r/Finanzen, local subreddits, gutefrage.net for the client's topics | Reply with real help. Link only if the rule of the community allows it. |
| Studies and data | One small local data piece per year (survey of 50 patients, price index) | This is the only reliable way to earn press links. |

### 3.4 Pillar E — AI citation

1. Entity check: name, address, phone, practitioner, specialties are identical on website, GBP, Wikidata (if any), and the top 10 citations.
2. Page structure: every service page has a definition block, an FAQ with schema, a "Quellen" block with 2–3 outbound links to authorities, and an author box. This is handled by `seo-page-optimizer`. This workflow only checks that it exists.
3. Citation seeding: get the client named in 3 third-party texts that LLMs crawl: a Verband profile, a local press piece, a directory with editorial text.
4. Monthly check: ask 5 fixed questions in ChatGPT, Perplexity, and Google AI Overview. Log if the client is named. File `06-ai-citation/llm-check-YYYY-MM.md`.

---

## 4. One-time setup: the Link library

Source 1: the SEO library `00_project/knowledge/seo-library/`. The 8 strongest link sources are already there: 019, 020, 021, 041, 042, 070, 073, 027. Plus `backlink-targets-dach.md` from 2026-08-08.

Source 2 (optional): a new NotebookLM notebook "Linkbuilding DACH" with 20–30 German sources. Export with the same method as the CRO library. Decision in section 7.

**Derive three files in `00_project/knowledge/link-library/_derived/`:**

| File | Content |
| --- | --- |
| `rules.md` | Every principle as an if/then rule with source. Drop everything that only works in the US or for SaaS. Add DACH rules: IHK and Verband first, Vereins-Sponsoring as the cheapest local link, Kennzeichnung for paid links, du/Sie by target type, HWG for health texts. |
| `targets-seed.md` | 100+ reusable DACH sources by pillar and industry. Each with domain, DR, cost, contact path. This is the seed for `backlink_targets`. |
| `scorecard.md` | 15–20 items to score a link profile and a single target. Score 0/1/2. Priority A/B/C. |

**Target score (used in `targets.md` and `backlink_targets`):**

```
Score = Relevance (0–3) + Authority (0–3) + Cost (0–2) + Effort (0–2)
Relevance: 3 same city + same industry · 2 same region or same industry · 1 DACH general · 0 none
Authority: 3 DR 50+ · 2 DR 30–49 · 1 DR 15–29 · 0 under 15 or no traffic
Cost:      2 free · 1 under 150 € · 0 over 150 €
Effort:    2 form or one mail · 1 call or two mails · 0 needs client action or event
Max 10. Work targets with 7+ first.
```

**Gate:** Martin approves the three derived files. Later runs only read them.

**Update rule:** after each monthly report, the agent appends a "Learnings" entry to `rules.md`. A target type that fails on 2 or more clients gets reviewed.

**Zeitnotiz 11.10.2026, erledigt 13.10.2026 — Sheet-Export Drive-Falle:** openpyxl mit Styling bricht die xlsx→Sheets-Konvertierung in Drive. `build_sheet.py` nutzt seit 2026-10-13 XlsxWriter (Start: `uv run --with xlsxwriter python3 build_sheet.py …`). Regel in Memory `well-designed-sheets.md`.

---

## 5. The run

### Step 0 — Readiness gate

| Input | Required | Check |
| --- | --- | --- |
| Website URL | Yes | Loads over https. |
| City and industry | Yes | Given by Martin. |
| Monthly budget in € | Yes | 0 allowed. |
| Top 5 local competitors | Yes | Martin names them, or the agent takes the top 5 from the map pack and the organic top 10 for "[Leistung] [Stadt]". |
| Citations status | Yes | Pillar A at 60 % live or higher. Otherwise finish citations first. |
| Memberships | Recommended | IHK, Verband, Vereine. Ask Martin once. Missing → `[FEHLT: Mitgliedschaften]`. |
| Client intro possible | Recommended | Can the client send a mail to Verein, Lieferant, Verband? Yes/No. |
| Review velocity + on-page | Yes | Local backlinks are the lever AFTER review velocity and on-page keywords are solid, not a first move (`rules.md` RH.1). If either is clearly weak, flag `[FEHLT: Grundlagen zuerst]` and recommend that work before this workflow starts. |

**Gate:** All required rows filled or flagged → Step 1. Otherwise stop and list what is missing.

### Step 1 — Baseline → `01-baseline/`

| # | What | Tool | Output |
| --- | --- | --- | --- |
| 1.1 | Own profile: referring domains, DR, dofollow share, anchors, top pages | DataForSEO Backlinks `summary`, `referring_domains`, `anchors` | `profile.md` |
| 1.2 | Toxic check: spam score, foreign-language domains, PBN patterns | DataForSEO `backlinks` with filters | disavow list if needed |
| 1.3 | Competitor backlink analysis — **Process B below** | DataForSEO | `competitors.md`, `gap.md` |
| 1.4 | Hand-over check — every `client_citations` row for the client's industry category that is not `live` goes on the hand-over list for the Citations module (section 3.0). Read only. | Supabase | `01-baseline/handover-citations.md` |
| 1.5 | (moved) Niche directory research is a Citations-module task since 2026-10-13. Row stays empty here. | — | — |
| 1.6 | Local source scan: Verbände, Vereine, Presse, Stadtportale, Hersteller/Lieferanten for the city — the 6 tactics in rules.md RB.3–RB.9, worked as a checklist, not stopped at the first hit | Firecrawl search + built-in browser | source list |
| 1.7 | Unlinked mentions: brand name, practitioner name, phone number in quotes | DataForSEO Content Analysis, Google | `05-pr/mentions.md` |
| 1.8 | Existing 741 data: citations status, NAP record, portal texts | Supabase, `00_project/assets/<slug>/` | links and facts |

**Gate:** Rows 1.1–1.4 and 1.6–1.8 filled. A row with no data gets "keine Daten, Grund: …".

**Process B — competitor backlink analysis (step-by-step, replaces ad-hoc calls):**

1. **Select competitors.** Minimum 8, not 5 — a pool of 5 gives too few gap hits to be worth the API cost (confirmed on the Hüwel pilot: 5 competitors → 10 gap domains, 8 competitors → 23). Source: DataForSEO SERP organic, keyword `"[Leistung] [Stadt]"`, DE, depth 20, filtered to real competing practices/businesses (drop directories, schools, franchises). If the nearest/obvious competitor has weak map-grid coverage, that is a signal to expand the search and find who actually dominates the grid instead (`rules.md` RH.2), not to settle for the weak neighbor. Add any competitor Martin or the client names by hand (e.g. a practice already flagged in Local Falcon data) even if it doesn't rank organically.
2. **Verify each competitor's real domain from their GBP**, not just a name guess, and check for a redirect — an acquired or merged business's domain commonly redirects to the parent's, which would otherwise count the wrong company's links (`rules.md` RH.3).
3. **Pull referring domains per competitor.** DataForSEO `backlinks/referring_domains`, `limit: 300`, `order_by: rank,desc`, one call per competitor plus one for the client's own domain.
4. **Run the raw export through the classifier prompt** (`00_project/knowledge/link-library/_derived/local-backlink-classifier-prompt.md`) before manual scoring — it separates local/regional/national/spam with an evidence requirement, cheaper than eyeballing 300+ domains per competitor (`rules.md` RH.6).
5. **Compute the gap locally** (no need for `domain_intersection` — plain set logic is cheaper and auditable): a domain counts if it links to **2 or more** competitors and does not already link to the client. Record which competitors, for the Quelle column.
6. **Filter spam before scoring.** A domain with `rank` near 0 despite a high referring-domain or backlink count on itself is a spam/link-farm signal (see `rules.md` RG.3) — drop it, do not score it. A domain is a reciprocal practice-to-practice link (another local competitor's own site, not a directory or publication) — drop it, not scalable and looks manipulative.
7. **Verify survivors** with one `backlinks/summary` call each before they go into `targets.md` — rank, backlink count, referring-domain count, so the score in Step 2 is real, not guessed.

**Process A — moved to the Citations module** (section 3.0). A directory in the gap list goes on the hand-over list, not into the Sheet.

**Checkpoint 1 — Martin reviews the raw baseline before any scoring happens** (added 2026-10-11, after the Hüwel pilot). Show `profile.md`, `competitors.md`, `gap.md`, the hand-over list for the Citations module, and the raw local-source finds, as plain lists — no score, no Sheet yet. This catches a wrong competitor set or a missed tactic before time goes into Step 2. Approved → go to Step 2. Martin names a competitor to add/drop, or a tactic from RB.3–RB.9 that wasn't worked → redo the relevant part of Step 1 first.

**Rows into the Sheet stay a quick pass, not a full field visit.** A row can carry "vermutl. frei" or an unconfirmed cost — mark it plainly, don't block the row on it (decided 2026-10-11). Confirm cost and contact details only for rows Martin actually ticks `Freigabe` on, as part of Step 3's prep, not before.

**No enforced pillar mix.** The target list reflects what the research actually finds per client — do not pad a thin pillar (e.g. Hersteller/PR) with weak filler just to show every pillar represented (decided 2026-10-11).

### Step 2 — Target list → `02-targets/targets.md` → **Checkpoint 2**

1. Merge: gap domains (1.3, without directories) + local sources (1.6) + unlinked mentions (1.7) + seed targets from the library that match industry and region. No pillar A row.
2. Score every target with the formula in section 4 **internally, to decide the row order** — the Score column itself is not shown to Martin (decided 2026-10-11, see "Sheet columns" below). Keep targets the research actually found real; no padding to hit a count.
3. Assign pillar and tactic. Write the contact path (email or form URL — see Kontakt below) and note the address form (du/Sie) for Step 3, where it is actually used.
4. Split into: **Free now** (score 7+, cost 2), **Needs client** (effort 0), **Buy candidates** (pillar C, within budget).
5. Write the 90-day plan: month 1 = Verbände, IHK, Vereine, mentions. Month 2 = Presse, Blogger, Lieferanten. Month 3 = buy to close the gap.

**Sheet columns (decided 2026-10-11, after Martin reviewed the first 3 Hüwel versions):**

| # | Domain | Säule | Taktik | DR | Kosten | Quelle | Kontakt | Status | Freigabe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- **DR** — not the raw DataForSEO 0–1000 rank. Convert with `round(min(rank/10, 100))` and label the column "DR (approx.)" — an approximation of the familiar 0–100 scale, not an official DR figure. State this once in the Sheet's legend, not per cell.
- **Score and Form are dropped from this table.** Score decided the row order already; showing the number itself adds a figure Martin doesn't act on. Form (du/Sie) only matters when a mail is actually drafted — it lives in the Outreach tab (Step 3), not here.
- **Kontakt is mandatory** (was specified here but never actually built into the first 3 Sheet versions — fixed 2026-10-11): email address or the submission-form URL. Where it isn't verified yet, write what's plausible (e.g. "Kontaktformular auf der Seite", "Mitgliedsantrag online") rather than inventing a specific address — never fabricate an email. A pillar A row never enters this Sheet (section 3.0).

**Checkpoint 2 — Martin approves the target list and the 90-day plan.** Approved → status `Ziele freigegeben`. Update `_run.json` with the Sheet link (section 2.4). Rows go into `backlink_targets` and `client_backlinks` with status `identified`.

### Step 3 — Outreach → `03-outreach/` → **Checkpoint 3**

1. Write one template per tactic: Verein, IHK, Verband, Presse, Blogger, Lieferant, Mention reclaim. German. du or Sie by target. Short. One ask. Include what the target gets.
2. Personalise every mail with one line about the target. No mass text.
3. Build `batch-01.md`: 20–30 mails. Each with target, contact name, address, subject, body, planned send date.
4. Flag mails the client must send (Verband with member number, Lieferant with customer number). Put them into a client mail with copy-paste text, same pattern as `client-listing-email-template.md`.
5. Each mail row gets the same `Freigabe` checkbox pattern as the target list (section 6 below), in the Sheet's Outreach tab — not a single approve-all gate for the whole batch, so Martin can send some rows and hold others.

**Checkpoint 3 — Martin ticks `Freigabe` per mail.** The agent's work on that row ends at "ready to send". Martin or the team sends manually through Airmailer, from the address decided in section 7. Follow-up after 7 days, one time, also manual. A human moves Status from `contacted` to `replied`, `agreed`, `live` as replies come in and ticks the live URL — the agent does not poll for this (no listings-inbox-poller equivalent for real outreach replies). The agent re-reads the Sheet on the next run and picks up status changes from there.

### Step 4 — Buy shortlist → `04-buy/shortlist.md` → **Checkpoint 4**

Only if budget > 0 and after month 1 results are in.

1. Candidates from Step 2 pass the rules in section 3.2.
2. Per candidate: domain, DR, traffic, price, proposed anchor, target URL, Kennzeichnung yes/no, seller contact.
3. Total within budget. Alternatives listed.

**Checkpoint 4 — Martin approves and pays.** The agent tracks delivery, checks the live URL, and runs the indexing checks.

### Step 5 — Monthly run → `07-report/report-YYYY-MM.md`

Runs on day 1 of each month without a checkpoint.

1. DataForSEO new and lost links for the client. Update `client_backlinks`.
2. DR and referring-domain trend. One line each.
3. Status table: contacted, replied, live, lost.
4. AI citation check (section 3.4, item 4).
5. Next 10 targets.
6. Learnings entry to `rules.md`.
7. Upload to Drive. Portal block updates from Supabase.

Status → `Monatslauf`.

---

## 6. Templates

**`_status.md` line:**

```
2026-10-15 · Step 1 done · 01-baseline/profile.md · next: Step 2
```

**`00-client-info.md`:**

```markdown
# <Kunde> — Backlink-Info
Kunde: · Website: · Stadt: · Branche: · Budget/Monat: · Wettbewerber: 1… 5… · Mitgliedschaften: · Kunden-Intro möglich: ja/nein · Status: Start
```

**Outreach mail skeleton (Verein, du):**

```
Betreff: Kurze Frage zur Sponsoren-Seite vom <Verein>

Hallo <Name>,

ich bin <Behandlerin> aus <Stadt>. Ich möchte den <Verein> mit <Betrag> € im Jahr unterstützen.
Gibt es dafür einen Platz auf eurer Sponsoren-Seite mit Logo und Link zu meiner Praxis?

Wenn ja: an wen schicke ich Logo und Überweisung?

Viele Grüße
<Name>
<Praxis> · <Website>
```

**Scorecard row (`scorecard.md`):**

| # | Regel | Prüfung | Prio | Score 0/1/2 | Beleg |
| --- | --- | --- | --- | --- | --- |
| 1 | Mindestens 5 DACH-Domains DR 20+ verlinken auf die Startseite | DataForSEO referring_domains | A |  |  |
| 2 | Kein Link aus Linkfarmen oder fremdsprachigen Domains | Toxic check 1.2 | A |  |  |
| 3 | IHK oder Verband verlinkt | Mitgliederliste prüfen | A |  |  |
| … | 15–20 Items aus der Link-Library |  |  |  |  |

---

## 7. Open points for the priming session

| # | Point | Options | My proposal |
| --- | --- | --- | --- |
| 1 | Library source | SEO library only · new NotebookLM "Linkbuilding DACH" | Start with the 8 SEO-library sources + `backlink-targets-dach.md`. Add the notebook later if rules are thin. |
| 2 | Supabase tables | build now · build after pilot | Build now. Two tables, same RLS pattern. One session. |
| 3 | Portal block | now · later | Later. First pilot runs from markdown. |
| 4 | Outreach sender | client's own address · `<slug>@listings.741.studio` · 741 address | Client's own address through Airmailer where possible. Local targets trust a local sender. Fallback: 741 address with "im Auftrag von". |
| 5 | Buy budget default | 0 · 150 · 300 € per month | 0 for the pilot. Free pillars first. |
| 6 | Pilot client | Suriya · Hüwel · Stürzl | Hüwel. Nürnberg has a dense Vereine and Presse landscape. Citations are further along. |
| 7 | Journalist channels DACH | to verify | Agent checks in setup which platforms still deliver. Result into `rules.md`. |
| 8 | Skill location | `~/.claude/skills/backlink-dach/SKILL.md` | default |
| 9 | Checkpoints | 3 (as drafted) · 4 with a report checkpoint | 3. The monthly report needs no stop. |

---

## 9. Pilot readiness (checked 2026-10-10)

| # | File / asset | Status | Note |
| --- | --- | --- | --- |
| 1 | `00_project/backlink-workflow-dach.md` | draft | needs Martin's go + section 7 answers |
| 2 | `00_project/knowledge/link-library/` + `INDEX.md` | 63 of 97 | 34 blocked by YouTube rate limit, retry later |
| 3 | `00_project/backlink-targets-dach.md` | exists | DACH seed list from 2026-08-08 |
| 4 | `seo-library` sources 019/020/021/041/042/070/073/027 | exists | digital PR + link building guides |
| 5 | Citations module (Supabase, poller, portal tab, runbook) | live | owns all of pillar A, also niche directories (2026-10-13) |
| 6 | `client-listing-email-template.md`, `loop-signals-playbook.md` | exists | patterns for client mails and co-citation |
| 7 | DataForSEO Backlinks API | tested OK | `backlinks/summary/live` 0.024 $ per call, no IP block |
| 8 | Airmailer | live | the only send channel |
| 9 | `client_locations` NAP for Hüwel, Suriya | exists | |
| 10 | `link-library/_derived/rules.md`, `targets-seed.md`, `scorecard.md` | **missing** | step 2 |
| 11 | Supabase `backlink_targets`, `client_backlinks` + RLS | **missing** | step 3 |
| 12 | Outreach templates (7 tactics, du/Sie) | **missing** | part of step 2 |
| 13 | Skill `~/.claude/skills/backlink-dach/SKILL.md` | installed | scorecard: `00_project/backlink-scorecard-2026-10-13.md` |
| 14 | Martin inputs: 9 decisions, pilot client, budget, 5 competitors, memberships, client intro, sender address | **missing** | 30 min |
| 15 | Portal block "Backlinks" | later | not needed for the pilot |

## 8. Sequence of first use

1. Martin confirms this doc and answers section 7.
2. Agent derives `rules.md`, `targets-seed.md`, `scorecard.md` into `00_project/knowledge/link-library/_derived/`. Martin approves.
3. Agent creates `backlink_targets` and `client_backlinks` in Supabase and seeds the targets.
4. Agent writes the skill `backlink-dach`.
5. Martin names the pilot client, budget, and competitors, and says "go". Agent runs Step 0 and Step 1 to Checkpoint 1 (baseline review), then on to Checkpoint 2 (target list) after approval.
