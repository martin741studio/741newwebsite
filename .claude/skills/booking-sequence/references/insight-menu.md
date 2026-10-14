# Insight menu, paid-call menu and case pick (booking-sequence)

## 1. What counts as a NEW insight
The prospect already saw the review page (`booking/baseline.md`). An insight is new only when it is NOT on that page. Martin's aim: "show her that we invested more time … we figured a bit more out."

Pick in this order and take the first two that hold (one for message 1, one for message 2):
1. **A change on the site since the review page.** `site-check.json` → `changed_since_review` (or compare `title`, `h1`, words with baseline.md by hand for old pages). Say what got better (honest praise, one sentence) and what is still open. **No change found:** do not invent one. Name one real strength of her site in one sentence (quoted from `booking/evidence/home.html` or a saved `booking/evidence/page-<name>.html`), then go straight to the new finding.
2. **Ranking today for the main money term** (paid call A): "nicht unter den ersten 50 Treffern" or "auf Platz 23". Only from the SERP evidence of today.
3. **A demand pocket the page did not show** (paid call B): a neighbouring city, a sub-service, a question term ("was kostet …", "… in der Nähe"), with real monthly volume.
4. **A blocker that Google sees in the raw page** (free): few visible words in the raw HTML (page loads by script), `noindex`, missing https redirect, title or main heading without the service or the town, no phone link. Explain in plain words, never "H1", "Canonical", "Schema", "SoLV", "NAP".
5. **Who wins the term today** (from the SERP call): "Die ersten drei Treffer sind Verzeichnisse, keine Praxis" — no bad-mouthing of named competitors.
6. **A strong page that nobody finds on her own site** (free): read the sitemap or the menu, curl the 5–10 main pages, and check which pages link to a strong article or service page. "Dein Artikel über X ist nur von der Seite Seminare aus verlinkt" + the volume of its topic. Save each page as `booking/evidence/page-<name>.html` for the quote.

Before you use an insight, search the section "Visible review-page text" in `booking/baseline.md` (what she saw) and the video text (`evidence/loom-transcript.md`, else `loom-script.md`). If either already says it, it is not new. The other sections of baseline.md are internal notes: a fact that is only there is still new for her.

Never: "unclaimed" / "nicht beansprucht" (Google profile ownership cannot be seen from outside), invented numbers, tool names, a repeat of the review page's main finding without anything new.

## 2. The traffic example (message 1, required)
- Take ONE volume term that fits the prospect's real service (and town for local businesses), from today's call or from the review run's `evidence/dfs-volumes-ads.json` when nothing better is new.
- Formula: 5 % of the monthly searches, rounded with "rund". Model sentence: „Schon 5 Prozent dieser Suchen wären rund 145 Besucher im Monat.“ Small volumes (under 200): use 10 % and say "jede zehnte Suche".
- It is an example, never a promise: no "garantiert", "sicher", "wirst du bekommen".
- Put the number pair into `claims.json` with `"derived": "2900 * 0.05 = 145"`.

## 3. Paid calls (max 3 per booking, cap 0,30 USD)
Always: `python3 00_project/prospect-mini/scripts/dfs.py 00_project/prospects/<slug>/booking <endpoint> '<json>' <out> 0.30`
(the booking folder is the ledger dir, so the review-run costs do not count against the cap; evidence lands in `booking/evidence/`).

| Call | Endpoint | Payload | Cost seen |
|---|---|---|---|
| A ranking | `serp/google/organic/live/regular` | `[{"keyword":"<term>","location_code":2276,"language_code":"de","depth":50}]` | 0,008 USD |
| B volumes | `keywords_data/google_ads/search_volume/live` | `[{"keywords":[<8-15 terms>],"location_code":2276,"language_code":"de"}]` | 0,09 USD |
| C local pack | `serp/google/maps/live/advanced` | `[{"keyword":"<service> <city>","location_code":2276,"language_code":"de","depth":20}]` | ≈ 0,01 USD |

- Where to measure: a **local term** ("heilpraktiker coburg") is measured from her town: replace `location_code` with `"location_name":"Coburg,Bavaria,Germany"` (format City,Region,Country). A **country-wide term** (an online offer, "online paartherapie") uses the country code. In the message, say where it was measured when it is local ("bei einer Suche aus Coburg").
- Country codes: DE 2276, AT 2040, CH 2756. Read `intake.json` → `location_code` when it exists.
- Health terms: volumes ONLY from the Google Ads endpoint (Labs returns none). No volume = "Google gibt keine Zahl heraus", never "0".
- Google merges close variants ("heilpraktiker x" / "heilpraktikerin x"): never add them up.
- A task status other than 20000: retry once, then drop that insight.
- Reuse first: if the review run already holds the data you need, use it and do not pay again.

## 4. Success story (message 2, or message 1 when merged)
- Source: `00_project/prospect-mini/case-library.json` only (`cases` with start + changes, `more` with jumps only).
- Branch map (prospect → case `branch`): health → gesundheit, heilpraktiker, psychotherapie, physio (pick the closest); law → recht; coach / consultant → beratung, dienstleistung; trade / other → dienstleistung.
- Pick: same branch first, then the most shared `gaps` with today's findings. Prefer a case that is NOT on her review page and not in her Loom (search the name in `booking/baseline.md` and `evidence/loom-transcript.md`). If every fitting case is already there, reuse the best fit and give one fact from the entry that the page did not show. Coaches / consultants without a branch match: Maria Abel (beratung) or Astrid Lengauer (dienstleistung).
- Never use a fact that the library marks as open or unclear (`_note`, for example the Laserstein start rank).
- Use only the facts in the entry: name, town/area, start state, 1–2 changes, the result (`jump`, `jump_sub`, or the result line in `changes`). Every number goes into `claims.json` with source `00_project/prospect-mini/case-library.json`.
- Health prospects (HWG): the story talks about Google visibility only (Platz, Karte, Sichtbarkeit), never about health results, patients or healing.
- Health search terms in any message: name them neutrally as what people search for ("danach wird gesucht"), never as a promise to treat ("ich helfe dir bei X"). Do not use terms for serious diseases (for example Krebs, Diabetes, Depression, Sucht); then pick a service term ("heilpraktiker wechseljahre").
- Close with the point Martin wants: often only a few points had to get better („Oft sind es nur wenige Punkte.“).
