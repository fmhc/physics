#!/usr/bin/env python3
"""DREIECK-LINSE-1 (Runde 36, runden-v3, explorativ). Code-Agent fuer die Leitung claude-primary.

Wirkt eine Fuenfer-Spitze (Kegel mit Fehlwinkel delta = pi/3) auf vorbeilaufende Q-Baelle wie eine Linse aus der
2+1-Gravitation? Q-Baelle laufen parallel zur Achse durch die Spitze mit Stossparameter +b bzw. -b an ihr vorbei.

Netz, statischer Ball und Zeitentwicklung wie EINFANG-1 (RUNDE-34/einfang-1/code/einfang.py; kegel_q.py unveraendert
aus RUNDE-26). Neu: B Baelle in B voneinander unabhaengigen Feldern auf demselben Netz (Stapel; die Felder wechselwirken
nicht, jedes Feld ist ein eigener Lauf mit genau einem Ball):
    A_i phi_i'' = -(L phi)_i - A_i U'(|phi_i|^2) phi_i - A_i gamma_i phi_i'
  L = Kotangens-Laplace, Dirichlet phi = 0 auf den Randecken, U(S) = S - S^2 + S^3/2 (M1, beta = 1/2),
  gamma_i = Schwamm g_max ((r - r_s)/(R - r_s))^2 fuer r > r_s.
  Energie E = Sum A |phi'|^2 + phi^H L phi + Sum A U(|phi|^2), Ladung Q = 2 Sum A Im(conj(phi') phi).
  Stoermer-Verlet (Kick-Drift-Kick), Schwamm als exakter Faktor exp(-gamma dt/2) vor und nach jedem Schritt; die
  entzogene Energie und Ladung wird je Feld mitgezaehlt.
Start je Feld: statischer Netzball (kegel_q.loese_ball, Q_lat = Q/gamma_v) mit harmonischem Schwerpunkt bei z0 = X0 + i b
in der Einlaufkarte; Boost mit v in Richtung -X (zur Spitze hin, parallel zur Achse), wie EINFANG-1 ohne
Lorentz-Kontraktion.
Kegelkoordinaten (r, phi): r = geodaetischer Abstand zur Spitze, phi = Abwicklungswinkel gegen den Einlaufstrahl
theta0 = 0 (Gitterrichtung), phi in [-Theta/2, Theta/2), Theta = n pi/3.
Ort des Balls: harmonischer Schwerpunkt W = Sum g q w / Sum g q, w = r^s exp(i s phi), s = 6/n, q = Ladung je Ecke,
  g = glattes Fenster um den letzten Ort: 1 bis Abstand 12, cos^2-Abfall bis 18, 0 dahinter (geodaetischer Abstand).
  W ist auf dem Kegel eindeutig (kein Schnitt); W = z_c^s exakt fuer runde Baelle, die die Spitze nicht ueberdecken.
  Vergleich (beschreibend): harte Schwelle |phi|^2 > 0,01 wie EINFANG-1.
Entwicklungskarten (abgerollte Dreiecke, Abstand d = |W|^(1/s)):
  Einlaufkarte  z_E = d exp(i arg(W)/s):  Schnitt hinter der Spitze (Gegenstrahl), = Netzkoordinaten (X, Y).
  Auslaufkarte  z_A = d exp(i arg(-W)/s): Schnitt vor der Spitze (Einlaufstrahl). Beide Bahnen +b und -b liegen darin
                ganz ohne Schnittdurchgang; die Verbindung ihrer Auslaufstuecke laeuft hinter der Spitze und umrundet
                sie nicht. Fuer Ecken: phi_A = phi - Theta/2 (phi > 0) bzw. phi + Theta/2 (phi <= 0).
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
F_R1 = 12.0       # glattes Fenster: Gewicht 1 bis zum Abstand 12 vom letzten Ort
F_R2 = 18.0       # ... cos^2-Abfall bis 18
S_THR = 0.01      # harte Schwelle (Vergleichsmass wie EINFANG-1)
R_BALL = 15.0     # Ballscheibe fuer E_ball, Q_ball
# Auswerteregeln (PLAN.md, Abschnitt 4)
T_SKIP = 30.0     # Startstrecke (Boost-Einschwingen) ausgenommen
D_FIT = 15.0      # Geradenausgleich nur fern der Spitze: d >= 15
D_MAX = 56.0      # ... und d <= 56 (Ball mindestens 14 vor dem Schwamm r_s = 70)
N_MIN = 50        # mindestens 50 Diagnosepunkte je Fenster
B_LISTE = (10.0, 20.0, 30.0, 40.0)


def jetzt():
    return time.strftime('%Y-%m-%dT%H:%M:%S%z')


def sauber(o):
    """Nicht endliche Zahlen -> None, numpy -> Python (jq-lesbares JSON)."""
    if isinstance(o, dict):
        return {str(k): sauber(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [sauber(v) for v in o]
    if isinstance(o, np.ndarray):
        return [sauber(v) for v in o.tolist()]
    if isinstance(o, (float, np.floating)):
        return float(o) if math.isfinite(float(o)) else None
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


def schreibe_json(pfad, obj):
    tmp = pfad + '.tmp'
    with open(tmp, 'w') as fh:
        json.dump(sauber(obj), fh, indent=1)
    os.replace(tmp, pfad)


def lade(p):
    with open(p) as fh:
        return json.load(fh)


def auslauf_winkel(phi, Theta):
    """Ecken-Winkel der Auslaufkarte (Schnitt auf dem Einlaufstrahl phi = 0)."""
    return np.where(phi > 0, phi - Theta / 2.0, phi + Theta / 2.0)


def kartenpruefung(net):
    """Kantenlaengen in beiden Entwicklungskarten: isometrisch abgerollt (Laenge h) oder am Schnitt; Kanten am Schnitt
    muessen nach Kleben mit der Drehung um Theta (Winkelsumme an der Spitze) wieder die Laenge h haben."""
    Theta_netz = float(net.winkelsumme[net.apex])
    aus = dict(winkelsumme_spitze=Theta_netz, Theta_soll=net.Theta,
               winkelsumme_minus_soll=Theta_netz - net.Theta)
    for name, ph in (('einlauf', net.phi), ('auslauf', auslauf_winkel(net.phi, net.Theta))):
        z = net.r * np.exp(1j * ph)
        zi, zj = z[net.kanten_i], z[net.kanten_j]
        L = np.abs(zi - zj)
        abw = np.abs(L - net.h)
        schnitt = abw > 1e-9
        Lg = np.minimum(np.abs(zi - zj * np.exp(1j * Theta_netz)), np.abs(zi - zj * np.exp(-1j * Theta_netz)))
        aus[name] = dict(kanten=int(len(L)), isometrisch=int((~schnitt).sum()), am_schnitt=int(schnitt.sum()),
                         max_abw_isometrisch=float(abw[~schnitt].max()),
                         max_abw_geklebt=float(np.abs(Lg[schnitt] - net.h).max()) if schnitt.any() else None)
    return aus


# --------------------------------------------------------------------------------------------------------------------
# Lauf
# --------------------------------------------------------------------------------------------------------------------
def befehl_lauf(args):
    import torch
    from kegel_q import Netz, baue_familie, loese_Q, loese_ball
    if not torch.cuda.is_available():
        raise RuntimeError('CUDA verlangt, aber nicht verfuegbar (kein CPU-Ausweichen)')
    torch.set_num_threads(1)
    dev = torch.device('cuda')
    geraet_name = torch.cuda.get_device_name(0)
    print('torch %s, Geraet %s (%s)' % (torch.__version__, dev, geraet_name), flush=True)
    dt, n, h, R = args.dt, args.n, args.h, args.R
    bs = [float(x) for x in args.b.split(',')]
    B = len(bs)
    net = Netz(n, h, R)
    net.setze_richtung(0.0)
    pr = net.pruefung()
    kp = kartenpruefung(net)
    fr = net.frei
    Nf = len(fr)
    s = net.s
    Theta = net.Theta
    print('Netz n=%d h=%g R=%g: %d Ecken, %d frei, Grad Spitze %d, Defekt %.6f, Euler %d (%.1f s)' % (
        n, h, R, pr['ecken'], pr['freie_ecken'], pr['grad_spitze'], pr['defekt_spitze'], pr['euler'],
        time.perf_counter() - T_START), flush=True)
    print('Kartenpruefung:', json.dumps(sauber(kp)), flush=True)

    if args.fortsetzen:
        z = np.load(args.fortsetzen)
        meta = json.loads(str(z['meta']))
        rec = json.loads(str(z['rec']))
        if meta['b'] != bs or meta['n'] != n or meta['h'] != h or meta['dt'] != dt:
            raise RuntimeError('Fortsetzung passt nicht zu den Argumenten')
        phi_np, p_np = z['phi'], z['p']
        t_now = float(z['t'])
        Ed0, Qd0 = z['E_damp'], z['Q_damp']
        dc0, phc0 = z['dc'], z['phc']
        meta['fortsetzungen'] = meta.get('fortsetzungen', []) + [dict(datei=args.fortsetzen, t=t_now, start=jetzt())]
        print('fortgesetzt bei t = %.3f aus %s' % (t_now, args.fortsetzen), flush=True)
    else:
        v = args.v
        gam = 1.0 / math.sqrt(1.0 - v * v)
        rad, fam = baue_familie(0.01, 60.0)
        g200, _ = loese_Q(rad, fam, args.Q)
        Q_lat = args.Q / gam
        gQ, fQ = loese_Q(rad, fam, Q_lat)
        dfr = np.gradient(fQ, rad.r)
        phi_np = np.zeros((Nf, B, 2))
        p_np = np.zeros((Nf, B, 2))
        baelle = []
        for k, b in enumerate(bs):
            r0 = math.hypot(args.X0, b)
            ph0 = math.atan2(b, args.X0)
            D1 = r0 ** s * math.cos(s * ph0)
            D2 = r0 ** s * math.sin(s * ph0)
            dist = net.abstand(xy=(args.X0, b))
            f0 = np.interp(dist, rad.r, fQ, right=0.0)
            f0[net.rand] = 0.0
            tb = time.perf_counter()
            rb, f = loese_ball(net, Q_lat, D1, D2, f0, 5.0, 1e-9, 12, 40000, 1e-10)
            tb = time.perf_counter() - tb
            om = rb['omega']
            xi = net.X - args.X0
            dfd = np.interp(dist, rad.r, dfr, right=0.0)
            dXf = np.where(dist > 1e-12, dfd * xi / np.maximum(dist, 1e-12), 0.0)
            phase = np.exp(-1j * om * gam * v * xi)
            phi_c = f * phase
            p_c = (v * dXf - 1j * om * gam * f) * phase
            phi_c[net.rand] = 0.0
            p_c[net.rand] = 0.0
            phi_np[:, k, 0] = phi_c.real[fr]
            phi_np[:, k, 1] = phi_c.imag[fr]
            p_np[:, k, 0] = p_c.real[fr]
            p_np[:, k, 1] = p_c.imag[fr]
            baelle.append(dict(b=b, X0=args.X0, d0=r0, phi0=ph0, D1=D1, D2=D2, Q_lat=Q_lat, E_lat=rb['E'], omega_lat=om,
                               c1=rb['c1'], c2=rb['c2'], res_max=rb['res_max'], aussen=rb['aussen'], nit=rb['nit'],
                               dauer_s=tb, f_max=float(f.max()), S_spitze=float(f[net.apex] ** 2),
                               E_rest=rb['E'] + om * (args.Q - Q_lat)))
            print('Ball b=%g: E %.8f omega %.6f c %.1e %.1e res %.1e aussen %d (%.1f s)' % (
                b, rb['E'], om, rb['c1'], rb['c2'], rb['res_max'], rb['aussen'], tb), flush=True)
        t_now = 0.0
        Ed0 = np.zeros(B)
        Qd0 = np.zeros(B)
        dc0 = np.array([math.hypot(args.X0, b) for b in bs])
        phc0 = np.array([math.atan2(b, args.X0) for b in bs])
        meta = dict(befehl='lauf', name=args.name, start=jetzt(), n=n, h=h, R=R, rs=args.rs, gmax=args.gmax, Q=args.Q,
                    v=v, gamma=gam, X0=args.X0, b=bs, dt=dt, T=args.T, diag=args.diag, s=s, Theta=Theta,
                    fenster=[F_R1, F_R2], S_thr=S_THR, R_ball=R_BALL, geraet=geraet_name, netz=pr, kartenpruefung=kp,
                    radial_Q=dict(omega=g200['omega'], R_half=g200['R_half'], kappa=g200['kappa'], E=g200['E']),
                    baelle=baelle)
        rec = dict(t=[])
        for key in REC_KEYS:
            rec[key] = []

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
    c_half2 = c_half * c_half
    A_s = A[idx]
    apex_f = int(np.searchsorted(fr, net.apex))
    assert fr[apex_f] == net.apex
    phi = torch.tensor(phi_np, dtype=f64, device=dev).contiguous()
    p = torch.tensor(p_np, dtype=f64, device=dev).contiguous()
    E_damp = torch.tensor(np.asarray(Ed0, dtype=float), dtype=f64, device=dev)
    Q_damp = torch.tensor(np.asarray(Qd0, dtype=float), dtype=f64, device=dev)
    dc = torch.tensor(np.asarray(dc0, dtype=float), dtype=f64, device=dev)
    phc = torch.tensor(np.asarray(phc0, dtype=float), dtype=f64, device=dev)

    def lap(ph):
        return (Lt @ ph.reshape(Nf, 2 * B)).reshape(Nf, B, 2)

    def kraft(ph):
        S = (ph * ph).sum(2)
        dU = 1.0 - 2.0 * S + 1.5 * S * S
        return -lap(ph) * invA[:, None, None] - dU[:, :, None] * ph

    def daempfe(ph, pp, Ed, Qd):
        ps = pp[idx]
        Ed = Ed + (A_s[:, None] * (1.0 - c_half2)[:, None] * (ps * ps).sum(2)).sum(0)
        qs = 2.0 * A_s[:, None] * (ps[:, :, 0] * ph[idx, :, 1] - ps[:, :, 1] * ph[idx, :, 0])
        Qd = Qd + ((1.0 - c_half)[:, None] * qs).sum(0)
        pp[idx] = ps * c_half[:, None, None]
        return Ed, Qd

    def abstand(d_, ph_):
        D = torch.remainder((ang[:, None] - ph_[None, :]).abs(), Theta)
        D = torch.minimum(D, Theta - D)
        q2 = rr[:, None] ** 2 + d_[None, :] ** 2 - 2.0 * rr[:, None] * d_[None, :] * torch.cos(D)
        return torch.where(D < PI, torch.sqrt(torch.clamp(q2, min=0.0)), rr[:, None] + d_[None, :])

    def diagnose(ph, pp, t, Ed, Qd, d_, ph_):
        S = (ph * ph).sum(2)
        q = 2.0 * A[:, None] * (pp[:, :, 0] * ph[:, :, 1] - pp[:, :, 1] * ph[:, :, 0])
        e = A[:, None] * (pp * pp).sum(2) + (ph * lap(ph)).sum(2) + A[:, None] * (S - S * S + 0.5 * S ** 3)
        dist = abstand(d_, ph_)
        xg = torch.clamp((dist - F_R1) / (F_R2 - F_R1), 0.0, 1.0)
        g = torch.cos(0.5 * PI * xg) ** 2
        wq = g * q
        sq = wq.sum(0)
        Wr = (wq * wu[:, None]).sum(0) / sq
        Wi = (wq * wv[:, None]).sum(0) / sq
        wt = torch.where(S > S_THR, q, torch.zeros_like(q))
        st = wt.sum(0)
        WTr = (wt * wu[:, None]).sum(0) / st
        WTi = (wt * wv[:, None]).sum(0) / st
        dn = torch.sqrt(Wr * Wr + Wi * Wi) ** (1.0 / s)
        phn = torch.atan2(Wi, Wr) / s
        mb = abstand(dn, phn) < R_BALL
        Eb = (e * mb).sum(0)
        Qb = (q * mb).sum(0)
        vals = torch.stack([Wr, Wi, WTr, WTi, sq, e.sum(0), q.sum(0), Ed, Qd, Eb, Qb, S.max(0).values, S[apex_f]])
        arr = vals.cpu().numpy()
        rec['t'].append(t)
        for j, key in enumerate(REC_KEYS):
            rec[key].append([float(a) for a in arr[j]])
        return dn, phn, bool(np.all(np.isfinite(arr)))

    nd = int(round(args.diag / dt))
    n_steps = int(round((args.T - t_now) / dt))
    step0 = int(round(t_now / dt))
    if not args.fortsetzen:
        dc, phc, ok = diagnose(phi, p, 0.0, E_damp, Q_damp, dc, phc)
        meta['E0'] = rec['E_tot'][0]
        meta['Q0'] = rec['Q_tot'][0]
        meta['K_eff'] = [rec['E_tot'][0][k] - meta['baelle'][k]['E_rest'] for k in range(B)]
        meta['K_nominal'] = [(meta['gamma'] - 1.0) * meta['baelle'][k]['E_rest'] for k in range(B)]
        print('Start: E0 %s Q0 %s K_eff %s' % (['%.6f' % x for x in meta['E0']], ['%.6f' % x for x in meta['Q0']],
                                             ['%.5f' % x for x in meta['K_eff']]), flush=True)
    F = kraft(phi)
    torch.cuda.synchronize()
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
            dc, phc, ok = diagnose(phi, p, t, E_damp, Q_damp, dc, phc)
            if not ok:
                grund = 'nicht endlich'
                break
            if (step0 + k) % (nd * 50) == 0:
                el = time.perf_counter() - tl
                dd = (np.array(rec['W_re'][-1]) ** 2 + np.array(rec['W_im'][-1]) ** 2) ** (0.5 / s)
                print('t %.1f d %s E %.6f Q %.6f (%.2f ms/Schritt)' % (
                    t, ' '.join('%.2f' % x for x in dd), sum(rec['E_tot'][-1]), sum(rec['Q_tot'][-1]), 1e3 * el / k),
                    flush=True)
            if time.perf_counter() - T_START > args.wand:
                grund = 'Wandzeit'
                fertig = False
                break
    torch.cuda.synchronize()
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
        np.savez(tmp, phi=phi.cpu().numpy(), p=p.cpu().numpy(), t=rec['t'][-1], E_damp=E_damp.cpu().numpy(),
                 Q_damp=Q_damp.cpu().numpy(), dc=dc.cpu().numpy(), phc=phc.cpu().numpy(),
                 meta=json.dumps(sauber(meta)), rec=json.dumps(sauber(rec)))
        os.replace(tmp, zpfad)
        meta['zustand'] = zpfad
        print('Zustand gespeichert:', zpfad, flush=True)
    schreibe_json(args.aus, dict(meta=meta, rec=rec))
    print('Ende: %s, t %.1f, %.2f ms/Schritt, Dauer %.1f s, geschrieben %s' % (
        grund, rec['t'][-1], meta['ms_je_schritt'], meta['dauer_s'], args.aus), flush=True)


REC_KEYS = ('W_re', 'W_im', 'WT_re', 'WT_im', 'Q_fenster', 'E_tot', 'Q_tot', 'E_damp', 'Q_damp', 'E_ball', 'Q_ball',
            'S_max', 'S_spitze')


# --------------------------------------------------------------------------------------------------------------------
# Auswertung (Regeln nach PLAN.md, Abschnitt 4)
# --------------------------------------------------------------------------------------------------------------------
def wrapgrad(a):
    return (a + 180.0) % 360.0 - 180.0


def gerade(t, z, haelften=True):
    """Geradenausgleich x(t), y(t) (je lineare Regression): Richtung, Schnelle, senkrechte Abweichung."""
    if len(t) < N_MIN:
        return None
    ax = np.polyfit(t, z.real, 1)
    ay = np.polyfit(t, z.imag, 1)
    vx, vy = float(ax[0]), float(ay[0])
    sp = math.hypot(vx, vy)
    ex, ey = vx / sp, vy / sp
    rx = z.real - (ax[1] + vx * t)
    ry = z.imag - (ay[1] + vy * t)
    perp = -rx * ey + ry * ex
    out = dict(n=int(len(t)), t_von=float(t[0]), t_bis=float(t[-1]), theta_grad=math.degrees(math.atan2(vy, vx)),
               v=sp, vx=vx, vy=vy, rms_senkrecht=float(np.sqrt(np.mean(perp ** 2))),
               max_senkrecht=float(np.max(np.abs(perp))))
    if haelften:
        m = len(t) // 2
        h1 = gerade(t[:m], z[:m], False) if m >= N_MIN else None
        h2 = gerade(t[m:], z[m:], False) if len(t) - m >= N_MIN else None
        if h1 and h2:
            out['theta_haelften'] = [h1['theta_grad'], h2['theta_grad']]
            out['v_haelften'] = [h1['v'], h2['v']]
            out['theta_haelften_diff'] = wrapgrad(h2['theta_grad'] - h1['theta_grad'])
    return out


def analyse_feld(meta, rec, k, wkey=('W_re', 'W_im')):
    s, Theta = meta['s'], meta['Theta']
    b = meta['b'][k]
    t = np.array(rec['t'])
    W = np.array([x[k] for x in rec[wkey[0]]]) + 1j * np.array([x[k] for x in rec[wkey[1]]])
    d = np.abs(W) ** (1.0 / s)
    phE = np.angle(W) / s
    phA = np.angle(-W) / s
    zA = d * np.exp(1j * phA)
    phU = np.unwrap(phE, period=Theta)
    zU = d * np.exp(1j * phU)
    a = dict(b=b, T_ende=float(t[-1]), punkte=int(len(t)))
    if not np.all(np.isfinite(W)):
        a['fehler'] = 'nicht endlich'
        return a, None
    kca = int(np.argmin(d))
    a['t_naechste'] = float(t[kca])
    a['d_min'] = float(d[kca])
    a['phiA_naechste_grad'] = math.degrees(phA[kca])
    a['d_ende'] = float(d[-1])
    m_in = (t >= T_SKIP) & (t < t[kca]) & (d >= D_FIT) & (d <= D_MAX)
    m_out = (t > t[kca]) & (d >= D_FIT) & (d <= D_MAX)
    a['ein'] = gerade(t[m_in], zA[m_in])
    a['aus'] = gerade(t[m_out], zA[m_out])
    a['ein_eigen'] = gerade(t[m_in], zU[m_in], False)
    a['aus_eigen'] = gerade(t[m_out], zU[m_out], False)
    a['ende_im_fenster'] = bool(d[-1] > D_MAX)
    if a['ein'] and a['aus']:
        eps = wrapgrad(a['aus']['theta_grad'] - a['ein']['theta_grad'])
        # Seite der Spitze: Kreuzprodukt Einlaufrichtung x (Spitze - Punkt der Einlaufgeraden)
        z1 = zA[m_in][0]
        cr = a['ein']['vx'] * (0.0 - z1.imag) - a['ein']['vy'] * (0.0 - z1.real)
        a['spitze_links'] = bool(cr > 0)
        a['ablenkung_grad'] = eps
        a['ablenkung_zur_spitze_grad'] = eps if cr > 0 else -eps
        a['v_ein'] = a['ein']['v']
        a['v_aus'] = a['aus']['v']
        a['v_aus_durch_v_ein_minus_1'] = a['aus']['v'] / a['ein']['v'] - 1.0
        a['v_ein_durch_v0_minus_1'] = a['ein']['v'] / meta['v'] - 1.0
    if a['ein_eigen'] and a['aus_eigen']:
        a['ablenkung_eigen_grad'] = wrapgrad(a['aus_eigen']['theta_grad'] - a['ein_eigen']['theta_grad'])
    # Bilanzen
    Et = np.array([x[k] for x in rec['E_tot']])
    Ed = np.array([x[k] for x in rec['E_damp']])
    Qt = np.array([x[k] for x in rec['Q_tot']])
    Qd = np.array([x[k] for x in rec['Q_damp']])
    Eb = np.array([x[k] for x in rec['E_ball']])
    Qb = np.array([x[k] for x in rec['Q_ball']])
    Sm = np.array([x[k] for x in rec['S_max']])
    a['bilanz_E_max'] = float(np.max(np.abs(Et + Ed - Et[0])))
    a['bilanz_Q_max'] = float(np.max(np.abs(Qt + Qd - Qt[0])))
    a['E_damp_ende'] = float(Ed[-1])
    a['Q_damp_ende'] = float(Qd[-1])
    for nm, msk in (('ein', m_in), ('aus', m_out)):
        if msk.sum() > 0:
            a['E_ball_' + nm] = float(Eb[msk].mean())
            a['Q_ball_' + nm] = float(Qb[msk].mean())
            a['S_max_spanne_' + nm] = [float(Sm[msk].min()), float(Sm[msk].max())]
    if 'E_ball_ein' in a and 'E_ball_aus' in a:
        a['E_ball_aus_minus_ein'] = a['E_ball_aus'] - a['E_ball_ein']
        a['Q_ball_aus_minus_ein'] = a['Q_ball_aus'] - a['Q_ball_ein']
    bahn = dict(t=t, d=d, zA=zA, m_in=m_in, m_out=m_out)
    return a, bahn


def analyse_lauf(L, wkey=('W_re', 'W_im')):
    meta, rec = L['meta'], L['rec']
    felder = {}
    bahnen = {}
    for k, b in enumerate(meta['b']):
        a, bahn = analyse_feld(meta, rec, k, wkey)
        felder['%+g' % b] = a
        bahnen['%+g' % b] = bahn
    Theta_grad = math.degrees(meta['kartenpruefung']['winkelsumme_spitze'])
    paare = {}
    for b in B_LISTE:
        ap, am = felder.get('%+g' % b), felder.get('%+g' % (-b))
        if ap is None or am is None or not (ap.get('aus') and am.get('aus') and ap.get('ein') and am.get('ein')):
            paare['%g' % b] = dict(auswertbar=False)
            continue
        w_aus = wrapgrad(ap['aus']['theta_grad'] - am['aus']['theta_grad'])
        w_ein = wrapgrad(ap['ein']['theta_grad'] - am['ein']['theta_grad'])
        pa = dict(auswertbar=True, winkel_aus_grad=w_aus, winkel_ein_grad=w_ein,
                  winkel_aus_minus_ein_grad=w_aus - w_ein,
                  ablenkung_zur_spitze_plus=ap['ablenkung_zur_spitze_grad'],
                  ablenkung_zur_spitze_minus=am['ablenkung_zur_spitze_grad'],
                  spiegel_diff_ablenkung=ap['ablenkung_zur_spitze_grad'] - am['ablenkung_zur_spitze_grad'],
                  v_aus_durch_v_ein_minus_1=[ap['v_aus_durch_v_ein_minus_1'], am['v_aus_durch_v_ein_minus_1']])
        # Schnittprobe: Einlaufkarte (Schnitt hinter der Spitze), jede Bahn in eigener Abwicklung; das Auslaufstueck
        # von -b wird ueber den Gegenstrahl (Kleben mit der Winkelsumme der Spitze) an das Blatt von +b gelegt.
        if ap.get('aus_eigen') and am.get('aus_eigen'):
            pa['winkel_aus_einlaufkarte_geklebt_grad'] = wrapgrad(
                ap['aus_eigen']['theta_grad'] - (am['aus_eigen']['theta_grad'] + Theta_grad))
            pa['schnittprobe_diff_grad'] = wrapgrad(pa['winkel_aus_einlaufkarte_geklebt_grad'] - w_aus)
        paare['%g' % b] = pa
    return dict(name=meta['name'], n=meta['n'], h=meta['h'], dt=meta['dt'], T_ende=float(L['rec']['t'][-1]),
                vollstaendig=meta.get('vollstaendig'), felder=felder, paare=paare, Theta_netz_grad=Theta_grad,
                ms_je_schritt=meta.get('ms_je_schritt')), bahnen


def urteile_kegel(an):
    """D1, D2, D3 aus der Analyse eines Kegel-Laufs (n = 5)."""
    u = {}
    P = an['paare']
    # D1
    w = {b: P.get('%g' % b, {}).get('winkel_aus_grad') if P.get('%g' % b, {}).get('auswertbar') else None
         for b in (20.0, 30.0, 40.0)}
    if any(x is None for x in w.values()):
        u['D1'] = dict(urteil='nicht auswertbar', werte=dict(winkel=w))
    else:
        dev = {b: x - 60.0 for b, x in w.items()}
        spann = max(w.values()) - min(w.values())
        ok = all(abs(x) <= 2.0 for x in dev.values()) and spann < 2.0
        u['D1'] = dict(urteil='eingetroffen' if ok else 'nicht eingetroffen',
                       werte=dict(winkel_aus_grad={'%g' % b: x for b, x in w.items()},
                                  abweichung_von_60_grad={'%g' % b: x for b, x in dev.items()}, spannweite_grad=spann),
                       regel='b = 20, 30, 40: |Winkel - 60 Grad| <= 2 Grad je b und Spannweite (max - min) < 2 Grad')
    # D2
    p10 = P.get('10', {})
    if not p10.get('auswertbar'):
        u['D2'] = dict(urteil='nicht auswertbar', werte={})
    else:
        x = p10['winkel_aus_grad']
        u['D2'] = dict(urteil='eingetroffen' if x - 60.0 >= 3.0 else 'nicht eingetroffen',
                       werte=dict(winkel_aus_grad=x, ueber_60_grad=x - 60.0,
                                  ablenkung_zur_spitze=[p10['ablenkung_zur_spitze_plus'],
                                                        p10['ablenkung_zur_spitze_minus']]),
                       regel='b = 10: Winkel - 60 Grad >= 3 Grad')
    # D3
    r = {}
    for b in (20.0, 30.0, 40.0, -20.0, -30.0, -40.0):
        f = an['felder'].get('%+g' % b)
        r['%+g' % b] = f.get('v_aus_durch_v_ein_minus_1') if f else None
    if any(x is None for x in r.values()):
        u['D3'] = dict(urteil='nicht auswertbar', werte=dict(v_aus_durch_v_ein_minus_1=r))
    else:
        mx = max(abs(x) for x in r.values())
        u['D3'] = dict(urteil='eingetroffen' if mx < 0.02 else 'nicht eingetroffen',
                       werte=dict(v_aus_durch_v_ein_minus_1=r, max_betrag=mx),
                       regel='b = +-20, +-30, +-40: |v_aus/v_ein - 1| < 0,02 je Bahn')
    return u


def urteil_flach(an):
    P = an['paare']
    w = {}
    for b in (10.0, 20.0, 30.0, 40.0):
        w['%g' % b] = P.get('%g' % b, {}).get('winkel_aus_grad') if P.get('%g' % b, {}).get('auswertbar') else None
    r = {}
    for b in (10.0, 20.0, 30.0, 40.0):
        for sg in (1.0, -1.0):
            f = an['felder'].get('%+g' % (sg * b))
            r['%+g' % (sg * b)] = f.get('v_aus_durch_v_ein_minus_1') if f else None
    if any(x is None for x in w.values()) or any(x is None for x in r.values()):
        return dict(urteil='nicht auswertbar', werte=dict(winkel_aus_grad=w, v_aus_durch_v_ein_minus_1=r))
    mw = max(abs(x) for x in w.values())
    mr = max(abs(x) for x in r.values())
    return dict(urteil='eingetroffen' if (mw < 0.5 and mr < 0.01) else 'nicht eingetroffen',
                werte=dict(winkel_aus_grad=w, max_betrag_winkel=mw, v_aus_durch_v_ein_minus_1=r, max_betrag_v=mr),
                regel='flaches Netz, b = 10, 20, 30, 40: |Winkel| < 0,5 Grad je b; alle 8 Bahnen |v_aus/v_ein - 1| < 0,01')


def befehl_auswertung(args):
    global B_LISTE
    B_LISTE = tuple(float(x) for x in args.b_liste.split(","))
    dateien = {os.path.basename(p)[:-5]: p for p in sorted(glob.glob(os.path.join(args.ordner, 'li-*.json')))}
    an = {}
    an_thr = {}
    for nm, p in dateien.items():
        L = lade(p)
        if L.get('meta', {}).get('befehl') != 'lauf':
            continue
        an[nm], _ = analyse_lauf(L)
        an_thr[nm], _ = analyse_lauf(L, ('WT_re', 'WT_im'))
    aus = dict(befehl='auswertung', start=jetzt(), regeln=dict(T_skip=T_SKIP, D_fit=D_FIT, D_max=D_MAX, N_min=N_MIN,
                                                               fenster=[F_R1, F_R2]),
               dateien=sorted(dateien), laeufe=an, urteile={}, konvergenz={}, vergleich_schwelle={})
    haupt_k, haupt_f = args.kegel, args.flach
    proben = [x for x in args.proben.split(',') if x]
    if haupt_f in an:
        aus['urteile']['D0'] = urteil_flach(an[haupt_f])
    else:
        aus['urteile']['D0'] = dict(urteil='nicht auswertbar', vermerk='Lauf %s fehlt' % haupt_f, werte={})
    if haupt_k in an:
        aus['urteile'].update(urteile_kegel(an[haupt_k]))
    else:
        for d_ in ('D1', 'D2', 'D3'):
            aus['urteile'][d_] = dict(urteil='nicht auswertbar', vermerk='Lauf %s fehlt' % haupt_k, werte={})
    # Konvergenzproben: gleiche Regeln; anderes Urteil -> Vermerk "nicht konvergiert" (Urteil bleibt)
    for pnm in proben:
        if pnm not in an:
            aus['konvergenz'][pnm] = dict(vorhanden=False)
            continue
        up = urteile_kegel(an[pnm])
        aus['konvergenz'][pnm] = dict(vorhanden=True, urteile=up)
        for d_ in ('D1', 'D2', 'D3'):
            if d_ not in aus['urteile'] or aus['urteile'][d_]['urteil'] == 'nicht auswertbar':
                continue
            # Teilprobe: nur Groessen, deren Bahnen in der Probe gerechnet sind
            if up[d_]['urteil'] == 'nicht auswertbar':
                continue
            if up[d_]['urteil'] != aus['urteile'][d_]['urteil']:
                alt = aus['urteile'][d_].get('vermerk')
                neu = 'nicht konvergiert (%s: %s)' % (pnm, up[d_]['urteil'])
                aus['urteile'][d_]['vermerk'] = (alt + '; ' + neu) if alt else neu
    # Vergleich mit dem Schwellen-Schwerpunkt (beschreibend)
    for nm in an:
        v = {}
        for b in B_LISTE:
            a1, a2 = an[nm]['paare']['%g' % b], an_thr[nm]['paare']['%g' % b]
            if a1.get('auswertbar') and a2.get('auswertbar'):
                v['%g' % b] = dict(winkel_fenster=a1['winkel_aus_grad'], winkel_schwelle=a2['winkel_aus_grad'],
                                   diff=a2['winkel_aus_grad'] - a1['winkel_aus_grad'])
        aus['vergleich_schwelle'][nm] = v
    aus['ende'] = jetzt()
    schreibe_json(os.path.join(args.ordner, 'auswertung.json'), aus)
    for k_, v_ in aus['urteile'].items():
        print(k_, v_['urteil'], v_.get('vermerk', ''), json.dumps(sauber(v_.get('werte', {}))), flush=True)
    for nm, a in an.items():
        for b in B_LISTE:
            pa = a['paare']['%g' % b]
            if pa.get('auswertbar'):
                print('%s b=%g: Winkel aus %.4f ein %.4f; Ablenkung zur Spitze %+.4f %+.4f; v %+.2e %+.2e; Schnittprobe '
                      '%.1e' % (nm, b, pa['winkel_aus_grad'], pa['winkel_ein_grad'], pa['ablenkung_zur_spitze_plus'],
                                pa['ablenkung_zur_spitze_minus'], pa['v_aus_durch_v_ein_minus_1'][0],
                                pa['v_aus_durch_v_ein_minus_1'][1], pa.get('schnittprobe_diff_grad', float('nan'))),
                      flush=True)
            else:
                print('%s b=%g: nicht auswertbar' % (nm, b), flush=True)


# --------------------------------------------------------------------------------------------------------------------
# Bilder
# --------------------------------------------------------------------------------------------------------------------
def befehl_bild(args):
    global B_LISTE
    B_LISTE = tuple(float(x) for x in args.b_liste.split(","))
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    farben = {10.0: '#c0392b', 20.0: '#d68910', 30.0: '#239b56', 40.0: '#2471a3'}
    laeufe = [x for x in args.laeufe.split(',') if x]
    fig, axs = plt.subplots(1, len(laeufe), figsize=(7.2 * len(laeufe), 7.0))
    if len(laeufe) == 1:
        axs = [axs]
    for ax, nm in zip(axs, laeufe):
        p = os.path.join(args.ordner, nm + '.json')
        if not os.path.exists(p):
            continue
        L = lade(p)
        an, bahnen = analyse_lauf(L)
        meta = L['meta']
        Th = meta['Theta']
        if meta['n'] != 6:
            # fehlender Keil der Auslaufkarte (Schnitt auf dem Einlaufstrahl)
            rr_ = 90.0
            a1, a2 = Th / 2.0, 2 * PI - Th / 2.0
            ww = np.linspace(a1, a2, 50)
            ax.fill(np.concatenate([[0], rr_ * np.cos(ww), [0]]), np.concatenate([[0], rr_ * np.sin(ww), [0]]),
                    color='#dddddd', zorder=0, label='fehlender Keil (Schnitt vor der Spitze)')
        circ = np.linspace(0, 2 * PI, 200)
        ax.plot(D_MAX * np.cos(circ), D_MAX * np.sin(circ), ':', color='#888888', lw=0.7)
        ax.plot(D_FIT * np.cos(circ), D_FIT * np.sin(circ), ':', color='#888888', lw=0.7)
        ax.plot([0], [0], 'k*', ms=10, label='Spitze' if meta['n'] != 6 else 'Mitte')
        for kk, b in enumerate(meta['b']):
            bn = bahnen['%+g' % b]
            if bn is None:
                continue
            c = farben.get(abs(b), 'k')
            ls = '-' if b > 0 else '--'
            ax.plot(bn['zA'].real, bn['zA'].imag, ls, color=c, lw=1.0, label='b = %+g' % b)
            a = an['felder']['%+g' % b]
            for key, msk in (('ein', bn['m_in']), ('aus', bn['m_out'])):
                g = a.get(key)
                if g is None:
                    continue
                zz = bn['zA'][msk]
                ax.plot(zz.real, zz.imag, '-', color=c, lw=2.6, alpha=0.35)
                # Ausgleichsgerade, verlaengert
                t0 = np.array([g['t_von'] - 600, g['t_bis'] + 600]) if key == 'aus' else np.array([g['t_von'] - 200, g['t_bis'] + 900])
                tt = np.array([g['t_von'], g['t_bis']])
                zm = zz.mean()
                tm = 0.5 * (tt[0] + tt[1])
                xs = zm.real + g['vx'] * (t0 - tm)
                ys = zm.imag + g['vy'] * (t0 - tm)
                ax.plot(xs, ys, ':', color=c, lw=0.8)
        ax.set_aspect('equal')
        ax.set_xlim(-75, 75)
        ax.set_ylim(-75, 75)
        ax.set_xlabel('x (Auslaufkarte)')
        ax.set_ylabel('y (Auslaufkarte)')
        tit = 'Fuenfer-Spitze (n = 5)' if meta['n'] == 5 else ('flaches Netz (n = 6)' if meta['n'] == 6 else 'n = %d' % meta['n'])
        ax.set_title('%s, %s: Bahnen in der abgerollten Ebene\n(Schnitt vor der Spitze; dick: Ausgleichsfenster)' % (nm, tit),
                     fontsize=10)
        ax.legend(fontsize=7, loc='lower left')
    fig.tight_layout()
    fig.savefig(os.path.join(args.ordner, 'bahnen.png'), dpi=120)
    print('geschrieben bahnen.png', flush=True)
    # Winkel gegen b
    A = lade(os.path.join(args.ordner, 'auswertung.json'))
    fig, axs = plt.subplots(1, 3, figsize=(16, 4.8))
    stil = {args.kegel: ('o', '#c0392b', 'Kegel n = 5 (Haupt)'), args.flach: ('s', '#555555', 'flach n = 6')}
    for ip, pn in enumerate([x for x in args.proben.split(',') if x]):
        stil[pn] = (('x', '+', '^')[ip % 3], ('#2471a3', '#8e44ad', '#117a65')[ip % 3], 'Kegel, Probe %s' % pn)
    for nm, (mk, c, lab) in stil.items():
        if nm not in A['laeufe']:
            continue
        P = A['laeufe'][nm]['paare']
        bb = [b for b in B_LISTE if P['%g' % b].get('auswertbar')]
        ww = [P['%g' % b]['winkel_aus_grad'] for b in bb]
        axs[0].plot(bb, ww, mk, color=c, ms=8, label=lab, mfc='none' if mk == 's' else c)
        eps = [P['%g' % b]['ablenkung_zur_spitze_plus'] + P['%g' % b]['ablenkung_zur_spitze_minus'] for b in bb]
        axs[1].plot(bb, eps, mk + '-', color=c, ms=7, label=lab, lw=0.8)
        F = A['laeufe'][nm]['felder']
        for sg in (1.0, -1.0):
            bv = [b for b in B_LISTE if F.get('%+g' % (sg * b), {}).get('v_aus_durch_v_ein_minus_1') is not None]
            rv = [100 * F['%+g' % (sg * b)]['v_aus_durch_v_ein_minus_1'] for b in bv]
            axs[2].plot(bv, rv, mk, color=c, ms=7, label=lab + (' (+b)' if sg > 0 else ' (-b)'),
                        mfc=c if sg > 0 else 'none')
    axs[0].axhspan(58, 62, color='#f5cba7', alpha=0.5, label='D1: 60 +- 2 Grad')
    axs[0].axhline(63, color='#c0392b', ls=':', lw=0.8, label='D2: 63 Grad (b = 10)')
    axs[0].axhline(0, color='k', lw=0.4)
    axs[0].set_xlabel('Stossparameter b')
    axs[0].set_ylabel('Winkel zwischen den Auslaufrichtungen +b, -b [Grad]')
    axs[0].set_title('Winkel gegen b (Auslaufkarte)')
    axs[0].legend(fontsize=7)
    axs[1].axhline(0, color='k', lw=0.4)
    axs[1].set_xlabel('Stossparameter b')
    axs[1].set_ylabel('Zusatzablenkung zur Spitze (Summe +b und -b) [Grad]')
    axs[1].set_title('Winkel minus Kartenwinkel der Einlaeufe')
    axs[1].legend(fontsize=7)
    axs[2].axhspan(-2, 2, color='#d5f5e3', alpha=0.6, label='D3: +-2 %')
    axs[2].axhspan(-1, 1, color='#abebc6', alpha=0.6, label='D0: +-1 %')
    axs[2].set_xlabel('Stossparameter |b|')
    axs[2].set_ylabel('v_aus/v_ein - 1 [%]')
    axs[2].set_title('Endschnelle gegen Startschnelle')
    axs[2].legend(fontsize=6)
    fig.tight_layout()
    fig.savefig(os.path.join(args.ordner, 'winkel.png'), dpi=120)
    print('geschrieben winkel.png', flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='befehl', required=True)
    a = sub.add_parser('lauf')
    a.add_argument('--name', required=True)
    a.add_argument('--n', type=int, required=True, choices=[5, 6])
    a.add_argument('--h', type=float, required=True)
    a.add_argument('--R', type=float, default=85.0)
    a.add_argument('--rs', type=float, default=70.0)
    a.add_argument('--gmax', type=float, default=1.0)
    a.add_argument('--Q', type=float, default=200.0)
    a.add_argument('--v', type=float, default=0.05)
    a.add_argument('--X0', type=float, default=42.0)
    a.add_argument('--b', required=True, help='Stossparameter, Komma-getrennt, z. B. 10,-10,20,-20')
    a.add_argument('--dt', type=float, required=True)
    a.add_argument('--T', type=float, required=True)
    a.add_argument('--diag', type=float, default=2.0)
    a.add_argument('--wand', type=float, default=520.0)
    a.add_argument('--zustand', default=None)
    a.add_argument('--fortsetzen', default=None)
    a.add_argument('--aus', required=True)
    a = sub.add_parser('auswertung')
    a.add_argument('--ordner', required=True)
    a.add_argument('--kegel', default='li-K')
    a.add_argument('--flach', default='li-F')
    a.add_argument('--proben', default='li-K-dt')
    a.add_argument('--b-liste', dest='b_liste', default='10,20,30,40')
    a = sub.add_parser('bild')
    a.add_argument('--ordner', required=True)
    a.add_argument('--laeufe', default='li-K,li-F')
    a.add_argument('--kegel', default='li-K')
    a.add_argument('--flach', default='li-F')
    a.add_argument('--proben', default='li-K-dt')
    a.add_argument('--b-liste', dest='b_liste', default='10,20,30,40')
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
