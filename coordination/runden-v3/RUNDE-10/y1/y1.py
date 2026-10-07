#!/usr/bin/env python3
"""Runde 10 (v3), Karte Y-1: Wirbel-Dreier (N = 3) in einem gemischten Ball, Energie gegen Geometrie (Y oder Dreieck).
Kopie von RUNDE-09/rot1/rot1.py (sha256 5a08be3e...), unveraendert bis auf diesen Kopf, die neuen Unterbefehle am Ende
(Abschnitt "Y-1") und main(). Plan und Vorab: PLAN.md daneben.
    N = 3, J_ab = 1:  L = sum_a (|psi_a,t|^2 - |grad psi_a|^2) - U(S) + g sum_{a<b} Re[(psi_a^* psi_b)^2] [+ c sum_a |psi_a|^4
    nur im zweiten Arm]; Kopplungskraft g psi_a^* (P - psi_a^2), P = sum_b psi_b^2.
Neue Unterbefehle: k1, meson, dreier_neutral, dreier_y, dreier_kette, dreier02, null, fein, auswertung.

Urspruenglicher Kopf von rot1.py:
Runde 9 (v3), Karte ROT-1: Wirbel mit gefuelltem Kern und Waende der relativen Phase. 2D-Querschnitt, N = 2, J = 1.

Modell (KANDIDAT.md 2.2, selbst nachgeprueft, PLAN.md 1):
    L = sum_a (|psi_a,t|^2 - |grad psi_a|^2) - U(S) + g Re[(psi_1^* psi_2)^2],  U = S - S^2 + S^3/2
    psi_a,tt - lap psi_a + U'(S) psi_a - g psi_a^* psi_b^2 = 0
    Ladung Q_a = int 2 Im(psi_a conj(psi_a,t)) (wie ring.py), Energie mit - g Re[...], J_z = sum_a int (x p_y - y p_x).

Unterbefehle (Plan, Vorab und Aufrufe in PLAN.md daneben):
    radial  g = 0: radialer Gradientenfluss bei festen Q_1 (m = 1) und Q_2 (m = 0); gefuellte Wirbel, Vergleichsobjekte,
            Virial und dE/dQ.
    dyn0    g = 0: 2D-Zeitentwicklung gefuellter und einkomponentiger Wirbel mit Saat 0,01 (Teilung, Kernaustritt).
    dyng    g != 0 (Rampe bis t = 50): Waende der relativen Phase, Musterdrehung, Schicksal; Symmetrieprobe g <-> -g.
    paar    statisch: psi_1-Wirbel bei (-d/2, 0), psi_2-Wirbel bei (+d/2, 0) in einem grossen gemischten Ball, E(d).
    alle    nur mit --rauch.
Grundlage: Gitter, Randschicht, Verlet, Stoerfaktor, Komponenten und Kreisabtastung wie RUNDE-07/ring/ring.py
(dort aus r5_2d_a/b.py), hier zweikomponentig neu geschrieben.

Aufruf: python rot1.py KARTE [--rauch] [--stufe grob|fein] [--laeufe A,B] [--out ORDNER] [--geraet cuda|cpu] [--budget s]
--geraet cpu nur fuer den lokalen Rauchtest (--rauch).
"""
import argparse
import cmath
import datetime
import json
import math
import os
import time
import traceback

import torch

DEV = torch.device("cuda")
F64 = torch.float64
C128 = torch.complex128

# ---------------------------------------------------------------- Festlegungen (PLAN.md 1 bis 3)
RH, RMAX = 0.05, 40.0              # radiales Zellmittengitter
R_TAU, R_IT, R_TOL = 0.25, 60000, 1e-10
SPONGE, SIGMA0 = 8.0, 1.0
STUFEN = {"grob": (0.3, 0.05), "fein": (0.2, 0.025)}
L_BOX = 38.4
T_MEAS, ANALYSE_DT = 1.0, 5.0
T_RAMP = 50.0
EINST = {"rampe": T_RAMP}         # paardyn setzt 0 (g von Anfang an)
STOER_EPS, STOER_LMAX = 0.01, 6
STOER_PHI = (2.4, 1.1)             # Phase je Komponente
BLUR, SCHWELLE_REL, Q_MIN_REL = 1.0, 0.5, 0.03
KREIS_R = (1.5, 2.5, 3.5, 4.5, 5.5, 6.5)
N_THETA = 256
DAUER_K = 3

Q_REF = {"Q94": 93.861, "Q110": 110.174, "Q139": 138.757, "Q199": 199.350}   # RING-Tabelle m = 1, omega^2 0,65/0,625/0,60/0,575
RING_TAB = {110.174: (0.625, 100.728), 93.861: (0.650, 87.714), 138.757: (0.600, 123.074), 199.350: (0.575, 169.447)}

# dyn0: (Name, Q_gesamt, q_2)
D0_LAEUFE = (("v1_Q110", 110.174, 0.0), ("fc_Q110_q10", 110.174, 0.10), ("fc_Q110_q25", 110.174, 0.25),
             ("fc_Q110_q40", 110.174, 0.40), ("v1_Q94", 93.861, 0.0), ("fc_Q94_q25", 93.861, 0.25),
             ("v1_Q139", 138.757, 0.0), ("fc_Q139_q25", 138.757, 0.25), ("v1_Q82_gleichesJ", 0.75 * 110.174, 0.0))
D0_T = {"grob": 1500.0, "fein": 600.0}
D0_FEIN = ("v1_Q110", "fc_Q110_q25")
# dyng: (Name, Q_gesamt, q_2, g, Saat)
DG_LAEUFE = (("Q199_g0", 199.35, 0.25, 0.0, True), ("Q199_g+0.2", 199.35, 0.25, 0.2, True),
             ("Q199_g-0.2", 199.35, 0.25, -0.2, True), ("Q199_g+0.5", 199.35, 0.25, 0.5, True),
             ("Q199_g-0.5", 199.35, 0.25, -0.5, True), ("Q199_g+0.5_ohne", 199.35, 0.25, 0.5, False),
             ("Q199_g-0.5_ohne", 199.35, 0.25, -0.5, False), ("Q110_g+0.2", 110.174, 0.25, 0.2, True),
             ("Q110_g+0.5", 110.174, 0.25, 0.5, True))
DG_T = {"grob": 1000.0, "fein": 400.0}
DG_FEIN = ("Q199_g+0.5",)
# paar
P_Q, P_GS, P_DS = 700.0, (0.0, 0.2, 0.5), (5.0, 6.5, 8.0, 9.5)   # d >= 5, damit sich die Klammerringe nicht beruehren (Aenderung 08:25, vor der Rechnung)
P_PIN, P_RP, P_XI = 0.0, 0.8, 1.0                 # Fleck wirkungslos (Rauchtest 08:09: Wirbel entkommen); statt dessen Phasenklammer
P_KL_IN, P_KL_AUS = 0.5, 2.0                       # Klammerring um A (psi_1) und B (psi_2); 08:25 von 0,4-1,0 auf 0,5-2,0 (GPU-Rauchtest: Phasenschlupf am Ringrand)
P_TAU, P_IT = 0.3, 6000
PP = {"Q": P_Q, "L": L_BOX, "rmax": RMAX, "konf": None, "stamm": "paar", "halb": 14.0}   # bandstat setzt andere Werte


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    if DEV.type == "cuda":
        torch.cuda.synchronize()
    return time.perf_counter()


def geraet_name():
    return torch.cuda.get_device_name(0) if DEV.type == "cuda" else "CPU (nur Rauchtest)"


def upot(s, b=1.0):
    return s - b * s * s + 0.5 * s ** 3


def fz(x, f="{:.4g}"):
    try:
        if x is None or (isinstance(x, float) and not math.isfinite(x)):
            return "-"
        return f.format(x)
    except Exception:
        return str(x)


# ---------------------------------------------------------------- radialer Loeser (PLAN 1.1)

class Radial:
    def __init__(self, rh=RH, rmax=RMAX, tau=R_TAU):
        M = int(round(rmax / rh))
        j = torch.arange(M, dtype=F64, device=DEV)
        self.M, self.h, self.tau = M, rh, tau
        self.r = (j + 0.5) * rh
        rp, rm = (j + 1.0) * rh, j * rh
        self.W = 2.0 * math.pi * self.r * rh
        self.A = {}
        self.inv = {}
        for m in (0, 1):
            A = torch.zeros((M, M), dtype=F64, device=DEV)
            d = (rp + rm) / (self.r * rh * rh) + m * m / (self.r * self.r)
            A[j.long(), j.long()] = d
            A[j[:-1].long(), j[1:].long()] = -rp[:-1] / (self.r[:-1] * rh * rh)
            A[j[1:].long(), j[:-1].long()] = -rm[1:] / (self.r[1:] * rh * rh)
            self.A[m] = A
            self.inv[m] = torch.linalg.inv(torch.eye(M, dtype=F64, device=DEV) + tau * A)

    def energie(self, u1, u2, Q1, Q2, b):
        W = self.W
        S = u1 * u1 + u2 * u2
        N1, N2 = (W * u1 * u1).sum(1), (W * u2 * u2).sum(1)
        G1 = (W * u1 * (u1 @ self.A[1].T)).sum(1)
        G2 = (W * u2 * (u2 @ self.A[0].T)).sum(1)
        V = (W * upot(S, b.unsqueeze(1))).sum(1)
        k1 = torch.where(Q1 > 0, Q1 * Q1 / (4.0 * N1.clamp(min=1e-300)), torch.zeros_like(Q1))
        k2 = torch.where(Q2 > 0, Q2 * Q2 / (4.0 * N2.clamp(min=1e-300)), torch.zeros_like(Q2))
        w1 = torch.where(Q1 > 0, Q1 / (2.0 * N1.clamp(min=1e-300)), torch.zeros_like(Q1))
        w2 = torch.where(Q2 > 0, Q2 / (2.0 * N2.clamp(min=1e-300)), torch.zeros_like(Q2))
        return {"E": k1 + k2 + G1 + G2 + V, "N1": N1, "N2": N2, "G1": G1, "G2": G2, "V": V, "w1": w1, "w2": w2}

    def loesen(self, konf, n_it=R_IT, tol=R_TOL, rauch=False):
        """konf: Liste {name, Q1, Q2, b}; Komponente 1 windet (m = 1), Komponente 2 nicht (m = 0)."""
        B = len(konf)
        r = self.r.unsqueeze(0)
        Q1 = torch.tensor([k["Q1"] for k in konf], dtype=F64, device=DEV)
        Q2 = torch.tensor([k["Q2"] for k in konf], dtype=F64, device=DEV)
        b = torch.tensor([k.get("b", 1.0) for k in konf], dtype=F64, device=DEV)
        Qt = Q1 + Q2
        q2 = (Q2 / Qt).unsqueeze(1)
        s0 = 1.0
        R = (torch.sqrt(Qt / (2.0 * 0.78 * math.pi * s0)) + 0.8).unsqueeze(1)
        Rc = R * torch.sqrt(q2) * 0.9
        sig = torch.sigmoid
        u1 = math.sqrt(s0) * torch.tanh(r / 1.2) * sig((R - r) / 0.8) * torch.where(q2 > 0, sig((r - Rc) / 0.8), torch.ones_like(r))
        u2 = math.sqrt(s0) * torch.where(q2 < 1, sig((Rc + 0.3 - r) / 0.8), sig((R - r) / 0.8))
        u1 = torch.where((Q1 > 0).unsqueeze(1), u1, torch.zeros_like(u1))
        u2 = torch.where((Q2 > 0).unsqueeze(1), u2, torch.zeros_like(u2))
        tau = self.tau
        verlauf = []
        it_end = n_it
        for it in range(1, n_it + 1):
            S = u1 * u1 + u2 * u2
            up = 1.0 - 2.0 * b.unsqueeze(1) * S + 1.5 * S * S
            N1, N2 = (self.W * u1 * u1).sum(1), (self.W * u2 * u2).sum(1)
            w1s = torch.where(Q1 > 0, (Q1 / (2.0 * N1.clamp(min=1e-300))) ** 2, torch.zeros_like(Q1)).unsqueeze(1)
            w2s = torch.where(Q2 > 0, (Q2 / (2.0 * N2.clamp(min=1e-300))) ** 2, torch.zeros_like(Q2)).unsqueeze(1)
            u1 = (u1 - tau * (up - w1s) * u1) @ self.inv[1].T
            u2 = (u2 - tau * (up - w2s) * u2) @ self.inv[0].T
            if it % 1000 == 0 or it == n_it:
                res = self.residuum(u1, u2, Q1, Q2, b)
                en = self.energie(u1, u2, Q1, Q2, b)
                verlauf.append({"it": it, "res_max": res.max().item(), "E": en["E"].tolist()})
                if not bool(torch.isfinite(res).all()):
                    raise RuntimeError("radialer Fluss nicht endlich")
                if res.max().item() < tol:
                    it_end = it
                    break
        res = self.residuum(u1, u2, Q1, Q2, b)
        en = self.energie(u1, u2, Q1, Q2, b)
        aus = []
        for i, k in enumerate(konf):
            f, h = u1[i], u2[i]
            S = f * f + h * h
            j_f = int(torch.argmax(f).item())
            s_max, j_s = S.max(0)
            halb = (torch.arange(self.M, device=DEV) > j_s) & (S < 0.5 * s_max)
            j_h = int(halb.to(torch.int64).argmax().item())
            h_halb = (h < 0.5 * h[0]) if h[0] > 0 else None
            n1, n2 = en["N1"][i].item(), en["N2"][i].item()
            w1, w2 = en["w1"][i].item(), en["w2"][i].item()
            V = en["V"][i].item()
            vir = w1 * w1 * n1 + w2 * w2 * n2
            aus.append({
                "name": k["name"], "Q1": k["Q1"], "Q2": k["Q2"], "b": k.get("b", 1.0), "E": en["E"][i].item(),
                "omega1": w1, "omega2": w2, "N1": n1, "N2": n2, "G1": en["G1"][i].item(), "G2": en["G2"][i].item(),
                "V": V, "J": k["Q1"], "virialrest": (V - vir) / (V + vir), "residuum": res[i].item(),
                "S_max": s_max.item(), "S_0": S[0].item(), "R_S_max": self.r[j_s].item(), "R_halb": self.r[j_h].item(),
                "R_ring_f": self.r[j_f].item() if k["Q1"] > 0 else None,
                "R_kern_h": (self.r[int(h_halb.to(torch.int64).argmax().item())].item() if h_halb is not None and bool(h_halb.any()) else None),
                "S_rand": S[-40:].max().item(), "iterationen": it_end,
                "f": f.cpu(), "h": h.cpu(),
            })
        return aus, verlauf

    def residuum(self, u1, u2, Q1, Q2, b):
        S = u1 * u1 + u2 * u2
        up = 1.0 - 2.0 * b.unsqueeze(1) * S + 1.5 * S * S
        N1, N2 = (self.W * u1 * u1).sum(1), (self.W * u2 * u2).sum(1)
        out = torch.zeros_like(Q1)
        for u, Q, N, m in ((u1, Q1, N1, 1), (u2, Q2, N2, 0)):
            ws = (Q / (2.0 * N.clamp(min=1e-300))) ** 2
            g = u @ self.A[m].T + (up - ws.unsqueeze(1)) * u
            rr = torch.sqrt((self.W * g * g).sum(1) / (self.W * u * u).sum(1).clamp(min=1e-300))
            out = torch.maximum(out, torch.where(Q > 0, rr, torch.zeros_like(rr)))
        return out


def profil_werte(prof, rr):
    """Lineare Interpolation f(r)/r und h(r) auf beliebige Radien (Zellmitten r_j = (j + 1/2) RH)."""
    f, h = prof["f"].to(DEV), prof["h"].to(DEV)
    M = f.shape[0]
    rj = (torch.arange(M, dtype=F64, device=DEV) + 0.5) * RH
    fr = f / rj
    u = (rr / RH - 0.5).clamp(min=0.0)
    j = u.floor().clamp(max=M - 2).long()
    t = (u - j).clamp(0.0, 1.0)
    innen = rr < 0.5 * RH
    fr_i = torch.where(innen, fr[0].expand_as(rr), fr[j] * (1 - t) + fr[j + 1] * t)
    h_i = torch.where(innen, h[0].expand_as(rr), h[j] * (1 - t) + h[j + 1] * t)
    aussen = rr > (M - 1) * RH
    return torch.where(aussen, torch.zeros_like(fr_i), fr_i), torch.where(aussen, torch.zeros_like(h_i), h_i)


# ---------------------------------------------------------------- 2D-Gitter und Zeitentwicklung

class Gitter:
    def __init__(self, L, dx):
        n = int(round(2.0 * L / dx))
        self.L, self.dx, self.n = L, dx, n
        x = -L + dx * torch.arange(n, dtype=F64, device=DEV)
        self.x = x.view(1, 1, n)
        self.y = x.view(1, n, 1)
        k = 2.0 * math.pi * torch.fft.fftfreq(n, d=dx, dtype=F64, device=DEV)
        self.kx = k.view(1, 1, n)
        self.ky = k.view(1, n, 1)
        self.minus_k2 = -(self.kx ** 2 + self.ky ** 2)
        tiefe = torch.maximum(self.x.abs(), self.y.abs())
        self.sigma = SIGMA0 * ((tiefe - (L - SPONGE)).clamp(min=0.0) / SPONGE) ** 2
        self.dA = dx * dx
        self.blur = torch.exp(0.5 * BLUR * BLUR * self.minus_k2)
        self.X2 = self.x.expand(1, n, n)[0].contiguous()
        self.Y2 = self.y.expand(1, n, n)[0].contiguous()


def stoerfaktor(g, x0, y0, r_s, eps, phi):
    """Wie ring.py: 1 + eps Sum_{l=1..6} Re[e^{i phi l} (z/r_s)^l] exp(-l (r^2/r_s^2 - 1)/2)."""
    X = g.x[0] - x0
    Y = g.y[0] - y0
    z = (X + 1j * Y) / r_s
    u2 = (X * X + Y * Y) / (r_s * r_s)
    fak = torch.ones_like(u2)
    zl = torch.ones_like(z)
    for l in range(1, STOER_LMAX + 1):
        zl = zl * z
        fak = fak + eps * (zl * cmath.exp(1j * phi * l)).real * torch.exp(-0.5 * l * (u2 - 1.0))
    return fak


def fc_feld(g, prof, saat, x0=0.0, y0=0.0):
    """psi_1 = f(r) e^{i theta}, psi_2 = h(r); psi_t = -i omega_a psi_a. Rueckgabe (2, n, n)."""
    X = g.x[0] - x0
    Y = g.y[0] - y0
    rr = torch.sqrt(X * X + Y * Y)
    fr, h = profil_werte(prof, rr)
    p1 = fr * (X + 1j * Y)
    p2 = h.to(C128)
    if saat:
        rs = max(prof["R_S_max"], 0.7 * prof["R_halb"])
        p1 = p1 * stoerfaktor(g, x0, y0, rs, STOER_EPS, STOER_PHI[0])
        p2 = p2 * stoerfaktor(g, x0, y0, rs, STOER_EPS, STOER_PHI[1])
    psi = torch.stack([p1, p2])
    vel = torch.stack([-1j * prof["omega1"] * p1, -1j * prof["omega2"] * p2])
    return psi, vel


def kraft(g, psi, gk):
    lap = torch.fft.ifft2(torch.fft.fft2(psi) * g.minus_k2)
    s = (psi.real ** 2 + psi.imag ** 2).sum(1, keepdim=True)
    F = lap - (1.0 + s * (1.5 * s - 2.0)) * psi
    p1, p2 = psi[:, 0], psi[:, 1]
    gg = gk.view(-1, 1, 1)
    F[:, 0] += gg * p1.conj() * p2 * p2
    F[:, 1] += gg * p2.conj() * p1 * p1
    return F


def grad(g, psi):
    ph = torch.fft.fft2(psi)
    return torch.fft.ifft2(ph * (1j * g.kx)), torch.fft.ifft2(ph * (1j * g.ky))


def dichten(g, psi, vel, gk):
    s_a = psi.real ** 2 + psi.imag ** 2                      # (B, 2, n, n)
    s = s_a.sum(1)
    rho_a = 2.0 * (psi * vel.conj()).imag
    gx, gy = grad(g, psi)
    kopp = ((psi[:, 0].conj() * psi[:, 1]) ** 2).real
    e = ((vel.real ** 2 + vel.imag ** 2 + gx.real ** 2 + gx.imag ** 2 + gy.real ** 2 + gy.imag ** 2).sum(1) + upot(s)
         - gk.view(-1, 1, 1) * kopp)
    px = (-2.0 * (vel.conj() * gx).real).sum(1)
    py = (-2.0 * (vel.conj() * gy).real).sum(1)
    return s_a, s, rho_a, e, px, py, kopp


def komponenten(maske):
    """Wie ring.py: zusammenhaengende Gebiete, 4er-Nachbarschaft, periodisch."""
    B, n, _ = maske.shape
    nn = n * n
    idx = torch.arange(nn, device=maske.device, dtype=torch.int64).view(1, n, n).expand(B, n, n)
    aus = torch.full((B, n, n), nn, device=maske.device, dtype=torch.int64)
    rand = torch.full((B, 1), nn, device=maske.device, dtype=torch.int64)
    lab = torch.where(maske, idx, aus)
    for it in range(4 * n):
        alt = lab
        nb = torch.minimum(torch.minimum(lab.roll(1, 1), lab.roll(-1, 1)),
                           torch.minimum(lab.roll(1, 2), lab.roll(-1, 2)))
        lab = torch.where(maske, torch.minimum(lab, nb), aus)
        flach = torch.cat([lab.reshape(B, nn), rand], dim=1)
        lab = torch.where(maske, flach.gather(1, lab.reshape(B, nn)).view(B, n, n), aus)
        if it % 4 == 3 and torch.equal(lab, alt):
            break
    return lab


def klumpenzahl(g, s, rho, schwelle, q_min):
    sb = torch.fft.ifft2(torch.fft.fft2(s) * g.blur).real
    maske = sb > schwelle.view(-1, 1, 1)
    lab = komponenten(maske)
    zahl = []
    for b in range(s.shape[0]):
        mb = maske[b]
        if not bool(mb.any()):
            zahl.append(0)
            continue
        u, inv = torch.unique(lab[b][mb], return_inverse=True)
        q = torch.zeros(int(u.shape[0]), dtype=F64, device=s.device).index_add_(0, inv, rho[b][mb]) * g.dA
        zahl.append(int((q >= q_min[b]).sum().item()))
    return zahl


def plaketten(ph):
    def wr(d):
        return torch.remainder(d + math.pi, 2.0 * math.pi) - math.pi
    p01 = ph.roll(-1, -1)
    p11 = p01.roll(-1, -2)
    p10 = ph.roll(-1, -2)
    return torch.round((wr(p01 - ph) + wr(p11 - p01) + wr(p10 - p11) + wr(ph - p10)) / (2.0 * math.pi))


def bloecke(ph):
    """Windung auf dem Umlauf durch die acht Nachbarn jedes Gitterpunkts (gegen den Uhrzeigersinn). Anders als die
    Plakette verliert das keinen Wirbel, der genau auf einem Gitterpunkt oder einer Gitterlinie sitzt (Rauchtest 08:09).
    Ein Wirbel zaehlt in bis zu vier Bloecken; Zahlen sind Blockzahlen, keine Wirbelzahlen."""
    def wr(d):
        return torch.remainder(d + math.pi, 2.0 * math.pi) - math.pi
    weg = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    vals = [ph.roll((-di, -dj), dims=(-2, -1)) for di, dj in weg]
    tot = torch.zeros_like(ph)
    for k in range(8):
        tot = tot + wr(vals[(k + 1) % 8] - vals[k])
    return torch.round(tot / (2.0 * math.pi))


def wirbel(g, psi, s, xc, yc, s_min, r_in):
    """psi_1-Wirbel (+1) naechst am Zentrum (Blockmitte); Blockzahlen mit +-Windung beider Komponenten in r < r_in
    (nur wo S > s_min)."""
    X = g.x - xc.view(-1, 1, 1)
    Y = g.y - yc.view(-1, 1, 1)
    r2 = X * X + Y * Y
    dicht = s > s_min.view(-1, 1, 1)
    w1 = bloecke(torch.angle(psi[:, 0])) * dicht
    w2 = bloecke(torch.angle(psi[:, 1])) * dicht
    innen = r2 < (r_in * r_in).view(-1, 1, 1)
    d1 = torch.where(w1 > 0.5, r2, torch.full_like(r2, 1e6)).amin((1, 2)).sqrt()
    B, n = r2.shape[0], r2.shape[-1]
    lage = {}
    for name, w in (("A", w1), ("B", w2)):
        rr = torch.where(w > 0.5, r2, torch.full_like(r2, 1e6)).reshape(B, -1)
        i = rr.argmin(1)
        ok = rr.gather(1, i.unsqueeze(1)).squeeze(1) < 1e5
        xs = g.X2.reshape(-1)[i]
        ys = g.Y2.reshape(-1)[i]
        lage[name] = [(xs[b].item(), ys[b].item()) if bool(ok[b]) else None for b in range(B)]
    return {"d_w1": d1.tolist(), "lage_A": lage["A"], "lage_B": lage["B"],
            "n1p": ((w1 > 0.5) & innen).sum((1, 2)).tolist(), "n1m": ((w1 < -0.5) & innen).sum((1, 2)).tolist(),
            "n2p": ((w2 > 0.5) & innen).sum((1, 2)).tolist(), "n2m": ((w2 < -0.5) & innen).sum((1, 2)).tolist()}


def abtasten(g, feld, xs, ys):
    """Bilinear, periodisch; feld (n, n), xs/ys beliebige Form."""
    fx = (xs + g.L) / g.dx
    fy = (ys + g.L) / g.dx
    j0f, i0f = torch.floor(fx), torch.floor(fy)
    tx, ty = fx - j0f, fy - i0f
    j0, i0 = j0f.long() % g.n, i0f.long() % g.n
    j1, i1 = (j0 + 1) % g.n, (i0 + 1) % g.n
    return ((1 - tx) * (1 - ty) * feld[i0, j0] + tx * (1 - ty) * feld[i0, j1]
            + (1 - tx) * ty * feld[i1, j0] + tx * ty * feld[i1, j1])


def kreis_waende(g, p1, p2, xc, yc, radien, gsign):
    """Wandmasse auf Kreisen um (xc, yc) fuer einen Lauf; p1, p2 (n, n). gsign >= 0: leichte Achse n_x, sonst n_y."""
    th = torch.arange(N_THETA, dtype=F64, device=p1.device) * (2.0 * math.pi / N_THETA)
    aus = []
    for rk in radien:
        xs, ys = xc + rk * torch.cos(th), yc + rk * torch.sin(th)
        a1, a2 = abtasten(g, p1, xs, ys), abtasten(g, p2, xs, ys)
        s1, s2 = a1.real ** 2 + a1.imag ** 2, a2.real ** 2 + a2.imag ** 2
        S = s1 + s2
        w = 2.0 * a1.conj() * a2

        def umlauf(z):
            ph = torch.angle(z)
            d = torch.remainder(ph.roll(-1) - ph + math.pi, 2.0 * math.pi) - math.pi
            return d.sum().item() / (2.0 * math.pi)
        wind = umlauf(w)
        wind1, wind2 = umlauf(a1), umlauf(a2)
        ne = w.real if gsign >= 0 else w.imag
        mx = ne.abs().max().clamp(min=1e-300)
        f90 = (ne.abs() >= 0.9 * mx).to(F64).mean().item()
        # Vorzeichenwechsel mit Hysterese +-0,5 max
        zust = torch.where(ne > 0.5 * mx, 1, torch.where(ne < -0.5 * mx, -1, 0)).tolist()
        z = [v for v in zust if v != 0]
        wechsel = 0
        if z:
            for i in range(len(z)):
                if z[i] != z[i - 1]:
                    wechsel += 1
        ds = rk * 2.0 * math.pi / N_THETA
        dne = (ne.roll(-1) - ne.roll(1)) / (2.0 * ds)
        kreuz = torch.sign(ne) != torch.sign(ne.roll(-1))
        mix = (torch.minimum(s1, s2) / S.clamp(min=1e-300)).mean().item()
        if bool(kreuz.any()):
            k_eff = (0.5 * (dne.abs() + dne.roll(-1).abs()))[kreuz] / mx
            s_k = (0.5 * (S + S.roll(-1)))[kreuz]
            minder = s1 if s1.mean() < s2.mean() else s2
            m_k = (0.5 * (minder + minder.roll(-1)))[kreuz] / minder.mean().clamp(min=1e-300)
            eintrag = {"rk_eff": (rk * k_eff).mean().item(), "k_eff": k_eff.mean().item(), "S_wand": s_k.mean().item(),
                       "minder_rel": m_k.mean().item()}
        else:
            eintrag = {"rk_eff": None, "k_eff": None, "S_wand": None, "minder_rel": None}
        eintrag.update({"r": rk, "windung": wind, "W1": wind1, "W2": wind2, "F90": f90, "wechsel": wechsel, "mischung": mix,
                        "S_mittel": S.mean().item()})
        aus.append(eintrag)
    return aus


def azimut(g, s, zx, zy, r_win, l_max, komplex=False):
    X = g.x - zx.view(-1, 1, 1)
    Y = g.y - zy.view(-1, 1, 1)
    r2 = X * X + Y * Y
    w = s * (r2 < (r_win * r_win).view(-1, 1, 1)).to(F64)
    u = (X - 1j * Y) / torch.sqrt(r2).clamp(min=1e-12)
    ws = w.sum((1, 2)).clamp(min=1e-300)
    ul = torch.ones_like(u)
    aus = []
    for _ in range(l_max):
        ul = ul * u
        a = (w * ul).sum((1, 2)) / ws
        aus.append(a if komplex else a.abs())
    return torch.stack(aus, dim=1)


FSP = ["xc", "yc", "Q1w", "Q2w", "Ew", "Jw", "N1w", "N2w", "Smax_w", "Cw", "ReP", "ImP", "d12",
       "A1", "A2", "A3", "A4", "A5", "A6", "ReA2s1", "ImA2s1", "ReA2s2", "ImA2s2"]
GSP = ["Q1", "Q2", "E", "J", "LQ1", "LQ2", "LE", "LJ", "C", "Smax"]


def messen(g, psi, vel, gk, zx, zy, r_win):
    s_a, s, rho_a, e, px, py, kopp = dichten(g, psi, vel, gk)
    dA = g.dA
    jz = g.x * py - g.y * px
    sig = g.sigma
    glob = torch.stack([rho_a[:, 0].sum((1, 2)) * dA, rho_a[:, 1].sum((1, 2)) * dA, e.sum((1, 2)) * dA,
                        jz.sum((1, 2)) * dA, (sig * rho_a[:, 0]).sum((1, 2)) * dA, (sig * rho_a[:, 1]).sum((1, 2)) * dA,
                        (2.0 * sig * (vel.real ** 2 + vel.imag ** 2).sum(1)).sum((1, 2)) * dA, (sig * jz).sum((1, 2)) * dA,
                        kopp.sum((1, 2)) * dA, s.amax((1, 2))], dim=1)
    X = g.x - zx.view(-1, 1, 1)
    Y = g.y - zy.view(-1, 1, 1)
    fen = ((X * X + Y * Y) < (r_win * r_win).view(-1, 1, 1)).to(F64)
    w = s * s * fen
    ws = w.sum((1, 2))
    da = ws > 1e-200
    xc = torch.where(da, zx + (w * X).sum((1, 2)) / ws.clamp(min=1e-300), zx)
    yc = torch.where(da, zy + (w * Y).sum((1, 2)) / ws.clamp(min=1e-300), zy)
    Xc = g.x - xc.view(-1, 1, 1)
    Yc = g.y - yc.view(-1, 1, 1)
    rc = torch.sqrt(Xc * Xc + Yc * Yc).clamp(min=1e-12)
    eith = (Xc + 1j * Yc) / rc
    P = (psi[:, 0].conj() * psi[:, 1] * eith * fen).sum((1, 2)) * dA
    com = []
    for a in (0, 1):
        sa = s_a[:, a] * fen
        n_ = sa.sum((1, 2)).clamp(min=1e-300)
        com.append(((sa * Xc).sum((1, 2)) / n_, (sa * Yc).sum((1, 2)) / n_))
    d12 = torch.sqrt((com[0][0] - com[1][0]) ** 2 + (com[0][1] - com[1][1]) ** 2)
    d12 = torch.where((s_a[:, 1] * fen).sum((1, 2)) * dA > 1e-6, d12, torch.zeros_like(d12))
    A = azimut(g, s, xc, yc, r_win, 6)
    A2a = azimut(g, s_a[:, 0], xc, yc, r_win, 2, komplex=True)[:, 1]
    A2b = azimut(g, s_a[:, 1], xc, yc, r_win, 2, komplex=True)[:, 1]
    fs = torch.stack([xc, yc, (rho_a[:, 0] * fen).sum((1, 2)) * dA, (rho_a[:, 1] * fen).sum((1, 2)) * dA,
                      (e * fen).sum((1, 2)) * dA, ((Xc * py - Yc * px) * fen).sum((1, 2)) * dA,
                      (s_a[:, 0] * fen).sum((1, 2)) * dA, (s_a[:, 1] * fen).sum((1, 2)) * dA, (s * fen).amax((1, 2)),
                      (kopp * fen).sum((1, 2)) * dA, P.real, P.imag, d12] + list(A.unbind(1))
                     + [A2a.real, A2a.imag, A2b.real, A2b.imag], dim=1)
    return glob, fs, xc, yc, s, rho_a.sum(1)


def schnitt(g, psi, xc, yc, halb=15.0):
    """Ausschnitt um (xc, yc) fuer Bilder: S_1, S_2, Delta, n_z/S (float32, CPU)."""
    n = g.n
    m = int(round(halb / g.dx))
    ic = int(round((yc + g.L) / g.dx))
    jc = int(round((xc + g.L) / g.dx))
    ii = (torch.arange(ic - m, ic + m + 1, device=psi.device) % n)
    jj = (torch.arange(jc - m, jc + m + 1, device=psi.device) % n)
    p = psi[:, ii][:, :, jj]
    s1, s2 = p[0].real ** 2 + p[0].imag ** 2, p[1].real ** 2 + p[1].imag ** 2
    delta = torch.angle(p[0].conj() * p[1])
    nz = (s1 - s2) / (s1 + s2).clamp(min=1e-12)
    return torch.stack([s1, s2, delta, nz]).float().cpu()


def entwickeln(g, psi, vel, dt, t_end, gfin, r_win, s_min, r_in, q_min, radien, gsign, budget, t_snap):
    """Velocity-Verlet mit Randschicht; g(t) = gfin min(1, t/T_RAMP) (bei gfin = 0 wirkungslos)."""
    B = psi.shape[0]
    daempf = torch.exp(-g.sigma * dt).unsqueeze(1)

    def gk_bei(t):
        return gfin * min(1.0, t / EINST["rampe"]) if EINST["rampe"] > 0 else gfin

    t0 = uhr()
    n_schritte = int(round(t_end / dt))
    alle = max(1, int(round(T_MEAS / dt)))
    ana = max(1, int(round(ANALYSE_DT / dt)))
    zx = torch.zeros(B, dtype=F64, device=DEV)
    zy = torch.zeros(B, dtype=F64, device=DEV)
    reihe_t, reihe_g, reihe_f = [], [], []
    analysen = []
    bilder = {}
    schwelle = None

    def mess(t, zx, zy):
        glob, fs, xc, yc, s, rho = messen(g, psi, vel, gk_bei(t), zx, zy, r_win)
        reihe_t.append(t)
        reihe_g.append(glob)
        reihe_f.append(fs)
        return xc, yc, s, rho

    def analyse(t, xc, yc, s, rho):
        nonlocal schwelle
        if schwelle is None:
            sb = torch.fft.ifft2(torch.fft.fft2(s) * g.blur).real
            schwelle = SCHWELLE_REL * sb.amax((1, 2))
        kz = klumpenzahl(g, s, rho, schwelle, q_min)
        wb = wirbel(g, psi, s, xc, yc, s_min, r_in)
        kr = [kreis_waende(g, psi[b, 0], psi[b, 1], xc[b].item(), yc[b].item(), radien, gsign[b]) for b in range(B)]
        analysen.append({"t": t, "klumpen": kz, "wirbel": wb, "kreise": kr})

    xc, yc, s, rho = mess(0.0, zx, zy)
    analyse(0.0, xc, yc, s, rho)
    bilder[0.0] = [schnitt(g, psi[b], xc[b].item(), yc[b].item()) for b in range(B)]
    zx, zy = xc, yc
    F = kraft(g, psi, gk_bei(0.0))
    t_ende = 0.0
    abbruch = False
    for n in range(1, n_schritte + 1):
        t = n * dt
        vel.add_(F, alpha=0.5 * dt)
        psi.add_(vel, alpha=dt)
        F = kraft(g, psi, gk_bei(t))
        vel.add_(F, alpha=0.5 * dt)
        vel.mul_(daempf)
        if n % alle == 0:
            xc, yc, s, rho = mess(t, zx, zy)
            zx, zy = xc, yc
            t_ende = t
            if n % ana == 0:
                analyse(t, xc, yc, s, rho)
            if any(abs(t - ts) < 0.5 * dt * alle for ts in t_snap):
                bilder[t] = [schnitt(g, psi[b], xc[b].item(), yc[b].item()) for b in range(B)]
            if uhr() - t0 > budget:
                abbruch = True
                break
    if t_ende not in bilder:
        bilder[t_ende] = [schnitt(g, psi[b], zx[b].item(), zy[b].item()) for b in range(B)]
    glob = torch.stack(reihe_g)
    fs = torch.stack(reihe_f)
    if not bool(torch.isfinite(glob).all()) or not bool(torch.isfinite(fs).all()):
        raise RuntimeError("nicht endliche Messwerte")
    return {"t": torch.tensor(reihe_t, dtype=F64), "glob": glob.cpu(), "fs": fs.cpu(), "analysen": analysen,
            "bilder": bilder, "abbruch": abbruch, "t_ende": t_ende, "sek": uhr() - t0}


# ---------------------------------------------------------------- Auswertung

def trapez(t, y):
    return torch.cat([torch.zeros(1, dtype=F64), torch.cumsum(0.5 * (y[1:] + y[:-1]) * (t[1:] - t[:-1]), 0)])


def bilanz(t, gl, gfin_b, gkop):
    """Rest(t) = X(t) + geschluckt(t) - X(0); E zusaetzlich mit Rampenarbeit int gdot C dt."""
    aus = {}
    Q0 = abs(gl[0, 0].item()) + abs(gl[0, 1].item())
    for name, i, li in (("Q1", 0, 4), ("Q2", 1, 5), ("J", 3, 7)):
        rest = gl[:, i] + trapez(t, gl[:, li]) - gl[0, i]
        aus[name] = rest.abs().max().item() / max(Q0, 1e-300)
    qs = gl[:, 0] + gl[:, 1] + trapez(t, gl[:, 4] + gl[:, 5]) - gl[0, 0] - gl[0, 1]
    aus["Q"] = qs.abs().max().item() / max(Q0, 1e-300)
    tr = EINST["rampe"]
    gdot = torch.where(t < tr, torch.full_like(t, gfin_b / tr), torch.zeros_like(t)) if tr > 0 else torch.zeros_like(t)
    e_rest = gl[:, 2] + trapez(t, gl[:, 6]) + trapez(t, gdot * gl[:, 8]) - gl[0, 2]
    aus["E"] = e_rest.abs().max().item() / abs(gl[0, 2].item())
    aus["E_nach_Rampe"] = (e_rest[t >= tr] - e_rest[t >= tr][0]).abs().max().item() / abs(gl[0, 2].item()) if bool((t >= tr).any()) else None
    geschluckt = trapez(t, gl[:, 4] + gl[:, 5])
    aus["Q_geschluckt_rel"] = geschluckt[-1].item() / max(Q0, 1e-300)
    # Fenster bis zum ersten Prozent geschluckter Ladung (Nachtrag 08:30): dort misst der Rest die Dynamik, nicht die
    # Quadratur grosser Verlustraten (RING-K: der Rest waechst mit der geschluckten Menge)
    m = geschluckt <= 0.01 * max(Q0, 1e-300)
    aus["t_1proz"] = t[m][-1].item()
    for name, rest in (("Q", qs), ("E", e_rest)):
        norm = max(Q0, 1e-300) if name == "Q" else abs(gl[0, 2].item())
        aus[name + "_bis_1proz"] = rest[m].abs().max().item() / norm
    jr = gl[:, 3] + trapez(t, gl[:, 7]) - gl[0, 3]
    aus["J_bis_1proz"] = jr[m].abs().max().item() / max(Q0, 1e-300)
    return aus


def test_nach(args):
    """Nachauswertung der Bilanz aus *_roh.pt im Ausgabeordner (nur Rechnen auf gespeicherten Reihen)."""
    zeilen = [f"ROT-1 nach: Bilanz bis 1 % geschluckter Ladung. {jetzt()}"]
    erg = {}
    for f in sorted(os.listdir(args.out)):
        if not f.endswith("_roh.pt"):
            continue
        roh = torch.load(os.path.join(args.out, f), map_location="cpu", weights_only=False)
        t, glob = roh["t"], roh["glob"]
        rampe = 0.0 if f.startswith("dyn0") else T_RAMP
        EINST["rampe"] = rampe
        for b, name in enumerate(roh["namen"]):
            gfin = 0.0
            for l in DG_LAEUFE:
                if l[0] == name:
                    gfin = l[3]
            bz = bilanz(t, glob[:, b], gfin, None)
            erg[f"{f}:{name}"] = bz
            zeilen.append(f"{f} {name}: t_1% {bz['t_1proz']:.0f}, Q {bz['Q_bis_1proz']:.1e}, E {bz['E_bis_1proz']:.1e}, "
                          f"J {bz['J_bis_1proz']:.1e} (ganzer Lauf Q {bz['Q']:.1e}, E {bz['E']:.1e}, J {bz['J']:.1e})")
    EINST["rampe"] = T_RAMP
    schreiben(args.out, "nach_bilanz", erg, "\n".join(zeilen) + "\n")
    # Zeitreihe der Waende waehrend Rampe und Wandbildung (Nachtrag 08:33): je Lauf t = 0 ... 150 alle 5
    z2 = [f"ROT-1 nach: Waende zeitaufgeloest (Kreise um den S^2-Schwerpunkt). {jetzt()}",
          "Spalten je Kreis r: F90 / r k_eff / k_eff gegen sqrt(|g| S) (Pol) und sqrt(2|g| S) (Aequator) / Wechsel / W (Delta) W1 W2 / "
          "Minderheit an der Wand relativ / Mischung; Fenster: Q1/Q, omega1 - omega2, d arg P/dt, Cw, J/Q, A2"]
    zr = {}
    for f in sorted(os.listdir(args.out)):
        if not (f.endswith("_roh.pt") and f.startswith("dyng")):
            continue
        roh = torch.load(os.path.join(args.out, f), map_location="cpu", weights_only=False)
        t, fs = roh["t"], roh["fs"]
        ix = {k: i for i, k in enumerate(roh["FSP"])}
        an = roh["analysen"]
        for b, name in enumerate(roh["namen"]):
            gfin = next((l[3] for l in DG_LAEUFE if l[0] == name), 0.0)
            z2.append(f"== {f} {name} (g = {gfin})")
            qw = fs[:, b, ix["Q1w"]] + fs[:, b, ix["Q2w"]]
            w1 = fs[:, b, ix["Q1w"]] / (2.0 * fs[:, b, ix["N1w"]].clamp(min=1e-300))
            w2 = fs[:, b, ix["Q2w"]] / (2.0 * fs[:, b, ix["N2w"]].clamp(min=1e-300))
            ph = torch.atan2(fs[:, b, ix["ImP"]], fs[:, b, ix["ReP"]])
            reihe = []
            for a in an:
                if a["t"] > 150.0 + 1e-9:
                    break
                i = int(torch.argmin((t - a["t"]).abs()))
                j0, j1 = max(i - 2, 0), min(i + 2, len(t) - 1)
                dph = (ph[j1] - ph[j0] + math.pi) % (2 * math.pi) - math.pi
                om_p = (dph / (t[j1] - t[j0])).item() if j1 > j0 else float("nan")
                teile = [f"t {a['t']:5.0f}: Q1/Q {(fs[i, b, ix['Q1w']] / qw[i]).item():.3f}, w1-w2 {(w1[i] - w2[i]).item():+.4f}, "
                         f"dargP/dt {om_p:+.4f}, Cw {fs[i, b, ix['Cw']].item():+.2f}, J/Q {(fs[i, b, ix['Jw']] / qw[i]).item():.3f}, "
                         f"A2 {fs[i, b, ix['A2']].item():.3f}"]
                eintrag = {"t": a["t"], "Q1_Q": (fs[i, b, ix['Q1w']] / qw[i]).item(), "w1_w2": (w1[i] - w2[i]).item(), "Omega_P": om_p}
                for k, rk in enumerate(KREIS_R):
                    if rk not in (2.5, 3.5, 4.5):
                        continue
                    e = a["kreise"][b][k]
                    kp = math.sqrt(abs(gfin) * e["S_wand"]) if e["S_wand"] else None
                    ka = math.sqrt(2 * abs(gfin) * e["S_wand"]) if e["S_wand"] else None
                    teile.append(f"r {rk}: {e['F90']:.2f}/{fz(e['rk_eff'], '{:.2f}')}/{fz(e['k_eff'], '{:.3f}')} "
                                 f"({fz(kp, '{:.3f}')}, {fz(ka, '{:.3f}')})/{e['wechsel']}/{e['windung']:+.1f} {e['W1']:+.1f} {e['W2']:+.1f}/"
                                 f"{fz(e['minder_rel'], '{:.2f}')}/{e['mischung']:.2f}")
                    eintrag[f"r{rk}"] = dict(e, k_pol=kp, k_aeq=ka)
                reihe.append(eintrag)
                z2.append("  " + "; ".join(teile))
            zr[f"{f}:{name}"] = reihe
    schreiben(args.out, "nach_waende", zr, "\n".join(z2) + "\n")


def rate(t, a, t_von=5.0):
    """Wachstumsrate: ln a zwischen erstem Ueberschreiten von max(3 a0, 3e-3) und 0,1 (a0 Median t in [5, 25])."""
    m = (t >= t_von) & (t <= 25.0)
    if not bool(m.any()):
        return None, None, None
    a0 = a[m].median().item()
    lo = max(3.0 * a0, 3e-3)
    i_a = torch.nonzero(a >= lo)
    i_b = torch.nonzero(a >= 0.1)
    if i_a.numel() == 0 or i_b.numel() == 0:
        return None, None, a0
    ia, ib = int(i_a[0]), int(i_b[0])
    if ib <= ia + 3:
        return None, t[ib].item(), a0
    tt, yy = t[ia:ib + 1], torch.log(a[ia:ib + 1].clamp(min=1e-300))
    A = torch.stack([tt, torch.ones_like(tt)], 1)
    k = torch.linalg.lstsq(A, yy.unsqueeze(1)).solution[:, 0]
    return k[0].item(), t[ib].item(), a0


def erste_dauerhaft(ts, flags, k=DAUER_K):
    lauf = 0
    for i, f in enumerate(flags):
        lauf = lauf + 1 if f else 0
        if lauf >= k:
            return ts[i - k + 1]
    return None


def drehrate(t, P, t_von, t_bis):
    m = (t >= t_von) & (t <= t_bis)
    if int(m.sum()) < 5:
        return None
    ph = torch.atan2(P[m, 1], P[m, 0])
    d = torch.remainder(ph[1:] - ph[:-1] + math.pi, 2.0 * math.pi) - math.pi
    ph = torch.cat([ph[:1], ph[:1] + torch.cumsum(d, 0)])
    tt = t[m]
    A = torch.stack([tt, torch.ones_like(tt)], 1)
    return torch.linalg.lstsq(A, ph.unsqueeze(1)).solution[0, 0].item()


def lauf_auswerten(name, b, erg, Q0, gfin, mitte_r):
    t, gl, fs = erg["t"], erg["glob"][:, b], erg["fs"][:, b]
    ix = {k: i for i, k in enumerate(FSP)}
    T = erg["t_ende"]
    an = erg["analysen"]
    ts = [a["t"] for a in an]
    kl = [a["klumpen"][b] for a in an]
    t_teil = erste_dauerhaft(ts, [k >= 2 for k in kl])
    qw = fs[:, ix["Q1w"]] + fs[:, ix["Q2w"]]
    halb = torch.nonzero(qw < 0.5 * qw[0])
    t_halb = t[int(halb[0])].item() if halb.numel() else None
    A = fs[:, ix["A1"]:ix["A6"] + 1]
    raten = {}
    for l in range(6):
        gam, tb, a0 = rate(t, A[:, l])
        raten[l + 1] = {"gamma": gam, "t_0.1": tb, "a0": a0, "max": A[:, l].max().item()}
    kand = [(v["t_0.1"], l) for l, v in raten.items() if v["t_0.1"] is not None]
    l_dom = min(kand)[1] if kand else max(raten, key=lambda l: raten[l]["max"])
    d12 = fs[:, ix["d12"]]
    i_d = torch.nonzero(d12 > 1.0)
    wb = [a["wirbel"] for a in an]
    zentral = [w["d_w1"][b] < 2.0 for w in wb]
    n2 = [w["n2p"][b] + w["n2m"][b] for w in wb]
    w1 = (fs[:, ix["Q1w"]] / (2.0 * fs[:, ix["N1w"]].clamp(min=1e-300)))
    w2 = (fs[:, ix["Q2w"]] / (2.0 * fs[:, ix["N2w"]].clamp(min=1e-300)))
    aus = {"name": name, "g": gfin, "T_erreicht": T, "Q1_0": gl[0, 0].item(), "Q2_0": gl[0, 1].item(),
           "J_0": gl[0, 3].item(), "E_0": gl[0, 2].item(), "t_teilung": t_teil, "t_fensterladung_halb": t_halb,
           "klumpen_ende": kl[-1], "l_dom": l_dom, "raten": raten, "d12_max": d12.max().item(),
           "t_d12_gt1": t[int(i_d[0])].item() if i_d.numel() else None,
           "anteil_wirbel_zentral": sum(zentral) / max(len(zentral), 1),
           "t_wirbel_weg": erste_dauerhaft(ts, [not z for z in zentral]),
           "psi2_wirbel_max": max(n2) if n2 else 0,
           "bilanz": bilanz(t, gl, gfin, None)}
    for tq in (0.0, 50.0, 100.0, 250.0, 500.0, 1000.0, 1500.0, T):
        i = int(torch.argmin((t - tq).abs()))
        if abs(t[i].item() - tq) > 1.0:
            continue
        aus[f"t{int(tq)}"] = {"Q1w": fs[i, ix["Q1w"]].item(), "Q2w": fs[i, ix["Q2w"]].item(),
                              "J_Q": (fs[i, ix["Jw"]] / qw[i]).item(), "E_Q": (fs[i, ix["Ew"]] / qw[i]).item(),
                              "omega1": w1[i].item(), "omega2": w2[i].item(), "Cw": fs[i, ix["Cw"]].item(),
                              "A2": fs[i, ix["A2"]].item(), "d12": d12[i].item()}
    # Musterdrehung und Waende in Zeitfenstern
    P = fs[:, [ix["ReP"], ix["ImP"]]]
    fenster = [(60.0, 160.0), (200.0, 400.0), (max(T - 200.0, 60.0), T)]
    aus["drehung"] = []
    for a_, b_ in fenster:
        if b_ <= a_ + 10:
            continue
        m = (t >= a_) & (t <= b_)
        om = drehrate(t, P, a_, b_)
        aus["drehung"].append({"von": a_, "bis": b_, "Omega_P": om, "omega1_minus_omega2": (w1[m] - w2[m]).mean().item(),
                               "Q1_Q": (fs[m, ix["Q1w"]] / qw[m]).mean().item(), "Cw": fs[m, ix["Cw"]].mean().item()})
    aus["waende"] = []
    for a_, b_ in [(0.0, 0.0)] + fenster:
        sel = [a for a in an if a_ <= a["t"] <= b_]
        if not sel:
            continue
        je_r = []
        for k, rk in enumerate(KREIS_R):
            eint = [a["kreise"][b][k] for a in sel]

            def mittel(key):
                v = [e[key] for e in eint if e[key] is not None]
                return sum(v) / len(v) if v else None
            wech = [e["wechsel"] for e in eint]
            je_r.append({"r": rk, "F90": mittel("F90"), "rk_eff": mittel("rk_eff"), "k_eff": mittel("k_eff"),
                         "S_wand": mittel("S_wand"), "minder_rel": mittel("minder_rel"), "windung": mittel("windung"), "W1": mittel("W1"), "W2": mittel("W2"),
                         "mischung": mittel("mischung"), "wechsel_median": sorted(wech)[len(wech) // 2]})
        aus["waende"].append({"von": a_, "bis": b_, "je_r": je_r})
    return aus


def bilder_schreiben(out, karte, stufe, namen, bilder, titel, halb=15.0):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:          # ohne matplotlib keine Bilder
        print(f"keine Bilder: {exc!r}", flush=True)
        return []
    zeiten = sorted(bilder)
    if len(zeiten) > 5:
        zeiten = [zeiten[0], zeiten[len(zeiten) // 4], zeiten[len(zeiten) // 2], zeiten[3 * len(zeiten) // 4], zeiten[-1]]
    pfade = []
    for b, name in enumerate(namen):
        fig, ax = plt.subplots(len(zeiten), 4, figsize=(12, 3 * len(zeiten)), squeeze=False)
        for i, tz in enumerate(zeiten):
            s1, s2, de, nz = bilder[tz][b]
            smax = float(max(s1.max(), s2.max(), 1e-12))
            maske = ((s1 > 0.02 * smax) & (s2 > 0.02 * smax)).float()
            for j, (feld, cm, lo, hi, tt) in enumerate(((s1, "viridis", 0, smax, "|psi_1|^2"), (s2, "viridis", 0, smax, "|psi_2|^2"),
                                                       (torch.where(maske > 0, de, torch.full_like(de, float("nan"))), "hsv", -math.pi, math.pi, "Delta = arg psi_2 - arg psi_1"),
                                                       (torch.where((s1 + s2) > 0.02 * smax, nz, torch.full_like(nz, float("nan"))), "coolwarm", -1, 1, "n_z/S"))):
                a = ax[i][j]
                a.imshow(feld.numpy(), origin="lower", cmap=cm, vmin=lo, vmax=hi, extent=(-halb, halb, -halb, halb))
                a.set_title(f"{tt}, t = {tz:.0f}", fontsize=8)
                a.tick_params(labelsize=6)
        fig.suptitle(f"{titel}: {name}", fontsize=10)
        fig.tight_layout()
        p = os.path.join(out, f"{karte}_{stufe}_{name}.png")
        fig.savefig(p, dpi=70)
        plt.close(fig)
        pfade.append(p)
    return pfade


def schreiben(out, stamm, ergebnis, text):
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, stamm + "_ergebnis.json"), "w") as fh:
        json.dump(ergebnis, fh, indent=1, default=lambda o: None)
    with open(os.path.join(out, stamm + "_bericht.txt"), "w") as fh:
        fh.write(text)
    print(text, flush=True)


# ---------------------------------------------------------------- Unterbefehle

def radial_konf(namen_q):
    """namen_q: Liste (Name, Q1, Q2); Rueckgabe konf fuer Radial.loesen."""
    return [{"name": n, "Q1": q1, "Q2": q2, "b": 1.0} for n, q1, q2 in namen_q]


def test_radial(args):
    start = jetzt()
    t0 = uhr()
    rad = Radial()
    konf = []
    qs = list(Q_REF.items()) if not args.rauch else [("Q110", Q_REF["Q110"])]
    q2s = (0.1, 0.25, 0.4)
    for qn, Q in qs:
        konf.append((f"v1_{qn}", Q, 0.0))
        konf.append((f"b_{qn}", 0.0, Q))
        for q2 in q2s:
            konf.append((f"fc_{qn}_q{int(round(100 * q2))}", (1 - q2) * Q, q2 * Q))
            konf.append((f"v1_{qn}_Q1_q{int(round(100 * q2))}", (1 - q2) * Q, 0.0))
            konf.append((f"b_{qn}_Q2_q{int(round(100 * q2))}", 0.0, q2 * Q))
    # dE/dQ-Probe (K5) an fc_Q110_q25
    Q = Q_REF["Q110"]
    dq = 0.5
    for s1, s2, tag in ((dq, 0.0, "+Q1"), (-dq, 0.0, "-Q1"), (0.0, dq, "+Q2"), (0.0, -dq, "-Q2")):
        konf.append((f"dq_{tag}", 0.75 * Q + s1, 0.25 * Q + s2))
    konf.append(("v1_Q82_gleichesJ", 0.75 * Q, 0.0))
    ergebnisse, verlauf = rad.loesen(radial_konf(konf), n_it=rauch_it(args.rauch))
    cache_schreiben(ergebnisse, rauch_it(args.rauch))
    per = {e["name"]: e for e in ergebnisse}
    dauer = uhr() - t0
    zeilen = [f"ROT-1 radial (g = 0, gefuellte Wirbel). Start {start}, Ende {jetzt()}, {geraet_name()}, torch {torch.__version__}",
              f"Gitter: h = {RH}, R = {RMAX}, tau = {R_TAU}; Dauer {dauer:.1f} s; letzter Stand {verlauf[-1]['it']} Iterationen, Residuum max {verlauf[-1]['res_max']:.2e}",
              "", "name | Q1 | Q2 | E | E/Q | omega1^2 | omega2^2 | Omega=omega1-omega2 | S_0 | S_max | R_S_max | R_halb | R_ring_f | R_kern_h | Virialrest | Residuum | S_rand"]
    for e in ergebnisse:
        Qt = e["Q1"] + e["Q2"]
        zeilen.append(" | ".join([e["name"], fz(e["Q1"], "{:.3f}"), fz(e["Q2"], "{:.3f}"), fz(e["E"], "{:.4f}"), fz(e["E"] / Qt, "{:.5f}"),
                                  fz(e["omega1"] ** 2, "{:.5f}"), fz(e["omega2"] ** 2, "{:.5f}"),
                                  fz(e["omega1"] - e["omega2"] if e["Q1"] > 0 and e["Q2"] > 0 else None, "{:.5f}"),
                                  fz(e["S_0"], "{:.4f}"), fz(e["S_max"], "{:.4f}"), fz(e["R_S_max"], "{:.3f}"), fz(e["R_halb"], "{:.3f}"),
                                  fz(e["R_ring_f"], "{:.3f}"), fz(e["R_kern_h"], "{:.3f}"), fz(e["virialrest"], "{:.1e}"),
                                  fz(e["residuum"], "{:.1e}"), fz(e["S_rand"], "{:.1e}")]))
    # Vergleiche
    zeilen += ["", "Vergleich bei gleichem Q und J = Q1 (E_sep = E_v1(Q1) + E_b(Q2), E_b = min(E_Ball, Q2) falls zerstreut):",
               "fall | E_fc | E_sep | Bindung E_sep - E_fc | E_v1(Q) [J = Q] | E_b(Q) [J = 0] | Reihenfolge E_b < E_fc < E_v1"]
    vergleich = []
    for qn, Q in qs:
        for q2 in q2s:
            tag = f"q{int(round(100 * q2))}"
            fc = per[f"fc_{qn}_{tag}"]
            v1q1 = per[f"v1_{qn}_Q1_{tag}"]
            bq2 = per[f"b_{qn}_Q2_{tag}"]
            eb2 = bq2["E"] if bq2["S_max"] > 0.1 else q2 * Q
            e_sep = v1q1["E"] + min(eb2, q2 * Q)
            ev1, eb = per[f"v1_{qn}"]["E"], per[f"b_{qn}"]["E"]
            ok = eb < fc["E"] < ev1
            vergleich.append({"fall": f"{qn}_{tag}", "E_fc": fc["E"], "E_sep": e_sep, "bindung": e_sep - fc["E"],
                              "E_v1_Q": ev1, "E_b_Q": eb, "reihenfolge": ok, "b_Q2_zerstreut": bq2["S_max"] <= 0.1})
            zeilen.append(" | ".join([f"{qn}_{tag}", fz(fc["E"], "{:.4f}"), fz(e_sep, "{:.4f}"), fz(e_sep - fc["E"], "{:.4f}"),
                                      fz(ev1, "{:.4f}"), fz(eb, "{:.4f}"), "ja" if ok else "NEIN"]))
    # K1/K5
    zeilen += ["", "K1: einkomponentig gegen die RING-Schiesstabelle (omega^2, E):"]
    k1 = []
    for qn, Q in qs:
        e = per[f"v1_{qn}"]
        w2r, er = RING_TAB.get(Q, (None, None))
        if w2r is None:
            continue
        k1.append({"Q": Q, "omega2": e["omega1"] ** 2, "omega2_ring": w2r, "E": e["E"], "E_ring": er})
        zeilen.append(f"  Q = {Q}: omega^2 {e['omega1'] ** 2:.5f} (RING {w2r}), E {e['E']:.4f} (RING {er}), rel. {abs(e['E'] - er) / er:.1e}")
    d = {k: per[f"dq_{k}"]["E"] for k in ("+Q1", "-Q1", "+Q2", "-Q2")}
    fc = per.get("fc_Q110_q25")
    k5 = None
    if fc is not None:
        k5 = {"dE_dQ1": (d["+Q1"] - d["-Q1"]) / (2 * dq), "omega1": fc["omega1"], "dE_dQ2": (d["+Q2"] - d["-Q2"]) / (2 * dq), "omega2": fc["omega2"]}
        zeilen.append(f"K5: dE/dQ1 = {k5['dE_dQ1']:.6f} gegen omega1 = {k5['omega1']:.6f}; dE/dQ2 = {k5['dE_dQ2']:.6f} gegen omega2 = {k5['omega2']:.6f}")
    zeilen.append(f"v1 gleiches J (Q1 = 82,63): E = {per['v1_Q82_gleichesJ']['E']:.4f}, omega^2 = {per['v1_Q82_gleichesJ']['omega1'] ** 2:.5f}")
    text = "\n".join(zeilen) + "\n"
    info = [{k: v for k, v in e.items() if k not in ("f", "h")} for e in ergebnisse]
    schreiben(args.out, "radial", {"start": start, "ende": jetzt(), "dauer_s": dauer, "loesungen": info, "vergleich": vergleich,
                                   "K1": k1, "K5": k5, "verlauf": verlauf}, text)
    torch.save({e["name"]: e for e in ergebnisse}, os.path.join(args.out, "radial_profile.pt"))
    # Bild der Profile
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, len(qs), figsize=(4 * len(qs), 3.2), squeeze=False)
        r = (torch.arange(int(round(RMAX / RH)), dtype=F64) + 0.5) * RH
        for i, (qn, Q) in enumerate(qs):
            a = ax[0][i]
            for tag, st in (("q10", ":"), ("q25", "-"), ("q40", "--")):
                e = per[f"fc_{qn}_{tag}"]
                a.plot(r, e["f"] ** 2, "b" + st, lw=1, label=f"|psi_1|^2 {tag}")
                a.plot(r, e["h"] ** 2, "r" + st, lw=1, label=f"|psi_2|^2 {tag}")
            a.plot(r, per[f"v1_{qn}"]["f"] ** 2, "k-", lw=0.8, label="einkomponentig m = 1")
            a.set_xlim(0, 14)
            a.set_title(f"{qn} = {Q}", fontsize=9)
            a.set_xlabel("r")
            a.legend(fontsize=6)
        fig.tight_layout()
        fig.savefig(os.path.join(args.out, "radial_profile.png"), dpi=80)
        plt.close(fig)
    except Exception as exc:
        print(f"kein Profilbild: {exc!r}", flush=True)


def cache_pfad():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "profil_cache.pt")


def cache_key(Q1, Q2, b, n_it):
    return f"{Q1:.5f}|{Q2:.5f}|{b:.6f}|{RH}|{RMAX}|{R_TAU}|{n_it}|{R_TOL}"


def cache_schreiben(ergebnisse, n_it):
    p = cache_pfad()
    try:
        alt = torch.load(p, map_location="cpu", weights_only=False) if os.path.exists(p) else {}
    except Exception:
        alt = {}
    for e in ergebnisse:
        alt[cache_key(e["Q1"], e["Q2"], e["b"], n_it)] = e
    tmp = p + f".tmp{os.getpid()}"
    torch.save(alt, tmp)
    os.replace(tmp, p)


def profile_fuer(liste, rauch):
    """liste: (Name, Q_gesamt, q_2) -> radiale Loesungen (je Lauf); erst Plattencache, sonst rechnen."""
    n_it = rauch_it(rauch)
    konf = [{"name": n, "Q1": (1 - q2) * Q, "Q2": q2 * Q, "b": 1.0} for n, Q, q2 in liste]
    p = cache_pfad()
    try:
        platte = torch.load(p, map_location="cpu", weights_only=False) if os.path.exists(p) else {}
    except Exception:
        platte = {}
    keys = [cache_key(k["Q1"], k["Q2"], 1.0, n_it) for k in konf]
    if all(k in platte for k in keys):
        erg = [dict(platte[k], name=c["name"]) for k, c in zip(keys, konf)]
        return erg, [{"it": -1, "res_max": max(e["residuum"] for e in erg), "E": [], "aus_cache": True}]
    rad = Radial()
    erg, verlauf = rad.loesen(konf, n_it=n_it)
    cache_schreiben(erg, n_it)
    return erg, verlauf


def rauch_it(rauch):
    if not rauch:
        return R_IT
    return 300 if DEV.type == "cpu" else 4000


def test_dyn(args, karte):
    start = jetzt()
    stufe = args.stufe
    dx, dt = STUFEN[stufe]
    if args.rauch and args.geraet == "cpu":
        dx, dt = 0.6, 0.1
    if karte == "dyn0":
        laeufe = [(n, Q, q2, 0.0, True) for n, Q, q2 in D0_LAEUFE]
        T = D0_T[stufe]
        fein = D0_FEIN
    else:
        laeufe = list(DG_LAEUFE)
        T = DG_T[stufe]
        fein = DG_FEIN
    if args.laeufe:
        wahl = args.laeufe.split(",")
        laeufe = [l for l in laeufe if l[0] in wahl]
    elif stufe == "fein":
        laeufe = [l for l in laeufe if l[0] in fein]
    if args.rauch:
        T = 20.0 if args.geraet == "cpu" else 0.05 * T
        laeufe = laeufe[:3] if args.geraet == "cpu" else laeufe
    t0 = uhr()
    profile, verlauf = profile_fuer([(l[0], l[1], l[2]) for l in laeufe], args.rauch)
    t_prof = uhr() - t0
    g = Gitter(L_BOX, dx)
    psis, vels = [], []
    for (name, Q, q2, gf, saat), pr in zip(laeufe, profile):
        p, v = fc_feld(g, pr, saat)
        psis.append(p)
        vels.append(v)
    psi = torch.stack(psis).contiguous()
    vel = torch.stack(vels).contiguous()
    B = len(laeufe)
    gfin = torch.tensor([l[3] for l in laeufe], dtype=F64, device=DEV)
    r_halb = torch.tensor([pr["R_halb"] for pr in profile], dtype=F64, device=DEV)
    r_win = r_halb + 10.0
    s_min = torch.full((B,), 0.05, dtype=F64, device=DEV)
    q_min = [Q_MIN_REL * l[1] for l in laeufe]
    gsign = [1 if l[3] >= 0 else -1 for l in laeufe]
    t_snap = (50.0, T / 3.0, 2.0 * T / 3.0)
    erg = entwickeln(g, psi, vel, dt, T, gfin, r_win, s_min, r_halb, q_min, KREIS_R, gsign, args.budget, t_snap)
    # K4: g <-> -g ohne Saat
    k4 = None
    namen = [l[0] for l in laeufe]
    if "Q199_g+0.5_ohne" in namen and "Q199_g-0.5_ohne" in namen:
        ia, ib = namen.index("Q199_g+0.5_ohne"), namen.index("Q199_g-0.5_ohne")
        n = g.n
        idx = torch.remainder(-torch.arange(n, device=DEV), n)

        def drehe(A):            # (R A)(x) = A(R^-1 x), R = +90 Grad (wie ring.py)
            return A[..., idx, :].transpose(-1, -2)

        sa = psi[ia].real ** 2 + psi[ia].imag ** 2
        sb = psi[ib].real ** 2 + psi[ib].imag ** 2
        smax = sa.max().item()
        plus = (sb - drehe(sa)).abs().max().item() / smax
        minus = (sb - drehe(drehe(drehe(sa)))).abs().max().item() / smax
        gl = erg["glob"]
        k4 = {"dichte_plus90": plus, "dichte_minus90": minus,
              "Q1_Reihe": (gl[:, ia, 0] - gl[:, ib, 0]).abs().max().item(), "E_Reihe": (gl[:, ia, 2] - gl[:, ib, 2]).abs().max().item()}
    ausw = [lauf_auswerten(l[0], b, erg, l[1], l[3], None) for b, l in enumerate(laeufe)]
    for a, pr in zip(ausw, profile):
        a["profil"] = {k: v for k, v in pr.items() if k not in ("f", "h")}
    dauer = uhr() - t0
    zeilen = [f"ROT-1 {karte} {stufe}{' RAUCH' if args.rauch else ''}. Start {start}, Ende {jetzt()}, {geraet_name()}, torch {torch.__version__}",
              f"dx {dx}, dt {dt}, L {L_BOX}, n {g.n}, T {T} (erreicht {erg['t_ende']}, Abbruch durch Budget: {erg['abbruch']}), "
              f"Profile {t_prof:.1f} s, Entwicklung {erg['sek']:.1f} s, zusammen {dauer:.1f} s; Hochrechnung x20 {20 * erg['sek']:.0f} s",
              f"radial: letzter Stand {verlauf[-1]['it']} Iterationen, Residuum max {verlauf[-1]['res_max']:.1e}", ""]
    zeilen.append("lauf | g | Q1_0 | Q2_0 | J_0/Q | omega1 | omega2 | t_teilung | t_Q_halb | Klumpen Ende | l_dom | gamma(l_dom) | t(A=0,1) | d12 max | t(d12>1) | Wirbel zentral | t Wirbel weg | psi2-Wirbel max | Bilanz Q/E(nach Rampe)/J | Q geschluckt")
    for a in ausw:
        rl = a["raten"][a["l_dom"]]
        bz = a["bilanz"]
        zeilen.append(" | ".join([a["name"], fz(a["g"]), fz(a["Q1_0"], "{:.2f}"), fz(a["Q2_0"], "{:.2f}"),
                                  fz(a["J_0"] / (a["Q1_0"] + a["Q2_0"]), "{:.4f}"), fz(a["profil"]["omega1"], "{:.5f}"),
                                  fz(a["profil"]["omega2"], "{:.5f}"), fz(a["t_teilung"]), fz(a["t_fensterladung_halb"]),
                                  str(a["klumpen_ende"]), str(a["l_dom"]), fz(rl["gamma"], "{:.4f}"), fz(rl["t_0.1"]),
                                  fz(a["d12_max"], "{:.3f}"), fz(a["t_d12_gt1"]), fz(a["anteil_wirbel_zentral"], "{:.2f}"),
                                  fz(a["t_wirbel_weg"]), str(a["psi2_wirbel_max"]),
                                  f"{bz['Q']:.1e}/{fz(bz['E_nach_Rampe'], '{:.1e}')}/{bz['J']:.1e}", fz(bz["Q_geschluckt_rel"], "{:.3f}")]))
    zeilen += ["", "A_l: je l Rate gamma, t(A_l = 0,1), Maximum"]
    for a in ausw:
        zeilen.append(a["name"] + ": " + "; ".join(f"l{l} {fz(v['gamma'], '{:.4f}')}/{fz(v['t_0.1'])}/{v['max']:.3f}" for l, v in a["raten"].items()))
    zeilen += ["", "Fensterwerte (Q1w, Q2w, J/Q, E/Q, omega1, omega2, Cw, A2, d12) zu festen Zeiten:"]
    for a in ausw:
        for k in sorted([k for k in a if k.startswith("t") and k[1:].isdigit()], key=lambda s: int(s[1:])):
            v = a[k]
            zeilen.append(f"  {a['name']} {k}: {v['Q1w']:.3f} {v['Q2w']:.3f} {v['J_Q']:.4f} {v['E_Q']:.4f} {v['omega1']:.5f} {v['omega2']:.5f} {v['Cw']:.4f} {v['A2']:.4f} {v['d12']:.3f}")
    zeilen += ["", "Musterdrehung: Omega_P = d arg P/dt gegen omega1 - omega2 (Fenstermittel), Q1/Q, Cw:"]
    for a in ausw:
        for d in a["drehung"]:
            zeilen.append(f"  {a['name']} [{d['von']:.0f}, {d['bis']:.0f}]: Omega_P {fz(d['Omega_P'], '{:.5f}')}, omega1-omega2 {d['omega1_minus_omega2']:.5f}, Q1/Q {d['Q1_Q']:.4f}, Cw {d['Cw']:.4f}")
    zeilen += ["", "Waende je Kreis (r: F90, r k_eff, k_eff, S an der Wand, Minderheit rel., Windung Delta, Mischung, Wechsel):"]
    for a in ausw:
        for w in a["waende"]:
            zeilen.append(f"  {a['name']} [{w['von']:.0f}, {w['bis']:.0f}]:")
            for e in w["je_r"]:
                zeilen.append(f"     r {e['r']}: F90 {fz(e['F90'], '{:.3f}')}, rk {fz(e['rk_eff'], '{:.2f}')}, k {fz(e['k_eff'], '{:.3f}')}, "
                              f"S {fz(e['S_wand'], '{:.3f}')}, minder {fz(e['minder_rel'], '{:.3f}')}, W {fz(e['windung'], '{:.2f}')}, "
                              f"W1 {fz(e['W1'], '{:.2f}')}, W2 {fz(e['W2'], '{:.2f}')}, mix {fz(e['mischung'], '{:.3f}')}, wechsel {e['wechsel_median']}")
    if k4 is not None:
        zeilen += ["", f"K4 g <-> -g ohne Saat: Dichte(-g) gegen Dichte(+g) um +90 Grad gedreht: {k4['dichte_plus90']:.2e}, "
                       f"um -90 Grad: {k4['dichte_minus90']:.2e}; Reihen Q1 {k4['Q1_Reihe']:.2e}, E {k4['E_Reihe']:.2e}"]
    text = "\n".join(zeilen) + "\n"
    stamm = f"{karte}_{stufe}" + ("_" + args.laeufe.replace(",", "+") if args.laeufe and len(args.laeufe) < 60 else ("_teil" if args.laeufe else ""))
    schreiben(args.out, stamm, {"start": start, "ende": jetzt(), "stufe": stufe, "dx": dx, "dt": dt, "T": T, "t_ende": erg["t_ende"],
                                "abbruch": erg["abbruch"], "sek": erg["sek"], "laeufe": ausw, "K4": k4}, text)
    torch.save({"t": erg["t"], "glob": erg["glob"], "fs": erg["fs"], "namen": namen, "FSP": FSP, "GSP": GSP,
                "analysen": erg["analysen"]}, os.path.join(args.out, stamm + "_roh.pt"))
    pf = bilder_schreiben(args.out, karte, stufe, namen, erg["bilder"], f"ROT-1 {karte} {stufe}")
    print("Bilder: " + ", ".join(pf), flush=True)


def test_paar(args):
    start = jetzt()
    t0 = uhr()
    dx = 0.3 if not (args.rauch and args.geraet == "cpu") else 0.6
    g = Gitter(PP["L"], dx)
    konf = list(PP["konf"]) if PP["konf"] else [(gg, d, False) for gg in P_GS for d in P_DS] + [(-0.5, 6.5, True)]
    if args.rauch:
        konf = [(0.0, 6.5, False), (0.5, 6.5, False), (-0.5, 6.5, True)]
    # gemischter Ball radial: Komponente 2 allein mit U_eff (b = 1 + |g|/4), psi_1 = psi_2 = F/sqrt(2)
    bs = sorted(set(1.0 + abs(k[0]) / 4.0 for k in konf))
    rad = Radial(rmax=PP["rmax"])
    erg, _ = rad.loesen([{"name": f"ball_b{b:.3f}", "Q1": 0.0, "Q2": PP["Q"], "b": b} for b in bs], n_it=rauch_it(args.rauch))
    ball = {round(b, 6): e for b, e in zip(bs, erg)}
    X, Y = g.x[0], g.y[0]
    rr = torch.sqrt(X * X + Y * Y)
    psi = []
    pin = []
    for gg, d, dreh in konf:
        e = ball[round(1.0 + abs(gg) / 4.0, 6)]
        _, F = profil_werte(e, rr)
        ax_, bx_ = -0.5 * d, 0.5 * d
        vA = ((X - ax_) + 1j * Y) / torch.sqrt((X - ax_) ** 2 + Y ** 2 + P_XI ** 2)
        vB = ((X - bx_) + 1j * Y) / torch.sqrt((X - bx_) ** 2 + Y ** 2 + P_XI ** 2)
        p1 = F / math.sqrt(2.0) * vA
        p2 = F / math.sqrt(2.0) * vB * (1j if dreh else 1.0)
        if gg < 0 and not dreh:
            p2 = p2 * 1j
        psi.append(torch.stack([p1, p2]))
        pin.append(torch.stack([P_PIN * torch.exp(-((X - ax_) ** 2 + Y ** 2) / P_RP ** 2),
                                P_PIN * torch.exp(-((X - bx_) ** 2 + Y ** 2) / P_RP ** 2)]))
    psi = torch.stack(psi)
    pin = torch.stack(pin)
    # Phasenklammer: im Ring P_KL_IN < |x - A| < P_KL_AUS wird die Phase von psi_1 auf arg(x - A) + c_A gesetzt (c_A bester
    # Mittelwert), ebenso psi_2 um B; die Amplitude bleibt frei. Die Windung +1 im Ring haelt den Wirbel im Innern fest.
    ringe, eiph = [], []
    for gg, d, dreh in konf:
        rr_ = []
        ee_ = []
        for cx in (-0.5 * d, 0.5 * d):
            Xc, Yc = X - cx, Y
            rc = torch.sqrt(Xc * Xc + Yc * Yc)
            rr_.append(((rc > P_KL_IN) & (rc < P_KL_AUS)).to(F64))
            ee_.append((Xc + 1j * Yc) / rc.clamp(min=1e-12))
        ringe.append(torch.stack(rr_))
        eiph.append(torch.stack(ee_))
    ringe = torch.stack(ringe)
    eiph = torch.stack(eiph)

    def klammer(psi):
        c = (psi * eiph.conj() * ringe).sum((2, 3))
        c = c / c.abs().clamp(min=1e-300)
        return torch.where(ringe > 0, psi.abs() * eiph * c.view(c.shape[0], 2, 1, 1), psi)
    psi = klammer(psi)
    gk = torch.tensor([k[0] for k in konf], dtype=F64, device=DEV).view(-1, 1, 1)
    Q = PP["Q"]
    tau = PP.get("tau", P_TAU)
    nenner = 1.0 - tau * g.minus_k2
    n_it = 400 if args.rauch else PP.get("it", P_IT)
    verlauf = []

    Qa = 0.5 * Q                                       # Q_1 = Q_2 = Q/2 fest (bei g = 0 einzeln erhalten; Aenderung 08:16)

    def energie(psi):
        s_a = psi.real ** 2 + psi.imag ** 2
        s = s_a.sum(1)
        Na = s_a.sum((2, 3)) * g.dA
        gx, gy = grad(g, psi)
        G = (gx.real ** 2 + gx.imag ** 2 + gy.real ** 2 + gy.imag ** 2).sum((1, 2, 3)) * g.dA
        V = upot(s).sum((1, 2)) * g.dA
        C = ((psi[:, 0].conj() * psi[:, 1]) ** 2).real.sum((1, 2)) * g.dA
        Ep = (pin * s_a).sum((1, 2, 3)) * g.dA
        E = (Qa * Qa / (4.0 * Na)).sum(1) + G + V - gk.view(-1) * C
        return E, Ep, Na, C, s_a

    for it in range(1, n_it + 1):
        s_a = psi.real ** 2 + psi.imag ** 2
        s = s_a.sum(1, keepdim=True)
        Na = s_a.sum((2, 3)) * g.dA
        w2 = (Qa / (2.0 * Na)) ** 2
        nl = (1.0 + s * (1.5 * s - 2.0) - w2.view(-1, 2, 1, 1) + pin) * psi
        p1, p2 = psi[:, 0], psi[:, 1]
        kop = torch.stack([p1.conj() * p2 * p2, p2.conj() * p1 * p1], 1)
        nl = nl - gk.view(-1, 1, 1, 1) * kop
        psi = klammer(torch.fft.ifft2(torch.fft.fft2(psi - tau * nl) / nenner))
        if it % 200 == 0 or it == n_it:
            E, Ep, Na, C, _ = energie(psi)
            verlauf.append({"it": it, "E": E.tolist(), "E_pin": Ep.tolist()})
            if not bool(torch.isfinite(E).all()):
                raise RuntimeError("paar: nicht endlich")
    E, Ep, Na, C, s_a = energie(psi)
    N = Na.sum(1)
    # Residuum: voller Gradient, enthaelt die Klammerzonen
    s = s_a.sum(1, keepdim=True)
    w2 = (Qa / (2.0 * Na)) ** 2
    lap = torch.fft.ifft2(torch.fft.fft2(psi) * g.minus_k2)
    p1, p2 = psi[:, 0], psi[:, 1]
    kop = torch.stack([p1.conj() * p2 * p2, p2.conj() * p1 * p1], 1)
    rest = -lap + (1.0 + s * (1.5 * s - 2.0) - w2.view(-1, 2, 1, 1) + pin) * psi - gk.view(-1, 1, 1, 1) * kop
    resid = torch.sqrt((rest.abs() ** 2).sum((1, 2, 3)) / (psi.abs() ** 2).sum((1, 2, 3)))
    aus = []
    th_bilder = []
    for i, (gg, d, dreh) in enumerate(konf):
        sgn = 1 if gg >= 0 else -1
        r_um = 0.5 * d + 2.5
        kr = kreis_waende(g, psi[i, 0], psi[i, 1], 0.0, 0.0, (r_um,), sgn)[0]
        kA = kreis_waende(g, psi[i, 0], psi[i, 1], -0.5 * d, 0.0, (2.4,), sgn)[0]
        kB = kreis_waende(g, psi[i, 0], psi[i, 1], 0.5 * d, 0.0, (2.4,), sgn)[0]
        # Wirbellagen
        wb = wirbel(g, psi[i:i + 1], s_a[i:i + 1].sum(1), torch.tensor([-0.5 * d], dtype=F64, device=DEV),
                    torch.tensor([0.0], dtype=F64, device=DEV), torch.tensor([0.05], dtype=F64, device=DEV),
                    torch.tensor([3.0], dtype=F64, device=DEV))
        # n_e entlang der Mittelsenkrechten x = 0
        ys = torch.linspace(-10.0, 10.0, 401, dtype=F64, device=DEV)
        a1, a2 = abtasten(g, psi[i, 0], torch.zeros_like(ys), ys), abtasten(g, psi[i, 1], torch.zeros_like(ys), ys)
        w = 2 * a1.conj() * a2
        ne = (w.real if sgn > 0 else w.imag) / (a1.abs() ** 2 + a2.abs() ** 2).clamp(min=1e-300)
        wechsel_y = [0.5 * (ys[j] + ys[j + 1]).item() for j in range(400) if (ne[j] > 0) != (ne[j + 1] > 0)]
        drift_i = abs(verlauf[-1]["E"][i] - verlauf[-6]["E"][i]) if len(verlauf) >= 6 else None
        aus.append({"g": gg, "d": d, "psi2_mal_i": dreh, "E": E[i].item(), "dE_letzte1000": drift_i, "E_pin": Ep[i].item(), "N": N[i].item(),
                    "omega": (Qa / (2.0 * Na[i, 0])).item(), "omega2": (Qa / (2.0 * Na[i, 1])).item(), "C": C[i].item(), "residuum": resid[i].item(),
                    "Q1_anteil": (s_a[i, 0].sum() / s_a[i].sum()).item(),
                    "S1_ring_A": ((s_a[i, 0] * ringe[i, 0]).sum() / ringe[i, 0].sum()).item(), "S2_ring_B": ((s_a[i, 1] * ringe[i, 1]).sum() / ringe[i, 1].sum()).item(),
                    "kreis_um_beide": kr, "kreis_A": kA, "kreis_B": kB, "wirbel_A_abstand": wb["d_w1"][0],
                    "ne_Mittelsenkrechte_Wechsel_y": wechsel_y, "ne_bei_y0": ne[200].item()})
        th_bilder.append(schnitt(g, psi[i], 0.0, 0.0, halb=PP["halb"]))
    # Auswertung E(d)
    zeilen = [f"ROT-1 paar{' RAUCH' if args.rauch else ''}. Start {start}, Ende {jetzt()}, {geraet_name()}, torch {torch.__version__}",
              f"Q = {Q}, dx {dx}, L {PP['L']}, Pinning Hoehe {P_PIN}, Radius {P_RP}; tau {tau}, Iterationen {n_it}; Dauer {uhr() - t0:.1f} s",
              "Ball radial: " + "; ".join(f"b {b:.4f}: omega^2 {e['omega2'] ** 2:.5f}, S_0 {e['S_0']:.4f}, R_halb {e['R_halb']:.3f}" for b, e in zip(bs, erg)),
              f"Phasenklammer Ring {P_KL_IN} bis {P_KL_AUS}; Konvergenz: max |E(letzte) - E(1000 Iterationen davor)| = "
              + (f"{max(abs(x - y) for x, y in zip(verlauf[-1]['E'], verlauf[-6]['E'])):.2e}" if len(verlauf) >= 6 else "-")
              + " (Residuum unten enthaelt die Klammerzonen)",
              "", "g | d | psi2*i | E | E_pin | omega | C | Q1-Anteil | Residuum | Kreis um beide: Wechsel/F90/Windung | um A: Windung | um B: Windung | Wirbel A Abstand | n_e-Wechsel auf x = 0 (y) | n_e(0,0)"]
    for a in aus:
        kr = a["kreis_um_beide"]
        zeilen.append(" | ".join([fz(a["g"]), fz(a["d"]), "ja" if a["psi2_mal_i"] else "-", f"{a['E']:.5f}", f"{a['E_pin']:.4f}",
                                  f"{a['omega']:.5f}/{a['omega2']:.5f}", f"{a['C']:.3f}", f"{a['Q1_anteil']:.4f} (S1 Ring A {a['S1_ring_A']:.3f})", f"{a['residuum']:.1e} / dE1000 {fz(a['dE_letzte1000'], '{:.1e}')}",
                                  f"{kr['wechsel']}/{kr['F90']:.3f}/{kr['windung']:.2f}", f"{a['kreis_A']['windung']:.2f} (W1 {a['kreis_A']['W1']:.2f}, W2 {a['kreis_A']['W2']:.2f})",
                                  f"{a['kreis_B']['windung']:.2f}", fz(a["wirbel_A_abstand"], "{:.2f}"),
                                  ",".join(f"{v:.2f}" for v in a["ne_Mittelsenkrechte_Wechsel_y"]), f"{a['ne_bei_y0']:.3f}"]))
    auswertung = {}
    e0 = {a["d"]: a["E"] + 0.0 for a in aus if a["g"] == 0.0 and not a["psi2_mal_i"]}

    def steigung(ds, ws):
        dd = torch.tensor(ds, dtype=F64)
        ww = torch.tensor(ws, dtype=F64)
        A = torch.stack([dd, torch.ones_like(dd)], 1)
        k = torch.linalg.lstsq(A, ww.unsqueeze(1)).solution[:, 0]
        rest = (ww - A @ k).abs().max().item()
        return k[0].item(), rest

    for gg in sorted(set(a["g"] for a in aus if a["g"] > 0)):
        eg = {a["d"]: a["E"] for a in aus if a["g"] == gg and not a["psi2_mal_i"]}
        ds = sorted(eg)
        if len(ds) < 2:
            continue
        # direkt: E_g(d) - E_g(d_min); die Lageabhaengigkeit im Ball ist klein (Abschaetzung im Bericht)
        Wd = [eg[d] - eg[ds[0]] for d in ds]
        k_d, r_d = steigung(ds, Wd)
        S0 = ball[round(1.0 + gg / 4.0, 6)]["S_0"]
        eintrag = {"d": ds, "W_direkt": Wd, "steigung_direkt": k_d, "fitrest_direkt": r_d,
                   "2sigma_pol": 2 * math.sqrt(gg) * S0 ** 1.5, "2sigma_aequator": 2 * math.sqrt(2 * gg) * S0 ** 1.5, "S0": S0}
        zeilen.append(f"g = {gg}: E_g(d) - E_g(d_min) = " + ", ".join(f"d {d}: {w:.4f}" for d, w in zip(ds, Wd))
                      + f"; Steigung {k_d:.4f} (Fitrest {r_d:.3f}) gegen 2 sigma_Pol {2 * math.sqrt(gg) * S0 ** 1.5:.4f}, "
                      f"2 sigma_Aequator {2 * math.sqrt(2 * gg) * S0 ** 1.5:.4f} (S_0 {S0:.4f})")
        dz = [d for d in ds if d in e0]
        if len(dz) >= 2:
            W = [(eg[d] - e0[d]) - (eg[dz[0]] - e0[dz[0]]) for d in dz]
            k0, r0 = steigung(dz, W)
            eintrag.update({"W_minus_E0": W, "steigung_minus_E0": k0, "fitrest_minus_E0": r0})
            zeilen.append(f"   mit Abzug E_0(d): " + ", ".join(f"d {d}: {w:.4f}" for d, w in zip(dz, W)) + f"; Steigung {k0:.4f} (Fitrest {r0:.3f})")
        auswertung[gg] = eintrag
    if e0:
        zeilen.append("E_0(d) bei g = 0 (Textur ohne Waende, psi_1 kann den Bereich um A raeumen): " + ", ".join(f"d {d}: {e0[d]:.4f}" for d in sorted(e0)))
    k4 = [a for a in aus if a["psi2_mal_i"]]
    for a in k4:
        ref = [b for b in aus if b["g"] == -a["g"] and b["d"] == a["d"] and not b["psi2_mal_i"]]
        if ref:
            zeilen.append(f"K4 paar: E(g = {a['g']}, psi_2 -> i psi_2, d = {a['d']}) = {a['E']:.8f} gegen E(g = {ref[0]['g']}) = {ref[0]['E']:.8f}, Differenz {a['E'] - ref[0]['E']:.2e}")
    text = "\n".join(zeilen) + "\n"
    schreiben(args.out, PP["stamm"], {"start": start, "ende": jetzt(), "konf": aus, "auswertung": auswertung, "verlauf": verlauf}, text)
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        n = len(konf)
        fig, ax = plt.subplots(n, 3, figsize=(9, 3 * n), squeeze=False)
        for i, (gg, d, dreh) in enumerate(konf):
            s1, s2, de, nz = th_bilder[i]
            smax = float(max(s1.max(), s2.max()))
            m = (s1 + s2) > 0.05 * smax
            for j, (feld, cm, lo, hi, tt) in enumerate(((torch.where(m, de, torch.full_like(de, float("nan"))), "hsv", -math.pi, math.pi, "Delta"),
                                                       (s1, "viridis", 0, smax, "|psi_1|^2"), (s2, "viridis", 0, smax, "|psi_2|^2"))):
                a = ax[i][j]
                a.imshow(feld.numpy(), origin="lower", cmap=cm, vmin=lo, vmax=hi, extent=(-PP["halb"], PP["halb"], -PP["halb"], PP["halb"]))
                a.set_title(f"g {gg}, d {d}{' (i psi_2)' if dreh else ''}: {tt}", fontsize=8)
                a.tick_params(labelsize=6)
        fig.tight_layout()
        fig.savefig(os.path.join(args.out, PP["stamm"] + "_felder.png"), dpi=60)
        plt.close(fig)
    except Exception as exc:
        print(f"kein Paarbild: {exc!r}", flush=True)


PD_GS, PD_DS, PD_T = (0.0, 0.2, 0.5), (3.0, 5.0, 7.0, 9.0), 250.0


def test_paardyn(args):
    """Nachtrag 08:25 (vor der Rechnung): psi_1-Wirbel bei (-d/2, 0), psi_2-Wirbel bei (+d/2, 0) im grossen gemischten Ball,
    ohne Zwang zeitlich entwickelt (g von Anfang an, keine Rampe). Eine Kraft F zwischen den Wirbeln wird (Magnus) zu
    einer Drehung des Paars: Omega = F/(pi rho_a d), rho_a = 2 omega S_a. Konstante Kraft (Einschluss): Omega d konstant;
    Kraft ~ 1/d: Omega d^2 konstant."""
    start = jetzt()
    t0 = uhr()
    EINST["rampe"] = 0.0
    dx, dt = STUFEN[args.stufe]
    T = PD_T
    konf = [(gg, d) for gg in PD_GS for d in PD_DS]
    if args.rauch:
        konf = [(0.0, 5.0), (0.5, 5.0)]
        if args.geraet == "cpu":
            dx, dt, T = 0.6, 0.1, 20.0
        else:
            T = 0.05 * T
    g = Gitter(L_BOX, dx)
    bs = sorted(set(1.0 + abs(k[0]) / 4.0 for k in konf))
    rad = Radial()
    erg_b, _ = rad.loesen([{"name": f"ball_b{b:.3f}", "Q1": 0.0, "Q2": P_Q, "b": b} for b in bs], n_it=rauch_it(args.rauch))
    ball = {round(b, 6): e for b, e in zip(bs, erg_b)}
    X, Y = g.x[0], g.y[0]
    rr = torch.sqrt(X * X + Y * Y)
    psis, vels, rh = [], [], []
    for gg, d in konf:
        e = ball[round(1.0 + abs(gg) / 4.0, 6)]
        _, F = profil_werte(e, rr)
        vA = ((X + 0.5 * d) + 1j * Y) / torch.sqrt((X + 0.5 * d) ** 2 + Y ** 2 + P_XI ** 2)
        vB = ((X - 0.5 * d) + 1j * Y) / torch.sqrt((X - 0.5 * d) ** 2 + Y ** 2 + P_XI ** 2)
        p = torch.stack([F / math.sqrt(2.0) * vA, F / math.sqrt(2.0) * vB])
        psis.append(p)
        vels.append(-1j * e["omega2"] * p)
        rh.append(e["R_halb"])
    psi = torch.stack(psis).contiguous()
    vel = torch.stack(vels).contiguous()
    B = len(konf)
    gfin = torch.tensor([k[0] for k in konf], dtype=F64, device=DEV)
    r_halb = torch.tensor(rh, dtype=F64, device=DEV)
    erg = entwickeln(g, psi, vel, dt, T, gfin, r_halb + 8.0, torch.full((B,), 0.05, dtype=F64, device=DEV), r_halb,
                     [Q_MIN_REL * P_Q] * B, KREIS_R, [1] * B, args.budget, (50.0, T / 2.0))
    an = erg["analysen"]
    aus = []
    zeilen = [f"ROT-1 paardyn {args.stufe}{' RAUCH' if args.rauch else ''}. Start {start}, Ende {jetzt()}, {geraet_name()}, torch {torch.__version__}",
              f"Q = {P_Q}, dx {dx}, dt {dt}, L {L_BOX}, T {T} (erreicht {erg['t_ende']}, Abbruch {erg['abbruch']}), Entwicklung {erg['sek']:.1f} s, "
              f"Hochrechnung x20 {20 * erg['sek']:.0f} s",
              "Ball radial: " + "; ".join(f"b {b:.4f}: omega {e['omega2']:.5f}, S_0 {e['S_0']:.4f}, R_halb {e['R_halb']:.3f}" for b, e in zip(bs, erg_b)),
              "", "g | d0 | Omega (Fit t >= 30) | d Mittel | d Drift/100 | Omega d | Omega d^2 | F = pi rho_a Omega d | 2 sigma_Pol | Wechsel auf Kreisen um beide (spaet) | Wirbel fehlen (Anteil) | Bilanz Q/E"]
    for b, (gg, d0) in enumerate(konf):
        ts, dd, ph = [], [], []
        fehlt = 0
        for a in an:
            A_, B_ = a["wirbel"]["lage_A"][b], a["wirbel"]["lage_B"][b]
            if A_ is None or B_ is None:
                fehlt += 1
                continue
            ts.append(a["t"])
            dd.append(math.hypot(B_[0] - A_[0], B_[1] - A_[1]))
            ph.append(math.atan2(B_[1] - A_[1], B_[0] - A_[0]))
        om = dmit = drift = None
        if len(ts) >= 5:
            phu = [ph[0]]
            for v in ph[1:]:
                dv = (v - phu[-1] + math.pi) % (2 * math.pi) - math.pi
                phu.append(phu[-1] + dv)
            tt = torch.tensor(ts, dtype=F64)
            m = tt >= min(30.0, 0.5 * T)
            if int(m.sum()) >= 3:
                A = torch.stack([tt[m], torch.ones_like(tt[m])], 1)
                om = torch.linalg.lstsq(A, torch.tensor(phu, dtype=F64)[m].unsqueeze(1)).solution[0, 0].item()
                dm = torch.tensor(dd, dtype=F64)[m]
                dmit = dm.mean().item()
                drift = torch.linalg.lstsq(A, dm.unsqueeze(1)).solution[0, 0].item() * 100.0
        e = ball[round(1.0 + abs(gg) / 4.0, 6)]
        rho_a = e["omega2"] * e["S_0"]           # 2 omega S_a mit S_a = S_0/2
        F_mag = math.pi * rho_a * abs(om) * dmit if om is not None and dmit is not None else None
        sig2 = 2 * math.sqrt(abs(gg)) * e["S_0"] ** 1.5
        spaet = [a for a in an if a["t"] >= 0.6 * erg["t_ende"]]
        wech = []
        for a in spaet:
            for k, rk in enumerate(KREIS_R):
                if rk > 0.5 * (dmit or d0) + 1.5:
                    wech.append(a["kreise"][b][k]["wechsel"])
        wm = sorted(wech)[len(wech) // 2] if wech else None
        bz = bilanz(erg["t"], erg["glob"][:, b], 0.0, None)
        eintrag = {"g": gg, "d0": d0, "Omega": om, "d_mittel": dmit, "d_drift_pro_100": drift, "F_magnus": F_mag,
                   "2sigma_pol": sig2, "wechsel_um_beide_spaet": wm, "fehlt_anteil": fehlt / max(len(an), 1),
                   "reihe": {"t": ts, "d": dd, "phi": ph}, "bilanz": bz}
        aus.append(eintrag)
        zeilen.append(" | ".join([fz(gg), fz(d0), fz(om, "{:.5f}"), fz(dmit, "{:.3f}"), fz(drift, "{:.3f}"),
                                  fz(om * dmit if om is not None and dmit else None, "{:.4f}"),
                                  fz(om * dmit * dmit if om is not None and dmit else None, "{:.4f}"), fz(F_mag, "{:.4f}"),
                                  fz(sig2, "{:.4f}"), str(wm), f"{fehlt / max(len(an), 1):.2f}", f"{bz['Q']:.1e}/{bz['E']:.1e}"]))
    zeilen += ["", "d(t) und Winkel (je 25):"]
    for e_ in aus:
        r = e_["reihe"]
        zeilen.append(f"  g {e_['g']} d0 {e_['d0']}: " + "; ".join(f"t {t:.0f}: d {d:.2f}, phi {p:.2f}" for i, (t, d, p) in enumerate(zip(r["t"], r["d"], r["phi"])) if i % 5 == 0))
    text = "\n".join(zeilen) + "\n"
    schreiben(args.out, f"paardyn_{args.stufe}", {"start": start, "ende": jetzt(), "T": T, "t_ende": erg["t_ende"], "laeufe": aus}, text)
    namen = [f"g{gg}_d{d:.0f}" for gg, d in konf]
    bilder_schreiben(args.out, "paardyn", args.stufe, namen, erg["bilder"], "ROT-1 paardyn")
    EINST["rampe"] = T_RAMP


RG_KONF = ([(0.5, d) for d in (3.0, 4.0, 5.0, 6.0, 7.0, 9.0, 11.0)] + [(0.0, d) for d in (3.0, 4.0, 5.0, 6.0, 7.0, 9.0, 11.0)]
           + [(0.2, d) for d in (3.0, 5.0, 7.0, 9.0)])
RG_T, RG_TA, RG_TOM = 250.0, 60.0, 30.0


def test_regge(args):
    """REGGE-1 (Vorab REGGE-1.md, 10:17:59): paardyn wiederholt, mit Rohreihen; je Lauf j = J_w - Q_w, eps = E_w - omega_b Q_w
    (Mittel t >= 60), Omega und mittleres d (t >= 30 wie paardyn und t >= 60); je g Fits j gegen d^2, eps gegen d,
    Hamilton-Probe Omega_H = Delta eps/Delta j zwischen Nachbarabstaenden."""
    start = jetzt()
    EINST["rampe"] = 0.0
    dx, dt = STUFEN[args.stufe]
    T = RG_T
    konf = list(RG_KONF)
    if args.rauch:
        konf = [(0.5, 5.0), (0.5, 7.0), (0.0, 5.0)]
        if args.geraet == "cpu":
            dx, dt, T = 0.6, 0.1, 20.0
        else:
            T = 0.1 * T
    g = Gitter(L_BOX, dx)
    bs = sorted(set(1.0 + abs(k[0]) / 4.0 for k in konf))
    rad = Radial()
    erg_b, _ = rad.loesen([{"name": f"ball_b{b:.3f}", "Q1": 0.0, "Q2": P_Q, "b": b} for b in bs], n_it=rauch_it(args.rauch))
    ball = {round(b, 6): e for b, e in zip(bs, erg_b)}
    X, Y = g.x[0], g.y[0]
    rr = torch.sqrt(X * X + Y * Y)
    psis, vels, rh = [], [], []
    for gg, d in konf:
        e = ball[round(1.0 + abs(gg) / 4.0, 6)]
        _, F = profil_werte(e, rr)
        vA = ((X + 0.5 * d) + 1j * Y) / torch.sqrt((X + 0.5 * d) ** 2 + Y ** 2 + P_XI ** 2)
        vB = ((X - 0.5 * d) + 1j * Y) / torch.sqrt((X - 0.5 * d) ** 2 + Y ** 2 + P_XI ** 2)
        p = torch.stack([F / math.sqrt(2.0) * vA, F / math.sqrt(2.0) * vB])
        psis.append(p)
        vels.append(-1j * e["omega2"] * p)
        rh.append(e["R_halb"])
    psi = torch.stack(psis).contiguous()
    vel = torch.stack(vels).contiguous()
    B = len(konf)
    gfin = torch.tensor([k[0] for k in konf], dtype=F64, device=DEV)
    r_halb = torch.tensor(rh, dtype=F64, device=DEV)
    erg = entwickeln(g, psi, vel, dt, T, gfin, r_halb + 8.0, torch.full((B,), 0.05, dtype=F64, device=DEV), r_halb,
                     [Q_MIN_REL * P_Q] * B, KREIS_R, [1] * B, args.budget, (T / 2.0,))
    t, gl, fs = erg["t"], erg["glob"], erg["fs"]
    ix = {k: i for i, k in enumerate(FSP)}
    an = erg["analysen"]
    ta = min(RG_TA, 0.5 * erg["t_ende"])
    m = t >= ta
    aus = []
    for b, (gg, d0) in enumerate(konf):
        e = ball[round(1.0 + abs(gg) / 4.0, 6)]
        wb = e["omega2"]
        rho_a = e["omega2"] * e["S_0"]
        qw = (fs[:, b, ix["Q1w"]] + fs[:, b, ix["Q2w"]])
        jw, ew = fs[:, b, ix["Jw"]], fs[:, b, ix["Ew"]]
        jr, er = (jw - qw)[m], (ew - wb * qw)[m]
        eintrag = {"g": gg, "d0": d0, "omega_b": wb, "rho_a": rho_a,
                   "Q_w": qw[m].mean().item(), "J_w": jw[m].mean().item(), "E_w": ew[m].mean().item(),
                   "j": jr.mean().item(), "j_std": jr.std().item(), "eps": er.mean().item(), "eps_std": er.std().item(),
                   "Q_box_0": (gl[0, b, 0] + gl[0, b, 1]).item(), "J_box_0": gl[0, b, 3].item(), "E_box_0": gl[0, b, 2].item(),
                   "Q_box_T": (gl[-1, b, 0] + gl[-1, b, 1]).item(), "J_box_T": gl[-1, b, 3].item(), "E_box_T": gl[-1, b, 2].item(),
                   "Q_geschluckt": trapez(t, gl[:, b, 4] + gl[:, b, 5])[-1].item(), "E_geschluckt": trapez(t, gl[:, b, 6])[-1].item(),
                   "J_geschluckt": trapez(t, gl[:, b, 7])[-1].item()}
        for tag, t0_ in (("30", RG_TOM), ("60", ta)):
            ts, dd, ph = [], [], []
            fehlt = 0
            for a in an:
                if a["t"] < min(t0_, 0.5 * erg["t_ende"]):
                    continue
                A_, B_ = a["wirbel"]["lage_A"][b], a["wirbel"]["lage_B"][b]
                if A_ is None or B_ is None:
                    fehlt += 1
                    continue
                ts.append(a["t"])
                dd.append(math.hypot(B_[0] - A_[0], B_[1] - A_[1]))
                ph.append(math.atan2(B_[1] - A_[1], B_[0] - A_[0]))
            om = dm = None
            if len(ts) >= 3:
                phu = [ph[0]]
                for v in ph[1:]:
                    phu.append(phu[-1] + (v - phu[-1] + math.pi) % (2 * math.pi) - math.pi)
                tt = torch.tensor(ts, dtype=F64)
                A = torch.stack([tt, torch.ones_like(tt)], 1)
                om = torch.linalg.lstsq(A, torch.tensor(phu, dtype=F64).unsqueeze(1)).solution[0, 0].item()
                dm = sum(dd) / len(dd)
            eintrag[f"Omega_{tag}"] = om
            eintrag[f"d_{tag}"] = dm
            eintrag[f"fehlt_{tag}"] = fehlt / max(fehlt + len(ts), 1)
            eintrag[f"reihe_{tag}"] = {"t": ts, "d": dd, "phi": ph}
        aus.append(eintrag)

    def fit(xs, ys):
        xx = torch.tensor(xs, dtype=F64)
        yy = torch.tensor(ys, dtype=F64)
        A = torch.stack([xx, torch.ones_like(xx)], 1)
        k = torch.linalg.lstsq(A, yy.unsqueeze(1)).solution[:, 0]
        rest = yy - A @ k
        n = len(xs)
        if n > 2:
            s2 = (rest ** 2).sum() / (n - 2)
            se = torch.sqrt(s2 / ((xx - xx.mean()) ** 2).sum()).item()
        else:
            se = float("nan")
        return k[0].item(), k[1].item(), se, rest.abs().max().item()

    auswertung = {}
    zeilen = [f"ROT-1 regge (REGGE-1) {args.stufe}{' RAUCH' if args.rauch else ''}. Start {start}, Ende {jetzt()}, {geraet_name()}, torch {torch.__version__}",
              f"Q = {P_Q}, dx {dx}, dt {dt}, L {L_BOX}, T {T} (erreicht {erg['t_ende']}, Abbruch {erg['abbruch']}), Entwicklung {erg['sek']:.1f} s; Mittel ab t = {ta}",
              "Ball: " + "; ".join(f"b {b:.4f}: omega {e['omega2']:.5f}, S_0 {e['S_0']:.4f}, R_halb {e['R_halb']:.3f}" for b, e in zip(bs, erg_b)),
              "", "g | d0 | d(t>=30) | Omega(t>=30) | d(t>=60) | Omega(t>=60) | fehlt | Q_w | j = J_w - Q_w (std) | eps = E_w - omega_b Q_w (std) | Q/E/J geschluckt"]
    for a in aus:
        zeilen.append(" | ".join([fz(a["g"]), fz(a["d0"]), fz(a["d_30"], "{:.3f}"), fz(a["Omega_30"], "{:.5f}"), fz(a["d_60"], "{:.3f}"),
                                  fz(a["Omega_60"], "{:.5f}"), f"{a['fehlt_60']:.2f}", f"{a['Q_w']:.3f}",
                                  f"{a['j']:.3f} ({a['j_std']:.3f})", f"{a['eps']:.4f} ({a['eps_std']:.4f})",
                                  f"{a['Q_geschluckt']:.3f}/{a['E_geschluckt']:.3f}/{a['J_geschluckt']:.3f}"]))
    for gg in sorted(set(k[0] for k in konf)):
        sel = sorted([a for a in aus if a["g"] == gg and a["d_60"] is not None and a["fehlt_60"] <= 0.3], key=lambda a: a["d_60"])
        if len(sel) < 2:
            continue
        rho_a = sel[0]["rho_a"]
        d = [a["d_60"] for a in sel]
        kj, cj, sej, rj = fit([x * x for x in d], [a["j"] for a in sel])
        ke, ce, see, re_ = fit(d, [a["eps"] for a in sel])
        ham = []
        for a1, a2 in zip(sel[:-1], sel[1:]):
            dj = a2["j"] - a1["j"]
            de = a2["eps"] - a1["eps"]
            om_h = de / dj if abs(dj) > 1e-12 else float("nan")
            om_m = 0.5 * (a1["Omega_60"] + a2["Omega_60"]) if a1["Omega_60"] is not None and a2["Omega_60"] is not None else float("nan")
            ham.append({"d1": a1["d_60"], "d2": a2["d_60"], "delta_j": dj, "delta_eps": de, "Omega_H": om_h, "Omega_mess": om_m,
                        "verh": om_h / om_m if om_m == om_m and om_m != 0 else float("nan")})
        # J gegen E: j - j(d_min) gegen (eps - eps(d_min))^2
        e0, j0 = sel[0]["eps"], sel[0]["j"]
        kje, cje, seje, rje = fit([(a["eps"] - e0) ** 2 for a in sel], [a["j"] - j0 for a in sel])
        auswertung[gg] = {"d": d, "j": [a["j"] for a in sel], "eps": [a["eps"] for a in sel],
                          "Omega": [a["Omega_60"] for a in sel], "steigung_j_d2": kj, "se_j_d2": sej, "rest_j": rj,
                          "magnus_j_d2": -math.pi * rho_a / 2.0, "steigung_eps_d": ke, "se_eps_d": see, "rest_eps": re_,
                          "hamilton": ham, "koeff_j_eps2": kje, "se_j_eps2": seje}
        zeilen += ["", f"g = {gg}: j gegen d^2: Steigung {kj:.4f} +- {sej:.4f} (Fitrest {rj:.3f}); Magnus -pi rho_a/2 = {-math.pi * rho_a / 2.0:.4f}; Regge (sigma 1,75) +0,687",
                   f"   eps gegen d: Steigung {ke:.4f} +- {see:.4f} (Fitrest {re_:.3f})",
                   f"   j - j_min gegen (eps - eps_min)^2: Koeffizient {kje:.4f} +- {seje:.4f}; Magnus -pi rho_a/(2 F^2) mit F = Steigung eps: "
                   + (f"{-math.pi * rho_a / (2.0 * ke * ke):.4f}" if abs(ke) > 1e-9 else "-") + "; Regge +1/(2 pi sigma)",
                   "   Hamilton-Probe (Nachbarn): " + "; ".join(f"d {h['d1']:.2f}->{h['d2']:.2f}: dj {h['delta_j']:+.2f}, deps {h['delta_eps']:+.3f}, "
                                                              f"Omega_H {h['Omega_H']:+.4f} gegen Omega {h['Omega_mess']:+.4f} (Verh. {h['verh']:.2f})" for h in ham)]
    text = "\n".join(zeilen) + "\n"
    schreiben(args.out, f"regge_{args.stufe}", {"start": start, "ende": jetzt(), "T": T, "t_ende": erg["t_ende"], "t_mittel_ab": ta,
                                                "laeufe": aus, "auswertung": auswertung}, text)
    torch.save({"t": t, "glob": gl, "fs": fs, "konf": konf, "FSP": FSP, "GSP": GSP,
                "lagen": [{"t": a["t"], "A": a["wirbel"]["lage_A"], "B": a["wirbel"]["lage_B"]} for a in an]},
               os.path.join(args.out, f"regge_{args.stufe}_roh.pt"))
    EINST["rampe"] = T_RAMP


BD_Q, BD_L, BD_RMAX, BD_T = 3600.0, 48.0, 48.0, 300.0
BD_KONF = ((0.5, 8.0, False), (0.5, 14.0, False), (0.5, 20.0, False), (0.5, 26.0, False),
           (0.0, 14.0, False), (0.0, 26.0, False), (-0.5, 20.0, True))
BD_FEIN = ((0.5, 20.0, False),)
BAND_START = {"linse": False, "w": 1.5, "stamm": "band"}
BD2_KONF = ((0.5, 8.0, False), (0.5, 14.0, False), (0.5, 20.0, False), (0.5, 26.0, False), (-0.5, 20.0, True))
BAND_START_STAMM3 = "band3"   # Wiederholung von band2 mit strenger Zaehlung (Nachtrag zwischen 10:51:52 und 10:53:06 (date))
BS_KONF = tuple((gg, d, False) for gg in (0.5, 0.2) for d in (8.0, 14.0, 20.0, 26.0)) + ((-0.5, 20.0, True),)


def erste_folge(ts, flags, k=3):
    return erste_dauerhaft(ts, flags, k)


def test_band(args):
    """BAND-1 (Vorab BAND-1.md, 10:31:17): psi_1-Wirbel bei (-d/2, 0), psi_2-Wirbel bei (+d/2, 0) im grossen gemischten Ball
    (Q = 3600, L = 48), frei entwickelt (g von Anfang an, T = 300). Je 5: Wirbelgruppen je Komponente und Vorzeichen in
    r < 0,85 R, Lagen A und B, Wandkreuzungen auf dem Kreis um die Paarmitte (d/2 + 3) und auf dem Randkreis 0,85 R,
    Klumpen. Einordnung nach der Scheiterregel BAND-1.md 5."""
    start = jetzt()
    EINST["rampe"] = 0.0
    dx, dt = STUFEN[args.stufe]
    T = BD_T
    konf = list(BD_FEIN if args.stufe == "fein" else (BD2_KONF if BAND_START["linse"] else BD_KONF))
    if args.rauch:
        konf = [(0.5, 14.0, False), (-0.5, 14.0, True)]
        if args.geraet == "cpu":
            dx, dt, T = 0.6, 0.1, 20.0
        else:
            T = 0.05 * T
    gr = Gitter(BD_L, dx)
    bs = sorted(set(1.0 + abs(k[0]) / 4.0 for k in konf))
    rad = Radial(rmax=BD_RMAX)
    erg_b, verl_b = rad.loesen([{"name": f"ball_b{b:.3f}", "Q1": 0.0, "Q2": BD_Q, "b": b} for b in bs], n_it=rauch_it(args.rauch))
    ball = {round(b, 6): e for b, e in zip(bs, erg_b)}
    X, Y = gr.x[0], gr.y[0]
    rr = torch.sqrt(X * X + Y * Y)
    psis, vels, rh = [], [], []
    for gg, d, dreh in konf:
        e = ball[round(1.0 + abs(gg) / 4.0, 6)]
        _, F = profil_werte(e, rr)
        vA = ((X + 0.5 * d) + 1j * Y) / torch.sqrt((X + 0.5 * d) ** 2 + Y ** 2 + P_XI ** 2)
        vB = ((X - 0.5 * d) + 1j * Y) / torch.sqrt((X - 0.5 * d) ** 2 + Y ** 2 + P_XI ** 2)
        if BAND_START["linse"]:
            # duenne Anfangslinse (BAND-1 Nachtrag 10:43:42): Delta = f(Delta_dipol), f monoton, Windung erhalten
            Dd = torch.angle(vB * vA.conj()).clamp(-math.pi + 1e-9, math.pi - 1e-9)
            dl = min(4.0 * BAND_START["w"] / d, 0.8)
            T0 = 1.0 / math.tan(0.5 * dl)
            fD = 2.0 * torch.atan(torch.sign(Dd) * (torch.tan(0.5 * Dd).abs() / T0) ** 3)
            hD = 0.5 * (Dd - fD)
            p = torch.stack([F / math.sqrt(2.0) * vA * torch.exp(1j * hD), F / math.sqrt(2.0) * vB * torch.exp(-1j * hD) * (1j if dreh else 1.0)])
        else:
            p = torch.stack([F / math.sqrt(2.0) * vA, F / math.sqrt(2.0) * vB * (1j if dreh else 1.0)])
        psis.append(p)
        vels.append(-1j * e["omega2"] * p)
        rh.append(e["R_halb"])
    psi = torch.stack(psis).contiguous()
    vel = torch.stack(vels).contiguous()
    B = len(konf)
    gfin = torch.tensor([k[0] for k in konf], dtype=F64, device=DEV)
    R_b = torch.tensor(rh, dtype=F64, device=DEV)
    r_win = R_b + 6.0
    daempf = torch.exp(-gr.sigma * dt).unsqueeze(1)
    alle = max(1, int(round(T_MEAS / dt)))
    ana = max(1, int(round(ANALYSE_DT / dt)))
    n_schritte = int(round(T / dt))
    zx = torch.zeros(B, dtype=F64, device=DEV)
    zy = torch.zeros(B, dtype=F64, device=DEV)
    lageA = [(-0.5 * k[1], 0.0) for k in konf]
    lageB = [(0.5 * k[1], 0.0) for k in konf]
    s0 = (psi.real ** 2 + psi.imag ** 2).sum(1)
    s0max = s0.amax((1, 2))
    sb0 = torch.fft.ifft2(torch.fft.fft2(s0) * gr.blur).real
    schwelle = SCHWELLE_REL * sb0.amax((1, 2))
    q_min = [Q_MIN_REL * BD_Q] * B
    reihe_t, reihe_g, reihe_f, analysen = [], [], [], []
    bilder = {}
    t_snap = (50.0, 150.0) if not args.rauch else ()
    t0 = uhr()

    def analyse(t, xc, yc):
        s = (psi.real ** 2 + psi.imag ** 2).sum(1)
        rho = (2.0 * (psi * vel.conj()).imag).sum(1)
        kz = klumpenzahl(gr, s, rho, schwelle, q_min)
        Xc = gr.x - xc.view(-1, 1, 1)
        Yc = gr.y - yc.view(-1, 1, 1)
        innen = ((Xc * Xc + Yc * Yc) < ((0.85 * R_b) ** 2).view(-1, 1, 1)) & (s > 0.05 * s0max.view(-1, 1, 1))
        zahl = {}
        masken = {}
        for a, name in ((0, "1"), (1, "2")):
            w = bloecke(torch.angle(psi[:, a]))
            for sg, tag in ((1, "p"), (-1, "m")):
                mk = (w * sg > 0.5) & innen
                masken[name + tag] = mk
                lab = komponenten(mk)
                zahl[name + tag] = [int(torch.unique(lab[b][mk[b]]).numel()) if bool(mk[b].any()) else 0 for b in range(B)]
                # Nachtrag zwischen 10:51:52 und 10:53:06 (date) (nachtraegliche Diagnose, nicht Teil der Scheiterregel): nur Bloecke mit S > 0,3 S_max (gefuellte
                # Einkomponenten-Wirbel); Umlaeufe ueber einen Strich verschwindender Dichte (Schlitz) fallen heraus
                mks = mk & (s > 0.3 * s0max.view(-1, 1, 1))
                labs = komponenten(mks)
                zahl["s" + name + tag] = [int(torch.unique(labs[b][mks[b]]).numel()) if bool(mks[b].any()) else 0 for b in range(B)]
        eintr = {"t": t, "klumpen": kz, "zahl": zahl, "A": [], "B": [], "d": [], "w_paar": [], "w_rand": [], "W_rand": []}
        for b in range(B):
            for key, alt, liste in (("1p", lageA, eintr["A"]), ("2p", lageB, eintr["B"])):
                mk = masken[key][b]
                if bool(mk.any()):
                    xs, ys = gr.X2[mk], gr.Y2[mk]
                    dd = (xs - alt[b][0]) ** 2 + (ys - alt[b][1]) ** 2
                    i = int(dd.argmin())
                    alt[b] = (xs[i].item(), ys[i].item())
                    liste.append(alt[b])
                else:
                    liste.append(None)
            A_, B_ = eintr["A"][-1], eintr["B"][-1]
            sgn = 1 if konf[b][0] >= 0 else -1
            if A_ is not None and B_ is not None:
                dab = math.hypot(B_[0] - A_[0], B_[1] - A_[1])
                mx, my = 0.5 * (A_[0] + B_[0]), 0.5 * (A_[1] + B_[1])
                kp = kreis_waende(gr, psi[b, 0], psi[b, 1], mx, my, (0.5 * dab + 3.0,), sgn)[0]
                eintr["d"].append(dab)
                eintr["w_paar"].append(kp["wechsel"])
                # Lage der uebrigen Windungsbloecke: im Bandbereich (Abstand zur Strecke AB < 3, nicht naeher als 2 an A oder B)
                # oder sonst im Ball (Nachtrag 10:34, vor dem ersten GPU-Lauf)
                alle_b = masken["1p"][b] | masken["1m"][b] | masken["2p"][b] | masken["2m"][b]
                xs, ys = gr.X2[alle_b], gr.Y2[alle_b]
                ax_, ay_, bx_, by_ = A_[0], A_[1], B_[0], B_[1]
                vx, vy = bx_ - ax_, by_ - ay_
                ll = max(vx * vx + vy * vy, 1e-12)
                tpar = (((xs - ax_) * vx + (ys - ay_) * vy) / ll).clamp(0.0, 1.0)
                dseg = torch.sqrt((xs - ax_ - tpar * vx) ** 2 + (ys - ay_ - tpar * vy) ** 2)
                dA_ = torch.sqrt((xs - ax_) ** 2 + (ys - ay_) ** 2)
                dB_ = torch.sqrt((xs - bx_) ** 2 + (ys - by_) ** 2)
                end = (dA_ < 2.0) | (dB_ < 2.0)
                eintr.setdefault("band_bloecke", []).append(int(((dseg < 3.0) & ~end).sum().item()))
                eintr.setdefault("sonst_bloecke", []).append(int(((dseg >= 3.0) & ~end).sum().item()))
            else:
                eintr["d"].append(None)
                eintr["w_paar"].append(None)
                eintr.setdefault("band_bloecke", []).append(None)
                eintr.setdefault("sonst_bloecke", []).append(None)
            kr = kreis_waende(gr, psi[b, 0], psi[b, 1], xc[b].item(), yc[b].item(), (0.85 * R_b[b].item(),), sgn)[0]
            eintr["w_rand"].append(kr["wechsel"])
            eintr["W_rand"].append((kr["W1"], kr["W2"]))
        analysen.append(eintr)

    glob, fs, xc, yc, s, rho = messen(gr, psi, vel, gfin, zx, zy, r_win)
    reihe_t.append(0.0)
    reihe_g.append(glob)
    reihe_f.append(fs)
    zx, zy = xc, yc
    analyse(0.0, xc, yc)
    bilder[0.0] = [schnitt(gr, psi[b], 0.0, 0.0, halb=32.0) for b in range(B)]

    def kraft_b(p):
        return kraft(gr, p, gfin)

    F_ = kraft_b(psi)
    t_ende = 0.0
    abbruch = False
    for n in range(1, n_schritte + 1):
        t = n * dt
        vel.add_(F_, alpha=0.5 * dt)
        psi.add_(vel, alpha=dt)
        F_ = kraft_b(psi)
        vel.add_(F_, alpha=0.5 * dt)
        vel.mul_(daempf)
        if n % alle == 0:
            glob, fs, xc, yc, s, rho = messen(gr, psi, vel, gfin, zx, zy, r_win)
            reihe_t.append(t)
            reihe_g.append(glob)
            reihe_f.append(fs)
            zx, zy = xc, yc
            t_ende = t
            if n % ana == 0:
                analyse(t, xc, yc)
            if any(abs(t - ts) < 0.5 * dt * alle for ts in t_snap):
                bilder[t] = [schnitt(gr, psi[b], 0.0, 0.0, halb=32.0) for b in range(B)]
            if uhr() - t0 > args.budget:
                abbruch = True
                break
    bilder[t_ende] = [schnitt(gr, psi[b], 0.0, 0.0, halb=32.0) for b in range(B)]
    sek = uhr() - t0
    tt = torch.tensor(reihe_t, dtype=F64)
    gl = torch.stack(reihe_g).cpu()
    fsr = torch.stack(reihe_f).cpu()
    if not bool(torch.isfinite(gl).all()):
        raise RuntimeError("band: nicht endlich")
    ix = {k: i for i, k in enumerate(FSP)}
    aus = []
    namen = []
    for b, (gg, d0, dreh) in enumerate(konf):
        ts = [a["t"] for a in analysen]
        extra = [((a["zahl"]["1p"][b] - 1) + a["zahl"]["1m"][b] + (a["zahl"]["2p"][b] - 1) + a["zahl"]["2m"][b]) for a in analysen]
        beide = [a["zahl"]["1p"][b] >= 1 and a["zahl"]["2p"][b] >= 1 for a in analysen]
        wp = [a["w_paar"][b] for a in analysen]
        wr = [a["w_rand"][b] for a in analysen]
        kl = [a["klumpen"][b] for a in analysen]
        qw = (fsr[:, b, ix["Q1w"]] + fsr[:, b, ix["Q2w"]])
        t_extra = erste_folge(ts, [e > 0 and bb for e, bb in zip(extra, beide)])
        t_umgelegt = erste_folge(ts, [w is not None and w >= 2 for w in wp])
        t_klumpen = erste_folge(ts, [k >= 2 for k in kl])
        q_ende = qw[-1].item() / qw[0].item()
        rand_w = sum(1 for w in wr if w and w > 0) / max(len(wr), 1)
        anteil_verbunden = sum(1 for w in wp if w == 0) / max(sum(1 for w in wp if w is not None), 1)
        if t_klumpen is not None or (rand_w > 0 and q_ende < 0.8):
            klasse = "zerschnitten"
        elif t_extra is not None or t_umgelegt is not None:
            klasse = "reisst"
        elif anteil_verbunden >= 0.8 and max(kl) <= 1:
            klasse = "reisst nicht"
        else:
            klasse = "unklar"
        ds = [x for x in (a["d"][b] for a in analysen) if x is not None]
        bz = bilanz(tt, gl[:, b], 0.0, None)
        eintrag = {"g": gg, "d0": d0, "psi2_mal_i": dreh, "klasse": klasse, "t_extra": t_extra, "t_umgelegt": t_umgelegt,
                   "t_klumpen": t_klumpen, "anteil_verbunden": anteil_verbunden, "randkreis_wechsel_anteil": rand_w,
                   "Q_w_ende_rel": q_ende, "extra_max": max(extra), "d_start": ds[0] if ds else None, "d_ende": ds[-1] if ds else None,
                   "d_min": min(ds) if ds else None, "d_max": max(ds) if ds else None, "bilanz": bz,
                   "reihe": {"t": ts, "extra": extra, "w_paar": wp, "w_rand": wr, "klumpen": kl, "d": [a["d"][b] for a in analysen],
                             "zahl": {k: [a["zahl"][k][b] for a in analysen] for k in ("1p", "1m", "2p", "2m")},
                             "band_bloecke": [a["band_bloecke"][b] for a in analysen],
                             "sonst_bloecke": [a["sonst_bloecke"][b] for a in analysen]}}
        bb_ = [x for x in eintrag["reihe"]["band_bloecke"] if x is not None]
        sb_ = [x for x in eintrag["reihe"]["sonst_bloecke"] if x is not None]
        eintrag["band_bloecke_max"] = max(bb_) if bb_ else None
        eintrag["sonst_bloecke_max"] = max(sb_) if sb_ else None
        eintrag["t_band_bloecke"] = erste_folge(ts, [x is not None and x > 0 for x in eintrag["reihe"]["band_bloecke"]])
        ext_s = [max(0, a["zahl"]["s1p"][b] - 1) + a["zahl"]["s1m"][b] + max(0, a["zahl"]["s2p"][b] - 1) + a["zahl"]["s2m"][b] for a in analysen]
        eintrag["reihe"]["extra_streng"] = ext_s
        eintrag["extra_streng_max"] = max(ext_s)
        eintrag["t_extra_streng"] = erste_folge(ts, [e > 0 for e in ext_s])
        aus.append(eintrag)
        namen.append(f"g{gg}_d{d0:.0f}{'_ipsi2' if dreh else ''}")
    k4 = None
    if (0.5, 20.0, False) in konf and (-0.5, 20.0, True) in konf:
        ia, ib = konf.index((0.5, 20.0, False)), konf.index((-0.5, 20.0, True))
        sa = psi[ia].real ** 2 + psi[ia].imag ** 2
        sb = psi[ib].real ** 2 + psi[ib].imag ** 2
        k4 = {"dichte": (sa - sb).abs().max().item() / sa.max().item(), "E_Reihe": (gl[:, ia, 2] - gl[:, ib, 2]).abs().max().item()}
    zeilen = [f"ROT-1 {BAND_START['stamm']} (BAND-1, Linse {BAND_START['linse']}) {args.stufe}{' RAUCH' if args.rauch else ''}. Start {start}, Ende {jetzt()}, {geraet_name()}, torch {torch.__version__}",
              f"Q = {BD_Q}, L = {BD_L}, dx {dx}, dt {dt}, n {gr.n}, T {T} (erreicht {t_ende}, Abbruch {abbruch}), Entwicklung {sek:.1f} s, Hochrechnung x20 {20 * sek:.0f} s",
              "Ball: " + "; ".join(f"b {b:.4f}: omega {e['omega2']:.5f}, S_0 {e['S_0']:.4f}, R_halb {e['R_halb']:.3f}, Residuum {e['residuum']:.1e}" for b, e in zip(bs, erg_b)),
              "", "lauf | Klasse | t_extra | t_umgelegt | t_klumpen | Anteil verbunden | Randkreis-Wechsel-Anteil | Q_w Ende/Start | extra max | Bloecke Band max (t ab 3x) / sonst max | d Start/min/max/Ende | Bilanz Q/E | Q geschluckt"]
    for n_, a in zip(namen, aus):
        zeilen.append(" | ".join([n_, a["klasse"], fz(a["t_extra"]), fz(a["t_umgelegt"]), fz(a["t_klumpen"]), f"{a['anteil_verbunden']:.2f}",
                                  f"{a['randkreis_wechsel_anteil']:.2f}", f"{a['Q_w_ende_rel']:.3f}", str(a["extra_max"]),
                                  f"{a['band_bloecke_max']} ({fz(a['t_band_bloecke'])}) / {a['sonst_bloecke_max']} / streng {a['extra_streng_max']} ({fz(a['t_extra_streng'])})",
                                  f"{fz(a['d_start'], '{:.2f}')}/{fz(a['d_min'], '{:.2f}')}/{fz(a['d_max'], '{:.2f}')}/{fz(a['d_ende'], '{:.2f}')}",
                                  f"{a['bilanz']['Q']:.1e}/{a['bilanz']['E']:.1e}", f"{a['bilanz']['Q_geschluckt_rel']:.3f}"]))
    zeilen += ["", "Zeitreihen je 25 (extra Wirbelgruppen / Wandkreuzungen Paarkreis / Randkreis / Klumpen / d):"]
    for n_, a in zip(namen, aus):
        r = a["reihe"]
        zeilen.append(f"  {n_}: " + "; ".join(f"t {t:.0f}: {e}/{fz(w)}/{fz(v)}/{k}/{fz(dd, '{:.1f}')}" for i, (t, e, w, v, k, dd) in
                                              enumerate(zip(r["t"], r["extra"], r["w_paar"], r["w_rand"], r["klumpen"], r["d"])) if i % 5 == 0))
    if k4:
        zeilen.append(f"K4 (d = 20): Dichte -g (i psi_2) gegen +g am Ende {k4['dichte']:.2e}; E-Reihe {k4['E_Reihe']:.2e}")
    text = "\n".join(zeilen) + "\n"
    schreiben(args.out, f"{BAND_START['stamm']}_{args.stufe}", {"start": start, "ende": jetzt(), "T": T, "t_ende": t_ende, "konf": [list(k) for k in konf],
                                               "laeufe": aus, "K4": k4}, text)
    torch.save({"t": tt, "glob": gl, "fs": fsr, "konf": konf, "FSP": FSP, "GSP": GSP}, os.path.join(args.out, f"{BAND_START['stamm']}_{args.stufe}_roh.pt"))
    bilder_schreiben(args.out, BAND_START["stamm"], args.stufe, namen, bilder, "BAND-1 frei " + BAND_START["stamm"], halb=32.0)
    EINST["rampe"] = T_RAMP


def test_bandstat(args):
    """BAND-1 statisch: geklammerter Gradientenfluss wie paar, grosser Ball Q = 3600, L = 48."""
    PP.update({"Q": BD_Q, "L": BD_L, "rmax": BD_RMAX, "konf": BS_KONF, "stamm": "bandstat", "halb": 32.0})
    try:
        test_paar(args)
    finally:
        PP.update({"Q": P_Q, "L": L_BOX, "rmax": RMAX, "konf": None, "stamm": "paar", "halb": 14.0})


def test_band2(args):
    """BAND-1 frei mit duenner Anfangslinse (Nachtrag 10:43:42)."""
    BAND_START.update({"linse": True, "stamm": "band2"})
    try:
        test_band(args)
    finally:
        BAND_START.update({"linse": False, "stamm": "band"})


def test_band3(args):
    """BAND-1: band2 wiederholt (gleiche Physik), zusaetzlich strenge Wirbelzaehlung S > 0,3 S_max (Nachtrag zwischen 10:51:52 und 10:53:06 (date))."""
    BAND_START.update({"linse": True, "stamm": BAND_START_STAMM3})
    try:
        test_band(args)
    finally:
        BAND_START.update({"linse": False, "stamm": "band"})


def test_bandstat2(args):
    """BAND-1 statisch, Nachtrag 10:37: bandstat mit 6000 Iterationen war nicht konvergiert (Drift bis 4,8 in 1000
    Iterationen). Gleiche Konfigurationen, tau 0,5 und 16000 Iterationen (Pseudozeit 8000 statt 1800)."""
    PP.update({"Q": BD_Q, "L": BD_L, "rmax": BD_RMAX, "konf": BS_KONF, "stamm": "bandstat2", "halb": 32.0, "tau": 0.5, "it": 16000})
    try:
        test_paar(args)
    finally:
        PP.update({"Q": P_Q, "L": L_BOX, "rmax": RMAX, "konf": None, "stamm": "paar", "halb": 14.0})
        PP.pop("tau", None)
        PP.pop("it", None)


# ================================================================ Y-1 (Runde 10): N = 3, Dreier mit Y-Knoten (PLAN.md)

Y_Q, Y_L, Y_RMAX = 3600.0, 38.4, 40.0
Y_TAU, Y_IT = 0.5, 12000
Y_KL_IN, Y_KL_AUS, Y_XI, Y_LINSE_W = 0.5, 2.0, 1.0, 1.0
Y_KONV = 0.02                       # Scheiterregel PLAN 7: max |dE| in 1000 Iterationen
SQ3 = math.sqrt(3.0)
Y_GEOS = [("gleich", 6.0), ("gleich", 9.0), ("gleich", 12.0), ("gleich", 15.0),
          ("gestreckt", 9.0), ("gestreckt", 13.0), ("stumpf", 6.0), ("stumpf", 9.0),
          ("kollinear", 5.0), ("kollinear", 6.5), ("kollinear", 8.0), ("kollinear", 10.0)]
ROT1_PAAR_E = {(0.5, 5.0): 484.2497786146344, (0.5, 6.5): 485.771014846081, (0.5, 8.0): 487.24106352260367,
               (0.5, 9.5): 488.6240918368635, (0.2, 5.0): 521.0848032847764, (0.2, 6.5): 521.8434659892106,
               (0.2, 8.0): 522.7773047888087, (0.2, 9.5): 523.8362122281067}   # RUNDE-09/rot1/lauf-69/ausgabe/paar_ergebnis.json


def steiner(P):
    """Fermat-Steiner-Punkt, L_St und ggf. Ecke (Winkel >= 120 Grad) fuer drei Punkte."""
    pts = [complex(x, y) for x, y in P]
    for i in range(3):
        a, b, c = pts[i], pts[(i + 1) % 3], pts[(i + 2) % 3]
        u, v = b - a, c - a
        if (u.real * v.real + u.imag * v.imag) / (abs(u) * abs(v)) <= -0.5 + 1e-12:
            return (a.real, a.imag), abs(u) + abs(v), i
    z = sum(pts) / 3.0
    for _ in range(20000):
        w = [1.0 / max(abs(z - p), 1e-12) for p in pts]
        zn = sum(wi * p for wi, p in zip(w, pts)) / sum(w)
        fertig = abs(zn - z) < 1e-14
        z = zn
        if fertig:
            break
    return (z.real, z.imag), sum(abs(z - p) for p in pts), None


def geo_dreier(typ, s):
    """PLAN 3: Ecken A (psi_1), B (psi_2), C (psi_3), Schwerpunkt im Ursprung."""
    if typ == "gleich":
        r = s / SQ3
        P = [(r * math.cos(math.radians(210.0)), r * math.sin(math.radians(210.0))),
             (r * math.cos(math.radians(330.0)), r * math.sin(math.radians(330.0))), (0.0, r)]
    elif typ == "gestreckt":
        h, bx = math.cos(math.radians(20.0)) * s, math.sin(math.radians(20.0)) * s
        yc = 2.0 * h / 3.0
        P = [(-bx, yc - h), (bx, yc - h), (0.0, yc)]
    elif typ == "stumpf":
        hx, hy = math.sin(math.radians(75.0)) * s, math.cos(math.radians(75.0)) * s
        yb = 2.0 * hy / 3.0
        P = [(-hx, yb - hy), (0.0, yb), (hx, yb - hy)]
    elif typ == "kollinear":
        P = [(-s, 0.0), (0.0, 0.0), (s, 0.0)]
    else:
        raise ValueError(typ)
    J, Lst, ecke = steiner(P)
    kanten = [math.dist(P[1], P[2]), math.dist(P[2], P[0]), math.dist(P[0], P[1])]   # gegenueber A, B, C
    kette = [(kanten[(i + 1) % 3] + kanten[(i + 2) % 3], i) for i in range(3)]
    kl, ki = min(kette)
    return {"typ": typ, "s": s, "ecken": P, "J": J, "L_St": Lst, "P2": 0.5 * sum(kanten), "kanten": kanten,
            "kette": kl, "kette_ecke": ki, "knoten_ecke": ecke, "rho": max(math.hypot(x, y) for x, y in P)}


def k_dreier(g, typ, s, saat, c=0.0, perm=(0, 1, 2), ziel=None, modus="gesamt", zusatz=""):
    geo = geo_dreier(typ, s)
    wirbel = [(perm[i], geo["ecken"][i][0], geo["ecken"][i][1], 1) for i in range(3)]
    Js = geo["J"] if saat == "Y" else (geo["ecken"][geo["kette_ecke"]] if saat == "kette" else None)
    pt = "" if tuple(perm) == (0, 1, 2) else "_p" + "".join(str(p + 1) for p in perm)
    return {"name": f"g{g:+.1f}_{typ}{s:g}_{saat}{pt}{zusatz}", "art": "dreier", "g": g, "c": c, "wirbel": wirbel,
            "saat": saat, "J_saat": Js, "ziel": ziel if ziel is not None else (0.0, 0.0), "modus": modus,
            "aktiv": (0, 1, 2), "geo": geo, "perm": list(perm)}


def k_zwei(art, g, d, modus="gesamt"):
    """meson: psi_1-Wirbel (+1) und psi_1-Gegenwirbel (-1); paar3: psi_1 bei A, psi_2 bei B, psi_3 ohne Wirbel;
    k1: wie paar3, aber psi_3 = 0 (N = 2 wie ROT-1 paar)."""
    if art == "meson":
        wirbel = [(0, -0.5 * d, 0.0, 1), (0, 0.5 * d, 0.0, -1)]
    else:
        wirbel = [(0, -0.5 * d, 0.0, 1), (1, 0.5 * d, 0.0, 1)]
    geo = {"typ": art, "s": d, "ecken": [(-0.5 * d, 0.0), (0.5 * d, 0.0)], "J": (0.0, 0.0), "rho": 0.5 * d}
    return {"name": f"{art}_g{g:+.1f}_d{d:g}", "art": art, "g": g, "c": 0.0, "wirbel": wirbel, "saat": "neutral",
            "J_saat": None, "ziel": None if art == "k1" else (0.0, 0.0), "modus": "einzeln" if art == "k1" else modus,
            "aktiv": (0, 1) if art == "k1" else (0, 1, 2), "geo": geo, "perm": [0, 1, 2]}


def linse_f(D, laenge):
    """Stauchung wie BAND-1 band2: f monoton, f(+-pi) = +-pi, f ~ 0 ausserhalb einer Linse der Halbbreite ~Y_LINSE_W."""
    dl = min(4.0 * Y_LINSE_W / max(laenge, 1e-9), 0.8)
    T0 = 1.0 / math.tan(0.5 * dl)
    Dc = D.clamp(-math.pi + 1e-9, math.pi - 1e-9)
    return 2.0 * torch.atan(torch.sign(Dc) * (torch.tan(0.5 * Dc).abs() / T0) ** 3)


def umlauf_z(z):
    ph = torch.angle(z)
    d = torch.remainder(ph.roll(-1) - ph + math.pi, 2.0 * math.pi) - math.pi
    return d.sum().item() / (2.0 * math.pi)


def b_von(k):
    na = len(k["aktiv"])
    return 1.0 + k["g"] * (na - 1) / (2.0 * na) - k["c"] / na


def y_statik(args, stamm, konf, Q=Y_Q, L=Y_L, rmax=Y_RMAX, tau=Y_TAU, n_it=Y_IT, com=True, dx=0.3, kl_aus=Y_KL_AUS):
    start = jetzt()
    t0 = uhr()
    if args.rauch:
        konf = konf[:3]
        if args.geraet == "cpu":
            dx, n_it = 0.6, 300
        else:
            n_it = min(n_it, 1000)
    gr = Gitter(L, dx)
    B, n, dA = len(konf), gr.n, gr.dA
    X, Y = gr.x[0], gr.y[0]
    Xf, Yf = gr.X2, gr.Y2
    bs = sorted(set(round(b_von(k), 9) for k in konf))
    rad = Radial(rmax=rmax)
    erg_b, _ = rad.loesen([{"name": f"ball_b{b:.4f}", "Q1": 0.0, "Q2": Q, "b": b} for b in bs], n_it=rauch_it(args.rauch))
    ball = {round(b, 9): e for b, e in zip(bs, erg_b)}
    t_rad = uhr() - t0
    rr = torch.sqrt(X * X + Y * Y)
    K = max(len(k["wirbel"]) for k in konf)
    kl_ring = torch.zeros((B, K, n, n), dtype=F64, device=DEV)
    kl_e = torch.ones((B, K, n, n), dtype=C128, device=DEV)
    kl_a = torch.zeros((B, K), dtype=torch.long, device=DEV)
    psis = []
    for i, k in enumerate(konf):
        e = ball[round(b_von(k), 9)]
        _, F = profil_werte(e, rr)
        amp = (F / math.sqrt(len(k["aktiv"]))).to(C128)
        J = k["J_saat"]
        thJ = torch.atan2(Y - J[1], X - J[0]) if J is not None else None
        felder = []
        for a in range(3):
            if a not in k["aktiv"]:
                felder.append(torch.zeros((n, n), dtype=C128, device=DEV))
                continue
            p = amp.clone()
            eig = [w for w in k["wirbel"] if w[0] == a]
            if J is None:
                for (_, xv, yv, wv) in eig:
                    p = p * ((X - xv) + 1j * wv * (Y - yv)) / torch.sqrt((X - xv) ** 2 + (Y - yv) ** 2 + Y_XI ** 2)
            else:
                if len(eig) != 1 or eig[0][3] != 1:
                    raise ValueError("Y-/Kettensaat nur fuer je einen +1-Wirbel je Komponente")
                _, xv, yv, _ = eig[0]
                r2 = (X - xv) ** 2 + (Y - yv) ** 2
                D = torch.remainder(torch.atan2(Y - yv, X - xv) - thJ + math.pi, 2.0 * math.pi) - math.pi
                arm = math.hypot(xv - J[0], yv - J[1])
                th = thJ + (linse_f(D, arm) if arm > 1e-6 else torch.zeros_like(D))
                p = p * torch.sqrt(r2 / (r2 + Y_XI ** 2)) * torch.exp(1j * th)
            felder.append(p)
        psis.append(torch.stack(felder))
        for j, (a, xv, yv, wv) in enumerate(k["wirbel"]):
            rc = torch.sqrt((X - xv) ** 2 + (Y - yv) ** 2)
            kl_ring[i, j] = ((rc > Y_KL_IN) & (rc < kl_aus)).to(F64)
            kl_e[i, j] = ((X - xv) + 1j * wv * (Y - yv)) / rc.clamp(min=1e-12)
            kl_a[i, j] = a
    psi = torch.stack(psis).contiguous()
    ar = torch.arange(B, device=DEV)

    def klammer(psi):
        for j in range(K):
            a = kl_a[:, j]
            sel = psi[ar, a]
            ring = kl_ring[:, j]
            c = (sel * kl_e[:, j].conj() * ring).sum((1, 2))
            c = c / c.abs().clamp(min=1e-300)
            psi[ar, a] = torch.where(ring > 0, sel.abs() * kl_e[:, j] * c.view(B, 1, 1), sel)
        return psi

    gk = torch.tensor([k["g"] for k in konf], dtype=F64, device=DEV).view(B, 1, 1, 1)
    ck = torch.tensor([k["c"] for k in konf], dtype=F64, device=DEV).view(B, 1, 1, 1)
    einzeln = torch.tensor([k["modus"] == "einzeln" for k in konf], dtype=torch.bool, device=DEV)
    qa = torch.tensor([[(Q / len(k["aktiv"]) if a in k["aktiv"] else 0.0) for a in range(3)] for k in konf], dtype=F64, device=DEV)
    ziel = torch.tensor([k["ziel"] if k["ziel"] is not None else (0.0, 0.0) for k in konf], dtype=F64, device=DEV)
    com_an = torch.tensor([bool(com) and k["ziel"] is not None for k in konf], dtype=torch.bool, device=DEV)
    nenner = 1.0 - tau * gr.minus_k2

    def omega2(s_a):
        Na = s_a.sum((2, 3)) * dA
        N = Na.sum(1)
        w2g = (Q / (2.0 * N)) ** 2
        w2e = torch.where(qa > 0, (qa / (2.0 * Na.clamp(min=1e-300))) ** 2, torch.zeros_like(qa))
        return torch.where(einzeln.view(B, 1), w2e, w2g.view(B, 1).expand(B, 3)), Na, N

    def energie(psi):
        s_a = psi.real ** 2 + psi.imag ** 2
        S = s_a.sum(1)
        Na = s_a.sum((2, 3)) * dA
        N = Na.sum(1)
        gx, gy = grad(gr, psi)
        G = (gx.real ** 2 + gx.imag ** 2 + gy.real ** 2 + gy.imag ** 2).sum((1, 2, 3)) * dA
        V = upot(S).sum((1, 2)) * dA
        P = (psi * psi).sum(1)
        q4 = (s_a * s_a).sum(1)
        Cl = 0.5 * (P.real ** 2 + P.imag ** 2 - q4)
        C = Cl.sum((1, 2)) * dA
        Q4 = q4.sum((1, 2)) * dA
        Kg = Q * Q / (4.0 * N)
        Ke = torch.where(qa > 0, qa * qa / (4.0 * Na.clamp(min=1e-300)), torch.zeros_like(qa)).sum(1)
        Kin = torch.where(einzeln, Ke, Kg)
        E = Kin + G + V - gk.view(B) * C + ck.view(B) * Q4
        return {"E": E, "K": Kin, "G": G, "V": V, "C": C, "Q4": Q4, "Na": Na, "N": N, "S": S, "s_a": s_a, "P": P, "Cl": Cl}

    psi = klammer(psi)
    verlauf = []
    schub = torch.zeros(B, dtype=F64, device=DEV)
    abbruch = False
    it_end = n_it
    t_schleife = uhr()
    for it in range(1, n_it + 1):
        s_a = psi.real ** 2 + psi.imag ** 2
        S = s_a.sum(1, keepdim=True)
        w2, _, _ = omega2(s_a)
        P = (psi * psi).sum(1, keepdim=True)
        nl = (1.0 + S * (1.5 * S - 2.0) - w2.view(B, 3, 1, 1) + 2.0 * ck * s_a) * psi - gk * (psi.conj() * (P - psi * psi))
        ft = torch.fft.fft2(psi - tau * nl) / nenner
        if com:
            S0 = S[:, 0]
            m = S0.sum((1, 2)).clamp(min=1e-300)
            sx = torch.where(com_an, (S0 * Xf).sum((1, 2)) / m - ziel[:, 0], torch.zeros(B, dtype=F64, device=DEV))
            sy = torch.where(com_an, (S0 * Yf).sum((1, 2)) / m - ziel[:, 1], torch.zeros(B, dtype=F64, device=DEV))
            schub += torch.sqrt(sx * sx + sy * sy)
            ft = ft * torch.exp(1j * (gr.kx * sx.view(B, 1, 1, 1) + gr.ky * sy.view(B, 1, 1, 1)))
        psi = klammer(torch.fft.ifft2(ft))
        if it % 200 == 0 or it == n_it:
            en = energie(psi)
            verlauf.append({"it": it, "E": en["E"].tolist()})
            if not bool(torch.isfinite(en["E"]).all()):
                raise RuntimeError("y1: nicht endlich")
            if it == 200:
                print(f"{stamm}: 200 Iterationen in {uhr() - t_schleife:.1f} s, Hochrechnung {n_it / 200 * (uhr() - t_schleife):.0f} s", flush=True)
            if uhr() - t0 > args.budget:
                abbruch = True
                it_end = it
                break
    t_iter = uhr() - t_schleife
    en = energie(psi)
    s_a, S, P, Cl = en["s_a"], en["S"], en["P"], en["Cl"]
    w2, Na, N = omega2(s_a)
    lap = torch.fft.ifft2(torch.fft.fft2(psi) * gr.minus_k2)
    Sk, Pk = S.unsqueeze(1), P.unsqueeze(1)
    rest = -lap + (1.0 + Sk * (1.5 * Sk - 2.0) - w2.view(B, 3, 1, 1) + 2.0 * ck * s_a) * psi - gk * (psi.conj() * (Pk - psi * psi))
    frei = torch.ones((B, n, n), dtype=F64, device=DEV)
    for i, k in enumerate(konf):
        for (a, xv, yv, wv) in k["wirbel"]:
            frei[i] = frei[i] * (((Xf - xv) ** 2 + (Yf - yv) ** 2) > 2.5 ** 2).to(F64)
    res_frei = torch.sqrt(((rest.abs() ** 2).sum(1) * frei).sum((1, 2)) / ((psi.abs() ** 2).sum(1) * frei).sum((1, 2)))
    th = torch.arange(N_THETA, dtype=F64, device=DEV) * (2.0 * math.pi / N_THETA)
    tq = torch.linspace(-4.0, 4.0, 33, dtype=F64, device=DEV)
    aus = []
    bilder = []
    for i, k in enumerate(konf):
        geo = k["geo"]
        e_b = ball[round(b_von(k), 9)]
        R_b = e_b["R_halb"]
        akt = k["aktiv"]
        Si, sai, Pi = S[i], s_a[i], P[i]
        # Knoten: Windungen von arg P (P = psi.psi); Soll Windung 2 im Knoten (PLAN 2.3)
        pl = plaketten(torch.angle(Pi))
        # keine Dichtemaske: im Knoten verschwindet auch S (Rauchtest 11:14/11:15); nur das Ballinnere zaehlt
        m = (pl != 0) & ((Xf ** 2 + Yf ** 2) < (R_b - 3.0) ** 2)
        pw = [((x_ + 0.5 * dx), (y_ + 0.5 * dx), int(w_)) for x_, y_, w_ in zip(Xf[m].tolist(), Yf[m].tolist(), pl[m].tolist())]
        psum = sum(w_ for _, _, w_ in pw)
        pos = [(x_, y_) for x_, y_, w_ in pw if w_ > 0]
        knoten = (sum(p[0] for p in pos) / len(pos), sum(p[1] for p in pos) / len(pos)) if pos else None
        # Umlaufwindung von P um Ecken und Steiner-Punkt (r = 1,5 und 3) und Dichteloch
        p_um = {}
        s_loch = {}
        for tag, (cx, cy) in list(zip("ABC", geo["ecken"])) + [("J", geo["J"])]:
            for r_ in (1.5, 3.0):
                p_um[f"{tag}{r_}"] = round(umlauf_z(abtasten(gr, Pi, cx + r_ * torch.cos(th), cy + r_ * torch.sin(th))), 3)
            s_loch[tag] = torch.where(((Xf - cx) ** 2 + (Yf - cy) ** 2) < 4.0, Si, torch.full_like(Si, 1e9)).min().item() / e_b["S_0"]
        # Knotenklasse (Nachtrag 11:18, vor jedem .69-Lauf): zuerst die Umlaufwindung 2 von P (r = 3), sonst die Plaketten
        klasse = None
        if k["art"] == "dreier":
            ecke_w = [t_ for t_ in "ABC" if abs(p_um[f"{t_}3.0"] - 2.0) < 0.1]
            if geo["knoten_ecke"] is None and abs(p_um["J3.0"] - 2.0) < 0.1:
                klasse = "Steiner"
            elif len(ecke_w) == 1:
                klasse = f"Ecke {ecke_w[0]}"
            elif knoten is not None:
                dJ = math.dist(knoten, geo["J"])
                de = [math.dist(knoten, ec) for ec in geo["ecken"]]
                if geo["knoten_ecke"] is None and dJ < 1.5:
                    klasse = "Steiner (Plaketten)"
                elif min(de) < 1.5:
                    klasse = f"Ecke {'ABC'[de.index(min(de))]} (Plaketten)"
                else:
                    klasse = "anders"
        # Nachtrag 11:27 (nach dreier_y/neutral, vor dreier02/null): Windung der eigenen Komponente um jeden Wirbel und
        # Wirbelzaehlung je Komponente (Abschirmung durch Gegenwirbel im Kern?)
        wind_um = []
        for (a, xv, yv, wv) in k["wirbel"]:
            ew = {"a": a + 1, "w": wv}
            for r_ in (1.5, 3.0, 4.5, 6.0):
                ew[str(r_)] = round(umlauf_z(abtasten(gr, psi[i, a], xv + r_ * torch.cos(th), yv + r_ * torch.sin(th))), 3)
            wind_um.append(ew)
        innen_b = (Xf ** 2 + Yf ** 2) < (R_b - 3.0) ** 2
        wirbel_je = {}
        for a in akt:
            pla = plaketten(torch.angle(psi[i, a]))
            mm = (pla != 0) & innen_b
            wirbel_je[str(a + 1)] = [(round(x_ + 0.5 * dx, 2), round(y_ + 0.5 * dx, 2), int(w_)) for x_, y_, w_ in
                                     zip(Xf[mm].tolist(), Yf[mm].tolist(), pla[mm].tolist())][:30]
        # Kreis um alle Wirbel
        rk = geo["rho"] + 3.0
        xs_c, ys_c = rk * torch.cos(th), rk * torch.sin(th)
        p_um["gross"] = round(umlauf_z(abtasten(gr, Pi, xs_c, ys_c)), 3)
        ac = [abtasten(gr, psi[i, a], xs_c, ys_c) for a in range(3)]
        wechsel = {}
        for a, b2 in ((0, 1), (0, 2), (1, 2)):
            if a not in akt or b2 not in akt:
                continue
            z = (ac[a].conj() * ac[b2]) ** 2
            mz = z.real / (ac[a].abs() ** 2 * ac[b2].abs() ** 2).clamp(min=1e-300)
            zust = [v for v in torch.where(mz > 0.3, 1, torch.where(mz < -0.3, -1, 0)).tolist() if v != 0]
            wechsel[f"{a + 1}{b2 + 1}"] = sum(1 for j in range(len(zust)) if zust[j] != zust[j - 1]) if zust else None
        wind = {str(a + 1): umlauf_z(ac[a]) for a in akt}
        # Arme: Wirbel -> Knoten (Steiner-Punkt) bzw. Mitte (Paare); Querprofil der eigenen Komponente
        arme = []
        for (a, xv, yv, wv) in k["wirbel"]:
            zp = geo["J"]
            La = math.hypot(zp[0] - xv, zp[1] - yv)
            if La < 1.0:
                arme.append({"a": a + 1, "L": La})
                continue
            ux, uy = (zp[0] - xv) / La, (zp[1] - yv) / La
            eintr = {"a": a + 1, "L": La}
            for f_, tag in ((0.35, "0.35"), (0.5, "0.5"), (0.65, "0.65")):
                mx, my = xv + f_ * La * ux, yv + f_ * La * uy
                qx, qy = mx - uy * tq, my + ux * tq
                Sq = abtasten(gr, Si, qx, qy)
                naq = abtasten(gr, sai[a], qx, qy) / Sq.clamp(min=1e-300)
                eintr[tag] = {"n_rel_mitte": [(abtasten(gr, sai[b2], torch.tensor([mx], dtype=F64, device=DEV), torch.tensor([my], dtype=F64, device=DEV))
                                               / abtasten(gr, Si, torch.tensor([mx], dtype=F64, device=DEV), torch.tensor([my], dtype=F64, device=DEV))).item() for b2 in range(3)],
                              "S_mitte": Sq[16].item(), "S_min_quer": Sq.min().item(), "na_rel_min_quer": naq.min().item(),
                              "breite_na_unter_0.1": (naq < 0.1).sum().item() * 0.25, "breite_na_unter_0.2": (naq < 0.2).sum().item() * 0.25}
                if tag == "0.5":
                    eintr["quer_na_rel"] = [round(v, 4) for v in naq.tolist()]
                    eintr["quer_S"] = [round(v, 4) for v in Sq.tolist()]
            arme.append(eintr)
        kanten_mitte = []
        ec = geo["ecken"]
        if len(ec) == 3:
            for (p_, q_) in ((0, 1), (1, 2), (2, 0)):
                mx, my = 0.5 * (ec[p_][0] + ec[q_][0]), 0.5 * (ec[p_][1] + ec[q_][1])
                tx_, ty_ = torch.tensor([mx], dtype=F64, device=DEV), torch.tensor([my], dtype=F64, device=DEV)
                Sm = abtasten(gr, Si, tx_, ty_).item()
                kanten_mitte.append({"kante": "ABC"[p_] + "ABC"[q_], "S": Sm,
                                     "n_rel": [abtasten(gr, sai[b2], tx_, ty_).item() / max(Sm, 1e-300) for b2 in range(3)]})
        na_ = len(akt)
        Dl = gk[i, 0] * ((na_ - 1) / (2.0 * na_) * Si * Si - Cl[i])
        netz = (Xf ** 2 + Yf ** 2) < (geo["rho"] + 5.0) ** 2
        rho_ = 2.0 * math.sqrt(max(w2[i, 0].item(), 0.0)) * Si
        sb = torch.fft.ifft2(torch.fft.fft2(Si) * gr.blur).real
        kz = klumpenzahl(gr, Si.unsqueeze(0), rho_.unsqueeze(0), (0.5 * sb.max()).view(1), [0.03 * Q])[0]
        dE1000 = abs(verlauf[-1]["E"][i] - verlauf[-6]["E"][i]) if len(verlauf) >= 6 else None
        om = [math.sqrt(max(w2[i, a].item(), 0.0)) for a in range(3)]
        Qa = [2.0 * om[a] * Na[i, a].item() for a in range(3)]
        aus.append({"name": k["name"], "art": k["art"], "g": k["g"], "c": k["c"], "saat": k["saat"], "perm": k["perm"],
                    "modus": k["modus"], "ziel": list(k["ziel"]) if k["ziel"] is not None else None,
                    "geo": {kk: vv for kk, vv in geo.items()}, "b": b_von(k), "R_halb": R_b, "S0_ball": e_b["S_0"],
                    "omega_ball": e_b["omega2"], "E": en["E"][i].item(), "K": en["K"][i].item(), "G": en["G"][i].item(),
                    "V": en["V"][i].item(), "C": en["C"][i].item(), "Q4": en["Q4"][i].item(), "omega": om, "Q_a": Qa,
                    "N_a": Na[i].tolist(), "dE1000": dE1000, "konvergiert": dE1000 is not None and dE1000 < Y_KONV,
                    "schub": schub[i].item(), "res_frei": res_frei[i].item(), "P_windungen": pw[:40], "P_summe": psum,
                    "knoten": knoten, "knoten_klasse": klasse, "kreis_r": rk, "kreis_wechsel": wechsel, "kreis_windung": wind,
                    "arme": arme, "kanten_mitte": kanten_mitte, "defizit_gesamt": (Dl.sum() * dA).item(),
                    "defizit_netz": (Dl * netz).sum().item() * dA, "klumpen": kz,
                    "S_max": Si.max().item(), "kl_aus": kl_aus, "P_umlauf": p_um, "S_loch": s_loch, "windung_um_wirbel": wind_um,
                    "wirbel_je_komponente": wirbel_je})
        bilder.append((sai.float().cpu(), Si.float().cpu(), Dl.float().cpu(), torch.angle(Pi).float().cpu(), pw))
    zeilen = [f"Y-1 {stamm}{' RAUCH' if args.rauch else ''}. Start {start}, Ende {jetzt()}, {geraet_name()}, torch {torch.__version__}",
              f"Q = {Q}, L = {L}, dx = {dx}, n = {n}, tau = {tau}, Iterationen {it_end} von {n_it} (Abbruch {abbruch}), "
              f"Schwerpunktbindung {com}; radial {t_rad:.1f} s, Schleife {t_iter:.1f} s",
              "Ball radial: " + "; ".join(f"b {b:.4f}: omega {e['omega2']:.5f}, S_0 {e['S_0']:.4f}, R_halb {e['R_halb']:.3f}, Residuum {e['residuum']:.1e}" for b, e in zip(bs, erg_b)),
              "", "Lauf | E | dE1000 | omega | Q_a/Q | P-Windungen (Summe) | Knoten -> Klasse | P-Umlauf r=1,5 um A/B/C/J, gross | S_min/S0 in r<2 um A/B/C/J | Kreis: Wechsel 12/13/23, Windungen | Arm 0.5: n_a/S min quer, Breite<0.1, S_min/S0 | Klumpen | Schub | res_frei"]
    for a in aus:
        qsum = sum(a["Q_a"])
        armtxt = []
        for ar_ in a["arme"]:
            if "0.5" in ar_:
                armtxt.append(f"{ar_['a']}: {ar_['0.5']['na_rel_min_quer']:.3f}/{ar_['0.5']['breite_na_unter_0.1']:.2f}/{ar_['0.5']['S_min_quer'] / a['S0_ball']:.2f}")
        zeilen.append(" | ".join([a["name"], f"{a['E']:.5f}", fz(a["dE1000"], "{:.1e}"), "/".join(f"{o:.5f}" for o in a["omega"]),
                                  "/".join(f"{q / max(qsum, 1e-300):.4f}" for q in a["Q_a"]), f"{a['P_summe']}",
                                  (f"({a['knoten'][0]:.2f}, {a['knoten'][1]:.2f}) -> {a['knoten_klasse']}" if a["knoten"] else "-"),
                                  "/".join(f"{a['P_umlauf'].get(t_ + '1.5', float('nan')):.1f}" for t_ in "ABCJ") + f", {a['P_umlauf']['gross']:.1f}",
                                  "/".join(f"{a['S_loch'][t_]:.2f}" for t_ in a["S_loch"]),
                                  "/".join(str(v) for v in a["kreis_wechsel"].values()) + ", " + "/".join(f"{v:.2f}" for v in a["kreis_windung"].values()),
                                  "; ".join(armtxt), str(a["klumpen"]), f"{a['schub']:.3f}", f"{a['res_frei']:.1e}"]))
        zeilen.append("    Windung eigene Komponente um Wirbel (r 1,5/3/4,5/6): "
                      + "; ".join(f"{w_['a']}: {w_['1.5']:.0f}/{w_['3.0']:.0f}/{w_['4.5']:.0f}/{w_['6.0']:.0f}" for w_ in a["windung_um_wirbel"])
                      + " | Wirbel je Komponente (x, y, w): "
                      + "; ".join(f"{c_}: " + " ".join(f"({x_:.1f},{y_:.1f},{w_:+d})" for x_, y_, w_ in v_) for c_, v_ in a["wirbel_je_komponente"].items()))
    text = "\n".join(zeilen) + "\n"
    schreiben(args.out, stamm, {"start": start, "ende": jetzt(), "Q": Q, "L": L, "dx": dx, "tau": tau, "n_it": n_it, "it_end": it_end,
                                "abbruch": abbruch, "com": com, "t_iter": t_iter, "konf": aus, "verlauf": verlauf}, text)
    y_bilder(args.out, stamm, konf, aus, bilder, gr)
    return aus


def y_bilder(out, stamm, konf, aus, bilder, gr):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:
        print(f"keine Bilder: {exc!r}", flush=True)
        return
    import numpy as np
    L, dx, n = gr.L, gr.dx, gr.n
    farben = ("red", "lime", "deepskyblue")
    for i, (k, a) in enumerate(zip(konf, aus)):
        sai, Si, Dl, argP, pw = bilder[i]
        halb = min(a["geo"]["rho"] + 7.0, L)
        j0, j1 = int(round((L - halb) / dx)), min(int(round((L + halb) / dx)) + 1, n)
        ext = (-L + dx * j0, -L + dx * (j1 - 1), -L + dx * j0, -L + dx * (j1 - 1))
        S = Si.numpy()
        smax = float(S.max())
        rgb = np.clip(1.5 * sai.numpy().transpose(1, 2, 0) / np.maximum(S, 1e-12)[..., None], 0.0, 1.0)
        rgb[S < 0.05 * smax] = 0.0
        fig, ax = plt.subplots(1, 4, figsize=(16, 4.4))
        ax[0].imshow(rgb[j0:j1, j0:j1], origin="lower", extent=ext)
        ax[0].set_title("RGB = 1,5 (n_1, n_2, n_3)/S (grau = gleich gemischt)", fontsize=8)
        dmax = float(Dl[j0:j1, j0:j1].max())
        im = ax[1].imshow(Dl.numpy()[j0:j1, j0:j1], origin="lower", extent=ext, cmap="magma", vmin=0.0, vmax=max(dmax, 1e-9))
        ax[1].set_title("Kopplungsdefizit g (S^2 (N-1)/(2N) - C)", fontsize=8)
        fig.colorbar(im, ax=ax[1], fraction=0.046)
        ax[2].imshow(np.where(S > 0.05 * smax, argP.numpy(), np.nan)[j0:j1, j0:j1], origin="lower", extent=ext, cmap="hsv", vmin=-math.pi, vmax=math.pi)
        ax[2].set_title("arg P, P = sum psi_a^2 (Punkte: Windungen +1 weiss, -1 schwarz)", fontsize=8)
        for x_, y_, w_ in pw:
            if abs(x_) <= halb and abs(y_) <= halb:
                ax[2].plot([x_], [y_], "o", ms=4, color="white" if w_ > 0 else "black", mec="k")
        ax[3].imshow(rgb, origin="lower", extent=(-L, L - dx, -L, L - dx))
        ax[3].set_title("ganzer Ball (RGB)", fontsize=8)
        for axx in ax[:3]:
            for (c_, xv, yv, wv) in k["wirbel"]:
                axx.plot([xv], [yv], marker="o" if wv > 0 else "s", ms=6, mfc="none", mec=farben[c_], mew=1.5)
            J = a["geo"]["J"]
            axx.plot([J[0]], [J[1]], "x", color="white", ms=7, mew=1.5)
            axx.tick_params(labelsize=6)
        fig.suptitle(f"Y-1 {stamm}: {a['name']}, E = {a['E']:.4f}, Knoten {a['knoten_klasse']}", fontsize=10)
        fig.tight_layout()
        fig.savefig(os.path.join(out, f"{stamm}_{a['name']}.png"), dpi=65)
        plt.close(fig)


def y_karte(karte, args):
    if karte == "k1":
        konf = [k_zwei("k1", g, d) for g in (0.5, 0.2) for d in (5.0, 6.5, 8.0, 9.5)]
        return y_statik(args, "k1", konf, Q=700.0, L=38.4, rmax=RMAX, tau=0.3, n_it=6000, com=False)
    if karte == "meson":
        konf = [k_zwei("meson", g, d) for g in (0.5, 0.2) for d in (6.0, 9.0, 12.0, 15.0)] + [k_zwei("paar3", 0.5, d) for d in (6.0, 9.0, 12.0, 15.0)]
        return y_statik(args, "meson", konf)
    if karte == "dreier_neutral":
        return y_statik(args, "dreier_neutral", [k_dreier(0.5, t, s, "neutral") for t, s in Y_GEOS])
    if karte == "dreier_y":
        return y_statik(args, "dreier_y", [k_dreier(0.5, t, s, "Y") for t, s in Y_GEOS])
    if karte == "dreier_kette":
        konf = [k_dreier(0.5, t, s, "kette") for t, s in Y_GEOS if t in ("gleich", "gestreckt")]
        konf += [k_dreier(0.5, "gestreckt", 9.0, "Y", perm=(2, 0, 1)), k_dreier(0.5, "gestreckt", 9.0, "Y", perm=(1, 0, 2))]
        g13 = geo_dreier("gestreckt", 13.0)
        konf += [k_dreier(0.5, "gestreckt", 13.0, "Y", ziel=g13["J"], zusatz="_zielJ")]
        return y_statik(args, "dreier_kette", konf)
    if karte == "dreier02":
        return y_statik(args, "dreier02", [k_dreier(0.2, t, s, "Y") for t, s in Y_GEOS])
    if karte == "dreier02n":
        return y_statik(args, "dreier02n", [k_dreier(0.2, t, s, "neutral") for t, s in Y_GEOS])
    if karte == "null":
        return y_statik(args, "null", [k_dreier(0.0, t, s, "neutral", modus="einzeln") for t, s in Y_GEOS])
    if karte == "dreierc":        # zweiter Arm, ANDERE THEORIE: + c sum_a |psi_a|^4, c = 0,4 > |g|/2 (Nachtrag PLAN 11)
        return y_statik(args, "dreierc", [k_dreier(0.5, t, s, "Y", c=0.4, zusatz="_c0.4") for t, s in Y_GEOS])
    if karte == "mesonc":
        konf = [dict(k_zwei("meson", 0.5, d), c=0.4, name=f"meson_g+0.5_d{d:g}_c0.4") for d in (6.0, 9.0, 12.0, 15.0)]
        konf += [k_dreier(0.5, t, s, "neutral", c=0.4, zusatz="_c0.4") for t, s in (("gleich", 9.0), ("gleich", 15.0), ("kollinear", 8.0), ("gestreckt", 13.0))]
        return y_statik(args, "mesonc", konf)
    if karte == "dreier_k4":      # Nachtrag PLAN 12: Klammerring bis r = 4 (Gegenwirbel im Kern erschwert)
        geos = (("gleich", 9.0), ("gleich", 12.0), ("gleich", 15.0), ("gestreckt", 13.0), ("stumpf", 9.0),
                ("kollinear", 8.5), ("kollinear", 10.0), ("kollinear", 12.0))
        konf = [k_dreier(0.5, t, s, "Y", zusatz="_k4") for t, s in geos]
        konf += [dict(k_zwei("meson", 0.5, d), name=f"meson_g+0.5_d{d:g}_k4") for d in (9.0, 12.0, 15.0, 18.0)]
        return y_statik(args, "dreier_k4", konf, kl_aus=4.0)
    if karte == "fein":
        wahl = (args.laeufe or "Y").split(",")
        konf = [k_dreier(0.5, "gleich", 12.0, wahl[0]), k_dreier(0.5, "kollinear", 8.0, "Y"), k_zwei("meson", 0.5, 12.0)]
        return y_statik(args, "fein", konf, dx=0.2)
    raise ValueError(karte)


def linfit(xs, ys):
    X_ = torch.tensor(xs, dtype=F64)
    Y_ = torch.tensor(ys, dtype=F64)
    A = torch.stack([X_, torch.ones_like(X_)], 1)
    sol = torch.linalg.lstsq(A, Y_.unsqueeze(1)).solution[:, 0]
    r = Y_ - A @ sol
    dof = len(xs) - 2
    se = None
    if dof > 0:
        s2 = (r * r).sum() / dof
        se = math.sqrt((s2 * torch.linalg.inv(A.T @ A))[0, 0].item())
    return {"steigung": sol[0].item(), "achse": sol[1].item(), "se": se, "rms": math.sqrt((r * r).mean().item()),
            "maxrest": r.abs().max().item(), "rest": [round(v, 5) for v in r.tolist()], "n": len(xs)}


def test_auswertung(args):
    """Liest alle *_ergebnis.json in --out und wertet nach PLAN 5 bis 7 aus (nur Rechnen auf gespeicherten Zahlen)."""
    alle = {}
    for f in sorted(os.listdir(args.out)):
        if not f.endswith("_ergebnis.json") or f.startswith("auswertung"):
            continue
        with open(os.path.join(args.out, f)) as fh:
            d = json.load(fh)
        if "konf" in d and isinstance(d["konf"], list) and d["konf"] and "art" in d["konf"][0]:
            alle[f[:-len("_ergebnis.json")]] = d
    z = [f"Y-1 Auswertung {jetzt()}; Stapel: {', '.join(sorted(alle))}"]
    erg = {"stapel": sorted(alle)}
    # K1
    if "k1" in alle:
        z.append("\nK1 (N = 2 wie ROT-1 paar):")
        k1 = []
        for a in alle["k1"]["konf"]:
            ref = ROT1_PAAR_E.get((a["g"], a["geo"]["s"]))
            rel = (a["E"] - ref) / ref if ref else None
            k1.append({"name": a["name"], "E": a["E"], "E_ROT1": ref, "rel": rel})
            z.append(f"  {a['name']}: E {a['E']:.10f} gegen ROT-1 {ref:.10f}, relativ {rel:.2e}")
        erg["K1"] = k1
    # Meson und paar3
    tau2 = {}
    for st_, cc, kl_ in (("meson", 0.0, 2.0), ("mesonc", 0.4, 2.0), ("dreier_k4", 0.0, 4.0)):
        if st_ not in alle:
            continue
        z.append(f"\nMeson (psi_1-Wirbel + Gegenwirbel) und paar3, Stapel {st_} (c = {cc}):")
        for art in ("meson", "paar3"):
            for g in (0.5, 0.2):
                sel = sorted([a for a in alle[st_]["konf"] if a["art"] == art and a["g"] == g and a["c"] == cc and a.get("kl_aus", 2.0) == kl_], key=lambda a: a["geo"]["s"])
                if len(sel) < 2:
                    continue
                tk = (f"{g}" if cc == 0.0 else f"{g}_c{cc}") + ("" if kl_ == 2.0 else "_k4")
                ds = [a["geo"]["s"] for a in sel]
                Es = [a["E"] for a in sel]
                f_all = linfit(ds, Es)
                f_gr = linfit(ds[1:], Es[1:]) if len(ds) >= 3 else None
                erg[f"{art}_{tk}"] = {"d": ds, "E": Es, "fit": f_all, "fit_ab_9": f_gr,
                                      "konvergiert": [a["konvergiert"] for a in sel], "kreis": [a["kreis_wechsel"] for a in sel]}
                z.append(f"  {art} g {g}: E(d) = " + ", ".join(f"{d_:g}: {e_:.4f}" for d_, e_ in zip(ds, Es))
                         + f"; Steigung {f_all['steigung']:.4f} +- {fz(f_all['se'], '{:.4f}')} (rms {f_all['rms']:.3f})"
                         + (f"; ab d = 9: {f_gr['steigung']:.4f} +- {fz(f_gr['se'], '{:.4f}')}" if f_gr else ""))
                if art == "meson":
                    tau2[tk] = f_all["steigung"]
    if "0.5" in tau2 and "paar3_0.5" in erg:
        z.append(f"  paar3/tau_2(0,5) = {erg['paar3_0.5']['fit']['steigung'] / tau2['0.5']:.3f} (Hand: 0,866)")
    if "0.5" in tau2 and "0.2" in tau2:
        z.append(f"  tau_2(0,2)/tau_2(0,5) = {tau2['0.2'] / tau2['0.5']:.3f}")
    erg["tau2"] = tau2
    # Dreier: beste Saat je (g, Geometrie)
    dreier = [dict(a, stapel=s) for s, d in alle.items() if s != "fein" for a in d["konf"]
              if a["art"] == "dreier" and a["perm"] == [0, 1, 2] and a["ziel"] == [0.0, 0.0] and not a["name"].endswith("_zielJ")]
    for g, cc, kl_ in ((0.5, 0.0, 2.0), (0.2, 0.0, 2.0), (0.0, 0.0, 2.0), (0.5, 0.4, 2.0), (0.5, 0.0, 4.0)):
        tk = (f"{g}" if cc == 0.0 else f"{g}_c{cc}") + ("" if kl_ == 2.0 else "_k4")
        gruppe = {}
        for a in dreier:
            if a["g"] == g and a["c"] == cc and a.get("kl_aus", 2.0) == kl_:
                gruppe.setdefault((a["geo"]["typ"], a["geo"]["s"]), []).append(a)
        if not gruppe:
            continue
        z.append(f"\nDreier g = {g}, c = {cc}: je Geometrie E je Saat (Konvergenz), beste Saat")
        beste = []
        for key in sorted(gruppe, key=lambda k_: (["gleich", "gestreckt", "stumpf", "kollinear"].index(k_[0]), k_[1])):
            kand = gruppe[key]
            konv = [a for a in kand if a["konvergiert"]]
            b_ = min(konv or kand, key=lambda a: a["E"])
            beste.append(b_)
            z.append(f"  {key[0]} {key[1]:g}: L_St {b_['geo']['L_St']:.3f}, P/2 {b_['geo']['P2']:.3f} | "
                     + "; ".join(f"{a['saat']}: {a['E']:.4f} ({fz(a['dE1000'], '{:.0e}')}, Knoten {a['knoten_klasse']}, Kreis {'/'.join(str(v) for v in a['kreis_wechsel'].values())})" for a in kand)
                     + f" | beste {b_['saat']}")
        Ls = [a["geo"]["L_St"] for a in beste]
        Ps = [a["geo"]["P2"] for a in beste]
        Es = [a["E"] for a in beste]
        fY, fD = linfit(Ls, Es), linfit(Ps, Es)
        eintr = {"beste": [{"name": a["name"], "saat": a["saat"], "E": a["E"], "L_St": a["geo"]["L_St"], "P2": a["geo"]["P2"],
                            "knoten_klasse": a["knoten_klasse"], "kreis_wechsel": a["kreis_wechsel"], "klumpen": a["klumpen"],
                            "dE1000": a["dE1000"]} for a in beste], "fit_Y": fY, "fit_Delta": fD}
        z.append(f"  Fit Y: E = {fY['achse']:.3f} + {fY['steigung']:.4f} L_St (+- {fz(fY['se'], '{:.4f}')}), rms {fY['rms']:.4f}, max {fY['maxrest']:.4f}")
        z.append(f"  Fit Dreieck: E = {fD['achse']:.3f} + {fD['steigung']:.4f} P/2 (+- {fz(fD['se'], '{:.4f}')}), rms {fD['rms']:.4f}, max {fD['maxrest']:.4f}")
        z.append(f"  Restfehler je Geometrie Y / Dreieck: " + ", ".join(f"{a['geo']['typ'][:4]}{a['geo']['s']:g} {ry:+.3f}/{rd:+.3f}" for a, ry, rd in zip(beste, fY["rest"], fD["rest"])))
        # Steigungsverhaeltnis
        def reihe(typ, smin):
            sel = sorted([a for a in beste if a["geo"]["typ"] == typ and a["geo"]["s"] >= smin], key=lambda a: a["geo"]["s"])
            return linfit([a["geo"]["s"] for a in sel], [a["E"] for a in sel]) if len(sel) >= 2 else None
        fe, fk = reihe("gleich", 9.0), reihe("kollinear", 6.5)
        fe_all, fk_all = reihe("gleich", 0.0), reihe("kollinear", 0.0)
        if fe and fk and abs(fk["steigung"]) > 1e-12:
            R = fe["steigung"] / fk["steigung"]
            dR = abs(R) * math.sqrt(((fe["se"] or 0.0) / fe["steigung"]) ** 2 + ((fk["se"] or 0.0) / fk["steigung"]) ** 2) if fe["steigung"] else None
            R_all = fe_all["steigung"] / fk_all["steigung"] if fe_all and fk_all else None
            eintr.update({"s_gleich": fe, "s_kollinear": fk, "R": R, "dR": dR, "R_alle_groessen": R_all})
            z.append(f"  Steigungen: gleichseitig a = 9..15 {fe['steigung']:.4f} +- {fz(fe['se'], '{:.4f}')}; kollinear l = 6,5..10 {fk['steigung']:.4f} +- {fz(fk['se'], '{:.4f}')}")
            z.append(f"  R = {R:.4f} +- {fz(dR, '{:.4f}')} (Y 0,866, Dreieck 0,750, Grenze 0,808); alle Groessen: {fz(R_all, '{:.4f}')}")
        # Knoten und Zerfall
        soll = {"gleich": "Steiner", "gestreckt": "Steiner", "stumpf": "Ecke B", "kollinear": "Ecke B"}
        treffer = sum(1 for a in beste if a["knoten_klasse"] == soll[a["geo"]["typ"]])
        zerfall = sum(1 for a in beste if (max([v for v in a["kreis_wechsel"].values() if v is not None] or [0]) >= 2) or a["klumpen"] >= 2)
        nkonv = sum(1 for a in beste if not a["konvergiert"])
        eintr.update({"knoten_treffer": treffer, "zerfall": zerfall, "nicht_konvergiert": nkonv, "n": len(beste)})
        mit_w = [a for a in beste if "windung_um_wirbel" in a]
        if mit_w:
            abg = [a["name"] for a in mit_w if any(abs(w_["4.5"]) < 0.5 for w_ in a["windung_um_wirbel"])]
            eintr["abgeschirmt"] = abg
            z.append(f"  Abschirmung (eigene Windung bei r = 4,5 gleich 0 an mindestens einem Wirbel): {len(abg)} von {len(mit_w)}: {', '.join(abg)}")
        z.append(f"  Knoten wie Y-Soll: {treffer} von {len(beste)}; Zerfallszeichen (Kreiswechsel >= 2 oder >= 2 Klumpen): {zerfall}; nicht konvergiert: {nkonv}")
        if g != 0.0 and "R" in eintr:
            y_ok = eintr["R"] >= 0.808 and fY["rms"] < fD["rms"] and treffer >= 2 * len(beste) / 3
            d_ok = eintr["R"] < 0.808 and fD["rms"] < 0.77 * fY["rms"]
            spanne = max(Es) - min(Es)
            if nkonv > len(beste) / 4:
                urteil = "nicht auswertbar"
            elif zerfall >= len(beste) / 2:
                urteil = "Zerfall"
            elif y_ok:
                urteil = "Y"
            elif d_ok:
                urteil = "Dreieck"
            else:
                urteil = "weder noch"
            if fY["rms"] > 0.1 * spanne and fD["rms"] > 0.1 * spanne and urteil in ("Y", "Dreieck"):
                urteil = "weder noch (beide Restfehler > 10 % der Spanne)"
            eintr["urteil"] = urteil
            z.append(f"  Urteil nach PLAN 7: {urteil}")
        if tk in tau2:
            z.append(f"  Vorhersage mit tau_2 = {tau2[tk]:.4f}: Y-Steigung = tau_2; gleichseitig 1,732 tau_2 = {SQ3 * tau2[tk]:.4f}, Dreieck 1,5 tau_2 = {1.5 * tau2[tk]:.4f}; kollinear 2 tau_2 = {2 * tau2[tk]:.4f}")
        # Kette gegen Y
        kv = []
        for key, kand in gruppe.items():
            ey = [a for a in kand if a["saat"] == "Y"]
            ek = [a for a in kand if a["saat"] == "kette"]
            if ey and ek:
                kv.append({"geo": key, "E_kette_minus_E_Y": ek[0]["E"] - ey[0]["E"], "L_kette_minus_L_St": ek[0]["geo"]["kette"] - ey[0]["geo"]["L_St"],
                           "knoten_kette": ek[0]["knoten_klasse"]})
        if kv:
            eintr["kette_gegen_Y"] = kv
            z.append("  Kette - Y: " + "; ".join(f"{v['geo'][0]} {v['geo'][1]:g}: dE {v['E_kette_minus_E_Y']:+.4f} bei dL {v['L_kette_minus_L_St']:+.3f} (Knoten Kette-Saat: {v['knoten_kette']})" for v in kv))
        erg[f"dreier_{tk}"] = eintr
    # S_3 und Schwerpunktziel
    ref = {a["name"]: a for s, d in alle.items() if s != "fein" for a in d["konf"]}
    z.append("\nS_3 und Schwerpunktziel:")
    for a in ref.values():
        if a["art"] == "dreier" and a["perm"] != [0, 1, 2]:
            r0 = ref.get(f"g{a['g']:+.1f}_{a['geo']['typ']}{a['geo']['s']:g}_{a['saat']}")
            if r0:
                z.append(f"  {a['name']}: E {a['E']:.10f} gegen {r0['E']:.10f}, relativ {(a['E'] - r0['E']) / r0['E']:.2e}")
                erg.setdefault("S3", []).append({"name": a["name"], "rel": (a["E"] - r0["E"]) / r0["E"]})
        if a["name"].endswith("_zielJ"):
            r0 = ref.get(a["name"][:-len("_zielJ")])
            if r0:
                z.append(f"  {a['name']}: E {a['E']:.5f} gegen Ziel Ursprung {r0['E']:.5f}, Differenz {a['E'] - r0['E']:+.5f}")
                erg["zielJ"] = {"dE": a["E"] - r0["E"]}
    # fein gegen grob
    if "fein" in alle:
        z.append("\nfein (dx 0,2) gegen grob (dx 0,3):")
        fe_ = {a["name"]: a for a in alle["fein"]["konf"]}
        for nm, a in fe_.items():
            r0 = ref.get(nm) if ref.get(nm) is not a else None
            gro = [b for s, d in alle.items() if s != "fein" for b in d["konf"] if b["name"] == nm]
            if gro:
                z.append(f"  {nm}: fein {a['E']:.5f}, grob {gro[0]['E']:.5f}, Differenz {a['E'] - gro[0]['E']:+.5f}")
        g12 = [b for b in alle["fein"]["konf"] if b["geo"]["typ"] == "gleich"]
        k8 = [b for b in alle["fein"]["konf"] if b["geo"]["typ"] == "kollinear"]
        if g12 and k8:
            df = g12[0]["E"] - k8[0]["E"]
            gg = [b for s, d in alle.items() if s != "fein" for b in d["konf"] if b["name"] == g12[0]["name"]]
            kk = [b for s, d in alle.items() if s != "fein" for b in d["konf"] if b["name"] == k8[0]["name"]]
            if gg and kk:
                dg = gg[0]["E"] - kk[0]["E"]
                z.append(f"  E(gleich 12) - E(kollinear 8): fein {df:.4f}, grob {dg:.4f}, relativ {(df - dg) / dg:+.3f}")
                erg["fein"] = {"diff_fein": df, "diff_grob": dg}
    text = "\n".join(z) + "\n"
    schreiben(args.out, "auswertung", erg, text)
    # Bild: E gegen L_St und P/2
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        gs = [g for g in ("0.5", "0.2", "0.0", "0.5_c0.4", "0.5_k4") if f"dreier_{g}" in erg]
        fig, ax = plt.subplots(len(gs), 2, figsize=(10, 4 * len(gs)), squeeze=False)
        mk = {"gleich": "o", "gestreckt": "^", "stumpf": "s", "kollinear": "D"}
        for r_, g in enumerate(gs):
            e_ = erg[f"dreier_{g}"]
            for c_, (key, fit, lab) in enumerate((("L_St", e_["fit_Y"], "L_St (Y)"), ("P2", e_["fit_Delta"], "P/2 (Dreieck)"))):
                a_ = ax[r_][c_]
                for b_ in e_["beste"]:
                    typ = next(t for t in mk if b_["name"].split("_")[1].startswith(t))
                    a_.plot(b_[key], b_["E"], mk[typ], color="C" + str(list(mk).index(typ)), label=typ)
                xs = [b_[key] for b_ in e_["beste"]]
                a_.plot([min(xs), max(xs)], [fit["achse"] + fit["steigung"] * min(xs), fit["achse"] + fit["steigung"] * max(xs)], "k--", lw=1)
                h, l = a_.get_legend_handles_labels()
                uniq = dict(zip(l, h))
                a_.legend(uniq.values(), uniq.keys(), fontsize=7)
                a_.set_xlabel(lab)
                a_.set_ylabel("E")
                a_.set_title(f"g = {g}: Steigung {fit['steigung']:.4f}, rms {fit['rms']:.4f}", fontsize=9)
        fig.tight_layout()
        fig.savefig(os.path.join(args.out, "auswertung_E_gegen_L.png"), dpi=70)
        plt.close(fig)
    except Exception as exc:
        print(f"kein Auswertungsbild: {exc!r}", flush=True)


KARTEN = {"radial": test_radial, "dyn0": lambda a: test_dyn(a, "dyn0"), "dyng": lambda a: test_dyn(a, "dyng"), "paar": test_paar,
          "regge": test_regge, "band": test_band, "bandstat": test_bandstat, "bandstat2": test_bandstat2, "band2": test_band2, "band3": test_band3,
          "paardyn": test_paardyn, "nach": test_nach}
Y_KARTEN = ("k1", "meson", "dreier_neutral", "dreier_y", "dreier_kette", "dreier02", "dreier02n", "null", "fein", "dreierc", "mesonc", "dreier_k4")
for _k in Y_KARTEN:
    KARTEN[_k] = (lambda kk: (lambda a: y_karte(kk, a)))(_k)
KARTEN["auswertung"] = test_auswertung


def main():
    global DEV
    ap = argparse.ArgumentParser()
    ap.add_argument("karte", choices=list(KARTEN) + ["alle"])
    ap.add_argument("--rauch", action="store_true")
    ap.add_argument("--stufe", default="grob", choices=list(STUFEN))
    ap.add_argument("--laeufe", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--geraet", default="cuda", choices=("cuda", "cpu"))
    ap.add_argument("--budget", type=float, default=480.0)
    args = ap.parse_args()
    if args.geraet == "cpu" and not args.rauch and args.karte != "auswertung":
        raise SystemExit("--geraet cpu nur mit --rauch (lokaler Rauchtest) oder fuer auswertung")
    DEV = torch.device(args.geraet)
    if args.geraet == "cuda" and not torch.cuda.is_available():
        raise SystemExit("CUDA nicht verfuegbar")
    torch.backends.cuda.matmul.allow_tf32 = False
    if args.out is None:
        args.out = "rauchtest" if args.rauch else "ausgabe"
    os.makedirs(args.out, exist_ok=True)
    print(f"start {jetzt()} karte {args.karte} geraet {geraet_name()}", flush=True)
    karten = list(KARTEN) if args.karte == "alle" else [args.karte]
    if args.karte == "alle" and not args.rauch:
        raise SystemExit("alle nur mit --rauch")
    rc = 0
    for k in karten:
        t0 = time.perf_counter()
        try:
            KARTEN[k](args)
        except Exception:
            traceback.print_exc()
            rc = 1
        print(f"karte {k} fertig nach {time.perf_counter() - t0:.1f} s", flush=True)
    print(f"ende {jetzt()} rc {rc}", flush=True)
    raise SystemExit(rc)


if __name__ == "__main__":
    main()
