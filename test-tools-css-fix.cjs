const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  // Apply a fix
  await page.evaluate(() => {
    const style = document.createElement('style');
    style.innerHTML = `
      .is-mobile-tools-slider .slider-pill_photo {
        position: absolute !important;
        inset: 0 !important;
        width: 100% !important;
        height: 100% !important;
        max-height: 100% !important;
        object-fit: cover !important;
      }
    `;
    document.head.appendChild(style);
  });
  
  await new Promise(r => setTimeout(r, 2000));
  
  const imgState = await page.evaluate(() => {
    const activeSlide = document.querySelector('.splide.tools-image .is-active');
    const img = activeSlide.querySelector('img');
    const rect = img ? img.getBoundingClientRect() : null;
    return {
      width: rect ? rect.width : null,
      height: rect ? rect.height : null,
    };
  });
  
  console.log('Active Image State After Fix:', imgState);
  await browser.close();
})();
