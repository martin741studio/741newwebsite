# Content Pool: Test Scenarios, Dry Run Result, Scorecard

Date: 2026-10-11. Scorecard source: `00_project/knowledge/workflow-library/_derived/scorecard.md`.

## 1. Test scenarios (written before the skill body, see the design note section 7)

| # | Type | Prompt | Expected |
| --- | --- | --- | --- |
| T1 | Obvious trigger | "Content-Pool für Dumann, danieladumann.de, Berlin-Charlottenburg" | Skill loads. Asks for the cost cap and the mode. Creates the run folder. Runs Step 0. |
| T2 | Paraphrase | "Welche Inhalte braucht die neue Seite von Dr. Adel, damit sie lokal vor den Wettbewerbern landet? Nimm Wettbewerbsdaten und echte Suchnachfrage." | Skill loads. Industry mode is BRAO, not HWG. |
| T3 | Must NOT trigger | "Schreib den Text für die Leistungsseite Hildegard-Medizin Berlin." | `seo-page-optimizer` handles it. |
| T4 | Must NOT trigger | "Mach den Seitenbaum mit Einzugsgebiet für Suriya." | The structure playbook handles it. |
| T5 | Must NOT trigger | "Bau mir den Prototyp der Startseite für Dumann." | `cro-homepage` handles it. |
| T6 | Paraphrase | "Welche Fragen stellen Leute zu Aderlass, und was davon sollten wir auf Dumanns Startseite beantworten, gemessen an dem, was die Konkurrenz abdeckt?" | Skill loads. |

**Result (proxy, 2026-10-11).** A fresh agent saw only the skill descriptions and the prompts. It chose: T1 content-pool, T2 content-pool, T3 seo-page-optimizer, T4 none (the structure playbook is not a skill), T5 cro-homepage, T6 content-pool. All six are as expected.
**Limit.** This is a routing proxy. The skill is not installed. The real trigger test (fresh session, skill installed) is open.

## 2. Functional test: the Dumann dry run

Real task, solved with the draft tools. Result in `00_project/assets/dumann/content-pool/`. 42 items, validator passed (0 errors, 3 warnings), report checked in Chrome, paid spend 0.38 USD for 22 calls.

Where the run stalled, guessed or needed a fix (each fix is now in the spec or a script):

| # | What happened | Fix |
| --- | --- | --- |
| 1 | `website-struktur-master-prompt.md` is only in a worktree, not on `main`. | Open: bring it to `main`. |
| 2 | GSC returned 403 for the service account. | Read the table in Chrome first (rule R-S5 added). Martin then added the service account. The API export works for the `www` property only and matches the hand read within about 4 %. Step 0 tests both addresses. |
| 3 | One competitor site blocked HTTP, headless Chrome and Firecrawl. | Reported as unreadable. The related claim carries a caveat. |
| 4 | SERP for "hildegard medizin berlin" returned no items. | Use a second query. Gate A0 says retry. |
| 5 | JS sites gave 48 and 55 words by HTTP. | Headless Chrome fallback in `page_metrics.py`. |
| 6 | First scoring gave 28 items priority A. National head terms inflated demand. | Rules R-S1 to R-S4. Now 10 A. |
| 7 | I typed "3 von 13" into a note. The data said 3 of 12. | Notes must not hold computable numbers. Validator checks volumes. Claim check added to Step 7. |
| 8 | Live-site check matched Wix event pages as service pages. | URL exclusion rule. Result is still coarse. |
| 9 | Autocomplete samples held brand and review noise. | Noise filter in `build_pool.py`. |
| 10 | The Local Falcon tool is not in this session. | Existing scan from the CRO dataset is used. No new scan. |

Context that I had to supply by hand (this is what the skill body must carry): the service list of the client, the two-audience split, which competitors are portals, the HWG wording rules, the fit scale, the CRO P0 rows.

## 2b. Functional test 2: Stürzl (law firm, BRAO, 2026-10-11)

Second real client, different type. 53 items, validator passed (0 errors, 0 warnings), 45 sitemap nodes with rules S1 to S8 passed (a test with planted errors caught all of them on the Dumann data). Paid spend 0.47 USD for 31 calls.

| # | What happened | Fix |
| --- | --- | --- |
| 1 | No GSC access (403 on three property forms). | Reported as `[FEHLT]`. The pool runs without own queries. |
| 2 | The site has no sitemap. | Crawl fallback in `site_urls.py`, list cap raised to 5,000. |
| 3 | Three SERPs came back empty with cost 0 (`location_name` invalid for the city). | Repeated with `location_code`. |
| 4 | zsh did not split the domain list, so a crawl ran on one "domain" with the whole list. | Pass the list by command substitution. |
| 5 | No item reached A. All scores 60 to 74. | Rule R-S6. Dumann unchanged (checked). |
| 6 | Reasons and "not built" text were fixed Dumann sentences in the renderer. | Moved into `tree.json`. The Dumann report text stayed identical. |
| 7 | I typed "9 Personen" for the team. The site lists at least 9 and one unclear entry. | Wording changed to "mindestens 9". |
| 8 | The client form used "wir". The house rule is "ich". | Rewritten. |

## 2c. Functional test 3: Hüwel (health, HWG, relaunched site, 2026-10-11)

45 items, validator passed, 27 sitemap nodes with rules S1 to S8 passed. Paid spend 0.32 USD for 25 calls. Search Console was read in Chrome (service account has no access).

| # | What happened | Fix |
| --- | --- | --- |
| 1 | The site was relaunched on 2026-10-06. GSC mixes old and new, and DataForSEO knew only 2 own keywords. | `gsc_note` in `tree.json`; GSC read by hand; lesson 22. |
| 2 | A token `{words:ST-12}` appeared as literal text in the pool report. | Typed number, check for braces in the rendered HTML (lesson 24). |
| 3 | The "best position" of a pattern group came from an English query (position 1.0). | Quote impressions only (lesson 25). |
| 4 | Static slugs end in `.html`; the sitemap check wanted a trailing slash and had fixed city names. | Rule S4 widened, place rule reads `meta.places` (lesson 27). Dumann and Stürzl re-checked. |
| 5 | A headless Chrome screenshot hung, and `timeout` does not exist on macOS. | Background run with kill loop (lesson 26). |
| 6 | I typed "12 questions" for the FAQ. The markup holds 4. | Corrected. The home FAQ markup was counted from the live page. |

## 3. Baseline (with vs. without the skill)

Not run. It needs a client run without the skill, or Martin's judgment on the top 20 of Dumann and Stürzl (the agreed success test: Martin keeps 80 % of the top 20 items). Open. A second client type is now covered by the Stürzl run.

## 4. Scorecard

Scale: 0 missing, 1 partly, 2 done.

| Section | Score | Max | Notes |
| --- | --- | --- | --- |
| A Fit | 5 | 8 | A1 2. A2 1 (cap is enforced in a script, no hook). A3 1 (paid calls, model may trigger it; Martin chose this). A4 1 (committed as a draft in the repo, not installed). |
| B Design | 10 | 10 | Use cases, scenarios first, hard task solved by hand, inputs and out-of-scope, degrees of freedom. |
| C SKILL.md | 14 | 16 | C3 1 (detail sits in the project docs, `references/` is empty). C5 1 (scripts tested only on one client; weights are named constants in docs). |
| D Verification | 9 | 12 | D1 2, D2 2, D3 2, D4 2, D5 1 (proxy only), **D6 0 (no baseline)**. |
| E Unattended | n/a | n/a | Steps 0 to 8 run attended. No schedule. |
| F 741 house rules | 9 | 10 | F1 1 (Drive upload and client message wait for Martin's go). Others 2. |
| **Total** | **47** | **56** | **83.9 %** |

**Blocking zero:** D6 (no baseline). The rule is "no 0 in A or D". Decision: **fix first**. To ship: install the skill, run the real trigger tests, run the baseline or Martin's top-20 judgment, and run one more client of another type (new site or non-health).
