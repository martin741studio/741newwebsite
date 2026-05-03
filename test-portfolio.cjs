const puppeteer = require('puppeteer');

(async () => {
  try {
    const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
    const page = await browser.newPage();
    
    page.on('console', msg => console.log('PAGE LOG:', msg.text()));
    page.on('pageerror', err => console.log('PAGE ERROR:', err.toString()));
    
    await page.goto('http://localhost:3000/pages/portfolio_full.html', { waitUntil: 'networkidle0' });
    
    // Wait for auto transition
    await new Promise(r => setTimeout(r, 6000));
    
    await browser.close();
    console.log('DONE');
  } catch (err) {
    console.error('TEST ERROR', err);
  }
})();
