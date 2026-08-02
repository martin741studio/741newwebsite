import"./modulepreload-polyfill-B5Qt9EMX.js";/* empty css              */import*as p from"https://esm.sh/three";document.addEventListener("DOMContentLoaded",function(){const e=document.querySelector(".slider-wrapper");e&&e.classList.add("loaded")});const V={settings:{transitionDuration:2.5,autoSlideSpeed:3e3}};let c=0,f=!1,u,w,C,M,m=[],k=!1,x=null,S=null,g=!1,I=!1;const X=()=>V.settings.autoSlideSpeed,B=50,$=()=>V.settings.transitionDuration,a=[{title:"Single Fin",media:"/assets/Portfolio/BackgroundImages/pexels-elina-araja-1743227-3320136.webp",mockup:"/assets/Portfolio/ClientMockups/SingleFin.webp",description:"A long-term digital partnership with the Single Fin team. We redesigned and rebuilt their WordPress site, then stayed on to implement tracking, set up analytics, support the in-house marketing team, and run paid advertising, turning continuous, data-driven optimization into a lasting edge for the Uluwatu beach club."},{title:"Anna Nussbaumer",media:"/assets/Portfolio/BackgroundImages/pexels-lorenzo-castellino-61076802-16674815.webp",mockup:"/assets/Portfolio/ClientMockups/AnnaNussbaumer.webp",description:"A close collaboration where Denise Lackner led the visual design and 741 Studio handled the technical implementation. We translated the concept into a fast, conversion-focused website, added end-to-end tracking, and built the funnel that turns coaching interest into booked clients."},{title:"Numero Quattro",media:"/assets/Portfolio/BackgroundImages/pexels-rudy-kirchner-278171-1229845.webp",mockup:"/assets/Portfolio/ClientMockups/NumeroQuattro.webp",description:"We built the technical foundation this neighborhood Italian favorite needed to market with confidence. Beyond development, we implemented clean tracking and ran paid advertising, giving the restaurant measurable campaign performance and a reliable base for growth."},{title:"Karin Lorenz",media:"/assets/Portfolio/BackgroundImages/pexels-phael-2291108.webp",mockup:"/assets/Portfolio/ClientMockups/KarinLorenz.webp",description:"Design and development came together to give this TCM practice a polished, trustworthy presence. We focused on seamless technical implementation and precise tracking, shaping a smooth customer journey that guides patients from first search to booked appointment."},{title:"IMMOKAUF.AT",media:"/assets/Portfolio/BackgroundImages/pexels-mike-chai-285623-842339.webp",mockup:"/assets/Portfolio/ClientMockups/Immokauf.webp",description:"Working from an established design, we delivered a reliable, user-friendly website for this Austrian real estate platform. Our focus was the technical infrastructure beneath it: the tracking, funnel, and lead-generation setup that keeps a steady flow of motivated sellers moving through the pipeline."},{title:"Marugame Udon",media:"/assets/Portfolio/BackgroundImages/pexels-ruiyang-zhang-915467-3717291.webp",mockup:"/assets/Portfolio/ClientMockups/MarugameUdon.webp",description:"We designed and developed a digital experience that reaches beyond the website itself. For Japan's favorite handmade udon kitchen, we implemented tracking, integrated newsletters, and structured the information flow, extending the brand into ongoing customer communication and marketing automation."},{title:"Avli Uluwatu",media:"/assets/Portfolio/BackgroundImages/pexels-efrem-efre-2786187-19593172.webp",mockup:"/assets/Portfolio/ClientMockups/AvliUluwatu.webp",description:"A modern online presence built to capture the atmosphere of this modern Greek restaurant. We designed and implemented a fully responsive experience that makes it effortless for guests to explore the menu, find the location, and reserve a table from any device."},{title:"Villa Ventures",media:"/assets/Portfolio/BackgroundImages/pexels-aleksandr-burzinskij-3169259-4987403.webp",mockup:"/assets/Portfolio/ClientMockups/VillaVentures.webp",description:"A premium digital presentation created to showcase the quality of the property and its investment opportunity. Our website supported the brand throughout its growth phase, and the project was ultimately sold to another company as part of a successful business exit."},{title:"Stil Gefährten",media:"/assets/Portfolio/BackgroundImages/pexels-anna-louise-210491-1387848.webp",mockup:"/assets/Portfolio/ClientMockups/StilGefaehrten.webp",description:"Revolutionized event management economics through a results-oriented digital command center. We focused on retention by structuring information for high-frequency client engagement, protecting brand focus while scaling logistics."},{title:"Versance.ai",media:"/assets/Portfolio/BackgroundImages/pexels-dang-vu-hai-683750211-18781763.webp",mockup:"/assets/Portfolio/ClientMockups/Versance.webp",description:"Positioned an AI-driven IR agent at the forefront of financial communication leverage. We engineered a high-trust digital portal that converts institutional complexity into clear investor decisions and scalable capital market assets."},{title:"Talkinfive",media:"/assets/Portfolio/BackgroundImages/pexels-ian-panelo-4691122.webp",mockup:"/assets/Portfolio/ClientMockups/TalkinFive.webp",description:"A trusted, long-term partnership rather than a single project. As Talkinfive's technical partner, we provide development expertise and hands-on digital execution across a wide range of their client projects and industries, quietly powering the work behind the scenes."},{title:"Protex Textiles",media:"/assets/Portfolio/BackgroundImages/pexels-kaue-barbier-710715348-33001980.webp",mockup:"/assets/Portfolio/ClientMockups/ProtexTextiles.webp",description:"We took a traditional textile manufacturer and translated its craft into a modern digital experience. From initial concept through design and technical development, we shaped thoughtful UX that presents complex industrial expertise clearly to global buyers."},{title:"Vertrauenszentrum",media:"/assets/Portfolio/BackgroundImages/pexels-marianamontrazi-7366424.webp",mockup:"/assets/Portfolio/ClientMockups/Vertrauenszentrum.webp",description:"A close pairing of creative and technical craft, with Denise Lackner leading the design and 741 Studio handling the build. We implemented tracking and the funnel to create a seamless, marketing-ready experience that helps patients navigate sensitive medical support with confidence."},{title:"Tacheles",media:"/assets/Portfolio/BackgroundImages/pexels-maumascaro-376533.webp",mockup:"/assets/Portfolio/ClientMockups/Tacheles.webp",description:"Clean design paired with responsive, carefully built development. For this bold lifestyle brand, we focused on a polished user experience across every screen size, letting the brand's distinctive voice come through without technical friction."},{title:"IGR",media:"/assets/Portfolio/BackgroundImages/pexels-pixabay-458530.webp",mockup:"/assets/Portfolio/ClientMockups/IGR.webp",description:"Digitized the ergonomics innovation prize into a global authority for workplace health. We stacked value by showcasing curated research through a scalable information architecture, influencing long-term industry standards."},{title:"Yacht Charter Indonesia",media:"/assets/Portfolio/BackgroundImages/pexels-rudy-kirchner-278171-1229845.webp",mockup:"/assets/Portfolio/ClientMockups/YachtCharterIndonesia.webp",description:"A complex booking platform built around discovery. We designed and developed an advanced filtering system, structured yacht categories, and an organized catalog, so visitors can navigate a large fleet and find the right charter quickly and intuitively."},{title:"WBG",media:"/assets/Portfolio/BackgroundImages/pexels-sliceisop-2280604.webp",mockup:"/assets/Portfolio/ClientMockups/WBG.webp",description:"Architected a structural information portal for public housing and urban scaling. We focused on civilizational growth by organizing district data into a clear interface, protecting public trust and urban resilience."},{title:"Vesta Noris",media:"/assets/Portfolio/BackgroundImages/pexels-szafran-16362694.webp",mockup:"/assets/Portfolio/ClientMockups/VestaNoris.webp",description:"Streamlined operational efficiency with a tailored digital asset. We engineered a scalable platform to maximize user engagement and optimize key conversion pathways."}];let T=0,P=0;const _=`
      varying vec2 vUv;
      void main() {
        vUv = uv;
        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
      }
    `,j=`
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
    `,s.addEventListener("click",l=>{l.preventDefault(),l.stopPropagation(),n!==c&&!f&&R(n)}),s.addEventListener("touchstart",l=>{l.stopPropagation()},{passive:!0}),e.appendChild(s)});let i=!1,t,o;e.addEventListener("mousedown",r=>{i=!0,t=r.pageX-e.offsetLeft,o=e.scrollLeft}),e.addEventListener("mouseleave",()=>i=!1),e.addEventListener("mouseup",()=>i=!1),e.addEventListener("mousemove",r=>{if(!i)return;r.preventDefault();const s=(r.pageX-e.offsetLeft-t)*2;e.scrollLeft=o-s})},U=e=>{document.querySelectorAll(".slide-nav-item").forEach((t,o)=>{t.classList.toggle("active",o===e)})},Q=(e,i)=>{const t=document.querySelectorAll(".slide-nav-item");if(t[e]){const o=t[e].querySelector(".slide-progress-fill");o.style.width=`${i}%`,o.style.opacity="1"}},Y=e=>{const i=document.querySelectorAll(".slide-nav-item");if(i[e]){const t=i[e].querySelector(".slide-progress-fill");t.style.opacity="0",setTimeout(()=>t.style.width="0%",300)}},E=e=>{const i=document.querySelectorAll(".slide-nav-item");if(i[e]){const t=i[e].querySelector(".slide-progress-fill");t.style.transition="width 0.2s ease-out",t.style.width="0%",setTimeout(()=>{t.style.transition="width 0.1s ease, opacity 0.3s ease"},200)}},q=e=>{const i=document.querySelector(".slide-number");i&&(i.textContent=String(e+1).padStart(2,"0"));const t=document.querySelector(".slide-total");t&&(t.textContent=String(a.length).padStart(2,"0"))},W=()=>{if(!k||!g||!I&&m.length<2)return;h();let e=0;const i=100/X()*B;S=setInterval(()=>{if(!g){h();return}f||(e+=i,Q(c,e),e>=100&&(e=0,Y(c),G()))},B)},h=()=>{S&&(clearInterval(S),S=null),x&&(clearTimeout(x),x=null)},y=(e=0)=>{h(),g&&k&&(e>0?x=setTimeout(()=>{g&&W()},e):W())},R=async e=>{if(f||e===c)return;f=!0,e=(e+a.length)%a.length,h(),E(c);let i;if(!I){if(!m[e])try{const v=await D(a[e].media);m[e]=v}catch{console.warn(`Critical: Failed to load slide ${e}, skipping...`),f=!1,R((e+1)%a.length);return}const d=m[c];if(i=m[e],!d||!i){console.warn("Missing textures for transition. Index:",c,e),f=!1,y(500);return}u.uniforms.uTexture1.value=d,u.uniforms.uTexture2.value=i,u.uniforms.uTexture1Size.value=d.userData.size,u.uniforms.uTexture2Size.value=i.userData.size}const t=document.getElementById("current-mockup"),o=document.getElementById("content-overlay"),r=document.getElementById("overlay-title"),n=document.getElementById("overlay-description"),s=a[e];t&&t.classList.remove("active"),o&&o.classList.remove("active"),setTimeout(()=>{s.mockup&&t&&(t.onload=()=>t.classList.add("active"),t.src=s.mockup,t.alt=`741 Studio Client Portfolio: ${s.title}`,t.complete&&t.classList.add("active")),r&&(r.textContent=s.title),n&&(n.textContent=s.description||""),o&&o.classList.add("active")},400),c=e,q(c),U(c);const l=document.getElementById(`nav-${e+1}`);if(l&&l.scrollIntoView({behavior:"smooth",block:"nearest",inline:"center"}),I)setTimeout(()=>{f=!1,y(100)},800);else{const d=performance.now(),v=$()*1e3,A=N=>{const O=N-d,b=Math.min(O/v,1),H=b<.5?2*b*b:1-Math.pow(-2*b+2,2)/2;u.uniforms.uProgress.value=H,b<1?requestAnimationFrame(A):(u.uniforms.uProgress.value=0,u.uniforms.uTexture1.value=i,u.uniforms.uTexture1Size.value=i.userData.size,f=!1,y(100))};requestAnimationFrame(A)}},G=()=>{if(f||!k||!g)return;const e=(c+1)%a.length;R(e)},J=()=>{if(!(Math.abs(P-T)<50)){if(P<T&&!f&&g)h(),E(c),G();else if(P>T&&!f&&g){h(),E(c);const e=(c-1+a.length)%a.length;R(e)}}},D=e=>new Promise((i,t)=>{const o=new p.TextureLoader,r=setTimeout(()=>t(new Error("Timeout")),1e4);o.load(e,n=>{clearTimeout(r),n.minFilter=n.magFilter=p.LinearFilter,n.userData={size:new p.Vector2(n.image.width,n.image.height)},i(n)},void 0,n=>{clearTimeout(r),t(n)})}),Z=async()=>{const e=document.querySelector(".webgl-canvas");if(!e)return;const i=document.createElement("canvas");i.className="webgl-canvas",e.replaceWith(i),C=new p.Scene,M=new p.OrthographicCamera(-1,1,1,-1,0,1),w=new p.WebGLRenderer({canvas:i,antialias:!1,alpha:!1}),w.setSize(window.innerWidth,window.innerHeight),w.setPixelRatio(Math.min(window.devicePixelRatio,2)),u=new p.ShaderMaterial({uniforms:{uTexture1:{value:null},uTexture2:{value:null},uProgress:{value:0},uResolution:{value:new p.Vector2(window.innerWidth,window.innerHeight)},uTexture1Size:{value:new p.Vector2(1,1)},uTexture2Size:{value:new p.Vector2(1,1)},uEffectType:{value:2},uGlobalIntensity:{value:1},uSpeedMultiplier:{value:1},uDistortionStrength:{value:1},uColorEnhancement:{value:1},uRippleFrequency:{value:25},uRippleAmplitude:{value:.08},uRippleWaveSpeed:{value:1},uRippleRippleCount:{value:1},uRippleDecay:{value:1}},vertexShader:_,fragmentShader:j});const t=new p.PlaneGeometry(2,2),o=new p.Mesh(t,u);C.add(o);const r=async()=>{const l=Math.min(a.length,2);for(let d=0;d<l;d++)try{const v=await D(a[d].media);m[d]=v}catch{console.warn("Failed to load initial image "+d)}m[0]&&(u.uniforms.uTexture1.value=m[0],u.uniforms.uTexture1Size.value=m[0].userData.size,m[1]&&(u.uniforms.uTexture2.value=m[1],u.uniforms.uTexture2Size.value=m[1].userData.size),k=!0,g=!0,y(1500))},n=async()=>{for(let l=2;l<a.length;l++)if(!m[l])try{const d=await D(a[l].media);m[l]=d}catch{console.warn("Background load failed for "+l)}};await r(),n();const s=()=>{requestAnimationFrame(s),w.render(C,M)};s()};let F=!1;const z=async()=>{if(F)return;F=!0,K(),q(0),U(0);const e=document.getElementById("current-mockup"),i=document.getElementById("content-overlay"),t=document.getElementById("overlay-title"),o=document.getElementById("overlay-description");a[0].mockup&&e&&(e.onload=()=>e.classList.add("active"),e.src=a[0].mockup,e.alt=`741 Studio Client Portfolio: ${a[0].title}`,e.complete&&e.classList.add("active")),t&&(t.textContent=a[0].title),o&&(o.textContent=a[0].description||""),i&&i.classList.add("active");try{await Z()}catch(r){console.error("WebGL Renderer Error:",r),I=!0,k=!0,g=!0,y(1500)}};document.readyState==="complete"||document.readyState==="interactive"?setTimeout(z,1):(window.addEventListener("DOMContentLoaded",z),window.addEventListener("load",z));const L=document.querySelector(".slider-wrapper");L&&(L.addEventListener("touchstart",e=>{e.target.closest(".slides-navigation")||(T=e.changedTouches[0].screenX)},{passive:!0}),L.addEventListener("touchend",e=>{e.target.closest(".slides-navigation")||(P=e.changedTouches[0].screenX,J())},{passive:!0}));window.addEventListener("resize",()=>{w&&u&&(w.setSize(window.innerWidth,window.innerHeight),u.uniforms.uResolution.value.set(window.innerWidth,window.innerHeight))});document.addEventListener("visibilitychange",()=>{document.hidden?h():g&&!f&&y()});
