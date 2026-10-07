#!/usr/bin/env python3
"""KOVARIANZ-2D-GEGENPROBE (Runde 41, Code-Agent): die Verformungs-Vorschrift von KOVARIANZ-KUGEL-1 (kovarianz.py,
unveraendert kopiert, sha256 bed2c12a...) Schritt fuer Schritt fuer allgemeines n. Hauptfall n = 2 (S^2).
Kontrolle K4D: derselbe Code mit n = 4 muss die Werte von kovarianz.py (live aufgerufen und aus dessen Laufdateien)
wiedergeben; dann ist der 2D-Lauf derselbe Codepfad wie der 4D-Lauf.

Grundlage unveraendert: kugel.py (INDUZIERT-KUGEL-1, c2a4d790...), kugel2.py (INDUZIERT-KUGEL-2, 15dcbd85...).
Bauvorschrift (wie kovarianz.py, n statt 4):
  0. Rundes Netz: k1.kugelnetz(n, N, saat) (Saatschluessel [20261004, 39, n, N, saat]); Regel Q (Sehnen je Simplex auf
     das Volumen des Grosskreis-Simplex skaliert, Grundmann-Moeller Grad 5) und Regel C (Sehnen).
  1. Punkte: dieselben Zufallspunkte, je Punkt nur theta verschoben (monotone Umordnung, Faserrichtung w fest), Dichte
     e^(n sigma) dV0, also Dichte 1 bezueglich g = e^(2 sigma) g0.
  2. Netz: neu gebaut, konvexe Huelle der verschobenen Punkte in der konformen Karte (Kugel vom Radius a).
  3. Laengen QI: Sehnen der isometrischen Einbettung als Rotationsflaeche (s = e^sigma sin theta,
     z' = -sqrt(e^(2 sigma) - s'^2)), je Simplex auf das g-Volumen seines Grosskreis-Simplex in der Karte skaliert.
     CI: dieselben Sehnen ohne Skalierung (Diagnose "ohne Volumenzuordnung je Simplex"). Fuer n = 2 haengen die
     Kotangens-Gewichte nur von Winkeln ab: Gamma(QI) = Gamma(CI) bis auf Rundung; nur Gamma_M sieht die Zuordnung.
  Gamma = 1/2 log det' K (k1.auswerten, roh), Gamma_M = 1/2 log det'(M^-1 K) wie kugel.py.
Verformungen (n = 2): M sigma = -ln(cosh t + sinh t cos theta), t = 0,2 (Moebius, isometrisch);
  K sigma = eps (1 - (n+1) cos^2 theta) + c (l = 2), eps in EPS_LISTE; dazu eps = +0,05 (Gegenvorzeichen, beschreibend).
Kontinuum (n = 2, Flaeche fest): Delta Gamma_P = -(1/(12 pi)) [1/2 Int |grad sigma|^2 dOmega + Int sigma dOmega]
  (Polyakov-Alvarez, Osgood-Phillips-Sarnak; die Haelfte von Delta log det' Delta_g), unabhaengig von N.

Aufruf (nur ueber kleintest.sh):
  python kovarianz2d.py vorab <aus.json>
  python kovarianz2d.py kontrolle <aus.json> <kovarianz-kugel-laufordner>
  python kovarianz2d.py messung <aus.json> <N-Liste> <saat0> <anzahl> [blind=0/1]
  python kovarianz2d.py auswertung <laufordner> <kugel1-laufordner> <aus.json>
"""
import glob
import json
import math
import os
import sys
import time

import numpy as np
import scipy
import scipy.linalg as sla
from scipy.interpolate import CubicHermiteSpline
from scipy.spatial import ConvexHull, cKDTree

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kugel as k1   # noqa: E402  (unveraendert aus INDUZIERT-KUGEL-1)
import kugel2 as k2  # noqa: E402  (unveraendert aus INDUZIERT-KUGEL-2)

N_HAUPT_DIM = 2
OMEGA3 = 2.0 * math.pi ** 2              # wie kovarianz.py (nur n = 4)
S0E = 32.0 * math.pi ** 2                # wie kovarianz.py (nur n = 4)
SININT = {2: 2.0, 4: 4.0 / 3.0}          # Int_0^pi sin^(n-1) theta d theta
GM5 = {2: k2.gm_regel(2, 2), 4: k2.GM5}
GLX, GLW = np.polynomial.legendre.leggauss(10)
ZELLEN = 8192

# Festlegungen (PLAN)
T_M = 0.2                                     # Moebius-Schub (wie KOVARIANZ-KUGEL-1)
EPS_LISTE = (-0.025, -0.05, -0.1, -0.2, -0.4)  # l = 2-Amplituden (Vorzeichen wie KOVARIANZ-KUGEL-1)
EPS_GEGEN = 0.05                              # Gegenvorzeichen (beschreibend)
EPS_HAUPT = -0.1                              # Hauptamplitude (wie KOVARIANZ-KUGEL-1)
KAPPA_GROB = (1.075, 0.071)                   # INDUZIERT-DICHTE-2D-GROB, c(0)/P
KAPPA_DICHTE = (0.924, 0.087)                 # INDUZIERT-DICHTE-2D, Fenster-Steigung/P
N_HAUPT = (1000, 2000, 4000)                  # Hauptschaetzer; N = 8000 beschreibend
E_FIT = (-0.1, -0.2, -0.4)                    # KG1-Steigung (PLAN Abschnitt 6)
EPS_KG3 = -0.4                                # KG3-Amplitude (PLAN Abschnitt 6)


def k_name(eps):
    return f"K{eps:+g}"


VERF_NAMEN = ("M",) + tuple(k_name(e) for e in EPS_LISTE) + (k_name(EPS_GEGEN),)


def gl_zellen(f, a, b):
    """Integral von f ueber [a, b] je Eintrag (10-Punkt-Gauss-Legendre)."""
    m = 0.5 * (b - a)
    c = 0.5 * (b + a)
    tot = np.zeros(np.broadcast(a, b).shape)
    for x, w in zip(GLX, GLW):
        tot = tot + w * f(c + m * x)
    return tot * m


class Verformung:
    """Rotationssymmetrische konforme Metrik e^(2 sigma(theta)) g0 auf S^n, sigma als Hermite-Spline."""

    def __init__(self, name, th, sig, dsig, par, n):
        self.name, self.par, self.n = name, par, n
        sp0 = CubicHermiteSpline(th, sig, dsig)
        self.th = th
        f_vol = lambda t: np.exp(n * sp0(t)) * np.sin(t) ** (n - 1)
        ivol = math.fsum(gl_zellen(f_vol, th[:-1], th[1:]).tolist())
        self.c_norm = -(1.0 / n) * math.log(ivol / SININT[n])
        self.sp = CubicHermiteSpline(th, sig + self.c_norm, dsig)
        self.dsp = self.sp.derivative()
        dz = gl_zellen(self.dichte, th[:-1], th[1:])
        self.cum = np.concatenate([[0.0], np.cumsum(dz)])
        self.total = self.cum[-1]
        self.cum = self.cum / self.total
        self.vol_rel = self.total / SININT[n]
        arg = np.exp(2.0 * self.sp(th)) - self.sprime(th) ** 2
        self.profil_min = float(np.min(arg))
        dzc = gl_zellen(self.zint, th[:-1], th[1:])
        self.zcum = np.concatenate([[0.0], np.cumsum(dz * 0.0 + dzc)])
        self.z_half = 0.5 * self.zcum[-1]
        if n == 4:
            f_s = lambda t: np.exp(2.0 * self.sp(t)) * (12.0 + 6.0 * self.dsp(t) ** 2) * np.sin(t) ** 3
            self.S = OMEGA3 * math.fsum(gl_zellen(f_s, th[:-1], th[1:]).tolist())
            self.dS = self.S - S0E
        else:
            # Polyakov-Funktional auf der Einheitskugel: PF = 2 pi Int (1/2 sigma'^2 + sigma) sin theta d theta
            f_p = lambda t: (0.5 * self.dsp(t) ** 2 + self.sp(t)) * np.sin(t)
            self.PF = 2.0 * math.pi * math.fsum(gl_zellen(f_p, th[:-1], th[1:]).tolist())
            self.dG_P = -self.PF / (12.0 * math.pi)

    def sigma(self, t):
        return self.sp(t)

    def dichte(self, t):
        return np.exp(self.n * self.sp(t)) * np.sin(t) ** (self.n - 1)

    def sprime(self, t):
        return np.exp(self.sp(t)) * (self.dsp(t) * np.sin(t) + np.cos(t))

    def zint(self, t):
        return np.sqrt(np.maximum(np.exp(2.0 * self.sp(t)) - self.sprime(t) ** 2, 0.0))

    def zelle(self, t):
        return np.clip(np.searchsorted(self.th, t, side="right") - 1, 0, len(self.th) - 2)

    def transport(self, theta):
        """theta' mit F_g(theta') = F_0(theta); F_0 = Verteilungsfunktion der Gleichverteilung auf S^n."""
        if self.n == 4:
            ziel = np.sin(0.5 * theta) ** 4 * (2.0 + np.cos(theta))
        else:
            ziel = np.sin(0.5 * theta) ** 2
        k = np.clip(np.searchsorted(self.cum, ziel, side="right") - 1, 0, len(self.th) - 2)
        lo, hi = self.th[k], self.th[k + 1]
        frac = np.clip((ziel - self.cum[k]) / (self.cum[k + 1] - self.cum[k]), 0.0, 1.0)
        t = lo + frac * (hi - lo)
        for _ in range(10):
            F = self.cum[k] + gl_zellen(self.dichte, lo, t) / self.total
            f = self.dichte(t) / self.total
            t = np.clip(t - (F - ziel) / np.maximum(f, 1e-300), lo, hi)
        res = self.cum[k] + gl_zellen(self.dichte, lo, t) / self.total - ziel
        return t, float(np.max(np.abs(res)))

    def profil(self, t):
        """Einbettung als Rotationsflaeche (Einheitsmassstab): s(theta), z(theta), Mittelpunkt bei z = 0."""
        k = self.zelle(t)
        zc = self.zcum[k] + gl_zellen(self.zint, self.th[k], t)
        return np.exp(self.sp(t)) * np.sin(t), self.z_half - zc


def gitter(n=ZELLEN):
    return np.linspace(0.0, math.pi, n + 1)


def verf_moebius(t, n):
    th = gitter()
    den = math.cosh(t) + math.sinh(t) * np.cos(th)
    return Verformung("M", th, -np.log(den), math.sinh(t) * np.sin(th) / den, {"t": t}, n)


def verf_konform(eps, n, name=None):
    th = gitter()
    kk = float(n + 1)
    sig, dsig = eps * (1.0 - kk * np.cos(th) ** 2), eps * (2.0 * kk) * np.cos(th) * np.sin(th)
    return Verformung(name or k_name(eps), th, sig, dsig, {"eps": eps, "l": 2}, n)


def verformungen(n=N_HAUPT_DIM):
    V = {"M": verf_moebius(T_M, n)}
    for e in EPS_LISTE + (EPS_GEGEN,):
        V[k_name(e)] = verf_konform(e, n)
    return V


# ---------------------------------------------------------------------- Netze
def gauss_bonnet(tri, sq, N):
    """n = 2: Summe der Winkeldefizite (Descartes) minus 4 pi; mit k1.regge wie kugel.eine_messung."""
    _, _, _, Gam = k1.p1(sq, 2)
    rg = k1.regge(tri, sq, Gam, 2, N)[0]
    return rg - 4.0 * math.pi


def huellnetz(Pu, a, n):
    """Huelle, Orientierung und Pruefungen wie kugel.kugelnetz, fuer gegebene Punkte Pu auf der Kugel vom Radius a."""
    Nh = Pu.shape[0]
    t0 = time.time()
    hull = ConvexHull(Pu)
    t_qh = time.time() - t0
    tri = np.ascontiguousarray(hull.simplices, dtype=np.int64)
    eqn = hull.equations[:, :n + 1]
    X = Pu[tri]
    c = X.mean(axis=1)
    nv = k1.kreuz(X[:, 1:, :] - X[:, :1, :])
    flip = np.einsum("fi,fi->f", nv, c) < 0
    tri[flip] = tri[flip][:, [1, 0] + list(range(2, n + 1))]
    X = Pu[tri]
    nv = k1.kreuz(X[:, 1:, :] - X[:, :1, :])
    nn = np.linalg.norm(nv, axis=1)
    nh = nv / nn[:, None]
    d0 = np.einsum("fi,fi->f", nh, c)
    q = a * nh
    r = np.min(np.linalg.norm(X - q[:, None, :], axis=2), axis=1)
    baum = cKDTree(Pu)
    innen = baum.query_ball_point(q, r * (1.0 - 1e-9), return_length=True)
    top = k1.topologie(tri, Nh, n)
    pr = dict(top)
    pr.update({"N_huelle": int(Nh), "F": int(tri.shape[0]), "F_je_N": tri.shape[0] / Nh, "sek_qhull": t_qh,
               "orient_umgedreht": int(np.sum(flip)), "d0_min": float(d0.min()),
               "normale_gegen_qhull_min_cos": float(np.min(np.einsum("fi,fi->f", nh, eqn))),
               "kappen_mit_punkt_innen": int(np.sum(innen > 0)),
               "vol_min": float((nn / float(math.factorial(n))).min())})
    return tri, X, nn, d0, pr


def schluessel(tri, N):
    s = np.sort(tri, axis=1).astype(np.int64)
    k = np.zeros(s.shape[0], dtype=np.int64)
    for j in range(s.shape[1]):
        k = k * np.int64(N) + s[:, j]
    return k


def theta_w(P, n):
    perp = np.linalg.norm(P[:, :n], axis=1)
    return np.arctan2(perp, P[:, n]), P[:, :n] / perp[:, None]


def jw_mittel(X, d0, a, verf, n):
    """Grundmann-Moeller-Mittel (Grad 5) von J(x) e^(n sigma(x/|x|)) ueber das flache Simplex."""
    gew, pkt = GM5[n]
    acc = np.zeros(X.shape[0])
    for w, b in zip(gew, pkt):
        xq = np.einsum("j,fjk->fk", b, X)
        rq = np.linalg.norm(xq, axis=1)
        thq = np.arctan2(np.linalg.norm(xq[:, :n], axis=1), xq[:, n])
        acc += w * (a ** n * d0 / rq ** (n + 1)) * np.exp(n * verf.sigma(thq))
    return acc


def sehnen2(Y, tri, n):
    return np.stack([np.einsum("fi,fi->f", Y[tri[:, j]] - Y[tri[:, i]], Y[tri[:, j]] - Y[tri[:, i]])
                     for (i, j) in k1.PAARE[n]], axis=1)


def rundes_netz(N, saat, n=N_HAUPT_DIM):
    """Wie kovarianz.rundes_netz (dort n = 4) fuer Regel C und Q; n = 2 zusaetzlich Gauss-Bonnet-Pruefung."""
    kn = k1.kugelnetz(n, N, saat)
    tri, a, V_K = kn["tri"], kn["geo"]["a"], kn["geo"]["V_K"]
    X = kn["P"][tri]
    c = X.mean(axis=1)
    nv = k1.kreuz(X[:, 1:, :] - X[:, :1, :])
    nh = nv / np.linalg.norm(nv, axis=1)[:, None]
    d0 = np.einsum("fi,fi->f", nh, c)
    Jq5 = k2.j_mittel(X, d0, a, n, GM5[n])
    sqQ = kn["sqC"] * (Jq5 ** (2.0 / n))[:, None]
    regeln = {"Q": k1.auswerten(tri, N, n, sqQ, V_K), "C": k1.auswerten(tri, N, n, kn["sqC"], V_K)}
    if n == 2:
        kn["pruefung"]["gauss_bonnet_abw"] = gauss_bonnet(tri, kn["sqC"], N)
    return kn, regeln


def verformtes_netz(kn, verf, N, n=N_HAUPT_DIM, extra=False):
    a, V_K = kn["geo"]["a"], kn["geo"]["V_K"]
    t0 = time.time()
    th, w = theta_w(kn["P"], n)
    th2, res = verf.transport(th)
    Pu = a * np.concatenate([np.sin(th2)[:, None] * w, np.cos(th2)[:, None]], axis=1)
    tri, X, nn, d0, pr = huellnetz(Pu, a, n)
    s, z = verf.profil(th2)
    Y = a * np.concatenate([s[:, None] * w, z[:, None]], axis=1)
    sq_ch = sehnen2(Y, tri, n)
    _, V_ch, lam_ch, _ = k1.p1(sq_ch, n)
    V_g = (nn / math.factorial(n)) * jw_mittel(X, d0, a, verf, n)
    if n == 4:
        sq_QI = sq_ch * np.sqrt(V_g / V_ch)[:, None]
    else:
        sq_QI = sq_ch * ((V_g / V_ch) ** (2.0 / n))[:, None]
    regeln = {"QI": k1.auswerten(tri, N, n, sq_QI, V_K), "CI": k1.auswerten(tri, N, n, sq_ch, V_K)}
    if n == 2:
        pr["gauss_bonnet_abw"] = gauss_bonnet(tri, sq_ch, N)
    neu = ~np.isin(schluessel(tri, N), schluessel(kn["tri"], N))
    fak = (V_g / V_ch) ** (1.0 / n)
    info = {"transport_res_max": res, "theta_versatz_max": float(np.max(np.abs(th2 - th))),
            "F": int(tri.shape[0]), "simplizes_neu": int(np.sum(neu)), "anteil_neu": float(np.mean(neu)),
            "V_g_summe_durch_N": math.fsum(V_g.tolist()) / V_K, "V_ch_durch_N": math.fsum(V_ch.tolist()) / V_K,
            "lam_min_sehnen": float(lam_ch.min()), "faktor_QI_min": float(fak.min()),
            "faktor_QI_max": float(fak.max()), "profil_min": verf.profil_min}
    if verf.name == "M":
        info["M_punkte_gegen_rund_max"] = float(np.max(np.abs(Y - kn["P"])) / a)
        info["M_netz_gleich"] = bool(int(np.sum(neu)) == 0 and tri.shape[0] == kn["tri"].shape[0])
    pr_ok = k1.kugel_gueltig(pr, n)
    lu = {r: k1.lu_ok(regeln[r]["lu"]) for r in regeln}
    rec = {"pruefung": pr, "kugel_gueltig": pr_ok, "lu_ok": lu, "info": info, "regeln": regeln,
           "gueltig": bool(pr_ok and all(lu.values()) and res <= 1e-10 and verf.profil_min >= -1e-12),
           "sekunden": time.time() - t0}
    if extra:
        rec["_tri"], rec["_sq"], rec["_Pu"], rec["_X"], rec["_d0"] = tri, sq_QI, Pu, X, d0
    return rec


# ---------------------------------------------------------------------- Vorab (Kontinuum)
def scherung(verf, m=20001):
    """Lokale Scherung der Transportabbildung (n = 2): ln(Streckung in theta / Streckung in phi), in g gemessen."""
    th = np.linspace(1e-4, math.pi - 1e-4, m)
    t2, _ = verf.transport(th)
    dt = np.gradient(t2, th)
    lr = np.log(dt * np.sin(th) / np.sin(t2))
    gw = np.sin(th) / np.sum(np.sin(th))
    return {"rms": float(np.sqrt(np.sum(gw * lr ** 2))), "max_abs": float(np.max(np.abs(lr)))}


def vorab_daten():
    out = {}
    V = verformungen(2)
    for name, v in V.items():
        out[name] = {"par": v.par, "c_norm": v.c_norm, "vol_rel": v.vol_rel, "profil_min": v.profil_min,
                     "PF": v.PF, "dG_P": v.dG_P,
                     "pred_GROB": KAPPA_GROB[0] * v.dG_P, "pred_GROB_se": KAPPA_GROB[1] * abs(v.dG_P),
                     "pred_DICHTE": KAPPA_DICHTE[0] * v.dG_P, "pred_DICHTE_se": KAPPA_DICHTE[1] * abs(v.dG_P),
                     "scherung": scherung(v)}
        if "eps" in v.par:
            out[name]["dG_P_zweite_ordnung"] = -(8.0 / 15.0) * v.par["eps"] ** 2
    # Polyakov-Steigungen (exakt) zwischen benachbarten Amplituden und als Ausgleich ueber E_FIT
    eps = np.array(EPS_LISTE)
    dg = np.array([V[k_name(e)].dG_P for e in EPS_LISTE])
    out["steigung_P_paarweise"] = {f"{EPS_LISTE[i]:g}/{EPS_LISTE[i + 1]:g}":
                                   float(math.log(dg[i + 1] / dg[i]) / math.log(eps[i + 1] / eps[i]))
                                   for i in range(len(EPS_LISTE) - 1)}
    ef = np.array(E_FIT)
    dgf = np.array([V[k_name(e)].dG_P for e in E_FIT])
    out["steigung_P_E_FIT"] = float(np.polyfit(np.log(np.abs(ef)), np.log(np.abs(dgf)), 1)[0])
    # Proben: kleines eps (zweite Ordnung -8/15), l = 1 (Moebius) exakt 0, Volumen
    kl = verf_konform(1e-3, 2, "klein")
    out["probe_klein"] = {"dG_P_durch_eps2": kl.dG_P / 1e-6, "erwartet": -8.0 / 15.0,
                          "rel_abw": kl.dG_P / 1e-6 / (-8.0 / 15.0) - 1.0}
    out["probe_M"] = {"PF": V["M"].PF, "erwartet": 0.0}
    t = np.linspace(0.0, math.pi, 2001)
    s, z = V["M"].profil(t)
    out["probe_M_profil"] = {"max_abw_kreis": float(np.max(np.abs(s ** 2 + z ** 2 - 1.0)))}
    out["probe_volumen"] = {k: v.vol_rel for k, v in V.items()}
    # Gitter-Wellenzahl von l = 2 (Laplace-Eigenwert 6/a^2 in Einheiten des Netzabstands, Dichte 1)
    out["k2_l2_je_N"] = {str(N): 6.0 * 4.0 * math.pi / N for N in (1000, 2000, 4000, 8000)}
    return out


# ---------------------------------------------------------------------- Modi
def modus_vorab(protokoll, out, ziel):
    out["vorab"] = vorab_daten()
    protokoll(json.dumps(out["vorab"], indent=1))
    k1.speichern(ziel, out)


def modus_kontrolle(kov_lauf, protokoll, out, ziel):
    n = 2
    V = verformungen(2)
    # (C1) sigma = 0: Pipeline gibt das runde Netz und Gamma zurueck
    th = gitter()
    v0 = Verformung("0", th, np.zeros_like(th), np.zeros_like(th), {}, n)
    kn, rr = rundes_netz(1000, 991, n)
    r0 = verformtes_netz(kn, v0, 1000, n)
    out["C1_sigma0"] = {"anteil_neu": r0["info"]["anteil_neu"], "theta_versatz_max": r0["info"]["theta_versatz_max"],
                        "gamma_QI_minus_Q": r0["regeln"]["QI"]["gamma"] - rr["Q"]["gamma"],
                        "gamma_CI_minus_C": r0["regeln"]["CI"]["gamma"] - rr["C"]["gamma"],
                        "gammaM_QI_minus_Q": r0["regeln"]["QI"]["gamma_M"] - rr["Q"]["gamma_M"],
                        "gueltig": r0["gueltig"], "rund_gueltig": k1.kugel_gueltig(kn["pruefung"], n),
                        "gauss_bonnet_rund": kn["pruefung"]["gauss_bonnet_abw"]}
    protokoll(f"C1: {out['C1_sigma0']}")
    k1.speichern(ziel, out)
    # (C2) Moebius: Transport = exakte Moebius-Abbildung, Netz gleich, Punkte gleich; Gamma (QI und CI) gleich
    rM = verformtes_netz(kn, V["M"], 1000, n)
    thx, w = theta_w(kn["P"], n)
    t = T_M
    u5 = np.cos(thx)
    y5 = (-math.sinh(t) + math.cosh(t) * u5) / (math.cosh(t) - math.sinh(t) * u5)
    th_m = np.arccos(np.clip(y5, -1, 1))
    th2, _ = V["M"].transport(thx)
    out["C2_moebius"] = {"transport_gegen_exakt_max": float(np.max(np.abs(th2 - th_m))),
                         "netz_gleich": rM["info"]["M_netz_gleich"],
                         "punkte_gegen_rund_max": rM["info"]["M_punkte_gegen_rund_max"],
                         "gamma_CI_minus_C": rM["regeln"]["CI"]["gamma"] - rr["C"]["gamma"],
                         "gamma_QI_minus_Q": rM["regeln"]["QI"]["gamma"] - rr["Q"]["gamma"],
                         "gueltig": rM["gueltig"], "anteil_neu": rM["info"]["anteil_neu"]}
    protokoll(f"C2: {out['C2_moebius']}")
    k1.speichern(ziel, out)
    # (C3) LU gegen dicht (N = 400, Saat 990) fuer QI, Verformungen M, K-0.1, K-0.4
    kb = []
    kn4, _ = rundes_netz(400, 990, n)
    for name in ("M", k_name(-0.1), k_name(-0.4)):
        r = verformtes_netz(kn4, V[name], 400, n, extra=True)
        e = k1.auswerten(r["_tri"], 400, n, r["_sq"], kn4["geo"]["V_K"], dicht=True)
        Kd = e["_K"].toarray()
        ev = np.linalg.eigvalsh(Kd)
        sgn, ld = np.linalg.slogdet(Kd + 1.0 / 400)
        gev = sla.eigh(Kd, np.diag(e["_m"]), eigvals_only=True)
        kb.append({"verf": name, "gueltig": r["gueltig"],
                   "abw_eigen": abs(e["gamma"] - 0.5 * math.fsum(np.log(ev[1:]).tolist())),
                   "abw_slogdet": abs(e["gamma"] - 0.5 * ld), "vorzeichen": float(sgn),
                   "gammaM_abw": abs(e["gamma_M"] - 0.5 * math.fsum(np.log(np.sort(gev)[1:]).tolist()))})
        protokoll(f"C3 {name}: {kb[-1]}")
    out["C3_lu_dicht"] = kb
    k1.speichern(ziel, out)
    # (C5) n = 2: Gamma haengt nicht von der Volumenzuordnung je Simplex ab (QI gegen CI), N = 1000, Saat 991
    c5 = {}
    for name in VERF_NAMEN:
        r = verformtes_netz(kn, V[name], 1000, n)
        c5[name] = {"gamma_QI_minus_CI": r["regeln"]["QI"]["gamma"] - r["regeln"]["CI"]["gamma"],
                    "gammaM_QI_minus_CI": r["regeln"]["QI"]["gamma_M"] - r["regeln"]["CI"]["gamma_M"],
                    "gueltig": r["gueltig"], "anteil_neu": r["info"]["anteil_neu"],
                    "gauss_bonnet": r["pruefung"]["gauss_bonnet_abw"]}
    c5["rund_Q_minus_C"] = rr["Q"]["gamma"] - rr["C"]["gamma"]
    out["C5_skaleninvarianz"] = c5
    protokoll(f"C5: {c5}")
    k1.speichern(ziel, out)
    # (K4D) derselbe Code mit n = 4 gegen kovarianz.py live und gegen dessen Laufdatei (Saat 0, N = 1000)
    import kovarianz as kov  # noqa: E402  (unveraendert aus KOVARIANZ-KUGEL-1)
    k4 = {}
    knA, rrA = rundes_netz(1000, 0, 4)
    knB, rrB = kov.rundes_netz(1000, 0)
    VA = {"M": verf_moebius(kov.T_M, 4), "K": verf_konform(kov.EPS_K, 4, "K")}
    VB = {"M": kov.verf_moebius(kov.T_M), "K": kov.verf_konform(kov.EPS_K)}
    gesp = None
    for d in sorted(glob.glob(os.path.join(kov_lauf, "messung-N1000-*.json"))):
        with open(d) as f:
            o = json.load(f)
        for rec in o.get("messungen", []):
            if rec["saat"] == 0 and rec["N"] == 1000:
                gesp = rec
    werte = {}
    for rg in ("Q", "C"):
        werte[f"rund/{rg}"] = (rrA[rg]["gamma"], rrB[rg]["gamma"],
                               gesp["rund"]["regeln"][rg]["gamma"] if gesp else None)
        werte[f"rund/{rg}/M"] = (rrA[rg]["gamma_M"], rrB[rg]["gamma_M"],
                                 gesp["rund"]["regeln"][rg]["gamma_M"] if gesp else None)
    for x in ("M", "K"):
        ra = verformtes_netz(knA, VA[x], 1000, 4)
        rb = kov.verformtes_netz(knB, VB[x], 1000)
        for rg in ("QI", "CI"):
            werte[f"{x}/{rg}"] = (ra["regeln"][rg]["gamma"], rb["regeln"][rg]["gamma"],
                                  gesp["verf"][x]["regeln"][rg]["gamma"] if gesp else None)
            werte[f"{x}/{rg}/M"] = (ra["regeln"][rg]["gamma_M"], rb["regeln"][rg]["gamma_M"],
                                    gesp["verf"][x]["regeln"][rg]["gamma_M"] if gesp else None)
        werte[f"{x}/anteil_neu"] = (ra["info"]["anteil_neu"], rb["info"]["anteil_neu"],
                                    gesp["verf"][x]["info"]["anteil_neu"] if gesp else None)
    k4["werte_generisch_live_gespeichert"] = werte
    k4["gespeichert_gefunden"] = gesp is not None
    k4["max_abw_live"] = max(abs(v[0] - v[1]) for v in werte.values())
    k4["max_abw_gespeichert"] = max(abs(v[0] - v[2]) for v in werte.values()) if gesp else None
    k4["bitgleich_live"] = all(v[0] == v[1] for v in werte.values())
    k4["bitgleich_gespeichert"] = bool(gesp) and all(v[0] == v[2] for v in werte.values())
    out["K4D"] = k4
    protokoll(f"K4D: max_abw_live {k4['max_abw_live']}, max_abw_gespeichert {k4['max_abw_gespeichert']}, "
              f"bitgleich live {k4['bitgleich_live']}, gespeichert {k4['bitgleich_gespeichert']}")
    out["vorab"] = vorab_daten()
    k1.speichern(ziel, out)
    return out


MESSWERTE = ("gamma", "gamma_M", "sum_log_m")


def modus_messung(Nlist, saat0, anzahl, blind, protokoll, out, ziel):
    n = N_HAUPT_DIM
    V = verformungen(n)
    out.update({"n": n, "Nlist": Nlist, "saat0": saat0, "anzahl": anzahl, "blind": blind, "messungen": [],
                "par": {k: v.par for k, v in V.items()}})
    streu = {}
    for saat in range(saat0, saat0 + anzahl):
        for N in Nlist:
            t0 = time.time()
            kn, rr = rundes_netz(N, saat, n)
            prr = kn["pruefung"]
            rec = {"N": N, "saat": saat, "rund": {"regeln": rr, "gueltig": bool(k1.kugel_gueltig(prr, n) and all(
                k1.lu_ok(rr[r]["lu"]) for r in rr)), "F": int(kn["tri"].shape[0]), "geo": kn["geo"],
                "gauss_bonnet_abw": prr["gauss_bonnet_abw"]}, "verf": {}}
            for name in VERF_NAMEN:
                rec["verf"][name] = verformtes_netz(kn, V[name], N, n)
            rec["sekunden"] = time.time() - t0
            rec["rss_mb"] = k1.rss_mb()
            for name in VERF_NAMEN:
                if rec["verf"][name]["gueltig"] and rec["rund"]["gueltig"]:
                    for q in ("gamma", "gamma_M"):
                        streu.setdefault(f"N{N}/{name}/QI/{q}", []).append(
                            rec["verf"][name]["regeln"]["QI"][q] - rr["Q"][q])
            zeile = " ".join(f"{nm}: ok {rec['verf'][nm]['gueltig']} neu {rec['verf'][nm]['info']['anteil_neu']:.3f}"
                             for nm in VERF_NAMEN)
            protokoll(f"N={N} saat={saat}: rund ok {rec['rund']['gueltig']}; {zeile}; gesamt {rec['sekunden']:.2f} s, "
                      f"RSS {k1.rss_mb():.0f} MB")
            if blind:
                for rg in list(rec["rund"]["regeln"].values()) + [r for nm in VERF_NAMEN
                                                                   for r in rec["verf"][nm]["regeln"].values()]:
                    for q in MESSWERTE:
                        rg.pop(q, None)
                out["blind_streuung"] = {k: {"std_delta": float(np.std(v, ddof=1)) if len(v) > 1 else None,
                                             "anzahl": len(v)} for k, v in streu.items()}
            out["messungen"].append(rec)
            k1.speichern(ziel, out)
    return out


# ---------------------------------------------------------------------- Auswertung
def lade(ordner, muster="messung-*.json"):
    recs = {}
    dateien = sorted(glob.glob(os.path.join(ordner, muster)))
    for d in dateien:
        with open(d) as f:
            o = json.load(f)
        for r in o.get("messungen", []):
            recs[(r["saat"], r["N"])] = r
    return recs, [os.path.basename(d) for d in dateien]


def stat(v):
    v = np.asarray(v, dtype=float)
    if v.size < 2:
        return {"mittel": float(v.mean()) if v.size else None, "se": None, "anzahl": int(v.size)}
    m, s = float(v.mean()), float(v.std(ddof=1))
    se = s / math.sqrt(v.size)
    return {"mittel": m, "std": s, "se": se, "t": m / se if se > 0 else None,
            "anzahl": int(v.size), "neg": int(np.sum(v < 0))}


LESARTEN = {"G_QI": ("QI", "Q", "gamma", False), "G_CI": ("CI", "C", "gamma", False),
            "GM_QI": ("QI", "Q", "gamma_M", False), "GM_CI_korr": ("CI", "C", "gamma_M", True)}


def wert(rd, q, korr):
    v = rd[q]
    if korr:
        v += rd["korr_M" if q == "gamma_M" else "korr"]
    return v


def delta(rec, x, lesart):
    rg, basis, q, korr = LESARTEN[lesart]
    return wert(rec["verf"][x]["regeln"][rg], q, korr) - wert(rec["rund"]["regeln"][basis], q, korr)


def log_steigung(eps, b):
    b = np.asarray(b, dtype=float)
    if np.any(b == 0) or not (np.all(b < 0) or np.all(b > 0)):
        return None
    return float(np.polyfit(np.log(np.abs(np.asarray(eps))), np.log(np.abs(b)), 1)[0])


def steigung_jackknife(dmat, eps):
    """dmat (Saaten, Amplituden): Ausgleichssteigung von ln abs(b) gegen ln abs(eps), SE per Jackknife ueber Saaten."""
    M = dmat.shape[0]
    b = dmat.mean(axis=0)
    s = log_steigung(eps, b)
    jk = [log_steigung(eps, (b * M - dmat[j]) / (M - 1)) for j in range(M)]
    if s is None or any(v is None for v in jk):
        return s, None
    jk = np.array(jk)
    return s, float(math.sqrt((M - 1) / M * np.sum((jk - jk.mean()) ** 2)))


def modus_auswertung(ordner, k1ordner, ziel, protokoll):
    recs, dateien = lade(ordner)
    vb = vorab_daten()
    Ns = sorted({k[1] for k in recs})
    saaten = sorted({k[0] for k in recs})
    out = {"dateien": dateien, "Ns": Ns, "N_haupt": list(N_HAUPT), "vorab": vb,
           "festlegungen": {"EPS_LISTE": EPS_LISTE, "EPS_GEGEN": EPS_GEGEN, "EPS_HAUPT": EPS_HAUPT, "E_FIT": E_FIT,
                            "EPS_KG3": EPS_KG3, "KAPPA_GROB": KAPPA_GROB, "T_M": T_M}}
    # Tor (ueber N_HAUPT; N = 8000 beschreibend)
    gute, aus, unvollst = [], [], []
    for s in saaten:
        if not all((s, N) in recs for N in N_HAUPT):
            unvollst.append(s)
            continue
        ok = all(recs[(s, N)]["rund"]["gueltig"] and all(
            recs[(s, N)]["verf"][x]["gueltig"] for x in VERF_NAMEN) for N in N_HAUPT)
        (gute if ok else aus).append(s)
    vollst = len(saaten) - len(unvollst)
    out["tor"] = {"saaten": len(saaten), "unvollstaendig": unvollst, "vollstaendig": vollst, "gut": len(gute),
                  "ausgeschlossen": aus, "bestanden": bool(len(gute) >= 20 and len(aus) <= 0.1 * vollst)}
    extra_N = [N for N in Ns if N not in N_HAUPT]
    gute_extra = {N: [s for s in gute if (s, N) in recs and recs[(s, N)]["rund"]["gueltig"] and all(
        recs[(s, N)]["verf"][x]["gueltig"] for x in VERF_NAMEN)] for N in extra_N}
    out["tor"]["extra_N_gute_saaten"] = {str(N): len(v) for N, v in gute_extra.items()}
    out["tor"]["extra_N_ungueltig"] = {str(N): sorted(set(s for s in gute if (s, N) in recs) - set(v))
                                       for N, v in gute_extra.items()}
    # K0: Gamma_C rund (n = 2) bitgleich mit INDUZIERT-KUGEL-1 (dort n = 2, N = 4000, 16000, 64000)
    k1recs, _ = lade(k1ordner, "messung-n2-*.json") if os.path.isdir(k1ordner) else ({}, [])
    vgl, gleich, maxabw = 0, 0, 0.0
    for (s, N), r in recs.items():
        if (s, N) in k1recs:
            a_, b_ = r["rund"]["regeln"]["C"]["gamma"], k1recs[(s, N)]["kugel"]["regeln"]["C"]["gamma"]
            vgl += 1
            gleich += int(a_ == b_)
            maxabw = max(maxabw, abs(a_ - b_))
    out["K0_bitgleich"] = {"verglichen": vgl, "gleich": gleich, "max_abw": maxabw,
                           "eingetroffen": bool(vgl > 0 and gleich == vgl)}
    # Messgroessen: je Verformung und Lesart
    res = {}
    dmats = {}
    for x in VERF_NAMEN:
        for les in LESARTEN:
            dj, tab, fitN = [], {N: [] for N in Ns}, []
            for s in gute:
                ys = [delta(recs[(s, N)], x, les) for N in N_HAUPT]
                for N, y in zip(N_HAUPT, ys):
                    tab[N].append(y)
                dj.append(float(np.mean(ys)))
            for N in extra_N:
                for s in gute_extra[N]:
                    tab[N].append(delta(recs[(s, N)], x, les))
            dmats[(x, les)] = np.array(dj)
            pred = vb[x]["pred_GROB"]
            pse = vb[x]["pred_GROB_se"]
            st = stat(dj)
            jeN = {str(N): stat(tab[N]) for N in Ns}
            for N in Ns:
                if jeN[str(N)]["mittel"] is not None:
                    jeN[str(N)]["y_durch_wurzelN"] = jeN[str(N)]["mittel"] / math.sqrt(N)
                    jeN[str(N)]["je_punkt"] = jeN[str(N)]["mittel"] / N
            # beschreibend: lineare Abhaengigkeit von N (gewichteter Ausgleich der N-Mittel, b = beta + alpha N)
            xs = np.array([float(N) for N in Ns if jeN[str(N)].get("se")])
            ys_ = np.array([jeN[str(N)]["mittel"] for N in Ns if jeN[str(N)].get("se")])
            ws = np.array([1.0 / jeN[str(N)]["se"] ** 2 for N in Ns if jeN[str(N)].get("se")])
            if xs.size >= 2:
                A = np.stack([np.ones_like(xs), xs], axis=1) * np.sqrt(ws)[:, None]
                coef, *_ = np.linalg.lstsq(A, ys_ * np.sqrt(ws), rcond=None)
                cov = np.linalg.inv(A.T @ A)
                lin = {"beta": float(coef[0]), "alpha_je_N": float(coef[1]),
                       "alpha_se": float(math.sqrt(cov[1, 1])), "beta_se": float(math.sqrt(cov[0, 0]))}
            else:
                lin = None
            res[f"{x}/{les}"] = {
                "b": st, "je_N": jeN, "pred_GROB": pred, "pred_GROB_se": pse, "dG_P": vb[x]["dG_P"],
                "verhaeltnis_b_pred": st["mittel"] / pred if pred != 0 else None,
                "abstand_in_se_komb": (st["mittel"] - pred) / math.hypot(st["se"], pse) if st.get("se") else None,
                "linear_in_N": lin}
    out["messgroessen"] = res
    # Steigungen (Lesart G_QI und GM_QI): E_FIT, paarweise, alle fuenf
    stg = {}
    for les in ("G_QI", "GM_QI", "G_CI", "GM_CI_korr"):
        for name, eset in (("E_FIT", E_FIT), ("alle", EPS_LISTE), ("klein3", EPS_LISTE[:3])):
            dm = np.stack([dmats[(k_name(e), les)] for e in eset], axis=1)
            s_, se_ = steigung_jackknife(dm, eset)
            stg[f"{les}/{name}"] = {"steigung": s_, "se": se_, "eps": list(eset)}
        for i in range(len(EPS_LISTE) - 1):
            e1, e2 = EPS_LISTE[i], EPS_LISTE[i + 1]
            dm = np.stack([dmats[(k_name(e1), les)], dmats[(k_name(e2), les)]], axis=1)
            s_, se_ = steigung_jackknife(dm, (e1, e2))
            stg[f"{les}/paar/{e1:g}/{e2:g}"] = {"steigung": s_, "se": se_}
    out["steigungen"] = stg
    # Zusatz (vorab festgelegt, beschreibend): b(eps) = A1 abs(eps) + A2 eps^2 ueber die fuenf negativen Amplituden,
    # je Saat (N-Mittel) und je N; Polyakov-Bezug aus denselben Ausgleich der exakten Kontinuumswerte
    E5 = np.array(EPS_LISTE)
    Dm = np.stack([np.abs(E5), E5 ** 2], axis=1)
    refP = np.linalg.lstsq(Dm, np.array([vb[k_name(e)]["dG_P"] for e in EPS_LISTE]), rcond=None)[0]
    zus = {"polyakov_A1_A2": [float(refP[0]), float(refP[1])]}
    for les in ("G_QI", "GM_QI", "G_CI", "GM_CI_korr"):
        dm = np.stack([dmats[(k_name(e), les)] for e in EPS_LISTE], axis=1)
        coef = np.linalg.lstsq(Dm, dm.T, rcond=None)[0]
        zus[les] = {"A1": stat(coef[0]), "A2": stat(coef[1])}
        for N in Ns:
            ss = gute if N in N_HAUPT else gute_extra[N]
            if len(ss) < 2:
                continue
            dN = np.stack([np.array([delta(recs[(s, N)], k_name(e), les) for s in ss]) for e in EPS_LISTE], axis=1)
            cN = np.linalg.lstsq(Dm, dN.T, rcond=None)[0]
            zus[les][f"N{N}"] = {"A1": stat(cN[0]), "A2": stat(cN[1]), "A1_je_punkt": float(np.mean(cN[0])) / N}
    out["zusatz_A1_A2"] = zus
    # Netzstatistik
    nst = {}
    for x in VERF_NAMEN:
        for N in Ns:
            ss = gute if N in N_HAUPT else gute_extra[N]
            vals = [recs[(s, N)]["verf"][x]["info"] for s in ss]
            if not vals:
                continue
            nst[f"{x}/N{N}"] = {"anteil_neu": float(np.mean([v["anteil_neu"] for v in vals])),
                                "V_g_summe_durch_N_max_abw": float(max(abs(v["V_g_summe_durch_N"] - 1) for v in vals)),
                                "V_ch_durch_N": float(np.mean([v["V_ch_durch_N"] for v in vals])),
                                "transport_res_max": float(max(v["transport_res_max"] for v in vals)),
                                "lam_min_sehnen": float(min(v["lam_min_sehnen"] for v in vals)),
                                "gauss_bonnet_max": float(max(abs(recs[(s, N)]["verf"][x]["pruefung"]["gauss_bonnet_abw"])
                                                              for s in ss))}
            if x == "M":
                nst[f"{x}/N{N}"]["netz_gleich"] = int(sum(v["M_netz_gleich"] for v in vals))
                nst[f"{x}/N{N}"]["punkte_gegen_rund_max"] = float(max(v["M_punkte_gegen_rund_max"] for v in vals))
        nst[f"rund/sekunden_je_N"] = {str(N): float(np.mean([recs[(s, N)]["sekunden"] for s in
                                                             (gute if N in N_HAUPT else gute_extra[N])]))
                                      for N in Ns if (gute if N in N_HAUPT else gute_extra[N])}
    out["netze"] = nst
    # Urteile (Lesart G_QI)
    def u(b):
        return "eingetroffen" if b else "nicht eingetroffen"
    urt = {}
    if not out["tor"]["bestanden"]:
        for kg in ("KG0", "KG1", "KG2", "KG3"):
            urt[kg] = {"plan": "nicht auswertbar (Tor)", "karte": "nicht auswertbar (Tor)"}
    else:
        kH = k_name(EPS_HAUPT)
        M_ = res["M/G_QI"]
        KH = res[f"{kH}/G_QI"]
        bM, sM = M_["b"]["mittel"], M_["b"]["se"]
        predH = KH["pred_GROB"]
        bKH = KH["b"]["mittel"]
        kg0_plan = abs(bM) <= 3 * sM or abs(bM) <= 0.05 * abs(predH)
        kg0_karte = abs(bM) <= 3 * sM or abs(bM) <= 0.05 * abs(bKH)
        urt["KG0"] = {"plan": u(kg0_plan), "karte": u(kg0_karte), "b_M": bM, "se": sM,
                      "in_se": bM / sM if sM else None, "b_M_durch_pred_K": bM / predH,
                      "b_M_durch_b_K": bM / bKH if bKH else None,
                      "Nebenlesart_GM_QI": {"b": res["M/GM_QI"]["b"]["mittel"], "se": res["M/GM_QI"]["b"]["se"],
                                            "eingetroffen_plan": bool(abs(res["M/GM_QI"]["b"]["mittel"]) <= 3 * res[
                                                "M/GM_QI"]["b"]["se"] or abs(res["M/GM_QI"]["b"]["mittel"]) <= 0.05 * abs(
                                                predH))}}
        # KG1: Steigung ueber E_FIT, auswertbar nur wenn jedes b(eps) gleiches Vorzeichen und >= 3 SE
        sig = {f"{e:g}": res[f"{k_name(e)}/G_QI"]["b"] for e in E_FIT}
        ausw = all(abs(v["mittel"]) >= 3 * v["se"] for v in sig.values()) and (
            all(v["mittel"] < 0 for v in sig.values()) or all(v["mittel"] > 0 for v in sig.values()))
        s1 = stg["G_QI/E_FIT"]
        if not ausw or s1["steigung"] is None or s1["se"] is None:
            kg1_plan = "nicht auswertbar (Signal unter 3 SE oder Vorzeichenwechsel)"
            kg1_karte = "nicht auswertbar (Signal unter 3 SE oder Vorzeichenwechsel)"
        else:
            lo, hi = s1["steigung"] - 2 * s1["se"], s1["steigung"] + 2 * s1["se"]
            if lo >= 1.8 and hi <= 2.2:
                kg1_plan = "eingetroffen"
            elif hi < 1.8 or lo > 2.2:
                kg1_plan = "nicht eingetroffen"
            else:
                kg1_plan = "nicht entschieden (2-SE-Intervall schneidet die Grenze)"
            kg1_karte = u(1.8 <= s1["steigung"] <= 2.2)
        urt["KG1"] = {"plan": kg1_plan, "karte": kg1_karte, "steigung": s1["steigung"], "se": s1["se"],
                      "E_FIT": list(E_FIT), "b_je_eps": sig, "steigung_P": vb["steigung_P_E_FIT"]}
        # KG2: Aenderung von N = 1000 auf 4000 bei EPS_HAUPT (Karte = Plan); Zusatz fuer alle Amplituden
        def kg2(x, n_a=N_HAUPT[0], n_b=N_HAUPT[-1]):
            j1, j4 = res[f"{x}/G_QI"]["je_N"][str(n_a)], res[f"{x}/G_QI"]["je_N"][str(n_b)]
            d = j4["mittel"] - j1["mittel"]
            sd = math.hypot(j1["se"], j4["se"])
            ok = abs(d) <= 2 * sd or abs(d) <= 0.1 * abs(j1["mittel"])
            return ok, {"N_a": n_a, "N_b": n_b, "b_a": j1["mittel"], "se_a": j1["se"], "b_b": j4["mittel"],
                        "se_b": j4["se"], "aenderung": d, "se_aenderung": sd, "in_se": d / sd,
                        "rel": d / j1["mittel"] if j1["mittel"] else None}
        ok2, z2 = kg2(kH)
        z2x = None
        if extra_N and all(len(gute_extra[N]) >= 2 for N in extra_N):
            nmax = max(extra_N)
            z2x = {e: dict(kg2(k_name(e), N_HAUPT[0], nmax)[1], eingetroffen=kg2(k_name(e), N_HAUPT[0], nmax)[0])
                   for e in EPS_LISTE + (EPS_GEGEN,)}
        urt["KG2"] = dict(z2, plan=u(ok2), karte=u(ok2), zusatz_alle_amplituden={
            e: dict(kg2(k_name(e))[1], eingetroffen=kg2(k_name(e))[0]) for e in EPS_LISTE + (EPS_GEGEN,)},
            zusatz_bis_Nmax=z2x)
        # KG3: Betrag bei EPS_KG3 gegen kappa_GROB * Polyakov, Intervallregel (Plan) bzw. Punktschaetzer (Karte)
        K3 = res[f"{k_name(EPS_KG3)}/G_QI"]
        b3, s3 = K3["b"]["mittel"], K3["b"]["se"]
        p3 = K3["pred_GROB"]
        r3 = b3 / p3
        sr3 = math.hypot(s3, b3 * KAPPA_GROB[1] / KAPPA_GROB[0]) / abs(p3)
        lo3, hi3 = r3 - 2 * sr3, r3 + 2 * sr3
        if lo3 >= 0.7 and hi3 <= 1.3:
            kg3_plan = "eingetroffen"
        elif hi3 < 0.7 or lo3 > 1.3:
            kg3_plan = "nicht eingetroffen"
        else:
            kg3_plan = "nicht entschieden (2-SE-Intervall schneidet die Grenze)"
        urt["KG3"] = {"plan": kg3_plan, "karte": u(abs(r3 - 1) <= 0.3), "eps": EPS_KG3, "b": b3, "se": s3,
                      "pred_GROB": p3, "dG_P": K3["dG_P"], "verhaeltnis": r3, "se_verhaeltnis": sr3,
                      "verhaeltnis_zu_P": b3 / K3["dG_P"],
                      "zusatz_alle_amplituden": {f"{e:g}": {"b": res[f"{k_name(e)}/G_QI"]["b"]["mittel"],
                                                             "se": res[f"{k_name(e)}/G_QI"]["b"]["se"],
                                                             "verhaeltnis_pred": res[f"{k_name(e)}/G_QI"][
                                                                 "verhaeltnis_b_pred"]}
                                                 for e in EPS_LISTE + (EPS_GEGEN,)}}
    out["urteile"] = urt
    k1.speichern(ziel, out)
    protokoll(json.dumps({"tor": out["tor"], "K0": out["K0_bitgleich"], "urteile": urt}, indent=1))
    return out


def main():
    modus = sys.argv[1]
    t0 = time.time()
    log = []

    def protokoll(s):
        print(s, flush=True)
        log.append(s)

    out = {"modus": modus, "argv": sys.argv[1:], "numpy": np.__version__, "scipy": scipy.__version__}
    if modus == "vorab":
        ziel = sys.argv[2]
        modus_vorab(protokoll, out, ziel)
    elif modus == "kontrolle":
        ziel = sys.argv[2]
        modus_kontrolle(sys.argv[3], protokoll, out, ziel)
    elif modus == "messung":
        ziel = sys.argv[2]
        Nlist = [int(x) for x in sys.argv[3].split(",")]
        saat0, anzahl = int(sys.argv[4]), int(sys.argv[5])
        opt = dict(a.split("=", 1) for a in sys.argv[6:])
        modus_messung(Nlist, saat0, anzahl, opt.get("blind", "0") == "1", protokoll, out, ziel)
    elif modus == "auswertung":
        ziel = sys.argv[4]
        if len(sys.argv) > 5:                      # nur fuer die Codeprobe auf kleinen N
            global N_HAUPT
            N_HAUPT = tuple(int(x) for x in sys.argv[5].split(","))
        out = modus_auswertung(sys.argv[2], sys.argv[3], ziel, protokoll)
    else:
        raise SystemExit("unbekannter Modus")
    out["laufzeit_gesamt_s"] = time.time() - t0
    out["protokoll"] = log
    k1.speichern(ziel, out)
    print("geschrieben", ziel, f"{time.time() - t0:.1f} s", flush=True)


if __name__ == "__main__":
    main()
