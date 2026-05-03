const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  const labels = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('.hr-node-label')).map(el => {
      const bold = el.querySelector('.bold-txt');
      const light = el.querySelector('.light-txt');
      const style = window.getComputedStyle(el);
      return {
        text: `${bold ? bold.textContent : ''} ${light ? light.textContent : ''}`,
        top: style.top,
        fontSize: style.fontSize,
        boldColor: bold ? window.getComputedStyle(bold).color : null,
        boldMargin: bold ? window.getComputedStyle(bold).marginRight : null,
        lightColor: light ? window.getComputedStyle(light).color : null
      };
    });
  });
  
  console.log('Labels count:', labels.length);
  console.log('Sample label:', labels[0]);
  await browser.close();
})();
