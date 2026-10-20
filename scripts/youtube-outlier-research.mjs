#!/usr/bin/env node
/**
 * YouTube outlier research for the health-practitioner channel.
 * Uses the YouTube Data API v3 with a restricted API key (public data only).
 * No external packages — Node builtins + fetch only.
 *
 *   node scripts/youtube-outlier-research.mjs
 */
import { readFileSync } from 'node:fs';

const ENV_PATH = new URL('../.secrets/youtube-api.env', import.meta.url);
const API_KEY = readFileSync(ENV_PATH, 'utf8').match(/YOUTUBE_API_KEY=(.+)/)[1].trim();

const SEED_KEYWORDS = [
  'white label web development',
  'automation for graphic designers',
  'agency tech stack',
  'zapier client onboarding workflow',
  'how brand designers scale',
  'creative agency backend systems',
  'freelance designer scale agency',
  'website speed for creative agencies',
];

const BASE = 'https://www.googleapis.com/youtube/v3';

async function apiGet(path, params) {
  const url = new URL(`${BASE}/${path}`);
  url.searchParams.set('key', API_KEY);
  for (const [k, v] of Object.entries(params)) url.searchParams.set(k, v);
  const res = await fetch(url);
  if (!res.ok) {
    const body = await res.text();
    throw new Error(`${path} failed: ${res.status} ${body.slice(0, 300)}`);
  }
  return res.json();
}

async function searchVideos(keyword) {
  const data = await apiGet('search', {
    part: 'snippet',
    q: keyword,
    type: 'video',
    maxResults: '15',
    order: 'viewCount',
    relevanceLanguage: 'en',
  });
  return (data.items || []).map((it) => ({
    videoId: it.id.videoId,
    channelId: it.snippet.channelId,
    title: it.snippet.title,
    channelTitle: it.snippet.channelTitle,
    publishedAt: it.snippet.publishedAt,
    seedKeyword: keyword,
  }));
}

async function getVideoStats(videoIds) {
  const stats = {};
  for (let i = 0; i < videoIds.length; i += 50) {
    const batch = videoIds.slice(i, i + 50);
    const data = await apiGet('videos', { part: 'statistics', id: batch.join(',') });
    for (const item of data.items || []) {
      stats[item.id] = Number(item.statistics.viewCount || 0);
    }
  }
  return stats;
}

async function getChannelAverages(channelIds) {
  const avg = {};
  const uniq = [...new Set(channelIds)];
  for (let i = 0; i < uniq.length; i += 50) {
    const batch = uniq.slice(i, i + 50);
    const data = await apiGet('channels', { part: 'statistics', id: batch.join(',') });
    for (const item of data.items || []) {
      const viewCount = Number(item.statistics.viewCount || 0);
      const videoCount = Number(item.statistics.videoCount || 1);
      avg[item.id] = viewCount / videoCount;
    }
  }
  return avg;
}

async function main() {
  const allVideos = [];
  for (const kw of SEED_KEYWORDS) {
    console.error(`Searching: ${kw}`);
    const results = await searchVideos(kw);
    allVideos.push(...results);
  }

  const videoStats = await getVideoStats(allVideos.map((v) => v.videoId));
  const channelAverages = await getChannelAverages(allVideos.map((v) => v.channelId));

  const enriched = allVideos.map((v) => {
    const views = videoStats[v.videoId] || 0;
    const channelAvg = channelAverages[v.channelId] || 0;
    const multiplier = channelAvg > 0 ? views / channelAvg : 0;
    return { ...v, views, channelAvg: Math.round(channelAvg), multiplier: Math.round(multiplier * 10) / 10 };
  });

  const outliers = enriched
    .filter((v) => v.multiplier >= 3)
    .sort((a, b) => b.multiplier - a.multiplier);

  console.log(JSON.stringify({ totalFound: enriched.length, outlierCount: outliers.length, outliers }, null, 2));
}

main().catch((err) => {
  console.error(err.message);
  process.exit(1);
});
