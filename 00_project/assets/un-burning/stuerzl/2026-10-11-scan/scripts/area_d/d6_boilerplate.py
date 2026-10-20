"""D04: AI-slop / boilerplate heuristic. Repeated sentences across pages + generic phrase list. Heuristic only: HUMAN REVIEW, never judged."""
import sys, os, json, re
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ub_lib import *

crawl = json.load(open(os.path.join(EVID, "area_d", "EV-D-crawl-data.json"), encoding="utf-8"))["pages"]
pages = {}
for u, p in crawl.items():
    if p.get("final_status") == 200 and p.get("text") and p["final_url"] not in pages:
        pages[p["final_url"]] = p["text"]
sent_pages = defaultdict(set)
page_sents = {}
for u, t in pages.items():
    ss = [s.strip() for s in re.split(r"(?<=[.!?])\s+", t) if len(s.strip()) >= 40]
    page_sents[u] = ss
    for s in ss:
        sent_pages[s].add(u)
rep = {s: sorted(v) for s, v in sent_pages.items() if len(v) >= 4}
GENERIC = [r"maßgeschneidert\w*", r"individuell\w* lösung\w*", r"hand in hand", r"mit leidenschaft", r"ganzheitlich\w*", r"umfassend\w* (?:beratung|betreuung)", r"kompetent\w*", r"diskret\w*", r"auf augenhöhe", r"rundum", r"in der heutigen", r"tauchen sie ein", r"zögern sie nicht", r"jeder fall ist (?:anders|individuell)", r"vertrauensvoll\w*", r"engagiert\w*"]
GRX = [(g, re.compile(g, re.I)) for g in GENERIC]
per_page = []
for u, t in pages.items():
    ss = page_sents[u]
    shared = sum(1 for s in ss if len(sent_pages[s]) >= 2)
    gen = {g: len(rx.findall(t)) for g, rx in GRX}
    per_page.append({"page": u, "words": len(t.split()), "sentences_40plus": len(ss), "sentences_shared_with_other_page": shared,
                     "shared_share": round(shared / len(ss), 2) if ss else None, "generic_phrase_hits": {k: v for k, v in gen.items() if v}})
per_page.sort(key=lambda x: -(x["shared_share"] or 0))
out = {"collected_at": now(), "method": "sentences >=40 chars; shared = sentence text identical on >=2 pages; generic phrase regexes", "verdict": "needs human review - no judgement",
       "sentences_on_4plus_pages": [{"sentence": s[:200], "pages_n": len(v)} for s, v in sorted(rep.items(), key=lambda kv: -len(kv[1]))[:25]],
       "per_page": per_page}
print(len(rep), "sentences on >=4 pages")
for x in out["sentences_on_4plus_pages"][:8]:
    print(x["pages_n"], x["sentence"][:120])
for x in per_page[:12]:
    print(x["shared_share"], x["words"], x["page"][-70:], x["generic_phrase_hits"])
save_evidence("EV-D-boilerplate", json.dumps(out, ensure_ascii=False, indent=1), "json", "python heuristic on EV-D-crawl-data", "repeated-sentence share + generic phrase list", note="heuristic; human review always")
