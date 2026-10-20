#!/usr/bin/env python3
"""Count visible words by script (A0 method 0.4). Never estimate.

    python3 wordcount.py page.md
    python3 wordcount.py page.md --bestand 248 --median 1100 --money
Prints JSON. With --bestand/--median it also checks: never thinner than Bestand, at least 70 % of the median (money pages).
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import read_input, visible_text, words  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("file", nargs="?")
ap.add_argument("--bestand", type=int)
ap.add_argument("--median", type=int)
ap.add_argument("--money", action="store_true")
a = ap.parse_args()
n = len(words(visible_text(read_input(a.file))))
out = {"words": n, "ok": True, "checks": []}
if a.bestand is not None:
    ok = n >= a.bestand
    out["checks"].append({"rule": "not thinner than Bestand", "need": a.bestand, "ok": ok})
    out["ok"] &= ok
if a.median is not None and a.money:
    need = int(a.median * 0.7)
    ok = n >= need
    out["checks"].append({"rule": "at least 70 % of competitor median", "need": need, "ok": ok})
    out["ok"] &= ok
print(json.dumps(out, ensure_ascii=False))
sys.exit(0 if out["ok"] else 1)
