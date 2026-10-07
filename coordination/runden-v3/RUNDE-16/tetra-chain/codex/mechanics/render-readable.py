"""Presentation only; reads already computed CSVs, no dynamics rerun."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(2,2,figsize=(11,6.5))
for col,label in enumerate(['11+1','19+1']):
    d=np.genfromtxt(label+'-linear.csv',delimiter=',',names=True)
    a=d['A_cell_sum'];rel=(a/a.mean()-1)*1e6
    axes[0,col].plot(d['time_over_period'],rel,color='royalblue')
    axes[0,col].set(title=f'{label}: berechnete lineare Eigenmode',xlabel='Zeit / Eigenperiode',ylabel='Flächenänderung relativ zum Mittel [ppm]')
    axes[0,col].text(.03,.95,f'Schnittpunktzahl konstant: {int(d["P"][0])}',transform=axes[0,col].transAxes,va='top',fontsize=9)
    h=np.genfromtxt(label+'-homothety.csv',delimiter=',',names=True)
    axes[1,col].plot(h['prescribed_phase'],h['A_cell_sum']/h['A_over_a_squared'][0],label='Schnittfläche / Ruhefläche')
    axes[1,col].plot(h['prescribed_phase'],h['A_over_a_squared']/h['A_over_a_squared'][0],'--',label='Skalenbereinigte Fläche')
    axes[1,col].set(title='Vorgegebene Skalierung: nur Messkontrolle',xlabel='Vorgegebene Phase',ylabel='Relative Fläche')
    axes[1,col].legend(fontsize=8)
    for ax in axes[:,col]:ax.grid(alpha=.2)
fig.suptitle('Der Punktzähler kann Bewegung übersehen — Fläche ergänzt die Messung',fontsize=13)
fig.tight_layout();fig.savefig('section-traces-readable.png',dpi=150)
