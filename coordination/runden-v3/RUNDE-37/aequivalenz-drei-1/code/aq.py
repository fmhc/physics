# -*- coding: utf-8 -*-
"""AEQUIVALENZ-DREI-1: aktive, passive und traege Masse eines Gitter-Q-Balls auf V mit netzgpu (unveraendert importiert).

Aufruf (nur ueber kleintest.sh auf der .69, Spur p4000a/p4000b):
  python aq.py <aus.json> om=<omega> h=<h> n=<zellen> [kb=0.03] [Tb=500] [Tf=200] [phimax=1e-3] [dtf=0.25] [maxiter=2500]

Ein Ball (Kontinuums-omega om, festes Q = Q_kont) um eine Lochmitte C1 in einer kubischen Superzelle n^3 von V.
Gemessen wird:
  aktiv : Quelle aus derselben Wirkung (-dH/dPhi bei festen phi, pi): Summe = E + gamma S (Homogenitaetsprobe per
          finiter Differenz mit uniformem Phi durch die Engine), Takt per Poisson (kopplung.takt_poisson) mit Quelle
          m_v + gamma s_v (Verteilung wie SCHWERE-MASSE-V), Fernfit -A/r + B r^2 + C + D (x^4+y^4+z^4 - 3/5 r^4),
          Kontrolle mit schmaler Gauss-Quelle derselben Masse.
  traege: Ball mit Phasendrall exp(-i k x) (k = kb in Q-Einheiten, Richtung x), freie Zeitentwicklung (N = 1);
          Energieschwerpunkt X_E, Ladungsschwerpunkt X_Q, Energiestrom-Impuls P_E = sum_e kvec_e J_e
          (J_e = -k_e Re[(phidot_a + phidot_b)^* (phi_b - phi_a)]); Gitter-Identitaet H dX_E/dt = P_E.
  passiv: ruhender Ball in einem Saegezahn-Takt Phi = g (z - z_c) (Sprung bei z_c +- n/2, weit weg vom Ball),
          gamma = 1 (Takt und Laengen) und gamma = 0 (nur Takt); Fallbeschleunigung des Energieschwerpunkts aus
          dem Bahnfit und aus der Anfangskraft dP_E/dt(0) / H; geteilt durch das Gefaelle g.
Einheiten: Q-Ball-Einheiten (m = 1); Netzlagen in a (kubische Kante), a_Q = h / LP = 2 sqrt(2) h Q-Laengen.
Synthetisch, keine Messdaten.
"""
import json
import math
import os
import sys
import time

import numpy as np
import torch

sys.path.insert(0, '/home/fmh/fmhc-physics-remote/netz-gpu/code')
from netzgpu import FASSUNG, kopplung, skalar  # noqa: E402
from netzgpu.datensatz import platte_frei_gb  # noqa: E402
from netzgpu.netz import Netz  # noqa: E402

T0 = time.time()


def log(*a):
    print('[%7.1f s]' % (time.time() - T0), *a, flush=True)


def schreibe(p, obj):
    obj['_meta'] = {'argv': sys.argv, 'torch': torch.__version__, 'gpu': torch.cuda.get_device_name(0),
                    'laufzeit_s': time.time() - T0, 'gpu_speicher_max_MB': torch.cuda.max_memory_allocated() / 1e6,
                    'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'fassung': FASSUNG}
    with open(p + '.tmp', 'w') as f:
        json.dump(obj, f, indent=1)
    os.replace(p + '.tmp', p)
    log('->', p)


def dk(N, z):
    return torch.complex(N.d0 @ z.real.contiguous(), N.d0 @ z.imag.contiguous())


def impuls_E(N, sk, phi, pi_):
    """Energiestrom-Impuls (a-Einheiten * Energie / Zeit); H dX_E/dt = P_E exakt auf dem Gitter."""
    phd = pi_ / sk.m
    J = -sk.k * (torch.conj(phd[sk.a] + phd[sk.b]) * dk(N, phi)).real
    return (N.kvec * J[:, None]).sum(0)


def impuls_E_punkt(N, sk, phi, pi_):
    """Zeitableitung von P_E aus den Bewegungsgleichungen (Anfangskraft)."""
    phd = pi_ / sk.m
    phdd = sk.kraft(phi) / sk.m
    J = -sk.k * ((torch.conj(phdd[sk.a] + phdd[sk.b]) * dk(N, phi)).real
                 + (torch.conj(phd[sk.a] + phd[sk.b]) * dk(N, phd)).real)
    return (N.kvec * J[:, None]).sum(0)


def zentrum(N, w, c):
    B = torch.tensor(N.box, dtype=N.dtype, device=N.device)
    d = N.x - c
    d = d - B * torch.round(d / B)
    return c + (w[:, None] * d).sum(0) / w.sum()


def wrap(d, L):
    return d - L * torch.round(d / L)


def lauf(N, sk, phi, pi_, T, dt, nrec, c0):
    """Zeitentwicklung mit Aufzeichnung von t, X_E, X_Q, P_E, H, Q."""
    nschritt = max(1, int(round(T / nrec / dt)))
    cE, cQ = c0.clone(), c0.clone()
    rec = []
    tk = []
    for b in range(nrec + 1):
        if b > 0:
            torch.cuda.synchronize()
            t1 = time.time()
            phi, pi_ = sk.schritt(phi, pi_, dt, nschritt)
            torch.cuda.synchronize()
            tk.append((time.time() - t1) / nschritt)
        e = sk.energie_ecke(phi, pi_)
        q = 2.0 * (torch.conj(phi) * pi_).imag
        cE = zentrum(N, e, cE)
        cQ = zentrum(N, q, cQ)
        P = impuls_E(N, sk, phi, pi_)
        rec.append([b * nschritt * dt] + cE.tolist() + cQ.tolist() + P.tolist() + [float(e.sum()), float(q.sum())])
    return np.array(rec), phi, pi_, {'schritte_je_aufz': nschritt, 'ms_je_schritt': 1e3 * float(np.median(tk))}


def polyfit(t, y, potenzen):
    """Kleinste Quadrate in s = t / t_max (Kondition), Koeffizienten zurueck in Potenzen von t."""
    tm = float(np.max(t))
    s = t / tm
    X = np.stack([s ** p for p in potenzen], 1)
    c, *_ = np.linalg.lstsq(X, y, rcond=None)
    rest = y - X @ c
    return c / tm ** np.array(potenzen, dtype=float), float(np.sqrt(np.mean(rest ** 2)))


def fernfit(N, phi, x0, r1, r2):
    d = N.ecken_minbild(x0)
    r = torch.linalg.norm(d, dim=1)
    sel = (r >= r1) & (r <= r2)
    rr = r[sel].cpu().numpy()
    dd = d[sel].cpu().numpy()
    y = phi[sel].cpu().numpy()
    c4 = (dd ** 4).sum(1) - 0.6 * rr ** 4
    X = np.stack([-1.0 / rr, rr ** 2, np.ones_like(rr), c4], 1)
    c, *_ = np.linalg.lstsq(X, y, rcond=None)
    rest = y - X @ c
    return {'A': float(c[0]), 'B': float(c[1]), 'C': float(c[2]), 'D': float(c[3]), 'n_ecken': int(sel.sum()),
            'rest_rms_rel': float(np.sqrt(np.mean(rest ** 2)) / np.max(np.abs(y)))}


def main(aus, om=0.85, h=0.8, n=16, kb=0.03, Tb=500.0, Tf=200.0, phimax=1e-3, dtf=0.25, maxiter=2500, nrec=100,
         gtol=1e-9):
    res = {'parameter': {'om': om, 'h': h, 'n': n, 'kb': kb, 'Tb': Tb, 'Tf': Tf, 'phimax': phimax, 'dtf': dtf,
                         'maxiter': maxiter, 'gtol': gtol}}
    frei = platte_frei_gb()
    log('Platte frei %.1f GB' % frei)
    if frei < 10.0:
        raise SystemExit('Platte unter 10 GB frei')
    N = Netz('V', (n, n, n))
    a_Q = h / skalar.LP
    log('Netz', N.N_e, N.N_k, N.N_d, N.N_t, 'a_Q = %.4f' % a_Q)
    x0 = torch.tensor([n / 2 - 0.25] * 3, dtype=N.dtype, device=N.device)          # Lochmitte C1
    sk0 = skalar.Skalar(N, h=h)
    st0 = sk0.st
    # ---------------------------------------------------------------- stationaerer Ball
    kont = skalar.qball_kont(om)
    r = sk0.abstand_Q(x0)
    f0 = torch.tensor(np.interp(r.cpu().numpy(), kont['r'], kont['f'], right=0.0), dtype=N.dtype, device=N.device)
    t1 = time.time()
    f, info = sk0.relaxieren(f0, kont['Q'], maxiter=maxiter, gtol=gtol)
    torch.cuda.synchronize()
    info['zeit_s'] = time.time() - t1
    omg = info['om']
    tl = sk0.teile(f, omg)
    E, Q, S = tl['E'], tl['Q'], tl['S']
    df = N.d0 @ f
    te = N.kvec / N.laengen()[:, None]
    Gdir = [float((sk0.s1 * df * df * te[:, i] ** 2).sum()) for i in range(3)]
    rmax = float(sk0.abstand_Q(x0).max())
    rand = float(tl['m'][sk0.abstand_Q(x0) > 0.8 * (n / 2) * a_Q].sum() / E)
    # Energieanteil in der Randschicht (Sprung des Saegezahns in z, Phasenschnitt in x): |d| > n/2 - 1 a
    dz = wrap(N.x[:, 2] - x0[2], float(n)).abs()
    dx = wrap(N.x[:, 0] - x0[0], float(n)).abs()
    schicht_z = float(tl['m'][dz > n / 2 - 1].sum() / E)
    schicht_x = float(tl['m'][dx > n / 2 - 1].sum() / E)
    ball = {'om_kont': om, 'om_gitter': omg, 'E': E, 'Q': Q, 'K': tl['K'], 'G': tl['G'], 'V': tl['V'], 'S': S,
            'S_rel': S / E, 'bindung': (Q - E) / E, 'E_kont': kont['E'], 'Q_kont': kont['Q'],
            'bindung_kont': kont['bind'], 'G_xyz': Gdir, 'omQ_plus_2Gx': omg * Q + 2 * Gdir[0],
            'energie_aussen_0.8_halbe_box': rand, 'energie_randschicht_z': schicht_z,
            'energie_randschicht_x': schicht_x, 'relax': info}
    res['ball'] = ball
    log('Ball', json.dumps({k: v for k, v in ball.items() if k != 'relax'}), 'iter', info['iter'], 'rest',
        info['resid_rel'], 'zeit', round(info['zeit_s'], 1))
    phi_c = f.to(torch.complex128)
    pi_c = sk0.m * (1j * omg) * phi_c

    # ---------------------------------------------------------------- aktiv
    akt = {}

    def H_uniform(eps, gam):
        Phi = torch.full((N.N_e,), eps, dtype=N.dtype, device=N.device)
        if gam:
            l, w = kopplung.metrik_aus_takt(N, Phi, gamma=gam)
        else:
            l, w = None, None
        sk = skalar.Skalar(N, h=h, N=1.0 + Phi, l=l, w=w)
        return sk.energie(phi_c, pi_c)
    eps = 1e-5
    for gam in (1.0, 0.0):
        dH = (H_uniform(eps, gam) - H_uniform(-eps, gam)) / (2 * eps)
        akt['dH_dPhi_gamma%g' % gam] = dH
        akt['dH_dPhi_durch_E_plus_gS_minus_1_gamma%g' % gam] = dH / (E + gam * S) - 1
    rr = sk0.abstand_Q(x0) / a_Q                                                    # in a
    for gam in (1.0, 0.0):
        src = tl['m'] + gam * tl['s']
        Msrc = float(src.sum())
        absw = src.abs()
        o = torch.argsort(rr, descending=True)
        kum = torch.cumsum(absw[o], 0) / absw.sum()
        r2 = 0.45 * n
        # kleinster Radius mit Quellanteil ausserhalb < 1e-5
        idx = int(torch.searchsorted(kum, torch.tensor(1e-5, dtype=kum.dtype, device=kum.device)))
        r1 = float(rr[o][max(idx - 1, 0)])
        knapp = r1 > r2 - 1.5
        r1 = min(max(r1, 2.5), r2 - 1.5)
        rest_ausserhalb = float(absw[rr > r1].sum() / absw.sum())
        ph, pinf = kopplung.takt_poisson(N, st0, src)
        fit = fernfit(N, ph, x0, r1, r2)
        mc, _ = kopplung.gauss_masse(N, x0, Msrc, 0.4)
        phc, _ = kopplung.takt_poisson(N, st0, mc)
        fitc = fernfit(N, phc, x0, r1, r2)
        akt['gamma%g' % gam] = {'quelle_summe': Msrc, 'quelle_durch_E': Msrc / E, 'band_a': [r1, r2],
                                'band_knapp': bool(knapp), 'quelle_betrag_ausserhalb_r1': rest_ausserhalb,
                                'fit': fit, 'kontrolle_fit': fitc, 'M_aktiv_fit': fit['A'],
                                'M_aktiv_fit_durch_quelle': fit['A'] / Msrc,
                                'kontrolle_A_durch_M': fitc['A'] / Msrc,
                                'M_aktiv_korrigiert': fit['A'] / (fitc['A'] / Msrc),
                                'M_aktiv_korr_durch_E': fit['A'] / (fitc['A'] / Msrc) / E, 'poisson': pinf}
        log('aktiv gamma', gam, json.dumps({k: v for k, v in akt['gamma%g' % gam].items()
                                            if k not in ('fit', 'kontrolle_fit', 'poisson')}))
    res['aktiv'] = akt
    del ph, phc, mc

    # ---------------------------------------------------------------- traege: Phasendrall in x, frei
    wmax = sk0.omega_max()
    dt0 = dtf * 2.0 / wmax
    nrb = nrec
    xr = wrap(N.x[:, 0] - x0[0], float(n)) * a_Q
    drall = torch.exp(-1j * kb * xr.to(torch.complex128))
    phi = phi_c * drall
    pi_ = pi_c * drall
    Htot = sk0.energie(phi, pi_)
    Qb = sk0.ladung(phi, pi_)
    P0 = impuls_E(N, sk0, phi, pi_)
    rec, phi_e, pi_e, tinfo = lauf(N, sk0, phi, pi_, Tb, dt0, nrb, x0.clone())
    t = rec[:, 0]
    XE, XQ, PE, HH = rec[:, 1:4] * a_Q, rec[:, 4:7] * a_Q, rec[:, 7:10] * a_Q, rec[:, 10]
    # lineare Fits ueber das ganze Fenster und die zweite Haelfte
    tr = {'E_tot': Htot, 'E_tot_durch_E_minus_1': Htot / E - 1, 'Q': Qb, 'kQ': kb * Qb, 'P_E0_Q': P0.tolist(),
          'P_E0_x_Q': float(P0[0]) * a_Q, 'kQ_durch_PE0_minus_1': kb * Qb / (float(P0[0]) * a_Q) - 1,
          'dt': dt0, 'omega_max': wmax, 'zeit': tinfo, 'H_rel_spanne': float((HH.max() - HH.min()) / Htot),
          'Q_rel_spanne': float((rec[:, 11].max() - rec[:, 11].min()) / Qb)}
    for name, sl in (('ganz', slice(0, None)), ('zweite_haelfte', slice(len(t) // 2, None))):
        cE, rE = polyfit(t[sl], XE[sl, 0], (0, 1))
        cQ, rQ = polyfit(t[sl], XQ[sl, 0], (0, 1))
        PEm = float(np.trapezoid(PE[sl, 0], t[sl]) / (t[sl][-1] - t[sl][0]))
        vE, vQ = float(cE[1]), float(cQ[1])
        tr[name] = {'v_E': vE, 'v_Q': vQ, 'rest_E': rE, 'rest_Q': rQ, 'P_E_mittel': PEm,
                    'M_traege_energiestrom': PEm / vE, 'M_traege_energiestrom_durch_Etot_minus_1': PEm / vE / Htot - 1,
                    'M_traege_phasenimpuls': kb * Qb / vE, 'M_traege_phasenimpuls_durch_Etot_minus_1': kb * Qb / vE / Htot - 1,
                    'M_traege_phasenimpuls_Q': kb * Qb / vQ, 'vQ_durch_vE_minus_1': vQ / vE - 1}
    tr['P_E_x_rel_spanne'] = float((PE[:, 0].max() - PE[:, 0].min()) / abs(PE[:, 0].mean()))
    tr['P_E_yz_max_durch_x'] = float(np.abs(PE[:, 1:]).max() / abs(PE[:, 0].mean()))
    tr['reihe_t_XE_XQ_PE_H'] = np.concatenate([t[:, None], XE[:, :1], XQ[:, :1], PE[:, :1], HH[:, None]], 1).tolist()
    res['traege'] = tr
    log('traege', json.dumps({k: v for k, v in tr.items() if k not in ('reihe_t_XE_XQ_PE_H',)}))
    del phi, pi_, phi_e, pi_e, drall

    # ---------------------------------------------------------------- passiv: Saegezahn-Takt in z
    pas = {}
    zr = wrap(N.x[:, 2] - x0[2], float(n))                       # a
    gPhi = phimax / (n / 2.0)                                     # je a
    gQ = gPhi / a_Q                                               # je Q-Laenge
    for gam in (1.0, 0.0):
        Phi = gPhi * zr
        Nl = 1.0 + Phi
        if gam:
            l, w = kopplung.metrik_aus_takt(N, Phi, gamma=gam)
        else:
            l, w = None, None
        sk = skalar.Skalar(N, h=h, N=Nl, l=l, w=w)
        st_min = {'min_s0': float(sk.st['s0'].min()), 'min_s1': float(sk.st['s1'].min())}
        phi = phi_c.clone()
        pi_ = sk.m * (1j * omg) * phi
        H0 = sk.energie(phi, pi_)
        Pd0 = impuls_E_punkt(N, sk, phi, pi_)                     # a * Energie / Zeit^2
        a0 = float(Pd0[2]) * a_Q / H0                             # Q-Einheiten
        wm = sk.omega_max()
        dtp = dtf * 2.0 / wm
        rec, _, _, tinfo = lauf(N, sk, phi, pi_, Tf, dtp, nrec, x0.clone())
        t = rec[:, 0]
        zE = rec[:, 3] * a_Q
        zQ = rec[:, 6] * a_Q
        PEz = rec[:, 9] * a_Q
        HH = rec[:, 10]
        out = {'g_Q': gQ, 'phimax': phimax, 'dt': dtp, 'omega_max': wm, 'zeit': tinfo, 'sterne': st_min,
               'H0': H0, 'H_rel_spanne': float((HH.max() - HH.min()) / H0),
               'a0_aus_dPdt0': a0, 'a0_durch_g': -a0 / gQ,
               'Pd0_xy_durch_z': float(torch.linalg.norm(Pd0[:2]) / abs(Pd0[2])),
               'fallweg_E_Q': float(zE[-1] - zE[0]), 'v_end_Q': float(PEz[-1] / HH[-1])}
        for name, sl in (('ganz', slice(0, None)), ('erste_haelfte', slice(0, len(t) // 2 + 1))):
            c2, r2_ = polyfit(t[sl], zE[sl] - zE[0], (0, 1, 2))
            c4, r4_ = polyfit(t[sl], zE[sl] - zE[0], (0, 1, 2, 4))
            q4, rq4 = polyfit(t[sl], zQ[sl] - zQ[0], (0, 1, 2, 4))
            p3, rp3 = polyfit(t[sl], PEz[sl] / HH[sl], (0, 1, 3))
            out[name] = {'a_E_quadr': 2 * c2[2], 'a_E_quadr_durch_g': -2 * c2[2] / gQ, 'rest_quadr': r2_,
                         'a_E_mit_t4': 2 * c4[2], 'a_E_mit_t4_durch_g': -2 * c4[2] / gQ, 'rest_t4': r4_,
                         'a_Q_mit_t4_durch_g': -2 * q4[2] / gQ, 'rest_Q_t4': rq4,
                         'a_aus_PE_durch_g': -p3[1] / gQ, 'rest_PE': rp3}
        out['reihe_t_zE_zQ_PEz_H'] = np.stack([t, zE, zQ, PEz, HH], 1).tolist()
        pas['gamma%g' % gam] = out
        log('passiv gamma', gam, json.dumps({k: v for k, v in out.items() if not k.startswith('reihe')}))
        del sk, phi, pi_
    res['passiv'] = pas

    # ---------------------------------------------------------------- Zusammenfassung (Q-Einheiten)
    MT = tr['zweite_haelfte']['M_traege_energiestrom']
    MTk = tr['zweite_haelfte']['M_traege_phasenimpuls']
    MA = akt['gamma1']['M_aktiv_korrigiert']
    zs = {'E': E, 'bindung': (Q - E) / E, 'S_rel': S / E, 'E_tot_boost': Htot,
          'M_aktiv_gamma1': MA, 'M_aktiv_quelle_gamma1': akt['gamma1']['quelle_summe'],
          'M_traege_energiestrom': MT, 'M_traege_phasenimpuls': MTk}
    for gam in ('gamma1', 'gamma0'):
        ag = pas[gam]['a0_durch_g']
        agf = pas[gam]['erste_haelfte']['a_E_mit_t4_durch_g']
        zs['a_durch_g_anfangskraft_' + gam] = ag
        zs['a_durch_g_bahnfit_' + gam] = agf
    # traege Masse auf den ruhenden Ball bezogen: M_traege(v) / E_tot(v) * E
    zs['M_traege_E_bezogen'] = MT / Htot * E
    zs['M_traege_phasenimpuls_E_bezogen'] = MTk / Htot * E
    zs['M_passiv_gamma1'] = zs['M_traege_E_bezogen'] * zs['a_durch_g_anfangskraft_gamma1']
    zs['M_passiv_durch_M_traege_gamma1'] = zs['a_durch_g_anfangskraft_gamma1']
    zs['M_aktiv_durch_M_traege'] = MA / zs['M_traege_E_bezogen']
    zs['M_aktiv_durch_M_passiv_gamma1'] = MA / zs['M_passiv_gamma1']
    zs['M_aktiv_durch_M_traege_phasenimpuls'] = MA / zs['M_traege_phasenimpuls_E_bezogen']
    res['zusammenfassung'] = zs
    log('zusammenfassung', json.dumps(zs))
    schreibe(aus, res)


if __name__ == '__main__':
    kw = {}
    for arg in sys.argv[2:]:
        k_, v_ = arg.split('=')
        kw[k_] = int(v_) if k_ in ('n', 'maxiter', 'nrec') else float(v_)
    main(sys.argv[1], **kw)
