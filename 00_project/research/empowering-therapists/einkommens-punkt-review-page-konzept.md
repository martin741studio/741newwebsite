# Konzept: Einkommens-Punkt auf der 741 Review-Page

Stand 31.10.2026. Nur Konzept, nichts gebaut. Martin 31.10.: Konzept als Grundlage freigegeben, Bau erst nach Werten und Wortlaut und separater Freigabe. Grundlage: Element-Inventar Empowering Therapists (Abschnitt G) und der heutige Wachstums-Rechner in `build_page.py`.

## 1. Was die Review-Page heute rechnet

Der Wachstums-Rechner (Sektion `#rechner`) hat sieben Regler: Suchvolumen, Klickanteil, Werbebudget, Klickpreis, Anfragequote, Abschlussquote, Wert pro Kunde. Er zeigt Besucher, Anfragen, neue Kunden pro Monat und Mehrumsatz pro Jahr.

Was fehlt gegenüber ihrem Muster:

| Ihr Element | Bei uns heute |
|---|---|
| Wo stehst du heute (Monatseinkommen) | Nicht vorhanden. Der Rechner startet bei null und zeigt nur das Plus. |
| Das Ziel als Zahl (10.000 bis 20.000 im Monat) | Nicht vorhanden. Der Rechner hat kein Ziel, nur ein Ergebnis. |
| Die Brücke: Sitzungen mal Satz mal Wochen | Nicht vorhanden. Wir rechnen über Suchvolumen, nicht über die Praxis. |
| Der Preis-Hebel (Satz erhöhen) | Nicht vorhanden. Der Wert pro Kunde ist ein Regler, aber niemand sagt, dass er zu niedrig ist. |
| Rechtfertigung des 741-Preises | Nicht vorhanden. Die 4.999 € stehen auf der Growth-Page ohne Bezug zur Lücke. |

## 2. Der neue Block: "Deine Praxis in Zahlen"

Platz: vor dem Wachstums-Rechner, nach dem Website-Check. Drei Spalten, alle Werte als Regler mit Startwerten aus unserer Recherche, jeder Startwert mit "Annahme" oder Quelle beschriftet.

### Spalte 1: Heute

- **Dein Satz pro Sitzung.** Startwert von ihrer Website oder aus dem Call. Quelle wird genannt ("laut deiner Website 129 €"). Fehlt er: Branchenwert mit Beschriftung "Annahme".
- **Sitzungen pro Woche heute.** Startwert geschätzt aus Signalen: Bewertungen pro Monat, Sichtbarkeit im Scan, Aussagen auf der Website ("Termine frei"), Alter der Praxis. Regler, damit sie korrigiert.
- **Monatseinkommen heute.** Rechnung: Satz mal Sitzungen mal 45 Wochen geteilt durch 12. Große Zahl, Beschriftung "geschätzt".

### Spalte 2: Ziel

- **Wunsch-Monatseinkommen.** Regler, Startwert 10.000 €. Sie stellt ihn selbst ein. Das ist ihr Muster: Die Kundin spricht die Zahl aus.
- **Sitzungen pro Woche, die dafür nötig sind, bei deinem heutigen Satz.** Rechnung: Ziel mal 12 geteilt durch 45 geteilt durch Satz.
- **Satz, der dafür nötig ist, bei deinen heutigen Sitzungen.** Rechnung: Ziel mal 12 geteilt durch 45 geteilt durch Sitzungen.

Die zwei Zahlen nebeneinander zeigen den Preis-Hebel ohne ein Wort: 10.000 € sind bei 129 € pro Stunde 21 Sitzungen pro Woche, bei 180 € sind es 15.

### Spalte 3: Lücke und Weg

- **Lücke pro Monat.** Ziel minus heute.
- **Fehlende neue Kunden pro Monat.** Lücke geteilt durch Wert pro Kunde (Regler aus dem Rechner, verknüpft).
- **Nötige Anfragen und Besucher.** Über Abschlussquote und Anfragequote aus dem Rechner zurückgerechnet.
- **Vergleich mit dem Markt.** Nötige Besucher gegen Suchvolumen mal Klickanteil. Ergebnis als Satz: "Mit Top-3-Plätzen bei 'Heilpraktiker Erding' sind das X Besucher im Monat. Das reicht für Y der Z fehlenden Kunden." Wenn es nicht reicht, steht da: "Der Rest kommt über den Satz oder über Pakete."
- **Was 741 kostet, in deiner Lücke gemessen.** "Das Programm kostet 4.999 € einmalig. Das sind N Wochen deiner Lücke" oder "M neue Kunden". Das ist die Rechtfertigung des Preises, in ihren Zahlen, nicht in unseren.

### Was sich dadurch im Call ändert

Martin sieht vor dem Call, welche Zielzahl sie eingestellt hat, wenn wir den Regler-Wert speichern (ein Eintrag in `site_form_submissions` oder eine neue Tabelle, nur Slug, Zeitstempel, Zielwert). Im Call: "Du hast 10.000 eingestellt. Bei deinem Satz sind das 21 Sitzungen. Lass uns über den Satz reden." Das ist der Einstieg in den Baustein "Preis und Angebot", den es noch nicht gibt.

## 3. Welche Daten wir pro Prospect schon haben

| Datum | Quelle heute | Für den Block |
|---|---|---|
| Satz pro Sitzung | Website des Prospects (Preisseite), Call, Verzeichnisse | Spalte 1, Startwert |
| Leistungen | Website, Google-Profil | Welche Leistung gerechnet wird |
| Suchvolumen | DataForSEO (schon im Rechner) | Spalte 3, Marktvergleich |
| Sichtbarkeit | Local-Falcon-Scan (schon auf der Seite) | Schätzung Sitzungen heute, Klickanteil heute |
| Bewertungen und Alter | Google-Profil | Schätzung Sitzungen heute |
| Wert pro Kunde | prospect.json `calc.val` (heute eine Annahme pro Prospect) | Spalte 3 |
| Kapazität | Call (Theresia: halbe bis dreiviertel Stelle) | Obergrenze für den Sitzungs-Regler |

## 4. Was fehlt und entschieden werden muss

1. **Branchenwerte für Deutschland mit Quelle.** Erledigt 31.10.: `branchenwerte-de-2026-10-31.md` mit Satz, Sitzungen pro Woche, Startwert-Bändern und Quellen je Zeile für fünf Branchen.
2. **Schätzregel für "Sitzungen heute".** Welche Signale, welche Bänder (niedrig, mittel, hoch). Muss einmal festgelegt und dann in `prospect.json` als `income.sessions_est` mit Begründung eingetragen werden.
3. **Zielwert-Standard.** Entschieden 31.10. (Martin): pro Branche. Psychotherapie und Physio 10.000 €, Heilpraktiker und Coaching 8.000 €, Massage 5.000 €. Herleitung in `branchenwerte-de-2026-10-31.md`.
4. **Speichern des Reglers.** Entschieden 31.10. (Martin): ja. Slug, Zeitstempel, Zielwert in Supabase, kurzer Hinweis am Regler. Bau erst nach separater Freigabe.
5. **Wortlaut der Preis-Zeile.** "N Wochen deiner Lücke" oder "M neue Kunden" oder beides.
6. **Schema.** Neuer Block `income` in `prospect.json`, neue Funktion `income(p)` in `build_page.py` vor `calc(p)`, JS teilt sich die Regler `conv`, `deal`, `val`, `vol`, `share` mit dem Rechner. Validierung in `validate.py` für fehlende Quellen.

## 5. Alle Aktionen und Teile ihrer Programme, nummeriert

### Therapist Private Pay Accelerator (12 Wochen)

1. Kassen-Ausstieg planen, hybrid über sechs bis zwölf Monate
2. Satz aus dem Wunschgehalt berechnen und festlegen
3. Satz bei Bestandsklienten erhöhen, mit Wortlaut
4. Erstgespräch strukturieren: 10 bis 15 Minuten, Fragen, klarer nächster Schritt
5. Diagnose: nicht gefunden oder nicht gebucht
6. Google-Unternehmensprofil beanspruchen und anlegen
7. Hauptkategorie wählen, Servicegebiet oder Adresse entscheiden
8. Leistungen, Beschreibung mit Suchbegriffen, Fotos, regelmäßige Beiträge
9. Bewertungen von Kolleginnen einholen
10. Verzeichnisse auswählen: Psychology Today plus zwei bis drei
11. Verzeichnisprofile umschreiben: erste zwei Sätze für die Klientin, nicht für Kollegen
12. Wunschklientin festlegen (Demografie, Diagnose, Alltag, unausgesprochene Bedürfnisse, Erwartungen, Beruhigungsfaktoren)
13. Klientensprache aus Intake-Formularen und Erstgesprächen sammeln
14. Fachsprache und Methodennamen aus den Texten nehmen
15. Pflichtelemente jeder Website-Seite setzen
16. Eine Seite pro Leistung anlegen
17. Keywords finden: Problem plus Zielgruppe plus Methode plus Stadt, Google-Vorschläge nutzen
18. Keyword in H1 und H2 jeder Seite
19. 500 bis 1.000 Wörter pro Seite
20. Preis und Selbstzahler-Hinweis auf die Website
21. Buchungslink und Telefonnummer sichtbar
22. FAQ-Sektion mit echten Klientenfragen
23. Name, Adresse, Telefon überall identisch
24. Professionelles Foto
25. Google Analytics einrichten und Fortschritt lesen
26. Inhalte regelmäßig aktualisieren
27. Für KI-Suche schreiben: Frage, Antwort, maschinenlesbare Qualifikation
28. Intensiv-Formate als Angebot aufsetzen
29. Google Ads Grundlagen
30. Antwortzeit auf Anfragen verkürzen
31. Geld-Mindset und Impostor-Arbeit
32. Burnout-Prävention in den Praxisablauf einbauen
33. Gruppenpraxis planen, Admin und Therapeutinnen einstellen
34. Verwaltung automatisieren
35. Weitere Einnahmequellen und zweites Business anlegen und vermarkten
36. Bonus: Praxis gründen mit Checkliste und Formularen
37. Bonus: Squarespace-Website von null bauen
38. Jede Woche: ein Modul, eine Aufgabe, drei Gruppen-Calls, ein privater Call
39. Google-Profil, Verzeichnisprofile und Website zur Prüfung einreichen
40. Wins in Slack posten

### Retreat (4 Tage, 2.497 Dollar)

41. Mastermind-Training zu 10.000 bis 20.000 Dollar Monaten
42. Persönliche Geschäftsberatung zur eigenen Praxis
43. Professionelle Headshots
44. Mindset, Yoga, Breathwork, Glaswandern, Journaling

### Wealthy Therapist Program (Bewerbung)

45. Strategie, Angebote, Marketing und Systeme für Einkommen über die Einzelstunde hinaus

### Buch, Guide, Gratis-Angebote

46. Buch "The Wealthy Therapist": Kassen-Ökonomie, Findbarkeit, Satz, Einkommen jenseits der Stunde, Skalierung, jedes Kapitel endet mit einer Aufgabe
47. SEO-Guide für 9,97 Dollar: Seite-für-Seite-Checkliste, Upsell Specialty-Page-Vorlage und 10-Seiten-Playbook
48. Gratis-Video per DM nach Kommentar-Wort
49. Kostenlose Facebook-Gruppe mit Trainings und Guides
50. 45-Minuten-Gespräch mit dem Team, ohne Pitch
