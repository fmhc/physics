#!/usr/bin/env python3
"""LICHT-1 (Runde 34, runden-v3, explorativ). Code-Agent fuer die Leitung claude-primary.

Wie schnell wird ein Q-Ball (M1, beta = 1/2, Q = 200), der in die Mulde einer Kegelspitze faellt?
  Teil A (radial): exakte Abbildung B(s) = E_flach(Q) - E_flach(sQ)/s, gamma = 1 + B/E, v_Grund = sqrt(1 - 1/gamma^2).
  Teil B (Netz):   Zeitentwicklung an einer Dreier-Spitze (n = 3, s = 2) mit dem Integrator aus EINFANG-1; dazu
                   B(s) und das statische Potential V(d) auf demselben Netz.
Netz, Radialloeser, statischer Ball: kegel_q.py (unveraenderte Kopie aus RUNDE-26). Zeitentwicklung, Boost, Schwamm,
Bilanz und harmonischer Schwerpunkt: wie einfang.py (RUNDE-34/einfang-1), hier erweitert um
  - n = 3 und 4,
  - axiale Diagnose auf der Spiegelachse (Startstrahl + Gegenstrahl): axialer Ladungsschwerpunkt xi_c und
    Feldmaximum xi_m (Parabel durch die drei hoechsten Achsenpunkte), xi < 0 vor, xi > 0 hinter der Spitze,
  - Ladungsfluss J je Ecke (kleinste Quadrate aus den Kantenfluessen 2 Im(conj phi_i phi_j)), daraus die mittlere und
    die rms-Fliessgeschwindigkeit der Ladung im Ball (v_mean = Sum A|J| / Sum A rho, v_rms^2 = Sum A |J|^2/rho / Sum A rho),
  - Stoppregel nach dem zweiten Durchgang (Vorzeichenwechsel von xi_c).
Befehle: radial, statik, lauf, auswertung, bild.
"""
import argparse
import glob
import json
import math
import os
import sys
import time

for _v in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ.setdefault(_v, '1')

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kegel_q import Radial, Netz, loese_Q, loese_ball, baue_familie, OMC2, SIGMA_TW  # noqa: E402

PI = math.pi
T_START = time.perf_counter()
R_C = 6.2551 + 3.0      # R_half(Q = 200) + 3 wie EINFANG-1
X_FENSTER = 12.0        # Fenster fuer v_ein wie EINFANG-1


def jetzt():
    return time.strftime('%Y-%m-%dT%H:%M:%S%z')


def schreibe_json(pfad, obj):
    tmp = pfad + '.tmp'
    with open(tmp, 'w') as fh:
        json.dump(obj, fh, indent=1)
    os.replace(tmp, pfad)


def lade(p):
    with open(p) as fh:
        return json.load(fh)


def v_aus_gamma(g):
    return math.sqrt(max(0.0, 1.0 - 1.0 / (g * g)))


# --------------------------------------------------------------------------------------------------------------------
# Teil A: radiale Familie bis nahe omega_c
# --------------------------------------------------------------------------------------------------------------------
def familie_weit(dr, rmax, eps_min, q=0.96):
    """Wie kegel_q.radial_familie, abwaerts aber geometrisch in eps = omega^2 - 1/2 (bis eps_min), damit grosse Q
    erreicht werden. Je Schritt drei Startwerte: Extrapolation, Vorgaenger, frische Duennwand mit skaliertem Radius."""
    rad = Radial(dr, rmax)
    om2_start = 0.62
    ab = []
    e = om2_start - OMC2
    while True:
        e *= q
        if e < eps_min:
            break
        ab.append(OMC2 + e)
    auf = [round(0.62 + 0.005 * k, 6) for k in range(1, 57)]
    R0 = SIGMA_TW / (om2_start - OMC2)
    S = 1.0 / (1.0 + np.exp(np.clip(math.sqrt(2.0) * (rad.r - R0), -700.0, 700.0)))
    f0, it0, nr0 = rad.newton(np.sqrt(S), om2_start)
    erg = {om2_start: (f0, it0, nr0, 'start')}
    for folge in (ab, auf):
        f_prev, o_prev, f_pp, o_pp = f0, om2_start, None, None
        for om2 in folge:
            kand = []
            if f_pp is not None:
                kand.append(('extrapol', f_prev + (om2 - o_prev) / (o_prev - o_pp) * (f_prev - f_pp)))
            kand.append(('vorgaenger', f_prev))
            best = None
            for k in range(3):
                if k < len(kand):
                    name, g = kand[k]
                elif k == 2 or len(kand) == 1:
                    gp = rad.groessen(f_prev, o_prev)
                    Rn = gp['R_half'] * (o_prev - OMC2) / (om2 - OMC2)
                    Sg = gp['S0'] / (1.0 + np.exp(np.clip(math.sqrt(2.0) * (rad.r - Rn), -700.0, 700.0)))
                    name, g = 'duennwand', np.sqrt(Sg)
                else:
                    continue
                f, it, nr = rad.newton(g, om2)
                if np.max(f) >= 0.05 and (best is None or nr < best[2]):
                    best = (f, it, nr, name)
                if best is not None and best[2] < 1e-9:
                    break
            if best is None:
                break
            erg[om2] = best
            f_pp, o_pp, f_prev, o_prev = f_prev, o_prev, best[0], om2
    fam = []
    for om2 in sorted(erg):
        f, it, nr, wie = erg[om2]
        g = rad.groessen(f, om2)
        g['newton_it'] = it
        g['res'] = nr
        g['start'] = wie
        fam.append((g, f))
    return rad, fam


def befehl_radial(args):
    s_liste = [float(x) for x in args.s.split(',')]
    s_dEdQ = [float(x) for x in args.s_dEdQ.split(',')] if args.s_dEdQ else []
    aus = dict(befehl='radial', start=jetzt(), dr=args.dr, rmax=args.rmax, eps_min=args.eps_min, Q=args.Q,
               s_liste=s_liste)
    tf = time.perf_counter()
    rad, fam = familie_weit(args.dr, args.rmax, args.eps_min, args.q)   # NACHTRAG: Schrittfaktor q waehlbar
    aus['q'] = args.q
    tab = [g for g, f in fam]
    aus['familie'] = [{k: g[k] for k in ('om2', 'omega', 'Q', 'E', 'R_half', 'S0', 'kappa', 'res', 'newton_it', 'start')}
                      for g in tab]
    aus['familie_max_res'] = float(max(g['res'] for g in tab))
    aus['familie_Q_max'] = float(max(g['Q'] for g in tab))
    aus['familie_dauer_s'] = time.perf_counter() - tf
    print('Familie: %d Punkte, max res %.2e, Q_max %.1f (om2 %.5f), %.1f s' % (
        len(tab), aus['familie_max_res'], aus['familie_Q_max'], tab[0]['om2'], aus['familie_dauer_s']), flush=True)
    g0, f0 = loese_Q(rad, fam, args.Q)
    E0 = g0['E']
    aus['flach_Q'] = dict(E=E0, omega=g0['omega'], R_half=g0['R_half'], kappa=g0['kappa'], S0=g0['S0'], res=g0['res'],
                          dQdom2=g0['dQdom2_fam'])
    B_inf = E0 - math.sqrt(OMC2) * args.Q
    aus['grenzwert_s_unendlich'] = dict(B=B_inf, gamma=1 + B_inf / E0, v=v_aus_gamma(1 + B_inf / E0),
                                        gamma_alt=E0 / (E0 - B_inf), v_alt=v_aus_gamma(E0 / (E0 - B_inf)))
    zeilen = []
    for s in s_liste:
        Qs = s * args.Q
        t = time.perf_counter()
        try:
            g, f = loese_Q(rad, fam, Qs)
        except Exception as ex:  # Loeser traegt nicht
            zeilen.append(dict(s=s, Q_strich=Qs, fehler=str(ex)))
            print('s %g: %s' % (s, ex), flush=True)
            continue
        B = E0 - g['E'] / s
        gam = 1.0 + B / E0
        gam_alt = E0 / (E0 - B)
        z = dict(s=s, n_aequiv=6.0 / s, Q_strich=Qs, omega=g['omega'], om2=g['om2'], E_flach_sQ=g['E'],
                 E_kegel=g['E'] / s, B=B, gamma=gam, v_grund=v_aus_gamma(gam), gamma_alt=gam_alt,
                 v_alt=v_aus_gamma(gam_alt), R_half=g['R_half'], kappa=g['kappa'], S0=g['S0'], res=g['res'],
                 dQdom2=g['dQdom2_fam'], stabiler_ast=bool(g['dQdom2_fam'] < 0), E_durch_Q=g['E'] / Qs,
                 f2_letzte_5=float(np.max(f[rad.r > args.rmax - 5.0] ** 2)),
                 rmax_minus_R_half=args.rmax - g['R_half'],
                 B_duennwand_karte=15.87 * (1.0 - 1.0 / math.sqrt(s)))
        if s in s_dEdQ:
            dq = 1e-3 * Qs
            gp, _ = loese_Q(rad, fam, Qs + dq)
            gm, _ = loese_Q(rad, fam, Qs - dq)
            z['dEdQ_num'] = (gp['E'] - gm['E']) / (2 * dq)
            z['dEdQ_rel_abw'] = z['dEdQ_num'] / g['omega'] - 1.0
        z['dauer_s'] = time.perf_counter() - t
        zeilen.append(z)
        print('s %5.2f Q %8.1f om %.6f R_half %7.3f E %.8f B %.6f gamma %.6f v %.4f dQdom2 %.3e f2rand %.1e %s (%.1f s)' % (
            s, Qs, g['omega'], g['R_half'], g['E'], B, gam, z['v_grund'], g['dQdom2_fam'], z['f2_letzte_5'],
            ('dEdQ %.1e' % z['dEdQ_rel_abw']) if 'dEdQ_rel_abw' in z else '', z['dauer_s']), flush=True)
        aus['zeilen'] = zeilen
        schreibe_json(args.aus, aus)
    aus['zeilen'] = zeilen
    aus['ende'] = jetzt()
    aus['dauer_s'] = time.perf_counter() - T_START
    schreibe_json(args.aus, aus)
    print('geschrieben', args.aus, 'Dauer %.1f s' % aus['dauer_s'], flush=True)


# --------------------------------------------------------------------------------------------------------------------
# Teil B, statisch: B(s) und V(d) auf dem Netz
# --------------------------------------------------------------------------------------------------------------------
def befehl_statik(args):
    net = Netz(args.n, args.h, args.R)
    net.setze_richtung(0.0)
    pr = net.pruefung()
    s = net.s
    rad, fam = baue_familie(0.01, 60.0)
    gQ, fQ = loese_Q(rad, fam, args.Q)
    gsQ, fsQ = loese_Q(rad, fam, s * args.Q)
    B_exakt = gQ['E'] - gsQ['E'] / s
    aus = dict(befehl='statik', start=jetzt(), n=args.n, h=args.h, R=args.R, Q=args.Q, s=s, netz=pr,
               radial=dict(E_Q=gQ['E'], omega_Q=gQ['omega'], R_half_Q=gQ['R_half'], E_sQ=gsQ['E'],
                           omega_sQ=gsQ['omega'], R_half_sQ=gsQ['R_half'], E_kegel_exakt=gsQ['E'] / s),
               B_exakt=B_exakt, punkte=[])
    print('Netz n=%d h=%g R=%g: %d Ecken, %d frei, Euler %d, Grad Spitze %d, Defekt %.6f (Soll %.6f), innen %s' % (
        args.n, args.h, args.R, pr['ecken'], pr['freie_ecken'], pr['euler'], pr['grad_spitze'], pr['defekt_spitze'],
        pr['defekt_soll'], pr['innen_grade']), flush=True)
    for d in [float(x) for x in args.d.split(',')]:
        t = time.perf_counter()
        D1 = d ** s
        dist = net.abstand(d=d)
        prof = fsQ if d == 0.0 else fQ
        f0 = np.interp(dist, rad.r, prof, right=0.0)
        f0[net.rand] = 0.0
        r, f = loese_ball(net, args.Q, D1, 0.0, f0, 5.0, 1e-9, 12, 40000, 1e-10)
        S = f * f
        Nn = float(net.A @ S)
        W = complex(float(net.A @ (S * net.u)) / Nn, float(net.A @ (S * net.v)) / Nn)
        p = dict(d=d, D1=D1, E=r['E'], E_korr=r['E'] + r['m1'] * r['c1'] + r['m2'] * r['c2'], omega=r['omega'],
                 c1=r['c1'], c2=r['c2'], m1=r['m1'], res_max=r['res_max'], aussen=r['aussen'], nit=r['nit'],
                 W_re=W.real, W_im=W.imag, d_W=abs(W) ** (1.0 / s), S_spitze=float(S[net.apex]), f_max=float(f.max()),
                 f_rand_max=float(np.max(f[np.abs(net.r - net.R) < 2 * net.h + 1e-9])),
                 dauer_s=time.perf_counter() - t)
        aus['punkte'].append(p)
        schreibe_json(args.aus, aus)
        print('d %5.2f: E %.10f E_korr %.10f omega %.6f c %.1e m1 %.3e res %.1e aussen %d d_W %.6f S_sp %.4f (%.1f s)' % (
            d, r['E'], p['E_korr'], r['omega'], r['c1'], r['m1'], r['res_max'], r['aussen'], p['d_W'], p['S_spitze'],
            p['dauer_s']), flush=True)
    pts = sorted(aus['punkte'], key=lambda q: q['d'])
    if pts and pts[0]['d'] == 0.0 and len(pts) > 1:
        aus['E_spitze'] = pts[0]['E_korr']
        aus['E_fern'] = pts[-1]['E_korr']
        aus['d_fern'] = pts[-1]['d']
        aus['B_gitter'] = aus['E_fern'] - aus['E_spitze']
        aus['B_rel_abw'] = (aus['B_gitter'] - B_exakt) / abs(B_exakt)
        aus['E_fern_gegen_radial_rel'] = aus['E_fern'] / gQ['E'] - 1.0
        print('B_gitter %.6f B_exakt %.6f rel %.2e E_fern %.8f' % (aus['B_gitter'], B_exakt, aus['B_rel_abw'],
                                                                   aus['E_fern']), flush=True)
    aus['ende'] = jetzt()
    aus['dauer_s'] = time.perf_counter() - T_START
    schreibe_json(args.aus, aus)
    print('geschrieben', args.aus, 'Dauer %.1f s' % aus['dauer_s'], flush=True)


# --------------------------------------------------------------------------------------------------------------------
# Teil B, Zeitentwicklung (Integrator, Boost, Schwamm, Bilanz wie einfang.py)
# --------------------------------------------------------------------------------------------------------------------
def achse(net):
    """Ecken auf der Spiegelachse: Startstrahl phi = 0 (xi = -r) und Gegenstrahl |phi| = Theta/2 (xi = +r)."""
    frei = ~net.rand
    nah = np.where(frei & (np.abs(net.phi) < 1e-7))[0]
    fern = np.where(frei & (np.abs(np.abs(net.phi) - net.Theta / 2.0) < 1e-7) & (net.r > 1e-12))[0]
    g = np.concatenate([nah, fern])
    xi = np.concatenate([-net.r[nah], net.r[fern]])
    o = np.argsort(xi)
    g, xi = g[o], xi[o]
    w = np.empty_like(xi)
    w[1:-1] = (xi[2:] - xi[:-2]) / 2.0
    w[0] = (xi[1] - xi[0]) / 2.0
    w[-1] = (xi[-1] - xi[-2]) / 2.0
    return g, xi, w


def kanten_lokal(net):
    """Gerichtete Kanten zwischen freien Ecken mit dem Kantenvektor in der lokalen Abwicklung der Ausgangsecke."""
    ki, kj = net.kanten_i, net.kanten_j
    m = ~net.rand[ki] & ~net.rand[kj]
    ki, kj = ki[m], kj[m]
    T = net.Theta

    def vek(a, b):
        dphi = net.phi[b] - net.phi[a]
        dphi = dphi - T * np.round(dphi / T)
        za = net.r[a] * np.exp(1j * net.phi[a])
        zb = net.r[b] * np.exp(1j * (net.phi[a] + dphi))
        return zb - za
    src = np.concatenate([ki, kj])
    dst = np.concatenate([kj, ki])
    e = np.concatenate([vek(ki, kj), vek(kj, ki)])
    return src, dst, e.real, e.imag


def befehl_lauf(args):
    import torch
    if args.geraet == 'cuda':
        if not torch.cuda.is_available():
            raise RuntimeError('CUDA verlangt, aber nicht verfuegbar (kein CPU-Ausweichen)')
        dev = torch.device('cuda')
        geraet_name = torch.cuda.get_device_name(0)
    else:
        torch.set_num_threads(1)
        dev = torch.device('cpu')
        geraet_name = 'cpu'
    print('torch %s, Geraet %s (%s)' % (torch.__version__, dev, geraet_name), flush=True)
    dt, n, h, R = args.dt, args.n, args.h, args.R
    net = Netz(n, h, R)
    net.setze_richtung(0.0)
    pr = net.pruefung()
    fr = net.frei
    Nf = len(fr)
    s = net.s
    Theta = net.Theta
    print('Netz n=%d h=%g R=%g: %d Ecken, %d frei, Grad Spitze %d, Defekt %.6f, innen %s, Bauzeit bis jetzt %.1f s' % (
        n, h, R, pr['ecken'], pr['freie_ecken'], pr['grad_spitze'], pr['defekt_spitze'], pr['innen_grade'],
        time.perf_counter() - T_START), flush=True)
    ax_g, ax_xi, ax_w = achse(net)
    ax_f = np.searchsorted(fr, ax_g)
    assert np.all(fr[ax_f] == ax_g)
    print('Achse: %d Ecken, xi von %.3f bis %.3f, Abstaende nah %.4f fern %.4f' % (
        len(ax_g), ax_xi[0], ax_xi[-1], ax_xi[1] - ax_xi[0], ax_xi[-1] - ax_xi[-2]), flush=True)
    src_g, dst_g, ex, ey = kanten_lokal(net)
    src_f = np.searchsorted(fr, src_g)
    dst_f = np.searchsorted(fr, dst_g)
    Mxx = np.bincount(src_f, weights=ex * ex, minlength=Nf)
    Mxy = np.bincount(src_f, weights=ex * ey, minlength=Nf)
    Myy = np.bincount(src_f, weights=ey * ey, minlength=Nf)
    det = Mxx * Myy - Mxy * Mxy
    ok = det > 1e-12 * np.maximum(Mxx * Myy, 1e-300)
    apex_f = int(np.searchsorted(fr, net.apex))
    assert fr[apex_f] == net.apex
    ok[apex_f] = False                     # an der Spitze hat ein Vektor keine Richtung (Holonomie)
    det_s = np.where(ok, det, 1.0)
    Ixx = np.where(ok, Myy / det_s, 0.0)
    Ixy = np.where(ok, -Mxy / det_s, 0.0)
    Iyy = np.where(ok, Mxx / det_s, 0.0)

    if args.fortsetzen:
        z = np.load(args.fortsetzen)
        meta = json.loads(str(z['meta']))
        rec = json.loads(str(z['rec']))
        phi_np, p_np = z['phi'], z['p']
        t_now = float(z['t'])
        E_damp0, Q_damp0 = float(z['E_damp']), float(z['Q_damp'])
        meta['fortsetzungen'] = meta.get('fortsetzungen', []) + [dict(datei=args.fortsetzen, t=t_now, start=jetzt())]
        print('fortgesetzt bei t = %.3f aus %s' % (t_now, args.fortsetzen), flush=True)
    else:
        v = args.v
        gam = 1.0 / math.sqrt(1.0 - v * v)
        rad, fam = baue_familie(0.01, 60.0)
        g200, _ = loese_Q(rad, fam, args.Q)
        Q_lat = args.Q / gam
        if args.d0 == 0.0:
            if v != 0.0:
                raise RuntimeError('Start auf der Spitze nur ruhend')
            gQ, fQ = loese_Q(rad, fam, s * Q_lat)     # Kegelball = ebener Ball mit Ladung s Q
            D1 = 0.0
        else:
            gQ, fQ = loese_Q(rad, fam, Q_lat)
            D1 = args.d0 ** s
        dist = net.abstand(d=args.d0)
        f0 = np.interp(dist, rad.r, fQ, right=0.0)
        f0[net.rand] = 0.0
        tb = time.perf_counter()
        rb, f = loese_ball(net, Q_lat, D1, 0.0, f0, 5.0, 1e-9, 12, 40000, 1e-10)
        tb = time.perf_counter() - tb
        om = rb['omega']
        print('statischer Ball: Q_lat %.6f E %.8f omega %.6f c %.1e %.1e res %.1e aussen %d (%.1f s)' % (
            Q_lat, rb['E'], om, rb['c1'], rb['c2'], rb['res_max'], rb['aussen'], tb), flush=True)
        xi = net.X - args.d0
        dfr = np.gradient(fQ, rad.r)
        dfd = np.interp(dist, rad.r, dfr, right=0.0)
        dXf = np.where(dist > 1e-12, dfd * xi / np.maximum(dist, 1e-12), 0.0)
        phase = np.exp(-1j * om * gam * v * xi)
        phi_c = f * phase
        p_c = (v * dXf - 1j * om * gam * f) * phase
        phi_c[net.rand] = 0.0
        p_c[net.rand] = 0.0
        phi_np = np.stack([phi_c.real, phi_c.imag], 1)[fr].copy()
        p_np = np.stack([p_c.real, p_c.imag], 1)[fr].copy()
        t_now = 0.0
        E_damp0 = Q_damp0 = 0.0
        E_rest = rb['E'] + om * (args.Q - Q_lat)
        meta = dict(befehl='lauf', name=args.name, start=jetzt(), n=n, h=h, R=R, s=s, rs=args.rs, gmax=args.gmax,
                    Q=args.Q, v=v, gamma=gam, d0=args.d0, dt=dt, T=args.T, diag=args.diag, S_thr=args.S_thr,
                    R_ball=args.R_ball, stopp_x=args.stopp_x, kreuz_stopp=args.kreuz_stopp, T_nach=args.T_nach,
                    geraet=geraet_name, netz=pr, achse=dict(ecken=int(len(ax_g)), xi_min=float(ax_xi[0]),
                                                           xi_max=float(ax_xi[-1])),
                    radial_Q=dict(omega=g200['omega'], R_half=g200['R_half'], kappa=g200['kappa'], E=g200['E']),
                    ball=dict(Q_lat=Q_lat, E_lat=rb['E'], omega_lat=om, c1=rb['c1'], c2=rb['c2'],
                              res_max=rb['res_max'], aussen=rb['aussen'], dauer_s=tb, f_max=float(f.max()),
                              S_spitze=float(f[net.apex] ** 2)),
                    E_rest=E_rest, K_nominal=(gam - 1.0) * E_rest, R_c=R_C)
        rec = {k: [] for k in ('t', 'x', 'W_re', 'W_im', 'x_S', 'xi_c', 'xi_S', 'xi_m', 'S_ax_max', 'v_mean', 'v_rms',
                               'E_tot', 'Q_tot', 'E_damp', 'Q_damp', 'E_ball', 'Q_ball', 'S_max', 'S_spitze', 'Q_thr')}

    f64 = torch.float64
    A = torch.tensor(net.A[fr], dtype=f64, device=dev)
    invA = 1.0 / A
    Lff = net.Lff.tocsr()
    Lt = torch.sparse_csr_tensor(torch.tensor(Lff.indptr, dtype=torch.int64), torch.tensor(Lff.indices, dtype=torch.int64),
                                 torch.tensor(Lff.data, dtype=f64), size=Lff.shape).to(dev)
    r_np = net.r[fr]
    ang = torch.tensor(net.phi[fr], dtype=f64, device=dev)
    rr = torch.tensor(r_np, dtype=f64, device=dev)
    wu = torch.tensor(net.u[fr], dtype=f64, device=dev)
    wv = torch.tensor(net.v[fr], dtype=f64, device=dev)
    gs = np.where(r_np > args.rs, args.gmax * ((r_np - args.rs) / (R - args.rs)) ** 2, 0.0)
    idx_np = np.where(gs > 0)[0]
    idx = torch.tensor(idx_np, dtype=torch.int64, device=dev)
    c_half = torch.tensor(np.exp(-gs[idx_np] * dt / 2.0), dtype=f64, device=dev)
    A_s = A[idx]
    axf = torch.tensor(ax_f, dtype=torch.int64, device=dev)
    axw = torch.tensor(ax_w, dtype=f64, device=dev)
    axxi = torch.tensor(ax_xi, dtype=f64, device=dev)
    srcT = torch.tensor(src_f, dtype=torch.int64, device=dev)
    dstT = torch.tensor(dst_f, dtype=torch.int64, device=dev)
    exT = torch.tensor(ex, dtype=f64, device=dev)
    eyT = torch.tensor(ey, dtype=f64, device=dev)
    IxxT = torch.tensor(Ixx, dtype=f64, device=dev)
    IxyT = torch.tensor(Ixy, dtype=f64, device=dev)
    IyyT = torch.tensor(Iyy, dtype=f64, device=dev)
    okT = torch.tensor(ok, dtype=torch.bool, device=dev)
    phi = torch.tensor(phi_np, dtype=f64, device=dev)
    p = torch.tensor(p_np, dtype=f64, device=dev)
    E_damp = torch.tensor(E_damp0, dtype=f64, device=dev)
    Q_damp = torch.tensor(Q_damp0, dtype=f64, device=dev)

    def kraft(ph):
        S = (ph * ph).sum(1)
        dU = 1.0 - 2.0 * S + 1.5 * S * S
        return -(Lt @ ph) * invA[:, None] - dU[:, None] * ph

    def daempfe(ph, pp, Ed, Qd):
        ps = pp[idx]
        c = c_half[:, None]
        Ed = Ed + (A_s * (1.0 - c_half * c_half) * (ps * ps).sum(1)).sum()
        qs = 2.0 * A_s * (ps[:, 0] * ph[idx, 1] - ps[:, 1] * ph[idx, 0])
        Qd = Qd + ((1.0 - c_half) * qs).sum()
        pp[idx] = ps * c
        return Ed, Qd

    def diagnose(ph, pp, t, Ed, Qd):
        S = (ph * ph).sum(1)
        q = 2.0 * A * (pp[:, 0] * ph[:, 1] - pp[:, 1] * ph[:, 0])
        Lph = Lt @ ph
        e = A * (pp * pp).sum(1) + (ph * Lph).sum(1) + A * (S - S * S + 0.5 * S ** 3)
        thr = S > args.S_thr
        wq = torch.where(thr, q, torch.zeros_like(q))
        sq = wq.sum()
        wS = A * S
        sS = wS.sum()
        # Ladungsfluss je Ecke
        c = 2.0 * (ph[srcT, 0] * ph[dstT, 1] - ph[srcT, 1] * ph[dstT, 0])
        bx = torch.zeros(Nf, dtype=f64, device=dev).index_add_(0, srcT, exT * c)
        by = torch.zeros(Nf, dtype=f64, device=dev).index_add_(0, srcT, eyT * c)
        Jx = IxxT * bx + IxyT * by
        Jy = IxyT * bx + IyyT * by
        J2 = Jx * Jx + Jy * Jy
        rho = q * invA
        mJ = thr & okT & (rho > 0)
        Am = torch.where(mJ, A, torch.zeros_like(A))
        rho_s = torch.where(mJ, rho, torch.ones_like(rho))
        n_rho = (Am * rho).sum()
        v_mean = (Am * torch.sqrt(J2)).sum() / n_rho
        v_rms = torch.sqrt((Am * J2 / rho_s).sum() / n_rho)
        # Achse
        S_ax = S[axf]
        rho_ax = rho[axf]
        wa = torch.where(S_ax > args.S_thr, axw * rho_ax, torch.zeros_like(rho_ax))
        xi_c = (wa * axxi).sum() / wa.sum()
        wS_ax = axw * S_ax
        xi_S = (wS_ax * axxi).sum() / wS_ax.sum()
        vals = torch.stack([e.sum(), q.sum(), sq, (wq * wu).sum() / sq, (wq * wv).sum() / sq,
                            (wS * wu).sum() / sS, (wS * wv).sum() / sS, S.max(), S[apex_f], Ed, Qd, xi_c, xi_S,
                            v_mean, v_rms]).cpu().numpy()
        Et, Qt, Qthr, Wr, Wi, WSr, WSi, Smax, Sap, Edv, Qdv, xic, xiS, vme, vrm = [float(a) for a in vals]
        Sa = S_ax.cpu().numpy()
        k = int(np.argmax(Sa))
        xi_m = float(ax_xi[k])
        if 0 < k < len(Sa) - 1:
            x0, x1, x2 = ax_xi[k - 1], ax_xi[k], ax_xi[k + 1]
            y0, y1, y2 = Sa[k - 1], Sa[k], Sa[k + 1]
            den = (x0 - x1) * (x0 - x2) * (x1 - x2)
            a2 = (x2 * (y1 - y0) + x1 * (y0 - y2) + x0 * (y2 - y1)) / den
            b2 = (x2 * x2 * (y0 - y1) + x1 * x1 * (y2 - y0) + x0 * x0 * (y1 - y2)) / den
            if a2 < 0:
                xi_m = float(min(max(-b2 / (2 * a2), x0), x2))

        def koord(a, b):
            m = math.hypot(a, b)
            return 0.0 if m == 0.0 else -a * m ** (1.0 / s - 1.0)
        x = koord(Wr, Wi)
        xS = koord(WSr, WSi)
        d = abs(x)
        beta = 0.0 if x <= 0 else Theta / 2.0
        D = torch.remainder((ang - beta).abs(), Theta)
        D = torch.minimum(D, Theta - D)
        dist = torch.where(D < PI, torch.sqrt(torch.clamp(rr * rr + d * d - 2.0 * rr * d * torch.cos(D), min=0.0)),
                           rr + d)
        mb = dist < args.R_ball
        bv = torch.stack([e[mb].sum(), q[mb].sum()]).cpu().numpy()
        for kk, val in (('t', t), ('x', x), ('W_re', Wr), ('W_im', Wi), ('x_S', xS), ('xi_c', xic), ('xi_S', xiS),
                        ('xi_m', xi_m), ('S_ax_max', float(Sa[k])), ('v_mean', vme), ('v_rms', vrm),
                        ('E_tot', Et), ('Q_tot', Qt), ('E_damp', Edv), ('Q_damp', Qdv), ('E_ball', float(bv[0])),
                        ('Q_ball', float(bv[1])), ('S_max', Smax), ('S_spitze', Sap), ('Q_thr', Qthr)):
            rec[kk].append(val)
        return xic

    nd = int(round(args.diag / dt))
    n_steps = int(round((args.T - t_now) / dt))
    step0 = int(round(t_now / dt))
    if not args.fortsetzen:
        xc = diagnose(phi, p, 0.0, E_damp, Q_damp)
        meta['E0'] = rec['E_tot'][0]
        meta['Q0'] = rec['Q_tot'][0]
        meta['K_eff'] = rec['E_tot'][0] - meta['E_rest']
        print('Start: E %.8f Q %.8f E_rest %.8f K_eff %.6f K_nominal %.6f x %.4f xi_c %.4f xi_m %.4f v_rms %.5f Q_ball %.6f'
              % (meta['E0'], meta['Q0'], meta['E_rest'], meta['K_eff'], meta['K_nominal'], rec['x'][0], xc,
                 rec['xi_m'][0], rec['v_rms'][0], rec['Q_ball'][0]), flush=True)
    # Zustand der Stoppregel aus den bisherigen Aufzeichnungen
    xs = rec['xi_c']
    eingetreten = False
    kreuz = []
    for kk in range(len(xs)):
        if not eingetreten and xs[kk] > -R_C:
            eingetreten = True
        elif eingetreten and kk > 0 and xs[kk - 1] != 0 and np.sign(xs[kk]) != np.sign(xs[kk - 1]):
            kreuz.append(rec['t'][kk])
    t_stopp = (kreuz[args.kreuz_stopp - 1] + args.T_nach) if (args.kreuz_stopp > 0 and len(kreuz) >= args.kreuz_stopp) \
        else None
    F = kraft(phi)
    tl = time.perf_counter()
    grund = 'T erreicht'
    fertig = True
    k = 0
    for k in range(1, n_steps + 1):
        E_damp, Q_damp = daempfe(phi, p, E_damp, Q_damp)
        p.add_(F, alpha=0.5 * dt)
        phi.add_(p, alpha=dt)
        F = kraft(phi)
        p.add_(F, alpha=0.5 * dt)
        E_damp, Q_damp = daempfe(phi, p, E_damp, Q_damp)
        if k % nd == 0:
            t = (step0 + k) * dt
            xc = diagnose(phi, p, t, E_damp, Q_damp)
            if not math.isfinite(xc) or not math.isfinite(rec['E_tot'][-1]):
                grund = 'nicht endlich'
                break
            prev = rec['xi_c'][-2] if len(rec['xi_c']) > 1 else xc
            if not eingetreten and xc > -R_C:
                eingetreten = True
            elif eingetreten and prev != 0 and np.sign(xc) != np.sign(prev):
                kreuz.append(t)
                print('Durchgang %d bei t %.2f (xi_c %.4f -> %.4f)' % (len(kreuz), t, prev, xc), flush=True)
                if args.kreuz_stopp > 0 and len(kreuz) == args.kreuz_stopp:
                    t_stopp = t + args.T_nach
            if t_stopp is not None and t >= t_stopp:
                grund = '%d Durchgaenge + T_nach' % args.kreuz_stopp
                break
            if kreuz and abs(xc) > args.stopp_x:
                grund = 'Ball bei |xi_c| > %g nach Durchgang' % args.stopp_x
                break
            if (step0 + k) % (nd * 100) == 0:
                el = time.perf_counter() - tl
                print('t %.1f x %.4f xi_c %.4f xi_m %.4f E %.6f E_damp %.3e Q %.6f E_ball %.6f S_max %.4f v_rms %.4f '
                      '(%.2f ms/Schritt)' % (t, rec['x'][-1], xc, rec['xi_m'][-1], rec['E_tot'][-1], rec['E_damp'][-1],
                                             rec['Q_tot'][-1], rec['E_ball'][-1], rec['S_max'][-1], rec['v_rms'][-1],
                                             1e3 * el / k), flush=True)
            if time.perf_counter() - T_START > args.wand:
                grund = 'Wandzeit'
                fertig = False
                break
    el = time.perf_counter() - tl
    meta['ms_je_schritt'] = 1e3 * el / max(k, 1)
    meta['schritte_dieser_abschnitt'] = k
    meta['grund_ende'] = grund
    meta['vollstaendig'] = fertig
    meta['kreuz_lauf'] = kreuz
    meta['ende'] = jetzt()
    meta['dauer_s'] = time.perf_counter() - T_START
    if not fertig:
        zpfad = args.zustand
        tmp = zpfad + '.tmp.npz'
        np.savez(tmp, phi=phi.cpu().numpy(), p=p.cpu().numpy(), t=rec['t'][-1], E_damp=float(E_damp),
                 Q_damp=float(Q_damp), meta=json.dumps(meta), rec=json.dumps(rec))
        os.replace(tmp, zpfad)
        meta['zustand'] = zpfad
        print('Zustand gespeichert:', zpfad, flush=True)
    schreibe_json(args.aus, dict(meta=meta, rec=rec))
    print('Ende: %s, t %.1f, %.2f ms/Schritt, Dauer %.1f s, geschrieben %s' % (
        grund, rec['t'][-1], meta['ms_je_schritt'], meta['dauer_s'], args.aus), flush=True)


# --------------------------------------------------------------------------------------------------------------------
# Auswertung (Regeln nach PLAN.md)
# --------------------------------------------------------------------------------------------------------------------
def steigung(t, y):
    if len(t) < 3:
        return None
    return float(np.polyfit(t, y, 1)[0])


def lokale_steigung(t, y, w):
    v = np.full(len(t), np.nan)
    for k in range(len(t)):
        m = np.abs(t - t[k]) <= w + 1e-9
        if m.sum() >= 3:
            v[k] = np.polyfit(t[m], y[m], 1)[0]
    return v


def analyse_lauf(L, stat, w_fit):
    m, r = L['meta'], L['rec']
    t = np.array(r['t'])
    xi = np.array(r['xi_c'])
    x = np.array(r['x'])
    xS = np.array(r['x_S'])
    a = dict(name=m['name'], n=m['n'], h=m['h'], dt=m['dt'], v0=m['v'], d0=m['d0'], T_ende=float(t[-1]),
             grund_ende=m['grund_ende'], vollstaendig=m['vollstaendig'], E_rest=m['E_rest'], K_eff=m['K_eff'],
             ms_je_schritt=m['ms_je_schritt'])
    Et, Ed, Qt, Qd = (np.array(r[k]) for k in ('E_tot', 'E_damp', 'Q_tot', 'Q_damp'))
    a['bilanz_E_max'] = float(np.max(np.abs(Et + Ed - Et[0])))
    a['bilanz_Q_max'] = float(np.max(np.abs(Qt + Qd - Qt[0])))
    a['E_absorbiert_ende'] = float(Ed[-1])
    a['E_ausserhalb_ball_ende'] = float(Et[-1] - r['E_ball'][-1])
    a['W_im_max'] = float(np.max(np.abs(r['W_im'])))
    a['S_max_spanne'] = [float(min(r['S_max'])), float(max(r['S_max']))]
    if m['v'] == 0:
        a['xi_c_drift_max'] = float(np.max(np.abs(xi - xi[0])))
        a['x_S_max'] = float(np.max(np.abs(xS)))
        a['v_rms_max'] = float(np.max(r['v_rms']))
        Eb = np.array(r['E_ball'])
        a['E_ball_rel_abw_max'] = float(np.max(np.abs(Eb / Eb[0] - 1)))
        return a
    ein = np.where(xi > -R_C)[0]
    if len(ein) == 0:
        a['ausgang'] = 'nicht angekommen'
        return a
    ke = int(ein[0])
    a['t_ein'] = float(t[ke])
    kreuz = []
    for k in range(max(ke, 1), len(xi)):
        if xi[k - 1] != 0 and np.sign(xi[k]) != np.sign(xi[k - 1]):
            kreuz.append(float(t[k - 1] + (t[k] - t[k - 1]) * (-xi[k - 1]) / (xi[k] - xi[k - 1])))
    a['t_kreuz'] = kreuz
    a['durchgaenge'] = len(kreuz)
    # Geschwindigkeiten
    mi = (t >= 20.0) & (x <= -X_FENSTER) & (t < t[ke])
    a['v_ein'] = steigung(t[mi], x[mi])
    a['v_ein_punkte'] = int(mi.sum())
    reihen = dict(v_ax=np.abs(lokale_steigung(t, xi, w_fit)), v_x=np.abs(lokale_steigung(t, x, w_fit)),
                  v_fm=np.abs(lokale_steigung(t, np.array(r['xi_m']), w_fit)),
                  v_xiS=np.abs(lokale_steigung(t, np.array(r['xi_S']), w_fit)),
                  v_rms=np.array(r['v_rms']), v_mean=np.array(r['v_mean']))
    grenzen = [0.0] + [0.5 * (kreuz[i] + kreuz[i + 1]) for i in range(len(kreuz) - 1)] + [float(t[-1])]
    durch = []
    for i in range(len(kreuz)):
        lo, hi = grenzen[i], grenzen[i + 1]
        mw = (t >= lo) & (t <= hi)
        dd = dict(nr=i + 1, t_kreuz=kreuz[i], fenster=[lo, hi])
        for nm, vv in reihen.items():
            vv_ = np.where(mw & np.isfinite(vv), vv, -1.0)
            kk = int(np.argmax(vv_))
            dd[nm + '_max'] = float(vv_[kk])
            dd[nm + '_t'] = float(t[kk])
            dd[nm + '_xi_c'] = float(xi[kk])
        # Umkehrpunkt nach diesem Durchgang (bis zum naechsten oder Laufende), Koordinate x_S wie KEGEL-Q
        hi2 = kreuz[i + 1] if i + 1 < len(kreuz) else float(t[-1])
        mu = (t > kreuz[i]) & (t <= hi2)
        if mu.sum() > 0:
            ku = int(np.argmax(np.where(mu, np.abs(xS), -1.0)))
            dd['umkehr_d'] = float(abs(xS[ku]))
            dd['umkehr_t'] = float(t[ku])
            dd['umkehr_xi_c'] = float(xi[ku])
            dd['umkehr_am_laufende'] = bool(ku == len(t) - 1)
        durch.append(dd)
    a['durchgang'] = durch
    # Energieerhaltung mit statischem B desselben Netzes
    if stat is not None and a['v_ein'] is not None:
        E_r = stat['E_fern']
        K0 = (1.0 / math.sqrt(1.0 - a['v_ein'] ** 2) - 1.0) * E_r
        gE = 1.0 + (K0 + stat['B_gitter']) / E_r
        a['K0'] = K0
        a['B_gitter'] = stat['B_gitter']
        a['E_rest_statik'] = E_r
        a['gamma_E'] = gE
        a['v_E'] = v_aus_gamma(gE)
        dpot = np.array([q['d'] for q in stat['punkte']])
        Vpot = np.array([q['E_korr'] for q in stat['punkte']]) - stat['E_fern']
        o = np.argsort(dpot)
        dpot, Vpot = dpot[o], Vpot[o]
        for i, dd in enumerate(durch):
            for nm in reihen:
                dd[nm + '_durch_v_E'] = dd[nm + '_max'] / a['v_E']
                vm = dd[nm + '_max']
                dd[nm + '_K'] = (1.0 / math.sqrt(1.0 - vm * vm) - 1.0) * E_r if 0 <= vm < 1 else None
            if 'umkehr_d' in dd and dd['umkehr_d'] <= dpot[-1]:
                dd['V_umkehr'] = float(np.interp(dd['umkehr_d'], dpot, Vpot))
                vor = K0 if i == 0 else durch[i - 1].get('V_umkehr')
                if vor is not None and not dd.get('umkehr_am_laufende'):
                    dd['verlust'] = vor - dd['V_umkehr']
                    dd['verlust_rel_K0_plus_B'] = dd['verlust'] / (K0 + stat['B_gitter'])
    return a


def befehl_auswertung(args):
    aus = dict(befehl='auswertung', start=jetzt(), w_fit=args.w_fit, urteile={}, teil_a={}, teil_b={})
    # ---- Teil A
    RA = lade(args.radial)
    zeilen = {round(z['s'], 6): z for z in RA['zeilen'] if 'fehler' not in z}
    aus['teil_a']['haupt'] = dict(datei=os.path.basename(args.radial), E_flach_Q=RA['flach_Q']['E'],
                                  grenzwert=RA['grenzwert_s_unendlich'], zeilen=RA['zeilen'],
                                  familie_max_res=RA['familie_max_res'], familie_Q_max=RA['familie_Q_max'])
    for nm, pfad in (('dr_probe', args.radial_dr), ('rmax_probe', args.radial_rmax)):
        if pfad and os.path.exists(pfad):
            P = lade(pfad)
            pz = {round(z['s'], 6): z for z in P['zeilen'] if 'fehler' not in z}
            aus['teil_a'][nm] = dict(datei=os.path.basename(pfad), dE_flach_Q=P['flach_Q']['E'] - RA['flach_Q']['E'],
                                     zeilen=[dict(s=s, dB=pz[s]['B'] - zeilen[s]['B'],
                                                  dv=pz[s]['v_grund'] - zeilen[s]['v_grund'])
                                             for s in sorted(pz) if s in zeilen])
    z12 = zeilen.get(1.2)
    if z12:
        rel = (z12['B'] - 1.4465) / 1.4465
        aus['urteile']['L0'] = dict(eingetroffen=bool(abs(rel) < 0.002), B_s1_2=z12['B'], soll=1.4465, rel_abw=rel,
                                    regel='|B(s = 1,2) - 1,4465| / 1,4465 < 0,002 (Q = 200, radial dr = 0,01)')
    else:
        aus['urteile']['L0'] = dict(eingetroffen=None, urteil='nicht entscheidbar (s = 1,2 fehlt)')
    bereiche = {1.5: (0.15, 0.23), 2.0: (0.19, 0.29), 6.0: (0.26, 0.40)}
    teile = {}
    ok1 = True
    for s_, (lo, hi) in bereiche.items():
        z = zeilen.get(s_)
        if z is None:
            ok1 = None
            teile['s=%g' % s_] = 'fehlt'
            continue
        tr = lo <= z['v_grund'] <= hi
        teile['s=%g' % s_] = dict(v=z['v_grund'], bereich=[lo, hi], drin=bool(tr))
        if ok1 is not None:
            ok1 = ok1 and tr
    v_alle = [z['v_grund'] for z in zeilen.values()] + [RA['grenzwert_s_unendlich']['v']]
    teile['max_v_alle_s_und_grenzwert'] = float(max(v_alle))
    if ok1 is not None:
        ok1 = ok1 and max(v_alle) < 0.45
    aus['urteile']['L1'] = dict(eingetroffen=ok1, teile=teile,
                                regel='v(1,5) in [0,15; 0,23], v(2) in [0,19; 0,29], v(6) in [0,26; 0,40] und v < 0,45 '
                                      'fuer alle gerechneten s und den Grenzwert s -> unendlich')
    # ---- Teil B
    stat = lade(args.statik) if args.statik and os.path.exists(args.statik) else None
    if stat is not None:
        aus['teil_b']['statik'] = {k: stat.get(k) for k in ('n', 'h', 'R', 'Q', 's', 'B_exakt', 'B_gitter', 'B_rel_abw',
                                                            'E_spitze', 'E_fern', 'd_fern', 'E_fern_gegen_radial_rel')}
        aus['teil_b']['statik']['netz'] = stat['netz']
        aus['teil_b']['statik']['V'] = [[q['d'], q['E_korr'] - stat['E_fern'], q['d_W'], q['S_spitze'], q['res_max']]
                                        for q in sorted(stat['punkte'], key=lambda q: q['d'])]
    laeufe = {}
    for pth in sorted(glob.glob(os.path.join(args.ordner, 'li-*.json'))):
        L = lade(pth)
        if L.get('meta', {}).get('befehl') == 'lauf':
            st = stat if (stat is not None and L['meta']['n'] == stat['n'] and abs(L['meta']['h'] - stat['h']) < 1e-12) \
                else None
            laeufe[L['meta']['name']] = analyse_lauf(L, st, args.w_fit)
    aus['teil_b']['laeufe'] = laeufe
    if stat is not None:
        nz = stat['netz']
        nn = stat['n']
        ruhe = laeufe.get(args.ruhe) if args.ruhe else None
        teile = dict(grad_spitze=bool(nz['grad_spitze'] == nn),
                     defekt=bool(abs(nz['defekt_spitze'] - nz['defekt_soll']) < 1e-9),
                     euler=bool(nz['euler'] == 1),
                     innen_grade=bool(set(nz['innen_grade'].keys()) <= {str(nn), '6'} and
                                      nz['innen_grade'].get(str(nn), 0) == 1),
                     B_1_prozent=bool(stat.get('B_rel_abw') is not None and abs(stat['B_rel_abw']) < 0.01),
                     ruhe=(bool(ruhe['xi_c_drift_max'] < 0.1 and ruhe['E_ball_rel_abw_max'] < 1e-3)
                           if ruhe and 'xi_c_drift_max' in ruhe else None))
        aus['teil_b']['netz_traegt'] = dict(teile=teile, ergebnis=(None if teile['ruhe'] is None else
                                                                   bool(all(teile.values()))),
                                            regel='Grad Spitze n, Defekt Soll auf 1e-9, Euler 1, Innenecken nur Grad 6 '
                                                  'ausser der Spitze, |B_gitter/B_exakt - 1| < 1 %, ruhender Kegelball: '
                                                  'Drift xi_c < 0,1 und E_ball < 1e-3 relativ')
    H = laeufe.get(args.haupt)
    if H is None or 'durchgang' not in H or len(H['durchgang']) < 1 or 'v_E' not in H:
        aus['urteile']['L2'] = dict(eingetroffen=None, urteil='nicht entscheidbar')
        aus['urteile']['L3'] = dict(eingetroffen=None, urteil='nicht entscheidbar')
    else:
        d1 = H['durchgang'][0]
        MU = 'v_rms'      # Urteilsmass nach PLAN.md
        rel = d1[MU + '_max'] / H['v_E'] - 1.0
        aus['urteile']['L2'] = dict(eingetroffen=bool(abs(rel) < 0.15), v_max_1=d1[MU + '_max'], v_E=H['v_E'],
                                    rel_abw=rel, lauf=args.haupt, mass='v_rms (Ladungsfluss)',
                                    andere_masse={nm: d1[nm + '_max'] / H['v_E'] - 1.0
                                                  for nm in ('v_x', 'v_ax', 'v_fm', 'v_xiS', 'v_mean')},
                                    regel='|v_rms,max(1. Durchgang) / v_E - 1| < 0,15; v_E aus gamma = 1 + (K0 + B_gitter)/E_fern')
        if len(H['durchgang']) >= 2:
            d2 = H['durchgang'][1]
            aus['urteile']['L3'] = dict(eingetroffen=bool(d2[MU + '_max'] < d1[MU + '_max']), v_max_1=d1[MU + '_max'],
                                        v_max_2=d2[MU + '_max'], lauf=args.haupt, mass='v_rms (Ladungsfluss)',
                                        andere_masse={nm: [d1[nm + '_max'], d2[nm + '_max']]
                                                      for nm in ('v_x', 'v_ax', 'v_fm', 'v_xiS', 'v_mean')},
                                        regel='v_rms,max(2. Durchgang) < v_rms,max(1. Durchgang)')
        else:
            aus['urteile']['L3'] = dict(eingetroffen=None, urteil='nicht entscheidbar (kein zweiter Durchgang)')
        konv = {}
        for nm in args.konvergenz.split(',') if args.konvergenz else []:
            K = laeufe.get(nm)
            if K and K.get('durchgang'):
                kd = K['durchgang']
                konv[nm] = dict(v_max_1=kd[0][MU + '_max'], rel_zu_haupt_1=kd[0][MU + '_max'] / d1[MU + '_max'] - 1.0,
                                v_max_2=kd[1][MU + '_max'] if len(kd) > 1 else None,
                                rel_zu_haupt_2=(kd[1][MU + '_max'] / H['durchgang'][1][MU + '_max'] - 1.0)
                                if (len(kd) > 1 and len(H['durchgang']) > 1) else None,
                                L2_gleich=bool(abs(kd[0][MU + '_max'] / H['v_E'] - 1.0) < 0.15) ==
                                aus['urteile']['L2']['eingetroffen'],
                                L3_gleich=(bool(kd[1][MU + '_max'] < kd[0][MU + '_max']) ==
                                           aus['urteile']['L3']['eingetroffen']) if len(kd) > 1 and
                                aus['urteile']['L3']['eingetroffen'] is not None else None)
        aus['urteile']['L2']['konvergenzproben'] = konv
        if konv and not all(k['L2_gleich'] for k in konv.values()):
            aus['urteile']['L2']['vermerk'] = 'nicht konvergiert'
        if konv and any(k['L3_gleich'] is False for k in konv.values()):
            aus['urteile']['L3']['vermerk'] = 'nicht konvergiert'
    aus['ende'] = jetzt()
    schreibe_json(os.path.join(args.ordner, 'auswertung.json'), aus)
    for k, v in aus['urteile'].items():
        print(k, v.get('eingetroffen'), json.dumps({kk: vv for kk, vv in v.items() if kk != 'regel'})[:600], flush=True)
    for nm, a in laeufe.items():
        print(nm, json.dumps({k: (round(v, 6) if isinstance(v, float) else v) for k, v in a.items()
                              if k != 'durchgang'}), flush=True)
        for dd in a.get('durchgang', []):
            print('   ', json.dumps({k: (round(v, 5) if isinstance(v, float) else v) for k, v in dd.items()}), flush=True)


# --------------------------------------------------------------------------------------------------------------------
# Bild v(t)
# --------------------------------------------------------------------------------------------------------------------
def befehl_bild(args):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    L = lade(os.path.join(args.ordner, 'li-%s.json' % args.name))
    A_ = lade(os.path.join(args.ordner, 'auswertung.json'))
    a = A_['teil_b']['laeufe'][args.name]
    r = L['rec']
    t = np.array(r['t'])
    t0 = max(0.0, a.get('t_ein', 0.0) - 150.0)
    m = t >= t0
    fig, axs = plt.subplots(2, 1, figsize=(11, 8.5), sharex=True)
    ax = axs[0]
    ax.plot(t[m], np.array(r['xi_c'])[m], '-', color='#c0392b', lw=1.5, label='xi_c (axialer Ladungsschwerpunkt)')
    ax.plot(t[m], np.array(r['x'])[m], '--', color='#555555', lw=1.0, label='x (harmonischer Schwerpunkt, EINFANG-1)')
    ax.plot(t[m], np.array(r['xi_m'])[m], ':', color='#2471a3', lw=1.0, label='xi_m (Feldmaximum auf der Achse)')
    for tk in a.get('t_kreuz', []):
        ax.axvline(tk, color='k', lw=0.5, ls=':')
    ax.axhline(0, color='k', lw=0.4)
    ax.set_ylabel('Ort auf der Achse (Spitze bei 0)')
    ax.set_title('LICHT-1: %s (n = %d, h = %g, dt = %g, v0 = %g, Q = 200)' % (args.name, a['n'], a['h'], a['dt'], a['v0']))
    ax.legend(fontsize=8)
    ax = axs[1]
    w = A_['w_fit']
    v_ax = np.abs(lokale_steigung(t, np.array(r['xi_c']), w))
    v_x = np.abs(lokale_steigung(t, np.array(r['x']), w))
    v_fm = np.abs(lokale_steigung(t, np.array(r['xi_m']), w))
    ax.plot(t[m], np.array(r['v_rms'])[m], '-', color='#27ae60', lw=2.0, label='v_rms Ladungsfluss (Urteilsmass L2/L3)')
    ax.plot(t[m], np.array(r['v_mean'])[m], '-', color='#7d3c98', lw=0.9, label='v_mean Ladungsfluss')
    ax.plot(t[m], v_ax[m], '-', color='#c0392b', lw=1.0, label='|d xi_c/dt| axialer Schwerpunkt')
    ax.plot(t[m], np.minimum(v_x[m], 1.0), '--', color='#555555', lw=0.9, label='|dx/dt| harmonisch (an der Spitze singulaer)')
    ax.plot(t[m], np.minimum(v_fm[m], 1.0), ':', color='#2471a3', lw=0.8, label='|d xi_m/dt| Feldmaximum')
    if 'v_E' in a:
        ax.axhline(a['v_E'], color='k', lw=1.0, ls='-.', label='v_E Energieerhaltung (B des Netzes) = %.3f' % a['v_E'])
    ax.set_ylim(0, max(0.45, 1.2 * a.get('v_E', 0.3)))
    ax.set_xlabel('t')
    ax.set_ylabel('Geschwindigkeit (c = 1)')
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(args.aus, dpi=120)
    print('geschrieben', args.aus)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='befehl', required=True)
    a = sub.add_parser('radial')
    a.add_argument('--Q', type=float, default=200.0)
    a.add_argument('--s', required=True)
    a.add_argument('--s-dEdQ', dest='s_dEdQ', default='')
    a.add_argument('--dr', type=float, default=0.01)
    a.add_argument('--rmax', type=float, default=90.0)
    a.add_argument('--eps-min', dest='eps_min', type=float, default=0.0065)
    a.add_argument('--q', type=float, default=0.96)
    a.add_argument('--aus', required=True)
    a = sub.add_parser('statik')
    a.add_argument('--n', type=int, required=True, choices=[3, 4, 5, 6, 7])
    a.add_argument('--h', type=float, required=True)
    a.add_argument('--R', type=float, default=60.0)
    a.add_argument('--Q', type=float, default=200.0)
    a.add_argument('--d', required=True)
    a.add_argument('--aus', required=True)
    a = sub.add_parser('lauf')
    a.add_argument('--name', required=True)
    a.add_argument('--n', type=int, required=True, choices=[3, 4, 5, 6, 7])
    a.add_argument('--h', type=float, required=True)
    a.add_argument('--R', type=float, default=60.0)
    a.add_argument('--rs', type=float, default=45.0)
    a.add_argument('--gmax', type=float, default=1.0)
    a.add_argument('--Q', type=float, default=200.0)
    a.add_argument('--v', type=float, required=True)
    a.add_argument('--d0', type=float, default=25.0)
    a.add_argument('--dt', type=float, required=True)
    a.add_argument('--T', type=float, required=True)
    a.add_argument('--diag', type=float, default=0.5)
    a.add_argument('--S-thr', dest='S_thr', type=float, default=0.01)
    a.add_argument('--R-ball', dest='R_ball', type=float, default=15.0)
    a.add_argument('--stopp-x', dest='stopp_x', type=float, default=24.0)
    a.add_argument('--kreuz-stopp', dest='kreuz_stopp', type=int, default=2)
    a.add_argument('--T-nach', dest='T_nach', type=float, default=80.0)
    a.add_argument('--geraet', choices=['cuda', 'cpu'], required=True)
    a.add_argument('--wand', type=float, default=540.0)
    a.add_argument('--zustand', default=None)
    a.add_argument('--fortsetzen', default=None)
    a.add_argument('--aus', required=True)
    a = sub.add_parser('auswertung')
    a.add_argument('--ordner', required=True)
    a.add_argument('--radial', required=True)
    a.add_argument('--radial-dr', dest='radial_dr', default=None)
    a.add_argument('--radial-rmax', dest='radial_rmax', default=None)
    a.add_argument('--statik', default=None)
    a.add_argument('--haupt', required=True)
    a.add_argument('--konvergenz', default='')
    a.add_argument('--ruhe', default='')
    a.add_argument('--w-fit', dest='w_fit', type=float, default=1.0)
    a = sub.add_parser('bild')
    a.add_argument('--ordner', required=True)
    a.add_argument('--name', required=True)
    a.add_argument('--aus', required=True)
    args = ap.parse_args()
    if args.befehl == 'lauf' and args.zustand is None:
        args.zustand = args.aus.replace('.json', '') + '-zustand.npz'
    try:
        {'radial': befehl_radial, 'statik': befehl_statik, 'lauf': befehl_lauf, 'auswertung': befehl_auswertung,
         'bild': befehl_bild}[args.befehl](args)
    except Exception:
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
