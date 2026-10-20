"""Saves the relevant result rows (url, title, snippet as returned) of firecrawl_search calls 1-5 as evidence. Excerpts only; own website rows and unrelated rows omitted."""
import sys, json
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ub_lib import save_evidence
S = {
 "EV-C-search-1": {"query": '"STÜRZL Steuerstrafrecht" Frankfurt', "rows": [
  ("https://www.lto.de/kanzleien-unternehmen/transfermarkt/detail/198-dr-anja-stuerzl-wechselt-zu-stuerzl-steuerstrafrecht","Dr. Anja Stürzl wechselt zu Stürzl Steuerstrafrecht - LTO","Stürzl Steuerstrafrecht startet in Frankfurt am Main. ... zum Dezember 2023 in eigener Kanzlei selbstständig"),
  ("https://de.linkedin.com/company/stuerzl-steuerstrafrecht","STÜRZL Steuerstrafrecht - LinkedIn","716 Follower:innen auf LinkedIn. Aufklären. Verständigen. Verteidigen."),
  ("https://www.anwalt.de/anja-stuerzl","Rechtsanwältin Dr. Anja Stürzl LL.M. - Anwalt.de","Kanzlei STÜRZL Steuerstrafrecht. Wiesenhüttenstraße 17, 60329 Frankfurt am Main."),
  ("https://www.bestlawyers.com/firms/sturzl-steuerstrafrecht/104283/DE","STÜRZL Steuerstrafrecht - Germany Firm | Best Lawyers","two lawyers recognized by Best Lawyers across three practice areas"),
  ("https://www.anwalt.de/kanzlei-stuerzl-steuerstrafrecht","Kanzlei STÜRZL Steuerstrafrecht - Anwalt.de","Rating 5.0(79) Kontaktdaten ... 2. Adresse. Wiesenhüttenstraße 17 60329 Frankfurt am Main."),
  ("https://anwalt-lotse.de/rechtsanwaeltin/anja-stuerzl-frankfurt-5vtd/","Rechtsanwältin Dr. jur. Anja Stürzl, Frankfurt - Anwalt-Lotse","STÜRZL Steuerstrafrecht Wiesenhüttenstr. 17 60329 Frankfurt. Zweigstelle München. Dr. Anja Stürzl Rechtsanwältin Oberanger 32 80331 München. 089-72444170. 069 ..."),
  ("https://de.linkedin.com/in/dr-anja-st%C3%BCrzl-ll-m-a85934a5","Dr. Anja Stürzl LL. M. - LinkedIn","STÜRZL Steuerstrafrecht. Dez. 2023 - Heute. Frankfurt am Main, Hessen, Deutschland."),
  ("https://www.zri-online.de/aktuell/stuerzl-steuerstrafrecht-eroeffnet-buero-in-muenchen-79764/","STÜRZL Steuerstrafrecht eröffnet Büro in München - ZRI online","press article"),
  ("https://firmeneintrag.creditreform.de/60329/6070874119/DR_ANJA_STUERZL_STUERZL_STEUERSTRAFRECHT","Dr. Anja Stürzl, STÜRZL Steuerstrafrecht, Frankfurt","Creditreform Firmendatenbank, Rechtsanwaltskanzleien ohne Notariat, PLZ 60329"),
  ("https://www.instagram.com/reel/Daa0ROvgMDi/","reel by a photographer","mentions Stürzl Steuerstrafrecht in Frankfurt (third-party post)"),
  ("https://www.juve.de/markt-und-management/bekannte-steuerstrafrechtlerin-von-rettenmaier-gruendet-eigene-boutique/","JUVE article","press article, 'Stürzl Steuerstrafrecht' spelling"),
 ]},
 "EV-C-search-2": {"query": '"Wiesenhüttenstraße 17" Frankfurt Stürzl', "rows": [
  ("https://www.anwalt.de/anja-stuerzl","Rechtsanwältin Dr. Anja Stürzl LL.M. - Anwalt.de","Rating 5.0(55) Kanzlei STÜRZL Steuerstrafrecht. Wiesenhüttenstraße 17, 60329 Frankfurt am Main."),
  ("https://de.linkedin.com/company/stuerzl-steuerstrafrecht","STÜRZL Steuerstrafrecht - LinkedIn","Orte. Primär. Wiesenhüttenstraße 17. Frankfurt, Hessen 60329, DE."),
  ("https://de.maptons.com/p/3302892716","STÜRZL Steuerstrafrecht, Wiesenhüttenstraße 17, lageplan","STÜRZL Steuerstrafrecht, Wiesenhüttenstraße 17, Deutschland, rechtsanwalt, telefon +49 69 298028870. (maptons.com scraper, many language subdomains: de, mt, hr, bj, qa, ee, py, is)"),
  ("https://juwist.com/mitgliederliste/","Mitgliederliste - JuWiSt","Dr. Anja Stürzl, LL.M. STÜRZL Steuerstrafrecht Wiesenhüttenstraße 17 60329 Frankfurt am Main"),
  ("https://www.infobel.com/de/germany/sturzl_steuerstrafrecht/frankfurt_oder/DE109851584-069298028870/businessdetails.aspx","STÜRZL Steuerstrafrecht, Frankfurt (Oder), DE - Infobel","STÜRZL Steuerstrafrecht in Frankfurt (Oder). Wiesenhüttenstraße 17 60329 Frankfurt (Oder)."),
  ("https://kulturstiftung-ukraine.org/index.php/datenschutz","Datenschutz - Kulturstiftung Ukraine","Anja Stürzl Wiesenhüttenstraße 17 60329 Frankfurt am Main. Telefon: +49 69-29802887-0 (separate foundation using the firm address and phone)"),
  ("https://kulturstiftung-ukraine.org/index.php/gremien","Gremien - Kulturstiftung Ukraine","Kulturstiftung Ukraine | Wiesenhüttenstraße 17 | 60329 Frankfurt am Main."),
  ("https://www.anwalt.de/anja-stuerzl/kontakt","Kontaktdaten von Rechtsanwältin Dr. Anja Stürzl LL.M. - Anwalt.de","Rating 5.0(55) Adresse. Wiesenhüttenstraße 17 60329 Frankfurt am Main."),
  ("https://www.anwalt.de/verzeichnis/rechtsanwaelte.php?stadt=Woerth_am_Main&thema=Steuerstrafrecht&cityid=5807","anwalt.de city listing","Anja Stürzl LL.M. Kanzlei STÜRZL Steuerstrafrecht, Wiesenhüttenstraße 17, 60329 Frankfurt am Main"),
 ]},
 "EV-C-search-3": {"query": '"069 29802887" OR "069 298028870" OR "+49 69 298028870" Stürzl', "rows": [
  ("https://mt.maptons.com/p/3302892716","maptons.com","Wiesenhüttenstraße 17; +49 69 298028870; rechtsanwalt; date stamps 11:40 14.08.2026"),
  ("https://anwalt-lotse.de/rechtsanwaeltin/anja-stuerzl-frankfurt-5vtd/","Anwalt-Lotse Anja Stürzl","069-298028870. 0160-339****. stuerzl@stuerzl-steuerstrafrecht.de. STÜRZL Steuerstrafrecht Wiesenhüttenstr. 17 60329 Frankfurt."),
  ("https://www.11880.com/branchenbuch/frankfurt-am-main/081314253B114102102/stuerzl-steuerstrafrecht.html","STÜRZL Steuerstrafrecht Frankfurt | Juli 2026 aktualisiert - 11880","(069) 298028870. Wiesenhüttenstr. 17. 60329 Frankfurt (Gutleutviertel)."),
  ("https://anwalt-lotse.de/rechtsanwalt/cedric-euler-frankfurt-oscv/","Anwalt-Lotse Cedric Euler","069-298028870. 069-298028879. euler@stuerzl-steuerstrafrecht.de. Stürzl Steuerstrafrecht RAin Dr. Anja Stürzl Wiesenhüttenstr. 17 60329 Frankfurt."),
  ("https://anwalt-lotse.de/rechtsanwalt/thorben-hoppe-eschborn-gqmh/","Anwalt-Lotse Thorben Hoppe","STÜRZL Steuerstrafrecht Wiesenhüttenstr. 17 60329 Frankfurt. 069-298028870. 069-298028879."),
 ]},
 "EV-C-search-4": {"query": '"Stürzl Steuerstrafrecht" München Oberanger 32', "rows": [
  ("https://www.anwalt.de/kanzlei-stuerzl-steuerstrafrecht/kontakt","Kontaktdaten von Kanzlei STÜRZL Steuerstrafrecht - Anwalt.de","+49 69 298... anzeigen; +49 160 33... anzeigen; kanzlei@stuerzl-steuerstrafrecht.de"),
  ("https://anwaltauskunft.de/rechtsanwalt/wimmer-287f04ca/","Lea Wimmer - Deutsche Anwaltauskunft","STÜRZL Steuerstrafrecht Oberanger 32, 80331 München. +49 (89) 7244 41 70 wimmer@stuerzl-steuerstrafrecht.de"),
  ("https://anwalt-lotse.de/rechtsanwaeltin/monika-glogger-muenchen-bci8/","Anwalt-Lotse Monika Glogger","089-72444170 glogger@stuerzl-steuerstrafrecht.de. STÜRZL Steuerstrafrecht Oberanger 32 80331 München."),
  ("https://www.anwalt.de/lea-wimmer-2","Lea Wimmer - Fachanwältin für Steuerrecht - Anwalt.de","Rating 5.0(23) Kanzlei STÜRZL Steuerstrafrecht. Oberanger 32, 80331 München"),
  ("https://rechtecheck.de/anwalt/steuerrecht/weisswasser/page/247","Rechtecheck list page (Weisswasser)","Kanzlei: Kanzlei STÜRZL Steuerstrafrecht. Neuhauser Str. 3a, 80331 München Route. (0,0) 0. Bewerten Details."),
  ("https://rechtecheck.de/anwalt/groebenzell/page/196","Rechtecheck list page (Groebenzell)","Kanzlei: Kanzlei STÜRZL Steuerstrafrecht ... Oberanger 32, 80331 München Route ... Steuerrecht"),
  ("https://rechtecheck.de/anwalt/steuerrecht/olching/page/13","Rechtecheck list page (Olching)","Kanzlei STÜRZL Steuerstrafrecht. Neuhauser Str. 3a, 80331 München ... and Oberanger 32, 80331 München (two entries on one page)"),
  ("https://www.anwalt.de/verzeichnis/rechtsanwaelte.php?stadt=Unterhaching&thema=Steuerstrafrecht&cityid=9861","anwalt.de city listing","Kanzlei STÜRZL Steuerstrafrecht, Oberanger 32, 80331 München; rating 4.5(364) is the city-list average, not the firm"),
 ]},
 "EV-C-search-5": {"query": '"Stützel Steuerstrafrecht"', "rows": [
  ("(no row)","no result names a firm 'Stützel Steuerstrafrecht'","10 results returned: own site (first), ht-strafrecht.de, winheller.com, skb-legal.com, rudolph-recht.de, nwb.de, juris.de, duncker-humblot.de, kanzlei-fuer-strafrecht.de, schweitzer-online.de. None is a spam or misspelled listing of the firm."),
 ]},
}
for eid, d in S.items():
    rows = [{"url": u, "title": t, "snippet": s} for u, t, s in d["rows"]]
    save_evidence(eid, json.dumps({"tool": "firecrawl_search", "query": d["query"], "sources": ["web"], "note": "relevant rows only, snippets as returned (shortened)", "rows": rows}, ensure_ascii=False, indent=1), "json", "firecrawl_search", f"firecrawl_search query={d['query']!r} sources=[web]", "area_c", note="excerpt of tool response")
    print(eid, len(rows))
