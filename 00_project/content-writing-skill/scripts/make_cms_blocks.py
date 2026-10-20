#!/usr/bin/env python3
"""Make the CMS plain-text blocks from the Markdown master (no HTML, no Markdown).

    python3 make_cms_blocks.py page.md > cms-blocks.txt

One block per section: "=== S01 | hero | headline ===". Fields: Titel, Text, Button, Frage/Antwort, Links.
Placeholders stay visible in square brackets. The TECH block is not exported.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import TECH_MARK, strip_frontmatter  # noqa: E402


def plain(line):
    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", line)
    line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
    line = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
    line = line.replace("`", "")
    return line.strip(), links


def main():
    raw = Path(sys.argv[1]).read_text(encoding="utf-8")
    body = strip_frontmatter(raw).split(TECH_MARK, 1)[0]
    out = []
    for m in re.finditer(r"<!--\s*(S\d\d)\s+([\w-]+)\s*\|([^>]*?)-->(.*?)<!--\s*/\1\s*-->", body, flags=re.S):
        sid, name, meta, content = m.groups()
        content = re.sub(r"<!--.*?-->", "", content, flags=re.S)
        out.append(f"=== {sid} | {name} | {meta.strip()} ===")
        links_all, lines, q = [], [], None
        for ln in content.strip().splitlines():
            if not ln.strip() or re.match(r"^\|\s*-+", ln):
                lines.append("")
                continue
            h = re.match(r"^(#{1,3})\s+(.*)$", ln)
            txt, links = plain(h.group(2) if h else ln)
            links_all += links
            if h and len(h.group(1)) == 3:
                lines.append(f"Frage: {txt}")
                q = True
                continue
            if h:
                lines.append(f"Titel: {txt}")
                continue
            if re.match(r"^\s*\|", ln):
                lines.append(" | ".join(c.strip() for c in txt.strip("|").split("|")))
                continue
            if re.match(r"^\s*[-*]\s+", ln):
                lines.append("• " + re.sub(r"^\s*[-*]\s+", "", txt))
                continue
            if re.match(r"^\s*\d+\.\s+", ln):
                lines.append(txt)
                continue
            if ln.strip().startswith("**") and ln.strip().endswith("**") and len(ln.strip()) < 60:
                lines.append(f"Button: {txt}")
                continue
            lines.append(("Antwort: " if q else "Text: ") + txt)
            q = None
        text = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()
        out.append(text)
        if links_all:
            out.append("Links: " + "; ".join(f"{a} -> {u}" for a, u in links_all))
        out.append("")
    if not out:
        print("make_cms_blocks: no sections found", file=sys.stderr)
        return 1
    print("\n".join(out).strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
