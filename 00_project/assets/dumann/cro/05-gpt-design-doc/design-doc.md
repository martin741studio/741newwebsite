# GPT Design Doc — Naturheilpraxis Daniela Dumann, Startseite

Stand 2026-10-11. Quelle: `02-data/brand.md`, `03-diagnosis/diagnosis.md` (Pattern-Wahl), `04-copy/approved-copy.md` (exakte Texte). Alle Prompts werden per ChatGPT (Claude in Chrome, Martins Session) erzeugt, ein Chat für diese Praxis. Jeder Prompt beginnt mit dem Global Style Block.

---

## Global Style Block (vor jeden Prompt kopieren)

```
MARKE: Naturheilpraxis Daniela Dumann, Heilpraktikerin in Berlin-Charlottenburg,
Schwerpunkt Hildegard-von-Bingen-Heilkunde.

FARBEN: Primär Lila #783ca0, Sekundär Oliv #aabe1e, Hintergrund Creme #f8f3fb,
Dunkel/Text #5b2d80. CTA-Akzent konsequent EINE Farbe: Oliv #aabe1e auf Creme.

TYPOGRAFIE: Headline-Akzent in einer ruhigen, leicht geschwungenen Schrift (Pacifico-
Charakter), Fließtext in einer klaren serifenlosen Schrift (Poppins-Charakter). Hoher
Kontrast, keine helle Schrift auf unscharfem Fotohintergrund (das ist der Fehler der
echten Seite).

MOOD: traditionsreich, gelehrt, mütterlich warm, naturverbunden, ruhig. KEIN esoterischer
Kitsch, kein Verkaufs-Look, eher wie eine seriöse, warme Arztpraxis mit Naturbezug.

LAYOUT-PATTERN: P0-Blueprint mit P9-Hierarchiezug (siehe 741 CRO-Raster): Bild zuerst,
dann fetter Farbtitel in Markenfarbe, dann gedämpfter kleinerer Fließtext, dann ein
großer Button. Abwechselnd helle Creme-Bänder und ein dunkles Lila-Band für die
Vertrauens-Sektion.

LOOK DER ECHTEN PRAXIS (Referenzfotos sind angehängt): eine Frau Anfang 60, kurze
blondgraue Haare, warmes, offenes Lächeln, in den Referenzfotos mit floralem bzw.
grünem Oberteil. Das Idealbild soll SIE zeigen, im Stil der Referenzfotos, nicht eine
andere Person.

FORMAT: Hochformat 1024x1536 pro Sektion. Eine CTA-Farbe (Oliv). Keine Stockfoto-Optik,
kein aufgesetzter Verkaufston, kein erfundener finaler Text in großen Lettern (Text im
Bild ist nur Platzhalter, die echte Copy steht in approved-copy.md).
```

---

## Referenzfotos (an jeden GPT-Chat anhängen, einmalig zu Beginn)

1. `31df7b_94e35f7279034a34b858172a8af23d85~mv2.jpg` — Portrait, floral, warmes Lächeln (Hero-Hauptreferenz)
2. `31df7b_ba734fdcd1904d7ba8de6d32f4359d03~mv2.jpg` — Portrait, grünes Oberteil, warmes Lächeln (Zweitreferenz)
3. Logo-Wortmarke + Icon (für Farbwerte, nicht zum Nachbauen)

---

## Sektion 1 — Hero

```
[GLOBAL STYLE BLOCK]

Sektion 1, Hero. Layout: P0-Hero-Anatomie (Text/Bild-Split, Bild rechts oder als warmer
Portraithintergrund, Text links/oben).

Headline (exakt, als Platzhaltertext einbauen):
"Ihr Weg zu mehr Wohlbefinden, persönlich begleitet von einer Heilpraktikerin in
Berlin-Charlottenburg seit 2002"

CTA-Text (exakt): "Termin buchen"
Rückversicherung unter dem CTA (exakt): "5,0 Sterne bei 9 Google Bewertungen"

Echtes Foto: die Frau aus den Referenzfotos, warmes Portrait, Blickrichtung leicht zur
Headline/CTA geneigt. Kein medizinisches Kittel-Klischee, eher eine ruhige, persönliche
Umgebung mit einem Hauch Grün/Kräuter im Hintergrund (Anspielung auf den Hildegard
Kräutergarten, NICHT als echtes Foto behauptet).

Hintergrund: Creme #f8f3fb mit einem sehr dezenten botanischen Linienmuster (Blätter/
Kräuter), nicht die unscharfe Blumenfoto-Optik der alten Seite.
Textur: feine Papier-/Leinenstruktur im Hintergrund, kein Hochglanz.
Abstand: viel Weißraum um Headline und CTA, Logo klein oben links, NICHT überlappend
mit dem CTA (das ist der Fehler der echten Seite, hier korrigieren).

Format: Hochformat 1024x1536. Look der echten Praxis. Eine CTA-Farbe (Oliv).
```

---

## Sektion 2 — „Ist das etwas für mich?"

```
[GLOBAL STYLE BLOCK]

Sektion 2, Situationen. Layout: 5 Karten im Raster (2 Spalten mobil gestapelt, Desktop
3+2), jede Karte mit kleinem Icon statt Foto.

Headline (exakt): "Fünf Themen, bei denen ich Sie begleite"

5 Karten-Titel (exakt, je ein kleines botanisches/medizinisches Icon, keine Fotos von
Personen):
1. "Verdauung und Darm"
2. "Erschöpfung"
3. "Schilddrüse"
4. "Ernährung"
5. "Frauenthemen"

CTA-Text (exakt): "Termin buchen"

Echtes Foto: keines nötig, reine Icon-Illustration im Linienstil der Marke (passend zum
Logo-Icon-Stil, lila Linienzeichnung).
Hintergrund: Creme, helles Band.
Textur: keine, klar und ruhig.
Abstand: großzügig zwischen den Karten, klare Lesbarkeit.

Format: Hochformat 1024x1536. Eine CTA-Farbe (Oliv).
```

---

## Sektion 3 — Leistungen

```
[GLOBAL STYLE BLOCK]

Sektion 3, Leistungen. Layout: 6 Karten, Bild oben, Titel + Link darunter.

Headline (exakt): "So arbeite ich mit Ihnen"

6 Karten-Titel (exakt):
1. "Ausleitung und Entgiftung mit Aderlass nach Hildegard von Bingen"
2. "Sanfte Darmsanierung für mehr Wohlbefinden"
3. "Ernährungsberatung, die zu Ihrem Alltag passt"
4. "Klassische Homöopathie, individuell auf Sie abgestimmt"
5. "Oligoscan, Ihre Mineralstoffe und Belastungen in wenigen Minuten sichtbar machen"
6. "Massagen und Anwendungen zur tiefen Entspannung"

CTA-Text pro Karte (exakt): "Mehr erfahren"

Echtes Foto: keine Personen nötig, ruhige, warme Nahaufnahmen mit Bezug zum jeweiligen
Thema (z. B. Kräuter/Tee-Tasse für Ausleitung, frisches Gemüse für Ernährung, ruhige
Hände für Massage), KEIN reines Dekor-Blumenfeld wie auf der alten Seite, jedes Bild
muss erkennbar zum Thema der Karte passen.
Hintergrund: Creme, Karten mit dezentem Schatten.
Textur: Papierstruktur dezent.
Abstand: gleichmäßiges Raster, 2 Spalten mobil, 3 Spalten Desktop.

Format: Hochformat 1024x1536. Eine CTA-Farbe (Oliv).
```

---

## Sektion 4 — Der erste Termin

```
[GLOBAL STYLE BLOCK]

Sektion 4, Erster Termin. Layout: 4 nummerierte Schritte senkrecht (mobil) bzw.
horizontal (Desktop), mit Verbindungslinie.

Headline (exakt): "In vier Schritten zu Ihrem ersten Termin"

4 Schritte (exakt):
1. "Termin buchen: Online über das Buchungsformular oder telefonisch unter 030 36430358"
2. "Anamnesebogen ausfüllen: Vor dem Termin zugesandt, hilft mir, Sie gut vorbereitet
   kennenzulernen"
3. "Erstgespräch, 60 Minuten: Ausführliche Anamnese, 220 Euro, Abrechnung nach GebüH"
4. "Individueller Behandlungsplan: Gemeinsam besprechen wir die für Sie passende
   Kombination, Folgetermine je angefangene Stunde 150 Euro"

Hinweis-Zeile (exakt): "Hausbesuche kann ich derzeit leider nicht anbieten. Die Praxis
liegt direkt am Schloss Charlottenburg."

CTA-Text (exakt): "Jetzt Termin buchen"

Echtes Foto: kein Personenfoto nötig, Schritt-Icons im Linienstil der Marke, dezent
Lila/Oliv.
Hintergrund: Creme.
Textur: keine.
Abstand: klare Nummerierung, großzügiger Zeilenabstand.

Format: Hochformat 1024x1536. Eine CTA-Farbe (Oliv).
```

---

## Sektion 5 — Über die Behandlerin

```
[GLOBAL STYLE BLOCK]

Sektion 5, Über die Behandlerin. Layout: großes Portrait links/oben, Text rechts/unten,
dunkles Lila-Band als Hintergrund für Kontrast zur Creme-Umgebung.

Headline (exakt): "Über 20 Jahre Erfahrung, auf Ihre Situation zugeschnitten"

Body (exakt, als Platzhaltertext): "Seit 2002 bin ich als Heilpraktikerin in
Berlin-Charlottenburg tätig. Mein Schwerpunkt liegt in der Heilkunde nach Hildegard von
Bingen, die ich unter anderem bei Dr. Wighard Strehlow und an der Phytaro
Heilpraktikerschule in Dortmund gelernt habe. Seit 2023 bin ich Vizepräsidentin der
Internationalen Gesellschaft Hildegard von Bingen. In meinem eigenen Hildegard
Kräutergarten in der Schorfheide wachsen viele der Heilpflanzen, mit denen ich in
Seminaren und Workshops arbeite."

Beweis-Zeile (exakt): "Diplom Sozialpädagogin (FH) seit 1985 · Heilpraktikerin seit
2002 · Gründerin von Viriditas, Schule für Naturheilweisen, seit 2021"

CTA-Text (exakt): "Termin buchen"

Echtes Foto: die Frau aus den Referenzfotos, großformatiges, warmes Portrait, diesmal
mit einem dezenten Anklang an den Kräutergarten (z. B. ein Zweig Kräuter in der Hand
oder im Vordergrund, NICHT als dokumentarisches Foto behauptet, nur als Stimmung).
Hintergrund: dunkles Lila #5b2d80 als Band, Text in Creme darauf.
Textur: keine, klarer Kontrast.
Abstand: großzügig, Portrait dominiert die obere Hälfte.

Format: Hochformat 1024x1536. Eine CTA-Farbe (Oliv, auf dem dunklen Band gut sichtbar).
```

---

## Sektion 6 — Bewertungen

```
[GLOBAL STYLE BLOCK]

Sektion 6, Bewertungen. Layout: offene Bewertungswand (keine Karussell-Optik), 3 Karten
nebeneinander (Desktop) bzw. gestapelt (mobil).

Headline (exakt): "5,0 Sterne bei 9 Google Bewertungen"

3 Zitate (exakt, mit Google-Symbol-Andeutung, Vorname + Initiale):
1. "Verfügt als Dozentin über umfassendes Wissen zur Heilkunde der Hildegard von
   Bingen, kombiniert mit langjähriger Erfahrung mit Patientinnen und Patienten."
   — Scheila B.
2. "Kann Daniela Dumann von Herzen empfehlen. Mein Interesse an der Heilkunde der
   Hildegard von Bingen hat mich zu ihr geführt." — Karin S.
3. "Hat uns die Prinzipien der Hildegard Medizin mit Tiefe, Herz und Seele vermittelt."
   — Dagmar J.

CTA-Text (exakt): "Alle Bewertungen auf Google ansehen"

Echtes Foto: keines nötig, Sterne-Icons in Oliv, dezente Zitat-Anführungszeichen im
Linienstil der Marke.
Hintergrund: Creme.
Textur: keine.
Abstand: gleichmäßig, jede Karte mit klarer Trennung.

Format: Hochformat 1024x1536. Eine CTA-Farbe (Oliv).
```

---

## Sektion 7 — FAQ

```
[GLOBAL STYLE BLOCK]

Sektion 7, FAQ. Layout: Akkordeon-Liste, 5 Fragen, erste Frage leicht geöffnet als
Beispiel.

5 Fragen (exakt):
1. "Was kostet ein Termin bei einer Heilpraktikerin?"
2. "Übernimmt meine private Krankenkasse die Kosten?"
3. "Wie bereite ich mich auf den ersten Termin vor?"
4. "Kann ich einen Termin absagen oder verschieben?"
5. "Bieten Sie Hausbesuche an?"

Echtes Foto: keines, reines Text-/Icon-Layout (Plus-/Minus-Symbole in Lila).
Hintergrund: Creme, leichte Kartentrennung.
Textur: keine.
Abstand: großzügig, gut lesbar.

Format: Hochformat 1024x1536. Eine CTA-Farbe (Oliv, nur falls ein CTA am Ende steht).
```

---

## Sektion 8 — Standort

```
[GLOBAL STYLE BLOCK]

Sektion 8, Standort. Layout: Kartenausschnitt links/oben (Platzhalter, echte Karte kommt
später technisch), Adresse + Anfahrt rechts/unten.

Headline (exakt): "So finden Sie zu mir"

Body (exakt): "Naturheilpraxis Daniela Dumann, Nithackstraße 24, 10585
Berlin-Charlottenburg, direkt am Schloss Charlottenburg. Bus 109, 309 oder M45 bis
Luisenplatz/Schloss Charlottenburg. S-Bahn bis Westend, Charlottenburg oder
Jungfernheide. Mit dem Auto über die Autobahnausfahrt Spandauer Damm. Termine nach
Vereinbarung."

CTA-Text (exakt): "Termin buchen"

Echtes Foto: ein ruhiges, warmes Idealbild des Eingangsbereichs/der Straße am Schloss
Charlottenburg (kein echtes Foto vorhanden, als Idealbild erzeugen, Handoff bekommt
einen Shoot-List-Eintrag für ein echtes Ersatzfoto).
Hintergrund: Creme.
Textur: keine.
Abstand: klar getrennt Karten-Platzhalter und Text-Block.

Format: Hochformat 1024x1536. Eine CTA-Farbe (Oliv).
```

---

## Sektion 9 — Abschluss-CTA

```
[GLOBAL STYLE BLOCK]

Sektion 9, Abschluss, Mini-Hero. Layout: wie Sektion 1, aber kompakter, zentriert.

Headline (exakt): "Vereinbaren Sie jetzt Ihren ersten Termin"

3 Rückversicherungs-Punkte (exakt): "5,0 Sterne bei 9 Google Bewertungen" ·
"Heilpraktikerin seit 2002" · "Erstgespräch 220 Euro, 60 Minuten"

CTA-Text (exakt): "Termin buchen" (primär) · "030 36430358" (sekundär, als
Telefon-Button)

Echtes Foto: kleines, warmes Portrait-Detail (Ausschnitt aus den Referenzfotos), nicht
dominant, der Fokus liegt auf Headline + CTA.
Hintergrund: dunkles Lila #5b2d80 Band, wie Sektion 5, für einen klaren Seitenabschluss.
Textur: keine.
Abstand: zentriert, großzügig.

Format: Hochformat 1024x1536. Eine CTA-Farbe (Oliv, hoher Kontrast auf Lila).
```

---

## Full-Page-Prompt (Gesamtreferenz, 2-3 Varianten generieren)

```
[GLOBAL STYLE BLOCK]

Erzeuge die GESAMTE Startseite als eine lange, durchgängige Referenzgrafik (Hochformat,
sehr lang), die alle 9 Sektionen in dieser Reihenfolge zeigt, mit den oben exakt
genannten Headlines pro Sektion als Platzhaltertext:

1. Hero (Creme, Portrait, Headline, CTA)
2. Ist das etwas für mich (Creme, 5 Icon-Karten)
3. Leistungen (Creme, 6 Bild-Karten)
4. Der erste Termin (Creme, 4 Schritte)
5. Über die Behandlerin (dunkles Lila-Band, großes Portrait)
6. Bewertungen (Creme, 3 Zitat-Karten)
7. FAQ (Creme, Akkordeon)
8. Standort (Creme, Karte + Text)
9. Abschluss-CTA (dunkles Lila-Band, Mini-Hero)

Ziel: Gesamteindruck und Rhythmus zeigen (hell/hell/hell/hell/dunkel/hell/hell/hell/
dunkel), nicht jedes Detail pixelgenau. Diese Grafik ist NUR Referenz für Layout und
Stimmung, der echte Text kommt aus approved-copy.md.

Format: sehr hohes Hochformat, Look der echten Praxis, eine CTA-Farbe (Oliv) konsequent
durchgehend.
```

---

## Mobile-Prompts (Hero + Sticky CTA, 390 px)

```
[GLOBAL STYLE BLOCK]

Mobile-Ansicht, 390 Breite. Zeige NUR den Hero-Bereich plus die untere Sticky-Leiste:

Oben: Logo klein links, kein überlappender Button (Fehler der alten Seite korrigieren).
Headline (exakt, max 3 Zeilen umbrechend): "Ihr Weg zu mehr Wohlbefinden, persönlich
begleitet von einer Heilpraktikerin in Berlin-Charlottenburg seit 2002"
Darunter das Portrait, dann die Rückversicherungszeile "5,0 Sterne bei 9 Google
Bewertungen".

UNTEN, als sticky Leiste über dem sichtbaren Bildschirmrand: ein durchgehender Oliv-
Balken mit dem Button "Termin buchen" (Haupttext) und einem kleinen Telefon-Icon
daneben (sekundär). Diese Leiste muss bei jedem Scroll-Stand sichtbar bleiben, als
eigenes UI-Element zeigen.

Format: Hochformat 1024x1536 (entspricht 390 Breite proportional), Tap-Fläche des
Buttons deutlich groß (mindestens 44 px Höhe andeuten), hoher Kontrast Text/Hintergrund.
```

---

## Do-nots (gelten für jeden Prompt)

- Keine erfundene zweite Person als Behandlerin, nur die Frau aus den Referenzfotos.
- Kein Stockfoto-Look (keine unecht lächelnden Model-Gesichter, keine generischen Natur-Blumenfelder wie auf der alten Seite).
- Kein falscher, finaler Fließtext in großen Lettern im Bild, nur die oben exakt genannten Headlines/kurzen Labels als Platzhalter.
- Nur eine CTA-Farbe (Oliv) in der gesamten Seite, nie Lila UND Oliv gleichzeitig für Buttons.
- Keine Vorher-Nachher-Darstellung, keine Krankheits-Symbolik (keine Spritzen, keine Röntgenbilder, keine Schmerz-Ikonografie).

## Gate-Check

Alle 9 Sektionen aus `approved-copy.md` haben einen Prompt. Jeder Prompt enthält den Global Style Block. Gate bestanden → Checkpoint 2.
