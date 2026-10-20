# MASTER-PROMPT: Ranking-Tracking je Kunde (Maps + Suche + Search Console)

Nutzung: Prompt unten kopieren, die vier Eingaben ausfüllen, in einem Chat im Kundenordner starten.
Rhythmus: Maps alle 2 Wochen (nach Umsetzungen). Organisch + GSC monatlich. Baseline = erste Messung.

---

## PROMPT

Du erstellst die Ranking-Messung für einen 741-Kunden. Du dokumentierst drei Ebenen: Google Maps, organische Suche, Search Console. Du prüfst außerdem, ob die wichtigsten Keywords wirklich auf der Website stehen.

### Eingaben
- Kunde: [Name]
- Domain: [https://…]
- GBP Place-ID: [ID oder "suchen"]
- Stichtag: [Datum]

### Regeln
1. Keine Annahmen. Jede Zahl kommt aus einem Tool. Fehlt eine Zahl, schreibe "fehlt" und nenne die Ursache.
2. Schlägt ein Abruf fehl, wiederhole ihn mit anderem Wortlaut. Ein Timeout heißt nicht "nicht vorhanden".
3. Scans kosten Credits. Lies zuerst vorhandene Reports (kostenlos). Neue Scans nur nach Martins Go. Nie einen Scan wiederholen (er ist dann doppelt in der Warteschlange).
4. Keine Tool-Namen auf der Kundenseite. Schreibe "Maps-Messung" und "Google-Daten".
5. Nichts geht ins Kundenportal ohne Martins Freigabe.

### Schritt 1: Die 5 Fokus-Keywords bestimmen
- Hole das GBP: Titel, Primärkategorie, Zusatzkategorien, Leistungen (Local Falcon `listAllLocalFalconLocations`, `listLocalFalconGbpServices`).
- Wähle die 5 wichtigsten Leistungen. Priorität haben Leistungen, die im GBP-Titel oder in der Primärkategorie stehen.
- Das Keyword muss die echte Leistung treffen (Public Affairs ist nicht PR).
- Prüfe Suchvolumen mit DataForSEO. Bei Volumen 0 sind die Daten oft nur dünn. Prüfe das Keyword dann über Google Autocomplete. Ersetze es nur, wenn es keine echte Suche gibt.
- Nutze für jede Messung genau diese 5 Keywords, damit die Verläufe vergleichbar bleiben. Änderungen schreibst du mit Datum und Grund auf.

### Schritt 2: Google Maps (Local Falcon)
- Lies zuerst `listLocalFalconScanReports` für die Place-ID. Nutze vorhandene Reports.
- Für jedes Keyword ohne aktuellen Report: Scan-Vorschlag mit Kosten an Martin (7×7, 5 km, google, 49 Credits je Scan). Starte nach Go.
- Poll mit `getLocalFalconReport`. Fieldmask: `keyword,arp,atrp,solv,found_in,image,heatmap,places.*`.
- Halte je Keyword fest: Datum, Grid-Größe, Radius, ARP, ATRP, SoLV, found_in, Top-3-Wettbewerber (Name, SoLV, ARP, Reviews, Rating).
- Prüfe das Grid-Bild visuell. Pins müssen sichtbar sein. Ist die Karte leer, nutze das Feld `heatmap`.
- Speichere das Bild mit Datum im Dateinamen. Überschreibe nie ein altes Bild.
- Berechne die Veränderung zur letzten Messung (ARP, SoLV).

### Schritt 3: Organische Suche (kein Maps)
- Nutze DataForSEO SERP (kein Ahrefs). Gerät: mobil. Standort: Stadt des Kunden. Sprache passend zum Markt.
- Für jedes der 5 Keywords und jeweils die Variante "Keyword + Stadt":
  - organische Position des Kunden
  - rankende URL
  - Top-3-Domains
  - SERP-Features (Local Pack, AI Overview, "Weitere Fragen", Videos)
- Ist der Kunde nicht in den Top 100, schreibe "nicht in Top 100". Rate keine Position.
- Optional monatlich: KI-Sichtbarkeit (Scans chatgpt / gemini / gaio / aimode, mit zitierten Quellen).

### Schritt 4: Search Console
- Nutze `scripts/gsc-client-export.mjs <siteUrl> 28`. Prüfe zuerst mit `--list`, ob die Property freigegeben ist.
- Antwortet der Abruf mit 403: Stopp. Sage Martin, dass er `reporting-bot@studio-apis-503306.iam.gserviceaccount.com` in der Search Console als Nutzer ("Uneingeschränkt") hinzufügen muss. Achte auf Property-Typ: URL-Präfix oder Domain.
- Halte je Fokus-Keyword fest: Impressionen, Klicks, CTR, Ø Position, rankende URL. Vergleiche 28 Tage mit den 28 Tagen davor.
- Erscheint das Keyword gar nicht? Notiere das als "keine Impressionen".
- Prüfe Kannibalisierung: Ranken mehrere URLs für dasselbe Keyword?
- Liste Chancen: Keywords mit mindestens 20 Impressionen und Position 8 bis 30.
- Liste die 10 stärksten Suchanfragen, die NICHT zu den 5 Keywords gehören. Schlage vor, ob eine neue Seite oder Ergänzung nötig ist.

### Schritt 5: Ist das Keyword auf der Website umgesetzt?
Rufe die Ziel-URL live ab. Prüfe je Keyword: Title, Meta-Description, H1, URL, erster Absatz, mindestens eine H2, Alt-Text eines Bildes, interne Links auf die Seite.
Ergebnis je Feld: ✓ vorhanden, ✗ fehlt, ⚠ nur ähnlich (nenne den echten Text).
Hat ein Keyword keine eigene Zielseite, schreibe das deutlich als Lücke.

### Schritt 6: Zusammenführung
Eine Haupttabelle, eine Zeile je Keyword:

| Keyword | Maps ARP | Maps SoLV | Δ | Organisch Pos. | GSC Impr. | GSC Klicks | GSC Ø Pos. | On-page (Title/H1/Meta/URL) | Ziel-URL |

Darunter:
1. Drei Sätze: Was hat sich verbessert, was nicht, was ist die wahrscheinliche Ursache (nur mit Datenbeleg).
2. Die 3 wichtigsten nächsten Maßnahmen (Priorität nach Hebel).
3. Offene Punkte, die Credits, Zugänge oder Martins Go brauchen.

### Schritt 7: Ablage
- Eine Zeile je Messung in der Tabelle `scans` (741-portal): keyword, date, arp, solv, found_in, Wettbewerberwerte, Bild-URLs, `approved_by_martin=false`.
- Grid-Bilder per FTP unter `clients.741.studio/r/<hash>/scans/<datum>-<keyword-slug>-grid.png`.
- Lokaler Report als Markdown mit Datum im Dateinamen.
- Die Kundenseite bekommt den Block "Ranking-Tracking: datierte Messungen" erst nach Freigabe.

### Ausgabe an Martin
1. Die Haupttabelle.
2. Die 3 Maßnahmen.
3. Eine fertige Status-Nachricht an den Kunden in Martins Ich-Form, du-Ansprache, ohne Call-Angebot und ohne Fragenliste.
