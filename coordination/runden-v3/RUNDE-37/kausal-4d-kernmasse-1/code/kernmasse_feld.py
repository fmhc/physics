"""KAUSAL-4D-KERNMASSE-1 (Runde 41, Code-Agent), Teil B: Felder mit der Masse im nichtlokalen Kern (VK) neben den
Pfadsummen mit der Masse ausserhalb (VJ, V0, V00 aus KAUSAL-4D-SCHICHT-2) auf derselben Streuung.

Baut auf kausal4d.py (KAUSAL-WELLE-4D) und schicht2_feld.py (KAUSAL-4D-SCHICHT-2), beide unveraendert importiert.
- VJ, V0, V00: Rechenweg von schicht2_feld.lauf_feld_v (gleiche Schicht-Indizes in gleicher Reihenfolge, gleiche
  Funktionen sf.gewichte, sf.loesen_v, sf.zuschauer_v, kd.messen), also bitgleich mit SCHICHT-2 auf derselben Saat.
- VK (Masse im Kern, VORAB.md Abschnitt 2 und 3): ein Schritt, kein Halt (b = 0),
      phi_K(x) = (1/rho) sum_{y vor x} W(y, x) J(y),   W = a [n = 0] + t(n),   n = Zahl der Elemente in I(y, x),
  t(n) = T(sigma_n), sigma_n = sqrt(n/c), c = pi rho/24, a = sqrt(rho)/(2 pi sqrt 6) (Johnston (3.44)), und
      T(sigma) = -a int_0^sigma exp(-c s^2) h_m(sigma - s) ds,   h_m(y) = (m/(2 sqrt y)) J1(m sqrt y)   (sigma = tau^2).
  Ziel-Mittel: g_K = a exp(-c sigma^2) + T(sigma) mit Fourier-Bild k~(sqrt(Z^2 + m^2)) (Masse im Argument, BBL (3.2)).
  n kommt aus demselben float32-GEMM P = C C wie die Schichten (Zaehler < 2^24, exakt).
- Zuschauer (Palm-Lesart) fuer VK: n = Zahl der Elemente der Menge in I(y, Punkt), S = C Pm wie sf.zuschauer_v.

Aufruf (nur ueber kleintest.sh auf der .69):
  kernmasse_feld.py feld  <rho> <saat_von> <saat_bis> <ausgabeordner> [zeitgrenze_s]
  kernmasse_feld.py probe <rho> <saat> <ausgabeordner>
  kernmasse_feld.py repro <rho> <saat> <tag> <alte_npz> <ausgabeordner>   (nur VJ und V0 verglichen, keine VK-Werte)
"""
import hashlib
import json
import os
import resource
import sys
import time

import numpy as np
import scipy.sparse as sps
from scipy.special import j1

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kausal4d as kd  # noqa: E402
import schicht2_feld as sf  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
NC = kd.NC
M = kd.MASSE
NAMEN = ("VJ", "V0", "V00", "VK")
NV = len(NAMEN)
NQ_T = 128                 # Gauss-Legendre-Knoten fuer T(sigma)
X_T = 8.0                  # obere Grenze c^(1/2) s <= X_T (exp(-64) vernachlaessigbar)


def gl(a, b, n):
    g, w = np.polynomial.legendre.leggauss(n)
    return 0.5 * (b - a) * g + 0.5 * (b + a), 0.5 * (b - a) * w


def h_m(y, m=M):
    """h_m(y) = (m/(2 sqrt y)) J1(m sqrt y) fuer y >= 0; h_m(0) = m^2/4; |h_m| <= m^2/4."""
    y = np.asarray(y, dtype=float)
    ys = np.maximum(y, 1e-300)
    x = m * np.sqrt(ys)
    klein = x < 1e-6
    return np.where(klein, 0.25 * m * m * (1.0 - x * x / 8.0), (m / (2.0 * np.sqrt(ys))) * j1(x))


def T_sigma(sig, rho, m=M, nq=NQ_T):
    """T(sigma) = -a int_0^min(sigma, X_T/sqrt c) exp(-c s^2) h_m(sigma - s) ds (Gauss-Legendre, nq Knoten)."""
    sig = np.atleast_1d(np.asarray(sig, dtype=float))
    c = np.pi * rho / 24.0
    a = kd.a_hop(rho)
    g, w = np.polynomial.legendre.leggauss(nq)
    oben = np.minimum(sig, X_T / np.sqrt(c))
    out = np.zeros(sig.size)
    for i0 in range(0, sig.size, 4096):
        i1 = min(i0 + 4096, sig.size)
        ob = oben[i0:i1, None]
        s = 0.5 * ob * (g[None, :] + 1.0)
        ws = 0.5 * ob * w[None, :]
        out[i0:i1] = -a * (ws * np.exp(-c * s * s) * h_m(sig[i0:i1, None] - s, m)).sum(axis=1)
    return out


def t_tabelle(rho, nmax, m=M):
    """t(n) = T(sqrt(n/c)), n = 0 ... nmax; t(0) = 0."""
    c = np.pi * rho / 24.0
    n = np.arange(nmax + 1, dtype=float)
    t = T_sigma(np.sqrt(n / c), rho, m)
    t[0] = 0.0
    return t


def w_tabelle(rho, nmax, m=M):
    """W(n) = a [n = 0] + t(n)."""
    w = t_tabelle(rho, nmax, m)
    w[0] += kd.a_hop(rho)
    return w


def schichten_und_vk(C, J, wtab, B=kd.B_GEMM):
    """Schichten wie sf.schichten_gemm (gleiche Bloecke, gleiche Masken, gleiche Reihenfolge) und zugleich
    acc[x] = sum_{y vor x} W(n_yx) J(y) (Real- und Imaginaerteil als Spalten)."""
    N = C.shape[0]
    z = [[], [], []]
    s = [[], [], []]
    Jr = np.concatenate([J.real, J.imag], axis=1)
    acc = np.zeros((N, Jr.shape[1]))
    for I0 in range(0, N, B):
        I1 = min(I0 + B, N)
        for J0 in range(I0, N, B):
            J1 = min(J0 + B, N)
            Cij = C[I0:I1, J0:J1]
            if not Cij.any():
                continue
            P = C[I0:I1, I0:J1] @ C[I0:J1, J0:J1]
            K = Cij > 0.5
            for n, mask in enumerate((K & (P < 0.5), K & (P > 0.5) & (P < 1.5), K & (P > 1.5) & (P < 2.5))):
                r, c = np.nonzero(mask)
                z[n].append(r + I0)
                s[n].append(c + J0)
            Pi = np.rint(P).astype(np.int64)
            W = np.where(K, wtab[Pi], 0.0)
            acc[J0:J1] += W.T @ Jr[I0:I1]
    leer = np.zeros(0, dtype=np.int64)
    sch = tuple((np.concatenate(z[n]) if z[n] else leer, np.concatenate(s[n]) if s[n] else leer) for n in range(3))
    return sch, acc


def zuschauer_vk(C, t, X, J, rho, pp, wtab):
    """phi_K an Punkten ausserhalb der Menge: (1/rho) sum_{y vor Punkt} W(n) J(y), n = Elemente der Menge in I(y, Punkt)."""
    P = pp.reshape(-1, 4)
    dt = P[None, :, 0] - t[:, None]
    d2 = ((P[None, :, 1:] - X[:, None, :]) ** 2).sum(axis=2)
    Pm = ((dt > 0.0) & (dt * dt >= d2)).astype(np.float32)
    S = C @ Pm
    Si = np.rint(S).astype(np.int64)
    W = np.where(Pm > 0.5, wtab[Si], 0.0)
    n = pp.shape[1]
    out = np.zeros((pp.shape[0], n), dtype=np.complex128)
    for c in range(pp.shape[0]):
        out[c] = (W[:, c * n:(c + 1) * n].T @ J[:, c]) / rho
    return out


def lauf_feld_k(rho, saat, tag=sf.SAAT_TAG):
    t0 = time.time()
    rng = sf.rng_feld(rho, saat, tag)
    t, X = kd.streuen(rng, rho)
    N = t.size
    t1 = time.time()
    C = kd.kausalmatrix(t, X)
    t2 = time.time()
    J = kd.quelle(t, X)
    wtab = w_tabelle(rho, N + 1)
    sch, acc = schichten_und_vk(C, J, wtab)
    phi_vk = (acc[:, :NC] + 1j * acc[:, NC:]) / rho
    t3 = time.time()
    Lts = [sps.csr_matrix((np.ones(zi.size), (sp, zi)), shape=(N, N)) for (zi, sp) in sch]
    psis, phis = [], []
    for (_, c0, c1, c2) in sf.VARIANTEN:
        psi, phi = sf.loesen_v(sf.gewichte(Lts, rho, (c0, c1, c2)), J, rho)
        psis.append(psi)
        phis.append(phi)
    t4 = time.time()
    pp = kd.pruefpunkte()
    phi_p3, nl0, nl1, nl2 = sf.zuschauer_v(C, t, X, psis, rho, pp)
    phi_pk = zuschauer_vk(C, t, X, J, rho, pp, wtab)
    phi_p = np.concatenate([phi_p3, phi_pk[None]], axis=0)
    summen = np.stack([kd.messen(t, X, phis[iv], rho) for iv in range(3)] + [kd.messen(t, X, phi_vk, rho)])
    lz = [sf.zeitklassen(t, Lt) for Lt in Lts]
    t5 = time.time()
    Ls = [int(zi.size) for (zi, _) in sch]
    kopf = {"modus": "feld", "rho": rho, "saat": saat, "saat_tag": tag, "N": int(N), "L0": Ls[0], "L1": Ls[1],
            "L2": Ls[2], "L0_je_N": Ls[0] / N, "L1_je_N": Ls[1] / N, "L2_je_N": Ls[2] / N,
            "relationen": float(C.sum(dtype=np.float64)), "namen": list(NAMEN),
            "linkzahl_zeitklassen_summe": lz[0][0], "linkzahl_zeitklassen_n": lz[0][1],
            "w0": float(wtab[0]), "t_max_abs": float(np.abs(wtab[1:]).max()),
            "zeit_streuen_s": round(t1 - t0, 2), "zeit_kausal_s": round(t2 - t1, 2), "zeit_links_vk_s": round(t3 - t2, 2),
            "zeit_loesen_s": round(t4 - t3, 2), "zeit_messen_s": round(t5 - t4, 2), "zeit_gesamt_s": round(t5 - t0, 2),
            "max_abs_phi": {NAMEN[iv]: float(np.abs(p).max()) for iv, p in enumerate(phis + [phi_vk])},
            "endlich": bool(all(np.isfinite(p).all() for p in phis + [phi_vk]) and np.isfinite(phi_p).all()),
            "links_zuschauer": nl0.tolist(),
            "maxrss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
            "skript_sha256": SKRIPT_SHA, "schicht2_feld_sha256": sf.SKRIPT_SHA, "kausal4d_sha256": kd.SKRIPT_SHA,
            "numpy": np.__version__, "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    return kopf, summen, phi_p


def lauf_probe_k(rho, saat):
    """Codeprobe VK: Blockrechnung gegen dichte Rechnung (float64, P = C C), Zuschauer gegen eine Schleife, die die
    Elemente in I(y, Punkt) explizit zaehlt; Schichten der Blockschleife gegen sf.schichten_gemm. Nur Pruefgroessen."""
    rng = sf.rng_feld(rho, saat, sf.PROBE_TAG)
    t, X = kd.streuen(rng, rho)
    N = t.size
    C = kd.kausalmatrix(t, X)
    J = kd.quelle(t, X)
    wtab = w_tabelle(rho, N + 1)
    sch, acc = schichten_und_vk(C, J, wtab, B=256)
    phi_b = (acc[:, :NC] + 1j * acc[:, NC:]) / rho
    sch_ref = sf.schichten_gemm(C, B=256)
    gleich = [bool(np.array_equal(sch[n][0], sch_ref[n][0]) and np.array_equal(sch[n][1], sch_ref[n][1]))
              for n in range(3)]
    C64 = C.astype(np.float64)
    P64 = C64 @ C64
    Wd = np.where(C64 > 0.5, wtab[np.rint(P64).astype(np.int64)], 0.0)
    phi_d = (Wd.T @ J) / rho
    dt = t[None, :] - t[:, None]
    d2 = ((X[None, :, :] - X[:, None, :]) ** 2).sum(axis=2)
    Cref = ((dt > 0) & (dt * dt >= d2)).astype(np.float64)
    pp = kd.pruefpunkte()[:, :9]
    phi_p = zuschauer_vk(C, t, X, J, rho, pp, wtab)
    zz = []
    for c in range(NC):
        for i in range(pp.shape[1]):
            tt, xx, yy, z3 = pp[c, i]
            past = np.nonzero((tt - t > 0) & ((tt - t) ** 2 >= (xx - X[:, 0]) ** 2 + (yy - X[:, 1]) ** 2
                                              + (z3 - X[:, 2]) ** 2))[0]
            s = 0.0 + 0.0j
            for y in past:
                nz = int(np.sum(Cref[y, past] > 0.5))
                s += wtab[nz] * J[y, c]
            ref = s / rho
            zz.append(abs(phi_p[c, i] - ref) / max(abs(ref), 1e-300))
    # Gewichtstabelle gegen die Schranke |t| <= m^2/(8 pi) (VORAB.md Abschnitt 4)
    out = {"modus": "probe", "rho": rho, "saat": saat, "N": int(N),
           "schichten_gleich_schicht2": gleich, "kausal_gleich_koordinaten": bool(np.array_equal(C64, Cref)),
           "VK_rel_abw_block_dicht": float(np.abs(phi_b - phi_d).max() / np.abs(phi_d).max()),
           "VK_rel_abw_zuschauer_schleife_max": float(max(zz)),
           "t_max_abs": float(np.abs(wtab[1:]).max()), "schranke_m2_8pi": M * M / (8 * np.pi),
           "skript_sha256": SKRIPT_SHA, "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    out["schicht2_probe"] = sf.lauf_probe(rho, saat)
    return out


def lauf_repro_k(rho, saat, tag, alt_npz):
    """VJ und V0 gegen gespeicherte Werte (gleiche Saat und gleicher Tag). Ausgabe nur Vergleichsgroessen und Zeiten."""
    kopf, summen, phi_p = lauf_feld_k(rho, saat, tag)
    alt = np.load(alt_npz)
    out = {"modus": "repro", "rho": rho, "saat": saat, "saat_tag": tag, "N": kopf["N"], "L0": kopf["L0"],
           "L1": kopf["L1"], "L2": kopf["L2"], "zeit_links_vk_s": kopf["zeit_links_vk_s"],
           "zeit_gesamt_s": kopf["zeit_gesamt_s"], "maxrss_mb": kopf["maxrss_mb"], "endlich": kopf["endlich"]}
    for iv, name in ((0, "VJ"), (1, "V0")):
        out[f"{name}_max_abs_abw_phi_p"] = float(np.abs(phi_p[iv] - alt["phi_p"][iv]).max())
        out[f"{name}_max_abs_abw_summen"] = float(np.abs(summen[iv] - alt["summen"][iv]).max())
        out[f"{name}_bitgleich_phi_p"] = bool(np.array_equal(phi_p[iv], alt["phi_p"][iv]))
        out[f"{name}_bitgleich_summen"] = bool(np.array_equal(summen[iv], alt["summen"][iv]))
    out.update({"skript_sha256": SKRIPT_SHA, "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
    return out


def main():
    modus = sys.argv[1]
    rho = float(sys.argv[2])
    if modus == "probe":
        saat, ordner = int(sys.argv[3]), sys.argv[4]
        os.makedirs(ordner, exist_ok=True)
        kopf = lauf_probe_k(rho, saat)
        with open(os.path.join(ordner, f"probe-r{rho:g}-s{saat}.json"), "w") as fh:
            json.dump(kopf, fh, indent=1)
        print(json.dumps(kopf), flush=True)
        return
    if modus == "repro":
        saat, tag, alt_npz, ordner = int(sys.argv[3]), int(sys.argv[4]), sys.argv[5], sys.argv[6]
        os.makedirs(ordner, exist_ok=True)
        kopf = lauf_repro_k(rho, saat, tag, alt_npz)
        with open(os.path.join(ordner, f"repro-r{rho:g}-s{saat}.json"), "w") as fh:
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
            print(json.dumps({"abbruch_vor_saat": saat, "grund": "zeitgrenze",
                              "verstrichen_s": round(time.time() - start, 1)}), flush=True)
            break
        ts = time.time()
        kopf, summen, phi_p = lauf_feld_k(rho, saat)
        np.savez_compressed(os.path.join(ordner, f"feld-r{rho:g}-s{saat}.npz"), summen=summen, phi_p=phi_p,
                            pruefpunkte=kd.pruefpunkte())
        with open(os.path.join(ordner, f"feld-r{rho:g}-s{saat}.json"), "w") as fh:
            json.dump(kopf, fh, indent=1)
        dauer_max = max(dauer_max, time.time() - ts)
        print(json.dumps({k: kopf[k] for k in ("rho", "saat", "N", "L0", "L1", "L2", "zeit_links_vk_s", "zeit_gesamt_s",
                                                "endlich", "maxrss_mb", "zeit_utc")}), flush=True)


if __name__ == "__main__":
    main()
