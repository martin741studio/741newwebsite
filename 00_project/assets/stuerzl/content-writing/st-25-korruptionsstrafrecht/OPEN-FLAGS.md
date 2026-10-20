# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Stürzl, Korruptionsstrafrecht, ST-25)

Lies diese Datei, bevor du an dieser Seite weiterarbeitest. Stand 2026-10-11, nach der Korrekturrunde (Review D, `../REVIEW-D.md`, Bericht `../FIX-D-report.md`). Entscheidung von Martin: Fragen an die Kanzlei stellen wir erst, wenn sie alles zur Bestätigung bekommt.

## A. Rechtsgrauzonen (BRAO / UWG), nicht vom Agenten zu entscheiden

| # | Stelle im Text | Frage | Aktueller Stand |
| --- | --- | --- | --- |
| A1 | S01, H1 "Anwalt bei Bestechung und Vorteilsannahme" | Kann als Fachgebietsbezeichnung gelesen werden (BORA, Fachanwaltsordnung). Gleiche Frage wie A3 bei ST-14. | Text steht so. Kanzlei prüft. |
| A2 | S03: "langjähriger Praxiserfahrung in wirtschafts- und steuerstrafrechtlichen Verfahren" | Wendung der Kanzlei (Kostentext, Kanzleiseite), ohne Zahl, unbelegt. | Steht. Kanzlei bestätigt. |
| A3 | S07 Block 1 und S08 Frage 1: "Eine Wertgrenze nennt der Gesetzestext nicht" | Aussage zum Gesetzestext (§ 299, §§ 331 bis 334 StGB, gelesen 2026-10-11). Sie ist belegt, kann aber als Einladung zu Geschenken missverstanden werden. | Text steht mit Hinweis auf die Umstände des Einzelfalls. Kanzlei prüft. |
| A4 | S08 Frage 2 (Betriebsprüfer, Mittagessen) | Frage kommt aus dem Bestand. Die Antwort nennt nur den Wortlaut von § 11 Abs. 1 Nr. 2 StGB ("wer bei einer Behörde Aufgaben der öffentlichen Verwaltung wahrnimmt, kann Amtsträger sein") und bewertet keinen Fall. Der Satz "Prüfer der Finanzbehörden können Amtsträger sein" ist entfallen, weil § 11 keine Prüfer nennt (Review D, Punkt 9). | Kanzlei prüft. |
| A5 | S05: "Wir beraten auch bei Korruptionsdelikten, die neben einer Steuerhinterziehung auftreten können" | Wendung der Live-Kanzleiseite ("typische Begleitdelikte"), jetzt in Wir-Form statt "nach Darstellung der Kanzlei" (Review D, Punkt 7). | Kanzlei bestätigt. |
| A6 | (entfällt) | Der frühere Flag zu "möglichst geräuschlos" in S09 war überholt: Die Wendung steht nicht im Text dieser Seite. | Erledigt. |
| A7 | **Die Live-Seiten selbst** nutzen Wörter, die wir nicht übernehmen: "Expertise", "Experten", "hochspezialisiert", "Spezialisierung", "ganzheitliche Beratung", "beste Lösung", "Festpreis" (Kanzleiseite); "herausragende fachliche Kompetenz", Peer-Zitate wie "Top-Adresse", Rankings und Auszeichnungen (Profilseite); "Expertise" (Seite Arbeitsstrafrecht, Unternehmensvertretung). | Möglicher Verstoß der Kanzlei gegen § 43b BRAO / UWG. Martin entscheidet, ob und wie die Kanzlei darauf hingewiesen wird. | Nur im Hinweis, nicht im Text. |
| A8 | S08 Frage 7 (Ermittlungsverfahren): StPO-Wortlaut zu § 160, § 170, § 136 | Allgemeine Information mit gespeichertem Gesetzestext (Beschuldigtenrechte, Gang des Ermittlungsverfahrens), keine Handlungsanweisung und keine Fallbeurteilung. | Kanzlei prüft. |

## B. Widersprüche im Kundenmaterial

| # | Widerspruch | Quellen | Stand |
| --- | --- | --- | --- |
| B1 | Vergütung: Kundentext "kein RVG, nach Zeitaufwand". Die freigegebene Startseite sagt in F1 (Zeile 155) schon "nicht nach dem RVG" und "Vergütungsvereinbarung". Nur Zeile 5 (Einwände-Übersicht) nennt noch "RVG oder Vereinbarung", das ist eine interne Notiz. | `cro/04-copy/approved-copy.md`, `kosten.txt` | **Stand korrigiert (2026-10-11):** Der frühere Hinweis "Startseite sagt noch RVG" ist überholt. Kein Konflikt mehr. |
| B2 | Erstberatung: Live-Kanzleiseite "zum Festpreis", Live-FAQ andere Sätze, Kundentext "Pauschale". Die freigegebene Startseite druckt die Spanne 250 bis 350 Euro. | `_work/live/kanzlei.txt`, `faq.txt`, `kosten.txt`, `approved-copy.md` F1 | Diese Seite nennt keinen Betrag und keinen Platzhalter, nur "üblicherweise eine Pauschale". Der Platzhalter für die Höhe steht auf /kosten/ (ST-31). Startseite und Kostenseite sollen eine Zahl gemeinsam nennen oder beide keine. |
| B3 | Rechtsschutz: Kostentext schweigt. | `kosten.txt`, Source of Truth Tab 01 Z46 | Platzhalter 5 auf /kosten/ (ST-31). |
| B4 | Der Bestand der Live-Seite nennt Skandale (CDU-Spendenaffäre, Siemens, DFB) und zitiert Transparency International. | `_work/live/korruptionsstrafrecht.txt` | Nicht übernommen, Quellen nicht gelesen. Kanzlei entscheidet, ob sie zurückkommen. |
| B5 | Der Bestand und die Fußzeile der Live-Seite nennen noch die alte Adresse (Wiesenhüttenstraße 17) und die alte Telefonnummer. Die bestätigten Daten stehen in `nap.json`. | `_work/live/korruptionsstrafrecht.txt`, `nap.json` | Die neue Seite nennt die alte Adresse nie. Umstellung der Live-Seite wartet auf Martins Go. |
| B6 | Titel von Dr. Stürzl stehen auf der Live-Profilseite (Lebenslauf). Kammernachweis liegt nicht vor; das Profil bei anwalt.de nennt "Rechtsanwaltskammer Köln" (prüfen). | `_work/live/dr-anja-stuerzl.txt`, `approved-copy.md` | Vor Livegang die Fachanwaltsurkunde von der Kanzlei erbitten. |

## C. Workflow-Hinweise

1. Links: Die Seite verlinkt mit Pfaden ohne `/index.php/` (wie ST-14): /steuerstrafrecht/, /sonstiges-wirtschaftsstrafrecht/, /selbstanzeige/, /ordnungswidrigkeiten/, /unternehmensvertretung/, /steuerfahndung-durchsuchung/, /dr-anja-stuerzl/, /kosten/. Das sind 8 Textlinks (Obergrenze). Der Link auf /compliance/ ist entfallen, um die Grenze von 8 einzuhalten. Die Pfade der Seiten ST-11, ST-20, ST-21, ST-23, ST-45 sind in der Sitemap noch Live-Pfade mit `/index.php/`. Das ist eine technische Entscheidung (Weiterleitungen).
2. Die Skript-Prüfung G6 kann die Direkt-Antwort wegen "Abs." und "Nr." falsch zählen. Die Antwort hat 4 echte Sätze.
3. Textbausteine sind je Seite verschieden formuliert (Kostenblock S06, S03-Schlusssatz, Vertraulichkeits-FAQ, Abschluss). Der Adressblock in S09 ist nach Beschluss der Korrekturrunde (Punkt 5) auf allen Seiten gleich.
4. Schema: `schema.jsonld` enthält jetzt FAQPage (brief.schema_faq = true). Der Person-Knoten für Dr. Stürzl kommt aus `_work/add_person_schema.py` und muss nach jedem Lauf von `run_gates.py` neu angehängt werden, weil `schema_tool.py make` Person nur auf Personenseiten schreibt. Wunsch an den Skill: Person-Knoten auch auf Leistungsseiten mit Person-Abschnitt.
5. Nicht behandelt: Ermittlungsmaßnahmen im Einzelnen (Durchsuchung, Beschlagnahme) gehören auf die Akutseite ST-18, hier nur Verweis.
