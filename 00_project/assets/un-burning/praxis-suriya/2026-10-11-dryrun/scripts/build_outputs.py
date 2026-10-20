"""Build all Un-Burning dry-run output files from evidence. Read-only on the world; writes only in this folder."""
import sys, json, re, os, collections, urllib.parse
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ub_lib import ROOT, now, load_manifest, save_manifest, sha256
from crawl_lib import canon_key, is_internal

NOW = now()
CLIENT_ID = "3f71ef33-8c74-4ea1-b2d3-0273c2e99649"
J = lambda p: json.load(open(os.path.join(ROOT, p)))
sm = J("evidence/area_d/crawl-sitemap.json")
ex = J("evidence/area_d/crawl-extra.json")
an = J("evidence/area_d/analysis.json")
gsc = json.load(open(ROOT + "/../baseline/2026-10-01-gsc-export-90d.json"))
insp = {x["url"]: x for x in J("evidence/area_e/inspect-results.json")}
gsc_by = {canon_key(p["keys"][0]): p for p in gsc["pages"]}
rows = {r["key"]: r for r in an["rows"]}
P = lambda u: urllib.parse.urlparse(u).path or "/"
def gclicks(key): return gsc_by[key]["clicks"] if key in gsc_by else 0
def gimpr(key): return gsc_by[key]["impressions"] if key in gsc_by else 0

# ------------------------------------------------------------------ NAP master
nap_master = {
  "name": "Praxis Suriya", "owner": "Coralie Suriyapperuma (Heilpraktikerin)",
  "address": {"street": "Schützenpfad 29", "postal_code": "55218", "city": "Ingelheim am Rhein", "country": "DE"},
  "phone": "0174 7411087", "phone_e164": "+491747411087",
  "website": "https://www.suriya-praxis.de",
  "website_note": "Live site canonical and GSC property are the non-www host https://suriya-praxis.de/ (www answers 301 to non-www, verified). The memory master says www. Decision for Martin: pick one canonical form for all listings. Proposal: non-www, because the site, schema and GSC use it.",
  "email": "suriyapraxis@gmail.com",
  "hours": {"mon-sat": "07:30-20:00", "sun": "closed"},
  "categories_primary": "Heilpraktiker/in (Naturopath)",
  "legal_form": "Einzelunternehmen (Impressum: Coralie Suriyapperuma)",
  "locked_at": "2026-09-02", "locked_by": "Martin (Coralie confirmed name 02.09. and address 08.09. by WhatsApp)",
  "source": "memory praxis-suriya-client.md (SOURCE OF TRUTH) ; Supabase client_locations row cfec507f... (nap_status locked)",
  "confidence": "client_stated",
  "old_values": {
    "names": ["Praxis Suriya - Ayurveda & Naturheilkunde", "Heilpraktiker Ingelheim I Praxis Suriya - Ayurveda & Naturheilkunde", "Ayurveda Praxis Suriya Ingelheim", "Suriya Ingelheim", "Suriya Praxis", "Suriya Heilpraktikerin", "Praxis Suriya für Naturheilkunde und Ayurveda", "Praxis Coralie Suriyapperuma Heilpraktikerin"],
    "addresses": ["Binger Str. 41 / Bingerstr. 41 (former home, not found live anywhere in this run)"],
    "phones_found_in_the_wild_not_master": ["06132 9723199", "06132 9795890", "01622714361", "01573 0331732 (also written 0157 30 33 17 32)"],
    "phones_status": "Liveness of these numbers is NOT verified. Nobody called them. Needs Coralie's answer (client_stated)."
  },
  "conflicts_inside_the_master_sources": [
    {"field": "name", "supabase_client_locations.business_name": "Praxis Suriya - Ayurveda & Naturheilkunde", "memory_master": "Praxis Suriya", "evidence": ["EV-C-client-locations"]},
    {"field": "services", "supabase_client_locations.services": "contains 'Faszientherapie'", "memory_master": "Coralie does NOT offer Faszientherapie (08.09.)", "evidence": ["EV-C-client-locations"]},
    {"field": "socials.instagram", "supabase": "suriya.ayurveda", "site_schema_and_footer": "suriya.praxis", "evidence": ["EV-C-client-locations", "EV-D-crawl-sitemap"]},
    {"field": "website", "supabase": "https://suriya-praxis.de", "memory_master": "https://www.suriya-praxis.de", "evidence": ["EV-C-client-locations", "EV-A-headers-www"]}
  ],
  "collected_at": NOW
}

# ------------------------------------------------------------------ Listing NAP table (live checks)
def ph_ok(p): 
    d = re.sub(r"\D", "", p or ""); return d in ("491747411087", "01747411087", "1747411087", "00491747411087")
L = [
 # key, directory, url, name_found, name_ok, addr_ok, phone_found, phone_ok, hours_ok, evidence, how, note
 ("cylex-main", "Cylex", "https://web2.cylex.de/firma-home/praxis-suriya---ayurveda-_-naturheilkunde-10733378.html", "Heilpraktiker Ingelheim I Praxis Suriya - Ayurveda & Naturheilkunde", False, True, "06132 9723199 (landline) + 0174 7411087 (mobile)", False, False, "EV-C-scrape-cylex", "firecrawl_scrape", "Hours Mo-Fr 09-19, Sa closed (master Mo-Sa 07:30-20:00). Social: facebook.com/naturheilpraxissuriya, instagram.com/suriyapraxis. Page offers 'Eintrag uebernehmen' (unclaimed). Last update 19.05.2026."),
 ("cylex-duplicate", "Cylex", "https://web2.cylex.de/firma-home/suriyapperuma--coralie-nilmini-heilpraktikerin-14095381.html", "Suriyapperuma, Coralie Nilmini Heilpraktikerin", False, True, "01573 0331732", False, None, "EV-C-scrape-cylex", "firecrawl_scrape (nearby-entry block of the main page)", "Second Cylex entry at the same address. Seen only in the 'similar businesses' block, entry page itself not opened."),
 ("infobel-1", "Infobel", "https://www.infobel.com/de/germany/heilpraktiker_ingelheim_i_praxis_suriya_ayurveda_naturheilkunde/ingelheim_am_rhein/DE109349224/businessdetails.aspx", "Heilpraktiker Ingelheim I Praxis Suriya - Ayurveda & Naturheilkunde", False, True, None, None, None, "EV-C-listing-infobel-1", "requests GET", "Phone not shown on page. Shows 5.0 (12 bewertungen), same count as GBP."),
 ("infobel-2", "Infobel", "https://www.infobel.com/de/germany/suriya_heilpraktikerin/ingelheim_am_rhein/DE111780212-061329795890/businessdetails.aspx", "Suriya Heilpraktikerin", False, True, "06132 9795890 (in URL)", False, None, "EV-C-listing-infobel-2", "requests GET", "Second Infobel entry for the same practice."),
 ("theralupa-10902", "Theralupa", "https://www.theralupa.de/heilpraktiker/ayurveda-praxis-suriya-ingelheim-10902", "Ayurveda Praxis Suriya Ingelheim", False, True, "01622714361", False, None, "EV-C-listing-theralupa-10902", "requests GET", "Address written 'Schützenpfad29'. DR70 directory, it is one of the quality backlinks (Ahrefs free 15.08.)."),
 ("theralupa-11505", "Theralupa", "https://www.theralupa.de/heilpraktiker/suriya-ingelheim-11505", "Suriya Ingelheim", False, True, "06132 /9795890", False, None, "EV-C-listing-theralupa-11505", "requests GET", "Second Theralupa entry. Duplicate of 10902."),
 ("golocal", "GoLocal", "https://www.golocal.de/ingelheim/heilpraktiker/praxis-suriya-YUWGl/", "Praxis Suriya", True, True, "(06132) 979 58 90 + Mobil (0157) 30 33 17 32", False, False, "EV-C-listing-golocal", "requests GET", "Hours Mo 09-20, Di 10-20, Mi closed, Do/Fr 09-20, Sa 11-17 (master Mo-Sa 07:30-20:00). Marked 'Nutzermeldung - nicht von golocal geprueft'. 2 reviews. DR77 directory."),
 ("jameda", "Jameda", "https://www.jameda.de/profil/coralie-suriyapperuma", "Praxis Coralie Suriyapperuma Heilpraktikerin", False, True, "06132 9723199", False, None, "EV-C-listing-jameda", "requests GET", "Practitioner profile with practice name variant."),
 ("aerzte-de", "aerzte.de", "https://www.aerzte.de/ingelheim-am-rhein/rheinland-pfalz/heilpraktiker/coralie-suriyapperuma", "Praxis Coralie Suriyapperuma Heilpraktikerin", False, True, "06132/9723199", False, None, "EV-C-listing-aerzte-de", "requests GET", ""),
 ("mapquest-1", "MapQuest", "https://www.mapquest.com/de/rheinland-pfalz/suriya-praxis-804350293", "Suriya Praxis", False, True, "+49 6132 9795890", False, False, "EV-C-scrape-mapquest", "firecrawl_scrape", "Hours Mo 9-20, Di 10-20, Mi closed, Do/Fr 9-20, Sa 11-17. Data partly from Foursquare. 'Claim it' offered (unclaimed)."),
 ("mapquest-2", "MapQuest", "https://www.mapquest.com/de/naturheilpraxis-petra-nieen-717989239", "Ayurveda-Praxis Suriya", False, None, None, None, None, "EV-C-search-1", "firecrawl_search snippet", "Second MapQuest entry seen only as a name in a 'similar places' list. Entry page not opened."),
 ("xing", "XING", "https://www.xing.com/profile/Coralie_Suriyapperuma", "Coralie Suriyapperuma (person profile)", None, True, None, None, None, "EV-C-listing-xing", "requests GET", "Person profile, address Schützenpfad 29 shown. Not a business listing."),
 ("work5", "work5.de", "https://work5.de/kategorien/dienstleister/gesundheit-und-schoenheit/heilpraktiker", "Praxis Suriya - Ayurveda & Naturheilkunde", False, True, None, None, None, "EV-C-listing-work5", "requests GET", "BrightLocal campaign 994242 directory. Phone not shown on the list page."),
 ("11880", "11880", "https://www.11880.com/suche/heilpraktiker/heidesheim", "Praxis Suriya - Ayurveda & Naturheilkunde", False, True, None, None, None, "EV-C-search-1", "firecrawl_search snippet (listing page itself returned 403)", "BrightLocal campaign 994242 directory."),
 ("maptons", "maptons.com", "https://zw.maptons.com/p/3112170407", "Heilpraktiker Ingelheim I Praxis Suriya - Ayurveda & Naturheilkunde", False, None, None, None, None, "EV-C-search-2", "firecrawl_search snippet (page returned 403)", "Scraper copy of Cylex-style data. No edit route known."),
 ("branchen-info", "branchen-info.net", "https://ingelheim-am-rhein.branchen-info.net/schuetten-iris/3170134/", "Praxis Suriya für Naturheilkunde und Ayurveda", False, None, None, None, None, "EV-C-search-1", "firecrawl_search snippet (page: connection refused on direct GET)", "Different name form. Page unreadable in this run."),
]
listing_rows = []
for k, d, u, nf, nok, aok, pf, pok, hok, ev, how, note in L:
    fields = [x for x in (nok, aok, pok) if x is not None]
    strict = (nok is True and aok is True and pok is True)
    conflict = any(x is False for x in (nok, aok, pok, hok))
    listing_rows.append({"key": k, "directory": d, "url": u, "name_found": nf, "name_ok": nok, "address_ok": aok, "phone_found": pf, "phone_ok": pok, "hours_ok": hok,
                         "strict_match": strict, "has_conflict": conflict, "evidence_id": ev, "read_via": how, "note": note, "confidence": "verified" if how.startswith(("requests", "firecrawl_scrape")) else "derived"})
n = len(listing_rows)
strict_n = sum(1 for r in listing_rows if r["strict_match"])
noconf_n = sum(1 for r in listing_rows if not r["has_conflict"])
fieldstat = {
  "name": {"ok": sum(1 for r in listing_rows if r["name_ok"] is True), "of": sum(1 for r in listing_rows if r["name_ok"] is not None)},
  "address": {"ok": sum(1 for r in listing_rows if r["address_ok"] is True), "of": sum(1 for r in listing_rows if r["address_ok"] is not None)},
  "phone": {"ok": sum(1 for r in listing_rows if r["phone_ok"] is True), "of": sum(1 for r in listing_rows if r["phone_ok"] is not None)},
  "hours": {"ok": sum(1 for r in listing_rows if r["hours_ok"] is True), "of": sum(1 for r in listing_rows if r["hours_ok"] is not None)},
}
cit = J("evidence/area_c/EV-C-client-citations.json")
cit_live = [c for c in cit if c["status"] in ("live", "submitted")]
cit_with_url = [c for c in cit if c.get("listing_url")]
cit_live_nourl = [c for c in cit_live if not c.get("listing_url")]
nap_stats = {
  "definition": "NAP consistency percent = listings with name, address and phone identical to the master / listings checked (data-model.md section 8). 'strict' needs all three fields confirmed. Name 'Praxis Suriya' only; address Schützenpfad 29, 55218 Ingelheim; phone 0174 7411087.",
  "sample": "Live-read listings found by web search and direct fetch in this run (not the 10 BrightLocal-style top directories, because client_citations holds no listing_url for them).",
  "listings_checked": n, "strict_consistent": strict_n, "strict_percent": round(100 * strict_n / n, 1),
  "no_conflict_found": noconf_n, "no_conflict_percent": round(100 * noconf_n / n, 1),
  "field_level": fieldstat,
  "client_citations_table": {"rows_total": len(cit), "rows_live_or_submitted": len(cit_live), "rows_with_listing_url": len(cit_with_url), "live_rows_without_listing_url": len(cit_live_nourl),
                            "rows_with_nap_match_value": sum(1 for c in cit if c.get("nap_match") is not None),
                            "note": "30 of 31 'live' rows have no listing_url and no nap_match. The table cannot prove consistency. Only the Foursquare row (status planned) has a URL and its slug carries the old name."},
  "goyellow": "Listing returns HTTP 410. Excluded from the sample.",
  "collected_at": NOW
}

# ------------------------------------------------------------------ nap-corrections
corr = []
def add_corr(l, field, old, new, method, status="found"):
    corr.append({"directory": l["directory"], "url": l["url"], "field": field, "old_value": old, "correct_value": new, "method": method, "status": status, "last_checked": NOW, "evidence_id": l["evidence_id"]})
for l in listing_rows:
    if l["name_ok"] is False: add_corr(l, "name", l["name_found"], "Praxis Suriya", "client_login or directory change form (to be decided)")
    if l["phone_ok"] is False: add_corr(l, "phone", l["phone_found"], "0174 7411087", "client_login or directory change form (to be decided)")
    if l["hours_ok"] is False: add_corr(l, "hours", "see note", "Mo-Sa 07:30-20:00, So geschlossen", "client_login or directory change form (to be decided)")
for l in listing_rows:
    if l["key"] in ("cylex-duplicate", "infobel-2", "theralupa-11505", "mapquest-2"):
        add_corr(l, "duplicate_listing", l["name_found"], "merge into the main listing or delete (per-item go)", "directory removal request")
corr.append({"directory": "Foursquare", "url": "https://app.foursquare.com/v/praxis-suriya--ayurveda--naturheilkunde/6a8e87f2f8e415479c9380dd", "field": "name (URL slug shows old name)", "old_value": "Praxis Suriya - Ayurveda & Naturheilkunde", "correct_value": "Praxis Suriya", "method": "client_login", "status": "found", "last_checked": "2026-09-09 (client_citations.last_checked, not re-read in this run)", "evidence_id": "EV-C-client-citations"})
corr.append({"directory": "Google Business Profile", "url": "place_id ChIJCasDQHi-vUcR1iIwAQ6zUqI", "field": "name", "old_value": "Praxis Suriya - Ayurveda & Naturheilkunde (BASELINE-REPORT 30.09.; rename pending since 02.09., not approved)", "correct_value": "Praxis Suriya", "method": "client_login (GBP manager)", "status": "found", "last_checked": "2026-09-30 (baseline report, NOT re-read live: Local Falcon MCP not connected in this run)", "evidence_id": "EV-C-baseline-report-s11"})
nap_corr = {"run": "praxis-suriya-2026-10-11-dryrun", "master": "nap-master.json", "stats": nap_stats, "listings_checked": listing_rows, "corrections": corr, "collected_at": NOW}

# ------------------------------------------------------------------ Index-intended + classes
def clazz(path):
    p = path
    cls = None
    if p in ("/",): return ("money", "yes", "Startseite")
    money = {"/massage-ingelheim/", "/ayurveda-therapie/", "/ayurveda-ingelheim/", "/ganzheitliche-schmerztherapie/", "/suriya-neuro-migraene/"}
    if p in money: return ("money", "yes", "Hub/Money-Seite")
    system_no = {"/shop/": "leer, 77 Woerter alt", "/link-instagram/": "Linktree-Seite", "/termin-vereinbaren-direkt/": "Termin-Duplikat", "/contact-2/": "Kontakt-Duplikat", "/meinayurvedaangebot/": "Alt-Uebersicht",
                 "/login/": "Login-Seite", "/happy-health/": "Alt-Seite ohne Zweck", "/404-error-page/": "Soft-404-Seite", "/wpms-html-sitemap/": "HTML-Sitemap Plugin"}
    if p in system_no: return ("system", "no", system_no[p])
    if p in ("/praxis-fuer-naturheilkunde-ingelheim/", "/suriya-praxis-fuer-naturheilkunde-ingelheim/", "/darmgesundheit/", "/behandlungsangebot-2/"): return ("archive", "no", "Duplikat/Alt-Seite (10.10. Audit, Abschnitt E)")
    if p in ("/impressum/", "/datenschutzerklaerung/"): return ("system", "yes", "Pflichtseite, indexierbar ok")
    if p in ("/termin-buchen/", "/massage-buchen/", "/kosten-abrechnung/", "/heilpraktikerin-ingelheim/", "/behandlungsangebot/", "/ayurveda-fortbildung/"): return ("service", "yes", "Kontakt/Info/Ueber-mich")
    if re.match(r"^/(heilpraktiker|schmerztherapie|massage)-(mainz|wiesbaden)/", p): return ("location", "yes", "Stadtseite")
    if p.startswith("/category/") or re.match(r"^/\d{4}/\d{2}/", p) or "/page/" in p or p in ("/blog/2/", "/blog/3/"): return ("archive", "no", "Archiv: noindex vorgeschlagen")
    if p == "/blog/": return ("blog", "yes", "Blog-Uebersicht")
    if p in ("/1428/", "/1524/", "/1742-2/"): return ("blog", "review", "Alt-Beitrag mit Nummern-Slug, Entscheid durch Martin")
    pg = sm.get("https://suriya-praxis.de" + p)
    if pg and "post-sitemap.xml" in str([u["sitemap"] for u in []]): pass
    return (None, None, None)
post_urls = set(k for k, r in rows.items() if any(s.startswith("post-") for s in r["sitemap"]))
index_rows = []
def add_index(url, key, source):
    path = urllib.parse.urlparse(url).path
    c, i, note = clazz(path)
    if c is None:
        if key in post_urls: c, i, note = "blog", "yes", "Beitrag"
        else: c, i, note = "service", "yes", "Leistungsseite"
    ins = insp.get(url) or insp.get("https://suriya-praxis.de" + path)
    r = sm.get(url) or ex.get(url) or {}
    cov = None; indexed = "unknown"; isrc = "not inspected, no GSC impressions"
    if ins:
        cov = ins["response"].get("inspectionResult", {}).get("indexStatusResult", {}).get("coverageState")
        indexed = "yes" if cov == "Gesendet und indexiert" else "no"; isrc = "GSC URL Inspection API"
    elif gimpr(key) > 0:
        indexed = "yes"; isrc = f"derived: {gimpr(key)} impressions in GSC 90d (not inspected)"
    robots = (r.get("meta_robots") or "") + " " + (r.get("x_robots_tag") or "")
    status = r.get("final_status"); hops = r.get("redirect_hops", 0)
    indexable = (status == 200 and "noindex" not in robots.lower() and hops == 0)
    if i == "yes": verdict = "ok" if indexed == "yes" else ("index_missing" if indexed == "no" else "unverified")
    elif i == "no":
        if not indexable: verdict = "ok"
        elif indexed == "yes": verdict = "index_unwanted"
        elif indexed == "no": verdict = "ok"
        else: verdict = "unverified"
    else: verdict = "decision_needed"
    # exceptions
    action = "keep"
    if verdict == "index_missing": action = "investigate then request indexing (GSC UI); content 1,653 words, 19 content inbound links"
    if verdict == "index_unwanted": action = "noindex (page stays) or 301 / delete after go"
    if i == "no" and verdict == "ok" and status == 200 and indexable: action = "noindex or remove from sitemap"
    if i == "no" and key in rows and rows[key]["sitemap"] and verdict == "ok": action = "remove from sitemap; " + ("already not indexed" if indexed == "no" else "")
    index_rows.append({"url": url, "source": source, "http_status": status, "redirect_hops": hops, "final_url": r.get("final_url"), "meta_robots": r.get("meta_robots"), "in_sitemap": bool(rows.get(key, {}).get("sitemap")),
                       "indexed": indexed, "indexed_source": isrc, "coverage_state": cov, "gsc_clicks_90d": gclicks(key), "gsc_impressions_90d": gimpr(key),
                       "intended": i, "class": c, "class_note": note, "class_is": "PROPOSED", "verdict": verdict, "action": action})
for u in sm: add_index(u, canon_key(u), "sitemap")
sm_keys = {canon_key(u) for u in sm}
for u, r in ex.items():
    if r.get("source") in ("internal_link_not_in_sitemap", "gsc_page_not_in_sitemap") and canon_key(u) not in sm_keys:
        add_index(u, canon_key(u), r["source"])
# redirected / 404 rows verdict fix
for x in index_rows:
    if x["http_status"] == 404: x.update({"verdict": "ok", "action": "404 in GSC history; redirect to the corrected post (see redirect-map)", "intended": "no"})
    elif x["redirect_hops"] and x["source"] == "gsc_page_not_in_sitemap": x.update({"verdict": "ok", "action": "keep 301 (single hop)", "intended": "no", "class": "archive", "class_note": "old URL, redirects"})
    elif x["redirect_hops"] and x["in_sitemap"]: x.update({"verdict": "ok", "action": "remove from sitemap (URL answers 301)"})
vc = collections.Counter(x["verdict"] for x in index_rows)
index_doc = {"run": "praxis-suriya-2026-10-11-dryrun", "classes_are": "PROPOSED by agent from page type and the 10.10 audit; Martin decides.", "intended_values": "yes | no | review (review is an addition to the data-model: needs a human decision)",
             "verdict_values": "ok | index_missing | index_unwanted | unverified | decision_needed (the last two are additions: unverified = not inspected and no GSC signal)",
             "counts": dict(vc), "inspected_urls": len(insp), "rows": index_rows, "collected_at": NOW}
json.dump(index_doc, open(ROOT + "/index-intended.json", "w"), ensure_ascii=False, indent=1)

# ------------------------------------------------------------------ Link plan (inverted tree)
HOME = "/"
parent_map = {}
def setp(children, parent): 
    for c in children: parent_map[c] = parent
setp(["/migraene-analyse-ingelheim/", "/suriya-cranio-neuro-analyse/", "/suriya-migraene-kompass/", "/migraene-ist-oft-mehr-als-kopfschmerz/", "/nackenspannung-migraene/", "/ayurveda-bei-migraene-praxis-suriya-heilpraktikerin-ingelheim/",
      "/migraene-und-nackenverspannungen-verstehen-ursachen-ganzheitliche-behandlung-suriya-praxis/"], "/suriya-neuro-migraene/")
setp(["/nervenregulationsmassage/", "/craniosacrale-therapie/", "/hnc-human-neuro-cybrainetics/", "/thetahealing/", "/suriya-neuro-self-care/", "/nervenregulation-vagusnerv/", "/praxis-suriya-ingelheim-nervenregulation-vagusnerv-akupunktur-ayurveda/"], "/nervensystem-vagus-beruhigen/")
setp(["/nacken-schulter/", "/hexenschuss-ruecken/", "/frozen-shoulder/", "/kiefer-cmd/", "/akupunktur-ingelheim-praxis/", "/ohrakupunktur-ingelheim/", "/schroepftherapie-ingelheim/", "/lymphdrainage-lipoedem-ingelheim/", "/mikronaehrstoffe-hormone-wechseljahre/", "/schmerztherapie-mainz/", "/schmerztherapie-wiesbaden/"], "/ganzheitliche-schmerztherapie/")
setp(["/ayurveda-therapie/", "/ayurveda-regenerationstherapie-ingelheim/", "/ayurveda-beratung/", "/ayurveda-darm-test/", "/ayurveda-ausleitung-7-tage/", "/ayurveda-fortbildung/", "/5-ayurveda-rituale-fuer-den-winter-so-staerkst-du-dein-nervensystem-und-bleibst-warm/", "/ayurveda-kochworkshops-2026-im-hoefchen-stadecken-elsheim/"], "/ayurveda-ingelheim/")
setp(["/massage-mainz/", "/massage-wiesbaden/"], "/massage-ingelheim/")
setp(["/massage-mainz/ayurveda/"], "/massage-mainz/"); setp(["/massage-wiesbaden/ayurveda/"], "/massage-wiesbaden/")
setp(["/schmerztherapie-mainz/akupunktur/"], "/schmerztherapie-mainz/")
setp(["/heilpraktiker-mainz/", "/heilpraktiker-wiesbaden/", "/ganzheitliche-schmerztherapie/", "/suriya-neuro-migraene/", "/nervensystem-vagus-beruhigen/", "/ayurveda-ingelheim/", "/massage-ingelheim/", "/heilpraktikerin-ingelheim/", "/termin-buchen/", "/kosten-abrechnung/", "/blog/"], HOME)
setp(["/soulistic-reset-free5tage/", "/innere-arbeit-theta-healing-meditation/", "/allergiebehandlung/", "/darmgesundheit-2/", "/hormongesundheit/"], "/blog/")
def title_anchor(key):
    t = (rows[key]["title"] or "").split(" – ")[0].split(" | ")[0].split(" » ")[0].split(" - Praxis")[0].strip()
    return t
lp = []
UNTOUCH = "/ayurveda-therapie/"
for key, par in sorted(parent_map.items()):
    if key not in rows: continue
    r = rows[key]
    gp = parent_map.get(par, HOME if par != HOME else None)
    inb_content = r["inbound_content"]; outc = set(r["outbound_content"])
    missing = []
    if key != UNTOUCH:
        if par in rows and par not in outc: missing.append({"from": key, "to": par, "anchor_proposal": title_anchor(par), "why": "child links to its parent", "type": "child_to_parent"})
        if gp and gp != par and gp in rows and gp not in outc and key not in (HOME,) and par != HOME: pass
    pr = rows.get(par)
    if pr and par != UNTOUCH and key not in pr["outbound_content"]:
        missing.append({"from": par, "to": key, "anchor_proposal": title_anchor(key), "why": "parent lists its child", "type": "parent_to_child"})
    if key == UNTOUCH:
        missing = [{"from": par, "to": key, "anchor_proposal": "Ayurveda-Massage in Ingelheim", "why": "link TO the untouchable page only", "type": "parent_to_child"}] if key not in rows[par]["outbound_content"] else []
    lp.append({"page": key, "title": r["title"], "parent": par, "grandparent": gp, "inbound_content_links": len(inb_content), "inbound_content_from": inb_content, "outbound_content_links": len(outc),
               "outbound_to_parent": par in outc, "outbound_to_home": HOME in outc, "missing_links": missing, "do_not_edit_page": key == UNTOUCH, "gsc_clicks_90d": gclicks(key), "assignment": "PROPOSED (menu structure 29.09. + 10.10 audit); no new pages invented"})
# Home -> hubs (grandparent links)
home_out = set(rows["/"]["outbound_content"])
hub_missing = [{"from": "/", "to": h, "anchor_proposal": title_anchor(h), "why": "home links to every hub (grandparent level)"} for h in ["/suriya-neuro-migraene/", "/nervensystem-vagus-beruhigen/", "/ganzheitliche-schmerztherapie/", "/ayurveda-ingelheim/", "/massage-ingelheim/"] if h not in home_out]
link_plan = {"run": "praxis-suriya-2026-10-11-dryrun", "method": "Content links only (menu, footer and Enfold sidebar are stripped, as in the 10.10 audit). Parents come from the menu structure in memory suriya-elementor-dinakar-set (29.09.) and the audit. Anchors are derived from page titles and need a human edit.",
             "hard_rules": ["/ayurveda-therapie/ (WP 1511) is never edited, only linked to", "No menu change in this plan", "Every edit needs Martin's go, build/swap rules apply"],
             "pages": lp, "home_missing_links_to_hubs": hub_missing,
             "summary": {"pages_in_plan": len(lp), "pages_without_link_to_parent": sum(1 for x in lp if not x["outbound_to_parent"] and not x["do_not_edit_page"]), "pages_with_ge_1_missing_link": sum(1 for x in lp if x["missing_links"]),
                         "total_missing_links": sum(len(x["missing_links"]) for x in lp) + len(hub_missing)}, "collected_at": NOW}
json.dump(link_plan, open(ROOT + "/link-plan.json", "w"), ensure_ascii=False, indent=1)

# ------------------------------------------------------------------ Differences vs 10.10 audit (selected pages)
audit_inb = {"/massage-ingelheim/": 9, "/ayurveda-therapie/": 5, "/ayurveda-ingelheim/": 13, "/nervenregulationsmassage/": 5, "/ayurveda-regenerationstherapie-ingelheim/": 3, "/ayurveda-beratung/": 1, "/ayurveda-darm-test/": 1,
             "/suriya-neuro-migraene/": 11, "/suriya-cranio-neuro-analyse/": 7, "/migraene-analyse-ingelheim/": 3, "/suriya-migraene-kompass/": 3, "/suriya-neuro-self-care/": 3, "/akupunktur-ingelheim-praxis/": 13, "/ohrakupunktur-ingelheim/": 8,
             "/schroepftherapie-ingelheim/": 9, "/lymphdrainage-lipoedem-ingelheim/": 4, "/craniosacrale-therapie/": 5, "/hnc-human-neuro-cybrainetics/": 3, "/thetahealing/": 3, "/mikronaehrstoffe-hormone-wechseljahre/": 7,
             "/heilpraktiker-mainz/": 1, "/heilpraktiker-wiesbaden/": 1, "/massage-mainz/": 1, "/massage-wiesbaden/": 1, "/schmerztherapie-mainz/": 1, "/schmerztherapie-wiesbaden/": 1}
audit_diff = []
for k, v in audit_inb.items():
    live = len(rows[k]["inbound_content"]) if k in rows else None
    audit_diff.append({"page": k, "audit_10_10": v, "live_11_10": live, "differs": live != v})
live_vs_audit = {
 "sitemap_url_count": {"audit": 89, "live": f"{an['n_sitemap_entries']} entries / {an['n_sitemap_urls_unique']} unique (/darmgesundheit/ listed twice)"},
 "praxis-fuer-naturheilkunde-ingelheim": {"audit": "200, 1:1 copy of home, canonical -> /", "live": "301 -> / (one hop). Still listed in sitemap."},
 "massage-ingelheim": {"audit": "live hub, 1,421 words", "live": f"200, {rows['/massage-ingelheim/']['word_count']} words (counting rule differs: footer and sidebar removed here)"},
 "inbound_counts": audit_diff,
 "word_counts": "Word counts here exclude footer, header, nav and sidebar. They are lower than the 10.10 audit numbers by about 60 to 90 words per page."
}

# ------------------------------------------------------------------ Redirect map
rm = []
def rmrow(old, status_now, now_target, hops, kind, proposed_target, reason, approval="proposed", note=""):
    key = canon_key(old)
    rm.append({"old_url": old, "status_now": status_now, "now_redirects_to": now_target, "hops": hops, "kind": kind, "gsc_clicks_90d": gclicks(key), "gsc_impressions_90d": gimpr(key),
               "backlinks": "unknown (no per-URL data; site total 575 links / 430 domains, mostly spam, Ahrefs free 15.08. by Martin)", "target_url": proposed_target, "reason": reason, "type": 301 if proposed_target else None, "approval": approval, "note": note})
# existing redirects/404
for u, r in ex.items():
    if r.get("source") == "gsc_page_not_in_sitemap":
        if r["final_status"] == 404:
            rmrow(u, 404, None, 0, "404", "https://suriya-praxis.de/5-ayurveda-rituale-fuer-den-winter-so-staerkst-du-dein-nervensystem-und-bleibst-warm/", "typo slug (der instead of den) has 404 and appears in GSC with impressions; correct post exists", note="GSC page list shows this URL, see gsc_impressions_90d")
        else:
            rmrow(u, 301, r["final_url"], r["redirect_hops"], "existing_301", None, "existing single-hop 301, keep as is", approval="keep")
for u in ["https://suriya-praxis.de/praxis-fuer-naturheilkunde-ingelheim/"]:
    r = sm[u]; rmrow(u, 301, r["final_url"], r["redirect_hops"], "existing_301_in_sitemap", None, "answers 301 to / but is still in the sitemap (remove from sitemap). The 10.10 audit saw it as 200 with canonical to /, so the redirect is new.", approval="keep")
for u, r in ex.items():
    if r.get("source") == "probe" and r["redirect_hops"]:
        rmrow(u, 301, r["final_url"], r["redirect_hops"], "host/path normalisation", None, "host or path variant normalised by one 301 (good)", approval="keep")
rmrow("https://suriya-praxis.de/author/admin/", 404, None, 0, "404 probe", None, "probe only, 404 is correct (no author archive)", approval="keep")
# proposals from 10.10 audit section E (currently 200)
props = [("/darmgesundheit/", "/darmgesundheit-2/", "same title as /darmgesundheit-2/, 166 words, carries old phone 06132 9723199, listed twice in sitemap"),
         ("/contact-2/", "/termin-buchen/", "Kontakt duplicate (26 words). Keep form, phone and hours 1:1 on the target (memory suriya-conversion-paths-must-stay). Has 6 clicks."),
         ("/termin-vereinbaren-direkt/", "/termin-buchen/", "duplicate booking page"),
         ("/meinayurvedaangebot/", "/ayurveda-ingelheim/", "old overview, 48 words"),
         ("/suriya-praxis-fuer-naturheilkunde-ingelheim/", "/", "old home, 68 words"),
         ("/behandlungsangebot-2/", "/behandlungsangebot/", "duplicate of in-menu page (audit: merge decision is Martin's)"),
         ("/shop/", "/", "empty shop page (alternative: noindex)")]
for old, tgt, why in props:
    u = "https://suriya-praxis.de" + old; r = sm[u]
    rmrow(u, 200, None, 0, "proposed_new_301", "https://suriya-praxis.de" + tgt, why, note="from 10.10 audit section E, re-verified live: still HTTP 200")
rm_doc = {"run": "praxis-suriya-2026-10-11-dryrun", "backlink_data": "No per-URL backlink data. Only site totals from the Ahrefs free check on 15.08.2026 (575 backlinks, 430 linking domains, DR 5, 6% dofollow domains); Martin: mostly spam. No data bought.",
          "rows": rm, "counts": {"404": sum(1 for x in rm if x["status_now"] == 404), "existing_301": sum(1 for x in rm if x["kind"].startswith("existing") or x["kind"].startswith("host")), "proposed_new_301": sum(1 for x in rm if x["kind"] == "proposed_new_301")}, "collected_at": NOW}
json.dump(rm_doc, open(ROOT + "/redirect-map.json", "w"), ensure_ascii=False, indent=1)
json.dump(nap_master, open(ROOT + "/nap-master.json", "w"), ensure_ascii=False, indent=1)
json.dump(nap_corr, open(ROOT + "/nap-corrections.json", "w"), ensure_ascii=False, indent=1)

# save helper numbers for the register builder
nums = {"index_counts": dict(vc), "audit_diff": audit_diff, "live_vs_audit": live_vs_audit, "nap_stats": nap_stats}
json.dump(nums, open(ROOT + "/evidence/area_d/derived-numbers.json", "w"), ensure_ascii=False, indent=1)
print("index verdicts", dict(vc)); print("nap", nap_stats["listings_checked"], nap_stats["strict_consistent"], nap_stats["no_conflict_found"], nap_stats["field_level"])
print("link plan", link_plan["summary"]); print("redirect counts", rm_doc["counts"])
print("audit diffs", [(d["page"], d["audit_10_10"], d["live_11_10"]) for d in audit_diff if d["differs"]])
