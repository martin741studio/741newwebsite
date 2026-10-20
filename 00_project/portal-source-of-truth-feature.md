# Portal-Feature: Gelockte "Source of Truth" Stammdatenkarte

**Ziel:** Eine feste, gelockte Stammdaten-/Leistungs-Wahrheit pro Kunde. 741 und Kunde ziehen immer exakt dieselben Daten. Standard für ALLE Kunden-Dashboards.

## Backend (fertig — Supabase 741-portal `galjmtozcgxcwtzkzbpi`)

Tabelle `public.client_master_data` (1 Zeile pro Kunde, PK = client_id → clients.id):

Felder (einfach, copy-fähig):
- `business_name, owner_name, legal_note`
- `public_address` (die EINE öffentliche NAP-Adresse), `billing_address` (nicht öffentlich)
- `phone, phone_note, website, public_email`
- `hours, languages, booking_url, booking_note`
- `google_place_id, google_review_link`
- `category_primary` + `categories_secondary` (jsonb array)
- `services` (jsonb array, verzeichnis-/GBP-listbar)
- `description_only` (jsonb array — nur in Beschreibung, NICHT als Leistung listen)
- `focus` (jsonb obj: zielgruppe, wunschpatientin, stil)
- `boundaries` (jsonb obj: macht_nicht[], preis_grenze)
- `open_points` (jsonb array [{feld, frage}] — noch zu klärende Punkte)
- `extra` (jsonb, frei), `locked` (bool, default true), `updated_by, updated_at, created_at`

RLS (identisch zum restlichen Portal):
- SELECT `read own`: `client_id = my_client_id() OR is_admin()`
- ALL `admin write`: `is_admin()` — nur Admin schreibt; Kunde hat KEINE Schreib-Policy (read-only = "gelockt").
- Trigger `trg_touch_client_master_data` hält `updated_at` frisch.

Erste Zeile geseedet: **Praxis Suriya** (client_id 3f71ef33-8c74-4ea1-b2d3-0273c2e99649), 27 Leistungen, 5 Nebenkategorien, 3 open_points (public_email, booking_url, faszientherapie).

## Frontend (TODO — im Portal-SPA-Repo, nicht auf diesem Rechner)

**Karte "Stammdaten / Source of Truth"** — ganz oben in der Dashboard-Übersicht verankert, für Admin UND Kunde sichtbar:
1. **Kopfzeile:** Titel + 🔒 "Gelockt"-Badge + Hinweis "Verbindliche Wahrheit — 741 & Kunde ziehen hieraus."
2. **Read-only**, KEINE Kommentar-/Edit-Buttons in der Kundenansicht.
3. **Copy-Button pro Feld** (Adresse, Telefon, Website, Place-ID, Review-Link, jede Leistung als Block etc.).
4. **Sektionen:** Identität/NAP · Kontakt/Buchung · Google-IDs · Kategorien · Leistungen (Chips) · Beschreibung-only (getrennt, klar "nicht als Leistung listen") · Fokus · Grenzen.
5. **`open_points`** als kleine gelbe "Noch zu klären"-Liste unten (nur Admin-Sicht optional).
6. **Admin-Edit** nur im Admin-Panel (separate Route), schreibt via `is_admin()`-Policy; Kundenansicht bleibt read-only.
7. Leere Felder (z.B. public_email, booking_url bei Suriya) als "— offen" rendern, nicht verstecken.

**Datenquelle:** `select * from client_master_data where client_id = <current>` (RLS liefert automatisch die eigene Zeile).

## Standardisierung
Beim Anlegen neuer Kunden: leere `client_master_data`-Zeile mit anlegen (oder lazy beim ersten Öffnen). So hat jeder Kunde die Karte.
