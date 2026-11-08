#!/usr/bin/env python3
"""
Write or update the run file of one backlink-dach run, so the overview Excel
(~/Desktop/Workflow-Uebersicht.xlsx) shows the run by itself.

Path:   00_project/assets/<slug>/backlink/<YYYY-MM-DD>/_run.json   (one folder per run)
Schema: 00_project/workflow-registry/README.md ("_run.json"). The Stop hook runs
        workflow_registry.py sync after every turn and reads this file.

Call it at every checkpoint and at the end of the run:
    python3 write_run.py --slug huewel --client "Praxis Hüwel" --status "in Arbeit" \
        --result "<Sheet-Link or 01-baseline/ path>" --note "Checkpoint 1: Baseline gezeigt"

Without --date the newest run folder of the client is updated; if none exists, today's
folder is created. Fields not given keep their old value.
"""
import argparse
import datetime
import glob
import json
import os
import sys

ROOT = "/Users/martindrendel/741website"
STATUSES = ("in Arbeit", "Trockenlauf", "fertig, Freigabe offen")
MODES = ("Echt", "Trockenlauf")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True, help="folder name under 00_project/assets/, e.g. huewel")
    ap.add_argument("--client", required=True, help="client name as in the overview Excel, e.g. 'Praxis Hüwel'")
    ap.add_argument("--status", required=True, choices=STATUSES)
    ap.add_argument("--mode", choices=MODES)
    ap.add_argument("--date", help="run folder date YYYY-MM-DD (default: newest folder, else today)")
    ap.add_argument("--result", help="link or path to the main result (Sheet link after Checkpoint 2)")
    ap.add_argument("--drive", help="Drive folder link")
    ap.add_argument("--note", help="one line: checkpoint reached, next step")
    ap.add_argument("--local", help="working folder if not 00_project/assets/<slug>/backlinks (repo-relative or absolute)")
    a = ap.parse_args()

    base = os.path.join(ROOT, "00_project", "assets", a.slug, "backlink")
    if a.date:
        try:
            datetime.date.fromisoformat(a.date)
        except ValueError:
            sys.exit(f"--date '{a.date}' ist kein Datum YYYY-MM-DD.")
        run_dir = os.path.join(base, a.date)
    else:
        existing = sorted(d for d in glob.glob(os.path.join(base, "????-??-??")) if os.path.isdir(d))
        run_dir = existing[-1] if existing else os.path.join(base, datetime.date.today().isoformat())
    os.makedirs(run_dir, exist_ok=True)

    path = os.path.join(run_dir, "_run.json")
    data = {}
    if os.path.exists(path):
        try:
            data = json.load(open(path, encoding="utf-8"))
        except json.JSONDecodeError:
            sys.exit(f"{path} ist kein gültiges JSON. Datei prüfen, nicht überschreiben.")

    data.update({"client": a.client, "workflow": "backlink", "status": a.status,
                 "mode": a.mode or data.get("mode") or "Echt",
                 "last_run": a.date or datetime.date.today().isoformat(),
                 "local": os.path.relpath(os.path.abspath(os.path.join(ROOT, a.local)) if a.local else
                                          os.path.join(ROOT, "00_project", "assets", a.slug, "backlinks"), ROOT)})
    for k in ("result", "drive", "note"):
        v = getattr(a, k)
        if v:
            data[k] = v
    for k in ("result", "drive", "note"):
        data.setdefault(k, "")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"OK — {os.path.relpath(path, ROOT)}: {data['status']} · {data['note']}")


if __name__ == "__main__":
    main()
