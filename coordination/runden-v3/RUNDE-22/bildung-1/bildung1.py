#!/usr/bin/env python3
"""BILDUNG-1 (Runde 22, v3): Wird ein einzelner Gauss-Klumpen von selbst zum Q-Ball?

Karte: coordination/runden-v3/RUNDE-22/bildung-1/KARTE.md; Plan (vor dem ersten echten Lauf eingefroren): PLAN.md.
Importiert unveraendert (nur gelesen, ohne Bytecode):
  - kf5_geburt.py aus Runde 6 (/home/fmh/fmhc-physics-remote/runde6-kf5): Gitter, kraft_fn, dichten, analyse_arm,
    fenster_start, fenster_probe, fenster_auswerten (darin familien_klasse), Familie, Konstanten (STUFEN, BOX0,
    FENSTER, DT_FENSTER, Schwellen, FAM_TOL).
  - kf_eich.py aus Runde 21 (/home/fmh/fmhc-physics-remote/runde21-kf-eich): profil, ball_feld, omega_gitter,
    familien_abstaende, familien_knoten, Hilfen (exakter Familienball fuer K0, Abstandsmasse wie Runde 20/21).
Neu hier: Gauss-Klumpen, Absorberrahmen, Abschnitte mit Zwischenspeicher, Diagnosen, Auswertung B0 bis B3.

Verlet wie kf5_geburt.lauf() (Zeile fuer Zeile nachgebaut), danach der Absorber im Rahmen:
    vel += F dt/2; psi += vel dt; psi *= m; F = kraft(psi); vel += F dt/2; vel *= m
    m = exp(-sigma dt), sigma = SIGMA * xi^2, xi = clamp((max(|x|, |y|) - INNEN) / BREITE, 0, 1); innen m = 1 exakt.
Klumpen: psi = A exp(-r^2 / (2 s^2)), psi_t = -i w0 psi (Vorzeichen wie kf5_geburt, damit Q = +Q_F),
    Q = 2 w0 A^2 pi s^2 = Q_F, w0 = omega_F = sqrt(0,60); s aus dem Ladungsradius R_F (PLAN.md, Abschnitt 3).

Aufruf:  python bildung1.py lauf --stufe grob|fein --gruppe alle|a|b --von T0 --bis T1 [--rauch]
         python bildung1.py zusammen --geraet cpu
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

R6 = "/home/fmh/fmhc-physics-remote/runde6-kf5"
R21 = "/home/fmh/fmhc-physics-remote/runde21-kf-eich"
sys.path.insert(0, R6)
sys.path.insert(1, R21)
import torch  # noqa: E402
import kf5_geburt as kg  # noqa: E402
import kf_eich as ke  # noqa: E402

HIER = os.path.dirname(os.path.abspath(__file__))
F64 = torch.float64
C128 = torch.complex128
z7 = kg.z7

# ---- feste Parameter (PLAN.md, vor dem ersten echten Lauf) ----
W2_F = 0.60
BOX = kg.BOX0                                   # 96 wie Runde 6
ABS_BREITE, ABS_SIGMA = 16.0, 1.0               # Absorberrahmen 16 breit, sigma_max 1
INNEN = 0.5 * BOX - ABS_BREITE                  # ungedaempft fuer max(|x|, |y|) <= 32
T_ENDE = 1000.0
T_FEN = (50.0, 100.0, 200.0, 250.0, 500.0, 1000.0)   # Fensterenden; Fenster [T - 40, T]
T_KARTE = (100.0, 250.0, 500.0, 1000.0)
T_K0 = (50.0, 100.0, 200.0)
T_DIAG = 10.0
S0_HAUPT, S0_ZUSATZ = 0.3, 0.1
BALL_SUCH = 5.0
K_TOL = 1e-3
R_TOL_DEF = 1e-3
RINGE = (6.0, 12.0, 20.0, 32.0)
MASKE_ABSTAND = 8.0                             # Box-Pruefung: Maske S >= 0,6 bleibt bei max(|x|,|y|) <= INNEN - 8
B3_ANTEIL = 0.80
ZEITGRENZE_S = 560.0
FAKTOR = {"i": 1.0, "ii": 1.3, "iii": 0.7}
GAUSS_FAKTOR = {"rms": 1.0, "mittel": math.sqrt(math.pi) / 2.0, "halb": math.sqrt(math.log(2.0))}
GRUPPEN = {"alle": ["K0", "i", "ii", "iii"], "a": ["K0", "i"], "b": ["ii", "iii"]}
RAUCH_T_ENDE, RAUCH_T_FEN, RAUCH_FENSTER = 60.0, (8.0, 16.0, 40.0), 4.0


# ---------------------------------------------------------------- Hilfen

def radius_definitionen(prof):
    """Kandidaten fuer r_ladung am exakten Profil (rho ~ f^2, Flaechengewicht r dr, Trapez auf r = i H_R):
    rms = sqrt(<r^2>), mittel = <r>, halb = Radius mit der halben Ladung."""
    h = ke.H_R
    tf = prof["tf"]
    N = len(tf) - 1
    m0 = m1 = m2 = 0.0
    for i in range(N + 1):
        r = i * h
        w = 0.5 if i in (0, N) else 1.0
        s = tf[i] * tf[i]
        m0 += w * s * r
        m1 += w * s * r * r
        m2 += w * s * r * r * r
    kum = [0.0]
    for i in range(1, N + 1):
        kum.append(kum[-1] + 0.5 * h * (tf[i - 1] ** 2 * (i - 1) * h + tf[i] ** 2 * i * h))
    halb = None
    for i in range(1, N + 1):
        if kum[i] >= 0.5 * kum[-1]:
            a = (0.5 * kum[-1] - kum[i - 1]) / (kum[i] - kum[i - 1])
            halb = (i - 1 + a) * h
            break
    return {"rms": math.sqrt(m2 / m0), "mittel": m1 / m0, "halb": halb}


def klumpen_feld(g, A, s, w0):
    r2 = g.X ** 2 + g.Y ** 2
    psi = (A * torch.exp(-r2 / (2.0 * s * s))).to(C128).contiguous()
    vel = ((-1j * w0) * psi).contiguous()
    return psi, vel


def absorber(g, dt):
    ax = ((g.x1.abs() - INNEN) / ABS_BREITE).clamp(0.0, 1.0)
    xi = torch.maximum(ax.view(1, -1), ax.view(-1, 1))
    sigma = ABS_SIGMA * xi * xi
    return torch.exp(-sigma * dt).contiguous(), (xi > 0.0).to(F64)


def diag_zeile(g, s, rho, e, ringmasken, rahmen, maxnorm, t):
    dA = g.dA
    z = {"t": t, "Q_box": (rho.sum((1, 2)) * dA).tolist(), "E_box": (e.sum((1, 2)) * dA).tolist(),
         "S_max": s.amax((1, 2)).tolist(), "Q_rahmen": ((rho * rahmen).sum((1, 2)) * dA).tolist()}
    for R, mk in ringmasken.items():
        z[f"Q_r{R:g}"] = ((rho * mk).sum((1, 2)) * dA).tolist()
    mn = maxnorm.expand_as(s)
    leer = torch.full_like(s, -1.0)
    for thr in (2.0 * S0_HAUPT, 2.0 * S0_ZUSATZ, 1e-4, 1e-6):
        z[f"ausdehnung_{thr:g}"] = torch.where(s >= thr, mn, leer).amax((1, 2)).tolist()
    return z


# ---------------------------------------------------------------- lauf

def befehl_lauf(args):
    start = ke.jetzt()
    t_start = kg.uhr()
    fam = kg.Familie()
    knoten = ke.familien_knoten()
    kn = knoten[round(W2_F, 6)]
    Q_F, E_F, R_F = kn["Q"], kn["E"], kn["r_ladung"]
    w0 = math.sqrt(W2_F)
    dx, dt = kg.STUFEN[args.stufe]
    g = kg.Gitter(BOX, dx)
    namen = GRUPPEN[args.gruppe]
    B = len(namen)
    rauch = args.rauch
    t_fen_liste = RAUCH_T_FEN if rauch else T_FEN
    fenster = RAUCH_FENSTER if rauch else kg.FENSTER
    t_max = RAUCH_T_ENDE if rauch else T_ENDE
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
    print(f"BILDUNG-1 lauf {name}: Start {start} auf {kg.geraet_name()}, n {g.n}, B {B}, Faelle {','.join(namen)}",
          flush=True)
    # Profil, Radiusdefinition, Klumpen
    tp0 = kg.uhr()
    prof = ke.profil(W2_F)
    rdef = radius_definitionen(prof)
    rel = {k: v / R_F - 1.0 for k, v in rdef.items() if v is not None}
    beste = min(rel, key=lambda k: abs(rel[k]))
    wahl = beste if abs(rel[beste]) <= R_TOL_DEF else "rms"
    s_basis = R_F / GAUSS_FAKTOR[wahl]
    klumpen = {}
    for nm in ("i", "ii", "iii"):
        s_k = FAKTOR[nm] * s_basis
        A_k = math.sqrt(Q_F / (2.0 * w0 * math.pi * s_k * s_k))
        klumpen[nm] = {"faktor": FAKTOR[nm], "s": s_k, "A": A_k, "w0": w0, "S_max": A_k * A_k,
                       "ladungsradius_def": GAUSS_FAKTOR[wahl] * s_k}
    dauer = {"profil": kg.uhr() - tp0}
    print(f"  R_F (r_ladung, omega^2 {W2_F}) {R_F:.6f}; Profil: rms {rdef['rms']:.6f}, mittel {rdef['mittel']:.6f}, "
          f"halb {rdef['halb']:.6f}; Wahl {wahl} (rel {rel[beste]:+.2e}); Q_F {Q_F:.6f}, E_F {E_F:.6f}, w0 {w0:.6f}",
          flush=True)
    for nm, kl in klumpen.items():
        print(f"  Klumpen {nm}: s {kl['s']:.6f}, A {kl['A']:.6f}, S_max {kl['S_max']:.5f}", flush=True)
    # Anfangszustand oder Zwischenspeicher
    if von == 0.0:
        felder = []
        for nm in namen:
            if nm == "K0":
                felder.append(ke.ball_feld(g, prof, {"w2": W2_F, "v": 0.0, "amp": 1.0}))
            else:
                felder.append(klumpen_feld(g, klumpen[nm]["A"], klumpen[nm]["s"], w0))
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
    rr = torch.sqrt(g.X ** 2 + g.Y ** 2)
    ringmasken = {R: (rr <= R).to(F64) for R in RINGE}
    maxnorm = torch.maximum(g.X.abs(), g.Y.abs())
    m, rahmen = absorber(g, dt)
    s, rho, e = kg.dichten(g, psi, vel, nl)
    kpr, k_ok = {}, True
    if von == 0.0:
        q_box = (rho.sum((1, 2)) * g.dA).tolist()
        e_box = (e.sum((1, 2)) * g.dA).tolist()
        r_rms = torch.sqrt((rho * rr * rr).sum((1, 2)) / rho.sum((1, 2))).tolist()
        Q0, E0 = q_box, e_box
        for b, nm in enumerate(namen):
            if nm == "K0":
                omr, res = ke.omega_gitter(g, prof)
                k = {"Q": q_box[b], "E": e_box[b], "Q_soll": Q_F, "E_soll": E_F, "dQ_rel": q_box[b] / Q_F - 1.0,
                     "dE_rel": e_box[b] / E_F - 1.0, "omega_gitter": omr, "domega_rel": omr / w0 - 1.0,
                     "residuum_gitter": res, "r_rms_gitter": r_rms[b], "r_rms_zu_R_F_rel": r_rms[b] / R_F - 1.0,
                     "E_zu_Q": e_box[b] / q_box[b], "S_max": s[b].max().item()}
                k["bestanden"] = all(abs(k[x]) <= K_TOL for x in ("dQ_rel", "dE_rel", "domega_rel"))
            else:
                kl = klumpen[nm]
                k = {"Q": q_box[b], "E": e_box[b], "Q_soll": Q_F, "dQ_rel": q_box[b] / Q_F - 1.0,
                     "r_rms_gitter": r_rms[b], "s": kl["s"], "r_rms_zu_s_rel": r_rms[b] / kl["s"] - 1.0,
                     "E_zu_Q": e_box[b] / q_box[b], "E_zu_Q_familie_bei_Q_F": E_F / Q_F, "S_max": s[b].max().item()}
                k["bestanden"] = abs(k["dQ_rel"]) <= K_TOL and abs(k["r_rms_zu_s_rel"]) <= K_TOL
            k_ok = k_ok and k["bestanden"]
            kpr[nm] = k
            print(f"  K {nm}: Q {k['Q']:.6f} (soll {Q_F:.6f}, rel {k['dQ_rel']:+.2e}), E {k['E']:.6f}, E/Q "
                  f"{k['E_zu_Q']:.5f}, r_rms {k['r_rms_gitter']:.6f}, S_max {k['S_max']:.5f} -> "
                  f"{'bestanden' if k['bestanden'] else 'NICHT bestanden'}", flush=True)
    meta = {"karte": "BILDUNG-1 (R22)", "name": name, "start": start, "rauch": rauch, "fertig": False,
            "stufe": args.stufe, "gruppe": args.gruppe, "faelle": namen, "von": von, "bis": bis, "dx": dx, "dt": dt,
            "n": g.n, "box": g.box, "absorber": {"breite": ABS_BREITE, "sigma_max": ABS_SIGMA, "innen": INNEN,
                                                 "form": "sigma_max * xi^2, xi = (max(|x|,|y|) - innen)/breite"},
            "t_fenster": [T for T in t_fen_liste if von <= T - fenster and T <= bis], "fenster": fenster,
            "herkunft": ke.herkunft(), "bildung1_sha256": ke.sha(os.path.abspath(__file__)), "quelle": quelle,
            "R_F": R_F, "Q_F": Q_F, "E_F": E_F, "w0": w0, "radius_kandidaten": rdef, "radius_rel": rel,
            "radius_wahl": wahl, "klumpen": klumpen, "Q0": Q0, "E0": E0, "k_pruefung": kpr, "k_bestanden": k_ok}
    if not k_ok:
        meta["ende"] = ke.jetzt()
        meta["abbruch"] = "K-Pruefung nicht bestanden: keine Zeitentwicklung (PLAN.md)"
        ke.schreibe_json(pfad_json, meta)
        raise SystemExit(meta["abbruch"])
    # Zeitentwicklung
    n_fen = int(round(fenster / dt))
    je_fen = int(round(kg.DT_FENSTER / dt))
    je_diag = int(round(T_DIAG / dt))
    n_von, n_bis = int(round(von / dt)), int(round(bis / dt))
    fen_start = {int(round((T - fenster) / dt)): T for T in meta["t_fenster"]}
    fen_ende = {int(round(T / dt)): T for T in meta["t_fenster"]}
    S0s = (S0_HAUPT, S0_ZUSATZ)
    aktiv, ergebnisse, diag = {}, [], []
    dauer.update({"analyse": 0.0, "fenster": 0.0, "diag": 0.0})
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
            rate = (verg - dauer["analyse"] - dauer["fenster"] - dauer["diag"]) / 400.0
            prognose = (kg.uhr() - t_start) + 1.10 * rate * (n_bis - schritt) + 3.0 * len(fen_start)
            print(f"  Prognose Gesamtdauer {prognose:.0f} s ({rate * 1e3:.2f} ms je Schritt)", flush=True)
            if prognose > ZEITGRENZE_S:
                meta["ende"] = ke.jetzt()
                meta["abbruch"] = f"Prognose {prognose:.0f} s ueber {ZEITGRENZE_S:.0f} s"
                ke.schreibe_json(pfad_json, meta)
                raise SystemExit(meta["abbruch"] + ": Abschnitt teilen")
        d_jetzt = schritt % je_diag == 0
        neu = schritt in fen_start
        probe = neu or any(schritt >= a["start"] and (schritt - a["start"]) % je_fen == 0 for a in aktiv.values())
        if not (d_jetzt or probe):
            continue
        s, rho, e = kg.dichten(g, psi, vel, nl)
        if d_jetzt:
            td = kg.uhr()
            diag.append(diag_zeile(g, s, rho, e, ringmasken, rahmen, maxnorm, round(schritt * dt, 6)))
            dauer["diag"] += kg.uhr() - td
        if not probe:
            continue
        if neu:
            ta = kg.uhr()
            T = fen_start[schritt]
            a = {"start": schritt, "fzs": {}, "zeilen": {}, "s_max": s.amax((1, 2)).tolist(),
                 "q_box": (rho.sum((1, 2)) * g.dA).tolist(), "q_r12": ((rho * ringmasken[12.0]).sum((1, 2)) * g.dA).tolist()}
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
                for S0 in S0s:
                    fen = kg.fenster_auswerten(a["fzs"][(b, S0)], t0, kg.DT_FENSTER, fam, g.box)
                    zeile = a["zeilen"][(b, S0)]
                    ztr = zeile.get("tropfen", {})
                    beste_tr, dbest = None, None
                    for tr in fen["tropfen"]:
                        if tr["x0"] is None or tr["y0"] is None:
                            continue
                        d = math.hypot(tr["x0"], tr["y0"])
                        if d <= BALL_SUCH and (dbest is None or d < dbest):
                            beste_tr, dbest = tr, d
                    z2 = zeile["schwellen"]["2"]
                    eintrag = {"fall": nm, "S0": S0, "T": T, "fenster": [t0, T], "N_fenstertropfen": len(fen["tropfen"]),
                               "zaehlung": fen["zaehlung"], "N_komp_2S0": z2["N_komp"], "N_tropfen_2S0": z2["N_tropfen"],
                               "S_max_box_start": z7(a["s_max"][b]), "Q0": Q0[b],
                               "Q_box_anteil_start": z7(a["q_box"][b] / Q0[b]),
                               "Q_r12_anteil_start": z7(a["q_r12"][b] / Q0[b])}
                    if beste_tr is None:
                        eintrag.update({"klasse": "kein Tropfen", "rund": None, "Q_net": None, "Q_anteil": None})
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
                        eintrag["d_F"] = z7(q / Q_F - 1.0) if q is not None else None
                        om = beste_tr.get("omega_ruhe")
                        eintrag["domega_F"] = z7(om - w0) if om is not None else None
                    ergebnisse.append(eintrag)
    dauer["vorwaerts_gesamt"] = kg.uhr() - t_vor
    # Zwischenspeicher am Abschnittsende
    if bis < t_max:
        zp = ke.frei_pfad(os.path.join(zw, f"{args.stufe}_{args.gruppe}_t{int(bis)}.pt"))
        torch.save({"t": bis, "faelle": namen, "stufe": args.stufe, "psi": psi.cpu(), "vel": vel.cpu(), "Q0": Q0,
                    "E0": E0}, zp + ".tmp")
        os.replace(zp + ".tmp", zp)
        meta["zwischenspeicher"] = {"datei": zp, "sha256": ke.sha(zp)}
    dauer["gesamt"] = kg.uhr() - t_start
    n_schritte = n_bis - n_von
    ent = dauer["vorwaerts_gesamt"] - dauer["analyse"] - dauer["fenster"] - dauer["diag"]
    meta.update({"ende": ke.jetzt(), "fertig": True, "dauer_s": dauer, "schritte": n_schritte,
                 "ms_je_schritt": ent / max(1, n_schritte) * 1e3, "n_proben": n_proben,
                 "gpu_speicher_mb": (torch.cuda.max_memory_allocated() / 2 ** 20) if kg.DEV.type == "cuda" else None,
                 "diag": diag})
    if rauch:
        meta["n_eintraege"] = len(ergebnisse)
        meta["prognose_25000_schritte_s"] = ent / max(1, n_schritte) * 25000
        ke.schreibe_json(pfad_json, meta)
        print(f"RAUCH {name}: Durchlauf ok; Dauer [s] " + ", ".join(f"{x} {y:.1f}" for x, y in dauer.items())
              + f"; {meta['ms_je_schritt']:.2f} ms je Schritt (B {B}); 25000 Schritte ~ "
              f"{meta['prognose_25000_schritte_s']:.0f} s; GPU max {kg.fz(meta['gpu_speicher_mb'], '.0f')} MB; "
              f"Fenstereintraege {len(ergebnisse)} (nicht ausgegeben)", flush=True)
        for z in diag:
            print(f"  diag t {z['t']:g}: " + " | ".join(
                f"{nm}: Qbox {z['Q_box'][b] / Q0[b]:.6f} r6 {z['Q_r6'][b] / Q0[b]:.4f} r12 {z['Q_r12'][b] / Q0[b]:.4f} "
                f"r20 {z['Q_r20'][b] / Q0[b]:.4f} rahmen {z['Q_rahmen'][b] / Q0[b]:.2e} aus0.6 {z['ausdehnung_0.6'][b]:g} "
                f"aus1e-4 {z['ausdehnung_0.0001'][b]:g} aus1e-6 {z['ausdehnung_1e-06'][b]:g}"
                for b, nm in enumerate(namen)), flush=True)
        return
    meta["ergebnisse"] = ergebnisse
    ke.schreibe_json(pfad_json, meta)
    L = [f"BILDUNG-1 {name}: Ende {meta['ende']}, Dauer [s] " + ", ".join(f"{x} {y:.1f}" for x, y in dauer.items())
         + f", {meta['ms_je_schritt']:.2f} ms je Schritt"]
    for x in ergebnisse:
        L.append(zeilentext(x))
    with open(ke.frei_pfad(os.path.join(basis, name + "_bericht.txt")), "w") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L), flush=True)


def zeilentext(x):
    return (f"  {x.get('stufe', '')} {x['fall']} S0 {x['S0']} T {x['T']:g}: {x['klasse']} | rund {x.get('rund')} rmax/ra "
            f"{kg.fz(x.get('rmax_zu_ra'), '.3f')} | Q-Anteil {kg.fz(x.get('Q_anteil'), '.4f')} (r12 "
            f"{kg.fz(x.get('Q_r12_anteil_start'), '.4f')}, Box {kg.fz(x.get('Q_box_anteil_start'), '.4f')}) | omega "
            f"{kg.fz(x.get('omega_ruhe'), '.5f')} +- {kg.fz(x.get('u_omega'), '.1e')} (fam(Q) "
            f"{kg.fz(x.get('omega_familie_bei_Q'), '.5f')}) | E/Q {kg.fz(x.get('E_zu_Q'), '.4f')} (fam "
            f"{kg.fz(x.get('E_zu_Q_familie'), '.4f')}) | dQ* {kg.fz(x.get('dQ_stern'), '+.4f')} | E/Q-Abst "
            f"{kg.fz(x.get('EQ_abstand'), '+.4f')} | omega-Abst {kg.fz(x.get('omega_abstand'), '+.5f')} | Q-Schw "
            f"{kg.fz(x.get('Q_schwankung'), '.3f')} | S_max {kg.fz(x.get('S_max_start'), '.3f')} | v "
            f"{kg.fz(x.get('v_mess'), '.4f')}")


# ---------------------------------------------------------------- zusammen (B0 bis B3, Box, Regeln PLAN.md)

def befehl_zusammen(args):
    out = os.path.join(HIER, "lauf-69", "ausgabe")
    eintraege, kpr, dateien, diag, q0 = [], {}, [], {}, {}
    for p in sorted(glob.glob(os.path.join(out, "*_ergebnis.json"))):
        with open(p) as fh:
            d = json.load(fh)
        if d.get("rauch") or not d.get("fertig"):
            continue
        dateien.append({"datei": os.path.basename(p), "sha256": ke.sha(p), "stufe": d["stufe"], "gruppe": d["gruppe"],
                        "von": d["von"], "bis": d["bis"], "radius_wahl": d["radius_wahl"]})
        for x in d["ergebnisse"]:
            x["stufe"] = d["stufe"]
            eintraege.append(x)
        for nm, k in d["k_pruefung"].items():
            kpr[f"{d['stufe']}/{nm}"] = k
        for b, nm in enumerate(d["faelle"]):
            q0[(d["stufe"], nm)] = d["Q0"][b]
            dd = diag.setdefault((d["stufe"], nm), {})
            for z in d["diag"]:
                dd[z["t"]] = {x: (v[b] if isinstance(v, list) else v) for x, v in z.items()}

    def such(stufe, fall, T, S0=S0_HAUPT):
        return [x for x in eintraege if x["stufe"] == stufe and x["fall"] == fall and abs(x["T"] - T) < 1e-9
                and abs(x["S0"] - S0) < 1e-12]

    def ok(x):
        return x["klasse"] == "auf" and bool(x["rund"])

    erg = {"zeit": ke.jetzt(), "dateien": dateien, "k_pruefung": kpr}
    # Box-Pruefung je Lauf (Stufe, Fall)
    box = {}
    for (st, nm), dd in sorted(diag.items()):
        ts = sorted(dd)
        aus06 = max(dd[t]["ausdehnung_0.6"] for t in ts)
        qb = [dd[t]["Q_box"] / q0[(st, nm)] for t in ts]
        box[f"{st}/{nm}"] = {"t_von_bis": [ts[0], ts[-1]], "n_diag": len(ts), "ausdehnung_0.6_max": aus06,
                             "bestanden": (ts[-1] >= T_ENDE - 1e-9) and aus06 <= INNEN - MASKE_ABSTAND,
                             "Q_box_anteil_ende": qb[-1], "Q_box_drift_max": max(abs(v - 1.0) for v in qb),
                             "Q_rahmen_anteil_max": max(dd[t]["Q_rahmen"] / q0[(st, nm)] for t in ts),
                             "Q_r12_anteil_ende": dd[ts[-1]]["Q_r12"] / q0[(st, nm)],
                             "ausdehnung_0.2_max": max(dd[t]["ausdehnung_0.2"] for t in ts)}
    erg["box"] = box
    box_ok = {k: v["bestanden"] for k, v in box.items()}
    z = {}
    # B0
    sel = [x for st in ("grob", "fein") for T in T_K0 for x in such(st, "K0", T)]
    if len(sel) < 2 * len(T_K0):
        z["B0"] = f"offen (unvollstaendig: {len(sel)} von {2 * len(T_K0)})"
    else:
        n = sum(1 for x in sel if ok(x))
        z["B0"] = "eingetroffen" if n == len(sel) else "nicht eingetroffen"
        z["B0_zahl"] = f"{n} von {len(sel)} 'auf' und rund"
    # B1
    sel = [x for st in ("grob", "fein") for x in such(st, "i", 500.0)]
    if len(sel) < 2:
        z["B1"] = f"offen (unvollstaendig: {len(sel)} von 2)"
    elif not all(box_ok.get(f"{st}/i", False) for st in ("grob", "fein")):
        z["B1"] = "offen (Box-Pruefung nicht bestanden)"
    else:
        n = sum(1 for x in sel if ok(x))
        z["B1"] = "eingetroffen" if n == 2 else "nicht eingetroffen"
        z["B1_zahl"] = f"{n} von 2 'auf' und rund"
    # B2
    sel = [x for st in ("grob", "fein") for nm in ("ii", "iii") for x in such(st, nm, 1000.0)]
    if len(sel) < 4:
        z["B2"] = f"offen (unvollstaendig: {len(sel)} von 4)"
    elif not all(box_ok.get(f"{st}/{nm}", False) for st in ("grob", "fein") for nm in ("ii", "iii")):
        z["B2"] = "offen (Box-Pruefung nicht bestanden)"
    else:
        n = sum(1 for x in sel if ok(x))
        z["B2"] = "eingetroffen" if n == 4 else "nicht eingetroffen"
        z["B2_zahl"] = f"{n} von 4 'auf' und rund"
    # B3
    anteile, fehlt = [], 0
    for st in ("grob", "fein"):
        for nm in ("i", "ii", "iii"):
            h, zu = such(st, nm, 1000.0), such(st, nm, 1000.0, S0_ZUSATZ)
            if not h or not zu:
                fehlt += 1
                continue
            if h[0]["Q_anteil"] is not None:
                anteile.append((st, nm, h[0]["Q_anteil"], "S0 0,3"))
            elif zu[0]["Q_anteil"] is not None:
                anteile.append((st, nm, zu[0]["Q_anteil"], "S0 0,1 (Ersatz)"))
            else:
                anteile.append((st, nm, 0.0, "kein Ball"))
    if fehlt:
        z["B3"] = f"offen (unvollstaendig: {fehlt} Laeufe fehlen)"
    elif not all(box_ok.get(f"{st}/{nm}", False) for st in ("grob", "fein") for nm in ("i", "ii", "iii")):
        z["B3"] = "offen (Box-Pruefung nicht bestanden)"
    else:
        z["B3"] = "eingetroffen" if all(a[2] >= B3_ANTEIL for a in anteile) else "nicht eingetroffen"
    z["B3_anteile"] = [f"{a[0]}/{a[1]}: {a[2]:.4f} ({a[3]})" for a in anteile]
    # Bedeutung (Karte)
    if z["B0"] != "eingetroffen":
        z["bedeutung"] = "K0 nicht bestanden oder offen: B1 bis B3 ohne Aussage (PLAN.md)"
    elif z["B1"] == "eingetroffen" and z["B2"] == "eingetroffen":
        z["bedeutung"] = ("B1 und B2 eingetroffen: Einzelne Klumpen laufen auf die Familie zu. M1 ist in 2D fuer "
                          "isolierte Klumpen bildungsfaehig (Stufe 5, im Modell) [H]. Das 'nie auf' in KF-5 lag dann am "
                          "Verschmelzen bzw. an der Zeit (Karte)")
    elif z["B1"] == "nicht eingetroffen":
        z["bedeutung"] = ("B1 nicht eingetroffen: Auch ein einzelner, gut passender Klumpen erreicht die Familie bis "
                          "T = 500 nicht. Stufe 5 ist fraglich; Grund beschreiben (Karte)")
    else:
        z["bedeutung"] = "Fall nicht in der Karte (B1 und B2 nicht beide eingetroffen, B1 nicht gescheitert): beschreibend"
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
                       "d_Q_anteil": (abs(x["Q_anteil"] - y["Q_anteil"])
                                      if (x.get("Q_anteil") is not None and y.get("Q_anteil") is not None) else None)})
    erg["L3"] = {"paare": len(l3), "klasse_gleich": sum(1 for v in l3 if v["gleich"]), "einzeln": l3}
    erg["vorhersagen"] = z
    pfad = ke.frei_pfad(os.path.join(out, "zusammen.json"))
    ke.schreibe_json(pfad, erg)
    L = [f"BILDUNG-1 zusammen ({erg['zeit']}), {len(dateien)} Dateien"]
    for nr in ("B0", "B1", "B2", "B3"):
        L.append(f"  {nr}: {z[nr]}" + (f" ({z[nr + '_zahl']})" if nr + "_zahl" in z else ""))
    L.append(f"  B3-Anteile: {z['B3_anteile']}")
    L.append(f"  Bedeutung: {z['bedeutung']}")
    for k, v in box.items():
        L.append(f"  Box {k}: {'bestanden' if v['bestanden'] else 'NICHT bestanden'}; Maske 0,6 max-Norm max "
                 f"{v['ausdehnung_0.6_max']:g} (Grenze {INNEN - MASKE_ABSTAND:g}), Maske 0,2 max {v['ausdehnung_0.2_max']:g}; "
                 f"Q_box Ende {v['Q_box_anteil_ende']:.6f}, Drift max {v['Q_box_drift_max']:.2e}, Rahmen max "
                 f"{v['Q_rahmen_anteil_max']:.2e}, Q(r<=12) Ende {v['Q_r12_anteil_ende']:.4f}")
    L.append(f"  L3: {erg['L3']['klasse_gleich']} von {erg['L3']['paare']} Paaren gleiche Klasse")
    for S0 in (S0_HAUPT, S0_ZUSATZ):
        L.append(f"== S0 {S0}")
        for nm in ("K0", "i", "ii", "iii"):
            for T in T_FEN:
                for st in ("grob", "fein"):
                    for x in such(st, nm, T, S0):
                        L.append(zeilentext(x))
    with open(ke.frei_pfad(os.path.join(out, "zusammen.txt")), "w") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L), flush=True)


def main():
    ap = argparse.ArgumentParser(description="BILDUNG-1 (Runde 22, v3)")
    ap.add_argument("befehl", choices=["lauf", "zusammen"])
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda")
    ap.add_argument("--stufe", choices=list(kg.STUFEN), default="grob")
    ap.add_argument("--gruppe", choices=list(GRUPPEN), default="alle")
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
    print(f"bildung1 {args.befehl}: Start {ke.jetzt()}", flush=True)
    {"lauf": befehl_lauf, "zusammen": befehl_zusammen}[args.befehl](args)
    print(f"bildung1 {args.befehl}: Ende {ke.jetzt()}", flush=True)


if __name__ == "__main__":
    main()
