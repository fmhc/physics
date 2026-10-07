#!/usr/bin/env python3
"""FA-1 Farb-Analogie, Runde 8 (v3, explorativ). Plan: PLAN.md (eingefroren 2026-09-30 06:54).

Drei Komponenten der Gesamtformel (gesamtformel-20260921/KANDIDAT.md 0 und 2.2), radial in 3D, J_ab = 1 fuer alle Paare:
  L = sum_a (|d_t psi_a|^2 - |grad psi_a|^2) - U(S) + g sum_{a<b} Re[(psi_a^* psi_b)^2]
  U(S) = S - S^2 + S^3/2,  S = sum_a |psi_a|^2
Radial mit u_a = r psi_a auf r_i = i h (i = 1..N), Rand u_0 = u_{N+1} = 0.
Ein stationaerer Ball mit festem innerem Vektor c (Stationaritaet von K(c) = sum_{a<b} Re[(c_a^* c_b)^2] auf |c| = 1)
ist exakt der N = 1-Ball mit U_b(S) = S - b S^2 + S^3/2, b = 1 + g K (PLAN 1.3).

Unterbefehle:
  ref    Schiessverfahren fuer Q_ref (N = 1, omega^2 = 0,70), stationaere Baelle aller Typen bei Q_ref (Newton bei festem Q),
         Energien, Virial, erste Ordnung, Barriere K = -1/9, Gitterprobe h = 0,05, Galerkin-Polynom (PLAN 1.7)
  fluss  Gradientenfluss der drei Komponenten bei festem Q aus zufaelligen Startphasen (E2 bis E6)
  dyn    Zeitentwicklung ohne Daempfung (Stoermer-Verlet, Schwamm am Rand) (D1 bis D9)
  rauch  kleine Fassung von allem
Geraet: cuda (Standard; ohne CUDA Abbruch, kein CPU-Ausweg) oder --geraet cpu (nur fuer den lokalen Rauchtest).
"""
import argparse
import json
import math
import os
import sys
import time

import numpy as np
import torch

F64 = torch.float64
C128 = torch.complex128
_trapz = getattr(np, "trapezoid", None) or getattr(np, "trapz")
PI4 = 4.0 * math.pi
START = time.time()
BUDGET = 540.0
S3 = math.sqrt(3.0)

# Zustandstypen: K-Wert und innerer Vektor (PLAN 1.3); k19 ist kein stationaerer Zustand, nur Wegpunkt (PLAN 1.8)
TYPEN = {
    "al3": (1.0 / 3.0, [1.0, 1.0, 1.0]),
    "al2": (0.25, [1.0, 1.0, 0.0]),
    "ein": (0.0, [1.0, 0.0, 0.0]),
    "k19": (-1.0 / 9.0, [1.0, 1j, 1j]),
    "d120": (-1.0 / 6.0, [1.0, complex(math.cos(math.pi / 3), math.sin(math.pi / 3)),
                          complex(math.cos(2 * math.pi / 3), math.sin(2 * math.pi / 3))]),
    "koll": (-0.2, [math.sqrt(0.6), 1j * math.sqrt(0.2), 1j * math.sqrt(0.2)]),
    "anti2": (-0.25, [1.0, 1j, 0.0]),
}
REIHENFOLGE_G_NEG = ["anti2", "koll", "d120", "ein", "al2", "al3"]   # erwartet aufsteigende Energie fuer g < 0


def vektor(name, chi=+1):
    c = np.array(TYPEN[name][1], dtype=complex)
    if name == "d120" and chi < 0:
        c = c.conj()
    return c / np.linalg.norm(c)


def K_von(c):
    c = np.asarray(c, dtype=complex)
    k = 0.0
    for a in range(3):
        for b in range(a + 1, 3):
            k += ((c[a].conjugate() * c[b]) ** 2).real
    return k


def stationaritaet(c):
    """Rest der Bedingung sum_{b != a} c_a^* c_b^2 = 2 K c_a (PLAN 1.3)."""
    c = np.asarray(c, dtype=complex)
    K = K_von(c)
    rest = [c[a].conjugate() * sum(c[b] ** 2 for b in range(3) if b != a) - 2 * K * c[a] for a in range(3)]
    return float(max(abs(x) for x in rest))


def uhr():
    return time.time() - START


def geraet_waehlen(name):
    if name == "cuda":
        if not torch.cuda.is_available():
            print("Kein CUDA-Geraet: Abbruch (kein CPU-Ausweg).", flush=True)
            sys.exit(4)
        dev = torch.device("cuda")
        print("Geraet:", torch.cuda.get_device_name(0), flush=True)
        return dev
    torch.set_num_threads(1)
    return torch.device("cpu")


def sync(dev):
    if dev.type == "cuda":
        torch.cuda.synchronize()


# ---------------------------------------------------------------- Gitteroperatoren
def gitter(h, R, dev):
    N = int(round(R / h))
    return torch.arange(1, N + 1, dtype=F64, device=dev) * h


def _pad(u):
    z = torch.zeros(u.shape[:-1] + (1,), dtype=u.dtype, device=u.device)
    return torch.cat([z, u, z], dim=-1)


def lap(u, h):
    up = _pad(u)
    return (up[..., 2:] - 2.0 * u + up[..., :-2]) / (h * h)


def grad2(u, h):
    up = _pad(u)
    d = (up[..., 1:] - up[..., :-1]) / h
    return (d.abs() ** 2).sum(-1) * h


def Uf(S, b):
    return S - b * S * S + 0.5 * S ** 3


def Up(S, b):
    return 1.0 - 2.0 * b * S + 1.5 * S * S


def Upp(S, b):
    return -2.0 * b + 3.0 * S


# ---------------------------------------------------------------- Schiessverfahren (Kontinuum, N = 1)
def schiessen(omega2, b, dev, r_max=40.0, hs=0.005, n_kand=64, runden=9):
    """Profil f(r) des N = 1-Balls mit U_b bei omega^2; Bisektion in Runden mit n_kand Kandidaten."""
    w2 = omega2
    d = b * b - 2.0 * (1.0 - w2)
    if d <= 0:
        return None
    S1 = b - math.sqrt(d)
    Sst = (2.0 * b + math.sqrt(4.0 * b * b - 6.0 * (1.0 - w2))) / 3.0
    lo, hi = math.sqrt(S1) * (1 + 1e-9), math.sqrt(Sst) * (1 - 1e-4)
    r0 = 1e-4
    n_schritte = int(r_max / hs)

    def rechte(r, f, fp):
        return fp, -2.0 * fp / r + (Up(f * f, b) - w2) * f

    def lauf(f0, aufzeichnen=False):
        f0 = torch.as_tensor(f0, dtype=F64, device=dev)
        c2 = (Up(f0 * f0, b) - w2) * f0 / 6.0
        f = f0 + c2 * r0 * r0
        fp = 2.0 * c2 * r0
        r = r0
        status = torch.zeros_like(f0)
        spur = [] if aufzeichnen else None
        for k in range(n_schritte):
            k1f, k1p = rechte(r, f, fp)
            k2f, k2p = rechte(r + hs / 2, f + hs / 2 * k1f, fp + hs / 2 * k1p)
            k3f, k3p = rechte(r + hs / 2, f + hs / 2 * k2f, fp + hs / 2 * k2p)
            k4f, k4p = rechte(r + hs, f + hs * k3f, fp + hs * k3p)
            f = f + hs / 6 * (k1f + 2 * k2f + 2 * k3f + k4f)
            fp = fp + hs / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
            r = r + hs
            neu_ueber = (f < 0) & (status == 0)
            neu_unter = (fp > 0) & (f > 0) & (status == 0)
            status = status + neu_ueber.to(F64) - neu_unter.to(F64)
            if aufzeichnen:
                spur.append((r, f.item(), fp.item(), status.item()))
                if status.item() != 0:
                    break
            elif k % 200 == 199 and bool((status != 0).all()):
                break
        return status, spur

    for _ in range(runden):
        f0 = torch.linspace(lo, hi, n_kand, dtype=F64, device=dev)
        status, _ = lauf(f0)
        st = status.cpu().numpy()
        unter = np.where(st < 0)[0]
        ueber = np.where(st > 0)[0]
        if len(unter) == 0 or len(ueber) == 0:
            break
        i = unter.max()
        if i + 1 >= n_kand or st[i + 1] <= 0:
            break
        f0c = f0.cpu().numpy()
        lo, hi = float(f0c[i]), float(f0c[i + 1])
        if hi - lo < 1e-15 * hi:
            break
    f0m = 0.5 * (lo + hi)
    _, spur = lauf(f0m, aufzeichnen=True)
    rr = np.array([s[0] for s in spur])
    ff = np.array([s[1] for s in spur])
    fpp = np.array([s[2] for s in spur])
    # Vertrauensbereich: bis 3 Einheiten vor dem Auseinanderlaufen; danach Schwanz A e^{-k r}/r
    r_div = rr[-1]
    k_as = math.sqrt(1.0 - w2)
    gut = rr < r_div - 3.0
    rm = rr[gut][-1]
    fm = ff[gut][-1]
    A = fm * rm * math.exp(k_as * rm)
    rg = np.arange(1, int(70.0 / hs) + 1) * hs
    fg = np.interp(rg, np.concatenate([[0.0], rr[gut]]), np.concatenate([[f0m], ff[gut]]))
    schwanz = rg > rm
    fg[schwanz] = A * np.exp(-k_as * rg[schwanz]) / rg[schwanz]
    fpg = np.gradient(fg, hs)
    w = math.sqrt(w2)
    S = fg * fg
    I2 = PI4 * _trapz(S * rg * rg, rg)
    Q = 2.0 * w * I2
    E = PI4 * _trapz((w2 * S + fpg * fpg + (S - b * S * S + 0.5 * S ** 3)) * rg * rg, rg)
    return {"f0": f0m, "f0_breite": hi - lo, "r_div": float(r_div), "r_anschluss": float(rm), "Q": Q, "E": E,
            "I2": I2, "I4": PI4 * _trapz(S * S * rg * rg, rg), "r": rg, "f": fg}


# ---------------------------------------------------------------- N = 1 bei festem Q: Fluss und Newton (Batch ueber b)
def n1_groessen(u, r, h, b, Q):
    S = u * u / (r * r)
    I = PI4 * h * (u * u).sum(-1)
    om = Q / (2.0 * I)
    T = PI4 * grad2(u, h)
    V = PI4 * h * (r * r * Uf(S, b)).sum(-1)
    E = om * om * I + T + V
    Vw = V - om * om * I
    I4 = PI4 * h * (u ** 4 / (r * r)).sum(-1)
    return {"E": E, "omega": om, "T": T, "Vw": Vw, "I2": I, "I4": I4}


def n1_fluss(u, r, h, b, Q, tau):
    dtau = 0.45 * h * h
    for _ in range(int(tau / dtau)):
        S = u * u / (r * r)
        I = PI4 * h * (u * u).sum(-1, keepdim=True)
        om = Q / (2.0 * I)
        u = u + dtau * (lap(u, h) + om * om * u - Up(S, b) * u)
    return u


def n1_newton(u, r, h, b, Q, iters=40, tol=1e-12):
    B, N = u.shape
    dev = u.device
    om = Q / (2.0 * PI4 * h * (u * u).sum(-1))
    D2 = (torch.diag(torch.full((N,), -2.0, dtype=F64, device=dev))
          + torch.diag(torch.ones(N - 1, dtype=F64, device=dev), 1)
          + torch.diag(torch.ones(N - 1, dtype=F64, device=dev), -1)) / (h * h)
    info = {"iter": 0, "schritt": float("nan"), "rest": float("nan")}
    bb = b.reshape(B, 1)
    for it in range(iters):
        S = u * u / (r * r)
        R1 = lap(u, h) + om[:, None] ** 2 * u - Up(S, bb) * u
        R2 = 2.0 * PI4 * h * om * (u * u).sum(-1) - Q
        J = torch.zeros(B, N + 1, N + 1, dtype=F64, device=dev)
        J[:, :N, :N] = D2 + torch.diag_embed(om[:, None] ** 2 - Up(S, bb) - 2.0 * S * Upp(S, bb))
        J[:, :N, N] = 2.0 * om[:, None] * u
        J[:, N, :N] = 4.0 * PI4 * h * om[:, None] * u
        J[:, N, N] = 2.0 * PI4 * h * (u * u).sum(-1)
        rhs = -torch.cat([R1, R2[:, None]], dim=1)
        dx = torch.linalg.solve(J, rhs.unsqueeze(-1)).squeeze(-1)
        u = u + dx[:, :N]
        om = om + dx[:, N]
        schritt = dx.abs().max(dim=1).values
        info = {"iter": it + 1, "schritt": schritt.cpu().tolist(), "rest": R1.abs().max(dim=1).values.cpu().tolist()}
        if bool((schritt < tol).all()):
            break
    S = u * u / (r * r)
    R1 = lap(u, h) + om[:, None] ** 2 * u - Up(S, bb) * u
    info["rest_end"] = R1.abs().max(dim=1).values.cpu().tolist()
    return u, om, info


def profile(b_liste, Q, h, R, dev, start_r, start_f, tau_fluss=300.0):
    """Stationaere N = 1-Profile bei festem Q fuer alle b (Fluss, dann Newton)."""
    r = gitter(h, R, dev)
    f0 = np.interp(r.cpu().numpy(), start_r, start_f)
    u0 = torch.as_tensor(f0, dtype=F64, device=dev) * r
    b = torch.tensor(b_liste, dtype=F64, device=dev)
    u = u0.unsqueeze(0).repeat(len(b_liste), 1)
    u = n1_fluss(u, r, h, b[:, None], Q, tau_fluss)
    u, om, info = n1_newton(u, r, h, b, Q)
    gr = n1_groessen(u, r, h, b[:, None], Q)
    ok = []
    for i in range(len(b_liste)):
        rest = info["rest_end"][i]
        smax = float((u[i] * u[i] / (r * r)).max())
        ok.append(bool(math.isfinite(rest) and rest < 1e-8 and smax > 0.05 and abs(float(om[i]) - float(gr["omega"][i])) < 1e-9))
    return r, u, om, gr, info, ok


# ---------------------------------------------------------------- Galerkin (PLAN 1.7)
def galerkin_120(omega, eps, gamma=0.0):
    """Innere Moden des 120-Grad-Balls, Sektor R = i: x'' + G x' + K x = 0, x = (p, q).

    P(nu) = nu^4 - (4 w^2 - 4 eps/3) nu^2 + 4 w eps nu - 2 eps^2/3; volles Spektrum = Nullstellen und deren Negative.
    Krein-Vorzeichen = Vorzeichen von H = nu^2 |v|^2 + v^H K v fuer reelle nu."""
    w = omega
    G = np.array([[0.0, 2 * w], [-2 * w, 0.0]], dtype=complex)
    K = -eps * np.array([[1.0 / 3.0, 1j], [-1j, 1.0]], dtype=complex)
    wurzeln = np.roots([1.0, 0.0, -(4 * w * w - 4 * eps / 3), 4 * w * eps, -2 * eps * eps / 3])
    moden = []
    for nu in wurzeln:
        if abs(nu.imag) < 1e-9 * max(1.0, abs(nu)):
            nu_r = nu.real
            M = -nu_r * nu_r * np.eye(2) + 1j * nu_r * G + K
            _, s, vh = np.linalg.svd(M)
            v = vh.conj()[-1]
            H = nu_r * nu_r * np.vdot(v, v).real + np.vdot(v, K @ v).real
            moden.append({"nu": float(nu_r), "krein": int(np.sign(H)), "H": float(H)})
        else:
            moden.append({"nu": [float(nu.real), float(nu.imag)], "krein": 0, "H": None})
    # erste Ordnung Daempfung: Begleitmatrix von x'' + (G + gamma I) x' + K x = 0
    A = np.zeros((4, 4), dtype=complex)
    A[:2, 2:] = np.eye(2)
    A[2:, :2] = -K
    A[2:, 2:] = -(G + gamma * np.eye(2))
    lam = np.linalg.eigvals(A)
    return {"moden": moden, "max_re_lambda": float(lam.real.max()), "lambda": [[float(x.real), float(x.imag)] for x in lam]}


def galerkin_schwellen(omega):
    """Kleinstes |eps|/omega^2, bei dem komplexe Nullstellen auftreten, getrennt fuer eps > 0 und eps < 0."""
    aus = {}
    for vz in (+1, -1):
        e_c = None
        for e in np.arange(0.001, 3.0, 0.001):
            eps = vz * e * omega * omega
            wz = np.roots([1.0, 0.0, -(4 * omega ** 2 - 4 * eps / 3), 4 * omega * eps, -2 * eps * eps / 3])
            if np.abs(wz.imag).max() > 1e-7:
                e_c = float(e)
                break
        aus["g>0" if vz > 0 else "g<0"] = e_c
    return aus


def lambda_ein(omega, eps):
    return math.sqrt(-2 * omega ** 2 + math.sqrt(4 * omega ** 4 + eps * eps))


# ---------------------------------------------------------------- drei Komponenten
def kopplung(u, r2, g):
    Z = (u * u).sum(1, keepdim=True)
    return g * u.conj() * (Z - u * u) / r2


def energie3(u, r, h, g, Q=None, v=None, maske=None):
    """E_Q (mit Q) bzw. Laborenergie (mit v). Rueckgabe je Batch."""
    r2 = r * r
    m = torch.ones_like(r) if maske is None else maske
    S = (u.abs() ** 2).sum(1) / r2
    up = _pad(u)
    d = (up[..., 1:] - up[..., :-1]) / h                      # Kante i liegt zwischen Punkt i und i+1, i = 0..N
    m_ext = torch.cat([torch.ones(1, dtype=F64, device=r.device), m])
    T = PI4 * h * ((d.abs() ** 2).sum(1) * m_ext).sum(-1)
    V = PI4 * h * (r2 * Uf(S, 1.0) * m).sum(-1)
    Z = (u * u).sum(1)
    q4 = (u.abs() ** 4).sum(1)
    C = -g.reshape(-1) * PI4 * h * (0.5 * (Z.abs() ** 2 - q4) / r2 * m).sum(-1)
    I = PI4 * h * ((u.abs() ** 2).sum(1) * m).sum(-1)
    if v is not None:
        kin = PI4 * h * ((v.abs() ** 2).sum(1) * m).sum(-1)
        return kin + T + V + C
    return Q * Q / (4.0 * I) + T + V + C


def messen(u, r, h, g, maske, v=None):
    r2 = r * r
    w = PI4 * h * (u * u * maske).sum(-1)                     # int psi_a^2 d^3x, (B, 3) komplex
    Na = PI4 * h * (u.abs() ** 2 * maske).sum(-1)
    n = Na / Na.sum(1, keepdim=True)
    Zw = w.sum(1).abs() / w.abs().sum(1)
    ph = torch.angle(w)
    zeta = torch.exp(1j * ph).sum(1).abs() / 3.0
    chi = (2.0 / (3.0 * S3)) * (torch.sin(ph[:, 1] - ph[:, 0]) + torch.sin(ph[:, 2] - ph[:, 1]) + torch.sin(ph[:, 0] - ph[:, 2]))
    T = []
    for a, b in ((0, 1), (1, 2), (2, 0)):
        T.append(-2.0 * g.reshape(-1) * PI4 * h * (((u[:, a].conj() * u[:, b]) ** 2).imag / r2 * maske).sum(-1))
    T = torch.stack(T, dim=1)
    aus = {"n": n, "Zw": Zw, "zeta": zeta, "chi": chi, "T": T}
    if v is not None:
        aus["Qa"] = -2.0 * PI4 * h * ((u.conj() * v).imag * maske).sum(-1)
    return aus


def einordnen(n, Zw, chi):
    ns = sorted(n, reverse=True)
    if ns[0] > 0.999:
        return "ein"
    if ns[2] < 1e-3 and abs(ns[0] - 0.5) < 1e-2 and abs(ns[1] - 0.5) < 1e-2:
        return "anti2" if Zw < 1e-2 else ("al2" if Zw > 0.99 else "paar?")
    if max(abs(x - 1.0 / 3.0) for x in n) < 1e-2:
        if Zw < 1e-2:
            return "d120+" if chi > 0 else "d120-"
        if Zw > 0.99:
            return "al3"
    if abs(ns[0] - 0.6) < 1e-2 and abs(ns[1] - 0.2) < 1e-2 and abs(ns[2] - 0.2) < 1e-2:
        return "koll"
    return "anderes"


# ---------------------------------------------------------------- Q_ref
def q_ref_bestimmen(dev, kurz=False, cache=None):
    t0 = uhr()
    if cache and not kurz and os.path.exists(cache):
        z = np.load(cache)
        sch = json.loads(str(z["meta"]))
        sch["r"], sch["f"] = z["r"], z["f"]
        print(f"Q_ref aus {cache}: Q_ref = {sch['Q']:.10f}, E = {sch['E']:.10f}", flush=True)
        return sch
    if kurz:
        sch = schiessen(0.70, 1.0, dev, r_max=30.0, hs=0.01, n_kand=32, runden=5)
    else:
        sch = schiessen(0.70, 1.0, dev)
    sync(dev)
    if cache and not kurz:
        meta = {k: float(v) for k, v in sch.items() if k not in ("r", "f")}
        np.savez(cache, r=sch["r"], f=sch["f"], meta=json.dumps(meta))
    print(f"Schiessen omega^2 = 0,70: f0 = {sch['f0']:.15f} (Breite {sch['f0_breite']:.2e}), Q_ref = {sch['Q']:.10f}, "
          f"E = {sch['E']:.10f}, r_div = {sch['r_div']:.2f}, {uhr() - t0:.1f} s", flush=True)
    return sch


# ---------------------------------------------------------------- Unterbefehl ref
def cmd_ref(a, dev):
    kurz = a.kurz
    sch = q_ref_bestimmen(dev, kurz, a.cache)
    Q = sch["Q"]
    g_liste = [-1.0, -0.6, -0.3, -0.1, 0.1, 0.3, 0.6] if not kurz else [-0.3, 0.3]
    typen = ["al3", "al2", "ein", "k19", "d120", "koll", "anti2"]
    h, R = (0.1, 70.0) if not kurz else (0.2, 30.0)
    paare = [(g, t) for g in g_liste for t in typen]
    b_liste = sorted(set(round(1.0 + g * TYPEN[t][0], 12) for g, t in paare))
    t0 = uhr()
    r, u, om, gr, info, ok = profile(b_liste, Q, h, R, dev, sch["r"], sch["f"], tau_fluss=300.0 if not kurz else 20.0)
    sync(dev)
    print(f"Profile ({len(b_liste)} b-Werte, h = {h}): {uhr() - t0:.1f} s, Newton {info['iter']} Schritte", flush=True)
    je_b = {}
    for i, b in enumerate(b_liste):
        je_b[b] = {"b": b, "ok": ok[i], "omega": float(om[i]), "omega2": float(om[i]) ** 2, "E": float(gr["E"][i]),
                   "I2": float(gr["I2"][i]), "I4": float(gr["I4"][i]), "kappa": float(gr["I4"][i] / gr["I2"][i]),
                   "virial": float((gr["T"][i] + 3 * gr["Vw"][i]) / gr["T"][i]), "rest": info["rest_end"][i],
                   "Smax": float((u[i] * u[i] / (r * r)).max()), "omega2_min": 1.0 - b * b / 2.0}
    ein = je_b[1.0]
    tabelle = []
    for g in g_liste:
        zeile = {"g": g, "typen": {}}
        for t in typen:
            b = round(1.0 + g * TYPEN[t][0], 12)
            d = dict(je_b[b])
            d["K"] = TYPEN[t][0]
            d["dE_zu_ein"] = d["E"] - ein["E"]
            d["erste_ordnung"] = (-g * TYPEN[t][0] * ein["I4"])
            d["verhaeltnis_erste_ordnung"] = (d["dE_zu_ein"] / d["erste_ordnung"]) if TYPEN[t][0] != 0 else None
            zeile["typen"][t] = d
        stat = [t for t in typen if t != "k19" and zeile["typen"][t]["ok"]]
        erwartet = REIHENFOLGE_G_NEG if g < 0 else list(reversed(REIHENFOLGE_G_NEG))
        erwartet = [t for t in erwartet if t in stat]
        gefunden = sorted(stat, key=lambda t: zeile["typen"][t]["E"])
        zeile["reihenfolge_erwartet"] = erwartet
        zeile["reihenfolge_gefunden"] = gefunden
        zeile["reihenfolge_ok"] = (erwartet == gefunden)
        zeile["barriere_k19_minus_d120"] = zeile["typen"]["k19"]["E"] - zeile["typen"]["d120"]["E"]
        zeile["barriere_erwartet"] = abs(g) * ein["I4"] / 18.0 if g < 0 else None
        zeile["d120_minus_anti2"] = zeile["typen"]["d120"]["E"] - zeile["typen"]["anti2"]["E"]
        zeile["d120_minus_anti2_erwartet"] = -g * (-1.0 / 6.0 + 0.25) * ein["I4"]
        # Galerkin am 120-Grad-Ball dieses g
        d120 = zeile["typen"]["d120"]
        eps = g * d120["kappa"]
        gal = galerkin_120(d120["omega"], eps)
        gal_d = galerkin_120(d120["omega"], eps, gamma=1e-3)
        for m in gal["moden"]:
            if isinstance(m["nu"], float):
                m["eingebettet"] = bool(abs(m["nu"]) > 1.0 - d120["omega"])
        zeile["galerkin_120"] = {"omega": d120["omega"], "kappa": d120["kappa"], "eps": eps,
                                 "e_durch_omega2": abs(eps) / d120["omega"] ** 2, "moden": gal["moden"],
                                 "max_re_lambda": gal["max_re_lambda"], "max_re_lambda_gamma_1e-3": gal_d["max_re_lambda"],
                                 "schwelle_kontinuum": 1.0 - d120["omega"],
                                 "nu_klein_formel": [abs(eps) / (2 * d120["omega"]) * (1 + 1 / S3),
                                                     abs(eps) / (2 * d120["omega"]) * (1 - 1 / S3)]}
        e1 = zeile["typen"]["ein"]
        zeile["lambda_ein_zwei_moden"] = lambda_ein(e1["omega"], g * e1["kappa"])
        tabelle.append(zeile)
        print(f"g = {g:+.2f}: Reihenfolge {'ok' if zeile['reihenfolge_ok'] else 'ABWEICHUNG'} {gefunden}; "
              f"E_120 - E_anti2 = {zeile['d120_minus_anti2']:.6f} (1. Ordnung {zeile['d120_minus_anti2_erwartet']:.6f}); "
              f"Barriere k19 {zeile['barriere_k19_minus_d120']:.6f} (erw. {zeile['barriere_erwartet']})", flush=True)
        print("   Galerkin 120:", json.dumps({"e/w2": round(zeile['galerkin_120']['e_durch_omega2'], 4),
                                            "moden": gal["moden"], "Schwelle": round(1.0 - d120['omega'], 5),
                                            "maxRe(gamma=1e-3)": gal_d["max_re_lambda"]}), flush=True)
    stat_check = {t: stationaritaet(vektor(t)) for t in TYPEN}
    stat_check["d120-"] = stationaritaet(vektor("d120", -1))
    K_check = {t: K_von(vektor(t)) for t in TYPEN}
    schw = galerkin_schwellen(je_b[round(1.0 + 0.3 / 6.0, 12)]["omega"] if not kurz else ein["omega"])
    aus = {"schiessen": {k: v for k, v in sch.items() if k not in ("r", "f")}, "Q_ref": Q, "h": h, "R": R,
           "je_b": {str(k): v for k, v in je_b.items()}, "tabelle": tabelle, "stationaritaet_rest": stat_check,
           "K_werte": K_check, "galerkin_schwellen_e_durch_omega2_bei_omega_d120_g-0.3": schw,
           "gitterkontrolle": {"omega2_FD_ein": ein["omega2"], "omega2_schiessen": 0.70,
                               "E_FD_ein": ein["E"], "E_schiessen": sch["E"]}}
    print("Stationaritaet (Rest):", stat_check, flush=True)
    print("Galerkin-Schwellen e/omega^2:", schw, flush=True)
    print(f"Gitter: omega^2 FD {ein['omega2']:.8f} gegen 0,70; E FD {ein['E']:.8f} gegen Schiessen {sch['E']:.8f}", flush=True)
    # Gitterprobe h = 0,05 bei g = -0,3
    if not kurz and uhr() < BUDGET - 200:
        g = -0.3
        b2 = [round(1.0 + g * TYPEN[t][0], 12) for t in typen]
        t0 = uhr()
        r5, u5, om5, gr5, info5, ok5 = profile(b2, Q, 0.05, 70.0, dev, sch["r"], sch["f"], tau_fluss=150.0)
        sync(dev)
        fein = {t: {"E": float(gr5["E"][i]), "omega2": float(om5[i]) ** 2, "ok": ok5[i]} for i, t in enumerate(typen)}
        ref_ein = fein["ein"]["E"]
        grob = {t: tabelle[g_liste.index(g)]["typen"][t] for t in typen}
        aus["gitterprobe_h005_g-0.3"] = {t: {"E_h005": fein[t]["E"], "E_h01": grob[t]["E"],
                                            "dE_zu_ein_h005": fein[t]["E"] - ref_ein,
                                            "dE_zu_ein_h01": grob[t]["dE_zu_ein"], "ok": fein[t]["ok"]} for t in typen}
        print(f"Gitterprobe h = 0,05 ({uhr() - t0:.1f} s):", json.dumps(aus["gitterprobe_h005_g-0.3"]), flush=True)
    return aus


# ---------------------------------------------------------------- Unterbefehl fluss
def cmd_fluss(a, dev):
    kurz = a.kurz
    sch = q_ref_bestimmen(dev, kurz, a.cache)
    Q = sch["Q"]
    h, R = (0.1, 70.0) if not kurz else (0.2, 30.0)
    laeufe = []
    if kurz:
        laeufe = [dict(g=-0.3, art="frei", seed=1, amp="gleich"), dict(g=-0.3, art="gleich", seed=2, amp="gleich"),
                  dict(g=-0.3, art="frei", seed=0, amp="ein")]
    else:
        for s in range(6):
            laeufe.append(dict(g=-0.3, art="frei", seed=100 + s, amp="gleich"))
        for s in range(6):
            laeufe.append(dict(g=-0.3, art="gleich", seed=200 + s, amp="gleich"))
        for s in range(3):
            laeufe.append(dict(g=-0.3, art="frei", seed=300 + s, amp="zufall"))
        for s in range(3):
            laeufe.append(dict(g=0.3, art="frei", seed=400 + s, amp="gleich"))
        for s in range(3):
            laeufe.append(dict(g=0.0, art="frei", seed=500 + s, amp="gleich"))
        laeufe.append(dict(g=-0.3, art="frei", seed=0, amp="ein"))
        for s in range(3):
            laeufe.append(dict(g=-0.6, art="frei", seed=600 + s, amp="gleich"))
        for s in range(3):
            laeufe.append(dict(g=-0.6, art="gleich", seed=700 + s, amp="gleich"))
    g_werte = sorted(set(L["g"] for L in laeufe))
    typen = ["al3", "al2", "ein", "d120", "koll", "anti2"]
    b_liste = sorted(set(round(1.0 + g * TYPEN[t][0], 12) for g in g_werte for t in typen))
    r, uprof, om, gr, info, ok = profile(b_liste, Q, h, R, dev, sch["r"], sch["f"], tau_fluss=300.0 if not kurz else 20.0)
    E_ref = {}
    for g in g_werte:
        E_ref[g] = {t: float(gr["E"][b_liste.index(round(1.0 + g * TYPEN[t][0], 12))]) for t in typen}
    u_ein = uprof[b_liste.index(1.0)]
    B = len(laeufe)
    u = torch.zeros(B, 3, u_ein.shape[0], dtype=C128, device=dev)
    c0 = []
    for i, L in enumerate(laeufe):
        rng = np.random.default_rng(L["seed"])
        if L["amp"] == "ein":
            c = np.array([1.0, 0.0, 0.0], dtype=complex)
        else:
            if L["amp"] == "gleich":
                x = np.ones(3) / 3.0 * (1.0 + 1e-3 * rng.standard_normal(3))
            else:
                x = rng.dirichlet(np.ones(3))
            ph = rng.uniform(0.0, 2 * math.pi, 3)
            c = np.sqrt(x / x.sum()) * np.exp(1j * ph)
        c0.append(c)
        u[i] = torch.as_tensor(c, dtype=C128, device=dev)[:, None] * u_ein.to(C128)[None, :]
    g = torch.tensor([L["g"] for L in laeufe], dtype=F64, device=dev).reshape(B, 1, 1)
    gleich = torch.tensor([1.0 if L["art"] == "gleich" else 0.0 for L in laeufe], dtype=F64, device=dev).reshape(B, 1, 1)
    r2 = r * r
    maske = torch.ones_like(r)
    dtau = 0.45 * h * h
    tau_max = a.tau if not kurz else 20.0
    n_mess = max(1, int(1.0 / dtau))
    spur = []
    t0 = uhr()
    anfang = messen(u, r, h, g, maske)
    k = 0
    tau = 0.0
    while tau < tau_max and uhr() < BUDGET - 60:
        S = (u.abs() ** 2).sum(1, keepdim=True) / r2
        I = PI4 * h * (u.abs() ** 2).sum((1, 2), keepdim=True)
        om2 = (Q / (2.0 * I)) ** 2
        u = u + dtau * (lap(u, h) + om2 * u - Up(S, 1.0) * u + kopplung(u, r2, g))
        # erzwungen gleiche Amplituden: Kanalnormen auf I/3 (Gesamtnorm unveraendert)
        Ia = PI4 * h * (u.abs() ** 2).sum(-1, keepdim=True)
        Ig = Ia.sum(1, keepdim=True)
        fak = torch.where(gleich > 0, torch.sqrt((Ig / 3.0) / Ia.clamp_min(1e-300)), torch.ones_like(Ia))
        u = u * fak
        k += 1
        tau += dtau
        if k % n_mess == 0:
            m = messen(u, r, h, g, maske)
            E = energie3(u, r, h, g, Q=Q)
            spur.append([tau] + [m[x].cpu().tolist() for x in ("n", "Zw", "zeta", "chi")] + [E.cpu().tolist()])
    sync(dev)
    print(f"Fluss: tau = {tau:.1f}, {k} Schritte, {uhr() - t0:.1f} s", flush=True)
    m = messen(u, r, h, g, maske)
    E = energie3(u, r, h, g, Q=Q)
    S = (u.abs() ** 2).sum(1, keepdim=True) / r2
    I = PI4 * h * (u.abs() ** 2).sum((1, 2), keepdim=True)
    om2 = (Q / (2.0 * I)) ** 2
    rest = (lap(u, h) + om2 * u - Up(S, 1.0) * u + kopplung(u, r2, g)).abs().amax(dim=(1, 2))
    ergebnisse = []
    for i, L in enumerate(laeufe):
        n = m["n"][i].cpu().tolist()
        Zw = float(m["Zw"][i])
        chi = float(m["chi"][i])
        typ = einordnen(n, Zw, chi)
        Ei = float(E[i])
        refs = E_ref[L["g"]]
        naechst = min(refs, key=lambda t: abs(refs[t] - Ei))
        ergebnisse.append({**L, "c0_betrag2": [float(abs(x) ** 2) for x in c0[i]],
                           "c0_phase2_grad": [float(np.degrees(np.angle(x ** 2))) for x in c0[i]],
                           "chi_anfang": float(anfang["chi"][i]), "Zw_anfang": float(anfang["Zw"][i]),
                           "n_ende": n, "Zw_ende": Zw, "zeta_ende": float(m["zeta"][i]), "chi_ende": chi,
                           "T_ende": m["T"][i].cpu().tolist(), "typ_ende": typ, "E_ende": Ei,
                           "naechster_ref": naechst, "E_ref_naechst": refs[naechst],
                           "dE_rel_zum_ref": (Ei - refs[naechst]) / abs(refs[naechst]), "rest_stationaer": float(rest[i]),
                           "kanal_2_3_max_abs": float(u[i, 1:].abs().max())})
        print(f"{i:2d} g={L['g']:+.1f} {L['art']:6s} {L['amp']:6s}: Ende {typ:8s} n={[round(x, 5) for x in n]} "
              f"Zw={Zw:.2e} chi={chi:+.4f} E={Ei:.8f} ~ {naechst} ({(Ei - refs[naechst]) / abs(refs[naechst]):+.1e}) "
              f"Rest {float(rest[i]):.1e}", flush=True)
    return {"Q_ref": Q, "h": h, "R": R, "tau": tau, "E_ref": {str(k): v for k, v in E_ref.items()},
            "laeufe": ergebnisse, "spur_jede_10": spur[::10], "profil_ok": dict(zip([str(b) for b in b_liste], ok))}


# ---------------------------------------------------------------- Unterbefehl dyn
def cmd_dyn(a, dev):
    kurz = a.kurz
    sch = q_ref_bestimmen(dev, kurz, a.cache)
    Q = sch["Q"]
    h, R, r_s = (0.1, 70.0, 45.0) if not kurz else (0.2, 30.0, 20.0)
    R_in = 40.0 if not kurz else 18.0
    if kurz:
        laeufe = [dict(typ="d120", g=-0.3, delta=1e-3, chi=+1), dict(typ="ein", g=-0.3, keim=1e-6),
                  dict(typ="ein", g=-0.3, keim=0.0)]
    else:
        laeufe = [dict(typ="d120", g=gg, delta=1e-3, chi=+1) for gg in (-0.1, -0.3, -0.6, -1.0, 0.1, 0.3, 0.6, 0.0)]
        laeufe += [dict(typ="ein", g=-0.3, keim=1e-6), dict(typ="ein", g=-0.3, keim=0.0),
                   dict(typ="anti2", g=-0.3, delta=1e-3, keim=1e-3),
                   dict(typ="d120", g=-0.3, delta=0.05, chi=+1), dict(typ="d120", g=-0.3, delta=0.15, chi=+1),
                   dict(typ="d120", g=-0.3, delta=1e-3, chi=-1)]
    b_liste = sorted(set(round(1.0 + L["g"] * TYPEN[L["typ"]][0], 12) for L in laeufe))
    r, uprof, om, gr, info, ok = profile(b_liste, Q, h, R, dev, sch["r"], sch["f"], tau_fluss=300.0 if not kurz else 20.0)
    B = len(laeufe)
    N = r.shape[0]
    u = torch.zeros(B, 3, N, dtype=C128, device=dev)
    v = torch.zeros_like(u)
    info_l = []
    for i, L in enumerate(laeufe):
        j = b_liste.index(round(1.0 + L["g"] * TYPEN[L["typ"]][0], 12))
        P = uprof[j].to(C128)
        w = float(om[j])
        c = vektor(L["typ"], L.get("chi", +1))
        rng = np.random.default_rng(1000 + i)
        d = L.get("delta", 0.0)
        if d > 0:
            xi = rng.standard_normal(3)
            xi = xi - xi.mean()
            eta = rng.standard_normal(3)
            c = c * (1.0 + d * xi) * np.exp(1j * d * eta)
        uu = torch.as_tensor(c, dtype=C128, device=dev)[:, None] * P[None, :]
        keim = L.get("keim", None)
        if keim is not None and L["typ"] == "ein":
            ph = rng.uniform(0, 2 * math.pi, 2)
            uu[1] = keim * np.exp(1j * ph[0]) * P
            uu[2] = keim * np.exp(1j * ph[1]) * P
        if keim is not None and L["typ"] == "anti2":
            uu[2] = keim * np.exp(1j * rng.uniform(0, 2 * math.pi)) * P / math.sqrt(2.0)
        u[i] = uu
        v[i] = -1j * w * uu
        info_l.append({"omega": w, "b": b_liste[j], "kappa": float(gr["I4"][j] / gr["I2"][j]), "I4": float(gr["I4"][j]),
                       "E_stat": float(gr["E"][j]), "profil_ok": ok[j]})
    g = torch.tensor([L["g"] for L in laeufe], dtype=F64, device=dev).reshape(B, 1, 1)
    r2 = r * r
    maske = (r < R_in).to(F64)
    gam = torch.where(r > r_s, 1.0 * ((r - r_s) / (R - r_s)) ** 2, torch.zeros_like(r))
    dt = 0.5 * h
    daempf = torch.exp(-gam * dt / 2.0).to(C128)

    def beschl(u):
        S = (u.abs() ** 2).sum(1, keepdim=True) / r2
        return lap(u, h) - Up(S, 1.0) * u + kopplung(u, r2, g)

    T_end = a.T if not kurz else 20.0
    dt_mess = 0.5
    n_mess = int(round(dt_mess / dt))
    reihen = {x: [] for x in ("t", "n", "Zw", "zeta", "chi", "T", "Qa", "E_in", "E_tot", "Q_in", "leer")}

    def aufnehmen(t, u, v):
        m = messen(u, r, h, g, maske, v=v)
        reihen["t"].append(t)
        for x in ("n", "Zw", "zeta", "chi", "T", "Qa"):
            reihen[x].append(m[x].cpu())
        reihen["E_in"].append(energie3(u, r, h, g, v=v, maske=maske).cpu())
        reihen["E_tot"].append(energie3(u, r, h, g, v=v).cpu())
        reihen["Q_in"].append(m["Qa"].sum(1).cpu())
        reihen["leer"].append(u[:, 1:].abs().amax(dim=(1, 2)).cpu())

    acc = beschl(u)
    aufnehmen(0.0, u, v)
    t = 0.0
    k = 0
    t0 = uhr()
    while t < T_end - 1e-9:
        v = v * daempf
        v = v + 0.5 * dt * acc
        u = u + dt * v
        acc = beschl(u)
        v = v + 0.5 * dt * acc
        v = v * daempf
        k += 1
        t = k * dt
        if k % n_mess == 0:
            aufnehmen(t, u, v)
            if k % (n_mess * 200) == 0 and uhr() > BUDGET - 45:
                print(f"Zeitwaechter: Abbruch bei t = {t:.1f}", flush=True)
                break
    sync(dev)
    print(f"Dynamik: T = {t:.1f}, {k} Schritte, {uhr() - t0:.1f} s", flush=True)
    tt = np.array(reihen["t"])
    n = torch.stack(reihen["n"]).numpy()          # (M, B, 3)
    chi = torch.stack(reihen["chi"]).numpy()
    Zw = torch.stack(reihen["Zw"]).numpy()
    T = torch.stack(reihen["T"]).numpy()          # (M, B, 3)
    Qa = torch.stack(reihen["Qa"]).numpy()
    E_in = torch.stack(reihen["E_in"]).numpy()
    E_tot = torch.stack(reihen["E_tot"]).numpy()
    Q_in = torch.stack(reihen["Q_in"]).numpy()
    leer = torch.stack(reihen["leer"]).numpy()
    ergebnisse = []
    for i, L in enumerate(laeufe):
        I = info_l[i]
        e = {**L, **I}
        if L["typ"] == "d120":
            dev_t = np.abs(n[:, i, :] - 1.0 / 3.0).max(axis=1)
        elif L["typ"] == "ein":
            dev_t = n[:, i, 1] + n[:, i, 2]
        else:
            dev_t = n[:, i, 2] + np.abs(n[:, i, 0] - n[:, i, 1])
        e["abw_anfang"] = float(dev_t[0])
        e["abw_max"] = float(dev_t.max())
        e["abw_ende"] = float(dev_t[-1])
        e["abw_max_letztes_viertel"] = float(dev_t[3 * len(dev_t) // 4:].max())
        e["t_max_abw"] = float(tt[int(dev_t.argmax())])
        e["n_min_min"] = float(n[:, i, :].min())
        e["chi_min"] = float(chi[:, i].min())
        e["chi_max"] = float(chi[:, i].max())
        e["chi_ende"] = float(chi[-1, i])
        e["Zw_max"] = float(Zw[:, i].max())
        e["n_ende"] = n[-1, i].tolist()
        e["typ_ende"] = einordnen(n[-1, i].tolist(), float(Zw[-1, i]), float(chi[-1, i]))
        e["dE_in_rel_max"] = float(np.abs(E_in[:, i] - E_in[0, i]).max() / abs(E_in[0, i]))
        e["dE_tot_rel_ende"] = float((E_tot[-1, i] - E_tot[0, i]) / abs(E_tot[0, i]))
        e["dQ_in_rel_max"] = float(np.abs(Q_in[:, i] - Q_in[0, i]).max() / abs(Q_in[0, i]))
        e["leer_max"] = float(leer[:, i].max())
        # Kreisstrom und Kanalbilanz
        Tm = T[:, i, :]
        e["T_mittel"] = Tm.mean(axis=0).tolist()
        e["T_erwartet_betrag"] = S3 / 9.0 * abs(L["g"]) * I["I4"] if L["typ"] == "d120" else None
        if len(tt) > 3:
            dQ = np.gradient(Qa[:, i, :], tt, axis=0)
            bil = np.stack([Tm[:, 0] - Tm[:, 2], Tm[:, 1] - Tm[:, 0], Tm[:, 2] - Tm[:, 1]], axis=1)  # sum_b T_ab
            e["dQa_dt_mittel_betrag"] = float(np.abs(dQ).mean())
            e["bilanz_rest_mittel"] = float(np.abs(dQ - bil).mean())
            e["T_betrag_mittel"] = float(np.abs(Tm).mean())
        # Wachstumsrate
        if L["typ"] == "ein" and L.get("keim", 0) > 0:
            sel = (dev_t > 1e-10) & (dev_t < 1e-4)
            if sel.sum() > 5:
                p = np.polyfit(tt[sel], np.log(dev_t[sel]), 1)
                e["lambda_gemessen"] = float(p[0] / 2.0)
            e["lambda_zwei_moden"] = lambda_ein(I["omega"], L["g"] * I["kappa"])
        elif dev_t.max() > 10 * max(dev_t[0], 1e-12):
            i1 = int(np.argmax(dev_t > 3 * dev_t[0]))
            i2 = int(np.argmax(dev_t > min(0.3 * dev_t.max(), 100 * dev_t[0])))
            if i2 > i1 + 3:
                p = np.polyfit(tt[i1:i2], np.log(dev_t[i1:i2]), 1)
                e["rate_gemessen"] = float(p[0])
        # langsame Frequenzen: FFT von n_1 (Hann), Spitzen in [0,004; 1,2]
        y = n[:, i, 0] - n[:, i, 0].mean()
        if len(y) > 64:
            wfen = np.hanning(len(y))
            sp = np.abs(np.fft.rfft(y * wfen))
            fr = 2 * math.pi * np.fft.rfftfreq(len(y), d=dt_mess)
            sel = (fr > 0.004) & (fr < 1.2)
            idx = np.where(sel)[0]
            spitzen = []
            for j in idx[1:-1]:
                if sp[j] > sp[j - 1] and sp[j] >= sp[j + 1]:
                    spitzen.append((float(sp[j]), float(fr[j])))
            spitzen.sort(reverse=True)
            e["fft_spitzen_nu"] = [x[1] for x in spitzen[:4]]
            e["fft_spitzen_hoehe"] = [x[0] for x in spitzen[:4]]
            e["fft_aufloesung"] = float(2 * math.pi / (tt[-1] - tt[0]))
        if L["typ"] == "d120":
            gal = galerkin_120(I["omega"], L["g"] * I["kappa"])
            e["galerkin"] = gal["moden"]
            e["galerkin_max_re_lambda"] = gal["max_re_lambda"]
            e["schwelle_kontinuum"] = 1.0 - I["omega"]
        ergebnisse.append(e)
        print(json.dumps({k2: (round(v2, 7) if isinstance(v2, float) else v2) for k2, v2 in e.items()
                          if k2 not in ("galerkin",)}), flush=True)
        if "galerkin" in e:
            print("   Galerkin:", json.dumps(e["galerkin"]), flush=True)
    stueck = max(1, len(tt) // 2000)
    reihe_aus = {"t": tt[::stueck].tolist(), "n": n[::stueck].tolist(), "chi": chi[::stueck].tolist(),
                 "Zw": Zw[::stueck].tolist(), "T": T[::stueck].tolist()}
    return {"Q_ref": Q, "h": h, "R": R, "r_schwamm": r_s, "R_innen": R_in, "dt": dt, "T": t, "laeufe": ergebnisse,
            "reihen": reihe_aus}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("befehl", choices=["ref", "fluss", "dyn", "rauch"])
    ap.add_argument("--geraet", default="cuda", choices=["cuda", "cpu"])
    ap.add_argument("--out", required=True)
    ap.add_argument("--kurz", action="store_true")
    ap.add_argument("--tau", type=float, default=600.0)
    ap.add_argument("--T", type=float, default=5000.0)
    ap.add_argument("--cache", default="schiessen-070.npz")
    a = ap.parse_args()
    dev = geraet_waehlen(a.geraet)
    os.makedirs(a.out, exist_ok=True)
    print(f"FA-1 {a.befehl} start {time.strftime('%Y-%m-%d %H:%M:%S %Z')}, torch {torch.__version__}", flush=True)
    if a.befehl == "rauch":
        a.kurz = True
        aus = {"ref": cmd_ref(a, dev), "fluss": cmd_fluss(a, dev), "dyn": cmd_dyn(a, dev)}
    elif a.befehl == "ref":
        aus = cmd_ref(a, dev)
    elif a.befehl == "fluss":
        aus = cmd_fluss(a, dev)
    else:
        aus = cmd_dyn(a, dev)
    aus["_meta"] = {"befehl": a.befehl, "kurz": a.kurz, "sekunden": uhr(), "torch": torch.__version__,
                    "geraet": str(dev), "ende": time.strftime('%Y-%m-%d %H:%M:%S %Z')}
    with open(os.path.join(a.out, f"ERGEBNIS-{a.befehl}.json"), "w") as fh:
        json.dump(aus, fh, indent=1, default=float)
    print(f"FA-1 {a.befehl} ende {time.strftime('%Y-%m-%d %H:%M:%S %Z')}, {uhr():.1f} s", flush=True)


if __name__ == "__main__":
    main()
