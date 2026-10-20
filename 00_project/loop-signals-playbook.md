# Loop-Signals-Playbook — Standard für alle Citation-Arbeiten

Ziel: nicht nur Einträge anlegen, sondern ein **Co-Citation-Netz** bauen, das Google + LLMs
die Echtheit einer Brand beweist. Gilt ab sofort für jeden Kunden. Quelle: Martins Strategie
(2026-08-25), hier als umsetzbare Regeln destilliert.

## 1. Image-Loop-Hack (Bilder als lokale Signale)
Bei jedem Bild-Upload (GBP, Yelp, Bing, Foursquare, Apple):
- **Dateiname-Formel:** immer `dienstleistung-stadtteil-brandname.jpg` (z. B. `akupunktur-ingelheim-praxis-suriya.jpg`). Nie `IMG_1234.jpg`.
- **EXIF-Geotag:** vor dem Upload echte GPS-Koordinaten der Praxis einbetten. Google liest sie beim Upload aus, auch wenn das Portal sie später strippt.
- **Caption-Loop:** in der Bildbeschreibung einen Entity-Loop schreiben, der auf ein ANDERES verifiziertes Profil verweist (z. B. „… mehr Berichte auf unserem verifizierten Google-Profil / Termin über unseren Google-Maps-Eintrag").
- **Visual Semantics:** echte Vor-Ort-Fotos (Praxisschild mit Brandname, Behandlungsräume) statt Stockfotos — liefert KIs visuelle Existenz-Beweise.

## 2. Co-Citation-Wheel (Verzeichnisse untereinander verlinken)
Profile NICHT isoliert nur auf die Startseite zeigen lassen. Kreislauf bauen:
- Facebook → Google-Maps-Review-Link
- Yelp → Apple-Maps-Profil oder spezifische Leistungsseite
- Website-Footer/Kontakt → strukturiert auf ALLE Haupt-Citations
- Jedes Profil verweist auf mind. ein anderes verifiziertes Profil → geschlossenes Vertrauens-Netz, schnellere Indexierung.

## 3. On-Click-PageRank-Shield (Review-Loop auf der Website)
Beste Bewertungen auf der Website spiegeln (`/reviews`), aber PageRank nicht verlieren:
- Reviews als Text/Grafik einbinden.
- Verifizierung per JavaScript-On-Click statt `<a href>`:
```
<div class="review-card" onclick="window.open('GBP_REVIEW_LINK','_blank');">
  "Zitat der Bewertung …"
</div>
```
- Effekt: echte Nutzerreisen zur Quelle werden registriert, Crawler folgen dem Event nicht → kein Linkjuice-Verlust. (Grauzone-Technik; bewusst einsetzen.)

## 4. Ecosystem-Link-Loop (echte lokale Partner)
Nach den 2026-Updates zählen nur echte Partnerlinks, kein Citation-Spam.
- Komplementäre lokale Betriebe ansprechen (bei Coralie: Yoga-Studios, Bio-Cafés, Physios in Ingelheim).
- Content-/Ressourcen-Tausch: Expertenbeitrag für deren Blog mit präzisem Anchor (`Akupunktur Ingelheim`), Gegenerwähnung bei uns.
- Für Wettbewerber nicht kopierbar → maximale lokale Relevanz.

## 5. Branded-Keyword-Loop
- Social-Content (Reels/TikTok) animiert Nutzer, gezielt nach `Brand + Leistung` zu googeln
  (z. B. „Praxis Suriya Akupunktur Ingelheim").
- Effekt: Google koppelt Brand fest ans Service-Keyword → mit der Zeit Ranking auch fürs
  nicht-branded Keyword.

## Einbau in unseren Workflow
- **Submission-Runbook:** Dateiname-Formel + Caption-Loop + Geotag als Pflichtfelder je Bild-Upload-Schritt.
- **Portal-Selfservice:** Co-Citation-Wheel als Anleitung („verlinke Profil X auf Profil Y").
- **Website (money pages):** On-Click-Review-Shield + Footer-Citation-Block als Baustein.
- **Content-Plan:** Branded-Keyword-Loop + Ecosystem-Outreach als wiederkehrende Aufgaben.
- Health-Kunden: HWG beachten (keine Heilversprechen in Captions/Anchors).
