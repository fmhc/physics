import json,pathlib,math,statistics,hashlib,socket,time
p=pathlib.Path(__file__).resolve().parent;start=time.monotonic();data=json.loads((p/'SOURCE.json').read_text());T=data['T_reference']
def ticks(series,eta):
 armed=False;out=[]
 for (ta,a),(tb,b) in zip(series,series[1:]):
  if a < -eta:armed=True
  if armed and a<eta<=b:out.append(ta+(tb-ta)*(eta-a)/(b-a));armed=False
 return out
def stats(ts,period):
 intervals=[b-a for a,b in zip(ts,ts[1:])];m=statistics.mean(intervals) if intervals else None;c=statistics.pstdev(intervals)/m if len(intervals)>1 else None
 return dict(ticks=ts,count=len(ts),mean=m,cv=c,pass_clock=bool(len(intervals)>=8 and c<.01 and abs(m/period-1)<.02))
checks=[]
for dt in [.1,.2]:
 samples=[(40+i*dt,math.sin(2*math.pi*(40+i*dt)/3.6)) for i in range(round(60/dt)+1)]
 checks.append(stats(ticks(samples,1e-4),3.6)['pass_clock'])
checks.append(not ticks([(i,.1) for i in range(100)],1e-4))
rows=[]
for r in data['rows']:
 w=[x for x in r['trace'] if x[0]>=40];s=stats(ticks([(x[0],x[3]) for x in w],1e-4),T)
 ft=r['ticks'];offsets=[(t-min(ft,key=lambda x:abs(x-t)))/T for t in s['ticks'] if ft and ft[0]+T/2<t<ft[-1]-T/2]
 s.update(h=r['h'],epsilon=r['epsilon'],alpha=r['alpha'],ratio=r['ratio'],mean_over_free_detector_period=s['mean']/(T/r['ratio']) if s['mean'] else None)
 s.update(offset_mean=statistics.mean(offsets) if offsets else None,offset_std=statistics.pstdev(offsets) if len(offsets)>1 else None);rows.append(s)
controls=all(checks) and all(r['count']==0 for r in rows if r['epsilon']==0 or r['alpha']==0)
verdicts=[]
for alpha,ratio in [(0,1),(.1,1),(1,1),(1,1.3)]:
 a,b=[next(r for r in rows if r['h']==h and r['epsilon']==.005 and r['alpha']==alpha and r['ratio']==ratio) for h in [.2,.1]]
 diff=abs(a['mean']/b['mean']-1) if a['mean'] and b['mean'] else None
 verdicts.append(dict(alpha=alpha,ratio=ratio,grid_difference=diff,detector_clock=bool(controls and a['pass_clock'] and b['pass_clock'] and diff<.01)))
result=dict(rows=rows,controls=controls,analytic_checks=checks,verdicts=verdicts,host=socket.gethostname(),wall_seconds=time.monotonic()-start,hashes={name:hashlib.sha256((p/name).read_bytes()).hexdigest() for name in ['SOURCE.json','PLAN.txt','analyze.py']})
(p/'RESULT.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
