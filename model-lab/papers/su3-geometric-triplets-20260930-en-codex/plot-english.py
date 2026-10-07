"""Translate labels and render existing data only; run on .69, no physics rerun."""
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from pathlib import Path
p=Path(__file__).parent;d=json.loads((p/'FIGURE-DATA.json').read_text())
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,2,figsize=(11,4.1),layout='constrained')
scan=d['scan'];root=d['roots'][-1]
axs[0].plot([s['A'] for s in scan],[s['Pmax'] for s in scan],'o-',color='#216b91',label='Prespecified grid')
axs[0].scatter([root['A']],[1],s=70,marker='*',color='#d47d1f',zorder=5,label='Frequencies matched')
axs[0].axvline(4,color='#777',ls=':',lw=1)
axs[0].set(xlabel='Depth of the outer shell well',ylabel='Maximum canonical transfer',title='68% is not a fixed value',ylim=(0,1.06))
axs[0].yaxis.set_major_formatter(PercentFormatter(1));axs[0].legend(loc='lower left',fontsize=8)
for label,col,name in [('original','#216b91','Original model'),('frequency_matched','#d47d1f','Frequency matched')]:
 r=next(x for x in d['runs'] if x['label']==label and x['h']==.0125)
 axs[1].plot(r['sample_times'],r['sample_modal_outer'],color=col,label=name+' · modes')
 axs[1].scatter([0,r['tmax'],2*r['tmax']],[r['initial_outer_fraction'],r['outer_at_canonical_max'],r['outer_at_return']],color=col,marker='x',s=36,zorder=5,label=name+' · energy samples')
axs[1].set(xlabel='Time (model units)',ylabel='Outer fraction / outer mode combination',title='Reversible exchange, no energy loss',ylim=(0,1.06));axs[1].yaxis.set_major_formatter(PercentFormatter(1));axs[1].legend(fontsize=7,loc='upper right')
fig.suptitle('Concentric linear field model · shell radii 6 and 10',fontsize=13)
fig.savefig(p/'transfer-detuning.png',dpi=160)
fig.savefig(p/'transfer-detuning.svg')
fig.savefig(p/'transfer-detuning.pdf')
