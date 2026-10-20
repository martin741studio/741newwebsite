# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Stürzl, Steuerfahndung und Durchsuchung, ST-18)

Lies diese Datei, bevor du an dieser Seite weiterarbeitest. Stand nach der Korrekturrunde 2026-10-11 (Review REVIEW-A). Die Vorversion des Textes liegt in `05-final/page-vorreview.md`. Fragen an die Kanzlei stellen wir erst, wenn sie alles zur Bestätigung bekommt (Entscheidung Martin).

## A. Rechtsgrauzonen (BRAO / UWG), nicht vom Agenten zu entscheiden

| # | Stelle im Text | Frage | Aktueller Stand |
| --- | --- | --- | --- |
| A1 | S04 Schritt 3: "Wir raten grundsätzlich, davon zunächst Gebrauch zu machen" (Schweigerecht) | Verhaltensempfehlung der Kanzlei aus der Live-FAQ, gestützt auf § 136 Abs. 1 StPO und mit dem Hinweis "Diese Hinweise sind allgemein gehalten". Der Satz "Rufen Sie uns an, bevor Sie sich äußern" (S02) ist gestrichen. | Text steht so. Kanzlei prüft. |
| A2 | S04 Schritt 5 | Der Hinweis "Vernichten oder verändern Sie nichts" ist gestrichen (keine Norm im Lauf, Einzelfallanweisung). Schritt 5 nennt jetzt nur § 94 Abs. 2 StPO und verweist auf das Gespräch mit einem Verteidiger. Wenn die Kanzlei den Hinweis wiederhaben will, braucht er eine Norm (zum Beispiel aus dem StGB). | Gestrichen. Kanzlei entscheidet. |
| A3 | früher S07 Block 4 und FAQ: "Die Ausübung des Schweigerechts darf nicht als Schuldeingeständnis gewertet werden" | Aussage der Live-FAQ ohne Gesetzestext im Lauf. Beleg wäre Rechtsprechung (BGH). | **Gestrichen** (Review Punkt 6). Kanzlei kann eine Fundstelle nennen, dann wieder aufnehmen. |
| A4 | S07 Block 5 und FAQ "Selbstanzeige nach Durchsuchung" | Der Text folgt jetzt dem Wortlaut von § 371 Abs. 2 Satz 1 Nr. 1 Buchst. d AO (unverjährte Steuerstraftaten, vor Berichtigung, Ergänzung oder Nachholung). Das Gesetz schreibt "Straffreiheit tritt nicht ein". Das Wort steht auf der Verbotsliste, daher schreibt die Seite "Strafbefreiung", wie die freigegebene Seite ST-14. | **Martin entscheidet**, ob "Strafbefreiung" bleibt oder der Gesetzeswortlaut "Straffreiheit" in diesem verneinenden Satz erlaubt wird. |
| A5 | S07 Block 1: "Steuerpolizei" | Umgangssprachliches Bild aus der Live-FAQ ("quasi die Steuerpolizei"), juristisch ungenau. Das Bild "Staatsanwaltschaft des Finanzamts" ist **gestrichen**. Statt dessen steht § 399 Abs. 1 AO (die Finanzbehörde nimmt die Rechte und Pflichten der Staatsanwaltschaft wahr). | "Steuerpolizei" bleibt mit "Man kann sie sich vorstellen". Kanzlei prüft. |
| A6 | **Die Live-Seite selbst** nutzt Wörter, die wir nicht übernehmen: "Spezialisierung", "hochspezialisiert", "Expertise", "Experten", "fachliche Exzellenz", "hart in der Sache", "Festpreis", "bestmögliche Beratung", "Straffreiheit" (H1 Selbstanzeige-Seite), "unermüdlich kämpfen". | Möglicher Verstoß der Kanzlei gegen § 43b BRAO / UWG. Martin entscheidet, ob und wie die Kanzlei darauf hingewiesen wird. | Nur im Hinweis, nicht im Text. |
| A7 | S01, S04 Schritt 2, FAQ 1, S09: Reihenfolge Telefon, dann Klärung der Anwesenheit | Neu festgelegt für diese Korrekturrunde: Die Kanzlei berät zuerst am Telefon und klärt danach, ob eine Anwesenheit vor Ort möglich ist. Kein Versprechen einer Begleitung in H1, Title, Meta und Hero. Die Live-Seite sagt "Begleitung von Durchsuchungen". | Text folgt der Vorgabe. Die Kanzlei bestätigt, dass die Formulierung stimmt. Gleiche Linie auf ST-19. |

## B. Widersprüche im Kundenmaterial, die vor Livegang gelöst sein müssen

| # | Widerspruch | Quellen | Stand |
| --- | --- | --- | --- |
| B1 | Vergütung: freigegebene Startseite "nach RVG", neuer Kundentext "kein RVG, nach Zeitaufwand". | `cro/04-copy/approved-copy.md` gegen `client-texte/kosten.txt` | Diese Seite folgt dem neuen Kundentext, ohne Beträge, mit den Abschwächungen "grundsätzlich" und "üblicherweise". Startseite anpassen. |
| B2 | Erstberatung: Kanzlei-Seite "zum Festpreis", Live-FAQ andere Sätze, Kundentext "Pauschale, üblicherweise 250 bis 350 Euro". | `kanzlei.txt`, Live-FAQ, `kosten.txt` | Der Platzhalter für den Betrag ist auf dieser Seite gestrichen (Entscheidung Fix-Auftrag Punkt 3). Der Betrag steht nur auf /kosten/ (ST-31). |
| B3 | Notfallnummern: öffentlich auf der Live-Kontaktseite, Besetzungszeiten nirgends dokumentiert. Die Kanzlei-Seite sagt "bei Bedarf 24/7-Erreichbarkeit". | Live-Kontaktseite, Live-Kanzlei-Seite | Nummern stehen im Text. Die Seite nennt keine Besetzungszeiten und kein "24/7". Frage an die Kanzlei: Zu welchen Zeiten nimmt jemand ab? |
| B4 | Begleitung vor Ort: Live-Seite "Begleitung von Durchsuchungen", Startseiten-Antwort F3 "klären wir im Telefonat". | Live-Seite Verteidigung im Steuerstrafverfahren; approved-copy.md F3 | Gelöst durch Vorgabe, siehe A7. |
| B5 | Telefonzeiten: Live und Source of Truth Mo bis Fr 9:30 bis 14:30, Google 9 bis 18. | Source of Truth Tab 02, Google-Profile | Seite nutzt 09:30 bis 14:30 (nap.json). Keine Zeiten im Schema. |

## C. Workflow-Hinweise

1. Cleanse (codex) in der Korrekturrunde: siehe `03-draft/cleanse-notes-fix.txt` und `_status.md`.
2. Link-Ziele ST-11, ST-12, ST-14, ST-19, ST-29, ST-31, ST-45 stehen im Sitetree mit den Slugs aus `assets/stuerzl/slugs.json`. Sie sind erst gültig, wenn die Zielseiten live sind.
3. Schema ohne FAQPage (G6-Regel). Beide Büros stehen mit Straße und PLZ im Markup (nap.json bestätigt). Person und Service kommen aus `_work/add-schema.py`; der Skill kann beides nicht selbst erzeugen (Wunsch für den Skill: Service-Knoten für page_type service, Person auf Dienstleistungsseiten).
4. Nicht verwendet: "steuerfahndung hessen" (140) und "steuerfahndung münchen" (210) als Text. Es gibt keinen belegten lokalen Fakt zu Hessen. Beide Büroorte stehen im Adressblock.
5. Die Live-FAQ enthält die Passagen I.3 (Durchsuchungsbeschluss) und V (Schweigerecht). Sie sind in S07 und S08 aufgegangen. Der Satz zum Schuldeingeständnis ist gestrichen, siehe A3.
