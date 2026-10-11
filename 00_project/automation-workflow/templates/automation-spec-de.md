# Automations-Spezifikation: <Kunde> · <Name der Automation>

Stand: <YYYY-MM-DD> · Lauf-Ordner: `00_project/assets/<kunde>/automation/<slug>/` · Status: Entwurf, wartet auf `go spec`

## 1. Ziel

<Ein Satz: Was passiert automatisch, für wen, mit welchem Ergebnis.>

## 2. Auslöser

| Feld | Wert |
|---|---|
| System | <z. B. Skool> |
| Ereignis | <z. B. "Answered Membership Questions"> |
| Art | Polling / Webhook / Zeitplan (Zeitzone!) |
| Konto / ID | <angemeldetes Konto, Gruppen-URL, Account-ID> |

## 3. Systeme und Konten (aus der Inventur, alle IDs geprüft)

| System | Konto (angezeigt) | Objekt-IDs | Zugang über | Nur lesen? |
|---|---|---|---|---|
| | | | LastPass / Portal-Zugang / OAuth | ja / nein |

## 4. Feld-Zuordnung

| Quelle (Feld) | Ziel-System | Ziel-Feld | Format / Umwandlung | Pflicht | Wenn leer |
|---|---|---|---|---|---|

## 5. Ablauf Schritt für Schritt

1. <Schritt> → erwartetes Ergebnis → wie wir es zurücklesen
2. …

## 6. Fehlerwege

| Fehler | Erkennung | Reaktion | Alarm an |
|---|---|---|---|
| Pflichtfeld leer | | | martin@741.studio |
| Falsches Format (z. B. Telefon) | | | |
| Zugang abgelaufen | | | |
| Ziel-System nicht erreichbar | | | |
| Doppelter Auslöser | | Dedupe über <Schlüssel> | |

## 7. Aktionen mit Freigabe

| ID (später) | Klasse | Aktion | Wer ist betroffen | Rückweg |
|---|---|---|---|---|
| | G | <z. B. Zap einschalten> | | <Zap ausschalten> |
| | M (Martin) | <z. B. Testmitgliedschaft kündigen> | | |

## 8. Testumgebung

- Testdatensatz: Name enthält `TEST-741`, E-Mail <test…@741.studio>
- Flow bleibt Entwurf / AUS bis zur Freigabe
- Test-Einstellungen, die vor dem Start zurück müssen: <z. B. Testpreise>

## 9. Tests (flow_class: messages / crm / internal)

- [ ] e2e mit Testdatensatz, alle Felder in allen Zielen zurückgelesen
- [ ] Fehlerwege (Pflicht bei messages / crm)
- [ ] Zweimal auslösen, keine Dubletten (Pflicht bei messages / crm)
- [ ] Alarm-Test (Pflicht bei messages / crm)
- [ ] weitere: <…>

## 10. Betrieb nach dem Start

- Verantwortlich: 741 (Überwachung im Rahmen der Betreuung)
- Alarm: Plattform-Fehlermeldung + tägliche Abgleich-Prüfung <Quelle-Zahl vs. Ziel-Zahl>
- Rückweg im Notfall: <in einem Satz>

## 11. Offene Punkte (nur echt Unbeantwortbares)

- <…>
