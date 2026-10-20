#!/usr/bin/env python3 -I
"""Build part-E/harm-register.json from verified/derived evidence of area E. No guessing: numbers come from the evidence files."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from e_lib import ROOT, PART, now, save_evidence, load_manifest
HERE = os.path.dirname(os.path.abspath(__file__))
stats = json.load(open(f"{HERE}/_stats.json"))
graph = json.load(open(f"{HERE}/_graph.json"))
idx = json.load(open(f"{ROOT}/index-intended.json"))
plan = json.load(open(f"{ROOT}/link-plan.json"))
# derived evidence row for the graph + stats
save_evidence("EV-E-linkgraph", json.dumps({"derived_from": ["EV-E-crawl", "EV-E-crawl-html"], "method": plan["method"], "stats": stats,
               "repeated_block_fingerprints": graph["rep_fingerprints"], "pages": graph["pages"]}, indent=1, ensure_ascii=False),
              "json", "python3 + bs4 (derived)", "scripts/E/e4_graph.py and e5_build.py applied to the crawl bodies EV-E-crawl-html; content area = #sp-component", note="derived data, recomputable")
M = {e["id"]: e for e in load_manifest()["evidence"]}
def ts(*ids): return max(M[i]["collected_at"] for i in ids)

CRAWL = "python3 -I scripts/E/e2_crawl.py"
RF_CRAWL = {"tool": CRAWL, "params": "GET only, UA 741-unburning-scan/1.0, delay 0.3 s, depth 4", "cost": "0 EUR"}
SU = "needs Super User (Linkemann/Framotec)"
items = []
def add(**k):
    n = len(items) + 1
    base = {"id": f"H-E-{n:03d}", "area": "E", "destructive": False, "approval": "proposed", "approved_by": None, "approved_at": None, "wave": None,
            "snapshot_id": None, "rollback": None, "before": None, "after": None, "done_at": None, "depends_on": [], "client_safe": True}
    base.update(k)
    if "collected_at" not in base: base["collected_at"] = ts(*base["evidence_ids"])
    items.append(base)
    return base["id"]

n_in = len(stats["content_urls_in_search"]); n_out = len(stats["content_urls_not_in_search"])
n_total = n_in + n_out
svc_missing = [u for u in stats["content_urls_not_in_search"] if u.count("/") <= 4 and "/article/" not in u and u.split("/")[-1] not in ("florentine-jilg", "lenka-schluetter", "thorben-hoppe")]
n_art_out = sum(1 for u in stats["content_urls_not_in_search"] if "/article/" in u)
n_staff_out = sum(1 for u in stats["content_urls_not_in_search"] if u.split("/")[-1] in ("florentine-jilg", "lenka-schluetter", "thorben-hoppe"))
n_svc_out = n_out - n_art_out - n_staff_out

# ---------------- E01
h001 = add(entity="search_index", check_id="UB.E01", source_field=None, target="sc-domain:stuerzl-steuerstrafrecht.de",
 item="Der Search-Console-Zugriff fehlt: Die Abfrage mit dem 741-Dienstkonto liefert für die Domain-Property und beide URL-Property-Varianten HTTP 403, die Index-Lage der Website ist damit nicht lesbar.",
 why="Ohne Search Console lässt sich weder prüfen, welche Seiten indexiert sind, noch eine Sitemap einreichen oder eine Indexierung anfordern; ein Verifizierungs-Token liegt in DNS und im Startseiten-Head (die Property ist vermutlich verifiziert), der Inhaber ist aber ungeklärt (vermutlich Herr Linkemann).",
 severity="blocks_revenue", action="claim", actor="client", effort="S", approval="blocked",
 action_detail="needs Search Console access: Der Inhaber der Property fügt 741studio18@gmail.com und das 741-Reporting-Dienstkonto als Nutzer hinzu (nur Zugriffsanfrage vorbereiten, Versand nur mit Martins Go). Danach URL-Inspektion für alle gewollten URLs und den Sitemap-Status lesen.",
 verify_check="node scripts/E/e1_gsc_test.mjs out.json: sites.list enthält die Property, searchAnalytics.query und urlInspection liefern HTTP 200",
 confidence="verified", source_tool="Search Console API (Dienstkonto, readonly) und dig",
 evidence_ids=["EV-E-gsc-access-test", "EV-E-dns-txt", "EV-E-crawl"],
 refetch={"tool": "node scripts/E/e1_gsc_test.mjs <out.json>", "params": "3 Property-Varianten, 3 URLs", "cost": "0 EUR"},
 drilldown_hint="EV-E-gsc-access-test: steps[] (sites.list HTTP 200 mit 5 anderen Properties, alle Property-Aufrufe 403). Verifizierungs-Token: TXT-Eintrag in EV-E-dns-txt und meta google-site-verification auf der Startseite (EV-E-crawl) sind identisch. Bezug zu Bereich A (GSC-Eigentum).",
 client_safe=False)

add(entity="search_index", check_id="UB.E01", source_field=None, target="site:stuerzl-steuerstrafrecht.de",
 item=f"Ersatzprüfung ohne Search Console: Eine site:-Suche im Web-Index von Firecrawl (nicht Google, grob) listet 45 URLs, davon kommen {n_in} von {n_total} gelesenen Inhalts-URLs vor und {n_out} nicht ({n_svc_out} Leistungsseiten, {n_art_out} Beiträge, {n_staff_out} Mitarbeiterprofile).",
 why="Die Treffer zeigen ältere Titel und die alte Adresse (Stand vor dem Umbau), die Zahl ist nur ein grober Näherungswert; fehlende URLs gelten als nicht verifiziert, nicht als nicht indexiert.",
 severity="cosmetic", action="keep", actor="741", effort="S",
 action_detail="Nur dokumentieren. Nicht gelistet (unverified): " + "; ".join(u.replace("/index.php/", "") .split("?")[0] for u in stats["content_urls_not_in_search"]) + ". Nach Search-Console-Zugriff per URL-Inspektion prüfen.",
 confidence="derived", source_tool="firecrawl_search (Web-Index, nicht Google)",
 evidence_ids=["EV-E-site-search", "EV-E-site-search-2", "EV-E-crawl"],
 refetch={"tool": "firecrawl_search", "params": "query=site:stuerzl-steuerstrafrecht.de limit=50 location=Germany sources=web", "cost": "10 Credits, 0 EUR"},
 drilldown_hint="EV-E-site-search: queries[0].results (45 Zeilen). Vergleich in index-intended.json: Feld search_index_signal. Zusatzabfragen mit inurl: lieferten leere oder unpassende Treffer (EV-E-site-search-2), eine Abfrage scheiterte mit HTTP 429.",
 client_safe=False)

# ---------------- E02
add(entity="website", check_id="UB.E02", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/",
 item="Geprüft und in Ordnung: Startseite, Leistungen-Übersicht, 9 Leistungsbereiche und 16 Unterseiten liefern HTTP 200 und eine Canonical auf sich selbst, und keine der 64 gelesenen HTML-Seiten trägt noindex oder einen X-Robots-Tag.",
 why="Technisch ist jede beabsichtigte Seite indexierbar; eine frühere Notiz nennt 17 Unterseiten, der Crawl findet 16 (eine 17. Seite ist nicht verlinkt oder nicht vorhanden, unverified).",
 severity="cosmetic", action="keep", actor="741", effort="S",
 action_detail="Keine Änderung. Anzahl Unterseiten (16 gefunden, 17 genannt) mit der Kundin klären, falls eine Seite fehlt.",
 confidence="verified", source_tool="python requests + bs4 (GET only)", evidence_ids=["EV-E-crawl", "EV-E-crawl-html"], refetch=RF_CRAWL,
 drilldown_hint="index-intended.json: Zeilen mit class=service und intended=yes; Felder meta_robots, canonical_state, indexable_technically.",
 client_text="Alle Leistungsseiten sind technisch für Google zugänglich und nicht gesperrt.")

h_cat = add(entity="search_index", check_id="UB.E02", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/index.php/component/content/category/allgemein?Itemid=228",
 item="Das Beitrags-Archiv /index.php/component/content/category/allgemein ist in mehreren URL-Varianten (Itemid=228, Itemid=0, start=10, start=20) indexierbar, zwei Varianten erscheinen in der Ersatz-Suche, und die Seitenzahl-Links sind doppelt maskiert (&amp;amp;).",
 why="Ein Archiv ohne eigenen Suchwert verdoppelt die Beitragsinhalte und erzeugt zusätzliche URL-Varianten, die Crawl-Budget und Signale verteilen.",
 severity="leaks_link_power", action="fix", actor="741", effort="M", approval="blocked",
 action_detail=f"{SU}: Archiv auf noindex setzen oder per Canonical auf /index.php/aktuelles zusammenführen, doppelt maskierte Pagination-Links reparieren (Template/Joomla), RSS- und Atom-Links im Head entfernen oder belassen (Entscheidung). Mit Search Console danach neu prüfen.",
 verify_check="curl -s <Archiv-URL> | grep -i 'name=\"robots\"' zeigt noindex; Pagination-Link im Quelltext ohne &amp;amp;",
 confidence="derived", source_tool="python requests + bs4 und firecrawl_search",
 evidence_ids=["EV-E-crawl", "EV-E-probes", "EV-E-probes-2", "EV-E-site-search"], refetch=RF_CRAWL,
 drilldown_hint="index-intended.json: Zeilen class=archive. Signal 'in Suche' stammt aus dem Firecrawl-Index (grob). Feed-Links (RSS/Atom) stehen als rel=alternate auf 3 Archiv-Seiten, der Feed antwortet mit 200 (EV-E-probes: category_feed).",
 client_text="Ein Beitrags-Archiv der Website erscheint in mehreren doppelten Adress-Varianten und sollte für Suchmaschinen zusammengeführt werden.")

h_art = add(entity="search_index", check_id="UB.E02", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/index.php/aktuelles",
 item="Die 12 Beiträge unter Aktuelles liegen auf Komponenten-Adressen mit ?catid=10&Itemid=228, haben 33 bis 243 Wörter (7 davon unter 60) und verlinken auf keine Leistungsseite.",
 why="Als Presse- und Terminhinweise ohne Leistungsbezug sind sie als eigene Suchseiten schwach; ob sie bleiben sollen, entscheidet die Kanzlei.",
 severity="leaks_link_power", action="fix", actor="741", effort="M", approval="blocked",
 action_detail=f"decision_needed (Martin und Kundin): (a) behalten, mit Link zurück auf Aktuelles und auf eine Leistung sowie lesbarer Adresse, oder (b) zu einer Seite 'Presse und Vorträge' zusammenfassen und die alten Adressen weiterleiten (das wäre ein Merge, braucht eigenes Go). Umsetzung: {SU}.",
 verify_check="Nach Umsetzung: index-intended.json neu erzeugen; Beiträge mit Up-Link auf /index.php/aktuelles",
 confidence="verified", source_tool="python requests + bs4 (GET only)", evidence_ids=["EV-E-crawl", "EV-E-linkgraph"], refetch=RF_CRAWL,
 drilldown_hint="index-intended.json: class=blog, intended=review, verdict=decision_needed (12 Zeilen). Wörter je Beitrag in link-plan.json (Feld words). Vorschläge für Links stehen im Link-Plan als topical_lateral.",
 client_safe=False)

add(entity="website", check_id="UB.E02", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/index.php/team",
 item="6 der 10 Team-Profile sind dünn (44 bis 114 Wörter), keines der 10 verlinkt zurück auf die Team-Seite, und drei davon fehlen im Ersatz-Suchindex.",
 why="Profilseiten mit Inhalt sind Vertrauens-Signale, reine Assistenz-Profile mit wenigen Wörtern bringen wenig und sind eine Entscheidung der Kanzlei (Personenbezug).",
 severity="cosmetic", action="keep", actor="client", effort="S",
 action_detail="decision_needed: Die 4 inhaltsstarken Profile bleiben gewollt; Mitarbeiter-Profile (6) behalten, ausbauen oder nicht indexieren. Keine Änderung ohne Entscheidung.",
 confidence="verified", source_tool="python requests + bs4 (GET only)", evidence_ids=["EV-E-crawl", "EV-E-site-search"], refetch=RF_CRAWL,
 drilldown_hint="index-intended.json: Zeilen class_note 'Mitarbeiter-Profil, dünn'.", client_safe=False)

add(entity="website", check_id="UB.E02", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/index.php/kontakt",
 item="Es gibt keine eigene Standortseite für Frankfurt oder München; München erscheint nur auf der Kontaktseite (H1 'Frankfurt am Main' und 'München') und im Profil der Standortleiterin.",
 why="Für lokale Suchen mit Ortsbezug fehlt eine eigene indexierbare Zielseite je Standort; ob München zum 741-Paket gehört, ist offen.",
 severity="leaks_link_power", action="fix", actor="741", effort="L", approval="blocked",
 action_detail=f"decision_needed: Standortseiten Frankfurt und München anlegen (Inhalt über den Content-Pool, Adresse erst nach Sperre der NAP-Stammdaten). Seiten anlegen: {SU}. Keine neue Seite als Link-Ziel im Link-Plan verwendet.",
 verify_check="index-intended.json enthält Zeilen mit class=location und intended=yes, HTTP 200, Canonical auf sich selbst",
 confidence="verified", source_tool="python requests + bs4 (GET only)", evidence_ids=["EV-E-crawl", "EV-E-linkgraph"], refetch=RF_CRAWL,
 drilldown_hint="index-intended.json: class=location nur /index.php/kontakt. NAP-Stammdaten sind noch nicht gesperrt (nap-master.json).",
 client_text="Für Frankfurt und München gibt es keine eigenen Standortseiten; sie würden die Auffindbarkeit bei ortsbezogenen Suchen unterstützen.")

# ---------------- E03
add(entity="cms", check_id="UB.E03", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/sitemap.xml",
 item="Unter /sitemap.xml liegt keine Sitemap (HTTP 404) und die robots.txt enthält keine Sitemap-Zeile; eine OSMap-Sitemap existiert nur unter einer Komponenten-Adresse (/index.php?option=com_osmap&view=xml&id=1&format=xml, 22 URLs).",
 why="Suchmaschinen finden die vorhandene Sitemap nicht von allein, und ob sie in der Search Console eingereicht ist, ist ohne Zugriff unbekannt (unverified).",
 severity="leaks_link_power", action="fix", actor="741", effort="S", approval="blocked",
 action_detail=f"{SU} oder Hosting-Zugang (robots.txt ist eine Datei im Webroot, Artfiles, kein FTP-Zugang): Zeile 'Sitemap: <Adresse der OSMap-Sitemap>' in robots.txt ergänzen und die Sitemap in der Search Console einreichen (needs Search Console access). Optional: Weiterleitung /sitemap.xml auf die OSMap-Adresse.",
 verify_check="curl -s https://www.stuerzl-steuerstrafrecht.de/robots.txt | grep -i '^sitemap:' liefert eine Zeile; die Adresse antwortet mit 200 und XML",
 confidence="verified", source_tool="python requests (GET only)", evidence_ids=["EV-E-crawl", "EV-E-robots-txt", "EV-E-sitemap-osmap", "EV-E-probes"],
 refetch={"tool": "curl -s -A 741-unburning-scan/1.0 <url>", "params": "/sitemap.xml, /robots.txt, OSMap-URL", "cost": "0 EUR"},
 drilldown_hint="EV-E-crawl: pages[] mit discovered_via=sitemap_probe (404 für /sitemap.xml, /sitemap.xml.gz, /sitemap_index.xml; com_xmap und com_jmap nicht installiert; com_osmap liefert nach 303 die XML). Der 741-Joomla-Konto-Typ ist Administrator, nicht Super User: SP Page Builder und Global Config sind gesperrt, ob OSMap bearbeitbar ist, ist ungeprüft.",
 client_text="Die Website hat keine für Suchmaschinen auffindbare Sitemap; eine vorhandene Sitemap ist nicht in der robots.txt eingetragen.")

add(entity="cms", check_id="UB.E03", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/index.php?option=com_osmap&view=xml&id=1&format=xml",
 item=f"Die OSMap-Sitemap listet nur 22 URLs (Hauptseiten, Pflichtseiten, 10 Team-Profile) und lässt {len(stats['sm_missing_pages'])} Leistungsseiten (9 Bereiche, 16 Unterseiten) sowie {len(stats['sm_missing_articles'])} Beiträge aus.",
 why="Die wichtigsten Seiten für Mandantenanfragen fehlen in der Sitemap; alle 22 gelisteten URLs sind sauber (HTTP 200, Canonical auf sich selbst, keine Weiterleitung).",
 severity="leaks_link_power", action="fix", actor="741", effort="S", approval="blocked",
 action_detail=f"{SU}: In OSMap das Menü beziehungsweise die Inhalte der Leistungsseiten einbeziehen (Ursache vermutlich ein nicht eingebundenes Menü; ungeprüft), Beiträge nach Entscheidung H-E-005 einbeziehen oder weglassen, danach Sitemap neu lesen. Ob das 741-Administrator-Konto OSMap bearbeiten darf, ist ungeprüft.",
 verify_check="Sitemap neu lesen: enthält alle 9 Leistungsbereiche und 16 Unterseiten, keine 404-URL, keine Weiterleitung",
 confidence="verified", source_tool="python requests (GET only)", evidence_ids=["EV-E-sitemap-osmap", "EV-E-crawl"], refetch=RF_CRAWL,
 drilldown_hint="Vergleich Sitemap gegen Crawl: index-intended.json Feld in_sitemap. Alle Einträge haben changefreq=weekly und priority=0.5 (einheitlich, ohne Aussagekraft). Die Sitemap spiegelt die Menüpunkte; die Leistungsseiten stehen vermutlich in einem Menü, das OSMap nicht einbezieht (ungeprüft).",
 client_text="In der vorhandenen Sitemap fehlen alle Leistungsseiten.")

# ---------------- E04
add(entity="website", check_id="UB.E04", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/index.php/schwerpunkte",
 item="Vier interne Links führen auf nicht vorhandene Seiten (HTTP 404): 'mehr zu den Schwerpunkten' auf der Startseite (/index.php/schwerpunkte), ein LinkedIn-Link ohne Schema auf der Seite von Dr. Monika Glogger und zwei Telefon-Links ohne tel: auf den Profilen von Lea Wimmer und Thorben Hoppe.",
 why="Ein toter Link auf der Startseite verschenkt einen der wenigen Inhalts-Links der Startseite und lenkt Besucher ins Leere.",
 severity="leaks_link_power", action="fix", actor="741", effort="S", approval="blocked",
 action_detail=f"{SU} (SP Page Builder): /index.php/schwerpunkte auf /index.php/leistungen umstellen (bestehende Seite, Entscheidung Martin); LinkedIn-Link mit https://, Telefonlinks mit tel:+49… korrigieren.",
 verify_check="Crawl: keine internen Links mit HTTP 404 aus dem Inhaltsbereich",
 confidence="verified", source_tool="python requests + bs4 (GET only)", evidence_ids=["EV-E-crawl", "EV-E-baseline-crawl"], refetch=RF_CRAWL,
 drilldown_hint="Dieselben vier Links nannte der Crawl vom 08.10.2026 (EV-E-baseline-crawl, derived); heute erneut gelesen. index-intended.json: Zeilen mit http_status=404 und source=crawl.",
 client_text="Die Startseite verweist mit 'mehr zu den Schwerpunkten' auf eine Seite, die nicht mehr existiert; drei weitere Links sind fehlerhaft.")

add(entity="website", check_id="UB.E04", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/",
 item="Der Inhalt der Startseite verlinkt nur auf 3 Ziele (Kanzlei, Leistungen und die tote Schwerpunkte-Seite); kein Leistungsbereich, keine FAQ, kein Team und kein Kontakt sind im Inhalt verlinkt, und Aktuelles, Team, FAQ, Friends, Join our Team und Kontakt haben keinen einzigen eingehenden Inhalts-Link (nur das Menü).",
 why="Die 9 Leistungsbereiche sind erst über die Leistungen-Übersicht erreichbar (Klicktiefe 2), und die Startseite gibt ihnen keine Inhalts-Link-Kraft.",
 severity="leaks_link_power", action="fix", actor="741", effort="S", approval="blocked",
 action_detail=f"{SU}: Im Inhalt der Startseite die wichtigsten Leistungsbereiche und Kontakt verlinken (12 Vorschläge im Link-Plan, Typ home_to_service und home_to_core); Anker sachlich halten (BORA, UWG). Kein Menü-Umbau in diesem Vorschlag.",
 verify_check="Graph neu berechnen: Startseite mit mindestens 9 Inhalts-Links auf Leistungsbereiche",
 confidence="verified", source_tool="python requests + bs4 (GET only)", evidence_ids=["EV-E-crawl", "EV-E-linkgraph"], refetch=RF_CRAWL,
 drilldown_hint="link-plan.json: Seite '/', Felder outbound_content_links (3) und missing_links. Das Hauptmenü hat kein Aufklappmenü, die Leistungsbereiche stehen nur auf der Übersichtsseite.",
 client_text="Die Startseite verlinkt im Text nur wenige Ziele; wichtige Leistungsseiten sind nicht direkt erreichbar.")

add(entity="website", check_id="UB.E04", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/index.php/leistungen",
 item="In den Texten der 26 Leistungsseiten steht kein einziger Link auf die Startseite, die 9 Bereichsseiten verlinken nicht auf die Leistungen-Übersicht, und bei 10 der 16 Unterseiten besteht der Link nach oben nur aus einem auf allen 25 Seiten wiederholten Block mit 9 Bereichs-Links.",
 why="Die Verlinkung nach oben (Unterseite zu Bereich, Bereich zu Übersicht und Startseite) hängt an Navigationsblöcken statt an Verweisen im Text, und die Texte der Seiten (111 bis 373 Wörter) enthalten außer den Listen mit Unterseiten und Geschwisterseiten keine Links.",
 severity="leaks_link_power", action="fix", actor="741", effort="M", approval="blocked",
 action_detail=f"{SU}: Je Bereichsseite einen Textlink zurück auf /index.php/leistungen und auf die Startseite, je Unterseite einen Textlink auf den Bereich ergänzen (Vorschläge im Link-Plan: 9 child_to_parent, 10 child_to_parent_contextual, 10 service_to_home). Wiederholten Block belassen.",
 verify_check="Graph neu berechnen: outbound_to_parent_contextual_only=true für alle Unterseiten, Bereichsseiten mit Link auf Übersicht und Startseite",
 confidence="verified", source_tool="python requests + bs4 (GET only)", evidence_ids=["EV-E-crawl", "EV-E-crawl-html", "EV-E-linkgraph"], refetch=RF_CRAWL,
 drilldown_hint="link-plan.json: Felder outbound_to_parent, up_link_only_via_repeated_block, outbound_to_home. Methode: nur Links im Bereich #sp-component, Kopf-, Off-Canvas- und Fußmenü sind ausgeschlossen. Klicktiefe aller Leistungsseiten höchstens 3.",
 client_text="Die Leistungsseiten verweisen im Text nicht aufeinander und nicht zurück auf die Startseite.")

add(entity="website", check_id="UB.E04", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/index.php/ordnungswidrigkeiten",
 item="Die Unterseiten-Listen sind uneinheitlich: Ordnungswidrigkeiten nennt nur 2 seiner 3 Unterseiten (Steuerordnungswidrigkeiten fehlt), Zollstrafrecht listet stattdessen zwei Unterseiten von Ordnungswidrigkeiten, und Zoll-, Arbeits-, Korruptions- und Sonstiges Wirtschaftsstrafrecht haben keine Unterseiten (die letzten drei auch keinen Textlink).",
 why="Die Unterseite Steuerordnungswidrigkeiten hat deshalb keinen Link von ihrer Elternseite, und die Zollstrafrecht-Seite zeigt Listen einer fremden Seite.",
 severity="leaks_link_power", action="fix", actor="741", effort="S", approval="blocked",
 action_detail=f"{SU}: Link auf /index.php/ordnungswidrigkeiten/steuerordnungswidrigkeiten in der Ordnungswidrigkeiten-Liste ergänzen, falsche Liste auf /index.php/zollstrafrecht prüfen (Kopierfehler vermutet, ungeprüft). Entscheidung Kundin, ob die drei Bereiche ohne Unterseiten bleiben.",
 verify_check="Graph neu berechnen: parent_to_child ohne Lücken",
 confidence="verified", source_tool="python requests + bs4 (GET only)", evidence_ids=["EV-E-crawl", "EV-E-linkgraph"], refetch=RF_CRAWL,
 drilldown_hint="link-plan.json: Typ parent_to_child für /index.php/ordnungswidrigkeiten. Listen der Seiten in EV-E-linkgraph (pages[].contextual).",
 client_safe=False)

add(entity="website", check_id="UB.E04", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/index.php/faq",
 item="Die FAQ-Seite (2.525 Wörter, 6 H1) enthält keinen internen Link, und keine Seite verweist im Inhalt auf sie; sie ist nur über das Hauptmenü erreichbar.",
 why="Die inhaltsstärkste Seite der Website gibt ihre Themen (Strafverfahren, Kosten, Selbstanzeige) nicht an die passenden Leistungsseiten weiter.",
 severity="leaks_link_power", action="fix", actor="741", effort="S", approval="blocked",
 action_detail=f"{SU}: FAQ-Abschnitte I und III auf die Leistungsseiten Verteidigung im Steuerstrafverfahren und Selbstanzeigen verlinken, Abschnitt II auf Kontakt; Steuerstrafrecht und Selbstanzeigen verlinken zurück auf die FAQ (5 Vorschläge). H1-Struktur ist ein On-Page-Thema, nicht Teil dieses Plans.",
 verify_check="Graph neu berechnen: FAQ mit mindestens 3 ausgehenden Inhalts-Links und mindestens 2 eingehenden",
 confidence="verified", source_tool="python requests + bs4 (GET only)", evidence_ids=["EV-E-crawl", "EV-E-linkgraph"], refetch=RF_CRAWL,
 drilldown_hint="link-plan.json: Seite /index.php/faq, Typ topical_lateral. inbound_content_links=0: kein Link im Inhalt, nur das Menü verlinkt die Seite.",
 client_text="Die FAQ-Seite ist nicht mit den passenden Leistungsseiten verlinkt.")

add(entity="website", check_id="UB.E04", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/index.php/team",
 item="Die 10 Team-Profile werden nur von der Team-Seite verlinkt und verlinken selbst nirgends hin; das Profil der Standortleiterin München ist von der Kontaktseite aus nicht verlinkt.",
 why="Die Profile der Anwältinnen sind Vertrauens-Seiten, bekommen aber keine Verweise von Leistungs- oder Kontaktseiten.",
 severity="cosmetic", action="fix", actor="741", effort="S", approval="blocked",
 action_detail=f"{SU}: Je Profil einen Textlink zurück auf /index.php/team, auf der Kontaktseite beim Standort München einen Link auf /index.php/lea-wimmer. Weitere Verweise von Leistungsseiten auf Profile nur nach Entscheidung der Kundin (Berufsrecht, Werbung).",
 verify_check="Graph neu berechnen: alle 10 Profile mit Link auf /index.php/team",
 confidence="verified", source_tool="python requests + bs4 (GET only)", evidence_ids=["EV-E-crawl", "EV-E-linkgraph"], refetch=RF_CRAWL,
 drilldown_hint="link-plan.json: Seiten der Profile, Typ child_to_parent; Kontakt: topical_lateral.", client_safe=False)

add(entity="website", check_id="UB.E04", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/index.php/component/content/article/presse?catid=10&Itemid=228",
 item="Kein Beitrag verlinkt zurück auf Aktuelles (nur Vorher/Nächster-Links in einer Kette), 4 Beiträge stehen nicht auf der Aktuelles-Seite, und die Beiträge Veranstaltungshinweis und Presse liegen 4 Klicks von der Startseite entfernt.",
 why="Die Soll-Klicktiefe von höchstens 3 wird für 2 Beiträge überschritten, und die Beiträge geben keine Linkkraft an Leistungsseiten weiter.",
 severity="cosmetic", action="fix", actor="741", effort="S", approval="blocked",
 action_detail=f"{SU}: Entscheidung H-E-005 abwarten; bei 'behalten' je Beitrag Link auf /index.php/aktuelles und eine passende Leistung oder ein Profil (topical_lateral Vorschläge im Link-Plan, Passung prüft ein Mensch), die vier fehlenden Beiträge auf Aktuelles aufführen.",
 verify_check="Graph neu berechnen: Klicktiefe aller Beiträge höchstens 3, alle mit Up-Link",
 confidence="verified", source_tool="python requests + bs4 (GET only)", evidence_ids=["EV-E-crawl", "EV-E-linkgraph"], refetch=RF_CRAWL,
 drilldown_hint="link-plan.json: Felder click_depth_from_home_any_link und missing_links der 12 Beitragsseiten.", depends_on=[h_art], client_safe=False)

add(entity="website", check_id="UB.E04", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/index.php/leistungen",
 item="Geprüft und in Ordnung: Die Leistungen-Übersicht verlinkt im Inhalt alle 9 Bereiche, die 5 Bereiche mit Unterseiten führen diese auf (eine Lücke bei Ordnungswidrigkeiten, siehe oben), und alle 26 Leistungsseiten sind in höchstens 3 Klicks von der Startseite erreichbar.",
 why="Das Grundgerüst des umgekehrten Baums (Startseite, Übersicht, Bereich, Unterseite) steht; die Lücken liegen bei den Links nach oben und zur Startseite.",
 severity="cosmetic", action="keep", actor="741", effort="S", action_detail="Keine Änderung.",
 confidence="verified", source_tool="python requests + bs4 (GET only)", evidence_ids=["EV-E-crawl", "EV-E-linkgraph"], refetch=RF_CRAWL,
 drilldown_hint="link-plan.json: click_depth_from_home_content_links_only=3 für alle Unterseiten.")

# ---------------- E05
add(entity="cms", check_id="UB.E05", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/robots.txt",
 item="Die robots.txt sperrt /components/ und /cache/, doch auf allen 64 gelesenen HTML-Seiten liegen Stylesheets und Skripte (SP Page Builder, Template-Cache) genau in diesen Pfaden.",
 why="Google kann die Seiten dadurch womöglich nicht vollständig darstellen; die Wirkung ist ohne Search Console (Live-Test) unverified.",
 severity="leaks_link_power", action="fix", actor="741", effort="S", approval="blocked",
 action_detail=f"{SU} oder Hosting-Zugang (robots.txt im Webroot, Artfiles): Disallow-Zeilen für /components/ und /cache/ entfernen oder Allow-Ausnahmen für die CSS- und JS-Dateien setzen; danach Live-Test in der Search Console (needs Search Console access).",
 verify_check="curl -s https://www.stuerzl-steuerstrafrecht.de/robots.txt zeigt keine Sperre der Pfade /components/ und /cache/",
 confidence="verified", source_tool="python requests + bs4 (GET only)", evidence_ids=["EV-E-robots-txt", "EV-E-crawl"], refetch=RF_CRAWL,
 drilldown_hint="EV-E-crawl: pages[].resources_under_robots_disallow (z. B. /components/com_sppagebuilder/assets/css/sppagebuilder.css, /cache/com_templates/templates/edulif/*.css und *.js). Joomla-Standard-robots.txt, nicht angepasst.",
 client_text="Die Konfiguration sperrt Dateien, die Suchmaschinen zum Darstellen der Seiten brauchen.")

add(entity="cms", check_id="UB.E05", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/index.php/kanzlei?utm_source=test",
 item="Jede URL-Variante liefert HTTP 200 mit Canonical auf sich selbst: beliebige Parameter (?utm_source, ?print=1, ?start=10, Itemid-Werte), /index.php, /index.php/ und /index.php/home als Startseiten-Duplikate sowie die Variante mit Slash am Ende.",
 why="Mit den geplanten Google-Ads-Parametern (gclid, utm) entstehen laufend neue indexierbare Duplikate, und die Canonical bündelt sie nicht.",
 severity="leaks_link_power", action="fix", actor="741", effort="M", approval="blocked",
 action_detail=f"{SU} (Joomla-Plugin oder .htaccess): Canonical ohne Parameter ausgeben, /index.php und /index.php/home per 301 auf / leiten, Slash-Variante auf die Variante ohne Slash, Druckansicht und tmpl=component auf noindex. Vor Ads-Start umsetzen.",
 verify_check="curl -s '<URL>?utm_source=x' | grep canonical zeigt die Adresse ohne Parameter; /index.php antwortet 301 auf /",
 confidence="verified", source_tool="python requests + bs4 (GET only)", evidence_ids=["EV-E-probes", "EV-E-probes-2"],
 refetch={"tool": "python3 -I scripts/E/e3_probes.py", "params": "41 GET-Proben", "cost": "0 EUR"},
 drilldown_hint="EV-E-probes: Zeilen home_index_php, home_index_php_slash, home_index_php_home, trailing_slash, print, utm_param, tmpl_component; EV-E-probes-2: article_no_itemid, article_itemid0, article_other_itemid, leistungen_param. Intern wird keine dieser Varianten verlinkt (nur Fehlerseiten verlinken /index.php), das Risiko liegt in externen Links und Ads-Parametern.",
 client_text="Dieselbe Seite ist unter vielen Adress-Varianten erreichbar, die Suchmaschinen als Duplikate werten können.")

add(entity="cms", check_id="UB.E05", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/index.php/component/users/login",
 item="Mindestens 7 Joomla-System-Routen sind aufrufbar und indexierbar, ohne robots-Meta und mit dem Startseiten-Titel: Anmelden, Passwort zurücksetzen, Benutzername erfragen, Tags, Kontakt-Komponente, Suche (Finder) und Featured; dazu die unverlinkte HTML-Sitemap der OSMap und die Backend-Anmeldung /administrator/ (in robots.txt gesperrt).",
 why="Keine dieser Routen wird intern verlinkt und keine erscheint in der Ersatz-Suche, doch sie sind ohne Schutz ein mögliches Duplikat-Risiko mit identischem Titel.",
 severity="cosmetic", action="fix", actor="741", effort="S", approval="blocked",
 action_detail=f"{SU}: Komponenten, die nicht gebraucht werden, abschalten (Tags, Kontakt, Suche, Featured, Registrierung) oder auf noindex setzen; HTML-Sitemap der OSMap auf noindex setzen oder bewusst veröffentlichen. Zugang zu /administrator/ bleibt unverändert.",
 verify_check="Jede genannte Route antwortet mit 404 oder trägt meta robots noindex",
 confidence="verified", source_tool="python requests + bs4 (GET only)", evidence_ids=["EV-E-probes", "EV-E-crawl"],
 refetch={"tool": "python3 -I scripts/E/e3_probes.py", "params": "41 GET-Proben", "cost": "0 EUR"},
 drilldown_hint="EV-E-probes: Zeilen users_login, users_reset, users_remind, users_registration (303 auf Anmeldung), tags, contact_component, finder, featured, administrator. Die HTML-Sitemap (/index.php?option=com_osmap&view=html&id=1) steht in EV-E-crawl (discovered_via=sitemap_probe) und in index-intended.json.", client_safe=False)

add(entity="cms", check_id="UB.E05", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/index.php/component/search/?searchword=steuer&searchphrase=all",
 item="Die Suchroute /index.php/component/search/ antwortet mit HTTP 500 und zeigt im Seitentext eine Datenbank-Fehlermeldung ('Unknown column').",
 why="Eine Fehlerseite mit Datenbankdetails ist ein Sicherheits-Hinweis, kein Index-Thema; die Route wird nicht verlinkt.",
 severity="cosmetic", action="fix", actor="741", effort="S", approval="blocked",
 action_detail=f"{SU}: Suchkomponente deaktivieren oder reparieren; Hinweis an Bereich D (Sicherheit) weitergeben. Nicht erneut aufrufen.",
 verify_check="Route antwortet mit 404 ohne Datenbank-Details",
 confidence="verified", source_tool="python requests (GET only)", evidence_ids=["EV-E-probes"],
 refetch={"tool": "python3 -I scripts/E/e3_probes.py", "params": "Zeile search", "cost": "0 EUR"},
 drilldown_hint="EV-E-probes: Zeile search (final_status 500, title enthält die Fehlermeldung).", client_safe=False)

add(entity="website", check_id="UB.E05", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/index.php/join-our-team",
 item="Auf der Seite 'Join our Team' liegt ein Link mit der Adresse file:////Users/…/clip_filelist.xml (Einfüge-Rest aus Word) und dem Linktext hello@stuerzl-steuerstrafrecht.de, und im mobilen Menü zeigt das Logo auf 64 Seiten auf den Host ohne www, der per 301 weiterleitet.",
 why="Der Dateilink führt ins Leere und nennt einen lokalen Benutzerpfad, der Logo-Link kostet auf jeder Seite einen Weiterleitungsschritt; beides ist unordentlich, ohne messbaren Verlust.",
 severity="cosmetic", action="fix", actor="741", effort="S", approval="blocked",
 action_detail=f"{SU}: Dateilink entfernen; die Adresse hello@… mit der Kundin klären (öffentlich ist kanzlei@…); Logo-Link im mobilen Menü auf https://www.stuerzl-steuerstrafrecht.de/ ändern (Template-Einstellung).",
 verify_check="Crawl: kein file:-Link, kein interner Link auf stuerzl-steuerstrafrecht.de ohne www",
 confidence="verified", source_tool="python requests + bs4 (GET only)", evidence_ids=["EV-E-crawl"], refetch=RF_CRAWL,
 drilldown_hint="EV-E-crawl: pages[] URL /index.php/join-our-team, links[] mit href beginnend file:. Logo: links[] region=offcanvas, href https://stuerzl-steuerstrafrecht.de.", client_safe=False)

add(entity="website", check_id="UB.E05", source_field=None, target="https://www.stuerzl-steuerstrafrecht.de/index.php/aktuelles",
 item="Geprüft und in Ordnung: Keine Inhaltsseite hat eine Seitenleiste oder einen Linkblock mit 50 oder mehr Links, die meisten Seiten haben 23 bis 38 Links; nur Aktuelles (53) und die Archiv-Seiten (66) liegen darüber, weil jeder Beitrag dreifach verlinkt ist.",
 why="Es gibt keinen schweren Linkblock, der Linkkraft verwässert.",
 severity="cosmetic", action="keep", actor="741", effort="S", action_detail="Keine Änderung. Doppelte Beitragslinks (Bild, Titel, 'weiterlesen') sind unkritisch.",
 confidence="verified", source_tool="python requests + bs4 (GET only)", evidence_ids=["EV-E-crawl"], refetch=RF_CRAWL,
 drilldown_hint="EV-E-crawl: pages[].links[] gezählt je Seite.")

add(entity="website", check_id="UB.E05", source_field=None, target="https://stuerzl-steuerstrafrecht.de/",
 item="Geprüft und in Ordnung: http und Host ohne www leiten in einem Schritt per 301 auf https://www.stuerzl-steuerstrafrecht.de/ weiter, und nicht vorhandene Adressen liefern einen echten 404-Status (keine Soft-404).",
 why="Es gibt keine Weiterleitungskette und keine Weiterleitung auf eine irreführende Seite.",
 severity="cosmetic", action="keep", actor="741", effort="S", action_detail="Keine Änderung.",
 confidence="verified", source_tool="python requests (GET only)", evidence_ids=["EV-E-probes", "EV-E-crawl"],
 refetch={"tool": "python3 -I scripts/E/e3_probes.py", "params": "Zeilen scheme_*, apex_deep, 404_test*", "cost": "0 EUR"},
 drilldown_hint="EV-E-probes: scheme_http_www, scheme_http_apex, apex_deep, 404_test, 404_test_root.")

reg = json.load(open("/Users/martindrendel/741website/00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/harm-register.json"))["run"]
first = min(e["collected_at"] for e in M.values())
run = {"run_id": "stuerzl-2026-10-11-scan", "client_slug": "stuerzl", "client_id": "b6f6e303-50e4-4afb-a343-337206cec316", "domain": "stuerzl-steuerstrafrecht.de",
       "mode": "scan", "from_audit_run": None, "previous_run_id": None, "started_at": first, "timezone": "Europe/Berlin", "catalog_version": reg["catalog_version"],
       "params": {"sitemap_url": None, "sitemap_note": "none at /sitemap.xml; OSMap sitemap found at /index.php?option=com_osmap&view=xml&id=1&format=xml", "gsc_property": "sc-domain:stuerzl-steuerstrafrecht.de (HTTP 403, not readable)",
                  "crawl": "GET only, manual redirect follow, 0.3 s delay, depth 4, UA 741-unburning-scan/1.0", "with_backlinks": False, "falcon_scan": False, "dataforseo": False,
                  "nap_master": "nap-master.json", "url_inspection_sample": 0, "scanned_areas": ["E"], "areas_note": "Part file of area E only (UB.E01 to UB.E05). E01 and the indexed state of E02 are unverified without Search Console."},
       "cost": {"eur": 0, "credits": 16}}
out = {"run": run, "items": items}
os.makedirs(PART, exist_ok=True)
json.dump(out, open(os.path.join(PART, "harm-register.json"), "w"), indent=1, ensure_ascii=False)
import collections
print(len(items), dict(collections.Counter(i["severity"] for i in items)), dict(collections.Counter(i["approval"] for i in items)))
