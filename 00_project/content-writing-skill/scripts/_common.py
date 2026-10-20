"""Shared helpers for the content-writing scripts. Read-only text tools, no network."""
import html as _html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REFS = HERE.parent / "references"
TECH_MARK = "<!-- TECH -->"
PLACEHOLDER_RE = re.compile(r"\[von Kunde bestätigen:[^\]]*\]")
FEHLT_RE = re.compile(r"\[FEHLT[^\]]*\]")


def read_input(path=None, text=None):
    if text is not None:
        return text
    if path in (None, "-"):
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def strip_frontmatter(s):
    if s.startswith("---\n"):
        end = s.find("\n---", 4)
        if end != -1:
            return s[end + 4:].lstrip("\n")
    return s


def frontmatter(s):
    """Parse a flat `key: value` frontmatter block. No nesting needed."""
    out = {}
    if s.startswith("---\n"):
        end = s.find("\n---", 4)
        if end != -1:
            for line in s[4:end].splitlines():
                if ":" in line and not line.startswith(" "):
                    k, v = line.split(":", 1)
                    out[k.strip()] = v.strip().strip('"')
    return out


def visible_text(s, keep_placeholders=False):
    """Text a reader sees: no frontmatter, no technical block, no comments, no markup."""
    s = strip_frontmatter(s)
    if TECH_MARK in s:
        s = s.split(TECH_MARK, 1)[0]
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    s = re.sub(r"<(script|style)\b.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = _html.unescape(s)
    if not keep_placeholders:
        s = PLACEHOLDER_RE.sub(" ", s)
        s = FEHLT_RE.sub(" ", s)
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", s)          # images
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)       # links keep their label
    s = re.sub(r"^\s{0,3}#{1,6}\s*", "", s, flags=re.M)  # heading marks
    s = re.sub(r"^\s*[-*]\s+", "", s, flags=re.M)        # bullets
    s = re.sub(r"[*_`>|]", " ", s)
    s = re.sub(r"[ \t]+", " ", s)
    return s.strip()


def sentences(s):
    parts = re.split(r"(?<=[.!?])\s+|\n{2,}|\n", s)
    return [p.strip() for p in parts if len(p.split()) >= 1 and p.strip()]


def words(s):
    return re.findall(r"[A-Za-zÄÖÜäöüß0-9][A-Za-zÄÖÜäöüß0-9'’\-]*", s)


def load_json(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def numbers(s):
    return re.findall(r"\d[\d.,]*\d|\d", s)


def detect_lang(s):
    low = " " + s.lower() + " "
    de = sum(low.count(w) for w in (" und ", " der ", " die ", " das ", " nicht ", " ist ", " ein ", " mit ", " für ", " sie "))
    en = sum(low.count(w) for w in (" and ", " the ", " is ", " of ", " to ", " with ", " for ", " you ", " that ", " are "))
    return "de" if de >= en else "en"
