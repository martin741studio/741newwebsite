# REVIEW-G: Batch G (ST-34, ST-35, ST-36, ST-37)

Reviewer: independent, read only. Date: 2026-10-11. Language: simple English. Quotes stay German (max 15 words).
Scope: correctness gaps only (A facts, B BRAO/UWG, C blog rules, D cross-page, E SEO rubric).
Method: I read page.md, brief.json, claims.json, placeholders.md, OPEN-FLAGS.md and the saved statute texts in _work for each page. I checked the saved BGH text (ST-35) and the saved BMF text (ST-37). I ran two web checks (current BGH case law on "großes Ausmaß"; BMF crypto letter status; Art. 97 § 23 EGAO). The web sources are secondary. Items from them are marked "check primary".

## Verdicts

| Page | Verdict | Main reason |
| --- | --- | --- |
| ST-34 Hub | FIX FIRST | Repeats two absolute limitation statements. States "Rechtsstand 11. Oktober 2026" for posts that are not at that state. |
| ST-35 Strafe | FIX FIRST | The 100.000 Euro limit is outdated (BGH 2015). Führungszeugnis rule is incomplete. Four statements have no saved source. |
| ST-36 Verjährung | FIX FIRST | "15 Jahre" and "Spätestens" are too absolute. "Beginn" claim ignores § 78a Satz 2. One FAQ claim has no legal basis. |
| ST-37 Krypto | FIX FIRST | One-year rule stated without the 10-year exception. Key PAA not answered. Steuerberater sentence misleads on intent. |

## ST-35 Steuerhinterziehung: Strafe und Strafrahmen

### A. Facts

1. OUTDATED (S04, FAQ "Gefängnis", claim L09, flag A1). Quote: "hält der Senat 100.000 Euro für angemessen". The text is correct for BGH 1 StR 416/08 (saved, Rn. 34 ff. and Leitsatz 5). But the BGH gave up the 100.000 Euro limit for pure "Unkenntnis" cases in Urteil vom 27.10.2015, 1 StR 373/15. Since then one limit applies: 50.000 Euro for every case (check primary; I read it in a 2016 secondary article, stb-web.de, and a 2024 Rose & Partner note). The page states "Rechtsstand: 11. Oktober 2026" and says "Stand von 2008". The 2008 sentence is not just old; it is wrong for today. Fix: delete the 100.000 sentence, state one limit of 50.000 Euro, cite 1 StR 373/15, save the ruling text, and update claim L09.
2. TOO ABSOLUTE (S06, claim L12). Quote: "Ins Führungszeugnis nimmt das Gesetz Verurteilungen zu einer Geldstrafe von nicht mehr als 90 Tagessätzen nicht auf". The saved § 32 BZRG has Abs. 4: for the Behördenführungszeugnis these convictions are included again if the crime was committed in a business context (relevant for Gewerbe, § 149 GewO). The conviction also stays in the register. Fix: say "im privaten Führungszeugnis" and add the Abs. 4 exception.
3. NO NORM / UNCLEAR (S07). Quote: "In beiden Fällen gelten Sie nicht als vorbestraft." The paragraph lists three routes (§ 170 Abs. 2 StPO, § 398 AO, § 153a StPO), so "beiden" is unclear. No norm is saved. Flag A4 says the text avoids "vorbestraft", but S07 uses it. Fix: use "keine Verurteilung" and cite, or cut.
4. NO SOURCE (S06, flag A2, claim L17 "Normen nicht geprüft"). Quote: "Waffen- oder Jagdverbot oder Passentzug". Rule B6: no source, no statement. Fix: name and read the norms, or cut the sentence.
5. NO SOURCE (S07). Quote: "Legen Sie keinen Einspruch ein, steht der Strafbefehl einem Urteil gleich." No StPO § 407/§ 410 text is saved. Fix: save and cite, or cut.
6. TOO ABSOLUTE (FAQ Selbstanzeige, claim L14). Quote: "Liegt die verkürzte Steuer über 25.000 Euro je Tat, tritt die Wirkung nach § 371 nicht ein." The saved § 371 Abs. 2a removes this limit for late or wrong Umsatzsteuer-Voranmeldungen and Lohnsteuer-Anmeldungen. Fix: add "grundsätzlich" and one clause on Abs. 2a, or use the ST-14 wording.
7. INCOMPLETE (S07). Quote: "Dafür braucht es die Zustimmung des Beschuldigten und des Gerichts (§ 153a Abs. 1 StPO)." The saved § 153a also needs: Auflagen remove the public interest and "die Schwere der Schuld nicht entgegensteht". The page reads as if consent and payment are enough. Fix: add both conditions.
8. WRONG SOURCE (FAQ "leichte Steuerhinterziehung", claim L17). Quote: "Er liegt auch vor, wenn jemand die Tat wissentlich begeht". The definition is cited next to § 15 StGB, which holds no definition (saved text is one sentence). The source is the live FAQ. Fix: cite a ruling or mark it as general doctrine without a § 15 reference.
9. Minor: § 41 StGB paraphrase drops "angebracht ist". § 40 StGB drops "wenn das Gesetz nichts anderes bestimmt".

### B. BRAO / UWG

- S08 step 3 gives a directive without knowing the case. Quote: "Reichen Sie nichts ein, bevor die Lage geklärt ist." It can delay a Selbstanzeige and acts as individual advice (rule B7). Fix: "Eine Selbstanzeige hat strenge Voraussetzungen. Lassen Sie vorher prüfen, ob sie in Ihrem Fall noch möglich ist."
- FAQ "Erstberatung" (quote: "klären wir in der Erstberatung"). The Source of Truth (Z17, Z19) says the Erstberatung is paid (250 to 350 Euro). The page implies a free first check ("klären wir mit Ihnen vorab"). Fix: say "kostenpflichtige Erstberatung" or link ST-31 once approved (LR13).
- Fachanwältin Steuerrecht seit 2021: claim C01 says "Kammernachweis offen". LR12 needs proof. Not provable now.
- No result promise, no superlative, no fear word found. No case assessment found.

### C. Blog rules

- Visible "zuletzt geprüft am" missing. Only "Rechtsstand: 11. Oktober 2026" (B5).
- Link to money page (ST-12) only in S03. None at the end (B8). Two CTAs (S08 and S11) where B9 asks for one.
- Author line is a placeholder (B4). Sources section present. Note "allgemeine Information, ersetzt keine Beratung im Einzelfall" present. No dashes found.

### E. SEO scores (0 to 100)

| Intent | Depth | GEO | E-E-A-T | Local | Technical | Schema | Links |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 85 | 78 | 85 | 45 | 35 | 85 | 20 | 72 |

Two lowest: Schema 20 (no JSON-LD produced, flag B6). Local 35 (national post; Frankfurt and München appear only in the phone line, "Frankfurt +49 69 298028870, München +49 89 72444170").
Top 3 page-text gaps: (1) PAA "Wie lange dauert ein Strafverfahren" is not answered (flag A6) although the SERP gate lists it. (2) No scannable "Strafrahmen auf einen Blick" table (Grundfall, besonders schwerer Fall, Geldstrafe, Bewährung) to lift for AI answers. (3) No author, no "zuletzt geprüft", no money-page link at the end.

## ST-36 Verjährung der Steuerhinterziehung

### A. Facts

1. TOO ABSOLUTE (S02, S03 table, FAQ, hub, ST-11). Quote: "in den besonders schweren Fällen nach 15 Jahren (§ 376 AO)". The saved § 376 Abs. 1 covers only "§ 370 Absatz 3 Satz 2 Nummer 1 bis 6". An unnamed besonders schwerer Fall keeps 5 years (§ 78 Abs. 4 StGB). The 15 years also apply only to acts not yet time-barred on 29.12.2020 (Art. 97 § 23 EGAO; not saved, check primary). Fix: write "in den Fällen des § 370 Abs. 3 Satz 2 Nr. 1 bis 6" and add the transition note.
2. INCOMPLETE / MISLEADING (S04, FAQ). Quote: "Wann eine Steuerhinterziehung beendet ist, steht weder dort noch in § 370 AO." The saved § 78a Satz 2 says: "Tritt ein zum Tatbestand gehörender Erfolg erst später ein, so beginnt die Verjährung mit diesem Zeitpunkt." The statute does give the hook. The page then drops the most searched sub-question (start of the period) as "Einzelfall". Fix: quote Satz 2, state clearly what is not read (BGH rules on Beendigung), and put it on the Kanzlei list.
3. TOO ABSOLUTE and self-contradicting (S04). Quote: "Spätestens verjährt die Verfolgung, wenn seit dem Beginn das Doppelte". § 78c Abs. 3 Satz 3 (saved): "§ 78b bleibt unberührt". The next paragraph ("Hinzu kommt das Ruhen") breaks the "Spätestens". Fix: "grundsätzlich spätestens ..., außer bei Ruhen (§ 78b)".
4. NO LEGAL BASIS (FAQ "Wann fängt Steuerhinterziehung an?", claim V13 = Kanzlei FAQ). Quote: "steht schon ab dem ersten Tag nach Fristablauf eine Hinterziehung durch Unterlassen im Raum". § 370 Abs. 1 needs a Verkürzung; § 370 Abs. 4 says Steuern are verkürzt when not (in time) festgesetzt. On day one after the deadline there is usually no Verkürzung for Veranlagungssteuern. No statute or ruling is saved. Fix: cut, or rewrite as "Vollendung erst bei Verkürzung; vorher kommt der Versuch in Betracht" with a source.
5. WRONG WORDING (S02, hub). Quote: "darf hinterzogene Steuern bis zu zehn Jahre festsetzen". "Bis zu" is wrong: § 171 Abs. 5 and 7 (saved) extend it. The page says so in S05. Fix: "zehn Jahre, und die Frist kann länger laufen".
6. TOO ABSOLUTE (FAQ Durchsuchung). Quote: "Ja, bei der Verfolgungsverjährung." § 78c Abs. 1 Nr. 4 names the richterliche Anordnung, not the search. A search under Gefahr im Verzug without a judge is not listed. Fix: "Ja, wenn ein Richter sie angeordnet hat."
7. INCOMPLETE (S05). Quote: "Spätestens beginnt sie mit Ablauf des dritten Kalenderjahres". Saved § 170 Abs. 2 Nr. 1 adds "es sei denn, dass die Festsetzungsfrist nach Absatz 1 später beginnt". Abs. 6 and 7 (foreign capital income, Drittstaat-Gesellschaft) delay the start up to 10 years. Fix: add "in der Regel" and one line on Abs. 6 and 7.
8. INCONSISTENT (S02, S03). S02 says "zwei Fristen nebeneinander". The table has three types (Verfolgung, Festsetzung, Zahlung); the text after it says "Die dritte: die Zahlung." Fix: say three.

### B. BRAO / UWG

- No case assessment, no promise, no superlative, no fear word found. Step 3 "Rechnen Sie nicht allein" is acceptable.
- Same title proof gap as ST-35 (C01).

### C. Blog rules

- Money page (ST-14) linked in S03 and S06, not at the end (B8). No visible "zuletzt geprüft am". Author placeholder. Sources, disclaimer present. No dashes found.

### E. SEO scores

| Intent | Depth | GEO | E-E-A-T | Local | Technical | Schema | Links |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 85 | 68 | 85 | 45 | 35 | 85 | 20 | 68 |

Two lowest: Schema 20 (none, flag B6). Local 35 (national post; only the phone line names the cities).
Top 3 gaps: (1) Start of the period is not answered, yet "Wann fängt ... an" and "5 oder 10 Jahre" are the main questions. (2) No worked timeline (for example Erklärung 2021 -> Festsetzungsfrist -> Verfolgungsverjährung), so no liftable example. (3) PAA answer for "Wann fängt Steuerhinterziehung an?" answers a different question.

## ST-37 Krypto und Steuerhinterziehung

### A. Facts

1. TOO ABSOLUTE (FAQ "Haltedauer"). Quote: "liegt kein privates Veräußerungsgeschäft ... vor". The saved § 23 Abs. 1 Satz 1 Nr. 2 Satz 4 raises the period to 10 years when the asset yields income in at least one year (Staking, Lending). BMF Rn. 63 removes this only for Currency and Payment Token. S03 also states the one-year rule for "Kryptowerte" in general. Fix: limit the sentence to Currency and Payment Token and name Satz 4.
2. MISLEADING (S04, claim K12 = live FAQ). Quote: "bleibt der Steuerpflichtige für die Angaben verantwortlich". It sits inside the Vorsatz paragraph. Responsibility for a return is not intent. No norm saved. Fix: move to a "Pflichten" paragraph with § 150 Abs. 2 AO, or cut.
3. QUESTION NOT ANSWERED (FAQ). H3: "Muss ich Kryptogewinne unter 600 Euro bei der Steuer angeben?" The answer gives the limit only. It does not say yes or no. "Weniger als 1.000 Euro" (§ 23 Abs. 3 Satz 5) is a Freigrenze: at 1.000 Euro the whole gain is taxable. The page does not explain this. A reader could conclude "nothing to declare". Fix: answer first, using only EStG text; make no claim on a reporting duty without a source.
4. NOT CHECKED FOR CURRENCY (S03, claims K01 to K04). The BMF letter of 6.3.2025 is presented at "Rechtsstand 11. Oktober 2026". The BFH ruling 14.02.2023, IX R 3/22, was not read (flag A1). A search found no newer BMF letter (check primary). Fix: add "Stand BMF-Schreiben vom 6. März 2025" and have the Fachanwältin read it.
5. INCOMPLETE (S05). Quote: "Die Pflichten sind erstmals für das Kalenderjahr 2026 zu erfüllen." With § 9 (31. Juli) the first report is due 31.7.2027. The page never says so. § 9 covers "zu meldende Nutzer" only; § 13 also names authorities of other states. Fix: add the date and the two limits.
6. INCOMPLETE (S06). The Selbstanzeige paragraph omits the 25.000 Euro limit and § 398a, the case that matters most for crypto amounts. Quote: "zum Beispiel nach Bekanntgabe der Einleitung eines Strafverfahrens". Fix: one sentence plus link to ST-14.

### B. BRAO / UWG

- S07 step 2 gives a directive without knowing the case. Quote: "Reichen Sie nichts vorschnell ein." Same fix as ST-35.
- Same title proof gap (C01). No promise, no superlative, no fear word found.
- Scope: the page explains tax law while the Kanzlei does not list general tax advice (flag A2). Acceptable only with the Fachanwältin's review.

### C. Blog rules

- Link to money page (ST-14) first appears in S06, which is mid-page, not in the first third (B8). None at the end. No visible "zuletzt geprüft am". Author placeholder. Disclaimer, sources present. No dashes found.

### E. SEO scores

| Intent | Depth | GEO | E-E-A-T | Local | Technical | Schema | Links |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 70 | 62 | 80 | 40 | 35 | 82 | 20 | 58 |

Two lowest: Schema 20 (none). Local 35 (national).
Top 3 gaps: (1) The PAA "Muss ich ... angeben" is not answered. (2) No "Selbstanzeige bei Krypto" section, although the SERP top 5 (crypto-crime.de, kleinstb.de, rosepartner.de) cover it; the page has 4 sentences. (3) No date for the first KStTG report, so the "Finanzamt erfährt es" point is not liftable. Demand: 20 searches (flag A5), so priority is low.

## ST-34 Ratgeber (Hub)

### A. Facts

1. Quote: "in besonders schweren Fällen nach 15 Jahren (§ 376 AO)" and "bis zu zehn Jahre festsetzen". Same fixes as ST-36 gaps 1 and 5. Claim H02 copies the wording.
2. Quote: "Die Beiträge geben den Rechtsstand vom 11. Oktober 2026 wieder." Not true for ST-35 (2008 and 2015 BGH) and not checked for ST-37 (BMF 2025). Fix: remove the date from the hub or tie it to the fixes.
3. Quote: "sobald eine Behörde eine Maßnahme trifft". Saved § 397 Abs. 1 lists Finanzbehörde, Polizei, Staatsanwaltschaft, Ermittlungspersonen, Strafrichter. A Strafrichter is not a Behörde. Fix: use the statute list.

### B. BRAO / UWG

- Quote: "Was gilt, wenn die Steuerfahndung vor der Tür steht?" is mild fear framing (LR16 spirit). Fix: "Was gilt bei einer Durchsuchung?".
- Titles (Fachanwältin 2021, Zertifizierte Beraterin 2022): same proof gap.

### C. Blog rules

Hub, not a post, so B4/B5 do not apply. FAQ answers repeat ST-35 and ST-36 FAQ text (B10, cannibalisation). Flag A1 (keyword "steuerstrafrecht" belongs to ST-11) is still open.

### E. SEO scores

| Intent | Depth | GEO | E-E-A-T | Local | Technical | Schema | Links |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 68 | 52 | 70 | 55 | 50 | 80 | 20 | 82 |

Two lowest: Schema 20 (none; CollectionPage planned only). Depth 52 (538 words; each card is one sentence; the 4 FAQ repeat the posts).
Top 3 gaps: (1) Cards are teasers with no definition of Steuerstrafrecht or an overview that a reader or an engine can lift. (2) No link up to the pillars ST-11 or ST-12; the hub links only to ST-14, ST-18, ST-32, ST-45. (3) Primary keyword "steuerstrafrecht ratgeber" has no volume data; the hub text does not name the cities or the "Fachanwältin" context in the first screen.

## Cross-page problems

1. 15-year and "Spätestens" wording is copied into ST-34 (FAQ), ST-36, and ST-11 ("In den besonders schweren Fällen des § 370 Abs. 3 Satz 2 AO beträgt sie 15 Jahre"; "Spätestens verjährt ... Doppelten"). Fix once, then sync all three.
2. "Bis zu zehn Jahre festsetzen" is in ST-34 and ST-36. ST-11 says "Sie beträgt zehn Jahre". Pick one wording.
3. ST-35 gives 25.000 Euro limit without Abs. 2a; ST-14 has the same gap (no mention of Abs. 2a, checked by search). ST-37 gives no limit at all. The three pages differ in how they present § 371 Abs. 2 Nr. 3 and § 398a.
4. Only ST-35 uses a court limit (BGH). ST-11 mentions "großes Ausmaß" without a number. After the fix to 50.000 Euro, check ST-11, ST-12 and ST-18 for any old BGH 100.000 figure (grep found none in ST-11 or ST-14; the 100.000 in the ST-14 table is the § 398a step, not the BGH limit).
5. Cannibalisation (B10): ST-11 holds full sections "Strafen" and "Verjährung" and FAQ on both, the same questions as ST-35 and ST-36. ST-14 FAQ "Wie hoch ist die Strafe bei 5.000 Euro" overlaps ST-35 FAQ "10.000 Euro". The hub FAQ repeats both posts.
6. Hub and ST-11 link to ST-35, ST-36 which are unapproved proposals (flags A2). Publish order matters.
7. The Erstberatung wording (ST-35 FAQ, "klären wir vorab" in ST-35, ST-36, ST-37 steps) conflicts with the paid Erstberatung in the Source of Truth. Align with ST-31.
8. All four pages carry the same title proof gap (Fachanwältin 2021 from CV, no Kammer proof) and the "wir" voice against blog rule B4 (first person of the author). Both depend on the author decision.
9. Both of the "Reichen Sie nichts ein" steps (ST-35, ST-37) push the reader away from a Selbstanzeige while ST-14 promotes it. Align the message.
