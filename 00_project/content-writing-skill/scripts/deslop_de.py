#!/usr/bin/env python3
"""German AI-tell linter for the slop gate (G5). English text goes to slopmonster's deslop.py.

    python3 deslop_de.py page.md                 # score visible text, exit 1 below 5/5
    python3 deslop_de.py page.md --claims claims.json   # numbers that the claim list backs are not "invented proof"
    python3 deslop_de.py --text "..." --json

Five groups, one point each (same shape as slopmonster): vocabulary, constructions,
punctuation, rhythm, invented proof. Score = 5 minus the groups that hit.
Reads only visible copy (no frontmatter, no <!-- TECH --> block, no comments, no placeholders).
"""
import argparse
import json
import os
import re
import statistics
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import REFS, detect_lang, load_json, numbers, read_input, sentences, visible_text, words  # noqa: E402


def allowed_numbers(claims_path):
    if not claims_path:
        return set()
    data = load_json(claims_path)
    items = data["claims"] if isinstance(data, dict) else data
    out = set()
    for c in items:
        for n in c.get("numbers", []):
            out.add(str(n))
        out.update(numbers(c.get("text", "")))
    return out


def lint_de(text, claims_path=None):
    tells = load_json(REFS / "de-tells.json")
    low = text.lower()
    hits = {"vocabulary": [], "constructions": [], "punctuation": [], "rhythm": [], "invented proof": []}

    for pat in tells["vocab_hard"]:
        for m in re.finditer(rf"(?<![\wäöüß]){pat}", low):
            hits["vocabulary"].append(m.group(0))
    soft = []
    for pat in tells["vocab_soft"]:
        for m in re.finditer(rf"(?<![\wäöüß]){pat}", low):
            soft.append(m.group(0))
    soft_group_hit = len(soft) >= tells["soft_threshold"]
    if soft_group_hit:
        hits["vocabulary"].extend(f"{w} (weiches Wort, {len(soft)} im Text)" for w in sorted(set(soft)))

    for c in tells["constructions"]:
        for m in re.finditer(c["re"], low, flags=re.S):
            hits["constructions"].append(f'{c["label"]}: "{m.group(0).strip()[:70]}"')

    for ch in tells["dash_chars"]:
        n = text.count(ch)
        if n:
            hits["punctuation"].append(f"Gedankenstrich {ch} x{n}")
    n = len(re.findall(r"\s-\s", text))
    if n:
        hits["punctuation"].append(f"Bindestrich als Gedankenstrich ' - ' x{n}")
    if text.count("!") >= 3:
        hits["punctuation"].append(f"Ausrufezeichen x{text.count('!')}")

    triples = re.findall(r"\b[\wäöüß-]+, [\wäöüß-]+ und [\wäöüß-]+\b", text)
    if len(triples) >= max(3, len(text.split()) // 250 + 2):
        hits["rhythm"].append(f"Dreier-Reihung x{len(triples)} (zum Beispiel: {triples[0]})")
    sents = [s for s in sentences(text) if len(s.split()) >= 3]
    if len(sents) >= 8:
        lens = [len(s.split()) for s in sents]
        sd = statistics.pstdev(lens)
        if sd < 3.5:
            hits["rhythm"].append(f"Satzlängen zu gleich (Streuung {sd:.1f}, mindestens 3,5 nötig)")

    ok_nums = allowed_numbers(claims_path)
    seen_proof = set()
    for pat in tells["proof_patterns"]:
        for m in re.finditer(pat, low):
            nums = numbers(m.group(0))
            if nums and all(n in ok_nums for n in nums):
                continue
            key = tuple(nums)
            if key in seen_proof:
                continue
            seen_proof.add(key)
            hits["invented proof"].append(f'"{m.group(0).strip()}" ohne Beleg in der Claim-Liste')

    score = 5 - sum(1 for g in hits.values() if g)
    return score, hits, len(words(text))


def lint_en(path, text):
    candidates = [
        os.environ.get("SLOPMONSTER_DESLOP", ""),
        str(Path(__file__).resolve().parents[3] / ".claude/skills/slopmonster/tools/deslop.py"),
        str(Path.home() / ".claude/skills/slopmonster/tools/deslop.py"),
        "/Users/martindrendel/741website/.claude/skills/slopmonster/tools/deslop.py",
        str(Path.cwd() / ".claude/skills/slopmonster/tools/deslop.py"),
    ]
    tool = next((c for c in candidates if c and Path(c).exists()), None)
    if not tool:
        print("deslop_de: slopmonster deslop.py not found for English text", file=sys.stderr)
        return 2, None
    r = subprocess.run([sys.executable, tool, "--text", text, "--allow-proof"], capture_output=True, text=True)
    m = re.search(r"score (\d)/5", r.stdout)
    return (int(m.group(1)) if m else 0), r.stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--text")
    ap.add_argument("--claims")
    ap.add_argument("--lang", choices=["auto", "de", "en"], default="auto")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    raw = read_input(a.file, a.text)
    text = visible_text(raw)
    if not text.strip():
        print("deslop_de: empty input, refusing to pass", file=sys.stderr)
        return 2
    lang = detect_lang(text) if a.lang == "auto" else a.lang

    if lang == "en":
        score, out = lint_en(a.file, text)
        if out is None:
            return 2
        print(out)
        return 0 if score == 5 else 1

    score, hits, nwords = lint_de(text, a.claims)
    if a.json:
        print(json.dumps({"lang": "de", "score": score, "words": nwords, "hits": hits}, ensure_ascii=False, indent=1))
    else:
        print(f"{nwords} Wörter sichtbarer Text (de)\n")
        for group, items in hits.items():
            if items:
                print(f"  {group}:")
                for i in items[:12]:
                    print(f"    · {i}")
        verdict = "CLEAN" if score == 5 else "braucht Umschreiben und Cleanse"
        print(f"\n  score {score}/5  {verdict}")
    return 0 if score == 5 else 1


if __name__ == "__main__":
    sys.exit(main())
