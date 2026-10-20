# Motion — STÜRZL Startseite Prototyp v1

Grundlage: `00_project/cro-homepage-motion-spec.md` (ruhig, Reveal einmal, nur transform und opacity, Atmen nur Hero und Abschluss). Abweichungen und Besonderheiten dieses Kunden:

| Abschnitt | Highlight | Umsetzung |
| --- | --- | --- |
| 1 Hero | Button "Vertraulich anfragen" | atmet (4,5 s), pausiert bei Hover, hebt sich 2 px; Hero baut sich beim Laden auf (90 ms Versatz); Wellenlinie unter "Frankfurt und München." zeichnet sich einmal |
| 2 Beweis-Leiste | Zitat | Reveal einmal; keine Sterne in der Leiste (fünf Belege mit Symbolen) |
| 3 Mandanten | Karten | zwei Karten, Reveal gestaffelt |
| 4 Leistungen | Pfeil "Mehr erfahren" | Karten gestaffelt, Hover hebt die Karte 3 px, Pfeil 4 px nach rechts |
| 5 Ablauf | Schrittlinie | Linie zieht von 1 nach 4 (900 ms), Nummern füllen sich |
| 6 Über Dr. Stürzl | Reveal | Foto und Text blenden ein; kein Unterstreichen der Titelzeile (Bewusst weggelassen, ruhiger) |
| 7 Bewertungen | Sterne je Karte | füllen links nach rechts, 60 ms Versatz |
| 9 FAQ | offene Frage | nativ `details`, Plus dreht um 45°, nur eine Frage offen |
| 10 Standorte | Kartennadel | fällt 12 px in Position, einmal, kein Prellen |
| 11 Abschluss | Button | atmet wie im Hero, pausiert bei Hover |

Reduced motion: alle Verschiebungen aus, Einblenden 300 ms, Atmen aus. Genau zwei atmende Elemente (gemessen: M10 = 2). Nichts bewegt sich beim Zurückscrollen (gemessen: 0 versteckte Elemente nach Auf- und Abscrollen). Kein Parallax, kein Karussell, keine Endlosschleife außer den zwei Buttons.
