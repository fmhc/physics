from pathlib import Path
import json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent; d=json.loads((P/'results-second-order/RESULT.json').read_text());rows=d['rows'];groups=d['groups']
labels={'N':'Räumlich linear','N2':'Räumlich 2. Ordnung','L':'Lokal linear','P':'Lokales Potentialminimum'}
colors={'reference_chi_over_y0':'#111827','N':'#d97706','N2':'#047857','L':'#7c3aed','P':'#dc2626'}
fig,axes=plt.subplots(1,2,figsize=(11,4.3),layout='constrained')
for ax,g in zip(axes,[.001,.005]):
 row=next(x for x in rows if x['stage']=='grid' and x['eta']==.1 and x['portal_g']==g and x['c8']==0);pr=row['profile']
 for key in ['reference_chi_over_y0','N','N2','L','P']:
  ax.plot(pr['r'],pr[key],label='B13-Referenz' if key=='reference_chi_over_y0' else labels[key],color=colors[key],lw=2 if key in ['reference_chi_over_y0','N2'] else 1.25,ls='-' if key=='reference_chi_over_y0' else '--')
 ax.set(xlim=(0,8),xlabel='r (Modelleinheiten)',ylabel='Higgsabweichung χ / y₀',title=f'g = {g}, η = 0,1, c₈ = 0');ax.grid(alpha=.2)
axes[0].legend(fontsize=8);fig.suptitle('Higgsantwort bei festgehaltenem Singulettprofil · radiales 3D-Modell')
fig.savefig(P/'higgs-profile-vergleich.svg');plt.close(fig)
fig,axes=plt.subplots(1,2,figsize=(11,4.4),layout='constrained');methods=['N','N2','L','P']
for ax,metric,title in zip(axes,['profile_relative_L2','higgs_energy_relative_error'],['Profilfehler (volumengewichtetes L2)','Fehler des Higgs-Energiebeitrags']):
 for g,offset,col in [(.001,-.12,'#2563eb'),(.005,.12,'#b45309')]:
  xs=[];mid=[];lo=[];hi=[]
  for k,m in enumerate(methods):
   vals=[100*x['fine_errors'][metric] for x in groups if x['portal_g']==g and x['method']==m];a,b=min(vals),max(vals);c=(a+b)/2
   xs.append(k+offset);mid.append(c);lo.append(c-a);hi.append(b-c)
  ax.errorbar(xs,mid,yerr=[lo,hi],fmt='o',capsize=5,color=col,label=f'g = {g}')
 ax.axhline(5,color='#dc2626',ls='--',lw=1,label='5-%-Pilotgrenze');ax.set(yscale='log',ylabel='Abweichung (%)',title=title);ax.set_xticks(range(4),['N','N2','L','P']);ax.grid(axis='y',alpha=.2);ax.legend(fontsize=8)
fig.suptitle('Feingitter: Spannweiten über η und c₈ · Balken sind keine Konfidenzintervalle')
fig.savefig(P/'approximation-errors.svg');plt.close(fig)
lines=['| g | Näherung | Profilfehler, % | Fehler Higgsenergie, % | Parametergruppen |','|---|---|---:|---:|---|']
for g in [.001,.005]:
 for m in methods:
  sub=[x for x in groups if x['portal_g']==g and x['method']==m]
  ranges=[]
  for key in ['profile_relative_L2','higgs_energy_relative_error']:
   v=[100*x['fine_errors'][key] for x in sub];ranges.append(f'{min(v):.5f}–{max(v):.5f}')
  lines.append(f'| {g} | {m} | {ranges[0]} | {ranges[1]} | '+', '.join(sorted(set(x['verdict'] for x in sub)))+' (4/4) |')
(P/'TABLE.md').write_text('\n'.join(lines)+'\n')
summary=dict(reference_residual_relative_max=max(x['reference_residual_relative'] for x in rows),grid_box_indicator_max=max(x['observed_grid_box_indicator'] for x in groups),first_elapsed_s=json.loads((P/'results/RESULT.json').read_text())['elapsed_s'],followup_elapsed_s=d['elapsed_s'],gpu_peak_allocated_bytes=d['gpu_peak_allocated_bytes'],N2_all_pass=all(x['verdict']=='brauchbar' for x in groups if x['method']=='N2'))
(P/'REPORT-SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n');print('\n'.join(lines));print(json.dumps(summary))

# Normalize SVG whitespace for repository checks; plot content is unchanged.
for svg in P.glob("*.svg"):
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text().splitlines()) + "\n")
