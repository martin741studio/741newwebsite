async function run() {
  const res = await fetch('https://weavy.ai/');
  const data = await res.text();
  const urls = data.match(/https:\/\/[^"'\s<>]+/g);
  if (urls) {
    console.log([...new Set(urls)].filter(u => u.includes('cdn.prod.website-files.com')).join('\n'));
  }
}
run();
