# KREIN-1: Krein-Norm und Energie der stillen Moden (float64, numpy/scipy; nur auf der .69 ueber kleintest.sh).
# Autor: Claude (Beweis-Agent), 2026-09-30. Plan und Herleitung: PLAN.md im selben Ordner.
# Konvention: psi = a e^{i rho t} + b e^{-i rho t}, a = A/r Y_lm (Kanal omega + rho, offen), b = B/r Y_lm (omega - rho).
#   A'' = (l(l+1)/r^2 + dp - (omega + rho)^2) A + sp B,  B'' = sp A + (l(l+1)/r^2 + dp - (omega - rho)^2) B
#   psi1 (Q-Ball selbst): dp = 1 - 4S + 9 beta S^2, sp = -2S + 6 beta S^2
#   psi2 (gemischter Ball, gfbic.py): dp = 1 - 2S + 3 beta S^2, sp = -g J S
# Krein-Norm N = int (omega + rho) A^2 + (rho - omega) B^2 dr, Energie E_2 = 2 rho N (PLAN.md),
# Gegenprobe E_2(0) = int rho^2 (A - B)^2 + (A' + B')^2 + l(l+1)(A + B)^2/r^2 + (dp + sp - omega^2)(A + B)^2 dr.
import json
import math
import sys
import time

import numpy as np
from scipy.integrate import solve_ivp, simpson

T0 = time.time()
BETA = 0.5


def log(*a):
    print("[%6.1fs]" % (time.time() - T0), *a, flush=True)


def profil(x, rend=40.0):
    """Q-Ball-Profil f(r) fuer omega^2 = x: Schiessen mit Bisektion, danach linearer Schwanz."""
    k2 = 1.0 - x
    kap0 = math.sqrt(k2)

    def N(f):
        return f * (k2 - 2.0 * f * f + 3.0 * BETA * f ** 4)

    def rhs(r, y):
        return [y[1], N(y[0]) - 2.0 * y[1] / r]

    def start(a, r0=1e-4):
        n0 = N(a)
        return [a + n0 * r0 * r0 / 6.0, n0 * r0 / 3.0]

    def ueber(r, y):
        return y[0]
    ueber.terminal = True
    ueber.direction = -1

    def unter(r, y):
        return y[1]
    unter.terminal = True
    unter.direction = 1

    top = math.sqrt((2.0 + math.sqrt(4.0 - 12.0 * BETA * k2)) / (6.0 * BETA))
    lo, hi = 0.05, top - 1e-12
    for _ in range(80):
        a = 0.5 * (lo + hi)
        s = solve_ivp(rhs, [1e-4, rend], start(a), method="DOP853", rtol=1e-12, atol=1e-15, events=[ueber, unter])
        if s.t_events[0].size > 0:
            hi = a
        elif s.t_events[1].size > 0:
            lo = a
        else:
            lo = a
        if hi - lo < 1e-15 * a:
            break
    a = 0.5 * (lo + hi)

    def klein(r, y):
        return y[0] - 1e-5 * a
    klein.terminal = True
    klein.direction = -1
    s = solve_ivp(rhs, [1e-4, rend], start(a), method="DOP853", rtol=1e-12, atol=1e-15, events=[klein],
                  dense_output=True)
    rc = float(s.t[-1])
    fc = float(s.y[0, -1])

    def f(r):
        r = np.asarray(r, dtype=float)
        out = np.empty_like(r)
        inn = r <= rc
        if inn.any():
            rr = np.maximum(r[inn], 1e-4)
            out[inn] = s.sol(rr)[0]
        if (~inn).any():
            out[~inn] = fc * (rc / r[~inn]) * np.exp(-kap0 * (r[~inn] - rc))
        return out
    return f, a, rc


def koeff(f, r, modell, g):
    S = f(np.atleast_1d(r)) ** 2
    if modell == "psi1":
        dp = 1.0 - 4.0 * S + 9.0 * BETA * S * S
        sp = -2.0 * S + 6.0 * BETA * S * S
    else:
        dp = 1.0 - 2.0 * S + 3.0 * BETA * S * S
        sp = -g * S
    return dp, sp


def hankel_geschlossen(l, kap, R):
    """reduzierte abklingende Loesung e^{-kap r} P(r), P = sum_k c_k (2 kap r)^{-k}, und Ableitung bei R"""
    P = 0.0
    dP = 0.0
    for k in range(l + 1):
        c = math.factorial(l + k) / (math.factorial(k) * math.factorial(l - k))
        P += c * (2.0 * kap * R) ** (-k)
        dP += c * (-k) * (2.0 * kap) ** (-k) * R ** (-k - 1)
    e = math.exp(-kap * (R - 30.0))          # Skalierung ohne Unterlauf
    return e * P, e * (-kap * P + dP)


def mode(x, rho, l, modell, g, R, rm, f, r0=1e-3):
    om = math.sqrt(x)
    wp2 = (om + rho) ** 2
    wm2 = (om - rho) ** 2
    kap = math.sqrt(1.0 - wm2)
    ll = l * (l + 1)

    def rhs(r, y):
        dp, sp = koeff(f, r, modell, g)
        dp = float(dp[0])
        sp = float(sp[0])
        c = ll / (r * r)
        return [y[2], y[3], (c + dp - wp2) * y[0] + sp * y[1], sp * y[0] + (c + dp - wm2) * y[1]]
    pass
    reg = []
    for kanal in (0, 1):
        y0 = [0.0, 0.0, 0.0, 0.0]
        y0[kanal] = r0 ** (l + 1)
        y0[2 + kanal] = (l + 1) * r0 ** l
        reg.append(solve_ivp(rhs, [r0, rm], y0, method="DOP853", rtol=1e-11, atol=1e-30, dense_output=True))
    B0, dB0 = hankel_geschlossen(l, kap, R)
    jost = solve_ivp(rhs, [R, rm], [0.0, B0, 0.0, dB0], method="DOP853", rtol=1e-11, atol=1e-30, dense_output=True)
    Mt = np.column_stack([reg[0].y[:, -1], reg[1].y[:, -1]])
    j = jost.y[:, -1]
    coef, res, _, _ = np.linalg.lstsq(Mt, j, rcond=None)
    rest = float(np.linalg.norm(Mt @ coef - j) / np.linalg.norm(j))
    ri = np.linspace(r0, rm, 20001)
    ra = np.linspace(rm, R, 60001)
    yi = coef[0] * reg[0].sol(ri) + coef[1] * reg[1].sol(ri)
    ya = jost.sol(ra)
    r = np.concatenate([ri, ra[1:]])
    y = np.concatenate([yi, ya[:, 1:]], axis=1)
    A, B, Ap, Bp = y
    dp, sp = koeff(f, r, modell, g)

    def integ(h):
        return simpson(h[:ri.size], x=ri) + simpson(h[ri.size - 1:], x=ra)
    Pa = integ(A * A)
    Pb = integ(B * B)
    n2 = Pa + Pb
    A, B, Ap, Bp = A / math.sqrt(n2), B / math.sqrt(n2), Ap / math.sqrt(n2), Bp / math.sqrt(n2)
    Pa, Pb = Pa / n2, Pb / n2
    N = (om + rho) * Pa + (rho - om) * Pb
    E0 = integ(rho * rho * (A - B) ** 2 + (Ap + Bp) ** 2 + ll * (A + B) ** 2 / (r * r) + (dp + sp - om * om) * (A + B) ** 2)
    # bic2-Normierung: Ursprungskoeffizient des geschlossenen Kanals B ~ n_b r^(l+1) gleich 1
    nb = coef[1] / math.sqrt(n2)
    N_bic2 = N / (nb * nb) if nb != 0 else float("nan")
    return {"R": R, "r_m": rm, "anschluss_rest": rest, "omega": om, "kappa_c": kap, "Anteil_a": Pa, "Anteil_b": Pb,
            "N": N, "K_E2": 2.0 * rho * N, "E2_t0": E0, "Verhaeltnis_E2t0_zu_2rhoN": E0 / (2.0 * rho * N),
            "N_bic2_norm_nb1": N_bic2, "A_ende": float(abs(A[-1])), "B_ende": float(abs(B[-1]))}


STELLEN = [
    ("l0n1", 0, 0.797677, 1.744618, "psi1", 0.0),
    ("l0n1_genau", 0, 0.7976767871118652, 1.7446175448373987, "psi1", 0.0),
    ("l0n2", 0, 0.685129, 1.690357, "psi1", 0.0),
    ("l0n3", 0, 0.631449, 1.652588, "psi1", 0.0),
    ("l1n1", 1, 0.754496, 1.826342, "psi1", 0.0),
    ("l1n2", 1, 0.660280, 1.717301, "psi1", 0.0),
    ("l2n1", 2, 0.643905, 1.762082, "psi1", 0.0),
    ("l2n2", 2, 0.606981, 1.694040, "psi1", 0.0),
    ("Z1_psi2_g0.2", 0, 0.7113723, 1.6888290, "psi2", 0.2),
]


def main():
    wahl = sys.argv[1].split(",") if len(sys.argv) > 1 else [s[0] for s in STELLEN]
    rm = float(sys.argv[2]) if len(sys.argv) > 2 else 4.0
    r0 = float(sys.argv[3]) if len(sys.argv) > 3 else 1e-3
    aus = []
    for name, l, x, rho, modell, g in STELLEN:
        if name not in wahl:
            continue
        f, a, rc = profil(x)
        log(name, "Profil a = %.15f, linearer Schwanz ab r = %.2f" % (a, rc))
        zeile = {"stelle": name, "l": l, "omega2": x, "rho": rho, "modell": modell, "g": g, "f0": a, "r_schwanz": rc,
                 "laeufe": []}
        for R in (36.0, 44.0):
            m = mode(x, rho, l, modell, g, R, rm, f, r0)
            zeile["laeufe"].append(m)
            log("  R = %.0f: rest %.2e  N = %.10f  Anteil_a = %.6f  K = 2 rho N = %.10f  E2(0) = %.10f  E2(0)/(2 rho N) = %.9f"
                "  N(bic2, n_b = 1) = %.6f" % (R, m["anschluss_rest"], m["N"], m["Anteil_a"], m["K_E2"], m["E2_t0"],
                                            m["Verhaeltnis_E2t0_zu_2rhoN"], m["N_bic2_norm_nb1"]))
        l1, l2 = zeile["laeufe"]
        zeile["dN_rel_zwischen_L"] = abs(l1["N"] - l2["N"]) / abs(l2["N"])
        zeile["vorzeichen"] = "positiv" if min(l1["K_E2"], l2["K_E2"], l1["E2_t0"], l2["E2_t0"]) > 0 else (
            "negativ" if max(l1["K_E2"], l2["K_E2"], l1["E2_t0"], l2["E2_t0"]) < 0 else "uneinheitlich")
        log("  Signatur:", zeile["vorzeichen"], " |dN|/N zwischen L = 36 und 44: %.2e" % zeile["dN_rel_zwischen_L"])
        aus.append(zeile)
    with open("KREIN-ERGEBNIS-r0-%g.json" % r0 if r0 != 1e-3 else "KREIN-ERGEBNIS.json", "w") as fh:
        json.dump(aus, fh, indent=1)
    log("geschrieben KREIN-ERGEBNIS.json")


if __name__ == "__main__":
    main()
