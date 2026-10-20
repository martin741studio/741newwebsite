## 3 · Website live (01.10.2026, stuerzl-steuerstrafrecht.de)

System: Joomla, Helix Ultimate, SP Page Builder. URLs mit `/index.php/`.

| Punkt | Ist |
|---|---|
| Title Start | „Stürzl Steuerstrafrecht – Home" |
| Meta Start | „Kanzlei in Frankfurt am Main mit Spezialisierung im Steuer- und Wirtschaftsstrafrecht." |
| H1 Start | „Kanzlei" |
| Titles Unterseiten | Muster „Stürzl Steuerstrafrecht – <Menüname>" |
| `/index.php/schwerpunkte` | **404.** Die Startseite verlinkt die Seite („mehr zu den Schwerpunkten"). |
| Leistungen | 9 Bereiche auf einer Seite, keine eigenen URLs |
| FAQ | 6 × H1. Inhalt stark (Verfahren, Kosten, Selbstanzeige, A–Z, Mythen). |
| Aktuelles | keine H1 |
| Sitemap | `/sitemap.xml` = 404. robots.txt ohne Sitemap-Zeile. |
| TTFB | 1,34 / 1,40 / 1,68 s (3 Messungen) |
| Canonical, HTTPS, 301 | in Ordnung |
| Schema | LegalService mit Adresse, Geo, Zeiten 09–18. München fehlt. Person nur als Name. |
| Tracking | GTM-WFPFSTK2 → GA4 G-FCG9RTJ1YQ. Events: phone_click, email_click, link_click, menu_item_click, on_page_navigation, expand_sections. Consent Mode Signale vorhanden (n3t Cookie Consent). **Kein Google-Ads-Tag, keine Ads-Conversion.** |
| Kontaktwege | Tel. Frankfurt +49 69 298028870 · Tel. München +49 89 72444170 · kanzlei@stuerzl-steuerstrafrecht.de · 2 Notfall-Mobilnummern · **kein Formular** · kein WhatsApp |
| Erreichbarkeit | Telefon Mo–Fr 09:30–14:30 (Kontaktseite) |

NAP Frankfurt: STÜRZL Steuerstrafrecht, Wiesenhüttenstraße 17, 60329 Frankfurt am Main, +49 69 29 80 28 87-0, Fax -9.
„Linkemann" steht nicht auf der Team-Seite. Schreibweise bleibt ungeprüft.


## 10 · Audit-Recherche 08.10.2026 (für Source-of-Truth-Sheet)

Payload: `00_project/assets/stuerzl/sheet/payload.json` (Builder `build_payload.py`, Push `push_payload.mjs` via Service-Account – braucht Sheets API im GCP-Projekt 608184211918, am 08.10. noch deaktiviert).

Korrekturen zu früheren Aussagen:
- **Leistungsseiten existieren**: 9 Bereichsseiten (/index.php/steuerstrafrecht, …/selbstanzeigen-steuerliche-korrekturen, …) + 17 Unterseiten. Dünn (114–376 Wörter), alle mit 2×H1 („Leistungen" + Bereich). Report-Abschnitt 5 korrigiert (v=20261008).
Neue Befunde:
- **Backlinks**: Rank 122, 100 Links, 58 Ref-Domains, Spam-Score 31; ~40 Spam-Domains (.shop/Casino/PBN) seit 07/2026 mit Anchor „High Quality Dofollow Backlinks DA 50 PA 40 Premium PBN Netw" → Disavow-Liste in Tab 08. Seriös nur bestlawyers (13), anwaltauskunft (4), tax-talents, tzelepis.
- **SERP 08.10. (Frankfurt)**: Marke #1; „anwalt steuerstrafrecht" #27; alle anderen Gattungsbegriffe nicht in Top 30.
- **On-Page**: LCP 7,2 s gerendert, 35 JS/13 CSS, 892 KB Bilder; 27 Seiten 2×H1, 18 ohne H1; 4 tote Links (schwerpunkte, /linkedin.com/… auf Glogger-Seite, 2× href="tel."); kein llms.txt; Kategorie-Duplikate.
- **Citations**: Infobel „Frankfurt (Oder)", Cylex München „Neuhauser Str. 3a" (falsch); anwalt.de Anja „RAK Köln"; Gelbe Seiten/Das Örtliche/Yelp nicht gefunden. Alle noch alte Adresse.
- **Unlinked Mentions**: LTO ×4, JUVE ×2, ZRI ×2, RWS, azur, Capital, Private Banking Magazin, BMF-PDF, IWW, C.F. Müller, R&W, Fürstenberg, young-tle – keine in der Backlink-Liste.
- **Negativ-Suche**: nichts gefunden.
- Alt-Agentur-Report 27.05.2025 (Voss): GSC 320 Klicks/5.150 Impr./28 Tage, Ø Pos 33.

