"""EV-D-crawl-table: one CSV row per crawled URL (status, hops, final URL, canonical, robots, title, H1 count, words, content links out, inlinks)."""
import sys, os, json, csv, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ub_lib import *
a = json.load(open(os.path.join(EVID, "area_d", "EV-D-analysis.json"), encoding="utf-8"))["pages"]
buf = io.StringIO()
w = csv.writer(buf)
w.writerow(["url", "type", "status", "requested_as_n", "max_hops", "canonical", "canonical_is_self", "meta_robots", "title", "h1_count", "h2_count", "words", "content_links_out", "content_links_in", "menu_footer_links_in", "meta_description_len", "evidence_id"])
for k, r in sorted(a.items()):
    hops = max(x["hops"] for x in r["requested_as"])
    w.writerow([k, r.get("type"), r.get("status"), len(r["requested_as"]), hops, r.get("canonical"), (r.get("canonical") or "").rstrip("/") == k.rstrip("/") if r.get("canonical") else "", r.get("meta_robots"), r.get("title"), r.get("h1_count"), r.get("h2_count"), r.get("word_count"), r.get("content_out"), r.get("content_in_n"), r.get("menu_in_n"), len(r.get("meta_description") or ""), r.get("evidence_id")])
save_evidence("EV-D-crawl-table", buf.getvalue(), "csv", "python from EV-D-analysis", "table view of the live crawl", note="derived")
print(len(a), "rows")
