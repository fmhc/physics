import http.server,functools,threading,json,pathlib,socket,time,math,statistics,hashlib
from playwright.sync_api import sync_playwright
root=pathlib.Path(__file__).resolve().parent
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(root)))
threading.Thread(target=server.serve_forever,daemon=True).start();start=time.monotonic()
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/home/fmh/.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell',args=['--no-sandbox','--disable-gpu'])
 page=browser.new_page();page.goto(f'http://127.0.0.1:{server.server_port}/')
 result=page.evaluate('''async()=>{
 const {DetectorSimulation,gradientCheck}=await import('./detector.js');
 const profile=await(await fetch('./profile.json')).json(),rows=[],start=performance.now();
 const gradient=gradientCheck(profile);if(!gradient.pass)throw Error('gradient check failed '+JSON.stringify(gradient));
 for(const h of [.2,.1])for(const [epsilon,alpha,ratio] of [[.005,0,1],[.005,.1,1],[.005,1,1],[.005,1,1.3],[0,1,1]]){
 const sim=new DetectorSimulation({profile,h,epsilon,alpha,ratio,R:80,linear:false,absorber:true});
 const first=sim.sample(),initialD=sim.detector(),initialTotal=first.energy+initialD.D,trace=[];
 let maxE=0,maxQ=0,maxAbsE=0,maxK=0,maxD=0;
 while(sim.t<100-1e-8){
 if(performance.now()-start>45000)throw Error('active JS budget exceeded');
 sim.step(5);const s=sim.sample(),d=sim.detector();if(!s.finite||!Object.values(d).every(Number.isFinite))throw Error('nonfinite');
 const error=Math.abs(s.energy+d.D+s.absorbedEnergy-initialTotal);
 maxAbsE=Math.max(maxAbsE,error);maxE=Math.max(maxE,error/initialTotal);
 maxQ=Math.max(maxQ,Math.abs((s.charge+s.absorbedCharge-first.charge)/first.charge));
 maxK=Math.max(maxK,d.K);maxD=Math.max(maxD,d.D);
 trace.push([s.t,s.density[0]-first.baselineDensity[0],d.F,d.X,d.P,d.D,d.K]);
 }
 rows.push({h,epsilon,alpha,ratio,base:first.baselineDensity[0],initialD,initialTotal,maxE,maxQ,maxAbsE,maxK,maxD,numericalPass:maxE<.005&&maxQ<.005,trace});
 }
 return {rho:profile.rho,omega2:profile.omega2,gradient,rows,active_js_seconds:(performance.now()-start)/1000};
 }''');browser.close()
server.shutdown();Tref=2*math.pi/result['rho']
for row in result['rows']:
 eta=1e-5*max(1,row['base']);window=[s for s in row['trace'] if s[0]>=40];armed=False;ticks=[]
 for a,b in zip(window,window[1:]):
  ta,ya=a[:2];tb,yb=b[:2]
  if ya < -eta:armed=True
  if armed and ya<eta<=yb:ticks.append(ta+(tb-ta)*(eta-ya)/(yb-ya));armed=False
 periods=[b-a for a,b in zip(ticks,ticks[1:])]
 mean=statistics.mean(periods) if periods else None;cv=statistics.pstdev(periods)/mean if len(periods)>1 else None
 row.update(ticks=ticks,period_mean=mean,period_cv=cv,clock=bool(len(periods)>=8 and cv<.01 and abs(mean/Tref-1)<.02 and row['numericalPass']),X_pp=max(s[3] for s in window)-min(s[3] for s in window))
 row['resolved_transfer_one_grid']=bool(row['maxK']>0 and row['maxAbsE']<.1*row['maxK'] and row['numericalPass'])
verdicts=[]
for alpha,ratio in [(0,1),(.1,1),(1,1),(1,1.3)]:
 a,b=[next(x for x in result['rows'] if x['h']==h and x['epsilon']==.005 and x['alpha']==alpha and x['ratio']==ratio) for h in [.2,.1]]
 nulls=[next(x for x in result['rows'] if x['h']==h and x['epsilon']==0) for h in [.2,.1]]
 controls=all(x['numericalPass'] and not x['clock'] for x in nulls)
 controls=controls and all(x['X_pp']==0 and x['maxK']==0 for x in result['rows'] if x['alpha']==0)
 diff=abs(a['period_mean']/b['period_mean']-1) if a['period_mean'] and b['period_mean'] else None
 xdiff=abs(a['X_pp']/b['X_pp']-1) if b['X_pp'] else None
 readout=bool(controls and all(x['numericalPass'] and x['X_pp']>max(1e-8,10*n['X_pp']) for x,n in zip([a,b],nulls)) and xdiff is not None and xdiff<.05)
 verdicts.append(dict(alpha=alpha,ratio=ratio,controls=controls,period_grid_difference=diff,X_grid_difference=xdiff,clock=bool(controls and a['clock'] and b['clock'] and diff<.01),readout=readout,resolved_transfer=bool(controls and a['resolved_transfer_one_grid'] and b['resolved_transfer_one_grid'])))
result.update(host=socket.gethostname(),wall_seconds=time.monotonic()-start,T_reference=Tref,verdicts=verdicts,hashes={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in ['run.py','detector.js','live-solver.js','profile.json','PLAN.txt']})
(root/'RESULT.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
