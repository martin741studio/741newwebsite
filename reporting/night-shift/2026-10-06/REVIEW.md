# Night Shift 2026-10-06 — 6 pages · 5 pass · 1 needs_martin · 0 skipped

## Praxis Suriya
- [ ] freigeben  **GBP-Profil — Öffnungszeiten / Termin-Button / Barrierefreiheit** (FEEDBACK) — pass
      → feedback/praxis-suriya/7fd15e89-27b8-426c-a28a-d88998ef37b1.md · Top-Fixes: —
- [ ] freigeben  **NAP / Citations / Domains** (FEEDBACK) — pass
      → feedback/praxis-suriya/d1c58471-eafc-4ef9-8418-1611a2345445.md · Top-Fixes: —
      Hinweis: Such-Volumen für "Ayurveda Ingelheim" vs. "Ayurveda Mainz" fehlt noch (DataForSEO nicht abrufbar). Vorschlag markiert dies als [fehlt:], keine Zahl erfunden.
- [ ] freigeben  **GBP-Empfehlung — Beschreibung** (FEEDBACK) — pass
      → feedback/praxis-suriya/21a25f8b-8ee2-4f8f-8378-36aac01e35c4.md · Top-Fixes: —
      Hinweis: Text ist der Kundentext 1:1 (Ersetzung, keine Neufassung). Länge 669/750 Zeichen, HWG-Scan sauber.

## Rabenmütter Shop
- [ ] freigeben  **Seitenbaum — Zusätzliche Verkaufskanäle** (FEEDBACK) — pass
      → feedback/rabenmuetter-shop/66478f5c-02a4-4076-b1c3-ad9d211e3533.md · Top-Fixes: —
      Hinweis: Pinterest-Shop-Status bleibt als Kundenangabe ("hoffe ich") markiert, nicht als bestätigte Tatsache übernommen.
- [ ] freigeben  **Seitenbaum — Trauerkarten (Pillar)** (FEEDBACK) — pass
      → feedback/rabenmuetter-shop/801d4d7d-1a22-4d45-a08e-e0b213dff2ec.md · Top-Fixes: —
      Hinweis: Enthält zwei Umsetzungsmodelle (A: Handschrift-Schriftart, B: echte Handschrift) als Antwort auf die Kundenfrage. Martin muss ein Modell wählen, bevor der Kunde die finale Antwort erhält.
- [ ] freigeben  **Trauerkarten-Kollektion (Hub)** (CREATE) — needs_martin (Versuch 2/2, Critic-Lauf für Versuch 2 ausgelassen gemäß Eskalationsregel aus Versuch 1)
      → specs/rabenmuetter-shop/trauerkarten-kollektion-hub.md
      Fails: JSON-LD fehlt komplett · Rubrik-Dimensionen unter 80: 1 Search-Intent=70, 2 Themen-Tiefe=15, 3 GEO-Extrahierbarkeit=40, 4 E-E-A-T=20, 7 Schema=0, 8 Interne Links=55
      Ursache: Kein DataForSEO-Zugriff und WebFetch auf rabenmuetter-verlag.de schlägt mit Tool-Fehler fehl, bevor Seiteninhalt lädt. 5. Fall in Folge (09-16, 09-22, 09-28 ×2, heute Nacht). Kein Problem der Textqualität — der Executor hat korrekt keine Daten erfunden.
      Martin: [ ] DataForSEO-Zugriff für diese Session klären  [ ] rabenmuetter-verlag.de per Hand prüfen (Kategorie-Namen, bestehende Trauerkarten-URLs)  [ ] 3–5 echte FAQ-Fragen liefern  [ ] Ansprechperson/Impressum-Angabe für E-E-A-T liefern

## Offene Punkte außerhalb der Seiten
- `processed-feedback.json` ist weiterhin leer (`[]`). Seit dem Lauf vom 09-16 gemeldet: der Tagesablauf trägt erledigte Feedback-IDs nicht ein. Risiko: dieselben 5 Feedback-Punkte können in einer künftigen Nacht erneut in die Queue rutschen, sobald sie nicht mehr in `processed-feedback.json` ausgeschlossen sind.
- Der DataForSEO/WebFetch-Blocker für Rabenmütter Shop ist jetzt 5× bestätigt. Ein weiterer Nacht-Versuch für diese Seite bringt vermutlich kein anderes Ergebnis. Empfehlung: Seite aus der automatischen Queue nehmen, bis Martin die Daten von Hand liefert.
