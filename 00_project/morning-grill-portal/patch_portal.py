#!/usr/bin/env python3
"""Add / update the Command Center (Morning Grill) in the portal index.html. Anchor-based and idempotent.
Usage: python3 patch_portal.py <in.html> <out.html>
Always run on a FRESH pull of the target file (live or staging). It never touches the block between the markers
'Entscheidungen (Kunden-Freigabe)' and 'Ende Entscheidungen' (Freigabe chat); it inserts its own blocks after it.
Stops with an error if an anchor is missing or ambiguous."""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSS_B, CSS_E = "/* ---------- Command Center (Morning Grill) BEGIN ---------- */", "/* ---------- Command Center (Morning Grill) END ---------- */"
JS_B, JS_E = "/* ---------- Command Center (Morning Grill) BEGIN ---------- */", "/* ---------- Command Center (Morning Grill) END ---------- */"
END_ENT = "/* ---------- Ende Entscheidungen ---------- */"


def die(m):
    sys.exit("PATCH STOPPED: " + m)


def once(s, needle, what):
    n = s.count(needle)
    if n != 1:
        die(f"anchor '{what}' found {n} times (expected 1)")


def main():
    src, dst = sys.argv[1], sys.argv[2]
    s = open(src, encoding="utf-8").read()
    css = open(os.path.join(HERE, "cc-block.css"), encoding="utf-8").read().rstrip("\n")
    js = open(os.path.join(HERE, "cc-block.js"), encoding="utf-8").read().rstrip("\n")
    css_blk = f"\n  {CSS_B}\n{css}\n  {CSS_E}\n"
    js_blk = f"\n{JS_B}\n{js}\n{JS_E}\n"
    if CSS_B in s:  # update mode: replace both blocks (CSS first, JS second occurrence of the marker)
        parts = s.split(CSS_B)
        if len(parts) != 3:
            die("expected the BEGIN marker twice (CSS + JS)")
        def after_end(chunk, end):
            return chunk[chunk.index(end) + len(end):]
        s = (parts[0] + CSS_B + "\n" + css + "\n  " + CSS_E + after_end(parts[1], CSS_E)
             + JS_B + "\n" + js + "\n" + JS_E + after_end(parts[2], JS_E))
    else:
        ends = [m.start() for m in re.finditer(re.escape(END_ENT), s)]
        if len(ends) != 2:
            die(f"'Ende Entscheidungen' marker found {len(ends)} times (expected 2: CSS and JS)")
        css_at = ends[0] + len(END_ENT)
        js_at = ends[1] + len(END_ENT)
        if "</style>" not in s[css_at:css_at + 4000] and s.rfind("<style", 0, css_at) < 0:
            die("first 'Ende Entscheidungen' is not inside a <style> block")
        s = s[:js_at] + js_blk + s[js_at:]   # JS first (later offset) so the CSS offset stays valid
        s = s[:css_at] + css_blk + s[css_at:]
    if 'id="grill"' not in s:
        once(s, '<div id="newsletter" class="container hidden"></div>', "newsletter container")
        s = s.replace('<div id="newsletter" class="container hidden"></div>', '<div id="newsletter" class="container hidden"></div>\n  <div id="grill" class="container hidden"></div>')
    if 'id="btn-grill"' not in s:
        needle = "onclick=\"showApp('newsletter');loadNewsletter()\">→ Newsletter</button>"
        once(s, needle, "newsletter button")
        s = s.replace(needle, needle + "\n      <button id=\"btn-grill\" class=\"btn btn-small btn-yellow\" style=\"margin-left:8px;display:none;\" onclick=\"showApp('grill');loadGrill()\">→ Command Center</button>")
    if "'newsletter','grill']" not in s:
        once(s, "'metaads','newsletter']", "showApp list")
        s = s.replace("'metaads','newsletter']", "'metaads','newsletter','grill']")
    if "const gb = $('btn-grill')" not in s:
        needle = "async function loadAdminHome() {"
        once(s, needle, "loadAdminHome")
        s = s.replace(needle, needle + "\n  { const gb = $('btn-grill'); if (gb) gb.style.display = (me && me.role === 'admin') ? '' : 'none'; }")
    open(dst, "w", encoding="utf-8").write(s)
    print(f"patched: {len(s)} bytes ({len(s) - len(open(src, encoding='utf-8').read()):+d})")


if __name__ == "__main__":
    main()
