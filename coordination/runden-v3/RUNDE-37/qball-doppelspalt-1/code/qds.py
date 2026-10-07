#!/usr/bin/env python3
# QBALL-DOPPELSPALT-1 (Runde 45/46): klassischer 2D-Q-Ball des Projektmodells (Papier I, beta = 1/2) und linearer
# Klein-Gordon-Kontrollarm an Einfach-, Doppel- und Dreifachspalt.
#   L = |d_t phi|^2 - |grad phi|^2 - U(S) - V_w(x, y) S,  S = |phi|^2,  U(S) = S - S^2 + BETA S^3,  BETA = 1/2, m = 1.
#   Energie E = int [|pi|^2 + |grad phi|^2 + U(S) + V_w S],  Ladung Q = 2 int Im(conj(phi) pi),  pi = d_t phi.
#   Kontrollarm: U(S) -> S (linear, m = 1), sonst gleich.
# Radiales Profil: Klasse Radial kopiert aus QBALL-DREIPOL-2 (code/dreipol2.py, eingefroren 20261004-182806), g = 0.
# Gitter: isotroper 9-Punkt-Laplace (conv2d, Feld ausserhalb des Gebiets = 0, Schwammschicht innen), float32,
# torch/CUDA. Zeitschritt: Geschwindigkeits-Verlet wie DREIPOL-2 (entwickle). Kein CPU-Fallback.
import sys, os, json, math, time, argparse, resource
import numpy as np
import scipy
from scipy.linalg import solve_banded
from scipy import ndimage
import torch
import torch.nn.functional as TF

BETA = 0.5
DEV = None
GERAET = None
# Q(omega) aus DIM-LEITER-QBALL-1 (lauf-69/d2.json, feines Gitter h = 0,0125): om2 = 0,64 bzw. 0,81
QTAB = {"0.8": 38.54342068550012, "0.9": 15.8188115197775}
LX, LY = 128.0, 64.0
X_W0, X_W1 = 0.0, 2.0     # Wand: Dicke 2 (Halbwertskanten)
EPS_W = 0.25              # Kantenbreite (tanh) von Wand und Spalten, fest (unabhaengig von h)
V_W = 4.0
X0 = -15.0                # Startort des Ballmittelpunkts
L_WEG = 40.0              # Laufzeit T = L_WEG / v
X_FLUSS = 3.0             # Flussebene hinter der Wand
SCHWAMM = 8.0             # Breite der Schwammschicht an allen vier Raendern
GAMMA0 = 1.0              # Daempfung gamma = GAMMA0 * s^2, s = Eindringtiefe / SCHWAMM
C_KERN = 0.05             # Kernschwelle: S >= C_KERN * S0 (S0 = |phi(0)|^2 des ruhenden Balls)
C_ZUORD = 1e-4            # zugeordnet werden Punkte mit S >= C_ZUORD * S0 ...
R_ZUORD = 3.0             # ... im Abstand <= R_ZUORD * R vom naechsten Kernpunkt
Q_MIN_STUECK = 0.02       # Stuecke unter 2 % Q werden nicht gefuehrt
Q_GROSS = 0.10            # "Stueck" im Sinn der Karte: >= 10 % von Q
WINKEL_X_AB = 3.0         # Winkelverteilung der Ladung: nur x > X_W1 + 3
NBIN = 90                 # 2-Grad-Bins von -90 bis 90 Grad


def geraet():
    global DEV
    if not torch.cuda.is_available():
        raise SystemExit("CUDA nicht verfuegbar: Abbruch (kein CPU-Fallback)")
    DEV = torch.device("cuda")
    torch.backends.cudnn.benchmark = True
    return dict(name=torch.cuda.get_device_name(0), torch=torch.__version__, cuda=torch.version.cuda,
                visible=os.environ.get("CUDA_VISIBLE_DEVICES"), numpy=np.__version__, scipy=scipy.__version__,
                python=sys.version.split()[0])


def U0(S):
    return S - S * S + BETA * S ** 3


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


def gpu_mb():
    return torch.cuda.max_memory_allocated() / 2 ** 20


# ------------------------------------------------------------------ radialer Bezug (kopiert aus DREIPOL-2, g = 0)
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
        rand = float(np.sum((self.w * f * f)[self.r > self.rmax - 5.0]) / np.sum(self.w * f * f))
        return f, dict(E=E, om=om, Lam=Lam, res=res, it=it, status=status, R_halb=self.r_halb(f), f0=float(f[0]),
                       dr=self.dr, rmax=self.rmax, Q=Q, g=g, d=self.d, rand_anteil=rand, sek=time.time() - t0)


# ------------------------------------------------------------------ Gitter (9-Punkt-Laplace, Nullrand, GPU)
class Gitter:
    def __init__(self, h):
        self.h = float(h)
        self.Nx, self.Ny = int(round(LX / h)), int(round(LY / h))
        self.x = -0.5 * LX + self.h * np.arange(self.Nx)
        self.y = -0.5 * LY + self.h * np.arange(self.Ny)
        self.dA = self.h * self.h
        Xn, Yn = np.meshgrid(self.x, self.y, indexing="ij")
        self.Xn, self.Yn = Xn, Yn
        self.X = torch.tensor(Xn, dtype=torch.float32, device=DEV)
        self.Y = torch.tensor(Yn, dtype=torch.float32, device=DEV)
        k = np.array([[1.0, 4.0, 1.0], [4.0, -20.0, 4.0], [1.0, 4.0, 1.0]]) / (6.0 * self.h * self.h)
        self.ker = torch.tensor(k, dtype=torch.float32, device=DEV).view(1, 1, 3, 3).repeat(2, 1, 1, 1).contiguous()
        sx = np.maximum(0.0, np.abs(Xn) - (0.5 * LX - SCHWAMM)) / SCHWAMM
        sy = np.maximum(0.0, np.abs(Yn) - (0.5 * LY - SCHWAMM)) / SCHWAMM
        self.gam = GAMMA0 * np.maximum(sx, sy) ** 2
        self.innen = (self.gam == 0.0)
        self.i_fluss = int(np.argmin(np.abs(self.x - X_FLUSS)))

    def lap(self, P):
        return TF.conv2d(P, self.ker, padding=1, groups=2)


def stufe(z, eps=EPS_W):
    return 0.5 * (1.0 + np.tanh(z / eps))


def spaltmitten(nspalt, w, d):
    """d = Kantenabstand (Breite des Stegs zwischen benachbarten Spalten), w = Spaltbreite (PLAN Abschn. 3)."""
    p = d + w
    if nspalt == 1:
        return {"A": 0.0}
    if nspalt == 2:
        return {"A": -0.5 * p, "B": 0.5 * p}
    if nspalt == 3:
        return {"A": -p, "B": 0.0, "C": p}
    raise ValueError(nspalt)


def wandpotential(G, mitten, offen, w):
    wx = stufe(G.Xn - X_W0) * stufe(X_W1 - G.Xn)
    sy = np.zeros_like(G.Yn)
    for s in offen:
        yc = mitten[s]
        sy = sy + stufe(G.Yn - (yc - 0.5 * w)) * stufe((yc + 0.5 * w) - G.Yn)
    return V_W * wx * np.clip(1.0 - sy, 0.0, 1.0)


def lade_profil(pfad, om):
    z = np.load(pfad)
    return dict(r=z["r_" + om], f=z["f_" + om], fp=z["fp_" + om])


def ball_felder(G, prof, om, v, x0, yb):
    """Lorentz-geboosteter Ball (Konvention phi = f e^{+i om t}): phi = f(r') e^{-i om gam v (x - x0)},
    pi = -gam v f'(r') X'/r' e^{...} + i om gam phi, X' = gam (x - x0), r' = sqrt(X'^2 + (y - yb)^2)."""
    gam = 1.0 / math.sqrt(1.0 - v * v)
    Xp = gam * (G.Xn - x0)
    Yp = G.Yn - yb
    rp = np.sqrt(Xp * Xp + Yp * Yp)
    fv = np.interp(rp, prof["r"], prof["f"], right=0.0)
    fpv = np.interp(rp, prof["r"], prof["fp"], right=0.0)
    ph = -om * gam * v * (G.Xn - x0)
    e = np.exp(1j * ph)
    with np.errstate(invalid="ignore", divide="ignore"):
        ratio = np.where(rp > 1e-9, Xp / np.where(rp > 1e-9, rp, 1.0), 0.0)
    phi = fv * e
    pi = (-gam * v * fpv * ratio + 1j * om * gam * fv) * e
    return phi, pi


def kg_felder(G, Rh, v, x0, yb):
    """Linearer Kontrollarm: Gauss-Paket mit |phi|^2 = exp(-r^2/sig^2), Halbwertsradius Rh wie der Ball,
    Traegerwellenzahl k = gam v (Gruppengeschwindigkeit v), rein positive Frequenz bezueglich des diskreten
    9-Punkt-Operators, normiert auf Q = 1."""
    gam = 1.0 / math.sqrt(1.0 - v * v)
    k = gam * v
    sig = Rh / math.sqrt(math.log(2.0))
    r2 = (G.Xn - x0) ** 2 + (G.Yn - yb) ** 2
    phi = np.exp(-r2 / (2.0 * sig * sig)) * np.exp(-1j * k * (G.Xn - x0))
    kx = 2.0 * np.pi * np.fft.fftfreq(G.Nx, d=G.h)
    ky = 2.0 * np.pi * np.fft.fftfreq(G.Ny, d=G.h)
    a = kx[:, None] * G.h
    b = ky[None, :] * G.h
    lam = (20.0 - 8.0 * (np.cos(a) + np.cos(b)) - 4.0 * np.cos(a) * np.cos(b)) / (6.0 * G.h * G.h)
    pi = np.fft.ifft2(1j * np.sqrt(1.0 + lam) * np.fft.fft2(phi))
    Q = 2.0 * float(np.sum(np.imag(np.conj(phi) * pi))) * G.dA
    s = 1.0 / math.sqrt(Q)
    return phi * s, pi * s


def zu_torch(liste):  # nur Ruhetest (B = 1)
    """Liste komplexer (Nx, Ny)-Felder -> (B, 2, Nx, Ny) float32 auf der GPU."""
    arr = np.stack([np.stack([z.real, z.imag]) for z in liste]).astype(np.float32)
    return torch.tensor(arr, device=DEV)


# ------------------------------------------------------------------ Zeitentwicklung
class Lauf:
    def __init__(self, G, Vc, ny, nichtlinear, dt):
        self.G, self.ny, self.nl, self.dt = G, ny, nichtlinear, dt
        self.C = Vc.shape[0]
        self.Vc = torch.tensor(Vc, dtype=torch.float32, device=DEV).view(self.C, 1, 1, G.Nx, G.Ny)
        self.W1 = (1.0 + self.Vc)
        self.damp = torch.tensor(np.exp(-G.gam * dt), dtype=torch.float32, device=DEV).view(1, 1, G.Nx, G.Ny)

    def kraft(self, P):
        G = self.G
        L = G.lap(P)
        Pv = P.view(self.C, self.ny, 2, G.Nx, G.Ny)
        Lv = L.view(self.C, self.ny, 2, G.Nx, G.Ny)
        if self.nl:
            S = Pv[:, :, 0:1] * Pv[:, :, 0:1]
            S.addcmul_(Pv[:, :, 1:2], Pv[:, :, 1:2])
            A = S * (3.0 * BETA)
            A.sub_(2.0)
            W = torch.addcmul(self.W1, S, A)
            Lv.addcmul_(W, Pv, value=-1.0)
        else:
            Lv.addcmul_(self.W1, Pv, value=-1.0)
        return L

    def energie(self, P, Pi):
        """Diskrete Energie je Element (Summation durch Teile mit dem Gitter-Laplace); float64-Summen."""
        G = self.G
        L = G.lap(P)
        Pv = P.view(self.C, self.ny, 2, G.Nx, G.Ny)
        S = (Pv * Pv).sum(2)
        if self.nl:
            pot = S - S * S + BETA * S * S * S
        else:
            pot = S.clone()
        pot = pot + self.Vc[:, :, 0] * S
        e = (Pi * Pi).sum(1) - (P * L).sum(1) + pot.view(-1, G.Nx, G.Ny)
        return (e.double().sum(dim=(1, 2)) * G.dA).cpu().numpy()

    def ladungsdichte(self, P, Pi):
        return 2.0 * (P[:, 0] * Pi[:, 1] - P[:, 1] * Pi[:, 0])


def zonen_matrix(G, mitten):
    """y-Zonen der Flussebene: jeder Punkt gehoert zum naechsten Spaltmittelpunkt (Voronoi in y)."""
    namen = sorted(mitten.keys())
    yc = np.array([mitten[s] for s in namen])
    idx = np.argmin(np.abs(G.y[:, None] - yc[None, :]), axis=1)
    Z = np.zeros((G.Ny, len(namen)), dtype=np.float32)
    Z[np.arange(G.Ny), idx] = 1.0
    return namen, torch.tensor(Z, device=DEV)


def winkel_bins(G):
    alpha = np.degrees(np.arctan2(G.Yn, G.Xn - X_W1))
    ok = (G.Xn > X_W1 + WINKEL_X_AB) & G.innen
    b = np.clip(np.floor((alpha + 90.0) / (180.0 / NBIN)).astype(np.int64), 0, NBIN - 1)
    b = np.where(ok, b, NBIN)  # Muellbin
    return torch.tensor(b.reshape(-1), device=DEV)


def stuecke(G, S, rho, px, py, S0, R, Q0):
    """Stuecke am Ende: Kerne = Zusammenhangskomponenten (8er) von S >= C_KERN S0; jeder Punkt mit S >= C_ZUORD S0
    im Abstand <= R_ZUORD R geht an den naechsten Kernpunkt."""
    kern = S >= C_KERN * S0
    lab, n = ndimage.label(kern, structure=np.ones((3, 3), dtype=int))
    if n == 0:
        return []
    dist, (ii, jj) = ndimage.distance_transform_edt(~kern, return_indices=True)
    zl = lab[ii, jj]
    ok = (S >= C_ZUORD * S0) & (dist * G.h <= R_ZUORD * R)
    zl = np.where(ok, zl, 0)
    out = []
    idx = np.arange(1, n + 1)
    q = ndimage.sum(rho, zl, idx) * G.dA
    xs = ndimage.sum(rho * G.Xn, zl, idx) * G.dA
    ys = ndimage.sum(rho * G.Yn, zl, idx) * G.dA
    Px = ndimage.sum(px, zl, idx) * G.dA
    Py = ndimage.sum(py, zl, idx) * G.dA
    Smax = ndimage.maximum(S, lab, idx)
    for k in range(n):
        if q[k] < Q_MIN_STUECK * Q0:
            continue
        out.append(dict(q=float(q[k] / Q0), x=float(xs[k] / q[k]), y=float(ys[k] / q[k]), Px=float(Px[k]),
                        Py=float(Py[k]), Smax=float(Smax[k] / S0)))
    out.sort(key=lambda s: -s["q"])
    return out


def klasse(st, R, fluesse_rel):
    """Ausgangsklasse (PLAN Abschn. 5)."""
    durch = [s for s in st if s["x"] > X_W1 + 0.5 * R and s["q"] >= Q_GROSS]
    zurueck = [s for s in st if s["x"] < X_W0 - 0.5 * R and s["q"] >= Q_GROSS]
    n_spalt = int(sum(1 for f in fluesse_rel if f >= Q_GROSS))
    if len(durch) >= 2:
        k = "geteilt"
    elif len(durch) == 1:
        k = "geteilt_wiedervereint" if n_spalt >= 2 else "ein_spalt"
    elif len(zurueck) >= 1:
        k = "reflektiert"
    elif len(st) > 0:
        k = "steckt"
    else:
        k = "zerflossen"
    theta = None
    if durch:
        s = durch[0]
        theta = math.degrees(math.atan2(s["Py"], s["Px"]))
    return dict(klasse=k, n_durch=len(durch), n_zurueck=len(zurueck), n_spalt_10=n_spalt, theta=theta,
                teilreflexion=bool(durch and zurueck))


def fahre(G, lauf, P, Pi, T, zonen, mess_dt=1.0, wand=540.0, verlauf=False):
    dt = lauf.dt
    nsteps = int(round(T / dt))
    nsub = max(1, int(round(mess_dt / dt)))
    namen, Z = zonen
    i = G.i_fluss
    F = lauf.kraft(P)
    flux = torch.zeros((P.shape[0], Z.shape[1]), dtype=torch.float64, device=DEV)
    E0 = lauf.energie(P, Pi)
    rho = lauf.ladungsdichte(P, Pi)
    Q0 = (rho.double().sum(dim=(1, 2)) * G.dA).cpu().numpy()
    reihe = []
    t0 = time.time()
    status = "fertig"
    rechts = (G.X > X_W1).float()
    for k in range(1, nsteps + 1):
        Pi.add_(F, alpha=0.5 * dt)
        P.add_(Pi, alpha=dt)
        F = lauf.kraft(P)
        Pi.add_(F, alpha=0.5 * dt)
        Pi.mul_(lauf.damp)
        d = (P[:, :, i + 1, :] - P[:, :, i - 1, :]) * (0.5 / G.h)
        jx = -2.0 * (P[:, 0, i, :] * d[:, 1] - P[:, 1, i, :] * d[:, 0])
        flux += (jx @ Z).double() * (G.h * dt)
        if verlauf and k % nsub == 0:
            rho = lauf.ladungsdichte(P, Pi)
            q = (rho.double().sum(dim=(1, 2)) * G.dA).cpu().numpy()
            qr = ((rho * rechts).double().sum(dim=(1, 2)) * G.dA).cpu().numpy()
            Smax = (P * P).sum(1).amax(dim=(1, 2)).cpu().numpy()
            reihe.append([k * dt, q.tolist(), qr.tolist(), Smax.tolist()])
        if k % 500 == 0:
            if not bool(torch.isfinite(P).all()):
                status = "nicht_endlich"
                break
            if time.time() - t0 > wand:
                status = "wandzeit"
                break
    torch.cuda.synchronize()
    sek = time.time() - t0
    E1 = lauf.energie(P, Pi)
    return dict(status=status, schritte=k, sek=sek, ms_schritt=1e3 * sek / max(k, 1), E0=E0, E1=E1, Q0=Q0,
                flux=flux.cpu().numpy(), zonen=namen, reihe=reihe), P, Pi


def endanalyse(G, lauf, P, Pi, S0, R, Q0ball, wbins):
    """Je Element: Stuecke, Winkelverteilung der Ladung (x > X_W1 + 3), Ladung links/rechts."""
    rho = lauf.ladungsdichte(P, Pi)
    B = P.shape[0]
    hist = torch.zeros((B, NBIN + 1), dtype=torch.float64, device=DEV)
    hist.index_add_(1, wbins, rho.reshape(B, -1).double())
    hist = (hist[:, :NBIN] * G.dA / Q0ball).cpu().numpy()
    dxP = torch.zeros_like(P)
    dyP = torch.zeros_like(P)
    dxP[:, :, 1:-1, :] = (P[:, :, 2:, :] - P[:, :, :-2, :]) * (0.5 / G.h)
    dyP[:, :, :, 1:-1] = (P[:, :, :, 2:] - P[:, :, :, :-2]) * (0.5 / G.h)
    px = -2.0 * (Pi * dxP).sum(1)
    py = -2.0 * (Pi * dyP).sum(1)
    S = (P * P).sum(1)
    rechts = G.X > X_W1
    links = G.X < X_W0
    qr = ((rho * rechts).double().sum(dim=(1, 2)) * G.dA / Q0ball).cpu().numpy()
    ql = ((rho * links).double().sum(dim=(1, 2)) * G.dA / Q0ball).cpu().numpy()
    out = []
    for b in range(B):
        st = stuecke(G, S[b].cpu().numpy(), rho[b].cpu().numpy(), px[b].cpu().numpy(), py[b].cpu().numpy(), S0, R,
                     Q0ball)
        out.append(dict(stuecke=st, q_rechts=float(qr[b]), q_links=float(ql[b]), hist=[round(float(x), 7) for x in hist[b]]))
    return out


# ------------------------------------------------------------------ Modi
def modus_profil(a):
    t0 = time.time()
    rad = Radial(2, dr=0.01, rmax=60.0)
    out = {"modus": "profil", "geraet": GERAET, "start_utc": jetzt(), "QTAB": QTAB}
    arr = {}
    for om in ("0.8", "0.9"):
        Q = QTAB[om]
        f, info = rad.fluss(rad.start(Q, om=float(om)), Q, 0.0, wand=a.wand, tol=a.tol)
        fp = np.gradient(f, rad.r)
        arr["r_" + om] = rad.r
        arr["f_" + om] = f
        arr["fp_" + om] = fp
        info["kappa"] = math.sqrt(max(0.0, 1.0 - info["om"] ** 2))
        out[om] = info
        print(om, info, flush=True)
    np.savez(a.out.replace(".json", ".npz"), **arr)
    out["sek"] = time.time() - t0
    out["ende_utc"] = jetzt()
    schreibe(a.out, out)


def modus_bilanz(a):
    """Energiebilanz (Karte, Pflicht d): Spaltkosten E(Q1) + E(Q2) - E(Q) gegen (gamma - 1) E(Q).
    E(q) aus DIM-LEITER-QBALL-1 d2.json (fein); fuer q unter der Townes-Schranke (kein Ball) E_min(q) = q (m = 1)."""
    d2 = json.load(open(a.d2))
    pk = d2["ergebnisse"]["2"]["fein"]["punkte"]
    Qs = np.array([p["Q"] for p in pk])
    Es = np.array([p["E"] for p in pk])
    o = np.argsort(Qs)
    Qs, Es = Qs[o], Es[o]
    Qmin = float(Qs[0])

    def Emin(q):
        if q <= Qmin:
            return q
        return float(np.interp(q, Qs, Es))

    out = {"modus": "bilanz", "start_utc": jetzt(), "Q_townes_rand": Qmin, "je_omega": {}}
    for om in ("0.8", "0.9"):
        Q = QTAB[om]
        E = Emin(Q)
        xs = np.round(np.arange(0.10, 0.5001, 0.01), 4)
        kosten = [Emin(x * Q) + Emin((1 - x) * Q) - E for x in xs]
        j = int(np.argmin(kosten))
        zeile = dict(Q=Q, E=E, kosten=dict(zip([float(x) for x in xs], kosten)), kmin=float(kosten[j]),
                     x_kmin=float(xs[j]), k_halb=float(kosten[-1]), ekin={})
        for v in (0.2, 0.3, 0.45):
            g = 1.0 / math.sqrt(1 - v * v)
            ek = (g - 1.0) * E
            zeile["ekin"][str(v)] = dict(gamma=g, Ekin=ek, reicht_fuer_kmin=bool(ek >= kosten[j]),
                                         reicht_fuer_halb=bool(ek >= kosten[-1]),
                                         x_erlaubt=[float(x) for x, k in zip(xs, kosten) if ek >= k])
        out["je_omega"][om] = zeile
        print(om, {k: v for k, v in zeile.items() if k != "kosten"}, flush=True)
    schreibe(a.out, out)


def modus_ruhe(a):
    """Ruhetest ohne Spalt (Karte, Pflicht c): Ball in Ruhe bei (0, 0), T = a.T; dazu Fahrtest v = 0,45 ohne Wand."""
    t0 = time.time()
    pr = json.load(open(a.profil))
    out = {"modus": "ruhe", "geraet": GERAET, "start_utc": jetzt(), "dt": a.dt, "T": a.T, "je": {}}
    for om in a.omegas:
        prof = lade_profil(a.profil.replace(".json", ".npz"), om)
        R = pr[om]["R_halb"]
        omv = pr[om]["om"]
        S0 = pr[om]["f0"] ** 2
        for h in a.hs:
            G = Gitter(h)
            zon = zonen_matrix(G, {"A": 0.0})
            e = {}
            for name, v, x0, T in (("ruhe", 0.0, 0.0, a.T), ("fahrt", 0.45, X0, L_WEG / 0.45)):
                phi, pi = ball_felder(G, prof, omv, v, x0, 0.0)
                P, Pi = zu_torch([phi]), zu_torch([pi])
                lauf = Lauf(G, np.zeros((1, G.Nx, G.Ny)), 1, True, a.dt)
                r0 = dict(S_max=float((P * P).sum(1).max()) / S0)
                res, P, Pi = fahre(G, lauf, P, Pi, T, zon, verlauf=True, wand=a.wand)
                rho = lauf.ladungsdichte(P, Pi)[0]
                S = (P * P).sum(1)[0]
                q = float(rho.double().sum()) * G.dA
                xs = float((rho * G.X).double().sum()) * G.dA / q
                ys = float((rho * G.Y).double().sum()) * G.dA / q
                Q0 = float(res["Q0"][0])
                qs = [r[1][0] for r in res["reihe"]]
                gam = 1.0 / math.sqrt(1 - v * v)
                e[name] = dict(v=v, T=T, status=res["status"], ms_schritt=res["ms_schritt"], Q0=Q0,
                               Q_rad=pr[om]["Q"], E_rad=pr[om]["E"], E0=float(res["E0"][0]), E1=float(res["E1"][0]),
                               gamma_E_rad=gam * pr[om]["E"], Q_ende=q, dQ_rel=(q - Q0) / Q0,
                               dQ_rel_max=float(max(abs(x - Q0) for x in qs) / Q0) if qs else None,
                               dE_rel=(float(res["E1"][0]) - float(res["E0"][0])) / float(res["E0"][0]),
                               x_ende=xs, y_ende=ys, x_soll=x0 + v * T,
                               S_max_start=r0["S_max"], S_max_ende=float(S.max()) / S0,
                               S_max_min=min(r[3][0] for r in res["reihe"]) / S0,
                               S_max_max=max(r[3][0] for r in res["reihe"]) / S0,
                               verlauf_t=[r[0] for r in res["reihe"]][::5], verlauf_Q=qs[::5])
                print(om, h, name, {k: vv for k, vv in e[name].items() if not k.startswith("verlauf")},
                      f"t={time.time() - t0:.0f}s", flush=True)
                del P, Pi, lauf
            out["je"]["%s_h%g" % (om, h)] = dict(R=R, om=omv, S0=S0, **e)
            schreibe(a.out, out)
            del G
            torch.cuda.empty_cache()
    out["sek"] = time.time() - t0
    out["gpu_mb"] = gpu_mb()
    out["ende_utc"] = jetzt()
    schreibe(a.out, out)


def ygitter(Ymax, ny, nur_ungerade):
    ys = np.linspace(-Ymax, Ymax, ny)
    idx = np.arange(ny)
    if nur_ungerade:
        idx = idx[1::2]
    return ys, idx


def modus_lauf(a):
    """Ein Auftrag: Modell (qball/lin), omega, h, Layout (nspalt, d/R), Konfigurationen, v-Liste, y-Gitter."""
    t0 = time.time()
    pr = json.load(open(a.profil))
    om = a.omega
    prof = lade_profil(a.profil.replace(".json", ".npz"), om)
    R = pr[om]["R_halb"]
    omv = pr[om]["om"]
    kap = math.sqrt(1.0 - omv * omv)
    S0 = pr[om]["f0"] ** 2
    Qball = pr[om]["Q"]
    w = a.wf * R   # Spaltbreite; Karte: w = R (wf = 1); Zusatzarm W (PLAN Abschn. 7a): wf = 3
    if a.d_art == "R":
        d = a.d * R
    else:  # "2R+4/kappa"
        d = 2.0 * R + 4.0 / kap
    mitten = spaltmitten(a.nspalt, w, d)
    ymax_spalt = max(abs(v) for v in mitten.values())
    Ymax = ymax_spalt + 0.5 * w + R + 2.0 / kap
    ys, idx = ygitter(Ymax, a.ny, a.nur_ungerade)
    G = Gitter(a.h)
    zon = zonen_matrix(G, mitten)
    wb = winkel_bins(G)
    konf = a.konfig
    chunk = a.chunk if a.chunk > 0 else len(konf)
    out = {"modus": "lauf", "geraet": GERAET, "start_utc": jetzt(), "argumente": vars(a), "R": R, "om": omv,
           "kappa": kap, "S0": S0, "Q_ball": Qball, "w": w, "d": d, "mitten": mitten, "Ymax": Ymax,
           "y": ys.tolist(), "idx": idx.tolist(), "konfig": konf, "h": a.h, "dt": a.dt, "Nx": G.Nx, "Ny": G.Ny,
           "je_v": {}}
    ny = len(idx)
    Qnorm = Qball if a.modell == "qball" else 1.0
    abbruch = False
    for v in a.vs:
        T = a.weg / v
        recs = {}
        teile = []
        zonen_namen = None
        for k0 in range(0, len(konf), chunk):
            kk = konf[k0:k0 + chunk]
            rest = a.zeitgrenze - (time.time() - t0) - a.reserve
            if rest <= 5.0:
                teile.append(dict(konfig=kk, status="nicht_gestartet_zeitgrenze"))
                abbruch = True
                break
            Vc = np.stack([wandpotential(G, mitten, list(k), w) for k in kk])
            B = len(kk) * ny
            P = torch.empty((B, 2, G.Nx, G.Ny), dtype=torch.float32, device=DEV)
            Pi = torch.empty_like(P)
            for jj, j in enumerate(idx):
                if a.modell == "qball":
                    phi, pi = ball_felder(G, prof, omv, v, X0, ys[j])
                else:
                    phi, pi = kg_felder(G, R, v, X0, ys[j])
                tphi = torch.tensor(np.stack([phi.real, phi.imag]).astype(np.float32), device=DEV)
                tpi = torch.tensor(np.stack([pi.real, pi.imag]).astype(np.float32), device=DEV)
                for ci in range(len(kk)):
                    P[ci * ny + jj] = tphi
                    Pi[ci * ny + jj] = tpi
            lauf = Lauf(G, Vc, ny, a.modell == "qball", a.dt)
            res, P, Pi = fahre(G, lauf, P, Pi, T, zon, wand=rest)
            zonen_namen = res["zonen"]
            ea = endanalyse(G, lauf, P, Pi, S0, R, Qnorm, wb)
            for ci, c in enumerate(kk):
                lst = []
                for jj, j in enumerate(idx):
                    b = ci * ny + jj
                    fl = (res["flux"][b] / Qnorm).tolist()
                    r = dict(j=int(j), y=float(ys[j]), Q0=float(res["Q0"][b] / Qnorm), E0=float(res["E0"][b]),
                             E1=float(res["E1"][b]), flux=fl, **ea[b])
                    if a.modell == "qball":
                        r.update(klasse(ea[b]["stuecke"], R, fl))
                    lst.append(r)
                if res["status"] == "fertig":
                    recs[c] = lst
            teile.append(dict(konfig=kk, status=res["status"], schritte=res["schritte"], sek=res["sek"],
                              ms_schritt=res["ms_schritt"]))
            print(f"v={v} konfig={kk} {res['status']} schritte={res['schritte']} sek={res['sek']:.1f} "
                  f"ms/schritt={res['ms_schritt']:.2f} gpu={gpu_mb():.0f}MB t={time.time() - t0:.0f}s", flush=True)
            del P, Pi, lauf
            torch.cuda.empty_cache()
            if res["status"] != "fertig":
                abbruch = True
                break
        st = "fertig" if len(recs) == len(konf) else "unvollstaendig"
        out["je_v"][str(v)] = dict(T=T, status=st, teile=teile, zonen=zonen_namen, laeufe=recs)
        schreibe(a.out, out)
        if abbruch:
            break
    out["sek"] = time.time() - t0
    out["gpu_mb"] = gpu_mb()
    out["ende_utc"] = jetzt()
    schreibe(a.out, out)


def liste(s, typ=float):
    return [typ(v) for v in s.split(",")]
def main():
    global GERAET
    ap = argparse.ArgumentParser()
    ap.add_argument("modus", choices=["profil", "bilanz", "ruhe", "lauf"])
    ap.add_argument("--out", required=True)
    ap.add_argument("--profil", default="")
    ap.add_argument("--d2", default="")
    ap.add_argument("--wand", type=float, default=540.0)
    ap.add_argument("--tol", type=float, default=1e-10)
    ap.add_argument("--omegas", type=lambda s: s.split(","), default=["0.8", "0.9"])
    ap.add_argument("--hs", type=liste, default=[0.25, 0.125])
    ap.add_argument("--T", type=float, default=200.0)
    ap.add_argument("--dt", type=float, default=0.05)
    ap.add_argument("--modell", choices=["qball", "lin"], default="qball")
    ap.add_argument("--omega", default="0.8")
    ap.add_argument("--h", type=float, default=0.25)
    ap.add_argument("--nspalt", type=int, default=2)
    ap.add_argument("--d_art", choices=["R", "fern"], default="R")
    ap.add_argument("--d", type=float, default=1.0)
    ap.add_argument("--konfig", type=lambda s: s.split(","), default=["A", "AB"])
    ap.add_argument("--vs", type=liste, default=[0.2, 0.3, 0.45])
    ap.add_argument("--ny", type=int, default=41)
    ap.add_argument("--nur_ungerade", type=int, default=0)
    ap.add_argument("--zeitgrenze", type=float, default=560.0)
    ap.add_argument("--reserve", type=float, default=40.0)
    ap.add_argument("--weg", type=float, default=L_WEG)
    ap.add_argument("--chunk", type=int, default=0)
    ap.add_argument("--wf", type=float, default=1.0)
    a = ap.parse_args()
    if a.modus != "bilanz":
        GERAET = geraet()
        print("geraet", GERAET, flush=True)
    t0 = time.time()
    {"profil": modus_profil, "bilanz": modus_bilanz, "ruhe": modus_ruhe, "lauf": modus_lauf}[a.modus](a)
    print("geschrieben", a.out, f"{time.time() - t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
