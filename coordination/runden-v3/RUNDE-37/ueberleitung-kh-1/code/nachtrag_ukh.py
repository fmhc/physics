#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UEBERLEITUNG-KH-1, Nachtrag nach Sicht (beschreibend, nicht geurteilt, nicht eingefroren).

Anlass: M_eff ist an allen k exakt singulaer (Meff_min_rel <= 7e-16); die Plan-Paarung (a) mit A = M_eff^-1 ist
damit nicht definiert. Hier wird der Grenzfall ohne Legendre-Umkehr der Nullrichtung behandelt:
  N1 Nullraum von M_eff (Lage, Ueberlapp mit der Raumdiagonale 111, Kopplung an C und Shift).
  N2 Passbedingung ohne Inverse: C in Bild(M_eff M_disp)? Dasselbe fuer (K_LR, c).
  N3 affiner Vergleich bei k = 0: 6 x 6 Gram-Matrizen von M_eff und K_LR auf gleichmaessigen Verzerrungsraten gegen G_L.
  N4 reduzierte Grenzdynamik: Nullrichtung u statisch eliminiert (Schur im Potential), Rest R1-artig mit C und M_disp
     (dim 6 - 3 - 1 = 2): omega^2, TT-Spanne (Fit wie ukh), wachsende Moden an Raster und BZ; Vergleich mit
     sum_i 4 sin^2(k_i/2).
Importiert ukh.py (eingefroren) unveraendert.
"""
import argparse, json, sys, os, time, platform, resource
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import ukh  # noqa: E402
import tg  # noqa: E402
import hm  # noqa: E402
import tp  # noqa: E402
import tti  # noqa: E402


def herm(X):
    return 0.5 * (X + np.conj(X.T))


def grenze_tg(vier, mod, ks):
    gf = ukh.grenzform(vier, ks)
    U = ukh.U_matrix(mod, ks)
    T11 = np.eye(11, dtype=complex); T11[:7, :7] = U
    S = np.array([np.conj(T11.T) @ Sp @ T11 for Sp in gf['Q0']])
    Meff = herm(S[2][np.ix_(ukh.IQ, ukh.IQ)])
    Veff = herm(S[0][np.ix_(ukh.IQ, ukh.IQ)])
    Cv = S[0][ukh.IQ, ukh.IN][:, None]
    X = S[1][np.ix_(ukh.IQ, ukh.IB)]
    return Meff, Veff, Cv, X


def rest_proj(Y, x):
    Q, R = np.linalg.qr(Y)
    r = x - Q @ (np.conj(Q.T) @ x)
    return float(np.linalg.norm(r) / max(np.linalg.norm(x), 1e-300))


def punkt(vier, mod, geo, ks, e111):
    eps = float(np.linalg.norm(ks))
    Meff, Veff, Cv, X = grenze_tg(vier, mod, ks)
    Bs, A1s, M, c = tg.ops(mod, ks)
    B = herm(Bs.toarray())
    K_LR = herm(geo['vref'] * hm.assemble(mod, geo['Kt'], ks))
    ev, Uv = np.linalg.eigh(Meff)
    null = np.abs(ev) <= 1e-10 * np.abs(ev).max()
    u = Uv[:, null]
    W = Uv[:, ~null]
    out = {'k': [float(x) for x in ks], 'eps': eps, 'n_null': int(null.sum())}
    out['u_111_anteil'] = float(np.sum(np.abs(u[e111]) ** 2)) if null.any() else None
    out['uC_rel'] = float(np.linalg.norm(np.conj(u.T) @ Cv) / np.linalg.norm(Cv)) if null.any() else None
    out['uX_rel'] = float(np.linalg.norm(np.conj(u.T) @ X) / np.linalg.norm(X)) if null.any() else None
    out['uM_rel'] = float(np.linalg.norm(np.conj(u.T) @ M) / np.linalg.norm(M)) if null.any() else None
    out['Vuu_rel'] = float(abs((np.conj(u.T) @ B @ u)[0, 0]) / np.linalg.norm(B, 2)) if null.any() else None
    # N2
    out['pass_ohne_inv_MC'] = rest_proj(Meff @ M, Cv)
    out['pass_ohne_inv_Kc'] = rest_proj(K_LR @ M, c)
    out['X_in_MeffM'] = rest_proj(Meff @ M, X)
    if out['n_null'] < 1:
        return out
    # N4: Nullrichtungen statisch eliminieren (nt2: auch n_null > 1, wenn V_uu regulaer)
    Vuu = np.conj(u.T) @ B @ u
    evu = np.linalg.eigvalsh(herm(Vuu))
    out['Vuu_kond'] = float(np.abs(evu).max() / max(np.abs(evu).min(), 1e-300))
    if out['Vuu_kond'] > 1e10:
        out['Vuu_singulaer'] = True
        return out
    Vui = np.linalg.inv(Vuu)
    Vp = herm(np.conj(W.T) @ B @ W - (np.conj(W.T) @ B @ u) @ Vui @ (np.conj(u.T) @ B @ W))
    uC = np.conj(u.T) @ Cv
    Cp = np.conj(W.T) @ Cv - (np.conj(W.T) @ B @ u) @ (Vui @ uC)
    out['nn_neu_rel'] = float(abs((np.conj(uC.T) @ Vui @ uC)[0, 0]) / max(np.linalg.norm(Cv) ** 2 / np.linalg.norm(B, 2), 1e-300))
    Mp = herm(np.conj(W.T) @ Meff @ W)
    Mdp = np.conj(W.T) @ M
    out['rang_Mdp'] = int(np.linalg.matrix_rank(Mdp, tol=1e-9 * max(np.linalg.norm(Mdp), 1e-300)))
    S2, Q2, C2, weg, svrel = hm.zerlege(Mdp, Cp)
    Ap = np.linalg.inv(Mp)
    out['pass_reduziert'] = ukh.passdefekt(Ap, Cp, Mdp)
    Ar = herm(np.conj(S2.T) @ Ap @ S2)
    Br = herm(np.conj(S2.T) @ Vp @ S2)
    lam = np.linalg.eigvals(Ar @ Br)
    lam = lam[np.argsort(lam.real)]
    s = max(float(np.abs(lam).max()), 1e-300)
    out['dim_red'] = int(S2.shape[1])
    out['w2'] = [float(x) for x in lam.real]
    out['w2_im_max_rel'] = float(np.abs(lam.imag).max() / s)
    out['w2k2'] = [float(x) / eps ** 2 for x in lam.real]
    out['n_wachsend'] = int(((lam.real < -1e-9 * s) | (np.abs(lam.imag) > 1e-9 * s)).sum())
    out['A_red_eig'] = [float(x) for x in np.linalg.eigvalsh(Ar)]
    out['B_red_eig'] = [float(x) for x in np.linalg.eigvalsh(Br)]
    kub = float(np.sum(4.0 * np.sin(0.5 * np.asarray(ks)) ** 2))
    out['w2_durch_kubisch'] = [float(x) / kub for x in lam.real]
    # mit Code-c statt C (gleiche Richtung erwartet)
    S3 = hm.zerlege(Mdp, np.conj(W.T) @ c)[0]
    lam3 = np.sort(np.linalg.eigvals(herm(np.conj(S3.T) @ Ap @ S3) @ herm(np.conj(S3.T) @ Vp @ S3)).real)
    out['w2_mit_c'] = [float(x) for x in lam3]
    # TT-Anteil der Moden: Ueberlapp mit projizierten affinen TT-Wellen
    return out


def n3_affin(vier, mod, geo):
    ks = np.zeros(3)
    Meff, Veff, Cv, X = grenze_tg(vier, mod, ks)
    K_LR = herm(geo['vref'] * hm.assemble(mod, geo['Kt'], ks))
    V6 = np.einsum('ei,sij,ej->es', mod['n'], tp.B6, mod['n'])
    GM = (V6.T @ Meff @ V6).real
    GK = (V6.T @ K_LR @ V6).real
    GL = np.eye(6) - np.outer(tp.TR, tp.TR)
    ev, Uv = np.linalg.eigh(Meff)
    u = Uv[:, np.abs(ev) <= 1e-10 * np.abs(ev).max()]
    Q, _ = np.linalg.qr(V6)
    u_aff = float(np.linalg.norm(np.conj(Q.T) @ u) ** 2) if u.size else None
    return {'GM_minus_GL_rel': float(np.linalg.norm(GM - GL) / np.linalg.norm(GL)),
            'GK_minus_GL_rel': float(np.linalg.norm(GK - GL) / np.linalg.norm(GL)),
            'GM_eig': [float(x) for x in np.linalg.eigvalsh(GM)], 'GL_eig': [float(x) for x in np.linalg.eigvalsh(GL)],
            'Meff_k0_eig': [float(x) for x in ev], 'KLR_k0_eig': [float(x) for x in np.linalg.eigvalsh(K_LR)],
            'u_affiner_anteil': u_aff, 'u_tg': [[float(np.real(x)), float(np.imag(x))] for x in np.ravel(u)],
            'kanten_tg': [[int(round(y)) for y in mod['n'][e] * mod['l'][e]] for e in range(mod['E'])]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    vier, mod, geo, tb = ukh.bau_alles()
    e111 = [e for e in range(mod['E']) if ukh.DS[mod['zu_DS'][e]] == (1, 1, 1)][0]
    lm = float(mod['l'].mean())
    erg = {'n3': n3_affin(vier, mod, geo), 'e111_tg': e111, 'l_mittel': lm}
    ras = []
    for ir, (nm, d) in enumerate(tti.richtungen13()):
        for kl in ukh.KL_RASTER:
            p = punkt(vier, mod, geo, (kl / lm) * d, e111)
            p.update({'ridx': ir, 'richtung': nm, 'kl': kl})
            ras.append(p)
    erg['raster'] = ras
    bz = []
    for teil in (0, 1):
        for m, ks in ukh.bz_k(teil):
            p = punkt(vier, mod, geo, ks, e111)
            p['m'] = list(m)
            bz.append(p)
    erg['bz'] = bz
    # Spanne (Fit wie ukh) fuer die reduzierte Grenzdynamik
    W = {}
    for p in ras:
        ok = p.get('dim_red') == 2 and p.get('n_wachsend') == 0 and p.get('n_null') == 1 and min(p['w2']) > 0
        W[(p['ridx'], p['kl'])] = (ok, sorted(p['w2k2']) if ok else [np.nan, np.nan])
    w0 = []
    alle_ok = True
    for i in range(13):
        for b in range(2):
            ws = [W[(i, kl)][1][b] for kl in ukh.KL_FIT]
            alle_ok &= all(W[(i, kl)][0] for kl in ukh.KL_FIT)
            if np.all(np.isfinite(ws)):
                w0.append(ukh.fit_kl(ukh.KL_FIT, ws)[0])
    w0 = np.array(w0)
    je = {}
    for kl in ukh.KL_RASTER:
        ww = np.array([W[(i, kl)][1] for i in range(13)], float)
        je['%g' % kl] = float(np.nanmax(ww) / np.nanmin(ww) - 1)
    alle = ras + bz
    def mx(key):
        xs = [p[key] for p in alle if p.get(key) is not None]
        return [float(min(xs)), float(max(xs))] if xs else None
    erg['zusammen'] = {
        'spanne0': float(w0.max() / w0.min() - 1) if len(w0) else None, 'w0_min': float(w0.min()) if len(w0) else None,
        'w0_max': float(w0.max()) if len(w0) else None, 'alle_ok_fit': bool(alle_ok), 'spanne_je_kl': je,
        'k_wachsend_raster': int(sum(p.get('n_wachsend', 0) > 0 for p in ras)),
        'k_wachsend_bz': int(sum(p.get('n_wachsend', 0) > 0 for p in bz)),
        'n_null_verteilung': sorted(set(p['n_null'] for p in alle)),
        'k_reduziert_bz': int(sum('w2' in p for p in bz)), 'k_Vuu_singulaer': int(sum(bool(p.get('Vuu_singulaer')) for p in alle)),
        'dim_red_je_n_null': sorted(set((p['n_null'], p.get('dim_red', -1), p.get('rang_Mdp', -1)) for p in alle)),
        'nn_neu_rel': mx('nn_neu_rel'),
        'dim_red_verteilung': sorted(set(p.get('dim_red', -1) for p in alle)),
        'u_111_anteil': mx('u_111_anteil'), 'uC_rel': mx('uC_rel'), 'uX_rel': mx('uX_rel'), 'uM_rel': mx('uM_rel'),
        'Vuu_rel': mx('Vuu_rel'), 'pass_ohne_inv_MC': mx('pass_ohne_inv_MC'), 'pass_ohne_inv_Kc': mx('pass_ohne_inv_Kc'),
        'X_in_MeffM': mx('X_in_MeffM'), 'pass_reduziert': mx('pass_reduziert'), 'w2_im_max_rel': mx('w2_im_max_rel'),
        'w2_durch_kubisch': [float(min(min(p['w2_durch_kubisch']) for p in alle if 'w2_durch_kubisch' in p)),
                             float(max(max(p['w2_durch_kubisch']) for p in alle if 'w2_durch_kubisch' in p))],
        'w2_mit_c_gegen_C': float(max(max(abs(x - y) / max(abs(y), 1e-300) for x, y in zip(sorted(p['w2_mit_c']),
                                                                                            sorted(p['w2'])))
                                      for p in alle if 'w2_mit_c' in p))}
    res = {'info': {'argv': sys.argv, 'python': platform.python_version(), 'numpy': np.__version__,
                    'skript_sha256': ukh.sha(os.path.abspath(__file__)), 'ukh_sha256': ukh.sha(os.path.abspath(ukh.__file__)),
                    'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(t0))},
           'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    tg.schreibe(a.out, res)
    print('fertig nachtrag laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
