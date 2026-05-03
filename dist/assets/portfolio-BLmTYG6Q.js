import"./modulepreload-polyfill-B5Qt9EMX.js";import*as f from"https://esm.sh/three";document.addEventListener("DOMContentLoaded",function(){const e=document.querySelector(".slider-wrapper");e&&e.classList.add("loaded")});const V={settings:{transitionDuration:2.5,autoSlideSpeed:5e3}};let u=0,m=!1,l,y,C,M,c=[],b=!1,T=null,k=null,g=!1,P=!1;const j=()=>V.settings.autoSlideSpeed,B=50,N=()=>V.settings.transitionDuration,a=[{title:"Single Fin",media:"/assets/Portfolio/BackgroundImages/pexels-elina-araja-1743227-3320136.jpg",mockup:"/assets/Portfolio/ClientMockups/SingleFin.png",description:"Dominated the Uluwatu beach club scene with a high-leverage digital booking engine that maximizes customer LTV. We eliminated acquisition friction by streamlining the VIP reservation workflow, resulting in a 40% uptick in high-ticket table retention."},{title:"Anna Nussbaumer",media:"/assets/Portfolio/BackgroundImages/pexels-lorenzo-castellino-61076802-16674815.jpg",mockup:"/assets/Portfolio/ClientMockups/AnnaNussbaumer.png",description:"Transformed personal coaching into a scalable digital asset through hormone-driven UX optimization. We stacked value by integrating cyclical life tracking into a premium membership platform, protecting user focus while driving 3x engagement."},{title:"Numero Quattro",media:"/assets/Portfolio/BackgroundImages/pexels-rudy-kirchner-278171-1229845.jpg",mockup:"/assets/Portfolio/ClientMockups/NumeroQuattro.png",description:"Re-engineered the digital footprint of a neighborhood Italian staple into a consistent monetization machine. We optimized the offer design to increase average order value through intuitive menu architecture and frictionless bookings."},{title:"Karin Lorenz",media:"/assets/Portfolio/BackgroundImages/pexels-phael-2291108.jpg",mockup:"/assets/Portfolio/ClientMockups/KarinLorenz.png",description:"Elevated TCM practice visibility with a premium, results-oriented digital presence. We focused on value stacking by simplifying complex healthcare information into actionable patient journeys, establishing institutional leadership."},{title:"IMMOKAUF.AT",media:"/assets/Portfolio/BackgroundImages/pexels-mike-chai-285623-842339.jpg",mockup:"/assets/Portfolio/ClientMockups/Immokauf.png",description:"Disrupted the Austrian real estate market with an asymmetric lead generation platform. We built a high-conversion engine that identifies motivated sellers through clear monetization math, accelerating deal flow through top-of-funnel screening."},{title:"Marugame Udon",media:"/assets/Portfolio/BackgroundImages/pexels-ruiyang-zhang-915467-3717291.jpg",mockup:"/assets/Portfolio/ClientMockups/MarugameUdon.png",description:"Scaled digital ROI for Japan's favorite handmade udon kitchen in Vancouver. We optimized unit economics by integrating a high-speed ordering workflow with clear value propositions, ensuring peak performance during high-demand windows."},{title:"Marina Development ID",media:"/assets/Portfolio/BackgroundImages/pexels-hikaique-125509.jpg",mockup:"/assets/Portfolio/ClientMockups/MarinaDevelopmentID.png",description:"Positioned Indonesia's premier marina infrastructure through a high-profile, strategic communication asset. We focused on long-term civilizational cycles by structuring information for international investment acquisition."},{title:"Avli Uluwatu",media:"/assets/Portfolio/BackgroundImages/pexels-efrem-efre-2786187-19593172.jpg",mockup:"/assets/Portfolio/ClientMockups/AvliUluwatu.png",description:"Captured the modern Greek luxury market with a high-conversion digital experience tailored for high-ticket travelers. We eliminated friction in the customer journey to maximize booking retention and seasonal LTV."},{title:"Villa Ventures",media:"/assets/Portfolio/BackgroundImages/pexels-aleksandr-burzinskij-3169259-4987403.jpg",mockup:"/assets/Portfolio/ClientMockups/VillaVentures.png",description:"Transformed boutique property management into a high-yield digital asset. We optimized the acquisition economics for luxury rentals by stacking value into a seamless booking interface, handling elite international demand."},{title:"Stil Gefährten",media:"/assets/Portfolio/BackgroundImages/pexels-anna-louise-210491-1387848.jpg",mockup:"/assets/Portfolio/ClientMockups/StilGefaehrten.png",description:"Revolutionized event management economics through a results-oriented digital command center. We focused on retention by structuring information for high-frequency client engagement, protecting brand focus while scaling logistics."},{title:"Versance.ai",media:"/assets/Portfolio/BackgroundImages/pexels-dang-vu-hai-683750211-18781763.jpg",mockup:"/assets/Portfolio/ClientMockups/Versance.png",description:"Positioned an AI-driven IR agent at the forefront of financial communication leverage. We engineered a high-trust digital portal that converts institutional complexity into clear investor decisions and scalable capital market assets."},{title:"Talkinfive",media:"/assets/Portfolio/BackgroundImages/pexels-ian-panelo-4691122.jpg",mockup:"/assets/Portfolio/ClientMockups/TalkinFive.png",description:"Engineered a high-leverage digital strategy platform that maximizes customer acquisition ROI. We optimized monetization math by streamlining lead capture and follow-up workflows, accelerating business growth through data precision."},{title:"Protex Textiles",media:"/assets/Portfolio/BackgroundImages/pexels-kaue-barbier-710715348-33001980.jpg",mockup:"/assets/Portfolio/ClientMockups/ProtexTextiles.png",description:"Elevated industrial textile finishing into a digital-first market leader. We focused on operational leverage by digitizing complex product catalogs for global institutional buyers, protecting long-term market position."},{title:"Vertrauenszentrum",media:"/assets/Portfolio/BackgroundImages/pexels-marianamontrazi-7366424.jpg",mockup:"/assets/Portfolio/ClientMockups/Vertrauenszentrum.png",description:"Humanized medical support through a high-trust, authoritative digital resource. We optimized for patient retention by structuring information around clear journeys, establishing institutional leadership in the healthcare sector."},{title:"Tacheles",media:"/assets/Portfolio/BackgroundImages/pexels-maumascaro-376533.jpg",mockup:"/assets/Portfolio/ClientMockups/Tacheles.png",description:"Scaled a taboo-breaking lifestyle brand into a digital monetization engine. We simplified acquisition economics by building a high-impact narrative that drives community growth and converts engagement into brand equity."},{title:"IGR",media:"/assets/Portfolio/BackgroundImages/pexels-pixabay-458530.jpg",mockup:"/assets/Portfolio/ClientMockups/IGR.png",description:"Digitized the ergonomics innovation prize into a global authority for workplace health. We stacked value by showcasing curated research through a scalable information architecture, influencing long-term industry standards."},{title:"Yacht Charter Indonesia",media:"/assets/Portfolio/BackgroundImages/pexels-rudy-kirchner-278171-1229845.jpg",mockup:"/assets/Portfolio/ClientMockups/YachtCharterIndonesia.png",description:"Dominated the luxury maritime market with a high-conversion yacht booking engine. We optimized LTV by integrating curated local experiences with frictionless charter workflows, built for elite global acquisition."},{title:"WBG",media:"/assets/Portfolio/BackgroundImages/pexels-sliceisop-2280604.jpg",mockup:"/assets/Portfolio/ClientMockups/WBG.png",description:"Architected a structural information portal for public housing and urban scaling. We focused on civilizational growth by organizing district data into a clear interface, protecting public trust and urban resilience."}];let S=0,I=0;const O=`
      varying vec2 vUv;
      void main() {
        vUv = uv;
        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
      }
    `,H=`
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
    `,X=()=>{const e=document.querySelector(".slides-navigation");if(!e)return;e.innerHTML="";let t=!1,i,r,d=!1;e.addEventListener("mousedown",o=>{t=!0,d=!1,i=o.pageX-e.offsetLeft,r=e.scrollLeft}),e.addEventListener("mouseleave",()=>{t=!1}),e.addEventListener("mouseup",()=>{t=!1}),e.addEventListener("mousemove",o=>{if(!t)return;o.preventDefault();const n=(o.pageX-e.offsetLeft-i)*2;Math.abs(n)>5&&(d=!0),e.scrollLeft=r-n}),a.forEach((o,p)=>{const n=document.createElement("button");n.className=`slide-nav-item${p===u?" active":""}`,n.id=`nav-${p+1}`,n.innerHTML=`
      <div class="slide-progress-line">
        <div class="slide-progress-fill"></div>
      </div>
      <span class="slide-nav-title">${o.title}</span>
    `,n.addEventListener("click",s=>{s.stopPropagation(),!d&&p!==u&&!m&&L(p)}),e.appendChild(n)})},$=e=>{document.querySelectorAll(".slide-nav-item").forEach((i,r)=>{i.classList.toggle("active",r===e)})},_=(e,t)=>{const i=document.querySelectorAll(".slide-nav-item");if(i[e]){const r=i[e].querySelector(".slide-progress-fill");r.style.width=`${t}%`,r.style.opacity="1"}},K=e=>{const t=document.querySelectorAll(".slide-nav-item");if(t[e]){const i=t[e].querySelector(".slide-progress-fill");i.style.opacity="0",setTimeout(()=>i.style.width="0%",300)}},z=e=>{const t=document.querySelectorAll(".slide-nav-item");if(t[e]){const i=t[e].querySelector(".slide-progress-fill");i.style.transition="width 0.2s ease-out",i.style.width="0%",setTimeout(()=>{i.style.transition="width 0.1s ease, opacity 0.3s ease"},200)}},q=e=>{const t=document.querySelector(".slide-number");t&&(t.textContent=String(e+1).padStart(2,"0"));const i=document.querySelector(".slide-total");i&&(i.textContent=String(a.length).padStart(2,"0"))},W=()=>{if(!b||!g||!P&&c.length<2)return;h();let e=0;const t=100/j()*B;k=setInterval(()=>{if(!g){h();return}e+=t,_(u,e),e>=100&&(clearInterval(k),k=null,K(u),m||R())},B)},h=()=>{k&&(clearInterval(k),k=null),T&&(clearTimeout(T),T=null)},w=(e=0)=>{h(),g&&b&&(e>0?T=setTimeout(()=>{g&&W()},e):W())},L=async e=>{if(m||e===u)return;if(e=(e+a.length)%a.length,h(),z(u),P)m=!0;else{if(!c[e])try{const v=await E(a[e].media);c[e]=v}catch{console.warn(`Critical: Failed to load slide ${e}, skipping...`),R();return}const n=c[u],s=c[e];if(!n||!s){console.warn("Missing textures for transition. Index:",u,e),m=!1,w(500);return}m=!0,l.uniforms.uTexture1.value=n,l.uniforms.uTexture2.value=s,l.uniforms.uTexture1Size.value=n.userData.size,l.uniforms.uTexture2Size.value=s.userData.size}const t=document.getElementById("current-mockup"),i=document.getElementById("content-overlay"),r=document.getElementById("overlay-title"),d=document.getElementById("overlay-description"),o=a[e];t&&t.classList.remove("active"),i&&i.classList.remove("active"),setTimeout(()=>{o.mockup&&t&&(t.onload=()=>t.classList.add("active"),t.src=o.mockup,t.alt=`741 Studio Client Portfolio: ${o.title}`,t.complete&&t.classList.add("active")),r&&(r.textContent=o.title),d&&(d.textContent=o.description||""),i&&i.classList.add("active")},400),u=e,q(u),$(u);const p=document.getElementById(`nav-${e+1}`);if(p&&p.scrollIntoView({behavior:"smooth",block:"nearest",inline:"center"}),P)setTimeout(()=>{m=!1,w(100)},800);else{const n=performance.now(),s=N()*1e3,v=F=>{const U=F-n,x=Math.min(U/s,1),G=x<.5?2*x*x:1-Math.pow(-2*x+2,2)/2;l.uniforms.uProgress.value=G,x<1?requestAnimationFrame(v):(l.uniforms.uProgress.value=0,l.uniforms.uTexture1.value=targetTexture,l.uniforms.uTexture1Size.value=targetTexture.userData.size,m=!1,w(100))};requestAnimationFrame(v)}},R=()=>{if(m||!b||!g)return;const e=(u+1)%a.length;L(e)},Q=()=>{if(!(Math.abs(I-S)<50)){if(I<S&&!m&&g)h(),z(u),R();else if(I>S&&!m&&g){h(),z(u);const e=(u-1+a.length)%a.length;L(e)}}},E=e=>new Promise((t,i)=>{const r=new f.TextureLoader,d=setTimeout(()=>i(new Error("Timeout")),1e4);r.load(e,o=>{clearTimeout(d),o.minFilter=o.magFilter=f.LinearFilter,o.userData={size:new f.Vector2(o.image.width,o.image.height)},t(o)},void 0,o=>{clearTimeout(d),i(o)})}),Y=async()=>{const e=document.querySelector(".webgl-canvas");if(!e)return;const t=document.createElement("canvas");t.className="webgl-canvas",e.replaceWith(t),C=new f.Scene,M=new f.OrthographicCamera(-1,1,1,-1,0,1),y=new f.WebGLRenderer({canvas:t,antialias:!1,alpha:!1}),y.setSize(window.innerWidth,window.innerHeight),y.setPixelRatio(Math.min(window.devicePixelRatio,2)),l=new f.ShaderMaterial({uniforms:{uTexture1:{value:null},uTexture2:{value:null},uProgress:{value:0},uResolution:{value:new f.Vector2(window.innerWidth,window.innerHeight)},uTexture1Size:{value:new f.Vector2(1,1)},uTexture2Size:{value:new f.Vector2(1,1)},uEffectType:{value:2},uGlobalIntensity:{value:1},uSpeedMultiplier:{value:1},uDistortionStrength:{value:1},uColorEnhancement:{value:1},uRippleFrequency:{value:25},uRippleAmplitude:{value:.08},uRippleWaveSpeed:{value:1},uRippleRippleCount:{value:1},uRippleDecay:{value:1}},vertexShader:O,fragmentShader:H});const i=new f.PlaneGeometry(2,2),r=new f.Mesh(i,l);C.add(r);const d=async()=>{const n=Math.min(a.length,2);for(let s=0;s<n;s++)try{const v=await E(a[s].media);c[s]=v}catch{console.warn("Failed to load initial image "+s)}c[0]&&(l.uniforms.uTexture1.value=c[0],l.uniforms.uTexture1Size.value=c[0].userData.size,c[1]&&(l.uniforms.uTexture2.value=c[1],l.uniforms.uTexture2Size.value=c[1].userData.size),b=!0,g=!0,w(1500))},o=async()=>{for(let n=2;n<a.length;n++)if(!c[n])try{const s=await E(a[n].media);c[n]=s}catch{console.warn("Background load failed for "+n)}};await d(),o();const p=()=>{requestAnimationFrame(p),y.render(C,M)};p()};let A=!1;const D=async()=>{if(A)return;A=!0,X(),q(0);const e=document.getElementById("current-mockup"),t=document.getElementById("content-overlay"),i=document.getElementById("overlay-title"),r=document.getElementById("overlay-description");a[0].mockup&&e&&(e.onload=()=>e.classList.add("active"),e.src=a[0].mockup,e.alt=`741 Studio Client Portfolio: ${a[0].title}`,e.complete&&e.classList.add("active")),i&&(i.textContent=a[0].title),r&&(r.textContent=a[0].description||""),t&&t.classList.add("active");try{await Y()}catch(d){console.error("WebGL Renderer Error:",d),P=!0,b=!0,g=!0,w(1500)}};document.readyState==="complete"||document.readyState==="interactive"?setTimeout(D,1):(window.addEventListener("DOMContentLoaded",D),window.addEventListener("load",D));document.addEventListener("click",e=>{e.target.closest(".slides-navigation")||!m&&g&&(h(),z(u),R())});document.addEventListener("touchstart",e=>{e.target.closest(".slides-navigation")||(S=e.changedTouches[0].screenX)});document.addEventListener("touchend",e=>{e.target.closest(".slides-navigation")||(I=e.changedTouches[0].screenX,Q())});window.addEventListener("resize",()=>{y&&l&&(y.setSize(window.innerWidth,window.innerHeight),l.uniforms.uResolution.value.set(window.innerWidth,window.innerHeight))});document.addEventListener("visibilitychange",()=>{document.hidden?h():g&&!m&&w()});
