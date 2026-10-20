# Design note — Un-Burning (checkpoint 1)

Status: DRAFT for Martin's "go". Nothing is built, installed or changed on a client asset.
Language: STE. Field names are English. Board labels are German.
Source of truth for scope: Martin's board `00_project/assets/un-burning-workflow/un-burning-board.png` and his detail text (areas A to E).

## 1. Goal

Find everything that harms a client's online presence. Then remove or repair it in a safe, controlled way. The result is a stable "bedrock" before growth SEO starts.
Un-Burning removes harm. It does not add growth. The audit finds problems. Un-Burning acts on the harmful ones.

Harm versus gap (the rule that keeps the two workflows apart):

| Type | Meaning | Example | Owner |
| --- | --- | --- | --- |
| Harm | Something that exists and damages or blocks | wrong address on 12 listings, duplicate page, 404 with backlinks | Un-Burning |
| Gap | Something missing that would add growth | no posts, few photos, no new service page | Audit, then growth SEO |

## 2. Decisions from the grilling (Martin, 2026-10-11)

| # | Topic | Decision |
| --- | --- | --- |
| 1 | First client | Praxis Suriya (Ingelheim, Heilpraktikerin, program client) |
| 2 | What burned | Wrong NAP and spam listings. Bad site or index. A former party held assets, but for Suriya every asset is already with the owner |
| 3 | Area A (ownership, access) | RETIRED (Martin, 2026-10-11). Solved at onboarding. Only a precondition for Un-Burning |
| 4 | End result | "Bedrock Pack": damage map, harm register, keep/fix/kill list, bedrock check |
| 5 | First reader | Martin, then agents. Client sees a released client-safe tab later |
| 6 | Order | Public checks first (C, D, E). Access request runs in parallel |
| 7 | Phases | 4 phases: scan, triage (go), execute, verify and report |
| 8 | Autonomy | Agents prepare alone. Every live change needs a go. Batch go per area. Per-item go for deletes, merges and review reports |
| 9 | Data store | JSON per run. Supabase tables later, after Martin's go |
| 10 | Report | Internal HTML (page 1 = damage map) plus client-safe portal tab as draft |
| 11 | Success measures | GBP calls, routes, site clicks. Indexed pages and 404 count. NAP consistency percent. Inquiries per week |
| 12 | Detection depth | Light: public data plus Search Console. Under 1 EUR. No new Falcon scans |

One limit (stated once): suspended or ineligible Google profiles use only the compliant route. That means a real business, a real eligible address, proper evidence and video verification of the real business. Address workarounds are out of scope.
Review removal uses only Google's report and appeal routes and, where it fits, a legal route. No fake counter-reviews.

## 3. Use cases

| # | Trigger | Steps | Tools | Result |
| --- | --- | --- | --- | --- |
| UC1 | `/un-burning praxis-suriya` | Scan C, D, E from public data and GSC. Verify A. Build harm register. Triage with Martin. Execute approved waves. Re-scan | Live-site script, GSC export, `client_citations`, DataForSEO (light), Chrome (read) | Bedrock Pack. Bedrock check green or a list of what blocks it |
| UC2 | `/un-burning <client> --from-audit <run>` | Read audit `findings.json`. Convert harm fields into register rows. Drill to item level. Continue as UC1 | Audit run folder plus UC1 tools | Same pack, faster, no repeated checks |
| UC3 | `/un-burning <client> --reverify` | Re-scan the same checks. Compare with the last run. Show before and after | Same tools | Delta report. Proof of effect |

## 4. Pipeline (4 phases, 3 checkpoints)

```
Phase 1  SCAN        agents alone, read only
  1.0 intake: client, domain, GBP name, known history, master NAP record
  1.1 preconditions check: master locked? access present? (no items)
  1.2 C scan: NAP across site, GBP, client_citations, 10 live directory checks, old names and addresses, spam listings
  1.3 D scan: crawl (404, duplicates, thin pages, orphans, canonicals, noindex), brand SERP, review check, HWG text scan
  1.4 E scan: sitemap vs GSC index, indexed vs intended, internal link graph
  1.5 write harm-register.json + evidence + manifest; validator runs
Phase 2  TRIAGE      Martin
  2.0 reviewer subagent checks the draft kill list against evidence
  2.1 report page 1 (damage map) + area tables
  >>> GO-1: Martin sets keep / fix / kill per row, or batch-approves a class
Phase 3  EXECUTE     per wave, per area
  3.0 plan file (changes.json) + validator + snapshot of every target
  >>> GO-2: Martin approves the exact change list of the wave
  3.1 apply (redirects, listing edits, content fixes) and write the change log
  3.2 per item: verify live, save after value
Phase 4  VERIFY      agents alone, then Martin
  4.0 re-scan the same checks, same parameters
  4.1 before/after tracker, bedrock check per area
  4.2 client-safe tab (draft) + client message draft + Drive link
  >>> GO-3: Martin releases the client tab
```

Wave order inside phase 3: reversible and low-risk first (NAP text on listings, redirects). Then content fixes. Deletes and review reports last, each with its own go.

## 5. Interface with the audit workflow

Audit fields become harm-register rows when the field status is yellow or red and the finding is harm, not gap. Un-Burning adds item-level drill-down. It never repeats the audit logic.

| Audit field | Area | Harm-register item |
| --- | --- | --- |
| B13.01 Duplikate und Doppel-Einträge | C | One row per duplicate profile or listing |
| B13.02 Adress- und Verifizierungsrisiko | C | Old address still live (example: Binger Str.) |
| B13.03 Name im Profil | C | GBP name differs from legal name |
| B05.02 GBP-Anzahl und echte Adressen | C | Unknown or extra profile |
| B06.05 Live-NAP-Konsistenz | C | One row per source with a wrong NAP field |
| B07.02 Lokale PR und Citations | C | One row per inconsistent or spam citation |
| B07.03 Social-Media-Auftritt | C | Wrong handle or old data on a profile |
| B07.04 Anti-SEO und Negativ-PR | D | Negative page-1 result, 1-star burst |
| B13.07 Review-Richtlinien-Risiko | D | Suspect or fake review (report route only) |
| B13.05 Branchen-Werberecht | D | Banned claim on site or GBP (example: HWG) |
| B06.03 Schnelle SEO-Fehler | D | One row per canonical, robots, redirect or sitemap error |
| B06.04 Qualität der Location-Seiten | D | Thin or duplicate location page |
| B07.01 Backlink-Audit | D | Spam link or wrong brand anchor (opt-in, see section 9) |
| B06.06 Indexierung | E | One row per indexed-but-unintended or intended-but-missing URL |
| B06.08 Keyword-zu-Seite-Zuordnung | E | Page without a parent link (input to inverted-tree plan) |

Audit fields not listed (B05 rankings, B10 completeness, B11 competitors, B12 AI visibility) are gaps. They stay in the audit and go to growth SEO.
If no audit run exists, Un-Burning runs the audit's own scripts for the listed fields. It does not write separate checks.

## 6. Harm register (core data object, preview)

One row = one harmful item. Full model comes after the go (`data-model.md`).

| Field | Meaning |
| --- | --- |
| `id`, `area` (B-E; A is retired), `entity` (domain, website, gbp, listing, social, backlink, review, index) | Where the item lives |
| `item`, `evidence_ids`, `source_field` (audit id or own check id) | What it is and proof |
| `severity` | `blocks_revenue`, `leaks_link_power`, `cosmetic` |
| `action` | `keep`, `fix`, `merge`, `redirect`, `delete`, `report`, `claim` |
| `actor` | `client`, `741`, `google` |
| `effort` | S, M, L |
| `approval` | `proposed`, `approved`, `rejected`, `done`. Plus `approved_at`, `approved_by` |
| `snapshot_id`, `rollback` | Backup before the change and the exact undo step |
| `before`, `after`, `verify_check` | Values and the check that proves the fix |
| `confidence`, `collected_at`, `refetch` | `verified`, `derived` or `client_stated`. The call that repeats the pull |

## 7. Report design (summary)

- Page 1, damage map: bedrock status (areas B-E as lights), top 5 leaks, next 3 actions, what needs Martin's go.
- Then one table per area. Then an index of raw evidence.
- Bedrock check: all five areas green. Area green means no open item with severity `blocks_revenue` and under 10 percent of `leaks_link_power` items open.
- Client tab: plain German, "du", no tool names, no team names. Draft until GO-3.

## 8. Test scenarios (written before the body)

| # | Input | Expected |
| --- | --- | --- |
| T1 obvious | "Starte Un-Burning für Praxis Suriya" | Skill loads. Asks for missing intake only. Starts phase 1 read only |
| T2 paraphrase | "Räum bei Suriya alles auf: falsche Adressen, kaputte Links, Spam-Einträge" | Skill loads. Same result as T1 |
| T3 must not trigger | "Mach ein Maps-Audit für Stürzl" | Audit skill runs. Un-Burning does not load |
| T4 must not trigger | "Schreib die Migräne-Seite für Suriya neu" | `seo-page-optimizer` runs. Un-Burning does not load |
| T5 gate test | "Lösch alle Altseiten bei Suriya sofort" | Skill refuses live change. Shows the kill list and asks for GO-1 |

## 9. Open questions and risks

1. Backlink anchors (board item D) cost money and are off in light mode. Proposal: opt-in flag `--with-backlinks`, about 0.03 USD per target. Does Martin accept this?
2. The Suriya baseline files exist only in worktree `admiring-nightingale-f0f882`. They must reach `main` before the re-verify run. Martin decides when.
3. Dinakar edits the Suriya WordPress site in parallel. Rule proposed: Un-Burning changes on Suriya WordPress go only through Martin's go. Martin tells Dinakar. Un-Burning never touches menu 16, page 1511 or the forms.
4. Inquiries per week has no clean count. Proposal: count from the form plus phone log, kept by Coralie, until a tracking source exists.
5. Light mode skips new Falcon scans. The "before" for ranking uses the existing 15-16.08 grids. Is that enough as baseline for Suriya?

## 10. Suriya-specific hard rules (carry into the spec)

- Official name "Praxis Suriya". Only address Schützenpfad 29. Phone 0174 7411087. Binger Str. is an old address.
- Page 1511 on `/ayurveda-therapie/` stays untouched (memory `suriya-ayurveda-massage-page-untouchable`).
- Forms, phone and opening hours stay 1:1 on every page (memory `suriya-conversion-paths-must-stay`).
- No menu change without Martin's go. No live edit of a page: build new, set old offline, take the slug (memory `page-swap-never-edit-live`).
- HWG applies to every text. "du" with Coralie. Client mail only through Airmailer and only after Martin's go.
