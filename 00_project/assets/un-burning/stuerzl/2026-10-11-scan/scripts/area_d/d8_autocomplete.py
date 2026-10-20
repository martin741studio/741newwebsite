"""D08: Google autocomplete (free suggest endpoint) for brand + negative modifiers. GET only."""
import sys, os, json, urllib.parse, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ub_lib import *

QUERIES = []
for brand in ["stürzl steuerstrafrecht", "anja stürzl", "dr. anja stürzl", "kanzlei stürzl"]:
    QUERIES.append(brand)
    for mod in ["erfahrungen", "bewertung", "abzocke", "kosten", "betrug", "skandal"]:
        QUERIES.append(f"{brand} {mod}")
out = {}
for q in QUERIES:
    url = "https://suggestqueries.google.com/complete/search?client=firefox&hl=de&gl=de&q=" + urllib.parse.quote(q)
    try:
        r = SESS.get(url, timeout=20)
        out[q] = {"status": r.status_code, "suggestions": (r.json()[1] if r.status_code == 200 else None)}
    except Exception as e:
        out[q] = {"status": None, "error": f"{type(e).__name__}: {e}"}
    time.sleep(DELAY)
    print(q, out[q].get("suggestions"), out[q].get("error"))
save_evidence("EV-D-autocomplete", json.dumps({"collected_at": now(), "endpoint": "suggestqueries.google.com/complete/search?client=firefox&hl=de&gl=de", "results": out}, ensure_ascii=False, indent=1),
              "json", "requests GET (Google suggest endpoint, free)", f"{len(QUERIES)} queries, hl=de gl=de", note="autocomplete is personalised/regional; read from a non-logged-in request")
