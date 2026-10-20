# Elemente-Katalog Track B, Daniela Dumann Startseite (2026-10-12)

Aus drei Recherchen mit insgesamt 25 gesehenen Seiten und 76 Elementen: `research-practitioner.md` (P1 bis P21), `research-award.md` (A1 bis A33), `research-highlights.md` (H1 bis H22). Tiles liegen in `references/`, `references/award/`, `references/practitioner/`, `references/highlights/`. Nichts ist kopiert: nur Struktur und Technik.
Quellen dieses Laufs: Awwwards, Land-book, One Page Love, Godly (Übersicht), dazu Seiten für Praxis, Kräuter-Erbe und Hildegard. **Grenze:** Firecrawl zeigt Ruhezustände. Bewegung wurde aus Code gelesen oder von mir selbst live gesehen (Ronas, 2026-10-10).

## 1. Drei Richtungen für die Signature-Idee (Empfehlung: B)

| | A: Pflanzentafel | **B: Viriditas-Faden (Empfehlung)** | C: Buch der Heilkunde |
| --- | --- | --- | --- |
| Idee | Jede Sektion trägt eine gezeichnete Pflanzentafel in Lila-Linie, Bogen-Portrait, versetzte Farbplatte, Schreibschrift-Akzent | Eine einzelne Pflanzenranke in Linienzeichnung wächst beim Scrollen die Seite hinab und verbindet alle Sektionen wie ein Faden. "Viriditas" (Grünkraft) ist Hildegards Wort und der Name von Danielas Schule | redaktioneller Look: Rand-Label-Spalte, hängender Einzug, Zierlinien, Randnotizen, Erbe-Zitatband, fast keine Bewegung |
| Merkbar wegen | schönes Gesamtbild | **eine** Bewegung, die die Marke erzählt | Ruhe und Gelehrsamkeit |
| Bewegung | gering (Linien zeichnen einmal) | mittel, nur Scroll, sehr langsam | sehr gering |
| HWG-Risiko | niedrig | niedrig (Pflanze ist Symbol, kein Versprechen) | am niedrigsten |
| Aufwand | M (Zeichnungen nötig) | M (ein SVG-Pfad, `stroke-dashoffset`; ist keine reine `transform/opacity`-Bewegung, Ausnahme steht in `motion.md`) | S |
| Risiko | wird beliebig | Aufmerksamkeit lenkt vom CTA ab, falls zu stark | wirkt zu still |

B nutzt Elemente aus A (Pflanzentafeln als Kapitelmarken) und aus C (Randnotizen, Zierlinien). Das echte Hildegard-Icon aus dem Logo dient als Siegel in Kopf und Fuß (P16).

## 2. Eine Hervorhebung pro Sektion (Martins Regel)

"Punkt" = der Satz, den die Sektion trägt. Die Sätze stammen aus dem freigegebenen Track-A-Text und dem Pool-Update und werden in Copy v3 final.

| # | Sektion | Punkt (hervorgehoben) | Technik (erste Wahl) | zweite Wahl | Quelle (Katalog-ID) |
| --- | --- | --- | --- | --- | --- |
| 1 | Hero | "Hildegard-Heilkunde in Charlottenburg": das Wort **Hildegard** | Wellen-Unterstreichung, einmal gezeichnet (H1) und Farbwort in Lila (H9); Bogen-Portrait (P1); ein Schreibschrift-Akzent (P3) | gestrichelter Ring um das Wort (H10) | H1, H9, P1, P3 |
| 2 | Beweis-Leiste | "Seit 2002" und "5,0 bei 9 Bewertungen" | Zahlen mit Linie, statisch (H8) und überlappende Beleg-Karte am Hero-Rand (A2) | sehr langsames Laufband der Mitgliedschaften (H14) | H8, A2 |
| 3 | Ist das etwas für mich | "Fünf Themen, bei denen ich Sie **begleite**" | Karten mit Blob-Plakette und Linien-Symbol (P7) plus Geister-Ziffer (H7) | Mono-Labels um ein Foto (H13) | P7, H7 |
| 4 | Leistungen | "Hildegard-Heilkunde als Mitte, acht Leistungen darum" | nummerierte Zeilen mit Kicker (H3), Bogen-Bildkarten (A10) | haftender Seitentitel (H2) | H3, A10 |
| 5 | Erster Termin | "60 Minuten, in denen ich zuhöre" | haftender Seitentitel mit Schrittlinie und Knoten (H2 und H16), Preisblock | große Ziffern (H3) | H2, H16, A3 |
| 6 | Über Daniela | Methode in 3 Sätzen, das Wort "Überzeugung" | Foto in Bogenform mit versetzter Lila-Farbplatte (P1, P2, H12), **einmal** aufleuchtende Aussage (H4), Erbe-Zitatband mit Quelle (P10) | Randnotiz (H5) | P1, P2, H4, H12, P10 |
| 7 | Bewertungen | "5,0 Sterne bei 9 Google-Bewertungen" | ein großes Zitat in Kursiv-Serif mit Rollen-Label (H19, P19) | nur kursiver Akzent (H18) | H19, P19 |
| 8 | FAQ | "Fragen vor dem ersten Termin" | übergroßes Geisterwort in Lila 6 bis 10 % (H6) plus Plus-Linien-FAQ (H20) | haftender Titel (H2) | H6, H20, A15 |
| 9 | Standort | "Direkt am Schloss Charlottenburg" | Randnotizen für Anreise und Parken (H5), Adress- und Zeitentabelle (A21) | versetzte Platte hinter der Karte (H12) | H5, A21 |
| 10 | Abschluss | "Lernen Sie mich **persönlich** kennen" | dunkles Lila-Band mit Wellenkante, Geisterwort, **ein** Oliv-Button, Telefon-Pille (A17, P15, H6) | Farbblock-Wechsel (H15) | A17, P15, H6 |
| Seite | durchgehend | der Faden | Viriditas-Ranke (Richtung B), Zierlinien (P17), Einblenden einmal (H21) | | P17, H21 |

## 3. Bestätigt gesehene Muster, die wir nicht übernehmen

Scroll-Hijacking, horizontales Pinning, Cursor-Spotlight und eigene Cursor, diagonale Clip-Keile, 3D und WebGL, schnelle Laufbänder, Schreibmaschinen-Text, Neon auf Schwarz, Pillen-Stockfotos, Doctolib-Blau, Krankheitslisten mit "vorbeugen", Pop-ups beim Laden, Comic-Schreibschrift, Vorher-Nachher, Erfolgszahlen. Gründe: Vertrauen, HWG, Ruhe, Palette.

## 4. HWG-Prüfung der Elemente

- Kein Element trägt ein Ergebnis. Zahlen nur als Fakten (Jahre, Bewertungsanzahl).
- Bewertungs-Zitate nur zu Zuhören, Stimmung, Terminen. Die sichtbaren Google-Zitate betreffen Kurse und kommen mit Rollen-Label ("Kursteilnehmerin") oder entfallen, bis Patientenstimmen vorliegen.
- Hildegard-Zitat im Erbe-Band: nur ein Satz zu Natur oder Ordnung, mit Quelle, geprüft vor dem Einbau. Kein Satz zu Heilung.
- Pflicht-Hinweisbox bleibt. Fuß-Grenzzeile "ersetzt keine ärztliche Behandlung" (P21).
