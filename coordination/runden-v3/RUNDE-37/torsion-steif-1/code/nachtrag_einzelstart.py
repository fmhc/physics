#!/usr/bin/env python3
# NACHTRAG 2 (nach Sicht, 2026-10-05 ab 04:46 CEST): nicht eingefroren, nicht Teil der Urteile.
# Folgerichtige Einzelstart-Wirkung (Start je Gelenk im Tetraeder T[0] der Winkelordnung): Q_s (W = sign(b - a)) UND
# M_s (nur eps_{T0} l_B, Gewicht 1). Frage der Karte ("Artefakt der Mittelung?"): Gilt KX auch hier, und bleibt
# ker Q_s >= J(ker M_s^+) mit Dimension >= 4?
import importlib.machinery
import importlib.util
import json
import sys

import numpy as np

_loader = importlib.machinery.SourceFileLoader('ts', sys.argv[1])
spec = importlib.util.spec_from_loader('ts', _loader)
ts = importlib.util.module_from_spec(spec)
_loader.exec_module(ts)


def build_M_single():
    Mt = []
    for H in ts.HINGES:
        l = H['d'].astype(float)
        L = ts.hat(l)
        j, Rt = H['T'][0]
        Rt = np.array(Rt)
        for (ta, ba, sa) in H['cross']:
            rho_x = np.array(ba)
            blk = sa * L
            for r in range(3):
                for c in range(3):
                    if blk[r, c] != 0:
                        Mt.append((7 + 3 * j + r, 3 * ta + c, blk[r, c], rho_x - Rt))
            for p, (et, va, dv) in enumerate(ts.TET_EDGES[j]):
                vec = 0.5 * sa * (ts.GAMMA[j][p] @ l)
                for c in range(3):
                    if vec[c] != 0:
                        Mt.append((et, 3 * ta + c, vec[c], rho_x - (Rt + va)))
    return Mt


QPs = ts.pack(ts.build_terms('einzel')[0])
MPs = ts.pack(build_M_single())
QPm = ts.pack(ts.build_terms('mittel')[0])
rng = np.random.default_rng(778)
ks = [rng.uniform(-np.pi, np.pi, 3) for _ in range(30)] + [1e-3 * np.array([1, 0.37, 0.61])]


def null_basis(A, tol=1e-9):
    u, s, vh = np.linalg.svd(A)
    r = int(np.sum(s > tol * s[0]))
    return vh[r:].conj().T


rows = []
for k in ks:
    Q = ts.assemble(QPs, (ts.NX, ts.NX), k)
    M = ts.assemble(MPs, (ts.NG, ts.NX), k)
    J, _ = ts.torsionfrei_J(k)
    kx = float(np.linalg.norm(M.conj().T + Q @ J) / np.linalg.norm(M))
    ev, V = np.linalg.eigh(0.5 * (Q + Q.conj().T))
    s = np.max(np.abs(ev))
    K = V[:, np.abs(ev) <= 1e-9 * s]
    N = null_basis(M.conj().T)
    JN = J @ N
    sv = np.linalg.svd(JN, compute_uv=False)
    rJN = int(np.sum(sv > 1e-9 * max(sv[0], 1e-300)))
    res = float(np.linalg.norm(Q @ JN) / max(1e-300, np.linalg.norm(Q) * np.linalg.norm(JN)))
    # Eichpruefung fuer die Einzelstart-Matrix
    H = np.zeros((61, 61), complex)
    H[:25, 25:] = M
    H[25:, :25] = M.conj().T
    H[25:, 25:] = Q
    Z = ts.gauge_vectors(k)
    eich = float(np.linalg.norm(H @ Z) / (np.linalg.norm(H) * np.linalg.norm(Z)))
    evH = np.linalg.eigvalsh(H)
    nH = int(np.sum(np.abs(evH) <= 1e-9 * np.max(np.abs(evH))))
    # Mittel-Q: gleiche Kernvektoren der Mittel-Wirkung? (J(ker M_s^+) gegen ker Q_mittel)
    Qm = ts.assemble(QPm, (ts.NX, ts.NX), k)
    res_m = float(np.linalg.norm(Qm @ JN) / max(1e-300, np.linalg.norm(Qm) * np.linalg.norm(JN)))
    rows.append(dict(k=[float(x) for x in k], KX_s=kx, dimkerQ_s=int(K.shape[1]), dimkerMh_s=int(N.shape[1]), rang_JN=rJN,
                     Qs_JN_res=res, eich_res_s=eich, H_null_s=nH, Qmittel_JNs_res=res_m))
json.dump(dict(einzelstart=rows), open(sys.argv[2], 'w'), indent=1)
print(json.dumps(dict(KX_s_max=max(r['KX_s'] for r in rows), dimkerQ_s=sorted({r['dimkerQ_s'] for r in rows}),
                      dimkerMh_s=sorted({r['dimkerMh_s'] for r in rows}), rang_JN=sorted({r['rang_JN'] for r in rows}),
                      Qs_JN_res_max=max(r['Qs_JN_res'] for r in rows), eich_res_s_max=max(r['eich_res_s'] for r in rows),
                      H_null_s=sorted({r['H_null_s'] for r in rows}), Qmittel_JNs_res_min=min(r['Qmittel_JNs_res'] for r in rows))))
