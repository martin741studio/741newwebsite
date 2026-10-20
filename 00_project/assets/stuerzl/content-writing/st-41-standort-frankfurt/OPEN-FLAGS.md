# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Stürzl, Standort Frankfurt, ST-41)

Lies diese Datei, bevor du an dieser Seite arbeitest. Stand 2026-10-11, nach der Korrekturrunde (REVIEW-F). Fragen an die Kanzlei stellen wir erst, wenn sie alles zur Bestätigung bekommt (Entscheidung von Martin).

## A. Rechtsgrauzonen (BRAO / UWG), nicht vom Agenten zu entscheiden

| # | Stelle im Text | Frage | Aktueller Stand |
| --- | --- | --- | --- |
| A1 | S01, H1: „Anwalt für Steuerstrafrecht“ | Kann als Fachgebietsbezeichnung gelesen werden (BORA, FAO). Es ist das Zielkeyword der Seite. | Text steht so. Kanzlei prüft. |
| A2 | S03: „Sie müssen dafür nicht in Frankfurt wohnen“ | Folgerung aus „Mandate in ganz Deutschland“, kein Satz der Kanzlei. | Text steht so. Kanzlei bestätigt. |
| A3 | S07: „Steuerpolizei“, „Staatsanwaltschaft des Finanzamts“ | Umgangssprachliche Bilder aus der Live-FAQ der Kanzlei. Die Seite erklärt die Rechtslage daneben mit § 399 Abs. 1 AO. | Text steht so, in Anführungszeichen. |
| A4 | S07: „Am Telefon besprechen wir mit Ihnen das weitere Vorgehen. Eine Begleitung vor Ort hängt vom Einzelfall ab und wird im Telefonat geklärt.“ | Wortlaut aus dem Startseiten-Brief (F3), dort Entwurf, Abgleich mit der Akutseite offen. | Text steht so. Kanzlei prüft. |
| A5 | S02, S06: Dezember 2023 als Gründung der Kanzlei in Frankfurt | Der Live-Lebenslauf schreibt „12/2023 Gründung von STÜRZL Steuerstrafrecht (Frankfurt/München)“, die Source of Truth „Frankfurt seit Dez. 2023“. | Text sagt nur Frankfurt. |
| A6 | **Die Live-Seiten selbst** nutzen Wörter, die wir nicht übernehmen: „Spezialisierung“, „Expertise“, „hart in der Sache“, „Festpreis“, „24/7“. Das Live-Profil von Dr. Stürzl nennt Rankings und Auszeichnungen (Handelsblatt, JUVE, WirtschaftsWoche). | Möglicher Verstoß gegen § 43b BRAO / UWG. Martin entscheidet. | Nur im Hinweis, nicht im Text. |
| A7 | S04: „Unsere Leistungen“ | Neutrale Liste mit den sechs Bereichen der freigegebenen Startseite, gleich auf ST-40, ST-41, ST-42. Die Kanzlei hat nicht gesagt, was welches Büro anbietet. „Begleitung vor Ort im Einzelfall“ ist ein Hedge (REVIEW-F ST-41 Punkt 4). | **Frage an die Kanzlei: Was bietet das Frankfurter Büro an?** Bis zur Antwort bleibt die Liste neutral. |
| A8 | S03: Aufbau der Zuständigkeit | §§ 386 Abs. 1 bis 3, 399 Abs. 1 und 388 Abs. 1 AO stehen nach dem gespeicherten Gesetzestext. Absatz 2 ist zusammengefasst („zugleich bestimmte andere Strafgesetze verletzt“, mit Verweis auf den Absatz). Der Satz zu § 388 Abs. 1 ist länger als 28 Wörter, weil er den Gesetzestext mit „zur Zeit der Einleitung des Strafverfahrens“ vollständig wiedergibt. | Text steht so. Keine Umformulierung des Gesetzes. |
| A9 | S07: Kosten | Eigene Wörter, kein Betrag: „grundsätzlich nach Zeitaufwand, in Einheiten von sechs Minuten“, „üblicherweise eine Pauschale“, Information zu den voraussichtlichen Kosten (Quelle `kosten.txt`, Fixes §2.3). | Text steht so. Kanzlei prüft. |
| A10 | Personen | Nur Dr. Stürzl steht im Frankfurter Büro. Thorben Hoppe ist entfernt: sein Live-Profil (ab 06/2026) nennt beide Städte, aber `nap.json`, Live-Kontaktseite und Source of Truth nennen ihn nicht als Ansprechperson (Entscheidung Hauptagent). Weitere Personen im Frankfurter Büro sind offen. | Frage an die Kanzlei, kein Platzhalter im Text. |

## B. Widersprüche und Lücken im Kundenmaterial

| # | Widerspruch | Quellen | Stand |
| --- | --- | --- | --- |
| B1 | Anschrift: Die Seite nennt Untermainkai 26 (bestätigt). Google-Profil, anwalt.de, Live-Website, Schema nennen noch Wiesenhüttenstraße 17. | Source of Truth Tab 00, `nap.json` | Umstellung wartet auf Martins Go. Nicht vorher livegehen. |
| B2 | Zwei Hauseingänge: Die Seite nennt „Post und Empfang: Wilhelm-Leuschner-Straße 23“. Welcher Eingang für Besucher gilt, ist nicht belegt. Die Platznummern 148 und 146 stehen nicht mehr im Text: die Source of Truth sagt nicht, dass es Besucherplätze sind. | Source of Truth Tab 02 Zeile 'Anzahl Profile und Adressen' | Frage an die Kanzlei. |
| B3 | Keine ÖPNV-Anfahrt zur neuen Anschrift belegt. Das Finanzamt-Verzeichnis nennt nur den Weg vom Hauptbahnhof zum Finanzamt, nicht zur Kanzlei. | Live-Kontaktseite (alte Anschrift) | Nicht im Text. Kanzlei liefert die Anfahrt. |
| B4 | Zeiten: Live und Source of Truth Montag bis Freitag durchgehend 9:30 bis 14:30 Uhr (Telefon). Google 9:00 bis 18:00 Uhr. | Live, Google | Seite folgt Live. Keine Zeit im Schema. |
| B5 | Leistungen, Fachgebiete und weitere Personen im Frankfurter Büro: nicht belegt (Pool CP-LOC-004 `needs_client`). | Pool | Fragen, siehe `placeholders.md`. Kein sichtbarer Platzhalter mehr. |
| B6 | Vergütung: Startseite „RVG“ gegen Kostentext „kein RVG“. Diese Seite nennt keinen Betrag. | `approved-copy.md`, `kosten.txt` | **Startseite muss angepasst werden.** |
| B7 | Lokaler Fakt (neu): Finanzamt Frankfurt am Main, Gutleutstraße 118 bis 124, 60327 Frankfurt am Main, vom Hauptbahnhof (Ausgang Süd) ca. 5 Minuten zu Fuß. Quelle: Verzeichnis finanzamt.hessen.de/Frankfurt, gelesen 2026-10-11 (`_work/finanzamt-frankfurt-verzeichnis.txt`). Das Verzeichnis nennt **keine** Steuerfahndung und keine Bußgeld- und Strafsachenstelle an dieser Anschrift. Das Finanzamt hat laut Verzeichnis zwei Verwaltungsstellen (Frankfurt, Frankfurt-Höchst), deshalb sagt die Seite „seine Anschrift“. | finanzamt.hessen.de | Jährlich prüfen. „Rechtsstand dieser Seite: Oktober 2026“ steht im Text. |
| B8 | Namensabweichung: Die Datenschutzhinweise der Steuerfahndungs- sowie Bußgeld- und Strafsachenstellen und das Stadtportal frankfurt.de nennen „Finanzamt Frankfurt am Main I“, das Verzeichnis der Finanzverwaltung nur „Frankfurt am Main“. Die frühere Aussage „bei sechs Finanzämtern“ ist gestrichen (Datenschutzhinweis, kein Verzeichnis). | `_work/hessen-steuerfahndung-quelle.txt`, `_work/finanzamt-frankfurt-verzeichnis.txt` | Die Datenschutzhinweise stehen nur noch in der FAQ, für den Satz zur Steuerfahndung („Nach den Datenschutzhinweisen …“). |
| B9 | Das Zielkeyword „anwalt steuerstrafrecht frankfurt“ hat keinen Suchvolumen-Datensatz (wenig Daten, nicht keine Nachfrage). Nachfrage im Cluster: „steuerfahndung hessen“ 140, „steuerfahndung frankfurt“ 50. | `03-demand/volume.json` | Hinweis. |
| B10 | Einzugsgebiet: Die Kanzlei sagt „deutschlandweit, keine feste regionale Grenze“; direkte Frankfurter Mandate „2–3“ (Source of Truth Tab 09 Z12, Tab 02 Z22). Der 5-km-Radius um Untermainkai 26 und die Liste der Stadtteile (Gutleutviertel, Gallus, Innenstadt, Nordend, Bornheim, Ostend) sind Martins Maps-Arbeitspriorität, keine Aussage der Kanzlei. Die Seite nennt deshalb keine Stadtteile. | Source of Truth | Offen: Entscheidung Martin, ob Stadtteile genannt werden. |
| B11 | Kein Frankfurter Gericht und keine Staatsanwaltschaft als lokaler Fakt: Dafür fehlen gelesene Quellen (Gerichtsverzeichnis, § 391 AO). | – | Offen, optionale Ergänzung. |

## C. Workflow-Hinweise

1. G6-Hinweis „strafre*“: Die Wettbewerber nutzen das Wort „Strafrecht“ in Überschriften. Die Seite nutzt Zusammensetzungen (Steuerstrafrecht, Wirtschaftsstrafrecht). Keine Änderung nötig.
2. Link-Pfade nach `assets/stuerzl/slugs.json`, ohne `/index.php/`.
3. Fotos: nur echte Bilder des Büros und der Personen. Neue Fotos zur neuen Anschrift laufen laut Source of Truth in etwa 2 Monaten ein.
4. Nicht kopieren: Die Münchner Seite (ST-42) hat eigenen Text. Beide teilen die neutrale Leistungsliste und den Adressblock (Fixes §2.5).
5. Schema: `schema_tool.py make` liefert beide Büros mit richtiger Anschrift, aber keinen eigenen Knoten je Büro. Gewünschte Änderung steht in FIX-F-report.md.
