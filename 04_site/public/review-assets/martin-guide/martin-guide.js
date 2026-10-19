/* 741 Martin guide: reveal each callout once when it enters the view. No dependencies. */
(function(){var els=document.querySelectorAll('.mg[data-reveal]');if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('is-in')});return}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('is-in');io.unobserve(e.target)}})},{threshold:.35});
els.forEach(function(e){io.observe(e)})})();
