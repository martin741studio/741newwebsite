# Kunden-Formular — Maps-Audit (Blöcke 1-4, 8, 9)

Status: Entwurf. Gleiche Fragen für alle Kunden. Kurz, eine Idee pro Frage, ohne Anrede-Pronomen. So passt jeder Text für "du" und "Sie". Nur Einleitung und Schluss haben eine Anrede-Variante.
Ablage: Portal-Formular auf clients.741.studio. Antworten landen in `audit_answers` (`question_id`). Für den Testlauf trägt Claude die Antworten aus dem Stürzl-Sheet (Tab `01 Erstgespraech`) ein. Quelle dort: `sheet_import`.
Dauer: etwa 12 Minuten. Pflichtfragen sind mit * markiert. Kein Auto-Raten: leere Antwort bleibt leer ("offen").
Re-Audit: Das Formular zeigt nur Fragen, deren Antwort älter als 90 Tage ist oder als "geändert" markiert wurde.
Modus `call`: nur Fragen mit (K).

## Inhalt

- Einleitung und Schluss
- Block 1 Leadgenerierung
- Block 2 Profitabilität
- Block 3 Lead-Volumen
- Block 4 Geografischer Fokus
- Block 8 Betrieb
- Block 9 Eignung
- Zugänge und Dateien
- Technische Hinweise

## Einleitung und Schluss

| Variante | Text |
| --- | --- |
| du | "Mit diesen Angaben messen wir, was bei dir für Platz 1 auf Google Maps zählt. Es dauert etwa 12 Minuten. Zahlen dürfen Schätzungen sein. Schreib dazu, wie sicher du bist. Leere Felder sind in Ordnung." |
| Sie | "Mit diesen Angaben messen wir, was bei Ihnen für Platz 1 auf Google Maps zählt. Es dauert etwa 12 Minuten. Zahlen dürfen Schätzungen sein. Bitte vermerken Sie, wie sicher Sie sind. Leere Felder sind in Ordnung." |
| Schluss du | "Danke. Wir werten die Angaben aus und melden uns mit dem Ergebnis." |
| Schluss Sie | "Danke. Wir werten die Angaben aus und melden uns mit dem Ergebnis." |

Hinweis im Formular, immer sichtbar: "Bitte keine Namen von Mandanten oder Patienten eintragen."
Jede Zahlenfrage hat ein Feld "Sicherheit": exakt / Schätzung / Bauchgefühl. Das Feld füllt `confidence` = `client_stated` und bleibt als Zusatz im Antwort-JSON.

## Block 1 — Leadgenerierung und Marketing-Historie

| ID | Frage | Antwort | Feld |
| --- | --- | --- | --- |
| Q-B01-01 * (K) | Über welche Kanäle kommen aktuell Anfragen? | Mehrfachauswahl: Google-Profil, Website-Suche, Empfehlung, Anzeigen, Verzeichnis, Social Media, Partner, Sonstiges. Dazu Anteil in % | B01.01 |
| Q-B01-02 | Welche Marketing-Maßnahmen liefen in den letzten 24 Monaten? | Liste: Maßnahme, Anbieter, Monatsbudget, Ergebnis (gut / mittel / schlecht / unbekannt) | B01.02 |
| Q-B01-03 | Wer betreut aktuell Website und Suchmaschinen-Optimierung? | Auswahl: niemand / Agentur / freie Person / intern. Name optional | B01.03 |
| Q-B01-04 | Was passiert, wenn nichts geändert wird? Gibt es einen anderen Plan? | Freitext, 3 Zeilen | B01.04 |
| Q-B01-05 * (K) | Was ist der Anlass für das Audit gerade jetzt? | Freitext, 2 Zeilen | B01.05 |

## Block 2 — Profitabilität und Ticket-Größen

| ID | Frage | Antwort | Feld |
| --- | --- | --- | --- |
| Q-B02-01 | Welche 5 Leistungen bringen den größten Umsatz? | Rangliste, bis 5 Einträge | B02.01 |
| Q-B02-02 | Wie hoch ist der durchschnittliche Umsatz pro Neukunde? | Zahl in EUR | B02.02 |
| Q-B02-03 | Welche 3 Leistungen haben die höchste Marge? | Rangliste, bis 3 Einträge | B02.03 |
| Q-B02-04 | Wie viel Umsatz bringt ein Kunde über die gesamte Dauer? Oder: wie oft kommt ein Kunde wieder? | Zahl in EUR oder Anzahl Wiederkehr | B02.04 |

## Block 3 — Lead-Volumen und Abschlussquoten

| ID | Frage | Antwort | Feld |
| --- | --- | --- | --- |
| Q-B03-01 * (K) | Wie viele Anfragen kommen pro Monat insgesamt? | Zahl. Optional je Kanal aus Q-B01-01 | B03.01 |
| Q-B03-02 | Wie viele Anfragen werden zu Aufträgen? Je Kanal in % | Zahl je Kanal | B03.02 |

## Block 4 — Geografischer Fokus und CRM-Daten

| ID | Frage | Antwort | Feld |
| --- | --- | --- | --- |
| Q-B04-01 | In welchen Orten oder Stadtteilen sollen mehr Kunden herkommen? | Liste, bis 10 Einträge. Optional Priorität | B04.01 |
| Q-B04-02 | Gibt es einen Export der Anfragen oder Aufträge der letzten 12 Monate? | Upload CSV oder Excel. Nur Spalten: Postleitzahl, Leistung, Datum, Quelle. Keine Namen | B04.02 |
| Q-B04-03 | Ist in den nächsten 12 Monaten ein neuer Standort oder eine neue Leistung geplant? | Auswahl: nein / neuer Standort / neue Leistung / beides. Dazu Freitext | B04.03 |
| Q-B04-04 | Ist die Adresse des Standorts in den letzten 12 Monaten umgezogen? | Ja / nein. Bei ja: Datum | B13.02 |

## Block 8 — Betrieb und Kommunikationsregeln

| ID | Frage | Antwort | Feld |
| --- | --- | --- | --- |
| Q-B08-01 | Wie werden Anfragen und Umsatz erfasst? Lässt sich ein Auftrag einem Kanal zuordnen? | Auswahl: CRM / Tabelle / Kanzlei- oder Praxissoftware / gar nicht. Zuordnung: ja / teilweise / nein | B08.01 |
| Q-B08-02 * | Wer ist Ansprechperson? Wer entscheidet? Wer gibt Texte frei? | Name, Rolle, Kontakt je Person | B08.02 |
| Q-B08-03 * | Was darf auf Website und Google-Profil nicht verändert werden? | Freitext. Beispiele: Texte mit Berufsrecht-Bezug, Fotos, Preise | B08.03 |
| Q-B08-04 | Wie läuft die Abstimmung am besten? | Kanal (E-Mail / Telefon / WhatsApp), Antwortzeit, Anrede (du / Sie) | B08.04 |

## Block 9 — Eignung

| ID | Frage | Antwort | Feld |
| --- | --- | --- | --- |
| Q-B09-01 * (K) | Wie viele neue Kunden pro Monat sind zusätzlich möglich, ohne Qualität zu verlieren? | Zahl. Dazu Wartezeit auf einen Erstkontakt in Tagen | B09.01 |
| Q-B09-02 * (K) | In welchem Rahmen liegt das monatliche Budget für Sichtbarkeit (ohne Werbebudget)? | Auswahl: unter 500 / 500-1.000 / 1.000-2.000 / über 2.000 EUR. Dazu Werbebudget pro Monat | B09.02 |
| Q-B09-03 * (K) | Wer nimmt Anrufe an? Zu welchen Zeiten? Wie viele Anrufe bleiben unbeantwortet? | Person, Zeiten, Anteil unbeantwortet in % | B09.03 |
| Q-B09-04 | Wie viele neue Bewertungen pro Monat sind realistisch, wenn Kunden gezielt gebeten werden? | Zahl | B05.03 (Tempo) |
| Q-B09-05 | Nutzt der Betrieb schon ein Google-Profil für Anfragen? Welcher Anteil der Anfragen kommt von dort? | Auswahl + Anteil in % | B05.01 |
| Q-B09-06 | Wie läuft die Bitte um Bewertungen heute? | Freitext: wer, wann, wie | B05.03 (Prozess) |
| Q-B09-07 | Welche Suchbegriffe sollen den Kunden zuerst bringen? Welche glaubt der Betrieb schon gut zu ranken? | Liste, Prio 1-3 | B05.05 |
| Q-B09-08 | Läuft Google-Werbung? Wenn ja: Budget pro Monat und Anbieter | Auswahl + Zahl | B05.07 |

## Zugänge und Dateien (Pflicht im Kickoff)

| ID | Frage | Antwort | Feld |
| --- | --- | --- | --- |
| Q-ACC-01 * | Wem gehören Domain, Hosting, Google-Profil, Analytics, Tag Manager, Search Console, Ads-Konto? | Tabelle: Asset, Eigentümer (Betrieb / Agentur / unbekannt), Zugang erteilt (ja / nein) | B06.01 |
| Q-ACC-02 | Gibt es weitere Google-Profile (andere Standorte, alte Einträge)? | Liste mit Adresse | B13.01 |

## Technische Hinweise

- Pflichtfelder: nur die mit `*`. Alles andere darf leer bleiben.
- Antworten werden mit Version gespeichert (`audit_answers.version`). Ändern erzeugt eine neue Version.
- Datenschutz: Hinweis auf Anonymisierung, Link zur Datenschutzerklärung, Einwilligung als Checkbox vor dem Absenden.
- Der Upload (Q-B04-02) wird vor der Speicherung geprüft: keine Spalten mit Namen, E-Mail oder Telefon. Sonst Abbruch mit Hinweis.
- Entwurf der Formular-Seite folgt nach dem Testlauf. Bis dahin: Sheet-Import.
