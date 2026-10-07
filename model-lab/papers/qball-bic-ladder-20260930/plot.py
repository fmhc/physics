import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
with open('figure-data.json') as f:d=json.load(f)
n=d['n'];x=d['x'];inv=[1/(v-.5) for v in x]
fig,axs=plt.subplots(1,2,figsize=(10,3.7),layout='constrained')
for ax,y,label in zip(axs,[x,inv],[r'$\omega^2$',r'$1/(\omega^2-1/2)$']):
 ax.scatter(n[2:],y[2:],facecolors='none',edgecolors='#2563a6',s=40,label='Numerical candidates')
 ax.scatter(n[:2],y[:2],color='#9b312b',marker='s',s=40,label='Existence enclosures')
 ax.set(xlabel='Continuation label n',ylabel=label,xticks=[1,3,5,7,9,11,13,15])
 ax.grid(alpha=.2)
axs[0].axhline(.5,color='0.5',lw=1,ls='--')
axs[0].legend(fontsize=8,loc='upper right')
fig.savefig('ladder.pdf');fig.savefig('ladder.svg');fig.savefig('ladder.png',dpi=160)
