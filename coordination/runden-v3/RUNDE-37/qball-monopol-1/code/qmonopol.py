"""QBALL-MONOPOL-1 (Runde 38, Code-Agent fuer claude-primary): axialsymmetrischer M1-Q-Ball mit Ladung im festen
Monopol-Hintergrundfeld (mu = q g/(4 pi) = 1/2) und Portal-Topf -V0 exp(-r^2/r_c^2) |phi|^2, r_c = 1.

Ansatz: phi = f(r, theta) e^{i k varphi} e^{-i omega t}, k = 0; Dirac-Eichung A_varphi = (g/(4 pi r)) (1 - cos theta)/sin theta
(String bei theta = pi). Mit reellem f:
    |D phi|^2 = f_r^2 + f_theta^2/r^2 + W(theta)/(r^2 sin^2 theta) f^2,   W = (k - mu (1 - cos theta))^2.
U(S) = S - S^2 + S^3/2 (M1, wie qladung2.py). Feste Ladung Q: omega = Q/(2N), N = int f^2 d^3x, und
    E_Q[f] = Q^2/(4N) + int [ |D phi|^2 + U(f^2) - V0 exp(-r^2) f^2 ] d^3x
(gleich omega^2 N + Gradient + Potential; stationaer <=> Q-Ball-Gleichung bei fester Ladung).
Relaxation: Minimierung von E_Q mit gedaempftem Newton (Levenberg-Marquardt in der Metrik 2w, Armijo-Liniensuche),
duennbesetzte LU (splu) plus Sherman-Morrison fuer den Rang-1-Term von Q^2/(4N).
Gitter: Finite Volumen in (r, theta); Zellmitten; r-Flaechen gleichabstaendig bis r_s, danach geometrisch gestreckt;
f = 0 auf r = Rmax (Dirichlet); bei theta = 0, pi und r = 0 natuerliche Randbedingung (Flaechengewicht 0).

Aufruf nur ueber kleintest.sh auf der .69:
  qmonopol.py rauch <ausgabe.json>
  qmonopol.py lauf <ausgabe.json> h=<h> rs=<r_s> Rmax=<R> Nt=<Nt> V0=<v1,v2,..> Q=<q1,q2,..> starts=<A,B> [qm0=1]
"""
import hashlib
import json
import os
import sys
import time

import numpy as np
import scipy
import scipy.sparse as sp
import scipy.sparse.linalg as spla

BETA = 0.5
MU = 0.5
SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
QL0 = {"Q": 473.41306250272663, "E_tabelle": 428.641, "E_qladung2": 428.6416866881757}


def U(S):
    return S - S * S + BETA * S ** 3


def Up(S):
    return 1.0 - 2.0 * S + 3.0 * BETA * S * S


def Upp(S):
    return -2.0 + 6.0 * BETA * S


def radialflaechen(h, rs, Rmax, wachstum=1.05):
    rf = list(h * np.arange(int(round(min(rs, Rmax) / h)) + 1))
    schritt = h
    while rf[-1] < Rmax - 1e-12:
        schritt *= wachstum
        rf.append(min(rf[-1] + schritt, Rmax) if Rmax - rf[-1] - schritt > 0.5 * schritt else Rmax)
    return np.array(rf)


class Gitter:
    def __init__(self, h, rs, Rmax, Nt, mu, V0, k=0, rc=1.0):
        rf = radialflaechen(h, rs, Rmax)
        Nr = len(rf) - 1
        self.h, self.rs, self.Nr, self.Nt, self.mu, self.V0, self.k = h, rs, Nr, Nt, mu, V0, k
        self.Rmax = float(rf[-1])
        r = 0.5 * (rf[1:] + rf[:-1])
        ht = np.pi / Nt
        tf = ht * np.arange(Nt + 1)
        t = 0.5 * (tf[1:] + tf[:-1])
        Vr = (rf[1:] ** 3 - rf[:-1] ** 3) / 3.0
        Lr = rf[1:] - rf[:-1]
        Vt = np.cos(tf[:-1]) - np.cos(tf[1:])
        self.r, self.t, self.rf, self.tf, self.Vr, self.Vt, self.Lr = r, t, rf, tf, Vr, Vt, Lr
        self.w = (2 * np.pi * np.outer(Vr, Vt)).ravel()
        Wt = (k - mu * (1.0 - np.cos(t))) ** 2
        self.a = (2 * np.pi * np.outer(Lr, Wt / np.sin(t) ** 2 * Vt)).ravel()
        self.topf = np.outer(np.exp(-(r / rc) ** 2), np.ones(Nt)).ravel()
        self.R = np.outer(r, np.ones(Nt)).ravel()
        self.C = np.outer(np.ones(Nr), np.cos(t)).ravel()
        n = Nr * Nt
        self.n = n
        idx = np.arange(n).reshape(Nr, Nt)
        dr = r[1:] - r[:-1]
        cr = 2 * np.pi * (rf[1:Nr] ** 2 / dr)[:, None] * Vt[None, :]
        cb = 2 * np.pi * (rf[Nr] ** 2 / (rf[Nr] - r[-1])) * Vt
        dgr = np.zeros((Nr, Nt))
        dgr[:-1, :] += cr
        dgr[1:, :] += cr
        dgr[-1, :] += cb
        self.Kr = sp.csr_matrix((np.concatenate([dgr.ravel(), -cr.ravel(), -cr.ravel()]),
                                 (np.concatenate([idx.ravel(), idx[:-1, :].ravel(), idx[1:, :].ravel()]),
                                  np.concatenate([idx.ravel(), idx[1:, :].ravel(), idx[:-1, :].ravel()]))), shape=(n, n))
        if Nt > 1:
            ct = 2 * np.pi * np.outer(Lr, np.sin(tf[1:Nt]) / ht)
            dgt = np.zeros((Nr, Nt))
            dgt[:, :-1] += ct
            dgt[:, 1:] += ct
            self.Kt = sp.csr_matrix((np.concatenate([dgt.ravel(), -ct.ravel(), -ct.ravel()]),
                                     (np.concatenate([idx.ravel(), idx[:, :-1].ravel(), idx[:, 1:].ravel()]),
                                      np.concatenate([idx.ravel(), idx[:, 1:].ravel(), idx[:, :-1].ravel()]))),
                                    shape=(n, n))
        else:
            self.Kt = sp.csr_matrix((n, n))
        self.K = (self.Kr + self.Kt).tocsr()
        self.K2 = (2.0 * self.K).tocsc()

    def E(self, f, Q):
        S = f * f
        N = self.w @ S
        return Q * Q / (4.0 * N) + f @ (self.K @ f) + self.a @ S + self.w @ (U(S) - self.V0 * self.topf * S)

    def teile(self, f, Q):
        S = f * f
        N = float(self.w @ S)
        d = {"N": N, "omega": Q / (2 * N), "e_kin": Q * Q / (4.0 * N), "e_rad": float(f @ (self.Kr @ f)),
             "e_pol": float(f @ (self.Kt @ f)), "e_az": float(self.a @ S), "e_pot": float(self.w @ U(S)),
             "e_topf": -self.V0 * float(self.w @ (self.topf * S))}
        d["E"] = d["e_kin"] + d["e_rad"] + d["e_pol"] + d["e_az"] + d["e_pot"] + d["e_topf"]
        return d

    def grad(self, f, Q):
        S = f * f
        N = self.w @ S
        om2 = (Q / (2 * N)) ** 2
        g = 2 * (self.K @ f + self.a * f + self.w * (Up(S) - self.V0 * self.topf - om2) * f)
        return g, N, om2

    def hdiag(self, f, om2):
        S = f * f
        return 2 * (self.a + self.w * (Up(S) + 2 * S * Upp(S) - self.V0 * self.topf - om2))


def sauber(x):
    """JSON ohne NaN/Inf (jq-lesbar)."""
    if isinstance(x, dict):
        return {k: sauber(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [sauber(v) for v in x]
    if isinstance(x, float) and not np.isfinite(x):
        return None
    return x


def schwerpunkt_z(G, f):
    rho = G.w * f * f
    return float(rho @ (G.R * G.C)) / float(rho.sum())


def relax(G, f, Q, maxit=80, tol=1e-12, lam=0.0, zeitgrenze=None, z_stop=None):
    """Gedaempfter Newton auf E_Q. Rueckgabe f, E, Status, Verlauf.
    z_stop: Abwanderungs-Stopp, sobald der Ladungsschwerpunkt z_c > z_stop (Ball hat Monopol und Topf verlassen)."""
    t0 = time.time()
    M = 2 * G.w
    E = G.E(f, Q)
    verlauf = []
    status = "maxit"
    for it in range(maxit):
        if zeitgrenze is not None and time.time() - t0 > zeitgrenze:
            status = "zeitgrenze"
            break
        if z_stop is not None and schwerpunkt_z(G, f) > z_stop:
            status = "abgewandert"
            break
        g, N, om2 = G.grad(f, Q)
        d = G.hdiag(f, om2)
        u = G.w * f
        c = 2 * Q * Q / N ** 3
        ok = False
        while lam < 1e14:
            A = (G.K2 + sp.diags(d + lam * M)).tocsc()
            try:
                lu = spla.splu(A)
            except RuntimeError:
                lam = max(10 * lam, 1e-6)
                continue
            y = lu.solve(-g)
            z = lu.solve(u)
            p = y - c * z * (u @ y) / (1 + c * (u @ z))
            gp = float(g @ p)
            if not np.isfinite(gp) or gp >= 0:
                lam = max(10 * lam, 1e-6)
                continue
            if lam == 0.0 and -gp < tol * abs(E):
                status = "konvergiert"
                verlauf.append([it, float(E), -gp, lam, 0.0])
                return f, float(E), status, verlauf, round(time.time() - t0, 2)
            alpha = 1.0
            while alpha > 1e-3:
                fn = f + alpha * p
                En = G.E(fn, Q)
                if En <= E + 1e-4 * alpha * gp:
                    ok = True
                    break
                alpha *= 0.5
            if ok:
                break
            if -gp < 1e-9 * abs(E):
                status = "konvergiert (Rundung)"
                verlauf.append([it, float(E), -gp, lam, -1.0])
                return f, float(E), status, verlauf, round(time.time() - t0, 2)
            lam = max(10 * lam, 1e-6)
        if not ok:
            status = "kein Abstieg"
            break
        verlauf.append([it, float(En), -gp, lam, alpha, schwerpunkt_z(G, fn)])
        f, E = fn, En
        lam = lam / 10.0 if lam > 1e-9 else 0.0
    return f, float(E), status, verlauf, round(time.time() - t0, 2)


def tiefste_eigenwerte(G, f, Q, sigma=-0.2, k=4):
    """Eigenwerte von Hess(E_Q) v = lambda (2w) v nahe sigma (Minimumspruefung, beschreibend)."""
    g, N, om2 = G.grad(f, Q)
    d = G.hdiag(f, om2)
    u = G.w * f
    c = 2 * Q * Q / N ** 3
    M = 2 * G.w
    A0 = (G.K2 + sp.diags(d)).tocsr()
    H = spla.LinearOperator((G.n, G.n), matvec=lambda x: A0 @ x + c * u * (u @ x), dtype=float)
    lu = spla.splu((G.K2 + sp.diags(d - sigma * M)).tocsc())
    zu = lu.solve(u)
    den = 1 + c * (u @ zu)

    def inv(b):
        y = lu.solve(b)
        return y - c * zu * (u @ y) / den

    OPinv = spla.LinearOperator((G.n, G.n), matvec=inv, dtype=float)
    vals = spla.eigsh(H, k=k, M=sp.diags(M).tocsr(), sigma=sigma, OPinv=OPinv, which="LM",
                      return_eigenvectors=False, tol=1e-10, maxiter=5000)
    return sorted(float(v) for v in vals)


def profil_1d(h, rs, Rmax, Q, V0=0.0):
    """Kugelfoermiger Ball (mu = 0) auf demselben r-Gitter, Nt = 1; Startprofil und Referenz."""
    G1 = Gitter(h, rs, Rmax, 1, 0.0, V0)
    N0 = Q / (2 * 0.9)
    R0 = (3 * N0 / (4 * np.pi * 1.05)) ** (1.0 / 3.0)
    f = np.sqrt(1.05) / (1 + np.exp((G1.r - R0) / 0.8))
    f, E, st, vl, sek = relax(G1, f, Q, maxit=200)
    T = G1.teile(f, Q)
    S = f * f
    i_half = int(np.argmin(np.abs(S - 0.5 * S[0])))
    return G1, f, {"E": E, "status": st, "iter": len(vl), "sek": sek, "omega2": T["omega"] ** 2, "f0_2": float(S[0]),
                   "R_halb": float(G1.r[i_half]), "teile": T}


def kennzahlen(G, f, Q):
    T = G.teile(f, Q)
    N = T["N"]
    om = Q / (2 * N)
    S = f * f
    rho = G.w * S
    F2 = S.reshape(G.Nr, G.Nt)
    d = {"teile": T, "omega2": om * om,
         "z_c": float(rho @ (G.R * G.C)) / N,
         "anteil_rand": float(rho[G.R > G.Rmax - 10.0].sum()) / N,
         "anteil_r_lt_3": float(rho[G.R < 3.0].sum()) / N,
         "cos_mittel": float(rho @ G.C) / N}
    # Winkelform: D(theta) = int f^2 r^2 dr entlang des Strahls
    Dt = (F2 * (G.r ** 2 * G.Lr)[:, None]).sum(axis=0)
    if G.Nt >= 4:
        D0 = (9 * Dt[0] - Dt[1]) / 8.0
        j = G.Nt // 2
        D90 = 0.5 * (Dt[j - 1] + Dt[j])
        DPI = (9 * Dt[-1] - Dt[-2]) / 8.0
        d["winkel_D0_D90"] = float(D0 / D90)
        d["winkel_Dpi_D90"] = float(DPI / D90)
        d["winkel_D_theta"] = [float(x) for x in Dt / D90]
        # punktweise am Maximum der Kugelmittel-Dichte
        mitt = (F2 * G.Vt[None, :]).sum(axis=1) / 2.0
        im = int(np.argmax(mitt))
        f0 = (9 * F2[im, 0] - F2[im, 1]) / 8.0
        f90 = 0.5 * (F2[im, j - 1] + F2[im, j])
        d["punkt_r_max"] = float(G.r[im])
        d["punkt_ratio_am_rmax"] = float(f0 / f90) if f90 > 0 else None
        # lokale Exponenten nahe r = 0, theta-Zelle 0
        fr = np.sqrt(F2[:6, 0])
        d["exponent_r0"] = [float(np.log(fr[i + 1] / fr[i]) / np.log(G.r[i + 1] / G.r[i])) for i in range(5)]
        d["exponent_r0_kugelmittel"] = [float(0.5 * np.log(mitt[i + 1] / mitt[i]) / np.log(G.r[i + 1] / G.r[i]))
                                        for i in range(5)]
    # Drehimpuls: Materie (kinetisch, eichinvariant) plus Kreuzanteil mit dem Monopolfeld (Thomson)
    Jm = 2 * om * float(rho @ (G.k - G.mu * (1 - G.C)))
    Jx = -G.mu * 2 * om * float(rho @ G.C)
    d["J_materie"] = Jm
    d["J_kreuz"] = Jx
    d["J_z"] = Jm + Jx
    d["J_z_plus_Q_halbe"] = Jm + Jx + Q * G.mu
    d["Q_kontrolle"] = 2 * om * N
    return d


def start_feld(G, G1, f1, d, winkel):
    rr = np.sqrt(np.maximum(G.R ** 2 + d * d - 2 * G.R * d * G.C, 0.0))
    f = np.interp(rr, G1.r, f1, right=0.0)
    if winkel == "sym":
        # z-symmetrische Verformung (Quadrupol) fuer QM0: regt die Translationsnullmode nicht an
        f = f * (1.0 + 0.3 * 0.5 * (3 * G.C ** 2 - 1))
    elif winkel:
        f = f * np.sqrt(1.0 + G.C)
    return f


def winkel_eigenwerte(Nt, mu, k=0, anzahl=3):
    """Diskreter Winkeloperator (eine r-Schale): kleinste Eigenwerte, Soll j(j+1) - mu^2 = 1/2, 2.5, ... (mu = 1/2)."""
    ht = np.pi / Nt
    tf = ht * np.arange(Nt + 1)
    t = 0.5 * (tf[1:] + tf[:-1])
    Vt = np.cos(tf[:-1]) - np.cos(tf[1:])
    ct = np.sin(tf[1:Nt]) / ht
    A = np.zeros((Nt, Nt))
    for j in range(Nt - 1):
        A[j, j] += ct[j]
        A[j + 1, j + 1] += ct[j]
        A[j, j + 1] -= ct[j]
        A[j + 1, j] -= ct[j]
    A += np.diag((k - mu * (1 - np.cos(t))) ** 2 / np.sin(t) ** 2 * Vt)
    Bm = np.diag(1.0 / np.sqrt(Vt))
    ev = np.linalg.eigvalsh(Bm @ A @ Bm)
    return [float(x) for x in ev[:anzahl]]


def rauch(ausgabe):
    t0 = time.time()
    erg = {"modus": "rauch", "skript_sha256": SKRIPT_SHA, "numpy": np.__version__, "scipy": scipy.__version__}

    def sichern():
        erg["zeit_s"] = round(time.time() - t0, 1)
        with open(ausgabe, "w") as fh:
            json.dump(erg, fh, indent=1)

    erg["winkel"] = {str(nt): {"mu0.5": winkel_eigenwerte(nt, MU), "mu0": winkel_eigenwerte(nt, 0.0)}
                     for nt in (16, 32, 64, 128)}
    sichern()
    # 1D-Kontrolle gegen QL0
    erg["eindim_QL0"] = []
    for h in (0.1, 0.05, 0.025):
        G1, f1, info = profil_1d(h, 20.0, 40.0, QL0["Q"])
        info.pop("teile")
        info["h"] = h
        erg["eindim_QL0"].append(info)
        sichern()
    # 2D-Zeitprobe: QM0-Fall und ein Monopolfall
    erg["zeitprobe"] = []
    for (h, nt) in ((0.1, 32), (0.05, 64)):
        G1, f1, info = profil_1d(h, 20.0, 40.0, QL0["Q"])
        G = Gitter(h, 20.0, 40.0, nt, 0.0, 0.0)
        f, E, st, vl, sek = relax(G, start_feld(G, G1, f1, 0.0, True), QL0["Q"], maxit=60, zeitgrenze=100)
        erg["zeitprobe"].append({"fall": "QM0", "h": h, "Nt": nt, "n": G.n, "E": E, "E1d": info["E"], "status": st,
                                 "iter": len(vl), "sek": sek, "z_c": kennzahlen(G, f, QL0["Q"])["z_c"]})
        sichern()
        G1, f1, info = profil_1d(h, 20.0, 40.0, 200.0)
        G = Gitter(h, 20.0, 40.0, nt, MU, 2.0)
        f, E, st, vl, sek = relax(G, start_feld(G, G1, f1, 0.0, True), 200.0, maxit=60, zeitgrenze=100)
        kz = kennzahlen(G, f, 200.0)
        erg["zeitprobe"].append({"fall": "mono Q=200 V0=2 A", "h": h, "Nt": nt, "n": G.n, "E": E, "E1d_frei": info["E"],
                                 "status": st, "iter": len(vl), "sek": sek, "z_c": kz["z_c"],
                                 "winkel": kz.get("winkel_D0_D90"), "J_z": kz["J_z"],
                                 "exponent": kz.get("exponent_r0"), "verlauf_letzte": vl[-5:]})
        sichern()
    erg["zeit_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    sichern()


def lauf(ausgabe, opts):
    t0 = time.time()
    h = float(opts.get("h", 0.05))
    rs = float(opts.get("rs", 20.0))
    Rmax = float(opts.get("Rmax", 40.0))
    Nt = int(opts.get("Nt", 64))
    V0s = [float(x) for x in opts.get("V0", "0,0.5,1,2").split(",")]
    Qs = [float(x) for x in opts.get("Q", "150,200,300,500,1000,2000").split(",")]
    starts = opts.get("starts", "A,B").split(",")
    maxit = int(opts.get("maxit", 60))
    zg = float(opts.get("zeitgrenze", 120))
    zplus = float(opts.get("zstop", 4.0))
    erg = {"modus": "lauf", "optionen": opts, "h": h, "rs": rs, "Rmax": Rmax, "Nt": Nt, "V0": V0s, "Q": Qs,
           "starts": starts, "mu": MU, "beta": BETA, "zstop_plus": zplus, "skript_sha256": SKRIPT_SHA,
           "numpy": np.__version__, "scipy": scipy.__version__, "referenz": [], "faelle": [], "artefakt": []}
    felder = {}

    def sichern(npz=False):
        erg["zeit_s"] = round(time.time() - t0, 1)
        with open(ausgabe, "w") as fh:
            json.dump(sauber(erg), fh, indent=1)
        if npz and opts.get("npz", "") and felder:
            np.savez_compressed(opts["npz"], **felder)

    G0 = Gitter(h, rs, Rmax, Nt, 0.0, 0.0)
    erg["n"] = G0.n
    erg["Nr"] = G0.Nr
    if opts.get("qm0", "0") == "1":
        G1, f1, info = profil_1d(h, rs, Rmax, QL0["Q"])
        f, E, st, vl, sek = relax(G0, start_feld(G0, G1, f1, 0.0, "sym"), QL0["Q"], maxit=maxit, zeitgrenze=zg)
        kz = kennzahlen(G0, f, QL0["Q"])
        erg["qm0"] = {"Q": QL0["Q"], "E_2d": E, "E_1d": info["E"], "E_tabelle": QL0["E_tabelle"],
                      "rel_2d_tabelle": E / QL0["E_tabelle"] - 1, "rel_1d_tabelle": info["E"] / QL0["E_tabelle"] - 1,
                      "rel_2d_1d": E / info["E"] - 1, "status": st, "iter": len(vl), "sek": sek, "z_c": kz["z_c"],
                      "omega2": kz["omega2"], "winkel_D0_D90": kz.get("winkel_D0_D90"),
                      "start_E": float(G0.E(start_feld(G0, G1, f1, 0.0, "sym"), QL0["Q"]))}
        sichern()
    profile = {}
    for Q in Qs:
        G1, f1, info = profil_1d(h, rs, Rmax, Q)
        profile[Q] = (G1, f1, info)
        ref = {"Q": Q, "V0": 0.0, "E_frei": info["E"], "status": info["status"], "omega2": info["omega2"],
               "R_halb": info["R_halb"], "f0_2": info["f0_2"]}
        erg["referenz"].append(ref)
        for V0 in V0s:
            if V0 == 0.0:
                continue
            G1t = Gitter(h, rs, Rmax, 1, 0.0, V0)
            ft, Et, stt, vlt, sekt = relax(G1t, f1.copy(), Q, maxit=200)
            erg["referenz"].append({"Q": Q, "V0": V0, "E_topf": Et, "status": stt,
                                    "omega2": G1t.teile(ft, Q)["omega"] ** 2})
        if opts.get("artefakt", "1") == "1":
            # Translationsartefakt: freier Ball (mu = 0, V0 = 0) auf dem 2D-Gitter, Start bei d = R_halb + 2,
            # gleicher Abwanderungs-Stopp wie die Monopolfaelle
            zs = info["R_halb"] + zplus
            fa, Ea, sta, vla, seka = relax(G0, start_feld(G0, G1, f1, info["R_halb"] + 2.0, False), Q, maxit=maxit,
                                           zeitgrenze=zg, z_stop=zs)
            erg["artefakt"].append({"Q": Q, "E_2d_frei_verschoben": Ea, "E_frei_1d": info["E"], "dE": Ea - info["E"],
                                    "status": sta, "iter": len(vla), "z_c": schwerpunkt_z(G0, fa), "z_stop": zs})
        sichern()

    def mono_fall(G, V0, Q, s, f1G=None):
        G1, f1, info = profile[Q] if f1G is None else f1G
        d = {"A": 0.0, "B": info["R_halb"], "C": 0.5 * info["R_halb"]}[s]
        zs = info["R_halb"] + zplus
        f, E, st, vl, sek = relax(G, start_feld(G, G1, f1, d, True), Q, maxit=maxit, zeitgrenze=zg, z_stop=zs)
        kz = kennzahlen(G, f, Q)
        fall = {"V0": V0, "Q": Q, "start": s, "d_start": d, "z_stop": zs, "E": E, "status": st, "iter": len(vl),
                "sek": sek, "E_frei": info["E"], "bindung_rel": 1.0 - E / info["E"], "kennzahlen": kz,
                "verlauf_letzte": vl[-4:]}
        if st.startswith("konvergiert") and opts.get("eig", "1") == "1":
            try:
                fall["eigenwerte"] = tiefste_eigenwerte(G, f, Q)
            except Exception as ex:  # nur beschreibend
                fall["eigenwerte_fehler"] = repr(ex)[:200]
        return fall, f

    for V0 in V0s:
        G = Gitter(h, rs, Rmax, Nt, MU, V0)
        for Q in Qs:
            for s in starts:
                fall, f = mono_fall(G, V0, Q, s)
                erg["faelle"].append(fall)
                if opts.get("npz", ""):
                    felder["f_V%s_Q%s_%s" % (V0, int(Q), s)] = f
                sichern()
    if opts.get("npz", ""):
        felder["gitter_r"] = G0.r
        felder["gitter_t"] = G0.t
        felder["gitter_Lr"] = G0.Lr
        felder["gitter_Vt"] = G0.Vt
        sichern(npz=True)
    # beschreibend: Q_max per Bisektion in log Q zwischen letztem gebundenem und erstem ungebundenem Rasterpunkt
    if opts.get("qmax", "0") == "1":
        erg["qmax"] = []
        for V0 in V0s:
            if V0 == 0.0:
                continue
            G = Gitter(h, rs, Rmax, Nt, MU, V0)
            geb = []
            for Q in Qs:
                bl = [c for c in erg["faelle"] if c["V0"] == V0 and c["Q"] == Q]
                geb.append(max(c["bindung_rel"] for c in bl) > 1e-3)
            kand = [i for i in range(len(Qs) - 1) if geb[i] and not any(geb[i + 1:])]
            if not kand:
                erg["qmax"].append({"V0": V0, "gebunden": geb, "bisektion": None})
                sichern()
                continue
            i = kand[0]
            lo, hi = np.log(Qs[i]), np.log(Qs[i + 1])
            schritte = []
            for _ in range(int(opts.get("qmax_schritte", 7))):
                mid = 0.5 * (lo + hi)
                Q = float(np.exp(mid))
                G1, f1, info = profil_1d(h, rs, Rmax, Q)
                best = None
                for s in starts:
                    fall, f = mono_fall(G, V0, Q, s, f1G=(G1, f1, info))
                    if best is None or fall["E"] < best["E"]:
                        best = fall
                b = best["bindung_rel"]
                schritte.append({"Q": Q, "bindung_rel": b, "E": best["E"], "E_frei": info["E"], "status": best["status"],
                                 "start": best["start"], "z_c": best["kennzahlen"]["z_c"]})
                if b > 1e-3:
                    lo = mid
                else:
                    hi = mid
                sichern()
            erg["qmax"].append({"V0": V0, "gebunden": geb, "Q_lo": float(np.exp(lo)), "Q_hi": float(np.exp(hi)),
                                "bisektion": schritte})
            sichern()
    erg["zeit_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    sichern(npz=True)


def main():
    modus = sys.argv[1]
    ausgabe = sys.argv[2]
    opts = dict(a.split("=", 1) for a in sys.argv[3:])
    if modus == "rauch":
        rauch(ausgabe)
    elif modus == "lauf":
        lauf(ausgabe, opts)
    print(json.dumps({"modus": modus, "ausgabe": ausgabe}))


if __name__ == "__main__":
    main()
