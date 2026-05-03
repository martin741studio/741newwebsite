const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  await new Promise(r => setTimeout(r, 2000));
  
  const imgState = await page.evaluate(() => {
    const activeSlide = document.querySelector('.splide.tools-image .is-active');
    if (!activeSlide) return 'No active slide';
    const img = activeSlide.querySelector('img');
    const rect = img ? img.getBoundingClientRect() : null;
    return {
      imgSrc: img ? img.src : null,
      width: rect ? rect.width : null,
      height: rect ? rect.height : null,
      opacity: window.getComputedStyle(activeSlide).opacity
    };
  });
  
  console.log('Active Image State:', imgState);
  await browser.close();
})();
