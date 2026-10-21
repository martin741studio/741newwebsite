#!/usr/bin/env python3
"""
verify_pitch.py - Deterministic verification linter for 741 Sales Pitch Architecture.

Offer version: 2026-10-21 (two packages, source of truth = live growth page
04_site/pages/growth-plan-de.html, section "Zwei Wege, mit uns zu arbeiten").

Enforces:
1. No prohibited third-party guru or author names (Hormozi, Miner, Voss, Keenan, Klaff).
2. Required 6 chronological call phases present, each with its own Markdown heading.
3. Both package prices present (7.999 €, 4.999 €).
4. No retired offer items (Starter / 1.999 €, 3.699 €, 5.549 €, 8.888 €, -10 % discount, struck-through prices).
5. Anchor order in Phase 4: Power Engine 7.999 € before the 4.999 € price.
6. Value stack in Phase 4: Gesamtwert 15.000 € stated before the 4.999 € price.
7. Ergebnis-Garantie (Top 3 Google Maps, ohne Zusatzkosten weiter) stated in Phase 4 before the 4.999 € price.
8. Bonuses present: Sichtbarkeits-Schutz 397 €, Sofort-Start 48 Stunden.
9. Payment: full payment on day one + fallback 60 %.
10. Referral ask (Foto + Kollegen) in Phase 6, after the buying decision; Gebietsschutz named.
"""

import re
import sys

FORBIDDEN_TERMS = ["hormozi", "alex hormozi", "jeremy miner", "nepq", "chris voss", "keenan", "gap selling", "oren klaff", "pitch anything"]
REQUIRED_PHASES = ["Phase 1", "Phase 2", "Phase 3", "Phase 4", "Phase 5", "Phase 6"]
REQUIRED_PRICES = ["7.999", "4.999"]
RETIRED_PATTERNS = [
    (r"1\.999", "Starter price 1.999 € (not sold by phone since 2026-10-21)"),
    (r"\bStarter\b", "Starter package (not sold by phone since 2026-10-21)"),
    (r"3\.699", "old core price 3.699 €"),
    (r"5\.549", "old struck-through list price 5.549 €"),
    (r"8\.888", "old struck-through list price 8.888 €"),
    (r"[−-]\s?10\s?%", "-10 % discount"),
    (r"Kennenlern-Rabatt", "Kennenlern-Rabatt"),
    (r"~~[^~\n]*€[^~\n]*~~", "struck-through price"),
    (r"<s>|<del>|durchgestrichen", "struck-through price"),
    (r"Geld zurück", "money-back promise (the guarantee is: work on at no extra cost)"),
]
GUARANTEE_RE = re.compile(r"Top[ -]?3.{0,120}?ohne Zusatzkosten weiter", re.S)


def section(content: str, n: int) -> str:
    """Text from the Markdown heading of phase n up to the next phase heading."""
    m = re.search(rf"^#+[^\n]*Phase {n}\b[^\n]*$", content, re.M)
    if not m:
        return ""
    nxt = re.search(r"^#+[^\n]*Phase \d\b[^\n]*$", content[m.end():], re.M)
    return content[m.end(): m.end() + nxt.start()] if nxt else content[m.end():]


def verify_file(filepath: str) -> bool:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"ERROR: Cannot read file {filepath}: {e}")
        return False

    errors = []
    lower_content = content.lower()

    # 1. Forbidden guru names
    for term in FORBIDDEN_TERMS:
        if term in lower_content:
            errors.append(f"Found forbidden guru term '{term}' in brief. Use internal 741 terminology only.")

    # 2. Six phases, each with a heading
    for i, phase in enumerate(REQUIRED_PHASES, 1):
        if phase not in content:
            errors.append(f"Missing required phase '{phase}' in call structure.")
        elif not section(content, i).strip():
            errors.append(f"'{phase}' has no Markdown heading (or an empty section).")

    # 3. Both package prices
    for price in REQUIRED_PRICES:
        if price not in content:
            errors.append(f"Missing package price '{price} €' in offer presentation.")

    # 4. Retired offer items
    for pattern, label in RETIRED_PATTERNS:
        if re.search(pattern, content):
            errors.append(f"Retired offer item found: {label}.")

    p4 = section(content, 4)
    p6 = section(content, 6)
    pos_core = p4.find("4.999")

    # 5. Anchor order: Power Engine 7.999 € first
    pos_power = p4.find("7.999")
    if pos_power < 0 or pos_core < 0 or pos_power > pos_core:
        errors.append("Phase 4 must name the Power Engine 7.999 € before the 4.999 € price (anchor first).")

    # 6. Value stack before the price
    pos_value = p4.find("15.000")
    if pos_value < 0 or pos_core < 0 or pos_value > pos_core:
        errors.append("Phase 4 must state the value stack (Gesamtwert 15.000 €) before the 4.999 € price.")

    # 7. Guarantee before the price
    g = GUARANTEE_RE.search(p4)
    if not g or pos_core < 0 or g.start() > pos_core:
        errors.append("Phase 4 must state the Ergebnis-Garantie ('Top 3 ... ohne Zusatzkosten weiter') before the 4.999 € price.")

    # 8. Bonuses
    if "397" not in content or "Sichtbarkeits-Schutz" not in content:
        errors.append("Missing bonus '1 Monat Sichtbarkeits-Schutz gratis (Wert 397 €)'.")
    if not re.search(r"48\s?(Stunden|h)\b", content):
        errors.append("Missing Sofort-Start bonus (Kick-off innerhalb von 48 Stunden).")

    # 9. Payment terms
    if not re.search(r"vollen Betrag|volle[rn]? Zahlung|Vollzahlung", content):
        errors.append("Missing default payment (voller Betrag am ersten Tag).")
    if not re.search(r"60\s?%", content):
        errors.append("Missing payment fallback (60 % am ersten Tag, Rest in bis zu zwei Zahlungen).")

    # 10. Referral ask after the yes + Gebietsschutz
    if "Foto" not in p6 or "Kollegen" not in p6:
        errors.append("Phase 6 must hold the referral ask (Foto + zwei Kollegen) after the buying decision.")
    if "Foto" in section(content, 4) + section(content, 5):
        errors.append("Referral photo ask appears before Phase 6. Ask for referrals only after the yes.")
    if "Gebietsschutz" not in content and "nur einen Betrieb" not in content:
        errors.append("Missing Gebietsschutz (Pro Ort nur ein Betrieb deiner Fachrichtung).")

    if errors:
        print("VERIFICATION FAILED:")
        for err in errors:
            print(f"  ✗ {err}")
        return False

    print("VERIFICATION PASSED: All 10 invariant checks succeeded.")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 verify_pitch.py <path-to-sales-cockpit.md>")
        sys.exit(1)

    success = verify_file(sys.argv[1])
    sys.exit(0 if success else 1)
