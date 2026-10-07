import json,pathlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=pathlib.Path(__file__).resolve().parent;d=json.loads((p/'RESULT.json').read_text())
f,ax=plt.subplots(3,1,figsize=(10,8),constrained_layout=True)
for row in d['rows']:
 if row['h']!=.1 or row['epsilon']==0:continue
 label=f"alpha={row['alpha']:g}, detector/rho={row['ratio']:g}"
 tr=row['trace'];t=[x[0] for x in tr]
 ax[0].plot(t,[x[1] for x in tr],label=label,lw=1)
 ax[1].plot(t,[x[3] for x in tr],label=label,lw=1)
 ax[2].plot(t,[max(1e-15,x[6]) for x in tr],label=label,lw=1)
 if row['alpha']==1 and row['ratio']==1:ax[2].axhline(row['maxAbsE'],color='black',ls=':',label='max absolute balance error, alpha=1 tuned')
ax[0].set(xlim=(40,60),ylabel='Central density contrast')
ax[1].set(ylabel='Detector coordinate X')
ax[2].set(yscale='log',ylabel='Detector kinetic energy',xlabel='Model time')
for a in ax:a.grid(alpha=.2)
ax[1].legend(fontsize=8,ncol=2);ax[2].legend(fontsize=7,ncol=2)
f.suptitle('Reciprocal detector on a prepared radial Q-ball mode\nh=0.1; exploratory classical model, no experimental noise model')
f.savefig(p/'DETECTOR.png',dpi=160)
