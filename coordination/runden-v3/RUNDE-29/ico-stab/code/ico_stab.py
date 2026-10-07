#!/usr/bin/env python3
"""ICO-STAB (Runde 29). Code-Agent fuer die Leitung claude-primary, 03.10.2026.
Karte: RUNDE-29/ico-stab/KARTE.md; Plan: RUNDE-29/ico-stab/PLAN.md. Stabcode nach RUNDE-27/frust-3d/code/frust_3d.py
(Energie je Stab, Loeser mit Sattelflucht, Kraefte und Momente unveraendert uebernommen; neu: Geometrie, Lager, Zentrum,
Hesse-Analyse ohne Drehmoden, Sattelprobe).

Ikosaeder mit Zentrum: 13 Knoten, 42 gleiche elastische Staebe (B = 1, Ks = 25600, N Segmente, von Natur aus gerade,
keine Torsion). 12 Speichen Zentrum-Ecke (Ruhelaenge l_sp) und 30 Kantenstaebe (Ruhelaenge 1).
Knoten: 0 = Zentrum; 1 = Spitze oben (0, 0, R_c); 2..6 = oberer Ring (Hoehe R_c/sqrt5, Radius 2 R_c/sqrt5, Azimut
  72 k Grad); 7..11 = unterer Ring (Hoehe -R_c/sqrt5, Azimut 72 k + 36 Grad); 12 = Spitze unten. R_c = sin 72 Grad
  = 0,951057 (Kante 1). Kanten = alle Eckpaare im Abstand 1 (30), Flaechen = alle Dreiecke aus Kanten (20).
Energie je Stab wie FRUST-3D: Dehnung (Ks/2) Summe (|e| - l0)^2 / l0, Biegung (B/l0) Summe (1 - t_i . t_(i+1)),
  Einspannung (2B/l0)(1 -+ d . t) nur bei Lagerung E.
Lagerung G (Gelenke): Verbinder = Punkte (nur Lage). Lager (nur Starrkoerper, statisch bestimmt): Ecke 1 fest, Ecke 12
  in x und y, Ecke 2 in y. Lagerung E: Verbinder = starre Koerper (Lage, Drehvektor r, Drehung exp(schief(r))), Ecke 1
  fest (Lage und Drehung); Wunschrichtungen = Stabrichtungen im regulaeren Ikosaeder mit Zentrum.
Zentrum "frei": nur die Lager oben. Zentrum "fest" (Konkurrenzzustand): die Lage des Zentrums ist keine freie Groesse,
  sondern das Mittel der 12 Ecken (X_0 = Summe X_v / 12; Gradient und Hesse-Matrix per Kettenregel, T^T H T). Die
  Haltekraft (Summe der Speichenkraefte am Zentrum) geht zu gleichen Teilen an die Ecken; sie wird als Reaktion am
  Zentrum berichtet. (Erste Fassung im Rauchlauf: Zentrum im Ursprung fest; die Huelle dehnte sich dann von der festen
  Ecke 1 aus, und das Zentrum sass 1,5e-4 neben der Huellenmitte.)
Start: Zentrum um versatz in Startrichtung verschoben (null; ecke = zu Ecke 1; kante = zur Mitte der Kante 1-2;
  flaeche = zur Mitte der Flaeche 1-2-3; zufallK = Normalverteilung, numpy default_rng(K)); Ecken regulaer. Staebe gerade
  plus halbe Sinuswelle quer zur Sehne mit Amplitude amp: Speichen in Richtung a = (0,36; -0,48; 0,80) senkrecht zur
  Sehne, Kanten senkrecht zur Kante von der Mitte weg.
Loeser wie FRUST-3D: gedaempfter Newton (Cholesky von H + mu I, mu ab 1e-10 max|diag H|, Armijo-Rueckschritt);
  Sattelflucht entlang des tiefsten Eigenvektors (hoechstens 6 Stoesse); stabil = kleinster Hesse-Eigenwert > -1e-6.
Hesse-Analyse: volles Spektrum der freien Komponenten (die Lager nehmen die Starrkoerpermoden) und Spektrum ohne die
  Drehmoden der geknickten Staebe (nur G: Drehung der inneren Knoten um die Sehne, exakte Nullrichtung; abgetrennt durch
  H + 1e3 Q Q^T mit orthonormalen Drehmoden Q).
Sattelprobe (nur Zentrum fest): Gradient und Hesse-Matrix des freien Problems (Zentrum losgelassen) im festgehaltenen
  Zustand.
Kraft des Stabs auf den Verbinder: -dE_Stab/dX; Moment: -d x dE_Stab/dd (nur E). Axialkraft entlang der Sehne, + = Zug.

Aufruf: python ico_stab.py <name> <N> <G|E> <frei|fest> <start> <versatz> <amp> <l_sp|Rc> <aus.json> [zeitgrenze_s]
  (l_sp = Rc heisst Speichen-Ruhelaenge R_c, Kontrolle)
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import scipy.linalg as sla  # noqa: E402
import torch  # noqa: E402
from torch.func import grad, hessian, vmap  # noqa: E402

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)
B, L, KS = 1.0, 1.0, 25600.0
ORDNUNG_EXP = 24          # Potenzreihe fuer exp(schief(r)); fuer |r| < 1 ist der Abbruchfehler < 1e-24
MAXIT = 300               # Newton-Schritte je Phase
MAX_FLUCHT = 6            # hoechstens sechs Stoesse aus einem Sattel
INSTABIL = -1e-6          # kleinster Hesse-Eigenwert darunter: Sattel (instabil)
ZEITGRENZE = 480.0        # s; die Spur bricht bei 600 s ab, so wird vorher noch geschrieben
R_C = math.sin(2.0 * math.pi / 5.0)   # Umkreisradius des Ikosaeders mit Kante 1: 0,951057
SIGMA_DREH = 1e3          # Verschiebung der Drehmoden in der Hesse-Analyse
STICH_DREH = 1e-5         # Stab mit Stich darueber gilt fuer die Drehmoden als gebogen
QUER_A = np.array([0.36, -0.48, 0.80])


def schief(v):
    z = torch.zeros_like(v[0])
    return torch.stack([torch.stack([z, -v[2], v[1]]), torch.stack([v[2], z, -v[0]]),
                        torch.stack([-v[1], v[0], z])])


def drehung(r):
    """exp(schief(r)) als Potenzreihe (Horner), glatt und vmap-/jacfwd-tauglich."""
    K = schief(r)
    eins = torch.eye(3, dtype=r.dtype)
    S = eins
    for n in range(ORDNUNG_EXP, 0, -1):
        S = eins + (K @ S) / n
    return S


def ikosaeder():
    """Knoten (Zentrum im Ursprung), Kanten (Abstand 1) und Flaechen."""
    h = R_C / math.sqrt(5.0)
    rho = 2.0 * R_C / math.sqrt(5.0)
    P = [np.zeros(3), np.array([0.0, 0.0, R_C])]
    for k in range(5):
        a = 2.0 * math.pi * k / 5.0
        P.append(np.array([rho * math.cos(a), rho * math.sin(a), h]))
    for k in range(5):
        a = 2.0 * math.pi * k / 5.0 + math.pi / 5.0
        P.append(np.array([rho * math.cos(a), rho * math.sin(a), -h]))
    P.append(np.array([0.0, 0.0, -R_C]))
    P = np.array(P)
    kanten = [(a, b) for a in range(1, 13) for b in range(a + 1, 13)
              if abs(float(np.linalg.norm(P[a] - P[b])) - 1.0) < 1e-9]
    ks = set(kanten)
    flaechen = [(a, b, c) for a in range(1, 13) for b in range(a + 1, 13) for c in range(b + 1, 13)
                if (a, b) in ks and (a, c) in ks and (b, c) in ks]
    if len(kanten) != 30 or len(flaechen) != 20:
        raise RuntimeError(f"Ikosaeder falsch: {len(kanten)} Kanten, {len(flaechen)} Flaechen")
    return P, kanten, flaechen


def startrichtung(P, start):
    if start == "null":
        return np.zeros(3)
    if start == "ecke":
        n = P[1].copy()
    elif start == "kante":
        n = 0.5 * (P[1] + P[2])
    elif start == "flaeche":
        n = (P[1] + P[2] + P[3]) / 3.0
    elif start.startswith("zufall"):
        n = np.random.default_rng(int(start[6:])).normal(size=3)
    else:
        raise ValueError(start)
    return n / np.linalg.norm(n)


def querrichtung(P, i, j, art):
    e = P[j] - P[i]
    e = e / np.linalg.norm(e)
    n = QUER_A.copy() if art == "speiche" else 0.5 * (P[i] + P[j])
    n = n - np.dot(n, e) * e
    return n / np.linalg.norm(n)


class Modell:
    def __init__(self, N, lag, zentrum, start, versatz, amp, l_sp):
        if lag not in ("G", "E") or zentrum not in ("frei", "fest"):
            raise ValueError((lag, zentrum))
        if zentrum == "fest" and (start != "null" or versatz != 0.0):
            raise ValueError("Zentrum fest nur mit Start null und Versatz 0")
        self.N, self.lag, self.zentrum, self.start, self.versatz = N, lag, zentrum, start, versatz
        P_ref, self.kanten, self.flaechen = ikosaeder()
        self.P_ref = P_ref
        self.richtung = startrichtung(P_ref, start)
        self.P = P_ref.copy()
        self.P[0] = versatz * self.richtung
        self.staebe = [(0, v, "speiche") for v in range(1, 13)] + [(a, b, "kante") for (a, b) in self.kanten]
        self.nv, self.R = len(self.P), len(self.staebe)
        self.lr = np.array([l_sp if art == "speiche" else L for (_, _, art) in self.staebe])
        d0i, d0j = [], []
        for (i, j, _) in self.staebe:
            e = P_ref[j] - P_ref[i]
            e = e / np.linalg.norm(e)
            d0i.append(e)
            d0j.append(-e)
        self.d0i_np, self.d0j_np = np.array(d0i), np.array(d0j)
        self.D0I = torch.tensor(self.d0i_np)
        self.D0J = torch.tensor(self.d0j_np)
        self.L0 = torch.tensor(self.lr / N)
        self.k = 3 if lag == "G" else 6
        self.nin = 3 * (N - 1)
        self.nloc = self.nin + 2 * self.k
        self.nfull = self.R * self.nin + self.nv * self.k
        gl = np.zeros((self.R, self.nloc), dtype=np.int64)
        for m, (i, j, _) in enumerate(self.staebe):
            gl[m, :self.nin] = m * self.nin + np.arange(self.nin)
            gl[m, self.nin:self.nin + self.k] = self.basis(i) + np.arange(self.k)
            gl[m, self.nin + self.k:] = self.basis(j) + np.arange(self.k)
        self.gl = gl
        self.glt = torch.tensor(gl)
        if lag == "G":
            fest = [self.basis(1) + c for c in range(3)] + [self.basis(12), self.basis(12) + 1, self.basis(2) + 1]
        else:
            fest = [self.basis(1) + c for c in range(6)]
        self.mitte = (zentrum == "fest")
        if self.mitte:
            fest += [self.basis(0) + c for c in range(3)]   # abhaengig: Zentrum = Mittel der 12 Ecken
        self.fest = np.array(sorted(fest), dtype=np.int64)
        self.fest_menge = set(int(c) for c in fest)
        self.frei = np.setdiff1d(np.arange(self.nfull), self.fest)
        if not np.array_equal(self.frei[:self.R * self.nin], np.arange(self.R * self.nin)):
            raise RuntimeError("innere Knoten nicht alle frei")
        self.abh = []   # (Komponente c, Lage unter den freien) je freie Lagekomponente einer Ecke
        if self.mitte:
            for v in range(1, 13):
                for c in range(3):
                    j = self.basis(v) + c
                    if j not in self.fest_menge:
                        self.abh.append((c, int(np.searchsorted(self.frei, j))))
        self.xvoll0 = self.startvoll(amp)
        self.f_T = vmap(self._teile)
        self.f_E = vmap(self._stab)
        self.f_G = vmap(grad(self._stab))
        self.f_H = vmap(hessian(self._stab))

    def basis(self, q):
        return self.R * self.nin + self.k * q

    def frei_index(self, q):
        """Lage der Lagekomponenten von Knoten q unter den freien Komponenten (None, wenn fest)."""
        aus = []
        for c in range(3):
            j = self.basis(q) + c
            if j in self.fest_menge:
                return None
            aus.append(int(np.searchsorted(self.frei, j)))
        return aus

    def startvoll(self, amp):
        teile = []
        s = np.linspace(0.0, 1.0, self.N + 1)[1:-1]
        for (i, j, art) in self.staebe:
            pts = self.P[i][None, :] + s[:, None] * (self.P[j] - self.P[i])[None, :]
            if amp > 0.0:
                n = querrichtung(self.P, i, j, art)
                pts = pts + amp * np.sin(math.pi * s)[:, None] * n[None, :]
            teile.append(pts.ravel())
        for q in range(self.nv):
            teile.append(self.P[q].copy() if self.lag == "G" else np.concatenate([self.P[q], np.zeros(3)]))
        return np.concatenate(teile)

    def _teile(self, z, d0i, d0j, l0):
        innen = z[:self.nin].reshape(self.N - 1, 3)
        o = self.nin
        Xi = z[o:o + 3]
        Xj = z[o + self.k:o + self.k + 3]
        y = torch.cat([Xi[None], innen, Xj[None]], 0)
        e = y[1:] - y[:-1]
        le = torch.sqrt((e * e).sum(1))
        t = e / le[:, None]
        es = 0.5 * KS * ((le - l0) ** 2).sum() / l0
        eb = (B / l0) * (1.0 - (t[:-1] * t[1:]).sum(1)).sum()
        if self.lag == "E":
            di = drehung(z[o + 3:o + 6]) @ d0i
            dj = drehung(z[o + self.k + 3:o + self.k + 6]) @ d0j
            ec = (2.0 * B / l0) * ((1.0 - (di * t[0]).sum()) + (1.0 + (dj * t[-1]).sum()))
        else:
            ec = 0.0 * es
        return torch.stack([es, eb, ec])

    def _stab(self, z, d0i, d0j, l0):
        return self._teile(z, d0i, d0j, l0).sum()

    def voll(self, x):
        xf = self.xvoll0.copy()
        xf[self.frei] = x
        if self.mitte:
            X = np.array([xf[self.basis(v):self.basis(v) + 3] for v in range(1, 13)])
            xf[self.basis(0):self.basis(0) + 3] = X.mean(0)
        return xf

    def lokal(self, xf):
        return torch.as_tensor(xf, dtype=torch.float64)[self.glt]

    def energie(self, x):
        return float(self.f_E(self.lokal(self.voll(x)), self.D0I, self.D0J, self.L0).sum())

    def gradient_voll(self, xf):
        G = self.f_G(self.lokal(xf), self.D0I, self.D0J, self.L0).numpy()
        g = np.zeros(self.nfull)
        np.add.at(g, self.gl.ravel(), G.ravel())
        return g

    def gradient(self, x):
        gf = self.gradient_voll(self.voll(x))
        g = gf[self.frei].copy()
        if self.mitte:   # Kettenregel: X_0 = Mittel der Ecken
            i0 = self.basis(0)
            for (c, p) in self.abh:
                g[p] += gf[i0 + c] / 12.0
        return g

    def hesse(self, x):
        Hl = self.f_H(self.lokal(self.voll(x)), self.D0I, self.D0J, self.L0).numpy()
        H = np.zeros((self.nfull, self.nfull))
        for m in range(self.R):
            ii = self.gl[m]
            H[np.ix_(ii, ii)] += Hl[m]
        if self.mitte:   # T^T H T mit x_voll = T x_frei + fest
            i0 = self.basis(0)
            A = H[:, self.frei].copy()
            for (c, p) in self.abh:
                A[:, p] += H[:, i0 + c] / 12.0
            Hf = A[self.frei, :].copy()
            for (c, p) in self.abh:
                Hf[p, :] += A[i0 + c, :] / 12.0
            H = Hf
        else:
            H = H[np.ix_(self.frei, self.frei)]
        return 0.5 * (H + H.T)


def newton(mod, x0, maxit, t_start):
    """Gedaempfter Newton wie FRUST-3D: Cholesky von H + mu I (mu ab 1e-10 max|diag H|, bei Fehlschlag x10),
    Armijo-Rueckschritt; findet die Liniensuche keinen Abstieg, wird mu vergroessert."""
    x = x0.copy()
    E = mod.energie(x)
    g = mod.gradient(x)
    verlauf = []
    meldung = "maxit"
    nx = len(x)
    for it in range(maxit):
        if time.time() - t_start > ZEITGRENZE:
            meldung = "Zeitgrenze"
            break
        gn = float(np.linalg.norm(g))
        if gn < 1e-13:
            verlauf.append([it, E, gn, 0.0, 0.0])
            meldung = "gradnorm < 1e-13"
            break
        H = mod.hesse(x)
        dmax = float(np.abs(np.diag(H)).max())
        mu = 1e-10 * dmax
        erfolg = False
        s = 0.0
        xn, En = x, E
        for _ in range(40):
            try:
                cf = sla.cho_factor(H + mu * np.eye(nx), lower=True)
            except np.linalg.LinAlgError:
                mu *= 10.0
                continue
            p = -sla.cho_solve(cf, g)
            gp = float(g @ p)
            s = 1.0
            while s >= 1e-10:
                xn = x + s * p
                En = mod.energie(xn)
                if En <= E + 1e-4 * s * gp + 1e-13 * abs(E):
                    erfolg = True
                    break
                s *= 0.5
            if erfolg:
                break
            mu *= 10.0
        verlauf.append([it, E, gn, mu, s if erfolg else 0.0])
        if not erfolg:
            meldung = "Liniensuche ohne Abstieg"
            break
        gnn = mod.gradient(xn)
        if float(np.linalg.norm(gnn)) >= gn and gn < 1e-8:
            meldung = "Rundungsboden (kein Fortschritt mehr)"
            break
        x, E, g = xn, En, gnn
    return x, verlauf, meldung


def loesen(mod, x0, t_start):
    """Newton bis zum Gleichgewicht; ist es ein Sattel (kleinster Hesse-Eigenwert < INSTABIL), Stoss entlang des
    zugehoerigen Eigenvektors (erste der Amplituden 1e-2, 3e-3, 1e-3, 3e-4, 1e-4 bezogen auf die groesste Komponente,
    die die Energie senkt) und erneut Newton; hoechstens MAX_FLUCHT Stoesse (wie FRUST-3D)."""
    x = x0.copy()
    phasen = []
    verlauf_alle = []
    ew = None
    for phase in range(MAX_FLUCHT + 1):
        x, verlauf, meldung = newton(mod, x, MAXIT, t_start)
        verlauf_alle += [[phase] + v for v in verlauf]
        E = mod.energie(x)
        w, V = np.linalg.eigh(mod.hesse(x))
        ew = w
        eintrag = {"phase": phase, "schritte": len(verlauf), "meldung": meldung, "energie": E,
                   "gradnorm": float(np.linalg.norm(mod.gradient(x))), "hesse_kleinste": [float(v) for v in w[:6]]}
        phasen.append(eintrag)
        if w[0] > INSTABIL or meldung == "Zeitgrenze" or phase == MAX_FLUCHT:
            break
        v = V[:, 0]
        gestossen = False
        for a in (1e-2, 3e-3, 1e-3, 3e-4, 1e-4):
            amp = a / float(np.abs(v).max())
            Ep, Em = mod.energie(x + amp * v), mod.energie(x - amp * v)
            if min(Ep, Em) < E:
                x = x + amp * v if Ep <= Em else x - amp * v
                eintrag["stoss"] = {"a": a, "energie_danach": min(Ep, Em)}
                gestossen = True
                break
        if not gestossen:
            eintrag["stoss"] = "kein Abstieg entlang des Eigenvektors"
            break
    return x, phasen, verlauf_alle, ew


def lasten(mod, x):
    """Kraft und Moment jedes Stabs auf seine beiden Verbinder, Form je Stab, Summen je Verbinder (wie FRUST-3D)."""
    xf = mod.voll(x)
    Z = mod.lokal(xf)
    o, k, N = mod.nin, mod.k, mod.N
    Gl = mod.f_G(Z, mod.D0I, mod.D0J, mod.L0).numpy()
    T = mod.f_T(Z, mod.D0I, mod.D0J, mod.L0).numpy()
    Zn = Z.numpy()
    Fi = -Gl[:, o:o + 3]
    Fj = -Gl[:, o + k:o + k + 3]
    l0 = mod.lr / N
    Ti_alle = np.zeros((mod.R, 3))
    Tj_alle = np.zeros((mod.R, 3))
    staebe = []
    for m, (i, j, art) in enumerate(mod.staebe):
        innen = Zn[m, :o].reshape(N - 1, 3)
        Xi = Zn[m, o:o + 3]
        Xj = Zn[m, o + k:o + k + 3]
        y = np.vstack([Xi[None, :], innen, Xj[None, :]])
        e = y[1:] - y[:-1]
        le = np.linalg.norm(e, axis=1)
        t = e / le[:, None]
        if mod.lag == "E":
            di = drehung(torch.tensor(Zn[m, o + 3:o + 6])).numpy() @ mod.d0i_np[m]
            dj = drehung(torch.tensor(Zn[m, o + k + 3:o + k + 6])).numpy() @ mod.d0j_np[m]
            c = 2.0 * B / l0[m]
            Ti = c * np.cross(di, t[0])            # dE/d(di) = -c t_0, tau = -di x dE/d(di)
            Tj = -c * np.cross(dj, t[-1])          # dE/d(dj) = +c t_letzt
            wi = math.degrees(math.acos(max(-1.0, min(1.0, float(di @ t[0])))))
            wj = math.degrees(math.acos(max(-1.0, min(1.0, float(-(dj @ t[-1]))))))
        else:
            Ti = np.zeros(3)
            Tj = np.zeros(3)
            wi = wj = 0.0
        Ti_alle[m] = Ti
        Tj_alle[m] = Tj
        sehne = Xj - Xi
        a = float(np.linalg.norm(sehne))
        eh = sehne / a
        rel = innen - Xi[None, :]
        quer = rel - (rel @ eh)[:, None] * eh[None, :]
        kreuz = np.linalg.norm(np.cross(t[:-1], t[1:]), axis=1)
        punkt = (t[:-1] * t[1:]).sum(1)
        theta = np.arctan2(kreuz, punkt)
        m_innen = (B / l0[m]) * np.sin(theta)
        fia = float(Fi[m] @ eh)
        fja = float(Fj[m] @ (-eh))
        staebe.append({
            "m": m, "i": i, "j": j, "art": art, "l_ruhe": float(mod.lr[m]), "a": a, "bogen": float(le.sum()),
            "verkuerzung": float(mod.lr[m] - a),
            "stich": float(np.linalg.norm(quer, axis=1).max()),
            "F_i": Fi[m].tolist(), "F_j": Fj[m].tolist(), "tau_i": Ti.tolist(), "tau_j": Tj.tolist(),
            "F_i_axial": fia, "F_j_axial": fja,
            "F_i_quer": float(np.linalg.norm(Fi[m] - fia * eh)), "F_j_quer": float(np.linalg.norm(Fj[m] + fja * eh)),
            "F_i_betrag": float(np.linalg.norm(Fi[m])), "F_j_betrag": float(np.linalg.norm(Fj[m])),
            "tau_i_betrag": float(np.linalg.norm(Ti)), "tau_j_betrag": float(np.linalg.norm(Tj)),
            "M_innen_max": float(m_innen.max()), "M_innen_mitte": float(m_innen[(N - 2) // 2]),
            "einspann_abweichung_grad_i": wi, "einspann_abweichung_grad_j": wj,
            "euler_verhaeltnis": float(-fia / (math.pi ** 2 * B / mod.lr[m] ** 2)),
            "energie_dehnung": float(T[m, 0]), "energie_biegung_innen": float(T[m, 1]),
            "energie_einspannung": float(T[m, 2])})
    knoten = []
    F_alle = np.zeros((mod.nv, 3))
    T_alle = np.zeros((mod.nv, 3))
    for q in range(mod.nv):
        for m, (i, j, _) in enumerate(mod.staebe):
            if q == i:
                F_alle[q] += Fi[m]
                T_alle[q] += Ti_alle[m]
            elif q == j:
                F_alle[q] += Fj[m]
                T_alle[q] += Tj_alle[m]
    for q in range(mod.nv):
        F = F_alle[q].copy()
        Tq = T_alle[q]
        if mod.mitte and q >= 1:   # Zwangskraft des Zentrums (Mittel der Ecken) geht zu gleichen Teilen an die Ecken
            F = F + F_alle[0] / 12.0
        fest = [c for c in range(mod.k) if mod.basis(q) + c in mod.fest_menge]
        fr = [c for c in range(3) if c not in fest]
        fx = [c for c in range(3) if c in fest]
        rest_F = float(np.linalg.norm(F[fr])) if fr else 0.0
        reak_F = float(np.linalg.norm(F[fx])) if fx else 0.0
        if mod.lag == "E":
            dreh_fest = 3 in fest
            rest_T = 0.0 if dreh_fest else float(np.linalg.norm(Tq))
            reak_T = float(np.linalg.norm(Tq)) if dreh_fest else 0.0
        else:
            rest_T = reak_T = 0.0
        knoten.append({"q": q, "F_summe": F.tolist(), "tau_summe": Tq.tolist(), "feste_komponenten": fest,
                       "rest_F": rest_F, "rest_tau": rest_T, "reaktion_F": reak_F, "reaktion_tau": reak_T})
    return staebe, knoten


def zentrumslage(mod, x):
    """Zentrum gegen die Mitte der (verformten) Huelle: Verschiebung u, Richtung gegen Ecken, Kantenmitten,
    Flaechenmitten; je Speiche cos(theta) gegen u."""
    xf = mod.voll(x)
    X = np.array([xf[mod.basis(q):mod.basis(q) + 3] for q in range(mod.nv)])
    ch = X[1:].mean(0)
    uv = X[0] - ch
    u = float(np.linalg.norm(uv))
    radien = [float(np.linalg.norm(X[v] - ch)) for v in range(1, 13)]
    aus = {"zentrum": X[0].tolist(), "huellenmitte": ch.tolist(), "u_vektor": uv.tolist(), "u": u,
           "eckradius": radien, "ecken": X.tolist()}
    if u > 1e-12:
        uh = uv / u

        def wink(d):
            return math.degrees(math.acos(max(-1.0, min(1.0, float(uh @ d) / float(np.linalg.norm(d))))))

        we = [(wink(X[v] - ch), v) for v in range(1, 13)]
        wk = [(wink(0.5 * (X[a] + X[b]) - ch), [a, b]) for (a, b) in mod.kanten]
        wf = [(wink((X[a] + X[b] + X[c]) / 3.0 - ch), [a, b, c]) for (a, b, c) in mod.flaechen]
        aus["winkel_naechste_ecke"] = min(we)[0]
        aus["naechste_ecke"] = min(we)[1]
        aus["winkel_naechste_kantenmitte"] = min(wk)[0]
        aus["naechste_kante"] = min(wk)[1]
        aus["winkel_naechste_flaechenmitte"] = min(wf)[0]
        aus["naechste_flaeche"] = min(wf)[1]
        aus["cos_theta_speiche"] = [float(uh @ (X[v] - ch)) / float(np.linalg.norm(X[v] - ch)) for v in range(1, 13)]
        if float(np.linalg.norm(mod.richtung)) > 0.0:
            aus["winkel_zur_startrichtung"] = wink(mod.richtung)
    return aus


def drehmoden(mod, x):
    """Orthonormale Drehmoden der gebogenen Staebe (nur G): innere Knoten drehen um die Sehne (Enden fest)."""
    if mod.lag != "G":
        return np.zeros((len(x), 0)), []
    xf = mod.voll(x)
    spalten, welche = [], []
    for m, (i, j, _) in enumerate(mod.staebe):
        innen = xf[m * mod.nin:(m + 1) * mod.nin].reshape(mod.N - 1, 3)
        Xi, Xj = xf[mod.basis(i):mod.basis(i) + 3], xf[mod.basis(j):mod.basis(j) + 3]
        e = (Xj - Xi) / np.linalg.norm(Xj - Xi)
        rel = innen - Xi[None, :]
        quer = rel - (rel @ e)[:, None] * e[None, :]
        if float(np.linalg.norm(quer, axis=1).max()) < STICH_DREH:
            continue
        v = np.zeros(len(x))
        v[m * mod.nin:(m + 1) * mod.nin] = np.cross(e[None, :], rel).ravel()
        spalten.append(v / np.linalg.norm(v))
        welche.append(m)
    if not spalten:
        return np.zeros((len(x), 0)), []
    return np.array(spalten).T, welche


def hesse_analyse(mod, x, w_voll=None, vektoren=False):
    H = mod.hesse(x)
    if w_voll is None:
        w_voll = np.linalg.eigvalsh(H)
    Q, welche = drehmoden(mod, x)
    hq = float(np.abs(H @ Q).max()) if Q.shape[1] else 0.0
    Hs = H + SIGMA_DREH * (Q @ Q.T) if Q.shape[1] else H
    aus = {"hesse_kleinste": [float(v) for v in w_voll[:24]], "hesse_groesste": float(w_voll[-1]),
           "nahe_null_voll": int(np.sum(np.abs(w_voll) < 1e-7)), "drehmoden_anzahl": len(welche),
           "drehmoden_staebe": welche, "drehmoden_HQ_max": hq}
    if vektoren:
        w2, V2 = np.linalg.eigh(Hs)
        idx = mod.frei_index(0)
        if idx is not None:
            aus["tiefste_vektoren_zentrumsanteil"] = [float(np.sum(V2[idx, n] ** 2)) for n in range(6)]
            aus["tiefste_vektoren_zentrumsrichtung"] = [(V2[idx, n] / max(1e-300, float(np.linalg.norm(V2[idx, n]))))
                                                        .tolist() for n in range(3)]
    else:
        w2 = np.linalg.eigvalsh(Hs)
    aus["ohne_drehmoden_kleinste"] = [float(v) for v in w2[:24]]
    aus["ohne_drehmoden_anzahl_negativ"] = int(np.sum(w2 < INSTABIL))
    aus["ohne_drehmoden_nahe_null"] = int(np.sum(np.abs(w2) < 1e-7))
    aus["verschobene_moden_bei_sigma"] = int(np.sum(np.abs(w2 - SIGMA_DREH) < 1e-3 * SIGMA_DREH))
    return aus


def sattelprobe(mod, x, l_sp):
    """Freies Problem (Zentrum losgelassen) im festgehaltenen Zustand: Gradient und Hesse-Spektrum."""
    mf = Modell(mod.N, mod.lag, "frei", "null", 0.0, 0.0, l_sp)
    xf = mod.voll(x)
    mf.xvoll0 = xf.copy()
    xs = xf[mf.frei].copy()
    g = mf.gradient(xs)
    idx = mf.frei_index(0)
    aus = {"gradnorm_frei": float(np.linalg.norm(g)), "gradient_zentrum": [float(g[i]) for i in idx],
           "energie_frei": mf.energie(xs)}
    aus.update(hesse_analyse(mf, xs, vektoren=True))
    return aus


def main():
    global ZEITGRENZE
    (name, N, lag, zentrum, start, versatz, amp, l_sp, pfad) = (
        sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5], float(sys.argv[6]), float(sys.argv[7]),
        R_C if sys.argv[8] == "Rc" else float(sys.argv[8]), sys.argv[9])
    if len(sys.argv) > 10:
        ZEITGRENZE = float(sys.argv[10])   # nur fuer Rauchlaeufe (<= 120 s); echte Laeufe: 480 s
    t0 = time.time()
    mod = Modell(N, lag, zentrum, start, versatz, amp, l_sp)
    x0 = mod.xvoll0[mod.frei].copy()
    E0 = mod.energie(x0)
    x, phasen, verlauf, ev = loesen(mod, x0, t0)
    meldung = phasen[-1]["meldung"]
    gn = float(np.linalg.norm(mod.gradient(x)))
    staebe, knoten = lasten(mod, x)
    teile = mod.f_T(mod.lokal(mod.voll(x)), mod.D0I, mod.D0J, mod.L0).numpy()
    je_art = {}
    for art in ("speiche", "kante"):
        idx = [m for m, s in enumerate(mod.staebe) if s[2] == art]
        je_art[art] = {"anzahl": len(idx), "dehnung": float(teile[idx, 0].sum()),
                       "biegung_innen": float(teile[idx, 1].sum()), "einspannung": float(teile[idx, 2].sum())}
    out = {"name": name, "N": N, "lagerung": lag, "zentrum_lagerung": zentrum, "start": start, "versatz": versatz,
           "amp": amp, "l_sp": l_sp, "R_c": R_C, "B": B, "L": L, "Ks": KS, "nx_frei": int(len(x)),
           "anzahl_staebe": mod.R, "anzahl_knoten": mod.nv, "feste_komponenten": mod.fest.tolist(),
           "startrichtung": mod.richtung.tolist(), "energie_start": E0, "energie": mod.energie(x),
           "energie_je_art": je_art, "gradnorm": gn, "newton_schritte": len(verlauf), "newton_verlauf": verlauf,
           "newton_meldung": meldung, "phasen": phasen, "anzahl_stoesse": len(phasen) - 1,
           "stabil": bool(ev[0] > INSTABIL), "staebe": staebe, "knoten": knoten, "kanten": mod.kanten,
           "flaechen": mod.flaechen, "zentrumslage": zentrumslage(mod, x)}
    out["hesse"] = hesse_analyse(mod, x, w_voll=ev)
    out["hesse_kleinste"] = [float(v) for v in ev[:24]]
    if zentrum == "fest":
        out["sattelprobe"] = sattelprobe(mod, x, l_sp)
    out["sek"] = time.time() - t0
    with open(pfad + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1)
    os.replace(pfad + ".tmp", pfad)
    frei_rest = max(max(kn["rest_F"], kn["rest_tau"]) for kn in knoten)
    zl = out["zentrumslage"]
    print(f"{name}: N {N}, {lag}, Zentrum {zentrum}, Start {start} {versatz}, amp {amp}, l_sp {l_sp}, nx {len(x)}, "
          f"Newton {len(verlauf)} ({meldung}), Stoesse {len(phasen) - 1}, |grad| {gn:.1e}, "
          f"E {out['energie']:.8e} (Start {E0:.3e}), stabil {out['stabil']}, Rest frei {frei_rest:.1e}, "
          f"{out['sek']:.1f} s", flush=True)
    for art in ("speiche", "kante"):
        st = [s for s in staebe if s["art"] == art]
        ax = [s["F_i_axial"] for s in st]
        print(f"  {art}: axial {min(ax):+.6e} .. {max(ax):+.6e}, Stich {min(s['stich'] for s in st):.4e} .. "
              f"{max(s['stich'] for s in st):.4e}, E dehn {je_art[art]['dehnung']:.4e} "
              f"bieg {je_art[art]['biegung_innen']:.4e} einsp {je_art[art]['einspannung']:.4e}", flush=True)
    sp = [s for s in staebe if s["art"] == "speiche"]
    print("  Speichen Stich: " + " ".join(f"{s['stich']:.4f}" for s in sp), flush=True)
    print("  Speichen axial: " + " ".join(f"{s['F_i_axial']:+.3f}" for s in sp), flush=True)
    print(f"  u {zl['u']:.6f}, Winkel Ecke {zl.get('winkel_naechste_ecke', float('nan')):.2f}, Kante "
          f"{zl.get('winkel_naechste_kantenmitte', float('nan')):.2f}, Flaeche "
          f"{zl.get('winkel_naechste_flaechenmitte', float('nan')):.2f} Grad, Flaeche {zl.get('naechste_flaeche')}",
          flush=True)
    h = out["hesse"]
    print(f"  Hesse voll kleinste {[float('%.3e' % v) for v in h['hesse_kleinste'][:6]]}, nahe null "
          f"{h['nahe_null_voll']}, Drehmoden {h['drehmoden_anzahl']} (|HQ| {h['drehmoden_HQ_max']:.1e}), ohne "
          f"Drehmoden {[float('%.3e' % v) for v in h['ohne_drehmoden_kleinste'][:4]]}", flush=True)
    for ph in phasen:
        print(f"  Phase {ph['phase']}: {ph['schritte']} Schritte ({ph['meldung']}), E {ph['energie']:.8e}, "
              f"kleinster EW {ph['hesse_kleinste'][0]:.3e}, Stoss {ph.get('stoss')}", flush=True)
    if zentrum == "fest":
        sp_ = out["sattelprobe"]
        print(f"  Sattelprobe: |grad frei| {sp_['gradnorm_frei']:.2e}, ohne Drehmoden kleinste "
              f"{[float('%.3e' % v) for v in sp_['ohne_drehmoden_kleinste'][:6]]}, negativ "
              f"{sp_['ohne_drehmoden_anzahl_negativ']}, Zentrumsanteil "
              f"{[float('%.3f' % v) for v in sp_.get('tiefste_vektoren_zentrumsanteil', [])]}", flush=True)


if __name__ == "__main__":
    main()
