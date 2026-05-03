const puppeteer = require('puppeteer');

(async () => {
  let errors = [];
  try {
    const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
    const page = await browser.newPage();
    
    // Set viewport to mobile 390px width
    await page.setViewport({ width: 390, height: 844 });
    
    page.on('console', msg => {
      if (msg.type() === 'error' || msg.type() === 'warning') {
        const text = msg.text();
        if (text.includes('favicon') || text.includes('CORS') || text.includes('Multiple instances of Three.js') || text.includes('WebGL') || text.includes('GL Driver Message')) return;
        console.log('CONSOLE ISSUE:', text);
        if (msg.type() === 'error') errors.push(text);
      }
    });
    page.on('pageerror', err => {
      console.log('PAGE ERROR:', err.toString());
      errors.push(err.toString());
    });
    
    console.log('Loading page...');
    await page.goto('http://localhost:3000/pages/portfolio_full.html', { waitUntil: 'networkidle0' });
    
    // Helper to get state
    const getState = async () => {
      return await page.evaluate(() => {
        const activeNav = document.querySelector('.slide-nav-item.active');
        const activeTitle = document.querySelector('#overlay-title').innerText;
        const currentSlideIndex = window.currentSlideIndex !== undefined ? window.currentSlideIndex : -1;
        return {
          navId: activeNav ? activeNav.id : null,
          title: activeTitle,
          index: currentSlideIndex
        };
      });
    };

    console.log('--- 1. Initial State Sync ---');
    await new Promise(r => setTimeout(r, 2000));
    let state = await getState();
    console.log('Initial State:', state);

    console.log('--- 2. Autoplay Stress (Wait 10s) ---');
    await new Promise(r => setTimeout(r, 10000));
    state = await getState();
    console.log('State after 10s:', state);

    console.log('--- 3. Rapid Interaction ---');
    // Rapidly click pills
    for (let i = 2; i <= 6; i++) {
      await page.click(`#nav-${i}`);
      await new Promise(r => setTimeout(r, 200)); // Click every 200ms
    }
    
    // Wait for transition to settle
    await new Promise(r => setTimeout(r, 3000));
    state = await getState();
    console.log('State after rapid clicks:', state);

    console.log('--- 4. Edge Case: Interrupt Autoplay ---');
    // Wait a bit, then click to interrupt
    await new Promise(r => setTimeout(r, 2000));
    await page.click('#nav-1');
    console.log('Clicked Nav 1');
    await new Promise(r => setTimeout(r, 3000)); // Wait for transition
    state = await getState();
    console.log('State after interrupt:', state);

    console.log('--- 5. Autoplay Resumes? ---');
    // Wait 5s to see if it auto slides to nav-2
    await new Promise(r => setTimeout(r, 5000));
    state = await getState();
    console.log('State after resuming autoplay:', state);
    
    await browser.close();
    
    console.log('--- TEST COMPLETE ---');
    if (errors.length > 0) {
      console.log('ERRORS DETECTED:', errors);
      process.exit(1);
    } else {
      console.log('No critical errors found.');
    }
  } catch (err) {
    console.error('TEST FRAMEWORK ERROR:', err);
    process.exit(1);
  }
})();
