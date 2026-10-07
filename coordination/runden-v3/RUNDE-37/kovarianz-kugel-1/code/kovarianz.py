#!/usr/bin/env python3
"""KOVARIANZ-KUGEL-1 (Runde 41, Code-Agent): gepaarte, rotationssymmetrische Verformungen der S^4-Netze.

Grundlage unveraendert: kugel.py (INDUZIERT-KUGEL-1, sha256 c2a4d790...) und kugel2.py (INDUZIERT-KUGEL-2, 15dcbd85...).
Rundes Netz und Regel Q genau wie KUGEL-2 (Saatschluessel [20261004, 39, 4, N, saat]); Gamma_Q(rund) muss bitgleich sein.

Jede Verformung X ist eine rotationssymmetrische Metrik g = e^(2 sigma(theta)) g0 auf der Kugel vom Radius a (theta =
Winkel zur Achse e5), in der konformen Karte gegeben (jede O(4)-symmetrische Metrik auf S^4 ist konform flach) und auf
Volumen N normiert (Int e^(4 sigma) dV0 = V0). Dieselbe Bauvorschrift fuer alle X:
  1. Punkte: dieselben Zufallspunkte wie das runde Netz, je Punkt nur theta verschoben (monotone Umordnung, Breitenrichtung
     w fest), so dass die Dichte e^(4 sigma) dV0 ist, also Dichte 1 bezueglich g.
  2. Netz: neu gebaut, konvexe Huelle der verschobenen Punkte in der konformen Karte (= Delaunay bezueglich der
     konformen Struktur von g; Moebius-invariant, fuer konform flache g intrinsisch).
  3. Laengen (Regel QI, Urteil): Sehnen in R^5 der isometrischen Einbettung von (S^4, g) als Rotationshyperflaeche
     (Profil s = e^sigma sin theta, z' = -sqrt(e^(2 sigma) - s'^2)); je Simplex auf das g-Volumen seines
     Grosskreis-Simplex skaliert (wie Regel Q). Fassung roh. Nebenlesart CI: dieselben Sehnen ohne Skalierung, Fassung
     korr (wie Regel C).
Verformungen: M (Nullprobe) sigma = -ln(cosh t + sinh t cos theta) (Moebius, isometrisch zur runden Kugel);
  K (konform l = 2) sigma = eps (1 - 5 cos^2 theta) + c; E (gestauchte Kugel) Rotationsellipsoid mit Achsenverhaeltnis
  lam, konforme Karte durch Begradigung d theta~/sin theta~ = d l/s.
Kontinuum: Delta S = Int sqrt(g) R - 32 pi^2 a^2 = a^2 [Omega3 Int e^(2 sigma)(12 + 6 sigma'^2) sin^3 - 32 pi^2];
  Vorhersage y = beta Delta S_Einheit/(32 pi^2) mit y = Delta Gamma/sqrt(N).

Aufruf (nur ueber kleintest.sh):
  python kovarianz.py vorab <aus.json>
  python kovarianz.py kontrolle <aus.json>
  python kovarianz.py messung <aus.json> <N-Liste> <saat0> <anzahl> [blind=0/1]
  python kovarianz.py auswertung <laufordner> <kugel2-laufordner> <aus.json>
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

N_DIM = 4
PAARE = k1.PAARE[N_DIM]
OMEGA3 = 2.0 * math.pi ** 2
V0E = 8.0 * math.pi ** 2 / 3.0          # Volumen der Einheits-S^4
S0E = 32.0 * math.pi ** 2               # Int R dV der Einheits-S^4
GLX, GLW = np.polynomial.legendre.leggauss(10)
ZELLEN = 8192

# Festlegungen (PLAN)
T_M = 0.2                                # Moebius-Schub
EPS_K = -0.1                             # konforme l = 2-Amplitude (Vorzeichen: Profil einbettbar)
LAM_E = math.exp(-0.5)                   # gestauchte Kugel: Achsenverhaeltnis q/p
BETA_Q = (-1.613, 0.052)                 # KUGEL-2, Regel Q roh (Karte)
BETA_C = (-1.455, 0.053)                 # KUGEL-1/-2, Regel C korr (Nebenlesart CI)
VERF_NAMEN = ("M", "K", "E")


def gl_zellen(f, a, b):
    """Integral von f ueber [a, b] je Eintrag (10-Punkt-Gauss-Legendre)."""
    m = 0.5 * (b - a)
    c = 0.5 * (b + a)
    tot = np.zeros(np.broadcast(a, b).shape)
    for x, w in zip(GLX, GLW):
        tot = tot + w * f(c + m * x)
    return tot * m


class Verformung:
    """Rotationssymmetrische konforme Metrik e^(2 sigma(theta)) g0, sigma als Hermite-Spline auf einem Gitter."""

    def __init__(self, name, th, sig, dsig, par):
        self.name, self.par = name, par
        sp0 = CubicHermiteSpline(th, sig, dsig)
        self.th = th
        f_vol = lambda t: np.exp(4.0 * sp0(t)) * np.sin(t) ** 3
        ivol = math.fsum(gl_zellen(f_vol, th[:-1], th[1:]).tolist())
        self.c_norm = -0.25 * math.log(ivol / (4.0 / 3.0))
        self.sp = CubicHermiteSpline(th, sig + self.c_norm, dsig)
        self.dsp = self.sp.derivative()
        dz = gl_zellen(self.dichte, th[:-1], th[1:])
        self.cum = np.concatenate([[0.0], np.cumsum(dz)])
        self.total = self.cum[-1]
        self.cum = self.cum / self.total
        self.vol_rel = self.total / (4.0 / 3.0)
        arg = np.exp(2.0 * self.sp(th)) - self.sprime(th) ** 2
        self.profil_min = float(np.min(arg))
        dzc = gl_zellen(self.zint, th[:-1], th[1:])
        self.zcum = np.concatenate([[0.0], np.cumsum(dz * 0.0 + dzc)])
        self.z_half = 0.5 * self.zcum[-1]
        f_s = lambda t: np.exp(2.0 * self.sp(t)) * (12.0 + 6.0 * self.dsp(t) ** 2) * np.sin(t) ** 3
        self.S = OMEGA3 * math.fsum(gl_zellen(f_s, th[:-1], th[1:]).tolist())
        self.dS = self.S - S0E

    def sigma(self, t):
        return self.sp(t)

    def dichte(self, t):
        return np.exp(4.0 * self.sp(t)) * np.sin(t) ** 3

    def sprime(self, t):
        return np.exp(self.sp(t)) * (self.dsp(t) * np.sin(t) + np.cos(t))

    def zint(self, t):
        return np.sqrt(np.maximum(np.exp(2.0 * self.sp(t)) - self.sprime(t) ** 2, 0.0))

    def zelle(self, t):
        return np.clip(np.searchsorted(self.th, t, side="right") - 1, 0, len(self.th) - 2)

    def transport(self, theta):
        """theta' mit F_g(theta') = F_0(theta); F_0 = sin^4(theta/2)(2 + cos theta) (Gleichverteilung)."""
        ziel = np.sin(0.5 * theta) ** 4 * (2.0 + np.cos(theta))
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
        """Einbettung als Rotationshyperflaeche (Einheitsmassstab): s(theta), z(theta), Mittelpunkt bei z = 0."""
        k = self.zelle(t)
        zc = self.zcum[k] + gl_zellen(self.zint, self.th[k], t)
        return np.exp(self.sp(t)) * np.sin(t), self.z_half - zc


def gitter(n=ZELLEN):
    return np.linspace(0.0, math.pi, n + 1)


def verf_moebius(t):
    th = gitter()
    den = math.cosh(t) + math.sinh(t) * np.cos(th)
    return Verformung("M", th, -np.log(den), math.sinh(t) * np.sin(th) / den, {"t": t})


def verf_konform(eps, l=2):
    th = gitter()
    if l == 2:
        sig, dsig = eps * (1.0 - 5.0 * np.cos(th) ** 2), eps * 10.0 * np.cos(th) * np.sin(th)
    else:
        sig, dsig = eps * np.cos(th), -eps * np.sin(th)
    return Verformung("K" if l == 2 else "L1", th, sig, dsig, {"eps": eps, "l": l})


def ellipsoid_tabelle(lam, n=ZELLEN):
    """Begradigung des Rotationsellipsoids (Halbachsen 1 (x4), lam): d theta~/sin theta~ = D d phi/sin phi,
    D = sqrt(cos^2 phi + lam^2 sin^2 phi). Rueckgabe theta~, sigma~ = ln(sin phi/sin theta~), d sigma~/d theta~."""
    phi = np.linspace(0.0, math.pi, n + 1)
    D = lambda p: np.sqrt(np.cos(p) ** 2 + lam ** 2 * np.sin(p) ** 2)
    reg = lambda p: (D(p) - 1.0) / np.sin(p)
    dI = gl_zellen(reg, phi[:-1], phi[1:])
    Icum = np.concatenate([[0.0], np.cumsum(dI)])
    I = Icum - Icum[n // 2]                                     # I(pi/2) = 0 (Spiegelsymmetrie)
    tt = 2.0 * np.arctan2(np.sin(0.5 * phi) * np.exp(I), np.cos(0.5 * phi))
    sig = np.log(np.cos(0.5 * phi) ** 2 + np.sin(0.5 * phi) ** 2 * np.exp(2.0 * I)) - I
    dtt = D(phi) * np.exp(-sig)                                 # d theta~/d phi
    with np.errstate(divide="ignore", invalid="ignore"):
        dsig_phi = 1.0 / np.tan(phi) - dtt / np.tan(tt)
        dsig = dsig_phi / dtt
    dsig[0] = 0.0
    dsig[-1] = 0.0
    return tt, sig, dsig, phi


def verf_ellipsoid(lam):
    tt, sig, dsig, _ = ellipsoid_tabelle(lam)
    return Verformung("E", tt, sig, dsig, {"lam": lam})


def gauss_dS_ellipsoid(lam, n=ZELLEN):
    """Unabhaengige Kontrolle: Int R dV des Ellipsoids aus den Hauptkruemmungen (Gauss-Gleichung), Volumen normiert."""
    phi = np.linspace(0.0, math.pi, n + 1)
    D = lambda p: np.sqrt(np.cos(p) ** 2 + lam ** 2 * np.sin(p) ** 2)
    fR = lambda p: (6.0 * (lam / D(p) ** 3) * (lam / D(p)) + 6.0 * (lam / D(p)) ** 2) * np.sin(p) ** 3 * D(p)
    fV = lambda p: np.sin(p) ** 3 * D(p)
    S = OMEGA3 * math.fsum(gl_zellen(fR, phi[:-1], phi[1:]).tolist())
    V = OMEGA3 * math.fsum(gl_zellen(fV, phi[:-1], phi[1:]).tolist())
    return S * math.sqrt(V0E / V) - S0E


def verformungen():
    return {"M": verf_moebius(T_M), "K": verf_konform(EPS_K), "E": verf_ellipsoid(LAM_E)}


# ---------------------------------------------------------------------- Netze
def huellnetz(Pu, a):
    """Huelle, Orientierung und Pruefungen wie kugel.kugelnetz, fuer gegebene Punkte Pu auf der Kugel vom Radius a."""
    n = N_DIM
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
               "kappen_mit_punkt_innen": int(np.sum(innen > 0)), "vol_min": float((nn / 24.0).min())})
    return tri, X, nn, d0, pr


def schluessel(tri, N):
    s = np.sort(tri, axis=1).astype(np.int64)
    k = np.zeros(s.shape[0], dtype=np.int64)
    for j in range(s.shape[1]):
        k = k * np.int64(N) + s[:, j]
    return k


def theta_w(P):
    perp = np.linalg.norm(P[:, :4], axis=1)
    return np.arctan2(perp, P[:, 4]), P[:, :4] / perp[:, None]


def jw_mittel(X, d0, a, verf):
    """Grundmann-Moeller-Mittel (Grad 5) von J(x) e^(4 sigma(x/|x|)) ueber das flache Simplex."""
    gew, pkt = k2.GM5
    acc = np.zeros(X.shape[0])
    for w, b in zip(gew, pkt):
        xq = np.einsum("j,fjk->fk", b, X)
        rq = np.linalg.norm(xq, axis=1)
        thq = np.arctan2(np.linalg.norm(xq[:, :4], axis=1), xq[:, 4])
        acc += w * (a ** N_DIM * d0 / rq ** (N_DIM + 1)) * np.exp(4.0 * verf.sigma(thq))
    return acc


def sehnen2(Y, tri):
    return np.stack([np.einsum("fi,fi->f", Y[tri[:, j]] - Y[tri[:, i]], Y[tri[:, j]] - Y[tri[:, i]])
                     for (i, j) in PAARE], axis=1)


def rundes_netz(N, saat):
    """Wie kugel2.eine_messung fuer Regel C und Q (bitgleich mit KUGEL-2)."""
    n = N_DIM
    kn = k1.kugelnetz(n, N, saat)
    tri, a, V_K = kn["tri"], kn["geo"]["a"], kn["geo"]["V_K"]
    X = kn["P"][tri]
    c = X.mean(axis=1)
    nv = k1.kreuz(X[:, 1:, :] - X[:, :1, :])
    nh = nv / np.linalg.norm(nv, axis=1)[:, None]
    d0 = np.einsum("fi,fi->f", nh, c)
    Jq5 = k2.j_mittel(X, d0, a, n, k2.GM5)
    sqQ = kn["sqC"] * (Jq5 ** (2.0 / n))[:, None]
    regeln = {"Q": k1.auswerten(tri, N, n, sqQ, V_K), "C": k1.auswerten(tri, N, n, kn["sqC"], V_K)}
    return kn, regeln


def verformtes_netz(kn, verf, N, extra=False):
    n = N_DIM
    a, V_K = kn["geo"]["a"], kn["geo"]["V_K"]
    t0 = time.time()
    th, w = theta_w(kn["P"])
    th2, res = verf.transport(th)
    Pu = a * np.concatenate([np.sin(th2)[:, None] * w, np.cos(th2)[:, None]], axis=1)
    tri, X, nn, d0, pr = huellnetz(Pu, a)
    s, z = verf.profil(th2)
    Y = a * np.concatenate([s[:, None] * w, z[:, None]], axis=1)
    sq_ch = sehnen2(Y, tri)
    _, V_ch, lam_ch, _ = k1.p1(sq_ch, n)
    V_g = (nn / math.factorial(n)) * jw_mittel(X, d0, a, verf)
    sq_QI = sq_ch * np.sqrt(V_g / V_ch)[:, None]
    regeln = {"QI": k1.auswerten(tri, N, n, sq_QI, V_K), "CI": k1.auswerten(tri, N, n, sq_ch, V_K)}
    neu = ~np.isin(schluessel(tri, N), schluessel(kn["tri"], N))
    info = {"transport_res_max": res, "theta_versatz_max": float(np.max(np.abs(th2 - th))),
            "F": int(tri.shape[0]), "simplizes_neu": int(np.sum(neu)), "anteil_neu": float(np.mean(neu)),
            "V_g_summe_durch_N": math.fsum(V_g.tolist()) / V_K, "V_ch_durch_N": math.fsum(V_ch.tolist()) / V_K,
            "lam_min_sehnen": float(lam_ch.min()), "faktor_QI_min": float(np.sqrt(np.sqrt(V_g / V_ch)).min()),
            "faktor_QI_max": float(np.sqrt(np.sqrt(V_g / V_ch)).max()), "profil_min": verf.profil_min}
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


# ---------------------------------------------------------------------- Modi
def vorab_daten():
    out = {}
    V = verformungen()
    for name, v in V.items():
        out[name] = {"par": v.par, "c_norm": v.c_norm, "vol_rel": v.vol_rel, "profil_min": v.profil_min,
                     "dS_einheit": v.dS, "dS_durch_S0": v.dS / S0E,
                     "y_pred_Q": BETA_Q[0] * v.dS / S0E, "y_pred_Q_se": BETA_Q[1] * abs(v.dS) / S0E,
                     "y_pred_C": BETA_C[0] * v.dS / S0E, "y_pred_C_se": BETA_C[1] * abs(v.dS) / S0E}
    # Kontrollen der Schreibtischformeln
    yy = 8.0 / 7.0
    koeff2 = 36.0 * yy * V0E                                   # 36 <Y^2> V0 (Einheitskugel, zweite Ordnung)
    out["zweite_ordnung_K"] = {"eps2_koeff": koeff2, "dS_zweite_ordnung": koeff2 * EPS_K ** 2,
                               "y_pred_Q_zweite_ordnung": BETA_Q[0] * koeff2 * EPS_K ** 2 / S0E}
    kl = verf_konform(1e-3)
    out["probe_K_kleines_eps"] = {"dS_durch_eps2": kl.dS / 1e-6, "erwartet": koeff2,
                                  "rel_abw": kl.dS / 1e-6 / koeff2 - 1.0}
    l1 = verf_konform(1e-2, l=1)
    out["probe_l1_kleines_eps"] = {"dS_durch_eps2": l1.dS / 1e-4, "erwartet": 0.0}
    out["probe_E_gauss"] = {"dS_gauss": gauss_dS_ellipsoid(LAM_E), "dS_konform": V["E"].dS,
                            "abw": gauss_dS_ellipsoid(LAM_E) - V["E"].dS}
    # Profilprobe E: eingebettetes Profil gegen Ellipse
    vE = V["E"]
    t = np.linspace(0.0, math.pi, 2001)
    s, z = vE.profil(t)
    A, C = float(vE.profil(np.array([0.5 * math.pi]))[0][0]), float(vE.profil(np.array([0.0]))[1][0])
    out["probe_E_profil"] = {"halbachsen_s_z": [A, C], "verhaeltnis": C / A, "lam": LAM_E,
                             "max_abw_ellipse": float(np.max(np.abs((s / A) ** 2 + (z / C) ** 2 - 1.0)))}
    vM = V["M"]
    s, z = vM.profil(t)
    out["probe_M_profil"] = {"max_abw_kreis": float(np.max(np.abs(s ** 2 + z ** 2 - 1.0)))}
    out["probe_volumen"] = {k: v.vol_rel for k, v in V.items()}
    return out


def modus_vorab(protokoll, out, ziel):
    out["vorab"] = vorab_daten()
    protokoll(json.dumps(out["vorab"], indent=1))
    k1.speichern(ziel, out)


def modus_kontrolle(protokoll, out, ziel):
    n = N_DIM
    V = verformungen()
    # (C1) sigma = 0: Pipeline gibt das runde Netz und Gamma_Q zurueck
    th = gitter()
    v0 = Verformung("0", th, np.zeros_like(th), np.zeros_like(th), {})
    kn, rr = rundes_netz(1000, 991)
    r0 = verformtes_netz(kn, v0, 1000)
    out["C1_sigma0"] = {"anteil_neu": r0["info"]["anteil_neu"], "theta_versatz_max": r0["info"]["theta_versatz_max"],
                        "gamma_QI_minus_Q": r0["regeln"]["QI"]["gamma"] - rr["Q"]["gamma"],
                        "gamma_CI_korr_minus_C_korr": (r0["regeln"]["CI"]["gamma"] + r0["regeln"]["CI"]["korr"])
                        - (rr["C"]["gamma"] + rr["C"]["korr"]), "gueltig": r0["gueltig"]}
    protokoll(f"C1: {out['C1_sigma0']}")
    k1.speichern(ziel, out)
    # (C2) Moebius: Transport = exakte Moebius-Abbildung, Netz gleich, Sehnen gleich; CI exakt null
    rM = verformtes_netz(kn, V["M"], 1000)
    thx, w = theta_w(kn["P"])
    t = T_M
    u5 = np.cos(thx)
    y5 = (-math.sinh(t) + math.cosh(t) * u5) / (math.cosh(t) - math.sinh(t) * u5)
    th_m = np.arccos(np.clip(y5, -1, 1))
    th2, _ = V["M"].transport(thx)
    out["C2_moebius"] = {"transport_gegen_exakt_max": float(np.max(np.abs(th2 - th_m))),
                         "netz_gleich": rM["info"]["M_netz_gleich"],
                         "punkte_gegen_rund_max": rM["info"]["M_punkte_gegen_rund_max"],
                         "gamma_CI_korr_minus_C_korr": (rM["regeln"]["CI"]["gamma"] + rM["regeln"]["CI"]["korr"])
                         - (rr["C"]["gamma"] + rr["C"]["korr"]), "gueltig": rM["gueltig"],
                         "anteil_neu": rM["info"]["anteil_neu"]}
    protokoll(f"C2: {out['C2_moebius']}")
    k1.speichern(ziel, out)
    # (C3) LU gegen dicht fuer QI (N = 400, Saat 990), alle Verformungen
    kb = []
    kn4, _ = rundes_netz(400, 990)
    for name, v in V.items():
        r = verformtes_netz(kn4, v, 400, extra=True)
        e = k1.auswerten(r["_tri"], 400, n, r["_sq"], kn4["geo"]["V_K"], dicht=True)
        Kd = e["_K"].toarray()
        ev = np.linalg.eigvalsh(Kd)
        sgn, ld = np.linalg.slogdet(Kd + 1.0 / 400)
        gev = sla.eigh(Kd, np.diag(e["_m"]), eigvals_only=True)
        kb.append({"verf": name, "gueltig": r["gueltig"], "abw_eigen": abs(e["gamma"] - 0.5 * math.fsum(np.log(ev[1:]).tolist())),
                   "abw_slogdet": abs(e["gamma"] - 0.5 * ld), "vorzeichen": float(sgn),
                   "gammaM_abw": abs(e["gamma_M"] - 0.5 * math.fsum(np.log(np.sort(gev)[1:]).tolist()))})
        protokoll(f"C3 {name}: {kb[-1]}")
    out["C3_lu_dicht"] = kb
    k1.speichern(ziel, out)
    # (C4) Negativprobe: konforme Sehnen e^((s_i+s_j)/2)|u_i-u_j| (ohne Einbettung) fuer K und E, N = 1000
    neg = {}
    for name in ("K", "E", "M"):
        r = verformtes_netz(kn, V[name], 1000, extra=True)
        thp, _ = theta_w(r["_Pu"])
        sg = V[name].sigma(thp)
        tri = r["_tri"]
        sqc = sehnen2(r["_Pu"], tri) * np.stack([np.exp(sg[tri[:, i]] + sg[tri[:, j]]) for (i, j) in PAARE], axis=1)
        _, _, lam, _ = k1.p1(sqc, n)
        neg[name] = {"nicht_einbettbar": int(np.sum(~(lam > 0))), "F": int(tri.shape[0]),
                     "QI_gueltig": r["gueltig"], "anteil_neu": r["info"]["anteil_neu"]}
        protokoll(f"C4 {name}: {neg[name]}")
    out["C4_konforme_sehnen"] = neg
    out["vorab"] = vorab_daten()
    k1.speichern(ziel, out)
    return out


MESSWERTE = ("gamma", "gamma_M", "sum_log_m")


def modus_messung(Nlist, saat0, anzahl, blind, protokoll, out, ziel):
    V = verformungen()
    out.update({"n": N_DIM, "Nlist": Nlist, "saat0": saat0, "anzahl": anzahl, "blind": blind, "messungen": [],
                "par": {k: v.par for k, v in V.items()}})
    streu = {}
    for saat in range(saat0, saat0 + anzahl):
        for N in Nlist:
            t0 = time.time()
            kn, rr = rundes_netz(N, saat)
            prr = kn["pruefung"]
            rec = {"N": N, "saat": saat, "rund": {"regeln": rr, "gueltig": bool(k1.kugel_gueltig(prr, N_DIM) and all(
                k1.lu_ok(rr[r]["lu"]) for r in rr)), "F": int(kn["tri"].shape[0]), "geo": kn["geo"]}, "verf": {}}
            for name in VERF_NAMEN:
                rec["verf"][name] = verformtes_netz(kn, V[name], N)
            rec["sekunden"] = time.time() - t0
            rec["rss_mb"] = k1.rss_mb()
            gq = rr["Q"]["gamma"]
            for name in VERF_NAMEN:
                if rec["verf"][name]["gueltig"] and rec["rund"]["gueltig"]:
                    streu.setdefault(f"N{N}/{name}/QI", []).append(
                        (rec["verf"][name]["regeln"]["QI"]["gamma"] - gq) / math.sqrt(N))
            zeile = " ".join(f"{nm}: ok {rec['verf'][nm]['gueltig']} neu {rec['verf'][nm]['info']['anteil_neu']:.3f} "
                             f"t {rec['verf'][nm]['sekunden']:.1f}s" for nm in VERF_NAMEN)
            protokoll(f"N={N} saat={saat}: rund ok {rec['rund']['gueltig']}; {zeile}; gesamt {rec['sekunden']:.1f} s, "
                      f"RSS {k1.rss_mb():.0f} MB")
            if blind:
                for rg in list(rec["rund"]["regeln"].values()) + [r for nm in VERF_NAMEN
                                                                   for r in rec["verf"][nm]["regeln"].values()]:
                    for q in MESSWERTE:
                        rg.pop(q, None)
                out["blind_streuung"] = {k: {"std_y": float(np.std(v, ddof=1)) if len(v) > 1 else None,
                                             "anzahl": len(v)} for k, v in streu.items()}
            out["messungen"].append(rec)
            k1.speichern(ziel, out)
    return out


# ---------------------------------------------------------------------- Auswertung
def lade(ordner):
    recs = {}
    dateien = sorted(glob.glob(os.path.join(ordner, "messung-*.json")))
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
    return {"mittel": m, "std": s, "se": s / math.sqrt(v.size), "t": m / (s / math.sqrt(v.size)) if s > 0 else None,
            "anzahl": int(v.size), "neg": int(np.sum(v < 0))}


def modus_auswertung(ordner, k2ordner, ziel, protokoll):
    recs, dateien = lade(ordner)
    vb = vorab_daten()
    Ns = sorted({k[1] for k in recs})
    saaten = sorted({k[0] for k in recs})
    out = {"dateien": dateien, "Ns": Ns, "vorab": vb}
    # Tor
    gute = []
    aus = []
    unvollst = []
    for s in saaten:
        if not all((s, N) in recs for N in Ns):
            unvollst.append(s)
            continue
        ok = all(recs[(s, N)]["rund"]["gueltig"] and all(
            recs[(s, N)]["verf"][x]["gueltig"] for x in VERF_NAMEN) for N in Ns)
        (gute if ok else aus).append(s)
    vollst = len(saaten) - len(unvollst)
    out["tor"] = {"saaten": len(saaten), "unvollstaendig": unvollst, "vollstaendig": vollst, "gut": len(gute),
                  "ausgeschlossen": aus, "bestanden": bool(len(gute) >= 20 and len(aus) <= 0.1 * vollst)}
    # K0: Gamma_Q und Gamma_C rund bitgleich mit KUGEL-2
    k2recs, _ = lade(k2ordner) if os.path.isdir(k2ordner) else ({}, [])
    vgl, gleich, maxabw = 0, 0, 0.0
    for (s, N), r in recs.items():
        if (s, N) in k2recs:
            for rg in ("Q", "C"):
                a_, b_ = r["rund"]["regeln"][rg]["gamma"], k2recs[(s, N)]["kugel"]["regeln"][rg]["gamma"]
                vgl += 1
                gleich += int(a_ == b_)
                maxabw = max(maxabw, abs(a_ - b_))
    out["K0_bitgleich"] = {"verglichen": vgl, "gleich": gleich, "max_abw": maxabw,
                           "eingetroffen": bool(vgl > 0 and gleich == vgl)}
    # Messgroessen
    res = {}
    for x in VERF_NAMEN:
        for regel, basis, fass in (("QI", "Q", "roh"), ("CI", "C", "korr")):
            yj, ytab, fits = [], {N: [] for N in Ns}, []
            for s in gute:
                ys = []
                for N in Ns:
                    r = recs[(s, N)]
                    gx = r["verf"][x]["regeln"][regel]["gamma"]
                    gb = r["rund"]["regeln"][basis]["gamma"]
                    if fass == "korr":
                        gx += r["verf"][x]["regeln"][regel]["korr"]
                        gb += r["rund"]["regeln"][basis]["korr"]
                    y = (gx - gb) / math.sqrt(N)
                    ys.append(y)
                    ytab[N].append(y)
                yj.append(float(np.mean(ys)))
                if len(Ns) >= 2:
                    A = np.stack([np.ones(len(Ns)), 1.0 / np.sqrt(np.array(Ns, dtype=float))], axis=1)
                    fits.append(np.linalg.lstsq(A, np.array(ys), rcond=None)[0])
            fits = np.array(fits) if fits else np.zeros((0, 2))
            pred = vb[x]["y_pred_Q" if regel == "QI" else "y_pred_C"]
            pse = vb[x]["y_pred_Q_se" if regel == "QI" else "y_pred_C_se"]
            st = stat(yj)
            res[f"{x}/{regel}"] = {
                "b": st, "y_je_N": {str(N): stat(ytab[N]) for N in Ns},
                "zweiparameter": {"b": stat(fits[:, 0]) if len(fits) else None,
                                  "d": stat(fits[:, 1]) if len(fits) else None},
                "pred": pred, "pred_se": pse,
                "verhaeltnis_b_pred": st["mittel"] / pred if pred != 0 else None,
                "abstand_in_se_komb": (st["mittel"] - pred) / math.hypot(st["se"], pse) if st.get("se") else None}
    out["messgroessen"] = res
    # Netzstatistik
    nst = {}
    for x in VERF_NAMEN:
        for N in Ns:
            vals = [recs[(s, N)]["verf"][x]["info"] for s in gute]
            nst[f"{x}/N{N}"] = {"anteil_neu": float(np.mean([v["anteil_neu"] for v in vals])),
                                "V_g_summe_durch_N_max_abw": float(max(abs(v["V_g_summe_durch_N"] - 1) for v in vals)),
                                "V_ch_durch_N": float(np.mean([v["V_ch_durch_N"] for v in vals])),
                                "transport_res_max": float(max(v["transport_res_max"] for v in vals)),
                                "lam_min_sehnen": float(min(v["lam_min_sehnen"] for v in vals))}
            if x == "M":
                nst[f"{x}/N{N}"]["netz_gleich"] = int(sum(v["M_netz_gleich"] for v in vals))
                nst[f"{x}/N{N}"]["punkte_gegen_rund_max"] = float(max(v["M_punkte_gegen_rund_max"] for v in vals))
    out["netze"] = nst
    # Urteile
    M_, K_, E_ = res["M/QI"], res["K/QI"], res["E/QI"]

    def u(b):
        return "eingetroffen" if b else "nicht eingetroffen"
    tor = out["tor"]["bestanden"]
    urt = {}
    if not tor:
        for kv in ("KV0", "KV1", "KV2", "KV3"):
            urt[kv] = {"plan": "nicht auswertbar (Tor)", "karte": "nicht auswertbar (Tor)"}
    else:
        bM, sM = M_["b"]["mittel"], M_["b"]["se"]
        bK, sK = K_["b"]["mittel"], K_["b"]["se"]
        bE, sE = E_["b"]["mittel"], E_["b"]["se"]
        kv0 = abs(bM) <= 2 * sM
        urt["KV0"] = {"karte": u(kv0), "plan": u(kv0), "b_M": bM, "se": sM, "in_se": bM / sM,
                      "b_M_durch_pred_K": bM / K_["pred"]}
        kv1 = bK <= -3 * sK
        urt["KV1"] = {"karte": u(kv1), "plan": u(kv1), "b_K": bK, "se": sK, "in_se": bK / sK, "pred_K": K_["pred"]}
        kv2 = bE >= 3 * sE
        urt["KV2"] = {"karte": u(kv2), "plan": u(kv2), "b_E": bE, "se": sE, "in_se": bE / sE, "pred_E": E_["pred"],
                      "einstein_lesart_b_E_kleiner_minus_3SE": bool(bE <= -3 * sE)}
        rk, re_ = bK / K_["pred"], bE / E_["pred"]
        kv3 = abs(rk - 1) <= 0.3 and abs(re_ - 1) <= 0.3
        urt["KV3"] = {"karte": u(kv3), "plan": u(kv3), "b_K_durch_pred_K": rk, "b_E_durch_pred_E": re_,
                      "K_vertraeglich_2SE": bool(abs(K_["abstand_in_se_komb"]) <= 2),
                      "E_vertraeglich_2SE": bool(abs(E_["abstand_in_se_komb"]) <= 2)}
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
        modus_kontrolle(protokoll, out, ziel)
    elif modus == "messung":
        ziel = sys.argv[2]
        Nlist = [int(x) for x in sys.argv[3].split(",")]
        saat0, anzahl = int(sys.argv[4]), int(sys.argv[5])
        opt = dict(a.split("=", 1) for a in sys.argv[6:])
        modus_messung(Nlist, saat0, anzahl, opt.get("blind", "0") == "1", protokoll, out, ziel)
    elif modus == "auswertung":
        ziel = sys.argv[4]
        out = modus_auswertung(sys.argv[2], sys.argv[3], ziel, protokoll)
    else:
        raise SystemExit("unbekannter Modus")
    out["laufzeit_gesamt_s"] = time.time() - t0
    out["protokoll"] = log
    k1.speichern(ziel, out)
    print("geschrieben", ziel, f"{time.time() - t0:.1f} s", flush=True)


if __name__ == "__main__":
    main()
