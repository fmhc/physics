# PROFILE-1: Profildaten fuer Abb. 3 des Leiter-Papers (Hintergrund f und Modenkomponenten), float64.
# Autor: Claude (Beweis-Agent), 2026-09-30. Nutzt krein.py (KREIN-1) unveraendert per Import (profil, koeff,
# hankel_geschlossen); Eigenfunktion wie krein.mode, hier mit Ausgabe der Felder auf einem festen Gitter.
# Konvention: psi = a e^{i rho t} + b e^{-i rho t} um phi = e^{i omega t} f; a = A/r Y_lm (Kanal omega + rho, offen),
# b = B/r Y_lm (Kanal omega - rho, geschlossen). Normierung wie KREIN-1: int_0^R (A^2 + B^2) dr = 1 (R = 44,
# Y_lm reell normiert). Vorzeichen: B ~ n_b r^(l+1) mit n_b > 0.
import hashlib
import json
import math
import os
import sys
import time

import numpy as np
from scipy.integrate import solve_ivp, simpson

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HIER))
import krein as KR  # noqa: E402

T0 = time.time()


def log(*a):
    print("[%6.1fs]" % (time.time() - T0), *a, flush=True)


def g12(v):
    return [float("%.12g" % w) for w in np.asarray(v, dtype=float).ravel()]


def felder(x, rho, l, R=44.0, rm=4.0, r0=1e-5, rgit=None):
    f, a0, rc = KR.profil(x)
    om = math.sqrt(x)
    wp2 = (om + rho) ** 2
    wm2 = (om - rho) ** 2
    kap = math.sqrt(1.0 - wm2)
    ll = l * (l + 1)

    def rhs(r, y):
        dp, sp = KR.koeff(f, r, "psi1", 0.0)
        dp = float(dp[0])
        sp = float(sp[0])
        c = ll / (r * r)
        return [y[2], y[3], (c + dp - wp2) * y[0] + sp * y[1], sp * y[0] + (c + dp - wm2) * y[1]]
    reg = []
    for kanal in (0, 1):
        y0 = [0.0, 0.0, 0.0, 0.0]
        y0[kanal] = r0 ** (l + 1)
        y0[2 + kanal] = (l + 1) * r0 ** l
        reg.append(solve_ivp(rhs, [r0, rm], y0, method="DOP853", rtol=1e-11, atol=1e-30, dense_output=True))
    B0, dB0 = KR.hankel_geschlossen(l, kap, R)
    jost = solve_ivp(rhs, [R, rm], [0.0, B0, 0.0, dB0], method="DOP853", rtol=1e-11, atol=1e-30, dense_output=True)
    Mt = np.column_stack([reg[0].y[:, -1], reg[1].y[:, -1]])
    j = jost.y[:, -1]
    coef, _, _, _ = np.linalg.lstsq(Mt, j, rcond=None)
    rest = float(np.linalg.norm(Mt @ coef - j) / np.linalg.norm(j))

    def eig(r):
        r = np.asarray(r, dtype=float)
        out = np.zeros((4, r.size))
        inn = r < rm
        if inn.any():
            rr = np.maximum(r[inn], r0)
            out[:, inn] = coef[0] * reg[0].sol(rr) + coef[1] * reg[1].sol(rr)
        if (~inn).any():
            out[:, ~inn] = jost.sol(r[~inn])
        return out
    # Normierung (wie krein.mode): int_r0^R (A^2 + B^2) dr = 1, Simpson auf feinem Gitter
    ri = np.linspace(r0, rm, 20001)
    ra = np.linspace(rm, R, 60001)
    yi = eig(ri)
    ya = eig(ra)
    n2 = simpson(yi[0] ** 2 + yi[1] ** 2, x=ri) + simpson(ya[0] ** 2 + ya[1] ** 2, x=ra)
    nb = coef[1] / math.sqrt(n2)
    s = 1.0 / math.sqrt(n2) * (1.0 if nb > 0 else -1.0)
    Pa = (simpson(yi[0] ** 2, x=ri) + simpson(ya[0] ** 2, x=ra)) / n2
    N = (om + rho) * Pa + (rho - om) * (1.0 - Pa)
    y = eig(rgit) * s
    A, B, Ap, Bp = y
    A = np.where(rgit > 0, A, 0.0)
    B = np.where(rgit > 0, B, 0.0)
    fr = np.where(rgit > 0, f(np.maximum(rgit, 1e-4)), a0)   # r = 0: exakter Grenzwert f(0) = a
    S = fr * fr
    _, sp = KR.koeff(f, np.maximum(rgit, 1e-4), "psi1", 0.0)
    with np.errstate(divide="ignore", invalid="ignore"):
        av = np.where(rgit > 0, A / rgit, (Ap if l == 0 else 0.0))
        bv = np.where(rgit > 0, B / rgit, (Bp if l == 0 else 0.0))
    kap0 = math.sqrt(1.0 - x)
    eps = x - 0.5
    Rtw = 1.0 / (2.0 * math.sqrt(KR.BETA) * eps)

    def kreuz(wert):
        idx = np.where(S < wert)[0]
        return float(rgit[idx[0]]) if idx.size else None
    return {"omega2": x, "rho": rho, "omega": om, "k_offen": math.sqrt(wp2 - 1.0), "kappa_c": kap, "kappa0": kap0,
            "f0": a0, "anschluss_rest": rest, "n_b": abs(nb), "Anteil_a": Pa, "N_krein": N, "K_E2": 2.0 * rho * N,
            "zonen_hilfe": {"R_tw_formel": Rtw, "wurzel_beta": math.sqrt(KR.BETA),
                            "r_bei_S_gleich_Sc_halbe": kreuz(0.5), "r_bei_sp_gleich_0": kreuz(2.0 / 3.0)},
            "f": g12(fr), "S": g12(S), "sp": g12(sp), "A": g12(A), "B": g12(B),
            "a": g12(av), "b": g12(bv)}


STELLEN = [("l0n1", 0, 1, 0.7976767871118652, 1.7446175448373987, "Beweiswerte BEWEIS-1 (z0, Mittelpunkte)"),
           ("l0n2", 0, 2, 0.685129, 1.690357, "RUNDE-07.md / MODELL-DUENNWAND.md"),
           ("l0n3", 0, 3, 0.631449, 1.652588, "RUNDE-07.md"),
           ("l1n1", 1, 1, 0.754496, 1.826342, "RUNDE-08/sp1/ERGEBNIS.md")]


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    rgit = np.round(np.arange(0, 3001) * 0.01, 10)
    aus = {"auftrag": "PROFILE-1 (Leitung, Runde 10): Profildaten fuer Abb. 3 des Leiter-Papers",
           "konvention": ("phi = e^{i omega t} (f + a e^{i rho t} + b e^{-i rho t}), a = A(r)/r Y_lm (Kanal omega + rho, offen), "
                          "b = B(r)/r Y_lm (Kanal omega - rho, geschlossen); A, B reduziert; U = S - S^2 + S^3/2, S = f^2; "
                          "sp = U''(S) S = -2S + 3S^2 (Kopplung, Vorzeichenwechsel bei S = 2/3)"),
           "normierung": ("wie KREIN-1: int_0^44 (A^2 + B^2) dr = 1 je Einheitswinkelnorm (Y_lm reell normiert); "
                          "Vorzeichen so, dass B ~ n_b r^(l+1) mit n_b > 0; a(0), b(0) bei l = 0 als Grenzwert A'(0), B'(0)"),
           "r": rgit.tolist(), "r_einheit": "dimensionslos (Masse 1)", "stellen": [],
           "code_sha256": {"profile.py": sha(os.path.abspath(__file__)), "krein.py": sha(KR.__file__)}}
    for name, l, n, x, rho, quelle in STELLEN:
        d = felder(x, rho, l, rgit=rgit)
        d.update({"name": name, "l": l, "n": n, "quelle_omega2_rho": quelle})
        aus["stellen"].append(d)
        log(name, "f0 = %.15f rest %.2e Anteil_a %.6f N %.10f K %.10f R_tw %.3f r(S=1/2) %s r(sp=0) %s" % (
            d["f0"], d["anschluss_rest"], d["Anteil_a"], d["N_krein"], d["K_E2"], d["zonen_hilfe"]["R_tw_formel"],
            d["zonen_hilfe"]["r_bei_S_gleich_Sc_halbe"], d["zonen_hilfe"]["r_bei_sp_gleich_0"]))
    with open(os.path.join(HIER, "PROFILE.json"), "w") as fh:
        json.dump(aus, fh)
    log("geschrieben PROFILE.json")


if __name__ == "__main__":
    main()
