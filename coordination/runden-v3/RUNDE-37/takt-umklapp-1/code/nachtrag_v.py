#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UMKLAPP-1, NACHTRAG nach dem Einfrieren (beschreibend, geht in kein Urteil ein).
Hinweis der Leitung 06:20 CEST (HODGE-L, Handrechnung): Finns gefuelltes Netz V ist an 12 von 116 Flaechen je Zelle
nicht Delaunay. Fragen: (1) Wie viele Flaechen von V verletzen die Delaunay-Bedingung? (2) Delaunay-gesteuerte 2-3-Zuege
an genau diesen Flaechen (staerkste Verletzung zuerst, nur erlaubte Zuege wie uk.kandidaten): ist V danach Delaunay?
(3) TT-Spektrum (tg.modell, tg.spektrum, tg_auswertung.netz_kennzahlen unveraendert) vor und nach den Zuegen.
uk.py, tg.py, tg_auswertung.py (eingefroren 06:19:02 CEST bzw. TT-GLAS-1) werden unveraendert importiert."""
import argparse, json, os, sys, time, hashlib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tg  # noqa: E402
import uk  # noqa: E402
import tg_auswertung as tga  # noqa: E402

TOL = 1e-9
KLASSEN = {'100': [0, 1, 2], '110': [3, 4, 5, 6, 7, 8], '111': [9, 10, 11, 12]}


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def mu_stat(LV, pos, G, O):
    fl = uk.flaechen(G, O)
    mu = uk.raender(LV, pos, G, O, fl)
    v = mu < -TOL
    return {'T': int(len(G)), 'F': int(fl['F']), 'mu_min': float(mu.min()), 'n_verletzt': int(v.sum()),
            'n_kugel': int((np.abs(mu) <= TOL).sum()), 'mu_verletzt_werte': sorted(set(round(float(x), 9) for x in mu[v]))[:10]}


def tt(LV, pos, G, O):
    mod = tg.modell(LV, pos, G, O, {})
    spek = tg.spektrum(mod, list(range(13)))
    kz = tga.netz_kennzahlen(spek)
    out = {k: kz.get(k) for k in ('regulaer', 'n_gruende', 'gruende', 'spanne', 'w_mittel', 'aufspaltung_max',
                                   'richtungsspanne_mittel_zweige', 'n_masselos', 'n_wachsend_max', 'n_unklar_max',
                                   'luecke_min', 'A_red_pd_alle', 'B_red_neg_max', 'tt_min', 'lin_max', 'dim', 'rang_voll',
                                   'w2k2', 'richtungen')}
    w = np.array(kz['w2k2'], float)
    if np.isfinite(w).all():
        out['klassen_abw'] = {k: float(np.max(w[i], axis=0).max() / np.min(w[i], axis=0).min() - 1) for k, i in KLASSEN.items()}
        out['klassen_abw_je_zweig'] = {k: [float(w[i, z].max() / w[i, z].min() - 1) for z in (0, 1)] for k, i in KLASSEN.items()}
    out['pruefung'] = mod['pruefung']
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    res = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'uk_sha256': sha(os.path.abspath(uk.__file__)),
                    'tg_sha256': sha(os.path.abspath(tg.__file__)), 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}}
    LV, pos, G0, O0, _ = tg.netz_V()
    nV = len(pos)
    G, O = G0.copy(), O0.copy()
    vmin = uk.VMIN_REL * float(uk.tet_vol(LV, pos, G0, O0).mean())
    res['vorher'] = mu_stat(LV, pos, G0, O0)
    zuege = []
    for _ in range(500):
        k = uk.kandidaten(LV, pos, G, O, nV, vmin)
        fl = k['fl']
        mu = uk.raender(LV, pos, G, O, fl)
        verl = np.nonzero(mu < -TOL)[0]
        if len(verl) == 0:
            res['ende'] = 'keine verletzte Flaeche mehr'
            break
        ok = verl[k['ok'][verl]]
        if len(ok) == 0:
            res['ende'] = 'verletzte Flaechen, aber keine erlaubt'
            res['blockiert'] = {'n_verletzt': int(len(verl)), 'davon_konvex': int(k['konvex'][verl].sum()),
                                'davon_volok': int(k['volok'][verl].sum()), 'davon_neu': int(k['neu'][verl].sum())}
            break
        j = ok[np.argmin(mu[ok])]
        zuege.append({'mu': float(mu[j]), 'n_verletzt_davor': int(len(verl)), 'n_erlaubt_davor': int(len(ok))})
        G, O = uk.zug23(LV, pos, G, O, fl, j)
    res['zuege'] = zuege
    res['n_zuege'] = len(zuege)
    res['nachher'] = mu_stat(LV, pos, G, O)
    res['regge_vorher'] = uk.regge(LV, pos, G0, O0, nV)
    res['regge_nachher'] = uk.regge(LV, pos, G, O, nV)
    res['tt_vorher'] = tt(LV, pos, G0, O0)
    res['tt_nachher'] = tt(LV, pos, G, O)
    res['laufzeit_s'] = time.time() - t0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig nachtrag V', len(zuege), 'zuege', 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
