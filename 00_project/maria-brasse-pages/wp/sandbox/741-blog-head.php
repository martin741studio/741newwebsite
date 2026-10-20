<?php
/** 741: H1 + Intro auf der Beitragsübersicht (page_for_posts). Lives in wp-content/novamira-sandbox/. */
add_action('generate_before_main_content', function(){
	if ( ! is_home() ) return;
	echo '<div class="sg-blog-head"><h1>Erfolge aus echten Projekten – Feng-Shui-Fallstudien</h1><p>Was passiert, wenn Räume wieder arbeiten? Fünf Projekte von Maria Brasse (ShuiGuru) aus Berlin, Brandenburg und der Eifel: Arztpraxis, Laden, Werkstatt, Kosmetik-Institut und Esoterik-Shop – jeweils mit Ausgangslage, Eingriff und dem, was sich danach verändert hat.</p></div>';
});
