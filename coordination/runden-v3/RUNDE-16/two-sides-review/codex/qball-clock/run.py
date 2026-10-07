import http.server,functools,threading,json,pathlib,socket,time,math,statistics,hashlib
from playwright.sync_api import sync_playwright
root=pathlib.Path(__file__).resolve().parent
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(root)))
threading.Thread(target=server.serve_forever,daemon=True).start();start=time.monotonic()
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/home/fmh/.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell',args=['--no-sandbox','--disable-gpu'])
 page=browser.new_page();page.goto(f'http://127.0.0.1:{server.server_port}/')
 result=page.evaluate('''async()=>{
 const {RadialSimulation}=await import('./live-solver.js');
 const profile=await(await fetch('./profile.json')).json(),rows=[],start=performance.now();
 for(const h of [.2,.1])for(const epsilon of [0,.005,.02]){
 const sim=new RadialSimulation({profile,h,epsilon,R:80,linear:false,absorber:true});
 const radii=[0,1,2,4],ids=radii.map(r=>Math.round(r/h)),first=sim.sample();
 const base=ids.map(i=>first.baselineDensity[i]),trace=[];let maxE=0,maxQ=0;
 while(sim.t<60-1e-8){
 if(performance.now()-start>45000)throw Error('active JS budget exceeded');
 sim.step(5);const s=sim.sample();if(!s.finite)throw Error('nonfinite');
 maxE=Math.max(maxE,Math.abs(s.energyBalanceDrift));maxQ=Math.max(maxQ,Math.abs(s.chargeBalanceDrift));
 trace.push([s.t,...ids.map((i,j)=>s.density[i]-base[j]),...ids.map(i=>s.density[i]-s.baselineDensity[i])]);
 }
 rows.push({h,epsilon,radii,base,maxE,maxQ,numericalPass:maxE<.005&&maxQ<.005,trace});
 }
 return {rho:profile.rho,omega2:profile.omega2,rows,active_js_seconds:(performance.now()-start)/1000};
 }''');browser.close()
server.shutdown()
Tref=2*math.pi/result['rho']
for row in result['rows']:
 row['observers']=[]
 for mode,startcol in [('raw',1),('corrected',5)]:
  for j,r in enumerate(row['radii']):
   eta=1e-5*max(1,row['base'][j]);ys=[(s[0],s[startcol+j]) for s in row['trace'] if s[0]>=10]
   armed=False;ticks=[]
   for (ta,ya),(tb,yb) in zip(ys,ys[1:]):
    if ya < -eta:armed=True
    if armed and ya<eta<=yb:
     ticks.append(ta+(tb-ta)*(eta-ya)/(yb-ya));armed=False
   periods=[b-a for a,b in zip(ticks,ticks[1:])];enough=len(periods)>=8
   mean=statistics.mean(periods) if periods else None;cv=statistics.pstdev(periods)/mean if len(periods)>1 else None
   drift=None
   if enough:
    k=len(periods)//2;drift=(statistics.mean(periods[k:])-statistics.mean(periods[:k]))/mean
   clock=bool(enough and cv<.01 and abs(mean/Tref-1)<.02 and row['numericalPass'])
   row['observers'].append(dict(mode=mode,r=r,eta=eta,ticks=ticks,period_mean=mean,period_cv=cv,relative_period_drift=drift,peak_to_peak=max(y for _,y in ys)-min(y for _,y in ys),finite_clock_one_grid=clock))
   if row['epsilon']==0 and mode=='corrected':assert not ticks
verdicts=[]
for epsilon in [.005,.02]:
 coarse=next(x for x in result['rows'] if x['epsilon']==epsilon and x['h']==.2)
 fine=next(x for x in result['rows'] if x['epsilon']==epsilon and x['h']==.1)
 for a,b in zip(coarse['observers'],fine['observers']):
  diff=abs(a['period_mean']/b['period_mean']-1) if a['period_mean'] and b['period_mean'] else None
  verdicts.append(dict(epsilon=epsilon,mode=a['mode'],r=a['r'],period_relative_grid_difference=diff,finite_clock=bool(a['finite_clock_one_grid'] and b['finite_clock_one_grid'] and diff<.01)))
result.update(host=socket.gethostname(),wall_seconds=time.monotonic()-start,T_reference=Tref,verdicts=verdicts,hashes={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in ['run.py','live-solver.js','profile.json','PLAN.txt']})
(root/'RESULT.json').write_text(json.dumps(result,indent=2))
print(json.dumps({**{k:v for k,v in result.items() if k!='rows'},'summary':[{'h':x['h'],'epsilon':x['epsilon'],'maxE':x['maxE'],'maxQ':x['maxQ'],'observers':x['observers']} for x in result['rows']]},indent=2))
