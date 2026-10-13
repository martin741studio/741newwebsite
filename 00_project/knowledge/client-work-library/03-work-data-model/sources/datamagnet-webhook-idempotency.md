# How to Deduplicate Webhooks and Ensure Idempotency (2026)
- URL: https://www.datamagnet.co/post/idempotency-enrichment-pipelines-duplicate-webhook-writes/
- Type: Vendor engineering blog post
- Published: 2026-07-22 (modified 2026-08-08)
- Fetched: 2026-10-13

## Key points
- Build the idempotency key from stable parts: the source name, the event type and the source event id.
- Do not build the key from receive time or from a payload hash, because these can change on redelivery.
- Check a dedup table before any write. If the key exists and is not expired, return success and stop.
- Make the write itself idempotent with an upsert on the natural key of the entity.
- The unique constraint is the second guard. It stops race conditions that the dedup check misses.
- Keep keys at least as long as the longest retry window of all senders. The article uses 24 to 48 hours.
- Gaps / bias notes: The article does not cover transactions. It comes from a data-enrichment vendor with its own product focus.
