#!/usr/bin/env python3
"""Exploratory existing-sample diagnostics only; no PDE solver."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import numpy as np

EXPECTED='97cfb7ff68bff7a64bb4fb0aaf44130e859f6689ad5482594e5209c79df6e89a'
LEVELS=('base','space','time')
KEYS=('r50_density','Qcore','chi_first_cell','rphi','rchi','tphi','tchi')


def describe(t,y):
    imin=int(np.argmin(y)); imax=int(np.argmax(y))
    peaks=np.flatnonzero((y[1:-1]>y[:-2])&(y[1:-1]>y[2:]))+1
    troughs=np.flatnonzero((y[1:-1]<y[:-2])&(y[1:-1]<y[2:]))+1
    intervals=np.diff(t[peaks])
    return dict(minimum=float(y[imin]),minimum_time=float(t[imin]),
                maximum=float(y[imax]),maximum_time=float(t[imax]),
                net_change=float(y[-1]-y[0]),
                strict_maxima_times=t[peaks].tolist(),strict_minima_times=t[troughs].tolist(),
                crest_intervals=int(len(intervals)),
                crest_interval_median=float(np.median(intervals)) if len(intervals) else None,
                crest_interval_range=[float(intervals.min()),float(intervals.max())] if len(intervals) else None)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    raw=args.input.read_bytes(); digest=hashlib.sha256(raw).hexdigest()
    if digest!=EXPECTED: raise ValueError('Input hash differs from frozen plan')
    data=json.loads(raw)
    arms=[a for a in data['arms'] if a['kind']=='cloud']
    if len(arms)!=3 or {a['level'] for a in arms}!=set(LEVELS):
        raise ValueError('Expected three unique cloud levels')
    series={}; summary={}; t=np.arange(81,dtype=float)*.8
    for arm in arms:
        if not arm['complete'] or len(arm['samples'])!=81:
            raise ValueError('Incomplete cloud input')
        times=np.array([s['t'] for s in arm['samples']],dtype=float)
        if not np.all(np.isfinite(times)) or np.max(abs(times-t))>1e-10:
            raise ValueError('Non-synchronous sample times')
        arrays={k:np.array([s[k] for s in arm['samples']],dtype=float) for k in KEYS}
        if not all(np.all(np.isfinite(x)) for x in arrays.values()):
            raise ValueError('Nonfinite diagnostics')
        arrays['Qcore_fraction']=arrays['Qcore']/1100
        level=arm['level']; series[level]=arrays
        row=dict(h=arm['h'],dt=arm['dt'],observables={},terminal_residuals={})
        for key in ('r50_density','Qcore_fraction','chi_first_cell'):
            row['observables'][key]=describe(t,arrays[key])
        mask=t>=48-1e-10
        for key in ('rphi','rchi','tphi','tchi'):
            y=arrays[key][mask]; tt=t[mask]; j=int(np.argmax(y))
            row['terminal_residuals'][key]=dict(sample_rms=float(np.sqrt(np.mean(y*y))),
                            maximum=float(y[j]),maximum_time=float(tt[j]))
        summary[level]=row
    args.out.mkdir(parents=True,exist_ok=False)
    with (args.out/'TIMESERIES.csv').open('w',newline='') as stream:
        writer=csv.writer(stream); columns=(*KEYS,'Qcore_fraction')
        writer.writerow(('level','t',*columns))
        for level in LEVELS:
            for i,stamp in enumerate(t):
                writer.writerow((level,float(stamp),*(float(series[level][k][i]) for k in columns)))
    result=dict(original_status=data['status'],analysis='exploratory; no classification change',
                input_sha256=digest,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                sample_dt=.8,nyquist_angular=float(np.pi/.8),window_angular_scale=float(2*np.pi/64),
                limitations='No field sidebands; peak counts are sampled diagnostic cycles, not eigenmodes.',arms=summary)
    (args.out/'SUMMARY.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    colors=dict(base='#1f77b4',space='#d95f02',time='#1b9e77')
    fig,ax=plt.subplots(3,1,figsize=(11,11),constrained_layout=True)
    sizes=('r50_density','Qcore_fraction','chi_first_cell')
    styles=('-', '--', ':')
    names=('R50 density / initial','Qcore / 1100','chi first cell')
    for level in LEVELS:
        for key,style,name in zip(sizes,styles,names):
            y=series[level][key]
            if key=='r50_density': y=y/y[0]
            ax[0].plot(t,y,ls=style,color=colors[level],label=f'{level}: {name}')
    ax[0].set_ylabel('Dimensionless diagnostics'); ax[0].legend(fontsize=7,ncol=3)
    mask=t>=48-1e-10
    for level in LEVELS:
        for key,style in zip(('rphi','rchi','tphi','tchi'),('-','--',':','-.')):
            y=series[level][key][mask]
            ax[1].plot(t[mask],np.ma.masked_less_equal(y,0),ls=style,color=colors[level],
                       label=f'{level}: {key}')
    ax[1].set_yscale('log'); ax[1].set_ylabel('Terminal normalized residuals')
    ax[1].legend(fontsize=7,ncol=4)
    for level in ('space','time'):
        for key,style,name in zip(sizes,styles,names):
            difference=abs(series[level][key]-series['base'][key])
            if key=='r50_density': difference=difference/series['base'][key][0]
            label=('space-base' if level=='space' else 'time-base')+': '+name
            if key=='r50_density':
                label=('space-base' if level=='space' else 'time-base')+': ΔR50/R50_base(0)'
            ax[2].plot(t,difference,ls=style,color=colors[level],label=label)
    ax[2].set_ylabel('Absolute spatial/time differences')
    ax[2].legend(fontsize=7,ncol=2)
    for panel in ax:
        panel.set_xlabel('Model time'); panel.grid(alpha=.2)
    fig.suptitle('Numerisch unentschieden — gespeicherte Diagnosen\n'+data['status'],fontsize=13)
    fig.savefig(args.out/'DIAGNOSTICS.png',dpi=140)
    plt.close(fig)


if __name__=='__main__':
    main()
