# Automations-Spezifikation: Marcel Rosenbach · Skool → KlickTipp + Pipedrive (NLP Practitioner)

Stand: 2026-10-11 · Trockenlauf aus Memory (Stand 2026-09-04). Jede Zeile mit (M) ist aus dem Gedächtnis und wird in P0 live geprüft. Status: Entwurf, kein `go spec`.

## 1. Ziel
Jedes neue Mitglied der Skool-Gruppe DEEP NLP, das die 3 Beitrittsfragen beantwortet, landet in KlickTipp (Tag startet die Practitioner-Serie) und in Pipedrive (Person + Deal + Notiz mit den Antworten), damit das Call-Team onboarden kann.

## 2. Auslöser
| Feld | Wert |
|---|---|
| System | Skool, Gruppe `deep-nlp` (M) |
| Ereignis | Zapier-Trigger "Answered Membership Questions" (Polling) (M) |
| Liefert | Unique ID, Date, First Name, Last Name, Email, Question/Answer #1–3. Kein Tier (M, getestet 2026-09-01) |
| Konto | Marcels Zapier (paid), Zap 378535838 (M) |

## 3. Systeme
| System | Konto | Objekt-IDs (M) | Zugang |
|---|---|---|---|
| Skool | DEEP NLP, Admin-Login | Plugins Mitgliedschaftsfragen + Zapier = An | LastPass |
| Zapier | Marcel | Zap 378535838 v3 | LastPass, Zapier MCP |
| KlickTipp | Account 341498 | Tag `NLP PRAC - SKOOL` 15038160, Kampagne 2048561, Mails 3164372 … 3165041 | LastPass |
| Pipedrive | marcelrosenbachfzco | Pipeline 11, Stage NEUER PRAC 161 | Zapier MCP (mr@marcel-rosenbach.de) |

## 4. Feld-Zuordnung (M)
| Quelle | Ziel | Feld | Hinweis |
|---|---|---|---|
| Email | KlickTipp | E-Mail | Dedupe-Schlüssel |
| First/Last Name | KlickTipp | Vorname/Nachname | |
| Answer #2 | KlickTipp | NLP-Ziel field1001147 | |
| Answer #3 | KlickTipp | Herausforderung field1001148 | |
| Answer #1 (Telefon) | KlickTipp | — | NICHT mappen: 406-Fehler am 2026-09-03 |
| Date | KlickTipp | Startdatum field1001150 | NICHT mappen: 406-Fehler |
| — | KlickTipp | Tag 15038160 | startet Kampagne 2048561 |
| Email | Pipedrive | Person (Find/Create, Dedupe E-Mail) | nur Vorname+Nachname, NICHT "Person Name" (400-Fehler) |
| Answer #1 | Pipedrive | Person Telefon | |
| First+Last | Pipedrive | Deal-Titel "<Name> – SKOOL PRACTITIONER", Stage 161, Person-ID aus Schritt 3 | |
| Answers #1–3 | Pipedrive | Notiz am Deal (gepinnt) | |

## 6. Fehlerwege (offen, in P1 ergänzen)
Telefon mit Buchstaben · leere Antwort · KlickTipp-Validierung · Pipedrive 400 · Zapier-Verbindung abgelaufen · doppelter Beitritt.

## 7. Aktionen mit Freigabe
| Klasse | Aktion | Rückweg |
|---|---|---|
| G | Zap-Änderung veröffentlichen (neue Version) | Zapier-Versionsverlauf, vorige Version |
| G | Alarm-Weg einschalten (Zapier-Fehlermails an martin@741.studio) | ausschalten |
| M | Test-Mitgliedschaft in Skool (Zahlung) | Martin kündigt |

## 8. Testumgebung
TEST-Mitglied: Vorname `TEST-741`, E-Mail `test-skool@741.studio` (Postfach anlegen = offene Frage). Kostet einen Skool-Beitritt (Zahlung = Martin).

## 9. Tests (flow_class: messages)
e2e · Fehlerwege · zweimal auslösen · Alarm. Siehe `test-plan.md`.

## 10. Betrieb
741 überwacht. Tägliche Abgleich-Prüfung: neue Skool-Mitglieder (Zap-Historie) = neue KlickTipp-Kontakte mit Tag 15038160 = neue Deals in Stage 161.
