#!/usr/bin/env python3
"""Runde 9, Karte GF-BIC-2 (Nachtrag D in PLAN.md): Umlaufzahl der W-Abbildung fuer psi_2-Stellen (Gegenlaeufer) und fuer
die Atmung des gemischten Balls (natives Profil, symmetrischer Sektor). Code begonnen 2026-09-30 07:08:35 CEST (date).

Verfahren wie bic2.py exakt (Version 3, l = 0), dessen Funktionen unveraendert importiert werden (newton_m, newton_direkt,
direkt_m, eigen, lin_fit_nullstelle, umlauf_rechteck, phasentest, profil, f_werte, radius_wo, r_halb). Neu:
  - lin_multi_k: wie bic2.lin_multi, aber mit eigener Koeffizientenfunktion (dp, sp, dp', sp') je Profil
  - k_psi2: dp = U'(S), sp = -g J S (zweite Komponente um den einkomponentigen Ball)
  - k_sym: dp = U' + S U'' - g J S, sp = S U'' - g J S/2 (gemischter Ball, symmetrischer Sektor, S = 2 h^2)
  - k_psi1: dp = U' + S U'', sp = S U'' (N = 1, Kontrolle gegen bic2)
  - prof_nativ: eigenes Schiessen fuer den gemischten Ball, h'' + (2/r) h' = [U'(2 h^2) - g J h^2 - omega^2] h,
    ohne Umweg ueber beta_eff (f = sqrt(2) h, damit S = f^2 die Gesamtdichte ist)
  - stelle: Stufe 1 grob (Pole, W-Gitter, Fit), Stufe 2 je Rechteckbreite neue Profile um den Fit-Mittelpunkt, zweiter
    Fit, Rechteck um den Fit-Mittelpunkt; liegt der zweite Fit ausserhalb 0,8 dx, dritte Lage um ihn.
Kommandos: rauch | punkt --name Z1|Z2|Z3|BG|K1
"""
import argparse
import cmath
import json
import math
import os
import sys
import traceback

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import numpy as np  # noqa: E402
import torch  # noqa: E402

HIER = os.path.dirname(os.path.abspath(__file__))
B2_PFAD = None
for _p in (HIER, os.path.normpath(os.path.join(HIER, "..", "..", "RUNDE-07", "bic2"))):
    if os.path.isfile(os.path.join(_p, "bic2.py")):
        sys.path.insert(0, _p)
        B2_PFAD = os.path.join(_p, "bic2.py")
        break
sys.path.insert(0, HIER)
import bic2 as B2  # noqa: E402
import gfbic as G  # noqa: E402  (nur fuer Budget, jetzt, sha256, jsonfest, uhr)

F64, C128 = torch.float64, torch.complex128
JK = 1.0

# Name: (Koeffizienten, g, x0, nu0, d nu/d x, cgam, Profilart)
PUNKTE = {
    "Z1": ("psi2", 0.2, 0.7113, 1.68874, 1.17, 0.01, "einfeld"),
    "Z2": ("psi2", 0.2, 0.6462, 1.6109, 1.25, 0.01, "einfeld"),
    "Z3": ("psi2", 0.4985, 0.551158, 1.51526, 1.35, 0.01, "einfeld"),
    "BG": ("sym", 0.2, 0.75869, 1.71173, 0.40, 1.07, "nativ"),
    "K1": ("psi1", 0.0, 0.797677, 1.744618, 0.4049, 1.07, "einfeld"),
}


# ================================================================ Koeffizienten (dp, sp, dp'(S), sp'(S))

def U1(S):
    return 1.0 - 2.0 * S + 1.5 * S * S


def U2(S):
    return -2.0 + 3.0 * S


def k_psi2(S, g):
    return U1(S), -g * JK * S, U2(S), -g * JK + 0.0 * S


def k_sym(S, g):
    return (U1(S) + S * U2(S) - g * JK * S, S * U2(S) - 0.5 * g * JK * S,
            2.0 * U2(S) + 3.0 * S - g * JK, U2(S) + 3.0 * S - 0.5 * g * JK)


def k_psi1(S, g):
    return U1(S) + S * U2(S), S * U2(S), 2.0 * U2(S) + 3.0 * S, U2(S) + 3.0 * S


KOEFF = {"psi2": k_psi2, "sym": k_sym, "psi1": k_psi1}


def lin_multi_k(profs, h, f_rand, dev, kfun, g, r_min=20.0):
    """wie bic2.lin_multi (gleiche Geometrie, gleiche Schluessel), Koeffizienten aus kfun(S, g)."""
    for p in profs:
        if abs(p["h"] - 0.5 * h) > 1e-12:
            raise ValueError("Profil braucht Schritt h/2")
    R = max([r_min] + [B2.radius_wo(p, f_rand * p["f0"]) for p in profs])
    K = int(math.ceil(R / h))
    K += K % 2
    rh = sorted(B2.r_halb(p) for p in profs)[len(profs) // 2]
    Km = max(2, min(K - 2, int(round(rh / h))))
    Km -= Km % 2
    dv, sv, reihe, om = [], [], [], []
    for p in profs:
        f, _ = B2.f_werte(p, 2 * K + 1)
        S = torch.tensor(f, dtype=F64) ** 2
        d_, s_, _, _ = kfun(S, g)
        dv.append(d_)
        sv.append(s_)
        s0 = p["f0"] ** 2
        S2 = 2.0 * p["f0"] * p["f2"]
        a0, b0, a1, b1 = kfun(s0, g)
        reihe.append([float(a0), float(a1) * S2, float(b0), float(b1) * S2])
        om.append(math.sqrt(p["w2"]))
    cf = [0.0] + [1.0 / (j * 0.5 * h) ** 2 for j in range(1, 2 * K + 1)]
    return {"h": h, "K": K, "Km": Km, "R_aus": K * h, "r_m": Km * h, "dvX": torch.stack(dv).to(dev),
            "svX": torch.stack(sv).to(dev), "reiheX": torch.tensor(reihe, dtype=F64, device=dev),
            "omX": torch.tensor(om, dtype=F64, device=dev), "cf": cf, "dev": dev, "n": len(profs)}


# ================================================================ natives Profil des gemischten Balls

def prof_nativ(w2, g, hp, n_kand=64, runden=9, r_max=90.0, f_schwanz=1e-5):
    """h'' + (2/r) h' = G(h), G(h) = [U'(2 h^2) - g J h^2 - omega^2] h = (a0 - c3 h^2 + 6 h^4) h, a0 = 1 - omega^2,
    c3 = 4 + g J. Schiessen in s = -ln(h_top - h(0)) (h_top: groessere Nullstelle von G/h), Klammer: Ueberschuss
    (h < 0) gegen Unterschuss (h' > 0). Rueckgabe im Profilformat von resonanz3d/bic2 mit f = sqrt(2) h."""
    a0 = 1.0 - w2
    c3 = 4.0 + g * JK
    disk = c3 * c3 - 24.0 * a0
    if disk <= 0:
        raise ValueError("kein Buckel")
    htop = math.sqrt((c3 + math.sqrt(disk)) / 12.0)

    def Gf(hh):
        return (a0 - c3 * hh * hh + 6.0 * hh ** 4) * hh

    def Gp(hh):
        return a0 - 3.0 * c3 * hh * hh + 30.0 * hh ** 4

    def start(s):
        h0 = htop - np.exp(-s)
        h2 = Gf(h0) / 6.0
        h4 = Gp(h0) * h2 / 20.0
        r = hp
        return h0, h2, h0 + h2 * r * r + h4 * r ** 4, 2.0 * h2 * r + 4.0 * h4 * r ** 3

    def rk4(r, hh, pp):
        def ab(rr, x, y):
            return y, Gf(x) - (2.0 / rr) * y
        k1h, k1p = ab(r, hh, pp)
        k2h, k2p = ab(r + 0.5 * hp, hh + 0.5 * hp * k1h, pp + 0.5 * hp * k1p)
        k3h, k3p = ab(r + 0.5 * hp, hh + 0.5 * hp * k2h, pp + 0.5 * hp * k2p)
        k4h, k4p = ab(r + hp, hh + hp * k3h, pp + hp * k3p)
        return hh + (hp / 6.0) * (k1h + 2 * k2h + 2 * k3h + k4h), pp + (hp / 6.0) * (k1p + 2 * k2p + 2 * k3p + k4p)

    lo, hi = -math.log(0.9 * htop), 30.0
    n_max = int(round(r_max / hp))
    for rnd in range(runden):
        s = np.linspace(lo, hi, n_kand)
        _, _, hh, pp = start(s)
        zust = np.zeros(n_kand)
        for k in range(1, n_max):
            hh, pp = rk4(k * hp, hh, pp)
            ueber = (zust == 0) & (hh < 0)
            unter = (zust == 0) & (hh >= 0) & (pp > 0)
            zust[ueber] = 1
            zust[unter] = -1
            hh = np.where(zust == 0, hh, 0.0)
            pp = np.where(zust == 0, pp, 0.0)
            if k % 100 == 0 and not np.any(zust == 0):
                break
        if rnd == 0 and not (zust[0] < 0 and zust[-1] > 0):
            raise ValueError(f"Klammer ungueltig: {zust[0]}, {zust[-1]}")
        if np.any(zust < 0):
            lo = max(lo, float(s[zust < 0].max()))
        if np.any(zust > 0):
            hi = min(hi, float(s[zust > 0].min()))
    s3 = np.array([lo, 0.5 * (lo + hi), hi])
    h0v, h2v, hh, pp = start(s3)
    fl, pl = [float(h0v[1])], [0.0]
    j_cut = None
    grund = 0
    for k in range(1, n_max):
        fl.append(float(hh[1]))
        pl.append(float(pp[1]))
        streu = abs(hh[2] - hh[0])
        if hh[1] < f_schwanz * h0v[1]:
            grund = 1
        elif pp[1] > 0:
            grund = 2
        elif hh[1] < 0:
            grund = 3
        elif streu > 1e-2 * abs(hh[1]):
            grund = 4
        if grund:
            j_cut = max(1, k - 1)
            break
        hh, pp = rk4(k * hp, hh, pp)
    if j_cut is None:
        j_cut = len(fl) - 1
    w = math.sqrt(2.0)
    return {"w2": w2, "dim": 3.0, "h": hp, "f": [w * v for v in fl[:j_cut + 1]], "fp": [w * v for v in pl[:j_cut + 1]],
            "j_cut": j_cut, "f0": w * float(h0v[1]), "f2": w * float(h2v[1]), "kappa": math.sqrt(a0), "dm1": 2.0,
            "r_cut": j_cut * hp, "grund": grund, "klammer": hi - lo, "htop": htop, "g": g}


def profil_fuer(art, w2, g, hp, dev):
    if art == "nativ":
        return prof_nativ(w2, g, hp)
    return B2.profil(w2, 3.0, 0.5, hp, dev)


# ================================================================ eine Stelle

def w_werte(L, rhos, ixs):
    Dw = B2.direkt_m(L, [complex(r, 0.0) for r in rhos], ixs, [1.0] * len(rhos), gram=False)
    W = [complex(float(Dw["la"][k].real), float(Dw["lb"][k].real)) for k in range(len(rhos))]
    im_rest = max(float(Dw["la"][k].imag.abs() + Dw["lb"][k].imag.abs()) / max(abs(W[k]), 1e-300)
                  for k in range(len(rhos)))
    return W, im_rest


def profile(xs, art, g, h, dev, budget, zeilen):
    out, t_max = [], 0.0
    for x in xs:
        t0 = G.uhr()
        out.append(profil_fuer(art, x, g, 0.5 * h, dev))
        t_max = max(t_max, G.uhr() - t0)
    return out, t_max


def stelle(name, a, dev, budget, zeilen):
    kname, g, x0, nu0, dnu, cgam, art = PUNKTE[name]
    # Fassung 2 (07:24, Nachtrag E): Keime und g von der Kommandozeile ueberschreibbar
    if getattr(a, "g", None) is not None:
        g = a.g
    if getattr(a, "x0", None) is not None:
        x0 = a.x0
    if getattr(a, "nu0", None) is not None:
        nu0 = a.nu0
    if getattr(a, "cgam", None) is not None:
        cgam = a.cgam
    kfun = KOEFF[kname]
    h, f_rand = a.h, a.frand
    e = {"name": name, "koeff": kname, "g": g, "x0": x0, "nu0": nu0, "h": h, "f_rand": f_rand, "profil": art}
    zeilen.append(f"=== {name}: Koeffizienten {kname}, g = {g}, Profil {art}, h = {h}, Keim x0 = {x0}, nu0 = {nu0}")
    # ---- Stufe 1
    offs = [float(v) for v in a.offs.split(",")]
    xs = sorted(x0 + o for o in offs)
    profs, t_prof = profile(xs, art, g, h, dev, budget, zeilen)
    e["t_profil_max"] = t_prof
    if art == "nativ":
        e["nativ"] = [{"x": p["w2"], "f0": p["f0"], "S0": p["f0"] ** 2, "r_cut": p["r_cut"], "grund": p["grund"],
                       "klammer": p["klammer"]} for p in profs]
        zeilen.append("  natives Profil: " + ", ".join(f"{p['w2']:.6f}: S0 {p['f0'] ** 2:.9f}, r_cut {p['r_cut']:.2f}, "
                                                        f"Grund {p['grund']}" for p in profs[:3]))
    L = lin_multi_k(profs, h, f_rand, dev, kfun, g)
    e.update({"x": xs, "R_aus": L["R_aus"], "r_m": L["r_m"], "K": L["K"]})
    zeilen.append(f"  Stufe 1: {len(xs)} Profile (je bis {t_prof:.1f} s), R = {L['R_aus']:.2f}, r_m = {L['r_m']:.3f}")
    keime = [complex(nu0 + dnu * (x - x0), -max(1e-10, cgam * (x - x0) ** 2)) for x in xs]
    pol = B2.newton_m(L, keime, list(range(len(xs))), [1.0] * len(xs), iters=a.iter_newton)
    pold = B2.newton_direkt(L, [p["rho"] for p in pol], list(range(len(xs))), [1.0] * len(xs))
    Dd = B2.direkt_m(L, [p["rho"] for p in pold], list(range(len(xs))), [1.0] * len(xs), gram=True)
    tab = []
    for i, x in enumerate(xs):
        ev = B2.eigen(Dd, i)
        tab.append({"x": x, "nu": pold[i]["rho"], "konv": pold[i]["konvergiert"], "Gamma": -pold[i]["rho"].imag,
                    "A_norm": ev["A_norm"], "Gamma_fluss": ev["Gamma_fluss"]})
        zeilen.append(f"    {x:.7f}: nu = {G.fz(pold[i]['rho'], 10)}, konv {pold[i]['konvergiert']}, "
                      f"A_norm {ev['A_norm'].real:+.4e} {ev['A_norm'].imag:+.4e}i, Gamma_Fluss {ev['Gamma_fluss']:.3e}")
    e["pole"] = tab
    e["phasentest"] = B2.phasentest(xs, [t["A_norm"] for t in tab], zeilen)
    ic = min(range(len(xs)), key=lambda i: abs(tab[i]["A_norm"]))
    rc = tab[ic]["nu"].real
    drs = [-3e-4, -1e-4, -3e-5, 0.0, 3e-5, 1e-4, 3e-4]
    innen = sorted(range(len(xs)), key=lambda i: abs(xs[i] - xs[ic]))[:3]
    pr, pi_ = [], []
    for i in innen:
        for d in drs:
            pr.append(rc + d)
            pi_.append(i)
    W, imr = w_werte(L, pr, pi_)
    nahe = [(pr[k] - rc, xs[pi_[k]] - xs[ic], W[k]) for k in range(len(pr)) if abs(pr[k] - rc) <= 1.01e-4]
    fit, grund = B2.lin_fit_nullstelle(nahe)
    if fit is None:
        zeilen.append(f"  Fit Stufe 1 nicht moeglich: {grund}")
        e["fehler"] = f"Fit 1: {grund}"
        return e
    dr0, dx0, J, res, cond = fit
    wn = {"rho": rc + dr0, "x": xs[ic] + dx0, "J": J, "fit_rest": res, "condJ": cond,
          "detJ": J[0][0] * J[1][1] - J[0][1] * J[1][0]}
    e["fit1"] = wn
    e["W_im_rest"] = imr
    zeilen.append(f"  Fit 1 (Mitte {xs[ic]:.7f}, nu {rc:.10f}): x* = {wn['x']:.9f}, nu* = {wn['rho']:.10f}, "
                  f"det J = {wn['detJ']:.3e}, cond J = {cond:.1e}, Rest {res:.1e}, |Im W|/|W| {imr:.1e}")
    # ---- Stufe 2: Rechtecke um den Fit-Mittelpunkt
    e["rechtecke"] = []
    for dx in [float(v) for v in a.dxs.split(",")]:
        zentrum = dict(wn)
        for lage in range(2):
            if not budget.ok(f"{name} dx {dx} Lage {lage}", 5 * t_prof + 40.0):
                e["rechtecke"].append({"dx": dx, "lage": lage, "fehler": "Zeit"})
                break
            xs_n = [zentrum["x"] + dx * t for t in (-1.0, -0.5, 0.0, 0.5, 1.0)]
            pn, _ = profile(xs_n, art, g, h, dev, budget, zeilen)
            L1 = lin_multi_k(pn, h, f_rand, dev, kfun, g)
            d2 = [-1e-4, -3e-5, 0.0, 3e-5, 1e-4]
            pr2 = [zentrum["rho"] + d for _ in xs_n for d in d2]
            pi2 = [i for i in range(len(xs_n)) for _ in d2]
            W2, imr2 = w_werte(L1, pr2, pi2)
            fit2, grund2 = B2.lin_fit_nullstelle([(pr2[k] - zentrum["rho"], xs_n[pi2[k]] - xs_n[2], W2[k])
                                                  for k in range(len(pr2))])
            if fit2 is None:
                zeilen.append(f"  dx {dx:.1e}, Lage {lage}: zweiter Fit nicht moeglich ({grund2})")
                e["rechtecke"].append({"dx": dx, "lage": lage, "fehler": f"Fit 2: {grund2}"})
                break
            dr2, dx2, J2, res2, cond2 = fit2
            wn2 = {"rho": zentrum["rho"] + dr2, "x": xs_n[2] + dx2, "J": J2, "fit_rest": res2, "condJ": cond2,
                   "detJ": J2[0][0] * J2[1][1] - J2[0][1] * J2[1][0]}
            zeilen.append(f"  dx {dx:.1e}, Lage {lage} um x = {xs_n[2]:.9f}: zweiter Fit x** = {wn2['x']:.9f}, "
                          f"nu** = {wn2['rho']:.10f}, det J = {wn2['detJ']:.3e}, cond {cond2:.1e}, Rest {res2:.1e}")
            ur = B2.umlauf_rechteck(L1, xs_n, 2, wn2["rho"], dx, wn2, a, zeilen, nu=1.0)
            innen_x = abs(wn2["x"] - xs_n[2]) <= 0.8 * dx
            innen_r = abs(wn2["rho"] - ur.get("rho_c", wn2["rho"])) <= 0.8 * ur.get("drho", 1.0)
            eintrag = {"dx": dx, "lage": lage, "x_mitte": xs_n[2], "fit2": wn2, "umlauf": ur.get("umlauf"),
                       "max_sprung": ur.get("max_sprung"), "aufgeloest": ur.get("aufgeloest"),
                       "min_absW": ur.get("min_absW"), "drho": ur.get("drho"), "fit2_im_rechteck": innen_x and innen_r,
                       "punkte": len(ur.get("pfad", []))}
            e["rechtecke"].append(eintrag)
            zeilen.append(f"    -> Umlauf {eintrag['umlauf']:+.4f}, aufgeloest {eintrag['aufgeloest']}, min |W| "
                          f"{eintrag['min_absW']:.3e}, Fit-Mitte im Rechteck {eintrag['fit2_im_rechteck']}")
            if innen_x:
                break
            zentrum = wn2
    return e


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kommando", choices=["rauch", "punkt"])
    ap.add_argument("--name", default="Z1")
    ap.add_argument("--h", type=float, default=0.02)
    ap.add_argument("--frand", type=float, default=1e-6)
    ap.add_argument("--offs", default="0,-5e-4,5e-4,-2e-3,2e-3")
    ap.add_argument("--dxs", default="5e-4,1e-4")
    ap.add_argument("--iter-newton", dest="iter_newton", type=int, default=20)
    ap.add_argument("--u-n", dest="u_n", type=int, default=60)
    ap.add_argument("--u-drho", dest="u_drho", type=float, default=2e-5)
    ap.add_argument("--u-drho-ohne-fit", dest="u_drho_ohne_fit", type=float, default=5e-4)
    ap.add_argument("--g", type=float, default=None, help="Fassung 2: g ueberschreiben")
    ap.add_argument("--x0", type=float, default=None, help="Fassung 2: Keim omega^2 ueberschreiben")
    ap.add_argument("--nu0", type=float, default=None, help="Fassung 2: Keim nu ueberschreiben")
    ap.add_argument("--cgam", type=float, default=None, help="Fassung 2: Keim-Breite ueberschreiben")
    ap.add_argument("--geraet", default="cpu", choices=["cpu", "cuda"])
    ap.add_argument("--out", default=None)
    ap.add_argument("--budget", type=float, default=540.0)
    a = ap.parse_args()
    torch.set_num_threads(1)
    dev = torch.device("cuda" if a.geraet == "cuda" else "cpu")
    budget = G.Budget(a.budget)
    out = a.out or os.path.join(HIER, f"ausgabe-umlauf-{a.name}")
    os.makedirs(out, exist_ok=True)
    kopf = (f"Runde 9 GF-BIC-2 umlauf {a.kommando} {a.name} Start {G.jetzt()}; gfbic_umlauf.py sha256 "
            f"{G.sha256(os.path.abspath(__file__))[:16]}, bic2.py {B2_PFAD} sha256 {G.sha256(B2_PFAD)[:16]}, "
            f"gfbic.py {G.sha256(G.__file__)[:16]}")
    zeilen = [kopf]
    print(kopf, flush=True)
    erg = {"argumente": vars(a), "start": G.jetzt()}
    rc = 0
    try:
        if a.kommando == "rauch":
            a.h, a.frand, a.offs, a.dxs, a.iter_newton, a.u_n = 0.08, 1e-5, "0,-1e-3,1e-3", "5e-4", 6, 12
            p = prof_nativ(0.75869, 0.2, 0.04)
            q = B2.profil(0.75869, 3.0, 1.0 / (2.0 * 1.05 ** 2), 0.04, dev)
            s_nat = p["f0"] ** 2
            s_b = q["f0"] ** 2 / 1.05
            zeilen.append(f"  Rauch Profil: S0 nativ {s_nat:.10f}, S0 aus beta_eff skaliert {s_b:.10f}, Differenz "
                          f"{s_nat - s_b:+.2e}")
            erg["Z1"] = stelle("Z1", a, dev, budget, zeilen)
        else:
            erg[a.name] = stelle(a.name, a, dev, budget, zeilen)
    except Exception:                                   # noqa: BLE001
        tb = traceback.format_exc()
        zeilen.append("FEHLER:\n" + tb)
        erg["fehler"] = tb
        rc = 1
    zeilen.append(f"Ende {G.jetzt()}, {G.uhr():.1f} s; entfallen: {budget.abgebrochen or 'nichts'}")
    erg["ende"] = G.jetzt()
    with open(os.path.join(out, "umlauf.json"), "w") as fh:
        json.dump(G.jsonfest(erg), fh, indent=1)
    with open(os.path.join(out, "umlauf_bericht.txt"), "w") as fh:
        fh.write("\n".join(zeilen) + "\n")
    print("\n".join(zeilen[1:]), flush=True)
    sys.exit(rc)


if __name__ == "__main__":
    main()
