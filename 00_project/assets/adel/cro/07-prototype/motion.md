# Bewegung — Abweichungen von der Standard-Spezifikation (Aydan Adel)

Basis: `00_project/cro-homepage-motion-spec.md`. Martin wollte die Ronas-IT-Elemente. Diese Abweichungen sind nötig. Alles andere folgt der Spezifikation.

| Element (Ronas) | Umsetzung hier | Grund |
| --- | --- | --- |
| Wellenlinien unter den drei H1-Zeilen | Einmal beim Laden von links nach rechts gezeichnet (nur `transform: scaleX`), danach ruhig. Verzögerung 0,35 s, 0,55 s, 0,75 s. | Ronas-Markenzeichen. Einmalig, kein Loop. |
| Drehender Text-Kreis ("Watch our showreel") | Steht still. Nur bei Hover dreht der Ring einmal in 6 s. | Spezifikation verbietet Loops. Hover ist erlaubt. |
| Absatz grau zu Tinte beim Scrollen | Wörter werden von 20 % auf 100 % Deckkraft heller (nur `opacity`), einmal pro Wort, nie zurück. | Spezifikation: nur transform und opacity, kein Re-Trigger. |
| Nummerierte Leistungsblöcke | Reveal je Element, 90 ms gestaffelt. Highlight: Pfeil bei "Mehr erfahren" rückt 4 px bei Hover. | Standard |
| Plus-FAQ | Plus dreht zu Minus (transform), Antwort fadet 250 ms ein, nur eine Frage offen. | Standard (Highlight Sektion 9) |
| Dunkles Abschlussband | Statische Wellenkante (CSS-Maske). Highlight: atmender CTA. | Standard |
| Breathing-CTA | Nur Hero und Abschluss. | Standard |

`prefers-reduced-motion`: alles ohne Bewegung, nur Fades.
