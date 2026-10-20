"""D08/D09/D10/741: write evidence files for tool results that were read through Firecrawl (MCP) or from stored baseline files.
The Firecrawl results are copied from the tool responses of this session (no private data). Third-party forum content is NOT stored in bulk: notes only."""
import sys, os, json, shutil, re, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ub_lib import *

T = now()
# ---- D08 brand / person SERP (firecrawl_search, location Frankfurt) ----
serp = {
 "collected_at": T, "tool": "firecrawl_search (MCP), sources=[web], location=Frankfurt, Germany", "note": "Firecrawl web index is a proxy for Google, not the Google SERP itself.",
 "queries": {
  "\"Stürzl Steuerstrafrecht\" Erfahrungen Bewertung": [
   ["https://www.anwalt.de/kanzlei-stuerzl-steuerstrafrecht", "Kanzlei STÜRZL Steuerstrafrecht - Anwalt.de (Rating 5.0, 79)"],
   ["https://www.fachseminare-von-fuerstenberg.de/unternehmen/dozenten/dr-anja-stuerzl", "Dr. Anja Stürzl, LL.M. - Fachseminare von Fürstenberg"],
   ["https://www.stuerzl-steuerstrafrecht.de/index.php/steuerstrafrecht/gutachten-risikobewertung", "Gutachten & Risikobewertung - Stürzl Steuerstrafrecht"],
   ["https://www.lto.de/kanzleien-unternehmen/transfermarkt/detail/728", "Lea Wimmer wechselt zu Stürzl Steuerstrafrecht - LTO"],
   ["https://www.anwalt.de/anja-stuerzl", "Rechtsanwältin Dr. Anja Stürzl LL.M. - Anwalt.de (Rating 5.0, 55)"],
   ["https://www.stuerzl-steuerstrafrecht.de/index.php/steuerstrafrecht/selbstanzeige-korrekturberatung", "Selbstanzeige & Korrekturberatung - Stürzl Steuerstrafrecht"],
   ["https://www.fachseminare-von-fuerstenberg.de/zertifizierter-berater/zertifizierungslehrgang-steuerstrafrecht", "Zertifizierter Berater für Steuerstrafrecht (DAA)"],
   ["https://de.linkedin.com/company/kantenwein-spatscheck-widmayer-van-bevern-partner", "Kantenwein ... LinkedIn (mentions the firm)"],
   ["https://www.anwalt.de/verzeichnis/rechtsanwaelte.php?stadt=Linz_am_Rhein&thema=Steuerstrafrecht&cityid=3730", "anwalt.de directory Steuerstrafrecht (positive review excerpt)"],
   ["https://topanwalt.faz.net/Sonderbeilage-TOP-Anwalt-Wirtschaftsanwaelte-2027.pdf", "TOP Anwälte 2027 (FAZ supplement, mentions the firm)"]],
  "\"Anja Stürzl\" Rechtsanwältin": [
   ["https://www.stuerzl-steuerstrafrecht.de/index.php/dr-anja-stuerzl", "Dr. Anja Stürzl (own site)"],
   ["https://de.linkedin.com/in/dr-anja-st%C3%BCrzl-ll-m-a85934a5", "LinkedIn"],
   ["https://www.stuerzl-steuerstrafrecht.de/index.php/kanzlei", "Kanzlei (own site)"],
   ["https://www.fachseminare-von-fuerstenberg.de/unternehmen/dozenten/dr-anja-stuerzl", "Fürstenberg"],
   ["https://www.lto.de/kanzleien-unternehmen/transfermarkt/detail/198-dr-anja-stuerzl-wechselt-zu-stuerzl-steuerstrafrecht", "LTO"],
   ["https://www.anwalt.de/anja-stuerzl", "anwalt.de"],
   ["https://lrz.legal/de/dr-anja-stuerzl", "LRZ.legal"],
   ["https://www.stuerzl-steuerstrafrecht.de/", "own home"],
   ["https://anwalt-lotse.de/rechtsanwaeltin/anja-stuerzl-frankfurt-5vtd/", "Anwalt-Lotse (shows Oberanger 32 München and 069 number)"],
   ["https://www.anwalt.de/anja-stuerzl/bewertungen", "anwalt.de reviews"]],
  "\"Anja Stürzl\" AfD": [
   ["https://www.cicero.de/kultur/initiative-transparente-demokratie-ngo-finanzierung-sturzl-mansfeld", "Cicero: Initiative Transparente Demokratie (Stürzl named as lawyer and initiative member)"],
   ["https://www.landtag.nrw.de/portal/WWW/dokumentenarchiv/Dokument/MMA18-985.pdf", "Landtag NRW committee protocol (Stürzl heard as expert)"],
   ["https://de.wikipedia.org/wiki/Initiative_Transparente_Demokratie", "Wikipedia: Initiative Transparente Demokratie (Stürzl chair of founding board)"],
   ["https://www.welt.de/debatte/article256162448/ngos-die-neue-macht-im-staat-nicht-gewaehlt-nicht-reguliert-nicht-kontrolliert.html", "WELT guest article"],
   ["https://www.ardmediathek.de/video/ttt-titel-thesen-temperamente/wie-unabhaengig-sind-ngos-in-deutschland-eine-debatte-ueber-finanzierung-und-einfluss/ard/Y3JpZDovL2Rhc2Vyc3RlLmRlL3R0dCAtIHRpdGVsIHRoZXNlbiB0ZW1wZXJhbWVudGUvZTc0NTdhZDEtMTA3ZC00Njc1LTk3YWItM2VhOWMyOTQ1Mzdh", "ARD ttt (Stürzl speaks for the initiative)"],
   ["https://www.ruhrbarone.de/wer-kontrolliert-die-guten/246470/", "Ruhrbarone (board listed)"],
   ["https://www.transparente-demokratie.de/team", "initiative team page (Vorstandsvorsitzende)"]]
 },
 "reading": "No negative page-1 result for the firm name plus erfahrungen/bewertung in the top 10. The person-name query shows public reports about Dr. Stürzl's role in a civic NGO-transparency initiative; whether this is a reputation harm is a judgement for the client, not a scan finding."
}
save_evidence("EV-D-brand-serp", json.dumps(serp, ensure_ascii=False, indent=1), "json", "firecrawl_search (MCP)", "3 queries: firm name + erfahrungen bewertung; person name + Rechtsanwältin; person name + AfD", note="result titles and URLs only")

# ---- D08 forum thread: notes only ----
thread = {
 "collected_at": T, "urls_read_live": ["https://www.autoadmit.com/thread.php?thread_id=5856705&forum_id=2", "https://www.xoxohth.com/thread.php?thread_id=5856705&forum_id=2"],
 "tool": "firecrawl_scrape (MCP, maxAge 0). Direct curl to autoadmit.com timed out from this host (unreadable by curl).",
 "http_status_both": 200, "thread_title": "Rate this German tax lawyer - link", "same_thread_on_both_domains": True,
 "posts": 21, "first_post": "2026-04-13", "last_post": "2026-04-14", "anonymous_authors": True,
 "links_to_firm_site_in_thread": ["/index.php/kanzlei", "/index.php/dr-anja-stuerzl", "/index.php/lina (now 404)", "/images/2023/11/10/portrait_kanzlei2.jpg", "/images/layout/header-team-11.jpg"],
 "objective_points": {
   "mentions_firm_or_named_lawyers": True,
   "disparages": True,
   "kind": "appearance-based, sexualised and abusive remarks about the principal and other women of the team, plus some discriminatory remarks; no statement about legal work, clients, fees or cases",
   "criticises_professional_quality": False,
   "mentions_clients_or_cases": False },
 "stored_text": "NOT stored on purpose: third-party posts about named persons. This file holds reading notes only.",
 "ranking_check": "The thread did not appear in the top 10 of the brand queries (see EV-D-brand-serp); it appears only for a targeted query (firecrawl search 'autoadmit stuerzl-steuerstrafrecht.de')."
}
save_evidence("EV-D-forum-thread-notes", json.dumps(thread, ensure_ascii=False, indent=1), "json", "firecrawl_scrape (MCP) + firecrawl_search", "read thread_id=5856705 on both mirror domains, public, read only", note="notes only, no bulk copy")

# ---- D09 reviews ----
rev = {
 "collected_at": T, "tool": "firecrawl_scrape (MCP, format query = LLM extraction of the live page; numbers cross-checked with the search snippet 'Rating 5.0 (55)' and '(79)')",
 "anwalt_de_person_page": {"url": "https://www.anwalt.de/anja-stuerzl/bewertungen", "rating": 5.0, "reviews": 55, "star_distribution": {"5": 55, "4": 0, "3": 0, "2": 0, "1": 0},
    "visible_review_dates_10": ["2026-06-18", "2026-05-16", "2026-05-16", "2026-04-30", "2026-04-16", "2026-04-11", "2026-04-10", "2026-04-10", "2026-04-08", "2026-04-08"], "marked_removed_or_disputed": "none shown"},
 "anwalt_de_firm_page": {"url": "https://www.anwalt.de/kanzlei-stuerzl-steuerstrafrecht", "rating": 5.0, "reviews": 79, "latest_dates_visible": ["2026-06-18", "2026-05-17", "2026-05-17"],
    "address_shown": ["Wiesenhüttenstraße 17, 60329 Frankfurt am Main (OLD address)", "Oberanger 32, 80331 München"]},
 "objective_signals": {"one_star_reviews": 0, "same_day_pairs_in_10_visible_dates": 3, "five_reviews_within_4_days": "2026-04-08 to 2026-04-11 (5 of 10 visible)", "all_reviews_5_star": True},
 "limit": "Only 10 of 55 review dates are visible on the page. No review text and no reviewer names stored."
}
save_evidence("EV-D-anwaltde-reviews", json.dumps(rev, ensure_ascii=False, indent=1), "json", "firecrawl_scrape (MCP, query format)", "GET anwalt.de person reviews page and firm page; metadata only", note="no review text stored")
save_evidence("EV-D-gbp-reviews-unreadable", "UNREADABLE: the Google Business Profile review list of the Frankfurt profile (place id ChIJyVGAdikEaW8RUOWpEJs-2XA) and of the Munich profile cannot be read in this run.\n"
              "Reason: no Local Falcon MCP read tool is connected in this session, and the scan brief forbids browser automation and any Local Falcon scan.\n"
              "Known from stored data only (2026-10-01 baseline report): Frankfurt 5.0 stars / 14 reviews, Munich 5.0 stars / 1 review. Not re-verified.\n", "txt", "none (tool not available)", "n/a", note="source unreadable - not 'nothing found'")

# ---- D10 unlinked mention search ----
ms = {"collected_at": T, "tool": "firecrawl_search (MCP)", "found": {"JUVE": "https://www.juve.de/markt-und-management/bekannte-steuerstrafrechtlerin-von-rettenmaier-gruendet-eigene-boutique/",
      "ZRI": "https://www.zri-online.de/aktuell/stuerzl-steuerstrafrecht-eroeffnet-buero-in-muenchen-79764/", "LTO": "https://www.lto.de/kanzleien-unternehmen/transfermarkt/detail/198-dr-anja-stuerzl-wechselt-zu-stuerzl-steuerstrafrecht"}}
save_evidence("EV-D-mention-search", json.dumps(ms, ensure_ascii=False, indent=1), "json", "firecrawl_search (MCP)", "juve.de Stürzl Steuerstrafrecht; ZRI Stürzl Steuerstrafrecht; person query")

# ---- 741 review page ----
F = "/Users/martindrendel/741website/04_site/review/anja-stuerzl/index.html"
data = open(F, "rb").read()
lines = data.decode("utf-8", "replace").split("\n")
hit = []
for i, l in enumerate(lines, 1):
    for m in re.finditer(r"kein Profil auffindbar|München ohne Profil|Profil neu anlegen|München anlegen", l):
        s = max(0, m.start() - 90); e = min(len(l), m.end() + 90)
        hit.append(f"line {i}: ...{re.sub(chr(10),' ',l[s:e])}...")
txt = f"file: {F}\nsha256: {sha256(data)}\nread only, no edit\n\n" + "\n".join(hit) + "\n"
txt += "\nlive page https://741.studio/review/anja-stuerzl/ : HTTP 200, meta robots noindex,nofollow, the sentence 'kein Profil auffindbar' is present once (checked 2026-10-11).\n"
txt += "git: the local file is untracked (git status '??').\n"
save_evidence("EV-D-741-review-page", txt, "txt", "grep on local file + curl", f"grep {F}; curl https://741.studio/review/anja-stuerzl/")

# ---- stored baseline copies (derived, original date 2026-10-09) ----
B = "/Users/martindrendel/741website/00_project/assets/un-burning/stuerzl/baseline/"
for fn, eid in [("backlinks_summary.json", "EV-D-bl-summary"), ("bl_anchors.json", "EV-D-bl-anchors"), ("bl_refdomains.json", "EV-D-bl-refdomains"),
                ("disavow-liste-2026-10-09.md", "EV-D-disavow-liste"), ("disavow-stuerzl-2026-10-09.txt", "EV-D-disavow-file")]:
    ext = fn.rsplit(".", 1)[1]
    save_evidence(eid, open(B + fn, "rb").read(), ext, "stored file (DataForSEO Backlinks pull, 2026-10-09)", f"copy of baseline/{fn}", note="derived: stored data dated 2026-10-09, no new pull")
rd = {i["domain"]: i for i in json.load(open(B + "bl_refdomains.json"))[0]["items"]}
A = [l.split(":", 1)[1].strip() for l in open(B + "disavow-stuerzl-2026-10-09.txt").read().splitlines() if l.startswith("domain:")]
from collections import Counter
anch = json.load(open(B + "bl_anchors.json"))[0]["items"]
pbn = [a for a in anch if "PBN" in a["anchor"] or "Premium SEO" in a["anchor"]]
summ = {"source_date": "2026-10-09", "referring_domains_total": len(rd), "group_A_domains": len(A), "group_A_first_seen_by_month": dict(Counter(rd[d]["first_seen"][:7] for d in A)),
        "group_A_backlinks": sum(rd[d]["backlinks"] for d in A), "pbn_anchor_backlinks": sum(a["backlinks"] for a in pbn), "total_backlinks": 100,
        "group_C": {d: {"backlinks": rd[d]["backlinks"], "first_seen": rd[d]["first_seen"][:10], "spam_score": rd[d]["backlinks_spam_score"]} for d in ["autoadmit.com", "xoxohth.com", "bestattorneyusa.com", "bestattorneyus.com", "reimes-presseblick.blogspot.com", "gkwsaa.easypanel.host"]},
        "lina_url_anchor": [{"anchor": a["anchor"], "backlinks": a["backlinks"], "referring_domains": a["referring_domains"], "first_seen": a["first_seen"][:10]} for a in anch if a["anchor"].endswith("/index.php/lina")],
        "broken_backlinks_reported_by_pull": 0}
save_evidence("EV-D-bl-groups", json.dumps(summ, ensure_ascii=False, indent=1), "json", "python derivation from stored baseline files", "counts per disavow group, dated 2026-10-09", note="derived")
print(json.dumps(summ, ensure_ascii=False)[:900])
