#!/usr/bin/env python3
"""Gate G6a (v2): SEO and GEO checks against the benchmark, with the evidence in mind.

    python3 seo_coverage.py <run_dir> [--page 05-final/page.md] [--fetch] [--json]

v2 changes after the check against the 741 SEO library and 2026 research (Ahrefs content-score study, Google helpful-content guide):
term, entity and statute coverage are ADVISORY (warnings, logged), because coverage scores correlate weakly with rankings and the
percentages have no source. HARD checks are the ones the library and Google guidance support:
  H1 PAA: every real PAA question answered in one block of the page, or dropped with a reason from the fixed list.
  H2 Answer block: starts early (within the first 200 words and the first 40 % of the page), 2 to 4 sentences (warn above 4, fail above 8).
  H3 Information gain: every accordion block (Vertiefung) holds a source (paragraph, link, "Quelle"), a number or a client fact.
  H4 Own edge: at least 2 headings that no benchmark page has; not 50 % or more of our headings copied from the benchmark.
  H5 No keyword stuffing: the exact primary phrase stands in at most one third of H2/H3 headings.
  H6 Freshness: a page that cites a statute shows a visible date line ("Rechtsstand", "Zuletzt geprüft", "Stand").
  H7 E-E-A-T: at least one proven credential (claims type credential) is visible on person, service, blog, about and team pages.
Advisory: subtopic stems found on >= 40 % of >= 5 benchmark pages, capitalised entities on >= 50 % (needs --fetch), statute citations on >= 30 %.
Benchmark below 5 usable pages: advisory checks are skipped with a note.
Waivers: brief.g6_ignore_terms = [{"term": "...", "reason": "off-offer | nicht rechtssicher | Duplikat | Rauschen"}].
"""
import argparse
import json
import math
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import TECH_MARK, load_json, strip_frontmatter, visible_text  # noqa: E402

STOP = set("""der die das den dem des ein eine einer eines einem einen und oder aber auch nicht nur wie was wer wann wo wenn dass
sind ist war wird werden wurde wurden hat haben kann können muss müssen soll sollen sich sie ihr ihre ihren ihrem ihrer ihres
wir uns unser unsere für mit bei auf aus nach vor von zum zur zur über unter durch gegen ohne bis seit zwischen
mehr sehr schon noch dann dazu damit dabei hier dort diese dieser dieses diesen diesem jede jeder jedes alle alles
steht stehen gibt geben macht machen kommt kommen welche welcher welches warum wieso weshalb""".split())
GENERIC = {"informationen","informatio","service","rahmen","erfahrung","inhalte","fällen","fälle","bereich","bereiche","möglichkeiten","möglichk","beratung","anwalt","anwälte","kanzlei","rechtsanwalt","rechtsanw","leistungen","telefon","termin","kontakt","ihnen","ihrer","unser","unsere","beispiel","zeit","fragen","thema","themen","fall","lösung","lösungen","weitere","wichtig","wichtige","allgemein"}
BOILER = {"kontak", "impres", "datens", "anschr", "anfahr", "telefo", "öffnung", "cookie", "newsle", "navigat", "menü", "suche", "mehr", "weiter", "zurück", "inhalt", "startse", "willkom", "team", "kanzlei", "aktuel", "leistun", "social", "folgen", "teilen"}
LAWS = "AO|StGB|StPO|OWiG|BRAO|UStG|EStG|SchwarzArbG|AEntG|GwG|ZollVG|StBerG|AktG|HGB|GmbHG|ZPO|BGB|GG|FGO|VwGO|GVG|JGG|SGB|AWG|GewStG|KStG|BetrVG|HinSchG|LkSG"
CITE = re.compile(rf"§§?\s*(\d+[a-z]?)(?:\s*(?:Abs\.|Absatz)\s*\d+)?(?:\s*(?:S\.|Satz)\s*\d+)?(?:\s*Nr\.\s*\d+[a-z]?)?\s*({LAWS})\b")


def stem(w):
    w = w.lower()
    return w[:7]


def toks(s):
    return [stem(w) for w in re.findall(r"[A-Za-zÄÖÜäöüß]{5,}", s) if w.lower() not in STOP]


def headings(raw):
    body = strip_frontmatter(raw).split(TECH_MARK, 1)[0]
    return [h.strip() for h in re.findall(r"(?m)^#{1,4}\s+(.+)$", body)]


def blocks(raw):
    body = strip_frontmatter(raw).split(TECH_MARK, 1)[0]
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    parts = re.split(r"(?m)^(#{2,4}\s+.+)$", body)
    out, cur = [], ("", "")
    for p in parts:
        if re.match(r"^#{2,4}\s+", p):
            cur = (p.strip("# ").strip(), "")
            out.append(cur)
        elif out:
            out[-1] = (out[-1][0], out[-1][1] + p)
    return out


def fetch_text(url):
    for _ in range(2):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh) Chrome/124"})
            h = urllib.request.urlopen(req, timeout=25).read().decode("utf-8", "ignore")
            h = re.sub(r"<(script|style|nav|footer|header|form|noscript)\b.*?</\1>", " ", h, flags=re.S | re.I)
            h = re.sub(r"<br\s*/?>|</p>|</h\d>|</li>|</div>", "\n", h)
            import html as _h
            return re.sub(r"[ \t]+", " ", _h.unescape(re.sub(r"<[^>]+>", " ", h)))
        except Exception:
            continue
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir")
    ap.add_argument("--page", default="05-final/page.md")
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    run = Path(a.run_dir)
    raw = (run / a.page).read_text(encoding="utf-8")
    brief = load_json(run / "01-brief/brief.json")
    ours = visible_text(raw)
    our_stems = set(toks(ours))
    our_text_low = ours.lower()
    fails, warns, rep = [], [], {}
    waived = {w["term"].lower() for w in brief.get("g6_ignore_terms", []) if w.get("reason")}

    bench_file = next((p for p in [run / "_work/bench-metrics.json", *sorted((run / "_work").glob("*bench*metrics*.json"))] if p.exists()), None)
    pages = []
    if bench_file:
        pages = [x for x in load_json(bench_file) if x.get("status") == "ok"]
    if not pages and brief.get("gate") == "A0-brand":
        warns.append("Typ-C-Seite ohne Wettbewerber-Benchmark (gate A0-brand): Themen-, Begriffs-, Norm- und Eigenleistungs-Prüfung entfallen")
    elif not pages:
        fails.append("kein Benchmark gespeichert (_work/bench-metrics.json fehlt oder leer)")
    else:
        n = len(pages)
        need = max(2, math.ceil(0.4 * n))
        df = {}
        ex = {}
        for p in pages:
            seen = set()
            for h in (p.get("h2") or []) + (p.get("h3") or []):
                for t in set(toks(h)):
                    if t in BOILER or any(t.startswith(b) for b in BOILER):
                        continue
                    if t not in seen:
                        seen.add(t)
                        df[t] = df.get(t, 0) + 1
                        ex.setdefault(t, h)
        want = sorted([t for t, c in df.items() if c >= need], key=lambda t: -df[t])
        miss = [t for t in want if t not in our_stems and ex[t].lower() not in waived and t not in waived and t not in GENERIC]
        rep["subtopics"] = {"pages": n, "need_pages": need, "terms": len(want),
                            "missing": [(t, df[t], ex[t]) for t in miss]}
        if len(pages) < 5:
            warns.append(f"Benchmark hat nur {len(pages)} lesbare Seiten (unter 5): Themen-, Begriffs- und Norm-Prüfung sind nur Hinweise")
        if miss:
            warns.append(f"[Hinweis] {len(miss)} von {len(want)} Themen-Begriffen der Wettbewerber-Überschriften fehlen im Text: "
                         + "; ".join(f'{t}* ({df[t]}/{n}, z. B. "{ex[t][:50]}")' for t in miss[:8]))

        # statutes
        cites = {}
        texts = []
        cache = run / "_work/bench-text"
        if a.fetch:
            cache.mkdir(exist_ok=True)
        for i, p in enumerate(pages):
            f = cache / f"{i}.txt"
            t = None
            if f.exists():
                t = f.read_text(encoding="utf-8")
            elif a.fetch:
                t = fetch_text(p["url"])
                if t:
                    f.write_text(t, encoding="utf-8")
            if t:
                texts.append(t)
        rep["bench_texts"] = len(texts)
        if texts:
            nt = len(texts)
            for t in texts:
                for k in {(m.group(1).lower(), m.group(2)) for m in CITE.finditer(t)}:
                    cites[k] = cites.get(k, 0) + 1
            our_cites = {(m.group(1).lower(), m.group(2)) for m in CITE.finditer(ours)}
            wantc = [k for k, c in cites.items() if c >= max(2, math.ceil(0.3 * nt))]
            missc = [k for k in wantc if k not in our_cites]
            rep["statutes"] = {"wanted": [f"§ {k[0]} {k[1]}" for k in wantc], "missing": [f"§ {k[0]} {k[1]}" for k in missc]}
            if missc:
                warns.append("[Hinweis] Normen der Wettbewerber ohne Zitat (nur zitieren, wenn sie für die Seite stimmen und relevant sind): " + ", ".join(f"§ {k[0]} {k[1]}" for k in missc[:8]))
            # entities
            ent_df = {}
            for t in texts:
                caps = {}
                for w in re.findall(r"\b[A-ZÄÖÜ][a-zäöüß]{5,}\b", t):
                    caps[w.lower()] = caps.get(w.lower(), 0) + 1
                allw = {}
                for w in re.findall(r"\b[A-Za-zÄÖÜäöüß]{6,}\b", t):
                    allw[w.lower()] = allw.get(w.lower(), 0) + 1
                for w in caps:
                    if caps[w] / max(1, allw.get(w, 1)) >= 0.7 and w not in STOP:
                        ent_df[w] = ent_df.get(w, 0) + 1
            wants = [w for w, c in sorted(ent_df.items(), key=lambda x: -x[1]) if c >= math.ceil(0.5 * nt) and stem(w) not in BOILER and w not in GENERIC and stem(w) not in GENERIC][:40]
            missing = [w for w in wants if stem(w) not in our_stems and w not in waived and w not in GENERIC and stem(w) not in GENERIC]
            cov = 1 - len(missing) / len(wants) if wants else 1
            rep["entities"] = {"wanted": len(wants), "coverage": round(cov, 2), "missing": missing}
            if missing:
                warns.append(f"[Hinweis] Begriffs-Abdeckung {int(cov*100)} % ({len(wants)} Begriffe aus mindestens 50 % der Seiten). Fehlen: {', '.join(missing[:12])}. Pflicht nur, wenn die Suchabsicht den Begriff braucht.")
        elif a.fetch:
            warns.append("Wettbewerber-Texte nicht lesbar, Begriffs- und Norm-Prüfung übersprungen")
        else:
            warns.append("Begriffs- und Norm-Prüfung nicht gelaufen (mit --fetch starten)")

    # PAA
    paa = brief.get("paa_questions")
    if paa is None:
        warns.append("brief.paa_questions fehlt (PAA-Prüfung nicht möglich)")
    else:
        bl = blocks(raw)
        rows = []
        for q in paa:
            if q.get("status") == "dropped":
                if q.get("reason_code") not in ("off-offer", "nicht rechtssicher", "Duplikat") or not q.get("reason"):
                    fails.append(f'PAA verworfen ohne Grund aus der festen Liste (reason_code: off-offer | nicht rechtssicher | Duplikat) und Text: "{q["q"]}"')
                rows.append((q["q"], "dropped", q.get("reason", "")))
                continue
            qs = {w[:5] for w in toks(q["q"])}   # 5-letter prefixes: German compounds (Steuerhinterziehung / hinterzogen)
            qs |= {w[:5] for w in re.findall(r"[A-Za-zÄÖÜäöüß]{5,}", q["q"].lower()) if w not in STOP}
            best = 0.0
            where = ""
            for h, t in bl:
                low = (h + " " + t).lower()
                sc = sum(1 for w in qs if w in low) / max(1, len(qs))
                hs = sum(1 for w in qs if w in h.lower()) / max(1, len(qs))
                sc = min(1.0, sc * 0.7 + hs * 0.5)   # a heading that names the question counts more than the body words alone
                if sc > best:
                    best, where = sc, h
            rows.append((q["q"], f"{int(best*100)} % in '{where[:40]}'", ""))
            if best < 0.6:
                fails.append(f'PAA nicht beantwortet ({int(best*100)} %): "{q["q"]}"')
        rep["paa"] = rows

    # ---- hard checks H2 to H7 ----
    body = strip_frontmatter(raw).split(TECH_MARK, 1)[0]
    plain_words = ours.split()
    total = max(1, len(plain_words))
    m = re.search(r"<!--\s*S\d\d\s+[\w+-]+\s*\|[^>]*element:\s*(hero\+)?answer[^>]*-->(.*?)<!--\s*/S\d\d\s*-->", body, flags=re.S)
    if not m and brief.get("require_answer_block", True) is False:
        pass
    elif not m:
        fails.append("H2 Direkt-Antwort-Block fehlt")
    else:
        before = visible_text(body[:m.start()])
        pos = len(before.split())
        ans = visible_text(m.group(2))
        ans_words = len(ans.split())
        ans_c = re.sub(r"\b(Abs|Nr|S|Art|z\. ?B|ggf|bzw|ca|Dr|vgl|u\. ?a|d\. ?h|ff)\.", lambda m: m.group(0).replace(".", "§§"), ans)
        sents = [x for x in re.split(r"(?<=[.!?])\s+", ans_c) if len(x.split()) >= 3]
        rep["answer"] = {"words_before": pos, "pos_percent": round(100 * pos / total), "sentences": len(sents), "words": ans_words}
        if pos > 200 or pos / total > 0.4:
            fails.append(f"H2 Direkt-Antwort beginnt zu spät (Wort {pos}, {int(100*pos/total)} % der Seite; erlaubt: bis Wort 200 und 40 %)")
        if len(sents) > 8:
            fails.append(f"H2 Direkt-Antwort hat {len(sents)} Sätze (über 8)")
        elif len(sents) > 4:
            warns.append(f"Direkt-Antwort hat {len(sents)} Sätze (Regel: 2 bis 4, etwa 50 Wörter). Kürzen für KI-Zitate.")
    for am in re.finditer(r"<!--\s*S\d\d\s+accordion\s*\|[^>]*-->(.*?)<!--\s*/S\d\d\s*-->", body, flags=re.S):
        for ht, bt in re.findall(r"(?ms)^###\s+(.+?)\s*$(.*?)(?=^###|\Z)", am.group(1)):
            t = visible_text(bt)
            if not (re.search(r"§|Quelle|https?://|\]\(/", bt) or re.search(r"\d", t)):
                fails.append(f'H3 Vertiefungs-Block ohne Quelle, Zahl oder Verweis: "{ht[:50]}"')
    hs = [h for h in re.findall(r"(?m)^#{2,3}\s+(.+)$", body)]
    kw = (brief.get("keyword_primary") or "").lower()
    kws = [w for w in re.findall(r"[a-zäöüß]{4,}", kw)]
    if kws and len(hs) >= 3:
        hit = [h for h in hs if all(re.search(r"(?<![a-zäöüß])" + re.escape(w[:max(5, len(w)-3)]), h.lower()) for w in kws)]
        if len(hit) > max(1, len(hs) // 3):
            fails.append(f"H5 Keyword-Stuffing: die Haupt-Phrase steht in {len(hit)} von {len(hs)} Überschriften (erlaubt: ein Drittel)")
    if pages:
        norm = lambda x: re.sub(r"[^a-zäöüß0-9 ]", "", x.lower()).strip()
        bh = {norm(h) for p in pages for h in (p.get("h2") or []) + (p.get("h3") or [])}
        own = [h for h in hs if norm(h) not in bh]
        copied = len(hs) - len(own)
        rep["own_headings"] = {"total": len(hs), "own": len(own), "copied": copied}
        if len(own) < 2 and len(hs) >= 4:
            fails.append("H4 weniger als 2 eigene Überschriften (keine Eigenleistung gegenüber dem Benchmark)")
        elif hs and copied / len(hs) >= 0.5:
            fails.append(f"H4 {copied} von {len(hs)} Überschriften stehen wörtlich auch beim Benchmark (Kopie der Struktur)")
    if "§" in ours and not re.search(r"Rechtsstand|Zuletzt geprüft|Stand:|Stand \w+ 20\d\d|Zuletzt aktualisiert", ours):
        fails.append("H6 Seite zitiert Gesetze, zeigt aber kein sichtbares Datum (Rechtsstand / Zuletzt geprüft)")
    cp = run / "01-brief/claims.json"
    if cp.exists() and brief.get("page_type") in ("service", "practitioner", "blog", "about", "team", "homepage"):
        cl = load_json(cp)
        cl = cl["claims"] if isinstance(cl, dict) else cl
        creds = [x for c in cl if c.get("type") == "credential" for x in c.get("must_appear", [])]
        if creds and not any(c.lower() in our_text_low for c in creds):
            fails.append("H7 keine belegte Qualifikation sichtbar auf der Seite (E-E-A-T)")

    out = {"pass": not fails, "fails": fails, "warns": warns, "report": rep}
    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=1, default=str))
    else:
        print(f"G6a coverage: {'FAIL' if fails else 'PASS'}")
        for f in fails:
            print("  FAIL ", f)
        for w in warns:
            print("  warn ", w)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
