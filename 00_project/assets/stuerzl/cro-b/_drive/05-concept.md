# Konzept und Storyboard (B4) — STÜRZL Startseite, Variante B (Track B)

Stand 2026-10-11. Grundlage: Martins Stimmen in Pool 1 und Pool 2 (`00-element-pool/votes-*.json`, `votes-summary-pool2.md`), `02-data/elements-catalog.md`, Brief B. Nur Elemente mit "ja" und "vielleicht" sind eingebaut, nichts mit "nein". Ohne eigene Stimme, aber begründet: Notfall-Streifen, Haarlinien-Köpfe mit Mikro-Labels, Diskretions-Haken-Sektion und "drei Wege" im Abschluss (aus Variante A) und Reveal an jedem Block (E05). Variante A (Track A) bleibt der ruhige Vergleich.

## Signature-Idee (ein Satz)
**Briefbogen:** Die Seite liest sich wie ein Brief der Kanzlei auf gutem Papier, mit Briefkopf (beide Büros), feinen Linien zwischen den Abschnitten, einem sich füllenden Lead-Absatz und einem Gruß am Ende. Grund: Diskretion, Ordnung und Persönlichkeit passen zu einer Kanzlei, und keine der gesehenen Kanzlei-Seiten folgt dieser Brief-Logik.
Ohne Rahmenlinie (N14 nein), ohne Initial (N12 nein), ohne Zeilen-Maske (N10 nein).

## Schrift
**Paar B (N30): Fraunces plus Instrument Sans.** H1 Fraunces 350, `font-variation-settings:"opsz" 144,"SOFT" 0,"WONK" 0`, 56 px; H2 Fraunces 350, 44 px; Text Instrument Sans 400, 17 px; Labels Instrument Sans 600, 12 bis 14 px, Versalien, Laufweite .14em.

## Komponenten (höchstens 4, alle optional, die Seite funktioniert ohne sie)
| # | Komponente | Elemente | Grund |
| --- | --- | --- | --- |
| 1 | Vertikaler Rückruf-Reiter am rechten Rand | N07 | hält den zweiten Kontaktweg dauerhaft im Bild, ohne Falldaten |
| 2 | Vollbild-Menü mit Ziffern | N28 | ruhiger Kopf (nur Wort "Menü" und Button), Notfall-Zeile bleibt im Menü sichtbar |
| 3 | Bild-Streifen für die sechs Leistungen | N17, N34 | Foto, Index-Code und Link je Leistung, zeigt die Breite auf einen Blick |
| 4 | Scroll-gefüllter Lead-Absatz | N11 | macht den Satz über Dr. Stürzl zu einem Moment, ohne Scroll zu blockieren |

Nicht eingebaut wegen Limit: Vorhang-Fußzeile (N27, vielleicht), Karte öffnet sich (N16, vielleicht), Streifen hoher Schmalbilder (N38, vielleicht). Der Salbei-Ton für die Skylines (N37, vielleicht) ist ein Bildfilter und kein Bauteil: eingebaut.

## Elemente aus beiden Abstimmungen
Hero: Foto setzt sich über 4 s (N04, ohne Zeilen-Maske), Farbwort in Salbei kursiv (E10), Hauptbutton atmet nur im Hero und Abschluss (E12), Beleg-Karte am Hero-Rand (E15). Beweis: Titel als Plaketten (E14). Mandanten: zwei Karten mit Foto-Kopf und Link-Pfeil (N15, E17). Leistungen: Bild-Streifen (N17) mit Index-Codes (N34), Foto und Link je Streifen (N18). Ablauf: haftender Titel mit Schrittlinie (E21) und große Ziffern mit Zähler (N19). Über Dr. Stürzl: Werdegang als Zeitleiste (E23), Foto mit versetzter Platte (E24), ihr eigenes Zitat groß (E26), Lead-Absatz füllt sich (N11). Bewertungen: drei offene Zitate, Sterne füllen sich (E27). Fragen: Geisterwort und Plus-Zeilen (E28). Standorte: gestaffelte Stadtbilder mit Etikett (N36), zwei Spalten mit eigener Nummer (N25), Linie zwischen den Büros (E30), Adress- und Zeitentabelle (E31), Salbei-Ton (N37). Abschluss: 50/50-Split (N39) mit Formular in drei Schritten (E33). Notfall-Streifen aus Variante A bleibt als Funktion (nicht abgestimmt, aber Pool-Priorität A und in Variante A freigegeben).

## Storyboard: je Sektion eine Bewegung
| # | Sektion | Das eine, was sich bewegt | Auslöser | Reduced Motion |
| --- | --- | --- | --- | --- |
| 0 | Briefkopf | Linie unter dem Briefkopf zeichnet sich einmal | Laden | Linie da |
| 1 | Hero | Foto setzt sich (108 auf 100 Prozent in 4 s); Button atmet | Laden | still |
| 2 | Beweis | Plaketten blenden gestaffelt ein | Sichtbar werden | Einblenden |
| 3 | Mandanten | Karten heben 3 px, Pfeil rückt 4 px | Hover | still |
| 4 | Leistungen | Streifen öffnet sich beim Überfahren, Tippen oder Fokus | Hover, Fokus, Tippen | erster Streifen offen |
| 5 | Ablauf | Titel haftet, Linie füllt sich, Zähler zählt | Scroll | Linie voll |
| 6 | Über Dr. Stürzl | Lead-Absatz füllt sich Wort für Wort | Scroll | voll lesbar |
| 7 | Bewertungen | Sterne füllen sich | Sichtbar werden | gefüllt |
| 8 | Vertraulich | nichts | – | – |
| 9 | Fragen | Plus dreht zum Kreuz | Klick | schneller |
| 10 | Standorte | Skylines blenden versetzt ein, Linie zwischen den Büros zeichnet sich | Sichtbar werden | sichtbar |
| 11 | Abschluss | Formular-Schritte wechseln, Button atmet | Klick | still |

Keine-Bewegung-Zonen: Notfall-Streifen, Telefonnummern, Rückruf-Panel (öffnet nur auf Klick), Formularfelder, Berufsrechts- und Honorarangaben, Bewertungstexte, Titel.

## Anwaltswerbe-Grenzen
Alle Texte aus Variante A (geprüft, Anwaltswerbe-Check, Prüfer-Lauf). Zusätze nur Struktur. Der Gruß "Mit freundlichen Grüßen, Dr. Anja Stürzl" steht als gesetzter Text, nicht als Unterschrift-Faksimile. Kein WhatsApp. Skylines und Büro-Foto sind echte Dateien der Kanzlei-Seite.
