# Konzept — 741.studio Startseite (Track B)

Stand 2026-10-11. Grundlage: `00-brief-b/brief-b.md`, Referenz-Board `02-data/references/board.md`, Element-Pool `00-element-pool/` (24 Elemente, 24 von 24 bewertet, siehe `votes-summary.md`). Konzept nach der Abstimmung, bereit für Copy und Bau.

## Signature Idea
**Die eigene Vorher/Nachher-Karte aus dem Hero wird zur Eröffnung der Seite.** Die grauen/roten Punkte (Kunden, die ein Unternehmen nicht finden) sammeln sich beim Laden zu gelben, leuchtenden Punkten und zur echten Vorher/Nachher-Karte, während die Zahl "+278 % Anrufe" hochzählt. Grund: Das Bild existiert schon und ist echt (kein neues KI-Bild nötig), es sagt exakt, was 741 verkauft (Unsichtbarkeit → Sichtbarkeit).

**Pool-Votum (24 von 24 bewertet, siehe `votes-summary.md`):** E01 (Punkte → Karte) bekam "vielleicht" mit der Notiz, die Bewegung der Punkte müsse erst "Sinn ergeben" statt nur ein Kreis zu sein — korrigiert: die Punkte ziehen jetzt sichtbar von außen zur Karte, nicht auf einer Kreisbahn. E02 (Punkte → Balken) bekam "vielleicht, Animation unklar im Kontext" und wird nicht gebaut. **Der Faden endet NICHT bei den Partner-Logos** (E24 "Faden-Ende: Punkte lösen sich in Logos auf" = Nein) — die Signature Idea bleibt auf den Hero begrenzt, die Logos bekommen ihr eigenes, unabhängiges Einblenden (E22, Ja).

## Sektions-Storyboard
| Sektion | Bewegt sich | Aufgabe | Auslöser | Reduced-Motion |
| --- | --- | --- | --- | --- |
| 0 Kopf | Nav-Einträge heben sich leicht an (Hop, E03 Ja); Kopf schrumpft beim Scrollen (E04 Ja); gelbe Linie wächst unter dem aktiven Link (E05 Ja) | Kopf wirkt lebendig, ohne vom Inhalt abzulenken | Hover / Scroll | kein Hub/Schrumpf, normale Unterstreichung |
| 1 Hero | Punkte ziehen sichtbar von außen zur bestehenden Vorher/Nachher-Karte (E01, korrigiert), echte Zahl (+278 % Anrufe) zählt währenddessen hoch; Garantie-Pille atmet sehr langsam (E07 Ja); Beleg-Karte kippt minimal mit dem Zeiger (E08 Ja); ein Wort der Headline steht kursiv (E09 Ja); riesige, ruhige Grund-Typografie (E06 Ja) | zeigt sofort das Versprechen, bevor ein Wort gelesen wird | Laden | Karte steht fertig, keine Punkte-Animation, keine Pille-Atmung, kein Kippen |
| 2 Outcome (übernommen) | Kennzahlen-Karten gleiten nacheinander ein und zählen dabei hoch (Bento Glide + E12, beide Ja/Vielleicht); Verbindungslinie zeichnet sich klar steigend (E13, korrigiert: nicht mehr hoch-dann-runter); Bewertungssterne füllen sich nacheinander (E14 Ja) | macht Ergebnisse lesbar statt als Textwand | Scroll | Karten/Linie/Sterne stehen fertig |
| 3 Gründer/Vertrauen (neu, Martin) | Foto blendet ein, gerader abgerundeter Rahmen statt Bogen (E15, korrigiert); kein gezeichnetes Anführungszeichen (E16 Nein); Unterschrift-Akzent "– Martin, Gründer von 741.studio" (E17 Ja); kein Zeitleisten-Muster (E18 Nein) | nach dem Zahlen-Beweis: das Gesicht dahinter, senkt die Hürde für den unsicheren Inhaber | Scroll-Reveal einmal | identisch, nur ohne Fade |
| 4 Professional-Tools (übernommen) | bleibt wie heute (eigene Interaktion schon vorhanden) | zeigt die Werkzeuge in Aktion | bestehend | bestehend |
| 5 Partner-Logos | Logos blenden gestaffelt ein, Graustufen → Farbe beim Hover (E22 Ja). Kein Bezug zu den Hero-Punkten (E24 Nein) | eigenständiger letzter Beweis vor den Leistungen | Scroll, einmal | Logos stehen fertig |
| 6 Leistungen (übernommen, dunkles Band) | jede Zeile zeigt beim Überfahren eine Kurzzeile (E19 Ja); nummerierte nebenstehende Variante mit wachsender Linie als Entwurfsoption (E21 Ja); glänzendes, per CSS erzeugtes Objekt driftet leicht statt des heutigen Fremd-Videos (E20 Ja) | aus der reinen Liste wird eine Aussage, eigenes statt geliehenes Material | Hover/Fokus/Scroll | Kurzzeile ist immer sichtbar, Objekt steht still |
| 7 Abschluss | keine Bewegung | letzter CTA | – | – |

## Komponenten (3 von max. 4 gewählt)
1. **Punkt-Formation im Hero** (eigene Signature Idea, korrigiert nach Votum) — Grund: Konversion, nicht Dekoration. Zeigt das Versprechen, bevor Text gelesen wird.
2. **Bento Glide** für die Outcome-Kennzahlen — Grund: Konversion. Zahlen werden nacheinander lesbar statt als Tabelle.
3. **Hop Navigation** im Kopf — Grund: Marke. Kleine, günstige Geste, die "selbstbewusst/poliert" fühlbar macht, ohne vom Inhalt abzulenken.
Nicht gewählt: Cursor-Figur, Zeichen/Maskottchen (passt nicht zu "skeptischer Inhaber, Vertrauen"), Spiel-Element, holografischer Sticker, Zeitleiste (E18 Nein), gezeichnetes Anführungszeichen (E16 Nein), Logo-Laufband (E23, E22 gewählt), Punkt-Auflösung bei den Logos (E24 Nein).

## Keine-Bewegung-Zonen
Garantie-Pille-Text und Sterne-Zeile, Preise (keine auf der Seite), rechtliche/Fuß-Texte, CTA-Buttons selbst (bewegen sich nicht, nur der Hover-Zustand ändert sich normal). Der Gründer-Text ist bewusst kurz und sachlich, kein "großes Zitat" (E16 Nein, Martins Notiz: der Platzhaltersatz wirkte gekünstelt).

## Was aus der Live-Seite bleibt (Inhalt, neu gestaltet)
- Hero-Beweiszeile: 90-Tage-Top-3-Garantie, ★★★★★, Vorher/Nachher-Karte (wird zur Signature Idea).
- Professional-Tools: interaktive Werkzeug-Vorführung, Funktion bleibt, nur Optik passt sich an.
- Outcome-Sektion: Ergebnisse/Zielgruppen-Aussagen, neu als Bento-Glide-Karten.
- Leistungen-Band (dunkel, glänzendes 3D-Objekt, Liste Webentwicklung/Design/SEO/Bezahlte Werbung/KI-Automatisierungen/Conversion-Optimierung/Branding/Strategie): bleibt als Sektion, bekommt Hover-Kurzzeilen.
- Partner-Logo-Leiste: bleibt, wird zum Ziel der Punkt-Auflösung.
Neu, nicht auf der Live-Seite: Gründer/Vertrauens-Sektion mit echtem Foto (`/assets/local-seo/images/founder_martin.png`, gerader abgerundeter Rahmen, kein Bogen), kurzem sachlichem Ich-Form-Text und Unterschrift-Akzent, nach dem Vorbild von Noughts & Ones. Kein Zitat-Großbuchstabe, keine Zeitleiste.

## Regeln aus dem Workflow, eingehalten
Eine Render-Funktion je Sektion. Kein Loop-Video geplant (kein Video-Tool verbunden), also entfällt die Loop-Regel. X-ray-Schalter kommt beim Build (B7). Jede Bewegung hat eine Aufgabe, siehe Tabelle.

## Von Martin entschieden (2026-10-11)
1. Punkt-Formation im Hero: **mit echten Zahlen** (+278 % Anrufe usw. zählen hoch, während sich die Punkte formen).
2. Gründer-Sektion: **Martin**, nicht das Team.
3. Reihenfolge: **nach der Outcome-Sektion** (erst Beweis/Zahlen, dann das Gesicht dahinter).
4. Giveaway- und Community-Promo: **beide weggelassen.**

## Status
Konzeptrichtung freigegeben (2026-10-11, "yes i guess i approve"). Element-Pool abgestimmt (24 von 24, `votes-summary.md`). Konzept oben ist auf dem Stand der Abstimmung. Nächster Schritt: Copy (B3), Design-Doc und GPT-Mockup (B5/B6), Bau (B7).
