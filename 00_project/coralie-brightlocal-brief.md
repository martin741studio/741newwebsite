# BrightLocal-Einreichungs-Brief — Praxis Suriya (Coralie)

Stand: 2026-08-24. Pilot-Kunde für das Citations-/Listings-Modul.
Kauf und Einreichung sind **Martins Aktion**. Dieses Dokument bereitet den Auftrag vor.

client_id: `3f71ef33-8c74-4ea1-b2d3-0273c2e99649`
BrightLocal location ID: `4139399` (Location angelegt 2026-08-25, Citation-Builder-Audit gestartet)

---

## 1. Kanonische NAP (Source of Truth aus `client_locations`)

BrightLocal muss diese Werte **exakt gleich** in jedes Verzeichnis eintragen.

| Feld | Wert |
|---|---|
| Business-Name | **Praxis Suriya – Ayurveda & Naturheilkunde** *(festgelegt 2026-08-24, in `client_locations` gesetzt)* |
| Inhaberin | Coralie Suriyapperuma |
| Straße | Schützenpfad 29 |
| PLZ | 55218 |
| Ort | Ingelheim am Rhein |
| Land | DE |
| Telefon | +49 174 7411087 |
| E-Mail | suriyapraxis@gmail.com |
| Website | https://suriya-praxis.de |
| Kategorie (primär) | Heilpraktiker |
| Kategorien (sekundär) | Akupunkteur, Massagetherapeut, Alternativmediziner, Ayurveda |
| Öffnungszeiten | Di/Mi/Do/Fr 09:00–19:00; Mo/Sa/So geschlossen; „nach Termin" |
| Instagram | suriya.ayurveda |

Kurzbeschreibung (für Verzeichnisse mit Textfeld):
> Naturheilpraxis in Ingelheim am Rhein: Heilpraktikerin Coralie Suriyapperuma behandelt Migräne, Kopf-, Nacken- & Kieferschmerzen sowie innere Unruhe – mit Akupunktur, Ayurveda, Vagusnerv-Regulation & Mikronährstoffmedizin. Ganzheitlich, persönlich, terminbasiert.

---

## 2. GBP-/NAP-Check VOR der Einreichung (Pflicht-Gate)

Ich habe das Live-Google-Listing am 2026-08-24 geprüft. Ergebnis: Kern-NAP sauber, aber **eine Entscheidung fehlt**.

**Sauber und konsistent (GBP = kanonisch):**
- Adresse: Schützenpfad 29, 55218 Ingelheim am Rhein ✓
- Telefon: +49 174 7411087 ✓
- Website: suriya-praxis.de ✓
- Bewertung: 5,0 (12) ✓
- Öffnungszeiten sind jetzt hinterlegt ✓ (waren am 2026-08-15 noch leer)

**Vor der Einreichung zu klären:**

1. **Business-Name — gestern festgelegt: „Praxis Suriya – Ayurveda & Naturheilkunde".**
   Kanonisch in `client_locations` gesetzt. Erledigt.
   Google zeigt Stand 2026-08-24 noch die alte Langform „Heilpraktiker Ingelheim I …".
   Google prüft Namens-Edits oft ein paar Tage. Kein neuer To-do — nur vor der Einreichung
   kurz prüfen, ob die Kurzform live ist. (Bindestrich: en-dash „–", überall gleich.)

2. **Kategorie.** Google führt die Praxis als „Naturheilpraktiker". Kanonisch steht „Heilpraktiker". Bitte auf einen Wert einigen.

3. **Öffnungszeiten.** GBP schließt 20:00, kanonisch 19:00. Bitte abgleichen.

> Regel: garbage in = garbage everywhere. Erst Name + Kategorie + Zeiten fixieren, dann Auftrag geben.

---

## 3. BrightLocal-Shortlist — Top 15 (DE, einmalig, kein Abo)

Auswahl-Logik: `method = brightlocal` und `country ∈ {DE}`. AT/CH-Verzeichnisse sind für einen DE-Standort raus.
Reihenfolge = tier (1 = Kern-Autorität, 2 = Longtail).

**Tier 1 — Kern-DE (8):**
1. Das Telefonbuch — https://www.dastelefonbuch.de/
2. Das Örtliche — https://www.dasoertliche.de/
3. Gelbe Seiten — https://www.gelbeseiten.de/
4. 11880.com — https://www.11880.com/
5. Cylex — https://www.cylex.de/
6. meinestadt.de — https://www.meinestadt.de/
7. Yelp Deutschland — https://www.yelp.de/
8. GoLocal — https://www.golocal.de/

**Tier 2 — DE-Longtail (7):**
9. Branchenbuch Deutschland — https://www.branchenbuch.de/
10. Hotfrog DE — https://www.hotfrog.de/
11. Opendi — https://www.opendi.de/
12. Yalwa — https://www.yalwa.de/
13. Stadtbranchenbuch — https://www.stadtbranchenbuch.com/
14. pointoo — https://www.pointoo.de/
15. KennstDuEinen — https://www.kennstdueinen.de/

**Phase 2 (optional, später):** Infobel, Tupalo, marktplatz-mittelstand (b2b, für eine Solo-Praxis am wenigsten relevant).

**Bewusst ausgeschlossen (falsches Land):** HEROLD (AT), firmenabc.at (AT), local.ch (CH), search.ch (CH).

### Kostenschätzung (einmalig)

- Basis: ~$2,00–3,20 pro Verzeichnis (aus Modul-Entscheidung, **bei Bestellung bestätigen**).
- 15 Verzeichnisse × $2,00–3,20 = **~$30–48 einmalig**.
- BrightLocal berechnet nur, was es wirklich einreichen kann. Manche Review-Seiten (z. B. Yelp) brauchen eine Inhaber-Verifizierung und fallen evtl. raus → echte Kosten eher am unteren Rand.
- Kein Aggregator-Zuschlag: die US-Datenaggregatoren greifen in DE nicht; Foursquare/HERE/TomTom machen wir selbst per API.
- **DE-Tiefe ist unbewiesen.** Dieser erste Auftrag testet, welche der 15 BrightLocal in DE wirklich abdeckt.

---

## 4. Was wir NICHT über BrightLocal machen

**Layer 1 — Aggregatoren, selbst per API (kostenlos, ~80 % Ranking-Wert):**
Google Business Profile (live), Bing Places, Apple Business Connect, Facebook, Foursquare, HERE Maps, TomTom.

**Layer 3 — Health-Nische, manuell durch uns:**
Heilpraktiker.de, arzt-auskunft, jameda, Doctolib, sanego, DocInsider, theralupa.
Für eine Heilpraktikerin zählen **Heilpraktiker.de + arzt-auskunft** am meisten. jameda/Doctolib sind arzt-fokussiert → Eignung prüfen.

---

## 5. Offene Punkte / Martins Aktionen

1. **BrightLocal-Plan prüfen** (Account existiert, Plan unklar). Zwei Dinge im Account bestätigen:
   (a) Der **Citation Builder** lässt einen neuen Build für **Deutschland** starten.
   (b) Der **Preis pro Verzeichnis** wird angezeigt (Einmal-Credits vs. Abo-Zwang).
   BrightLocal koppelt den Citation Builder teils an ein aktives Plattform-Abo. Wenn der Account ruht,
   ggf. nur Build-Credits kaufen, nicht zwingend ein Monats-Abo. Kurz gegenchecken.
2. **GBP-Name:** gestern geändert, kanonisch gesetzt. Nur prüfen, ob Google die Kurzform schon zeigt (aktuell noch Langform, evtl. in Google-Prüfung).
3. **DataForSEO-IP whitelisten** für den automatischen Monitor (fixe Dev-VPS-IP, nicht Laptop). Laptop-IP heute: 179.65.207.58 (dynamisch → nur als Übergang).
4. **Go zum Kauf** der 15 Verzeichnisse.

Nach Lieferung: BrightLocal-CSV mit `reporting/import-brightlocal.mjs` in `client_citations` importieren.
