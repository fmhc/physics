#!/usr/bin/env python3
"""RAUTE-ATEM-1 (Runde 42), Code-Agent fuer die Leitung claude-primary.

Modell (KARTE.md, Lesart PLAN.md Abschn. 2):
- Vier Punkte A, B (Scharnier), C, D; Durchmesser d_i = 1 + eps sin(phi_i) PU.
- Staebe A-B, A-C, B-C, A-D, B-D harmonisch, Ruhelaenge s_ij = (d_i + d_j)/2, Steifigkeit k (Zug und Druck).
- C-D: Fangbindung. Harmonisch wie ein Stab, solange die Luecke r_CD - s_CD < delta_f ist, sonst kraftfrei.
  Das schliesst die Huellenabstossung (Luecke < 0) ein.
- Phasen: phi_i' = omega - mu_phi dU/dphi_i + sqrt(2T) xi_i, U = Stab- und Huellenenergie (kein Mediumanteil).
  dU/dphi_i = -(eps/2) cos(phi_i) * Summe der Stabkraefte t_b (Zug positiv) an i.
- Medium (schaltbar): f_ij = B cos(phi_i - phi_j) / r^(D-1) entlang der Verbindung, positiv = anziehend, alle 6 Paare.
- Lagen ueberdaempft, ohne Rauschen: x_i' = mu_x F_i.
Einheiten: Laenge PU (Ruhedurchmesser 1), Zeit Takte (omega = 2 pi je Takt).
Nur auf der .69 ueber kleintest.sh (1 Thread).
"""
import argparse
import json
import math
import resource
import sys
import time

import numpy as np

OMEGA = 2.0 * math.pi
EPS = 0.10                      # Atemamplitude im Durchmesser (wie ATEM-NETZ-1)
K = 1.0                         # Stabsteifigkeit (wie ATEM-NETZ-1)
MU_X = 2.0                      # Lagebeweglichkeit: mu_x k / omega = 0,32 (Lagen langsamer als der Atem)
KAPPA = 0.01                    # schwache Huellenkopplung (K/omega = 0,01; ATEM-NETZ-1: 0,005 und 0,05)
MU_PHI = 8.0 * OMEGA * KAPPA / (K * EPS ** 2)   # = 50,27; K_xy = mu_phi k eps^2 / 8 = kappa omega
T_NOISE = 1.0e-3 * KAPPA * OMEGA                # T = 1e-3 K_xy (wie ATEM-NETZ-1)
DELTA_F = 0.02                  # Fangabstand (PLAN Abschn. 3)
G_AUF = 0.20                    # Oeffnungsschwelle (Plan): C-D-Luecke >= 2 eps
B_WERTE = (0.03, 0.05, 0.08)    # B / (k delta_f) = 1,5; 2,5; 4; B/k < 4(1-eps)^3/27 = 0,108 (kein Kollaps)
SAATEN = (1, 2, 3, 4)
DT = 0.005                      # 200 Schritte je Takt
TAKTE = 500
Z0 = 0.05                       # Startstoerung 3D: C und D je 0,05 PU angehoben (Faltwinkel ~173,4 Grad)
JITTER = 0.002                  # Lagerauschen am Start (je Koordinate, Saat-abhaengig)
SUB = 10                        # Ablage alle 10 Schritte (0,05 Takt)
PRUEF_ALLE = 1000               # Werkzeugprobe alle 1000 Schritte (5 Takte)
FD_H = 1.0e-5

I = np.array([0, 0, 1, 0, 1, 2])
J = np.array([1, 2, 2, 3, 3, 3])
NAMEN = ['AB', 'AC', 'BC', 'AD', 'BD', 'CD']
INC = np.zeros((6, 4))
INC[np.arange(6), I] = 1.0
INC[np.arange(6), J] = -1.0
ABS_INC = np.abs(INC)
H3 = math.sqrt(3.0) / 2.0


def rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def wrap(a):
    return (a + np.pi) % (2.0 * np.pi) - np.pi


def zustand(x, phi, B, dim, eps, mu_phi):
    """Vektorisiert: Knotenkraefte F, Phasengeschwindigkeit, Stabkraefte t (Zug +), Mediumkraefte fm (anziehend +)."""
    d = 1.0 + eps * np.sin(phi)
    dx = x[J] - x[I]
    r = np.sqrt((dx * dx).sum(axis=1))
    u = dx / r[:, None]
    s = 0.5 * (d[I] + d[J])
    gap = r - s
    t = K * gap
    cd_aktiv = bool(gap[5] < DELTA_F)
    if not cd_aktiv:
        t[5] = 0.0
    fm = B * np.cos(phi[I] - phi[J]) / r ** (dim - 1)
    F = INC.T @ ((t + fm)[:, None] * u)
    st = ABS_INC.T @ t
    dphi = OMEGA + mu_phi * 0.5 * eps * np.cos(phi) * st
    return F, dphi, t, fm, r, gap, cd_aktiv


def kraefte_schleife(x, phi, B, dim, eps):
    """Unabhaengiger Pfad (Schleife je Paar): Knotenkraft = Summe Stabkraefte + Mediumkraefte."""
    F = np.zeros((4, dim))
    for b in range(6):
        i, j = int(I[b]), int(J[b])
        dv = [float(x[j, a] - x[i, a]) for a in range(dim)]
        r = math.sqrt(sum(c * c for c in dv))
        s = 0.5 * ((1.0 + eps * math.sin(phi[i])) + (1.0 + eps * math.sin(phi[j])))
        tb = K * (r - s) if (b < 5 or (r - s) < DELTA_F) else 0.0
        fb = B * math.cos(phi[i] - phi[j]) / r ** (dim - 1)
        for a in range(dim):
            F[i, a] += (tb + fb) * dv[a] / r
            F[j, a] -= (tb + fb) * dv[a] / r
    return F


def energie(x, phi, B, dim, eps):
    E = 0.0
    for b in range(6):
        i, j = int(I[b]), int(J[b])
        dv = x[j] - x[i]
        r = math.sqrt(float(dv @ dv))
        s = 0.5 * ((1.0 + eps * math.sin(phi[i])) + (1.0 + eps * math.sin(phi[j])))
        g = r - s
        E += 0.5 * K * g * g if (b < 5 or g < DELTA_F) else 0.5 * K * DELTA_F ** 2
        c = math.cos(phi[i] - phi[j])
        E += (-B * c / r) if dim == 3 else (B * c * math.log(r))
    return E


def kraft_fd(x, phi, B, dim, eps):
    F = np.zeros((4, dim))
    for i in range(4):
        for a in range(dim):
            xp = x.copy()
            xm = x.copy()
            xp[i, a] += FD_H
            xm[i, a] -= FD_H
            F[i, a] = -(energie(xp, phi, B, dim, eps) - energie(xm, phi, B, dim, eps)) / (2.0 * FD_H)
    return F


def faltwinkel(x):
    x3 = x if x.shape[1] == 3 else np.hstack([x, np.zeros((4, 1))])
    a = x3[1] - x3[0]
    a = a / np.linalg.norm(a)
    vc = x3[2] - x3[0]
    vc = vc - vc.dot(a) * a
    vd = x3[3] - x3[0]
    vd = vd - vd.dot(a) * a
    return math.atan2(float(np.linalg.norm(np.cross(vc, vd))), float(vc.dot(vd)))


def start_raute(seed, dim):
    rng = np.random.default_rng(seed)
    phi = rng.uniform(0.0, 2.0 * math.pi, 4)
    jit = rng.normal(0.0, JITTER, (4, 3))
    x0 = np.array([[0.0, -0.5, 0.0], [0.0, 0.5, 0.0], [-H3, 0.0, 0.0], [H3, 0.0, 0.0]])
    if dim == 3:
        x0[2, 2] += Z0
        x0[3, 2] += Z0
    x = (x0 + jit)[:, :dim].copy()
    return x, phi, rng


def start_tetraeder():
    th = math.acos(1.0 / 3.0)
    return np.array([[0.0, -0.5, 0.0], [0.0, 0.5, 0.0],
                     [-H3 * math.sin(th / 2), 0.0, H3 * math.cos(th / 2)],
                     [H3 * math.sin(th / 2), 0.0, H3 * math.cos(th / 2)]])


def integriere(x, phi, rng, B, dim, takte, eps, mu_phi, T, pruefen=True):
    nsteps = int(round(takte / DT))
    nrec = nsteps // SUB + 1
    rec = {'t': np.zeros(nrec), 'theta': np.zeros(nrec), 'gap': np.zeros((nrec, 6)), 'r': np.zeros((nrec, 6)),
           'tb': np.zeros((nrec, 6)), 'fm': np.zeros((nrec, 6)), 'phi': np.zeros((nrec, 4)),
           'x': np.zeros((nrec, 4, dim)), 'cd': np.zeros(nrec, dtype=bool)}
    sig = math.sqrt(2.0 * T * DT) if T > 0 else 0.0
    pr = {'n': 0, 'n_ausgelassen': 0, 'max_int_vs_schleife': 0.0, 'max_schleife_vs_fd': 0.0,
          'max_bilanz_mit_reibung': 0.0, 'max_impuls_summe': 0.0}
    k_rec = 0
    for n in range(nsteps + 1):
        F1, dp1, t1, fm1, r1, g1, cd1 = zustand(x, phi, B, dim, eps, mu_phi)
        if n % SUB == 0:
            rec['t'][k_rec] = n * DT
            rec['theta'][k_rec] = faltwinkel(x)
            rec['gap'][k_rec] = g1
            rec['r'][k_rec] = r1
            rec['tb'][k_rec] = t1
            rec['fm'][k_rec] = fm1
            rec['phi'][k_rec] = phi
            rec['x'][k_rec] = x
            rec['cd'][k_rec] = cd1
            k_rec += 1
        if pruefen and n % PRUEF_ALLE == 0:
            # Werkzeugprobe: Kraftbilanz je Knoten. Stab- plus Mediumkraefte (Schleife) gegen
            # (a) die vektorisierte Kraft, die die Bewegung treibt (Reibung = -x'/mu_x), (b) -grad(U + V) numerisch.
            Fs = kraefte_schleife(x, phi, B, dim, eps)
            v = MU_X * F1
            pr['n'] += 1
            pr['max_int_vs_schleife'] = max(pr['max_int_vs_schleife'], float(np.abs(F1 - Fs).max()))
            pr['max_bilanz_mit_reibung'] = max(pr['max_bilanz_mit_reibung'], float(np.abs(Fs - v / MU_X).max()))
            pr['max_impuls_summe'] = max(pr['max_impuls_summe'], float(np.abs(Fs.sum(axis=0)).max()))
            if abs(g1[5] - DELTA_F) < 1.0e-3:
                pr['n_ausgelassen'] += 1
            else:
                Ffd = kraft_fd(x, phi, B, dim, eps)
                pr['max_schleife_vs_fd'] = max(pr['max_schleife_vs_fd'], float(np.abs(Fs - Ffd).max()))
        if n == nsteps:
            break
        xi = sig * rng.standard_normal(4) if sig > 0 else 0.0
        xp = x + DT * MU_X * F1
        pp = phi + DT * dp1 + xi
        F2, dp2, *_ = zustand(xp, pp, B, dim, eps, mu_phi)
        x = x + 0.5 * DT * MU_X * (F1 + F2)
        phi = phi + 0.5 * DT * (dp1 + dp2) + xi
    return x, phi, rec, pr


def lauf_raute(dim, B, seed, takte, aus_npz):
    t0 = time.time()
    x, phi, rng = start_raute(seed, dim)
    x, phi, rec, pr = integriere(x, phi, rng, B, dim, takte, EPS, MU_PHI, T_NOISE)
    np.savez_compressed(aus_npz, **rec)
    return {'dim': dim, 'B': B, 'seed': seed, 'takte': takte, 'npz': aus_npz, 'werkzeugprobe': pr,
            'laufzeit_s': round(time.time() - t0, 2)}


def statik(dim, B, eps, takte):
    """Ableitbare Kontrolle: feste Phasenmuster 0, 120, 240, 240 Grad (mu_phi = 0, T = 0).
    eps = 0: reine Statik; eps = EPS: Atmen bei festen Relativphasen (Zeitmittel der letzten Haelfte)."""
    psi = np.array([0.0, 2 * math.pi / 3, 4 * math.pi / 3, 4 * math.pi / 3])
    if dim == 3:
        x = start_tetraeder()
    else:
        x = np.array([[0.0, -0.5], [0.0, 0.5], [-H3, 0.0], [H3, 0.0]])
    rng = np.random.default_rng(0)
    x, phi, rec, pr = integriere(x, psi.copy(), rng, B, dim, takte, eps, 0.0, 0.0)
    h = len(rec['t']) // 2
    tb_m = rec['tb'][h:].mean(axis=0)
    fm_m = rec['fm'][h:].mean(axis=0)
    F, _, t, fm, r, gap, cd = zustand(x, phi, B, dim, eps, 0.0)
    aus = {'dim': dim, 'B': B, 'eps': eps, 'takte': takte, 'werkzeugprobe': pr,
           'tb_ende': dict(zip(NAMEN, t.tolist())), 'fm_ende': dict(zip(NAMEN, fm.tolist())),
           'tb_mittel_2haelfte': dict(zip(NAMEN, tb_m.tolist())), 'fm_mittel_2haelfte': dict(zip(NAMEN, fm_m.tolist())),
           'r_ende': dict(zip(NAMEN, r.tolist())), 'cd_gebunden_ende': cd,
           'max_restkraft_ende': float(np.abs(F).max())}
    if dim == 3:
        aus['max_abw_stab_gleich_minus_paar'] = float(np.abs(t + fm).max())
    else:
        # Gleichgewicht der verformten Raute: 5 Stabkraefte aus den Knotengleichungen (kleinste Quadrate)
        dx = x[J] - x[I]
        u = dx / np.sqrt((dx * dx).sum(axis=1))[:, None]
        A = np.zeros((8, 5))
        rhs = np.zeros(8)
        for b in range(5):
            for a in range(2):
                A[2 * I[b] + a, b] += u[b, a]
                A[2 * J[b] + a, b] -= u[b, a]
        for b in range(6):
            for a in range(2):
                rhs[2 * I[b] + a] -= fm[b] * u[b, a]
                rhs[2 * J[b] + a] += fm[b] * u[b, a]
        tl, *_ = np.linalg.lstsq(A, rhs, rcond=None)
        aus['t_gleichgewicht'] = dict(zip(NAMEN[:5], tl.tolist()))
        aus['max_abw_stab_gegen_gleichgewicht'] = float(np.abs(tl - t[:5]).max())
    return aus


def dtprobe(dim, B, takte):
    """Schrittweitenprobe: DT gegen DT/2, gleiche Saat, deterministisch (T = 0)."""
    global DT, SUB
    res = {}
    for fak in (1, 2):
        DT = 0.005 / fak
        SUB = 10 * fak
        x, phi, rng = start_raute(1, dim)
        x, phi, rec, pr = integriere(x, phi, rng, B, dim, takte, EPS, MU_PHI, 0.0, pruefen=False)
        res[fak] = (x, phi)
    DT, SUB = 0.005, 10
    return {'max_dx': float(np.abs(res[1][0] - res[2][0]).max()),
            'max_dphi': float(np.abs(wrap(res[1][1] - res[2][1])).max()), 'takte': takte, 'dim': dim, 'B': B}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['rauch', 'haupt', 'kontrolle', 'statik', 'dtprobe'])
    ap.add_argument('--dim', type=int, default=3)
    ap.add_argument('--B', type=float, default=0.0)
    ap.add_argument('--saaten', default='1,2,3,4')
    ap.add_argument('--takte', type=float, default=TAKTE)
    ap.add_argument('--aus', required=True)
    a = ap.parse_args()
    t0 = time.time()
    params = {'OMEGA': OMEGA, 'EPS': EPS, 'K': K, 'MU_X': MU_X, 'KAPPA': KAPPA, 'MU_PHI': MU_PHI,
              'T_NOISE': T_NOISE, 'DELTA_F': DELTA_F, 'G_AUF': G_AUF, 'DT': DT, 'Z0': Z0, 'JITTER': JITTER,
              'SUB': SUB, 'PRUEF_ALLE': PRUEF_ALLE, 'FD_H': FD_H}
    out = {'modus': a.modus, 'params': params, 'argv': sys.argv[1:], 'laeufe': []}
    saaten = [int(s) for s in a.saaten.split(',')]
    if a.modus in ('haupt', 'kontrolle', 'rauch'):
        B = 0.0 if a.modus == 'kontrolle' else a.B
        for s in saaten:
            npz = a.aus.replace('.json', '') + f'_s{s}.npz'
            r = lauf_raute(a.dim, B, s, a.takte, npz)
            out['laeufe'].append(r)
            print(f"[{a.modus}] dim={a.dim} B={B} seed={s}: {r['laufzeit_s']} s, Werkzeugprobe {r['werkzeugprobe']}",
                  flush=True)
    elif a.modus == 'statik':
        for dim in (3, 2):
            for B in B_WERTE:
                r = statik(dim, B, 0.0, a.takte)
                out['laeufe'].append(r)
                print(f"[statik] dim={dim} B={B}: Restkraft {r['max_restkraft_ende']:.2e}", flush=True)
            r = statik(dim, 0.05, EPS, a.takte)
            out['laeufe'].append(r)
            print(f"[statik-atem] dim={dim} B=0.05 eps={EPS}: Werkzeugprobe {r['werkzeugprobe']}", flush=True)
    elif a.modus == 'dtprobe':
        out['dtprobe'] = dtprobe(a.dim, a.B, a.takte)
        print(f"[dtprobe] {out['dtprobe']}", flush=True)
    out['laufzeit_s'] = round(time.time() - t0, 2)
    out['rss_mb'] = round(rss_mb(), 1)
    with open(a.aus, 'w') as f:
        json.dump(out, f, indent=1)
    print(f"fertig, {out['laufzeit_s']} s, {out['rss_mb']} MB", flush=True)


if __name__ == '__main__':
    main()
