#!/usr/bin/env python3
"""Descriptive postprocessing only; no new spectrum computation or pass gates."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parent
data=json.loads((root/'result.json').read_text())
fig,axs=plt.subplots(1,2,figsize=(11,4),layout='constrained')
colors=['#2563eb','#9333ea','#0891b2','#ea580c','#16a34a','#dc2626']
directions=['axis0','axis1','axis2','axis3','diagonal4','spatial111']
symmetry={}
for ax,(name,arm) in zip(axs,data['arms'].items()):
    symmetry[name]=0.
    for direction,color in zip(directions,colors):
        selected=[(p,s) for p,s in zip(data['points'],arm) if p.get('direction')==direction and p['sign']==1]
        ax.plot([p['scale'] for p,s in selected],[s['lowest_five'][0] for p,s in selected],'o-',color=color,label=direction,markersize=4)
        for p,s in selected:
            n=next(t for q,t in zip(data['points'],arm) if q.get('direction')==direction and q['sign']==-1 and q['scale']==p['scale'])
            symmetry[name]=max(symmetry[name],abs(s['lowest_five'][0]-n['lowest_five'][0])/max(s['max_abs'],n['max_abs']))
    ax.set_xscale('log'); ax.set_yscale('symlog',linthresh=1e-10)
    ax.axhline(0,color='#475569',lw=.7)
    ax.set_xlabel('Norm of primitive-cell Bloch phase q')
    ax.set_ylabel('Smallest projected quadratic eigenvalue')
    ax.set_title(name.replace('_',' ')); ax.grid(alpha=.2)
axs[1].legend(fontsize=8)
fig.suptitle('Fixed Maxwell weights on V × Euclidean time\nSmall-q consistency diagnostic; eigenvalues are not photon energies',fontsize=12)
fig.savefig(root/'small-q.svg')
(root/'small-q.svg').write_text('\n'.join(line.rstrip() for line in (root/'small-q.svg').read_text().splitlines())+'\n')
summary={'post_hoc_diagnostic':True,'not_an_acceptance_gate':True,'q_minus_q_min_eigenvalue_difference_over_spectral_scale':symmetry,'minimum_d0_singular_ratio':min(data['d0_smallest_over_largest_singular_value']),'rank_relative_threshold':1e-10,'summaries':{}}
for name,arm in data['arms'].items():
    summary['summaries'][name]={kind:{c:sum(s['classification']==c for p,s in zip(data['points'],arm) if p['kind']==kind) for c in ['negative','positive','unresolved']} for kind in ['random','ray']}
    summary['summaries'][name]['rays']={direction:[{'qnorm':p['scale'],'minimum':s['lowest_five'][0],'relative':s['min_relative']} for p,s in zip(data['points'],arm) if p.get('direction')==direction and p['sign']==1] for direction in directions}
(root/'postprocess.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary))
