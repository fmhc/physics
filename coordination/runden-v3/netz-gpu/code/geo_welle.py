# -*- coding: utf-8 -*-
"""Demo 1: Schwerewellen-Paket auf V (Richtungsgleichheit sichtbar), Datensatz netz-gpu/1. Synthetisch, linear um flach.

Stufen:
  spektrum  --n N --teil i --nteil m : Projekt-Bloecke (CPU) an den k der Halbmenge K+ der Superzelle, Reduktion auf
            der GPU, TT-Moden (w2, u, Bu, P) als Zwischenstand lauf/geo/spek-n<N>-h<..>-t<i>.npz
  datensatz --n N : Zwischenstaende laden, TT-Paket (Gauss-Huelle, zirkulare Polarisation um z, qd = 0) spektral exakt
            entwickeln, in den Ortsraum von netz.py synthetisieren, Pruefungen, Datensatz schreiben.
"""
import argparse
import copy
import json
import math
import os
import sys
import time

import numpy as np
import torch

sys.path.insert(0, '/home/fmh/fmhc-physics-remote/netz-gpu/code')
from netzgpu.netz import Netz  # noqa: E402
from netzgpu.datensatz import Datensatz, platte_frei_gb  # noqa: E402
from netzgpu import geometrie as geo  # noqa: E402

LAUF = '/home/fmh/fmhc-physics-remote/netz-gpu/lauf/geo'
ZIEL = '/home/fmh/fmhc-physics-remote/netz-gpu/datensaetze/schwerewelle-v'


def log(*a):
    print(time.strftime('%H:%M:%S'), *a, flush=True)


def spek_pfad(n, h, teil):
    return os.path.join(LAUF, 'spek-n%d-h%d-t%d.npz' % (n, round(-math.log2(h)), teil))


def stufe_spektrum(a):
    gi = geo.KGitter(a.n)
    idx = np.array_split(np.arange(gi.K), a.nteil)[a.teil]
    log('K+ =', gi.K, 'teil', a.teil, 'von', a.nteil, ':', len(idx), 'k')
    P = geo.Projekt(a.h)
    bl = P.bloecke_viele(gi.ks[idx], log=log, alle=250)
    log('bloecke', bl['t_s'], 's, je k', bl['t_s'] / len(idx), 'gruende', bl['gruende'])
    torch.cuda.synchronize()
    t0 = time.time()
    sp = geo.reduktion_gpu(bl, gi.ks[idx])
    torch.cuda.synchronize()
    t_red = time.time() - t0
    log('reduktion gpu', t_red, 's')
    np.savez(spek_pfad(a.n, a.h, a.teil) + '.tmp.npz', idx=idx, ks=gi.ks[idx],
             **{x: sp[x].cpu().numpy() for x in ('w2', 'u', 'Bu', 'P', 'gueltig', 'tt_ok', 'n_neg', 'n_null', 'luecke',
                                                  'n_wachsend', 'rang_rel', 'M_min_rel')},
             t_bloecke=bl['t_s'], t_red=t_red, gpu_max_MB=torch.cuda.max_memory_allocated() / 1e6)
    os.replace(spek_pfad(a.n, a.h, a.teil) + '.tmp.npz', spek_pfad(a.n, a.h, a.teil))
    log('gespeichert', spek_pfad(a.n, a.h, a.teil))


def lade_spektrum(n, h, nteil, dev='cuda'):
    gi = geo.KGitter(n)
    teile = [np.load(spek_pfad(n, h, t)) for t in range(nteil)]
    idx = np.concatenate([z['idx'] for z in teile])
    assert sorted(idx.tolist()) == list(range(gi.K))
    o = np.argsort(idx)
    sp = {}
    for x in ('w2', 'u', 'Bu', 'P', 'gueltig', 'tt_ok', 'n_neg', 'n_null', 'luecke', 'n_wachsend'):
        v = np.concatenate([z[x] for z in teile])[o]
        sp[x] = torch.as_tensor(v, device=dev)
    info = {'t_bloecke_s': float(sum(float(z['t_bloecke']) for z in teile)),
            't_red_gpu_s': float(sum(float(z['t_red']) for z in teile))}
    return gi, sp, info


def ecken_halb(netz, x):
    """Kantengroesse x (N_k,) je zur Haelfte auf beide Ecken: (N_e,)."""
    e = torch.zeros(netz.N_e, dtype=x.dtype, device=x.device)
    e.index_add_(0, netz.kanten[:, 0], 0.5 * x)
    e.index_add_(0, netz.kanten[:, 1], 0.5 * x)
    return e


def stufe_datensatz(a):
    t_start = time.time()
    frei = platte_frei_gb()
    log('Platte frei %.1f GB' % frei)
    if frei < 10.0:
        raise SystemExit('Platte unter 10 GB frei')
    dev = 'cuda'
    t0 = time.time()
    N = Netz('V', (a.n, a.n, a.n))
    torch.cuda.synchronize()
    t_netz = time.time() - t0
    log('Netz', N.N_e, N.N_k, N.N_d, N.N_t, '%.1f s' % t_netz)
    P = geo.Projekt(a.h)
    zo = geo.NetzZuordnung(P, N)
    log('Zuordnung', json.dumps(zo.info()))
    gi, sp, spinfo = lade_spektrum(a.n, a.h, a.nteil, dev)
    x0 = (a.n / 2.0, a.n / 2.0, a.n / 2.0)
    W = geo.TTWelle(P, zo, gi, sp, sigma=a.sigma, x0=x0, H='zirkular_z', amplitude=a.amplitude)
    log('TTWelle: ausgelassen', W.n_ausgelassen, 'g_max dort', W.g_ausgelassen_max, 'skala', W.skala)
    zeiten = [a.dt * i for i in range(a.bilder)]
    E_k = W.energie_k()
    E_kt = W.energie_k_t(zeiten)
    # Pruefungen bei t = 0
    f0 = W.felder([0.0])
    pr_regge = geo.pruefe_regge(N, f0['q'][:, 0] / f0['q'][:, 0].abs().max(), f0['Bq'][:, 0] / f0['q'][:, 0].abs().max())
    pr_eich = geo.pruefe_eichkern(P, zo, gi, n_k=24)
    log('regge', json.dumps(pr_regge), 'eichkern', json.dumps(pr_eich))
    # Datensatz
    quelle = {'lauf': os.path.join(LAUF, 'welle-datensatz.log'), 'skript': os.path.abspath(__file__),
              'modell': 'TT-Schwerewellen der stetigen Grenze (UEBERLEITUNG-V-2): B 3D-Regge, M_eff 4D-Zeltstangen bei '
                        'h = 2^-%d, Lapse R1, Reduktion R1; spektral exakt je Mode' % round(-math.log2(a.h)),
              'hinweis': 'synthetisch, keine Messdaten, linear um flach',
              'anfang': 'q = TT-Anteil von exp(-|k|^2 sigma^2/2) e^{ik(x-x0)} n.H.n/2, H = e+ + i ex um z, qd = 0',
              'sigma_a': a.sigma, 'x0_a': list(x0), 'h': a.h, 'amplitude_max_dehnung_t0': a.amplitude,
              'k_halbmenge': gi.K, 'k_voll': gi.K_voll, 'k_ausgelassen': W.n_ausgelassen,
              'g_ausgelassen_max': W.g_ausgelassen_max}
    ds = Datensatz(ZIEL, 'Schwerewellen-Paket auf V (Richtungsgleichheit sichtbar)', N, quelle=quelle,
                   hinweis='synthetisch, keine Messdaten, linear um flach')
    ds.groesse('dehnung', 'kante', 1, 'TT-Schwerewelle: relative Laengenaenderung delta l / l (linear um flach)',
               symmetrisch=True)
    ds.groesse('energie', 'ecke', 1, 'Energiedichte je Ecke: 1/2 (p qd + q B q) je Kante, halb auf beide Ecken '
               '(Summe = Gesamtenergie; oertlich auch negativ moeglich, M_eff indefinit)')
    rmax = a.n / 2.0
    skala = {"q": 0.0, "emin": 0.0, "emax": 0.0}
    # Vergleichslauf: dieselben Moden und Anfangswerte, aber Frequenz exakt |k| (isotrop, ohne Gitterdispersion)
    Wk = copy.copy(W)
    kabs = torch.linalg.norm(torch.as_tensor(gi.ks, dtype=torch.float64, device=dev), dim=1)
    Wk.w = kabs[:, None].repeat(1, W.w.shape[1])
    E_real = []
    zr = {'R_gitter': [], 'R_kontinuum': [], 'R_energie': []}
    gr = 6
    for g0 in range(0, len(zeiten), gr):
        tz = zeiten[g0:g0 + gr]
        f = W.felder(tz)
        Fk, T = Wk.koeff(tz)
        qk_alle = zo.synthese(Fk[..., :T], gi.ks)
        del Fk
        for i, t in enumerate(tz):
            q = f['q'][:, i]
            ev = f['energie_ecke'][:, i]
            Er = float(f['eps_kante'][:, i].sum())
            E_real.append(Er)
            neg = float(ev.clamp_max(0.0).abs().sum() / ev.abs().sum())
            rg = geo.schalenradien(N, ecken_halb(N, q * q), x0, rmax)
            rk = geo.schalenradien(N, ecken_halb(N, qk_alle[:, i] ** 2), x0, rmax)
            re = geo.schalenradien(N, ev, x0, rmax)
            ds.bild(t, dehnung=q, energie=ev)
            if t >= a.t_skala - 1e-12:
                skala["q"] = max(skala["q"], float(q.abs().max()))
                skala["emin"] = min(skala["emin"], float(ev.min()))
                skala["emax"] = max(skala["emax"], float(ev.max()))
            ds.diagnose('energie_gesamt', Er)
            ds.diagnose('energie_moden', E_kt[g0 + i])
            ds.diagnose('energie_neg_anteil', neg)
            ver = np.array([rg[x] / rk[x] for x in ('100', '110', '111')])
            for j, nm in enumerate(('100', '110', '111')):
                ds.diagnose('radius_' + nm, rg[nm])
                ds.diagnose('radius_' + nm + '_kontinuum', rk[nm])
                ds.diagnose('radius_' + nm + '_energie', re[nm])
            ds.diagnose('radius_spanne', rg['spanne'])
            ds.diagnose('radius_spanne_kontinuum', rk['spanne'])
            ds.diagnose('isotropie_kennzahl', float(ver.max() / ver.min() - 1))
            ds.diagnose('verzoegerung_mittel', float(np.mean([rg[x] - rk[x] for x in ('100', '110', '111')])))
            zr['R_gitter'].append(rg)
            zr['R_kontinuum'].append(rk)
            zr['R_energie'].append(re)
            log('t %.3f E %.12e neg %.3f | q2: R100 %.4f R110 %.4f R111 %.4f | kont %.4f %.4f %.4f | kennz %.2e | E-gew %.4f %.4f %.4f' % (
                t, Er, neg, rg['100'], rg['110'], rg['111'], rk['100'], rk['110'], rk['111'], ver.max() / ver.min() - 1,
                re['100'], re['110'], re['111']))
        del f, qk_alle
    E_real = np.array(E_real)
    zus = {'energie_k_exakt': E_k, 'energie_real_rel_streuung': float((E_real.max() - E_real.min()) / E_real.mean()),
           'energie_real_gegen_k_rel': float(np.abs(E_real / E_k - 1).max()),
           'energie_moden_gegen_k_rel': float(np.abs(np.array(E_kt) / E_k - 1).max()),
           'pruefung_regge_fd': pr_regge, 'pruefung_eichkern': pr_eich, 'zuordnung': zo.info(),
           'spektrum': {'n_neg_Meff': sorted(set(sp['n_neg'].cpu().tolist())), 'n_null_max': int(sp['n_null'].max()),
                        'n_wachsend_max': int(sp['n_wachsend'].max()), 'gueltig': int(sp['gueltig'].sum()),
                        'tt_ok': int(sp['tt_ok'].sum()), **spinfo},
           'radius_kegel_grad': 20.0, 'radius_rmax_a': rmax,
           'radius_hinweis': 'radius_<r>: mit q^2 (je Ecke) gewichteter mittlerer Abstand von x0 in 20-Grad-Kegeln um alle '
                             'zu <r> gleichwertigen Richtungen (gepoolt), nur r < n/2; _kontinuum: dieselbe Messung fuer '
                             'dieselben Moden und Anfangswerte mit omega = |k| exakt (isotrop, ohne Gitterdispersion); '
                             'isotropie_kennzahl = max/min - 1 von radius/radius_kontinuum ueber [100], [110], [111]; '
                             'verzoegerung_mittel = Mittel von radius - radius_kontinuum; _energie: energiegewichtet '
                             '(nur positive Anteile, beschreibend). radius_spanne_kontinuum zeigt, wieviel Spanne schon '
                             'Polarisationsmuster, Nahfeld und Ecken-Stichprobe der Kegel erzeugen. Ab t ~ n/2 - 2 sigma '
                             'reichen periodische Bilder in die Kegel.'}
    ds.groesse('dehnung', 'kante', 1, 'TT-Schwerewelle: relative Laengenaenderung delta l / l (linear um flach); Farbskala aus den '
               'Bildern ab t = %g (fruehere Bilder uebersteuern)' % a.t_skala, vmin=-skala['q'], vmax=skala['q'])
    ds.groesse('energie', 'ecke', 1, 'Energiedichte je Ecke: 1/2 (p qd + q B q) je Kante, halb auf beide Ecken (Summe = '
               'Gesamtenergie; oertlich auch negativ moeglich, M_eff indefinit); Farbskala aus den Bildern ab t = %g' % a.t_skala,
               vmin=skala['emin'], vmax=skala['emax'])
    zus['farbskala_ab_t'] = a.t_skala
    ds.setze('geometrie_zusammenfassung', zus)
    p = ds.schliessen()
    zus['radien'] = zr
    zus['t_netz_s'] = t_netz
    zus['t_gesamt_s'] = time.time() - t_start
    zus['gpu_max_MB'] = torch.cuda.max_memory_allocated() / 1e6
    zus['datensatz_MB'] = ds.bytes / 1e6
    with open(os.path.join(LAUF, 'welle-zusammenfassung.json'), 'w') as fh:
        json.dump(zus, fh, indent=1)
    log('fertig', p, json.dumps({k: zus[k] for k in ('energie_real_rel_streuung', 'energie_real_gegen_k_rel',
                                                       'energie_moden_gegen_k_rel', 't_gesamt_s', 'gpu_max_MB', 'datensatz_MB')}))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('stufe', choices=['spektrum', 'datensatz'])
    ap.add_argument('--n', type=int, default=12)
    ap.add_argument('--h', type=float, default=2.0 ** -10)
    ap.add_argument('--teil', type=int, default=0)
    ap.add_argument('--nteil', type=int, default=1)
    ap.add_argument('--sigma', type=float, default=1.0)
    ap.add_argument('--amplitude', type=float, default=1e-3)
    ap.add_argument('--dt', type=float, default=0.25)
    ap.add_argument('--bilder', type=int, default=17)
    ap.add_argument('--t_skala', type=float, default=1.5)
    a = ap.parse_args()
    if a.stufe == 'spektrum':
        stufe_spektrum(a)
    else:
        stufe_datensatz(a)


if __name__ == '__main__':
    main()
