#!/usr/bin/env python3
"""
Build the client's Backlink-Ziele Google Sheet (xlsx, converts on Drive upload).
Replaces the hand-written code rebuilt from scratch 4 times on the Hüwel pilot (v1-v4).

Writes with XlsxWriter, never openpyxl: openpyxl output with fills, data validation or
freeze panes fails Drive's xlsx->Sheets conversion ("Invalid conversion requested",
11.10.2026; house rule in memory well-designed-sheets.md).

Run (no venv needed, uv fetches XlsxWriter):
    uv run --with xlsxwriter python3 build_sheet.py --title "Backlink-Ziele — Praxis Hüwel" --rows rows.csv --out sheet.xlsx

rows.csv columns (header row required):
    n,domain,saeule,taktik,rank,kosten,quelle,kontakt,status,freigabe

Validates before writing (fix the input until it passes, never bypass):
- every row needs a non-empty Quelle and Kontakt,
- Säule must be one of B, C, D, E, B/D. Pillar A (also niche directories such as jameda,
  Doctolib, theralupa) belongs to the Citations module since 2026-10-13 and is refused here,
- Status must be a known value.
- rank: DataForSEO rank or blank; shown as "DR (approx.)" = round(min(rank/10,100)).
- freigabe: "ja"/"✓"/"TRUE" -> ☑, anything else -> ☐, "-" -> no dropdowns (placeholder row).
"""
import argparse
import csv
import sys

try:
    import xlsxwriter
except ImportError:
    sys.exit("XlsxWriter fehlt. Starte mit: uv run --with xlsxwriter python3 build_sheet.py ...")

VALID_SAEULE = {"B", "C", "D", "E", "B/D"}
PILLAR_A = {"A", "A-niche", "A-Nische"}
VALID_STATUS = ["identified", "contacted", "replied", "agreed", "live", "lost",
                "rejected", "braucht Recherche"]
HEADERS = ["#", "Domain", "Säule", "Taktik", "DR (approx.)", "Kosten", "Quelle", "Kontakt", "Status", "Freigabe"]
WIDTHS = [4, 32, 7, 36, 8, 18, 28, 34, 16, 9]
WRAP_COLS = {3, 6, 7}  # 0-based: Taktik, Quelle, Kontakt
HEADER_ROW = 3          # 0-based row index (Excel row 4)
FILLS = {"green": "#D9F2D0", "grey": "#F2F2F2", "yellow": "#FFF3C4"}


def dr(rank):
    if rank in (None, "", "–", "-"):
        return "–"
    try:
        return round(min(float(rank) / 10, 100))
    except ValueError:
        return "–"


def norm_freigabe(v):
    if str(v).strip() in ("-", "–", ""):
        return "–" if str(v).strip() in ("-", "–") else "☐"
    return "☑" if str(v).strip().lower() in ("ja", "yes", "true", "✓", "☑") else "☐"


def validate(rows):
    errors = []
    for r in rows:
        n = r.get("n", "?")
        dom = r.get("domain")
        if not r.get("quelle", "").strip():
            errors.append(f"Zeile {n} ({dom}): Quelle fehlt — jede Zeile braucht eine Quelle.")
        if not r.get("kontakt", "").strip():
            errors.append(f"Zeile {n} ({dom}): Kontakt fehlt — nie leer lassen, lieber 'noch zu prüfen'.")
        s = r.get("saeule", "")
        if s in PILLAR_A:
            errors.append(f"Zeile {n} ({dom}): Säule A gehört ins Citations-Modul (Grenze 2026-10-13). "
                          "Zeile raus und als Übergabe an das Citations-Modul melden.")
        elif s not in VALID_SAEULE:
            errors.append(f"Zeile {n} ({dom}): Säule '{s}' ist kein bekannter Wert ({sorted(VALID_SAEULE)}).")
        if r.get("status") not in VALID_STATUS:
            errors.append(f"Zeile {n} ({dom}): Status '{r.get('status')}' ist kein bekannter Wert ({VALID_STATUS}).")
    return errors


def row_fill(row, freigabe):
    if freigabe == "☑":
        return "green"
    if row["status"] == "braucht Recherche":
        return "grey"
    k = row.get("kosten", "")
    if "unbekannt" in k.lower() or "Mitgliedsbeitrag" in k:
        return "yellow"
    return None


def build(title, rows, out_path, stand=""):
    wb = xlsxwriter.Workbook(out_path)
    ws = wb.add_worksheet("Ziele")
    base = {"font_name": "Arial", "font_size": 10, "border": 1, "border_color": "#D0D0D0", "valign": "vcenter"}
    fmt = {}
    for fill in (None, *FILLS):
        for wrap in (False, True):
            d = dict(base, text_wrap=wrap)
            if fill:
                d["bg_color"] = FILLS[fill]
            fmt[(fill, wrap)] = wb.add_format(d)
    title_f = wb.add_format({"font_name": "Arial", "font_size": 14, "bold": True, "font_color": "#1A3C34"})
    sub_f = wb.add_format({"font_name": "Arial", "font_size": 9, "italic": True, "font_color": "#666666"})
    head_f = wb.add_format({"font_name": "Arial", "font_size": 10, "bold": True, "font_color": "#FFFFFF",
                            "bg_color": "#1A3C34", "align": "center", "valign": "vcenter", "text_wrap": True, "border": 1})

    ws.write(0, 0, title, title_f)
    ws.write(1, 0, stand or "DR (approx.) = round(min(Rank/10,100)) aus DataForSEO, keine offizielle DR-Zahl. "
                            "Jede Zeile hat Quelle + Kontakt. Branchenverzeichnisse (Säule A) laufen im Citations-Modul.", sub_f)
    ws.set_row(HEADER_ROW, 28)
    for i, h in enumerate(HEADERS):
        ws.write(HEADER_ROW, i, h, head_f)
    for i, w in enumerate(WIDTHS):
        ws.set_column(i, i, w)

    r = HEADER_ROW + 1
    for row in rows:
        freigabe = norm_freigabe(row.get("freigabe", ""))
        vals = [row["n"], row["domain"], row["saeule"], row["taktik"], dr(row.get("rank")),
                row["kosten"], row["quelle"], row["kontakt"], row["status"], freigabe]
        fill = row_fill(row, freigabe)
        for i, v in enumerate(vals):
            if i == 0 and str(v).isdigit():
                v = int(v)
            ws.write(r, i, v, fmt[(fill, i in WRAP_COLS)])
        if freigabe != "–":
            ws.data_validation(r, 8, r, 8, {"validate": "list", "source": VALID_STATUS})
            ws.data_validation(r, 9, r, 9, {"validate": "list", "source": ["☐", "☑"]})
        r += 1

    ws.freeze_panes(HEADER_ROW + 1, 0)
    ws.write(r + 1, 0, "Legende: 🟩 freigegeben · 🟨 bedingt (Kosten klären) · ⬜ braucht Recherche", sub_f)
    wb.close()
    return r - HEADER_ROW - 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--rows", required=True, help="CSV with header row")
    ap.add_argument("--out", required=True)
    ap.add_argument("--stand", default="")
    args = ap.parse_args()

    with open(args.rows, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    errors = validate(rows)
    if errors:
        print(f"{len(errors)} Zeile(n) nicht bereit für das Sheet:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        print("\nFix die Eingabe, dann nochmal laufen lassen. Kein Sheet geschrieben.", file=sys.stderr)
        sys.exit(1)

    n = build(args.title, rows, args.out, args.stand)
    print(f"OK — {n} Zeilen geschrieben nach {args.out}. Jede Zeile hat Quelle + Kontakt, keine Säule-A-Zeile (geprüft).")
    print("Nächster Schritt: über die Drive-MCP create_file hochladen (xlsx→Sheets-Konvertierung, disableConversionToGoogleType NICHT setzen), dann in Chrome öffnen und per Screenshot verifizieren (nie ungeprüft als fertig melden).")


if __name__ == "__main__":
    main()
