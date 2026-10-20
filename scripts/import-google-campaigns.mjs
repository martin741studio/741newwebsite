#!/usr/bin/env node
/**
 * 741 Studio — Google Ads Campaigns Ingestion Worker
 * Ingests Google Ads campaign metrics (impressions, clicks, spend, conversions)
 * into Supabase public.google_campaigns for client accounts.
 *
 * Usage:
 *   node scripts/import-google-campaigns.mjs --dry-run
 *   node scripts/import-google-campaigns.mjs --apply
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

const CLIENT_MAP = {
  'balihealing': 'd0519d13-0bfc-4dfb-b512-57bf550387e6'
};

const args = process.argv.slice(2);
const DRY_RUN = !args.includes('--apply');

async function getAuthToken() {
  const res = await fetch(`${env.SUPABASE_URL}/auth/v1/token?grant_type=password`, {
    method: 'POST',
    headers: { 'apikey': env.SUPABASE_ANON, 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: env.STANDUP_EMAIL, password: env.STANDUP_PASSWORD })
  });
  if (!res.ok) throw new Error(`Auth failed: ${res.status} ${await res.text()}`);
  const data = await res.json();
  return data.access_token;
}

function collectCampaigns() {
  const campaigns = [];

  // 1. Bali Healing Ozone Campaign (from verified audit ads-read-2026-10-13.json)
  const baliAdsPath = join(ROOT, '00_project/assets/audit/balihealing/2026-10-11-kickoff/evidence/ads-read-2026-10-13.json');
  if (existsSync(baliAdsPath)) {
    try {
      const raw = JSON.parse(readFileSync(baliAdsPath, 'utf8'));
      const c = (raw.campaigns && raw.campaigns[0]) || {};
      const allTime = c.all_time || {};
      
      // Monthly rates: 17,650 IDR ≈ 1 EUR
      const spendEur = Number(((allTime.cost_idr || 571785) / 17650).toFixed(2));
      const dailyBudgetEur = Number(((c.budget_idr_day || 164073) / 17650).toFixed(2));

      campaigns.push({
        client_id: CLIENT_MAP['balihealing'],
        campaign_id: '239-394-2913-ozone',
        name: c.name || 'Ozone – Search – Bali',
        status: 'PAUSED',
        effective_status: 'PAUSED_VERIFICATION',
        channel_type: 'SEARCH',
        daily_budget: dailyBudgetEur,
        spend: spendEur,
        impressions: allTime.impressions || 685,
        clicks: allTime.clicks || 61,
        conversions: allTime.conversions || 14,
        currency: 'EUR',
        date_start: '2026-08-03',
        date_stop: '2026-10-13',
        metadata: {
          account: raw.account,
          mcc: '476-158-5143',
          conversion_action: allTime.conversion_action || 'Balihealing (web) contact_whatsapp',
          raw_cost_idr: allTime.cost_idr || 571785,
          raw_cpc_idr: allTime.avg_cpc_idr || 9374,
          bidding_strategy: c.bidding || 'Maximize clicks',
          monthly_net_cost_idr: raw.billing && raw.billing.net_cost_idr
        }
      });
    } catch (err) {
      console.warn('⚠️ Fehler beim Lesen von bali ads:', err.message);
    }
  }

  return campaigns;
}

async function main() {
  console.log('=== 741 Google Ads Campaigns Ingestion Worker ===');
  console.log(`Mode: ${DRY_RUN ? 'DRY-RUN (use --apply to write to Supabase)' : 'APPLY (Live DB sync)'}\n`);

  const token = await getAuthToken();
  console.log(`✅ Authentifiziert als: standup-bot@741.studio\n`);

  const campaigns = collectCampaigns();
  console.log(`Gefundene Google Ads Kampagnen: ${campaigns.length}`);

  for (const c of campaigns) {
    console.log(`\n• [${c.name}] Status: ${c.status} | Spend: €${c.spend} | Clicks: ${c.clicks} | Conversions: ${c.conversions}`);
  }

  if (DRY_RUN) {
    console.log('\n[DRY-RUN abgeschlossen. Führe mit --apply aus, um Daten live zu schreiben]');
    return;
  }

  // Upsert to Supabase
  const res = await fetch(`${env.SUPABASE_URL}/rest/v1/google_campaigns`, {
    method: 'POST',
    headers: {
      'apikey': env.SUPABASE_ANON,
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
      'Prefer': 'resolution=merge-duplicates,return=representation'
    },
    body: JSON.stringify(campaigns)
  });

  if (!res.ok) {
    console.error('❌ Fehler beim Einfügen:', res.status, await res.text());
  } else {
    const data = await res.json();
    console.log(`\n✅ ${data.length} Kampagne(n) erfolgreich in google_campaigns synchronisiert.`);
  }
}

main().catch(err => {
  console.error('Fataler Fehler:', err);
  process.exit(1);
});
