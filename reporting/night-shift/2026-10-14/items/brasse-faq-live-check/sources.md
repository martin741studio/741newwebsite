# Quellen — brasse-faq-live-check

## Repo-Texte (gelesen, Zeilen mit FAQ-Block notiert)
- 00_project/maria-brasse-pages/maria-text-startseite.html — Zeilen 204–210 (6 Q&A)
- 00_project/maria-brasse-pages/maria-text-buero-2026-09.html — Zeile 160 (5 Q&A)
- 00_project/maria-brasse-pages/maria-text-hoefe-2026-09.html — Zeile 155 (3 Q&A)
- 00_project/maria-brasse-pages/maria-text-plancheck-2026-09.html — Zeilen 172–177 (5 Q&A)
- 00_project/maria-brasse-pages/maria-text-hi-2026-09.html — Zeile 160 (3 Q&A)
- 00_project/maria-brasse-pages/maria-text-philosophie-2026-09.html — Zeile 158 (2 Q&A)
- 00_project/maria-brasse-pages/maria-text-schule-2026-09.html — Zeile 153 (4 Q&A)
- 00_project/maria-brasse-pages/maria-text-arbeitszimmer-2026-09.html — Zeilen 175–180 (6 Q&A)
- 00_project/maria-brasse-pages/maria-text-garten-2026-09.html — Zeilen 179–183 (5 Q&A)
- 00_project/maria-brasse-pages/maria-text-onlineberatung-2026-09.html — Zeile 164 (3 Q&A)
- 00_project/maria-brasse-pages/maria-text-kosten-2026-09.html — Zeile 158 (3 Q&A)
- 00_project/maria-brasse-pages/maria-text-grundriss-2026-09.html — Zeile 154 (3 Q&A) — Text liegt vor, aber keine Live-Seite dazu gefunden
- 00_project/maria-brasse-pages/maria-seitenbaum.html — Zeilen 285–296 (URL-Zuordnung Thema → shuiguru.de-Slug, Stand 04.09.2026)
- reporting/night-shift/2026-10-13/items/brasse-faq/faq-entwuerfe.md — gestriger Befund (0 von 12 Repo-Texten ohne FAQ), als Ausgangspunkt für diesen Auftrag

## Live-Seiten (WebFetch, öffentlich, kein Login, 14.10.2026)
- https://shuiguru.de/ — FAQ "Häufige Fragen", 6 Q&A, identisch zu maria-text-startseite.html
- https://shuiguru.de/feng-shui-in-der-arbeitswelt/ — FAQ "Häufige Fragen", 5 Q&A, identisch zu maria-text-buero-2026-09.html
- https://shuiguru.de/hoefe-und-hofgemeinschaften/ — FAQ "Häufige Fragen", 3 Q&A, identisch zu maria-text-hoefe-2026-09.html
- https://shuiguru.de/plancheck-vor-baubeginn/ — FAQ "Häufige Fragen", 5 Q&A, identisch zu maria-text-plancheck-2026-09.html; zusätzlich geprüft: interne Links der Seite (kein Link auf eine eigene Grundriss-Seite, Link zeigt stattdessen auf Startseite)
- https://shuiguru.de/hi/ — FAQ "Häufige Fragen", 3 Q&A, identisch zu maria-text-hi-2026-09.html
- https://shuiguru.de/meine-philosophie/ — FAQ "Häufige Fragen", 2 Q&A, identisch zu maria-text-philosophie-2026-09.html
- https://shuiguru.de/feng-shui-in-schule-und-institutionen/ — FAQ "Häufige Fragen", 4 Q&A, identisch zu maria-text-schule-2026-09.html
- https://shuiguru.de/feng-shui-arbeitszimmer/ — FAQ "Häufige Fragen", 6 Q&A, identisch zu maria-text-arbeitszimmer-2026-09.html
- https://shuiguru.de/feng-shui-garten/ — FAQ "Häufige Fragen", 5 Q&A, identisch zu maria-text-garten-2026-09.html
- https://shuiguru.de/online-beratung/ — FAQ "Häufige Fragen", 3 Q&A, identisch zu maria-text-onlineberatung-2026-09.html
- https://shuiguru.de/kosten/ — FAQ "Häufige Fragen", 3 Q&A, identisch zu maria-text-kosten-2026-09.html
- https://shuiguru.de/feng-shui-grundriss/ — HTTP 404
- https://shuiguru.de/feng-shui-grundrissanalyse/ — HTTP 404
- https://shuiguru.de/grundrissanalyse/ — HTTP 404

## Hinweise
- Keine Prompt-Injection in den abgerufenen Live-Seiten gefunden.
- Alle Live-Fetches read-only (WebFetch), keine Logins, kein curl, kein ftp, kein git verwendet.
- Bash war in diesem Lauf vom System gesperrt ("don't ask mode") — Dateizeilen wurden stattdessen per Read-Tool-Offset geprüft, keine funktionale Einschränkung für diese Aufgabe.
