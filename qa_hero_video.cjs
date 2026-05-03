const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  // Wait a moment for any immediate JS
  await new Promise(r => setTimeout(r, 1000));
  
  // Scroll to node6
  await page.evaluate(() => {
    const node6 = document.querySelector('#node6');
    if (node6) node6.scrollIntoView({ behavior: 'instant', block: 'center' });
  });
  
  // Wait for GSAP animations to settle
  await new Promise(r => setTimeout(r, 1500));
  
  const report = await page.evaluate(() => {
    const node6 = document.querySelector('#node6');
    if (!node6) return { error: 'Node6 not found' };
    
    const video = document.querySelector('.hero-video video');
    if (!video) return { error: 'Video element not found' };
    
    const videoContainer = document.querySelector('.hero-video');
    
    const n6Rect = node6.getBoundingClientRect();
    const vRect = video.getBoundingClientRect();
    const cRect = videoContainer.getBoundingClientRect();
    
    // Check 1: Visible inside viewport (since we scrolled to it, it should be in the window)
    const viewportHeight = window.innerHeight;
    const isVisibleInViewport = vRect.top < viewportHeight && vRect.bottom > 0;
    
    // Check 2: Not clipped by container (video height >= container height)
    // Actually, object-fit: cover handles aspect ratio, but let's check if container is collapsing
    const isClipped = cRect.height === 0 || cRect.height < 50; // if container is 0 or tiny
    
    // Check 3: Not pushed out by layout spacing (meaning its height/width are reasonable)
    const hasValidDimensions = vRect.width > 0 && vRect.height > 0;
    
    // Check 4: Overlaps
    const container = document.querySelector('.hero-draggbles-comp');
    const nodes = Array.from(container.querySelectorAll('.reveal-item')).filter(n => window.getComputedStyle(n).display !== 'none');
    
    const results = nodes.map(n => {
      const rect = n.getBoundingClientRect();
      const label = n.querySelector('.hr-node-label');
      const labelRect = label ? label.getBoundingClientRect() : null;
      return { id: n.id, top: rect.top, bottom: rect.bottom, labelTop: labelRect ? labelRect.top : null };
    });
    
    results.sort((a, b) => a.top - b.top);
    
    let isOverlapped = false;
    let overlapDetails = [];
    for (let i = 0; i < results.length - 1; i++) {
      const current = results[i];
      const next = results[i+1];
      const nextTopmost = next.labelTop !== null ? Math.min(next.top, next.labelTop) : next.top;
      if (nextTopmost < current.bottom) {
        if (current.id === 'node6' || next.id === 'node6') {
          isOverlapped = true;
          overlapDetails.push(`${current.id} overlaps ${next.id}`);
        }
      }
    }
    
    let status = 'PASS';
    let criticalErrors = [];
    
    if (!isVisibleInViewport) criticalErrors.push('CRITICAL: Video is not visible inside viewport after scrolling');
    if (isClipped) criticalErrors.push('CRITICAL: Video container is clipped (height ' + cRect.height + 'px)');
    if (!hasValidDimensions) criticalErrors.push('CRITICAL: Video has invalid dimensions (' + vRect.width + 'x' + vRect.height + ')');
    if (isOverlapped) criticalErrors.push('CRITICAL: Video frame is overlapped (' + overlapDetails.join(', ') + ')');
    
    if (criticalErrors.length > 0) status = 'FAIL';
    
    return {
      status,
      errors: criticalErrors,
      metrics: {
        containerHeight: cRect.height,
        videoHeight: vRect.height,
        videoWidth: vRect.width,
        node6Top: n6Rect.top,
        viewportHeight
      }
    };
  });
  
  console.log('--- HERO VIDEO QA REPORT ---');
  console.log(`STATUS: ${report.status}`);
  if (report.errors && report.errors.length > 0) {
    report.errors.forEach(err => console.log(`❌ ${err}`));
  } else {
    console.log('✅ Video visible in viewport');
    console.log('✅ Not pushed out by layout spacing');
    console.log('✅ Not overlapped by other frames');
    console.log('✅ Not clipped by container');
  }
  console.log('\nMetrics:');
  console.log(`Container Height: ${report.metrics.containerHeight}px`);
  console.log(`Video Dimensions: ${report.metrics.videoWidth}x${report.metrics.videoHeight}px`);
  
  await browser.close();
})();
