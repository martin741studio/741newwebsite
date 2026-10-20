# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Stürzl, Verteidigung von Privatpersonen, ST-29)

Lies diese Datei, bevor du an dieser Seite weiterarbeitest. Stand nach der Korrekturrunde 2026-10-11 (Review REVIEW-A). Die Vorversion des Textes liegt in `05-final/page-vorreview.md`. Fragen an die Kanzlei stellen wir erst, wenn sie alles zur Bestätigung bekommt (Entscheidung Martin).

## A. Rechtsgrauzonen (BRAO / UWG), nicht vom Agenten zu entscheiden

| # | Stelle im Text | Frage | Aktueller Stand |
| --- | --- | --- | --- |
| A1 | H1 und Title | "Strafverteidiger" ist **entfernt** (Dr. Stürzl ist Fachanwältin für Steuerrecht, nicht für Strafrecht). H1 jetzt "Verteidigung im Steuerstrafrecht für Privatpersonen". Das Keyword "strafverteidiger steuerstrafrecht" (ohne Volumen) ist durch "verteidigung im steuerstrafrecht" ersetzt. Das Zitat von Dr. Stürzl in S05 nennt weiter das Wort "Strafverteidigung" (Wortlaut der Startseite). | Erledigt. Kanzlei prüft das Zitat. |
| A2 | S05: Zitat Dr. Stürzl "Effektive Strafverteidigung ist nicht zwingend laut und konfrontativ ..." | Wörtlich von der **Live-Startseite** (Box Dr. Anja Stürzl), nicht von der Kanzleiseite. Die Zitate stehen dort neben "fachliche Exzellenz" und "niemals aufzugeben"; diese Teile sind nicht übernommen. | Text steht so. |
| A3 | früher S04/S02: "hartnäckig", "schnell beenden, auch mit einem Kompromiss", "egal wie lange es dauert" | **Gestrichen.** Ersetzt durch "Wir vertreten Ihre Interessen" und "Wir besprechen mit Ihnen, was Sie erreichen möchten und welche Wege das Verfahren bietet". | Erledigt. |
| A4 | früher S07 Block 2: "Aus einem Zeugen kann schnell ein Beschuldigter werden. Manchmal versucht man auch, eine Person bewusst im Zeugenstatus zu halten" | Live-Aussage ohne Beleg, Unterstellung gegenüber Behörden. | **Gestrichen.** Statt dessen stehen §§ 52, 55, 68b, 136, 161a, 163 StPO. |
| A5 | früher S07 Block 3: "Im Unternehmenskontext ist den Behörden Fehlverhalten oft noch nicht bekannt" und "Das gilt nicht bei Antragsdelikten" | "oft" ohne Quelle. | **Gestrichen** bzw. durch den Wortlaut von § 152 Abs. 2 StPO ("soweit nicht gesetzlich ein anderes bestimmt ist") ersetzt. |
| A6 | FAQ "Was ist zu tun, wenn ein Steuerstrafverfahren eingeleitet wurde?": "Wir raten grundsätzlich, zuerst mit einem Verteidiger zu sprechen" | Allgemeine Verhaltensempfehlung (Live-FAQ), mit "Was im Einzelfall richtig ist, klären wir mit Ihnen". | Text steht so. Kanzlei prüft. |
| A7 | **Die Live-Seite selbst** nutzt "bestmögliche Lösung", "umfassend und hartnäckig", "Worst Case". | "Bestmöglich" ist ein Superlativ (§ 43b BRAO / UWG). Martin entscheidet, ob und wie die Kanzlei darauf hingewiesen wird. | Nur im Hinweis, nicht im Text. |
| A8 | S07 Block 1: "Im Alltag spricht man meist von einer Vorladung." | Sprachhinweis zur Ladung nach § 163a Abs. 3 StPO, damit "Vorladung beschuldigter" (Suchbegriff) im Text steht. Keine Norm nennt das Wort. | Text steht so. |

## B. Widersprüche im Kundenmaterial, die vor Livegang gelöst sein müssen

| # | Widerspruch | Quellen | Stand |
| --- | --- | --- | --- |
| B1 | Vergütung: freigegebene Startseite "nach RVG", neuer Kundentext "kein RVG, nach Zeitaufwand". | `approved-copy.md` gegen `kosten.txt` | Diese Seite folgt dem neuen Kundentext, ohne Beträge, mit "grundsätzlich" und "üblicherweise". |
| B2 | Erstberatung: Kanzlei-Seite "Festpreis", Kundentext "Pauschale 250 bis 350 Euro". | `kanzlei.txt`, `kosten.txt` | Der Platzhalter für den Betrag ist gestrichen (Fix-Auftrag Punkt 3). Der Betrag steht nur auf /kosten/ (ST-31). |
| B3 | Rechtsschutzversicherung: Kostentext schweigt; Zeugenbeistand ebenfalls ohne Aussage. | `kosten.txt` | Platzhalter 1 bleibt (S08). |
| B4 | Kosten eines Zeugenbeistands: Die Kanzlei nennt keine eigene Regelung (PAA aus der SERP). Die Antwort verweist auf die Vergütungsvereinbarung. | Pool, `kosten.txt` | Offen. Kanzlei klärt, ob für Zeugenbeistand gleiche Regeln gelten. |
| B5 | Die Live-Seite führt unter "Strafverfahren" Durchsuchungen, Sicherstellung, Untersuchungshaft, Hauptverhandlung, Vermögensarrest als Themen, aber ohne Text. | Live-Seite | Texte stammen aus Gesetz. Vermögensarrest ist jetzt mit § 111e Abs. 1, 2 und 4 StPO ausgebaut. |

## C. Workflow-Hinweise

1. Cleanse (codex) in der Korrekturrunde: Der Aufruf ist am Nutzungslimit von codex gescheitert (siehe `03-draft/cleanse-notes-fix.txt`). Es gibt keine Cleanse-Fassung. Lint G5 ist 5/5. Ein Cleanse nach dem Limit-Ende (17:20 Uhr laut Fehlermeldung) bleibt möglich; dann `diff_claims.py diff` prüfen.
2. Kein Sitetree-Keyword, kein belegtes Volumen: Keyword "verteidigung im steuerstrafrecht" ist eine Entscheidung des Agenten auf Anweisung des Reviews. `brief.word_range` oben auf 1750 erhöht (Vorladung/Beschuldigtenvernehmung und Vermögensarrest).
3. Die drei Live-Unterseiten (ST-30: Zeugenbegleitung, Strafanzeige, Ordnungswidrigkeiten) bleiben. Ihre Inhalte sind in S07 zusammengefasst. Verlinken, sobald die neuen Pfade feststehen.
4. Link-Ziele ST-12, ST-14, ST-18, ST-19, ST-21, ST-23, ST-31, ST-45 sind erst gültig, wenn die Zielseiten live sind.
5. Person und Service im Schema kommen aus `_work/add-schema.py`, nach jedem Lauf von `run_gates.py` neu starten.
