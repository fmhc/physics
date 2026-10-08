import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent;rows=json.loads((P/'results/RESULT.json').read_text());cc=json.loads((P/'results/COMPARISONS.json').read_text());qa=json.loads((P/'results/QA.json').read_text());assert len(rows)==18 and len(cc)==12
phase=[dict(stage=x['stage'],method=x['method'],eigenvalue=x['eigenvalues'][0],overlap=x['phase_overlap_squared'][0],passed=x['phase_overlap_squared'][0]>.95 and abs(x['eigenvalues'][0])<1e-6) for x in rows if x['sector']=='imag']
groups=[]
for method in ['E3','Ecomp']:
 errors=[x for x in cc if x['method']==method];mx=max(v for x in errors for v in x['relative_eigenvalue_errors'])
 drift=max(abs(v-next(y['relative_eigenvalue_errors'][i] for y in errors if y['stage']=='base' and y['sector']==x['sector'])) for x in errors for i,v in enumerate(x['relative_eigenvalue_errors']))
 positive=all(min(x['eigenvalues'][1:] if x['sector']=='imag' else x['eigenvalues'])>1e-6 for x in rows if x['method'] in ['full',method]);phaseok=all(x['passed'] for x in phase if x['method'] in ['full',method])
 verdict='bestanden' if positive and phaseok and mx+drift<=.05 and drift<=.005 else 'unentschieden'
 groups.append(dict(method=method,maximum_relative_spectral_error=mx,drift=drift,nontrivial_positive=positive,phase_passed=phaseok,verdict=verdict,minimum_eigenvector_overlap_squared=min(v for x in errors for v in x['eigenvector_overlap_squared']),maximum_operator_relative_frobenius=max(x['operator_relative_frobenius'] for x in errors)))
s=dict(groups=groups,phase_checks=phase,minimum_higgs_block_eigenvalue=min(x['higgs_block_minimum'] for x in qa if x['method']=='full'),max_schur_solve_residual=max(x['schur_solve_relative_residual'] for x in qa if x['method']=='full'),max_raw_asymmetry=max(x['raw_hessian_asymmetry_max'] for x in qa),max_finite_difference_error=max(v[-1] for x in qa if x['method']!='full' for v in x['finite_difference_relative_errors'].values()),max_eigen_residual=max(x['eigen_residual_max'] for x in rows),max_orthogonality=max(x['orthogonality_max'] for x in rows))
(P/'SUMMARY.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(s,indent=2))
plt.rcParams.update({'svg.fonttype':'none','font.size':11})
fig,axs=plt.subplots(1,2,figsize=(11,4.5),layout='constrained')
for ax,sector,title in [(axs[0],'real','Radiale Amplituden'),(axs[1],'imag','Radiale Phasen, ohne gemeinsame Drehung')]:
 for method,color in [('E3','#c17827'),('Ecomp','#18826b')]:
  fine=next(x for x in cc if (x['method'],x['sector'],x['stage'])==(method,sector,'grid'))
  vals=[100*v for v in fine['relative_eigenvalue_errors']];other=[x for x in cc if x['method']==method and x['sector']==sector]
  lo=[v-min(100*x['relative_eigenvalue_errors'][i] for x in other) for i,v in enumerate(vals)];hi=[max(100*x['relative_eigenvalue_errors'][i] for x in other)-v for i,v in enumerate(vals)]
  ax.errorbar(range(1,len(vals)+1),vals,yerr=[lo,hi],fmt='o-',capsize=3,label=method,color=color)
 ax.set_yscale('log');ax.set_xlabel('Sortierter nichttrivialer Eigenwert');ax.set_ylabel('Relativer Fehler [%]');ax.set_title(title,fontsize=11);ax.grid(alpha=.2);ax.legend()
fig.suptitle('Reduzierte Higgsmodelle · statische radiale Energiekrümmung')
fig.supxlabel('Vergleich mit voller statischer Higgs-Mitreaktion · feines Gitter mit Gitter-/Boxspanne',fontsize=10)
fig.savefig(P/'reduced-mode-errors.svg',metadata={'Date':None});p=P/'reduced-mode-errors.svg';p.write_text('\n'.join(l.rstrip() for l in p.read_text().splitlines())+'\n')
