# 06 — OpenAI: "A practical guide to building agents"

Type: vendor guide (34-page PDF, web version dated 2026-01-15). Fetched 2026-11-03.
URL: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/

## Key content for job design
- Agent = model + tools + instructions. Tools in three types: Data (read), Action (write: send emails, update CRM), Orchestration (other agents).
- Instructions best practices: "Use existing documents" (SOPs, policy docs → routines); "Prompt agents to break down tasks"; "Define clear actions" ("every step corresponds to a specific action or output"); "Capture edge cases" (what to do when information is missing).
- Tool safeguards: "Assess the risk of each tool ... by assigning a rating—low, medium, or high—based on factors like read-only vs. write access, reversibility, required account permissions, and financial impact. Use these risk ratings to trigger automated actions, such as pausing for guardrail checks before executing high-risk functions or escalating to a human."
- Human intervention triggers: (1) "Exceeding failure thresholds: set limits on agent retries or actions"; (2) "High-risk actions: sensitive, irreversible, or high stakes ... canceling user orders, authorizing large refunds, or making payments."
- Guardrails are layered (relevance, safety, PII, moderation, tool safeguards, rules-based, output validation); start from identified risks and add from real failures.
- Manager pattern (one agent coordinates specialists via tool calls) vs decentralized handoffs. "Maximize a single agent's capabilities first."

## Assessment for 741
New vs. video: a risk rating per tool with four named factors (read/write, reversibility, permissions, money) instead of Tyler's flat "send, spend, delete, publish"; a second approval trigger (retry/failure threshold) Tyler does not have; "capture edge cases" as a required job-description section.
Marketing: Agents SDK code; "contact sales".
Usable for 741: every job description gets a tool table with a risk rating (low/medium/high) derived from the four factors; high = needs go; a retry cap per agent ("after N failed attempts, stop and report"); the manager pattern is the model for Martin as manager, with the morning grill as the manager's inbox.
