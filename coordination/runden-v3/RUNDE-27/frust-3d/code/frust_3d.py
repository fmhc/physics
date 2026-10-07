#!/usr/bin/env python3
"""FRUST-3D (Runde 27). Code-Agent fuer die Leitung claude-primary, 03.10.2026.
Karte: RUNDE-27/frust-3d/KARTE.md; Plan: RUNDE-27/frust-3d/PLAN.md. Stabcode nach RUNDE-26/tetra-kette/code/tetra_kette.py.

n_tet regulaere Tetraeder um die gemeinsame Kante AB, gebaut aus gleichen elastischen Staeben (Ruhelaenge 1, B = 1,
Ks = 25600, N Segmente, von Natur aus gerade, keine Torsion). Ecken: A = 0, B = 1, Ringecken r_k = 2 + k.
  n_tet = 5: pentagonale Bipyramide, 16 Staebe (Achse, 10 Speichen, 5 Ringstaebe), geschlossen und frustriert.
  n_tet = 1 und 4: offen, spannungsfrei (Kontrollen; 4 Tetraeder lassen 77,9 Grad offen).
Energie je Stab wie TETRA-STAB: Dehnung (Ks/2) Summe (|e| - l0)^2 / l0, Biegung (B/l0) Summe (1 - t_i . t_(i+1)),
  Einspannung (2B/l0)(1 -+ d . t) nur bei Lagerung E.
Lagerung G (Gelenke): Verbinder = Punkte (nur Lage), Stabenden frei drehbar, keine Einspannterme.
  Lager: A fest, B in x und y, r_0 in y (sechs Komponenten, nimmt nur die Starrkoerperbewegung).
Lagerung E (Einspannung): Verbinder = starre Koerper (Lage X, Drehvektor r, Drehung exp(schief(r))), jeder Stab in
  seiner Wunschrichtung eingespannt. Lager: A fest (Lage und Drehung).
Wunschrichtungen (Einspannung im Bezug, r = 0):
  M = normiertes Mittel der Kantenrichtungen in den regulaeren Tetraedern, die den Stab enthalten. Bei n_tet = 5 stehen
      die fuenf regulaeren Tetraeder in 72-Grad-Schritten um AB; die 7,36-Grad-Luecke ist gleichmaessig auf die fuenf
      Fugen verteilt (je 1,47 Grad). Bei offenen Anordnungen (Schritt = Diederwinkel) sind das die exakten Kanten.
  K = Kantenrichtungen der geschlossenen Bipyramide mit Achse 1,0515 (Speichen und Ring 1), nur fuer n_tet = 5.
Start: Ecken A = (0, 0, 1/2), B = (0, 0, -1/2) (Achse 1); n_tet = 5: Ring mit Radius 1/(2 sin 36 Grad) (Ringstaebe 1);
  offen: exakte regulaere Lage. Staebe gerade plus Anstoss.
Anstoss: halbe Sinuswelle quer zur Sehne mit Amplitude amp. "aus": Speichen in der Meridianebene und Ring in der
  Ringebene von der Achse weg, Achse in +x; "ein": umgekehrt; "keine": ohne.
Loeser: Energie, Gradient, Hesse-Matrix je Stab gebuendelt (torch.func.vmap, grad, hessian), global dicht; gedaempfter
  Newton (Cholesky mit kleiner Grundverschiebung 1e-10 max|diag H|, bei Bedarf groesser, Armijo-Rueckschritt).
  Endet Newton in einem Sattel (kleinster Hesse-Eigenwert < -1e-6), folgt ein Stoss entlang des Eigenvektors und erneut
  Newton (hoechstens 6 Stoesse). Hesse-Eigenwerte werden immer berechnet (Argument hesse nur protokolliert).
Kraft des Stabs auf den Verbinder: -dE_Stab/dX; Moment: -d x dE_Stab/dd (nur E). Axialkraft entlang der Sehne, + = Zug.

Aufruf: python frust_3d.py <name> <n_tet> <N> <G|E> <M|K> <aus|ein|keine> <amp> <achse_l0> <hesse 0/1> <aus.json>
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
DIEDER = math.acos(1.0 / 3.0)                      # Diederwinkel des regulaeren Tetraeders, 70,529 Grad
RHO_T = math.sqrt(3.0) / 2.0                        # Abstand der Ringecken von AB im regulaeren Tetraeder
R_RING = 1.0 / (2.0 * math.sin(math.pi / 5.0))      # Radius des geschlossenen Fuenfecks mit Kante 1
H_STERN = 2.0 * math.sqrt(1.0 - R_RING ** 2)        # Achse der Bipyramide mit Speichen und Ring 1: 1,0515


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


def ringpunkt(rho, phi):
    return np.array([rho * math.cos(phi), rho * math.sin(phi), 0.0])


def aufbau(n_tet):
    """Startecken, Staebe (i, j, Art) und die Bilder der Ecken je regulaerem Tetraeder (fuer die Wunschrichtungen)."""
    A = np.array([0.0, 0.0, 0.5])
    Bq = np.array([0.0, 0.0, -0.5])
    bilder = []
    if n_tet == 5:
        g = 2.0 * math.pi / 5.0 - DIEDER
        for k in range(5):
            bilder.append({0: A, 1: Bq, 2 + k: ringpunkt(RHO_T, 2.0 * math.pi * k / 5.0 + g / 2.0),
                           2 + (k + 1) % 5: ringpunkt(RHO_T, 2.0 * math.pi * (k + 1) / 5.0 - g / 2.0)})
        P = [A, Bq] + [ringpunkt(R_RING, 2.0 * math.pi * k / 5.0) for k in range(5)]
        nring = 5
        ring = [(2 + k, 2 + (k + 1) % 5) for k in range(5)]
    elif n_tet in (1, 2, 3, 4):
        for k in range(n_tet):
            bilder.append({0: A, 1: Bq, 2 + k: ringpunkt(RHO_T, k * DIEDER), 3 + k: ringpunkt(RHO_T, (k + 1) * DIEDER)})
        P = [A, Bq] + [ringpunkt(RHO_T, k * DIEDER) for k in range(n_tet + 1)]
        nring = n_tet + 1
        ring = [(2 + k, 3 + k) for k in range(n_tet)]
    else:
        raise ValueError("n_tet muss 1 bis 5 sein")
    staebe = [(0, 1, "achse")] + [(0, 2 + k, "speiche") for k in range(nring)] + \
        [(1, 2 + k, "speiche") for k in range(nring)] + [(i, j, "ring") for (i, j) in ring]
    return np.array(P), staebe, bilder


def wunschrichtungen(P, staebe, bilder, wunsch):
    PK = P.copy()
    PK[0] = np.array([0.0, 0.0, 0.5 * H_STERN])
    PK[1] = np.array([0.0, 0.0, -0.5 * H_STERN])
    d0i, d0j = [], []
    for (i, j, _) in staebe:
        for (u, v, ziel) in ((i, j, d0i), (j, i, d0j)):
            if wunsch == "M":
                s = np.zeros(3)
                n = 0
                for b in bilder:
                    if u in b and v in b:
                        e = b[v] - b[u]
                        s = s + e / np.linalg.norm(e)
                        n += 1
                if n == 0:
                    raise RuntimeError("Stab in keinem Tetraeder")
            elif wunsch == "K":
                s = PK[v] - PK[u]
            else:
                raise ValueError(wunsch)
            ziel.append(s / np.linalg.norm(s))
    return np.array(d0i), np.array(d0j)


def querrichtung(P, i, j, art, richtung):
    e = P[j] - P[i]
    e = e / np.linalg.norm(e)
    if art == "achse":
        n = np.array([1.0, 0.0, 0.0])
    else:
        m = 0.5 * (P[i] + P[j])
        n = np.array([m[0], m[1], 0.0])
    n = n - np.dot(n, e) * e
    n = n / np.linalg.norm(n)
    return n if richtung == "aus" else -n


class Modell:
    def __init__(self, n_tet, N, lag, wunsch, anstoss, amp, achse_l0):
        if lag not in ("G", "E"):
            raise ValueError(lag)
        self.n_tet, self.N, self.lag = n_tet, N, lag
        self.P, self.staebe, self.bilder = aufbau(n_tet)
        self.nv, self.R = len(self.P), len(self.staebe)
        self.lr = np.array([achse_l0 if art == "achse" else L for (_, _, art) in self.staebe])
        self.d0i_np, self.d0j_np = wunschrichtungen(self.P, self.staebe, self.bilder, wunsch)
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
            fest = [self.basis(0) + c for c in range(3)] + [self.basis(1), self.basis(1) + 1, self.basis(2) + 1]
        else:
            fest = [self.basis(0) + c for c in range(6)]
        self.fest = np.array(fest, dtype=np.int64)
        self.fest_menge = set(int(c) for c in fest)
        self.frei = np.setdiff1d(np.arange(self.nfull), self.fest)
        self.xvoll0 = self.startvoll(anstoss, amp)
        self.f_T = vmap(self._teile)
        self.f_E = vmap(self._stab)
        self.f_G = vmap(grad(self._stab))
        self.f_H = vmap(hessian(self._stab))

    def basis(self, q):
        return self.R * self.nin + self.k * q

    def startvoll(self, anstoss, amp):
        teile = []
        s = np.linspace(0.0, 1.0, self.N + 1)[1:-1]
        for (i, j, art) in self.staebe:
            pts = self.P[i][None, :] + s[:, None] * (self.P[j] - self.P[i])[None, :]
            if anstoss != "keine" and amp > 0.0:
                n = querrichtung(self.P, i, j, art, anstoss)
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
        return self.gradient_voll(self.voll(x))[self.frei]

    def hesse(self, x):
        Hl = self.f_H(self.lokal(self.voll(x)), self.D0I, self.D0J, self.L0).numpy()
        H = np.zeros((self.nfull, self.nfull))
        for m in range(self.R):
            ii = self.gl[m]
            H[np.ix_(ii, ii)] += Hl[m]
        H = H[np.ix_(self.frei, self.frei)]
        return 0.5 * (H + H.T)


def newton(mod, x0, maxit, t_start):
    """Gedaempfter Newton: Cholesky von H + mu I (mu ab 1e-10 max|diag H|, bei Fehlschlag x10), Armijo-Rueckschritt;
    findet die Liniensuche keinen Abstieg, wird mu vergroessert."""
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
    zugehoerigen Eigenvektors (Vorzeichen und Groesse: erste der Amplituden 1e-2, 3e-3, 1e-3, 3e-4, 1e-4 bezogen auf die
    groesste Komponente, die die Energie senkt) und erneut Newton; hoechstens MAX_FLUCHT Stoesse."""
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
    """Kraft und Moment jedes Stabs auf seine beiden Verbinder, Form je Stab, Summen je Verbinder."""
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
    for q in range(mod.nv):
        F = np.zeros(3)
        Tq = np.zeros(3)
        for m, (i, j, _) in enumerate(mod.staebe):
            if q == i:
                F += Fi[m]
                Tq += Ti_alle[m]
            elif q == j:
                F += Fj[m]
                Tq += Tj_alle[m]
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


def form(mod, x):
    xf = mod.voll(x)
    X = np.array([xf[mod.basis(q):mod.basis(q) + 3] for q in range(mod.nv)])
    achse = X[1] - X[0]
    la = float(np.linalg.norm(achse))
    u = achse / la
    radien = []
    hoehen = []
    for q in range(2, mod.nv):
        w = X[q] - X[0]
        hoehen.append(float(w @ u))
        w = w - (w @ u) * u
        radien.append(float(np.linalg.norm(w)))
    return {"achse": la, "ringradius": radien, "ring_hoehe_ab_A": hoehen, "ecken": X.tolist()}


def wunschwinkel(mod, q):
    eintr = []
    for m, (i, j, _) in enumerate(mod.staebe):
        if q == i:
            eintr.append((f"{i}-{j}", mod.d0i_np[m]))
        elif q == j:
            eintr.append((f"{j}-{i}", mod.d0j_np[m]))
    aus = []
    for a in range(len(eintr)):
        for b in range(a + 1, len(eintr)):
            c = float(np.clip(eintr[a][1] @ eintr[b][1], -1.0, 1.0))
            aus.append([eintr[a][0], eintr[b][0], math.degrees(math.acos(c))])
    return aus


def main():
    (name, n_tet, N, lag, wunsch, anstoss, amp, achse_l0, hesse_an, pfad) = (
        sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6], float(sys.argv[7]),
        float(sys.argv[8]), int(sys.argv[9]), sys.argv[10])
    t0 = time.time()
    mod = Modell(n_tet, N, lag, wunsch, anstoss, amp, achse_l0)
    x0 = mod.xvoll0[mod.frei].copy()
    E0 = mod.energie(x0)
    x, phasen, verlauf, ev = loesen(mod, x0, t0)
    meldung = phasen[-1]["meldung"]
    gn = float(np.linalg.norm(mod.gradient(x)))
    staebe, knoten = lasten(mod, x)
    teile = mod.f_T(mod.lokal(mod.voll(x)), mod.D0I, mod.D0J, mod.L0).numpy()
    je_art = {}
    for art in ("achse", "speiche", "ring"):
        idx = [m for m, s in enumerate(mod.staebe) if s[2] == art]
        je_art[art] = {"anzahl": len(idx), "dehnung": float(teile[idx, 0].sum()),
                       "biegung_innen": float(teile[idx, 1].sum()), "einspannung": float(teile[idx, 2].sum())}
    out = {"name": name, "n_tet": n_tet, "N": N, "lagerung": lag, "wunsch": wunsch, "anstoss": anstoss, "amp": amp,
           "achse_l0": achse_l0, "B": B, "L": L, "Ks": KS, "nx_frei": int(len(x)), "anzahl_staebe": mod.R,
           "anzahl_ecken": mod.nv, "feste_komponenten": mod.fest.tolist(), "energie_start": E0,
           "energie": mod.energie(x), "energie_je_art": je_art, "gradnorm": gn, "newton_schritte": len(verlauf),
           "newton_verlauf": verlauf, "newton_meldung": meldung, "phasen": phasen, "anzahl_stoesse": len(phasen) - 1,
           "stabil": bool(ev[0] > INSTABIL), "staebe": staebe, "knoten": knoten,
           "form": form(mod, x), "wunschwinkel_A": wunschwinkel(mod, 0), "wunschwinkel_r0": wunschwinkel(mod, 2),
           "start_sehnen": [float(np.linalg.norm(mod.P[j] - mod.P[i])) for (i, j, _) in mod.staebe]}
    out["hesse_kleinste"] = [float(v) for v in ev[:24]]
    out["hesse_groesste"] = float(ev[-1])
    out["hesse_arg"] = hesse_an
    out["sek"] = time.time() - t0
    with open(pfad + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1)
    os.replace(pfad + ".tmp", pfad)
    frei_rest = max(max(kn["rest_F"], kn["rest_tau"]) for kn in knoten)
    print(f"{name}: n_tet {n_tet}, N {N}, {lag}/{wunsch}, Anstoss {anstoss} {amp}, Achse l0 {achse_l0}, nx {len(x)}, "
          f"Newton {len(verlauf)} ({meldung}), Stoesse {len(phasen) - 1}, |grad| {gn:.1e}, "
          f"E {out['energie']:.8e} (Start {E0:.3e}), stabil {out['stabil']}, "
          f"Rest frei {frei_rest:.1e}, {out['sek']:.1f} s", flush=True)
    for art in ("achse", "speiche", "ring"):
        st = [s for s in staebe if s["art"] == art]
        if not st:
            continue
        ax = [s["F_i_axial"] for s in st]
        print(f"  {art}: axial {min(ax):+.6e} .. {max(ax):+.6e}, Stich max {max(s['stich'] for s in st):.4e}, "
              f"tau max {max(max(s['tau_i_betrag'], s['tau_j_betrag']) for s in st):.4e}, "
              f"E dehn {je_art[art]['dehnung']:.4e} bieg {je_art[art]['biegung_innen']:.4e} "
              f"einsp {je_art[art]['einspannung']:.4e}", flush=True)
    f = out["form"]
    print(f"  Achse {f['achse']:.6f}, Ringradius {min(f['ringradius']):.6f} .. {max(f['ringradius']):.6f}, "
          f"Ringhoehe ab A {min(f['ring_hoehe_ab_A']):.6f} .. {max(f['ring_hoehe_ab_A']):.6f}, "
          f"Hesse kleinste {[float('%.3e' % v) for v in out['hesse_kleinste'][:4]]}", flush=True)
    for ph in phasen:
        print(f"  Phase {ph['phase']}: {ph['schritte']} Schritte ({ph['meldung']}), E {ph['energie']:.8e}, "
              f"kleinster EW {ph['hesse_kleinste'][0]:.3e}, Stoss {ph.get('stoss')}", flush=True)


if __name__ == "__main__":
    main()
