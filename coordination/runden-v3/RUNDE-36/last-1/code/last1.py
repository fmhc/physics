#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LAST-1 (Runde 36, fmhc-physics), Code-Agent.

Wechselwirkung zweier gleicher Quellen im fcc-Stabnetz, statisch, periodisch, Loesung per FFT.
Netz wie NETZ-C-1: Stablaenge 1, Zentralfedern k = 1, Winkelfedern W1 = d(cos theta) ueber alle 66 Stabpaare je
Knoten, Gewicht k_theta (aniso: 0, iso: 1/18). Kubische Kante a = sqrt2, L^3 kubische Zellen, 4 L^3 Knoten.
Hilfsgitter: einfach kubisch mit Weite a/2 = 1/sqrt2, Knoten = Punkte mit gerader Indexsumme, (2L)^3 Punkte.

Quellen (k = 1, f = 1, delta = 1; Pi skaliert mit f^2 bzw. delta^2):
  a  Punktlast f = z-Dach auf einem Knoten
  b  Dilatationszentrum: die 12 Staebe um einen Knoten mit Ruhelaenge 1 + delta
  c  zu langer Einzelstab (Ruhelaenge 1 + delta) laengs [110], zweiter Stab parallel, um Gittervektor R verschoben
Pi_12(R) = Pi(Paar) - 2 Pi(einzeln) = -f1^T K^-1 f2 = -(1/N) sum_{q != 0} S(q) e^{-i q R},  S = f^H D^-1 f,
fuer alle R zugleich (irfftn). q = 0 entfaellt (Lasten: gleichfoermiger Gegenkraft-Hintergrund; Eigendehnungen:
feste Zelle). Hintergrundkorrektur: Ewald-artige Kontinuumskorrektur dPi (PLAN Abschnitt 3), Pi_korr = Pi_torus - dPi.

Aufrufe (nur ueber kleintest.sh auf der .69):
  last1.py rauch     --out X.json
  last1.py kontrolle --L 16 --out X.json
  last1.py kontinuum --out X.json
  last1.py lauf      --L 32 [--L 64 ...] --out X.json
"""
import argparse, json, os, sys, time, hashlib, platform, resource
import numpy as np

S2 = np.sqrt(2.0)
KTH = {'aniso': 0.0, 'iso': 1.0 / 18.0}
NETZE = ('aniso', 'iso')
NB6 = np.array([[1, 1, 0], [1, -1, 0], [1, 0, 1], [1, 0, -1], [0, 1, 1], [0, 1, -1]])
NB12 = np.vstack([NB6, -NB6])
OMEGA = 1.0 / S2                       # Volumen je Knoten a^3/4
IJ = [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (2, 0)]
DB = NB6[0] / S2                       # Stabrichtung [110] (Quelle c)
RMIN_X, RMAX_X = 1.4, 16.5             # Extraktionsbereich (Stablaengen)
EPS_C = (1e-4, 2e-4)                   # |q| fuer die elastischen Konstanten (1/Stablaenge)
SIG_FAKTOR = 8.0                       # Ewald: sigma = L_box / 8
NT_NPHI = (32, 64)                     # Winkelquadratur der Ewald-Integrale (Gauss-Legendre in t, gleichmaessig in phi)
NPHI_KONT = 128                        # Kreisintegral der Kontinuumsformeln
H_KONT = 2e-3                          # Schritt fuer d^2/dt^2 der Dipolformel
SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()


# ------------------------------------------------------------------ Steifigkeit im q-Raum
def koeff_tensoren():
    """Winkelfeder-Koeffizienten: A-Terme je Stabrichtung b, Kreuzterme je (b1, b2, Vorzeichen)."""
    TA = np.zeros((6, 3, 3))
    TX = {}
    for i in range(12):
        for j in range(i + 1, 12):
            d1 = NB12[i] / S2; d2 = NB12[j] / S2
            c = float(d1 @ d2)
            if abs(c + 1.0) < 1e-12:
                continue
            g1 = d2 - c * d1; g2 = d1 - c * d2
            b1, s1 = i % 6, (1 if i < 6 else -1)
            b2, s2 = j % 6, (1 if j < 6 else -1)
            TA[b1] += np.outer(g1, g1); TA[b2] += np.outer(g2, g2)
            key = (min(b1, b2), max(b1, b2), s1 * s2)
            gg = np.outer(g1, g2) + np.outer(g2, g1)
            TX[key] = TX.get(key, np.zeros((3, 3))) + gg
    return TA, TX


TA_W, TX_W = koeff_tensoren()


def halbwinkel(qx, qy, qz):
    sh, ch = [], []
    for b in range(6):
        th = 0.5 * (qx * NB6[b, 0] + qy * NB6[b, 1] + qz * NB6[b, 2])
        sh.append(np.sin(th)); ch.append(np.cos(th))
    return sh, ch


def baue_D(sh, ch, kth):
    """D(q) als 6 Komponenten (xx, yy, zz, xy, yz, zx); q in Hilfsgitter-Einheiten (Phase q.n)."""
    shape = np.broadcast(*sh).shape
    D = [np.zeros(shape) for _ in range(6)]
    for b in range(6):
        A = 4.0 * sh[b] ** 2                          # |e^{i theta} - 1|^2
        dh = NB6[b] / S2
        T = np.outer(dh, dh) + kth * TA_W[b]
        for c, (i, j) in enumerate(IJ):
            if T[i, j] != 0.0:
                D[c] += T[i, j] * A
        del A
    if kth > 0:
        for (b1, b2, sg), T in TX_W.items():
            # Re[(E1-1)^*(E2-1)] = 4 s1 s2 (c1 c2 + s1 s2) mit s_i = sigma_i sh_bi
            X = (4.0 * sg) * sh[b1] * sh[b2] * (ch[b1] * ch[b2] + sg * sh[b1] * sh[b2])
            for c, (i, j) in enumerate(IJ):
                if T[i, j] != 0.0:
                    D[c] += (kth * T[i, j]) * X
            del X
    return D


def nullmaske(sh):
    """q kongruent 0 (alle Halbwinkel-Sinus null): dort entfaellt die Loesung (q = 0)."""
    return sum(s ** 2 for s in sh) < 1e-24


def invertiere(D, null):
    xx, yy, zz, xy, yz, zx = D
    c00 = yy * zz - yz * yz
    c01 = zx * yz - xy * zz
    c02 = xy * yz - zx * yy
    det = xx * c00 + xy * c01 + zx * c02
    c11 = xx * zz - zx * zx
    c12 = xy * zx - xx * yz
    c22 = xx * yy - xy * xy
    det[null] = 1.0
    detmin = float(np.abs(det[~null]).min()) if (~null).any() else 0.0
    G = [c00, c11, c22, c01, c12, c02]   # xx, yy, zz, xy, yz, zx
    for g in G:
        g /= det
        g[null] = 0.0
    return G, int(null.sum()), detmin


def max_ungerade(P):
    """Groesster Betrag auf den Hilfsgitterpunkten mit ungerader Indexsumme (keine Knoten; muss 0 sein)."""
    return max(float(np.abs(P[1::2, 0::2, 0::2]).max()), float(np.abs(P[0::2, 1::2, 0::2]).max()),
               float(np.abs(P[0::2, 0::2, 1::2]).max()), float(np.abs(P[1::2, 1::2, 1::2]).max()))


def Gij(G, i, j):
    idx = {(0, 0): 0, (1, 1): 1, (2, 2): 2, (0, 1): 3, (1, 0): 3, (1, 2): 4, (2, 1): 4, (2, 0): 5, (0, 2): 5}
    return G[idx[(i, j)]]


def elastische_konstanten(kth, eps):
    """C11, C12, C44 aus D(q) = Omega C_ijkl q_j q_l bei |q| = eps (1/Stablaenge)."""
    qg = eps / S2                                         # Hilfsgitter-Einheiten
    qs = np.array([[qg, 0, 0], [qg / S2, qg / S2, 0]])
    sh, ch = halbwinkel(qs[:, 0], qs[:, 1], qs[:, 2])
    D = baue_D(sh, ch, kth)
    n = OMEGA * eps ** 2
    C11 = D[0][0] / n; C44 = D[1][0] / n
    C12 = 2 * D[3][1] / n - C44
    return dict(C11=float(C11), C12=float(C12), C44=float(C44))


# ------------------------------------------------------------------ Gittervektoren
def gittervektoren(zentrum=(0.0, 0.0, 0.0), rmin=RMIN_X, rmax=RMAX_X):
    m = int(np.ceil(rmax * S2)) + 2
    a = np.arange(-m, m + 1)
    n = np.stack(np.meshgrid(a, a, a, indexing='ij'), -1).reshape(-1, 3)
    n = n[(n.sum(1) % 2) == 0]
    r = np.linalg.norm(n - np.asarray(zentrum), axis=1) / S2
    ok = (r >= rmin) & (r <= rmax)
    return n[ok], r[ok]


# ------------------------------------------------------------------ Felder (Hauptweg, halbes Gitter)
def felder(L, kth, mit_u=True):
    t0 = time.time()
    n2 = 2 * L
    q12 = 2 * np.pi * np.fft.fftfreq(n2)
    q3 = 2 * np.pi * np.arange(L + 1) / n2
    qx = q12[:, None, None]; qy = q12[None, :, None]; qz = q3[None, None, :]
    sh, ch = halbwinkel(qx, qy, qz)
    sh = [np.broadcast_to(s, (n2, n2, L + 1)).copy() for s in sh]
    ch = [np.broadcast_to(c, (n2, n2, L + 1)).copy() for c in ch]
    D = baue_D(sh, ch, kth)
    G, nnull, detmin = invertiere(D, nullmaske(sh))
    del D
    v = [4.0 * sum(sh[b] * ch[b] * (NB6[b, i] / S2) for b in range(6)) for i in range(3)]
    S = {}
    S['a'] = Gij(G, 2, 2)
    Sb = np.zeros_like(S['a'])
    for i in range(3):
        for j in range(3):
            Sb += Gij(G, i, j) * v[i] * v[j]
    S['b'] = Sb
    Gdd = sum(Gij(G, i, j) * DB[i] * DB[j] for i in range(3) for j in range(3))
    S['c'] = 4.0 * sh[0] ** 2 * Gdd
    del Gdd
    sh0, ch0 = sh[0], ch[0]
    del sh, ch
    nv, rv = gittervektoren()
    idx = tuple((nv % n2).T)
    out = dict(L=L, n2=n2, nullpunkte_q=nnull, det_min=detmin, t_D_s=time.time() - t0)
    werte = dict(n=nv, r=rv)
    for qn in ('a', 'b', 'c'):
        P = -np.fft.irfftn(S[qn], s=(n2, n2, n2), axes=(0, 1, 2))
        out['ungerade_rel_' + qn] = max_ungerade(P) / float(np.abs(P).max())
        werte['Pi_torus_' + qn] = P[idx].copy()
        werte['Pi_selbst_kreuz0_' + qn] = float(P[0, 0, 0])
        del P
    del S
    if mit_u:
        # Verschiebungsfelder einzelner Quellen
        for qn in ('a', 'b', 'c'):
            if qn == 'a':
                uh = [Gij(G, i, 2) for i in range(3)]
                zen = (0.0, 0.0, 0.0)
            elif qn == 'b':
                uh = [-1j * sum(Gij(G, i, j) * v[j] for j in range(3)) for i in range(3)]
                zen = (0.0, 0.0, 0.0)
            else:
                fak = -2.0 * sh0 ** 2 - 2j * sh0 * ch0
                uh = [fak * sum(Gij(G, i, j) * DB[j] for j in range(3)) for i in range(3)]
                zen = (0.5, 0.5, 0.0)
            nu, ru = gittervektoren(zentrum=zen)
            iu = tuple((nu % n2).T)
            U = np.zeros((len(nu), 3))
            for i in range(3):
                ui = np.fft.irfftn(uh[i], s=(n2, n2, n2), axes=(0, 1, 2))
                U[:, i] = ui[iu]
                del ui
            del uh
            werte['u_n_' + qn] = nu; werte['u_r_' + qn] = ru; werte['u_' + qn] = U
    out['t_gesamt_s'] = time.time() - t0
    out['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    return out, werte


# ------------------------------------------------------------------ Kontinuum: Gamma, Quellenfunktionen
def gamma_inv(C, qh):
    """Gamma_ik(qh) = C_ijkl qh_j qh_l fuer kubische C; Rueckgabe (n,3,3) Inverse."""
    C11, C12, C44 = C['C11'], C['C12'], C['C44']
    n = qh.shape[0]
    Gm = np.empty((n, 3, 3))
    for i in range(3):
        Gm[:, i, i] = C11 * qh[:, i] ** 2 + C44 * (1.0 - qh[:, i] ** 2)
        for j in range(3):
            if i != j:
                Gm[:, i, j] = (C12 + C44) * qh[:, i] * qh[:, j]
    return np.linalg.inv(Gm)


def s_funktion(C, quelle, qh):
    """Winkelfunktion s(qh): Monopol S = s/q^2 (a, ax, ay), Dipol S = s (b, c)."""
    Gi = gamma_inv(C, qh)
    if quelle == 'a':
        return Gi[:, 2, 2]
    if quelle == 'ax':
        return Gi[:, 0, 2]
    if quelle == 'ay':
        return Gi[:, 1, 2]
    if quelle == 'b':
        return 16.0 * np.einsum('ni,nij,nj->n', qh, Gi, qh)
    if quelle == 'c':
        return (qh @ DB) ** 2 * np.einsum('i,nij,j->n', DB, Gi, DB)
    raise ValueError(quelle)


def ewald_dPi(C, quelle, L, rphys, nt=NT_NPHI[0], nphi=NT_NPHI[1], chunk=500):
    """dPi(r) = Pi_torus,kont(r) - Pi_unendlich,kont(r) (PLAN 3.2); rphys (n,3) in Stablaengen."""
    Lb = L * S2; V = Lb ** 3; sig = Lb / SIG_FAKTOR; a = sig ** 2 / 2
    monopol = quelle in ('a', 'ax', 'ay')
    M = int(np.ceil(10.0 * SIG_FAKTOR / (2 * np.pi))) + 1
    ar = np.arange(-M, M + 1)
    m = np.stack(np.meshgrid(ar, ar, ar, indexing='ij'), -1).reshape(-1, 3)
    halb = (m[:, 2] > 0) | ((m[:, 2] == 0) & (m[:, 1] > 0)) | ((m[:, 2] == 0) & (m[:, 1] == 0) & (m[:, 0] > 0))
    m = m[halb]
    q = 2 * np.pi * m / Lb
    qn = np.linalg.norm(q, axis=1); qh = q / qn[:, None]
    s = s_funktion(C, quelle, qh)
    if monopol:
        w = (1 + a * qn ** 2) * np.exp(-a * qn ** 2) * s / qn ** 2
    else:
        w = np.exp(-a * qn ** 2) * s
    keep = np.abs(w) > 1e-18 * np.abs(w).max()
    q = q[keep]; w = w[keep]
    # Winkelquadratur
    t, wt = np.polynomial.legendre.leggauss(nt)
    phi = 2 * np.pi * np.arange(nphi) / nphi
    T, P = np.meshgrid(t, phi, indexing='ij')
    WT = np.repeat(wt[:, None], nphi, 1) * (2 * np.pi / nphi)
    st = np.sqrt(1 - T ** 2)
    om = np.stack([st * np.cos(P), st * np.sin(P), T], -1).reshape(-1, 3)
    wom = WT.reshape(-1) * s_funktion(C, quelle, om) / (2 * np.pi) ** 3
    out = np.empty(len(rphys))
    for k0 in range(0, len(rphys), chunk):
        r = rphys[k0:k0 + chunk]
        summe = (2.0 / V) * (np.cos(r @ q.T) @ w)
        b = r @ om.T
        beta = b ** 2 / (4 * a)
        if monopol:
            R = 0.5 * np.sqrt(np.pi / a) * np.exp(-beta) * (1.5 - beta)
        else:
            R = np.sqrt(np.pi) / (4 * a ** 1.5) * (1 - 2 * beta) * np.exp(-beta)
        integ = R @ wom
        out[k0:k0 + chunk] = -(summe - integ)
    return out, dict(sigma=sig, M=M, nq=int(len(w)), nt=nt, nphi=nphi)


def kontinuum_unendlich(C, quelle, rphys, nphi=NPHI_KONT, h=H_KONT, chunk=2000):
    """Pi_unendlich im Kontinuum: Monopol -(1/(8 pi^2 r)) Kreisintegral Gamma^-1 (Synge/Lifshitz);
    Dipol (1/(8 pi^2 r^3)) Kreisintegral d^2 s/dt^2 bei t = 0 (PLAN 3.3)."""
    out = np.empty(len(rphys))
    phi = 2 * np.pi * np.arange(nphi) / nphi
    for k0 in range(0, len(rphys), chunk):
        r = rphys[k0:k0 + chunk]
        rn = np.linalg.norm(r, axis=1); rh = r / rn[:, None]
        a = np.where(np.abs(rh[:, 2:3]) < 0.9, np.array([[0, 0, 1.0]]), np.array([[1.0, 0, 0]]))
        e1 = np.cross(a, rh); e1 /= np.linalg.norm(e1, axis=1)[:, None]
        e2 = np.cross(rh, e1)
        E = (np.cos(phi)[None, :, None] * e1[:, None, :] + np.sin(phi)[None, :, None] * e2[:, None, :])
        n = len(r)
        if quelle in ('a', 'ax', 'ay'):
            s = s_funktion(C, quelle, E.reshape(-1, 3)).reshape(n, nphi)
            G = s.mean(1) * 2 * np.pi / (8 * np.pi ** 2 * rn)
            out[k0:k0 + chunk] = -G if quelle == 'a' else G
        else:
            vals = []
            for tt in (-h, 0.0, h):
                qh = np.sqrt(1 - tt ** 2) * E + tt * rh[:, None, :]
                vals.append(s_funktion(C, quelle, qh.reshape(-1, 3)).reshape(n, nphi))
            d2 = (vals[0] - 2 * vals[1] + vals[2]) / h ** 2
            out[k0:k0 + chunk] = d2.mean(1) * 2 * np.pi / (8 * np.pi ** 2 * rn ** 3)
    return out


# ------------------------------------------------------------------ Kontrolle: explizite Paare im Ortsraum
def verschiebe(A, d):
    """A(x + d) als Feld ueber x (letzte drei Achsen)."""
    return np.roll(A, shift=(-int(d[0]), -int(d[1]), -int(d[2])), axis=(-3, -2, -1))


def energie_gradient(u, kth, e0, gerade):
    E = 0.0
    grad = np.zeros_like(u)
    for b in range(6):
        d = NB6[b]; dh = d / S2
        e = np.einsum('i,i...->...', dh, verschiebe(u, d) - u)
        if e0 is not None:
            e = e - e0[b]
        e = e * gerade
        E += 0.5 * float((e ** 2).sum())
        gx = e[None] * dh[:, None, None, None]
        grad += np.roll(gx, shift=tuple(int(x) for x in d), axis=(1, 2, 3)) - gx
    if kth > 0:
        for i in range(12):
            for j in range(i + 1, 12):
                d1, d2 = NB12[i], NB12[j]
                h1, h2 = d1 / S2, d2 / S2
                c = float(h1 @ h2)
                if abs(c + 1) < 1e-12:
                    continue
                g1 = h2 - c * h1; g2 = h1 - c * h2
                row = (np.einsum('i,i...->...', g1, verschiebe(u, d1) - u)
                       + np.einsum('i,i...->...', g2, verschiebe(u, d2) - u)) * gerade
                E += 0.5 * kth * float((row ** 2).sum())
                t = kth * row[None]
                grad += (np.roll(t * g1[:, None, None, None], shift=tuple(int(x) for x in d1), axis=(1, 2, 3))
                         + np.roll(t * g2[:, None, None, None], shift=tuple(int(x) for x in d2), axis=(1, 2, 3))
                         - t * (g1 + g2)[:, None, None, None])
    return E, grad


def quelle_ortsraum(qn, R, n2):
    """Kraefte f (3, n2^3) und Ruhelaengenaenderungen e0 (je Stabrichtung) einer Quelle am Gittervektor R."""
    f = np.zeros((3, n2, n2, n2)); e0 = None
    R = np.asarray(R)
    if qn == 'a':
        f[2][tuple(R % n2)] += 1.0
    else:
        e0 = [np.zeros((n2, n2, n2)) for _ in range(6)]
        if qn == 'b':
            staebe = [(b, R) for b in range(6)] + [(b, R - NB6[b]) for b in range(6)]
        else:
            staebe = [(0, R)]
        for b, x in staebe:
            e0[b][tuple(x % n2)] += 1.0
            dh = NB6[b] / S2
            for i in range(3):
                f[i][tuple((x + NB6[b]) % n2)] += dh[i]
                f[i][tuple(x % n2)] -= dh[i]
    return f, e0


def kontrolle(L, kth, Rliste):
    n2 = 2 * L
    q = 2 * np.pi * np.fft.fftfreq(n2)
    sh, ch = halbwinkel(q[:, None, None], q[None, :, None], q[None, None, :])
    sh = [np.broadcast_to(s, (n2,) * 3).copy() for s in sh]
    ch = [np.broadcast_to(c, (n2,) * 3).copy() for c in ch]
    G, nnull, _ = invertiere(baue_D(sh, ch, kth), nullmaske(sh))
    gerade = ((np.indices((n2,) * 3).sum(0) % 2) == 0).astype(float)
    N = n2 ** 3 // 2

    def loese(f):
        fh = [np.fft.fftn(f[i]) for i in range(3)]
        uh = [sum(Gij(G, i, j) * fh[j] for j in range(3)) for i in range(3)]
        u = np.array([np.fft.ifftn(uh[i]) for i in range(3)])
        return u.real, float(np.abs(u.imag).max())

    def pi_von(f, e0):
        u, im = loese(f)
        E, grad = energie_gradient(u, kth, e0, gerade)
        if e0 is None:
            fbar = f.sum(axis=(1, 2, 3)) / N
            res = grad - (f - fbar[:, None, None, None] * gerade[None])
            Pi = E - float((f * u).sum())
        else:
            res = grad
            Pi = E
        res = res * gerade[None]
        return Pi, float(np.abs(res).max()), im, float(np.abs(u * (1 - gerade[None])).max()), float(np.abs(u.sum(axis=(1, 2, 3))).max())

    out = dict(L=L, kth=kth, nullpunkte_q=nnull, quellen={})
    for qn in ('a', 'b', 'c'):
        f1, e01 = quelle_ortsraum(qn, (0, 0, 0), n2)
        P1, res1, im1, odd1, sum1 = pi_von(f1, e01)
        recs = []
        for R in Rliste:
            f2, e02 = quelle_ortsraum(qn, R, n2)
            e0p = None if e01 is None else [e01[b] + e02[b] for b in range(6)]
            Pp, resp, imp, oddp, sump = pi_von(f1 + f2, e0p)
            recs.append(dict(R=list(map(int, R)), r=float(np.linalg.norm(R) / S2), Pi_paar=Pp,
                             Pi12_explizit=Pp - 2 * P1, residuum_max=resp, imag_max=imp, ungerade_max=oddp,
                             summe_u_max=sump))
        out['quellen'][qn] = dict(Pi_einzeln=P1, residuum_einzeln=res1, imag_einzeln=im1, paare=recs,
                                  f_max=float(np.abs(f1).max()))
    # Hauptweg (halbes Gitter, Korrelation) zum Vergleich
    _, werte = felder(L, kth, mit_u=False)
    lut = {tuple(n): i for i, n in enumerate(werte['n'])}
    for qn in ('a', 'b', 'c'):
        for rec in out['quellen'][qn]['paare']:
            i = lut[tuple(rec['R'])]
            rec['Pi12_korrelation'] = float(werte['Pi_torus_' + qn][i])
            rec['abw_rel'] = abs(rec['Pi12_korrelation'] - rec['Pi12_explizit']) / max(abs(rec['Pi12_explizit']), 1e-300)
    return out


# ------------------------------------------------------------------ Laeufe
def info():
    return dict(numpy=np.__version__, python=platform.python_version(), host=platform.node(),
                start_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), argv=sys.argv, skript_sha256=SKRIPT_SHA)


def lauf(Ls, aus, netze=NETZE):
    res = dict(info=info(), netze={})
    npz = {}
    for netz in netze:
        kth = KTH[netz]
        C = elastische_konstanten(kth, EPS_C[0]); C2 = elastische_konstanten(kth, EPS_C[1])
        res['netze'][netz] = dict(kth=kth, C=C, C_eps2=C2, groessen={})
        for L in Ls:
            o, w = felder(L, kth, mit_u=True)
            rphys = w['n'] / S2
            t = time.time()
            for qn in ('a', 'b', 'c'):
                dP, ei = ewald_dPi(C, qn, L, rphys)
                w['dPi_' + qn] = dP
                w['Pi_korr_' + qn] = w['Pi_torus_' + qn] - dP
                o['ewald_' + qn] = ei
            # Korrektur der Punktlast-Verschiebung (Kontrast zu L4): u_korr = u_torus - dG f
            nu = w['u_n_a']; rpu = nu / S2
            # ewald_dPi liefert fuer die Monopol-Komponenten dPi_k = -dG_kz (k = x, y, z), also dG_kz = -dPi_k
            dG = np.stack([-ewald_dPi(C, k, L, rpu)[0] for k in ('ax', 'ay', 'a')], 1)
            w['u_korr_a'] = w['u_a'] - dG
            o['t_ewald_s'] = time.time() - t
            res['netze'][netz]['groessen'][str(L)] = o
            for k, v in w.items():
                if isinstance(v, np.ndarray):
                    npz['%s_L%d_%s' % (netz, L, k)] = v
                else:
                    o[k] = v
            print(netz, 'L', L, 'fertig', json.dumps({k: o[k] for k in ('t_gesamt_s', 'maxrss_MB', 'nullpunkte_q')}), flush=True)
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    np.savez_compressed(aus.replace('.json', '.npz'), **npz)
    return res


def kontinuum(aus):
    res = dict(info=info(), netze={})
    npz = {}
    nv, rv = gittervektoren()
    rphys = nv / S2
    npz['n'] = nv; npz['r'] = rv
    for netz in NETZE:
        C = elastische_konstanten(KTH[netz], EPS_C[0])
        res['netze'][netz] = dict(C=C)
        for qn in ('a', 'b', 'c'):
            t = time.time()
            npz['%s_Pi_kont_%s' % (netz, qn)] = kontinuum_unendlich(C, qn, rphys)
            res['netze'][netz]['t_' + qn] = time.time() - t
        # Kelvin (nur sinnvoll fuer iso; fuer beide Netze mit mu = C44, nu aus C12 berechnet)
        mu = C['C44']; lam = C['C12']; nu = lam / (2 * (lam + mu))
        rh = rphys / np.linalg.norm(rphys, axis=1)[:, None]
        npz['%s_Pi_kelvin_a' % netz] = -((3 - 4 * nu) + rh[:, 2] ** 2) / (16 * np.pi * mu * (1 - nu) * rv)
        res['netze'][netz]['kelvin'] = dict(mu=mu, nu=nu)
    # Probe der Dipolformel mit kleinerem Schritt
    Ci = elastische_konstanten(KTH['aniso'], EPS_C[0])
    sel = rphys[::97][:200]
    p1 = kontinuum_unendlich(Ci, 'b', sel); p2 = kontinuum_unendlich(Ci, 'b', sel, h=H_KONT / 2)
    res['dipol_schrittprobe_max_rel'] = float(np.max(np.abs(p1 - p2)) / np.max(np.abs(p1)))
    p3 = kontinuum_unendlich(Ci, 'b', sel, nphi=2 * NPHI_KONT)
    res['dipol_nphi_probe_max_rel'] = float(np.max(np.abs(p1 - p3)) / np.max(np.abs(p1)))
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    np.savez_compressed(aus.replace('.json', '.npz'), **npz)
    return res


def rauch(aus):
    """Nur Kontrollgroessen und Zeiten, keine Pi-Werte."""
    res = dict(info=info())
    res['C'] = {n: elastische_konstanten(KTH[n], EPS_C[0]) for n in NETZE}
    Rl = [(2, 2, 0), (4, 0, 0), (2, 2, 2)]
    for n in NETZE:
        k = kontrolle(8, KTH[n], Rl)
        res['kontrolle_L8_' + n] = {qn: dict(residuum=max(p['residuum_max'] for p in v['paare']),
                                            abw_rel=max(p['abw_rel'] for p in v['paare']),
                                            imag=max(p['imag_max'] for p in v['paare']),
                                            ungerade=max(p['ungerade_max'] for p in v['paare']))
                                    for qn, v in k['quellen'].items()}
        res['kontrolle_L8_' + n]['nullpunkte_q'] = k['nullpunkte_q']
    for L in (32, 64):
        t = time.time()
        o, w = felder(L, KTH['iso'], mit_u=True)
        res['zeit_felder_L%d_s' % L] = time.time() - t
        res['rss_nach_L%d_MB' % L] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
        res['ungerade_L%d' % L] = {k: v for k, v in o.items() if k.startswith('ungerade')}
        if L == 32:
            C = res['C']['iso']
            rp = w['n'][:3000] / S2
            t = time.time()
            d1, _ = ewald_dPi(C, 'a', L, rp)
            res['zeit_ewald_3000_s'] = time.time() - t
            d2, _ = ewald_dPi(C, 'a', L, rp, nt=96, nphi=192)
            res['ewald_quadratur_probe_rel'] = float(np.max(np.abs(d1 - d2)) / np.max(np.abs(d1)))
            d3, _ = ewald_dPi(C, 'b', L, rp)
            d4, _ = ewald_dPi(C, 'b', L, rp, nt=96, nphi=192)
            res['ewald_quadratur_probe_rel_b'] = float(np.max(np.abs(d3 - d4)) / np.max(np.abs(d3)))
            res['anzahl_gittervektoren'] = int(len(w['n']))
        del w
    return res


def rauch2(aus):
    """Quadraturwahl, Zeiten und Speicher fuer L = 128; keine Pi-Werte."""
    res = dict(info=info())
    C = elastische_konstanten(KTH['iso'], EPS_C[0])
    nv, rv = gittervektoren()
    rp = nv[:3000] / S2
    for qn in ('a', 'b', 'c'):
        d1, _ = ewald_dPi(C, qn, 32, rp, nt=32, nphi=64)
        d2, _ = ewald_dPi(C, qn, 32, rp, nt=64, nphi=128)
        res['ewald_32x64_gegen_64x128_rel_' + qn] = float(np.max(np.abs(d1 - d2)) / np.max(np.abs(d1)))
    t = time.time()
    ewald_dPi(C, 'b', 64, nv / S2)
    res['zeit_ewald_alle_%d_s' % len(nv)] = time.time() - t
    t = time.time()
    kontinuum_unendlich(C, 'b', nv[:2000] / S2)
    res['zeit_kontinuum_2000_s'] = time.time() - t
    t = time.time()
    o, w = felder(128, KTH['iso'], mit_u=True)
    res['zeit_felder_L128_s'] = time.time() - t
    res['maxrss_nach_L128_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ungerade_L128'] = {k: v for k, v in o.items() if k.startswith('ungerade')}
    res['nullpunkte_L128'] = o['nullpunkte_q']
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['rauch', 'rauch2', 'kontrolle', 'kontinuum', 'lauf'])
    ap.add_argument('--L', type=int, action='append')
    ap.add_argument('--netz', default='aniso,iso')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    if a.modus == 'rauch':
        res = rauch(a.out)
    elif a.modus == 'rauch2':
        res = rauch2(a.out)
    elif a.modus == 'kontrolle':
        Rl = [(2, 2, 0), (4, 4, 0), (6, 0, 0), (4, 2, 2), (4, 4, 4), (0, 0, 8)]
        res = dict(info=info(), netze={n: kontrolle(L, KTH[n], Rl) for n in NETZE for L in a.L[:1]})
    elif a.modus == 'kontinuum':
        res = kontinuum(a.out)
    else:
        res = lauf(a.L, a.out, tuple(a.netz.split(',')))
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1, default=lambda x: x.tolist() if isinstance(x, np.ndarray) else float(x))
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], 'maxrss %.0f MB' % res['maxrss_MB'], flush=True)


if __name__ == '__main__':
    main()
