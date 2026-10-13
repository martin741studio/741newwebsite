# Kunden-Freigabe im Portal: Einbau (Stand 2026-10-13)

Workflow-Schritt 3: Einbau ins Portal `clients.741.studio`, nur auf Staging. Vorlage: `../prototype/index.html`. Regeln: `../brief.md`.

## Dateien

| Datei | Inhalt | Status |
| --- | --- | --- |
| `01-migration.sql` | Tabellen `client_approval_settings`, `approval_items`, `approval_decisions`, Trigger, RPCs, RLS | angewendet 13.10. nach Martins Go |
| `02-mails-draft.sql` | Tag-7-Regel, Sammel-Mail (max. 1 pro Tag), Erinnerung Tag 3, Versand mit BCC an martin@741.studio | **Entwurf, nicht aktiv** |
| `03-seed-testpraxis.sql` | Testpraxis Musterstadt mit den 5 Beispiel-Elementen aus dem Prototyp | angewendet 13.10. |
| `05-seed-suriya-drafts.sql` | Praxis Suriya: 5 Elemente als Entwurf, gegen Live-Website und HWG geprüft | angewendet 13.10., Coralie sieht nichts bis „An Kunde geben“ |
| `04-rls-tests.sql` + `04-rls-dryrun-result-2026-10-13.txt` | 20 RLS- und Regel-Tests, alle OK | fertig |
| `mail-digest-text.txt`, `mail-reminder-text.txt` | Mailtexte, Slop-Check 5/5 | Entwurf |
| `mail-digest-text-en.txt`, `mail-reminder-text-en.txt` | englische Mailtexte (clients.lang ≠ de), Slop-Check 5/5 | Entwurf |
| `src/ap.css`, `src/ap.js`, `src/build.py` | Portal-Modul und Bau-Skript | auf Staging |

## Portal-Bau

1. Live-Datei frisch holen: `curl -s https://clients.741.studio/index.html -o live.html`
2. `python3 src/build.py live.html portal.html`. Erste Fassung: setzt Tab und Admin-Ansicht ein. Ist das Modul schon in der Live-Datei (seit 13.10. live), tauscht das Skript nur die eigenen Blöcke zwischen den Markern `Entscheidungen (Kunden-Freigabe)` und `Ende Entscheidungen`. Änderungen anderer Chats bleiben so erhalten. Die Martin-Figuren bettet `inline.py` ein.
3. Skript-Teil mit `node --check` prüfen
4. Backup nach `clients.741.studio/backup/`.
5. **Seit 13.10. (Martin): direkt live, kein Staging-Schritt für dieses Modul.** Upload nach `clients.741.studio/index.html`, danach live prüfen (nur lesen, wenn Chrome als Kunde angemeldet ist). Karten bleiben Entwürfe, bis Martin sie pro Element im Chat freigibt. Memory: `decisions-work-tasks-live-only.md`.

Stand 13.10.: Tab live seit 10:50 (Bali-Zeit). Kunden ohne freigegebene Elemente sehen keinen neuen Tab.

Ohne Tabellen bleibt der Tab unsichtbar. Das restliche Portal läuft normal (geprüft am 13.10. in Chrome als Admin).

## Was der Einbau macht

- Kunde: Tab „Entscheidungen“ mit Zähler, Filter, Varianten, „741 empfiehlt“, Warum-Zeile mit Quelle und Stand, SEO-Schloss, zwei Knöpfe („Passt so“, „Ich möchte etwas ändern“ mit Textfeld, Martin 13.10.), „ändern“ bis zum Go. Deep-Link `?view=decisions`.
- Martin-Figuren nur hier: hello oben, think beim ersten Punkt mit aktivem Ja, point beim ersten SEO-Schloss, celebrate wenn alles entschieden ist.
- Nur der benannte Entscheider kann entscheiden. Andere Logins sehen alles nur zum Lesen.
- Admin: Knopf „Entscheidungen · n offen · m bereit“ im Kundenkopf. Tabelle mit Status, „An Kunde geben“, „Go für live“ (zweiter Klick bestätigt), Einstellungen, Protokoll, Kundenansicht als Vorschau.
- Datenbank: Preis, Gesundheit, Behandlung und Recht erzwingen ein aktives Ja. Bei Gesundheitskunden geht kein Element ohne HWG-Prüfung raus. Eine Inhaltsänderung erzeugt eine neue Version und setzt die Entscheidung zurück. Nach dem Go ist das Element gesperrt. Das Protokoll ist nur anhängbar.

## Nicht im Umfang

- Formular zum Anlegen von Elementen im Portal. Elemente kommen per SQL aus den Workflows (Audit, Content-Pool, CRO, Seitenbaum, Google-Profil).
## Sprache (seit 13.10.)

- Die Kundenansicht folgt `clients.lang`: `de` → Deutsch, jede andere Sprache (`en`, `id`) → Englisch. Texte stehen in `AP_TX` in `src/ap.js`. Die Tab-Beschriftung kommt aus `apTabLabel(b)`.
- Die 741-Ansicht (Admin) bleibt deutsch. Die Vorschau „Kundenansicht ansehen“ zeigt die Kundensprache.
- `build.py` stellt im Update-Modus die alte deutsche Tab-Beschriftung einmalig auf `apTabLabel(b)` um.
- Mail-Entwurf `02-mails-draft.sql`: englischer Zweig in `approval_build_mail` (Datum „20 Oct“). Getestet am 13.10. nur in einer Transaktion mit Rollback, nichts angewendet.
- Varianten mit `"ask_note": true` zeigen ein Pflichtfeld über „Passt so“ / „Looks good“. Gespeichert wird `approve_with_change` mit Notiz (Martin 13.10.). Gesetzt bei Bali B2-A und B5-B.
- Große Schrift bei `kind = price` nur, wenn die Variante eine Zahl enthält (Martin 13.10.).
- Tests: `screenshots/en-2026-10-13/` (EN Bali Healing, DE Testpraxis, Desktop und 390 px).
