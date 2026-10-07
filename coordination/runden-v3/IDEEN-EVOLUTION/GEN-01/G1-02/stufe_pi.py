#!/usr/bin/env python3
"""G1-02 (GEN-01): Teilchen oder Welle an der Stufe, Spaltfenster ab Pi = V2 / (2 omega (1 - omega)) ~ 1.

Kopie der 1D-Teile aus coordination/runden-v3/RUNDE-06/weber/weber.py (Unterbefehl feinv1d). Unveraendert uebernommen:
anker, masse_medium, v_aus_masse, schranken1d (v_cl exakt aus gamma M1 = M2), klassisch1d, ball1d, Kraft und
Velocity-Verlet mit Daempfungsschicht, Messgroessen, fragmente1d, klassifizieren, dx = 0,1, dt = 0,05 (--fein: halbiert),
Q_FRAG_MIN, S_REL_FRAG. Das Original bleibt unveraendert.
Neu (KARTE.md, auch Ergaenzung T-1 vor dem Stempel): Parameter als Argumente (omega^2, V2-Liste, Stufenbreite B,
Startabstand, v/v_cl-Liste, Box, Zone, T = t_a/v + t_b); jeder Lauf wird bei seinem eigenen T ausgewertet (Zustand dort
gesichert); Gegenproben B = 25 und V2 = 0 als eigener Aufruf; Urteil nach den Regeln der Karte; Plausibilitaetsschranke
als eigene Pruefung mit "bestanden"; L3 grob gegen fein.

Unterbefehle:
  papier   v_cl, Pi, Pi/(1 + Pi) je Stufe (Sekunden, nur Formeln)
  haupt    B = 1, V2 = 0,01 0,05 0,10 0,20, zehn v/v_cl (40 Laeufe, Box +-200)
  gegen    B = 25 bei V2 = 0,20 (10 Laeufe, Box +-1200, Zone 50, T = 180/v + 1000) und V2 = 0 bei den zehn v von V2 = 0,20
  urteil   --a haupt_<stufe>_ergebnis.json --b gegen_<stufe>_ergebnis.json: V1 bis V4, Scheitert-Regeln, Gegenproben
  l3       --a <grob.json> --b <fein.json>: gleiche Klassen, |dq_durch| <= 0,05, Effekt >= 5 x Aenderung

Aufruf: python stufe_pi.py <unterbefehl> [--geraet cuda|cpu] [--fein] [--out ORDNER] [--rauch FAKTOR] [Parameter]
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

SPEICHER_GB = 1.5
T_MESS = 1.0
Q_FRAG_MIN = 0.05          # wie weber.py
ZERFALL_GRENZE = 0.5       # wie weber.py
S_REL_FRAG = 0.01          # wie weber.py
SIGMA0 = 1.0               # wie weber.py
DX1, DT1, FEIN = 0.1, 0.05, 0.5

# Vorgaben der Karte G1-02
W2 = 0.9
V2_HAUPT = "0.01,0.05,0.10,0.20"
REL = "0.90,0.95,0.98,1.00,1.02,1.05,1.10,1.20,1.35,1.50"
BOX_B1 = {"B": 1.0, "L": 200.0, "x_schwamm": 160.0, "x0": 20.0, "x_s": 8.0, "t_a": 45.0, "t_b": 200.0}
BOX_B25 = {"B": 25.0, "L": 1200.0, "x_schwamm": 1160.0, "x0": 80.0, "x_s": 50.0, "t_a": 180.0, "t_b": 1000.0}
TOL_NULL = 1e-4            # Ergaenzung T-1: Toleranz der Pruefungen ">= 0"
TOL_SUMME = 0.01
E_DRIFT_MAX = 1e-3


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    if DEV.type == "cuda":
        torch.cuda.synchronize()
    return time.perf_counter()


def geraet_name():
    return torch.cuda.get_device_name(0) if DEV.type == "cuda" else "cpu"


def schreiben(out, name, ausgabe, text):
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, name + "_ergebnis.json"), "w") as fh:
        json.dump(ausgabe, fh, indent=1)
    with open(os.path.join(out, name + "_bericht.txt"), "w") as fh:
        fh.write(text + "\n")
    print(text, flush=True)


# ---------------------------------------------------------------- aus weber.py (unveraendert)

def anker(w2):
    """Geschlossene 1D-Werte: N = sqrt(2) arcosh(1/b0), G = sqrt(a0)/2 - b0^2 N/4, Q = 2 omega N, E = omega Q + 2 G."""
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    w = math.sqrt(w2)
    n = math.sqrt(2.0) * math.acosh(1.0 / b0)
    g = math.sqrt(a0) / 2.0 - b0 * b0 * n / 4.0
    s_c = 2.0 * a0 / (1.0 + b0)
    q = 2.0 * w * n
    d = n / s_c
    rho_w = 2.0 * w2 * s_c
    return {"w2": w2, "omega": w, "a0": a0, "b0": b0, "N": n, "G": g, "Q": q, "E": w * q + 2.0 * g, "S_c": s_c,
            "D": d, "rho_W": rho_w, "sigma": g, "we_faktor": rho_w * d / g}


def masse_medium(q, v2):
    lo, hi = 0.5 + 1e-12, 1.0 - 1e-12
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if 2.0 * math.sqrt(mid + v2) * anker(mid)["N"] > q:
            lo = mid
        else:
            hi = mid
    w = 0.5 * (lo + hi)
    a = anker(w)
    om = math.sqrt(w + v2)
    return {"w2_familie": w, "omega_medium": om, "M": om * q + 2.0 * a["G"], "N": a["N"]}


def v_aus_masse(m1, m_ziel):
    return 0.0 if m_ziel <= m1 else math.sqrt(1.0 - (m1 / m_ziel) ** 2)


def v_cl(w2, v2):
    """Klassische Stufenschwelle wie schranken1d in weber.py: gamma M1 = M2."""
    a = anker(w2)
    m1, q = a["E"], a["Q"]
    m2 = masse_medium(q, v2)["M"]
    return v_aus_masse(m1, m2) if m2 > m1 else None


def klassisch1d(w2, v2, v):
    a = anker(w2)
    m1 = a["E"]
    m2 = masse_medium(a["Q"], v2)["M"] if v2 != 0.0 else m1
    gam1 = 1.0 / math.sqrt(1.0 - v * v)
    if gam1 * m1 > m2:
        gam2 = gam1 * m1 / m2
        return "durch", math.sqrt(1.0 - 1.0 / (gam2 * gam2))
    return "reflektiert", v


def ball1d(a, x, xc, v):
    gam = 1.0 / math.sqrt(1.0 - v * v)
    xi = gam * (x - xc)
    k = math.sqrt(a["a0"])
    arg = (2.0 * k * xi).clamp(-600.0, 600.0)
    nenner = 1.0 + a["b0"] * torch.cosh(arg)
    f = torch.sqrt(2.0 * a["a0"] / nenner)
    fp = -f * k * a["b0"] * torch.sinh(arg) / nenner
    ph = torch.exp(1j * (a["omega"] * gam * v * (x - xc)))
    return f * ph, (-gam * v * fp - 1j * a["omega"] * gam * f) * ph


def fragmente1d(s, rho, x, dx, s_thr, q0):
    m = (s > s_thr).to(torch.int64)
    if int(m.sum()) == 0:
        return []
    null = torch.zeros(1, dtype=torch.int64)
    d = torch.diff(m, prepend=null, append=null)
    anf = (d == 1).nonzero().flatten().tolist()
    end = (d == -1).nonzero().flatten().tolist()
    aus = []
    for i, j in zip(anf, end):
        w = rho[i:j]
        q = w.sum().item() * dx
        xs = x[i:j]
        xm = (w * xs).sum().item() / w.sum().item() if abs(w.sum().item()) > 1e-300 else xs.mean().item()
        aus.append({"q": q / q0, "x": xm, "S_max": s[i:j].max().item(), "breite": (j - i) * dx})
    return sorted(aus, key=lambda f: -f["q"])


def klassifizieren(fr, q_mitte, x_s):
    n5 = sum(1 for f in fr if f["q"] >= Q_FRAG_MIN)
    q_t = sum(f["q"] for f in fr if f["x"] > x_s and f["q"] >= Q_FRAG_MIN)
    q_r = sum(f["q"] for f in fr if f["x"] < -x_s and f["q"] >= Q_FRAG_MIN)
    q_frei = 1.0 - sum(f["q"] for f in fr)
    haupt = fr[0] if fr else None
    q_h = haupt["q"] if haupt else 0.0
    if q_mitte >= 0.2:
        k = "haengt"
    elif n5 >= 3 or q_frei >= 0.3:
        k = "zerspritzt"
    elif q_t >= 0.1 and q_r >= 0.1:
        k = "gespalten"
    elif q_h >= 0.9:
        k = "durch" if haupt["x"] > x_s else ("reflektiert" if haupt["x"] < -x_s else "haengt")
    else:
        k = "angeschlagen"
    return {"klasse": k, "zerfall": q_h < ZERFALL_GRENZE, "q_haupt": q_h, "x_haupt": haupt["x"] if haupt else None,
            "q_durch": q_t, "q_zurueck": q_r, "q_frei": q_frei, "n_frag": n5}


# ---------------------------------------------------------------- Gitter und Zeitentwicklung (Box als Parameter)

def gitter1d(dx, L):
    i0 = int(round(L / dx))
    return (torch.arange(2 * i0 + 1, dtype=F64, device=DEV) - i0) * dx


def messen1d_bauen(x, dx, V, x_s):
    links = (x < -x_s).to(F64)
    mitte = (x.abs() <= x_s).to(F64)
    rechts = (x > x_s).to(F64)

    def messen(psi, vel):
        s = psi.real ** 2 + psi.imag ** 2
        rho = 2.0 * (psi * vel.conj()).imag
        gx = torch.zeros_like(psi)
        gx[:, 1:-1] = (psi[:, 2:] - psi[:, :-2]) / (2.0 * dx)
        e = vel.real ** 2 + vel.imag ** 2 + gx.real ** 2 + gx.imag ** 2 + s - s * s + 0.5 * s ** 3 + V * s
        return torch.stack([(rho * links).sum(1) * dx, (rho * mitte).sum(1) * dx, (rho * rechts).sum(1) * dx,
                            rho.sum(1) * dx, e.sum(1) * dx, (rho * links * x).sum(1) * dx,
                            (rho * rechts * x).sum(1) * dx], dim=1)
    return messen


def entwickeln1d(psi, vel, V, x, dx, dt, n_ende, messen, L, x_schwamm):
    """Velocity-Verlet wie weber.py; der Zustand von Lauf b wird im Schritt n_ende[b] gesichert."""
    sigma = SIGMA0 * ((x.abs() - x_schwamm).clamp(min=0.0) / (L - x_schwamm)) ** 2

    def kraft(p):
        fluss = (p[:, 1:] - p[:, :-1]) / dx
        lap = torch.zeros_like(p)
        lap[:, 1:-1] = (fluss[:, 1:] - fluss[:, :-1]) / dx
        s = p.real ** 2 + p.imag ** 2
        return lap - (1.0 - 2.0 * s + 1.5 * s * s + V) * p

    fertig = {}
    for b, n in enumerate(n_ende):
        fertig.setdefault(n, []).append(b)
    alle = max(1, int(round(T_MESS / dt)))
    psi_e, vel_e = psi.clone(), vel.clone()
    reihe = [messen(psi, vel)]
    kr = kraft(psi)
    for n in range(1, max(n_ende) + 1):
        vel = vel + (0.5 * dt) * (kr - sigma * vel)
        psi = psi + dt * vel
        kr = kraft(psi)
        vel = vel + (0.5 * dt) * (kr - sigma * vel)
        if n % alle == 0:
            reihe.append(messen(psi, vel))
        if n in fertig:
            for b in fertig[n]:
                psi_e[b] = psi[b]
                vel_e[b] = vel[b]
    daten = torch.stack(reihe)
    if not bool(torch.isfinite(daten).all()):
        raise RuntimeError("nicht endliche Messwerte: Lauf instabil")
    return daten, psi_e, vel_e, alle


def rechne1d(laeufe, box, dx, dt, rauch):
    """Ein Stapel in einer Box; Ballzentrum startet bei -x0, Stufe V2 (1 + tanh(x/B))/2 bei x = 0."""
    x = gitter1d(dx, box["L"])
    psis, vels, vs, n_ende, t_ende = [], [], [], [], []
    alle = max(1, int(round(T_MESS / dt)))
    for lf in laeufe:
        p, pv = ball1d(anker(lf["w2"]), x, -box["x0"], lf["v"])
        psis.append(p)
        vels.append(pv)
        vs.append(lf["V2"] * 0.5 * (1.0 + torch.tanh(x / box["B"])))
        t_soll = (box["t_a"] / lf["v"] + box["t_b"]) * rauch
        k = max(21, int(math.ceil(t_soll / T_MESS)))
        n_ende.append(k * alle)
        t_ende.append(k * alle * dt)
    psi = torch.stack(psis).contiguous()
    vel = torch.stack(vels).contiguous()
    V = torch.stack(vs).contiguous()
    for a in (psi, vel):
        a[:, 0] = 0.0
        a[:, -1] = 0.0
    daten, psi_e, vel_e, alle = entwickeln1d(psi, vel, V, x, dx, dt, n_ende, messen1d_bauen(x, dx, V, box["x_s"]),
                                             box["L"], box["x_schwamm"])
    s_end = (psi_e.real ** 2 + psi_e.imag ** 2).cpu()
    rho_end = (2.0 * (psi_e * vel_e.conj()).imag).cpu()
    xc = x.cpu()
    d = daten.cpu()
    zeilen = []
    for b, lf in enumerate(laeufe):
        a = anker(lf["w2"])
        k = n_ende[b] // alle
        q0, e0 = d[0, b, 3].item(), d[0, b, 4].item()
        fr = fragmente1d(s_end[b], rho_end[b], xc, dx, S_REL_FRAG * a["S_c"], q0)
        kl = klassifizieren(fr, d[k, b, 1].item() / q0, box["x_s"])
        z = {**lf, "B": box["B"], "x_s": box["x_s"], "L": box["L"], "dx": dx, "dt": dt, "t_ende": t_ende[b], **kl,
             "fragmente": fr[:6], "Q0": q0, "E0": e0, "q_mitte_ende": d[k, b, 1].item() / q0,
             "q_box_ende": d[k, b, 3].item() / q0, "E_drift_max": ((d[:k + 1, b, 4] / e0 - 1.0).abs().max()).item()}
        for seite, iq, ix in (("durch", 2, 6), ("zurueck", 0, 5)):
            qa, qb = d[k - 20, b, iq].item(), d[k, b, iq].item()
            if qa >= Q_FRAG_MIN * q0 and qb >= Q_FRAG_MIN * q0:
                z["v_" + seite] = (d[k, b, ix].item() / qb - d[k - 20, b, ix].item() / qa) / (20.0 * T_MESS)
        z["vorhersage_teilchen"], z["v_aus_teilchen"] = klassisch1d(lf["w2"], lf["V2"], lf["v"])
        zeilen.append(z)
    return zeilen


# ---------------------------------------------------------------- Kenngroessen und Pruefungen

def pi_wert(w2, v2):
    om = math.sqrt(w2)
    return v2 / (2.0 * om * (1.0 - om))


def spalt(z):
    """Rasterpunkt im Spaltfenster: 0,1 < q_durch < 0,9 (Karte, Messgroessen)."""
    return 0.1 < z["q_durch"] < 0.9


def spalt_streng(z):
    """'gespalten' im Sinn von V2: zwei Fragmente, eines je Seite, q_frei <= 0,15."""
    return (spalt(z) and z["n_frag"] == 2 and z["q_zurueck"] >= Q_FRAG_MIN and z["q_durch"] >= Q_FRAG_MIN
            and z["q_frei"] <= 0.15)


def stufe_kennzahlen(zz):
    """dT = q_durch(1,02 v_cl) - q_durch(0,98 v_cl), Spaltfenster W, strenge Spaltpunkte, Monotonie im Fenster."""
    zz = sorted(zz, key=lambda z: z["rel"])
    bei = {round(z["rel"], 4): z for z in zz}
    dT = None
    if 0.98 in bei and 1.02 in bei:
        dT = bei[1.02]["q_durch"] - bei[0.98]["q_durch"]
    fenster = [z for z in zz if spalt(z)]
    mono = all(b["q_durch"] >= a["q_durch"] - 0.05 for a, b in zip(fenster[:-1], fenster[1:]))
    return {"V2": zz[0]["V2"], "B": zz[0]["B"], "Pi": pi_wert(zz[0]["w2"], zz[0]["V2"]), "dT": dT,
            "W": len(fenster), "W_rel": [z["rel"] for z in fenster],
            "spalt_streng_rel": [z["rel"] for z in zz if spalt_streng(z)], "monoton_im_fenster": mono,
            "q_durch": [[z["rel"], round(z["q_durch"], 4), z["klasse"]] for z in zz]}


def plausibel(zeilen):
    """Plausibilitaetsschranke der Karte je Lauf; V4 (Energie) nur fuer Laeufe mit v <= 1,02 v_cl im Spaltfenster."""
    verstoesse = []
    for z in zeilen:
        name = f"V2 {z['V2']:.2f} B {z['B']:.0f} rel {z['rel']:.2f}"
        for k in ("q_durch", "q_zurueck", "q_frei"):
            if z[k] < -TOL_NULL:
                verstoesse.append(f"{name}: {k} = {z[k]:.5f} < 0")
        summe = z["q_durch"] + z["q_zurueck"] + z["q_frei"]
        if abs(summe - 1.0) > TOL_SUMME:
            verstoesse.append(f"{name}: q_durch + q_zurueck + q_frei = {summe:.4f} (Klasse {z['klasse']})")
        if z["E_drift_max"] >= E_DRIFT_MAX:
            verstoesse.append(f"{name}: |E-Drift| = {z['E_drift_max']:.2e} >= 1e-3")
        for k in ("v_durch", "v_zurueck"):
            if k in z and abs(z[k]) >= 1.0:
                verstoesse.append(f"{name}: |{k}| = {abs(z[k]):.3f} >= 1")
        if z["V2"] > 0.0 and z["rel"] <= 1.02 + 1e-9 and spalt(z):
            p = pi_wert(z["w2"], z["V2"])
            if z["q_durch"] > p / (1.0 + p) + 0.05:
                verstoesse.append(f"{name}: V4 q_durch {z['q_durch']:.3f} > Pi/(1+Pi) + 0,05 = {p / (1 + p) + 0.05:.3f}")
    return {"bestanden": not verstoesse, "verstoesse": verstoesse, "laeufe": len(zeilen)}


def zeile_text(z):
    frs = ", ".join(f"{f['q']:.3f}@{f['x']:.1f}" for f in z["fragmente"][:4])
    return (f"  V2 {z['V2']:.2f} B {z['B']:>4.0f} rel {z['rel']:.2f} v {z['v']:.4f} T {z['t_ende']:.0f} | "
            f"{z['klasse']:<12} | q_h {z['q_haupt']:.3f} | durch {z['q_durch']:.3f} | zurueck {z['q_zurueck']:.3f} | "
            f"frei {z['q_frei']:.3f} | n {z['n_frag']} | E-Drift {z['E_drift_max']:.1e} | Teilchenbild "
            f"{z['vorhersage_teilchen']} | {frs}")


# ---------------------------------------------------------------- Unterbefehle

def laeufe_bauen(w2, v2_liste, rel_liste, v2_fuer_v=None):
    aus = []
    for v2 in v2_liste:
        vc = v_cl(w2, v2_fuer_v if v2_fuer_v is not None else v2)
        if vc is None:
            raise SystemExit(f"keine klassische Schwelle fuer V2 = {v2}")
        for rel in rel_liste:
            aus.append({"w2": w2, "V2": v2, "rel": rel, "v_cl": vc, "v": round(vc * rel, 8)})
    return aus


def test_papier(out, w2, v2_liste):
    zeilen = []
    for v2 in v2_liste:
        p = pi_wert(w2, v2)
        zeilen.append({"V2": v2, "Pi": p, "grenze_Pi_1_plus_Pi": p / (1.0 + p), "v_cl": v_cl(w2, v2)})
    a = anker(w2)
    text = [f"papier G1-02: omega^2 {w2}, omega {a['omega']:.5f}, 1 - omega {1 - a['omega']:.5f}, Q {a['Q']:.5f}, "
            f"E {a['E']:.5f}, S_c {a['S_c']:.5f}"]
    text += [f"  V2 {z['V2']:.2f}: Pi {z['Pi']:.4f}, Pi/(1+Pi) {z['grenze_Pi_1_plus_Pi']:.4f}, v_cl {z['v_cl']:.5f}"
             for z in zeilen]
    schreiben(out, "papier", {"test": "papier", "start": jetzt(), "anker": a, "stufen": zeilen}, "\n".join(text))


def lauf_gruppe(out, name, gruppen, fein, rauch, args):
    start = jetzt()
    dx, dt, stufe = (DX1 * FEIN, DT1 * FEIN, "fein") if fein else (DX1, DT1, "grob")
    print(f"{name} {stufe} Start {start} auf {geraet_name()}, torch {torch.__version__}", flush=True)
    zeilen, dauer = [], {}
    for gname, box, laeufe in gruppen:
        t0 = uhr()
        zeilen += rechne1d(laeufe, box, dx, dt, rauch)
        dauer[gname] = uhr() - t0
        print(f"  {gname}: {len(laeufe)} Laeufe, {dauer[gname]:.1f} s", flush=True)
    kenn = []
    for v2 in sorted({z["V2"] for z in zeilen}):
        for b in sorted({z["B"] for z in zeilen if z["V2"] == v2}):
            kenn.append(stufe_kennzahlen([z for z in zeilen if z["V2"] == v2 and z["B"] == b]))
    pl = plausibel(zeilen)
    text = [f"{name} ({stufe}, dx {dx}, dt {dt}). Start {start}, Ende {jetzt()}, {geraet_name()}"
            + (f" RAUCHTEST (T x {rauch}): Zahlen ungueltig" if rauch != 1.0 else "")]
    text.append("Dauer [s]: " + ", ".join(f"{k} {s:.1f}" for k, s in dauer.items()))
    if rauch != 1.0:
        text.append(f"Hochrechnung voller Aufruf (Entwicklung x {1 / rauch:.0f}): {sum(dauer.values()) / rauch:.0f} s")
    text += [zeile_text(z) for z in zeilen]
    for k in kenn:
        text.append(f"  Stufe V2 {k['V2']:.2f} B {k['B']:.0f} Pi {k['Pi']:.3f}: dT {k['dT']}, W {k['W']} {k['W_rel']}, "
                    f"streng gespalten {k['spalt_streng_rel']}, monoton im Fenster {k['monoton_im_fenster']}")
    text.append(f"Plausibilitaetsschranke: bestanden = {pl['bestanden']}" + "".join("\n    " + v for v in pl["verstoesse"]))
    ausgabe = {"test": name, "stufe": stufe, "start": start, "ende": jetzt(), "rauch": rauch, "dauer_s": dauer,
               "geraet": geraet_name(), "torch": torch.__version__, "argumente": vars(args),
               "boxen": {g: b for g, b, _ in gruppen}, "laeufe": zeilen, "stufen": kenn, "plausibilitaet": pl}
    schreiben(out, f"{name}_{stufe}", ausgabe, "\n".join(text))


def test_urteil(out, pfad_a, pfad_b):
    with open(pfad_a) as fh:
        h = json.load(fh)
    with open(pfad_b) as fh:
        g = json.load(fh)
    st = sorted([k for k in h["stufen"] if k["B"] == 1.0 and k["V2"] > 0.0], key=lambda k: k["Pi"])
    klein, gross = st[0], st[-1]
    u, scheitert = [], []
    v1 = klein["dT"] is not None and klein["dT"] >= 0.9 and klein["W"] == 0
    u.append(f"V1 (Pi {klein['Pi']:.3f}): dT {klein['dT']}, W {klein['W']} -> {'erfuellt' if v1 else 'verfehlt'}")
    v2 = (gross["dT"] is not None and gross["dT"] <= 0.8 and len(gross["spalt_streng_rel"]) >= 2
          and gross["monoton_im_fenster"])
    u.append(f"V2 (Pi {gross['Pi']:.3f}): dT {gross['dT']}, streng gespalten {gross['spalt_streng_rel']}, monoton "
             f"{gross['monoton_im_fenster']} -> {'erfuellt' if v2 else 'verfehlt'}")
    dts = [k["dT"] for k in st]
    verletzt = sum(1 for a, b in zip(dts[:-1], dts[1:]) if a is None or b is None or b > a + 0.05)
    u.append(f"V3 dT ueber Pi {[round(k['Pi'], 3) for k in st]}: {dts}; Verletzungen {verletzt}")
    pl_h = h["plausibilitaet"]
    v4 = not any("V4" in v for v in pl_h["verstoesse"])
    u.append(f"V4 (Energieschranke): {'erfuellt' if v4 else 'verletzt'}")
    if gross["dT"] is not None and gross["dT"] >= 0.9 and gross["W"] == 0:
        scheitert.append("bei Pi = 2,05 und B = 1 bleibt der Sprung voll")
    if klein["W"] > 0:
        scheitert.append("bei Pi = 0,10 tritt ein Spalt auf")
    if verletzt >= 2:
        scheitert.append("V3 an zwei oder mehr Stellen verletzt")
    b25 = [k for k in g["stufen"] if k["B"] == 25.0]
    v0 = [z for z in g["laeufe"] if z["V2"] == 0.0]
    gp_b25 = bool(b25) and b25[0]["dT"] is not None and b25[0]["dT"] >= 0.9 and b25[0]["W"] == 0
    gp_v0 = bool(v0) and all(z["klasse"] == "durch" and z["q_haupt"] >= 0.99 for z in v0)
    u.append(f"Gegenprobe B = 25: dT {b25[0]['dT'] if b25 else None}, W {b25[0]['W'] if b25 else None} -> "
             f"{'bestanden' if gp_b25 else 'VERLETZT'}")
    u.append(f"Gegenprobe V2 = 0: {len(v0)} Laeufe -> {'bestanden' if gp_v0 else 'VERLETZT'}")
    plaus = pl_h["bestanden"] and g["plausibilitaet"]["bestanden"]
    u.append("Scheitert-Regeln (unabhaengig von der Plausibilitaet gemeldet): " + ("; ".join(scheitert) or "keine"))
    if not plaus:
        nur_v4 = all("V4" in v for v in pl_h["verstoesse"] + g["plausibilitaet"]["verstoesse"])
        ausgang = ("Plausibilitaetsschranke nicht bestanden" + (" (nur V4, Energieschranke)" if nur_v4 else "")
                   + ": kein Ausgang; Verstoesse in den Berichten von haupt und gegen")
    elif scheitert:
        ausgang = "scheitert: " + "; ".join(scheitert)
    elif v1 and v2 and verletzt == 0 and v4 and gp_b25 and gp_v0:
        ausgang = "getroffen"
    else:
        ausgang = "nicht entscheidbar"
    text = [f"urteil G1-02 aus {pfad_a} und {pfad_b}. {jetzt()}"] + ["  " + x for x in u]
    text.append(f"Plausibilitaet haupt {pl_h['bestanden']}, gegen {g['plausibilitaet']['bestanden']}")
    text.append(f"Ausgang nach KARTE.md: {ausgang}")
    schreiben(out, f"urteil_{h['stufe']}", {"a": pfad_a, "b": pfad_b, "urteil": u, "scheitert": scheitert,
                                            "plausibel": plaus, "ausgang": ausgang}, "\n".join(text))


def test_l3(out, pfad_a, pfad_b):
    with open(pfad_a) as fh:
        a = json.load(fh)
    with open(pfad_b) as fh:
        b = json.load(fh)
    sl = lambda z: (round(z["V2"], 6), round(z["B"], 3), round(z["rel"], 4))
    bb = {sl(z): z for z in b["laeufe"]}
    anders, dq = [], []
    for z in a["laeufe"]:
        y = bb.get(sl(z))
        if y is None:
            continue
        dq.append(abs(z["q_durch"] - y["q_durch"]))
        if z["klasse"] != y["klasse"]:
            anders.append([z["V2"], z["B"], z["rel"], z["klasse"], y["klasse"]])
    aenderung = max(dq) if dq else 0.0
    st = sorted([k for k in a["stufen"] if k["B"] == 1.0 and k["V2"] > 0.0], key=lambda k: k["Pi"])
    effekt = None
    if len(st) >= 2 and st[0]["dT"] is not None and st[-1]["dT"] is not None:
        effekt = abs(st[0]["dT"] - st[-1]["dT"])
    eff_ok = True if effekt is None else effekt >= 5.0 * aenderung
    bestanden = not anders and aenderung <= 0.05 and eff_ok
    text = [f"L3 {pfad_a} gegen {pfad_b}: {len(dq)} Paare, Klassen verschieden {len(anders)}, max |dq_durch| "
            f"{aenderung:.4f}, Effekt |dT(Pi klein) - dT(Pi gross)| {effekt} (verlangt >= 5 x Aenderung: {eff_ok}). "
            f"L3 bestanden = {bestanden}"]
    text += [f"  verschieden: {x}" for x in anders]
    schreiben(out, f"l3_{a['test']}", {"a": pfad_a, "b": pfad_b, "anders": anders, "max_dq": aenderung,
                                       "effekt": effekt, "bestanden": bestanden}, "\n".join(text))


def zahlen(s):
    return tuple(float(t) for t in s.split(",") if t.strip())


def main():
    global DEV
    ap = argparse.ArgumentParser(description="G1-02: Q-Ball an der Stufe, Spaltfenster ab Pi ~ 1")
    ap.add_argument("test", choices=["papier", "haupt", "gegen", "urteil", "l3"])
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda")
    ap.add_argument("--out", default=None)
    ap.add_argument("--fein", action="store_true", help="dx und dt halbiert (L3)")
    ap.add_argument("--rauch", type=float, default=1.0, help="Formprobe: T mal Faktor (Zahlen dann ungueltig)")
    ap.add_argument("--w2", type=float, default=W2)
    ap.add_argument("--v2", default=V2_HAUPT, help="haupt: Stufenhoehen")
    ap.add_argument("--rel", default=REL, help="v/v_cl-Liste")
    ap.add_argument("--v2-gegen", type=float, default=0.20, help="gegen: Stufe der B-25-Gegenprobe und v-Quelle fuer V2 = 0")
    ap.add_argument("--b-haupt", type=float, default=BOX_B1["B"])
    ap.add_argument("--b-gegen", type=float, default=BOX_B25["B"])
    ap.add_argument("--x0-gegen", type=float, default=BOX_B25["x0"])
    ap.add_argument("--nur", default="b25,v0", help="gegen: Teilgruppen")
    ap.add_argument("--a", default=None)
    ap.add_argument("--b", default=None)
    args = ap.parse_args()
    if args.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("--geraet cuda, aber kein CUDA-Geraet sichtbar: Abbruch.")
        DEV = torch.device("cuda")
        gesamt = torch.cuda.get_device_properties(0).total_memory
        torch.cuda.set_per_process_memory_fraction(min(1.0, SPEICHER_GB * 1e9 / gesamt), 0)
    else:
        DEV = torch.device("cpu")
        torch.set_num_threads(1)
    out = args.out or os.path.join(os.path.dirname(os.path.abspath(__file__)), "ausgabe")
    rel = zahlen(args.rel)
    if args.test == "papier":
        test_papier(out, args.w2, zahlen(args.v2) + (args.v2_gegen,))
    elif args.test == "haupt":
        box = dict(BOX_B1, B=args.b_haupt)
        lf = laeufe_bauen(args.w2, zahlen(args.v2), rel)
        lauf_gruppe(out, "haupt", [("B1", box, lf)], args.fein, args.rauch, args)
    elif args.test == "gegen":
        nur = [n.strip() for n in args.nur.split(",") if n.strip()]
        gruppen = []
        if "b25" in nur:
            box = dict(BOX_B25, B=args.b_gegen, x0=args.x0_gegen)
            gruppen.append(("B25", box, laeufe_bauen(args.w2, (args.v2_gegen,), rel)))
        if "v0" in nur:
            gruppen.append(("V0", dict(BOX_B1), laeufe_bauen(args.w2, (0.0,), rel, v2_fuer_v=args.v2_gegen)))
        lauf_gruppe(out, "gegen", gruppen, args.fein, args.rauch, args)
    elif args.test == "urteil":
        if not (args.a and args.b):
            raise SystemExit("urteil braucht --a (haupt) und --b (gegen)")
        test_urteil(out, args.a, args.b)
    else:
        if not (args.a and args.b):
            raise SystemExit("l3 braucht --a und --b")
        test_l3(out, args.a, args.b)


if __name__ == "__main__":
    main()
