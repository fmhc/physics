#!/usr/bin/env python3
"""INDUZIERT-XI-KUGEL-1 (Runde 40/41, Code-Agent): Kruemmungskopplung xi R phi^2 eines P1-Skalars auf denselben
S^4-Netzen wie INDUZIERT-KUGEL-1/-2 (Saatschluessel [20261004, 39, 4, N, saat]), Laengenregel Q (volumentreu je Simplex).

Operator A(xi) = K + xi R M:
  K  = P1-Steifigkeit der Regel Q (kugel.p1 / kugel.matrix, unveraendert), Laengen wie kugel2.eine_messung (Q).
  R  = n(n-1)/a^2 = 12/a^2 (Skalarkruemmung der Kugel vom Radius a).
  M  = konzentrierte P1-Masse diag(m_i), m_i = Summe_(T an i) V_T/(n+1) (dieselbe Masse wie Gamma_M in kugel.auswerten).
  Nebenlesart Mk (nur xi = 1/6): konsistente P1-Masse M_T,ij = V_T (1 + delta_ij)/((n+1)(n+2)).
xi = 0: Gamma(0) = kugel.auswerten (geerdete LU, 1/2 log det' K): Weg und Zahlen wie Regel Q in kugel2.eine_messung.
xi > 0: Gamma(xi) = 1/2 log det A(xi) (A regulaer, LU ohne Erdung, dieselben splu-Optionen wie kugel.gamma_lu).
Fruehere Nullmode: Der konstante Vektor ist exakter verallgemeinerter Eigenvektor von (A(xi), M) zum Eigenwert xi R, und
  es gilt exakt Gamma(xi) = 1/2 ln(xi R V_R/N) + Gamma(0) + 1/2 Summe'_k ln(1 + xi R/mu_k) (mu_k: verallgemeinerte
  Eigenwerte von (K, M) ohne die Null; V_R = Summe m_i = 1^T M 1; Gamma(0) mit det' K = N det K_(0)). Gespeichert:
  gamma (roh), nullmode = 1/2 ln(xi R V_R/N), gamma_tilde = gamma - nullmode. Fuer Mk gilt dasselbe (1^T Mk 1 = V_R).
Torus: nicht neu gerechnet (R = 0, Referenz unveraendert); die Auswertung nimmt ihn aus den Laufdateien von
  INDUZIERT-KUGEL-1.

Aufruf (nur ueber kleintest.sh):
  python xi_kugel.py kontrolle <aus.json>
  python xi_kugel.py messung <aus.json> <N-Liste> <saat0> <anzahl> [blind=0/1]
"""
import json
import math
import os
import sys
import time

import numpy as np
import scipy
import scipy.linalg as sla
import scipy.sparse as sp
import scipy.sparse.linalg as spla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kugel as k1   # noqa: E402  (unveraendert aus INDUZIERT-KUGEL-1, sha256 c2a4d790...)
import kugel2 as k2  # noqa: E402  (unveraendert aus INDUZIERT-KUGEL-2, sha256 15dcbd85...; Regel Q)

N_DIM = 4
XI_WERTE = (1.0 / 12.0, 1.0 / 6.0, 0.25)       # xi > 0 (xi = 0 ueber kugel.auswerten)
XI_NAMEN = ("1/12", "1/6", "1/4")
XI_KONS = 1.0 / 6.0
MESSWERTE = ("gamma", "gamma_M", "sum_log_m", "gamma_tilde")


def q_laengen(kn, n=N_DIM):
    """Regel Q wie kugel2.eine_messung (dieselben Operationen in derselben Reihenfolge)."""
    tri = kn["tri"]
    a = kn["geo"]["a"]
    X = kn["P"][tri]
    c = X.mean(axis=1)
    nv = k1.kreuz(X[:, 1:, :] - X[:, :1, :])
    nh = nv / np.linalg.norm(nv, axis=1)[:, None]
    d0 = np.einsum("fi,fi->f", nh, c)
    Jq5 = k2.j_mittel(X, d0, a, n, k2.GM5)
    sqQ = kn["sqC"] * (Jq5 ** (2.0 / n))[:, None]
    VCk = np.linalg.norm(nv, axis=1) / math.factorial(n)
    return sqQ, {"V_Q5": math.fsum((VCk * Jq5).tolist()), "Jq5_min": float(Jq5.min()), "Jq5_max": float(Jq5.max())}


def masse_konsistent(tri, N, V, n=N_DIM):
    """Konsistente P1-Masse: M_T,ij = V_T (1 + delta_ij)/((n+1)(n+2)); Zeilensumme = konzentrierte Masse."""
    loc = (np.ones((n + 1, n + 1)) + np.eye(n + 1)) / float((n + 1) * (n + 2))
    return k1.matrix(tri, N, V[:, None, None] * loc[None, :, :])


def logdet_halb(A):
    """1/2 log det A fuer regulaeres symmetrisches A: duenne LU mit den Optionen von kugel.gamma_lu, ohne Erdung."""
    t1 = time.time()
    A = A.tocsc()
    A.sort_indices()
    lu = spla.splu(A, permc_spec="MMD_AT_PLUS_A", diag_pivot_thresh=0.0,
                   options={"SymmetricMode": True, "Equil": False})
    d = lu.U.diagonal()
    info = {"sek_lu": time.time() - t1, "nnz_A": int(A.nnz), "nnz_LU": int(lu.L.nnz + lu.U.nnz),
            "min_U": float(np.min(d)), "neg_U": int(np.sum(d < 0)),
            "perm_gleich": bool(np.array_equal(lu.perm_r, lu.perm_c)), "nicht_einbettbar": 0}
    return 0.5 * math.fsum(np.log(np.abs(d)).tolist()), info


def xi_reihe(K, m, Mk, R, VR, N, nicht_einbettbar, xi_werte=XI_WERTE, xi_kons=XI_KONS):
    """Gamma(xi) mit konzentrierter Masse fuer alle xi_werte und mit konsistenter Masse fuer xi_kons."""
    Md = sp.diags(m).tocsc()
    reihe = []
    for xi in xi_werte:
        g, info = logdet_halb(K + (xi * R) * Md)
        info["nicht_einbettbar"] = nicht_einbettbar
        z = 0.5 * math.log(xi * R * VR / N)
        reihe.append({"xi": xi, "gamma": g, "nullmode": z, "gamma_tilde": g - z, "lu": info})
    kons = None
    if xi_kons is not None:
        g, info = logdet_halb(K + (xi_kons * R) * Mk)
        info["nicht_einbettbar"] = nicht_einbettbar
        z = 0.5 * math.log(xi_kons * R * VR / N)
        kons = {"xi": xi_kons, "gamma": g, "nullmode": z, "gamma_tilde": g - z, "lu": info}
    return reihe, kons


def form_pruefung(g0, reihe, kons):
    """Exakte Eigenschaften [M]: Gamma~(xi) - Gamma(0) = 1/2 Summe' ln(1 + xi R/mu_k) ist streng steigend und streng
    konkav in xi; die xi-Werte sind gleichabstaendig (0, 1/12, 2/12, 3/12). Nur Wahrheitswerte (blind tauglich)."""
    w = [g0] + [r["gamma_tilde"] for r in reihe]
    d = [w[i + 1] - w[i] for i in range(len(w) - 1)]
    out = {"monoton": bool(all(x > 0 for x in d)), "konkav": bool(all(d[i + 1] < d[i] for i in range(len(d) - 1)))}
    if kons is not None:
        out["kons_monoton"] = bool(kons["gamma_tilde"] > g0)
    return out


# ---------------------------------------------------------------------- eine Messung (Saat, N)
def eine_messung(N, saat, protokoll):
    n = N_DIM
    t0 = time.time()
    kn = k1.kugelnetz(n, N, saat)
    tri = kn["tri"]
    V_K = kn["geo"]["V_K"]
    a = kn["geo"]["a"]
    sqQ, qinfo = q_laengen(kn)
    e0 = k1.auswerten(tri, N, n, sqQ, V_K, dicht=True)        # Gamma_Q(0) wie kugel2 (Regel Q)
    K = e0.pop("_K", None)
    m = e0.pop("_m", None)
    R = n * (n - 1) / a ** 2
    pr = kn["pruefung"]
    kg = k1.kugel_gueltig(pr, n)
    rec = {"n": n, "N": N, "saat": saat}
    lu_ok = {"0": k1.lu_ok(e0["lu"])}
    masse = {"R": R, "R_mal_a2": R * a * a}
    reihe, kons, form = [], None, {}
    if K is not None:
        _, V, _, _ = k1.p1(sqQ, n)
        VR = e0["V"]
        Mk = masse_konsistent(tri, N, V)
        zs = np.asarray(Mk.sum(axis=1)).ravel()
        masse.update({"V_R": VR, "summe_m_rel": abs(math.fsum(m.tolist()) / VR - 1.0),
                      "Mk_zeilensumme_rel": float(np.max(np.abs(zs - m)) / np.max(m)),
                      "Mk_summe_rel": abs(math.fsum(zs.tolist()) / VR - 1.0), "m_min": float(m.min()),
                      "m_max": float(m.max())})
        reihe, kons = xi_reihe(K, m, Mk, R, VR, N, e0["nicht_einbettbar"])
        for nm, r in zip(XI_NAMEN, reihe):
            lu_ok[nm] = k1.lu_ok(r["lu"])
        lu_ok["kons"] = k1.lu_ok(kons["lu"])
        form = form_pruefung(e0["gamma"], reihe, kons)
        del K, Mk
    gueltig = bool(kg and len(lu_ok) == 5 and all(lu_ok.values()))
    rec.update({"kugel": {"geo": kn["geo"], "pruefung": pr, "gueltig": kg, "Q0": e0, "xi": reihe, "xi_kons": kons,
                          "masse": masse, "Q_quadratur": qinfo},
                "lu_ok": lu_ok, "gueltig": gueltig, "form": form,
                "sekunden": time.time() - t0, "rss_mb": k1.rss_mb()})
    lus = " ".join(f"{r['xi']:.4f} {r['lu']['sek_lu']:.1f}" for r in reihe)
    protokoll(f"N={N} saat={saat}: gueltig {gueltig} (Kugel {kg}, LU {lu_ok}); F {pr['F']}, V_Q5/V_K "
              f"{qinfo['V_Q5'] / V_K:.7f}, R a^2 {masse['R_mal_a2']:.12f}, Masse-Proben "
              f"{masse.get('summe_m_rel', -1):.1e}/{masse.get('Mk_zeilensumme_rel', -1):.1e}; Form {form}; LU 0 "
              f"{e0['lu'].get('sek_lu', -1):.1f}, {lus}, kons {(kons['lu']['sek_lu'] if kons else -1.0):.1f} s; gesamt "
              f"{rec['sekunden']:.1f} s, RSS {k1.rss_mb():.0f} MB")
    return rec


def modus_messung(Nlist, saat0, anzahl, blind, protokoll, out, ziel):
    out.update({"n": N_DIM, "Nlist": Nlist, "saat0": saat0, "anzahl": anzahl, "blind": blind,
                "xi_werte": [0.0] + list(XI_WERTE), "xi_kons": XI_KONS, "messungen": []})
    for saat in range(saat0, saat0 + anzahl):
        for N in Nlist:
            rec = eine_messung(N, saat, protokoll)
            if blind:
                for d in [rec["kugel"]["Q0"]] + list(rec["kugel"]["xi"]) + (
                        [rec["kugel"]["xi_kons"]] if rec["kugel"]["xi_kons"] else []):
                    for q in MESSWERTE:
                        d.pop(q, None)
            out["messungen"].append(rec)
            k1.speichern(ziel, out)
    return out


# ---------------------------------------------------------------------- Kontrollen
def modus_kontrolle(protokoll, out, ziel):
    n = N_DIM
    N = 400
    # (KX0) Regel Q gegen kugel2.eine_messung (Saat 990, N = 400): Gamma_Q(0) bitgleich, obwohl dort vorher C und S
    rec2 = k2.eine_messung(N, 990, lambda s: None)
    kn = k1.kugelnetz(n, N, 990)
    tri, a, V_K = kn["tri"], kn["geo"]["a"], kn["geo"]["V_K"]
    sqQ, _ = q_laengen(kn)
    e0 = k1.auswerten(tri, N, n, sqQ, V_K, dicht=True)
    K, m = e0.pop("_K"), e0.pop("_m")
    q2 = rec2["kugel"]["regeln"]["Q"]
    out["KX0_regel_Q_gegen_kugel2"] = {f: {"gleich": bool(e0[f] == q2[f]), "abw": abs(e0[f] - q2[f])}
                                       for f in ("gamma", "gamma_M", "sum_log_m", "V", "korr", "lam_min")}
    protokoll(f"KX0: {out['KX0_regel_Q_gegen_kugel2']}")
    k1.speichern(ziel, out)
    # (KX1, KX2) duenne LU gegen dicht (slogdet), exakte Nullmoden-Identitaet gegen verallgemeinerte Eigenwerte
    R = n * (n - 1) / a ** 2
    _, V, _, _ = k1.p1(sqQ, n)
    VR = e0["V"]
    Mk = masse_konsistent(tri, N, V)
    Kd, Md, Mkd = K.toarray(), np.diag(m), Mk.toarray()
    mu = np.sort(sla.eigh(Kd, Md, eigvals_only=True))
    muk = np.sort(sla.eigh(Kd, Mkd, eigvals_only=True))
    reihe, kons = xi_reihe(K, m, Mk, R, VR, N, 0)
    kx = []
    for r, Mx, mux, art in [(x, Md, mu, "konzentriert") for x in reihe] + [(kons, Mkd, muk, "konsistent")]:
        xi = r["xi"]
        sgn, ld = np.linalg.slogdet(Kd + xi * R * Mx)
        ident = 0.5 * math.fsum(np.log1p(xi * R / mux[1:]).tolist())
        kx.append({"xi": xi, "masse": art, "lu_ok": k1.lu_ok(r["lu"]), "abw_dicht": abs(r["gamma"] - 0.5 * ld),
                   "vorzeichen": float(sgn), "abw_identitaet": abs((r["gamma_tilde"] - e0["gamma"]) - ident),
                   "mu0": float(mux[0]), "mu1": float(mux[1]), "xiR": xi * R})
        protokoll(f"KX1/KX2 {art} xi={xi:.4f}: {kx[-1]}")
    out["KX1_KX2"] = kx
    out["KX3_form"] = form_pruefung(e0["gamma"], reihe, kons)
    # (KX4) Grenzwert xi -> 0 und Negativprobe ohne Nullmoden-Abzug
    rg, _ = xi_reihe(K, m, Mk, R, VR, N, 0, xi_werte=(1e-9,), xi_kons=None)
    out["KX4_grenzwert"] = {"xi": 1e-9, "abw_mit_abzug": abs(rg[0]["gamma_tilde"] - e0["gamma"]),
                            "abw_ohne_abzug": abs(rg[0]["gamma"] - e0["gamma"]), "nullmode": rg[0]["nullmode"]}
    protokoll(f"KX3: {out['KX3_form']}; KX4: {out['KX4_grenzwert']}")
    # (KX5) Massen: Summe m = V_R, Zeilensumme Mk = m, 1^T Mk 1 = V_R
    zs = np.asarray(Mk.sum(axis=1)).ravel()
    out["KX5_masse"] = {"summe_m_rel": abs(math.fsum(m.tolist()) / VR - 1.0),
                        "Mk_zeilensumme_rel": float(np.max(np.abs(zs - m)) / np.max(m)),
                        "Mk_summe_rel": abs(math.fsum(zs.tolist()) / VR - 1.0), "R_mal_a2": R * a * a,
                        "Mk_symmetrisch": float(abs(Mk - Mk.T).max()), "Mk_min_eigen": float(np.linalg.eigvalsh(Mkd)[0])}
    protokoll(f"KX5: {out['KX5_masse']}")
    k1.speichern(ziel, out)
    # (KX6) Skalierung: Laengen mal lam, a mal lam: Gamma~(xi) - Gamma(0) unveraendert (dimensionslos m^2 a^2 = 12 xi)
    lam = 1.37
    e2 = k1.auswerten(tri, N, n, sqQ * lam ** 2, V_K, dicht=True)
    K2, m2 = e2.pop("_K"), e2.pop("_m")
    _, V2, _, _ = k1.p1(sqQ * lam ** 2, n)
    R2 = n * (n - 1) / (lam * a) ** 2
    reihe2, kons2 = xi_reihe(K2, m2, masse_konsistent(tri, N, V2), R2, e2["V"], N, 0)
    out["KX6_skalierung"] = {
        "max_abw": max(abs((r2["gamma_tilde"] - e2["gamma"]) - (r1["gamma_tilde"] - e0["gamma"]))
                       for r1, r2 in zip(reihe + [kons], reihe2 + [kons2])),
        "gamma0_verschiebung_abw": abs(e2["gamma"] - e0["gamma"] - (N - 1) * math.log(lam))}
    protokoll(f"KX6: {out['KX6_skalierung']}")
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
