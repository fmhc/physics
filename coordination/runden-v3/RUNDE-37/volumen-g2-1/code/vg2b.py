#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VOLUMEN-G2-1 (fmhc-physics, RUNDE-37, schlanke Karte), Rechen-Agent fuer die Leitung claude-primary.

Frage: Haelt eine Volumenbedingung V(l) = V0 die Umklapp-Dynamik stabil, wenn sie im laufenden Integrator mitgefuehrt wird?

Modell (VORAB.md):
  H(x, y) = 1/2 y^T A_r y + 1/2 x^T B_r x, l = l0 (1 + S x); A_r, B_r aus nn.NetzG (M_eff und B am gedehnten Netz).
  Bedingung g(x) = V(x) - V0 = 0, V = Summe der Tetraedervolumen (Cayley-Menger, exakt).
  Integrator: implizite Mitte mit Lagrange-Multiplikator (x1 - x0 = dt A y_m, y1 - y0 = -dt (B x_m + lam G(x_m)),
  g(x1) = 0). Schrittweite: omega_s dt <= h nach jedem Operatorwechsel (Unterschritte).
  Nachfuehrung: Operatoren am gedehnten Netz bei jedem Zug (nn-G1) und je Periode (Stufe P); Spruenge getrennt gebucht.
  Zuege wie nn.lauf Arm b, Abbildung td.abbilden (Lesart P); mit Bedingung danach Projektion von x und y.
Importiert unveraendert: nn, td, tg, tu aus NETZ-NICHTLINEAR-1/code.
"""
import argparse, json, os, sys, time, platform, resource
import numpy as np
import scipy
import scipy.linalg as sla

NNCODE = '/home/fmh/fmhc-physics-remote/netz-nichtlinear-1/code'
sys.path.insert(0, NNCODE)
import nn  # noqa: E402
import td  # noqa: E402
import tg  # noqa: E402
import tu  # noqa: E402

PA = np.array([(i, j) for (i, j, _, _) in tg.PAARE])
TOLV = 1e-14          # |g| / V0 im Newton
TOLN = 1e-10          # negative Eigenwerte relativ (wie AG2)


# ------------------------------------------------------------------------------------------------ Volumen
def cm(l6):
    T = len(l6)
    M = np.ones((T, 5, 5))
    M[:, 0, 0] = 0.0
    for i in range(4):
        M[:, i + 1, i + 1] = 0.0
    sq = l6 ** 2
    M[:, PA[:, 0] + 1, PA[:, 1] + 1] = sq
    M[:, PA[:, 1] + 1, PA[:, 0] + 1] = sq
    return M


class Vol:
    def __init__(self, N):
        self.eidx = N.mod['eidx']
        self.l0 = N.l0
        self.S = N.S
        self.E = N.E

    def wert(self, x):
        l6 = (self.l0 * (1.0 + self.S @ x))[self.eidx]
        d = np.linalg.det(cm(l6))
        return float(np.sqrt(np.clip(d / 288.0, 0.0, None)).sum()), float(d.min())

    def grad(self, x):
        """G = dV/dx (m), c = dV/da (E), V."""
        l6 = (self.l0 * (1.0 + self.S @ x))[self.eidx]
        M = cm(l6)
        d = np.linalg.det(M)
        Vt = np.sqrt(np.clip(d / 288.0, 0.0, None))
        Mi = np.linalg.inv(M)
        dV6 = 2.0 * Vt[:, None] * l6 * Mi[:, PA[:, 0] + 1, PA[:, 1] + 1]
        dVl = np.bincount(self.eidx.ravel(), dV6.ravel(), self.E)
        c = dVl * self.l0
        return self.S.T @ c, c, float(Vt.sum())


class Zuf:
    """Gegenprobe (--bed 2): zufaellige lineare Einzelbedingung r . a = 0 an den Kanten, r fest je Kantenschluessel
    (pseudozufaellig aus dem Schluessel, damit sie ueber Zuege hinweg dieselbe Kante meint). Gleiche Schnittstelle wie Vol;
    wert gibt V0 + r . a zurueck, damit g = wert - V0 = r . a ist."""
    V0 = None

    def __init__(self, N):
        self.S = N.S
        self.r = ((N.keys.astype(np.float64) * 0.6180339887498949) % 1.0) * 2.0 - 1.0
        self.G = self.S.T @ self.r

    def wert(self, x):
        return float(Zuf.V0 + self.r @ (self.S @ x)), 1.0

    def grad(self, x):
        return self.G, self.r, float(Zuf.V0)


MK = Vol


# ------------------------------------------------------------------------------------------------ Operatoren
def neu_stat():
    return {'Fn2': 0.0, 'Fc2': 0.0, 'FnA2': 0.0, 'FcA2': 0.0, 'Fn_max': 0.0, 'Fc_max': 0.0, 'lam_max': 0.0,
            'nicht_konv': 0}


def omega_s(N):
    e = N.eig or N.spektrum()
    return float(np.sqrt(max(abs(e['w2_max']), abs(e['w2_min'])) + e['w2im_max']))


class Schritt:
    """Implizite Mitte fuer feste Operatoren, optional mit Bedingung."""

    def __init__(self, N, dt):
        self.N = N
        self.dt = dt
        self.A = N.Ar
        self.B = np.asarray(N.Br)
        m = self.A.shape[0]
        self.lu = sla.lu_factor(np.eye(m) + (dt * dt / 4.0) * (self.A @ self.B))

    def __call__(self, x, y, vol=None, V0=None, stat=None):
        dt, A, B = self.dt, self.A, self.B
        xm0 = sla.lu_solve(self.lu, x + 0.5 * dt * (A @ y))
        if vol is None:
            xm = xm0
            ym = y - 0.5 * dt * (B @ xm)
            if stat is not None:
                stat['Fn2'] += float((B @ xm) @ (B @ xm))
                stat['Fn_max'] = max(stat['Fn_max'], float(np.linalg.norm(B @ xm)))
            return 2 * xm - x, 2 * ym - y, 0.0
        g = vol.grad(x)[0]
        lam = 0.0
        ok = False
        for outer in range(12):
            u = -(dt * dt / 4.0) * sla.lu_solve(self.lu, A @ g)
            du = 2.0 * float(g @ u)
            if du == 0.0:
                raise RuntimeError('Newton: G u = 0')
            for k in range(12):
                x1 = 2.0 * (xm0 + lam * u) - x
                gv = vol.wert(x1)[0] - V0
                if abs(gv) <= TOLV * V0:
                    break
                lam -= gv / du
            xm = xm0 + lam * u
            gneu = vol.grad(xm)[0]
            if np.linalg.norm(gneu - g) <= 1e-13 * np.linalg.norm(g) and abs(gv) <= TOLV * V0:
                g = gneu
                ok = True
                break
            g = gneu
        if not ok:
            # letzter Stand: u mit dem aktuellen g neu, Bedingung exakt erzwingen
            u = -(dt * dt / 4.0) * sla.lu_solve(self.lu, A @ g)
            du = 2.0 * float(g @ u)
            for k in range(12):
                x1 = 2.0 * (xm0 + lam * u) - x
                gv = vol.wert(x1)[0] - V0
                if abs(gv) <= TOLV * V0:
                    break
                lam -= gv / du
            xm = xm0 + lam * u
            if stat is not None:
                stat['nicht_konv'] += 1
        ym = y - 0.5 * dt * (B @ xm + lam * g)
        if stat is not None:
            Fn = B @ xm
            stat['Fn2'] += float(Fn @ Fn)
            stat['Fc2'] += float(lam * lam * (g @ g))
            stat['FnA2'] += abs(float(Fn @ (A @ Fn)))
            stat['FcA2'] += abs(float(lam * lam * (g @ (A @ g))))
            stat['Fn_max'] = max(stat['Fn_max'], float(np.linalg.norm(Fn)))
            stat['Fc_max'] = max(stat['Fc_max'], float(abs(lam) * np.linalg.norm(g)))
            stat['lam_max'] = max(stat['lam_max'], abs(lam))
        return 2 * xm - x, 2 * ym - y, lam


def proj_x(N, vol, x, V0):
    A = N.Ar
    for k in range(30):
        G = vol.grad(x)[0]
        gv = vol.wert(x)[0] - V0
        if abs(gv) <= TOLV * V0:
            return x, k
        d = A @ G
        den = float(G @ d)
        if abs(den) < 1e-12 * np.linalg.norm(G) * np.linalg.norm(d):
            d, den = G, float(G @ G)
        x = x - (gv / den) * d
    return x, -1


def proj_y(N, vol, x, y):
    G = vol.grad(x)[0]
    AG = N.Ar @ G
    den = float(G @ AG)
    mu = float(G @ (N.Ar @ y)) / den
    return y - mu * G, mu


def neg(ev, s=None):
    s = np.abs(ev).max() if s is None else s
    return int((ev < -TOLN * s).sum())


def analyse(N, vol, x):
    """Spektrum mit und ohne Bedingung am Zustand x (wie AG2, aber G an x)."""
    t0 = time.time()
    G, c, V = vol.grad(x)
    M = 0.5 * (N.M + N.M.T)
    Zc = sla.null_space(c[None, :])
    R = Zc.T @ M @ Zc
    r = {'M_n_neg': N.meff.get('M_n_neg'), 'M_neg_bed': neg(np.linalg.eigvalsh(0.5 * (R + R.T))),
         'A_pd': bool(N.A_pd), 'n_A_neg': int(N.n_A_neg), 'n_wachsend': (N.eig or {}).get('n_wachsend'),
         'w2_wachsend': (N.eig or {}).get('w2_wachsend'), 'omega_s': omega_s(N)}
    Ainv = np.linalg.inv(N.Ar)
    Ainv = 0.5 * (Ainv + Ainv.T)
    Zx = sla.null_space(G[None, :])
    Kr = Zx.T @ Ainv @ Zx
    Kr = 0.5 * (Kr + Kr.T)
    Vr = Zx.T @ np.asarray(N.Br) @ Zx
    Vr = 0.5 * (Vr + Vr.T)
    r['kin_neg_ohne'] = neg(np.linalg.eigvalsh(Ainv))
    r['kin_neg_bed'] = neg(np.linalg.eigvalsh(Kr))
    w = sla.eigvals(Vr, Kr)
    s = float(np.abs(w).max())
    tau = td.TAU_REL * s
    wa = (w.real < -tau) | (np.abs(w.imag) > tau)
    r['wachsend_bed'] = int(wa.sum())
    r['w2_wachsend_bed'] = [complex(v).real for v in w[wa][:6]]
    r['omega_max_bed'] = float(np.sqrt(np.abs(w).max()))
    # Kosinus TT-Richtung / Bedingungsnormale wird beim Start gesetzt
    r['t_s'] = time.time() - t0
    return r


def energie(N, x, y):
    return N.energie(x, y)


# ------------------------------------------------------------------------------------------------ Lauf
def lauf(a):
    T0w = time.time()
    LV, pos, G0, O0, ninfo = td.netz_bauen(a.netz)
    rez = 2 * np.pi * np.linalg.inv(LV).T
    k1 = rez[0]
    hp, hx = td.polarisation(k1)
    nn.B_GD['an'] = True
    N0 = nn.NetzG(LV, pos, G0, O0, k1, hp, hx, rolle='start')
    if not N0.A_pd:
        raise RuntimeError('A_red nicht positiv definit am Start')
    mode, xm, w2, Qm = td.tt_mode(N0, a.A, k1)
    om = mode['omega']
    Tper = 2 * np.pi / om
    ws0 = omega_s(N0)
    NT = int(np.ceil(Tper * ws0 / a.h))
    dt0 = Tper / NT
    nges = NT * a.perioden
    ds = max(1, NT // a.proben)
    V0 = float(abs(np.linalg.det(LV)))
    Zuf.V0 = V0
    vol0 = MK(N0)
    Vx0, dmin0 = vol0.wert(np.zeros(N0.m))
    xref = float(np.linalg.norm(xm))
    # Startzustand, projiziert (beide Arme gleich)
    y_roh = sla.lu_solve(N0.lu, om * xm)
    H_roh = N0.energie(np.zeros(N0.m), y_roh)[0]
    y_s, mu0 = proj_y(N0, vol0, np.zeros(N0.m), y_roh)
    H0 = N0.energie(np.zeros(N0.m), y_s)[0]
    Gs = vol0.grad(np.zeros(N0.m))[0]
    vTT = N0.Ar @ y_roh
    cos_tt = float(abs(Gs @ vTT) / (np.linalg.norm(Gs) * np.linalg.norm(vTT)))
    start = {'V0_detLV': V0, 'V_x0': Vx0, 'V_rel_fehler': (Vx0 - V0) / V0, 'cm_det_min': dmin0, 'H_roh': H_roh,
             'H0': H0, 'H0_proj_rel': (H0 - H_roh) / H_roh, 'cos_TT_normale': cos_tt, 'omega_s0': ws0,
             'omega_TT': om, 'T': Tper, 'NT': NT, 'dt0': dt0, 'm': int(N0.m), 'E': int(N0.E),
             'analyse': analyse(N0, vol0, np.zeros(N0.m))}
    bed = bool(a.bed)
    zfile = a.out + '.zustand.npz'
    if os.path.exists(zfile):
        z = np.load(zfile, allow_pickle=False)
        meta = json.load(open(a.out + '.zustand.json'))
        G, O, f = z['G'], z['O'], z['f']
        x, y, n = z['x'], z['y'], int(z['n'])
        if bool(z['ist_start']):
            N = N0
        elif a.opgd and not bool(z['f_hg']):
            N = nn.NetzG(LV, pos, G, O, k1, hp, hx, f=f, rolle='neustart')
        else:
            N = nn.NetzG(LV, pos, G, O, k1, hp, hx, rolle='neustart_hg')
        st = meta['st']
        abschnitt = meta['abschnitt'] + 1
    else:
        N = N0
        x = np.zeros(N0.m)
        y = y_s.copy()
        n = 0
        st = {'proben': [], 'ereignisse': [], 'nachf': [], 'gesperrt': [], 'sum_zug': 0.0, 'sum_proj': 0.0,
              'sum_upd': 0.0, 'n_zuege': 0, 'nicht_konv': 0, 'perioden': [], 'V_max_rel': 0.0, 'dH_max': 0.0}
        abschnitt = 0
    gesperrt = set(tuple(g) for g in st['gesperrt'])
    vol = MK(N)
    abbruch = None
    cache = {}
    stat = neu_stat()
    pstat = dict(stat)

    def integ(Ncur, d):
        key = (id(Ncur), d)
        if key not in cache:
            if len(cache) > 6:
                cache.clear()
            cache[key] = Schritt(Ncur, d)
        return cache[key]

    def step(Ncur, volc, x, y, d, stt=None):
        return integ(Ncur, d)(x, y, volc if bed else None, V0, stt)

    def probe(t):
        H, Vp, K = N.energie(x, y)
        mu = N.mu_alle(x)
        Vx = vol.wert(x)[0]
        vr = (Vx - V0) / V0
        st['V_max_rel'] = max(st['V_max_rel'], abs(vr))
        dH = (H - H0) / H0
        st['dH_max'] = max(st['dH_max'], abs(dH))
        st['proben'].append([t, H, Vp, K, dH, vr, st['n_zuege'], int((mu < 0).sum()), float(mu.min()),
                             st['sum_zug'], st['sum_proj'], st['sum_upd'], pstat['Fn_max'], pstat['Fc_max'],
                             np.sqrt(pstat['Fc2'] / pstat['Fn2']) if pstat['Fn2'] > 0 else None, pstat['lam_max'], np.sqrt(pstat['FcA2'] / pstat['FnA2']) if pstat['FnA2'] > 0 else None])
        for k_ in ('Fn2', 'Fc2', 'FnA2', 'FcA2', 'Fn_max', 'Fc_max', 'lam_max'):
            pstat[k_] = 0.0

    def stt_add(d):
        for k_ in ('Fn2', 'Fc2', 'FnA2', 'FcA2'):
            stat[k_] += d[k_]
            pstat[k_] += d[k_]
        for k_ in ('Fn_max', 'Fc_max', 'lam_max'):
            stat[k_] = max(stat[k_], d[k_])
            pstat[k_] = max(pstat[k_], d[k_])
        stat['nicht_konv'] += d['nicht_konv']

    if n == 0 and not st['proben']:
        probe(0.0)
    while n < nges:
        if time.time() - T0w > a.budget:
            break
        t_cur = n * dt0
        rem = dt0
        while rem > 0:
            nsub = max(1, int(np.ceil(dt0 * omega_s(N) / a.h)))
            dts = dt0 / nsub
            d = dts if (rem > dts * (1 + 1e-9) or abs(rem - dts) <= 1e-9 * dts) else rem
            sd = neu_stat()
            x1, y1, lam = step(N, vol, x, y, d, sd)
            ev = None
            if a.arm == 'b':
                mu1 = N.mu_alle(x1)
                kand = np.nonzero(mu1 < 0)[0]
                kand = [j for j in kand if tuple(N.fkeys[N.fl['t1'][j] * 4 + N.fl['i1'][j]].tolist()) not in gesperrt]
                if kand:
                    v1 = N.Ar @ y
                    v2 = N.Ar @ (N.Br @ x)
                    best = None
                    for j in kand:
                        lo, hi = 0.0, d
                        if N.mu_eine(j, x) < 0:
                            continue
                        for _ in range(td.BISEKT):
                            mid = 0.5 * (lo + hi)
                            if N.mu_eine(j, x + mid * v1 - 0.5 * mid * mid * v2) < 0:
                                hi = mid
                            else:
                                lo = mid
                        if best is None or hi < best[1]:
                            best = (j, hi)
                    ev = best
            if ev is None:
                stt_add(sd)
                x, y = x1, y1
                rem = 0.0 if d >= rem * (1 - 1e-9) else rem - d
                continue
            j, tau = ev
            sd = neu_stat()
            xe, ye, _ = Schritt(N, tau)(x, y, vol if bed else None, V0, sd)
            stt_add(sd)
            te = t_cur + (dt0 - rem) + tau
            H1 = N.energie(xe, ye)[0]
            rec = {'t': te, 'n': n, 'periode': te / Tper}
            L9 = N.l9_0[j] * (1.0 + N.S[N.f9[j]] @ xe)
            vv = td.vol_bipyr(L9)
            if np.all(vv > 0) or np.all(vv < 0):
                typ, r = 23, None
            else:
                typ, r = 32, tu.ungerade(vv)
            mu_hg = float(td.mu_bipyr(N.l9_0[j][None, :])[0])
            rec.update({'typ': typ, 'mu_hg': mu_hg, 'ausnahme_hg': bool(typ == 23 and mu_hg > 0)})
            aus = None if (typ == 32 and r is None) else td.zug_ausfuehren(N, j, typ, r, td.VMIN_B * N0.vbar)
            if aus is None:
                rec['ausgefuehrt'] = False
                gesperrt.add(tuple(N.fkeys[N.fl['t1'][j] * 4 + N.fl['i1'][j]].tolist()))
                st['ereignisse'].append(rec)
                x, y = xe, ye
                rem -= tau
                continue
            Gn, On, besch = aus
            a_alt = N.S @ xe
            f_alt = 1.0 + a_alt
            l_extra = {}
            if besch['kante_neu'] is not None:
                i9, ok9 = N.idx_von_keys(besch['k9'])
                L9g = N.l0[i9] * (1.0 + a_alt[i9])
                l_extra[besch['kante_neu']] = float(td.l_de_flach(L9g[None, :])[0])

            def f_neu_fn(N2, N=N, f_alt=f_alt, besch=besch, l_extra=l_extra):
                idx, ok = N2.idx_von_keys(N.keys)
                fn = np.ones(N2.E)
                fn[idx[ok]] = f_alt[ok]
                if besch['kante_neu'] is not None:
                    inew, okn = N2.idx_von_keys(np.array([besch['kante_neu']]))
                    fn[inew[0]] = l_extra[besch['kante_neu']] / N2.l0[inew[0]]
                return fn
            try:
                if a.opgd:
                    N2 = nn.NetzG(LV, pos, Gn, On, k1, hp, hx, f_fn=f_neu_fn, rolle='neu_gd')
                else:
                    N2 = nn.NetzG(LV, pos, Gn, On, k1, hp, hx, rolle='neu_hg')
            except (RuntimeError, AssertionError, np.linalg.LinAlgError) as exc:
                rec['ausgefuehrt'] = False
                rec['fehler'] = repr(exc)[:300]
                st['ereignisse'].append(rec)
                abbruch = {'t': te, 'n': n, 'grund': 'Operator nach Zug: ' + repr(exc)[:300]}
                x, y = xe, ye
                break
            x2, y2, minfo = td.abbilden(N, N2, xe, ye, besch, 'P')
            H2 = N2.energie(x2, y2)[0]
            vol2 = MK(N2)
            V_nach = vol2.wert(x2)[0]
            rec.update({'ausgefuehrt': True, 'dH_zug_rel': (H2 - H1) / H0, 'V_vor_rel': (vol.wert(xe)[0] - V0) / V0,
                        'V_nach_rel': (V_nach - V0) / V0, 'V_hg_neu_rel': (vol2.wert(np.zeros(N2.m))[0] - V0) / V0})
            st['sum_zug'] += (H2 - H1) / H0
            if bed:
                x3, kx = proj_x(N2, vol2, x2, V0)
                y3, mu = proj_y(N2, vol2, x3, y2)
                H3 = N2.energie(x3, y3)[0]
                rec.update({'dH_proj_rel': (H3 - H2) / H0, 'proj_newton': kx, 'proj_dx_rel':
                            float(np.linalg.norm(x3 - x2) / max(np.linalg.norm(x2), 1e-300)), 'proj_mu': mu})
                st['sum_proj'] += (H3 - H2) / H0
                x2, y2 = x3, y3
            rec['analyse'] = analyse(N2, vol2, x2)
            rec['nach'] = nn.kurz(N2)
            st['ereignisse'].append(rec)
            st['n_zuege'] += 1
            N, vol = N2, vol2
            cache.clear()
            x, y = x2, y2
            mu_n = N.mu_alle(x)
            for jj in np.nonzero(mu_n < 0)[0]:
                gesperrt.add(tuple(N.fkeys[N.fl['t1'][jj] * 4 + N.fl['i1'][jj]].tolist()))
            rem -= tau
            print('zug %d t/T=%.4f typ=%d ausn_hg=%s dH_zug=%.3e M_n_neg=%s Mbed=%s A_pd=%s wachs=%s/%s' % (
                st['n_zuege'], te / Tper, typ, rec['ausnahme_hg'], rec['dH_zug_rel'], rec['analyse']['M_n_neg'],
                rec['analyse']['M_neg_bed'], N.A_pd, rec['analyse']['n_wachsend'], rec['analyse']['wachsend_bed']),
                flush=True)
            if time.time() - T0w > a.budget + 100:
                abbruch = {'t': te, 'n': n, 'grund': 'Zeitgrenze innerhalb eines Schritts'}
                break
        if abbruch is not None:
            probe(n * dt0)
            break
        n += 1
        if a.arm == 'b' and gesperrt:
            mu_n = N.mu_alle(x)
            fk = N.fkeys[N.fl['t1'] * 4 + N.fl['i1']]
            frei = set(tuple(r_) for r_ in fk[mu_n > 0].tolist())
            gesperrt -= frei
        Hn = N.energie(x, y)[0]
        if not np.all(np.isfinite(x)) or float(np.linalg.norm(x)) > 1e6 * xref:
            abbruch = {'t': n * dt0, 'n': n, 'grund': 'Zustand > 1e6 x Anfangsmode oder nicht endlich'}
        elif abs(Hn - H0) > a.hmax * abs(H0):
            abbruch = {'t': n * dt0, 'n': n, 'grund': '|H - H0| > %g H0 (Kaskade)' % a.hmax}
        if abbruch is not None:
            probe(n * dt0)
            break
        if n % ds == 0 or n == nges:
            probe(n * dt0)
        if n % NT == 0:
            pr = st['proben'][-1]
            st['perioden'].append({'periode': n // NT, 'dH_rel': pr[4], 'V_rel': pr[5], 'n_zuege': st['n_zuege'],
                                   'sum_zug': st['sum_zug'], 'sum_proj': st['sum_proj'], 'sum_upd': st['sum_upd'],
                                   'Fc_Fn_rms_gesamt': np.sqrt(stat['Fc2'] / stat['Fn2']) if stat['Fn2'] > 0 else None,
                                   'Fc_Fn_rms_A_gesamt': np.sqrt(stat['FcA2'] / stat['FnA2']) if stat['FnA2'] > 0 else None,
                                   'Fc_max': stat['Fc_max'], 'Fn_max': stat['Fn_max'], 'lam_max': stat['lam_max']})
            print('periode %d dH=%.3e V=%.3e zuege=%d upd=%.3e Fc/Fn=%s' % (
                n // NT, pr[4], pr[5], st['n_zuege'], st['sum_upd'], st['perioden'][-1]['Fc_Fn_rms_gesamt']),
                flush=True)
            if a.stufe == 'P' and a.opgd and n < nges:
                f_now = 1.0 + N.S @ x
                H1 = N.energie(x, y)[0]
                rec = {'periode': n // NT}
                try:
                    N2 = nn.NetzG(LV, pos, N.G, N.O, k1, hp, hx, f=f_now, rolle='nachf')
                except (RuntimeError, AssertionError, np.linalg.LinAlgError) as exc:
                    rec['fehler'] = repr(exc)[:300]
                    st['nachf'].append(rec)
                    abbruch = {'t': n * dt0, 'n': n, 'grund': 'Nachfuehrung: ' + repr(exc)[:300]}
                    break
                dS = float(np.abs(N2.S - N.S).max())
                rec['S_gleich'] = dS
                if dS > 1e-10:
                    x = N2.S.T @ (N.S @ x)
                    y = N2.S.T @ (N.S @ y)
                H2 = N2.energie(x, y)[0]
                rec['dH_upd_rel'] = (H2 - H1) / H0
                rec['dAr_rel'] = float(np.linalg.norm(N2.Ar - N.Ar) / np.linalg.norm(N.Ar))
                rec['dBr_rel'] = float(np.linalg.norm(N2.Br - N.Br) / np.linalg.norm(N.Br))
                st['sum_upd'] += (H2 - H1) / H0
                vol = MK(N2)
                if bed:
                    y3, mu = proj_y(N2, vol, x, y)
                    H3 = N2.energie(x, y3)[0]
                    rec['dH_proj_rel'] = (H3 - H2) / H0
                    st['sum_proj'] += (H3 - H2) / H0
                    y = y3
                rec['analyse'] = analyse(N2, vol, x)
                st['nachf'].append(rec)
                N = N2
                cache.clear()
    fertig = (n >= nges) or (abbruch is not None)
    st['gesperrt'] = [list(g) for g in gesperrt]
    st['nicht_konv'] += stat['nicht_konv']
    if not fertig:
        with open(a.out + '.zustand.json.tmp', 'w') as fh:
            json.dump({'st': st, 'abschnitt': abschnitt}, fh, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
        np.savez(a.out + '.zustand.tmp.npz', x=x, y=y, n=n, G=N.G, O=N.O, f=N.f, ist_start=bool(N is N0),
                 f_hg=bool(not N.meff.get('gedehnt', False)))
        os.replace(a.out + '.zustand.json.tmp', a.out + '.zustand.json')
        os.replace(a.out + '.zustand.tmp.npz', zfile)
    else:
        for fp in (zfile, a.out + '.zustand.json'):
            if os.path.exists(fp):
                os.remove(fp)
    H_end = N.energie(x, y)[0]
    return {'netz': a.netz, 'arm': a.arm, 'bed': bed, 'stufe': a.stufe, 'opgd': bool(a.opgd), 'h': a.h, 'A': a.A,
            'perioden_soll': a.perioden, 'fertig': fertig, 'abschnitt': abschnitt, 'n': n, 'nges': nges,
            'abbruch': abbruch, 'start': start, 'dH_end': (H_end - H0) / H0,
            'drift_ohne_spruenge': (H_end - H0) / H0 - st['sum_zug'] - st['sum_proj'] - st['sum_upd'],
            'stat_abschnitt': stat, 'N_ende': nn.kurz(N),
            'proben_spalten': ['t', 'H', 'V', 'K', 'dH_rel', 'Vol_rel', 'n_zuege', 'n_mu_neg', 'mu_min', 'sum_zug',
                               'sum_proj', 'sum_upd', 'Fn_max', 'Fc_max', 'Fc_Fn_rms', 'lam_max', 'Fc_Fn_rms_A'],
            'st': st, 'wand_s': time.time() - T0w}


# ------------------------------------------------------------------------------------------------ Rauchtest
def rauch(a):
    out = {}
    LV, pos, G0, O0, ninfo = td.netz_bauen(a.netz)
    rez = 2 * np.pi * np.linalg.inv(LV).T
    k1 = rez[0]
    hp, hx = td.polarisation(k1)
    t = time.time()
    N0 = nn.NetzG(LV, pos, G0, O0, k1, hp, hx, rolle='start')
    out['t_bau_s'] = time.time() - t
    vol = Vol(N0)
    V0 = float(abs(np.linalg.det(LV)))
    Zuf.V0 = V0
    m = N0.m
    Vx, dmin = vol.wert(np.zeros(m))
    out['V0'] = V0
    out['V_rel'] = (Vx - V0) / V0
    rng = np.random.default_rng(7)
    x = 1e-3 * rng.standard_normal(m) / np.sqrt(m) * 10
    G, c, V = vol.grad(x)
    fd = []
    for k in range(4):
        d = rng.standard_normal(m)
        eps = 1e-6
        num = (vol.wert(x + eps * d)[0] - vol.wert(x - eps * d)[0]) / (2 * eps)
        fd.append([float(G @ d), num, float(abs(G @ d - num) / abs(num))])
    out['grad_fd'] = fd
    mode, xm, w2, Qm = td.tt_mode(N0, a.A, k1)
    om = mode['omega']
    y = sla.lu_solve(N0.lu, om * xm)
    ys, mu = proj_y(N0, vol, np.zeros(m), y)
    out['proj_mu'] = mu
    out['omega_s'] = omega_s(N0)
    Tper = 2 * np.pi / om
    dt = a.h / out['omega_s']
    for bed in (0, 1):
        stat = neu_stat()
        S = Schritt(N0, dt)
        xx, yy = np.zeros(m), ys.copy()
        H0 = N0.energie(xx, yy)[0]
        t = time.time()
        nst = 200
        for k in range(nst):
            xx, yy, lam = S(xx, yy, vol if bed else None, V0, stat)
        out['bed%d' % bed] = {'dH_rel': (N0.energie(xx, yy)[0] - H0) / H0, 'V_rel': (vol.wert(xx)[0] - V0) / V0,
                              'ms_je_schritt': 1e3 * (time.time() - t) / nst, 'stat': stat,
                              'G_A_y': float(vol.grad(xx)[0] @ (N0.Ar @ yy))}
    out['analyse'] = analyse(N0, vol, np.zeros(m))
    out['T'] = Tper
    out['NT_h'] = int(np.ceil(Tper * out['omega_s'] / a.h))
    # Nachfuehrungsbau: S gleich?
    aa = N0.S @ xm
    t = time.time()
    N1 = nn.NetzG(LV, pos, G0, O0, k1, hp, hx, f=1.0 + aa, rolle='dehn')
    out['nachf_S_diff'] = float(np.abs(N1.S - N0.S).max())
    out['nachf_t_s'] = time.time() - t
    out['nachf_dAr_rel'] = float(np.linalg.norm(N1.Ar - N0.Ar) / np.linalg.norm(N0.Ar))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['lauf', 'rauch'])
    ap.add_argument('--netz', default='glas-N128-s2')
    ap.add_argument('--A', type=float, default=1e-3)
    ap.add_argument('--arm', default='b', choices=['a', 'b'])
    ap.add_argument('--bed', type=int, default=1)
    ap.add_argument('--stufe', default='P', choices=['F', 'P'])
    ap.add_argument('--opgd', type=int, default=1, help='1: Operatoren am gedehnten Netz (G), 0: Hintergrund (H)')
    ap.add_argument('--h', type=float, default=1.0)
    ap.add_argument('--perioden', type=int, default=10)
    ap.add_argument('--proben', type=int, default=20)
    ap.add_argument('--budget', type=float, default=480.0)
    ap.add_argument('--hmax', type=float, default=100.0)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    global MK
    if a.bed == 2:
        MK = Zuf
    t0 = time.time()
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(),
            'host': platform.node(), 'argv': sys.argv, 'skript_sha256': td.sha(os.path.abspath(__file__)),
            'module_sha256': {mm.__name__: td.sha(os.path.abspath(mm.__file__)) for mm in (nn, td, tg, tu)},
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    erg = rauch(a) if a.modus == 'rauch' else lauf(a)
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    tg.schreibe(a.out, res)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], 'fertig=%s' % erg.get('fertig'), flush=True)


if __name__ == '__main__':
    main()
