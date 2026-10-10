# Lokale-Relevanz-Klassifikator — Prompt für Process B (Schritt 1.3)

Adaptiert aus Quelle 098 (`link-library/098-...md`) für den 741-Workflow: DataForSEO statt Ahrefs, DACH statt US, Output direkt in unser `targets.md`-Zeilenformat statt eigener Bucket-Listen. Nicht wörtlich übernommen — eigene Fassung, auf unsere Tabellenstruktur zugeschnitten.

**Zweck:** einen rohen Referring-Domains-Export (Process B, Schritt 2) automatisch in lokal-relevant/regional/national/Spam vorsortieren, BEVOR von Hand gescored wird. Ersetzt das manuelle Durchscrollen.

**Einsatz:** Agent füllt die eckigen Klammern, hängt die rohe Domain-Liste an, lässt sich selbst (oder ein frisches Subagent) den Prompt beantworten, übernimmt nur Zeilen mit „Confirmed local" in `targets.md`.

---

```
Du prüfst eine Liste von Referring Domains auf echte geografische Relevanz für ein lokales Unternehmen.

ZIEL-KONTEXT
- Stadt/Region: [STADT]
- Branche: [BRANCHE]
- Referenz-Standort für Nähe-Bewertung: [ADRESSE DER PRAXIS/DES GBP-EINTRAGS]
- Ziel-Domain des Kunden: [DOMAIN]

WAS ZÄHLT ALS LOKAL
Eine Quelle ist lokal relevant, wenn ihre Community, ihr Publikum, ihr Standort, ihre Mitglieder oder ein konkretes lokales Projekt nachweisbar mit [STADT]/[REGION] verbunden sind.
Ein Stadtname in der Domain macht sie NICHT automatisch lokal. Das Fehlen eines Stadtnamens schließt sie NICHT automatisch aus.
Trenne echte lokale Quellen von nationalen Verzeichnissen mit Stadt-Unterseiten — die gehören separat gelistet, nicht in die Hauptrangliste.

FESTE PRIORITÄT (keine Mischung aus Score und Reihenfolge)
1. IHK/HWK — NUR wenn die Branche des Kunden tatsächlich IHK-/HWK-pflichtig ist (bei freien Berufen wie Heilpraktiker, Architekt, Arzt: NICHT zutreffend, dann entfällt diese Stufe ersatzlos — nicht durch den Berufsverband auffüllen, der steht unter 2).
2. Branchenverband / Nischen-Verzeichnis mit nachgewiesenem Fach- UND Orts-Bezug.
3. Alles andere mit verifizierter Orts-Nähe, sortiert nach Entfernung zur Referenz-Adresse — je näher am Standort, desto weiter oben. Keine Autoritäts-Metrik darf diese Reihenfolge überstimmen.

REGELN
- Jede Einstufung braucht einen Beleg (welche Seite, welcher Hinweis) — kein Name-Raten. Unsichere Fälle kommen unter „Needs verification", nie unter „Confirmed local".
- Domain-Rank/Traffic ist KEIN Lokalitäts-Filter — ein Rank nahe 0 heißt Spam-Verdacht (separat flaggen), nicht automatisch „nicht lokal".
- Mutterfirma/Tochterdomain/Redirect nach Übernahme separat kennzeichnen, nicht als unabhängige lokale Quelle werten.
- Keine erfundenen Entfernungen oder Adressen — nur verifizierbare Angaben.
- Zeig jeden Treffer, nicht nur die Top 10.

OUTPUT — direkt als targets.md-Zeilen
Für jede „Confirmed local"-Domain: Domain | Priorität (1/2/3) | Kategorie | Beleg in einem Satz | Nähe-Label (gleiche Straße/Stadtteil/Stadt/Region/unbekannt)
Separat darunter: Regional/National-mit-Lokalseite/Zugehörig-Dupliziert/Needs verification — je eine kurze Liste, nicht in die Hauptrangliste gemischt.
Abschluss: wie viele Domains geprüft, wie viele in welcher Kategorie — Summe muss aufgehen.

DOMAIN-LISTE:
[EXPORT EINFÜGEN]
```
