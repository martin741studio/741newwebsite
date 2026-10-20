#!/usr/bin/env python3
"""Run the rival-model cleanse (gate G5) over many pages and write PROPOSALS, never overwrite a page.

    python3 cleanse_all.py <content-writing-dir> [--pages st-11-steuerstrafrecht,...] [--page-file 05-final/page.md] [--wait-minutes 300]

For each page: probe codex (wait and retry while a usage limit blocks it), run cleanse_de.sh on the page, then
  - identical text            -> <page>/04-gates/cleanse.json {"status": "unchanged"}   (G5 complete)
  - claim diff FAIL           -> status "rejected" with the reasons
  - claim diff PASS, changes  -> writes 04-gates/cleanse-proposal.md (cleansed text) and cleanse.diff for human or reviewer choice
A person (or the main agent) applies only the safe changes. Legal hedges must not weaken (the writers rejected 4 of 7 changes once).
"""
import argparse
import difflib
import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def probe():
    r = run(["bash", "-c", 'echo "Antworte nur mit dem Wort ok." | codex exec --skip-git-repo-check --sandbox read-only "$(cat)" 2>&1 | tail -3'], timeout=120)
    return "ok" in r.stdout.lower() and "limit" not in r.stdout.lower()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir")
    ap.add_argument("--pages")
    ap.add_argument("--page-file", default="05-final/page.md")
    ap.add_argument("--wait-minutes", type=int, default=300)
    a = ap.parse_args()
    d = Path(a.dir)
    pages = [p.strip() for p in a.pages.split(",")] if a.pages else sorted(p.name for p in d.iterdir() if p.is_dir() and (p / a.page_file).exists())
    waited = 0
    while not probe():
        if waited >= a.wait_minutes:
            print("codex still blocked, giving up", flush=True)
            return 3
        print(f"codex blocked, waiting ({waited} min)", flush=True)
        time.sleep(600)
        waited += 10
    for name in pages:
        pg = d / name / a.page_file
        claims = d / name / "01-brief/claims.json"
        out = d / name / "04-gates"
        out.mkdir(exist_ok=True)
        tmp = out / "cleansed.tmp.md"
        r = run(["bash", str(HERE / "cleanse_de.sh"), str(pg)], env={**__import__("os").environ, "TIMEOUT": "280"})
        if r.returncode != 0 or not r.stdout.strip():
            res = {"status": "error", "code": r.returncode, "stderr": r.stderr[-300:]}
        else:
            tmp.write_text(r.stdout, encoding="utf-8")
            old = pg.read_text(encoding="utf-8").strip()
            new = r.stdout.strip()
            if old == new:
                res = {"status": "unchanged"}
            else:
                dr = run([sys.executable, str(HERE / "diff_claims.py"), "diff", str(pg), str(tmp), str(claims), "--json"])
                try:
                    dj = json.loads(dr.stdout)
                except Exception:
                    dj = {"pass": False, "fails": [dr.stdout[-200:]]}
                lint = run([sys.executable, str(HERE / "deslop_de.py"), str(tmp), "--claims", str(claims), "--json"])
                try:
                    lj = json.loads(lint.stdout)
                except Exception:
                    lj = {"score": None}
                diff = "".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), "page.md", "cleansed", n=1))
                (out / "cleanse.diff").write_text(diff, encoding="utf-8")
                if dj.get("pass"):
                    (out / "cleanse-proposal.md").write_text(r.stdout, encoding="utf-8")
                    res = {"status": "proposal", "lint": lj.get("score"), "changed_lines": diff.count("\n+") }
                else:
                    res = {"status": "rejected", "fails": dj.get("fails")}
            tmp.unlink(missing_ok=True)
        (out / "cleanse.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        print(name, res.get("status"), res.get("changed_lines", ""), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
