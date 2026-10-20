# Prompt: Bebilderte Google-Bewertungs-Anleitung (741-Standard)

Kopiere den Block unten als Prompt. Fülle die Platzhalter in [ECKIGEN KLAMMERN].
Referenz-Vorlagen (fertiges Beispiel ShuiGuru): `07_social/templates/bewertungs-anleitung/`

---

Erstelle eine bebilderte Google-Bewertungs-Anleitung für unseren Kunden nach dem 741-Standard — in zwei Formaten: A4-PDF (Druck/Auslage) und PNG 1080×1350 (WhatsApp-Weiterleitung).

## Kunden-Inputs
- Kunde/Marke: [FIRMENNAME], Ansprechperson: [VORNAME]
- Branche/Leistungen (2–4 Kern-Leistungen): [z. B. Büro, Garten, Hof, Hausplanung]
- Ort + Kiez/Stadtteil: [z. B. Berlin-Neukölln]
- Google Place ID: [ChIJ…]
- Website: [https://…]
- Ansprache der Endkund:innen: „du"

## Harte Regeln
1. **Nur echte Brand-Assets:** Logo/Wordmark und Icon von der Kunden-Website laden (nie Platzhalter). Markenfarben aus der Website ziehen (1 Hauptfarbe + 1 Akzent). Kein 741-Branding — es ist das Material des Kunden.
2. **Struktur ist Pflicht — W-Blöcke, nie eine nackte Schrittliste:**
   - **Wer** (Intro, 1–2 Sätze): „Ich bin [VORNAME] ([MARKE]) — deine Erfahrung hilft anderen, … und macht mich bei Google sichtbar." Persönlich, von der Kundin/dem Kunden gesprochen.
   - **Schritt 1 · Wo:** Profil öffnen — QR-Code ODER Google-Suche „[MARKE] [STADT]" → Button „Rezension schreiben".
   - **Schritt 2 · Wie:** Sterne + 2–3 Sätze.
   - **Schritt 3 · Fertig:** auf „Posten" tippen + Dank mit Namen.
3. **Jeder Schritt bekommt ein UI-Bild** (Handy-Mock in HTML/CSS, kein Fake-Screenshot):
   - Mock 1: Google-Suchfeld mit „[MARKE] [STADT]" + Profil-Card + Button **„✎ Rezension schreiben"**, Button mit goldenem Glow markiert.
   - Mock 2: Bewertungsfenster „[MARKE] bewerten" mit **5 goldenen Sternen** + Textfeld mit dem **Ideal-Beispieltext** (siehe Regel 4) + „Posten"-Button.
4. **W-Fragen-Box für den Bewertungstext selbst** (im Schritt „Wie"):
   - **WAS** haben wir gemacht? Leistung benennen: **[Leistung 1, 2, 3]**.
   - **WIE** hat es sich verändert? 1–2 Sätze zum Ergebnis reichen.
   - **WO** war das? Am besten mit Ort/Kiez — z. B. „in [KIEZ]".
   - KEIN „WER" in dieser Box — WO ist der Local-Baustein.
   - Der Beispieltext im Mock zeigt die beste Variante = **Leistung + Ort + Ergebnis in einem Satz**, Muster: „[VORNAME] hat unser **[Leistung] in [KIEZ]** [gemacht] — [konkretes Ergebnis]. Klare Empfehlung!"
5. **QR-Code:** python `segno`, error='h', dunkle Markenfarbe, transparenter Hintergrund. Ziel-URL exakt: `https://search.google.com/local/writereview?placeid=[PLACE_ID]` (vorher per curl testen: erwartet 302). QR prominent unten mit Zeile „Kamera drauf → Bewertungsfenster öffnet sich direkt" + Dank + vollständigem Link in Kleinschrift (nur A4).
6. **Ton:** warm, einfach, „du", Badge „Deine Google-Bewertung · in 60 Sekunden". Keine Fachbegriffe, keine Tool-Namen, kein Druck.

## Technik/Format
- Ein HTML pro Format, Assets als data-URIs (Logo, Icon, QR) → self-contained.
- WhatsApp: 1080×1350 px, Blöcke gestapelt, QR-Zeile unten (`margin-top:auto`). Render: headless Chrome `--screenshot --window-size=1080,1350`.
- A4: gleiches Layout, per `@page{size:A4;margin:0}` + `html{zoom:~0.72}` auf EINE Seite skaliert, Fußzeile „[MARKE] · [Branche] · [STADT & Radius] | [WEBSITE]". Render: `--print-to-pdf --no-pdf-header-footer`. Seitenzahl prüfen: muss 1 sein.
- Dateinamen: `[kunde]-bewertungs-anleitung.pdf` + `[kunde]-bewertung-whatsapp.png`. HTML-Quellen mit ins Kunden-/Template-Verzeichnis.
- Vor Abgabe: PNG und PDF selbst ansehen (rendern + prüfen: nichts abgeschnitten, QR-Box vollständig, Umlaute korrekt).

## Lieferung
PNG + PDF an Martin senden, dazu ein 2-Zeilen-WhatsApp-Text (Ich-Form Martin → Kunde) mit dem vollen Bewertungs-Link zum Mitschicken. Nichts direkt an den Endkunden senden.

## Technik-Gotchas (macOS, Stand 04.09.2026)
- Kein `timeout`-Befehl auf macOS → `perl -e 'alarm 75; exec @ARGV' "<chrome>" …` nutzen. Headless Chrome beendet sich oft nicht sauber (Exit 142/143), Output ist trotzdem da.
- Google-Fonts-`<link>` lässt Headless Chrome hängen → Font als `@font-face` mit woff2-data-URI einbetten (Google-CSS mit Chrome-UA laden, `/* latin */`-URL nehmen).
- Chrome-Binary direkt aufrufen: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome --headless=new --disable-gpu --user-data-dir=<tmp> --timeout=15000 …` (eigenes user-data-dir, sonst kollidiert es mit dem Antigravity-Profil).
- Markenfarben bei Enfold-Sites: `:root{--enfold-main-color-*}` in `uploads/dynamic_avia/avia-merged-styles-*.css`.
- Fertige Beispiele: ShuiGuru (Berlin, Feng Shui) + Praxis Suriya (Ingelheim, Heilpraktikerin, 04.09.2026).
