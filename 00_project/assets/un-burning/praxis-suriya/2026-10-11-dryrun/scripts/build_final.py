import sys, json, os, collections, glob, subprocess
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ub_lib import ROOT, now, load_manifest, save_manifest, sha256
NOW = now()
R = json.load(open(ROOT + "/harm-register.json"))
items = R["items"]
# ---------------- bedrock (computed, per data-model section 7)
def is_open(i): return i["approval"] not in ("done", "rejected") and i["action"] != "keep"
areas = {}
for a in "ABCDE":
    its = [i for i in items if i["area"] == a]
    scanned = [i for i in its if i["approval"] != "blocked" or a != "A"]
    if a == "A" or not its: areas[a] = "grey"; continue
    op = [i for i in its if is_open(i)]
    if any(i["severity"] == "blocks_revenue" for i in op): areas[a] = "red"
    else:
        ll = [i for i in its if i["severity"] == "leaks_link_power"]
        lo = [i for i in ll if is_open(i)]
        areas[a] = "yellow" if ll and len(lo) / len(ll) > 0.10 else "green"
R["run"]["bedrock"] = {"areas": areas, "ready_for_growth": False,
                       "note": "Area A is grey: verify-only, role lists need a browser read. ready_for_growth is false because C is not green and A is unverified. Dry run: computed from proposed rows, no item is done."}
json.dump(R, open(ROOT + "/harm-register.json", "w"), ensure_ascii=False, indent=1)
# ---------------- who-owns-what
def row(asset, found, role741, status, ev, access=None, note=""):
    return {"asset": asset, "owner_expected": "client (Coralie Suriyapperuma); 741 = admin", "owner_found": found, "741_role": role741, "status": status, "evidence_ids": ev, "access_request": access, "confidence": "verified" if ev and status != "unknown" else "client_stated", "note": note, "collected_at": NOW}
wow = [
 row("domain_registrar", "unknown: DENIC and RDAP do not disclose the holder (entities list is empty)", "unknown", "unknown", ["EV-A-whois-www", "EV-A-rdap-denic"], "Coralie shows the registrar account or sends a DENIC web-whois screenshot", "Martin: every asset is already with the owner (client_stated)."),
 row("dns", "Cyon name servers ns1.cyon.ch, ns2.cyon.ch; SOA serial 2023050203; zone last changed 2023-05-04 (DENIC)", "unknown", "unconfirmed", ["EV-A-dig-ns", "EV-A-dig-soa", "EV-A-whois-www"], "Confirm the Cyon account holder in the browser"),
 row("hosting", "Cyon (A 149.126.4.112, rDNS s103.cyon.net), LiteSpeed cache header", "admin (Cyon access per memory)", "unconfirmed", ["EV-A-dig-a", "EV-A-headers-root"], "Confirm the Cyon account holder in the browser", "Mail MX is mail.suriya-praxis.de on Cyon; SPF include spf.protection.cyon.net."),
 row("cms", "WordPress (Enfold + Elementor); admin user list not read (no WordPress access used in this run)", "admin user 'Martin' (memory, not re-verified)", "unknown (needs browser read)", ["EV-M-praxis-suriya-client"], "Read Users list in wp-admin"),
 row("gbp", "unknown: owner and manager list needs a logged-in read. Place ID ChIJCasDQHi-vUcR1iIwAQ6zUqI", "manager 741studio18@gmail.com (memory, not re-verified)", "unknown (needs browser read)", ["EV-M-praxis-suriya-client"], "Read GBP > Settings > People and access"),
 row("ga4", "unknown (needs browser read)", "unknown", "unknown (needs browser read)", [], "Read GA4 > Admin > Access management"),
 row("gsc", "Service account reporting-bot@studio-apis-503306 has siteFullUser on https://suriya-praxis.de/ (verified). Owner list not readable via API.", "Full user (service account) and browser account 741studio18 (memory)", "unconfirmed", ["EV-E-gsc-sitemaps"], "Read Search Console > Settings > Users and permissions"),
 row("gtm", "unknown", "unknown", "unknown (needs browser read)", [], "Ask which GTM container, if any, the site uses"),
 row("ads", "unknown", "unknown", "unknown (needs browser read)", [], "Read Google Ads account access"),
 row("social:instagram", "Profile suriya.praxis exists (search result snippets). Other handles in use: coraliesuriyaperuma, suriyapraxis, suriya.ayurveda", "unknown", "unknown (needs browser read)", ["EV-C-search-1", "EV-D-page-suriya-praxis.de_impressum", "EV-C-scrape-cylex"], "Confirm which handle is the real one and who administers it"),
 row("social:facebook", "Profile facebook.com/coraliesuriyapperuma exists (search result). Other handles in use: hellotosuriyapperuma, naturheilpraxissuriya", "unknown", "unknown (needs browser read)", ["EV-C-search-1", "EV-D-page-suriya-praxis.de_impressum", "EV-C-scrape-cylex"], "Confirm which handle is the real one and who administers it"),
 row("social:linkedin", "Profile de.linkedin.com/in/coralie-suriyapperuma-coach exists (search result)", "unknown", "unknown (needs browser read)", ["EV-C-search-1"], None),
 row("listing:cylex", "Not claimed: page offers 'Eintrag uebernehmen' and 'Eintrag entfernen'", "none", "third_party", ["EV-C-scrape-cylex"], "Coralie claims the listing (email or phone verification at Cylex)", "Two entries exist (main + duplicate)."),
 row("listing:mapquest", "Not claimed: 'Claim it' offered", "none", "third_party", ["EV-C-scrape-mapquest"], "Coralie claims the listing"),
 row("listing:golocal", "Marked as user report ('Nutzermeldung - nicht von golocal geprueft'); claim state unknown", "unknown", "unknown", ["EV-C-listing-golocal"], "Check if a golocal account exists for Coralie"),
 row("listing:theralupa", "Two entries (10902, 11505); login owner unknown", "unknown", "unknown", ["EV-C-listing-theralupa-10902", "EV-C-listing-theralupa-11505"], "Coralie confirms which Theralupa login she has"),
 row("listing:wildcrumble_ug", "Related business, not harm: Wildcrumble UG (haftungsbeschraenkt), same address Schützenpfad 29 (Gebäude 44), same phone 0174 7411087, managing director Coralie Suriyapperuma", "none", "owned", ["EV-C-listing-wildcrumble-impressum"], None, "Shared phone and address with the practice. Needs no action. Note for NAP work: do not mix the two businesses in listings."),
]
json.dump({"run": "praxis-suriya-2026-10-11-dryrun", "rule": "100 percent client ownership, agency is admin. Statuses: owned, unconfirmed, third_party, unknown.", "assets": wow, "collected_at": NOW}, open(ROOT + "/who-owns-what.json", "w"), ensure_ascii=False, indent=1)
# ---------------- manifest: add output files
m = load_manifest()
m["outputs"] = []
for f in sorted(glob.glob(ROOT + "/*.json") + glob.glob(ROOT + "/*.md") + glob.glob(ROOT + "/scripts/*")):
    if os.path.basename(f) == "manifest.json" or os.path.isdir(f): continue
    b = open(f, "rb").read(); m["outputs"].append({"file": os.path.relpath(f, ROOT), "sha256": sha256(b), "bytes": len(b)})
m["generated_at"] = NOW
save_manifest(m)
print("bedrock", areas)
