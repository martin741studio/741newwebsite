# Gate A0 (voll): Stürzl, Compliance (ST-26)

Datum: 2026-10-11. Seitentyp A (Geldseite, neue Leistung, Pool-Priorität A). Modus: neu (die Seite gibt es nicht, Live-URL liefert 404).

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth | ja | `client-baseline.md`, `client-texte/compliance.txt` (370 Wörter), `pruefung-2026-10-11.md`, `source-of-truth-2026-10-11.md` (Compliance: höchste Marge, Priorität), Live-Profile Dr. Glogger und Dr. Stürzl, 2026-10-11. |
| 2 | Live-Bestand abgerufen und gezählt | ja, kein Bestand | https://stuerzl-steuerstrafrecht.de/compliance/ und /index.php/compliance liefern 404 (curl, 2026-10-11). Compliance ist heute nur Kachel. Der Kundentext (370 Wörter) ist Quelle, nicht Bestand. |
| 3 | Autocomplete-Themenbaum (mindestens 15) | ja | 4 Seeds, 531 Treffer (tax compliance 245, compliance management system 183, hinweisgeberschutz 95, compliance anwalt 8). `_work/autocomplete.json`, 2026-10-11. |
| 4 | Ziel-Keyword und Suchvolumen | ja, mit Abweichung vom Sitetree | Sitetree: "tax compliance" 590. Der Kundentext nennt Steuer nicht, die Seite führt daher "compliance beratung" 140 als Hauptbegriff und deckt "tax compliance" über einen Gesetzes-Block ab (§ 153 AO) plus Veröffentlichungen von Dr. Stürzl. Cluster: compliance management system 590, hinweisgebersystem 720, compliance schulung 390, tax compliance management system 320, compliance anwalt 70. `_work/vol.json` (26 Begriffe), DataForSEO, 2026-10-11, 0,09 USD. Entscheidung für Martin: OPEN-FLAGS C1. |
| 5 | SERP Top 10 | ja | `_work/serp-compliance-anwalt.json` und `serp-tax-compliance.json`, DataForSEO, 2026-10-11, je 0,0035 USD. "compliance anwalt": Kanzlei-Seiten (CMS, Winheller, SLB, Kapellmann, dms-strafrecht u. a.). "tax compliance": überwiegend Steuerberater und Wirtschaftsprüfer, Fachartikel, ein Video. |
| 6 | Echte PAA-Fragen | ja | 8 Fragen aus beiden SERPs. 7 beantwortet (FAQ, Vertiefung), 1 verworfen (Welche Aufgaben hat ein Compliance Officer?, off-offer). Liste in brief.json. |
| 7 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 23 von 23 gelesen. Referenzmenge: 14 Kanzlei-Seiten zu Compliance. Zusätzlich 9 Seiten zu Tax Compliance (Steuerberater, nicht vergleichbar, nur für Themen-Hinweise). `_work/bench-metrics.json`. |
| 8 | Lokaler Fakt | nicht nötig | Bundesweite Themenseite. |

## Messreihe Kanzlei-Seiten zu Compliance (Referenzmenge)

| Wörter | Seite |
| --- | --- |
| 1847 | https://www.dr-buchert.de/compliance-beratung/ |
| 1395 | https://se-legal.de/rechtsanwalt/rechtsanwalte-fur-compliance/ |
| 1279 | https://www.bfs-kanzlei.de/rechtsanwalt-compliance.php |
| 1260 | https://kapellmann.de/de/kompetenzen/compliance |
| 1165 | https://www.bwlh.de/Anwalt/Compliance/compliance.html |
| 1042 | https://compliancerechtsanwaelte.de/ |
| 960 | https://www.gvw.com/leistungen/detail/compliance |
| 747 | https://www.strafrecht.berlin/compliance/ |
| 647 | https://dms-strafrecht.de/compliance/ |
| 602 | https://www.winheller.com/wirtschaftsrecht/compliance.html |
| 447 | https://www.mtrlegal.com/rechtsberatung/wirtschaftsstrafrecht/compliance/ |
| 376 | https://www.liebenstein-law.de/service/compliance/ |
| 374 | https://www.slb-law.de/rechtsgebiete/compliance/ |
| 147 | https://fachanwaelte-strafrecht-potsdamer-platz.de/de/compliance |

Messwerte: 14, Median 853.5, 70 % = 597

## Messreihe Seiten zu Tax Compliance (Steuerberater, Zusatz)

| Wörter | Seite |
| --- | --- |
| 3409 | https://www.dr-buchert.de/tax-compliance-tax-cms-steuerstrafrechtliche-beratung-fuer-unternehmen/ |
| 1597 | https://www.hlb-hussmann.de/steuerberatung-nuernberg/tax-compliance-management-system/ |
| 1362 | https://www.tax-legal-excellence.com/anforderungen-an-ein-tax-compliance-system/ |
| 1017 | https://schulz-beratung.de/mindestanforderungen-an-ein-tax-compliance-system/ |
| 914 | https://sp-unternehmerforum.de/ziele-des-tax-compliance-management-systems/ |
| 760 | https://www.breidenbach-wp.de/tax-compliance-management-systeme/ |
| 659 | https://lueders-warneboldt.de/news/tax-compliance-management-system/ |
| 455 | https://www.xn--steuerstrafrecht-mnchen-tpc.de/steuerlexikon/tax-compliance/ |
| 293 | https://www.sb-p.de/leistungen/tax-compliance/ |

Messwerte: 9, Median 914, 70 % = 639

## Wortzahl-Urteil (vorab, Ziel)

Kein Bestand (404). Referenz-Median 853,5 Wörter, Untergrenze 597. Zielkorridor 750 bis 1600. Kundentext 370 Wörter. Die Tiefe kommt aus Gesetzestexten (§ 130, § 30 OWiG, §§ 12, 16, 17 HinSchG, § 153 AO), nicht aus Füllwörtern.

## Konflikte im Kundenmaterial

1. Der Kundentext nennt Steuer und Tax Compliance nicht, der Sitetree-Auftrag verlangt "tax compliance". Die Seite erfindet keine Tax-CMS-Leistung. Sie nennt Gesetz und Veröffentlichungen und fragt per Platzhalter.
2. Der Kundentext enthält "ganzheitlichen Verteidigungsstrategie", "Haftung zu vermeiden", "im Einzelfall sogar zu vermeiden", "maßgeblich": nicht übernommen (BRAO, Ergebnisnähe).
3. Kostenmodell: neuer Kundentext gegen freigegebene Startseite ("RVG").

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden. Kein Blocker. Einschränkung: Hauptkeyword weicht vom Sitetree ab (OPEN-FLAGS C1).
