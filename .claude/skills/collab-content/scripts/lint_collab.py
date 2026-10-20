#!/usr/bin/env python3
"""
741 Co-Marketing & Backlink Collaboration Linter (scripts/lint_collab.py).
Validates editorial article drafts for:
1. Hard Plain-Text Rule (Zero raw HTML tags in client-editable CMS text).
2. YMYL / Medical Policy Compliance (No forbidden disease cure claims).
3. Backlink Integrity (Valid URLs, contextual anchors, no naked URL spam).
"""

import sys
import re
import os

HTML_TAG_PATTERN = re.compile(r'<\/?(?:span|div|p|br|table|tr|td|style|script|font|b|i|strong|em)[^>]*>', re.IGNORECASE)
INLINE_STYLE_PATTERN = re.compile(r'style\s*=\s*["\'][^"\']*["\']', re.IGNORECASE)
MD_LINK_PATTERN = re.compile(r'\[([^\]]+)\]\((https?:\/\/[^\)]+)\)')

FORBIDDEN_YMYL_TERMS = [
    r'\bcures?\s+(?:cancer|diabetes|disease|all\s+illness)\b',
    r'\bguaranteed\s+(?:cure|healing|result)\b',
    r'\beradicates?\s+(?:disease|infection)\b',
    r'\b100%\s+(?:cure|effective|safe)\b',
    r'\bmedical\s+miracle\b'
]

def lint_file(file_path):
    if not os.path.exists(file_path):
        return [f"File not found: {file_path}"]
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    errors = []
    
    # 1. Plain-text HTML Tag Check
    html_tags = HTML_TAG_PATTERN.findall(content)
    if html_tags:
        errors.append(f"Forbidden raw HTML tags detected ({len(html_tags)} instances): {set(html_tags)}")
        
    styles = INLINE_STYLE_PATTERN.findall(content)
    if styles:
        errors.append(f"Forbidden inline styles detected ({len(styles)} instances)")
        
    # 2. YMYL / Medical Claim Check
    for pattern in FORBIDDEN_YMYL_TERMS:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            errors.append(f"YMYL compliance violation: Found forbidden health claim pattern '{pattern}': {matches}")
            
    # 3. Backlink Check
    links = MD_LINK_PATTERN.findall(content)
    if not links:
        errors.append("No valid contextual Markdown backlinks found in article.")
    else:
        for anchor, url in links:
            if anchor.strip().lower() in ["click here", "here", "read more", "link", "website"]:
                errors.append(f"Low-quality generic anchor text detected: '[{anchor}]({url})'")
            if len(anchor.strip()) < 3:
                errors.append(f"Anchor text too short: '[{anchor}]({url})'")
                
    return errors

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 lint_collab.py <file1.md> [<file2.md> ...]")
        sys.exit(1)
        
    all_clean = True
    for path in sys.argv[1:]:
        print(f"\n[LINT] Scanning: {path}")
        errors = lint_file(path)
        if errors:
            all_clean = False
            print(f"❌ FAIL: {len(errors)} issues found:")
            for err in errors:
                print(f"   • {err}")
        else:
            print("✅ PASS: 0 HTML tags, clean plain-text, YMYL compliant, valid backlinks.")
            
    if not all_clean:
        sys.exit(1)
    print("\nAll articles passed collaboration linter checks.")

if __name__ == "__main__":
    main()
