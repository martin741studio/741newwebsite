# Scorecard: today's homepage (heilpraxis-heckel.de, desktop 1440)

Source rule: `knowledge/cro-library/_derived/scorecard.md` (22 items, score 0/1/2).
Screenshot: `evidence/home-today-1440.jpg` (first screen, cookie banner not shown).
Text: `evidence/site-text-2026-10-15.txt` (curl of the homepage and subpages).
Scores 0 and 1 have an evidence line.

| # | Rule | Prio | Score | Evidence |
| --- | --- | --- | --- | --- |
| 1 | Hero: what, for whom, next step in 5 seconds | A | 1 | Screenshot shows name and "Heilpraktikerin für Psychotherapie und Coach". No next step visible. |
| 2 | Headline = result + city | A | 0 | Screenshot: greeting "Herzlich willkommen!" is the first headline. No city, no result. |
| 3 | Sub-headline: situation first, then 3-4 help | A | 1 | Text: "bei mir sind Sie richtig, wenn Sie psychotherapeutische Begleitung suchen". Below the fold. |
| 4 | Primary CTA visible on 1440x800 without scrolling | A | 0 | Screenshot: no button in the first screen. |
| 5 | CTA text names next step and benefit | A | 0 | Only text links "MEHR INFOS" (3x) in `site-text-2026-10-15.txt`. |
| 6 | Reassurance under the CTA | A | 0 | No CTA, so no reassurance line. |
| 7 | Two proof forms above the fold | A | 0 | Google panel: 0 reviews, "Keine Rezensionen" (`google-panel-2026-10-15.md`). No quote on the site. |
| 8 | Face and qualification in hero or section 2 | A | 2 | Screenshot: photo of Gabriele Heckel in the hero. Title beside it. |
| 9 | "Erster Termin": 3-4 steps, duration, price | A | 1 | Text: "Ihre Einstiegsstunde: 45 Minuten für 35 €". No steps listed. |
| 10 | One accent colour for CTA; blur test | A | 1 | Yellow accent only on nav link "STARTSEITE" and a rule. No CTA to test. |
| 11 | CTA repeats every 2 sections | A | 1 | Three "MEHR INFOS" text links, no CTA button. |
| 12 | Reviews open, name + Google logo + heading | B | 0 | No reviews on site; Google has 0 reviews. |
| 13 | Proof heading carries a benefit | B | 0 | No proof block. |
| 14 | 3-4 proof blocks spread over page | B | 0 | No proof blocks. |
| 15 | Situation section: 3-5 situations, HWG-clean | B | 1 | Text: "Leid und Krisen zu überwinden" and "Ihr Körper und ihre Seele können sich erholen". Situations present, not HWG-clean (see 22). |
| 16 | Services as cards with benefit heading and link | B | 1 | Three teasers with "MEHR INFOS". Headings: "Psychotherapie", "Coaching für mehr Lebensenergie", "Heilsame Berührungen". Not cards in the screenshot. |
| 17 | FAQ with real objections | B | 0 | No FAQ on homepage. |
| 18 | Location: map, address, parking, transport, hours | B | 1 | Address on Kontakt page only ("Friedrich-Zeitler-Strasse 23, 92242 Hirschau"). No map or hours on homepage. |
| 19 | Closing section = mini hero with CTA | B | 0 | Homepage ends with "Kostenlose Leseprobe" download. No closing CTA. |
| 20 | Each section heading states a point | C | 0 | Headings: "Herzlich willkommen!", "Bevorstehende Veranstaltungen", "Kostenlose Leseprobe". Labels, no statement. |
| 21 | Typography: headline 3-4x body, body 16 px or more | C | 1 | Not measured (no computed styles, Chrome not used). Screenshot: body text readable, headline size visible. Partial. |
| 22 | Health: no HWG breach (no healing promise, no before/after, no fear) | A | 0 | "Leid und Krisen zu überwinden"; "Heilsame Berührungen"; "Ihr Körper und ihre Seele können sich erholen". Hard gate: one breach = 0. |

## Total

- Sum: 11 of 44 (scale in `scorecard.md`: 36 of 44 needed).
- Prio A items at 2: 1 of 12 (item 8 only). Prio A not met.
- Item 22 = 0: hard gate fails. No checkpoint.
