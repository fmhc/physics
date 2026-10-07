#!/usr/bin/env python3
"""G2-08 (Ideen-Evolution Gen 2): Q-Ball-Prisma. Kopie von RUNDE-01/qg1/qg1.py, umgebaut (Original unveraendert).

Karte: GEN-02/G2-08/KARTE.md. Explorativ, float64 / complex128, --geraet cuda|cpu (cpu nur fuer Formprobe oder kleine Laeufe).

Modell wie qg1 (d = 1):  L = A(x)|psi_t|^2 - B(x)|psi_x|^2 - C(x) U(S),  U(S) = S - S^2 + S^3/2.
    A = 1 + a Phi, B = 1 + b Phi (an Halbpunkten), C = 1 + c Phi. Variante A (Optik) (0, 4, 0), Variante C (volle Metrik)
    (-2, 2, 0). Geaendert gegen qg1: Phi(x) = Phi2 (1 + tanh((x - x_s)/w))/2 statt g x/2 (Stufe), Ball startet bei
    x0 = -20 mit Lorentz-Boost v (wie r5d.ball), Messung der Ladungsanteile links, in der Stufe, rechts.
Profil: geschlossener 1D-Anker f^2 = 2 a0/(1 + b0 cosh(2 sqrt(a0) y)) mit Ableitung (qg1 K0: Schuss gegen Anker
    1,2e-10, lauf-69); das Schiessen von qg1 entfaellt deshalb.
Schwellen (bindend, vor der Entwicklung, ohne erste Ordnung): im Gebiet hinter der Stufe (A2, B2 konstant) gilt bei
    fester Ladung M2 = sqrt(B2) E(Q/sqrt(A2 B2)) mit der Familie E(Q) des freien Balls (C = 1);
    v_cl = sqrt(1 - (M1/M2)^2), M1 = E(Q). Familie geschlossen: W = omega^2 I, G = sqrt(a0)/2 - b0^2 I/4, E = 2 (W + G),
    Q = 2 W/omega, I = sqrt(2) arcosh(1/b0).
Laufzeit je Lauf T_run = min(2000, 80/v) (skaliert mit der Geschwindigkeit, damit durchlaufende Baelle die Zone
    |x - x_s| < 6 verlassen und zurueckgeworfene den Schwamm bei |x| = 80 noch nicht erreichen); gemessen bei T_run.

Aufruf:  python prisma.py haupt|gegen [--geraet cuda|cpu] [--stufen beide|grob] [--faktor F] [--out ORDNER]
  haupt: 12 Schwellenlaeufe (A, C; omega^2 0,55/0,70/0,90; 0,95 und 1,05 der Schwelle) + 12 Prisma-Laeufe
         (v_P1, v_P2), grob; fein nur die vier Schwellenlaeufe bei omega^2 = 0,70 (L3).
  gegen: Phi2 = 0 (A, 0,70, v_P1) und umgekehrte Stufe Phi2 = -0,01 (A, 0,55, v_P1), grob.
  --faktor < 1 nur fuer die Formprobe (alle T_run mal F; Zahlen ungueltig).
"""
import argparse
import datetime
import json
import math
import os
import time

import torch

DEV = torch.device("cpu")
F64 = torch.float64

OMEGA2 = [0.55, 0.70, 0.90]
VARIANTEN = {"A": (0.0, 4.0, 0.0), "C": (-2.0, 2.0, 0.0)}
PHI2 = 0.01
X_S, W_STUFE = 0.0, 1.0
X0 = -20.0
ZONE = 6.0
L_BOX = 120.0            # Box [-L, L], Dirichlet-Rand (wie qg1)
X_SPONGE = 80.0          # Daempfungsschicht fuer |x| > X_SPONGE (wie qg1)
SIGMA0 = 1.0
DX, DT = 0.1, 0.05       # grob; fein halbiert beide
T_MEAS = 1.0
T_MAX, T_WEG = 2000.0, 80.0
SPALTEN = ["q_zurueck", "q_stufe", "q_durch", "q_box", "e_box", "q_schwammzone", "X_zurueck", "X_durch", "S_max"]


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    if DEV.type == "cuda":
        torch.cuda.synchronize()
    return time.perf_counter()


def teilen(a, b):
    return a / b if b != 0.0 else float("nan")


# ---------------------------------------------------------------- Familie und Schwellen (geschlossen)

def anker_wgv(w2):
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    integral = math.sqrt(2.0) * math.acosh(1.0 / b0)
    w = w2 * integral
    g = math.sqrt(a0) / 2.0 - b0 * b0 * integral / 4.0
    return w, g, w + g


def familie(w2):
    w, g, v = anker_wgv(w2)
    return 2.0 * w / math.sqrt(w2), w + g + v


def w2_von_q(q):
    lo, hi = 0.5 + 1e-13, 1.0 - 1e-13
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if familie(mid)[0] > q:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def schwelle(kopplung, w2, phi2):
    ka, kb, _ = kopplung
    a2, b2 = 1.0 + ka * phi2, 1.0 + kb * phi2
    q, m1 = familie(w2)
    m2 = math.sqrt(b2) * familie(w2_von_q(q / math.sqrt(a2 * b2)))[1]
    return {"v_cl": math.sqrt(max(0.0, 1.0 - (m1 / m2) ** 2)), "M1": m1, "M2": m2, "Q": q,
            "R_erste_Ordnung": (m2 / m1 - 1.0) / phi2 if phi2 else float("nan"),
            "licht_hinten": math.sqrt(b2 / a2)}


def alle_schwellen():
    return {f"{n}|{w2}": schwelle(k, w2, PHI2) for n, k in VARIANTEN.items() for w2 in OMEGA2}


# ---------------------------------------------------------------- Laeufe

def lauf(name, variante, w2, v, phi2=PHI2, rolle="schwelle", faktor=1.0, soll=None):
    return {"name": name, "variante": variante, "kopplung": VARIANTEN[variante], "omega2": w2, "v": v, "phi2": phi2,
            "rolle": rolle, "T_run": min(T_MAX, T_WEG / v) * faktor, "soll": soll}


def prisma_v(schw):
    v = {w2: schw[f"A|{w2}"]["v_cl"] for w2 in OMEGA2}
    return 0.5 * (v[0.70] + v[0.90]), 0.5 * (v[0.55] + v[0.70])


def laeufe_haupt(schw, faktor):
    aus = []
    for n in VARIANTEN:
        for w2 in OMEGA2:
            vc = schw[f"{n}|{w2}"]["v_cl"]
            aus.append(lauf(f"{n} w2={w2} 0,95 v_cl", n, w2, 0.95 * vc, faktor=faktor, soll="reflektiert"))
            aus.append(lauf(f"{n} w2={w2} 1,05 v_cl", n, w2, 1.05 * vc, faktor=faktor, soll="durch"))
    vp1, vp2 = prisma_v(schw)
    soll = {("A", "P1"): {0.55: "reflektiert", 0.70: "reflektiert", 0.90: "durch"},
            ("A", "P2"): {0.55: "reflektiert", 0.70: "durch", 0.90: "durch"},
            ("C", "P1"): {w2: "reflektiert" for w2 in OMEGA2}, ("C", "P2"): {w2: "reflektiert" for w2 in OMEGA2}}
    for n in VARIANTEN:
        for pn, vp in (("P1", vp1), ("P2", vp2)):
            for w2 in OMEGA2:
                aus.append(lauf(f"{n} w2={w2} {pn} v={vp:.5f}", n, w2, vp, rolle="prisma", faktor=faktor,
                                soll=soll[(n, pn)][w2]))
    return aus


def laeufe_gegen(schw, faktor):
    vp1, _ = prisma_v(schw)
    return [lauf("ohne Stufe A w2=0.7 v_P1", "A", 0.70, vp1, phi2=0.0, rolle="gegen", faktor=faktor, soll="durch"),
            lauf("umgekehrt A w2=0.55 v_P1", "A", 0.55, vp1, phi2=-PHI2, rolle="gegen", faktor=faktor, soll="durch")]


# ---------------------------------------------------------------- Zeitentwicklung

def gitter(dx):
    i0 = int(round(L_BOX / dx))
    return (torch.arange(2 * i0 + 1, dtype=F64, device=DEV) - i0) * dx


def profil_abl(y, w2):
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    z = (2.0 * math.sqrt(a0) * y).clamp(-700.0, 700.0)
    nen = 1.0 + b0 * torch.cosh(z)
    f = torch.sqrt(2.0 * a0 / nen)
    return f, -f * b0 * math.sqrt(a0) * torch.sinh(z) / nen


def entwickeln(laeufe, dx, dt):
    x = gitter(dx)
    xh = 0.5 * (x[1:] + x[:-1])

    def spalte(werte):
        return torch.tensor(werte, dtype=F64, device=DEV).unsqueeze(1)

    ka, kb, kc = (spalte([r["kopplung"][i] for r in laeufe]) for i in range(3))
    phi2 = spalte([r["phi2"] for r in laeufe])
    phi = phi2 * 0.5 * (1.0 + torch.tanh((x - X_S) / W_STUFE))
    phi_h = phi2 * 0.5 * (1.0 + torch.tanh((xh - X_S) / W_STUFE))
    koef_a, koef_b, koef_c = 1.0 + ka * phi, 1.0 + kb * phi_h, 1.0 + kc * phi
    inv_a = 1.0 / koef_a
    sigma = SIGMA0 * ((x.abs() - X_SPONGE).clamp(min=0.0) / (L_BOX - X_SPONGE)) ** 2
    psi, vel = [], []
    for r in laeufe:
        om, v = math.sqrt(r["omega2"]), r["v"]
        gam = 1.0 / math.sqrt(1.0 - v * v)
        f, fp = profil_abl(gam * (x - X0), r["omega2"])
        ph = torch.exp(1j * (om * gam * v * (x - X0)))
        psi.append(f * ph)
        vel.append((-gam * v * fp - 1j * om * gam * f) * ph)
    psi, vel = torch.stack(psi), torch.stack(vel)
    for a in (psi, vel):
        a[:, 0] = 0.0
        a[:, -1] = 0.0
    m_z = (x < X_S - ZONE).to(F64)
    m_d = (x > X_S + ZONE).to(F64)
    m_s = 1.0 - m_z - m_d
    m_sw = (x.abs() > X_SPONGE).to(F64)

    def kraft(psi):
        fluss = koef_b * (psi[:, 1:] - psi[:, :-1]) / dx
        lap = torch.zeros_like(psi)
        lap[:, 1:-1] = (fluss[:, 1:] - fluss[:, :-1]) / dx
        s = psi.real ** 2 + psi.imag ** 2
        return lap - koef_c * (1.0 - 2.0 * s + 1.5 * s * s) * psi

    def messen(psi, vel):
        s = psi.real ** 2 + psi.imag ** 2
        rho = 2.0 * koef_a * (psi * vel.conj()).imag
        e = koef_a * (vel.real ** 2 + vel.imag ** 2) + koef_c * (s - s * s + 0.5 * s ** 3)
        d = psi[:, 1:] - psi[:, :-1]
        e[:, :-1] += koef_b * (d.real ** 2 + d.imag ** 2) / (dx * dx)
        q_z, q_d = (rho * m_z).sum(1) * dx, (rho * m_d).sum(1) * dx
        return torch.stack([q_z, (rho * m_s).sum(1) * dx, q_d, rho.sum(1) * dx, e.sum(1) * dx,
                            (rho * m_sw).sum(1) * dx,
                            (x * rho * m_z).sum(1) * dx / torch.where(q_z.abs() > 1e-300, q_z, torch.ones_like(q_z)),
                            (x * rho * m_d).sum(1) * dx / torch.where(q_d.abs() > 1e-300, q_d, torch.ones_like(q_d)),
                            s.max(dim=1).values], dim=1)

    t_end = max(r["T_run"] for r in laeufe)
    n_s = int(math.ceil(t_end / dt))
    alle = int(round(T_MEAS / dt))
    reihe = [messen(psi, vel)]
    kr = kraft(psi)
    for n in range(1, n_s + 1):
        vel = vel + (0.5 * dt) * (kr * inv_a - sigma * vel)
        psi = psi + dt * vel
        kr = kraft(psi)
        vel = vel + (0.5 * dt) * (kr * inv_a - sigma * vel)
        if n % alle == 0:
            reihe.append(messen(psi, vel))
    daten = torch.stack(reihe).cpu()
    if not bool(torch.isfinite(daten[:, :, :6]).all()):
        raise RuntimeError("nicht endliche Messwerte: Lauf instabil")
    t = torch.arange(daten.shape[0], dtype=F64) * (alle * dt)
    return t, daten


# ---------------------------------------------------------------- Auswertung

def steigung(t, y):
    tm = t - t.mean()
    return float((tm * (y - y.mean())).sum() / (tm * tm).sum()) if t.numel() > 2 else float("nan")


def auswerten(laeufe, t, daten):
    zeilen = []
    for b, r in enumerate(laeufe):
        d = {k: daten[:, b, i] for i, k in enumerate(SPALTEN)}
        i_t = min(int(round(r["T_run"] / T_MEAS)), daten.shape[0] - 1)
        q0, e0 = float(d["q_box"][0]), float(d["e_box"][0])
        anteil = {k: float(d[f"q_{k}"][i_t]) / q0 for k in ("zurueck", "stufe", "durch")}
        anteil["frei"] = 1.0 - sum(anteil.values())
        ausgang = {"zurueck": "reflektiert", "stufe": "haengt", "durch": "durch"}[
            max(("zurueck", "stufe", "durch"), key=lambda k: anteil[k])]
        spaltet = anteil["durch"] > 0.1 and anteil["zurueck"] > 0.1
        m = (t >= 0.75 * t[i_t] - 1e-9) & (t <= t[i_t] + 1e-9)
        x_seite = d["X_durch"] if ausgang == "durch" else d["X_zurueck"]
        v2 = steigung(t[m], x_seite[m]) if ausgang != "haengt" else float("nan")
        if ausgang == "reflektiert" and not v2 < 0.0:
            ausgang = "vor der Stufe"          # links, aber nicht umgekehrt: Stufe nie erreicht (kein Ausgang)
        smax = d["S_max"][m]
        kontakt = d["q_schwammzone"].abs() > 1e-6 * abs(q0)
        i_k = int(torch.nonzero(kontakt)[0, 0]) if bool(kontakt[: i_t + 1].any()) else i_t + 1
        bis = slice(0, max(i_k, 1))
        a2 = 1.0 + r["kopplung"][0] * r["phi2"]
        b2 = 1.0 + r["kopplung"][1] * r["phi2"]
        licht = math.sqrt(b2 / a2) if ausgang == "durch" else 1.0
        zeilen.append({
            "name": r["name"], "variante": r["variante"], "omega2": r["omega2"], "v": r["v"], "phi2": r["phi2"],
            "rolle": r["rolle"], "soll": r["soll"], "T_run": r["T_run"], "anteile": anteil, "ausgang": ausgang,
            "richtig": ausgang == r["soll"], "spaltet": spaltet, "v2": v2,
            "S_max_schwankung": float((smax.max() - smax.min()) / (2.0 * smax.mean())) if smax.numel() else float("nan"),
            "t_kontakt": float(t[min(i_k, len(t) - 1)]),
            "plaus": {
                "ladung_bis_Schwamm_1e-6": {"max_rel": float((d["q_box"][bis] - q0).abs().max()) / abs(q0)},
                "energie_bis_Schwamm_1e-5": {"max_rel": float((d["e_box"][bis] - e0).abs().max()) / abs(e0)},
                "anteile_0_bis_1": {"min": min(anteil.values()), "max": max(anteil.values())},
                "summe_1": {"summe": sum(anteil.values()), "hinweis": "frei = Rest, Summe gilt per Bau"},
                "v2_unter_Licht": {"v2": v2, "licht": licht}}})
        p = zeilen[-1]["plaus"]
        p["ladung_bis_Schwamm_1e-6"]["bestanden"] = p["ladung_bis_Schwamm_1e-6"]["max_rel"] <= 1e-6
        p["energie_bis_Schwamm_1e-5"]["bestanden"] = p["energie_bis_Schwamm_1e-5"]["max_rel"] <= 1e-5
        p["anteile_0_bis_1"]["bestanden"] = p["anteile_0_bis_1"]["min"] >= -1e-9 and p["anteile_0_bis_1"]["max"] <= 1.0 + 1e-9
        p["summe_1"]["bestanden"] = abs(p["summe_1"]["summe"] - 1.0) <= 1e-3
        p["v2_unter_Licht"]["bestanden"] = (not math.isfinite(v2)) or abs(v2) < licht
    return zeilen


def pruefen_haupt(zeilen, schw):
    schw_z = [z for z in zeilen if z["rolle"] == "schwelle"]
    falsch_schw = [z["name"] for z in schw_z if not z["richtig"]]
    pr = [z for z in zeilen if z["rolle"] == "prisma"]
    falsch_a = [z["name"] for z in pr if z["variante"] == "A" and not z["richtig"]]
    sort_c = [z["name"] for z in pr if z["variante"] == "C" and z["ausgang"] != "reflektiert"]
    vc = [schw[f"C|{w2}"]["v_cl"] for w2 in OMEGA2]
    c_spanne = max(vc) / min(vc) - 1.0
    spalt = [z["name"] for z in zeilen if z["spaltet"]]
    durch = [z for z in zeilen if z["ausgang"] == "durch"]
    v4 = all(z["anteile"]["durch"] >= 0.97 and z["S_max_schwankung"] < 0.02 for z in durch)
    plaus = all(v["bestanden"] for z in zeilen for v in z["plaus"].values())
    return {
        "V1_C_schwellen_richtig": all(z["richtig"] for z in schw_z if z["variante"] == "C"),
        "V1_C_schwellen_spanne": c_spanne,
        "V2_A_schwellen_richtig": all(z["richtig"] for z in schw_z if z["variante"] == "A"),
        "V3_prisma_A_falsch": falsch_a, "V3_prisma_C_sortiert": sort_c,
        "V4_durch_97pz_und_Smax_2pz": v4,
        "falsche_schwellenlaeufe": falsch_schw, "spaltende_laeufe": spalt,
        "scheitert": len(falsch_schw) > 1 or bool(falsch_a) or bool(sort_c) or c_spanne > 0.02 or bool(spalt),
        "nicht_entscheidbar": not plaus, "plausibilitaet_bestanden": plaus}


def pruefen_gegen(zeilen):
    z0, zu = zeilen
    return {"ohne_Stufe_durch_v2_gleich_v_1e-3": {"ausgang": z0["ausgang"], "v2": z0["v2"], "v": z0["v"],
                                                   "rel": teilen(abs(z0["v2"] - z0["v"]), z0["v"]),
                                                   "bestanden": z0["ausgang"] == "durch"
                                                   and abs(z0["v2"] - z0["v"]) <= 1e-3 * z0["v"]},
            "umgekehrt_durch_v2_groesser_v": {"ausgang": zu["ausgang"], "v2": zu["v2"], "v": zu["v"],
                                              "bestanden": zu["ausgang"] == "durch" and zu["v2"] > zu["v"]},
            "plausibilitaet_bestanden": all(v["bestanden"] for z in zeilen for v in z["plaus"].values())}


def text_zeilen(zeilen):
    aus = ["  Lauf | v | T_run | Soll | Ausgang | Anteile zurueck/stufe/durch/frei | v2 | S_max-Schwankung | "
           "Ladung, Energie bis Schwamm"]
    for z in zeilen:
        a, p = z["anteile"], z["plaus"]
        aus.append(f"  {z['name']:30s} | {z['v']:.5f} | {z['T_run']:.0f} | {z['soll']} | {z['ausgang']}"
                   f"{' SPALTET' if z['spaltet'] else ''} | {a['zurueck']:.4f}/{a['stufe']:.4f}/{a['durch']:.4f}/"
                   f"{a['frei']:.1e} | {z['v2']:+.5f} | {z['S_max_schwankung']:.2e} | "
                   f"{p['ladung_bis_Schwamm_1e-6']['max_rel']:.1e}, {p['energie_bis_Schwamm_1e-5']['max_rel']:.1e}")
    return aus


def main():
    global DEV
    ap = argparse.ArgumentParser(description="G2-08 Q-Ball-Prisma (Kopie qg1)")
    ap.add_argument("teil", choices=["haupt", "gegen"])
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda")
    ap.add_argument("--stufen", choices=["beide", "grob"], default="beide")
    ap.add_argument("--faktor", type=float, default=1.0, help="nur Formprobe: alle T_run mal F")
    ap.add_argument("--out", default="ausgabe")
    args = ap.parse_args()
    if args.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("--geraet cuda, aber keine CUDA-Karte sichtbar: Abbruch (kein stiller CPU-Ausweg).")
        DEV = torch.device("cuda")
        name_geraet = torch.cuda.get_device_name(0)
    else:
        torch.set_num_threads(1)
        name_geraet = "CPU, 1 Thread"
    os.makedirs(args.out, exist_ok=True)
    start = jetzt()
    kopf = (f"G2-08 prisma.py {args.teil} Start {start} auf {name_geraet}, torch {torch.__version__}, Faktor {args.faktor}"
            + ("  FORMPROBE: Zahlen ungueltig" if args.faktor != 1.0 else ""))
    print(kopf, flush=True)
    schw = alle_schwellen()
    vp1, vp2 = prisma_v(schw)
    text = [kopf, f"Phi2 = {PHI2}, Stufe bei x_s = {X_S}, w = {W_STUFE}, Start x0 = {X0}, Zone |x - x_s| < {ZONE}",
            "Codeschwellen (bindend): Variante omega^2 | v_cl | M1 | M2 | (M2/M1 - 1)/Phi2 | Licht hinten"]
    for k, s in schw.items():
        text.append(f"  {k} | {s['v_cl']:.6f} | {s['M1']:.6f} | {s['M2']:.6f} | {s['R_erste_Ordnung']:.4f} | "
                    f"{s['licht_hinten']:.5f}")
    text.append(f"  v_P1 = {vp1:.6f}, v_P2 = {vp2:.6f}")
    laeufe = laeufe_haupt(schw, args.faktor) if args.teil == "haupt" else laeufe_gegen(schw, args.faktor)
    ausgabe = {"start": start, "geraet": name_geraet, "torch": torch.__version__, "teil": args.teil,
               "faktor": args.faktor, "schwellen": schw, "v_P1": vp1, "v_P2": vp2,
               "parameter": {"phi2": PHI2, "x_s": X_S, "w": W_STUFE, "x0": X0, "zone": ZONE, "L_box": L_BOX,
                             "x_sponge": X_SPONGE, "dx_dt_grob": [DX, DT], "T_run": f"min({T_MAX}, {T_WEG}/v) x Faktor"},
               "stufen": {}}
    stufen = [("grob", DX, DT, laeufe)]
    if args.teil == "haupt" and args.stufen == "beide":
        stufen.append(("fein", DX / 2.0, DT / 2.0,
                       [r for r in laeufe if r["rolle"] == "schwelle" and r["omega2"] == 0.70]))
    reihen = {}
    for stufe, dx, dt, ll in stufen:
        t0 = uhr()
        t, daten = entwickeln(ll, dx, dt)
        sek = uhr() - t0
        print(f"{stufe}: {len(ll)} Laeufe, T bis {max(r['T_run'] for r in ll):.0f}, {sek:.1f} s", flush=True)
        zeilen = auswerten(ll, t, daten)
        pr = pruefen_haupt(zeilen, schw) if (args.teil == "haupt" and stufe == "grob") else (
            pruefen_gegen(zeilen) if args.teil == "gegen" else None)
        ausgabe["stufen"][stufe] = {"zeilen": zeilen, "pruefung": pr, "sek": sek}
        reihen[stufe] = {"t": t, "daten": daten, "spalten": SPALTEN, "laeufe": ll}
        text += [f"[{stufe}] {sek:.1f} s"] + text_zeilen(zeilen)
        if pr is not None:
            text.append(f"  Pruefung [{stufe}]: {json.dumps(pr, default=str)}")
        with open(os.path.join(args.out, f"prisma_{args.teil}_ergebnis.json"), "w") as fh:
            json.dump(ausgabe, fh, indent=1, default=str)
    if "fein" in ausgabe["stufen"]:
        g = {z["name"]: z for z in ausgabe["stufen"]["grob"]["zeilen"]}
        l3 = []
        for zf in ausgabe["stufen"]["fein"]["zeilen"]:
            zg = g[zf["name"]]
            e = {"lauf": zf["name"], "gleicher_ausgang": {"bestanden": zg["ausgang"] == zf["ausgang"]}}
            if zg["ausgang"] == "durch" and zf["ausgang"] == "durch":
                eff, aend = abs(zg["v2"]), abs(zf["v2"] - zg["v2"])
                e["v2"] = {"effekt": eff, "aenderung": aend, "bestanden": bool(eff >= 5.0 * aend)}
            l3.append(e)
        ausgabe["L3"] = l3
        n_ok = sum(1 for e in l3 for k, v in e.items() if k != "lauf" and v["bestanden"])
        n_ges = sum(1 for e in l3 for k in e if k != "lauf")
        text.append(f"L3 (fein = dx/2, dt/2; gleicher Ausgang, v2 Effekt >= 5 x Aenderung): {n_ok} von {n_ges} bestanden")
    ausgabe["ende"] = jetzt()
    text.append(f"Ende {ausgabe['ende']}")
    with open(os.path.join(args.out, f"prisma_{args.teil}_ergebnis.json"), "w") as fh:
        json.dump(ausgabe, fh, indent=1, default=str)
    with open(os.path.join(args.out, f"prisma_{args.teil}_bericht.txt"), "w") as fh:
        fh.write("\n".join(text) + "\n")
    torch.save(reihen, os.path.join(args.out, f"prisma_{args.teil}_reihen.pt"))
    print("\n".join(text), flush=True)


if __name__ == "__main__":
    main()
