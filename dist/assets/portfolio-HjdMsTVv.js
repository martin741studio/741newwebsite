import"./modulepreload-polyfill-B5Qt9EMX.js";import*as p from"https://esm.sh/three";document.addEventListener("DOMContentLoaded",function(){const e=document.querySelector(".slider-wrapper");e&&e.classList.add("loaded")});const q={settings:{transitionDuration:2.5,autoSlideSpeed:3e3}};let c=0,f=!1,u,y,R,B,m=[],x=!1,b=null,T=null,g=!1,P=!1;const H=()=>q.settings.autoSlideSpeed,W=50,X=()=>q.settings.transitionDuration,a=[{title:"Single Fin",media:"/assets/Portfolio/BackgroundImages/pexels-elina-araja-1743227-3320136.jpg",mockup:"/assets/Portfolio/ClientMockups/SingleFin.png",description:"Dominated the Uluwatu beach club scene with a high-leverage digital booking engine that maximizes customer LTV. We eliminated acquisition friction by streamlining the VIP reservation workflow, resulting in a 40% uptick in high-ticket table retention."},{title:"Anna Nussbaumer",media:"/assets/Portfolio/BackgroundImages/pexels-lorenzo-castellino-61076802-16674815.jpg",mockup:"/assets/Portfolio/ClientMockups/AnnaNussbaumer.png",description:"Transformed personal coaching into a scalable digital asset through hormone-driven UX optimization. We stacked value by integrating cyclical life tracking into a premium membership platform, protecting user focus while driving 3x engagement."},{title:"Numero Quattro",media:"/assets/Portfolio/BackgroundImages/pexels-rudy-kirchner-278171-1229845.jpg",mockup:"/assets/Portfolio/ClientMockups/NumeroQuattro.png",description:"Re-engineered the digital footprint of a neighborhood Italian staple into a consistent monetization machine. We optimized the offer design to increase average order value through intuitive menu architecture and frictionless bookings."},{title:"Karin Lorenz",media:"/assets/Portfolio/BackgroundImages/pexels-phael-2291108.jpg",mockup:"/assets/Portfolio/ClientMockups/KarinLorenz.png",description:"Elevated TCM practice visibility with a premium, results-oriented digital presence. We focused on value stacking by simplifying complex healthcare information into actionable patient journeys, establishing institutional leadership."},{title:"IMMOKAUF.AT",media:"/assets/Portfolio/BackgroundImages/pexels-mike-chai-285623-842339.jpg",mockup:"/assets/Portfolio/ClientMockups/Immokauf.png",description:"Disrupted the Austrian real estate market with an asymmetric lead generation platform. We built a high-conversion engine that identifies motivated sellers through clear monetization math, accelerating deal flow through top-of-funnel screening."},{title:"Marugame Udon",media:"/assets/Portfolio/BackgroundImages/pexels-ruiyang-zhang-915467-3717291.jpg",mockup:"/assets/Portfolio/ClientMockups/MarugameUdon.png",description:"Scaled digital ROI for Japan's favorite handmade udon kitchen in Vancouver. We optimized unit economics by integrating a high-speed ordering workflow with clear value propositions, ensuring peak performance during high-demand windows."},{title:"Avli Uluwatu",media:"/assets/Portfolio/BackgroundImages/pexels-efrem-efre-2786187-19593172.jpg",mockup:"/assets/Portfolio/ClientMockups/AvliUluwatu.png",description:"Captured the modern Greek luxury market with a high-conversion digital experience tailored for high-ticket travelers. We eliminated friction in the customer journey to maximize booking retention and seasonal LTV."},{title:"Villa Ventures",media:"/assets/Portfolio/BackgroundImages/pexels-aleksandr-burzinskij-3169259-4987403.jpg",mockup:"/assets/Portfolio/ClientMockups/VillaVentures.png",description:"Transformed boutique property management into a high-yield digital asset. We optimized the acquisition economics for luxury rentals by stacking value into a seamless booking interface, handling elite international demand."},{title:"Stil Gefährten",media:"/assets/Portfolio/BackgroundImages/pexels-anna-louise-210491-1387848.jpg",mockup:"/assets/Portfolio/ClientMockups/StilGefaehrten.png",description:"Revolutionized event management economics through a results-oriented digital command center. We focused on retention by structuring information for high-frequency client engagement, protecting brand focus while scaling logistics."},{title:"Versance.ai",media:"/assets/Portfolio/BackgroundImages/pexels-dang-vu-hai-683750211-18781763.jpg",mockup:"/assets/Portfolio/ClientMockups/Versance.png",description:"Positioned an AI-driven IR agent at the forefront of financial communication leverage. We engineered a high-trust digital portal that converts institutional complexity into clear investor decisions and scalable capital market assets."},{title:"Talkinfive",media:"/assets/Portfolio/BackgroundImages/pexels-ian-panelo-4691122.jpg",mockup:"/assets/Portfolio/ClientMockups/TalkinFive.png",description:"Engineered a high-leverage digital strategy platform that maximizes customer acquisition ROI. We optimized monetization math by streamlining lead capture and follow-up workflows, accelerating business growth through data precision."},{title:"Protex Textiles",media:"/assets/Portfolio/BackgroundImages/pexels-kaue-barbier-710715348-33001980.jpg",mockup:"/assets/Portfolio/ClientMockups/ProtexTextiles.png",description:"Elevated industrial textile finishing into a digital-first market leader. We focused on operational leverage by digitizing complex product catalogs for global institutional buyers, protecting long-term market position."},{title:"Vertrauenszentrum",media:"/assets/Portfolio/BackgroundImages/pexels-marianamontrazi-7366424.jpg",mockup:"/assets/Portfolio/ClientMockups/Vertrauenszentrum.png",description:"Humanized medical support through a high-trust, authoritative digital resource. We optimized for patient retention by structuring information around clear journeys, establishing institutional leadership in the healthcare sector."},{title:"Tacheles",media:"/assets/Portfolio/BackgroundImages/pexels-maumascaro-376533.jpg",mockup:"/assets/Portfolio/ClientMockups/Tacheles.png",description:"Scaled a taboo-breaking lifestyle brand into a digital monetization engine. We simplified acquisition economics by building a high-impact narrative that drives community growth and converts engagement into brand equity."},{title:"IGR",media:"/assets/Portfolio/BackgroundImages/pexels-pixabay-458530.jpg",mockup:"/assets/Portfolio/ClientMockups/IGR.png",description:"Digitized the ergonomics innovation prize into a global authority for workplace health. We stacked value by showcasing curated research through a scalable information architecture, influencing long-term industry standards."},{title:"Yacht Charter Indonesia",media:"/assets/Portfolio/BackgroundImages/pexels-rudy-kirchner-278171-1229845.jpg",mockup:"/assets/Portfolio/ClientMockups/YachtCharterIndonesia.png",description:"Dominated the luxury maritime market with a high-conversion yacht booking engine. We optimized LTV by integrating curated local experiences with frictionless charter workflows, built for elite global acquisition."},{title:"WBG",media:"/assets/Portfolio/BackgroundImages/pexels-sliceisop-2280604.jpg",mockup:"/assets/Portfolio/ClientMockups/WBG.png",description:"Architected a structural information portal for public housing and urban scaling. We focused on civilizational growth by organizing district data into a clear interface, protecting public trust and urban resilience."},{title:"Vesta Noris",media:"/assets/Portfolio/BackgroundImages/pexels-szafran-16362694.jpg",mockup:"/assets/Portfolio/ClientMockups/VestaNoris.png",description:"Streamlined operational efficiency with a tailored digital asset. We engineered a scalable platform to maximize user engagement and optimize key conversion pathways."},{title:"Local SEO",media:"/assets/Portfolio/BackgroundImages/pexels-thevisualgriot-5936860.jpg",mockup:"/assets/Portfolio/ClientMockups/LocalSEO.gif",description:"Dominated local search visibility through an optimized digital infrastructure. We implemented data-driven architectures to drive hyper-local lead generation and sustainable organic growth."}];let S=0,I=0;const $=`
      varying vec2 vUv;
      void main() {
        vUv = uv;
        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
      }
    `,_=`
      uniform sampler2D uTexture1;
      uniform sampler2D uTexture2;
      uniform float uProgress;
      uniform vec2 uResolution;
      uniform vec2 uTexture1Size;
      uniform vec2 uTexture2Size;
      uniform int uEffectType;
      
      // Global settings uniforms
      uniform float uGlobalIntensity;
      uniform float uSpeedMultiplier;
      uniform float uDistortionStrength;
      uniform float uColorEnhancement;
      
      // Glass uniforms
      uniform float uGlassRefractionStrength;
      uniform float uGlassChromaticAberration;
      uniform float uGlassBubbleClarity;
      uniform float uGlassEdgeGlow;
      uniform float uGlassLiquidFlow;
      
      // Frost uniforms
      uniform float uFrostIntensity;
      uniform float uFrostCrystalSize;
      uniform float uFrostIceCoverage;
      uniform float uFrostTemperature;
      uniform float uFrostTexture;
      
      // Ripple uniforms
      uniform float uRippleFrequency;
      uniform float uRippleAmplitude;
      uniform float uRippleWaveSpeed;
      uniform float uRippleRippleCount;
      uniform float uRippleDecay;
      
      // Plasma uniforms
      uniform float uPlasmaIntensity;
      uniform float uPlasmaSpeed;
      uniform float uPlasmaEnergyIntensity;
      uniform float uPlasmaContrastBoost;
      uniform float uPlasmaTurbulence;
      
      // Timeshift uniforms
      uniform float uTimeshiftDistortion;
      uniform float uTimeshiftBlur;
      uniform float uTimeshiftFlow;
      uniform float uTimeshiftChromatic;
      uniform float uTimeshiftTurbulence;
      
      varying vec2 vUv;

      vec2 getCoverUV(vec2 uv, vec2 textureSize) {
        vec2 s = uResolution / textureSize;
        float scale = max(s.x, s.y);
        vec2 scaledSize = textureSize * scale;
        vec2 offset = (uResolution - scaledSize) * 0.5;
        return (uv * uResolution - offset) / scaledSize;
      }

      float noise(vec2 p) {
        return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453);
      }

      float smoothNoise(vec2 p) {
        vec2 i = floor(p);
        vec2 f = fract(p);
        f = f * f * (3.0 - 2.0 * f);
        
        return mix(
          mix(noise(i), noise(i + vec2(1.0, 0.0)), f.x),
          mix(noise(i + vec2(0.0, 1.0)), noise(i + vec2(1.0, 1.0)), f.x),
          f.y
        );
      }

      float rand(vec2 uv) {
        float a = dot(uv, vec2(92., 80.));
        float b = dot(uv, vec2(41., 62.));
        float x = sin(a) + cos(b) * 51.;
        return fract(x);
      }

      vec4 rippleEffect(vec2 uv, float progress) {
        vec4 currentImg = texture2D(uTexture1, getCoverUV(uv, uTexture1Size));
        vec4 newImg = texture2D(uTexture2, getCoverUV(uv, uTexture2Size));
        
        vec2 center = vec2(0.5, 0.5);
        float dist = distance(uv, center);
        
        // Add simple turbulent spatial noise using pure sine interference (WebGL 1.0 safe)
        float morph = sin(uv.x * 20.0 + progress * 10.0) * cos(uv.y * 20.0 - progress * 10.0) * 0.05 * sin(progress * 3.14);
        dist += morph; 
        
        float maxDist = 0.8;
        
        float effectiveSpeed = uRippleWaveSpeed * uSpeedMultiplier * 1.2; 
        float effectiveAmplitude = uRippleAmplitude * uDistortionStrength * uGlobalIntensity * 3.0; // 3x stronger
        float effectiveDecay = uRippleDecay * 0.5; // Lower decay so it travels thicker and further
        
        float waveRadius = progress * maxDist * 1.5 * effectiveSpeed;
        
        // Calculate the distance from the current wave front
        float distDiff = dist - waveRadius;
        
        // Single focused highly-refractive ripple (1 crest only)
        // Using an exponential gaussian burst instead of a sine wave ensures exactly ONE ripple ring.
        float singleRing = exp(-pow(distDiff * 12.0, 2.0)) * exp(-abs(distDiff) * 4.0 * effectiveDecay);
        
        float combinedRipple = singleRing * effectiveAmplitude * 1.5; // boosted to compensate for single ring
        
        vec2 normal = normalize(uv - center);
        
        // Simulate extreme chromatic aberration for heavy glassy chunk feel
        vec2 distortedUV = getCoverUV(uv + normal * combinedRipple, uTexture2Size);
        vec2 distortedUVR = getCoverUV(uv + normal * (combinedRipple * 1.35), uTexture2Size);
        vec2 distortedUVB = getCoverUV(uv + normal * (combinedRipple * 0.65), uTexture2Size);
        
        vec4 distortedImg = texture2D(uTexture2, distortedUV);
        distortedImg.r = texture2D(uTexture2, distortedUVR).r;
        distortedImg.b = texture2D(uTexture2, distortedUVB).b;
        
        float fadeEdge = smoothstep(maxDist, maxDist * 0.9, dist);
        vec4 rippleResult = mix(newImg, distortedImg, fadeEdge);
        
        float mask = smoothstep(0.0, 0.2, progress) * (1.0 - smoothstep(0.8, 1.0, progress));
        rippleResult = mix(newImg, rippleResult, mask);
        
        // Apply color enhancement with #fac118 brand yellow tint based on distortion intensity
        vec3 yellowTint = vec3(0.98, 0.75, 0.09); // #fac118
        
        // Calculate an intensely shiny glossy highlight peaking at the wave crests
        float specular = pow(clamp(singleRing * 1.5, 0.0, 1.0), 4.0);
        
        float rippleIntensity = abs(combinedRipple) * 8.0; 
        float tintWeight = clamp(rippleIntensity * mask, 0.0, 0.7); // Let the yellow bleed in more heavily
        
        rippleResult.rgb = mix(rippleResult.rgb, yellowTint, tintWeight);
        // Add Specular Highlights for extreme glassy pop
        rippleResult.rgb += specular * mask * yellowTint * 1.5;
        
        float transition = smoothstep(0.0, 1.0, progress);
        return mix(currentImg, rippleResult, transition);
      }

      /// Omitting other effects like glass, plasma, frost, etc. for token size temporarily since the user wants the ripple.
      /// The requested code had multiple effects, so we will stub them back to ripple as a fallback if selected.
      
      void main() {
        gl_FragColor = rippleEffect(vUv, uProgress);
      }
    `,K=()=>{const e=document.querySelector(".slides-navigation");if(!e)return;e.innerHTML="",a.forEach((r,n)=>{const s=document.createElement("button");s.className=`slide-nav-item${n===c?" active":""}`,s.id=`nav-${n+1}`,s.innerHTML=`
      <div class="slide-progress-line">
        <div class="slide-progress-fill"></div>
      </div>
      <span class="slide-nav-title">${r.title}</span>
    `,s.addEventListener("click",l=>{l.preventDefault(),l.stopPropagation(),n!==c&&!f&&z(n)}),s.addEventListener("touchstart",l=>{l.stopPropagation()},{passive:!0}),e.appendChild(s)});let i=!1,t,o;e.addEventListener("mousedown",r=>{i=!0,t=r.pageX-e.offsetLeft,o=e.scrollLeft}),e.addEventListener("mouseleave",()=>i=!1),e.addEventListener("mouseup",()=>i=!1),e.addEventListener("mousemove",r=>{if(!i)return;r.preventDefault();const s=(r.pageX-e.offsetLeft-t)*2;e.scrollLeft=o-s})},F=e=>{document.querySelectorAll(".slide-nav-item").forEach((t,o)=>{t.classList.toggle("active",o===e)})},Q=(e,i)=>{const t=document.querySelectorAll(".slide-nav-item");if(t[e]){const o=t[e].querySelector(".slide-progress-fill");o.style.width=`${i}%`,o.style.opacity="1"}},Y=e=>{const i=document.querySelectorAll(".slide-nav-item");if(i[e]){const t=i[e].querySelector(".slide-progress-fill");t.style.opacity="0",setTimeout(()=>t.style.width="0%",300)}},L=e=>{const i=document.querySelectorAll(".slide-nav-item");if(i[e]){const t=i[e].querySelector(".slide-progress-fill");t.style.transition="width 0.2s ease-out",t.style.width="0%",setTimeout(()=>{t.style.transition="width 0.1s ease, opacity 0.3s ease"},200)}},U=e=>{const i=document.querySelector(".slide-number");i&&(i.textContent=String(e+1).padStart(2,"0"));const t=document.querySelector(".slide-total");t&&(t.textContent=String(a.length).padStart(2,"0"))},V=()=>{if(!x||!g||!P&&m.length<2)return;h();let e=0;const i=100/H()*W;T=setInterval(()=>{if(!g){h();return}f||(e+=i,Q(c,e),e>=100&&(e=0,Y(c),j()))},W)},h=()=>{T&&(clearInterval(T),T=null),b&&(clearTimeout(b),b=null)},k=(e=0)=>{h(),g&&x&&(e>0?b=setTimeout(()=>{g&&V()},e):V())},z=async e=>{if(f||e===c)return;f=!0,e=(e+a.length)%a.length,h(),L(c);let i;if(!P){if(!m[e])try{const v=await D(a[e].media);m[e]=v}catch{console.warn(`Critical: Failed to load slide ${e}, skipping...`),f=!1,z((e+1)%a.length);return}const d=m[c];if(i=m[e],!d||!i){console.warn("Missing textures for transition. Index:",c,e),f=!1,k(500);return}u.uniforms.uTexture1.value=d,u.uniforms.uTexture2.value=i,u.uniforms.uTexture1Size.value=d.userData.size,u.uniforms.uTexture2Size.value=i.userData.size}const t=document.getElementById("current-mockup"),o=document.getElementById("content-overlay"),r=document.getElementById("overlay-title"),n=document.getElementById("overlay-description"),s=a[e];t&&t.classList.remove("active"),o&&o.classList.remove("active"),setTimeout(()=>{s.mockup&&t&&(t.onload=()=>t.classList.add("active"),t.src=s.mockup,t.alt=`741 Studio Client Portfolio: ${s.title}`,t.complete&&t.classList.add("active")),r&&(r.textContent=s.title),n&&(n.textContent=s.description||""),o&&o.classList.add("active")},400),c=e,U(c),F(c);const l=document.getElementById(`nav-${e+1}`);if(l&&l.scrollIntoView({behavior:"smooth",block:"nearest",inline:"center"}),P)setTimeout(()=>{f=!1,k(100)},800);else{const d=performance.now(),v=X()*1e3,M=G=>{const N=G-d,w=Math.min(N/v,1),O=w<.5?2*w*w:1-Math.pow(-2*w+2,2)/2;u.uniforms.uProgress.value=O,w<1?requestAnimationFrame(M):(u.uniforms.uProgress.value=0,u.uniforms.uTexture1.value=i,u.uniforms.uTexture1Size.value=i.userData.size,f=!1,k(100))};requestAnimationFrame(M)}},j=()=>{if(f||!x||!g)return;const e=(c+1)%a.length;z(e)},J=()=>{if(!(Math.abs(I-S)<50)){if(I<S&&!f&&g)h(),L(c),j();else if(I>S&&!f&&g){h(),L(c);const e=(c-1+a.length)%a.length;z(e)}}},D=e=>new Promise((i,t)=>{const o=new p.TextureLoader,r=setTimeout(()=>t(new Error("Timeout")),1e4);o.load(e,n=>{clearTimeout(r),n.minFilter=n.magFilter=p.LinearFilter,n.userData={size:new p.Vector2(n.image.width,n.image.height)},i(n)},void 0,n=>{clearTimeout(r),t(n)})}),Z=async()=>{const e=document.querySelector(".webgl-canvas");if(!e)return;const i=document.createElement("canvas");i.className="webgl-canvas",e.replaceWith(i),R=new p.Scene,B=new p.OrthographicCamera(-1,1,1,-1,0,1),y=new p.WebGLRenderer({canvas:i,antialias:!1,alpha:!1}),y.setSize(window.innerWidth,window.innerHeight),y.setPixelRatio(Math.min(window.devicePixelRatio,2)),u=new p.ShaderMaterial({uniforms:{uTexture1:{value:null},uTexture2:{value:null},uProgress:{value:0},uResolution:{value:new p.Vector2(window.innerWidth,window.innerHeight)},uTexture1Size:{value:new p.Vector2(1,1)},uTexture2Size:{value:new p.Vector2(1,1)},uEffectType:{value:2},uGlobalIntensity:{value:1},uSpeedMultiplier:{value:1},uDistortionStrength:{value:1},uColorEnhancement:{value:1},uRippleFrequency:{value:25},uRippleAmplitude:{value:.08},uRippleWaveSpeed:{value:1},uRippleRippleCount:{value:1},uRippleDecay:{value:1}},vertexShader:$,fragmentShader:_});const t=new p.PlaneGeometry(2,2),o=new p.Mesh(t,u);R.add(o);const r=async()=>{const l=Math.min(a.length,2);for(let d=0;d<l;d++)try{const v=await D(a[d].media);m[d]=v}catch{console.warn("Failed to load initial image "+d)}m[0]&&(u.uniforms.uTexture1.value=m[0],u.uniforms.uTexture1Size.value=m[0].userData.size,m[1]&&(u.uniforms.uTexture2.value=m[1],u.uniforms.uTexture2Size.value=m[1].userData.size),x=!0,g=!0,k(1500))},n=async()=>{for(let l=2;l<a.length;l++)if(!m[l])try{const d=await D(a[l].media);m[l]=d}catch{console.warn("Background load failed for "+l)}};await r(),n();const s=()=>{requestAnimationFrame(s),y.render(R,B)};s()};let A=!1;const C=async()=>{if(A)return;A=!0,K(),U(0),F(0);const e=document.getElementById("current-mockup"),i=document.getElementById("content-overlay"),t=document.getElementById("overlay-title"),o=document.getElementById("overlay-description");a[0].mockup&&e&&(e.onload=()=>e.classList.add("active"),e.src=a[0].mockup,e.alt=`741 Studio Client Portfolio: ${a[0].title}`,e.complete&&e.classList.add("active")),t&&(t.textContent=a[0].title),o&&(o.textContent=a[0].description||""),i&&i.classList.add("active");try{await Z()}catch(r){console.error("WebGL Renderer Error:",r),P=!0,x=!0,g=!0,k(1500)}};document.readyState==="complete"||document.readyState==="interactive"?setTimeout(C,1):(window.addEventListener("DOMContentLoaded",C),window.addEventListener("load",C));const E=document.querySelector(".slider-wrapper");E&&(E.addEventListener("touchstart",e=>{e.target.closest(".slides-navigation")||(S=e.changedTouches[0].screenX)},{passive:!0}),E.addEventListener("touchend",e=>{e.target.closest(".slides-navigation")||(I=e.changedTouches[0].screenX,J())},{passive:!0}));window.addEventListener("resize",()=>{y&&u&&(y.setSize(window.innerWidth,window.innerHeight),u.uniforms.uResolution.value.set(window.innerWidth,window.innerHeight))});document.addEventListener("visibilitychange",()=>{document.hidden?h():g&&!f&&k()});
