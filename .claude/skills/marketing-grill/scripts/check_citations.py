#!/usr/bin/env python3
"""Verify a drafted playbook has a non-empty Sources section, and that every
file it cites actually exists on disk (Step 2.5: the mechanical half of
enforcing `claims-need-real-data` -- never asserts the CONTENT is correct,
only that a citation is not pointing at nothing).

Usage:
  check_citations.py <playbook.md>

Exit 0 and prints "OK" if a "## Sources" section exists, has at least one
bullet, and every backtick-quoted `path/like/this.md` or `this.md` token in
that section resolves to a real file (relative to the repo root this script
is run from). Exit 1 with the problem otherwise.
"""
import os
import re
import sys

PATH_RE = re.compile(r'`([^`]+\.md)`')

# A bare filename (no "/") can live in any of these -- a citation only needs
# to resolve in ONE of them to count as real.
SEARCH_DIRS = [
    '.',
    os.path.expanduser('~/.claude/projects/-Users-martindrendel-741website/memory'),
    '00_project/workflow-builds/marketing-grill',
    '00_project/knowledge/hormozi-library/_derived',
]


def resolves(p):
    if '/' in p:
        return os.path.exists(p)
    return any(os.path.exists(os.path.join(d, p)) for d in SEARCH_DIRS)


def main(argv):
    if not argv:
        sys.exit(__doc__)
    path = argv[0]
    if not os.path.exists(path):
        sys.exit(f'FAIL: playbook not found: {path}')
    text = open(path, encoding='utf-8').read()
    m = re.search(r'^##\s*Sources\s*$(.*)', text, re.MULTILINE | re.DOTALL)
    if not m:
        sys.exit('FAIL: no "## Sources" section found')
    section = m.group(1)
    bullets = [ln for ln in section.splitlines() if ln.strip().startswith('-')]
    if not bullets:
        sys.exit('FAIL: "## Sources" section has no bullets')
    paths = PATH_RE.findall(section)
    if not paths:
        sys.exit('FAIL: no file paths found in the Sources section'
                  ' (every source should be backtick-quoted, e.g. `file.md`)')
    missing = [p for p in paths if not resolves(p)]
    if missing:
        sys.exit('FAIL: these cited files do not resolve in any known'
                  ' location (repo root, memory/, workflow-builds/,'
                  ' hormozi-library/_derived/):\n  ' + '\n  '.join(missing))
    print(f'OK: {len(bullets)} source bullet(s), {len(paths)} file path(s),'
          f' all resolve on disk.')


if __name__ == '__main__':
    main(sys.argv[1:])
