2026-10-11 · Step 0 Readiness ok: DataForSEO balance 17.23 USD, cap 5 USD. GSC API works for https://suriya-praxis.de/ (export 2026-07-11 to 2026-10-09: 300 queries, 61 pages) · 03-demand/gsc-api.json · next: Step 1
2026-10-11 · Step 1 Client baseline written from memory (locked data), live site (62 own pages measured, 90 sitemap URLs) and GSC; 7 [FEHLT] points · 01-client/client-baseline.md · next: Step 2
2026-10-11 · Step 2 Seeds: 302 + 62 terms in 2 Ads volume calls, 62 in 1 Labs call (11 terms where the Ads call had no data) · 03-demand/volume.json, volume2.json, volume3.json, labs-overview.json · next: Step 3
2026-10-11 · Step 3 Competitors: 12 SERPs, 24 sites in 4 tiers (11 local, 6 massage, 4 niche, 3 topic), 44 pages measured (all readable, apotheken-umschau.de returns 0 words = unreadable), 21 sitemaps (ayu-med.de sitemap unreadable, its pages readable) · 02-competitors/ · next: Step 4
2026-10-11 · Step 4 Demand: autocomplete tree (17 seeds), 8 ranked-keyword pulls, Trends (1 call, 5 terms), GSC API · 03-demand/ · next: Step 5
2026-10-11 · Step 5-6 Candidates (57 items, 6 cut) and build · 04-pool/candidates.json, pool.json, summary.json · next: Step 7
2026-10-11 · Step 7 Validator: 57 items, 0 errors, 1 warning (apotheken-umschau.de unreadable). Typed numbers in notes checked by script against GSC, overlap and metrics files · next: Step 8
2026-10-11 · Step 8 Report rendered, checked in headless Chrome (1440 px, 500 px, one opened card), xlsx 4 sheets · 05-report/content-pool-report.html, content-pool.xlsx · next: CHECKPOINT (Martin)
2026-10-11 · Step 10 Own pages measured (62), GSC pages and status of all 61 GSC URLs (52 ok, 8 redirect 301, 1 404 with 1 impression), 5-word text overlap of 58 pages, backlinks summary for client + 3 competitors · 05-sitetree/ · 03-demand/backlinks-*.json
2026-10-11 · Step 11-12 Sitetree: 49 nodes (30 Bleibt, 15 Überarbeiten, 0 Neu, 1 Vorschlag), 7 redirect proposals (4 only with Martin's go, 3 "not now" or sitemap tidy), rules S1-S8 pass (0 errors), checked in headless Chrome (1440 px, 500 px) · 05-sitetree/tree.json, sitetree.json, 05-report/content-pool-sitetree.html, .xlsx · next: CHECKPOINT 2 (Martin)
2026-10-11 · Client form draft (10 points, du, Ich-Form from Martin), not sent · 01-client/client-form-suriya-de.md
2026-10-11 · Spend 0.4797 USD of 5 USD cap (28 paid calls) · spend.jsonl
2026-10-11 · Not done on purpose: no Drive upload, no send, no commit, no live-site change, no new Local Falcon scan, no registry write (shared Excel outside this folder)
