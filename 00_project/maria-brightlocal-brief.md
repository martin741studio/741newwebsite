# BrightLocal Citation Builder — ShuiGuru / Maria Brasse (Stand 08.10.2026)

Vorgehen wie bei Coralie (Campaign 994242, 25 Manual, $80): **25 Verzeichnisse**, Duplikat-Entfernung AUS (Maria hat außer GBP nichts), Aggregators N/A, Standard-Turnaround. Kauf = Martin.

## Stammdaten (1:1 einfügen — identisch zum GBP)
- **Business Name:** ShuiGuru - Maria Brasse
- **Adresse:** Warthestraße 29, 12051 Berlin, Deutschland (Berlin-Neukölln)
- **Telefon:** +49 1578 5955528
- **Website:** https://shuiguru.de
- **E-Mail (Listings-Identität):** shuiguru@listings.741.studio  ← Catch-all, Bestätigungsmails landen im Poller (`listing_emails`)
- **Kategorie primär:** Feng shui consultant / Feng-Shui-Beraterin · sekundär: Business management consultant, Building consultant, Educational consultant
- **Öffnungszeiten:** Mo–So 10:00–19:00
- **Logo:** https://shuiguru.de/wp-content/uploads/2022/12/cropped-cropped-CC1D9FBC-693E-4B53-B933-0B55840A5848.jpeg
- **Fotos:** https://shuiguru.de/wp-content/uploads/2026/09/maria-brasse-feng-shui-beraterin-portrait.jpg (echt, orange Jacke) · https://shuiguru.de/wp-content/uploads/2026/09/maria-brasse-feng-shui-beraterin-berlin-portrait.jpg (Kaffee)
- **Inhaberin:** Maria Brasse · Gründung: [fehlt: Jahr von Maria] · Zahlungsarten: [fehlt]
- **Social:** https://www.instagram.com/frieden_unterm_dach/ · https://de.linkedin.com/in/maria-brasse

## Beschreibung (GBP-Text, 740 Z., Sie-Form)
ShuiGuru ist die Feng-Shui-Beratung von Maria Brasse aus Berlin – vor Ort in Berlin und Brandenburg, online in ganz Deutschland. Ich arbeite mit schamanischem Feng Shui: mit den vier Himmelsrichtungen und den vier Elementen Luft, Feuer, Wasser und Erde. Mein Schwerpunkt sind Räume, die arbeiten müssen: Büros und Betriebe, Höfe und Gärten, Schulen und Institutionen, das Homeoffice – und Häuser schon vor dem Bau oder Kauf (Plancheck am Grundriss). Sie senden mir Fotos, Videos und Grundrisse, ich liefere Ihnen eine klare Analyse und konkrete, umsetzbare Schritte. Keine Deko-Tipps von der Stange, sondern Räume, in denen Menschen ruhiger arbeiten, leichter lernen und sich wohlfühlen. Der Start ist immer ein unverbindliches Vorgespräch.

## Kurzbeschreibung (für Felder mit Limit)
Feng-Shui-Beratung in Berlin & bundesweit: Büro, Garten & Hof, Schule, Plancheck vor dem Hausbau. Maria Brasse – konkret, praktisch, auch online.

## Verzeichnisse (25) — Häkchen manuell setzen, Spam-Filler abwählen
google.de · Yelp Deutschland · 11880.com · Cylex · goyellow.de · Hotfrog DE · Infobel · KennstDuEinen · Opendi · pointoo · Stadtbranchenbuch · Tupalo · oeffnungszeiten.com · onlinestreet.de · de.enrollbusiness.com · misterwhat.de · unternehmensauskunft.com · firmeneintrag.de · firmenindex-deutschland.de · branchenbuch24.com · branchenbuchdeutschland.de · Branchenbuch Deutschland · branchen-domain.de · branchen-info.net · marktplatz-mittelstand (B2B)
Reserve, falls eines nicht verfügbar: az-deutschland.com · branchenorte.de · business-branchenbuch.de · de.bizin.eu

## UI-Gotchas (aus Coralie-Order)
- Menge im Dropdown bestimmt den Preis: 10/15/25/35/50 × $3,20 (option-values 10→10, 15→11, 25→1, 35→16, 50→2); Häkchen nur innerhalb der Menge.
- „Show all 72" muss expandiert sein, sonst fehlen Zeilen im DOM. Selectize-Dropdown nur per korrekter option-value setzen.
- DE-A-Liste (Das Örtliche, Gelbe Seiten, Das Telefonbuch, meinestadt, GoLocal) ist bei BrightLocal NICHT verfügbar → Selbsteintrag über das Portal-Modul.

## Nach dem Kauf
Campaign-ID notieren → `reporting/import-brightlocal.mjs` bzw. SQL: 25 `client_citations` auf `submitted`, `submitted_via='brightlocal'`, notes='Campaign <ID>'. Citation-Logins später in `client_directory_accounts`.

## Stand 08.10.2026 — Bestellseite vorbereitet (Location 4172000, Step 2 offen im Chrome-Tab)
Warenkorb korrekt: **25× Manual Submissions = $80,00**, Aggregatoren AUS, Duplikat-Entfernung AUS. Liste „Show all 76" ist expandiert.
BrightLocal hat automatisch 25 nach „Authority" vorgewählt — 15 davon sind internationale Füller. **Von Hand umstellen (je ein Klick aufs Kästchen):**

**ABWÄHLEN (15):** maps.apple.com · trustburn.com · all.biz · storeboard.com · brownbook.net · ec21.com · cybo.com · trepup.com · yplocal.us · agreatertown.com · linkcentre.com · trustindex.io · top-rated.online · iformative.com · localstar.org

**BLEIBEN (10, schon angehakt):** google.de · provenexpert.com · tupalo.com · infobel.com · yelp.de · de.enrollbusiness.com · 11880.com · goyellow.de · homify.de · onlinestreet.de

**ANHAKEN (15):** hotfrog.de · oeffnungszeiten.com · misterwhat.de · unternehmensauskunft.com · firmeneintrag.de · firmenindex-deutschland.de · branchenbuch24.com · branchenbuchdeutschland.de · branchen-domain.de · branchen-info.net · business-branchenbuch.de · branchenorte.de · de.bizin.eu · az-deutschland.com · work5.de

Danach: Terms-Häkchen → „Continue to Payment". Vorher evtl. Banner „Check My Billing Address" (Steuerangaben) bestätigen.
Nicht im BrightLocal-Katalog (→ Selbsteintrag über Portal-Modul): Cylex, Das Örtliche, Gelbe Seiten, Das Telefonbuch, meinestadt, GoLocal, Opendi, pointoo, Stadtbranchenbuch, KennstDuEinen, marktplatz-mittelstand.
