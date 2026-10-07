#!/usr/bin/env python3
"""INDUZIERT-1: Auswertekette (Gegenterm, Schur-Komplement, Spin-Projektoren wie REGGE-4D-1), Urteile IN0 bis IN5, Bilder.

Aufruf: python induziert_auswertung.py <datenordner> <aus.json> <bildordner> [probe]
  Erwartet im Datenordner: kontrolle.json, teilA.json, teilB-n4-m<m2>-L<Lq>.json, optional teilB-n3-*.json.
  probe: nur Probe des Auswertecodes (Rauchdaten), keine Urteile zur Karte.
"""
import glob
import json
import os
import sys

import numpy as np
import scipy.linalg as sla

import regge4d

POLYAKOV = -1.0 / (24 * np.pi)
# Schwellen der Karte (unveraendert) und Festlegungen des Plans
IN0_SYMBOL = 1e-12
IN0_HERM = 1e-9
IN1_TOL = 0.03
IN3_ZIEL, IN3_TOL = -2.0, 0.10
IN4_TOL, IN4_BETRAG = 0.05, 0.2
IN5_TOL = 0.10
KONTROLLE_TOL = 1e-5          # PLAN: Torus-Gegenprobe (Blase gegen direkte zweite Differenz)
IN1_L, IN1_N, IN1_RICHTUNG = 1024, 8, "achse_10"
IN2_BETRAEGE = [0.05, 0.1, 0.2]
IN3_BETRAG = 0.05
MASSEN_URTEIL = [0.01, 0.04]
L_HAUPT, L_KONV = 64, 48
PINV_RCOND = 1e-8


def mat(x):
    return np.array(x["re"]) + 1j * np.array(x["im"])


def herm(P):
    return 0.5 * (P + P.conj().T)


def ct_metrik(P0, B):
    """Metrik-Teil von Pi(0): CT = P0 B (B^T P0 B)^-1 B^T P0, also (P0 - CT) B = 0 (PLAN [F4])."""
    X = P0 @ B
    return X @ np.linalg.solve(B.T @ X, X.T)


def komplement(B):
    U, sv, _ = np.linalg.svd(B, full_matrices=True)
    r = int(np.sum(sv > 1e-10 * sv[0]))
    return U[:, r:]


def schur(Pi, B, C):
    Khh = B.T @ Pi @ B
    Khw = B.T @ Pi @ C
    Kww = herm(C.T @ Pi @ C)
    w, U = np.linalg.eigh(Kww)
    keep = np.abs(w) > PINV_RCOND * max(np.max(np.abs(w)), 1e-300)
    Kinv = (U[:, keep] / w[keep]) @ U[:, keep].conj().T
    Ks = herm(Khh - Khw @ Kinv @ Khw.conj().T)
    return Ks, herm(Khh), w


def spin(git, K, k):
    n = git.n
    kn = float(np.linalg.norm(k))
    k2 = kn * kn
    P2, P1, P0s, P0w, svec, wvec = git.projektoren(k / kn)
    r2 = int(round(np.trace(P2)))
    r1 = int(round(np.trace(P1)))
    t2 = np.trace(P2 @ K)
    c2 = float(t2.real / (r2 * k2))
    c1 = float(np.trace(P1 @ K).real / (r1 * k2))
    c0s = float((svec @ K @ svec).real / k2)
    c0w = float((wvec @ K @ wvec).real / k2)
    c0sw = float((svec @ K @ wvec).real / k2)
    w2, U2 = np.linalg.eigh(P2)
    Q2 = U2[:, w2 > 0.5]
    spin2 = np.linalg.eigvalsh(herm(Q2.T @ K @ Q2)) / k2
    nK = np.linalg.norm(K)
    P0 = P0s + P0w
    misch = {"2-1": float(np.linalg.norm(P2 @ K @ P1) / nK), "2-0": float(np.linalg.norm(P2 @ K @ P0) / nK),
             "1-0": float(np.linalg.norm(P1 @ K @ P0) / nK)}
    K_eh = c2 * k2 * (P2 - (n - 2) * P0s)
    dev = float(np.linalg.norm(K - K_eh) / np.linalg.norm(K_eh)) if c2 != 0 else None
    return {"c2": c2, "c1": c1, "c0s": c0s, "c0w": c0w, "c0sw": c0sw,
            "r": c0s / c2 if c2 != 0 else None, "spin2": spin2.tolist(), "mischung": misch,
            "abw_EH_normiert": dev, "imag_tr_P2K": float(abs(t2.imag) / (r2 * k2)),
            "eig_K_durch_k2": (np.linalg.eigvalsh(K) / k2).tolist()}, Q2


def rayleigh(Pi, Vs, W):
    """Verallgemeinerte Eigenwerte von (Vs^+ Pi Vs, Vs^+ W Vs)."""
    A = herm(Vs.conj().T @ Pi @ Vs)
    M = herm(Vs.conj().T @ W @ Vs).real
    return sla.eigh(A, M, eigvals_only=True)


def kette_datei(d):
    n = d["n"]
    git = regge4d.Gitter(n, 3)
    dirs = np.array(d["dirs"])
    assert np.array_equal(dirs, git.dirs), "Kantenreihenfolge weicht von regge4d ab"
    B = git.B0()
    s0 = np.array(d["s0"])
    Gp = np.array(d["Gamma_strich"])
    nE = len(s0)
    p0 = [p for p in d["punkte"] if p["betrag_nominal"] == 0.0][0]
    P0 = herm(mat(p0["Pi_base"])).real
    V20 = herm(mat(p0["V2_base"])).real
    CT = ct_metrik(P0, B)
    J = np.diag(2 * np.sqrt(s0))
    Jinv = np.linalg.inv(J)
    Tad = np.diag(2 * Gp)
    P0l = J @ P0 @ J + Tad
    Bl = Jinv @ B
    CTl = ct_metrik(P0l, Bl)
    C = komplement(B)
    Cl = komplement(Bl)
    W_l = np.diag(1.0 / (4 * s0))     # |delta l|^2 = sum |delta s|^2/(4 s)
    W_s = np.eye(nE)
    # k = 0: Vakuumteil gegen Volumen
    A = B.T @ P0 @ B
    Vm = B.T @ V20 @ B
    alpha = float(np.sum(A * Vm) / np.sum(Vm * Vm))
    in5 = {"alpha": alpha, "rel_frob_rest": float(np.linalg.norm(A - alpha * Vm) / np.linalg.norm(A)),
           "eig_B0T_Pi0_B0": np.linalg.eigvalsh(A).tolist(), "eig_B0T_V2_B0": np.linalg.eigvalsh(Vm).tolist()}
    S0, _, _ = schur(P0.astype(complex), B, C)
    S0 = S0.real
    a2 = float(np.sum(S0 * Vm) / np.sum(Vm * Vm))
    in5["schur_alpha"] = a2
    in5["schur_rel_frob_rest"] = float(np.linalg.norm(S0 - a2 * Vm) / np.linalg.norm(S0))
    a3 = float(np.sum(P0 * V20) / np.sum(V20 * V20))
    in5["voll15_rel_frob_rest"] = float(np.linalg.norm(P0 - a3 * V20) / np.linalg.norm(P0))
    # Vakuumspannung (Tadpole) in h: T = B^T Gamma'
    T = B.T @ Gp
    Tv = B.T @ np.array(d["V_strich"])
    basis, namen = git.sym_basis()
    Tmat = sum(t * X for t, X in zip(T, basis))
    in5["vakuumspannung_h"] = dict(zip(namen, T.tolist()))
    in5["vakuumspannung_eig"] = np.linalg.eigvalsh(Tmat).tolist()
    in5["volumen_erste_ableitung_h"] = dict(zip(namen, Tv.tolist()))
    in5["eig_Pi0_15"] = np.linalg.eigvalsh(P0).tolist()
    in5["eig_Pi0_minus_CT_15"] = np.linalg.eigvalsh(P0 - CT).tolist()
    res = []
    for p in d["punkte"]:
        if p["betrag_nominal"] == 0.0:
            continue
        k = np.array(p["k"])
        Pb = mat(p["Pi_base"])
        ph = np.exp(1j * (dirs @ k) / 2)
        Pm = herm(np.conj(ph)[:, None] * Pb * ph[None, :])
        phi = 0.5 * (dirs @ k)[None, :] - 0.5 * (dirs @ k)[:, None]
        cosf, expf = np.cos(phi), np.exp(1j * phi)
        V2m = herm(np.conj(ph)[:, None] * mat(p["V2_base"]) * ph[None, :])
        var = {
            "P": (Pm - CT * cosf, B, C, W_l),
            "R1_mitte": (Pm - CT, B, C, W_l),
            "R2_fusspunkt": (Pm - CT * expf, B, C, W_l),
            "G_ganz": (Pm - P0 * cosf, B, C, W_l),
            "U_roh": (Pm, B, C, W_l),
            "L_laengen": (J @ Pm @ J + Tad - CTl * cosf, Bl, Cl, np.eye(nE)),
        }
        eintrag = {"richtung": p["richtung"], "betrag": p["betrag_nominal"], "k": p["k"],
                   "herm_rel": p["herm_rel"], "mid_imag_rel": float(np.max(np.abs(Pm.imag)) / np.max(np.abs(Pm)))}
        Gb = git.eich_basis(k).astype(complex)
        for name, (Ps, Bv, Cv, W) in var.items():
            Ks, Kd, ww = schur(Ps, Bv, Cv)
            sp, Q2 = spin(git, Ks, k)
            spd, _ = spin(git, Kd, k)
            # Eichmoden und Spin 2 im vollen Kantenraum, je Einheit Kantenlaengen-Aenderung (W)
            if name == "L_laengen":
                Gv = Jinv @ Gb          # delta l = delta s/(2 l)
            else:
                Gv = Gb
            S2 = (Bv @ Q2).astype(complex)
            kg_ = rayleigh(Ps, Gv, W)
            k2_ = rayleigh(Ps, S2, W)
            kg_s = rayleigh(Ps, Gv, np.eye(nE) if name != "L_laengen" else np.diag(4 * s0))
            k2_s = rayleigh(Ps, S2, np.eye(nE) if name != "L_laengen" else np.diag(4 * s0))
            kap2 = float(np.mean(k2_))
            eintrag[name] = {
                "schur": sp, "direkt": {"c2": spd["c2"], "r": spd["r"], "c0s": spd["c0s"]},
                "Kww_eig": ww.real.tolist(),
                "eich_l": kg_.tolist(), "spin2_l": k2_.tolist(), "kappa2_l": kap2,
                "eich_verhaeltnis_l": float(np.max(np.abs(kg_)) / kap2) if kap2 > 0 else None,
                "eich_s": kg_s.tolist(), "spin2_s": k2_s.tolist(),
                "eich_verhaeltnis_s": float(np.max(np.abs(kg_s)) / np.mean(k2_s)) if np.mean(k2_s) > 0 else None,
                "eig_Pisub_15": np.linalg.eigvalsh(herm(Ps)).tolist(),
            }
        # Volumen-Hesse (beschreibend): Spin-Struktur der Gitter-Volumenvariation
        Kv, _, _ = schur(V2m - V20 * cosf, B, C)
        spv, _ = spin(git, Kv, k)
        eintrag["volumen_k2_teil"] = {"c2": spv["c2"], "c0s": spv["c0s"]}
        res.append(eintrag)
    return {"n": n, "m2": d["m2"], "Lq": d["Lq"], "in5": in5, "punkte": res,
            "Pi0_metrik_eig": np.linalg.eigvalsh(A).tolist(), "Gamma_strich": Gp.tolist()}


def polyakov_form(phi):
    """K_Pol/k^2 = -(1/(48 pi)) t t^T, t_a = <theta, X_a>, theta = 1 - n n (2D, Basis h00, h11, h01)."""
    c, s = np.cos(phi), np.sin(phi)
    t = np.array([s * s, c * c, -np.sqrt(2.0) * s * c])
    return -np.einsum("a...,b...->ab...", t, t) / (48 * np.pi)


def harmonische_fit(h):
    """4phi-Harmonische der k^2-Form (beschreibend). Polynomiale k^2-Terme (lokal, Gegenterme, Konventionen,
    Fortsetzungen zweiter Ordnung, Massenmatrix) tragen nur die Moden 0 und 2 in phi; die 4phi-Mode bei O(k^2)
    kommt nur aus dem nicht-analytischen, universellen Polyakov-Anteil (k^2 delta - k k)(...)/k^2."""
    pts = h["punkte"]
    phi = np.array([p["phi"] for p in pts])
    kap2 = np.array([p["betrag"] for p in pts]) ** 2
    Y = np.array([p["K2"] for p in pts])
    spalten = [np.ones_like(phi)]
    for m in (2, 4):
        spalten += [np.cos(m * phi), np.sin(m * phi)]
    spalten.append(kap2)
    for m in (2, 4, 6):
        spalten += [kap2 * np.cos(m * phi), kap2 * np.sin(m * phi)]
    X = np.stack(spalten, axis=1)
    eintraege = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
    fein = np.linspace(0, 2 * np.pi, 1440, endpoint=False)
    T = polyakov_form(fein)
    gem, vorh, tab = [], [], {}
    for a, b in eintraege:
        y = Y[:, a, b]
        coef, *_ = np.linalg.lstsq(X, y, rcond=None)
        rest = y - X @ coef
        p4c = float(2 * np.mean(T[a, b] * np.cos(4 * fein)))
        p4s = float(2 * np.mean(T[a, b] * np.sin(4 * fein)))
        gem += [coef[3], coef[4]]
        vorh += [p4c, p4s]
        tab[f"{a}{b}"] = {"mode0": float(coef[0]), "cos2": float(coef[1]), "sin2": float(coef[2]),
                          "cos4": float(coef[3]), "sin4": float(coef[4]), "cos4_polyakov": p4c,
                          "sin4_polyakov": p4s, "rest_rms": float(np.sqrt(np.mean(rest ** 2))),
                          "y_rms": float(np.sqrt(np.mean(y ** 2)))}
    gem, vorh = np.array(gem), np.array(vorh)
    lam = float(gem @ vorh / (vorh @ vorh))
    return {"L": h["L"], "punkte": len(pts), "lambda_polyakov": lam,
            "rel_rest": float(np.linalg.norm(gem - lam * vorh) / np.linalg.norm(gem)),
            "betrag_min_max": [float(np.sqrt(kap2.min())), float(np.sqrt(kap2.max()))], "eintraege": tab,
            "imag_rel_max": float(max(p["imag_rel"] for p in pts))}


def lade(ordner):
    def j(name):
        f = os.path.join(ordner, name)
        if os.path.exists(f):
            with open(f) as fh:
                return json.load(fh)
        return None

    B = {}
    for f in sorted(glob.glob(os.path.join(ordner, "teilB-n*-m*-L*.json"))):
        with open(f) as fh:
            d = json.load(fh)
        B[(d["n"], d["m2"], d["Lq"])] = d
    return j("kontrolle.json"), j("teilA.json"), B


def urteile_B(ketten, L):
    """IN2 bis IN5 auf dem Gitter L (n = 4, Massen MASSEN_URTEIL), Variante 'P' (Plan) und 'R2_fusspunkt'."""
    out = {}
    for var in ("P", "R2_fusspunkt"):
        c2w, rw, ew = {}, {}, {}
        ok2 = ok3 = ok4 = True
        fehl = False
        for m2 in MASSEN_URTEIL:
            kk = ketten.get((4, m2, L))
            if kk is None:
                fehl = True
                continue
            for e in kk["punkte"]:
                s = e[var]["schur"]
                key = f"m2={m2} {e['richtung']} {e['betrag']}"
                if e["betrag"] in IN2_BETRAEGE:
                    c2w[key] = s["c2"]
                    ok2 &= s["c2"] > 0
                if e["betrag"] == IN3_BETRAG:
                    rw[key] = s["r"]
                    ok3 &= (s["r"] is not None) and abs(s["r"] / IN3_ZIEL - 1) <= IN3_TOL
                if e["betrag"] == IN4_BETRAG:
                    v = e[var]["eich_verhaeltnis_l"]
                    ew[key] = {"verhaeltnis": v, "kappa2_l": e[var]["kappa2_l"], "eich_l": e[var]["eich_l"]}
                    ok4 &= (v is not None) and v <= IN4_TOL
        out[var] = {"IN2": None if fehl else ok2, "IN3": None if fehl else ok3, "IN4": None if fehl else ok4,
                    "c2": c2w, "r": rw, "eich": ew}
    ok5 = True
    w5 = {}
    for m2 in MASSEN_URTEIL:
        kk = ketten.get((4, m2, L))
        if kk is None:
            ok5 = None
            break
        w5[f"m2={m2}"] = kk["in5"]
        ok5 &= kk["in5"]["rel_frob_rest"] > IN5_TOL
    out["IN5"] = ok5
    out["IN5_werte"] = w5
    return out


def urteil_text(b):
    return "eingetroffen" if b else "nicht eingetroffen"


def main():
    ordner, ziel, bildordner = sys.argv[1], sys.argv[2], sys.argv[3]
    probe = len(sys.argv) > 4 and sys.argv[4] in ("probe", "probe16")
    if len(sys.argv) > 4 and sys.argv[4] == "probe16":
        # nur Codeprobe der Urteilslogik auf groben Rauchgittern (L_q = 16 statt 64, 12 statt 48)
        global L_HAUPT, L_KONV
        L_HAUPT, L_KONV = 16, 12
    ko, ta, tb = lade(ordner)
    ketten = {key: kette_datei(d) for key, d in tb.items()}
    erg = {"hinweis": "PROBE des Auswertecodes auf Rauchdaten, keine Urteile zur Karte" if probe else
           "Urteile nach PLAN.md Abschnitt 8", "urteile": {}}
    # ---------------- Kontrollen (Gate)
    tor = ko["torus"] if ko else []
    tor_max = max([x.get("rel_abw", x.get("rel_abw_max", 0.0)) for x in tor] + [0.0])
    gate = bool(ko) and tor_max <= KONTROLLE_TOL
    erg["kontrolle"] = {"torus_max_rel_abw": tor_max, "gate_bestanden": gate, "torus": tor,
                        "ableitungen": ko["ableitungen"] if ko else None, "symbol": ko["symbol"] if ko else None}
    # ---------------- IN0
    sym = ko["symbol"]["n4"]["max_abs"] if ko else None
    hm = [p["herm_rel"] for (n, m2, L), d in tb.items() if n == 4 for p in d["punkte"]]
    herm_max = max(hm) if hm else None
    if sym is None or herm_max is None:
        erg["urteile"]["IN0"] = {"urteil": "nicht auswertbar", "werte": {}}
    else:
        erg["urteile"]["IN0"] = {"urteil": urteil_text(sym <= IN0_SYMBOL and herm_max <= IN0_HERM),
                                 "werte": {"symbol_max_abs": sym, "hermitesch_max_rel": herm_max,
                                           "symbol_n2_n3": {k: ko["symbol"][k]["max_abs"] for k in ("n2", "n3")}}}
    # ---------------- IN1
    if ta is None:
        erg["urteile"]["IN1"] = {"urteil": "nicht auswertbar", "werte": {}}
    else:
        tab = []
        for lauf in ta["laeufe"]:
            for p in lauf["punkte"]:
                tab.append({"L": lauf["L"], **{k: p[k] for k in ("richtung", "n", "betrag", "c_P_eckenskalierung",
                                                               "c_l_linear", "c_s_linear", "c_D_mit_mass",
                                                               "herm_rel", "eich_roh_durch_k2", "eich_ct_durch_k2",
                                                               "konform_rayleigh_roh_durch_k2",
                                                               "konform_rayleigh_ct_durch_k2")}})
        sel = [t for t in tab if t["L"] == IN1_L and t["n"] == IN1_N and t["richtung"] == IN1_RICHTUNG]
        if not sel or probe:
            erg["urteile"]["IN1"] = {"urteil": "nicht auswertbar", "werte": {"tabelle": tab}}
        else:
            c = sel[0]["c_P_eckenskalierung"]
            ok = abs(c / POLYAKOV - 1) <= IN1_TOL
            u = urteil_text(ok) if gate else "nicht auswertbar"
            erg["urteile"]["IN1"] = {"urteil": u, "werte": {"c_P": c, "polyakov": POLYAKOV,
                                                            "verhaeltnis": c / POLYAKOV, "punkt": sel[0],
                                                            "tabelle": tab,
                                                            "Gamma_strich_L": {l["L"]: l["Gamma_strich"]
                                                                               for l in ta["laeufe"]}}}
    # ---------------- Teil A2 (beschreibend): universeller Polyakov-Anteil aus der 4phi-Harmonischen
    if ta is not None and "harmonische" in ta:
        erg["teilA2_harmonische"] = [harmonische_fit(h) for h in ta["harmonische"]]
    # ---------------- IN2 bis IN5
    uH = urteile_B(ketten, L_HAUPT)
    uK = urteile_B(ketten, L_KONV)
    for nr in ("IN2", "IN3", "IN4"):
        h, kv = uH["P"][nr], uK["P"][nr]
        hw, kw = uH["R2_fusspunkt"][nr], uK["R2_fusspunkt"][nr]
        if h is None or not gate:
            u = "nicht auswertbar"
            verm = "Daten fehlen" if h is None else "Torus-Gegenprobe nicht bestanden"
        elif kv is not None and kv != h:
            u = "nicht auswertbar"
            verm = f"Gitter L_q = {L_KONV} und {L_HAUPT} geben verschiedene Urteile"
        else:
            u = urteil_text(h)
            verm = None
        werte = {"plan_P": {k: uH["P"][k] for k in ("c2", "r", "eich")}, "kartenwortlaut_R2": urteil_text(hw)
                 if hw is not None else None, "R2_konv_gleich": (kw == hw) if kw is not None else None,
                 "konvergenz_L48_urteil_P": kv}
        erg["urteile"][nr] = {"urteil": u, "werte": werte}
        if verm:
            erg["urteile"][nr]["vermerk"] = verm
    h5, k5 = uH["IN5"], uK["IN5"]
    if h5 is None or not gate:
        erg["urteile"]["IN5"] = {"urteil": "nicht auswertbar", "werte": uH["IN5_werte"]}
    elif k5 is not None and k5 != h5:
        erg["urteile"]["IN5"] = {"urteil": "nicht auswertbar", "werte": uH["IN5_werte"],
                                 "vermerk": "Gitter geben verschiedene Urteile"}
    else:
        erg["urteile"]["IN5"] = {"urteil": urteil_text(h5), "werte": uH["IN5_werte"]}
    if probe:
        for nr in erg["urteile"]:
            erg["urteile"][nr]["urteil"] = "PROBE: " + erg["urteile"][nr]["urteil"]
    # ---------------- beschreibend: alle Ketten
    erg["ketten"] = {f"n{n}-m{m2}-L{L}": v for (n, m2, L), v in ketten.items()}
    # Gitterkonvergenz
    konv = {}
    for (n, m2, L), v in ketten.items():
        if L == L_HAUPT and (n, m2, L_KONV) in ketten:
            w = ketten[(n, m2, L_KONV)]
            dc, dr = 0.0, 0.0
            for a, b in zip(v["punkte"], w["punkte"]):
                assert a["richtung"] == b["richtung"] and a["betrag"] == b["betrag"]
                for var in ("P", "R2_fusspunkt", "G_ganz", "L_laengen", "R1_mitte"):
                    dc = max(dc, abs(a[var]["schur"]["c2"] / b[var]["schur"]["c2"] - 1))
                    if a[var]["schur"]["r"] is not None and b[var]["schur"]["r"]:
                        dr = max(dr, abs(a[var]["schur"]["r"] / b[var]["schur"]["r"] - 1))
            konv[f"n{n}-m{m2}"] = {"max_rel_c2": dc, "max_rel_r": dr}
    erg["gitterkonvergenz_L64_gegen_L48"] = konv
    # Leitungszusatz (beschreibend, nicht geurteilt): Richtungsabhaengigkeit im kleinsten k
    zus = {}
    gruppen = {"achse": ["achse_1000"], "flaeche": ["flaeche_1100", "gegen_1m100"], "raum": ["raum_1110"],
               "hyper": ["hyper_1111"], "uebrige": ["quer_11m1m1", "schief_111m1", "allg_1234"]}
    for (n, m2, L), v in ketten.items():
        if n != 4:
            continue
        for b in (0.025, 0.05):
            pk = [e for e in v["punkte"] if e["betrag"] == b]
            if not pk:
                continue
            for var in ("P", "R2_fusspunkt", "R1_mitte", "G_ganz", "L_laengen", "U_roh"):
                c2 = {e["richtung"]: e[var]["schur"]["c2"] for e in pk}
                r = {e["richtung"]: e[var]["schur"]["r"] for e in pk}
                ac = np.array(list(c2.values()))
                ar = np.array([x for x in r.values() if x is not None])
                eintrag = {"c2": c2, "r": r,
                           "gruppen_c2": {g: [c2[x] for x in xs if x in c2] for g, xs in gruppen.items()},
                           "gruppen_r": {g: [r[x] for x in xs if x in r] for g, xs in gruppen.items()},
                           "c2_spanne_rel": float((ac.max() - ac.min()) / abs(ac.mean())),
                           "c2_std_rel": float(ac.std() / abs(ac.mean()))}
                if len(ar):
                    eintrag["r_spanne_rel"] = float((ar.max() - ar.min()) / abs(ar.mean()))
                    eintrag["r_std_rel"] = float(ar.std() / abs(ar.mean()))
                zus[f"m{m2}-L{L}-k{b}-{var}"] = eintrag
    erg["leitungszusatz_richtungen"] = zus
    with open(ziel, "w") as f:
        json.dump(erg, f, indent=1)
    for nr, v in erg["urteile"].items():
        print(nr, v["urteil"], v.get("vermerk", ""))
    bilder(ta, ketten, bildordner)
    print("Bilder geschrieben")


def bilder(ta, ketten, ordner):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    # Teil A
    if ta is not None:
        fig, axs = plt.subplots(1, 2, figsize=(15, 5.5))
        stile = {"c_P_eckenskalierung": ("-", "P: det' K, Ecken-Skalierung (Plan)"),
                 "c_l_linear": ("-.", "det' K, linear in l"), "c_s_linear": (":", "det' K, linear in s"),
                 "c_D_mit_mass": ("--", "D: det'(M^-1 K), Flaechenterm abgezogen")}
        farben = {256: "tab:blue", 512: "tab:orange", 1024: "tab:green", 64: "tab:blue", 128: "tab:orange"}
        for lauf in ta["laeufe"]:
            pk = [p for p in lauf["punkte"] if p["richtung"] == "achse_10"]
            b = np.array([p["betrag"] for p in pk])
            for key, (ls, lab) in stile.items():
                axs[0].semilogx(b, [p[key] for p in pk], ls, color=farben.get(lauf["L"], "k"), marker=".",
                                label=f"L={lauf['L']}: {lab}" if lauf["L"] == ta["laeufe"][-1]["L"] else None)
        axs[0].axhline(POLYAKOV, color="k", lw=1)
        axs[0].axhspan(POLYAKOV * 0.97, POLYAKOV * 1.03, color="0.85")
        axs[0].set_title("Teil A (2D, k laengs Achse): Steifigkeit/(Flaeche k^2); schwarz -1/(24 pi), Band 3 %")
        axs[0].set_xlabel("|k|")
        axs[0].legend(fontsize=7)
        lauf = ta["laeufe"][-1]
        for r, f in (("achse_10", "tab:green"), ("diag_11", "tab:red"), ("gegen_1m1", "tab:purple")):
            pk = [p for p in lauf["punkte"] if p["richtung"] == r]
            b = np.array([p["betrag"] for p in pk])
            axs[1].semilogx(b, [p["c_P_eckenskalierung"] for p in pk], "-", color=f, marker=".", label=f"P {r}")
            axs[1].semilogx(b, [p["c_D_mit_mass"] for p in pk], "--", color=f, marker=".", label=f"D {r}")
        axs[1].axhline(POLYAKOV, color="k", lw=1)
        axs[1].set_title(f"Teil A, L = {lauf['L']}: drei Richtungen (P durchgezogen, D gestrichelt)")
        axs[1].set_xlabel("|k|")
        axs[1].legend(fontsize=7)
        fig.tight_layout()
        fig.savefig(f"{ordner}/bild-teilA.png", dpi=110)
        plt.close(fig)
        if "harmonische" in ta:
            h = ta["harmonische"][-1]
            pts = h["punkte"]
            phi = np.array([p["phi"] for p in pts])
            kap2 = np.array([p["betrag"] for p in pts]) ** 2
            Y = np.array([p["K2"] for p in pts])
            sp = [np.ones_like(phi), np.cos(2 * phi), np.sin(2 * phi), np.cos(4 * phi), np.sin(4 * phi), kap2]
            for m in (2, 4, 6):
                sp += [kap2 * np.cos(m * phi), kap2 * np.sin(m * phi)]
            X = np.stack(sp, axis=1)
            fein = np.linspace(0, np.pi, 400)
            T = polyakov_form(fein)
            fig, axs = plt.subplots(1, 3, figsize=(16, 4.8))
            for ax, (a, b) in zip(axs, [(0, 0), (0, 1), (2, 2)]):
                y = Y[:, a, b]
                coef, *_ = np.linalg.lstsq(X, y, rcond=None)
                ohne4 = coef.copy()
                ohne4[3] = ohne4[4] = 0.0
                ax.plot(phi, y - X @ ohne4, ".", ms=4, label="Gitter minus Moden 0, 2 und k^2-Terme")
                ax.plot(fein, coef[3] * np.cos(4 * fein) + coef[4] * np.sin(4 * fein), "-", label="Fit 4phi")
                p4c = 2 * np.mean(polyakov_form(np.linspace(0, 2 * np.pi, 1440, endpoint=False))[a, b]
                                  * np.cos(4 * np.linspace(0, 2 * np.pi, 1440, endpoint=False)))
                p4s = 2 * np.mean(polyakov_form(np.linspace(0, 2 * np.pi, 1440, endpoint=False))[a, b]
                                  * np.sin(4 * np.linspace(0, 2 * np.pi, 1440, endpoint=False)))
                ax.plot(fein, p4c * np.cos(4 * fein) + p4s * np.sin(4 * fein), "k--", label="Polyakov -1/(48 pi)")
                ax.set_title(f"Eintrag h{['00', '11', '01'][a]}-h{['00', '11', '01'][b]}, L = {h['L']}")
                ax.set_xlabel("Richtung phi von k")
                ax.legend(fontsize=7)
            fig.tight_layout()
            fig.savefig(f"{ordner}/bild-teilA2-harmonische.png", dpi=110)
            plt.close(fig)
    # Teil B
    for n in (4, 3):
        ks = sorted([key for key in ketten if key[0] == n and key[2] == max(k[2] for k in ketten if k[0] == n)],
                    key=lambda x: x[1]) if any(k[0] == n for k in ketten) else []
        if not ks:
            continue
        ziel_r = -(n - 2)
        fig, axs = plt.subplots(3, len(ks), figsize=(6 * len(ks), 13), squeeze=False)
        for j, key in enumerate(ks):
            kk = ketten[key]
            namen = sorted(set(e["richtung"] for e in kk["punkte"]), key=lambda r: [e["richtung"] for e in
                                                                                     kk["punkte"]].index(r))
            for r in namen:
                pk = [e for e in kk["punkte"] if e["richtung"] == r]
                b = [e["betrag"] for e in pk]
                axs[0, j].semilogx(b, [e["P"]["schur"]["c2"] for e in pk], "-", marker=".", label=r)
                axs[1, j].semilogx(b, [e["P"]["schur"]["r"] for e in pk], "-", marker=".", label=r)
                axs[2, j].semilogx(b, [e["P"]["eich_verhaeltnis_l"] if e["P"]["eich_verhaeltnis_l"] is not None
                                       else np.nan for e in pk], "-", marker=".", label=r)
                for var, mk in (("R2_fusspunkt", "x"), ("G_ganz", "^"), ("L_laengen", "s"), ("R1_mitte", "+")):
                    axs[1, j].semilogx(b, [e[var]["schur"]["r"] if e[var]["schur"]["r"] is not None else np.nan
                                           for e in pk], mk, color="0.5", ms=4,
                                       label=var if r == namen[0] else None)
            axs[0, j].axhline(0, color="k", lw=0.8)
            axs[0, j].set_title(f"n={n}, m^2={key[1]}, L_q={key[2]}: c2 (Plan P, Schur)")
            axs[1, j].axhline(ziel_r, color="k", lw=1)
            axs[1, j].axhspan(ziel_r * 1.1, ziel_r * 0.9, color="0.85")
            axs[1, j].set_title(f"c0s/c2 (P farbig; Varianten grau), Ziel {ziel_r} +-10 %")
            axs[2, j].axhline(IN4_TOL, color="k", lw=1)
            axs[2, j].set_yscale("log")
            axs[2, j].set_title("Eichmoden: max|kappa_eich|/kappa_spin2 (je Einheit delta l), Linie 5 %")
            for a in axs[:, j]:
                a.set_xlabel("|k|")
            axs[0, j].legend(fontsize=6)
            axs[1, j].legend(fontsize=6)
        fig.tight_layout()
        fig.savefig(f"{ordner}/bild-teilB-n{n}.png", dpi=100)
        plt.close(fig)


if __name__ == "__main__":
    main()
