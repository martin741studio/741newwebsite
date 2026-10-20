# BATCH-A-report: Stürzl, Akut und Verteidigung (ST-18, ST-12, ST-19, ST-29)

Datum: 2026-10-11. Alle vier Seiten sind lokal fertig, Freigabe offen (Checkpoint 2 bei Martin). Kein Upload, kein Reviewer-Aufruf, keine Änderung an bestehenden Dateien. Ordner: `content-writing/st-18-steuerfahndung-durchsuchung/`, `st-12-verteidigung-steuerstrafverfahren/`, `st-19-durchsuchungsbegleitung-schulung/`, `st-29-verteidigung-privatpersonen/`. Je Ordner: `05-final/page.md`, `cms-blocks.txt`, `placeholders.md`, `schema.jsonld`, `measure-plan.md`, `04-gates/gates.md`, `OPEN-FLAGS.md`, `_status.md`, `_run.json`.

## Tabelle je Seite

| ID | Seite | Wörter | Bestand | Wettbewerber-Median | G1 | G2 | G3 | G4 | G5 | G6 | Platzhalter | Cleanse-Aufrufe | Kosten USD | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST-18 | Steuerfahndung und Durchsuchung (Akutseite, neu) | 1616 | kein Bestand | 1275 (31 Seiten, 70 % = 892) | pass | pass | pass | pass | pass 5/5 | pass | 2 (Pauschale Erstberatung, Rechtsschutz) | 1 (Änderung abgelehnt) | 0,0900 | fertig, Freigabe offen |
| ST-12 | Verteidigung im Steuerstrafverfahren | 1515 | 276 | 1442,5 (24 Seiten, 70 % = 1009) | pass | pass | pass | pass | pass 5/5 | pass | 2 (Pauschale, Rechtsschutz) | 1 (2 Änderungen abgelehnt) | 0,0935 | fertig, Freigabe offen |
| ST-19 | Durchsuchungsbegleitung und Schulung (Unternehmen) | 1231 | 223 | 1048 (20 Seiten, 70 % = 733) | pass | pass | pass | pass | pass 5/5 | pass | 2 (Schulung Format/Dauer/Abrechnung, Pauschale) | 1 (1 übernommen, 1 abgelehnt) | 0,0970 | fertig, Freigabe offen |
| ST-29 | Verteidigung von Privatpersonen | 1336 | 211 | 1008,5 (22 Seiten, 70 % = 705) | pass | pass | pass | pass | pass 5/5 | pass | 2 (Pauschale, Rechtsschutz) | 1 (2 übernommen) | 0,0955 | fertig, Freigabe offen |

Seller-Layer ohne Vertiefung und FAQ: ST-18 554, ST-12 510, ST-19 483, ST-29 478 Wörter (Regel 550; ST-18 liegt 4 Wörter darüber, weil die Schrittfolge der ersten Stunde der Kern der Akutseite ist). Zählt man die FAQ mit, liegen alle vier über 550. Der Referenzlauf Selbstanzeige liegt dann bei 1057. Siehe Regelvorschlag 3.

G6-Hinweise (nur Hinweise, `seo_coverage.py --fetch`): ST-18 fehlen steuerhinterziehung, steuerberater (Akutseite, nicht gebraucht). ST-12 fehlen betriebsprüfung, strafsachenstelle (kein Gesetzestext im Lauf, Hinweis an die Kanzlei möglich). ST-19: Beschluss, Beamte, Ansprechpartner wurden eingebaut; kopien, maßnahme, ablauf, strafrecht bleiben draußen (kein belegbarer Inhalt). ST-29: § 370 AO und Selbstanzeige: Selbstanzeige ist verlinkt, § 370 steht in ST-12 und im Ratgeber ST-35.

## Was blockiert wurde

Nichts. Alle vier Seiten hatten Pool-Item, Stimmprofil und Daten. Zwei Seiten haben kein Sitetree-Keyword mit Volumen (ST-19, ST-29). Ich habe ein Keyword gewählt und als Entscheidung für Martin gekennzeichnet: ST-19 "durchsuchung im unternehmen" (keine Daten), ST-29 "strafverteidiger steuerstrafrecht" (keine Daten). Für ST-18 hat das Sitetree-Keyword "steuerfahndung anwalt" ebenfalls keine Daten; das Umfeld hat 6.600 ("steuerfahndung").

## Entfernte Platzhalter nach der Korrektur des Koordinators

- ST-18: Platzhalter "Notfallnummern und Zeiten" an drei Stellen (S01, S04 Schritt 2, S09) entfernt. Die Nummern 0160 3396513 und 0160 95945730 stehen als Fakten (Quelle Live-Kontaktseite). Telefonzeiten Mo bis Fr 9:30 bis 14:30 sind in S09 aufgenommen (Claim C32). Besetzungszeiten der Notfallnummern sind nicht dokumentiert: kein "24/7", keine Zeiten im Text, Frage in `OPEN-FLAGS.md` B3.
- ST-19, ST-29, ST-12: In diesen Entwürfen standen von Anfang an Nummern und Zeiten als Fakten, weil die Korrektur kam, bevor ich sie schrieb. Es gab dort keine Adress-, Park- oder Telefonzeit-Platzhalter.
- Adresse Frankfurt (Untermainkai 26) steht in keinem Seitentext (keine Standortseite). In den Claims C03 ist sie als bestätigt geführt (nap.json). Keine alte Adresse genannt.

Bleibende Platzhalter: Pauschale der Erstberatung (ST-18, ST-12, ST-19, ST-29), Rechtsschutzversicherung (ST-18, ST-12, ST-29), Format, Dauer und Abrechnung der Schulung (ST-19).

## Neue Widersprüche im Kundenmaterial

1. Kostenmodell: freigegebene Startseite "nach RVG" gegen Kundentext "kein RVG, nach Zeitaufwand". Die Live-FAQ nennt außerdem "Rechtsanwaltsvergütungsordnung" statt "-gesetz" (Fehler im Live-Text). Alle vier Seiten folgen dem neuen Kundentext, ohne Beträge.
2. Erstberatung: Kanzlei-Seite "Festpreis", Source of Truth Tab 01 "350 Euro fest", Kundentext "Pauschale, üblicherweise 250 bis 350 Euro", Live-FAQ andere Sätze. Vier Fassungen.
3. Notfallnummern: öffentlich, aber ohne Besetzungszeiten. Die Live-Seite ST-19 sagt "24/7", die Kontaktseite nennt keine Zeiten, die Telefonzentrale nur Mo bis Fr 9:30 bis 14:30.
4. Begleitung vor Ort: Live-Seite "Begleitung von Durchsuchungen" gegen Startseiten-Antwort F3 "klären wir im Telefonat". Die Seiten folgen F3.
5. Live-FAQ I.4 nennt "vorbestraft ab mehr als 90 Tagessätzen oder mehr als 3 Monaten" und Nebenfolgen (Waffenverbot, Passentzug). Ohne Gesetzestext im Lauf nicht übernommen (ST-12 OPEN-FLAGS B4).
6. Live-FAQ und Individualpersonen-Seite sagen, dass ein Einstellungsverfahren nach § 153a StPO nicht "vorbestraft" macht. Auch dazu liegt kein Gesetzestext im Lauf (BZRG). Aussage ist als Kanzleiaussage geflaggt (ST-12 A2).
7. ST-19: Schulungsinhalt, Format, Dauer und Preis stehen nirgends. Die Seite gibt nur die Live-Aussagen wieder.
8. Das Batch-Dokument `content-writing-stuerzl-batch.md` sagt noch, die Adresse Frankfurt sei nicht endgültig und die Notfallnummern seien nicht freigegeben. Der Koordinator hat das korrigiert. Die Datei selbst ist noch alt (nicht von mir geändert).

## Vorschläge für Regeln im Skill

1. `check_legal.py` (BRAO, "Superlativ / Marktführer"): Das Muster `nr\.? ?1` schlägt bei jedem Gesetzeszitat "Nr. 1" an. Ich habe "Nummer 1" geschrieben (so schreibt es auch das Gesetz). Vorschlag: das Muster nur bei "Nr. 1" ohne vorangehendes "Abs." oder "Satz" oder "§" auslösen.
2. `check_style.py` (verbotene Wörter): Der Abgleich prüft nur den Wortanfang. Ein Eintrag wie "beste" würde "besteht" sperren. Ich habe "beste" bewusst nicht in `forbidden_words` des Briefs geführt (G2 prüft es mit Wortgrenze). Vorschlag: im Skill vermerken oder auf ganze Wörter prüfen.
3. 550-Wörter-Regel (Seller-Layer): Die Anweisung nennt S01 bis S06 und S08 bis S09, also mit FAQ. Der Referenzlauf erfüllt das nicht (1057). Vorschlag: Regel eindeutig machen (ohne FAQ) und `validate_page.py` prüft sie mit Warnung.
4. G6 H5 (Keyword-Stuffing) nutzt 5-Buchstaben-Präfixe. Beim Keyword "steuerstrafverfahren" zählt jede Überschrift mit "Steuer..." (Steuerhinterziehung, Steuererklärung, Steuerberater) als Treffer. Ich musste fünf Überschriften umschreiben. Vorschlag: ganze Wortstämme des Keywords prüfen oder für Ein-Wort-Keywords die Schwelle auf die vollen Wortformen legen.
5. G4 "Sprecher gemischt: ich/wir" schlägt bei FAQ-Fragen in Ich-Form (PAA, zum Beispiel "Muss ich aussagen?") und bei Zitaten an. Vorschlag: Überschriften und Zitate ausnehmen.
6. Cleanse: Der Cleanse erzeugt oft Satzfragmente zur Rhythmus-Streuung ("Auch außerhalb der Hauptverhandlung.", "Und was in welcher Abteilung liegt.") und streicht Absicherungen ("gegebenenfalls"). In `prompts/cleanse-de.txt` aufnehmen: keine Fragmente, keine Absicherungen streichen, Gesetzeswortlaut nicht lockern. Vier von sieben Vorschlägen musste ich ablehnen.
7. `scratchpad`: Parallele Agenten teilen sich ein Scratchpad. Mein Hilfsmodul `brief_common.py` wurde von einem anderen Agenten überschrieben. Vorschlag: im Batch-Dokument je Agent einen Unterordner im Scratchpad vorschreiben.
8. `page-templates.md`: Für Akutseiten fehlt eine Vorlage. Ich habe die Servicevorlage genutzt und S04 (Schrittfolge) als "erste Stunde" ausgebaut, den Notfallstreifen in S01 gelegt. Vorschlag: Variante "Akutseite" mit S00 Notfallstreifen und S04 als Kern in die Vorlagen aufnehmen.

## Rechtsgrauzonen (vollständig in den `OPEN-FLAGS.md` je Seite)

- Verhaltensempfehlungen (Schweigerecht, "zuerst mit einem Verteidiger sprechen", "nichts vernichten") sind allgemein gehalten, stammen aus der Live-FAQ und sind mit § 136 Abs. 1 StPO belegt (ST-18 A1, A2; ST-29 A6).
- "Gelten nicht als vorbestraft" nach Einstellung (ST-12 A2): keine Norm im Lauf.
- "Darf nicht als Schuldeingeständnis gewertet werden" (ST-18 A3): Live-FAQ ohne Rechtsprechungsbeleg.
- § 103 StPO auf nicht verdächtige Unternehmen angewandt (ST-19 A1): übliche Auslegung, nicht im Gesetzestext.
- Das Wort "Strafverteidiger" in H1 und Title (ST-29 A1).
- "hartnäckig" als Wort der Kanzlei (ST-29 A3).
- Wörter der Live-Seiten, die nicht übernommen sind und die Kanzlei selbst nutzt: Spezialisierung, hochspezialisiert, Expertise, Experten, fachliche Exzellenz, hart in der Sache, Festpreis, bestmögliche Beratung, bestmögliche Lösung, Straffreiheit (H1 Selbstanzeige-Seite), unermüdlich kämpfen, "nicht in Panik verfallen". Entscheidung bei Martin (Un-Burning D11).

## Rechtsquellen (gespeichert in `_work/laws/` je Seite, gelesen 2026-10-11)

StPO §§ 52, 55, 68b, 94, 98, 102, 103, 105, 106, 107, 110, 111e, 112, 117, 136, 137, 140, 147, 152, 153a, 158, 161a, 163a, 170, 312, 407, 410; AO §§ 208, 370, 371, 377, 378, 386, 393, 397, 400, 404; OWiG §§ 67, 130; StGB §§ 73, 164, 203; BRAO § 43a. Jede Norm im Text steht im Claim-Verzeichnis `01-brief/claims.json` mit Quelle. Keine Urteile, keine Literatur zitiert.

## Kosten und Aufrufe

DataForSEO gesamt 0,3760 USD (je Seite 0,09 bis 0,097, ein Volumenaufruf je Seite, dazu 5 SERP-Aufrufe zu 0,0035 und 0,002 USD). Cleanse: 4 Aufrufe (1 je Seite). Keine weiteren Kosten.
