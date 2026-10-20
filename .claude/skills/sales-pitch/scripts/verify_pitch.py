#!/usr/bin/env python3
"""
verify_pitch.py - Deterministic verification linter for 741 Sales Pitch Architecture.

Enforces:
1. No prohibited third-party guru or author names in prospect-facing cockpit (Hormozi, Miner, Voss, Keenan, Klaff).
2. Required 6 chronological call phases (Min 00-05 to Min 55-60) present.
3. 3-Tier Offer Stack exact figures present (1.999 €, 3.699 €, 7.999 €).
4. Performance Guarantee explicit phrasing present.
"""

import sys
import re

FORBIDDEN_TERMS = ["hormozi", "alex hormozi", "jeremy miner", "nepq", "chris voss", "keenan", "gap selling", "oren klaff", "pitch anything"]
REQUIRED_PHASES = ["Phase 1", "Phase 2", "Phase 3", "Phase 4", "Phase 5", "Phase 6"]
REQUIRED_PRICES = ["1.999", "3.699", "7.999"]
REQUIRED_GUARANTEE_TOKENS = ["Garantie", "kostenlos weiter", "Geld zurück"]

def verify_file(filepath: str) -> bool:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"ERROR: Cannot read file {filepath}: {e}")
        return False

    errors = []
    lower_content = content.lower()

    # 1. Check for forbidden guru names
    for term in FORBIDDEN_TERMS:
        if term in lower_content:
            errors.append(f"Found forbidden guru term '{term}' in brief. Use internal 741 terminology only.")

    # 2. Check for required phases
    for phase in REQUIRED_PHASES:
        if phase not in content:
            errors.append(f"Missing required phase '{phase}' in call structure.")

    # 3. Check for 3-tier price anchors
    for price in REQUIRED_PRICES:
        if price not in content:
            errors.append(f"Missing required price tier '{price} €' in offer presentation.")

    # 4. Check for guarantee phrasing
    guarantee_found = any(token in content for token in REQUIRED_GUARANTEE_TOKENS)
    if not guarantee_found:
        errors.append("Missing explicit 741 performance guarantee phrasing.")

    if errors:
        print("VERIFICATION FAILED:")
        for err in errors:
            print(f"  ✗ {err}")
        return False

    print("VERIFICATION PASSED: All 4 invariant checks succeeded.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 verify_pitch.py <path-to-sales-cockpit.md>")
        sys.exit(1)

    success = verify_file(sys.argv[1])
    sys.exit(0 if success else 1)
