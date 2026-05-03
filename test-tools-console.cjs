const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err.message));
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  await new Promise(r => setTimeout(r, 2000));
  
  await page.evaluate(() => {
    const slides = Array.from(document.querySelectorAll('.splide.tool-tags .splide__slide'));
    const describerSlide = slides.find(s => !s.classList.contains('splide__slide--clone') && s.innerText.includes('Describer'));
    if (describerSlide) describerSlide.click();
  });
  
  await new Promise(r => setTimeout(r, 1000));
  
  await browser.close();
})();
