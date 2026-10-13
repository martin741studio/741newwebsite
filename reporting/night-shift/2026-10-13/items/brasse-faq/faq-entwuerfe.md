# Maria Brasse (shuiguru.de) — FAQ-Check der 12 Seitentexte

**Status: BLOCKED AUF MARTIN — kein FAQ-Entwurf in diesem Lauf, weil die Annahme der Aufgabe nicht zutrifft.**

**Eine-Zeile-Eskalation:** Auftrag ging von „4 Texte ohne FAQ" aus — geprüft sind alle 12 Dateien, tatsächlich haben **0 von 12** keinen FAQ-Block. Bevor irgendein FAQ-Entwurf geschrieben wird, muss Martin bestätigen, ob der Night-Queue-Auftrag eine ältere Dateiversion oder eine andere Seitenauswahl gemeint hat — sonst gibt es nichts zu entwerfen.

Geprüft wurden alle 12 Dateien in `00_project/maria-brasse-pages/maria-text-*.html` (erneut verifiziert per Grep über alle 12 Dateien auf „Häufige Fragen"/„FAQPage" — Treffer in allen 12).
**Jede einzelne Datei hat bereits einen ausgefüllten FAQ-Block** (`<h2>Häufige Fragen</h2>` + 2–6 echte Frage/Antwort-Paare, kein Platzhaltertext). Es gibt also 0 Texte ohne FAQ — nicht 4.

Ich habe deshalb **keine neuen FAQ-Entwürfe geschrieben**, um bestehende, bereits von Maria/Martin formulierte Antworten nicht zu duplizieren oder zu überschreiben (Hard Rule: nur im Zielordner schreiben, reale Daten, keine Zusatzarbeit über die Aufgabe hinaus). Was Martin stattdessen bekommt: die vollständige Bestandsaufnahme, damit er entscheiden kann, ob die Aufgabe obsolet ist oder ob eine andere Quelle gemeint war (siehe `summary.md`).

## Liste: Seite → Thema → bereits vorhandene FAQ

| Datei | Seitenthema | FAQ vorhanden? | Anzahl Q&A |
|---|---|---|---|
| maria-text-startseite.html | Startseite | ✅ ja | 6 |
| maria-text-hi-2026-09.html | „Hi!" (Vorstellung/Über mich) | ✅ ja | 3 |
| maria-text-philosophie-2026-09.html | Philosophie | ✅ ja | 2 |
| maria-text-plancheck-2026-09.html | Plancheck vor Baubeginn | ✅ ja | 5 |
| maria-text-grundriss-2026-09.html | Feng-Shui-Grundrissanalyse | ✅ ja | 3 |
| maria-text-garten-2026-09.html | Feng Shui im Garten | ✅ ja | 5 |
| maria-text-buero-2026-09.html | Feng Shui in der Arbeitswelt (Büro) | ✅ ja | 5 |
| maria-text-arbeitszimmer-2026-09.html | Homeoffice/Arbeitszimmer | ✅ ja | 6 |
| maria-text-hoefe-2026-09.html | Höfe und Hofgemeinschaften | ✅ ja | 3 |
| maria-text-schule-2026-09.html | Feng Shui in Schule und Institutionen | ✅ ja | 4 |
| maria-text-onlineberatung-2026-09.html | Feng-Shui-Beratung online | ✅ ja | 3 |
| maria-text-kosten-2026-09.html | Kosten | ✅ ja | 3 |

**Texte ohne FAQ: keine (0 von 12).**

## Belege (Auszüge, je ein Beispiel pro Datei)

- **startseite**: „Was kostet eine Feng-Shui-Beratung?", „Geht Feng Shui auch online?", „Wann ist der richtige Zeitpunkt für den Plancheck?", „Was bringt Feng Shui im Büro?", „Arbeiten Sie auch mit Schulen?" + 1 weitere.
- **hi**: „Was bedeutet schamanisches Feng Shui konkret?", „Arbeiten Sie allein oder im Team?", „Kommen Sie auch außerhalb Berlins?"
- **philosophie**: „Ist schamanisches Feng Shui esoterisch oder praktisch?", „Muss ich an etwas Bestimmtes glauben, um davon zu profitieren?"
- **plancheck**: „Wann sollte ich den Plancheck beauftragen?", „Reicht ein Grundriss, oder muss ich das Grundstück zeigen?" + 3 weitere.
- **grundriss**: „Reicht ein einfacher Grundriss, oder brauche ich professionelle Baupläne?" + 2 weitere.
- **garten**: „Was sind die wichtigsten Grundregeln für einen Feng-Shui-Garten?" + 4 weitere.
- **buero**: „Wo sollte der Schreibtisch stehen?" + 4 weitere.
- **arbeitszimmer**: „Welche Farbe eignet sich fürs Homeoffice?" + 5 weitere.
- **hoefe**: „Was unterscheidet eine Hofberatung von einer Wohnraumberatung?" + 2 weitere.
- **schule**: „Wie lange dauert ein Klassenzimmer-Projekt?" + 3 weitere.
- **onlineberatung**: „Welche Unterlagen brauche ich für die Online-Beratung?" + 2 weitere.
- **kosten**: „Kostet das Vorgespräch etwas?" + 2 weitere.

Quellenangabe je Zeile in `sources.md`.

## Zusätzlich gefunden (nicht Teil der Aufgabe, nur als Hinweis)

`00_project/maria-brasse-pages/maria-faq-fragen-2026-10.html` ist ein **separates** Tool (Stand 08.10.2026): 6 echte Google-„People also ask"-Fragen (DataForSEO, Google DE, Garten-Themen), bei denen Martin noch Marias eigene Antwort einholen muss, bevor daraus ein FAQ-Block + FAQPage-Schema gebaut wird. Das ist eine offene Aufgabe für Martin/Maria selbst, keine Textdatei ohne FAQ — und nicht Teil dieses Auftrags, deshalb hier nur erwähnt, nicht bearbeitet.
