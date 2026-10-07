# HOPF-1 Stufe B: kurze Relaxation des Knotens n im festen Ball-Hintergrund (phi mitgefuehrt, nicht relaxiert),
# aussermittige Lage (Schale in der Wand). Abstimmung Leitung/Codex 30.09.: die zentrierte Relaxation mit
# Ladungsoptimierung rechnet Codex; d = 0 laeuft hier nur als Kontrolle mit derselben Methode.
# Autor: Claude (Code-Agent HOPF-1), 2026-09-30. Plan: PLAN.md Abschnitt 4. Nur auf der .69 ueber kleintest.sh.
# Geometrie: Kasten um das Knotenzentrum (periodisch), Knotenachse z; Ballzentrum bei (0, 0, -d), also auf der
# Knotenachse (koaxial, gJ-Integral exakt null, hier weggelassen). Normzwang ueber n = m/|m|; L-BFGS auf m.
# E[n] = Int c (grad n)^2 + (kappa/2) sum_{i<j} H_ij^2 + mu^2 v^2 (1 - n3) + U(S_phi + c s) - U(S_phi),
#   c = v^2/4, s = n1^2 + n2^2; Vakuum: S_phi = 0.
# E_int_prod(d) = E_ball,d[n*_vak] - E_vak[n*_vak]; E_int_rel(d) = E_ball,d[n*_d] - E_vak[n*_vak].
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


def dichten(m, Sp, h, v, kappa, mu):
    n = m / torch.sqrt((m * m).sum(0, keepdim=True))
    D = [(torch.roll(n, -1, dims=1 + i) - n) / h for i in range(3)]      # Vorwaertsdifferenzen, periodisch
    e2 = sum((d * d).sum(0) for d in D)
    H01 = (n * kreuz(D[0], D[1])).sum(0)
    H02 = (n * kreuz(D[0], D[2])).sum(0)
    H12 = (n * kreuz(D[1], D[2])).sum(0)
    e4 = H01 * H01 + H02 * H02 + H12 * H12
    c = 0.25 * v * v
    s = n[0] * n[0] + n[1] * n[1]
    eU = U(Sp + c * s) - U(Sp)
    e0 = mu * mu * v * v * (1.0 - n[2])
    return n, s, c * e2, 0.5 * kappa * e4, e0, eU


def energie(m, Sp, h, v, kappa, mu):
    n, s, a, b, c0, d = dichten(m, Sp, h, v, kappa, mu)
    return (a + b + c0 + d).sum() * h ** 3


def relaxiere(m0, Sp, h, v, kappa, mu, iters, tmax, etikett, dt=0.01, block=250):
    """Arrested Newton flow (Battye-Sutcliffe): n_tt = -(dE/dn)_tangential / h^3, Geschwindigkeit auf null, sobald E steigt.
    Kleine Schritte statt L-BFGS: L-BFGS sprang in Lauf B-w060 (09:05) ueber die Gitterbarriere, der Knoten entwickelte
    sich ab (E -> 0, Hopfzahl 0). Hopfzahl wird je Block geprueft; faellt |h| unter 0,5, bricht die Relaxation ab."""
    n = (m0 / torch.sqrt((m0 * m0).sum(0, keepdim=True))).detach()
    vel = torch.zeros_like(n)
    verlauf = []
    t0 = time.time()
    E_alt = None
    stopps = 0
    for k in range(1, iters + 1):
        n.requires_grad_(True)
        E = energie(n, Sp, h, v, kappa, mu)
        g, = torch.autograd.grad(E, n)
        with torch.no_grad():
            n = n.detach()
            E = float(E)
            if E_alt is not None and E > E_alt:
                vel.zero_()
                stopps += 1
            g = g / h ** 3
            gt = g - (g * n).sum(0, keepdim=True) * n
            vel = vel - dt * gt
            vel = vel - (vel * n).sum(0, keepdim=True) * n
            n = n + dt * vel
            n = n / torch.sqrt((n * n).sum(0, keepdim=True))
        E_alt = E
        if k % block == 0 or k == iters or time.time() - t0 > tmax:
            gn = float(torch.sqrt((gt * gt).sum()) * h ** 1.5)
            H, F = hopfzahl_feld(n, h)
            verlauf.append((k, E, gn, H, stopps))
            log("%s Schritt %5d  E = %.9f  |grad_t| = %.3e  Hopfzahl %.4f (Fluss %.4f)  Stopps %d"
                % (etikett, k, E, gn, H, F, stopps))
            if abs(F) < 0.5:
                log("%s ABBRUCH: Hopfzahl verloren" % etikett)
                break
            if time.time() - t0 > tmax:
                break
    log("%s Ende Schritt %5d  E = %.9f  (%.1f s)" % (etikett, k, verlauf[-1][1], time.time() - t0))
    return n.detach(), verlauf


def relaxiere_lbfgs(m0, Sp, h, v, kappa, mu, iters, tmax, etikett, block=100):
    m = m0.clone().detach().requires_grad_(True)
    verlauf = []
    t0 = time.time()
    it = 0
    E_alt = None
    while it < iters and time.time() - t0 < tmax:
        opt = torch.optim.LBFGS([m], lr=1.0, max_iter=block, history_size=10, line_search_fn="strong_wolfe",
                                tolerance_grad=1e-12, tolerance_change=1e-15)

        def closure():
            opt.zero_grad()
            E = energie(m, Sp, h, v, kappa, mu)
            E.backward()
            return E
        opt.step(closure)
        it += block
        with torch.no_grad():
            m.data = m.data / torch.sqrt((m.data * m.data).sum(0, keepdim=True))
        m.grad = None
        Eg = energie(m, Sp, h, v, kappa, mu)
        Eg.backward()
        E = float(Eg)
        with torch.no_grad():
            g = m.grad
            gt = g - (g * m.data).sum(0, keepdim=True) * m.data
            gn = float(torch.sqrt((gt * gt).sum()) / h ** 1.5)
        m.grad = None
        verlauf.append((it, E, gn))
        if len(verlauf) % 5 == 1:
            log("%s it %5d  E = %.9f  |grad_t|/h^1.5 = %.3e" % (etikett, it, E, gn))
        if E_alt is not None and abs(E_alt - E) < 1e-11 * abs(E):
            break
        E_alt = E
    log("%s Ende it %5d  E = %.9f  |grad_t|/h^1.5 = %.3e  (%.1f s)" % (etikett, it, verlauf[-1][1], verlauf[-1][2],
                                                                      time.time() - t0))
    return m.detach(), verlauf


def hopfzahl_feld(m, h):
    """Whitehead-Integral (1/16 pi^2) Int A.B, curl A = B per FFT, zentrale Differenzen; Kontrolle gegen Gitterkollaps"""
    with torch.no_grad():
        n = m / torch.sqrt((m * m).sum(0, keepdim=True))
        N = n.shape[1]

        def d(f, ax):
            return (torch.roll(f, -1, ax) - torch.roll(f, 1, ax)) / (2.0 * h)
        D = [d(n, 1 + i) for i in range(3)]
        Bx = (n * kreuz(D[1], D[2])).sum(0)
        By = (n * kreuz(D[2], D[0])).sum(0)
        Bz = (n * kreuz(D[0], D[1])).sum(0)
        k = torch.fft.fftfreq(N, d=h).to(n.device).to(DT) * 2.0 * math.pi
        KX, KY, KZ = torch.meshgrid(k, k, k, indexing="ij")
        K2 = KX * KX + KY * KY + KZ * KZ
        K2[0, 0, 0] = 1.0
        bx, by, bz = torch.fft.fftn(Bx), torch.fft.fftn(By), torch.fft.fftn(Bz)
        ax_ = 1j * (KY * bz - KZ * by) / K2
        ay_ = 1j * (KZ * bx - KX * bz) / K2
        az_ = 1j * (KX * by - KY * bx) / K2
        for q in (ax_, ay_, az_):
            q[0, 0, 0] = 0.0
        Ax, Ay, Az = torch.fft.ifftn(ax_).real, torch.fft.ifftn(ay_).real, torch.fft.ifftn(az_).real
        H = float((Ax * Bx + Ay * By + Az * Bz).sum() * h ** 3 / (16.0 * math.pi ** 2))
        fluss = float(By[N // 2:, N // 2, :].sum() * h * h / (4.0 * math.pi))
    return H, fluss


def diagnose(m, Sp, S0, X, Y, Z, h, v, kappa, mu):
    with torch.no_grad():
        n, s, a, b, c0, eU = dichten(m, Sp, h, v, kappa, mu)
        c = 0.25 * v * v
        rho = torch.sqrt(X * X + Y * Y)
        Ms = s.sum()
        kern = torch.clamp(-n[2] - 0.8, min=0.0)                    # Gewicht nahe Suedpol (Kernring)
        kr = U(Sp + c * s) - U(Sp) - U(c * s)
        innen = Sp > 0.9 * S0
        aussen = Sp <= 0.1 * S0
        wand = ~innen & ~aussen
        w3 = h ** 3
        ks = float(kern.sum())
        return {"E_sigma": float(a.sum() * w3), "E_FS": float(b.sum() * w3), "E_mu": float(c0.sum() * w3),
                "E_U_rest": float(eU.sum() * w3), "E_kreuz": float(kr.sum() * w3),
                "E_kreuz_innen": float((kr * innen).sum() * w3), "E_kreuz_wand": float((kr * wand).sum() * w3),
                "E_kreuz_aussen": float((kr * aussen).sum() * w3),
                "M_b": float(Ms * w3), "rho_s": float((rho * s).sum() / Ms), "z_s": float((Z * s).sum() / Ms),
                "S_phi_s_durch_S0": float((Sp * s).sum() / Ms / S0),
                "rho_kern": float((rho * kern).sum() / ks) if ks > 0 else float("nan"),
                "z_kern": float((Z * kern).sum() / ks) if ks > 0 else float("nan"), "n3_min": float(n[2].min()),
                "s2_durch_s": float((s * s).sum() / Ms)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--geraet", default="cuda")
    ap.add_argument("--w2", type=float, default=0.6)
    ap.add_argument("--v", type=float, default=1.0)
    ap.add_argument("--kappa", type=float, default=1.0)
    ap.add_argument("--mu", type=float, default=1.0)
    ap.add_argument("--L", type=float, default=5.0)
    ap.add_argument("--N", type=int, default=100)
    ap.add_argument("--start", default="1.0,0.5", help="Ansatz A: R_h,w")
    ap.add_argument("--d-schritt", type=float, default=0.25)
    ap.add_argument("--d-relax", default="auto,0", help="Lagen fuer die Ball-Relaxation; auto = Minimum von E_int_prod(d)")
    ap.add_argument("--iters", type=int, default=4000)
    ap.add_argument("--dt", type=float, default=0.008)
    ap.add_argument("--tmax", type=float, default=120.0)
    ap.add_argument("--out", default="B")
    a = ap.parse_args()
    if a.geraet == "cpu":
        torch.set_num_threads(1)
    dev = torch.device(a.geraet)
    if a.geraet == "cuda":
        log("GPU", torch.cuda.get_device_name(0), "frei/gesamt [MB]", [int(q / 2 ** 20) for q in torch.cuda.mem_get_info()])
    r, S, info = ball(a.w2)
    S0 = info["S0"]
    Rb = info["R_ball_S0halbe"]
    h = 2.0 * a.L / a.N
    log("Ball omega^2 = %.4f S0 = %.5f R(S0/2) = %.3f r(S=2/3) = %.3f E_Q = %.4f Q = %.4f; v = %.2f kappa = %.3f mu = %.3f;"
        " Kasten um den Knoten L = %.2f N = %d h = %.4f" % (a.w2, S0, Rb, info["r_S_2/3"], info["E_Q"], info["Q"], a.v,
                                                            a.kappa, a.mu, a.L, a.N, h))
    bf = Ballfeld(r, S, dev)
    x = torch.tensor(-a.L + (np.arange(a.N) + 0.5) * h, dtype=DT, device=dev)
    X, Y, Z = torch.meshgrid(x, x, x, indexing="ij")
    null = torch.zeros_like(X)

    def Sphi(d):
        return bf(torch.sqrt(X * X + Y * Y + (Z + d) ** 2))
    erg = {"argv": sys.argv, "ball": info, "param": vars(a), "h": h}
    Rh, w = [float(q) for q in a.start.split(",")]
    n1, n2, n3 = knoten("A", (Rh, w), X, Y, Z)
    m0 = torch.stack([n1, n2, n3])
    E0 = float(energie(m0, null, h, a.v, a.kappa, a.mu))
    d0 = diagnose(m0, null, S0, X, Y, Z, h, a.v, a.kappa, a.mu)
    log("Start Ansatz A %s: E_vak = %.6f (Sigma %.3f FS %.3f mu %.3f U %.3f) rho_kern %.3f" % (a.start, E0, d0["E_sigma"],
        d0["E_FS"], d0["E_mu"], d0["E_U_rest"], d0["rho_kern"]))
    mv, verl_v = relaxiere(m0, null, h, a.v, a.kappa, a.mu, a.iters, a.tmax, "vak ", dt=a.dt)
    Ev = float(energie(mv, null, h, a.v, a.kappa, a.mu))
    dv = diagnose(mv, null, S0, X, Y, Z, h, a.v, a.kappa, a.mu)
    log("Vakuumknoten: E_H = %.6f (Sigma %.3f FS %.3f mu %.3f U %.3f) rho_kern %.3f z_kern %.4f rho_s %.3f n3_min %.4f"
        " <s^2>/<s> %.3f" % (Ev, dv["E_sigma"], dv["E_FS"], dv["E_mu"], dv["E_U_rest"], dv["rho_kern"], dv["z_kern"],
                             dv["rho_s"], dv["n3_min"], dv["s2_durch_s"]))
    H0, F0 = hopfzahl_feld(m0, h)
    Hv, Fv = hopfzahl_feld(mv, h)
    log("Hopfzahl Start %.4f (Fluss %.4f), relaxiert %.4f (Fluss %.4f)" % (H0, F0, Hv, Fv))
    erg["vakuum"] = {"E_H": Ev, "diag": dv, "verlauf": verl_v, "E_start_ansatz": E0, "hopf_start": [H0, F0],
                     "hopf_relaxiert": [Hv, Fv]}

    # Produktansatz mit relaxiertem Knoten, Verschiebung entlang der Achse
    ds = np.round(np.arange(0.0, Rb + 3.0 + 1e-9, a.d_schritt), 4)
    scan = []
    with torch.no_grad():
        for d in ds:
            Sp = Sphi(float(d))
            Eb = float(energie(mv, Sp, h, a.v, a.kappa, a.mu))
            dd = diagnose(mv, Sp, S0, X, Y, Z, h, a.v, a.kappa, a.mu)
            scan.append({"d": float(d), "E_int_prod": Eb - Ev, "E_kreuz": dd["E_kreuz"], "innen": dd["E_kreuz_innen"],
                         "wand": dd["E_kreuz_wand"], "aussen": dd["E_kreuz_aussen"],
                         "S_phi_s_durch_S0": dd["S_phi_s_durch_S0"]})
            log("Produkt d = %5.2f: E_int = %.6f (innen %.4f wand %.4f aussen %.4f) S_phi_s/S0 %.3f"
                % (d, Eb - Ev, dd["E_kreuz_innen"], dd["E_kreuz_wand"], dd["E_kreuz_aussen"], dd["S_phi_s_durch_S0"]))
    erg["produkt_scan"] = scan
    j = int(np.argmin([q["E_int_prod"] for q in scan]))
    dmin = scan[j]["d"]
    log("Minimum Produktansatz (relaxierter Knoten): d = %.2f E_int = %.6f; d = 0: %.6f; Verhaeltnis Mitte/Minimum %.3f"
        % (dmin, scan[j]["E_int_prod"], scan[0]["E_int_prod"], scan[0]["E_int_prod"] / scan[j]["E_int_prod"]))
    erg["produkt_min"] = {"d": dmin, "E_int": scan[j]["E_int_prod"], "E_int_d0": scan[0]["E_int_prod"]}

    erg["relax"] = []
    for tok in a.d_relax.split(","):
        d = dmin if tok == "auto" else float(tok)
        Sp = Sphi(d)
        Eprod = float(energie(mv, Sp, h, a.v, a.kappa, a.mu)) - Ev
        mb, verl_b = relaxiere(mv, Sp, h, a.v, a.kappa, a.mu, a.iters, a.tmax, "d=%.2f" % d, dt=a.dt)
        Eb = float(energie(mb, Sp, h, a.v, a.kappa, a.mu))
        Es = float(energie(mb, null, h, a.v, a.kappa, a.mu))
        db = diagnose(mb, Sp, S0, X, Y, Z, h, a.v, a.kappa, a.mu)
        log("Relaxiert bei d = %.2f: E_int_rel = %.6f (Produkt %.6f) = Verformung %.6f + Kreuz %.6f (innen %.4f wand %.4f"
            " aussen %.4f); rho_kern %.3f (vak %.3f) z_kern %.4f (vak %.4f) S_phi_s/S0 %.3f"
            % (d, Eb - Ev, Eprod, Es - Ev, db["E_kreuz"], db["E_kreuz_innen"], db["E_kreuz_wand"], db["E_kreuz_aussen"],
               db["rho_kern"], dv["rho_kern"], db["z_kern"], dv["z_kern"], db["S_phi_s_durch_S0"]))
        # Kontrolle: Rueckrechnung des relaxierten Knotens auf Nachbarlagen (Drift-Neigung)
        nb = {}
        for dd_ in (d - 0.5, d + 0.5):
            if dd_ >= 0:
                nb["%.2f" % dd_] = float(energie(mb, Sphi(dd_), h, a.v, a.kappa, a.mu)) - Ev
        Hb, Fb = hopfzahl_feld(mb, h)
        log("   relaxierter Knoten an Nachbarlagen: %s; Hopfzahl %.4f (Fluss %.4f)" % (json.dumps(nb), Hb, Fb))
        erg["relax"].append({"d": d, "E_int_rel": Eb - Ev, "E_int_prod": Eprod, "Verformung": Es - Ev, "diag": db,
                             "verlauf": verl_b, "nachbarlagen": nb, "hopf": [Hb, Fb]})
        if a.geraet == "cuda":
            torch.cuda.empty_cache()

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
