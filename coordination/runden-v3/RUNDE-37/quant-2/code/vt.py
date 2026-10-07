#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-2, Nachauswertung (nach Sicht, beschreibend): statisches Potential aus der Abhaengigkeit von der Zeitlaenge.

Je Klasse (b, b', r) gilt fuer grosse T: ln C(T) = ln A - T V. Mit den Multihit-Korrelatoren bei beta = 1,42 fuer
Nt = 4, 6, 8 (T = Nt tau) wird V je Klasse aus der Steigung von ln C gegen T bestimmt (gewichtete Gerade ueber die
Nt mit C > 3 Fehler; mindestens Nt = 4 und 6), dann V(r) = u_b + u_b' + sigma r - c/r gefittet (qu2.fit_V).
Fehler: Jackknife, Bin i gleichzeitig in allen Dateien weggelassen (Dateien unabhaengig, gleiche Binzahl).
Aufruf: vt.py AUS DATEI_NT4 DATEI_NT6 DATEI_NT8
"""
import sys, os, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import qu2  # noqa: E402

aus = sys.argv[1]
pf = sys.argv[2:]
R, KL, T, B = None, None, [], []
for p in pf:
    res = json.load(open(p + '.json'))
    z = np.load(p + '.npz')
    r = np.array(res['p_r']); kl = np.array(res['p_klassen'])
    if R is None:
        R, KL = r, kl
    assert np.array_equal(kl, KL)
    T.append(res['Nt'] * res['tau'])
    B.append(z['korm_0'])
T = np.array(T)
nb = min(b.shape[0] for b in B)
B = [b[:nb] for b in B]
M = np.array([b.mean(0) for b in B])                                   # (nT, ncl)
J = np.array([[np.delete(b, i, 0).mean(0) for b in B] for i in range(nb)])   # (nb, nT, ncl)
E = np.sqrt((nb - 1) / nb * ((J - J.mean(0)) ** 2).sum(0))             # (nT, ncl)
sig = M > 3 * E
ok = sig[0] & sig[1]                                                    # Nt = 4 und 6 signifikant


def steigung(Cm, Ce, use):
    V = np.full(Cm.shape[1], np.nan)
    for j in np.where(ok)[0]:
        u = use[:, j]
        x = T[u]; y = np.log(Cm[u, j]); w = (Cm[u, j] / Ce[u, j]) ** 2
        A = np.stack([np.ones_like(x), -x], 1)
        p, *_ = np.linalg.lstsq(A * np.sqrt(w)[:, None], y * np.sqrt(w), rcond=None)
        V[j] = p[1]
    return V


V0 = steigung(M, E, sig)
Vj = np.array([steigung(np.where(J[i] > 0, J[i], np.nan), E, sig & (J[i] > 0)) for i in range(nb)])
Ve = np.sqrt((nb - 1) / nb * np.nansum((Vj - np.nanmean(Vj, 0)) ** 2, 0))
sel = ok & np.isfinite(V0) & (Ve > 0)
nsub = int(KL[:, :2].max()) + 1
out = {'kopf': qu2.kopf(), 'dateien': pf, 'T': T.tolist(), 'n_bins': nb, 'n_klassen': int(len(R)),
       'n_klassen_V': int(sel.sum()), 'n_mit_nt8': int((sel & sig[2]).sum()) if len(T) > 2 else 0,
       'klassen': [[int(KL[j, 0]), int(KL[j, 1]), float(R[j]), float(V0[j]), float(Ve[j])] for j in np.where(sel)[0]],
       'fits': {}}
for rmin in (0.0, 0.3):
    s = sel & (R > rmin)
    for form in ('sc', 'c', 's_cfest'):
        p, chi2, dof = qu2.fit_V(R[s], KL[s, :2], V0[s], Ve[s], nsub, form, c_fest=np.pi / 12)
        pj = [qu2.fit_V(R[s], KL[s, :2], Vj[i][s], Ve[s], nsub, form, c_fest=np.pi / 12)[0]
              for i in range(nb) if np.isfinite(Vj[i][s]).all()]
        err = {}
        for k in p:
            if k.startswith('u'):
                continue
            v = np.array([q[k] for q in pj])
            err[k] = float(np.sqrt((len(v) - 1) / len(v) * ((v - v.mean()) ** 2).sum())) if len(v) > 2 else None
        out['fits']['%s_rmin%.1f' % (form, rmin)] = {'par': {k: p[k] for k in p if not k.startswith('u')}, 'err': err,
                                                     'chi2': chi2, 'dof': dof, 'n': int(s.sum()), 'n_jk': len(pj)}
# gemittelt in r-Bins (nur Anschauung)
edges = np.linspace(0, R.max() + 1e-9, 9)
vb = []
for i in range(8):
    s = sel & (R >= edges[i]) & (R < edges[i + 1])
    if s.any():
        w = 1 / Ve[s] ** 2
        vb.append([float(0.5 * (edges[i] + edges[i + 1])), float((V0[s] * w).sum() / w.sum()), float(np.sqrt(1 / w.sum())),
                   int(s.sum())])
out['V_rbins'] = vb
with open(aus, 'w') as f:
    json.dump(out, f, indent=1)
print(json.dumps({k: out[k] for k in ('n_klassen_V', 'n_mit_nt8', 'fits', 'V_rbins')}), flush=True)
