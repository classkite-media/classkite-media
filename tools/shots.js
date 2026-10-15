const { chromium } = require('playwright');
(async()=>{const [,,html,out]=process.argv;const b=await chromium.launch();const p=await b.newPage({viewport:{width:1300,height:1200}});
await p.goto('file://'+html);await p.waitForTimeout(400);
const names={img1:'post-1-pdf-to-live-lesson',img2:'post-2-live-student-grid',img3:'post-3-ai-expected-vs-actual',img4:'post-4-practice-at-home',img5:'post-5-quiz-question'};
for(const [id,n] of Object.entries(names)){await p.locator('#'+id).screenshot({path:`${out}/${n}.png`});}
await b.close();})();
