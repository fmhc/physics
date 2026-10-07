#!/usr/bin/env python3
"""Runde 3 (runden-v3), 1D-Tests: Chemie 1, 2/3, 7, 15, 14 (Zufall); Wellen 5 nur als Papierprobe (t6).

Version 2 (2026-09-30, geschrieben ab 02:50:57 CEST, gemessen): nur test2 geaendert (Punktzwang in der Mitte statt Schwerpunktzwang, normiertes
Anfangsfeld, Einfrieren ungebundener Laeufe statt Abbruch; Grund und Notiz in PLAN.md, Abschnitt 12).
Version 1 (2026-09-30, 02:13 CEST): erste Abgabe; t1, t3 bis t6 liefen damit auf der .69 mit rc 0, t2 brach ab.

Explorativ. Ohne Testlauf abgegeben (auf dem Laptop gilt das Interpreterverbot). Plan, Aufruf, Vorhersagen und Latten
stehen in PLAN.md daneben. Nur CUDA, float64 (psi als complex128); ohne CUDA bricht das Programm ab.

Modell (wie RUNDE-01/qg1/qg1.py ohne Feld, A = B = C = 1):
    L = |psi_t|^2 - |psi_x|^2 - U(S),  S = |psi|^2,  U = S - S^2 + S^3/2,  psi_tt = psi_xx - U'(S) psi.
    Ball: psi = f(x) exp(-i omega t); Anti-Ball: psi = f(x) exp(+i omega t).
    Ladungsdichte rho = 2 Im(psi conj(psi_t)), Energiedichte |psi_t|^2 + |psi_x|^2 + U, Impulsdichte -2 Re(conj(psi_t) psi_x).
Uebernommen aus qg1.py (unveraendert): rhs, rk4, schiessen, profil_bahn, profil_anker, energien, Gitter (dx = 0,1 und
0,05 mit dt = 0,05 und 0,025), Velocity-Verlet mit Daempfungsschicht. Geaendert nur:
    - gitter() hat die Boxlaenge als Parameter (Standard wie qg1).
    - Profile an beliebiger Stelle: lineare Interpolation der Schiessbahn (h = 0,01) statt Indexgriff; Lorentz-Boost.
    - Die Profile werden einmal geschossen und in profile_r3.pt zwischengespeichert.
    - Test 2 relaxiert statt zu entwickeln (gedaempfte Dynamik desselben Verlet-Schemas, feste Ladung).
Wellen 5 ist im Ein-Feld-Modell nicht umsetzbar (duenner Hintergrund modulationsinstabil, v_c = 0; PLAN.md):
t6 rechnet nur die Dispersionstabelle, keine Zeitentwicklung.

Aufruf:  python tests1d_r3.py {profil,t1,t2,t3,t4,t5,t6,alle} [--out ORDNER] [--profil DATEI] [--kurz]
         --kurz: Rauchtest, alle Lauf- und Relaxationszeiten x 0,1 (Zahlen dann ohne Bedeutung).
"""
import argparse
import datetime
import json
import math
import os
import time

import torch

DEV = torch.device("cuda")
F64 = torch.float64
C128 = torch.complex128

# ---- Feste Parameter aus qg1.py ----
L_BOX = 120.0            # Box [-L, L], Rand wie qg1
X_SPONGE = 80.0          # Daempfungsschicht fuer |x| > X_SPONGE
SIGMA0 = 1.0             # Daempfung am Rand
DX, DT = 0.1, 0.05       # grob; die feine Stufe halbiert beide
T_MEAS = 1.0             # Messabstand
H_ODE = 0.01             # Schrittweite beim Schiessen
X_ODE = 80.0             # Schiesslaenge
N_KAND, RUNDEN = 4096, 4 # Kandidaten je Einschachtelungsrunde, Zahl der Runden
SCHWANZ = 1e-3           # ab f < SCHWANZ * f(0): exponentieller Schwanz
TOL_PROFIL = 1e-6        # K0: max |f_Schuss - f_Anker| auf dem Gitter

# ---- Neu in Runde 3 ----
OMEGA2_ALLE = [0.60, 0.70, 0.80, 0.85]    # alle in den sechs Tests gebrauchten Baelle
X_INNEN = 75.0                            # Messbereich |x| < X_INNEN, vor der Daempfungsschicht
STUFEN = (("grob", DX, DT), ("fein", DX / 2.0, DT / 2.0))


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    torch.cuda.synchronize()
    return time.perf_counter()


# ---------------------------------------------------------------- Profil durch Schiessen (aus qg1.py)

def rhs(f, fp, a0):
    """f'' = (U'(f^2) - omega^2) f = (a0 - 2 f^2 + 1.5 f^4) f,  a0 = 1 - omega^2."""
    s = f * f
    return fp, (a0 - 2.0 * s + 1.5 * s * s) * f


def rk4(f, fp, a0, h):
    k1f, k1p = rhs(f, fp, a0)
    k2f, k2p = rhs(f + 0.5 * h * k1f, fp + 0.5 * h * k1p, a0)
    k3f, k3p = rhs(f + 0.5 * h * k2f, fp + 0.5 * h * k2p, a0)
    k4f, k4p = rhs(f + h * k3f, fp + h * k3p, a0)
    return (f + (h / 6.0) * (k1f + 2.0 * k2f + 2.0 * k3f + k4f),
            fp + (h / 6.0) * (k1p + 2.0 * k2p + 2.0 * k3p + k4p))


def schiessen(a0):
    """Zentralwert f(0) je omega durch Einschachteln, alle omega und Kandidaten gleichzeitig (unveraendert aus qg1)."""
    n_om = a0.shape[0]
    lo = torch.full((n_om, 1), 1e-3, dtype=F64, device=DEV)
    hi = torch.ones((n_om, 1), dtype=F64, device=DEV)
    stufen = torch.linspace(0.0, 1.0, N_KAND, dtype=F64, device=DEV)
    n_schritte = int(round(X_ODE / H_ODE))
    for _ in range(RUNDEN):
        f0 = lo + (hi - lo) * stufen
        f, fp = f0.clone(), torch.zeros_like(f0)
        zustand = torch.zeros_like(f0)
        for _ in range(n_schritte):
            f, fp = rk4(f, fp, a0, H_ODE)
            ueber = (zustand == 0) & (f < 0)
            unter = (zustand == 0) & (f >= 0) & (fp > 0)
            zustand = zustand + ueber.to(F64) - unter.to(F64)
            lebt = (zustand == 0).to(F64)
            f = f * lebt
            fp = fp * lebt
        lo = torch.where(zustand < 0, f0, torch.zeros_like(f0)).max(dim=1, keepdim=True).values
        hi = torch.where(zustand > 0, f0, torch.full_like(f0, 2.0)).min(dim=1, keepdim=True).values
    return 0.5 * (lo + hi), hi - lo


def profil_bahn(f0, a0):
    """Schiessbahn f(j h) ab f(0) = f0, bis f unter SCHWANZ * f0 faellt; danach eingefroren (unveraendert aus qg1)."""
    n_schritte = int(round(X_ODE / H_ODE))
    f, fp = f0.clone(), torch.zeros_like(f0)
    schwelle = SCHWANZ * f0
    steigt = torch.zeros_like(f0, dtype=torch.bool)
    bahn = [f]
    for _ in range(n_schritte):
        weiter = f >= schwelle
        f_neu, fp_neu = rk4(f, fp, a0, H_ODE)
        steigt = steigt | (weiter & (fp_neu > 0))
        f = torch.where(weiter, f_neu, f)
        fp = torch.where(weiter, fp_neu, fp)
        bahn.append(f)
    if bool(steigt.any()):
        raise RuntimeError("Schiessbahn steigt vor dem Schwanz wieder an: f(0) zu ungenau")
    bahn = torch.cat(bahn, dim=1)
    j_cut = (bahn >= schwelle).sum(dim=1, keepdim=True)
    if bool((j_cut > n_schritte).any()):
        raise RuntimeError("Schwanzschwelle innerhalb X_ODE nicht erreicht")
    return bahn, j_cut


def gitter(dx, L=L_BOX):
    """Symmetrisches Gitter x_i = (i - i0) dx auf [-L, L]; x = 0 liegt genau auf einem Punkt."""
    i0 = int(round(L / dx))
    return (torch.arange(2 * i0 + 1, dtype=F64, device=DEV) - i0) * dx


def profil_anker(w2, dx):
    """Analytischer 1D-Anker (nur Kontrolle): f^2 = 2 a0 / (1 + b0 cosh(2 sqrt(a0) x))."""
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    x = gitter(dx)
    return torch.sqrt(2.0 * a0 / (1.0 + b0 * torch.cosh(2.0 * math.sqrt(a0) * x)))


def energien(f, w2, dx):
    """W, G, V und Q eines ruhenden Profils, als Gittersummen. f: (n_om, N) (aus qg1)."""
    w2 = torch.tensor(w2, dtype=F64, device=DEV)
    s = f * f
    w = w2 * s.sum(1) * dx
    g = ((f[:, 1:] - f[:, :-1]) / dx).pow(2).sum(1) * dx
    v = (s - s * s + 0.5 * s ** 3).sum(1) * dx
    q = 2.0 * torch.sqrt(w2) * s.sum(1) * dx
    return w, g, v, q


# ---------------------------------------------------------------- Profile: Zwischenspeicher, Auswertung, Baelle

def profile_holen(pfad):
    """Schiesst alle OMEGA2_ALLE einmal (qg1-Verfahren) und speichert Bahn und Schwanzindex; laedt, wenn vorhanden."""
    if os.path.exists(pfad):
        d = torch.load(pfad, map_location=DEV, weights_only=True)
        if d["omega2"] == OMEGA2_ALLE and d["h_ode"] == H_ODE and d["x_ode"] == X_ODE:
            print(f"Profile aus {pfad} geladen (geschossen {d['erzeugt']})", flush=True)
            return d
    t0 = uhr()
    a0 = (1.0 - torch.tensor(OMEGA2_ALLE, dtype=F64, device=DEV)).unsqueeze(1)
    f0, klammer = schiessen(a0)
    bahn, j_cut = profil_bahn(f0, a0)
    d = {"omega2": list(OMEGA2_ALLE), "h_ode": H_ODE, "x_ode": X_ODE, "bahn": bahn, "j_cut": j_cut, "f0": f0,
         "klammer": klammer, "schiessen_s": uhr() - t0, "erzeugt": jetzt()}
    torch.save(d, pfad)
    print(f"Schiessen fertig nach {d['schiessen_s']:.1f} s, gespeichert in {pfad}", flush=True)
    return d


def iw_von(w2):
    return OMEGA2_ALLE.index(w2)


def profil_werte(p, iw, xi):
    """f(|xi|) aus der Schiessbahn und df/dxi.

    Innen lineare Interpolation der Bahn (h = 0,01), jenseits der Schwelle f_cut exp(-sqrt(a0)(|xi| - x_cut)) wie qg1.
    Ableitung aus dem ersten Integral f'^2 = f^2 (a0 - f^2 + f^4/2), Vorzeichen -sign(xi)."""
    a0 = 1.0 - p["omega2"][iw]
    bahn = p["bahn"][iw]
    jc = int(p["j_cut"][iw, 0].item())
    a = xi.abs() / H_ODE
    j0 = a.floor().long().clamp(max=bahn.shape[0] - 2)
    w = a - j0.to(F64)
    innen = (1.0 - w) * bahn[j0] + w * bahn[j0 + 1]
    aussen = bahn[jc] * torch.exp(-math.sqrt(a0) * (a - jc) * H_ODE)
    f = torch.where(a < jc, innen, aussen)
    s = f * f
    fp = -torch.sign(xi) * f * torch.sqrt((a0 - s + 0.5 * s * s).clamp(min=0.0))
    return f, fp


def k0_pruefen(p, dx):
    """K0 wie qg1: max |f_Schuss - f_Anker| auf dem Gitter, je omega."""
    x = gitter(dx)
    return [(profil_werte(p, iw, x)[0] - profil_anker(w2, dx)).abs().max().item()
            for iw, w2 in enumerate(p["omega2"])]


def ball(p, iw, x, x0, v=0.0, theta=0.0, anti=False):
    """psi und psi_t bei t = 0 fuer einen Ball bei x0 mit Geschwindigkeit v (exakter Lorentz-Boost) und Phase theta.

    Ball: f(g (x - x0 - v t)) exp(-i omega g (t - v (x - x0))); Anti-Ball: komplex konjugiert. Danach mal exp(i theta)."""
    om = math.sqrt(p["omega2"][iw])
    gam = 1.0 / math.sqrt(1.0 - v * v)
    f, fp = profil_werte(p, iw, gam * (x - x0))
    phase = torch.polar(torch.ones_like(x), om * gam * v * (x - x0))
    psi = f * phase
    vel = ((-gam * v) * fp) * phase - (1j * om * gam) * psi
    if anti:
        psi, vel = torch.conj_physical(psi), torch.conj_physical(vel)
    dreh = complex(math.cos(theta), math.sin(theta))
    return psi * dreh, vel * dreh


def stapel(n_laeufe, x):
    return (torch.zeros(n_laeufe, x.shape[0], dtype=C128, device=DEV),
            torch.zeros(n_laeufe, x.shape[0], dtype=C128, device=DEV))


def spalte(werte):
    return torch.tensor(werte, dtype=F64, device=DEV).unsqueeze(1)


# ---------------------------------------------------------------- Dichten

def s_von(psi):
    return psi.real ** 2 + psi.imag ** 2


def u_von(s):
    return s - s * s + 0.5 * s ** 3


def rho_von(psi, vel):
    return 2.0 * (psi * vel.conj()).imag


def e_dichte(psi, vel, dx):
    e = vel.abs() ** 2 + u_von(s_von(psi))
    e[:, :-1] += ((psi[:, 1:] - psi[:, :-1]).abs() / dx) ** 2
    return e


# ---------------------------------------------------------------- Zeitentwicklung (Verlet aus qg1)

def entwickeln(psi, vel, x, dx, dt, t_end, messen, t_mess=T_MEAS):
    """Velocity-Verlet mit Daempfungsschicht aus qg1 (A = B = C = 1) fuer alle Laeufe als ein Stapel (B x N)."""
    sigma = SIGMA0 * ((x.abs() - X_SPONGE).clamp(min=0.0) / (L_BOX - X_SPONGE)) ** 2

    def kraft(psi):
        fluss = (psi[:, 1:] - psi[:, :-1]) / dx
        lap = torch.zeros_like(psi)
        lap[:, 1:-1] = (fluss[:, 1:] - fluss[:, :-1]) / dx
        s = psi.real ** 2 + psi.imag ** 2
        return lap - (1.0 - 2.0 * s + 1.5 * s * s) * psi

    n_schritte = int(round(t_end / dt))
    alle = int(round(t_mess / dt))
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
    t = torch.arange(daten.shape[0], dtype=F64, device=DEV) * t_mess
    return t, daten


# ---------------------------------------------------------------- Auswertehilfen

def linfit(t, y, t0, t1):
    """Gerade y = k0 + k1 (t - t_anfang) auf [t0, t1]; y: (M, B). Rueckgabe Steigung (B,) und Achsenabschnitt (B,)."""
    wahl = (t >= t0 - 1e-9) & (t <= t1 + 1e-9)
    ts, ys = t[wahl], y[wahl]
    a_mat = torch.stack([torch.ones_like(ts), ts - ts[0]], dim=1)
    koef = torch.linalg.lstsq(a_mat, ys).solution
    return koef[1], koef[0]


def l3_quote(fein, grob):
    """Latte L3: |Effekt fein| / |fein - grob|; bestanden ab 5."""
    diff = abs(fein - grob)
    return abs(fein) / diff if diff > 0 else float("inf")


def zahl(z, stellen=4):
    if z is None:
        return "-"
    if isinstance(z, float) and not math.isfinite(z):
        return str(z)
    return f"{z:.{stellen}g}"


# ---------------------------------------------------------------- Test 1: Chemie 1, Elektronegativitaet

def test1(p, kurz):
    """Zwei ruhende Baelle, links omega^2 = 0,8 (klein), rechts 0,6 (gross), Abstand d; Ladung links/rechts ueber t.

    Anfangsphase phi0 des rechten Balls 0, pi/2, pi, 3pi/2 (Josephson-Probe); Spiegel und gleiche omega als Gegenprobe.
    Trennpunkt fest bei x = 0 (Mitte der Startorte, Punkt zur Haelfte je Seite). Verschiebung z = (dQ_gross - dQ_klein)/2,
    unempfindlich gegen symmetrischen Abstrahlverlust; berichtet wird dQ_klein = -z (negativ: der kleine Ball gibt ab)."""
    T = 400.0 * (0.1 if kurz else 1.0)
    abstaende = [8.0, 10.0, 12.0]
    phasen = [0.0, 0.5 * math.pi, math.pi, 1.5 * math.pi]
    laeufe = []
    for d in abstaende:
        for ph in phasen:
            laeufe.append({"d": d, "links": 0.80, "rechts": 0.60, "phi0": ph, "art": "klein-gross"})
        laeufe.append({"d": d, "links": 0.60, "rechts": 0.80, "phi0": 0.0, "art": "spiegel"})
        laeufe.append({"d": d, "links": 0.80, "rechts": 0.80, "phi0": 0.0, "art": "gleich-0.8"})
        laeufe.append({"d": d, "links": 0.60, "rechts": 0.60, "phi0": 0.0, "art": "gleich-0.6"})
    stufen = {}
    for stufe, dx, dt in STUFEN:
        x = gitter(dx)
        psi, vel = stapel(len(laeufe), x)
        for n, r in enumerate(laeufe):
            a, b = ball(p, iw_von(r["links"]), x, -0.5 * r["d"])
            c, e = ball(p, iw_von(r["rechts"]), x, 0.5 * r["d"], theta=r["phi0"])
            psi[n] = a + c
            vel[n] = b + e
        innen = x.abs() < X_INNEN
        halbe = 0.5 * (x == 0).to(F64)                          # Trennpunkt x = 0 zaehlt je zur Haelfte
        links = ((x < 0) & innen).to(F64) + halbe
        rechts = ((x > 0) & innen).to(F64) + halbe

        def messen(psi, vel):
            s = s_von(psi)
            rho = rho_von(psi, vel)
            x_l = (x * s * links).sum(1) / (s * links).sum(1).clamp(min=1e-300)
            x_r = (x * s * rechts).sum(1) / (s * rechts).sum(1).clamp(min=1e-300)
            return torch.stack([(rho * links).sum(1) * dx, (rho * rechts).sum(1) * dx, rho.sum(1) * dx,
                                x_l, x_r], dim=1)

        t0 = uhr()
        t, daten = entwickeln(psi, vel, x, dx, dt, T, messen)
        sek = uhr() - t0
        q_l, q_r, q_box, x_l, x_r = daten.unbind(dim=2)
        ab, spaet = t >= T / 8.0, t >= T / 2.0
        zeilen = []
        for n, r in enumerate(laeufe):
            z_links = 0.5 * ((q_r[:, n] - q_r[0, n]) - (q_l[:, n] - q_l[0, n]))   # Verschiebung nach rechts
            dq = z_links if r["art"] == "spiegel" else -z_links                  # dQ_klein (bei gleich: dQ_links)
            y = dq[ab] - dq[ab].mean()
            spek = torch.fft.rfft(y).abs()
            frq = torch.fft.rfftfreq(y.shape[0], d=T_MEAS, dtype=F64, device=DEV)
            k = int(spek[1:].argmax()) + 1
            zeilen.append({**r, "q_links_0": q_l[0, n].item(), "q_rechts_0": q_r[0, n].item(),
                           "mittel_dq": dq[spaet].mean().item(),
                           "amplitude_dq": 0.5 * (dq[ab].max() - dq[ab].min()).item(),
                           "trend_dq": linfit(t, dq.unsqueeze(1), T / 8.0, T)[0][0].item(),
                           "periode": (1.0 / frq[k]).item(),
                           "abstand_ende": (x_r[-1, n] - x_l[-1, n]).item(),
                           "q_box_verlust": (1.0 - q_box[-1, n] / q_box[0, n]).item()})
        stufen[stufe] = {"sekunden": sek, "laeufe": zeilen,
                         "reihen": {"t": t[::5].tolist(), "q_links": q_l[::5].T.tolist()}}
    # Zusammenfassung je Abstand
    zusammen = []
    for d in abstaende:
        z = {"d": d}
        for stufe in stufen:
            ls = [r for r in stufen[stufe]["laeufe"] if r["d"] == d]
            m = [r["mittel_dq"] for r in ls if r["art"] == "klein-gross"]
            amp = sum(r["amplitude_dq"] for r in ls if r["art"] == "klein-gross") / 4.0
            spiegel = [r for r in ls if r["art"] == "spiegel"][0]
            gleich = [r for r in ls if r["art"].startswith("gleich")]
            z[stufe] = {
                "mittel_je_phase": m,                                      # phi0 = 0, pi/2, pi, 3pi/2
                "phasenmittel": sum(m) / 4.0,                              # intrinsischer Anteil
                "josephson_cos": -0.5 * (m[0] - m[2]),                     # m(phi0) ~ C - A cos phi0 + B sin phi0
                "josephson_sin": 0.5 * (m[1] - m[3]),
                "amplitude_mittel": amp,
                "periode_phi0_0": ls[0]["periode"],
                "spiegel_minus_phi0_0": spiegel["mittel_dq"] - m[0],
                "gleich_max_betrag": max(abs(g["mittel_dq"]) for g in gleich),
                "abstand_ende_min": min(r["abstand_ende"] for r in ls if r["art"] == "klein-gross"),
                "gleich_abstand_ende": [g["abstand_ende"] for g in gleich],
                "q_klein_0": ls[0]["q_links_0"],
            }
        f = z["fein"]
        pm, amp = f["phasenmittel"], f["amplitude_mittel"]
        if abs(pm) >= 0.2 * amp:
            z["urteil"] = "Nettofluss klein->gross (H)" if pm < 0 else "Nettofluss gross->klein (gegen H)"
        else:
            z["urteil"] = "kein Nettofluss: Pendeln, Richtung folgt der Anfangsphase (Josephson)"
        z["verschmolzen"] = f["abstand_ende_min"] < 0.5 * d
        z["L3_phasenmittel"] = l3_quote(pm, z["grob"]["phasenmittel"])
        z["L3_mittel_phi0_0"] = l3_quote(f["mittel_je_phase"][0], z["grob"]["mittel_je_phase"][0])
        zusammen.append(z)
    text = ["Test 1, Chemie 1 (Elektronegativitaet): omega^2 = 0,8 links (klein), 0,6 rechts (gross); T = " + zahl(T),
            "Laufzeit [s]: " + ", ".join(f"{s} {stufen[s]['sekunden']:.1f}" for s in stufen),
            "d | mittleres dQ_klein je phi0 = 0, pi/2, pi, 3pi/2 (fein) | Phasenmittel | Amplitude | Periode | "
            "Josephson cos/sin | Spiegel-Diff | gleich max | L3 | Urteil"]
    for z in zusammen:
        f = z["fein"]
        text.append(f"  {z['d']:4.1f} | " + ", ".join(zahl(m) for m in f["mittel_je_phase"])
                    + f" | {zahl(f['phasenmittel'])} | {zahl(f['amplitude_mittel'])} | {zahl(f['periode_phi0_0'])}"
                    + f" | {zahl(f['josephson_cos'])}/{zahl(f['josephson_sin'])} | {zahl(f['spiegel_minus_phi0_0'])}"
                    + f" | {zahl(f['gleich_max_betrag'])} | {zahl(z['L3_phasenmittel'])}, {zahl(z['L3_mittel_phi0_0'])}"
                    + f" | {z['urteil']}{' (verschmolzen)' if z['verschmolzen'] else ''}")
    text.append("  Q_klein(0) = " + zahl(zusammen[0]["fein"]["q_klein_0"], 6)
                + "; Vorhersage Periode 2 pi/(omega1 - omega2) = " + zahl(2.0 * math.pi / (math.sqrt(0.8) - math.sqrt(0.6))))
    return {"test": "t1", "T": T, "laeufe": laeufe, "stufen": stufen, "zusammen": zusammen}, "\n".join(text)


# ---------------------------------------------------------------- Test 2: Chemie 2/3, Bindungskurve und Morse

def morse_fit(d, e):
    """E = c0 + c1 u + c2 u^2, u = exp(-a (d - d_min)), a im Raster; D = c1^2/(4 c2), d0 = d_min + ln(-c1/(2 c2))/a."""
    a_raster = torch.linspace(0.05, 3.0, 2951, dtype=F64, device=DEV)
    u = torch.exp(-a_raster.unsqueeze(1) * (d - d.min()).unsqueeze(0))
    a_mat = torch.stack([torch.ones_like(u), u, u * u], dim=2)
    y = e.unsqueeze(0).unsqueeze(2).expand(a_raster.shape[0], -1, 1).contiguous()
    koef = torch.linalg.lstsq(a_mat, y).solution[:, :, 0]
    rms = ((a_mat @ koef.unsqueeze(2))[:, :, 0] - e.unsqueeze(0)).pow(2).mean(1).sqrt()
    k = int(rms.argmin())
    c0, c1, c2 = koef[k].tolist()
    a = a_raster[k].item()
    if c2 <= 0.0 or c1 >= 0.0:
        return {"gueltig": False, "a": a, "c": [c0, c1, c2], "rms": rms[k].item()}
    D = c1 * c1 / (4.0 * c2)
    return {"gueltig": True, "D": D, "a": a, "d0": d.min().item() + math.log(-c1 / (2.0 * c2)) / a,
            "E_unendlich": c0, "rms": rms[k].item(), "rms_zu_D": rms[k].item() / D, "a_am_rand": k in (0, 2950)}


def expo_fit(d, e):
    """ln|E| = ln C - kappa d."""
    a_mat = torch.stack([torch.ones_like(d), d], dim=1)
    koef = torch.linalg.lstsq(a_mat, torch.log(e.abs()).unsqueeze(1)).solution[:, 0]
    return {"C": math.exp(koef[0].item()), "kappa": -koef[1].item()}


def interpolieren(proben, ziele):
    """Lineare Interpolation von (d, E)-Proben (nach d sortiert) an den Zielabstaenden; None ausserhalb der Proben."""
    aus = []
    for z in ziele:
        wert = None
        for (da, ea), (db, eb) in zip(proben[:-1], proben[1:]):
            if da <= z <= db and db > da:
                wert = ea + (z - da) / (db - da) * (eb - ea)
                break
        aus.append(wert)
    return aus


def test2(p, kurz):
    """E(d) eines Paars omega^2 = 0,7 bei fester Ladung je Ball, Delta phi = 0 (symmetrisch) und pi (antisymmetrisch).

    Version 2 (30.09.2026, nach dem Abbruch "Relaxation instabil" der Version 1 auf der .69).
    Relaxation mit gedaempfter Dynamik (Verlet, Daempfung gamma) des Funktionals bei fester Gesamtladung Q = 2 q:
        E_Q[phi] = Q^2 / (4 N) + Int phi_x^2 + Int U(phi^2),  N = Int phi^2,  omega = Q / (2 N).
    Die Spiegelsymmetrie phi(-x) = +-phi(x) haelt die Ladung je Ball fest.
    Neu in Version 2:
      - Punktzwang in der Mitte statt Schwerpunktzwang: symmetrisch phi(0) = c, antisymmetrisch phi(+-dx) = +-s dx.
        Der Schwerpunktzwang von Version 1 wirkte mit dem Hebel (x - X) bis an den Boxrand. Bei Anziehung konnte das
        Paar verschmelzen und den Schwerpunkt mit wenig weit aussen geparkter Ladung halten; dieses Aussenfeld wuchs
        exponentiell bis zum Ueberlauf. Der Punktzwang wirkt nur in der Mitte und laesst kein Ausweichen zu.
      - c und s kommen aus der Summe zweier Baelle bei d_start; drei symmetrische Laeufe mit c ueber dem Scheitel des
        verschmolzenen Balls und ein freier Lauf (verschmilzt, Minimum) ergaenzen die Kurve.
      - Anfangsfeld auf N = 2 N1 normiert (omega = omega_1 < 1 am Start; vorher bis omega = 8 bei gegenphasig kleinem d).
      - Laeufe, deren Feld nach aussen laeuft (|phi| > 1e-6 bei |x| > 80), die nicht endlich werden oder deren
        omega >= 0,999 erreicht, werden auf den letzten guten Stand eingefroren und als "ungebunden" gefuehrt,
        nicht gefittet. Kein Abbruch des ganzen Tests mehr.
    Gemessen wird d = 2 X (X = Schwerpunkt von phi^2 auf x > 0) im Endzustand; E an den Sollabstaenden wird zwischen
    den gebundenen Laeufen linear interpoliert. Nullpunkt: dasselbe Paar bei d = 40."""
    w2 = 0.70
    iw = iw_von(w2)
    d_start = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0]
    d_soll = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 10.0, 12.0]
    tau_end = 600.0 * (0.1 if kurz else 1.0)
    gamma, omega_grenze, fern_grenze = 1.0, 0.999, 1e-6
    laeufe = []
    for dp in (0.0, math.pi):
        for d in d_start + [40.0]:
            laeufe.append({"dphi": dp, "d_start": d, "zwang": "mitte", "c_vorgabe": None})
    for c in (0.95, 1.05, 1.2):
        laeufe.append({"dphi": 0.0, "d_start": 2.6, "zwang": "mitte", "c_vorgabe": c})
    laeufe.append({"dphi": 0.0, "d_start": 2.6, "zwang": "frei", "c_vorgabe": None})
    stufen = {}
    for stufe, dx, dt in STUFEN:
        x = gitter(dx)
        i0 = int(round(L_BOX / dx))
        f1 = profil_werte(p, iw, x)[0].unsqueeze(0)
        w, g, v, q = energien(f1, [w2], dx)
        e1, q1, n1 = (w + g + v).item(), q.item(), (f1 * f1).sum().item() * dx
        Q = 2.0 * q1
        sym = [r["dphi"] == 0.0 for r in laeufe]
        vz = spalte([1.0 if s_ else -1.0 for s_ in sym])
        phi = torch.stack([profil_werte(p, iw, x - 0.5 * r["d_start"])[0]
                           + (1.0 if s_ else -1.0) * profil_werte(p, iw, x + 0.5 * r["d_start"])[0]
                           for r, s_ in zip(laeufe, sym)])
        phi = phi * torch.sqrt(2.0 * n1 / ((phi * phi).sum(1, keepdim=True) * dx))    # N = 2 N1, omega = omega_1
        fest = torch.zeros_like(phi)
        zwang_wert = []
        for n, (r, s_) in enumerate(zip(laeufe, sym)):
            if r["zwang"] == "frei":
                zwang_wert.append(None)
            elif s_:
                if r["c_vorgabe"] is not None:
                    phi[n, i0] = r["c_vorgabe"]
                fest[n, i0] = 1.0
                zwang_wert.append(phi[n, i0].item())
            else:
                fest[n, i0 - 1] = 1.0
                fest[n, i0 + 1] = 1.0
                zwang_wert.append(phi[n, i0 + 1].item() / dx)
        los = 1.0 - fest
        rechts = (x > 0).to(F64)
        aussen = (x.abs() > 80.0).to(F64)

        def spiegeln(y):
            return 0.5 * (y + vz * torch.flip(y, dims=[1]))

        def kraft(phi):
            nn = (phi * phi).sum(1, keepdim=True) * dx
            fluss = (phi[:, 1:] - phi[:, :-1]) / dx
            lap = torch.zeros_like(phi)
            lap[:, 1:-1] = (fluss[:, 1:] - fluss[:, :-1]) / dx
            s = phi * phi
            fk = lap - (1.0 - 2.0 * s + 1.5 * s * s) * phi + (Q / (2.0 * nn)) ** 2 * phi   # = -(1/2) dE_Q/dphi
            return spiegeln(fk) * los                                                      # Zwangspunkte fest

        def messen(phi):
            nn = (phi * phi).sum(1) * dx
            s = phi * phi
            e = Q * Q / (4.0 * nn) + ((phi[:, 1:] - phi[:, :-1]) / dx).pow(2).sum(1) * dx + u_von(s).sum(1) * dx
            return e, (x * s * rechts).sum(1) / (s * rechts).sum(1), Q / (2.0 * nn)

        t0 = uhr()
        aktiv = torch.ones(len(laeufe), 1, dtype=F64, device=DEV)
        vel = torch.zeros_like(phi)
        gut = phi.clone()
        fk = kraft(phi)
        n_schritte, alle = int(round(tau_end / dt)), int(round(1.0 / dt))
        reihe = []
        for n in range(1, n_schritte + 1):
            vel = vel + (0.5 * dt) * (fk - gamma * vel)
            phi = phi + dt * vel
            fk = kraft(phi) * aktiv
            vel = (vel + (0.5 * dt) * (fk - gamma * vel)) * aktiv
            if n % alle == 0:
                e, X, om = messen(phi)
                fern = (phi.abs() * aussen).max(1).values
                gesund = torch.isfinite(phi).all(1) & torch.isfinite(e) & (fern <= fern_grenze) & (om < omega_grenze)
                aktiv = aktiv * gesund.to(F64).unsqueeze(1)
                phi = torch.where(aktiv > 0, phi, gut)                 # eingefroren: letzter guter Stand
                vel = torch.where(aktiv > 0, vel, torch.zeros_like(vel))
                fk = torch.where(aktiv > 0, fk, torch.zeros_like(fk))
                gut = phi.clone()
                e, X, om = messen(phi)
                fern = (phi.abs() * aussen).max(1).values
                reihe.append(torch.stack([e, X, om, fern, aktiv[:, 0]], dim=1))
        daten = torch.stack(reihe)                                     # (M, B, 5)
        sek = uhr() - t0
        e_end, x_end, om_end, fern_end, ak_end = daten[-1].unbind(dim=1)
        i80 = int(0.8 * (daten.shape[0] - 1))
        zeilen = []
        for n, r in enumerate(laeufe):
            zeilen.append({**r, "zwang_wert": zwang_wert[n], "E": e_end[n].item(), "d_ist": 2.0 * x_end[n].item(),
                           "omega_ende": om_end[n].item(), "fernfeld": fern_end[n].item(),
                           "gebunden": bool(ak_end[n].item() > 0),
                           "konvergenz_dE": abs(e_end[n].item() - daten[i80, n, 0].item())})
        ref = {z["dphi"]: z["E"] for z in zeilen if z["d_start"] > 39.0 and z["gebunden"]}
        for z in zeilen:
            z["E_minus_2E1"] = z["E"] - 2.0 * e1
            z["E_int"] = z["E"] - ref[z["dphi"]] if z["dphi"] in ref else z["E"] - 2.0 * e1
        proben = {}
        for key, dp in (("0", 0.0), ("pi", math.pi)):
            proben[key] = sorted((z["d_ist"], z["E_int"]) for z in zeilen
                                 if z["dphi"] == dp and z["gebunden"] and z["d_start"] < 39.0)
        stufen[stufe] = {"sekunden": sek, "E1": e1, "q1": q1, "N1": n1, "laeufe": zeilen,
                         "referenz_vorhanden": {("0" if k == 0.0 else "pi"): True for k in ref},
                         "proben": proben, "kurve": {k: interpolieren(proben[k], d_soll) for k in proben}}
    # Auswertung je Stufe
    kappa = math.sqrt(1.0 - w2)
    b0 = math.sqrt(2.0 * w2 - 1.0)
    for stufe in stufen:
        st = stufen[stufe]
        pr0 = [pp for pp in st["proben"]["0"] if pp[0] < 14.0]
        prp = [pp for pp in st["proben"]["pi"] if pp[0] < 14.0]
        aus = {}
        if len(pr0) >= 4:
            aus["morse_0"] = morse_fit(torch.tensor([pp[0] for pp in pr0], dtype=F64, device=DEV),
                                       torch.tensor([pp[1] for pp in pr0], dtype=F64, device=DEV))
        else:
            aus["morse_0"] = {"gueltig": False, "grund": "weniger als 4 gebundene Punkte"}
        for key, pr in (("0", pr0), ("pi", prp)):
            weit = [pp for pp in pr if pp[0] >= 6.0]
            aus["asymptotik_" + key] = (expo_fit(torch.tensor([pp[0] for pp in weit], dtype=F64, device=DEV),
                                                 torch.tensor([pp[1] for pp in weit], dtype=F64, device=DEV))
                                        if len(weit) >= 2 else None)
        k0, kp = st["kurve"]["0"], st["kurve"]["pi"]
        aus["verhaeltnis_pi_zu_0"] = {str(d): (kp[i] / k0[i] if (k0[i] is not None and kp[i] is not None
                                                                and k0[i] != 0.0) else None)
                                      for i, d in enumerate(d_soll) if d >= 6.0}
        if pr0:
            i_min = min(range(len(pr0)), key=lambda i: pr0[i][1])
            aus["minimum"] = {"d_ist": pr0[i_min][0], "E_int": pr0[i_min][1], "index": i_min}
            drei = pr0[max(i_min - 1, 0):i_min + 2]
            if (0 < i_min < len(pr0) - 1
                    and min(drei[1][0] - drei[0][0], drei[2][0] - drei[1][0]) > 1e-6):   # drei verschiedene d
                dd = torch.tensor([pp[0] for pp in drei], dtype=F64, device=DEV)
                ee = torch.tensor([pp[1] for pp in drei], dtype=F64, device=DEV)
                a_mat = torch.stack([torch.ones_like(dd), dd, dd * dd], dim=1)
                c = torch.linalg.lstsq(a_mat, ee.unsqueeze(1)).solution[:, 0].tolist()
                if c[2] != 0.0:
                    aus["minimum"].update({"kruemmung": 2.0 * c[2], "d_parabel": -c[1] / (2.0 * c[2]),
                                           "omega_vib": math.sqrt(max(2.0 * c[2], 0.0) / (0.5 * st["E1"]))})
        else:
            aus["minimum"] = None
        m = aus["morse_0"]
        if m.get("gueltig"):
            m["omega_vib"] = math.sqrt(2.0 * m["D"] * m["a"] ** 2 / (0.5 * st["E1"]))
            m["schwanz_koeff"] = 2.0 * m["D"] * math.exp(m["a"] * m["d0"])
        werte_pi = [w_ for w_ in kp if w_ is not None]
        aus["null_alle_negativ"] = all(pp[1] < 0 for pp in pr0)
        d_min = aus["minimum"]["d_ist"] if aus["minimum"] else 0.0
        aus["null_negativ_ab_minimum"] = all(pp[1] < 0 for pp in pr0 if pp[0] >= d_min)
        aus["pi_alle_positiv"] = all(pp[1] > 0 for pp in prp)
        aus["pi_monoton_fallend"] = all(werte_pi[i] > werte_pi[i + 1] for i in range(len(werte_pi) - 1))
        aus["referenz_d40"] = {("0" if z["dphi"] == 0.0 else "pi"): z["E_minus_2E1"]
                               for z in st["laeufe"] if z["d_start"] > 39.0}
        geb = [z for z in st["laeufe"] if z["gebunden"]]
        aus["max_konvergenz_dE"] = max(z["konvergenz_dE"] for z in geb) if geb else None
        aus["ungebunden"] = [[z["dphi"], z["d_start"], z["c_vorgabe"], z["omega_ende"]]
                             for z in st["laeufe"] if not z["gebunden"]]
        st["auswertung"] = aus
    fein, grob = stufen["fein"], stufen["grob"]
    l3 = {key: [l3_quote(a, b) if (a is not None and b is not None) else None
                for a, b in zip(fein["kurve"][key], grob["kurve"][key])] for key in ("0", "pi")}
    l3_werte = [w_ for key in l3 for w_ in l3[key] if w_ is not None]
    vorhersage = {"kappa": kappa, "C_asymptotik": 16.0 * kappa ** 3 / b0}
    text = ["Test 2 (Version 2), Chemie 2/3 (Bindungskurve): Paar omega^2 = 0,7, feste Ladung je Ball, Punktzwang in "
            "der Mitte, tau = " + zahl(tau_end),
            "Laufzeit [s]: " + ", ".join(f"{s} {stufen[s]['sekunden']:.1f}" for s in stufen)
            + f"; E1 fein = {fein['E1']:.8f}, q1 fein = {fein['q1']:.8f}",
            "d_soll | E_int(0) fein | E_int(pi) fein | E_int(0) grob | E_int(pi) grob | L3 0 | L3 pi"]
    for i, d in enumerate(d_soll):
        text.append(f"  {d:5.2f} | {zahl(fein['kurve']['0'][i], 6)} | {zahl(fein['kurve']['pi'][i], 6)} | "
                    f"{zahl(grob['kurve']['0'][i], 6)} | {zahl(grob['kurve']['pi'][i], 6)} | "
                    f"{zahl(l3['0'][i])} | {zahl(l3['pi'][i])}")
    text.append("Laeufe (fein): dphi/pi, d_start, Zwangwert | d_ist | E_int | omega | gebunden | Konvergenz dE")
    for z in fein["laeufe"]:
        text.append(f"  {z['dphi'] / math.pi:.0f}, {z['d_start']:.1f}, {zahl(z['zwang_wert'])} | {z['d_ist']:.4f} | "
                    f"{z['E_int']:.6e} | {z['omega_ende']:.5f} | {z['gebunden']} | {z['konvergenz_dE']:.1e}")
    a = fein["auswertung"]
    text += [f"Morse (Delta phi = 0, fein): {json.dumps(a['morse_0'])}",
             f"Asymptotik d >= 6: 0: {json.dumps(a['asymptotik_0'])}; pi: {json.dumps(a['asymptotik_pi'])}; "
             f"Vorhersage kappa = {kappa:.4f}, C = 16 kappa^3/b0 = {vorhersage['C_asymptotik']:.4f}",
             f"E_int(pi)/E_int(0) bei d >= 6: {json.dumps(a['verhaeltnis_pi_zu_0'])}",
             f"Minimum (Delta phi = 0): {json.dumps(a['minimum'])}",
             f"Vorzeichen: 0 alle negativ {a['null_alle_negativ']} (ab Minimum {a['null_negativ_ab_minimum']}), "
             f"pi alle positiv {a['pi_alle_positiv']}, "
             f"pi monoton fallend {a['pi_monoton_fallend']}; Referenz d = 40 (E - 2 E1): {json.dumps(a['referenz_d40'])}",
             f"Kontrollen: max Konvergenz dE (gebundene) {zahl(a['max_konvergenz_dE'])}; ungebunden (dphi, d_start, "
             f"c, omega): {json.dumps(a['ungebunden'])}; L3 min {zahl(min(l3_werte) if l3_werte else None)}",
             f"Morse grob zum Vergleich: {json.dumps(grob['auswertung']['morse_0'])}"]
    return {"test": "t2", "version": 2, "tau_end": tau_end, "gamma": gamma, "omega_grenze": omega_grenze,
            "fern_grenze": fern_grenze, "d_soll": d_soll, "laeufe": laeufe, "stufen": stufen, "l3": l3,
            "vorhersage": vorhersage}, "\n".join(text)


# ---------------------------------------------------------------- Test 3: Chemie 7, Aktivierungsenergie (Stoesse)

def test3(p, kurz):
    """Zwei gleiche Baelle omega^2 = 0,7 bei -+8, Geschwindigkeit +-v, Phase des rechten Balls dphi.

    Ausgang: getrennt (Abstand der Halbraum-Schwerpunkte von |psi|^2 nach der engsten Annaeherung > 30),
    verschmolzen (sonst, und am Ende mehr als die Haelfte der Ladung in |x| < 6), sonst gebunden/unklar.
    Bei dphi = +-pi/2 zusaetzlich durchgelaufen/abgeprallt aus der Relativphase am Maximum jeder Haelfte:
    Beim Abprallen bleibt sie bei dphi, beim Durchlaufen wechselt ihr Vorzeichen (Boost-Phasen heben sich auf).
    dphi = -pi/2 ist das Spiegelbild von +pi/2 (Symmetrie-Gegenprobe)."""
    w2 = 0.70
    iw = iw_von(w2)
    T = 800.0 * (0.1 if kurz else 1.0)
    x0, sep_getrennt, r_zentral = 8.0, 30.0, 6.0
    vs = [0.05, 0.1, 0.2, 0.3, 0.45, 0.6]
    phasen = [0.0, 0.5 * math.pi, math.pi, -0.5 * math.pi]
    laeufe = [{"dphi": ph, "v": v} for ph in phasen for v in vs]
    stufen = {}
    for stufe, dx, dt in STUFEN:
        x = gitter(dx)
        psi, vel = stapel(len(laeufe), x)
        for n, r in enumerate(laeufe):
            a, b = ball(p, iw, x, -x0, v=r["v"])
            c, e = ball(p, iw, x, x0, v=-r["v"], theta=r["dphi"])
            psi[n] = a + c
            vel[n] = b + e
        innen = x.abs() < X_INNEN
        rechts, links = ((x > 0) & innen).to(F64), ((x < 0) & innen).to(F64)
        zentral = (x.abs() < r_zentral).to(F64)
        zeilen_idx = torch.arange(len(laeufe), device=DEV)

        def messen(psi, vel):
            s = s_von(psi)
            rho = rho_von(psi, vel)
            x_r = (x * s * rechts).sum(1) / (s * rechts).sum(1).clamp(min=1e-300)
            x_l = (x * s * links).sum(1) / (s * links).sum(1).clamp(min=1e-300)
            p_r = psi[zeilen_idx, (s * rechts).argmax(1)]
            p_l = psi[zeilen_idx, (s * links).argmax(1)]
            return torch.stack([x_l, x_r, (rho * links).sum(1) * dx, (rho * rechts).sum(1) * dx,
                                (rho * zentral).sum(1) * dx, (rho * innen.to(F64)).sum(1) * dx,
                                torch.angle(p_r * p_l.conj()), s.max(1).values], dim=1)

        t0 = uhr()
        t, daten = entwickeln(psi, vel, x, dx, dt, T, messen)
        sek = uhr() - t0
        x_l, x_r, q_l, q_r, q_z, q_in, relphase, s_max = [y.cpu() for y in daten.unbind(dim=2)]
        tc = t.cpu()
        zeilen = []
        for n, r in enumerate(laeufe):
            sp = x_r[:, n] - x_l[:, n]
            i_min = int(sp.argmin())
            z = {**r, "sep_min": sp[i_min].item(), "t_sep_min": tc[i_min].item()}
            nach = (sp[i_min:] > sep_getrennt).nonzero()
            if nach.shape[0] > 0:
                i_g = i_min + int(nach[0, 0])
                i_a = max(i_g - 20, i_min)
                z.update({"klasse": "getrennt", "t_getrennt": tc[i_g].item(),
                          "v_aus": ((sp[i_g] - sp[i_a]) / (2.0 * (tc[i_g] - tc[i_a]).clamp(min=1e-9))).item(),
                          "relphase_aus": relphase[i_g, n].item(),
                          "ladungsasymmetrie": ((q_r[i_g, n] - q_l[i_g, n]) / (q_r[i_g, n] + q_l[i_g, n])).item()})
                if abs(abs(r["dphi"]) - 0.5 * math.pi) < 1e-9:
                    wechsel = math.sin(z["relphase_aus"]) * math.copysign(1.0, r["dphi"]) < 0.0
                    z["klasse"] = "durchgelaufen" if wechsel else "abgeprallt"
            else:
                anteil = (q_z[-1, n] / q_in[-1, n]).item()
                z.update({"zentralanteil_ende": anteil, "sep_ende": sp[-1].item(),
                          "klasse": "verschmolzen" if (anteil > 0.5 and sp[-1].item() < 10.0) else "gebunden/unklar"})
            z["s_max_ende"] = s_max[-1, n].item()
            zeilen.append(z)
        stufen[stufe] = {"sekunden": sek, "laeufe": zeilen,
                         "reihen": {"t": tc[::4].tolist(), "sep": (x_r - x_l)[::4].T.tolist()}}
    # Phasendiagramm und Barriere (fein), L3 als Zahl abweichender Zellen und Aenderung von v_aus
    diagramm, barriere = {}, {}
    fz, gz = stufen["fein"]["laeufe"], stufen["grob"]["laeufe"]
    for ph in phasen:
        key = f"{ph / math.pi:+.2f} pi"
        zs = [z for z in fz if z["dphi"] == ph]
        diagramm[key] = [z["klasse"] for z in zs]
        versch = [z["v"] for z in zs if z["klasse"] == "verschmolzen"]
        barriere[key] = {"kleinstes_v_verschmolzen": min(versch) if versch else None,
                         "groesstes_v_verschmolzen": max(versch) if versch else None}
    abweichend = sum(1 for a, b in zip(fz, gz) if a["klasse"] != b["klasse"])
    dv = [abs(a["v_aus"] - b["v_aus"]) for a, b in zip(fz, gz) if "v_aus" in a and "v_aus" in b]
    spiegel = sum(1 for a, b in zip([z for z in fz if z["dphi"] == phasen[1]], [z for z in fz if z["dphi"] == phasen[3]])
                  if a["klasse"] != b["klasse"])
    text = ["Test 3, Chemie 7 (Stoesse): omega^2 = 0,7, Start -+8, T = " + zahl(T),
            "Laufzeit [s]: " + ", ".join(f"{s} {stufen[s]['sekunden']:.1f}" for s in stufen),
            "Phasendiagramm (fein), Spalten v = " + ", ".join(str(v) for v in vs)]
    for key, kl in diagramm.items():
        text.append(f"  dphi = {key}: " + ", ".join(kl) + f" | Barriere {json.dumps(barriere[key])}")
    text.append("Einzelwerte (fein): dphi/pi, v | Klasse | sep_min | v_aus | Relphase aus | Ladungsasymmetrie")
    for z in fz:
        text.append(f"  {z['dphi'] / math.pi:+.2f}, {z['v']:.2f} | {z['klasse']} | {z['sep_min']:.3f} | "
                    f"{zahl(z.get('v_aus'))} | {zahl(z.get('relphase_aus'))} | {zahl(z.get('ladungsasymmetrie'))}")
    text.append(f"L3: abweichende Klassen fein/grob {abweichend} von {len(fz)}; max |v_aus fein - grob| "
                f"{zahl(max(dv) if dv else None)}; Spiegelprobe +pi/2 gegen -pi/2: {spiegel} abweichende Klassen")
    return {"test": "t3", "T": T, "laeufe": laeufe, "stufen": stufen, "diagramm": diagramm, "barriere": barriere,
            "L3_abweichende_klassen": abweichend, "spiegel_abweichend": spiegel}, "\n".join(text)


# ---------------------------------------------------------------- Test 4: Chemie 15, Redox ueber Bruecke

def exponentiell(werte):
    """Fester Massstab: Betraege fallen je Bruecke, alle Verhaeltnisse unter 0,5, Spreizung max/min hoechstens 2."""
    b = [abs(w) for w in werte]
    r = [b[i + 1] / b[i] if b[i] > 0 else float("nan") for i in range(len(b) - 1)]
    endlich = all(math.isfinite(x) and x > 0 for x in r)
    spreizung = max(r) / min(r) if endlich else float("nan")
    return {"verhaeltnisse": r, "spreizung": spreizung,
            "exponentiell": endlich and all(x < 0.5 for x in r) and spreizung <= 2.0}


def test4(p, kurz):
    """Kette Spender (0,85) - n Bruecken (0,7) - Empfaenger (0,6), Abstand a = 10, n = 0 bis 3.

    Varianten: alle gleichphasig (D0, Hauptmessung laut Auftrag), Spender um pi/2 voraus (D90), ohne Spender (Kontrolle).
    Anfangssteigung = Geradenfit der Empfaengerladung (Zelle x > x_A - a/2) auf [2, 15]; Spendereffekt = Differenz
    zum Lauf ohne Spender."""
    T = 400.0 * (0.1 if kurz else 1.0)
    a_abst, t_a, t_b = 10.0, 2.0, 15.0                      # Fenster auch im Rauchtest (T = 40) gleich
    varianten = ("D0", "D90", "ohneD")
    laeufe = [{"n": n, "art": art} for n in range(4) for art in varianten]
    stufen = {}
    for stufe, dx, dt in STUFEN:
        x = gitter(dx)
        psi, vel = stapel(len(laeufe), x)
        grenzen_a, grenzen_d = [], []
        for i, r in enumerate(laeufe):
            n = r["n"]
            orte = [(k - 0.5 * (n + 1)) * a_abst for k in range(n + 2)]
            omegas = [0.85] + [0.70] * n + [0.60]
            for k in range(n + 2):
                if k == 0 and r["art"] == "ohneD":
                    continue
                th = 0.5 * math.pi if (k == 0 and r["art"] == "D90") else 0.0
                b, bt = ball(p, iw_von(omegas[k]), x, orte[k], theta=th)
                psi[i] += b
                vel[i] += bt
            grenzen_a.append(orte[-1] - 0.5 * a_abst)
            grenzen_d.append(orte[0] + 0.5 * a_abst)
        innen = x.abs() < X_INNEN
        akz = ((x > spalte(grenzen_a)) & innen).to(F64)
        spe = ((x < spalte(grenzen_d)) & innen).to(F64)

        def messen(psi, vel):
            rho = rho_von(psi, vel)
            return torch.stack([(rho * akz).sum(1) * dx, (rho * spe).sum(1) * dx,
                                (rho * innen.to(F64)).sum(1) * dx], dim=1)

        t0 = uhr()
        t, daten = entwickeln(psi, vel, x, dx, dt, T, messen)
        sek = uhr() - t0
        dqa = daten[:, :, 0] - daten[0, :, 0]
        dqd = daten[:, :, 1] - daten[0, :, 1]
        steig = linfit(t, dqa, t_a, t_b)[0]
        i100 = int(round(min(100.0, T) / T_MEAS))
        zeilen = []
        for i, r in enumerate(laeufe):
            j = laeufe.index({"n": r["n"], "art": "ohneD"})
            diff = dqa[:, i] - dqa[:, j]
            zeilen.append({**r, "q_A0": daten[0, i, 0].item(), "steigung_A": steig[i].item(),
                           "steigung_spendereffekt": linfit(t, diff.unsqueeze(1), t_a, t_b)[0][0].item(),
                           "spendereffekt_t100": diff[i100].item(), "spendereffekt_T": diff[-1].item(),
                           "dQ_A_max": dqa[:, i].abs().max().item(),
                           "dQ_A_mittel_spaet": dqa[:, i][t >= T / 2].mean().item(),
                           "dQ_D_mittel_spaet": dqd[:, i][t >= T / 2].mean().item(),
                           "q_verlust": (1.0 - daten[-1, i, 2] / daten[0, i, 2]).item()})
        stufen[stufe] = {"sekunden": sek, "laeufe": zeilen,
                         "reihen": {"t": t[::2].tolist(), "dQ_A": dqa[::2].T.tolist()}}
    urteile = {}
    for stufe in stufen:
        zs = stufen[stufe]["laeufe"]
        u = {}
        for art in ("D0", "D90"):
            roh = [z["steigung_A"] for z in zs if z["art"] == art]
            eff = [z["steigung_spendereffekt"] for z in zs if z["art"] == art]
            u[art] = {"steigung_A": roh, "exp_roh": exponentiell(roh), "spendereffekt": eff,
                      "exp_spendereffekt": exponentiell(eff)}
        urteile[stufe] = u
    l3 = [l3_quote(a["steigung_A"], b["steigung_A"])
          for a, b in zip(stufen["fein"]["laeufe"], stufen["grob"]["laeufe"]) if a["art"] != "ohneD"]
    l3_eff = [l3_quote(a["steigung_spendereffekt"], b["steigung_spendereffekt"])
              for a, b in zip(stufen["fein"]["laeufe"], stufen["grob"]["laeufe"]) if a["art"] != "ohneD"]
    text = ["Test 4, Chemie 15 (Redox ueber Bruecke): D 0,85 - n x B 0,7 - A 0,6, Abstand 10, Steigung auf ["
            + zahl(t_a) + ", " + zahl(t_b) + "], T = " + zahl(T),
            "Laufzeit [s]: " + ", ".join(f"{s} {stufen[s]['sekunden']:.1f}" for s in stufen),
            "n | Variante | Steigung dQ_A | Spendereffekt-Steigung | Spendereffekt t=100 | dQ_A max | dQ_A Mittel spaet"]
    for z in stufen["fein"]["laeufe"]:
        text.append(f"  {z['n']} | {z['art']} | {z['steigung_A']:.4e} | {z['steigung_spendereffekt']:.4e} | "
                    f"{z['spendereffekt_t100']:.4e} | {z['dQ_A_max']:.4e} | {z['dQ_A_mittel_spaet']:.4e}")
    for art, u in urteile["fein"].items():
        text.append(f"  {art}: roh {json.dumps(u['exp_roh'])}; Spendereffekt {json.dumps(u['exp_spendereffekt'])}")
    text.append(f"L3 (|fein|/|fein - grob|): Steigung min {zahl(min(l3))}, Spendereffekt min {zahl(min(l3_eff))}")
    return {"test": "t4", "T": T, "fenster": [t_a, t_b], "laeufe": laeufe, "stufen": stufen, "urteile": urteile,
            "l3_steigung": l3, "l3_spendereffekt": l3_eff}, "\n".join(text)


# ---------------------------------------------------------------- Test 5: Chemie 14 (Zufallskarte), Q gegen Anti-Q

def test5(p, kurz):
    """Ball exp(-i omega t) bei -d/2, Anti-Ball exp(+i omega t) bei +d/2 (Phase theta), omega^2 = 0,7, in Ruhe.

    Betragsladung Q_abs = Int |rho| in |x| < X_INNEN; t50 = erste Zeit, zu der das gleitende Maximum (20 Zeiteinheiten)
    von Q_abs unter die Haelfte faellt (Ladungstausch laesst Q_abs kurz einbrechen). Kontrolle: Ball-Ball-Paar."""
    w2 = 0.70
    iw = iw_von(w2)
    T, t_mess = 1000.0 * (0.1 if kurz else 1.0), 0.5
    abstaende = [3.0, 5.0, 8.0, 12.0]
    arten = [("anti", 0.0), ("anti", math.pi), ("gleich", 0.0), ("gleich", math.pi)]
    laeufe = [{"d": d, "art": art, "theta": th} for d in abstaende for (art, th) in arten]
    stufen = {}
    for stufe, dx, dt in STUFEN:
        x = gitter(dx)
        q1 = energien(profil_werte(p, iw, x)[0].unsqueeze(0), [w2], dx)[3].item()
        psi, vel = stapel(len(laeufe), x)
        for n, r in enumerate(laeufe):
            a, b = ball(p, iw, x, -0.5 * r["d"])
            c, e = ball(p, iw, x, 0.5 * r["d"], theta=r["theta"], anti=(r["art"] == "anti"))
            psi[n] = a + c
            vel[n] = b + e
        innen = x.abs() < X_INNEN
        innen_f, innen_m = innen.to(F64), innen[1:-1]
        rechts, links = ((x > 0) & innen).to(F64), ((x < 0) & innen).to(F64)

        def messen(psi, vel):
            s = s_von(psi)
            rho = rho_von(psi, vel)
            mitte = s[:, 1:-1]
            klumpen = ((mitte > s[:, :-2]) & (mitte >= s[:, 2:]) & (mitte > 0.05) & innen_m).sum(1).to(F64)
            return torch.stack([(rho.abs() * innen_f).sum(1) * dx, (rho.clamp(min=0.0) * innen_f).sum(1) * dx,
                                (rho.clamp(max=0.0) * innen_f).sum(1) * dx, (rho * rechts).sum(1) * dx,
                                (rho * links).sum(1) * dx, (e_dichte(psi, vel, dx) * innen_f).sum(1) * dx,
                                s.max(1).values, klumpen], dim=1)

        t0 = uhr()
        t, daten = entwickeln(psi, vel, x, dx, dt, T, messen, t_mess=t_mess)
        sek = uhr() - t0
        tc = t.cpu()
        q_abs, q_plus, q_minus, q_r, q_l, e_in, s_max, klumpen = [y.cpu() for y in daten.unbind(dim=2)]
        breite = int(round(20.0 / t_mess))
        gm = q_abs.clone()
        for k in range(1, breite + 1):
            gm[k:] = torch.maximum(gm[k:], q_abs[:-k])

        def erste(maske):
            idx = maske.nonzero()
            return tc[idx[0, 0]].item() if idx.shape[0] > 0 else None

        spaet = tc >= T - 200.0
        zeilen = []
        for n, r in enumerate(laeufe):
            q0 = q_abs[0, n].item()
            qr = q_r[:, n][spaet]
            tausch = int(((qr[1:] * qr[:-1]) < 0).sum())
            z = {**r, "q_abs0": q0, "q_abs0_zu_2q": q0 / (2.0 * q1),
                 "t50_roh": erste(q_abs[:, n] <= 0.5 * q0), "t50": erste((gm[:, n] <= 0.5 * q0) & (tc >= 20.0)),
                 "t10": erste((gm[:, n] <= 0.9 * q0) & (tc >= 20.0)),
                 "rest_q_abs": q_abs[-1, n].item() / q0, "rest_q_abs_glatt": gm[-1, n].item() / q0,
                 "q_gesamt_0": (q_plus[0, n] + q_minus[0, n]).item(), "q_gesamt_ende": (q_plus[-1, n] + q_minus[-1, n]).item(),
                 "rest_e": e_in[-1, n].item() / e_in[0, n].item(), "s_max_ende": s_max[-1, n].item(),
                 "klumpen_ende": int(klumpen[-1, n]), "vorzeichenwechsel_q_rechts_spaet": tausch}
            if z["s_max_ende"] < 0.02:
                z["endzustand"] = "Strahlung, nichts Lokalisiertes"
            elif z["klumpen_ende"] >= 1 and tausch >= 4:
                z["endzustand"] = "Restgebilde mit Ladungstausch"
            elif z["klumpen_ende"] >= 1:
                z["endzustand"] = "Restball/Restbaelle"
            else:
                z["endzustand"] = "unklar"
            zeilen.append(z)
        stufen[stufe] = {"sekunden": sek, "q1": q1, "laeufe": zeilen,
                         "reihen": {"t": tc[::4].tolist(), "q_abs": q_abs[::4].T.tolist(), "q_rechts": q_r[::4].T.tolist()}}
    fz, gz = stufen["fein"]["laeufe"], stufen["grob"]["laeufe"]
    l3 = [l3_quote(1.0 - a["rest_q_abs_glatt"], 1.0 - b["rest_q_abs_glatt"]) for a, b in zip(fz, gz)]
    text = ["Test 5, Chemie 14 (Q gegen Anti-Q): omega^2 = 0,7, T = " + zahl(T),
            "Laufzeit [s]: " + ", ".join(f"{s} {stufen[s]['sekunden']:.1f}" for s in stufen),
            "d | Art | theta/pi | Q_abs0/2q | t10 | t50 (glatt) | t50 roh | Rest Q_abs (glatt) | Rest E | Q ges. Ende | "
            "Klumpen | Wechsel | Endzustand | L3"]
    for z, q in zip(fz, l3):
        text.append(f"  {z['d']:4.1f} | {z['art']} | {z['theta'] / math.pi:.0f} | {z['q_abs0_zu_2q']:.4f} | "
                    f"{zahl(z['t10'])} | {zahl(z['t50'])} | {zahl(z['t50_roh'])} | {zahl(z['rest_q_abs_glatt'])} | "
                    f"{zahl(z['rest_e'])} | {zahl(z['q_gesamt_ende'])} | {z['klumpen_ende']} | "
                    f"{z['vorzeichenwechsel_q_rechts_spaet']} | {z['endzustand']} | {zahl(q)}")
    return {"test": "t5", "T": T, "t_mess": t_mess, "laeufe": laeufe, "stufen": stufen, "l3": l3}, "\n".join(text)


# ---------------------------------------------------------------- Wellen 5: nur Papierprobe (Dispersion)

def landau(S, t_lauf=400.0):
    """Bogoliubov-Zweige des homogenen Hintergrunds psi = sqrt(S) exp(-i omega t), omega^2 = U'(S):
    Omega^2 = [B -+ sqrt(B^2 - 4 k^2 (k^2 + m2))] / 2, B = 2 k^2 + m2 + 4 omega^2, m2 = 2 U''(S) S = -4 S + 6 S^2.
    Unterer Zweig stabil geschrieben: Omega_-^2 = 2 k^2 (k^2 + m2) / (B + Wurzel)."""
    k = torch.linspace(1e-4, 4.0, 40000, dtype=F64, device=DEV)
    om2 = 1.0 - 2.0 * S + 1.5 * S * S
    m2 = 2.0 * (3.0 * S - 2.0) * S
    b = 2.0 * k * k + m2 + 4.0 * om2
    xm = 2.0 * k * k * (k * k + m2) / (b + torch.sqrt(b * b - 4.0 * k * k * (k * k + m2)))
    instabil, stabil = xm < 0, xm > 0
    wachstum = torch.sqrt(-xm[instabil]).max().item() if bool(instabil.any()) else 0.0
    return {"S": S, "omega_bg": math.sqrt(om2), "beta_2SUpp": m2,
            "stabil": not bool(instabil.any()), "wachstumsrate_max": wachstum,
            "k_instabil_bis": k[instabil].max().item() if bool(instabil.any()) else 0.0,
            "verstaerkung_ueber_t_lauf": math.exp(wachstum * t_lauf),
            "v_c_landau_raster": (torch.sqrt(xm[stabil]) / k[stabil]).min().item(),
            "c_s": math.sqrt(m2 / (m2 + 4.0 * om2)) if m2 > 0 else None,
            "gegenpunkt_2_minus_2S": 2.0 - 2.0 * S}


def test6():
    """Wellen 5 ist im Ein-Feld-Modell nicht umsetzbar (PLAN.md): keine Zeitentwicklung, nur die Dispersionstabelle."""
    zeilen = [landau(S) for S in (1e-3, 2e-3, 1e-2, 0.1, 0.5, 2.0 / 3.0, 0.7, 0.8, 1.0)]
    text = ["Wellen 5, Papierprobe (keine Messung): homogener Hintergrund, S | omega_bg | beta | stabil | "
            "Wachstumsrate | k_instabil bis | Verstaerkung in 400 | v_c (Raster) | c_s | Gegenpunkt 2 - 2S"]
    for z in zeilen:
        text.append(f"  {z['S']:.4g} | {z['omega_bg']:.4f} | {z['beta_2SUpp']:.4g} | {z['stabil']} | "
                    f"{z['wachstumsrate_max']:.4g} | {z['k_instabil_bis']:.4g} | {z['verstaerkung_ueber_t_lauf']:.4g} | "
                    f"{z['v_c_landau_raster']:.4g} | {zahl(z['c_s'])} | {z['gegenpunkt_2_minus_2S']:.4g}")
    return {"test": "t6", "art": "Papierprobe", "zeilen": zeilen}, "\n".join(text)


# ---------------------------------------------------------------- Hauptprogramm

def ablegen(out, name, ausgabe, text):
    with open(os.path.join(out, name + "_ergebnis.json"), "w") as fh:
        json.dump(ausgabe, fh, indent=1)
    with open(os.path.join(out, name + "_bericht.txt"), "w") as fh:
        fh.write(text + "\n")
    print(text, flush=True)


def main():
    ap = argparse.ArgumentParser(description="Runde 3, 1D-Tests: Chemie 1, 2/3, 7, 15, 14; Wellen 5 nur Papierprobe")
    ap.add_argument("befehl", choices=["profil", "t1", "t2", "t3", "t4", "t5", "t6", "alle"])
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "ausgabe"))
    ap.add_argument("--profil", default=None, help="Profil-Zwischenspeicher (Standard: OUT/profile_r3.pt)")
    ap.add_argument("--kurz", action="store_true", help="Rauchtest: Lauf- und Relaxationszeiten x 0,1")
    args = ap.parse_args()
    if not torch.cuda.is_available():
        raise SystemExit("Kein CUDA-Geraet: Abbruch (kein CPU-Ausweg).")
    os.makedirs(args.out, exist_ok=True)
    geraet = torch.cuda.get_device_name(0)
    meta = {"geraet": geraet, "torch": torch.__version__, "kurz": args.kurz}
    endung = "_kurz" if args.kurz else ""
    print(f"R3-1D {args.befehl} Start {jetzt()} auf {geraet}, torch {torch.__version__}, kurz = {args.kurz}", flush=True)
    if args.befehl in ("t6", "alle"):
        ausgabe, text = test6()
        ablegen(args.out, "t6" + endung, {**ausgabe, **meta, "ende": jetzt()}, text)
        if args.befehl == "t6":
            return
    pfad = args.profil or os.path.join(args.out, "profile_r3.pt")
    p = profile_holen(pfad)
    k0 = {"grob": k0_pruefen(p, DX), "fein": k0_pruefen(p, DX / 2.0)}
    k0_max = max(k0["grob"] + k0["fein"])
    zeilen = [f"Profile: {pfad}, geschossen {p['erzeugt']} in {p['schiessen_s']:.1f} s",
              "omega2 | f0^2 Schuss | f0^2 Anker | Klammer | K0 grob | K0 fein"]
    for iw, w2 in enumerate(p["omega2"]):
        zeilen.append(f"  {w2:.2f} | {p['f0'][iw, 0].item() ** 2:.12f} | {1.0 - math.sqrt(2.0 * w2 - 1.0):.12f} | "
                      f"{p['klammer'][iw, 0].item():.1e} | {k0['grob'][iw]:.1e} | {k0['fein'][iw]:.1e}")
    zeilen.append(f"K0 (max |f_Schuss - f_Anker| <= {TOL_PROFIL}): "
                  + ("bestanden" if k0_max <= TOL_PROFIL else "NICHT bestanden") + f", max {k0_max:.2e}")
    ablegen(args.out, "profil" + endung, {"k0": k0, "k0_max": k0_max, **meta}, "\n".join(zeilen))
    if k0_max > 10.0 * TOL_PROFIL:
        raise SystemExit("K0 weit verfehlt: Profil unbrauchbar, keine Tests.")
    tests = {"t1": test1, "t2": test2, "t3": test3, "t4": test4, "t5": test5}
    wahl = list(tests) if args.befehl == "alle" else ([] if args.befehl == "profil" else [args.befehl])
    for name in wahl:
        start = jetzt()
        t0 = uhr()
        ausgabe, text = tests[name](p, args.kurz)
        sek = uhr() - t0
        kopf = f"{name}: Start {start}, Ende {jetzt()}, Dauer {sek:.1f} s, {geraet}, K0 max {k0_max:.1e}"
        ablegen(args.out, name + endung, {**ausgabe, **meta, "start": start, "ende": jetzt(), "dauer_s": sek,
                                           "k0_max": k0_max}, kopf + "\n" + text)


if __name__ == "__main__":
    main()
