# me&you: Bild-Prompts für ChatGPT (06.10.2026)

Regel: Jeder Prompt verlangt ein hyperrealistisches Foto. Jeder Prompt bekommt echte Referenzbilder. Michael-Bilder nutzen seine echten Fotos, damit Gesicht, Statur und Stil stimmen. Persona-Bilder nutzen die Crops aus der Ehlers.pdf, damit Look und Szene zur Persona passen.

Ziel: Platzhalter und zu kleine Bilder (PDF-Crops 590 bis 1090 px) durch große, echte wirkende Fotos ersetzen.

## Gemeinsamer Stil-Block (in jeden Prompt)

> Hyperrealistic photograph, indistinguishable from a real editorial photo. Shot on a full-frame camera, 35mm or 50mm lens, natural light, shallow depth of field, real skin texture with pores and fine lines, natural fabric folds, no plastic skin, no AI gloss, no text, no logos, no watermark. Muted, warm editorial colour grade: cream, sand, soft dove blue, deep navy shadows. Calm, premium, quiet. Landscape 3:2.

## Michael-Referenz-Block (für Bilder mit Michael)

> The man in the attached reference photos is Michael Ehlers, a German rhetoric trainer in his late fifties. Keep his exact face, bald head, short grey-white beard, rectangular dark glasses, build and age. Do not make him younger or slimmer. He wears smart-casual clothes in the style of the references: linen shirt or knit, dark trousers, no tie.

## Michael-Referenzen (Martins Auswahl, 06.10.)
Aus der Bildauswahl-Seite: site-f09 (weißes Hemd, Café, 3476 px), site-f25 (weißes Hemd, Holztür, 4480 px), site-f10 (Sakko), site-f32 (weißes Hemd), michael-magazine, michael-stage, plus ein Instagram-Reel (noch zu bestimmen). Lokale Kopien: scratchpad `refs/michael-f09-cafe-white.jpg`, `refs/michael-f25-door-white.jpg`, `refs/michael-f10-jacket.jpg`, `refs/michael-f32-white.jpg`, `refs/michael-magazine.jpg`, `refs/michael-stage.jpg`. Für jedes Michael-Bild zwei bis drei davon hochladen.

## Bilder

| # | Datei | Sektion | Referenzen | Ersetzt |
|---|---|---|---|---|
| 1 | `ai-seminar-room.webp` | Seminare-Hero, v3 Methode | michael-jacket, michael-olive, gen-group | gen-group |
| 2 | `ai-seminar-finca.webp` | Startseite Seminar-Teaser | michael-f25-door-white, michael-f09-cafe-white, gen-mallorca | gen-mallorca |
| 3 | `ai-replayers-main.webp` | LP Replayers Hero, Situationskarte | pdf-replayers-main | pdf-replayers-main |
| 4 | `ai-replayers-desk.webp` | Situationskarte Replayers | pdf-replayers-desk | pdf-replayers-desk |
| 5 | `ai-overlooked-main.webp` | LP Overlooked Hero, Situationskarte | pdf-overlooked-main | pdf-overlooked-main |
| 6 | `ai-overlooked-thinker.webp` | LP Coaches Hero | pdf-overlooked-thinker | pdf-overlooked-thinker |
| 7 | `ai-undersold-main.webp` | LP Undersold Hero, Seminare Einstieg | pdf-undersold-main | pdf-undersold-main |
| 8 | `ai-undersold-table.webp` | Seminare "Drei Tage", Situationskarte | pdf-undersold-table | pdf-undersold-table |

### 1 Seminarraum mit Michael
[Michael-Referenz-Block] Scene: Michael leads a small rhetoric seminar of ten to twelve participants, men and women aged 35 to 55, business casual. They sit in a loose half circle of wooden chairs in a bright, calm room with tall windows, linen curtains and a plant. Michael stands slightly off-centre, mid-gesture, speaking with warm focus. Participants listen, one woman smiles. No flipchart text, no screens. Use the third reference only for room mood and composition. [Stil-Block]

### 2 Finca-Terrasse mit Michael
[Michael-Referenz-Block] Scene: golden hour on a stone finca terrace above a quiet Mediterranean bay in Mallorca. Michael sits at the head of a long wooden table with five seminar participants, coffee cups and notebooks, in conversation. Olive tree, warm low sun from the side, sea in the soft background. Use the third reference only for place and light. [Stil-Block]

### 3 Replayers: Heimweg
Scene: a woman in her early forties sits in a regional train in the evening and writes quickly in a notebook, the perfect sentence that came too late. Other passengers soft in the background, warm window light. Recreate the mood, framing and casting of the reference, but as a new, sharp, high-resolution photo. [Stil-Block]

### 4 Replayers: Schreibtisch
Scene: a woman at a wooden desk in warm lamp light at night, writing in a notebook, thoughtful. Recreate mood, framing and casting of the reference as a new high-resolution photo. [Stil-Block]

### 5 Overlooked: Meeting
Scene: a meeting at a glass table in a modern office with cool daylight. A competent woman in her forties speaks, but the others look at a man at the head of the table. Recreate the mood, framing and casting of the reference as a new high-resolution photo. [Stil-Block]

### 6 Overlooked: Denker am Fenster
Scene: a man in his late forties sits by a large window, city skyline soft behind him, thoughtful, holding a coffee cup. Recreate mood, framing and casting of the reference as a new high-resolution photo. [Stil-Block]

### 7 Undersold: Handschlag
Scene: a confident handshake across a table between a founder and a client, the small team around them applauds, warm interior light, wood and linen. Recreate the mood, framing and casting of the reference as a new high-resolution photo. [Stil-Block]

### 8 Undersold: Tisch
Scene: a small group of four adults laughing together at a wooden table, notebooks and glasses of water, warm afternoon light, relaxed and real. Recreate mood, framing and casting of the reference as a new high-resolution photo. [Stil-Block]

## Ablauf
ChatGPT (Chrome, neuer Chat je Bild) → Referenzen hochladen → Prompt → Ergebnis prüfen (Gesicht Michael, Hände, Text im Bild) → Download → `prototype/assets/ai-*.webp` (1536 px) → Build → Deploy.

## Status
| # | Status |
|---|---|
| 1 | live (Seminare-Hero A, Methode 03 B) |
| 2 | in ChatGPT generiert, Download offen |
| 3 | in ChatGPT generiert, Download offen |
| 4 | live (Situationskarte Replayers) |
| 5–7 | offen |
| 8 | offen, Priorität (Martin 06.10.: zu niedrig aufgelöst) |
