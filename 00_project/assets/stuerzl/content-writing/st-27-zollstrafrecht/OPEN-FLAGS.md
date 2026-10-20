# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Stürzl, Zollstrafrecht, ST-27)

Lies diese Datei, bevor du an dieser Seite weiterarbeitest. Stand 2026-10-11, nach der Korrekturrunde (Review D, `../REVIEW-D.md`, Bericht `../FIX-D-report.md`).

## A. Rechtsgrauzonen (BRAO / UWG), nicht vom Agenten zu entscheiden

| # | Stelle im Text | Frage | Aktueller Stand |
| --- | --- | --- | --- |
| A1 | S01, H1 "Anwalt bei Zollhinterziehung, Zollfahndung und Bannbruch" | Kann als Fachgebietsbezeichnung gelesen werden (BORA, Fachanwaltsordnung). | Text steht so. Kanzlei prüft. |
| A2 | (entfällt auf dieser Seite) | Die Wendung "langjährige Praxiserfahrung" steht nicht mehr in S03 dieser Seite. | Erledigt. |
| A3 | S07 Block 4 und FAQ "Kann ich Fehler bei Einfuhr oder Ausfuhr noch korrigieren?" | Aussage, dass § 371 AO bei Zollhinterziehung eine Rolle spielen kann. Sie folgt aus § 3 Abs. 3 und § 369 AO, die Live-Seite sagt es nicht ausdrücklich. Die Antwort lautet jetzt "Das hängt vom Einzelfall ab ... prüfen wir vor jedem Schritt" statt "Möglich" (Review D, Punkt 7). | Kanzlei prüft. |
| A4 | S09: "möglichst geräuschlos" (Wendung der Kanzlei) | Kann als Ergebnisaussage gelesen werden. Durch "möglichst" abgeschwächt. | Steht. Kanzlei prüft. |
| A5 | **Die Live-Seiten selbst** nutzen Wörter, die wir nicht übernehmen: "Expertise", "Experten", "hochspezialisiert", "ganzheitliche Beratung", "Festpreis", "hohe fachliche Spezialisierung" (Kanzleiseite, Arbeitsstrafrecht, Kostentext), dazu Rankings und Peer-Zitate auf der Profilseite. | Möglicher Verstoß der Kanzlei gegen § 43b BRAO / UWG. Martin entscheidet. | Nur im Hinweis, nicht im Text. |
| A6 | S05: "In ihrem Profil führt sie die Kommentierung der §§ 380 bis 383b AO im Heidelberger Kommentar zum Steuerstrafrecht auf, zu der auch § 382 AO gehört." | Das Live-Profil nennt die Kommentierung mit dem Zusatz "3. Auflage, erscheint 2024". Ob sie erschienen ist, ist nicht geprüft. Der Satz sagt deshalb nur, was das Profil aufführt. | Kanzlei bestätigt den Stand der Veröffentlichung. |
| A7 | S08 "Was gilt für Bargeld bei Ein- und Ausreise?" | Gesetzestext § 12a ZollVG gelesen (Anzeigepflicht auf Verlangen, Sicherstellung bis 30 Tage, Verwendung in Steuerstrafverfahren). Die EU-Verordnung 2018/1672 (Anmeldepflicht an der EU-Außengrenze) ist nicht gelesen und nicht erwähnt. Allgemeine Information, keine Fallbeurteilung. | Kanzlei prüft. |
| A8 | S07 Block 4 (Verjährung) | Fünf Jahre nach § 78 Abs. 3 Nr. 4 StGB für § 370 Abs. 1 AO; 15 Jahre nach § 376 Abs. 1 AO nur für die Fälle des § 370 Abs. 3 Satz 2 Nr. 1 bis 6. Die längere Frist für § 373 AO (Höchstmaß zehn Jahre) steht nicht im Text. Beginn und Unterbrechung der Verjährung (§§ 78a, 78c StGB) sind nicht gelesen und nicht erwähnt. | Kanzlei prüft. |

## B. Widersprüche im Kundenmaterial

| # | Widerspruch | Quellen | Stand |
| --- | --- | --- | --- |
| B1 | Vergütung: Kundentext "kein RVG, nach Zeitaufwand". Die freigegebene Startseite sagt in F1 (Zeile 155) schon "nicht nach dem RVG" und "Vergütungsvereinbarung". Nur Zeile 5 (Einwände-Übersicht) nennt noch "RVG oder Vereinbarung", das ist eine interne Notiz. | `approved-copy.md`, `kosten.txt` | **Stand korrigiert (2026-10-11):** Der frühere Hinweis "Startseite sagt noch RVG" ist überholt. Kein Konflikt mehr. |
| B2 | Erstberatung: Live-Kanzleiseite "Festpreis", Live-FAQ andere Sätze, Kundentext "Pauschale". Die freigegebene Startseite druckt die Spanne 250 bis 350 Euro. | `_work/live/kanzlei.txt`, `faq.txt`, `kosten.txt`, `approved-copy.md` F1 | Diese Seite nennt keinen Betrag, nur "üblicherweise eine Pauschale". Der Platzhalter für die Höhe steht auf /kosten/ (ST-31). Startseite und Kostenseite sollen eine Zahl gemeinsam nennen oder beide keine. |
| B3 | Rechtsschutz: Kostentext schweigt. | `kosten.txt` | Platzhalter 5 auf /kosten/ (ST-31). |
| B4 | Die Live-Seite Zollstrafrecht endet mit einer Liste (Steuerordnungswidrigkeiten, § 30 OWiG, § 130 OWiG), die zur Seite Ordnungswidrigkeiten passt. Wahrscheinlich ein Kopierfehler. | `_work/live/zollstrafrecht.txt` | Inhalt in Vertiefung Block 5 übernommen, weil er auch für Unternehmen im Zollverfahren gilt. Kanzlei bestätigt. |
| B5 | Fußzeile der Live-Seite nennt die alte Adresse und die alte Telefonnummer. | `_work/live/zollstrafrecht.txt`, `nap.json` | Neue Seite nennt nur bestätigte Daten. Umstellung wartet auf Martins Go. |

## C. Workflow-Hinweise

1. Links ohne `/index.php/` (wie ST-14). Die Seite hat 8 Textlinks (Obergrenze): /steuerstrafrecht/, /steuerfahndung-durchsuchung/, /selbstanzeige/, /ordnungswidrigkeiten/, /unternehmensvertretung/, /arbeitsstrafrecht/, /dr-anja-stuerzl/, /kosten/.
2. Die Direkt-Antwort zählt der Skript-Zähler wegen "Abs." als mehr als 4 Sätze. Die Antwort hat 4 echte Sätze.
3. Nicht behandelt, weil keine Quelle gelesen: Zollschuld nach dem Zollkodex der Union (nur die Verordnungsnummer aus § 3 Abs. 3 AO steht im Text), Außenwirtschaftsgesetz, Beispiele für verbotene Waren beim Bannbruch (Review D, Lücke 1 und 2). Dafür braucht es gelesene Quellen (EUR-Lex, Einfuhrverbote).
4. Textbausteine sind je Seite verschieden formuliert (Kostenblock S06, S03-Schlusssatz, S04, Vertraulichkeits-FAQ, Abschluss). Der Adressblock in S09 ist nach Beschluss der Korrekturrunde (Punkt 5) auf allen Seiten gleich.
5. Schema: `schema.jsonld` enthält jetzt FAQPage (brief.schema_faq = true). Der Person-Knoten für Dr. Stürzl kommt aus `_work/add_person_schema.py` und muss nach jedem Lauf von `run_gates.py` neu angehängt werden.
6. Der Zielbereich der Wortzahl im Brief (900 bis 1500) wurde auf 900 bis 1900 angehoben, weil das Review mehr Tiefe verlangt (Verjährung, Bargeld, Zollkodex, Länge der Blöcke).
