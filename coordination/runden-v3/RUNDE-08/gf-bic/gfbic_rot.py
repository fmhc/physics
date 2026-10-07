#!/usr/bin/env python3
"""Runde 9, Karte ROT-2 (PLAN.md Nachtrag F): innere Drehung der relativen Phase im gemischten Ball (N = 2, J = 1),
radiale 3D-Zeitentwicklung der vollen nichtlinearen Zwei-Komponenten-Gleichungen. Code begonnen 2026-09-30 07:52:52 CEST.

Phi_a = r psi_a:  Phi_a,tt = Phi_a,rr - U'(S) Phi_a + g J conj(Phi_a) Phi_b^2 / r^2 - sigma(r) Phi_a,t,
S = (|Phi_1|^2 + |Phi_2|^2) / r^2, U' = 1 - 2 S + 1,5 S^2. Leapfrog (Stoermer-Verlet) mit Schwamm, Gitter r_j = j Delta.
Anfang: gemischter Ball psi_1 = psi_2 = h(r) e^{-i omega t} (natives Profil, auf dem FD-Gitter per Newton nachrelaxiert),
Kick der relativen Phase: omega_1 = omega + Omega_0/2, omega_2 = omega - Omega_0/2 (gleiche Profile).
Messgroessen: Delta theta = arg int psi_1^* psi_2 (global) und am Ursprung; Q_a in r < R_m; Ladungs- und Energiefluss
durch r = R_m; Zeitreihen psi_+- = (psi_1 +- psi_2)/sqrt 2 bei R_m fuer Spektren.
Kommandos: rauch | lauf --kicks 0.1,0.3 --g ... --w2 ... --delta ...
"""
import argparse
import json
import math
import os
import sys
import traceback

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import numpy as np  # noqa: E402
import scipy.linalg as sla  # noqa: E402

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import gfbic_umlauf as GU  # noqa: E402
import gfbic as G  # noqa: E402

JK = 1.0


def U1(S):
    return 1.0 - 2.0 * S + 1.5 * S * S


def U2(S):
    return -2.0 + 3.0 * S


def profil_fd(w2, g, delta, R):
    """natives Profil (gfbic_umlauf.prof_nativ, Schritt hp) auf r_j = j delta, dann Newton auf dem FD-Gitter:
    -H'' + (U'(2 h^2) - g J h^2 - w2) H = 0, h = H/r (je Komponente)."""
    hp = 0.005
    k = int(round(delta / hp))
    M = int(round(R / delta)) - 1
    p = GU.prof_nativ(w2, g, hp)
    f, _ = GU.B2.f_werte(p, k * (M + 1) + 1)
    r = delta * np.arange(1, M + 1)
    h = np.array(f)[k::k][:M] / math.sqrt(2.0)        # f = sqrt(2) h
    H = r * h
    for it in range(30):
        hh = H / r
        V = U1(2 * hh * hh) - g * JK * hh * hh - w2
        lap = np.zeros(M)
        lap[1:-1] = H[2:] - 2 * H[1:-1] + H[:-2]
        lap[0] = H[1] - 2 * H[0]
        lap[-1] = H[-2] - 2 * H[-1]
        res = -lap / delta ** 2 + V * H
        dV = 4 * hh * hh * U2(2 * hh * hh) - 2 * g * JK * hh * hh
        diag = 2.0 / delta ** 2 + V + dV
        ab = np.zeros((3, M))
        ab[0, 1:] = -1.0 / delta ** 2
        ab[1, :] = diag
        ab[2, :-1] = -1.0 / delta ** 2
        dH = sla.solve_banded((1, 1), ab, -res)
        H = H + dH
        if np.max(np.abs(dH)) < 1e-13 * np.max(np.abs(H)):
            break
    return r, H / r, {"newton_iter": it + 1, "max_res": float(np.max(np.abs(res))), "S0": 2 * (H[0] / r[0]) ** 2}


def lauf(w2, g, kick, delta, R, T, r_m, sig0, l_sp, dt_fak, mess_dt, profil=None, start="kick"):
    om = math.sqrt(w2)
    if profil is None:
        profil = profil_fd(w2, g, delta, R)
    r, h, pinfo = profil
    M = len(r)
    dt = dt_fak * delta
    nsteps = int(round(T / dt))
    nm = max(1, int(round(mess_dt / dt)))
    sig = np.where(r > R - l_sp, sig0 * ((r - (R - l_sp)) / l_sp) ** 2, 0.0)
    a_p = 1.0 + 0.5 * sig * dt
    a_m = 1.0 - 0.5 * sig * dt
    w1, w2_ = om + 0.5 * kick, om - 0.5 * kick
    P1 = (r * h).astype(complex)
    P2 = (r * h).astype(complex)
    if start == "ungleich":                     # Fassung 2 (08:06): Ungleichgewicht z0 = kick, beide mit omega
        w1, w2_ = om, om
        P1 = P1 * math.sqrt(1.0 + kick)
        P2 = P2 * math.sqrt(1.0 - kick)
    P1a = P1 * np.exp(1j * w1 * dt)            # Phi(-dt): psi ~ e^{-i omega_a t}
    P2a = P2 * np.exp(1j * w2_ * dt)
    inv_r2 = 1.0 / r ** 2
    jm = int(round(r_m / delta)) - 1           # Index von R_m
    wq = np.full(jm + 1, delta)

    def kraft(A, B):
        S = (np.abs(A) ** 2 + np.abs(B) ** 2) * inv_r2
        lapA = np.empty_like(A)
        lapA[1:-1] = A[2:] - 2 * A[1:-1] + A[:-2]
        lapA[0] = A[1] - 2 * A[0]
        lapA[-1] = A[-2] - 2 * A[-1]
        lapB = np.empty_like(B)
        lapB[1:-1] = B[2:] - 2 * B[1:-1] + B[:-2]
        lapB[0] = B[1] - 2 * B[0]
        lapB[-1] = B[-2] - 2 * B[-1]
        u1 = U1(S)
        FA = lapA / delta ** 2 - u1 * A + g * JK * np.conj(A) * B * B * inv_r2
        FB = lapB / delta ** 2 - u1 * B + g * JK * np.conj(B) * A * A * inv_r2
        return FA, FB

    ts, dth_g, dth_0, q1, q2, fq, fe, pp, pm = [], [], [], [], [], [], [], [], []
    FA, FB = kraft(P1, P2)
    for n in range(nsteps):
        N1 = (2 * P1 - a_m * P1a + dt * dt * FA) / a_p
        N2 = (2 * P2 - a_m * P2a + dt * dt * FB) / a_p
        if n % nm == 0:
            V1 = (N1 - P1a) / (2 * dt)
            V2 = (N2 - P2a) / (2 * dt)
            t = n * dt
            c = np.sum(np.conj(P1[:jm + 1]) * P2[:jm + 1] * wq)
            ts.append(t)
            dth_g.append(float(np.angle(c)))
            dth_0.append(float(np.angle(P2[0] * np.conj(P1[0]))))
            q1.append(float(-8 * math.pi * np.sum(np.imag(np.conj(P1[:jm + 1]) * V1[:jm + 1]) * wq)))
            q2.append(float(-8 * math.pi * np.sum(np.imag(np.conj(P2[:jm + 1]) * V2[:jm + 1]) * wq)))
            fqs, fes = 0.0, 0.0
            for P, V in ((P1, V1), (P2, V2)):
                Pr = (P[jm + 1] - P[jm - 1]) / (2 * delta)
                fqs += 8 * math.pi * float(np.imag(np.conj(P[jm]) * Pr))
                fes += -8 * math.pi * float(np.real(np.conj(V[jm]) * (Pr - P[jm] / r[jm])))
            fq.append(fqs)
            fe.append(fes)
            pp.append(complex((P1[jm] + P2[jm]) / (math.sqrt(2) * r[jm])))
            pm.append(complex((P1[jm] - P2[jm]) / (math.sqrt(2) * r[jm])))
        P1a, P2a, P1, P2 = P1, P2, N1, N2
        FA, FB = kraft(P1, P2)
        if not np.all(np.isfinite(P1[:10])):
            break
    return {"t": np.array(ts), "dth_g": np.unwrap(np.array(dth_g)), "dth_0": np.unwrap(np.array(dth_0)),
            "q1": np.array(q1), "q2": np.array(q2), "fq": np.array(fq), "fe": np.array(fe), "pp": np.array(pp),
            "pm": np.array(pm), "dt": dt, "M": M, "profil": pinfo, "omega": om, "kick": kick, "g": g, "w2": w2,
            "delta": delta}


def spektrum(x, dtm, fmin, fmax, n_peaks=3):
    """Hann-gefensterte FFT mit 4-facher Nullauffuellung, groesste lokale Maxima in [fmin, fmax] (Kreisfrequenz)."""
    n = len(x)
    if n < 16:
        return []
    w = np.hanning(n)
    X = np.fft.fft((x - np.mean(x)) * w, 4 * n)
    f = 2 * math.pi * np.fft.fftfreq(4 * n, dtm)
    A = np.abs(X) * 2 / np.sum(w)
    sel = np.where((f >= fmin) & (f <= fmax))[0]
    if len(sel) < 3:
        return []
    Asel = A[sel]
    pk = [i for i in range(1, len(sel) - 1) if Asel[i] >= Asel[i - 1] and Asel[i] >= Asel[i + 1]]
    pk.sort(key=lambda i: -Asel[i])
    return [(float(f[sel[i]]), float(Asel[i])) for i in pk[:n_peaks]]


def auswerten(res, zeilen):
    t, dtm = res["t"], res["t"][1] - res["t"][0]
    om = res["omega"]
    dth = res["dth_g"]
    # langsamer Anteil: gleitendes Mittel ueber eine schnelle Periode 2 pi/(2 omega)
    nw = max(1, int(round((math.pi / om) / dtm)))
    ker = np.ones(nw) / nw
    slow = np.convolve(dth, ker, mode="same")
    innen = slice(nw, len(slow) - nw)
    s_in = slow[innen] - slow[innen][0] if len(slow[innen]) else slow
    phi_max = float(np.max(np.abs(slow[innen] - np.mean(slow[innen])))) if len(slow[innen]) else float("nan")
    lauf_ = float(np.max(slow[innen]) - np.min(slow[innen])) if len(slow[innen]) else float("nan")
    drift = float(s_in[-1]) if len(s_in) else float("nan")
    Q = res["q1"] + res["q2"]
    z = (res["q1"] - res["q2"]) / np.where(np.abs(Q) > 0, Q, 1.0)
    halb = len(t) // 2
    sp_z = spektrum(z[halb // 2:], dtm, 0.005, 0.5)
    sp_slow = spektrum(slow[halb // 2:], dtm, 0.005, 0.5)
    sp_fast = spektrum(dth[halb // 2:] - slow[halb // 2:], dtm, 1.0, 2.5)
    sp_pp = spektrum(res["pp"][halb:], dtm, 1.0, 4.0, 4) if len(res["pp"]) else []
    sp_pm = spektrum(res["pm"][halb:], dtm, 1.0, 4.0, 4) if len(res["pm"]) else []
    # negative Frequenzen (psi ~ e^{-i omega t}): Spektrum von conj
    sp_pp_n = spektrum(np.conj(res["pp"][halb:]), dtm, 1.0, 4.0, 4)
    sp_pm_n = spektrum(np.conj(res["pm"][halb:]), dtm, 1.0, 4.0, 4)
    fq_m = float(np.mean(res["fq"][halb:]))
    fe_m = float(np.mean(res["fe"][halb:]))
    q_bil = float((Q[-1] - Q[0]) + np.sum(res["fq"]) * dtm)
    e = {"kick": res["kick"], "g": res["g"], "delta": res["delta"], "phi_max": phi_max, "phi_spanne": lauf_,
         "phi_drift": drift, "laeuft": bool(lauf_ > math.pi), "z_max": float(np.max(np.abs(z))),
         "z_spektrum": sp_z, "slow_spektrum": sp_slow, "fast_spektrum": sp_fast, "fq_mittel": fq_m, "fe_mittel": fe_m,
         "Q0": float(Q[0]), "Q_end": float(Q[-1]), "Q_bilanz_rest": q_bil,
         "dQ12_drift": float((res["q1"][-1] - res["q2"][-1]) - (res["q1"][0] - res["q2"][0])),
         "spek_plus_neg": sp_pp_n, "spek_minus_neg": sp_pm_n, "spek_plus_pos": sp_pp, "spek_minus_pos": sp_pm,
         "profil": res["profil"], "T": float(t[-1])}
    zeilen.append(f"  Kick {res['kick']:.3f} (g {res['g']}, Delta {res['delta']}): langsame Phase max |phi - <phi>| = "
                  f"{phi_max:.4f}, Spanne {lauf_:.4f} rad, laeuft {e['laeuft']}; z max {e['z_max']:.4f}; "
                  f"Linien z {[(round(a, 5), round(b, 5)) for a, b in sp_z[:2]]}, langsam {[(round(a, 5), round(b, 5)) for a, b in sp_slow[:2]]}, "
                  f"schnell {[(round(a, 4), round(b, 4)) for a, b in sp_fast[:1]]}")
    zeilen.append(f"    Fluss r = R_m (2. Haelfte): Q {fq_m:+.3e}, E {fe_m:+.3e}; Q0 {Q[0]:.5f}, Q_end {Q[-1]:.5f}, "
                  f"Bilanzrest {q_bil:+.2e}; Q1-Q2 Drift {e['dQ12_drift']:+.3e}")
    zeilen.append(f"    Spektrum bei R_m (Frequenz, Amplitude), psi_+ neg/pos: {[(round(a, 4), f'{b:.2e}') for a, b in sp_pp_n[:3]]} / "
                  f"{[(round(a, 4), f'{b:.2e}') for a, b in sp_pp[:2]]}; psi_- neg/pos: "
                  f"{[(round(a, 4), f'{b:.2e}') for a, b in sp_pm_n[:3]]} / {[(round(a, 4), f'{b:.2e}') for a, b in sp_pm[:2]]}")
    return e


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kommando", choices=["rauch", "lauf"])
    ap.add_argument("--w2", type=float, default=0.755738)
    ap.add_argument("--g", type=float, default=4.0 * (1.0 / math.sqrt(0.9) - 1.0))
    ap.add_argument("--kicks", default="0,0.1,0.3")
    ap.add_argument("--start", default="kick", choices=["kick", "ungleich"],
                    help="Fassung 2: ungleich = Ladungsungleichgewicht z0 (Werte aus --kicks), beide mit omega")
    ap.add_argument("--delta", type=float, default=0.1)
    ap.add_argument("--R", type=float, default=80.0)
    ap.add_argument("--T", type=float, default=3000.0)
    ap.add_argument("--rm", type=float, default=20.0)
    ap.add_argument("--sig0", type=float, default=1.0)
    ap.add_argument("--lsp", type=float, default=20.0)
    ap.add_argument("--dtfak", type=float, default=0.4)
    ap.add_argument("--messdt", type=float, default=0.25)
    ap.add_argument("--out", default=None)
    ap.add_argument("--budget", type=float, default=540.0)
    a = ap.parse_args()
    budget = G.Budget(a.budget)
    out = a.out or os.path.join(HIER, "ausgabe-rot")
    os.makedirs(out, exist_ok=True)
    if a.kommando == "rauch":
        a.T, a.delta, a.R, a.kicks = 200.0, 0.2, 40.0, "0,0.3"
    kopf = (f"Runde 9 ROT-2 {a.kommando} Start {G.jetzt()}; gfbic_rot.py sha256 {G.sha256(os.path.abspath(__file__))[:16]}; "
            f"w2 {a.w2}, g {a.g:.6f}, Delta {a.delta}, R {a.R}, T {a.T}, R_m {a.rm}")
    zeilen = [kopf]
    print(kopf, flush=True)
    erg = {"argumente": vars(a), "laeufe": []}
    rc = 0
    try:
        if a.kommando == "rauch":
            a.T, a.delta, a.R, a.kicks = 200.0, 0.2, 40.0, "0,0.3"
        prof = profil_fd(a.w2, a.g, a.delta, a.R)
        zeilen.append(f"  Profil FD: Newton {prof[2]['newton_iter']} Schritte, Rest {prof[2]['max_res']:.1e}, S0 {prof[2]['S0']:.6f}")
        for k in [float(v) for v in a.kicks.split(",")]:
            if not budget.ok(f"Kick {k}", 30.0):
                break
            t0 = G.uhr()
            res = lauf(a.w2, a.g, k, a.delta, a.R, a.T, a.rm, a.sig0, a.lsp, a.dtfak, a.messdt, profil=prof,
                       start=a.start)
            e = auswerten(res, zeilen)
            e["sek"] = G.uhr() - t0
            erg["laeufe"].append(e)
            np.savez_compressed(os.path.join(out, f"zeit_{a.start}{k:.3f}_g{a.g:.3f}_d{a.delta}.npz"), t=res["t"],
                                dth_g=res["dth_g"], dth_0=res["dth_0"], q1=res["q1"], q2=res["q2"], fq=res["fq"],
                                fe=res["fe"], pp=res["pp"], pm=res["pm"])
            zeilen.append(f"    ({e['sek']:.1f} s)")
            with open(os.path.join(out, "rot.json"), "w") as fh:
                json.dump(G.jsonfest(erg), fh, indent=1)
    except Exception:                                   # noqa: BLE001
        tb = traceback.format_exc()
        zeilen.append("FEHLER:\n" + tb)
        erg["fehler"] = tb
        rc = 1
    zeilen.append(f"Ende {G.jetzt()}, {G.uhr():.1f} s; entfallen: {budget.abgebrochen or 'nichts'}")
    with open(os.path.join(out, "rot.json"), "w") as fh:
        json.dump(G.jsonfest(erg), fh, indent=1)
    with open(os.path.join(out, "rot_bericht.txt"), "w") as fh:
        fh.write("\n".join(zeilen) + "\n")
    print("\n".join(zeilen[1:]), flush=True)
    sys.exit(rc)


if __name__ == "__main__":
    main()
