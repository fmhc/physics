#!/usr/bin/env python3
"""RUNDE-38, Karte HAGEDORN-2: lineare Stabilitaet dicker drehender 2D-Q-Ball-Ringe kurz vor der Duennwand-Grenze.

Plan, Kriterien und Urteilsregeln: ../PLAN.md. Explorativ (v3), synthetische Rechnung, keine Messdatenbestaetigung.

Wiederverwendet, unveraendert (HAGEDORN-1): regge2d.py (Schiessen, Integrale, Radien), hagedorn.py (fd_matrix 8. Ordnung,
eigvec, Potential u1/u2, Hilfsfunktionen). BdG-Herleitung wie HAGEDORN-1 (PLAN.md dort, Abschnitt 1):
    Omega (x, y) = [[0, 1], [A, -G]] (x, y),  A = [[-L_+, W], [W, -L_-]],  G = 2 omega diag(1, -1),
    L_pm = D_(m pm l) + omega^2 - U' - S U'',  W = S U'',  D_k = d^2/dr^2 + (1/r) d/dr - k^2/r^2.
Neu gegenueber HAGEDORN-1 (PLAN.md Abschnitt 2):
    - Gitter r_j = r_a + (j - 1/2) h, j = 1..N. r_a = R_innen - 12/kappa, falls >= 2 (dann Dirichlet bei r_a, ungerade
      Spiegelung), sonst r_a = 0 mit Paritaet (-1)^|k| wie HAGEDORN-1. Aussen L = R_aussen + 12/kappa, Dirichlet.
    - h = 0,2 fuer alle Profile, fein h/2 = 0,1 (gleicher Kasten); Kastenprobe mit 18/kappa (innen und aussen).
    - l = 0 bis 3m.
    - Profilquelle: Versuch 1 Schiessen (regge2d, h0 = 0,005), gueltig nur mit |Virial| <= 1e-5; Versuch 2 gedaempftes
      Newton auf der vollen Scheibe (h_t = 0,05) aus dem Duennwand-Ansatz. Beide werden fuer alle Zeilen gerechnet und
      verglichen; das Gitterprofil entsteht in jedem Fall durch Newton auf dem jeweiligen Gitter.
    - Randanteil zaehlt bei r_a > 0 auch das innere Randviertel.

Aufruf (nur ueber kleintest.sh auf der .69):
    hagedorn2.py profile --out ORDNER
    hagedorn2.py bdg --profile ORDNER/profile.npz --zeilen 3:0.55,5:0.55 --out ORDNER2 [--l-liste 0,1,2]
                     [--ohne-fein] [--ohne-kasten] [--budget 540] [--dicht]
    (--dicht: Dichteprobe, volles Spektrum auf h/2, ohne Fein- und Kastenprobe)
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
from scipy.special import expit

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import regge2d as rg  # noqa: E402
import hagedorn as hg  # noqa: E402

# ---- Raster und Gitter (PLAN.md Abschnitt 2) ----
M_LISTE = (3, 5, 8, 12)
W2_LISTE = (0.51, 0.52, 0.53, 0.54, 0.55)
H0_SCHIESSEN = 0.005
H_BASIS = 0.2
H_TAB = 0.05            # Versuch 2: Newton-Tabelle auf der vollen Scheibe
SCHWANZ = 12.0          # Kasten: r_a = R_innen - 12/kappa (falls >= R_A_MIN), L = R_aussen + 12/kappa
SCHWANZ_KASTEN = 18.0   # Kastenprobe: 18/kappa innen und aussen
SCHWANZ_TAB = 22.0      # Tabelle bis r_aussen(Duennwand) + 22/kappa
R_A_MIN = 2.0           # innerer Schnitt erst ab r_a >= 2, sonst volle Scheibe
INNEN = 6.0             # Nullmoden-Residuen gewertet auf R_innen - 6/kappa <= r <= R_aussen + 6/kappa
DOMEGA = 1e-4
SIGMA_WAND = 1.0 / (2.0 * math.sqrt(2.0))   # Wandspannung bei omega^2 = 1/2 [M], PLAN.md Abschnitt 0
VIRIAL_MAX = 1e-5       # Schiessprofil nur gueltig mit |Virial| <= 1e-5 (wie RG-1 fuer Fits)

# ---- Schwellen und Regeln (wie HAGEDORN-1; PLAN.md Abschnitt 3) ----
IM_INSTABIL = 1e-4
IM_STABIL = 1e-6
IM_KANDIDAT = 1e-7
RAND_MAX = 0.1
RING_MIN = 0.6
RING_BAND = 1e-2
NULL_KANDIDATEN = 6
RING_SUCHE_MAX = 60
KANDIDATEN_MAX = 120
RING_FEIN_L = (2, 3, 4, 5, 6)   # Ringast auf h/2 verfolgt (beschreibend)


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def wkey(w2):
    return f"{w2:.2f}"


def dateiname(m, w2):
    return f"zeile_m{m}_w{wkey(w2)}.json"


def l_liste_fuer(m):
    return list(range(3 * m + 1))


def duennwand_radien(m, w2):
    """Duennwand-Naeherung [M], PLAN.md Abschnitt 0: eps r^2 -+ sigma r - m^2 = 0."""
    eps = w2 - 0.5
    wurzel = math.sqrt(SIGMA_WAND ** 2 + 4.0 * eps * m * m)
    return (wurzel - SIGMA_WAND) / (2.0 * eps), (wurzel + SIGMA_WAND) / (2.0 * eps)


# ---------------------------------------------------------------- Gitter und Operatoren

_CACHE = {}


def paritaet(k, ra):
    if ra > 0.0:
        return -1.0                       # Dirichlet bei r_a (ungerade Spiegelung)
    return 1.0 if abs(k) % 2 == 0 else -1.0


def radial_op(N, h, k, ra):
    schl = (N, h, k, ra)
    if schl in _CACHE:
        return _CACHE[schl]
    p = paritaet(k, ra)
    r = ra + (np.arange(N) + 0.5) * h
    D2 = hg.fd_matrix(N, h, p, hg.C2, 2)
    D1 = hg.fd_matrix(N, h, p, hg.C1, 1)
    D = (D2 + sp.diags(1.0 / r) @ D1 - sp.diags(float(k * k) / r ** 2)).tocsr()
    _CACHE[schl] = D
    return D


def ableitung(N, h, k, ra, f):
    return hg.fd_matrix(N, h, paritaet(k, ra), hg.C1, 1) @ f


def kasten(R_in, R_aus, kappa, schwanz):
    ra = R_in - schwanz / kappa
    if ra < R_A_MIN:
        ra = 0.0
    return ra, R_aus + schwanz / kappa


def gitter(ra, L_end, h):
    N = int(math.ceil((L_end - ra) / h - 1e-9))
    return N, ra + (np.arange(N) + 0.5) * h


def interp(tab, r):
    f_tab, fp_tab, h_tab, off = tab
    return rg.hermite(f_tab, fp_tab, h_tab, r - off)


def residuum(Dm, f, w2):
    return Dm @ f + (w2 - hg.u1(f * f)) * f


def newton(f0, m, w2, N, h, ra, tol=1e-12, itmax=80):
    """Gedaempftes Newton (Schrittweite halbieren, bis die 2-Norm des Rests faellt)."""
    Dm = radial_op(N, h, m, ra)
    f = f0.copy()
    F = residuum(Dm, f, w2)
    res = float(np.max(np.abs(F)))
    n2 = float(np.linalg.norm(F))
    verlauf = [res]
    for _it in range(itmax):
        if res < tol:
            break
        S = f * f
        J = (Dm + sp.diags(w2 - hg.u1(S) - 2.0 * S * hg.u2(S))).tocsc()
        d = spla.spsolve(J, F)
        lam = 1.0
        ok = False
        while lam >= 1.0 / 1024.0:
            fn = f - lam * d
            Fn = residuum(Dm, fn, w2)
            n2n = float(np.linalg.norm(Fn))
            if np.isfinite(n2n) and n2n < n2:
                ok = True
                break
            lam *= 0.5
        if not ok:
            break
        f, F, n2 = fn, Fn, n2n
        res = float(np.max(np.abs(F)))
        verlauf.append(res)
    return f, verlauf


def gitter_profil(tab, m, w2, h, ra, L_end):
    N, r = gitter(ra, L_end, h)
    f0 = interp(tab, r)
    f, verlauf = newton(f0, m, w2, N, h, ra)
    return dict(N=N, h=h, ra=ra, L=ra + N * h, r=r, f=f, newton=verlauf,
                abweichung_start=float(np.max(np.abs(f - f0)) / max(np.max(np.abs(f0)), 1e-300)))


def integrale(f, r, h, m, w2, fp):
    """E, Q, R auf dem versetzten Gitter (Mittelpunktsumme), wie RG-1 definiert."""
    w = 2.0 * math.pi * r * h
    S = f * f
    N2 = float(np.sum(w * S))
    G = float(np.sum(w * (fp * fp + m * m * S / (r * r))))
    VU = float(np.sum(w * rg.upot(S)))
    om = math.sqrt(w2)
    smax, rmax, rin, raus = rg.radien(r, S)
    return dict(Q=2.0 * om * N2, E=w2 * N2 + G + VU, virial=(VU - w2 * N2) / (VU + w2 * N2), R_max=float(rmax),
                R_innen=float(rin), R_aussen=float(raus), S_max=float(smax), r_mittel=float(np.sum(w * S * r)) / N2)


def profil_pruefung(f, r):
    """Ein Ring: f >= 0, die Menge {S >= S_max/2} ist ein einziges Intervall (keine zwei Ringe, keine Knoten)."""
    S = f * f
    smax = float(np.max(S))
    innen = (S[1:-1] > S[:-2]) & (S[1:-1] >= S[2:]) & (S[1:-1] > 1e-3 * smax)
    ueber = (S >= 0.5 * smax).astype(int)
    bereiche = int(np.sum(np.diff(np.concatenate([[0], ueber])) == 1))
    return dict(min_f_rel=float(np.min(f) / np.max(f)), anzahl_maxima=int(np.sum(innen)), anzahl_bereiche=bereiche,
                f_max=float(np.max(f)))


# ---------------------------------------------------------------- Profile (Versuch 1 Schiessen, Versuch 2 Newton)

def tabelle_duennwand(m, w2):
    r_i, r_o = duennwand_radien(m, w2)
    kappa = math.sqrt(1.0 - w2)
    N = int(math.ceil((r_o + SCHWANZ_TAB / kappa) / H_TAB))
    r = (np.arange(N) + 0.5) * H_TAB
    q = math.sqrt(2.0)
    S0 = expit(-q * (r - r_o)) * expit(q * (r - r_i))
    f0 = np.sqrt(S0)
    f, verlauf = newton(f0, m, w2, N, H_TAB, 0.0)
    fp = ableitung(N, H_TAB, m, 0.0, f)
    pr = profil_pruefung(f, r)
    ig = integrale(f, r, H_TAB, m, w2, fp)
    gueltig = bool(verlauf[-1] <= 1e-10 and pr["min_f_rel"] >= -1e-10 and pr["anzahl_bereiche"] == 1
                   and pr["f_max"] > 0.5)
    info = dict(r_innen_duennwand=r_i, r_aussen_duennwand=r_o, N=N, h=H_TAB, newton_rest=verlauf[-1],
                newton_schritte=len(verlauf) - 1, gueltig=gueltig, **pr, **ig)
    return info, (f, fp, H_TAB, 0.5 * H_TAB)


def cmd_profile(args):
    start = jetzt()
    t0 = time.perf_counter()
    os.makedirs(args.out, exist_ok=True)
    zeilen = rg.zeilen_bauen(M_LISTE, W2_LISTE, False)
    P = rg.parameter(zeilen, H0_SCHIESSEN)
    sch = rg.schiessen(P, print)
    schl = set((z["m"], rg.w2_schluessel(z["w2"]), False) for z in zeilen)
    erg, prof = rg.profile_bauen(P, sch, zeilen, schl, print)
    t_schiessen = time.perf_counter() - t0
    print(f"Schiessen fertig in {t_schiessen:.1f} s")
    arrays = {}
    aus = []
    for z in erg:
        m, w2 = z["m"], z["w2"]
        kappa = math.sqrt(1.0 - w2)
        key = (m, rg.w2_schluessel(w2), False)
        s_ok = bool(z.get("gueltig") and key in prof and abs(z.get("virial", 1.0)) <= VIRIAL_MAX)
        zeile = dict(m=m, w2=w2, schiessen=z, schiessen_gueltig_h2=s_ok)
        if key in prof:
            f, fp, h = prof[key]
            arrays[f"s_f_{m}_{wkey(w2)}"] = f
            arrays[f"s_fp_{m}_{wkey(w2)}"] = fp
            arrays[f"s_h_{m}_{wkey(w2)}"] = np.array([h, 0.0])
        t1 = time.perf_counter()
        tinfo, ttab = tabelle_duennwand(m, w2)
        tinfo["dauer_s"] = time.perf_counter() - t1
        zeile["duennwand"] = tinfo
        arrays[f"t_f_{m}_{wkey(w2)}"] = ttab[0]
        arrays[f"t_fp_{m}_{wkey(w2)}"] = ttab[1]
        arrays[f"t_h_{m}_{wkey(w2)}"] = np.array([ttab[2], ttab[3]])
        if s_ok:
            zeile.update(quelle="schiessen", Q=z["Q"], E=z["E"], R_max=z["R_max"], R_innen=z["R_innen"],
                         R_aussen=z["R_aussen"], r_mittel=z["r_mittel"], virial=z["virial"])
        elif tinfo["gueltig"]:
            zeile.update(quelle="duennwand-newton", Q=tinfo["Q"], E=tinfo["E"], R_max=tinfo["R_max"],
                         R_innen=tinfo["R_innen"], R_aussen=tinfo["R_aussen"], r_mittel=tinfo["r_mittel"],
                         virial=tinfo["virial"])
        else:
            zeile.update(quelle=None, grund=f"Schiessen: {z.get('grund')}, Virial {z.get('virial')}; "
                                            f"Newton: Rest {tinfo['newton_rest']:.1e}, Bereiche {tinfo['anzahl_bereiche']}")
        # Vergleich beider Quellen auf dem Basisgitter (gleicher Kasten)
        if s_ok and tinfo["gueltig"]:
            ra, Le = kasten(z["R_innen"], z["R_aussen"], kappa, SCHWANZ)
            p1 = gitter_profil((prof[key][0], prof[key][1], prof[key][2], 0.0), m, w2, H_BASIS, ra, Le)
            p2 = gitter_profil(ttab, m, w2, H_BASIS, ra, Le)
            zeile["vergleich_quellen"] = dict(
                max_diff_rel=float(np.max(np.abs(p1["f"] - p2["f"])) / float(np.max(np.abs(p1["f"])))),
                newton_rest_schiessen=p1["newton"][-1], newton_rest_duennwand=p2["newton"][-1],
                dE_rel=(tinfo["E"] - z["E"]) / z["E"], dQ_rel=(tinfo["Q"] - z["Q"]) / z["Q"],
                dR_max=tinfo["R_max"] - z["R_max"], dR_innen=tinfo["R_innen"] - z["R_innen"],
                dR_aussen=tinfo["R_aussen"] - z["R_aussen"])
        aus.append(zeile)
        vq = zeile.get("vergleich_quellen", {})
        print(f"m = {m}, omega^2 = {w2}: Quelle {zeile.get('quelle')}; Schiessen gueltig {z.get('gueltig')} "
              f"(Virial {z.get('virial')}, Spreizung {z.get('spreizung')}, Grund {z.get('grund')}); Duennwand-Newton "
              f"Rest {tinfo['newton_rest']:.1e} nach {tinfo['newton_schritte']} Schritten, Bereiche "
              f"{tinfo['anzahl_bereiche']} (lok. Maxima {tinfo['anzahl_maxima']}), R_i {tinfo['R_innen']:.3f} ({tinfo['r_innen_duennwand']:.3f}), R_a "
              f"{tinfo['R_aussen']:.3f} ({tinfo['r_aussen_duennwand']:.3f}), E {tinfo['E']:.6g}; Vergleich "
              f"{vq.get('max_diff_rel', float('nan')):.1e}, dE {vq.get('dE_rel', float('nan')):.1e}", flush=True)
    np.savez(os.path.join(args.out, "profile.npz"), **arrays)
    hg.json_schreiben(os.path.join(args.out, "zeilen.json"),
                      dict(start=start, ende=jetzt(), dauer_s=time.perf_counter() - t0, schiessen_s=t_schiessen,
                           h0=H0_SCHIESSEN, knoten=platform.node(), numpy=np.__version__, scipy=scipy.__version__,
                           zeilen=aus))
    print(f"Profile fertig in {time.perf_counter() - t0:.1f} s")


def tab_laden(dat, zrow):
    m, w2 = zrow["m"], zrow["w2"]
    pre = "s" if zrow["quelle"] == "schiessen" else "t"
    hh = dat[f"{pre}_h_{m}_{wkey(w2)}"]
    return (dat[f"{pre}_f_{m}_{wkey(w2)}"], dat[f"{pre}_fp_{m}_{wkey(w2)}"], float(hh[0]), float(hh[1]))


# ---------------------------------------------------------------- BdG

def bdg(f, m, l, w2, N, h, ra):
    S = f * f
    V = w2 - hg.u1(S) - S * hg.u2(S)
    Lp = radial_op(N, h, m + l, ra) + sp.diags(V)
    Lm = radial_op(N, h, m - l, ra) + sp.diags(V)
    W = sp.diags(S * hg.u2(S))
    A = sp.bmat([[-Lp, W], [W, -Lm]]).tocsr()
    om = math.sqrt(w2)
    G = sp.diags(np.concatenate([np.full(N, 2.0 * om), np.full(N, -2.0 * om)]))
    I2 = sp.identity(2 * N, format="csr")
    M = sp.bmat([[None, I2], [A, -G]]).tocsc()
    return M, A, G


def anteile(x, prof, R_in, R_aus):
    r, f, ra, L = prof["r"], prof["f"], prof["ra"], prof["L"]
    N = r.size
    wt = r * (np.abs(x[:N]) ** 2 + np.abs(x[N:2 * N]) ** 2)
    ges = float(np.sum(wt))
    rand = r >= R_aus + 0.75 * (L - R_aus)
    if ra > 0.0:
        rand |= r <= R_in - 0.75 * (R_in - ra)
    band = f * f >= RING_BAND * float(np.max(f * f))
    return float(np.sum(wt[rand]) / ges), float(np.sum(wt[band]) / ges)


def sektor(prof, m, l, w2, R_in, R_aus, x_ref=None):
    f, r, h, N, ra = prof["f"], prof["r"], prof["h"], prof["N"], prof["ra"]
    M, _A, _G = bdg(f, m, l, w2, N, h, ra)
    t0 = time.perf_counter()
    ev = sla.eigvals(M.toarray(), check_finite=False, overwrite_a=True)
    t_eig = time.perf_counter() - t0
    aus = dict(l=l, n=int(M.shape[0]), t_eig_s=t_eig)
    rest = np.ones(ev.size, bool)
    if x_ref is not None:
        idx = np.argsort(np.abs(ev))[:NULL_KANDIDATEN]
        ueb = []
        for i in idx:
            z = hg.eigvec(M, ev[i])
            x = z[:2 * N]
            o = abs(hg.wdot(x_ref, x, r, h)) / (hg.wnorm(x_ref, r, h) * hg.wnorm(x, r, h))
            ueb.append((float(o), int(i)))
        ueb.sort(reverse=True)
        paar = [i for _o, i in ueb[:2]]
        rest[paar] = False
        aus["nullpaar"] = [dict(omega=hg.cz(ev[i]), betrag=float(abs(ev[i])), ueberlappung=o) for o, i in ueb[:2]]
        aus["nullpaar_max_betrag"] = float(max(abs(ev[i]) for i in paar))
    kand = []
    randmoden = []
    ik = np.nonzero(rest & (ev.imag > IM_KANDIDAT))[0]
    ik = ik[np.argsort(-ev.imag[ik])]
    aus["kandidaten_ungeprueft"] = [hg.cz(ev[i]) for i in ik[KANDIDATEN_MAX:]]
    for i in ik[:KANDIDATEN_MAX]:
        z = hg.eigvec(M, ev[i])
        ra_, ri_ = anteile(z, prof, R_in, R_aus)
        eintrag = dict(omega=hg.cz(ev[i]), randanteil=ra_, ringanteil=ri_)
        (randmoden if ra_ > RAND_MAX else kand).append(eintrag)
    kand.sort(key=lambda e: -e["omega"][1])
    aus["kandidaten"] = kand[:40]
    aus["anzahl_kandidaten"] = len(kand)
    aus["randmoden"] = randmoden[:40]
    aus["anzahl_randmoden"] = len(randmoden)
    if kand:
        aus["max_im_gezaehlt"] = kand[0]["omega"][1]
        aus["max_im_omega"] = kand[0]["omega"]
    else:
        im_ok = ev.imag[rest & (ev.imag <= IM_KANDIDAT)]
        aus["max_im_gezaehlt"] = float(max(0.0, np.max(im_ok))) if im_ok.size else 0.0
        aus["max_im_omega"] = None
    reell = np.nonzero(rest & (np.abs(ev.imag) <= IM_STABIL) & (ev.real > 0.0))[0]
    reell = reell[np.argsort(ev.real[reell])]
    liste = []
    ring = None
    for i in reell[:RING_SUCHE_MAX]:
        z = hg.eigvec(M, ev[i])
        ra_, ri_ = anteile(z, prof, R_in, R_aus)
        liste.append(dict(omega=hg.cz(ev[i]), ringanteil=ri_, randanteil=ra_))
        if ri_ >= RING_MIN:
            ring = liste[-1]
            break
    aus["ringast"] = ring
    aus["reell_aufsteigend"] = liste[:8]
    aus["kleinste_betraege"] = [hg.cz(z) for z in ev[rest][np.argsort(np.abs(ev[rest]))][:6]]
    return aus


def verfolgen(M, lam, k=6):
    sig = lam + 1e-7 * (1.0 + abs(lam)) * (1.0 + 1.0j)
    try:
        ev = spla.eigs(M.astype(complex), k=k, sigma=sig, which="LM", return_eigenvectors=False, tol=1e-12,
                       maxiter=5000)
    except Exception as e:  # noqa: BLE001
        return None, str(e)
    i = int(np.argmin(np.abs(ev - lam)))
    return complex(ev[i]), [hg.cz(z) for z in ev]


def nullpaar_nahe_null(M, k=4):
    try:
        ev = spla.eigs(M.astype(complex), k=k, sigma=1e-7 * (1 + 1j), which="LM", return_eigenvectors=False,
                       tol=1e-12, maxiter=5000)
    except Exception as e:  # noqa: BLE001
        return None, str(e)
    ev = ev[np.argsort(np.abs(ev))]
    return [hg.cz(z) for z in ev[:2]], [hg.cz(z) for z in ev]


def wnorm_fenster(x, r, h, sel1):
    w = np.concatenate([r, r]) * h
    sel = np.concatenate([sel1, sel1])
    return math.sqrt(float(np.sum((w * np.abs(x[:2 * r.size]) ** 2)[sel])))


def nullmoden_residuen(prof, m, w2, R_in, R_aus):
    """Residuen der bekannten Nullmoden (beschreibend), gewertet im Fenster R_innen - 6/kappa <= r <= R_aussen + 6/kappa."""
    f, r, h, N, ra = prof["f"], prof["r"], prof["h"], prof["N"], prof["ra"]
    om = math.sqrt(w2)
    kappa = math.sqrt(1.0 - w2)
    fenster = (r >= R_in - INNEN / kappa) & (r <= R_aus + INNEN / kappa)
    _M0, A0, G0 = bdg(f, m, 0, w2, N, h, ra)
    x0 = np.concatenate([f, -f])
    res_phase = hg.wnorm(A0 @ x0, r, h) / hg.wnorm(x0, r, h)
    res_phase_f = wnorm_fenster(A0 @ x0, r, h, fenster) / hg.wnorm(x0, r, h)
    S = f * f
    J = (radial_op(N, h, m, ra) + sp.diags(w2 - hg.u1(S) - 2.0 * S * hg.u2(S))).tocsc()
    f_om = spla.spsolve(J, -2.0 * om * f)
    fs = []
    for s in (+1.0, -1.0):
        w2s = (om + s * DOMEGA) ** 2
        fsol, verl = newton(f + s * DOMEGA * f_om, m, w2s, N, h, ra)
        fs.append((fsol, verl))
    f_om_fd = (fs[0][0] - fs[1][0]) / (2.0 * DOMEGA)
    x1 = np.concatenate([f_om_fd, f_om_fd])
    gx0 = G0 @ x0
    res_verallg_f = wnorm_fenster(A0 @ x1 - gx0, r, h, fenster) / hg.wnorm(gx0, r, h)
    abw_fom = float(np.max(np.abs(f_om - f_om_fd)) / np.max(np.abs(f_om)))
    _M1, A1, _G1 = bdg(f, m, 1, w2, N, h, ra)
    fp = ableitung(N, h, m, ra, f)
    xT = np.concatenate([fp - m * f / r, fp + m * f / r])
    res_versch = hg.wnorm(A1 @ xT, r, h) / hg.wnorm(xT, r, h)
    res_versch_f = wnorm_fenster(A1 @ xT, r, h, fenster) / hg.wnorm(xT, r, h)
    dQ = 4.0 * math.pi * float(np.sum((S + 2.0 * om * f * f_om) * r) * h)
    ig = integrale(f, r, h, m, w2, fp)
    return dict(res_phase=res_phase, res_phase_fenster=res_phase_f, res_verschiebung=res_versch,
                res_verschiebung_fenster=res_versch_f, res_verallgemeinert_fenster=res_verallg_f,
                f_omega_abw_differenz_gegen_exakt=abw_fom, dQ_domega=dQ, gitter_integrale=ig,
                newton_plus=fs[0][1][-1], newton_minus=fs[1][1][-1]), x0, xT


def zeile_rechnen(m, w2, tab, zrow, l_liste, fein, mit_kasten, log, h=H_BASIS):
    t0 = time.perf_counter()
    _CACHE.clear()
    om = math.sqrt(w2)
    kappa = math.sqrt(1.0 - w2)
    R_in, R_aus = float(zrow["R_innen"]), float(zrow["R_aussen"])
    ra, Le = kasten(R_in, R_aus, kappa, SCHWANZ)
    prof = gitter_profil(tab, m, w2, h, ra, Le)
    log(f"  m = {m}, omega^2 = {w2} ({zrow['quelle']}): N = {prof['N']}, h = {h}, r_a = {ra:.2f}, L = {prof['L']:.2f}, "
        f"Newton-Rest {prof['newton'][-1]:.1e} nach {len(prof['newton']) - 1} Schritten, Abw. Start "
        f"{prof['abweichung_start']:.1e}")
    nm, x0, xT = nullmoden_residuen(prof, m, w2, R_in, R_aus)
    log(f"    Nullmoden (Fenster): Phase {nm['res_phase_fenster']:.1e}, Verschiebung {nm['res_verschiebung_fenster']:.1e}, "
        f"verallg. {nm['res_verallgemeinert_fenster']:.1e}; ganzer Kasten Verschiebung {nm['res_verschiebung']:.1e}; "
        f"dQ/domega {nm['dQ_domega']:.6g}; E Gitter {nm['gitter_integrale']['E']:.6f} gegen Quelle {zrow['E']:.6f}")
    sektoren = []
    for l in l_liste:
        xr = x0 if l == 0 else (xT if l == 1 else None)
        s = sektor(prof, m, l, w2, R_in, R_aus, xr)
        sektoren.append(s)
        ring = s["ringast"]
        log(f"    l = {l:2d}: n = {s['n']}, eig {s['t_eig_s']:.1f} s, max Im gezaehlt {s['max_im_gezaehlt']:.2e} "
            f"{s['max_im_omega']}, Kand. {s['anzahl_kandidaten']}, Randmoden {s['anzahl_randmoden']}, "
            f"Nullpaar {s.get('nullpaar_max_betrag', float('nan')):.1e}, Ringast {('%.6f' % ring['omega'][0]) if ring else '-'}",
            flush=True)
    erg = dict(m=m, w2=w2, omega=om, kappa=kappa, quelle=zrow["quelle"], R_max=zrow["R_max"], R_aussen=R_aus,
               R_innen=R_in, r_mittel=zrow.get("r_mittel"), Q=zrow["Q"], E=zrow["E"],
               basis=dict(h=h, N=prof["N"], ra=ra, L=prof["L"], newton=prof["newton"],
                          abweichung_start=prof["abweichung_start"]),
               nullmoden=nm, sektoren=sektoren)
    if fein:
        pf = gitter_profil(tab, m, w2, h / 2.0, ra, prof["L"])
        nmf, _x0f, _xTf = nullmoden_residuen(pf, m, w2, R_in, R_aus)
        fe = dict(h=h / 2.0, N=pf["N"], ra=ra, L=pf["L"], newton=pf["newton"], nullmoden=nmf, sektoren=[])
        for s in sektoren:
            l = s["l"]
            need_ring = s["ringast"] is not None and l in RING_FEIN_L
            need_im = s["kandidaten"] and s["kandidaten"][0]["omega"][1] > IM_STABIL
            if l not in (0, 1) and not need_ring and not need_im:
                continue
            Mf, _A, _G = bdg(pf["f"], m, l, w2, pf["N"], pf["h"], ra)
            e = dict(l=l)
            if l in (0, 1):
                e["nullpaar"], e["nahe_null"] = nullpaar_nahe_null(Mf)
            if need_ring:
                lam = complex(*s["ringast"]["omega"])
                w, _u = verfolgen(Mf, lam)
                e["ringast"] = hg.cz(w) if w is not None else None
                e["ringast_rel"] = float(abs(w - lam) / abs(w)) if w is not None else None
            if need_im:
                lam = complex(*s["kandidaten"][0]["omega"])
                w, _u = verfolgen(Mf, lam)
                e["max_im"] = hg.cz(w) if w is not None else None
                e["max_im_rel"] = float(abs(w - lam) / abs(w)) if w is not None else None
            fe["sektoren"].append(e)
        erg["fein"] = fe
        log(f"    fein: N = {pf['N']}, Newton-Rest {pf['newton'][-1]:.1e}, Verschiebung (Fenster) "
            f"{nmf['res_verschiebung_fenster']:.1e}", flush=True)
    if mit_kasten:
        kz = [(s["kandidaten"][0]["omega"][1], s["l"], complex(*s["kandidaten"][0]["omega"])) for s in sektoren
              if s["kandidaten"] and s["kandidaten"][0]["omega"][1] > IM_STABIL]
        if kz:
            kz.sort(reverse=True)
            ra2, Le2 = kasten(R_in, R_aus, kappa, SCHWANZ_KASTEN)
            pk = gitter_profil(tab, m, w2, h, ra2, Le2)
            kp = dict(ra=ra2, L=pk["L"], N=pk["N"], newton=pk["newton"][-1], sektoren=[])
            for _im, l, lam in kz[:3]:
                Mk, _A, _G = bdg(pk["f"], m, l, w2, pk["N"], pk["h"], ra2)
                w, umg = verfolgen(Mk, lam)
                kp["sektoren"].append(dict(l=l, basis=hg.cz(lam), kasten=hg.cz(w) if w is not None else None,
                                           umgebung=umg))
            erg["kasten"] = kp
            log(f"    Kasten: {[(e['l'], e['basis'], e['kasten']) for e in kp['sektoren']]}", flush=True)
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
    paare = []
    for teil in args.zeilen.split(","):
        a, b = teil.split(":")
        paare.append((int(a), float(b)))
    h = H_BASIS / 2.0 if args.dicht else H_BASIS
    print(f"Start {start}, {platform.node()}, Python {platform.python_version()}, numpy {np.__version__}, "
          f"scipy {scipy.__version__}, OMP_NUM_THREADS={os.environ.get('OMP_NUM_THREADS')}, h = {h}, "
          f"dicht = {args.dicht}", flush=True)
    c_eig = None
    offen = []
    for m, w2 in paare:
        pfad = os.path.join(args.out, dateiname(m, w2))
        if os.path.exists(pfad):
            print(f"  m = {m}, omega^2 = {w2}: vorhanden, uebersprungen")
            continue
        z = zrows[(m, wkey(w2))]
        if not z.get("quelle"):
            hg.json_schreiben(pfad, dict(m=m, w2=w2, status="kein Profil", grund=z.get("grund")))
            continue
        l_liste = [int(x) for x in args.l_liste.split(",")] if args.l_liste else l_liste_fuer(m)
        kappa = math.sqrt(1.0 - w2)
        ra, Le = kasten(float(z["R_innen"]), float(z["R_aussen"]), kappa, SCHWANZ)
        n = 4 * gitter(ra, Le, h)[0]
        t_est = len(l_liste) * (c_eig if c_eig else 1.5e-9) * n ** 3 * 1.6
        verbraucht = time.perf_counter() - t_start
        if verbraucht + t_est > args.budget:
            print(f"  m = {m}, omega^2 = {w2}: Budget reicht nicht (verbraucht {verbraucht:.0f} s, geschaetzt "
                  f"{t_est:.0f} s), offen", flush=True)
            offen.append(f"{m}:{w2}")
            continue
        tab = tab_laden(dat, z)
        erg = zeile_rechnen(m, w2, tab, z, l_liste, not (args.ohne_fein or args.dicht),
                            not (args.ohne_kasten or args.dicht), print, h=h)
        erg.update(status="gerechnet", dicht=bool(args.dicht), start=start, ende=jetzt(), knoten=platform.node(),
                   numpy=np.__version__, scipy=scipy.__version__, l_liste=l_liste)
        hg.json_schreiben(pfad, erg)
        tz = [s["t_eig_s"] / s["n"] ** 3 for s in erg["sektoren"]]
        c_eig = max(tz) if c_eig is None else max(c_eig, max(tz))
        print(f"  -> {pfad} ({erg['dauer_s']:.1f} s)", flush=True)
    print(f"Ende {jetzt()}, Dauer {time.perf_counter() - t_start:.1f} s; offen: {','.join(offen) if offen else '-'}")


def main():
    ap = argparse.ArgumentParser(description="HAGEDORN-2: BdG-Spektrum dicker drehender 2D-Q-Ball-Ringe")
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
    a2.add_argument("--dicht", action="store_true")
    a2.add_argument("--budget", type=float, default=540.0)
    args = ap.parse_args()
    {"profile": cmd_profile, "bdg": cmd_bdg}[args.befehl](args)


if __name__ == "__main__":
    main()
