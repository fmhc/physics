#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PUMPE-NETZ-1, zweiter Nachtrag nach Sicht (beschreibend, aendert kein Urteil).

Frage: Wie viel der Abweichung G_rad/G_N in H1 kommt aus den Nicht-TT-Anteilen der (nicht erhaltenen) phi-Quelle, und
wie gross waere die Abweichung fuer eine erhaltene, spurfreie Doppelstern-Quelle (S_c = (u + i w)(u + i w)^T, Kreisbahn)?
Kompakte Quelle (k R -> 0): Kantenkraft sigma_e = Summe Q_zp : (S - tr(S) 1) mal e^(i k.m_e) (nachtrag_iso.Q_map),
statische Kopplung an die zwei weichen Moden von B_red (= dynamische bei J_iso, KD in H1), Winkelmittel 10 x 20, kl = 0,01.
Je Quelle: volle Spannung S und nur ihr TT-Anteil Lambda_n[S] je Richtung.
pn.py, ew.py, mn.py, nachtrag_iso.py unveraendert importiert.
Aufruf: python nachtrag_doppelstern.py --out nachtrag/doppelstern.json
"""
import argparse, json, sys, time, platform, os, resource, hashlib, math
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ew  # noqa: E402
import mn  # noqa: E402
import pn  # noqa: E402
import nachtrag_iso as ni  # noqa: E402

LP, VCELL = pn.LP, pn.VCELL


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def lam_proj(n, S):
    P = np.eye(3) - np.outer(n, n)
    PSP = P @ S @ P
    return PSP - 0.5 * P * np.trace(P @ S)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'host': platform.node(), 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'argv': sys.argv, 'skript_sha256': sha(os.path.abspath(__file__)), 'pn_sha256': sha(os.path.abspath(pn.__file__)),
            'ni_sha256': sha(os.path.abspath(ni.__file__))}
    mod = ew.baue('V')
    tder = pn.tet_ableitungen(mod)
    Q = ni.Q_map(mod, tder)
    quellen = {}
    for nm, v in (('001', [0, 0, 1]), ('111', [1, 1, 1]), ('110', [1, 1, 0]), ('123', [1, 2, 3])):
        m = np.array(v, float) / np.linalg.norm(v)
        u = np.cross(m, [0.3, 0.5, 0.7])
        u /= np.linalg.norm(u)
        w = np.cross(m, u)
        quellen['bahn_' + nm] = np.outer(u + 1j * w, u + 1j * w)
    for nm, ach in pn.ACHSEN:
        q = pn.quelle(mod, tder, ach)
        quellen['phi_' + nm] = q['S0'].astype(complex)
        quellen['phi_' + nm + '_spurfrei'] = pn.tf(q['S0']).astype(complex)
    nd, wd = pn.richtungen(10, 20)
    kl = 0.01
    s = kl / LP
    res = {k_: {'lat': 0.0, 'lat_nurTT': 0.0, 'E': 0.0} for k_ in quellen}
    for i0 in range(0, len(nd), 50):
        nn = nd[i0:i0 + 50]
        ww = wd[i0:i0 + 50]
        k = s * nn
        o = ew.ops(mod, k)
        B, M, c = o['B'], o['M'], o['c']
        U, sv, _ = np.linalg.svd(np.concatenate([M, c], -1))
        S = U[:, :, 40:]
        Bred = pn.herm(pn.cT(S) @ B @ S)
        lb, Vb = np.linalg.eigh(Bred)
        ph = np.exp(1j * (k @ mod['mitte'].T))
        for nm, Sc in quellen.items():
            for j in range(len(nn)):
                for art, T in (('lat', Sc), ('lat_nurTT', lam_proj(nn[j], Sc))):
                    Mx = T - np.trace(T) * np.eye(3)
                    sig = np.einsum('eij,ij->e', Q, Mx) * ph[j]
                    pr = np.conj(Vb[j][:, :2].T) @ (np.conj(S[j].T) @ (-sig))
                    res[nm][art] += ww[j] * float((np.abs(pr) ** 2 / lb[j, :2]).sum())
                L_ = lam_proj(nn[j], Sc)
                res[nm]['E'] += ww[j] * 4 * VCELL ** 2 * float(np.real(np.sum(L_ * np.conj(Sc)))) / s ** 2
    out = {'info': info, 'kl': kl, 'quellen': {}}
    for nm, r in res.items():
        Sc = quellen[nm]
        out['quellen'][nm] = {'G_rad_ueber_G_voll': r['lat'] / r['E'], 'G_rad_ueber_G_nurTT': r['lat_nurTT'] / r['E'],
                              'spur_abs': float(abs(np.trace(Sc))), 'norm_TF': float(np.linalg.norm(Sc - np.trace(Sc) / 3 * np.eye(3)))}
    out['laufzeit_s'] = time.time() - t0
    out['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    out['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(out, f, indent=1)
    os.replace(a.out + '.tmp', a.out)
    print('fertig nachtrag_doppelstern laufzeit %.1f s' % out['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
