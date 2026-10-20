# Motion — Dumann Track B, Prototyp v1

Basis: `00_project/cro-homepage-motion-spec.md` plus die Track-B-Ausnahmen (Workflow Abschnitt 4). Alles nur Code. Kein Video, kein Parallax, kein Scroll-Hijacking, kein Cursor-Folger.

| Sektion | Das eine, was sich bewegt | Auslöser | Reduced Motion |
| --- | --- | --- | --- |
| Seite | **Viriditas-Faden**: ein SVG-Pfad (Ranke mit 48 Blättern) wächst mit dem Scroll-Anteil, Blätter erscheinen, wenn der Pfad sie erreicht, am Ende eine Blüte in Oliv. Im Abschlussband wechselt der Faden auf Hellflieder | Scroll | komplett sichtbar, still |
| 1 Hero | Wellenlinie unter "Hildegard-Heilkunde" zeichnet sich einmal; Button atmet (4,5 s, pausiert bei Hover) | Laden | Linie da, Button still |
| 2 Beweis | Linie unter jeder Zahl zeichnet sich einmal | Sichtbar werden | Linie sichtbar |
| 3 Themen | Karten blenden gestaffelt ein, Hover hebt 3 px | Sichtbar werden | nur Einblenden |
| 4 Leistungen | Bild-Vorschau wechselt beim Überfahren oder Fokussieren einer Zeile (Überblenden 400 ms); Pfeil rückt 4 px | Hover, Fokus | erstes Bild fest |
| 5 Termin | Titel haftet (`position:sticky`), Schrittlinie füllt sich mit dem Scroll, Knoten füllen sich | Scroll | Linie voll |
| 6 Über Daniela | Foto und Text blenden einmal ein; Zitatband blendet einmal ein | Sichtbar werden | Einblenden |
| 7 Bewertungen | Sterne füllen sich links nach rechts | Sichtbar werden | gefüllt |
| 8 FAQ | Plus dreht zu Kreuz, nur eine Frage offen (natives `details`) | Klick | – |
| 9 Standort | Nadel fällt 12 px, einmal | Sichtbar werden | sichtbar |
| 10 Abschluss | Farbblock-Wechsel (E30): der Kopf wechselt von Creme zu Lila, der Faden zu Hellflieder; das Abschlussband ist Lila; Button atmet | Scroll | fester Farbwechsel ohne Übergang |

**Ausnahmen von der Motion-Spec (Track B):** (1) Im Hero bewegen sich zwei Dinge: die Wellenlinie zeichnet sich einmal beim Laden (1,1 s, danach still), der Button atmet dauerhaft. (2) Alle Buchungsbuttons heben sich beim Überfahren 2 px; die zwei atmenden Buchungsbuttons (Hero, Abschluss) sind die einzigen Ausnahme von "keine Bewegung auf Buchungslinks". (3) Die Hinweisbox blendet nicht ein (kein Reveal-Element). (4) der Faden und die Schrittlinie animieren `stroke-dashoffset` und `transform:scaleY`, nicht nur `transform` und `opacity`. Beide laufen nur beim Scrollen, auf einem Pfad ohne Layoutänderung. Es gibt genau zwei atmende Elemente (Hero und Abschluss). Keine Bewegung in Preisblock, Hinweisbox, Bewertungstext, Buchungslinks.
**Schalter:** `?rm=1` erzwingt die Reduced-Motion-Fassung (zusätzlich zur Systemeinstellung), `?xray=1` oder Taste `x` zeigt Code-Ebenen rot und Bild-Ebenen blau umrandet, `?shot=1` zeigt alle Zustände für Screenshots.
