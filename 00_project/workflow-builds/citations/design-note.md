# Design Note: Citations DACH (`citations`)

Spec: `00_project/workflow-architecture.md` §4.1 · Language: STE.

## 1. Use Cases (Rule R1.1)

| # | Trigger | Steps | Tools | Result |
|---|---|---|---|---|
| **UC1 Status Check** | `/citations-dach <client>` | Read `client_locations`, query `client_citations` in Supabase, run live monitor. | `citation-monitor.mjs`, Supabase | Status table: live, submitted, planned rows. |
| **UC2 Submission Runbook** | `/citations-dach <client> runbook` | Generate step-by-step submission data for Group A (741) and Group B (Client). | `submission-runbook.mjs` | Markdown runbook with pre-filled NAP and category mapping. |
| **UC3 BrightLocal Sync** | `/citations-dach <client> sync-bl` | Import BrightLocal audit export or order status into Supabase. | `import-brightlocal.mjs` | `client_citations` updated with live URLs and verification timestamps. |

## 2. Pipeline with Checkpoints

```
[Canonical NAP Lock] ──► [Aggregator Self-Service] ──► [Group A: 741 Priority] ──► [BrightLocal Order] ──► [Group B: Client] ──► [Live Monitor & _run.json]
   (client_locations)        (11880, Gelbe Seiten)         (Apple, Bing, DasÖrtliche)     (Paid Package)       (Facebook, Jameda)     (Auto-sync to Excel)
```

* **Checkpoints:**
  * **Go-A (NAP Lock):** Martin confirms canonical address and telephone before directory submissions begin.
  * **Go-B (BrightLocal Order):** Martin gives explicit Go before purchasing external BrightLocal citation credits.
  * **Go-C (Client Handoff):** Martin approves the client instructions for Group B logins.

## 3. Degrees of Freedom (Rule R1.7)
* **Deterministic / Fragile:** Directory URL HTTP checks, Supabase database reads/writes, CSV parsing $\to$ Node.js scripts in `reporting/`.
* **Qualitative:** Writing polite instructions for client self-service logins $\to$ guided prompt template.

## 4. Hand-Solved Task (Praxis Suriya)
* Real case solved in `00_project/coralie-aggregator-pack.md` (Praxis Suriya, Ingelheim).
* 44 directories mapped, canonical NAP locked, 38 live citations verified, 6 pending indexing.
