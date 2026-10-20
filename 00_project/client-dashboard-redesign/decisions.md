# Decisions — client dashboard and report redesign

Format: round, question, answer, date. Martin decides. Recommendation was first option.

## Round 1 (2026-10-13) — foundation
| # | Question | Answer |
|---|---|---|
| 1 | First screen content | 4 numbers + 1 sentence. Everything else one click deeper. |
| 2 | Long report | Summary page + one page per topic (Found on Google, Enquiries, Reviews, Ads, Backlinks, Plan). Each page: one question, 1–3 charts. |
| 3 | Technical terms | Plain words on the page, technical term in small print. |
| 4 | Pilot | Bali Healing only. Roll out after Martin's go. |

## Next
Round 2 starts when the six research files in `00_project/knowledge/client-dashboard-library/` are done. One area per round, max 4 cards, recommendation first.

## Round 2 (2026-10-13) — first screen
| # | Question | Answer |
|---|---|---|
| 5 | First-screen layout | A "Three questions": cards Enquiries, Found on Google, 741 at work; each with one number + one sentence; then a "Needs you" card. |
| 6 | Cost includes 741 fee? | No. Ad spend only. |
| 7 | Currency (Bali) | IDR only, as Google bills it. |
| 8 | Sentence under each number | Auto-draft from the numbers, 741 checks weekly before the client sees it. |

## Round 3 (2026-10-13) — results pages
| # | Question | Answer |
|---|---|---|
| 9 | Enquiries page | A: answer line + four tiles (one per channel, 6 monthly columns, current month hatched, WhatsApp before Aug = dashed "not tracked" slot). |
| 10 | Reviews page | Scoreboard (rating, count, unanswered) + bars you / leader / target (2x leader) + monthly pace. |
| 11 | Found on Google page | A: headline sentence + 3 tiles (map, normal results, AI) → big grid → You win / Close / Missing → competitors → AI strip. All-keywords list behind a link. |
| 12 | Name for SoLV | "Top-3 coverage" as a count ("31 of 49 spots"); German "Top-3-Abdeckung"; SoLV in small grey print. |

Data checks before design (from research B/C): do we store the 49 point values per keyword (or only the image)? sample size per AI cell? how is the 45-of-100 clinic score calculated? which ARP rule do the scans use? cause of the 15–23 Sep zero website clicks (possible data delay)?

## Round 4 (2026-10-13) — status, colours, ads, backlinks
| # | Question | Answer |
|---|---|---|
| 13 | Status frame | B: "Needs you" first, one column: banner sentence → Needs you (decision + access cards) → phase line → 741 works on (max 5 rows) → next four weeks → done recently → who to ask. |
| 14 | Colour and word rule | Two layers. Colour = health only: green fine, amber needs someone soon, red costs the client now, grey not started / no data. Each with shape and word. Progress (Planned, Doing, To check, Done) is plain text. These four colours never appear in charts. |
| 15 | Ads page | A: status pill + three tiles (spent, WhatsApp clicks, cost per WhatsApp click) + weekly bars + gap card "Booked jobs: not tracked yet. Tell us." |
| 16 | Backlinks page | A: sentence + five step rows (requests, messages, in talk, offers, live) + four health tiles (links, sites, broken, rated risky). Plain words, never "toxic". |

## Round 5 (2026-10-13) — structure
| # | Question | Answer |
|---|---|---|
| 17 | Tabs | Overview · Results · Plan · Decisions · Reports (dated archive). Setup shows only while open. Chat is one button, always visible. Results = five pages: Enquiries, Found on Google, Reviews, Ads, Backlinks. |
| 18 | Onboarding and access | Setup tab only while open. Ticks come from real data. Seven platforms in one compact list with check date. Open steps move into "Needs you" after week 2. When all done: tab disappears, one line "Setup complete". |
| 19 | Plan tab | 12 tracks as three-stage groups (Not started, In progress, Live) with one-line outcome; site structure as expandable outline with a badge per page; content plan: 19 priority first, "x of 19 live", 26 later. |
| 20 | Automatic colours and warnings | Automatic. Red = blocker with real effect today or overdue. Amber = client action open over 3 days, due within 7 days, or update missing. Grey = no update for 10 days or no data. Green = none of these. The client sees a warning banner only after Martin releases it. |

## Round 6 (2026-10-13) — look and production
| # | Question | Answer |
|---|---|---|
| 21 | Look | 741 look, calmer: cream background, 741 yellow as accent for one key number and buttons, DM Sans, condensed headline only for page titles, charts in one neutral ramp plus the four fixed status colours. |
| 22 | Martin guide figure | Overview ("point" next to the one sentence) and empty states ("think"). Max one per page. Never in charts or tables. |
| 23 | Production | Results pages (Enquiries, Found on Google, Reviews, Ads, Backlinks) come from stored data in one template for all clients, plus the weekly sentence. Special documents (site tree, text drafts, previews) stay hand-made but follow the same rules. Every number has a date and a source. |
| 24 | Old reports | Reports tab = dated archive. Old versions are marked "replaced" with a pointer to the current page. Nothing is deleted. |

## Round 7 (2026-10-13) — after the data check (`02-data-readiness-bali.md`)
| # | Question | Answer |
|---|---|---|
| 25 | Fix three wrong statements on the live Bali roadmap | Yes. Done 13.10.: review-reply row, Sep contact row + flatline text, "45 of 100" wording. Backup `clients.741.studio/backup/balihealing-seo-roadmap-2026-10-13-pre-fix.html`, copy `_src/bali-roadmap-live-2026-10-13.html`, new file `_src/bali-roadmap-v3.1.html`. Not touched: footer "v2, reviewed 23 Sep", footer "2 open decisions", Track 9 30-day totals, `client_reports` row date 23.09. |
| 26 | Two Google profiles | One page with a switch between Natural Health Center and Beauty Clinic. Overview shows both in one card. |
| 27 | Booked jobs for Bali | Peggy or Pasha send one monthly count. 741 enters it in the portal. |
| 28 | Backlink tiles | "Links we can use" counts checked sites only. One grey line "Ignored: spam links, not from you." |

## Data facts that change the design
- The September zero-click gap was a Google data delay (68 clicks now shown for 15–23 Sep).
- Review replies: 79 of 100 have a reply. The 8 newest do not.
- The 45-of-100 score is "Profile and site readiness" of our audit, not a rank against clinics.
- AI cells have 9 samples from one run (23 Sep). Show "x of 9 spots" with the date, no trend before 3 runs.
- Map top-3 share: only "ozone therapy" has a same-setting history. Other keywords have 1 scan. Grid points are not stored (fix: save `data_points` at each scan).
- Average map rank (ARP) skips spots where the business is not found. Show "spots found" next to it.

## Design checkpoint (2026-10-13)
| # | Question | Answer |
|---|---|---|
| 29 | Prototype v1 | Approved. Build on staging. |

## Staging build (2026-10-13) — nothing live
- Module "Dashboard (neu)": `portal/src/dsh.js`, `dsh.css`, `build.py` (marker blocks, idempotent), feed `portal/src/feed-bali.json`, smoke test `portal/src/smoke.js`.
- Uploaded to `clients.741.studio/staging/index.html` and the feed to `clients.741.studio/r/a331bf716f08/dashboard.json`. Live `index.html` is unchanged. Staging before: `portal/out/staging-before-2026-10-13.html`.
- Only Bali Healing (client id in `DSH_FEEDS`) gets the new view. Admin sees a yellow button "Neues Dashboard (Vorschau)" on the Bali page. Other clients are unchanged.
- Decisions tab shows only when the approval module is on for the client (Bali: not released yet; the 6 decisions open the roadmap page until then). Setup steps are derived from real data (display only, nothing is written).
- Not done: weekly refresh job for the feed (numbers are the 13 Oct snapshot), German labels, a real client login test, live release.

## Live release (2026-10-13, Martin: "Yes, go live now")
- Live `clients.741.studio/index.html` now has the module "Dashboard (neu)" (only Bali Healing). Backup: `clients.741.studio/backup/index-2026-10-13-pre-dashboard.html` (also `portal/out/live-prerelease.html`). Release file: `portal/out/live-release.html`. Live equals the release file (byte compare). Admin check on live: button and all views load, no console errors.
- Not tested: a real Bali client login (Peggy/Pasha). The numbers are the 13 Oct snapshot until the refresh job exists (follow-up session proposed).
- Rollback: upload `portal/out/live-prerelease.html` as `index.html`.

## Fix release 1 (2026-10-13, Martin's feedback on the live dashboard)
- Back button: every dashboard view is a browser history entry (`#d/<view>`). Back moves inside the portal. A report opens in the portal's own viewer; the back link inside a report closes the viewer. Tested as a real Bali client login on staging: Back from Found → Plan → Overview, report open/close, no re-login.
- Decision cards: the Needs-you list and the Decisions tab now come from the approval module (not from roadmap links). The admin preview also shows drafts, marked "Draft". A client sees only released items. Bali has 7 drafts (B1–B7), so the client sees none until Martin releases them.
- Overview shows both Google profiles (Beauty Clinic line and "Biggest gap" line).
- Live uploaded. Backup: `clients.741.studio/backup/index-2026-10-13-pre-dashboard-fix1.html`.
- Blocker for releasing Bali's decision cards: the approval module card text is German only on live. An English version exists in `00_project/client-approval-workflow/portal/src/ap.js` (other chat, not live).

## Rollout step 1 (2026-10-14, Martin: "Yes, Hüwel first, then the others")
- Module made client-neutral without touching Bali: new generic view in `portal/src/dsh.js` (`DSHL` de/en string table, `dshG*` pages). It runs when the feed has no `nhc` block. Bali pages stay as they are (regression: 20 views byte-identical to live).
- Hüwel feed `clients.741.studio/r/68044e8de1b5/dashboard.json` (built by `portal/feed/build.mjs --client huewel`). `DSH_FEEDS` has Bali and Hüwel.
- Tested on staging with the real Hüwel client login (German): Overview, Ergebnisse (Anfragen, Bei Google gefunden), Berichte; no console errors. Not live yet. Waiting for Martin's go.
- Next clients need: feed config `portal/feed/clients/<slug>.json`, entry in `DSH_FEEDS`, grants for Search Console / GA4 (see bulk/INDEX.md, Dashboard readiness).

## Rollout step 2 (2026-10-14): nine clients live
- `DSH_FEEDS` has 9 clients: Bali, Hüwel, Dumann, Stürzl, Johni, Suriya, Maria, Rabenmütter, Kamil (feed hashes in `clients/<slug>.json`). Feeds uploaded with `feed/deploy.mjs feeds`. Live portal: backup `index-2026-10-14-pre-dashboard-9clients.html`, release file `portal/out/live-release5.html`.
- Fixes in the generic view: null-safe sentences (no "mehr als" when the previous month is null), cards and tabs hidden when data is null, empty-overview message, week bar from `meta.week`/`weeks`, new Files tab (materials upload) for the generic view.
- Bali view unchanged (20 views byte-identical). Bali still has no Files/Materials tab in its own layout.
- Not browser-tested after this release (Chrome login expired). Node tests passed for all 9 feeds.
- Data gaps by client: see `00_project/client-approval-workflow/bulk/INDEX.md` (Dashboard readiness). Maria and Suriya: no Search Console access (403). Kamil: no program, reports only. Rabenmütter: Search Console only from 29 Aug.

## Rollout step 3 (2026-10-14, late): Google profile data in the generic view
- Feed keys `main` (calls/web/dir per month), `rev.main` (reviews) and `map` (top-3 spots of 49 per keyword) are rendered: Enquiries tiles, Reviews page, "Läuft gut / Nah dran / Noch nicht sichtbar" map list, map-based overview card when Search Console is missing.
- Feeds uploaded: Suriya, Maria, Stürzl. Hüwel stays without Maps (Martin 14 Oct). Dumann waits (which of the two Google entries is real).
- Live portal backup: `index-2026-10-14-pre-dashboard-google-data.html`; release file `portal/out/live-release6.html`. Live module checked in node against all 8 live feeds: no undefined or NaN. Bali: 20 views identical. Not browser-tested (Chrome login expired).
