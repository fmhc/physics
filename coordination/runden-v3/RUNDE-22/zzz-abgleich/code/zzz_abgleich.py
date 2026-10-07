#!/usr/bin/env python3
# ZZZ-ABGLEICH (Runde 22): Innenwellenzahlen nach Zhang/Zhou/Zhu, arXiv:2510.27064v1, Gl. (101)-(102), (109),
# an den Leiterstellen des Papiers (RUNDE-13 3D, RUNDE-12 2D) auswerten.
# Abbildung (ARBEITSFELD.md Abschn. 1a): ihr omega_Q -> unser omega, ihr omega -> unser rho,
# ihr 1+U -> unser D = 1 - 4S + 9 beta S^2, ihr W -> unser C = -2S + 6 beta S^2, ihr g -> unser beta.
# Nur Standardbibliothek; kein numpy, kein torch. Eingabe: eingabe.json (per jq aus den Laufdateien erzeugt).
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"
import cmath
import json
import math
import sys
import time

T0 = time.time()
PI = math.pi


def DC(S, beta):
    return 1.0 - 4.0 * S + 9.0 * beta * S * S, -2.0 * S + 6.0 * beta * S * S


def innen(w2, rho, S, beta):
    """-rho_1, -rho_2 nach ZZZ Gl. (101), (102) mit unserer Abbildung."""
    D, C = DC(S, beta)
    wurzel = math.sqrt(C * C + 4.0 * w2 * rho * rho)
    m1 = w2 + rho * rho + wurzel - D
    m2 = w2 + rho * rho - wurzel - D
    return D, C, m1, m2


def k_in_papier(w2, rho, beta):
    """main.tex Z. 299-301, unabhaengig geschrieben: D_c = 1 + 1/(4 beta), C_c = 1/(2 beta)."""
    Dc = 1.0 + 1.0 / (4.0 * beta)
    Cc = 1.0 / (2.0 * beta)
    return math.sqrt(w2 + rho * rho - Dc + math.sqrt(4.0 * w2 * rho * rho + Cc * Cc))


def interp(xs, ys, x, var):
    """Lineare Interpolation in x (var='x') oder in u = 1/(x - 1/2) (var='u') zwischen den einschliessenden Zeilen."""
    if var == "u":
        t = [1.0 / (a - 0.5) for a in xs]
        z = 1.0 / (x - 0.5)
    else:
        t = list(xs)
        z = x
    paare = sorted(zip(t, ys))
    for (t0, y0), (t1, y1) in zip(paare[:-1], paare[1:]):
        if t0 <= z <= t1:
            return y0 + (y1 - y0) * (z - t0) / (t1 - t0)
    raise ValueError("x ausserhalb der Zeilen")


def stelle(sp, beta):
    w2 = sp["x_stern"]
    rho = sp["rho_stern"]
    w = math.sqrt(w2)
    eps = w2 - 0.5
    dim = sp["dim"]
    R_tw = (dim - 1) / (4.0 * math.sqrt(beta) * eps)
    R_h_u = interp(sp["x"], sp["R_halb"], w2, "u")
    R_h_x = interp(sp["x"], sp["R_halb"], w2, "x")
    S0_u = interp(sp["x"], sp["S0"], w2, "u")
    Sc = 1.0 / (2.0 * beta)
    aus = {"n": sp["n"], "dim": dim, "h": sp["h"], "quelle": sp["quelle"], "omega2": w2, "omega": w, "rho": rho,
           "eps": eps, "u": 1.0 / eps, "R_tw": R_tw, "R_halb": R_h_u, "R_halb_interp_x_minus_u": R_h_x - R_h_u,
           "S0_stelle": S0_u, "rho_minus_omega": rho - w,
           "eps_ZZZ": rho - (1.0 + w),
           "k_plus_aussen": math.sqrt((w + rho) ** 2 - 1.0),
           "kminus2_aussen": (rho - w) ** 2 - 1.0,
           "k_in_papier_Sc": k_in_papier(w2, rho, beta)}
    for name, S in (("Sc", Sc), ("S0", S0_u)):
        D, C, m1, m2 = innen(w2, rho, S, beta)
        k1 = math.sqrt(m1) if m1 > 0 else float("nan")
        k2c = cmath.sqrt(m2)
        kap2 = math.sqrt(-m2) if m2 < 0 else 0.0
        k2 = math.sqrt(m2) if m2 > 0 else 0.0
        sig_p = k1 + k2c
        sig_m = k1 - k2c
        aus[name] = {"S": S, "D": D, "C": C, "-rho1": m1, "-rho2": m2, "k1": k1, "kappa2": kap2, "k2_reell": k2,
                     "sigma_plus": [sig_p.real, sig_p.imag], "sigma_minus": [sig_m.real, sig_m.imag],
                     "abs_sigma": abs(sig_p),
                     "naiv_summe": k1 + kap2 + k2, "naiv_differenz": k1 - kap2 - k2,
                     "pi_k1": PI / k1, "pi_naiv_summe": PI / (k1 + kap2 + k2),
                     "pi_naiv_differenz": PI / (k1 - kap2 - k2) if (k1 - kap2 - k2) != 0 else float("inf"),
                     "pi_abs_sigma": PI / abs(sig_p),
                     "Phase_Rhalb_durch_pi": k1 * R_h_u / PI, "Phase_Rtw_durch_pi": k1 * R_tw / PI}
    aus["pi_2rho_ZZZ_gross"] = PI / (2.0 * rho)
    aus["pi_2omega_ZZZ_gross"] = PI / (2.0 * w)
    aus["b_lokal_Sc"] = 2.0 * math.sqrt(beta) * PI / aus["Sc"]["k1"] * (2.0 / (dim - 1))
    aus["b_lokal_S0"] = 2.0 * math.sqrt(beta) * PI / aus["S0"]["k1"] * (2.0 / (dim - 1))
    return aus


def wellen(s, name):
    """Kandidaten-Wellenzahlen X an einer Stelle (fuer Lesart name = Sc oder S0)."""
    q = s[name]
    return {"Re_sigma(=k1)": q["k1"], "naiv_Summe(k1+kappa2)": q["naiv_summe"],
            "naiv_Differenz(k1-kappa2)": q["naiv_differenz"], "|sigma|": q["abs_sigma"],
            "ZZZ_gross_omega_Summe(2rho)": 2.0 * s["rho"], "ZZZ_gross_omega_Differenz(2omega)": 2.0 * s["omega"]}


def paar(a, b):
    dn = b["n"] - a["n"]
    erg = {"von": a["n"], "nach": b["n"], "dim": a["dim"], "dn": dn,
           "dR_halb": (b["R_halb"] - a["R_halb"]) / dn, "dR_tw": (b["R_tw"] - a["R_tw"]) / dn,
           "du": (b["u"] - a["u"]) / dn, "tests": {}}
    for name in ("Sc", "S0"):
        wa, wb = wellen(a, name), wellen(b, name)
        t = {}
        for X in wa:
            xm = 0.5 * (wa[X] + wb[X])
            t[X] = {"pi_durch_X_mittel": PI / xm,
                    "dR_halb_durch_(pi/X)": erg["dR_halb"] / (PI / xm),
                    "dR_tw_durch_(pi/X)": erg["dR_tw"] / (PI / xm),
                    "Phasentest_Rhalb": (wb[X] * b["R_halb"] - wa[X] * a["R_halb"]) / (PI * dn),
                    "Phasentest_Rtw": (wb[X] * b["R_tw"] - wa[X] * a["R_tw"]) / (PI * dn)}
        erg["tests"][name] = t
    return erg


def main():
    pfad = sys.argv[1] if len(sys.argv) > 1 else "eingabe.json"
    with open(pfad) as fh:
        ein = json.load(fh)
    beta = ein["beta"]
    out = {"start": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "beta": beta}
    # Selbstpruefung: ZZZ -rho_1 bei S = S_c gleich main.tex k_in^2
    for gruppe in ("d3_h002", "d3_h004", "d2"):
        st = [stelle(sp, beta) for sp in ein[gruppe]]
        for s in st:
            s["check_kin_papier_minus_ZZZ_Sc"] = s["k_in_papier_Sc"] - s["Sc"]["k1"]
        st.sort(key=lambda s: s["n"])
        paare = []
        for a, b in zip(st[:-1], st[1:]):
            paare.append(paar(a, b))
        out[gruppe] = {"stellen": st, "paare": paare}
    # Schritte in u = 1/eps aus tab:ladder (ohne rho)
    tab = ein["tabelle_omega2"]
    ns = sorted(int(k) for k in tab)
    u = {n: 1.0 / (tab[str(n)] - 0.5) for n in ns}
    out["tabelle_u_schritte"] = [{"von": a, "nach": b, "du": u[b] - u[a],
                                  "dR_tw_3D": (u[b] - u[a]) / (2.0 * math.sqrt(beta)),
                                  "k_eff_aus_dR_tw": PI * 2.0 * math.sqrt(beta) / (u[b] - u[a])}
                                 for a, b in zip(ns[:-1], ns[1:])]
    out["sek"] = time.time() - T0
    with open("zzz_abgleich.json", "w") as fh:
        json.dump(out, fh, indent=1)
    # Kurzausgabe
    for gruppe in ("d3_h002", "d3_h004", "d2"):
        print(f"=== {gruppe}")
        for s in out[gruppe]["stellen"]:
            print(f"n={s['n']:2d} w2={s['omega2']:.7f} rho={s['rho']:.6f} epsZZZ={s['eps_ZZZ']:+.4f} "
                  f"k-^2={s['kminus2_aussen']:+.4f} R_halb={s['R_halb']:.4f} R_tw={s['R_tw']:.4f} S0={s['S0_stelle']:.5f} "
                  f"chk={s['check_kin_papier_minus_ZZZ_Sc']:.1e} dRinterp={s['R_halb_interp_x_minus_u']:.1e}")
            for name in ("Sc", "S0"):
                q = s[name]
                print(f"    {name}: -rho1={q['-rho1']:.5f} -rho2={q['-rho2']:+.5f} k1={q['k1']:.5f} kappa2={q['kappa2']:.5f} "
                      f"pi/k1={q['pi_k1']:.4f} pi/(k1+kap)={q['pi_naiv_summe']:.4f} pi/(k1-kap)={q['pi_naiv_differenz']:.4f} "
                      f"pi/|sig|={q['pi_abs_sigma']:.4f} PhiRh={q['Phase_Rhalb_durch_pi']:.4f} PhiRtw={q['Phase_Rtw_durch_pi']:.4f}")
            print(f"    pi/(2rho)={s['pi_2rho_ZZZ_gross']:.4f} pi/(2omega)={s['pi_2omega_ZZZ_gross']:.4f} "
                  f"b_lokal Sc/S0 = {s['b_lokal_Sc']:.4f}/{s['b_lokal_S0']:.4f}")
        for p in out[gruppe]["paare"]:
            print(f"  Paar {p['von']}->{p['nach']} (dn={p['dn']}): dR_halb={p['dR_halb']:.4f} dR_tw={p['dR_tw']:.4f} du={p['du']:.4f}")
            for name in ("Sc", "S0"):
                for X, t in p["tests"][name].items():
                    print(f"    {name} {X:34s} pi/X={t['pi_durch_X_mittel']:.4f} dRh/(pi/X)={t['dR_halb_durch_(pi/X)']:.4f} "
                          f"dRtw/(pi/X)={t['dR_tw_durch_(pi/X)']:.4f} Phase(Rh)={t['Phasentest_Rhalb']:.4f} "
                          f"Phase(Rtw)={t['Phasentest_Rtw']:.4f}")
    print("=== Schritte in u (tab:ladder)")
    for r in out["tabelle_u_schritte"]:
        print(f"  {r['von']:2d}->{r['nach']:2d}: du={r['du']:.4f} dR_tw={r['dR_tw_3D']:.4f} k_eff={r['k_eff_aus_dR_tw']:.4f}")
    print(f"sek={out['sek']:.3f}")


if __name__ == "__main__":
    main()
