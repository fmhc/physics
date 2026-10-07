#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TT-GLAS-1, NACHTRAG nach dem Einfrieren (beschreibend, geht in kein Urteil ein).

Frage: Wie haengt die Richtungsspanne je Zufallsnetz am Bewegungsgewicht je Tetraeder?
  J1    : J_t = 1 (Hauptlauf, Kontrolle der Nachtrag-Strecke)
  JV    : J_t = V_t / mittleres V_t (Volumengewicht)
  JinvV : J_t = mittleres V_t / V_t (Kehrwert, Art von A2 in EINE-WELT-LOCH-1)
tg.py und tg_auswertung.py (eingefroren 2026-10-05 04:39:07 CEST) werden unveraendert importiert.
"""
import argparse, json, os, sys, time, hashlib, resource
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tg  # noqa: E402
import tg_auswertung as tga  # noqa: E402


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def netz_gewichtet(N, saat, art):
    LV, pos, G, O, pr = tg.zufallsnetz(N, saat)
    mod = tg.modell(LV, pos, G, O, pr)
    X = pos[G] + np.einsum('tai,ij->taj', O.astype(float), LV)
    vol = np.abs(np.linalg.det(X[:, 1:] - X[:, :1])) / 6.0
    if art == 'JV':
        w = vol / vol.mean()
    elif art == 'JinvV':
        w = vol.mean() / vol
    else:
        w = np.ones(len(vol))
    mod['A0'] = mod['A0'] * w[:, None, None]
    return mod, {'J_min': float(w.min()), 'J_max': float(w.max())}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--N', type=int, required=True)
    ap.add_argument('--saaten', required=True)
    ap.add_argument('--arten', default='J1,JV,JinvV')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    res = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'tg_sha256': sha(os.path.abspath(tg.__file__)),
                    'tga_sha256': sha(os.path.abspath(tga.__file__)), 'argv': sys.argv,
                    'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}, 'netze': [], 'zusammenfassung': {}}
    arten = a.arten.split(',')
    for saat in [int(x) for x in a.saaten.split(',')]:
        for art in arten:
            mod, ji = netz_gewichtet(a.N, saat, art)
            kz = tga.netz_kennzahlen(tg.spektrum(mod, list(range(13))))
            z = {k: kz.get(k) for k in ('regulaer', 'n_gruende', 'gruende', 'spanne', 'w_mittel', 'aufspaltung_max',
                                         'richtungsspanne_mittel_zweige', 'n_masselos', 'n_wachsend_max', 'n_unklar_max',
                                         'tt_min', 'lin_max', 'luecke_min', 'A_red_pd_alle', 'B_red_neg_max')}
            z.update({'N': a.N, 'saat': saat, 'art': art})
            z.update(ji)
            res['netze'].append(z)
    for art in arten:
        sp_ = np.array([z['spanne'] for z in res['netze'] if z['art'] == art and z['regulaer']])
        res['zusammenfassung'][art] = {'n_netze': sum(1 for z in res['netze'] if z['art'] == art),
                                       'n_regulaer': int(len(sp_)),
                                       'spanne_mittel': float(sp_.mean()) if len(sp_) else None,
                                       'spanne_sd': float(sp_.std(ddof=1)) if len(sp_) > 1 else None}
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig nachtrag', a.N, a.arten, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
