import json
from pathlib import Path
p=Path(__file__).parent
data=json.loads((p/'RESULT.json').read_text());rows=data['records']
comparisons=[]
for model in ('vfw_proxy','standard'):
 for dim in (1,2):
  for seed in (31,73):
   def get(arm,dt):return next(r for r in rows if (r['model'],r['dim'],r['seed'],r['arm'],r['dt'])==(model,dim,seed,arm,dt))
   a=get('main',.01);b=get('K0',.01)
   effect=a['end']['R']-b['end']['R']
   error=max(abs(a['end']['R']-get('main',.02)['end']['R']),abs(b['end']['R']-get('K0',.02)['end']['R']))
   comparisons.append(dict(model=model,dim=dim,seed=seed,Rmain=a['end']['R'],RK0=b['end']['R'],effect=effect,dt_error=error,L2=effect>=.05,L3=effect>=5*error,Dmain=a['end']['D'],DK0=b['end']['D'],Dreverse=get('reverseJ',.01)['end']['D'],probe_main=a['end']['probe'],probe_K0=b['end']['probe']))
result=dict(host=data['host'],runs=len(rows),valid=all(r['valid'] for r in rows),wall_seconds=data['wall_seconds'],cpu_seconds=data['cpu_seconds'],max_null=max(r['null_error'] for r in rows),max_center=max(r['center_error'] for r in rows),checks=data['checks'],comparisons=comparisons)
(p/'SUMMARY.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
