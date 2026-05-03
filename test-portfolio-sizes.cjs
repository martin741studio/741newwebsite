const puppeteer = require('puppeteer');

const runTest = async (width, height, name) => {
  let errors = [];
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width, height });
  
  console.log(`\n--- Testing ${name} (${width}x${height}) ---`);
  await page.goto('http://localhost:3000/pages/portfolio_full.html', { waitUntil: 'domcontentloaded' });
  
  const getState = async () => {
    return await page.evaluate(() => {
      const activeNav = document.querySelector('.slide-nav-item.active');
      const activeTitle = document.querySelector('#overlay-title').innerText;
      return {
        navId: activeNav ? activeNav.id : null,
        title: activeTitle,
      };
    });
  };

  // Wait 4s for first autoplay transition
  await new Promise(r => setTimeout(r, 4000));
  let state = await getState();
  console.log(`State after 4s (autoplay):`, state);

  // Click nav-5 using JS to bypass scroll/mask-image issues
  await page.evaluate(() => document.getElementById('nav-5').click());
  await new Promise(r => setTimeout(r, 3000));
  state = await getState();
  console.log(`State after clicking nav-5:`, state);

  await browser.close();
};

(async () => {
  await runTest(360, 740, 'Mobile Small');
  await runTest(1920, 1080, 'Desktop');
  console.log('\nALL TESTS COMPLETE');
})();
