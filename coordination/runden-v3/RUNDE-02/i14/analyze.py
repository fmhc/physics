import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import json,numpy as np
from pathlib import Path
p=Path(__file__).parent;data=json.loads((p/'RESULT.json').read_text());results=[]
for run in data['results']:
 for idx,factor in enumerate((2,3)):
  ts=[];rs=[];ns=[];qs=[];fits=[];pairs=[];merges=0;splits=0;selected=[]
  for e in run['trace']:
   d=e['thresholds'][idx];cs=[c for c in d['components'] if not c['winding']]
   ts.append(e['t']);ns.append(len(cs));rs.append(float(np.mean([c['R'] for c in cs])) if cs else None);qs.append(float(np.mean([c['Q'] for c in cs])) if cs else None)
   if e['t']>=80:
    pairs.extend(d['tracking']['pairs']);merges+=d['tracking']['merges'];splits+=d['tracking']['splits']
   if e['t'] in (40,80,120,160,200):selected.append(dict(t=e['t'],count=d['count'],nonwinding=len(cs),mean_R=rs[-1],mean_Q=qs[-1]))
  use=np.array([t>=80 and n>=3 and r is not None for t,n,r in zip(ts,ns,rs)])
  t=np.array(ts)[use];r=np.array([x or 0 for x in rs])[use]
  for power in (2,3,4):
   if len(t)>=2:
    y=r**power;b,a=np.polyfit(t,y,1);res=np.sum((y-a-b*t)**2);var=np.sum((y-y.mean())**2)
    fits.append(dict(power=power,points=len(t),slope=float(b),intercept=float(a),R2=None if var==0 else float(1-res/var)))
   else:fits.append(dict(power=power,points=len(t),slope=None,R2=None))
  if len(pairs)>2:
   pr=np.array([v['R'] for v in pairs]);dq=np.array([v['dQ_dt'] for v in pairs]);corr=float(np.corrcoef(pr,dq)[0,1]) if pr.std()>0 and dq.std()>0 else None
  else:corr=None
  f=fits[1];compatible=f['points']>=20 and f['slope'] is not None and f['slope']>0 and f['R2'] is not None and f['R2']>=.9
  results.append(dict(tag=run['tag'],factor=factor,selected=selected,fits=fits,compatible=bool(compatible),track_pairs=len(pairs),radius_dQ_correlation=corr,merge_events=merges,split_events=splits,ts=ts,R=rs,n=ns))
comparisons=[]
main=next(r for r in data['results'] if r['tag']=='main')
for other in data['results']:
 if other['tag'] not in ('time','space'):continue
 for idx,factor in enumerate((2,3)):
  ca=np.array([e['thresholds'][idx]['count'] for e in main['trace']]);cb=np.array([e['thresholds'][idx]['count'] for e in other['trace']])
  comparisons.append(dict(other=other['tag'],factor=factor,max_count_difference=int(np.max(abs(ca-cb))),fraction_different=float(np.mean(ca!=cb))))
summary=dict(cpu=data['cpu'],wall=data['wall'],results=results,comparisons=comparisons,conservation=[{k:r[k] for k in ('tag','energy_error','charge_error')} for r in data['results']])
(p/'SUMMARY.json').write_text(json.dumps(summary,indent=2))
print(json.dumps({**summary,'results':[{k:v for k,v in r.items() if k not in ('ts','R','n')} for r in results]},indent=2))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(2,2,figsize=(11,7),layout='constrained')
for r in results:
 col=0 if r['factor']==2 else 1
 ax[0,col].plot(r['ts'],r['n'],label=r['tag']);ax[1,col].plot(r['ts'],r['R'],label=r['tag'])
 ax[0,col].set(title=f'Density threshold {r["factor"]}× initial S',ylabel='Non-winding components')
 ax[1,col].set(xlabel='Field simulation time',ylabel='Mean equivalent radius')
for a in ax.ravel():a.legend();a.grid(alpha=.2)
fig.suptitle('I14: continuation T40–200; threshold structures, not certified Q-balls')
fig.savefig(p/'I14.png',dpi=145)
