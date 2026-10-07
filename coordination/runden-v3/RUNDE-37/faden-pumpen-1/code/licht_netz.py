#!/usr/bin/env python3
"""LICHT-FINN-NETZ-1 (Runde 43, Code-Agent fuer die Leitung claude-primary).

Dispersion kurzer Wellen auf Finns regelmaessigem Tetraeder-Netz, je Richtung (26 Richtungen), aus exakten
Bloch-Eigenwerten. Laengeneinheit l = 1 PU = Tetraederkante (Pyrochlor-Abstand); Diamant-Bindung b = sqrt(6)/2 PU.

Operatoren auf Finns Netz:
  S-D  Skalar, Diamant-Graph (Tetraedermitten), gleiche Gewichte (patch-test: sum d = 0 an jedem Knoten)
  S-P  Skalar, Pyrochlor-Graph (Tetraederecken, Kanten = Tetraederkanten), gleiche Gewichte (Kanten in +-Paaren)
  W-D  Weyl-Operator nach spinnetz.py: H0_ij = (i/2) A (sigma.n_ij) e^{ik.d_ij}, Diamant-Graph, gleiche Gewichte
  Q-W  Weyl-Quantenautomat QCA-DIAMANT-4, Vertreter "d1|L2:P+P" (Fassung 1 frei), nur kopiert (A, freqs)
  Q-G  Grover-Lauf QCA-DIAMANT-4, Vertreter "cayley|T:1+3" (Fassung 2 w0), nur kopiert
  M-D  Maxwell in der Coulomb-Phase: A auf Diamant-Kanten (= Pyrochlor-Ecken), Fluss auf Sechsringen, K = C^dag C
Kontrollen (Dimensionsvergleich): Z3 Skalar, Z3 Weyl (spinnetz-Kubik), Z3 Maxwell (Yee), Kette 1D, Quadrat 2D, Wabe 2D.

Fit je Richtung und Zweig: omega/k = c (1 + a1 k + a2 k^2 + ... ) (alle Potenzen bis Grad g); Kartenmodell nur gerade.

Aufruf (nur ueber kleintest.sh):
  python licht_netz.py rechnen <haupt_A1f.json> <haupt_A2w.json> <aus.json>
  python licht_netz.py bild <aus.json> <bild.png>
"""
import itertools
import json
import math
import sys
import time

import numpy as np

HBARC = 1.973269804e-16      # GeV m
L_P = 1.616255e-35           # m
E_QG2_SUB = 6.9e11           # GeV, LHAASO 2024, n = 2, subluminal (STRANG-ANKER-L DOSSIER Z. 86)
E_QG1_SUB = 1.0e20           # GeV, n = 1, subluminal (Z. 85)
E_QG1_SUP = 1.1e20           # GeV, n = 1, superluminal (Z. 85)

SQ2, SQ3 = math.sqrt(2.0), math.sqrt(3.0)
AC = 2.0 * SQ2               # kubische Gitterkonstante: Tetraederkante AC*sqrt(2)/4 = 1 PU
TV = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], dtype=float)
D_BOND = AC / 4.0 * TV       # Diamant-Bindungen A -> B
B_LEN = AC * SQ3 / 4.0       # = sqrt(6)/2
P_SITE = AC / 8.0 * TV       # Pyrochlor-Ecken = Bindungsmitten
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)

# Fenster: (k_min, k_max, Punkte, Grad); W0 Hauptfenster, Wk und Wg Proben (nur beschreibend)
FENSTER = {"W0": (0.01, 0.30, 60, 8), "Wk": (0.005, 0.15, 60, 6), "Wg": (0.01, 0.60, 80, 10)}
K_TEST = 1e-4
FLACH = 1e-3                 # Zweige mit c < FLACH gelten als flach (QCA) und zaehlen nicht
LF1_FENSTER = (0.01, 0.2)
LF2_SCHWELLE = 0.10
LF0_ISO = 1e-6
LF0_Z3 = 1e-6

FINN = ["S-D", "S-P", "W-D", "Q-W", "Q-G", "M-D"]
KONTROLLEN = ["Z3-S", "Z3-W", "Z3-M", "K1-S", "Q2-S", "WB-S"]
SYMM_KUBISCH = ["S-D", "S-P", "W-D", "Q-G", "M-D", "Z3-S", "Z3-W", "Z3-M"]   # LF0 nach Plan (Praemisse der Karte)


def js(x):
    if isinstance(x, dict):
        return {str(k): js(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [js(v) for v in x]
    if isinstance(x, (np.floating, float)):
        v = float(x)
        return v if math.isfinite(v) else None
    if isinstance(x, np.bool_):
        return bool(x)
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, np.ndarray):
        return js(x.tolist())
    return x


def wrap(x):
    return (np.asarray(x) + np.pi) % (2 * np.pi) - np.pi


# ------------------------------------------------------------------ Richtungen
def richtungen26():
    return np.array([np.array(v, float) / np.linalg.norm(v) for v in itertools.product((-1, 0, 1), repeat=3) if any(v)])


def klasse(n):
    return {1: "100", 2: "110", 3: "111"}[int(np.sum(np.abs(n) > 1e-9))]


def richtungen2d(m=24):
    w = 2 * np.pi * np.arange(m) / m
    return np.stack([np.cos(w), np.sin(w), np.zeros(m)], axis=1)


def fib(m):
    i = np.arange(m) + 0.5
    phi = np.arccos(1 - 2 * i / m)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], axis=1)


# ------------------------------------------------------------------ Graphen (gerichtete Kanten i -> j, Versatz d)
def b_diamant():
    b = []
    for a in range(4):
        b.append((0, 1, D_BOND[a]))
        b.append((1, 0, -D_BOND[a]))
    return 2, b


def b_pyrochlor():
    b = []
    for i in range(4):
        for j in range(4):
            if i != j:
                d = P_SITE[j] - P_SITE[i]
                b.append((i, j, d))      # Aufwaerts-Tetraeder
                b.append((i, j, -d))     # Abwaerts-Tetraeder (Bild durch die gemeinsame Ecke)
    return 4, b


def b_kubisch(dim):
    b = []
    for a in range(dim):
        e = np.zeros(3)
        e[a] = 1.0
        b.append((0, 0, e))
        b.append((0, 0, -e))
    return 1, b


def b_wabe():
    b = []
    for w in (90.0, 210.0, 330.0):
        d = np.array([math.cos(math.radians(w)), math.sin(math.radians(w)), 0.0])
        b.append((0, 1, d))
        b.append((1, 0, -d))
    return 2, b


# ------------------------------------------------------------------ Operatoren: k -> Liste positiver Zweige
def op_skalar(ns, bonds):
    def f(k):
        L = np.zeros((ns, ns), dtype=complex)
        for i, j, d in bonds:
            L[i, i] += 1.0
            L[i, j] -= np.exp(1j * (k @ d))
        ev = np.linalg.eigvalsh(L)
        return [math.sqrt(max(ev[0], 0.0))]
    return f, 1


def weyl_matrix(ns, bonds, k):
    H = np.zeros((2 * ns, 2 * ns), dtype=complex)
    for i, j, d in bonds:
        n = d / np.linalg.norm(d)
        H[2 * i:2 * i + 2, 2 * j:2 * j + 2] += 0.5j * (n[0] * SX + n[1] * SY + n[2] * SZ) * np.exp(1j * (k @ d))
    return H


def op_weyl(ns, bonds):
    def f(k):
        ev = np.linalg.eigvalsh(weyl_matrix(ns, bonds, k))
        return list(ev[ns:])        # positive Haelfte (Spektrum symmetrisch), aufsteigend: lo, hi
    return f, ns


def sechsringe():
    """Sechsringe des Diamant-Gitters bis auf FCC-Verschiebung; ganzzahlige Koordinaten in Einheiten AC/8."""
    DI = 2 * TV.astype(int)
    gesehen = {}
    for jfolge in itertools.product(range(4), repeat=6):
        if any(jfolge[m] == jfolge[(m + 1) % 6] for m in range(6)):
            continue
        x = np.zeros(3, dtype=int)
        pos, kant = [x.copy()], []
        for m, j in enumerate(jfolge):
            s = 1 if m % 2 == 0 else -1
            mid2 = 2 * x + s * DI[j]
            x = x + s * DI[j]
            kant.append((j, tuple(int(v) for v in mid2), s))
            pos.append(x.copy())
        if np.any(x != 0):
            continue
        if len({tuple(p) for p in pos[:-1]}) != 6:
            continue
        schl = []
        for a in (pos[0], pos[2], pos[4]):
            for o in (1, -1):
                schl.append(tuple(sorted((j, tuple(int(v) for v in np.array(m2) - 2 * a), o * s) for (j, m2, s) in kant)))
        key = min(schl)
        if key not in gesehen:
            gesehen[key] = (kant, pos)
    return list(gesehen.values())


def maxwell_diamant():
    ringe = sechsringe()
    E = AC / 8.0
    zeilen = []
    for kant, pos in ringe:
        c = np.mean(np.array(pos[:-1], float), axis=0) * E
        zeilen.append([(j, np.array(m2, float) * E / 2.0 - c, s) for (j, m2, s) in kant])

    def C_of(k):
        C = np.zeros((len(zeilen), 4), dtype=complex)
        for p, z in enumerate(zeilen):
            for j, rel, s in z:
                C[p, j] += s * np.exp(1j * (k @ rel))
        return C

    def G_of(k):
        G = np.zeros((4, 2), dtype=complex)
        for j in range(4):
            G[j, 0] = -np.exp(-0.5j * (k @ D_BOND[j]))
            G[j, 1] = np.exp(0.5j * (k @ D_BOND[j]))
        return G
    return C_of, G_of, 2, len(ringe)


def maxwell_kubisch():
    e = np.eye(3)

    def C_of(k):
        C = np.zeros((3, 3), dtype=complex)
        for p, (a, b) in enumerate(((0, 1), (1, 2), (2, 0))):
            c = (e[a] + e[b]) / 2
            C[p, a] += np.exp(1j * (k @ (e[a] / 2 - c))) - np.exp(1j * (k @ (e[b] + e[a] / 2 - c)))
            C[p, b] += np.exp(1j * (k @ (e[a] + e[b] / 2 - c))) - np.exp(1j * (k @ (e[b] / 2 - c)))
        return C

    def G_of(k):
        G = np.zeros((3, 1), dtype=complex)
        for a in range(3):
            G[a, 0] = np.exp(0.5j * k[a]) - np.exp(-0.5j * k[a])
        return G
    return C_of, G_of, 1, 3


def op_maxwell(C_of, nknoten):
    def f(k):
        C = C_of(k)
        ev = np.linalg.eigvalsh(C.conj().T @ C)
        return [math.sqrt(max(v, 0.0)) for v in ev[nknoten:]]
    nb = C_of(np.array([0.1, 0.2, 0.3])).shape[1]
    return f, nb - nknoten


def qca_laden(pfad, schluessel):
    d = json.load(open(pfad))
    r = d["faelle"][schluessel]["repr"]
    A = np.array(r["A"]["re"], dtype=float) + 1j * np.array(r["A"]["im"], dtype=float)
    fr = np.array(r["freqs"], dtype=float)

    def W(k):   # wie W_at in qca_diamant.py (QCA-DIAMANT-4); u = k b / sqrt3, Zweischritt
        u = np.asarray(k, float) * B_LEN / SQ3
        ph = np.exp(1j * (fr @ u))
        return np.tensordot(ph, A, axes=1)
    return W, A.shape[-1], bool(r.get("kegel_0", False))


def cluster(ph, tol=1e-7):
    rest = list(range(len(ph)))
    out = []
    while rest:
        i = rest.pop(0)
        g = [i] + [j for j in rest if abs(float(wrap(ph[j] - ph[i]))) < tol]
        rest = [j for j in rest if j not in g]
        out.append((float(np.angle(np.mean(np.exp(1j * ph[g])))), len(g)))
    return out


def op_qca(W, phc, m):
    def f(k):
        ph = np.angle(np.linalg.eigvals(W(k)))
        rel = wrap(ph - phc)
        nah = np.sort(rel[np.argsort(np.abs(rel))[:m]])
        return list(np.abs(nah))
    return f, m


# ------------------------------------------------------------------ Fit
def fit(kk, om, grad, gerade=False):
    s = kk.max()
    x = kk / s
    pot = [j for j in range(grad + 1) if (not gerade) or j % 2 == 0]
    X = np.stack([x ** j for j in pot], axis=1)
    y = om / kk
    coef = np.linalg.lstsq(X, y, rcond=None)[0]
    rms = float(np.sqrt(np.mean((X @ coef - y) ** 2)))
    p = {j: float(coef[m] / s ** j) for m, j in enumerate(pot)}
    c = p[0]
    if abs(c) < 1e-12:
        return {"c": c, "flach": True}
    return {"c": c, "a1": p.get(1, 0.0) / c, "a2": p.get(2, 0.0) / c, "a3": p.get(3, 0.0) / c,
            "a4": p.get(4, 0.0) / c, "rms_rel": rms / abs(c), "flach": bool(abs(c) < FLACH)}


def zweige_richtung(op, nzw, n, fen):
    k0, k1, nk, g = FENSTER[fen]
    kk = np.linspace(k0, k1, nk)
    om = np.array([op(k * n) for k in kk], dtype=float)
    return [fit(kk, om[:, z], g) for z in range(nzw)], [fit(kk, om[:, z], g, gerade=True) for z in range(nzw)], kk, om


def kurven(op, nzw, dirs):
    k0, k1, nk, g = FENSTER["W0"]
    kk = np.linspace(k0, k1, 30)
    out = {}
    for n in dirs:
        om = np.array([op(k * n) for k in kk], dtype=float)
        out[klasse(n)] = {"k": kk, "om_durch_k": (om / kk[:, None]).T}
    return out


def zusammenfassen(werte):
    w = np.array([v for v in werte if v is not None], dtype=float)
    if len(w) == 0:
        return None
    mit = float(np.mean(w))
    return {"mittel": mit, "min": float(np.min(w)), "max": float(np.max(w)), "spannweite": float(np.max(w) - np.min(w)),
            "spannweite_rel": float((np.max(w) - np.min(w)) / abs(mit)) if mit != 0 else None,
            "sd_rel": float(np.std(w) / abs(mit)) if mit != 0 else None, "anzahl": int(len(w))}


def operator_auswerten(name, op, nzw, dirs, kugel=None, mit_kurven=False):
    t0 = time.time()
    erg = {"name": name, "zweige": nzw, "fenster": {}}
    for fen in FENSTER:
        je = []
        for n in dirs:
            fa, fg, kk, om = zweige_richtung(op, nzw, n, fen)
            je.append({"n": n, "klasse": klasse(n), "voll": fa, "gerade": fg})
        zw = []
        for z in range(nzw):
            gueltig = [e for e in je if not e["voll"][z].get("flach", False)]
            zz = {"gueltige_richtungen": len(gueltig)}
            for grp in ("voll", "gerade"):
                zz[grp] = {}
                for key in ("c", "a1", "a2", "a3", "a4", "rms_rel"):
                    if grp == "gerade" and key in ("a1", "a3"):
                        continue
                    zz[grp][key] = zusammenfassen([e[grp][z].get(key) for e in gueltig])
            zz["je_richtung"] = [{"n": e["n"], "klasse": e["klasse"], "c": e["voll"][z].get("c"),
                                  "a1": e["voll"][z].get("a1"), "a2": e["voll"][z].get("a2"),
                                  "a3": e["voll"][z].get("a3"), "a4": e["voll"][z].get("a4"),
                                  "a2_gerade": e["gerade"][z].get("a2"), "a4_gerade": e["gerade"][z].get("a4"),
                                  "rms_rel": e["voll"][z].get("rms_rel"), "flach": e["voll"][z].get("flach")}
                                 for e in je]
            zw.append(zz)
        erg["fenster"][fen] = zw
    if kugel is not None:
        per = [[] for _ in range(nzw)]
        for n in kugel:
            fa, _, _, _ = zweige_richtung(op, nzw, n, "W0")
            for z in range(nzw):
                if not fa[z].get("flach", False):
                    per[z].append(fa[z]["a2"])
        erg["kugel_a2_W0"] = [zusammenfassen(p) for p in per]
    if mit_kurven:
        erg["kurven"] = kurven(op, nzw, [np.array([1.0, 0, 0]), np.array([1.0, 1, 0]) / SQ2, np.ones(3) / SQ3])
    erg["laufzeit_s"] = time.time() - t0
    return erg


# ------------------------------------------------------------------ Schreibtisch-Formeln (PLAN Abschnitt 2, [M])
def s4(n):
    return float(np.sum(np.asarray(n) ** 4))


def s6(n):
    return float(np.sum(np.asarray(n) ** 6))


def schreibtisch(name, n, zweig):
    if name in ("Z3-S", "Z3-M", "K1-S", "Q2-S"):
        return {"a2": -s4(n) / 24.0, "a4": s6(n) / 720.0 - s4(n) ** 2 / 1152.0}
    if name == "Z3-W":
        return {"a2": -s4(n) / 6.0, "a4": s6(n) / 45.0 - s4(n) ** 2 / 72.0}
    if name == "WB-S":
        return {"a2": -1.0 / 32.0}
    if name == "S-D":
        return {"a2": -(3.0 - 2.0 * s4(n)) / 48.0}
    if name == "W-D":
        q = np.array([n[1] * n[2], n[2] * n[0], n[0] * n[1]])
        betrag = float(np.linalg.norm(np.cross(q, n))) * B_LEN / SQ3
        return {"a1": (-betrag if zweig == 0 else betrag)}
    return {}


def schreibtisch_vergleich(erg, dirs):
    out = {}
    zw = erg["fenster"]["W0"]
    for z, zz in enumerate(zw):
        for key in ("a1", "a2", "a4"):
            abw = []
            for e in zz["je_richtung"]:
                soll = schreibtisch(erg["name"], np.array(e["n"]), z).get(key)
                if soll is not None and e.get(key) is not None:
                    abw.append(abs(e[key] - soll))
            if abw:
                out[f"zweig{z}_{key}_max_abw"] = float(max(abw))
    return out


# ------------------------------------------------------------------ Schranken (Teil K)
def l_aus_a2(a2):
    if a2 is None or a2 >= 0:
        return None
    return HBARC / (E_QG2_SUB * math.sqrt(2.0 * abs(a2)))


def l_aus_a1(a1):
    if a1 is None or a1 == 0:
        return None
    return HBARC / (2.0 * abs(a1) * (E_QG1_SUB if a1 < 0 else E_QG1_SUP))


def schranken(erg):
    out = []
    for z, zz in enumerate(erg["fenster"]["W0"]):
        a2s = [e["a2"] for e in zz["je_richtung"] if not e.get("flach") and e.get("a2") is not None]
        a1s = [e["a1"] for e in zz["je_richtung"] if not e.get("flach") and e.get("a1") is not None]
        if not a2s:
            out.append(None)
            continue
        neg = [a for a in a2s if a < 0]
        r = {"a2_alle_negativ": len(neg) == len(a2s), "a2_positiv_richtungen": len(a2s) - len(neg)}
        if neg:
            amin, amit, amax = min(abs(a) for a in neg), abs(float(np.mean(neg))), max(abs(a) for a in neg)
            for tag, a in (("konservativ_min_abs_a2", amin), ("mittel_abs_a2", amit), ("streng_max_abs_a2", amax)):
                lm = l_aus_a2(-a)
                r[tag] = {"abs_a2": a, "l_m": lm, "l_durch_lP": lm / L_P, "bindung_m": lm * B_LEN}
        if a1s:
            amax1 = max(abs(a) for a in a1s)
            r["a1_max_abs"] = amax1
            if amax1 > 1e-8:
                r["linear"] = {"l_m_sub": HBARC / (2.0 * amax1 * E_QG1_SUB), "l_m_sup": HBARC / (2.0 * amax1 * E_QG1_SUP)}
                r["linear"]["l_durch_lP_sub"] = r["linear"]["l_m_sub"] / L_P
        out.append(r)
    return out


# ------------------------------------------------------------------ Urteile (PLAN Abschnitt 5, mechanisch)
def urteil_menge(flags):
    if not flags:
        return "nicht auswertbar"
    if all(flags):
        return "eingetroffen"
    if not any(flags):
        return "nicht eingetroffen"
    return "geteilt"


def basis(name):
    return name.rstrip("0123456789")


def urteile(ops):
    u = {}
    # LF0
    iso = {}
    for name, erg in ops.items():
        if "fehler" in erg:
            continue
        for z, zz in enumerate(erg["fenster"]["W0"]):
            c = zz["voll"]["c"]
            if c is None or c["spannweite_rel"] is None:
                continue
            iso[f"{name}/{z}"] = c["spannweite_rel"]
    z3 = ops.get("Z3-S")
    z3_ok, z3_abw = None, None
    if z3 and "fehler" not in z3:
        abw = [abs(e["a2"] + 1.0 / 24.0) for e in z3["fenster"]["W0"][0]["je_richtung"] if e["klasse"] == "100"]
        z3_abw = max(abw)
        z3_ok = z3_abw < LF0_Z3
    plan_iso = {k: v for k, v in iso.items() if basis(k.split("/")[0]) in SYMM_KUBISCH}
    u["LF0"] = {
        "plan": "eingetroffen" if (plan_iso and all(v < LF0_ISO for v in plan_iso.values()) and z3_ok) else "nicht eingetroffen",
        "karte": "eingetroffen" if (iso and all(v < LF0_ISO for v in iso.values()) and z3_ok) else "nicht eingetroffen",
        "spannweite_rel_c": iso, "z3_a2_achse_max_abw": z3_abw, "z3_ok": z3_ok,
        "verletzt_plan": [k for k, v in plan_iso.items() if not v < LF0_ISO],
        "verletzt_karte": [k for k, v in iso.items() if not v < LF0_ISO]}
    # LF1, LF2 je Zweig auf Finns Netz
    lf1, lf2 = {}, {}
    for name, erg in ops.items():
        if basis(name) not in FINN or "fehler" in erg:
            continue
        for z, zz in enumerate(erg["fenster"]["W0"]):
            a2 = zz["voll"]["a2"]
            if a2 is None:
                continue
            lf1[f"{name}/{z}"] = {"abs_mittel": abs(a2["mittel"]),
                                  "ok": LF1_FENSTER[0] <= abs(a2["mittel"]) <= LF1_FENSTER[1]}
            lf2[f"{name}/{z}"] = {"spannweite_rel": a2["spannweite_rel"],
                                  "ok": (a2["spannweite_rel"] is not None and a2["spannweite_rel"] > LF2_SCHWELLE)}
    md = [k for k in lf1 if basis(k.split("/")[0]) == "M-D"]
    u["LF1"] = {"plan_M-D": urteil_menge([lf1[k]["ok"] for k in md]) if md else "nicht auswertbar",
                "karte_alle_finn": urteil_menge([v["ok"] for v in lf1.values()]), "je_zweig": lf1}
    u["LF2"] = {"plan_M-D": urteil_menge([lf2[k]["ok"] for k in md]) if md else "nicht auswertbar",
                "karte_alle_finn": urteil_menge([v["ok"] for v in lf2.values()]), "je_zweig": lf2}
    return u


# ------------------------------------------------------------------ Hauptteil
def rechnen(pfad_a1f, pfad_a2w, aus):
    t0 = time.time()
    d26 = richtungen26()
    d2 = richtungen2d()
    d1 = np.array([[1.0, 0, 0], [-1.0, 0, 0]])
    kugel = fib(200)
    ops, kontrollen = {}, {}
    plan = []

    ns, bd = b_diamant()
    plan.append(("S-D", lambda: op_skalar(ns, bd), d26, True))
    npy, bp = b_pyrochlor()
    plan.append(("S-P", lambda: op_skalar(npy, bp), d26, True))
    plan.append(("W-D", lambda: op_weyl(ns, bd), d26, True))
    try:
        C_d, G_d, nk_d, nringe = maxwell_diamant()
        kontrollen["M-D_sechsringe_je_zelle"] = nringe
        rng = np.random.default_rng([43, 1])
        cg, herm, nullen, luecke = [], [], [], []
        for _ in range(50):
            k = rng.normal(size=3)
            C, G = C_d(k), G_d(k)
            cg.append(float(np.max(np.abs(C @ G))))
            ev = np.linalg.eigvalsh(C.conj().T @ C)
            nullen.append(float(max(abs(ev[0]), abs(ev[1]))))
            luecke.append(float(ev[2]))
        kontrollen["M-D_rot_grad_max"] = max(cg)
        kontrollen["M-D_eichnullen_max"] = max(nullen)
        kontrollen["M-D_photon_min_ev_zufall"] = min(luecke)
        plan.append(("M-D", lambda: op_maxwell(C_d, nk_d), d26, True))
    except Exception as ex:  # noqa: BLE001
        ops["M-D"] = {"fehler": repr(ex)}
    try:
        Wq, sq, kq = qca_laden(pfad_a1f, "d1|L2:P+P")
        Wg, sg, kg = qca_laden(pfad_a2w, "cayley|T:1+3")
        rng = np.random.default_rng([43, 2])
        un = []
        for W in (Wq, Wg):
            for _ in range(20):
                M = W(rng.normal(size=3))
                un.append(float(np.max(np.abs(M.conj().T @ M - np.eye(M.shape[0])))))
        kontrollen["QCA_unitaer_max_abw"] = max(un)
        for name, W, kq_ in (("Q-W", Wq, kq), ("Q-G", Wg, kg)):
            cl = cluster(np.angle(np.linalg.eigvals(W(np.zeros(3)))))
            kontrollen[f"{name}_cluster_k0"] = cl
            kontrollen[f"{name}_kegel_0_quelle"] = kq_
            kegel = [(p, m) for (p, m) in cl if m >= 2]
            for ci, (p, m) in enumerate(kegel):
                plan.append((f"{name}" if len(kegel) == 1 else f"{name}{ci}",
                             (lambda W=W, p=p, m=m: op_qca(W, p, m)), d26, True))
    except Exception as ex:  # noqa: BLE001
        ops["Q-W"] = {"fehler": repr(ex)}
    n1, bz = b_kubisch(3)
    plan.append(("Z3-S", lambda: op_skalar(n1, bz), d26, False))
    plan.append(("Z3-W", lambda: op_weyl(n1, bz), d26, False))
    C_z, G_z, nk_z, _ = maxwell_kubisch()
    plan.append(("Z3-M", lambda: op_maxwell(C_z, nk_z), d26, False))
    nk1, bk1 = b_kubisch(1)
    plan.append(("K1-S", lambda: op_skalar(nk1, bk1), d1, False))
    nq2, bq2 = b_kubisch(2)
    plan.append(("Q2-S", lambda: op_skalar(nq2, bq2), d2, False))
    nwb, bwb = b_wabe()
    plan.append(("WB-S", lambda: op_skalar(nwb, bwb), d2, False))

    # Hermitezitaet der Bloch-Matrizen (Stichprobe)
    rng = np.random.default_rng([43, 3])
    he = []
    for _ in range(20):
        k = rng.normal(size=3)
        H = weyl_matrix(ns, bd, k)
        he.append(float(np.max(np.abs(H - H.conj().T))))
    kontrollen["W-D_hermite_max"] = max(he)

    for name, mk, dirs, finn in plan:
        try:
            op, nzw = mk()
            erg = operator_auswerten(name, op, nzw, dirs, kugel=(kugel if finn else None), mit_kurven=finn)
            erg["schreibtisch_vergleich"] = schreibtisch_vergleich(erg, dirs)
            if finn:
                erg["schranken"] = schranken(erg)
            ops[name] = erg
        except Exception as ex:  # noqa: BLE001
            ops[name] = {"fehler": repr(ex)}
        print(f"{name}: {'Fehler ' + ops[name]['fehler'] if 'fehler' in ops[name] else 'ok'} "
              f"({time.time() - t0:.1f} s)", flush=True)

    # Kopfprobe der Umrechnung (WEYL-LINEAR-1: kappa 0,117 -> 5,91e-28 m)
    kontrollen["kopfprobe_kappa_0117_m"] = l_aus_a2(-0.117)
    kontrollen["b_durch_PU"] = B_LEN
    kontrollen["tetraederkante_PU"] = float(np.linalg.norm(P_SITE[0] - P_SITE[1]))
    kontrollen["pyrochlor_nachbarn_je_ecke"] = int(sum(1 for (i, j, d) in bp if i == 0))
    kontrollen["pyrochlor_abstaende"] = sorted({round(float(np.linalg.norm(d)), 12) for (_, _, d) in bp})

    namen_finn = [n for n in ops if basis(n) in FINN]
    out = {"karte": "LICHT-FINN-NETZ-1", "numpy": np.__version__, "argv": sys.argv, "fenster": FENSTER,
           "einheit": "l = 1 PU = Tetraederkante; Diamant-Bindung b = sqrt(6)/2 PU",
           "konstanten": {"hbarc_GeV_m": HBARC, "l_P_m": L_P, "E_QG2_sub_GeV": E_QG2_SUB,
                          "E_QG1_sub_GeV": E_QG1_SUB, "E_QG1_sup_GeV": E_QG1_SUP},
           "kontrollen": kontrollen, "operatoren": ops, "finn_operatoren": namen_finn}
    out["urteile"] = urteile(ops)
    out["laufzeit_s"] = time.time() - t0
    with open(aus, "w") as fh:
        json.dump(js(out), fh, indent=1)
    print(f"fertig {time.time() - t0:.1f} s -> {aus}", flush=True)


def bild(pfad, png):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    d = json.load(open(pfad))
    ops = d["operatoren"]
    namen = [n for n in ops if "fehler" not in ops[n] and "schranken" in ops[n]]
    fig, ax = plt.subplots(2, 2, figsize=(14, 10))
    farbe = {"100": "tab:blue", "110": "tab:orange", "111": "tab:green"}
    # (a) a2 je Richtung
    x = 0
    ticks, labels = [], []
    for n in namen:
        for z, zz in enumerate(ops[n]["fenster"]["W0"]):
            for e in zz["je_richtung"]:
                if e.get("flach") or e.get("a2") is None:
                    continue
                ax[0, 0].plot(x + 0.15 * (["100", "110", "111"].index(e["klasse"]) - 1), e["a2"], "o",
                              color=farbe[e["klasse"]], ms=4)
            ticks.append(x)
            labels.append(f"{n}/{z}")
            x += 1
    ax[0, 0].axhspan(-0.2, -0.01, color="0.9", zorder=0)
    ax[0, 0].axhspan(0.01, 0.2, color="0.9", zorder=0)
    ax[0, 0].set_xticks(ticks)
    ax[0, 0].set_xticklabels(labels, rotation=60, fontsize=8)
    ax[0, 0].set_ylabel("a2 (k in 1/PU)")
    ax[0, 0].set_title("(a) a2 je Richtung (blau 100, orange 110, gruen 111); grau: LF1-Band")
    # (b) a4 je Richtung
    x = 0
    for n in namen:
        for z, zz in enumerate(ops[n]["fenster"]["W0"]):
            for e in zz["je_richtung"]:
                if e.get("flach") or e.get("a4") is None:
                    continue
                ax[0, 1].plot(x + 0.15 * (["100", "110", "111"].index(e["klasse"]) - 1), e["a4"], "o",
                              color=farbe[e["klasse"]], ms=4)
            x += 1
    ax[0, 1].set_xticks(ticks)
    ax[0, 1].set_xticklabels(labels, rotation=60, fontsize=8)
    ax[0, 1].set_ylabel("a4 (k in 1/PU)")
    ax[0, 1].set_title("(b) a4 je Richtung")
    # (c) Kurven omega/(c k) - 1
    stil = {"100": "-", "110": "--", "111": ":"}
    for n in namen:
        kv = ops[n].get("kurven", {})
        cz = ops[n]["fenster"]["W0"]
        for kl, kd in kv.items():
            kk = np.array(kd["k"])
            for z, row in enumerate(kd["om_durch_k"]):
                c = cz[z]["voll"]["c"]
                if c is None or abs(c["mittel"]) < FLACH:
                    continue
                ax[1, 0].plot(kk, np.array(row) / c["mittel"] - 1, stil[kl], lw=1)
    ax[1, 0].set_xlabel("k (1/PU)")
    ax[1, 0].set_ylabel("omega/(c k) - 1")
    ax[1, 0].set_title("(c) Abweichung je Operator; Linie 100, Strich 110, Punkt 111")
    # (d) bedingte Schranke
    x = 0
    for n in namen:
        for z, s in enumerate(ops[n]["schranken"]):
            if s and "konservativ_min_abs_a2" in s:
                lo, mi, hi = (s["streng_max_abs_a2"]["l_m"], s["mittel_abs_a2"]["l_m"], s["konservativ_min_abs_a2"]["l_m"])
                ax[1, 1].plot([x, x], [lo, hi], "k-")
                ax[1, 1].plot(x, mi, "ko")
            x += 1
    ax[1, 1].axhline(L_P, color="r", lw=1)
    ax[1, 1].set_yscale("log")
    ax[1, 1].set_xticks(ticks)
    ax[1, 1].set_xticklabels(labels, rotation=60, fontsize=8)
    ax[1, 1].set_ylabel("Tetraederkante l < ... (m)")
    ax[1, 1].set_title("(d) bedingte LHAASO-Schranke (E_QG,2 > 6,9e11 GeV); rot: Planck-Laenge")
    fig.suptitle("LICHT-FINN-NETZ-1: Dispersion auf Finns Tetraeder-Netz (synthetische Rechnung)")
    fig.tight_layout()
    fig.savefig(png, dpi=110)
    print(f"bild -> {png}", flush=True)


if __name__ == "__main__":
    if len(sys.argv) >= 5 and sys.argv[1] == "rechnen":
        rechnen(sys.argv[2], sys.argv[3], sys.argv[4])
    elif len(sys.argv) >= 4 and sys.argv[1] == "bild":
        bild(sys.argv[2], sys.argv[3])
    else:
        print(__doc__)
        sys.exit(2)
