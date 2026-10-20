# Schreib-Briefing: <Seite> für <Kunde>

Zwei Teile. Teil A ist das deutsche Formular für Martin (und, wenn Martin es freigibt, für den Kunden). Teil B ist die Maschinen-Version `brief.json`; Felder siehe `content-writing-brief.schema.json`. Der Agent füllt vor, was die Daten hergeben. Martin ergänzt nur Lücken.

## Teil A: Formular

**1. Auftrag**
- Kunde / Seite oder Thema: …
- Seitentyp: Startseite · Leistungsseite · Ortsseite · Behandler- oder Anwaltsseite · Kostenseite · FAQ-Seite · Blogbeitrag
- Modus: neu · Überarbeitung einer bestehenden Seite (Bestand-URL: …)
- Sprache: Deutsch · Englisch
- Rechtsmodus: Heilmittelwerbegesetz (HWG) · Anwaltsrecht (BRAO/UWG) · keiner
- Pool-Einträge (IDs): CP-…, CP-… (Sitemap-Knoten: ST-…)

**2. Leser und Ziel**
- Wer liest das? Welche Frage hat die Person, in welchen Worten? …
- Was soll danach passieren? (Ziel) …
- Kontaktweg: WhatsApp · Telefon · Formular · Buchung · E-Mail (Hinweis: bei Anwälten und Ärzten ist WhatsApp oft ausgeschlossen)
- Text des Haupt-Buttons: …
- Beruhigungszeile unter dem Button: …

**3. Suche**
- Haupt-Keyword (Menge, Quelle, Datum): …
- Weitere Keywords: …
- Stadt (nur lokale Seiten): …
- Interne Links (Ziel-Seite, Ankertext): …

**4. Stimme**
- Stimmprofil: `voice.md` vorhanden? ja/nein. Anrede: du / Sie. Sprecher: ich / wir / dritte Person.
- Eigene Wendungen, die bleiben: …
- Wörter, die nie vorkommen: …

**5. Belege, die wir zeigen dürfen**
- Bewertungen (Zahl, Quelle, Freigabe): …
- Titel und Qualifikationen (mit Beleg): …
- Zahlen, die der Kunde bestätigt hat: …
- Fotos: …

**6. Blogbeitrag zusätzlich**
- Autor mit Titel: … · Seite der Person: … · Prüfdatum: …
- Money-Seite, auf die der Beitrag verlinkt: …

**7. Offen beim Kunden (gelbe Platzhalter erlaubt)**
- Preise · Jahre · Titel ohne Beleg · Zitate · Notfallnummern · …

**8. Nicht**
- Verbotene Wörter und Themen: …

## Teil B: brief.json (Auszug)

```json
{
  "client": "STÜRZL Steuerstrafrecht", "client_slug": "stuerzl", "page_slug": "selbstanzeige",
  "page_type": "service", "mode": "rewrite", "language": "de", "address": "sie", "speaker": "wir",
  "legal_mode": "BRAO", "voice_sheet": "00_project/assets/stuerzl/voice.md",
  "pool_item_ids": ["CP-SVC-009", "CP-SVC-010"], "sitetree_node": "ST-14",
  "keyword_primary": "selbstanzeige anwalt", "local_city": null, "intent": "commercial",
  "cta": {"goal": "Vertrauliche Anfrage", "channel": "form", "text": "Vertraulich anfragen",
          "reassurance": "Nennen Sie uns nur Ihr Thema, keine Einzelheiten."},
  "sections": [{"id": "S01", "element": "hero", "job": "…", "cta": "primary"}],
  "gate": "A0-full", "money_page": true, "bestand_words": 248, "benchmark_median_words": null,
  "faq_min": 5, "internal_links_min": 3, "cta_min": 3, "cta_text": "Vertraulich anfragen",
  "forbidden_words": ["spezialisiert", "Experte"], "blockers": []
}
```
