# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Stürzl, Team, ST-44)

Stand 2026-10-11 (Fix-Runde nach REVIEW-E). Martin: Fragen an die Kanzlei stellen wir erst, wenn sie alles zur Bestätigung bekommt. Keine Bestätigung der Kanzlei liegt vor; offene Punkte stehen als "offen".

## A. Rechtsgrauzonen (BRAO / UWG)

| # | Stelle im Text | Frage | Stand |
| --- | --- | --- | --- |
| A1 | S03: „angestellt“ bei Lea Wimmer, Dr. Glogger, Thorben Hoppe | Die Live-Seite nennt sie „Salary Partner/in“ mit Fußnote „Angestellte Rechtsanwältin/Angestellter Rechtsanwalt“. „Partner“ für Angestellte kann als Hinweis auf eine Gesellschafterstellung gelesen werden (Berufsrecht, UWG). Der Text schreibt „angestellt“, die Fußnote der Kanzlei. | offen: Kanzlei entscheidet über ihre Wortwahl. |
| A2 | S03: Titel Lea Wimmer „Fachanwältin für Steuerrecht“ (Live-Profil: seit 2017), Dr. Glogger „Zertifizierter Compliance Officer (Univ. Münster)“ (Live-Profil: 2024) | Titel stammen aus den Live-Profilen, nicht aus Kammernachweisen. `nap.json` führt für Dr. Glogger keine Titel („Rechtsanwältin“). | offen. |
| A3 | S03: Rechtsgebiete bei Thorben Hoppe, Florentine Jilg | Hoppe: Die Karte nennt jetzt „Strafrecht, Steuerrecht sowie Compliance“ (Wortlaut des Live-Profils, REVIEW-E Textlücke 1). „Strafrecht“ allein ist kein belegtes Rechtsgebiet der Kanzlei (client-baseline.md); die Kanzlei entscheidet, ob die Zeile so bleibt. Jilg: Live-Profil nennt „Schwerpunkt im Medizinstrafrecht, Jugendstrafrecht und Sanktionen“ („Schwerpunkt“ ohne Beleg, außerhalb der Leistungen). Die Karte nennt keine Rechtsgebiete. | offen. |
| A4 | Karte „Mary, Chief Barking Officer (CBO)“ | Entfernt in der Fix-Runde (REVIEW-E Punkt 2). Das Live-Profil beschreibt Mary (Bürohündin laut Text) als Beraterin von Mandanten mit „Tätigkeitsschwerpunkt Steuerstrafrecht“ (Humor). Auf einer Anwaltsseite kann das irreführen (UWG). Zurück nur mit klarem Hinweis „Bürohund“ und Go der Kanzlei. | erledigt; Rückkehr offen. |
| A5 | Live-Teamseite | Nutzt „Spezialisierung bringt Spitzenleistung!“ und „kompromisslose Verteidigung“, Meta-Keywords „Expertise“, „Spezialisierung“. | Nicht übernommen. Nur im Hinweis. |
| A6 | S04: „Wir sind überzeugt, dass kreative Verteidigungsansätze entstehen, wenn unterschiedliche Charaktere eng zusammenarbeiten“ | Live-Text: „Nur wer mit unterschiedlichen Charakteren eng zusammenarbeitet, findet kreative Verteidigungsansätze“ (absolute Qualitätsaussage). Die Seite formuliert es als Überzeugung (REVIEW-E Punkt 4). | erledigt. |
| A7 | S04 (früher): „und Sie haben eine verlässliche Erreichbarkeit“ | Gestrichen (REVIEW-E Punkt 3). Die Aussage stammt aus dem unveröffentlichten Kostentext (`kosten.txt`), Erreichbarkeitszeiten sind nicht belegt. | erledigt. |
| A8 | S03: E-Mail-Adressen der vier Anwältinnen und Anwälte | Stehen auf den Live-Profilseiten. Direkte Adressen auf der Team-Seite sind neu. | offen: Kanzlei bestätigt. |
| A9 | S02, S04: Vier-Augen-Prinzip | Quelle ist der unveröffentlichte Kostentext. Eine Selbstauskunft, kein nachprüfbarer Beleg. | Die Seite /kosten/ muss im selben Go live gehen. |

## B. Widersprüche im Kundenmaterial

| # | Widerspruch | Quellen | Stand |
| --- | --- | --- | --- |
| B1 | Die Pool-Daten sagen, die Teamseite rankt für Pösl, Kellner, Brunzel, Euler, Fenzl, Scherübel. Der sichtbare Live-Text nennt keinen dieser Namen. Im HTML stehen Alt-Texte „Dr. Philipp Kellner, Rechtsanwalt \| Associate“ (am Foto von Dr. Glogger), „Alice Laporte, Human Resources“ und „Nellie Runhaar, Office Managerin“. /index.php/cedric-euler liefert 404. Pressemeldungen (LTO 10.10.2024 und 23.06.2025, ZRI 09.10.2024) nennen Dr. Philipp Kellner als Rechtsanwalt der Kanzlei im Münchner Büro; die aktuelle Teamseite führt ihn nicht. | `_work/live/team.html`, `ranked-stuerzl-steuerstrafrecht.de.json` | Frage an die Kanzlei: Sind das ehemalige Kolleginnen und Kollegen? Die Namen stehen nur in dieser Datei, nicht auf der Seite und nicht im Technikblock. Alt-Texte beim Relaunch ersetzen. |
| B2 | Dr. Glogger ist laut Source of Truth „50 % Teilzeit, seit April 2026“; Live-Profil „4/2026 … bei STÜRZL (München)“. | Source of Truth Tab 01 Z46 | Kein Widerspruch im Text; Teilzeit steht nicht auf der Seite. |
| B3 | München: Lea Wimmer laut Live-Profil seit 7/2025, Büro laut Lebenslauf Dr. Stürzl seit 03/2026, Source of Truth „seit Anfang 2026“, ZRI 09.10.2024 „spätestens zum Januar 2025“. | Live-Profile, ZRI, `nap.json` | Karten nennen keine Eintrittsdaten und keine Eröffnung (Fix-Runde: kein Datum auf der Seite). |
| B4 | Rolle von Florentine Jilg: Live-Karte „Wissenschaftliche Mitarbeiterin“, Source of Truth Tab 01 Z46 „Organisation/IT“, Tab 02 Z45 „Organisation, Adresse, Fotos“. | Live-Karte, `source-of-truth-2026-10-11.md` | Die Karte folgt dem Source of Truth: „Organisation und IT“ (REVIEW-E Punkt 5). Frage an die Kanzlei in placeholders.md. |
| B5 | Thorben Hoppe: ST-41 sagt, er berate in Frankfurt und München seit Juni 2026. ST-43 und ST-44 nannten früher nur Frau Dr. Stürzl (Frankfurt) und Frau Wimmer und Dr. Glogger (München). | Live-Profil Hoppe, RWS-Meldung 18.06.2026 | Behoben: ST-43 und ST-44 nennen ihn jetzt an beiden Standorten. |

## C. Workflow-Hinweise

1. Fix-Runde 2026-10-11: Sicherung `05-final/page-vorreview.md`, neuer Entwurf `03-draft/draft-v3.md`. Kein Cleanse-Aufruf (nur kleine Änderungen). Frühere Cleanse-Datei r1 bleibt als Verlauf.
2. Profilseiten der Assistenz (ST-48) bleiben bestehen; die Team-Seite verlinkt sie nicht. Es gibt keine Sitemap-Zeile für Thorben Hoppe und Florentine Jilg (ST-48 leer in `slugs.json`). Der Link `/thorben-hoppe/` ist entfernt (REVIEW-E Punkt 1).
3. Fotos: Freigabe der Abgebildeten und echte Dateien nötig. Die Live-Seite enthält Fotos; ob die Personen zustimmen, ist nicht dokumentiert. Alt-Texte: Name und Rolle der abgebildeten Person.
4. Wettbewerber-Messung nur Information (Typ C). Median 477 Wörter.
5. Schema: `05-final/schema.jsonld` ist da (WebPage, BreadcrumbList, LegalService). Person-Schema liegt auf ST-45 und ST-46; `sameAs` bleibt überall leer, bis Profile geprüft sind.
6. Bewusst offen: keine FAQ-Blöcke (Markenseite Typ C, keine PAA-Daten); keine Straßenadresse im Fließtext der Karten (der Adressblock am Ende nennt beide Büros).
