import torch,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent;rows=json.loads((P/'results/RESULT.json').read_text());assert len(rows)==18
def t(v):return torch.tensor(v,device='cuda',dtype=torch.float64)
def distance(a,b):return float((t(a)-t(b)).norm()/t(b).norm())
comp=[];seedchecks=[]
for stage in ['base','grid','box']:
 for method in ['full','E3','Ecomp']:
  rr=[x for x in rows if x['stage']==stage and x['method']==method]
  seedchecks.append(dict(stage=stage,method=method,relative_profile_distance=distance(rr[1]['u'],rr[0]['u'])))
 for method in ['E3','Ecomp']:
  for seed in [0,1]:
   ref=next(x for x in rows if (x['stage'],x['method'],x['seed'])==(stage,'full',seed));x=next(x for x in rows if (x['stage'],x['method'],x['seed'])==(stage,method,seed))
   comp.append(dict(stage=stage,method=method,seed=seed,profile_error=distance(x['u'],ref['u']),higgs_profile_error=distance(x['z'],ref['z']),energy_error=abs(x['energy']/ref['energy']-1),omega_error=abs(x['omega']/ref['omega']-1)))
verdict=[]
for method in ['E3','Ecomp']:
 valid=all(x['residual']<1e-5 for x in rows if x['method'] in ['full',method]) and all(x['relative_profile_distance']<.001 for x in seedchecks if x['method'] in ['full',method])
 gates={}
 for key,lim in [('profile_error',.01),('energy_error',.001),('omega_error',.005)]:
  cc=[x for x in comp if x['method']==method];drift=max(abs(x[key]-next(y[key] for y in cc if y['stage']=='base' and y['seed']==x['seed'])) for x in cc)
  mx=max(x[key] for x in cc);mn=min(x[key] for x in cc)
  gates[key]=dict(maximum=mx,minimum=mn,drift=drift,limit=lim,verdict='bestanden' if mx+drift<=lim else ('verfehlt' if mn-drift>lim else 'unentschieden'))
 result='unentschieden' if not valid else ('bestanden' if all(v['verdict']=='bestanden' for v in gates.values()) else ('verfehlt' if any(v['verdict']=='verfehlt' for v in gates.values()) else 'unentschieden'))
 verdict.append(dict(method=method,convergence_and_seed_gate=valid,verdict=result,gates=gates))
s=dict(comparisons=comp,seed_checks=seedchecks,verdicts=verdict,max_residual=max(x['residual'] for x in rows),max_tail=max(x['tail'] for x in rows),all_bound=all(x['bound'] for x in rows))
(P/'SUMMARY.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(s,indent=2))
plt.rcParams.update({'svg.fonttype':'none','font.size':11})
fig,axs=plt.subplots(1,2,figsize=(11,4.5),layout='constrained')
for m,color in [('E3','#d07922'),('Ecomp','#16826b')]:
 for ax,key,title in [(axs[0],'profile_error','Materieprofil'),(axs[1],'omega_error','Frequenz bei festem Q')]:
  vals=[100*max(x[key] for x in comp if x['stage']==stage and x['method']==m) for stage in ['base','grid','box']]
  ax.plot([0,1,2],vals,'o-',label=m,color=color);ax.set_xticks([0,1,2],['Basis','feiner','größere Box']);ax.set_yscale('log');ax.set_title(title);ax.set_ylabel('Relativer Fehler [%]');ax.legend();ax.grid(alpha=.2)
fig.suptitle('Selbstkonsistenter Higgs-Pilot · g = 0,005 · Q = 600')
fig.supxlabel('Vergleich mit voller Theorie · Maximum über zwei Startwerte · radialer 3D-Zweig',fontsize=10)
fig.savefig(P/'minima-errors.svg',metadata={'Date':None});p=P/'minima-errors.svg';p.write_text('\n'.join(l.rstrip() for l in p.read_text().splitlines())+'\n')
