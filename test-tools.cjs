const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  await new Promise(r => setTimeout(r, 2000));
  
  // Get initial state
  const state1 = await page.evaluate(() => {
    const activeImage = document.querySelector('.splide.tools-image .is-active img');
    const activeTag = document.querySelector('.splide.tool-tags .is-active .slide_super-chip');
    return {
      imageSrc: activeImage ? activeImage.src : null,
      tagText: activeTag ? activeTag.innerText : null
    };
  });
  
  console.log('Initial state:', state1);
  
  // Click the next tag
  await page.evaluate(() => {
    const nextTag = document.querySelectorAll('.splide.tool-tags .splide__slide')[1]; // index 1
    nextTag.click();
  });
  
  await new Promise(r => setTimeout(r, 1000));
  
  const state2 = await page.evaluate(() => {
    const activeImage = document.querySelector('.splide.tools-image .is-active img');
    const activeTag = document.querySelector('.splide.tool-tags .is-active .slide_super-chip');
    return {
      imageSrc: activeImage ? activeImage.src : null,
      tagText: activeTag ? activeTag.innerText : null
    };
  });
  
  console.log('State after click:', state2);
  await browser.close();
})();
