#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TT-GLAS-2: mechanische Auswertung (Urteile TG2-0 bis TG2-3 nach PLAN.md Abschnitt 6), Tabellen und Bild.

Liest lauf/bz-N*-s*.json (Aufgabe 1), lauf/dk-N*-s*.json (Aufgaben 2 und 3; Teile je Netz ueber ridx zusammengefuehrt),
dazu TT-GLAS-1 lauf/auswertung.json und nachtrag/n512/auswertung-n512.json (Referenz). Schreibt auswertung.json,
tabellen.md und tg2-bild.png in --out.
"""
import argparse, glob, json, os, re, hashlib, time
import numpy as np

REF_TG1 = '/home/fmh/fmhc-physics-remote/tt-glas-1/lauf/auswertung.json'
REF_N512 = '/home/fmh/fmhc-physics-remote/tt-glas-1/nachtrag/n512/auswertung-n512.json'
TOL_G0 = 1e-3
N_KLASSEN = 112
SCHWELLE_G3 = 0.07
MIN_NETZE_G3 = 4
LIN_MAX = 0.01
NBOOT = 2000
VARIANTEN = ('a', 'b', 'c', 'd', 'e')


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def kennz(w):
    w = np.asarray(w, float)
    if w.shape != (13, 2) or not np.isfinite(w).all() or (w <= 0).any():
        return None
    wbar = w.mean(1)
    sp_ = float(w.max() / w.min() - 1)
    au = float(np.max(w[:, 1] / w[:, 0] - 1))
    return {'spanne': sp_, 'aufspaltung_max': au, 'richtungsspanne': float(wbar.max() / wbar.min() - 1),
            'doppelbrechungsanteil': au / sp_ if sp_ > 0 else None, 'w_mittel': float(w.mean())}


def ols(x, y):
    A = np.vstack([np.ones_like(x), x]).T
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(c[0]), float(c[1])


def mittel_sd(x):
    x = np.asarray([v for v in x if v is not None], float)
    if len(x) == 0:
        return None, None, 0
    return float(x.mean()), (float(x.std(ddof=1)) if len(x) > 1 else None), int(len(x))


# ------------------------------------------------------------------------------------------------ Aufgabe 1
def bz_netze(lauf, res):
    netze = []
    for p in sorted(glob.glob(os.path.join(lauf, 'bz-N*-s*.json'))):
        d = json.load(open(p))
        e = d['ergebnis']
        res['eingaben'][os.path.basename(p)] = {'sha256': sha(p), 'bz_sha256': d['info']['skript_sha256'],
                                                'dz_sha256': d['info']['dz_sha256'], 'geraet': d['info']['geraet'],
                                                'gpu': d['info']['gpu'], 'laufzeit_s': d['laufzeit_s']}
        pk = e['punkte']
        fertig = sorted(z['klasse'] for z in pk)
        nicht_g = [z for z in pk if not z['gamma']]
        g = [z for z in pk if z['gamma']]
        wmin = [(z['w2_min_ohne_null'], z) for z in nicht_g if z['w2_min_ohne_null'] is not None]
        zmin = min(wmin, key=lambda t: t[0])[1] if wmin else None
        n = {'N': e['N'], 'saat': e['saat'], 'n_punkte': len(pk), 'vollstaendig': fertig == list(range(N_KLASSEN)) and not e['abgebrochen_frist'],
             'abgebrochen_frist': e['abgebrochen_frist'], 'geraet': d['info']['geraet'], 'laufzeit_s': d['laufzeit_s'],
             'n_wachsend': int(sum(z['n_wachsend'] for z in pk)),
             'wachsend_orte': [{'m': z['m'], 'eps': z['eps'], 'werte': z['wachsend_werte']} for z in pk if z['n_wachsend'] > 0][:20],
             'n_null_gamma': [int(z['n_null']) for z in g], 'n_null_sonst': int(sum(z['n_null'] for z in nicht_g)),
             'null_sonst_orte': [z['m'] for z in nicht_g if z['n_null'] > 0][:20],
             'w2_min': float(zmin['w2_min_ohne_null']) if zmin else None, 'w2_min_m': zmin['m'] if zmin else None,
             'w2_min_eps': zmin['eps'] if zmin else None,
             'w2_min_rel_skala': (float(min(z['w2_min_ohne_null'] / z['skala'] for z in nicht_g if z['w2_min_ohne_null'] is not None))
                                  if any(z['w2_min_ohne_null'] is not None for z in nicht_g) else None),
             'gamma_w2_min_ohne_null': [z['w2_min_ohne_null'] for z in g],
             'gamma_w2_kleinste': [z['w2_kleinste'][:8] for z in g],
             'A_red_pd_alle': bool(all(z['A_red_pd'] for z in nicht_g)), 'A_red_pd_gamma': [z['A_red_pd'] for z in g],
             'B_red_neg_max': int(max(z['B_red_neg'] for z in nicht_g)) if nicht_g else None,
             'B_red_neg_gamma': [z['B_red_neg'] for z in g],
             'rang_voll': bool(all(z['rang_Mc'] == z['nX'] for z in nicht_g)), 'w2im_max': float(max(z['w2im_max'] for z in pk)),
             'skala_max': float(max(z['skala'] for z in pk)),
             'punkte_eps_w2min': [[z['eps'], z['w2_min_ohne_null'], int(z['gamma'])] for z in pk],
             'kontrolle': e.get('kontrollpunkt_100')}
        netze.append(n)
    return netze


# ------------------------------------------------------------------------------------------------ Aufgaben 2 und 3
def dk_netze(lauf, res):
    teile = {}
    for p in sorted(glob.glob(os.path.join(lauf, 'dk-N*-s*.json'))):
        d = json.load(open(p))
        e = d['ergebnis']
        key = (int(e['N']), int(e['saat']))
        res['eingaben'][os.path.basename(p)] = {'sha256': sha(p), 'dk_sha256': d['info']['skript_sha256'],
                                                'dz_sha256': d['info']['dz_sha256'], 'geraet': d['info']['geraet'],
                                                'laufzeit_s': d['laufzeit_s']}
        t = teile.setdefault(key, {'zeilen': {}, 'pruefung': e['pruefung'], 'k3': e['k3'], 'varianten': set()})
        t['varianten'] |= set(e['varianten'])
        for z in e['zeilen']:
            t['zeilen'][z['ridx']] = z
    netze = []
    for (N, saat), t in sorted(teile.items()):
        zl = [t['zeilen'][i] for i in sorted(t['zeilen'])]
        n = {'N': N, 'saat': saat, 'ridx': sorted(t['zeilen']), 'vollstaendig': sorted(t['zeilen']) == list(range(13)),
             'varianten': sorted(t['varianten']), 'pruefung': t['pruefung'], 'k3': t['k3']}
        if not n['vollstaendig']:
            netze.append(n)
            continue
        # (a) regulaer
        gr = []
        for z in zl:
            for key in ('eps1', 'eps2'):
                if key not in z:
                    continue
                a = z[key]['a']
                if a['n_masselos'] != 2 or len(a['w2k2_masselos']) != 2:
                    gr.append('%s %s: %d masselos' % (z['richtung'], key, a['n_masselos']))
                if a['n_wachsend'] > 0:
                    gr.append('%s %s: %d wachsend' % (z['richtung'], key, a['n_wachsend']))
                if a['n_unklar'] > 0:
                    gr.append('%s %s: %d unklar' % (z['richtung'], key, a['n_unklar']))
            if 'eps2' in z and len(z['eps2']['a']['w2k2_masselos']) == 2 and len(z['eps1']['a']['w2k2_masselos']) == 2:
                lin = max(abs(x / y - 1) for x, y in zip(z['eps2']['a']['w2k2_masselos'], z['eps1']['a']['w2k2_masselos']))
                if lin > LIN_MAX:
                    gr.append('%s nicht linear %.3g' % (z['richtung'], lin))
        n['a_regulaer'] = len(gr) == 0
        n['a_gruende'] = gr[:10]
        n['mit_lin'] = any('eps2' in z for z in zl)
        lins = [abs(x / y - 1) for z in zl if 'eps2' in z and len(z['eps2']['a']['w2k2_masselos']) == 2
                and len(z['eps1']['a']['w2k2_masselos']) == 2 for x, y in zip(z['eps2']['a']['w2k2_masselos'], z['eps1']['a']['w2k2_masselos'])]
        n['lin_max'] = float(max(lins)) if lins else None
        lm = [z['eps1']['a']['luecke_min'] for z in zl if z['eps1']['a']['luecke_min'] is not None]
        n['luecke_min'] = float(min(lm)) if lm else None
        n['A_red_pd_alle'] = bool(all(z['eps1']['A_red_pd'] for z in zl))
        n['werte'] = {}
        n['kennzahlen'] = {}
        wa = [z['eps1']['a']['w2k2_masselos'] if len(z['eps1']['a']['w2k2_masselos']) == 2 else [np.nan, np.nan] for z in zl]
        n['werte']['a'] = wa
        n['kennzahlen']['a'] = kennz(wa) if n['a_regulaer'] else None
        if 'b' in n['varianten']:
            wb = [z['eps1']['b']['w2k2'] for z in zl]
            n['werte']['b'] = wb
            n['kennzahlen']['b'] = kennz(wb)
            n['b_im_max'] = float(max(z['eps1']['b']['w2im_max'] for z in zl))
            n['b_masse_ev_min'] = float(min(min(z['eps1']['b']['masse_ev']) for z in zl))
            # Cauchy-Pruefung: Ritz-Werte >= Eigenwerte (a), relativ
            if n['a_regulaer']:
                n['ritz_minus_a_min_rel'] = float(np.min(np.array(wb) / np.array(wa) - 1))
        if 'c' in n['varianten']:
            okc = all(z['eps1']['c']['n_masselos'] == 2 and len(z['eps1']['c']['w2k2_masselos']) == 2 for z in zl)
            wc = [z['eps1']['c']['w2k2_masselos'] if len(z['eps1']['c']['w2k2_masselos']) == 2 else [np.nan, np.nan] for z in zl]
            n['werte']['c'] = wc
            n['c_gueltig'] = bool(okc)
            n['kennzahlen']['c'] = kennz(wc) if okc else None
            n['c_n_masselos'] = sorted(set(int(z['eps1']['c']['n_masselos']) for z in zl))
            n['c_n_negativ_max'] = int(max(z['eps1']['c']['n_negativ'] for z in zl))
            n['c_w2_negativ_beispiel'] = [z['eps1']['c']['w2_negativ'][:3] for z in zl if z['eps1']['c']['n_negativ'] > 0][:3]
            n['c_n_unklar_max'] = int(max(z['eps1']['c']['n_unklar'] for z in zl))
            n['c_K3_red_neg_max'] = int(max(z['eps1']['c']['K3_red_neg'] for z in zl))
            n['c_B_red_pd_alle'] = bool(all(z['eps1']['c']['B_red_pd'] for z in zl))
            lc = [z['eps1']['c']['luecke_min'] for z in zl if z['eps1']['c']['luecke_min'] is not None]
            n['c_luecke_min'] = float(min(lc)) if lc else None
        for v in ('d', 'e'):
            if v in n['varianten']:
                wv = [z['eps1'][v]['w2k2'] for z in zl]
                n['werte'][v] = wv
                n['kennzahlen'][v] = kennz(wv)
        if 'b' in n['varianten']:
            pa = np.array([z['eps1']['proj_anteil_weg'] for z in zl])
            bz_ = np.array([z['eps1']['Bz_k2V'] for z in zl])
            n['proj_anteil_weg'] = {'min': float(pa.min()), 'max': float(pa.max()), 'mittel': float(pa.mean())}
            n['Bz_k2V'] = {'min': float(bz_.min()), 'max': float(bz_.max())}
        if 'e' in n['varianten']:
            be = np.array([z['eps1']['e']['B_k2V'] for z in zl])
            n['e_B_k2V'] = {'min': float(be.min()), 'max': float(be.max())}
        netze.append(n)
    return netze


def laufliste(lauf):
    """Start, Ende, Spur und Rueckgabecode je Lauf aus den kleintest-Logs (lauf/tg2-*.log)."""
    out = []
    for p in sorted(glob.glob(os.path.join(lauf, 'tg2-*.log'))):
        txt = open(p).read()
        s = re.search(r'^start (\S+) spur=(\S+) unit=(\S+)', txt, re.M)
        e = re.search(r'^ende (\S+) rc=(\d+)', txt, re.M)
        z = {'name': os.path.basename(p)[:-4], 'spur': s.group(2) if s else None, 'start': s.group(1) if s else None,
             'ende': e.group(1) if e else None, 'rc': int(e.group(2)) if e else None}
        if s and e:
            t0 = time.mktime(time.strptime(s.group(1)[:19], '%Y-%m-%dT%H:%M:%S'))
            t1 = time.mktime(time.strptime(e.group(1)[:19], '%Y-%m-%dT%H:%M:%S'))
            z['dauer_s'] = int(t1 - t0)
        out.append(z)
    return out


def boot_exponent(gr, rng):
    out = []
    Ns = sorted(gr)
    for _ in range(NBOOT):
        xb, yb = [], []
        for N in Ns:
            g = gr[N][rng.integers(0, len(gr[N]), len(gr[N]))]
            xb += [np.log(N)] * len(g)
            yb += list(np.log(g))
        out.append(ols(np.array(xb), np.array(yb))[1])
    return np.array(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lauf', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    res = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                    'ref_tg1_sha256': sha(REF_TG1), 'ref_n512_sha256': sha(REF_N512)}, 'eingaben': {}}
    ref = json.load(open(REF_TG1))
    refw = {(int(n['N']), int(n['saat'])): np.array(n['w2k2'], float) for n in ref['netze'] if n.get('vollstaendig')}
    bz = bz_netze(a.lauf, res)
    dk = dk_netze(a.lauf, res)
    res['bz_netze'] = bz
    res['dk_netze'] = dk
    # ---------------- TG2-0
    abw_dk, abw_bz, verglichen = [], [], {128: 0, 256: 0}
    zeilen0 = []
    for n in dk:
        if n['N'] in (128, 256) and n['vollstaendig'] and (n['N'], n['saat']) in refw:
            w = np.array(n['werte']['a'], float)
            r = refw[(n['N'], n['saat'])]
            dev = np.abs(w / r - 1)
            m = float(np.nanmax(dev)) if np.isfinite(dev).any() else float('inf')
            if not np.isfinite(dev).all():
                m = float('inf')
            abw_dk.append(m)
            verglichen[n['N']] += 1
            zeilen0.append({'N': n['N'], 'saat': n['saat'], 'quelle': 'dk', 'abw_max': m})
    for n in bz:
        ko = n['kontrolle']
        if n['N'] in (128, 256) and ko and (n['N'], n['saat']) in refw:
            r = refw[(n['N'], n['saat'])][0]
            if len(ko['w2k2_masselos']) == 2:
                m = float(np.max(np.abs(np.array(ko['w2k2_masselos']) / r - 1)))
            else:
                m = float('inf')
            abw_bz.append(m)
            zeilen0.append({'N': n['N'], 'saat': n['saat'], 'quelle': 'bz', 'abw_max': m})
    alle0 = abw_dk + abw_bz
    g0 = {'abw_max_dk': max(abw_dk) if abw_dk else None, 'abw_max_bz': max(abw_bz) if abw_bz else None,
          'n_verglichen_dk': verglichen, 'n_verglichen_bz': len(abw_bz), 'zeilen': zeilen0}
    gmax = max(alle0) if alle0 else None
    if gmax is None:
        g0['plan'] = g0['wortlaut'] = 'nicht entscheidbar'
    else:
        g0['wortlaut'] = ('eingetroffen' if gmax <= TOL_G0 else 'verfehlt') if (verglichen[128] >= 1 and verglichen[256] >= 1) else (
            'verfehlt' if gmax > TOL_G0 else 'nicht entscheidbar')
        if gmax > TOL_G0:
            g0['plan'] = 'verfehlt'
        elif verglichen[128] == 12 and verglichen[256] == 12:
            g0['plan'] = 'eingetroffen'
        else:
            g0['plan'] = 'nicht entscheidbar'
    g0['abw_max'] = gmax
    # beschreibend: N = 512, Saat 1 gegen TT-GLAS-1 Nachtrag
    try:
        r512 = json.load(open(REF_N512))
        rn = [n for n in r512['netze'] if int(n['N']) == 512 and int(n['saat']) == 1 and n.get('vollstaendig')]
        mine = [n for n in dk if n['N'] == 512 and n['saat'] == 1 and n['vollstaendig']]
        if rn and mine:
            dev = np.abs(np.array(mine[0]['werte']['a'], float) / np.array(rn[0]['w2k2'], float) - 1)
            g0['n512_s1_abw_max'] = float(np.nanmax(dev)) if np.isfinite(dev).all() else None
            g0['n512_s1_spanne_ref'] = rn[0].get('spanne')
    except Exception as ex:  # noqa: BLE001
        g0['n512_fehler'] = str(ex)
    res['TG2-0'] = g0
    # ---------------- TG2-1
    netz24 = [n for n in bz if n['N'] in (128, 256) and 1 <= n['saat'] <= 12]
    schluessel = sorted(set((n['N'], n['saat']) for n in netz24))
    alle24 = len(schluessel) == 24
    wachs = sum(n['n_wachsend'] for n in netz24)
    voll = all(n['vollstaendig'] for n in netz24) and alle24
    g1 = {'n_netze': len(schluessel), 'n_vollstaendig': int(sum(n['vollstaendig'] for n in netz24)), 'n_wachsend_summe': int(wachs),
          'netze_mit_wachsend': [(n['N'], n['saat'], n['n_wachsend']) for n in netz24 if n['n_wachsend'] > 0],
          'n_punkte_summe': int(sum(n['n_punkte'] for n in netz24)),
          'null_gamma_verteilung': sorted(set(tuple(n['n_null_gamma']) for n in netz24)),
          'null_sonst_summe': int(sum(n['n_null_sonst'] for n in netz24))}
    if wachs > 0:
        g1['plan'] = g1['wortlaut'] = 'verfehlt'
    else:
        g1['plan'] = 'eingetroffen' if voll else 'nicht entscheidbar'
        g1['wortlaut'] = 'eingetroffen' if alle24 else 'nicht entscheidbar'
    res['TG2-1'] = g1
    # ---------------- Zerlegung je N (beschreibend) und TG2-2
    jeN = {}
    for N in sorted(set(n['N'] for n in dk)):
        nn = [n for n in dk if n['N'] == N and n['vollstaendig']]
        z = {'n_netze': len(nn), 'n_a_regulaer': int(sum(n.get('a_regulaer', False) for n in nn))}
        for v in VARIANTEN:
            ks = [n['kennzahlen'].get(v) for n in nn if n.get('kennzahlen', {}).get(v)]
            if not ks:
                continue
            zz = {}
            for key in ('spanne', 'aufspaltung_max', 'richtungsspanne', 'doppelbrechungsanteil', 'w_mittel'):
                m, s, c = mittel_sd([k[key] for k in ks])
                zz[key] = {'mittel': m, 'sd': s, 'n': c}
            z[v] = zz
        anteile = [n['kennzahlen']['c']['spanne'] / (n['kennzahlen']['b']['spanne'] + n['kennzahlen']['c']['spanne'])
                   for n in nn if n.get('kennzahlen', {}).get('b') and n.get('kennzahlen', {}).get('c')]
        if anteile:
            m, s, c = mittel_sd(anteile)
            z['anteil_c'] = {'mittel': m, 'sd': s, 'n': c}
        jeN[str(N)] = z
    res['je_N'] = jeN
    g2 = {}
    vergl = {}
    for N in (128, 256):
        nn = [n for n in dk if n['N'] == N and n['vollstaendig'] and n.get('kennzahlen', {}).get('b') and n.get('kennzahlen', {}).get('c')]
        if nn:
            vergl[N] = (float(np.mean([n['kennzahlen']['b']['spanne'] for n in nn])), float(np.mean([n['kennzahlen']['c']['spanne'] for n in nn])), len(nn))
    g2['je_N'] = {str(N): {'spanne_b': v[0], 'spanne_c': v[1], 'n': v[2]} for N, v in vergl.items()}
    if len(vergl) == 2:
        kl = [v[0] < v[1] for v in vergl.values()]
        g2['plan'] = 'eingetroffen' if all(kl) else ('verfehlt' if not any(kl) else 'nicht entscheidbar (gemischt)')
    else:
        g2['plan'] = 'nicht entscheidbar'
    nn = [n for n in dk if n['N'] in (128, 256) and n['vollstaendig'] and n.get('kennzahlen', {}).get('b') and n.get('kennzahlen', {}).get('c')]
    if nn:
        sb = float(np.mean([n['kennzahlen']['b']['spanne'] for n in nn]))
        sc = float(np.mean([n['kennzahlen']['c']['spanne'] for n in nn]))
        g2.update({'spanne_b_alle': sb, 'spanne_c_alle': sc, 'n_alle': len(nn), 'wortlaut': 'eingetroffen' if sb < sc else 'verfehlt'})
    else:
        g2['wortlaut'] = 'nicht entscheidbar'
    res['TG2-2'] = g2
    # ---------------- TG2-3 und Exponent
    n1024 = [n for n in dk if n['N'] == 1024 and n['vollstaendig'] and n.get('a_regulaer') and n['kennzahlen'].get('a')]
    g3 = {'n_netze': len(n1024), 'saaten': [n['saat'] for n in n1024]}
    if len(n1024) >= MIN_NETZE_G3:
        m = float(np.mean([n['kennzahlen']['a']['spanne'] for n in n1024]))
        g3.update({'spanne_mittel': m, 'plan': 'eingetroffen' if m < SCHWELLE_G3 else 'verfehlt'})
        g3['wortlaut'] = g3['plan']
    else:
        if n1024:
            g3['spanne_mittel'] = float(np.mean([n['kennzahlen']['a']['spanne'] for n in n1024]))
        g3['plan'] = g3['wortlaut'] = 'nicht entscheidbar (weniger als %d Netze)' % MIN_NETZE_G3
    res['TG2-3'] = g3
    rng = np.random.default_rng(17)
    gr = {}
    for n in dk:
        if n['vollstaendig'] and n.get('a_regulaer') and n['kennzahlen'].get('a'):
            gr.setdefault(n['N'], []).append(n['kennzahlen']['a']['spanne'])
    gr = {N: np.array(v) for N, v in gr.items() if len(v) >= 1}
    ex = {}
    if len(gr) >= 2:
        x = np.concatenate([[np.log(N)] * len(v) for N, v in sorted(gr.items())])
        y = np.concatenate([np.log(v) for N, v in sorted(gr.items())])
        a0, p = ols(x, y)
        bs = boot_exponent({N: v for N, v in gr.items() if len(v) >= 2}, rng) if all(len(v) >= 2 for v in gr.values()) else None
        ex['dieser_lauf'] = {'N': sorted(gr), 'p': p, 'a0': a0, 'p_boot_95': [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))] if bs is not None else None,
                             'spanne_1024_gerade': float(np.exp(a0 + p * np.log(1024)))}
        gr2 = dict(gr)
        for N in (32, 64):
            v = [nr['spanne'] for nr in ref['netze'] if int(nr['N']) == N and nr.get('regulaer')]
            if v:
                gr2[N] = np.array(v)
        x = np.concatenate([[np.log(N)] * len(v) for N, v in sorted(gr2.items())])
        y = np.concatenate([np.log(v) for N, v in sorted(gr2.items())])
        a1, p1 = ols(x, y)
        ex['mit_tg1_32_64'] = {'N': sorted(gr2), 'p': p1, 'a0': a1}
        db = {}
        for N in (32, 64):
            v = [nr['aufspaltung_max'] / nr['spanne'] for nr in ref['netze'] if int(nr['N']) == N and nr.get('regulaer')]
            if v:
                db[str(N)] = {'mittel': float(np.mean(v)), 'sd': float(np.std(v, ddof=1)), 'n': len(v)}
        ex['doppelbrechungsanteil_tg1'] = db
    res['exponent'] = ex
    res['laeufe'] = laufliste(a.lauf)
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(os.path.join(a.out, 'auswertung.json.tmp'), 'w') as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(os.path.join(a.out, 'auswertung.json.tmp'), os.path.join(a.out, 'auswertung.json'))
    tabellen(res, a.out)
    bild(res, gr, ref, a.out)
    print('fertig auswertung bz=%d dk=%d' % (len(bz), len(dk)), flush=True)


def f(x, nd=4):
    if x is None:
        return '-'
    if isinstance(x, float):
        return ('%.' + str(nd) + 'g') % x
    return str(x)


def pct(x):
    return '-' if x is None else '%.2f' % (100 * x)


def tabellen(res, out):
    L = ['# TT-GLAS-2: Tabellen (mechanisch aus auswertung.json; Punkt als Dezimalzeichen)', '']
    L += ['## Laeufe (aus den kleintest-Logs, UTC)', '', '| Lauf | Spur | Start | Ende | Dauer s | rc |', '|---|---|---|---|---|---|']
    for z in res['laeufe']:
        L.append('| %s | %s | %s | %s | %s | %s |' % (z['name'], z['spur'], (z['start'] or '-')[11:19], (z['ende'] or '-')[11:19],
                                                    z.get('dauer_s', '-'), z['rc']))
    L += ['', '## Stabilitaet je Netz (Aufgabe 1)', '',
          '| N | Saat | Klassen | vollst. | wachsend | Null bei Gamma | Null sonst | min omega^2 (ohne Gamma) | bei m | min omega^2 / s | A_red pd (ohne Gamma) | B_red neg max | Geraet | Laufzeit s |',
          '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for n in sorted(res['bz_netze'], key=lambda n: (n['N'], n['saat'])):
        L.append('| %d | %d | %d | %s | %d | %s | %d | %s | %s | %s | %s | %s | %s | %.0f |' % (
            n['N'], n['saat'], n['n_punkte'], 'ja' if n['vollstaendig'] else 'nein', n['n_wachsend'], n['n_null_gamma'], n['n_null_sonst'],
            f(n['w2_min']), n['w2_min_m'], f(n['w2_min_rel_skala'], 3), 'ja' if n['A_red_pd_alle'] else 'nein', n['B_red_neg_max'],
            n['geraet'], n['laufzeit_s']))
    L += ['', '## Zerlegung je Netz (Aufgabe 2; Spannen in Prozent)', '',
          '| N | Saat | (a) voll | (b) affin, nur Masse | (c) Ersatzmasse, Relaxation | (d) Kontrolle zu c | (e) unprojiziert | Anteil c/(b+c) | (a) regulaer | (c) gueltig | (c) neg. omega^2 max | Projektionsanteil max |',
          '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for n in sorted(res['dk_netze'], key=lambda n: (n['N'], n['saat'])):
        if not n['vollstaendig']:
            L.append('| %d | %d | unvollstaendig (ridx %s) | | | | | | | | | |' % (n['N'], n['saat'], n['ridx']))
            continue
        k = n['kennzahlen']
        sp = {v: (k[v]['spanne'] if k.get(v) else None) for v in VARIANTEN}
        ant = sp['c'] / (sp['b'] + sp['c']) if sp['b'] is not None and sp['c'] is not None else None
        L.append('| %d | %d | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
            n['N'], n['saat'], pct(sp['a']), pct(sp['b']), pct(sp['c']), pct(sp['d']), pct(sp['e']), f(ant, 3),
            'ja' if n.get('a_regulaer') else 'nein', ('ja' if n.get('c_gueltig') else 'nein') if 'c' in n['varianten'] else '-',
            n.get('c_n_negativ_max', '-'), f(n.get('proj_anteil_weg', {}).get('max'), 3)))
    L += ['', '## Mittel je N (Spanne, Aufspaltung, Doppelbrechungsanteil; Mittel +- SD, Prozent bzw. Anteil)', '',
          '| N | Variante | Netze | Spanne % | Aufspaltung max % | Richtungsspanne % | Doppelbrechungsanteil | omega^2/k^2 Mittel |', '|---|---|---|---|---|---|---|---|']
    for N, z in sorted(res['je_N'].items(), key=lambda t: int(t[0])):
        for v in VARIANTEN:
            if v not in z:
                continue
            q = z[v]
            L.append('| %s | %s | %d | %s +- %s | %s +- %s | %s +- %s | %s +- %s | %s |' % (
                N, v, q['spanne']['n'], pct(q['spanne']['mittel']), pct(q['spanne']['sd']), pct(q['aufspaltung_max']['mittel']),
                pct(q['aufspaltung_max']['sd']), pct(q['richtungsspanne']['mittel']), pct(q['richtungsspanne']['sd']),
                f(q['doppelbrechungsanteil']['mittel'], 3), f(q['doppelbrechungsanteil']['sd'], 2), f(q['w_mittel']['mittel'], 5)))
    L += ['', '## Urteile', '']
    for g in ('TG2-0', 'TG2-1', 'TG2-2', 'TG2-3'):
        L.append('- %s: nach Plan %s; nach Kartenwortlaut %s' % (g, res[g].get('plan'), res[g].get('wortlaut')))
    with open(os.path.join(out, 'tabellen.md'), 'w') as fh:
        fh.write('\n'.join(L) + '\n')


def bild(res, gr, ref, out):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    farbe = {128: '#2a78d6', 256: '#eb6834', 512: '#1baf7a', 1024: '#4a3aa7'}
    tx, tx2, grid = '#0b0b0b', '#52514e', '#e4e3df'
    plt.rcParams.update({'font.size': 9, 'axes.edgecolor': tx2, 'axes.labelcolor': tx, 'xtick.color': tx2, 'ytick.color': tx2,
                         'axes.titlesize': 10, 'axes.titleweight': 'bold'})
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.6), facecolor='#fcfcfb')
    for x in ax:
        x.set_facecolor('#fcfcfb')
        x.grid(True, color=grid, lw=0.6)
        for s in ('top', 'right'):
            x.spines[s].set_visible(False)
    # 1: kleinster Eigenwert ueber |k|
    for N in (128, 256):
        pts = np.array([p for n in res['bz_netze'] if n['N'] == N for p in n['punkte_eps_w2min'] if p[1] is not None and p[2] == 0], float)
        if len(pts):
            ax[0].scatter(pts[:, 0], pts[:, 1], s=14, color=farbe[N], alpha=0.55, edgecolors='none', label='N = %d (%d Netze)' % (
                N, len([n for n in res['bz_netze'] if n['N'] == N])))
    kk = np.linspace(0.05, 2.2, 100)
    ax[0].plot(kk, 4.9 * kk ** 2, color=tx2, lw=1.2, ls='--', label='4,9 k^2 (Schall, TT-GLAS-1)')
    ax[0].axhline(0, color=tx, lw=0.8)
    ax[0].set_yscale('symlog', linthresh=1e-2)
    ax[0].set_xlabel('|k| (Gitterpunkte des 6^3-Gitters, ohne Gamma)')
    ax[0].set_ylabel('kleinstes omega^2 (ohne Nullmoden)')
    ax[0].set_title('1  Kleinster Eigenwert je k')
    ax[0].legend(frameon=False, fontsize=8, loc='lower right')
    # 2: Spanne gegen N
    for nr in ref['netze']:
        if int(nr['N']) in (32, 64) and nr.get('regulaer'):
            ax[1].scatter(int(nr['N']), 100 * nr['spanne'], s=12, color='#b9b8b2', edgecolors='none')
    for N, v in sorted(gr.items()):
        ax[1].scatter([N] * len(v), 100 * v, s=14, color=farbe.get(N, tx2), alpha=0.6, edgecolors='none')
        ax[1].errorbar(N, 100 * v.mean(), yerr=(100 * v.std(ddof=1) if len(v) > 1 else 0), fmt='o', ms=7, color=farbe.get(N, tx2),
                       mec='#fcfcfb', mew=1.5, capsize=3, lw=1.5, label='N = %d: %.1f %% (%d Netze)' % (N, 100 * v.mean(), len(v)))
    ex = res.get('exponent', {}).get('dieser_lauf')
    if ex:
        xx = np.array([100, 1300])
        ax[1].plot(xx, 100 * np.exp(ex['a0'] + ex['p'] * np.log(xx)), color=tx, lw=1.5, label='Gerade dieser Lauf: N^%.2f' % ex['p'])
    ax[1].scatter([], [], s=12, color='#b9b8b2', label='TT-GLAS-1, N = 32, 64')
    ax[1].axhline(7, color=tx2, lw=0.8, ls=':')
    ax[1].text(30, 7.3, '7 % (TG2-3)', color=tx2, fontsize=8)
    ax[1].set_xscale('log')
    ax[1].set_yscale('log')
    ax[1].set_xlabel('N (Punkte je Superzelle)')
    ax[1].set_ylabel('Spanne von omega^2/k^2 je Netz (%)')
    ax[1].set_title('2  Spanne (a) gegen N')
    ax[1].legend(frameon=False, fontsize=7.5, loc='lower left')
    # 3: Doppelbrechungsanteil gegen N
    for n in res['dk_netze']:
        k = n.get('kennzahlen', {}).get('a') if n.get('vollstaendig') else None
        if k and k['doppelbrechungsanteil'] is not None:
            ax[2].scatter(n['N'], k['doppelbrechungsanteil'], s=14, color=farbe.get(n['N'], tx2), alpha=0.6, edgecolors='none')
    for N, z in sorted(res['je_N'].items(), key=lambda t: int(t[0])):
        if 'a' in z and z['a']['doppelbrechungsanteil']['mittel'] is not None:
            q = z['a']['doppelbrechungsanteil']
            ax[2].errorbar(int(N), q['mittel'], yerr=q['sd'] or 0, fmt='o', ms=7, color=farbe.get(int(N), tx2), mec='#fcfcfb', mew=1.5,
                           capsize=3, lw=1.5)
    db = res.get('exponent', {}).get('doppelbrechungsanteil_tg1', {})
    for N, q in db.items():
        ax[2].errorbar(int(N), q['mittel'], yerr=q['sd'], fmt='o', ms=6, color='#b9b8b2', capsize=3, lw=1.2)
    ax[2].set_xscale('log')
    ax[2].set_ylim(0, 1.05)
    ax[2].set_xlabel('N (Punkte je Superzelle)')
    ax[2].set_ylabel('Doppelbrechungsanteil = Aufspaltung / Spanne')
    ax[2].set_title('3  Doppelbrechungsanteil (a) gegen N')
    fig.text(0.01, 0.01, 'TT-GLAS-2, synthetische Gitterrechnung (.69), keine Messdaten. Grau: TT-GLAS-1.', color=tx2, fontsize=8)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(os.path.join(out, 'tg2-bild.png'), dpi=130, facecolor='#fcfcfb')


if __name__ == '__main__':
    main()
