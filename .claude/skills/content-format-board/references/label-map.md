# Label map — internal term → client-facing label

Martin's decision 2026-10-24: client-facing boards use plain descriptive English, never the creator's names, the program name, or tool/creator names from the knowledge base. `scripts/label_map.py` holds the same table as data and `scripts/verify_board.py` fails a board that still contains an internal term.

| Internal (never in a board) | Client-facing label |
| --- | --- |
| One-Shot | Single-Scene Hook |
| One-Shot L1 (lo-fi) | Single-Scene Hook, phone version |
| One-Shot L2 (hi-fi) | Single-Scene Hook, produced version |
| One-Shot L3 (vignette) | Single-Scene Hook, moment version |
| One-Shot L4 (dual stimulation) | Single-Scene Hook, two-stories version |
| Ten-Shot / 10-Shot | Fast-Cut Story |
| Ten-Shot L1 (no text) | Fast-Cut Story, visuals only |
| Ten-Shot L2 (text overlay) | Fast-Cut Story, with context line |
| Ten-Shot L3 (narration) | Fast-Cut Story, narrated |
| Yap / Yapping | Talk-to-Camera |
| Raw Yap | Talk-to-Camera, phone version |
| Graphic Yap | Talk-to-Camera, with graphics |
| Prop Yap | Talk-to-Camera, with a prop |
| Cinematic Yap | Talk-to-Camera, produced version |
| How/Why We Do It | Why-We-Do-It Educational |
| Content level / readiness check | Production readiness check |
| Visual amplifier | Supporting graphic |
| Title hook / visual hook | On-screen opening line / opening image |
| Retention bridge | Second sentence (proof line) |
| Seamless loop | Loop ending |

Banned strings in any client-facing board (case-insensitive): Alex Garcia, Cut 30, Cut30, Hormozi, ACCCM, SPCL, Yap, Yapping, One-Shot (hyphenated; plain "one shot" as in "one take" is allowed), Ten-Shot, 10-Shot, Answer the Public, Answer Socrates, Exploding Topics, BuzzSumo, Glimpse, NotebookLM, Benign Violation, 360Brew, ReelForge, UGC Copilot, Socialync, Virvid.

Language: German clients get the German labels — Einzelszenen-Hook, Schnellschnitt-Story, Direkt-in-die-Kamera, Warum-wir-es-so-machen (lehrend), Produktions-Check. Run `deslop_de.py` on German boards, `deslop.py` on English ones.
