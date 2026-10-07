#!/usr/bin/env python3
"""DIAMANT-NULLSTELLEN-1 (Runde 44, Code-Agent fuer die Leitung claude-primary).

Nullstellen und Dispersion dreier Spin-1/2-Operatoren auf Finns Diamant-Netz (Knoten = Tetraedermitten),
exakte 4x4-Bloch-Matrizen in Lage-Eichung (A bei 0, B bei d_a), Basis (A up, A down, B up, B down).
  W-D     H_AB = sum_a (i/2) sigma.n_a e^{ik.d_a}         (wie licht_netz.weyl_matrix, LICHT-FINN-NETZ-1)
  W-D+S3  H_AB = sum_v (i/2) w_s sigma.v e^{ik.(a/4)v}     v ganzzahlig (Einheit a/4), Schale 1 (4 Vektoren, w1 = 1/sqrt3,
          identisch mit W-D) und Schale 3 (12 Vektoren (+-1,+-1,+-3), Summe = 3 mod 4), w3 = w1/9
  FKM     Fu/Kane/Mele: t auf naechsten Nachbarn, i (8 lambda/a^2) sigma.(d1 x d2) auf zweiten Nachbarn; t = 1, lambda = 1/4
Laengeneinheit l = 1 PU = Tetraederkante; a = 2 sqrt2 PU (kubische Kante), b = sqrt6/2 PU (Diamant-Bindung).

Aufruf (nur ueber kleintest.sh):
  python diamant_nullstellen.py rechnen <aus.json>          Hauptlauf
  python diamant_nullstellen.py rauch <aus.json>            Rauchtest (kleine Gitter), druckt nur Schluessel und Laufzeit
  python diamant_nullstellen.py bild <aus.json> <bild.png>
"""
import itertools
import json
import math
import sys
import time

import numpy as np

SQ2, SQ3 = math.sqrt(2.0), math.sqrt(3.0)
AC = 2.0 * SQ2                      # kubische Gitterkonstante a: Tetraederkante AC*sqrt(2)/4 = 1 PU
G0 = 2.0 * math.pi / AC             # 2 pi / a
TV = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], dtype=float)
D_BOND = AC / 4.0 * TV              # Diamant-Bindungen A -> B (wie licht_netz.py)
B_LEN = AC * SQ3 / 4.0              # = sqrt(6)/2
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
S0 = np.eye(2, dtype=complex)
PAULI = np.array([SX, SY, SZ])

BREZ = G0 * np.array([[-1, 1, 1], [1, -1, 1], [1, 1, -1]], dtype=float)   # primitive reziproke Vektoren (Zeilen)
V_BZ = abs(float(np.linalg.det(BREZ)))
U_STERN = math.acos(1.0 / 3.0) / math.pi                                    # 0,3918...: tan(alpha/2) = 1/sqrt2
P_DOSSIER = G0 * np.array([1.0, U_STERN, U_STERN])                          # (1; 0,392; 0,392) 2 pi/a
W_PUNKT = G0 * np.array([1.0, 0.5, 0.0])
GV = G0 * np.array([p for p in itertools.product(range(-2, 3), repeat=3)
                    if all(x % 2 == 0 for x in p) or all(x % 2 == 1 for x in p)], dtype=float)
W_ALLE = G0 * np.array(sorted({tuple(s * np.array(perm)) for perm in itertools.permutations((1.0, 0.5, 0.0))
                               for s in itertools.product((1, -1), repeat=3)}), dtype=float)

# Festlegungen des Plans [F]
FENSTER = {"W0": (0.01, 0.30, 60, 8), "Wk": (0.005, 0.15, 60, 6), "Wg": (0.01, 0.60, 80, 10)}
GITTER_PLAN = (48, 96)              # Linie gegen Punkte: Zaehlskalierung zwischen diesen beiden
GITTER_BESCHR = 144                 # dritter Punkt, nur beschreibend
KAPPA = 1.5                         # Schwelle tau = KAPPA * h * v_op, h = V_BZ^(1/3)/N
STARTS = 300                        # Startpunkte der Nullstellensuche (aus N = 48 unter der Schwelle)
E_KONV = 1e-9                       # konvergierte Nullstelle: E_min < E_KONV
CLUSTER_TOL = 1e-3                  # verschiedene Nullstellen: Abstand > 1e-3 / PU nach Faltung
GAMMA_TOL = 0.05                    # Abstand zu Gamma, ab dem eine Nullstelle "nicht Gamma" ist
DN0_NULL = 1e-10
DN0_A1 = 1e-6
DN0_SPALT = 1e-10
DN0_ISO = 1e-6
DN1_DIM = (0.5, 1.5)
DN1_MIN_TREFFER = 30
DN1_KARTE_MIN = 20
DN2_PLAN = 1e-4
DN3_SCHWELLE = 0.10
T_FKM, LAM_FKM = 1.0, 0.25          # t = 4 lambda


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


# ------------------------------------------------------------------ Richtungen (wie licht_netz.py)
def richtungen26():
    return np.array([np.array(v, float) / np.linalg.norm(v) for v in itertools.product((-1, 0, 1), repeat=3) if any(v)])


def klasse(n):
    return {1: "100", 2: "110", 3: "111"}[int(np.sum(np.abs(n) > 1e-9))]


def fib(m):
    i = np.arange(m) + 0.5
    phi = np.arccos(1 - 2 * i / m)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], axis=1)


# ------------------------------------------------------------------ Schalen und Operatoren
def schale1():
    return TV.copy()


def schale3():
    out = set()
    for perm in set(itertools.permutations((1, 1, 3))):
        for s in itertools.product((1, -1), repeat=3):
            v = tuple(int(p * q) for p, q in zip(perm, s))
            if sum(v) % 4 == 3:
                out.add(v)
    return np.array(sorted(out), dtype=float)


def spruenge(name):
    w1 = 1.0 / SQ3
    s = [(v, w1) for v in schale1()]
    if name == "W-D+S3":
        s += [(v, w1 / 9.0) for v in schale3()]
    return s


def v_vektor(K, spr):
    """V(k) = sum w v e^{ik.(a/4)v}; M = (i/2) sigma.V. K: (n,3)."""
    V = np.zeros((K.shape[0], 3), dtype=complex)
    for v, w in spr:
        ph = np.exp(1j * (K @ (AC / 4.0 * v)))
        V += w * ph[:, None] * v[None, :]
    return V


def h_chiral(K, spr):
    V = v_vektor(K, spr)
    M = 0.5j * np.einsum("ni,iab->nab", V, PAULI)
    H = np.zeros((K.shape[0], 4, 4), dtype=complex)
    H[:, :2, 2:] = M
    H[:, 2:, :2] = np.conj(np.transpose(M, (0, 2, 1)))
    return H


def fkm_tabelle(t=T_FKM, lam=LAM_FKM):
    """Sprungtabelle (R_j, B_j) mit H(k) = sum_j e^{ik.R_j} B_j (4x4)."""
    Rs, Bs = [], []
    for a in range(4):
        B = np.zeros((4, 4), dtype=complex)
        B[0, 2] = B[1, 3] = t
        Rs.append(D_BOND[a])
        Bs.append(B)
        B = np.zeros((4, 4), dtype=complex)
        B[2, 0] = B[3, 1] = t
        Rs.append(-D_BOND[a])
        Bs.append(B)
    pref = 8.0 * lam / AC ** 2
    for al in range(4):
        for be in range(4):
            if al == be:
                continue
            for off, d1, d2 in ((0, D_BOND[al], -D_BOND[be]), (2, -D_BOND[al], D_BOND[be])):
                c = np.cross(d1, d2)
                B = np.zeros((4, 4), dtype=complex)
                B[off:off + 2, off:off + 2] = 1j * pref * np.einsum("i,iab->ab", c, PAULI)
                Rs.append(d1 + d2)
                Bs.append(B)
    return np.array(Rs), np.array(Bs)


FKM_R, FKM_B = fkm_tabelle()


def h_fkm(K):
    return np.tensordot(np.exp(1j * (K @ FKM_R.T)), FKM_B, axes=1)


def hfun(name):
    if name == "FKM":
        return h_fkm
    spr = spruenge(name)
    return lambda K: h_chiral(K, spr)


def eig(Hf, K, chunk=100000):
    out = np.empty((K.shape[0], 4))
    for i in range(0, K.shape[0], chunk):
        out[i:i + chunk] = np.linalg.eigvalsh(Hf(K[i:i + chunk]))
    return out


# Kopie aus licht_netz.py (LICHT-FINN-NETZ-1), nur fuer die Kontrolle K1
def weyl_matrix_kopie(k):
    bonds = []
    for a in range(4):
        bonds.append((0, 1, D_BOND[a]))
        bonds.append((1, 0, -D_BOND[a]))
    H = np.zeros((4, 4), dtype=complex)
    for i, j, d in bonds:
        n = d / np.linalg.norm(d)
        H[2 * i:2 * i + 2, 2 * j:2 * j + 2] += 0.5j * (n[0] * SX + n[1] * SY + n[2] * SZ) * np.exp(1j * (k @ d))
    return H


def fkm_dvektor(K, t=T_FKM, lam=LAM_FKM):
    """Geschlossene Form [M, Plan]: E = +-|d|, d1 = t(1 + sum cos k.a_j), d2 = t sum sin k.a_j, d3..5 mit 2 lambda."""
    a1, a2, a3 = AC / 2 * np.array([0, 1, 1.0]), AC / 2 * np.array([1, 0, 1.0]), AC / 2 * np.array([1, 1, 0.0])
    x1, x2, x3 = K @ a1, K @ a2, K @ a3
    d1 = t * (1 + np.cos(x1) + np.cos(x2) + np.cos(x3))
    d2 = t * (np.sin(x1) + np.sin(x2) + np.sin(x3))
    s = np.sin
    d3 = 2 * lam * (s(x2) - s(x3) - s(x2 - x1) + s(x3 - x1))
    d4 = 2 * lam * (s(x3) - s(x1) - s(x3 - x2) + s(x1 - x2))
    d5 = 2 * lam * (s(x1) - s(x2) - s(x1 - x3) + s(x2 - x3))
    return np.sqrt(d1 ** 2 + d2 ** 2 + d3 ** 2 + d4 ** 2 + d5 ** 2)


# ------------------------------------------------------------------ BZ-Hilfen
def gitter(N):
    s = np.arange(N) / N
    S = np.stack(np.meshgrid(s, s, s, indexing="ij"), -1).reshape(-1, 3)
    return S @ BREZ


def falte(k):
    s = np.linalg.solve(BREZ.T, k)
    s = s - np.floor(s)
    k = s @ BREZ
    d = np.linalg.norm(k[None, :] - GV, axis=1)
    return k - GV[int(np.argmin(d))]


def abstand_menge(k, P):
    """kleinster Abstand von k zu einer Punktmenge P modulo reziprokes Gitter."""
    best = np.inf
    for p in P:
        d = np.linalg.norm(falte(k - p))
        best = min(best, d)
    return float(best)


def in_ebene(k, tol=1e-6):
    q = k / G0
    return bool(np.any(np.abs(q - np.round(q)) < tol))


def tempo_ref(Hf, P0, k0=1e-4):
    d = richtungen26()
    E = eig(Hf, P0[None, :] + k0 * d)
    return float(np.mean(E[:, 2] / k0))


# ------------------------------------------------------------------ Nullstellensuche
def gitter_zaehlen(Hf, N, v_op):
    K = gitter(N)
    E = eig(Hf, K)
    em = np.min(np.abs(E), axis=1)
    h = V_BZ ** (1.0 / 3.0) / N
    tau = KAPPA * h * v_op
    sel = em < tau
    return {"N": N, "h": h, "tau": tau, "treffer": int(np.sum(sel)), "min_E": float(np.min(em)),
            "spaltung_max": float(np.max(np.maximum(E[:, 1] - E[:, 0], E[:, 3] - E[:, 2])))}, K[sel], em[sel]


def vv_grad(k, spr):
    V = np.zeros(3, dtype=complex)
    dV = np.zeros((3, 3), dtype=complex)
    for v, w in spr:
        d = AC / 4.0 * v
        ph = np.exp(1j * (k @ d))
        V += w * v * ph
        dV += w * np.outer(1j * d, v) * ph
    return V @ V, 2.0 * dV @ V


def newton_chiral(k0, spr, it=80):
    k = np.array(k0, float)
    for _ in range(it):
        g, gr = vv_grad(k, spr)
        J = np.array([gr.real, gr.imag])
        F = np.array([g.real, g.imag])
        step = -np.linalg.pinv(J, rcond=1e-13) @ F
        nst = np.linalg.norm(step)
        if nst > 0.2:
            step *= 0.2 / nst
        k = k + step
        if nst < 1e-15:
            break
    return k


def nm_fkm(k0, Hf):
    from scipy.optimize import minimize
    f = lambda k: float(np.min(np.abs(np.linalg.eigvalsh(Hf(k[None, :])[0])))) ** 2  # noqa: E731
    simplex = np.vstack([k0, k0 + 0.02 * np.eye(3)])
    r = minimize(f, k0, method="Nelder-Mead",
                 options={"xatol": 1e-12, "fatol": 1e-28, "maxiter": 4000, "maxfev": 8000, "initial_simplex": simplex})
    return np.array(r.x)


def nullstellen_suche(name, Hf, starts):
    out = []
    spr = None if name == "FKM" else spruenge(name)
    for k0 in starts:
        try:
            k = nm_fkm(k0, Hf) if spr is None else newton_chiral(k0, spr)
        except Exception as ex:  # noqa: BLE001
            out.append({"fehler": repr(ex)})
            continue
        e = float(np.min(np.abs(np.linalg.eigvalsh(Hf(k[None, :])[0]))))
        kf = falte(k)
        out.append({"k": kf, "E": e, "konv": e < E_KONV})
    konv = [o for o in out if o.get("konv")]
    gam = [o for o in konv if np.linalg.norm(o["k"]) < GAMMA_TOL]
    rest = [o for o in konv if np.linalg.norm(o["k"]) >= GAMMA_TOL]
    cl = []
    for o in rest:
        if all(abstand_menge(o["k"], [c]) > CLUSTER_TOL for c in cl):
            cl.append(o["k"])
    xs = G0 * np.vstack([np.eye(3), -np.eye(3)])
    klass = {"X": 0, "W": 0, "Ebene_k_i_in_2pi/a_Z": 0, "sonst": 0}
    for o in rest:
        if abstand_menge(o["k"], xs) < CLUSTER_TOL:
            klass["X"] += 1
        elif abstand_menge(o["k"], W_ALLE) < CLUSTER_TOL:
            klass["W"] += 1
        elif in_ebene(o["k"]):
            klass["Ebene_k_i_in_2pi/a_Z"] += 1
        else:
            klass["sonst"] += 1
    sonst_bsp = [o["k"] / G0 for o in rest if not in_ebene(o["k"])][:10]
    return {"starts": len(starts), "konvergiert": len(konv), "gamma": len(gam), "nicht_gamma": len(rest),
            "verschiedene_nicht_gamma": len(cl), "klassen_nicht_gamma": klass,
            "abs_k_nicht_gamma": {"min": float(min((np.linalg.norm(o["k"]) for o in rest), default=np.nan)),
                                  "max": float(max((np.linalg.norm(o["k"]) for o in rest), default=np.nan))},
            "beispiele_sonst_in_2pi_durch_a": sonst_bsp,
            "punkte_in_2pi_durch_a": [o["k"] / G0 for o in rest][:400],
            "fehler": sum(1 for o in out if "fehler" in o)}


# ------------------------------------------------------------------ Fit (Kopie aus licht_netz.py)
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
            "a4": p.get(4, 0.0) / c, "rms_rel": rms / abs(c), "flach": False}


def zusammenfassen(werte):
    w = np.array([v for v in werte if v is not None], dtype=float)
    if len(w) == 0:
        return None
    mit = float(np.mean(w))
    return {"mittel": mit, "min": float(np.min(w)), "max": float(np.max(w)), "spannweite": float(np.max(w) - np.min(w)),
            "spannweite_rel": float((np.max(w) - np.min(w)) / abs(mit)) if mit != 0 else None,
            "max_abs": float(np.max(np.abs(w))), "anzahl": int(len(w))}


def dispersion(Hf, P0, dirs):
    erg = {}
    for fen, (k0, k1, nk, g) in FENSTER.items():
        kk = np.linspace(k0, k1, nk)
        je = []
        for n in dirs:
            E = eig(Hf, P0[None, :] + kk[:, None] * n[None, :])
            je.append({"n": n, "klasse": klasse(n), "zweige": [fit(kk, E[:, 2 + z], g) for z in range(2)]})
        zw = []
        for z in range(2):
            zz = {"je_richtung": [dict(n=e["n"], klasse=e["klasse"], **{q: e["zweige"][z].get(q) for q in
                                                                           ("c", "a1", "a2", "a3", "a4", "rms_rel")})
                                  for e in je]}
            for grp in ("alle", "100", "110", "111"):
                sel = [e for e in je if grp == "alle" or e["klasse"] == grp]
                zz[grp] = {q: zusammenfassen([e["zweige"][z].get(q) for e in sel]) for q in ("c", "a1", "a2", "a3", "a4")}
            zw.append(zz)
        erg[fen] = zw
    return erg


# ------------------------------------------------------------------ Wortlaut-Frage (beschreibend)
def wortlaut(name, Hf, dirs, kbetrag=0.1):
    spr = spruenge(name)
    tau = {"1": S0, "x": SX, "y": SY, "z": SZ}
    zeilen = []
    for n in dirs:
        k = kbetrag * n
        H = Hf(k[None, :])[0]
        ev, U = np.linalg.eigh(H)
        luecke = ev[3] - ev[2]
        V = v_vektor(k[None, :], spr)[0]
        m = np.cross(V.real, V.imag)
        if luecke < 1e-9 or np.linalg.norm(m) < 1e-14:
            zeilen.append({"n": n, "klasse": klasse(n), "entartet": True, "luecke": luecke})
            continue
        m = m / np.linalg.norm(m)
        q = np.array([n[1] * n[2], n[2] * n[0], n[0] * n[1]])
        qk = np.cross(q, n)
        cos_qk = float(abs(m @ qk) / np.linalg.norm(qk)) if np.linalg.norm(qk) > 1e-12 else None
        e3 = np.cross(n, m)
        rahmen = {"0": S0, "k": np.einsum("i,iab->ab", n, PAULI), "m": np.einsum("i,iab->ab", m, PAULI),
                  "kxm": np.einsum("i,iab->ab", e3, PAULI)}
        werte = []
        for z in (2, 3):
            psi = U[:, z]
            w = {}
            for ta, Ta in tau.items():
                for sb, Sb in rahmen.items():
                    w[f"tau{ta}*sigma_{sb}"] = float(np.real(np.conj(psi) @ np.kron(Ta, Sb) @ psi))
            werte.append(w)
        zeilen.append({"n": n, "klasse": klasse(n), "entartet": False, "luecke": luecke, "cos_m_qxk": cos_qk,
                       "lo": werte[0], "hi": werte[1]})
    ok = [z for z in zeilen if not z["entartet"]]
    zus = {}
    if ok:
        for key in ok[0]["lo"]:
            lo = np.array([z["lo"][key] for z in ok])
            hi = np.array([z["hi"][key] for z in ok])
            zus[key] = {"lo_mittel": float(np.mean(lo)), "hi_mittel": float(np.mean(hi)),
                        "max_abs_lo": float(np.max(np.abs(lo))), "max_abs_hi": float(np.max(np.abs(hi))),
                        "min_abs_differenz": float(np.min(np.abs(hi - lo))),
                        "trennt": bool(np.all(np.sign(lo) == -np.sign(hi)) and np.min(np.abs(hi - lo)) > 0.5)}
    return {"k_betrag": kbetrag, "richtungen": len(zeilen), "nicht_entartet": len(ok), "zusammenfassung": zus,
            "trennende_groessen": [k for k, v in zus.items() if v["trennt"]],
            "helizitaet_tau1_sigma_k": zus.get("tau1*sigma_k"), "chiralitaet_taux_sigma_0": zus.get("taux*sigma_0"),
            "cos_m_qxk_min": min((z["cos_m_qxk"] for z in ok if z["cos_m_qxk"] is not None), default=None),
            "zeilen": zeilen[:6]}


# ------------------------------------------------------------------ Kontrollen
def kontrollen(rng):
    k = {}
    s3 = schale3()
    k["schale3_anzahl"] = int(len(s3))
    k["schale3_produkte"] = sorted({int(round(np.prod(v))) for v in s3})
    k["schale3_summe"] = s3.sum(axis=0)
    k["schale3_zweites_moment"] = (s3.T @ s3)
    k["schale3_drittes_moment_xyz"] = float(np.sum(s3[:, 0] * s3[:, 1] * s3[:, 2]))
    k["schale1_drittes_moment_xyz"] = float(np.sum(TV[:, 0] * TV[:, 1] * TV[:, 2]))
    K = rng.normal(size=(20, 3)) * 2.0
    Hwd = hfun("W-D")(K)
    k["K1_wd_gegen_licht_netz_max"] = float(max(np.max(np.abs(Hwd[i] - weyl_matrix_kopie(K[i]))) for i in range(20)))
    for name in ("W-D", "W-D+S3", "FKM"):
        Hf = hfun(name)
        H = Hf(K)
        k[f"K2_hermite_{name}"] = float(np.max(np.abs(H - np.conj(np.transpose(H, (0, 2, 1))))))
        per = 0.0
        for b in BREZ:
            per = max(per, float(np.max(np.abs(eig(Hf, K) - eig(Hf, K + b[None, :])))))
        k[f"K3_periodisch_{name}"] = per
    E = eig(hfun("FKM"), K)
    k["K6_fkm_dvektor_max_abw"] = float(np.max(np.abs(E[:, 3] - fkm_dvektor(K))))
    k["K6_fkm_dvektor_max_abw_unten"] = float(np.max(np.abs(E[:, 0] + fkm_dvektor(K))))
    # K8: R senkrecht I auf der Ebene k_x = 2 pi/a
    P = np.column_stack([np.full(50, G0), rng.uniform(-G0, G0, 50), rng.uniform(-G0, G0, 50)])
    for name in ("W-D", "W-D+S3"):
        V = v_vektor(P, spruenge(name))
        k[f"K8_R_mal_I_ebene_{name}"] = float(np.max(np.abs(np.sum(V.real * V.imag, axis=1))))
    return k


def schleife_wd(m=64):
    """Analytische Schleife um X in der Ebene k_x = 2 pi/a (Dossier, ARBEITSFELD 1.5): g(u,v) = 0."""
    def g(u, v):
        al, be = math.pi / 2 * (u + v), math.pi / 2 * (u - v)
        return 2 * math.sin(al) ** 2 + 2 * math.sin(be) ** 2 - (math.cos(al) + math.cos(be)) ** 2
    pkt = []
    for th in np.linspace(0, 2 * math.pi, m, endpoint=False):
        lo, hi = 0.0, 0.7
        if g(hi * math.cos(th), hi * math.sin(th)) <= 0:
            continue
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            if g(mid * math.cos(th), mid * math.sin(th)) < 0:
                lo = mid
            else:
                hi = mid
        r = 0.5 * (lo + hi)
        pkt.append([1.0, r * math.cos(th), r * math.sin(th)])
    return G0 * np.array(pkt)


# ------------------------------------------------------------------ Urteile (PLAN Abschnitt 6, mechanisch)
def urteile(R):
    u = {}
    wd = R["operatoren"]["W-D"]
    s3 = R["operatoren"]["W-D+S3"]
    fk = R["operatoren"]["FKM"]
    # DN0
    a_pkt = (wd["E_W"] < DN0_NULL and wd["E_P_dossier"] < DN0_NULL and wd["schleife_anzahl"] >= 32
             and wd["schleife_E_max"] < DN0_NULL)
    a_dim = wd["dimension"]["D_plan"] is not None and DN1_DIM[0] <= wd["dimension"]["D_plan"] < DN1_DIM[1]
    a1max = max(s3["dispersion"]["W0"][z]["alle"]["a1"]["max_abs"] for z in range(2))
    b_ok = a1max < DN0_A1
    spalt = fk["spaltung_max"]
    iso = max(fk["dispersion_Xz"]["W0"][z]["alle"]["c"]["spannweite_rel"] for z in range(2))
    c_ok = spalt < DN0_SPALT and iso < DN0_ISO
    u["DN0"] = {"plan": "eingetroffen" if (a_pkt and a_dim and b_ok and c_ok) else "nicht eingetroffen",
                "karte": "eingetroffen" if (a_pkt and b_ok and c_ok) else "nicht eingetroffen",
                "teil_a_punkte_schleife": a_pkt, "teil_a_dimension_linie": a_dim, "teil_b_a1_max_abs": a1max,
                "teil_b": b_ok, "teil_c_spaltung_max": spalt, "teil_c_tempo_spannweite_rel": iso, "teil_c": c_ok}
    # DN1
    D = s3["dimension"]["D_plan"]
    n2 = s3["dimension"]["zaehlung"][1]["treffer"]
    if D is None or n2 < DN1_MIN_TREFFER:
        p = "nicht eingetroffen (zu wenig Treffer: nur Punkte)"
    elif DN1_DIM[0] <= D < DN1_DIM[1]:
        p = "eingetroffen"
    elif D < DN1_DIM[0]:
        p = "nicht eingetroffen (Punkte)"
    else:
        p = "nicht eingetroffen (Flaechen)"
    nv = s3["suche"]["verschiedene_nicht_gamma"]
    u["DN1"] = {"plan": p, "karte": "eingetroffen" if nv >= DN1_KARTE_MIN else "nicht eingetroffen",
                "D_plan": D, "treffer_N96": n2, "verschiedene_nicht_gamma": nv}
    # DN2
    je = [e for z in range(2) for e in s3["dispersion"]["W0"][z]["je_richtung"] if e["klasse"] == "110"]
    a3 = [abs(e["a3"]) for e in je]
    rausch = max(abs(e["a3"]) for z in range(2) for e in s3["dispersion"]["W0"][z]["je_richtung"]
                 if e["klasse"] in ("100", "111"))
    schw_k = max(10.0 * rausch, 1e-7)

    def drei(flags):
        return "eingetroffen" if all(flags) else ("nicht eingetroffen" if not any(flags) else "geteilt")
    u["DN2"] = {"plan": drei([a > DN2_PLAN for a in a3]), "karte": drei([a > schw_k for a in a3]),
                "a3_110_min_abs": min(a3), "a3_110_max_abs": max(a3), "rauschboden_100_111": rausch,
                "schwelle_karte": schw_k}
    # DN3
    sp = [fk["dispersion_Xz"]["W0"][z]["alle"]["a2"]["spannweite_rel"] for z in range(2)]
    allx = []
    for key in ("dispersion_Xz", "dispersion_Xx", "dispersion_Xy"):
        for z in range(2):
            allx += [e["a2"] for e in fk[key]["W0"][z]["je_richtung"]]
    pool = zusammenfassen(allx)
    u["DN3"] = {"plan": drei([s is not None and s > DN3_SCHWELLE for s in sp]),
                "karte": "eingetroffen" if (pool["spannweite_rel"] is not None and pool["spannweite_rel"] > DN3_SCHWELLE)
                else "nicht eingetroffen", "spannweite_rel_Xz": sp, "spannweite_rel_drei_X": pool["spannweite_rel"]}
    return u


# ------------------------------------------------------------------ Hauptteil
def rechnen(aus, rauch=False):
    t0 = time.time()
    rng = np.random.default_rng([44, 1])
    gitter_n = (8, 16) if rauch else GITTER_PLAN
    gitter_b = 24 if rauch else GITTER_BESCHR
    nstarts = 10 if rauch else STARTS
    out = {"karte": "DIAMANT-NULLSTELLEN-1", "numpy": np.__version__, "argv": sys.argv, "rauch": rauch,
           "festlegungen": {"FENSTER": FENSTER, "GITTER_PLAN": gitter_n, "GITTER_BESCHR": gitter_b, "KAPPA": KAPPA,
                            "STARTS": nstarts, "E_KONV": E_KONV, "CLUSTER_TOL": CLUSTER_TOL, "GAMMA_TOL": GAMMA_TOL,
                            "t": T_FKM, "lambda": LAM_FKM},
           "einheit": "l = 1 PU = Tetraederkante; a = 2 sqrt2 PU; Impulse in 1/PU; Punkte in 2 pi/a"}
    out["kontrollen"] = kontrollen(rng)
    print(f"kontrollen ({time.time() - t0:.1f} s)", flush=True)
    ops = {}
    d26 = richtungen26()
    for name in ("W-D", "W-D+S3", "FKM"):
        t1 = time.time()
        Hf = hfun(name)
        P0 = G0 * np.array([0.0, 0.0, 1.0]) if name == "FKM" else np.zeros(3)
        erg = {"bezugspunkt_2pi_durch_a": P0 / G0}
        v_op = tempo_ref(Hf, P0)
        erg["v_op"] = v_op
        zl = []
        starts_k, starts_e = None, None
        for N in gitter_n + (gitter_b,):
            z, Ks, Es = gitter_zaehlen(Hf, N, v_op)
            zl.append(z)
            if N == gitter_n[0]:
                starts_k, starts_e = Ks, Es
            print(f"{name} gitter N={N} ({time.time() - t0:.1f} s)", flush=True)
        D = math.log2(zl[1]["treffer"] / zl[0]["treffer"]) if zl[0]["treffer"] > 0 and zl[1]["treffer"] > 0 else None
        D3 = (math.log(zl[2]["treffer"] / zl[1]["treffer"]) / math.log(gitter_b / gitter_n[1])
              if zl[1]["treffer"] > 0 and zl[2]["treffer"] > 0 else None)
        erg["dimension"] = {"zaehlung": zl, "D_plan": D, "D_beschr_96_144": D3}
        erg["spaltung_max"] = max(z["spaltung_max"] for z in zl)
        idx = rng.permutation(len(starts_k))[:nstarts]
        erg["suche"] = nullstellen_suche(name, Hf, starts_k[idx])
        print(f"{name} suche ({time.time() - t0:.1f} s)", flush=True)
        if name == "FKM":
            Kr = rng.uniform(-2 * G0, 2 * G0, size=(2000, 3))
            Er = eig(Hf, Kr)
            erg["spaltung_zufall_max"] = float(np.max(np.maximum(Er[:, 1] - Er[:, 0], Er[:, 3] - Er[:, 2])))
            erg["spaltung_max"] = max(erg["spaltung_max"], erg["spaltung_zufall_max"])
            for key, P in (("dispersion_Xz", G0 * np.array([0, 0, 1.0])), ("dispersion_Xx", G0 * np.array([1.0, 0, 0])),
                           ("dispersion_Xy", G0 * np.array([0, 1.0, 0]))):
                erg[key] = dispersion(Hf, P, d26)
            for P, tag in ((G0 * np.array([0, 0, 1.0]), "E_Xz"), (np.zeros(3), "E_Gamma"), (W_PUNKT, "E_W")):
                erg[tag] = float(np.min(np.abs(eig(Hf, P[None, :]))))
        else:
            erg["dispersion"] = dispersion(Hf, np.zeros(3), d26)
            erg["E_W"] = float(np.min(np.abs(eig(Hf, W_PUNKT[None, :]))))
            erg["E_P_dossier"] = float(np.min(np.abs(eig(Hf, P_DOSSIER[None, :]))))
            erg["E_P_dossier_gefaltet"] = float(np.min(np.abs(eig(Hf, (P_DOSSIER - G0 * np.ones(3))[None, :]))))
            erg["E_X"] = float(np.min(np.abs(eig(Hf, (G0 * np.array([1.0, 0, 0]))[None, :]))))
            if name == "W-D":
                S = schleife_wd()
                Es = np.min(np.abs(eig(Hf, S)), axis=1)
                erg["schleife_anzahl"] = int(len(S))
                erg["schleife_E_max"] = float(np.max(Es)) if len(S) else None
                erg["schleife_punkte_2pi_durch_a"] = S / G0
            dw = np.vstack([d26[[klasse(n) == "110" for n in d26]], fib(20)])
            erg["wortlaut"] = wortlaut(name, Hf, dw)
        erg["laufzeit_s"] = time.time() - t1
        ops[name] = erg
        print(f"{name} fertig ({time.time() - t0:.1f} s)", flush=True)
    out["operatoren"] = ops
    try:
        out["urteile"] = urteile(out)
    except Exception as ex:  # noqa: BLE001
        out["urteile"] = {"fehler": repr(ex)}
    out["laufzeit_s"] = time.time() - t0
    with open(aus, "w") as fh:
        json.dump(js(out), fh, indent=1)
    if rauch:
        def schluessel(d, tiefe=0):
            if isinstance(d, dict) and tiefe < 2:
                return {k: schluessel(v, tiefe + 1) for k, v in d.items()}
            return type(d).__name__
        print(json.dumps(schluessel(js(out))))
    print(f"fertig {time.time() - t0:.1f} s -> {aus}", flush=True)


def bild(pfad, png):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    d = json.load(open(pfad))
    ops = d["operatoren"]
    fig = plt.figure(figsize=(16, 10))
    for i, name in enumerate(("W-D", "W-D+S3", "FKM")):
        ax = fig.add_subplot(2, 3, i + 1, projection="3d")
        P = np.array(ops[name]["suche"]["punkte_in_2pi_durch_a"]).reshape(-1, 3)
        if len(P):
            ax.scatter(P[:, 0], P[:, 1], P[:, 2], s=4, c="tab:red")
        if name == "W-D" and ops[name].get("schleife_punkte_2pi_durch_a"):
            S = np.array(ops[name]["schleife_punkte_2pi_durch_a"])
            ax.plot(S[:, 0], S[:, 1], S[:, 2], "k-", lw=0.8)
        ax.scatter([0], [0], [0], s=30, c="k", marker="*")
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_zlim(-1, 1)
        ax.set_title(f"{name}: Nullstellen ausser Gamma (gefaltet, 2 pi/a)\n"
                     f"verschieden: {ops[name]['suche']['verschiedene_nicht_gamma']}, D = "
                     f"{ops[name]['dimension']['D_plan'] if ops[name]['dimension']['D_plan'] is None else round(ops[name]['dimension']['D_plan'], 2)}",
                     fontsize=9)
    farbe = {"100": "tab:blue", "110": "tab:orange", "111": "tab:green"}
    for i, (name, key) in enumerate((("W-D", "dispersion"), ("W-D+S3", "dispersion"), ("FKM", "dispersion_Xz"))):
        ax = fig.add_subplot(2, 3, 4 + i)
        for z, mark in ((0, "v"), (1, "^")):
            for j, e in enumerate(ops[name][key]["W0"][z]["je_richtung"]):
                ax.plot(j, e["a1"], mark, color=farbe[e["klasse"]], ms=4)
                ax.plot(j, e["a2"], "o", color=farbe[e["klasse"]], ms=3, alpha=0.5)
                ax.plot(j, e["a3"], "s", color=farbe[e["klasse"]], ms=3, mfc="none")
        ax.axhline(0, color="0.5", lw=0.5)
        ax.set_xlabel("Richtung (26), Farbe = Klasse 100/110/111")
        ax.set_title(f"{name}: a1 (Dreieck, lo unten/hi oben), a2 (Punkt), a3 (Quadrat); k in 1/PU", fontsize=9)
    fig.suptitle("DIAMANT-NULLSTELLEN-1: Nullstellen und Dispersion (synthetische Rechnung)")
    fig.tight_layout()
    fig.savefig(png, dpi=100)
    print(f"bild -> {png}", flush=True)


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] in ("rechnen", "rauch"):
        rechnen(sys.argv[2], rauch=(sys.argv[1] == "rauch"))
    elif len(sys.argv) >= 4 and sys.argv[1] == "bild":
        bild(sys.argv[2], sys.argv[3])
    else:
        print(__doc__)
        sys.exit(2)
