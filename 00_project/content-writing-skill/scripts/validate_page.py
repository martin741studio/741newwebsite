#!/usr/bin/env python3
"""Gate G3: SEO and structure check of the Markdown master against the brief.

    python3 validate_page.py page.md --brief brief.json [--placeholders placeholders.md] [--json]

Checks: frontmatter title (<=60) and meta (<=155), exactly one H1, primary keyword in title and H1,
city in H1 for local pages, section IDs in the order of the brief, word floors, answer block, FAQ count,
internal links in the visible body, CTA count and text, placeholder list matches the page.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import PLACEHOLDER_RE, TECH_MARK, frontmatter, load_json, read_input, strip_frontmatter, visible_text, words  # noqa: E402


def run(raw, brief, placeholders_md=None):
    fails, warns, info = [], [], {}
    fm = frontmatter(raw)
    body = strip_frontmatter(raw)
    body_visible_src = body.split(TECH_MARK, 1)[0]

    title, meta = fm.get("title", ""), fm.get("meta", "")
    if not title:
        fails.append("frontmatter: title fehlt")
    elif len(title) > 60:
        fails.append(f"Title {len(title)} Zeichen (max 60)")
    if not meta:
        fails.append("frontmatter: meta fehlt")
    elif len(meta) > 155:
        fails.append(f"Meta {len(meta)} Zeichen (max 155)")

    h1 = re.findall(r"(?m)^#\s+(.+)$", body_visible_src) + re.findall(r"<h1[^>]*>(.*?)</h1>", body_visible_src, flags=re.S | re.I)
    if len(h1) != 1:
        fails.append(f"H1-Anzahl {len(h1)} (genau 1 nötig)")
    kw = (brief.get("keyword_primary") or "").lower()
    if kw:
        if title and kw not in title.lower():
            warns.append(f'Haupt-Keyword "{kw}" nicht im Title')
        if h1 and not all(part in h1[0].lower() for part in kw.split()[:2]):
            warns.append(f'Haupt-Keyword "{kw}" nicht (vollständig) im H1')
    city = (brief.get("local_city") or "")
    if city and h1 and brief.get("page_type") in ("location", "homepage", "service") and city.lower() not in h1[0].lower():
        warns.append(f"Ort {city} nicht im H1")

    ids = re.findall(r"<!--\s*(S\d\d)\b", body_visible_src)
    plan = [s["id"] for s in brief.get("sections", [])]
    if plan and ids != plan:
        fails.append(f"Abschnitts-IDs weichen vom Plan ab: Seite {ids} gegen Plan {plan}")
    closers = re.findall(r"<!--\s*/(S\d\d)\s*-->", body_visible_src)
    if ids != closers:
        fails.append("Abschnitt ohne Schlussmarke <!-- /Sxx -->")
    empty = []
    for sid in ids:
        m = re.search(rf"<!--\s*{sid}\b.*?-->(.*?)<!--\s*/{sid}\s*-->", body_visible_src, flags=re.S)
        if m and len(words(visible_text(m.group(1)))) < 5:
            empty.append(sid)
    if empty:
        fails.append(f"Abschnitte fast leer: {empty}")

    n = len(words(visible_text(raw)))
    info["words"] = n
    if brief.get("bestand_words") and n < brief["bestand_words"]:
        fails.append(f"Wortzahl {n} unter Bestand {brief['bestand_words']}")
    if brief.get("money_page") and brief.get("benchmark_median_words"):
        need = int(brief["benchmark_median_words"] * 0.7)
        if n < need:
            fails.append(f"Wortzahl {n} unter 70 % des Wettbewerber-Medians ({need})")
    if brief.get("word_range"):
        lo, hi = brief["word_range"]
        if not (lo <= n <= hi):
            warns.append(f"Wortzahl {n} außerhalb Zielbereich {lo} bis {hi}")

    if brief.get("require_answer_block", True) and brief.get("page_type") != "location":
        if not re.search(r"element:\s*(hero\+)?answer|\|\s*answer\b", body_visible_src):
            fails.append("Direkt-Antwort-Block fehlt (Abschnitt mit element: answer)")
    faq_min = brief.get("faq_min", 0)
    if faq_min:
        q = len(re.findall(r"(?m)^###\s+.+\?\s*$", body_visible_src))
        if q < faq_min:
            fails.append(f"FAQ: {q} Fragen (mindestens {faq_min}, Format '### Frage?')")
    links = re.findall(r"\]\((/[^)\s]*|https?://[^)\s]*)\)", body_visible_src)
    lmin = brief.get("internal_links_min", 0)
    if len(links) < lmin:
        fails.append(f"interne Links im sichtbaren Text: {len(links)} (mindestens {lmin})")
    ctas = len(re.findall(r"cta:\s*(primary|secondary)", body_visible_src))
    if brief.get("cta_min") and ctas < brief["cta_min"]:
        fails.append(f"CTA-Abschnitte: {ctas} (mindestens {brief['cta_min']})")
    if brief.get("cta_text") and brief["cta_text"].lower() not in body_visible_src.lower():
        fails.append(f'Primärer CTA-Text "{brief["cta_text"]}" fehlt')

    ph = PLACEHOLDER_RE.findall(raw)
    info["placeholders"] = len(ph)
    if placeholders_md and Path(placeholders_md).exists():
        listed = Path(placeholders_md).read_text(encoding="utf-8")
        missing = [p for p in set(ph) if p not in listed]
        if missing:
            fails.append(f"{len(missing)} Platzhalter fehlen in placeholders.md")
    elif ph:
        warns.append("placeholders.md fehlt, obwohl Platzhalter im Text stehen")
    if "schema" not in body.lower().split(TECH_MARK, 1)[-1] and TECH_MARK in body:
        warns.append("Technik-Block ohne Schema-Abschnitt")
    if TECH_MARK not in body:
        warns.append("Technik-Block (<!-- TECH -->) fehlt")
    return fails, warns, info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--brief", required=True)
    ap.add_argument("--placeholders")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    fails, warns, info = run(read_input(a.file), load_json(a.brief), a.placeholders)
    if a.json:
        print(json.dumps({"pass": not fails, "fails": fails, "warns": warns, "info": info}, ensure_ascii=False, indent=1))
    else:
        print(f"G3 seo/structure: {'FAIL' if fails else 'PASS'}  {info}")
        for f in fails:
            print("  FAIL ", f)
        for w in warns:
            print("  warn ", w)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
