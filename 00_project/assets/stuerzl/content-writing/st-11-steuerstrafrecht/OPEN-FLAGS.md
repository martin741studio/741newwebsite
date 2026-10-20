# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Stürzl, Steuerstrafrecht Säulenseite ST-11)

Lies diese Datei, bevor du an dieser Seite weiterarbeitest. Stand 2026-10-11, nach der Korrekturrunde (REVIEW-B, `content-writing-stuerzl-fixes.md`). Die Vorversion steht in `05-final/page-vorreview.md`. Fragen an die Kanzlei stellen wir erst, wenn sie alles zur Bestätigung bekommt.

## A. Rechtsgrauzonen (BRAO / UWG), nicht vom Agenten zu entscheiden

| # | Stelle im Text | Frage | Aktueller Stand |
| --- | --- | --- | --- |
| A1 | S01, H1 und Title: "Anwalt für Steuerstrafrecht" | Kann als Fachgebietsbezeichnung gelesen werden (BORA, Fachanwaltsordnung). Das Review (REVIEW-B, ST-11 Punkt 5) schlägt "Steuerstrafrecht: Verfahren und Verteidigung" vor. | Von Martin freigegeben (fixes Punkt 13), bleibt in H1 und Title. Kanzlei prüft. Gleiche Frage wie bei /selbstanzeige/ (A3). |
| A2 | S05: Titel "Fachanwältin für Steuerrecht" und "Zertifizierte Beraterin für Steuerstrafrecht (DAA)" | Titel stammen aus dem Lebenslauf, nicht aus einem Kammernachweis (B5 der Kanzlei-Flags). | Kanzlei bestätigt. |
| A3 | S05: Dozentin im Lehrgang DAA, Gastdozentin Bundesfinanzakademie, Rechtsprechungsübersicht NZWiSt (mit Stefan Rolletschke) | Aus dem Live-Profil, gegenwärtiger Stand nicht belegt. Nennung eines Dritten als Mit-Autor. | Text steht so. Kanzlei bestätigt. |
| A4 | S07 Block 1 und 3, FAQ: Strafrahmen 5 Jahre, 6 Monate bis 10 Jahre; Verjährung; Festsetzungsfrist 10 Jahre | Nach dem Review korrigiert: fünf Jahre im Grundfall (§ 78 Abs. 3 Nr. 4 und Abs. 4 StGB, abgeleitet, nicht wörtlich); 15 Jahre nur in den Fällen des § 370 Abs. 3 Satz 2 Nr. 1 bis 6 AO (§ 376 Abs. 1 AO); Spätestgrenze im Grundfall das Doppelte (§ 78c Abs. 3 Satz 2 StGB), in den Fällen des § 376 Abs. 1 AO das Zweieinhalbfache (§ 376 Abs. 3 AO). Beginn und Beendigung der Tat in der Praxis (Rechtsprechung) nicht gelesen, daher nicht behandelt. | Text steht so. Kanzlei prüft. |
| A5 | **Die Live-Seite selbst** nutzt "Spezialisierung", "besondere fachliche Expertise", "Experten", "bestmögliche Beratung" (Text der Säulenseite) | Möglicher Verstoß gegen § 43b BRAO / UWG. | Nur hier im Hinweis, nicht im Text. Martin entscheidet über den Hinweis an die Kanzlei (Un-Burning D11). |
| A6 | S07 Block 5: "verteidigen wir auch konfrontativ" (Wendung der Live-Kanzleiseite, auch im Zitat in S05) | Kann als Kampfrhetorik gelesen werden. "Kämpfen bis zum Ende" und "hart in der Sache" sind nicht übernommen. Der Satz "Dort gibt es zahlreiche Möglichkeiten, auf die Ermittlungen einzuwirken" ist gestrichen. | Text steht so. Kanzlei und Martin entscheiden einmal für alle Seiten (REVIEW-B, Querpunkt 9). |
| A7 | FAQ "Welcher Anwalt hilft bei Steuerhinterziehung?" | Echte PAA-Frage. Die Antwort nennt die eigenen Titel (sachlich). | Text steht so. Kanzlei prüft. |
| A8 | S07 Block 2: "Häufig erfahren Betroffene davon bei einer Durchsuchung" | Aussage aus der Live-Seite ST-12, nicht aus dem Gesetz. | Kanzlei bestätigt. |
| A9 | S07 Block 5: "viele Verfahren enden bereits im Ermittlungsverfahren" | Aussage der Kanzlei (Live-FAQ II.1), kein Gesetzestext. | Text steht so. Kanzlei bestätigt. |
| A10 | S07 Block 4: § 153 Abs. 1 AO | Nach dem Review mit den Bedingungen "Steuerpflichtiger" und "vor Ablauf der Festsetzungsfrist" wiedergegeben. Die Selbstanzeige selbst (§ 371 Abs. 2 AO) steht nicht auf dieser Seite, nur der Verweis auf /selbstanzeige/. | Erledigt. |

## B. Widersprüche im Kundenmaterial und offene Entscheidungen

| # | Widerspruch | Quellen | Stand |
| --- | --- | --- | --- |
| B1 | Vergütung: freigegebene Startseite sagt "Vergütung nach RVG oder Vereinbarung" (Schritt 4). Neuester Kundentext sagt "kein RVG, nach Zeitaufwand". | `cro/04-copy/approved-copy.md` gegen `client-texte/kosten.txt` | Diese Seite folgt dem Kundentext und den drei Kernsätzen aus dem Fix-Auftrag, keine Beträge. Startseite anpassen. |
| B2 | Erstberatung: Live-Kanzleiseite "Festpreis", Live-FAQ andere Sätze, neuer Text "Pauschale". | `kanzlei.txt`, Live-FAQ, `kosten.txt` | Platzhalter entfernt. Die Seite sagt nur "üblicherweise gegen Pauschale". Der Betrag steht nur auf /kosten/ (ST-31). |
| B3 | Kannibalisierung (Regel S6): Das Sitetree gibt "anwalt steuerstrafrecht" an ST-00, ST-10 und ST-11. | `sitetree.json` | ST-11 behält es als Säulenseite ohne Stadt. ST-10 (Hub) nimmt "leistungen steuerstrafrecht". ST-00 trägt es laut freigegebenem CRO-Brief auch. Martin entscheidet. |
| B4 | Ratgeber-Links (/ratgeber/steuerhinterziehung-strafe/, /ratgeber/verjaehrung/) führen auf Seiten mit Status "Vorschlag". | `sitetree.json`, `slugs.json` | Beide Seiten (ST-35, ST-36) sind geschrieben und stehen in slugs.json. Links entfernen, falls die Ratgeber nicht gebaut werden. |
| B5 | Die Live-Säulenseite zeigt vier Kacheln (Selbstanzeige, Gutachten, Durchsuchung, Verteidigung). Die neue Seite führt über Text und Links zu den Kind-Seiten. | Live-Seite | Hinweis an 741. |
| B6 | Der Seitenpfad wechselt von /index.php/steuerstrafrecht zu /steuerstrafrecht/. Weiterleitung nötig, Seite nicht live ändern (Page-Swap-Regel). | `slugs.json` | Offen für den Livegang. |
| B7 | Vorschläge aus REVIEW-B, die Kanzlei-Freigabe oder Technik brauchen: Prüfzeile "Fachlich geprüft von Dr. Anja Stürzl, Rechtsstand Oktober 2026" und Person-Schema für Dr. Stürzl auf dieser Seite. | REVIEW-B, `schema_tool.py` (Person nur auf Personenseiten) | Nicht umgesetzt. Martin entscheidet, ob die Kanzlei die Prüfzeile erlaubt. Der Rechtsstand steht schon im Text. |
