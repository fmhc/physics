#!/usr/bin/env python3
"""stille.py - Runde 16 LOG-NACHBAU, eigener Code des Code-Agenten (frischer Kontext, 2026-10-02).

Stille Stellen (gebundene Zustaende im Kontinuum) der radialen Atmungsmode l = 0 von Q-Baellen.
Methode: HERLEITUNG.md, Ablauf: PLAN.md (Kartenordner).

W(w2, rho) = G_a + i G_b, G_x = Wronski[Y_x, Z_d] = -2 kappa gamma_x (wachsender Anteil des geschlossenen Kanals).
Geschlossene Bedingung: G_b = 0. Kenngroesse s = G_a an deren Nullstellen.

Unterbefehle:
  rauch                                 kleiner Rauchtest (lokal, <= 120 s)
  scan  <modell> <stufe> <aus> <w2 ...> Zeilen rechnen, je Zeile eine JSON-Datei
  kand  <modell> <stufe> <aus> <zeilendateien ...>   Kandidaten, Lokalisierung, Umlauf
  k2    <aus> <w2 ...>                  Profile auf zwei Stufen, Q und E
"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
import json
import time
import math
import numpy as np

STUFEN = {1: 0.01, 2: 0.005}       # Profilschritt hp; linearer Schritt h = 2 hp
RAND = 2e-3                         # Abstand der rho-Abtastung von den Fenstergrenzen 1 -+ w
NRHO = 401                          # rho-Punkte je Zeile
HALB = 1e-3                         # Halbbreite des Umlauf-Rechtecks (w2 und rho)
NKANTE = 16                         # Anfangspunkte je Rechteckkante
SPRUNG = 0.4                        # aufgeloest: groesster Phasensprung < 0,4 rad
VERF_RUNDEN = 6                     # Halbierungsrunden fuer den Umlauf


# ---------------------------------------------------------------- Modelle
def modell(name):
    if name == 'kontrolle':
        U = lambda S: S - S * S + 0.5 * S ** 3
        dU = lambda S: 1.0 - 2.0 * S + 1.5 * S * S
        d2U = lambda S: -2.0 + 3.0 * S
    elif name == 'log':
        U = lambda S: np.log1p(S)
        dU = lambda S: 1.0 / (1.0 + S)
        d2U = lambda S: -1.0 / (1.0 + S) ** 2
    else:
        raise ValueError(name)
    return U, dU, d2U


def f_klammer(name, w2):
    """Klammer [lo, hi] fuer f0: lo mit Phi(lo) = 0 (Unterschuss), hi sicher Ueberschuss."""
    w2 = np.asarray(w2, float)
    if name == 'kontrolle':
        lo = np.sqrt(1.0 - np.sqrt(2.0 * w2 - 1.0))
        hi = np.sqrt((2.0 + np.sqrt(6.0 * w2 - 2.0)) / 3.0) * (1.0 - 1e-12)
        return lo, hi
    x = np.full_like(w2, 2.0)
    for _ in range(200):
        x = x - (w2 * x - np.log1p(x)) / (w2 - 1.0 / (1.0 + x))
    return np.sqrt(x), np.full_like(w2, 30.0)


# ---------------------------------------------------------------- Profil
def _acc(r, f, fp, w2c, dU):
    a = (dU(f * f) - w2c) * f
    if r == 0.0:
        return a / 3.0
    return a - 2.0 * fp / r


def _rk4(r, f, fp, w2c, dU, hs):
    k1f, k1p = fp, _acc(r, f, fp, w2c, dU)
    f2, p2 = f + 0.5 * hs * k1f, fp + 0.5 * hs * k1p
    k2f, k2p = p2, _acc(r + 0.5 * hs, f2, p2, w2c, dU)
    f3, p3 = f + 0.5 * hs * k2f, fp + 0.5 * hs * k2p
    k3f, k3p = p3, _acc(r + 0.5 * hs, f3, p3, w2c, dU)
    f4, p4 = f + hs * k3f, fp + hs * k3p
    k4f, k4p = p4, _acc(r + hs, f4, p4, w2c, dU)
    return (f + hs / 6.0 * (k1f + 2 * k2f + 2 * k3f + k4f),
            fp + hs / 6.0 * (k1p + 2 * k2p + 2 * k3p + k4p))


def klassifiziere(f0, w2c, dU, hs, nmax):
    """+1 Ueberschuss (f < 0 zuerst), -1 Unterschuss (f' > 0 zuerst), 0 offen."""
    f = f0.copy()
    fp = np.zeros_like(f)
    cls = np.zeros(f.shape, int)
    for n in range(nmax):
        f, fp = _rk4(n * hs, f, fp, w2c, dU, hs)
        neu_u = (cls == 0) & (f < 0)
        neu_n = (cls == 0) & (fp > 0) & (f >= 0)
        cls[neu_u] = 1
        cls[neu_n] = -1
        fertig = cls != 0
        f = np.where(fertig, 0.0, f)
        fp = np.where(fertig, 0.0, fp)
        if fertig.all():
            break
    return cls


def f0_bisektion(name, w2, dU, nmax_r, hs=0.02, K=24, runden=8):
    lo, hi = f_klammer(name, w2)
    lo = lo * (1 + 1e-9)
    nmax = int(nmax_r / hs) + 1
    for _ in range(runden):
        t = np.arange(1, K + 1) / (K + 1.0)
        cand = lo[:, None] + (hi - lo)[:, None] * t[None, :]
        cls = klassifiziere(cand, w2[:, None], dU, hs, nmax)
        for b in range(len(w2)):
            c = cls[b]
            pos = np.nonzero(c > 0)[0]
            i = pos[0] if len(pos) else K
            nhi = cand[b, i] if i < K else hi[b]
            nlo = cand[b, i - 1] if i > 0 else lo[b]
            lo[b], hi[b] = nlo, nhi
    return 0.5 * (lo + hi)


def profile(name, w2, stufe, ausgabe_traj=True):
    """Q-Ball-Profile fuer ein Feld w2 (B,) auf dem gemeinsamen Gitter r_n = n hp, n = 0..N."""
    U, dU, d2U = modell(name)
    w2 = np.asarray(w2, float)
    hp = STUFEN[stufe]
    mu = np.sqrt(1.0 - w2)
    n_p = np.rint(2.5 / mu / hp).astype(int)
    N = int(np.max(n_p + np.rint(16.0 / mu / hp).astype(int)))
    N += N % 2
    R = N * hp
    f0 = f0_bisektion(name, w2, dU, nmax_r=R)
    # Startwert A aus kurzem Aussenlauf
    B = len(w2)
    npmax = int(n_p.max())

    def aussen(F0, speichern=False):
        f = F0.copy()
        fp = np.zeros_like(f)
        wc = w2[:, None] if f.ndim == 2 else w2
        tf = np.empty((npmax + 1,) + f.shape) if speichern else None
        tp = np.empty((npmax + 1,) + f.shape) if speichern else None
        at_f = np.empty_like(f)
        at_p = np.empty_like(f)
        if speichern:
            tf[0], tp[0] = f, fp
        for n in range(npmax):
            f, fp = _rk4(n * hp, f, fp, wc, dU, hp)
            m = n_p == n + 1
            if m.any():
                at_f[m], at_p[m] = f[m], fp[m]
            if speichern:
                tf[n + 1], tp[n + 1] = f, fp
        return at_f, at_p, tf, tp

    def innen(A, speichern=False):
        mu_c = mu[:, None] if A.ndim == 2 else mu
        wc = w2[:, None] if A.ndim == 2 else w2
        f = A * np.exp(-mu_c * R) / R
        fp = -f * (mu_c + 1.0 / R)
        nmin = int(n_p.min())
        tf = np.empty((N - nmin + 1,) + f.shape) if speichern else None
        tp = np.empty((N - nmin + 1,) + f.shape) if speichern else None
        at_f = np.empty_like(f)
        at_p = np.empty_like(f)
        if speichern:
            tf[N - nmin], tp[N - nmin] = f, fp
        for n in range(N, nmin, -1):
            f, fp = _rk4(n * hp, f, fp, wc, dU, -hp)
            m = n_p == n - 1
            if m.any():
                at_f[m], at_p[m] = f[m], fp[m]
            if speichern:
                tf[n - 1 - nmin], tp[n - 1 - nmin] = f, fp
        return at_f, at_p, tf, tp

    fa, pa, _, _ = aussen(f0)
    rp = n_p * hp
    A = fa * rp * np.exp(mu * rp)
    eps = 1e-7
    hist = []
    for it in range(12):
        F0 = np.stack([f0, f0 * (1 + eps)], axis=1)
        AA = np.stack([A, A * (1 + eps)], axis=1)
        fa, pa, _, _ = aussen(F0)
        fi, pi_, _, _ = innen(AA)
        r1 = fa[:, 0] - fi[:, 0]
        r2 = pa[:, 0] - pi_[:, 0]
        j11 = (fa[:, 1] - fa[:, 0]) / (f0 * eps)
        j21 = (pa[:, 1] - pa[:, 0]) / (f0 * eps)
        j12 = -(fi[:, 1] - fi[:, 0]) / (A * eps)
        j22 = -(pi_[:, 1] - pi_[:, 0]) / (A * eps)
        det = j11 * j22 - j12 * j21
        d0 = -(j22 * r1 - j12 * r2) / det
        d1 = -(-j21 * r1 + j11 * r2) / det
        f0 = f0 + d0
        A = A + d1
        sch = float(np.max(np.maximum(np.abs(d0 / f0), np.abs(d1 / A))))
        hist.append(sch)
        if sch < 1e-14:
            break
    fa, pa, tfa, tpa = aussen(f0, speichern=True)
    fi, pi_, tfi, tpi = innen(A, speichern=True)
    nmin = int(n_p.min())
    f = np.empty((B, N + 1))
    fp = np.empty((B, N + 1))
    for b in range(B):
        k = n_p[b]
        f[b, :k + 1] = tfa[:k + 1, b]
        fp[b, :k + 1] = tpa[:k + 1, b]
        f[b, k:] = tfi[k - nmin:, b]
        fp[b, k:] = tpi[k - nmin:, b]
    sprung_f = np.abs(fa - fi) / f0
    sprung_p = np.abs(pa - pi_) / f0
    r = np.arange(N + 1) * hp
    wS = np.ones(N + 1)
    wS[1:-1:2] = 4.0
    wS[2:-1:2] = 2.0
    wS *= hp / 3.0
    S = f * f
    Q = 8 * np.pi * np.sqrt(w2) * np.sum(wS * S * r * r, axis=1)
    E = 4 * np.pi * np.sum(wS * (w2[:, None] * S + fp * fp + U(S)) * r * r, axis=1)
    # Groesse: Radius mit f = f0/2 und f(R)
    r_halb = np.array([r[np.argmax(f[b] < 0.5 * f0[b])] for b in range(B)])
    knoten = np.array([int(np.sum(np.diff(np.sign(f[b, :])) != 0)) for b in range(B)])
    return dict(w2=w2, hp=hp, N=N, R=R, f0=f0, A=A, mu=mu, rp=rp, f=f, fp=fp, Q=Q, E=E,
                sprung_f=sprung_f, sprung_p=sprung_p, newton=hist, r_halb=r_halb,
                f_R_rel=f[:, -1] / f0, knoten=knoten)


# ---------------------------------------------------------------- linearisierte Kanaele
def G_werte(name, prof, idx, rho, Nlin=None):
    """G_a, G_b fuer Punkte (w2[idx], rho). prof: Rueckgabe von profile(). Schritt h = 2 hp."""
    U, dU, d2U = modell(name)
    idx = np.asarray(idx, int)
    rho = np.asarray(rho, float)
    S = prof['f'] ** 2
    VT = (dU(S) + S * d2U(S)).T.copy()   # (N+1, B)
    gT = (S * d2U(S)).T.copy()
    hp = prof['hp']
    h = 2 * hp
    N = prof['N'] if Nlin is None else Nlin
    w = np.sqrt(prof['w2'][idx])
    Ea = ((w + rho) ** 2)[:, None]
    Eb = ((w - rho) ** 2)[:, None]
    kap = np.sqrt(1.0 - (w - rho) ** 2)
    M = len(rho)
    u = np.zeros((M, 2))
    v = np.zeros((M, 2))
    up = np.zeros((M, 2))
    vp = np.zeros((M, 2))
    up[:, 0] = 1.0
    vp[:, 1] = 1.0

    def acc(u, v, V, g):
        return (V - Ea) * u + g * v, (V - Eb) * v + g * u

    for n in range(N // 2):
        V0 = VT[2 * n][idx][:, None]
        g0 = gT[2 * n][idx][:, None]
        V1 = VT[2 * n + 1][idx][:, None]
        g1 = gT[2 * n + 1][idx][:, None]
        V2 = VT[2 * n + 2][idx][:, None]
        g2 = gT[2 * n + 2][idx][:, None]
        a1u, a1v = acc(u, v, V0, g0)
        k1 = (up, vp, a1u, a1v)
        u2, v2, p2, q2 = u + 0.5 * h * up, v + 0.5 * h * vp, up + 0.5 * h * a1u, vp + 0.5 * h * a1v
        a2u, a2v = acc(u2, v2, V1, g1)
        u3, v3, p3, q3 = u + 0.5 * h * p2, v + 0.5 * h * q2, up + 0.5 * h * a2u, vp + 0.5 * h * a2v
        a3u, a3v = acc(u3, v3, V1, g1)
        u4, v4, p4, q4 = u + h * p3, v + h * q3, up + h * a3u, vp + h * a3v
        a4u, a4v = acc(u4, v4, V2, g2)
        u = u + h / 6.0 * (up + 2 * p2 + 2 * p3 + p4)
        v = v + h / 6.0 * (vp + 2 * q2 + 2 * q3 + q4)
        up = up + h / 6.0 * (a1u + 2 * a2u + 2 * a3u + a4u)
        vp = vp + h / 6.0 * (a1v + 2 * a2v + 2 * a3v + a4v)
    R = (N // 2) * h
    G = -np.exp(-kap * R)[:, None] * (kap[:, None] * v + vp)
    # Isotropie-Kontrolle W[Y_a, Y_b] (soll 0 sein) relativ
    Wab = u[:, 0] * up[:, 1] - up[:, 0] * u[:, 1] + v[:, 0] * vp[:, 1] - vp[:, 0] * v[:, 1]
    skala = np.abs(u[:, 0] * up[:, 1]) + np.abs(up[:, 0] * u[:, 1]) + np.abs(v[:, 0] * vp[:, 1]) + np.abs(vp[:, 0] * v[:, 1])
    return G[:, 0], G[:, 1], Wab / np.maximum(skala, 1e-300)


def G_punkte(name, stufe, w2, rho):
    """G an beliebigen Punkten; Profile je eindeutigem w2."""
    w2 = np.asarray(w2, float)
    rho = np.asarray(rho, float)
    uw, inv = np.unique(w2, return_inverse=True)
    prof = profile(name, uw, stufe)
    Ga, Gb, iso = G_werte(name, prof, inv, rho)
    return Ga, Gb, iso, prof


# ---------------------------------------------------------------- Zeilen
def rho_gitter(w2):
    w = math.sqrt(w2)
    return np.linspace(1 - w + RAND, 1 + w - RAND, NRHO)


def illinois(name, prof, b, rl, rr, fl, fr, iters=14, tol=1e-10):
    """Vektorisierte Regula falsi (Illinois) fuer G_b = 0 auf Zeile(n) b."""
    rl, rr, fl, fr = rl.copy(), rr.copy(), fl.copy(), fr.copy()
    seite = np.zeros(len(rl), int)
    for _ in range(iters):
        rm = (rl * fr - rr * fl) / (fr - fl)
        _, gm, _ = G_werte(name, prof, b, rm)
        links = np.sign(gm) == np.sign(fl)
        rl = np.where(links, rm, rl)
        fl = np.where(links, gm, fl)
        rr = np.where(~links, rm, rr)
        fr = np.where(~links, gm, fr)
        fr = np.where(links & (seite == 1), fr * 0.5, fr)
        fl = np.where(~links & (seite == -1), fl * 0.5, fl)
        seite = np.where(links, 1, -1)
        if np.max(rr - rl) < tol:
            break
    rm = (rl * fr - rr * fl) / (fr - fl)
    return rm, rr - rl


def scan(name, stufe, ausdir, w2liste, nb=10):
    os.makedirs(ausdir, exist_ok=True)
    w2a = np.array(w2liste, float)
    for j0 in range(0, len(w2a), nb):
        t0 = time.time()
        wb = w2a[j0:j0 + nb]
        prof = profile(name, wb, stufe)
        rh = np.concatenate([rho_gitter(x) for x in wb])
        bi = np.repeat(np.arange(len(wb)), NRHO)
        Ga, Gb, iso = G_werte(name, prof, bi, rh)
        Ga, Gb, iso = Ga.reshape(len(wb), NRHO), Gb.reshape(len(wb), NRHO), iso.reshape(len(wb), NRHO)
        rhm = rh.reshape(len(wb), NRHO)
        jb, jr = np.nonzero(np.sign(Gb[:, :-1]) * np.sign(Gb[:, 1:]) < 0)
        if len(jb):
            wur, br = illinois(name, prof, jb, rhm[jb, jr], rhm[jb, jr + 1], Gb[jb, jr], Gb[jb, jr + 1])
            sa, sb, _ = G_werte(name, prof, jb, wur)
        else:
            wur, br, sa, sb = (np.zeros(0),) * 4
        dt = time.time() - t0
        for b, w2 in enumerate(wb):
            m = jb == b
            d = dict(modell=name, stufe=stufe, w2=float(w2), hp=prof['hp'], R=prof['R'], f0=float(prof['f0'][b]),
                     Q=float(prof['Q'][b]), E=float(prof['E'][b]), r_halb=float(prof['r_halb'][b]),
                     f_R_rel=float(prof['f_R_rel'][b]), knoten=int(prof['knoten'][b]),
                     anschluss_f=float(prof['sprung_f'][b]), anschluss_p=float(prof['sprung_p'][b]),
                     newton=prof['newton'], rho=rhm[b].tolist(), Ga=Ga[b].tolist(), Gb=Gb[b].tolist(),
                     iso_max=float(np.max(np.abs(iso[b]))),
                     nullstellen=wur[m].tolist(), klammer=br[m].tolist(), s=sa[m].tolist(),
                     Gb_an_null=sb[m].tolist(), sekunden_block=dt)
            fn = os.path.join(ausdir, 'zeile-%s-st%d-w2_%.4f.json' % (name, stufe, w2))
            with open(fn + '.tmp', 'w') as fh:
                json.dump(d, fh)
            os.replace(fn + '.tmp', fn)
            print('zeile w2=%.4f stufe=%d nullstellen=%d s=%s iso=%.1e anschl=%.1e knoten=%d' % (
                w2, stufe, int(m.sum()), ''.join('+' if x > 0 else '-' for x in sa[m]), d['iso_max'],
                d['anschluss_f'], d['knoten']), flush=True)
        print('block %d zeilen %.1fs' % (len(wb), dt), flush=True)


# ---------------------------------------------------------------- Kandidaten
def kandidaten(zeilen):
    """zeilen: Liste von dicts, sortiert nach w2. Gibt Startpunkte (w2, rho, Quelle) zurueck."""
    kand = []
    paare = []
    for j in range(len(zeilen) - 1):
        A, B = zeilen[j], zeilen[j + 1]
        ra, sa = np.array(A['nullstellen']), np.array(A['s'])
        rb, sb = np.array(B['nullstellen']), np.array(B['s'])
        # Detektor 1: wechselseitig naechste Nullstellen (Abstand <= 0,03), Vorzeichenwechsel von s
        if len(ra) and len(rb):
            for i in range(len(ra)):
                k = int(np.argmin(np.abs(rb - ra[i])))
                i2 = int(np.argmin(np.abs(ra - rb[k])))
                if i2 == i and abs(rb[k] - ra[i]) <= 0.03:
                    wechsel = np.sign(sa[i]) != np.sign(sb[k])
                    paare.append(dict(w2a=A['w2'], w2b=B['w2'], ra=float(ra[i]), rb=float(rb[k]),
                                      sa=float(sa[i]), sb=float(sb[k]), wechsel=bool(wechsel)))
                    if wechsel:
                        t = abs(sa[i]) / (abs(sa[i]) + abs(sb[k]))
                        kand.append(dict(w2=A['w2'] + t * (B['w2'] - A['w2']),
                                         rho=float(ra[i] + t * (rb[k] - ra[i])), quelle='s-wechsel'))
        # Detektor 2: Zellen-Umlauf auf dem (w2, rho-Index)-Gitter aus den Eckwerten
        WA = np.array(A['Ga']) + 1j * np.array(A['Gb'])
        WB = np.array(B['Ga']) + 1j * np.array(B['Gb'])
        ph = lambda z: np.angle(z)
        wrap = lambda x: (x + np.pi) % (2 * np.pi) - np.pi
        # Ecken: A_i -> A_{i+1} -> B_{i+1} -> B_i -> A_i (gegen den Uhrzeigersinn in (rho, w2)? Vorzeichen egal)
        d1 = wrap(ph(WA[1:]) - ph(WA[:-1]))
        d2 = wrap(ph(WB[1:]) - ph(WA[1:]))
        d3 = wrap(ph(WB[:-1]) - ph(WB[1:]))
        d4 = wrap(ph(WA[:-1]) - ph(WB[:-1]))
        n = np.rint((d1 + d2 + d3 + d4) / (2 * np.pi)).astype(int)
        for i in np.nonzero(n != 0)[0]:
            rA = 0.5 * (A['rho'][i] + A['rho'][i + 1])
            rB = 0.5 * (B['rho'][i] + B['rho'][i + 1])
            kand.append(dict(w2=0.5 * (A['w2'] + B['w2']), rho=0.5 * (rA + rB), quelle='zelle', n_zelle=int(n[i])))
    return kand, paare


def _schranken(name, w2, rho):
    w2 = np.clip(w2, 0.55 if name == 'kontrolle' else 0.05, 0.995)
    w = np.sqrt(w2)
    rho = np.clip(rho, 1 - w + 1e-4, 1 + w - 1e-4)
    return w2, rho


def newton2d(name, stufe, w2, rho, iters=10, dw=1e-6, dr=1e-6):
    """2D-Newton auf (G_a, G_b) = 0, vektorisiert ueber Kandidaten."""
    w2 = np.array(w2, float)
    rho = np.array(rho, float)
    K = len(w2)
    verlauf = []
    ok = np.zeros(K, bool)
    for it in range(iters):
        W2 = np.concatenate([w2, w2 + dw, w2])
        RH = np.concatenate([rho, rho, rho + dr])
        Ga, Gb, _, _ = G_punkte(name, stufe, W2, RH)
        g0a, g0b = Ga[:K], Gb[:K]
        J11 = (Ga[K:2 * K] - g0a) / dw
        J21 = (Gb[K:2 * K] - g0b) / dw
        J12 = (Ga[2 * K:] - g0a) / dr
        J22 = (Gb[2 * K:] - g0b) / dr
        det = J11 * J22 - J12 * J21
        dx = -(J22 * g0a - J12 * g0b) / det
        dy = -(-J21 * g0a + J11 * g0b) / det
        dx = np.where(np.isfinite(dx), dx, 0.0)
        dy = np.where(np.isfinite(dy), dy, 0.0)
        schritt = np.maximum(np.abs(dx), np.abs(dy))
        fak = np.where(schritt > 0.01, 0.01 / np.maximum(schritt, 1e-300), 1.0)
        w2, rho = _schranken(name, w2 + fak * dx, rho + fak * dy)
        verlauf.append(schritt.tolist())
        ok = schritt < 1e-10
        if ok.all():
            break
    return w2, rho, ok, verlauf


def _rechteck(t, w2c, rhoc):
    t = np.asarray(t, float)
    k = np.floor(t).astype(int) % 4
    x = t - np.floor(t)
    s = -1 + 2 * x
    w = np.select([k == 0, k == 1, k == 2, k == 3], [s, 1 + 0 * s, -s, -1 + 0 * s])
    r = np.select([k == 0, k == 1, k == 2, k == 3], [-1 + 0 * s, s, 1 + 0 * s, -s])
    return w2c + HALB * w, rhoc + HALB * r


def umlaeufe(name, stufe, w2c, rhoc):
    """Phasenumlauf von W um Rechtecke [w2c -+ HALB] x [rhoc -+ HALB], adaptiv verfeinert, ueber Kandidaten gebuendelt.
    Gegen den Uhrzeigersinn in der (w2, rho)-Ebene."""
    K = len(w2c)
    werte = [dict() for _ in range(K)]
    neu = [np.arange(4 * NKANTE) / NKANTE for _ in range(K)]
    erg = [None] * K
    for rnd in range(VERF_RUNDEN + 1):
        W2, RH, wer = [], [], []
        for k in range(K):
            if len(neu[k]):
                w, r = _rechteck(neu[k], w2c[k], rhoc[k])
                W2.append(w)
                RH.append(r)
                wer += [(k, t) for t in neu[k].tolist()]
        if wer:
            Ga, Gb, _, _ = G_punkte(name, stufe, np.concatenate(W2), np.concatenate(RH))
            for (k, t), z in zip(wer, (Ga + 1j * Gb).tolist()):
                werte[k][t] = z
        for k in range(K):
            tt = np.array(sorted(werte[k]))
            z = np.array([werte[k][t] for t in tt])
            ph = np.angle(z)
            d = (np.roll(ph, -1) - ph + np.pi) % (2 * np.pi) - np.pi
            groesst = float(np.max(np.abs(d)))
            n = float(np.sum(d) / (2 * np.pi))
            erg[k] = dict(umlauf=int(round(n)), umlauf_roh=n, groesster_sprung=groesst, punkte=len(tt),
                          aufgeloest=bool(groesst < SPRUNG), min_absW=float(np.min(np.abs(z))),
                          max_absW=float(np.max(np.abs(z))), runden=rnd,
                          rand=[[float(a), float(b.real), float(b.imag)] for a, b in zip(tt, z)])
            schlecht = np.nonzero(np.abs(d) >= SPRUNG)[0]
            tneu = []
            if rnd < VERF_RUNDEN:
                for i in schlecht:
                    t1 = tt[i]
                    t2 = tt[(i + 1) % len(tt)]
                    if t2 <= t1:
                        t2 += 4.0
                    tneu.append((0.5 * (t1 + t2)) % 4.0)
            neu[k] = np.array(tneu)
        if all(len(x) == 0 for x in neu):
            break
    return erg


def kand_lauf(name, stufe, ausdatei, dateien):
    t0 = time.time()
    zeilen = sorted([json.load(open(f)) for f in dateien], key=lambda d: d['w2'])
    kand, paare = kandidaten(zeilen)
    print('kandidaten roh:', len(kand), flush=True)
    uniq = []
    for k in kand:
        treffer = [u for u in uniq if abs(k['w2'] - u['w2']) < 2e-3 and abs(k['rho'] - u['rho']) < 2e-3]
        if treffer:
            if k['quelle'] not in treffer[0]['quelle']:
                treffer[0]['quelle'] += '+' + k['quelle']
        else:
            uniq.append(dict(k))
    print('kandidaten:', len(uniq), json.dumps(uniq), flush=True)
    erg = []
    if uniq:
        w2l, rl, ok, verl = newton2d(name, stufe, [u['w2'] for u in uniq], [u['rho'] for u in uniq])
        print('newton fertig %.1fs' % (time.time() - t0), flush=True)
        # doppelte Endpunkte zusammenlegen
        rein = []
        for i in range(len(uniq)):
            w = math.sqrt(w2l[i])
            im_fenster = bool((1 - w < rl[i] < 1 + w) and
                              (name == 'kontrolle' or 0.70 - 0.005 <= w2l[i] <= 0.98 + 0.005))
            e = dict(start=uniq[i], w2=float(w2l[i]), rho=float(rl[i]), konvergiert=bool(ok[i]),
                     im_fenster=im_fenster, newton=[v[i] for v in verl])
            e['doppelt_von'] = None
            for j, f in enumerate(erg):
                if f['konvergiert'] and abs(f['w2'] - e['w2']) < 1e-7 and abs(f['rho'] - e['rho']) < 1e-7:
                    e['doppelt_von'] = j
                    break
            erg.append(e)
            if ok[i] and im_fenster and e['doppelt_von'] is None:
                rein.append(i)
        if rein:
            ul = umlaeufe(name, stufe, w2l[rein], rl[rein])
            Ga, Gb, _, _ = G_punkte(name, stufe, w2l[rein], rl[rein])
            for j, i in enumerate(rein):
                erg[i].update(ul[j])
                erg[i]['G_am_punkt'] = [float(Ga[j]), float(Gb[j])]
        for i, e in enumerate(erg):
            print('kand', i, json.dumps(e), flush=True)
    out = dict(modell=name, stufe=stufe, zeilen=len(zeilen), w2_min=zeilen[0]['w2'], w2_max=zeilen[-1]['w2'],
               paare=paare, kandidaten=erg, sekunden=time.time() - t0)
    with open(ausdatei + '.tmp', 'w') as fh:
        json.dump(out, fh, indent=1)
    os.replace(ausdatei + '.tmp', ausdatei)
    print('fertig %.1fs' % (time.time() - t0), flush=True)


# ---------------------------------------------------------------- K2
def k2_lauf(ausdatei, w2liste):
    t0 = time.time()
    w2 = np.array(w2liste, float)
    res = {}
    for st in (1, 2):
        p = profile('log', w2, st)
        res[st] = p
    zeilen = []
    for i, x in enumerate(w2):
        a, b = res[1], res[2]
        zeilen.append(dict(w2=float(x), Q1=float(a['Q'][i]), Q2=float(b['Q'][i]), E1=float(a['E'][i]),
                           E2=float(b['E'][i]), dQ_rel=float(abs(a['Q'][i] - b['Q'][i]) / abs(b['Q'][i])),
                           dE_rel=float(abs(a['E'][i] - b['E'][i]) / abs(b['E'][i])),
                           f0_1=float(a['f0'][i]), f0_2=float(b['f0'][i]), r_halb=float(b['r_halb'][i]),
                           R=float(b['R']), f_R_rel=float(b['f_R_rel'][i]), knoten=int(b['knoten'][i]),
                           anschluss=float(b['sprung_f'][i]), dEdQ_kontr=None))
    # Kontrolle dE/dw = w dQ/dw (numerisch, Nachbarpunkte), nur informativ
    out = dict(zeilen=zeilen, max_dQ_rel=max(z['dQ_rel'] for z in zeilen),
               max_dE_rel=max(z['dE_rel'] for z in zeilen), sekunden=time.time() - t0)
    with open(ausdatei + '.tmp', 'w') as fh:
        json.dump(out, fh, indent=1)
    os.replace(ausdatei + '.tmp', ausdatei)
    print(json.dumps(out, indent=1), flush=True)


# ---------------------------------------------------------------- Rauchtest
def rauch():
    t0 = time.time()
    global STUFEN, NRHO
    STUFEN = {1: 0.04, 2: 0.02}
    NRHO = 41
    p = profile('kontrolle', np.array([0.797677]), 1)
    print('profil f0=%.8f R=%.1f Q=%.6f E=%.6f anschl=%.1e newton=%s r_halb=%.2f knoten=%d' % (
        p['f0'][0], p['R'], p['Q'][0], p['E'][0], p['sprung_f'][0], p['newton'], p['r_halb'][0], p['knoten'][0]))
    Ga, Gb, iso = G_werte('kontrolle', p, [0, 0, 0], [1.70, 1.744618, 1.78])
    print('G_a', Ga, 'G_b', Gb, 'iso', iso)
    print('sekunden %.1f' % (time.time() - t0))


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'rauch':
        rauch()
    elif cmd == 'scan':
        scan(sys.argv[2], int(sys.argv[3]), sys.argv[4], [float(x) for x in sys.argv[5:]])
    elif cmd == 'kand':
        kand_lauf(sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5:])
    elif cmd == 'umlauf':
        # NACHTRAG-1: umlauf <modell> <stufe> <runden> <halb> <aus> <w2> <rho> [<w2> <rho> ...]
        _name, _st = sys.argv[2], int(sys.argv[3])
        VERF_RUNDEN = int(sys.argv[4])
        HALB = float(sys.argv[5])
        _aus = sys.argv[6]
        _xy = [float(x) for x in sys.argv[7:]]
        _w2, _rho = np.array(_xy[0::2]), np.array(_xy[1::2])
        _t0 = time.time()
        _ul = umlaeufe(_name, _st, _w2, _rho)
        for _k in range(len(_w2)):
            _ul[_k]['w2'] = float(_w2[_k])
            _ul[_k]['rho'] = float(_rho[_k])
            print('umlauf', json.dumps({k: v for k, v in _ul[_k].items() if k != 'rand'}), flush=True)
        _out = dict(modell=_name, stufe=_st, runden_max=VERF_RUNDEN, halb=HALB, sprung=SPRUNG, nkante=NKANTE,
                    ergebnisse=_ul, sekunden=time.time() - _t0)
        with open(_aus + '.tmp', 'w') as _fh:
            json.dump(_out, _fh)
        os.replace(_aus + '.tmp', _aus)
    elif cmd == 'k2':
        k2_lauf(sys.argv[2], [float(x) for x in sys.argv[3:]])
    else:
        raise SystemExit('unbekannt: ' + cmd)
