#!/usr/bin/env python3
"""BILDUNG-2 (Runde 22, v3): Woran scheiterten die KF-5-Tropfen: Groesse, Wellenbad oder Verschmelzen?

Karte: coordination/runden-v3/RUNDE-22/bildung-2/KARTE.md; Plan (vor dem ersten echten Lauf eingefroren): PLAN.md.
Importiert unveraendert (nur gelesen, ohne Bytecode):
  - bildung1.py (Runde 22, /home/fmh/fmhc-physics-remote/runde22-bildung-1): radius_definitionen, klumpen_feld,
    absorber (Box 96), diag_zeile und die Konstanten (W2_F, BOX, ABS_BREITE, ABS_SIGMA, T_FEN, T_DIAG, S0_HAUPT,
    S0_ZUSATZ, BALL_SUCH, K_TOL, R_TOL_DEF, RINGE, MASKE_ABSTAND, GAUSS_FAKTOR, ZEITGRENZE_S, RAUCH_*).
  - darueber, wie in BILDUNG-1: kf5_geburt.py (R6: Gitter, kraft_fn, dichten, komponenten, eigenschaften, analyse_arm,
    fenster_start, fenster_probe, fenster_auswerten, Familie, Konstanten) und kf_eich.py (R21: profil, ball_feld,
    omega_gitter, familien_abstaende, familien_knoten, Hilfen).
Neu hier: Arm A (Klumpen (i) bei omega^2 0,52, Box 128), Wellenbad (Arm B, K-Arm B0, Zusatz BAD = Bad allein),
Arm C (zwei Klumpen (i) bei 0,60, Mittenabstand 3 R_F, gleichphasig) mit Gebietszahl-Reihe, Auswertung C0 bis C4.

Verlet und Absorber wie bildung1.befehl_lauf (Zeile fuer Zeile nachgebaut):
    vel += F dt/2; psi += vel dt; psi *= m; F = kraft(psi); vel += F dt/2; vel *= m
Absorber in der Form von bildung1.absorber (Breite 16, sigma_max 1, sigma = sigma_max xi^2), innen = Box/2 - 16; fuer
Box 96 bitgleich mit bildung1.absorber (Pruefung im Lauf).
Wellenbad: Summe der Gittermoden k = 2 pi n / Box mit BAD_K[0] <= |k| <= BAD_K[1], gleiche Amplitude, Phase gleich-
verteilt (fester Seed BAD_SAAT, CPU-Generator), positive Frequenz omega_k = sqrt(1 + k^2) (freie Dispersion um psi = 0,
U'(0) = 1): psi = sum c e^{i k.x}, psi_t = sum (-i omega_k) c e^{i k.x}; Ladung in der Box Box^2 sum 2 omega_k |c|^2 =
BAD_ANTEIL Q_F (Gitter: exakt, Moden orthogonal). Grob und fein: dieselbe kontinuierliche Funktion.

Aufruf:  python bildung2.py lauf --stufe grob|fein --gruppe a|A|bc|b|c --von T0 --bis T1 [--rauch]
         python bildung2.py zusammen --geraet cpu
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"
import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import glob  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import types  # noqa: E402

R6 = "/home/fmh/fmhc-physics-remote/runde6-kf5"
R21 = "/home/fmh/fmhc-physics-remote/runde21-kf-eich"
R22B1 = "/home/fmh/fmhc-physics-remote/runde22-bildung-1"
sys.path.insert(0, R6)
sys.path.insert(1, R21)
sys.path.insert(2, R22B1)
import torch  # noqa: E402
import kf5_geburt as kg  # noqa: E402
import kf_eich as ke  # noqa: E402
import bildung1 as b1  # noqa: E402

HIER = os.path.dirname(os.path.abspath(__file__))
F64 = torch.float64
C128 = torch.complex128
z7 = kg.z7

# ---- feste Parameter (PLAN.md, vor dem Rauchlauf im Code festgelegt) ----
W2_A = 0.52                                     # Arm A: Familienpunkt omega^2 0,52 (Knoten der Familiendatei)
W2_BC = b1.W2_F                                 # Arme B, C: 0,60 wie BILDUNG-1
BOX_A = 128.0                                   # Arm A: groessere Box (Plan, Abschnitt 4)
BOX_BC = b1.BOX                                 # 96 wie BILDUNG-1
T_ENDE = 1000.0
T_FEN = b1.T_FEN                                # Fensterenden 50, 100, 200, 250, 500, 1000; Fenster [T - 40, T]
T_KARTE = (100.0, 250.0, 500.0, 1000.0)
S0_HAUPT, S0_ZUSATZ = b1.S0_HAUPT, b1.S0_ZUSATZ
BAD_ANTEIL = 0.20                               # Ladung des Bads in der Box = 20 % von Q_F (Karte)
BAD_K = (0.25, 1.0)                             # Band |k|
BAD_SAAT = 2202
C_ABSTAND_R = 3.0                               # Arm C: Mittenabstand 3 R_F (Karte)
DICHT_DT, DICHT_BIS = 1.0, 100.0                # Gebietszahl alle 1 bis t = 100, danach alle T_DIAG
VERSCHMOLZEN_MITTE = 2.0                        # verschmolzen: ein Gebiet, rund, Schwerpunkt <= 2 von der Mitte
GEBIET_LISTE_MAX = 6
RINGE_A = (12.0, 24.0, 32.0, 48.0)
R_BALLRING = {96.0: 12.0, 128.0: 24.0}         # Q(r <= R) am Fensterbeginn als zweites Ladungsmass
FAELLE = {
    "A": {"box": BOX_A, "w2": W2_A, "art": "klumpen"},
    "KA": {"box": BOX_A, "w2": W2_A, "art": "ball"},
    "B": {"box": BOX_BC, "w2": W2_BC, "art": "klumpen+bad"},
    "B0": {"box": BOX_BC, "w2": W2_BC, "art": "ball+bad"},
    "BAD": {"box": BOX_BC, "w2": W2_BC, "art": "bad"},
    "C": {"box": BOX_BC, "w2": W2_BC, "art": "zwei_klumpen"},
}
GRUPPEN = {"a": ["A", "KA"], "A": ["A"], "bc": ["B0", "B", "BAD", "C"], "b": ["B0", "B", "BAD"], "c": ["C"]}


# ---------------------------------------------------------------- Hilfen

def absorber_box(g, dt):
    """Wie bildung1.absorber, aber innen = Box/2 - Breite aus der eigenen Box (bildung1: fest Box 96)."""
    innen = 0.5 * g.box - b1.ABS_BREITE
    ax = ((g.x1.abs() - innen) / b1.ABS_BREITE).clamp(0.0, 1.0)
    xi = torch.maximum(ax.view(1, -1), ax.view(-1, 1))
    sigma = b1.ABS_SIGMA * xi * xi
    return torch.exp(-sigma * dt).contiguous(), (xi > 0.0).to(F64), innen


def bad_felder(g, q_soll):
    """Wellenbad (Formel im Kopf der Datei). Rueckgabe psi, vel (n, n) und Kennzahlen."""
    k1 = 2.0 * math.pi / g.box
    nc = int(math.floor(BAD_K[1] / k1)) + 1
    m = 2 * nc + 1
    gen = torch.Generator().manual_seed(BAD_SAAT)
    phi = 2.0 * math.pi * torch.rand((m, m), generator=gen, dtype=F64)
    j = torch.arange(-nc, nc + 1, dtype=F64)
    ky, kx = (k1 * j).view(-1, 1), (k1 * j).view(1, -1)
    kk = torch.sqrt(ky * ky + kx * kx)
    band = ((kk >= BAD_K[0]) & (kk <= BAD_K[1])).to(F64)
    om = torch.sqrt(1.0 + kk * kk)
    n_moden = int(band.sum().item())
    summe_om = float((om * band).sum().item())
    amp = math.sqrt(q_soll / (2.0 * g.box * g.box * summe_om))
    c = (amp * torch.exp(1j * phi)) * band                       # [Mode y, Mode x]
    cv = (-1j * om) * c
    welle = torch.exp(1j * k1 * (j.to(kg.DEV).view(-1, 1) * g.x1.view(1, -1)))      # (m, n)
    psi = (welle.T @ c.to(kg.DEV) @ welle).contiguous()
    vel = (welle.T @ cv.to(kg.DEV) @ welle).contiguous()
    info = {"n_moden": n_moden, "amp": amp, "k_band": list(BAD_K), "saat": BAD_SAAT, "nc": nc,
            "omega_mittel": summe_om / n_moden, "S_mittel_soll": n_moden * amp * amp,
            "Q_soll": q_soll, "E_zu_Q_soll": float((om * om * band).sum().item()) / summe_om}
    return psi, vel, info


def einzel_dichten(g, psi, vel):
    nl1 = torch.ones((1, 1, 1), dtype=F64, device=kg.DEV)
    s, rho, e = kg.dichten(g, psi.unsqueeze(0), vel.unsqueeze(0), nl1)
    return s[0], rho[0], e[0]


def gebiete(g, s, rho):
    """Gebietszahl mit der Klassifikator-Maske S >= 2 S0 (periodische 4-Nachbar-Komponenten, Flaeche >= A_MIN), je
    Schwelle; 'verschmolzen' = genau ein Gebiet, rund (rmax/R_A <= KOMPAKT_FAMILIE), Schwerpunkt <= VERSCHMOLZEN_MITTE
    von (0, 0)."""
    aus = {}
    for S0 in (S0_HAUPT, S0_ZUSATZ):
        etik, K, _ = kg.komponenten(s >= kg.FAKTOREN[0] * S0)
        liste = []
        if K > 0:
            ei = kg.eigenschaften(g, etik, K, s, rho)
            fl, ra, xs, ys = ei["flaeche"].tolist(), ei["ra"].tolist(), ei["x"].tolist(), ei["y"].tolist()
            rm, qm, sm = ei["rmax"].tolist(), ei["q_maske"].tolist(), ei["smax"].tolist()
            for k in range(K):
                if fl[k] >= kg.A_MIN:
                    liste.append({"A": z7(fl[k]), "ra": z7(ra[k]), "x": z7(xs[k]), "y": z7(ys[k]),
                                  "rmax_zu_ra": z7(rm[k] / ra[k]), "Q_maske": z7(qm[k]), "S_max": z7(sm[k])})
        liste.sort(key=lambda d: -d["A"])
        n = len(liste)
        eins = liste[0] if n == 1 else None
        versch = bool(eins is not None and eins["rmax_zu_ra"] <= kg.KOMPAKT_FAMILIE
                      and math.hypot(eins["x"], eins["y"]) <= VERSCHMOLZEN_MITTE)
        aus[f"{S0:g}"] = {"n": n, "verschmolzen": versch, "gebiete": liste[:GEBIET_LISTE_MAX]}
    return aus


def familienpunkt(w2, knoten):
    kn = knoten[round(w2, 6)]
    prof = ke.profil(w2)
    rdef = b1.radius_definitionen(prof)
    rel = {k: v / kn["r_ladung"] - 1.0 for k, v in rdef.items() if v is not None}
    beste = min(rel, key=lambda k: abs(rel[k]))
    wahl = beste if abs(rel[beste]) <= b1.R_TOL_DEF else "rms"
    w0 = math.sqrt(w2)
    s = 1.0 * kn["r_ladung"] / b1.GAUSS_FAKTOR[wahl]            # Klumpen (i): Faktor 1 wie BILDUNG-1
    A = math.sqrt(kn["Q"] / (2.0 * w0 * math.pi * s * s))
    info = {"w2": w2, "Q_F": kn["Q"], "E_F": kn["E"], "R_F": kn["r_ladung"], "f_max": kn["f_max"], "w0": w0,
            "radius_kandidaten": rdef, "radius_rel": rel, "radius_wahl": wahl, "s": s, "A": A, "S_max_klumpen": A * A,
            "f0_profil": prof["f0"], "Q_rad": prof["Q_rad"], "E_rad": prof["E_rad"]}
    return prof, info


# ---------------------------------------------------------------- lauf

def befehl_lauf(args):
    start = ke.jetzt()
    t_start = kg.uhr()
    fam = kg.Familie()
    knoten = ke.familien_knoten()
    namen = GRUPPEN[args.gruppe]
    boxen = sorted({FAELLE[nm]["box"] for nm in namen})
    if len(boxen) != 1:
        raise SystemExit("Gruppe mit verschiedenen Boxen")
    box = boxen[0]
    dx, dt = kg.STUFEN[args.stufe]
    g = kg.Gitter(box, dx)
    B = len(namen)
    rauch = args.rauch
    t_fen_liste = b1.RAUCH_T_FEN if rauch else T_FEN
    fenster = b1.RAUCH_FENSTER if rauch else kg.FENSTER
    t_max = b1.RAUCH_T_ENDE if rauch else T_ENDE
    von, bis = float(args.von), float(args.bis)
    if not (0.0 <= von < bis <= t_max):
        raise SystemExit(f"Abschnitt {von} -> {bis} ausserhalb 0 .. {t_max}")
    for T in t_fen_liste:
        if (T - fenster < von < T) or (T - fenster < bis < T):
            raise SystemExit(f"Abschnittsgrenze schneidet das Fenster [{T - fenster}, {T}]")
    name = f"{args.stufe}_{args.gruppe}_{int(von)}-{int(bis)}" + ("_rauch" if rauch else "")
    basis = os.path.join(HIER, "lauf-69", "rauch" if rauch else "ausgabe")
    zw = os.path.join(HIER, "lauf-69", "rauch-zwischen" if rauch else "zwischen")
    os.makedirs(basis, exist_ok=True)
    os.makedirs(zw, exist_ok=True)
    pfad_json = ke.frei_pfad(os.path.join(basis, name + "_ergebnis.json"))
    print(f"BILDUNG-2 lauf {name}: Start {start} auf {kg.geraet_name()}, Box {box:g}, n {g.n}, B {B}, Faelle "
          f"{','.join(namen)}", flush=True)
    tp0 = kg.uhr()
    profile, punkte = {}, {}
    for w2 in sorted({FAELLE[nm]["w2"] for nm in namen}):
        profile[w2], punkte[w2] = familienpunkt(w2, knoten)
        p = punkte[w2]
        print(f"  omega^2 {w2:g}: Q_F {p['Q_F']:.6f}, E_F {p['E_F']:.6f}, R_F {p['R_F']:.6f}; Profil rms "
              f"{p['radius_kandidaten']['rms']:.6f}, mittel {p['radius_kandidaten']['mittel']:.6f}, halb "
              f"{p['radius_kandidaten']['halb']:.6f}; Wahl {p['radius_wahl']} (rel {p['radius_rel'][p['radius_wahl']]:+.2e})"
              f"; Klumpen (i) s {p['s']:.6f}, A {p['A']:.6f}, S_max {p['S_max_klumpen']:.5f}", flush=True)
    dauer = {"profil": kg.uhr() - tp0}
    rr = torch.sqrt(g.X ** 2 + g.Y ** 2)
    kpr, k_ok, bad_info = {}, True, None
    if von == 0.0:
        felder = []
        for nm in namen:
            f = FAELLE[nm]
            p = punkte[f["w2"]]
            teile = []
            if f["art"] in ("klumpen", "klumpen+bad"):
                teile.append(("klumpen", (0.0, 0.0), b1.klumpen_feld(g, p["A"], p["s"], p["w0"])))
            elif f["art"] in ("ball", "ball+bad"):
                teile.append(("ball", (0.0, 0.0), ke.ball_feld(g, profile[f["w2"]], {"w2": f["w2"], "v": 0.0,
                                                                                       "amp": 1.0})))
            elif f["art"] == "zwei_klumpen":
                d = C_ABSTAND_R * p["R_F"]
                for x0 in (-0.5 * d, 0.5 * d):
                    gs = types.SimpleNamespace(X=g.X - x0, Y=g.Y)
                    teile.append(("klumpen", (x0, 0.0), b1.klumpen_feld(gs, p["A"], p["s"], p["w0"])))
            if "bad" in f["art"]:
                bp, bv, bad_info = bad_felder(g, BAD_ANTEIL * p["Q_F"])
                teile.append(("bad", None, (bp, bv)))
            k = {"teile": []}
            ok = True
            for art, mitte, (tp, tv) in teile:
                s1, rho1, e1 = einzel_dichten(g, tp, tv)
                q1 = (rho1.sum() * g.dA).item()
                e_1 = (e1.sum() * g.dA).item()
                z = {"art": art, "mitte": mitte, "Q": q1, "E": e_1, "E_zu_Q": e_1 / q1, "S_max": s1.max().item()}
                if art == "klumpen":
                    r2 = (g.X - mitte[0]) ** 2 + (g.Y - mitte[1]) ** 2
                    r_rms = math.sqrt(((rho1 * r2).sum() / rho1.sum()).item())
                    z.update({"Q_soll": p["Q_F"], "dQ_rel": q1 / p["Q_F"] - 1.0, "s": p["s"], "r_rms_gitter": r_rms,
                              "r_rms_zu_s_rel": r_rms / p["s"] - 1.0})
                    z["bestanden"] = abs(z["dQ_rel"]) <= b1.K_TOL and abs(z["r_rms_zu_s_rel"]) <= b1.K_TOL
                elif art == "ball":
                    omr, res = ke.omega_gitter(g, profile[f["w2"]])
                    r_rms = math.sqrt(((rho1 * rr * rr).sum() / rho1.sum()).item())
                    z.update({"Q_soll": p["Q_F"], "E_soll": p["E_F"], "dQ_rel": q1 / p["Q_F"] - 1.0,
                              "dE_rel": e_1 / p["E_F"] - 1.0, "omega_gitter": omr, "domega_rel": omr / p["w0"] - 1.0,
                              "residuum_gitter": res, "r_rms_gitter": r_rms, "r_rms_zu_R_F_rel": r_rms / p["R_F"] - 1.0})
                    z["bestanden"] = all(abs(z[x]) <= b1.K_TOL for x in ("dQ_rel", "dE_rel", "domega_rel"))
                else:
                    z.update({"Q_soll": bad_info["Q_soll"], "dQ_rel": q1 / bad_info["Q_soll"] - 1.0,
                              "S_mittel": s1.mean().item(), "S_mittel_soll": bad_info["S_mittel_soll"],
                              "E_zu_Q_soll": bad_info["E_zu_Q_soll"]})
                    z["bestanden"] = abs(z["dQ_rel"]) <= b1.K_TOL
                ok = ok and z["bestanden"]
                k["teile"].append(z)
            psi_b = sum(t[2][0] for t in teile)
            vel_b = sum(t[2][1] for t in teile)
            s1, rho1, e1 = einzel_dichten(g, psi_b, vel_b)
            k["Q_summe"] = (rho1.sum() * g.dA).item()
            k["E_summe"] = (e1.sum() * g.dA).item()
            k["Q_teile"] = sum(z["Q"] for z in k["teile"])
            k["Q_kreuz_rel"] = k["Q_summe"] / k["Q_teile"] - 1.0
            k["S_max_summe"] = s1.max().item()
            if f["art"] == "zwei_klumpen":
                d = C_ABSTAND_R * p["R_F"]
                soll = 2.0 * p["Q_F"] * (1.0 + math.exp(-d * d / (4.0 * p["s"] * p["s"])))
                k.update({"Q_summe_soll_analytisch": soll, "dQ_summe_rel": k["Q_summe"] / soll - 1.0,
                          "S_mitte_analytisch": (2.0 * p["A"] * math.exp(-d * d / (8.0 * p["s"] * p["s"]))) ** 2,
                          "S_mitte_gitter": s1[g.n // 2, g.n // 2].item(), "x_mitte_gitter": g.x1[g.n // 2].item()})
                ok = ok and abs(k["dQ_summe_rel"]) <= b1.K_TOL
            k["bestanden"] = ok
            k_ok = k_ok and ok
            kpr[nm] = k
            felder.append((psi_b, vel_b))
            print(f"  K {nm}: " + "; ".join(
                f"{z['art']} Q {z['Q']:.6f} (rel {z['dQ_rel']:+.2e}) E/Q {z['E_zu_Q']:.5f} S_max {z['S_max']:.5f}"
                + (f" r_rms {z['r_rms_gitter']:.6f} (rel {z.get('r_rms_zu_s_rel', z.get('r_rms_zu_R_F_rel')):+.2e})"
                   if "r_rms_gitter" in z else "")
                + (f" omega_gitter rel {z['domega_rel']:+.2e}, E rel {z['dE_rel']:+.2e}" if z["art"] == "ball" else "")
                for z in k["teile"]) + f" | Summe Q {k['Q_summe']:.6f} (Kreuz {k['Q_kreuz_rel']:+.2e}), E "
                f"{k['E_summe']:.6f}, S_max {k['S_max_summe']:.5f}"
                + (f", Q analytisch {k['Q_summe_soll_analytisch']:.6f} (rel {k['dQ_summe_rel']:+.2e}), S Mitte "
                   f"{k['S_mitte_gitter']:.5f} (analytisch {k['S_mitte_analytisch']:.5f}, x {k['x_mitte_gitter']:g})"
                   if f["art"] == "zwei_klumpen" else "")
                + f" -> {'bestanden' if ok else 'NICHT bestanden'}", flush=True)
        psi = torch.stack([f[0] for f in felder]).contiguous()
        vel = torch.stack([f[1] for f in felder]).contiguous()
        del felder
        Q0 = E0 = None
        quelle = "Anfangszustand"
    else:
        zp = os.path.join(zw, f"{args.stufe}_{args.gruppe}_t{int(von)}.pt")
        ck = torch.load(zp, map_location="cpu")
        if ck["faelle"] != namen or ck["stufe"] != args.stufe or abs(ck["t"] - von) > 1e-9:
            raise SystemExit(f"Zwischenspeicher {zp} passt nicht")
        psi = ck["psi"].to(kg.DEV).contiguous()
        vel = ck["vel"].to(kg.DEV).contiguous()
        Q0, E0 = ck["Q0"], ck["E0"]
        quelle = {"datei": zp, "sha256": ke.sha(zp)}
        del ck
    nl = torch.ones((B, 1, 1), dtype=F64, device=kg.DEV)
    kraft = kg.kraft_fn(g, nl)
    ringe = b1.RINGE if box == b1.BOX else RINGE_A
    ringmasken = {R: (rr <= R).to(F64) for R in ringe}
    r_ball = R_BALLRING[box]
    ballring = (rr <= r_ball).to(F64)
    maxnorm = torch.maximum(g.X.abs(), g.Y.abs())
    m, rahmen, innen = absorber_box(g, dt)
    abs_gleich = None
    if box == b1.BOX:
        m1, r1 = b1.absorber(g, dt)
        abs_gleich = bool(torch.equal(m, m1) and torch.equal(rahmen, r1) and innen == b1.INNEN)
        if not abs_gleich:
            raise SystemExit("Absorber Box 96 nicht bitgleich mit bildung1.absorber")
        del m1, r1
    s, rho, e = kg.dichten(g, psi, vel, nl)
    if von == 0.0:
        Q0 = (rho.sum((1, 2)) * g.dA).tolist()
        E0 = (e.sum((1, 2)) * g.dA).tolist()
    meta = {"karte": "BILDUNG-2 (R22)", "name": name, "start": start, "rauch": rauch, "fertig": False,
            "stufe": args.stufe, "gruppe": args.gruppe, "faelle": namen, "von": von, "bis": bis, "dx": dx, "dt": dt,
            "n": g.n, "box": g.box, "innen": innen, "absorber_bitgleich_bildung1": abs_gleich,
            "absorber": {"breite": b1.ABS_BREITE, "sigma_max": b1.ABS_SIGMA, "innen": innen,
                         "form": "sigma_max * xi^2, xi = (max(|x|,|y|) - innen)/breite"},
            "t_fenster": [T for T in t_fen_liste if von <= T - fenster and T <= bis], "fenster": fenster,
            "herkunft": ke.herkunft(), "bildung1_sha256": ke.sha(os.path.join(R22B1, "bildung1.py")),
            "bildung2_sha256": ke.sha(os.path.abspath(__file__)), "quelle": quelle,
            "punkte": {f"{w2:g}": p for w2, p in punkte.items()}, "bad": bad_info,
            "parameter": {"BAD_ANTEIL": BAD_ANTEIL, "BAD_K": list(BAD_K), "BAD_SAAT": BAD_SAAT,
                          "C_ABSTAND_R": C_ABSTAND_R, "DICHT_DT": DICHT_DT, "DICHT_BIS": DICHT_BIS,
                          "VERSCHMOLZEN_MITTE": VERSCHMOLZEN_MITTE, "ringe": list(ringe), "r_ballring": r_ball},
            "Q0": Q0, "E0": E0, "k_pruefung": kpr, "k_bestanden": k_ok}
    if not k_ok:
        meta["ende"] = ke.jetzt()
        meta["abbruch"] = "K-Pruefung nicht bestanden: keine Zeitentwicklung (PLAN.md)"
        ke.schreibe_json(pfad_json, meta)
        raise SystemExit(meta["abbruch"])
    # Zeitentwicklung
    n_fen = int(round(fenster / dt))
    je_fen = int(round(kg.DT_FENSTER / dt))
    je_diag = int(round(b1.T_DIAG / dt))
    je_dicht = int(round(DICHT_DT / dt))
    n_dicht_bis = int(round(DICHT_BIS / dt))
    n_von, n_bis = int(round(von / dt)), int(round(bis / dt))
    fen_start = {int(round((T - fenster) / dt)): T for T in meta["t_fenster"]}
    fen_ende = {int(round(T / dt)): T for T in meta["t_fenster"]}
    S0s = (S0_HAUPT, S0_ZUSATZ)
    aktiv, ergebnisse, diag, geb_reihe = {}, [], [], []
    dauer.update({"analyse": 0.0, "fenster": 0.0, "diag": 0.0, "gebiete": 0.0})
    n_proben = 0
    t_vor = kg.uhr()
    F = kraft(psi)
    for schritt in range(n_von, n_bis + 1):
        if schritt > n_von:
            vel.add_(F, alpha=0.5 * dt)
            psi.add_(vel, alpha=dt)
            psi.mul_(m)
            F = kraft(psi)
            vel.add_(F, alpha=0.5 * dt)
            vel.mul_(m)
        if schritt == n_von + 400 and not rauch:
            verg = kg.uhr() - t_vor
            rate = (verg - dauer["analyse"] - dauer["fenster"] - dauer["diag"] - dauer["gebiete"]) / 400.0
            prognose = (kg.uhr() - t_start) + 1.10 * rate * (n_bis - schritt) + 4.0 * len(fen_start)
            print(f"  Prognose Gesamtdauer {prognose:.0f} s ({rate * 1e3:.2f} ms je Schritt)", flush=True)
            if prognose > b1.ZEITGRENZE_S:
                meta["ende"] = ke.jetzt()
                meta["abbruch"] = f"Prognose {prognose:.0f} s ueber {b1.ZEITGRENZE_S:.0f} s"
                ke.schreibe_json(pfad_json, meta)
                raise SystemExit(meta["abbruch"] + ": Abschnitt teilen")
        d_jetzt = schritt % je_diag == 0
        g_jetzt = d_jetzt or (schritt % je_dicht == 0 and schritt <= n_dicht_bis)
        neu = schritt in fen_start
        probe = neu or any(schritt >= a["start"] and (schritt - a["start"]) % je_fen == 0 for a in aktiv.values())
        if not (d_jetzt or g_jetzt or probe):
            continue
        s, rho, e = kg.dichten(g, psi, vel, nl)
        t_jetzt = round(schritt * dt, 6)
        if d_jetzt:
            td = kg.uhr()
            diag.append(b1.diag_zeile(g, s, rho, e, ringmasken, rahmen, maxnorm, t_jetzt))
            dauer["diag"] += kg.uhr() - td
        if g_jetzt:
            tg = kg.uhr()
            geb_reihe.append({"t": t_jetzt, "faelle": [gebiete(g, s[b], rho[b]) for b in range(B)]})
            dauer["gebiete"] += kg.uhr() - tg
        if not probe:
            continue
        if neu:
            ta = kg.uhr()
            T = fen_start[schritt]
            a = {"start": schritt, "fzs": {}, "zeilen": {}, "s_max": s.amax((1, 2)).tolist(),
                 "q_box": (rho.sum((1, 2)) * g.dA).tolist(), "q_ring": ((rho * ballring).sum((1, 2)) * g.dA).tolist()}
            for b in range(B):
                for S0 in S0s:
                    zeile, _, tropfen = kg.analyse_arm(g, s[b], rho[b], e[b], psi[b], S0, fam, None)
                    a["fzs"][(b, S0)] = kg.fenster_start(tropfen)
                    a["zeilen"][(b, S0)] = zeile
            aktiv[T] = a
            dauer["analyse"] += kg.uhr() - ta
        tf_ = kg.uhr()
        for a in aktiv.values():
            if schritt >= a["start"] and (schritt - a["start"]) % je_fen == 0:
                for (b, S0), fz in a["fzs"].items():
                    if fz is not None:
                        kg.fenster_probe(g, fz, s[b], rho[b], e[b], psi[b])
                        n_proben += 1
        dauer["fenster"] += kg.uhr() - tf_
        if schritt in fen_ende:
            T = fen_ende[schritt]
            a = aktiv.pop(T)
            t0 = round(T - fenster, 6)
            for b, nm in enumerate(namen):
                q_F = punkte[FAELLE[nm]["w2"]]["Q_F"]
                for S0 in S0s:
                    fen = kg.fenster_auswerten(a["fzs"][(b, S0)], t0, kg.DT_FENSTER, fam, g.box)
                    zeile = a["zeilen"][(b, S0)]
                    ztr = zeile.get("tropfen", {})
                    beste_tr, dbest = None, None
                    alle = []
                    for tr in fen["tropfen"]:
                        alle.append({x: tr.get(x) for x in ("x0", "y0", "klasse", "rund", "Q_net", "omega_ruhe",
                                                             "u_omega", "E_zu_Q", "Q_schwankung", "stoss", "verloren")})
                        if tr["x0"] is None or tr["y0"] is None:
                            continue
                        d = math.hypot(tr["x0"], tr["y0"])
                        if d <= b1.BALL_SUCH and (dbest is None or d < dbest):
                            beste_tr, dbest = tr, d
                    z2 = zeile["schwellen"]["2"]
                    eintrag = {"fall": nm, "S0": S0, "T": T, "fenster": [t0, T], "N_fenstertropfen": len(fen["tropfen"]),
                               "zaehlung": fen["zaehlung"], "tropfen_alle": alle, "N_komp_2S0": z2["N_komp"],
                               "N_tropfen_2S0": z2["N_tropfen"], "S_max_box_start": z7(a["s_max"][b]), "Q0": Q0[b],
                               "Q_F": q_F, "Q_box_anteil_start": z7(a["q_box"][b] / Q0[b]),
                               "Q_ring_F_start": z7(a["q_ring"][b] / q_F), "r_ballring": r_ball}
                    if beste_tr is None:
                        eintrag.update({"klasse": "kein Tropfen", "rund": None, "Q_net": None, "Q_anteil": None,
                                        "Q_anteil_F": None})
                    else:
                        k = beste_tr["k"]
                        eintrag.update({x: beste_tr.get(x) for x in (
                            "klasse", "klasse_roh", "rund", "Q_net", "Q_roh", "E_ruhe_net", "E_zu_Q", "E_zu_Q_familie",
                            "omega_rot", "omega_ruhe", "u_omega", "omega_inst_mittel", "omega_geo",
                            "omega_familie_bei_Q", "v", "S_max_mittel", "Q_schwankung", "verloren", "stoss", "dQ",
                            "dQ_band", "x0", "y0")})
                        eintrag["v_mess"] = eintrag.pop("v")
                        eintrag["abstand_mitte"] = z7(dbest)
                        eintrag["rmax_zu_ra"] = (ztr.get("rmax_zu_ra") or [None] * (k + 1))[k]
                        eintrag["A_maske"] = (ztr.get("A") or [None] * (k + 1))[k]
                        eintrag["S_max_start"] = (ztr.get("S_max") or [None] * (k + 1))[k]
                        eintrag.update(ke.familien_abstaende(fam, beste_tr))
                        q = beste_tr.get("Q_net")
                        eintrag["Q_anteil"] = z7(q / Q0[b]) if q is not None else None
                        eintrag["Q_anteil_F"] = z7(q / q_F) if q is not None else None
                    ergebnisse.append(eintrag)
    dauer["vorwaerts_gesamt"] = kg.uhr() - t_vor
    if bis < t_max:
        zp = ke.frei_pfad(os.path.join(zw, f"{args.stufe}_{args.gruppe}_t{int(bis)}.pt"))
        torch.save({"t": bis, "faelle": namen, "stufe": args.stufe, "psi": psi.cpu(), "vel": vel.cpu(), "Q0": Q0,
                    "E0": E0}, zp + ".tmp")
        os.replace(zp + ".tmp", zp)
        meta["zwischenspeicher"] = {"datei": zp, "sha256": ke.sha(zp)}
    dauer["gesamt"] = kg.uhr() - t_start
    n_schritte = n_bis - n_von
    ent = dauer["vorwaerts_gesamt"] - dauer["analyse"] - dauer["fenster"] - dauer["diag"] - dauer["gebiete"]
    meta.update({"ende": ke.jetzt(), "fertig": True, "dauer_s": dauer, "schritte": n_schritte,
                 "ms_je_schritt": ent / max(1, n_schritte) * 1e3, "n_proben": n_proben,
                 "gpu_speicher_mb": (torch.cuda.max_memory_allocated() / 2 ** 20) if kg.DEV.type == "cuda" else None,
                 "diag": diag, "gebiete": geb_reihe})
    if rauch:
        meta["n_eintraege"] = len(ergebnisse)
        meta["prognose_25000_schritte_s"] = ent / max(1, n_schritte) * 25000
        ke.schreibe_json(pfad_json, meta)
        print(f"RAUCH {name}: Durchlauf ok; Dauer [s] " + ", ".join(f"{x} {y:.1f}" for x, y in dauer.items())
              + f"; {meta['ms_je_schritt']:.2f} ms je Schritt (B {B}); 25000 Schritte ~ "
              f"{meta['prognose_25000_schritte_s']:.0f} s; GPU max {kg.fz(meta['gpu_speicher_mb'], '.0f')} MB; "
              f"Fenstereintraege {len(ergebnisse)}, Gebietsproben {len(geb_reihe)} (nicht ausgegeben)", flush=True)
        for z in diag:
            print(f"  diag t {z['t']:g}: " + " | ".join(
                f"{nm}: Qbox {z['Q_box'][b] / Q0[b]:.6f} rahmen {z['Q_rahmen'][b] / Q0[b]:.2e}"
                + (f" r32 {z['Q_r32'][b] / Q0[b]:.4f} aus1e-4 {z['ausdehnung_0.0001'][b]:g}" if nm == "BAD" else "")
                for b, nm in enumerate(namen)), flush=True)
        return
    meta["ergebnisse"] = ergebnisse
    ke.schreibe_json(pfad_json, meta)
    L = [f"BILDUNG-2 {name}: Ende {meta['ende']}, Dauer [s] " + ", ".join(f"{x} {y:.1f}" for x, y in dauer.items())
         + f", {meta['ms_je_schritt']:.2f} ms je Schritt"]
    for x in ergebnisse:
        L.append(zeilentext(x))
    with open(ke.frei_pfad(os.path.join(basis, name + "_bericht.txt")), "w") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L), flush=True)


def zeilentext(x):
    return (f"  {x.get('stufe', '')} {x['fall']} S0 {x['S0']} T {x['T']:g}: {x['klasse']} | N_Tropfen "
            f"{x['N_fenstertropfen']} | rund {x.get('rund')} rmax/ra {kg.fz(x.get('rmax_zu_ra'), '.3f')} | Q/Q_F "
            f"{kg.fz(x.get('Q_anteil_F'), '.4f')} (Q/Q0 {kg.fz(x.get('Q_anteil'), '.4f')}, Ring/Q_F "
            f"{kg.fz(x.get('Q_ring_F_start'), '.4f')}) | omega {kg.fz(x.get('omega_ruhe'), '.5f')} +- "
            f"{kg.fz(x.get('u_omega'), '.1e')} (fam(Q) {kg.fz(x.get('omega_familie_bei_Q'), '.5f')}) | E/Q "
            f"{kg.fz(x.get('E_zu_Q'), '.4f')} (fam {kg.fz(x.get('E_zu_Q_familie'), '.4f')}) | dQ* "
            f"{kg.fz(x.get('dQ_stern'), '+.4f')} | E/Q-Abst {kg.fz(x.get('EQ_abstand'), '+.4f')} | omega-Abst "
            f"{kg.fz(x.get('omega_abstand'), '+.5f')} | Q-Schw {kg.fz(x.get('Q_schwankung'), '.3f')} | v "
            f"{kg.fz(x.get('v_mess'), '.4f')} | Ort ({kg.fz(x.get('x0'), '.2f')}, {kg.fz(x.get('y0'), '.2f')})")


# ---------------------------------------------------------------- zusammen (C0 bis C4, Box, Regeln PLAN.md)

def befehl_zusammen(args):
    out = os.path.join(HIER, "lauf-69", "ausgabe")
    eintraege, kpr, dateien, diag, q0, geb, innen_von = [], {}, [], {}, {}, {}, {}
    for p in sorted(glob.glob(os.path.join(out, "*_ergebnis.json"))):
        with open(p) as fh:
            d = json.load(fh)
        if d.get("rauch") or not d.get("fertig"):
            continue
        dateien.append({"datei": os.path.basename(p), "sha256": ke.sha(p), "stufe": d["stufe"], "gruppe": d["gruppe"],
                        "von": d["von"], "bis": d["bis"], "bildung2_sha256": d["bildung2_sha256"]})
        for x in d["ergebnisse"]:
            x["stufe"] = d["stufe"]
            eintraege.append(x)
        for nm, k in (d.get("k_pruefung") or {}).items():
            kpr[f"{d['stufe']}/{nm}"] = k
        for b, nm in enumerate(d["faelle"]):
            q0[(d["stufe"], nm)] = d["Q0"][b]
            innen_von[(d["stufe"], nm)] = d["innen"]
            dd = diag.setdefault((d["stufe"], nm), {})
            for z in d["diag"]:
                dd[z["t"]] = {x: (v[b] if isinstance(v, list) else v) for x, v in z.items()}
            gg = geb.setdefault((d["stufe"], nm), {})
            for z in d["gebiete"]:
                gg[z["t"]] = z["faelle"][b]

    def such(stufe, fall, T, S0=S0_HAUPT):
        return [x for x in eintraege if x["stufe"] == stufe and x["fall"] == fall and abs(x["T"] - T) < 1e-9
                and abs(x["S0"] - S0) < 1e-12]

    def auf(x):
        return x["klasse"] == "auf" and bool(x["rund"])

    erg = {"zeit": ke.jetzt(), "dateien": dateien, "k_pruefung": kpr}
    box = {}
    for (st, nm), dd in sorted(diag.items()):
        ts = sorted(dd)
        aus06 = max(dd[t]["ausdehnung_0.6"] for t in ts)
        qb = [dd[t]["Q_box"] / q0[(st, nm)] for t in ts]
        grenze = innen_von[(st, nm)] - b1.MASKE_ABSTAND
        box[f"{st}/{nm}"] = {"t_von_bis": [ts[0], ts[-1]], "n_diag": len(ts), "ausdehnung_0.6_max": aus06,
                             "grenze": grenze, "bestanden": (ts[-1] >= T_ENDE - 1e-9) and aus06 <= grenze,
                             "Q_box_anteil_ende": qb[-1], "Q_rahmen_anteil_max": max(dd[t]["Q_rahmen"] / q0[(st, nm)]
                                                                                     for t in ts),
                             "ausdehnung_0.2_max": max(dd[t]["ausdehnung_0.2"] for t in ts),
                             "reihe": {f"{t:g}": {x: dd[t][x] for x in dd[t] if x.startswith("Q_") or x == "S_max"}
                                       for t in ts if t in (0.0, 50.0, 100.0, 200.0, 250.0, 500.0, 750.0, 1000.0)}}
    erg["box"] = box
    box_ok = {k: v["bestanden"] for k, v in box.items()}
    z = {}
    # C0: B0 zu allen sechs Fensterenden, beide Gitter
    sel = [x for st in ("grob", "fein") for T in T_FEN for x in such(st, "B0", T)]
    if len(sel) < 2 * len(T_FEN):
        z["C0"] = f"offen (unvollstaendig: {len(sel)} von {2 * len(T_FEN)})"
    elif not all(box_ok.get(f"{st}/B0", False) for st in ("grob", "fein")):
        z["C0"] = "offen (Box-Pruefung nicht bestanden)"
    else:
        n = sum(1 for x in sel if auf(x))
        z["C0"] = "eingetroffen" if n == len(sel) else "nicht eingetroffen"
        z["C0_zahl"] = f"{n} von {len(sel)} 'auf' (und rund)"
    # C1: A bei T = 500, beide Gitter
    sel = [x for st in ("grob", "fein") for x in such(st, "A", 500.0)]
    if len(sel) < 2:
        z["C1"] = f"offen (unvollstaendig: {len(sel)} von 2)"
    elif not all(box_ok.get(f"{st}/A", False) for st in ("grob", "fein")):
        z["C1"] = "offen (Box-Pruefung nicht bestanden)"
    else:
        n = sum(1 for x in sel if auf(x))
        z["C1"] = "eingetroffen" if n == 2 else "nicht eingetroffen"
        z["C1_zahl"] = f"{n} von 2 'auf' und rund"
    # C2: B bei T = 500, beide Gitter; nur wertbar bei C0 eingetroffen
    sel = [x for st in ("grob", "fein") for x in such(st, "B", 500.0)]
    if len(sel) < 2:
        z["C2"] = f"offen (unvollstaendig: {len(sel)} von 2)"
    elif not all(box_ok.get(f"{st}/B", False) for st in ("grob", "fein")):
        z["C2"] = "offen (Box-Pruefung nicht bestanden)"
    else:
        n = sum(1 for x in sel if auf(x))
        roh = "eingetroffen" if n == 2 else "nicht eingetroffen"
        z["C2_zahl"] = f"{n} von 2 'auf' und rund"
        z["C2_roh"] = roh
        z["C2"] = roh if z["C0"] == "eingetroffen" else f"offen (C0 {z['C0']}; ohne C0: {roh})"
    # C3, C4: je Gitter
    c3, c4, cdet = {}, {}, {}
    for st in ("grob", "fein"):
        reihe = geb.get((st, "C"), {})
        ts = sorted(reihe)
        det = {"n_proben": len(ts)}
        if not ts or ts[-1] < T_ENDE - 1e-9:
            det["fehlt"] = True
            cdet[st] = det
            continue
        vs = [(t, reihe[t][f"{S0_HAUPT:g}"]["verschmolzen"]) for t in ts]
        t_m = None
        for i in range(len(vs)):
            if all(v for _, v in vs[i:]):
                t_m = vs[i][0]
                break
        det["t_verschmolzen_dauerhaft"] = t_m
        det["t_erst_n1"] = next((t for t in ts if reihe[t][f"{S0_HAUPT:g}"]["n"] == 1), None)
        det["t_erst_n2"] = next((t for t in ts if reihe[t][f"{S0_HAUPT:g}"]["n"] >= 2), None)
        det["t_erst_verschmolzen"] = next((t for t, v in vs if v), None)
        det["n_wechsel"] = [[t, reihe[t][f"{S0_HAUPT:g}"]["n"], reihe[t][f"{S0_ZUSATZ:g}"]["n"]]
                            for i, t in enumerate(ts)
                            if i == 0 or reihe[t][f"{S0_HAUPT:g}"]["n"] != reihe[ts[i - 1]][f"{S0_HAUPT:g}"]["n"]]
        einzeln = []
        for T in T_FEN:
            for x in such(st, "C", T):
                if x["N_fenstertropfen"] >= 2 and any(tr["klasse"] == "auf" and tr["rund"] for tr in x["tropfen_alle"]):
                    if t_m is None or (T - kg.FENSTER) < t_m:
                        einzeln.append(T)
        det["einzeln_auf_fenster_vor_t_m"] = einzeln
        c3[st] = (t_m is not None) and not einzeln
        x1000 = such(st, "C", 1000.0)
        det["T1000"] = ({"klasse": x1000[0]["klasse"], "rund": x1000[0]["rund"], "N": x1000[0]["N_fenstertropfen"]}
                        if x1000 else None)
        if t_m is not None and x1000:
            c4[st] = auf(x1000[0])
        elif t_m is None:
            c4[st] = None
        cdet[st] = det
    erg["C_details"] = cdet
    box_c = all(box_ok.get(f"{st}/C", False) for st in ("grob", "fein"))
    if len(c3) < 2:
        z["C3"] = "offen (unvollstaendig)"
    elif not box_c:
        z["C3"] = "offen (Box-Pruefung nicht bestanden)"
    elif c3["grob"] and c3["fein"]:
        z["C3"] = "eingetroffen"
    elif not c3["grob"] and not c3["fein"]:
        z["C3"] = "nicht eingetroffen"
    else:
        z["C3"] = f"offen (Gitter uneinig: grob {c3['grob']}, fein {c3['fein']})"
    if len(cdet) < 2 or any(cdet[st].get("fehlt") for st in ("grob", "fein")):
        z["C4"] = "offen (unvollstaendig)"
    elif not box_c:
        z["C4"] = "offen (Box-Pruefung nicht bestanden)"
    elif any(c4.get(st) is None for st in ("grob", "fein")):
        z["C4"] = ("offen (kein dauerhaftes Verschmelzen bis T = 1000 auf "
                   + ", ".join(st for st in ("grob", "fein") if c4.get(st) is None) + ")")
    elif c4["grob"] and c4["fein"]:
        z["C4"] = "eingetroffen"
    elif not c4["grob"] and not c4["fein"]:
        z["C4"] = "nicht eingetroffen"
    else:
        z["C4"] = f"offen (Gitter uneinig: grob {c4['grob']}, fein {c4['fein']})"
    # Bedeutung (Karte, mechanisch)
    bed = []
    if z["C0"] == "nicht eingetroffen":
        bed.append("C0 nicht eingetroffen: Der Klassifikator taugt im Bad nicht; Arm B bleibt offen (Karte)")
    if z["C1"] == "nicht eingetroffen":
        bed.append("C1 nicht eingetroffen: Grosse, duennwandige Klumpen erreichen die Familie langsamer oder gar nicht "
                   "(Karte)")
    if z["C2"] == "nicht eingetroffen":
        bed.append("C2 nicht eingetroffen (bei C0): Das Wellenbad hindert die Bildung (Karte)")
    if z["C1"] == "eingetroffen" and z["C2"] == "eingetroffen" and z["C4"] == "nicht eingetroffen":
        bed.append("C1 und C2 eingetroffen, C4 nicht: Groesse und Bad hindern die Bildung nicht; das 'nie auf' in KF-5 "
                   "lag am Verschmelzen [H] (Karte)")
    if not bed:
        bed.append("Kombination ohne Bedeutung in der Karte: beschreibend, keine Deutung")
    z["bedeutung"] = bed
    # L3 grob gegen fein
    l3 = []
    for x in eintraege:
        if x["stufe"] != "grob":
            continue
        y = such("fein", x["fall"], x["T"], x["S0"])
        if y:
            y = y[0]
            l3.append({"fall": x["fall"], "T": x["T"], "S0": x["S0"], "klasse": [x["klasse"], y["klasse"]],
                       "gleich": x["klasse"] == y["klasse"],
                       "d_omega": (abs(x["omega_ruhe"] - y["omega_ruhe"])
                                   if (x.get("omega_ruhe") is not None and y.get("omega_ruhe") is not None) else None),
                       "d_Q_anteil_F": (abs(x["Q_anteil_F"] - y["Q_anteil_F"])
                                        if (x.get("Q_anteil_F") is not None and y.get("Q_anteil_F") is not None)
                                        else None)})
    erg["L3"] = {"paare": len(l3), "klasse_gleich": sum(1 for v in l3 if v["gleich"]), "einzeln": l3}
    erg["vorhersagen"] = z
    # Gebietsreihe (kurz) je Lauf
    erg["gebiete_kurz"] = {}
    for (st, nm), reihe in sorted(geb.items()):
        erg["gebiete_kurz"][f"{st}/{nm}"] = [[t, reihe[t][f"{S0_HAUPT:g}"]["n"], reihe[t][f"{S0_ZUSATZ:g}"]["n"],
                                             reihe[t][f"{S0_HAUPT:g}"]["verschmolzen"]] for t in sorted(reihe)]
    pfad = ke.frei_pfad(os.path.join(out, "zusammen.json"))
    ke.schreibe_json(pfad, erg)
    L = [f"BILDUNG-2 zusammen ({erg['zeit']}), {len(dateien)} Dateien"]
    for nr in ("C0", "C1", "C2", "C3", "C4"):
        L.append(f"  {nr}: {z[nr]}" + (f" ({z[nr + '_zahl']})" if nr + "_zahl" in z else ""))
    for st, det in cdet.items():
        L.append(f"  C-Details {st}: {json.dumps(det)}")
    for b_ in z["bedeutung"]:
        L.append(f"  Bedeutung: {b_}")
    for k, v in box.items():
        L.append(f"  Box {k}: {'bestanden' if v['bestanden'] else 'NICHT bestanden'}; Maske 0,6 max-Norm max "
                 f"{v['ausdehnung_0.6_max']:g} (Grenze {v['grenze']:g}), Maske 0,2 max {v['ausdehnung_0.2_max']:g}; "
                 f"Q_box Ende {v['Q_box_anteil_ende']:.6f}, Rahmen max {v['Q_rahmen_anteil_max']:.2e}")
    L.append(f"  L3: {erg['L3']['klasse_gleich']} von {erg['L3']['paare']} Paaren gleiche Klasse")
    for S0 in (S0_HAUPT, S0_ZUSATZ):
        L.append(f"== S0 {S0}")
        for nm in ("B0", "KA", "A", "B", "BAD", "C"):
            for T in T_FEN:
                for st in ("grob", "fein"):
                    for x in such(st, nm, T, S0):
                        L.append(zeilentext(x))
                        if nm == "C" and x["N_fenstertropfen"] >= 2:
                            L.append("      alle: " + json.dumps(x["tropfen_alle"]))
    for k, v in erg["gebiete_kurz"].items():
        if k.endswith("/C"):
            L.append(f"  Gebiete {k} [t, n(0,6), n(0,2), verschmolzen]: {json.dumps(v)}")
    with open(ke.frei_pfad(os.path.join(out, "zusammen.txt")), "w") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L), flush=True)


def main():
    ap = argparse.ArgumentParser(description="BILDUNG-2 (Runde 22, v3)")
    ap.add_argument("befehl", choices=["lauf", "zusammen"])
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda")
    ap.add_argument("--stufe", choices=list(kg.STUFEN), default="grob")
    ap.add_argument("--gruppe", choices=list(GRUPPEN), default="bc")
    ap.add_argument("--von", type=float, default=0.0)
    ap.add_argument("--bis", type=float, default=T_ENDE)
    ap.add_argument("--rauch", action="store_true")
    args = ap.parse_args()
    if args.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("--geraet cuda, aber kein CUDA-Geraet sichtbar: Abbruch (kein stiller CPU-Ausweg).")
        kg.DEV = torch.device("cuda")
    else:
        if args.befehl != "zusammen":
            raise SystemExit("Rechnungen nur auf der GPU (PLAN.md)")
        kg.DEV = torch.device("cpu")
        torch.set_num_threads(1)
    print(f"bildung2 {args.befehl}: Start {ke.jetzt()}", flush=True)
    {"lauf": befehl_lauf, "zusammen": befehl_zusammen}[args.befehl](args)
    print(f"bildung2 {args.befehl}: Ende {ke.jetzt()}", flush=True)


if __name__ == "__main__":
    main()
