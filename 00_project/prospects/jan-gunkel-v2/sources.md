# Jan Dominik Gunkel – Konzept Fassung 2 (jan-gunkel-v2): Quellen

Stand: 13.10.2026. Seite: `04_site/review/jan-gunkel-v2/index.html` (gebaut mit `build_v2.py` aus `04_site/review/jan-gunkel/index.html`).
Auftrag: Antwort von Dominik vom 10.10.2026 (`00_project/prospects/_replies/jan-dominik-gunkel-2026-10-13.md`).

## DataForSEO (Kosten 0,186 USD von 0,30 USD, siehe cost_ledger.jsonl)
- `evidence/dfs-volumes-de.json`: Suchvolumen Deutschland (location 2276), 50 Begriffe.
- `evidence/dfs-volumes-nrw.json`: Suchvolumen NRW (North Rhine-Westphalia), 21 Begriffe.
- `evidence/dfs-serp-1euro.json`: Google Köln, "firma für 1 euro kaufen" (Börsen, Ratgeber, GmbH-Aufkäufer/Abwickler; kein Käufer, der weiterführt).
- `evidence/dfs-serp-zahlungsunfaehigkeit.json`: Google Köln, "zahlungsunfähigkeit gmbh" (Kanzleien, Ratgeber).
- `evidence/dfs-serp-inupio.json`: Google DE, "inupio" (Inupio nicht unter den Top 10).
- Ohne Messwert (None): unternehmen in insolvenz kaufen, firma/unternehmen in der krise verkaufen, sanierungsfall übernahme, investor für insolvente firma, sanierungsberater köln, firma verkaufen köln u. a.

## Amtliche und Markt-Zahlen
- IT.NRW über IHK Köln, "Wirtschaftsregion Köln in Zahlen", Ausgabe 2025, S. 7: eröffnete Unternehmensinsolvenzen IHK-Bezirk Köln 2024 = 609 (2023 = 440); Köln 342, Leverkusen 50, Rhein-Erft 120, Oberberg 44, Rhein-Berg 53; NRW 2024 = 4.329.
  https://www.ihk.de/blueprint/servlet/resource/blob/6719188/30e27e4ec3bf6c3e8514f18c3638b081/broschuere-wirtschaftsregion-koeln-2025-data.pdf
- IT.NRW über Handwerksblatt (11.03.2026): NRW 2025 = 6.502 beantragte Unternehmensinsolvenzen, +15,3 % zu 2024 (5.640).
  https://www.handwerksblatt.de/handwerkspolitik/mehr-insolvenzen-in-nrw-1
- Creditreform, "Insolvenzen in Deutschland, Jahr 2025" (08.12.2025): 81,6 % der Unternehmensinsolvenzen bei Firmen mit bis zu 10 Beschäftigten.
  https://www.creditreform.de/aktuelles-wissen/pressemeldungen-fachbeitraege/news-details/show/insolvenzen-in-deutschland-jahr-2025
- Eigener Check 13.10.2026: http://inupio.com antwortet 301 auf https://www.linkedin.com/in/jan-dominik-gunkel/ ; https://www.inupio.com nicht erreichbar.

## Annahmen im Rechner (als "Annahme" auf der Seite markiert)
- B2B- und Branchenanteil 50 %, Sichtquote 60 %, Anfragen vor dem Antrag 2 pro Jahr, Prüfquote 20 %.
- Ergebnis mit Startwerten: ≈ 55 passende Fälle im Markt, ≈ 35 gesehen, ≈ 7 zur Prüfung pro Jahr.
- Regionsbasis ist der IHK-Bezirk Köln (Untergrenze); Köln + 60 Min. ist größer (Bonn, Düsseldorf, Aachen fehlen).

## Gates
- AI-Slop: `deslop_de.py` mit `claims.json` = 5/5.
- Desktop 1440 und 375 px in Chrome geprüft: keine Überbreite, keine Konsolenfehler, Rechner rechnet.
