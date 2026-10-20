"""Build part-D/harm-register.json and redirect-map.json from the evidence of this run. Re-run safe."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ub_lib import *

M = {e["id"]: e for e in load_manifest()["evidence"]}
B = "https://www.stuerzl-steuerstrafrecht.de"
STORED = "2026-10-09T00:00:00+02:00"
items = []
cnt = [0]


def pg(slug):
    eid = "EV-D-page-www.stuerzl-steuerstrafrecht.de" + slug
    assert eid in M, eid
    return eid


def it(entity, item, why, check, target, sev, action, detail, actor, effort, ev, conf="verified", tool="requests GET", approval="proposed",
       destructive=None, verify="", refetch=None, hint="", safe=True, text=None, source_field=None, collected=None, depends=None):
    cnt[0] += 1
    for e in ev:
        assert e in M, e
    if destructive is None:
        destructive = action in ("delete", "report", "merge")
    d = {
        "id": f"H-D-{cnt[0]:03d}", "area": "D", "entity": entity, "item": item, "why": why, "check_id": check, "source_field": source_field,
        "target": target, "severity": sev, "action": action, "action_detail": detail, "actor": actor, "effort": effort, "destructive": destructive,
        "approval": approval, "approved_by": None, "approved_at": None, "wave": None, "snapshot_id": None, "rollback": None, "before": None, "after": None,
        "verify_check": verify, "done_at": None, "confidence": conf, "collected_at": collected or M[ev[0]]["collected_at"], "source_tool": tool,
        "evidence_ids": ev, "refetch": refetch or {"tool": tool, "cost": "0 EUR"}, "depends_on": depends or [], "drilldown_hint": hint, "client_safe": safe}
    if safe and text:
        d["client_text"] = text
    items.append(d)
    return d["id"]


GET = "requests GET (UA 741-unburning-scan/1.0, 0.3 s delay)"
CR = "re-run scripts/area_d/d1_crawl.py (0 EUR)"

# ---------------- D01 / D02: dead links, URL variants, redirects ----------------
it("website", "Auf der Startseite führt der Link „mehr zu den Schwerpunkten“ auf /index.php/schwerpunkte und die Seite antwortet 404 (heute live bestätigt).",
   "Besucher und Suchmaschinen landen auf der wichtigsten Seite in einer Sackgasse.", "UB.D01", B + "/index.php/schwerpunkte", "leaks_link_power", "redirect",
   "Link auf der Startseite auf /index.php/leistungen ändern (Seite listet die 9 Bereiche) und zusätzlich 301 von /index.php/schwerpunkte auf /index.php/leistungen setzen. Joomla-Super-User nötig (angefragt am 09.10.).",
   "741", "S", [pg("_index.php_schwerpunkte-404"), pg(""), "EV-D-analysis"], tool=GET, verify="curl -sI /index.php/schwerpunkte liefert 301 und das Ziel 200; Startseite enthält keinen Link mehr auf /schwerpunkte",
   refetch={"tool": CR, "cost": "0 EUR"}, hint="redirect-map.json Zeile 1; Quelle des Links: Startseite, Linktext 'mehr zu den Schwerpunkten'", source_field="B06.03",
   text="Auf der Startseite führt der Link „mehr zu den Schwerpunkten“ auf eine nicht vorhandene Seite.")

it("website", "Vier Mitarbeiterseiten tragen kaputte Telefonlinks (href „tel.+49…“ statt „tel:+49…“); sie führen auf eine 404-Seite (2 Nummern, 4 Seiten).",
   "Wer am Handy auf die Nummer tippt, ruft nicht an, sondern landet auf einer Fehlerseite.", "UB.D01", B + "/tel.+4969298028870 und " + B + "/tel.+498972444170", "blocks_revenue", "fix",
   "href auf tel:+4969298028870 bzw. tel:+498972444170 korrigieren (Punkt statt Doppelpunkt). Betroffen: Seiten von Florentine Jilg, Thorben Hoppe (Frankfurt) sowie Dr. Monika Glogger, Lea Wimmer (München). Nur diese vier Seiten; die Kontaktseite ist nicht betroffen. Telefonnummern sind noch nicht vom Kunden bestätigt (NAP nicht gesperrt).",
   "741", "S", [pg("_tel._4969298028870-404"), pg("_tel._498972444170-404"), "EV-D-analysis"], tool=GET,
   verify="Crawl: kein internes href beginnt mit 'tel.'; Tipp auf die Nummer startet einen Anruf", refetch={"tool": CR, "cost": "0 EUR"},
   hint="EV-D-analysis dead_internal_links: Quellseiten je Link", source_field="B06.03",
   text="Auf vier Teamseiten führt die Telefonnummer auf eine Fehlerseite statt einen Anruf zu starten.")

it("website", "Auf der Seite von Dr. Glogger zeigt das LinkedIn-Symbol auf /linkedin.com/in/… (Schema fehlt), der Link antwortet 404.",
   "Toter Link auf der eigenen Domain statt auf das Profil.", "UB.D01", B + "/linkedin.com/in/dr-monika-glogger-geb-werndl-3354a9123", "cosmetic", "fix",
   "href auf https://www.linkedin.com/in/dr-monika-glogger-geb-werndl-3354a9123 ändern (abgeleitet aus dem kaputten href; Profil beim Kunden bestätigen lassen).",
   "741", "S", [pg("_linkedin.com_in_dr-monika-glogger-geb-werndl-3354a9123-404"), pg("_index.php_dr-monika-glogger")], tool=GET,
   verify="Seite enthält keinen href, der mit /linkedin.com beginnt", refetch={"tool": CR, "cost": "0 EUR"}, source_field="B06.03",
   text="Das LinkedIn-Symbol auf einer Teamseite führt auf eine nicht vorhandene Seite der eigenen Domain.")

it("website", "Die Datei /images/slider-arrow.svg, auf die die Startseite verweist, antwortet 404.", "Defektes Bild im Layout; kostet eine unnötige Anfrage.",
   "UB.D01", B + "/images/slider-arrow.svg", "cosmetic", "fix", "Datei wieder hochladen oder den Verweis im Template/Slider entfernen.", "741", "S",
   ["EV-D-perf-assets"], tool=GET, verify="GET /images/slider-arrow.svg liefert 200 oder kein Verweis mehr", refetch={"tool": "re-run scripts/area_d/d5_perf_assets.py", "cost": "0 EUR"},
   text="Eine Layout-Grafik auf der Startseite fehlt auf dem Server.")

it("website", "Ein externer Link führt auf eine tote Seite (otto-schmidt.de, Seminar Steuerstrafverfahren; 404). Er steht auf 3 Seiten.",
   "Veralteter Verweis in einem Beitrag; wirkt ungepflegt.", "UB.D01", "https://www.otto-schmidt.de/seminare/seminare-steuerrecht/steuerstrafverfahren-und-besteuerungsverfahren", "cosmetic", "fix",
   "Link entfernen oder auf die aktuelle Seite des Veranstalters ändern (Ersatz-URL nicht gefunden, nicht geraten).", "741", "S", ["EV-D-external-links"], tool=GET,
   verify="Externer Link-Check zeigt keinen 404", refetch={"tool": "re-run scripts/area_d/d3_external_links.py", "cost": "0 EUR"},
   text="Ein Beitrag verlinkt auf ein Seminar, dessen Seite beim Veranstalter nicht mehr existiert.")

it("website", "Von 50 externen Links antworten 40 mit 200, 1 mit 404 (siehe oben) und 9 mit 999 oder 403 (LinkedIn und anwalt.de blocken Bots); diese 9 sind nicht als tot belegt.",
   "Ergebnis der Prüfung festhalten, damit blockierte Antworten nicht als Fehler gelten.", "UB.D01", "externe Links aller gecrawlten Seiten", "cosmetic", "keep",
   "Keine Änderung. Die 9 blockierten Links bei Bedarf von Hand im Browser prüfen. LinkedIn-Links tragen einen Tracking-Parameter (lipi=…): beim nächsten Edit entfernen.",
   "741", "S", ["EV-D-external-links"], tool=GET, verify="Stichprobe im Browser", refetch={"tool": "re-run scripts/area_d/d3_external_links.py", "cost": "0 EUR"},
   text="Externe Links wurden geprüft; bis auf einen sind alle erreichbar oder nur für Programme gesperrt.")

it("website", "Die Hostvarianten sind sauber: http, https, www und ohne www führen mit genau einer 301-Weiterleitung auf https://www.stuerzl-steuerstrafrecht.de; HSTS ist gesetzt. Keine Ketten, keine Schleifen.",
   "Geprüft und in Ordnung: keine Linkkraft geht über Hostvarianten verloren.", "UB.D02", "http/https, www/ohne www", "cosmetic", "keep", "Keine Änderung.", "741", "S",
   ["EV-D-variants"], tool=GET, verify="curl -sIL <Variante> zeigt höchstens einen Sprung", refetch={"tool": "re-run scripts/area_d/d2_variants.py", "cost": "0 EUR"},
   hint="EV-D-variants Zeilen kind=host und host_deep", text="Die Weiterleitungen von http und von der Adresse ohne www sind in Ordnung.")

it("website", "Dieselbe Seite ist unter mehreren URLs mit 200 erreichbar, jede mit sich selbst als Canonical: Startseite unter /, /index.php, /index.php/ und /index.php/home; Unterseiten mit und ohne Schrägstrich am Ende (z. B. /index.php/kanzlei und /index.php/kanzlei/); beliebige Parameter (?utm_source=…, ?foo=bar, /index.php?s=test) liefern 200, 'index, follow' und einen Canonical mit demselben Parameter.",
   "Das Canonical-Tag spiegelt jede aufgerufene URL und bündelt deshalb nichts; Signale verteilen sich auf viele Duplikate.", "UB.D03", B + "/index.php",
   "leaks_link_power", "redirect",
   "301 von /index.php, /index.php/ und /index.php/home auf /; 301 von Adressen mit Schrägstrich am Ende auf die Form ohne; Canonical-Ausgabe so einstellen, dass Parameter nicht übernommen werden (Joomla-SEF/Canonical-Plugin). Joomla-Super-User nötig.",
   "741", "M", ["EV-D-variants"], tool=GET, verify="curl -sI /index.php zeigt 301 auf /; Canonical von ?foo=bar zeigt auf /",
   refetch={"tool": "re-run scripts/area_d/d2_variants.py", "cost": "0 EUR"}, hint="EV-D-variants kind=index_php, trailing_slash, param; redirect-map.json Zeilen 'proposed_duplicate'",
   text="Dieselbe Seite lässt sich unter mehreren Adressen aufrufen, und die Seite meldet jede davon als Hauptadresse.")

it("website", "Alle URLs tragen /index.php/ (Joomla-URL-Umschreibung aus); die saubere Form (z. B. /kanzlei) antwortet 404. Es gibt keinen Weiterleitungsweg zwischen den Formen.",
   "Unschön, aber kein messbarer Verlust; eine Umstellung würde alle bestehenden Adressen und Backlinks berühren.", "UB.D02", B + "/index.php/", "cosmetic", "keep",
   "Nicht jetzt ändern. Entscheidung für später: URL-Umschreibung einschalten nur zusammen mit einer vollständigen 301-Karte aller bestehenden /index.php/-Adressen und Test.",
   "741", "L", ["EV-D-variants"], tool=GET, verify="-", hint="Entscheidung offen (Martin); Risiko: alle Backlinks zeigen auf /index.php/-Adressen", safe=False)

it("website", "Fehlerseiten sind echt: unbekannte Adressen liefern 404 (keine Soft-404); /index.php/component/search/ liefert 500.",
   "404-Verhalten in Ordnung; der 500-Fehler der Suchkomponente ist unschön.", "UB.D02", B + "/index.php/component/search/?searchword=test", "cosmetic", "fix",
   "Suchkomponente deaktivieren oder reparieren; nicht indexierbar machen (noindex). Joomla-Super-User nötig.", "741", "S", ["EV-D-variants"], tool=GET,
   verify="curl -sI liefert nicht 500", refetch={"tool": "re-run scripts/area_d/d2_variants.py", "cost": "0 EUR"}, hint="EV-D-variants kind=system", text="Die interne Suche liefert einen Serverfehler.")

# ---------------- D07: sitemap / robots / canonical / head ----------------
it("website", "Es gibt keine XML-Sitemap: /sitemap.xml, /sitemap_index.xml, /index.php/sitemap und die Komponentenadresse antworten 404; robots.txt hat keine Sitemap-Zeile (Standard-Joomla-Datei von 2023).",
   "Google muss alle 62 Seiten allein über Links finden; neue oder verwaiste Seiten werden spät oder nie entdeckt.", "UB.D07", B + "/sitemap.xml", "leaks_link_power", "fix",
   "Sitemap-Erweiterung in Joomla einrichten (nur die gewollten 200-Seiten, ohne Parameter- und Kategorie-Duplikate), Zeile 'Sitemap: https://www.stuerzl-steuerstrafrecht.de/sitemap.xml' in robots.txt, Einreichung in der Search Console. Siehe auch Bereich E (UB.E03).",
   "741", "M", ["EV-D-variants", "EV-D-robots"], tool=GET, verify="GET /sitemap.xml liefert 200 mit XML; robots.txt enthält die Sitemap-Zeile",
   refetch={"tool": "re-run scripts/area_d/d2_variants.py", "cost": "0 EUR"}, hint="EV-D-variants kind=system; EV-D-robots", source_field="B06.03",
   text="Die Website hat keine Sitemap; Google kann die Seiten nur über Links entdecken.")

it("website", "robots.txt sperrt /components/, /cache/, /plugins/ u. a.; 17 Stylesheet- und Script-Dateien der Startseite liegen in gesperrten Pfaden (u. a. die Hauptdatei sppagebuilder.css und das Template-CSS unter /cache/).",
   "Google kann die Seite womöglich nicht so darstellen, wie Besucher sie sehen; ob das einen Schaden verursacht, zeigt nur die Search Console (URL-Prüfung).", "UB.D07", B + "/robots.txt",
   "leaks_link_power", "fix",
   "Disallow-Zeilen für /components/, /cache/, /plugins/, /modules/, /layouts/, /libraries/ entfernen oder für die Asset-Pfade Allow-Ausnahmen setzen. Vorher in der Search Console 'Live-URL testen' (gerenderte Ansicht) prüfen. Search Console fehlt noch.",
   "741", "S", ["EV-D-robots", "EV-D-perf-assets"], tool=GET, verify="Alle Assets der Startseite erlaubt laut robots.txt; URL-Prüfung zeigt die Seite vollständig",
   refetch={"tool": "re-run scripts/area_d/d5_perf_assets.py", "cost": "0 EUR"}, hint="EV-D-perf-assets own_host_assets_blocked_by_robots",
   text="Die robots.txt sperrt Ordner mit Design- und Script-Dateien; Google sieht die Seite dadurch eventuell unvollständig.")

it("website", "Indexierbarkeit geprüft: keine Seite hat noindex (47 mit 'index, follow', 15 ohne Robots-Tag), kein X-Robots-Tag, jede Seite hat einen Canonical auf sich selbst; einzige Abweichung ist eine Seitenzahl-Adresse mit doppelt kodiertem &amp;.",
   "Keine gewollte Seite ist versehentlich ausgeschlossen.", "UB.D07", "alle 62 gecrawlten URLs mit Status 200", "cosmetic", "keep", "Keine Änderung.", "741", "S",
   ["EV-D-analysis", "EV-D-crawl-data"], tool=GET, verify="Re-Crawl: keine Seite mit noindex", refetch={"tool": CR, "cost": "0 EUR"},
   text="Keine Seite ist versehentlich von der Suche ausgeschlossen.")

it("website", "26 Seiten haben zwei H1: alle 25 Leistungsseiten (9 Bereiche, 16 Unterseiten; erste H1 immer „Leistungen“, zweite der Bereichsname) und die Kontaktseite (Frankfurt am Main / München). Frühere Zählung 27: heute 26.",
   "Die generische erste H1 „Leistungen“ steht vor dem Thema jeder Leistungsseite und schwächt das Themensignal.", "UB.D07", "26 URLs (Liste in EV-D-groups h1_two)", "leaks_link_power", "fix",
   "Den Seitentitel-Baustein im Template von H1 auf einen Absatz oder h2 umstellen, damit nur die thematische Überschrift H1 ist. Joomla-Super-User nötig.", "741", "M",
   ["EV-D-groups", "EV-D-analysis"], tool=GET, verify="Re-Crawl: h1_count = 1 auf allen Leistungsseiten", refetch={"tool": CR, "cost": "0 EUR"},
   hint="EV-D-groups h1_two", source_field="B06.03",
   text="Auf den Leistungsseiten stehen zwei Hauptüberschriften; die erste ist nur das Wort „Leistungen“.")

it("website", "14 Seiten haben keine H1: alle 10 Teamseiten (Personenseiten) und 4 Aktuelles-Listen (/aktuelles und 3 Kategorieadressen). Frühere Zählung 18: heute 14 (die Differenz waren Duplikat-URLs mit &amp;).",
   "Die Personenseiten ohne H1 tragen den Namen nicht als Hauptüberschrift; für Namenssuchen ist das ein schwaches Signal.", "UB.D07", "14 URLs (Liste in EV-D-groups h1_none)", "cosmetic", "fix",
   "Auf Teamseiten den Namen der Person als H1 setzen. Die Listen-Duplikate werden mit H-D-014 bereinigt.", "741", "S", ["EV-D-groups", "EV-D-analysis"], tool=GET,
   verify="Re-Crawl: h1_count = 1 auf allen Teamseiten", refetch={"tool": CR, "cost": "0 EUR"}, hint="EV-D-groups h1_none",
   text="Auf den Teamseiten fehlt die Hauptüberschrift mit dem Namen der Person.")

it("website", "Die FAQ-Seite (2.525 Wörter) hat 6 H1 (Titel und die Abschnitte I bis IV als H1).", "Abschnittsüberschriften sollten H2 sein; sonst gibt es keine Rangfolge.",
   "UB.D07", B + "/index.php/faq", "cosmetic", "fix", "Abschnittsüberschriften auf H2 ändern, nur den Seitentitel als H1 lassen.", "741", "S", [pg("_index.php_faq"), "EV-D-groups"], tool=GET,
   verify="Re-Crawl: faq h1_count = 1", refetch={"tool": CR, "cost": "0 EUR"}, text="Die FAQ-Seite nutzt für Abschnittstitel die Hauptüberschrift mehrfach.")

it("website", "52 von 62 Seiten teilen dieselbe Meta-Description („STÜRZL Steuerstrafrecht ist eine Kanzlei mit Spezialisierung …“). Titel folgen dem Muster „Stürzl Steuerstrafrecht – <Menüname>“; die Startseite endet auf „Home“.",
   "Gleiche Beschreibung auf fast allen Seiten gibt dem Suchergebnis keinen seitenspezifischen Text.", "UB.D03", "52 URLs (EV-D-groups same_meta_description_pages)", "cosmetic", "fix",
   "Für jede Leistungsseite eine eigene Beschreibung schreiben (Inhalt vom Kunden; Berufsrecht prüfen, siehe D11). Titel und H1 der Startseite sind Wachstumsarbeit (Backlog Punkt 5), kein Schaden.",
   "741", "M", ["EV-D-groups", "EV-D-analysis"], tool=GET, verify="Re-Crawl: keine Meta-Description auf mehr als 2 Seiten identisch", refetch={"tool": CR, "cost": "0 EUR"},
   text="Fast alle Seiten haben dieselbe Beschreibung im Suchergebnis.")

it("website", "Strukturierte Daten: auf allen Seiten steht derselbe LegalService-Block (Adresse Wiesenhüttenstraße 17, Zeiten 09:00-18:00, Gründerin nur als Name). München fehlt, die Person hat keine Details (Titel, sameAs).",
   "Unvollständig; für Suchmaschinen fehlt der zweite Standort. Die Adresse ist ohnehin veraltet (Umzug 05.10.), das gehört zu Bereich C.", "UB.D07", B + "/", "cosmetic", "fix",
   "Nach Adress-Sperre durch Martin: Adresse aktualisieren, München als eigenen Standort und Person-Schema ergänzen. Ergänzung ist Wachstumsarbeit, nur die Adresse ist Schadensbehebung.", "741", "M",
   [pg(""), "EV-D-crawl-data"], tool=GET, verify="Schema-Test auf der Startseite zeigt die bestätigte Adresse und München", refetch={"tool": CR, "cost": "0 EUR"},
   hint="Bereich C: Adressabgleich", source_field="B06.03", text="Die strukturierten Daten kennen nur den Frankfurter Standort mit alter Adresse.")

it("website", "Geschwindigkeit nur teilweise neu geprüft: Antwortzeit der Startseite 1,18 / 1,67 / 1,13 s; im HTML 27 Scripts (376 KB), 12 Stylesheets (857 KB), 9 Bilder (rund 0,9 MB). Der frühere LCP-Wert 7,2 s (08.10.) konnte nicht neu gemessen werden: PageSpeed-API antwortet 429 und es ist kein Render-Werkzeug erlaubt.",
   "Langsame Seiten verschlechtern Nutzersignale; der LCP-Wert selbst ist hier nicht neu belegt.", "UB.D07", B + "/", "leaks_link_power", "fix",
   "LCP in der Search Console (Core Web Vitals) oder per PageSpeed mit Schlüssel neu messen; danach Cache, Bildgrößen (fusszeile5.jpg 288 KB), CSS-Bündelung. Joomla-Super-User nötig.", "741", "M",
   ["EV-D-perf-assets", "EV-D-psi-attempt"], conf="verified", tool="requests GET (Timing), PageSpeed API (429)", verify="LCP unter 2,5 s auf Mobil",
   refetch={"tool": "re-run scripts/area_d/d5_perf_assets.py; PSI needs an API key", "cost": "0 EUR"}, hint="LCP 7,2 s ist derived (08.10.2026, Messung der Vorsession), nicht neu belegt",
   text="Die Startseite lädt langsam; die genaue Ladezeit wird mit einem Messwerkzeug nachgeprüft.")

# ---------------- D03: duplicates ----------------
it("website", "Die Kategorie „Aktuelles“ ist unter mehreren URLs erreichbar: /index.php/aktuelles, …/category/allgemein?Itemid=228 und …?Itemid=0 (letztere beiden inhaltlich identisch), dazu Seitenzahl-Adressen …start=10 (eine mit doppelt kodiertem &amp;amp;) und RSS- und Atom-Feeds mit 200.",
   "Mehrere Adressen für dieselbe Liste verteilen Signale und erzeugen Crawl-Abfall.", "UB.D03", B + "/index.php/component/content/category/allgemein?Itemid=0", "leaks_link_power", "merge",
   "301 von …category/allgemein?Itemid=0 und …?Itemid=228 auf /index.php/aktuelles; Seitenzahl-Links ohne &amp;amp; ausgeben; Feeds abschalten oder noindex. Vorher klären, warum /aktuelles nur 308 Wörter zeigt und die Kategorie 788 (Liste vollständig?).",
   "741", "M", ["EV-D-analysis", "EV-D-feeds-pagination", pg("_index.php_component_content_category_allgemein_Itemid_228")], tool=GET,
   verify="curl -sI …Itemid=0 liefert 301 auf /index.php/aktuelles", refetch={"tool": "re-run scripts/area_d/d2b_feeds.py", "cost": "0 EUR"},
   hint="redirect-map.json Zeilen category_duplicate", text="Die Nachrichtenliste ist unter mehreren Adressen erreichbar.")

it("website", "Vier Seiten-Paare haben identischen Text (Ähnlichkeit 100 %): Bereich Steuerstrafrecht = Unterseite Selbstanzeige & Korrekturberatung; Bereich Selbstanzeigen = Unterseite Selbstanzeige-Beratung/Begleitung; Bereich Ordnungswidrigkeiten = Unterseite Steuerordnungswidrigkeiten; sowie die zwei Kategorie-Adressen von „Aktuelles“.",
   "Die Unterseiten zeigen nur den Text des Bereichs; sie tragen eigenen Titel, aber keinen eigenen Inhalt und konkurrieren mit der Bereichsseite.", "UB.D03", "3 Seitenpaare (EV-D-groups exact_text_duplicates)",
   "leaks_link_power", "merge",
   "Entscheidung nach GSC-Daten: die Seite mit Klicks/Backlinks behalten, die andere per 301 zusammenführen. Alternative (empfohlen, wenn die Unterseite gewollt ist): eigenen Text schreiben statt 301. Solange keine Search-Console-Daten vorliegen, nichts umleiten.",
   "741", "M", ["EV-D-analysis", "EV-D-groups"], tool="python shingle analysis of live crawl", approval="blocked", conf="derived",
   verify="Pro Paar: ein Ziel mit 200, das andere 301; oder Ähnlichkeit unter 50 %", refetch={"tool": "re-run scripts/area_d/d4_analyze.py", "cost": "0 EUR"},
   hint="Blockiert: Search-Console-Klicks pro Seite fehlen (kein GSC-Zugang). redirect-map.json Zeilen exact_duplicate", source_field="B06.03",
   text="Drei Leistungs-Unterseiten haben exakt denselben Text wie ihre übergeordnete Seite.")

it("website", "Vier weitere Paare sind zu über 80 % ähnlich (Jaccard 0,82 bis 0,87): Einzelpersonen-Bereich mit seiner Unterseite Ordnungswidrigkeiten sowie der Unternehmens-Bereich mit zwei Unterseiten und diese Unterseiten untereinander; weitere 18 Paare liegen zwischen 0,5 und 0,8.",
   "Sehr ähnliche Texte auf verwandten Seiten teilen Rankingsignale.", "UB.D03", "4 Paare (EV-D-groups near_duplicates_jaccard_ge_0_8)", "leaks_link_power", "fix",
   "Pro Unterseite eigenen, fachlich anderen Text vom Kunden einholen (Fälle ohne Mandantenbezug); keine Zusammenlegung ohne GSC-Daten.", "client", "L", ["EV-D-analysis", "EV-D-groups"],
   tool="python shingle analysis of live crawl", conf="derived", verify="Re-Scan: kein Paar über 0,8", refetch={"tool": "re-run scripts/area_d/d4_analyze.py", "cost": "0 EUR"},
   hint="EV-D-analysis dupes_ge_0_5", text="Mehrere Leistungsseiten sind einander im Text sehr ähnlich und brauchen eigene Inhalte.")

# ---------------- D04: AI-slop heuristic ----------------
it("website", "Heuristik: 46 Sätze (ab 40 Zeichen) stehen wortgleich auf mindestens 4 Seiten (u. a. „Durch die Spezialisierung in diesem Bereich haben wir eine besondere fachliche Expertise …“); Bereichs- und Unterseiten teilen bis zu 100 % ihrer Sätze. Wenige Standardfloskeln (kompetent, diskret, auf Augenhöhe).",
   "Wiederholter Textbaustein ohne eigenen Mehrwert pro Seite; ob das als KI-Text oder Vorlage zu werten ist, entscheidet ein Mensch.", "UB.D04", "alle Leistungsseiten (EV-D-boilerplate)",
   "cosmetic", "keep", "Nicht bewertet. Zur manuellen Prüfung durch Martin. Rewrite mit echten Fachinhalten siehe H-D-015/H-D-016.", "741", "S", ["EV-D-boilerplate"],
   tool="python heuristic", conf="derived", verify="Menschliche Prüfung", refetch={"tool": "re-run scripts/area_d/d6_boilerplate.py", "cost": "0 EUR"},
   hint="Prüfung durch Mensch erforderlich (needs human review)", safe=False)

# ---------------- D05: thin ----------------
it("website", "Die 25 Leistungsseiten sind dünn: 9 Bereichsseiten mit 111 bis 261 Wörtern, 16 Unterseiten mit 180 bis 373 Wörtern (frühere Angabe 114 bis 376; 16 Unterseiten, nicht 17).",
   "Gewollte Leistungsseiten mit wenig eigenem Text ranken kaum; heute liegt „anwalt steuerstrafrecht“ auf Platz 27 (08.10.).", "UB.D05", "25 URLs (EV-D-groups thin_service_words)",
   "leaks_link_power", "fix", "Pro Seite echten Fachtext (Ablauf, Fristen, Risiken, FAQ) vom Kunden einholen; Standard: startseite-money-page-standard.md. Texte nur mit Berufsrechtsprüfung (D11).",
   "client", "L", ["EV-D-groups", "EV-D-analysis"], tool=GET, verify="Re-Crawl: jede Leistungsseite über 600 Wörter und mit eigenem Text", refetch={"tool": CR, "cost": "0 EUR"},
   hint="Backlog Punkt 11 und 13", text="Die Leistungsseiten enthalten nur kurze Texte und sollten ausführlicher werden.")

it("website", "6 von 10 Teamseiten haben unter 120 Wörter (44, 77, 77, 83, 102, 114); nur 3 haben über 270 Wörter.",
   "Personenseiten tragen die fachliche Glaubwürdigkeit; kurze Seiten zeigen wenig.", "UB.D05", "10 URLs (EV-D-groups thin_team_bios_words)", "cosmetic", "fix",
   "Pro Person Kurzvita, Sprachen, Veröffentlichungen ergänzen (Texte und Freigabe von den Personen). Titel und Auszeichnungen nur nach Titelprüfung (D11).", "client", "M", ["EV-D-groups"],
   tool=GET, verify="Mindestens 150 Wörter je Person", refetch={"tool": CR, "cost": "0 EUR"}, text="Mehrere Teamseiten sind sehr kurz.")

it("website", "12 Beitragsseiten unter Aktuelles sind sehr kurz; 7 haben unter 60 Wörter (33 bis 59: Presse, Vortrag, Veranstaltungshinweis, Ranking WirtschaftsWoche u. a.).",
   "Dünne Pressenotizen ohne eigenen Inhalt; ungewollte Seiten sollten zusammengeführt statt gelöscht werden.", "UB.D05", "12 URLs (EV-D-groups news_articles_words)", "cosmetic", "fix",
   "Entweder auf mindestens 150 Wörter mit Quelle und Datum ausbauen oder auf eine Seite 'Presse' zusammenführen (301). Nicht löschen; erst GSC-Daten und Backlinks prüfen.",
   "741", "M", ["EV-D-groups"], tool=GET, verify="Re-Crawl", refetch={"tool": CR, "cost": "0 EUR"}, text="Mehrere Beitragsseiten enthalten nur zwei Zeilen.")

# ---------------- D06: orphans / menu-only ----------------
it("website", "Keine echten Waisenseiten: jede der 62 gefundenen Seiten hat mindestens einen Link. 10 Seiten (Start, FAQ, Kontakt, Team, Friends, Join our Team, Aktuelles, Impressum, Datenschutz, Nutzungsbedingungen) sind aber nur über Menü oder Fußzeile verlinkt, ohne Link im Fließtext einer anderen Seite; darunter die stärkste Textseite (FAQ, 2.525 Wörter) und die Kontaktseite.",
   "Ohne Fließtext-Links sieht Google FAQ und Kontakt nicht als wichtig für die Leistungsseiten.", "UB.D06", B + "/index.php/faq", "leaks_link_power", "fix",
   "Aus den Leistungsseiten per Fließtext auf passende FAQ-Abschnitte und die Kontaktseite verlinken (Linkplan in Bereich E04). Seiten, die in keiner Verlinkung vorkommen (z. B. neu angelegte), findet nur eine Sitemap oder GSC.",
   "741", "M", ["EV-D-groups", "EV-D-analysis"], tool="python link graph of live crawl", conf="derived", verify="Jede Leistungsseite verlinkt im Text auf Kontakt, jede FAQ-Gruppe hat einen Eingangslink",
   refetch={"tool": "re-run scripts/area_d/d4_analyze.py", "cost": "0 EUR"}, hint="EV-D-groups menu_only_pages; Verlinkungsplan in Bereich E",
   text="Wichtige Seiten wie FAQ und Kontakt sind nur über das Menü verlinkt, nicht aus den Inhalten.")

# ---------------- /lina 404 with backlinks ----------------
it("website", "Die ehemalige Team-Adresse /index.php/lina antwortet 404, hat laut gespeicherter Ankerdatei aber 5 Backlinks von 4 Domains (alle aus dem Forum-Thread, siehe H-D-0%d)." % 0,
   "Toter Link mit Backlinks.", "UB.D01", B + "/index.php/lina", "leaks_link_power", "redirect",
   "Niedrige Priorität. 301 auf /index.php/team, nachdem der Kunde bestätigt hat, dass die Person nicht mehr im Team ist. Die einzigen bekannten Links stammen aus dem Forum-Thread.",
   "741", "S", ["EV-D-variants", "EV-D-bl-anchors", "EV-D-bl-groups"], conf="derived", tool="requests GET + stored anchors file (2026-10-09)", verify="curl -sI /index.php/lina liefert 301 auf /index.php/team",
   refetch={"tool": "re-run scripts/area_d/d2_variants.py", "cost": "0 EUR"}, hint="redirect-map.json Zeile lina", safe=False,
   collected=M["EV-D-variants"]["collected_at"])
lina_id = items[-1]["id"]

# ---------------- D08: negative PR / brand SERP ----------------
forum_id = it("search_index", "Ein anonymer Forum-Thread (Titel „Rate this German tax lawyer - link“, 21 Beiträge, 13.-14.04.2026) steht unter zwei Domains (autoadmit.com, xoxohth.com) und verlinkt Kanzlei-, Team- und Bildseiten. Er enthält herabsetzende Äußerungen über das Aussehen der Inhaberin und weiterer Frauen im Team sowie beleidigende Beiträge; zur anwaltlichen Arbeit, zu Mandanten oder Fällen steht nichts darin.",
   "Reputationsfall, kein Linkfall: Herabsetzung benannter Personen. In den Top 10 der Markensuchen taucht der Thread nicht auf (nur bei gezielter Suche).", "UB.D08", "https://www.autoadmit.com/thread.php?thread_id=5856705&forum_id=2",
   "cosmetic", "keep",
   "Entscheidung über Meldung oder rechtlichen Weg liegt bei Martin und der Rechtsanwältin der Kanzlei; kein Linkfall. Kein Disavow vor dieser Entscheidung. Optional: Meldung an den Betreiber der Plattform (Belästigung), Erfolg unsicher (anonymes Forum). Es wird niemand kontaktiert.",
   "client", "S", ["EV-D-forum-thread-notes", "EV-D-brand-serp"], tool="firecrawl_scrape (MCP)", destructive=True, approval="proposed",
   verify="Entscheidung dokumentiert; falls Meldung: Statusmeldung der Plattform", refetch={"tool": "firecrawl_scrape URL, maxAge 0 (1 credit)", "cost": "0 EUR (Firecrawl credits)"},
   hint="Nur Notizen im Beleg gespeichert, Forentext nicht kopiert (Rechte Dritter). 'needs human review'", safe=False)

it("search_index", "Google-Autocomplete ergänzt „stürzl steuerstrafrecht“ nur neutral (münchen, fotos, anja stürzl steuerstrafrecht); zu erfahrungen, bewertung, abzocke, kosten, betrug, skandal liefert Google für Kanzlei, Person und „kanzlei stürzl“ keinen Vorschlag. In den Top 10 (Firecrawl-Websuche) zu „Stürzl Steuerstrafrecht Erfahrungen Bewertung“ steht kein negatives Ergebnis.",
   "Geprüft und in Ordnung: keine negative Markensuche erkennbar.", "UB.D08", "Google Autocomplete (hl=de), Firecrawl-Websuche", "cosmetic", "keep",
   "Keine Änderung. Prüfung monatlich wiederholen.", "741", "S", ["EV-D-autocomplete", "EV-D-brand-serp"], tool="Google suggest endpoint + firecrawl_search",
   verify="Wiederholung der 28 Abfragen", refetch={"tool": "re-run scripts/area_d/d8_autocomplete.py", "cost": "0 EUR"},
   hint="Firecrawl-Index ist ein Ersatz für die Google-Ergebnisseite, nicht die Seite selbst", text="Bei der Suche nach dem Kanzleinamen erscheinen keine negativen Ergänzungen oder Treffer.")

it("search_index", "Der Autocomplete für den Personennamen „anja stürzl“ ergänzt u. a. „afd“ und „transparente demokratie“. Öffentliche Berichte (Cicero, WELT, Wikipedia, ARD) nennen Dr. Stürzl als Vorsitzende der Initiative Transparente Demokratie. Was genau die Ergänzung „afd“ auslöst, ist nicht belegt.",
   "Politische Zuordnung im Namens-Autocomplete kann Mandanten verunsichern; ob das ein Schaden ist, ist ein Urteil der Mandantin, kein Scan-Befund.", "UB.D08", "Google Autocomplete 'anja stürzl'", "cosmetic", "keep",
   "Nur zur Kenntnis und zur Entscheidung der Mandantin. Keine Maßnahme durch 741, keine Gegenmaßnahme, kein Linkfall. 'needs human review'.", "client", "S",
   ["EV-D-autocomplete", "EV-D-brand-serp"], tool="Google suggest endpoint + firecrawl_search", destructive=False, verify="-", refetch={"tool": "re-run scripts/area_d/d8_autocomplete.py", "cost": "0 EUR"},
   hint="Sensibles Thema; nicht in Kundenansicht ohne Martins Freigabe", safe=False)

# ---------------- D09: reviews ----------------
it("review", "anwalt.de (öffentlich): Kanzlei 5,0 bei 79 Bewertungen, Dr. Stürzl 5,0 bei 55 Bewertungen, alle 55 mit 5 Sternen, keine 1- bis 4-Sterne-Bewertung. Von 10 sichtbaren Daten liegen 5 Bewertungen zwischen 08. und 11.04.2026; insgesamt gibt es drei Tage mit je zwei Bewertungen. Kein objektiver Beleg für gekaufte oder gefälschte Bewertungen.",
   "Kontext für die Bewertungslage; auffällig sind nur die einheitlichen 5 Sterne und die kleine Häufung im April.", "UB.D09", "https://www.anwalt.de/anja-stuerzl/bewertungen", "cosmetic", "keep",
   "Keine Meldung. Vollständige Liste (alle Daten) manuell prüfen ('needs manual review'). Wir posten keine Gegenbewertungen und antworten nicht für die Kanzlei.", "client", "S",
   ["EV-D-anwaltde-reviews", "EV-D-brand-serp"], tool="firecrawl_scrape (MCP, query format)", verify="-", refetch={"tool": "firecrawl_scrape anwalt.de bewertungen (query format)", "cost": "0 EUR (Firecrawl credits)"},
   hint="Nur 10 von 55 Daten sichtbar; kein Bewertungstext gespeichert. anwalt.de zeigt noch die alte Adresse (Bereich C)", safe=False)

it("review", "Die Google-Bewertungen beider Profile (Frankfurt, München) sind in diesem Lauf nicht lesbar: kein Local-Falcon-Lesewerkzeug verbunden, Browser-Automation ausgeschlossen. Letzter bekannter Stand (01.10.2026): Frankfurt 5,0 / 14, München 5,0 / 1.",
   "Ohne Lesezugriff sind 1-Stern-Häufungen und Tagescluster nicht prüfbar.", "UB.D09", "GBP Frankfurt ChIJyVGAdikEaW8RUOWpEJs-2XA und München", "cosmetic", "keep",
   "Im nächsten Lauf mit angeschlossenem Local-Falcon-Lesewerkzeug oder GBP-Zugang lesen (Datum, Sterne, Verlauf).", "741", "S", ["EV-D-gbp-reviews-unreadable"],
   conf="derived", tool="none (source unreadable)", approval="blocked", verify="Bewertungsliste mit Daten gelesen", refetch={"tool": "Local Falcon MCP reviews read or GBP login", "cost": "0 EUR / credits"},
   hint="Quelle unleserlich, nicht 'nichts gefunden'", safe=False, collected=M["EV-D-gbp-reviews-unreadable"]["collected_at"])

# ---------------- D10: backlinks (stored 2026-10-09) ----------------
it("backlink", "Gruppe A: 37 Spam-Domains (Linkpaket-Anker „High Quality Dofollow Backlinks DA 50 PA 40 Premium PBN …“ und „Premium SEO Authority Backlinks …“), 33 davon erstmals zwischen 08/2026 und 10/2026 gesehen, 4 älter (12/2024 bis 05/2025). Insgesamt 38 Backlinks aus Gruppe A, 33 davon mit PBN-Ankern, bei 100 Backlinks im Profil.",
   "Gekauftes oder automatisch gesetztes Linkpaket; schadet nicht sicher, ist aber ein Risiko und ein Warnsignal.", "UB.D10", "disavow-stuerzl-2026-10-09.txt (37 domain:-Zeilen)", "leaks_link_power", "report",
   "Disavow-Datei in der Search Console hochladen. Die Datei existiert (nicht hochgeladen). Upload braucht Search-Console-Zugriff (offen) und Martins Go. Vorher die Kanzlei fragen, ob jemand Links gekauft hat.",
   "741", "S", ["EV-D-disavow-liste", "EV-D-disavow-file", "EV-D-bl-groups", "EV-D-bl-anchors"], conf="derived", tool="DataForSEO Backlinks (stored pull, 2026-10-09)", approval="blocked", collected=STORED,
   verify="Search Console zeigt die hochgeladene Datei; nach 4 Wochen neue Backlink-Daten", refetch={"tool": "DataForSEO Backlinks pull (paid, not run)", "cost": "paid, not run in this scan"},
   hint="Stand 09.10.2026, nicht neu gezogen. 33 PBN-Anker-Links von 100 Backlinks", safe=False, source_field=None)

it("backlink", "Gruppe B: 8 Tool-Seiten (Website-Checker, Kurz-URL-Dienste), alle nofollow, Spam-Score 25 bis 50.", "Geben keine Linkkraft weiter; kein Handlungsbedarf.", "UB.D10",
   "anchorurl.cloud, bye.fyi, drjack.world, jake.eu, piclur.com, ready.pro, screenshots.wiki, shortenurls.eu", "cosmetic", "keep", "Nicht disavowen, nur beobachten.", "741", "S",
   ["EV-D-disavow-liste", "EV-D-bl-refdomains"], conf="derived", tool="DataForSEO Backlinks (stored pull, 2026-10-09)", collected=STORED, verify="-", refetch={"tool": "DataForSEO Backlinks pull (paid, not run)", "cost": "paid, not run"}, safe=False)

it("backlink", "Gruppe C (Forum): autoadmit.com (15 Backlinks, erstmals 15.04.2026) und xoxohth.com (10 Backlinks, 21.04.2026) verlinken die Kanzlei aus demselben Thread; Spam-Score 0, Domain-Rang 82 und 72.",
   "Echte, thematisch fremde Domains: ein Reputationsfall (siehe Forum-Eintrag), kein Spam-Link.", "UB.D10", "autoadmit.com, xoxohth.com", "cosmetic", "keep",
   "Kein Disavow, bevor der rechtliche Weg entschieden ist. Entscheidung bei Martin und der Rechtsanwältin der Kanzlei; kein Linkfall.", "client", "S",
   ["EV-D-bl-refdomains", "EV-D-bl-groups", "EV-D-forum-thread-notes"], conf="derived", tool="DataForSEO Backlinks (stored pull, 2026-10-09) + live thread read", destructive=True, collected=STORED,
   verify="-", refetch={"tool": "DataForSEO Backlinks pull (paid, not run)", "cost": "paid, not run"}, depends=[forum_id], hint="Thread live am 11.10.2026 gelesen (verified), Backlinkzahlen aus 09.10. (derived)", safe=False)

it("backlink", "Gruppe C (US-Verzeichnis): bestattorneyusa.com (2 Backlinks) und bestattorneyus.com (3) führen automatisch erzeugte Profile mit falschen Orten in der Profil-URL (anja-sturzl-tucson, lea-wimmer-boston).",
   "Falsche Angaben zur Kanzlei in einem Fremdverzeichnis; geringe Reichweite.", "UB.D10", "bestattorneyusa.com, bestattorneyus.com", "cosmetic", "claim",
   "Profil beanspruchen und korrigieren oder Löschung beim Betreiber verlangen; danach über Disavow entscheiden. Kein Kontakt ohne Martins Go.", "741", "S",
   ["EV-D-disavow-liste", "EV-D-bl-refdomains"], conf="derived", tool="DataForSEO Backlinks (stored pull, 2026-10-09)", collected=STORED, verify="Profil zeigt korrekte Orte oder ist entfernt",
   refetch={"tool": "DataForSEO Backlinks pull (paid, not run)", "cost": "paid, not run"}, safe=False)

it("backlink", "Gruppe C (Blog): reimes-presseblick.blogspot.com setzt 2 Dofollow-Links mit dem Anker „Fachanwältin für Steuerrecht“ auf die Team-Seite (Spam-Score 15, erstmals 06/2025). Gruppe C (Host): gkwsaa.easypanel.host, ein zufälliger Hosting-Host mit 1 Backlink.",
   "Kontext der Beiträge unbekannt; erst lesen, dann entscheiden.", "UB.D10", "reimes-presseblick.blogspot.com, gkwsaa.easypanel.host", "cosmetic", "keep",
   "Beitrag lesen ('needs human review'). Wenn der Kontext die Kanzlei in ein schlechtes Licht rückt: Disavow. Host beobachten.", "741", "S",
   ["EV-D-disavow-liste", "EV-D-bl-refdomains"], conf="derived", tool="DataForSEO Backlinks (stored pull, 2026-10-09)", collected=STORED, verify="-",
   refetch={"tool": "DataForSEO Backlinks pull (paid, not run)", "cost": "paid, not run"}, safe=False)

it("backlink", "Gruppe D (behalten): bestlawyers.com, anwaltauskunft.de, tax-talents.de, tzelepis.de.", "Gute oder harmlose Links.", "UB.D10", "4 Domains", "cosmetic", "keep",
   "Nicht anfassen.", "741", "S", ["EV-D-disavow-liste", "EV-D-bl-refdomains"], conf="derived", tool="DataForSEO Backlinks (stored pull, 2026-10-09)", collected=STORED, verify="-",
   refetch={"tool": "DataForSEO Backlinks pull (paid, not run)", "cost": "paid, not run"}, safe=False)

it("backlink", "Unverlinkte Erwähnungen live bestätigt (3 Beispiele): LTO (Wechsel von Dr. Stürzl), JUVE (Gründung der Boutique) und ZRI (Büroeröffnung München) nennen die Kanzlei im Text, enthalten aber keinen Link auf stuerzl-steuerstrafrecht.de.",
   "Lücke, kein Schaden: gehört in den Wachstumsplan. Keine Rangminderung durch das Fehlen.", "UB.D10", "lto.de, juve.de, zri-online.de", "cosmetic", "keep",
   "gap not harm: moved to growth backlog (Linkaufbau, Presse-Ansprache über Backlog Punkt 9). Hier keine Maßnahme.", "741", "S",
   ["EV-D-mention-lto", "EV-D-mention-juve", "EV-D-mention-zri", "EV-D-mentions-summary", "EV-D-mention-search"], tool=GET, verify="-",
   refetch={"tool": "re-run scripts/area_d/d10_mentions.py", "cost": "0 EUR"}, hint="Weitere Erwähnungen laut Audit 08.10.: RWS, azur, Capital u. a., nicht einzeln geprüft", safe=False)

# ---------------- D11: advertising law (text hits, no legal judgement) ----------------
it("website", "Rangfolgen und Auszeichnungen werden im Text als Superlative genannt: „Beste Anwältin“ (Best Lawyers, 2023-2027), „Deutschlands beste Kanzleien 2025“, „Beste Kanzleien 2025 und 2026“ (Handelsblatt), „TOP Anwalt Steuerstrafrecht 2025“, „Top Kanzlei 2024“ (WirtschaftsWoche), „renommiertesten Kanzleien“ (3 Seiten). Standort: Seiten von Dr. Stürzl, Lea Wimmer, Nachrichtenliste.",
   "Werbung mit Auszeichnungen und Superlativen kann nach BORA/UWG eine Quellen- und Belegangabe verlangen; hier nur Fundstellen, kein Rechtsurteil.", "UB.D11", B + "/index.php/dr-anja-stuerzl", "cosmetic", "keep",
   "Human review, no legal judgement: Kanzlei oder Fachanwalt für Berufsrecht prüft Quelle, Jahr und Methode jeder Auszeichnung. Trefferliste in EV-D-adlaw-hits (category ranking_award, superlative).", "client", "S",
   ["EV-D-adlaw-hits"], tool="python regex scan of live crawl", verify="Prüfergebnis der Kanzlei", refetch={"tool": "re-run scripts/area_d/d11_adlaw.py", "cost": "0 EUR"}, safe=False,
   hint="305 Treffer insgesamt; Zahl enthält Wiederholungen im Seitenboilerplate")

it("website", "Ergebnis- und Leistungsversprechen im Text: Überschrift „Selbstanzeigen: Ihre Chance auf Schutz bei steuerlichen Korrekturen und Straffreiheit selbst im Falle von vorsätzlich hinterzogenen Steuern“ (Bereichsseite und 5 Seiten mit demselben Text), „garantieren wir Ihnen qualifizierte, diskrete …“ und „So garantieren wir Ihnen eine Beratung auf …“, „Das für Sie beste Ergebnis steht dabei zu jedem Zeit …“, „die beste Lösung“ (Friends, Kanzlei).",
   "Garantie- und Erfolgsaussagen sind bei Rechtsberatung riskant (UWG, BORA); hier nur Fundstellen, kein Rechtsurteil.", "UB.D11", B + "/index.php/selbstanzeigen-steuerliche-korrekturen", "cosmetic", "keep",
   "Human review, no legal judgement: Kanzlei prüft Formulierungen mit Berufsrecht; bei Textänderungen nur Texte des Kunden verwenden.", "client", "S", ["EV-D-adlaw-hits"],
   tool="python regex scan of live crawl", verify="Prüfergebnis der Kanzlei", refetch={"tool": "re-run scripts/area_d/d11_adlaw.py", "cost": "0 EUR"}, safe=False,
   hint="EV-D-adlaw-hits category guarantee_success (mit vielen Datenschutz-Treffern, die harmlos sind)")

it("website", "Selbstbeschreibungen mit Spezialisierung und Fachlichkeit: „Spezialisierung“ auf 52 Seiten in der Standard-Beschreibung, „hochspezialisierte Boutique“, „führenden Sozietäten/Beratern“ (Beschreibung anderer), „besondere fachliche Expertise“ (5 Seiten), „Experten aus unserem Netzwerk“ (für externe Berater, nicht als Titel). „Spezialist“ wird nicht als Titel der Anwältinnen geführt; es kommt nur im Plural für externe Fachleute vor.",
   "BORA verlangt bei Spezialisierungshinweisen Zurückhaltung und Wahrheit; hier nur Fundstellen, kein Rechtsurteil.", "UB.D11", "alle Seiten (Meta-Description und Boilerplate)", "cosmetic", "keep",
   "Human review, no legal judgement: Kanzlei prüft, ob 'Spezialisierung' und 'hochspezialisiert' mit Tätigkeitsschwerpunkten nach BORA gedeckt sind.", "client", "S", ["EV-D-adlaw-hits"],
   tool="python regex scan of live crawl", verify="Prüfergebnis der Kanzlei", refetch={"tool": "re-run scripts/area_d/d11_adlaw.py", "cost": "0 EUR"}, safe=False)

it("website", "Titel: „Fachanwältin für Steuerrecht“ (Dr. Stürzl, seit 2021) und „Zertifizierte Beraterin für Steuerstrafrecht (DAA)“ sind dokumentiert (Bestätigung der Kanzlei steht noch aus). Die Seite von Lea Wimmer nennt ebenfalls „Fachanwältin für Steuerrecht“ (seit 2017); dieser Titel steht nicht in den dokumentierten Angaben. Ein „Fachanwalt für Strafrecht“ wird nirgends geführt; „Fachanwaltskurs Strafrecht 2023“ ist ein Kurs, kein Titel.",
   "Fachanwaltstitel sind nur mit Verleihung zulässig; der zweite Titel ist hier nicht belegt.", "UB.D11", B + "/index.php/lea-wimmer", "cosmetic", "fix",
   "needs title check: Kanzlei bestätigt Titel und Jahr jeder Person (Anwaltskammer-Nachweis). Bis dahin keine Neuveröffentlichung der Titel in Schema, Verzeichnissen oder Anzeigen.", "client", "S",
   [pg("_index.php_lea-wimmer"), pg("_index.php_dr-anja-stuerzl"), "EV-D-adlaw-hits"], tool="python regex scan of live crawl", verify="Titelbestätigung dokumentiert",
   refetch={"tool": "re-run scripts/area_d/d11_adlaw.py", "cost": "0 EUR"}, safe=False)

it("website", "„Strafverteidiger/in“ und „Strafverteidigung“ werden an 13 Stellen als Selbstbeschreibung genutzt (u. a. „Strafverteidigerin mit Leidenschaft“ auf der Startseite). Es ist kein Fachanwaltstitel. Der Kunde wünscht „Strafverteidiger“ als Anzeigenbegriff (Onboarding 06.10.).",
   "Zur Kenntnis: Begriff ist keine geschützte Bezeichnung; die Kanzlei entscheidet über die Verwendung.", "UB.D11", B + "/", "cosmetic", "keep",
   "Human review, no legal judgement: nur Fundstelle; vor dem Einsatz in Anzeigentexten Berufsrecht prüfen lassen.", "client", "S", ["EV-D-adlaw-hits"],
   tool="python regex scan of live crawl", verify="-", refetch={"tool": "re-run scripts/area_d/d11_adlaw.py", "cost": "0 EUR"}, safe=False)

# ---------------- 741 side ----------------
it("website", "Unsere eigene Review-Seite für den Kunden behauptet „München: kein Profil auffindbar“ (Zeile 1052) und „München ohne Profil“ (Zeile 1011) und schlägt vor, das München-Profil neu anzulegen (Zeilen 1010, 1066, 1084). Das ist falsch: das München-Profil existiert (Oberanger 32, 5,0 bei 1 Bewertung, 01.10.2026). Die Seite ist live (noindex) unter 741.studio/review/anja-stuerzl/.",
   "Eine Neuanlage kann ein Doppelprofil erzeugen und dem Ranking schaden; die Falschaussage schwächt unsere Glaubwürdigkeit.", "UB.D11", "/Users/martindrendel/741website/04_site/review/anja-stuerzl/index.html",
   "leaks_link_power", "fix",
   "Aussagen zu München korrigieren (Profil vorhanden; Handlung: Kategorien, Fotos, Bewertungen, NAP) und Seite neu ausliefern. Datei nur gelesen, nicht geändert; Änderung braucht Martins Go.", "741", "S",
   ["EV-D-741-review-page"], tool="grep on local file + curl", verify="grep 'kein Profil auffindbar' liefert 0 Treffer in Datei und Live-Seite",
   refetch={"tool": "grep -n 'kein Profil auffindbar' 04_site/review/anja-stuerzl/index.html", "cost": "0 EUR"}, hint="Quelle: Woche-1-Befunde Abschnitt 1 (München existiert); lokale Datei ist ungetrackt und unterscheidet sich vom Live-Stand", safe=False)

# fix the lina item reference to the forum item
for d in items:
    if "H-D-0%d" % 0 in d["item"]:
        d["item"] = d["item"].replace("H-D-0%d" % 0, forum_id)
# fix reference ids inside text (H-D-014 etc. are set after we know ids)
byk = {d["check_id"] + "|" + d["item"][:40]: d["id"] for d in items}
def find(prefix):
    for d in items:
        if d["item"].startswith(prefix):
            return d["id"]
    raise KeyError(prefix)
cat_id = find("Die Kategorie „Aktuelles“")
exact_id = find("Vier Seiten-Paare")
near_id = find("Vier weitere Paare")
for d in items:
    d["action_detail"] = d["action_detail"].replace("H-D-014", cat_id).replace("H-D-015/H-D-016", f"{exact_id}/{near_id}")
    d["item"] = d["item"]

run = {
    "run_id": "stuerzl-2026-10-11-scan-partD", "client_slug": "stuerzl", "client_id": "b6f6e303-50e4-4afb-a343-337206cec316", "domain": "stuerzl-steuerstrafrecht.de",
    "mode": "scan", "from_audit_run": None, "previous_run_id": None, "started_at": "2026-10-11T05:19:00+02:00", "timezone": "Europe/Berlin", "catalog_version": "ub-catalog-0.1-draft",
    "params": {
        "scanned_areas": ["D"], "area_note": "Part D only (agent S2). Other areas are in their own part folders.",
        "crawl": "GET only, manual redirect follow, 0.3 s delay, UA 741-unburning-scan/1.0, BFS from https://www.stuerzl-steuerstrafrecht.de/, depth<=4, internal links only",
        "sitemap_url": None, "gsc_property": "sc-domain:stuerzl-steuerstrafrecht.de (no access, gsc clicks unknown)",
        "with_backlinks": "stored 2026-10-09 files only, no new pull", "dataforseo": False, "falcon_scan": False, "nap_master": "nap-master.json (provisional, not used in area D)",
        "firecrawl": "used for brand SERP, forum thread, anwalt.de, unlinked mention search"},
    "cost": {"eur": 0, "credits": 0}}
reg = {"run": run, "items": items}
json.dump(reg, open(os.path.join(PART, "harm-register.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(items), "items")

# ---------------- redirect-map.json ----------------
BL = "unknown at URL level: stored pull 2026-10-09 has anchors and domains only; no URL-anchored backlink entry for this URL"
def row(old, status, kind, target, reason, approval="proposed", **kw):
    r = {"old_url": old, "status_now": status, "kind": kind, "gsc_clicks_90d": "unknown (no GSC access)", "backlinks": kw.pop("backlinks", {"count": None, "note": BL}),
         "target_url": target, "reason": reason, "type": 301 if target else None, "approval": approval}
    r.update(kw)
    return r
rows = [
 row(B + "/index.php/schwerpunkte", 404, "dead_internal_link", B + "/index.php/leistungen", "Home page link 'mehr zu den Schwerpunkten' points here; the Leistungen page lists the 9 areas. Also fix the home link itself.", linked_from=[B + "/"], backlinks={"count": 0, "note": "no URL-anchored backlink in stored anchors file (2026-10-09); pull reports broken_backlinks 0"}),
 row(B + "/tel.+498972444170", 404, "malformed_tel_href", None, "Not a page: malformed tel link. Fix the href to tel:+498972444170 on the pages that carry it. No redirect.", approval="proposed", linked_from=[B + "/index.php/dr-monika-glogger", B + "/index.php/lea-wimmer"], href_fix_to="tel:+498972444170"),
 row(B + "/tel.+4969298028870", 404, "malformed_tel_href", None, "Not a page: malformed tel link. Fix the href to tel:+4969298028870 on the pages that carry it. No redirect.", linked_from=[B + "/index.php/florentine-jilg", B + "/index.php/thorben-hoppe"], href_fix_to="tel:+4969298028870"),
 row(B + "/linkedin.com/in/dr-monika-glogger-geb-werndl-3354a9123", 404, "malformed_external_href", None, "Not a page: external link written without scheme. Fix the href to the full LinkedIn address (derived from the broken href, confirm with the person).", linked_from=[B + "/index.php/dr-monika-glogger"], href_fix_to="https://www.linkedin.com/in/dr-monika-glogger-geb-werndl-3354a9123"),
 row(B + "/index.php/lina", 404, "former_team_page_with_backlinks", B + "/index.php/team", "Former team page. Stored anchors file lists 5 backlinks from 4 domains, all from the forum thread (group C). Low priority; confirm the person left the team first.", backlinks={"count": 5, "referring_domains": 4, "note": "anchor = URL, first seen 2026-04-15, stored pull dated 2026-10-09 (derived)", "source_file": "baseline/bl_anchors.json"}),
 row(B + "/images/slider-arrow.svg", 404, "asset_404", None, "Image file missing; restore the file or remove the reference. No redirect.", backlinks={"count": 0, "note": "asset"}),
 row("https://www.otto-schmidt.de/seminare/seminare-steuerrecht/steuerstrafverfahren-und-besteuerungsverfahren", 404, "external_dead_link", None, "External site no longer has the page; remove the link on the 3 pages that carry it. No replacement URL found, none invented.", backlinks={"count": None, "note": "outbound link, not a backlink"}),
 row("http://stuerzl-steuerstrafrecht.de/", 301, "existing_301", "https://www.stuerzl-steuerstrafrecht.de", "single hop, keep", approval="keep", hops=1),
 row("http://www.stuerzl-steuerstrafrecht.de/", 301, "existing_301", "https://www.stuerzl-steuerstrafrecht.de/", "single hop, keep", approval="keep", hops=1),
 row("https://stuerzl-steuerstrafrecht.de/", 301, "existing_301", "https://www.stuerzl-steuerstrafrecht.de", "single hop, keep", approval="keep", hops=1),
 row("http://www.stuerzl-steuerstrafrecht.de/index.php/kanzlei", 301, "existing_301", B + "/index.php/kanzlei", "single hop, keep (same for https apex deep links)", approval="keep", hops=1),
 row(B + "/index.php", 200, "proposed_duplicate", B + "/", "Same page as the home page, self canonical, no redirect. 301 to /.", backlinks={"count": None, "note": BL}),
 row(B + "/index.php/", 200, "proposed_duplicate", B + "/", "Same page as the home page, self canonical, no redirect. 301 to /."),
 row(B + "/index.php/home", 200, "proposed_duplicate", B + "/", "Same page as the home page, self canonical, no redirect. 301 to /."),
 row(B + "/index.php/kanzlei/", 200, "proposed_duplicate_trailing_slash", B + "/index.php/kanzlei", "Trailing-slash twin with its own canonical. Rule: 301 every /index.php/<x>/ to /index.php/<x> (example row)."),
 row(B + "/index.php/component/content/category/allgemein?Itemid=228", 200, "category_duplicate", B + "/index.php/aktuelles", "Menu item 'Aktuelles' by raw component route; 788 words vs 308 on /aktuelles (check list completeness first)."),
 row(B + "/index.php/component/content/category/allgemein?Itemid=0", 200, "category_duplicate", B + "/index.php/aktuelles", "Identical text to ?Itemid=228 (similarity 1.0)."),
 row(B + "/index.php/steuerstrafrecht/selbstanzeige-korrekturberatung", 200, "exact_duplicate", B + "/index.php/steuerstrafrecht", "Text identical to the parent area page (similarity 1.0). Preferred fix is own text for the sub page; 301 only if the page is not wanted. GSC clicks needed to pick the stronger page.", approval="blocked"),
 row(B + "/index.php/selbstanzeigen-steuerliche-korrekturen/selbstanzeige-beratung-begleitung-selbstanzeige", 200, "exact_duplicate", B + "/index.php/selbstanzeigen-steuerliche-korrekturen", "Text identical to the parent area page (similarity 1.0). Same decision rule.", approval="blocked"),
 row(B + "/index.php/ordnungswidrigkeiten/steuerordnungswidrigkeiten", 200, "exact_duplicate", B + "/index.php/ordnungswidrigkeiten", "Text identical to the parent area page (similarity 1.0). Same decision rule.", approval="blocked"),
]
rm = {"run": "stuerzl-2026-10-11-scan-partD", "collected_at": now(),
      "backlink_data": "Stored pull of 2026-10-09 (DataForSEO Backlinks): site totals 100 backlinks, 58 referring domains; anchors and referring domains only, NO per-URL target list. Match by URL was possible only where an anchor equals the URL (/index.php/lina: 5 backlinks / 4 domains). Everything else is unknown or 0 in the anchors file. No new pull.",
      "gsc_note": "No Search Console access: every gsc_clicks_90d is unknown. Decision tree step 1 (never delete a URL with clicks or backlinks) cannot be completed for exact_duplicate rows, hence approval blocked.",
      "probes_not_in_wild": "Probed variants without index.php (e.g. /kanzlei, /steuerstrafrecht) and upper-case /index.php/Kanzlei return 404 and are not linked anywhere. Listed in EV-D-variants, not in this map.",
      "evidence": ["EV-D-crawl-data", "EV-D-variants", "EV-D-analysis", "EV-D-external-links", "EV-D-bl-anchors", "EV-D-feeds-pagination"],
      "rows": rows}
json.dump(rm, open(os.path.join(RUN, "redirect-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(rows), "redirect rows")
