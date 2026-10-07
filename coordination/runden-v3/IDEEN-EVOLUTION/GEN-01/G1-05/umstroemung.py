#!/usr/bin/env python3
"""G1-05 Teil (a): stationaere Umstroemung einer festen Ball-Delle im chi-Kondensat, Sattel-Knoten u_SN per Schiessen.

Neuer Code (die Karte erlaubt ihn fuer Teil a). Formeln wie coordination/runden-v3/RUNDE-06/medium1d/medium1d.py:
om0 = sqrt(mc2 + 2 g4 C0), schall (c_s), k_stroemung (Lorentz: K = gamma om0 u, Omega = gamma om0), Ballprofil des
analytischen 1D-Ankers bei omega^2 = 0,7 (S = 2 a0/(1 + b0 cosh(2 sqrt(a0) x))), G4 = 0,5, MC2 = 1, LAM = 0,1.
Rueckwirkung des Mediums auf den Ball vernachlaessigt (Karte).

Stationaer: chi = a(x) exp(i(theta - Omega t)), a^2 theta' = J = C0 K,
            a'' = [mc2 + 2 g4 a^2 + lam S(x) - Omega^2] a + J^2 / a^3.
Symmetrische Loesung, geschossen von der Mitte nach aussen (Formprobe 08:08: Schiessen von x0 = -60 aus brauchte
delta ~ exp(-kappa 60) unter 1e-15 und fand beim gestreckten Profil nichts, daher umgestellt):
            a(0) = a_c, a'(0) = 0, RK4 bis x = 60 (gestreckt: 60 x Streckung).
Klasse +1: a steigt ueber a0 = sqrt(C0); Klasse -1: a' < 0, bevor a0 erreicht ist. Die Loesung, die gegen den
Fixpunkt a0 laeuft (Sattel fuer u < c_s), liegt auf einer Trennlinie zwischen +1 und -1 im Raster von a_c
(2000 Werte, 1 - a_c/a0 logarithmisch in [1e-8; 0,999]). Loesung vorhanden = mindestens ein Klassenwechsel.
u steigt in 0,05 c_s bis zum ersten u ohne Loesung, dann in 0,005 c_s im Intervall davor; u_SN = letztes u mit Loesung
(Klammer bis zum ersten u ohne). RK4 mit h = 0,01 und h = 0,005 (L3).
Hydraulische Zahl (Karte, Papier): 1 + M^2/2 = (3/2) M^(2/3) + beta, beta = lam S_max/(2 g4 C0).

Aufruf: python umstroemung.py [--c0 0.1,0.2,0.3] [--kontrollen ja|nein] [--h 0.01] [--out ORDNER] [--rauch]
Ausgabe: umstroemung_ergebnis.json und umstroemung_bericht.txt (V1, Kontrollen, Plausibilitaet, L3, Vorgabe fuer b).
"""
import argparse
import datetime
import json
import math
import os
import time

import torch

F64 = torch.float64
G4, MC2, LAM = 0.5, 1.0, 0.1
W2_BALL = 0.7
X_MAX = 60.0                       # Integration von x = 0 bis X_MAX x streck
DU_REL = 0.005
N_AC = 2000                        # Raster der Mitteldichte a_c
V1_KLAMMER = {0.1: (0.33, 0.53), 0.3: (0.54, 0.77)}
B_OFFSETS = (-0.15, -0.05, 0.05, 0.15, 0.30)


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def om0(c):
    return math.sqrt(MC2 + 2.0 * G4 * c)


def schall(c):
    g = 2.0 * G4 * c
    return math.sqrt(g / (2.0 * (MC2 + g) + g)) if c > 0.0 else 0.0


def s_ball(x, streck=1.0):
    a0, b0 = 1.0 - W2_BALL, math.sqrt(2.0 * W2_BALL - 1.0)
    y = x / streck
    return 2.0 * a0 / (1.0 + b0 * torch.cosh((2.0 * math.sqrt(a0) * y).clamp(-700.0, 700.0)))


def s_max():
    a0, b0 = 1.0 - W2_BALL, math.sqrt(2.0 * W2_BALL - 1.0)
    return 2.0 * a0 / (1.0 + b0)


def hydraulisch(c0, lam):
    beta = lam * s_max() / (2.0 * G4 * c0)
    if beta >= 1.0:
        return 0.0
    lo, hi = 1e-12, 1.0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if 1.0 + 0.5 * m * m - 1.5 * m ** (2.0 / 3.0) - beta > 0.0:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


def klassen(c0, lam, u, ac, h, streck, x_max):
    """Schiessen von der Mitte: a(0) = ac, a'(0) = 0, RK4 bis x_max. u: (U, 1), ac: (U, D).
    Klasse +1: a steigt ueber a0 (ueberschiesst); -1: a' < 0 fuer x > 0, bevor a0 erreicht ist (dreht um); 0: offen.
    Die gesuchte Loesung (Anlauf gegen a0) liegt auf der Trennlinie zwischen +1 und -1."""
    a0 = math.sqrt(c0)
    w = om0(c0)
    gam = 1.0 / torch.sqrt(1.0 - u * u)
    k = gam * w * u
    om2 = (gam * w) ** 2
    j2 = (c0 * k) ** 2
    a = ac.clone()
    p = torch.zeros_like(a)
    kl = torch.zeros_like(a, dtype=torch.int8)
    n = int(round(x_max / h))
    xs = h * torch.arange(n + 1, dtype=F64)
    sx = s_ball(xs, streck)
    sm = s_ball(xs + 0.5 * h, streck)

    def f(aa, s):
        return (MC2 + 2.0 * G4 * aa * aa + lam * s - om2) * aa + j2 / aa ** 3

    for i in range(n):
        s0, s1, s2 = float(sx[i]), float(sm[i]), float(sx[i + 1])
        k1a, k1p = p, f(a, s0)
        k2a, k2p = p + 0.5 * h * k1p, f(a + 0.5 * h * k1a, s1)
        k3a, k3p = p + 0.5 * h * k2p, f(a + 0.5 * h * k2a, s1)
        k4a, k4p = p + h * k3p, f(a + h * k3a, s2)
        a = a + (h / 6.0) * (k1a + 2.0 * k2a + 2.0 * k3a + k4a)
        p = p + (h / 6.0) * (k1p + 2.0 * k2p + 2.0 * k3p + k4p)
        offen = kl == 0
        ueber = offen & (~torch.isfinite(a) | (a > a0))
        unter = offen & ~ueber & (p < 0.0)
        kl = torch.where(ueber, torch.ones_like(kl), kl)
        kl = torch.where(unter, -torch.ones_like(kl), kl)
        fertig = kl != 0
        a = torch.where(fertig, torch.full_like(a, a0), a)
        p = torch.where(fertig, torch.zeros_like(p), p)
        if bool(fertig.all()):
            break
    return kl


def existenz(c0, lam, us, h, streck, n_ac):
    """Je u: gibt es eine Trennlinie (+1 neben -1) im Raster von ac? ac = a0 (1 - d), d log-verteilt in [1e-8, 0,999]."""
    a0 = math.sqrt(c0)
    u = torch.tensor(us, dtype=F64).unsqueeze(1)
    d = torch.logspace(-8.0, math.log10(0.999), n_ac, dtype=F64)
    ac = (a0 * (1.0 - d)).unsqueeze(0).expand(len(us), -1).contiguous()
    kl = klassen(c0, lam, u, ac, h, streck, X_MAX * streck)
    wechsel = []
    for zeile in kl.tolist():
        nz = [c for c in zeile if c != 0]            # offene Punkte (nahe der Trennlinie) nicht als Trenner zaehlen
        wechsel.append(sum(1 for p, q in zip(nz[:-1], nz[1:]) if p * q < 0))
    offen = (kl == 0).sum(dim=1)
    return [w > 0 for w in wechsel], wechsel, offen.tolist()


def u_sn(c0, lam, h, streck, rauch):
    """u steigt in 0,05 c_s bis zum ersten u ohne Loesung, dann in 0,005 c_s im Intervall davor (Raster 0,005 c_s)."""
    cs = schall(c0)
    n_ac = N_AC // (8 if rauch else 1)
    grob = [round(0.05 * (j + 1), 6) for j in range(19)]                    # 0,05 ... 0,95
    if rauch:
        grob = grob[::4]
    ex, we, of = existenz(c0, lam, [r * cs for r in grob], h, streck, n_ac)
    erstes_ohne_grob = next((r for r, e in zip(grob, ex) if not e), None)
    luecke = any(e for r, e in zip(grob, ex) if erstes_ohne_grob is not None and r > erstes_ohne_grob)
    if erstes_ohne_grob is None:
        lo, hi = grob[-1], 1.0
    else:
        i = grob.index(erstes_ohne_grob)
        lo, hi = (grob[i - 1] if i > 0 else 0.0), erstes_ohne_grob
    fein = [round(lo + DU_REL * (j + 1), 6) for j in range(int(round((hi - lo) / DU_REL)) - 1)]
    if rauch:
        fein = fein[::5]
    letztes, erstes_ohne = (lo if lo > 0.0 else None), hi
    if fein:
        ex2, we2, of2 = existenz(c0, lam, [r * cs for r in fein], h, streck, n_ac)
        for r, e in zip(fein, ex2):
            if e:
                letztes = r
            else:
                erstes_ohne = r
                break
    else:
        ex2, we2, of2 = [], [], []
    return {"C0": c0, "lam": lam, "h": h, "streck": streck, "c_s": cs, "u_SN_zu_cs": letztes,
            "erstes_ohne_zu_cs": erstes_ohne, "loesung_bei_hoeherem_u_nach_luecke": luecke,
            "grob": [[r, e, w, o] for r, e, w, o in zip(grob, ex, we, of)],
            "fein": [[r, e, w, o] for r, e, w, o in zip(fein, ex2, we2, of2)], "n_ac": n_ac}


def main():
    ap = argparse.ArgumentParser(description="G1-05 (a): Sattel-Knoten der stationaeren Umstroemung")
    ap.add_argument("--c0", default="0.1,0.2,0.3")
    ap.add_argument("--kontrollen", choices=["ja", "nein"], default="ja")
    ap.add_argument("--h", type=float, default=0.01, help="RK4-Schritt; L3 rechnet zusaetzlich h/2")
    ap.add_argument("--streck", type=float, default=4.0, help="Kontrolle: S(x/streck)")
    ap.add_argument("--lam-klein", type=float, default=0.01, help="Kontrolle: schwaches Hindernis")
    ap.add_argument("--out", default=None)
    ap.add_argument("--rauch", action="store_true", help="Formprobe: jedes 20. u, weniger delta (Zahlen ungueltig)")
    args = ap.parse_args()
    torch.set_num_threads(1)
    out = args.out or os.path.join(os.path.dirname(os.path.abspath(__file__)), "ausgabe")
    os.makedirs(out, exist_ok=True)
    start = jetzt()
    t0 = time.perf_counter()
    c0s = [float(c) for c in args.c0.split(",") if c.strip()]
    haupt, kontrolle, l3 = [], [], []
    for c0 in c0s:
        grob = u_sn(c0, LAM, args.h, 1.0, args.rauch)
        fein = u_sn(c0, LAM, 0.5 * args.h, 1.0, args.rauch)
        grob["M_hydr"] = hydraulisch(c0, LAM)
        haupt.append(grob)
        a, b = grob["u_SN_zu_cs"], fein["u_SN_zu_cs"]
        aend = abs(a - b) if a is not None and b is not None else None
        eff = (1.0 - a) if a is not None else None
        l3.append({"C0": c0, "u_SN_h": a, "u_SN_h2": b, "aenderung": aend, "effekt_1_minus_uSN": eff,
                   "bestanden": aend is not None and aend <= DU_REL + 1e-12 and eff is not None
                   and eff >= 5.0 * aend})
        print(f"C0 {c0}: u_SN/c_s {a} (h) / {b} (h/2), hydraulisch {grob['M_hydr']:.4f}, "
              f"{time.perf_counter() - t0:.1f} s", flush=True)
        if args.kontrollen == "ja":
            kl = u_sn(c0, args.lam_klein, args.h, 1.0, args.rauch)
            st = u_sn(c0, LAM, args.h, args.streck, args.rauch)
            st["M_hydr"] = hydraulisch(c0, LAM)
            kontrolle.append({"C0": c0, "lam_klein": kl, "gestreckt": st,
                              "lam_klein_ok": kl["u_SN_zu_cs"] is not None and kl["u_SN_zu_cs"] >= 0.9,
                              "gestreckt_ok": st["u_SN_zu_cs"] is not None
                              and abs(st["u_SN_zu_cs"] - st["M_hydr"]) <= 0.05})
            print(f"  Kontrollen C0 {c0}: lam {args.lam_klein} -> {kl['u_SN_zu_cs']}, gestreckt x{args.streck} -> "
                  f"{st['u_SN_zu_cs']} (hydraulisch {st['M_hydr']:.4f}), {time.perf_counter() - t0:.1f} s", flush=True)
    # V1 und Plausibilitaet
    v1 = []
    for z in haupt:
        if z["C0"] in V1_KLAMMER:
            lo, hi = V1_KLAMMER[z["C0"]]
            r = z["u_SN_zu_cs"]
            v1.append({"C0": z["C0"], "u_SN_zu_cs": r, "klammer": [lo, hi],
                       "erfuellt": r is not None and lo <= r <= hi and z["M_hydr"] <= r <= 1.0})
    verst = []
    for z in haupt:
        r = z["u_SN_zu_cs"]
        if r is None:
            verst.append(f"C0 {z['C0']}: keine Loesung schon bei 0,005 c_s")
        elif not (z["M_hydr"] <= r <= 1.0):
            verst.append(f"C0 {z['C0']}: u_SN/c_s {r} nicht zwischen hydraulisch {z['M_hydr']:.4f} und 1")
        if z["loesung_bei_hoeherem_u_nach_luecke"]:
            verst.append(f"C0 {z['C0']}: Loesung taucht nach einer Luecke wieder auf (Suche pruefen)")
    plaus = {"bestanden": not verst, "verstoesse": verst,
             "hinweis": "Ladungserhaltung, Solitonen und Kraft gehoeren zu Teil b (nicht in diesem Code)"}
    scheitert_v1 = [x for x in v1 if not x["erfuellt"]]
    ausgang = ("Plausibilitaetsschranke nicht bestanden: kein Ausgang" if not plaus["bestanden"] else
               ("scheitert (V1): " + ", ".join(f"C0 {x['C0']} u_SN/c_s {x['u_SN_zu_cs']}" for x in scheitert_v1))
               if scheitert_v1 else "V1 erfuellt (Teil a); Teil b offen")
    vorgabe_b = None
    z2 = next((z for z in haupt if abs(z["C0"] - 0.2) < 1e-12), None)
    if z2 is not None and z2["u_SN_zu_cs"] is not None:
        vorgabe_b = {"C0": 0.2, "c_s": z2["c_s"], "u_SN_zu_cs": z2["u_SN_zu_cs"],
                     "u_zu_cs": [round(z2["u_SN_zu_cs"] + o, 4) for o in B_OFFSETS],
                     "u": [round((z2["u_SN_zu_cs"] + o) * z2["c_s"], 6) for o in B_OFFSETS]}
    text = [f"umstroemung G1-05 (a). Start {start}, Ende {jetzt()}, cpu, {time.perf_counter() - t0:.1f} s"
            + (" RAUCHTEST: Zahlen ungueltig" if args.rauch else "")]
    for z, l in zip(haupt, l3):
        text.append(f"  C0 {z['C0']}: c_s {z['c_s']:.4f}, hydraulisch {z['M_hydr']:.4f}, u_SN/c_s {l['u_SN_h']} (h) "
                    f"{l['u_SN_h2']} (h/2), erstes ohne {z['erstes_ohne_zu_cs']}; L3 {l['bestanden']}")
    for k in kontrolle:
        text.append(f"  Kontrolle C0 {k['C0']}: lam klein -> {k['lam_klein']['u_SN_zu_cs']} (ok {k['lam_klein_ok']}), "
                    f"gestreckt -> {k['gestreckt']['u_SN_zu_cs']} gegen {k['gestreckt']['M_hydr']:.4f} "
                    f"(ok {k['gestreckt_ok']})")
    text.append(f"V1: {[(x['C0'], x['u_SN_zu_cs'], x['erfuellt']) for x in v1]}")
    text.append(f"Plausibilitaetsschranke: bestanden = {plaus['bestanden']} {verst}")
    text.append(f"Ausgang Teil a: {ausgang}")
    text.append(f"Vorgabe fuer Teil b (C0 = 0,2): {vorgabe_b}")
    ausgabe = {"test": "umstroemung", "start": start, "ende": jetzt(), "rauch": args.rauch, "argumente": vars(args),
               "konstanten": {"G4": G4, "MC2": MC2, "LAM": LAM, "W2_BALL": W2_BALL, "X_MAX": X_MAX, "N_AC": N_AC, "DU_REL": DU_REL},
               "haupt": haupt, "kontrollen": kontrolle, "l3": l3, "v1": v1, "plausibilitaet": plaus,
               "ausgang": ausgang, "vorgabe_b": vorgabe_b}
    name = "umstroemung_" + "_".join(f"{c:g}" for c in c0s)
    with open(os.path.join(out, name + "_ergebnis.json"), "w") as fh:
        json.dump(ausgabe, fh, indent=1)
    with open(os.path.join(out, name + "_bericht.txt"), "w") as fh:
        fh.write("\n".join(text) + "\n")
    print("\n".join(text), flush=True)


if __name__ == "__main__":
    main()
