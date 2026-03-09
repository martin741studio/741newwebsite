const https = require('https');

https.get('https://weavy.ai/', (res) => {
  let data = '';
  res.on('data', (chunk) => {
    data += chunk;
  });
  res.on('end', () => {
    const urls = data.match(/https:\/\/assets\.weavy\.ai\/[^"'\s]+/g);
    if (urls) {
      console.log([...new Set(urls)].join('\n'));
    }
  });
}).on('error', (err) => {
  console.error(err);
});
