<?php
/**
 * Plugin Name: ShuiGuru Consent & Analytics (741)
 * Description: Cookie-Banner (Opt-in), Google Consent Mode v2, GA4 G-8B0M7DXENR (lädt erst nach Einwilligung) und Conversion-Events.
 * Author: 741 Studio
 * Version: 1.0.0
 */
if (!defined('ABSPATH')) exit;

const SG_GA4_ID = 'G-8B0M7DXENR';

add_action('wp_head', function () {
    if (is_admin()) return; ?>
<!--noptimize--><script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',functionality_storage:'granted',security_storage:'granted',wait_for_update:500});
(function(){
  var ID='<?php echo esc_js(SG_GA4_ID); ?>';
  window.sgLoadGA=function(){
    if(window.sgGALoaded) return; window.sgGALoaded=true;
    gtag('consent','update',{analytics_storage:'granted'});
    var s=document.createElement('script'); s.async=true; s.src='https://www.googletagmanager.com/gtag/js?id='+ID; document.head.appendChild(s);
    gtag('js',new Date()); gtag('config',ID,{allow_google_signals:false,allow_ad_personalization_signals:false});
  };
  try{ if(localStorage.getItem('sg_consent')==='granted'){ window.sgLoadGA(); } }catch(e){}
})();
</script><!--/noptimize-->
<?php }, 1);

add_action('wp_footer', function () {
    if (is_admin()) return;
    $privacy = esc_url(home_url('/datenschutz/')); ?>
<!--noptimize--><div id="sg-consent" role="dialog" aria-live="polite" aria-label="Cookie-Einstellungen" hidden>
  <div class="sg-c-inner">
    <p class="sg-c-text"><strong>Ihre Privatsphäre</strong><br>Ich nutze Google Analytics, um zu verstehen, wie Besucher meine Website nutzen, und sie zu verbessern. Das geschieht nur mit Ihrer Einwilligung. Sie können Ihre Auswahl jederzeit über „Cookie-Einstellungen“ im Seitenfuß ändern. Mehr in der <a href="<?php echo $privacy; ?>">Datenschutzerklärung</a>.</p>
    <div class="sg-c-btns">
      <button type="button" class="sg-c-btn" data-sg-consent="denied">Nur notwendige</button>
      <button type="button" class="sg-c-btn" data-sg-consent="granted">Alle akzeptieren</button>
    </div>
  </div>
</div>
<style>
#sg-consent{position:fixed;left:16px;right:16px;bottom:16px;z-index:99999;display:flex;justify-content:center}
#sg-consent[hidden]{display:none}
#sg-consent .sg-c-inner{max-width:980px;width:100%;background:#fff;border-top:4px solid #10595B;box-shadow:0 10px 40px rgba(0,0,0,.18);padding:20px 24px;display:flex;gap:20px;align-items:center;flex-wrap:wrap;font-size:15px;line-height:1.55;color:#222}
#sg-consent .sg-c-text{flex:1 1 420px;margin:0}
#sg-consent .sg-c-text a{color:#10595B;text-decoration:underline}
#sg-consent .sg-c-btns{display:flex;gap:10px;flex-wrap:wrap}
#sg-consent .sg-c-btn{background:#10595B;color:#fff;border:0;border-radius:0;padding:12px 22px;font-weight:600;cursor:pointer;font-size:15px}
#sg-consent .sg-c-btn:hover{background:#0b3a3b}
</style>
<script>
(function(){
  var box=document.getElementById('sg-consent'); if(!box) return;
  var stored=null; try{stored=localStorage.getItem('sg_consent');}catch(e){}
  if(!stored){ box.hidden=false; }
  box.addEventListener('click',function(e){
    var b=e.target.closest('[data-sg-consent]'); if(!b) return;
    var v=b.getAttribute('data-sg-consent');
    try{localStorage.setItem('sg_consent',v);}catch(e){}
    box.hidden=true;
    if(v==='granted'){ window.sgLoadGA&&window.sgLoadGA(); }
    else { gtag('consent','update',{analytics_storage:'denied'}); if(window.sgGALoaded){ location.reload(); } }
  });
  document.addEventListener('click',function(e){
    var a=e.target.closest('a'); if(!a) return;
    var href=a.getAttribute('href')||'';
    if(href.indexOf('#cookie-einstellungen')!==-1){ e.preventDefault(); box.hidden=false; return; }
    if(href.indexOf('tel:')===0){ gtag('event','click_phone',{link_url:href}); }
    else if(href.indexOf('mailto:')===0){ gtag('event','click_email',{link_url:href}); }
    else if(href.indexOf('/kaeffchen')!==-1){ gtag('event','click_cta_kaeffchen',{link_text:(a.textContent||'').trim().slice(0,80),page_path:location.pathname}); }
  });
  var sgLeadAt=0; function lead(formId){ var n=Date.now(); if(n-sgLeadAt<3000) return; sgLeadAt=n; gtag('event','generate_lead',{form_id:String(formId||''),form_name:'Kontaktformular',page_path:location.pathname}); }
  if(window.jQuery){ jQuery(document).on('wpformsAjaxSubmitSuccess',function(ev,res){ lead(ev&&ev.target&&ev.target.getAttribute&&ev.target.getAttribute('data-formid')); }); }
  document.addEventListener('wpformsAjaxSubmitSuccess',function(ev){ lead(ev&&ev.target&&ev.target.getAttribute&&ev.target.getAttribute('data-formid')); });
})();
</script><!--/noptimize-->
<?php }, 100);
