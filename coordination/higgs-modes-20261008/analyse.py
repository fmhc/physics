from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent;rows=json.loads((P/'results/RESULT.json').read_text());qa=json.loads((P/'results/QA.json').read_text());assert len(rows)==24
symchecks=[];sectors=[]
for sector,ell in [('imag',0),('real',1)]:
 rr={x['stage']:x for x in rows if x['sector']==sector and x['ell']==ell}
 idx={s:max(range(8),key=lambda i:x['symmetry_overlap_squared'][i]) for s,x in rr.items()}
 overlaps={s:x['symmetry_overlap_squared'][idx[s]] for s,x in rr.items()};vals={s:x['eigenvalues'][idx[s]] for s,x in rr.items()}
 passed=min(overlaps.values())>.95 and (max(abs(v) for v in vals.values())<1e-6 if sector=='imag' else (abs(vals['grid'])<=.4*abs(vals['base'])+1e-6 and abs(vals['box']-vals['base'])<=max(.1*abs(vals['base']),1e-6)))
 symchecks.append(dict(sector=sector,ell=ell,passed=passed,indices=idx,overlaps=overlaps,eigenvalues=vals))
for ell in range(4):
 for sector in ['real','imag']:
  rr={x['stage']:x for x in rows if x['sector']==sector and x['ell']==ell};sym=next((s for s in symchecks if s['sector']==sector and s['ell']==ell),None)
  vals={s:min(v for i,v in enumerate(x['eigenvalues']) if sym is None or not sym['passed'] or i!=sym['indices'][s]) for s,x in rr.items()}
  drift=max(abs(vals[s]-vals['base']) for s in ['grid','box']);mn=min(vals.values());mx=max(vals.values());verdict='positiv aufgeloest' if mn-2*drift>1e-6 else ('negativ aufgeloest' if mx+2*drift< -1e-6 else 'unentschieden')
  if sym is not None and not sym['passed']:verdict='unentschieden'
  sectors.append(dict(ell=ell,sector=sector,eigenvalues_excluding_identified_symmetry=vals,drift=drift,verdict=verdict))
s=dict(symmetry_checks=symchecks,sectors=sectors,max_hvp_error=max(q['hvp_relative_error'] for q in qa),max_eigen_residual=max(q['eigen_residual_max'] for q in qa),max_orthogonality_error=max(q['orthogonality_max'] for q in qa),max_phase_ward=max(x.get('phase_ward_residual',0) for x in rows))
(P/'SUMMARY.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(s,indent=2))
print('fine antisymmetric modes',json.dumps([dict(ell=x['ell'],sector=x['sector'],modes=[dict(eigenvalue=x['eigenvalues'][i],weight=w) for i,w in enumerate(x['antisymmetric_matter_weight']) if w>.9]) for x in rows if x['stage']=='grid'],indent=2))
plt.rcParams.update({'svg.fonttype':'none','font.size':11})
fig,axs=plt.subplots(1,2,figsize=(11.5,4.5),layout='constrained')
for sector,color in [('real','#257ca3'),('imag','#c07526')]:
 ss=[s for s in sectors if s['sector']==sector];vals=[s['eigenvalues_excluding_identified_symmetry']['grid'] for s in ss]
 lo=[v-min(s['eigenvalues_excluding_identified_symmetry'].values()) for s,v in zip(ss,vals)];hi=[max(s['eigenvalues_excluding_identified_symmetry'].values())-v for s,v in zip(ss,vals)]
 axs[0].errorbar(range(4),vals,yerr=[lo,hi],fmt='o-',capsize=4,label='Amplitude + Higgs' if sector=='real' else 'Phase',color=color)
axs[0].axhline(0,color='black',lw=1);axs[0].set_xticks(range(4));axs[0].set_xlabel('Winkelordnung l');axs[0].set_ylabel('Energiekrümmung λ (dimensionslos)');axs[0].set_title('Niedrigste Krümmung ohne Symmetrierichtung');axs[0].legend(fontsize=9)
for sym,color,label in [(symchecks[0],'#c07526','Gemeinsame Phase'),(symchecks[1],'#257ca3','Translation')]:
 axs[1].plot([0,1,2],[abs(sym['eigenvalues'][s]) for s in ['base','grid','box']],'o-',label=label,color=color)
axs[1].set_yscale('log');axs[1].set_xticks([0,1,2],['Basis','feiner','größere Box']);axs[1].set_ylabel('|λ|');axs[1].set_title('Identifizierte Symmetrierichtungen');axs[1].legend(fontsize=9)
for ax in axs:ax.grid(alpha=.2)
fig.suptitle('HIGGS-MODES-1 · volle Portaltheorie bei fester Ladung')
fig.supxlabel('Links: feines Gitter mit Gitter-/Boxspanne · keine Zeitentwicklungsfrequenzen',fontsize=10)
fig.savefig(P/'mode-spectrum.svg',metadata={'Date':None});p=P/'mode-spectrum.svg';p.write_text('\n'.join(l.rstrip() for l in p.read_text().splitlines())+'\n')
