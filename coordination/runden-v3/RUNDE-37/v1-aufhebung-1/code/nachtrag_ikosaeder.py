#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GLAS-STRAHLUNG-1, Nachtrag nach Sicht (beschreibend, aendert kein Urteil).

Anlass (Sicht der Zwischenauswertung N = 128, 256, 09:34 CEST): Das Mittel ueber die 24 festen Bahnlagen enthaelt einen
Stichprobenfehler der Lagen. Die Leistung einer Kreisbahn ist eine hermitesche quadratische Form in S(m), also ein
gerades Polynom vom Grad <= 4 in der Bahnnormale m (k -> -k gibt m -> -m). Die 12 Ecken des Ikosaeders sind ein
sphaerisches 5-Design; fuer gerade Funktionen genuegen die 6 Achsen. Ihr Mittel ist das exakte Lagenmittel.
gs.py (eingefroren) wird unveraendert importiert; nur in diesem Prozess wird gs.bahnnormalen durch die 6 Achsen ersetzt.
Probe: zweites, gedrehtes Ikosaeder muss dasselbe Mittel geben (Rundung).
Aufruf: python nachtrag_ikosaeder.py --v lauf/v.json --ein lauf/gs-N*.json --out aus/nachtrag-ikosaeder.json
"""
import argparse, json, os, sys, time, hashlib, math
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gs  # noqa: E402  (eingefroren, unveraendert)

GROESSEN = ['P_P1_SV1_J', 'P_P1_S_J', 'P_P1_TTL_J', 'P_P1_TT_J', 'K_P1_SV1_J', 'P_P1_SV1_ohneJ', 'P_umkreis_SV1_J']


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def achsen(drehung=None):
    f = (1 + math.sqrt(5)) / 2
    v = np.array([[0, 1, f], [0, 1, -f], [1, f, 0], [1, -f, 0], [f, 0, 1], [-f, 0, 1]], float)
    v /= np.linalg.norm(v, axis=1)[:, None]
    if drehung is not None:
        v = v @ drehung.T
    out = []
    for i, m in enumerate(v):
        u = np.cross(m, [0.3, 0.5, 0.7])
        u /= np.linalg.norm(u)
        w = np.cross(m, u)
        out.append(('ik%d' % i, m, np.outer(u + 1j * w, u + 1j * w)))
    return out


def drehung(seed=5):
    rng = np.random.default_rng(seed)
    q, r = np.linalg.qr(rng.normal(size=(3, 3)))
    q = q * np.sign(np.diag(r))[None, :]
    if np.linalg.det(q) < 0:
        q[:, 0] *= -1
    return q


def exakt(r, rot=None):
    gs.bahnnormalen = lambda: achsen(rot)
    a = gs.netz_auswerten(r)
    return {g: float(np.mean([b[g] for b in a['bahnen'].values()])) for g in GROESSEN}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--v', required=True)
    ap.add_argument('--ein', nargs='+', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    res = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'gs_sha256': sha(os.path.abspath(gs.__file__)),
                    'eingaben': {os.path.basename(p): sha(p) for p in [a.v] + a.ein}}}
    R = drehung()
    with open(a.v) as fh:
        rv = json.load(fh)['ergebnis']
    e1, e2 = exakt(rv), exakt(rv, R)
    res['V'] = {'exakt': e1, 'probe_gedreht_max_abw': max(abs(e1[g] - e2[g]) for g in GROESSEN)}
    netze = []
    probe = 0.0
    for p in sorted(a.ein):
        with open(p) as fh:
            r = json.load(fh)['ergebnis']
        if r['abgebrochen_frist'] or r['n_oben_fertig'] < r['n_oben_geplant']:
            continue
        e1, e2 = exakt(r), exakt(r, R)
        probe = max(probe, max(abs(e1[g] - e2[g]) for g in GROESSEN))
        z = {'datei': os.path.basename(p), 'N': r['N'], 'saat': r['saat'], 'exakt': e1}
        z['kanal'] = {'TT': e1['P_P1_TT_J'] - 1, 'L': e1['P_P1_TTL_J'] - e1['P_P1_TT_J'], 'nn': e1['P_P1_S_J'] - e1['P_P1_TTL_J'],
                      'V1': e1['P_P1_SV1_J'] - e1['P_P1_S_J']}
        netze.append(z)
    res['probe_gedreht_max_abw_glas'] = probe
    res['netze'] = netze
    jeN = {}
    for N in sorted(set(z['N'] for z in netze)):
        xs = [z for z in netze if z['N'] == N]
        n = len(xs)
        zN = {'netze': n}
        for g in GROESSEN:
            v = np.array([z['exakt'][g] for z in xs])
            zN[g] = {'mittel': float(v.mean()), 'sd_netze': float(v.std(ddof=1)) if n > 1 else None,
                     'se': float(v.std(ddof=1) / math.sqrt(n)) if n > 1 else None}
        for k in ('TT', 'L', 'nn', 'V1'):
            v = np.array([z['kanal'][k] for z in xs])
            zN['kanal_' + k] = {'mittel': float(v.mean()), 'sd_netze': float(v.std(ddof=1)) if n > 1 else None,
                                'se': float(v.std(ddof=1) / math.sqrt(n)) if n > 1 else None}
        jeN[str(N)] = zN
    res['je_N'] = jeN
    res['laufzeit_s'] = time.time() - t0
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1)
    os.replace(a.out + '.tmp', a.out)
    print('fertig nachtrag_ikosaeder laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
