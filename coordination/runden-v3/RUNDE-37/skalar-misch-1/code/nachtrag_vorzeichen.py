#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SKALAR-MISCH-1, Nachtrag nach dem Einfrieren und nach Sicht (beschreibend, geht in kein Plan-Urteil ein).

Anlass (nach Sicht auf suche-F1.json): Der Lambda[D]-Anteil Q der langwelligen TT-Masse wechselt auf der Kurve dTT = 0
das Vorzeichen (zwischen log10 J_Kegel = -1,7 und -1,6). Die Planannahme "Q ist ein Quadrat, Q >= 0" (PLAN 2.3) ist
falsch; das kompakte Residuum sqrt(max(Q, 0)) der Plan-Suche ist darum fehlerhaft (es laesst Q < 0 frei).
Hier dasselbe mit vorzeichenbehaftetem Q:
  F1: Newton/LM auf (dTT, Q) -> exakter TT-isotroper Punkt (2 Gleichungen, 2 Gewichte); dort alle Kennzahlen.
  F2: LM auf (dTT, Q, Gang_0) aus denselben 3 Starts wie der Plan; danach LM auf (13-Richtungen-TT-Residuen, Gang_0),
      damit auch Anteile ausserhalb der Zwei-Term-Struktur mitgenommen werden.
smi.py (eingefroren 20261005-094129) wird unveraendert importiert.
Aufruf: python nachtrag_vorzeichen.py --out nachtrag/vorzeichen.json
"""
import argparse, json, sys, time, platform, os, resource, hashlib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import smi  # noqa: E402  (eingefroren, unveraendert)
import ew  # noqa: E402
import pn  # noqa: E402
import nachtrag_iso as ni  # noqa: E402


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    ende = t0 + 540
    info = {'numpy': np.__version__, 'host': platform.node(), 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'argv': sys.argv, 'skript_sha256': sha(os.path.abspath(__file__)), 'smi_sha256': sha(os.path.abspath(smi.__file__))}
    mod = ew.baue('V')
    tder = pn.tet_ableitungen(mod)
    Q = ni.Q_map(mod, tder)
    P = smi.alles_vorbereiten(mod, Q)
    wd = P['wd']
    bl = smi.bahnen()
    m4 = np.array([float((m ** 4).sum()) for _, m, _ in bl])
    out = {'info': info, 't_vorbereitung': time.time() - t0}

    def r_f1(x):
        try:
            d, q, off = smi.dtt_q(P['p2'], smi.gewichte(x, 'F1'))
            return np.array([d, q])
        except np.linalg.LinAlgError:
            return np.full(2, 1e3)

    def r_f2(x):
        try:
            w = smi.gewichte(x, 'F2')
            d, q, off = smi.dtt_q(P['p2'], w)
            g = smi.gang_null(P['p200'], w, wd, bl, m4)[0]['gang']
            return np.array([d, q, g])
        except np.linalg.LinAlgError:
            return np.full(3, 1e3)

    def r_f2_voll(x):
        try:
            w = smi.gewichte(x, 'F2')
            r = smi.tt_null(P['p13'], w)['res']
            g = smi.gang_null(P['p200'], w, wd, bl, m4)[0]['gang']
            return np.concatenate([r, [g]])
        except np.linalg.LinAlgError:
            return np.full(53, 1e3)

    # F1: exakter TT-Punkt
    x, r, hist = smi.lm(r_f1, np.array([-1.672, 0.057]), maxit=40, h=1e-7)
    w = smi.gewichte(x, 'F1')
    out['F1_tt_exakt'] = {'x': x.tolist(), 'w': w.tolist(), 'rest': r.tolist(), 'F_verlauf': [h_.get('F') for h_ in hist],
                          'messung': smi.messen(w, P, wd, bl, m4), 'diagnose': smi.tt_diagnose(P['p13'], w),
                          'stabil': smi.stabil(mod, w)}
    # F2: drei Starts wie im Plan
    xi = np.array([0.0, pn.XK, pn.XK, pn.XS, pn.XS])
    starts = [xi, np.log10([0.829, 9.78, 99.8, 31.9, 0.049]), xi + np.random.default_rng(5).uniform(-0.2, 0.2, 5)]
    laeufe = []
    for x0 in starts:
        if time.time() > ende - 120:
            laeufe.append({'x0': x0.tolist(), 'abbruch': 'zeit'})
            continue
        t1 = time.time()
        x, r, hist = smi.lm(r_f2, x0, maxit=25, h=1e-6, zeit=min(time.time() + 110, ende - 100))
        w = smi.gewichte(x, 'F2')
        z = {'x0': x0.tolist(), 'x': x.tolist(), 'w': w.tolist(), 'rest': r.tolist(), 'F_verlauf': [h_.get('F') for h_ in hist],
             'am_rand': bool(np.any(np.abs(np.abs(x) - 2.0) < 1e-9)), 'messung': smi.messen(w, P, wd, bl, m4),
             'diagnose': smi.tt_diagnose(P['p13'], w), 't': time.time() - t1}
        laeufe.append(z)
    out['F2_laeufe'] = laeufe
    # bester F2-Endpunkt: Feinlauf auf alle 13 Richtungen + Gang_0
    ok = [z for z in laeufe if 'messung' in z and z['messung'].get('ok')]
    if ok and time.time() < ende - 60:
        b = min(ok, key=lambda z: max(z['messung']['tt_spanne0'], abs(z['messung']['gang0'])))
        x, r, hist = smi.lm(r_f2_voll, np.array(b['x']), maxit=15, h=1e-6, zeit=ende - 40)
        w = smi.gewichte(x, 'F2')
        out['F2_fein'] = {'x0': b['x'], 'x': x.tolist(), 'w': w.tolist(), 'F_verlauf': [h_.get('F') for h_ in hist],
                          'messung': smi.messen(w, P, wd, bl, m4), 'diagnose': smi.tt_diagnose(P['p13'], w)}
        if time.time() < ende - 15:
            out['F2_fein']['stabil'] = smi.stabil(mod, w)
    out['laufzeit_s'] = time.time() - t0
    out['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    out['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(out, f, indent=1, default=lambda o: o.tolist() if hasattr(o, 'tolist') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig nachtrag_vorzeichen laufzeit %.1f s' % out['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
