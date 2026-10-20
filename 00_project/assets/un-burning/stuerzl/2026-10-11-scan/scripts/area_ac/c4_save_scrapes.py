"""Saves the NAP-relevant verbatim blocks of the firecrawl_scrape results of this run as evidence files.
The scrape tool returns text to the agent only; these files hold the cited blocks (shortened, unchanged text)."""
import sys, json
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ub_lib import save_evidence

def sv(eid, text, url, tool="firecrawl_scrape", params="formats=[markdown] maxAge=0", note=""):
    save_evidence(eid, text.strip()+"\n", "md", tool, f"{tool} url={url} {params}", "area_c", note=("excerpt of tool response; "+note).strip("; "))

sv("EV-C-listing-anwalt-de-firm", """
URL: https://www.anwalt.de/kanzlei-stuerzl-steuerstrafrecht  (HTTP 200)
H1: Kanzlei STÜRZL Steuerstrafrecht | 5,0/5 | 79 Bewertungen
Header address line: Wiesenhüttenstraße 17, 60329 Frankfurt am Main
Weiterer Standort: 80331 München
Profile 2: Dr. Anja Stürzl LL.M. (Rechtsanwältin, 55 Bewertungen), Lea Wimmer (Fachanwältin für Steuerrecht, 23 Bewertungen)
## Kontaktdaten von Kanzlei STÜRZL Steuerstrafrecht 2
- Adresse: Wiesenhüttenstraße 17, 60329 Frankfurt am Main
  Öffnungszeiten: Mo.–Do. 09:00–12:30, 12:30–18:00 | Fr. 9:00–12:30, 12:30–18:00
  Kontakt: +49 69 298... anzeigen | +49 160 33... anzeigen | kanzlei@stuerzl-steuerstrafrecht.de | https://www.stuerzl-steuerstrafrecht.de/
  Call button: tel:+4969298028870
- Weitere Informationen / Adresse: Oberanger 32, 80331 München
  Kontakt: +49 89 724... anzeigen | wimmer@stuerzl-steuerstrafrecht.de | https://www.stuerzl-steuerstrafrecht.de/
Kanzlei-Impressum link: https://www.stuerzl-steuerstrafrecht.de/index.php/impressum
""", "https://www.anwalt.de/kanzlei-stuerzl-steuerstrafrecht", note="phone digits are masked on the page except the tel: link")

sv("EV-C-listing-anwalt-de-anja", """
URL: https://www.anwalt.de/anja-stuerzl  (HTTP 200, onlyMainContent=false)
H1: Dr. Anja Stürzl LL.M. | Rechtsanwältin | 5,0/5 | 55 Bewertungen
Firm line: Kanzlei STÜRZL Steuerstrafrecht, Wiesenhüttenstraße 17, 60329 Frankfurt am Main
Section 'Qualifikationen und Auszeichnungen':
 - Fachanwältin für Steuerrecht -- Rechtsanwaltskammer Köln -- Website https://www.rak-koeln.de/
 - Masterstudiengang Wirtschaftsrecht -- Universität Osnabrück
 - Zertifizierte Beraterin für Steuerstrafrecht (DAA) -- Deutsche Anwaltakademie
 - WirtschaftsWoche Top Kanzlei 2024 Steuerstrafrecht; Top Anwalt 2023; Handelsblatt Best Lawyers 2024; WiWo 2025 Ranking
Section 'Kontaktdaten': Adresse Wiesenhüttenstraße 17, 60329 Frankfurt am Main; Öffnungszeiten Mo.–Do. 09:00–12:30, 12:30–18:00, Fr. 9:00–12:30, 12:30–18:00
 Kontakt: +49 69 298... anzeigen | +49 160 33... anzeigen | kanzlei@stuerzl-steuerstrafrecht.de ; Call button tel:+4969298028870
Text: 'seit Dezember 2023 meine eigene Kanzlei STÜRZL Steuerstrafrecht mit Sitz in Frankfurt und München'
""", "https://www.anwalt.de/anja-stuerzl", params="formats=[markdown] maxAge=0 onlyMainContent=false")

sv("EV-C-listing-anwalt-lotse-anja", """
URL: https://anwalt-lotse.de/rechtsanwaeltin/anja-stuerzl-frankfurt-5vtd/  (HTTP 200)
Heading: Daten aus dem amtlichen Verzeichnis der Bundesrechtsanwaltskammer -- 'verifiziert vor 3 Wochen' (relative to 2026-10-11)
Frau Rechtsanwältin Dr. jur. Anja Stürzl, Aktiv; Fachanwaltschaft: Steuerrecht; Zulassung seit 8 Jahren
Mitglied der Rechtsanwaltskammer Frankfurt
069-298028870 | 0160-339•••• | stuerzl@stuerzl-steuerstrafrecht.de | www.stuerzl-steuerstrafrecht.de
STÜRZL Steuerstrafrecht, Wiesenhüttenstr. 17, 60329 Frankfurt
Zweigstelle München: Dr. Anja Stürzl Rechtsanwältin, Oberanger 32, 80331 München
089-72444170 | 069-298028879 | kanzlei@stuerzl-steuerstrafrecht.de | www.stuerzl-steuerstrafrecht.de
Link 'Profil beanspruchen' offered.
Portals with a hit: anwalt.de, Best Lawyers, rechtecheck.de. 14 portals without hit incl. Deutsche Anwaltsauskunft listed as 'geprüft'.
""", "https://anwalt-lotse.de/rechtsanwaeltin/anja-stuerzl-frankfurt-5vtd/", params="formats=[markdown] maxAge=0 onlyMainContent=true", note="mirror of the official BRAK directory; the RAK/BRAK site itself was not read")

sv("EV-C-listing-11880", """
URL: https://www.11880.com/branchenbuch/frankfurt-am-main/081314253B114102102/stuerzl-steuerstrafrecht.html  (HTTP 200)
STÜRZL Steuerstrafrecht | Rechtsanwalt | Öffnungszeiten hinzufügen (no hours stored)
(069) 298028870  (tel:+4969298028870)
Wiesenhüttenstr. 17, 60329 Frankfurt (Gutleutviertel)
kanzlei@stuerzl-steuerstrafrecht.de | https://www.stuerzl-steuerstrafrecht.de
Branchen: Rechtsanwalt; Dienstleistungen: Rechtsanwalt, Drogenstrafrecht
Bewertungen: noch keine
Footer: 'STÜRZL Steuerstrafrecht in Frankfurt wurde aktualisiert am 04.10.2026. Eintragsdaten vom 17.08.2026.'  Button 'Änderungen vorschlagen'.
""", "https://www.11880.com/branchenbuch/frankfurt-am-main/081314253B114102102/stuerzl-steuerstrafrecht.html", params="formats=[markdown] maxAge=0 onlyMainContent=true")

sv("EV-C-listing-rechtecheck-frankfurt", """
URL: https://rechtecheck.de/anwalt/frankfurt/anja-stuerzl/  (HTTP 200)
HTML title: 'Rechtsanwältin Anja Stürzl | Frankfurt (Oder)'
Body: Rechtsanwältin Dr. jur. Anja Stürzl | Kanzlei STÜRZL Steuerstrafrecht | Wiesenhüttenstr. 17, 60329 Frankfurt | www.stuerzl-steuerstrafrecht.de | Rechtsgebiet: Steuerrecht
Active filter on the page: 'Frankfurt (Oder)'; section 'Sind Sie Anja Stürzl? Daten aktualisieren'
No phone number shown.
""", "https://rechtecheck.de/anwalt/frankfurt/anja-stuerzl/", params="formats=[markdown] maxAge=0 onlyMainContent=true")

sv("EV-C-listing-rechtecheck-muenchen", """
URL: https://rechtecheck.de/anwalt/muenchen/kanzlei/kanzlei-stuerzl-steuerstrafrecht/  (HTTP 200)
Title: Kanzlei STÜRZL Steuerstrafrecht | Anwaltskanzlei in München
Kanzlei STÜRZL Steuerstrafrecht, Neuhauser Str. 3a, 80331 München. Rechtsgebiete: Steuerrecht, Steuerstrafrecht. Anwalt: Frau Lea Wimmer. 'Verwalten Sie die Kanzlei? Daten aktualisieren'. No phone shown.
Context: search snippet of the same run shows 'Neuhauser Straße 3 a, 80331 München' as the address of Dr. Rose Rechtsanwälte (another firm) on rose-rechtsanwaelte.de (EV-C-search-4b).
""", "https://rechtecheck.de/anwalt/muenchen/kanzlei/kanzlei-stuerzl-steuerstrafrecht/", params="formats=[markdown] maxAge=0 onlyMainContent=true")

sv("EV-C-search-4b", """
firecrawl_search query='Kanzlei STÜRZL Steuerstrafrecht Neuhauser Str. 3a München' (2026-10-11), relevant rows:
 - https://rose-rechtsanwaelte.de/rechtsgebiete/steuerstrafrecht/ -- 'Dr. Rose Rechtsanwälte, Neuhauser Straße 3 a, 80331 München, Telefon: 089 - 242 90 74 0'
 - https://rechtecheck.de/anwalt/muenchen/kanzlei/kanzlei-stuerzl-steuerstrafrecht/ -- 'Kanzlei STÜRZL Steuerstrafrecht Neuhauser Str. 3a 80331 München'
 - https://www.lto.de/recht/kanzleien-unternehmen/k/stuerzl-steuerstrafrecht-zweite-niederlassung-muenchen -- 'Spätestens zum Jahresbeginn 2025 berät Stürzl Steuerstrafrecht auch in München.'
""", "(search)", tool="firecrawl_search", params="query='Kanzlei STÜRZL Steuerstrafrecht Neuhauser Str. 3a München' sources=[web]")

sv("EV-C-listing-cylex-search-ffm", """
URL: https://web2.cylex.de/s?q=Stürzl Steuerstrafrecht&c=Frankfurt am Main  (HTTP 200)
Treffer 1 von 1: STÜRZL Steuerstrafrecht, Wiesenhüttenstraße 17, 60329 Frankfurt am Main, Hessen, 069 298028870, 'Jetzt geschlossen' -> https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-16927796.html
""", "https://www.cylex.de/s?q=St%C3%BCrzl+Steuerstrafrecht&c=Frankfurt+am+Main")

sv("EV-C-listing-cylex-ffm", """
URL: https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-16927796.html  (HTTP 200)
STÜRZL Steuerstrafrecht, Frankfurt am Main | Kategorie: Rechtsanwälte (Geld & Recht)
Adresse: Wiesenhüttenstraße 17, 60329 Frankfurt am Main, Hessen | Telefon: 069 298028870 | kanzlei@stuerzl-steuerstrafrecht.de | www.stuerzl-steuerstrafrecht.de
Öffnungszeiten: Mo-Fr 09:00 - 18:00; Sa, So geschlossen. 'Letzte Aktualisierung: 16.04.2026'
Beschreibung (Abschnitt 'Adresse & Kontaktdaten'): 'Wiesenhüttenstraße 17 60329 Frankfurt am Main Neuhauser Str. 3a 80331 München Telefon: 069 29802887-0 E-Mail: kanzlei@stuerzl-steuerstrafrecht.de LinkedIn: STÜRZL Steuerstrafrecht'
Buttons: 'Eintrag übernehmen' (unclaimed), 'Fehlerhafte Daten melden', 'Eintrag entfernen'. Bewertungen: keine.
""", "https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-16927796.html", params="formats=[markdown] maxAge=0 onlyMainContent=true")

sv("EV-C-listing-cylex-search-muc", """
URL: https://web2.cylex.de/s?q=Stürzl Steuerstrafrecht&c=München  (HTTP 200) -- 'Treffer 1 - 2 von 2'
 1. STÜRZL Steuerstrafrecht, Oberanger 32, 80331 München, Bayern, 089 72444170 -> .../stuerzl-steuerstrafrecht-17168776.html (geo 48.1346048,11.5703246)
 2. STÜRZL Steuerstrafrecht, Neuhauser Str. 3a, 80331 München, Bayern, 089 72444170 -> .../stuerzl-steuerstrafrecht-17045957.html (geo 48.137934,11.570809)
""", "https://www.cylex.de/s?q=St%C3%BCrzl+Steuerstrafrecht&c=M%C3%BCnchen")

sv("EV-C-listing-cylex-muc-wrong", """
URL: https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-17045957.html  (HTTP 200)
STÜRZL Steuerstrafrecht, München | Kategorie-Pfad: Computer & Edv > Produktion und Vertrieb von It-Produkten > Software Hersteller
Adresse: Neuhauser Str. 3a, 80331 München, Bayern | Telefon 089 72444170 | kanzlei@stuerzl-steuerstrafrecht.de | www.stuerzl-steuerstrafrecht.de
Buttons: 'Eintrag übernehmen' (unclaimed), 'Fehlerhafte Daten melden', 'Eintrag entfernen'. Keine Bewertungen.
""", "https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-17045957.html", params="formats=[markdown] maxAge=0 onlyMainContent=true")

sv("EV-C-listing-cylex-muc-ok", """
URL: https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-17168776.html  (HTTP 200)
STÜRZL Steuerstrafrecht, München | no category listed (pin icon)
Adresse: Oberanger 32, 80331 München, Bayern | Telefon 089 72444170 | kanzlei@stuerzl-steuerstrafrecht.de | www.stuerzl-steuerstrafrecht.de
'Letzte Aktualisierung: 18.05.2026'. Buttons: 'Eintrag übernehmen' (unclaimed), 'Fehlerhafte Daten melden', 'Eintrag entfernen'.
""", "https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-17168776.html", params="formats=[markdown] maxAge=0 onlyMainContent=true")

sv("EV-C-listing-gelbeseiten", """
URL: https://www.gelbeseiten.de/suche/stürzl%20steuerstrafrecht/frankfurt-am-main  (page HTTP 404 as search URL, but the page is a search result page)
Text: 'Leider finden wir zu Ihrer Suchanfrage im gesamten Bundesgebiet keine passenden Einträge.'  Heading: 'Stürzl steuerstrafrecht in Frankfurt am Main (0 Treffer)'
""", "https://www.gelbeseiten.de/suche/st%C3%BCrzl%20steuerstrafrecht/frankfurt-am-main", params="formats=[markdown] maxAge=0 onlyMainContent=true")

sv("EV-C-listing-oertliche", """
URL: https://www.dasoertliche.de/?zvo_ok=1&form_name=search_nat&kw=Stürzl Steuerstrafrecht&ci=Frankfurt am Main ... (fetched with curl, HTTP 410 status but a normal result page)
Text: 'Abweichendes Suchergebnis! Für "Stürzl Steuerstrafrecht" in "Frankfurt am Main" konnte leider kein exakt passender Eintrag ermittelt werden.' Alternatives offered: 'Steuerstrafrecht (3)', 'Rechtsanwälte (682)'.
""", "dasoertliche.de search", tool="curl+firecrawl_scrape", params="city disambiguation followed")

sv("EV-C-listing-yelp", """
URL: https://www.yelp.de/search?find_desc=Stürzl+Steuerstrafrecht&find_loc=Frankfurt+am+Main
curl: HTTP 200, 559993 bytes, page title 'Best Stürzl Steuerstrafrecht in Frankfurt am Main, Hessen - Last Updated Oktober 2026 - Yelp', robots noindex, no /biz/ links in the static HTML (results are rendered by JavaScript).
firecrawl_scrape: 'We apologize for the inconvenience but we do not support this site.'
Result: UNREADABLE in this run (not 'nothing found').
""", "https://www.yelp.de/search", tool="curl+firecrawl_scrape", params="")

sv("EV-C-listing-infobel", """
Direct fetch: https://www.infobel.com/de/germany/sturzl_steuerstrafrecht/frankfurt_oder/DE109851584-069298028870/businessdetails.aspx -> firecrawl_scrape returned the Infobel 'Abuse' page (captcha 'I am not a robot'); page content UNREADABLE live.
Search snippet (firecrawl_search, 2026-10-11, query '"Wiesenhüttenstraße 17" Frankfurt Stürzl'): title 'STÜRZL Steuerstrafrecht, Frankfurt (Oder), DE - Infobel'; text 'STÜRZL Steuerstrafrecht in Frankfurt (Oder). Wiesenhüttenstraße 17 60329 Frankfurt (Oder). Telefon anzeigen.' URL carries phone 069298028870.
""", "infobel.com", tool="firecrawl_scrape+firecrawl_search", params="")

sv("EV-C-listing-bestlawyers", """
URL: https://www.bestlawyers.com/firms/sturzl-steuerstrafrecht/104283/DE  (HTTP 200)
'STÜRZL Steuerstrafrecht -- 2 Locations in Germany: Frankfurt/Main, Germany; Munich, Germany'. Firm tenure with Best Lawyers began 2023.
Recognized lawyers: Anja Stürzl (Frankfurt/Main, 'Unactivated Profile'), Lea Wimmer (Munich, 'Unactivated Profile'). No street address, no phone on the page.
""", "https://www.bestlawyers.com/firms/sturzl-steuerstrafrecht/104283/DE", params="formats=[markdown] maxAge=0 onlyMainContent=true")

sv("EV-C-search-misc", """
Search snippets (firecrawl_search, 2026-10-11) for pages that carry firm NAP and were not opened:
 - https://de.maptons.com/p/3302892716 (+ mt, hr, bj, qa, ee, py, is subdomains): 'STÜRZL Steuerstrafrecht, Wiesenhüttenstraße 17, Deutschland, rechtsanwalt, telefon +49 69 298028870' with page time stamps 12.07.2026 to 13.09.2026 and coordinates 50.1044088 (page returns HTTP 403 to curl).
 - https://de.linkedin.com/company/stuerzl-steuerstrafrecht : 'Orte. Primär. Wiesenhüttenstraße 17. Frankfurt, Hessen 60329, DE.' (716 Follower). firecrawl_scrape: not supported for company profiles in this team plan -> page not opened.
 - https://firmeneintrag.creditreform.de/60329/6070874119/DR_ANJA_STUERZL_STUERZL_STEUERSTRAFRECHT : 'Dr. Anja Stürzl, STÜRZL Steuerstrafrecht, Frankfurt' (street not in snippet).
 - https://juwist.com/mitgliederliste/ : 'Dr. Anja Stürzl, LL.M. STÜRZL Steuerstrafrecht Wiesenhüttenstraße 17 60329 Frankfurt am Main' (member list of an association, not run by the firm).
 - https://anwaltauskunft.de/rechtsanwalt/wimmer-287f04ca/ : 'Lea Wimmer ... STÜRZL Steuerstrafrecht Oberanger 32, 80331 München. +49 (89) 7244 41 70 wimmer@stuerzl-steuerstrafrecht.de'.
 - https://www.anwalt.de/lea-wimmer-2 : 'Rating 5.0(23) Kanzlei STÜRZL Steuerstrafrecht. Oberanger 32, 80331 München'.
 - https://www.xing.com/profile/Lea_Wimmer2 : 'Lea Wimmer - Rechtsanwältin, Salary Partnerin, Stürzl Steuerstrafrecht' (no address in snippet).
 - https://kulturstiftung-ukraine.org/index.php/datenschutz : separate foundation; 'Anja Stürzl Wiesenhüttenstraße 17 60329 Frankfurt am Main. Telefon: +49 69-29802887-0'.
 - https://www.juve.de/juve-rankings/deutschland/wirtschafts-und-steuerstrafrecht/ : ranking lists 'Stürzl, Frankfurt' under 'Aufsteiger' (name only, no address, no firm profile found).
 - Instagram/Facebook: only third-party posts mention the firm (IWW institute, a photographer). No firm-owned Instagram or Facebook profile appeared in the results.
 - Search for '"Untermainkai 26" Stürzl Steuerstrafrecht': no result shows the new address for the firm.
 - Search for '"Stützel Steuerstrafrecht"': no result names such a firm (see EV-C-search-5).
""", "(search)", tool="firecrawl_search", params="several queries, see text")
print("saved")
