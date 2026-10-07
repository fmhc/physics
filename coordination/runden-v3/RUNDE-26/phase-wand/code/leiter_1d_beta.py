#!/usr/bin/env python3
"""LEITER-1D-BETA (Runde 26, PHASE-WAND), Code-Agent (Claude, Anthropic) fuer die Leitung claude-primary, 03.10.2026.
Neue Fassung von RUNDE-25/leiter-1d/code/leiter_1d.py (sha256 f236d377...) fuer beliebiges beta; Karte
coordination/runden-v3/RUNDE-26/phase-wand/KARTE.md, Plan PLAN.md daneben (Abschnitt 5: Liste der Aenderungen).
Alle beta-abhaengigen Groessen kommen aus --konfig (JSON); bei beta = 1/2 rechnet der Code bitgleich wie leiter_1d.py.

Modell M1: U = S - S^2 + beta S^3, S = f^2, omega^2 = omega_min^2 + eps, omega_min^2 = 1 - 1/(4 beta), eine Raumdimension.
Profil exakt aus der ersten Integralform f'^2 = U(f^2) - omega^2 f^2 (Quadratur x(S) geschlossen geloest):
    S(x) = 2 m2 / (1 + 2 sqrt(beta eps) cosh(b x)),  m2 = 1/(4 beta) - eps,  b = 2 sqrt(m2) = sqrt(2 * 2 m2),
    S(0) = S0 = S_c - sqrt(eps/beta) (KLEINERE Wurzel von 1 - omega^2 - S + beta S^2 = 0), S_c = 1/(2 beta).
    beta = 1/2: S(x) = (1 - 2 eps) / (1 + sqrt(2 eps) cosh(sqrt(2 - 4 eps) x)), S0 = 1 - sqrt(2 eps).
Linearisierung (mitrotierend) wie WAND-BETA (RUNDE-24/wand-beta/code/wand_beta.py, Klasse MB):
    A'' = [W - (rho - omega)^2] A + C B,   B'' = C A + [W - (rho + omega)^2] B,
    W = U' + U'' S = 1 - 4 S + 9 beta S^2,   C = U'' S = -2 S + 6 beta S^2.
W-Abbildung: bei X = N h mit N = ceil((x_s + D)/h) (Integrationsbezug x_s: 2 sqrt(beta eps) cosh(b x_s) = 1, wie
leiter_1d.py; nicht die Wandlage der Formel) startet A = 1, A' = -q
(abklingend im geschlossenen Kanal, q = sqrt(1 - (rho - omega)^2)), B = B' = 0 (offener Kanal null); klassisches RK4 mit
festem Schritt h auf dem Gitter x_j = j h nach innen bis x = 0. Normierung exp(-q (X - x_w)) > 0 (aendert weder
Nullstellen noch Umlauf).
    gerade:   (F1, F2) = (A'(0), B'(0))        ungerade: (F1, F2) = (A(0), B(0))
Stille Stelle (BIC) = gemeinsame Nullstelle von (F1, F2) in der Ebene (rho, l), l = ln(1/eps).

Kommandos:
  selbsttest  synthetische W-Abbildung (keine Physik): Scan, Aeste, Verfeinerung, Umlauf gegen bekannte Nullstellen
  k0          Profilproben, ebene Wand rho_z mit demselben RK4, G2-10-Vergleich (omega^2 = 0,55 bis 0,70)
  scan        je eps_j = 10^(-7 + j/40) rho-Abtastung, Nullstellen von F1 je Paritaet (Illinois), F2 dort
  sprossen    Aeste, Vorzeichenwechsel von F2, Verfeinerung, Umlauf-Rechtecke, Gegenproben (D = 40, DOP853)
  regel       mechanische Auswertung: gezaehlte Sprossen, Schritte, PW2 (RUNDE-26 PLAN.md Abschnitt 6)
Alles float64, CPU, ein Faden. Jeder Aufruf braucht --konfig (beta, rho_z, Fenster, eps-Raster, Bezugsschritt).
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import argparse  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402

# Vorbelegung = beta = 1/2 wie leiter_1d.py; ueberschrieben durch lade_konfig (--konfig)
BETA = 0.5
OM2_MIN = 0.5                 # omega_min^2 = 1 - 1/(4 beta)
SC = 1.0                      # S_c = 1/(2 beta)
C9 = 4.5                      # 9 beta
C6 = 3.0                      # 6 beta
C3 = 1.5                      # 3 beta
RHO_Z = 1.5241497621          # ebene Wand (RUNDE-24 WAND-BETA)
B_INF = 2.3100                # Bezugsschritt in ln(1/eps): lambda pi / k_in(rho_z)
BAND = 0.10                   # Toleranz des Schrittkriteriums
E0 = -7.0                     # eps_j = 10^(E0 + j/J_ANZ)
J_ANZ = 40                    # Rasterpunkte je Dekade in eps
J_MAX = 252                   # eps_252 = 10^-0,7 = 0,1995
LEITER_FENSTER = (1.30, 1.70)
LINK = 0.03                   # Aeste: groesster rho-Abstand benachbarter Wurzeln (Rasterschritt 1/40 Dekade)
PARIT = ("gerade", "ungerade")
G210_RHO_B = {0.55: 1.375130, 0.60: 1.380272, 0.65: 1.427327, 0.70: 1.494353}   # G2-10 lauf-69-d1*.log, h = 0,02
G210 = True
KONFIG = {}
T_START = time.time()


def lade_konfig(pfad):
    """Setzt die beta-abhaengigen Modulgroessen aus einer JSON-Datei."""
    global BETA, OM2_MIN, SC, C9, C6, C3, RHO_Z, B_INF, BAND, E0, J_MAX, LEITER_FENSTER, G210, KONFIG
    global EPS_BEREICH
    with open(pfad) as fh:
        K = json.load(fh)
    KONFIG = K
    BETA = float(K["beta"])
    OM2_MIN = 1.0 - 1.0 / (4.0 * BETA)
    SC = 1.0 / (2.0 * BETA)
    C9, C6, C3 = 9.0 * BETA, 6.0 * BETA, 3.0 * BETA
    RHO_Z = float(K["rho_z"])
    B_INF = float(K["schritt_ref"])
    BAND = float(K["band"])
    E0 = float(K["e0"])
    J_MAX = int(K["j_max"])
    LEITER_FENSTER = tuple(float(v) for v in K["fenster"])
    EPS_BEREICH = tuple(float(v) for v in K["eps_bereich"])
    G210 = bool(K.get("g210", False))
    return K


def jetzt():
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


def sek():
    return round(time.time() - T_START, 2)


def log(*a):
    print(f"[{sek():8.1f} s]", *a, flush=True)


def jsonfest(x):
    if isinstance(x, dict):
        return {str(k): jsonfest(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonfest(v) for v in x]
    if isinstance(x, np.ndarray):
        return [jsonfest(v) for v in x.tolist()]
    if isinstance(x, (np.floating, float)):
        v = float(x)
        return v if math.isfinite(v) else str(v)
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, (np.bool_,)):
        return bool(x)
    return x


def schreibe(pfad, obj):
    with open(pfad + ".tmp", "w") as fh:
        json.dump(jsonfest(obj), fh, indent=1)
    os.replace(pfad + ".tmp", pfad)


def eps_j(j):
    return 10.0 ** (E0 + j / J_ANZ)


def par(eps):
    """om, a = 2 sqrt(beta eps), Aa = 2 m2, b = sqrt(2 Aa), x_s (Integrationsbezug, S(x_s) = Aa/2).
    beta = 1/2: bitgleich zu leiter_1d.py (sqrt(4 y) = 2 sqrt(y) und 2 (0,5 - eps) = 1 - 2 eps exakt in IEEE)."""
    eps = np.asarray(eps, dtype=float)
    om = np.sqrt(OM2_MIN + eps)
    a = 2.0 * np.sqrt(BETA * eps)
    Aa = 2.0 * (0.25 / BETA - eps)
    b = np.sqrt(2.0 * Aa)
    xw = np.arccosh(1.0 / a) / b
    return om, a, Aa, b, xw


def x_w_formel(eps):
    """Wandlage der Formel (PLAN.md Abschnitt 3): S(x_w) = S_c/2, cosh(b x_w) = (1 - 8 beta eps)/(2 sqrt(beta eps))."""
    om, a, Aa, b, xs = par(eps)
    return float(np.arccosh((1.0 - 8.0 * BETA * eps) / a) / b)


def S_profil(x, a, Aa, b):
    t = np.exp(-b * np.abs(x))
    return Aa * t / (t + 0.5 * a * (1.0 + t * t))


def S_skalar(x, a, Aa, b):
    t = math.exp(-b * abs(x))
    return Aa * t / (t + 0.5 * a * (1.0 + t * t))


# ----------------------------------------------------------------------------------------------------------------------
# RK4 und W-Abbildung
# ----------------------------------------------------------------------------------------------------------------------

def _rhs(y, p11, c, p22):
    k = np.empty_like(y)
    k[0] = y[2]
    k[1] = y[3]
    k[2] = p11 * y[0] + c * y[1]
    k[3] = c * y[0] + p22 * y[1]
    return k


def rk4_nach_innen(koeff_k, y, j_start, j_ende, h, Ni=None):
    """y' = (y2, y3, P (y0, y1)) von x = j_start h nach x = j_ende h (j_ende < j_start), Schritt -h auf x_j = j h.
    koeff_k(k) -> (p11, c, p22) bei x = k h/2 (Halbschritt-Index). Ni: Element i startet erst bei j = Ni[i] (vorher
    bleibt y auf dem Startwert). Rueckgabe y, logn mit y_wahr = y * exp(logn)."""
    n = y.shape[1]
    logn = np.zeros(n)
    hs = -h
    k_hi = koeff_k(2 * j_start)
    nmin = None if Ni is None else int(Ni.min())
    for j in range(j_start, j_ende, -1):
        k_m = koeff_k(2 * j - 1)
        k_lo = koeff_k(2 * j - 2)
        k1 = _rhs(y, *k_hi)
        k2 = _rhs(y + (0.5 * hs) * k1, *k_m)
        k3 = _rhs(y + (0.5 * hs) * k2, *k_m)
        k4 = _rhs(y + hs * k3, *k_lo)
        dy = (hs / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        if Ni is not None and j > nmin:
            dy *= (Ni >= j)
        y += dy
        k_hi = k_lo
        if j % 128 == 0:
            m = np.abs(y).max(axis=0)
            y /= m
            logn += np.log(m)
    return y, logn


def W_physik(rho, eps, h, D):
    """W-Abbildung des 1D-Q-Balls. rho: Array (n); eps: Skalar (alle gleich) oder Array (n).
    Rueckgabe Y (4, n) = (A, B, A', B') bei x = 0, normiert mit exp(-q (X_i - x_w,i))."""
    rho = np.atleast_1d(np.asarray(rho, dtype=float))
    n = rho.size
    skalar = np.ndim(eps) == 0
    om, a, Aa, b, xw = par(eps)
    dm2 = (rho - om) ** 2
    dp2 = (rho + om) ** 2
    if np.any(dm2 >= 1.0) or np.any(dp2 <= 1.0):
        raise ValueError("rho ausserhalb des Fensters (1 - omega, 1 + omega)")
    q = np.sqrt(1.0 - dm2)
    if skalar:
        N = int(math.ceil((float(xw) + D) / h))
        Ni = None
        Xi = N * h
        a_, Aa_, b_ = float(a), float(Aa), float(b)

        def koeff_k(k):
            S = S_skalar(k * 0.5 * h, a_, Aa_, b_)
            W = 1.0 - 4.0 * S + C9 * S * S
            c = -2.0 * S + C6 * S * S
            return W - dm2, c, W - dp2
    else:
        Ni = np.ceil((xw + D) / h).astype(np.int64)
        N = int(Ni.max())
        Xi = Ni * h
        if n * (2 * N + 1) <= 3e7:
            # Koeffizienten vorab auf dem Halbschrittgitter (gleiche Stuetzstellen k h/2 wie im Skalarzweig)
            xg = np.arange(2 * N + 1) * 0.5 * h
            Sg = S_profil(xg[:, None], a[None, :], Aa[None, :], b[None, :])
            Wg = 1.0 - 4.0 * Sg + C9 * Sg * Sg
            Cg = -2.0 * Sg + C6 * Sg * Sg
            P11g = Wg - dm2[None, :]
            P22g = Wg - dp2[None, :]
            del Sg, Wg

            def koeff_k(k):
                return P11g[k], Cg[k], P22g[k]
        else:
            def koeff_k(k):
                S = S_profil(k * 0.5 * h, a, Aa, b)
                W = 1.0 - 4.0 * S + C9 * S * S
                c = -2.0 * S + C6 * S * S
                return W - dm2, c, W - dp2
    y = np.zeros((4, n))
    y[0] = 1.0
    y[2] = -q
    y, logn = rk4_nach_innen(koeff_k, y, N, 0, h, Ni)
    return y * np.exp(logn - q * (Xi - xw))


def W_synthetisch(rho, eps, h, D):
    """Selbsttest (keine Physik). l = ln(1/eps). Ast r(l) = 1,52 + 0,02 e^(-0,3 l) sin(1,36 l).
    gerade: F1 = e^(l/2) (rho - r), F2 = cos(1,36 l + 0,4) + 3 (rho - r)
    ungerade: F1 = -e^(l/2) (rho - r - 0,001), F2 = sin(1,36 l + 0,4) + 3 (rho - r)."""
    rho = np.atleast_1d(np.asarray(rho, dtype=float))
    ell = -np.log(np.asarray(eps, dtype=float)) * np.ones_like(rho)
    r = 1.52 + 0.02 * np.exp(-0.3 * ell) * np.sin(1.36 * ell)
    g = np.exp(0.5 * ell)
    Y = np.empty((4, rho.size))
    Y[2] = g * (rho - r)
    Y[3] = np.cos(1.36 * ell + 0.4) + 3.0 * (rho - r)
    Y[0] = -g * (rho - r - 0.001)
    Y[1] = np.sin(1.36 * ell + 0.4) + 3.0 * (rho - r)
    return Y


def F_wahl(Y, pidx):
    """pidx: 0 = gerade, 1 = ungerade (Skalar oder Array). Rueckgabe F1, F2."""
    pidx = np.asarray(pidx)
    F1 = np.where(pidx == 0, Y[2], Y[0])
    F2 = np.where(pidx == 0, Y[3], Y[1])
    return F1, F2


# ----------------------------------------------------------------------------------------------------------------------
# Illinois (vektorisiert)
# ----------------------------------------------------------------------------------------------------------------------

def illinois(f, a, b, fa, fb, tol, iters):
    """f(idx, x) -> Werte der Elemente idx an x. Klammern [a, b] mit fa fb < 0 (fa = 0 oder fb = 0 erlaubt).
    Rueckgabe x, Klammerbreite, Iterationen, konvergiert (Klammer < tol, f = 0 oder Schritt auf Rundungsniveau)."""
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    fa = np.array(fa, dtype=float)
    fb = np.array(fb, dtype=float)
    n = a.size
    seite = np.zeros(n, dtype=int)
    x = np.where(np.abs(fa) <= np.abs(fb), a, b)
    fertig = (fa == 0.0) | (fb == 0.0)
    x = np.where(fa == 0.0, a, np.where(fb == 0.0, b, x))
    konv = fertig.copy()
    its = np.zeros(n, dtype=int)
    x_alt = np.full(n, np.nan)
    for _ in range(iters):
        akt = (~fertig) & (np.abs(b - a) > tol)
        konv |= (~fertig) & ~akt
        fertig |= ~akt
        if not akt.any():
            break
        idx = np.nonzero(akt)[0]
        aa, bb, ffa, ffb = a[idx], b[idx], fa[idx], fb[idx]
        with np.errstate(invalid="ignore", divide="ignore"):
            c = (aa * ffb - bb * ffa) / (ffb - ffa)
        lo, hi = np.minimum(aa, bb), np.maximum(aa, bb)
        c = np.where((c > lo) & (c < hi), c, 0.5 * (aa + bb))
        fc = np.asarray(f(idx, c), dtype=float)
        its[idx] += 1
        x[idx] = c
        null = fc == 0.0
        wie_b = (fc * ffb > 0.0) & ~null
        wie_a = (fc * ffa > 0.0) & ~null
        # c auf der Seite von b
        ib = idx[wie_b]
        b[ib] = c[wie_b]
        fb[ib] = fc[wie_b]
        fa[ib] = np.where(seite[ib] == -1, 0.5 * fa[ib], fa[ib])
        seite[ib] = -1
        ia = idx[wie_a]
        a[ia] = c[wie_a]
        fa[ia] = fc[wie_a]
        fb[ia] = np.where(seite[ia] == 1, 0.5 * fb[ia], fb[ia])
        seite[ia] = 1
        i0 = idx[null]
        fertig[i0] = True
        konv[i0] = True
        stau = np.abs(c - x_alt[idx]) <= 4e-16 * np.maximum(1.0, np.abs(c))
        istau = idx[stau]
        fertig[istau] = True
        konv[istau] = True
        x_alt[idx] = c
    konv |= np.abs(b - a) <= tol
    return x, np.abs(b - a), its, konv


# ----------------------------------------------------------------------------------------------------------------------
# Scan: Nullstellen von F1 in rho je eps und Paritaet
# ----------------------------------------------------------------------------------------------------------------------

def scan(Wf, js, h, D, n_rho, voll, tol=1e-13):
    klammern = []
    anzahl = []
    for j in js:
        eps = eps_j(j)
        om = math.sqrt(OM2_MIN + eps)
        lo, hi = (1.0 - om + 0.002, 1.0 + om - 0.002) if voll else LEITER_FENSTER
        rhos = np.linspace(lo, hi, n_rho)
        Y = Wf(rhos, eps, h, D)
        for p, parit in enumerate(PARIT):
            F1 = Y[2] if p == 0 else Y[0]
            sg = np.where(F1 >= 0.0, 1, -1)
            idx = np.nonzero(sg[:-1] != sg[1:])[0]
            for i in idx:
                klammern.append((j, eps, p, rhos[i], rhos[i + 1], F1[i], F1[i + 1]))
            anzahl.append({"j": j, "par": parit, "n": int(idx.size)})
    wurzeln = []
    if klammern:
        K = np.array([k[1:] for k in klammern], dtype=float)
        jj = np.array([k[0] for k in klammern], dtype=int)
        eps_a, pidx = K[:, 0], K[:, 1].astype(int)

        def f(idx, x):
            return F_wahl(Wf(x, eps_a[idx], h, D), pidx[idx])[0]
        x, breite, its, konv = illinois(f, K[:, 2], K[:, 3], K[:, 4], K[:, 5], tol, 80)
        Y = Wf(x, eps_a, h, D)
        F1, F2 = F_wahl(Y, pidx)
        for i in range(x.size):
            wurzeln.append({"j": int(jj[i]), "eps": eps_a[i], "ell": -math.log(eps_a[i]), "par": PARIT[pidx[i]],
                            "rho": x[i], "F2": F2[i], "F1_rest": F1[i], "Ynorm": float(np.abs(Y[:, i]).max()),
                            "klammer": breite[i], "it": int(its[i]), "konv": bool(konv[i])})
    return wurzeln, anzahl


# ----------------------------------------------------------------------------------------------------------------------
# Aeste und Kandidaten
# ----------------------------------------------------------------------------------------------------------------------

def aeste(wurzeln, parit, schritt=1, link=LINK, fenster=None):
    """Verknuepft Wurzeln (eine Paritaet, im Fenster) benachbarter Rasterpunkte (j, j + schritt) als gegenseitig
    naechste Nachbarn mit |d rho| < link. Rueckgabe: Liste der Aeste (Listen von Wurzeln, j aufsteigend).
    fenster = None: das Leiterfenster der Konfiguration zur Laufzeit (in leiter_1d.py fest (1,30; 1,70))."""
    fenster = LEITER_FENSTER if fenster is None else fenster
    w = [x for x in wurzeln if x["par"] == parit and fenster[0] <= x["rho"] <= fenster[1]]
    nach_j = {}
    for x in w:
        nach_j.setdefault(x["j"], []).append(x)
    js = sorted(nach_j)
    for j in js:
        nach_j[j].sort(key=lambda x: x["rho"])
    ast_von = {}
    alle = []
    for j in js:
        for x in nach_j[j]:
            if id(x) not in ast_von:
                ast_von[id(x)] = len(alle)
                alle.append([x])
        jn = j + schritt
        if jn not in nach_j:
            continue
        A, B = nach_j[j], nach_j[jn]
        for x in A:
            bn = min(B, key=lambda y: abs(y["rho"] - x["rho"]))
            an = min(A, key=lambda y: abs(y["rho"] - bn["rho"]))
            if an is x and abs(bn["rho"] - x["rho"]) < link and id(bn) not in ast_von:
                ast_von[id(bn)] = ast_von[id(x)]
                alle[ast_von[id(x)]].append(bn)
    return alle


def kandidaten(ast_liste, parit):
    k = []
    for ia, ast in enumerate(ast_liste):
        for x, y in zip(ast[:-1], ast[1:]):
            sx = 1 if x["F2"] >= 0.0 else -1
            sy = 1 if y["F2"] >= 0.0 else -1
            if sx != sy:
                ell_lin = x["ell"] + (y["ell"] - x["ell"]) * x["F2"] / (x["F2"] - y["F2"])
                rho_lin = x["rho"] + (y["rho"] - x["rho"]) * (ell_lin - x["ell"]) / (y["ell"] - x["ell"])
                k.append({"par": parit, "ast": ia, "j_a": x["j"], "j_b": y["j"], "ell_a": x["ell"], "ell_b": y["ell"],
                          "rho_a": x["rho"], "rho_b": y["rho"], "s_a": x["F2"], "s_b": y["F2"], "ell_lin": ell_lin,
                          "rho_lin": rho_lin})
    return k


def lade_wurzeln(pfade):
    wurzeln, anzahl, meta = [], [], []
    gesehen = set()
    for p in pfade:
        with open(p) as fh:
            d = json.load(fh)
        meta.append({k: d[k] for k in ("h", "D", "n_rho", "voll", "j_liste", "sek") if k in d})
        for w in d["wurzeln"]:
            key = (w["j"], w["par"], round(w["rho"], 9))
            if key in gesehen:
                continue
            gesehen.add(key)
            wurzeln.append(w)
        anzahl += d["anzahl"]
    return wurzeln, anzahl, meta


# ----------------------------------------------------------------------------------------------------------------------
# Verfeinerung der Sprossen (geschachteltes Illinois)
# ----------------------------------------------------------------------------------------------------------------------

def rho_wurzel_lokal(Wf, eps, pidx, rho_mitte, w, h, D, n=41, tol=1e-13):
    """Je Element: Abtastung rho_mitte +- w (n Punkte), Vorzeichenwechsel von F1 am naechsten zur Mitte, Illinois.
    Rueckgabe rho, F2, F1-Rest, ok."""
    m = rho_mitte.size
    rho_w = np.full(m, np.nan)
    ok = np.zeros(m, dtype=bool)
    offen = np.arange(m)
    ww = w.copy()
    kl = np.zeros((m, 4))
    for versuch in range(2):
        if offen.size == 0:
            break
        u = np.linspace(-1.0, 1.0, n)
        R = rho_mitte[offen, None] + ww[offen, None] * u[None, :]
        om = np.sqrt(OM2_MIN + eps[offen])[:, None]
        R = np.clip(R, 1.0 - om + 1e-9, 1.0 + om - 1e-9)
        E = np.repeat(eps[offen], n)
        P = np.repeat(pidx[offen], n)
        F1 = F_wahl(Wf(R.ravel(), E, h, D), P)[0].reshape(offen.size, n)
        noch = []
        for t, i in enumerate(offen):
            sg = np.where(F1[t] >= 0.0, 1, -1)
            wi = np.nonzero(sg[:-1] != sg[1:])[0]
            if wi.size == 0:
                noch.append(i)
                continue
            k = wi[np.argmin(np.abs(wi + 0.5 - (n - 1) / 2.0))]
            kl[i] = (R[t, k], R[t, k + 1], F1[t, k], F1[t, k + 1])
            ok[i] = True
        offen = np.array(noch, dtype=int)
        ww[offen] *= 4.0
    idx_ok = np.nonzero(ok)[0]
    F2 = np.full(m, np.nan)
    F1r = np.full(m, np.nan)
    if idx_ok.size:
        def f(idx, x):
            ii = idx_ok[idx]
            return F_wahl(Wf(x, eps[ii], h, D), pidx[ii])[0]
        x, br, its, konv = illinois(f, kl[idx_ok, 0], kl[idx_ok, 1], kl[idx_ok, 2], kl[idx_ok, 3], tol, 80)
        rho_w[idx_ok] = x
        Y = Wf(x, eps[idx_ok], h, D)
        a1, a2 = F_wahl(Y, pidx[idx_ok])
        F2[idx_ok] = a2
        F1r[idx_ok] = a1
        ok[idx_ok] &= konv
    return rho_w, F2, F1r, ok


def verfeinere(Wf, kand, h, D, tol_ell=1e-10, iters=40):
    """Geschachteltes Illinois: aussen l (Vorzeichenwechsel von F2 entlang des Asts), innen rho (F1 = 0)."""
    if not kand:
        return []
    nc = len(kand)
    la = np.array([k["ell_a"] for k in kand])
    lb = np.array([k["ell_b"] for k in kand])
    ra = np.array([k["rho_a"] for k in kand])
    rb = np.array([k["rho_b"] for k in kand])
    pidx = np.array([PARIT.index(k["par"]) for k in kand])
    w0 = np.maximum(4.0 * np.abs(rb - ra), 2e-3)
    letzt = {"rho": np.full(nc, np.nan), "F1": np.full(nc, np.nan), "ok": np.ones(nc, dtype=bool)}

    def s_fun(idx, ell):
        rho_lin = ra[idx] + (rb[idx] - ra[idx]) * (ell - la[idx]) / (lb[idx] - la[idx])
        r, F2, F1r, ok = rho_wurzel_lokal(Wf, np.exp(-ell), pidx[idx], rho_lin, w0[idx], h, D)
        letzt["rho"][idx] = r
        letzt["F1"][idx] = F1r
        letzt["ok"][idx] &= ok
        return np.where(ok, F2, np.nan)

    alle = np.arange(nc)
    sa = s_fun(alle, la.copy())
    sb = s_fun(alle, lb.copy())
    vz_ok = np.isfinite(sa) & np.isfinite(sb) & (sa * sb <= 0.0)
    erg = [dict(k) for k in kand]
    for i in range(nc):
        erg[i].update({"s_a_neu": sa[i], "s_b_neu": sb[i], "vorzeichen_ok": bool(vz_ok[i]), "h": h, "D": D})
    idx = np.nonzero(vz_ok)[0]
    if idx.size:
        def f(ii, ell):
            return s_fun(idx[ii], ell)
        x, br, its, konv = illinois(f, la[idx], lb[idx], sa[idx], sb[idx], tol_ell, iters)
        s_end = s_fun(idx, x)
        for t, i in enumerate(idx):
            eps = math.exp(-x[t])
            erg[i].update({"ell": x[t], "eps": eps, "omega2": OM2_MIN + eps, "rho": letzt["rho"][i], "F1_rest": letzt["F1"][i],
                           "F2_rest": s_end[t], "klammer_ell": br[t], "it": int(its[t]),
                           "konv": bool(konv[t] and letzt["ok"][i]), "inner_ok": bool(letzt["ok"][i])})
    for e in erg:
        e.setdefault("konv", False)
    return erg


# ----------------------------------------------------------------------------------------------------------------------
# Umlauf im Rechteck (rho, l), gegen den Uhrzeigersinn (rho waagrecht, l = ln(1/eps) senkrecht)
# ----------------------------------------------------------------------------------------------------------------------

def _punkte(r, t):
    k = np.floor(t).astype(int)
    f = t - k
    r0, r1 = r["rho_c"] - r["drho"], r["rho_c"] + r["drho"]
    l0, l1 = r["ell_c"] - r["dell"], r["ell_c"] + r["dell"]
    rho = np.select([k == 0, k == 1, k == 2], [r0 + f * (r1 - r0), np.full_like(f, r1), r1 - f * (r1 - r0)], r0)
    ell = np.select([k == 0, k == 1, k == 2], [np.full_like(f, l0), l0 + f * (l1 - l0), np.full_like(f, l1)],
                    l1 - f * (l1 - l0))
    return rho, ell


def umlaeufe(Wf, rects, h, D, n0=60, runden=30, sprung=0.4):
    if not rects:
        return []
    ts = [np.linspace(0.0, 4.0, 4 * n0, endpoint=False) for _ in rects]
    Fs = [None] * len(rects)

    def auswerten(liste):
        R, L, P, wo = [], [], [], []
        for i, t in liste:
            rho, ell = _punkte(rects[i], t)
            R.append(rho)
            L.append(ell)
            P.append(np.full(t.size, PARIT.index(rects[i]["par"])))
            wo.append((i, t.size))
        R, L, P = np.concatenate(R), np.concatenate(L), np.concatenate(P)
        F1, F2 = F_wahl(Wf(R, np.exp(-L), h, D), P)
        Z = F1 + 1j * F2
        aus, s = [], 0
        for i, m in wo:
            aus.append((i, Z[s:s + m]))
            s += m
        return aus

    for i, Z in auswerten([(i, ts[i]) for i in range(len(rects))]):
        Fs[i] = Z
    runde_n = [0] * len(rects)
    for runde in range(runden + 1):
        neu = []
        for i in range(len(rects)):
            Z = Fs[i]
            d = np.angle(np.roll(Z, -1) * np.conj(Z))
            gross = np.nonzero(np.abs(d) >= sprung)[0]
            if gross.size and runde < runden:
                t = ts[i]
                tn = np.roll(t, -1)
                tn = np.where(tn <= t, tn + 4.0, tn)
                mid = 0.5 * (t[gross] + tn[gross]) % 4.0
                neu.append((i, mid))
                runde_n[i] = runde + 1
        if not neu:
            break
        for i, Z in auswerten(neu):
            t = np.concatenate([ts[i], neu_t(neu, i)])
            Zn = np.concatenate([Fs[i], Z])
            o = np.argsort(t, kind="stable")
            ts[i], Fs[i] = t[o], Zn[o]
    erg = []
    for i, r in enumerate(rects):
        Z = Fs[i]
        d = np.angle(np.roll(Z, -1) * np.conj(Z))
        summe = float(d.sum() / (2.0 * math.pi))
        U = int(round(summe))
        erg.append({**r, "h": h, "D": D, "U": U, "summe_2pi": summe, "groesster_sprung": float(np.abs(d).max()),
                    "punkte": int(Z.size), "runden": runde_n[i],
                    "aufgeloest": bool(np.abs(d).max() < sprung and abs(summe - U) < 0.1),
                    "min_betrag": float(np.abs(Z).min())})
    return erg


def neu_t(neu, i):
    for k, t in neu:
        if k == i:
            return t
    return np.zeros(0)


# ----------------------------------------------------------------------------------------------------------------------
# Gegenprobe DOP853 (scipy, adaptiv) und Newton in (rho, l)
# ----------------------------------------------------------------------------------------------------------------------

def W_dop(rho, eps, D=40.0, rtol=1e-12):
    from scipy.integrate import solve_ivp
    om, a, Aa, b, xw = [float(v) for v in par(eps)]
    dm2, dp2 = (rho - om) ** 2, (rho + om) ** 2
    q = math.sqrt(1.0 - dm2)
    X = xw + D

    def f(x, z):
        S = S_skalar(x, a, Aa, b)
        W = 1.0 - 4.0 * S + C9 * S * S
        c = -2.0 * S + C6 * S * S
        return [z[2], z[3], (W - dm2) * z[0] + c * z[1], c * z[0] + (W - dp2) * z[1]]
    sol = solve_ivp(f, (X, 0.0), [1.0, 0.0, -q, 0.0], method="DOP853", rtol=rtol, atol=1e-30)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.y[:, -1] * math.exp(-q * (X - xw)), sol.nfev


def newton_dop(rho0, ell0, p, D=40.0, rtol=1e-12, iters=10):
    def F(r, l):
        Y, nf = W_dop(r, math.exp(-l), D, rtol)
        return (np.array([Y[2], Y[3]]) if p == 0 else np.array([Y[0], Y[1]])), nf
    r, l = rho0, ell0
    nfev = 0
    verlauf = []
    for it in range(iters):
        F0, n0 = F(r, l)
        Fr, n1 = F(r + 1e-7, l)
        Fl, n2 = F(r, l + 1e-6)
        nfev += n0 + n1 + n2
        J = np.column_stack([(Fr - F0) / 1e-7, (Fl - F0) / 1e-6])
        d = np.linalg.solve(J, -F0)
        r, l = r + d[0], l + d[1]
        verlauf.append([float(d[0]), float(d[1])])
        if abs(d[0]) < 1e-12 and abs(d[1]) < 1e-10:
            break
    Fe, ne = F(r, l)
    return {"rho": r, "ell": l, "F_rest": Fe.tolist(), "it": it + 1, "schritte": verlauf, "nfev": nfev + ne,
            "konv": bool(abs(verlauf[-1][0]) < 1e-10 and abs(verlauf[-1][1]) < 1e-8)}


# ----------------------------------------------------------------------------------------------------------------------
# Kommandos
# ----------------------------------------------------------------------------------------------------------------------

def cmd_scan(args, Wf=W_physik):
    js = list(range(args.j_von, args.j_bis + 1, args.j_schritt))
    log(f"scan: h = {args.h}, D = {args.D}, n_rho = {args.n_rho}, voll = {args.voll}, j {js[0]} .. {js[-1]} "
        f"({len(js)} Werte)")
    w, anzahl = scan(Wf, js, args.h, args.D, args.n_rho, args.voll)
    out = {"kommando": "scan", "beginn": BEGINN, "ende": jetzt(), "sek": sek(), "h": args.h, "D": args.D,
           "n_rho": args.n_rho, "voll": args.voll, "j_liste": js, "eps_liste": [eps_j(j) for j in js],
           "fenster": None if args.voll else LEITER_FENSTER, "wurzeln": w, "anzahl": anzahl,
           "nicht_konvergiert": sum(1 for x in w if not x["konv"])}
    schreibe(args.out, out)
    log(f"scan fertig: {len(w)} Wurzeln, nicht konvergiert {out['nicht_konvergiert']}")
    return out


def rechtecke_aus(kand_fein, eigene, drho, dell):
    """Rechteckmitte: Kandidat der feinen Stufe (lineare Lage aus dem Scan) mit gleicher Paritaet und |dl| < 0,3;
    sonst die eigene lineare Lage (Vermerk)."""
    rects = []
    for e in eigene:
        if not e.get("konv"):
            rects.append(None)
            continue
        best = None
        for k in kand_fein:
            if k["par"] == e["par"] and abs(k["ell_lin"] - e["ell"]) < 0.3:
                if best is None or abs(k["ell_lin"] - e["ell"]) < abs(best["ell_lin"] - e["ell"]):
                    best = k
        if best is not None:
            rects.append({"par": e["par"], "rho_c": round(best["rho_lin"], 6), "ell_c": round(best["ell_lin"], 4),
                          "drho": drho, "dell": dell, "mitte": "fein_scan"})
        else:
            rects.append({"par": e["par"], "rho_c": round(e["rho_lin"], 6), "ell_c": round(e["ell_lin"], 4),
                          "drho": drho, "dell": dell, "mitte": "eigen"})
    return rects


def cmd_sprossen(args, Wf=W_physik):
    w_eigen, anz, meta = lade_wurzeln(args.scan.split(","))
    w_fein, _, _ = lade_wurzeln(args.scan_fein.split(","))
    out = {"kommando": "sprossen", "beginn": BEGINN, "h": args.h, "D": args.D, "scan_meta": meta,
           "drho": args.drho, "dell": args.dell}
    kand, kand_fein, ast_info = [], [], {}
    for parit in PARIT:
        al = aeste(w_eigen, parit)
        k = kandidaten(al, parit)
        kand += k
        kand_fein += kandidaten(aeste(w_fein, parit), parit)
        ast_info[parit] = [{"ast": i, "j_von": a[0]["j"], "j_bis": a[-1]["j"], "n": len(a),
                            "rho_min": min(x["rho"] for x in a), "rho_max": max(x["rho"] for x in a),
                            "wechsel": sum(1 for x in k if x["ast"] == i)} for i, a in enumerate(al)]
    out["aeste"] = ast_info
    out["kandidaten"] = kand
    log(f"sprossen h = {args.h}: {len(kand)} Kandidaten: " +
        ", ".join(f"{k['par'][0]} j{k['j_a']}-{k['j_b']} l~{k['ell_lin']:.3f} rho~{k['rho_lin']:.5f}" for k in kand))
    erg = verfeinere(Wf, kand, args.h, args.D)
    out["sprossen"] = erg
    schreibe(args.out, out)
    log("Verfeinerung: " + ", ".join(f"{e['par'][0]} l = {e.get('ell', float('nan')):.8f} rho = "
                                     f"{e.get('rho', float('nan')):.9f} konv {e['konv']}" for e in erg))
    rects = rechtecke_aus(kand_fein, erg, args.drho, args.dell)
    gueltig = [r for r in rects if r is not None]
    um = umlaeufe(Wf, gueltig, args.h, args.D)
    t = 0
    for i, r in enumerate(rects):
        if r is not None:
            erg[i]["umlauf"] = um[t]
            t += 1
    out["sprossen"] = erg
    schreibe(args.out, out)
    log("Umlaeufe: " + ", ".join(f"{e['par'][0]} U = {e['umlauf']['U']} (Summe {e['umlauf']['summe_2pi']:.4f}, "
                                 f"Sprung {e['umlauf']['groesster_sprung']:.3f}, Punkte {e['umlauf']['punkte']})"
                                 for e in erg if "umlauf" in e))
    out["ende"] = jetzt()
    out["sek"] = sek()
    schreibe(args.out, out)
    log("sprossen fertig")
    return out


def cmd_dop853(args):
    """Gegenprobe: je konvergierte Sprosse einer sprossen-Ausgabe Newton in (rho, l) mit scipy DOP853 (adaptiv),
    Gebiet D = 40, Start an der RK4-Lage."""
    with open(args.sprossen) as fh:
        d = json.load(fh)
    out = {"kommando": "dop853", "beginn": BEGINN, "quelle": args.sprossen, "D": args.D, "rtol": args.rtol,
           "ergebnisse": []}
    for e in d["sprossen"]:
        if not e.get("konv"):
            continue
        try:
            r = newton_dop(e["rho"], e["ell"], PARIT.index(e["par"]), args.D, args.rtol)
            r.update({"par": e["par"], "ell_rk4": e["ell"], "rho_rk4": e["rho"], "d_ell": r["ell"] - e["ell"],
                      "d_rho": r["rho"] - e["rho"]})
        except Exception as ex:   # noqa: BLE001
            r = {"par": e["par"], "ell_rk4": e["ell"], "fehler": repr(ex)}
        out["ergebnisse"].append(r)
        schreibe(args.out, out)
        log(f"DOP853 {e['par']}: l = {r.get('ell', float('nan')):.10f} (d {r.get('d_ell', float('nan')):.2e}), rho = "
            f"{r.get('rho', float('nan')):.10f} (d {r.get('d_rho', float('nan')):.2e}), konv {r.get('konv')}")
    out["ende"] = jetzt()
    out["sek"] = sek()
    schreibe(args.out, out)


def ebene_wand_cin(rhos, h):
    """c_in der ebenen Wand (omega = omega_min, S = S_c/(1 + e^(x/sqrt(beta)))) wie wand_beta.c_in, aber mit
    diesem RK4 auf x_j = j h von x_b = 43 sqrt(beta) nach x_a = -36 sqrt(beta). Nur Vorzeichen/Nullstelle zaehlen.
    beta = 1/2: bitgleich zu leiter_1d.py (rate = sqrt(1/beta) = sqrt(2), S_c = 1, W_in = 1,5, C_in = 1)."""
    rhos = np.atleast_1d(np.asarray(rhos, dtype=float))
    om = math.sqrt(OM2_MIN)
    s2 = math.sqrt(1.0 / BETA)
    w_in, c_in_ = 1.0 + 1.0 / (4.0 * BETA), 1.0 / (2.0 * BETA)
    dm2, dp2 = (rhos - om) ** 2, (rhos + om) ** 2
    q = np.sqrt(1.0 - dm2)

    def koeff_k(k):
        x = k * 0.5 * h
        t = math.exp(-s2 * abs(x))
        S = SC * t / (1.0 + t) if x > 0 else SC / (1.0 + t)
        W = 1.0 - 4.0 * S + C9 * S * S
        c = -2.0 * S + C6 * S * S
        return W - dm2, c, W - dp2
    jb = int(math.ceil(43.0 / s2 / h))
    ja = int(math.floor(-36.0 / s2 / h))
    y = np.zeros((4, rhos.size))
    y[0] = 1.0
    y[2] = -q
    y, logn = rk4_nach_innen(koeff_k, y, jb, ja, h)
    xa, xb = ja * h, jb * h
    cin = np.empty(rhos.size)
    kin = np.empty(rhos.size)
    kap = np.empty(rhos.size)
    for i, r in enumerate(rhos):
        P = np.array([[w_in - (r - om) ** 2, c_in_], [c_in_, w_in - (r + om) ** 2]])
        lam, vec = np.linalg.eigh(P)
        e2 = vec[:, 1] * (1.0 if vec[0, 1] > 0 else -1.0)
        kk = math.sqrt(lam[1])
        ye, ye1 = e2 @ y[:2, i], e2 @ y[2:, i]
        cin[i] = (kk * ye - ye1) / (2.0 * kk) * math.exp(logn[i] + kk * xa - q[i] * xb)
        kin[i], kap[i] = math.sqrt(-lam[0]), kk
    return cin, kin, kap


def cmd_k0(args):
    out = {"kommando": "k0", "beginn": BEGINN, "h_liste": args.h_liste}
    from scipy.integrate import quad
    # (1) Profil: erste Integralform, Bewegungsgleichung, Quadratur x(S)
    prof = []
    for eps in KONFIG.get("k0_eps", (1e-7, 1e-5, 1e-3, 0.05, 0.2)):
        om, a, Aa, b, xw = [float(v) for v in par(eps)]
        x = np.linspace(0.0, xw + 30.0, 4001)
        ch, sh = np.cosh(b * x), np.sinh(b * x)
        Dn = 1.0 + a * ch
        S = Aa / Dn
        S1 = -Aa * a * b * sh / Dn ** 2
        S2 = -Aa * a * b * b * ch / Dn ** 2 + 2.0 * Aa * a * a * b * b * sh * sh / Dn ** 3
        # erste Integralform: S'^2/(4 S^2) = 1 - omega^2 - S + beta S^2 = beta (S_c - S)^2 - eps
        g = BETA * (SC - S - a / (2.0 * BETA)) * (SC - S + a / (2.0 * BETA))
        r1 = np.abs(S1 * S1 / (4.0 * S * S) - g).max()
        Up = 1.0 - 2.0 * S + C3 * S * S
        r2 = np.abs(S2 / (2.0 * S) - S1 * S1 / (4.0 * S * S) - (Up - om * om)).max()
        S0 = (1.0 - a) / (2.0 * BETA)
        dx = []
        for fak in (0.999, 0.9, 0.5, 0.1, 1e-3, 1e-6):
            Sv = fak * S0
            xq, fehler = quad(lambda u: 1.0 / ((S0 - u * u) * math.sqrt(a + BETA * u * u)), 0.0, math.sqrt(S0 - Sv),
                              epsabs=1e-14, epsrel=1e-13, limit=200)
            xa_ = math.acosh((Aa / Sv - 1.0) / a) / b
            dx.append(abs(xq - xa_))
        wurzeln = sorted(np.roots([BETA, -1.0, 1.0 - om * om]).real.tolist())
        xwf = x_w_formel(eps) if (1.0 - 8.0 * BETA * eps) / a >= 1.0 else float("nan")
        prof.append({"eps": eps, "S0": S0, "S0_kleinere_wurzel": wurzeln[0], "S0_groessere_wurzel": wurzeln[1],
                     "x_w": xw, "S_bei_x_w": Aa / 2.0, "x_w_formel": xwf,
                     "S_bei_x_w_formel": float(S_skalar(xwf, a, Aa, b)) if math.isfinite(xwf) else None,
                     "rest_erste_integralform": r1, "rest_bewegungsgleichung": r2, "quadratur_max_dx": max(dx),
                     "S_am_rand_D30": float(S_skalar(xw + 30.0, a, Aa, b))})
        log(f"Profil eps = {eps:g}: S0 = {S0:.10f}, x_w = {xw:.4f}, x_w(Formel) = {xwf:.4f}, Reste {r1:.2e} / "
            f"{r2:.2e}, Quadratur {max(dx):.2e}")
    out["profil"] = prof
    # (2) ebene Wand: rho_z mit diesem RK4
    wand = []
    for h in args.h_liste:
        rr = np.linspace(*KONFIG.get("k0_rho_bereich", (1.50, 1.55)), 26)
        cin, _, _ = ebene_wand_cin(rr, h)
        sg = np.where(cin >= 0, 1, -1)
        i = int(np.nonzero(sg[:-1] != sg[1:])[0][0])

        def f(idx, x):
            return ebene_wand_cin(x, h)[0]
        x, br, its, konv = illinois(f, [rr[i]], [rr[i + 1]], [cin[i]], [cin[i + 1]], 1e-14, 80)
        _, kin, kap = ebene_wand_cin(x, h)
        wand.append({"h": h, "rho_z": x[0], "abw_zu_R24": x[0] - RHO_Z, "k_in": kin[0], "kappa_in": kap[0],
                     "b_inf": math.sqrt(1.0 / BETA) * math.pi / kin[0], "it": int(its[0]), "konv": bool(konv[0]),
                     "wechsel_im_fenster": int((sg[:-1] != sg[1:]).sum())})
        log(f"ebene Wand h = {h}: rho_z = {x[0]:.12f} (Abw. {x[0] - RHO_Z:.2e}), k_in = {kin[0]:.6f}, "
            f"kappa_in = {kap[0]:.6f}")
    out["ebene_wand"] = wand
    schreibe(args.out, out)
    # (2b) W-Abbildung: RK4 (h, D = 30) gegen DOP853 (rtol 1e-12, D = 40), rohe Vektoren (A, B, A', B') bei x = 0
    vgl = []
    for eps in KONFIG.get("k0_eps_vgl", (1e-6, 1e-3, 0.1)):
        for rho in KONFIG.get("k0_rho_vgl", (1.40, 1.52, 1.62)):
            Yd, nf = W_dop(rho, eps, 40.0, 1e-12)
            for h in args.h_liste:
                Yr = W_physik(np.array([rho]), eps, h, 30.0)[:, 0]
                vgl.append({"eps": eps, "rho": rho, "h": h, "rel_abw": float(np.abs(Yr - Yd).max() / np.abs(Yd).max()),
                            "betrag": float(np.abs(Yd).max()), "nfev_dop": nf})
    out["rk4_gegen_dop853"] = vgl
    log("RK4 gegen DOP853: " + ", ".join(f"eps {v['eps']:g} rho {v['rho']} h {v['h']}: {v['rel_abw']:.1e}" for v in vgl))
    schreibe(args.out, out)
    # (3) G2-10-Vergleich: omega^2 = 0,55 .. 0,70 (Schritt 0,005), ganzes Fenster, beide Paritaeten (nur beta = 1/2)
    g = []
    h = args.h_g210
    for k in (range(31) if G210 else ()):
        w2 = round(0.55 + 0.005 * k, 3)
        eps = w2 - 0.5
        om = math.sqrt(w2)
        rhos = np.linspace(1.0 - om + 0.002, 1.0 + om - 0.002, args.n_g210)
        Y = W_physik(rhos, eps, h, 30.0)
        for p in (0, 1):
            F1 = Y[2] if p == 0 else Y[0]
            sg = np.where(F1 >= 0, 1, -1)
            for i in np.nonzero(sg[:-1] != sg[1:])[0]:
                g.append({"omega2": w2, "eps": eps, "p": p, "a": rhos[i], "b": rhos[i + 1], "fa": F1[i], "fb": F1[i + 1]})
    if g:
        E = np.array([x["eps"] for x in g])
        P = np.array([x["p"] for x in g])

        def f(idx, x):
            return F_wahl(W_physik(x, E[idx], h, 30.0), P[idx])[0]
        x, br, its, konv = illinois(f, [x["a"] for x in g], [x["b"] for x in g], [x["fa"] for x in g],
                                    [x["fb"] for x in g], 1e-13, 80)
        F1, F2 = F_wahl(W_physik(x, E, h, 30.0), P)
        for i, e in enumerate(g):
            e.update({"par": PARIT[e["p"]], "rho": x[i], "F2": F2[i], "F1_rest": F1[i], "konv": bool(konv[i])})
    out["g210"] = {"h": h, "n_rho": args.n_g210, "wurzeln": g, "gerechnet": G210,
                   "vergleich_gerade": [{"omega2": w2, "rho_b_G210": rb,
                                         "rho_hier": [e["rho"] for e in g if e["omega2"] == w2 and e["p"] == 0]}
                                        for w2, rb in (G210_RHO_B.items() if G210 else ())]}
    for v in out["g210"]["vergleich_gerade"]:
        log(f"G2-10 omega^2 = {v['omega2']}: rho_b(G2-10) = {v['rho_b_G210']:.6f}, hier {v['rho_hier']}")
    out["ende"] = jetzt()
    out["sek"] = sek()
    schreibe(args.out, out)
    log("k0 fertig")


def cmd_selbsttest(args):
    """Synthetische W-Abbildung durch dieselben Funktionen (scan, aeste, kandidaten, verfeinere, umlaeufe)."""
    from scipy.optimize import brentq
    js = list(range(0, J_MAX + 1))
    w, anz = scan(W_synthetisch, js, 0.0, 0.0, args.n_rho, False)
    erw = []
    for p in (0, 1):
        def r(l):
            return 1.52 + 0.02 * math.exp(-0.3 * l) * math.sin(1.36 * l) + (0.001 if p == 1 else 0.0)

        def s(l):
            return F_wahl(W_synthetisch(np.array([r(l)]), math.exp(-l), 0, 0), p)[1][0]
        ls = np.linspace(-math.log(eps_j(J_MAX)), -math.log(eps_j(0)), 4001)
        sv = [s(l) for l in ls]
        for i in range(len(ls) - 1):
            if sv[i] * sv[i + 1] < 0:
                l0 = brentq(s, ls[i], ls[i + 1], xtol=1e-14)
                # Umlaufzeichen = Vorzeichen der Jacobi-Determinante d(F1, F2)/d(rho, l)
                d = 1e-6
                Z = lambda rr, ll: np.array(F_wahl(W_synthetisch(np.array([rr]), math.exp(-ll), 0, 0), p))[:, 0]  # noqa
                J = np.column_stack([(Z(r(l0) + d, l0) - Z(r(l0) - d, l0)) / (2 * d),
                                     (Z(r(l0), l0 + d) - Z(r(l0), l0 - d)) / (2 * d)])
                erw.append({"par": PARIT[p], "ell": l0, "rho": r(l0), "U_erwartet": int(np.sign(np.linalg.det(J)))})
    kand = []
    for parit in PARIT:
        kand += kandidaten(aeste(w, parit), parit)
    erg = verfeinere(W_synthetisch, kand, 0.0, 0.0)
    rects = rechtecke_aus(kand, erg, 0.01, 0.5)
    um = umlaeufe(W_synthetisch, [r for r in rects if r is not None], 0.0, 0.0)
    t = 0
    for i, r in enumerate(rects):
        if r is not None:
            erg[i]["umlauf"] = um[t]
            t += 1
    vergleich = []
    for e in erw:
        best = min(erg, key=lambda x: abs(x.get("ell", 1e9) - e["ell"]) + (0 if x["par"] == e["par"] else 1e9))
        vergleich.append({**e, "ell_gefunden": best.get("ell"), "rho_gefunden": best.get("rho"),
                          "U_gefunden": best.get("umlauf", {}).get("U"), "d_ell": best.get("ell", 1e9) - e["ell"],
                          "d_rho": best.get("rho", 1e9) - e["rho"]})
    ok = (len(erw) == len(erg) and all(abs(v["d_ell"]) < 1e-9 and abs(v["d_rho"]) < 1e-9 and v["U_gefunden"] ==
                                       v["U_erwartet"] for v in vergleich))
    out = {"kommando": "selbsttest", "beginn": BEGINN, "ende": jetzt(), "sek": sek(), "n_wurzeln": len(w),
           "n_kandidaten": len(kand), "erwartet": len(erw), "vergleich": vergleich, "bestanden": ok}
    schreibe(args.out, out)
    for v in vergleich:
        log(f"{v['par']}: l = {v['ell']:.10f} gefunden {v['ell_gefunden']}, d_l = {v['d_ell']:.1e}, d_rho = "
            f"{v['d_rho']:.1e}, U erwartet {v['U_erwartet']} gefunden {v['U_gefunden']}")
    log(f"selbsttest bestanden: {ok} ({len(erg)} gefunden, {len(erw)} erwartet)")


# ----------------------------------------------------------------------------------------------------------------------
# Regel (mechanisch, PLAN.md Abschnitt 6)
# ----------------------------------------------------------------------------------------------------------------------

EPS_BEREICH = (1e-7, 0.05)
TOL_ELL = 1e-4
TOL_RHO = 1e-5


def cmd_regel(args):
    with open(args.k0) as fh:
        k0 = json.load(fh)
    with open(args.grob) as fh:
        sg = json.load(fh)
    with open(args.fein) as fh:
        sf = json.load(fh)
    wf, _, _ = lade_wurzeln(args.scan_fein.split(","))
    d40 = dop = None
    if args.d40:
        with open(args.d40) as fh:
            d40 = json.load(fh)
    if args.dop:
        with open(args.dop) as fh:
            dop = json.load(fh)
    aus = {"kommando": "regel", "beginn": BEGINN, "eingaben": vars(args)}
    # K0-Bedingung: Profilreste <= 1e-10, Quadratur <= 1e-9, rho_z (feinste Stufe) auf 1e-6
    prof_ok = all(p["rest_erste_integralform"] <= 1e-10 and p["rest_bewegungsgleichung"] <= 1e-10 and
                  p["quadratur_max_dx"] <= 1e-9 for p in k0["profil"])
    wand_ok = all(abs(w["abw_zu_R24"]) <= 1e-6 and w["konv"] for w in k0["ebene_wand"])
    aus["K0"] = {"profil_ok": prof_ok, "wand_ok": wand_ok, "bestanden": prof_ok and wand_ok}
    # Sprossen: Paarung fein <-> grob (gleiche Paritaet, |dl| < 0,3)
    liste = []
    for e in sf["sprossen"]:
        z = {"par": e["par"], "fein": e}
        g = [x for x in sg["sprossen"] if x["par"] == e["par"] and x.get("konv") and e.get("konv") and
             abs(x["ell"] - e["ell"]) < 0.3]
        z["grob"] = g[0] if g else None
        gruende = []
        if not e.get("konv"):
            gruende.append("fein nicht konvergiert")
        if z["grob"] is None:
            gruende.append("keine grobe Entsprechung")
        else:
            dl = abs(z["grob"]["ell"] - e["ell"])
            dr = abs(z["grob"]["rho"] - e["rho"])
            z["d_ell_stufen"], z["d_rho_stufen"] = dl, dr
            if not (dl <= TOL_ELL and dr <= TOL_RHO):
                gruende.append("Stufen weichen ab")
            uf, ug = e.get("umlauf"), z["grob"].get("umlauf")
            if not uf or not ug:
                gruende.append("Umlauf fehlt")
            else:
                if not (uf["aufgeloest"] and ug["aufgeloest"]):
                    gruende.append("Umlauf nicht aufgeloest")
                if not (abs(uf["U"]) == 1 and uf["U"] == ug["U"]):
                    gruende.append("Umlauf nicht +-1 gleich")
        z["gezaehlt"] = not gruende
        z["gruende"] = gruende
        # Kontrollen (berichtet, keine Regel): Gebiet D = 40 (gleiche Stufe), DOP853-Newton
        if e.get("konv") and d40 is not None:
            k = [x for x in d40["sprossen"] if x["par"] == e["par"] and x.get("konv") and abs(x["ell"] - e["ell"]) < 0.3]
            if k:
                z["D40"] = {"d_ell": k[0]["ell"] - e["ell"], "d_rho": k[0]["rho"] - e["rho"],
                            "U": (k[0].get("umlauf") or {}).get("U")}
        if e.get("konv") and dop is not None:
            k = [x for x in dop["ergebnisse"] if x["par"] == e["par"] and x.get("ell_rk4") == e["ell"]]
            if k:
                z["dop853"] = {x: k[0].get(x) for x in ("d_ell", "d_rho", "konv", "it", "F_rest", "fehler")}
        z["kurz"] = {"par": e["par"], "ell": e.get("ell"), "eps": e.get("eps"), "omega2": e.get("omega2"),
                     "rho": e.get("rho"), "U": (e.get("umlauf") or {}).get("U"),
                     "U_grob": ((z["grob"] or {}).get("umlauf") or {}).get("U"),
                     "rho_minus_rho_z": (e.get("rho") - RHO_Z) if e.get("rho") is not None else None}
        liste.append(z)
    aus["sprossen"] = liste
    sp = sorted([z["kurz"] for z in liste if z["gezaehlt"] and EPS_BEREICH[0] <= z["kurz"]["eps"] <= EPS_BEREICH[1]],
                key=lambda x: x["eps"])
    aus["sprossen_im_bereich"] = sp
    n = len(sp)
    aus["konfig"] = KONFIG
    aus["anzahl"] = {"n": n, "mindestens_drei": n >= 3, "eps_bereich": EPS_BEREICH}
    if n >= 3:
        schritte = [sp[i]["ell"] - sp[i + 1]["ell"] for i in range(n - 1)]
        zwei = schritte[:2]
        aus["PW2"] = {"schritte_kleinstes_eps_zuerst": schritte, "zwei": zwei, "bezug": B_INF, "band": BAND,
                      "relativ": [s / B_INF - 1.0 for s in zwei],
                      "eingetroffen": all((1.0 - BAND) * B_INF <= s <= (1.0 + BAND) * B_INF for s in zwei)}
    else:
        aus["PW2"] = {"eingetroffen": False, "grund": "weniger als drei Sprossen (nicht auswertbar)"}
    if n >= 2:
        abst = [abs(x["rho"] - RHO_Z) for x in sorted(sp, key=lambda x: -x["eps"])]
        monoton = all(abst[i + 1] < abst[i] for i in range(n - 1))
        letzte = abs(sp[0]["rho"] - RHO_Z)
        aus["laufen_zu_rho_z_info"] = {"abstaende_fallendes_eps": abst, "monoton": monoton,
                                       "kleinstes_eps_abstand_rho_z": letzte}
    if not aus["K0"]["bestanden"]:
        aus["PW2"]["nicht_auswertbar_K0"] = True
        aus["PW2"]["eingetroffen"] = False
    # Kontrolle (keine Regel): Hauptast je Paritaet gegen rho_z
    haupt = {}
    for parit in PARIT:
        al = aeste(wf, parit)
        start = [a for a in al if a[0]["j"] == 0]
        if not start:
            haupt[parit] = None
            continue
        a = min(start, key=lambda a: abs(a[0]["rho"] - RHO_Z))
        dek = []
        for d in range(int(math.ceil(J_MAX / J_ANZ)) + 1):
            pts = [x for x in a if d * J_ANZ <= x["j"] < (d + 1) * J_ANZ]
            if pts:
                dek.append({"eps_von": eps_j(d * J_ANZ), "max_abw": max(abs(x["rho"] - RHO_Z) for x in pts),
                            "n": len(pts)})
        haupt[parit] = {"j_von": a[0]["j"], "j_bis": a[-1]["j"], "rho_bei_j0": a[0]["rho"],
                        "abw_bei_j0": a[0]["rho"] - RHO_Z, "dekaden": dek,
                        "verlauf": [[x["j"], x["rho"], x["F2"]] for x in a]}
    aus["hauptast"] = haupt
    aus["ende"] = jetzt()
    schreibe(args.out, aus)
    log(f"K0 {aus['K0']}, Sprossen im Bereich n = {n}, PW2 {aus['PW2']['eingetroffen']}")
    for x in sp:
        log(f"  {x['par']:8s} ln(1/eps) = {x['ell']:.8f} eps = {x['eps']:.4e} rho = {x['rho']:.10f} U = {x['U']}")


BEGINN = jetzt()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="kommando", required=True)
    a = sp.add_parser("scan")
    a.add_argument("--h", type=float, required=True)
    a.add_argument("--D", type=float, default=30.0)
    a.add_argument("--j-von", type=int, default=0)
    a.add_argument("--j-bis", type=int, default=J_MAX)
    a.add_argument("--j-schritt", type=int, default=1)
    a.add_argument("--n-rho", type=int, default=2001)
    a.add_argument("--voll", action="store_true")
    a.add_argument("--out", required=True)
    a = sp.add_parser("sprossen")
    a.add_argument("--h", type=float, required=True)
    a.add_argument("--D", type=float, default=30.0)
    a.add_argument("--scan", required=True)
    a.add_argument("--scan-fein", required=True)
    a.add_argument("--drho", type=float, default=0.01)
    a.add_argument("--dell", type=float, default=0.5)
    a.add_argument("--out", required=True)
    a = sp.add_parser("dop853")
    a.add_argument("--sprossen", required=True)
    a.add_argument("--D", type=float, default=40.0)
    a.add_argument("--rtol", type=float, default=1e-12)
    a.add_argument("--out", required=True)
    a = sp.add_parser("k0")
    a.add_argument("--h-liste", type=lambda s: [float(v) for v in s.split(",")], default=[0.01, 0.005])
    a.add_argument("--h-g210", type=float, default=0.01)
    a.add_argument("--n-g210", type=int, default=2001)
    a.add_argument("--out", required=True)
    a = sp.add_parser("selbsttest")
    a.add_argument("--n-rho", type=int, default=2001)
    a.add_argument("--out", required=True)
    a = sp.add_parser("regel")
    a.add_argument("--k0", required=True)
    a.add_argument("--grob", required=True)
    a.add_argument("--fein", required=True)
    a.add_argument("--scan-fein", required=True)
    a.add_argument("--d40", default="")
    a.add_argument("--dop", default="")
    a.add_argument("--out", required=True)
    for p in sp.choices.values():
        p.add_argument("--konfig", required=True)
    args = ap.parse_args()
    lade_konfig(args.konfig)
    log(f"leiter_1d_beta {args.kommando} Beginn {BEGINN}, argv {sys.argv[1:]}, beta = {BETA}, omega_min^2 = {OM2_MIN}, "
        f"rho_z = {RHO_Z}, Fenster {LEITER_FENSTER}, eps_j = 10^({E0} + j/{J_ANZ}), j_max = {J_MAX}")
    {"scan": cmd_scan, "sprossen": cmd_sprossen, "k0": cmd_k0, "selbsttest": cmd_selbsttest, "dop853": cmd_dop853,
     "regel": cmd_regel}[args.kommando](args)


if __name__ == "__main__":
    main()
