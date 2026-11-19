const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1280,height:720}});
  await p.goto('file://' + process.cwd() + '/ui.html');
  // confetti pieces
  await p.evaluate(()=>{const c=document.getElementById('conf');const cols=['#ffcf5a','#4c7dff','#ff6b9a','#5ee0a0','#ffffff'];
    for(let i=0;i<70;i++){const d=document.createElement('div');d.className='conf';d.style.background=cols[i%5];
      d.dataset.x=(Math.random()*1280);d.dataset.vy=(120+Math.random()*220);d.dataset.r=Math.random()*360;d.dataset.vr=(Math.random()-.5)*600;d.dataset.y0=-40-Math.random()*300;c.appendChild(d);}});
  const fps=24,N=96;
  for(let f=0;f<N;f++){const t=f/fps;
    await p.evaluate((t)=>{
      // pop-in with overshoot starting at 0.25s
      const s=t<0.25?0:Math.min(1,(t-0.25)/0.35); const e=s<1? (1-Math.pow(1-s,3))*1.08 - 0.08*Math.sin(s*Math.PI) : 1;
      const k=t<0.25?0: (s<1? e : 1);
      const c=document.getElementById('c'); c.style.transform=`scale(${k})`; c.style.opacity=t<0.25?0:Math.min(1,(t-0.25)/0.15);
      // confetti falls after pop (dies down — small celebration)
      document.querySelectorAll('.conf').forEach(d=>{const tt=Math.max(0,t-0.3);
        d.style.left=d.dataset.x+'px'; d.style.top=(+d.dataset.y0 + d.dataset.vy*tt)+'px';
        d.style.transform=`rotate(${+d.dataset.r + d.dataset.vr*tt}deg)`; d.style.opacity=t<0.3?0:Math.max(0,1-tt/2.6);});
      // timer: ticks at 1s/1s, ominous
      const sec=59-Math.floor(Math.max(0,t-0.6)); document.getElementById('tm').textContent='Expires in 00:59:'+String(sec).padStart(2,'0');
    },t);
    await p.screenshot({path:`f_${String(f).padStart(3,'0')}.png`});}
  await b.close();})();
