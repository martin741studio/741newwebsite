# Pipeline — personal-posts

```
[ 0. No thought ready? (conditional, secondary entry point) ]
   - Martin asks "what should I post about" -> offer 2-3 open ideas from
     00_project/assets/741studio/personal-posts/topic-backlog.json
   - Martin picks/restates one as his own thought -> continues below as normal
            │
            ▼
[ Martin dictates/types a raw thought ]
            │
            ▼
[ 1. Topic check ]
   - names a client + a result? -> branch to client-go check
   - otherwise -> straight to drafting
            │
            ▼
[ 1b. Client-go check (conditional) ]
   - known go on file for THIS post -> draft named, with real number
   - no go on file -> ask Martin (card) -> default: draft anonymized (industry + real number, no name/logo)
            │
            ▼
[ 2. Core draft ]
   - one core argument in Martin's voice (references/voice-profile.md)
   - opening line follows the DR hero pattern scaled down (claim + one reason), copy-rules.md C2.1/C2.8/C4.1
   - claim check: every number/result traced to a real source, never invented (claims-need-real-data)
            │
            ▼
[ 3. Platform adaptation ]
   - LinkedIn (full argument) · X (sharpest single version, thread if needed)
   - Instagram caption · Facebook caption  (both pair with an image, step 5)
            │
            ▼
[ 4. Slop gate — per platform version, not once for all ]
   - deslop.py --text  ->  5/5?  yes: continue   no: cleanse.sh -> re-lint -> repeat until 5/5
            │
            ▼
🛑 [ CHECKPOINT: Martin's go, per post, every time ]
   - show all platform versions together
   - Martin approves, rejects, or asks for a rewrite of one or more versions
   - no auto-post, no auto-schedule, ever
            │
            ▼
[ 5. Image (Instagram + Facebook only, conditional) ]
   - reuse social-visuals-workflow: 07_social/templates/ -> headless-Chrome PNG
   - skip entirely for LinkedIn/X-only runs
            │
            ▼
[ 6. Delivery ]
   - approved text (+ image where built) handed to Martin, ready to paste
   - Martin posts it himself, on his own schedule
```

**Checkpoints that matter:** one real gate (Martin's go per post, step 4->5). Everything before it is draft-and-check; everything after it is reuse of an already-approved image pipeline plus delivery. No second internal checkpoint needed, unlike a full page build, because there is no CMS write and no live-site risk here (hard limit: never auto-post).
