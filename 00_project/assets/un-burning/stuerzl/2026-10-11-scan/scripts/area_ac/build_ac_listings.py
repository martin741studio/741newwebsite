"""Builds the listing table and nap-corrections.json for areas C (STÜRZL). Pure data + arithmetic. No network."""
import json, os, sys
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ub_lib import RUN, now
NOW = now()
OLD = "Wiesenhüttenstraße 17, 60329 Frankfurt am Main"
NEW = "Untermainkai 26, 60329 Frankfurt am Main"
MUC = "Oberanger 32, 80331 München"
NAME = "STÜRZL Steuerstrafrecht"
PH_FFM = "+49 69 298028870"; PH_MUC = "+49 89 72444170"

def L(key, directory, url, kind, loc, name_found, name_ok, addr_found, addr_ok_prop, addr_ok_old, shows_old, phone_found, phone_ok, ev, via, note, conf="verified", hours=None, in_sample=True, claim=None, wrong_munich=False):
    strict_prop = bool(name_ok and addr_ok_prop and phone_ok)
    strict_old = bool(name_ok and addr_ok_old and phone_ok)
    return {"key":key,"directory":directory,"url":url,"kind":kind,"office":loc,"name_found":name_found,"name_ok":name_ok,
      "address_found":addr_found,"address_ok":addr_ok_prop,"address_ok_old_master":addr_ok_old,"shows_old_address":shows_old,
      "phone_found":phone_found,"phone_ok":phone_ok,"hours_found":hours,"hours_ok":None,
      "strict_match":strict_prop,"strict_match_old_master":strict_old,
      "has_conflict": not strict_prop, "evidence_id":ev,"read_via":via,"note":note,"confidence":conf,"in_sample":in_sample,"claim_state":claim}

rows = [
 L("anwalt-de-firm-ffm","anwalt.de (Kanzlei)","https://www.anwalt.de/kanzlei-stuerzl-steuerstrafrecht","business_listing","frankfurt","Kanzlei STÜRZL Steuerstrafrecht",False,OLD,False,True,True,"tel link +49 69 298028870 (display masked)",True,"EV-C-listing-anwalt-de-firm","firecrawl_scrape","Name carries the platform prefix 'Kanzlei' (platform convention). Hours Mo-Do 09:00-12:30 + 12:30-18:00, Fr 9:00-12:30 + 12:30-18:00. 5.0 with 79 reviews. Main lead channel per client.",hours="Mo-Fr 09:00-18:00",claim="profile content managed (uploads, reviews, legal tips); account holder unconfirmed"),
 L("anwalt-de-firm-muc","anwalt.de (Kanzlei, Standort München)","https://www.anwalt.de/kanzlei-stuerzl-steuerstrafrecht","business_listing","muenchen","Kanzlei STÜRZL Steuerstrafrecht",False,MUC,True,True,False,"+49 89 724... (masked, prefix only)",None,"EV-C-listing-anwalt-de-firm","firecrawl_scrape","Second location of the same profile. Phone digits masked, so the phone is not confirmed. No hours shown for München.",claim="see anwalt.de Kanzlei"),
 L("anwalt-de-anja","anwalt.de (Dr. Anja Stürzl)","https://www.anwalt.de/anja-stuerzl","person_profile","frankfurt","Dr. Anja Stürzl LL.M. (firm: Kanzlei STÜRZL Steuerstrafrecht)",False,OLD,False,True,True,"tel link +49 69 298028870 (display masked)",True,"EV-C-listing-anwalt-de-anja","firecrawl_scrape","Person profile, 5.0 with 55 reviews. Fachanwalt line names 'Rechtsanwaltskammer Köln' as issuing body (see item on RAK Köln).",hours="Mo-Fr 09:00-18:00"),
 L("anwalt-lotse-ffm","Anwalt-Lotse (mirror of BRAK directory)","https://anwalt-lotse.de/rechtsanwaeltin/anja-stuerzl-frankfurt-5vtd/","mirror_of_official_directory","frankfurt",NAME,True,"Wiesenhüttenstr. 17, 60329 Frankfurt",False,False,True,"069-298028870 (fax 069-298028879)",True,"EV-C-listing-anwalt-lotse-anja","firecrawl_scrape","Data 'aus dem amtlichen Verzeichnis der Bundesrechtsanwaltskammer', verified about 3 weeks before 2026-10-11, so before the move. Member of Rechtsanwaltskammer Frankfurt. Street written 'Wiesenhüttenstr.' (abbreviation)."),
 L("anwalt-lotse-muc","Anwalt-Lotse (BRAK Zweigstelle München)","https://anwalt-lotse.de/rechtsanwaeltin/anja-stuerzl-frankfurt-5vtd/","mirror_of_official_directory","muenchen","Dr. Anja Stürzl Rechtsanwältin",False,MUC,True,True,False,"089-72444170",True,"EV-C-listing-anwalt-lotse-anja","firecrawl_scrape","BRAK branch entry uses the person name by design ('Zweigstelle München')."),
 L("11880","11880","https://www.11880.com/branchenbuch/frankfurt-am-main/081314253B114102102/stuerzl-steuerstrafrecht.html","business_listing","frankfurt",NAME,True,"Wiesenhüttenstr. 17, 60329 Frankfurt (Gutleutviertel)",False,False,True,"(069) 298028870",True,"EV-C-listing-11880","firecrawl_scrape","Updated 2026-10-04, entry data of 2026-08-17. No hours. Service tag 'Drogenstrafrecht' is not on the firm's website. Button 'Änderungen vorschlagen'.",claim="not marked 'vom Inhaber bestätigt' on the page"),
 L("cylex-ffm","Cylex (Frankfurt)","https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-16927796.html","business_listing","frankfurt",NAME,True,OLD,False,True,True,"069 298028870",True,"EV-C-listing-cylex-ffm","firecrawl_scrape","Hours Mo-Fr 09:00-18:00 (last update 2026-04-16). Description text names 'Neuhauser Str. 3a, 80331 München' as the München address (wrong). Unclaimed ('Eintrag übernehmen').",hours="Mo-Fr 09:00-18:00",claim="unclaimed"),
 L("cylex-muc-ok","Cylex (München, Oberanger)","https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-17168776.html","business_listing","muenchen",NAME,True,MUC,True,True,False,"089 72444170",True,"EV-C-listing-cylex-muc-ok","firecrawl_scrape","Correct entry for the second office. No category. Last update 2026-05-18. Unclaimed.",claim="unclaimed"),
 L("cylex-muc-wrong","Cylex (München, Neuhauser Str.)","https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-17045957.html","business_listing","muenchen",NAME,True,"Neuhauser Str. 3a, 80331 München",False,False,False,"089 72444170",True,"EV-C-listing-cylex-muc-wrong","firecrawl_scrape","Second Cylex entry for the same office with another firm's street address (Neuhauser Straße 3a is the address of Dr. Rose Rechtsanwälte, see EV-C-search-4b). Category 'Software Hersteller'. Unclaimed.",claim="unclaimed"),
 L("rechtecheck-ffm","rechtecheck.de (Frankfurt)","https://rechtecheck.de/anwalt/frankfurt/anja-stuerzl/","business_listing","frankfurt",NAME,True,"Wiesenhüttenstr. 17, 60329 Frankfurt",False,False,True,None,None,"EV-C-listing-rechtecheck-frankfurt","firecrawl_scrape","HTML title and active filter say 'Frankfurt (Oder)'. No phone shown. 'Daten aktualisieren' offered.",claim="unclaimed ('Sind Sie Anja Stürzl?')"),
 L("rechtecheck-muc","rechtecheck.de (München)","https://rechtecheck.de/anwalt/muenchen/kanzlei/kanzlei-stuerzl-steuerstrafrecht/","business_listing","muenchen","Kanzlei STÜRZL Steuerstrafrecht",False,"Neuhauser Str. 3a, 80331 München",False,False,False,None,None,"EV-C-listing-rechtecheck-muenchen","firecrawl_scrape","Wrong street (another firm's address). No phone. Lists Lea Wimmer as the lawyer.",claim="unclaimed"),
 L("bestattorneyusa-anja","bestattorneyusa.com (Anja Stürzl)","https://bestattorneyusa.com/attorneys/anja-sturzl-tucson-20528","auto_generated_profile","frankfurt","Anja Stürzl",False,"Wiesenhüttenstraße 17 Frankfurt/Main DE (page title says 'Tucson')",False,False,True,None,None,"EV-C-bestattorneyusa-anja","curl","Auto-generated US directory profile: city label Tucson, rating 4.0 (1 review) with a review text of unknown origin, award text with years. 'Claim this profile' offered. Not opened by the firm.",claim="unclaimed"),
 L("bestattorneyusa-lea","bestattorneyusa.com (Lea Wimmer)","https://bestattorneyusa.com/attorneys/lea-wimmer-boston-5898","auto_generated_profile","muenchen","Lea Wimmer",False,"Neuhauserstraße 3a Munich DE (page title says 'Boston')",False,False,False,None,None,"EV-C-bestattorneyusa-lea","curl","Auto-generated US directory profile: city label Boston, wrong Munich street, rating 4.0 (1 review). 'Claim this profile' offered.",claim="unclaimed"),
]

derived = [
 L("infobel","Infobel","https://www.infobel.com/de/germany/sturzl_steuerstrafrecht/frankfurt_oder/DE109851584-069298028870/businessdetails.aspx","business_listing","frankfurt",NAME,True,"Wiesenhüttenstraße 17 60329 Frankfurt (Oder)",False,False,True,"069298028870 (in URL)",True,"EV-C-listing-infobel","firecrawl_search snippet (page behind captcha)","City 'Frankfurt (Oder)' is wrong (the firm is in Frankfurt am Main). Page itself unreadable.",conf="derived",in_sample=False),
 L("maptons","maptons.com (scraper copy, 8+ language subdomains)","https://de.maptons.com/p/3302892716","scraper","frankfurt",NAME,True,"Wiesenhüttenstraße 17",False,False,True,"+49 69 298028870",True,"EV-C-search-misc","firecrawl_search snippet (HTTP 403 to curl)","Copy of map data with page time stamps 2026-07-12 to 2026-09-13. No edit route known.",conf="derived",in_sample=False),
 L("linkedin-company","LinkedIn company page","https://de.linkedin.com/company/stuerzl-steuerstrafrecht","social","frankfurt",NAME,True,"Wiesenhüttenstraße 17, Frankfurt, Hessen 60329, DE (primary location)",False,False,True,None,None,"EV-C-search-misc","firecrawl_search snippet (scrape not supported)","716 followers. München location not visible in the snippet. Admin unknown.",conf="derived",in_sample=False),
 L("juwist","JuWiSt e.V. member list","https://juwist.com/mitgliederliste/","third_party_member_list","frankfurt","STÜRZL Steuerstrafrecht",True,"Wiesenhüttenstraße 17 60329 Frankfurt am Main",False,True,True,None,None,"EV-C-search-misc","firecrawl_search snippet","Association list, edited by the association. Firm cannot edit directly.",conf="derived",in_sample=False),
 L("creditreform","Creditreform firm database","https://firmeneintrag.creditreform.de/60329/6070874119/DR_ANJA_STUERZL_STUERZL_STEUERSTRAFRECHT","business_listing","frankfurt","Dr. Anja Stürzl, STÜRZL Steuerstrafrecht",False,"60329 Frankfurt (street not in snippet)",None,None,None,None,None,"EV-C-search-misc","firecrawl_search snippet","Street not visible in the snippet; page not opened.",conf="derived",in_sample=False),
 L("anwalt-de-lea","anwalt.de (Lea Wimmer)","https://www.anwalt.de/lea-wimmer-2","person_profile","muenchen","Lea Wimmer",False,MUC,True,True,False,"+49 89 724... (masked)",None,"EV-C-search-misc","firecrawl_search snippet","5.0 with 23 reviews. Address matches the second office.",conf="derived",in_sample=False),
 L("anwaltauskunft-wimmer","Deutsche Anwaltauskunft (Lea Wimmer)","https://anwaltauskunft.de/rechtsanwalt/wimmer-287f04ca/","person_profile","muenchen",NAME,True,MUC,True,True,False,"+49 (89) 7244 41 70",True,"EV-C-search-misc","firecrawl_search snippet","Address and phone match the second office (phone with different spacing).",conf="derived",in_sample=False),
 L("bestlawyers","Best Lawyers (firm page)","https://www.bestlawyers.com/firms/sturzl-steuerstrafrecht/104283/DE","business_listing","frankfurt",NAME,True,"city level only: Frankfurt/Main and Munich",None,None,None,None,None,"EV-C-listing-bestlawyers","firecrawl_scrape","Read live, but shows no street and no phone. Both lawyer profiles are 'Unactivated'.",conf="verified",in_sample=False),
]

def pct(n, d): return round(100.0*n/d, 1) if d else None
S = rows
n = len(S)
def cnt(f): return sum(1 for r in S if f(r))
def addr_phone_prop(r): return bool(r["address_ok"] and r["phone_ok"])
def addr_phone_old(r): return bool(r["address_ok_old_master"] and r["phone_ok"])
def loose_old(r): return bool(r["phone_ok"] and (r["address_ok_old_master"] or r["shows_old_address"] or (r["office"]=="muenchen" and r["address_ok"])))
stats = {
 "definition": "NAP consistency percent = listings with name, address and phone identical to the master / listings checked (data-model.md section 8). 'strict' needs all three fields confirmed (a masked or missing phone counts as not confirmed). Character-exact: 'Wiesenhüttenstr.' differs from 'Wiesenhüttenstraße'; a platform prefix 'Kanzlei' differs from the master name. Phone compared as digits (format differences are noted, not counted).",
 "masters_compared": {"proposed": {"name": NAME, "frankfurt": NEW, "muenchen": MUC, "phone_ffm": PH_FFM, "phone_muc": PH_MUC, "locked": False},
                       "old": {"name": NAME, "frankfurt": OLD, "muenchen": MUC, "phone_ffm": PH_FFM, "phone_muc": PH_MUC, "note": "valid until 2026-10-05"}},
 "sample": "13 external listing rows whose address was read live in this run (anwalt.de x3 rows, BRAK mirror x2 rows, 11880, Cylex x3, rechtecheck x2, bestattorneyusa x2). Derived rows (search snippets) and sources without address are listed but not counted.",
 "listings_checked": n,
 "against_proposed_master": {"strict_consistent": cnt(lambda r:r["strict_match"]), "strict_percent": pct(cnt(lambda r:r["strict_match"]),n),
                             "address_and_phone_only_consistent": cnt(addr_phone_prop), "address_and_phone_only_percent": pct(cnt(addr_phone_prop),n),
                             "note": "No Frankfurt listing shows Untermainkai 26. Only München entries can match."},
 "against_old_master": {"strict_consistent": cnt(lambda r:r["strict_match_old_master"]), "strict_percent": pct(cnt(lambda r:r["strict_match_old_master"]),n),
                        "address_and_phone_only_consistent": cnt(addr_phone_old), "address_and_phone_only_percent": pct(cnt(addr_phone_old),n),
                        "loose_old_address_in_any_form_and_phone": cnt(loose_old), "loose_percent": pct(cnt(loose_old),n),
                        "note": "The old master is the state before the move of 2026-10-05; shown for the re-scan comparison."},
 "shows_old_address": {"count": cnt(lambda r:r["shows_old_address"]), "of": n, "rows": [r["key"] for r in S if r["shows_old_address"]]},
 "wrong_other_than_move": {"rows": ["cylex-muc-wrong","rechtecheck-muc","bestattorneyusa-lea","rechtecheck-ffm (city label Oder)","infobel (city Oder, derived)","cylex-ffm (description names Neuhauser Str. 3a)"]},
 "by_office": {"frankfurt": {"rows": cnt(lambda r:r["office"]=="frankfurt"), "old_address_shown": cnt(lambda r:r["office"]=="frankfurt" and r["shows_old_address"])},
               "muenchen": {"rows": cnt(lambda r:r["office"]=="muenchen"), "street_correct": cnt(lambda r:r["office"]=="muenchen" and r["address_ok"])}},
 "field_level": {"name": {"ok": cnt(lambda r:r["name_ok"]), "of": n},
                 "address_proposed": {"ok": cnt(lambda r:r["address_ok"]), "of": n},
                 "address_old": {"ok": cnt(lambda r:r["address_ok_old_master"]), "of": n},
                 "phone": {"ok": cnt(lambda r:r["phone_ok"] is True), "of": cnt(lambda r:r["phone_ok"] is not None), "not_shown_or_masked": cnt(lambda r:r["phone_ok"] is None)}},
 "client_citations_table": {"rows_total_for_client": 0, "note": "client_citations holds 0 rows for this client (Citations module not started). client_locations holds 0 rows; the portal table 'locations' holds 1 row (Frankfurt, old address, phone empty, hours empty, no München)."},
 "not_in_sample": {"gelbe_seiten": "0 hits (live search page)", "das_oertliche": "no exact entry (live search page)", "yelp": "unreadable (JavaScript page, scrape not supported)", "bing_places": "not publicly readable", "apple_maps": "not publicly readable", "rak_frankfurt_brak": "official site not read; BRAK data seen through the Anwalt-Lotse mirror", "bestattorneyus_com": "no profile at the slugs of the .com twin (404); search parameter ignored by that site", "juve": "ranking mentions 'Stürzl, Frankfurt' (name only), no firm profile"},
 "collected_at": NOW,
}

# corrections: one row per wrong field. correct_value for the move rows is the PROPOSED, NOT LOCKED address.
BLOCK = "wait for NAP lock (Martin + client confirm Untermainkai 26)"
def C(directory, url, field, old, correct, method, ev, status="found", note="", blocked=False, severity=None, destructive=False):
    d = {"directory":directory,"url":url,"field":field,"old_value":old,"correct_value":correct,"method":method,"status":status,"last_checked":NOW,"evidence_id":ev}
    if blocked: d["blocked_until"] = BLOCK
    if severity: d["severity"] = severity
    if note: d["note"] = note
    d["destructive"] = destructive
    return d
CORR = []
move = "Untermainkai 26, 60329 Frankfurt am Main (PROPOSED, master not locked)"
CORR += [
 C("anwalt.de (Kanzlei)","https://www.anwalt.de/kanzlei-stuerzl-steuerstrafrecht","address (Standort Frankfurt)",OLD,move,"client_login","EV-C-listing-anwalt-de-firm",blocked=True,severity="blocks_revenue"),
 C("anwalt.de (Dr. Anja Stürzl)","https://www.anwalt.de/anja-stuerzl","address",OLD,move,"client_login","EV-C-listing-anwalt-de-anja",blocked=True,severity="blocks_revenue"),
 C("anwalt.de (Kanzlei + Anja)","https://www.anwalt.de/kanzlei-stuerzl-steuerstrafrecht","hours","Mo-Fr 09:00-18:00","binding hours from the client (open question: office hours vs phone hours 09:30-14:30)","client_login","EV-C-listing-anwalt-de-firm",blocked=True,severity="cosmetic",note="Hours are not part of the provisional master."),
 C("Rechtsanwaltskammer Frankfurt / BRAK directory","https://anwalt-lotse.de/rechtsanwaeltin/anja-stuerzl-frankfurt-5vtd/ (mirror)","address (Kanzlei Frankfurt)","Wiesenhüttenstr. 17, 60329 Frankfurt",move,"client_login (lawyer reports the change to the chamber; official directory not read)","EV-C-listing-anwalt-lotse-anja",blocked=True,severity="blocks_revenue",note="Mirror data is about 3 weeks old. The official directory must be checked after the lawyer files the change."),
 C("11880","https://www.11880.com/branchenbuch/frankfurt-am-main/081314253B114102102/stuerzl-steuerstrafrecht.html","address","Wiesenhüttenstr. 17, 60329 Frankfurt (Gutleutviertel)",move,"directory change form ('Änderungen vorschlagen')","EV-C-listing-11880",blocked=True,severity="leaks_link_power"),
 C("Cylex (Frankfurt)","https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-16927796.html","address",OLD,move,"claim listing, then change form","EV-C-listing-cylex-ffm",blocked=True,severity="leaks_link_power"),
 C("Cylex (Frankfurt)","https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-16927796.html","description (München address)","Neuhauser Str. 3a 80331 München in the description","Oberanger 32, 80331 München","claim listing, then change form","EV-C-listing-cylex-ffm",severity="leaks_link_power",note="Not a move record: wrong already before the move."),
 C("Cylex (Frankfurt)","https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-16927796.html","hours","Mo-Fr 09:00-18:00","binding hours from the client","claim listing, then change form","EV-C-listing-cylex-ffm",blocked=True,severity="cosmetic"),
 C("Cylex (München, Neuhauser Str.)","https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-17045957.html","duplicate_listing_wrong_address","Neuhauser Str. 3a, 80331 München; category Software Hersteller","remove entry (duplicate of Cylex 17168776, Oberanger 32)","directory removal request ('Eintrag entfernen') after claim","EV-C-listing-cylex-muc-wrong",severity="leaks_link_power",destructive=True,note="Per-item go needed. The München office itself is NOT a duplicate; only this second Cylex entry is."),
 C("Cylex (München, Oberanger)","https://web2.cylex.de/firma-home/stuerzl-steuerstrafrecht-17168776.html","category","(none)","Rechtsanwälte","claim listing, then change form","EV-C-listing-cylex-muc-ok",severity="cosmetic"),
 C("rechtecheck.de (München)","https://rechtecheck.de/anwalt/muenchen/kanzlei/kanzlei-stuerzl-steuerstrafrecht/","address","Neuhauser Str. 3a, 80331 München",MUC,"directory update form ('Daten aktualisieren')","EV-C-listing-rechtecheck-muenchen",severity="leaks_link_power"),
 C("rechtecheck.de (Frankfurt)","https://rechtecheck.de/anwalt/frankfurt/anja-stuerzl/","city label","Frankfurt (Oder)","Frankfurt am Main","directory update form ('Daten aktualisieren')","EV-C-listing-rechtecheck-frankfurt",severity="leaks_link_power"),
 C("rechtecheck.de (Frankfurt)","https://rechtecheck.de/anwalt/frankfurt/anja-stuerzl/","address","Wiesenhüttenstr. 17, 60329 Frankfurt",move,"directory update form ('Daten aktualisieren')","EV-C-listing-rechtecheck-frankfurt",blocked=True,severity="leaks_link_power"),
 C("Infobel","https://www.infobel.com/de/germany/sturzl_steuerstrafrecht/frankfurt_oder/DE109851584-069298028870/businessdetails.aspx","city","Frankfurt (Oder)","Frankfurt am Main","Infobel change request (route not checked: page behind captcha)","EV-C-listing-infobel",severity="leaks_link_power",note="derived from a search snippet of 2026-10-11"),
 C("Infobel","https://www.infobel.com/de/germany/sturzl_steuerstrafrecht/frankfurt_oder/DE109851584-069298028870/businessdetails.aspx","address","Wiesenhüttenstraße 17 60329 Frankfurt (Oder)",move,"Infobel change request","EV-C-listing-infobel",blocked=True,severity="leaks_link_power"),
 C("LinkedIn company page","https://de.linkedin.com/company/stuerzl-steuerstrafrecht","address (primary location)","Wiesenhüttenstraße 17, Frankfurt, Hessen 60329",move,"client_login (page admin)","EV-C-search-misc",blocked=True,severity="cosmetic",note="derived from a search snippet of 2026-10-11"),
 C("JuWiSt e.V. member list","https://juwist.com/mitgliederliste/","address","Wiesenhüttenstraße 17 60329 Frankfurt am Main",move,"member asks the association","EV-C-search-misc",blocked=True,severity="cosmetic",note="derived from a search snippet of 2026-10-11"),
 C("maptons.com (scraper)","https://de.maptons.com/p/3302892716","address","Wiesenhüttenstraße 17",move,"none (no edit route; follows the source data)","EV-C-search-misc",blocked=True,severity="cosmetic",status="found",note="No action of its own: re-check after GBP and the main directories are corrected."),
 C("bestattorneyusa.com (Anja Stürzl)","https://bestattorneyusa.com/attorneys/anja-sturzl-tucson-20528","city / profile","Tucson; Wiesenhüttenstraße 17 Frankfurt/Main; 1 review of unknown origin","claim the profile and correct the city and address, or request removal","claim ('Claim Profile') by the lawyer; removal request only if the claim fails","EV-C-bestattorneyusa-anja",severity="cosmetic",note="Auto-generated. Per-item go before any removal request."),
 C("bestattorneyusa.com (Lea Wimmer)","https://bestattorneyusa.com/attorneys/lea-wimmer-boston-5898","city / address","Boston; Neuhauserstraße 3a Munich DE","claim the profile and correct city and address (Oberanger 32, 80331 München), or request removal","claim ('Claim Profile') by the lawyer; removal request only if the claim fails","EV-C-bestattorneyusa-lea",severity="cosmetic",note="Auto-generated. Per-item go before any removal request."),
 C("Google Business Profile Frankfurt","place_id ChIJyVGAdikEaW8RUOWpEJs-2XA","address","Wiesenhüttenstraße 17 (not changed yet per file of 2026-10-07; live profile NOT read in this run)",move,"client_login / manager role (GBP)","EV-C-gbp-stored-2026-10-01",blocked=True,severity="blocks_revenue",status="found",note="An address change can trigger re-verification; plan video verification first."),
 C("Own website (Impressum, Kontakt, footer on 13 pages, JSON-LD)","https://www.stuerzl-steuerstrafrecht.de/","address, schema address and geo","Wiesenhüttenstraße 17, 60329 Frankfurt am Main; geo 50.104409, 8.66711",move+"; new geo coordinates","Joomla Super User (741 account is only Administrator)","EV-C-site-analysis",blocked=True,severity="blocks_revenue"),
]
out = {"run":"stuerzl-2026-10-11-scan","master":"nap-master.json (provisional, locked=false)","stats":stats,"listings_checked":S,
       "derived_or_partial_not_counted":derived,
       "own_website_rows":[
        {"key":"site-impressum","url":"https://www.stuerzl-steuerstrafrecht.de/index.php/impressum","address_found":OLD,"shows_old_address":True,"address_ok":False,"phone_found":"+49 69 29 80 28 87-0 (Fax -9)","phone_ok":True,"hours_found":None,"munich_in_body":False,"evidence_id":"EV-C-site-impressum","confidence":"verified","note":"Impressum body names Frankfurt only; München appears only in the footer line."},
        {"key":"site-kontakt","url":"https://www.stuerzl-steuerstrafrecht.de/index.php/kontakt","address_found":OLD+" (Frankfurt); "+MUC+" (München)","shows_old_address":True,"address_ok":False,"phone_found":"+49 69 29 80 28 87-0 / +49 89 72 44 41 7-0","phone_ok":True,"hours_found":"Mo-Fr 09:30-14:30 (both offices)","evidence_id":"EV-C-site-kontakt","confidence":"verified","note":"Directions text sends visitors to Wiesenhüttenstraße; parking 'im Hof'. 2 emergency mobile numbers shown."},
        {"key":"site-footer-13-pages","url":"13 pages, see EV-C-site-analysis","address_found":OLD+" | "+MUC,"shows_old_address":True,"address_ok":False,"phone_found":"069 29802887-0","phone_ok":True,"evidence_id":"EV-C-site-analysis","confidence":"verified","note":"13 of 13 sampled pages show the old address in the footer. 0 pages show Untermainkai."},
        {"key":"site-jsonld","url":"13 pages, one identical LegalService block","address_found":OLD,"shows_old_address":True,"address_ok":False,"phone_found":"+49-69-298028870","phone_ok":True,"hours_found":"Mo-Fr 09:00-18:00","evidence_id":"EV-C-site-analysis","confidence":"verified","note":"No München entity. geo 50.104409, 8.66711 (old building). sameAs: LinkedIn only."}],
       "corrections":CORR,"collected_at":NOW}
json.dump(out, open(os.path.join(RUN,"nap-corrections.json"),"w"), indent=1, ensure_ascii=False)
print(json.dumps(stats, indent=1, ensure_ascii=False)[:3500]); print(len(CORR),"corrections")
