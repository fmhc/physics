#!/usr/bin/env python3
"""Runde 6 (v3): Zerspritzt ein Q-Ball an einer Potentialstufe wie ein Tropfen? Test mit der Weber-Zahl.

Explorativ. Ohne Testlauf abgegeben (Laptop: Interpreterverbot laut CLAUDE.md); Plan, Aufrufe, Vorhersagen und Latten
stehen in PLAN.md daneben.

Modell wie RUNDE-02/tests1d/tests1d.py (1D) und RUNDE-03/tests2d-r3/tests2d_r3.py (2D):
    L = |psi_t|^2 - |grad psi|^2 - U(S) - V(x) S,  U = S - S^2 + S^3/2,  S = |psi|^2,
    psi_tt = Lap psi - (U'(S) + V(x)) psi,  Stufe V(x) = V2 (1 + tanh(x/B))/2 mit B = 1 (wie Runde 3).
    Ladungsdichte rho = 2 Im(psi conj psi_t), Energiedichte |psi_t|^2 + |grad psi|^2 + U + V S.
1D: geschlossener Anker f^2 = 2 a0/(1 + b0 cosh(2 sqrt(a0) x)) (RUNDE-02: stimmte mit dem Schiessen auf 1,5e-10);
    finite Differenzen, Velocity-Verlet, Dirichlet-Rand, Daempfungsschicht wie tests1d.py.
2D: Profil, Gitter, Ball und Massenformel aus tests2d_r3.py (unveraenderte Kopie im selben Ordner, per import);
    spektraler Laplace, Velocity-Verlet, Randschicht wie dort.
Weber-Zahl (Groessen vorab aus dem Profil, wie im Tropfentest):
    rho_W = 2 omega^2 S_c (Enthalpiedichte), 1D: D = N/S_c, sigma = G (E - omega Q = 2 sigma);
    2D: D = 2 R_Q, R_Q = sqrt(N/(pi S_c)), sigma = G/(pi R_Q).  We_n = rho_W v_n^2 D / sigma.

Unterbefehle:
  papier    1D-Profilgroessen, Weber-Faktor, klassische Stufenschwelle, Energieschranken fuer Spaltung (Sekunden)
  karte1d   1D-Karte omega^2 {0,6 0,7 0,8} x V2 {-0,04 -0,02 -0,01 0 +0,01 +0,02} x v {0,05 ... 0,40}
  feinv1d   1D, abstossende Stufen: 9 Geschwindigkeiten um die klassische Schwelle v_cl je (omega^2, V2)
  winkel2d  2D, omega^2 = 0,7, V2 = -0,02, v = 0,2: Winkel 0, 20, 25, 30, 35, 40, 60 Grad, Kontrolle V2 = 0 bei 0 und 20
  l3        Vergleich zweier Ergebnisdateien (grob gegen fein) aus karte1d oder feinv1d, ohne Rechnung
  rauch     karte1d, feinv1d, winkel2d mit Laufzeit x 0,05 (nur Durchlauf und Hochrechnung; Zahlen ungueltig)

Aufruf: python weber.py <unterbefehl> [--geraet cuda|cpu] [--out ORDNER] [--fein] [--stufe grob|fein|beide]
                        [--karte JSON] [--a JSON --b JSON] [--nur karte1d,feinv1d,winkel2d]
"""
import argparse
import datetime
import json
import math
import os
import sys
import time

import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tests2d_r3 as r3  # noqa: E402  (unveraenderte Kopie aus RUNDE-03/tests2d-r3/)

DEV = torch.device("cpu")
F64 = torch.float64
C128 = torch.complex128

# ---- Feste Parameter (vor dem Lauf in PLAN.md festgehalten) ----
SPEICHER_GB = 1.5          # Deckel fuer den Torch-Speicher auf der GPU
RAUCH_FAKTOR = 0.05
T_MESS = 1.0
B_STUFE = 1.0              # Stufenbreite wie Runde 3
Q_FRAG_MIN = 0.05          # Fragment zaehlt ab 5 % der Anfangsladung
ZERFALL_GRENZE = 0.5       # H: Zerfall, wenn das Hauptfragment weniger als 50 % traegt

# 1D (Numerik wie tests1d.py)
DX1, DT1, FEIN = 0.1, 0.05, 0.5
L1 = 200.0                 # Box [-L1, L1], Dirichlet
X_SCHWAMM1 = 160.0         # Daempfung fuer |x| > 160, 40 breit, sigma0 = 1 wie tests1d.py
SIGMA0 = 1.0
X0_1D = 20.0               # Startabstand des Ballzentrums vor der Stufe
X_AUS = 25.0               # Weg hinter der Stufe bis zur Auswertung
T_ZUSATZ = 60.0
X_S1 = 8.0                 # |x| <= X_S1 zaehlt als "an der Stufe"
S_REL_FRAG = 0.01          # Fragmentgebiet: S > 0,01 S_c
W2_1D = (0.6, 0.7, 0.8)
V2_1D = (-0.04, -0.02, -0.01, 0.0, 0.01, 0.02)
V_1D = (0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40)
FEINV_V2 = (0.01, 0.02)
FEINV_REL = (-0.2, -0.1, -0.05, -0.02, 0.0, 0.02, 0.05, 0.1, 0.2)
FEINV_T_ZUSATZ = 200.0

# 2D (Aufbau wie tests2d_r3.py, Test brechung)
W2_2D, V_2D = 0.70, 0.2
L_2D, T_2D, X0_2D = 42.0, 280.0, -16.0
X_EVAL_2D = 12.0           # Auswertung, wenn der (vorhergesagte) durchgelassene Ball bei x = +12 steht
X_S2 = 6.0                 # |x| <= X_S2 zaehlt als "an der Stufe"
FAMILIE_2D = tuple(round(0.686 + 0.002 * j, 6) for j in range(15))   # 0,686 ... 0,714, enthaelt 0,70
LAEUFE_2D = (("w00", -0.02, 0.0), ("w20", -0.02, 20.0), ("w25", -0.02, 25.0), ("w30", -0.02, 30.0),
             ("w35", -0.02, 35.0), ("w40", -0.02, 40.0), ("w60", -0.02, 60.0),
             ("ohne00", 0.0, 0.0), ("ohne20", 0.0, 20.0))
STUFEN_2D = (("grob", 0.3, 0.05), ("fein", 0.15, 0.025))


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    if DEV.type == "cuda":
        torch.cuda.synchronize()
    return time.perf_counter()


def geraet_name():
    return torch.cuda.get_device_name(0) if DEV.type == "cuda" else "cpu"


def schreiben(out, name, ausgabe, zeitreihen, text):
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, name + "_ergebnis.json"), "w") as fh:
        json.dump(ausgabe, fh, indent=1)
    if zeitreihen is not None:
        torch.save(zeitreihen, os.path.join(out, name + "_zeitreihen.pt"))
    with open(os.path.join(out, name + "_bericht.txt"), "w") as fh:
        fh.write(text + "\n")
    print(text, flush=True)


# ---------------------------------------------------------------- 1D: Anker, Medium, Schranken (reine Formeln)

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
    """1D-Ball der Ladung q im Medium V2 (ruhend): Profil der Vakuumfamilie bei w = omega_med^2 - V2,
    q = 2 omega_med N(w), E = omega_med q + 2 G(w). Einschachteln in w (Q faellt mit w)."""
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
    """Kleinste Geschwindigkeit mit gamma m1 >= m_ziel (0, wenn schon in Ruhe erlaubt)."""
    return 0.0 if m_ziel <= m1 else math.sqrt(1.0 - (m1 / m_ziel) ** 2)


def schranken1d(w2, v2):
    """Klassische Stufenschwelle und Energieschranken fuer Spaltung in zwei gleiche Baelle (Fragmente ruhend;
    der Impuls ist an der Stufe nicht erhalten). Notwendige, keine hinreichenden Bedingungen."""
    a = anker(w2)
    m1, q = a["E"], a["Q"]
    m2 = masse_medium(q, v2)["M"]
    halb_vak = masse_medium(0.5 * q, 0.0)["M"]
    halb_med = masse_medium(0.5 * q, v2)["M"]
    aus = {"w2": w2, "V2": v2, "M1": m1, "M2": m2, "Phi": abs(v2) * a["N"] / a["G"],
           "V2_zu_bindung": abs(v2) / (1.0 - a["omega"]),
           "v_cl": v_aus_masse(m1, m2) if m2 > m1 else None,
           "dE_spaltung_vakuum": 2.0 * halb_vak - m1,
           "v_E_vakuum": v_aus_masse(m1, 2.0 * halb_vak),
           "v_E_durch_und_zurueck": v_aus_masse(m1, halb_vak + halb_med),
           "v_E_beide_durch": v_aus_masse(m1, 2.0 * halb_med)}
    for k in ("v_E_vakuum", "v_E_durch_und_zurueck", "v_E_beide_durch"):
        aus["We" + k[1:]] = a["we_faktor"] * aus[k] ** 2
    if aus["v_cl"] is not None:
        aus["We_cl"] = a["we_faktor"] * aus["v_cl"] ** 2
    return aus


def klassisch1d(w2, v2, v):
    """Teilchenbild: durch, wenn gamma M1 > M2; dann v_aus aus gamma2 M2 = gamma1 M1; sonst Reflexion mit v."""
    a = anker(w2)
    m1 = a["E"]
    m2 = masse_medium(a["Q"], v2)["M"] if v2 != 0.0 else m1
    gam1 = 1.0 / math.sqrt(1.0 - v * v)
    if gam1 * m1 > m2:
        gam2 = gam1 * m1 / m2
        return "durch", math.sqrt(1.0 - 1.0 / (gam2 * gam2))
    return "reflektiert", v


# ---------------------------------------------------------------- 1D: Gitter, Ball, Zeitentwicklung

def gitter1d(dx):
    i0 = int(round(L1 / dx))
    return (torch.arange(2 * i0 + 1, dtype=F64, device=DEV) - i0) * dx


def ball1d(a, x, xc, v):
    """Lorentz-geboosteter Anker: psi = f(xi) exp(i omega gamma v (x - xc)), xi = gamma (x - xc),
    psi_t = (-gamma v f'(xi) - i omega gamma f(xi)) exp(...), f' = -f sqrt(a0) b0 sinh(2 sqrt(a0) xi)/(1 + b0 cosh)."""
    gam = 1.0 / math.sqrt(1.0 - v * v)
    xi = gam * (x - xc)
    k = math.sqrt(a["a0"])
    arg = (2.0 * k * xi).clamp(-600.0, 600.0)
    nenner = 1.0 + a["b0"] * torch.cosh(arg)
    f = torch.sqrt(2.0 * a["a0"] / nenner)
    fp = -f * k * a["b0"] * torch.sinh(arg) / nenner
    ph = torch.exp(1j * (a["omega"] * gam * v * (x - xc)))
    return f * ph, (-gam * v * fp - 1j * a["omega"] * gam * f) * ph


def entwickeln1d(psi, vel, V, x, dx, dt, t_end, messen):
    """Velocity-Verlet wie tests1d.py (Stapel B x N), mit Stufe V (B x N)."""
    sigma = SIGMA0 * ((x.abs() - X_SCHWAMM1).clamp(min=0.0) / (L1 - X_SCHWAMM1)) ** 2

    def kraft(p):
        fluss = (p[:, 1:] - p[:, :-1]) / dx
        lap = torch.zeros_like(p)
        lap[:, 1:-1] = (fluss[:, 1:] - fluss[:, :-1]) / dx
        s = p.real ** 2 + p.imag ** 2
        return lap - (1.0 - 2.0 * s + 1.5 * s * s + V) * p

    n_schritte = int(round(t_end / dt))
    alle = max(1, int(round(T_MESS / dt)))
    reihe = [messen(psi, vel)]
    kr = kraft(psi)
    for n in range(1, n_schritte + 1):
        vel = vel + (0.5 * dt) * (kr - sigma * vel)
        psi = psi + dt * vel
        kr = kraft(psi)
        vel = vel + (0.5 * dt) * (kr - sigma * vel)
        if n % alle == 0:
            reihe.append(messen(psi, vel))
    daten = torch.stack(reihe)                   # (M, B, K)
    if not bool(torch.isfinite(daten).all()):
        raise RuntimeError("nicht endliche Messwerte: Lauf instabil")
    t = torch.arange(daten.shape[0], dtype=F64, device=DEV) * (alle * dt)
    return t, daten, psi, vel


SPALTEN1D = ["Q_links", "Q_mitte", "Q_rechts", "Q_box", "E_box", "Smax_links", "Smax_rechts", "Smax_mitte",
             "QX_links", "QX_rechts"]


def messen1d_bauen(x, dx, V):
    links = (x < -X_S1).to(F64)
    mitte = (x.abs() <= X_S1).to(F64)
    rechts = (x > X_S1).to(F64)

    def messen(psi, vel):
        s = psi.real ** 2 + psi.imag ** 2
        rho = 2.0 * (psi * vel.conj()).imag
        gx = torch.zeros_like(psi)
        gx[:, 1:-1] = (psi[:, 2:] - psi[:, :-2]) / (2.0 * dx)
        e = vel.real ** 2 + vel.imag ** 2 + gx.real ** 2 + gx.imag ** 2 + s - s * s + 0.5 * s ** 3 + V * s
        return torch.stack([(rho * links).sum(1) * dx, (rho * mitte).sum(1) * dx, (rho * rechts).sum(1) * dx,
                            rho.sum(1) * dx, e.sum(1) * dx, (s * links).amax(1), (s * rechts).amax(1),
                            (s * mitte).amax(1), (rho * links * x).sum(1) * dx, (rho * rechts * x).sum(1) * dx],
                           dim=1)
    return messen


def fragmente1d(s, rho, x, dx, s_thr, q0):
    """Zusammenhaengende Gebiete mit S > s_thr; Ladung je Gebiet (relativ zu q0), Schwerpunkt, S_max, Breite."""
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
    """Ausgang aus der Fragmentliste (Ladungen relativ) und der Restladung an der Stufe."""
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


def t_lauf1d(v):
    return (X0_1D + X_AUS) / v + T_ZUSATZ


def rechne1d(laeufe, dx, dt, t_end):
    """Ein Stapel mit gemeinsamer Laufzeit; Ballzentrum startet bei -X0_1D, Stufe bei x = 0."""
    x = gitter1d(dx)
    psis, vels, vs = [], [], []
    for lf in laeufe:
        p, pv = ball1d(anker(lf["w2"]), x, -X0_1D, lf["v"])
        psis.append(p)
        vels.append(pv)
        vs.append(lf["V2"] * 0.5 * (1.0 + torch.tanh(x / B_STUFE)))
    psi = torch.stack(psis).contiguous()
    vel = torch.stack(vels).contiguous()
    V = torch.stack(vs).contiguous()
    for a in (psi, vel):
        a[:, 0] = 0.0
        a[:, -1] = 0.0
    t, daten, psi, vel = entwickeln1d(psi, vel, V, x, dx, dt, t_end, messen1d_bauen(x, dx, V))
    s_end = (psi.real ** 2 + psi.imag ** 2).cpu()
    rho_end = (2.0 * (psi * vel.conj()).imag).cpu()
    xc = x.cpu()
    d = daten.cpu()
    tc = t.cpu()
    zeilen = []
    k20 = min(20, d.shape[0] - 1)
    for b, lf in enumerate(laeufe):
        a = anker(lf["w2"])
        q0, e0 = d[0, b, 3].item(), d[0, b, 4].item()
        fr = fragmente1d(s_end[b], rho_end[b], xc, dx, S_REL_FRAG * a["S_c"], q0)
        kl = klassifizieren(fr, d[-1, b, 1].item() / q0, X_S1)
        z = {"w2": lf["w2"], "V2": lf["V2"], "v": lf["v"], "We": a["we_faktor"] * lf["v"] ** 2, "dx": dx, "dt": dt,
             "t_end": tc[-1].item(), **kl, "fragmente": fr[:6], "Q0": q0, "E0": e0,
             "q_links_ende": d[-1, b, 0].item() / q0, "q_mitte_ende": d[-1, b, 1].item() / q0,
             "q_rechts_ende": d[-1, b, 2].item() / q0, "q_box_ende": d[-1, b, 3].item() / q0,
             "E_drift_max": ((d[:, b, 4] / e0 - 1.0).abs().max()).item()}
        for seite, iq, ix in (("durch", 2, 9), ("zurueck", 0, 8)):
            qa, qb = d[-1 - k20, b, iq].item(), d[-1, b, iq].item()
            if k20 > 0 and qa >= Q_FRAG_MIN * q0 and qb >= Q_FRAG_MIN * q0:
                xa, xb = d[-1 - k20, b, ix].item() / qa, d[-1, b, ix].item() / qb
                z["v_" + seite] = (xb - xa) / (tc[-1].item() - tc[-1 - k20].item())
        z["vorhersage_teilchen"], z["v_aus_teilchen"] = klassisch1d(lf["w2"], lf["V2"], lf["v"])
        zeilen.append(z)
    return zeilen, {"t": tc, "daten": d, "S_ende": s_end, "rho_ende": rho_end, "spalten": SPALTEN1D,
                    "laeufe": [dict(lf) for lf in laeufe]}


def stufe1d(fein):
    return (DX1 * FEIN, DT1 * FEIN, "fein") if fein else (DX1, DT1, "grob")


def zeile1d_text(z):
    frs = ", ".join(f"{f['q']:.3f}@{f['x']:.1f}" for f in z["fragmente"][:4])
    return (f"  {z['w2']:.2f} {z['V2']:+.2f} {z['v']:.4f} | We {z['We']:.3f} | {z['klasse']:<12} | "
            f"{'ZERFALL' if z['zerfall'] else '-':<7} | q_h {z['q_haupt']:.3f} | durch {z['q_durch']:.3f} | "
            f"zurueck {z['q_zurueck']:.3f} | frei {z['q_frei']:.3f} | n {z['n_frag']} | Teilchenbild "
            f"{z['vorhersage_teilchen']} | E-Drift {z['E_drift_max']:.1e} | Fragmente {frs}")


# ---------------------------------------------------------------- papier

def test_papier(out):
    start = jetzt()
    profile = [anker(w2) for w2 in W2_1D]
    schranken = [schranken1d(w2, v2) for w2 in W2_1D for v2 in V2_1D]
    text = [f"Papier (1D, nur Formeln). Start {start}"]
    text.append("omega2 | N | G=sigma | Q | E | S_c | D=N/S_c | rho_W | We-Faktor (We = Faktor v^2)")
    for a in profile:
        text.append(f"  {a['w2']:.2f} | {a['N']:.5f} | {a['G']:.5f} | {a['Q']:.5f} | {a['E']:.5f} | {a['S_c']:.5f} | "
                    f"{a['D']:.4f} | {a['rho_W']:.5f} | {a['we_faktor']:.4f}")
    text.append("omega2 V2 | M1 | M2 | Phi=|V2|N/G | v_cl (We_cl) | dE_Spaltung | v_E vakuum (We) | "
                "v_E durch+zurueck (We) | v_E beide durch (We)")
    for s in schranken:
        vcl = f"{s['v_cl']:.4f} ({s['We_cl']:.3f})" if s["v_cl"] is not None else "-"
        text.append(f"  {s['w2']:.2f} {s['V2']:+.2f} | {s['M1']:.5f} | {s['M2']:.5f} | {s['Phi']:.3f} | {vcl} | "
                    f"{s['dE_spaltung_vakuum']:.4f} | {s['v_E_vakuum']:.4f} ({s['We_E_vakuum']:.3f}) | "
                    f"{s['v_E_durch_und_zurueck']:.4f} ({s['We_E_durch_und_zurueck']:.3f}) | "
                    f"{s['v_E_beide_durch']:.4f} ({s['We_E_beide_durch']:.3f})")
    ausgabe = {"test": "papier", "start": start, "ende": jetzt(), "profile": profile, "schranken": schranken}
    schreiben(out, "papier", ausgabe, None, "\n".join(text))


# ---------------------------------------------------------------- karte1d

def schwellen1d(zeilen):
    gruppen = {}
    for z in zeilen:
        gruppen.setdefault((z["w2"], z["V2"]), []).append(z)
    aus = []
    for (w2, v2), zz in sorted(gruppen.items()):
        zz = sorted(zz, key=lambda z: z["v"])
        wechsel = [{"v_a": a["v"], "v_b": b["v"], "von": a["klasse"], "nach": b["klasse"]}
                   for a, b in zip(zz[:-1], zz[1:]) if a["klasse"] != b["klasse"]]
        zf = [z["zerfall"] for z in zz]
        e = {"w2": w2, "V2": v2, "klassen": [[z["v"], z["klasse"]] for z in zz], "wechsel": wechsel,
             "zerfall_v": [z["v"] for z in zz if z["zerfall"]], "monoton": None, "v_c": None, "We_c_intervall": None}
        if any(zf):
            i = zf.index(True)
            e["monoton"] = all(zf[i:])
            if e["monoton"]:
                e["v_c"] = zz[i]["v"]
                e["We_c_intervall"] = [zz[i - 1]["We"] if i > 0 else 0.0, zz[i]["We"]]
        aus.append(e)
    return aus


def urteil_karte(zeilen, schw):
    """Feste Regeln aus PLAN.md, Abschnitt Latten."""
    u = []
    ohne = [z for z in zeilen if z["V2"] == 0.0]
    l2 = all(z["klasse"] == "durch" and z["q_haupt"] >= 0.99 for z in ohne)
    u.append(f"L2 Gegenprobe V2 = 0: {'bestanden' if l2 else 'VERLETZT'} ({len(ohne)} Laeufe; verlangt: alle durch, "
             "q_haupt >= 0,99)")
    mit = [s for s in schw if s["zerfall_v"] and s["V2"] != 0.0]
    if not mit:
        we_max = max(z["We"] for z in zeilen)
        u.append(f"H: kein Zerfall (Hauptfragment < 50 %) in der ganzen Karte bis We = {we_max:.2f} -> H scheitert (L1)")
    for v2 in sorted({s["V2"] for s in mit}):
        ss = [s for s in mit if s["V2"] == v2]
        if len(ss) < len(W2_1D) or not all(s["monoton"] for s in ss):
            u.append(f"H V2 {v2:+.2f}: Zerfall nicht bei allen omega^2 oder nicht monoton in v "
                     f"({[(s['w2'], s['zerfall_v']) for s in ss]}) -> H hier nicht getragen")
            continue
        lo = max(s["We_c_intervall"][0] for s in ss)
        hi = min(s["We_c_intervall"][1] for s in ss)
        u.append(f"H V2 {v2:+.2f}: We_c-Intervalle {[[round(w, 3) for w in s['We_c_intervall']] for s in ss]} -> "
                 + (f"gemeinsamer Bereich [{lo:.3f}, {hi:.3f}]: H getragen" if lo <= hi else
                    "kein gemeinsamer Bereich: We_c haengt von der Ballgroesse ab, H scheitert"))
    gesp = [z for z in zeilen if z["klasse"] == "gespalten"]
    if gesp:
        rel = []
        for z in gesp:
            vcl = schranken1d(z["w2"], z["V2"])["v_cl"]
            rel.append((z["w2"], z["V2"], z["v"], round(z["v"] / vcl, 3) if vcl else None))
        u.append(f"Gegenhypothese: {len(gesp)} gespaltene Laeufe (omega2, V2, v, v/v_cl): {rel}")
    else:
        u.append("Gegenhypothese: kein gespaltener Lauf im groben v-Raster (feinv1d entscheidet)")
    return u


def test_karte1d(out, rauch, fein):
    start = jetzt()
    dx, dt, stufe = stufe1d(fein)
    print(f"karte1d {stufe} Start {start} auf {geraet_name()}, torch {torch.__version__}", flush=True)
    zeilen, zeitreihen, dauer = [], {}, {}
    for v in V_1D:
        laeufe = [{"w2": w2, "V2": v2, "v": v} for w2 in W2_1D for v2 in V2_1D]
        t_end = t_lauf1d(v) * (RAUCH_FAKTOR if rauch else 1.0)
        t0 = uhr()
        zz, zr = rechne1d(laeufe, dx, dt, t_end)
        dauer[f"entw_v{v:.2f}"] = uhr() - t0
        print(f"  v = {v:.2f}: T = {t_end:.0f}, {dauer[f'entw_v{v:.2f}']:.1f} s", flush=True)
        zeilen += zz
        zeitreihen[f"v{v:.2f}"] = zr
    schw = schwellen1d(zeilen)
    urteil = ["Rauchtest: keine Deutung"] if rauch else urteil_karte(zeilen, schw)
    text = [f"karte1d ({stufe}, dx {dx}, dt {dt}). Start {start}, Ende {jetzt()}, {geraet_name()}"
            + (" RAUCHTEST: Zahlen ungueltig" if rauch else "")]
    text += laufzeit_text(dauer, rauch)
    text.append("omega2 V2 v | We | Klasse | Zerfall | q_haupt | durch | zurueck | frei | n_frag | Teilchenbild | "
                "E-Drift | Fragmente q@x")
    text += [zeile1d_text(z) for z in sorted(zeilen, key=lambda z: (z["w2"], z["V2"], z["v"]))]
    text.append("Schwellen je (omega2, V2): Wechsel der Klasse, Zerfall-v, We_c-Intervall")
    for s in schw:
        w = "; ".join(f"{e['v_a']:.2f}->{e['v_b']:.2f} {e['von']}->{e['nach']}" for e in s["wechsel"]) or "kein Wechsel"
        text.append(f"  {s['w2']:.2f} {s['V2']:+.2f}: {w}; Zerfall bei v = {s['zerfall_v']}; We_c {s['We_c_intervall']}")
    text += ["Urteil nach PLAN.md: " + zz for zz in urteil]
    ausgabe = {"test": "karte1d", "stufe": stufe, "start": start, "ende": jetzt(), "rauch": rauch, "dauer_s": dauer,
               "geraet": geraet_name(), "torch": torch.__version__,
               "parameter": {"dx": dx, "dt": dt, "L": L1, "x_schwamm": X_SCHWAMM1, "x0": X0_1D, "x_aus": X_AUS,
                             "t_zusatz": T_ZUSATZ, "x_s": X_S1, "B": B_STUFE, "w2": W2_1D, "V2": V2_1D, "v": V_1D,
                             "s_rel_frag": S_REL_FRAG, "q_frag_min": Q_FRAG_MIN},
               "profile": [anker(w2) for w2 in W2_1D], "laeufe": zeilen, "schwellen": schw, "urteil": urteil}
    schreiben(out, f"karte1d_{stufe}", ausgabe, zeitreihen, "\n".join(text))


def laufzeit_text(dauer, rauch):
    zeilen = ["Dauer [s]: " + ", ".join(f"{k} {s:.1f}" for k, s in dauer.items())]
    if rauch:
        entw = sum(s for k, s in dauer.items() if k.startswith("entw"))
        rest = sum(s for k, s in dauer.items() if not k.startswith("entw"))
        zeilen.append(f"Hochrechnung voller Aufruf: {rest + entw / RAUCH_FAKTOR:.0f} s (feste Teile {rest:.0f} s + "
                      f"Entwicklung x {1 / RAUCH_FAKTOR:.0f}); ueber 540 s: nicht starten, Leitung entscheidet.")
    return zeilen


# ---------------------------------------------------------------- feinv1d

def test_feinv1d(out, rauch, fein):
    start = jetzt()
    dx, dt, stufe = stufe1d(fein)
    print(f"feinv1d {stufe} Start {start} auf {geraet_name()}, torch {torch.__version__}", flush=True)
    laeufe = []
    for w2 in W2_1D:
        for v2 in FEINV_V2:
            vcl = schranken1d(w2, v2)["v_cl"]
            for rel in FEINV_REL:
                laeufe.append({"w2": w2, "V2": v2, "v": round(vcl * (1.0 + rel), 6), "rel": rel, "v_cl": vcl})
    v_min = min(lf["v"] for lf in laeufe)
    t_end = ((X0_1D + X_AUS) / v_min + FEINV_T_ZUSATZ) * (RAUCH_FAKTOR if rauch else 1.0)
    t0 = uhr()
    zeilen, zeitreihen = rechne1d(laeufe, dx, dt, t_end)
    dauer = {"entw": uhr() - t0}
    for z, lf in zip(zeilen, laeufe):
        z["rel"], z["v_cl"] = lf["rel"], lf["v_cl"]
    auswertung = []
    for w2 in W2_1D:
        for v2 in FEINV_V2:
            zz = sorted([z for z in zeilen if z["w2"] == w2 and z["V2"] == v2], key=lambda z: z["v"])
            a = anker(w2)
            v50 = None
            for p, q in zip(zz[:-1], zz[1:]):
                if (p["q_durch"] - 0.5) * (q["q_durch"] - 0.5) <= 0.0 and p["q_durch"] != q["q_durch"]:
                    v50 = p["v"] + (0.5 - p["q_durch"]) * (q["v"] - p["v"]) / (q["q_durch"] - p["q_durch"])
                    break
            fenster = [z["v"] for z in zz if 0.1 < z["q_durch"] < 0.9]
            auswertung.append({"w2": w2, "V2": v2, "v_cl": zz[0]["v_cl"], "v50": v50,
                               "v50_zu_vcl": (v50 / zz[0]["v_cl"]) if v50 else None,
                               "We50": (a["we_faktor"] * v50 ** 2) if v50 else None,
                               "spaltfenster_v": fenster, "n_gespalten": sum(1 for z in zz if z["klasse"] == "gespalten"),
                               "q_durch": [[z["v"], round(z["q_durch"], 4), z["klasse"]] for z in zz]})
    urteil = ["Rauchtest: keine Deutung"]
    if not rauch:
        urteil = []
        ok = [e for e in auswertung if e["v50"] is not None]
        if len(ok) == len(auswertung):
            nah = all(abs(e["v50_zu_vcl"] - 1.0) <= 0.1 for e in ok)
            urteil.append("Uebergang zurueck -> durch liegt " + ("bei allen sechs innerhalb 10 % von v_cl "
                          "(Gegenhypothese/Teilchenschwelle getragen)" if nah else "NICHT ueberall bei v_cl"))
            for v2 in FEINV_V2:
                we = {e["w2"]: e["We50"] for e in ok if e["V2"] == v2}
                if 0.6 in we and 0.8 in we:
                    urteil.append(f"V2 {v2:+.2f}: We50(0,8)/We50(0,6) = {we[0.8] / we[0.6]:.3f} "
                                  "(Weber-Bild: etwa 1; Teilchenschwelle: etwa 1,8)")
        else:
            urteil.append("Nicht bei allen (omega2, V2) ein Uebergang q_durch = 0,5 im Raster: Raster zu schmal oder "
                          "Ausgang haengt (siehe Tabelle)")
    text = [f"feinv1d ({stufe}, dx {dx}, dt {dt}, T {t_end:.0f}). Start {start}, Ende {jetzt()}, {geraet_name()}"
            + (" RAUCHTEST: Zahlen ungueltig" if rauch else "")]
    text += laufzeit_text(dauer, rauch)
    text += [zeile1d_text(z) + f" | v/v_cl {1.0 + z['rel']:.2f}" for z in zeilen]
    for e in auswertung:
        text.append(f"  omega2 {e['w2']:.2f} V2 {e['V2']:+.2f}: v_cl {e['v_cl']:.4f}, v50 {e['v50']}, v50/v_cl "
                    f"{e['v50_zu_vcl']}, We50 {e['We50']}, Spaltfenster {e['spaltfenster_v']}")
    text += ["Urteil nach PLAN.md: " + u for u in urteil]
    ausgabe = {"test": "feinv1d", "stufe": stufe, "start": start, "ende": jetzt(), "rauch": rauch, "dauer_s": dauer,
               "geraet": geraet_name(), "torch": torch.__version__, "t_end": t_end,
               "parameter": {"dx": dx, "dt": dt, "rel": FEINV_REL, "V2": FEINV_V2, "w2": W2_1D},
               "laeufe": zeilen, "auswertung": auswertung, "urteil": urteil}
    schreiben(out, f"feinv1d_{stufe}", ausgabe, zeitreihen, "\n".join(text))


# ---------------------------------------------------------------- l3 (Vergleich zweier Dateien)

def test_l3(out, pfad_a, pfad_b):
    with open(pfad_a) as fh:
        a = json.load(fh)
    with open(pfad_b) as fh:
        b = json.load(fh)
    schluessel = lambda z: (round(z["w2"], 6), round(z["V2"], 6), round(z["v"], 6))
    bb = {schluessel(z): z for z in b["laeufe"]}
    gleich, anders, dq = 0, [], []
    for z in a["laeufe"]:
        y = bb.get(schluessel(z))
        if y is None:
            continue
        if z["klasse"] == y["klasse"]:
            gleich += 1
            dq.append(max(abs(z["q_haupt"] - y["q_haupt"]), abs(z["q_durch"] - y["q_durch"])))
        else:
            anders.append([z["w2"], z["V2"], z["v"], z["klasse"], y["klasse"], z["zerfall"], y["zerfall"]])
    zerfall_anders = [x for x in anders if x[5] != x[6]]
    bestanden = len(anders) <= 1 and not zerfall_anders and (max(dq) if dq else 0.0) <= 0.05
    text = [f"L3-Vergleich {pfad_a} gegen {pfad_b}: {gleich} gleiche Klassen, {len(anders)} verschieden "
            f"(davon Zerfall verschieden: {len(zerfall_anders)}); max |dq| bei gleicher Klasse "
            f"{(max(dq) if dq else 0.0):.4f}. L3 {'bestanden' if bestanden else 'NICHT bestanden'} "
            "(verlangt: hoechstens 1 Klassenwechsel, kein Zerfallswechsel, |dq| <= 0,05)"]
    text += [f"  verschieden: {x}" for x in anders]
    schreiben(out, "l3_vergleich", {"a": pfad_a, "b": pfad_b, "gleich": gleich, "anders": anders,
                                    "max_dq": max(dq) if dq else 0.0, "bestanden": bestanden}, None, "\n".join(text))


# ---------------------------------------------------------------- winkel2d

SPALTEN2D = ["Q_links", "Q_mitte", "Q_rechts", "Q_box", "E_box", "Smax_links", "Smax_rechts",
             "QX_rechts", "QY_rechts", "QX_links", "QY_links"]


def messen2d_bauen(g, V):
    links = (g.x < -X_S2).to(F64)
    mitte = (g.x.abs() <= X_S2).to(F64)
    rechts = (g.x > X_S2).to(F64)

    def messen(psi, vel):
        s = psi.real ** 2 + psi.imag ** 2
        rho = 2.0 * (psi * vel.conj()).imag
        ph = torch.fft.fft2(psi)
        gx = torch.fft.ifft2(ph * (1j * g.kx))
        gy = torch.fft.ifft2(ph * (1j * g.ky))
        e = (vel.real ** 2 + vel.imag ** 2 + gx.real ** 2 + gx.imag ** 2 + gy.real ** 2 + gy.imag ** 2
             + r3.upot(s) + V * s)
        da = g.dA
        return torch.stack([(rho * links).sum((1, 2)) * da, (rho * mitte).sum((1, 2)) * da,
                            (rho * rechts).sum((1, 2)) * da, rho.sum((1, 2)) * da, e.sum((1, 2)) * da,
                            (s * links).amax((1, 2)), (s * rechts).amax((1, 2)),
                            (rho * rechts * g.x).sum((1, 2)) * da, (rho * rechts * g.y).sum((1, 2)) * da,
                            (rho * links * g.x).sum((1, 2)) * da, (rho * links * g.y).sum((1, 2)) * da], dim=1)
    return messen


def entwickeln2d(g, psi, vel, V, dt, t_end, messen, t_schnapp):
    """Velocity-Verlet wie tests2d_r3.entwickeln; zusaetzlich je Lauf b ein Schnappschuss (S, rho auf der CPU) beim
    ersten Messzeitpunkt t >= t_schnapp[b]."""
    daempf = torch.exp(-g.sigma * dt)
    mk2 = g.minus_k2

    def kraft(p):
        lap = torch.fft.ifft2(torch.fft.fft2(p) * mk2)
        s = p.real * p.real + p.imag * p.imag
        return lap - (1.0 + s * (1.5 * s - 2.0) + V) * p

    schnapp = [None] * psi.shape[0]

    def fangen(t):
        for b in range(psi.shape[0]):
            if schnapp[b] is None and t >= t_schnapp[b] - 1e-9:
                s = psi[b].real ** 2 + psi[b].imag ** 2
                rho = 2.0 * (psi[b] * vel[b].conj()).imag
                schnapp[b] = {"t": t, "S": s.cpu(), "rho": rho.cpu()}

    n_schritte = int(round(t_end / dt))
    alle = int(round(T_MESS / dt))
    reihe = [messen(psi, vel)]
    fangen(0.0)
    F = kraft(psi)
    for n in range(1, n_schritte + 1):
        vel.add_(F, alpha=0.5 * dt)
        psi.add_(vel, alpha=dt)
        F = kraft(psi)
        vel.add_(F, alpha=0.5 * dt)
        vel.mul_(daempf)
        if n % alle == 0:
            reihe.append(messen(psi, vel))
            fangen(n * dt)
    daten = torch.stack(reihe)
    if not bool(torch.isfinite(daten).all()):
        raise RuntimeError("nicht endliche Messwerte: Lauf instabil")
    t = torch.arange(daten.shape[0], dtype=F64, device=DEV) * (alle * dt)
    for b in range(psi.shape[0]):                     # falls t_schnapp > t_end: Endzustand
        if schnapp[b] is None:
            s = psi[b].real ** 2 + psi[b].imag ** 2
            schnapp[b] = {"t": t[-1].item(), "S": s.cpu(), "rho": (2.0 * (psi[b] * vel[b].conj()).imag).cpu()}
    return t, daten, schnapp


def fragmente2d(s, rho, xs, dA, q0, s_c, r_frag, n_max=5):
    """Gierige Spitzensuche: dichteste Stelle, Ladung im Kreis r_frag, Kreis ausblenden, wiederholen,
    solange S_max > 0,05 S_c. s, rho: (n, n) auf der CPU, Index [iy, ix]; xs: Koordinaten (n,)."""
    s = s.clone()
    rho = rho.clone()
    n = s.shape[0]
    X = xs.view(1, n)
    Y = xs.view(n, 1)
    aus = []
    for _ in range(n_max):
        smax = s.max().item()
        if smax < 0.05 * s_c:
            break
        idx = int(torch.argmax(s))
        iy, ix = idx // n, idx % n
        maske = ((X - xs[ix]) ** 2 + (Y - xs[iy]) ** 2) < r_frag ** 2
        w = rho * maske
        q = w.sum().item() * dA
        ws = w.sum().item()
        xm = (w * X).sum().item() / ws if abs(ws) > 1e-300 else xs[ix].item()
        ym = (w * Y).sum().item() / ws if abs(ws) > 1e-300 else xs[iy].item()
        aus.append({"q": q / q0, "x": xm, "y": ym, "S_max": smax})
        s = s * (~maske)
        rho = rho * (~maske)
    return sorted(aus, key=lambda f: -f["q"])


def test_winkel2d(out, rauch, stufen_wahl, karte):
    start = jetzt()
    print(f"winkel2d Start {start} auf {geraet_name()}, torch {torch.__version__}", flush=True)
    dauer = {}
    t0 = uhr()
    sch = r3.schiessen(list(FAMILIE_2D), [0] * len(FAMILIE_2D))
    fam = r3.profile_bauen(sch, 1.5 * L_2D + 5.0)
    dauer["schiessen_s"] = uhr() - t0
    pr = [p for p in fam if p["omega2"] == W2_2D][0]
    w = math.sqrt(W2_2D)
    m1, q1 = pr["E"], pr["Q"]
    r_q = math.sqrt(pr["N"] / (math.pi * pr["S_zentrum"]))
    sigma = pr["G"] / (math.pi * r_q)
    rho_w = 2.0 * W2_2D * pr["S_zentrum"]
    we_faktor = rho_w * 2.0 * r_q / sigma
    weber = {"R_Q": r_q, "D": 2.0 * r_q, "sigma": sigma, "rho_W": rho_w, "we_faktor": we_faktor,
             "G": pr["G"], "N": pr["N"], "Q": q1, "E": m1, "S_c": pr["S_zentrum"], "R_halb": pr["R_halb"],
             "energieschranke_duennwand_We": 4.0 * (math.sqrt(2.0) - 1.0) * 2.0}
    vorh, t_eval = {}, {}
    for name, v2, th in LAEUFE_2D:
        thr = math.radians(th)
        vv = r3.brechung_vorhersage(m1, q1, fam, v2, V_2D, thr)
        vorh[name] = vv
        vn1 = V_2D * math.cos(thr)
        if vv is not None and vv["ausgang"] == "durchgelaufen":
            vn2 = vv["v2"] * math.cos(math.radians(vv["theta2_grad"]))
            t_eval[name] = min(abs(X0_2D) / vn1 + X_EVAL_2D / vn2, T_2D)
        else:
            t_eval[name] = min(2.0 * abs(X0_2D) / vn1, T_2D)
        print(f"Vorhersage {name}: v_n {vn1:.4f}, We_n {we_faktor * vn1 ** 2:.3f}, t_eval {t_eval[name]:.1f}, "
              f"{json.dumps(vv)}", flush=True)
    faktor = RAUCH_FAKTOR if rauch else 1.0
    t_end = T_2D * faktor
    ergebnis, zeitreihen = {}, {}
    for stufe, dx, dt in STUFEN_2D:
        if stufen_wahl != "beide" and stufe != stufen_wahl:
            continue
        g = r3.Gitter(L_2D, dx)
        psis, vels, vs, ts = [], [], [], []
        for name, v2, th in LAEUFE_2D:
            thr = math.radians(th)
            y0 = -0.5 * V_2D * math.sin(thr) * T_2D           # wie Runde 3: y = 0 bei t = T/2
            p_, v_ = r3.ball_feld(g, pr, x0=X0_2D, y0=y0, v=V_2D, winkel=thr)
            psis.append(p_)
            vels.append(v_)
            vs.append(v2 * 0.5 * (1.0 + torch.tanh(g.x / B_STUFE)))
            ts.append(t_eval[name] * faktor)
        psi = torch.cat(psis).contiguous()
        vel = torch.cat(vels).contiguous()
        V = torch.cat(vs)
        t0 = uhr()
        t, daten, schnapp = entwickeln2d(g, psi, vel, V, dt, t_end, messen2d_bauen(g, V), ts)
        dauer[f"entw_{stufe}_s"] = uhr() - t0
        print(f"Entwicklung {stufe} fertig nach {dauer[f'entw_{stufe}_s']:.1f} s", flush=True)
        d = daten.cpu()
        tc = t.cpu()
        xs = g.x.flatten().cpu()
        zeilen = []
        for b, (name, v2, th) in enumerate(LAEUFE_2D):
            q0 = d[0, b, 3].item()
            sn = schnapp[b]
            i_ev = min(int(round(sn["t"] / T_MESS)), d.shape[0] - 1)
            fr = fragmente2d(sn["S"], sn["rho"], xs, g.dA, q0, pr["S_zentrum"], pr["R_halb"] + 5.0)
            kl = klassifizieren(fr, d[i_ev, b, 1].item() / q0, X_S2)
            vn1 = V_2D * math.cos(math.radians(th))
            qbox = d[:, b, 3] / q0
            verlust = (qbox < 0.99).nonzero()
            z = {"lauf": name, "V2": v2, "winkel": th, "v_n": vn1, "We_n": we_faktor * vn1 ** 2, "stufe": stufe,
                 "dx": dx, "dt": dt, "t_eval": sn["t"], **kl, "fragmente": fr,
                 "q_rechts_eval": d[i_ev, b, 2].item() / q0, "q_links_eval": d[i_ev, b, 0].item() / q0,
                 "q_box_eval": qbox[i_ev].item(), "q_box_ende": qbox[-1].item(),
                 "q_rechts_ende": d[-1, b, 2].item() / q0,
                 "t_randschicht": tc[int(verlust[0])].item() if verlust.numel() > 0 else None,
                 "E_drift_bis_eval": ((d[:i_ev + 1, b, 4] / d[0, b, 4] - 1.0).abs().max()).item(),
                 "vorhersage": vorh[name]}
            qr = d[i_ev, b, 2].item()
            if qr > Q_FRAG_MIN * q0 and i_ev >= 10:
                qa = d[i_ev - 10, b, 2].item()
                if qa > Q_FRAG_MIN * q0:
                    z["vx_rechts"] = (d[i_ev, b, 7].item() / qr - d[i_ev - 10, b, 7].item() / qa) / (10 * T_MESS)
                    z["vy_rechts"] = (d[i_ev, b, 8].item() / qr - d[i_ev - 10, b, 8].item() / qa) / (10 * T_MESS)
            zeilen.append(z)
        ergebnis[stufe] = zeilen
        zeitreihen[stufe] = {"t": tc, "daten": d, "spalten": SPALTEN2D, "laeufe": list(LAEUFE_2D),
                             "schnapp_S": torch.stack([s["S"] for s in schnapp]),
                             "schnapp_t": [s["t"] for s in schnapp]}
    # Kennzahlen: kritischer Winkel, L2, L3, Vergleich mit 1D
    kenn, urteil = {}, ["Rauchtest: keine Deutung"] if rauch else []
    haupt = ergebnis.get("grob") or ergebnis.get("fein") or []
    stufe_d = [z for z in haupt if z["V2"] != 0.0]
    if not rauch and haupt:
        ohne = [z for z in haupt if z["V2"] == 0.0]
        l2 = all(z["klasse"] == "durch" and z["q_haupt"] >= 0.97 for z in ohne)
        urteil.append(f"L2 Gegenprobe V2 = 0: {'bestanden' if l2 else 'VERLETZT'} (verlangt: durch, q_haupt >= 0,97)")
        zf = sorted([(z["winkel"], z["zerfall"], z["v_n"], z["We_n"]) for z in stufe_d])
        if not any(x[1] for x in zf):
            urteil.append("Kein Zerfall bei 0 bis 60 Grad: kein kritischer Winkel. Tropfen-Weber-Deutung der "
                          "Runde-3-Verluste nicht getragen; Vorhersage V-2D-1 (Randschicht-Artefakt) pruefen: "
                          + ", ".join(f"{z['lauf']} q_rechts_eval {z['q_rechts_eval']:.3f}, q_box_ende "
                                      f"{z['q_box_ende']:.3f}, t_randschicht {z['t_randschicht']}" for z in stufe_d))
        else:
            ok = [x for x in zf if not x[1]]
            nok = [x for x in zf if x[1]]
            theta_c = [max(x[0] for x in nok), min(x[0] for x in ok)] if ok else [max(x[0] for x in nok), None]
            kenn["theta_c_grad"] = theta_c
            kenn["v_n_c"] = [V_2D * math.cos(math.radians(a)) for a in theta_c if a is not None]
            kenn["We_n_c"] = [we_faktor * v ** 2 for v in kenn["v_n_c"]]
            mono = all(x[1] for x in zf if x[0] <= theta_c[0])
            urteil.append(f"Zerfall bei {[x[0] for x in nok]} Grad; kritischer Winkel zwischen {theta_c} Grad, "
                          f"v_n,c {kenn['v_n_c']}, We_n,c {kenn['We_n_c']}; monoton: {mono}")
    if not rauch and "grob" in ergebnis and "fein" in ergebnis:
        gg = {z["lauf"]: z for z in ergebnis["grob"]}
        aend = [(z["lauf"], z["klasse"] == gg[z["lauf"]]["klasse"], abs(z["q_haupt"] - gg[z["lauf"]]["q_haupt"]),
                 abs(z["q_rechts_eval"] - gg[z["lauf"]]["q_rechts_eval"])) for z in ergebnis["fein"]]
        l3 = all(a[1] for a in aend) and max(max(a[2], a[3]) for a in aend) <= 0.02
        kenn["L3"] = {"aenderungen": aend, "bestanden": l3}
        urteil.append(f"L3 grob/fein: {'bestanden' if l3 else 'NICHT bestanden'} (verlangt: gleiche Klasse, "
                      "|dq| <= 0,02)")
    if karte and not rauch:
        try:
            with open(karte) as fh:
                k1 = json.load(fh)
            for s in k1["schwellen"]:
                if abs(s["w2"] - W2_2D) < 1e-9 and abs(s["V2"] + 0.02) < 1e-9:
                    kenn["schwelle_1d"] = s
                    urteil.append(f"1D-Vergleich (omega2 0,7, V2 -0,02): Klassen {s['klassen']}, We_c {s['We_c_intervall']}")
        except (OSError, KeyError, ValueError) as err:
            urteil.append(f"1D-Vergleich nicht moeglich: {err}")
    ende = jetzt()
    ausgabe = {"test": "winkel2d", "start": start, "ende": ende, "rauch": rauch, "dauer_s": dauer,
               "geraet": geraet_name(), "torch": torch.__version__,
               "parameter": {"omega2": W2_2D, "v": V_2D, "L": L_2D, "T": T_2D, "x0": X0_2D, "x_eval": X_EVAL_2D,
                             "x_s": X_S2, "B": B_STUFE, "stufen": STUFEN_2D, "laeufe": LAEUFE_2D},
               "ball": r3.profil_info(pr), "weber": weber, "t_eval": t_eval, "vorhersage": vorh,
               "ergebnis": ergebnis, "kennzahlen": kenn, "urteil": urteil}
    text = [f"winkel2d. Start {start}, Ende {ende}, {geraet_name()}" + (" RAUCHTEST: Zahlen ungueltig" if rauch else "")]
    text += laufzeit_text(dauer, rauch)
    text.append(f"Ball omega2 {W2_2D}: Q {q1:.4f}, E {m1:.4f}, R_Q {r_q:.4f}, sigma {sigma:.5f}, rho_W {rho_w:.5f}, "
                f"We-Faktor {we_faktor:.4f} (We_n = Faktor v_n^2)")
    text.append("Stufe Lauf | Winkel | v_n | We_n | t_eval | Klasse | Zerfall | q_haupt | durch | zurueck | frei | n | "
                "q_rechts(eval) | q_box(eval) | q_box(Ende) | t_randschicht | E-Drift")
    for stufe, zz in ergebnis.items():
        for z in zz:
            text.append(f"  {stufe} {z['lauf']} | {z['winkel']:.0f} | {z['v_n']:.4f} | {z['We_n']:.3f} | "
                        f"{z['t_eval']:.0f} | {z['klasse']} | {'ZERFALL' if z['zerfall'] else '-'} | "
                        f"{z['q_haupt']:.3f} | {z['q_durch']:.3f} | {z['q_zurueck']:.3f} | {z['q_frei']:.3f} | "
                        f"{z['n_frag']} | {z['q_rechts_eval']:.4f} | {z['q_box_eval']:.4f} | {z['q_box_ende']:.4f} | "
                        f"{z['t_randschicht']} | {z['E_drift_bis_eval']:.1e}")
    text += ["Urteil nach PLAN.md: " + u for u in urteil]
    schreiben(out, "winkel2d", ausgabe, zeitreihen, "\n".join(text))


# ---------------------------------------------------------------- main

def main():
    global DEV
    ap = argparse.ArgumentParser(description="Runde 6: Q-Ball an der Stufe, Weber-Test")
    ap.add_argument("test", choices=["papier", "karte1d", "feinv1d", "winkel2d", "l3", "rauch"])
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda")
    ap.add_argument("--out", default=None)
    ap.add_argument("--fein", action="store_true", help="1D: dx und dt halbiert (Latte L3)")
    ap.add_argument("--stufe", choices=["grob", "fein", "beide"], default="beide", help="2D-Aufloesung")
    ap.add_argument("--karte", default=None, help="winkel2d: karte1d_grob_ergebnis.json fuer den 1D-Vergleich")
    ap.add_argument("--a", default=None, help="l3: erste Ergebnisdatei (grob)")
    ap.add_argument("--b", default=None, help="l3: zweite Ergebnisdatei (fein)")
    ap.add_argument("--nur", default="karte1d,feinv1d,winkel2d", help="rauch: Liste der Unterbefehle")
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
    r3.DEV = DEV                                          # 2D-Hilfen aus tests2d_r3.py auf dasselbe Geraet
    out = args.out or os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   "rauchtest" if args.test == "rauch" else "ausgabe")
    if args.test == "papier":
        test_papier(out)
    elif args.test == "karte1d":
        test_karte1d(out, False, args.fein)
    elif args.test == "feinv1d":
        test_feinv1d(out, False, args.fein)
    elif args.test == "winkel2d":
        test_winkel2d(out, False, args.stufe, args.karte)
    elif args.test == "l3":
        if not (args.a and args.b):
            raise SystemExit("l3 braucht --a und --b")
        test_l3(out, args.a, args.b)
    else:
        nur = [n.strip() for n in args.nur.split(",") if n.strip()]
        test_papier(out)
        if "karte1d" in nur:
            test_karte1d(out, True, args.fein)
        if "feinv1d" in nur:
            test_feinv1d(out, True, args.fein)
        if "winkel2d" in nur:
            test_winkel2d(out, True, args.stufe, None)


if __name__ == "__main__":
    main()
