# Team-/Outreach-Dashboard — Strukturplan

**Stand:** 20.08.2026 · Grundlage: CRM-Sheet (164 Zeilen) + bestehendes Kundenportal

---

## 1. Wo es leben soll — Empfehlung: **gleiche URL, gleicher Login**

`clients.741.studio` behalten, **keine** neue Domain. Begründung:

- Auth, Rollen-System (`profiles.role`) und RLS existieren bereits und sind erprobt
- Eine Codebasis, ein Deploy, ein Passwort pro Person
- Eine neue Subdomain würde trotzdem auf dieselbe Datenbank zeigen → kein Sicherheitsgewinn,
  nur doppelte Pflege. **Die echte Grenze ist die RLS, nicht die URL.**

**Aber ein Risiko benennen:** Das Portal ist kundenseitig. Interne Team-Daten in derselben App heißt,
ein Fehler in der Rollenprüfung kann Internes für Kunden sichtbar machen (genau dieser Fehler ist mir
beim Standup schon einmal passiert). Gegenmaßnahmen, verbindlich:
- Interne Daten in **eigenen Tabellen**, nie in bestehende Kundentabellen mischen
- Jede interne Funktion mit explizitem Rollen-Guard (`raise 'staff only'`)
- Nach jedem Release **Gegentest mit einem echten Kunden-Token** (0 Zeilen erwartet)
- Kunden-Zugangsdaten (`client_credentials`) bleiben **admin-only** — Outreach-Leute sehen sie nie

---

## 2. Rollen

| Rolle | Wer | Sieht | Darf |
|---|---|---|---|
| `admin` | Martin | alles (Kunden + Team + Tresor) | alles |
| `manager` | Gayo | alle Outreach-Daten, alle Team-Mitglieder, alle Prospects | zuweisen, Ziele setzen, Reports lesen |
| `staff` | Outreach-Leute | **eigene** Tagesplanung/Reports + die ihnen zugewiesenen Prospects | eigene Aktivitäten erfassen |
| `client` | Kunden | unverändert nur eigene Kundendaten | unverändert |

**Offene Entscheidung für dich:** Soll Gayo als zweiter Haupt-Admin auch den **Kunden-Zugangsdaten-Tresor**
und Rechnungen sehen? Technisch trennbar — „alles Outreach" ≠ „alles Kunden".

---

## 3. Datenmodell (Supabase, neue Tabellen)

**`team_members`** — user_id, name, rolle, aktiv, LinkedIn-Seat(s), Zeitzone, Wochenstunden-Soll

**`prospects`** — das CRM, Sheet-Spalten plus die fehlenden Felder:
- vorhanden: company, contact_name, linkedin_url, email, lead_source, type, account/seat,
  pipeline_status (To Pitch / Pitched / In Pipeline), connection_status (Request Sent / Connected)
- **neu und entscheidend:** `owner_id` (wer betreut), `next_action_date` (NAD — heute 0× genutzt),
  `last_contact_at`, `outcome` (keine Antwort / geantwortet / Termin / gewonnen / verloren), `market`

**`outreach_activities`** — jede einzelne Berührung (das Herzstück für „wer hat wen"):
prospect_id, member_id, channel (linkedin/email/call), action (connect_request / message /
follow_up / reply_received / call_booked), occurred_at, notes

**`daily_plans`** (morgens) — member_id, datum, vorhaben (Text), Ziel-Anzahl, Segment/Markt

**`daily_reports`** (abends) — member_id, datum, erledigt (Text), Zahlen (Requests / Nachrichten /
Antworten / Termine), **Arbeitsstunden**, Blocker

> Die Zahlen im Abendreport werden aus `outreach_activities` **vorgeschlagen**, nicht abgetippt —
> sonst wird geschätzt statt gemessen.

---

## 4. Täglicher Ablauf

**Morgens** → Staff loggt sich ein, sieht „Heute geplant"-Feld + seine offenen NADs → trägt Vorhaben + Zielzahl ein
**Tagsüber** → Aktivitäten erfassen (einzeln oder Sammel-Eintrag; später Import aus LinkedIn-Export)
**Abends** → „Tagesabschluss": erledigt, Zahlen (vorbefüllt), Stunden, Blocker
**Für dich + Gayo** → ein Board: heute geplant vs. geliefert, pro Person; Wochensummen;
Antwortquote je Person; überfällige NADs; wer wen kontaktiert hat

---

## 5. Sheets oder Datenbank? — Empfehlung: schrittweise

**Phase 1 (schnell, kein Risiko):** Tagesplanung + Tagesreport **neu im Dashboard**.
Das ist der eigentliche Mehrwert und existiert heute nirgends. CRM bleibt im Sheet.

**Phase 2:** Sheet **read-only nach Supabase spiegeln** (nächtlicher Sync) → Prospects werden im
Dashboard sichtbar, ich kann sie zusammenfassen. Gearbeitet wird weiter im Sheet.

**Phase 3 (erst wenn das Team es will):** CRM-Bearbeitung ins Dashboard, Sheet wird abgelöst.

**Warum nicht sofort alles migrieren:** Das Sheet ist die Muskelerinnerung des Teams. Ein Werkzeugwechsel
mitten im laufenden Outreach kostet Durchsatz. Erst Sichtbarkeit schaffen, dann Werkzeug tauschen.

---

## 6. Was ich als Agent dann liefern kann

Wie beim Kunden-Standup (`daily_standup()` läuft bereits werktags):
- **Team-Standup morgens:** wer hat was vor, wer hat gestern was geliefert, wo klemmt es
- **Wochenauswertung:** Aktivitäten je Person, Antwortquote, Termine, Stunden vs. Ergebnis
- **Pipeline-Hygiene:** überfällige NADs, Prospects ohne Owner, seit X Tagen unberührt
- **Rohdaten-Zusammenfassung** über alle Quellen hinweg in einem Brief

---

## 7. Lücken im heutigen Sheet, die mitgefixt werden müssen

1. **Keine Personen-Spalte** → ohne `owner_id` ist „wer hat wen kontaktiert" unbeantwortbar
2. **NAD 0 von 164 gefüllt** → Follow-ups laufen aktuell auf Zuruf
3. **Notes 0 von 164** → kein Kontext für Übergaben
4. **Kein Ergebnisfeld** → „Pitched" sagt nicht, ob geantwortet wurde
5. **Keine Zeitkomponente** → Stunden müssen neu erfasst werden, aus dem Sheet nicht rekonstruierbar
6. Nur 9 brauchbare E-Mails bei 164 Kontakten → Kanal ist praktisch rein LinkedIn

---

## 8. Vorschlag Reihenfolge

1. Rollen `manager` + `staff` einführen, RLS + Gegentest mit Kunden-Token
2. `daily_plans` / `daily_reports` + Formulare (morgens/abends) — **Phase 1 live**
3. Team-Board für Martin + Gayo
4. Sheet-Spiegelung (`prospects`) + Agent-Wochenbericht
5. Aktivitäten-Erfassung, danach optional CRM-Umzug

---

## ✅ ENTSCHEIDUNGEN MARTIN (20.08.2026)

**Gleiche URL + Rollen — bestätigt.** `clients.741.studio`, kein neuer Login.

**ZWEI GETRENNTE ADMINISTRATIONSBEREICHE** (Kernentscheidung):

| Bereich | Inhalt | Wer |
|---|---|---|
| **A · Kundenbetreuung / Delivery** | Kunden, 90-Tage-Programme, Aufgaben, Reports, **Zugangsdaten-Tresor** (Coralie, Hüwel …) | Martin (+ Dinakar als Entwickler) |
| **B · Outreach & Sales** | Team, Tagespläne, Tagesreports, Aktivitäten, Prospect-Auswertungen | Martin (Admin), **Gayo (Manager)**, Outreach-Leute (Staff) |

Die Bereiche sind **übergeordnet getrennt** — nicht ineinander verschachtelt.
**Gayo ist NICHT Voll-Admin:** Er sieht das Outreach-Board (wer macht was), kann in den Accounts
anderer Outreach-Leute **kommentieren/vermerken** — hat aber **keinen** Zugriff auf Bereich A
(Kundendaten, Programme, Zugangsdaten-Tresor).

**Datenfluss:** Die Eingaben der Outreach-Leute laufen im Admin-Account zusammen (Aggregation nach oben).

**Sheet-Anbindung — korrigiert:** Die Prospect-Daten werden **NICHT** ins Portal gespiegelt/dupliziert.
Das Sheet bleibt das Sheet. Im Dashboard erscheinen **ausschließlich Zusammenfassungen und Zählungen**.

**Phase 1 startet:** Tagesplan + Tagesreport, jeder loggt sich ein und macht seine Vermerke.

**Benachrichtigung — Martins eigentliches Bedürfnis:** Er will nicht jeden Report einzeln lesen.
Er will wissen: **Fängt überhaupt jemand an zu arbeiten?** Wenn kein Anfangsreport kommt, läuft keine Aktivität.
→ Umsetzung: Dashboard ist die Quelle der Wahrheit, **plus Ausnahme-Meldung** (nur wenn etwas fehlt),
nicht der Volltext jedes Reports.

---

## Rollen-Technik (ohne Bestehendes zu gefährden)

`profiles.role` bleibt unverändert (`admin` / `client`) — damit ist die bestehende Kunden-RLS nicht angefasst.
Neu **parallel** dazu:

- Tabelle `team_members`: user_id, name, `level` (`manager` | `member`), aktiv
- Helper `is_team_manager()` / `is_team_member()`; Martin als `admin` besteht beide implizit
- Bereich B liest **nie** aus Kundentabellen, Bereich A **nie** aus Team-Tabellen
- Pflicht nach jedem Release: Gegentest mit echtem **Kunden-Token** (0 Zeilen) **und** mit **Staff-Token**
  (kein Zugriff auf `clients` / `client_credentials`)
