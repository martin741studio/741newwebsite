# NovaFabric: Tamper-Evident, Replayable Evidence for Autonomous AI Agent Runs
- URL: https://arxiv.org/abs/2609.12582
- Type: Research paper (arXiv cs.CR)
- Published: 2026-09-11 (v1)
- Fetched: 2026-10-13

## Key points
- The system records an agent run without a change to the agent logic.
- Each run becomes a portable "Run Capsule" with a schema of fifteen entity types.
- A signature, a trusted timestamp and a Merkle log seal the capsule. A redaction step removes secrets.
- The design builds on OpenTelemetry, in-toto and W3C PROV. The paper adds integration, not new cryptography.
- The tests rejected all three tested tamper classes. Completeness of the recorded streams was only about 0.65.
- Replay of tool-using runs worked in 2 of 10 workloads. Replay is still an open problem.
- A third party can check an exported evidence bundle with standard tools.
- Gaps / bias notes: Single-author paper with a self-built system. The level is above the needs of a small agency. The useful idea is a content hash and a sealed summary per run.
