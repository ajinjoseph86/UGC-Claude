const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1280,height:720}});
  await p.goto('file://' + process.cwd() + '/ui.html');
  const T = "help me build a birthday reminder app please.. use less credits... for free.";
  const fps=24, N=96, t0=0.35, t1=3.35;
  const times=[];
  for (let f=0; f<N; f++) {
    const t=f/fps; let n = t<t0?0: Math.min(T.length, Math.floor((t-t0)/(t1-t0)*T.length));
    const blink = (n<T.length) || (Math.floor(t*2)%2===0);
    await p.evaluate(([txt,blink,full])=>{
      const bx=document.getElementById('b');
      bx.innerHTML = (txt.length? txt.replace(/&/g,'&amp;').replace(/</g,'&lt;') : '<span class="ph">Message…</span>') + (blink?'<span class="cur"></span>':'');
      document.getElementById('s').className = 'send'+(txt.length?' on':'');
    }, [T.slice(0,n), blink, n===T.length]);
    await p.screenshot({path:`f_${String(f).padStart(3,'0')}.png`});
  }
  await b.close();
})();
