#!/usr/bin/env python3
"""Google Autocomplete topic tree (free). Fixes the 'volume 0 means no data' gap.

Usage:
  autocomplete_tree.py --out tree.json [--hl de --gl de] [--letters] "seed one" "seed two" ...

For every seed it asks: "<seed>", "<seed> a" .. "<seed> z" (with --letters), and question prefixes
(was, wie, wann, warum, wo, wer, kann, ist) + seed. Writes {seed: {query: [suggestions]}}.
Throttled. Failed calls are listed under "_errors", never dropped silently.
"""
import argparse, json, time, urllib.parse, urllib.request

QWORDS = ["was", "wie", "wann", "warum", "wo", "wer", "kann", "ist", "wie viel", "welche"]


def suggest(q, hl, gl):
    url = "https://suggestqueries.google.com/complete/search?" + urllib.parse.urlencode({"client": "firefox", "hl": hl, "gl": gl, "q": q})
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=20) as r:
        return json.loads(r.read().decode("utf-8", errors="replace"))[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("seeds", nargs="+")
    ap.add_argument("--out", required=True)
    ap.add_argument("--hl", default="de")
    ap.add_argument("--gl", default="de")
    ap.add_argument("--letters", action="store_true")
    ap.add_argument("--qwords", default="", help="comma list of question words (default German). English: what,how,why,where,who,can,is,how much,best,does")
    ap.add_argument("--sleep", type=float, default=0.25)
    a = ap.parse_args()
    qwords = [w.strip() for w in a.qwords.split(",") if w.strip()] or QWORDS
    out, errors = {}, []
    for seed in a.seeds:
        qs = [seed] + [f"{seed} {c}" for c in "abcdefghijklmnopqrstuvwxyz"] * a.letters + [f"{w} {seed}" for w in qwords]
        out[seed] = {}
        for q in qs:
            for attempt in range(2):
                try:
                    out[seed][q] = suggest(q, a.hl, a.gl)
                    break
                except Exception as e:  # noqa
                    if attempt == 1:
                        errors.append({"q": q, "error": str(e)[:100]})
                    time.sleep(1)
            time.sleep(a.sleep)
    out["_errors"] = errors
    json.dump(out, open(a.out, "w"), ensure_ascii=False, indent=1)
    total = len({s for sd in out.values() if isinstance(sd, dict) for v in sd.values() if isinstance(v, list) for s in v})
    print(f"{total} unique suggestions, {len(errors)} errors -> {a.out}")


if __name__ == "__main__":
    main()
