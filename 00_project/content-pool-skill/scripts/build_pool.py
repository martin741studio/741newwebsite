#!/usr/bin/env python3
"""Build pool.json from candidates.json plus the raw data in the run folder.

The agent writes the JUDGMENT (topic, fit, compliance, conversion, effort, regex patterns).
This script adds every NUMBER from the raw files, so no number is typed by hand:
volumes, autocomplete hits, People-Also-Ask hits, own ranking signal, competitor coverage, scores.

Usage: build_pool.py --run-dir <content-pool dir> [--date YYYY-MM-DD]
Reads:  04-pool/candidates.json, 03-demand/volume.json, 03-demand/autocomplete.json,
        02-competitors/serp-*.json, 02-competitors/metrics.json, 02-competitors/site_urls.json,
        03-demand/ranked-<client domain>.json, spend.jsonl
Writes: 04-pool/pool.json

Score (0-100 each): demand 30 %, gap 25 %, fit 25 %, conversion 15 %, effort 5 %.
Rules found in the Dumann dry run (2026-10-11):
  R-S1 A keyword without a place name counts as national: its volume score is multiplied by 0.6.
  R-S2 If 50 % or more of the competitor set has the item (table stakes), demand has a floor of 100 x share.
  R-S3 A gap without demand is not an opportunity: if demand < 30, the gap score is halved.
  R-S5 Client GSC queries count as demand: 80 from 100 impressions, 70 from 30, 60 from 10, else 50 (basis client).
  R-S6 If fewer than 5 items reach A, the best quarter of the live items (fit 2 or 3) with total >= 65 becomes A.
  R-S4 Priority: A >= 75, B >= 55, else C. Table stakes never stay C. fit 1 is never A. fit 0 is cut.
"""
import argparse, glob, json, math, os, re, sys, time

W = {"demand": 0.30, "gap": 0.25, "fit": 0.25, "conversion": 0.15, "effort": 0.05}
FIT_PTS = {0: 0, 1: 33, 2: 67, 3: 100}
CONV_PTS = {0: 0, 1: 33, 2: 67, 3: 100}
EFF_PTS = {1: 100, 2: 67, 3: 33}


def jl(path):
    return json.load(open(path)) if os.path.exists(path) else None


VOL_FILE = {}


def volume_map(run):
    out = {}
    for f in sorted(glob.glob(f"{run}/03-demand/volume*.json")):
        if "payload" in f:
            continue
        d = jl(f)
        for r in d["tasks"][0].get("result") or []:
            out[r["keyword"].lower()] = r.get("search_volume")
            VOL_FILE.setdefault(r["keyword"].lower(), os.path.relpath(f, run))
    return out


def ac_pool(run):
    d = jl(f"{run}/03-demand/autocomplete.json") or {}
    s = set()
    for seed, qs in d.items():
        if seed.startswith("_") or not isinstance(qs, dict):
            continue
        for sug in qs.values():
            # Drop review/brand noise ("... rezensionen", long business-name strings).
            s.update(x.lower() for x in sug if not re.search(r"rezension|bewertung|erfahrungen mit|\bdr\.? med\b", x.lower()) and len(x) <= 70)
    return sorted(s)


def paa_pool(run):
    out = []
    for f in sorted(glob.glob(f"{run}/02-competitors/serp-[0-9]*.json")):
        if "payload" in f:
            continue
        d = jl(f)
        r = (d["tasks"][0].get("result") or [{}])[0]
        for it in r.get("items", []):
            if it["type"] == "people_also_ask":
                out += [e.get("title") for e in it.get("items", []) if e.get("title")]
    return sorted(set(out))


def own_ranked(run, domain):
    d = jl(f"{run}/03-demand/ranked-{domain}.json")
    rows = []
    if d:
        r = (d["tasks"][0].get("result") or [{}])[0]
        for it in r.get("items") or []:
            rows.append((it["keyword_data"]["keyword"], it["keyword_data"]["keyword_info"]["search_volume"], it["ranked_serp_element"]["serp_item"]["rank_absolute"]))
    return rows


def own_site(run, domain):
    """Existing-site mode: headings of measured own pages and slugs of the own sitemap."""
    metrics = (jl(f"{run}/02-competitors/metrics.json") or []) + (jl(f"{run}/05-sitetree/own-metrics.json") or [])
    sites = jl(f"{run}/02-competitors/site_urls.json") or {}
    heads = []
    for m in metrics:
        if m.get("status") == "ok" and domain in m["url"]:
            heads.append((m["url"], " ".join([m["title"]] + m["h1"] + m["h2"] + m["h3"]).lower()))
    urls = sites.get(domain, {}).get("urls", []) if sites.get(domain, {}).get("status") == "ok" else []
    return heads, urls


def live_status(patterns, heads, urls, item_type, page_tag, audience="patient"):
    """Existing-site gap status. Coarse on purpose; a human reads the result.
    Own-page items (page_tag service:* or item_type page): present only with an own URL slug; a heading on another page = weak.
    FAQ items: never present automatically (the single questions need a manual read); topic found = weak.
    Other blocks: present = a measured own page has the topic in a heading; weak = only an URL slug has it.
    """
    pats = [p for p in patterns if not p.startswith("flag_")]
    if not pats:
        return "n/a", None
    # Event, product and blog URLs (Wix: /service-page/, /product-page/, /post/) never count as the practice's own service page.
    skip = r"/(service-page|product-page|post|blog|event)/" + (r"|/kurse|ausbildung|seminar|fastenleiter" if audience == "patient" else "")
    own_urls = [u for u in urls if not re.search(skip, u.lower())]
    pool_urls = own_urls if (page_tag.startswith("service:") or item_type == "page") else urls
    slug_hit = next((u for u in pool_urls if any(re.search(p, re.sub(r"[-_/.]", " ", u.lower())) for p in pats)), None)
    head_hit = next((url for url, h in heads if any(re.search(p, h) for p in pats)), None)
    own_page = page_tag.startswith("service:") or item_type == "page"
    if item_type == "faq":
        return ("weak", head_hit or slug_hit) if (head_hit or slug_hit) else ("missing", None)
    if own_page:
        if slug_hit: return "present", slug_hit
        return ("weak", head_hit) if head_hit else ("missing", None)
    if head_hit: return "present", head_hit
    if slug_hit: return "weak", slug_hit
    return "missing", None


def gsc_rows(run):
    """Client GSC queries from 03-demand/gsc-queries-90d.tsv (query, clicks, impressions, position). Empty list if the file is missing."""
    path = f"{run}/03-demand/gsc-queries-90d.tsv"
    rows = []
    if os.path.exists(path):
        for line in open(path):
            if line.startswith("#") or line.startswith("query\t") or not line.strip():
                continue
            q, c, i, pos = (line.rstrip("\n").split("\t") + ["", "", "", ""])[:4]
            rows.append((q, int(c), int(i), float(pos) if pos else None))
    return rows


def gsc_signal(rows, patterns):
    hits = [r for r in rows if any(re.search(p, r[0]) for p in patterns)]
    if not hits:
        return None
    poss = [r[3] for r in hits if r[3] is not None]
    return {"queries": len(hits), "impressions": sum(r[2] for r in hits), "clicks": sum(r[1] for r in hits),
            "best_position": min(poss) if poss else None, "top_query": max(hits, key=lambda r: r[2])[0]}


def corpora(run, comp_cfg):
    metrics = jl(f"{run}/02-competitors/metrics.json") or []
    sites = jl(f"{run}/02-competitors/site_urls.json") or {}
    corp, flags = {}, {}
    for dom in comp_cfg:
        parts, fl = [], set()
        for m in metrics:
            if m.get("status") == "ok" and dom in m["url"]:
                parts += [m["title"], m.get("meta_description", "")] + m["h1"] + m["h2"] + m["h3"]
                if m["faq_signal"]: fl.add("FLAG_FAQ")
                if m["price_mention"]: fl.add("FLAG_PRICE")
                if m["rating_mention"]: fl.add("FLAG_RATING")
                if m["tel_link"]: fl.add("FLAG_TEL")
                if m["booking_hint"]: fl.add("FLAG_BOOKING")
                if m["has_form"]: fl.add("FLAG_FORM")
                if any(t in ("MedicalBusiness", "Physician", "MedicalClinic", "MedicalOrganization") for t in m["jsonld_types"]): fl.add("FLAG_SCHEMA_MEDICAL")
                if any(t in ("LegalService", "Attorney", "Notary") for t in m["jsonld_types"]): fl.add("FLAG_SCHEMA_LEGAL")
                if any("Rating" in t for t in m["jsonld_types"]): fl.add("FLAG_SCHEMA_RATING")
        s = sites.get(dom, {})
        if s.get("status") == "ok":
            parts += [re.sub(r"[-_/.]", " ", u.split(dom, 1)[-1]) for u in s["urls"]]
        corp[dom] = " ".join(parts).lower() + " " + " ".join(sorted(fl)).lower()
        flags[dom] = fl
    readable = {d for d in comp_cfg if corp[d].strip() and (any(m.get("status") == "ok" and d in m["url"] for m in metrics) or sites.get(d, {}).get("status") == "ok")}
    return corp, readable


def vol_pts(v):
    return min(100, 100 * math.log10(v + 1) / math.log10(1601))


def gsc_pts(g):
    if not g: return 0
    i = g["impressions"]
    if i < 5: return 0  # fewer than 5 impressions is noise, not demand (lesson 28)
    return 80 if i >= 100 else 70 if i >= 30 else 60 if i >= 10 else 50


def demand_score(vol_local, vol_nat, ac, paa, client, share_expect, mode, table_stakes, gsc=None):
    cands = [(0, "none")]
    if vol_local:
        cands.append((vol_pts(vol_local), "volume"))
    if vol_nat:
        cands.append((0.6 * vol_pts(vol_nat), "volume"))
    if ac >= 1: cands.append((45 if ac >= 5 else 35, "autocomplete"))
    if paa >= 1: cands.append((55 if paa >= 3 else 45, "paa"))
    if client: cands.append((60, "client"))
    if gsc: cands.append((gsc_pts(gsc), "client"))
    if mode == "expectation" or table_stakes: cands.append((100 * share_expect, "expectation"))
    return max(cands, key=lambda x: x[0])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--date", default=time.strftime("%Y-%m-%d"))
    a = ap.parse_args()
    run = a.run_dir.rstrip("/")
    cand = jl(f"{run}/04-pool/candidates.json")
    meta, comp_cfg = cand["meta"], cand["competitors"]
    vols, ac, paa = volume_map(run), ac_pool(run), paa_pool(run)
    own = own_ranked(run, meta["domain"])
    gsc = gsc_rows(run)
    own_heads, own_urls = own_site(run, meta["domain"]) if meta.get("mode") == "existing" else ([], [])
    corp, readable = corpora(run, comp_cfg)
    spend = 0.0
    if os.path.exists(f"{run}/spend.jsonl"):
        spend = sum(json.loads(l)["cost"] for l in open(f"{run}/spend.jsonl") if l.strip())
    items = []
    for c in cand["items"]:
        kws = []
        for k in c.get("keywords", []):
            v = vols.get(k.lower(), "absent")
            scope = "local" if any(re.search(r"(?<![a-zäöüß])" + re.escape(pl.lower()) + r"(?![a-zäöüß])", k.lower()) for pl in meta.get("places", [])) else "national"
            kws.append({"kw": k, "scope": scope, "volume": None if v == "absent" else v, "volume_source": meta.get("volume_source", "DataForSEO google_ads/search_volume/live, de, 2276"), "volume_date": a.date})
        vol_max = max([k["volume"] for k in kws if k["volume"]], default=None)
        vol_local = max([k["volume"] for k in kws if k["volume"] and k["scope"] == "local"], default=None)
        vol_nat = max([k["volume"] for k in kws if k["volume"] and k["scope"] == "national"], default=None)
        vol_sum = sum(k["volume"] for k in kws if k["volume"]) if any(k["volume"] for k in kws) else None
        ac_hits_l = [s for s in ac if any(re.search(p, s) for p in c.get("ac_terms", []))]
        paa_hits_l = [s for s in paa if any(re.search(p, s.lower()) for p in c.get("paa_terms", []))]
        client_sig = None
        for kw, v, pos in own:
            if any(re.search(p, kw) for p in c.get("client_signal_kw", [])):
                client_sig = f"{meta['domain']} ranks #{pos} for '{kw}' ({v}/month)"
                break
        if c.get("client_signal_text"):
            client_sig = c["client_signal_text"]
        # competitor coverage
        tiers = set(c.get("cover_tiers", ["local"]))
        dom_in = [d for d, cfg in comp_cfg.items() if cfg["tier"] in tiers and d in readable]
        pats = c.get("cover_patterns", [])
        cov = [d for d in dom_in if any(re.search(p, corp[d]) for p in pats)] if pats else []
        denom = len(dom_in)
        share = round(len(cov) / denom, 3) if denom else 0.0
        table_stakes = share >= 0.5 and denom >= 3
        g = gsc_signal(gsc, c["gsc_patterns"]) if c.get("gsc_patterns") else None
        if g and g["impressions"] < 5:
            g = None  # fewer than 5 impressions is noise, not demand (lesson 28)
        if g:
            gtxt = f"GSC 3 months: {g['queries']} queries, {g['impressions']} impressions, {g['clicks']} clicks" + (f", best position {g['best_position']}" if g["best_position"] else "") + f"; top query '{g['top_query']}'"
            client_sig = f"{client_sig}. {gtxt}" if client_sig else gtxt
        d_score, basis = demand_score(vol_local, vol_nat, len(ac_hits_l), len(paa_hits_l), client_sig, share, c.get("demand_mode", "search"), table_stakes, g)
        gap = 100 * (1 - share) if pats else 50.0
        if d_score < 30:
            gap *= 0.5
        total = (W["demand"] * d_score + W["gap"] * gap + W["fit"] * FIT_PTS[c["fit"]] + W["conversion"] * CONV_PTS[c["conversion"]] + W["effort"] * EFF_PTS[c["effort"]])
        total = round(total, 1)
        comp = c["compliance"]
        if c["fit"] == 0 or comp["flag"] == "block" or c["page_tag"] == "cut":
            prio, status = "cut", "cut"
        else:
            prio = "A" if total >= 75 else "B" if total >= 55 else "C"
            if table_stakes and prio == "C": prio = "B"
            if c["fit"] == 1:
                status = "adjacent_review"
                if prio == "A": prio = "B"
            elif c.get("needs_client"):
                status = "needs_client"
            else:
                status = "draft"
        live_s, live_u = live_status(pats, own_heads, own_urls, c["item_type"], c["page_tag"], c["audience"]) if meta.get("mode") == "existing" else ("n/a", None)
        if c.get("live_status"): live_s, live_u = c["live_status"], c.get("live_url")
        ev = []
        for k in kws:
            if k["volume"] is not None:
                ev.append({"type": "volume", "file": VOL_FILE.get(k["kw"].lower(), "03-demand/volume*.json"), "ref": k["kw"], "date": a.date})
        if ac_hits_l: ev.append({"type": "autocomplete", "file": "03-demand/autocomplete.json", "ref": " | ".join(c.get("ac_terms", []))[:200], "date": a.date})
        if paa_hits_l: ev.append({"type": "paa", "file": "02-competitors/serp-*.json", "ref": paa_hits_l[0], "date": a.date})
        if g: ev.append({"type": "ranked", "file": "03-demand/gsc-queries-90d.tsv", "ref": " | ".join(c["gsc_patterns"])[:160], "date": a.date})
        if client_sig and own: ev.append({"type": "ranked", "file": f"03-demand/ranked-{meta['domain']}.json", "ref": client_sig[:120], "date": a.date})
        if cov:
            if os.path.exists(f"{run}/02-competitors/site_urls.json"):
                ev.append({"type": "sitemap", "file": "02-competitors/site_urls.json", "ref": ",".join(cov)[:200], "date": a.date})
            ev.append({"type": "competitor-page", "file": "02-competitors/metrics.json", "ref": ",".join(cov)[:200], "date": a.date})
        ev += c.get("evidence_extra", [])
        if not ev:
            ev.append({"type": "manual", "file": "01-client/client-baseline.md", "ref": c.get("topic", ""), "date": a.date})
        items.append({
            "id": c["id"], "pillar": c["pillar"], "audience": c["audience"], "page_tag": c["page_tag"],
            "section_hint": c.get("section_hint"), "item_type": c["item_type"], "topic": c["topic"],
            "question": c.get("question"), "keywords": kws, "service_ref": c.get("service_ref"),
            "fit": c["fit"], "fit_reason": c["fit_reason"], "adjacent": c["fit"] == 1,
            "client_confirmation": "open" if c["fit"] == 1 else "not_needed",
            "demand": {"volume_max": vol_max, "volume_sum": vol_sum, "autocomplete_hits": len(ac_hits_l), "autocomplete_samples": sorted(ac_hits_l, key=len)[:4],
                       "paa_hits": len(paa_hits_l), "paa_samples": paa_hits_l[:3], "client_signal": client_sig, "gsc": g, "trend_note": c.get("trend_note"),
                       "basis": basis, "date": a.date},
            "competitor": {"set": "+".join(sorted(tiers)), "denominator": denom, "covering": len(cov), "share": share, "covering_domains": cov,
                           "table_stakes": table_stakes, "note": c.get("cover_note")},
            "compliance": comp, "conversion": c["conversion"], "effort": c["effort"],
            "score": {"demand": round(d_score, 1), "gap": round(gap, 1), "fit": FIT_PTS[c["fit"]], "conversion": CONV_PTS[c["conversion"]], "effort": EFF_PTS[c["effort"]], "total": total},
            "priority": prio, "status": status, "live_status": live_s, "live_url": live_u,
            "needs_client": c.get("needs_client", []), "decision_note": c.get("decision_note"), "owner": c.get("owner", "martin" if c["fit"] == 1 else "agent"),
            "evidence": ev,
        })
    # Gate A0 benchmark: median words of measured competitor HOMEPAGES (local tier). 70 % of it is the floor.
    from urllib.parse import urlparse
    import statistics
    mets = (jl(f"{run}/02-competitors/metrics.json") or []) + (jl(f"{run}/05-sitetree/own-metrics.json") or [])
    home_words = {}
    for m in mets:
        if m.get("status") != "ok":
            continue
        dom = next((d for d in comp_cfg if d in m["url"]), None)
        if dom and comp_cfg[dom]["tier"] == "local" and urlparse(m["url"]).path in ("", "/"):
            home_words[dom] = m["words"]
    own_home = next((m["words"] for m in mets if m.get("status") == "ok" and meta["domain"] in m["url"] and urlparse(m["url"]).path in ("", "/")), None)
    bench = None
    if home_words:
        med = statistics.median(home_words.values())
        bench = {"homepages_measured": home_words, "median_words": med, "floor_70pct": round(0.7 * med), "own_homepage_words": own_home,
                 "own_below_floor": own_home is not None and own_home < 0.7 * med}
    gsum = None
    if gsc and meta.get("gsc_groups"):
        gg = meta["gsc_groups"]
        brand = [r for r in gsc if re.search(gg["brand"], r[0])]
        train = [r for r in gsc if r not in brand and re.search(gg["training"], r[0])]
        rest = [r for r in gsc if r not in brand and r not in train]
        agg = lambda L: {"queries": len(L), "impressions": sum(r[2] for r in L), "clicks": sum(r[1] for r in L)}
        gsum = {"listed": agg(gsc), "brand": agg(brand), "training": agg(train), "patient_service": agg(rest), "totals_from_gsc_ui": meta.get("gsc_totals")}
    # R-S6: if fewer than 5 items reach A, the best quarter of the live items with total >= 65 becomes A.
    # Multi-page runs (meta.rs6_group = "audience" or "page_tag"): the rule runs once per group, so each page gets its own top.
    grp_key = meta.get("rs6_group")
    groups = {}
    for i in items: groups.setdefault(i[grp_key] if grp_key else "all", []).append(i)
    for g_items in groups.values():
      if sum(1 for i in g_items if i["priority"] == "A") < 5:
        live_i = sorted([i for i in g_items if i["priority"] in ("B", "C") and i["fit"] >= 2], key=lambda i: -i["score"]["total"])
        for i in live_i[: max(5, round(0.25 * len([x for x in g_items if x["priority"] != "cut"])))]:
            if i["score"]["total"] >= 65:
                i["priority"] = "A"
                i["decision_note"] = (i.get("decision_note") or "") + (" " if i.get("decision_note") else "") + "Stufe A durch Regel R-S6 (relative Spitze)."
    pool = {"meta": {**meta, "gsc_summary": gsum, "built": a.date, "spend_usd": round(spend, 4), "unreadable_competitors": sorted(set(comp_cfg) - readable), "benchmark": bench or meta.get("benchmark")},
            "services": cand.get("services", {}), "competitors": comp_cfg, "items": items}
    json.dump(pool, open(f"{run}/04-pool/pool.json", "w"), ensure_ascii=False, indent=1)
    by = {}
    for i in items: by[i["priority"]] = by.get(i["priority"], 0) + 1
    print(f"{len(items)} items -> {run}/04-pool/pool.json | priorities {by} | spend {spend:.4f} USD | unreadable {pool['meta']['unreadable_competitors']}")


if __name__ == "__main__":
    main()
