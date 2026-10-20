# REVIEW-B: independent review of batch B (ST-11, ST-13, ST-10, ST-32)

Reviewer: independent, read only. Date: 2026-10-11. Scope: correctness gaps only. Quotes from the pages stay German and stay under 15 words.
Checked against: legal-rules.md, fact-rules.md, voice.md, nap.json, source-of-truth-2026-10-11.md, content-writing-stuerzl-batch.md section 2, claims.json, brief.json, saved statute texts in each `_work/law`, the live FAQ `selbstanzeige/_work/live/faq.txt`, slugs.json, scoring-rubric.md.

Checks that passed on all four pages (no action): no dashes (em or en), no forbidden word from the batch list, no "kostenlos/Festpreis/24/7", Sie only, wir for the firm, phone numbers match nap.json, no hours or emergency numbers shown, no old address, every internal link exists in slugs.json, titles of Dr. Stürzl match claims (Fachanwältin für Steuerrecht seit 2021, Zertifizierte Beraterin für Steuerstrafrecht (DAA) seit 2022; both confirmed in the live profile and the CV), cost model is time-based with no amounts.

---

## ST-11 Steuerstrafrecht (Säulenseite). VERDICT: FIX FIRST

### Correctness gaps
1. S07 Verjährung: "Spätestens verjährt die Verfolgung nach dem Doppelten der gesetzlichen Frist (§ 78c Abs. 3 StGB)." The page applies this rule to the 15-year cases too. § 376 Abs. 3 AO (saved in `_work/law/ao_1977__376.txt`) sets the 2.5-fold limit for those cases. ST-36 says this correctly, so the two pages contradict. Fix: add "im Grundfall; in den Fällen des § 376 Abs. 1 AO das Zweieinhalbfache (§ 376 Abs. 3 AO)".
2. S07 and FAQ "Wann verjährt": "in besonders schweren Fällen 15 Jahre (§ 376 Abs. 1 AO)". The statute limits this to "§ 370 Absatz 3 Satz 2 Nummer 1 bis 6". The FAQ drops the limit. A besonders schwerer Fall without a Nr. 1 to 6 example stays at 5 years (§ 78 Abs. 4 StGB). Fix: write "in den Fällen des § 370 Abs. 3 Satz 2 Nr. 1 bis 6 AO".
3. S07 Selbstanzeige: "muss das nach § 153 AO unverzüglich anzeigen und die erforderliche Richtigstellung vornehmen." § 153 Abs. 1 binds the Steuerpflichtiger (and successors) and only "vor Ablauf der Festsetzungsfrist". The text says "Wer" and drops both conditions. Fix: "Wer als Steuerpflichtiger vor Ablauf der Festsetzungsfrist nachträglich erkennt, …".
4. S05 quote: "Auf der Kanzleiseite schreibt sie: „Effektive Strafverteidigung ist nicht zwingend ‚laut‘ …" The source is the Startseite box (`live/home.txt` line 21), not the Kanzlei page. The live text has a sentence between the two sentences ("Es gibt nicht die eine „richtige“ Verteidigungsstrategie."). The page joins them without a cut mark. Fix: "Auf der Startseite der Kanzlei" and add [...] or quote the two sentences separately.
5. H1 and title: "Anwalt für Steuerstrafrecht: Verfahren und Verteidigung". It reads as a field title (LR12, LR17, § 7 BORA). No proof of a Schwerpunkt exists in the claim list. OPEN-FLAGS A1 leaves it open, so it is still an open gate. Safer fix: H1 "Steuerstrafrecht: Verfahren und Verteidigung"; keep "Anwalt Steuerstrafrecht" in the title only after the Kanzlei and Martin approve.
6. S03: "schildern Sie sie uns kurz." This asks for situation details. It conflicts with the S01 and S09 line "Nennen Sie uns nur Ihr Thema" (LR14, § 203 StGB). Fix: "nennen Sie uns Ihr Thema".
7. S02: "Der wichtigste Tatbestand ist die Steuerhinterziehung nach § 370" is an unbacked judgement; no claim covers "wichtigste". Fix: "Zentral ist die Steuerhinterziehung nach § 370 AO" or add a source.
8. S06 placeholder: "[von Kunde bestätigen: Höhe der Pauschale für die Erstberatung, …]". It asks for an amount on a page that must carry no amounts, and the note text leaks internal remarks. Fix: delete the placeholder and keep "gegen Pauschale"; the figure lives on /kosten/ only.
9. TECH line is stale: "Frankfurt ohne Straße bis die Adresse bestätigt ist". The address is confirmed and the schema file already holds "Untermainkai 26". Fix the note.
10. Grey (Martin decides, already in OPEN-FLAGS A6): S07 "Dort gibt es zahlreiche Möglichkeiten, auf die Ermittlungen einzuwirken." Reads close to an outcome hint. Soften or confirm with the Kanzlei.

### SEO scores (0 to 100)
1 intent 80 | 2 depth 82 | 3 GEO-extractability 84 | 4 E-E-A-T 80 | 5 local signals 55 | 6 technical on-page 88 | 7 schema 50 | 8 internal links 85
Lowest two. Local 55: only "Büros in Frankfurt und München" and phone numbers; no street address and no hours visible on the page. Schema 50: `schema.jsonld` has WebPage, BreadcrumbList, LegalService only; no Person for Dr. Stürzl although S05 is a person block; no Service.
Top 3 page-text gaps (additive): (a) add a visible NAP block with both addresses and the confirmed phone hours (Mo bis Fr 09:30 bis 14:30, Termine nach Vereinbarung); (b) add a small table "Fristen und Strafrahmen auf einen Blick" built only from saved statutes (370, 376, 78, 169) for GEO; (c) add a reviewer line under the H1: "Fachlich geprüft von Dr. Anja Stürzl, Rechtsstand Oktober 2026" (needs Kanzlei OK) and add Person schema.

---

## ST-13 Gutachten und Risikobewertung. VERDICT: FIX FIRST

### Correctness gaps
1. Title, H1 and meta: "Tax Compliance: Gutachten und Risikobewertung im Steuerstrafrecht". The Kanzlei text does not mention Steuer (pruefung-2026-10-11.md point 4: "Nicht selbst ergänzen"). The service is unproven (LR15) and the question sits only in a placeholder in S07. S02 also defines the term without a source: "Tax Compliance heißt: Ein Unternehmen hält seine steuerlichen Pflichten ein." Fix: title and H1 "Gutachten und Risikobewertung im Steuerstrafrecht"; take "Tax Compliance" out of the meta until Dr. Glogger answers; mark the S02 definition as client-to-confirm.
2. S07 § 30 OWiG: "Zusätzlich kann nach § 30 OWiG gegen das Unternehmen selbst eine Geldbuße festgesetzt werden". § 30 Abs. 1 names the "juristische Person oder Personenvereinigung", not every Unternehmen (a sole trader is outside). It also allows a fine when the entity was enriched. Fix: "gegen die juristische Person oder Personenvereinigung" and name the groups ("Organ", "Prokurist" and so on) in short.
3. S07 § 130 OWiG: "Wer als Inhaber … die Aufsichtsmaßnahmen unterlässt … handelt nach § 130 OWiG ordnungswidrig". The statute says "vorsätzlich oder fahrlässig" and requires that the violated duty is threatened with Strafe or Geldbuße. Both are dropped. The H3 says "Verantwortung der Leitung", but the text names only the Inhaber. Fix: add both elements; for Leitungspersonen cite § 9 OWiG (file exists in the batch law folders) or change the H3.
4. Outcome wording (LR10, LR16): S03 "möchten die Korrektur so gestalten, dass kein unnötiges Risiko entsteht"; FAQ "damit eine Korrektur kein unnötiges Risiko eingeht"; S07 "selbstanzeigesicheren“ Korrektur". All three promise or imply a safe result. Fix: "damit Sie die Folgen einer Korrektur vorab kennen"; replace "selbstanzeigesicher" with "mit Blick auf die Anforderungen des § 371 AO" or get the Kanzlei's explicit OK for their own term.
5. S07 block 1 puts "Eine Steuerhinterziehung nach § 370 AO ist mit Freiheitsstrafe bis zu fünf Jahren … bedroht" directly after the § 153 duty, for readers who only found an error. This reads as a threat (LR4). Next sentence: "Sie ist auch dann sinnvoll, wenn … kein vorwerfbares Fehlverhalten erkennbar ist" reads as advice on a case. Fix: split into two blocks (error without intent / intent) and cut the "sinnvoll" sentence or phrase it as "kann geprüft werden".
6. § 153 text: S07 and FAQ "Muss ich einen Fehler melden?": "sind Sie nach § 153 Abs. 1 AO verpflichtet". Same two missing conditions as ST-11 gap 3 (Steuerpflichtiger, vor Ablauf der Festsetzungsfrist). The "Ja, Pflicht" tone without the intent case is incomplete. Fix as in ST-11.
7. S03: "Ob sie strafrechtlich relevant sind, hängt davon ab, wie sie entstanden sind." No claim backs this; the client phrase is "hängt von einer ganzen Reihe an Faktoren ab" (C23). Fix: use the client phrase.
8. S07 block 3: "An kleine und mittelständische Unternehmen werden immer höhere Anforderungen … gestellt." A general fact with no source (F6). The live page frames it as "Unserer Erfahrung nach". Fix: attribute it to the Kanzlei's experience.
9. S05: "Auf der Kanzleiseite schreibt sie: „Jedes Mandat und jeder Mandant ist anders.“" Source is the Startseite (home.txt line 21). Fix: "Auf der Startseite der Kanzlei".
10. S06 amount placeholder: same as ST-11 gap 8.

### SEO scores (0 to 100)
1 intent 55 | 2 depth 58 | 3 GEO-extractability 75 | 4 E-E-A-T 82 | 5 local signals 55 | 6 technical on-page 75 | 7 schema 50 | 8 internal links 78
Lowest two. Intent 55: the keyword "tax compliance" has an informational SERP with no lawyer offer in the top 10 (OPEN-FLAGS B3), and the page does not deliver Tax-CMS content, only a 3 paragraph block "Tax Compliance im Unternehmen". Depth 58: no content on Tax-CMS parts, Betriebsprüfung or risk analysis steps that the competitors rank with.
Top 3 page-text gaps (additive): (a) once the Kanzlei confirms the offer, add a block "Was eine steuerstrafrechtliche Risikoprüfung umfasst" with steps; until then drop the keyword from title and H1 (see gap 1); (b) add a short table "§ 153 AO oder § 371 AO" from the live FAQ III and the saved statutes; (c) add visible NAP and a Person schema (Dr. Stürzl with her Tax Compliance publications).

---

## ST-10 Leistungen (Hub). VERDICT: FIX FIRST (text overlap above the limit; one grey word)

### Correctness gaps
1. S02: "Unser Fokus liegt auf dem Steuerstrafrecht." "Fokus" is a synonym of Schwerpunkt, which needs proof (LR12). The live sentence goes on with "hohe Spezialisierung". The page cut that but kept the claim. Fix: "Wir beraten und verteidigen im Steuerstrafrecht und in angrenzenden Gebieten des Wirtschaftsstrafrechts."
2. S03 card 1 is titled "Verteidigung im Steuerstrafverfahren" (the title of ST-12) but links to /steuerstrafrecht/ and /verteidigung-von-individualpersonen/. ST-12 is linked only in S04. Fix: link the card to /steuerstrafrecht/verteidigung-im-steuerstrafverfahren/.
3. S04: "schildern Sie sie uns kurz. Wir ordnen sie ein." Same conflict with "nur Ihr Thema" as ST-11 gap 6 (LR14). Fix: "nennen Sie uns Ihr Thema".
4. Text overlap with ST-11 is 31.1 % (163 of 524 shared 5-word phrases) and with ST-13 is 27.1 %. Limit is 25 %. See the overlap section below.
No other fact gap: the six card texts match `approved-copy.md` section 4 (cards 01 to 06). Card 01 is titled "Steuerstrafrecht" there; the page renamed it (see gap 2).

### SEO scores (0 to 100)
1 intent 85 | 2 depth 65 | 3 GEO-extractability 70 | 4 E-E-A-T 70 | 5 local signals 60 | 6 technical on-page 85 | 7 schema 45 | 8 internal links 80
Lowest two. Schema 45: only WebPage, BreadcrumbList, LegalService; no ItemList for the six areas. Depth 65: each card is one sentence; the page tells the reader nothing about when to choose which area beyond S04.
Top 3 page-text gaps (additive): (a) one more sentence per card that names the typical trigger (for example "Sie haben ein Schreiben der Steuerfahndung erhalten") without case detail; (b) a unique hub FAQ "Welcher Bereich passt zu meiner Lage?" instead of the copied confidentiality and cost answers; (c) visible NAP and the confirmed phone hours, plus ItemList schema. Also fix: only 2 inbound links to this hub (LINK-NETWORK.md).

---

## ST-32 FAQ. VERDICT: FIX FIRST

### Correctness gaps
1. Statements with no saved source stay in the text, against the batch rule ("Sonst Aussage streichen"). OPEN-FLAGS A1 to A3 admit this. List: S09 "Die Ausübung dieses Rechts darf nicht als Schuldeingeständnis gewertet werden." (placed after the § 136 cite, but § 136 does not say it); S09 "Die Einstellung enthält keinen Schuldspruch und ist kein Urteil." (not in § 153a); S09 Vorsatz "oder ihren Erfolg billigend in Kauf nimmt" (case law); S06 "ein Waffen- oder Jagdverbot oder Einschränkungen beim Reisepass"; S08 "Dieser Status beginnt mit der Einleitung des Verfahrens (§ 397 Abs. 1 AO)" (§ 397 defines the Einleitung, not the Beschuldigten status). Fix: cut each, or save the source (statute or BGH decision) and cite it.
2. S09: "muss mit einem Verspätungszuschlag rechnen (§ 152 AO)". § 152 Abs. 1 says "kann"; only Abs. 2 makes it mandatory (after 14 or 19 months), and Abs. 1 sets it aside for an excusable delay. Fix: "kann mit einem Verspätungszuschlag rechnen müssen" or cite Abs. 1 and 2 correctly.
3. S06 "Wann verjährt": "in besonders schweren Fällen 15 Jahre (§ 376 Abs. 1 AO)". Same missing limit "Nr. 1 bis 6" as ST-11 gap 2.
4. S06: "Wer leichtfertig Steuern verkürzt, handelt ordnungswidrig". § 378 Abs. 1 binds "als Steuerpflichtiger oder bei Wahrnehmung der Angelegenheiten eines Steuerpflichtigen". Fix: add the condition.
5. S07: "Bei Vorsatz oder Leichtfertigkeit gilt die Korrektur als Selbstanzeige (§ 371 AO, § 378 Abs. 3 AO)" and "Beide setzen voraus, dass die Steuererklärung … objektiv falsch war". This is the client's doctrine; the saved § 153 text has no such rule. Mark as client statement or add a source; also § 153 needs the same two conditions as ST-11 gap 3 (the FAQ says only "müssen Sie ihn nach § 153 AO anzeigen").
6. S06 "Wann kommt bei Steuerhinterziehung eine Freiheitsstrafe in Betracht?": the answer is about Bewährung, not about when prison applies. "setzt das Gericht … zur Bewährung aus, wenn die gesetzlichen Voraussetzungen erfüllt sind" hides the prognosis test of § 56 Abs. 1 ("wenn zu erwarten ist …"). It can read as a comfort promise. Fix: retitle "Kann eine Freiheitsstrafe zur Bewährung ausgesetzt werden?" and name the test.
7. S05 "Darf das Finanzamt meine Wohnung durchsuchen?": the answer never says what the Finanzamt or the Steuerfahndung may do (§ 102 StPO is general; § 404 AO is in the next answer). Fix: one sentence linking § 404 AO and § 105 StPO to the question.
8. Brief rule not met: the page and TECH note promise a first paragraph of 40 to 60 words. Counted: 21 of 40 answers meet it, 7 are above 60 (for example "zu spät abgegeben" 91, "Freiheitsstrafe" 74) and 12 are below 40 (for example "Konsequenzen" 23, "Verteidiger" 26).
9. Mythen format: the client uses "Falsch." and "Nein." at the start. The late-filing answer now starts "Doch, das kann es." and the client's advice "unbedingt vorher eine Fristverlängerung beantragen" became "sollte … klären". Meaning softened on purpose (A4). Keep, but Kanzlei must confirm.

### Live FAQ compared with the page (section by section)
Kept in meaning: I.1 Ablauf, Einleitungsvermerk (corrected to Aktenvermerk, A6), Strafbefehl, Urteil; I.2 BuStra, Steuerfahndung "Steuerpolizei", Hauptzollamt, Rentenversicherung, Finanzbehörden; I.3 Haftbefehl, Untersuchungshaft, Durchsuchungsbeschluss; I.4 Strafen, Konsequenzen, vorbestraft (rule replaced by BZRG, A7); III Unterschied § 153 / § 371, "Was kann schief gehen"; IV Anschlusserklärung, Akteneinsicht, Beschuldigter, Belehrung, Strafanzeige, Vollmacht-Zahl; V all five myths (Vorsatz, Steuerberater, Geldauflage, zu spät, Schweigerecht). Part II (Kosten) removed on purpose (client wish, B1).
Dropped or changed (the client must see this list):
- I.1 Abschluss: "In beiden Fällen gelten Sie nicht als vorbestraft." and the Geldauflage line "Offengelassen, ob der Vorwurf zutrifft" are gone. The myth answer lost "man gilt … nicht als vorbestraft".
- I.1 Strafbefehl: "Wird ein Einspruch eingelegt, geht es mit der regulären Hauptverhandlung weiter." is gone. I.1 also drops "oder ein Haftbefehl erlassen wird".
- I.2 Steuerfahndung: "im Auftrag der Straf- und Bußgeldsachenstelle oder Staatsanwaltschaft" is gone. Hauptzollamt: the live "Verfolgung … Vorenthalten von Sozialabgaben" became "prüft Schwarzarbeit". Rentenversicherung: "(vorsätzlich)" and the examples Schwarzarbeit and Scheinselbständigkeit are gone. BuStra: "(kleineren) Steuerdelikten" is gone.
- I.4: "Passentzug" became "Einschränkungen beim Reisepass" (softened).
- III: the second question "Stimmt es, dass man nur eine Selbstanzeige abgeben muss, wenn man absichtlich Steuern verkürzt hat?" is dropped. The answer "regelmäßig notwendig … selbst wenn man nicht vorsätzlich gehandelt hat" became "wird … oft so gestaltet". That core point for non-intentional errors is lost. Also dropped: "Entscheidung hängt von einer inneren Tatsache ab" and "Voraussetzungen … grundlegend unterschiedlich".
- IV: entries Bußgeldbescheid, Einleitungsverfügung, Einstellung gegen Geldauflage (cross references) and Vollmacht ("Strafprozessvollmacht") are gone. Belehrung lost "oder Zeugen" and "Aussagen können gegen ihn verwendet werden". Anschlusserklärung lost the reason (Sperrgrund der Tatentdeckung). Strafanzeige lost "von jeder Person gestellt".
- V Schweigerecht: "Sie sollten zunächst immer von diesem Recht Gebrauch machen und einen Anwalt kontaktieren" is dropped (A3, advice for a case). Steuerberater myth: "ggf. (mit) strafbar" became "mitstrafbar machen".
- Dropped for BRAO reasons and correct: "Worst Case Szenario", "Strafe muss sein? Möglich. Sogar wahrscheinlich", "nicht über den Tisch gezogen", Monopoly line, Hoeneß, "exzellenten Ruf", "24/7-Erreichbarkeit".
- Topic lost: the live heading "Kosten/Versicherung" (Rechtsschutz) has no home now (OPEN-FLAGS B1).

### SEO scores (0 to 100)
1 intent 85 | 2 depth 88 | 3 GEO-extractability 85 | 4 E-E-A-T 55 | 5 local signals 50 | 6 technical on-page 90 | 7 schema 45 | 8 internal links 68
Lowest two. E-E-A-T 55: no author or reviewer line and no named lawyer on a page full of legal answers (only "Wir" and "Rechtsanwälte"). Schema 45: LegalService, WebPage, BreadcrumbList; no FAQPage (a decision, kept), no Person.
Top 3 page-text gaps (additive): (a) add a reviewer line "Fachlich geprüft von Dr. Anja Stürzl, Fachanwältin für Steuerrecht, Rechtsstand Oktober 2026" with link (Kanzlei OK needed); (b) link to /steuerstrafrecht/verteidigung-im-steuerstrafverfahren/ (ST-12), /unternehmensvertretung/ and /dr-anja-stuerzl/ from fitting answers: the FAQ now has no link to ST-12, the page that owns "steuerstrafverfahren"; (c) bring the 19 out-of-band short answers into the 40 to 60 word band.

---

## Text overlap (link-network check, 5-word phrases, limit 25 %)
Method: same shingle logic as `link_network.py` (shared phrases divided by the smaller page).

ST-10 with ST-11: 163 of 524 = 31.1 %. Need at most 131, so cut at least 33 shared phrases; aim for 80. Rewrite or cut in ST-10 (shared / total phrases in the paragraph):
- FAQ "Bleibt meine Anfrage vertraulich?" 32/36: replace with a unique hub question.
- Closing block "Sprechen wir vertraulich über Ihre Situation" 30/30: write a hub-specific closing.
- FAQ "Was kostet die Beratung?" 22/33: shorten to one new sentence plus the /kosten/ link.
- S02 18/62 and S04 12/45: reword the repeated lead sentences.
- Hero reassurance 24/24, phone line 14/14, "Weitere Fragen und Antworten" 8/8: template lines shared by every page; vary the wording by page type.
After the first three changes the overlap drops to about 20 %.

ST-10 with ST-13: 27.1 %. Same boilerplate; the same three changes fix it.

ST-11 with ST-32: 505 of 1694 = 29.8 %. Need at most 423, so cut at least 83; aim for 130. Rewrite or cut in ST-11:
- S08 FAQ answers that ST-32 repeats word for word: "3.000 Euro" 39/39, "Bleibt meine Anfrage vertraulich?" 42/42, "Kosten für einen Anwalt" 38/51, "Wann verjährt" 28/40, "Welche Strafen" 22/42, "Wann fängt" 18/62, "Finanzamt bei Verdacht" 18/51. Make each a 1 to 2 sentence answer in new words plus a link to /faq/. This alone saves about 170.
- S07 "Welche Rolle die Verteidigung spielt" 83/112 and "Wie ein Steuerstrafverfahren abläuft" 38/65 and 47/87: these copy the § 136, 137, 147, 386, 397 sentences of ST-32. Keep one version only (the FAQ is the better home for the plain statute text); in ST-11 write the role of the defence in your own words.
- Closing block 44/48, hero 24/24, phone line 14/14: vary as above.

---

## Cross-page problems
1. Overlap above the limit: ST-10/ST-11 31 %, ST-10/ST-13 27 %, ST-11/ST-32 30 %. Cause: copied template blocks (hero reassurance, confidentiality FAQ, cost FAQ, closing CTA, phone line). Vary these per page type site-wide, not per pair.
2. Verjährung contradiction: ST-11 says the final limit is "das Doppelte" for all cases; ST-36 correctly says 2.5-fold for the § 376 cases. ST-11 and ST-32 both drop "Nr. 1 bis 6" for the 15-year rule.
3. § 153 AO is paraphrased without "Steuerpflichtiger" and without "vor Ablauf der Festsetzungsfrist" in ST-11, ST-13 (twice) and ST-32. Fix once in a shared sentence.
4. Erstberatung amount: ST-11 and ST-13 carry a visible placeholder for the amount; ST-10, ST-32 and ST-31 do not, and ST-31 says "nennen wir Ihnen vor dem Gespräch". Remove the amount placeholder from ST-11 and ST-13 so the figure lives on /kosten/ only.
5. "schildern Sie sie uns kurz" (ST-11 S03, ST-10 S04) conflicts with the rule "nur Ihr Thema" used in every CTA (LR14). Check the other batch pages for the same line.
6. Quote source: ST-11 and ST-13 both say "Auf der Kanzleiseite schreibt sie"; the quotes come from the Startseite. Check ST-43, ST-45 and others that reuse the quotes.
7. Keyword split: ST-13 keeps "tax compliance" while ST-26 (/compliance/) mentions tax compliance five times and takes "compliance beratung". Decide which page owns the term; ST-13 should not own it before the offer is confirmed. Likewise the sitetree gives "steuerstrafverfahren" to ST-12 and ST-32 (B3), and ST-32 does not link to ST-12.
8. Links to unbuilt pages: ST-11 (2) and ST-32 (1) link to /ratgeber/verjaehrung/ and /ratgeber/steuerhinterziehung-strafe/ (status Vorschlag). ST-10 and ST-13 link to /compliance/ (not approved). Remove or hold the links until the targets go live.
9. Grey wording that needs one decision for all pages: "Anwalt für Steuerstrafrecht" (H1/title, ST-11), "Fokus" (ST-10), "selbstanzeigesicher" (ST-13, ST-32), "konfrontativ" (ST-11). Martin and the Kanzlei decide once.
10. ST-10 gets 2 inbound links only and the hub card for ST-12 does not link ST-12 (see ST-10 gap 2).
