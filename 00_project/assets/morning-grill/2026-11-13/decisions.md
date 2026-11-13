# Decisions 2026-11-13 (Morgen-Grill, kurz nach 12:00 WITA)

Quellen: Portal live 12:50, 12 Chats (S2), Kalender (leer), Outreach-Board, Server-Journal. Scan PASS, S8 Tracking nicht lesbar.
Entfernte Scanner-Karten: Dumann-Frist (geparkt 11.11.), read-source-of-truth (Regel, keine Frist), Suriya-Verzeichnismails (geparkt), Hüwel-Nachricht 20.10. (am 09.11. beantwortet, nur read_by_admin-Flag offen), Stephan/Manuela-Freigaben (Prio 4, kurzer Brief).

1. STÜRZL E24 — Martin: "Go – beide Profile einstellen (Empfehlung)".
   Erledigt 13:12 WITA: Beschreibung München (ChIJnWDIW4d1nkcRJjE6HD1bhXM) und Frankfurt (ChIJyVGAdikEaW8RUOWpEJs-2XA) per Local Falcon API, Wortlaut aus E24. Rückgabe: beide Texte gesetzt, Google-Status hasPendingEdits=true (Google prüft). approval_items E24: status go, go_at gesetzt, Notiz an Anja.
   Offen: in 1-3 Tagen live in Maps zurücklesen (hasPendingEdits weg).
2. Suriya Ads — Martin: "Go – Keyword pausieren (Empfehlung)".
   Erledigt: "massage ingelheim" (Phrase, criterion 199637296286~381408921559, Konto 499-126-8644) PAUSED, zurückgelesen. Grund: 7 Tage 28,81 EUR, 20 Klicks, 0 Conversions. "ayurveda massage ingelheim" bleibt an (1 Conversion).
3. Nacht 13.11. — Martin: "Stürzl + Suriya (Empfehlung)".
   Queue reporting/night-shift/queue/2026-11-13.json (2 Items: stuerzl-fahrplan-m2-bis-ziel, suriya-fahrplan-m2-bis-ziel), commit 2bedf438, auf dem Server per git ff, Probelauf ok.
   Fund + Fix: Der Probelauf schrieb state.json mit "pass" in den echten Tagesordner, der echte Lauf hätte beide Items übersprungen. Ordner verschoben (2026-11-13-dry-1310), run.py schreibt Probeläufe jetzt nach <day>-dry (commit a4d90da4, Server aktualisiert).
   Fund 2: Queue per scp UND im Commit blockiert den ff-merge auf dem Server. Regel: Queue nicht committen, nur push_queue.sh (heute einmalig per Hand gelöst).
