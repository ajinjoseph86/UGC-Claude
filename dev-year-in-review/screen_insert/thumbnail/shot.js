const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const [w,h,name] of [[1920,1080,'thumb_16x9.png'],[1080,1920,'thumb_9x16.png']]) {
    const p = await b.newPage({viewport:{width:w,height:h}});
    await p.goto('file://' + process.cwd() + `/thumb.html?w=${w}&h=${h}`, {waitUntil:'networkidle'}).catch(()=>{});
    await p.evaluate(() => document.fonts.ready);
    console.log(name, await p.evaluate(() => document.fonts.check('100px Anton')));
    await p.screenshot({path:name});
  }
  await b.close();
})();
