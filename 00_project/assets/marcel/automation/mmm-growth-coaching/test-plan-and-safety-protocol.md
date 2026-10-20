# Testplan & Sicherheits-Protokoll: MMM Growth-Identity-Coaching Funnel

**Projekt:** Marcel Rosenbach (`deep-nlp.com`)  
**Datum:** 17.10.2026  
**Ziel:** Vollständige End-to-End-Prüfung der neuen Strecke OHNE Unterbrechung des bestehenden Make More Money Kurs-Zugangs.

---

## 1. Das Gating-Prinzip (Hard Rule)

> [!CAUTION]
> **DAS LIVE-FORMULAR `7RaKgP` WIRD ERST GANZ ZUM SCHLUSS UMGESTELLT!**
> Die Weiterleitung des bestehenden MMM-Tally-Formulars (`https://tally.so/r/7RaKgP`) darf erst dann auf `https://deep-nlp.com/more-money-now` geändert werden, wenn alle nachfolgenden Testfälle T1 bis T5 erfolgreich bestanden und dokumentiert sind.

---

## 2. Testfälle (End-to-End & Fehlertoleranz)

| Test-ID | Testfall | Erwartetes Verhalten | Nachweis-Kriterium |
|---|---|---|---|
| **T1** | **E2E Neuanmeldung Bewerbung**<br>Absenden des neuen Tally-Formulars mit Testdaten: `TEST-741 Max Mustermann` | 1. Tally leitet weiter auf `https://deep-nlp.com/grow-now`<br>2. Pipedrive: Person wird gefunden/angelegt, Deal in Pipeline `GROW WITH NLP! 🤯` / Phase `🔥 Growth aktiviert` mit Titel `Max Mustermann 💸GROWTH-COACHING`<br>3. Pipedrive Notiz: Alle 5 Fragen + Antworten sauber formatiert mit Leerzeilen<br>4. KlickTipp: Kontakt angelegt/aktualisiert mit Tag `Growth-Identity-Coaching`<br>5. KlickTipp E-Mail: Genau 1 Bestätigungsmail mit `Hey Max,` verschickt | Screenshot / API-Log von Pipedrive Deal + KlickTipp Tag & Mail |
| **T2** | **Ungültige Telefoneingabe**<br>Eingabe von Buchstaben im Telefonfeld | Tally blockiert clientseitig ("Bitte eine gültige Telefonnummer eingeben"). Kein Fehllauf in Zapier. | Formular lässt sich nicht absenden |
| **T3** | **Mehrfachauswahl Hindernisse (Frage 3)**<br>Auswahl von 3 verschiedenen Hindernissen | Pipedrive-Notiz formatiert jedes Hindernis in eine eigene Zeile, kein unleserlicher Textblock. | Pipedrive Notiz Textprüfung |
| **T4** | **Bestehender Kontakt (Deduplizierung)**<br>Erneutes Absenden mit derselben E-Mail-Adresse | 1. Bestehende Person in Pipedrive wird wiederverwendet (keine Personen-Duplikate)<br>2. KlickTipp-Kontakt wird aktualisiert, kein 406-Fehler | Pipedrive Personen-ID bleibt identisch |
| **T5** | **Bestehende MMM-Anmeldung (Altes Tally `7RaKgP`)**<br>Absenden einer MMM-Basiskurs-Anmeldung | 1. Pipedrive Deal wird erstellt mit Titel `Vorname Nachname 🤑MAKE MORE MONEY`<br>2. KlickTipp Tag `MAKE MORE MONEY, BABY` vergeben<br>3. Kurszustellung und alte E-Mail-Serie laufen wie gewohnt | Bestehende Automation läuft unverändert |

---

## 3. Pre-Switch Checklist (Freigabe-Gate)

Vor dem Klick auf "Publish" in Tally `7RaKgP`:
- [ ] Danke-Seite 1 (`https://deep-nlp.com/more-money-now`) ist live in WordPress angelegt und erreichbar.
- [ ] Danke-Seite 2 (`https://deep-nlp.com/grow-now`) ist live in WordPress angelegt und erreichbar.
- [ ] Neues Tally-Formular ist veröffentlicht und `redirectOnCompletion` steht auf `https://deep-nlp.com/grow-now`.
- [ ] Zapier Automation ist eingeschaltet und Testlauf war erfolgreich (T1).
- [ ] KlickTipp-Tag `Growth-Identity-Coaching` existiert als echtes Tag (nicht als Label).
- [ ] KlickTipp-Bestätigungsmail ist angelegt und aktiv.

---

## 4. Finale Freigabe-Aktion (Gated Step)

Erst nach Erfüllung aller Punkte oben:
1. In Tally Formular `https://tally.so/forms/7RaKgP/edit` wechseln.
2. Text über dem Feld "Vorname" austauschen zu:  
   `Aktuell die Chance auf ein kostenfreies Growth-Identity-Coaching. Reduzierte Plätze!`
3. In den Settings von `7RaKgP` die Weiterleitung (`Redirect on completion`) auf `https://deep-nlp.com/more-money-now` umstellen.
4. "Publish" klicken und mit cURL prüfen:  
   `curl -sL https://tally.so/r/7RaKgP | grep more-money-now`
