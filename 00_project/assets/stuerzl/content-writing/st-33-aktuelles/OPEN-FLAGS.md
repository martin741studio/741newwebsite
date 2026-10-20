# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Stürzl, Aktuelles, ST-33)

Lies diese Datei, bevor du an dieser Seite arbeitest. Stand 2026-10-11, nach der Korrekturrunde (REVIEW-F).

## A. Rechtsgrauzonen (BRAO / UWG), nicht vom Agenten zu entscheiden

| # | Stelle | Frage | Aktueller Stand |
| --- | --- | --- | --- |
| A1 | **Beitragsliste der Live-Seite (CMS, nicht Teil dieses Textes). RISIKO: Die Liste erscheint unter dem Einleitungstext und trägt die Teaser der Kanzlei unverändert auf die neue Seite.** Betroffene Teaser (Wortlaut der Live-Seite vom 2026-10-11): (1) „Neue JUVE-Rankings: Wie Frauen im Strafrecht zur festen Größe wurden“ (Ranking-Bezug, Auszeichnung); (2) Podcast IMS024: „Dr. Anja Stürzl ist erfolgreiche Gründerin einer Boutique-Kanzlei“ (Erfolgs- und Selbstlob-Aussage); (3) Seminar PStRneo: Vortrag „Business Case: Steuerstrafrecht – Spezialisierung, Personal Brand“ („Spezialisierung“ ist ein Wort der BORA-Liste, § 7 BORA); (4) **„Influencer*innen auf Social Media – Jetzt vor Strafverfolgung schützen!“** (Schutzversprechen als Ergebnis; Teaser-Text: „erkennen den Ernst der Lage oft erst, wenn das Finanzamt anklopft“ = Angstwirkung). Dazu als Hinweis: „Capital Magazin: Steuern hinterzogen? Das sollten Sie jetzt (nicht) tun“ (Titel einer Drittseite als Handlungsanweisung ohne Kenntnis des Falls) und „Kluge Köpfe im Strafrecht“ (Rubrik des Verlags). | Das kann gegen § 43b BRAO / UWG verstoßen (Selbstlob, Ranking-Werbung, Ergebnisversprechen) und widerspricht den Regeln der Fixes-Datei §2.8. | Nicht im Einleitungstext. **Vor dem Livegang: Kanzlei bittet um Umtitelung oder Kürzung der Teaser (1) bis (4) oder nimmt die Beiträge aus der Liste. Martin entscheidet, ob und wie die Kanzlei darauf hingewiesen wird.** Der Teaser-Titel (4) fehlte in der ersten Fassung dieser Datei (REVIEW-F ST-33 Punkt 2). |
| A2 | S01 und S02: „Interviews und Fachbeiträge von und mit Dr. Anja Stürzl“, Themenzeile | Beschreibt nur Art, Urheberin und Themen der Beiträge laut Liste, keine Wertung. Die Themenzeile folgt den Titeln der Liste (Stand 2026-10-11) und muss mit der Liste übereinstimmen, wenn sie sich ändert. | Text steht so. |
| A3 | S03: CTA „Vertraulich anfragen“ | Neu in der Korrekturrunde. Kein Adressblock (Fixes §2.5: nicht auf Aktuelles). | Text steht so. |

## B. Lücken im Kundenmaterial

| # | Lücke | Quellen | Stand |
| --- | --- | --- | --- |
| B1 | Der Ratgeber (ST-34) ist ein Vorschlag. Der Verweis in S02 gilt nur, wenn die Kanzlei ihn freigibt. | Sitetree | Verweis streichen, wenn der Ratgeber nicht kommt. |
| B2 | Die Seite „Veröffentlichungen, Vorträge und Presse“ (ST-49) entsteht in Batch E. Presseerwähnungen sind nicht freigegeben. | Source of Truth Tab 07, Batch E | Verweis steht. |
| B3 | Die Live-Seite hat keinen Einleitungstext und keine H1. Der Einleitungstext ist neu und braucht Freigabe. | Live-Seite | Entwurf. |
| B4 | Beiträge zu Dritten: Die Beiträge nennen Medien und Verlage (JUVE, Capital, C.F. Müller, Private Banking Magazin, IWW). Die Verlinkung braucht die Zustimmung der Kanzlei. | Live-Seite | Hinweis. |
| B5 | Das Wort „aktuelle Beiträge“ ist durch „Beiträge und Hinweise“ ersetzt: Die Liste reicht bis 2024 zurück (REVIEW-F ST-33 Punkt 3). | Live-Seite | Erledigt. |

## C. Workflow-Hinweise

1. Die Beitragsliste erzeugt das CMS. Der Text enthält H1, Themenzeile, Einleitungsabsatz und einen kurzen CTA-Block.
2. Link-Pfade nach `assets/stuerzl/slugs.json`, ohne `/index.php/`. Der CTA-Block gehört unter die Liste.
3. Schema: Die Seite bräuchte CollectionPage mit ItemList für die CMS-Liste. `schema_tool.py` kann das nicht. Gewünschte Änderung steht in FIX-F-report.md.
