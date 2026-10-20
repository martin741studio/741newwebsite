#!/usr/bin/env python3
"""Run gates G1 to G5 (lint part) on a draft and write the gate report.

    python3 run_gates.py <run_dir> [--page 03-draft/draft-v1.md]

Needs: <run_dir>/01-brief/brief.json and claims.json. Writes <run_dir>/04-gates/gates.json and gates.md.
Exit 1 if any gate fails. The rival-model cleanse is separate (cleanse_de.sh); run it, then run this again.
"""
import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sh(*cmd):
    r = subprocess.run([sys.executable, *map(str, cmd)], capture_output=True, text=True)
    try:
        return json.loads(r.stdout), r.returncode
    except json.JSONDecodeError:
        return {"pass": False, "fails": [f"Skript-Fehler: {r.stdout[-200:]} {r.stderr[-200:]}"], "warns": []}, r.returncode


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir")
    ap.add_argument("--page", default="03-draft/draft-v1.md")
    a = ap.parse_args()
    run = Path(a.run_dir)
    page = run / a.page
    brief_p = run / "01-brief/brief.json"
    claims_p = run / "01-brief/claims.json"
    for p in (page, brief_p, claims_p):
        if not p.exists():
            print(f"run_gates: missing {p}", file=sys.stderr)
            return 2
    brief = json.loads(brief_p.read_text(encoding="utf-8"))
    mode = {"HWG": "hwg", "BRAO": "brao"}.get(str(brief.get("legal_mode", "")).upper(), "none")
    ph = run / "05-final/placeholders.md"

    res = {}
    res["G1 facts"], _ = sh(HERE / "diff_claims.py", "trace", page, claims_p, "--json")
    legal_args = [HERE / "check_legal.py", page, "--mode", mode, "--claims", claims_p, "--json"]
    if brief.get("section_only"):
        legal_args.append("--no-notice-check")
    res["G2 legal"], _ = sh(*legal_args)
    g2 = res["G2 legal"]
    g2["fails"] = [f'{h["rule"]}: "{h["match"]}"' for h in g2.get("block", [])]
    if g2.get("notice_missing"):
        g2["fails"].append("Pflichthinweis fehlt")
    seo_args = [HERE / "validate_page.py", page, "--brief", brief_p, "--json"]
    if ph.exists():
        seo_args += ["--placeholders", ph]
    res["G3 seo"], _ = sh(*seo_args)
    res["G4 style"], _ = sh(HERE / "check_style.py", page, "--brief", brief_p, "--json")
    lint, _ = sh(HERE / "deslop_de.py", page, "--claims", claims_p, "--json")
    score = lint.get("score")
    lint["pass"] = score == 5
    lint["fails"] = [f"{g}: {', '.join(v[:3])}" for g, v in lint.get("hits", {}).items() if v]
    lint.setdefault("warns", [])
    res["G5 slop (lint)"] = lint

    # G6 coverage and schema (only when a benchmark or a nap_file exists; money pages must have both)
    cov, _ = sh(HERE / "seo_coverage.py", run, "--page", a.page, "--json")
    sch_fails, sch_warns = [], []
    if brief.get("nap_file"):
        mk = subprocess.run([sys.executable, HERE / "schema_tool.py", "make", run, "--page", a.page], capture_output=True, text=True)
        ck, _ = sh(HERE / "schema_tool.py", "check", run, "--page", a.page, "--json")
        sch_fails, sch_warns = ck.get("fails", []), ck.get("warns", [])
    elif brief.get("money_page"):
        sch_fails = ["brief.nap_file fehlt (Schema braucht gesperrte Stammdaten)"]
    g6 = {"pass": cov.get("pass") and not sch_fails, "fails": cov.get("fails", []) + sch_fails, "warns": cov.get("warns", []) + sch_warns}
    res["G6 seo/geo coverage + schema"] = g6
    ok = all(r.get("pass") for r in res.values())
    out = {"date": str(date.today()), "page": str(page), "pass": ok, "gates": res}
    (run / "04-gates").mkdir(exist_ok=True)
    (run / "04-gates/gates.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    lines = [f"# Gate report {date.today()}", f"Page: `{page.name}`. Result: **{'PASS' if ok else 'FAIL'}**", "",
             "| Gate | Result | Findings |", "| --- | --- | --- |"]
    for name, r in res.items():
        f = "; ".join(r.get("fails", [])) or "none"
        lines.append(f"| {name} | {'PASS' if r.get('pass') else 'FAIL'} | {f} |")
    review = res["G2 legal"].get("review", [])
    if review:
        lines += ["", "## Legal: for human review", ""]
        lines += [f'- {h["rule"]}: "{h["match"]}" ...{h["context"]}...' for h in review]
    warns = [f"{n}: {w}" for n, r in res.items() for w in r.get("warns", [])]
    if warns:
        lines += ["", "## Warnings", ""] + [f"- {w}" for w in warns]
    (run / "04-gates/gates.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
