#!/usr/bin/env python3
"""Gate G2: legal word scan for HWG (health) and BRAO/UWG (law). Not legal advice.

    python3 check_legal.py page.md --mode hwg|brao|none [--claims claims.json] [--json]

Block hits fail the gate (exit 1). Review hits are listed for the human check.
A 'review' title word (Fachanwältin) passes only when a claim in claims.json has type "credential" and contains it.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import REFS, load_json, read_input, sentences, visible_text  # noqa: E402


def scan(text, mode, claims=None):
    terms = load_json(REFS / "legal-terms.json")[mode]
    low = text.lower()
    block, review = [], []
    cred_text = " ".join(c.get("text", "") for c in (claims or []) if c.get("type") == "credential").lower()
    for label, pat in terms["block"]:
        for m in re.finditer(pat, low):
            a, b = max(0, m.start() - 40), min(len(low), m.end() + 40)
            block.append({"rule": label, "match": m.group(0), "context": text[a:b].replace("\n", " ")})
    soft = [s.lower() for s in terms.get("softeners", [])]
    for label, pat in terms["review"]:
        for m in re.finditer(pat, low):
            word = m.group(0)
            if "Titel" in label or "Schwerpunkt" in label:
                if word in cred_text or word[:8] in cred_text:
                    continue
            a, b = max(0, m.start() - 40), min(len(low), m.end() + 40)
            if label.startswith("Wirkwort"):
                sent = next((s for s in sentences(low) if word in s), "")
                if any(sw in sent for sw in soft):
                    continue
            review.append({"rule": label, "match": word, "context": text[a:b].replace("\n", " ")})
    notice = terms.get("required_notice")
    notice_missing = bool(notice) and notice.lower() not in low
    return block, review, notice_missing, notice


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--text")
    ap.add_argument("--mode", required=True, choices=["hwg", "brao", "none"])
    ap.add_argument("--claims")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-notice-check", action="store_true", help="skip the mandatory-notice check (for single sections)")
    a = ap.parse_args()
    raw = read_input(a.file, a.text)
    text = visible_text(raw)
    if not text.strip():
        print("check_legal: empty input", file=sys.stderr)
        return 2
    claims = None
    if a.claims:
        d = load_json(a.claims)
        claims = d["claims"] if isinstance(d, dict) else d
    block, review, notice_missing, notice = scan(text, a.mode, claims)
    if a.no_notice_check:
        notice_missing = False
    fail = bool(block) or notice_missing
    if a.json:
        print(json.dumps({"mode": a.mode, "pass": not fail, "block": block, "review": review,
                          "notice_missing": notice_missing}, ensure_ascii=False, indent=1))
    else:
        print(f"G2 legal ({a.mode}): {'FAIL' if fail else 'PASS'}")
        for h in block:
            print(f'  BLOCK  {h["rule"]}: "{h["match"]}"  ...{h["context"]}...')
        if notice_missing:
            print(f'  BLOCK  Pflichthinweis fehlt: "{notice}"')
        for h in review:
            print(f'  review {h["rule"]}: "{h["match"]}"  ...{h["context"]}...')
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
