# HOPF-1 (Runde 10): Wechselwirkungsenergie Q-Ball + Hopf-Knoten (h = 1) im Produktansatz, Modell B.5 (Codex,
# literatur-20260923/SPIN-KONSTRUKTION-codex.md, Zeilen 591-690).
# Autor: Claude (Code-Agent HOPF-1), 2026-09-30. Plan, Schreibtischpruefung, Entscheidungsregeln: PLAN.md im Kartenordner.
# Nur auf der .69 ueber kleintest.sh (float64; GPU-Spur p4000a/p4000b, Rauchtest cpu6).
#
# E_int = Int [U(S_phi + S_b) - U(S_phi) - U(S_b)] d^3x - gJ Int Re[(phi* b)^2] d^3x,  U(s) = s - s^2 + s^3/2,
#   S_phi = f(r)^2, S_b = c s, c = v^2/4, s = n1^2 + n2^2, b = (v/2)(n1 + i n2).
#   Exakt: E_U(c) = c A1 + c^2 A2 mit A1 = Int S_phi s (-2 + 1,5 S_phi), A2 = Int 1,5 S_phi s^2.
#   gJ-Term (phi = f e^{-i omega t}): -gJ c Re[G e^{2 i omega t}], G = Int S_phi (n1 + i n2)^2.
# Knoten: A = Hopfabbildung W = Z1/Z0 mit Profil f(r) = 2 atan(sinh(R_h/w)/sinh(r/w)); B = kompakter Torus.
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
import krein as KR  # noqa: E402  (KREIN-1, unveraendert: Q-Ball-Profil per Schiessen)

T0 = time.time()
DT = torch.float64
GJ_MAX = 4.0 * (math.sqrt(2.0) - 1.0)
VS = (0.5, 1.0)


def log(*a):
    print("[%7.1fs]" % (time.time() - T0), *a, flush=True)


def U(s):
    return s - s * s + 0.5 * s * s * s


# ------------------------------------------------------------------ Q-Ball
def ball(x, dr=1e-3, rmax=80.0):
    from scipy.integrate import simpson
    f, a, rc = KR.profil(x)
    r = np.arange(0.0, rmax + 0.5 * dr, dr)
    fv = f(r)
    S = fv * fv
    om = math.sqrt(x)
    fp = np.gradient(fv, dr)
    w = 4.0 * math.pi * r * r
    Q = 2.0 * om * simpson(w * S, x=r)
    E = simpson(w * (om * om * S + fp * fp + U(S)), x=r)
    S0 = float(S[0])

    def r_bei(wert):
        i = int(np.argmax(S < wert))
        return float(r[i]) if S[i] < wert else float("nan")
    info = {"omega2": x, "omega": om, "f0": float(a), "S0": S0, "r_schwanz": float(rc), "Q": float(Q),
            "E_Q": float(E), "E_Q_durch_omega_Q": float(E / (om * Q)),
            "r_S_0.9S0": r_bei(0.9 * S0), "R_ball_S0halbe": r_bei(0.5 * S0), "r_S_2/3": r_bei(2.0 / 3.0),
            "r_S_0.1S0": r_bei(0.1 * S0), "g_S0": S0 * (-2.0 + 1.5 * S0), "c_lokal_mitte": 4.0 / 3.0 - S0}
    return r, S, info


class Ballfeld:
    def __init__(self, r, S, dev):
        self.dr = float(r[1] - r[0])
        self.S = torch.tensor(S, dtype=DT, device=dev)
        self.n = len(S)

    def __call__(self, R):
        u = torch.clamp(R / self.dr, max=self.n - 1.000001)
        i = torch.floor(u)
        w = u - i
        i = i.long()
        return self.S[i] * (1.0 - w) + self.S[i + 1] * w


# ------------------------------------------------------------------ Knoten h = 1 (Zentrum im Ursprung, Achse z)
def knoten(typ, par, X, Y, Z):
    if typ == "A":
        Rh, w = par
        r = torch.sqrt(X * X + Y * Y + Z * Z)
        sh = math.sinh(Rh / w)
        fh = 2.0 * torch.atan(sh / torch.sinh(torch.clamp(r, min=1e-300) / w))
        grenz = 2.0 / (w * sh)                       # lim_{r->0} sin f / r
        sf = torch.where(r > 1e-9, torch.sin(fh) / torch.clamp(r, min=1e-9), torch.full_like(r, grenz))
        z1r, z1i = X * sf, Y * sf
        z0r, z0i = torch.cos(fh), Z * sf
        n1 = 2.0 * (z1r * z0r + z1i * z0i)
        n2 = 2.0 * (z1i * z0r - z1r * z0i)
        n3 = z0r * z0r + z0i * z0i - z1r * z1r - z1i * z1i
    elif typ == "B":
        Rh, a = par
        rho = torch.sqrt(X * X + Y * Y)
        dq = rho - Rh
        de = torch.sqrt(dq * dq + Z * Z)
        Th = torch.clamp(math.pi * (1.0 - de / a), min=0.0)
        ph = torch.atan2(Y, X) + torch.atan2(Z, dq)
        st = torch.sin(Th)
        n1 = st * torch.cos(ph)
        n2 = st * torch.sin(ph)
        n3 = torch.cos(Th)
    else:
        raise ValueError(typ)
    return n1, n2, n3


# ------------------------------------------------------------------ Lagen
def lagen_bauen(info, rauch=False):
    Rb = info["R_ball_S0halbe"]
    r23 = info["r_S_2/3"]
    L = []

    def add(fam, typ, par, d, koax, x):
        L.append({"familie": fam, "typ": typ, "par": [float(p) for p in par], "d": [float(q) for q in d],
                  "koax": koax, "x": float(x)})
    if rauch:
        for Rh in (1.0, Rb):
            add("F1A", "A", (Rh, 0.75), (0, 0, 0), True, Rh)
        add("F1B", "B", (max(2.0, Rb), 1.5), (0, 0, 0), True, max(2.0, Rb))
        for d in (0.0, Rb):
            add("F2z_klein", "A", (0.75, 0.35), (0, 0, d), True, d)
            add("F2x_klein", "A", (0.75, 0.35), (d, 0, 0), False, d)
        return L
    radien = sorted(set([round(q, 3) for q in np.arange(0.5, Rb + 4.001, 0.5)] + [round(Rb, 3), round(r23, 3)]))
    for Rh in radien:
        add("F1A", "A", (Rh, 0.75), (0, 0, 0), True, Rh)
    for Rh in radien:
        add("F1S", "A", (Rh, 0.5 * Rh), (0, 0, 0), True, Rh)
    for Rh in radien:
        if Rh >= 2.0:
            add("F1B", "B", (Rh, 1.5), (0, 0, 0), True, Rh)
    ds = sorted(set([round(q, 3) for q in np.arange(0.0, Rb + 5.001, 0.5)] + [round(Rb, 3), round(r23, 3)]))
    for d in ds:
        add("F2z_klein", "A", (0.75, 0.35), (0, 0, d), True, d)
    for d in ds:
        add("F2z_mittel", "A", (1.5, 0.7), (0, 0, d), True, d)
    for d in ds:
        add("F2x_klein", "A", (0.75, 0.35), (d, 0, 0), False, d)
    for d in ds:
        add("F2x_mittel", "A", (1.5, 0.7), (d, 0, 0), False, d)
    return L


GROESSEN = ["A1", "A1_innen", "A1_wand", "A1_aussen", "A2", "A2_innen", "A2_wand", "A2_aussen", "M_b", "O",
            "G_re", "G_im", "D_v0.5", "D_v1.0"]


def akkumulieren(acc, k, Sp, gw, innen, wand, aussen, s, n1, n2, wgt):
    a1 = gw * s * wgt
    a2 = 1.5 * Sp * s * s * wgt
    acc["A1"][k] += a1.sum()
    acc["A1_innen"][k] += (a1 * innen).sum()
    acc["A1_wand"][k] += (a1 * wand).sum()
    acc["A1_aussen"][k] += (a1 * aussen).sum()
    acc["A2"][k] += a2.sum()
    acc["A2_innen"][k] += (a2 * innen).sum()
    acc["A2_wand"][k] += (a2 * wand).sum()
    acc["A2_aussen"][k] += (a2 * aussen).sum()
    acc["M_b"][k] += (s * wgt).sum()
    acc["O"][k] += (Sp * s * wgt).sum()
    if n1 is not None:
        acc["G_re"][k] += (Sp * (n1 * n1 - n2 * n2) * wgt).sum()
        acc["G_im"][k] += (Sp * 2.0 * n1 * n2 * wgt).sum()
    for v in VS:
        c = 0.25 * v * v
        Sb = c * s
        acc["D_v%.1f" % v][k] += ((U(Sp + Sb) - U(Sp) - U(Sb)) * wgt).sum()


def integrale_3d(bf, S0, lagen, L, h, dev, chunk=2_000_000):
    N = int(round(2.0 * L / h))
    x = torch.tensor(-L + (np.arange(N) + 0.5) * h, dtype=DT, device=dev)
    Y2, Z2 = torch.meshgrid(x, x, indexing="ij")
    nb = max(1, chunk // (N * N))
    K = len(lagen)
    acc = {g: torch.zeros(K, dtype=DT, device=dev) for g in GROESSEN}
    wgt = h ** 3
    for i0 in range(0, N, nb):
        xs = x[i0:i0 + nb]
        m = xs.numel()
        X3 = xs.view(-1, 1, 1).expand(m, N, N)
        Y3 = Y2.unsqueeze(0).expand(m, N, N)
        Z3 = Z2.unsqueeze(0).expand(m, N, N)
        R = torch.sqrt(X3 * X3 + Y3 * Y3 + Z3 * Z3)
        Sp = bf(R)
        innen = (Sp > 0.9 * S0).to(DT)
        aussen = (Sp <= 0.1 * S0).to(DT)
        wand = 1.0 - innen - aussen
        gw = Sp * (-2.0 + 1.5 * Sp)
        for k, lg in enumerate(lagen):
            dx, dy, dz = lg["d"]
            n1, n2, n3 = knoten(lg["typ"], lg["par"], X3 - dx, Y3 - dy, Z3 - dz)
            s = n1 * n1 + n2 * n2
            akkumulieren(acc, k, Sp, gw, innen, wand, aussen, s, n1, n2, wgt)
    return {g: acc[g].cpu().numpy().tolist() for g in GROESSEN}, N


def integrale_2d(bf, S0, lagen, L, h2, dev, chunk=2_000_000):
    """achsensymmetrisch in (rho, z), nur koaxiale Lagen (Ballzentrum auf der Knotenachse)"""
    Nr = int(round(L / h2))
    Nz = int(round(2.0 * L / h2))
    rho = torch.tensor((np.arange(Nr) + 0.5) * h2, dtype=DT, device=dev)
    z = torch.tensor(-L + (np.arange(Nz) + 0.5) * h2, dtype=DT, device=dev)
    nb = max(1, chunk // Nr)
    K = len(lagen)
    acc = {g: torch.zeros(K, dtype=DT, device=dev) for g in GROESSEN}
    for j0 in range(0, Nz, nb):
        zs = z[j0:j0 + nb]
        Z2, P2 = torch.meshgrid(zs, rho, indexing="ij")
        wgt = 2.0 * math.pi * P2 * h2 * h2
        R = torch.sqrt(P2 * P2 + Z2 * Z2)
        Sp = bf(R)
        innen = (Sp > 0.9 * S0).to(DT)
        aussen = (Sp <= 0.1 * S0).to(DT)
        wand = 1.0 - innen - aussen
        gw = Sp * (-2.0 + 1.5 * Sp)
        null = torch.zeros_like(P2)
        for k, lg in enumerate(lagen):
            dz = lg["d"][2]
            n1, n2, n3 = knoten(lg["typ"], lg["par"], P2, null, Z2 - dz)
            s = n1 * n1 + n2 * n2
            akkumulieren(acc, k, Sp, gw, innen, wand, aussen, s, None, None, wgt)
    return {g: acc[g].cpu().numpy().tolist() for g in GROESSEN}, (Nr, Nz)


# ------------------------------------------------------------------ Hopfzahl (Whitehead) und Knotenenergien
def hopfzahl(typ, par, L, N, dev):
    h = 2.0 * L / N
    x = torch.tensor(-L + (np.arange(N) + 0.5) * h, dtype=DT, device=dev)
    X, Y, Z = torch.meshgrid(x, x, x, indexing="ij")
    n1, n2, n3 = knoten(typ, par, X, Y, Z)
    del X, Y, Z
    norm_fehler = float((n1 * n1 + n2 * n2 + n3 * n3 - 1.0).abs().max())

    def d(f, ax):
        return (torch.roll(f, -1, ax) - torch.roll(f, 1, ax)) / (2.0 * h)
    D = [(d(n1, a), d(n2, a), d(n3, a)) for a in range(3)]
    e2 = float(sum((q * q).sum() for a in range(3) for q in D[a]) * h ** 3)

    def F(j, k):
        a, b = D[j], D[k]
        return (n1 * (a[1] * b[2] - a[2] * b[1]) + n2 * (a[2] * b[0] - a[0] * b[2]) + n3 * (a[0] * b[1] - a[1] * b[0]))
    Bx, By, Bz = F(1, 2), F(2, 0), F(0, 1)
    del D
    e4 = float(((Bx * Bx + By * By + Bz * Bz).sum()) * h ** 3)       # = Int sum_{i<j} H_ij^2
    e0 = float((1.0 - n3).sum() * h ** 3)
    s = n1 * n1 + n2 * n2
    eS = float(s.sum() * h ** 3)
    eS2 = float((s * s).sum() * h ** 3)
    k = torch.fft.fftfreq(N, d=h).to(dev).to(DT) * 2.0 * math.pi
    KX, KY, KZ = torch.meshgrid(k, k, k, indexing="ij")
    K2 = KX * KX + KY * KY + KZ * KZ
    K2[0, 0, 0] = 1.0
    bx, by, bz = torch.fft.fftn(Bx), torch.fft.fftn(By), torch.fft.fftn(Bz)
    ax = 1j * (KY * bz - KZ * by) / K2
    ay = 1j * (KZ * bx - KX * bz) / K2
    az = 1j * (KX * by - KY * bx) / K2
    for q in (ax, ay, az):
        q[0, 0, 0] = 0.0
    Ax, Ay, Az = torch.fft.ifftn(ax).real, torch.fft.ifftn(ay).real, torch.fft.ifftn(az).real
    H = float((Ax * Bx + Ay * By + Az * Bz).sum() * h ** 3 / (16.0 * math.pi ** 2))
    # Fluss durch die Halbebene y ~ 0, x > 0 (Rand: z-Achse und Unendlich, beide Nordpol): Grad der Einschraenkung, +-1
    fluss = float(By[N // 2:, N // 2, :].sum() * h * h / (4.0 * math.pi))
    return {"typ": typ, "par": list(par), "L": L, "N": N, "h": h, "hopfzahl": H, "norm_fehler_max": norm_fehler,
            "e2_Int_gradn2": e2, "e4_Int_sum_i<j_Hij2": e4, "e0_Int_1-n3": e0, "Int_s": eS, "Int_s2": eS2,
            "fluss_halbebene_durch_4pi": fluss}


# ------------------------------------------------------------------ Auswertung
def zeile(lg, g, info, gJ=GJ_MAX):
    S0 = info["S0"]
    out = {}
    A1, A2 = g["A1"], g["A2"]
    for v in VS:
        c = 0.25 * v * v
        out["E_v%.1f" % v] = c * A1 + c * c * A2
        for reg in ("innen", "wand", "aussen"):
            out["E_v%.1f_%s" % (v, reg)] = c * g["A1_" + reg] + c * c * g["A2_" + reg]
        out["D_rel_v%.1f" % v] = (g["D_v%.1f" % v] - out["E_v%.1f" % v]) / abs(out["E_v%.1f" % v]) if out["E_v%.1f" % v] != 0 else float("nan")
        Gabs = math.hypot(g["G_re"], g["G_im"])
        out["gJ_max_rel_v%.1f" % v] = gJ * c * Gabs / abs(out["E_v%.1f" % v]) if out["E_v%.1f" % v] != 0 else float("nan")
    out["c_stern"] = -A1 / A2 if A2 > 0 else float("nan")
    out["g_je_Knotenmenge"] = A1 / g["M_b"] if g["M_b"] > 0 else float("nan")
    out["Sphi_mittel_s"] = g["O"] / g["M_b"] if g["M_b"] > 0 else float("nan")
    out["S_phi_mittel_durch_S0"] = out["Sphi_mittel_s"] / S0
    out["G_abs_durch_A1"] = math.hypot(g["G_re"], g["G_im"]) / abs(A1) if A1 != 0 else float("nan")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--geraet", default="cuda")
    ap.add_argument("--w2", type=float, default=0.6)
    ap.add_argument("--h", default="0.2,0.1")
    ap.add_argument("--h2d", type=float, default=0.01)
    ap.add_argument("--rauch", action="store_true")
    ap.add_argument("--hopf-N", type=int, default=128)
    ap.add_argument("--out", default="ERG")
    ap.add_argument("--familien", default="")
    a = ap.parse_args()
    if a.geraet == "cpu":
        torch.set_num_threads(1)
    dev = torch.device(a.geraet)
    if a.geraet == "cuda":
        log("GPU", torch.cuda.get_device_name(0), "frei/gesamt [MB]",
            [int(q / 2 ** 20) for q in torch.cuda.mem_get_info()])
    r, S, info = ball(a.w2)
    log("Ball omega^2 = %.4f: f0 = %.12f S0 = %.6f R(S0/2) = %.3f r(S=2/3) = %.3f r(0.9 S0) = %.3f r(0.1 S0) = %.3f"
        " Q = %.4f E_Q = %.4f E/(omega Q) = %.5f g(S0) = %.4f 4/3 - S0 = %.4f"
        % (a.w2, info["f0"], info["S0"], info["R_ball_S0halbe"], info["r_S_2/3"], info["r_S_0.9S0"], info["r_S_0.1S0"],
           info["Q"], info["E_Q"], info["E_Q_durch_omega_Q"], info["g_S0"], info["c_lokal_mitte"]))
    bf = Ballfeld(r, S, dev)
    lagen = lagen_bauen(info, a.rauch)
    if a.familien:
        lagen = [lg for lg in lagen if lg["familie"] in a.familien.split(",")]
    L = (6.0 if a.rauch else info["R_ball_S0halbe"] + 9.0)
    L = math.ceil(L)
    log("Lagen: %d, Halbkante L = %.1f" % (len(lagen), L))
    erg = {"ball": info, "L": L, "lagen": lagen, "gitter": {}, "hopf": [], "argv": sys.argv}

    # Hopfzahl und Knotenenergien der Referenzknoten
    if not a.rauch or a.hopf_N <= 64:
        for typ, par, LL in (("A", (1.5, 0.75), 6.0), ("A", (0.75, 0.35), 4.0), ("A", (1.5, 0.7), 6.0),
                             ("B", (2.5, 1.5), 6.0)):
            hz = hopfzahl(typ, par, LL, a.hopf_N, dev)
            erg["hopf"].append(hz)
            log("Hopfzahl %s %s N=%d: h = %.5f  |n|-1 max %.1e  e2 %.4f e4 %.4f e0 %.4f Int s %.4f Int s^2 %.4f Fluss/4pi %.4f"
                % (typ, par, a.hopf_N, hz["hopfzahl"], hz["norm_fehler_max"], hz["e2_Int_gradn2"],
                   hz["e4_Int_sum_i<j_Hij2"], hz["e0_Int_1-n3"], hz["Int_s"], hz["Int_s2"], hz["fluss_halbebene_durch_4pi"]))
            if a.geraet == "cuda":
                torch.cuda.empty_cache()

    for h in [float(q) for q in a.h.split(",")]:
        t = time.time()
        g, N = integrale_3d(bf, info["S0"], lagen, L, h, dev)
        erg["gitter"]["3d_h%.3f" % h] = g
        log("3D h = %.3f (N = %d): %.1f s" % (h, N, time.time() - t))
    koax = [i for i, lg in enumerate(lagen) if lg["koax"]]
    t = time.time()
    g2, N2 = integrale_2d(bf, info["S0"], [lagen[i] for i in koax], L, a.h2d, dev)
    g2voll = {q: [float("nan")] * len(lagen) for q in GROESSEN}
    for j, i in enumerate(koax):
        for q in GROESSEN:
            g2voll[q][i] = g2[q][j]
    erg["gitter"]["2d_h%.3f" % a.h2d] = g2voll
    log("2D h = %.3f (%s): %.1f s" % (a.h2d, N2, time.time() - t))

    # Tabelle
    schluessel = sorted(erg["gitter"].keys())
    fein3 = "3d_h%.3f" % min(float(q) for q in a.h.split(","))
    grob3 = "3d_h%.3f" % max(float(q) for q in a.h.split(","))
    zweid = "2d_h%.3f" % a.h2d
    erg["tabelle"] = []
    log("Spalten: familie x | <S_phi>_s/S0 M_b | E(v=0,5) E(v=1) [innen wand aussen fuer v=1] | g/Knotenmenge c* |"
        " rel(3D fein - 2D) rel(3D grob - 3D fein) | |G|/|A1| gJmax-Anteil(v=1) | Algebra-Gegenprobe")
    for i, lg in enumerate(lagen):
        gi = {}
        for key in schluessel:
            gi[key] = {q: erg["gitter"][key][q][i] for q in GROESSEN}
        best = zweid if lg["koax"] else fein3
        z = zeile(lg, gi[best], info)
        z3f = zeile(lg, gi[fein3], info)
        z3g = zeile(lg, gi[grob3], info)
        rel_fein_2d = (z3f["E_v1.0"] - z["E_v1.0"]) / abs(z["E_v1.0"]) if lg["koax"] and z["E_v1.0"] != 0 else float("nan")
        rel_grob_fein = (z3g["E_v1.0"] - z3f["E_v1.0"]) / abs(z3f["E_v1.0"]) if z3f["E_v1.0"] != 0 else float("nan")
        z.update({"familie": lg["familie"], "typ": lg["typ"], "par": lg["par"], "d": lg["d"], "x": lg["x"],
                  "quelle": best, "rel_3dfein_minus_2d": rel_fein_2d, "rel_3dgrob_minus_3dfein": rel_grob_fein,
                  "G_abs_durch_A1_3dfein": z3f["G_abs_durch_A1"], "gJ_max_rel_v1.0_3dfein": z3f["gJ_max_rel_v1.0"],
                  "M_b": gi[best]["M_b"], "A1": gi[best]["A1"], "A2": gi[best]["A2"]})
        erg["tabelle"].append(z)
        log("%-10s %6.3f | %6.3f %9.3f | %11.4e %11.4e [%11.4e %11.4e %11.4e] | %8.4f %7.4f | %9.2e %9.2e | %8.1e %8.1e | %8.1e"
            % (lg["familie"], lg["x"], z["S_phi_mittel_durch_S0"], z["M_b"], z["E_v0.5"], z["E_v1.0"],
               z["E_v1.0_innen"], z["E_v1.0_wand"], z["E_v1.0_aussen"], z["g_je_Knotenmenge"], z["c_stern"],
               rel_fein_2d, rel_grob_fein, z3f["G_abs_durch_A1"], z3f["gJ_max_rel_v1.0"], z["D_rel_v1.0"]))

    # Kennzahlen je Familie
    erg["familien"] = {}
    for fam in sorted(set(lg["familie"] for lg in lagen)):
        idx = [i for i, lg in enumerate(lagen) if lg["familie"] == fam]
        T = [erg["tabelle"][i] for i in idx]
        k = {}
        for v in VS:
            Es = [t["E_v%.1f" % v] for t in T]
            j = int(np.argmin(Es))
            k["v%.1f" % v] = {"x_min": T[j]["x"], "E_min": Es[j], "E_x0": Es[0], "x0": T[0]["x"],
                              "Verhaeltnis_E_x0_zu_E_min": Es[0] / Es[j] if Es[j] != 0 else float("nan"),
                              "S_phi_mittel_durch_S0_bei_min": T[j]["S_phi_mittel_durch_S0"],
                              "max_E": max(Es)}
        gs = [t["g_je_Knotenmenge"] for t in T]
        j = int(np.argmin(gs))
        k["g_je_Knotenmenge_min"] = {"x": T[j]["x"], "g": gs[j], "S_phi_mittel_durch_S0": T[j]["S_phi_mittel_durch_S0"]}
        cs = np.array([t["c_stern"] for t in T], dtype=float)
        if np.isfinite(cs).any():
            j = int(np.nanargmin(cs))
            k["c_stern_min"] = {"x": T[j]["x"], "c_stern": float(cs[j])}
        erg["familien"][fam] = k
        log("Familie %s: %s" % (fam, json.dumps(k)))
    def ohne_nan(o):
        if isinstance(o, float):
            return o if math.isfinite(o) else None
        if isinstance(o, dict):
            return {q: ohne_nan(w) for q, w in o.items()}
        if isinstance(o, (list, tuple)):
            return [ohne_nan(w) for w in o]
        return o
    with open(a.out + ".json", "w") as fh:
        json.dump(ohne_nan(erg), fh, indent=1, allow_nan=False)
    log("geschrieben", a.out + ".json")


if __name__ == "__main__":
    main()
