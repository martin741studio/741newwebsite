"""
studio741_server.py

741 Studio MCP Server for Claude Desktop & AI Agents.
Exposes 11 tools to interact with:
- Supabase Portal (clients, programs, backlinks, GSC, grid scans, ads, work_items, approvals, telemetry)
- Local Assets & Markdown Audits (00_project/assets/[client]/)
- Backlink Ingestion Worker execution
"""

import asyncio
import json
import os
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP Server
mcp = FastMCP(
    "studio741",
    instructions="741 Studio: Client Data Backbone, SEO Metrics, Campaigns & Assets"
)

STUDIO_ROOT = Path("/Users/martindrendel/741website")
SECRETS_FILE = STUDIO_ROOT / ".secrets" / "standup.env"

_sb_token: Optional[str] = None
_sb_config: Dict[str, str] = {}


def _get_sb_config() -> Dict[str, str]:
    global _sb_config
    if _sb_config:
        return _sb_config
    if not SECRETS_FILE.exists():
        return {}
    cfg = {}
    for line in SECRETS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, v = line.split("=", 1)
            cfg[k.strip()] = v.strip()
    _sb_config = cfg
    return _sb_config


async def _get_auth_token() -> Optional[str]:
    global _sb_token
    if _sb_token:
        return _sb_token
    cfg = _get_sb_config()
    sb_url = cfg.get("SUPABASE_URL")
    sb_anon = cfg.get("SUPABASE_ANON")
    email = cfg.get("STANDUP_EMAIL")
    password = cfg.get("STANDUP_PASSWORD")

    if not all([sb_url, sb_anon, email, password]):
        return None

    auth_url = f"{sb_url}/auth/v1/token?grant_type=password"
    headers = {"apikey": sb_anon, "Content-Type": "application/json"}
    payload = {"email": email, "password": password}

    async with httpx.AsyncClient(timeout=15.0) as client:
        try:
            r = await client.post(auth_url, headers=headers, json=payload)
            if r.status_code == 200:
                _sb_token = r.json().get("access_token")
                return _sb_token
        except Exception:
            pass
    return None


async def _query_supabase(endpoint: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    cfg = _get_sb_config()
    token = await _get_auth_token()
    if not token or not cfg.get("SUPABASE_URL"):
        return []

    url = f"{cfg.get('SUPABASE_URL')}/rest/v1/{endpoint}"
    headers = {
        "apikey": cfg.get("SUPABASE_ANON", ""),
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient(timeout=15.0) as client:
        try:
            r = await client.get(url, headers=headers, params=params or {})
            if r.status_code == 200:
                return r.json()
            return [{"error": f"HTTP {r.status_code}", "detail": r.text}]
        except Exception as e:
            return [{"error": str(e)}]


# ─────────────────────────────────────────────────────────────
# 11 Granular Tools
# ─────────────────────────────────────────────────────────────

@mcp.tool()
async def studio741_list_clients() -> str:
    """List all active 741 Studio clients, their UUIDs, names, contact emails, and status."""
    res = await _query_supabase("clients", {"select": "id,name,contact_person,contact_email,status,created_at"})
    return json.dumps(res, indent=2, ensure_ascii=False)


@mcp.tool()
async def studio741_get_client_details(client_id: str) -> str:
    """Get full details for a client: active programs, goals, work phases, and actors."""
    programs = await _query_supabase("programs", {"client_id": f"eq.{client_id}"})
    goals = await _query_supabase("work_goals", {"client_id": f"eq.{client_id}"})
    phases = await _query_supabase("work_phases", {"client_id": f"eq.{client_id}"})
    actors = await _query_supabase("work_actors", {"client_id": f"eq.{client_id}"})

    data = {
        "client_id": client_id,
        "programs": programs,
        "work_goals": goals,
        "work_phases": phases,
        "work_actors": actors
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


@mcp.tool()
async def studio741_query_backlinks(client_id: str, limit: int = 50, toxic_only: bool = False) -> str:
    """Query ingested backlinks for a client, filtering by toxicity or limit."""
    params: Dict[str, Any] = {
        "client_id": f"eq.{client_id}",
        "limit": str(limit),
        "order": "created_at.desc"
    }
    if toxic_only:
        params["is_toxic"] = "eq.true"
    res = await _query_supabase("client_backlinks", params)
    return json.dumps(res, indent=2, ensure_ascii=False)


@mcp.tool()
async def studio741_query_gsc_performance(client_id: str, days: int = 30) -> str:
    """Query Google Search Console daily performance metrics (clicks, impressions, CTR, position)."""
    params = {
        "client_id": f"eq.{client_id}",
        "limit": "100",
        "order": "date.desc"
    }
    res = await _query_supabase("gsc_daily_performance", params)
    return json.dumps(res, indent=2, ensure_ascii=False)


@mcp.tool()
async def studio741_query_geo_grid(client_id: str) -> str:
    """Query Local Falcon map scan grids, keyword rankings, and centroid coordinates."""
    params = {
        "client_id": f"eq.{client_id}",
        "limit": "20",
        "order": "scan_date.desc"
    }
    res = await _query_supabase("geo_grid_scans", params)
    return json.dumps(res, indent=2, ensure_ascii=False)


@mcp.tool()
async def studio741_query_citations(client_id: str, include_listings: bool = False) -> str:
    """Query BrightLocal directory audit health (NAP consistency, live vs missing citations, rating, reviews) and optionally list individual directory citations."""
    audits = await _query_supabase("brightlocal_audits", {
        "client_id": f"eq.{client_id}",
        "order": "audit_date.desc",
        "limit": "5"
    })
    result: Dict[str, Any] = {"audits": audits}
    if include_listings:
        listings = await _query_supabase("client_citations", {
            "client_id": f"eq.{client_id}",
            "limit": "100"
        })
        result["directory_citations"] = listings
    return json.dumps(result, indent=2, ensure_ascii=False)


@mcp.tool()
async def studio741_query_drive_assets(client_id: str, category: Optional[str] = None, limit: int = 50) -> str:
    """Query client deliverables, reports, spreadsheets, and CRO assets stored in Drive."""
    params: Dict[str, Any] = {
        "client_id": f"eq.{client_id}",
        "limit": str(limit),
        "order": "created_at.desc"
    }
    if category:
        params["category"] = f"eq.{category}"
    res = await _query_supabase("client_drive_assets", params)
    return json.dumps(res, indent=2, ensure_ascii=False)


@mcp.tool()
async def studio741_query_ads(client_id: str, channel: str = "all") -> str:
    """Query active Meta and Google ad campaigns, spend, clicks, conversions, and ROAS."""
    results = {}
    if channel in ("all", "meta"):
        results["meta"] = await _query_supabase("meta_campaigns", {"client_id": f"eq.{client_id}"})
    if channel in ("all", "google"):
        results["google"] = await _query_supabase("google_campaigns", {"client_id": f"eq.{client_id}"})
    return json.dumps(results, indent=2, ensure_ascii=False)


@mcp.tool()
async def studio741_read_client_asset(client_slug: str, relative_path: str) -> str:
    """Safely read a local markdown audit, keyword list, or strategy document in 00_project/assets/clients/[client_slug]/."""
    base_dirs = [
        STUDIO_ROOT / "00_project" / "assets" / client_slug,
        STUDIO_ROOT / ".claude" / "worktrees" / "admiring-nightingale-f0f882" / "00_project" / "assets" / client_slug
    ]
    target_path = None
    for b in base_dirs:
        candidate = (b / relative_path).resolve()
        if candidate.exists() and str(candidate).startswith(str(b)):
            target_path = candidate
            break

    if not target_path:
        return f"Error: Asset not found for client {client_slug} at path: {relative_path}"

    try:
        content = target_path.read_text(encoding="utf-8", errors="replace")
        return content[:15000] + ("\n... [Truncated]" if len(content) > 15000 else "")
    except Exception as e:
        return f"Error reading asset: {e}"


@mcp.tool()
async def studio741_run_backlink_sync(client_slug: str = "suriya", apply: bool = False) -> str:
    """Run the backlink parser to ingest local audits into Supabase (dry-run or apply mode)."""
    script_path = STUDIO_ROOT / "scripts" / "import-backlinks.mjs"
    if not script_path.exists():
        return "Error: scripts/import-backlinks.mjs not found"

    cmd = ["node", str(script_path), f"--client={client_slug}"]
    if apply:
        cmd.append("--apply")
    else:
        cmd.append("--dry-run")

    proc = subprocess.run(cmd, cwd=str(STUDIO_ROOT), capture_output=True, text=True, timeout=60)
    return proc.stdout or proc.stderr


@mcp.tool()
async def studio741_create_work_item(client_id: str, title: str, description: str = "", phase_id: str = "") -> str:
    """Create a new work item draft for review in Supabase without modifying live production."""
    cfg = _get_sb_config()
    token = await _get_auth_token()
    if not token:
        return "Error: Unable to authenticate with Supabase"

    url = f"{cfg.get('SUPABASE_URL')}/rest/v1/work_items"
    headers = {
        "apikey": cfg.get("SUPABASE_ANON", ""),
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    payload: Dict[str, Any] = {
        "client_id": client_id,
        "title": title,
        "description": description,
        "status": "draft"
    }
    if phase_id:
        payload["phase_id"] = phase_id

    async with httpx.AsyncClient(timeout=15.0) as client:
        r = await client.post(url, headers=headers, json=payload)
        return r.text


@mcp.tool()
async def studio741_propose_approval(client_id: str, title: str, description: str = "", work_item_id: str = "") -> str:
    """Stage an action into approval_items for human-in-the-loop review (client/admin approval)."""
    cfg = _get_sb_config()
    token = await _get_auth_token()
    if not token:
        return "Error: Unable to authenticate with Supabase"

    url = f"{cfg.get('SUPABASE_URL')}/rest/v1/approval_items"
    headers = {
        "apikey": cfg.get("SUPABASE_ANON", ""),
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    payload: Dict[str, Any] = {
        "client_id": client_id,
        "title": title,
        "description": description,
        "status": "pending_review"
    }
    if work_item_id:
        payload["work_item_id"] = work_item_id

    async with httpx.AsyncClient(timeout=15.0) as client:
        r = await client.post(url, headers=headers, json=payload)
        return r.text


@mcp.tool()
async def studio741_log_agent_run(
    client_id: str,
    agent_id: str,
    prompt_tokens: int = 0,
    cached_prompt_tokens: int = 0,
    completion_tokens: int = 0,
    model: str = "claude-3-5-sonnet"
) -> str:
    """Log an agent execution run, token metrics, cache hits, and estimated cost in Supabase telemetry."""
    cfg = _get_sb_config()
    token = await _get_auth_token()
    if not token:
        return "Error: Unable to authenticate with Supabase"

    url = f"{cfg.get('SUPABASE_URL')}/rest/v1/work_agent_runs"
    headers = {
        "apikey": cfg.get("SUPABASE_ANON", ""),
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "client_id": client_id,
        "agent_id": agent_id,
        "state": "completed",
        "model_tier": model,
        "prompt_tokens": prompt_tokens,
        "cached_prompt_tokens": cached_prompt_tokens,
        "completion_tokens": completion_tokens
    }

    async with httpx.AsyncClient(timeout=15.0) as client:
        r = await client.post(url, headers=headers, json=payload)
        return f"Logged telemetry: {r.status_code}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
