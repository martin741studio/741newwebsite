"""D11: advertising-law text scan (BRAO/BORA/UWG hints). Hits only. No legal judgement. Uses the crawl text of all pages."""
import sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ub_lib import *

crawl = json.load(open(os.path.join(EVID, "area_d", "EV-D-crawl-data.json"), encoding="utf-8"))["pages"]
PATTERNS = [
    ("superlative", r"\b(beste[rnms]?|besten|führend\w*|marktführer\w*|nummer\s?1|top[- ]?(?:anwalt|anwältin|kanzlei)\w*|einzigartig\w*|unübertroffen\w*|hochspezialisiert\w*|renommiert\w*|bestens)\b"),
    ("expert_specialist", r"\b(experte[n]?|expertin(?:nen)?|expertise|spezialist\w*|spezialisiert\w*|spezialisierung)\b"),
    ("guarantee_success", r"\b(garantier\w*|erfolgreich\w*|erfolgsquote\w*|erfolgsgarantie|erfolg(?:e|en)?\b|100\s?%|straffrei\w*|straflos\w*|sicher(?:lich)?\s+(?:vermeiden|straffrei))"),
    ("title_fachanwalt", r"\b(fachanwalt\w*|fachanwält\w*|fachanwaltschaft|fachanwaltstitel)\b"),
    ("title_strafverteidiger", r"\b(strafverteidig\w*)\b"),
    ("title_other", r"(zertifizierte[rn]? berater\w*(?: für [A-Za-zäöüß]+)?|\(DAA\)|\bLL\.\s?M\.|tätigkeitsschwerpunkt\w*|interessenschwerpunkt\w*|schwerpunkt\w*)"),
    ("ranking_award", r"\b(juve|handelsblatt|wirtschaftswoche|best lawyers|top[- ]?anwält\w*|ranking\w*|ausgezeichnet\w*|auszeichnung\w*|empfohlen\w*|leading|chambers|legal 500)\b"),
]
RX = [(k, re.compile(p, re.I)) for k, p in PATTERNS]
hits, per_page = [], {}
for url, p in crawl.items():
    if p.get("final_status") != 200 or p.get("text") is None:
        continue
    fu = p["final_url"]
    if fu in per_page:
        continue
    blob = {"title": p.get("title") or "", "meta_description": p.get("meta_description") or "", "h1": " | ".join(p.get("h1_texts") or []), "text": p["text"]}
    per_page[fu] = 0
    for field, txt in blob.items():
        for k, rx in RX:
            for m in rx.finditer(txt):
                s = max(0, m.start() - 70); e = min(len(txt), m.end() + 70)
                hits.append({"page": fu, "field": field, "category": k, "term": m.group(0), "context": txt[s:e]})
                per_page[fu] += 1
from collections import Counter
print(len(hits), "hits on", len([x for x in per_page.values() if x]), "pages")
print(Counter(h["category"] for h in hits))
print(Counter((h["category"], h["term"].lower()) for h in hits).most_common(60))
save_evidence("EV-D-adlaw-hits", json.dumps({"collected_at": now(), "note": "keyword hits only; human review, no legal judgement; scanned: title, meta description, H1 and main-body text of every crawled 200 page", "hit_count": len(hits), "hits": hits}, ensure_ascii=False, indent=1),
              "json", "python regex scan of EV-D-crawl-data", "regex categories: " + ", ".join(k for k, _ in PATTERNS), note="no legal judgement")
