#!/usr/bin/env python3
"""Plot saved nonlinear response diagnostics only; no solver or fit."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--sha256',required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args(); raw=a.input.read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    if digest!=a.sha256: raise ValueError('Input hash mismatch')
    data=json.loads(raw)
    arms=[x for x in data['arms'] if x['epsilon']>0]
    if len(arms)!=6 or not all(x['complete'] for x in arms): raise ValueError('Expected six complete excited arms')
    rho=next(x['rho'] for x in data['ritz'] if x['h']==.05)
    fig,axes=plt.subplots(2,1,figsize=(10,8),sharex=True,constrained_layout=True)
    times=np.array([s['t'] for s in arms[0]['samples']])
    axes[0].plot(times,np.cos(rho*times),color='black',lw=1.6,label='cos(ρt), festes Soll')
    axes[0].plot(times,np.sin(rho*times),color='gray',lw=1.6,label='sin(ρt), festes Soll')
    colors={.001:'#0072B2',.002:'#D55E00'}
    for arm in arms:
        t=np.array([s['t'] for s in arm['samples']])
        if not np.array_equal(t,times): raise ValueError('Non-synchronous samples')
        eps=arm['epsilon']
        if arm['level']=='space':
            co=np.array([s['mode_response']['projection_coefficients'] for s in arm['samples']])
            for j,name in enumerate(('cos','sin')):
                axes[0].plot(t,co[:,j],color=colors[eps],ls='--' if j==0 else ':',lw=1.1,
                    marker='o' if eps==.001 else 'x',markevery=8,ms=3,
                    label=f'{name}-Projektion, ε={eps:g}')
    palette={'base':'#0072B2','space':'#009E73','time':'#D55E00'}
    for arm in arms:
        error=np.array([s['mode_response']['linear_error'] for s in arm['samples']])
        axes[1].plot(times,error,color=palette[arm['level']],ls='-' if arm['epsilon']==.001 else '--',
            label=f"{arm['level']}: h={arm['h']:g}, dt={arm['dt']:g}, ε={arm['epsilon']:g}")
    axes[0].set_ylabel('Feste Modenkoordinaten')
    axes[0].set_title(f'Feines Raumgitter h=0.05: Projektion auf Re(v), −Im(v), ρ={rho:.6f}')
    axes[0].legend(fontsize=8,ncol=2)
    axes[1].set_ylabel('‖ΔY/(εs) − Re(v exp(iρt))‖ / ‖v‖')
    axes[1].set_xlabel('Modellzeit t'); axes[1].legend(fontsize=8,ncol=2)
    for ax in axes: ax.grid(alpha=.25); ax.set_xlim(0,32)
    fig.suptitle('Nichtlineare Kleinamplitudenprobe — T=32\nBaseline abgezogen; feste Frequenz, kein Fit',fontsize=13)
    a.out.mkdir(parents=True,exist_ok=False)
    fig.savefig(a.out/'EXCITATION.png',dpi=160)
    fig.savefig(a.out/'EXCITATION.svg')
    plt.close(fig)
    (a.out/'PROVENANCE.json').write_text(json.dumps(dict(input_sha256=digest,
        plot_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),original_status=data['status'],
        note='Saved diagnostics only; no solver, fit or paper edit'),indent=2)+'\n')


if __name__=='__main__':
    main()
