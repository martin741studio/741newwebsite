#!/usr/bin/env python3
"""Gate G4: style rules. No dashes, one address form, no forbidden words, no leftovers.

    python3 check_style.py page.md --address du|sie [--forbidden words.txt|"a,b,c"] [--json]
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import PLACEHOLDER_RE, frontmatter, load_json, read_input, sentences, visible_text  # noqa: E402


def check(raw, address, forbidden):
    text = visible_text(raw, keep_placeholders=True)
    plain = visible_text(raw)
    fails, warns = [], []
    fm = frontmatter(raw)
    for key in ("title", "meta"):
        val = fm.get(key, "")
        if any(ch in val for ch in ("—", "–")) or re.search(r"\s-\s", val):
            fails.append(f"Gedankenstrich im Frontmatter {key}")

    for ch in ("—", "–"):
        if ch in text:
            fails.append(f"Gedankenstrich {ch} x{text.count(ch)}")
    n_hyphen = len(re.findall(r"\s-\s", text))
    if n_hyphen:
        fails.append(f"Bindestrich als Gedankenstrich ' - ' x{n_hyphen}")

    low = plain
    du = len(re.findall(r"\b(du|dir|dich|dein\w*)\b", low, flags=re.I))
    sie = len(re.findall(r"(?<![.!?]\s)(?<!^)\b(Sie|Ihnen|Ihr\w*)\b", low)) + len(re.findall(r"\b(Ihnen|Ihre[mnrs]?|Ihr)\b", low))
    if address == "du":
        if sie >= 2:
            fails.append(f"Anrede gemischt: {sie} Sie-Formen in einem du-Text")
    elif address == "sie":
        if du >= 2:
            fails.append(f"Anrede gemischt: {du} du-Formen in einem Sie-Text")
    if du >= 3 and sie >= 3:
        fails.append(f"Anrede gemischt: {du} du-Formen und {sie} Sie-Formen")

    for w in forbidden:
        w = w.strip()
        if w and re.search(rf"(?<![\wäöüß]){re.escape(w)}", plain, flags=re.I):
            fails.append(f'verbotenes Wort: "{w}"')

    for pat in (r"\bTODO\b", r"\bXXX\b", r"lorem ipsum", r"\[FEHLT", r"\{\{", r"\bTBD\b"):
        if re.search(pat, text, flags=re.I):
            fails.append(f"Rest im Text: {pat}")

    bad_ph = [m for m in re.findall(r"\[[^\]]{3,}\]", text) if not PLACEHOLDER_RE.fullmatch(m) and not m.startswith("[http")]
    bad_ph = [b for b in bad_ph if not re.match(r"\[[^\]]+\]\(", b)]
    if bad_ph:
        fails.append(f"eckige Klammern, die kein Platzhalter-Format haben: {bad_ph[:3]} (erlaubt nur [von Kunde bestätigen: ...])")

    long_s = [s for s in sentences(plain) if len(s.split()) > 28]
    if long_s:
        warns.append(f"{len(long_s)} Sätze über 28 Wörter (zum Beispiel: {long_s[0][:70]}...)")
    ich = len(re.findall(r"\b(ich|mein\w*|mir)\b", low, flags=re.I))
    wir = len(re.findall(r"\b(wir|unser\w*|uns)\b", low, flags=re.I))
    if ich >= 3 and wir >= 3:
        warns.append(f"Sprecher gemischt: ich {ich}, wir {wir}")
    return fails, warns, {"du": du, "sie": sie, "ich": ich, "wir": wir}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--text")
    ap.add_argument("--address", choices=["du", "sie", "any"], default="any")
    ap.add_argument("--forbidden", default="")
    ap.add_argument("--brief")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    raw = read_input(a.file, a.text)
    forb = []
    if a.forbidden:
        p = Path(a.forbidden)
        forb = p.read_text(encoding="utf-8").splitlines() if p.exists() else a.forbidden.split(",")
    addr = a.address
    if a.brief:
        b = load_json(a.brief)
        forb += b.get("forbidden_words", [])
        if addr == "any":
            addr = b.get("address", "any").lower()
    fails, warns, counts = check(raw, addr, forb)
    if a.json:
        print(json.dumps({"pass": not fails, "fails": fails, "warns": warns, "counts": counts}, ensure_ascii=False, indent=1))
    else:
        print(f"G4 style: {'FAIL' if fails else 'PASS'}  {counts}")
        for f in fails:
            print("  FAIL ", f)
        for w in warns:
            print("  warn ", w)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
