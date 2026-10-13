# Kunden-Freigabe im Portal: Einbau (Stand 2026-10-13)

Workflow-Schritt 3: Einbau ins Portal `clients.741.studio`, nur auf Staging. Vorlage: `../prototype/index.html`. Regeln: `../brief.md`.

## Dateien

| Datei | Inhalt | Status |
| --- | --- | --- |
| `01-migration.sql` | Tabellen `client_approval_settings`, `approval_items`, `approval_decisions`, Trigger, RPCs, RLS | Probelauf mit Rollback OK, **wartet auf Go** |
| `02-mails-draft.sql` | Tag-7-Regel, Sammel-Mail (max. 1 pro Tag), Erinnerung Tag 3, Versand mit BCC an martin@741.studio | **Entwurf, nicht aktiv** |
| `03-seed-testpraxis.sql` | Testpraxis Musterstadt mit den 5 Beispiel-Elementen aus dem Prototyp | **wartet auf Go** |
| `04-rls-tests.sql` + `04-rls-dryrun-result-2026-10-13.txt` | 20 RLS- und Regel-Tests, alle OK | fertig |
| `mail-digest-text.txt`, `mail-reminder-text.txt` | Mailtexte, Slop-Check 5/5 | Entwurf |
| `src/ap.css`, `src/ap.js`, `src/build.py` | Portal-Modul und Bau-Skript | auf Staging |

## Portal-Bau

1. Live-Datei frisch holen: `curl -s https://clients.741.studio/index.html -o live.html`
2. `python3 src/build.py live.html portal.html` (setzt Tab, Admin-Ansicht und bettet die Martin-Figuren per `inline.py` ein)
3. Skript-Teil mit `node --check` prüfen
4. Backup nach `clients.741.studio/backup/`, Upload NUR nach `clients.741.studio/staging/index.html`
5. Live nur nach Martins ausdrücklichem Go

Ohne Tabellen bleibt der Tab unsichtbar. Das restliche Portal läuft normal (geprüft am 13.10. in Chrome als Admin).

## Was der Einbau macht

- Kunde: Tab „Entscheidungen“ mit Zähler, Filter, Varianten, „741 empfiehlt“, Warum-Zeile mit Quelle und Stand, SEO-Schloss, zwei Knöpfe („Passt so“, „Ich möchte etwas ändern“ mit Textfeld, Martin 13.10.), „ändern“ bis zum Go. Deep-Link `?view=decisions`.
- Martin-Figuren nur hier: hello oben, think beim ersten Punkt mit aktivem Ja, point beim ersten SEO-Schloss, celebrate wenn alles entschieden ist.
- Nur der benannte Entscheider kann entscheiden. Andere Logins sehen alles nur zum Lesen.
- Admin: Knopf „Entscheidungen · n offen · m bereit“ im Kundenkopf. Tabelle mit Status, „An Kunde geben“, „Go für live“ (zweiter Klick bestätigt), Einstellungen, Protokoll, Kundenansicht als Vorschau.
- Datenbank: Preis, Gesundheit, Behandlung und Recht erzwingen ein aktives Ja. Bei Gesundheitskunden geht kein Element ohne HWG-Prüfung raus. Eine Inhaltsänderung erzeugt eine neue Version und setzt die Entscheidung zurück. Nach dem Go ist das Element gesperrt. Das Protokoll ist nur anhängbar.

## Nicht im Umfang

- Formular zum Anlegen von Elementen im Portal. Elemente kommen per SQL aus den Workflows (Audit, Content-Pool, CRO, Seitenbaum, Google-Profil).
- Englische und indonesische Oberfläche für den Tab (Pilot ist deutsch).
