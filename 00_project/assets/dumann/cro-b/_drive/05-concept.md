# Konzept und Storyboard (B4) — Daniela Dumann, Startseite, Track B

Stand 2026-10-11. Grundlage: Martins Stimmen (`00-element-pool/votes-martin-2026-10-11.json`), `02-data/elements-catalog.md`, Brief B. Nur Elemente mit "ja" sind eingebaut. Elemente ohne Stimme und "nein" fehlen.

## Signature-Idee (ein Satz)
**Der Viriditas-Faden:** Eine einzige Pflanzenranke in Lila-Linie wächst beim Scrollen langsam die Seite hinab und verbindet alle Sektionen. "Viriditas" ist Hildegards Wort für die Grünkraft der Schöpfung und der Name von Danielas Schule, deshalb erzählt die eine Bewegung die Marke, ohne ein Wort zu versprechen.

## Komponenten (höchstens 4, alle optional, Seite funktioniert ohne sie)
| # | Komponente | Elemente | Grund |
| --- | --- | --- | --- |
| 1 | Viriditas-Faden (Ranke wächst beim Scrollen, `stroke-dashoffset`) | E01 | Markenidee, führt den Blick nach unten zum Button |
| 2 | Leistungsliste mit Bild-Vorschau (nummerierte Zeilen, beim Überfahren erscheint ein Bild) | E18, E20 | zeigt acht Dinge auf einem Blick, spart Fläche, jede Zeile ist ein Link |
| 3 | Haftender Titel mit Schrittlinie (Sektion 5) | E21 | macht den Ablauf in vier Schritten greifbar |
| 4 | Farbblock-Wechsel beim Scrollen (Hintergrund wechselt Creme zu Lila beim Abschluss) | E30 | Ruhe, führt zum dunklen Abschlussband |

Zusätzlich ohne eigene Komponentenzählung: Hildegard-Siegel in Kopf und Fuß (E03), Wellen-Unterstreichung (E05), Farbwort in Lila kursiv (E07), Bogen-Portrait (E09, E22), Schreibschrift-Akzent B (E11), Atmen-Button nur Hero und Abschluss (E12), Zahlen mit Linie (E13), Themen-Karten mit Blob (E17), Bogen-Bildkarte (E19), Erbe-Zitatband (E24), Randnotiz (E25), FAQ mit Geisterwort und Plus-Zeilen (E27), Adress- und Zeitentabelle (E28), dunkles Abschlussband mit Wellenkante (E29), ruhiges Einblenden einmal (E04).

## Storyboard: je Sektion eine Bewegung
| # | Sektion | Das eine, was sich bewegt | Aufgabe für den Besucher | Auslöser | Reduced Motion |
| --- | --- | --- | --- | --- | --- |
| 0 | Seite | Viriditas-Faden wächst | verbindet die Sektionen, führt nach unten | Scroll | Faden komplett sichtbar, still |
| 1 | Hero | Wellenlinie unter "Hildegard-Heilkunde" zeichnet sich einmal; Button atmet | zeigt den Punkt der Seite, Blick zum Button | Laden | Linie sichtbar, Button still |
| 2 | Beweis-Leiste | Linie unter den Zahlen zeichnet sich | vier belegte Fakten | Sichtbar werden | Linie sichtbar |
| 3 | Fünf Themen | Blob-Plaketten blenden gestaffelt ein | Wiedererkennung | Sichtbar werden | nur Einblenden 300 ms |
| 4 | Leistungen | Bild-Vorschau beim Überfahren der Zeile | Überblick, Neugier | Hover | erstes Bild fest sichtbar |
| 5 | Erster Termin | Titel haftet, Schrittlinie füllt sich | Schwelle senken | Scroll | Linie sichtbar |
| 6 | Über Daniela | Foto in Bogenform, Farbplatte versetzt; Zitatband blendet einmal ein | Person und Herkunft der Idee | Sichtbar werden | still |
| 7 | Bewertungen | Sterne füllen sich links nach rechts | Vertrauen | Sichtbar werden | gefüllt |
| 8 | FAQ | Plus dreht zum Kreuz, Antwort öffnet | Einwände | Klick | schneller |
| 9 | Standort | Randnotizen blenden ein | Anfahrt verstehen | Sichtbar werden | still |
| 10 | Abschluss | Hintergrund wechselt zu Lila, Wellenkante, Button atmet | ein Schritt: Termin | Scroll | fester Farbwechsel, Button still |

Keine-Bewegung-Zonen (Brief): Preise, Hinweisbox, Zitate von Patientinnen, Formular- und Buchungslinks.

## HWG und Grenzen
- Das Pflanzenmotiv ist ein Symbol, kein Versprechen. Keine Zahl und kein Zitat trägt ein Ergebnis.
- Die Pflicht-Hinweisbox (Hildegard-Heilkunde schulmedizinisch nicht allgemein anerkannt) steht in Sektion 4 und im Fuß, ruhig und lesbar, ohne Bewegung.
- Das Bach-Zitat der Live-Seite entfällt (Heilung im Fremdzitat).

## Das Hildegard-Zitat (von Martin: "online suchen")
Quelle: Hildegard von Bingen, *Symphonia armonie celestium revelationum*, Responsorium "O nobilissima viriditas" (Handschriften Dendermonde 165r-v und Riesenkodex 471rb-va, Text auch in *Scivias* III.13.7b). Edition: Barbara Newman, *Symphonia*, Cornell University Press 1988/1998, S. 218. Gefunden und geprüft auf `hildegard-society.org/2017/04/o-nobilissima-viriditas-responsory.html` (lateinischer Text und englische Übersetzung von Nathaniel M. Campbell) und `lieder.net` (TextId 552419).
- Latein (nur der Anfang): "O nobilissima viriditas, quae radicas in sole"
- Deutsch (eigene Übersetzung, vor Live-Gang von der Kundin zu prüfen): "O edelste Grünkraft, die du in der Sonne wurzelst"
- Kontext: Im Original geht es um Jungfrauen, die Zeile ist ein Naturbild und trägt keine Aussage zu Heilung. Eine Aussage zur Gesundheit wurde absichtlich nicht gewählt (HWG).
- Quellenzeile im Zitatband: "Hildegard von Bingen, Symphonia, Responsorium O nobilissima viriditas"

## Signature als Code
Ein SVG-Pfad (Ranke mit Blättern) läuft als `position:absolute` Ebene am rechten Rand des Textblocks. `stroke-dashoffset` folgt dem Scroll-Anteil (0 bis 1). Reiner Code, kein Video. Ausnahme zur Motion-Spec (keine reine `transform`/`opacity`-Bewegung) steht in `motion.md`. Der Faden liegt hinter dem Text und blockiert keine Klicks (`pointer-events:none`).
