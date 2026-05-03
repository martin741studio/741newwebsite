const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  // Wait for initial load
  await new Promise(r => setTimeout(r, 2000));
  
  // Scroll to tools
  await page.evaluate(() => {
    const el = document.querySelector('.section_prof-tools-mobile');
    if (el) el.scrollIntoView();
  });
  
  await new Promise(r => setTimeout(r, 1000));
  
  await page.screenshot({ path: 'tools_before.png', fullPage: true });
  
  // Try clicking the chip that says "Describer" (which should be logical index 1)
  await page.evaluate(() => {
    const slides = Array.from(document.querySelectorAll('.splide.tool-tags .splide__slide'));
    const describerSlide = slides.find(s => !s.classList.contains('splide__slide--clone') && s.innerText.includes('Describer'));
    if (describerSlide) describerSlide.click();
  });
  
  await new Promise(r => setTimeout(r, 1000));
  await page.screenshot({ path: 'tools_after.png', fullPage: true });
  
  await browser.close();
  console.log('Screenshots saved.');
})();
