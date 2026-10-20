# System: Tägliche Vorher/Nachher-Stories (Local-Falcon-Ergebnisse)

**Ziel:** Jeden Tag automatisch eine „Kunden-Ergebnis"-Story (1080×1920) im 741-CI bereitstellen,
Team postet sie in ~30 Sek. mit @Mention-Sticker. 2 Wochen Vorlauf, danach Recycling.

**Modell für die Automation:** Sonnet (`claude-sonnet-5`) — reicht fürs Bild-Bauen, günstiger; Opus nur wenn strategisch mitgedacht werden muss.

**Entscheidungen (11.08.2026):**
- **Posting:** „Morgens-fertig, ihr tippt" — Erstellung + Queue laufen automatisch, der letzte
  Schritt (Posten + @Mention-Sticker) ist ein manueller Tipp. Grund: Story-@Mentions gehen
  über keine offizielle API zuverlässig.
- **Lieferung:** Telegram-Bot **@Socials741_bot** (Token in `.secrets/telegram-741.env`, validiert 11.08.2026). Chat-ID noch offen (Martin muss dem Bot einmal schreiben).

**Posting-Accounts (nach Sprache):**
- **EN** → Instagram **@741.studio**
- **DE** → Instagram **@heymartin.seo.agentur**
Jede Story bekommt in der Queue eine Sprache → landet auf dem richtigen Account.
Der **zu taggende Kunden-@** ist davon getrennt und kommt mit der Kunden-Datenbank (s. u.).

---

## Datenquelle (kein Screenshot nötig)

Für getrackte Kunden: **direkt aus Local Falcon** (MCP). 49 Standorte sind bereits im Account.
- `listAllLocalFalconLocations` → Kunde finden (Place ID, lat/lng, Name)
- `listLocalFalconScanReports` / `getLocalFalconReport` → Grid-Werte, Keyword, Center, Datum
- **Vorher** = ältester relevanter Scan, **Nachher** = neuester Scan desselben Keywords.
- `center`, `spacingKm`, `rows` kommen 1:1 aus dem Report → Karte zentriert exakt richtig.

**Screenshots (Drive-Ordner)** nur noch für Ausnahmen: Alt-Daten aus anderen Tools
(z. B. Maria Abel 2023). Ordner: Google Drive `Story-Automation/screenshots-extern/`.
Dann liest Claude die Werte beim Batch-Bau aus dem Bild ab.

## Bausteine

1. **Template:** `07_social/templates/before_after_story.html` (Master, generisch).
   Pro Kunde eine Kopie `before_after_<kunde>.html`, nur `CONFIG` getauscht. Echte Karte
   via Leaflet+CARTO. Aufbau: Titel · Keyword+Ort · Vorher/Nachher-Karte · 2 Stats ·
   Proof-Zeile (andere echte Cases) · CTA „Alle Cases auf 741.studio". Details:
   `prompt-before-after-story.md`.
2. **Render:** Headless-Chrome → `07_social/output/`, `--virtual-time-budget=30000`.
3. **Queue = Google Sheet „741 Story-Queue"** (noch anzulegen). Spalten:
   `Datum | Sprache (EN/DE) | Kunde | Place-ID | Keyword | Vorher-Scan-ID | Nachher-Scan-ID | Stat1 | Stat2 | Kunden-@ (tag) | Caption | Bild-Datei | Status (ready/posted) | Evergreen? (j/n)`
   Sprache steuert den Posting-Account (EN→@741.studio, DE→@heymartin.seo.agentur).
4. **Kunde→@-Mapping (zum Taggen):** Spalte `Kunden-@`. Kommt mit der Kunden-Datenbank
   (Martin baut sie gerade). Ist ein Kunden-@ unbekannt → Story ohne Tag ausliefern, Team ergänzt.
5. **Lieferung:** täglicher Cron → nimmt die nächste `ready`-Zeile, schickt Bild + Caption +
   „tagge @handle" nach Telegram, setzt nichts auf `posted` (Martin bestätigt oder ignoriert).

## Ablauf

**Batch (alle 2 Wochen, halbautomatisch, Claude):**
1. Für jeden aktiven Kunden neuesten + Vergleichs-Scan aus Falcon ziehen.
2. Nur Kunden mit echtem Fortschritt (Vorher schlechter als Nachher) aufnehmen —
   sonst kein „Ergebnis". Keine erfundenen Zahlen.
3. Client-HTML rendern, PNG in Drive `Story-Automation/ready-to-post/`.
4. Zeile in „741 Story-Queue" mit Datum (nächste freie Slots), Caption, Handle, Status=ready.

**Täglich (Cron, automatisch):**
- Nächste `ready`-Zeile mit Datum ≤ heute → Bild+Caption+Handle nach Telegram.
- Queue leer? → älteste `Evergreen=j` erneut einplanen (recyceln).

**Manuell (Team, ~30 Sek.):**
- Bild aus Telegram speichern → Story hochladen → @Mention-Sticker setzen → posten.
- Optional in der Sheet Status auf `posted` setzen.

## Guardrails

- **Nur echte Daten.** Ränge/Stats immer aus Falcon. Fehlt eine belastbare Zahl → Kunde
  überspringen, nicht schätzen.
- **Einverständnis:** Kunde muss OK sein, öffentlich als Ergebnis gezeigt zu werden.
  Für Website-Cases (Laserstein/Schlirf/Abel/Lengauer) gegeben. Neue Kunden vorher freigeben.
- **Kein Media-Buyer-Ping** ([[no-messages-to-media-buyer]]) — Lieferung geht an Martin/Team.

## Auto-Posting (Feed-Carousels, voll automatisch)

- **Weg:** Instagram Graph API über n8n. Feed-Carousels mit Caption = 100 % hands-off; nur Kunden-Stories mit @Mention bleiben halb-auto (Telegram-Tap).
- **Voraussetzungen (Martins Part, weil Login/OAuth):**
  1. @heymartin.seo.agentur auf **Business** umstellen (Einstellungen → Konto-Typ → Business).
  2. Mit einer **Facebook-Seite** verknüpfen (Pflicht für Content-Publishing-API).
  3. **Meta-App** + langlebiger Token (System-User); ggf. App-Review für `instagram_content_publish`.
  4. **Öffentlicher Bild-Ordner** (741-Server) — API holt Bilder per URL.
- **Claude baut danach:** n8n-Flow (Queue → Bild-Upload → Carousel-Container → publish mit Caption), Caption-Pipeline, Bild-Hosting-Anbindung.
- **Bild-Bibliothek:** Martin liefert GDrive-Ordner mit echten Fotos → Foto-Hintergrund-Option (`cover-photo`/`cta-photo`, Foto + Dunkel-Overlay) fest in `build_carousel.py` einbauen. Demo: `output/carousel_localseo/slide_1_photo.png`.

## Status / Offen

- [x] **Telegram-Bot** @Socials741_bot, Token in `.secrets/telegram-741.env`, validiert.
- [x] **Posting-Accounts** geklärt: EN→@741.studio, DE→@heymartin.seo.agentur.
- [ ] **Telegram Chat-ID:** Martin schreibt dem Bot einmal irgendwas → Claude holt die
      Chat-ID via `getUpdates` und trägt sie in `.secrets/telegram-741.env` nach.
- [ ] **Kunden-Datenbank** (Martin baut sie): pro Kunde Name · Falcon-Place-ID · Keyword ·
      Kunden-@ zum Taggen · Sprache · Freigabe (dürfen wir zeigen?).
- [ ] **Startliste:** welche der 49 Falcon-Standorte in die erste 2-Wochen-Rotation.

→ Sobald Chat-ID + Datenbank da sind, baut Claude die erste 2-Wochen-Charge als Proof.
