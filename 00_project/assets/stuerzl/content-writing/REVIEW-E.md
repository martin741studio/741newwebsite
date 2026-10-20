# REVIEW-E: Stürzl pages ST-43, ST-44, ST-45, ST-46, ST-49

Reviewer: independent, read only. Date: 2026-10-11. Scope: correctness gaps only (A facts, B BRAO/UWG, C brief, D cross-page, E SEO).
Checked against: legal-rules.md, fact-rules.md, voice.md, nap.json, source-of-truth-2026-10-11.md, slugs.json, batch brief section 2, live texts, each page folder, ext sources of ST-49.
Quotes are German, max 15 words. No dash characters were found in any of the five page.md files. No word from the forbidden list appears in a page body.

## ST-43 Kanzlei: VERDICT FIX FIRST

1. S06: "Auf der Kanzleiseite sagt sie: „Jedes Mandat und jeder Mandant ist anders.“" Why: the line is on the live Startseite (home.txt line 21), not on the Kanzleiseite. Claim C19 itself says Startseite. Fix: write "Auf der Startseite" or drop the place.
2. S03: "stehen wir im Austausch mit den Finanzbehörden." Why: no claim backs it. The live text only says guest lecturer at the Bundesfinanzakademie. The sentence suggests a special link to the tax authority (UWG, § 43b BRAO, misleading). Fix: cut the card. Keep the lecturer role in S06 only.
3. S03: "erreichen Sie uns unter 0160 3396513 oder 0160 95945730" and the heading "Persönlich erreichbar". Why: answering hours are not documented. "erreichen Sie uns" reads as a promise. Fix: say "Für dringende Fälle nennen wir diese Notfallnummern" and rename the heading.
4. S05 under "Was sich nachprüfen lässt": "Wir arbeiten nach dem Vier-Augen-Prinzip". Why: source is the unpublished client draft kosten.txt. It is a self-claim, not a verifiable fact. Fix: move to S07 or rename the heading.
5. S07: "vereinbaren wir die Vergütung zu Beginn des Mandats schriftlich mit Ihnen." Why: source says "üblicherweise" individual fee agreements. "schriftlich" is not in the source. Fix: "üblicherweise auf Grundlage einer Vergütungsvereinbarung". Delete "schriftlich".
6. S01: "Wir erklären Ihnen jeden Schritt." Why: not in claims.json. Only in approved-copy.md line 33. Fix: add a claim with that source.
7. S04: "unvermeidliche Verfahren zügig und geräuschlos zu beenden" with "arbeiten darauf hin". Why: still an outcome statement (LR10). OPEN-FLAGS A2 leaves it open. Fix: cut "zügig und geräuschlos" or get the client to take the risk in writing.
8. OPEN-FLAGS A1, A4, A5, A8: Stand "Kanzlei bestätigt". Why: the file header says no questions went to the client yet. No proof exists. Fix: set status "offen".
9. TECH: "NAP erst nach Freigabe der Frankfurter Adresse". Why: stale. The address is confirmed (nap.json). No schema.jsonld exists for this page. Fix: write the schema file.

Scores (0-100): 1 intent 72, 2 depth 74, 3 GEO 70, 4 E-E-A-T 74, 5 local 80, 6 technical 86, 7 schema 40, 8 links 92.
Lowest two: schema 40 (TECH note only, no JSON-LD). GEO 70 (answer block is good, 53 words, but no FAQ and no definition).
Top 3 text gaps: (1) The target keyword "wirtschaftsstrafrecht kanzlei" has no section that says what Wirtschaftsstrafrecht work the firm does. Only links in S04. (2) No Q and A block (Kosten, Vertraulichkeit, wer ist Ansprechpartner). (3) Trust data absent: no Kammer proof, no reviews or awards (placeholders only), no sameAs for Dr. Stürzl.

## ST-44 Team: VERDICT FIX FIRST

1. S03: "[Mehr zu Thorben Hoppe](/thorben-hoppe/)". Why: this path is not in slugs.json (ST-48 is empty). The link target does not exist in the plan. Fix: remove the link or add a slug and a page.
2. S03: "Mary, Chief Barking Officer (CBO)" listed with the team. Why: the live profile says she advises clients (UWG, misleading on a law-firm page). The placeholder is visible, but the card is still in the text. Fix: remove the card, or add a plain label such as "Bürohund", only with the client's go.
3. S04: "und Sie haben eine verlässliche Erreichbarkeit". Why: availability promise from an unpublished draft, no hours documented. Fix: cut that half sentence.
4. S04: "Nur wer mit unterschiedlichen Charakteren eng zusammenarbeitet, findet kreative Verteidigungsansätze". Why: absolute quality claim, no proof (live copy). Fix: "Wir sind überzeugt, dass ..." or cut.
5. S03: "Florentine Jilg, wissenschaftliche Mitarbeiterin." Why: Source of Truth Tab 01 Z46 names her role "Organisation/IT". Roles differ and the question is not in placeholders.md. Fix: add a client question or use a neutral title.
6. page.md TECH names Dr. Philipp Kellner, Alice Laporte, Nellie Runhaar. Why: brief says no former colleagues. The file travels to the CMS team. Fix: keep the names only in OPEN-FLAGS.md.

Scores: 1 intent 82, 2 depth 58, 3 GEO 60, 4 E-E-A-T 66, 5 local 65, 6 technical 78, 7 schema 35, 8 links 75.
Lowest two: schema 35 (Person per lawyer planned, nothing drafted). Depth 58 (409 words, bare lines for Hoppe and Jilg).
Top 3 text gaps: (1) No facts per person for Thorben Hoppe (no Rechtsgebiete, no career). The live profile lists "Strafrecht | Steuerrecht | Compliance" and the page omits them. (2) No street address and no direct contact per lawyer (the live profiles have email and phone). (3) No question blocks (Wer betreut mein Mandat? Welche Sprachen?) and no real photo or alt text.

## ST-45 Dr. Anja Stürzl: VERDICT FIX FIRST

1. S04: "So sagt es Dr. Anja Stürzl auf der Kanzleiseite." Why: all four quotes are on the live Startseite (home.txt line 21; claims C06 to C08 say Startseite). Fix: "auf der Startseite".
2. S05: "Sie erklären jeden Schritt und stehen Ihnen gegenüber Behörden und vor Gericht zur Seite." Why: "Sie" after "Dr. Stürzl und ihr Team" reads as the formal Sie (the reader). Also the claim is not in claims.json. Fix: "Das Team erklärt ..." and add the claim.
3. S04 card 4: "Fachliche Kompetenz verbindet sie mit Diskretion und Empathie." Why: the source is a firm statement in wir-form (kanzlei.txt), not a personal quote. "sie" is also unclear (Kanzlei or Dr. Stürzl). Fix: "Die Kanzlei verbindet ...".
4. S07: "Die vollständige Liste mit Vorträgen und Presseberichten finden Sie unter ..." Why: ST-49 is not complete. It omits the live item "Betriebsleiter als Verantwortlicher nach § 9 Abs. 2 Nr. 1 OWiG" (gate false positive) and the R&W and Bundesfinanzakademie talks. Fix: say "Eine Auswahl".
5. H1 and S02 use "Dr." but no line gives the basis. The dissertation (Peter Lang 2018) is proven only in ST-49 (C28). Fix: add one line with source to S06 or S07.
6. OPEN-FLAGS A1, A3, A7: "Kanzlei bestätigt". Why: no confirmation is on file. Fix: set status "offen".

Scores: 1 intent 90, 2 depth 80, 3 GEO 72, 4 E-E-A-T 78, 5 local 70, 6 technical 90, 7 schema 45, 8 links 90.
Lowest two: schema 45 (no JSON-LD file). Local 70 (Frankfurt and Munich named, phones given, but no address and no office link).
Top 3 text gaps: (1) Person schema not built and sameAs empty, although Source of Truth Tab 12 gives LinkedIn (Z26) and anwalt.de, Fürstenberg, R&W profile URLs. (2) Kammer admission, doctorate basis and awards are missing, so credentials stay partial. (3) Answer block has 5 sentences (G6 rule 2 to 4) and no liftable question (for example "Welche Titel führt Dr. Stürzl?").
Person-schema readiness: name, jobTitle, worksFor, alumniOf and knowsAbout are ready. Missing: sameAs, hasCredential with issuer, image, doctorate, Kammer. E-E-A-T: strong first-hand quotes and a dated career. Weak: no proof file for the titles.

## ST-46 Dr. Monika Glogger: VERDICT FIX FIRST

1. S06: five titles listed as hers, e.g. „Untreue und öffentliche Daseinsvorsorge“ with co-author Peters. Why: all ten live titles carry the byline "Werndl". The link to Dr. Glogger is unproven (placeholder only). If wrong, the page claims foreign publications. S03 repeats it: "Veröffentlichungen zum Unternehmensstrafrecht in Fachzeitschriften". Fix: hold S06 and the S03 bullet until the client confirms. Then add the Nomos 2019 dissertation, which is the link.
2. S06: "Das Profil von Dr. Glogger nennt Veröffentlichungen zu Themen des Unternehmensstrafrechts." Why: the live list also has Sicherungsverwahrung and terrorism titles. The Jahrbuch is not a Fachzeitschrift. Fix: "Auswahl aus der Publikationsliste des Live-Profils".
3. S04 heading: "Compliance: Wobei Dr. Glogger Unternehmen begleitet". Why: the list comes from the firm text compliance.txt, which names no author. The body says "Die Kanzlei berät". Fix: heading "Compliance bei STÜRZL Steuerstrafrecht".
4. S04: "und aus der Beratung durch eine Kanzlei". Why: the CV shows associate posts at Ufer Knauer and Streck Mack Schwedhelm with no compliance role. OPEN-FLAGS A5 covers only the first half. Fix: cut the second half.
5. page.md TECH and placeholders.md name Dr. Philipp Kellner (former colleague). Fix: keep only in OPEN-FLAGS.md.

Scores: 1 intent 85, 2 depth 62, 3 GEO 66, 4 E-E-A-T 55, 5 local 68, 6 technical 78, 7 schema 40, 8 links 74.
Lowest two: E-E-A-T 55 (one 2024 certificate, no Kammer, byline conflict, doctorate not shown). Schema 40.
Top 3 text gaps: (1) Resolve "Werndl" and show the dissertation as basis for "Dr.". (2) S04 is firm text. Add what she personally handles, from a client source. (3) No sameAs (the live LinkedIn link is broken, 404 per Source of Truth Tab 02 Z33), no photo, no /kontakt/ link, no address line.
Person-schema readiness: name, jobTitle "Rechtsanwältin", worksFor, alumniOf ready. sameAs and credential evidence not ready.

## ST-49 Publikationen: VERDICT FIX FIRST

1. S05: "**10. September 2026, JUVE:**" Why: the JUVE page shows 04.09.2026 12:05 (_work/ext/p3.html). 10.09. is the firm's own post date. Fix: 4. September 2026.
2. S05: "**6. August 2026, Capital Magazin:**" Why: date comes only from the firm's post. capital.de gave HTTP 403, so it is unchecked. Fix: check by hand or write "August 2026".
3. S04: "12. April 2024: Webinar „Steuerstrafverfahren und Besteuerungsverfahren: ..." under Dr. Stürzl's talks. Why: the source never names her (OPEN-FLAGS A8). The entry claims a talk. Fix: remove until the client confirms the role.
4. S01: "Hier finden Sie die Fachbeiträge unserer Kanzlei." Why: titles from 2019 to 2022 were written at Flick Gocke Schaumburg and Rettenmaier. Title and meta also say "von STÜRZL Steuerstrafrecht". Fix: "Fachbeiträge von Dr. Anja Stürzl".
5. S05: "Neue JUVE-Rankings: Wie Frauen im Strafrecht zur festen Größe wurden". Why: the linked title works as a ranking reference while rankings are unreleased. The firm's post says she is in the ranking. "Kluge Köpfe im Strafrecht" is a flattering column name too. Fix: drop both or get the client to release them.
6. S03: titles "... Wann dem Geschäftsführer Gefängnis droht" and "... Strafen drohen". Why: fear wording (LR16). OPEN-FLAGS A5 leaves it. Fix: drop these three entries or cite only the first title part with the client's go.
7. S03: titles were changed (dash to colon, typo fixed) and the IWW talk title is reworded. Why: a citation that is not exact is not a citation, and the change is not shown. Fix: cite exact or mark "gekürzt".
8. S03: the jurisPR-StrafR 9/2020 note is missing (script false positive). Why: the live profile lists it, and ST-45 calls this list complete. Fix: add it, fix the G2 pattern.
9. S05: LTO items of 10.10.2024 and 23.06.2025 sit under "Presse". Why: the LTO pages carry "Anzeige" banners. Only the first LTO item is marked "Kanzleimitteilung". Fix: mark all LTO items by type or ask the client.
10. S04: "20. November 2026: angekündigter Vortrag ..." Why: the Referenten page shows no day. 20.11. is only the Kongresstag. Fix: write "19. und 20. November 2026".

Scores: 1 intent 78, 2 depth 82, 3 GEO 62, 4 E-E-A-T 80, 5 local 45, 6 technical 80, 7 schema 40, 8 links 72.
Lowest two: schema 40. Local 45 (phones only, no address).
Top 3 text gaps: (1) No topic index. Entries are not grouped by theme and not linked to the service pages (Tax Compliance to /compliance/, § 153 AO and Teilselbstanzeige to /selbstanzeige/). (2) No JSON-LD (Article or ScholarlyArticle with Person author, CollectionPage). Several entries have no year. (3) Mixed attribution and unchecked dates, see 1 to 4.

## Cross-page problems

1. "Auf der Kanzleiseite" is wrong in ST-43 S06 and ST-45 S04. The quote is on the Startseite.
2. ST-45 S07 says "vollständige Liste" and ST-49 is a selection. ST-49 omits a live item.
3. /thorben-hoppe/ (ST-44) has no slug. /lea-wimmer/ (ST-47, in slugs.json) is linked from ST-44 and ST-49 but ST-47 is not in this batch.
4. Munich office date has no single answer. ZRI 09.10.2024 (opening planned by Jan 2025, Leopoldstraße), LTO 23.06.2025 (team in Munich), Dr. Stürzl CV 03/2026, Source of Truth "seit Anfang 2026" (Oberanger 32). ST-49 lists the 2024 and 2025 items. Pick one wording before ST-42, ST-43, ST-49 go live.
5. Founding wording. ST-43 S02 "Büros in Frankfurt am Main und München, gegründet ... im Dezember 2023" reads as two offices at founding. ST-45 and ST-41 say founded in Frankfurt. The live CV says "Frankfurt/München".
6. Vier-Augen-Prinzip appears in ST-43 S05, ST-44 S02 and S04. The source is the unpublished kosten.txt. These pages need the /kosten/ page live in the same go.
7. Hoppe: ST-41 says he advises in Frankfurt and Munich since June 2026. ST-43 S06/S08 and ST-44 S04 name only Stürzl (Frankfurt) and Wimmer/Glogger (Munich) as contacts.
8. "Kanzlei bestätigt" in OPEN-FLAGS of ST-43, ST-45, ST-46 conflicts with the rule that no questions went out yet.
9. Names of former colleagues sit in ST-44 and ST-46 page.md TECH notes and in ST-46 placeholders.md.
10. Spelling "LL. M." (ST-43 to ST-46) vs "LL.M." (ST-41, ST-42, ST-45 S07). Pick one.
11. None of the five pages has a schema.jsonld, while ST-41 has one. The #kanzlei @id and sameAs must be set once for all pages.
12. Cost model, Sie/wir, no-dash rule and internal link slugs (except item 3) are consistent across the five pages. Lea Wimmer, Dr. Glogger and Dr. Stürzl titles match across pages and match the live profiles.
