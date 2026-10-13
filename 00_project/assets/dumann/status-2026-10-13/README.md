# Dumann: Statusseite und Entscheidungskarten (Entwurf, 13.10.2026)

Alles ist Entwurf. Nichts ist an Daniela gesendet, kein Wix-Eingriff, `index.html` des Portals unverändert, kein Bericht veröffentlicht.

| Datei | Zweck |
| --- | --- |
| `build_status_dumann.py` | Daten und Texte der Statusseite. Baut `status-dumann-2026-10-13.html` |
| `../../client-status/build_status.py` | Gemeinsamer Baukasten für jeden Kunden (Look wie Bali, Farbe aus `theme`) |
| `status-dumann-2026-10-13.html`, `status-1440.png`, `status-500.png` | Ergebnis und Screenshots |
| `cards_dumann.py`, `cards.json`, `approval-drafts-dumann.sql`, `approval-cards-draft.md` | Karten E8 bis E27 (je Vorher, Optionen, Schloss). `lint_cards.py` prüft jede Karte auf 5/5 |
| `tasks-dumann.md` | Aufgabenliste (Kundentext) und interne Notizen |
| `portal-message-daniela.txt` | Portal-Nachricht, Martin sendet |
| `fetch_gsc.mjs`, `data/` | Search-Console-Pull und Live-Abruf als Beleg |
| `claims.json`, `SOURCES.md` | Belegte Zahlen für das Slop-Gate, Quellenliste |

Neuer Kunde: `build_status_dumann.py` kopieren, `cfg` mit eigenen Zahlen füllen, `theme` auf die Kundenfarbe setzen, Zahlen in `SOURCES.md` belegen, dann Slop-Gate (`deslop_de.py`) und Screenshots bei 1440 und 500 px.
Karten stehen als `draft` in `approval_items` (E1 bis E7 vom Freigabe-Chat, E8 bis E27 aus diesem Lauf). Freigabe nur einzeln durch Martin im Chat.
