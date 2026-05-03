const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
  
  await new Promise(r => setTimeout(r, 2000));
  
  // Scroll to trigger any reveals
  await page.evaluate(() => {
    document.querySelector('.hero-draggbles-comp').scrollIntoView();
  });
  
  await new Promise(r => setTimeout(r, 1000));
  
  const tagsLayout = await page.evaluate(() => {
    const nodes = [1, 2, 3, 4, 5, 6].map(n => document.querySelector(`#node${n}`));
    
    return nodes.map((node, i) => {
      if (!node) return { node: i+1, status: 'missing' };
      if (window.getComputedStyle(node).display === 'none') return { node: i+1, status: 'hidden' };
      
      const label = node.querySelector('.hr-node-label');
      if (!label) return { node: i+1, status: 'no-label' };
      
      // Get the main visual element (image or model or video container)
      let media = node.querySelector('img') || node.querySelector('model-viewer') || node.querySelector('.hero-video');
      
      if (!media) return { node: i+1, status: 'no-media' };
      
      const nodeRect = node.getBoundingClientRect();
      const labelRect = label.getBoundingClientRect();
      const mediaRect = media.getBoundingClientRect();
      
      return {
        node: `node${i+1}`,
        labelTop: labelRect.top,
        mediaTop: mediaRect.top,
        distanceFromMediaTop: mediaRect.top - labelRect.bottom,
        distanceFromNodeTop: labelRect.top - nodeRect.top,
        text: label.innerText
      };
    });
  });
  
  console.log('Desktop Tags Visual Layout:');
  console.table(tagsLayout);
  
  await browser.close();
})();
