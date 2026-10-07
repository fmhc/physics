#!/usr/bin/env python3
"""KOVARIANZ-EPS-1 (Runde 42, Code-Agent): Ist die 4D-Antwort auf die konforme l = 2-Verformung glatt in der Amplitude,
und liegt die Anomalie von KOVARIANZ-KUGEL-1 am Neuvernetzen?

Unveraendert importiert: kovarianz2d.py (KOVARIANZ-2D-GEGENPROBE, sha256 4d83a55d..., n allgemein, mit n = 4 bitgleich
zu kovarianz.py), kugel.py (INDUZIERT-KUGEL-1, c2a4d790...), kugel2.py (INDUZIERT-KUGEL-2, 15dcbd85...).
Alles auf S^4 (n = 4), dieselben Punkte (Saatschluessel [20261004, 39, 4, N, saat]), derselbe Transport (monotone
Umordnung in theta), dieselbe Laengenregel QI (Sehnen der isometrischen Einbettung, je Simplex auf das g-Volumen seines
Grosskreis-Simplex in der konformen Karte skaliert). Rundes Netz: Regel Q roh wie KUGEL-2 (nur Q).
  (a) Neuvernetzung wie KOVARIANZ-KUGEL-1: konvexe Huelle der verschobenen Punkte in der konformen Karte (kv2.huellnetz).
  (b) Mitgenommene Verbindungen: das runde Netz (kugelnetz, orientiert) bleibt, nur die Punkte werden verschoben und die
      Laengen neu berechnet. QI mit dem Betrag |V_g| (fuer nicht umgeklappte Simplizes gleich QI). Gezaehlt je Netz:
      umgeklappt (Orientierung in der Karte: n.c <= 0 mit der runden Eckenreihenfolge), entartet (Sehnen-Gram nicht
      positiv), fast entartet (Sehnen-Gram-Eigenwert < 1e-6), staerkste Quetschung V_Sehnen(b)/V_Sehnen(rund).
Verformungen: K(eps) sigma = eps (1 - 5 cos^2 theta) + c (kv2.verf_konform, n = 4); M Moebius-Schub t = 0,2 (nur (b));
  D(kappa) Scherkontrolle (nur (b)): sigma = 0, Punkte vorher mit der Faserdrehung um kappa theta in der (w1, w2)-Ebene
  verschoben (massstreu, nicht isometrisch, Geometrie unveraendert: reine Gitter-Scherantwort des festen Netzes).
Messgroesse: y = (Gamma_X - Gamma_Q(rund))/sqrt(N), gepaart je Saat und N.

Aufruf (nur ueber kleintest.sh):
  python kovarianz_eps.py vorab <aus.json>
  python kovarianz_eps.py kontrolle <aus.json> <kovarianz-kugel-laufordner>
  python kovarianz_eps.py messung <aus.json> <N-Liste> <saat0> <anzahl> [blind=0/1]
  python kovarianz_eps.py auswertung <laufordner> <kovarianz-kugel-laufordner> <aus.json> [N-Liste nur Codeprobe]
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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kugel as k1          # noqa: E402  (unveraendert aus INDUZIERT-KUGEL-1)
import kugel2 as k2         # noqa: E402  (unveraendert aus INDUZIERT-KUGEL-2)
import kovarianz2d as kv2   # noqa: E402  (unveraendert aus KOVARIANZ-2D-GEGENPROBE)

N_DIM = 4
S0E = 32.0 * math.pi ** 2
V0E = 8.0 * math.pi ** 2 / 3.0

# Festlegungen (PLAN)
T_M = 0.2                                                      # Moebius-Schub (wie KOVARIANZ-KUGEL-1)
EPS_A = (-0.1, -0.05, -0.025, 0.025, 0.05)                     # Bauweise (a), Karte ohne +0,1
EPS_B = (-0.1, -0.05, -0.025, -0.0125, 0.0125, 0.025, 0.05)    # Bauweise (b), dazu +-0,0125 (Zusatz)
EPS_NICHT_BAUBAR = (0.1,)                                      # Karte; Profil nicht einbettbar
EPS_PAARE = (0.025, 0.05)                                      # Karte: gerader/ungerader Anteil, Steigung
EPS_PAARE_B_ZUSATZ = (0.0125, 0.025, 0.05)                     # (b) beschreibend, drei Punkte
EPS_KE34 = 0.05                                                # KE3/KE4: groesste baubare symmetrische Amplitude
KAPPA_D = (0.25, 0.5)                                          # Scherkontrolle (b)
BETA_Q = (-1.613, 0.052)                                       # INDUZIERT-KUGEL-2, Regel Q roh
C_SCHER = (1.0 / 24.0, 0.0, 1.0 / 16.0)                        # Scherprognose: Schaetzung, untere, obere Schranke
N_HAUPT = (1000, 2000, 4000)
MESSWERTE = ("gamma", "gamma_M", "sum_log_m")


def kname(eps):
    return f"K{eps:+g}"


def verf_k(eps):
    return kv2.verf_konform(eps, N_DIM, kname(eps))


def verf_null():
    th = kv2.gitter()
    return kv2.Verformung("0", th, np.zeros_like(th), np.zeros_like(th), {}, N_DIM)


def verformungen():
    V = {"M": kv2.verf_moebius(T_M, N_DIM)}
    for e in sorted(set(EPS_A) | set(EPS_B)):
        V[kname(e)] = verf_k(e)
    V["0"] = verf_null()
    return V


def drehe(P, kappa):
    """Faserdrehung: w in der (w1, w2)-Ebene um kappa theta gedreht (massstreu, nicht isometrisch)."""
    th, w = kv2.theta_w(P, N_DIM)
    al = kappa * th
    c, s = np.cos(al), np.sin(al)
    w2 = w.copy()
    w2[:, 0] = c * w[:, 0] - s * w[:, 1]
    w2[:, 1] = s * w[:, 0] + c * w[:, 1]
    a = float(np.linalg.norm(P[0]))
    return a * np.concatenate([np.sin(th)[:, None] * w2, np.cos(th)[:, None]], axis=1)


# ---------------------------------------------------------------------- Netze
def rund(N, saat):
    """Rundes Netz und Regel Q roh, Operationen wie kv2.rundes_netz (n = 4), nur Q."""
    n = N_DIM
    kn = k1.kugelnetz(n, N, saat)
    tri, a, V_K = kn["tri"], kn["geo"]["a"], kn["geo"]["V_K"]
    X = kn["P"][tri]
    c = X.mean(axis=1)
    nv = k1.kreuz(X[:, 1:, :] - X[:, :1, :])
    nh = nv / np.linalg.norm(nv, axis=1)[:, None]
    d0 = np.einsum("fi,fi->f", nh, c)
    Jq5 = k2.j_mittel(X, d0, a, n, kv2.GM5[n])
    sqQ = kn["sqC"] * (Jq5 ** (2.0 / n))[:, None]
    q = k1.auswerten(tri, N, n, sqQ, V_K)
    _, V_ch0, lam0, _ = k1.p1(kn["sqC"], n)
    kn["_V_ch0"] = V_ch0
    rec = {"Q": q, "gueltig": bool(k1.kugel_gueltig(kn["pruefung"], n) and k1.lu_ok(q["lu"])),
           "F": int(tri.shape[0]), "geo": kn["geo"], "lam_min_sehnen": float(lam0.min())}
    return kn, rec


def bau_a(kn, verf, N, extra=False):
    """(a) Neuvernetzung: Operationen fuer QI wie kv2.verformtes_netz (n = 4), ohne CI."""
    n = N_DIM
    a, V_K = kn["geo"]["a"], kn["geo"]["V_K"]
    t0 = time.time()
    th, w = kv2.theta_w(kn["P"], n)
    th2, res = verf.transport(th)
    Pu = a * np.concatenate([np.sin(th2)[:, None] * w, np.cos(th2)[:, None]], axis=1)
    tri, X, nn, d0, pr = kv2.huellnetz(Pu, a, n)
    s, z = verf.profil(th2)
    Y = a * np.concatenate([s[:, None] * w, z[:, None]], axis=1)
    sq_ch = kv2.sehnen2(Y, tri, n)
    _, V_ch, lam_ch, _ = k1.p1(sq_ch, n)
    V_g = (nn / math.factorial(n)) * kv2.jw_mittel(X, d0, a, verf, n)
    sq_QI = sq_ch * np.sqrt(V_g / V_ch)[:, None]
    qi = k1.auswerten(tri, N, n, sq_QI, V_K)
    neu = ~np.isin(kv2.schluessel(tri, N), kv2.schluessel(kn["tri"], N))
    info = {"transport_res_max": res, "theta_versatz_max": float(np.max(np.abs(th2 - th))), "F": int(tri.shape[0]),
            "simplizes_neu": int(np.sum(neu)), "anteil_neu": float(np.mean(neu)),
            "V_g_summe_durch_N": math.fsum(V_g.tolist()) / V_K, "V_ch_durch_N": math.fsum(V_ch.tolist()) / V_K,
            "lam_min_sehnen": float(lam_ch.min()), "profil_min": verf.profil_min,
            "netz_gleich_rund": bool(int(np.sum(neu)) == 0 and tri.shape[0] == kn["tri"].shape[0])}
    pr_ok = k1.kugel_gueltig(pr, n)
    rec = {"QI": qi, "info": info, "kugel_gueltig": pr_ok, "lu_ok": k1.lu_ok(qi["lu"]),
           "gueltig": bool(pr_ok and k1.lu_ok(qi["lu"]) and res <= 1e-10 and verf.profil_min >= -1e-12),
           "sekunden": time.time() - t0}
    if extra:
        rec["_tri"], rec["_sq"] = tri, sq_QI
    return rec


def bau_b(kn, verf, N, P_start=None, extra=False, tri_ersatz=None):
    """(b) Mitgenommene Verbindungen: rundes Netz kn['tri'], Punkte verschoben, Laengen neu (QI mit |V_g|)."""
    n = N_DIM
    a, V_K = kn["geo"]["a"], kn["geo"]["V_K"]
    t0 = time.time()
    tri = kn["tri"] if tri_ersatz is None else tri_ersatz
    P0 = kn["P"] if P_start is None else P_start
    th, w = kv2.theta_w(P0, n)
    th2, res = verf.transport(th)
    Pu = a * np.concatenate([np.sin(th2)[:, None] * w, np.cos(th2)[:, None]], axis=1)
    X = Pu[tri]
    c = X.mean(axis=1)
    nv = k1.kreuz(X[:, 1:, :] - X[:, :1, :])
    orient = np.einsum("fi,fi->f", nv, c)
    nn = np.linalg.norm(nv, axis=1)
    nh = nv / np.maximum(nn, 1e-300)[:, None]
    d0 = np.einsum("fi,fi->f", nh, c)
    s, z = verf.profil(th2)
    Y = a * np.concatenate([s[:, None] * w, z[:, None]], axis=1)
    sq_ch = kv2.sehnen2(Y, tri, n)
    _, V_ch, lam_ch, _ = k1.p1(sq_ch, n)
    V_g = (nn / math.factorial(n)) * kv2.jw_mittel(X, d0, a, verf, n)       # mit Vorzeichen
    with np.errstate(divide="ignore", invalid="ignore"):
        fak = np.sqrt(np.abs(V_g) / V_ch)
    sq_QI = sq_ch * fak[:, None]
    qi = k1.auswerten(tri, N, n, sq_QI, V_K)
    um = orient <= 0
    V0 = kn.get("_V_ch0")
    quetsch = float(np.min(V_ch / V0)) if V0 is not None and tri_ersatz is None else None
    info = {"transport_res_max": res, "theta_versatz_max": float(np.max(np.abs(th2 - th))), "F": int(tri.shape[0]),
            "umgeklappt": int(np.sum(um)), "V_g_negativ": int(np.sum(V_g < 0)),
            "entartet_sehnen": int(np.sum(~(lam_ch > 0))), "fast_entartet_lam_1e-6": int(np.sum(lam_ch < 1e-6)),
            "lam_min_sehnen": float(lam_ch.min()), "quetschung_min_Vch_durch_rund": quetsch,
            "V_g_summe_durch_N": math.fsum(V_g.tolist()) / V_K,
            "V_g_betrag_summe_durch_N": math.fsum(np.abs(V_g).tolist()) / V_K,
            "V_ch_durch_N": math.fsum(V_ch.tolist()) / V_K, "profil_min": verf.profil_min,
            "faktor_min": float(np.nanmin(fak) ** 0.5), "faktor_max": float(np.nanmax(fak) ** 0.5)}
    rec = {"QI": qi, "info": info, "lu_ok": k1.lu_ok(qi["lu"]),
           "gueltig": bool(k1.lu_ok(qi["lu"]) and res <= 1e-10 and verf.profil_min >= -1e-12),
           "sekunden": time.time() - t0}
    if extra:
        rec["_tri"], rec["_sq"], rec["_um"] = tri, sq_QI, um
    return rec


# ---------------------------------------------------------------------- Vorab (Kontinuum, Scherprognose)
def scher_K(verf, m=40001):
    """<tr H^2> (S^4-Mittel) der Rueckholung phi*g = e^H g0 fuer den Transport der Verformung (massstreu: tr H = 0)."""
    th = np.linspace(1e-4, math.pi - 1e-4, m)
    t2, _ = verf.transport(th)
    dt = np.gradient(t2, th)
    sg = verf.sigma(t2)
    lr = sg + np.log(dt)
    la = sg + np.log(np.sin(t2) / np.sin(th))
    gw = np.sin(th) ** 3
    gw = gw / np.sum(gw)
    trH2 = 4.0 * (lr ** 2 + 3.0 * la ** 2)
    return {"trH2_mittel": float(np.sum(gw * trH2)), "spur_abw_max": float(np.max(np.abs(lr + 3.0 * la))),
            "scherung_max": float(np.max(np.abs(lr - la)))}


def scher_D(kappa, m=4001, mu=400):
    """<tr H^2> der Faserdrehung um kappa theta: Block [[1+g^2, g], [g, 1]], g = kappa rho sin theta, rho^2 ~ U(0,1)
    auf S^3; tr H^2 = 8 arsinh(g/2)^2."""
    th = np.linspace(0.0, math.pi, m)
    u = (np.arange(mu) + 0.5) / mu
    g = kappa * np.sqrt(u)[None, :] * np.sin(th)[:, None]
    tr = 8.0 * np.arcsinh(0.5 * g) ** 2
    gw = np.sin(th) ** 3
    return {"trH2_mittel": float(np.sum(gw * tr.mean(axis=1)) / np.sum(gw)), "kappa": kappa}


def vorab_daten():
    out = {"BETA_Q": BETA_Q, "C_SCHER": C_SCHER}
    V = verformungen()
    alle = sorted(set(EPS_A) | set(EPS_B) | set(EPS_NICHT_BAUBAR))
    for e in alle:
        v = V.get(kname(e)) or verf_k(e)
        d = {"eps": e, "c_norm": v.c_norm, "vol_rel": v.vol_rel, "profil_min": v.profil_min,
             "baubar": bool(v.profil_min >= -1e-12), "dS_einheit": v.dS,
             "y_E": BETA_Q[0] * v.dS / S0E, "y_E_se": BETA_Q[1] * abs(v.dS) / S0E,
             "dS_zweite_ordnung": 36.0 * (8.0 / 7.0) * V0E * e ** 2}
        if d["baubar"]:
            d["scherung"] = scher_K(v)
            d["y_scher_je_wurzelN"] = [c * d["scherung"]["trH2_mittel"] for c in C_SCHER]
        out[kname(e)] = d
    out["M"] = {"dS_einheit": V["M"].dS, "y_E": 0.0, "scherung": scher_K(V["M"])}
    out["D"] = {f"{k:g}": scher_D(k) for k in KAPPA_D}
    for k in KAPPA_D:
        out["D"][f"{k:g}"]["y_scher_je_wurzelN"] = [c * out["D"][f"{k:g}"]["trH2_mittel"] for c in C_SCHER]
    # gerade und ungerade Anteile der Einstein-Vorhersage
    gu = {}
    for e in EPS_PAARE_B_ZUSATZ:
        p, m_ = out[kname(e)], out[kname(-e)]
        gu[f"{e:g}"] = {"y_E_gerade": 0.5 * (p["y_E"] + m_["y_E"]), "y_E_ungerade": 0.5 * (p["y_E"] - m_["y_E"]),
                        "y_E_gerade_se": 0.5 * (p["y_E_se"] + m_["y_E_se"]),
                        "trH2_gerade": 0.5 * (p["scherung"]["trH2_mittel"] + m_["scherung"]["trH2_mittel"]),
                        "trH2_ungerade": 0.5 * (p["scherung"]["trH2_mittel"] - m_["scherung"]["trH2_mittel"])}
    out["gerade_ungerade"] = gu
    # Einstein-Steigung des geraden Anteils zwischen 0,025 und 0,05
    out["steigung_E_gerade_025_05"] = math.log(gu["0.05"]["y_E_gerade"] / gu["0.025"]["y_E_gerade"]) / math.log(2.0)
    out["steigung_scher_gerade_025_05"] = math.log(gu["0.05"]["trH2_gerade"] / gu["0.025"]["trH2_gerade"]) / math.log(2.0)
    # Proben
    kl = verf_k(1e-3)
    out["probe_K_kleines_eps"] = {"dS_durch_eps2": kl.dS / 1e-6, "erwartet": 36.0 * (8.0 / 7.0) * V0E}
    out["probe_K_scher_kleines_eps"] = {"trH2_durch_eps2": scher_K(kl)["trH2_mittel"] / 1e-6,
                                        "erwartet_48_mal_sin4": 48.0 * (96.0 / 140.0)}
    return out


# ---------------------------------------------------------------------- Modi
def modus_vorab(protokoll, out, ziel):
    out["vorab"] = vorab_daten()
    protokoll(json.dumps(out["vorab"], indent=1))
    k1.speichern(ziel, out)


def modus_kontrolle(kov_lauf, protokoll, out, ziel):
    n = N_DIM
    V = verformungen()
    # (C1) sigma = 0: (a) und (b) geben das runde Netz und Gamma_Q zurueck
    kn, rr = rund(1000, 991)
    ra0 = bau_a(kn, V["0"], 1000)
    rb0 = bau_b(kn, V["0"], 1000)
    out["C1_sigma0"] = {"a_minus_Q": ra0["QI"]["gamma"] - rr["Q"]["gamma"], "a_neu": ra0["info"]["anteil_neu"],
                        "b_minus_Q": rb0["QI"]["gamma"] - rr["Q"]["gamma"], "b_umgeklappt": rb0["info"]["umgeklappt"],
                        "gueltig": [ra0["gueltig"], rb0["gueltig"], rr["gueltig"]]}
    protokoll(f"C1: {out['C1_sigma0']}")
    k1.speichern(ziel, out)
    # (C2) Moebius: (a) netzgleich, (a) = (b) in Gamma
    raM = bau_a(kn, V["M"], 1000)
    rbM = bau_b(kn, V["M"], 1000)
    out["C2_moebius"] = {"a_netz_gleich": raM["info"]["netz_gleich_rund"], "a_minus_b": raM["QI"]["gamma"] - rbM["QI"]["gamma"],
                         "b_umgeklappt": rbM["info"]["umgeklappt"], "gueltig": [raM["gueltig"], rbM["gueltig"]]}
    protokoll(f"C2: {out['C2_moebius']}")
    k1.speichern(ziel, out)
    # (C3) Codepfad: rund und (a) gegen kv2 (live) und gegen KOVARIANZ-KUGEL-1-Laufdatei (Saat 0, N = 1000)
    knA, rrA = rund(1000, 0)
    knB, rrB = kv2.rundes_netz(1000, 0, n)
    gesp = None
    for d in sorted(glob.glob(os.path.join(kov_lauf, "messung-N1000-*.json"))):
        with open(d) as f:
            o = json.load(f)
        for rec in o.get("messungen", []):
            if rec["saat"] == 0 and rec["N"] == 1000:
                gesp = rec
    vK = verf_k(-0.1)
    ra = bau_a(knA, vK, 1000)
    rb = kv2.verformtes_netz(knB, vK, 1000, n)
    w = {"rund_Q": (rrA["Q"]["gamma"], rrB["Q"]["gamma"], gesp["rund"]["regeln"]["Q"]["gamma"] if gesp else None),
         "a_K-0.1_QI": (ra["QI"]["gamma"], rb["regeln"]["QI"]["gamma"],
                        gesp["verf"]["K"]["regeln"]["QI"]["gamma"] if gesp else None),
         "a_K-0.1_anteil_neu": (ra["info"]["anteil_neu"], rb["info"]["anteil_neu"],
                                gesp["verf"]["K"]["info"]["anteil_neu"] if gesp else None)}
    vP = verf_k(0.05)
    ra5 = bau_a(knA, vP, 1000)
    rb5 = kv2.verformtes_netz(knB, vP, 1000, n)
    w["a_K+0.05_QI"] = (ra5["QI"]["gamma"], rb5["regeln"]["QI"]["gamma"], None)
    out["C3_codepfad"] = {"werte_hier_kv2_gespeichert": w, "gespeichert_gefunden": gesp is not None,
                          "bitgleich_kv2": all(v[0] == v[1] for v in w.values()),
                          "bitgleich_gespeichert": bool(gesp) and all(v[0] == v[2] for v in w.values() if v[2] is not None)}
    protokoll(f"C3: {out['C3_codepfad']}")
    k1.speichern(ziel, out)
    # (C4) LU gegen dicht fuer (b), N = 400, Saat 990: K-0.1, K+0.05, D(0.5)
    kb = []
    kn4, _ = rund(400, 990)
    faelle = [(kname(-0.1), V[kname(-0.1)], None), (kname(0.05), V[kname(0.05)], None),
              ("D0.5", V["0"], drehe(kn4["P"], 0.5))]
    for name, v, Ps in faelle:
        r = bau_b(kn4, v, 400, P_start=Ps, extra=True)
        e = k1.auswerten(r["_tri"], 400, n, r["_sq"], kn4["geo"]["V_K"], dicht=True)
        Kd = e["_K"].toarray()
        ev = np.linalg.eigvalsh(Kd)
        sgn, ld = np.linalg.slogdet(Kd + 1.0 / 400)
        kb.append({"verf": name, "gueltig": r["gueltig"], "umgeklappt": r["info"]["umgeklappt"],
                   "abw_eigen": abs(e["gamma"] - 0.5 * math.fsum(np.log(ev[1:]).tolist())),
                   "abw_slogdet": abs(e["gamma"] - 0.5 * ld), "vorzeichen": float(sgn), "eigen_1": float(ev[1])})
        protokoll(f"C4 {name}: {kb[-1]}")
    out["C4_lu_dicht_b"] = kb
    k1.speichern(ziel, out)
    # (C5) Umklapp-Erkennung (Negativprobe): drei Simplizes mit vertauschten Ecken 0, 1 muessen als umgeklappt zaehlen
    tri_neg = kn["tri"].copy()
    tri_neg[:3] = tri_neg[:3][:, [1, 0, 2, 3, 4]]
    rneg = bau_b(kn, V["0"], 1000, tri_ersatz=tri_neg)
    out["C5_umklapp_negativprobe"] = {"umgeklappt": rneg["info"]["umgeklappt"], "erwartet": 3,
                                      "V_g_negativ": rneg["info"]["V_g_negativ"],
                                      "gamma_minus_Q": rneg["QI"]["gamma"] - rr["Q"]["gamma"]}
    protokoll(f"C5: {out['C5_umklapp_negativprobe']}")
    # (C6) Nicht baubar: eps = +0,1 (Profil nicht einbettbar)
    v01 = verf_k(0.1)
    out["C6_eps_plus_0.1"] = {"profil_min": v01.profil_min, "baubar": bool(v01.profil_min >= -1e-12)}
    protokoll(f"C6: {out['C6_eps_plus_0.1']}")
    # (C7) Umklappzahlen je Amplitude (b), N = 1000, 2000, Saat 991 (nur Geometrie, kein Gamma)
    c7 = {}
    for N in (1000, 2000):
        knx, _ = rund(N, 991) if N != 1000 else (kn, rr)
        for e in EPS_B:
            r = bau_b(knx, V[kname(e)], N)
            c7[f"N{N}/{kname(e)}"] = {k_: r["info"][k_] for k_ in ("umgeklappt", "entartet_sehnen", "fast_entartet_lam_1e-6",
                                                                    "lam_min_sehnen", "quetschung_min_Vch_durch_rund")}
        for k in KAPPA_D:
            r = bau_b(knx, V["0"], N, P_start=drehe(knx["P"], k))
            c7[f"N{N}/D{k:g}"] = {k_: r["info"][k_] for k_ in ("umgeklappt", "entartet_sehnen", "fast_entartet_lam_1e-6",
                                                                "lam_min_sehnen", "quetschung_min_Vch_durch_rund")}
        protokoll(f"C7 N={N}: " + json.dumps({k_: v_["umgeklappt"] for k_, v_ in c7.items() if k_.startswith(f'N{N}/')}))
    out["C7_umklappen"] = c7
    out["vorab"] = vorab_daten()
    k1.speichern(ziel, out)
    return out


def eine_messung(N, saat, V):
    t0 = time.time()
    kn, rr = rund(N, saat)
    rec = {"N": N, "saat": saat, "rund": rr, "a": {}, "b": {}}
    for e in EPS_A:
        rec["a"][kname(e)] = bau_a(kn, V[kname(e)], N)
    rec["b"]["M"] = bau_b(kn, V["M"], N)
    for e in EPS_B:
        rec["b"][kname(e)] = bau_b(kn, V[kname(e)], N)
    for k in KAPPA_D:
        rec["b"][f"D{k:g}"] = bau_b(kn, V["0"], N, P_start=drehe(kn["P"], k))
    rec["sekunden"] = time.time() - t0
    rec["rss_mb"] = k1.rss_mb()
    return rec


def modus_messung(Nlist, saat0, anzahl, blind, protokoll, out, ziel):
    V = verformungen()
    out.update({"n": N_DIM, "Nlist": Nlist, "saat0": saat0, "anzahl": anzahl, "blind": blind, "messungen": [],
                "EPS_A": EPS_A, "EPS_B": EPS_B, "KAPPA_D": KAPPA_D, "T_M": T_M})
    streu = {}
    for saat in range(saat0, saat0 + anzahl):
        for N in Nlist:
            rec = eine_messung(N, saat, V)
            gq = rec["rund"]["Q"].get("gamma")
            for bw in ("a", "b"):
                for nm, r in rec[bw].items():
                    if r["gueltig"] and rec["rund"]["gueltig"]:
                        streu.setdefault(f"N{N}/{bw}/{nm}", []).append((r["QI"]["gamma"] - gq) / math.sqrt(N))
            za = " ".join(f"{nm} {r['gueltig']:d} neu {r['info']['anteil_neu']:.3f}" for nm, r in rec["a"].items())
            zb = " ".join(f"{nm} {r['gueltig']:d} um {r['info']['umgeklappt']}" for nm, r in rec["b"].items())
            protokoll(f"N={N} saat={saat}: rund {rec['rund']['gueltig']:d}; a: {za}; b: {zb}; {rec['sekunden']:.1f} s, "
                      f"RSS {rec['rss_mb']:.0f} MB")
            if blind:
                for rg in [rec["rund"]["Q"]] + [r["QI"] for bw in ("a", "b") for r in rec[bw].values()]:
                    for q in MESSWERTE:
                        rg.pop(q, None)
                out["blind_streuung"] = {k: {"std_y": float(np.std(v, ddof=1)) if len(v) > 1 else None,
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
    return kv2.stat(v)


def y_wert(rec, bw, nm):
    return (rec[bw][nm]["QI"]["gamma"] - rec["rund"]["Q"]["gamma"]) / math.sqrt(rec["N"])


def u(b):
    return "eingetroffen" if b else "nicht eingetroffen"


def intervall_urteil(x, se, lo, hi):
    """Intervallregel: [x - 2 SE, x + 2 SE] in [lo, hi] -> eingetroffen; ganz ausserhalb -> nicht; sonst offen."""
    a_, b_ = x - 2.0 * se, x + 2.0 * se
    if a_ >= lo and b_ <= hi:
        return "eingetroffen"
    if b_ < lo or a_ > hi:
        return "nicht eingetroffen"
    return "nicht entschieden (2-SE-Intervall schneidet die Grenze)"


def modus_auswertung(ordner, kov_ordner, ziel, protokoll):
    recs, dateien = lade(ordner)
    vb = vorab_daten()
    Ns = list(N_HAUPT)
    saaten = sorted({k[0] for k in recs})
    out = {"dateien": dateien, "N_haupt": Ns, "vorab": vb,
           "festlegungen": {"EPS_A": EPS_A, "EPS_B": EPS_B, "EPS_PAARE": EPS_PAARE, "EPS_KE34": EPS_KE34,
                            "KAPPA_D": KAPPA_D, "BETA_Q": BETA_Q, "T_M": T_M}}
    namen_a = [kname(e) for e in EPS_A]
    namen_b = ["M"] + [kname(e) for e in EPS_B]
    namen_d = [f"D{k:g}" for k in KAPPA_D]
    # Tor je Bauweise
    tor = {}
    gute = {}
    for bw, namen in (("a", namen_a), ("b", namen_b), ("d", namen_d)):
        g_, aus, unv = [], [], []
        for s in saaten:
            if not all((s, N) in recs for N in Ns):
                unv.append(s)
                continue
            ok = all(recs[(s, N)]["rund"]["gueltig"] and all(
                recs[(s, N)]["b" if bw == "d" else bw][nm]["gueltig"] for nm in namen) for N in Ns)
            (g_ if ok else aus).append(s)
        voll = len(saaten) - len(unv)
        tor[bw] = {"saaten": len(saaten), "unvollstaendig": unv, "vollstaendig": voll, "gut": len(g_),
                   "ausgeschlossen": aus, "bestanden": bool(len(g_) >= 20 and len(aus) <= 0.1 * voll)}
        gute[bw] = g_
    out["tor"] = tor
    # KE0 Teil 1: Reproduktion KOVARIANZ-KUGEL-1 (rund Q und (a) K-0.1 QI je (Saat, N))
    kov, _ = lade(kov_ordner) if os.path.isdir(kov_ordner) else ({}, [])
    vgl, gleich, maxabw = 0, 0, 0.0
    vglr, gleichr, maxr = 0, 0, 0.0
    for (s, N), r in recs.items():
        if (s, N) in kov:
            a_ = r["a"][kname(-0.1)]["QI"]["gamma"]
            b_ = kov[(s, N)]["verf"]["K"]["regeln"]["QI"]["gamma"]
            vgl += 1
            gleich += int(a_ == b_)
            maxabw = max(maxabw, abs(a_ - b_))
            a2, b2 = r["rund"]["Q"]["gamma"], kov[(s, N)]["rund"]["regeln"]["Q"]["gamma"]
            vglr += 1
            gleichr += int(a2 == b2)
            maxr = max(maxr, abs(a2 - b2))
    kk1_y = [np.mean([(kov[(s, N)]["verf"]["K"]["regeln"]["QI"]["gamma"] - kov[(s, N)]["rund"]["regeln"]["Q"]["gamma"])
                      / math.sqrt(N) for N in Ns]) for s in sorted({k[0] for k in kov}) if all((s, N) in kov for N in Ns)]
    out["KE0_reproduktion"] = {"verglichen_aK": vgl, "gleich_aK": gleich, "max_abw_aK": maxabw,
                               "verglichen_rund": vglr, "gleich_rund": gleichr, "max_abw_rund": maxr,
                               "KK1_b_K_alle_saaten": stat(kk1_y)}
    # Messgroessen
    res = {}
    ymat = {}
    for bw, namen in (("a", namen_a), ("b", namen_b), ("d", namen_d)):
        quelle = "b" if bw == "d" else bw
        for nm in namen:
            yj, tab = [], {N: [] for N in Ns}
            for s in gute[bw]:
                ys = [y_wert(recs[(s, N)], quelle, nm) for N in Ns]
                for N, y in zip(Ns, ys):
                    tab[N].append(y)
                yj.append(float(np.mean(ys)))
            ymat[(bw, nm)] = (np.array(yj), {N: np.array(tab[N]) for N in Ns})
            res[f"{bw}/{nm}"] = {"b": stat(yj), "y_je_N": {str(N): stat(tab[N]) for N in Ns},
                                 "dGamma_je_N": {str(N): stat(np.array(tab[N]) * math.sqrt(N)) for N in Ns}}
            if nm.startswith("K"):
                eps = float(nm[1:])
                res[f"{bw}/{nm}"]["y_E"] = vb[kname(eps)]["y_E"]
            # Netzdaten
            nets = {}
            for N in Ns:
                infos = [recs[(s, N)][quelle][nm]["info"] for s in gute[bw]]
                if not infos:
                    continue
                if bw == "a":
                    nets[str(N)] = {"anteil_neu": float(np.mean([i_["anteil_neu"] for i_ in infos])),
                                    "netz_gleich": int(sum(i_["netz_gleich_rund"] for i_ in infos)),
                                    "V_ch_durch_N": float(np.mean([i_["V_ch_durch_N"] for i_ in infos]))}
                else:
                    um = np.array([i_["umgeklappt"] for i_ in infos])
                    nets[str(N)] = {"umgeklappt_mittel": float(um.mean()), "umgeklappt_max": int(um.max()),
                                    "netze_ohne_umklappen": int(np.sum(um == 0)),
                                    "entartet_summe": int(sum(i_["entartet_sehnen"] for i_ in infos)),
                                    "fast_entartet_mittel": float(np.mean([i_["fast_entartet_lam_1e-6"] for i_ in infos])),
                                    "lam_min": float(min(i_["lam_min_sehnen"] for i_ in infos)),
                                    "quetschung_min": float(min(i_["quetschung_min_Vch_durch_rund"] for i_ in infos)),
                                    "V_g_summe_max_abw": float(max(abs(i_["V_g_summe_durch_N"] - 1) for i_ in infos)),
                                    "V_g_betrag_summe": float(np.mean([i_["V_g_betrag_summe_durch_N"] for i_ in infos]))}
            res[f"{bw}/{nm}"]["netze"] = nets
    out["messgroessen"] = res

    # Gerade/ungerade Anteile je Bauweise (N-Mittel je Saat und je N)
    def gu_teil(bw, e):
        yp, tp = ymat[(bw, kname(e))]
        ym, tm = ymat[(bw, kname(-e))]
        G, U = 0.5 * (yp + ym), 0.5 * (yp - ym)
        jeN = {str(N): {"G": stat(0.5 * (tp[N] + tm[N])), "U": stat(0.5 * (tp[N] - tm[N]))} for N in Ns}
        return G, U, {"G": stat(G), "U": stat(U), "je_N": jeN,
                      "y_E_gerade": vb["gerade_ungerade"][f"{e:g}"]["y_E_gerade"],
                      "y_E_ungerade": vb["gerade_ungerade"][f"{e:g}"]["y_E_ungerade"]}
    gu = {}
    Gm = {}
    for bw, eset in (("a", EPS_PAARE), ("b", EPS_PAARE_B_ZUSATZ)):
        for e in eset:
            G, U, st = gu_teil(bw, e)
            Gm[(bw, e)] = (G, U)
            gu[f"{bw}/{e:g}"] = st
    out["gerade_ungerade"] = gu
    # Steigungen
    stg = {}
    for bw, eset, nm in (("a", EPS_PAARE, "G_025_05"), ("b", EPS_PAARE, "G_025_05"), ("b", EPS_PAARE_B_ZUSATZ, "G_drei")):
        dm = np.stack([Gm[(bw, e)][0] for e in eset], axis=1)
        s_, se_ = kv2.steigung_jackknife(dm, eset)
        stg[f"{bw}/{nm}"] = {"steigung": s_, "se": se_, "eps": list(eset)}
    for bw, namen_eps in (("a", (-0.025, -0.05, -0.1)), ("b", (-0.025, -0.05, -0.1))):
        dm = np.stack([ymat[(bw, kname(e))][0] for e in namen_eps], axis=1)
        s_, se_ = kv2.steigung_jackknife(dm, namen_eps)
        stg[f"{bw}/einseitig_negativ"] = {"steigung": s_, "se": se_, "eps": list(namen_eps)}
    out["steigungen"] = stg
    # Scherkontrolle (beschreibend): y_D/<trH^2>_D als Scherkoeffizient je sqrt(N); scherbereinigtes (b)
    sch = {}
    for k in KAPPA_D:
        nm = f"D{k:g}"
        trd = vb["D"][f"{k:g}"]["trH2_mittel"]
        jeN = {}
        for N in Ns:
            yd = ymat[("d", nm)][1][N]
            jeN[str(N)] = {"y": stat(yd), "c_scher": float(np.mean(yd)) / (math.sqrt(N) * trd) if len(yd) else None}
        sch[nm] = {"trH2": trd, "b": stat(ymat[("d", nm)][0]), "je_N": jeN}
    if gute["d"] and gute["b"]:
        gemeinsam = sorted(set(gute["d"]) & set(gute["b"]))
        bereinigt = {}
        for e in EPS_PAARE_B_ZUSATZ:
            trk = vb["gerade_ungerade"][f"{e:g}"]["trH2_gerade"]
            jeN = {}
            for N in Ns:
                vals = []
                for s in gemeinsam:
                    r = recs[(s, N)]
                    G_sN = 0.5 * (y_wert(r, "b", kname(e)) + y_wert(r, "b", kname(-e)))
                    yD = y_wert(r, "b", "D0.5")
                    vals.append(G_sN - yD * trk / vb["D"]["0.5"]["trH2_mittel"])
                jeN[str(N)] = stat(vals)
            bereinigt[f"{e:g}"] = {"trH2_K_gerade": trk, "je_N": jeN,
                                   "y_E_gerade": vb["gerade_ungerade"][f"{e:g}"]["y_E_gerade"]}
        sch["b_gerade_minus_skalierte_D0.5"] = bereinigt
    out["scherkontrolle"] = sch
    # Urteile
    urt = {}
    ta, tb = tor["a"]["bestanden"], tor["b"]["bestanden"]
    # KE0
    if ta and tb:
        rep = out["KE0_reproduktion"]
        rep_ok = rep["verglichen_aK"] > 0 and rep["max_abw_aK"] <= 1e-8 and rep["max_abw_rund"] <= 1e-8
        bM = res["b/M"]["b"]
        m_ok = abs(bM["mittel"]) <= 3.0 * bM["se"]
        urt["KE0"] = {"plan": u(rep_ok and m_ok), "karte": u(rep_ok and m_ok), "teil1_reproduktion": u(rep_ok),
                      "teil2_moebius_b": u(m_ok), "b_M": bM["mittel"], "se_M": bM["se"],
                      "in_se": bM["mittel"] / bM["se"] if bM["se"] else None,
                      "b_M_durch_bK_a_minus0.1": bM["mittel"] / res[f"a/{kname(-0.1)}"]["b"]["mittel"],
                      "b_a_K-0.1_hier": res[f"a/{kname(-0.1)}"]["b"], "KK1_b_K_alle": rep["KK1_b_K_alle_saaten"]}
    else:
        urt["KE0"] = {"plan": "nicht auswertbar (Tor)", "karte": "nicht auswertbar (Tor)"}
    # KE1 (a): gleiches Vorzeichen bei +eps und -eps fuer eps = 0,025 und 0,05
    if ta:
        paare = {}
        karte_ok, plan_vz = True, "eingetroffen"
        for e in EPS_PAARE:
            bp, bm = res[f"a/{kname(e)}"]["b"], res[f"a/{kname(-e)}"]["b"]
            sig_p, sig_m = abs(bp["mittel"]) >= 3 * bp["se"], abs(bm["mittel"]) >= 3 * bm["se"]
            gleich_vz = np.sign(bp["mittel"]) == np.sign(bm["mittel"])
            paare[f"{e:g}"] = {"b_plus": bp["mittel"], "se_plus": bp["se"], "b_minus": bm["mittel"], "se_minus": bm["se"],
                               "gleiches_vorzeichen": bool(gleich_vz), "beide_3SE": bool(sig_p and sig_m)}
            karte_ok = karte_ok and bool(gleich_vz)
            if sig_p and sig_m and not gleich_vz:
                plan_vz = "nicht eingetroffen"
            elif not (sig_p and sig_m and gleich_vz) and plan_vz == "eingetroffen":
                plan_vz = "nicht entschieden (ein Wert unter 3 SE)"
        sa = stg["a/G_025_05"]
        if plan_vz == "eingetroffen":
            if sa["steigung"] is None or sa["se"] is None:
                plan = "nicht entschieden (Steigung nicht bestimmbar)"
            elif sa["steigung"] + 2 * sa["se"] < 1.7:
                plan = "eingetroffen"
            elif sa["steigung"] - 2 * sa["se"] >= 1.7:
                plan = "nicht eingetroffen (gleiches Vorzeichen, aber gerader Anteil quadratisch)"
            else:
                plan = "nicht entschieden (Steigung schneidet 1,7)"
        else:
            plan = plan_vz
        urt["KE1"] = {"plan": plan, "karte": u(karte_ok), "paare": paare, "steigung_G_a": sa,
                      "plan_vorzeichenteil": plan_vz}
    else:
        urt["KE1"] = {"plan": "nicht auswertbar (Tor)", "karte": "nicht auswertbar (Tor)"}
    # KE2 (b): gerader Anteil Steigung 1,7 bis 2,3; ungerader Anteil unter 20 % des geraden (eps = 0,025 und 0,05)
    if tb:
        sb = stg["b/G_025_05"]
        Gs = {f"{e:g}": gu[f"b/{e:g}"] for e in EPS_PAARE}
        sig_ok = all(abs(v["G"]["mittel"]) >= 3 * v["G"]["se"] for v in Gs.values())
        quot = {k_: abs(v["U"]["mittel"]) / abs(v["G"]["mittel"]) for k_, v in Gs.items()}
        karte = (sb["steigung"] is not None and 1.7 <= sb["steigung"] <= 2.3 and all(q < 0.2 for q in quot.values()))
        if not sig_ok or sb["steigung"] is None or sb["se"] is None:
            plan = "nicht auswertbar (gerader Anteil unter 3 SE oder Vorzeichenwechsel)"
        else:
            p_s = intervall_urteil(sb["steigung"], sb["se"], 1.7, 2.3)
            p_u_ok = all(abs(v["U"]["mittel"]) + 2 * v["U"]["se"] < 0.2 * abs(v["G"]["mittel"]) for v in Gs.values())
            p_u_nein = any(abs(v["U"]["mittel"]) - 2 * v["U"]["se"] >= 0.2 * abs(v["G"]["mittel"]) for v in Gs.values())
            if p_s == "eingetroffen" and p_u_ok:
                plan = "eingetroffen"
            elif p_s == "nicht eingetroffen" or p_u_nein:
                plan = "nicht eingetroffen"
            else:
                plan = "nicht entschieden"
            urt["KE2_teile"] = {"steigung": p_s, "ungerade_klein": p_u_ok, "ungerade_gross": p_u_nein}
        urt["KE2"] = {"plan": plan, "karte": u(karte), "steigung_G_b": sb, "quotient_U_durch_G": quot,
                      "G_U": {k_: {"G": v["G"], "U": v["U"]} for k_, v in Gs.items()}}
    else:
        urt["KE2"] = {"plan": "nicht auswertbar (Tor)", "karte": "nicht auswertbar (Tor)"}
    # KE3 (b): gerader Anteil (y) bei eps = 0,05 von N = 1000 auf 4000: unter 15 % oder innerhalb 2 SE
    if tb:
        def ke3(e):
            j = gu[f"b/{e:g}"]["je_N"]
            g1, g4 = j[str(Ns[0])]["G"], j[str(Ns[-1])]["G"]
            d = g4["mittel"] - g1["mittel"]
            sd = math.hypot(g1["se"], g4["se"])
            ok = abs(d) <= 2 * sd or abs(d) <= 0.15 * abs(g1["mittel"])
            return ok, {"eps": e, "G_1000": g1["mittel"], "se_1000": g1["se"], "G_4000": g4["mittel"], "se_4000": g4["se"],
                        "aenderung": d, "se_aenderung": sd, "in_se": d / sd if sd else None,
                        "rel": d / g1["mittel"] if g1["mittel"] else None}
        ok3, z3 = ke3(EPS_KE34)
        urt["KE3"] = dict(z3, plan=u(ok3), karte=u(ok3),
                          zusatz={f"{e:g}": dict(ke3(e)[1], eingetroffen=ke3(e)[0]) for e in EPS_PAARE_B_ZUSATZ})
    else:
        urt["KE3"] = {"plan": "nicht auswertbar (Tor)", "karte": "nicht auswertbar (Tor)"}
    # KE4 (b): gerader Anteil bei eps = 0,05: Einstein-Vorzeichen (negativ) und innerhalb Faktor 3 der Vorhersage
    if tb:
        g = gu[f"b/{EPS_KE34:g}"]
        G, se = g["G"]["mittel"], g["G"]["se"]
        pred = g["y_E_gerade"]
        pse = vb["gerade_ungerade"][f"{EPS_KE34:g}"]["y_E_gerade_se"]
        r = G / pred
        sr = math.hypot(se, G * pse / abs(pred)) / abs(pred)
        karte = bool(G < 0 and 1.0 / 3.0 <= r <= 3.0)
        if G > 0 and G >= 3 * se:
            plan = "nicht eingetroffen (falsches Vorzeichen, >= 3 SE)"
        else:
            plan = intervall_urteil(r, sr, 1.0 / 3.0, 3.0)
            if plan == "eingetroffen" and not (G < 0 and abs(G) >= 3 * se):
                plan = "nicht entschieden (Vorzeichen unter 3 SE)"
        urt["KE4"] = {"plan": plan, "karte": u(karte), "eps": EPS_KE34, "G": G, "se": se, "pred": pred, "pred_se": pse,
                      "verhaeltnis": r, "se_verhaeltnis": sr,
                      "zusatz": {f"{e:g}": {"G": gu[f"b/{e:g}"]["G"]["mittel"], "se": gu[f"b/{e:g}"]["G"]["se"],
                                            "pred": gu[f"b/{e:g}"]["y_E_gerade"],
                                            "verhaeltnis": gu[f"b/{e:g}"]["G"]["mittel"] / gu[f"b/{e:g}"]["y_E_gerade"]}
                                 for e in EPS_PAARE_B_ZUSATZ}}
    else:
        urt["KE4"] = {"plan": "nicht auswertbar (Tor)", "karte": "nicht auswertbar (Tor)"}
    out["urteile"] = urt
    k1.speichern(ziel, out)
    protokoll(json.dumps({"tor": tor, "KE0_reproduktion": out["KE0_reproduktion"], "urteile": urt}, indent=1))
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
