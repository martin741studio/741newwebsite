# Dataset — Landing page "The Replayers" me&you (2026-10-12)

Shared facts: `../../02-data/dataset.md` (homepage), `../../michael/02-data/dataset.md`, `../../seminare/02-data/dataset.md`, `../../rhetorik/02-data/dataset.md`, reviews `../../02-data/reviews.md`, stimmen `../../stimmen/02-data/dataset.md`. Content pool: `../../../content-pool/04-pool/pool.json` (items with `page_tag` = `lp:replayers`), findings `content-pool/04-pool/findings-replayers.md`.

Rule: when two sources conflict, the newer and safer statement goes on the page. The conflict goes to section 6 and to the handoff.

## 0. Task and decisions already made
- Main session (Martin, 2026-10-12): CRO run for lp-replayers, workflow section 4b. Stop at Checkpoint 1 (copy).
- Decisions given to this run (Martin can change them at Checkpoint 1):
  - D1 Hero H1 (client approved, copy deck R3 page 06): „Dir fehlen nicht die Worte. Sie kommen nur zu spät.“
  - D2 Primary CTA „Gespräch buchen“ → `/gespraech-buchen?utm_source=lp-replayers&utm_content=<section>`.
  - D3 Soft first step: free video training → `https://www.meandyou.de/sichtbarkeit-neu?utm_source=lp-replayers&utm_content=<section>`. Only one CTA visible per screen.
  - D4 Community „Talk to Me“ stays out. Book and podcast may appear as quiet first steps (cleared facts only).
  - D5 Lampenfieber only as FAQ, answered with practice and feedback. No health claims, no remedies.

## 1. Sources of this run (all read 2026-10-12)
| ID | Source | What it gives |
|---|---|---|
| L1 | Preview v2 `prototype-v2/lp-replayers.html` (local, served on port 8832) | current page, 480 words with the marquee repeated 3 times (about 260 unique words) |
| L2 | Copy deck R3 page 06 (`../../02-data/copydeck-r3.txt`) | H1 „Dir fehlen nicht die Worte. \| Sie kommen nur zu spät.“, button „Gespräch buchen“ on all three LPs, warm palette, indoor photography |
| L3 | Design guidelines section 02 (`quellen/meandyou-design-richtlinien.html`) | persona rules (see section 4) |
| L4 | Homepage approved copy, situation card 1 | „Im Meeting bleibst du still. Auf dem Heimweg hast du den perfekten Satz. Das Problem ist nicht dein Wissen, sondern der Moment.“ |
| L5 | Book page, Dussmann kulturkaufhaus.de ISBN 978-3-579-02394-6 (Firecrawl) | „Nie wieder sprachlos! Mit den richtigen Worten besser durchs Leben“, Gütersloher Verlagshaus, 26.08.2019, 256 pages, paperback. Text: „In 50 kurzen Kapiteln beschreibt er alltägliche Situationen, in denen uns oft die Worte fehlen und gibt praktische Tipps, wie wir die richtigen finden können.“ Questions in the text: „Wie entschuldige ich mich angemessen? Wie verteidige ich mich, wenn ich zu Unrecht angegriffen werde? Wie macht man ein Kompliment?“ Note on the page: „Eine Nachauflage des Werkes von Michael Ehlers wird unter einem veränderten Titel erscheinen.“ |
| L6 | Apple Podcasts, show page „Unübersehbar“ (Firecrawl, maxAge 0) | Michael: „Autor von neun Büchern und Lehrbeauftragter an der Universität St. Gallen. Seit 2008 spreche ich hier im Podcast …“, „Rhetorik und Auftritt, Schlagfertigkeit und Wirkung …“, „Alle zwei Wochen eine neue Folge“ |
| L7 | Podcast episode 193 „Warum du nach dem Seminar nichts kannst“, 07.09.2026, 12 min (Apple, maxAge 0) | „Du erfährst, warum sich Wissen wie Fortschritt anfühlt, obwohl es keiner ist“; real training is „individuell, mit sofortigem Feedback, an der Grenze des eigenen Könnens, mit Wiederholung“; Michael works with „so wenig Theorie wie möglich, individuelles Feedback statt Stoffplan“, „weil Technik ohne geklärte Person ein Kostüm bleibt“; „vier Übungen für die nächste Woche, darunter die härteste von allen: dreißig Sekunden Selbstaufnahme“ |
| L8 | Podcast episode „Der Satz, der zehn Sekunden dauert“, 23.09.2026, 9 min (Apple) | „Eine Unternehmerin mit fünf Standorten sitzt zwei Tage in Michael Ehlers' Seminar und schafft es nicht, eine einzige Bitte auszusprechen.“ „… was das innere Gericht mit Deiner Sprache macht …“ |
| L9 | Podcast episode „Alles ganz furchtbar.“, 24.08.2026, 7 min (Apple) | chapter from „Nie wieder sprachlos“: three strategies against constant complaining: „Distanzieren, Verantwortung übertragen und meinen Favoriten, den umgedrehten Spieß“ |
| L10 | Podcast episode „Folge 30 – Schlagfertigkeit VS Wortmächtigkeit“ (podigee, older) | „Wer schlagfertig ist, gilt als kommunikativ stark. Aber stimmt das auch? Wie kann ich mit fiesen Angriffen umgehen?“ |
| L11 | de.wikipedia.org/wiki/Treppenwitz (Firecrawl, maxAge 0) | „ein geistreicher Gedanke, der jemandem einen Moment zu spät („beim Hinausgehen auf der Treppe“) einfällt“; from French „l’esprit de l’escalier“ (Denis Diderot, 18th century); in German since the first half of the 19th century |
| L12 | meandyou.de/sichtbarkeit-neu (rhetorik run R4) | video by Michael, „Nicht mehr überhört – sondern unübersehbar.“, „So gewinnst du Aufmerksamkeit und Vertrauen – ohne laut zu werden oder dich zu verbiegen.“; Wistia length 29:39 min (rhetorik OPEN-FLAGS R7) |
| L13 | Reviews (`../../02-data/reviews.md`, `../../stimmen/02-data/dataset.md`) | persona language, see section 3 |
| L14 | Approved copy homepage, seminare, faq, rhetorik | cleared lines, see section 5 |

## 2. Current page (L1)
Sections: header with button, hero (overline „Der Nachdenker“, H1, sub line, quote box „Das Schlimmste daran ist, dass dir die perfekte Antwort erst Stunden später einfällt …“, button), „Warum Michael“ (numbers 30+ / 8.000+ / Top 100 Trainer / 9 Bücher, ERFOLG text, button), method (3 steps), quotes as marquee (Sarna Röser, Peter Escher, Emrullah Ates, Neven Subotic), 3 video tiles, closer „Der nächste Schritt ist ein Gespräch.“, footer.
Technical: title „Landingpage Replayers · me&you Prototyp v2“, 1 H1, no meta description, no JSON-LD, no robots tag. All 5 buttons go to `https://www.meandyou.de/seminare-termin` (old page). Header button and hero button are visible at the same time.
First viewport 1440 × 900: H1, sub line and button visible (`v2-lp-replayers-first-viewport-1440.png`). No proof line in the first screen. Page height 8.421 px (`v2-lp-replayers-full-1440.png`).
Note: the v2 facts „9 Bücher“ and „Top 100 Trainer“ are already fixed today. The content pool findings F5 still name the older values.

## 3. Proof for this persona
| Fact | Wording | Source |
|---|---|---|
| ProvenExpert | 250 published reviews, 227 with 5 stars. No overall score shown in the scrape | reviews.md B (claim C01) |
| Participants | über 8.000 | live site (C03) |
| Christian S., ProvenExpert, 29.08.2023, Rhetorik 1 Mallorca | „Kennen Sie die Situation, unsicher oder sprachlos zu sein? Wollen Sie flüssig vor Menschen oder einer Kamera sprechen ohne „äh“s? Dann sind Sie bei Michael am besten aufgehoben.“ | stimmen dataset P1 (full text) |
| Julian L., ProvenExpert, 03.04.2023, Rhetorik 1 Mallorca | „Michael schafft es, das Maximum aus einem rauszuholen und die Redeangst zu nehmen.“ „Die Trainings vor der Kamera mit den darauf folgenden Auswertungen helfen die Selbst- und Fremdwahrnehmung zu schärfen.“ | reviews.md P5 |
| Jasmina L., ProvenExpert, 28.08.2023 | „Die Herangehensweise und das individuelle Feedback haben mich sehr motiviert und mir unheimlich viel Selbstvertrauen geschenkt“ | reviews.md P2 |
| Jenny Eikel, Google | „zwischen der ersten und der letzten Rede lagen wirklich Welten“; „Michaels Feedback war unheimlich wertschätzend, klar und unglaublich hilfreich“ | reviews.md G7 |
| Christin R., ProvenExpert, 17.04.2023 | „… dass wir Teilnehmer ein Mix von Anfänger bis Profi waren und Michael uns alle, egal auf welchem Level, weiterbringen konnte.“ | reviews.md P4 |
| Video testimonials | 3 videos (1:00, 1:12, 1:23), people without names | C19, stimmen run |
Never: Google star number, the review of Tajan Fattah (G13), the 1-star review.

## 4. Persona rules (L3, design guidelines section 02)
Core line: „Es sollte sich sicher anfühlen zuzugeben, dass man den Faden verliert.“ Tone: „Warm, geduldig, nachsichtig. Spricht die Person nach dem Meeting an, nicht während dessen. Nie klinisch, nie wie eine Bühne.“ Use: „Kostenloser Trainings-Funnel, das Buch, die 39-Euro-Community, Erstkontakt-Anzeigen und organische Inhalte.“ Visual goal: „Wiedererkennung vor Anleitung.“ Layout: generous space, one idea per screen, soft edges, no visible grid lines or hard dividers, body text with less contrast than the headline, never more than one CTA visible at the same time. Hero label „Der Nachdenker“. Photography: close crop, interior, natural light, person in motion, rarely looks into the camera, slight grain.
Note: the guideline names a price for the community. Prices never go on the page (D4 keeps the community out).

## 5. Offer facts (cleared on approved pages)
| Fact | Wording / value | Source |
|---|---|---|
| Call | 30 Minuten, kostenlos, per Video; a member of Michael's team; no obligation; confirmation by e-mail, reminder by WhatsApp | C08, C16, F03, faq approved |
| Seminar Schlagfertigkeit | „Ruhig bleiben, wenn es eng wird“, working title Rhetorik II [von Kunde bestätigen: Seminarname]: Schlagfertigkeit, Überzeugungspsychologie, unfaire Methoden durchschauen, Angriffe ruhig kontern, Meetings; anchor `/seminare#ruhig-bleiben`; place 2027 Barcelona | homepage approved, S21, S24 |
| Seminar entry | „Frei sprechen, auch mit Lampenfieber“, working title Rhetorik I; anchor `/seminare#frei-sprechen`; places Mallorca, Frankfurt, Berlin | homepage approved, S20, S24 |
| Seminar format | 3 + 1 Tage, 3 Videoanalysen mit Sofort-Feedback, VR-Training, 10 bis 14 Plätze | C07 |
| Seminar places | Mallorca, Barcelona, Zypern, Dubai, Frankfurt, Berlin | C13 |
| Michael | seit 1990; über 30 Jahre; neun Bücher als Autor oder Herausgeber; Lehrbeauftragter Universität St. Gallen; Rhetorik-Analyst für ARTE und WELT TV; laut ERFOLG Magazin Top 100 Trainer; Podcast „Unübersehbar“ seit 2008 | M01–M05, C05 |
| Method | „Wirkung beginnt nicht bei der Technik. Die meisten Rhetoriktrainings starten bei Werkzeugen. Wir starten davor: bei Persönlichkeit, Selbstbild, Mustern und innerer Stabilität. Erst wenn das steht, tragen die Werkzeuge.“ „Persönlichkeit. Kongruenz. Wirkung.“ with lines „Wer du bist, bevor du sprichst.“ „Wenn Haltung und Worte dasselbe sagen.“ „Was davon im Raum ankommt.“ | R04, rhetorik R3 |
| Introverts | „Rhetorik heißt nicht, lauter oder extrovertierter zu werden. Viele Introvertierte überzeugen durch Präzision und Ruhe.“ | R08, faq approved |
| Practice | „Rhetorik ist ein Handwerk, und jedes Handwerk braucht Übung.“; exercise „Sprich zwei Minuten frei … Nimm dich dabei mit dem Handy auf …“ | faq approved |
| Free video | video by Michael on /sichtbarkeit-neu, length 29:39 min by Wistia; the page names it a video, the copy deck names it „Training“ | L12, rhetorik K4 |

## 6. Search demand (content pool, DataForSEO de, 2026-10-12)
| Keyword | Volume/month | Use |
|---|---|---|
| schlagfertigkeit | 2.400 | title, H2 |
| lampenfieber | 1.900 | FAQ only (D5) |
| treppenwitz | 1.600 | recognition block |
| schlagfertigkeit lernen | 480 | primary keyword: title, H1 kicker, first paragraph |
| rhetorik buch | 390 | book block |
| was ist ein treppenwitz / treppenwitz bedeutung | 320 / 260 | answer in the Treppenwitz block |
| rhetorik übungen | 210 | exercises |
| redeangst überwinden / redeangst | 170 / 110 | FAQ |
| schlagfertigkeit buch | 170 | book block |
| frei sprechen / frei sprechen lernen | 140 / 110 | situation „frei sprechen“ |
| schlagfertigkeit trainieren / schlagfertig werden | 110 / 110 | H2, FAQ |
| den faden verlieren | 110 | situation |
| lampenfieber überwinden | 90 | FAQ |
| schlagfertigkeit seminar | 40 | seminar line |
| kann man schlagfertigkeit lernen | 40 | FAQ |
People Also Ask (`serp-11`, `serp-13`): „Kann man Schlagfertigkeit lernen?“, „Wie lerne ich Schlagfertiger zu werden?“, „Was steckt hinter Schlagfertigkeit?“, „Welche Übungen kann ich machen, um meine Schlagfertigkeit zu trainieren?“, „Woher kommt Lampenfieber?“, „Wie bekomme ich die Nervosität weg?“, „Was kann man gegen Lampenfieber machen?“, „Wie kann ich Bühnenangst überwinden?“. `serp-12`: „Was bedeutet Treppenwitz?“.
Benchmark (gate A0): 8 competitor pages, median 1.546,5 words, floor 1.083 words (`content-pool/02-competitors/metrics-replayers.json`, copied to `content-writing/lp-replayers/_work/bench-metrics.json`). Rankings: meandyou.de ranks for no Schlagfertigkeit term (homepage run, section 6).

## 7. Conflicts and compliance
| # | Finding | Handling |
|---|---|---|
| K1 | v2 shows public figures (Neven Subotic, Sarna Röser). Their quotes do not name the persona problem | proof from persona voices (section 3). Peter Escher stays out here (Overlooked tone) |
| K2 | v2: all buttons go to `/seminare-termin` (old page) | `/gespraech-buchen` with UTM (D2) |
| K3 | v2: header button and hero button visible together; the persona rule says one CTA | header button hides while the hero button is in view (prototype rule, Step 6) |
| K4 | Book title: the publisher page says a new edition will come with a changed title (L5) | name „Nie wieder sprachlos!“ with year 2019, no price, no shop link. [von Kunde bestätigen: aktueller Titel und Bezugsquelle] |
| K5 | Podcast exercise „dreißig Sekunden Selbstaufnahme“ is named, but the other three exercises are only in the audio | use only the named exercise and the cleared FAQ exercise. [von Kunde bestätigen: Übungen im Wortlaut] |
| K6 | „Warum die Worte zu spät kommen“: Michael's own sentence does not exist in text form. Episode L8 gives a story and the term „inneres Gericht“ | tell the story from L8 as it is written. No own theory in Michael's name. [von Kunde bestätigen: Michaels Satz dazu] |
| K7 | Lampenfieber: autocomplete has medication and remedy terms | FAQ answers with practice and feedback only. No remedy, no health claim, no „angstfrei“ promise (D5) |
| K8 | Community „Talk to Me“: guideline says Replayers product, the FAQ run cut it | out (D4) |
| K9 | Free video: page says „Video“, copy deck „Training“, length 29:39 min not confirmed, sign-in unknown | „kostenloses Video-Training“, length „rund 30 Minuten“ as yellow mark (rhetorik R7) |
| K10 | Quote names (Christian S., Julian L., Jasmina L., Jenny Eikel) | public on ProvenExpert and Google. [von Kunde bestätigen: Einwilligung Namen] as on the sibling pages |
| K11 | Does Michael lead every seminar himself? | open on all pages. The LP says „Michael und sein Team“ only where the call is meant |
| K12 | Persona guideline names the community price | no price on any page |

## 8. Open client facts [FEHLT]
1. Content, length and sign-in of the free video training (K9).
2. Two or three exercises from Michael word for word, with release (K5).
3. Michael's own sentence on why the words come late (K6).
4. Current title, edition and where to get „Nie wieder sprachlos!“ (K4). Cover file and permission.
5. Consent for the quote names (K10).
6. Seminar names (Rhetorik I and II are working titles).
7. Name and role of the person in the call.
8. Does Michael lead every seminar himself (K11).
