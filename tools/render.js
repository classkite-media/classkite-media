const { chromium } = require('playwright');
const fs=require('fs');
(async()=>{
  const [,,html,outdir,mode]=process.argv;
  const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1920}});
  await p.goto('file://'+html); await p.waitForTimeout(500);
  const dur=await p.evaluate(()=>window.DUR);
  fs.mkdirSync(outdir,{recursive:true});
  const times = mode==='preview' ? JSON.parse(process.argv[5]) : Array.from({length:Math.round(dur*30)},(_,i)=>i/30);
  for(let i=0;i<times.length;i++){ await p.evaluate(t=>render(t),times[i]); await p.screenshot({path:`${outdir}/f${String(i).padStart(4,'0')}.png`}); }
  await b.close();
})();
