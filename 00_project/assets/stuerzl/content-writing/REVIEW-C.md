# REVIEW-C: ST-21, ST-26, ST-20, ST-23 (correctness review, 2026-10-11)

Reviewer: independent, read only. Scope: correctness gaps only (A facts, B BRAO/UWG, C brief, D consistency, E SEO). Quotes are German and kept under 15 words. "Fix" is one line.

Checks that passed on all four pages: no dashes (— or –), Sie only, wir for the firm, no word from the forbidden list (spezialisiert, Experte, Expertise, beste, kostenlos, Festpreis and so on), phones match nap.json, no amounts in the cost block, cost model is time based with "gegen Pauschale" for the Erstberatung, titles of Dr. Stürzl are the same on every page and match the live profile, all internal links exist in slugs.json, sections S01 to S09 are in order.

---

## ST-21 Unternehmensvertretung. VERDICT: FIX FIRST

1. Quote: "Nicht, wenn sie derselben Tat beschuldigt sind (§ 146 StPO)." (FAQ). Why: § 146 Satz 2 also bars one lawyer from defending several accused of different offences in one proceeding. The text says it is allowed for other offences. Fix: add Satz 2.
2. Quote: "Hat ein Mitarbeiter gehandelt, kommt es darauf an, ob die Leitung die nötige Aufsicht unterlassen hat." (S07) and FAQ "Wann ist die Leitung für Verstöße von Mitarbeitern verantwortlich?" Why: § 130 OWiG binds the "Inhaber", and only for duties that "den Inhaber treffen" and carry a penalty or fine. The page swaps Inhaber for Leitung and drops the duty condition. The link Leitung to Inhaber (§ 9 OWiG) is not in the saved law texts. Fix: write "Inhaber", add the duty condition, or save § 9 OWiG.
3. Quote: "Bei einer Ordnungswidrigkeit bestimmt deren Höchstmaß die Grenze." (S07). Why: § 30 Abs. 2 Satz 3 OWiG can raise the maximum tenfold where a law points to § 30. Also § 30 Abs. 4 covers "eingestellt" and "von Strafe abgesehen" and has a bar when the act cannot be prosecuted. Fix: add the tenfold rule and the Abs. 4 bar.
4. Quote: "Sie schrieb Aufsätze zu den Risiken von GmbH-Geschäftsführern (GmbH-Steuerpraxis, 2020)." Why: the live profile lists them "gemeinsam mit" other authors (Lersch, Schauf). The text reads as sole authorship (UWG: misleading). Fix: "verfasste gemeinsam mit …".
5. Quote: "Auf der Kanzleiseite sagt sie: „Effektive Strafverteidigung ist nicht zwingend ‚laut‘ …" Why: claim U22 and the live files show the quote on the Startseite (home.txt), not the Kanzlei page. Fix: "Auf der Startseite".
6. Quote: "Auch die Übernahme von Geldbußen und Verteidigungskosten für Mitarbeiter gehört zu den Fragen" (S07). Why: the only source is a live line with a typo ("Überahme") and no explanation. Advertising advice on paying fines for staff is legally sensitive and unconfirmed (flag A5 is still open). Fix: cut it until the client explains.
7. Quote: "§ 164 StGB … wider besseres Wissen einer rechtswidrigen Tat verdächtigt, macht sich … strafbar." Why: the statute also needs a report "bei einer Behörde" and the aim to start an official procedure. Fix: add both conditions.
8. Quote: "Aus einem Zeugen kann schnell ein Beschuldigter werden. Manchmal wird eine Person bewusst als Zeuge geführt." Why: client words, no statute or other source, grey zone for fear wording (LR16) and a claim about authorities. Fix: soften or get the client to confirm.
9. H1 "Unternehmensstrafrecht: Vertretung …" against S02 "kein Strafrecht für Unternehmen als solche". Why: H1 names a field the text says does not exist; reads as a Fachgebiet label (flag A1, still open). Fix: decide with Martin before release.
10. Brief: seller layer (S01 to S06, S09, without S07 and S08) counts about 606 words by my count; the limit is 550. Fix: check with wordcount.py and cut.
11. Placeholders sit in the visible text with internal notes ("der Kundentext nennt eine Spanne, die Live-FAQ andere Sätze"). Fix: strip the note before the text goes to the client.

Scores: intent 78, depth 82, GEO 76, E-E-A-T 74, local 55, technical 80, schema 60, internal links 82.
Two lowest: local 55 (only "Frankfurt und München" in H1 and phones, no street address, no local fact). Schema 60 (schema.jsonld has WebPage, BreadcrumbList, LegalService only; the TECH note promises Service, Person, FAQPage).
Top 3 text gaps: (a) add one line with both office addresses from nap.json in S09; (b) rename the H3 "Mitarbeiter als Zeugen" to include "Zeugenbeistand" (320 searches) and explain "Sockelverteidigung" in one sentence (50 searches, now undefined); (c) start the FAQ "Wann macht sich ein Geschäftsführer strafbar?" with a direct answer, not "Das hängt von der Tat ab".

---

## ST-26 Compliance. VERDICT: FIX FIRST

A. Correctness gaps
1. Quote: "die rechtssicher und im Alltag umsetzbar sind" (S04 step 3) and "Unser Fokus liegt auf rechtssicheren, pragmatischen Lösungen" (S07). Why: "rechtssicher" promises legal certainty of the firm's output. It is a result claim (§ 43b BRAO, UWG). It is not in the flag list (A2 covers only "schützen" and "reduzieren"). Fix: "rechtlich geprüft".
2. Quote: "Voraussetzung ist, dass im Betrieb eine Zuwiderhandlung … begangen wird, die gehörige Aufsicht verhindert oder wesentlich erschwert hätte." Why: the grammar makes the duty the subject. The statute says "durch gehörige Aufsicht verhindert … worden wäre". It also drops "Pflichten, die den Inhaber treffen". Fix: copy the statute structure.
3. Quote: "Die Leitung kann nach § 130 OWiG ordnungswidrig handeln, wenn sie die nötige Aufsicht unterlässt." (FAQ) and the H3 "Pflichten der Geschäftsleitung und Aufsicht nach § 130 OWiG". Why: § 130 binds the Inhaber, not the Leitung. Fix: say Inhaber; explain the Leitung link with § 9 OWiG (not saved).
4. Quote: "kann die Geldbuße bis zu einer Million Euro betragen (§ 130 Abs. 3 Satz 1 OWiG)". Why: Satz 2 applies § 30 Abs. 2 Satz 3 OWiG (tenfold rule). The page shows a ceiling that can be too low. Flag A4 knows this, the text still has the plain figure. Fix: "grundsätzlich bis …; in bestimmten Fällen höher".
5. Quote: "gibt innerhalb von drei Monaten eine Rückmeldung (§ 17 HinSchG)". Why: § 17 Abs. 2 says three months after the confirmation of receipt (or three months and seven days after receipt). Fix: add "nach der Bestätigung".
6. Quote: "Steuerstrafrechtliche Risiken prüfen wir auch vorab in einem Gutachten." Why: no claim in claims.json backs this service on this page (it exists on ST-13 only). Fix: add a claim with source.
7. Quote: "Wer selbst gegen ein Gesetz verstößt, kann zudem persönlich verfolgt werden." and "Ein Compliance-Verstoß ist ein Verstoß gegen Gesetze oder gegen interne oder externe Verhaltensstandards." Why: no source. The second is a definition built from the client text, but not quoted from it. Fix: add claims or cut.
8. Quote: "Dabei suchen wir nach rechtlichen Risiken." (S04 step 2). Why: process steps 2 and 3 are not in the client text or in a claim. Fix: add a claim from the client or word it as the client's "Überprüfung".
9. Brief: target /leistungen/ is in the brief and is not linked. Fix: add the link.
10. Brief: seller layer about 590 words by my count against the limit of 550. Fix: check with wordcount.py.

B. Compliance text against the client text (compliance.txt). Changed in meaning or dropped:
- Dropped: "zentrales Steuerungsinstrument moderner Unternehmensführung".
- Dropped: "Unabhängig von Größe und Struktur … essenziell". Only "Die Regelungsdichte wächst" stays.
- Changed: "schützen nicht nur präventiv vor (straf-)rechtlichen Risiken" became "können vor straf- und bußgeldrechtlichen Risiken schützen". Softened with "können". Scope narrowed from legal risks to criminal and fine risks.
- Dropped: "sichern zugleich Reputation und schaffen langfristig Vertrauen und Stabilität".
- Changed: "maßgeblich dazu beitragen … zu reduzieren oder im Einzelfall sogar zu vermeiden" became "kann … beitragen, Sanktionsrisiken … zu reduzieren. Das gilt nur im Einzelfall." "maßgeblich" and "vermeiden" are cut. "Im Einzelfall" moved from "vermeiden" to the whole effect. The meaning is narrower (safer). The client has not approved this.
- Dropped: "kein nice-to-have … integraler Bestandteil einer ganzheitlichen Verteidigungsstrategie". Cut on purpose ("ganzheitlich").
- Changed: "Aufgrund unserer langjährigen Erfahrung … kennen wir die praktischen Herausforderungen" became a loose "mit langjähriger Erfahrung im Wirtschafts- und Steuerstrafrecht" (S03). The link from experience to compliance work is gone.
- Changed: bullet "Beratung zu aufsichts- und organisationsrechtlichen Pflichten von Geschäftsleitung und Organen" is narrowed to § 130 and § 30 OWiG and gets a new service claim ("prüfen, ob die vorhandenen Strukturen sie abdecken").
- Dropped as a service: "Unterstützung bei der Umsetzung komplexer regulatorischer Vorgaben". It stays only as a trigger bullet in S03, and "komplexer" is gone.
- Dropped: the whole closing "Unser Ziel … Risiken frühzeitig zu erkennen und zu kontrollieren, Haftung zu vermeiden … Handlungsspielraum … zu sichern". Cut on purpose.
- Dropped: "in allen Phasen … bis hin zur effektiven Verteidigung im Ermittlungs- und Gerichtsverfahren". The page never offers court defence, only "Behörden und Ermittlungsorganen".
- Kept almost word for word: the Leitlinie, the six bullets (reworded), "strukturierte und diskrete Aufarbeitung", "Begleitung gegenüber Behörden und Ermittlungsorganen".
Claims that go beyond the client text: "Verstöße lassen sich … nie ganz ausschließen" (from the live OWi page, not from compliance.txt); the full HinSchG block (statute backed, with the gaps above); the Tax Compliance block with § 153 AO and publications (flag A5); the Gutachten sentence; the FAQ definitions; process steps 2 and 3.
Verdict on "Haftung vermeiden / schützen": "Haftung vermeiden" is gone, good. "schützen" stays twice ("können vor … Risiken schützen", "entfaltet ihren Schutz"). The first sits in the answer block under the H2, where answer engines will quote it as a claim. Not a clear BRAO breach because of "können", but it is the client's softened wording. Better: the client's own phrase "Maßnahmen zur Risikobegrenzung". Worse than "schützen" is "rechtssicher" (gap 1).

Scores: intent 82, depth 76, GEO 80, E-E-A-T 82, local 42, technical 80, schema 60, internal links 68.
Two lowest: local 42 (no office, no city and no address anywhere in the text; only phone labels). Schema 60 (WebPage, BreadcrumbList, LegalService only; no FAQPage, no Person).
Top 3 text gaps: (a) add "Büros in Frankfurt und München" and both addresses in S09; (b) add H3 terms with demand: "Hinweisgebersystem" (720), "Compliance Schulung" (390), "Rechtsanwälte" for "compliance anwalt" (70); (c) add the missing links (/leistungen/ from the brief, and the pillar /sonstiges-wirtschaftsstrafrecht/).

---

## ST-20 Wirtschaftsstrafrecht. VERDICT: FIX FIRST

1. Quote: "Die Strafandrohung reicht bis zu fünf Jahren Freiheitsstrafe oder Geldstrafe." (S07, Subventionsbetrug). Why: wrong ceiling. § 264 Abs. 2 StGB gives six months to ten years in especially serious cases. The page names the ten years for Betrug but not here. Fix: add Abs. 2.
2. Quote: "§ 266 Abs. 1 StGB sieht Freiheitsstrafe bis zu fünf Jahren oder Geldstrafe vor." (S07, FAQ "Welche Strafe droht bei Untreue?"). Why: § 266 Abs. 2 applies § 263 Abs. 3, so especially serious Untreue also reaches ten years. The answer is incomplete for a question about "welche Strafe". Fix: add Abs. 2 with § 263 Abs. 3.
3. Quote: "Die Frist beträgt drei Wochen nach Zahlungsunfähigkeit und sechs Wochen nach Überschuldung (§ 15a Abs. 1 InsO)." (FAQ). Why: the statute says "ohne schuldhaftes Zögern" and "spätestens". The FAQ reads like a safe period. S07 has the words, the FAQ drops them. Fix: add both.
4. Quote: "Pflichten des Unternehmens können so auch die Geschäftsführung strafrechtlich treffen." Why: § 14 Abs. 1 StGB speaks of "besondere persönliche Merkmale" and says the law is applied to the representative. "Pflichten" is the page's own word. The line before ("gelten besondere persönliche Merkmale … auch für ihn") turns the statute around. Fix: use the statute wording.
5. Quote: "schrieb den Aufsatz „Wann dem Geschäftsführer Strafe wegen Untreue gegenüber der GmbH droht“" Why: the claim W13 and the profile say "gemeinsam mit Jana Hammesfahr". Sole authorship is implied. Fix: add the co-author.
6. Quote: "stehen die Rechtsgebiete Wirtschaftsstrafrecht, Compliance sowie Steuerstrafrecht." (S05, Dr. Glogger). Why: repeats a list of practice areas for a lawyer who joined in April 2026. It works like an Interessenschwerpunkt claim without proof (LR12, LR15). Fix: cut, or use the client's exact wording after confirmation.
7. Quote: "Wir prüfen, ob der Vorwurf zum Kern des Wirtschaftsstrafrechts gehört." (S04). Why: "Kern" is never defined. With H1/title "Anwalt für Wirtschaftsstrafrecht" it reads as a field claim (flag A1 still open). Fix: define in one sentence from the client's live text, or drop "Kern".
8. Quote: "Das Wirtschaftsstrafrecht umfasst Straftaten im wirtschaftlichen Zusammenhang" (S02). Why: no claim backs this definition. § 74c GVG is a court competence list. Fix: add a source or word it as "Zum Wirtschaftsstrafrecht zählen häufig".
9. Quote: "Er nennt die Straftaten, die beim Landgericht die Wirtschaftsstrafkammer verhandelt." (S02, FAQ). Why: § 74c applies only where the Landgericht is the competent court (§ 74 Abs. 1, 3), and part of the list needs "besondere Kenntnisse des Wirtschaftslebens". S02 and FAQ drop this. Fix: add "soweit …".
10. Quote: "Der Bankrott nach § 283 Abs. 1 StGB sieht Freiheitsstrafe bis zu fünf Jahren oder Geldstrafe vor." Why: Abs. 1 needs Überschuldung or (drohende) Zahlungsunfähigkeit and a listed act. The page gives only the penalty. Fix: one clause on the conditions.
11. Brief: seller layer about 588 words against the limit of 550.

Scores: intent 80, depth 72, GEO 76, E-E-A-T 70, local 55, technical 80, schema 60, internal links 85.
Two lowest: local 55 (Frankfurt und München only in title, H1 and phones; no address). Schema 60 (no FAQPage, no Person).
Top 3 text gaps: (a) add the NAP line with both addresses; (b) add the common term "Insolvenzverschleppung" to the H3 on § 15a (term absent now); (c) add the claim and one sentence on Dr. Stürzl's teaching post in the LL.M. Wirtschafts- und Steuerstrafrecht (live profile, Köln) to lift E-E-A-T for this topic.

---

## ST-23 Ordnungswidrigkeiten. VERDICT: FIX FIRST

1. Quote: "wenn ein Verstoß geschieht, den gehörige Aufsicht verhindert oder wesentlich erschwert hätte." (S07). Why: § 130 OWiG needs a breach of a duty that "den Inhaber trifft" and is backed by penalty or fine. The page says any "Verstoß". It also drops "vorsätzlich oder fahrlässig". The sentence before says "Organisationsverschulden … Das regelt § 130 OWiG" and uses Leitung for Inhaber. Fix: copy the conditions.
2. Quote: "Ausreichende Compliance-Maßnahmen können helfen, Leitungspersonen zu schützen." Why: no statute backs it. It rests on a client sentence that was stronger ("schützen … die Leitungspersonen"). It is an outcome claim about the firm's field (A3 still open). Fix: cut, or "Ob Maßnahmen im Einzelfall wirken, hängt vom Sachverhalt ab".
3. Quote: "Ja, unter den Voraussetzungen des § 30 OWiG … bis zu zehn Millionen Euro" (FAQ "mein Unternehmen"). Why: "Ja" to the reader's own company reads like a case assessment. It also shows only the 10 and 5 million figures. For an Ordnungswidrigkeit as base act the maximum follows the OWi maximum, with the tenfold rule (§ 30 Abs. 2 Satz 2 und 3). Fix: "Das ist möglich, wenn …" and add the OWi rule.
4. Quote: "Ein Beispiel: Auch wenn ein Steuerberater die Erklärung vorbereitet hat, bleibt der Steuerpflichtige verantwortlich." Why: the live FAQ answer is about criminal risk and ends "andernfalls macht man sich ggf. (mit) strafbar". The page cuts that, recasts it as an example of leichtfertige Steuerverkürzung (an OWi), and has no source that blind signing is "leichtfertig". The question asks for examples and the answer gives none. Fix: restore the live sentence or add a source.
5. Quote: "Die Verfolgung von Ordnungswidrigkeiten nach den §§ 378 bis 380 AO verjährt in fünf Jahren (§ 384 AO)." Why: the FAQ title asks about any Steuerordnungswidrigkeit; § 384 also names § 383a, and other ones follow OWiG § 31 (saved, not used). No start date, no word on interruption. Fix: scope the question and add the start rule with source.
6. Quote: "Auf der Kanzleiseite sagt sie: „Jedes Mandat und jeder Mandant ist anders.“" Why: the source is the Startseite. Fix: "Auf der Startseite".
7. Quote: "muss der Täter sie innerhalb der ihm bestimmten angemessenen Frist entrichten." Why: § 378 Abs. 3 Satz 2 is a condition for no fine ("wird nicht festgesetzt, wenn …"), not a duty. Also "gegenüber der Finanzbehörde" is missing in Satz 1, and § 371 Abs. 4 applies. Fix: write it as a condition.
8. Quote: "Wir vertreten Sie gegenüber der Finanzbehörde und, wenn nötig, vor Gericht." (S04). Why: no claim backs court representation in OWi matters on this page. Fix: add a claim.
9. Brief: the pillar /sonstiges-wirtschaftsstrafrecht/ is a brief target and is not linked. The page has only 5 links.
10. Brief: seller layer about 566 words against the limit of 550.

Scores: intent 82, depth 80, GEO 78, E-E-A-T 76, local 50, technical 78, schema 60, internal links 52.
Two lowest: local 50 (city only in H1 and phones; no address). Internal links 52 (5 links, no pillar, no Steuerstrafrecht, no Verjährung or Ratgeber link).
Top 3 text gaps: (a) add links to /sonstiges-wirtschaftsstrafrecht/, /steuerstrafrecht/, /ratgeber/verjaehrung/ and /steuerfahndung-durchsuchung/; (b) define "leichtfertig" with a source and name "Aufsichtspflichtverletzung" (320 searches) in the H3 on § 130; (c) add the NAP line with both addresses.

---

## Cross-page problems

1. § 130 OWiG is paraphrased four different ways. ST-21 and ST-26 FAQ say Leitung, ST-23 drops the duty condition, ST-26 has a garbled sentence. All should carry one agreed wording: Inhaber, duty of the Inhaber, penalty or fine, "durch gehörige Aufsicht … worden wäre".
2. The § 30 OWiG ceilings differ. Only ST-21 mentions the OWi rule. ST-23 shows only 10 and 5 million. ST-26 shows only "eine Million" for § 130. The tenfold rule (§ 30 Abs. 2 Satz 3) appears nowhere.
3. Quote source: ST-21 and ST-23 say "Kanzleiseite", ST-20 says "Sie sagt". Real source for both quotes: Startseite.
4. Co-authors are missing in ST-20 and ST-21, present in ST-26. Make one rule.
5. Boilerplate is identical on ST-20, ST-21, ST-23 and ST-26: S03 closing ("Wir stehen Ihnen zur Seite, mit langjähriger Erfahrung …"), S06 cost block, FAQ confidentiality and cost answers, S09. "Fehler passieren …" repeats on three. Risk of thin or duplicate content between sibling pages.
6. "Pauschale" has two meanings in ST-26 (Honorar-Pauschale and Erstberatung-Pauschale in neighbouring paragraphs). Only ST-21 says what the Erstberatung contains. Make the wording equal on all pages and on ST-31.
7. Tax Compliance overlaps: ST-13 has "Tax Compliance" in title and H1, ST-26 has an H3 and an FAQ on it. Keyword cannibalisation until the client decides (placeholder 2).
8. Dr. Glogger appears with a credential (ST-21, ST-26) and with a practice-area list (ST-20). Use one confirmed block.
9. ST-22 and ST-24 sub pages have no slug and are not linked from ST-21 and ST-23.
10. Schema files hold only WebPage, BreadcrumbList, LegalService on all four, while the TECH notes of ST-21 promise Service, Person, FAQPage.
11. The seller layer is over 550 words on all four by my count. Run wordcount.py to confirm.
12. Placeholders carry internal remarks inside the visible text on all four. Strip before client delivery.
13. Open grey-zone flags still in the text: "Anwalt für Wirtschaftsstrafrecht" (ST-20), "Unternehmensstrafrecht" (ST-21), "möglichst geräuschlos" (all four), "langjähriger Erfahrung" (all four). The batch lists the live-site risk words as not adopted, which is correct. Martin must decide these four before release.
