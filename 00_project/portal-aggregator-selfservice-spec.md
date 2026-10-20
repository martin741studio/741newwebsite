# Feature-Spec: Aggregatoren-Selfservice im Kundenportal

Für den Dashboard-Chat / Developer. Ziel: der Kunde (und Admin/Developer) trägt die
kostenlosen Layer-1-Karten/KI-Aggregatoren selbst ein, mit vorbefüllten Daten und
Status-Häkchen. Teil des Citations-/Listings-Moduls.

Supabase-Projekt: `741-portal` = `galjmtozcgxcwtzkzbpi`.

## 1. Warum
Die Aggregatoren (Bing, Apple, Foursquare, TomTom, HERE, Facebook) haben **keine
Auto-Submit-API**. Es sind Portal-Flows mit Konto + Verifizierung. Die Verifizierung
geht **nur mit den Logins des Kunden** (Apple-ID, Microsoft-Konto). Darum ist
Kunden-Selfservice hier der richtige Weg — geführt, mit fertigen Daten.

## 2. Wo im Portal
Bestehender Tab **„Sichtbarkeit"** (`renderCitations()`). Neue Sektion darunter:
**„Selbst eintragen: Karten & KI-Aggregatoren"**. Kunde und Admin sehen sie; Admin
kann Status überschreiben.

## 3. Datenmodell (was existiert, was neu)
Existiert:
- `client_locations` — kanonische NAP (Name, Straße, PLZ, Ort, Telefon, Website,
  E-Mail, `primary_category`, `hours` jsonb, `description`). Quelle fürs Prefill.
- `directories` — Masterliste; die tier0-Zeilen sind die Aggregatoren
  (Bing Places, Apple Business Connect, Foursquare, TomTom, HERE, Facebook/Meta;
  GBP ist tier0, aber schon live; Instagram = social, separat).
- `client_citations` — Status je Kunde×Verzeichnis
  (`status`: missing/planned/submitted/live/inconsistent, `listing_url`,
  `submitted_via`, `last_checked`, `nap_match`, `notes`).

Neu:
- Spalte **`directories.guide jsonb`** (wie `access_grants.guide`): pro Aggregator
  `{ url, effort, category_hint, steps: [..] }`. Seed für die 6 tier0-Zeilen (Texte s. §6).

## 4. RLS / Schreibrecht des Kunden
Kunde darf aktuell `client_citations` nur lesen. Für Selfservice braucht er
Schreiben auf den eigenen Status — **sauber per SECURITY-DEFINER-RPC**, nicht per
direktem Table-Update:

```
client_set_citation_status(p_directory_id uuid, p_status text)
  - nur eigene Zeile (my_client_id() = client_id)
  - nur tier0-Verzeichnisse
  - status ∈ {planned, submitted, live}
  - setzt last_checked = now()
```

Admin behält vollen Zugriff (is_admin()).

## 5. Frontend-Verhalten
In `renderCitations()` eine Karten-Liste der tier0-Verzeichnisse (außer GBP), für die
der Kunde eine `client_citations`-Zeile hat. Pro Karte:
- Name + Aufwand (`guide.effort`)
- Schritte (`guide.steps`)
- Kategorie-Hinweis (`guide.category_hint`)
- Button „Portal öffnen" (`guide.url`)
- **Prefill-Block** aus `client_locations` mit Kopier-Buttons je Feld
  (Muster wie bei den Zugangs-Einladungen)
- **Status-Umschalter** offen → eingereicht → live → ruft die RPC
- Fortschritt oben (z. B. „2/6 live")

Admin sieht dasselbe + darf jeden Status setzen.

## 6. Die 6 Ziele (Seed für `directories.guide`)
Reihenfolge = Wert/Aufwand.

1. **Bing Places** — `https://www.bingplaces.com` · ~2 Min
   - Kategorie: Health & Medical → Alternative Medicine / Naturopath
   - Schritte: Einloggen (Microsoft) → „Import from Google" → GBP wählen → prüfen → absenden.
2. **Apple Business Connect** — `https://businessconnect.apple.com` · ~10 Min + Verifizierung
   - Kategorie: Medical/Health → Alternative or Complementary Medicine
   - Schritte: mit Apple-ID anmelden → Business suchen/anlegen → Daten prüfen → Verifizierung (Telefon/Doku).
3. **Foursquare** — `https://foursquare.com/venue/claim` · ~10 Min
   - Kategorie: Health & Medicine → Alternative / Holistic Health
   - Schritte: Listing suchen → claimen → Inhaberschaft bestätigen. Kostenlos ($20-Upsell ignorieren).
4. **TomTom** — `https://www.tomtom.com/mapshare/tools/` · ~10 Min (oder auto via GBP)
   - Kategorie: Health Care / Practitioner
   - Schritte: MapShare → „Single company" → Konto → Firmendaten. Bei sauberem GBP evtl. schon da.
5. **Facebook Page** — `https://www.facebook.com/pages/create` · ~15 Min
   - Kategorie: Medical & Health → Alternative & Holistic Health Service
   - Schritte: Seite anlegen → Kategorie → NAP → veröffentlichen.
6. **HERE** — `https://mapcreator.here.com` · gering
   - Kategorie: Health / Medical
   - Schritte: WeGo-App „Suggest an edit" oder Map Creator. Geringster Wert — nur wenn Zeit.

## 7. Prefill-Felder (aus `client_locations`, überall identisch)
Name · Straße (deutsche Reihenfolge „Straße Nr.") · PLZ Ort · Land · Telefon ·
Website · E-Mail · Kategorie (`primary_category`, pro Portal nächste Entsprechung) ·
Öffnungszeiten (`hours`) · Beschreibung (`description`).

NAP-Konsistenz ist Pflicht: überall exakt gleich.

## 8. Schon gebaute Assets (wiederverwenden)
- `reporting/aggregator-pack.mjs` — Generator; baut aus `client_locations` den
  Einreichungs-Pack je Kunde (`--client <id>`). Gleiche Daten/Texte wie diese Spec.
  Kann als Vorlage für den Seed und als Admin-Export dienen.
- `00_project/coralie-aggregator-pack.md` — Beispiel-Output für Coralie.

## 9. Grenzen (wichtig)
- Kein Auto-Submit. Das Modul führt + trackt, es reicht nicht selbst ein.
- Verifizierung braucht die Kunden-Logins (Apple-ID, Microsoft). Darum Selfservice.
- Manuelle Verzeichnis-Einreichungen (Layer 2, DE-Longtail) laufen weiter über
  BrightLocal — nicht Teil dieses Selfservice-Moduls.
