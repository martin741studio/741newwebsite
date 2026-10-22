#!/usr/bin/env python3
"""Check a platform draft against the length rules in references/platform-specs.md.

Usage:
  check_lengths.py <file>...     (platform inferred from filename: draft-x.txt,
                                   draft-linkedin.txt, draft-instagram.txt, draft-facebook.txt)
  check_lengths.py --platform x <file>

Exit 0 when every file passes its hard limit (soft-target misses are warnings only).
"""
import os, re, sys

URL_RE = re.compile(r'https?://\S+|www\.\S+')

LIMITS = {
    'x': {'hard': 280, 'soft': 280, 'per_segment': True},
    'linkedin': {'hard': 3000, 'soft': 900, 'per_segment': False},
    'instagram': {'hard': 2200, 'soft': 400, 'per_segment': False},
    'facebook': {'hard': None, 'soft': 2000, 'per_segment': False},
}


def infer_platform(path):
    stem = os.path.splitext(os.path.basename(path))[0].lower()
    parts = stem.split('-')
    for p in LIMITS:
        if p in parts:
            return p
    sys.exit(f'cannot infer platform from filename: {path} (use --platform)')


def check(path, platform):
    with open(path) as f:
        text = f.read()
    limits = LIMITS[platform]

    url_match = URL_RE.search(text)
    ok = True
    if url_match:
        print(f'FAIL  {platform}: outbound link in the post body ("{url_match.group(0)}") — '
              f'reach penalty, move it to the first comment instead (references/strategy-notes.md)')
        ok = False

    segments = [s for s in text.split('\n---\n')] if limits['per_segment'] else [text]
    for n, seg in enumerate(segments, 1):
        length = len(seg.strip())
        label = f'{platform} segment {n}/{len(segments)}' if len(segments) > 1 else platform
        if limits['hard'] and length > limits['hard']:
            print(f'FAIL  {label}: {length} chars, hard limit {limits["hard"]}')
            ok = False
        elif limits['soft'] and length > limits['soft']:
            print(f'warn  {label}: {length} chars, over the {limits["soft"]} soft target')
        else:
            print(f'OK    {label}: {length} chars')
    return ok


if __name__ == '__main__':
    args = sys.argv[1:]
    forced_platform = None
    if '--platform' in args:
        i = args.index('--platform')
        forced_platform = args[i + 1]
        del args[i:i + 2]
    if not args:
        sys.exit(__doc__)
    all_ok = True
    for path in args:
        platform = forced_platform or infer_platform(path)
        if not check(path, platform):
            all_ok = False
    sys.exit(0 if all_ok else 1)
