#!/usr/bin/env python3
# NACHTRAG (nach Sicht der Hauptergebnisse, 2026-10-05 ab 04:42 CEST): nicht eingefroren, nicht Teil der Urteile.
# (1) Herkunft der 4 Nullmoden von Q(k): Ist ker Q = J(ker M^+)? Zaehlung 25 Geometrie- gegen 21 gemittelte Gelenkvektor-
#     Komponenten (Hypothese nach Sicht).
# (2) TS0 flache Faelle: Drehwinkel per atan2 statt arccos (Genauigkeit bei psi -> 0).
# Nutzt die eingefrorenen Funktionen aus torsion_steif.py.eingefroren-20261005-043849 (nur gelesen).
import importlib.util
import json
import sys

import numpy as np

import importlib.machinery
_loader = importlib.machinery.SourceFileLoader('ts', sys.argv[1])
spec = importlib.util.spec_from_loader('ts', _loader)
ts = importlib.util.module_from_spec(spec)
_loader.exec_module(ts)
out = {}
QP_t, MP_t = ts.build_terms('mittel')
QP, MP = ts.pack(QP_t), ts.pack(MP_t)
QP1 = ts.pack(ts.build_terms('einzel')[0])
rng = np.random.default_rng(777)
ks = [rng.uniform(-np.pi, np.pi, 3) for _ in range(40)]
ks += [np.pi * q * np.array([1, 0, 0]) for q in (0.3, 0.7)] + [np.pi * q * np.array([1, 1, 1]) for q in (0.3, 0.7)]
ks += [np.pi * q * np.array([1, 1, 0]) for q in (0.3, 0.7)] + [1e-3 * np.array([1, 0.37, 0.61])]


def null_basis(A, tol=1e-9):
    u, s, vh = np.linalg.svd(A)
    r = int(np.sum(s > tol * s[0]))
    return vh[r:].conj().T


rows = []
for k in ks:
    Q = ts.assemble(QP, (ts.NX, ts.NX), k)
    M = ts.assemble(MP, (ts.NG, ts.NX), k)
    J, _ = ts.torsionfrei_J(k)
    ev, V = np.linalg.eigh(0.5 * (Q + Q.conj().T))
    s = np.max(np.abs(ev))
    K = V[:, np.abs(ev) <= 1e-9 * s]                     # ker Q
    N = null_basis(M.conj().T)                            # ker M^+ (25 x n)
    JN = J @ N
    sv = np.linalg.svd(JN, compute_uv=False)
    rJN = int(np.sum(sv > 1e-9 * max(sv[0], 1e-300)))
    # Hauptwinkel zwischen span(J N) und ker Q
    if K.shape[1] and rJN:
        Uj, sj, _ = np.linalg.svd(JN)
        Uj = Uj[:, :rJN]
        c = np.linalg.svd(Uj.conj().T @ K, compute_uv=False)
        max_sin = float(np.sqrt(max(0.0, 1 - np.min(c) ** 2))) if len(c) else None
    else:
        max_sin = None
    # Anteil ds gegen Omega in ker M^+ ohne Translationen (Projektion weg von den 3 Translationsvektoren)
    Z = ts.gauge_vectors(k)[:ts.NG, 18:]
    Pt = np.eye(ts.NG) - Z @ np.linalg.pinv(Z)
    Nr = Pt @ N
    ds_anteil = float(np.linalg.norm(Nr[:7]) / max(1e-300, np.linalg.norm(Nr)))
    # Variante E1: enthaelt ker Q_E1 ebenfalls J(ker M^+)?
    Q1 = ts.assemble(QP1, (ts.NX, ts.NX), k)
    e1_res = float(np.linalg.norm(Q1 @ JN) / max(1e-300, np.linalg.norm(Q1) * np.linalg.norm(JN)))
    rows.append(dict(k=[float(x) for x in k], dimkerQ=int(K.shape[1]), dimkerMh=int(N.shape[1]), rang_JN=rJN,
                     max_sin_JN_gegen_kerQ=max_sin, ds_anteil_ohne_transl=ds_anteil, Q_JN_res=float(np.linalg.norm(Q @ JN) / max(1e-300, np.linalg.norm(Q) * np.linalg.norm(JN))),
                     E1_Q1_JN_res=e1_res))
out['kern'] = rows

# (2) flache Faelle, Winkel per atan2
flach = []
for e_idx in range(7):
    H = ts.HINGES[e_idx]
    d = H['d']
    P0, P1 = (0, 0, 0), tuple(int(c) for c in d)
    m = H['m']
    Ws = []
    for kk in range(m):
        tau, base, sig = H['cross'][kk]
        a, b = ts.TRIS[tau]
        tri = [tuple(int(c) for c in base), tuple(int(c) for c in base + a), tuple(int(c) for c in base + a + b)]
        Ws.append([w for w in tri if w not in (P0, P1)][0])
    rr = np.random.default_rng(1)
    emb = []
    for kk, (j, Rt) in enumerate(H['T']):
        order = [P0, P1, Ws[kk - 1], Ws[kk]]
        S4 = np.array([[float(np.sum((np.array(order[a]) - np.array(order[b])) ** 2)) for b in range(4)] for a in range(4)])
        X = ts.cm_embed(S4)
        Lam = ts.random_rotation(rr)
        emb.append({order[i]: Lam @ X[i] for i in range(4)})
    P = np.eye(3)
    for kk in range(m):
        C0, C1 = emb[kk], emb[(kk + 1) % m]
        w = Ws[kk]
        F0 = np.column_stack([C0[P1] - C0[P0], C0[w] - C0[P0], np.cross(C0[P1] - C0[P0], C0[w] - C0[P0])])
        F1 = np.column_stack([C1[P1] - C1[P0], C1[w] - C1[P0], np.cross(C1[P1] - C1[P0], C1[w] - C1[P0])])
        P = F1 @ np.linalg.inv(F0) @ P
    psi_atan = float(np.arctan2(np.linalg.norm(ts.vee(P - P.T)) / 2, (np.trace(P) - 1) / 2))
    psi_acos = float(np.arccos(np.clip((np.trace(P) - 1) / 2, -1, 1)))
    flach.append(dict(kante=d.tolist(), psi_atan2=psi_atan, psi_arccos=psi_acos, eins_minus_c=float(1 - (np.trace(P) - 1) / 2)))
out['flach'] = flach
json.dump(out, open(sys.argv[2], 'w'), indent=1)
print(json.dumps(dict(dimkerQ=sorted({r['dimkerQ'] for r in rows}), dimkerMh=sorted({r['dimkerMh'] for r in rows}),
                      rang_JN=sorted({r['rang_JN'] for r in rows}), max_sin=max(r['max_sin_JN_gegen_kerQ'] or 0 for r in rows),
                      Q_JN_res=max(r['Q_JN_res'] for r in rows), E1_res=max(r['E1_Q1_JN_res'] for r in rows),
                      flach_psi_atan2_max=max(abs(f['psi_atan2']) for f in flach))))
