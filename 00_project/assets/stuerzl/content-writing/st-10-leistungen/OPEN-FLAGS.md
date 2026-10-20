# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Stürzl, Leistungen ST-10)

Lies diese Datei, bevor du an dieser Seite weiterarbeitest. Stand 2026-10-11, nach der Korrekturrunde (REVIEW-B, `content-writing-stuerzl-fixes.md`). Die Vorversion steht in `05-final/page-vorreview.md`.

## A. Rechtsgrauzonen (BRAO / UWG)

| # | Stelle im Text | Frage | Aktueller Stand |
| --- | --- | --- | --- |
| A1 | S01, H1 "Leistungen: Steuerstrafrecht und Wirtschaftsstrafrecht" | Nennt Rechtsgebiete, keine Titel wie "Spezialist". Kann als Fachgebietsangabe gelesen werden. | Text steht so. Kanzlei prüft. |
| A2 | S02: früher "Unser Fokus liegt auf dem Steuerstrafrecht" | "Fokus" ist ein Synonym für "Schwerpunkt" und braucht Beleg (LR12). Der Satz lautet jetzt "Wir beraten und verteidigen im Steuerstrafrecht und in angrenzenden Gebieten des Wirtschaftsstrafrechts." | Erledigt. |
| A3 | S02: Titel von Dr. Stürzl | Aus Lebenslauf, nicht aus Kammernachweis. | Kanzlei bestätigt. |
| A4 | **Die Live-Seite selbst** schreibt "umfassender Fachkompetenz", "garantieren wir Ihnen eine Beratung auf höchstem Niveau", "höchsten Niveau" | Ergebnisgarantie und Superlativ, § 43b BRAO / UWG. | Nicht übernommen. Martin entscheidet über den Hinweis an die Kanzlei. |

## B. Widersprüche und offene Entscheidungen

| # | Punkt | Quellen | Stand |
| --- | --- | --- | --- |
| B1 | Vergütung: Startseite "RVG oder Vereinbarung", Kundentext "kein RVG". Die FAQ-Antwort folgt dem Kundentext. | `approved-copy.md`, `kosten.txt` | Keine Beträge. |
| B2 | Erstberatung "gegen Pauschale": Live-Kanzleiseite "Festpreis". Betrag nicht genannt. | `kanzlei.txt`, `kosten.txt` | Kein Platzhalter nötig. Die Seite verweist für die Erstberatung auf /kosten/. |
| B3 | Kannibalisierung: Das Sitetree gibt "anwalt steuerstrafrecht" an ST-00, ST-10 und ST-11. Der Hub nimmt "leistungen steuerstrafrecht". | `sitetree.json` | Martin entscheidet. |
| B4 | Karte "Unternehmensvertretung" verlinkt /compliance/ (ST-26, geschrieben, in slugs.json). Die freigegebene Startseite hat noch keine Compliance-Karte. | `approved-copy.md`, `compliance.txt` | Link bleibt. Martin entscheidet, ob Compliance eine eigene (siebte) Karte bekommt. |
| B5 | Pool CP-SVC-001: 6 statt 9 Kacheln. Ordnungswidrigkeiten, Zoll, Arbeits- und Korruptionsstrafrecht, Wirtschaftsstrafrecht erscheinen als Unterlinks in den Karten. | `pool.json` | Keine Streichung von Seiten. Die Reihenfolge der Karten folgt der freigegebenen Startseite. |
| B6 | Der Hub verlinkt mehr als 8 Seiten im Text (Hub-Charakter). | `link_network.py` | Absicht. Karte 1 verlinkt jetzt auch /steuerstrafrecht/verteidigung-im-steuerstrafverfahren/ (ST-12). |
| B7 | Die neue URL /leistungen/ ersetzt /index.php/leistungen und den toten Link /index.php/schwerpunkte. Weiterleitung nötig, nicht live ändern (Page-Swap-Regel). | `slugs.json` | Offen für den Livegang. |
| B8 | Vorschläge aus REVIEW-B: ItemList-Schema für die sechs Bereiche, Prüfzeile mit Dr. Stürzl. | REVIEW-B, `schema_tool.py` | Nicht umgesetzt: `schema_tool.py` erzeugt kein ItemList. Wunsch an den Skill. Eingehende Links (nur 3) entstehen auf den anderen Seiten, nicht hier. |
