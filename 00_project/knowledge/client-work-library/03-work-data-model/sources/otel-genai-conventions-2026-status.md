# OpenTelemetry's GenAI semantic conventions are not stable yet: what shipped in 2026
- URL: https://dev.to/azena-ai/opentelemetrys-genai-semantic-conventions-are-not-stable-yet-heres-what-actually-shipped-in-2026-3mke
- Type: Practitioner blog post (DEV Community)
- Published: 2026-07-16
- Fetched: 2026-10-13

## Key points
- All gen_ai attributes, spans, metrics and events still have the status Development. None is Stable.
- On 12 June 2026 (semconv v1.42.0), the GenAI and MCP conventions moved to a separate semantic-conventions-genai repository. The old opentelemetry.io pages are now stubs.
- Version 1.41.0 (April 2026) added invoke_workflow and split invoke_agent into client and internal spans.
- An agent run is a span tree: invoke_agent at the root, chat spans for model calls, and execute_tool spans for tools.
- Prompt and output text is not captured by default. Content capture is opt-in because of privacy.
- Several attribute names changed. Teams must plan for renames in code and in saved queries.
- Traces show time and tokens. They do not show quality, so teams need separate checks.
- Gaps / bias notes: This is a secondary source. The author's company sells AI tooling. Check names against the repository before use.
