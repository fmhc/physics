#!/usr/bin/env python3
"""G1-07 (GEN-01): Tod ohne Mindestladung. Ruhender 1D-Ball (omega^2 = 0,80) unter gleichmaessigem Abfluss -gamma psi_t.

Kopie aus coordination/runden-v3/RUNDE-05/r5b/r5b.py; unveraendert uebernommen: profil_anker_x, anker_wgv, anker_q_e,
ball (ruhender Anker), dichte, ladung, energie_dichte, breite_s, Laplace ueber Flussdifferenzen, Velocity-Verlet mit
quadratischer Daempfungsschicht (sigma0 = 1) und gleichmaessiger Daempfung gamma, dx = 0,1, dt = 0,05 (--fein halbiert).
Das Original bleibt unveraendert.
Neu (KARTE.md): Box +-600 mit Schwamm ab 550 (Argumente), Abfluss je Lauf mit Stoppzeit, Messung im Fenster |x| < 100
und im Zentrum (S_c, Phase), Familienvergleich ueber eine Tabelle des Ankers, Todesladung Q_d (erster Zeitpunkt mit
|S_c/S_c,fam - 1| > 0,1), t90/t50/t10 aus q_rel wie auswertung_tod in RUNDE-07/r5f/r5f.py, Urteil nach der Karte,
Plausibilitaetsschranke als eigene Pruefung mit "bestanden", L3 grob gegen fein.

Unterbefehle:
  dauer   gamma = 2e-3, 1e-3, 5e-4 ohne Stopp (T = ln(Q0/0,05)/gamma + 500) und gamma = 0 (Gegenprobe, T = 2000)
  stopp   gamma = 1e-3 bis Q_erw = 0,8 Q_d(1e-3), Q_d aus --dauer-json (Regel vorab), danach 2000 ohne Abfluss
  urteil  --a dauer_<stufe>_ergebnis.json --b stopp_<stufe>_ergebnis.json: V1 bis V4, Scheitert-Regeln, Gegenprobe
  l3      --a dauer grob --b dauer fein: Q_d auf 5 %, p auf 0,05, Effekt >= 5 x Aenderung
Nicht enthalten: der 3D-Vergleich der Gegenprobe (siehe NACHTRAG.md).
Aufruf: python abfluss1d.py <unterbefehl> [--geraet cuda|cpu] [--fein] [--out ORDNER] [--rauch F] [Parameter]
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
C128 = torch.complex128
NAN = float("nan")

SPEICHER_GB = 1.5
SIGMA0 = 1.0
DX, DT, FEIN = 0.1, 0.05, 0.5
T_MESS = 0.5               # Phase im Zentrum: |omega| T_MESS <= 0,5 < pi
OM_HALB = 10               # omega aus der Phase ueber +-10 Messpunkte (+-5 Zeiteinheiten)

# Vorgaben der Karte G1-07
W2_START = 0.80
GAMMAS = "2e-3,1e-3,5e-4"
Q_ENDE, T_NACH = 0.05, 500.0
T_GEGEN = 2000.0
T_NACH_STOPP = 2000.0
STOPP_FAKTOR = 0.8
STOPP_GAMMA = 1e-3
BRUCH = 0.1
FENSTER = 100.0
BOX = {"L": 600.0, "x_schwamm": 550.0}
TOL_Q = 1e-4               # Toleranz fuer Q_tot <= Q_erw (Diskretisierung), vor jedem Lauf festgelegt


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    if DEV.type == "cuda":
        torch.cuda.synchronize()
    return time.perf_counter()


def geraet_name():
    return torch.cuda.get_device_name(0) if DEV.type == "cuda" else "cpu"


def sauber(o):
    """NaN und Unendlich als null, damit jq die Datei lesen kann."""
    if isinstance(o, float):
        return o if math.isfinite(o) else None
    if isinstance(o, dict):
        return {k: sauber(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [sauber(v) for v in o]
    return o


def schreiben(out, name, ausgabe, text):
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, name + "_ergebnis.json"), "w") as fh:
        json.dump(sauber(ausgabe), fh, indent=1, allow_nan=False)
    with open(os.path.join(out, name + "_bericht.txt"), "w") as fh:
        fh.write(text + "\n")
    print(text, flush=True)


def endlich(v):
    return v is not None and isinstance(v, float) and math.isfinite(v)


# ---------------------------------------------------------------- aus r5b.py (unveraendert)

def profil_anker_x(w2, x):
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    return torch.sqrt(2.0 * a0 / (1.0 + b0 * torch.cosh(2.0 * math.sqrt(a0) * x)))


def anker_wgv(w2):
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    integral = math.sqrt(2.0) * math.acosh(1.0 / b0)
    w = w2 * integral
    g = math.sqrt(a0) / 2.0 - b0 * b0 * integral / 4.0
    return w, g, w + g


def anker_q_e(w2):
    w, g, v = anker_wgv(w2)
    return 2.0 * w / math.sqrt(w2), w + g + v


def ball(x, w2, phase=0.0):
    psi = profil_anker_x(w2, x) * complex(math.cos(phase), math.sin(phase))
    return psi, (-1j * math.sqrt(w2)) * psi


def dichte(psi):
    return psi.real ** 2 + psi.imag ** 2


def ladung(psi, vel):
    return 2.0 * (psi * vel.conj()).imag


def energie_dichte(psi, vel, dx):
    s = dichte(psi)
    e = vel.real ** 2 + vel.imag ** 2 + s - s * s + 0.5 * s ** 3
    g = (psi[:, 1:] - psi[:, :-1]) / dx
    e[:, :-1] += g.real ** 2 + g.imag ** 2
    return e


def breite_s(x, s, maske):
    m = (s * maske).sum(1).clamp(min=1e-300)
    mitte = (x * s * maske).sum(1) / m
    return torch.sqrt(((x - mitte.unsqueeze(1)) ** 2 * s * maske).sum(1) / m)


# ---------------------------------------------------------------- Gitter, Familie, Zeitentwicklung

def gitter(dx, L):
    i0 = int(round(L / dx))
    return (torch.arange(2 * i0 + 1, dtype=F64, device=DEV) - i0) * dx, i0


def familie_tabelle(n=200001):
    """Anker-Familie ueber eps = 1 - omega^2 (logarithmisch): ln Q, S_c = 2 a0/(1 + b0), omega (CPU, float64)."""
    eps = torch.logspace(-9.0, math.log10(0.5 - 1e-9), n, dtype=F64)
    w2 = 1.0 - eps
    b0 = torch.sqrt(2.0 * w2 - 1.0)
    q = 2.0 * torch.sqrt(w2) * math.sqrt(2.0) * torch.acosh(1.0 / b0)
    return {"lnq": torch.log(q), "s_c": 2.0 * eps / (1.0 + b0), "omega": torch.sqrt(w2)}


def familie_bei(tab, q):
    """S_c und omega der Familie bei den Ladungen q (1D-Tensor, CPU), lineare Interpolation in ln Q."""
    lx = torch.log(q.clamp(min=1e-300))
    i = torch.searchsorted(tab["lnq"], lx).clamp(1, tab["lnq"].shape[0] - 1)
    x0, x1 = tab["lnq"][i - 1], tab["lnq"][i]
    w = ((lx - x0) / (x1 - x0)).clamp(0.0, 1.0)
    return (tab["s_c"][i - 1] + w * (tab["s_c"][i] - tab["s_c"][i - 1]),
            tab["omega"][i - 1] + w * (tab["omega"][i] - tab["omega"][i - 1]))


SPALTEN = ["Q_tot", "Q_in", "E_tot", "E_in", "S_c", "Re_psi_c", "Im_psi_c", "breite"]


def messen_bauen(x, dx, i0):
    innen = (x.abs() < FENSTER).to(F64)

    def messen(psi, vel):
        s = dichte(psi)
        rho = ladung(psi, vel)
        e = energie_dichte(psi, vel, dx)
        return torch.stack([rho.sum(1) * dx, (rho * innen).sum(1) * dx, e.sum(1) * dx, (e * innen).sum(1) * dx,
                            s[:, i0], psi[:, i0].real, psi[:, i0].imag, breite_s(x, s, innen)], dim=1)
    return messen


def entwickeln(psi, vel, x, dx, dt, t_end, messen, gamma, t_stop, L, x_schwamm):
    """Velocity-Verlet wie r5b.entwickeln; gamma (B,) wirkt je Lauf nur in Schritten mit Mitte vor t_stop (B,)."""
    sig0 = (SIGMA0 * ((x.abs() - x_schwamm).clamp(min=0.0) / (L - x_schwamm)) ** 2).unsqueeze(0)
    gam = gamma.unsqueeze(1)
    tst = t_stop.unsqueeze(1)

    def kraft(p):
        fluss = (p[:, 1:] - p[:, :-1]) / dx
        lap = torch.zeros_like(p)
        lap[:, 1:-1] = (fluss[:, 1:] - fluss[:, :-1]) / dx
        s = p.real ** 2 + p.imag ** 2
        return lap - (1.0 - 2.0 * s + 1.5 * s * s) * p

    n_schritte = int(round(t_end / dt))
    alle = max(1, int(round(T_MESS / dt)))
    reihe = [messen(psi, vel)]
    kr = kraft(psi)
    for j in range(1, n_schritte + 1):
        sig = sig0 + gam * (tst > (j - 0.5) * dt).to(F64)
        vel = vel + (0.5 * dt) * (kr - sig * vel)
        psi = psi + dt * vel
        kr = kraft(psi)
        vel = vel + (0.5 * dt) * (kr - sig * vel)
        if j % alle == 0:
            reihe.append(messen(psi, vel))
    daten = torch.stack(reihe)
    if not bool(torch.isfinite(daten).all()):
        raise RuntimeError("nicht endliche Messwerte: Lauf instabil")
    t = torch.arange(daten.shape[0], dtype=F64) * (alle * dt)
    return t, daten.cpu()


def rechnen(laeufe, fein, rauch):
    dx, dt, stufe = (DX * FEIN, DT * FEIN, "fein") if fein else (DX, DT, "grob")
    x, i0 = gitter(dx, BOX["L"])
    felder = [ball(x, W2_START) for _ in laeufe]
    psi = torch.stack([p for p, _ in felder]).contiguous()
    vel = torch.stack([v for _, v in felder]).contiguous()
    for a in (psi, vel):
        a[:, 0] = 0.0
        a[:, -1] = 0.0
    gamma = torch.tensor([lf["gamma"] for lf in laeufe], dtype=F64, device=DEV)
    t_stop = torch.tensor([lf["t_stop"] * rauch for lf in laeufe], dtype=F64, device=DEV)
    t_end = max(lf["T"] for lf in laeufe) * rauch
    t0 = uhr()
    t, d = entwickeln(psi, vel, x, dx, dt, t_end, messen_bauen(x, dx, i0), gamma, t_stop, BOX["L"], BOX["x_schwamm"])
    return t, d, uhr() - t0, dx, dt, stufe


# ---------------------------------------------------------------- Auswertung je Lauf

def erste_zeit(t, maske):
    idx = maske.nonzero().flatten()
    return float(t[idx[0]]) if idx.numel() else NAN


def auswerten(t, d, b, lf, tab, rauch):
    """Kenngroessen eines Laufs bis zu seinem eigenen T."""
    T = lf["T"] * rauch
    k_end = int(torch.searchsorted(t, torch.tensor([T + 1e-9], dtype=F64))[0]) - 1
    tt, dd = t[:k_end + 1], d[:k_end + 1, b]
    g, ts = lf["gamma"], lf["t_stop"] * rauch
    q0 = float(dd[0, 0])
    q_erw = q0 * torch.exp(-g * tt.clamp(max=ts))
    q_tot, q_in = dd[:, 0], dd[:, 1]
    q_rel = q_in / q_erw
    s_c = dd[:, 4]
    s_fam, om_fam = familie_bei(tab, q_erw)
    abw = (s_c / s_fam - 1.0).abs()
    t_bruch = erste_zeit(tt, abw > BRUCH) if g > 0.0 else NAN
    k_bruch = int(torch.searchsorted(tt, torch.tensor([t_bruch], dtype=F64))[0]) if endlich(t_bruch) else len(tt)
    q_d = float(q_erw[k_bruch]) if endlich(t_bruch) else NAN
    th = torch.atan2(dd[:, 6], dd[:, 5])
    dth = torch.remainder(th[1:] - th[:-1] + math.pi, 2.0 * math.pi) - math.pi
    th_u = torch.cat([th[:1], th[0] + torch.cumsum(dth, 0)])
    om = torch.full_like(th_u, NAN)
    h = OM_HALB
    if len(th_u) > 2 * h:
        om[h:-h] = -(th_u[2 * h:] - th_u[:-2 * h]) / (tt[2 * h:] - tt[:-2 * h])
    amp_ok = (dd[:, 5] ** 2 + dd[:, 6] ** 2) > 1e-12
    z = {**lf, "T_eff": float(tt[-1]), "t_stop_eff": ts, "Q0": q0, "Q_erw_ende": float(q_erw[-1]),
         "t_bruch": t_bruch, "Q_d": q_d, "S_c_0": float(s_c[0])}
    for key, s in (("t90", 0.9), ("t50", 0.5), ("t10", 0.1)):
        z[key] = erste_zeit(tt, q_rel < s)
    # V2: omega folgt der Familie, solange Q_erw > 2 Q_d (vor dem Bruch)
    vor = torch.isfinite(om) & (torch.arange(len(tt)) < k_bruch)
    folge = vor & (q_erw > 2.0 * q_d) if endlich(q_d) else vor
    z["om_abw_max_folge"] = float((om[folge] - om_fam[folge]).abs().max()) if bool(folge.any()) else NAN
    z["om_max_vor_bruch"] = float(om[vor].max()) if bool(vor.any()) else NAN
    spaet = torch.isfinite(om) & (tt >= tt[-1] - 100.0)
    z["om_ende"] = float(om[spaet].mean()) if bool(spaet.any()) else NAN
    if endlich(ts) and ts < tt[-1]:
        k_s = int(torch.searchsorted(tt, torch.tensor([ts], dtype=F64))[0])
        z["Q_erw_stopp"] = float(q_erw[min(k_s, len(tt) - 1)])
        z["q_rel_stopp_ende"] = float(q_in[-1]) / z["Q_erw_stopp"]
    # Gegenprobe gamma = 0
    if g == 0.0:
        ok = torch.isfinite(om)
        z["dQ_in_rel_max"] = float(((q_in - q_in[0]) / q0).abs().max())
        z["om_abw_0894_max"] = float((om[ok] - math.sqrt(W2_START)).abs().max()) if bool(ok.any()) else NAN
        z["S_c_rel_max"] = float((s_c / s_c[0] - 1.0).abs().max())
    # Plausibilitaet
    v = []
    if float((q_tot / q_erw - 1.0).max()) > TOL_Q:
        v.append(f"Q_tot > Q_erw (max rel {float((q_tot / q_erw - 1.0).max()):.2e})")
    vb = torch.arange(len(tt)) < k_bruch
    if bool(vb.any()) and float((q_tot[vb] / q_erw[vb] - 1.0).abs().max()) >= 1e-3:
        v.append(f"vor dem Bruch |Q_tot/Q_erw - 1| = {float((q_tot[vb] / q_erw[vb] - 1.0).abs().max()):.2e}")
    if float(q_rel.max()) > 1.02:
        v.append(f"q_rel max {float(q_rel.max()):.4f} > 1,02")
    omk = torch.isfinite(om) & amp_ok
    if bool(omk.any()) and float(om[omk].min()) <= 0.0:
        v.append(f"omega <= 0 (min {float(om[omk].min()):.4f})")
    if float((dd[:, 3] - dd[:, 2]).max()) > 1e-12 * max(1.0, float(dd[0, 2])):
        v.append("E_in > E_tot")
    z["plausibel"] = {"bestanden": not v, "verstoesse": v}
    z["reihe_duenn"] = {"t": tt[::200].tolist(), "q_rel": q_rel[::200].tolist(), "S_c": s_c[::200].tolist(),
                        "S_fam": s_fam[::200].tolist(), "omega": [None if not math.isfinite(o) else o
                                                               for o in om[::200].tolist()]}
    return z


def zeile_text(z):
    return (f"  gamma {z['gamma']:.1e} t_stop {z['t_stop_eff']:.0f} T {z['T_eff']:.0f} | Q0 {z['Q0']:.4f} | t_bruch "
            f"{z['t_bruch']:.1f} | Q_d {z['Q_d']:.4f} | t90 {z['t90']:.0f} t50 {z['t50']:.0f} t10 {z['t10']:.0f} | "
            f"om-Abw {z['om_abw_max_folge']:.2e} | om_max vor Bruch {z['om_max_vor_bruch']:.5f} | om Ende "
            f"{z['om_ende']:.5f} | plausibel {z['plausibel']['bestanden']}")


# ---------------------------------------------------------------- Unterbefehle

def t_dauer(q0, g):
    return math.log(q0 / Q_ENDE) / g + T_NACH


def test_dauer(out, fein, rauch, gammas, args):
    start = jetzt()
    q0 = anker_q_e(W2_START)[0]
    laeufe = [{"name": f"dauer {g:g}", "gamma": g, "t_stop": math.inf, "T": t_dauer(q0, g)} for g in gammas]
    if args.mit_gegen:
        laeufe.append({"name": "gegen gamma 0", "gamma": 0.0, "t_stop": math.inf, "T": T_GEGEN})
    t, d, sek, dx, dt, stufe = rechnen(laeufe, fein, rauch)
    tab = familie_tabelle()
    zeilen = [auswerten(t, d, b, lf, tab, rauch) for b, lf in enumerate(laeufe)]
    text = [f"dauer ({stufe}, dx {dx}, dt {dt}). Start {start}, Ende {jetzt()}, {geraet_name()}, {sek:.1f} s"
            + (f" RAUCHTEST (T x {rauch}): Zahlen ungueltig" if rauch != 1.0 else "")]
    if rauch != 1.0:
        text.append(f"Hochrechnung voller Aufruf: {sek / rauch:.0f} s")
    text += [zeile_text(z) for z in zeilen]
    pl = all(z["plausibel"]["bestanden"] for z in zeilen)
    text.append(f"Plausibilitaetsschranke: bestanden = {pl}" + "".join(
        f"\n    gamma {z['gamma']:.1e}: {v}" for z in zeilen for v in z["plausibel"]["verstoesse"]))
    ausgabe = {"test": "dauer", "stufe": stufe, "start": start, "ende": jetzt(), "rauch": rauch, "sek": sek,
               "geraet": geraet_name(), "torch": torch.__version__, "argumente": vars(args), "box": BOX, "dx": dx,
               "dt": dt, "laeufe": zeilen, "plausibilitaet": {"bestanden": pl}}
    schreiben(out, f"dauer_{stufe}", ausgabe, "\n".join(text))


def test_stopp(out, fein, rauch, args):
    start = jetzt()
    if args.qd is not None:
        q_d, quelle = args.qd, "--qd (nur Formprobe)"
    else:
        with open(args.dauer_json) as fh:
            dj = json.load(fh)
        treffer = [z for z in dj["laeufe"] if abs(z["gamma"] - STOPP_GAMMA) < 1e-12]
        if not treffer or not endlich(treffer[0]["Q_d"]):
            raise SystemExit("kein Q_d fuer gamma = 1e-3 in --dauer-json: Stopp-Lauf nicht festgelegt")
        q_d, quelle = treffer[0]["Q_d"], args.dauer_json
    q0 = anker_q_e(W2_START)[0]
    t_stop = math.log(q0 / (STOPP_FAKTOR * q_d)) / STOPP_GAMMA
    laeufe = [{"name": "stopp 1e-3", "gamma": STOPP_GAMMA, "t_stop": t_stop, "T": t_stop + T_NACH_STOPP}]
    t, d, sek, dx, dt, stufe = rechnen(laeufe, fein, rauch)
    z = auswerten(t, d, 0, laeufe[0], familie_tabelle(), rauch)
    z["Q_d_quelle"], z["Q_d_vorgabe"] = quelle, q_d
    text = [f"stopp ({stufe}, dx {dx}, dt {dt}). Start {start}, Ende {jetzt()}, {geraet_name()}, {sek:.1f} s; "
            f"Q_d(1e-3) = {q_d:.5f} aus {quelle}, t_stop = {t_stop:.1f}"
            + (f" RAUCHTEST (T x {rauch}): Zahlen ungueltig" if rauch != 1.0 else "")]
    if rauch != 1.0:
        text.append(f"Hochrechnung voller Aufruf: {sek / rauch:.0f} s")
    text.append(zeile_text(z))
    text.append(f"  q_rel(t_stop + 2000) bezogen auf Q_erw(t_stop): {z.get('q_rel_stopp_ende')}, omega am Ende "
                f"{z['om_ende']}")
    text.append(f"Plausibilitaetsschranke: bestanden = {z['plausibel']['bestanden']} {z['plausibel']['verstoesse']}")
    ausgabe = {"test": "stopp", "stufe": stufe, "start": start, "ende": jetzt(), "rauch": rauch, "sek": sek,
               "geraet": geraet_name(), "argumente": vars(args), "laeufe": [z],
               "plausibilitaet": {"bestanden": z["plausibel"]["bestanden"]}}
    schreiben(out, f"stopp_{stufe}", ausgabe, "\n".join(text))


def fit_p(zeilen):
    pts = [(math.log(z["gamma"]), math.log(z["Q_d"])) for z in zeilen if z["gamma"] > 0.0 and endlich(z["Q_d"])]
    if len(pts) < 3:
        return NAN
    mx = sum(p[0] for p in pts) / len(pts)
    my = sum(p[1] for p in pts) / len(pts)
    return sum((p[0] - mx) * (p[1] - my) for p in pts) / sum((p[0] - mx) ** 2 for p in pts)


def test_urteil(out, pfad_a, pfad_b):
    with open(pfad_a) as fh:
        a = json.load(fh)
    with open(pfad_b) as fh:
        b = json.load(fh)
    zz = {round(z["gamma"], 12): z for z in a["laeufe"]}
    p = fit_p(a["laeufe"])
    qd = {g: zz[g]["Q_d"] if g in zz else NAN for g in (2e-3, 1e-3, 5e-4)}
    u, scheitert = [], []
    v1 = endlich(p) and 0.38 <= p <= 0.62 and endlich(qd[1e-3]) and 0.08 <= qd[1e-3] <= 0.40
    u.append(f"V1: p = {p:.3f}, Q_d(1e-3) = {qd[1e-3]} -> {'erfuellt' if v1 else 'verfehlt'}")
    dauer = [z for z in a["laeufe"] if z["gamma"] > 0.0]
    v2 = all(endlich(z["om_abw_max_folge"]) and z["om_abw_max_folge"] < 2e-3 and endlich(z["om_max_vor_bruch"])
             and z["om_max_vor_bruch"] < 1.0 for z in dauer)
    u.append(f"V2: omega-Abweichung {[z['om_abw_max_folge'] for z in dauer]}, omega max vor Bruch "
             f"{[z['om_max_vor_bruch'] for z in dauer]} -> {'erfuellt' if v2 else 'verfehlt'}")
    r = qd[5e-4] / qd[2e-3] if endlich(qd[5e-4]) and endlich(qd[2e-3]) else NAN
    v3 = endlich(r) and 0.38 <= r <= 0.62
    u.append(f"V3: Q_d(5e-4)/Q_d(2e-3) = {r} -> {'erfuellt' if v3 else 'verfehlt'}")
    s = b["laeufe"][0]
    qs = s.get("q_rel_stopp_ende", NAN)
    v4 = endlich(qs) and qs >= 0.5 and endlich(s["om_ende"]) and s["om_ende"] < 1.0
    u.append(f"V4: q_rel(t_stop + 2000) = {qs}, omega Ende {s['om_ende']} -> {'erfuellt' if v4 else 'verfehlt'}")
    if endlich(p) and (p < 0.3 or p > 0.7):
        scheitert.append(f"p = {p:.3f} ausserhalb [0,3; 0,7]")
    if any(endlich(z["om_max_vor_bruch"]) and z["om_max_vor_bruch"] > 1.0 for z in dauer):
        scheitert.append("omega > 1 vor dem Bruch")
    if endlich(qs) and qs < 0.1:
        scheitert.append("gestoppter Rest zerlaeuft (q_rel < 0,1)")
    g0 = [z for z in a["laeufe"] if z["gamma"] == 0.0]
    gp = (bool(g0) and all(endlich(g0[0][k]) for k in ("dQ_in_rel_max", "om_abw_0894_max", "S_c_rel_max"))
          and g0[0]["dQ_in_rel_max"] < 1e-3 and g0[0]["om_abw_0894_max"] < 1e-3 and g0[0]["S_c_rel_max"] < 0.01)
    u.append("Gegenprobe gamma = 0: " + (f"dQ_in {g0[0]['dQ_in_rel_max']}, omega-Abw {g0[0]['om_abw_0894_max']},"
             f" S_c {g0[0]['S_c_rel_max']}" if g0 else "fehlt") + f" -> {'bestanden' if gp else 'VERLETZT'}")
    u.append("Gegenprobe 3D-Vergleich: nicht in diesem Code (NACHTRAG.md)")
    plaus = a["plausibilitaet"]["bestanden"] and b["plausibilitaet"]["bestanden"]
    if not plaus:
        ausgang = "Plausibilitaetsschranke nicht bestanden: kein Ausgang"
    elif scheitert:
        ausgang = "scheitert: " + "; ".join(scheitert)
    elif v1 and v2 and v3 and v4 and gp:
        ausgang = "getroffen (1D; 3D-Gegenprobe offen)"
    else:
        ausgang = "nicht entscheidbar"
    text = [f"urteil G1-07 aus {pfad_a} und {pfad_b}. {jetzt()}"] + ["  " + x for x in u]
    text.append(f"Ausgang nach KARTE.md: {ausgang}")
    schreiben(out, f"urteil_{a['stufe']}", {"a": pfad_a, "b": pfad_b, "p": p, "Q_d": {str(k): v for k, v in qd.items()},
                                            "urteil": u, "scheitert": scheitert, "plausibel": plaus,
                                            "ausgang": ausgang}, "\n".join(text))


def test_l3(out, pfad_a, pfad_b):
    with open(pfad_a) as fh:
        a = json.load(fh)
    with open(pfad_b) as fh:
        b = json.load(fh)
    qa = {round(z["gamma"], 12): z["Q_d"] for z in a["laeufe"] if z["gamma"] > 0.0}
    qb = {round(z["gamma"], 12): z["Q_d"] for z in b["laeufe"] if z["gamma"] > 0.0}
    rel = {g: abs(qb[g] / qa[g] - 1.0) for g in qa if g in qb and endlich(qa[g]) and endlich(qb[g])}
    pa, pb = fit_p(a["laeufe"]), fit_p(b["laeufe"])
    aend = max((abs(math.log(qb[g] / qa[g])) for g in rel), default=NAN)
    eff = (abs(math.log(qa[5e-4] / qa[2e-3])) if all(g in qa and endlich(qa[g]) for g in (5e-4, 2e-3)) else NAN)
    ok = (len(rel) == len(qa) and all(r <= 0.05 for r in rel.values()) and endlich(pa) and endlich(pb)
          and abs(pa - pb) <= 0.05 and endlich(eff) and endlich(aend) and eff >= 5.0 * aend)
    text = [f"L3 {pfad_a} gegen {pfad_b}: Q_d rel. Abweichung {rel}, p {pa} gegen {pb}, Effekt |ln Q_d(5e-4)/Q_d(2e-3)| "
            f"{eff}, Aenderung max |ln Q_d fein/grob| {aend}. L3 bestanden = {ok} (verlangt: Q_d auf 5 %, p auf 0,05, "
            "Effekt >= 5 x Aenderung)"]
    schreiben(out, "l3_dauer", {"a": pfad_a, "b": pfad_b, "rel": {str(k): v for k, v in rel.items()}, "p_a": pa,
                                "p_b": pb, "effekt": eff, "aenderung": aend, "bestanden": ok}, "\n".join(text))


def main():
    global DEV
    ap = argparse.ArgumentParser(description="G1-07: 1D-Ball unter gleichmaessigem Abfluss, Todesladung Q_d(gamma)")
    ap.add_argument("test", choices=["dauer", "stopp", "urteil", "l3"])
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda")
    ap.add_argument("--out", default=None)
    ap.add_argument("--fein", action="store_true", help="dx und dt halbiert (L3)")
    ap.add_argument("--rauch", type=float, default=1.0, help="Formprobe: alle Zeiten mal Faktor (Zahlen ungueltig)")
    ap.add_argument("--gammas", default=GAMMAS, help="dauer: Liste der Abflussraten")
    ap.add_argument("--ohne-gegen", dest="mit_gegen", action="store_false", help="dauer: ohne den Lauf gamma = 0")
    ap.add_argument("--L", type=float, default=BOX["L"])
    ap.add_argument("--x-schwamm", type=float, default=BOX["x_schwamm"])
    ap.add_argument("--dauer-json", default=None, help="stopp: Ergebnis von dauer derselben Stufe (Q_d bei 1e-3)")
    ap.add_argument("--qd", type=float, default=None, help="stopp: Q_d von Hand, nur fuer die Formprobe")
    ap.add_argument("--a", default=None)
    ap.add_argument("--b", default=None)
    args = ap.parse_args()
    BOX["L"], BOX["x_schwamm"] = args.L, args.x_schwamm
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
    if args.test == "dauer":
        test_dauer(out, args.fein, args.rauch, [float(g) for g in args.gammas.split(",") if g.strip()], args)
    elif args.test == "stopp":
        if args.dauer_json is None and args.qd is None:
            raise SystemExit("stopp braucht --dauer-json (oder --qd fuer die Formprobe)")
        test_stopp(out, args.fein, args.rauch, args)
    elif args.test == "urteil":
        if not (args.a and args.b):
            raise SystemExit("urteil braucht --a (dauer) und --b (stopp)")
        test_urteil(out, args.a, args.b)
    else:
        if not (args.a and args.b):
            raise SystemExit("l3 braucht --a und --b")
        test_l3(out, args.a, args.b)


if __name__ == "__main__":
    main()
