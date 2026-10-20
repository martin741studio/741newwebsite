# 741 CRO-Raster — Scorecard (Startseite lokale Praxis)

Stand 2026-10-11, von Martin freigegeben. 22 Items. Score 0 = fehlt, 1 = teilweise, 2 = erfüllt. Jeder Score 0 oder 1 braucht eine Beleg-Zeile (Zitat, Screenshot-Name oder Zahl). Prio A = Hero, CTA, Erster-Termin-Klarheit, Vertrauen above the fold. Prio B = Beweise, Angebot, Standort. Prio C = Rest.

Bestehenskriterium Prototyp: alle Prio-A-Items = 2, Gesamt mindestens 36 von 44.

| # | Regel | Prüfung | Prio | Score 0/1/2 | Beleg |
| --- | --- | --- | --- | --- | --- |
| 1 | Hero nennt in 5 Sekunden: was, für wen, nächster Schritt | Hero lesen, 5-Sekunden-Test | A | | |
| 2 | Headline = gefühltes Ergebnis + Stadt, nicht „wer wir sind“ | H1/Headline lesen; Stadt enthalten? | A | | |
| 3 | Sub-Headline: Situation zuerst, dann 3–4 konkrete Hilfen | Sub-Headline lesen | A | | |
| 4 | Primärer CTA im ersten Bildschirm (1440×800) ohne Scrollen sichtbar | Screenshot 1440 px, erster Viewport | A | | |
| 5 | CTA-Text nennt nächsten Schritt + Nutzen, nicht „Kontakt“ | Button-Text lesen | A | | |
| 6 | Rückversicherung direkt unter dem CTA (Antwortzeit, Dauer, unverbindlich) | Zeile unter Button vorhanden? | A | | |
| 7 | Zwei Beweisformen above the fold (Google-Bewertung + Zahl/Zitat) | Hero-Screenshot | A | | |
| 8 | Gesicht + Qualifikation der Behandlerin im Hero oder Sektion 2 | Screenshot, Bild echt? | A | | |
| 9 | „Dein erster Termin“: 3–4 Schritte, Dauer, Preisrahmen | Sektion vorhanden, Felder gefüllt? | A | | |
| 10 | Nur eine Akzentfarbe für den CTA; Blur-Test besteht | Screenshot unscharf prüfen | A | | |
| 11 | CTA wiederholt sich mindestens alle 2 Sektionen | Sektionen zählen | A | | |
| 12 | Bewertungen offen (keine Karussells), mit Vorname + Google-Logo + Überschrift | Review-Block prüfen | B | | |
| 13 | Beweis-Überschrift trägt Nutzen, nicht „Bewertungen“ | Überschrift lesen | B | | |
| 14 | 3–4 Beweisblöcke über die Seite verteilt, einer am Kontaktblock | Seite scrollen, zählen | B | | |
| 15 | Situationen-Sektion: 3–5 erkennbare Situationen + Weg hinaus, HWG-sauber | Sektion lesen, HWG-Check | B | | |
| 16 | Leistungen als Karten mit Nutzen-Überschrift und Link | Sektion prüfen | B | | |
| 17 | FAQ mit echten Einwänden: Preis zuerst, Krankenkasse, Dauer, Absage | FAQ lesen | B | | |
| 18 | Standort: Karte, Adresse, Parken, ÖPNV, Öffnungszeiten | Sektion prüfen | B | | |
| 19 | Abschluss-Sektion = Mini-Hero (Headline, Checkmarks, Beweis, CTA + Telefon) | Letzte Sektion prüfen | B | | |
| 20 | Jede Sektions-Überschrift trägt eine Aussage (kein Label) | Nur Überschriften lesen: verkauft die Seite? | C | | |
| 21 | Typografie/Hierarchie: Headline 3–4× Body, Body ≥ 16 px | Computed styles, Screenshot | C | | |
| 22 | Nur Health-Kunden: keine HWG-Verstöße (keine Heilversprechen, keine Vorher/Nachher, keine Angst) | Volltext-Check | A | | |

## Scoring-Hinweise

- Item 4: 2 = Button vollständig sichtbar auf 1440×800 ohne Scrollen; 1 = teilweise sichtbar oder nur Telefon; 0 = unter dem Fold.
- Item 7: 2 = zwei verschiedene Beweisformen; 1 = eine; 0 = keine.
- Item 11: 2 = CTA in Hero, Sektion 3, 5, 6, 7, 10; 1 = CTA in weniger Sektionen; 0 = nur ein CTA.
- Geltungsbereich: nur Desktop (Martin, 2026-10-11). Mobile-Punkte gehören in den späteren Mobile-/Rebuild-Workflow.
- Item 12: Karussell = maximal 1.
- Item 22: ein einziger Verstoß = 0. Dieses Item ist ein Hard Gate: ohne 2 kein Checkpoint. Bei Nicht-Health-Kunden entfällt Item 22; Gesamt dann mindestens 34 von 42.

## Quellen

Items 1–21 stammen aus `rules.md` (R1–R11, L1–L7). Item 22 aus L8/L9 und der HWG-Guideline.
