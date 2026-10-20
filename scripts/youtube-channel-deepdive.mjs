#!/usr/bin/env node
/**
 * Phase 1 step 4-6 of the YouTube SOP: channel deep-dive + negative evidence.
 * For each seed channel (found as an outlier in youtube-outlier-research.mjs),
 * pull its top and bottom performing videos to find repeated winning topics
 * and execution failures.
 *
 *   node scripts/youtube-channel-deepdive.mjs
 */
import { readFileSync } from 'node:fs';

const ENV_PATH = new URL('../.secrets/youtube-api.env', import.meta.url);
const API_KEY = readFileSync(ENV_PATH, 'utf8').match(/YOUTUBE_API_KEY=(.+)/)[1].trim();
const BASE = 'https://www.googleapis.com/youtube/v3';

// Seed channels: the real outliers from the first pass, dental-marketing focused.
const SEED_CHANNELS = [
  { name: 'Ravi Abuvala', id: null, handle: null },
  { name: 'The Futur', id: null, handle: null },
  { name: 'Paige Battcher', id: null, handle: null },
  { name: 'Rafael Rabl', id: null, handle: null },
  { name: 'ItsKeaton', id: null, handle: null },
  { name: 'GHL Experts', id: null, handle: null },
  { name: 'OpsKings', id: null, handle: null },
];

async function apiGet(path, params) {
  const url = new URL(`${BASE}/${path}`);
  url.searchParams.set('key', API_KEY);
  for (const [k, v] of Object.entries(params)) url.searchParams.set(k, v);
  const res = await fetch(url);
  if (!res.ok) throw new Error(`${path} failed: ${res.status} ${(await res.text()).slice(0, 200)}`);
  return res.json();
}

async function findChannelId(name) {
  const data = await apiGet('search', { part: 'snippet', q: name, type: 'channel', maxResults: '1' });
  return data.items?.[0]?.snippet?.channelId || null;
}

async function getUploadsPlaylist(channelId) {
  const data = await apiGet('channels', { part: 'contentDetails,statistics,snippet', id: channelId });
  const item = data.items?.[0];
  if (!item) return null;
  return {
    uploadsPlaylist: item.contentDetails.relatedPlaylists.uploads,
    subCount: Number(item.statistics.subscriberCount || 0),
    videoCount: Number(item.statistics.videoCount || 0),
    title: item.snippet.title,
  };
}

async function getAllPlaylistVideoIds(playlistId, max = 50) {
  const ids = [];
  let pageToken;
  while (ids.length < max) {
    const data = await apiGet('playlistItems', {
      part: 'contentDetails',
      playlistId,
      maxResults: '50',
      ...(pageToken ? { pageToken } : {}),
    });
    ids.push(...(data.items || []).map((i) => i.contentDetails.videoId));
    pageToken = data.nextPageToken;
    if (!pageToken) break;
  }
  return ids.slice(0, max);
}

async function getVideoStats(ids) {
  const out = [];
  for (let i = 0; i < ids.length; i += 50) {
    const batch = ids.slice(i, i + 50);
    const data = await apiGet('videos', { part: 'statistics,snippet', id: batch.join(',') });
    for (const item of data.items || []) {
      out.push({
        id: item.id,
        title: item.snippet.title,
        publishedAt: item.snippet.publishedAt,
        views: Number(item.statistics.viewCount || 0),
      });
    }
  }
  return out;
}

async function main() {
  const report = [];
  for (const seed of SEED_CHANNELS) {
    console.error(`Channel: ${seed.name}`);
    const channelId = await findChannelId(seed.name);
    if (!channelId) { console.error('  not found, skipping'); continue; }
    const info = await getUploadsPlaylist(channelId);
    if (!info) continue;
    const videoIds = await getAllPlaylistVideoIds(info.uploadsPlaylist, 50);
    const videos = await getVideoStats(videoIds);
    videos.sort((a, b) => b.views - a.views);
    const avg = videos.reduce((s, v) => s + v.views, 0) / (videos.length || 1);
    report.push({
      channel: info.title,
      subCount: info.subCount,
      videoCount: info.videoCount,
      avgViewsSampled: Math.round(avg),
      top5: videos.slice(0, 5).map((v) => ({ title: v.title, views: v.views, multiplier: Math.round((v.views / avg) * 10) / 10 })),
      bottom5: videos.slice(-5).map((v) => ({ title: v.title, views: v.views })),
    });
  }
  console.log(JSON.stringify(report, null, 2));
}

main().catch((err) => { console.error(err.message); process.exit(1); });
