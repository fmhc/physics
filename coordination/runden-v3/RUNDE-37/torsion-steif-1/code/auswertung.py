#!/usr/bin/env python3
# TORSION-STEIF-1: Auswertung nach PLAN.md Abschn. 5 und 6 (eingefroren mit dem Plan).
# Aufruf: python auswertung.py haupt.json auswertung.json
import json
import sys

import numpy as np

src, dst = sys.argv[1], sys.argv[2]
D = json.load(open(src))
A = {}


def is_gamma(k):
    kk = np.mod(np.array(k) + np.pi, 2 * np.pi) - np.pi
    return bool(np.all(np.abs(kk) < 1e-12))


pts = []      # (set, index, eintrag)
gam = []
for name, lst in D['k'].items():
    for i, r in enumerate(lst):
        (gam if is_gamma(r['k']) else pts).append((name, i, r))

# ---------------- TS0
lin = D['linien']
a_wort = all(c['abw_betrag'] <= 1e-8 and (abs(c['delta']) <= 1e-12 or c['achsfehler'] <= 1e-8) for c in lin)
a_plan_sign = all(c['abw_signed'] <= 1e-8 for c in lin)
flat_ok = all(abs(c['delta']) <= 1e-12 for c in lin if c['eta'] == 0.0 and c['stoer'] == 0.0)
b_wort = all(r['eich_res_trans'] <= 1e-9 and r['eich_rang'] == 21 for _, _, r in pts)
b_plan_rot = all(r['eich_res_rot'] <= 1e-9 for _, _, r in pts)
A['TS0'] = dict(
    a_wortlaut=a_wort, a_plan_vorzeichen=a_plan_sign, a_flach_delta0=flat_ok, b_wortlaut=b_wort, b_plan_drehung=b_plan_rot,
    linien_max_abw_betrag=max(c['abw_betrag'] for c in lin), linien_max_abw_signed=max(c['abw_signed'] for c in lin),
    linien_max_achsfehler=max(c['achsfehler'] for c in lin if abs(c['delta']) > 1e-12),
    linien_max_orth=max(c['orth_fehler'] for c in lin), linien_max_flach_delta=max(abs(c['delta']) for c in lin if c['eta'] == 0.0 and c['stoer'] == 0.0),
    linien_delta_bereich=[min(c['delta'] for c in lin), max(c['delta'] for c in lin)],
    eich_res_trans_max=max(r['eich_res_trans'] for _, _, r in pts), eich_res_rot_max=max(r['eich_res_rot'] for _, _, r in pts),
    eich_rang_werte=sorted({r['eich_rang'] for _, _, r in pts}),
    urteil_wortlaut='eingetroffen' if (a_wort and b_wort) else 'verfehlt',
    urteil_plan='eingetroffen' if (a_wort and a_plan_sign and flat_ok and b_wort and b_plan_rot) else 'verfehlt')

# ---------------- TS1
N0 = [r['Q_neg_null_pos'][1] for _, _, r in pts]
neg_nz = {r['Q_neg_null_pos'][0] for _, _, r in pts if r['Q_neg_null_pos'][1] == 0}
ratios = []
for name, i, r in pts:
    ev = np.abs(np.array(r['Q_eig']))
    ratios.append((float(ev.min() / ev.max()), name, i, r['k']))
ratios.sort()
if all(n >= 1 for n in N0):
    klasse = '(i) Nullband'
elif any(n >= 1 for n in N0) or len(neg_nz) > 1:
    klasse = '(ii) Nullmenge'
else:
    klasse = '(iii) keine'
per_set = {}
for name in D['k']:
    sel = [r for nm, _, r in pts if nm == name]
    if sel:
        per_set[name] = dict(n=len(sel), n_mit_null=sum(r['Q_neg_null_pos'][1] >= 1 for r in sel),
                             traegheiten=sorted({tuple(r['Q_neg_null_pos']) for r in sel}),
                             min_ratio=min(float(np.min(np.abs(r['Q_eig'])) / np.max(np.abs(r['Q_eig']))) for r in sel))
gam_info = [dict(k=r['k'], Q=r['Q_neg_null_pos'], H=r['H_neg_null_pos'], Rss=r['Rss_neg_null_pos'], eich_rang=r['eich_rang']) for _, _, r in gam[:3]]
sym = max(float(np.max(np.abs(np.sort(r['Q_eig']) + np.sort(r['Q_eig'])[::-1]))) for _, _, r in pts)
qmax = max(float(np.max(np.abs(r['Q_eig']))) for _, _, r in pts)
qmin_abs = min(float(np.min(np.abs(r['Q_eig']))) for _, _, r in pts)
A['TS1'] = dict(klasse=klasse, n_k=len(pts), n_k_mit_null=int(sum(n >= 1 for n in N0)), traegheiten_ohne_null=sorted(neg_nz),
                min_ratio=ratios[0][0], min_ratio_wo=[ratios[0][1], ratios[0][2], ratios[0][3]], kleinste5=ratios[:5],
                je_menge=per_set, gamma=gam_info, spektrum_symmetrie_max=sym, Q_max_abs=qmax, Q_min_abs=qmin_abs,
                urteil_wortlaut='eingetroffen' if klasse != '(iii) keine' else 'verfehlt',
                urteil_plan={'(i) Nullband': 'eingetroffen', '(ii) Nullmenge': 'teilweise eingetroffen', '(iii) keine': 'verfehlt'}[klasse])

# ---------------- TS2
NH = [r['H_neg_null_pos'][1] for _, _, r in pts]
rk = [r['eich_rang'] for _, _, r in pts]
negH = sorted({r['H_neg_null_pos'][0] for _, _, r in pts})
ok_null = all(nh == rr for nh, rr in zip(NH, rk))
ok_res = all(r['eich_residuum'] <= 1e-9 for _, _, r in pts)
ident = sum(r['H_neg_null_pos'][1] != 18 + r['Rss_neg_null_pos'][1] + r['Q_neg_null_pos'][1] for _, _, r in pts)
kx = max(r['KX'] for _, _, r in pts)
A['TS2'] = dict(null_gleich_rang=ok_null, eich_res_ok=ok_res, traegheit_H_neg=negH, H_null_werte=sorted(set(NH)),
                identitaet_abweichungen=int(ident), KX_max=kx,
                urteil_wortlaut='eingetroffen' if (ok_null and ok_res and len(negH) == 1) else 'verfehlt',
                urteil_plan_zusatz_ok=bool(ident == 0 and kx <= 1e-9))

# ---------------- Kontrollen
kn = D['KN']
kg = [c['zweite_diff']['0.001']['erste'] / c['zweite_diff']['0.002']['erste'] for c in kn]
A['Kontrollen'] = dict(
    KH_max=max(r['herm_Q'] for _, _, r in pts), KT_max=max(abs(r['Q_trace']) for _, _, r in pts),
    KN_rel=[c['rel_abw'] for c in kn], KN_ok=all(c['rel_abw'] <= 1e-6 for c in kn),
    KG_verhaeltnis=kg, KG_ok=all(abs(v - 0.25) <= 0.01 for v in kg),
    KJ_max=max(r['J_konsistenz'] for _, _, r in pts), KX_max=kx,
    R_herm_max=max(r['R_herm'] for _, _, r in pts), R_JQJ_max=max(r['R_gegen_JQJ'] for _, _, r in pts),
    R_omega_max=max(r['R_omega_norm'] for _, _, r in pts),
    Rss_traegheiten=sorted({tuple(r['Rss_neg_null_pos']) for _, _, r in pts}),
    Rss_klein=[dict(k=float(np.linalg.norm(r['k'])), eig=r['Rss_eig']) for r in D['k']['klein']])

# ---------------- Variante E1 (beschreibend)
A['E1'] = dict(n_k_mit_null=int(sum(r['Q1_neg_null_pos'][1] >= 1 for _, _, r in pts)), n_k=len(pts),
               traegheiten=sorted({tuple(r['Q1_neg_null_pos']) for _, _, r in pts}))

# ---------------- Rahmenenergie (beschreibend)
RA = {}
for name, lst in D['k'].items():
    if not (name.startswith('linie-G') or name == 'klein'):
        continue
    for kap in ('0.0', '0.25', '1.0'):
        sel = [r for r in lst if not is_gamma(r['k'])]
        tr = [tuple(r['rahmen'][kap]['Q_neg_null_pos']) for r in sel]
        wechsel = sum(1 for a, b in zip(tr, tr[1:]) if a[0] != b[0] or a[1] or b[1])
        RA.setdefault(kap, {})[name] = dict(traegheiten=sorted(set(tr)), wechsel_oder_null=wechsel,
                                            min_absmin=min(r['rahmen'][kap]['Q_absmin'] for r in sel),
                                            H_null=sorted({r['rahmen'][kap]['H_neg_null_pos'][1] for r in sel}))
wk = []
for r in D['k']['klein']:
    row = dict(k=float(np.linalg.norm(r['k'])))
    for kap in ('0.0', '0.25', '1.0'):
        w = np.array(r['rahmen'][kap]['weitz_eig'])
        g = np.array(r['rahmen'][kap]['weitz_gram_eig'])
        row[kap] = dict(weitz_max_abs=float(np.max(np.abs(w))), weitz_min=float(np.min(w)),
                        rel_zu_2kappa_gram=(float(np.max(np.abs(np.sort(w) - 2 * float(kap) * np.sort(g)))) / max(1e-300, float(np.max(np.abs(w))))) if float(kap) > 0 else None)
    wk.append(row)
RA['weitzenboeck_klein'] = wk
A['Rahmenenergie'] = RA

# Linienprofile (beschreibend): min|lambda|/max|lambda| von Q an 9 Punkten je Linie
prof = {}
for name, lst in D['k'].items():
    if name.startswith('linie-'):
        idx = np.linspace(0, len(lst) - 1, 9).astype(int)
        prof[name] = [(round(float(np.linalg.norm(lst[i]['k'])), 4), float(np.min(np.abs(lst[i]['Q_eig'])) / np.max(np.abs(lst[i]['Q_eig']))),
                       lst[i]['Q_neg_null_pos']) for i in idx]
A['Linienprofile_Q'] = prof

json.dump(A, open(dst, 'w'), indent=1, default=lambda o: o if not isinstance(o, tuple) else list(o))
print(json.dumps(dict(TS0=[A['TS0']['urteil_wortlaut'], A['TS0']['urteil_plan']], TS1=[A['TS1']['urteil_wortlaut'], A['TS1']['urteil_plan'], A['TS1']['klasse']],
                      TS2=[A['TS2']['urteil_wortlaut'], A['TS2']['urteil_plan_zusatz_ok']], KN_ok=A['Kontrollen']['KN_ok'], KG_ok=A['Kontrollen']['KG_ok'])))
