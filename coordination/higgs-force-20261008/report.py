import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
D=json.loads((P/'results/RESULT.json').read_text());Q=json.loads((P/'results/QA.json').read_text())
fine=[r for r in D['rows'] if r['stage']=='grid']
for g in [.001,.005]:
 print('g',g)
 rr=[r for r in fine if r['portal_g']==g]
 for m in ['E2','E3','Ecomp']:
  print(m,{k:[100*min(r['methods'][m][k] for r in rr),100*max(r['methods'][m][k] for r in rr)] for k in ['force_relative_error','higgs_energy_relative_error']})
 for k in ['Cplug_force_relative_error','omitted_chain_force_relative','Cplug_cross_derivative_defect']: print(k,[100*min(r[k] for r in rr),100*max(r[k] for r in rr)])
print('QA C3',max(r['analytic_C3_relative_error'] for r in Q['rows']))
for m in ['E3','Ecomp']:
 print('QA',m,'FD',max(r['finite_difference_relative_errors'][m][-1] for r in Q['rows']),'sym',max(r['cross_derivative'][m]['relative_defect'] for r in Q['rows']))
print('drift',max(g['observed_grid_box_indicator'] for g in D['groups']))
print('elapsed',D['elapsed_s'],'peak',D['gpu_peak_allocated_bytes'])
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
fig,axs=plt.subplots(1,2,figsize=(12,4.7),layout='constrained')
colors=['#2877ac','#dc7a22','#17856a']
for ax,key,title in zip(axs,['force_relative_error','higgs_energy_relative_error'],['Zusätzliche Portalkraft','Statischer Higgs-Energiebeitrag']):
 for j,m in enumerate(['E2','E3','Ecomp']):
  for i,g in enumerate([.001,.005]):
   vals=[100*r['methods'][m][key] for r in fine if r['portal_g']==g]
   mid=(min(vals)+max(vals))/2;x=i+(j-1)*.17
   ax.errorbar(x,mid,yerr=[[mid-min(vals)],[max(vals)-mid]],fmt='o',capsize=5,color=colors[j],label=m if i==0 else None)
 ax.axhline(5,color='#9a3440',linestyle='--',label='Pilotgrenze 5 %')
 ax.set_yscale('log');ax.set_xticks([0,1],['g = 0,001','g = 0,005']);ax.set_xlim(-.4,1.4)
 ax.set_ylabel('Relativer Fehler [%]');ax.set_title(title);ax.grid(axis='y',alpha=.2);ax.legend(fontsize=9)
fig.suptitle('HIGGS-FORCE-1 · Energie und Kraft gemeinsam geprüft',fontsize=16)
fig.supxlabel('Feines Radialgitter · Spannen über je vier Parameterfälle · feste archivierte 3D-Profile',fontsize=10)
fig.savefig(P/'force-errors.svg',metadata={'Date':None})
p=P/'force-errors.svg';p.write_text('\n'.join(s.rstrip() for s in p.read_text().splitlines())+'\n')
