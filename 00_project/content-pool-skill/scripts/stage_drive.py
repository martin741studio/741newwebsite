#!/usr/bin/env python3
"""Stage a finished content-pool run for the Drive upload: flat names (step number first), PDFs of both reports, raw-data zip, README, manifest.

Usage: stage_drive.py <content-pool run dir>
Output: <run>/_drive/ with all files and MANIFEST.json (name -> bytes). Upload that folder with the browser method
(about 10 MB per call), then compare the Drive listing with MANIFEST.json.
Needs Google Chrome for the PDFs. The zip holds 02-competitors, 03-demand, the own-page data and spend.jsonl. No secrets are read.
"""
import glob, json, os, shutil, subprocess, sys, zipfile

run = sys.argv[1].rstrip("/")
out = f"{run}/_drive"
shutil.rmtree(out, ignore_errors=True)
os.makedirs(out)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
pool = json.load(open(f"{run}/04-pool/pool.json"))
m = pool["meta"]
try:
    nodes = len(json.load(open(f"{run}/05-sitetree/sitetree.json"))["nodes"])
except Exception:
    nodes = "?"


def put(src, name):
    if os.path.exists(src):
        shutil.copy(src, f"{out}/{name}")
        return name
    print("  missing source:", src)


def pdf(html_path, name, open_details=False):
    src = html_path
    if open_details:
        t = open(html_path).read().replace("<details ", "<details open ").replace("<details>", "<details open>")
        src = f"{out}/_tmp.html"
        open(src, "w").write(t)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={out}/{name}", f"file://{os.path.abspath(src)}"], capture_output=True, timeout=120)
    if open_details:
        os.remove(src)
    return name if os.path.exists(f"{out}/{name}") else None


names = []
readme = f"""# Content Pool: {m['client']}

Stand: {m['built']}. Interne Arbeitsunterlagen von 741. Nicht an die Kundin senden. Das Kundenformular (01) ist ein Entwurf.

Lies zuerst: 05-pool-bericht.pdf (Befunde, vier Säulen, Startseiten-Karte), dann 06-sitemap.pdf.

| Datei | Inhalt |
| --- | --- |
| _status.md | Lauf-Protokoll, ein Eintrag je Schritt. Zeigt den nächsten Schritt |
| 01-client-baseline.md | Echte Kundendaten, Quellen, [FEHLT]-Liste |
| 01-client-formular-de.md | Entwurf: offene Fragen an die Kundin (nicht gesendet) |
| 04-pool.json | Der Pool, maschinenlesbar (jedes Item mit Beleg-Dateien) |
| 04-pool-top.md | Startseiten-Items je CRO-Zeile, Eingabe für den Copy-Schritt |
| 04-pool-summary.json, 04-pool-candidates.json | Befunde und Urteile (Fit, HWG) hinter dem Pool |
| 05-pool-bericht.pdf / .html | Bericht (HTML: im Browser öffnen, mit Filter und Detail) |
| 05-pool.xlsx | Alle Pool-Items, filterbar |
| 06-sitemap.pdf / .html / .xlsx | Sitemap aus dem Pool, {nodes} Knoten |
| 06-sitetree.json, 06-sitetree-tree.json | Sitemap maschinenlesbar und Urteile |
| 07-rohdaten.zip | Rohdaten: Google-Ergebnisse, Wettbewerber-Messungen, Suchvolumen, Autocomplete, Search Console, Backlinks, Kosten-Log |

Methode: "741 Content-Pool-Raster". Spec im Repo: 00_project/content-pool-workflow.md.
"""
open(f"{out}/00-lies-mich.md", "w").write(readme)
names.append("00-lies-mich.md")
names.append(put(f"{run}/_status.md", "_status.md"))
names.append(put(f"{run}/01-client/client-baseline.md", "01-client-baseline.md"))
for f in glob.glob(f"{run}/01-client/client-form-*-de.md"):
    names.append(put(f, "01-client-formular-de.md"))
names.append(put(f"{run}/04-pool/pool.json", "04-pool.json"))
names.append(put(f"{run}/04-pool/pool-top.md", "04-pool-top.md"))
names.append(put(f"{run}/04-pool/summary.json", "04-pool-summary.json"))
names.append(put(f"{run}/04-pool/candidates.json", "04-pool-candidates.json"))
names.append(put(f"{run}/05-report/content-pool-report.html", "05-pool-bericht.html"))
names.append(pdf(f"{run}/05-report/content-pool-report.html", "05-pool-bericht.pdf", open_details=True))
names.append(put(f"{run}/05-report/content-pool.xlsx", "05-pool.xlsx"))
names.append(put(f"{run}/05-report/content-pool-sitetree.html", "06-sitemap.html"))
names.append(pdf(f"{run}/05-report/content-pool-sitetree.html", "06-sitemap.pdf"))
names.append(put(f"{run}/05-report/content-pool-sitetree.xlsx", "06-sitemap.xlsx"))
names.append(put(f"{run}/05-sitetree/sitetree.json", "06-sitetree.json"))
names.append(put(f"{run}/05-sitetree/tree.json", "06-sitetree-tree.json"))
with zipfile.ZipFile(f"{out}/07-rohdaten.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for d in ("02-competitors", "03-demand"):
        for root, _, files in os.walk(f"{run}/{d}"):
            for fn in files:
                if fn.startswith(".") or "payload" in fn: continue
                p = os.path.join(root, fn)
                z.write(p, os.path.relpath(p, run))
    for f in ("05-sitetree/own-metrics.json", "05-sitetree/own-urls.txt", "spend.jsonl"):
        if os.path.exists(f"{run}/{f}"): z.write(f"{run}/{f}", f)
names.append("07-rohdaten.zip")
names = [n for n in names if n]
man = {n: os.path.getsize(f"{out}/{n}") for n in names}
json.dump(man, open(f"{out}/MANIFEST.json", "w"), indent=1)
print(len(names), "files,", round(sum(man.values()) / 1e6, 2), "MB ->", out)
for n, s in man.items(): print(f"  {s:>9}  {n}")
