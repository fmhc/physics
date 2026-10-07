#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UMKLAPP-1: mechanische Auswertung (Urteile UK0 bis UK3 nach PLAN.md Abschnitt 5).
Liest lauf/kontrolle-*.json, lauf/mb-*.json, lauf/tt-*.json und (f = 0 bei N = 256, Vergleich) die eingefrorenen
TT-GLAS-1-Laeufe; schreibt auswertung.json. tg_auswertung.netz_kennzahlen (TT-GLAS-1) wird unveraendert benutzt."""
import argparse, glob, json, os, sys, hashlib, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tg_auswertung as tga  # noqa: E402

TOL_UK0 = 1e-10
STEIG = (0.8, 1.2)
A_FIT = [1e-3, 1e-2, 3e-2]
A_KLEIN = (1e-4, 1e-3)
UK3_SCHWELLE = 0.2
TT_MIN = 0.99
F_HAUPT = 0.2


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def steigung(a, phi):
    a, phi = np.asarray(a, float), np.asarray(phi, float)
    if np.any(phi <= 0):
        return None
    A = np.vstack([np.ones_like(a), np.log(a)]).T
    c, *_ = np.linalg.lstsq(A, np.log(phi), rcond=None)
    return float(c[1])


def wortlaut_uk2(spek):
    """Kartenwortlaut UK2 je Netz: an allen Punkten genau 2 masselose, beide positiv, keine wachsende Mode;
    TT-Anteil >= 0,99 an den TT-Richtungen."""
    g = []
    for z in spek:
        for key in ('eps1', 'eps2'):
            if key in z:
                p = z[key]
                if p['n_masselos'] != 2 or len(p['w2k2_masselos']) != 2:
                    g.append('%s %s masselos %d' % (z['richtung'], key, p['n_masselos']))
                if p['n_wachsend'] > 0:
                    g.append('%s %s wachsend %d' % (z['richtung'], key, p['n_wachsend']))
        if 'tt_anteil' in z['eps1'] and (len(z['eps1']['tt_anteil']) < 2 or min(z['eps1']['tt_anteil']) < TT_MIN):
            g.append('%s TT %s' % (z['richtung'], z['eps1']['tt_anteil']))
    return g


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lauf', required=True)
    ap.add_argument('--ttglas', required=True, help='Ordner lauf/ von TT-GLAS-1 auf der .69')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    res = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'tga_sha256': sha(os.path.abspath(tga.__file__)),
                    'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}, 'eingaben': {}}

    # ------------------------------------------------------------------ UK0
    zeilen = []
    for p in sorted(glob.glob(os.path.join(a.lauf, 'kontrolle-*.json'))):
        d = json.load(open(p))
        res['eingaben'][os.path.basename(p)] = {'sha256': sha(p), 'uk_sha256': d['info']['skript_sha256']}
        for z in d['ergebnis']:
            for n in z['nach']:
                zeilen.append({'N': z['N'], 'saat': z['saat'], 'f': n['f'], 'n_zuege': n['zuege']['n_zuege'],
                               'n_ziel': n['zuege']['n_ziel'], 'S0': z['netz0']['S'], 'S': n['regge']['S'], 'dS': n['dS'],
                               'dS_rel': n['dS_rel'], 'eps_absmax': n['regge']['eps_absmax'],
                               'vol_summe_rel_abw': n['regge']['vol_summe_rel_abw'],
                               'vol_min_rel_mittel': n['regge']['vol_min_rel_mittel'], 'T': n['regge']['T'],
                               'E': n['regge']['E'], 'affin0': z['affin0'], 'affin': n['affin'],
                               'start': z['zugstat']['start'], 'anteil_zug_ok_ende': n['zuege']['anteil_zug_ok']})
    res['kontrolle'] = zeilen
    gueltig = [z for z in zeilen if z['n_zuege'] > 0]
    if gueltig:
        mrel = max(z['dS_rel'] for z in gueltig)
        mabs = max(abs(z['dS']) for z in gueltig)
        res['UK0'] = {'n_netze_f': len(gueltig), 'dS_rel_max': mrel, 'dS_abs_max': mabs,
                      'plan': 'eingetroffen' if mrel <= TOL_UK0 else 'verfehlt',
                      'wortlaut': 'eingetroffen' if mabs <= TOL_UK0 else 'verfehlt'}
    else:
        res['UK0'] = {'plan': 'nicht entscheidbar', 'wortlaut': 'nicht entscheidbar'}

    # ------------------------------------------------------------------ UK1 (M-B)
    netze = []
    for p in sorted(glob.glob(os.path.join(a.lauf, 'mb-*.json'))):
        d = json.load(open(p))
        res['eingaben'][os.path.basename(p)] = {'sha256': sha(p), 'uk_sha256': d['info']['skript_sha256']}
        netze += d['ergebnis']
    mb = {'n_netze': len(netze), 'selbsttest_a0_alle': bool(all(z['selbsttest_a0'] for z in netze)) if netze else None,
          'saum_verletzt_max': max([max(r['saum_verletzt']) for z in netze for r in z['zufall']] or [None]) if netze else None}
    gruppen = {}
    for N in sorted(set(z['N'] for z in netze)):
        gruppen[str(N)] = [z for z in netze if z['N'] == N]
    gruppen['alle'] = netze
    A = netze[0]['a'] if netze else []
    for gname, gz in gruppen.items():
        if not gz:
            continue
        phiT = np.array([[np.mean(r['n_weg']) / z['T0'] for r in z['zufall']] for z in gz])     # (Netze, a)
        phiF = np.array([[np.mean(r['n_verletzt']) / z['F0'] for r in z['zufall']] for z in gz])
        ncl = np.array([[np.sum(r['n_cluster']) for r in z['zufall']] for z in gz]).sum(0)
        n23 = np.array([[np.sum(r['n_23']) for r in z['zufall']] for z in gz]).sum(0)
        n32 = np.array([[np.sum(r['n_32']) for r in z['zufall']] for z in gz]).sum(0)
        nso = np.array([[np.sum(r['n_sonst']) for r in z['zufall']] for z in gz]).sum(0)
        nweg = np.array([[np.sum(r['n_weg']) for r in z['zufall']] for z in gz]).sum(0)
        m_T, m_F = phiT.mean(0), phiF.mean(0)
        se_T = phiT.std(0, ddof=1) / np.sqrt(len(gz)) if len(gz) > 1 else np.full(len(A), np.nan)
        idx = [A.index(x) for x in A_FIT]
        i0, i1 = A.index(A_KLEIN[0]), A.index(A_KLEIN[1])
        s_lok = (float(np.log(m_T[i1] / m_T[i0]) / np.log(A_KLEIN[1] / A_KLEIN[0]))
                 if m_T[i0] > 0 and m_T[i1] > 0 else None)
        dehn = np.array([[np.array(r['n_verletzt']) / z['F0'] for r in z['dehnung']] for z in gz])   # (Netze, 6, a)
        mu_cdf = {x: float(np.sum([z['mu0_cdf'][x] for z in gz]) / np.sum([z['F0'] for z in gz])) for x in gz[0]['mu0_cdf']}
        xs = sorted(mu_cdf, key=float)
        mb[gname] = {'n_netze': len(gz), 'a': A, 'phi_T': m_T.tolist(), 'phi_T_se': se_T.tolist(), 'phi_F': m_F.tolist(),
                     'phi_T_durch_a': (m_T / np.array(A)).tolist(),
                     'steigung_T_1e-3_3e-2': steigung(A_FIT, m_T[idx]), 'steigung_F_1e-3_3e-2': steigung(A_FIT, m_F[idx]),
                     'steigung_T_alle': steigung(A, m_T), 'steigung_T_lokal_1e-4_1e-3': s_lok,
                     'cluster': ncl.tolist(), 'cluster_23': n23.tolist(), 'cluster_32': n32.tolist(), 'cluster_sonst': nso.tolist(),
                     'tetra_weg_summe': nweg.tolist(),
                     'dehnung_phi_F': dehn.mean(axis=(0, 1)).tolist(),
                     'dehnung_steigung_1e-3_3e-2': steigung(A_FIT, dehn.mean(axis=(0, 1))[idx]),
                     'mu0_cdf': mu_cdf, 'mu0_cdf_steigung': steigung([float(x) for x in xs], [mu_cdf[x] for x in xs]),
                     'mu0_min': float(min(z['mu0_min'] for z in gz)), 'mu0_n_neg': int(sum(z['mu0_n_neg'] for z in gz))}
    res['mb'] = mb
    if netze and '128' in mb and '256' in mb:
        sw = mb['alle']['steigung_T_1e-3_3e-2']
        inb = lambda s: s is not None and STEIG[0] <= s <= STEIG[1]  # noqa: E731
        s128, s256 = mb['128']['steigung_T_1e-3_3e-2'], mb['256']['steigung_T_1e-3_3e-2']
        ohne = (mb['128']['phi_T'][0] > 0 and mb['256']['phi_T'][0] > 0 and inb(mb['alle']['steigung_T_lokal_1e-4_1e-3']))
        res['UK1'] = {'steigung_alle': sw, 'steigung_128': s128, 'steigung_256': s256,
                      'steigung_lokal_alle': mb['alle']['steigung_T_lokal_1e-4_1e-3'], 'ohne_schwelle': bool(ohne),
                      'plan': 'eingetroffen' if (inb(s128) and inb(s256) and ohne) else 'verfehlt',
                      'wortlaut': 'eingetroffen' if inb(sw) else 'verfehlt'}
    else:
        res['UK1'] = {'plan': 'nicht entscheidbar', 'wortlaut': 'nicht entscheidbar'}

    # ------------------------------------------------------------------ TT (UK2, UK3)
    teile = {}

    def nimm(key, e, quelle, pfad):
        t = teile.setdefault(key, {'spektrum': {}, 'pruefung': e['pruefung'], 'zugstat': e.get('zugstat'), 'quelle': quelle})
        for z in e['spektrum']:
            t['spektrum'][z['ridx']] = z
        t.setdefault('dateien', []).append(os.path.basename(pfad))
    for p in sorted(glob.glob(os.path.join(a.lauf, 'tt-*.json'))):
        d = json.load(open(p))
        res['eingaben'][os.path.basename(p)] = {'sha256': sha(p), 'uk_sha256': d['info']['skript_sha256'], 'laufzeit_s': d['laufzeit_s']}
        for e in d['ergebnis']:
            nimm((int(e['N']), int(e['saat']), float(e['f'])), e, 'UMKLAPP-1', p)
    # TT-GLAS-1 (f = 0): N = 256 als Ausgangswert, N = 128 nur zum Vergleich
    tg_ref = {}
    for p in sorted(glob.glob(os.path.join(a.ttglas, 'netz-N*-s*.json'))):
        d = json.load(open(p))
        e = d['ergebnis']
        tg_ref[(int(e['N']), int(e['saat']))] = (e, p, d['info']['skript_sha256'])
    vergleich = []
    for (N, s, f), t in sorted(teile.items()):
        if f == 0.0 and (N, s) in tg_ref:
            e, p, _ = tg_ref[(N, s)]
            ref = {z['ridx']: z for z in e['spektrum']}
            dev = []
            for r, z in t['spektrum'].items():
                w1, w0 = np.array(z['eps1']['w2k2_masselos']), np.array(ref[r]['eps1']['w2k2_masselos'])
                if len(w1) == len(w0) and len(w0):
                    dev.append(float(np.max(np.abs(w1 / w0 - 1))))
            vergleich.append({'N': N, 'saat': s, 'ridx': sorted(t['spektrum']), 'w2k2_rel_abw_max': max(dev) if dev else None,
                              'ttglas_datei': os.path.basename(p), 'ttglas_sha256': sha(p)})
    res['vergleich_ttglas_f0'] = vergleich
    for (N, s), (e, p, tsha) in tg_ref.items():
        if N == 256 and (N, s, 0.0) in teile and len(teile[(N, s, 0.0)]['spektrum']) < 13:
            teile[(N, s, 0.0)] = {'spektrum': {z['ridx']: z for z in e['spektrum']}, 'pruefung': e['pruefung'], 'zugstat': None,
                                  'quelle': 'TT-GLAS-1', 'dateien': [os.path.basename(p)]}
            res['eingaben']['ttglas/' + os.path.basename(p)] = {'sha256': sha(p), 'tg_sha256': tsha}
    nl = []
    for (N, s, f), t in sorted(teile.items()):
        if sorted(t['spektrum']) != list(range(13)):
            nl.append({'N': N, 'saat': s, 'f': f, 'vollstaendig': False, 'ridx': sorted(t['spektrum'])})
            continue
        spek = [t['spektrum'][r] for r in range(13)]
        kz = tga.netz_kennzahlen(spek)
        w = np.array(kz['w2k2'], float)
        kz.update({'N': N, 'saat': s, 'f': f, 'vollstaendig': True, 'quelle': t['quelle'], 'dateien': t['dateien'],
                   'tempo_mittel': float(np.sqrt(w).mean()) if np.isfinite(w).all() else None,
                   'uk2_wortlaut_gruende': wortlaut_uk2(spek)[:10], 'uk2_wortlaut_ok': len(wortlaut_uk2(spek)) == 0,
                   'pruefung': t['pruefung'], 'zugstat': t['zugstat']})
        nl.append(kz)
    res['tt_netze'] = nl
    voll = [n for n in nl if n['vollstaendig']]
    tab = []
    for N in sorted(set(n['N'] for n in voll)):
        for f in sorted(set(n['f'] for n in voll if n['N'] == N)):
            g = [n for n in voll if n['N'] == N and n['f'] == f]
            reg = [n for n in g if n['regulaer']]
            sp_ = np.array([n['spanne'] for n in reg]) if reg else np.array([])
            zeile = {'N': N, 'f': f, 'n': len(g), 'n_regulaer': len(reg), 'n_uk2_wortlaut': sum(n['uk2_wortlaut_ok'] for n in g),
                     'saaten': [n['saat'] for n in g],
                     'spanne': [n.get('spanne') for n in g], 'spanne_mittel': float(sp_.mean()) if len(sp_) else None,
                     'spanne_sd': float(sp_.std(ddof=1)) if len(sp_) > 1 else None,
                     'w_mittel': float(np.mean([n['w_mittel'] for n in reg])) if reg else None,
                     'tempo_mittel': float(np.mean([n['tempo_mittel'] for n in reg])) if reg else None,
                     'aufspaltung_max_mittel': float(np.mean([n['aufspaltung_max'] for n in reg])) if reg else None,
                     'richtungsspanne_mittel': float(np.mean([n['richtungsspanne_mittel_zweige'] for n in reg])) if reg else None,
                     'n_wachsend_max': int(max(n['n_wachsend_max'] for n in g)), 'n_unklar_max': int(max(n['n_unklar_max'] for n in g)),
                     'A_red_pd_alle': bool(all(n['A_red_pd_alle'] for n in g)), 'B_red_neg_max': int(max(n['B_red_neg_max'] for n in g)),
                     'tt_min': min([n['tt_min'] for n in g if n['tt_min'] is not None] or [None]),
                     'lin_max': max([n['lin_max'] for n in g if n['lin_max'] is not None] or [None]),
                     'luecke_min': min([n['luecke_min'] for n in g if n['luecke_min'] is not None] or [None]),
                     'f_eff': [n['zugstat']['ende']['f_eff'] if n.get('zugstat') else 0.0 for n in g],
                     'T': [n['pruefung']['T'] for n in g], 'E': [n['pruefung']['E'] for n in g],
                     'vol_min_rel_mittel': [n['pruefung']['vol_min_rel_mittel'] for n in g],
                     'D_absmax': [n['pruefung']['D_absmax'] for n in g],
                     'dieder_summe_minus_2pi_max': max(n['pruefung']['dieder_summe_minus_2pi_max'] for n in g),
                     'volumen_summe_rel_abw_max': max(n['pruefung']['volumen_summe_rel_abw'] for n in g)}
            tab.append(zeile)
    res['tabelle_tt'] = tab
    # UK2
    g02 = [n for n in voll if n['f'] == F_HAUPT]
    Ns02 = sorted(set(n['N'] for n in g02))
    if g02:
        res['UK2'] = {'N': Ns02, 'n_netze': len(g02), 'n_regulaer': sum(n['regulaer'] for n in g02),
                      'n_wortlaut_ok': sum(n['uk2_wortlaut_ok'] for n in g02),
                      'nicht_regulaer': [{'N': n['N'], 'saat': n['saat'], 'gruende': n['gruende'][:5]} for n in g02 if not n['regulaer']],
                      'plan': 'eingetroffen' if all(n['regulaer'] for n in g02) else 'verfehlt',
                      'wortlaut': 'eingetroffen' if all(n['uk2_wortlaut_ok'] for n in g02) else 'verfehlt'}
        if Ns02 != [128, 256]:
            res['UK2']['vermerk'] = 'nicht beide N vollstaendig'
    else:
        res['UK2'] = {'plan': 'nicht entscheidbar', 'wortlaut': 'nicht entscheidbar'}
    # UK3
    paare = []
    for fv in sorted(set(n['f'] for n in voll if n['f'] > 0)):
        for n in [x for x in voll if x['f'] == fv]:
            b = [x for x in voll if x['f'] == 0.0 and x['N'] == n['N'] and x['saat'] == n['saat']]
            if b and b[0]['regulaer'] and n['regulaer']:
                paare.append({'N': n['N'], 'saat': n['saat'], 'f': fv, 'spanne0': b[0]['spanne'], 'spanne_f': n['spanne'],
                              'r': n['spanne'] / b[0]['spanne'] - 1, 'w_rel': n['w_mittel'] / b[0]['w_mittel'] - 1,
                              'tempo_rel': n['tempo_mittel'] / b[0]['tempo_mittel'] - 1})
    res['paare'] = paare
    p02 = [p for p in paare if p['f'] == F_HAUPT]
    if p02:
        rr = np.abs([p['r'] for p in p02])
        res['UK3'] = {'n_paare': len(p02), 'abs_r': rr.tolist(), 'median_abs_r': float(np.median(rr)), 'min_abs_r': float(rr.min()),
                      'mittel_r': float(np.mean([p['r'] for p in p02])),
                      'plan': 'eingetroffen' if np.median(rr) > UK3_SCHWELLE else 'verfehlt',
                      'wortlaut': 'eingetroffen' if rr.min() > UK3_SCHWELLE else 'verfehlt'}
    else:
        res['UK3'] = {'plan': 'nicht entscheidbar', 'wortlaut': 'nicht entscheidbar'}
    # Zufallsniveau (beschreibend): |s_j / s_i - 1| fuer verschiedene TT-GLAS-1-Netze gleicher Groesse
    pa = os.path.join(a.ttglas, 'auswertung.json')
    if os.path.exists(pa):
        aw = json.load(open(pa))
        res['eingaben']['ttglas/auswertung.json'] = {'sha256': sha(pa)}
        zn = {}
        for N in (128, 256):
            s_ = [n['spanne'] for n in aw['netze'] if n.get('vollstaendig') and n.get('regulaer') and n['N'] == N]
            r_ = [abs(s_[j] / s_[i] - 1) for i in range(len(s_)) for j in range(len(s_)) if i != j]
            zn[str(N)] = {'n_netze': len(s_), 'median_abs_r': float(np.median(r_)) if r_ else None,
                          'anteil_ueber_0_2': float(np.mean(np.array(r_) > UK3_SCHWELLE)) if r_ else None}
        res['zufallsniveau_ttglas'] = zn
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig auswertung', len(nl), 'tt-netze', len(netze), 'mb-netze', flush=True)


if __name__ == '__main__':
    main()
