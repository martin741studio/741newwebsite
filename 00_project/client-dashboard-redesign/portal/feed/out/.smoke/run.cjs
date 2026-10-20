const esc=s=>String(s??'');const apGuide=(p,t)=>'<aside>'+t+'</aside>';const apOn=()=>true;const apOpenCount=()=>2;const apRenderClient=()=>'<div>decisions</div>';const renderOnboarding=()=>'<div>onb</div>';const renderGrants=()=>'<div>grants</div>';const renderMaterials=()=>'<div>mat</div>';const renderChat=()=>'<div>chat</div>';const rerender=()=>{};const applyShellLang=()=>{};const $=()=>({});const document={getElementById:()=>null};const window={scrollTo(){},addEventListener(){}};const history={pushState(){},replaceState(){}};const location={hash:''};const bundleIsAdmin=true;let adminSub='dash';const closeReport=()=>{};const openReport=()=>{};const fetch=()=>Promise.reject(new Error('x'));/* ---------- Dashboard (neu) · 2026-10-13 ----------
   Client view for pilot clients (Bali Healing). Data comes from a JSON feed (DSH_FEEDS) that 741 writes after each check.
   Decisions, setup and chat reuse the existing modules. All names start with dsh/dz- to avoid clashes. */
const DSH_FEEDS = {
  'd0519d13-0bfc-4dfb-b512-57bf550387e6': 'https://clients.741.studio/r/a331bf716f08/dashboard.json',   // Bali Healing (en)
  'f0a6730f-8f56-4c61-8085-1955f3bb285a': 'https://clients.741.studio/r/68044e8de1b5/dashboard.json',   // Praxis Hüwel (de)
  'd01f4236-8674-45fe-a347-0751fa7b24de': 'https://clients.741.studio/r/f92ed4298f5c/dashboard.json',   // Naturheilpraxis Daniela Dumann (de)
  'b6f6e303-50e4-4afb-a343-337206cec316': 'https://clients.741.studio/r/e006e37becd5/dashboard.json',   // STÜRZL Steuerstrafrecht (de)
  'b84427b9-57bc-4145-83fc-ec284d2de785': 'https://clients.741.studio/r/92c3a6769ec0/dashboard.json',   // Johni Jaya Motor (en)
  '3f71ef33-8c74-4ea1-b2d3-0273c2e99649': 'https://clients.741.studio/r/8dbd937730d2/dashboard.json',   // Praxis Suriya (de)
  '444ac77b-747d-4855-89e5-12ac97d2363c': 'https://clients.741.studio/r/5f46411185b2/dashboard.json',   // Maria Brasse (de)
  'fbcc70d1-4c56-437c-b5fb-8056e48d3f62': 'https://clients.741.studio/r/42d4bf7a8982/dashboard.json',   // Rabenmütter Shop (de)
  'cc5ad406-d06d-4b5a-a33c-3386b9e3de60': 'https://clients.741.studio/r/970008794dd5/dashboard.json'    // Kamil Böyük (de, reports only)
};
const DSH = { d: null, loaded: null, view: 'overview', profile: 'nhc', chat: false, err: null };
let DD = null;
const dshFmt = n => new Intl.NumberFormat('en-US').format(n);
const DSHS = {
  green: ['green', 'Fine', '<svg viewBox="0 0 12 12"><circle cx="6" cy="6" r="5.5" fill="currentColor"/></svg>'],
  amber: ['amber', 'Needs you', '<svg viewBox="0 0 12 12"><path d="M6 1 11.5 11H.5z" fill="currentColor"/></svg>'],
  red: ['red', 'Blocked', '<svg viewBox="0 0 12 12"><path d="M4 .5h4L11.5 4v4L8 11.5H4L.5 8V4z" fill="currentColor"/></svg>'],
  grey: ['grey', 'No data', '<svg viewBox="0 0 12 12"><circle cx="6" cy="6" r="4.8" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>']
};
const dshSt = (c, w) => `<span class="dz-st dz-${c}">${DSHS[c][2]}${w || DSHS[c][1]}</span>`;
const dshMg = (pose, text) => apGuide(pose, text, true);
function dshOn(b) { return !!(b && b.client && DSH_FEEDS[b.client.id]); }
function dshLoad(b) {
  if (DSH.loaded === b.client.id) return;
  DSH.loaded = b.client.id; DSH.d = null; DSH.err = null;
  fetch(DSH_FEEDS[b.client.id] + '?v=' + Date.now()).then(r => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
    .then(j => { DSH.d = j; }).catch(e => { DSH.err = String(e.message || e); }).finally(() => rerender());
}
function dshPush(v, extra) { try { history.pushState(Object.assign({ dsh: v }, extra || {}), '', '#d/' + v); } catch (e) {} }
function dshGo(v) { DSH.view = v; DSH.chat = false; dshPush(v); rerender(); window.scrollTo(0, 0); }
/* Browser Back stays inside the dashboard: every view is a history entry. An open report closes first. */
window.addEventListener('popstate', e => {
  const rv = document.getElementById('report-viewer');
  if (rv && rv.style.display !== 'none' && rv.style.display !== '') { closeReport(); return; }
  const st = e.state;
  if (st && st.dsh) {
    if (typeof bundleIsAdmin !== 'undefined' && bundleIsAdmin && adminSub !== 'dash') adminSub = 'dash';
    DSH.view = st.dsh; DSH.chat = false; rerender(); window.scrollTo(0, 0); return;
  }
  if (typeof adminSub !== 'undefined' && adminSub === 'dash') { adminSub = null; rerender(); }
});
/* Reports open in the portal's own viewer (no page change). The back link inside a report closes the viewer. */
function dshOpenReport(url, title) {
  openReport(url, title);
  try { history.pushState({ dshReport: 1, dsh: DSH.view }, '', '#d/' + DSH.view); } catch (e) {}
  const f = document.getElementById('rv-frame');
  f.addEventListener('load', function once() {
    f.removeEventListener('load', once);
    try { f.contentDocument.querySelectorAll('a.backlink').forEach(a => { a.addEventListener('click', ev => { ev.preventDefault(); history.back(); }); }); } catch (e) {}
  });
}
function dshSetP(p) { DSH.profile = p; rerender(); }
function dshToggleChat() { DSH.chat = !DSH.chat; rerender(); const h = document.getElementById('chat-history'); if (h) h.scrollTop = h.scrollHeight; }
/* Steps are derived from real data: access step is done when all required platforms are granted, start step when the programme has a start date. Display only, nothing is written. */
function dshSteps(b) {
  const grantsOk = (b.grants || []).filter(g => g.required).every(g => ['erteilt', 'geprueft', 'entfaellt'].includes(g.status));
  return (b.steps || []).map(s => {
    const accessStep = /zugang|zugaenge|access/i.test((s.kind || '') + ' ' + (s.title || ''));
    const done = s.status === 'erledigt' || (s.kind === 'start' && b.program && b.program.start_date) || (accessStep && grantsOk);
    return done && s.status !== 'erledigt' ? Object.assign({}, s, { status: 'erledigt' }) : s;
  });
}
function dshOpenSteps(b) { return dshSteps(b).filter(s => s.status !== 'erledigt').length; }
/* Decision cards come from the approval module. The client sees released items. The admin preview also shows drafts, marked as draft. */
function dshDecItems(b) {
  if (typeof apOn !== 'function' || !b.apReady) return [];
  const all = (b.apItems || []).filter(i => i.status !== 'withdrawn');
  return DSH.admin ? all : all.filter(i => i.status !== 'draft');
}
function dshDecOpen(b) { return dshDecItems(b).filter(i => i.status === 'open' || i.status === 'draft'); }
function dshTabs(b, cur) {
  const nDec = dshDecOpen(b).length, nSet = dshOpenSteps(b);
  const T = [['overview', 'Overview'], ['results', 'Results'], ['plan', 'Plan']];
  if (dshDecItems(b).length) T.push(['decisions', 'Decisions', nDec]);
  T.push(['reports', 'Reports']); if (nSet) T.push(['setup', 'Setup', nSet]);
  return `<nav class="dz-tabs">${T.map(t => `<a class="dz-tab ${cur === t[0] ? 'dz-on' : ''}" href="#" onclick="dshGo('${t[0]}');return false">${t[1]}${t[2] ? `<span class="dz-n">${t[2]}</span>` : ''}</a>`).join('')}</nav>`;
}
function dshSub(cur) {
  const T = [['enquiries', 'Enquiries'], ['found', 'Found on Google'], ['reviews', 'Reviews'], ['ads', 'Ads'], ['backlinks', 'Backlinks']];
  const P = DD.profiles || [['nhc', 'Natural Health Center'], ['beauty', 'Beauty Clinic']];
  return `<div class="dz-sub">${T.map(t => `<a class="dz-pill ${cur === t[0] ? 'dz-on' : ''}" href="#" onclick="dshGo('results/${t[0]}');return false">${t[1]}</a>`).join('')}<span class="dz-sw" role="group" aria-label="Google profile">${P.map(p => `<button class="${DSH.profile === p[0] ? 'dz-on' : ''}" onclick="dshSetP('${p[0]}')">${p[1]}</button>`).join('')}</span></div>`;
}
function dshBars(vals,labels,o={}){
 const W=o.w||340,H=o.h||96,pad=18,n=vals.length,gw=(W)/n,bw=Math.min(34,gw-8);const mx=Math.max(...vals.filter(v=>v!=null),1);
 let g=`<defs><pattern id="h${o.id||0}" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="#fffefa"/><rect width="2.4" height="6" fill="#b9b19b"/></pattern></defs>`;
 vals.forEach((v,i)=>{const x=i*gw+(gw-bw)/2;const part=o.partial===i;const last=o.full===i;
  if(v==null){g+=`<rect x="${x}" y="${H-pad-14}" width="${bw}" height="14" rx="3" fill="none" stroke="#c9c2ae" stroke-dasharray="3 3"/>`;}
  else{const h=Math.max(2,(H-pad-16)*v/mx);g+=`<rect x="${x}" y="${H-pad-h}" width="${bw}" height="${h}" rx="3" fill="${part?`url(#h${o.id||0})`:last?'var(--dz-bar-now)':'var(--dz-bar)'}" ${part?'stroke="#b9b19b"':''}/><text class="${last||part?'dz-v':''}" x="${x+bw/2}" y="${H-pad-h-4}" text-anchor="middle">${dshFmt(v)}</text>`;}
  g+=`<text x="${x+bw/2}" y="${H-3}" text-anchor="middle">${labels[i]}</text>`;});
 return `<svg class="dz-bars" viewBox="0 0 ${W} ${H}" role="img" aria-label="${o.aria||'Bar chart'}">${g}</svg>`;
}
function dshEnq(p,i){return {calls:DD[p].calls[i],web:DD[p].web[i],dir:DD[p].dir[i]}}
function dshSeg(n,total){n=n||5;total=total||13;let h='';for(let i=1;i<=total;i++)h+=`<i class="${i<n?'dz-d':i==n?'dz-n':''}"></i>`;return `<span class="dz-seg" aria-label="Week ${n} of ${total}">${h}</span>`}
function dshTile(title,vals,labels,note,o){const v=vals,last=v[5];const prev=v[4];const d=(last!=null&&prev!=null)?last-prev:null;
 return `<div class="dz-card dz-tile"><div class="dz-q">${title}</div><div class="dz-num">${last==null?'—':dshFmt(last)}<span class="dz-dl">${d==null?'':(d>0?'+':'')+d+' vs Aug'}</span></div><div class="dz-d">${note}</div>${dshBars(v,labels,{partial:6,full:5,id:o,aria:title})}</div>`}
function dshEnquiries(){
 const P=DSH.profile,d=DD[P];const wa=DD.wa;const lab=DD.months;
 const a=P=='nhc'?d.calls[5]+d.web[5]+d.dir[5]+wa[5]:null;
 return `${dshTabs(DSH.b,'results')}${dshSub('enquiries')}<h1 class="dz-t">Do I get more enquiries?</h1>
 <p class="dz-lead">${P=='nhc'?`<b>${dshFmt(a)} contact actions in September.</b> That is ${dshFmt(Math.abs(a-(d.calls[4]+d.web[4]+d.dir[4]+wa[4])))} fewer than in August. Calls, website visits, direction requests and WhatsApp taps each dipped a little.`:'<b>The Beauty Clinic profile had 158 Google actions in September</b> (2 calls, 59 website visits, 97 direction requests). Earlier months are not stored yet.'}</p>
 <div class="dz-grid2">
  ${dshTile('Taps on Call',d.calls,lab,'Button taps on your Google profile. Not proven calls.','e1')}
  ${dshTile('Visits to your website from Google',d.web,lab,'Clicks, not enquiries.','e2')}
  ${dshTile('Asked for directions',d.dir,lab,'Google adjusts this count after the fact.','e3')}
  ${dshTile('Taps on WhatsApp (website)',wa,lab,P=='nhc'?'Counted since 2 Aug. Before that: not tracked, not zero.':'Website-wide, not per profile. Counted since 2 Aug.','e4')}
 </div>
 <div class="dz-grid2 dz-gap2"><div class="dz-gapcard"><h3>Leads you told us about</h3><p class="dz-mut">Your website has no enquiry form, so no leads are counted yet.</p></div>
  <div class="dz-gapcard">${dshMg('think','Booked jobs: not tracked yet. Send us one number each month, for example from WhatsApp Business. Then we can show what an enquiry costs.','Martin thinks about booked jobs')}<h3>Booked jobs</h3><p class="dz-mut">Not tracked yet.</p></div></div>
 <p class="dz-foot">Hatched bar: 1–13 Oct, still counting. Dashed slot: not tracked yet. Google numbers read 13 Oct. The newest 2–3 days can still grow.</p>`}
function dshFound(){
 const P=DSH.profile;
 const rows=DD.map;const win=rows.filter(r=>r[1]>=25),cl=rows.filter(r=>r[1]>=5&&r[1]<25),mi=rows.filter(r=>r[1]<5);
 const kw=r=>`<div class="dz-kw"><span>${r[0]}</span><b>${r[1]} of 49</b></div>`;
 const aiPlatform=[['ChatGPT',55.6],['Gemini',26.5],['Google AI mode',36.8]];
 const cell=p=>{const x=Math.round(p/100*9);const z=x==0?0:x<=2?1:x<=4?2:x<=6?3:4;return `<div class="dz-hz${z}">${p==12.5?'1 of 8':x+' of 9'}</div>`};
 return `${dshTabs(DSH.b,'results')}${dshSub('found')}<h1 class="dz-t">Am I easier to find?</h1>
 ${P=='nhc'?`<p class="dz-lead"><b>On the map you are in the top 3 on 19 of 49 spots for "ozone therapy"</b> (12 Oct). In September it was 28 of 49. For "naturopath" you are top 3 on 35 of 49.</p>
 <div class="dz-grid3"><div class="dz-card"><div class="dz-q">On the map</div><div class="dz-big">19 of 49</div><p class="dz-sentence">Top-3 coverage for "ozone therapy". <span class="dz-mut">SoLV 38.78%</span></p></div>
 <div class="dz-card"><div class="dz-q">In normal results</div><div class="dz-big">${DD.gsc.pos}</div><p class="dz-sentence">Average position in Google Search, page 2. July: ${DD.gsc.posJul}.</p></div>
 <div class="dz-card"><div class="dz-q">In AI answers</div><div class="dz-big">5 of 9</div><p class="dz-sentence">ChatGPT names you in about 5 of 9 checks. Gemini about 2, Google AI mode about 3 (23 Sep).</p></div></div>
 <div class="dz-card dz-gap2"><h2>Ozone therapy on the map</h2><p class="dz-mut">Each dot is one spot around the clinic. The map shows the grid of an earlier scan. The new grid needs the 49 points saved with each scan.</p>
  <img src="https://lf-static-v2.localfalcon.com/image/17f404087637806" alt="Grid map for ozone therapy" style="max-width:100%;border-radius:10px;margin-top:10px;border:1px solid var(--dz-line)" loading="lazy"></div>
 <h2 class="dz-gap2">Where you win, where you are close, where you are missing</h2>
 <div class="dz-cols3 dz-gap"><div class="dz-card"><div class="dz-st dz-green">${DSHS.green[2]}You win · 25+ of 49</div>${win.map(kw).join('')}</div><div class="dz-card"><div class="dz-st dz-amber">${DSHS.amber[2]}Close · 5–24 of 49</div>${cl.map(kw).join('')}</div><div class="dz-card"><div class="dz-st dz-grey">${DSHS.grey[2]}Missing · under 5</div>${mi.map(kw).join('')}</div></div>
 <p class="dz-mut dz-s dz-gap">A selection of your keywords is shown. Scan dates differ (23 Sep to 12 Oct). Only "ozone therapy" has a series with the same settings. Different scan settings are not comparable.</p>
 <div class="dz-card dz-gap2"><h2>Ozone therapy: who is ahead?</h2><table class="dz-t"><tr><th>Business</th><th>Reviews</th><th>Top 3 on the map</th></tr><tr><td><b>Blood Ozone Bali Therapy</b></td><td>128 (5 Oct)</td><td>98% (21 Sep)</td></tr><tr><td><b>You</b></td><td>100 (13 Oct)</td><td>39% (12 Oct)</td></tr></table><p class="dz-mut dz-s dz-gap">Dates differ. The gap to the leader is mostly review count and pace.</p></div>
 <div class="dz-card dz-gap2"><h2>In AI answers</h2><p class="dz-mut">How often each AI tool named you in 9 checks per keyword. One run, 23 Sep. No trend before 3 runs.</p><div class="dz-heat dz-gap"><div class="dz-h"></div><div class="dz-h">ChatGPT</div><div class="dz-h">Gemini</div><div class="dz-h">Google AI mode</div>${DD.ai.map(r=>`<div class="dz-k">${r[0]}</div>${cell(r[1])}${cell(r[2])}${cell(r[3])}`).join('')}</div></div>
 <div class="dz-card dz-gap2"><div class="dz-q">Profile and site readiness</div><div class="dz-big">45 of 100</div><p class="dz-sentence">Our own check of your profile and site (13 Oct). It is not a rank against other clinics.</p></div>`
 :`<p class="dz-lead"><b>On the map, the Beauty Clinic is missing for 13 of 14 treatments</b> (0 of 49 spots). Only "hydraglo facial" shows up, on 1 of 49 spots. This is the biggest gap in the account.</p>
 <div class="dz-card"><div class="dz-st dz-grey">${DSHS.grey[2]}Missing · 0 of 49</div>${DD.beautyMap.map(k=>`<div class="dz-kw"><span>${k}</span><b>0 of 49</b></div>`).join('')}<div class="dz-kw"><span>hydraglo facial</span><b>1 of 49</b></div></div>
 <p class="dz-mut dz-s dz-gap">First scan 23 Sep. The Beauty Clinic has 10 reviews and 1 Google category.</p>`}`}
function dshReviews(){
 const P=DSH.profile,r=DD.rev[P];const lead=DD.rev.nhc.leader,tg=lead*2;
 const mx=Math.max(r.n,lead,tg);const row=(l,v,c)=>`<div class="dz-row"><span class="dz-l">${l}</span><span class="dz-b"><i style="width:${v/mx*100}%;background:${c}"></i></span><span class="dz-c">${v}</span></div>`;
 return `${dshTabs(DSH.b,'results')}${dshSub('reviews')}<h1 class="dz-t">Do people trust me?</h1>
 <div class="dz-grid3"><div class="dz-card"><div class="dz-q">Rating</div><div class="dz-big">${r.star.toFixed(1)} ★</div></div><div class="dz-card"><div class="dz-q">Reviews</div><div class="dz-big">${r.n}</div></div><div class="dz-card"><div class="dz-q">Without a reply</div><div class="dz-big">${r.unans}</div><p class="dz-mut">${P=='nhc'?'79 of 100 have a reply. The 8 newest do not (latest 29 Sep).':'2 reviews wait for a reply.'}</p></div></div>
 ${P=='nhc'?`<div class="dz-card dz-gap2"><h2>Compared with the local leader</h2>${row('You',r.n,'var(--dz-ink)')}${row('Leader',lead,'#8f8566')}${row('Target',tg,'#d7cfb8')}<p class="dz-sentence"><b>${lead-r.n} more reviews to match the leader. ${tg-r.n} to reach the target</b> of twice the leader. The leader is Blood Ozone Bali Therapy (128 reviews, 5 Oct).</p></div>
 <div class="dz-card dz-gap2"><h2>New reviews per month, 2026</h2>${dshBars(DD.rev.nhc.per,DD.rev.nhc.months,{id:'r1',w:420,h:110,aria:'New reviews per month'})}<p class="dz-mut dz-s">Reviews arrive in bursts with long gaps. A steady trickle is what Google and AI tools trust. The pace needed starts once we set a target date.</p></div>`
 :`<div class="dz-gapcard dz-gap2"><h3>Leader for the Beauty Clinic</h3><p class="dz-mut">Not measured yet. We read the leader's review count with the next scan.</p></div>`}`}
function dshAds(){const a=DD.ads;
 return `${dshTabs(DSH.b,'results')}${dshSub('ads')}<h1 class="dz-t">What do my ads do?</h1>
 <div class="dz-banner dz-red">${dshSt('red','Paused')}<span><b>Paused since 1 Oct.</b> Google's verification is open. Upload your business licence (NIB). The check takes 1 to 10 days. Data to 12 Oct.</span></div>
 <div class="dz-grid3"><div class="dz-card"><div class="dz-q">Spent (campaign cost, all time)</div><div class="dz-big dz-plain">IDR ${dshFmt(a.spent)}</div></div><div class="dz-card"><div class="dz-q">WhatsApp clicks from ads</div><div class="dz-big dz-plain">${a.wa}</div><p class="dz-mut">from ${a.clicks} ad clicks</p></div><div class="dz-card"><div class="dz-q">Cost per WhatsApp click</div><div class="dz-big">IDR ${dshFmt(a.per)}</div></div></div>
 <p class="dz-sentence dz-gap"><b>IDR ${dshFmt(a.spent)} ÷ ${a.wa} WhatsApp clicks = IDR ${dshFmt(a.per)} each.</b> Since 2 Aug every WhatsApp click from an ad counts as a result. We see the click, not the conversation.</p>
 <div class="dz-gapcard dz-gap">${dshMg('think','Booked jobs: not tracked yet. Tell us each month how many WhatsApp chats became bookings.','Martin thinks about booked jobs')}<h3>Weekly spend and results</h3><p class="dz-mut">No weekly numbers are stored yet. The weekly view starts when the ads restart.</p></div>
 <p class="dz-foot">Billing shows about 13% more than campaign cost because of tax. This page shows campaign cost.</p>`}
function dshBacklinks(){const f=DD.funnel;const mx=f[0][1];
 return `${dshTabs(DSH.b,'results')}${dshSub('backlinks')}<h1 class="dz-t">Who links to me?</h1>
 <p class="dz-lead"><b>Of 149 requests, 9 became article offers. No link is live yet.</b> The first articles go live in October.</p>
 <div class="dz-card">${f.map(r=>`<div class="dz-row"><span class="dz-l">${r[0]}</span><span class="dz-b"><i style="width:${r[1]/mx*100}%"></i></span><span class="dz-c">${r[1]}</span></div>`).join('')}<p class="dz-mut dz-s">Since 25 Sep. Messages and accepted requests both read 38. We confirm the numbers with the outreach sheet.</p></div>
 <div class="dz-grid3 dz-gap2"><div class="dz-card dz-tile"><div class="dz-q">Links we can use</div><div class="dz-num">—</div><div class="dz-d">Not rated yet</div></div><div class="dz-card dz-tile"><div class="dz-q">Broken links to fix</div><div class="dz-num">25</div><div class="dz-d">Checked 11 Oct</div></div><div class="dz-card dz-tile"><div class="dz-q">Real sites linking</div><div class="dz-num">—</div><div class="dz-d">Not rated yet</div></div></div>
 <p class="dz-mut dz-gap">${dshSt('grey','Ignored')} About 960 spam links appeared after 23 Sep (73 links then, 1,034 on 11 Oct). They are not from you. Google usually ignores such links.</p>`}
function dshPlan(){const col=s=>DD.tracks.filter(t=>t[0]==s);const c=(s,k)=>`<div class="dz-col"><h3>${s}<span class="dz-mut">${col(s).length}</span></h3>${col(s).map(t=>`<div class="dz-trk"><b>${t[1]}</b><div class="dz-o">${t[2]}</div><div class="dz-o">${t[3]}</div></div>`).join('')}</div>`;
 return `${dshTabs(DSH.b,'plan')}<h1 class="dz-t">The plan</h1><p class="dz-lead">13 jobs in three stages. Open a job in the full roadmap for the details.</p>
 <div class="dz-tr">${c('Not started')}${c('In progress')}${c('Live')}</div>
 <div class="dz-card dz-gap2 dz-tree"><h2>Site structure</h2><p class="dz-mut">As planned on 18 Sep. Open a branch to see what changes.</p>${DD.tree.map(b=>`<details><summary><span>${b[0]}</span><span class="dz-badge ${/new/.test(b[1])?'dz-new':/update/.test(b[1])?'dz-up':''}">${b[1]}</span></summary>${b[2].length?`<ul style="margin:8px 0 0 20px;font-size:15px">${b[2].map(x=>`<li>${x}</li>`).join('')}</ul>`:'<p class="dz-mut dz-s" style="margin-top:6px">No change planned.</p>'}</details>`).join('')}</div>
 <div class="dz-card dz-gap2"><h2>Content plan</h2><p class="dz-mut">45 topics from real searches. 19 are top priority. Live so far: not counted yet.</p><p class="dz-sentence">Next up: Craniosacral Therapy · Prolozone Injection · NAET Allergy Treatment · Reiki in Canggu · Ozone Insufflation vs Autohemotherapy · "Bali Healing Therapy" landing page.</p></div>
 <a class="dz-btn dz-gap" href="#" onclick="dshOpenReport('${DD.meta.roadmap_url}','SEO and Content Roadmap');return false">Open the full roadmap</a>`}
function dshReports(){return `${dshTabs(DSH.b,'reports')}<h1 class="dz-t">Reports</h1><p class="dz-lead">Every report with its date. Older versions point to the current page.</p>
 <div class="dz-card"><table class="dz-t"><tr><th>Report</th><th>Period</th><th>State</th><th></th></tr>${DD.reports.map(r=>`<tr><td><b>${r[0]}</b></td><td>${r[1]}</td><td>${/Replaced/.test(r[3])?dshSt('grey','Replaced'):dshSt('green','Current')}<div class="dz-mut dz-s">${/Replaced/.test(r[3])?r[3]:''}</div></td><td>${r[2]?`<a class=\"dz-btn dz-o\" href=\"#\" onclick=\"dshOpenReport('${r[4]}','${r[0].replace(/'/g,'')}');return false\">Open</a>`:''}</td></tr>`).join('')}</table></div>`}

function dshOverview(b) {
  const a = dshEnq('nhc', 5), pv = dshEnq('nhc', 4); const tot = a.calls + a.web + a.dir + DD.wa[5], totB = pv.calls + pv.web + pv.dir + DD.wa[4];
  const g6 = DD.nhc.calls.map((_, i) => DD.nhc.calls[i] + DD.nhc.web[i] + DD.nhc.dir[i]);
  const bn = DD.banner, nDec = (typeof apOn === 'function' && apOn(b)) ? apOpenCount(b) : 0, nSet = dshOpenSteps(b);
  const needs = dshDecOpen(b).map(i => `<li>${dshSt('amber', 'Needs you')}<span class="dz-tx"><b>${esc(i.title)}</b>${i.status === 'draft' ? ' <span class="dz-badge">Draft: not released to the client</span>' : ''}</span><a class="dz-btn" href="#" onclick="dshGo('decisions');return false">Decide</a></li>`);
  DD.needs.filter(n => n.go !== 'decisions').forEach(n => needs.push(`<li>${dshSt('amber', 'Needs you')}<span class="dz-tx">${n.t}</span><a class="dz-btn dz-o" href="#" onclick="dshGo('${n.go}');return false">${n.btn}</a></li>`));
  if (nSet) needs.push(`<li>${dshSt('amber', 'Needs you')}<span class="dz-tx"><b>Setup: ${nSet} step${nSet > 1 ? 's' : ''} still open.</b></span><a class="dz-btn dz-o" href="#" onclick="dshGo('setup');return false">Open setup</a></li>`);
  const nNeeds = needs.length;
  return `${dshTabs(b, 'overview')}
 <div class="dz-strip"><b>${esc(DD.meta.client)}</b><span class="dz-mut">Week ${DD.meta.week} of ${DD.meta.weeks}</span>${dshSeg()}<span class="dz-mut">Last update from 741: ${DD.meta.last_update}</span></div>
 ${bn ? `<div class="dz-banner dz-${bn.color}">${dshSt(bn.color, bn.label)}<span>${bn.html} <b>${nNeeds} thing${nNeeds === 1 ? '' : 's'} need${nNeeds === 1 ? 's' : ''} you.</b></span></div>` : ''}
 ${dshMg(DD.guide.overview.pose, DD.guide.overview.text)}
 <div class="dz-grid3">
  <div class="dz-card"><div class="dz-q">Do I get more enquiries?</div><div class="dz-big">${dshFmt(tot)}</div><p class="dz-sentence"><b>contact actions in September</b>, ${dshFmt(Math.abs(tot - totB))} fewer than in August. All four channels dipped a little.</p>
   ${dshBars(g6, DD.months, { partial: 6, full: 5, id: 'o1', aria: 'Google profile actions per month' })}<p class="dz-mut"><b>Beauty Clinic:</b> ${DD.beauty.calls[5] + DD.beauty.web[5] + DD.beauty.dir[5]} Google actions in September (2 calls, 59 website visits, 97 direction requests).</p><div class="dz-chk">Google profile actions per month, Natural Health Center. WhatsApp taps: ${DD.wa[5]} in September. Checked by 741 · ${DD.meta.as_of}</div><a class="dz-btn dz-o dz-gap" href="#" onclick="dshGo('results/enquiries');return false">See enquiries</a></div>
  <div class="dz-card"><div class="dz-q">Am I easier to find?</div><div class="dz-big">${DD.gsc.sep}</div><p class="dz-sentence"><b>search clicks in September</b>, ${DD.gsc.aug - DD.gsc.sep} fewer than August. Average position ${DD.gsc.pos} (page 2), up from ${DD.gsc.posJul} in July.</p>
   <p class="dz-mut">On the map: top 3 on 19 of 49 spots for "ozone therapy" (12 Oct). <b>Biggest gap: the Beauty Clinic is missing on the map for 13 of 14 treatments.</b></p><div class="dz-chk">Checked by 741 · ${DD.meta.as_of}</div><a class="dz-btn dz-o dz-gap" href="#" onclick="dshGo('results/found');return false">See where you show up</a></div>
  <div class="dz-card"><div class="dz-q">What is 741 doing?</div><p class="dz-sentence"><b>This week:</b> ${DD.work.this_week}</p>
   <p class="dz-mut"><b>Done recently:</b> ${DD.work.done}</p><div class="dz-chk">Checked by 741 · ${DD.meta.as_of}</div><a class="dz-btn dz-o dz-gap" href="#" onclick="dshGo('plan');return false">See the plan</a></div>
 </div>
 ${nNeeds ? `<div class="dz-need dz-gap2"><h2>Needs you (${nNeeds})</h2><span class="dz-mut">741 waits for these. Nothing changes on your live site without your OK.</span><ul>${needs.join('')}</ul></div>` : ''}
 <p class="dz-foot">${DD.source_note} Google can add the newest 2–3 days late. Sentences are drafted from the numbers and checked by 741.</p>`;
}
function dshDecisions(b) { const draft = DSH.admin && dshDecItems(b).some(i => i.status === 'draft'); return `${dshTabs(b, 'decisions')}<h1 class="dz-t">Your decisions</h1>${draft ? '<div class="dz-banner dz-amber"><span><b>Preview for 741.</b> These cards are drafts. The client sees them after you release them with the button "Entscheidungen" above. The card text of the decision module is still German.</span></div>' : ''}${apRenderClient(b, DSH.admin)}`; }
function dshSetup(b) { const st = dshSteps(b), nb = Object.assign({}, b, { steps: st }); return `${dshTabs(b, 'setup')}<h1 class="dz-t">Setup</h1><p class="dz-lead">${st.filter(s => s.status === 'erledigt').length} of ${st.length} steps done. Open steps also appear in "Needs you" on the Overview.</p><div class="dz-grid">${renderOnboarding(nb, false)}${renderGrants(b, false)}</div>`; }
function dshInner(b) {
  if (DSH.err) return `<div class="dz-card"><b>The dashboard data could not load.</b><div class="dz-mut">${esc(DSH.err)}</div></div>`;
  if (!DSH.d) return '<div class="dz-mut" style="padding:40px 0">Loading your dashboard…</div>';
  DD = DSH.d;
  if (dshGen()) return dshGInner(b);
  const v = DSH.view.split('/'); const sub = v[1] || 'enquiries';
  if (v[0] === 'results') return ({ enquiries: dshEnquiries, found: dshFound, reviews: dshReviews, ads: dshAds, backlinks: dshBacklinks }[sub] || dshEnquiries)();
  if (v[0] === 'plan') return dshPlan();
  if (v[0] === 'reports') return dshReports();
  if (v[0] === 'decisions') return dshDecisions(b);
  if (v[0] === 'setup') return dshSetup(b);
  return dshOverview(b);
}
function dshPage(b) {
  DSH.b = b; DSH.admin = typeof bundleIsAdmin !== 'undefined' && bundleIsAdmin; dshLoad(b);
  const chat = DSH.chat ? `<div class="dz-panel">${renderChat(b, false)}</div>` : '';
  return `<div class="dz">${dshInner(b)}${chat}<button class="dz-chat" onclick="dshToggleChat()">${(DD && dshGen()) ? (DSH.chat ? dshT().closeChat : dshT().chat) : (DSH.chat ? 'Close chat' : 'Chat with 741')}</button></div>`;
}
function dshRenderClient(b, target) {
  if (!DSH.init) { DSH.init = true; const m = location.hash.match(/^#d\/(.+)$/); if (m) DSH.view = m[1]; try { history.replaceState({ dsh: DSH.view }, '', '#d/' + DSH.view); } catch (e) {} }
  applyShellLang(b.client.lang || 'en'); $(target).innerHTML = dshPage(b); const h = document.getElementById('chat-history'); if (h) h.scrollTop = h.scrollHeight; }
function dshAdminButton(b) { return dshOn(b) ? `<button class="btn btn-small btn-yellow" onclick="adminSub='dash';dshPush(DSH.view,{dshAdmin:1});rerender()">Neues Dashboard (Vorschau)</button>` : ''; }
function dshAdminView(b) { return `<span class="backlink" onclick="history.back()">← Zur Kundenseite</span>${dshPage(b)}`; }
/* ---- Generic view for any client feed (German or English). Used when the feed has no Bali profile blocks (nhc). Bali keeps its own pages above. ---- */
const DSHL = {
  de: {
    tabs: { overview: 'Übersicht', results: 'Ergebnisse', plan: 'Plan', decisions: 'Entscheidungen', reports: 'Berichte', files: 'Dateien', setup: 'Einrichtung' },
    sub: { enquiries: 'Anfragen', found: 'Bei Google gefunden', reviews: 'Bewertungen' },
    q1: 'Bekomme ich mehr Anfragen?', q2: 'Werde ich besser gefunden?', q3: 'Was hat sich seit dem Start verändert?', q3w: 'Was macht 741?',
    week: (n, m) => `Woche ${n} von ${m}`, lastUpdate: 'Letztes Update von 741:',
    needsTitle: n => `Braucht dich (${n})`, needsSub: '741 wartet auf diese Punkte. Auf deiner Live-Seite ändert sich nichts ohne dein Ja.',
    needsChip: 'Braucht dich', decide: 'Entscheiden', draft: 'Entwurf: dem Kunden noch nicht freigegeben', openSetup: 'Einrichtung öffnen',
    setupOpen: n => `Einrichtung: ${n} Schritt${n === 1 ? '' : 'e'} noch offen.`,
    seeEnq: 'Anfragen ansehen', seeFound: 'Ergebnisse ansehen', seeResults: 'Vorher und nachher ansehen',
    notMeasured: 'Noch nicht gemessen', checked: 'Von 741 geprüft', emptyOv: 'Deine Zahlen werden gerade vorbereitet. Berichte, Entscheidungen und den Chat mit 741 findest du hier im Portal.',
    chat: 'Chat mit 741', closeChat: 'Chat schließen',
    ev: { phone_click: 'Klicks auf die Telefonnummer', email_click: 'Klicks auf die E-Mail-Adresse', whatsapp_click: 'Klicks auf WhatsApp', generate_lead: 'Formular-Anfragen' },
    g: { calls: 'Klicks auf „Anrufen“ im Google-Profil', web: 'Besuche deiner Website über Google', dir: 'Wegbeschreibungen über Google' },
    gNote: { calls: 'Gezählt wird der Klick auf den Knopf, nicht der Anruf.', web: 'Das sind Besuche, keine Anfragen.', dir: 'Google passt diese Zahl nachträglich an.' },
    enqG: (n, d, mo, prev, pl) => `<b>${n} Kontakt-Aktionen über ${pl ? 'deine Google-Profile' : 'dein Google-Profil'} im ${mo}</b>${d == null ? '.' : ', ' + (d === 0 ? 'so viele wie' : d > 0 ? d + ' mehr als' : Math.abs(d) + ' weniger als') + ' im ' + prev + '.'} Das sind Klicks auf Anrufen, Website und Wegbeschreibung.`,
    rvRating: 'Bewertung', rvCount: 'Bewertungen', rvUnans: 'Ohne Antwort', rvPer: 'Neue Bewertungen pro Monat', rvLead: (n, st) => `<b>${n} Google-Bewertungen, ${st} Sterne.</b>`,
    mapTitle: 'Auf der Google-Karte', mapWin: 'Läuft gut · ab 25 von 49', mapClose: 'Nah dran · 5 bis 24', mapMiss: 'Noch nicht sichtbar · unter 5', pts: 'von 49 Punkten',
    mapNote: 'Jede Zahl zeigt, an wie vielen von 49 Punkten rund um den Standort du bei Google Maps unter den ersten 3 stehst. Das Datum nennt den Stand der Messung je Suchbegriff.',
    mapBest: (kw, n) => `Auf der Google-Karte stehst du bei „${kw}“ an ${n} von 49 Punkten unter den ersten 3.`,
    evNote: { phone_click: 'Gezählt wird der Klick, nicht der Anruf.', email_click: 'Gezählt wird der Klick, nicht die Nachricht.', whatsapp_click: 'Gezählt wird der Klick, nicht das Gespräch.', generate_lead: 'Gesendete Anfragen über das Formular.' },
    enqLead: n => `<b>${n} Anfragen seit dem Start der Messung.</b> Davor wurde nicht gemessen, das ist kein Nullwert.`,
    enqNone: 'Die Messung der Anfragen läuft. Es gibt noch keinen Wert.',
    foundLead: (c, d, mo, prev) => `<b>${c} Klicks aus der Google-Suche im ${mo}</b>${d == null ? '.' : ', ' + (d === 0 ? 'so viele wie' : d > 0 ? d + ' mehr als' : Math.abs(d) + ' weniger als') + ' im ' + prev + '.'}`,
    posText: (p, pj, mj) => p == null ? '' : `Durchschnittsposition ${dshN(p, 1)} (${p <= 10 ? 'Seite 1' : p <= 20 ? 'Seite 2' : 'weiter hinten'})${pj == null ? '.' : ', im ' + mj + ' waren es ' + dshN(pj, 1) + '.'}`,
    clicksMonth: 'Klicks aus der Google-Suche pro Monat', fullMonthNote: 'Nur volle Monate. Google trägt die letzten Tage verspätet nach.',
    beforeAfter: 'Vorher und nachher', before: 'Vorher', after: 'Nachher', latest: 'Zuletzt', better: 'besser', worse: 'schlechter', same: 'gleich',
    queries: 'Dein wichtigster Suchbegriff', listings: 'Verzeichniseinträge online', of: 'von',
    reviewsTitle: 'Google-Bewertungen', reviewsLead: (n, s) => `<b>${n} Bewertungen, ${s} Sterne.</b>`,
    reports: 'Berichte', reportsLead: 'Jeder Bericht mit Datum. Ältere Fassungen verweisen auf die aktuelle Seite.', repReport: 'Bericht', repPeriod: 'Zeitraum', repState: 'Stand', open: 'Öffnen',
    current: 'Aktuell', replaced: 'Ersetzt', foot: 'Sätze werden aus den Zahlen vorbereitet und von 741 geprüft.', loading: 'Dein Dashboard lädt …',
    resultsTitle: 'Ergebnisse', setupTitle: 'Einrichtung', decisionsTitle: 'Deine Entscheidungen', back: '← Zur Kundenseite',
    status: { red: 'Blockiert', amber: 'Braucht dich', green: 'Im Plan', grey: 'Noch keine Daten' },
    locale: 'de-DE'
  },
  en: {
    tabs: { overview: 'Overview', results: 'Results', plan: 'Plan', decisions: 'Decisions', reports: 'Reports', files: 'Files', setup: 'Setup' },
    sub: { enquiries: 'Enquiries', found: 'Found on Google', reviews: 'Reviews' },
    q1: 'Do I get more enquiries?', q2: 'Am I easier to find?', q3: 'What changed since the start?', q3w: 'What is 741 doing?',
    week: (n, m) => `Week ${n} of ${m}`, lastUpdate: 'Last update from 741:',
    needsTitle: n => `Needs you (${n})`, needsSub: '741 waits for these. Nothing changes on your live site without your OK.',
    needsChip: 'Needs you', decide: 'Decide', draft: 'Draft: not released to the client', openSetup: 'Open setup',
    setupOpen: n => `Setup: ${n} step${n === 1 ? '' : 's'} still open.`,
    seeEnq: 'See enquiries', seeFound: 'See results', seeResults: 'See before and after',
    notMeasured: 'Not measured yet', checked: 'Checked by 741', emptyOv: 'Your numbers are being prepared. You find reports, decisions and the chat with 741 here in the portal.',
    chat: 'Chat with 741', closeChat: 'Close chat',
    ev: { phone_click: 'Taps on the phone number', email_click: 'Taps on the email address', whatsapp_click: 'Taps on WhatsApp', generate_lead: 'Form enquiries' },
    g: { calls: 'Taps on “Call” in the Google profile', web: 'Visits to your website from Google', dir: 'Asked for directions on Google' },
    gNote: { calls: 'We count the tap on the button, not the call.', web: 'These are visits, not enquiries.', dir: 'Google adjusts this count afterwards.' },
    enqG: (n, d, mo, prev, pl) => `<b>${n} contact actions from your Google ${pl ? 'profiles' : 'profile'} in ${mo}</b>${d == null ? '.' : ', ' + (d === 0 ? 'the same as' : d > 0 ? d + ' more than' : Math.abs(d) + ' fewer than') + ' in ' + prev + '.'} These are taps on call, website and directions.`,
    rvRating: 'Rating', rvCount: 'Reviews', rvUnans: 'Without a reply', rvPer: 'New reviews per month', rvLead: (n, st) => `<b>${n} Google reviews, ${st} stars.</b>`,
    mapTitle: 'On the Google map', mapWin: 'Going well · 25 or more of 49', mapClose: 'Close · 5 to 24', mapMiss: 'Not visible yet · under 5', pts: 'of 49 spots',
    mapNote: 'Each number shows on how many of 49 spots around the location you are in the top 3 on Google Maps. The date is the scan date for each search term.',
    mapBest: (kw, n) => `On the Google map you are in the top 3 for "${kw}" on ${n} of 49 spots.`,
    evNote: { phone_click: 'We count the tap, not the call.', email_click: 'We count the tap, not the message.', whatsapp_click: 'We count the tap, not the chat.', generate_lead: 'Enquiries sent through the form.' },
    enqLead: n => `<b>${n} enquiries since the measurement started.</b> Before that nothing was measured. That is not zero.`,
    enqNone: 'Measuring enquiries has started. There is no value yet.',
    foundLead: (c, d, mo, prev) => `<b>${c} clicks from Google Search in ${mo}</b>${d == null ? '.' : ', ' + (d === 0 ? 'the same as' : d > 0 ? d + ' more than' : Math.abs(d) + ' fewer than') + ' in ' + prev + '.'}`,
    posText: (p, pj, mj) => p == null ? '' : `Average position ${dshN(p, 1)} (${p <= 10 ? 'page 1' : p <= 20 ? 'page 2' : 'further back'})${pj == null ? '.' : ', in ' + mj + ' it was ' + dshN(pj, 1) + '.'}`,
    clicksMonth: 'Clicks from Google Search per month', fullMonthNote: 'Full months only. Google adds the latest days late.',
    beforeAfter: 'Before and after', before: 'Before', after: 'After', latest: 'Latest', better: 'better', worse: 'worse', same: 'same',
    queries: 'Your most important search term', listings: 'Directory listings online', of: 'of',
    reviewsTitle: 'Google reviews', reviewsLead: (n, s) => `<b>${n} reviews, ${s} stars.</b>`,
    reports: 'Reports', reportsLead: 'Every report with its date. Older versions point to the current page.', repReport: 'Report', repPeriod: 'Period', repState: 'State', open: 'Open',
    current: 'Current', replaced: 'Replaced', foot: 'Sentences are drafted from the numbers and checked by 741.', loading: 'Loading your dashboard…',
    resultsTitle: 'Results', setupTitle: 'Setup', decisionsTitle: 'Your decisions', back: '← Back to the client page',
    status: { red: 'Blocked', amber: 'Needs you', green: 'On track', grey: 'No data yet' },
    locale: 'en-US'
  }
};
const dshLang = () => (DD && DD.meta && DD.meta.lang === 'de') ? 'de' : 'en';
const dshT = () => DSHL[dshLang()];
const dshGen = () => !(DD && DD.nhc);
function dshDate(iso) { if (!iso) return ''; const d = new Date(String(iso).slice(0, 10) + 'T12:00:00'); return isNaN(d) ? String(iso) : d.toLocaleDateString(dshT().locale, { day: '2-digit', month: '2-digit', year: 'numeric' }); }
function dshN(n, frac) { return n == null ? '—' : new Intl.NumberFormat(dshT().locale, frac ? { minimumFractionDigits: frac, maximumFractionDigits: frac } : {}).format(n); }
function dshGSt(c, w) { return `<span class="dz-st dz-${c}">${DSHS[c][2]}${w || dshT().status[c]}</span>`; }
function dshGProfiles() { return (DD.profiles && DD.profiles.length) ? DD.profiles : []; }
function dshGKey() { const P = dshGProfiles(); if (P.length > 1 && P.some(x => x[0] === DSH.profile)) return DSH.profile; return P.length ? P[0][0] : 'main'; }
function dshGMain() { const b = DD[dshGKey()]; return b && b.calls ? b : null; }
function dshGRevMain() { return DD.rev && DD.rev[dshGKey()] ? DD.rev[dshGKey()] : null; }
function dshGAllMain() {   // every profile that has Google profile numbers: [{key, label, b}]
  const P = dshGProfiles(), keys = P.length ? P : [['main', '']];
  return keys.filter(k => DD[k[0]] && DD[k[0]].calls).map(k => ({ key: k[0], label: k[1], b: DD[k[0]] }));
}
function dshGSumTotals(blocks) { return blocks.length ? blocks[0].calls.map((_, i) => blocks.some(b => b.calls[i] == null || b.web[i] == null || b.dir[i] == null) ? null : blocks.reduce((a, b) => a + b.calls[i] + b.web[i] + b.dir[i], 0)) : null; }
function dshGMap() { return DD.map && DD.map.length ? DD.map : null; }
function dshGTotals() { const m = dshGMain(); return m ? m.calls.map((_, i) => (m.calls[i] == null || m.web[i] == null || m.dir[i] == null) ? null : m.calls[i] + m.web[i] + m.dir[i]) : null; }
function dshGHasResults() { return !!(DD.ga4_events || dshGAllMain().length || dshGMap() || dshGRevMain() || (DD.gsc && DD.gsc.sep != null) || DD.ergebnisse || DD.citations); }
function dshGHasPlan() { return !!((DD.tracks && DD.tracks.length) || (DD.tree && DD.tree.length)); }
function dshGMonthNames() { const g = DD.meta && DD.meta.derived && DD.meta.derived.gsc; return (g && g.months) || ['', '', '']; }
function dshGTabs(b, cur) {
  const T = dshT(), nDec = dshDecOpen(b).length, nSet = dshOpenSteps(b), items = [['overview', T.tabs.overview]];
  if (dshGHasResults()) items.push(['results', T.tabs.results]);
  if (dshGHasPlan()) items.push(['plan', T.tabs.plan]);
  if (dshDecItems(b).length) items.push(['decisions', T.tabs.decisions, nDec]);
  if (DD.reports && DD.reports.length) items.push(['reports', T.tabs.reports]);
  items.push(['files', T.tabs.files]);
  if (nSet) items.push(['setup', T.tabs.setup, nSet]);
  return `<nav class="dz-tabs">${items.map(t => `<a class="dz-tab ${cur === t[0] ? 'dz-on' : ''}" href="#" onclick="dshGo('${t[0]}');return false">${t[1]}${t[2] ? `<span class="dz-n">${t[2]}</span>` : ''}</a>`).join('')}</nav>`;
}
function dshGSub(cur) {
  const T = dshT(), items = [];
  if (DD.ga4_events || dshGAllMain().length) items.push(['enquiries', T.sub.enquiries]);
  if ((DD.gsc && DD.gsc.sep != null) || DD.ergebnisse || DD.citations || dshGMap()) items.push(['found', T.sub.found]);
  if (dshGRevMain() || (DD.rev && DD.rev[dshGKey()]) || (DD.ergebnisse && DD.ergebnisse.reviews)) items.push(['reviews', T.sub.reviews]);
  const P = dshGProfiles(), sw = (P.length > 1 && (cur === 'enquiries' || cur === 'reviews')) ? `<span class="dz-sw" role="group">${P.map(x => `<button class="${dshGKey() === x[0] ? 'dz-on' : ''}" onclick="dshSetP('${x[0]}')">${esc(x[1])}</button>`).join('')}</span>` : '';
  return `<div class="dz-sub">${items.map(t => `<a class="dz-pill ${cur === t[0] ? 'dz-on' : ''}" href="#" onclick="dshGo('results/${t[0]}');return false">${t[1]}</a>`).join('')}${sw}</div>`;
}
function dshGEvTotal() {
  if (!DD.ga4_events) return null;
  const i = DD.meta.partial != null ? DD.meta.partial : DD.months.length - 1; let n = 0, any = false;
  Object.keys(DD.ga4_events).forEach(k => { const v = DD.ga4_events[k][i]; if (v != null) { any = true; n += v; } });
  return any ? n : null;
}
function dshGDelta(m) {   // neutral wording, no status colours in numbers
  const T = dshT(); if (m.before == null || m.after == null) return '';
  const d = m.after - m.before; if (d === 0) return T.same;
  const good = (m.better === 'lower') ? d < 0 : d > 0;
  return `${good ? '▲' : '▼'} ${good ? T.better : T.worse}`;
}
function dshGOverview(b) {
  const T = dshT(), nDec = dshDecOpen(b).length, nSet = dshOpenSteps(b), bn = DD.banner;
  const needs = dshDecOpen(b).map(i => `<li>${dshGSt('amber', T.needsChip)}<span class="dz-tx"><b>${esc(i.title)}</b>${i.status === 'draft' ? ` <span class="dz-badge">${T.draft}</span>` : ''}</span><a class="dz-btn" href="#" onclick="dshGo('decisions');return false">${T.decide}</a></li>`);
  (DD.needs || []).filter(n => n.go !== 'decisions').forEach(n => needs.push(`<li>${dshGSt('amber', T.needsChip)}<span class="dz-tx">${n.t}</span><a class="dz-btn dz-o" href="#" onclick="dshGo('${n.go}');return false">${n.btn}</a></li>`));
  if (nSet) needs.push(`<li>${dshGSt('amber', T.needsChip)}<span class="dz-tx"><b>${T.setupOpen(nSet)}</b></span><a class="dz-btn dz-o" href="#" onclick="dshGo('setup');return false">${T.openSetup}</a></li>`);
  const cards = [];
  if (dshGAllMain().length) {
    const all = dshGAllMain(), tot = dshGSumTotals(all.map(x => x.b)), f = DD.meta.full != null ? DD.meta.full : tot.length - 2, n = tot[f], d = (tot[f - 1] == null || n == null) ? null : n - tot[f - 1];
    const per = all.length > 1 ? all.map(x => { const t = x.b.calls[f] + x.b.web[f] + x.b.dir[f]; return `<p class="dz-mut"><b>${esc(x.label)}:</b> ${dshN(t)}</p>`; }).join('') : '';
    cards.push(`<div class="dz-card"><div class="dz-q">${T.q1}</div><div class="dz-big">${n == null ? '—' : dshN(n)}</div><p class="dz-sentence">${T.enqG(dshN(n), d, DD.months[f], DD.months[f - 1], all.length > 1)}</p>${per}${dshBars(tot, DD.months, { partial: DD.meta.partial, full: f, id: 'go1', aria: T.q1 })}<div class="dz-chk">${T.checked} · ${dshDate(DD.meta.as_of)}</div><a class="dz-btn dz-o dz-gap" href="#" onclick="dshGo('results/enquiries');return false">${T.seeEnq}</a></div>`);
  } else if (DD.ga4_events) {
    const n = dshGEvTotal(); const src = DD.meta.sources && DD.meta.sources.whatsapp;
    cards.push(`<div class="dz-card"><div class="dz-q">${T.q1}</div><div class="dz-big">${n == null ? '—' : dshN(n)}</div><p class="dz-sentence">${n == null ? T.enqNone : T.enqLead(dshN(n))}</p>${src && src.note ? `<p class="dz-mut">${esc(src.note)}</p>` : ''}<div class="dz-chk">${T.checked} · ${dshDate(DD.meta.as_of)}</div><a class="dz-btn dz-o dz-gap" href="#" onclick="dshGo('results/enquiries');return false">${T.seeEnq}</a></div>`);
  }
  if (DD.gsc && DD.gsc.sep != null) {
    const m = dshGMonthNames(), g = DD.gsc, pos = g.pos, c = g.sep;
    cards.push(`<div class="dz-card"><div class="dz-q">${T.q2}</div><div class="dz-big">${dshN(c)}</div><p class="dz-sentence">${T.foundLead(dshN(c), g.aug == null ? null : c - g.aug, m[2] || '', m[1] || '')}</p><p class="dz-mut">${T.posText(pos, g.posJul, m[0] || '')}</p>${dshGMap() ? (() => { const b = DD.map.slice().sort((x, y) => y[1] - x[1])[0]; return `<p class="dz-mut">${T.mapBest(esc(b[0]), b[1])}</p>`; })() : ''}${DD.citations ? `<p class="dz-mut">${T.listings}: <b>${DD.citations.live} ${T.of} ${DD.citations.total}</b></p>` : ''}<div class="dz-chk">${T.checked} · ${dshDate(DD.meta.as_of)}</div><a class="dz-btn dz-o dz-gap" href="#" onclick="dshGo('results/found');return false">${T.seeFound}</a></div>`);
  }
  if (!(DD.gsc && DD.gsc.sep != null) && dshGMap()) {
    const best = DD.map.slice().sort((a, b) => b[1] - a[1])[0];
    cards.push(`<div class="dz-card"><div class="dz-q">${T.q2}</div><div class="dz-big">${best[1]}</div><p class="dz-sentence">${T.mapBest(esc(best[0]), best[1])}</p>${DD.citations ? `<p class="dz-mut">${T.listings}: <b>${DD.citations.live} ${T.of} ${DD.citations.total}</b></p>` : ''}<div class="dz-chk">${T.checked} · ${dshDate(DD.meta.as_of)}</div><a class="dz-btn dz-o dz-gap" href="#" onclick="dshGo('results/found');return false">${T.seeFound}</a></div>`);
  }
  if (DD.ergebnisse && DD.ergebnisse.metrics) {
    const mm = DD.ergebnisse.metrics.filter(x => x.key === 'clicks' || x.key === 'position');
    cards.push(`<div class="dz-card"><div class="dz-q">${T.q3}</div>${mm.map(x => `<p class="dz-sentence"><b>${esc(x.label)}</b><br>${dshN(x.before, x.key === 'position' ? 1 : 0)} → <b>${dshN(x.after, x.key === 'position' ? 1 : 0)}</b> <span class="dz-dl">${dshGDelta(x)}</span></p>`).join('')}<p class="dz-mut dz-s">${esc(DD.ergebnisse.windows.before.label)} → ${esc(DD.ergebnisse.windows.after.label)}</p><div class="dz-chk">${T.checked} · ${dshDate(DD.ergebnisse.read)}</div><a class="dz-btn dz-o dz-gap" href="#" onclick="dshGo('results/found');return false">${T.seeResults}</a></div>`);
  } else if (DD.work && (DD.work.this_week || DD.work.done)) {
    cards.push(`<div class="dz-card"><div class="dz-q">${T.q3w}</div>${DD.work.this_week ? `<p class="dz-sentence">${DD.work.this_week}</p>` : ''}${DD.work.done ? `<p class="dz-mut">${DD.work.done}</p>` : ''}<div class="dz-chk">${T.checked} · ${dshDate(DD.meta.as_of)}</div></div>`);
  }
  const guide = DD.guide && DD.guide.overview ? dshMg(DD.guide.overview.pose, DD.guide.overview.text) : '';
  return `${dshGTabs(b, 'overview')}
 <div class="dz-strip"><b>${esc(DD.meta.client)}</b>${DD.meta.week ? `<span class="dz-mut">${T.week(DD.meta.week, DD.meta.weeks)}</span>${dshSeg(DD.meta.week, DD.meta.weeks)}` : ''}${DD.meta.last_update ? `<span class="dz-mut">${T.lastUpdate} ${esc(DD.meta.last_update)}</span>` : ''}</div>
 ${bn ? `<div class="dz-banner dz-${bn.color}">${dshGSt(bn.color, bn.label)}<span>${bn.html}</span></div>` : ''}${guide}
 ${cards.length ? `<div class="${cards.length === 2 ? 'dz-grid2' : 'dz-grid3'}">${cards.join('')}</div>` : `<div class="dz-gapcard"><p class="dz-mut">${T.emptyOv}</p></div>`}
 ${needs.length ? `<div class="dz-need dz-gap2"><h2>${T.needsTitle(needs.length)}</h2><span class="dz-mut">${T.needsSub}</span><ul>${needs.join('')}</ul></div>` : ''}
 <p class="dz-foot">${esc(DD.source_note || '')} ${T.foot}</p>`;
}
function dshGEnquiries() {
  const T = dshT(), ev = DD.ga4_events || {}, order = ['phone_click', 'email_click', 'whatsapp_click', 'generate_lead'].filter(k => ev[k]);
  const n = dshGEvTotal();
  const gm = dshGMain(), gt = gm ? ['calls', 'web', 'dir'].map((k, i) => `<div class="dz-card dz-tile"><div class="dz-q">${T.g[k]}</div><div class="dz-num">${gm[k][DD.meta.full] == null ? '—' : dshN(gm[k][DD.meta.full])}<span class="dz-dl">${DD.months[DD.meta.full]}</span></div><div class="dz-d">${T.gNote[k]}</div>${dshBars(gm[k], DD.months, { partial: DD.meta.partial, full: DD.meta.full, id: 'gg' + i, aria: T.g[k] })}</div>`) : [];
  const tiles = gt.concat(order.map((k, i) => {
    const v = ev[k], p = DD.meta.partial, last = p != null ? v[p] : v[v.length - 1];
    return `<div class="dz-card dz-tile"><div class="dz-q">${T.ev[k]}</div><div class="dz-num">${last == null ? '—' : dshN(last)}</div><div class="dz-d">${T.evNote[k]}</div>${dshBars(v, DD.months, { partial: p, full: DD.meta.full, id: 'g' + i, aria: T.ev[k] })}</div>`;
  }));
  const src = DD.meta.sources && DD.meta.sources.whatsapp;
  return `${dshGTabs(DSH.b, 'results')}${dshGSub('enquiries')}<h1 class="dz-t">${T.q1}</h1>
 <p class="dz-lead">${gm ? (() => { const tot = dshGTotals(), f = DD.meta.full, v = tot[f]; return T.enqG(dshN(v), tot[f - 1] == null || v == null ? null : v - tot[f - 1], DD.months[f], DD.months[f - 1], false); })() : (n == null ? T.enqNone : T.enqLead(dshN(n)))}</p>
 <div class="dz-grid2">${tiles.join('')}</div>
 <p class="dz-foot">${src && src.note ? esc(src.note) + ' ' : ''}${T.notMeasured}: ${dshLang() === 'de' ? 'gestrichelte Felder. Schraffierter Balken: laufender Monat.' : 'dashed slots. Hatched bar: month in progress.'}</p>`;
}
function dshGFound() {
  const T = dshT(), g = DD.gsc, m = dshGMonthNames(), E = DD.ergebnisse;
  let html = `${dshGTabs(DSH.b, 'results')}${dshGSub('found')}<h1 class="dz-t">${T.q2}</h1>`;
  if (!(g && g.sep != null) && dshGMap()) { const b = DD.map.slice().sort((x, y) => y[1] - x[1])[0]; html += `<p class="dz-lead"><b>${T.mapBest(esc(b[0]), b[1])}</b></p>`; }
  if (g && g.sep != null) {
    html += `<p class="dz-lead">${T.foundLead(dshN(g.sep), g.aug == null ? null : g.sep - g.aug, m[2] || '', m[1] || '')} ${T.posText(g.pos, g.posJul, m[0] || '')}</p>
 <div class="dz-card"><div class="dz-q">${T.clicksMonth}</div>${dshBars([g.jul, g.aug, g.sep], m, { full: 2, id: 'gf', w: 420, h: 110, aria: T.clicksMonth })}<p class="dz-mut dz-s">${T.fullMonthNote}</p></div>`;
  }
  if (E && E.metrics) {
    const rows = E.metrics.map(x => { const f = x.key === 'position' || x.key === 'ctr' ? 1 : 0; return `<tr><td><b>${esc(x.label)}</b></td><td>${dshN(x.before, f)}${x.unit ? ' ' + x.unit : ''}</td><td><b>${dshN(x.after, f)}${x.unit ? ' ' + x.unit : ''}</b></td><td>${dshN(x.latest, f)}${x.unit ? ' ' + x.unit : ''}</td><td>${dshGDelta(x)}</td></tr>`; }).join('');
    html += `<div class="dz-card dz-gap2"><h2>${esc(E.title)}</h2><p class="dz-mut">${T.before}: ${esc(E.windows.before.label)} · ${T.after}: ${esc(E.windows.after.label)} · ${T.latest}: ${esc(E.windows.latest.label)}</p>
 <table class="dz-t"><tr><th></th><th>${T.before}</th><th>${T.after}</th><th>${T.latest}</th><th></th></tr>${rows}</table>
 ${(E.queries || []).map(q => `<p class="dz-sentence"><b>${T.queries}: „${esc(q.query)}“</b><br>${dshN(q.before.position, 1)} → <b>${dshN(q.after.position, 1)}</b> (${T.latest}: ${dshN(q.latest.position, 1)}) · ${dshN(q.before.clicks)} → <b>${dshN(q.after.clicks)}</b> ${dshLang() === 'de' ? 'Klicks' : 'clicks'}</p>`).join('')}
 ${E.note ? `<p class="dz-mut dz-s">${esc(E.note)}</p>` : ''}<p class="dz-chk">${T.checked} · ${dshDate(E.read)}</p></div>`;
  }
  if (dshGMap()) {
    const rows = DD.map, win = rows.filter(r => r[1] >= 25), cl = rows.filter(r => r[1] >= 5 && r[1] < 25), mi = rows.filter(r => r[1] < 5);
    const kw = r => `<div class="dz-kw"><span>${esc(r[0])} <span class="dz-mut dz-s">(${esc(r[2] || '')})</span></span><b>${r[1]} ${dshT().pts.split(' ')[0] === 'von' ? 'von 49' : 'of 49'}</b></div>`;
    html += `<h2 class="dz-gap2">${T.mapTitle}</h2><div class="dz-cols3 dz-gap"><div class="dz-card"><div class="dz-st dz-green">${DSHS.green[2]}${T.mapWin}</div>${win.map(kw).join('')}</div><div class="dz-card"><div class="dz-st dz-amber">${DSHS.amber[2]}${T.mapClose}</div>${cl.map(kw).join('')}</div><div class="dz-card"><div class="dz-st dz-grey">${DSHS.grey[2]}${T.mapMiss}</div>${mi.map(kw).join('')}</div></div><p class="dz-mut dz-s dz-gap">${T.mapNote}</p>`;
  }
  if (DD.citations) {
    const c = DD.citations, pct = c.total ? Math.round(c.live / c.total * 100) : 0;
    html += `<div class="dz-card dz-gap2"><h2>${T.listings}</h2><div class="dz-row"><span class="dz-b"><i style="width:${pct}%"></i></span><span class="dz-c" style="flex-basis:90px">${c.live} ${T.of} ${c.total}</span></div></div>`;
  }
  return html;
}
function dshGReviews() {
  const T = dshT(), r = DD.ergebnisse && DD.ergebnisse.reviews, rm = dshGRevMain();
  if (rm) {
    const stats = `<div class="dz-grid3"><div class="dz-card"><div class="dz-q">${T.rvRating}</div><div class="dz-big">${dshN(rm.star, 1)} ★</div></div><div class="dz-card"><div class="dz-q">${T.rvCount}</div><div class="dz-big">${dshN(rm.n)}</div></div><div class="dz-card"><div class="dz-q">${T.rvUnans}</div><div class="dz-big">${rm.unans == null ? '—' : dshN(rm.unans)}</div></div></div>`;
    const per = rm.months && rm.per ? `<div class="dz-card dz-gap2"><h2>${T.rvPer}</h2>${dshBars(rm.per, rm.months, { id: 'rv', w: 420, h: 110, aria: T.rvPer })}</div>` : '';
    const ba = r ? `<div class="dz-card dz-gap2"><h2>${T.before} / ${T.after}</h2><table class="dz-t"><tr><th></th><th>${T.rvCount}</th><th>${dshLang() === 'de' ? 'Sterne' : 'Stars'}</th></tr>${[[T.before, r.before], [T.after, r.after]].map(x => x[1] ? `<tr><td><b>${x[0]}</b> <span class="dz-mut dz-s">${dshDate(x[1].date)}</span></td><td>${dshN(x[1].n)}</td><td>${dshN(x[1].star, 1)} ★</td></tr>` : '').join('')}</table></div>` : '';
    return `${dshGTabs(DSH.b, 'results')}${dshGSub('reviews')}<h1 class="dz-t">${T.sub.reviews}</h1><p class="dz-lead">${T.rvLead(dshN(rm.n), dshN(rm.star, 1))}</p>${stats}${per}${ba}<p class="dz-foot">${T.checked} · ${dshDate(DD.meta.as_of)}</p>`;
  }
  if (!r) return `${dshGTabs(DSH.b, 'results')}${dshGSub('reviews')}<h1 class="dz-t">${T.reviewsTitle}</h1><div class="dz-gapcard"><p class="dz-mut">${T.notMeasured}</p></div>`;
  const row = (l, x) => x ? `<tr><td><b>${l}</b> <span class="dz-mut dz-s">${dshDate(x.date)}</span></td><td>${dshN(x.n)}</td><td>${dshN(x.star, 1)} ★</td></tr>` : '';
  return `${dshGTabs(DSH.b, 'results')}${dshGSub('reviews')}<h1 class="dz-t">${T.reviewsTitle}</h1>
 <p class="dz-lead">${T.reviewsLead(dshN(r.after.n), dshN(r.after.star, 1))}</p>
 <div class="dz-card"><table class="dz-t"><tr><th></th><th>${dshLang() === 'de' ? 'Bewertungen' : 'Reviews'}</th><th>${dshLang() === 'de' ? 'Sterne' : 'Stars'}</th></tr>${row(T.before, r.before)}${row(T.after, r.after)}</table>${r.note ? `<p class="dz-mut dz-s">${esc(r.note)}</p>` : ''}<p class="dz-chk">${esc(r.source || '')}</p></div>`;
}
function dshGReports() {
  const T = dshT(), isRep = s => /Replaced|Ersetzt/i.test(s || '');
  return `${dshGTabs(DSH.b, 'reports')}<h1 class="dz-t">${T.reports}</h1><p class="dz-lead">${T.reportsLead}</p>
 <div class="dz-card"><table class="dz-t"><tr><th>${T.repReport}</th><th>${T.repPeriod}</th><th>${T.repState}</th><th></th></tr>${(DD.reports || []).map(r => `<tr><td><b>${esc(r[0])}</b></td><td>${esc(r[1])}</td><td>${isRep(r[3]) ? dshGSt('grey', T.replaced) : dshGSt('green', T.current)}</td><td>${r[4] ? `<a class="dz-btn dz-o" href="#" onclick="dshOpenReport('${r[4]}','${esc(r[0]).replace(/'/g, '')}');return false">${T.open}</a>` : ''}</td></tr>`).join('')}</table></div>`;
}
function dshGDecisions(b) { const T = dshT(); const draft = DSH.admin && dshDecItems(b).some(i => i.status === 'draft'); return `${dshGTabs(b, 'decisions')}<h1 class="dz-t">${T.decisionsTitle}</h1>${draft ? `<div class="dz-banner dz-amber"><span><b>Vorschau für 741.</b> Diese Karten sind Entwürfe. Der Kunde sieht sie erst nach der Freigabe im Chat.</span></div>` : ''}${apRenderClient(b, DSH.admin)}`; }
function dshGFiles(b) { const T = dshT(); return `${dshGTabs(b, 'files')}<h1 class="dz-t">${T.tabs.files}</h1><div class="dz-grid" style="max-width:840px">${renderMaterials(b, false)}</div>`; }
function dshGSetup(b) { const T = dshT(), st = dshSteps(b), nb = Object.assign({}, b, { steps: st }); return `${dshGTabs(b, 'setup')}<h1 class="dz-t">${T.setupTitle}</h1><div class="dz-grid">${renderOnboarding(nb, false)}${renderGrants(b, false)}</div>`; }
function dshGInner(b) {
  const v = DSH.view.split('/'), sub = v[1] || 'enquiries';
  if (v[0] === 'results') return ({ enquiries: dshGEnquiries, found: dshGFound, reviews: dshGReviews }[sub] || (DD.ga4_events ? dshGEnquiries : dshGFound))();
  if (v[0] === 'reports') return dshGReports();
  if (v[0] === 'decisions') return dshGDecisions(b);
  if (v[0] === 'setup') return dshGSetup(b);
  if (v[0] === 'files') return dshGFiles(b);
  if (v[0] === 'plan' && dshGHasPlan()) return dshPlan();
  return dshGOverview(b);
}

/* ---------- Ende Dashboard (neu) ---------- */

DSH.d={"months":["Apr","Mai","Jun","Jul","Aug","Sep","1.–19. Okt"],"main":{"calls":[1,1,3,1,1,1,1],"web":[7,4,3,1,4,3,6],"dir":[37,38,43,51,43,53,10]},"wa":[],"gsc":{"sep":159,"aug":110,"jul":111,"pos":26.4,"posJul":31.7},"rev":{"main":{"n":9,"star":5,"unans":3,"leader":null,"months":["Jan","Feb","Mär","Apr","Mai","Jun","Jul","Aug","Sep"],"per":[0,0,0,0,0,0,0,0,6]}},"map":[["ernährungsberatung charlottenburg",0,"1. Okt."],["heilpraktiker charlottenburg",0,"1. Okt."]],"ai":null,"ads":null,"funnel":[],"tracks":[],"tree":[],"decisions":[],"reports":[["🧭 Dein SEO-Fahrplan","Stand 13.10.2026","daniela-dumann-fahrplan-2026-10.html","Aktuell","https://clients.741.studio/r/f92ed4298f5c/daniela-dumann-fahrplan-2026-10.html?v=20261014a"],["🤖 KI-Sichtbarkeit & Wettbewerber-Analyse","Erste Messung · Stand 09.10.2026","daniela-dumann-ki-sichtbarkeit-2026-10.html","Aktuell","https://clients.741.studio/r/f92ed4298f5c/daniela-dumann-ki-sichtbarkeit-2026-10.html"],["📈 Sichtbarkeits-Report — GBP, Search & GA4","Jul–Sep 2026","daniela-dumann-sichtbarkeit-2026-09.html","Aktuell","https://clients.741.studio/r/f92ed4298f5c/daniela-dumann-sichtbarkeit-2026-09.html?v=20261001a"],["📍 GBP-Empfehlung & Freigabe","Bitte durchgehen & freigeben","daniela-dumann-gbp-2026-09.html","Aktuell","https://clients.741.studio/r/f92ed4298f5c/daniela-dumann-gbp-2026-09.html?v=20260907d"],["🗺️ Website-Struktur & Startseiten-Text","Seitenbaum · 04.09.2026","daniela-dumann-seitenbaum-2026-09.html","Aktuell","https://clients.741.studio/r/f92ed4298f5c/daniela-dumann-seitenbaum-2026-09.html?v=20260916c"],["📋 Woche 1 — Bestandsaufnahme & Fahrplan","Woche 1 · 31.08.2026","daniela-dumann-woche1-2026-08.html","Aktuell","https://clients.741.studio/r/3f44fe649fe4/daniela-dumann-woche1-2026-08.html"],["📊 Deine Google-Sichtbarkeits-Analyse (Start)","Ausgangslage · vor Programmstart","daniela-dumann","Aktuell","https://741.studio/review/daniela-dumann/"]],"meta":{"client_id":"d01f4236-8674-45fe-a347-0751fa7b24de","client":"Naturheilpraxis Daniela Dumann","lang":"de","as_of":"2026-10-19","week":6,"weeks":13,"full":5,"partial":6,"last_update":"14. Okt.: Dein SEO-Fahrplan","refresh":{"generated_at":"2026-10-19T01:53:26.135Z","job":"portal/feed/build.mjs","as_of":"2026-10-19","status":"ok","failed":[],"gaps":[],"filling_from":"2026-10-17","carried":["banner","guide","needs","work","decisions_note","decisions","tracks","tree","funnel","profiles","meta.client_id","meta.client","meta.lang"]},"filling":{"from":"2026-10-17","to":"2026-10-19","month_index":[6],"note":"Google trägt die neuesten Tage verspätet nach. Die Zahlen dieser Tage können noch steigen."},"sources":{"profile_actions":{"source":"Google-Profil-Daten (Anrufe, Website-Besuche, Routenanfragen)","read":"2026-10-19","note":"Die neuesten 3 Tage (ab 2026-10-17) können noch steigen."},"search_console":{"source":"Google Search Console (Klicks und Durchschnittsposition in der Google-Suche)","read":"2026-10-19","note":"Endgültige Daten für volle Monate. Durchschnittsposition des letzten vollen Monats."},"reviews":{"source":"Google-Bewertungen des Profils (aktuelle Liste)","read":"2026-10-19","note":"Neue Bewertungen pro Monat nach dem Datum, das Google zeigt (Ortszeit)."},"map":{"source":"Google-Maps-Prüfungen (49 Punkte rund um die Praxis, Top-3-Abdeckung)","read":"2026-10-19","note":"Neueste Prüfung je Suchbegriff. Die Prüfdaten unterscheiden sich. Die Einstellungen können je Suchbegriff abweichen."},"citations":{"source":"Verzeichniseinträge im 741-Portal (Status je Verzeichnis)","read":"2026-10-19","note":""},"reports":{"source":"Berichte im 741-Portal","read":"2026-10-19","note":""},"last_update":{"source":"Berichte im 741-Portal","read":"2026-10-19","note":"14. Okt. 2026"}},"derived":{"running_month_settled":{"from":"2026-10-01","to":"2026-10-16","main":{"calls":1,"web":6,"dir":10}},"gsc":{"months":["Jul","Aug","Sep"],"impressions":[3167,2602,1976],"position":[31.7,36.1,26.4],"running_month":{"from":"2026-10-01","to":"2026-10-17","clicks":85,"impressions":1100,"position":27.3}},"reviews":{"main":{"replied":6,"newest_without_reply":1,"latest_without_reply":"2026-10-04","newest_review":"2026-10-04"}},"map_detail":{"main":[{"name":"ernährungsberatung charlottenburg","keyword":"ernährungsberatung charlottenburg","top3":0,"of":49,"date":"2026-10-01","found_in":1,"arp":14,"atrp":20.86,"solv":0,"grid":"7x7","radius":"2 km"},{"name":"heilpraktiker charlottenburg","keyword":"heilpraktiker charlottenburg","top3":0,"of":49,"date":"2026-10-01","found_in":5,"arp":14.6,"atrp":20.35,"solv":0,"grid":"7x7","radius":"2 km"}]},"map_skipped_other_grid":[],"map_settings_mixed":false}},"banner":{"color":"amber","label":"Korrigiert","html":"Ein Google-Eintrag von dir zeigte „Permanent geschlossen“, obwohl du weiter geöffnet bist. Ich habe das sofort korrigiert, er ist wieder offen."},"guide":{"overview":{"pose":"point","text":"Dein größter Hebel: 21 von 34 Seiten zeigen bei Google noch den Namen hildegardbingen statt deines Praxisnamens. Ich warte auf dein Ja zu den ersten Karten, dann geht der neue Titel live."}},"needs":[{"t":"Der Fragebogen zur Positionierung wartet noch auf dich und hilft, für wen deine Seiten künftig schreiben.","go":"setup","btn":"Zur Einrichtung"}],"work":{"this_week":"Sieben Kategorien und 40 Leistungen in deinem Google-Profil sind gesetzt. Dein neues Startseiten-Design liegt als Vorschau bereit, mit wachsender Ranke, fünf Themen und sechs Leistungen.","done":"Deine ersten 13 Entscheidungskarten liegen bereit. Entscheide über den Namen hinter deinen Seitentiteln, über die ersten Seiten und über das neue Design."},"decisions_note":null,"source_note":"Zahlen gelesen am 19. Okt. 2026 aus der Google Search Console und den Google-Profilen. Eintragsstände aus dem 741-Portal.","profiles":[],"citations":{"live":1,"total":90,"by_status":{"planned":85,"live":1,"inconsistent":4},"read":"2026-10-19"}};DSH.loaded='x';DSH.admin=true;DSH.b={client:{id:'x'},apReady:true,apItems:[{title:'IV page',status:'draft'}],steps:[{kind:'stammdaten',status:'offen'}],grants:[],program:{start_date:'2026-09-14'}};
const views=['overview','results/enquiries','results/found','results/reviews','results/ads','results/backlinks','plan','reports','decisions','setup'];
let bad=0;
for(const p of ['nhc','beauty']){DSH.profile=p;for(const v of views){DSH.view=v;try{const h=dshInner({"client":{"id":"x","name":"t","lang":"en"},"apReady":true,"apItems":[{"title":"IV page","status":"draft"},{"title":"Prices","status":"open"}],"steps":[{"kind":"vertrag_avv","status":"erledigt"},{"kind":"stammdaten","status":"offen"}],"grants":[],"program":{"start_date":"2026-09-14"}});if(/undefined|NaN|\[object/.test(h)){console.log('SUSPECT',p,v,(h.match(/.{30}(undefined|NaN|\[object).{30}/)||[''])[0]);bad++}}catch(e){console.log('ERR',p,v,e.message);bad++}}}
console.log('done bad=',bad);