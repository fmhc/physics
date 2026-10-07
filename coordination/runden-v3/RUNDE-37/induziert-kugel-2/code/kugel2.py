#!/usr/bin/env python3
"""INDUZIERT-KUGEL-2 (Runde 40, Code-Agent): zwei weitere Laengenregeln (G, Q) auf denselben S^4-Netzen wie
INDUZIERT-KUGEL-1.

Netze (Saatschluessel [20261004, 39, n, N, saat]), Regeln C und S, P1, LU, Gamma_M und Volumenumrechnung kommen
unveraendert aus kugel.py (INDUZIERT-KUGEL-1, sha256 c2a4d790...); dieses Skript ruft dessen Funktionen in derselben
Reihenfolge auf (kugelnetz, dann auswerten C, dann S) und fuegt hinzu:
  Regel Q (volumentreu je Simplex): je Simplex alle Sehnenlaengen mal <J>_T^(1/n); <J>_T = Mittel des Jacobi-Faktors
    J(x) = a^n d0/|x|^(n+1) der Radialprojektion ueber das flache Simplex, Grundmann-Moeller-Regel vom Grad 5
    (21 Punkte bei n = 4). Dann ist V_Q,T = Int_T J = Volumen des geodaetischen Simplex (bis auf den Quadraturfehler).
  Regel G (geodaetisch): Laenge = 2 a arcsin(c/(2a)) = a arccos(x_i.x_j/a^2) je Kante (gemeinsame Kanten gleich lang).
    Einbettbarkeit je Simplex: Gram-Matrix positiv definit (wie kugel.auswerten) und Cayley-Menger-Determinanten
    aller Seiten (Dreiecke, Tetraeder, 4-Simplex) mit richtigem Vorzeichen; Zaehlung je Netz.
    Gamma_G nur, wenn kein Simplex verletzt ist (sonst bricht kugel.auswerten vor der LU ab).
  Regel Gs (G*, Nebenlesart des Plans): G in den einbettbaren Simplizes, Q-Laengen in den nicht einbettbaren.
Torus: wird nicht neu gerechnet; die Auswertung uebernimmt Torus-Gamma aus den Laufdateien von INDUZIERT-KUGEL-1
(gleiche Saat, gleiches N, Torus-Saat 39000 + saat).

Aufruf (nur ueber kleintest.sh):
  python kugel2.py kontrolle <aus.json>
  python kugel2.py messung <aus.json> <N-Liste> <saat0> <anzahl> [blind=0/1]
"""
import itertools
import json
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
import scipy
import scipy.linalg as sla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kugel as k1  # noqa: E402  (unveraendert aus INDUZIERT-KUGEL-1)

N_DIM = 4
PAARE = k1.PAARE[N_DIM]
LAM_SCHWELLEN = (1e-2, 1e-3, 1e-4, 1e-6)


# ---------------------------------------------------------------------- Quadratur
def kompositionen(m, k):
    """Alle k-Tupel nichtnegativer ganzer Zahlen mit Summe m."""
    if k == 1:
        yield (m,)
        return
    for i in range(m + 1):
        for rest in kompositionen(m - i, k - 1):
            yield (i,) + rest


def gm_regel(n, s):
    """Grundmann-Moeller-Regel vom Grad 2s+1 auf dem n-Simplex: Gewichte (Summe 1, relativ zum Volumen) und
    baryzentrische Punkte. w_i = (-1)^i 2^(-2s) (d+n-2i)^d n!/(i! (d+n-i)!), Punkte (2 beta_j + 1)/(d+n-2i), |beta| = s-i."""
    d = 2 * s + 1
    gew, pkt = [], []
    for i in range(s + 1):
        w = Fraction((-1) ** i * (d + n - 2 * i) ** d * math.factorial(n),
                     2 ** (2 * s) * math.factorial(i) * math.factorial(d + n - i))
        for beta in kompositionen(s - i, n + 1):
            gew.append(float(w))
            pkt.append([float(Fraction(2 * b + 1, d + n - 2 * i)) for b in beta])
    return np.array(gew), np.array(pkt)


GM5 = gm_regel(N_DIM, 2)
GM3 = gm_regel(N_DIM, 1)


def j_mittel(X, d0, a, n, regel):
    """Quadraturmittel von J(x) = a^n d0/|x|^(n+1) ueber jedes Simplex (X: (F, n+1, n+1) Ecken in R^(n+1))."""
    gew, pkt = regel
    J = np.zeros(X.shape[0])
    for w, b in zip(gew, pkt):
        xq = np.einsum("j,fjk->fk", b, X)
        J += w * (a ** n * d0 / np.linalg.norm(xq, axis=1) ** (n + 1))
    return J


def j_grad2(X, c, d0, a, n):
    """Quadratur zweiten Grades wie kugel.kugelnetz (V_Q_quadratur von INDUZIERT-KUGEL-1)."""
    tq = 1.0 / math.sqrt(n + 2.0)
    Jq = np.zeros(X.shape[0])
    for i in range(n + 1):
        xq = c + tq * (X[:, i] - c)
        Jq += a ** n * d0 / np.linalg.norm(xq, axis=1) ** (n + 1)
    return Jq / (n + 1)


# ---------------------------------------------------------------------- Cayley-Menger
def cm_vol2(sq, n):
    """Quadrierte Volumina aller Seiten der Dimension k = 2..n je Simplex aus Cayley-Menger-Determinanten:
    V_k^2 = (-1)^(k+1) CM_k/(2^k (k!)^2). Rueckgabe {k: (F, Anzahl Seiten)}; einbettbar heisst V_k^2 > 0 fuer alle."""
    F = sq.shape[0]
    D = np.zeros((F, n + 1, n + 1))
    for e, (i, j) in enumerate(PAARE if n == N_DIM else k1.PAARE[n]):
        D[:, i, j] = sq[:, e]
        D[:, j, i] = sq[:, e]
    out = {}
    for k in range(2, n + 1):
        seiten = list(itertools.combinations(range(n + 1), k + 1))
        werte = np.empty((F, len(seiten)))
        for si, s in enumerate(seiten):
            M = np.ones((F, k + 2, k + 2))
            M[:, 0, 0] = 0.0
            idx = np.array(s)
            M[:, 1:, 1:] = D[:, idx][:, :, idx]
            werte[:, si] = (-1) ** (k + 1) * np.linalg.det(M) / (2 ** k * math.factorial(k) ** 2)
        out[k] = werte
    return out


def einbettung(sq, n):
    """Zaehlungen je Netz: Gram-Kriterium (lambda_min > 0) und Cayley-Menger je Seitendimension."""
    _, V, lam, _ = k1.p1(sq, n)
    vol2 = cm_vol2(sq, n)
    gram_schlecht = ~(lam > 0)
    cm_schlecht = np.zeros(sq.shape[0], dtype=bool)
    z = {}
    for k, w in vol2.items():
        sch = np.any(~(w > 0), axis=1)
        z[f"cm{k}_simplizes_verletzt"] = int(np.sum(sch))
        z[f"cm{k}_seiten_verletzt_je_simplex_summe"] = int(np.sum(~(w > 0)))
        cm_schlecht |= sch
    z.update({"gram_nicht_einbettbar": int(np.sum(gram_schlecht)), "cm_irgendeine_seite": int(np.sum(cm_schlecht)),
              "gram_cm_uneinig": int(np.sum(gram_schlecht != cm_schlecht)), "F": int(sq.shape[0]),
              "anteil_nicht_einbettbar": float(np.mean(gram_schlecht | cm_schlecht)),
              "lam_min": float(lam.min()), "V_einbettbar": math.fsum(V[~(gram_schlecht | cm_schlecht)].tolist())})
    for s in LAM_SCHWELLEN:
        z[f"lam_unter_{s:g}"] = int(np.sum(lam < s))
    return z, gram_schlecht | cm_schlecht, lam


# ---------------------------------------------------------------------- eine Messung (Saat, N)
def eine_messung(N, saat, protokoll):
    n = N_DIM
    t0 = time.time()
    kn = k1.kugelnetz(n, N, saat)
    tri = kn["tri"]
    V_K = kn["geo"]["V_K"]
    a = kn["geo"]["a"]
    regeln = {}
    for r, sq in (("C", kn["sqC"]), ("S", kn["sqS"])):          # wie INDUZIERT-KUGEL-1 (Reihenfolge C, S)
        regeln[r] = k1.auswerten(tri, N, n, sq, V_K)
    t_cs = time.time() - t0
    # Simplexdaten wie in kugel.kugelnetz (nach der Orientierung)
    t1 = time.time()
    X = kn["P"][tri]
    c = X.mean(axis=1)
    nv = k1.kreuz(X[:, 1:, :] - X[:, :1, :])
    nh = nv / np.linalg.norm(nv, axis=1)[:, None]
    d0 = np.einsum("fi,fi->f", nh, c)
    J_c = a ** n * d0 / np.linalg.norm(c, axis=1) ** (n + 1)
    # Regel Q
    Jq5 = j_mittel(X, d0, a, n, GM5)
    Jq3 = j_mittel(X, d0, a, n, GM3)
    Jq2 = j_grad2(X, c, d0, a, n)
    sqQ = kn["sqC"] * (Jq5 ** (2.0 / n))[:, None]
    VCk = np.linalg.norm(nv, axis=1) / math.factorial(n)
    qinfo = {"J_neu_gegen_kugelnetz_max_rel": float(np.max(np.abs(J_c / kn["J"] - 1.0))),
             "V_Q5": math.fsum((VCk * Jq5).tolist()), "V_Q3": math.fsum((VCk * Jq3).tolist()),
             "V_Q2_neu": math.fsum((VCk * Jq2).tolist()),
             "max_rel_Jq5_gegen_Jq3": float(np.max(np.abs(Jq5 / Jq3 - 1.0))),
             "max_rel_Jq5_gegen_Jq2": float(np.max(np.abs(Jq5 / Jq2 - 1.0))),
             "Jq5_min": float(Jq5.min()), "Jq5_max": float(Jq5.max()),
             "Jc_durch_Jq5_mittel": float(np.mean(J_c / Jq5)),
             "faktor_Q_durch_S_min": float(np.min((Jq5 / J_c) ** (1.0 / n))),
             "faktor_Q_durch_S_max": float(np.max((Jq5 / J_c) ** (1.0 / n)))}
    qinfo["V_Q2_neu_gegen_KUGEL1_rel"] = qinfo["V_Q2_neu"] / kn["geo"]["V_Q_quadratur"] - 1.0
    regeln["Q"] = k1.auswerten(tri, N, n, sqQ, V_K)
    # Regel G
    cC = np.sqrt(kn["sqC"])
    dG = 2.0 * a * np.arcsin(cC / (2.0 * a))
    sqG = dG ** 2
    P = kn["P"]
    dA = np.stack([a * np.arccos(np.clip(np.einsum("fi,fi->f", P[tri[:, i]], P[tri[:, j]]) / a ** 2, -1.0, 1.0))
                   for (i, j) in PAARE], axis=1)
    ginfo, schlecht, lamG = einbettung(sqG, n)
    ginfo["arcsin_gegen_arccos_max_rel"] = float(np.max(np.abs(dA / dG - 1.0)))
    ginfo["G_durch_C_laenge_max"] = float(np.max(dG / cC))
    cinfo, schlechtC, lamC = einbettung(kn["sqC"], n)
    ginfo["C_kontrolle"] = {k: cinfo[k] for k in ("gram_nicht_einbettbar", "cm_irgendeine_seite", "gram_cm_uneinig",
                                                   "lam_min") + tuple(f"lam_unter_{s:g}" for s in LAM_SCHWELLEN)}
    del lamC, schlechtC
    regeln["G"] = k1.auswerten(tri, N, n, sqG, V_K)
    if np.any(schlecht):
        sqGs = np.where(schlecht[:, None], sqQ, sqG)
        regeln["Gs"] = k1.auswerten(tri, N, n, sqGs, V_K)
        ginfo["Gs_gleich_G"] = False
    else:
        regeln["Gs"] = dict(regeln["G"])
        ginfo["Gs_gleich_G"] = True
    ginfo["Gs_ersetzt"] = int(np.sum(schlecht))
    t_neu = time.time() - t1
    pr = kn["pruefung"]
    kg = k1.kugel_gueltig(pr, n)
    lu_ok = {r: k1.lu_ok(regeln[r]["lu"]) for r in regeln}
    rec = {"n": n, "N": N, "saat": saat,
           "kugel": {"geo": kn["geo"], "pruefung": pr, "gueltig": kg, "regeln": regeln, "G_einbettung": ginfo,
                     "Q_quadratur": qinfo},
           "lu_ok": lu_ok,
           "gueltig": bool(kg and all(lu_ok[r] for r in ("C", "S", "Q", "Gs"))),
           "gueltig_G": bool(kg and lu_ok["G"]),
           "sek_C_S": t_cs, "sek_neu": t_neu, "sekunden": time.time() - t0, "rss_mb": k1.rss_mb()}
    lus = " ".join(f"{r} {regeln[r]['lu'].get('sek_lu', -1):.1f}" for r in ("C", "S", "Q", "G", "Gs"))
    protokoll(f"N={N} saat={saat}: gueltig {rec['gueltig']} (Kugel {kg}, LU {lu_ok}); G nicht einbettbar "
              f"{ginfo['gram_nicht_einbettbar']} (CM: 2 {ginfo['cm2_simplizes_verletzt']}, 3 "
              f"{ginfo['cm3_simplizes_verletzt']}, 4 {ginfo['cm4_simplizes_verletzt']}, uneinig "
              f"{ginfo['gram_cm_uneinig']}) von F {ginfo['F']}; C nicht einbettbar "
              f"{ginfo['C_kontrolle']['gram_nicht_einbettbar']}; V_Q5/V_K {qinfo['V_Q5'] / V_K:.7f}, V_Q2/V_K "
              f"{qinfo['V_Q2_neu'] / V_K:.6f}, Jq5/Jq3 {qinfo['max_rel_Jq5_gegen_Jq3']:.1e}, V_G(einb.)/V_K "
              f"{ginfo['V_einbettbar'] / V_K:.5f}; LU {lus} s; C+S {t_cs:.1f} s, neu {t_neu:.1f} s, gesamt "
              f"{rec['sekunden']:.1f} s, RSS {k1.rss_mb():.0f} MB")
    return rec


MESSWERTE = ("gamma", "gamma_M", "sum_log_m")


def modus_messung(Nlist, saat0, anzahl, blind, protokoll, out, ziel):
    out.update({"n": N_DIM, "Nlist": Nlist, "saat0": saat0, "anzahl": anzahl, "blind": blind, "messungen": []})
    for saat in range(saat0, saat0 + anzahl):
        for N in Nlist:
            rec = eine_messung(N, saat, protokoll)
            if blind:
                for r in rec["kugel"]["regeln"].values():
                    for q in MESSWERTE:
                        r.pop(q, None)
            out["messungen"].append(rec)
            k1.speichern(ziel, out)
    return out


# ---------------------------------------------------------------------- Kontrollen
def modus_kontrolle(protokoll, out, ziel):
    n = N_DIM
    rng = np.random.default_rng([20261004, 40, 7])
    # (KQ1) Quadratur: baryzentrische Monome Grad <= 6 gegen n! alpha!/(n + |alpha|)!
    kq = {}
    for name, regel, grad in (("GM5", GM5, 5), ("GM3", GM3, 3)):
        gew, pkt = regel
        fehler = {}
        for g in range(0, 7):
            m = 0.0
            for alpha in kompositionen(g, n + 1):
                exakt = math.factorial(n) * math.prod(math.factorial(x) for x in alpha) / math.factorial(n + g)
                quad = float(np.sum(gew * np.prod(pkt ** np.array(alpha)[None, :], axis=1)))
                m = max(m, abs(quad - exakt) / exakt)
            fehler[str(g)] = m
        kq[name] = {"punkte": int(len(gew)), "gewichtssumme": float(np.sum(gew)), "grad": grad,
                    "max_rel_fehler_je_grad": fehler,
                    "exakt_bis_grad": max([gg for gg in range(7) if all(fehler[str(h)] <= 1e-12 for h in range(gg + 1))],
                                          default=-1)}
    out["KQ1_quadratur"] = kq
    protokoll(f"KQ1 Quadratur: {kq}")
    k1.speichern(ziel, out)
    # (KCM) Cayley-Menger-Proben: regulaeres Simplex, Dreiecksverletzung, flaches Quadrat mit geodaetischen Laengen
    reg = np.eye(5)                                                     # regulaeres 4-Simplex in R^5 (Kante sqrt 2)
    sq_reg = np.array([[np.sum((reg[j] - reg[i]) ** 2) for (i, j) in PAARE]])
    sq_dreieck = sq_reg.copy()
    sq_dreieck[0, 0] = 9.0                                              # Kante (0,1) = 3 > 2 sqrt 2: Dreieck (0,1,2) verletzt
    # Kugel S^4 vom Radius a = 3: vier Punkte als Quadrat auf einem kleinen Kreis (Radius r), fuenfter Punkt daneben
    a, r, h = 3.0, 1.0, 0.05
    z0 = math.sqrt(a ** 2 - r ** 2)
    quad = [np.array([r * math.cos(t), r * math.sin(t), 0.0, 0.0, z0]) for t in (0.0, math.pi / 2, math.pi, 1.5 * math.pi)]
    quad[1] = quad[1] + np.array([0.0, 0.0, h, 0.0, 0.0])
    quad[1] *= a / np.linalg.norm(quad[1])                               # Tetraeder mit kleiner Dicke ~ h
    p5 = np.array([0.0, 0.0, 0.3, 1.0, 0.0])
    p5 = p5 + np.array([0.0, 0.0, 0.0, 0.0, z0])
    p5 *= a / np.linalg.norm(p5)
    Pq = np.array(quad + [p5])
    sq_sehne = np.array([[np.sum((Pq[j] - Pq[i]) ** 2) for (i, j) in PAARE]])
    sq_geo = (2.0 * a * np.arcsin(np.sqrt(sq_sehne) / (2.0 * a))) ** 2
    kcm = {}
    for name, sq in (("regulaer", sq_reg), ("dreieck_verletzt", sq_dreieck), ("quadrat_sehne", sq_sehne),
                     ("quadrat_geodaetisch", sq_geo)):
        z, sch, lam = einbettung(sq, n)
        kcm[name] = {"gram_nicht_einbettbar": z["gram_nicht_einbettbar"], "cm2": z["cm2_simplizes_verletzt"],
                     "cm3": z["cm3_simplizes_verletzt"], "cm4": z["cm4_simplizes_verletzt"], "lam_min": z["lam_min"]}
    out["KCM_cayley_menger"] = kcm
    protokoll(f"KCM: {kcm}")
    k1.speichern(ziel, out)
    # (KQ2, KG1, KCM-Netz) Netze Saat 991 (wie KF in INDUZIERT-KUGEL-1): Volumina, J, Formeln, Einbettbarkeit
    kf = []
    for N in (1000, 2000):
        kn = k1.kugelnetz(n, N, 991)
        tri, aa = kn["tri"], kn["geo"]["a"]
        X = kn["P"][tri]
        c = X.mean(axis=1)
        nv = k1.kreuz(X[:, 1:, :] - X[:, :1, :])
        nh = nv / np.linalg.norm(nv, axis=1)[:, None]
        d0 = np.einsum("fi,fi->f", nh, c)
        J_c = aa ** n * d0 / np.linalg.norm(c, axis=1) ** (n + 1)
        VCk = np.linalg.norm(nv, axis=1) / math.factorial(n)
        Jq5, Jq3, Jq2 = j_mittel(X, d0, aa, n, GM5), j_mittel(X, d0, aa, n, GM3), j_grad2(X, c, d0, aa, n)
        cC = np.sqrt(kn["sqC"])
        dG = 2.0 * aa * np.arcsin(cC / (2.0 * aa))
        P = kn["P"]
        dA = np.stack([aa * np.arccos(np.clip(np.einsum("fi,fi->f", P[tri[:, i]], P[tri[:, j]]) / aa ** 2, -1.0, 1.0))
                       for (i, j) in PAARE], axis=1)
        zG, schG, _ = einbettung(dG ** 2, n)
        zC, _, _ = einbettung(kn["sqC"], n)
        sqQ = kn["sqC"] * (Jq5 ** (2.0 / n))[:, None]
        zQ, _, _ = einbettung(sqQ, n)
        V_K = kn["geo"]["V_K"]
        rec = {"N": N, "a": aa, "J_gegen_kugelnetz_max_rel": float(np.max(np.abs(J_c / kn["J"] - 1.0))),
               "V_Q5/V_K-1": math.fsum((VCk * Jq5).tolist()) / V_K - 1.0,
               "V_Q3/V_K-1": math.fsum((VCk * Jq3).tolist()) / V_K - 1.0,
               "V_Q2/V_K-1": math.fsum((VCk * Jq2).tolist()) / V_K - 1.0,
               "V_Q2_gegen_KUGEL1_rel": math.fsum((VCk * Jq2).tolist()) / kn["geo"]["V_Q_quadratur"] - 1.0,
               "max_rel_Jq5_gegen_Jq3": float(np.max(np.abs(Jq5 / Jq3 - 1.0))),
               "max_rel_Jq5_gegen_Jq2": float(np.max(np.abs(Jq5 / Jq2 - 1.0))),
               "arcsin_gegen_arccos_max_rel": float(np.max(np.abs(dA / dG - 1.0))),
               "G": zG, "C": {k: zC[k] for k in ("gram_nicht_einbettbar", "cm_irgendeine_seite", "gram_cm_uneinig")},
               "Q": {k: zQ[k] for k in ("gram_nicht_einbettbar", "cm_irgendeine_seite", "gram_cm_uneinig")},
               "V_Q_regel/V_K-1": zQ["V_einbettbar"] / V_K - 1.0}
        kf.append(rec)
        protokoll(f"KQ2/KG1 N={N}: {rec}")
        k1.speichern(ziel, out | {"KQ2_KG1_netze": kf})
    out["KQ2_KG1_netze"] = kf
    # (KB2) LU gegen dicht fuer Q und Gs (S^4, N = 400, Saat 990 wie KB in INDUZIERT-KUGEL-1); nur Abweichungen
    kb = []
    N = 400
    kn = k1.kugelnetz(n, N, 990)
    tri, aa, V_K = kn["tri"], kn["geo"]["a"], kn["geo"]["V_K"]
    X = kn["P"][tri]
    c = X.mean(axis=1)
    nv = k1.kreuz(X[:, 1:, :] - X[:, :1, :])
    nh = nv / np.linalg.norm(nv, axis=1)[:, None]
    d0 = np.einsum("fi,fi->f", nh, c)
    Jq5 = j_mittel(X, d0, aa, n, GM5)
    sqQ = kn["sqC"] * (Jq5 ** (2.0 / n))[:, None]
    sqG = (2.0 * aa * np.arcsin(np.sqrt(kn["sqC"]) / (2.0 * aa))) ** 2
    zG, schG, _ = einbettung(sqG, n)
    sqGs = np.where(schG[:, None], sqQ, sqG)
    for name, sq in (("Q", sqQ), ("Gs", sqGs)):
        e = k1.auswerten(tri, N, n, sq, V_K, dicht=True)
        Kd = e["_K"].toarray()
        m = e["_m"]
        ev = np.linalg.eigvalsh(Kd)
        sgn, ld = np.linalg.slogdet(Kd + 1.0 / N)
        gev = sla.eigh(Kd, np.diag(m), eigvals_only=True)
        gM_dicht = 0.5 * math.fsum(np.log(np.sort(gev)[1:]).tolist())
        lamb = 1.37
        e2 = k1.auswerten(tri, N, n, sq * lamb ** 2, V_K)
        kb.append({"regel": name, "lu_ok": k1.lu_ok(e["lu"]), "nicht_einbettbar": e["nicht_einbettbar"],
                   "abw_eigen": abs(e["gamma"] - 0.5 * math.fsum(np.log(ev[1:]).tolist())),
                   "abw_slogdet": abs(e["gamma"] - 0.5 * ld), "vorzeichen": float(sgn), "eigen_0": float(ev[0]),
                   "eigen_1": float(ev[1]), "gammaM_abw_dicht": abs(e["gamma_M"] - gM_dicht),
                   "skal_korr_abw": abs((e2["gamma"] + e2["korr"]) - (e["gamma"] + e["korr"])),
                   "skal_korrM_abw": abs((e2["gamma_M"] + e2["korr_M"]) - (e["gamma_M"] + e["korr_M"])),
                   "G_nicht_einbettbar_N400": zG["gram_nicht_einbettbar"]})
        protokoll(f"KB2 {name}: {kb[-1]}")
    out["KB2_lu_dicht"] = kb
    k1.speichern(ziel, out)
    return out


def main():
    modus = sys.argv[1]
    t0 = time.time()
    log = []

    def protokoll(s):
        print(s, flush=True)
        log.append(s)

    out = {"modus": modus, "argv": sys.argv[1:], "numpy": np.__version__, "scipy": scipy.__version__}
    ziel = sys.argv[2]
    if modus == "kontrolle":
        modus_kontrolle(protokoll, out, ziel)
    elif modus == "messung":
        Nlist = [int(x) for x in sys.argv[3].split(",")]
        saat0, anzahl = int(sys.argv[4]), int(sys.argv[5])
        opt = dict(a.split("=", 1) for a in sys.argv[6:])
        modus_messung(Nlist, saat0, anzahl, opt.get("blind", "0") == "1", protokoll, out, ziel)
    else:
        raise SystemExit("unbekannter Modus")
    out["laufzeit_gesamt_s"] = time.time() - t0
    out["rss_mb_ende"] = k1.rss_mb()
    out["protokoll"] = log
    k1.speichern(ziel, out)
    print("geschrieben", ziel, f"{time.time() - t0:.1f} s", flush=True)


if __name__ == "__main__":
    main()
