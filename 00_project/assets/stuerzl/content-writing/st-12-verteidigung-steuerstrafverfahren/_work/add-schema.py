#!/usr/bin/env python3
"""Ergänzt schema.jsonld um Person (Dr. Stürzl) und Service. Läuft NACH `schema_tool.py make` (run_gates.py ruft make auf und überschreibt die Datei).

    python3 _work/add-schema.py <run_dir>

Nur belegte Daten aus assets/stuerzl/nap.json und dem sichtbaren Text (H1, Abschnitt S05 nennt Namen und Titel).
Das Skript ist idempotent: vorhandene Person/Service-Knoten werden ersetzt.
"""
import json
import re
import sys
from pathlib import Path

run = Path(sys.argv[1]).resolve()
ROOT = Path("/Users/martindrendel/741website")
brief = json.loads((run / "01-brief/brief.json").read_text(encoding="utf-8"))
nap = json.loads((ROOT / brief["nap_file"]).read_text(encoding="utf-8"))
page = (run / "05-final/page.md").read_text(encoding="utf-8")
h1 = re.search(r"(?m)^#\s+(.+)$", page).group(1).strip()
base = nap["base_url"]
url = base + brief["url_slug"]
org_id = base + "/" + nap["organization"]["id"]
p = nap["people"]["dr-anja-stuerzl"]
purl = base + p["url_slug"]
schema_f = run / "05-final/schema.jsonld"
doc = json.loads(schema_f.read_text(encoding="utf-8"))
g = [x for x in doc["@graph"] if x.get("@type") not in ("Person", "Service")]
g.append({
    "@type": "Person", "@id": purl + "#person", "name": p["name"], "jobTitle": p["jobTitle"], "url": purl,
    "worksFor": {"@id": org_id},
    "hasCredential": [{"@type": "EducationalOccupationalCredential", "name": c} for c in p["credentials"]],
})
g.append({
    "@type": "Service", "@id": url + "#service", "name": h1, "url": url,
    "serviceType": brief.get("service_type") or "Rechtsberatung im Steuerstrafrecht",
    "provider": {"@id": org_id},
    "areaServed": {"@type": "Country", "name": "Deutschland"},
    "mainEntityOfPage": {"@id": url + "#webpage"},
})
doc["@graph"] = g
schema_f.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", [x["@type"] for x in g])
