# HOPF-1 Stufe B, achsensymmetrisch (2D in rho, z): Relaxation des Knotens im festen Ball-Hintergrund (phi mitgefuehrt),
# aussermittige Lage auf der Knotenachse (Schale in der Wand); d = 0 nur als Kontrolle derselben Methode.
# Autor: Claude (Code-Agent HOPF-1), 2026-09-30. Grund fuer 2D: das 3D-Gitter h = 0,1 verlor die Hopfzahl
# (L-BFGS, Lauf B-w060) bzw. lag unter der Kontinuumsschranke (Fluss, Lauf B-w060-fluss, abgebrochen).
# Achsensymmetrischer h = 1-Ansatz: n1 + i n2 = e^{i phi} (m1 + i m2), n3 = m3, m(rho, z) in S^2.
# Reduzierte Energie (Herleitung PLAN.md/ERGEBNIS.md): E = Int 2 pi rho drho dz {
#   c [|grad m|^2 + (m1^2 + m2^2)/rho^2] + (kappa/2) [(m.(d_rho m x d_z m))^2 + |grad m3|^2/rho^2]
#   + mu^2 v^2 (1 - m3) + U(S_phi + c (m1^2 + m2^2)) - U(S_phi) },  c = v^2/4.
# Hopfzahl = Grad von m: (1/4 pi) Int m.(d_rho m x d_z m) drho dz. Ballzentrum bei z = -d (Knotenachse = Ballachse).
import argparse
import json
import math
import os
import sys
import time

import numpy as np
import torch

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from hopf1 import ball, Ballfeld, knoten, U  # noqa: E402

T0 = time.time()
DT = torch.float64


def log(*a):
    print("[%7.1fs]" % (time.time() - T0), *a, flush=True)


def kreuz(a, b):
    return torch.stack([a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]])


class Gitter:
    def __init__(self, Lr, Lz, h, dev):
        self.h = h
        self.Nr = int(round(Lr / h))
        self.Nz = int(round(2 * Lz / h))
        rho = torch.tensor((np.arange(self.Nr) + 0.5) * h, dtype=DT, device=dev)
        z = torch.tensor(-Lz + (np.arange(self.Nz) + 0.5) * h, dtype=DT, device=dev)
        self.P, self.Z = torch.meshgrid(rho, z, indexing="ij")
        self.w = 2.0 * math.pi * self.P * h * h
        self.nord = torch.tensor([0.0, 0.0, 1.0], dtype=DT, device=dev).view(3, 1, 1)


def ableitungen(m, G):
    h = G.h
    mr = torch.cat([m[:, 1:, :], G.nord.expand(3, 1, m.shape[2])], dim=1)     # rho-Rand aussen: Nordpol
    mz = torch.cat([m[:, :, 1:], G.nord.expand(3, m.shape[1], 1)], dim=2)     # z-Rand oben: Nordpol
    return (mr - m) / h, (mz - m) / h


def dichten(m, Sp, G, v, kappa, mu):
    m = m / torch.sqrt((m * m).sum(0, keepdim=True))
    Dr, Dz = ableitungen(m, G)
    c = 0.25 * v * v
    s = m[0] * m[0] + m[1] * m[1]
    P2 = G.P * G.P
    e_sig = c * ((Dr * Dr).sum(0) + (Dz * Dz).sum(0) + s / P2)
    q = (m * kreuz(Dr, Dz)).sum(0)
    e_fs = 0.5 * kappa * (q * q + (Dr[2] * Dr[2] + Dz[2] * Dz[2]) / P2)
    e_mu = mu * mu * v * v * (1.0 - m[2])
    e_U = U(Sp + c * s) - U(Sp)
    return m, s, q, e_sig, e_fs, e_mu, e_U


def energie(m, Sp, G, v, kappa, mu):
    _, _, _, a, b, c0, d = dichten(m, Sp, G, v, kappa, mu)
    return ((a + b + c0 + d) * G.w).sum()


def grad_hopf(m, G):
    with torch.no_grad():
        m = m / torch.sqrt((m * m).sum(0, keepdim=True))
        Dr, Dz = ableitungen(m, G)
        return float((m * kreuz(Dr, Dz)).sum() * G.h * G.h / (4.0 * math.pi))


def relaxiere(m0, Sp, G, v, kappa, mu, schritte, dt, tmax, etikett, block=2000):
    """Arrested Newton flow: m_tt = -(dE/dm)/w (tangential), Geschwindigkeit null, sobald E steigt."""
    m = (m0 / torch.sqrt((m0 * m0).sum(0, keepdim=True))).detach()
    # Randbedingung (Regularitaet auf der Achse, Vakuum am Kastenrand): erste rho-Spalte, letzte rho-Spalte, erste und
    # letzte z-Zeile fest auf dem Nordpol. Ohne sie kippten im Rauchtest (09:13) die Achsenzellen, Grad(m) sprang auf -2.
    frei = torch.ones_like(m[0])
    frei[0, :] = 0.0
    frei[-1, :] = 0.0
    frei[:, 0] = 0.0
    frei[:, -1] = 0.0
    m = m * frei + G.nord * (1.0 - frei)
    vel = torch.zeros_like(m)
    verlauf = []
    t0 = time.time()
    E_alt = None
    stopps = 0
    for k in range(1, schritte + 1):
        m.requires_grad_(True)
        E = energie(m, Sp, G, v, kappa, mu)
        g, = torch.autograd.grad(E, m)
        with torch.no_grad():
            m = m.detach()
            E = float(E)
            if E_alt is not None and E > E_alt:
                vel.zero_()
                stopps += 1
            g = g / G.w
            gt = (g - (g * m).sum(0, keepdim=True) * m) * frei
            vel = vel - dt * gt
            vel = vel - (vel * m).sum(0, keepdim=True) * m
            m = m + dt * vel
            m = m / torch.sqrt((m * m).sum(0, keepdim=True))
        dE = None if E_alt is None else E_alt - E
        E_alt = E
        ende = (k == schritte) or (time.time() - t0 > tmax)
        if k % block == 0 or ende:
            gr = grad_hopf(m, G)
            gn = float(torch.sqrt((gt * gt * G.w).sum()))
            verlauf.append((k, E, gn, gr, stopps))
            log("%s Schritt %6d  E = %.9f  |g| = %.3e  Grad(m) = %.5f  Stopps %d" % (etikett, k, E, gn, gr, stopps))
            if abs(gr) < 0.5:
                log("%s ABBRUCH: Hopfzahl verloren" % etikett)
                break
        if ende:
            break
    log("%s Ende Schritt %d (%.1f s)" % (etikett, k, time.time() - t0))
    return m.detach(), verlauf


def relaxiere_lbfgs(m0, Sp, G, v, kappa, mu, schritte, tmax, etikett, block=200):
    """L-BFGS (strong Wolfe) auf m mit festem Rahmen (Achse, Kastenrand = Nordpol); Grad(m) je Block geprueft."""
    frei = torch.ones_like(m0[0])
    frei[0, :] = 0.0
    frei[-1, :] = 0.0
    frei[:, 0] = 0.0
    frei[:, -1] = 0.0
    m = (m0 / torch.sqrt((m0 * m0).sum(0, keepdim=True)))
    m = (m * frei + G.nord * (1.0 - frei)).detach().requires_grad_(True)
    verlauf = []
    t0 = time.time()
    k = 0
    E_alt = None
    while k < schritte and time.time() - t0 < tmax:
        opt = torch.optim.LBFGS([m], lr=1.0, max_iter=block, history_size=12, line_search_fn="strong_wolfe",
                                tolerance_grad=1e-14, tolerance_change=1e-16)

        def closure():
            opt.zero_grad()
            E = energie(m, Sp, G, v, kappa, mu)
            E.backward()
            m.grad.mul_(frei)
            return E
        opt.step(closure)
        k += block
        with torch.no_grad():
            m.data = m.data / torch.sqrt((m.data * m.data).sum(0, keepdim=True))
        E = float(energie(m, Sp, G, v, kappa, mu))
        gr = grad_hopf(m, G)
        verlauf.append((k, E, gr))
        log("%s L-BFGS it %6d  E = %.9f  Grad(m) = %.5f" % (etikett, k, E, gr))
        if abs(gr) < 0.5:
            log("%s ABBRUCH: Hopfzahl verloren" % etikett)
            break
        if E_alt is not None and abs(E_alt - E) < 1e-12 * abs(E):
            break
        E_alt = E
    log("%s Ende (%.1f s)" % (etikett, time.time() - t0))
    return m.detach(), verlauf


def diagnose(m, Sp, S0, G, v, kappa, mu):
    with torch.no_grad():
        m, s, q, a, b, c0, eU = dichten(m, Sp, G, v, kappa, mu)
        c = 0.25 * v * v
        kr = U(Sp + c * s) - U(Sp) - U(c * s)
        innen = Sp > 0.9 * S0
        aussen = Sp <= 0.1 * S0
        wand = ~innen & ~aussen
        w = G.w
        Ms = (s * w).sum()
        i = int(torch.argmin(m[2]))
        ir, iz = divmod(i, m.shape[2])
        return {"E_sigma": float((a * w).sum()), "E_FS": float((b * w).sum()), "E_mu": float((c0 * w).sum()),
                "E_U_rest": float((eU * w).sum()), "E_kreuz": float((kr * w).sum()),
                "E_kreuz_innen": float((kr * w * innen).sum()), "E_kreuz_wand": float((kr * w * wand).sum()),
                "E_kreuz_aussen": float((kr * w * aussen).sum()), "M_b": float(Ms),
                "rho_kern": float(G.P[ir, iz]), "z_kern": float(G.Z[ir, iz]), "n3_min": float(m[2].min()),
                "z_s": float((G.Z * s * w).sum() / Ms), "rho_s": float((G.P * s * w).sum() / Ms),
                "S_phi_s_durch_S0": float((Sp * s * w).sum() / Ms / S0), "grad_m": grad_hopf(m, G)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--geraet", default="cuda")
    ap.add_argument("--w2", type=float, default=0.6)
    ap.add_argument("--v", type=float, default=1.0)
    ap.add_argument("--kappa", type=float, default=1.0)
    ap.add_argument("--mu", type=float, default=1.0)
    ap.add_argument("--Lr", type=float, default=6.0)
    ap.add_argument("--Lz", type=float, default=6.0)
    ap.add_argument("--h", type=float, default=0.025)
    ap.add_argument("--start", default="1.2,0.6")
    ap.add_argument("--schritte", type=int, default=20000)
    ap.add_argument("--dt", type=float, default=0.002)
    ap.add_argument("--tmax", type=float, default=140.0)
    ap.add_argument("--d-schritt", type=float, default=0.25)
    ap.add_argument("--d-relax", default="auto,0")
    ap.add_argument("--out", default="C")
    ap.add_argument("--methode", default="lbfgs")
    a = ap.parse_args()
    if a.geraet == "cpu":
        torch.set_num_threads(1)
    dev = torch.device(a.geraet)
    r, S, info = ball(a.w2)
    S0 = info["S0"]
    Rb = info["R_ball_S0halbe"]
    G = Gitter(a.Lr, a.Lz, a.h, dev)
    log("Ball omega^2 = %.4f S0 = %.5f R(S0/2) = %.3f r(S=2/3) = %.3f E_Q = %.4f Q = %.4f; v = %.2f kappa = %.3f mu = %.3f;"
        " 2D-Kasten rho < %.1f, |z| < %.1f, h = %.4f (%d x %d), dt = %.4f"
        % (a.w2, S0, Rb, info["r_S_2/3"], info["E_Q"], info["Q"], a.v, a.kappa, a.mu, a.Lr, a.Lz, a.h, G.Nr, G.Nz, a.dt))
    bf = Ballfeld(r, S, dev)
    null = torch.zeros_like(G.P)

    def Sphi(d):
        return bf(torch.sqrt(G.P * G.P + (G.Z + d) ** 2))
    Rh, w = [float(q) for q in a.start.split(",")]
    n1, n2, n3 = knoten("A", (Rh, w), G.P, torch.zeros_like(G.P), G.Z)
    m0 = torch.stack([n1, n2, n3])
    d0 = diagnose(m0, null, S0, G, a.v, a.kappa, a.mu)
    E0 = float(energie(m0, null, G, a.v, a.kappa, a.mu))
    log("Start Ansatz A %s: E = %.6f (Sigma %.3f FS %.3f mu %.3f U %.3f) Grad(m) %.5f  [3D-Stufe-B-Gitter h = 0,1: 284,035]"
        % (a.start, E0, d0["E_sigma"], d0["E_FS"], d0["E_mu"], d0["E_U_rest"], d0["grad_m"]))
    erg = {"argv": sys.argv, "ball": info, "param": vars(a), "start": {"E": E0, "diag": d0}}
    if a.methode == "lbfgs":
        mv, vv = relaxiere_lbfgs(m0, null, G, a.v, a.kappa, a.mu, a.schritte, a.tmax, "vak ")
    else:
        mv, vv = relaxiere(m0, null, G, a.v, a.kappa, a.mu, a.schritte, a.dt, a.tmax, "vak ")
    Ev = float(energie(mv, null, G, a.v, a.kappa, a.mu))
    dv = diagnose(mv, null, S0, G, a.v, a.kappa, a.mu)
    log("Vakuumknoten: E_H = %.6f (Sigma %.3f FS %.3f mu %.3f U %.3f; Virial Sigma - FS + 3(mu + U) = %.3f) rho_kern %.3f"
        " z_kern %.3f n3_min %.4f Grad %.5f" % (Ev, dv["E_sigma"], dv["E_FS"], dv["E_mu"], dv["E_U_rest"],
                                               dv["E_sigma"] - dv["E_FS"] + 3 * (dv["E_mu"] + dv["E_U_rest"]),
                                               dv["rho_kern"], dv["z_kern"], dv["n3_min"], dv["grad_m"]))
    erg["vakuum"] = {"E_H": Ev, "diag": dv, "verlauf": vv}
    ds = np.round(np.arange(0.0, Rb + 3.0 + 1e-9, a.d_schritt), 4)
    scan = []
    with torch.no_grad():
        for d in ds:
            Sp = Sphi(float(d))
            Eb = float(energie(mv, Sp, G, a.v, a.kappa, a.mu))
            dd = diagnose(mv, Sp, S0, G, a.v, a.kappa, a.mu)
            scan.append({"d": float(d), "E_int_prod": Eb - Ev, "innen": dd["E_kreuz_innen"], "wand": dd["E_kreuz_wand"],
                         "aussen": dd["E_kreuz_aussen"], "S_phi_s_durch_S0": dd["S_phi_s_durch_S0"]})
    for q in scan[::2]:
        log("Produkt (relaxierter Knoten) d = %5.2f: E_int = %.6f (innen %.4f wand %.4f aussen %.4f) S_phi_s/S0 %.3f"
            % (q["d"], q["E_int_prod"], q["innen"], q["wand"], q["aussen"], q["S_phi_s_durch_S0"]))
    j = int(np.argmin([q["E_int_prod"] for q in scan]))
    dmin = scan[j]["d"]
    log("Minimum Produktansatz: d = %.2f E_int = %.6f; d = 0: %.6f; Mitte/Minimum = %.3f"
        % (dmin, scan[j]["E_int_prod"], scan[0]["E_int_prod"], scan[0]["E_int_prod"] / scan[j]["E_int_prod"]))
    erg["produkt_scan"] = scan
    erg["produkt_min"] = {"d": dmin, "E_int": scan[j]["E_int_prod"], "E_int_d0": scan[0]["E_int_prod"]}
    erg["relax"] = []
    for tok in a.d_relax.split(","):
        d = dmin if tok == "auto" else float(tok)
        Sp = Sphi(d)
        Eprod = float(energie(mv, Sp, G, a.v, a.kappa, a.mu)) - Ev
        if a.methode == "lbfgs":
            mb, vb = relaxiere_lbfgs(mv, Sp, G, a.v, a.kappa, a.mu, a.schritte, a.tmax, "d=%.2f" % d)
        else:
            mb, vb = relaxiere(mv, Sp, G, a.v, a.kappa, a.mu, a.schritte, a.dt, a.tmax, "d=%.2f" % d)
        Eb = float(energie(mb, Sp, G, a.v, a.kappa, a.mu))
        Es = float(energie(mb, null, G, a.v, a.kappa, a.mu))
        db = diagnose(mb, Sp, S0, G, a.v, a.kappa, a.mu)
        nb = {}
        with torch.no_grad():
            for dd_ in (d - 0.5, d - 0.25, d + 0.25, d + 0.5):
                if dd_ >= 0:
                    nb["%.2f" % dd_] = float(energie(mb, Sphi(dd_), G, a.v, a.kappa, a.mu)) - Ev
        log("Relaxiert bei d = %.2f: E_int_rel = %.6f (Produkt %.6f) = Verformung %.6f + Kreuz %.6f (innen %.4f wand %.4f"
            " aussen %.4f); Kern rho %.3f z %.3f (Vakuum %.3f / %.3f); z_s %.4f (Vakuum %.4f); S_phi_s/S0 %.3f; Grad %.5f"
            % (d, Eb - Ev, Eprod, Es - Ev, db["E_kreuz"], db["E_kreuz_innen"], db["E_kreuz_wand"], db["E_kreuz_aussen"],
               db["rho_kern"], db["z_kern"], dv["rho_kern"], dv["z_kern"], db["z_s"], dv["z_s"], db["S_phi_s_durch_S0"],
               db["grad_m"]))
        log("   relaxierter Knoten an Nachbarlagen (E - E_H): %s" % json.dumps(nb))
        erg["relax"].append({"d": d, "E_int_rel": Eb - Ev, "E_int_prod": Eprod, "Verformung": Es - Ev, "diag": db,
                             "verlauf": vb, "nachbarlagen": nb})

    def ohne_nan(o):
        if isinstance(o, float):
            return o if math.isfinite(o) else None
        if isinstance(o, dict):
            return {q: ohne_nan(w_) for q, w_ in o.items()}
        if isinstance(o, (list, tuple)):
            return [ohne_nan(w_) for w_ in o]
        return o
    with open(a.out + ".json", "w") as fh:
        json.dump(ohne_nan(erg), fh, indent=1, allow_nan=False)
    log("geschrieben", a.out + ".json")


if __name__ == "__main__":
    main()
