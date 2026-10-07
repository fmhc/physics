#!/usr/bin/env python3
# QBALL-DREIPOL-2 (Runde 42): Ist das einfarbige Q-Ball-Dreieck stabil (Teil A, 2D), gibt es es in 3D (Teil B),
# bleibt ein schiefer Dreier in echter Zeit beisammen (Teil C, 2D)?
# Modell und Verfahren kopiert aus QBALL-DREIPOL-1 (code/dreipol.py, eingefroren 20261004-174224; Kopie
# dreipol-vorlage-qd1.py), portiert auf torch/CUDA (float64, complex128) und auf d = 2 oder 3 Raumdimensionen
# verallgemeinert. Kein CPU-Fallback: ohne CUDA bricht das Skript ab. Der radiale 1D-Bezug (tridiagonal) und die
# Zufallszahlen laufen wie in DREIPOL-1 auf der CPU (numpy/scipy), alles auf dem Gitter auf der GPU.
#   L = sum_a |d_t phi_a|^2 - |grad phi_a|^2 - V,  V = U(S) + g4 sum_a |phi_a|^4,  S = sum_a |phi_a|^2,
#   U(S) = S - S^2 + BETA S^3,  BETA = 1/2.
# Energie E = int [sum_a |pi_a|^2 + |grad phi_a|^2 + V];  Ladung Q_a = 2 int Im(conj(phi_a) pi_a).
# Feste Ladungen: E_Q[psi] = W[psi] + sum_a Q_a^2/(2 Lam_a), Lam_a = 2 int |psi_a|^2, om_a = Q_a/Lam_a.
import sys, os, json, time, math, argparse, resource
import numpy as np
import scipy
from scipy.linalg import solve_banded
import torch

BETA = 0.5
SQ3 = math.sqrt(3.0)
DEV = None
WINKEL = [0.5 * math.pi + 2.0 * math.pi * k / 3.0 for k in range(3)]   # Ecken 90, 210, 330 Grad wie DREIPOL-1


def geraet():
    global DEV
    if not torch.cuda.is_available():
        raise SystemExit("CUDA nicht verfuegbar: Abbruch (kein CPU-Fallback)")
    DEV = torch.device("cuda")
    return dict(name=torch.cuda.get_device_name(0), torch=torch.__version__, cuda=torch.version.cuda,
                visible=os.environ.get("CUDA_VISIBLE_DEVICES"), numpy=np.__version__, scipy=scipy.__version__,
                python=sys.version.split()[0])


def U0(S):
    return S - S * S + BETA * S ** 3


def U0p(S):
    return 1.0 - 2.0 * S + 3.0 * BETA * S * S


def Ug(S, g):
    return S - (1.0 - g) * S * S + BETA * S ** 3


def Ugp(S, g):
    return 1.0 - 2.0 * (1.0 - g) * S + 3.0 * BETA * S * S


def jetzt():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def schreibe(pfad, obj):
    tmp = pfad + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(obj, fh)
    os.replace(tmp, pfad)


def maxrss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def gpu_mb():
    return torch.cuda.max_memory_allocated() / 2 ** 20


# ------------------------------------------------------------------ radialer Bezug (eine Komponente, Kopplung g, d = 2 oder 3)
class Radial:
    def __init__(self, d=2, dr=0.01, rmax=60.0):
        M = int(round(rmax / dr))
        self.d, self.M, self.dr, self.rmax = d, M, dr, rmax
        j = np.arange(M)
        self.r = (j + 0.5) * dr
        self.rp = (j + 1.0) * dr
        self.rm = j * dr
        fl = (lambda r: 2.0 * np.pi * r) if d == 2 else (lambda r: 4.0 * np.pi * r * r)
        self.w = fl(self.r) * dr
        self.Ap = fl(self.rp)
        self.Am = fl(self.rm)
        self.cp = self.Ap / (self.w * dr)
        self.cm = self.Am / (self.w * dr)

    def lap(self, f):
        fp = np.r_[f[1:], 0.0]
        fm = np.r_[0.0, f[:-1]]
        return self.cp * (fp - f) - self.cm * (f - fm)

    def energie(self, f, Q, g):
        fp = np.r_[f[1:], 0.0]
        Eg = float(np.sum(self.Ap * (fp - f) ** 2)) / self.dr
        Ep = float(np.sum(self.w * Ug(f * f, g)))
        Lam = 2.0 * float(np.sum(self.w * f * f))
        return Eg + Ep + Q * Q / (2.0 * Lam), Q / Lam, Lam

    def start(self, Q, A=1.0, om=0.8):
        if self.d == 2:
            R0 = math.sqrt(Q / (2.0 * math.pi * om * A * A))
        else:
            R0 = (3.0 * Q / (8.0 * math.pi * om * A * A)) ** (1.0 / 3.0)
        return A / (1.0 + np.exp((self.r - R0) / 0.8))

    def r_halb(self, f):
        S = f * f
        k = np.nonzero(S < 0.5 * S[0])[0]
        if len(k) == 0 or k[0] == 0:
            return None
        j = int(k[0])
        return float(self.r[j - 1] + (0.5 * S[0] - S[j - 1]) * (self.r[j] - self.r[j - 1]) / (S[j] - S[j - 1]))

    def fluss(self, f, Q, g, tau=0.5, c=1.0, nmax=600000, tol=1e-10, wand=60.0):
        for versuch in range(5):
            fe, info = self._fluss(f, Q, g, tau, c, nmax, tol, wand)
            info["tau"] = tau
            info["versuche"] = versuch + 1
            if info["status"] != "nicht_endlich":
                return fe, info
            tau *= 0.5
        return fe, info

    def _fluss(self, f, Q, g, tau, c, nmax, tol, wand):
        M = self.M
        ab = np.zeros((3, M))
        ab[0, 1:] = -tau * self.cp[:-1]
        ab[1, :] = 1.0 + tau * c + tau * (self.cp + self.cm)
        ab[2, :-1] = -tau * self.cm[1:]
        t0 = time.time()
        f = f.copy()
        res = float("inf")
        status = "nmax"
        it = 0
        for it in range(nmax):
            S = f * f
            Lam = 2.0 * float(np.sum(self.w * S))
            om2 = (Q / Lam) ** 2
            if it % 200 == 0:
                R = -self.lap(f) + (Ugp(S, g) - om2) * f
                res = float(np.abs(R).max())
                if res < tol:
                    status = "konvergiert"
                    break
                if time.time() - t0 > wand:
                    status = "wandzeit"
                    break
            rhs = f + tau * (c - Ugp(S, g) + om2) * f
            if not np.all(np.isfinite(rhs)):
                status = "nicht_endlich"
                break
            f = solve_banded((1, 1), ab, rhs)
        if status == "nicht_endlich":
            return f, dict(E=float("nan"), om=float("nan"), Lam=float("nan"), res=float("nan"), it=it, status=status,
                           R_halb=None, f0=float("nan"), dr=self.dr, rmax=self.rmax, Q=Q, g=g, d=self.d,
                           sek=time.time() - t0)
        E, om, Lam = self.energie(f, Q, g)
        # Anteil der Norm in der aeusseren Randzone (r > rmax - 5): Kontrolle gegen Zerfliessen
        rand = float(np.sum((self.w * f * f)[self.r > self.rmax - 5.0]) / np.sum(self.w * f * f))
        return f, dict(E=E, om=om, Lam=Lam, res=res, it=it, status=status, R_halb=self.r_halb(f), f0=float(f[0]),
                       dr=self.dr, rmax=self.rmax, Q=Q, g=g, d=self.d, rand_anteil=rand, sek=time.time() - t0)


# ------------------------------------------------------------------ Gitter (periodisch, spektral, d = 2 oder 3, GPU)
class Gitter:
    def __init__(self, N=256, L=64.0, d=2):
        self.N, self.L, self.d = int(N), float(L), int(d)
        self.h = self.L / self.N
        x = -0.5 * self.L + self.h * np.arange(self.N)
        self.x = x
        k = 2.0 * np.pi * np.fft.fftfreq(self.N, d=self.h)
        xt = torch.tensor(x, dtype=torch.float64, device=DEV)
        kt = torch.tensor(k, dtype=torch.float64, device=DEV)
        self.X = list(torch.meshgrid(*([xt] * d), indexing="ij"))
        self.K = list(torch.meshgrid(*([kt] * d), indexing="ij"))
        self.K2 = sum(kk * kk for kk in self.K)
        self.dV = self.h ** d
        self.Ntot = self.N ** d
        self.i0 = self.N // 2
        self.dims = tuple(range(-d, 0))
        self.view = (3,) + (1,) * d

    def fft(self, f):
        return torch.fft.fftn(f, dim=self.dims)

    def ifft(self, F):
        return torch.fft.ifftn(F, dim=self.dims)

    def grad2(self, f):
        F = self.fft(f)
        return (self.K2 * (F.real ** 2 + F.imag ** 2)).sum(dim=self.dims) * self.dV / self.Ntot

    def lap(self, f):
        return self.ifft(-self.K2 * self.fft(f))

    def phase(self, dvec):
        arg = sum(kk * float(dd) for kk, dd in zip(self.K, dvec))
        return torch.exp(-1j * arg)

    def shiftF(self, F, dvec):
        # Feld mit Fourierbild F, verschoben: f(x - dvec)
        return self.ifft(F * self.phase(dvec))

    def achse(self, n2):
        # Werte laengs der +x-Achse durch den Ursprung
        if self.d == 2:
            return n2[self.i0:, self.i0]
        return n2[self.i0:, self.i0, self.i0]


def profil(G, rad, f, pos=None):
    pos = [0.0] * G.d if pos is None else pos
    xs = np.meshgrid(*([G.x] * G.d), indexing="ij")
    r = np.sqrt(sum((xx - p) ** 2 for xx, p in zip(xs, pos)))
    return torch.tensor(np.interp(r, rad.r, f, right=0.0), dtype=torch.complex128, device=DEV)


def n2von(psi):
    return psi.real ** 2 + psi.imag ** 2


def energie_Q(G, psi, Q, g4):
    n2 = n2von(psi)
    S = n2.sum(0)
    Wpot = G.dV * float((U0(S) + g4 * (n2 * n2).sum(0)).sum())
    Lam = (2.0 * G.dV * n2.sum(dim=G.dims)).tolist()
    g2 = G.grad2(psi).tolist()
    Wgrad, Ekin = 0.0, 0.0
    om = [0.0, 0.0, 0.0]
    for a in range(3):
        if Q[a] > 0:
            Wgrad += g2[a]
            om[a] = float(Q[a] / Lam[a])
            Ekin += Q[a] ** 2 / (2.0 * Lam[a])
    E = Wpot + Wgrad + Ekin
    return E, dict(E=E, Wpot=Wpot, Wgrad=Wgrad, Ekin=Ekin, Lam=Lam, om=om)


def residuum(G, psi, Q, g4):
    n2 = n2von(psi)
    S = n2.sum(0)
    Up = U0p(S)
    Lam = (2.0 * G.dV * n2.sum(dim=G.dims)).tolist()
    lp = G.lap(psi)
    r = 0.0
    for a in range(3):
        if Q[a] > 0:
            om2 = (Q[a] / Lam[a]) ** 2
            R = -lp[a] + (Up + 2.0 * g4 * n2[a] - om2) * psi[a]
            r = max(r, float(R.abs().max()))
    return r


def fluss(G, psi, Q, g4, tau=0.5, c=1.0, nmax=4000, tol=1e-7, alle=50, wand=300.0, beob=None):
    """Halbimpliziter Gradientenfluss von E_Q bei festen Ladungen Q_a (wie DREIPOL-1, ohne Stifte).
    beob(psi) -> Liste weiterer Messwerte je Protokollzeile."""
    t0 = time.time()
    den = (1.0 / (1.0 + tau * (G.K2 + c)))[None]
    Qt = torch.tensor([float(q) for q in Q], dtype=torch.float64, device=DEV)
    mask = Qt > 0
    psi = psi.clone()
    verlauf = []
    status = "nmax"
    it = 0
    for it in range(nmax + 1):
        if it % alle == 0 or it == nmax:
            E, _ = energie_Q(G, psi, Q, g4)
            res = residuum(G, psi, Q, g4)
            row = [it, E, res]
            if beob is not None:
                row += beob(psi)
            verlauf.append(row)
            if (not math.isfinite(E)) or (not math.isfinite(res)):
                status = "nicht_endlich"
                break
            if res < tol:
                status = "konvergiert"
                break
            if time.time() - t0 > wand:
                status = "wandzeit"
                break
            if it == nmax:
                break
        n2 = n2von(psi)
        S = n2.sum(0)
        Up = U0p(S)
        Lam = 2.0 * G.dV * n2.sum(dim=G.dims)
        om2 = torch.where(mask, (Qt / torch.where(mask, Lam, torch.ones_like(Lam))) ** 2, torch.zeros_like(Lam))
        neu = G.ifft(G.fft(psi + tau * (c - Up[None] - 2.0 * g4 * n2 + om2.view(G.view)) * psi) * den)
        psi = torch.where(mask.view(G.view), neu, psi)
    return psi, dict(status=status, it=int(it), verlauf=verlauf, sek=time.time() - t0, tau=tau, c=c, tol=tol)


def r_halb_gitter(G, n2tot):
    s = G.achse(n2tot).cpu().numpy()
    x = G.x[G.i0:]
    k = np.nonzero(s < 0.5 * s[0])[0]
    if len(k) == 0 or k[0] == 0:
        return None
    j = int(k[0])
    return float(x[j - 1] + (0.5 * s[0] - s[j - 1]) * (x[j] - x[j - 1]) / (s[j] - s[j - 1]))


def schwerpunkte(G, n2):
    tot = n2.sum(dim=G.dims)
    out = []
    for a in range(3):
        s = float(tot[a])
        if s <= 0:
            out.append([0.0] * G.d)
        else:
            out.append([float((xx * n2[a]).sum()) / s for xx in G.X])
    return out


def paarabstaende(sp):
    return [float(math.dist(sp[i], sp[j])) for i, j in ((0, 1), (0, 2), (1, 2))]


def reinheit(G, n2, sp):
    """Anteil von |psi_a|^2 in der eigenen Voronoi-Zelle (naechster Komponentenschwerpunkt)."""
    dist = torch.stack([sum((xx - p[i]) ** 2 for i, xx in enumerate(G.X)) for p in sp])
    zelle = torch.argmin(dist, dim=0)
    tot = n2.sum(dim=G.dims)
    return [float((n2[a] * (zelle == a)).sum() / tot[a]) if float(tot[a]) > 0 else None for a in range(3)]


def kabsch_rms(p, q):
    """RMS-Abstand der Punkte q zu p nach bester Verschiebung und Drehung (ohne Spiegelung)."""
    P = np.array(p, float)
    Qm = np.array(q, float)
    P = P - P.mean(0)
    Qm = Qm - Qm.mean(0)
    H = Qm.T @ P
    U, S, Vt = np.linalg.svd(H)
    dsign = np.sign(np.linalg.det(Vt.T @ U.T))
    D = np.eye(P.shape[1])
    D[-1, -1] = dsign
    Rm = Vt.T @ D @ U.T
    return float(np.sqrt(np.mean(np.sum((Qm @ Rm.T - P) ** 2, axis=1))))


def ein_pol_ball(G, rad, g4, Q1, wand=120.0, tol=1e-8, nmax=6000, wand_rad=60.0):
    f, ir = rad.fluss(rad.start(Q1), Q1, g4, wand=wand_rad)
    psi = torch.zeros((3,) + (G.N,) * G.d, dtype=torch.complex128, device=DEV)
    psi[0] = profil(G, rad, f)
    Q = [Q1, 0.0, 0.0]
    psi, info = fluss(G, psi, Q, g4, nmax=nmax, tol=tol, wand=wand)
    E, dd = energie_Q(G, psi, Q, g4)
    n2 = n2von(psi[0])
    r2 = sum(xx * xx for xx in G.X)
    R_rms = float(math.sqrt(float((r2 * n2).sum()) / float(n2.sum())))
    inf = dict(Q=Q1, E=E, om=dd["om"][0], Lam=dd["Lam"][0], R_halb=r_halb_gitter(G, n2), R_rms=R_rms,
               S0=float(G.achse(n2)[0]), status=info["status"], it=info["it"], res=info["verlauf"][-1][2],
               sek=info["sek"], radial=dict(E=ir["E"], om=ir["om"], R_halb=ir["R_halb"], status=ir["status"],
                                            res=ir["res"], it=ir["it"], rand_anteil=ir.get("rand_anteil"),
                                            sek=ir["sek"]),
               abw_gitter_radial=E / ir["E"] - 1.0)
    return psi[0].clone(), inf


def misch_ball(G, rad, g4, Q, wand=120.0, tol=1e-8, nmax=6000, wand_rad=60.0):
    """Gleich gemischter Ball (1,1,1)/sqrt3 mit Q_a = Q/3; Start: radialer Ball mit g_eff = g4/3."""
    geff = g4 / 3.0
    f, ir = rad.fluss(rad.start(Q), Q, geff, wand=wand_rad)
    base = profil(G, rad, f) / SQ3
    psi = torch.stack([base, base.clone(), base.clone()])
    Qa = [Q / 3.0] * 3
    psi, info = fluss(G, psi, Qa, g4, nmax=nmax, tol=tol, wand=wand)
    E, dd = energie_Q(G, psi, Qa, g4)
    return psi, dict(Q=Q, g_eff=geff, E=E, om=dd["om"], status=info["status"], it=info["it"],
                     res=info["verlauf"][-1][2], sek=info["sek"], R_halb=r_halb_gitter(G, n2von(psi).sum(0)),
                     radial=dict(E=ir["E"], om=ir["om"], R_halb=ir["R_halb"], status=ir["status"], res=ir["res"],
                                 it=ir["it"], rand_anteil=ir.get("rand_anteil"), sek=ir["sek"]),
                     abw_gitter_radial=E / ir["E"] - 1.0)


def dreieck_pos(G, d0):
    rho = d0 / SQ3
    pos = []
    for w in WINKEL:
        p = [rho * math.cos(w), rho * math.sin(w)] + [0.0] * (G.d - 2)
        pos.append(p)
    return pos, rho


def beobachter(G, ref_sp=None, R=1.0):
    """Messwerte je Protokollzeile im Fluss: Schwerpunkte, Paarabstaende, Reinheit, Abstand zum Referenzdreieck."""
    ref_pa = paarabstaende(ref_sp) if ref_sp is not None else None

    def f(psi):
        n2 = n2von(psi)
        sp = schwerpunkte(G, n2)
        pa = paarabstaende(sp)
        rein = reinheit(G, n2, sp)
        row = [sp, pa, rein]
        if ref_sp is not None:
            d_form = max(abs(pa[i] - ref_pa[i]) for i in range(3)) / R
            d_rms = kabsch_rms(ref_sp, sp) / R
            row += [d_form, d_rms]
        return row
    return f


def zustand_info(G, psi, Q, g4, R, ref=None):
    E, dd = energie_Q(G, psi, Q, g4)
    n2 = n2von(psi)
    sp = schwerpunkte(G, n2)
    pa = paarabstaende(sp)
    out = dict(E=E, om=dd["om"], Lam=dd["Lam"], res=residuum(G, psi, Q, g4), schwerpunkte=sp, paarabstand=pa,
               paarabstand_R=[p / R for p in pa], reinheit=reinheit(G, n2, sp), S_max=float(n2.sum(0).max()))
    if ref is not None:
        out["d_form_R"] = max(abs(pa[i] - ref["paarabstand"][i]) for i in range(3)) / R
        out["d_rms_R"] = kabsch_rms(ref["schwerpunkte"], sp) / R
        out["dE"] = E - ref["E"]
    return out


def schnitt(G, n2):
    # 2D: Feld selbst (jeder zweite Punkt); 3D: Ebene z = 0
    if G.d == 2:
        return n2[:, ::2, ::2].float().cpu().numpy()
    return n2[:, :, :, G.i0].float().cpu().numpy()


# ------------------------------------------------------------------ Teil A: Stabilitaet des 2D-Dreiecks bei g4 = -0,1
def stoerungen(G, Pref, ref, R, amp_v, amp_l):
    """Stoerungen ausserhalb des symmetrischen Unterraums (PLAN Abschnitt 4)."""
    sp = ref["schwerpunkte"]
    mitte = np.mean(np.array(sp), axis=0)
    out = {}
    F = G.fft(Pref)
    # V1: Pol 1 tangential (x-Richtung) um amp_v R verschoben (bricht die Spiegelung x -> -x)
    P = Pref.clone()
    P[0] = G.shiftF(F[0], [amp_v * R, 0.0])
    out["V1"] = (P, list(ref["Q"]), "Pol 1 um %.2f R tangential (+x)" % amp_v)
    # V2: Pol 2 radial nach aussen um amp_v R
    e = np.array(sp[1]) - mitte
    e = e / np.linalg.norm(e)
    P = Pref.clone()
    P[1] = G.shiftF(F[1], list(amp_v * R * e))
    out["V2"] = (P, list(ref["Q"]), "Pol 2 um %.2f R radial nach aussen" % amp_v)
    # L1: 5 % von Farbe 2 aus Klumpen 2 nach Klumpen 1 (Klumpen 1 +5 %, Klumpen 2 -5 %), gleichphasig
    P = Pref.clone()
    d12 = list(np.array(sp[0]) - np.array(sp[1]))
    P[1] = math.sqrt(1.0 - amp_l) * Pref[1] + math.sqrt(amp_l) * G.shiftF(F[1], d12)
    out["L1"] = (P, list(ref["Q"]), "%.0f %% der Farbe 2 von Klumpen 2 nach Klumpen 1" % (100 * amp_l))
    # L2: 5 % von Farbe 1 aus Klumpen 1 nach Klumpen 2 (Klumpen 1 -5 %, Klumpen 2 +5 %), gleichphasig
    P = Pref.clone()
    d21 = list(np.array(sp[1]) - np.array(sp[0]))
    P[0] = math.sqrt(1.0 - amp_l) * Pref[0] + math.sqrt(amp_l) * G.shiftF(F[0], d21)
    out["L2"] = (P, list(ref["Q"]), "%.0f %% der Farbe 1 von Klumpen 1 nach Klumpen 2" % (100 * amp_l))
    # P1: Phasenversatz pi/2 auf Komponente 2
    P = Pref.clone()
    P[1] = P[1] * complex(math.cos(0.5 * math.pi), math.sin(0.5 * math.pi))
    out["P1"] = (P, list(ref["Q"]), "Phase von Komponente 2 um pi/2 versetzt")
    # P2: Phasenversatz 2pi/3 und 4pi/3 auf Komponenten 2 und 3
    P = Pref.clone()
    P[1] = P[1] * complex(math.cos(2 * math.pi / 3), math.sin(2 * math.pi / 3))
    P[2] = P[2] * complex(math.cos(4 * math.pi / 3), math.sin(4 * math.pi / 3))
    out["P2"] = (P, list(ref["Q"]), "Phasen von Komponente 2 und 3 um 2pi/3 und 4pi/3 versetzt")
    # L3 (beschreibend, ohne Urteil): Sektorwechsel Q = (1+amp_l, 1-amp_l, 1) Q1, Amplituden skaliert
    Q1 = ref["Q"][0]
    P = Pref.clone()
    P[0] = P[0] * math.sqrt(1.0 + amp_l)
    P[1] = P[1] * math.sqrt(1.0 - amp_l)
    out["L3"] = (P, [Q1 * (1.0 + amp_l), Q1 * (1.0 - amp_l), Q1], "Sektorwechsel Q = (63, 57, 60), beschreibend")
    return out


def modus_A(a):
    t0 = time.time()
    G = Gitter(a.N, a.L, 2)
    rad = Radial(2)
    g4, Q1 = a.g4, a.Q1
    out = {"modus": "A", "geraet": GERAET, "N": a.N, "L": a.L, "h": G.h, "g4": g4, "Q1": Q1, "start_utc": jetzt(),
           "amp_v": a.amp_v, "amp_l": a.amp_l, "tol_ref": a.tol_ref, "tol_st": a.tol_st}
    psi1, ball = ein_pol_ball(G, rad, g4, Q1)
    R, E1 = ball["R_halb"], ball["E"]
    out["ball"] = ball
    print("ball", ball, f"t={time.time() - t0:.0f}s", flush=True)
    F1 = G.fft(psi1)
    pos, rho = dreieck_pos(G, 2.0 * R)
    P = torch.stack([G.shiftF(F1, p) for p in pos])
    Q = [Q1, Q1, Q1]
    out["E_eingespannt"] = energie_Q(G, P, Q, g4)[0]
    # (1) Nachbau wie DREIPOL-1 (tol 1e-7), dann weiter bis tol_ref (Referenz fuer die Stoerungen)
    Pf, i1 = fluss(G, P, Q, g4, nmax=a.nmax_nachbau, tol=1e-7, wand=170.0)
    out["nachbau"] = dict(status=i1["status"], it=i1["it"], sek=i1["sek"], **zustand_info(G, Pf, Q, g4, R))
    print("nachbau", {k: v for k, v in out["nachbau"].items()}, f"t={time.time() - t0:.0f}s", flush=True)
    Pref, i2 = fluss(G, Pf, Q, g4, nmax=a.nmax_ref, tol=a.tol_ref, wand=120.0)
    ref = dict(status=i2["status"], it=i2["it"], sek=i2["sek"], Q=Q, **zustand_info(G, Pref, Q, g4, R))
    out["referenz"] = ref
    print("referenz", ref, f"t={time.time() - t0:.0f}s", flush=True)
    schreibe(a.out, out)
    # (2) Mischball Q = 3 Q1
    psim, mix = misch_ball(G, rad, g4, 3.0 * Q1)
    out["mischball"] = mix
    print("mischball", mix, f"t={time.time() - t0:.0f}s", flush=True)
    schreibe(a.out, out)
    snaps = {"referenz": schnitt(G, n2von(Pref))}
    # (3) Stoerungen und Fluss bei festen Ladungen
    out["stoerungen"] = {}
    st = stoerungen(G, Pref, ref, R, a.amp_v, a.amp_l)
    for name in a.liste:
        P0, Qs, text = st[name]
        start = zustand_info(G, P0, Qs, g4, R, ref=ref)
        bo = beobachter(G, ref["schwerpunkte"], R)
        Pe, info = fluss(G, P0, Qs, g4, nmax=a.nmax_st, tol=a.tol_st, wand=a.wand_st, beob=bo)
        ende = zustand_info(G, Pe, Qs, g4, R, ref=ref)
        # Verlauf kompakt: it, E - E_ref, res, d_form, d_rms, Reinheit
        vl = [[r[0], r[1] - ref["E"], r[2], r[-2], r[-1], r[5]] for r in info["verlauf"]]
        out["stoerungen"][name] = dict(text=text, Q=Qs, status=info["status"], it=info["it"], sek=info["sek"],
                                       start=start, ende=ende, verlauf=vl)
        snaps["%s_start" % name] = schnitt(G, n2von(P0))
        snaps["%s_ende" % name] = schnitt(G, n2von(Pe))
        print(f"{name}: {info['status']} it={info['it']} d_rms {start['d_rms_R']:.4f} -> {ende['d_rms_R']:.4f} "
              f"d_form {start['d_form_R']:.4f} -> {ende['d_form_R']:.4f} dE {start['dE']:.3e} -> {ende['dE']:.3e} "
              f"t={time.time() - t0:.0f}s", flush=True)
        schreibe(a.out, out)
    np.savez_compressed(a.out.replace(".json", "_bilder.npz"), x=G.x[::2], **snaps)
    out["sek"] = time.time() - t0
    out["maxrss_mb"] = maxrss_mb()
    out["gpu_mb"] = gpu_mb()
    out["ende_utc"] = jetzt()
    schreibe(a.out, out)


# ------------------------------------------------------------------ Teil B: 3D
def modus_B(a):
    t0 = time.time()
    G = Gitter(a.N, a.L, 3)
    rad = Radial(3, dr=a.dr, rmax=a.rmax)
    g4, Q1 = a.g4, a.Q1
    out = {"modus": "B", "geraet": GERAET, "N": a.N, "L": a.L, "h": G.h, "g4": g4, "Q1": Q1, "dr": a.dr,
           "rmax": a.rmax, "tol": a.tol, "start_utc": jetzt()}
    psi1, ball = ein_pol_ball(G, rad, g4, Q1, wand=a.wand_ball, tol=a.tol, nmax=a.nmax_ball, wand_rad=a.wand_rad)
    R, E1 = ball["R_halb"], ball["E"]
    out["ball"] = ball
    print("ball", ball, f"t={time.time() - t0:.0f}s gpu={gpu_mb():.0f}MB", flush=True)
    schreibe(a.out, out)
    if a.mit_misch:
        psim, mix = misch_ball(G, rad, g4, 3.0 * Q1, wand=a.wand_ball, tol=a.tol, nmax=a.nmax_ball, wand_rad=a.wand_rad)
        out["mischball"] = mix
        print("mischball", mix, f"t={time.time() - t0:.0f}s", flush=True)
        del psim
        schreibe(a.out, out)
    if a.mit_dreieck:
        F1 = G.fft(psi1)
        pos, rho = dreieck_pos(G, 2.0 * R)
        P = torch.stack([G.shiftF(F1, p) for p in pos])
        del F1
        Q = [Q1, Q1, Q1]
        out["start"] = zustand_info(G, P, Q, g4, R)
        out["E_drei_getrennt"] = 3.0 * E1
        snaps = {"start": schnitt(G, n2von(P))}
        bo = beobachter(G, None, R)
        Pe, info = fluss(G, P, Q, g4, nmax=a.nfluss, tol=a.tol, alle=a.alle, wand=a.wand_fluss, beob=bo)
        ende = zustand_info(G, Pe, Q, g4, R)
        out["fluss"] = dict(status=info["status"], it=info["it"], sek=info["sek"], ende=ende,
                            verlauf=[[r[0], r[1], r[2], r[4], r[5]] for r in info["verlauf"]])
        snaps["ende"] = schnitt(G, n2von(Pe))
        np.savez_compressed(a.out.replace(".json", "_bilder.npz"), x=G.x, **snaps)
        print("fluss", info["status"], info["it"], ende, f"t={time.time() - t0:.0f}s", flush=True)
    out["sek"] = time.time() - t0
    out["maxrss_mb"] = maxrss_mb()
    out["gpu_mb"] = gpu_mb()
    out["ende_utc"] = jetzt()
    schreibe(a.out, out)


# ------------------------------------------------------------------ Teil C: schiefer Dreier in echter Zeit (2D)
def kraft(G, ph, g4):
    n2 = n2von(ph)
    S = n2.sum(0)
    return G.lap(ph) - (U0p(S)[None] + 2.0 * g4 * n2) * ph


def energie_t(G, phi, pi, g4):
    n2 = n2von(phi)
    S = n2.sum(0)
    E = G.dV * float((U0(S) + g4 * (n2 * n2).sum(0)).sum())
    E += G.dV * float((pi.real ** 2 + pi.imag ** 2).sum())
    E += float(G.grad2(phi).sum())
    return E


SPALTEN = ["t", "E", "Q1", "Q2", "Q3", "Qin1", "Qin2", "Qin3", "X1", "X2", "X3", "Y1", "Y2", "Y3", "Xt", "Yt",
           "Smax", "r1", "r2", "r3"]


def messe(G, t, phi, pi, g4, Rk):
    q = 2.0 * (phi.real * pi.imag - phi.imag * pi.real)
    Qa = (G.dV * q.sum(dim=G.dims)).tolist()
    qt = q.sum(0)
    st = float(qt.sum())
    Xt = float((G.X[0] * qt).sum()) / st
    Yt = float((G.X[1] * qt).sum()) / st
    inside = ((G.X[0] - Xt) ** 2 + (G.X[1] - Yt) ** 2) < Rk * Rk
    Qin = (G.dV * (q * inside[None]).sum(dim=G.dims)).tolist()
    sa = q.sum(dim=G.dims).tolist()
    Xa = [float((G.X[0] * q[k]).sum()) / sa[k] if sa[k] != 0 else 0.0 for k in range(3)]
    Ya = [float((G.X[1] * q[k]).sum()) / sa[k] if sa[k] != 0 else 0.0 for k in range(3)]
    ra = [math.hypot(Xa[k] - Xt, Ya[k] - Yt) for k in range(3)]
    Smax = float(n2von(phi).sum(0).max())
    return [t, energie_t(G, phi, pi, g4)] + Qa + Qin + Xa + Ya + [Xt, Yt, Smax] + ra


def rauschfeld(G, saat, kc=2.0):
    rng = np.random.default_rng(saat)
    w = rng.standard_normal((6, G.N, G.N))
    eta = torch.tensor(w[0:3] + 1j * w[3:6], dtype=torch.complex128, device=DEV)
    F = G.fft(eta) * torch.exp(-G.K2 / (2.0 * kc * kc))[None]
    eta = G.ifft(F)
    return eta / math.sqrt(float((eta.real ** 2 + eta.imag ** 2).mean()))


def entwickle(G, phi, pi, g4, dt, T, dmess, Rk, schnapp_t=(), wand=540.0):
    t0 = time.time()
    nsteps = int(round(T / dt))
    nsub = int(round(dmess / dt))
    schnapp_k = {int(round(ts / dt)): ts for ts in schnapp_t}
    schnapp = {}
    phi = phi.clone()
    pi = pi.clone()
    f = kraft(G, phi, g4)
    rec = [messe(G, 0.0, phi, pi, g4, Rk)]
    if 0 in schnapp_k:
        schnapp[schnapp_k[0]] = schnitt(G, n2von(phi))
    status = "fertig"
    for k in range(1, nsteps + 1):
        pi += (0.5 * dt) * f
        phi += dt * pi
        f = kraft(G, phi, g4)
        pi += (0.5 * dt) * f
        if k % nsub == 0:
            rec.append(messe(G, k * dt, phi, pi, g4, Rk))
            if not math.isfinite(rec[-1][1]):
                status = "nicht_endlich"
                break
            if time.time() - t0 > wand:
                status = "wandzeit"
                break
        if k in schnapp_k:
            schnapp[schnapp_k[k]] = schnitt(G, n2von(phi))
    return np.array(rec), status, schnapp


def schief_start(G, rad, g4, Q1, fern, klein, saat=None, eps=0.0):
    """Schiefer Dreier: Pol 1 so weit nach aussen, dass seine Abstaende zu Pol 2 und 3 'fern' * d0 sind;
    Pol 2 mit Ladung 'klein' * Q1. Baelle in Ruhe (pi = i om psi), Rauschen eps wie DREIPOL-1."""
    psiA, ballA = ein_pol_ball(G, rad, g4, Q1)
    psiB, ballB = ein_pol_ball(G, rad, g4, klein * Q1)
    R = ballA["R_halb"]
    d0 = 2.0 * R
    rho = d0 / SQ3
    p2 = [-0.5 * d0, -0.5 * rho]
    p3 = [0.5 * d0, -0.5 * rho]
    y1 = -0.5 * rho + math.sqrt((fern * d0) ** 2 - (0.5 * d0) ** 2)
    p1 = [0.0, y1]
    FA = G.fft(psiA)
    FB = G.fft(psiB)
    P = torch.stack([G.shiftF(FA, p1), G.shiftF(FB, p2), G.shiftF(FA, p3)])
    oms = [ballA["om"], ballB["om"], ballA["om"]]
    pi = torch.stack([1j * oms[k] * P[k] for k in range(3)])
    phi = P.clone()
    if eps > 0:
        env = torch.sqrt(n2von(P).sum(0))
        eta = rauschfeld(G, saat)
        eta2 = rauschfeld(G, saat + 1000)
        phi = P + eps * eta * env[None]
        pi = pi + eps * ballA["om"] * eta2 * env[None]
    Rk = rho + 3.0 * R
    info = dict(ballA=ballA, ballB=ballB, R=R, d0=d0, rho=rho, R_K=Rk, pos=[p1, p2, p3], om=oms,
                Q=[Q1, klein * Q1, Q1], paarabstand_start=paarabstaende([p1, p2, p3]))
    return phi, pi, info, (psiA, psiB)


def modus_S(a):
    """Schwellen fuer die Ableitbarkeitsprobe von DP3: Startenergie des schiefen Dreiers, drei getrennte Baelle,
    zwei verschmolzen plus einer frei (Paarminimum aus zwei Startformen)."""
    t0 = time.time()
    G = Gitter(a.N, a.L, 2)
    rad = Radial(2)
    out = {"modus": "S", "geraet": GERAET, "start_utc": jetzt(), "je_g4": {}}
    for g4 in a.g4liste:
        Q1 = a.Q1
        phi, pi, info, (psiA, psiB) = schief_start(G, rad, g4, Q1, a.fern, a.klein)
        E_start = energie_t(G, phi, pi, g4)
        EA, EB = info["ballA"]["E"], info["ballB"]["E"]
        R = info["R"]
        e = dict(E_start=E_start, E_1_Q1=EA, E_1_klein=EB, E_drei_getrennt=2 * EA + EB, info=info)
        paare = {}
        for name, (Qa, Qb, Erest) in {"60+60 (Pol 2 frei)": (Q1, Q1, EB),
                                       "60+57 (Pol 1 oder 3 frei)": (Q1, a.klein * Q1, EA)}.items():
            psiQa = psiA
            psiQb = psiB if abs(Qb - a.klein * Q1) < 1e-12 else psiA
            FA, FB = G.fft(psiQa), G.fft(psiQb)
            z = torch.zeros_like(psiA)
            # Form 1: beruehrendes Paar (Abstand 2R), verschiedene Farben
            P = torch.stack([G.shiftF(FA, [R, 0.0]), G.shiftF(FB, [-R, 0.0]), z])
            P1, i1 = fluss(G, P, [Qa, Qb, 0.0], g4, nmax=12000, tol=1e-7, wand=100.0)
            E1_, _ = energie_Q(G, P1, [Qa, Qb, 0.0], g4)
            pa1 = paarabstaende(schwerpunkte(G, n2von(P1)))[0]
            # Form 2: gemischter Start (beide Farben auf demselben Platz)
            P = torch.stack([psiQa.clone(), G.shiftF(FB, [0.0, 0.0]), z])
            P2, i2 = fluss(G, P, [Qa, Qb, 0.0], g4, nmax=12000, tol=1e-7, wand=100.0)
            E2_, _ = energie_Q(G, P2, [Qa, Qb, 0.0], g4)
            pa2 = paarabstaende(schwerpunkte(G, n2von(P2)))[0]
            Emin = min(E1_, E2_)
            paare[name] = dict(Q=[Qa, Qb], E_paar_beruehrend=E1_, status1=i1["status"], it1=i1["it"],
                               abstand1_R=pa1 / R, E_paar_gemischt=E2_, status2=i2["status"], it2=i2["it"],
                               abstand2_R=pa2 / R, E_paar_min=Emin, E_rest=Erest, schwelle=Emin + Erest,
                               start_minus_schwelle=E_start - (Emin + Erest))
            print(g4, name, paare[name], f"t={time.time() - t0:.0f}s", flush=True)
        e["paare"] = paare
        e["ausstoss_energetisch_verboten"] = bool(all(p["start_minus_schwelle"] < 0 for p in paare.values()))
        e["zerfall_in_drei_verboten"] = bool(E_start < e["E_drei_getrennt"])
        out["je_g4"]["%g" % g4] = e
        print("g4", g4, "E_start", E_start, "drei", e["E_drei_getrennt"], f"t={time.time() - t0:.0f}s", flush=True)
        schreibe(a.out, out)
    out["sek"] = time.time() - t0
    out["ende_utc"] = jetzt()
    schreibe(a.out, out)


def modus_C(a):
    t0 = time.time()
    G = Gitter(a.N, a.L, 2)
    rad = Radial(2)
    g4, Q1 = a.g4, a.Q1
    out = {"modus": "C", "geraet": GERAET, "N": a.N, "L": a.L, "h": G.h, "g4": g4, "Q1": Q1, "fern": a.fern,
           "klein": a.klein, "start_utc": jetzt(), "laeufe": {}}
    snaps = {}
    for saat in a.saaten:
        phi, pi, info, _ = schief_start(G, rad, g4, Q1, a.fern, a.klein, saat=saat, eps=a.eps)
        if "info" not in out:
            out["info"] = info
        rec, status, sn = entwickle(G, phi, pi, g4, a.dt, a.T, a.dmess, info["R_K"], schnapp_t=a.schnapp,
                                    wand=a.wand_t)
        for ts, arr in sn.items():
            snaps["s%d_t%g" % (saat, ts)] = arr
        E0 = rec[0, 1]
        dE = float(np.abs(rec[:, 1] - E0).max() / abs(E0))
        dQ = float(max(np.abs(rec[:, 2 + k] - rec[0, 2 + k]).max() / abs(rec[0, 2 + k]) for k in range(3)))
        out["laeufe"]["saat%d" % saat] = dict(status=status, spalten=SPALTEN, reihe=rec.tolist(), dE_rel=dE,
                                              dQ_rel=dQ, saat=saat, eps=a.eps, dt=a.dt, T=a.T)
        print(f"saat {saat}: {status} dE={dE:.2e} dQ={dQ:.2e} t_end={rec[-1, 0]} t={time.time() - t0:.0f}s "
              f"gpu={gpu_mb():.0f}MB", flush=True)
        schreibe(a.out, out)
    np.savez_compressed(a.out.replace(".json", "_bilder.npz"), x=G.x[::2], **snaps)
    out["sek"] = time.time() - t0
    out["maxrss_mb"] = maxrss_mb()
    out["gpu_mb"] = gpu_mb()
    out["ende_utc"] = jetzt()
    schreibe(a.out, out)


# ------------------------------------------------------------------ Rauchlauf
def modus_rauch(a):
    t0 = time.time()
    out = {"modus": "rauch", "geraet": GERAET, "start_utc": jetzt(),
           "threads_env": {k: os.environ.get(k) for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS")}}
    if "2d" in a.teile:
        # 2D-Einpolball g4 = -0,1, Q1 = 60 gegen DREIPOL-1 (c_m01.json: E = 48.51294293268749, R_halb = 3.17581826)
        G = Gitter(256, 64.0, 2)
        rad = Radial(2)
        psi1, ball = ein_pol_ball(G, rad, -0.1, 60.0)
        out["ball2d"] = ball
        out["ball2d_abw_qd1"] = dict(E=ball["E"] / 48.51294293268749 - 1.0, R_halb=ball["R_halb"] - 3.1758182642377246)
        print("ball2d", ball, out["ball2d_abw_qd1"], f"t={time.time() - t0:.0f}s", flush=True)
        P = torch.stack([psi1, psi1, psi1]) / SQ3
        t1 = time.time()
        _, inf = fluss(G, P, [20.0, 20.0, 20.0], -0.1, nmax=200, tol=0.0, alle=50)
        torch.cuda.synchronize()
        out["ms_flussschritt_2d"] = 1e3 * (time.time() - t1) / 200
        ph = P.clone()
        pi = 1j * 0.7 * ph
        t1 = time.time()
        rec, st, _ = entwickle(G, ph, pi, -0.1, 0.025, 5.0, 0.5, 13.0)
        torch.cuda.synchronize()
        out["ms_zeitschritt_2d"] = 1e3 * (time.time() - t1) / 200
        print("ms fluss/zeit 2d", out["ms_flussschritt_2d"], out["ms_zeitschritt_2d"], flush=True)
        schreibe(a.out, out)
    if "rad3" in a.teile:
        # 3D radial: Einpolball fuer mehrere Q bei g4 = -0,1 und +0,1 (nur Einzelball-Aufbau)
        out["rad3"] = []
        for g in (-0.1, 0.1):
            for Q in a.Qscan:
                rad = Radial(3, dr=a.dr_scan, rmax=a.rmax_scan)
                f, ir = rad.fluss(rad.start(Q), Q, g, wand=a.wand_scan, tol=1e-8)
                z = {k: ir.get(k) for k in ("Q", "g", "E", "om", "R_halb", "status", "res", "it", "rand_anteil",
                                            "sek", "f0", "dr", "rmax")}
                out["rad3"].append(z)
                print("rad3", z, f"t={time.time() - t0:.0f}s", flush=True)
                schreibe(a.out, out)
    if "git3" in a.teile:
        out["git3"] = []
        for N in a.Nliste:
            G = Gitter(N, a.L3, 3)
            rad = Radial(3, dr=0.01, rmax=a.rmax)
            psi1, ball = ein_pol_ball(G, rad, -0.1, a.Q3, wand=150.0, tol=1e-6, nmax=20000, wand_rad=60.0)
            P = torch.stack([psi1, psi1, psi1]) / SQ3
            torch.cuda.synchronize()
            t1 = time.time()
            _, inf = fluss(G, P, [a.Q3 / 3] * 3, -0.1, nmax=100, tol=0.0, alle=50)
            torch.cuda.synchronize()
            ms = 1e3 * (time.time() - t1) / 100
            z = dict(N=N, L=a.L3, h=a.L3 / N, ball=ball, ms_flussschritt_3k=ms, gpu_mb=gpu_mb())
            out["git3"].append(z)
            print("git3", z, f"t={time.time() - t0:.0f}s", flush=True)
            schreibe(a.out, out)
            del G, psi1, P
            torch.cuda.empty_cache()
    out["sek"] = time.time() - t0
    out["maxrss_mb"] = maxrss_mb()
    out["gpu_mb"] = gpu_mb()
    out["ende_utc"] = jetzt()
    schreibe(a.out, out)


def liste(s, typ=float):
    return [typ(v) for v in s.split(",")]


def main():
    global GERAET
    ap = argparse.ArgumentParser()
    ap.add_argument("modus", choices=["rauch", "A", "B", "C", "S"])
    ap.add_argument("--out", required=True)
    ap.add_argument("--N", type=int, default=256)
    ap.add_argument("--L", type=float, default=64.0)
    ap.add_argument("--Q1", type=float, default=60.0)
    ap.add_argument("--g4", type=float, default=-0.1)
    ap.add_argument("--g4liste", type=liste, default=[0.1, -0.1])
    # Teil A
    ap.add_argument("--amp_v", type=float, default=0.15)
    ap.add_argument("--amp_l", type=float, default=0.05)
    ap.add_argument("--tol_ref", type=float, default=1e-9)
    ap.add_argument("--nmax_nachbau", type=int, default=12000)
    ap.add_argument("--nmax_ref", type=int, default=8000)
    ap.add_argument("--nmax_ball", type=int, default=20000)
    ap.add_argument("--tol_st", type=float, default=1e-8)
    ap.add_argument("--nmax_st", type=int, default=8000)
    ap.add_argument("--wand_st", type=float, default=45.0)
    ap.add_argument("--liste", type=lambda s: s.split(","), default=["V1", "V2", "L1", "L2", "P1", "P2", "L3"])
    # Teil B
    ap.add_argument("--dr", type=float, default=0.01)
    ap.add_argument("--rmax", type=float, default=60.0)
    ap.add_argument("--tol", type=float, default=1e-6)
    ap.add_argument("--wand_ball", type=float, default=90.0)
    ap.add_argument("--wand_rad", type=float, default=60.0)
    ap.add_argument("--nfluss", type=int, default=20000)
    ap.add_argument("--alle", type=int, default=50)
    ap.add_argument("--wand_fluss", type=float, default=300.0)
    ap.add_argument("--mit_misch", type=int, default=1)
    ap.add_argument("--mit_dreieck", type=int, default=1)
    # Teil C
    ap.add_argument("--fern", type=float, default=1.1)
    ap.add_argument("--klein", type=float, default=0.95)
    ap.add_argument("--saaten", type=lambda s: liste(s, int), default=[1, 2, 3, 4])
    ap.add_argument("--eps", type=float, default=1e-3)
    ap.add_argument("--T", type=float, default=300.0)
    ap.add_argument("--dt", type=float, default=0.025)
    ap.add_argument("--dmess", type=float, default=0.5)
    ap.add_argument("--schnapp", type=liste, default=[0.0, 100.0, 200.0, 300.0])
    ap.add_argument("--wand_t", type=float, default=130.0)
    # Rauchlauf
    ap.add_argument("--teile", type=lambda s: s.split(","), default=["2d", "rad3", "git3"])
    ap.add_argument("--Qscan", type=liste, default=[100.0, 200.0, 400.0, 800.0, 1600.0])
    ap.add_argument("--dr_scan", type=float, default=0.02)
    ap.add_argument("--rmax_scan", type=float, default=40.0)
    ap.add_argument("--wand_scan", type=float, default=20.0)
    ap.add_argument("--Q3", type=float, default=400.0)
    ap.add_argument("--L3", type=float, default=48.0)
    ap.add_argument("--Nliste", type=lambda s: liste(s, int), default=[64, 96])
    a = ap.parse_args()
    GERAET = geraet()
    print("geraet", GERAET, flush=True)
    t0 = time.time()
    {"rauch": modus_rauch, "A": modus_A, "B": modus_B, "C": modus_C, "S": modus_S}[a.modus](a)
    print("geschrieben", a.out, f"{time.time() - t0:.1f}s", flush=True)


GERAET = None
if __name__ == "__main__":
    main()
