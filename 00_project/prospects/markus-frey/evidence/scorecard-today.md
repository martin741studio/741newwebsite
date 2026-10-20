# Scorecard: stressfrey.de homepage today (22 items)

Source: `evidence/home-today-1440.jpg` (first screen, 1440 x 801, cookie banner declined by operator) and `evidence/home-raw.html` (curl, 2026-10-15, for text items). Only the first screen is a screenshot. Items that need the full page use the text dump. Scale per `knowledge/cro-library/_derived/scorecard.md`.

| # | Rule (short) | Prio | Score | Evidence |
| --- | --- | --- | --- | --- |
| 1 | Hero says what, who, next step in 5 s | A | 1 | Banner reads "Spitzenenergie - auch morgen noch!" (image). Nav says "Online Coaching". No sentence names the service in the first screen. |
| 2 | Headline = result + city | A | 1 | Result present ("Spitzenenergie ... auch morgen noch"). City not in first screen. "Köln" only in the author line (home-raw.html, "Markus Frey, Köln"). |
| 3 | Sub-headline: situation, then 3-4 help points | A | 1 | Subline "Auch in herausfordernden Zeiten, Krisenzeiten gar, dauerhaft Zugriff auf die persönliche Spitzenenergie erhalten" (situation). Help points are slogans in the checkmarks, not concrete help. |
| 4 | Primary CTA fully visible on 1440 x 800 | A | 1 | "Kostenloses E-Book sichern!" fully visible at y 731-785. It is a lead magnet. The consult CTA "Kostenloses Kennenlern-Coaching sichern!" is only in the text below the fold. |
| 5 | CTA text: next step + benefit | A | 2 | "Kostenloses E-Book sichern!" names the step and a benefit. |
| 6 | Reassurance line under CTA | A | 0 | No line under the E-book button in the first screen. Text dump has no reassurance near the CTA. |
| 7 | Two proof types above the fold | A | 0 | First screen has a video thumbnail and a banner. No rating, review, number or quote. home-raw.html has no "Bewertung" text. |
| 8 | Face + qualification of the practitioner | A | 1 | Face shown in video thumbnail. No title or qualification in first screen. |
| 9 | "Dein erster Termin": 3-4 steps, duration, price frame | A | 0 | No such section in home-raw.html (no "Termin", no "Ablauf", no "Preis"). |
| 10 | One accent colour for CTA; blur test | A | 1 | Button (#315875) and banner box (#00558b) are both blue. CTA contrast is low against the banner. |
| 11 | CTA repeats every 2 sections | A | 1 | The word "sichern" (CTA verb) appears 3 times in home-raw.html, not spread over every second section. |
| 12 | Reviews open, name + Google logo + heading | B | 0 | No review block. Text dump has no "Bewertung" and no review. |
| 13 | Proof heading carries a benefit | B | 0 | No proof heading on the page. |
| 14 | 3-4 proof blocks spread over the page | B | 0 | No testimonial, quote or review block in home-raw.html. |
| 15 | Situations section (3-5 situations, way out, HWG-clean) | B | 1 | Situations present: "Sie sind zielorientiert ...", "Sie wissen, dass nicht das Tempo ...", "Sie haben gelernt ...". Way out: "Kostenloses Kennenlern-Coaching sichern!". Not HWG-clean: "sodass Stress und Burnout keine Chance mehr haben" (promise, see item 22). |
| 16 | Services as cards with benefit heading and link | B | 1 | Services shown as text lists ("Vorträge", "Online Coaching"). No benefit cards. |
| 17 | FAQ with real objections | B | 0 | No FAQ in home-raw.html. |
| 18 | Location block: map, address, parking, transport, hours | B | 0 | No address, map or opening hours in home-raw.html. |
| 19 | Closing section = mini hero | B | 0 | Page ends with info and privacy text. No closing CTA section. |
| 20 | Every section heading states a point | C | 1 | Mixed: "Wie kann ich Sie unterstützen?" (question). "Dieser Läufer war ich, Markus Frey." (statement). |
| 21 | Type hierarchy, body at least 16 px | C | 1 | Not measured with computed styles. Screenshot: body text about 18 px, banner slogan is an image. Judgement only. |
| 22 | HWG (health clients only) | A | n/a | Branch class is "service", so item 22 is out of scope per the scorecard rule. Flag: "sodass Stress und Burnout keine Chance mehr haben" reads as a prevention promise. |

## Total

- Items 1-21 (scored): 13 of 42.
- Item 22: not applied (branch "service").
- Prio A items at 2: 1 of 11 (item 5 only). Prio A is not met. Gate (34 of 42) not met.
- Items 6, 7, 9 are 0 and carry the most risk on the first screen (no reassurance, no proof, no first-appointment section).
