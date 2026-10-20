# Review 1: Startseite me&you (draft-v3.md)

Date: 2026-10-11. Reviewer: independent subagent. Mode: review only. No draft edits.

Inputs checked:
- `03-draft/draft-v3.md`
- `01-brief/brief.json` and `01-brief/claims.json`
- `cro/02-data/dataset.md`, `cro/02-data/reviews.md`, `cro/02-data/copydeck-r3.txt`
- `_work/bestand-dedup.txt` (live page text), `prototype-v2/build_v2.py` (FAQ sources)
- `~/Downloads/2026 Michael Ehlers Kursinhalte R1-R3 4 Tage.pdf` (seminar topics)
- `05-final/schema.jsonld`, `05-final/placeholders.md`, `nap.json`, `voice.md`
- `_work/bench-metrics.json`, `cro/02-data/demand/sv-out.json`, `serp1-out.json`
- Scorecard `~/.claude/skills/content-writing/assets/content-writing-scorecard.md`
- SEO rubric `.claude/skills/seo-page-optimizer/references/scoring-rubric.md`

Approved lines are not touched. The fixes below never reword them.

## Verdict

- Real gaps: **26** (6 high, 9 medium, 11 low).
- SEO audit: **partially aligned**, average 77/100. Five dimensions are under 85.
- Scorecard: **73.5/100** and one BLOCK error (Fakten). Decision: **nachbessern**.
- The gate report says "G1 PASS". G1 checks numbers only. It does not catch unbacked text claims. Several FAQ facts have no source in `claims.json` or `dataset.md`.

---

## 1. Correctness review: real gaps

Severity: H = must fix before client, M = should fix, L = small fix.

### Review quotes (checked word by word against `reviews.md` and the live page)

Quotes that match the source exactly: Jenny Eikel (S08), Adrian Bourcevet (S08, cut marked with […]), Michael B., Christin R., Julian L., Peter Escher. Three quotes have errors.

**R01 · S08 · H · misleading statement**
- Quote: „Sechs Stimmen, ungekürzt bis auf die markierten Stellen.“
- Why wrong: All six quotes are excerpts from longer reviews. Only the Adrian quote has a […] mark. Jenny, Michael B., Christin R. and Julian L. are single sentences taken out of long reviews. The sentence is false.
- Fix: „Sechs Auszüge aus öffentlichen Bewertungen. Auslassungen innerhalb eines Zitats sind mit […] markiert.“

**R02 · S02 · H · quote differs from source**
- Quote: „Zwischen der ersten und der letzten Rede lagen wirklich Welten.“
- Source (G7): „… jeder hat sich um 180 Grad gedreht - zwischen der ersten und der letzten Rede lagen wirklich Welten.“
- Why wrong: The quote starts in the middle of a sentence. The cut has no […] mark. The draft also changes „zwischen“ to „Zwischen“.
- Fix: „[…] zwischen der ersten und der letzten Rede lagen wirklich Welten.“ Jenny Eikel, Teilnehmerin, Google

**R03 · S04 · L · quote differs from source**
- Quote: „… die von sich denken, sie wären keine großen Redner.“
- Source (live page): „… sie wären “keine großen Redner”.“
- Why wrong: The draft removes the inner quotation marks. Joining the three live lines into one quote is fine.
- Fix: „Zu mir kommen regelmäßig Menschen, die von sich denken, sie wären ‚keine großen Redner‘. Nach 3 Dekaden …“

### Facts and claims not backed by `claims.json` or `dataset.md`

**R04 · S10 · H · unbacked claim**
- Quote: „Aktuelle Erkenntnisse treffen auf über 30 Jahre Praxis aus Politik, Medien und Wirtschaft. Viele erfahrene Teilnehmer sagen, dass sie noch einmal ein neues Niveau erreicht haben.“
- Why wrong: The source is the old live FAQ (`build_v2.py`, line 413). That FAQ said „25 Jahre“ and put the sentence in quotation marks with no name. No review in `reviews.md` says „neues Niveau“. „Viele“ is a number claim with no data. „Praxis aus Politik“ is not in the dataset either.
- Fix: „Ja. Auch Menschen mit viel Erfahrung lernen hier noch dazu. Peter Escher, Moderator beim MDR, schreibt: „Trotz 40 Jahren Medienerfahrung konnte ich erstaunlich viel vom Rhetoriktraining profitieren.““ Alternative with G9 (verbatim): „Ich habe in diesem Kurs mehr gelernt als in all meinen bisherigen Schulungen zusammen.“ Emrullah Ates, Google.

**R05 · S10 · H · unbacked claim and internal conflict**
- Quote: „Snacks und Getränke während des Programms und ein leichtes Frühstück im Rahmen des Seminars. Das Abendessen und das Hotelfrühstück zahlst du selbst.“ Also: „Kann ich eine Begleitperson mitbringen? Ja. Die Kosten dafür trägst du selbst. Ein Upgrade …“
- Why wrong: Verpflegung and Begleitperson are not in `claims.json` (C12 covers only Übernachtung, Anreise, Absage). They are not in `dataset.md`. The source is the Sales-Checkliste draft. `dataset.md` §10.8 says the client has not approved it. Also, „leichtes Frühstück enthalten“ next to „Hotelfrühstück zahlst du selbst“ confuses the reader.
- Fix: Add both facts to `claims.json` after client approval. Until then, mark both answers as yellow placeholders in `placeholders.md`. Clearer text: „Während des Programms gibt es Snacks, Getränke und ein leichtes Frühstück. Das Frühstücksbuffet im Hotel und das Abendessen zahlst du selbst.“

**R06 · S10 · H · unverified legal source**
- Quote: „Die Seminarkosten werden laut AGB nicht erstattet. Du bekommst stattdessen einen Gutschein für ein späteres Seminar.“
- Why wrong: The source is the Sales-Checkliste draft (C12), not the AGB. Nobody has read the AGB. „laut AGB“ names a legal document that may say something different. Gutschein terms (value, time limit) are also unknown.
- Fix: Read https://www.meandyou.de/agb and quote the rule with the exact clause. Until then use a placeholder: „[von Kunde bestätigen: Regel bei Absage laut AGB, Gutschein-Bedingungen]“. Add it to `placeholders.md`.

**R07 · S10 · M · unbacked claim**
- Quote: „Der Preis hängt von Format und Ort ab.“
- Why wrong: No source says the price changes with the location. The live page shows one price only (Mexico).
- Fix: „Den Preis für dein Seminar nennt dir Michaels Team im kostenlosen Gespräch.“ Keep the sentence about what is included.

**R08 · S08 · M · unbacked claim and AI filler**
- Quote: „Drei Teilnehmer erzählen im Video, jeweils in gut einer Minute, wie sie das Seminar erlebt haben. Keine Schauspieler, keine Skripte.“
- Why wrong: `dataset.md` says only „3 echte Video-Stimmen“. „Keine Skripte“ has no source. The video lengths are 1:00, 1:12 and 1:23. „gut einer Minute“ is wrong for the first one. The „Kein X, kein Y“ line is also a typical AI pattern.
- Fix: „Drei Teilnehmer erzählen im Video, wie sie das Seminar erlebt haben. Jedes Video dauert etwa eine Minute.“

**R09 · S08 · L · card heading changes the quote's meaning**
- Quote: „Auch nach 40 Jahren vor dem Mikrofon“
- Why wrong: The quote says „40 Jahren Medienerfahrung“. Peter Escher is a TV presenter. „vor dem Mikrofon“ is not in the source.
- Fix: „Auch nach 40 Jahren Medienerfahrung“

**R10 · S09 · L · fact not in claim list**
- Quote: „Mallorca (Rhetorik I) … Dubai (Rhetorik III) … Barcelona (Rhetorik II) … Frankfurt (Rhetorik I) … Berlin (Rhetorik I) … Zypern (Rhetorik III)“
- Why wrong: The link from location to seminar is correct on the live page („Mallorca & Deutschland Rhetorik 1“, „Barcelona Rhetorik 2“, „Dubai Rhetorik 3“, „Zypern Rhetorik 3“). But C10 and `dataset.md` §2.2 list dates only.
- Fix: Add the link from location to seminar to C10 (source: meandyou.de Terminliste, 2026-10-11).

**R11 · S07 and S11 · L · process facts not in claim list**
- Quote: „Danach bekommst du eine Bestätigung per E-Mail …“; „Kostenlos und ohne Verpflichtung.“; „ohne Verpflichtung“
- Why wrong: The e-mail confirmation and „ohne Verpflichtung“ are not in C08 or `dataset.md` §2.3. The WhatsApp reminder is backed.
- Fix: Check the Calendly event „Sichtbarkeit Neu“ (e-mail confirmation setting). Then add both facts to C08.

### Sentences that can mislead the reader

**R12 · S08 · M · general result claim**
- Quote: „## Zwischen der ersten und der letzten Rede liegen Welten.“
- Why wrong: One reviewer described her own group in the past tense. The H2 turns this into a present-tense promise for every participant. A result claim needs a claim-list entry. This one has none.
- Fix: Use the Copy Deck H2 „Vorher. Nachher.“ or a neutral H2: „Was Teilnehmer über das Seminar schreiben“. Keep Jenny's sentence as a marked quote with her name.

**R13 · S04 · M · old award shown as current**
- Quote: „Das ERFOLG Magazin zählt Michael Ehlers zu den Top 100 Trainern im deutschsprachigen Raum und zu den Top 10 Speakern.“
- Why wrong: The source is cover issue 3/2017. „zählt“ (present tense) says that the ranking is current. `dataset.md` K5 says: no claim that it is current.
- Fix: „Das ERFOLG Magazin hat Michael Ehlers zu den Top 100 Trainern im deutschsprachigen Raum gezählt und als Top-10-Speaker genannt.“ The S02 and S04 bullets with „laut ERFOLG Magazin“ can stay.

**R14 · S10 · M · mixes three seminars into one**
- Quote: „Freie Reden vor der Gruppe, Stegreifreden, Übungen zu Schlagfertigkeit und Körpersprache.“
- Why wrong: The PDF puts Schlagfertigkeit in Rhetorik II and Stegreifrede in Rhetorik III. A Rhetorik I participant will not get these topics. The answer says every seminar has all of them.
- Fix: „Du sprichst selbst, und zwar viel. Dreimal wirst du auf Video aufgenommen und bekommst sofort Feedback. Im VR-Training sprichst du vor einem virtuellen Publikum. Die Themen hängen vom Seminar ab: in Rhetorik I zum Beispiel freie Rede und Struktur, in Rhetorik II Schlagfertigkeit, in Rhetorik III die Stegreifrede.“

**R15 · S10 · M · contradicts S04**
- Quote: „Wissen aus Büchern hilft wenig, wenn du unter Druck sprichst.“
- Why wrong: S04 says „Seine Arbeit steht in Büchern“. The FAQ makes Michael's own books look useless.
- Fix: „Bücher geben dir das Wissen. Unter Druck hilft dir aber nur, was du geübt hast.“

**R16 · S06 and S09 · M · working titles shown as final, numbering contradicts the text**
- Quote: „Kein Stufenmodell. Ein klarer Einstieg, danach eigenständige Formate, die du frei wählst.“ followed by „Rhetorik I / Rhetorik II / Rhetorik III“
- Why wrong: `dataset.md` §10.1 says the seminar names are open („[FEHLT: Seminarnamen]“, working titles). The draft uses them without a placeholder. Roman numerals tell the reader that there are levels, which contradicts „Kein Stufenmodell“. The Copy Deck says: „No numbers … Nothing that implies order.“
- Fix: Mark the names as placeholders in `placeholders.md`: „[von Kunde bestätigen: Seminarnamen]“. Tell the client about the conflict between numbers and „Kein Stufenmodell“.

**R17 · S09 · L · unclear claim**
- Quote: „Rhetorik I findet auch in Frankfurt und Berlin statt, ohne Flug.“
- Why wrong: „ohne Flug“ is true only for some readers. A reader in Munich may fly to Berlin.
- Fix: „Rhetorik I gibt es auch in Deutschland: in Frankfurt und in Berlin.“

### Broken promises against the brief or the scorecard

**R18 · placeholders.md and flags · H · BLOCK item (scorecard „Offene Kundenfakten“)**
- Quote: frontmatter „flags: see OPEN-FLAGS.md“; `placeholders.md` has 1 row.
- Why wrong: `OPEN-FLAGS.md` does not exist anywhere in the project. These open client facts are on the page without a placeholder:
  1. „30 Jahre“ (`dataset.md` §10.3, live page also says 25)
  2. ProvenExpert „4,9“ (calculated 4,90; the score ProvenExpert itself shows is `[FEHLT]`)
  3. Sales-Checkliste answers: Übernachtung, Verpflegung, Begleitperson, Absage (§10.8)
  4. Seminar names (§10.1)
  5. Phone number: the page uses +49 15888367664, the GBP uses +49 160 96600322 (`nap.json`: open)
- Fix: Create `OPEN-FLAGS.md` with the three flags from the HTML comment (Situation 3 du, ProvenExpert 4,9, dates shown). Add items 1 to 5 to `placeholders.md`.

**R19 · TECH and schema.jsonld · M · draft spec not delivered**
- Quote: „Schema: WebPage, BreadcrumbList, EducationalOrganization (Institut Michael Ehlers GmbH, Hallstadt), Person (Michael Ehlers).“
- Why wrong: `schema.jsonld` has no Person node. The organization has no address, no telephone, no logo, no sameAs. It has an empty `"department": []`. The schema does not match the text.
- Fix: See SEO dimension 7.

**R20 · S08 · L · name format differs from the design note and the Copy Deck**
- Quote: „Jenny Eikel, Google“, „Adrian Bourcevet, Google“ next to „Michael B.“, „Christin R.“, „Julian L.“
- Why wrong: The design note in the draft says „Vorname“. The Copy Deck format is „[Vorname], [Rolle]“. Full names for Google reviewers and initials for ProvenExpert are not consistent. Full names on a sales page also need consent.
- Fix: „Jenny E., Google“ and „Adrian B., Google“. Use full names only with written consent.

### German language errors

**R21 · S03 · M · wrong word**
- Quote: „als überzeugend und vertrauensvoll wahrgenommen werden willst“
- Why wrong: „vertrauensvoll“ means „full of trust“ (trusting). The meaning here is „worthy of trust“. The error comes from the live page.
- Fix: „als überzeugend und vertrauenswürdig wahrgenommen werden willst“

**R22 · S05 · L · two possible meanings**
- Quote: „Hier lernst du nicht zu schauspielern.“
- Why wrong: Without a comma, the sentence can mean „you do not learn acting here“ or „you learn not to act“. The reader must guess.
- Fix: „Hier musst du nicht schauspielern.“

### Marketing filler and AI text

**R23 · S02 · L · heading talks about the text, not the topic**
- Quote: „## Das Rhetorik-Seminar von Michael Ehlers in vier Sätzen“
- Why wrong: This is a typical AI pattern. It also gives no search or GEO value. Gate G6 counts 5 sentences in this block, so the promise of four is not safe.
- Fix: „## Wie läuft das Rhetorik-Seminar von Michael Ehlers ab?“ A question H2 matches the PAA „Was macht man in einem Rhetorik-Seminar?“.

**R24 · S05 · L · negation pattern**
- Quote: „Das Ziel ist kein einzelner Auftritt.“
- Why wrong: The page already has eight „kein/nicht X, Y“ lines. Most of them are approved or client lines. This one is new. Too many lines of this type is an AI tell.
- Fix: „Das Ziel: Rhetorik wird ein fester Teil deines Auftretens.“ Delete the next sentence.

**R25 · S10 · L · unbacked detail and off-scope FAQ**
- Quote: „Der Online-Kurs ist ein Selbstlernkurs mit kurzen Lektionen und Fragerunden in einer Community.“
- Why wrong: `dataset.md` §2.4 says „Video-Lektionen, Zugang mindestens 12 Monate“. The Community „Talk to Me“ is a different product. „Fragerunden“ has no source. K10 says that the new FAQ covers the seminar and the call only.
- Fix: „Der Online-Kurs ist ein Selbstlernkurs mit Video-Lektionen.“ Do not use the course name, because it contains the forbidden word „Intelligente“.

**R26 · S03 · L · paraphrase of approved wording**
- Quote: „für Menschen, die ein Unternehmen gegründet haben“
- Why wrong: The Copy Deck has approved wording: „Führungskräfte · Gründerinnen und Gründer · Beraterinnen und Berater“. The paraphrase is longer. It also mixes three gender forms in one sentence.
- Fix: „Gedacht ist es für Führungskräfte, Gründerinnen und Gründer, Beraterinnen und Berater.“

### Flags for the client (approved text, not counted as gaps)

- S06 „Kein Konferenzraum, kein Hotelsaal.“ (approved). FAQ answers and review G1 say that seminars take place in hotels. For Frankfurt and Berlin we do not know the venue. Ask the client if the line is true for all six locations.
- S03 Situation 3 „Dein Unternehmen …“: already flagged for the client.
- „Get Together“: Duden spells „Get-together“. The client PDF and C07 use „Get Together“. Keep it as the client's term, or ask once.

### Checked and correct

- Address form: only du. „Sie kommen nur zu spät“ is the plural pronoun, not a polite form.
- No prices anywhere. No forbidden words. No dashes used as punctuation.
- All approved lines are verbatim: H1 slogan, subline, situation 1 and 2 headlines and bodies, situation 3 body, S04 H2, S05 H2 and body, method steps, S06 H2 and body, S11 H2 and the first two body sentences.
- All 10 seminar dates match C10.
- Seminar topics in S06 match the PDF (Lampenfieber, Redestil, unfaire Methoden, Kritik motivierend, DeepOcean).
- Numbers 250, 4,8, 8.000, 30, 1.000, 14, 10 to 14, 3 + 1, 30 Minuten: all in the claim list.

---

## 2. SEO audit (AUDIT mode, 8 dimensions)

Target keyword: „Rhetorik-Seminar“ (880/month, DE). SERP: academy and seminar pages (Haufe, Kitzmann, IHK, KBW), 3-pack local results, PAA box. Benchmark median 1,747 words. Draft about 1,831 visible words.

| # | Dimension | Score | Evidence |
|---|---|---|---|
| 1 | Search-intent match | 88 | Commercial seminar page with dates, places and a booking CTA, like the top 5. The price is not shown (client rule), while 5 of 12 benchmarks show prices. |
| 2 | Topical depth | **78** | Covers the what, who, where, when, process and 14 FAQs. G6 term coverage is 75 %. Missing: Präsentation (1 use), Stimme, Präsenz, Inhouse/Firmen, Coaching. Related searches „Wochenende“ and „Bildungsurlaub“ have no answer. |
| 3 | GEO-extractability | **82** | It has a direct-answer block, a fact list, 14 FAQs and named entities (ERFOLG Magazin, ProvenExpert, DeepOcean, 6 places). No definition sentence. The answer block is about 67 words and its H2 is a meta heading (R23). The price FAQ gives no number. |
| 4 | E-E-A-T | 86 | Named trainer, 30+ years, 8.000 participants, 1.000+ talks, media logos, six sourced reviews. No book titles. The ERFOLG award is from 2017 but uses present tense (R13). No Person schema. |
| 5 | Local signals | **72** | Six places and ten dates are in the copy. NAP conflict: the page phone is +49 15888367664, the GBP phone is +49 160 96600322 (`nap.json` open). Hallstadt address is in no visible text or schema. The SERP has a 3-pack local result. |
| 6 | Technical on-page | 88 | Title 59 chars with keyword first. Meta 143 chars. One H1 with the keyword. Logical H2/H3. Small issues: the `#termine` anchor has no target id in S09. Only the S11 CTA has an href. The list in S07 is broken by a nested list. |
| 7 | Schema | **45** | `schema.jsonld`: WebPage, BreadcrumbList with one item, EducationalOrganization with no address, phone, logo or sameAs, and an empty `department`. No Person, although TECH promises it. No Event or Course for the 10 dates. Competitors Kitzmann, KBW and IHK use Course/CourseInstance/Event. |
| 8 | Internal links | **74** | 8 targets, more than the minimum of 6. Anchors „Mehr dazu“ (3 times) and „Mehr zu den Seminaren“ (3 times, same URL) do not name the topic. Risk: `/seminare` is the money page and the home page targets the same keyword „Rhetorik-Seminar“. |

Average: 77. Verdict: **partially aligned**.

### Fixes for the dimensions under 85 (biggest gain first)

1. **Schema (45 → about 90).**
   - Add a `Person` node for Michael Ehlers: jobTitle „Rhetoriktrainer“, `worksFor` #organization, `url` /michael, and `sameAs` when the profiles are checked.
   - Complete the organization: `address` Landsknechtstraße 50, 96103 Hallstadt, the telephone that Martin chooses, `logo`, `sameAs` with the ProvenExpert URL. Remove `"department": []`.
   - Add one `EducationEvent` per visible date: name, startDate, endDate, `location` with Place and city, `organizer` #organization, `eventAttendanceMode` Offline. Do not add `offers` with a price, because of the client rule.
   - Leave out FAQPage. That decision is in the brief (`schema_faq: false`). The rubric lists FAQPage, so this costs a few points. This is a known trade-off.
2. **Local signals (72 → about 88).**
   - Choose one phone number. Use it on the page, in the footer, in the schema and in the GBP.
   - Show the company address in the visible footer.
   - Give S09 the id `termine` so the hero link works.
   - Optional: if the client confirms enough unique content, consider a later Frankfurt page („rhetorik seminar frankfurt“ has 90/month). Do not create it as a thin copy of this page.
3. **Internal links (74 → about 90).**
   - Change the anchors to name the topic:
     - „Mehr zu: Wenn dir die Worte zu spät kommen“ → /lp-replayers
     - „Mehr zu: Recht haben und trotzdem überhört werden“ → /lp-overlooked
     - „Mehr zu: Wenn dein Unternehmen kleiner wirkt“ → /lp-undersold
   - Use one link to /seminare per card, with an anchor that names the seminar, for example „Rhetorik I im Detail“ → /seminare#rhetorik-1.
   - Prevent keyword overlap with /seminare. The home page keeps „Rhetorik-Seminar mit Michael Ehlers“ (brand plus keyword). /seminare targets „Rhetorik-Seminare: Termine und Inhalte“. Confirm this in the sitetree.
   - Check that /lp-replayers, /lp-overlooked and /lp-undersold exist on the live domain at launch. Today they exist only as prototypes.
4. **Topical depth (78 → about 86).**
   - Add „Präsentation“ and „Stimme“ to the Rhetorik I card where the PDF supports it (Rede halten, Struktur, Gestik).
   - Ask the client 3 yes/no questions: Inhouse for companies? 1:1 coaching (the PDF title says „1:1 Betreuung“; „rhetorik coaching“ has 390/month)? Bildungsurlaub? Each „yes“ becomes one FAQ answer of 2 sentences.
5. **GEO-extractability (82 → about 90).**
   - Use the question H2 from R23.
   - Shorten the answer block to about 50 words.
   - Add one definition sentence. Example: „Das Ehlers-Rhetorik-Framework hat drei Schritte: Persönlichkeit, Kongruenz, Wirkung.“ First confirm that the framework is the same as the three-step method. `dataset.md` §2.1 lists them in one row but does not say this directly.
   - Add a visible „Stand: Oktober 2026“ near the dates.

---

## 3. Content-writing scorecard (0/1/2 per item)

The rule is 2 = the scorecard check is fully met, 1 = partly met, 0 = not met. Points: 2 = full points, 1 = half, 0 = none.

| Block | Item | Score | Points | Reason |
|---|---|---|---|---|
| Textqualität | Hook follows the rule page | 2 | 5/5 | Situation and result first („Werde unübersehbar …“, „… trotzdem nicht gehört werden“). No pun, no „Wer wir sind“. |
| | Pain before solution, way out in the same section | 2 | 5/5 | S03: three situations, then „Der gemeinsame Punkt … Genau dort setzt das Seminar an“, then the CTA. |
| | One main CTA, reassurance line, repeated every 2 sections | 2 | 5/5 | „Gespräch buchen“ in 8 sections. Never more than 1 section without a CTA. Reassurance in S01, S03, S07, S11. |
| | Objections answered (price, confidentiality, process, duration) | 1 | 2.5/5 | Price (scope only), process and duration: yes. Confidentiality: no answer about the video recordings or the group. Needs a client fact, so add a placeholder. |
| | Scan format and elements | 2 | 5/5 | Short paragraphs, cards, lists, numbered steps. |
| SEO und GEO | One H1, title ≤ 60, meta ≤ 155, keyword in title and H1 | 2 | 4/4 | 59 / 143 chars, one H1, keyword in both. |
| | Direct-answer block, definition, entities | 1 | 2/4 | Block and entities: yes. No definition sentence. |
| | FAQ from real PAA, existing client FAQ kept | 2 | 4/4 | 3 PAA answered, 3 dropped with a reason. The live FAQ items for the seminar are kept. The online-course items are dropped per K10. |
| | G6: PAA, early answer, information gain, own headings, visible date, schema matches text | 1 | 2/4 | No visible date. The schema does not match the text (R19). |
| | Internal links in visible text, anchors name the topic, no keyword conflict | 1 | 2/4 | Generic anchors („Mehr dazu“). Overlap risk with /seminare. |
| | Word count: not under current page, ≥ 70 % of median, verdict sentence with source and date | 1 | 2/4 | 1,831 ≥ 1,787 current page and ≥ 1,223 (70 % of 1,747). The verdict sentence is missing: TECH says „siehe gates.md“, and gates.md has no verdict. |
| **Fakten (BLOCK)** | Every number and claim is in the claim list | **0** | 0/10 | R04, R05, R06, R07, R08, R10, R11 are not in `claims.json`. Media logos (S02) are in `dataset.md` but not in `claims.json`. |
| | Local fact real and sourced | 2 | 5/5 | Places and dates match C10 and C13. |
| | Open client facts are placeholders in placeholders.md | **0** | 0/5 | Only 1 of at least 6 open facts is listed (R18). |
| Recht (BLOCK) | G2 has no block hits, required notice present | 2 | 10/10 | Legal mode none. G2 PASS. |
| | Grey areas listed and decided by Martin | 0 | 0/5 | OPEN-FLAGS.md is missing. Not decided: the ERFOLG 2017 tense, the no-refund rule, full reviewer names, Situation 3. |
| Slop und Stil (BLOCK under 5/5) | G5 5/5 after cleanse, claim diff clean | 2 | 5/5 | G5 score 5, diff_claims PASS. |
| | G4: no dashes, one address form, no forbidden words | 2 | 5/5 | du 78, Sie 0. No forbidden words. |
| Lesegefühl | Fits the voice profile | 2 | 4/4 | Calm, adult tone. Own phrases kept. Third person plus „wir“ for the team, as in `voice.md`. |
| | One concrete client detail per section | 2 | 3/3 | Every section has one (dates, WhatsApp reminder, DeepOcean, 3 video analyses …). |
| | Sentence length varies | 2 | 3/3 | Fragments mixed with longer sentences. |

**Total: 73.5 / 100. BLOCK error in Fakten (claim list item = 0). Decision: nachbessern** (fix S02, S04, S05, S06, S08, S09, S10, then run the gates again).

### Shortest path to „liefern“

1. Fix R01 to R17 and R21 to R26 in the draft. This is text only, and no approved line changes.
2. Add the missing claims (R10, R11, media logos) to `claims.json`. Add R04 to R06 only after client approval.
3. Write `OPEN-FLAGS.md` and complete `placeholders.md` (R18).
4. Rebuild `schema.jsonld` (SEO fix 1).
5. Write a word-count verdict sentence with source and date in `gates.md`.

Expected score after these steps: about 90, with no BLOCK error.

---

## Round 2 (draft-v4.md, 2026-10-11)

Scope: I checked v4 against the Round 1 gaps. I also looked for new errors from the fixes. I read the updated `claims.json` (C01 to C19), `placeholders.md` (6 rows), `OPEN-FLAGS.md` (F1 to F11) and `gates.md` for v4. As instructed, I did not check `05-final/schema.jsonld`.

Independent check: I read https://www.meandyou.de/agb again (Firecrawl, maxAge 0). The text matches C15 word for word: „Stornierungen sind bis 8 Wochen vor Beginn gegen 30% Stornogebühr möglich. Danach ist der volle Preis fällig.“ The S10 answer is a correct paraphrase.

### Round 1 gaps: status

Closed: R01, R02, R03, R04, R05 (removed, F10), R06 (AGB verified), R07, R08, R09, R10 (C10), R11 (C16, phrase removed), R12 (new H2, see N1), R13, R14 (see N2), R15, R16 (topic titles plus placeholder, F7), R17, R18 (files written), R20, R21, R22, R23, R24, R25, R26.
Open but tracked: R19 schema (prototype, not checked).

All quotes in v4 match the source. That includes Emrullah A. (G9), „[…] zwischen …“ and ‚keine großen Redner‘. Address form is du only. No prices, no forbidden words, no „4,9“. Words: 1,823 (gate). This is above the current page (1,787) and inside the brief range of 1,800 to 2,400.

### New errors from the fixes

**N1 · S08 · M · conflicts with the facts**
- Quote: „## Was Teilnehmer nach drei Tagen schreiben“
- Why wrong: Jenny writes „Diese vier Rhetorik Seminartage“. Adrian writes „vier intensive Tage“. S09 says „Jeder Termin dauert vier Tage“. The Peter Escher quote comes from the old website. We do not know that he attended a three-day seminar.
- Fix: „## Was Teilnehmer über das Seminar schreiben“

**N2 · S10 · L · suggests levels**
- Quote: „im Einstieg zum Beispiel freie Rede und Struktur, danach Schlagfertigkeit oder die Stegreifrede.“
- Why wrong: „danach“ suggests an order. S06 says „Kein Stufenmodell … eigenständige Formate, die du frei wählst“.
- Fix: „im Einstieg zum Beispiel freie Rede und Struktur, in den anderen Formaten Schlagfertigkeit oder die Stegreifrede.“

**N3 · S06 card „Frei sprechen“ · L · repeated phrase**
- Quote: „außerdem die richtigen Fragen. Mit den richtigen Fragen lenkst du Gespräche in deine Richtung.“
- Fix: „Dazu kommen Körpersprache und Sprache. Mit den richtigen Fragen lenkst du Gespräche in deine Richtung.“

**N4 · S06 card „Mit Sprache führen“ · L · meaning changed from the source**
- Quote: „Methoden, mit denen große Redner im Alltag überzeugen“
- Why wrong: The PDF says „Methoden großer Redner im Alltag“. That means you use their methods in your daily life. The draft says the great speakers persuade in their daily life.
- Fix: „Dazu Stegreifreden vor einer Gruppe und Methoden großer Redner, die du im Alltag nutzt.“

**N5 · S11 · L · repeated point**
- Quote: bullet „kostenlos“ directly under „Ein Gespräch, 30 Minuten, kostenlos.“
- Fix: Replace the bullet with „Termin online wählen“ (backed by S07 and C16), or delete it.

**N6 · line 18 HTML comment · L · old note**
- Quote: „ProvenExpert-Wert 4,9 gerechnet“
- Why wrong: The page no longer uses 4,9 (F2). A later agent can read this comment and add the number again.
- Fix: „ProvenExpert ohne Gesamtnote, 227 von 250 mit 5 Sternen (F2).“

### Remaining gaps

**N7 · S10 „Bin ich als Anfänger richtig?“ · L · plural with one source (I missed this in Round 1)**
- Quote: „Teilnehmer schreiben, dass Michael alle weiterbringt, egal auf welchem Level.“
- Why wrong: Only one review says this (Christin R., P4).
- Fix: „Christin R. schreibt auf ProvenExpert, dass Michael alle weiterbringt, egal auf welchem Level.“

**N8 · TECH / gates.md · L · scorecard item**
- Quote: „Wortzahl-Urteil: siehe gates.md“
- Why wrong: `gates.md` still has no verdict sentence.
- Fix: Add one line to `gates.md`: „Wortzahl 1.823: über Bestand (1.787, `_work/bestand-dedup.txt`) und über 70 % des Medians (1.747, `_work/bench-metrics.json`), Stand 2026-10-11.“

**N9 · S10 · L · open facts not marked in the text**
- Quote: „die Übernachtungen im Seminarzeitraum“ (S10, twice) and „über 30 Jahren“ (S01, S02, S04)
- Why wrong: Both are rows 3 and 4 in `placeholders.md`. The text does not mark them yellow. The scorecard needs open client facts marked as placeholders.
- Fix: Add a placeholder marker for the prototype, for example `<!-- placeholder: 3 -->` and `<!-- placeholder: 4 -->`, so the build shows them in yellow until the client confirms.

Note, not a gap: G6 counts 6 sentences in the answer block. The block itself has 4 sentences and 44 words. The gate probably also counts the bullet list and the quote, so no text change is needed.

Count: **9 items left** (1 medium, 8 low). No high gaps are left.

### Scorecard, Round 2

| Block | Item | R1 | R2 | Points R2 | Reason for the change |
|---|---|---|---|---|---|
| Textqualität | Hook | 2 | 2 | 5 | |
| | Pain before solution | 2 | 2 | 5 | |
| | CTA | 2 | 2 | 5 | |
| | Objections | 1 | 1 | 2.5 | Confidentiality still open (F9) |
| | Scan format | 2 | 2 | 5 | |
| SEO und GEO | H1, title, meta | 2 | 2 | 4 | |
| | Answer block, definition, entities | 1 | 2 | 4 | Question H2, 44 words, „Die Methode hat drei Schritte“ |
| | FAQ from PAA | 2 | 2 | 4 | |
| | G6 incl. date and schema | 1 | 1 | 2 | Date added. Schema is in the prototype and is not checked yet |
| | Internal links | 1 | 2 | 4 | Anchors name the topic. Keyword overlap has a plan (F8) |
| | Word count with verdict sentence | 1 | 1 | 2 | Numbers OK, verdict sentence missing (N8) |
| Fakten (BLOCK) | Every claim in claim list | 0 | 2 | 10 | C15 to C19 added. AGB verified |
| | Local fact | 2 | 2 | 5 | |
| | Placeholders | 0 | 1 | 2.5 | All listed, but two not marked in the text (N9) |
| Recht (BLOCK) | G2 | 2 | 2 | 10 | |
| | Grey areas listed and decided | 0 | 1 | 2.5 | Listed in F1 to F11, Martin has not decided yet |
| Slop und Stil | G5 | 2 | 2 | 5 | |
| | G4 | 2 | 2 | 5 | |
| Lesegefühl | Voice | 2 | 2 | 4 | |
| | Client detail per section | 2 | 2 | 3 | |
| | Sentence rhythm | 2 | 2 | 3 | |

**Total: 92.5 / 100 (Round 1: 73.5). No BLOCK error.** The claim check now passes. The open facts and grey areas are listed and wait for the client or Martin, which is normal at Checkpoint 2.

**Decision: liefern**, after these small text fixes: N1 to N5 and N7, plus the housekeeping in N6, N8 and N9. None of them needs a new client fact. After the fixes, run G1 to G6 again. Then Martin decides F1 to F11 at the checkpoint.

SEO note: Internal links and GEO now meet the Round 1 fixes. Schema stays unscored until the prototype JSON-LD exists. Then validate it in the Rich Results Test. Local signals stay limited until the phone number is decided (placeholder 5).
