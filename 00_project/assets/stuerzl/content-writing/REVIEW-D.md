# REVIEW-D: independent review, batch D (ST-25, ST-27, ST-28, ST-31)

Reviewer: independent, read only. Date: 2026-10-11. Scope: correctness gaps only (A facts, B BRAO/UWG, C brief, D consistency, E SEO). Quotes are German, short. "Sev" = High / Med / Low.
Sources checked: legal-rules.md, fact-rules.md, voice.md, nap.json, source-of-truth snapshot, batch file section 2, each page.md, brief.json, claims.json, placeholders.md, OPEN-FLAGS.md, saved statute texts in _work, live FAQ, kosten.txt, ki-baustein.txt, approved-copy.md.
Checked and clean on all four pages: no dash characters; Sie and wir used; one primary CTA text "Vertraulich anfragen"; no word from the forbidden list; no amount in visible text; phones, addresses and hours (Mo bis Fr 09:30 bis 14:30, Termine nach Vereinbarung) match nap.json; no "24/7"; titles of Dr. Stürzl identical on all pages; all internal links exist in slugs.json; section order follows the brief.

---

## ST-25 Korruptionsstrafrecht: VERDICT FIX FIRST

Correctness gaps
1. High, A. FAQ "Welche Folgen kann ein Korruptionsvorwurf für ein Unternehmen haben?": "Hinzu kommen kann die Einziehung dessen, was durch die Tat erlangt wurde (§ 73 StGB)." Why: § 73 Abs. 1 binds Täter oder Teilnehmer. The saved § 30 Abs. 5 OWiG says a Geldbuße against the legal person excludes Einziehung under §§ 73, 73c for the same Tat. The text puts both together as "Hinzu". Fix: split person and company, or add the § 30 Abs. 5 limit.
2. High, A. S07 block "Amtsträger": "Beide sehen Freiheitsstrafe bis zu drei Jahren oder Geldstrafe vor." Why: true for § 331 Abs. 1 and § 333 Abs. 1 only. Abs. 2 (Richter, Schiedsrichter) has up to five years. The next sentences (sechs Monate bis fünf Jahre; drei Monate bis fünf Jahre; ein Jahr bis zehn Jahre) are Abs. 1 values and skip the minder schwere Fälle and § 332 Abs. 2 (one to ten years; § 335 Abs. 1 Nr. 2 at least two years). Fix: add "für Amtsträger (Absatz 1)" and one sentence that Richter have higher frames.
3. Med, A. S07 block 1: "ohne Einwilligung des Unternehmens ... eine Handlung vornehme oder unterlasse". Why: § 299 Abs. 1 Nr. 2 and Abs. 2 Nr. 2 apply only "bei dem Bezug von Waren oder Dienstleistungen". The text drops that limit and widens the offence. Fix: add the limit.
4. Med, A. S07 block 4: "Der Grund liegt in § 4 Abs. 5 Satz 1 Nr. 10 EStG" and "stehen regelmäßig auch Steuerhinterziehungsvorwürfe im Raum". Why: the statute gives a deduction ban and a duty to inform the tax office (Satz 2). It does not say tax-evasion charges follow "regelmäßig", and it is not "der Grund". The only source is the old live page (claim C25). Fix: "Ein Anknüpfungspunkt ist ..." or cut "regelmäßig".
5. Med, A. Same block and the FAQ: "Gegen ein Unternehmen kann nach § 30 OWiG eine Geldbuße festgesetzt werden". Why: § 30 Abs. 1 names juristische Person and Personenvereinigung. A sole trader is not covered. Fix: use the statute wording.
6. Med, A. S05: "Auf der Kanzleiseite schreibt sie: „Jedes Mandat und jeder Mandant ist anders.“" Why: the quote stands on the Startseite box (selbstanzeige/_work/live/home.txt, line 21; claim C23 says Live-Start), not on the Kanzlei page. Fix: "Auf der Startseite".
7. Med, A/C. S05: "Korruptionsdelikte gehören nach Darstellung der Kanzlei zu den typischen Begleitdelikten einer Steuerhinterziehung." Why: the firm speaks about itself in the third person (voice rule: wir), and the live source ("Unsere rechtliche Expertise erstreckt sich auch auf viele typische „Begleitdelikte“") is turned into a general legal claim. Fix: "Wir beraten auch bei Korruptionsdelikten, die neben einer Steuerhinterziehung auftreten können."
8. Med, A. S06: "Was sie kostet, nennen wir Ihnen vor dem Gespräch." and "vereinbaren die Vergütung ... schriftlich". Why: claim C33 cites approved-copy F1, but F1 has no such sentence (F1 names a range and says the Vergütungsvereinbarung is fixed before the Mandat). kosten.txt puts the cost information inside the Erstberatung. "schriftlich" is not in kosten.txt, and § 3a Abs. 1 RVG requires Textform (ST-31 says so itself). Fix: use the kosten.txt wording, or get the client's yes; write "in Textform".
9. Low, B. FAQ "Darf man dem Betriebsprüfer zum Mittagessen einladen?": "Prüfer der Finanzbehörden können Amtsträger sein (§ 11 Abs. 1 Nr. 2 StGB)." Why: § 11 does not name Prüfer and no claim backs it; the pair is a concrete-conduct question next to the Wein question (flags A3, A4 already). Fix: source it or cut the Prüfer sentence.
10. Low, C. S03: "Fehler passieren." after a list of bribery situations. Why: the client phrase is made for tax mistakes; here it can read as playing down a crime. Fix: drop it on this page.
11. Low, B. Meta: "welche steuerlichen Folgen drohen". Why: fear verb, near LR16. Fix: "möglich sind".
12. Low, C. S07 block 3 has 117 words (minimum 120). OPEN-FLAGS A6 names "möglichst geräuschlos" in S09, but it is not in the text (stale flag).

Scores (0 to 100): intent 80 | depth 78 | GEO-extractability 80 | E-E-A-T 60 | local 45 | technical 85 | schema 55 | internal links 78
Two lowest: local 45: no street address or catchment in the visible text, only "Frankfurt und München" in H1 and two phone lines. Schema 55: schema.jsonld has WebPage, BreadcrumbList and two LegalService nodes, but no FAQPage (7 visible FAQ), no Person, no Service.
Top 3 page-text gaps (additive):
1. S02 has five statute references and no plain definition of "Bestechlichkeit" and "Vorteilsannahme" (2,900 and 320 searches). Add one short definition sentence for each.
2. G6 lists missing terms: Ermittlungen, Maßnahmen, Schutz, Vorwürfe. Add one FAQ "Wie läuft ein Ermittlungsverfahren ab?" (needs saved StPO text) and link to /steuerfahndung-durchsuchung/ and /sonstiges-wirtschaftsstrafrecht/ (the breadcrumb parent is not linked in the body).
3. Add the two office addresses and "Mandate in ganz Deutschland" to S09 (confirmed facts), and add FAQPage and Person schema.

---

## ST-27 Zollstrafrecht: VERDICT FIX FIRST

Correctness gaps
1. High, A. S02: "Werden sie verkürzt, liegt eine Zollhinterziehung nach § 370 AO vor." FAQ: "Zollhinterziehung liegt vor, wenn Einfuhr- oder Ausfuhrabgaben verkürzt werden". Why: § 370 Abs. 1 needs unrichtige oder unvollständige Angaben, or pflichtwidriges In-Unkenntnis-Lassen, and the Tat is a crime only with intent; leichtfertig is an Ordnungswidrigkeit (§ 378). The text reads as strict liability. It copies the live sentence. Fix: add the conduct and the intent, and name § 378.
2. High, A. S07 block 4: "Nach § 382 Abs. 1 AO handelt ordnungswidrig, wer als Pflichtiger Zollvorschriften vorsätzlich oder fahrlässig zuwiderhandelt". Why: the statute limits this to rules that point to this fine rule ("soweit die Zollvorschriften ... auf diese Bußgeldvorschrift verweisen") and also covers "bei der Wahrnehmung der Angelegenheiten eines Pflichtigen". The text is too broad. Fix: add the limit.
3. Med, A. S07 block 1: "Den gleichen Rahmen sieht § 373 Abs. 2 AO vor, wenn jemand ... eine Waffe bei sich führt." Why: Nr. 1 means a Schusswaffe. Nr. 2 means another Waffe or Werkzeug carried to overcome resistance by force. Abs. 2 also covers Bannbruch. Abs. 1 has a minder schwerer Fall (up to five years) that is dropped. Fix: use the statute wording.
4. Low, A. S07 block 1: § 374 "Der Rahmen reicht bis zu fünf Jahren". Why: § 374 Abs. 2 (gewerbsmäßig, Bande) is six months to ten years. Fix: say "in Absatz 1".
5. Low, A. S07 block 2: § 386 Abs. 2 "wenn die Tat ausschließlich eine Steuerstraftat darstellt" (Nr. 2, Kirchensteuer and other levies, dropped); Abs. 3 "Ist ein Haftbefehl erlassen" (statute: also Unterbringungsbefehl). Fix: add both.
6. Med, A. S05: "Auf der Kanzleiseite schreibt sie: „Jedes Mandat und jeder Mandant ist anders.“" Why: the quote is on the Startseite. Fix: "Auf der Startseite".
7. Med, B. FAQ "Kann ich Fehler bei Einfuhr oder Ausfuhr noch korrigieren?": "Möglich." Why: a first-person question answered with "Möglich." reads as a case assessment and invites a Selbstanzeige. Flag A3 says the live page never says this for customs. Fix: "Das hängt vom Einzelfall ab. Ob § 371 AO greift, prüfen wir vor jedem Schritt."
8. Med, A. S06: "vereinbaren ... schriftlich" and "nennen wir Ihnen vor dem Gespräch": unbacked, see ST-25 gap 8.
9. Low, B. FAQ "Droht meinem Unternehmen eine Geldbuße?" Fear verb in a heading. Fix: "Kann meinem Unternehmen eine Geldbuße auferlegt werden?" Also "Unternehmen" for § 30 OWiG (see ST-25 gap 5).
10. Low, C. S07 blocks 2, 3, 4 have 113, 104, 113 words (minimum 120).

Scores (0 to 100): intent 78 | depth 70 | GEO-extractability 80 | E-E-A-T 58 | local 45 | technical 85 | schema 55 | internal links 80
Two lowest: E-E-A-T 58: person block is 47 words, only titles, no link between the credentials and customs work. Local 45: no address or catchment in the visible text.
Top 3 page-text gaps:
1. "zollfahndung" (720) and "bannbruch" (390) get one FAQ each. Add a block on how a Zollfahndung search runs (link ST-18) and examples of banned goods (needs a read source).
2. Depth: Zollkodex and Zollschuld, Verjährung and Bargeld are missing (the writer says no source was read). Read and add one block.
3. Add addresses, "bundesweit" and FAQPage and Person schema; lengthen blocks 2 to 4 to 120 words.

---

## ST-28 Schwarzarbeit und Arbeitsstrafrecht: VERDICT FIX FIRST

Correctness gaps
1. High, A. S07 block 4: "Wer Ausländer zu Arbeitsbedingungen beschäftigt, die in einem auffälligen Missverhältnis ... stehen, wird nach § 10 Abs. 1 SchwarzArbG ... bestraft." Why: § 10 Abs. 1 needs a vorsätzliche Handlung nach § 404 Abs. 2 Nr. 3 SGB III (employment without permit) plus the Missverhältnis. The text drops the first part. Fix: add "ohne die erforderliche Genehmigung" and "vorsätzlich".
2. Med, A. S07 block 2: "Gewerbsmäßiges Handeln oder das Handeln in einer Bande bedroht § 9 SchwarzArbG mit Freiheitsstrafe bis zu fünf Jahren." Why: § 9 Abs. 1 applies only to acts under § 8 Abs. 4 (false Belege). Fix: add "bei den Handlungen nach § 8 Abs. 4".
3. Med, A. FAQ "Wann ist Arbeitnehmerüberlassung unzulässig?" and S07 block 3: "Überlassungshöchstdauer von 18 Monaten". Why: § 1 Abs. 1b AÜG allows other limits by Tarifvertrag and Betriebsvereinbarung (up to 24 months) and counts earlier assignments. Fix: "grundsätzlich 18 Monate; tarifliche Abweichungen sind möglich".
4. Med, A. FAQ "Wer bekommt Ärger bei Schwarzarbeit?": "Ausnahmen gibt es für Gefälligkeit und Nachbarschaftshilfe." Why: § 1 Abs. 4 and § 8 Abs. 6 apply only to services "nicht nachhaltig auf Gewinn gerichtet". S07 has the limit, the FAQ drops it. Fix: add it.
5. Med, B. S07 block 1, § 266a Abs. 6 paragraph. Why: it describes step by step how to get "von einer Bestrafung" absent. That is close to LR10 "Strafe vermeiden" and to advice. The text also writes "innerhalb der bestimmten angemessenen Frist" (statute: von der Einzugsstelle bestimmten) and mixes Satz 1 (court may) with Satz 2 (no punishment). Flag A5 exists. Fix: shorten to a neutral one-line statement of the rule with the Einzugsstelle limit.
6. Med, B. H1 "Verteidigung gegen Strafe und Bußgeld" plus "Welche Folgen Ihnen drohen", "welche Strafen und Bußgelder drohen", "Wer bekommt Ärger". Why: H1 is close to the banned "Strafe vermeiden"; fear and colloquial verbs. Fix: "Verteidigung bei Vorwürfen wegen Schwarzarbeit und Sozialversicherungsbetrug"; "möglich sind".
7. Med, A. S05: "Auf der Kanzleiseite schreibt sie: ..." Quote is on the Startseite (see ST-25 gap 6).
8. Low-Med, B. S05: "ziehen wir bei Bedarf Fachleute aus unserem Netzwerk hinzu." Why: reword of "Experten" (live text); the network is unproven and "Fachleute" keeps the expert claim (§ 7 BORA grey). Fix: cut, or name the proof.
9. Low, A. FAQ "Ist Sozialversicherungsbetrug eine Straftat?": "Das Vorenthalten ... ist nach § 266a StGB strafbar." (no Vorsatz) and "Wer leichtfertig handelt, begeht nach § 8 Abs. 3 SchwarzArbG eine Ordnungswidrigkeit." Why: § 8 Abs. 3 is limited to Arbeitgeber acts under § 266a Abs. 2 Nr. 1 or 2. Fix: add both limits.
10. Low, A/C. S07 block 5: "gehören nach Darstellung der Kanzlei zu den typischen Begleitdelikten" (third person, see ST-25 gap 7) and "Unternehmen" for § 30 OWiG.
11. Low, C. FAQ names Sozialleistungsempfänger, but the brief dropped Sozialbetrug as off-offer (LR15).
12. Med, A. S06 "schriftlich" and "vor dem Gespräch": unbacked (ST-25 gap 8).

Scores (0 to 100): intent 72 | depth 65 | GEO-extractability 78 | E-E-A-T 72 | local 45 | technical 78 | schema 55 | internal links 75
Two lowest: depth 65: "finanzkontrolle schwarzarbeit" (2,400) and "scheinselbständigkeit strafe" (480) have no heading or FAQ; the page has 1,618 words against a competitor median of 1,876. Local 45: no address or catchment in the text.
Top 3 page-text gaps:
1. Add an FAQ "Was ist die Finanzkontrolle Schwarzarbeit?" (currently one bracket in S07) and a block on Scheinselbständigkeit (needs a read source, for example § 7 SGB IV).
2. "schwarzarbeit strafe" (2,900) is answered only inside a closed accordion. Add the three frames (§ 266a: bis fünf Jahre; § 8 SchwarzArbG: bis 50.000 und 100.000 Euro; § 9) as one sentence in S02.
3. Local lines and schema (FAQPage, Person); link /selbstanzeige/ and /steuerfahndung-durchsuchung/; the slug /arbeitsstrafrecht/ carries no keyword (flag B6).

---

## ST-31 Kosten und Honorar: VERDICT FIX FIRST

Correctness gaps
1. High, A/B. S04 (Vier-Augen-Prinzip): "Außerdem hat die Zusammenarbeit von erfahrenen und jüngeren Anwältinnen und Anwälten einen Kostenvorteil". Why: not in kosten.txt (only the live FAQ: "aus Kostengründen sinnvoll"); it is stated as a fact, while the FAQ says "kann ... Kosten sparen". OPEN-FLAGS A3 says the page says "kann"; S04 does not. It is a price promise (UWG). Fix: "kann ... Kosten sparen" or cut; correct the flag.
2. High, A. S07, S08, FAQ 2: "Was Ihre Erstberatung kostet, nennen wir Ihnen vor dem Gespräch.", "Wir sagen Ihnen vor dem Gespräch, was die Erstberatung kostet.", "Konkrete Zahlen besprechen wir vor der Beauftragung mit Ihnen." Why: claim C09 cites approved-copy F1; F1 does not contain these sentences and prints the range itself. kosten.txt puts the cost information inside the Erstberatung; ST-14 says the same. These are new promises. Fix: use "In der Erstberatung informieren wir Sie offen über die voraussichtlichen Kosten eines Mandats" or get the client's yes.
3. Med, A. S02 "schriftlich" and FAQ "im Einzelfall und schriftlich" against S04 "bedarf sie der Textform". Why: internal conflict; "schriftlich" is not in kosten.txt. Fix: "in Textform" everywhere.
4. Med, A. S04 § 3a paragraph: "Sie muss als Vergütungsvereinbarung bezeichnet und von anderen Vereinbarungen deutlich abgesetzt sein". Why: statute says "oder in vergleichbarer Weise bezeichnet" and "mit Ausnahme der Auftragserteilung", and Satz 4 exempts a Gebührenvereinbarung nach § 34. Fix: add the three limits.
5. Med, A. S04 row Pauschale: "wenn sich der Umfang ... vollständig abschätzen lässt oder ein Gutachten das Ziel ist." Why: kosten.txt says "beispielsweise" and "Beratungstätigkeit". The examples became a closed list. Fix: "zum Beispiel".
6. Med, B. S04 and FAQ: "Wir bleiben erreichbar." / "Wir bleiben verlässlich erreichbar." Why: an availability promise. Only the phone window Mo bis Fr 09:30 bis 14:30 is documented, and the answering of calls is not checked in the source of truth. Fix: "erreichbar in den Telefonzeiten und nach Vereinbarung".
7. Low-Med, B. S04: "In unserem Fachgebiet ist es deshalb üblich" and "So sichern wir die fachliche Qualität". Why: "Fachgebiet" is a close cousin of "Spezialgebiet" (§ 7 BORA); "sichern" is a quality guarantee. Fix: "In Wirtschafts- und Steuerstrafsachen"; "kontrollieren wir wichtige Entscheidungen zusätzlich".
8. Med, A. S05 and FAQ 4: "Im Regelfall zahlen Sie die Vergütung nach der Vereinbarung selbst." Why: not in kosten.txt; no source (flag A5 says "Kanzlei bestätigt", which is not a source). Fix: placeholder or cut.
9. Med, C. Title, H1 and meta promise "Anwaltskosten bei Selbstanzeige", but the body says nothing specific to Selbstanzeige. H1 also promises "womit Sie rechnen müssen" while every amount is a placeholder. Fix: add one confirmed sentence on how Selbstanzeige mandates are billed, or remove the promise until amounts exist.
10. Low, C. S08: "Ihre Anwältin ist Dr. Anja Stürzl". Why: the same page says two lawyers work on each Mandat and the rate depends on seniority. Fix: "Die Kanzlei leitet Dr. Anja Stürzl".
11. Low, C. Placeholder text in S04 says "Kundentext und Live-FAQ widersprechen sich". Fine as a placeholder, but it must never reach the CMS.

Client text check (kosten.txt and ki-baustein.txt)
Dropped or changed in meaning:
- Intro "Vertrauenssache ... existenzielle ... Erfahrung, Sorgfalt und Zeit ... Anspruch wollen wir uns messen lassen": dropped. The reason why the work needs time is lost.
- "Auch im laufenden Mandat behalten wir die Kosten im Blick und kommunizieren ... stets offen": weakened to "sprechen weiter mit Ihnen über die Kosten" (monitoring dropped).
- "Mandate sind so unterschiedlich wie die Sachverhalte und Menschen": dropped.
- Pauschale: "beispielsweise" and "Beratungstätigkeit" dropped; examples became a closed list (gap 5).
- Stundensätze (350 bis 500), "regulär", "aktuell": dropped on purpose, placeholder 1. Vorschuss (1.000 bis 5.000): placeholder 2. Erstberatung (250 bis 350): placeholder 3; "üblicherweise" kept only in FAQ 3, dropped in S02 and the table.
- Vier-Augen: "hohe fachliche Qualität ... verlässliche Erreichbarkeit sicher" became "sichern wir die fachliche Qualität" and "Wir bleiben erreichbar"; heading "Mit vereinten Kräften" dropped.
- RVG block: "kaum ein Fall gleicht dem anderen", "individuelle Begleitung" dropped; rest kept.
- "Warum sich die Investition in uns lohnt" with its intro ("Anspruch ist nicht, die günstigste Kanzlei zu sein") and all nine bullets: dropped as a whole. Lost with it: the value argument for the price, and provable proof points (Lehr-, Vortrags- und Veröffentlichungstätigkeit is provable on the live profile; Praxiserfahrung).
- KI block: "modern", "speziell", "erheblich", "gestalten Prozesse effizienter", "permanente Weiterentwicklung", "beispielsweise", "individuelle" (Verteidigungsstrategie), and the closing "stärken wir die Qualität ... wirtschaftlich sinnvoll" dropped. Last sentence ("Wert darauf ... allen datenschutzrechtlichen und berufsständischen Anforderungen gerecht") replaced by placeholder 5. Added: "Das kann Zeit und Kosten sparen" (from the kosten.txt bullet, not from ki-baustein.txt).
Added and not in the client text: "Kostenvorteil" sentence, "schriftlich", the three "vor dem Gespräch" promises, "Im Regelfall zahlen Sie ... selbst", the Stoppuhr sentence (live FAQ, backed by C05), the StPO and RVG statute paragraphs (backed by saved texts).
Amounts in visible text: none (checked page.md, cms-blocks.txt, schema.jsonld). Amounts appear only in placeholders.md.
BRAO risk words: "Spezialisierung" removed; "ausgezeichneter Ruf" removed; "unbedingte Leidenschaft" removed; "bestmöglich" is not in the client texts and not on the page. Also removed: "hochqualifiziert", "besonders hohe", "starkes Netzwerk", "umfassende ... Weiterbildung", "persönliche Erreichbarkeit auch außerhalb der klassischen Bürozeiten". Kept and grey: "Fachgebiet", "sichern wir die fachliche Qualität", "Haftungsrisiko", "erfahrenen" (neutral).
Check on flags: OPEN-FLAGS B1/B4 say the approved Startseite still says "RVG". approved-copy.md F1 (line 155) already says "nicht nach dem RVG" and prints "250 bis 350 Euro" (only line 5 still says RVG). The real conflict is therefore: the Startseite will show the Erstberatung range while /kosten/ and three service pages show a placeholder and "nennen wir Ihnen vor dem Gespräch".

Scores (0 to 100): intent 58 | depth 60 | GEO-extractability 65 | E-E-A-T 62 | local 40 | technical 85 | schema 55 | internal links 65
Two lowest: local 40: no city in H1 or body, only phone labels and one bullet "Büros in Frankfurt und München". Intent 58: the query is "wie viel kostet", and the page gives no figure; the FAQ answer "Wie hoch sind die Kosten" holds none.
Top 3 page-text gaps:
1. No figures: once the client agrees, fill placeholders 1 to 3 as ranges in the table and the answer block (competitors with figures rank for "strafverteidiger kosten", 210 searches; the word "Strafverteidiger" is not on the page).
2. Selbstanzeige: add the confirmed billing facts for Selbstanzeige and Gutachten and link /steuerstrafrecht/gutachten-risikobewertung/ and /selbstanzeige/ from S04.
3. All five internal links sit in one S08 paragraph. Spread them into the body (add /kontakt/ when written), add FAQPage and Person schema, and add the value block back with provable points (Dozentin, Veröffentlichungen from the live profile).

---

## Cross-page problems (batch D and ST-14)

1. Quote misattribution on ST-25, ST-27, ST-28: "Auf der Kanzleiseite schreibt sie". The source is the Startseite.
2. "Was sie kostet, nennen wir Ihnen vor dem Gespräch" on ST-25, 27, 28, 31 is not in approved-copy F1 (cited source) or kosten.txt, and ST-14 does not say it. Decide one promise for all five pages.
3. "schriftlich" (ST-14, 25, 27, 28, 31) against "Textform" (ST-31 S04, § 3a RVG). Use "in Textform" or "in einer Vergütungsvereinbarung".
4. The Startseite F1 prints "250 bis 350 Euro" for the Erstberatung; ST-31 and the service pages hide it behind a placeholder. Publish both together or neither.
5. Three identical S06 cost blocks (ST-25, 27, 28), identical FAQ "Bleibt meine Anfrage vertraulich?" and identical S09 phone text: duplicate-content risk on top of the ">25 %" overlap the writers already met. Vary wording or shorten to a link.
6. "Unternehmen" for § 30 OWiG on ST-25, 27, 28 (statute: juristische Person, Personenvereinigung).
7. Third-person "nach Darstellung der Kanzlei" on ST-25 and ST-28 breaks the wir voice.
8. Credential proof (LR12): all pages state "Fachanwältin für Steuerrecht seit 2021". Claim source is the CV note and the live profile. No Kammer proof is saved, and the source of truth says the anwalt.de profile names "Rechtsanwaltskammer Köln" ("prüfen"). Ask the firm for the Fachanwaltsurkunde before go-live.
9. Fear verbs "drohen", "Ärger", "Droht ..." appear in headings and meta on ST-25, 27, 28.
10. Schema on all four pages: no FAQPage and no Person node, although each page shows 7 to 9 FAQ and a named lawyer.
11. Local signals: no street address in any visible text; only H1 city names and phone lines.
12. ST-31 promises "erreichbar" while the documented phone window is Mo bis Fr 09:30 bis 14:30.
13. Internal links: ST-25 breadcrumb has /sonstiges-wirtschaftsstrafrecht/ but the body never links it; ST-31 mentions a Gutachten-Pauschale without a link to ST-13.
14. Accordion size: ST-27 blocks 2 to 4 and ST-25 block 3 are below 120 words.
