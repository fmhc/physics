#!/usr/bin/env python3
# KAC-DIAMANT-WICK-1: 8x8-Kac-Erzeuger auf Finns Diamantnetz, reell und Wick-rotiert nach Ghose (2609.29248, Gl. 66-77).
# Aufruf (nur auf der .69 ueber kleintest.sh): python kac_wick.py rauch|haupt <ausgabe.json>
# Einheiten: c = lambda = hbar = 1, Bindungslaenge l = c/lambda = 1. Regeln und Schwellen: PLAN.md Abschn. 5.
import sys
import json
import time
import platform
import numpy as np

C = 1.0
LAM = 1.0
E4 = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float) / np.sqrt(3.0)
J4 = np.ones((4, 4))
I4 = np.eye(4)
I8 = np.eye(8)
REGELN = {"gleich": (J4 / 4.0, 0.0), "ohne_rueck": ((J4 - I4) / 3.0, -1.0 / 3.0)}
KARTE_K = [0.0125, 0.025, 0.05, 0.1]
K_FORM = [0.0125, 0.025, 0.05]          # Formrest bis zum Auswertepunkt 0,05 (PLAN 5)
K_A = 0.05 * np.sqrt(3.0) / 4.0          # 0,05 in Einheiten der kubischen Konstante (beschreibend)
SCHWELLE = 2.8e-3                        # Eichung QCA-TETRA-1
# Schreibtischwerte (PLAN 3.1, 3.4), vor der Rechnung gebunden
NIVEAUS_REELL = {"gleich": [0, -2, -1, -1, -1, -1, -1, -1],
                 "ohne_rueck": [0, -2, -2 / 3, -2 / 3, -2 / 3, -4 / 3, -4 / 3, -4 / 3]}
M_SCHREIB = {"gleich": 1.5, "ohne_rueck": 1.0}
D_SCHREIB = {"gleich": 1.0 / 3.0, "ohne_rueck": 0.5}
CEFF_SCHREIB = {"gleich": np.sqrt(2.0 / 3.0), "ohne_rueck": 1.0}


def mischmatrix(P):
    Z = np.zeros((4, 4))
    return np.block([[Z, P], [P, Z]])


def diag_transport(kvecs):
    kvecs = np.atleast_2d(kvecs)
    u = C * kvecs @ E4.T
    return np.concatenate([u, -u], axis=1)          # (N, 8), Zustand (A,i): +c e_i.k, (B,i): -c e_i.k


def batch(kvecs, M, art):
    d = diag_transport(kvecs)
    N = d.shape[0]
    ar = np.arange(8)
    if art == "wick":       # Ghose: H = T(k) + lambda (I - M)
        H = np.broadcast_to(LAM * (I8 - M), (N, 8, 8)).astype(complex if np.iscomplexobj(d) else float).copy()
        H[:, ar, ar] += d
        return H
    if art == "reell":      # Kac: G = -i T(k) + lambda (M - I)
        G = np.broadcast_to(LAM * (M - I8), (N, 8, 8)).astype(complex).copy()
        G[:, ar, ar] += -1j * d
        return G
    if art == "gjks":       # Nebenarm: t, v reell, Rate lambda -> i lambda, H = i G
        G = np.broadcast_to((1j * LAM) * (M - I8), (N, 8, 8)).astype(complex).copy()
        G[:, ar, ar] += -1j * d
        return 1j * G
    raise ValueError(art)


def fib_dirs(n):  # woertlich aus qca-tetra-1/code/qca_tetra.py
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], -1)


LAT26 = np.array([[i, j, k] for i in (-1, 0, 1) for j in (-1, 0, 1) for k in (-1, 0, 1) if (i, j, k) != (0, 0, 0)], float)
LAT26_TYP = ["1" + "1" * (int(np.count_nonzero(v)) - 1) + "0" * (3 - int(np.count_nonzero(v))) for v in LAT26]
LAT26 /= np.linalg.norm(LAT26, axis=1)[:, None]
_z = np.random.default_rng(20261005).normal(size=(400, 3))
RAND400 = _z / np.linalg.norm(_z, axis=1)[:, None]
KARTE_DIRS = np.concatenate([LAT26, RAND400])      # 426: Formtest, KW3
FIB400 = fib_dirs(400)                              # Streuung wie QCA-TETRA-1
ALLE = np.concatenate([KARTE_DIRS, FIB400])         # 826
N_KARTE = len(KARTE_DIRS)


def wick_baender(dirs, ks, M, art="wick"):
    kv = (np.asarray(ks)[None, :, None] * dirs[:, None, :]).reshape(-1, 3)
    H = batch(kv, M, art)
    if art == "gjks":
        H = H.real if np.abs(H.imag).max() == 0 else H
    E = np.linalg.eigvalsh(H)
    return E.reshape(len(dirs), len(ks), 8)


def reell_eig(dirs, ks, M):
    kv = (np.asarray(ks)[None, :, None] * dirs[:, None, :]).reshape(-1, 3)
    w = np.linalg.eigvals(batch(kv, M, "reell"))
    idx = np.argsort(-w.real, axis=1, kind="stable")
    w = np.take_along_axis(w, idx, axis=1)
    return w.reshape(len(dirs), len(ks), 8)         # w[..., 0] langsam (aus 0), w[..., 7] schnell (aus -2)


def paar_kennzahlen(E, lev, ks, i, j, telegraph=False):
    """Fitregel PLAN 5 fuer ein Paar (i < j) ueber alle Richtungen. E: (ndir, nk, 8), lev: (8,) bei k = 0."""
    ks = np.asarray(ks)
    if telegraph:   # reell: g = -E0 -+ Wurzel(Delta^2 - c^2 k^2); i = langsam, j = schnell
        E0 = -(lev[i] + lev[j]) / 2
        De = (lev[i] - lev[j]) / 2
        m = -(E[..., i] + E[..., j]) / 2
        h = (E[..., i] - E[..., j]) / 2
        cl2 = (De ** 2 - h ** 2) / ks ** 2
    else:
        E0 = (lev[i] + lev[j]) / 2
        De = (lev[j] - lev[i]) / 2
        m = (E[..., i] + E[..., j]) / 2
        h = (E[..., j] - E[..., i]) / 2
        cl2 = (h ** 2 - De ** 2) / ks ** 2
    im_max = float(np.max(np.abs(np.imag(cl2)))) if np.iscomplexobj(cl2) else 0.0
    cl2r = np.real(cl2)
    k1 = list(ks).index(0.0125)
    k2 = list(ks).index(0.025)
    ce2 = (4 * cl2r[:, k1] - cl2r[:, k2]) / 3
    pos = (cl2r > 0).all(axis=1) & (ce2 > 0)
    ce = np.sqrt(np.where(ce2 > 0, ce2, np.nan))
    cl = np.sqrt(np.where(cl2r > 0, cl2r, np.nan))
    fc = np.abs(cl - ce[:, None]) / ce[:, None]
    fm = np.abs(np.real(m) - np.real(E0)) / (ce[:, None] * ks[None, :])
    fr = np.maximum(fc, fm)
    kf = [list(ks).index(k) for k in K_FORM]
    formrest = np.nanmax(fr[:, kf], axis=1)
    formrest = np.where(pos, formrest, np.inf)
    formrest_01 = np.where(pos, fr[:, list(ks).index(0.1)], np.inf)
    # strenge Nebenlesart: exakte Form bei allen vier Kartenwerten (cl2 - ce2 = (h^2 - Delta^2)/k^2 - ce2)
    rest_exakt = np.abs(cl2 - ce2[:, None]) * ks[None, :] ** 2
    streng = pos & (rest_exakt <= 1e-9 * np.abs(ce2[:, None]) * ks[None, :] ** 2).all(axis=1) \
        & (np.abs(m - E0) <= 1e-12).all(axis=1)
    k5 = list(ks).index(0.05)
    v = cl[:, k5]
    return {"E0": float(np.real(E0)), "Delta": float(np.real(De)), "ce2": ce2, "ce": ce, "pos": pos,
            "formrest": formrest, "formrest_01": formrest_01, "v005": v, "streng": streng, "im_max": im_max}


def streuung(v):
    v = np.asarray(v)
    if not np.all(np.isfinite(v)):
        return {"std_rel": float("inf"), "spann_rel": float("inf"), "mittel": float("nan")}
    return {"std_rel": float(v.std() / v.mean()), "spann_rel": float((v.max() - v.min()) / v.mean()), "mittel": float(v.mean())}


def D_stoerung(M, dirs):
    """exakter k^2-Koeffizient des langsamen reellen Zweigs: D(n) = u0^T T(n) (-G0)^+ T(n) u0."""
    G0 = LAM * (M - I8)
    w, V = np.linalg.eigh(G0)
    i0 = int(np.argmax(w))
    R = np.zeros((8, 8))
    for mm in range(8):
        if mm != i0:
            R += np.outer(V[:, mm], V[:, mm]) / (-w[mm])
    u0 = V[:, i0]
    d = diag_transport(dirs)                 # (ndir, 8)
    Tu = d * u0[None, :]
    return np.einsum("ni,ij,nj->n", Tu, R, Tu), float(w[i0])


def analytisch(p, k):
    """Schreibtischformeln PLAN 3.3 (c = lambda = 1), sortiert."""
    a = np.sqrt((1 + p) ** 2 / 4 + k ** 2 / 3)
    b100 = [(1 + p) / 2 - a, (1 + p) / 2 + a, (3 - p) / 2 - a, (3 - p) / 2 + a,
            1 - np.sqrt(p ** 2 + k ** 2 / 3), 1 - np.sqrt(p ** 2 + k ** 2 / 3),
            1 + np.sqrt(p ** 2 + k ** 2 / 3), 1 + np.sqrt(p ** 2 + k ** 2 / 3)]
    B = 1 + p ** 2 + 10 * k ** 2 / 9
    Cc = (p + k ** 2 / 3) ** 2 + 4 * k ** 2 / 9
    x1 = (B + np.sqrt(B ** 2 - 4 * Cc)) / 2
    x2 = (B - np.sqrt(B ** 2 - 4 * Cc)) / 2
    t = np.sqrt(p ** 2 + k ** 2 / 9)
    b111 = [1 - np.sqrt(x1), 1 + np.sqrt(x1), 1 - np.sqrt(x2), 1 + np.sqrt(x2), 1 - t, 1 - t, 1 + t, 1 + t]
    return np.sort(b100), np.sort(b111)


def regel_auswerten(name, P, p, ausgabe_paare=True):
    M = mischmatrix(P)
    out = {"regel": name, "p_triplett": p}
    # --- Kontrollen ---
    lev_r = np.sort(np.linalg.eigvalsh(LAM * (M - I8)))
    lev_w = np.sort(np.linalg.eigvalsh(LAM * (I8 - M)))
    soll_r = np.sort(np.array(NIVEAUS_REELL[name]))
    out["niveaus_reell"] = lev_r.tolist()
    out["niveaus_wick"] = lev_w.tolist()
    out["niveaus_abw_reell"] = float(np.max(np.abs(lev_r - soll_r)))
    out["niveaus_abw_wick"] = float(np.max(np.abs(lev_w - np.sort(-soll_r))))
    ks = np.array(KARTE_K + [K_A, 1.0])
    Ew = wick_baender(ALLE, ks, M)                       # (826, 6, 8)
    Eg = wick_baender(ALLE, ks, M, art="gjks")
    out["gjks_gegen_wick_max"] = float(np.max(np.abs(Eg - Ew)))
    out["chiral_max"] = float(np.max(np.abs(Ew + Ew[..., ::-1] - 2 * LAM)))
    # H(k) = -G(-i k)
    kv = (0.05 * ALLE)
    Hk = batch(kv, M, "wick")
    Gm = batch(-1j * kv.astype(complex), M, "reell")
    out["identitaet_H_gleich_minus_G_von_minus_ik"] = float(np.max(np.abs(Hk + Gm)))
    # analytische Formeln [100], [111]
    abw = 0.0
    for kk in KARTE_K + [1.0, 3.0]:
        a100, a111 = analytisch(p, kk)
        n100 = np.linalg.eigvalsh(batch(kk * np.array([[1.0, 0, 0]]), M, "wick")[0])
        n111 = np.linalg.eigvalsh(batch(kk * np.array([[1.0, 1, 1]]) / np.sqrt(3), M, "wick")[0])
        abw = max(abw, float(np.max(np.abs(n100 - a100))), float(np.max(np.abs(n111 - a111))))
    out["analytisch_100_111_max"] = abw
    # --- KW0: k^2-Koeffizient des diffusiven Zweigs ---
    Dn, w0 = D_stoerung(M, ALLE)
    out["D_stoerung"] = {"mittel": float(Dn.mean()), "spann_rel": float((Dn.max() - Dn.min()) / Dn.mean()),
                         "abw_schreib": float(np.max(np.abs(Dn - D_SCHREIB[name]))), "w0": w0}
    wr = reell_eig(ALLE, KARTE_K, M)
    d1 = -np.real(wr[:, 0, 0]) / KARTE_K[0] ** 2
    d2 = -np.real(wr[:, 1, 0]) / KARTE_K[1] ** 2
    Dr = (4 * d1 - d2) / 3
    out["D_richardson_reell"] = {"mittel": float(Dr.mean()), "spann_rel": float((Dr.max() - Dr.min()) / Dr.mean()),
                                 "abw_stoerung_max": float(np.max(np.abs(Dr - Dn))),
                                 "im_langsam_max": float(np.max(np.abs(np.imag(wr[:, :, 0]))))}
    e1a = -Ew[:, 0, 0] / KARTE_K[0] ** 2
    e1b = -Ew[:, 1, 0] / KARTE_K[1] ** 2
    Dw = (4 * e1a - e1b) / 3
    out["D_wick_kruemmung"] = {"mittel": float(Dw.mean()), "abw_stoerung_max": float(np.max(np.abs(Dw - Dn)))}
    # --- Paare, Wick ---
    lev0 = np.linalg.eigvalsh(LAM * (I8 - M))
    Ek = Ew[:, :4, :]                                      # nur Kartenwerte
    paare = []
    for i in range(8):
        for j in range(i + 1, 8):
            r = paar_kennzahlen(Ek, lev0, KARTE_K, i, j)
            karte = slice(0, N_KARTE)
            fib = slice(N_KARTE, None)
            form_ok = bool(np.all(r["pos"][karte]) and np.all(r["formrest"][karte] <= SCHWELLE))
            pos_all = bool(np.all(r["pos"]))
            s_fib = streuung(r["v005"][fib]) if pos_all else streuung([np.inf])
            s_karte = streuung(r["v005"][karte]) if pos_all else streuung([np.inf])
            fr_k = r["formrest"][karte]
            eintrag = {"paar": [i + 1, j + 1], "E0": r["E0"], "Delta": r["Delta"],
                       "c_eff_mittel": float(np.nanmean(r["ce"])) if np.any(np.isfinite(r["ce"])) else None,
                       "c_eff_spann_rel": float((np.nanmax(r["ce"]) - np.nanmin(r["ce"])) / np.nanmean(r["ce"])) if np.any(np.isfinite(r["ce"])) else None,
                       "formrest_max_karte": float(np.max(fr_k)), "formrest_01_max_karte": float(np.max(r["formrest_01"][karte])),
                       "form_ok": form_ok, "pos_alle": pos_all,
                       "streuung_fib": s_fib, "streuung_karte": s_karte,
                       "streng_richtungen": int(np.sum(r["streng"][karte])),
                       "streng_100_110_111": {t: int(np.sum(r["streng"][:26][[q for q in range(26) if LAT26_TYP[q] == t]]))
                                              for t in ("100", "110", "111")}}
            if [i + 1, j + 1] == [1, 8]:
                m = r["Delta"] / r["ce2"]
                eintrag["m_mittel"] = float(np.mean(m[karte]))
                eintrag["m_abw_rel_max_karte"] = float(np.max(np.abs(m[karte] - M_SCHREIB[name])) / M_SCHREIB[name])
                eintrag["ceff_abw_schreib_max"] = float(np.max(np.abs(r["ce"] - CEFF_SCHREIB[name])))
                # beschreibend: a-Einheit und relativistischer Bereich
                for lab, kk in (("k_a", K_A), ("k_1", 1.0)):
                    q = list(ks).index(kk)
                    h = (Ew[:, q, 7] - Ew[:, q, 0]) / 2
                    v = np.sqrt(h ** 2 - r["Delta"] ** 2) / kk
                    eintrag["streuung_fib_" + lab] = streuung(v[fib])
                    eintrag["v_" + lab + "_100_110_111"] = [float(v[LAT26_TYP.index(t)]) for t in ("100", "110", "111")]
                # Asymptotik: Grenzgeschwindigkeit bei |k| = 200
                vas = []
                for n in (np.array([1.0, 0, 0]), np.array([1.0, 1, 0]) / np.sqrt(2), np.array([1.0, 1, 1]) / np.sqrt(3)):
                    e = np.linalg.eigvalsh(batch(200.0 * n[None, :], M, "wick")[0])
                    vas.append([float((e[7] - e[0]) / 2 / 200.0), float(np.max(np.abs(E4 @ n)))])
                eintrag["grenzgeschw_100_110_111_numerik_schreib"] = vas
                beta_dirs = {}
                for t in ("100", "110", "111"):
                    q = LAT26_TYP.index(t)
                    beta_dirs[t] = float(((Ek[q, 2, 7] - Ek[q, 2, 0]) ** 2 / 4 - r["Delta"] ** 2 - r["ce2"][q] * 0.05 ** 2) / 0.05 ** 4)
                eintrag["beta_k4_bei_005_100_110_111"] = beta_dirs
            paare.append(eintrag)
    ok = [q for q in paare if q["form_ok"] and q["pos_alle"]]
    if ok:
        best = min(ok, key=lambda q: q["streuung_fib"]["std_rel"])
        best_markiert = False
    else:
        cand = [q for q in paare if q["pos_alle"]]
        best = min(cand, key=lambda q: q["streuung_fib"]["std_rel"]) if cand else None
        best_markiert = True
    out["paare_wick"] = paare if ausgabe_paare else None
    out["bestes_paar_wick"] = best
    out["bestes_paar_form_verfehlt"] = best_markiert
    out["paare_form_ok"] = [q["paar"] for q in ok]
    # --- reelle Fassung: aeusseres Paar (langsam, schnell) ---
    wr4 = reell_eig(ALLE, KARTE_K, M)
    levr = reell_eig(np.array([[1.0, 0, 0]]), [0.0], M)[0, 0]
    r = paar_kennzahlen(wr4, levr, KARTE_K, 0, 7, telegraph=True)
    karte = slice(0, N_KARTE)
    fib = slice(N_KARTE, None)
    out["reell_aeusseres_paar"] = {"E0": r["E0"], "Delta": r["Delta"], "c_eff_mittel": float(np.nanmean(r["ce"])),
                                   "formrest_max_karte": float(np.max(r["formrest"][karte])),
                                   "formrest_01_max_karte": float(np.max(r["formrest_01"][karte])),
                                   "form_ok": bool(np.all(r["pos"][karte]) and np.all(r["formrest"][karte] <= SCHWELLE)),
                                   "streuung_fib": streuung(r["v005"][fib]), "streuung_karte": streuung(r["v005"][karte]),
                                   "im_max_cl2": r["im_max"], "im_max_eig": float(np.max(np.abs(np.imag(wr4[:, :, [0, 7]])))),
                                   "m_mittel": float(np.mean(r["Delta"] / r["ce2"][karte])),
                                   "streng_richtungen": int(np.sum(r["streng"][karte]))}
    return out


def urteile(res):
    u = {}
    kw0 = all(res[n]["niveaus_abw_reell"] <= 1e-12 and res[n]["niveaus_abw_wick"] <= 1e-12
              and res[n]["D_stoerung"]["spann_rel"] < 1e-9 for n in REGELN)
    u["KW0"] = "eingetroffen" if kw0 else "nicht eingetroffen"
    kw1_regeln = [n for n in REGELN if res[n]["bestes_paar_wick"] is not None and not res[n]["bestes_paar_form_verfehlt"]
                  and res[n]["bestes_paar_wick"]["streuung_fib"]["std_rel"] < SCHWELLE]
    u["KW1"] = "eingetroffen" if kw1_regeln else "nicht eingetroffen"
    u["KW1_regeln"] = kw1_regeln
    streng = [n for n in REGELN if any(q["streng_richtungen"] == N_KARTE and q["streuung_fib"]["std_rel"] < SCHWELLE
                                       for q in res[n]["paare_wick"])]
    u["KW1_streng"] = "eingetroffen" if streng else "nicht eingetroffen"
    u["KW1_streng_regeln"] = streng
    sg = res["gleich"]["bestes_paar_wick"]["streuung_fib"]["std_rel"]
    so = res["ohne_rueck"]["bestes_paar_wick"]["streuung_fib"]["std_rel"]
    u["KW2"] = "eingetroffen" if so < sg else "nicht eingetroffen"
    u["KW2_werte"] = {"gleich": sg, "ohne_rueck": so, "verhaeltnis_ohne_durch_gleich": so / sg}
    kw3 = []
    for n in kw1_regeln:
        b = res[n]["bestes_paar_wick"]
        rat = abs(b["Delta"] / LAM - round(b["Delta"] / LAM * 12) / 12) <= 1e-12
        mok = b.get("m_abw_rel_max_karte", np.inf) <= 1e-6
        kw3.append((n, bool(rat), bool(mok)))
    u["KW3"] = ("eingetroffen" if kw3 and all(a and b for _, a, b in kw3) else "nicht eingetroffen") if kw1_regeln else "entfaellt (KW1 nicht eingetroffen)"
    u["KW3_einzeln"] = kw3
    return u


def main():
    global KARTE_DIRS, FIB400, ALLE, N_KARTE
    modus, ziel = sys.argv[1], sys.argv[2]
    t0 = time.time()
    res = {"modus": modus, "python": platform.python_version(), "numpy": np.__version__,
           "start_unix": t0, "einheiten": "c = lambda = hbar = 1, l = c/lambda = 1"}
    if modus == "rauch":
        try:
            import matplotlib
            res["matplotlib"] = matplotlib.__version__
        except Exception as ex:  # nur Umgebungsbericht
            res["matplotlib"] = "fehlt: " + repr(ex)
        for name, (P, p) in REGELN.items():
            M = mischmatrix(P)
            res[name] = {"niveaus_wick": np.linalg.eigvalsh(LAM * (I8 - M)).tolist(),
                         "baender_100_k005": np.linalg.eigvalsh(batch(0.05 * np.array([[1.0, 0, 0]]), M, "wick")[0]).tolist(),
                         "analytisch_100_k005": analytisch(p, 0.05)[0].tolist()}
        res["richtungen"] = {"karte": int(N_KARTE), "fib": int(len(FIB400)), "typen26": {t: LAT26_TYP.count(t) for t in ("100", "110", "111")}}
    elif modus == "rauchhaupt":   # nur Codepfad: 30 + 10 Richtungen, keine Zahlen in die Ausgabe
        KARTE_DIRS, FIB400 = KARTE_DIRS[:30], FIB400[:10]
        ALLE = np.concatenate([KARTE_DIRS, FIB400])
        N_KARTE = len(KARTE_DIRS)
        tmp = {}
        for name, (P, p) in REGELN.items():
            tmp[name] = regel_auswerten(name, P, p)
        urteile(tmp)
        res["codepfad"] = "lief ohne Ausnahme"
        res["schluessel"] = sorted(tmp["gleich"].keys())
    else:
        for name, (P, p) in REGELN.items():
            res[name] = regel_auswerten(name, P, p)
        res["urteile"] = urteile(res)
    res["dauer_s"] = time.time() - t0
    with open(ziel, "w") as f:
        json.dump(res, f, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    print(json.dumps({k: res[k] for k in res if k in ("modus", "numpy", "matplotlib", "dauer_s", "urteile", "richtungen", "codepfad")}, indent=1))


if __name__ == "__main__":
    main()
