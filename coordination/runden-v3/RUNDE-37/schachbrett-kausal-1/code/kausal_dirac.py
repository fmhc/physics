"""SCHACHBRETT-KAUSAL-1 (Runde 38, Code-Agent): Dirac-Feld in 1+1 auf Poisson-Kausalmengen, Hauptbauweise "Eckpaar-Kette".

Kontinuum [M]: (d_t + d_x) psi_R = -i m psi_L + j_R, (d_t - d_x) psi_L = -i m psi_R + j_L; U = t - x, V = t + x (ohne sqrt2).
Umgruppierung des Schachbretts [M, PLAN.md Abschnitt 1]: Eine Zickzack-Bahn, die als L-Laeufer ankommt, ist eindeutig durch
die Kette ihrer L->R-Ecken bestimmt; die R->L-Ecken liegen an den Rechteckecken (U_y, V_z) aufeinanderfolgender Glieder.
Je Eckpaar (-i m/2)^2 dU dV = -(m^2/2) dt dx. Auf der Kausalmenge sind die Eckpaare Elemente (Gewicht 1/rho):
  psi_L(x) = s_L(x) - (m^2/(2 rho)) sum_{y < x} psi_L(y)      (Elemente = L->R-Ecken)
  psi_R(x) = s_R(x) - (m^2/(2 rho)) sum_{y < x} psi_R(y)      (Elemente = R->L-Ecken)
  s_a = Bahnen ohne Element-Ecke, analytisch aus der glatten Quelle:
  s_R(x) = (1/2) int_{-inf}^{V_x} j_R(U_x, V') dV' - (i m/2) int_{J-(x)} j_L dt dx
  s_L(x) = (1/2) int_{-inf}^{U_x} j_L(U', V_x) dU' - (i m/2) int_{J-(x)} j_R dt dx
Das ist Johnstons Rekursion (arXiv:0806.3083 (3.5), (3.31): b = -m^2/rho, a = 1/2) mit der Quelle s_a statt J; dieselbe
Stop-Amplitude -m^2/(2 rho) je Element. Erwartungswert = Kontinuum (Kettenentwicklung, Poisson/Palm) [M].
Punktquelle j_R = delta am Ursprung: s_L = -i m/2 im Zukunftskegel, also psi_L = S_LR = -i m K_Johnston, und
  S_RR (glatt) = (-i m/2) int_0^{V_x} psi_L(U_x, V') dV' = -(m^2/4) V_x + (i m^3/(4 rho)) sum_{y<x} psi_L(y) (V_x - V_y).
Wiederverwendet (unveraendert): kausal_welle.py aus KAUSAL-WELLE-1 (Loeser = CDQ-Rekursion psi = J - (m^2/(2 rho)) C psi,
streuen_kegel = Poisson-Streuung in D = J+(Scheibe r0) geschnitten {t <= tb}). Koordinaten dort: u = U/sqrt2, v = V/sqrt2.

Aufruf (nur ueber kleintest.sh auf der .69):
  kausal_dirac.py paket <rho> <saat_von> <saat_bis> <ausgabeordner> [zeitgrenze_s]
  kausal_dirac.py punkt <rho> <saat_von> <saat_bis> <ausgabeordner> [zeitgrenze_s]
  kausal_dirac.py probe <rho> <saat> <ausgabeordner>
  kausal_dirac.py zeit  <rho> <saat> <ausgabeordner>      (nur Laufzeit und Endlichkeit, keine Feldwerte)
"""
import hashlib
import json
import os
import sys
import time

import numpy as np
from scipy.linalg import solve_triangular
from scipy.special import wofz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kausal_welle as kw  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
SQ2 = np.sqrt(2.0)
M = 1.0
ETA2 = 1.0
PAKETE = [
    {"name": "zitter", "sigma": 1.0, "omega": 0.0, "p": 0.0, "cR": 1.0, "cL": 0.0, "vx": 0.0},
    {"name": "bewegt", "sigma": 4.0, "omega": float(np.cosh(ETA2)), "p": float(np.sinh(ETA2)),
     "cR": float(np.exp(ETA2 / 2) / np.sqrt(2 * np.cosh(ETA2))), "cL": float(np.exp(-ETA2 / 2) / np.sqrt(2 * np.cosh(ETA2))),
     "vx": float(np.tanh(ETA2))},
]
NP = len(PAKETE)
SIG = np.array([P["sigma"] for P in PAKETE])
VX = np.array([P["vx"] for P in PAKETE])
R0 = 4.5 * SIG.max()
T_LAUF = 20.0
TA = 3.0 * SIG
TB = 3.0 * SIG.max() + T_LAUF
W_SCHEIBE = 0.5
N_SCHEIBEN = 40
XB_MIN = -140
XB_N = 280
PRUEF_DT = (0.0, 10.0, 20.0)
PROFIL_J = np.arange(-10, 11)
# Punktquelle (Propagator): Pruefpunkte wie KAUSAL-WELLE-1, Rapiditaeten beidseitig (R/L unsymmetrisch)
TAUS = np.array([0.5, 1.0, 2.0, 3.0, 5.0, 8.0, 12.0, 16.0])
ZETAS = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
T_PUNKT = 25.0


def I_int(t, W, s):
    """int_{-inf}^t exp(-t'^2/(2 s^2) - i W t') dt' (aus KAUSAL-WELLE-1 kontinuum.py, dort gegen Quadratur geprueft)."""
    t = np.asarray(t, dtype=float)
    W = np.asarray(W, dtype=float)
    with np.errstate(all="ignore"):
        pre = s * np.sqrt(np.pi / 2.0) * np.exp(-t ** 2 / (2 * s * s) - 1j * W * t)
        a = pre * wofz((W * s * s - 1j * t) / (s * SQ2))
        b = s * np.sqrt(2 * np.pi) * np.exp(-W ** 2 * s * s / 2.0) - pre * wofz((1j * t - W * s * s) / (s * SQ2))
    return np.where(t <= 0, a, b)


def quellen_paket(u, v):
    """s_R, s_L je Paket an Punkten (u, v) [Koordinaten mit 1/sqrt2]; Spalten (2c, 2c+1) = (s_R, s_L) von Paket c.
    j_a = c_a exp(-(t^2 + x^2)/(2 sigma^2)) exp(-i(omega t - p x)) = c_a f(U; A) f(V; B), f(y; W) = exp(-y^2/(4 sigma^2) - i W y),
    A = (omega + p)/2, B = (omega - p)/2; F(Y; W) = int_{-inf}^Y f = I_int(Y, W, sqrt2 sigma); int_{J-(x)} j dt dx = (1/2) c F F."""
    Ul = SQ2 * np.asarray(u, dtype=float)
    Vl = SQ2 * np.asarray(v, dtype=float)
    out = np.zeros((Ul.size, 2 * NP), dtype=np.complex128)
    for c, P in enumerate(PAKETE):
        s = P["sigma"]
        A = 0.5 * (P["omega"] + P["p"])
        B = 0.5 * (P["omega"] - P["p"])
        fU = np.exp(-Ul * Ul / (4 * s * s) - 1j * A * Ul)
        fV = np.exp(-Vl * Vl / (4 * s * s) - 1j * B * Vl)
        FU = I_int(Ul, A, SQ2 * s)
        FV = I_int(Vl, B, SQ2 * s)
        FF = FU * FV
        out[:, 2 * c] = 0.5 * (P["cR"] * fU * FV - 0.5j * M * P["cL"] * FF)
        out[:, 2 * c + 1] = 0.5 * (P["cL"] * FU * fV - 0.5j * M * P["cR"] * FF)
    return out


def pruefpunkte_paket():
    """(NP, 24, 2) Feld (t, x): 3 Pruefpunkte (t = ta, ta + 10, ta + 20; x = vx t), dann 21 Profilpunkte bei ta + 20."""
    out = np.zeros((NP, 3 + PROFIL_J.size, 2))
    for c in range(NP):
        for i, dt in enumerate(PRUEF_DT):
            t = TA[c] + dt
            out[c, i] = (t, VX[c] * t)
        tb = TA[c] + T_LAUF
        out[c, 3:, 0] = tb
        out[c, 3:, 1] = VX[c] * tb + 2.0 * PROFIL_J
    return out


def zuschauer_summen(L, ut, vt):
    """sum_{y < x} PSI(y) (alle Spalten) und sum PSI(y) (v_x - v_y) fuer einen Punkt x ausserhalb der Menge (Palm)."""
    k = np.searchsorted(L.U, ut)
    m = L.V[:k] < vt
    P = L.PSI[:k][m]
    return P.sum(axis=0), (P * (vt - L.V[:k][m])[:, None]).sum(axis=0)


def messen(L, rho):
    """Summen je (Paket, Scheibe, x-Klasse relativ zu vx t): |psi_R|^2, |psi_L|^2, x (|psi_R|^2 + |psi_L|^2), Zahl."""
    t = (L.U + L.V) / SQ2
    x = (L.V - L.U) / SQ2
    out = np.zeros((NP, N_SCHEIBEN, XB_N, 4))
    nb = N_SCHEIBEN * XB_N
    for c in range(NP):
        k = np.floor((t - TA[c]) / W_SCHEIBE).astype(np.int64)
        d = x - VX[c] * t
        j = np.floor(d).astype(np.int64) - XB_MIN
        ok = (k >= 0) & (k < N_SCHEIBEN) & (j >= 0) & (j < XB_N)
        idx = k[ok] * XB_N + j[ok]
        pR = L.PSI[ok, 2 * c]
        pL = L.PSI[ok, 2 * c + 1]
        wR = pR.real ** 2 + pR.imag ** 2
        wL = pL.real ** 2 + pL.imag ** 2
        out[c, :, :, 0] = np.bincount(idx, weights=wR, minlength=nb).reshape(N_SCHEIBEN, XB_N)
        out[c, :, :, 1] = np.bincount(idx, weights=wL, minlength=nb).reshape(N_SCHEIBEN, XB_N)
        out[c, :, :, 2] = np.bincount(idx, weights=(wR + wL) * x[ok], minlength=nb).reshape(N_SCHEIBEN, XB_N)
        out[c, :, :, 3] = np.bincount(idx, minlength=nb).reshape(N_SCHEIBEN, XB_N)
    return out


def loesen_paket(rho, rng):
    U, V = kw.streuen_kegel(rng, rho, R0, TB)
    SRC = quellen_paket(U, V)
    L = kw.Loeser(U, V, rho, lambda lo, hi: SRC[lo:hi], 2 * NP)
    L.loesen()
    del SRC
    return L


def lauf_paket(rho, saat):
    t0 = time.time()
    rng = np.random.default_rng(np.random.SeedSequence([20261004, 38, 81, int(rho), int(saat)]))
    L = loesen_paket(rho, rng)
    t1 = time.time()
    summen = messen(L, rho)
    pp = pruefpunkte_paket()
    psi_p = np.zeros((NP, pp.shape[1], 2), dtype=np.complex128)
    for c in range(NP):
        for i in range(pp.shape[1]):
            tt, xx = pp[c, i]
            ut, vt = (tt - xx) / SQ2, (tt + xx) / SQ2
            s_x = quellen_paket(np.array([ut]), np.array([vt]))[0]
            S0, _ = zuschauer_summen(L, ut, vt)
            psi_p[c, i, 0] = s_x[2 * c] - (M * M / (2.0 * rho)) * S0[2 * c]
            psi_p[c, i, 1] = s_x[2 * c + 1] - (M * M / (2.0 * rho)) * S0[2 * c + 1]
    t2 = time.time()
    kopf = {"modus": "paket", "rho": rho, "saat": saat, "N": int(L.U.size), "r0": R0, "tb": TB,
            "zeit_loesen_s": round(t1 - t0, 2), "zeit_messen_s": round(t2 - t1, 2), "zeit_gesamt_s": round(t2 - t0, 2),
            "max_abs_psi": float(np.abs(L.PSI).max()), "endlich": bool(np.isfinite(L.PSI).all()),
            "skript_sha256": SKRIPT_SHA, "kausal_welle_sha256": kw.SKRIPT_SHA, "numpy": np.__version__,
            "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    return kopf, summen, psi_p


def streuen_punkt(rng, rho, Tp):
    Lk = SQ2 * Tp
    n = rng.poisson(rho * Lk * Lk / 2.0)
    a = rng.random(n) * Lk
    b = rng.random(n) * Lk
    f = a + b > Lk
    a[f] = Lk - a[f]
    b[f] = Lk - b[f]
    o = np.argsort(a, kind="stable")
    return np.ascontiguousarray(a[o]), np.ascontiguousarray(b[o])


def lauf_punkt(rho, saat):
    """R-Punktquelle am Ursprung (kein Element). psi_L an Elementen per Rekursion; S_LR, S_RR (glatt) an Zuschauern."""
    t0 = time.time()
    rng = np.random.default_rng(np.random.SeedSequence([20261004, 38, 82, int(rho), int(saat)]))
    U, V = streuen_punkt(rng, rho, T_PUNKT)
    SRC = np.full((U.size, 1), -0.5j * M, dtype=np.complex128)
    L = kw.Loeser(U, V, rho, lambda lo, hi: SRC[lo:hi], 1)
    L.loesen()
    slr = np.zeros((ZETAS.size, TAUS.size), dtype=np.complex128)
    srr = np.zeros((ZETAS.size, TAUS.size), dtype=np.complex128)
    for a, z in enumerate(ZETAS):
        for b, ta in enumerate(TAUS):
            tt, xx = ta * np.cosh(z), ta * np.sinh(z)
            ut, vt = (tt - xx) / SQ2, (tt + xx) / SQ2
            S0, S1 = zuschauer_summen(L, ut, vt)
            slr[a, b] = -0.5j * M - (M * M / (2.0 * rho)) * S0[0]
            srr[a, b] = -(M * M / 4.0) * (SQ2 * vt) + (1j * M ** 3 / (4.0 * rho)) * SQ2 * S1[0]
    kopf = {"modus": "punkt", "rho": rho, "saat": saat, "N": int(U.size), "taus": TAUS.tolist(), "zetas": ZETAS.tolist(),
            "SLR_re": slr.real.tolist(), "SLR_im": slr.imag.tolist(), "SRR_re": srr.real.tolist(), "SRR_im": srr.imag.tolist(),
            "max_abs_psi": float(np.abs(L.PSI).max()), "endlich": bool(np.isfinite(L.PSI).all()),
            "zeit_gesamt_s": round(time.time() - t0, 2), "skript_sha256": SKRIPT_SHA, "kausal_welle_sha256": kw.SKRIPT_SHA,
            "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    return kopf


def gl_quellen_probe(tt, xx, n=400):
    """Gegenprobe der analytischen s_a: direkte Gauss-Legendre-Quadratur (Strahl 1D, Vergangenheit 2D)."""
    g, wg = np.polynomial.legendre.leggauss(n)
    Ux, Vx = tt - xx, tt + xx
    out = np.zeros(2 * NP, dtype=np.complex128)
    for c, P in enumerate(PAKETE):
        s = P["sigma"]
        om, p = P["omega"], P["p"]
        lo = -14.0 * s

        def j_tx(T, X):
            return np.exp(-(T * T + X * X) / (2 * s * s) - 1j * (om * T - p * X))
        # Strahlintegrale (1/2) int dV' bzw. dU' (Laenge in V bzw. U), Parameter y in [lo, Vx] bzw. [lo, Ux]
        b = Vx
        yy = 0.5 * (b - lo) * g + 0.5 * (b + lo)
        ww = 0.5 * (b - lo) * wg
        jR_strahl = np.sum(ww * j_tx((Ux + yy) / 2, (yy - Ux) / 2))
        b = Ux
        yy = 0.5 * (b - lo) * g + 0.5 * (b + lo)
        ww = 0.5 * (b - lo) * wg
        jL_strahl = np.sum(ww * j_tx((yy + Vx) / 2, (Vx - yy) / 2))
        # Vergangenheit: int dt dx = (1/2) int dU dV ueber U < Ux, V < Vx
        uu = 0.5 * (Ux - lo) * g + 0.5 * (Ux + lo)
        wu = 0.5 * (Ux - lo) * wg
        vv = 0.5 * (Vx - lo) * g + 0.5 * (Vx + lo)
        wv = 0.5 * (Vx - lo) * wg
        UU, VV = np.meshgrid(uu, vv, indexing="ij")
        flaeche = 0.5 * np.einsum("i,ij,j->", wu, j_tx((UU + VV) / 2, (VV - UU) / 2), wv)
        out[2 * c] = 0.5 * P["cR"] * jR_strahl - 0.5j * M * P["cL"] * flaeche
        out[2 * c + 1] = 0.5 * P["cL"] * jL_strahl - 0.5j * M * P["cR"] * flaeche
    return out


def lauf_probe(rho, saat):
    """Codeprobe: CDQ gegen dichte Loesung, Zuschauer gegen Maskensumme, analytische Quellen gegen Quadratur."""
    rng = np.random.default_rng(np.random.SeedSequence([20261004, 38, 83, int(rho), int(saat)]))
    U, V = kw.streuen_kegel(rng, rho, 9.0, 8.0)
    SRC = quellen_paket(U, V)
    L = kw.Loeser(U, V, rho, lambda lo, hi: SRC[lo:hi], 2 * NP)
    L.loesen()
    N = U.size
    A = ((U[None, :] < U[:, None]) & (V[None, :] < V[:, None])).astype(np.float64)
    a = M ** 2 / (2.0 * rho)
    psi = solve_triangular(np.eye(N) + a * A, SRC, lower=True)
    d_psi = float(np.abs(psi - L.PSI).max() / np.abs(psi).max())
    zz = []
    for (tt, xx) in [(3.0, 0.5), (6.0, -2.0), (7.5, 1.0)]:
        ut, vt = (tt - xx) / SQ2, (tt + xx) / SQ2
        m = (U < ut) & (V < vt)
        S0, S1 = zuschauer_summen(L, ut, vt)
        ref0 = psi[m].sum(axis=0)
        ref1 = (psi[m] * (vt - V[m])[:, None]).sum(axis=0)
        zz.append(float(np.max(np.abs(S0 - ref0)) / max(np.abs(ref0).max(), 1e-300)))
        zz.append(float(np.max(np.abs(S1 - ref1)) / max(np.abs(ref1).max(), 1e-300)))
    qq = []
    for (tt, xx) in [(0.0, 0.0), (2.0, 1.0), (5.0, -3.0), (12.0, 7.0), (20.0, 15.0)]:
        an = quellen_paket(np.array([(tt - xx) / SQ2]), np.array([(tt + xx) / SQ2]))[0]
        gl = gl_quellen_probe(tt, xx)
        qq.append(float(np.max(np.abs(an - gl)) / max(np.abs(gl).max(), 1e-300)))
    return {"modus": "probe", "rho": rho, "saat": saat, "N": int(N), "rel_abw_psi": d_psi,
            "rel_abw_zuschauer_max": float(max(zz)), "quellen_analytisch_gegen_quadratur_max": float(max(qq)),
            "quellen_einzeln": qq, "skript_sha256": SKRIPT_SHA,
            "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}


def main():
    modus = sys.argv[1]
    rho = float(sys.argv[2])
    if modus in ("probe", "zeit"):
        saat, ordner = int(sys.argv[3]), sys.argv[4]
        os.makedirs(ordner, exist_ok=True)
        if modus == "probe":
            kopf = lauf_probe(rho, saat)
        else:
            t0 = time.time()
            rng = np.random.default_rng(np.random.SeedSequence([20261004, 38, 81, int(rho), int(saat)]))
            L = loesen_paket(rho, rng)
            t1 = time.time()
            messen(L, rho)
            kopf = {"modus": "zeit", "rho": rho, "saat": saat, "N": int(L.U.size), "zeit_loesen_s": round(t1 - t0, 2),
                    "zeit_messen_s": round(time.time() - t1, 2), "endlich": bool(np.isfinite(L.PSI).all()),
                    "skript_sha256": SKRIPT_SHA, "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        with open(os.path.join(ordner, f"{modus}-r{int(rho)}-s{saat}.json"), "w") as fh:
            json.dump(kopf, fh, indent=1)
        print(json.dumps(kopf))
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
        if modus == "paket":
            kopf, summen, psi_p = lauf_paket(rho, saat)
            np.savez_compressed(os.path.join(ordner, f"paket-r{int(rho)}-s{saat}.npz"), summen=summen, psi_p=psi_p,
                                pruefpunkte=pruefpunkte_paket())
            with open(os.path.join(ordner, f"paket-r{int(rho)}-s{saat}.json"), "w") as fh:
                json.dump(kopf, fh, indent=1)
            info = kopf
        elif modus == "punkt":
            kopf = lauf_punkt(rho, saat)
            with open(os.path.join(ordner, f"punkt-r{int(rho)}-s{saat}.json"), "w") as fh:
                json.dump(kopf, fh, indent=1)
            info = {k: kopf[k] for k in ("modus", "rho", "saat", "N", "endlich", "zeit_gesamt_s")}
        else:
            raise SystemExit("unbekannter Modus")
        dauer_max = max(dauer_max, time.time() - ts)
        print(json.dumps({k: info[k] for k in ("modus", "rho", "saat", "N", "endlich", "zeit_gesamt_s")}), flush=True)


if __name__ == "__main__":
    main()
