# N03 — Best VPS for Claude Code (2026): real prices, setup, limits

- Author/org: Vishnu, Agent 37 (managed Claude Code hosting vendor)
- Type: comparison guide with prices
- Publish date: 2026-09-06 (verified: on-page "Published on Sep 6, 2026" and JSON-LD)
- URL: https://www.agent37.com/blog/claude-code-vps
- Fetch date: 2026-10-13

## Extract (own words)

- The plan, not the VPS, is the big cost. Real cost = Claude plan + server.
- Prices checked September 2026: Vultr 2 vCPU/4 GB $20/mo; DigitalOcean $24/mo; Hetzner CPX22 4 GB EUR 19.99/mo (cheap CX line shown "not available" in early September); Contabo 4 vCPU/8 GB about EUR 5.50/mo on a 24-month term; Oracle free tier up to 2 OCPU/12 GB Arm with reclaim risk; MacStadium Mac mini from $109/mo; AWS t4g.medium about $25/mo.
- Setup is about 15 minutes; hardening, backups and updates are the ongoing cost.
- An idle server in tmux uses no plan quota. Autonomous overnight runs are what consume the weekly cap.
- Claude Code on the web costs no extra compute but is not an always-on machine and VMs are reclaimed when idle.
- No published Anthropic policy against datacenter IPs, per the author.
- Vendor offer: managed instance $4.94/mo dedicated or from $1.99 shared (gVisor isolation, browser terminal).

## IF/THEN rules for 741

1. IF Martin wants a cheap Linux night box in the EU, THEN budget about EUR 20/month for 4 GB and check that the plan is actually orderable before planning.
2. IF the night shift needs macOS tools, THEN compare a home Mac mini (one-off cost) with MacStadium (from $109/mo).
3. IF overnight runs use the plan login, THEN expect the weekly cap, not the server, to be the limit.

## Limits / caveats

- Vendor article that also sells hosting. Prices change; re-check on order day.
