#!/usr/bin/env python3
"""zweifeld_n4.py - PLAN-NACHTRAG-4 (nachtraeglich, Diagnose und Lokalisierung entlang der geschlossenen Kurve).

Je Vorzeichenwechsel von s aus Detektor 1 (Paar w2a -> w2b auf einer Kurve m_a = 0):
  Stufe L = 0..7: 9 w^2-Werte gleichmaessig in der aktuellen Klammer; je w^2 Nullstelle von m_a in
  [rho_guess -+ 0,0015] (Illinois, 1e-11); s mit eta, ausgerichtet am eta der Zeile w2a; neue Klammer = Intervall mit
  Vorzeichenwechsel von s. Klammer schrumpft je Stufe um 8 (Ende ~1e-10 in w^2).
  Danach Umlauf von W2 (zeroth: zweifeld_n2.umlaeufe_n2, Halbbreite 1e-3, 40 Runden) um den lokalisierten Punkt.
Ausgegeben wird s auf jeder Stufe, damit sichtbar ist, ob s stetig durch 0 geht oder springt.
Aufruf: kurve <modell> <stufe> <npz> <ausdatei> <kandidatendatei-json (n3w2)> <index ...>
"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
import json
import time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zweifeld as Z
import zweifeld_n2 as N2
import zweifeld_n3 as N3  # noqa: F401  (Monkeypatch der robusten Fortsetzung)


def ma_s(modell, lin, cache, w2, rho):
    r = Z.punkte(modell, lin, cache, w2, rho)
    return r['ma'], r['s'], r['eta']


def nullstellen_kurve(modell, lin, cache, w2, rg, halb=0.0015):
    lo = rg - halb
    hi = rg + halb
    flo, _, _ = ma_s(modell, lin, cache, w2, lo)
    fhi, _, _ = ma_s(modell, lin, cache, w2, hi)
    ok = np.sign(flo) * np.sign(fhi) < 0
    rl, rr, fl, fr = lo.copy(), hi.copy(), flo.copy(), fhi.copy()
    rl[~ok] = rg[~ok] - 1e-9
    rr[~ok] = rg[~ok] + 1e-9
    fl[~ok] = -1.0
    fr[~ok] = 1.0

    def fe(x):
        return ma_s(modell, lin, cache, w2, x)[0]

    wur, br = Z.illinois(fe, rl, rr, fl, fr, iters=30, tol=1e-11)
    ma, s, eta = ma_s(modell, lin, cache, w2, wur)
    return wur, ma, s, eta, ok


def verfolge(modell, lin, cache, paar, eta_ref, stufen=8, n=9):
    w2a, w2b, ra, rb = paar['w2a'], paar['w2b'], paar['ra'], paar['rb']
    verlauf = []
    for L in range(stufen):
        w2 = np.linspace(w2a, w2b, n)
        rg = ra + (rb - ra) * (w2 - w2a) / (w2b - w2a)
        wur, ma, s, eta, ok = nullstellen_kurve(modell, lin, cache, w2, rg)
        flip = np.where(np.sum(eta * eta_ref[None, :], axis=1) >= 0, 1.0, -1.0)
        so = flip * s
        verlauf.append(dict(stufe=L, w2=w2.tolist(), rho=wur.tolist(), s=so.tolist(), ma=ma.tolist(),
                            klammer_ok=ok.tolist()))
        wechsel = np.nonzero(np.sign(so[:-1]) * np.sign(so[1:]) < 0)[0]
        if len(wechsel) == 0:
            return verlauf, None
        i = int(wechsel[0])
        w2a, w2b, ra, rb = float(w2[i]), float(w2[i + 1]), float(wur[i]), float(wur[i + 1])
        eta_ref = flip[i] * eta[i]
        sa, sb = so[i], so[i + 1]
        verlauf[-1]['wechsel_index'] = i
        verlauf[-1]['anzahl_wechsel'] = int(len(wechsel))
    t = abs(sa) / (abs(sa) + abs(sb))
    return verlauf, (w2a + t * (w2b - w2a), ra + t * (rb - ra), float(sa), float(sb))


def main():
    t0 = time.time()
    modell, stufe, npz, aus, kdatei = sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6]
    idx = [int(x) for x in sys.argv[7:]]
    cache = Z.ProfilCache(modell, stufe, npz)
    lin = Z.Lin(modell, cache.hp, cache.R_lin, cache.r_m)
    kd = json.load(open(kdatei))
    paare = [p for p in kd['paare'][str(stufe)] if p['wechsel']]
    erg = []
    for j in idx:
        p = paare[j]
        # eta der Zeile w2a an der Nullstelle ra
        _, _, eta0 = ma_s(modell, lin, cache, np.array([p['w2a']]), np.array([p['ra']]))
        eta_ref = eta0[0] * (1.0 if p['sa'] * 1.0 == p['sa'] else 1.0)
        # Ausrichtung so, dass s(w2a) das Vorzeichen von p['sa'] hat
        _, s0, _ = ma_s(modell, lin, cache, np.array([p['w2a']]), np.array([p['ra']]))
        if np.sign(s0[0]) != np.sign(p['sa']):
            eta_ref = -eta_ref
        verlauf, pkt = verfolge(modell, lin, cache, p, eta_ref, stufen=6)
        e = dict(paar=p, verlauf=verlauf, punkt=None)
        if pkt is not None:
            w2s, rs, sa, sb = pkt
            ul = N2.umlaeufe_n2(modell, lin, cache, np.array([w2s]), np.array([rs]))[0]
            inf = cache.info[round(float(w2s), 13)]
            e.update(punkt=[float(w2s), float(rs)], s_klammer=[float(sa), float(sb)], umlauf=ul, chi0=float(inf["chi0"]),
                     in_e1=bool(Z._in_e1(modell, float(w2s), float(rs))))
        Z.log('paar %d: %s' % (j, json.dumps({k: v for k, v in e.items() if k not in ('verlauf',)}, default=str)))
        for v in verlauf:
            Z.log('   L%d s=%s' % (v['stufe'], ' '.join('%.2e' % x for x in v['s'])))
        erg.append(e)
        Z.speichere_json(aus, dict(modell=modell, stufe=stufe, ergebnisse=erg, sekunden=time.time() - t0))
    Z.log('fertig %.1fs' % (time.time() - t0))


if __name__ == '__main__':
    if sys.argv[1] != 'kurve':
        raise SystemExit('unbekannt')
    main()
