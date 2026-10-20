#!/usr/bin/env python3
"""Gates G1 (fact trace) and the cleanse guard.

    python3 diff_claims.py trace page.md claims.json [--json]
        Every number in the visible text must be backed by the claim list.
        Every claim marked required must appear. Unused claims are warned.
    python3 diff_claims.py diff before.md after.md claims.json [--json]
        After a rival-model cleanse: no new numbers, no lost required claims,
        same placeholders, same section IDs, length within 10 %.

claims.json: {"claims":[{"id":"C01","text":"...","source":"...","type":"fact|credential|number|legal|placeholder",
              "numbers":["14"],"must_appear":["Fachanwältin für Steuerrecht"],"required":true}]}
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import PLACEHOLDER_RE, load_json, numbers, read_input, visible_text, words  # noqa: E402

UNIT_AFTER = r"\s*(%|€|euro|prozent|jahr\w*|mandant\w*|bewertung\w*|fälle|fällen|verfahren|tage\w*|stunden|minuten|monat\w*|wochen)"


def claim_items(path):
    d = load_json(path)
    return d["claims"] if isinstance(d, dict) else d


def allowed(claims, extra=()):
    out = set(extra)
    for c in claims:
        out.update(str(n) for n in c.get("numbers", []))
        out.update(numbers(c.get("text", "")))
        for s in c.get("must_appear", []):
            out.update(numbers(s))
    return out


def text_numbers(raw):
    t = visible_text(raw)
    t = re.sub(r"(?m)^\s*\d+[.)]\s+", "", t)          # numbered list markers
    return t, numbers(t)


def trace(raw, claims):
    t, nums = text_numbers(raw)
    ok = allowed(claims)
    low = t.lower()
    untraced = []
    for n in nums:
        if n in ok:
            continue
        if n.isdigit() and int(n) <= 10 and not re.search(rf"(?<!\d){n}{UNIT_AFTER}", low):
            continue
        untraced.append(n)
    untraced = sorted(set(untraced))
    missing = []
    unused = []
    for c in claims:
        needs = c.get("must_appear", [])
        found = all(s.lower() in low or s.lower() in raw.lower() for s in needs) if needs else True
        if c.get("required") and not found:
            missing.append(c["id"])
        if needs and not found and not c.get("required"):
            unused.append(c["id"])
    fails = []
    if untraced:
        fails.append(f"Zahlen ohne Beleg in der Claim-Liste: {untraced}")
    if missing:
        fails.append(f"Pflicht-Claims fehlen im Text: {missing}")
    return fails, ([f"Claims nicht verwendet: {unused}"] if unused else [])


def diff(before, after, claims):
    tb, nb = text_numbers(before)
    ta, na = text_numbers(after)
    fails = []
    new = sorted(set(na) - set(nb) - allowed(claims))
    if new:
        fails.append(f"Cleanse hat neue Zahlen eingefügt: {new}")
    lost = [c["id"] for c in claims if c.get("required") and c.get("must_appear")
            and not all(s.lower() in ta.lower() or s.lower() in after.lower() for s in c["must_appear"])]
    if lost:
        fails.append(f"Cleanse hat Pflicht-Claims entfernt: {lost}")
    pb = sorted(PLACEHOLDER_RE.findall(before))
    pa = sorted(PLACEHOLDER_RE.findall(after))
    if pb != pa:
        fails.append(f"Platzhalter geändert: vorher {len(pb)}, nachher {len(pa)}")
    sb = re.findall(r"<!--\s*(/?S\d\d)\b", before)
    sa = re.findall(r"<!--\s*(/?S\d\d)\b", after)
    if sb != sa:
        fails.append("Abschnitts-IDs (<!-- S01 ... -->) geändert oder verloren")
    br = lambda t: set(re.findall(r"(?<!\])\[[^\]\n]{2,}\](?!\()", t))
    new_br = sorted(br(after) - br(before))
    if new_br:
        fails.append(f"Cleanse hat neue eckige Klammern eingefügt: {new_br[:3]} (insgesamt {len(new_br)})")
    wb, wa = len(words(tb)), len(words(ta))
    if wb and abs(wa - wb) / wb > 0.10:
        fails.append(f"Länge außerhalb 10 %: {wb} -> {wa} Wörter")
    return fails, []


def main():
    args = [a for a in sys.argv[1:] if a != "--json"]
    as_json = "--json" in sys.argv
    if len(args) >= 3 and args[0] == "trace":
        fails, warns = trace(read_input(args[1]), claim_items(args[2]))
    elif len(args) >= 4 and args[0] == "diff":
        fails, warns = diff(read_input(args[1]), read_input(args[2]), claim_items(args[3]))
    else:
        print(__doc__)
        return 2
    if as_json:
        print(json.dumps({"pass": not fails, "fails": fails, "warns": warns}, ensure_ascii=False, indent=1))
    else:
        print(f"{args[0]}: {'FAIL' if fails else 'PASS'}")
        for f in fails:
            print("  FAIL ", f)
        for w in warns:
            print("  warn ", w)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
