# Platform specs — checkable length rules

Used by `scripts/check_lengths.py`. Hard limits are the platform's own technical cap. Soft targets are readability guidance from `voice-profile.md`; going over a soft target is a warning, not a failure.

| Platform | Hard limit | Soft target | Image |
| --- | --- | --- | --- |
| X / Twitter | 280 characters per segment (thread = multiple segments, split on a line of `---`) | 1 segment where possible | never |
| LinkedIn | 3,000 characters | 3-6 short paragraphs (roughly 600-900 characters) | never |
| Instagram | 2,200 characters | short, pull-quote line first | always (via social-visuals-workflow) |
| Facebook | no practical hard limit; flag over 2,000 as too long | close to Instagram length | always (via social-visuals-workflow) |

File naming convention for a run's drafts (used by `check_lengths.py` and `verify_draft.py`, which infer the platform from the filename): `draft-x.txt`, `draft-linkedin.txt`, `draft-instagram.txt`, `draft-facebook.txt`.
