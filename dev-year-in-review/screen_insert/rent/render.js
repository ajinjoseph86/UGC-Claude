const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1280,height:720}});
  await p.goto('file://' + process.cwd() + '/ui.html');
  const T = "build an app that pays my rent\ni have no money\nuse less credits...\ni believe in u... \u2665";
  const fps=24, N=96, t0=0.35, t1=3.35;
  for (let f=0; f<N; f++) {
    const t=f/fps; let n = t<t0?0: Math.min(T.length, Math.floor((t-t0)/(t1-t0)*T.length));
    const blink = (n<T.length) || (Math.floor(t*2)%2===0);
    await p.evaluate(([txt,blink])=>{
      const bx=document.getElementById('b');
      const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
      bx.innerHTML = (txt.length? esc(txt).replace('\u2665','<span style="color:#ff4d6d;text-shadow:0 0 12px rgba(255,77,109,.7);font-size:30px">\u2665</span>') : '<span class="ph">Message…</span>') + (blink?'<span class="cur"></span>':'');
      document.getElementById('s').className = 'send'+(txt.length?' on':'');
    }, [T.slice(0,n), blink]);
    await p.screenshot({path:`f_${String(f).padStart(3,'0')}.png`});
  }
  await b.close();
})();
