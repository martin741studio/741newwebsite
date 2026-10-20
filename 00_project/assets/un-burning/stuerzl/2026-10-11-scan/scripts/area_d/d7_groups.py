"""Build EV-D-groups: URL lists per pattern (so the register can stay grouped). Derived from EV-D-analysis / EV-D-crawl-data."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ub_lib import *
a = json.load(open(os.path.join(EVID, "area_d", "EV-D-analysis.json"), encoding="utf-8"))
P = {k: r for k, r in a["pages"].items() if r.get("status") == 200}
P.pop("https://www.stuerzl-steuerstrafrecht.de", None)
def L(f): return sorted(k for k, r in P.items() if f(r))
g = {
 "collected_at": now(),
 "pages_200": len(P),
 "h1_two": L(lambda r: r["h1_count"] == 2),
 "h1_none": L(lambda r: r["h1_count"] == 0),
 "h1_many": L(lambda r: r["h1_count"] > 2),
 "service_area_pages": L(lambda r: r["type"] == "service_area"),
 "service_sub_pages": L(lambda r: r["type"] == "service_sub"),
 "thin_service_words": {k: r["word_count"] for k, r in P.items() if r["type"] in ("service_area", "service_sub")},
 "thin_team_bios_words": {k: r["word_count"] for k, r in P.items() if r["type"] == "team_bio"},
 "news_articles_words": {k: r["word_count"] for k, r in P.items() if r["type"] == "news_article"},
 "menu_only_pages": [{"url": k, "type": r["type"], "words": r["word_count"], "menu_inlinks": r["menu_in_n"], "content_inlinks": r["content_in_n"]} for k, r in P.items() if r["content_in_n"] == 0],
 "same_meta_description_pages": L(lambda r: (r.get("meta_description") or "").startswith("STÜRZL Steuerstrafrecht ist eine Kanzlei mit Spezialisierung")),
 "exact_text_duplicates": a["exact_text_dupes"],
 "near_duplicates_jaccard_ge_0_8": [d for d in a["dupes_ge_0_5"] if d["jaccard"] >= 0.8 and d["jaccard"] < 1.0],
 "similar_0_5_to_0_8_count": len([d for d in a["dupes_ge_0_5"] if 0.5 <= d["jaccard"] < 0.8]),
 "dead_internal_links": a["dead_internal_links"],
 "dead_links_note": "sources are the pages that carry the link",
}
from collections import Counter
print({k: (len(v) if isinstance(v, (list, dict)) else v) for k, v in g.items()})
print(Counter(r["word_count"] < 60 for r in P.values() if r["type"] == "news_article"), sorted(g["news_articles_words"].values()))
print(sorted(g["thin_team_bios_words"].values()), sorted(g["thin_service_words"].values()))
save_evidence("EV-D-groups", json.dumps(g, ensure_ascii=False, indent=1), "json", "python grouping of EV-D-analysis", "URL lists per pattern", note="derived from the live crawl of this run")
