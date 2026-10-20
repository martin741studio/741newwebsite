# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Stürzl, Schwarzarbeit / Arbeitsstrafrecht, ST-28)

Lies diese Datei, bevor du an dieser Seite weiterarbeitest. Stand 2026-10-11, nach der Korrekturrunde (Review D, `../REVIEW-D.md`, Bericht `../FIX-D-report.md`).

## A. Rechtsgrauzonen (BRAO / UWG), nicht vom Agenten zu entscheiden

| # | Stelle im Text | Frage | Aktueller Stand |
| --- | --- | --- | --- |
| A1 | S01, H1 "Strafe, Bußgeld und Verteidigung" | Der frühere H1 "Verteidigung gegen Strafe und Bußgeld" stand nahe an "Strafe vermeiden" (LR10) und ist ersetzt. "Strafe" bleibt als Suchwort (2.900) und als sachliche Angabe. | Steht. Kanzlei prüft. |
| A2 | (entfällt auf dieser Seite) | Die Wendung "langjährige Praxiserfahrung" steht nicht mehr in S03 dieser Seite. | Erledigt. |
| A3 | (erledigt) S05: Satz zum Netzwerk ("Fachleute aus unserem Netzwerk") | War eine Umformulierung von "Experten aus unserem Netzwerk" (Bestand), das Netzwerk ist unbelegt. Der Satz ist gestrichen (Review D, Punkt 8). | Erledigt. |
| A4 | S05: Urteilsanmerkung zu § 266a StGB (juris PraxisReport StrafR 03/2020) | Steht auf der Live-Profilseite (Urteilsanmerkungen). Heft und Anmerkung nicht selbst geprüft. | Kanzlei bestätigt. |
| A5 | S07 Block 1: § 266a Abs. 6 StGB (Absehen von Bestrafung) | Der Absatz steht jetzt als neutrale Wiedergabe der Regel (Gericht kann absehen; schriftliche Mitteilung an die Einzugsstelle; Frist, die die Einzugsstelle bestimmt). Die Schritt-für-Schritt-Anleitung ist entfallen (Review D, Punkt 5). "Hängt vom Einzelfall ab" steht dabei. | Kanzlei prüft. |
| A6 | (entfällt) | "Möglichst geräuschlos" steht nicht im Text dieser Seite. | Erledigt. |
| A7 | **Die Live-Seiten selbst** nutzen Wörter, die wir nicht übernehmen: "Expertise", "Experten" (Seite Arbeitsstrafrecht: "Wir ... haben die notwendige Expertise und Erfahrung"), "hochspezialisiert", "ganzheitliche Beratung", "Festpreis" (Kanzleiseite), dazu Rankings und Peer-Zitate auf der Profilseite. | Möglicher Verstoß der Kanzlei gegen § 43b BRAO / UWG. Martin entscheidet. | Nur im Hinweis, nicht im Text. |
| A8 | S07 Block 4: § 10 Abs. 1 SchwarzArbG | Der Text gibt den Wortlaut wieder (vorsätzliche Handlung nach § 404 Abs. 2 Nr. 3 SGB III und auffälliges Missverhältnis). Die Klammer "also einen Ausländer ohne die erforderliche Genehmigung beschäftigt" fasst § 404 Abs. 2 Nr. 3 SGB III zusammen (gelesen, `_work/sgb_3__404.txt`). | Kanzlei prüft. |
| A9 | S08 "Was ist Scheinselbständigkeit?" | Der Begriff steht nicht im Gesetz. Die Antwort nennt nur § 7 Abs. 1 SGB IV (gelesen) und sagt "hängt vom Einzelfall ab". Eine Definition von "Scheinselbständigkeit" aus Rechtsprechung oder Statusfeststellung (§ 7a SGB IV) ist nicht gelesen. | Kanzlei prüft. |

## B. Widersprüche im Kundenmaterial

| # | Widerspruch | Quellen | Stand |
| --- | --- | --- | --- |
| B1 | Vergütung: Kundentext "kein RVG, nach Zeitaufwand". Die freigegebene Startseite sagt in F1 (Zeile 155) schon "nicht nach dem RVG" und "Vergütungsvereinbarung". Nur Zeile 5 (Einwände-Übersicht) nennt noch "RVG oder Vereinbarung", das ist eine interne Notiz. | `approved-copy.md`, `kosten.txt` | **Stand korrigiert (2026-10-11):** Der frühere Hinweis "Startseite sagt noch RVG" ist überholt. Kein Konflikt mehr. |
| B2 | Erstberatung: Live-Kanzleiseite "Festpreis", Live-FAQ andere Sätze, Kundentext "Pauschale". Die freigegebene Startseite druckt die Spanne 250 bis 350 Euro. | `_work/live/kanzlei.txt`, `faq.txt`, `kosten.txt`, `approved-copy.md` F1 | Diese Seite nennt keinen Betrag, nur "üblicherweise gegen Pauschale". Der Platzhalter für die Höhe steht auf /kosten/ (ST-31). Startseite und Kostenseite sollen eine Zahl gemeinsam nennen oder beide keine. |
| B3 | Rechtsschutz: Kostentext schweigt. | `kosten.txt` | Platzhalter 5 auf /kosten/ (ST-31). |
| B4 | Live-Seite: Tippfehler "Abreitszeitschutzgesetz" und Satzfehler "Wir bringen haben ...". Die Seite nennt das Arbeitszeitgesetz nicht, weil kein Gesetzestext gelesen wurde. | `_work/live/arbeitsstrafrecht.txt` | Kanzlei entscheidet, ob das Arbeitszeitgesetz bleibt. Dann Text holen. |
| B5 | Fußzeile der Live-Seite nennt die alte Adresse und die alte Telefonnummer. | `_work/live/arbeitsstrafrecht.txt`, `nap.json` | Neue Seite nennt nur bestätigte Daten. Umstellung wartet auf Martins Go. |
| B6 | Seitentitel: Sitetree verlangt Suchwörter statt "Arbeitsstrafrecht". Der Live-Slug `/arbeitsstrafrecht/` trägt kein Suchwort. | Sitetree ST-28 | Slug bleibt, bis Weiterleitung und Go vorliegen. |
| B7 | Sozialleistungsbetrug (Empfänger von Sozialleistungen, § 1 Abs. 2 SchwarzArbG) gehört laut Brief (LR15) nicht zum Angebot. | `brief.json` (PAA "Was zählt als Sozialbetrug?" verworfen) | Die Nennung der Sozialleistungsempfänger ist aus FAQ und Vertiefung entfernt (Review D, Punkt 11). |

## C. Workflow-Hinweise

1. Links ohne `/index.php/` (wie ST-14). Die Seite hat 8 Textlinks (Obergrenze): /steuerstrafrecht/, /zollstrafrecht/, /unternehmensvertretung/, /ordnungswidrigkeiten/, /selbstanzeige/, /steuerfahndung-durchsuchung/, /dr-anja-stuerzl/, /kosten/.
2. Das Skript `check_legal.py` blockiert "Nr. 1" als Superlativ in manchen Fällen; der Text benutzt "Nummer 1" im AÜG-Absatz. Vorschlag für den Skill: Regex auf "Nr. 1" nach "Abs." ausnehmen.
3. PAA "Wer bekommt Ärger bei Schwarzarbeit?" ist im Brief auf "verworfen, Duplikat" gesetzt, weil die FAQ-Überschrift das Angstwort "Ärger" nicht mehr trägt. Die Frage ist als "Wer kann bei Schwarzarbeit betroffen sein?" beantwortet.
4. Nicht behandelt: Arbeitszeitgesetz, Statusfeststellung nach § 7a SGB IV, Verjährung (gehört in einen Ratgeber-Beitrag).
5. Textbausteine sind je Seite verschieden formuliert (Kostenblock S06, S03-Schlusssatz, S04, Vertraulichkeits-FAQ, Abschluss). Der Adressblock in S09 ist nach Beschluss der Korrekturrunde (Punkt 5) auf allen Seiten gleich.
6. Schema: `schema.jsonld` enthält jetzt FAQPage (brief.schema_faq = true). Der Person-Knoten für Dr. Stürzl kommt aus `_work/add_person_schema.py` und muss nach jedem Lauf von `run_gates.py` neu angehängt werden.
