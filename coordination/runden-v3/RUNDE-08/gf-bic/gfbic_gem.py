#!/usr/bin/env python3
"""Runde 8, Karte GF-BIC, Nachtrag A (PLAN.md): gemischter Ball psi_1 = psi_2 = h e^{-i omega t} (g > 0, J = 1).
Code begonnen 2026-09-30 06:26:38 CEST (date). Explorativ. Importiert gfbic.py (unveraendert) und resonanz3d.py.

- Symmetrischer Sektor = N = 1 mit U_eff = U - g J S^2/4 (S = 2 h^2); im ODE-Format dp = U' + S U'' - g J S,
  sp = S U'' - g J S/2. Nach S' = b S die beta-Familie mit beta_eff = 1/(2 b^2), b = 1 + g J/4 (Profil daraus).
- Antisymmetrischer Sektor: dp = U'(S) + g J S, sp = -g J S/2 (bei eps = 0).
- Floquet des antisymmetrischen Sektors mit der symmetrischen Atmungsmode an einer stillen Stelle als Pumpe:
  eta_tt - 2 i omega eta_t + [-Lap + U'(2|H|^2) + 2 g J |H|^2 - omega^2] eta - g J H^2 eta^* = 0, H = h + eps xi,
  xi = a e^{-i rho t} + b e^{i rho t} je Komponente, normiert max|a + b| = 1.
Kommandos: rauch | gemischt
"""
import argparse
import json
import math
import os
import sys
import traceback

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import numpy as np  # noqa: E402
import scipy.linalg as sla  # noqa: E402
import scipy.sparse as sps  # noqa: E402
import scipy.sparse.linalg as spla  # noqa: E402
import torch  # noqa: E402

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import gfbic as G  # noqa: E402

R3 = G.R3
F64 = torch.float64
JK = G.JK
BETA = G.BETA
# (Name, g, omega^2, rho*-Keim, rho* bekannt?)  beta_eff = 0,45 -> g = 0,216370; 0,40 -> g = 0,472136
PUNKTE = {"M1": (4.0 * (1.0 / math.sqrt(0.9) - 1.0), 0.755738, 1.72, False),
          "M2": (4.0 * (1.0 / math.sqrt(0.9) - 1.0), 0.577365, 1.602162, True),
          "M3": (4.0 * (1.0 / math.sqrt(0.8) - 1.0), 0.566347, 1.583776, True)}


def profil_gemischt(w2, g, hp, dev):
    """Profil S_tot(r) = 2 h^2 des gemischten Balls aus der beta_eff-Familie (f' = sqrt(b) sqrt(S_tot))."""
    b = 1.0 + g * JK / 4.0
    beta_eff = 1.0 / (2.0 * b * b)
    prof = R3.profil(w2, 3.0, beta_eff, hp, dev)
    s = 1.0 / math.sqrt(b)
    p2 = dict(prof)
    p2["f"] = [x * s for x in prof["f"]]
    p2["fp"] = [x * s for x in prof["fp"]]
    p2["f0"] = prof["f0"] * s
    p2["f2"] = prof["f2"] * s
    return p2, beta_eff, b


def koeff_gem(sektor, S, g):
    if sektor == "sym":
        return G.U1(S) + S * G.U2(S) - g * JK * S, S * G.U2(S) - 0.5 * g * JK * S
    if sektor == "anti":
        return G.U1(S) + g * JK * S, -0.5 * g * JK * S
    raise ValueError(sektor)


def pencil(r, S, w, delta, dp, spv):
    M = len(r)
    haupt = 2.0 / delta ** 2 + dp - w * w
    neben = -np.ones(M - 1) / delta ** 2
    Kaa = sps.diags([neben, haupt, neben], [-1, 0, 1], format="csr")
    C = sps.diags(spv, 0, format="csr")
    K0 = sps.bmat([[Kaa, C], [C, Kaa]], format="csr")
    Gam = sps.diags(np.concatenate([2.0 * w * np.ones(M), -2.0 * w * np.ones(M)]), 0, format="csr")
    I2 = sps.identity(2 * M, format="csr")
    return sps.bmat([[None, I2], [K0, -Gam]], format="csc")


def pumpe_sym(r, S, w, delta, g, rho_keim, R_loc):
    dp, spv = koeff_gem("sym", S, g)
    A = pencil(r, S, w, delta, dp, spv)
    ev, V = spla.eigs(A.astype(complex), k=10, sigma=complex(rho_keim), which="LM")
    M = len(r)
    innen = np.concatenate([r < R_loc, r < R_loc])
    kand = []
    for i in range(len(ev)):
        x = V[:2 * M, i]
        loc = float(np.sum(np.abs(x[innen]) ** 2) / np.sum(np.abs(x) ** 2))
        kand.append((loc, i))
    kand.sort(reverse=True)
    loc, i = kand[0]
    x = V[:2 * M, i]
    j = int(np.argmax(np.abs(x)))
    x = x * (abs(x[j]) / x[j])
    im_rest = float(np.max(np.abs(x.imag)) / np.max(np.abs(x.real)))
    x = x.real
    a_, b_ = x[:M] / r, x[M:] / r
    s_ = a_ + b_
    k = int(np.argmax(np.abs(s_)))
    nrm = s_[k]
    return {"rho": complex(ev[i]), "loc": loc, "im_rest": im_rest, "a": a_ / nrm, "b": b_ / nrm,
            "kandidaten": [(float(l_), complex(ev[i_])) for l_, i_ in kand]}


def monodromie_anti(r, S, w, delta, rho, g, eps, a_, b_, sigma, nt, dev):
    """Monodromie des antisymmetrischen Sektors, eta = p + i q, P = r p, Q = r q.
    D - w^2 = base0 + eps cos * Dmod, C_r = Cr0 + eps cos * Crmod, C_i = eps sin * Cimod (C = g J H^2)."""
    M = len(r)
    h = np.sqrt(0.5 * S)
    t = lambda x: torch.tensor(x, dtype=F64, device=dev).unsqueeze(1)
    base0 = t(G.U1(S) + 2.0 * g * JK * h * h - w * w)
    Dmod = t(G.U2(S) * 4.0 * h * (a_ + b_) + 4.0 * g * JK * h * (a_ + b_))
    Cr0 = t(g * JK * h * h)
    Crmod = t(g * JK * 2.0 * h * (a_ + b_))
    Cimod = t(g * JK * 2.0 * h * (b_ - a_))
    sig = t(sigma)
    n = 4 * M
    Y = torch.eye(n, dtype=F64, device=dev)
    T = 2.0 * math.pi / rho
    dt = T / nt
    inv_d2 = 1.0 / delta ** 2

    def lap(X):
        out = -2.0 * X
        out[1:] += X[:-1]
        out[:-1] += X[1:]
        return out * inv_d2

    def rhs(tt, Y):
        P, Q, Pt, Qt = Y[:M], Y[M:2 * M], Y[2 * M:3 * M], Y[3 * M:]
        c, s_ = math.cos(rho * tt), math.sin(rho * tt)
        Dm = base0 + (eps * c) * Dmod
        Cr = Cr0 + (eps * c) * Crmod
        Ci = (eps * s_) * Cimod
        dPt = -2.0 * w * Qt + lap(P) - (Dm - Cr) * P + Ci * Q - sig * (Pt + w * Q)
        dQt = 2.0 * w * Pt + lap(Q) - (Dm + Cr) * Q + Ci * P - sig * (Qt - w * P)
        return torch.cat([Pt, Qt, dPt, dQt], 0)

    tt = 0.0
    for _ in range(nt):
        k1 = rhs(tt, Y)
        k2 = rhs(tt + 0.5 * dt, Y + (0.5 * dt) * k1)
        k3 = rhs(tt + 0.5 * dt, Y + (0.5 * dt) * k2)
        k4 = rhs(tt + dt, Y + dt * k3)
        Y = Y + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        tt += dt
    mu = np.linalg.eigvals(Y.cpu().numpy())
    return mu, np.log(np.abs(mu)) / T, T


def punkt(name, a, dev, budget, zeilen):
    g, w2, rho_keim, bekannt = PUNKTE[name]
    om = math.sqrt(w2)
    prof, beta_eff, b = profil_gemischt(w2, g, a.hp, dev)
    n = int(R3.radius_wo(prof, 1e-13 * prof["f0"]) / a.hp) + 2
    fz_, _ = R3.f_werte(prof, n)
    fz_ = np.array(fz_)
    rr = a.hp * np.arange(n)
    wq = np.full(n, a.hp)
    wq[0] = wq[-1] = 0.5 * a.hp
    h2 = 0.5 * fz_ ** 2
    N2h = float(np.sum(wq * h2 * rr ** 2))
    N4h = float(np.sum(wq * h2 ** 2 * rr ** 2))
    alpha = 2.0 * g * JK * N4h / N2h
    nu0_2 = math.sqrt(0.5 * (3.0 * alpha + 4.0 * w2 - math.sqrt((3.0 * alpha + 4.0 * w2) ** 2 - 8.0 * alpha ** 2)))
    R_halb = R3.r_halb(prof)
    Rbox = max(a.rbox, R_halb + 30.0)
    R_loc = R_halb + 12.0
    r, f = G.fd_gitter(prof, a.hp, a.dfd, Rbox)
    S = f ** 2
    e = {"g": g, "beta_eff": beta_eff, "b": b, "omega2": w2, "S0_tot": prof["f0"] ** 2, "R_halb": R_halb,
         "alpha": alpha, "nu0_2moden": nu0_2, "R_kasten": Rbox, "M": len(r)}
    zeilen.append(f"=== {name}: g = {g:.6f} (beta_eff = {beta_eff:.6f}, b = {b:.6f}), omega^2 = {w2}, S0_tot = "
                  f"{e['S0_tot']:.6f}, R_halb = {R_halb:.4f}; Zwei-Moden nu_0 = {nu0_2:.8f} (alpha {alpha:.6e})")
    # ---- statisches Spektrum des antisymmetrischen Sektors (FD dicht)
    dp, spv = koeff_gem("anti", S, g)
    A = pencil(r, S, om, a.dfd, dp, spv).toarray()
    ev, V = sla.eig(A)
    M = len(r)
    x = V[:2 * M, :]
    innen = np.concatenate([r < R_loc, r < R_loc])
    loc = np.sum(np.abs(x[innen, :]) ** 2, axis=0) / np.maximum(np.sum(np.abs(x) ** 2, axis=0), 1e-300)
    inst = sorted([complex(z) for z in ev if z.imag > 1e-7], key=lambda z: -z.imag)
    kante = 1.0 - om
    geb = sorted(float(z.real) for z, lc in zip(ev, loc) if abs(z.imag) <= 1e-7 and 0.0 <= z.real < kante - 1e-4
                 and lc > 0.9)
    nb_ = -np.ones(M - 1) / a.dfd ** 2
    diag0 = 2.0 / a.dfd ** 2 + G.U1(S) - w2
    # L_eff = -Lap + U'(S) - g J S/2 - w^2 hat h als Nullmode (Kontrolle der Skalierung); L_p = + g J S/2, L_q = + 3 g J S/2
    Leff = sla.eigh_tridiagonal(diag0 - 0.5 * g * JK * S, nb_, select="i", select_range=(0, 1), eigvals_only=True)
    Lp = sla.eigh_tridiagonal(diag0 + 0.5 * g * JK * S, nb_, select="i", select_range=(0, 1), eigvals_only=True)
    Lq = sla.eigh_tridiagonal(diag0 + 1.5 * g * JK * S, nb_, select="i", select_range=(0, 1), eigvals_only=True)
    e["anti"] = {"instabil": inst, "gebunden": geb, "Leff_klein": Leff.tolist(), "Lp_klein": Lp.tolist(),
                 "Lq_klein": Lq.tolist()}
    zeilen.append(f"  antisymmetrisch (FD Delta {a.dfd}, R {Rbox:.1f}, M {M}): instabil {[G.fz(z, 8) for z in inst[:3]]}; "
                  f"gebunden 0 <= nu < 1 - omega = {kante:.6f}: {[round(v, 8) for v in geb]}; kleinste Eigenwerte "
                  f"L_eff {[f'{v:.3e}' for v in Leff]} (Nullmode h), L_p {[f'{v:.4e}' for v in Lp]}, "
                  f"L_q {[f'{v:.4e}' for v in Lq]}")
    if geb:
        zeilen.append(f"  nu_0 (FD) / nu_0 (Zwei-Moden) = {geb[0] / nu0_2:.6f}")
    # ---- Pumpe: symmetrische Atmungsmode
    pm = pumpe_sym(r, S, om, a.dfd, g, rho_keim, R_loc)
    rho = pm["rho"].real
    e["pumpe"] = {"rho": pm["rho"], "loc": pm["loc"], "im_rest": pm["im_rest"], "kandidaten": pm["kandidaten"][:5]}
    zeilen.append(f"  Pumpe (symmetrisch, N = 1 mit U_eff): rho_FD = {G.fz(pm['rho'], 8)} (Keim {rho_keim}, "
                  f"bekannt {bekannt}), Lokalisierung {pm['loc']:.6f}; Kandidaten "
                  f"{[(round(l_, 4), round(z.real, 5)) for l_, z in pm['kandidaten'][:4]]}")
    if geb:
        zeilen.append(f"  Summenresonanz: rho - nu_0 = {rho - geb[0]:.6f} (Kanal a offen ab {kante:.6f}: "
                      f"{'ja' if rho - geb[0] > kante else 'nein'})")
    sigma = np.where(r > Rbox - a.lsp, a.sig0 * ((r - (Rbox - a.lsp)) / a.lsp) ** 2, 0.0)
    nt = int(math.ceil((2.0 * math.pi / rho) / (a.dtfak * a.dfd)))
    e["nt"] = nt
    e["laeufe"] = []
    for eps in [float(v) for v in a.eps.split(",")]:
        if not budget.ok(f"{name} eps {eps}", a.reserve):
            continue
        t0 = G.uhr()
        mu, raten, T = monodromie_anti(r, S, om, a.dfd, rho, g, eps, pm["a"], pm["b"], sigma, nt, dev)
        o = np.argsort(-raten)
        top = [(float(raten[i]), complex(mu[i])) for i in o[:6]]
        lauf = {"eps": eps, "top": top, "n_instabil": int(np.sum(raten > a.schwelle)), "sek": G.uhr() - t0}
        if geb:
            # Multiplikator der Pseudo-Goldstone-Mode: exp(-i nu_0 T) (bzw. konjugiert); naechster zu dieser Stelle
            ziel = np.exp(-1j * geb[0] * T)
            iz = [int(np.argmin(np.abs(mu - ziel))), int(np.argmin(np.abs(mu - np.conj(ziel))))]
            lauf["rate_nu0"] = [float(raten[i]) for i in iz]
        e["laeufe"].append(lauf)
        zeilen.append(f"  eps = {eps:+.4f}: groesste Raten {[round(v[0], 10) for v in top[:4]]}, n(Rate > {a.schwelle:g}) "
                      f"= {lauf['n_instabil']}" + (f", Rate an nu_0: {[round(v, 10) for v in lauf['rate_nu0']]}"
                                                   if 'rate_nu0' in lauf else "") + f" ({lauf['sek']:.1f} s)")
    return e


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kommando", choices=["rauch", "gemischt"])
    ap.add_argument("--punkte", default="M1,M2,M3")
    ap.add_argument("--eps", default="0,0.01,0.02,-0.02,0.04")
    ap.add_argument("--hp", type=float, default=0.01)
    ap.add_argument("--dfd", type=float, default=0.1)
    ap.add_argument("--rbox", type=float, default=40.0)
    ap.add_argument("--lsp", type=float, default=12.0)
    ap.add_argument("--sig0", type=float, default=1.5)
    ap.add_argument("--dtfak", type=float, default=0.5)
    ap.add_argument("--schwelle", type=float, default=1e-6)
    ap.add_argument("--reserve", type=float, default=30.0)
    ap.add_argument("--geraet", default="cpu", choices=["cpu", "cuda"])
    ap.add_argument("--out", default=None)
    ap.add_argument("--budget", type=float, default=540.0)
    a = ap.parse_args()
    if a.geraet == "cuda":
        dev = torch.device("cuda")
    else:
        torch.set_num_threads(1)
        dev = torch.device("cpu")
    budget = G.Budget(a.budget)
    out = a.out or os.path.join(HIER, f"ausgabe-{a.kommando}")
    os.makedirs(out, exist_ok=True)
    kopf = (f"Runde 8 GF-BIC gemischt {a.kommando} Start {G.jetzt()}, Geraet {a.geraet}; gfbic_gem.py sha256 "
            f"{G.sha256(os.path.abspath(__file__))[:16]}, gfbic.py {G.sha256(G.__file__)[:16]}, resonanz3d.py "
            f"{G.sha256(G.R3_PFAD)[:16]}")
    zeilen = [kopf]
    print(kopf, flush=True)
    erg = {"argumente": vars(a), "start": G.jetzt(), "ergebnisse": {}}
    rc = 0
    try:
        if a.kommando == "rauch":
            a.hp, a.dfd, a.eps = 0.02, 0.2, "0,0.04"
            erg["ergebnisse"]["M2"] = punkt("M2", a, dev, budget, zeilen)
        else:
            for nm in a.punkte.split(","):
                erg["ergebnisse"][nm] = punkt(nm, a, dev, budget, zeilen)
                with open(os.path.join(out, "gemischt.json"), "w") as fh:
                    json.dump(G.jsonfest(erg), fh, indent=1)
    except Exception:                                   # noqa: BLE001
        tb = traceback.format_exc()
        zeilen.append("FEHLER:\n" + tb)
        erg["fehler"] = tb
        rc = 1
    zeilen.append(f"Ende {G.jetzt()}, {G.uhr():.1f} s; entfallen: {budget.abgebrochen or 'nichts'}")
    erg["ende"] = G.jetzt()
    with open(os.path.join(out, f"{a.kommando}.json"), "w") as fh:
        json.dump(G.jsonfest(erg), fh, indent=1)
    with open(os.path.join(out, f"{a.kommando}_bericht.txt"), "w") as fh:
        fh.write("\n".join(zeilen) + "\n")
    print("\n".join(zeilen[1:]), flush=True)
    sys.exit(rc)


if __name__ == "__main__":
    main()
