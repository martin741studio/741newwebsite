# me&you: Website-Struktur (Stand 05.10.2026)

Quelle: Copy Deck Round 3 (29.09.2026), Design-Richtlinien (Ehlers.pdf), Feedback zur Persona-Präsentation.
Prototyp v2: https://claude.ai/artifact/DpyEL5pa1Bc42nT8z1kCyx (privat). Code: `00_project/assets/meandyou/prototype-v2/`.

## Seitenbaum

```
Home                       index.html
├── Seminare               seminare.html      (Money-Page, keine Preise)
├── Über Michael           michael.html
├── Was ist Rhetorik       rhetorik.html      (Einstieg, Soft-CTA "Kostenloses Training ansehen")
├── FAQ                    faq.html
├── Gespräch buchen        besteht heute als /seminare-termin
└── Impressum · Datenschutz · AGB

Nicht in der Navigation (Anzeigen-Traffic):
├── Landingpage Replayers  lp-replayers.html
├── Landingpage Overlooked lp-overlooked.html
├── Landingpage Undersold  lp-undersold.html
└── Landingpage Coaches    lp-coaches.html    (ENTWURF, nicht freigegeben)
```

Navigation: Seminare · Michael · Was ist Rhetorik · Stimmen · FAQ + Button "Gespräch buchen".

## Blöcke je Seite (ein Block = ein Bildschirm)

| Seite | Blöcke |
|---|---|
| Home | Hero (Kampagne an/aus) · Drei Situationen · Warum Michael (Zahlen, Video) · Die Methode · Seminar-Teaser · Stimmen · Gespräch buchen |
| Seminare | Hero · Der Einstieg [Seminar A] · Die Formate [B, C, D] · Drei Tage, zwölf Menschen · Orte · Für wen · Gespräch buchen |
| Über Michael | Hero · Autorität (Zahlen, Auszeichnung, Medien) · Gespräch buchen |
| Was ist Rhetorik | Hero mit Soft-CTA · Methode + Platzhalter Training · Gespräch buchen |
| FAQ | 13 Fragen (Ist-Texte) · Gespräch buchen |
| Landingpages | Hero in Persona-Farbe · Warum Michael · Methode · Stimmen · Gespräch buchen |

## Wo die drei Personas erscheinen

- **Home, Block 2:** drei Situationen unter einer Überschrift. Jede Karte hat die freigegebene Persona-Headline und das Persona-Foto aus der PDF.
- **Landingpages:** eine Struktur, drei Ausprägungen (Farbe, Foto, Headline).
- **Seminare-Seite:** keine Personas. Sie gehört zur Welt "The Undersold" (Ort und Gruppe führen).

## Entscheidungen im Prototyp (Vorschlag, noch nicht bestätigt)

1. **"Stimmen" in der Navigation** führt zum Stimmen-Block auf Home. Das Copy Deck hat keine eigene Stimmen-Seite.
2. **"Mehr dazu →"** unter jeder Situation führt zur Landingpage dieser Persona. Das Copy Deck nennt kein Ziel.
3. **Button-Farbe:** Taubenblau aus der PDF. Das Copy Deck nennt Ultramarin. Die PDF ist die Design-Quelle, deshalb bleibt Taubenblau, bis Martin anders entscheidet. Der Wert steht an einer Stelle (`--dove`).
4. **Stimmen-Block:** zeigt die vier echten Kundenzitate. Das Format "Vorher. Nachher." braucht echte Fälle, die noch fehlen.
5. **Orte:** Ortsname echt, Monat als Platzhalter (Copy Deck: keine Termine, bis der Kunde bestätigt).

## Produktleiter: Platz auf der Website (Vorschlag)

| Stufe | Produkt | Persona-Welt | Platz |
|---|---|---|---|
| 1 | Kostenloses Training | Replayers | Seite "Was ist Rhetorik" (Soft-CTA), Landingpage Replayers |
| 2 | Buch, Community | Replayers | Seite "Was ist Rhetorik", Block unter dem Training. Im Copy Deck noch nicht enthalten. |
| 3 | Onlinekurs | Overlooked | Landingpage Overlooked, Seite "Über Michael" oder eigene Kurs-Seite. Im Copy Deck noch nicht enthalten. |
| 4 | Seminare | Undersold | Seite "Seminare", Home-Teaser |
| 5 | Premium / Executive | Undersold | Im Gespräch, nicht auf der Seite |

## Bilder: Zuordnung

| Stelle | Bild | Quelle |
|---|---|---|
| Home Hero, Video-Standbild, Über Michael, Was ist Rhetorik | Michael (5 Motive) | Echt, von meandyou.de |
| Situation 1, Landingpage Replayers | Frau am Schreibtisch, Bahn-Szene | Ehlers.pdf, Seiten 5 und 6 |
| Situation 2, Landingpage Overlooked, Coaches-Entwurf | Glastisch-Gespräch, Mann am Fenster | Ehlers.pdf, Seiten 9 und 10 |
| Situation 3, Landingpage Undersold, Seminare "Einstieg" und "Drei Tage" | Handschlag-Runde, Gruppe am Holztisch | Ehlers.pdf, Seiten 13 und 14 |
| Seminar-Teaser, Orte, Abschluss, Seminare-Hero | Mallorca, Barcelona, Dubai, Gruppe, Abend-Küste | ChatGPT, nach den Fotoregeln der PDF |

Die PDF-Fotos sind Ausschnitte aus 920 × 514 px großen Seiten und zweifach hochskaliert. Sie sind unscharf, sobald sie groß stehen. Für den echten Bau brauchen wir die Originaldateien.

## Offen

- Seminarnamen, Schwerpunkte, Definition des Einstiegs-Seminars (Kunde).
- Hero-Video und Autoritäts-Video (Kunde).
- Echte Vorher-Nachher-Fälle (Kunde, Pauspapier).
- Prüfen: "Top 100 Speaker" und "5 Bücher" im Copy Deck. Die Ist-Seite sagt "Top 100 Trainer" und "Top10 Speaker".
- Du/Sie: Situation 3 nutzt "Ihr Unternehmen", der Rest "du" (im Copy Deck als offene Frage markiert).
- Ziel-Link für "Kostenloses Training ansehen".
- FAQ-Texte sprechen vom Online-Kurs. Für die neue Seite braucht es Seminar-Fragen.
