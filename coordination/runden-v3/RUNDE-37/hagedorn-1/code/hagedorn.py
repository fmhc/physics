#!/usr/bin/env python3
"""RUNDE-37, Karte HAGEDORN-1: lineare Stabilitaet und Ringschwingungen drehender 2D-Q-Ball-Ringe (Winding m).

Plan, Herleitung und Urteilsregeln: ../PLAN.md. Explorativ (v3), synthetische Rechnung, keine Messdatenbestaetigung.

Modell wie RG-1 (RUNDE-06/regge/regge2d.py, hier unveraendert als code/regge2d.py):
    L = |phi_t|^2 - |grad phi|^2 - U(S), S = |phi|^2, U(S) = S - S^2 + S^3/2, phi = f(r) e^(i m theta - i omega t).
Stoerung (PLAN.md Abschnitt 1):
    phi = e^(-i omega t) e^(i m theta) [f + u e^(i l theta - i Omega t) + v* e^(-i l theta + i Omega* t)]
    (Omega + omega)^2 u = H_+ u + W v,   (Omega - omega)^2 v = H_- v + W u
    H_pm = -D_(m pm l) + U'(S) + S U''(S),  W = S U''(S),  D_k = d^2/dr^2 + (1/r) d/dr - k^2/r^2.
    Mit L_pm = D_(m pm l) + omega^2 - U' - S U'' und A = [[-L_+, W], [W, -L_-]], G = 2 omega diag(1, -1):
    Omega^2 x + Omega G x = A x,  x = (u, v)  ->  Omega (x, y) = [[0, 1], [A, -G]] (x, y),  y = Omega x.
Diskretisierung: versetztes gleichmaessiges Gitter r_j = (j - 1/2) h, j = 1..N, L = N h; zentrale Differenzen
8. Ordnung (9 Punkte) fuer d/dr und d^2/dr^2; Geisterpunkte r < 0 ueber die Paritaet (-1)^|k| der Winkelkomponente
k (u: k = m + l, v: k = m - l); bei r = L ungerade Spiegelung (Dirichlet). Profil: Schiessprofil aus regge2d.py
(h0 = 0,005), kubisch-hermitesch auf das Gitter gelegt, dann Newton auf demselben Gitter (diskrete Gleichung exakt).

Aufruf (nur ueber kleintest.sh auf der .69):
    hagedorn.py profile --out ORDNER
    hagedorn.py bdg --profile ORDNER/profile.npz --zeilen 8:0.55,5:0.55 --out ORDNER2 [--l-liste 0,1,2]
                    [--ohne-fein] [--ohne-kasten] [--budget 540]
Ausgabe: je Zeile eine JSON-Datei zeile_m{m}_w{w2}.json (atomar geschrieben); vorhandene Dateien werden uebersprungen.
"""
import os

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse
import datetime
import json
import math
import platform
import sys
import time

import numpy as np
import scipy
import scipy.linalg as sla
import scipy.sparse as sp
import scipy.sparse.linalg as spla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import regge2d as rg  # noqa: E402

# ---- Raster und Gitter (PLAN.md Abschnitt 2) ----
M_LISTE = (0, 1, 2, 3, 5, 8)
W2_LISTE = (0.55, 0.70, 0.85, 0.95, 0.99)
L_LISTE = tuple(range(13))
H0_SCHIESSEN = 0.005
H_BASIS = {0.55: 0.10, 0.70: 0.11, 0.85: 0.15, 0.95: 0.25, 0.99: 0.50}
SCHWANZ = 12.0          # Kasten L = R_aussen + 12/kappa (Basis und fein)
SCHWANZ_KASTEN = 18.0   # Kastenprobe L' = R_aussen + 18/kappa
DOMEGA = 1e-4           # Differenzenschritt in omega fuer die verallgemeinerte Nullmode
INNEN = 6.0             # Nullmoden-Residuen gewertet auf r <= R_aussen + 6/kappa (nach Rauchlauf r1/r2, PLAN.md R)

# ---- Schwellen und Regeln (PLAN.md Abschnitt 3; Karte unveraendert, Zusaetze gekennzeichnet) ----
IM_INSTABIL = 1e-4      # Karte HG1
IM_STABIL = 1e-6        # Karte HG2
IM_KANDIDAT = 1e-7      # Zusatz: ab hier wird der Eigenvektor geprueft (Randanteil)
RAND_MAX = 0.1          # Zusatz: Randanteil > 0,1 -> Randmode (unecht, offengelegt, nicht gewertet)
RING_MIN = 0.6          # Zusatz: Ringanteil >= 0,6 -> Ringmode (Ringast)
RING_BAND = 1e-2        # Zusatz: Ringband = {r : f^2 >= 1e-2 max f^2}
NULL_KANDIDATEN = 6     # Zusatz: Nullpaar = 2 der 6 betragskleinsten Eigenwerte mit groesster Ueberlappung
RING_SUCHE_MAX = 60     # hoechstens so viele reelle Kandidaten je l fuer den Ringast
KANDIDATEN_MAX = 120    # hoechstens so viele Kandidaten (groesstes Im zuerst) je l mit Eigenvektor pruefen

C1 = np.array([1 / 280, -4 / 105, 1 / 5, -4 / 5, 0.0, 4 / 5, -1 / 5, 4 / 105, -1 / 280])
C2 = np.array([-1 / 560, 8 / 315, -1 / 5, 8 / 5, -205 / 72, 8 / 5, -1 / 5, 8 / 315, -1 / 560])

RNG = np.random.default_rng(20261004)


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def u1(s):
    return 1.0 - 2.0 * s + 1.5 * s * s


def u2(s):
    return -2.0 + 3.0 * s


def wkey(w2):
    return f"{w2:.2f}"


def dateiname(m, w2):
    return f"zeile_m{m}_w{wkey(w2)}.json"


def json_schreiben(pfad, obj):
    tmp = pfad + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(obj, fh, indent=1, ensure_ascii=False, default=float)
    os.replace(tmp, pfad)


def cz(z):
    return [float(np.real(z)), float(np.imag(z))]


# ---------------------------------------------------------------- Profile (Schiessen, regge2d)

def cmd_profile(args):
    start = jetzt()
    t0 = time.perf_counter()
    zeilen = rg.zeilen_bauen(M_LISTE, W2_LISTE, False)
    P = rg.parameter(zeilen, H0_SCHIESSEN)
    sch = rg.schiessen(P, print)
    schl = set((z["m"], rg.w2_schluessel(z["w2"]), False) for z in zeilen)
    erg, prof = rg.profile_bauen(P, sch, zeilen, schl, print)
    os.makedirs(args.out, exist_ok=True)
    arrays = {}
    for (m, w2k, _n), (f, fp, h) in prof.items():
        arrays[f"f_{m}_{wkey(w2k)}"] = f
        arrays[f"fp_{m}_{wkey(w2k)}"] = fp
        arrays[f"h_{m}_{wkey(w2k)}"] = np.array([h])
    np.savez(os.path.join(args.out, "profile.npz"), **arrays)
    json_schreiben(os.path.join(args.out, "zeilen.json"),
                   dict(start=start, ende=jetzt(), dauer_s=time.perf_counter() - t0, h0=H0_SCHIESSEN,
                        knoten=platform.node(), numpy=np.__version__, scipy=scipy.__version__, zeilen=erg))
    for z in erg:
        print(f"m = {z['m']}, omega^2 = {z['w2']}: gueltig {z['gueltig']}, Q = {z.get('Q')}, E = {z.get('E')}, "
              f"R_max = {z.get('R_max')}, R_aussen = {z.get('R_aussen')}, Virial {z.get('virial')}")
    print(f"Profile fertig in {time.perf_counter() - t0:.1f} s")


# ---------------------------------------------------------------- Differenzen auf dem versetzten Gitter

_CACHE = {}


def fd_matrix(N, h, p, coeffs, order):
    j = np.arange(N)
    rows, cols, vals = [], [], []
    for o, c in zip(range(-4, 5), coeffs):
        if c == 0.0:
            continue
        k = j + o
        kk = k.copy()
        s = np.ones(N)
        neg = k < 0
        kk[neg] = -k[neg] - 1          # r_(-k-1) = -r_k ... Geisterpunkt -> Spiegelpunkt, Faktor Paritaet p
        s[neg] = p
        big = k >= N
        kk[big] = 2 * N - k[big] - 1   # ungerade Spiegelung an L = N h
        s[big] = -1.0
        rows.append(j)
        cols.append(kk)
        vals.append(c * s)
    A = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(N, N))
    return A / h ** order


def radial_op(N, h, k):
    """D_k = d^2/dr^2 + (1/r) d/dr - k^2/r^2 mit Paritaet (-1)^|k|."""
    schl = (N, h, k)
    if schl in _CACHE:
        return _CACHE[schl]
    p = 1.0 if abs(k) % 2 == 0 else -1.0
    r = (np.arange(N) + 0.5) * h
    D2 = fd_matrix(N, h, p, C2, 2)
    D1 = fd_matrix(N, h, p, C1, 1)
    D = (D2 + sp.diags(1.0 / r) @ D1 - sp.diags(float(k * k) / r ** 2)).tocsr()
    _CACHE[schl] = D
    return D


def ableitung(N, h, k, f):
    p = 1.0 if abs(k) % 2 == 0 else -1.0
    return fd_matrix(N, h, p, C1, 1) @ f


# ---------------------------------------------------------------- Newton auf dem Gitter

def newton(f0, m, w2, N, h, tol=1e-12, itmax=30):
    Dm = radial_op(N, h, m)
    f = f0.copy()
    verlauf = []
    best = np.inf
    stau = 0
    for it in range(itmax + 1):
        S = f * f
        F = Dm @ f + (w2 - u1(S)) * f
        res = float(np.max(np.abs(F)))
        verlauf.append(res)
        if res < tol:
            break
        if res > 0.5 * best:
            stau += 1
            if stau >= 3:
                break
        else:
            stau = 0
        best = min(best, res)
        if it == itmax:
            break
        J = (Dm + sp.diags(w2 - u1(S) - 2.0 * S * u2(S))).tocsc()
        f = f - spla.spsolve(J, F)
    return f, verlauf


def gitter_profil(tab, m, w2, h, L):
    f_tab, fp_tab, h_tab = tab
    N = int(math.ceil(L / h))
    r = (np.arange(N) + 0.5) * h
    f0 = rg.hermite(f_tab, fp_tab, h_tab, r)
    f, verlauf = newton(f0, m, w2, N, h)
    return dict(N=N, h=h, L=N * h, r=r, f=f, f0=f0, newton=verlauf,
                abweichung_schiessprofil=float(np.max(np.abs(f - f0)) / np.max(np.abs(f0))))


# ---------------------------------------------------------------- BdG

def bdg(f, m, l, w2, N, h):
    S = f * f
    V = w2 - u1(S) - S * u2(S)
    Lp = radial_op(N, h, m + l) + sp.diags(V)
    Lm = radial_op(N, h, m - l) + sp.diags(V)
    W = sp.diags(S * u2(S))
    A = sp.bmat([[-Lp, W], [W, -Lm]]).tocsr()
    om = math.sqrt(w2)
    G = sp.diags(np.concatenate([np.full(N, 2.0 * om), np.full(N, -2.0 * om)]))
    I2 = sp.identity(2 * N, format="csr")
    M = sp.bmat([[None, I2], [A, -G]]).tocsc()
    return M, A, G


def wnorm(x, r, h):
    N = r.size
    w = np.concatenate([r, r]) * h
    return math.sqrt(float(np.sum(w * np.abs(x[:2 * N]) ** 2)))


def wdot(a, b, r, h):
    w = np.concatenate([r, r]) * h
    return complex(np.sum(w * np.conj(a) * b))


def eigvec(M, lam):
    """Eigenvektor zu lam per inverser Iteration (komplexe LU, Verschiebung knapp neben lam)."""
    n = M.shape[0]
    sig = lam + 1e-9 * (1.0 + abs(lam)) * (1.0 + 1.0j)
    lu = spla.splu((M.astype(complex) - sig * sp.identity(n, dtype=complex, format="csc")).tocsc())
    x = RNG.standard_normal(n) + 1j * RNG.standard_normal(n)
    for _ in range(4):
        x = lu.solve(x)
        x /= np.linalg.norm(x)
    return x


def anteile(x, r, h, f, r_rand):
    N = r.size
    wt = r * (np.abs(x[:N]) ** 2 + np.abs(x[N:2 * N]) ** 2)
    ges = float(np.sum(wt))
    band = f * f >= RING_BAND * float(np.max(f * f))
    return float(np.sum(wt[r >= r_rand]) / ges), float(np.sum(wt[band]) / ges)


def verfolgen(M, lam, k=6):
    """Eigenwert nahe lam auf einem anderen Gitter (Shift-Invert, Arnoldi)."""
    sig = lam + 1e-7 * (1.0 + abs(lam)) * (1.0 + 1.0j)
    try:
        ev = spla.eigs(M.astype(complex), k=k, sigma=sig, which="LM", return_eigenvectors=False, tol=1e-12,
                       maxiter=5000)
    except Exception as e:  # noqa: BLE001
        return None, str(e)
    i = int(np.argmin(np.abs(ev - lam)))
    return complex(ev[i]), [cz(z) for z in ev]


def nullpaar_nahe_null(M, k=4):
    try:
        ev = spla.eigs(M.astype(complex), k=k, sigma=1e-7 * (1 + 1j), which="LM", return_eigenvectors=False,
                       tol=1e-12, maxiter=5000)
    except Exception as e:  # noqa: BLE001
        return None, str(e)
    ev = ev[np.argsort(np.abs(ev))]
    return [cz(z) for z in ev[:2]], [cz(z) for z in ev]


def sektor(prof, m, l, w2, R_aussen, x_ref=None):
    """Volles Spektrum eines Sektors l (dicht), Nullpaar, Kandidaten, Ringast."""
    f, r, h, N, L = prof["f"], prof["r"], prof["h"], prof["N"], prof["L"]
    M, A, G = bdg(f, m, l, w2, N, h)
    t0 = time.perf_counter()
    ev = sla.eigvals(M.toarray(), check_finite=False, overwrite_a=True)
    t_eig = time.perf_counter() - t0
    r_rand = R_aussen + 0.75 * (L - R_aussen)
    aus = dict(l=l, n=int(M.shape[0]), t_eig_s=t_eig, r_rand=r_rand)
    rest = np.ones(ev.size, bool)
    # Nullpaar (l = 0 Phase, l = 1 Verschiebung)
    if x_ref is not None:
        idx = np.argsort(np.abs(ev))[:NULL_KANDIDATEN]
        ueb = []
        for i in idx:
            z = eigvec(M, ev[i])
            x = z[:2 * N]
            o = abs(wdot(x_ref, x, r, h)) / (wnorm(x_ref, r, h) * wnorm(x, r, h))
            ueb.append((float(o), int(i)))
        ueb.sort(reverse=True)
        paar = [i for _o, i in ueb[:2]]
        rest[paar] = False
        aus["nullpaar"] = [dict(omega=cz(ev[i]), betrag=float(abs(ev[i])), ueberlappung=o) for o, i in ueb[:2]]
        aus["nullpaar_kandidaten"] = [dict(omega=cz(ev[i]), ueberlappung=o) for o, i in ueb]
        aus["nullpaar_max_betrag"] = float(max(abs(ev[i]) for i in paar))
    # Kandidaten fuer Instabilitaet (Im > IM_KANDIDAT), Eigenvektor -> Randanteil, Ringanteil
    kand = []
    randmoden = []
    ik = np.nonzero(rest & (ev.imag > IM_KANDIDAT))[0]
    ik = ik[np.argsort(-ev.imag[ik])]
    aus["kandidaten_ungeprueft"] = [cz(ev[i]) for i in ik[KANDIDATEN_MAX:]]
    for i in ik[:KANDIDATEN_MAX]:
        z = eigvec(M, ev[i])
        ra, ri = anteile(z, r, h, f, r_rand)
        eintrag = dict(omega=cz(ev[i]), randanteil=ra, ringanteil=ri)
        if ra > RAND_MAX:
            randmoden.append(eintrag)
        else:
            kand.append(eintrag)
    kand.sort(key=lambda e: -e["omega"][1])
    aus["kandidaten"] = kand
    aus["randmoden"] = randmoden
    im_rest = ev.imag[rest]
    aus["max_im_alle_ohne_nullpaar"] = float(np.max(im_rest)) if im_rest.size else 0.0
    if kand:
        aus["max_im_gezaehlt"] = kand[0]["omega"][1]
        aus["max_im_omega"] = kand[0]["omega"]
    else:
        # alle uebrigen Eigenwerte haben Im <= IM_KANDIDAT (oder sind Randmoden)
        im_ok = ev.imag[rest & (ev.imag <= IM_KANDIDAT)]
        aus["max_im_gezaehlt"] = float(max(0.0, np.max(im_ok))) if im_ok.size else 0.0
        aus["max_im_omega"] = None
    # Ringast: kleinste positive Re Omega unter den reellen (|Im| <= IM_STABIL), Ringanteil >= RING_MIN
    reell = np.nonzero(rest & (np.abs(ev.imag) <= IM_STABIL) & (ev.real > 0.0))[0]
    reell = reell[np.argsort(ev.real[reell])]
    liste = []
    ring = None
    for i in reell[:RING_SUCHE_MAX]:
        z = eigvec(M, ev[i])
        ra, ri = anteile(z, r, h, f, r_rand)
        liste.append(dict(omega=cz(ev[i]), ringanteil=ri, randanteil=ra))
        if ri >= RING_MIN:
            ring = liste[-1]
            break
    aus["ringast"] = ring
    aus["reell_aufsteigend"] = liste[:12]
    aus["anzahl_komplex_im_gt_kandidat"] = int(np.sum(rest & (ev.imag > IM_KANDIDAT)))
    aus["kleinste_betraege"] = [cz(z) for z in ev[rest][np.argsort(np.abs(ev[rest]))][:6]]
    return aus, M


def wnorm_innen(x, r, h, r_innen):
    N = r.size
    w = np.concatenate([r, r]) * h
    sel = np.concatenate([r <= r_innen, r <= r_innen])
    return math.sqrt(float(np.sum((w * np.abs(x[:2 * N]) ** 2)[sel])))


def nullmoden_residuen(prof, m, w2, tab, R_aus):
    """Residuen der bekannten Nullmoden im diskreten A (PLAN.md Abschnitt 3, HG0 a).
    Gewertet wird der Innenbereich r <= R_aussen + 6/kappa (Kastenrand-Abschneidefehler ausgenommen, PLAN.md 3.0);
    das Residuum ueber den ganzen Kasten wird mitberichtet."""
    f, r, h, N = prof["f"], prof["r"], prof["h"], prof["N"]
    om = math.sqrt(w2)
    r_in = R_aus + INNEN / math.sqrt(1.0 - w2)
    _M0, A0, G0 = bdg(f, m, 0, w2, N, h)
    x0 = np.concatenate([f, -f])
    res_phase = wnorm(A0 @ x0, r, h) / wnorm(x0, r, h)
    res_phase_innen = wnorm_innen(A0 @ x0, r, h, r_in) / wnorm(x0, r, h)
    # f_omega exakt aus der diskreten Familie: J f_omega = -2 omega f
    S = f * f
    J = (radial_op(N, h, m) + sp.diags(w2 - u1(S) - 2.0 * S * u2(S))).tocsc()
    f_om = spla.spsolve(J, -2.0 * om * f)
    # verallgemeinerte Nullmode aus der omega-Ableitung (Differenzen in omega, Newton bei omega +- DOMEGA,
    # Start f +- DOMEGA f_omega; nach Rauchlauf r4: Start bei f allein sprang fuer m = 8, omega^2 = 0,99 auf einen
    # anderen Ast)
    fs = []
    for s in (+1.0, -1.0):
        w2s = (om + s * DOMEGA) ** 2
        fsol, verl = newton(f + s * DOMEGA * f_om, m, w2s, N, h)
        fs.append((fsol, verl))
    f_om_fd = (fs[0][0] - fs[1][0]) / (2.0 * DOMEGA)
    x1 = np.concatenate([f_om_fd, f_om_fd])
    gx0 = G0 @ x0
    res_verallg = wnorm(A0 @ x1 - gx0, r, h) / wnorm(gx0, r, h)
    abw_fom = float(np.max(np.abs(f_om - f_om_fd)) / np.max(np.abs(f_om)))
    # Verschiebung, l = 1
    _M1, A1, _G1 = bdg(f, m, 1, w2, N, h)
    fp = ableitung(N, h, m, f)
    xT = np.concatenate([fp - m * f / r, fp + m * f / r])
    res_versch = wnorm(A1 @ xT, r, h) / wnorm(xT, r, h)
    res_versch_innen = wnorm_innen(A1 @ xT, r, h, r_in) / wnorm(xT, r, h)
    res_verallg_innen = wnorm_innen(A0 @ x1 - gx0, r, h, r_in) / wnorm(gx0, r, h)
    # Ladung und dQ/domega (Mittelpunktsumme; dQ/domega aus der diskreten Familie)
    N2 = float(np.sum(S * r) * h * 2.0 * math.pi)
    Q = 2.0 * om * N2
    dQ = 4.0 * math.pi * float(np.sum((S + 2.0 * om * f * f_om) * r) * h)
    Qp = 2.0 * (om + DOMEGA) * float(np.sum(fs[0][0] ** 2 * r) * h * 2.0 * math.pi)
    Qm = 2.0 * (om - DOMEGA) * float(np.sum(fs[1][0] ** 2 * r) * h * 2.0 * math.pi)
    return dict(res_phase=res_phase, res_verallgemeinert=res_verallg, res_verschiebung=res_versch,
                res_phase_innen=res_phase_innen, res_verschiebung_innen=res_versch_innen,
                res_verallgemeinert_innen=res_verallg_innen, r_innen=r_in,
                f_omega_abw_differenz_gegen_exakt=abw_fom, Q_gitter=Q, dQ_domega=dQ, dQ_domega_differenz=(Qp - Qm) /
                (2.0 * DOMEGA), newton_plus=fs[0][1][-1], newton_minus=fs[1][1][-1]), x0, xT


def zeile_rechnen(m, w2, tab, zrow, l_liste, fein, kasten, log):
    t0 = time.perf_counter()
    om = math.sqrt(w2)
    kappa = math.sqrt(1.0 - w2)
    R_aus = float(zrow["R_aussen"]) if (zrow.get("R_aussen") is not None and math.isfinite(zrow["R_aussen"])) \
        else float(zrow["R_max"])
    h = H_BASIS[round(w2, 2)]
    L = R_aus + SCHWANZ / kappa
    prof = gitter_profil(tab, m, w2, h, L)
    log(f"  m = {m}, omega^2 = {w2}: N = {prof['N']}, h = {h}, L = {prof['L']:.2f}, Newton-Rest "
        f"{prof['newton'][-1]:.1e} nach {len(prof['newton']) - 1} Schritten, Abw. vom Schiessprofil "
        f"{prof['abweichung_schiessprofil']:.1e}")
    nm, x0, xT = nullmoden_residuen(prof, m, w2, tab, R_aus)
    log(f"    Nullmoden-Residuen (innen): Phase {nm['res_phase_innen']:.1e}, Verschiebung {nm['res_verschiebung_innen']:.1e}, verallg. {nm['res_verallgemeinert_innen']:.1e}; ganzer Kasten: Phase {nm['res_phase']:.1e}, verallg. {nm['res_verallgemeinert']:.1e}, "
        f"Verschiebung {nm['res_verschiebung']:.1e}; dQ/domega {nm['dQ_domega']:.6g} (Differenz "
        f"{nm['dQ_domega_differenz']:.6g}); Q Gitter {nm['Q_gitter']:.6f} gegen Schiessen {zrow['Q']:.6f}")
    sektoren = []
    for l in l_liste:
        xr = x0 if l == 0 else (xT if l == 1 else None)
        s, _M = sektor(prof, m, l, w2, R_aus, xr)
        sektoren.append(s)
        ring = s["ringast"]
        log(f"    l = {l:2d}: n = {s['n']}, eig {s['t_eig_s']:.1f} s, max Im gezaehlt {s['max_im_gezaehlt']:.2e}, "
            f"Kandidaten {len(s['kandidaten'])}, Randmoden {len(s['randmoden'])}, "
            f"Nullpaar {s.get('nullpaar_max_betrag', float('nan')):.1e}, "
            f"Ringast {('%.6f' % ring['omega'][0]) if ring else '-'}")
    erg = dict(m=m, w2=w2, omega=om, kappa=kappa, R_max=zrow["R_max"], R_aussen=R_aus, R_innen=zrow.get("R_innen"),
               Q=zrow["Q"], E=zrow["E"], basis=dict(h=h, N=prof["N"], L=prof["L"], newton=prof["newton"],
                                                    abweichung_schiessprofil=prof["abweichung_schiessprofil"]),
               nullmoden=nm, sektoren=sektoren)
    # feines Gitter h/2, gleicher Kasten: Nullpaare, Ringast, Instabilitaeten verfolgen
    if fein:
        pf = gitter_profil(tab, m, w2, h / 2.0, prof["L"])
        nmf, _x0f, _xTf = nullmoden_residuen(pf, m, w2, tab, R_aus)
        fe = dict(h=h / 2.0, N=pf["N"], L=pf["L"], newton=pf["newton"], nullmoden=nmf, sektoren=[])
        for s in sektoren:
            l = s["l"]
            Mf, _A, _G = bdg(pf["f"], m, l, w2, pf["N"], pf["h"])
            e = dict(l=l)
            if l in (0, 1):
                e["nullpaar"], e["nahe_null"] = nullpaar_nahe_null(Mf)
            if s["ringast"]:
                lam = complex(*s["ringast"]["omega"])
                w, umg = verfolgen(Mf, lam)
                e["ringast"] = cz(w) if w is not None else None
                e["ringast_rel"] = float(abs(w - lam) / abs(w)) if w is not None else None
            if s["kandidaten"] and s["kandidaten"][0]["omega"][1] > IM_STABIL:
                lam = complex(*s["kandidaten"][0]["omega"])
                w, umg = verfolgen(Mf, lam)
                e["max_im"] = cz(w) if w is not None else None
                e["max_im_rel"] = float(abs(w - lam) / abs(w)) if w is not None else None
            fe["sektoren"].append(e)
        erg["fein"] = fe
        log(f"    fein: N = {pf['N']}, Newton-Rest {pf['newton'][-1]:.1e}, Residuen innen Phase {nmf['res_phase_innen']:.1e}, Verschiebung innen {nmf['res_verschiebung_innen']:.1e}, ganzer Kasten Phase {nmf['res_phase']:.1e}, "
            f"Verschiebung {nmf['res_verschiebung']:.1e}")
    # Kastenprobe fuer gezaehlte Instabilitaeten mit Im > IM_STABIL
    if kasten:
        kz = [(s["kandidaten"][0]["omega"][1], s["l"], complex(*s["kandidaten"][0]["omega"])) for s in sektoren
              if s["kandidaten"] and s["kandidaten"][0]["omega"][1] > IM_STABIL]
        if kz:
            kz.sort(reverse=True)
            pk = gitter_profil(tab, m, w2, h, R_aus + SCHWANZ_KASTEN / kappa)
            kp = dict(L=pk["L"], N=pk["N"], newton=pk["newton"][-1], sektoren=[])
            for _im, l, lam in kz[:3]:
                Mk, _A, _G = bdg(pk["f"], m, l, w2, pk["N"], pk["h"])
                w, umg = verfolgen(Mk, lam)
                kp["sektoren"].append(dict(l=l, basis=cz(lam), kasten=cz(w) if w is not None else None,
                                           umgebung=umg))
            erg["kasten"] = kp
    erg["dauer_s"] = time.perf_counter() - t0
    return erg


def cmd_bdg(args):
    start = jetzt()
    t_start = time.perf_counter()
    dat = np.load(args.profile)
    with open(os.path.join(os.path.dirname(args.profile), "zeilen.json")) as fh:
        zj = json.load(fh)
    zrows = {(z["m"], wkey(z["w2"])): z for z in zj["zeilen"]}
    os.makedirs(args.out, exist_ok=True)
    l_liste = [int(x) for x in args.l_liste.split(",")] if args.l_liste else list(L_LISTE)
    paare = []
    for teil in args.zeilen.split(","):
        a, b = teil.split(":")
        paare.append((int(a), float(b)))
    print(f"Start {start}, {platform.node()}, Python {platform.python_version()}, numpy {np.__version__}, "
          f"scipy {scipy.__version__}, OMP_NUM_THREADS={os.environ.get('OMP_NUM_THREADS')}, l = {l_liste}")
    c_eig = None   # Sekunden je n^3 (aus den bisherigen Zerlegungen)
    offen = []
    for m, w2 in paare:
        pfad = os.path.join(args.out, dateiname(m, w2))
        if os.path.exists(pfad):
            print(f"  m = {m}, omega^2 = {w2}: vorhanden, uebersprungen")
            continue
        z = zrows[(m, wkey(w2))]
        if not z.get("gueltig"):
            json_schreiben(pfad, dict(m=m, w2=w2, status="kein Profil", grund=z.get("grund")))
            continue
        kappa = math.sqrt(1.0 - w2)
        R_aus = float(z["R_aussen"])
        N_est = int(math.ceil((R_aus + SCHWANZ / kappa) / H_BASIS[round(w2, 2)]))
        n = 4 * N_est
        t_est = len(l_liste) * (c_eig if c_eig else 2.5e-9) * n ** 3 * 1.4
        verbraucht = time.perf_counter() - t_start
        if verbraucht + t_est > args.budget:
            print(f"  m = {m}, omega^2 = {w2}: Budget reicht nicht (verbraucht {verbraucht:.0f} s, geschaetzt "
                  f"{t_est:.0f} s), offen")
            offen.append(f"{m}:{w2}")
            continue
        tab = (dat[f"f_{m}_{wkey(w2)}"], dat[f"fp_{m}_{wkey(w2)}"], float(dat[f"h_{m}_{wkey(w2)}"][0]))
        erg = zeile_rechnen(m, w2, tab, z, l_liste, not args.ohne_fein, not args.ohne_kasten, print)
        erg.update(status="gerechnet", start=start, ende=jetzt(), knoten=platform.node(), numpy=np.__version__,
                   scipy=scipy.__version__, l_liste=l_liste)
        json_schreiben(pfad, erg)
        tz = [s["t_eig_s"] / s["n"] ** 3 for s in erg["sektoren"]]
        c_eig = max(tz) if c_eig is None else max(c_eig, max(tz))
        print(f"  -> {pfad} ({erg['dauer_s']:.1f} s)")
    print(f"Ende {jetzt()}, Dauer {time.perf_counter() - t_start:.1f} s; offen: {','.join(offen) if offen else '-'}")


def main():
    ap = argparse.ArgumentParser(description="HAGEDORN-1: BdG-Spektrum drehender 2D-Q-Ball-Ringe")
    sub = ap.add_subparsers(dest="befehl", required=True)
    a1 = sub.add_parser("profile")
    a1.add_argument("--out", required=True)
    a2 = sub.add_parser("bdg")
    a2.add_argument("--profile", required=True)
    a2.add_argument("--zeilen", required=True)
    a2.add_argument("--out", required=True)
    a2.add_argument("--l-liste", default="")
    a2.add_argument("--ohne-fein", action="store_true")
    a2.add_argument("--ohne-kasten", action="store_true")
    a2.add_argument("--budget", type=float, default=540.0)
    args = ap.parse_args()
    {"profile": cmd_profile, "bdg": cmd_bdg}[args.befehl](args)


if __name__ == "__main__":
    main()
