# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Stürzl, Dr. Monika Glogger, ST-46)

Stand 2026-10-11 (Fix-Runde nach REVIEW-E). Martin: Fragen an die Kanzlei stellen wir erst, wenn sie alles zur Bestätigung bekommt. Keine Bestätigung der Kanzlei liegt vor; offene Punkte stehen als "offen".

## A. Rechtsgrauzonen (BRAO / UWG)

| # | Stelle im Text | Frage | Stand |
| --- | --- | --- | --- |
| A1 | S01, S03: „Zertifizierter Compliance Officer (Univ. Münster)“ seit 2024 | Titel nur aus dem Live-Profil. Nicht in `nap.json`. Ob es ein geschützter oder ein Hochschulzertifikat-Titel ist, belegt die Quelle nicht. | offen: Kanzlei bestätigt Wortlaut und Quelle. |
| A2 | S01: „angestellt“ statt „Salary Partnerin“ | Die Live-Seite nennt „Salary Partnerin*“ mit Fußnote „Angestellte Rechtsanwältin“. „Partner“ kann irreführen (UWG). | offen: Kanzlei entscheidet. |
| A3 | H1 und S01: „Rechtsgebiete Wirtschaftsstrafrecht und Compliance“ | Live-Profil nennt die drei Rechtsgebiete. Keine Fachanwaltsbezeichnung. Text sagt „Rechtsgebiete“, nie „Fachanwältin“ oder „Schwerpunkt“. | Steht so. |
| A4 | S04: Compliance-Leistungen aus `compliance.txt` | Der Kundentext nennt „Haftung zu vermeiden“ und „Sanktionsrisiken … zu vermeiden“. Beides ist nicht übernommen. Wer den Textbaustein geschrieben hat, ist nicht belegt. Die Überschrift lautet jetzt „Compliance bei STÜRZL Steuerstrafrecht“, nicht mehr „Wobei Dr. Glogger Unternehmen begleitet“ (REVIEW-E Punkt 3). | offen: Kanzlei prüft Wortwahl. |
| A5 | S04: „Dr. Glogger kennt Compliance aus der Praxis eines Unternehmens.“ | Ableitung aus dem Lebenslauf (Syndikusrechtsanwältin und Compliance Officer 2022 bis 2026). Der zweite Halbsatz „und aus der Beratung durch eine Kanzlei“ ist gestrichen: Der Lebenslauf zeigt Stationen bei Ufer Knauer und Streck Mack Schwedhelm ohne Compliance-Rolle (REVIEW-E Punkt 4). | offen: Kanzlei bestätigt. |
| A6 | Live-Meta-Description der Seite | Nutzt „Spezialisierung“. Nicht übernommen. | Nur im Hinweis. |

## B. Widersprüche im Kundenmaterial

| # | Widerspruch | Quellen | Stand |
| --- | --- | --- | --- |
| B1 | Alle zehn Veröffentlichungen stehen unter dem Autorennamen „Werndl“. Der Bezug zu Dr. Glogger ist auf der Seite nicht erklärt. | Live-Profil | Zurückgehalten in der Fix-Runde (REVIEW-E Punkt 1 und 2, Entscheidung Martin): S06 zeigt nur die Mitgliedschaft (JuWiSt, vom Live-Profil als ihre ausgewiesen) und einen Platzhalter. Der Satz „Veröffentlichungen zum Unternehmensstrafrecht in Fachzeitschriften“ in S03 ist durch die JuWiSt-Mitgliedschaft ersetzt. Die Dissertation (Nomos 2019, „Zweispurigkeit und Vertrauensschutz …“, der Beleg für „Dr.“) bleibt ebenfalls zurückgehalten. Der Werdegang nennt weiter „Promotion … Universität Augsburg 2014 bis 2017“ (Lebenslauf, ihr Name). Rückkehr der Liste erst nach Bestätigung des Autorennamens. |
| B2 | Das Foto trägt den Alt-Text „Dr. Philipp Kellner“. Eine Pressemeldung (LTO 2024, ZRI 2024) nennt Dr. Philipp Kellner als Rechtsanwalt der Kanzlei in München. | Live-HTML (`_work/live/dr-monika-glogger.html`), LTO und ZRI | Frage an die Kanzlei: Ist er ausgeschieden? Die Teamseite nennt ihn nicht. |
| B3 | Teilzeit (50 %, seit April 2026) | Source of Truth Tab 01 Z46 | Steht nicht auf der Seite (Mandatsaussage nicht nötig). |
| B4 | Telefon im Profil: +49 89 72 44 41 70 (München). Das entspricht `nap.json`. | Live-Profil, `nap.json` | Kein Widerspruch. |

## C. Workflow-Hinweise

1. Früherer Lauf: 1 Cleanse-Aufruf, eine kleine Rhythmus-Änderung in S04 (Satz geteilt), Diff PASS (`draft-v2.md`). Aktuelle Fassung: `03-draft/draft-v3.md` (Fix-Runde).
2. Die Seite zitiert keine Gesetze; die Zeile „Stand der Liste: Oktober 2026“ steht trotzdem sichtbar.
3. Fotos: echte Dateien und Freigabe der Abgebildeten fehlen.
4. Wettbewerber-Messung nur Information (Typ C).
5. Fix-Runde 2026-10-11: Sicherung `05-final/page-vorreview.md`, neuer Entwurf `03-draft/draft-v3.md`. Kein Cleanse-Aufruf. Der Name des früheren Kollegen steht nur in dieser Datei (B2), nicht mehr im Technikblock und nicht in `placeholders.md`.
6. Person-Schema (`05-final/schema.jsonld`, aus `nap.json`): bereit sind `name` (Dr. Monika Glogger), `jobTitle` („Rechtsanwältin“) und `worksFor` (`https://stuerzl-steuerstrafrecht.de/#kanzlei`). `hasCredential` ist leer, weil `nap.json` für Dr. Glogger keine Titel führt; der Titel „Zertifizierter Compliance Officer (Univ. Münster)“ (2024) steht im Text und im Live-Profil und kann nach Bestätigung dort ergänzt werden. `sameAs` bleibt leer: Der LinkedIn-Link der Live-Profilseite liefert 404 (Source of Truth Tab 02 Z33, fehlendes https://). Nicht bereit: `image`, Veröffentlichungen.
7. Offene Frage zum Inhalt: Welche Compliance-Mandate betreut Dr. Glogger persönlich? S04 beschreibt die Leistungen der Kanzlei (Kundentext ohne Autor). Das Source of Truth (Tab 02 Z45) führt sie als Ansprechpartnerin für „Texte/Website, Compliance, Kosten“; das ist keine Aussage zu ihren Mandaten.
8. Büro-Link und Adressblock stehen jetzt in S07 (REVIEW-E: kein /kontakt/-Link, keine Adresszeile).
