<?php
/**
 * 741 Studio — simple 301 redirect map for renamed/removed slugs.
 * Lives in wp-content/novamira-sandbox/ (Novamira loads enabled sandbox PHP; mu-plugins/ + .htaccess are write-protected for the agent).
 */
add_action( 'template_redirect', function () {
	$path = untrailingslashit( parse_url( $_SERVER['REQUEST_URI'], PHP_URL_PATH ) );
	$map = array(
		'/hi' => '/ueber-mich-maria-brasse/',
	);
	if ( isset( $map[ $path ] ) ) {
		wp_safe_redirect( home_url( $map[ $path ] ), 301 );
		exit;
	}
}, 1 );
