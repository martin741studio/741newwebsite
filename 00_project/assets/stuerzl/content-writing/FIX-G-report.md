# FIX-G report: Batch G (ST-34, ST-35, ST-36, ST-37)

Date: 2026-10-11. Source: `REVIEW-G.md`. Text language: normal German. Report language: STE.

## Summary

| Page | Words before | Words after | Gates G1 to G6 | Cleanse calls | Backup |
| --- | --- | --- | --- | --- | --- |
| ST-34 Hub | 538 | 610 | pass (lint 5/5) | 1 attempt, failed (codex usage limit) | `05-final/page-vorreview.md` |
| ST-35 Strafe | 1672 | 1848 | pass (lint 5/5) | 1 attempt, failed | same |
| ST-36 Verjährung | 1284 | 1490 | pass (lint 5/5) | 1 attempt, failed | same |
| ST-37 Krypto | 1199 | 1467 | pass (lint 5/5) | 1 attempt, failed | same |

- The rival-model cleanse did not run. The codex call ended with "usage limit" (exit 1, new limit window at 17:20 per the message). Nothing was changed by a cleanse. G5 passes only in the lint. One cleanse call per page stays open. After it runs, `diff_claims.py diff` must pass.
- Word counts are above the brief range on three posts (ST-35 1848 of 1800, ST-36 1490 of 1300, ST-37 1467 of 1300). Every added sentence answers a review point. The source lists and the example in ST-36 can be cut first.
- `link_network.py` ran on a copy of the folder (it writes `LINK-NETWORK.md`, so I did not run it in the real folder). No similarity fail for the four pages. Link counts: ST-34 9, ST-35 6, ST-36 5, ST-37 4.
- Each page has a new draft `03-draft/draft-v3.md`, a rebuilt `05-final/` (page.md, cms-blocks.txt, placeholders.md, schema.jsonld draft, measure-plan.md), new claims, a new brief, an updated `OPEN-FLAGS.md` (section C) and `_run.json`.
- New sources are saved in `_work/`: see the lists below.
- `brief.nap_file` was not set in the four briefs. I set it. For posts the schema tool fails on placeholder text, so `byline.name` in the brief and `published:` in the front matter are empty. The visible placeholders stay in the text. `schema.jsonld` is a draft until the author and date are known (flag B6).

## Special points of this batch

| Point | Result |
| --- | --- |
| (1) ST-35 BGH limits | Primary text of BGH, 27.10.2015, 1 StR 373/15 (BGHSt 61, 28; HRRS 2016 Nr. 212) saved as `st-35.../_work/bgh-1-StR-373-15.html` and `.txt`. It states one limit: a large extent exists for every tax evasion above 50.000 Euro (Leitsatz 1, Rn. 29 to 32). The 100.000 Euro sentence is deleted. The 2025 use of the 50.000 Euro limit by the Landgericht Bonn is saved as an excerpt (`lg-bonn-62-KLs-1-24-auszug.txt`). Not checked: later BGH rulings after 2015 and whether they change the 2008 sentencing rules (six-digit amount, millions). The visible text says this. The line is in OPEN-FLAGS A1. |
| (1) Führungszeugnis | Corrected against the saved § 32 BZRG: Abs. 2 Nummer 5 and the exception in Abs. 4 (certificate for authorities, business context, § 149 Abs. 2 Satz 1 Nummer 1 GewO). The word "vorbestraft" is gone. |
| (2) ST-36 | § 78a StGB now quoted with Satz 2 from the saved text. § 376 Abs. 1 and Abs. 3 AO are stated with their limit "§ 370 Abs. 3 Satz 2 Nummer 1 bis 6". Ruhen (§ 78b StGB) is mentioned because the text was saved (`stgb__78b.txt`). |
| (2) Transition rule | The review named Art. 97 § 23 EGAO for the 15-year rule and the date 29.12.2020. I fetched and saved the text (`egao_art97_par23.txt`). It covers only § 376 AO in the version of the law of 19.12.2008. I found no transition rule for the 15 years and did not claim one. The text says only that for older acts the version in force at that time can matter. Open point: OPEN-FLAGS A4. |
| (3) ST-37 | Ten-year rule: wording of § 23 Abs. 1 Satz 1 Nummer 2 Satz 4 EStG and BMF Rn. 63 (not for Currency and Payment Token). The link to staking and lending is not in any saved text, so the page says only that the BMF letter has its own sections for them (flag A8). The 600-euro question is answered from § 23 Abs. 3 Satz 5 EStG and BMF Rn. 53 (1.000 Euro, up to VZ 2023 600 Euro, Freigrenze). No claim on a duty to declare. BMF date 6 March 2025 is in the saved header and on the saved BMF page (`bmf-seite-2026-10-11.md`). No later letter was found. The page says later changes were not checked. First KStTG report: derived from § 9 Abs. 1, § 10 and § 21 (31 July 2027). It is marked as a derivation in the claims and in flag A3. |
| (4) Rechtsstand line | True for each post now (law texts of 11 Oct 2026; ST-35 BGH 2008 and 2015, other rulings not read; ST-36 no rulings read; ST-37 BMF letter of 6 Mar 2025, later changes not checked). The hub no longer says that all posts reflect the state of 11 Oct 2026. Each post and the hub show "Zuletzt geprüft am 11. Oktober 2026". |
| (5) Directives | "Reichen Sie nichts ein" and similar lines are replaced by general information (ST-35 step 3, ST-37 step 2, ST-36 step 3). Step titles are now statements ("Beschuldigte dürfen schweigen"). |
| (6) Author, date, notice | All four pages have the author placeholder and the date placeholder in S01 (posts also in the last section). All four end with the notice line. The hub got the author and date placeholders and the notice line at the end. |
| (7) Hub links up | Added /steuerstrafrecht/ and /steuerstrafrecht/verteidigung-im-steuerstrafverfahren/ (both in `slugs.json`). The hub also has the three-line address block (decision 5), because it is not a post. Please confirm (flag A8 of ST-34). |

## ST-35 Steuerhinterziehung: Strafe und Strafrahmen

| Review point | Result |
| --- | --- |
| A1 100.000 Euro limit outdated | behoben und belegt: one limit 50.000 Euro, BGH 1 StR 373/15 cited, source saved, claim L09 and new claim L21 |
| A2 Führungszeugnis too absolute | behoben und belegt: § 32 Abs. 2 Nummer 5 and Abs. 4 BZRG; "gewöhnliches Führungszeugnis" vs. "für Behörden" |
| A3 "In beiden Fällen ... nicht als vorbestraft" | behoben: sentence deleted |
| A4 Waffen- und Jagdverbot, Passentzug | behoben: sentence deleted, no norm read (flag A2) |
| A5 Strafbefehl equal to a judgment | belegt: StPO § 407 Abs. 1, § 410 Abs. 1 and 3 saved and cited |
| A6 25.000 Euro limit too absolute | behoben: "grundsätzlich", § 371 Abs. 2 Satz 1 Nummer 3, Abs. 2a, § 398a |
| A7 § 153a incomplete | behoben: both missing conditions added, effect of fulfilled conditions added |
| A8 Vorsatz definition, wrong source | behoben und belegt: § 15 StGB plus BGH 1 StR 416/08 Rn. 41; the firm's definition is out of the text (flag A10) |
| A9 § 41 and § 40 paraphrase | behoben: "angebracht", "bereichert oder zu bereichern versucht", "wenn das Gesetz nichts anderes bestimmt" |
| B Directive "Reichen Sie nichts ein" | behoben: step 3 is general information |
| B Erstberatung wording | behoben: no mention of a first meeting on this page. The cost model stays on /kosten/ |
| B Title proof (C01) | bewusst offen: no Kammer proof, flag B2 |
| C "zuletzt geprüft am" | behoben |
| C Money page link at the end, two CTAs | behoben: link in S03 and S11, one CTA (S11), `cta_min` 1 |
| C Author line | bewusst offen: placeholder, decision with the firm (B1, B4) |
| E PAA "Wie lange dauert ein Strafverfahren" | behoben: answered without a number, with BGH 1 StR 373/15 Leitsatz 6 |
| E Table "Strafrahmen auf einen Blick" | behoben: table added in S03 |
| E Schema 20 | behoben als Entwurf: `schema.jsonld` exists, author and date empty until release |
| E Local 35 | teilweise behoben: offices named in the author box. The post stays national |
| Cross-page: 100.000 in other pages | geprüft: grep for "100.000" in the final pages of ST-11, ST-12 and ST-18 finds nothing |

New sources in `st-35.../_work/`: `bgh-1-StR-373-15.html/.txt`, `lg-bonn-62-KLs-1-24-auszug.txt`, `gesetze/stpo__407.txt`, `gesetze/stpo__410.txt`.

## ST-36 Verjährung der Steuerhinterziehung

| Review point | Result |
| --- | --- |
| A1 "15 Jahre" too absolute | behoben: "in den Fällen des § 370 Abs. 3 Satz 2 Nummer 1 bis 6 AO", "alle anderen Fälle: fünf Jahre" (§ 78 Abs. 3 Nummer 4, Abs. 4 StGB). Transition note: see special point (2); bewusst offen (A4) |
| A2 Beginn, § 78a Satz 2 | behoben und belegt: Satz 2 quoted. The BGH rules on Beendigung are not read; the text says so; flag A1 |
| A3 "Spätestens" contradiction | behoben: "grundsätzlich", reservation § 78b (§ 78c Abs. 3 Satz 3), Ruhen section |
| A4 FAQ "Wann fängt Steuerhinterziehung an" | behoben: old sentence deleted; new answer from § 370 Abs. 1, 2, 4 AO and § 78a StGB |
| A5 "bis zu zehn Jahre" | behoben: "zehn Jahre lang", the period can run longer (§ 171 AO) |
| A6 FAQ Durchsuchung "Ja" | behoben: the law names the judge's order (§ 78c Abs. 1 Nummer 4 StGB) |
| A7 § 170 Abs. 2 Nummer 1 incomplete | behoben: "in der Regel", "es sei denn ... später", § 170 Abs. 6 and 7 |
| A8 "zwei" vs. three periods | behoben: three periods in S02, S03 |
| B Title proof | bewusst offen (B2) |
| B Step 3 "bevor Sie etwas einreichen" | behoben: step section is now general information, no CTA there |
| C Money page link at the end, "zuletzt geprüft" | behoben |
| E Worked example | behoben: simplified example (return in 2022, end of 2032). Own calculation, flag A6 |
| E PAA answer | behoben (see A4) |
| E Local 35 | teilweise: offices named |

New sources: `gesetze/egao_art97_par23.txt`. Statutes already saved: `stgb__78a.txt`, `stgb__78b.txt`, `ao__376.txt`.

## ST-37 Krypto und Steuerhinterziehung

| Review point | Result |
| --- | --- |
| A1 one-year rule without the 10-year exception | behoben und belegt: wording of Satz 4, BMF Rn. 63; S02, S03 and FAQ changed. Staking and lending link: bewusst offen (A8) |
| A2 "bleibt der Steuerpflichtige verantwortlich" in the intent paragraph | behoben: sentence deleted; § 150 Abs. 2 AO in the duty sentence; Vorsatz from § 15 StGB and BGH Rn. 41 |
| A3 600-euro question not answered | behoben und belegt: answered from § 23 Abs. 3 Satz 5 EStG and BMF Rn. 53; no claim on a duty to declare |
| A4 BMF letter currency | belegt: date from saved header and BMF page; "later changes not checked" is visible; flag A1 |
| A5 KStTG date and limits | belegt (derived): first report 31 July 2027; § 2 scope; § 13 other states; flag A3 |
| A6 Selbstanzeige: 25.000 Euro and § 398a | behoben: added with the wording of the saved § 371 |
| B Directive "Reichen Sie nichts vorschnell ein" | behoben: general information |
| B Title proof | bewusst offen (B2) |
| B Scope: tax law | bewusst offen (A2): the firm must confirm and the specialist lawyer must read the tax parts |
| C Money page link in the first third | behoben: end of S03 and S10. "zuletzt geprüft" added |
| E Selbstanzeige section too short | behoben: section S06 now covers exclusion, 25.000 Euro, § 398a, payment |
| E Date of the first report | behoben (see A5) |

New sources in `st-37.../_work/`: `bmf-seite-2026-10-11.md`. Already saved: `bmf-krypto-clean.txt`, `gesetze/estg__23.txt`, `gesetze/ksttg.txt`.

## ST-34 Ratgeber (Hub)

| Review point | Result |
| --- | --- |
| A1 15 years and "bis zu zehn Jahre" | behoben: same wording as ST-36 (claim H02 updated) |
| A2 "Rechtsstand 11. Oktober 2026" not true for the posts | behoben: sentence deleted; the hub says each post names its sources and check date |
| A3 "sobald eine Behörde eine Maßnahme trifft" | behoben: list of § 397 Abs. 1 AO (Finanzbehörde, Polizei, Staatsanwaltschaft, Ermittlungsperson, Strafrichter) |
| B Card "Steuerfahndung vor der Tür" | behoben: "Was gilt bei einer Durchsuchung?" |
| B Title proof | bewusst offen (B2) |
| C FAQ repeats the posts (cannibalisation) | behoben in part: answers are short and point to the post. Content overlap remains by nature of a hub |
| C Keyword conflict A1 | bewusst offen: Martin decides |
| E Definition and overview | behoben: definition from § 369 Abs. 1 AO in the answer block |
| E No link up to ST-11 or ST-12 | behoben: both linked in S02 |
| E Cities in the first screen | behoben: S01 names Frankfurt am Main and München |
| E Schema 20 | behoben als Entwurf (schema.jsonld, author empty) |

New sources in `st-34.../_work/gesetze/`: `ao__369.txt`, `ao__171.txt` (copied from the saved texts of ST-35 and ST-36).

## Open points for Martin or the firm

1. Author of the four texts and the publish dates (B1, B4). Titles: no Kammer proof (B2).
2. Specialist lawyer to read: BGH rulings after 2015 (ST-35), the 15-year transition rule (ST-36), the BMF letter and later changes, the staking and lending link, and the date 31 July 2027 (ST-37).
3. Cleanse: one call per page is still open (codex limit).
4. Confirm that the hub carries the address block.
5. Suggestions for the skill: the G2 rule "Superlativ" hits the statute phrase "nach bestem Wissen und Gewissen" and the rule "gewinnen" hits "Gewinnen" as a noun. The schema tool fails on blog placeholders; allow an empty author in the brief.
