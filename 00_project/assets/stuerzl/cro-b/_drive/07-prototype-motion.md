# Motion — STÜRZL Variante B (Briefbogen), Prototyp v1

Basis: `00_project/cro-homepage-motion-spec.md` plus Track-B-Ausnahmen. Alles nur Code, kein Video, kein Parallax, kein Scroll-Hijacking.

| Sektion | Das eine, was sich bewegt | Auslöser | Reduced Motion |
| --- | --- | --- | --- |
| Briefkopf, Köpfe | Haarlinien ziehen sich einmal von links | Sichtbar werden | sichtbar |
| 1 Hero | Foto setzt sich (108 auf 100 Prozent in 4 s); Button atmet | Laden | still |
| 2 Beweis | Plaketten blenden gestaffelt ein | Sichtbar werden | Einblenden |
| 3 Mandanten | Karte hebt 3 px, Pfeil rückt 4 px | Hover | still |
| 4 Leistungen | Streifen öffnet sich (Hover, Fokus, Tippen), Titel und Link erscheinen | Hover, Fokus, Tippen | erster Streifen offen |
| 5 Ablauf | Titel haftet, Linie füllt sich, Zähler "1 : 4" bis "4 : 4", aktiver Schritt voll | Scroll | alles voll |
| 6 Über Dr. Stürzl | Lead-Absatz füllt sich Wort für Wort; Zeitleiste füllt Punkte | Scroll | voll lesbar |
| 7 Bewertungen | Sterne füllen sich | Sichtbar werden | gefüllt |
| 9 Fragen | Plus dreht zum Kreuz | Klick | schneller |
| 10 Standorte | Skylines blenden ein | Sichtbar werden | sichtbar |
| 11 Abschluss | Formular wechselt Schritt, Button atmet | Klick | still |

Komponenten (höchstens 4): Rückruf-Reiter, Vollbild-Menü, Foto-Streifen, Lead-Absatz. Ausnahmen von der Spec: Im Hero bewegen sich das Foto und der Button (zwei Dinge, Foto einmalig, Button atmet). Das Menü öffnet sich per Klick mit 0,6 s Gleiten. Genau zwei atmende Buttons (Hero, Abschluss-Formular, gemessen 2). Keine Bewegung in Notfall-Streifen, Telefonnummern, Berufsrechtsangaben, Bewertungstexten.
**Schalter:** `?rm=1` (Reduced-Motion-Test), `?xray=1` oder Taste `x` (Code rot, Fotos blau), `?shot=1` (alle Zustände für Screenshots).
