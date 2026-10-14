# Pipeline (step 2.4)

Shape: 4.1 Sequential workflow with gates, with a 4.3 iterative-refinement loop at the
verification step. No Martin "go" checkpoint mid-run — this is a one-shot prep document
Martin reads and can correct in chat; the only hard gate is the verification step before
showing it (a wrong or unsourced brief before a real sales call is the one failure mode that
actually costs Martin money, so that gate is non-negotiable even though there is no
multi-day/Martin-approval checkpoint like a client deliverable has).

```
Step 1  Find the prospect + the call
        - If Martin named a booked call: reuse find_prospect.py-style lookup
          (00_project/prospects/<slug>/booking/) — same slug resolution as booking-sequence.
        - If 0 or >1 match, or no booking folder at all (UC3, thin case): ask via a card
          (handled by the orchestrator, never in prose) with the candidates, or confirm
          "no prior history — short brief only".

Step 2  Read context (read only, in this order)
        - booking/booking.json (who, when, call link, language)
        - booking/baseline.md (what she already saw: positioning + findings + proof wall)
        - booking/claims.json (every number already shown, with its source)
        - booking/m1.txt, m2.txt, m3.txt if present (what has been sent since, so nothing repeats)
        - memory 741studio-pricing.md (package order, guarantee tier)
        - 00_project/sales-einwandbehandlung.md (house objection playbook + call dramaturgy)
        - (optional, only if the booking folder is thin) LinkedIn CRM Pipeline tab per
          linkedin-crm-access.md

Step 3  Pick (one line of reasoning per pick, in picks.md style like booking-sequence)
        - The ONE new gap to lead with (not already shown) + the gaps already shown, kept short
        - One proof case that matches her business shape (solo/agency/health/etc.), one reserve case
        - Package recommendation: premium tier named first, the guaranteed 90-Tage tier
          recommended by default unless Martin's notes say otherwise, Starter named only as the anchor
        - 2-4 objections from sales-einwandbehandlung.md, RANKED for this prospect's situation
          (not the full list — e.g. a fully-booked solo consultant gets the capacity-objection
          reframe first, not a generic price objection)

Step 4  Draft the one-pager (template below, house framing only)
        Sections: who she is -> her goal question -> the gap (sourced) -> proof -> package
        recommendation -> ranked objections -> call structure (quantify goal, show gap, proof,
        recommend + guarantee before price, objection, close question) -> "nicht vergessen"
        (call link, device tip, what not to repeat).

Step 5  Verify (loop until it passes)
        - Run the German slop check with the real claims file:
          `python3 00_project/content-writing-skill/scripts/deslop_de.py <file> --claims <booking/claims.json>`
          Fix and re-run until `score 5/5 CLEAN`.
        - grep the output for outside method names (hormozi, ramoszi, closer framework,
          diagnostic sale, "nach <Autor>") — must be empty.
        - Confirm every number in the brief traces to claims.json or to a freshly-fetched
          source cited inline — never an invented figure.

Step 6  Deliver
        - Write 00_project/prospects/<slug>/call-prep.md
        - Show Martin in chat: the brief, the check output line, the call time in both zones.
        - No client/prospect message is ever sent from this skill — it only writes a file
          Martin reads before the call.
        - Write/update _run.json in the prospect's run folder (registry picks it up via sync).
```

## Where booking-sequence and sales-call-prep meet
Both read `00_project/prospects/<slug>/booking/`. booking-sequence WRITES that folder (it owns
booking.json, baseline.md, claims.json, m1-m3, the reminders). sales-call-prep only READS it
and writes a separate file (`call-prep.md`) — it never edits booking-sequence's files and
never schedules or sends anything. If sales-call-prep is asked to run before booking-sequence
has ever run for this prospect, it falls back to UC3 (thin case) rather than inventing the
missing history.
