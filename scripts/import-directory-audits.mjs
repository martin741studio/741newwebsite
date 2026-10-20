#!/usr/bin/env node
/**
 * 741 Studio — Directory Citations & BrightLocal Audits Ingestion Worker
 * Aggregates client_citations and citation campaign logs into public.brightlocal_audits.
 *
 * Usage:
 *   node scripts/import-directory-audits.mjs --dry-run
 *   node scripts/import-directory-audits.mjs --apply
 */

import { readFileSync, existsSync } from 'node:fs';
import { resolve, join } from 'node:path';

const ROOT = process.cwd();
const SECRETS_PATH = join(ROOT, '.secrets', 'standup.env');

if (!existsSync(SECRETS_PATH)) {
  console.error('❌ .secrets/standup.env nicht gefunden');
  process.exit(1);
}

const env = Object.fromEntries(
  readFileSync(SECRETS_PATH, 'utf8')
    .split('\n')
    .filter(Boolean)
    .filter(l => !l.trimStart().startsWith('#'))
    .map(l => {
      const idx = l.indexOf('=');
      return [l.slice(0, idx).trim(), l.slice(idx + 1).trim()];
    })
);

const args = process.argv.slice(2);
const DRY_RUN = !args.includes('--apply');

async function getAuthToken() {
  const res = await fetch(`${env.SUPABASE_URL}/auth/v1/token?grant_type=password`, {
    method: 'POST',
    headers: { 'apikey': env.SUPABASE_ANON, 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: env.STANDUP_EMAIL, password: env.STANDUP_PASSWORD })
  });
  if (!res.ok) {
    throw new Error(`Auth failed (${res.status}): ${await res.text()}`);
  }
  const data = await res.json();
  return data.access_token;
}

// Client metadata & known audit context
const CLIENT_AUDIT_PROFILES = {
  '3f71ef33-8c74-4ea1-b2d3-0273c2e99649': {
    name: 'Praxis Suriya',
    audit_date: '2026-09-30',
    report_type: 'citation_tracker',
    nap_consistency_score: 100.00,
    duplicate_count: 0,
    average_rating: 5.00,
    review_count: 12,
    report_url: 'https://tools.brightlocal.com/seo-tools/admin/citation-builder/4139399',
    raw_summary: {
      campaign_id: '994242',
      location_id: '4139399',
      campaign_type: 'manual_submission_25',
      cost_usd: 80.00,
      notes: 'BrightLocal verified 30.09.2026. GBP NAP 100% consistent.'
    }
  },
  'f0a6730f-8f56-4c61-8085-1955f3bb285a': {
    name: 'Praxis Hüwel',
    audit_date: '2026-09-30',
    report_type: 'citation_tracker',
    nap_consistency_score: 98.00,
    duplicate_count: 0,
    average_rating: 5.00,
    review_count: 18,
    report_url: null,
    raw_summary: {
      campaign_type: 'brightlocal_network_update',
      notes: 'Campaign updated 02.09.2026, status verified 30.09.2026 across 38 live citations.'
    }
  },
  '444ac77b-747d-4855-89e5-12ac97d2363c': {
    name: 'Maria Brasse',
    audit_date: '2026-10-08',
    report_type: 'citation_builder',
    nap_consistency_score: 100.00,
    duplicate_count: 0,
    average_rating: 5.00,
    review_count: 1,
    report_url: 'https://tools.brightlocal.com/seo-tools/admin/citation-builder/4172000',
    raw_summary: {
      location_id: '4172000',
      reference_code: 'SHUIGURU-MAR-12051',
      campaign_type: 'manual_submission_25',
      cost_usd: 80.00,
      status: 'submitted_turnaround',
      notes: 'Ordered 08.10.2026. 25 manual submissions in progress.'
    }
  },
  'd01f4236-8674-45fe-a347-0751fa7b24de': {
    name: 'Naturheilpraxis Daniela Dumann',
    audit_date: '2026-10-08',
    report_type: 'citation_tracker',
    nap_consistency_score: 82.00,
    duplicate_count: 2,
    average_rating: 5.00,
    review_count: 31,
    report_url: null,
    raw_summary: {
      keeper_place_id: 'ChIJwdcWYxZRqEcR8RDtWZzHMgI',
      duplicate_alt_place_id: 'ChIJoalqkSVRqEcRbzKqYgZtGr8',
      resolution_date: '2026-10-09',
      notes: 'Dublette B closed permanently 09.10.2026; phone number typo on directory entry identified. 31 reviews aggregated across platforms.'
    }
  },
  'b6f6e303-50e4-4afb-a343-337206cec316': {
    name: 'STÜRZL Steuerstrafrecht',
    audit_date: '2026-10-08',
    report_type: 'citation_tracker',
    nap_consistency_score: 0.00,
    duplicate_count: 0,
    average_rating: null,
    review_count: 0,
    report_url: null,
    raw_summary: {
      audit_ref: 'B07.02',
      missing_core_directories: ['Das Örtliche', 'Gelbe Seiten', 'Das Telefonbuch'],
      notes: 'Core directory gap audit 08.10.2026. Tier 1 citations missing.'
    }
  }
};

async function main() {
  console.log('=== 741 Studio Directory Citations & BrightLocal Ingestion Worker ===');
  console.log(`Mode: ${DRY_RUN ? 'DRY-RUN (use --apply to write to Supabase)' : 'APPLY (writing to Supabase)'}\n`);

  const token = await getAuthToken();
  const headers = {
    'apikey': env.SUPABASE_ANON,
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  };

  // 1. Fetch current client_citations grouped by client
  const citRes = await fetch(`${env.SUPABASE_URL}/rest/v1/client_citations?select=*`, { headers });
  if (!citRes.ok) {
    throw new Error(`Failed to fetch client_citations: ${citRes.status} ${await citRes.text()}`);
  }
  const citations = await citRes.json();
  console.log(`Fetched ${citations.length} raw client_citations from Supabase.`);

  // Group citations by client_id
  const citationsByClient = {};
  for (const c of citations) {
    if (!citationsByClient[c.client_id]) citationsByClient[c.client_id] = [];
    citationsByClient[c.client_id].push(c);
  }

  const auditRecords = [];

  for (const [clientId, profile] of Object.entries(CLIENT_AUDIT_PROFILES)) {
    const clientCitations = citationsByClient[clientId] || [];
    const totalCount = clientCitations.length;
    
    // Status breakdown
    let liveCount = 0;
    let missingCount = 0;
    for (const c of clientCitations) {
      if (c.status === 'live') {
        liveCount++;
      } else if (c.status === 'missing' || c.status === 'planned') {
        missingCount++;
      }
    }

    // Include submitted count if Maria Brasse
    if (clientId === '444ac77b-747d-4855-89e5-12ac97d2363c') {
      const submitted = clientCitations.filter(c => c.status === 'submitted').length;
      profile.raw_summary.submitted_count = submitted;
    }

    const auditRecord = {
      client_id: clientId,
      audit_date: profile.audit_date,
      report_type: profile.report_type,
      nap_consistency_score: profile.nap_consistency_score,
      citation_count: totalCount,
      citation_live_count: liveCount,
      citation_missing_count: missingCount,
      duplicate_count: profile.duplicate_count,
      average_rating: profile.average_rating,
      review_count: profile.review_count,
      report_url: profile.report_url,
      raw_summary: profile.raw_summary
    };

    auditRecords.push({ clientName: profile.name, record: auditRecord });
  }

  console.log(`\nPrepared ${auditRecords.length} BrightLocal audit summaries:`);
  for (const { clientName, record } of auditRecords) {
    console.log(`• [${clientName}] Date: ${record.audit_date} | Citations: ${record.citation_count} (Live: ${record.citation_live_count}, Missing/Planned: ${record.citation_missing_count}) | NAP: ${record.nap_consistency_score}% | Rating: ${record.average_rating ?? 'N/A'} (${record.review_count} rev)`);
  }

  if (DRY_RUN) {
    console.log('\n[DRY-RUN completed. Run with --apply to commit to Supabase]');
    return;
  }

  // 2. Ingest into public.brightlocal_audits via UPSERT (on_conflict=client_id,audit_date,report_type)
  console.log('\nWriting to public.brightlocal_audits...');
  const payload = auditRecords.map(a => a.record);

  const upsertRes = await fetch(`${env.SUPABASE_URL}/rest/v1/brightlocal_audits?on_conflict=client_id,audit_date,report_type`, {
    method: 'POST',
    headers: {
      ...headers,
      'Prefer': 'resolution=merge-duplicates,return=representation'
    },
    body: JSON.stringify(payload)
  });

  if (!upsertRes.ok) {
    const errText = await upsertRes.text();
    throw new Error(`Failed to upsert brightlocal_audits (${upsertRes.status}): ${errText}`);
  }

  const inserted = await upsertRes.json();
  console.log(`✅ Successfully upserted ${inserted.length} audit records into public.brightlocal_audits!`);
}

main().catch(err => {
  console.error('❌ Ingestion Error:', err);
  process.exit(1);
});
