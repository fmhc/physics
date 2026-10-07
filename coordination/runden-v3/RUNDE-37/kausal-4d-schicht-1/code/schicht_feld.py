"""KAUSAL-4D-SCHICHT-1 (Runde 38, Code-Agent), Teil B: Felder fuer drei Sprungregeln auf derselben Streuung.

Baut auf kausal4d.py (KAUSAL-WELLE-4D, unveraendert importiert): Streuung, Kausalmatrix, Quelle, Gebiet D, Pruefpunkte,
Messung. Neu:
- Aus demselben float32-GEMM-Produkt P = C C wie die Links (P == 0) fallen die 1-Element-Intervalle ab (P == 1).
  Zaehler bis 2^24 exakt; Zwischenindex wie in kausal4d.links_gemm auf [I0, J1) beschraenkt (zeitlich sortiert).
- Varianten (Amplituden in Einheiten von a = sqrt(rho)/(2 pi sqrt 6), Johnston (3.44)):
    VJ: Links 1 a                       (sigma = sum a_n = +a)
    V0: Links 2 a, 1-Element -2 a        (sigma = 0)
    VM: Links 3 a, 1-Element -4 a        (sigma = -a)
  Normierung sum a_n Gamma(n + 1/2)/n! = a sqrt(pi) in allen drei (PLAN Abschnitt 2).
- Rekursion je Variante: Phi^T = a (c0 L0^T + c1 L1^T); psi = J - (m^2/rho) Phi^T psi; phi = (1/rho) Phi^T psi.
- Zuschauer (Palm-Lesart): phi(p) = (1/rho) sum_y Phi(y, p) psi(y); Phi(y, p) = a c0 [y -<* p] + a c1 [|I(y, p)| = 1].

Aufruf (nur ueber kleintest.sh auf der .69):
  schicht_feld.py feld  <rho> <saat_von> <saat_bis> <ausgabeordner> [zeitgrenze_s]
  schicht_feld.py probe <rho> <saat> <ausgabeordner>
  schicht_feld.py repro <rho> <saat> <alte_npz> <alte_json> <ausgabeordner>
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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kausal4d as kd  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
NC = kd.NC
VARIANTEN = (("VJ", 1.0, 0.0), ("V0", 2.0, -2.0), ("VM", 3.0, -4.0))
NV = len(VARIANTEN)
SAAT_TAG = 141          # neue Saatfolge (KAUSAL-WELLE-4D: 81 Feld, 83 Probe, 99 Zeit)
PROBE_TAG = 143


def rng_feld(rho, saat, tag=SAAT_TAG):
    return np.random.default_rng(np.random.SeedSequence([20261004, 38, tag, int(round(rho * 1000)), int(saat)]))


def links_eins_gemm(C, B=kd.B_GEMM):
    """Links (P == 0) und 1-Element-Intervalle (P == 1) mit C[i, j] = 1, P = C C; Bloecke wie kausal4d.links_gemm."""
    N = C.shape[0]
    z0, s0, z1, s1 = [], [], [], []
    for I0 in range(0, N, B):
        I1 = min(I0 + B, N)
        for J0 in range(I0, N, B):
            J1 = min(J0 + B, N)
            Cij = C[I0:I1, J0:J1]
            if not Cij.any():
                continue
            P = C[I0:I1, I0:J1] @ C[I0:J1, J0:J1]
            K = Cij > 0.5
            r, c = np.nonzero(K & (P < 0.5))
            z0.append(r + I0)
            s0.append(c + J0)
            r, c = np.nonzero(K & (P > 0.5) & (P < 1.5))
            z1.append(r + I0)
            s1.append(c + J0)
    leer = np.zeros(0, dtype=np.int64)
    return ((np.concatenate(z0) if z0 else leer, np.concatenate(s0) if s0 else leer),
            (np.concatenate(z1) if z1 else leer, np.concatenate(s1) if s1 else leer))


def gewichte(Lt0, Lt1, rho, c0, c1):
    a = kd.a_hop(rho)
    W = (a * c0) * Lt0
    if c1 != 0.0:
        W = W + (a * c1) * Lt1
    return W.tocsr()


def loesen_v(W, J, rho):
    """(I + (m^2/rho) W) psi = J (W = Phi^T, streng untere Dreiecksmatrix); phi = W psi/rho."""
    N = J.shape[0]
    A = (sps.identity(N, format="csr") + (kd.MASSE ** 2 / rho) * W).tocsr()
    b = np.concatenate([J.real, J.imag], axis=1)
    x = spsolve_triangular(A, b, lower=True)
    psi = x[:, :NC] + 1j * x[:, NC:]
    phi = (W @ psi) / rho
    return psi, phi


def zuschauer_v(C, t, X, psis, rho, pp):
    """phi je Variante an Punkten ausserhalb der Menge: Links (S == 0) und 1-Element-Intervalle (S == 1) in die Menge."""
    a = kd.a_hop(rho)
    P = pp.reshape(-1, 4)
    dt = P[None, :, 0] - t[:, None]
    d2 = ((P[None, :, 1:] - X[:, None, :]) ** 2).sum(axis=2)
    Pm = ((dt > 0.0) & (dt * dt >= d2)).astype(np.float32)          # (N, n): y in der Vergangenheit des Punktes
    S = C @ Pm                                                        # Zahl der Elemente in I(y, Punkt)
    L0 = ((Pm > 0.5) & (S < 0.5)).astype(np.float64)
    L1 = ((Pm > 0.5) & (S > 0.5) & (S < 1.5)).astype(np.float64)
    n = pp.shape[1]
    out = np.zeros((NV, pp.shape[0], n), dtype=np.complex128)
    for iv, (_, c0, c1) in enumerate(VARIANTEN):
        for c in range(pp.shape[0]):
            s0 = L0[:, c * n:(c + 1) * n].T @ psis[iv][:, c]
            s1 = L1[:, c * n:(c + 1) * n].T @ psis[iv][:, c]
            out[iv, c] = (a / rho) * (c0 * s0 + c1 * s1)
    return out, L0.sum(axis=0).reshape(pp.shape[0], n), L1.sum(axis=0).reshape(pp.shape[0], n)


def zeitklassen(t, Lt):
    grad = np.asarray(Lt.sum(axis=1)).ravel()
    k = np.clip(np.floor((t - kd.LZ_T0) / kd.LZ_W).astype(np.int64), 0, kd.LZ_N - 1)
    return np.bincount(k, weights=grad, minlength=kd.LZ_N).tolist(), np.bincount(k, minlength=kd.LZ_N).tolist()


def lauf_feld_v(rho, saat, tag=SAAT_TAG):
    t0 = time.time()
    rng = rng_feld(rho, saat, tag)
    t, X = kd.streuen(rng, rho)
    N = t.size
    t1 = time.time()
    C = kd.kausalmatrix(t, X)
    t2 = time.time()
    (zi0, sp0), (zi1, sp1) = links_eins_gemm(C)
    t3 = time.time()
    Lt0 = sps.csr_matrix((np.ones(zi0.size), (sp0, zi0)), shape=(N, N))   # Lt0[j, i] = 1, wenn i -<* j
    Lt1 = sps.csr_matrix((np.ones(zi1.size), (sp1, zi1)), shape=(N, N))   # Lt1[j, i] = 1, wenn |I(i, j)| = 1
    J = kd.quelle(t, X)
    psis, phis = [], []
    for (_, c0, c1) in VARIANTEN:
        psi, phi = loesen_v(gewichte(Lt0, Lt1, rho, c0, c1), J, rho)
        psis.append(psi)
        phis.append(phi)
    t4 = time.time()
    pp = kd.pruefpunkte()
    phi_p, nl0, nl1 = zuschauer_v(C, t, X, psis, rho, pp)
    summen = np.stack([kd.messen(t, X, phis[iv], rho) for iv in range(NV)])
    lz0 = zeitklassen(t, Lt0)
    lz1 = zeitklassen(t, Lt1)
    t5 = time.time()
    kopf = {"modus": "feld", "rho": rho, "saat": saat, "saat_tag": tag, "N": int(N), "L0": int(zi0.size),
            "L1": int(zi1.size), "L0_je_N": zi0.size / N, "L1_je_N": zi1.size / N,
            "relationen": float(C.sum(dtype=np.float64)),
            "linkzahl_zeitklassen_summe": lz0[0], "linkzahl_zeitklassen_n": lz0[1],
            "eins_zeitklassen_summe": lz1[0],
            "zeit_streuen_s": round(t1 - t0, 2), "zeit_kausal_s": round(t2 - t1, 2), "zeit_links_s": round(t3 - t2, 2),
            "zeit_loesen_s": round(t4 - t3, 2), "zeit_messen_s": round(t5 - t4, 2), "zeit_gesamt_s": round(t5 - t0, 2),
            "max_abs_psi": {VARIANTEN[iv][0]: float(np.abs(psis[iv]).max()) for iv in range(NV)},
            "max_abs_phi": {VARIANTEN[iv][0]: float(np.abs(phis[iv]).max()) for iv in range(NV)},
            "endlich": bool(all(np.isfinite(p).all() for p in phis) and np.isfinite(phi_p).all()),
            "links_zuschauer": nl0.tolist(), "eins_zuschauer": nl1.tolist(),
            "maxrss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
            "skript_sha256": SKRIPT_SHA, "kausal4d_sha256": kd.SKRIPT_SHA, "numpy": np.__version__,
            "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    return kopf, summen, phi_p


def lauf_probe(rho, saat):
    """Codeprobe: GEMM-Links und 1-Element-Intervalle gegen dichtes C C (float64), Kausalitaet gegen Koordinaten,
    Rekursion je Variante gegen dichte Loesung und Reihe, Zuschauer je Variante gegen explizite Schleife."""
    rng = rng_feld(rho, saat, PROBE_TAG)
    t, X = kd.streuen(rng, rho)
    N = t.size
    C = kd.kausalmatrix(t, X)
    (zi0, sp0), (zi1, sp1) = links_eins_gemm(C, B=256)
    C64 = C.astype(np.float64)
    P64 = C64 @ C64
    Lref0 = ((C64 > 0.5) & (P64 < 0.5)).astype(np.float64)
    Lref1 = ((C64 > 0.5) & (P64 > 0.5) & (P64 < 1.5)).astype(np.float64)
    Ld0 = np.zeros((N, N))
    Ld0[zi0, sp0] = 1.0
    Ld1 = np.zeros((N, N))
    Ld1[zi1, sp1] = 1.0
    dt = t[None, :] - t[:, None]
    d2 = ((X[None, :, :] - X[:, None, :]) ** 2).sum(axis=2)
    Cref = ((dt > 0) & (dt * dt >= d2)).astype(np.float64)
    out = {"modus": "probe", "rho": rho, "saat": saat, "N": int(N), "L0": int(zi0.size), "L1": int(zi1.size),
           "links_gleich_dicht": bool(np.array_equal(Ld0, Lref0)), "eins_gleich_dicht": bool(np.array_equal(Ld1, Lref1)),
           "kausal_gleich_koordinaten": bool(np.array_equal(C64, Cref))}
    Lt0 = sps.csr_matrix((np.ones(zi0.size), (sp0, zi0)), shape=(N, N))
    Lt1 = sps.csr_matrix((np.ones(zi1.size), (sp1, zi1)), shape=(N, N))
    J = kd.quelle(t, X)
    a = kd.a_hop(rho)
    beta = kd.MASSE ** 2 / rho
    pp = kd.pruefpunkte()[:, :9]
    psis = []
    for iv, (name, c0, c1) in enumerate(VARIANTEN):
        psi, phi = loesen_v(gewichte(Lt0, Lt1, rho, c0, c1), J, rho)
        psis.append(psi)
        Wd = a * (c0 * Lref0.T + c1 * Lref1.T)
        psi_d = np.linalg.solve(np.eye(N) + beta * Wd, J)
        phi_d = (Wd @ psi_d) / rho
        reihe = np.zeros_like(J)
        term = J.copy()
        for _ in range(400):
            reihe += term
            term = -beta * (Wd @ term)
        phi_r = (Wd @ reihe) / rho
        out[f"{name}_rel_abw_phi_rekursion_dicht"] = float(np.abs(phi - phi_d).max() / np.abs(phi_d).max())
        out[f"{name}_rel_abw_reihe_dicht"] = float(np.abs(phi_r - phi_d).max() / np.abs(phi_d).max())
        out[f"{name}_rest_reihe"] = float(np.abs(term).max())
    phi_p, _, _ = zuschauer_v(C, t, X, psis, rho, pp)
    for iv, (name, c0, c1) in enumerate(VARIANTEN):
        Wd = a * (c0 * Lref0.T + c1 * Lref1.T)
        psi_d = np.linalg.solve(np.eye(N) + beta * Wd, J)
        zz = []
        for c in range(NC):
            for i in range(pp.shape[1]):
                tt, xx, yy, z3 = pp[c, i]
                past = np.nonzero((tt - t > 0) & ((tt - t) ** 2 >= (xx - X[:, 0]) ** 2 + (yy - X[:, 1]) ** 2
                                                  + (z3 - X[:, 2]) ** 2))[0]
                s = 0.0 + 0.0j
                for y in past:
                    nz = int(np.sum(Cref[y, past] > 0.5))     # Elemente der Menge in I(y, Punkt)
                    if nz == 0:
                        s += c0 * psi_d[y, c]
                    elif nz == 1:
                        s += c1 * psi_d[y, c]
                ref = (a / rho) * s
                zz.append(abs(phi_p[iv, c, i] - ref) / max(abs(ref), 1e-300))
        out[f"{name}_rel_abw_zuschauer_max"] = float(max(zz))
    out.update({"skript_sha256": SKRIPT_SHA, "kausal4d_sha256": kd.SKRIPT_SHA,
                "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
    return out


def lauf_repro(rho, saat, alt_npz, alt_json):
    """Variante VJ mit der Saatfolge von KAUSAL-WELLE-4D (Tag 81) gegen deren gespeicherte Werte."""
    kopf, summen, phi_p = lauf_feld_v(rho, saat, tag=81)
    alt = np.load(alt_npz)
    aj = json.load(open(alt_json))
    d_p = float(np.abs(phi_p[0] - alt["phi_p"]).max() / np.abs(alt["phi_p"]).max())
    d_s = float(np.abs(summen[0] - alt["summen"]).max() / np.abs(alt["summen"]).max())
    return {"modus": "repro", "rho": rho, "saat": saat, "N_neu": kopf["N"], "N_alt": aj["N"], "L0_neu": kopf["L0"],
            "L_alt": aj["L"], "rel_abw_phi_p_VJ_gegen_alt": d_p, "rel_abw_summen_VJ_gegen_alt": d_s,
            "L1_neu": kopf["L1"], "zeit_gesamt_s": kopf["zeit_gesamt_s"], "skript_sha256": SKRIPT_SHA,
            "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}


def main():
    modus = sys.argv[1]
    rho = float(sys.argv[2])
    if modus == "probe":
        saat, ordner = int(sys.argv[3]), sys.argv[4]
        os.makedirs(ordner, exist_ok=True)
        kopf = lauf_probe(rho, saat)
        with open(os.path.join(ordner, f"probe-r{rho:g}-s{saat}.json"), "w") as fh:
            json.dump(kopf, fh, indent=1)
        print(json.dumps(kopf), flush=True)
        return
    if modus == "repro":
        saat, alt_npz, alt_json, ordner = int(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6]
        os.makedirs(ordner, exist_ok=True)
        kopf = lauf_repro(rho, saat, alt_npz, alt_json)
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
        kopf, summen, phi_p = lauf_feld_v(rho, saat)
        np.savez_compressed(os.path.join(ordner, f"feld-r{rho:g}-s{saat}.npz"), summen=summen, phi_p=phi_p,
                            pruefpunkte=kd.pruefpunkte())
        with open(os.path.join(ordner, f"feld-r{rho:g}-s{saat}.json"), "w") as fh:
            json.dump(kopf, fh, indent=1)
        dauer_max = max(dauer_max, time.time() - ts)
        print(json.dumps({k: kopf[k] for k in ("rho", "saat", "N", "L0", "L1", "zeit_links_s", "zeit_gesamt_s",
                                                "endlich", "maxrss_mb", "zeit_utc")}), flush=True)


if __name__ == "__main__":
    main()
