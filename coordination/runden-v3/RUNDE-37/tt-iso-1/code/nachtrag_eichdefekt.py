#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TT-ISO-1, Nachtrag nach dem Einfrieren (Zusatz der Leitung, 22:1x CEST; beschreibend, kein Urteil).

Spur-Eichdefekt je Ecke v: |(1 - P_M) A c_v| / |A c_v|, Definition wie ew.py Z. 397-401 (P_M ueber QR von M).
Punkte: |k| = 0,1; 0,01; 0,001 laengs [100] und laengs z0 = ew.richtungen()[3] (Saat 3, im Hauptlauf schon fest).
Faelle (Netz V): Hauptlauf A1R1 (J = 1, g = 1); TB1-Bestwahl je Paarung (g = 1); TB2-Bestwahl je Paarung (J, g).
A ist die volle Bewegungsmatrix der Wahl (A1R1/A2R1: sum J_t A0_t bzw. mit V_F/V_t; A3R2: A = (sum J_t K_t)^-1),
c = c_g (tti.c_gew). Benutzt tti.py (eingefroren 20261004-221441), ew.py, nachtrag_kinetik.py, tp.py unveraendert.
"""
import argparse, json, sys, os, time, hashlib, platform
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ew  # noqa: E402
import tti  # noqa: E402

KS = (0.1, 0.01, 0.001)


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def defekt(netz, kk, J, gk, paarung):
    ba = tti.basis(netz, kk[None, :])
    gvec = np.array([gk[a] for a in netz.kart], float)
    c = tti.c_gew(netz.mod, ba['B'], ba['k'], gvec)[0]
    w = {'A1R1': 0, 'A2R1': 1, 'A3R2': 2}[paarung]
    T = sum(J[i] * ba['teile'][a][w][0] for i, a in enumerate(netz.arten))
    A = np.linalg.inv(T) if paarung == 'A3R2' else T
    M = ba['M'][0]
    Q, _ = np.linalg.qr(M)
    Ac = A @ c
    rest = Ac - Q @ (np.conj(Q.T) @ Ac)
    d = np.linalg.norm(rest, axis=0) / np.maximum(np.linalg.norm(Ac, axis=0), 1e-300)
    sv = np.linalg.svd(M, compute_uv=False)
    gesamt = float(np.linalg.norm(rest) / max(np.linalg.norm(Ac), 1e-300))
    # Summe ueber alle Ecken = globale Dilatationswelle (Bloch-Konvention von ew), Gegenstueck zum Netz ohne Fuellung
    As = Ac.sum(axis=1)
    rs = As - Q @ (np.conj(Q.T) @ As)
    summe = float(np.linalg.norm(rs) / max(np.linalg.norm(As), 1e-300))
    return d, float(sv.min() / sv.max()), (gesamt, summe)


def fall(netz, J, gk, paarung):
    out = {}
    for nm, d in (ew.richtungen()[0], ew.richtungen()[3]):
        zeilen = []
        for kb in KS:
            dv, sv, ges = defekt(netz, kb * d, J, gk, paarung)
            zeilen.append({'k': kb, 'max': float(dv.max()), 'median': float(np.median(dv)), 'je_ecke': dv.tolist(),
                           'M_sv_min_rel': sv, 'gesamt_frobenius': ges[0], 'summe_dilatation': ges[1]})
        for z0, z1 in zip(zeilen[:-1], zeilen[1:]):
            z1['potenz_summe'] = float(np.log(z1['summe_dilatation'] / z0['summe_dilatation']) / np.log(z1['k'] / z0['k']))
            z1['potenz_max'] = float(np.log(z1['max'] / z0['max']) / np.log(z1['k'] / z0['k']))
            z1['potenz_median'] = float(np.log(z1['median'] / z0['median']) / np.log(z1['k'] / z0['k']))
        out[nm] = {'richtung': d.tolist(), 'zeilen': zeilen}
    return out




def g_diagnose(netz):
    """Warum ist g != 1 ungueltig? B_red-Traegheit und Gueltigkeit (A1R1, J = 1) an [100], |k| = 1e-3, 2e-3."""
    d = ew.richtungen()[0][1]
    kp = np.array([1e-3 * d, 2e-3 * d])
    ee = np.array([1e-3, 2e-3])
    ba = tti.basis(netz, kp)
    out = []
    for a in netz.frei_kanten:
        for y in (-1.0, -0.05, 0.05, 1.0):
            gk = tti.g_eins(netz)
            gk[a] = float(10.0 ** y)
            gvec = np.array([gk[b] for b in netz.kart], float)
            c = tti.c_gew(netz.mod, ba['B'], ba['k'], gvec)
            zeile = {'kantenart': a, 'log10_g': y, 'B_red_neg': [], 'dim': []}
            for j in range(len(kp)):
                U, r, s = ew.phys_basis_rr(ba['M'][j], c[j])
                S = U[:, r:]
                Br = np.conj(S.T) @ ba['B'][j] @ S
                eB = np.linalg.eigvalsh(0.5 * (Br + np.conj(Br.T)))
                zeile['B_red_neg'].append(int((eB <= 0).sum()))
                zeile['dim'].append(int(S.shape[1]))
            pr = tti.prep(netz, ba, gk)
            w, neg, lu, ok = tti.auswerten(pr, ee, 'A1R1', np.ones((1, len(netz.arten))))
            zeile.update({'ok': bool(ok[0]), 'neg_k': int(neg[0]), 'luecke': float(lu[0])})
            out.append(zeile)
    return out
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lauf', required=True, help='Ordner mit verf-V-*.json')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    netz = tti.Netz('V')
    res = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'tti_sha256': sha(os.path.abspath(tti.__file__)),
                    'ew_sha256': sha(os.path.abspath(ew.__file__)), 'numpy': np.__version__, 'host': platform.node(),
                    'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'z0': ew.richtungen()[3][1].tolist()},
           'faelle': {}}
    res['faelle']['hauptlauf_A1R1_J1'] = fall(netz, np.ones(len(netz.arten)), tti.g_eins(netz), 'A1R1')
    nJ = len(netz.frei_arten)
    for p in tti.PAARUNGEN:
        pfad = os.path.join(a.lauf, 'verf-V-%s.json' % p)
        if not os.path.exists(pfad):
            res['faelle']['fehlt_' + p] = pfad
            continue
        res['info']['verf_%s_sha256' % p] = sha(pfad)
        with open(pfad) as fh:
            v = json.load(fh)['ergebnis']
        J1 = netz.J_aus_log(np.array(v['tb1_best']['x']))[0]
        res['faelle']['tb1_' + p] = fall(netz, J1, tti.g_eins(netz), p)
        z = np.array(v['tb2_best']['z'])
        J2 = netz.J_aus_log(z[:nJ])[0]
        g2 = netz.g_aus_log(z[nJ:])
        res['faelle']['tb2_' + p] = fall(netz, J2, g2, p)
    res['g_diagnose_V'] = g_diagnose(netz)
    res['laufzeit_s'] = time.time() - t0
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1)
    os.replace(a.out + '.tmp', a.out)
    print('fertig nachtrag eichdefekt laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
