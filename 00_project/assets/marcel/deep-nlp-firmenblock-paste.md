# DEEP NLP – Firmenblock zum Einfügen (Stand 08.10.2026)

Quelle: Marcels WhatsApp 06.10.2026 + Teilnahmebedingungen-Doc (Schreibweise dort).

## 1) Impressum  (Seite 34 → Thrive Architect)
Absatz UNTER „ANGABEN GEMÄß § 5 TMG" – diese 3 Zeilen ersetzen:

```
EXCELLENT MIND Solutions
Jalan Dr.Ir. Soekarno Delod Peken Kec Tabanan
82121 Bali, Indonesia
```

durch (4 Zeilen, Zeilenumbruch = Shift+Enter, damit es ein Absatz bleibt):

```
DEEP NLP LLC
7901 4th St N, Ste 300
St. Petersburg, FL 33702
United States of America
```

## 2) Datenschutzerklärung  (Seite „Datenschutz" → Thrive Architect)
Abschnitt „Hinweis zur verantwortlichen Stelle" – dieselben 3 alten Zeilen durch denselben 4-Zeilen-Block ersetzen.
E-Mail-Zeile darunter bleibt: `E-Mail: kontakt@marcel-rosenbach.de`

## 3) Prüfen nach dem Speichern
```
curl -s https://deep-nlp.com/impressum/ | grep -ci "EXCELLENT MIND"    # soll 0 sein
curl -s https://deep-nlp.com/datenschutz/ | grep -ci "EXCELLENT MIND"  # soll 0 sein
```

## 4) Teilnahmebedingungen
Text: Google-Doc 1CDQU3U6LeR72gfq2KTX0EmomEnxV0_r6yWDGq84fKmc
Neue Seite: https://deep-nlp.com/gewinnspiel  (Stil wie /datenschutz/)
Footer-Link „TEILNAHMEBEDINGUNGEN" NUR auf Gewinnspiel-Seiten (/gewinne-jetzt, /fast-gewonnen), nicht im globalen Footer.
Termine laut Doc: 12.10.2026 – 18.10.2026, 12:00 Uhr MESZ.
