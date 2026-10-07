#!/usr/bin/env python3
"""Display completed saved diagnostics only; no evolution, trajectory analysis or fit."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--sha256',help='Optional expected input SHA256')
    args=parser.parse_args(); raw=args.input.read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    if args.sha256 is not None and digest!=args.sha256:
        raise ValueError('Input hash mismatch')
    data=json.loads(raw)
    if data['status'] not in ('UNRESOLVED','CONTROLLED_NONLINEAR_SECOND_BAND_IN_FIXED_WINDOWS'):
        raise ValueError('Expected completed analysis, not a partial run')
    if len(data['arms'])!=11 or not all(a['complete'] for a in data['arms']):
        raise ValueError('Expected eleven complete arms')
    combinations=(('base',.001),('base',.002),('space',.002),('time',.002))
    rows=data['measurements']
    mapping={(r['level'],r['epsilon'],r['time_window'],r['shell']):r for r in rows}
    expected={(level,eps,w,s) for level,eps in combinations for w in (0,1) for s in (0,1)}
    if len(rows)!=16 or set(mapping)!=expected:
        raise ValueError('Missing or duplicate measurement combinations')
    ratios=[r for r in data['comparisons'] if r['kind']=='quartic_even_band_flux']
    ratio_map={(r['time_window'],r['shell']):r for r in ratios}
    positions=((0,0),(0,1),(1,0),(1,1))
    if len(ratios)!=4 or set(ratio_map)!=set(positions):
        raise ValueError('Missing or duplicate flux ratios')

    fig,axes=plt.subplots(2,1,figsize=(11,8),sharex=True,constrained_layout=True)
    palette={'base':'#0072B2','space':'#009E73','time':'#D55E00'}
    axes[0].axhline(1,color='black',lw=1.4,label='Stationäre Antwort: Verhältnis 1')
    any_failure=False
    for level,eps in combinations:
        values=[]
        for w,s in positions:
            row=mapping[(level,eps,w,s)]
            value=row['Aout_abs']/row['target_abs'] if row['target_abs']>0 else None
            if value is None or not math.isfinite(value):
                raise ValueError('Invalid completed amplitude diagnostic')
            values.append(value)
        axes[0].plot(range(4),values,color=palette[level],lw=1.4,
                     ls=':' if eps==.001 else '-',marker='s' if eps==.001 else 'o',ms=5,
                     label=f'{level}, ε=±{eps:g} (Baseline abgezogen)')
        for x,((w,s),value) in enumerate(zip(positions,values)):
            if not mapping[(level,eps,w,s)]['passed']:
                axes[0].plot(x,value,marker='x',ms=9,mew=1.5,color='#CC3311',ls='none')
                any_failure=True
    if any_failure:
        axes[0].plot([],[],marker='x',ms=8,color='#CC3311',ls='none',label='Mindestens ein Messgate verfehlt')
    axes[0].set_ylabel('|Aout aus Ueven| / |Aout stationär|')
    axes[0].set_title('Quadratische Außenfeldantwort: Ueven bereits durch α² geteilt')
    axes[0].legend(fontsize=8,ncol=2)

    targets=[]; measured=[]; invalid=[]
    for x,key in enumerate(positions):
        row=ratio_map[key]; target=row['expected_ratio']; value=row['measured_ratio']
        if not math.isfinite(target) or target<=0:
            raise ValueError('Invalid expected flux ratio')
        targets.append(target)
        measured.append(value if value is not None and math.isfinite(value) else float('nan'))
        if value is None or not math.isfinite(value):
            invalid.append(x)
    axes[1].plot(range(4),targets,color='black',ls='--',lw=1.4,label='Soll (α₂/α₁)⁴ = 16')
    axes[1].fill_between(range(4),[.8*t for t in targets],[1.2*t for t in targets],
                          color='gray',alpha=.15,label='Vorab-Grenze: ±20 %')
    axes[1].plot(range(4),measured,color='#0072B2',lw=1.4,marker='o',label='Gespeichertes physisches Bandflussverhältnis')
    for x,key in enumerate(positions):
        row=ratio_map[key]
        if x in invalid:
            axes[1].annotate('unaufgelöst / undefiniert',(x,targets[x]),xytext=(0,18),
                             textcoords='offset points',ha='center',color='#CC3311',fontsize=8)
        elif not row['passed']:
            axes[1].plot(x,measured[x],marker='x',ms=10,mew=1.5,color='#CC3311',ls='none')
    axes[1].set_ylabel('F⁽even,2ρ⁾(ε=.002) / F⁽even,2ρ⁾(ε=.001)')
    axes[1].set_title('Basisgitter: quartische Skalierung des paritätsgeraden Bandflusses')
    axes[1].legend(fontsize=8,ncol=2)
    labels=[]
    for w,s in positions:
        row=mapping[('base',.002,w,s)]
        lo,hi=row['radius_window']; left,right=row['window']
        labels.append(f'Fenster {w+1}: t={left:g}…{right:.2f}\nr={lo:g}…{hi:g}')
    axes[1].set_xticks(range(4),labels,fontsize=9)
    for ax in axes:
        ax.grid(alpha=.25); ax.set_xlim(-.2,3.2); ax.set_ylim(bottom=0)
    fig.suptitle(f"{data['status']} — freie M2-Zeitentwicklung bis T=128\n"
                 'Gespeicherte Diagnosen; keine Lebensdauer- oder Dämpfungsmessung',fontsize=13)
    args.out.mkdir(parents=True,exist_ok=False)
    fig.savefig(args.out/'TIME-DOMAIN.png',dpi=160)
    fig.savefig(args.out/'TIME-DOMAIN.svg')
    plt.close(fig)
    (args.out/'PROVENANCE.json').write_text(json.dumps(dict(input_sha256=digest,
        plot_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),original_status=data['status'],
        note='Saved scalar diagnostics only; ratios for display, no new trajectory analysis, fit or gate decision'),indent=2)+'\n')


if __name__=='__main__':
    main()
