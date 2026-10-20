# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Stürzl, Ordnungswidrigkeiten ST-23)

Lies diese Datei, bevor du an dieser Seite weiterarbeitest. Stand 2026-10-11 (nach Review C, Korrekturrunde). Fragen an die Kanzlei stellen wir erst, wenn sie alles zur Bestätigung bekommt (Martin).

## A. Rechtsgrauzonen (BRAO / UWG), nicht vom Agenten zu entscheiden

| # | Stelle | Frage | Stand |
| --- | --- | --- | --- |
| A1 | S03: "mit langjähriger Erfahrung im Wirtschafts- und Steuerstrafrecht" | Erfahrungsaussage ohne Zahl, aus dem Kundentext. | Steht. Kanzlei bestätigt. |
| A2 | "möglichst geräuschlos" (Wendung der Kanzlei) | Steht auf dieser Seite nicht mehr (S09 neu formuliert). Die Wendung bleibt auf ST-21. | Erledigt hier. |
| A3 | S07 Block 4: Aussage der Live-Seite, Compliance-Maßnahmen "schützen" die Leitungspersonen | Der Satz "Ausreichende Compliance-Maßnahmen können helfen, Leitungspersonen zu schützen" ist gestrichen (Review C Punkt 2). Die Seite sagt nur noch: Ob die Maßnahmen den Anforderungen genügen, hängt vom Sachverhalt ab. | Behoben. |
| A4 | S07 Block 3 und 4, FAQ: gesetzliche Höchstbeträge (zehn Millionen, fünf Millionen, eine Million, verzehnfacht) | Sie stehen sachlich mit Norm und ohne Wertung, jetzt vollständig mit der Verzehnfachung nach § 30 Abs. 2 Satz 3 OWiG. Sie können Angst machen. | Steht. Martin prüft den Ton. |
| A5 | S01 und S07: "leichtfertig" statt "unbeabsichtigt" | Die Live-Seite sagt, auch "unbeabsichtigte Fehler" könnten als Ordnungswidrigkeit geahndet werden. § 378 AO verlangt Leichtfertigkeit. Die Seite folgt dem Gesetz. | Kanzlei bestätigt die Änderung. |
| A6 | S08 Frage "Unterschied": "Vorsatz liegt auch dann vor, wenn jemand den Erfolg einer Tat billigend in Kauf nimmt" | Aus der Live-FAQ (Mythen), ohne gelesene Rechtsprechung. | Steht. Kanzlei bestätigt. |
| A7 | **Live-Seite**: "bestmöglich", "essenziell", "empfindliche Bußgelder", "Expertise", "kompetente" | Mögliche Verstöße gegen § 43b BRAO / UWG und Angst-Ton. Nicht übernommen. | Hinweis an Martin (Un-Burning D11). |
| A8 | **Wortlaut-Regel für die ganze Website**: S07 Block 3 (§ 30 OWiG) und Block 4 (§ 130 OWiG, § 9 OWiG) | Diese Seite führt den geprüften, nahe am Gesetzestext liegenden Wortlaut (gespeichert in `_work/law/`: owig_1968__30, __130, __9, __17, __31, __33). ST-21 und ST-26 übernehmen denselben Satz zu § 130 OWiG. ST-21 übernimmt den Satz zu § 30 Abs. 1. ST-20 verlinkt hierher. Die Seite sagt bewusst nicht, ob ein Geschäftsführer "Inhaber" im Sinne von § 130 OWiG ist. Sie zitiert nur § 9 Abs. 1 OWiG. | Ein Jurist der Kanzlei prüft den Wortlaut einmal. Änderungen dann an allen Seiten gleich. |
| A9 | S08 Frage "Beispiele": Hinweis zum Steuerberater | Der Satz folgt der Live-FAQ (Mythen, Abschnitt V): Man sollte jede Steuererklärung vor der Unterschrift prüfen, sonst kann man sich im Einzelfall (mit) strafbar machen. Quelle ist die Kanzlei, kein Gesetz. Die Seite sagt nicht, dass Blindunterschrift leichtfertig ist. | Kanzlei bestätigt. |
| A10 | S07 Block 1: "Das Gesetz erklärt den Begriff leichtfertig nicht" | Keine Rechtsprechung gelesen und gespeichert. Eine Definition mit Urteil (zum Beispiel BGH) bräuchte eine gelesene Quelle. | Offen. Bei Bedarf Quelle holen. |
| A11 | S07 Block 1: Geldbuße bei "§ 371 Abs. 4 AO gilt entsprechend" | Die Seite nennt den Verweis, erklärt § 371 Abs. 4 AO nicht (Anzeige nach § 153 AO und Dritte). Der Text steht in `_work/law/ao_1977__371.txt`. | Steht. Jurist prüft, ob eine Erklärung nötig ist. |

## B. Widersprüche und Lücken im Kundenmaterial

| # | Punkt | Quellen | Stand |
| --- | --- | --- | --- |
| B1 | Vergütung: Startseite sagt "RVG", neuer Kundentext "kein RVG". Diese Seite folgt dem neuen Text und nennt das RVG nicht. | approved-copy.md gegen kosten.txt | Startseite anpassen. |
| B2 | Erstberatung: drei Fassungen, kein Betrag auf der Seite. Der Platzhalter ist gestrichen (Fixes Nr. 3). Betrag nur auf /kosten/. | kanzlei.txt, faq.txt, kosten.txt | Frage an die Kanzlei bleibt bei ST-31. |
| B3 | Rechtsschutz und Kostenübernahme durch ein Unternehmen: Kostentext schweigt. Der Platzhalter ist gestrichen. | kosten.txt | Frage an die Kanzlei bleibt bei ST-31. |
| B4 | Veröffentlichungsstatus: Das Live-Profil nennt "Kommentierung der §§ 380–383b AO" im Heidelberger Kommentar (3. Auflage, "erscheint 2024"). Die Seite nennt nur den Kommentar zu §§ 379, 380 AO (3. Auflage 2023). | Live-Profil Dr. Stürzl | Kanzlei bestätigt den Erscheinungsstatus der zweiten Kommentierung. |
| B5 | Die zwei Live-Unterseiten (Unternehmensgeldbußen, Geldbußen wegen Organisationsverschulden, ST-22/ST-24) haben keinen Slug in `slugs.json` (ST-22 und ST-24 leer). Die Seite verlinkt sie deshalb nicht. Sie tragen denselben Einleitungstext (Duplikat). | slugs.json, Live-Seiten | Martin ergänzt Slugs. Danach Links in S07 Block 3 und 4 nachtragen. |
| B6 | Zitatquelle: "Jedes Mandat und jeder Mandant ist anders." steht auf der Startseite, nicht auf der Kanzleiseite. Die Seite sagt jetzt "Auf der Startseite". | home.txt | Behoben. |

## C. Hinweise für den Workflow

1. Die Nachfrage liegt bei "organisationsverschulden" (480) und "aufsichtspflichtverletzung" (320). Die Seite deckt beides in S07 Block 4 ab. Eine eigene Seite für Organisationsverschulden (ST-24) wäre der bessere Ort für diese Nachfrage.
2. Keyword-Überschneidung: ST-21 verlinkt auf diese Seite für Organisationsverschulden und führt dafür kein eigenes Keyword.
3. Dr. Gloggers Beitrag zu Aufsichtsmängeln von Vorständen (2017, unter dem Namen Werndl) wäre ein starker Beleg. Er bleibt draußen, bis die Namensfrage geklärt ist (siehe OPEN-FLAGS ST-21 B5).
4. Wortzahl: Die Seite hat etwa 2.100 Wörter und liegt damit über dem Zielbereich (900 bis 1600), weil sie den Wortlaut von § 30 und § 130 OWiG für die ganze Website trägt. Der Seller-Layer bleibt unter 550 Wörtern. Der Wettbewerber-Median liegt bei 1083, die längsten Seiten bei 2.000 bis 3.300 Wörtern.
5. Co-Autoren: Auf allen vier Seiten steht "gemeinsam mit Co-Autoren" ohne Namen (Regel: keine möglichen ehemaligen Kolleginnen und Kollegen nennen). Martin entscheidet, ob Namen aus dem Live-Profil genannt werden.
