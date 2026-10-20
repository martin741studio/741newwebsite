const fs=require('fs');
const js=fs.readFileSync('src/dsh.js','utf8');
const feed=JSON.parse(fs.readFileSync(process.env.FEED||'src/feed-bali.json','utf8'));
const pre=`const esc=s=>String(s??'');const apGuide=(p,t)=>'<aside>'+t+'</aside>';const apOn=()=>true;const apOpenCount=()=>2;const apRenderClient=()=>'<div>decisions</div>';const renderOnboarding=()=>'<div>onb</div>';const renderGrants=()=>'<div>grants</div>';const renderMaterials=()=>'<div>mat</div>';const renderChat=()=>'<div>chat</div>';const rerender=()=>{};const applyShellLang=()=>{};const $=()=>({});const document={getElementById:()=>null};const window={scrollTo(){},addEventListener(){}};const history={pushState(){},replaceState(){}};const location={hash:''};const bundleIsAdmin=true;let adminSub='dash';const closeReport=()=>{};const openReport=()=>{};const fetch=()=>Promise.reject(new Error('x'));`;
const b={client:{id:'x',name:'t',lang:'en'},apReady:true,apItems:[{title:'IV page',status:'draft'},{title:'Prices',status:'open'}],steps:[{kind:'vertrag_avv',status:'erledigt'},{kind:'stammdaten',status:'offen'}],grants:[],program:{start_date:'2026-09-14'}};
const code=pre+js+`
DSH.d=${JSON.stringify(feed)};DSH.loaded='x';DSH.admin=true;DSH.b={client:{id:'x'},apReady:true,apItems:[{title:'IV page',status:'draft'}],steps:[{kind:'stammdaten',status:'offen'}],grants:[],program:{start_date:'2026-09-14'}};
const views=['overview','results/enquiries','results/found','results/reviews','results/ads','results/backlinks','plan','reports','decisions','setup'];
let bad=0;
for(const p of ['nhc','beauty']){DSH.profile=p;for(const v of views){DSH.view=v;try{const h=dshInner(${JSON.stringify(b)});if(/undefined|NaN|\\[object/.test(h)){console.log('SUSPECT',p,v,(h.match(/.{30}(undefined|NaN|\\[object).{30}/)||[''])[0]);bad++}}catch(e){console.log('ERR',p,v,e.message);bad++}}}
console.log('done bad=',bad);`;
fs.writeFileSync('/tmp/smoke-run.js',code);
