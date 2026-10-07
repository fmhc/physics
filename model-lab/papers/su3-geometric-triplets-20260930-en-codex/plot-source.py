import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from pathlib import Path
p=Path(__file__).parent;d=json.loads((p/'RESULT.json').read_text())
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,2,figsize=(11,4.1),layout='constrained')
scan=d['scan'];root=d['roots'][-1]
axs[0].plot([s['A'] for s in scan],[s['Pmax'] for s in scan],'o-',color='#216b91',label='Vorgegebenes Raster')
axs[0].scatter([root['A']],[1],s=70,marker='*',color='#d47d1f',zorder=5,label='Frequenzen abgeglichen')
axs[0].axvline(4,color='#777',ls=':',lw=1)
axs[0].set(xlabel='Tiefe der äußeren Schalenmulde',ylabel='Maximaler kanonischer Transfer',title='Die 68 % sind keine feste Zahl',ylim=(0,1.06))
axs[0].yaxis.set_major_formatter(PercentFormatter(1));axs[0].legend(loc='lower left',fontsize=8)
for label,col,name in [('original','#216b91','Ausgangsmodell'),('frequency_matched','#d47d1f','Frequenzabgleich')]:
 r=next(x for x in d['runs'] if x['label']==label and x['h']==.0125)
 axs[1].plot(r['sample_times'],r['sample_modal_outer'],color=col,label=name+' · Moden')
 axs[1].scatter([0,r['tmax'],2*r['tmax']],[r['initial_outer_fraction'],r['outer_at_canonical_max'],r['outer_at_return']],color=col,marker='x',s=36,zorder=5,label=name+' · Energie-Stichpunkte')
axs[1].set(xlabel='Zeit (Modelleinheiten)',ylabel='Anteil außen / äußere Modenkombination',title='Reversibler Austausch, kein Energieverlust',ylim=(0,1.06));axs[1].yaxis.set_major_formatter(PercentFormatter(1));axs[1].legend(fontsize=7,loc='upper right')
fig.suptitle('Konzentrisches lineares Feldmodell · Schalenradien 6 und 10',fontsize=13)
fig.savefig(p/'transfer.png',dpi=160);fig.savefig(p/'transfer.svg')
