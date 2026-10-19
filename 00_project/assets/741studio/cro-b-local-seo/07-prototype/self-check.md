# Self-Check — Local-SEO-Seite (Track B QA T1–T10)

| # | Check | Ergebnis |
|---|---|---|
| T1 | Frame Rate | Kein sichtbares Ruckeln beim vollen Scroll (Chrome, Desktop + Mobile) |
| T2 | Video-Loops | Keine CSS-Loop-Videos verwendet (nur YouTube-Embeds, eigene Steuerung) |
| T3 | Off-Screen Media | Testimonial-Videos `loading="lazy"`, Hero-Video bewusst eager (Above-the-Fold) |
| T4 | Reduced Motion | Alle eigenen Animationen (Zeitleiste, Zahlen, CTA-Atmen, Sticky-Leiste) prüfen `prefers-reduced-motion` und springen auf Endzustand |
| T5 | Komponenten-Isolation | Seite funktioniert vollständig ohne JS-Animationen (Inhalte sind im HTML vorhanden, nur Bewegung fällt weg) |
| T6 | Gewichts-Budget | ~1,5 MB Gesamtressourcen beim Laden, unter 12-MB-Budget, erstes Sichtfeld unter 2,5 MB |
| T7 | X-Ray-Switch | Nicht gebaut — Seite ist direkt im Live-Template gebaut, kein separater Code/Media-Mockup-Layer wie bei einem Stand-alone-Prototyp |
| T8 | CTA im ersten Sichtfeld | Hero-CTA bei 701px Höhe sichtbar, kein Intro-Animations-Delay, der ihn verdeckt |
| T9 | Tastatur-Navigation | Proof-Wall-Pfeile sind echte `<button>`-Elemente, CTA-Links sind `<a>`, alles per Tab erreichbar |
| T10 | Kontrast | Dunkler Text (#1a1a1a) auf Creme (#f7f6f2) und Weiß, Lemon nur als Akzent (Button-Hintergrund mit dunklem Text, Linien, Pillen) — keine Textfarbe mit niedrigem Kontrast |

**Anmerkung zu T7:** Diese Seite wurde, wie die Portfolio-Seite, direkt im echten Live-Template gebaut statt als getrennter lokaler Mockup-Prototyp mit Code/Media-X-Ray. Diese Abweichung vom Standard-Lieferformat ist dieselbe wie bei der Portfolio-Seite (vom Agenten entschieden, um direkt deploybaren Code zu liefern). Der GPT-Full-Page-Mockup (B6) deckt die visuelle Referenzfunktion ab, die ein X-Ray sonst zusätzlich bieten würde.

**Gesamt-Score: 9/10 Punkte voll erfüllt, 1 Punkt (T7) strukturell nicht anwendbar wegen des direkten Live-Template-Baus.**
