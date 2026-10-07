#!/usr/bin/env python3
# QBALL-DREIPOL-1 (Runde 42): Q-Baelle mit drei komplexen Komponenten ("drei Pole") in 2+1 Dimensionen.
# Modell = Papier I (main.tex, Gl. eq:action) mit drei Komponenten und Anisotropie g4:
#   L = sum_a |d_t phi_a|^2 - |grad phi_a|^2 - V,  V = U(S) + g4 sum_a |phi_a|^4,  S = sum_a |phi_a|^2,
#   U(S) = S - S^2 + BETA S^3,  BETA = 1/2  (freie Masse 1, Selbstkopplung des Quartterms -1).
# Energie E = int [sum_a |pi_a|^2 + |grad phi_a|^2 + V];  Ladung je Komponente Q_a = 2 int Im(conj(phi_a) pi_a).
# Bewegung: d_t^2 phi_a = Lap phi_a - (U'(S) + 2 g4 |phi_a|^2) phi_a.
# Feste Ladungen (astra L3 sinngemaess): E_Q[psi] = W[psi] + sum_a Q_a^2 / (2 Lam_a),  Lam_a = 2 int |psi_a|^2,
#   om_a = Q_a / Lam_a; Minimum von E_Q = stationaerer Zustand psi_a exp(i om_a t).
# Gitter: periodisch L x L, N x N Knoten, spektrale Ableitungen (scipy.fft, workers=1).
# Radialer Bezug: zentrierte Zellen, Fluss-Laplace, Dirichlet bei rmax, Gradientenfluss bei festem Q.
import sys, os, json, time, math, argparse, resource
import numpy as np
import scipy
import scipy.fft as sfft
from scipy.linalg import solve_banded

BETA = 0.5
SQ3 = math.sqrt(3.0)
RICHTUNGEN = [("ein_pol", (1.0, 0.0, 0.0)), ("zwei_pole", (1.0, 1.0, 0.0)), ("gleich_gemischt", (1.0, 1.0, 1.0))]


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


def g4tag(g4):
    if g4 == 0.0:
        return "0"
    return ("p" if g4 > 0 else "m") + ("%g" % abs(g4)).replace("0.", "0")


# ------------------------------------------------------------------ radialer Bezug (eine Komponente, Kopplung g)
class Radial:
    def __init__(self, dr=0.01, rmax=60.0):
        M = int(round(rmax / dr))
        self.M, self.dr, self.rmax = M, dr, rmax
        j = np.arange(M)
        self.r = (j + 0.5) * dr
        self.rp = (j + 1.0) * dr
        self.rm = j * dr
        self.w = 2.0 * np.pi * self.r * dr
        self.cp = self.rp / (self.r * dr * dr)
        self.cm = self.rm / (self.r * dr * dr)

    def lap(self, f):
        fp = np.r_[f[1:], 0.0]
        fm = np.r_[0.0, f[:-1]]
        return self.cp * (fp - f) - self.cm * (f - fm)

    def energie(self, f, Q, g):
        fp = np.r_[f[1:], 0.0]
        Eg = 2.0 * np.pi * float(np.sum(self.rp * (fp - f) ** 2)) / self.dr
        Ep = float(np.sum(self.w * Ug(f * f, g)))
        Lam = 2.0 * float(np.sum(self.w * f * f))
        return Eg + Ep + Q * Q / (2.0 * Lam), Q / Lam, Lam

    def start(self, Q, A=1.0, om=0.8):
        R0 = math.sqrt(Q / (2.0 * math.pi * om * A * A))
        return A / (1.0 + np.exp((self.r - R0) / 0.8))

    def r_halb(self, f):
        S = f * f
        k = np.nonzero(S < 0.5 * S[0])[0]
        if len(k) == 0 or k[0] == 0:
            return None
        j = int(k[0])
        return float(self.r[j - 1] + (0.5 * S[0] - S[j - 1]) * (self.r[j] - self.r[j - 1]) / (S[j] - S[j - 1]))

    def fluss(self, f, Q, g, tau=0.5, c=1.0, nmax=400000, tol=1e-10, wand=60.0):
        # bei nicht endlichen Werten Neustart vom selben Startprofil mit halbem tau (hoechstens 5 Versuche)
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
                           R_halb=None, f0=float("nan"), dr=self.dr, rmax=self.rmax, Q=Q, g=g, sek=time.time() - t0)
        E, om, Lam = self.energie(f, Q, g)
        return f, dict(E=E, om=om, Lam=Lam, res=res, it=it, status=status, R_halb=self.r_halb(f), f0=float(f[0]),
                       dr=self.dr, rmax=self.rmax, Q=Q, g=g, sek=time.time() - t0)


# ------------------------------------------------------------------ 2D-Gitter
class Gitter:
    def __init__(self, N=256, L=64.0):
        self.N = int(N)
        self.L = float(L)
        self.h = self.L / self.N
        x = -0.5 * self.L + self.h * np.arange(self.N)
        self.x = x
        self.X, self.Y = np.meshgrid(x, x, indexing="ij")
        k = 2.0 * np.pi * sfft.fftfreq(self.N, d=self.h)
        self.KX, self.KY = np.meshgrid(k, k, indexing="ij")
        self.K2 = self.KX ** 2 + self.KY ** 2
        self.dA = self.h * self.h
        self.i0 = self.N // 2

    def fft(self, f):
        return sfft.fft2(f, workers=1)

    def ifft(self, F):
        return sfft.ifft2(F, workers=1)

    def grad2(self, f):
        F = self.fft(f)
        return float(np.sum(self.K2 * (F.real ** 2 + F.imag ** 2))) * self.dA / self.N ** 2

    def lap(self, f):
        return self.ifft(-self.K2 * self.fft(f))

    def phase(self, dx, dy):
        return np.exp(-1j * (self.KX * dx + self.KY * dy))

    def shiftF(self, F, dx, dy):
        # Feld mit Fourierbild F, verschoben: f(x - dx, y - dy)
        return self.ifft(F * self.phase(dx, dy))


def profil_2d(G, rad, f, x0=0.0, y0=0.0):
    r = np.sqrt((G.X - x0) ** 2 + (G.Y - y0) ** 2)
    return np.interp(r, rad.r, f, right=0.0)


def energie_Q(G, psi, Q, g4):
    n2 = psi.real ** 2 + psi.imag ** 2
    S = n2.sum(0)
    Wpot = G.dA * float(np.sum(U0(S) + g4 * np.sum(n2 * n2, axis=0)))
    Wgrad = 0.0
    Lam = 2.0 * G.dA * n2.sum(axis=(1, 2))
    Ekin = 0.0
    om = [0.0] * psi.shape[0]
    for a in range(psi.shape[0]):
        if Q[a] > 0:
            Wgrad += G.grad2(psi[a])
            om[a] = float(Q[a] / Lam[a])
            Ekin += Q[a] ** 2 / (2.0 * Lam[a])
    E = Wpot + Wgrad + Ekin
    return E, dict(E=E, Wpot=Wpot, Wgrad=Wgrad, Ekin=Ekin, Lam=[float(v) for v in Lam], om=om)


def residuum(G, psi, Q, g4):
    n2 = psi.real ** 2 + psi.imag ** 2
    S = n2.sum(0)
    Up = U0p(S)
    Lam = 2.0 * G.dA * n2.sum(axis=(1, 2))
    r = 0.0
    for a in range(psi.shape[0]):
        if Q[a] > 0:
            om2 = (Q[a] / Lam[a]) ** 2
            R = -G.lap(psi[a]) + (Up + 2.0 * g4 * n2[a] - om2) * psi[a]
            r = max(r, float(np.abs(R).max()))
    return r


def fluss(G, psi, Q, g4, tau=0.5, c=1.0, nmax=4000, tol=1e-7, tolE=None, pins=None, alle=50, wand=300.0):
    """Halbimpliziter Gradientenfluss von E_Q bei festen Ladungen Q_a. pins: Liste (x, y) je Komponente oder None;
    dann wird jede aktive Komponente nach jedem Schritt spektral so verschoben, dass ihr |psi_a|^2-Schwerpunkt
    auf dem Stift liegt (eingespannte Relaxation)."""
    t0 = time.time()
    act = [a for a in range(psi.shape[0]) if Q[a] > 0]
    den = 1.0 / (1.0 + tau * (G.K2 + c))
    psi = psi.copy()
    verlauf = []
    E_alt = None
    status = "nmax"
    it = 0
    for it in range(nmax + 1):
        if it % alle == 0 or it == nmax:
            E, _ = energie_Q(G, psi, Q, g4)
            res = residuum(G, psi, Q, g4)
            verlauf.append([it, E, res])
            if (not np.isfinite(E)) or (not np.isfinite(res)):
                status = "nicht_endlich"
                break
            if pins is None and res < tol:
                status = "konvergiert"
                break
            if tolE is not None and E_alt is not None and abs(E - E_alt) < tolE * abs(E):
                status = "konvergiert_E"
                break
            E_alt = E
            if time.time() - t0 > wand:
                status = "wandzeit"
                break
            if it == nmax:
                break
        n2 = psi.real ** 2 + psi.imag ** 2
        S = n2.sum(0)
        Up = U0p(S)
        Lam = 2.0 * G.dA * n2.sum(axis=(1, 2))
        for a in act:
            om2 = (Q[a] / Lam[a]) ** 2
            Fa = G.fft(psi[a] + tau * (c - Up - 2.0 * g4 * n2[a] + om2) * psi[a]) * den
            if pins is not None and pins[a] is not None:
                w = n2[a] / n2[a].sum()
                xa = float(np.sum(G.X * w))
                ya = float(np.sum(G.Y * w))
                Fa = Fa * G.phase(pins[a][0] - xa, pins[a][1] - ya)
            psi[a] = G.ifft(Fa)
    return psi, dict(status=status, it=int(it), verlauf=verlauf, sek=time.time() - t0, tau=tau, c=c, tol=tol)


def r_halb_2d(G, n2):
    s = n2[G.i0:, G.i0]
    x = G.x[G.i0:]
    k = np.nonzero(s < 0.5 * s[0])[0]
    if len(k) == 0 or k[0] == 0:
        return None
    j = int(k[0])
    return float(x[j - 1] + (0.5 * s[0] - s[j - 1]) * (x[j] - x[j - 1]) / (s[j] - s[j - 1]))


def schwerpunkte(G, n2):
    out = []
    for a in range(n2.shape[0]):
        s = n2[a].sum()
        if s <= 0:
            out.append([0.0, 0.0])
        else:
            out.append([float(np.sum(G.X * n2[a]) / s), float(np.sum(G.Y * n2[a]) / s)])
    return out


def ein_pol_ball(G, rad, g4, Q1, wand=120.0, tol=1e-8):
    f, ir = rad.fluss(rad.start(Q1), Q1, g4)
    psi = np.zeros((3, G.N, G.N), complex)
    psi[0] = profil_2d(G, rad, f)
    Q = np.array([Q1, 0.0, 0.0])
    psi, info = fluss(G, psi, Q, g4, nmax=6000, tol=tol, wand=wand)
    E, d = energie_Q(G, psi, Q, g4)
    n2 = psi[0].real ** 2 + psi[0].imag ** 2
    r2 = G.X ** 2 + G.Y ** 2
    R_rms = float(math.sqrt(np.sum(r2 * n2) / np.sum(n2)))
    inf = dict(E=E, om=d["om"][0], Lam=d["Lam"][0], R_halb=r_halb_2d(G, n2), R_rms=R_rms, S0=float(n2[G.i0, G.i0]),
               status=info["status"], it=info["it"], res=info["verlauf"][-1][2], sek=info["sek"],
               radial=dict(E=ir["E"], om=ir["om"], R_halb=ir["R_halb"], status=ir["status"], res=ir["res"]))
    return psi[0].copy(), inf


# ------------------------------------------------------------------ Zeitentwicklung
def kraft(G, ph, g4, act):
    n2 = ph.real ** 2 + ph.imag ** 2
    S = n2.sum(0)
    Up = U0p(S)
    F = np.zeros_like(ph)
    for a in act:
        F[a] = G.ifft(-G.K2 * G.fft(ph[a])) - (Up + 2.0 * g4 * n2[a]) * ph[a]
    return F


def energie_t(G, phi, pi, g4, act):
    n2 = phi.real ** 2 + phi.imag ** 2
    S = n2.sum(0)
    E = G.dA * float(np.sum(U0(S) + g4 * np.sum(n2 * n2, axis=0)))
    E += G.dA * float(np.sum(pi.real ** 2 + pi.imag ** 2))
    for a in act:
        E += G.grad2(phi[a])
    return E


SPALTEN = ["t", "E", "Q1", "Q2", "Q3", "Qin1", "Qin2", "Qin3", "X1", "X2", "X3", "Y1", "Y2", "Y3", "Xt", "Yt",
           "Smax"]


def messe(G, t, phi, pi, g4, act, Rk):
    q = 2.0 * (phi.real * pi.imag - phi.imag * pi.real)
    Qa = G.dA * q.sum(axis=(1, 2))
    qt = q.sum(0)
    st = float(qt.sum())
    Xt = float(np.sum(G.X * qt) / st)
    Yt = float(np.sum(G.Y * qt) / st)
    inside = ((G.X - Xt) ** 2 + (G.Y - Yt) ** 2) < Rk * Rk
    Qin = G.dA * (q * inside[None]).sum(axis=(1, 2))
    Xa, Ya = [], []
    for a in range(3):
        s = float(q[a].sum())
        Xa.append(float(np.sum(G.X * q[a]) / s) if s != 0 else 0.0)
        Ya.append(float(np.sum(G.Y * q[a]) / s) if s != 0 else 0.0)
    S = (phi.real ** 2 + phi.imag ** 2).sum(0)
    return [t, energie_t(G, phi, pi, g4, act)] + [float(v) for v in Qa] + [float(v) for v in Qin] + Xa + Ya + \
        [Xt, Yt, float(S.max())]


def rauschfeld(G, saat, kc=2.0):
    rng = np.random.default_rng(saat)
    w = rng.standard_normal((6, G.N, G.N))
    eta = w[0:3] + 1j * w[3:6]
    F = sfft.fft2(eta, axes=(1, 2), workers=1) * np.exp(-G.K2 / (2.0 * kc * kc))[None]
    eta = sfft.ifft2(F, axes=(1, 2), workers=1)
    eta = eta / math.sqrt(float(np.mean(np.abs(eta) ** 2)))
    return eta


def entwickle(G, phi, pi, g4, dt, T, dmess, Rk, schnapp_t=(), wand=420.0, t_start=None):
    t0 = time.time() if t_start is None else t_start
    act = [a for a in range(3) if np.any(phi[a] != 0)]
    nsteps = int(round(T / dt))
    nsub = int(round(dmess / dt))
    schnapp_k = {int(round(ts / dt)): ts for ts in schnapp_t}
    schnapp = {}
    phi = phi.copy()
    pi = pi.copy()
    f = kraft(G, phi, g4, act)
    rec = [messe(G, 0.0, phi, pi, g4, act, Rk)]
    if 0 in schnapp_k:
        schnapp[schnapp_k[0]] = (phi.real ** 2 + phi.imag ** 2)[:, ::2, ::2].astype(np.float32)
    status = "fertig"
    k = 0
    for k in range(1, nsteps + 1):
        pi += (0.5 * dt) * f
        phi += dt * pi
        f = kraft(G, phi, g4, act)
        pi += (0.5 * dt) * f
        if k % nsub == 0:
            rec.append(messe(G, k * dt, phi, pi, g4, act, Rk))
            if not np.isfinite(rec[-1][1]):
                status = "nicht_endlich"
                break
        if k in schnapp_k:
            schnapp[schnapp_k[k]] = (phi.real ** 2 + phi.imag ** 2)[:, ::2, ::2].astype(np.float32)
        if time.time() - t0 > wand:
            status = "wandzeit"
            break
    return np.array(rec), status, schnapp, phi, pi


# ------------------------------------------------------------------ Modus a: Kontrolle E(Q) je Richtung
def radial_ref(cache, Q, g, dr=0.01):
    key = (round(Q, 9), round(g, 12), dr)
    if key not in cache:
        rad = Radial(dr=dr)
        f, ir = rad.fluss(rad.start(Q), Q, g)
        cache[key] = (f, ir, rad)
    return cache[key]


def modus_a(a):
    t0 = time.time()
    G = Gitter(a.N, a.L)
    out = {"modus": "a", "N": a.N, "L": a.L, "h": G.h, "Q": a.Q, "g4": a.g4, "start_utc": jetzt(),
           "versionen": dict(numpy=np.__version__, scipy=scipy.__version__, python=sys.version.split()[0]),
           "zustaende": [], "radial": [], "extern": None}
    cache = {}
    if a.extern:
        f, ir, _ = radial_ref(cache, 100.0, 0.0)
        f2, ir2, _ = radial_ref(cache, 100.0, 0.0, dr=0.02)
        out["extern"] = dict(quelle="RUNDE-37/qb-bs-2d/lauf-69/auswertung.json, E_fein bei q = 100 (l = 0, M = 1200)",
                             E_quelle=82.13970757077503, E_dr001=ir["E"], E_dr002=ir2["E"], om=ir["om"],
                             abw_dr001=ir["E"] / 82.13970757077503 - 1.0, abw_dr002=ir2["E"] / 82.13970757077503 - 1.0)
        print("extern", out["extern"], flush=True)
    for Q in a.Q:
        f0, ir0, rad0 = radial_ref(cache, Q, 0.0)
        for g4 in a.g4:
            for name, n in RICHTUNGEN:
                nn = np.array(n) / np.linalg.norm(n)
                geff = g4 * float(np.sum(nn ** 4))
                fr, irr, _ = radial_ref(cache, Q, geff)
                fr2, irr2, _ = radial_ref(cache, Q, geff, dr=0.02)
                psi = np.zeros((3, G.N, G.N), complex)
                base = profil_2d(G, rad0, f0)
                for k in range(3):
                    if nn[k] > 0:
                        psi[k] = nn[k] * base
                Qa = Q * nn ** 2
                psi, info = fluss(G, psi, Qa, g4, nmax=a.nmax, tol=a.tol, wand=a.wand)
                E, d = energie_Q(G, psi, Qa, g4)
                n2 = psi.real ** 2 + psi.imag ** 2
                z = dict(Q=Q, g4=g4, richtung=name, n=nn.tolist(), sum_n4=float(np.sum(nn ** 4)), g_eff=geff,
                         E=E, om=d["om"], status=info["status"], it=info["it"], res=info["verlauf"][-1][2],
                         sek=info["sek"], E_rad=irr["E"], om_rad=irr["om"], E_rad_dr002=irr2["E"],
                         rad_status=irr["status"], rad_res=irr["res"], abw=E / irr["E"] - 1.0,
                         R_halb=r_halb_2d(G, n2.sum(0)), R_halb_rad=irr["R_halb"])
                out["zustaende"].append(z)
                print(f"Q={Q} g4={g4} {name} geff={geff:.5f} E={E:.8f} E_rad={irr['E']:.8f} abw={z['abw']:.2e} "
                      f"om={d['om']} it={info['it']} res={z['res']:.1e} {info['status']} "
                      f"t={time.time() - t0:.0f}s rss={maxrss_mb():.0f}MB", flush=True)
                out["sek"] = time.time() - t0
                schreibe(a.out, out)
    for key, (f, ir, rad) in cache.items():
        out["radial"].append(dict(Q=key[0], g=key[1], dr=key[2], E=ir["E"], om=ir["om"], R_halb=ir["R_halb"],
                                  status=ir["status"], res=ir["res"], it=ir["it"]))
    out["sek"] = time.time() - t0
    out["maxrss_mb"] = maxrss_mb()
    out["ende_utc"] = jetzt()
    schreibe(a.out, out)


# ------------------------------------------------------------------ Modus b: zwei Q-Baelle in Ruhe im Abstand d
def modus_b(a):
    t0 = time.time()
    G = Gitter(a.N, a.L)
    rad = Radial()
    g4, Q1 = a.g4[0], a.Q1
    psi1, ball = ein_pol_ball(G, rad, g4, Q1)
    E1 = ball["E"]
    R = ball["R_halb"]
    F1 = G.fft(psi1)
    print("ball", ball, f"t={time.time() - t0:.0f}s", flush=True)
    out = {"modus": "b", "N": a.N, "L": a.L, "h": G.h, "g4": g4, "Q1": Q1, "ball": ball, "start_utc": jetzt(),
           "eingespannt": [], "relaxiert": []}
    z3 = np.zeros((G.N, G.N), complex)
    for x in a.dR:
        d = x * R
        A = G.shiftF(F1, 0.5 * d, 0.0)
        B = G.shiftF(F1, -0.5 * d, 0.0)
        P = np.stack([A + B, z3, z3])
        Es0 = energie_Q(G, P, [2.0 * Q1, 0.0, 0.0], g4)[0] - 2.0 * E1
        P = np.stack([A - B, z3, z3])
        Espi = energie_Q(G, P, [2.0 * Q1, 0.0, 0.0], g4)[0] - 2.0 * E1
        P = np.stack([A, B, z3])
        Ev = energie_Q(G, P, [Q1, Q1, 0.0], g4)[0] - 2.0 * E1
        rho = d / SQ3
        P = np.stack([G.shiftF(F1, rho * math.cos(0.5 * math.pi + 2.0 * math.pi * k / 3.0),
                               rho * math.sin(0.5 * math.pi + 2.0 * math.pi * k / 3.0)) for k in range(3)])
        Et = energie_Q(G, P, [Q1, Q1, Q1], g4)[0] - 3.0 * E1
        out["eingespannt"].append(dict(d_R=x, d=d, gleich_phase=Es0, gleich_gegen=Espi, verschieden=Ev,
                                       dreieck_verschieden=Et))
        print(f"eingespannt d/R={x} fertig t={time.time() - t0:.0f}s", flush=True)
        schreibe(a.out, out)
    for x in a.dR_relax:
        d = x * R
        A = G.shiftF(F1, 0.5 * d, 0.0)
        B = G.shiftF(F1, -0.5 * d, 0.0)
        P = np.stack([A, B, z3])
        Qv = np.array([Q1, Q1, 0.0])
        Pr, info = fluss(G, P, Qv, g4, nmax=a.nmax_relax, tolE=a.tolE, pins=[(0.5 * d, 0.0), (-0.5 * d, 0.0), None],
                         wand=a.wand_relax)
        E, dd = energie_Q(G, Pr, Qv, g4)
        sp = schwerpunkte(G, Pr.real ** 2 + Pr.imag ** 2)
        out["relaxiert"].append(dict(d_R=x, d=d, verschieden=E - 2.0 * E1, status=info["status"], it=info["it"],
                                     sek=info["sek"], schwerpunkte=sp, om=dd["om"],
                                     E_verlauf_letzte=info["verlauf"][-3:]))
        print(f"relaxiert d/R={x} {info['status']} it={info['it']} t={time.time() - t0:.0f}s", flush=True)
        schreibe(a.out, out)
    out["sek"] = time.time() - t0
    out["maxrss_mb"] = maxrss_mb()
    out["ende_utc"] = jetzt()
    schreibe(a.out, out)


# ------------------------------------------------------------------ Modus c: Dreier aus drei Polen
def lokal_anteil(G, n2, Rk):
    st = n2.sum(0)
    Xt = float(np.sum(G.X * st) / st.sum())
    Yt = float(np.sum(G.Y * st) / st.sum())
    inside = ((G.X - Xt) ** 2 + (G.Y - Yt) ** 2) < Rk * Rk
    return [float((n2[k] * inside).sum() / n2[k].sum()) for k in range(n2.shape[0])], [Xt, Yt]


def paarabstaende(sp):
    out = []
    for i, j in ((0, 1), (0, 2), (1, 2)):
        out.append(float(math.hypot(sp[i][0] - sp[j][0], sp[i][1] - sp[j][1])))
    return out


def modus_c(a):
    t0 = time.time()
    G = Gitter(a.N, a.L)
    rad = Radial()
    g4, Q1 = a.g4[0], a.Q1
    psi1, ball = ein_pol_ball(G, rad, g4, Q1)
    E1, R, om1 = ball["E"], ball["R_halb"], ball["om"]
    F1 = G.fft(psi1)
    d0 = a.dfak * R
    rho = d0 / SQ3
    Rk = rho + a.rkfak * R
    pos = [(rho * math.cos(0.5 * math.pi + 2.0 * math.pi * k / 3.0),
            rho * math.sin(0.5 * math.pi + 2.0 * math.pi * k / 3.0)) for k in range(3)]
    P = np.stack([G.shiftF(F1, pos[k][0], pos[k][1]) for k in range(3)])
    Q = np.array([Q1, Q1, Q1])
    E_ein = energie_Q(G, P, Q, g4)[0]
    out = {"modus": "c", "N": a.N, "L": a.L, "h": G.h, "g4": g4, "Q1": Q1, "ball": ball, "d0": d0, "rho": rho,
           "R_K": Rk, "pos": pos, "E_eingespannt": E_ein, "E_drei_getrennt": 3.0 * E1, "start_utc": jetzt()}
    print("ball", ball, f"d0={d0:.4f} R_K={Rk:.4f} t={time.time() - t0:.0f}s", flush=True)
    schreibe(a.out, out)
    snaps = {}
    # (i) Gradientenfluss ohne Stifte vom eingespannten Dreieck (oder Endzustand eines frueheren Laufs laden)
    Pf = None
    if a.nfluss > 0 or a.lade_fluss:
        if a.lade_fluss:
            Pf = np.load(a.lade_fluss)
            info = dict(status="geladen:" + os.path.basename(a.lade_fluss), it=0, sek=0.0,
                        verlauf=[[0, energie_Q(G, Pf, Q, g4)[0], residuum(G, Pf, Q, g4)]])
        else:
            Pf, info = fluss(G, P, Q, g4, nmax=a.nfluss, tol=a.tol, alle=50, wand=a.wand_fluss)
            np.save(a.out.replace(".json", "_fluss.npy"), Pf)
        Ef, df = energie_Q(G, Pf, Q, g4)
        n2f = Pf.real ** 2 + Pf.imag ** 2
        sp = schwerpunkte(G, n2f)
        anteil, Xt = lokal_anteil(G, n2f, Rk)
        out["fluss"] = dict(E_ende=Ef, B=3.0 * E1 - Ef, status=info["status"], it=info["it"], sek=info["sek"],
                            res=info["verlauf"][-1][2], om=df["om"], schwerpunkte=sp, paarabstand=paarabstaende(sp),
                            lokal_anteil=anteil, Xt=Xt, S_max=float(n2f.sum(0).max()),
                            verlauf=info["verlauf"][::max(1, len(info["verlauf"]) // 200)])
        snaps["fluss_ende"] = n2f[:, ::2, ::2].astype(np.float32)
        print("fluss", {k: v for k, v in out["fluss"].items() if k != "verlauf"}, f"t={time.time() - t0:.0f}s",
              flush=True)
        schreibe(a.out, out)
    # (ii) Zeitentwicklung vom eingespannten Dreieck (c1) bzw. vom Flussendzustand (c2), Rauschen eps
    laeufe = []
    if a.T > 0 and "c1" in a.laeufe:
        laeufe.append(("c1", P, [om1, om1, om1]))
    if a.T > 0 and "c2" in a.laeufe and Pf is not None:
        laeufe.append(("c2", Pf, df["om"]))
    out["laeufe"] = {}
    for name, P0, oms in laeufe:
        S0 = (P0.real ** 2 + P0.imag ** 2).sum(0)
        env = np.sqrt(S0)
        eta = rauschfeld(G, a.saat)
        eta2 = rauschfeld(G, a.saat + 1000)
        phi = P0 + a.eps * eta * env[None]
        pi = np.stack([1j * oms[k] * P0[k] for k in range(3)]) + a.eps * om1 * eta2 * env[None]
        rec, status, sn, phiE, piE = entwickle(G, phi, pi, g4, a.dt, a.T, a.dmess, Rk, schnapp_t=a.schnapp,
                                               wand=a.wand_t)
        for ts, arr in sn.items():
            snaps["%s_t%g" % (name, ts)] = arr
        E0 = rec[0, 1]
        dE = float(np.abs(rec[:, 1] - E0).max() / E0)
        dQ = float(max(np.abs(rec[:, 2 + k] - rec[0, 2 + k]).max() / abs(rec[0, 2 + k]) for k in range(3)))
        out["laeufe"][name] = dict(status=status, spalten=SPALTEN, reihe=rec.tolist(), dE_rel=dE, dQ_rel=dQ,
                                   saat=a.saat, eps=a.eps, dt=a.dt, T=a.T, om_start=list(map(float, oms)))
        print(f"{name}: {status} dE={dE:.2e} dQ={dQ:.2e} t_end={rec[-1, 0]} t={time.time() - t0:.0f}s "
              f"rss={maxrss_mb():.0f}MB", flush=True)
        schreibe(a.out, out)
    if snaps:
        np.savez_compressed(a.out.replace(".json", "_bilder.npz"), x=G.x[::2], **snaps)
    out["sek"] = time.time() - t0
    out["maxrss_mb"] = maxrss_mb()
    out["ende_utc"] = jetzt()
    schreibe(a.out, out)


# ------------------------------------------------------------------ Rauchlauf: Zeit, Speicher, QD0-Kontrolle
def modus_rauch(a):
    t0 = time.time()
    out = {"modus": "rauch", "start_utc": jetzt(),
           "versionen": dict(numpy=np.__version__, scipy=scipy.__version__, python=sys.version.split()[0]),
           "threads_env": {k: os.environ.get(k) for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS")}}
    G = Gitter(a.N, a.L)
    x = np.random.default_rng(0).standard_normal((G.N, G.N)) + 0j
    t1 = time.time()
    for _ in range(50):
        G.ifft(G.fft(x))
    out["ms_fft_paar"] = (time.time() - t1) / 50 * 1e3
    ph = np.stack([x, x, x]) * 0.1
    t1 = time.time()
    for _ in range(20):
        kraft(G, ph, 0.1, [0, 1, 2])
    out["ms_kraft_3k"] = (time.time() - t1) / 20 * 1e3
    print("zeiten", out["ms_fft_paar"], out["ms_kraft_3k"], flush=True)
    schreibe(a.out, out)
    # externer Abgleich radial (g = 0, Q = 100) mit QB-BS-2D
    cache = {}
    f, ir, _ = radial_ref(cache, 100.0, 0.0)
    f2, ir2, _ = radial_ref(cache, 100.0, 0.0, dr=0.02)
    out["extern"] = dict(E_quelle=82.13970757077503, E_dr001=ir["E"], E_dr002=ir2["E"], sek=ir["sek"], it=ir["it"],
                         status=ir["status"], abw=ir["E"] / 82.13970757077503 - 1.0)
    print("extern", out["extern"], flush=True)
    schreibe(a.out, out)
    # QD0-Kontrolle (Teilmenge): Q = 60, g4 = +0.1 und -0.1, drei Richtungen
    out["qd0"] = []
    f0, ir0, rad0 = radial_ref(cache, 60.0, 0.0)
    for g4 in (0.1, -0.1):
        for name, n in RICHTUNGEN:
            nn = np.array(n) / np.linalg.norm(n)
            geff = g4 * float(np.sum(nn ** 4))
            fr, irr, _ = radial_ref(cache, 60.0, geff)
            psi = np.zeros((3, G.N, G.N), complex)
            base = profil_2d(G, rad0, f0)
            for k in range(3):
                if nn[k] > 0:
                    psi[k] = nn[k] * base
            Qa = 60.0 * nn ** 2
            psi, info = fluss(G, psi, Qa, g4, nmax=a.nmax, tol=a.tol, wand=a.wand)
            E, d = energie_Q(G, psi, Qa, g4)
            z = dict(g4=g4, richtung=name, g_eff=geff, E=E, E_rad=irr["E"], abw=E / irr["E"] - 1.0, om=d["om"],
                     it=info["it"], status=info["status"], res=info["verlauf"][-1][2], sek=info["sek"],
                     ms_je_schritt=1e3 * info["sek"] / max(info["it"], 1),
                     verlauf=info["verlauf"][::max(1, len(info["verlauf"]) // 40)])
            out["qd0"].append(z)
            print(f"QD0 g4={g4} {name} abw={z['abw']:.2e} it={info['it']} res={z['res']:.1e} {info['status']} "
                  f"ms/schritt={z['ms_je_schritt']:.1f} t={time.time() - t0:.0f}s", flush=True)
            schreibe(a.out, out)
    # Einpolball g4 = +0.1, Q1 = 60: Aufbau (R_halb, R_rms, om) und Gitterprobe N = 320 bei gleichem L
    rad = Radial()
    psi1, ball = ein_pol_ball(G, rad, 0.1, 60.0)
    G2 = Gitter(320, a.L)
    psi2, ball2 = ein_pol_ball(G2, rad, 0.1, 60.0)
    out["ball_p01"] = ball
    out["ball_p01_N320"] = ball2
    out["gitterprobe_E_rel"] = ball2["E"] / ball["E"] - 1.0
    print("ball", ball, "N320", ball2, flush=True)
    schreibe(a.out, out)
    # kurze Zeitentwicklung des Einpolballs (Erhaltung, ms je Schritt) und Zeitmessung mit drei Komponenten
    P = np.stack([psi1, 0 * psi1, 0 * psi1])
    pi = 1j * ball["om"] * P
    t1 = time.time()
    rec, status, sn, _, _ = entwickle(G, P, pi, 0.1, a.dt, 10.0, 0.5, 3.0 * ball["R_halb"])
    sek = time.time() - t1
    out["zeit_einpol"] = dict(T=10.0, dt=a.dt, sek=sek, ms_je_schritt=1e3 * sek / (10.0 / a.dt), status=status,
                              dE=float(np.abs(rec[:, 1] - rec[0, 1]).max() / rec[0, 1]),
                              dQ=float(np.abs(rec[:, 2] - rec[0, 2]).max() / rec[0, 2]),
                              drift=float(math.hypot(rec[-1, 8] - rec[0, 8], rec[-1, 11] - rec[0, 11])))
    print("zeit_einpol", out["zeit_einpol"], flush=True)
    m = np.stack([psi1, psi1, psi1]) / SQ3   # nur Zeitmessung mit drei aktiven Komponenten (kein Gleichgewicht)
    t1 = time.time()
    rec, status, sn, _, _ = entwickle(G, m, 1j * ball["om"] * m, 0.1, a.dt, 2.0, 0.5, 3.0 * ball["R_halb"])
    sek = time.time() - t1
    out["zeit_3k"] = dict(T=2.0, sek=sek, ms_je_schritt=1e3 * sek / (2.0 / a.dt), status=status)
    print("zeit_3k", out["zeit_3k"], flush=True)
    out["sek"] = time.time() - t0
    out["maxrss_mb"] = maxrss_mb()
    out["ende_utc"] = jetzt()
    schreibe(a.out, out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("modus", choices=["rauch", "a", "b", "c"])
    ap.add_argument("--out", required=True)
    ap.add_argument("--N", type=int, default=256)
    ap.add_argument("--L", type=float, default=64.0)
    ap.add_argument("--Q", type=lambda s: [float(v) for v in s.split(",")], default=[60.0])
    ap.add_argument("--Q1", type=float, default=60.0)
    ap.add_argument("--g4", type=lambda s: [float(v) for v in s.split(",")], default=[-0.1, 0.0, 0.1])
    ap.add_argument("--extern", action="store_true")
    ap.add_argument("--nmax", type=int, default=8000)
    ap.add_argument("--tol", type=float, default=1e-7)
    ap.add_argument("--wand", type=float, default=150.0)
    ap.add_argument("--dR", type=lambda s: [float(v) for v in s.split(",")],
                    default=[0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.5, 4.0, 5.0, 6.0])
    ap.add_argument("--dR_relax", type=lambda s: [float(v) for v in s.split(",")], default=[1.5, 2.0, 2.5, 3.0, 4.0])
    ap.add_argument("--nmax_relax", type=int, default=4000)
    ap.add_argument("--tolE", type=float, default=1e-11)
    ap.add_argument("--wand_relax", type=float, default=80.0)
    ap.add_argument("--dfak", type=float, default=2.0)
    ap.add_argument("--rkfak", type=float, default=3.0)
    ap.add_argument("--nfluss", type=int, default=8000)
    ap.add_argument("--wand_fluss", type=float, default=170.0)
    ap.add_argument("--T", type=float, default=200.0)
    ap.add_argument("--dt", type=float, default=0.025)
    ap.add_argument("--dmess", type=float, default=0.5)
    ap.add_argument("--eps", type=float, default=1e-3)
    ap.add_argument("--saat", type=int, default=1)
    ap.add_argument("--laeufe", type=lambda s: s.split(","), default=["c1"])
    ap.add_argument("--lade_fluss", default="")
    ap.add_argument("--schnapp", type=lambda s: [float(v) for v in s.split(",")], default=[0.0, 100.0, 200.0])
    ap.add_argument("--wand_t", type=float, default=200.0)
    a = ap.parse_args()
    t0 = time.time()
    {"rauch": modus_rauch, "a": modus_a, "b": modus_b, "c": modus_c}[a.modus](a)
    print("geschrieben", a.out, f"{time.time() - t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
