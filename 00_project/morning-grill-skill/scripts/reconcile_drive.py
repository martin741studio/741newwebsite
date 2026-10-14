#!/usr/bin/env python3
"""Reconcile NAP (name/address/phone) between Supabase and a client's Drive Source-of-Truth-Sheet
(goals-data-architecture, Phase C, folded in 2026-10-15). Read only on both sides. Never picks a
winner — emits one flagged item per disagreement, for a grill decision card.

Needs: 00_project/.secrets/ga-sc-reporting-bot.json (service account, already used for GSC exports)
shared on the Drive Source-of-Truth-Sheet as a Viewer (already true for Stuerzl, confirmed live
2026-10-15). Needs the FRAMEWORK python (has google-api-python-client):
  /Library/Frameworks/Python.framework/Versions/3.10/bin/python3 reconcile_drive.py [--client NAME]

Scope for this build: NAP only (name/address/phone). Wider fields (pricing, contract terms) are a
later slice once this one proves out (R1.3).
"""
import argparse, json, os, re, sys, urllib.parse

# The framework python (needed for google-api-python-client) has no system CA bundle wired up by
# default, which breaks sb.py's plain urllib call to Supabase with SSL_CERT_VERIFY_FAILED. Point it
# at certifi's bundle before any HTTPS call happens.
try:
    import certifi
    os.environ.setdefault("SSL_CERT_FILE", certifi.where())
except ImportError:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sb  # noqa: E402

REPO = os.environ.get("MG_REPO", "/Users/martindrendel/741website")
SHEETS_CFG = os.path.join(REPO, "00_project", "morning-grill-skill", "assets", "reconcile-sheets.json")
SA_KEY = os.path.join(REPO, ".secrets", "ga-sc-reporting-bot.json")


def sheets_service():
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    creds = service_account.Credentials.from_service_account_file(
        SA_KEY, scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]
    )
    return build("sheets", "v4", credentials=creds)


def read_nap_tab(svc, sheet_id, tab):
    res = svc.spreadsheets().values().get(spreadsheetId=sheet_id, range=f"'{tab}'!A1:G40").execute()
    rows = res.get("values", [])
    header_line = rows[0][0] if rows and rows[0] else ""
    soll = None
    m = re.search(r"Soll-Adresse:\s*([^(]+?)(?:\s*\(([^)]*)\))?\s*$", header_line)
    if m:
        soll = {"address": m.group(1).strip(), "note": (m.group(2) or "").strip()}
    gbp_rows = []
    for r in rows:
        if len(r) >= 4 and "Google-Unternehmensprofil" in (r[0] or ""):
            gbp_rows.append({"label": r[0], "address_shown": r[3], "status": r[5] if len(r) > 5 else ""})
    return {"header": header_line, "soll_adresse": soll, "gbp_rows": gbp_rows}


def read_supabase_nap(client_name):
    q = urllib.parse.quote(client_name)
    clients = sb.request("GET", f"clients?select=id,name&name=eq.{q}")
    if not clients:
        return None, f"no Supabase client named '{client_name}'"
    cid = clients[0]["id"]
    locs = sb.request("GET", f"locations?select=label,street,zip,city,is_primary&client_id=eq.{cid}")
    primary = next((l for l in locs if l.get("is_primary")), (locs[0] if locs else None))
    return {"locations": locs, "primary": primary}, None


def normalize(addr):
    """Compare street + postcode only. City suffixes differ between sources ('Frankfurt' vs
    'Frankfurt am Main'); a street or postcode difference is the real disagreement."""
    a = (addr or "").strip().lower().replace("straße", "str.")
    street = a.split(",")[0].strip()
    zip_m = re.search(r"\b(\d{5})\b", a)
    return (re.sub(r"\s+", " ", street), zip_m.group(1) if zip_m else "")


def reconcile(client_name, cfg):
    svc = sheets_service()
    drive = read_nap_tab(svc, cfg["sheet_id"], cfg.get("nap_tab", "11 Citations & NAP"))
    supa, err = read_supabase_nap(client_name)
    flags = []
    if err:
        return [{"client": client_name, "field": "nap", "flag": "no_supabase_client", "detail": err}]
    supa_addr = f"{supa['primary']['street']}, {supa['primary']['zip']} {supa['primary']['city']}" if supa.get("primary") else None
    if not supa_addr:
        flags.append({"client": client_name, "field": "address", "flag": "missing_in_supabase", "drive": drive["soll_adresse"]})
    elif drive["soll_adresse"] and normalize(supa_addr) != normalize(drive["soll_adresse"]["address"]):
        flags.append({
            "client": client_name, "field": "address", "flag": "disagreement",
            "supabase_locations_street": supa_addr,
            "drive_soll_adresse": drive["soll_adresse"]["address"],
            "drive_soll_note": drive["soll_adresse"]["note"],
        })
    for g in drive["gbp_rows"]:
        if supa_addr and normalize(g["address_shown"]) != normalize(supa_addr) and "alt" in (g["status"] or "").lower():
            flags.append({
                "client": client_name, "field": "address", "flag": "gbp_row_marked_stale_in_sheet",
                "sheet_label": g["label"], "sheet_address_shown": g["address_shown"], "sheet_status": g["status"],
                "supabase_locations_street": supa_addr,
            })
    if not flags:
        flags.append({"client": client_name, "field": "address", "flag": "ok", "note": "Supabase locations matches the Drive Soll-Adresse"})
    return flags


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--client")
    a = ap.parse_args()
    if not os.path.exists(SHEETS_CFG):
        print(f"no {SHEETS_CFG} — nothing configured yet, add a client there first"); return 0
    cfg_all = json.load(open(SHEETS_CFG, encoding="utf-8"))
    clients = [a.client] if a.client else list(cfg_all.keys())
    out = []
    for name in clients:
        if name not in cfg_all:
            print(f"WARNING: {name} not in {SHEETS_CFG}"); continue
        out.extend(reconcile(name, cfg_all[name]))
    print(json.dumps(out, ensure_ascii=False, indent=1))
    disagreements = [f for f in out if f["flag"] not in ("ok",)]
    print(f"\n{len(disagreements)} flagged item(s) out of {len(out)} checked — never auto-resolved, needs a grill card.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
