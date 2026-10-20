# Batch D: Begleitdelikte und Kosten (Stürzl, Content Writing, 2026-10-11)

Seiten: ST-25, ST-27, ST-28, ST-31. Alle lokal, kein Upload, kein CMS. Reviewer-Schritt nicht gelaufen (Hauptagent). Ordner: `content-writing/st-25-korruptionsstrafrecht/`, `st-27-zollstrafrecht/`, `st-28-schwarzarbeit-arbeitsstrafrecht/`, `st-31-kosten/`. Je Ordner: `05-final/page.md`, `cms-blocks.txt`, `placeholders.md`, `schema.jsonld`, `measure-plan.md`, `04-gates/gates.md`, `OPEN-FLAGS.md`, `_run.json`.

## Ergebnis je Seite

| ID | Seite | Wörter (Seite) | Bestand | Wettbewerber-Median (70 %) | G1 | G2 | G3 | G4 | G5 | G6 | Platzhalter | Cleanse-Aufrufe | Kosten USD | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST-25 | Korruptionsstrafrecht | 1.476 | 227 | 1.181 (826), 11 Seiten | pass | pass | pass | pass | 5/5 | pass | 0 | 2 | 0,099 | fertig, Freigabe offen |
| ST-27 | Zollstrafrecht | 1.320 | 147 | 742 (519), 15 Seiten | pass | pass | pass | pass | 5/5 | pass | 0 | 2 | 0,094 | fertig, Freigabe offen |
| ST-28 | Schwarzarbeit, Sozialversicherung, Arbeitnehmerüberlassung | 1.552 | 148 | 1.877 (1.313), 14 Seiten | pass | pass | pass | pass | 5/5 | pass | 0 | 2 | 0,097 | fertig, Freigabe offen |
| ST-31 | Kosten und Honorar (neu, mit KI-Abschnitt) | 1.272 | keiner (Seite neu, FAQ-Kostenteil als Quelle) | 744 (521), 17 Kostenseiten | pass | pass | pass | pass | 5/5 | pass | 5 | 1 | 0,097 | fertig, Freigabe offen |

Seller-Layer (S01 bis S06, S09, ohne FAQ und Vertiefung): ST-25 527, ST-27 465, ST-28 483 Wörter (Vorgabe höchstens 550). ST-31 ist Typ D und hat keinen Seller-Layer. Vertiefung: ST-25 4 Blöcke (606 Wörter), ST-27 4 Blöcke (545), ST-28 5 Blöcke (762). FAQ: 7, 7, 7 und 9 Fragen.
G6 (seo_coverage, schema_tool, link_network) lief mit. Die vier Seiten bestehen den Link- und Ähnlichkeitstest zusammen (nach Kürzung des Kostenblocks, siehe unten). Hinweis-Meldungen von G6 (Begriffe, Normen) sind in `04-gates/gates.md` und wurden geprüft; relevante Lücken sind geschlossen (zum Beispiel § 374 AO, § 299a StGB, "Finanzkontrolle Schwarzarbeit", Compliance-Verweis).
Nachfrage- und SERP-Daten: DataForSEO je Seite 0,09 bis 0,10 USD (Volumen, 2 bis 3 SERP-Abrufe), unter dem Limit von 1 USD. Gesetzestexte (gesetze-im-internet.de) liegen je Seite in `_work/`.

## Was blockiert wurde

Nichts. Keine Seite stoppte am A0-Gate. Die Lücken im Pool wurden im Lauf selbst gefüllt:
1. ST-25 hatte keine Nachfragedaten und kein Keyword (`keywords: []`). Volumen, 2 SERPs und Autocomplete wurden erhoben (Primär-Keyword "korruptionsstrafrecht", 30; Cluster "bestechlichkeit" 2.900, "vorteilsannahme" 320).
2. ST-27, ST-28, ST-31: Pool hatte kein SERP-Set zum Keyword. SERP und Wettbewerber-Messung wurden ergänzt.
Nicht geschrieben, weil keine Quelle gelesen wurde: Zollkodex der Union (Zollschuld), ZollVG, Außenwirtschaftsrecht, Arbeitszeitgesetz, steuerliche Absetzbarkeit der Anwaltskosten (PAA, als "nicht rechtssicher" verworfen), Skandal-Beispiele und TI-Definition aus dem Bestand von ST-25.

## Korrektur des Hauptagenten (Adresse, Zeiten, Notfallnummern)

Die Datei `nap.json` und `source-of-truth-2026-10-11.md` wurden gelesen. Auf meinen vier Seiten gab es **keinen Platzhalter** zu Adresse, Parken, Telefonzeiten oder Notfallnummern, deshalb wurde keiner entfernt. Neu aufgenommen: die bestätigten Telefonzeiten (Mo bis Fr 09:30 bis 14:30 Uhr, Termine auch außerhalb nach Vereinbarung) im Abschluss-Abschnitt jeder Seite (Claim C30, Quelle Live-Kontaktseite und Source of Truth Tab 02 Zeile 38). Adressen stehen nicht auf den Leistungsseiten (Standort-Seiten ST-41, ST-42). Notfallnummern: nicht verwendet (gehören zur Akutseite ST-18). Schema nutzt die bestätigten Stammdaten aus `nap.json` ohne Öffnungszeiten. Aus `OPEN-FLAGS.md` und `placeholders.md` wurde nichts zu Adresse entfernt, weil dort nichts stand; B5 (alte Adresse auf der Live-Seite) bleibt als Hinweis.

## Neue Widersprüche im Kundenmaterial

1. Stundensätze: Kundentext EUR 350 bis 500 nach Seniorität, Live-FAQ 380 bis 450 / 330 bis 400 / 280 bis 350 nach Funktion, Source of Truth früher 350 bis 450. Beide Fassungen dürfen nicht gleichzeitig live sein (Platzhalter 1 auf ST-31).
2. Erstberatung: Kundentext Pauschale EUR 250 bis 350, Live-Kanzleiseite "zum Festpreis", Source of Truth früher "350 € fest" (Platzhalter 3).
3. Die freigegebene Startseite sagt an vier Stellen "RVG", der neue Kundentext "kein RVG".
4. Live-FAQ: "Gibt es auch Pauschalen?" und "Kriege ich eine Kostenschätzung?" haben denselben Antworttext. Live-FAQ sagt "24/7-Erreichbarkeit", die Kontaktseite Telefonzeiten 09:30 bis 14:30.
5. Die Live-Seite Zollstrafrecht endet mit einer Liste (Steuerordnungswidrigkeiten, § 30 OWiG, § 130 OWiG), die zur Seite Ordnungswidrigkeiten gehört. Wahrscheinlich ein Kopierfehler.
6. Der Bestand "Arbeitsstrafrecht" hat Satz- und Tippfehler ("Wir bringen haben ...", "Abreitszeitschutzgesetz") und das Wort "Experten aus unserem Netzwerk".
7. Der Kundentext Kosten enthält interne Notizen ("Ziel: Wir sprechen über's Geld ...") und Fehler im Preisformat. Nicht übernommen.
8. Fußzeilen aller Live-Seiten nennen noch Wiesenhüttenstraße 17 und die alte Telefonnummer.

## Rechtsgrauzonen (Details je Seite in `OPEN-FLAGS.md`)

1. **ST-31 KI-Abschnitt:** Die Zusage "allen datenschutzrechtlichen und berufsständischen Anforderungen gerecht" steht nicht im Text, sondern als Platzhalter 5. Rechtsrahmen: § 43a Abs. 2 BRAO, § 43e BRAO (Dienstleister, Textform-Vertrag, Auslandsregel, Einwilligung bei mandatsbezogenen Diensten), § 203 StGB, DSGVO. Entscheidung: Kanzlei und ihre Datenschutzberatung.
2. "Anwalt für ..." in den H1 (Fachgebietsbezeichnung), "langjährige Praxiserfahrung" (unbelegt), "möglichst geräuschlos" (Ergebnisnähe), "Netzwerk" statt "Experten" (ST-28).
3. ST-25: "Eine Wertgrenze nennt der Gesetzestext nicht" (belegt durch §§ 299, 331 bis 334 StGB, kann aber missverstanden werden). Fragen zu Wein und Betriebsprüfer stammen aus dem Bestand, die Antworten nennen nur Gesetz und Umstände.
4. ST-27 und ST-28: Aussage, dass § 371 AO bei Zollhinterziehung eine Rolle spielen kann (folgt aus § 3 Abs. 3, § 369 AO; Live-Seite sagt es nicht). § 266a Abs. 6 StGB (Absehen von Strafe) bedingt formuliert.
5. ST-31: "Das kann Zeit und Kosten sparen" (KI, Vier-Augen-Prinzip) ist eine Preisaussage im weiteren Sinn (UWG). Steht mit "kann".
6. Die Live-Seiten nutzen selbst Wörter, die wir nicht übernehmen ("Expertise", "Experten", "hochspezialisiert", "ganzheitliche Beratung", "Festpreis", "exzellenter Ruf", "unglaubliche Leidenschaft", Peer-Zitate und Rankings auf der Profilseite). Möglicher Verstoß gegen § 43b BRAO / UWG. Martin entscheidet über den Hinweis an die Kanzlei.

## Vorschläge für den Skill

1. `legal-terms.json` (BRAO block): Das Muster `nr\.? ?1` blockiert "Abs. 1 Nr. 1" in Norm-Zitaten. Vorschlag: Treffer nach "Abs." oder "§" ausnehmen. Ich schreibe jetzt "Nummer 1".
2. `seo_coverage.py` (Antwortblock): Der Satzzähler trennt an "Abs." und zählt 5 oder 6 Sätze bei Antworten mit Normzitat. Vorschlag: Abkürzungen (Abs., Nr., Satz, §) vor dem Trennen ausnehmen.
3. `deslop_de.py`: Die Dreier-Regel trifft auch Behördenlisten ("Zoll, Staatsanwaltschaft und Finanzamt") und Verfahrensbeteiligte. Das zwingt zu "sowie"-Umbauten. Vorschlag: nur dann zählen, wenn alle drei Glieder Adjektive oder Abstrakta sind, oder Schwelle auf 4.
4. `link_network.py` hat gezeigt: Ein gleicher Kostenblock auf jeder Leistungsseite erzeugt 29 bis 34 % Ähnlichkeit. Regel für den Skill: Kostenblock auf Leistungsseiten höchstens 50 Wörter, Einzelheiten nur auf /kosten/. (In ST-14 steht noch der lange Block.)
5. Template "Kostenseite" in `page-templates.md` um einen optionalen Abschnitt "Technik/KI" und einen "Gesetzliche Vorgaben für die Vergütungsvereinbarung (§ 3a RVG)" erweitern.
6. Die Prüfregel für das Wortlimit 550 (Seller-Layer) fehlt im Skript. Vorschlag: `validate_page.py` zählt S01 bis S06 und S09 (ohne FAQ und Accordion).
7. Vor dem Packen ein gemeinsames Hilfsskript für `placeholders.md`, `cms-blocks` und `_run.json` (mehrere Agenten schrieben Hilfsskripte in dasselbe Scratchpad und überschrieben einander; ich habe meine in `scratchpad/batchD/` abgelegt).

## Entscheidungen für Martin

1. Beträge (Stundensatz, Vorschuss, Erstberatung) erst nach Bestätigung der Kanzlei. Reihenfolge beim Livegang: erst `/kosten/`, dann Kostenteil der FAQ kürzen und verlinken.
2. KI-Datenschutz-Satz: bleibt draußen, bis Nachweis vorliegt.
3. Kostenblock auf den Leistungsseiten ist jetzt kurz (50 Wörter) und ohne Platzhalter. ST-14 hat noch den langen Block mit zwei Platzhaltern: anpassen oder so lassen.
4. Slug von ST-28: Live-Pfad `/arbeitsstrafrecht/` trägt kein Suchwort. Umbenennung nur mit Weiterleitung und Go.
5. Bestand-Skandale und TI-Zitat (ST-25): zurückholen, wenn ein Agent die Quellen liest?
