#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NETZ-NICHTLINEAR-1, Kreuzungsscan (Zusatz, nach Sicht des ersten G1-Laufs).

Faehrt nn.lauf (G1) bis zum K-ten ausgefuehrten Zug. An jedem dieser Zuege wird M_eff der NEUEN Zerlegung an mehreren
Geometrien gerechnet:
  - 'hg': am ungedehnten Hintergrund (Lesart H, wie UMKLAPP-FOLGE-1),
  - 'tau': am gedehnten Netz zur Zeit t_e + tau, Zustand aus der freien Bahn x(tau) = x_e + tau v1 - tau^2/2 v2 mit den
    Operatoren vor dem Zug (wie die Bisektion in td.lauf); neue Kante aus der flachen Doppelpyramide.
Je Punkt: mu der alten Flaeche (gedehnt), Zahl der negativen M_eff-Richtungen, die vier betragskleinsten Eigenwerte
(relativ, mit Vorzeichen), A_red definit, wachsende Moden, w2_max.
Danach wird der Lauf ueber das Budget beendet. Importiert nn unveraendert (Haken nn.HAKEN).
"""
import argparse, json, os, sys, time
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import nn  # noqa: E402
import td  # noqa: E402
import tg  # noqa: E402

TAUK = [-30.0, -3.0, -0.3, -0.03, 0.0, 0.03, 0.3, 3.0, 30.0]
ZUST = {'n': 0, 'K': 1, 'args': None}


def punkt(N, Gn, On, besch, j, a_s, LV, pos, k1, hp, hx, rolle, gedehnt=True):
    L9s = N.l9_0[j] * (1.0 + a_s[N.f9[j]])
    mu_s = float(td.mu_bipyr(L9s[None, :])[0])
    lde = float(td.l_de_flach(L9s[None, :])[0]) if besch['kante_neu'] is not None else None

    def fn(N2):
        idx, ok = N2.idx_von_keys(N.keys)
        fv = np.ones(N2.E)
        fv[idx[ok]] = 1.0 + a_s[ok]
        if besch['kante_neu'] is not None:
            inew, okn = N2.idx_von_keys(np.array([besch['kante_neu']]))
            fv[inew[0]] = lde / N2.l0[inew[0]]
        return fv
    t = time.time()
    if gedehnt:
        Ns = nn.NetzG(LV, pos, Gn, On, k1, hp, hx, f_fn=fn, rolle=rolle)
    else:
        Ns = nn.NetzG(LV, pos, Gn, On, k1, hp, hx, rolle=rolle)
    ev = np.linalg.eigvalsh(Ns.M)
    sm = float(np.abs(ev).max())
    o = np.argsort(np.abs(ev))[:4]
    return {'mu_alt_flaeche': mu_s, 'M_n_neg': int((ev < -1e-10 * sm).sum()),
            'ev_klein_rel': sorted(float(ev[i] / sm) for i in o), 'A_pd': bool(Ns.A_pd), 'n_A_neg': int(Ns.n_A_neg),
            'n_wachsend': Ns.eig['n_wachsend'], 'w2_max': Ns.eig['w2_max'], 'w2_wachsend': Ns.eig['w2_wachsend'],
            't_s': time.time() - t}


def haken(N, Gn, On, besch, a_alt, j, typ, mu_hg, LV, pos, k1, hp, hx):
    fr = sys._getframe(1).f_locals
    xe, ye, dt = fr['xe'], fr['ye'], fr['dt']
    v1 = N.Ar @ ye
    v2 = N.Ar @ (N.Br @ xe)
    out = {'typ': typ, 'mu_hg': mu_hg, 'dt': dt}
    out['hg'] = punkt(N, Gn, On, besch, j, np.zeros(N.E), LV, pos, k1, hp, hx, 'scan_hg', gedehnt=False)
    out['tau'] = []
    for k in TAUK:
        tau = k * dt
        xs = xe + tau * v1 - 0.5 * tau * tau * v2
        p = punkt(N, Gn, On, besch, j, N.S @ xs, LV, pos, k1, hp, hx, 'scan_tau')
        p['tau_dt'] = k
        out['tau'].append(p)
        print('scan zug %d tau %g dt: mu %.3e neg %d ev %s' % (ZUST['n'] + 1, k, p['mu_alt_flaeche'], p['M_n_neg'],
                                                              p['ev_klein_rel']), flush=True)
    ZUST['n'] += 1
    if ZUST['n'] >= ZUST['K']:
        ZUST['args'].budget = 0.0          # Lauf endet am naechsten Schrittbeginn
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--netz', default='glas-N128-s1')
    ap.add_argument('--lesart', default='P', choices=['R', 'P'])
    ap.add_argument('--K', type=int, default=1)
    ap.add_argument('--bgd', type=int, default=1)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    args = argparse.Namespace(netz=a.netz, A=1e-3, arm='b', lesart=a.lesart, h=0.5, perioden=10, proben=200,
                              budget=540.0, split=0, vergleich=0, hmax=100.0, zugmax=200, out=a.out)
    nn.B_GD['an'] = bool(a.bgd)
    ZUST['K'] = a.K
    ZUST['args'] = args
    nn.HAKEN['zug'] = haken
    t0 = time.time()
    erg = nn.lauf(args)
    res = {'info': {'argv': sys.argv, 'skript_sha256': td.sha(os.path.abspath(__file__)),
                    'nn_sha256': td.sha(os.path.abspath(nn.__file__)), 'tauk': TAUK},
           'scans': [e.get('scan') for e in erg['ereignisse'] if e.get('scan')],
           'ereignisse': [{k: v for k, v in e.items() if k != 'scan'} for e in erg['ereignisse']],
           'laufzeit_s': time.time() - t0}
    tg.schreibe(a.out, res)
    print('fertig scan laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
