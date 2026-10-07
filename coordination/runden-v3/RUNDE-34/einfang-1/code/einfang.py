#!/usr/bin/env python3
"""EINFANG-1 (Runde 34, runden-v3, explorativ). Code-Agent fuer die Leitung claude-primary.

Faengt eine Fuenfer-Ecke des Dreiecksnetzes einen langsam heranlaufenden Q-Ball ein?

Netz und statischer Ball aus KEGEL-Q (kegel_q.py, Kopie von RUNDE-26/kegel-q/code/kegel_q.py.eingefroren-20261003-043140).
Zeitentwicklung des komplexen Feldes (Normierung genau wie im statischen Funktional von KEGEL-Q):
    A_i phi_i'' = -(L phi)_i - A_i U'(|phi_i|^2) phi_i - A_i gamma_i phi_i'
  L = Kotangens-Laplace (L phi)_i = Sum_j w_ij (phi_i - phi_j), Dirichlet phi = 0 auf den Randecken,
  U(S) = S - S^2 + S^3/2 (M1, beta = 1/2), gamma_i = Schwamm im Randband r > r_s (sonst 0).
  Energie  E = Sum A |phi'|^2 + phi^H L phi + Sum A U(|phi|^2)
  Ladung   Q = 2 Sum A Im(conj(phi') phi)
  Der statische Ball phi = f exp(-i omega t) mit L f + A (U'(f^2) - omega^2) f = 0 ist eine exakte stationaere Loesung.
Integrator: Stoermer-Verlet (Kick-Drift-Kick); Schwamm als exakter Faktor exp(-gamma dt/2) vor und nach jedem Schritt
(Strang-Teilung). Die dabei entzogene Energie und Ladung wird exakt mitgezaehlt (Energiebilanz).
Ort des Balls: harmonischer Schwerpunkt wie KEGEL-Q, W = <r^s exp(i s phi)>, s = 6/n, phi gegen den Startstrahl
theta0 = 0. Gewicht: Ladungsdichte auf den Ecken mit |phi|^2 > S_thr (Haupt, "x"); zum Vergleich |phi|^2 auf allen
Ecken ("x_S", Definition von KEGEL-Q). Vorzeichenbehaftete Bahnkoordinate x = -Re W |W|^(1/s - 1): Start bei
x = -d0 auf dem Startstrahl, Austritt bei x > 0 auf dem Gegenstrahl (phi = +-Theta/2).

Befehle: lauf, auswertung, bild.
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

PI = math.pi
T_START = time.perf_counter()
R_C = 6.2551 + 3.0      # R_half(Q = 200) + 3 aus KEGEL-Q radial.json (dr = 0,01): R_half = 6,2551
X_FENSTER = 12.0        # Geschwindigkeitsfenster |x| >= 12 (Rest des Potentials < 2e-4)


def jetzt():
    return time.strftime('%Y-%m-%dT%H:%M:%S%z')


def schreibe_json(pfad, obj):
    tmp = pfad + '.tmp'
    with open(tmp, 'w') as fh:
        json.dump(obj, fh, indent=1)
    os.replace(tmp, pfad)


def Uf(S):
    return S - S * S + 0.5 * S ** 3


# --------------------------------------------------------------------------------------------------------------------
# Lauf
# --------------------------------------------------------------------------------------------------------------------
def befehl_lauf(args):
    import torch
    from kegel_q import Netz, baue_familie, loese_Q, loese_ball
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
    s = net.s
    Theta = net.Theta
    print('Netz n=%d h=%g R=%g: %d Ecken, %d frei, Grad Spitze %d, Defekt %.6f, Bauzeit bis jetzt %.1f s' % (
        n, h, R, pr['ecken'], pr['freie_ecken'], pr['grad_spitze'], pr['defekt_spitze'],
        time.perf_counter() - T_START), flush=True)

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
        # Boost (Netzfassung): statisches Netzprofil f, Phase exp(i omega gamma u xi), u = -v (Richtung Spitze),
        # phi' = [-u d_X f - i omega gamma f] exp(...); d_X f aus dem radialen Kontinuumsprofil (Ladung Q_lat).
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
        meta = dict(befehl='lauf', name=args.name, start=jetzt(), n=n, h=h, R=R, rs=args.rs, gmax=args.gmax,
                    Q=args.Q, v=v, gamma=gam, d0=args.d0, dt=dt, T=args.T, diag=args.diag, S_thr=args.S_thr,
                    R_ball=args.R_ball, stopp_x=args.stopp_x, geraet=geraet_name, netz=pr,
                    radial_Q=dict(omega=g200['omega'], R_half=g200['R_half'], kappa=g200['kappa'], E=g200['E']),
                    ball=dict(Q_lat=Q_lat, E_lat=rb['E'], omega_lat=om, c1=rb['c1'], c2=rb['c2'],
                              res_max=rb['res_max'], aussen=rb['aussen'], dauer_s=tb, f_max=float(f.max()),
                              S_spitze=float(f[net.apex] ** 2)),
                    E_rest=E_rest, K_nominal=(gam - 1.0) * E_rest, R_c=R_C)
        rec = {k: [] for k in ('t', 'x', 'W_re', 'W_im', 'x_S', 'WS_re', 'WS_im', 'E_tot', 'Q_tot', 'E_damp',
                               'Q_damp', 'E_ball', 'Q_ball', 'S_max', 'S_spitze', 'Q_thr')}

    # Geraetefelder
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
    apex_f = int(np.searchsorted(fr, net.apex))
    assert fr[apex_f] == net.apex
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
        wq = torch.where(S > args.S_thr, q, torch.zeros_like(q))
        sq = wq.sum()
        wS = A * S
        sS = wS.sum()
        vals = torch.stack([e.sum(), q.sum(), sq, (wq * wu).sum() / sq, (wq * wv).sum() / sq,
                            (wS * wu).sum() / sS, (wS * wv).sum() / sS, S.max(), S[apex_f], Ed, Qd]).cpu().numpy()
        Et, Qt, Qthr, Wr, Wi, WSr, WSi, Smax, Sap, Edv, Qdv = [float(a) for a in vals]

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
        for k, val in (('t', t), ('x', x), ('W_re', Wr), ('W_im', Wi), ('x_S', xS), ('WS_re', WSr), ('WS_im', WSi),
                       ('E_tot', Et), ('Q_tot', Qt), ('E_damp', Edv), ('Q_damp', Qdv), ('E_ball', float(bv[0])),
                       ('Q_ball', float(bv[1])), ('S_max', Smax), ('S_spitze', Sap), ('Q_thr', Qthr)):
            rec[k].append(val)
        return x

    nd = int(round(args.diag / dt))
    n_steps = int(round((args.T - t_now) / dt))
    step0 = int(round(t_now / dt))
    if not args.fortsetzen:
        x = diagnose(phi, p, 0.0, E_damp, Q_damp)
        meta['E0'] = rec['E_tot'][0]
        meta['Q0'] = rec['Q_tot'][0]
        meta['K_eff'] = rec['E_tot'][0] - meta['E_rest']
        print('Start: E %.8f Q %.8f E_rest %.8f K_eff %.6f K_nominal %.6f x %.4f Q_ball %.6f' % (
            meta['E0'], meta['Q0'], meta['E_rest'], meta['K_eff'], meta['K_nominal'], x, rec['Q_ball'][0]), flush=True)
    xs = np.array(rec['x'])
    eingetreten = bool(np.any(xs > -R_C))
    ausgetreten = False
    if eingetreten:
        k_e = int(np.argmax(xs > -R_C))
        ausgetreten = bool(np.any(np.abs(xs[k_e:]) > R_C))
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
            x = diagnose(phi, p, t, E_damp, Q_damp)
            if not math.isfinite(x) or not math.isfinite(rec['E_tot'][-1]):
                grund = 'nicht endlich'
                break
            if not eingetreten and x > -R_C:
                eingetreten = True
            elif eingetreten and not ausgetreten and abs(x) > R_C:
                ausgetreten = True
            if ausgetreten and abs(x) > args.stopp_x:
                grund = 'Ball bei |x| > %g nach Austritt' % args.stopp_x
                break
            if (step0 + k) % (nd * 50) == 0:
                el = time.perf_counter() - tl
                print('t %.1f x %.4f x_S %.4f E %.6f E_damp %.3e Q %.6f E_ball %.6f Q_ball %.6f S_max %.4f '
                      '(%.2f ms/Schritt)' % (t, x, rec['x_S'][-1], rec['E_tot'][-1], rec['E_damp'][-1],
                                             rec['Q_tot'][-1], rec['E_ball'][-1], rec['Q_ball'][-1],
                                             rec['S_max'][-1], 1e3 * el / k), flush=True)
            if time.perf_counter() - T_START > args.wand:
                grund = 'Wandzeit'
                fertig = False
                break
    el = time.perf_counter() - tl
    meta['ms_je_schritt'] = 1e3 * el / max(k, 1)
    meta['schritte_dieser_abschnitt'] = k
    meta['grund_ende'] = grund
    meta['vollstaendig'] = fertig
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
def lade(p):
    with open(p) as fh:
        return json.load(fh)


def steigung(t, y):
    if len(t) < 3:
        return None
    a, b = np.polyfit(t, y, 1)
    return float(a)


def potential(kraft_json, n):
    """V(d) = E(d) - E_flach aus KEGEL-Q (h = 0,3, Q = 200); E_flach aus bind-n6-h0.3-Q200.json."""
    K = lade(kraft_json)
    Ef = lade(os.path.join(os.path.dirname(kraft_json), 'bind-n6-h0.3-Q200.json'))['punkte'][0]['E_korr_erste_ordnung']
    d = np.array([pt['d'] for pt in K['punkte']])
    E = np.array([pt['E_korr_erste_ordnung'] for pt in K['punkte']])
    o = np.argsort(d)
    return d[o], E[o] - Ef


def analyse(L, pot):
    m, r = L['meta'], L['rec']
    t = np.array(r['t'])
    x = np.array(r['x'])
    xS = np.array(r['x_S'])
    Eb, Qb = np.array(r['E_ball']), np.array(r['Q_ball'])
    E_rest, om = m['E_rest'], m['ball']['omega_lat']
    a = dict(name=m['name'], n=m['n'], v=m['v'], h=m['h'], dt=m['dt'], gmax=m['gmax'], T_ende=float(t[-1]),
             grund_ende=m['grund_ende'], K_nominal=m['K_nominal'], K_eff=m['K_eff'], E0=m['E0'], Q0=m['Q0'])
    # Energie- und Ladungsbilanz (Gesamtnetz + Schwamm)
    Et, Ed, Qt, Qd = np.array(r['E_tot']), np.array(r['E_damp']), np.array(r['Q_tot']), np.array(r['Q_damp'])
    a['bilanz_E_max'] = float(np.max(np.abs(Et + Ed - Et[0])))
    a['bilanz_Q_max'] = float(np.max(np.abs(Qt + Qd - Qt[0])))
    a['E_absorbiert_ende'] = float(Ed[-1])
    a['Q_absorbiert_ende'] = float(Qd[-1])
    a['E_unterwegs_ende'] = float(Et[-1] - Eb[-1])
    a['Q_unterwegs_ende'] = float(Qt[-1] - Qb[-1])
    a['E_abgestrahlt_ende'] = a['E_absorbiert_ende'] + a['E_unterwegs_ende']
    a['Q_abgestrahlt_ende'] = a['Q_absorbiert_ende'] + a['Q_unterwegs_ende']
    a['Q_ball_0'] = float(Qb[0])
    a['Q_ball_ende'] = float(Qb[-1])
    a['E_ball_0'] = float(Eb[0])
    a['E_ball_ende'] = float(Eb[-1])
    if m['v'] == 0:
        a['ausgang'] = 'ruhend'
        a['x_abw_max'] = float(np.max(np.abs(x - x[0])))
        a['E_ball_rel_abw_max'] = float(np.max(np.abs(Eb / Eb[0] - 1)))
        a['Q_ball_rel_abw_max'] = float(np.max(np.abs(Qb / Qb[0] - 1)))
        a['S_max_spanne'] = [float(min(r['S_max'])), float(max(r['S_max']))]
        return a
    ein = np.where(x > -R_C)[0]
    if len(ein) == 0:
        a['ausgang'] = 'nicht angekommen'
        return a
    ke = int(ein[0])
    a['t_ein'] = float(t[ke])
    kreuz = [k for k in range(max(ke, 1), len(x)) if np.sign(x[k]) != np.sign(x[k - 1]) and x[k - 1] != 0]
    raus = [k for k in range(ke + 1, len(x)) if abs(x[k]) > R_C]
    ka = raus[0] if raus else None
    a['t_kreuz'] = [float(t[k]) for k in kreuz]
    if ka is not None:
        nk = len([k for k in kreuz if k <= ka])
        a['t_aus'] = float(t[ka])
        a['seite_aus'] = 'fern' if x[ka] > 0 else 'nah'
        a['durchgaenge_vor_aus'] = nk
        if x[ka] > 0 and nk == 1:
            a['ausgang'] = 'durchgelaufen'
        elif x[ka] < 0 and nk == 0:
            a['ausgang'] = 'zurueckgeworfen'
        else:
            a['ausgang'] = 'nach %d Durchgaengen ausgetreten (%s)' % (nk, a['seite_aus'])
    else:
        T_frei = 4.0 * R_C / m['v']
        a['T_frei_regel'] = T_frei
        a['durchgaenge'] = len(kreuz)
        if len(kreuz) >= 2 or (t[-1] - t[ke] >= T_frei):
            a['ausgang'] = 'eingefangen'
        else:
            a['ausgang'] = 'offen (Lauf zu kurz)'
    # Geschwindigkeiten
    mi = (t >= 20.0) & (x <= -X_FENSTER) & (t < t[ke])
    a['v_ein'] = steigung(t[mi], x[mi])
    a['v_ein_punkte'] = int(mi.sum())
    if ka is not None:
        mo = (t > t[ka]) & (np.abs(x) >= X_FENSTER)
        a['v_aus'] = steigung(t[mo], np.abs(x[mo]))
        a['v_aus_punkte'] = int(mo.sum())
        a['v_aus_x_spanne'] = [float(np.abs(x[mo]).min()), float(np.abs(x[mo]).max())] if mo.sum() else None
    else:
        mo = None
        a['v_aus'] = None

    def K(v, Q):
        return (1.0 / math.sqrt(1.0 - v * v) - 1.0) * (E_rest + om * (Q - m['Q']))
    if a['v_ein'] is not None:
        a['Q_ball_ein'] = float(Qb[mi].mean())
        a['E_ball_ein'] = float(Eb[mi].mean())
        a['K_ein'] = K(a['v_ein'], a['Q_ball_ein'])
    if a.get('v_aus') is not None and a['v_ein'] is not None:
        a['Q_ball_aus'] = float(Qb[mo].mean())
        a['E_ball_aus'] = float(Eb[mo].mean())
        a['K_aus'] = K(a['v_aus'], a['Q_ball_aus'])
        a['verlust_K'] = a['K_ein'] - a['K_aus']
        a['verlust_K_rel'] = a['verlust_K'] / a['K_ein']
        a['verlust_E_ball'] = a['E_ball_ein'] - a['E_ball_aus']
        a['verlust_Q_ball'] = a['Q_ball_ein'] - a['Q_ball_aus']
        a['E_innen_aus'] = a['E_ball_aus'] - (E_rest + om * (a['Q_ball_aus'] - m['Q'])) - a['K_aus']
        a['E_innen_ein'] = a['E_ball_ein'] - (E_rest + om * (a['Q_ball_ein'] - m['Q'])) - a['K_ein']
    # Umkehrpunkte gegen das statische Potential (KEGEL-Q, h = 0,3), Koordinate x_S wie KEGEL-Q
    if pot is not None and a.get('K_ein') is not None:
        dpot, Vpot = pot
        if a['ausgang'] == 'zurueckgeworfen':
            k0 = int(np.argmax(xS))
            dU_ = abs(float(xS[k0]))
            a['umkehr_d'] = dU_
            a['V_umkehr'] = float(np.interp(dU_, dpot, Vpot))
            a['umkehr_V_minus_K_ein'] = a['V_umkehr'] - a['K_ein']
        elif kreuz:
            k1 = kreuz[0]
            k2 = kreuz[1] if len(kreuz) > 1 else len(x)
            seg = slice(k1, k2)
            if ka is None or ka > k1:
                kk = k1 + int(np.argmax(np.abs(xS[seg])))
                if ka is None or kk < ka:
                    dU_ = abs(float(xS[kk]))
                    a['umkehr1_d'] = dU_
                    a['umkehr1_t'] = float(t[kk])
                    a['V_umkehr1'] = float(np.interp(dU_, dpot, Vpot))
                    a['verlust_1_aus_umkehr'] = a['K_ein'] - a['V_umkehr1']
    a['S_max_spanne'] = [float(min(r['S_max'])), float(max(r['S_max']))]
    return a


def befehl_auswertung(args):
    dateien = sorted(glob.glob(os.path.join(args.ordner, 'ef-*.json')))
    laeufe = {}
    for p in dateien:
        L = lade(p)
        if L.get('meta', {}).get('befehl') == 'lauf':
            laeufe[L['meta']['name']] = L
    pot5 = potential(args.kraft5, 5)
    pot7 = potential(args.kraft7, 7)
    an = {}
    for name, L in sorted(laeufe.items()):
        pot = pot5 if L['meta']['n'] == 5 else (pot7 if L['meta']['n'] == 7 else None)
        an[name] = analyse(L, pot)
        an[name]['vollstaendig'] = L['meta']['vollstaendig']
    aus = dict(befehl='auswertung', start=jetzt(), R_c=R_C, X_fenster=X_FENSTER, laeufe=an, urteile={})
    # EF0: flaches Netz, v = 0,05
    L = laeufe.get('e6-v0.05')
    if L:
        r = L['rec']
        t, x, Qb = np.array(r['t']), np.array(r['x']), np.array(r['Q_ball'])
        m1 = (t >= 20) & (t <= 120)
        m2 = (t >= 350) & (t <= 450)
        vf, v4 = steigung(t[m1], x[m1]), steigung(t[m2], x[m2])
        k400 = int(np.argmin(np.abs(t - 400.0)))
        dq = float(Qb[k400] / Qb[0] - 1.0)
        ok = (vf is not None and v4 is not None and abs(v4 / vf - 1.0) < 0.05 and abs(dq) < 0.01)
        aus['urteile']['EF0'] = dict(eingetroffen=bool(ok), v_frueh=vf, v_400=v4,
                                     v_400_durch_v_frueh_minus_1=(v4 / vf - 1.0) if (vf and v4) else None,
                                     v_frueh_durch_nominal_minus_1=(vf / 0.05 - 1.0) if vf else None,
                                     Q_ball_400_rel=dq, t_400=float(t[k400]),
                                     regel='|v(350..450)/v(20..120) - 1| < 0,05 und |Q_ball(400)/Q_ball(0) - 1| < 0,01')
    else:
        aus['urteile']['EF0'] = dict(eingetroffen=None, urteil='nicht entscheidbar (Lauf fehlt)')

    def ausgang(name):
        return an[name]['ausgang'] if name in an else None
    a1, a2 = ausgang('f5-v0.1'), ausgang('f5-v0.05')
    if a1 and a2:
        def verlaesst(nm):
            return an[nm].get('t_aus') is not None and an[nm]['ausgang'] != 'eingefangen'
        aus['urteile']['EF1'] = dict(eingetroffen=bool(verlaesst('f5-v0.1') and verlaesst('f5-v0.05')),
                                     ausgang_v0_1=a1, ausgang_v0_05=a2,
                                     regel='beide Laeufe: Austritt |x| > R_c nach dem Eintritt, kein Einfang')
    else:
        aus['urteile']['EF1'] = dict(eingetroffen=None, urteil='nicht entscheidbar')
    a3 = ausgang('f5-v0.02')
    if a3:
        ent = a3 not in ('offen (Lauf zu kurz)', 'nicht angekommen')
        aus['urteile']['EF2'] = dict(eingetroffen=(bool(a3 == 'eingefangen') if ent else None), ausgang=a3,
                                     regel='Ausgang "eingefangen" (|x| <= R_c von t_ein bis Laufende, dazu mindestens '
                                           'zwei Durchgaenge oder T_ende - t_ein >= 4 R_c/v)')
        konv = {}
        for nm in ('f5-v0.02-dt0.05', 'f5-v0.02-h0.2'):
            if nm in an:
                konv[nm] = dict(ausgang=an[nm]['ausgang'], v_aus=an[nm].get('v_aus'), verlust_K=an[nm].get('verlust_K'),
                                gleicher_ausgang=bool(an[nm]['ausgang'] == a3))
        aus['urteile']['EF2']['konvergenzproben'] = konv
        if konv and not all(k['gleicher_ausgang'] for k in konv.values()):
            aus['urteile']['EF2']['vermerk'] = 'nicht konvergiert: eine Konvergenzprobe hat einen anderen Ausgang'
    else:
        aus['urteile']['EF2'] = dict(eingetroffen=None, urteil='nicht entscheidbar')
    a4 = ausgang('s7-v0.05')
    if a4:
        aus['urteile']['EF3'] = dict(eingetroffen=bool(a4 == 'zurueckgeworfen'), ausgang=a4,
                                     regel='Ausgang "zurueckgeworfen": x bleibt < 0 (keine Spitzenkreuzung), Austritt bei '
                                           'x < -R_c')
    else:
        aus['urteile']['EF3'] = dict(eingetroffen=None, urteil='nicht entscheidbar')
    aus['ende'] = jetzt()
    schreibe_json(os.path.join(args.ordner, 'auswertung.json'), aus)
    for k, v in aus['urteile'].items():
        print(k, v.get('eingetroffen'), {kk: vv for kk, vv in v.items() if kk not in ('regel',)}, flush=True)
    for nm, a in an.items():
        print(nm, json.dumps({k: (round(v, 6) if isinstance(v, float) else v) for k, v in a.items()}), flush=True)


# --------------------------------------------------------------------------------------------------------------------
# Bild
# --------------------------------------------------------------------------------------------------------------------
def befehl_bild(args):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    dateien = sorted(glob.glob(os.path.join(args.ordner, 'ef-*.json')))
    fig, axs = plt.subplots(1, 2, figsize=(13, 5.2))
    farben = {5: '#c0392b', 6: '#555555', 7: '#2471a3'}
    stile = {0.1: '-', 0.05: '--', 0.02: ':', 0.0: '-.'}
    for p in dateien:
        L = lade(p)
        m = L.get('meta', {})
        if m.get('befehl') != 'lauf':
            continue
        if m['name'] not in args.namen.split(','):
            continue
        t, x = np.array(L['rec']['t']), np.array(L['rec']['x'])
        lab = '%s (n=%d, v=%g, h=%g, dt=%g)' % (m['name'], m['n'], m['v'], m['h'], m['dt'])
        ax = axs[0]
        ax.plot(t, x, stile.get(m['v'], '-'), color=farben[m['n']], lw=1.4, label=lab)
        ax2 = axs[1]
        ax2.plot(t, np.array(L['rec']['E_ball']) - L['rec']['E_ball'][0], stile.get(m['v'], '-'), color=farben[m['n']],
                 lw=1.2, label=m['name'])
    for ax in axs[:1]:
        ax.axhline(R_C, color='k', lw=0.6, ls=':')
        ax.axhline(-R_C, color='k', lw=0.6, ls=':')
        ax.axhline(0, color='k', lw=0.4)
        ax.set_xlabel('t')
        ax.set_ylabel('x (harmonischer Ladungsschwerpunkt, Spitze bei 0)')
        ax.set_title('EINFANG-1: Bahnen, Q = 200 (gepunktet: +-R_c = R_half + 3)')
        ax.legend(fontsize=7)
    axs[1].set_xlabel('t')
    axs[1].set_ylabel('E_ball(t) - E_ball(0)')
    axs[1].set_title('Ballenergie (Scheibe r < 15 um den Ball)')
    axs[1].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(args.aus, dpi=130)
    print('geschrieben', args.aus)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='befehl', required=True)
    a = sub.add_parser('lauf')
    a.add_argument('--name', required=True)
    a.add_argument('--n', type=int, required=True, choices=[5, 6, 7])
    a.add_argument('--h', type=float, required=True)
    a.add_argument('--R', type=float, default=60.0)
    a.add_argument('--rs', type=float, default=45.0)
    a.add_argument('--gmax', type=float, default=1.0)
    a.add_argument('--Q', type=float, default=200.0)
    a.add_argument('--v', type=float, required=True)
    a.add_argument('--d0', type=float, default=25.0)
    a.add_argument('--dt', type=float, required=True)
    a.add_argument('--T', type=float, required=True)
    a.add_argument('--diag', type=float, default=2.0)
    a.add_argument('--S-thr', dest='S_thr', type=float, default=0.01)
    a.add_argument('--R-ball', dest='R_ball', type=float, default=15.0)
    a.add_argument('--stopp-x', dest='stopp_x', type=float, default=24.0)
    a.add_argument('--geraet', choices=['cuda', 'cpu'], required=True)
    a.add_argument('--wand', type=float, default=540.0)
    a.add_argument('--zustand', default=None)
    a.add_argument('--fortsetzen', default=None)
    a.add_argument('--aus', required=True)
    a = sub.add_parser('auswertung')
    a.add_argument('--ordner', required=True)
    a.add_argument('--kraft5', required=True)
    a.add_argument('--kraft7', required=True)
    a = sub.add_parser('bild')
    a.add_argument('--ordner', required=True)
    a.add_argument('--namen', required=True)
    a.add_argument('--aus', required=True)
    args = ap.parse_args()
    if args.befehl == 'lauf' and args.zustand is None:
        args.zustand = args.aus.replace('.json', '') + '-zustand.npz'
    try:
        {'lauf': befehl_lauf, 'auswertung': befehl_auswertung, 'bild': befehl_bild}[args.befehl](args)
    except Exception:
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
