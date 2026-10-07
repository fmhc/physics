"""KAUSAL-WELLE-4D (Runde 38, Code-Agent): massive Wellenpakete auf 3+1-Kausalmengen, Johnstons retardierter Propagator.

Quelle [S]: S. Johnston, "Particle propagators on discrete spacetime", CQG 25 (2008) 202001, arXiv:0806.3083v2:
(2.2) (A_R)_ij = 1 wenn v_i -<* v_j (Link); (3.2) Phi = a A_R (Summe ueber Pfade); (3.5) K = I + Phi (I - b Phi)^-1;
(3.33) V = (pi/24) tau^4; (3.44) a = sqrt(rho)/(2 pi sqrt 6), b = -m^2/rho; (3.25) Kontinuum
K_m = (1/2pi) delta(tau^2) - (m/4pi) J1(m tau)/tau im Vorwaertskegel.

Feld (ohne Konventionsterm I): phi(x) = (1/rho) sum_y (K - I)(y, x) J(y) = (a/rho) (L^T psi)(x),
psi = J - (a m^2/rho) L^T psi (Vorwaertsrekursion in Zeitordnung, L^T streng untere Dreiecksmatrix).

Gebiet D = J+(B) geschnitten J-(top): B = 4-Kugel vom Radius R_S um 0 (Traeger der gekappten Quelle),
top = (T_TOP, 0, 0, 0). D ist kausal konvex; jede Kette von der Quelle zu einem Punkt von D liegt in D, Links zwischen
Punkten von D sind dieselben wie in einer unbegrenzten Streuung. phi ist an jedem Punkt von D exakt.

Kausalrelation: y vor x, wenn t_x - t_y >= |x - y| (t_x > t_y). Links: L = C und nicht (C C > 0), float32-GEMM in Bloecken
(nur obere Dreiecksbloecke, Zwischenindex auf [I0, J1) beschraenkt).

Aufruf (nur ueber kleintest.sh auf der .69):
  kausal4d.py zeit  <N_erwartet> <ausgabeordner>
  kausal4d.py feld  <rho> <saat_von> <saat_bis> <ausgabeordner> [zeitgrenze_s]
  kausal4d.py probe <rho> <saat> <ausgabeordner>
"""
import hashlib
import json
import os
import resource
import sys
import time

import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import spsolve_triangular

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
MASSE = 1.0
SIGMA = 1.0
R_S = 3.5
T_TOP = 5.0
ETAS = (0.0, 0.5)
NC = len(ETAS)
OM = np.cosh(np.array(ETAS)) * MASSE
PP = np.sinh(np.array(ETAS)) * MASSE
VN = np.tanh(np.array(ETAS))
SQ2 = np.sqrt(2.0)
# Pruefpunkte: je Konfiguration t in PRUEF_T; Lagen A = Paketmitte (0, 0, v t), B = (0.6, 0, v t), C = (0, 0, v t - 0.6)
PRUEF_T = (2.0, 2.6, 3.2)
VERSATZ = 0.6
# Profil (nur Bild): t = 3.2, x = y = 0, z = -1.6 ... 1.6 (Schritt 0.2)
PROFIL_T = 3.2
PROFIL_Z = np.round(np.arange(-8, 9) * 0.2, 10)
# Zeitscheiben fuer die Norm: [2.0, 2.5), [2.5, 3.0), [3.0, 3.5), [3.5, 4.0); Radialklassen 0.25 bis r = 3
SCHEIBE_T0 = 2.0
SCHEIBE_W = 0.5
N_SCHEIBEN = 4
R_KLASSE = 0.25
N_RKLASSEN = 12
# Linkzahl je Element nach Zeitklassen (beschreibend): Klassen der Breite 0.5 von -R_S bis T_TOP
LZ_T0 = -R_S
LZ_W = 0.5
LZ_N = int(round((T_TOP - LZ_T0) / LZ_W))
B_GEMM = 2048
B_BAU = 512


def a_hop(rho):
    return np.sqrt(rho) / (2.0 * np.pi * np.sqrt(6.0))


def f_unten(r):
    """Untere Grenze t >= f(r) von J+(B) (B = 4-Kugel Radius R_S um 0)."""
    r = np.asarray(r, dtype=float)
    k = R_S / SQ2
    return np.where(r <= k, -np.sqrt(np.maximum(R_S * R_S - r * r, 0.0)), r - SQ2 * R_S)


def in_D(t, r):
    return (t >= f_unten(r)) & (t <= T_TOP - r)


def r_max_D():
    return 0.5 * (T_TOP + SQ2 * R_S)


def zylinder_volumen():
    return (T_TOP + R_S) * (4.0 * np.pi / 3.0) * r_max_D() ** 3


def pruefpunkte():
    """(NC, 18 + 17, 4) Felder (t, x, y, z): 9 Pruefpunkte je Konfiguration (3 Zeiten x 3 Lagen), dann 17 Profilpunkte."""
    n_p = len(PRUEF_T) * 3
    out = np.zeros((NC, n_p + PROFIL_Z.size, 4))
    for c in range(NC):
        i = 0
        for t in PRUEF_T:
            z0 = VN[c] * t
            for (x, y, z) in [(0.0, 0.0, z0), (VERSATZ, 0.0, z0), (0.0, 0.0, z0 - VERSATZ)]:
                out[c, i] = (t, x, y, z)
                i += 1
        out[c, n_p:, 0] = PROFIL_T
        out[c, n_p:, 3] = PROFIL_Z
    return out


def streuen(rng, rho):
    """Poisson-Streuung in D (Ausduennung aus dem Zylinder [-R_S, T_TOP] x Kugel r_max); nach t sortiert."""
    rm = r_max_D()
    n = rng.poisson(rho * zylinder_volumen())
    t = -R_S + (T_TOP + R_S) * rng.random(n)
    r = rm * rng.random(n) ** (1.0 / 3.0)
    mu = 2.0 * rng.random(n) - 1.0
    ph = 2.0 * np.pi * rng.random(n)
    s = np.sqrt(1.0 - mu * mu)
    X = np.stack([r * s * np.cos(ph), r * s * np.sin(ph), r * mu], axis=1)
    ok = in_D(t, r)
    t = t[ok]
    X = X[ok]
    o = np.argsort(t, kind="stable")
    return np.ascontiguousarray(t[o]), np.ascontiguousarray(X[o])


def kausalmatrix(t, X):
    """C[i, j] = 1 (float32), wenn i vor j (t sortiert, also streng obere Dreiecksmatrix)."""
    N = t.size
    C = np.zeros((N, N), dtype=np.float32)
    for i0 in range(0, N, B_BAU):
        i1 = min(i0 + B_BAU, N)
        dt = t[None, i0:] - t[i0:i1, None]
        d2 = np.zeros_like(dt)
        for k in range(3):
            d2 += (X[None, i0:, k] - X[i0:i1, None, k]) ** 2
        C[i0:i1, i0:] = ((dt > 0.0) & (dt * dt >= d2)).astype(np.float32)
    return C


def links_gemm(C, B=B_GEMM):
    """Links (i, j) mit C[i, j] = 1 und (C C)[i, j] = 0; Bloecke I <= J, Zwischenindex in [I0, J1)."""
    N = C.shape[0]
    zeilen = []
    spalten = []
    for I0 in range(0, N, B):
        I1 = min(I0 + B, N)
        for J0 in range(I0, N, B):
            J1 = min(J0 + B, N)
            Cij = C[I0:I1, J0:J1]
            if not Cij.any():
                continue
            P = C[I0:I1, I0:J1] @ C[I0:J1, J0:J1]
            r, c = np.nonzero((Cij > 0.5) & (P < 0.5))
            zeilen.append(r + I0)
            spalten.append(c + J0)
    return np.concatenate(zeilen), np.concatenate(spalten)


def quelle(t, X):
    """J (N, NC) komplex, gekappt auf die 4-Kugel R_S."""
    r2 = (t * t + (X * X).sum(axis=1))[:, None]
    ph = -r2 / (2.0 * SIGMA ** 2) - 1j * (OM[None, :] * t[:, None] - PP[None, :] * X[:, 2:3])
    J = np.exp(ph)
    J *= (r2 <= R_S * R_S)
    return J


def loesen(Lt, J, rho):
    """(I + alpha Lt) psi = J, alpha = a m^2/rho; Real- und Imaginaerteil als Spalten."""
    a = a_hop(rho)
    alpha = a * MASSE ** 2 / rho
    N = J.shape[0]
    A = (sps.identity(N, format="csr") + alpha * Lt).tocsr()
    b = np.concatenate([J.real, J.imag], axis=1)
    x = spsolve_triangular(A, b, lower=True)
    psi = x[:, :NC] + 1j * x[:, NC:]
    phi = (a / rho) * (Lt @ psi)
    return psi, phi


def zuschauer(C, t, X, psi, rho, pp):
    """phi an Punkten ausserhalb der Menge (Palm-Lesart): (a/rho) sum ueber die Links des Punktes in die Menge."""
    a = a_hop(rho)
    P = pp.reshape(-1, 4)
    dt = P[None, :, 0] - t[:, None]
    d2 = ((P[None, :, 1:] - X[:, None, :]) ** 2).sum(axis=2)
    Pm = ((dt > 0.0) & (dt * dt >= d2)).astype(np.float32)          # (N, n): y in der Vergangenheit des Punktes
    S = C @ Pm                                                        # Zahl der Nachfolger von y in dieser Vergangenheit
    Lk = (Pm > 0.5) & (S < 0.5)                                       # Links y -<* Punkt
    out = np.zeros((pp.shape[0], pp.shape[1]), dtype=np.complex128)
    nl = Lk.sum(axis=0).reshape(pp.shape[0], pp.shape[1])
    for c in range(pp.shape[0]):
        n = pp.shape[1]
        sel = Lk[:, c * n:(c + 1) * n]
        out[c] = (a / rho) * (sel.T.astype(np.float64) @ psi[:, c])
    return out, nl


def messen(t, X, phi, rho):
    """Summen |phi|^2 je (Konfiguration, Scheibe, Radialklasse) und Punktzahlen; Norm n_k = Summe/(rho w)."""
    k = np.floor((t - SCHEIBE_T0) / SCHEIBE_W).astype(np.int64)
    r = np.sqrt((X * X).sum(axis=1))
    j = np.floor(r / R_KLASSE).astype(np.int64)
    ok = (k >= 0) & (k < N_SCHEIBEN) & (j >= 0) & (j < N_RKLASSEN)
    idx = k[ok] * N_RKLASSEN + j[ok]
    nb = N_SCHEIBEN * N_RKLASSEN
    out = np.zeros((NC, N_SCHEIBEN, N_RKLASSEN, 2))
    for c in range(NC):
        w2 = np.abs(phi[ok, c]) ** 2
        out[c, :, :, 0] = np.bincount(idx, weights=w2, minlength=nb).reshape(N_SCHEIBEN, N_RKLASSEN)
        out[c, :, :, 1] = np.bincount(idx, minlength=nb).reshape(N_SCHEIBEN, N_RKLASSEN)
    return out


def linkzahl_zeitklassen(t, Lt):
    """Vergangenheitslinks je Element, summiert nach Zeitklassen; dazu Elementzahl je Klasse."""
    grad = np.asarray(Lt.sum(axis=1)).ravel()
    k = np.clip(np.floor((t - LZ_T0) / LZ_W).astype(np.int64), 0, LZ_N - 1)
    return (np.bincount(k, weights=grad, minlength=LZ_N).tolist(), np.bincount(k, minlength=LZ_N).tolist())


def rng_feld(rho, saat):
    return np.random.default_rng(np.random.SeedSequence([20261004, 38, 81, int(round(rho * 1000)), int(saat)]))


def lauf_feld(rho, saat):
    t0 = time.time()
    rng = rng_feld(rho, saat)
    t, X = streuen(rng, rho)
    N = t.size
    t1 = time.time()
    C = kausalmatrix(t, X)
    t2 = time.time()
    zi, sp = links_gemm(C)
    t3 = time.time()
    Lt = sps.csr_matrix((np.ones(zi.size), (sp, zi)), shape=(N, N))   # Lt[j, i] = 1, wenn i -<* j
    J = quelle(t, X)
    psi, phi = loesen(Lt, J, rho)
    t4 = time.time()
    pp = pruefpunkte()
    phi_p, nl_p = zuschauer(C, t, X, psi, rho, pp)
    summen = messen(t, X, phi, rho)
    lz_sum, lz_n = linkzahl_zeitklassen(t, Lt)
    t5 = time.time()
    kopf = {"modus": "feld", "rho": rho, "saat": saat, "N": int(N), "L": int(zi.size), "L_je_N": zi.size / N,
            "relationen": float(C.sum(dtype=np.float64)), "linkzahl_zeitklassen_summe": lz_sum,
            "linkzahl_zeitklassen_n": lz_n, "zeit_streuen_s": round(t1 - t0, 2), "zeit_kausal_s": round(t2 - t1, 2),
            "zeit_links_s": round(t3 - t2, 2), "zeit_loesen_s": round(t4 - t3, 2), "zeit_messen_s": round(t5 - t4, 2),
            "zeit_gesamt_s": round(t5 - t0, 2), "max_abs_psi": float(np.abs(psi).max()),
            "max_abs_phi": float(np.abs(phi).max()), "endlich": bool(np.isfinite(phi).all() and np.isfinite(phi_p).all()),
            "links_zuschauer": nl_p.tolist(), "maxrss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
            "skript_sha256": SKRIPT_SHA, "numpy": np.__version__,
            "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    return kopf, summen, phi_p


def lauf_zeit(n_erw, ordner):
    rho = n_erw / volumen_D_grob()
    rng = np.random.default_rng(np.random.SeedSequence([20261004, 38, 99, int(n_erw)]))
    t0 = time.time()
    t, X = streuen(rng, rho)
    t1 = time.time()
    C = kausalmatrix(t, X)
    t2 = time.time()
    zi, sp = links_gemm(C)
    t3 = time.time()
    kopf = {"modus": "zeit", "N_erwartet": n_erw, "rho": rho, "N": int(t.size), "L": int(zi.size),
            "L_je_N": zi.size / t.size, "zeit_streuen_s": round(t1 - t0, 2), "zeit_kausal_s": round(t2 - t1, 2),
            "zeit_links_s": round(t3 - t2, 2), "maxrss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
            "skript_sha256": SKRIPT_SHA, "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    return kopf


def volumen_D_grob(n=4000):
    """Volumen von D (Mittelpunktregel in t, analytisch in r); nur fuer die Wahl von rho im Zeitmodus."""
    tt = -R_S + (T_TOP + R_S) * (np.arange(n) + 0.5) / n
    k = R_S / SQ2
    rp = np.where(tt <= -k, np.sqrt(np.maximum(R_S ** 2 - tt ** 2, 0.0)), tt + SQ2 * R_S)
    rd = np.minimum(rp, T_TOP - tt)
    return float((4.0 * np.pi / 3.0) * (rd ** 3).sum() * (T_TOP + R_S) / n)


def lauf_probe(rho, saat):
    """Codeprobe: GEMM-Links gegen dichte Rechnung, Rekursion gegen dichte Loesung und Reihe, Zuschauer gegen Schleife."""
    rng = np.random.default_rng(np.random.SeedSequence([20261004, 38, 83, int(round(rho * 1000)), int(saat)]))
    t, X = streuen(rng, rho)
    N = t.size
    C = kausalmatrix(t, X)
    zi, sp = links_gemm(C, B=256)
    Ld = np.zeros((N, N))
    Ld[zi, sp] = 1.0
    C64 = C.astype(np.float64)
    Lref = ((C64 > 0.5) & ((C64 @ C64) < 0.5)).astype(np.float64)
    # unabhaengige Kausalpruefung aus den Koordinaten
    dt = t[None, :] - t[:, None]
    d2 = ((X[None, :, :] - X[:, None, :]) ** 2).sum(axis=2)
    Cref = ((dt > 0) & (dt * dt >= d2)).astype(np.float64)
    links_ok = bool(np.array_equal(Ld, Lref))
    kausal_ok = bool(np.array_equal(C64, Cref))
    Lt = sps.csr_matrix((np.ones(zi.size), (sp, zi)), shape=(N, N))
    J = quelle(t, X)
    psi, phi = loesen(Lt, J, rho)
    a = a_hop(rho)
    alpha = a * MASSE ** 2 / rho
    Ltd = Lref.T
    psi_d = np.linalg.solve(np.eye(N) + alpha * Ltd, J)
    phi_d = (a / rho) * (Ltd @ psi_d)
    reihe = np.zeros_like(J)
    term = J.copy()
    for _ in range(200):
        reihe += term
        term = -alpha * (Ltd @ term)
    phi_r = (a / rho) * (Ltd @ reihe)
    d_phi = float(np.abs(phi - phi_d).max() / np.abs(phi_d).max())
    d_reihe = float(np.abs(phi_r - phi_d).max() / np.abs(phi_d).max())
    # Zuschauer: Schleife ueber Elemente der Vergangenheit (maximale Elemente)
    pp = pruefpunkte()[:, :9]
    phi_p, _ = zuschauer(C, t, X, psi, rho, pp)
    zz = []
    for c in range(NC):
        for i in range(pp.shape[1]):
            tt, xx, yy, z3 = pp[c, i]
            past = np.nonzero((tt - t > 0) & ((tt - t) ** 2 >= (xx - X[:, 0]) ** 2 + (yy - X[:, 1]) ** 2 + (z3 - X[:, 2]) ** 2))[0]
            s = 0.0 + 0.0j
            for y in past:
                if not np.any(Cref[y, past] > 0.5):
                    s += psi_d[y, c]
            ref = (a / rho) * s
            zz.append(abs(phi_p[c, i] - ref) / max(abs(ref), 1e-300))
    return {"modus": "probe", "rho": rho, "saat": saat, "N": int(N), "L": int(zi.size), "links_gleich_dicht": links_ok,
            "kausal_gleich_koordinaten": kausal_ok, "rel_abw_phi_rekursion_dicht": d_phi, "rel_abw_reihe_dicht": d_reihe,
            "rel_abw_zuschauer_max": float(max(zz)), "skript_sha256": SKRIPT_SHA,
            "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}


def main():
    modus = sys.argv[1]
    if modus == "zeit":
        n_erw, ordner = int(sys.argv[2]), sys.argv[3]
        os.makedirs(ordner, exist_ok=True)
        kopf = lauf_zeit(n_erw, ordner)
        with open(os.path.join(ordner, f"zeit-n{n_erw}.json"), "w") as fh:
            json.dump(kopf, fh, indent=1)
        print(json.dumps(kopf), flush=True)
        return
    rho = float(sys.argv[2])
    if modus == "probe":
        saat, ordner = int(sys.argv[3]), sys.argv[4]
        os.makedirs(ordner, exist_ok=True)
        kopf = lauf_probe(rho, saat)
        with open(os.path.join(ordner, f"probe-r{rho:g}-s{saat}.json"), "w") as fh:
            json.dump(kopf, fh, indent=1)
        print(json.dumps(kopf), flush=True)
        return
    s0, s1, ordner = int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    grenze = float(sys.argv[6]) if len(sys.argv) > 6 else 540.0
    os.makedirs(ordner, exist_ok=True)
    start = time.time()
    dauer_max = 0.0
    for saat in range(s0, s1 + 1):
        if time.time() - start + 1.3 * dauer_max > grenze:
            print(json.dumps({"abbruch_vor_saat": saat, "grund": "zeitgrenze", "verstrichen_s": round(time.time() - start, 1)}))
            break
        ts = time.time()
        kopf, summen, phi_p = lauf_feld(rho, saat)
        np.savez_compressed(os.path.join(ordner, f"feld-r{rho:g}-s{saat}.npz"), summen=summen, phi_p=phi_p,
                            pruefpunkte=pruefpunkte())
        with open(os.path.join(ordner, f"feld-r{rho:g}-s{saat}.json"), "w") as fh:
            json.dump(kopf, fh, indent=1)
        dauer_max = max(dauer_max, time.time() - ts)
        print(json.dumps({k: kopf[k] for k in kopf if k not in ("links_zuschauer", "linkzahl_zeitklassen_summe",
                                                                  "linkzahl_zeitklassen_n")}), flush=True)


if __name__ == "__main__":
    main()
