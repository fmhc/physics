import json,pathlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=pathlib.Path(__file__).resolve().parent;d=json.loads((root/'RESULT.json').read_text())
a=next(r for r in d['rows'] if r['epsilon']==.005 and r['h']==.1)
fig,axs=plt.subplots(2,1,figsize=(10,7),layout='constrained')
for j,c in [(0,'#007a87'),(2,'#ad5000'),(3,'#77549b')]:
 o=next(o for o in a['observers'] if o['mode']=='raw' and o['r']==a['radii'][j]);x=[s[0] for s in a['trace']];y=[s[1+j] for s in a['trace']]
 axs[0].plot(x,y,color=c,label=f'r = {a["radii"][j]}')
 ts=o['ticks'];axs[0].scatter(ts,[o['eta']]*len(ts),color=c,s=13)
 axs[1].plot(range(1,len(ts)),[ts[k+1]-ts[k] for k in range(len(ts)-1)],'.-',color=c,label=f'r = {a["radii"][j]}')
axs[0].set(xlim=(10,35),ylabel='Density minus fixed initial reference',xlabel='Model time',title='Radial Q-ball mode: measured threshold crossings')
axs[1].axhline(d['T_reference'],color='gray',ls='--',label='Linear mode reference')
axs[1].set(xlabel='Measured interval',ylabel='Tick period (model units)',title='Period variation: a finite-window diagnostic')
axs[1].ticklabel_format(axis='y',style='plain',useOffset=False)
for ax in axs:ax.grid(alpha=.2);ax.legend(fontsize=9)
fig.suptitle('Nonlinear radial PDE | epsilon = 0.005 | h = 0.1 | T = 60\nKnown mode used as initial excitation; no claim of emergent time',fontsize=12)
fig.savefig(root/'CLOCK.png',dpi=160)
