(function(){
var shot=/[?&]shot=1/.test(location.search);if(shot)document.body.classList.add('shot');
var hd=document.getElementById('hd');addEventListener('scroll',function(){hd.classList.toggle('sc',scrollY>8)},{passive:true});
var els=[].slice.call(document.querySelectorAll('.rv,.rv-l,.rv-r'));
function show(e,d){setTimeout(function(){e.classList.add('in')},d||0)}
var hero=document.getElementById('s01');
[].slice.call(hero.querySelectorAll('.rv')).forEach(function(e,i){show(e,shot?0:90*i)});
if(shot||!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('in')});document.querySelector('.steps').classList.add('in');return}
var io=new IntersectionObserver(function(es){es.forEach(function(en){if(!en.isIntersecting)return;var e=en.target;var sib=[].slice.call(e.parentNode.children).filter(function(x){return x.classList.contains('rv')});var k=Math.max(0,sib.indexOf(e));show(e,k*90);io.unobserve(e)})},{threshold:.2});
els.filter(function(e){return !hero.contains(e)}).forEach(function(e){io.observe(e)});
var st=document.querySelector('.steps');var io2=new IntersectionObserver(function(es){if(es[0].isIntersecting){st.classList.add('in');io2.disconnect()}},{threshold:.4});io2.observe(st);
[].slice.call(document.querySelectorAll('.acc-grid')).forEach(function(g){var ds=[].slice.call(g.querySelectorAll('details'));ds.forEach(function(d){d.addEventListener('toggle',function(){if(d.open)ds.forEach(function(o){if(o!==d)o.open=false})})})});
document.addEventListener('click',function(e){var a=e.target.closest('a.btn');if(a&&window.dataLayer)dataLayer.push({event:'booking_click',section:a.dataset.section})});
})();
