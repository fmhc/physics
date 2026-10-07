#!/usr/bin/env python3
"""R4-CB, Runde 4 (runden-v3): sechs 1D-Tests aus Chemie und Biologie mit Q-Baellen plus Zufallskarte Artbildung.

Explorativ. Ohne Testlauf abgegeben (auf dem Laptop gilt das Interpreterverbot). Plan, Aufrufe, Laufzeiten und
Vorhersagen stehen in PLAN.md daneben. Nur CUDA, float64 (psi als complex128); ohne CUDA bricht das Programm ab.

Modell (wie RUNDE-01/qg1/qg1.py ohne Feld, A = B = C = 1):
    L = |psi_t|^2 - |psi_x|^2 - U(S) - V(x) S,   S = |psi|^2,   U = S - S^2 + S^3/2,
    psi_tt = psi_xx - (U'(S) + V(x)) psi.  V(x) ist nur in der Chromatographie ungleich null (kleines Massenpotential).
Ladungsdichte rho = 2 Im(psi conj(psi_t)), Ladung eines Balls Q = 2 omega Int f^2 (wie qg1).

Uebernommen aus qg1.py (unveraendert): rhs, rk4, schiessen, profil_bahn, anker_wgv, Gitter, dx/dt (grob 0,1/0,05,
fein 0,05/0,025), Velocity-Verlet mit quadratischer Daempfungsschicht (sigma0 = 1, Breite 40), Messabstand 1.
Geaendert: Boxlaenge je Test (gitter und profil_gitter haben dafuer einen Parameter). Anfangsdaten kommen aus dem
analytischen 1D-Anker (qg1: Schuss = Anker auf 1,2e-10), weil verschobene und Lorentz-geboostete Baelle das Profil an
beliebigen Stellen brauchen. Der 1D-Schuss bleibt als Kontrolle K0 (Unterbefehl profil).
Artbildung: radiales Schiessen (d = 3, m = 0; d = 2, m = 0, 1, 2) nach demselben Einschachtelungsschema, aber mit
logarithmischem Parameter und Integration der Abweichung vom Gipfel f_t (sonst waeren duenne Waende in float64 nicht
erreichbar).

Aufruf:  python chemie_bio.py <test> [--out ORDNER]
    test: profil | katalyse | kette | chromatographie | neuron | wunde | nerv | artbildung | rauch
    rauch: alle Tests ausser profil mit kurzer Zeit und kleinem Schiessen, nur Durchlaufprobe.
"""
import argparse
import datetime
import json
import math
import os
import time
import traceback

import torch

DEV = torch.device("cuda")
F64 = torch.float64
C128 = torch.complex128

# ---- aus qg1.py uebernommen (Werte unveraendert) ----
SIGMA0 = 1.0             # Daempfung am Rand
DX, DT = 0.1, 0.05       # grobe Aufloesung; die feine halbiert beide
T_MEAS = 1.0             # Messabstand
H_ODE = 0.01             # Schrittweite beim 1D-Schiessen (Kontrolle K0)
X_ODE = 80.0             # Schiesslaenge 1D
N_KAND, RUNDEN = 4096, 4 # Kandidaten je Einschachtelungsrunde, Zahl der Runden (1D)
SCHWANZ = 1e-3           # ab f < SCHWANZ * f_max: exponentieller Schwanz statt Schiessbahn
TOL_PROFIL = 1e-6        # K0: max |f_Schuss - f_Anker|
L_BOX_QG1 = 120.0        # qg1: Box [-120, 120], Daempfung ab |x| = 80
# ---- neu in R4-CB ----
SCHWAMM = 40.0           # Breite der Daempfungsschicht (qg1: 120 - 80)
L3_FAKTOR = 5.0          # L3: Effekt mindestens fuenfmal groesser als die Aenderung fein gegen grob
S_KLUMPEN = 0.05         # Klumpen = zusammenhaengender Bereich mit S > 0,05
T_RAUCH = 20.0           # Laufzeit im Rauchtest


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    torch.cuda.synchronize()
    return time.perf_counter()


# ================================================================ aus qg1.py: 1D-Profil durch Schiessen (Kontrolle)

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
    """Zentralwert f(0) je omega durch Einschachteln (qg1, unveraendert)."""
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
    """Schiessbahn f(j h) ab f(0) = f0 bis unter SCHWANZ * f0 (qg1, unveraendert)."""
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


def gitter(dx, l_box=L_BOX_QG1):
    """Symmetrisches Gitter x_i = (i - i0) dx auf [-L, L]; x = 0 liegt genau auf einem Punkt."""
    i0 = int(round(l_box / dx))
    return (torch.arange(2 * i0 + 1, dtype=F64, device=DEV) - i0) * dx


def profil_gitter(bahn, j_cut, a0, dx, l_box=L_BOX_QG1):
    """Geschossenes Profil auf dem Gitter (qg1; nur l_box als Parameter)."""
    m = int(round(dx / H_ODE))
    i0 = int(round(l_box / dx))
    k = (torch.arange(2 * i0 + 1, device=DEV) - i0).abs()
    j = (k * m).unsqueeze(0).repeat(bahn.shape[0], 1)
    innen = bahn.gather(1, j.clamp(max=bahn.shape[1] - 1))
    f_cut = bahn.gather(1, j_cut)
    aussen = f_cut * torch.exp(-torch.sqrt(a0) * (j - j_cut).to(F64) * H_ODE)
    f = torch.where(j < j_cut, innen, aussen)
    f[:, 0] = 0.0
    f[:, -1] = 0.0
    return f


def anker_wgv(w2):
    """Geschlossene 1D-Werte: I = sqrt(2) arcosh(1/b0), W = omega^2 I, G = sqrt(a0)/2 - b0^2 I/4, V = W + G."""
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    integral = math.sqrt(2.0) * math.acosh(1.0 / b0)
    w = w2 * integral
    g = math.sqrt(a0) / 2.0 - b0 * b0 * integral / 4.0
    return w, g, w + g


# ================================================================ gemeinsame 1D-Bausteine

def anker(w2, y):
    """Analytischer 1D-Anker f^2 = 2 a0 / (1 + b0 cosh(2 sqrt(a0) y)) und f' an beliebigen Stellen y.

    w2 als Zahl oder als Tensor, der mit y broadcastet (z. B. (B, 1) gegen (B, N))."""
    w2 = torch.as_tensor(w2, dtype=F64, device=DEV)
    a0 = 1.0 - w2
    b0 = torch.sqrt(2.0 * w2 - 1.0)
    k = torch.sqrt(a0)
    arg = 2.0 * k * y
    nenner = 1.0 + b0 * torch.cosh(arg)
    f = torch.sqrt(2.0 * a0 / nenner)
    fs = -f * b0 * k * torch.sinh(arg) / nenner
    return f, fs


def anker_qe(w2):
    """Ladung Q = 2 omega Int f^2 und Energie E = W + G + V des ruhenden Ankers (geschlossen)."""
    w, g, v = anker_wgv(w2)
    return 2.0 * math.sqrt(w2) * w / w2, w + g + v


def ball(x, w2, x0, v=0.0, phase=0.0):
    """Lorentz-geboosteter Anker-Ball: psi(x, 0) und psi_t(x, 0).

    Exakte Loesung psi = f(gamma (x - x0 - v t)) exp(-i omega gamma (t - v (x - x0)) + i phase)."""
    om = math.sqrt(w2)
    gam = 1.0 / math.sqrt(1.0 - v * v)
    y = gam * (x - x0)
    f, fs = anker(w2, y)
    e = torch.polar(torch.ones_like(y), om * gam * v * (x - x0) + phase)
    return f * e, torch.complex(-v * gam * fs, -om * gam * f) * e


def entwickeln(psi, vel, x, dx, dt, t_end, l_box, messen, pot=None):
    """Velocity-Verlet wie qg1.entwickeln (A = B = C = 1), optional Massenpotential pot (B, N).

    messen(psi, vel) liefert (B, k) je Messzeit. Rueckgabe: t (M,), daten (M, B, k), psi und vel am Ende."""
    sigma = SIGMA0 * ((x.abs() - (l_box - SCHWAMM)).clamp(min=0.0) / SCHWAMM) ** 2
    psi = psi.clone()
    vel = vel.clone()
    for z in (psi, vel):                         # Dirichlet-Rand
        z[:, 0] = 0.0
        z[:, -1] = 0.0

    def kraft(p):
        fluss = (p[:, 1:] - p[:, :-1]) / dx
        lap = torch.zeros_like(p)
        lap[:, 1:-1] = (fluss[:, 1:] - fluss[:, :-1]) / dx
        s = p.real ** 2 + p.imag ** 2
        u1 = 1.0 - 2.0 * s + 1.5 * s * s
        if pot is not None:
            u1 = u1 + pot
        return lap - u1 * p

    n_schritte = int(round(t_end / dt))
    alle = int(round(T_MEAS / dt))
    reihe = [messen(psi, vel)]
    kr = kraft(psi)
    for n in range(1, n_schritte + 1):
        vel = vel + (0.5 * dt) * (kr - sigma * vel)
        psi = psi + dt * vel
        kr = kraft(psi)
        vel = vel + (0.5 * dt) * (kr - sigma * vel)
        if n % alle == 0:
            reihe.append(messen(psi, vel))
    daten = torch.stack(reihe)
    if not bool(torch.isfinite(daten).all()):
        raise RuntimeError("nicht endliche Messwerte: Lauf instabil")
    t = torch.arange(daten.shape[0], dtype=F64, device=DEV) * T_MEAS
    return t, daten, psi, vel


def klumpen(p, q, x, dx, x_innen, n_top, s_schwelle=S_KLUMPEN):
    """Zahl der Klumpen (zusammenhaengend S > s_schwelle, |x| < x_innen) und die n_top groessten Klumpenladungen."""
    s = p.real ** 2 + p.imag ** 2
    rho = 2.0 * (p * q.conj()).imag
    maske = (s > s_schwelle) & (x.abs() < x_innen)
    start = maske.clone()
    start[:, 1:] = maske[:, 1:] & ~maske[:, :-1]
    marke = torch.cumsum(start.to(torch.int64), dim=1) * maske.to(torch.int64)
    lad = torch.zeros(p.shape[0], p.shape[1] + 1, dtype=F64, device=DEV)
    lad.scatter_add_(1, marke, rho * dx)
    top = torch.topk(lad[:, 1:], n_top, dim=1).values
    return marke.max(dim=1).values.to(F64), top


def verfolger(x, dx, r_win, x_start):
    """Messung fuer einen Ball je Lauf, Fenster +-r_win um den vorigen Schwerpunkt (wie qg1).

    Spalten: X, Q im Fenster, Breite, max S im Fenster, Q in der Box."""
    zust = {"x_alt": x_start}

    def messen(p, q):
        s = p.real ** 2 + p.imag ** 2
        rho = 2.0 * (p * q.conj()).imag
        fen = ((x - zust["x_alt"]).abs() < r_win).to(F64)
        qw = (rho * fen).sum(1) * dx
        qs = qw.clamp(min=1e-30)
        X = (x * rho * fen).sum(1) * dx / qs
        b2 = ((x - X.unsqueeze(1)) ** 2 * rho * fen).sum(1) * dx / qs
        smax = (s * fen).max(dim=1).values
        zust["x_alt"] = X.unsqueeze(1)
        return torch.stack([X, qw, torch.sqrt(b2.clamp(min=0.0)), smax, rho.sum(1) * dx], dim=1)

    return messen


def energie(p, q, dx):
    """Energie je Lauf: Int |psi_t|^2 + |psi_x|^2 + U(S)."""
    s = p.real ** 2 + p.imag ** 2
    grad = ((p[:, 1:] - p[:, :-1]).abs() / dx) ** 2
    return ((q.abs() ** 2 + s - s * s + 0.5 * s ** 3).sum(1) + grad.sum(1)) * dx


def erste_zeit(t, y, schwelle):
    """Erste Messzeit mit y >= schwelle (y: (M,)); None, wenn nie."""
    ueber = y >= schwelle
    if not bool(ueber.any()):
        return None
    return t[torch.argmax(ueber.to(torch.int64))].item()


def dauerhaft_unter(t, y, schwelle):
    """Erste Zeit, ab der y (M, B) bis zum Ende unter schwelle (B,) bleibt; inf, wenn y am Ende darueber liegt."""
    m = y.shape[0]
    ueber = y > schwelle.unsqueeze(0)
    idx = torch.arange(m, device=DEV).unsqueeze(1).expand(m, y.shape[1])
    letzte = torch.where(ueber, idx, torch.full_like(idx, -1)).max(dim=0).values
    t_ab = t[(letzte + 1).clamp(max=m - 1)]
    return torch.where(letzte + 1 < m, t_ab, torch.full_like(t_ab, float("inf")))


def durchgang(t, X, schwelle):
    """Erste Zeit, zu der X (M, B) die Schwelle erreicht, linear interpoliert; inf, wenn nie."""
    ueber = X >= schwelle
    hat = ueber.any(dim=0)
    i = torch.argmax(ueber.to(torch.int64), dim=0)
    i1 = i.clamp(min=1)
    b = torch.arange(X.shape[1], device=DEV)
    x0, x1 = X[i1 - 1, b], X[i1, b]
    nenner = torch.where((x1 - x0).abs() > 1e-12, x1 - x0, torch.ones_like(x0))
    anteil = ((schwelle - x0) / nenner).clamp(0.0, 1.0)
    tc = t[i1 - 1] + anteil * (t[i1] - t[i1 - 1])
    tc = torch.where(i == 0, torch.zeros_like(tc), tc)
    return torch.where(hat, tc, torch.full_like(tc, float("inf")))


def endlich(v):
    return v if (v is not None and math.isfinite(v)) else None


def l3_zeile(l3):
    return ("L3 (fein gegen grob): " + ("bestanden" if l3["bestanden"] else "NICHT bestanden") + "; "
            + ", ".join(f"{k} = {v:.3e}" if isinstance(v, float) else f"{k} = {v}"
                        for k, v in l3.items() if k != "bestanden"))


# ================================================================ Test 1: Katalyse (Chemie 8)

KAT_W2 = 0.7
KAT_V = [0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6]
KAT_DPHI = {"pi": math.pi, "3pi/4": 0.75 * math.pi}
KAT_VAR = ["ohne", "bruecke", "sperre", "nur_AC"]
KAT_X0, KAT_T, KAT_L = 12.0, 300.0, 120.0


def test_katalyse(dx, dt, rauch):
    """A (Phase 0, +v) bei -12 gegen B (Phase dphi, -v) bei +12; C ruhend bei 0 mit Phase dphi/2 (bruecke) oder
    dphi/2 + pi (sperre); nur_AC ohne B als Kontrolle. Ausgang: groesster Klumpen im Mittel der letzten 50 Zeiten."""
    x = gitter(dx, KAT_L)
    laeufe = [{"dphi": dn, "variante": var, "v": v} for dn in KAT_DPHI for var in KAT_VAR for v in KAT_V]
    psi = torch.zeros(len(laeufe), x.shape[0], dtype=C128, device=DEV)
    vel = torch.zeros_like(psi)
    for n, r in enumerate(laeufe):
        dphi = KAT_DPHI[r["dphi"]]
        teile = [(-KAT_X0, r["v"], 0.0)]
        if r["variante"] != "nur_AC":
            teile.append((KAT_X0, -r["v"], dphi))
        if r["variante"] in ("bruecke", "nur_AC"):
            teile.append((0.0, 0.0, 0.5 * dphi))
        elif r["variante"] == "sperre":
            teile.append((0.0, 0.0, 0.5 * dphi + math.pi))
        for x0, v, ph in teile:
            a, b = ball(x, KAT_W2, x0, v, ph)
            psi[n] += a
            vel[n] += b
    x_innen = KAT_L - SCHWAMM - 5.0

    def messen(p, q):
        n_kl, top = klumpen(p, q, x, dx, x_innen, 3)
        return torch.cat([n_kl.unsqueeze(1), top], dim=1)

    t_end = T_RAUCH if rauch else KAT_T
    t, daten, _, _ = entwickeln(psi, vel, x, dx, dt, t_end, KAT_L, messen)
    q0, _ = anker_qe(KAT_W2)
    spaet = t >= t_end - 50.0 - 1e-9
    q_top = daten[spaet][:, :, 1:4].mean(dim=0) / q0
    for n, r in enumerate(laeufe):
        r["q_klumpen_end"] = q_top[n].tolist()
        r["n_klumpen_end"] = int(daten[-1, n, 0].item())
        r["verschmolzen"] = r["q_klumpen_end"][0] >= 1.5
        r["alle_drei"] = r["q_klumpen_end"][0] >= 2.5
    schwellen = {}
    for dn in KAT_DPHI:
        for var in KAT_VAR:
            teil = [r for r in laeufe if r["dphi"] == dn and r["variante"] == var]
            vs = [r["v"] for r in teil if r["verschmolzen"]]
            schwellen[dn + " " + var] = {"v_schwelle": min(vs) if vs else None,
                                         "muster": "".join("x" if r["verschmolzen"] else "." for r in teil)}
    return {"t_end": t_end, "q0": q0, "laeufe": laeufe, "schwellen": schwellen}


def l3_katalyse(erg):
    g, f = erg["grob"]["laeufe"], erg["fein"]["laeufe"]
    aend = max(abs(a["q_klumpen_end"][0] - b["q_klumpen_end"][0]) for a, b in zip(g, f))
    idx = {(r["dphi"], r["variante"], r["v"]): r["q_klumpen_end"][0] for r in f}
    effekt = max(abs(idx[(dn, "bruecke", v)] - idx[(dn, "ohne", v)]) for dn in KAT_DPHI for v in KAT_V)
    gleich = sum(1 for a, b in zip(g, f) if a["verschmolzen"] == b["verschmolzen"])
    return {"effekt_max_dq1_bruecke_ohne": effekt, "aenderung_max_dq1": aend,
            "bestanden": effekt >= L3_FAKTOR * aend, "klassen_gleich": f"{gleich} von {len(f)}"}


def bericht_katalyse(erg):
    z = [f"Katalyse (Chemie 8): omega^2 = {KAT_W2}, Q0 = {erg['fein']['q0']:.4f}, Start bei -+{KAT_X0}, "
         f"T = {erg['fein']['t_end']}",
         f"  v = {KAT_V}; x = verschmolzen (groesster Klumpen >= 1,5 Q0, Mittel der letzten 50 Zeiteinheiten)"]
    for stufe in ("grob", "fein"):
        for k, s in erg[stufe]["schwellen"].items():
            z.append(f"  {stufe:4s} {k:14s} {s['muster']}   kleinstes v mit Verschmelzung: {s['v_schwelle']}")
    z.append("  fein, groesster Klumpen / Q0 je v:")
    for dn in KAT_DPHI:
        for var in KAT_VAR:
            werte = [r["q_klumpen_end"][0] for r in erg["fein"]["laeufe"] if r["dphi"] == dn and r["variante"] == var]
            z.append(f"    {dn:5s} {var:8s} " + " ".join(f"{w:.2f}" for w in werte))
    z.append("  " + l3_zeile(erg["L3"]))
    return z


# ================================================================ Test 2: Kettenreaktion (Chemie 16)

KET_W2 = 0.7
KET_NPAAR = 5
KET_DIN = [16.0, 20.0, 24.0]
KET_DZUEND = 8.0
KET_ZUSATZ = 4.0         # Abstand zwischen den Paaren = d_in + 4
KET_T, KET_L = 600.0, 180.0
KET_BREITE = 3.0         # Paar gilt als verschmolzen, sobald die Ladungs-RMS-Breite im Paarfenster unter 3 faellt


def test_kette(dx, dt, rauch):
    """Fuenf gleichphasige Paare (Abstand d_in), benachbarte Paare gegenphasig. zuend: Paar 0 mit Abstand 8;
    kalt: alle mit d_in; paar: ein einzelnes Paar (natuerliche Verschmelzungszeit); zuendpaar: einzelnes Paar mit 8."""
    x = gitter(dx, KET_L)
    kk = KET_NPAAR
    laeufe = [{"d_in": d, "art": a} for d in KET_DIN for a in ("zuend", "kalt", "paar")]
    laeufe.append({"d_in": KET_DIN[0], "art": "zuendpaar"})
    nb = len(laeufe)
    psi = torch.zeros(nb, x.shape[0], dtype=C128, device=DEV)
    vel = torch.zeros_like(psi)
    zentren = torch.zeros(nb, kk, dtype=F64, device=DEV)
    halb = torch.zeros(nb, 1, dtype=F64, device=DEV)
    for n, r in enumerate(laeufe):
        abst = 2.0 * r["d_in"] + KET_ZUSATZ
        pk = [(k - 0.5 * (kk - 1)) * abst for k in range(kk)]
        r["zentren"] = pk
        zentren[n] = torch.tensor(pk, dtype=F64, device=DEV)
        halb[n, 0] = 0.5 * abst
        if r["art"] in ("zuend", "kalt"):
            paare = [(pk[k], KET_DZUEND if (k == 0 and r["art"] == "zuend") else r["d_in"], k * math.pi)
                     for k in range(kk)]
        elif r["art"] == "paar":
            paare = [(pk[kk // 2], r["d_in"], 0.0)]
        else:
            paare = [(pk[kk // 2], KET_DZUEND, 0.0)]
        for c, d, ph in paare:
            for sg in (-0.5, 0.5):
                a, b = ball(x, KET_W2, c + sg * d, 0.0, ph)
                psi[n] += a
                vel[n] += b
    q0, _ = anker_qe(KET_W2)
    xv = x.view(1, 1, -1)
    maske = ((xv - zentren.unsqueeze(2)).abs() < halb.unsqueeze(2)).to(F64)          # (B, K, N)

    def messen(p, q):
        rho = (2.0 * (p * q.conj()).imag).unsqueeze(1) * maske
        qk = rho.sum(2) * dx
        qs = qk.clamp(min=1e-30)
        X = (rho * xv).sum(2) * dx / qs
        b2 = (rho * (xv - X.unsqueeze(2)) ** 2).sum(2) * dx / qs
        breite = torch.where(qk > 0.5 * q0, torch.sqrt(b2.clamp(min=0.0)), torch.full_like(qk, 999.0))
        return torch.cat([breite, qk / q0], dim=1)

    t_end = T_RAUCH if rauch else KET_T
    t, daten, _, _ = entwickeln(psi, vel, x, dx, dt, t_end, KET_L, messen)
    fusion = daten[:, :, :kk] < KET_BREITE                                              # (M, B, K)
    hat = fusion.any(dim=0)
    t_fus = t[torch.argmax(fusion.to(torch.int64), dim=0)]
    for n, r in enumerate(laeufe):
        r["t_fusion"] = [t_fus[n, k].item() if bool(hat[n, k]) else None for k in range(kk)]
        r["breite_end"] = daten[-1, n, :kk].tolist()
        r["ladung_end_je_paar"] = daten[-1, n, kk:].tolist()
    ausw = {}
    for d in KET_DIN:
        z, k_, p_ = (next(r for r in laeufe if r["d_in"] == d and r["art"] == a) for a in ("zuend", "kalt", "paar"))
        tz = [t_end + 1.0 if u is None else u for u in z["t_fusion"]]
        tk = [t_end + 1.0 if u is None else u for u in k_["t_fusion"]]
        gez = [tz[k] < 0.8 * tk[k] for k in range(kk)]
        reich = 0
        for k in range(1, kk):
            if not gez[k]:
                break
            reich = k
        abst = 2.0 * d + KET_ZUSATZ
        v_front = abst * reich / (tz[reich] - tz[0]) if (reich >= 1 and tz[reich] > tz[0]) else None
        ausw[str(d)] = {"t_fusion_zuend": z["t_fusion"], "t_fusion_kalt": k_["t_fusion"],
                        "t_fusion_paar_allein": p_["t_fusion"][kk // 2], "gezuendet_paare_1_bis_4": gez[1:],
                        "reichweite_paare": reich, "v_front": v_front}
    return {"t_end": t_end, "laeufe": laeufe, "auswertung": ausw,
            "t_fusion_zuendpaar_allein": laeufe[-1]["t_fusion"][kk // 2]}


def l3_kette(erg):
    t_end = erg["fein"]["t_end"]
    aend, gleich, gesamt = 0.0, 0, 0
    for a, b in zip(erg["grob"]["laeufe"], erg["fein"]["laeufe"]):
        for u, w in zip(a["t_fusion"], b["t_fusion"]):
            gesamt += 1
            gleich += int((u is None) == (w is None))
            if u is not None and w is not None:
                aend = max(aend, abs(u - w))
    effekt = 0.0
    for au in erg["fein"]["auswertung"].values():
        for u, w in zip(au["t_fusion_zuend"][1:], au["t_fusion_kalt"][1:]):
            effekt = max(effekt, abs((t_end if u is None else u) - (t_end if w is None else w)))
    return {"effekt_max_zeitgewinn": effekt, "aenderung_max_fusionszeit": aend,
            "bestanden": effekt >= L3_FAKTOR * aend, "fusion_gleich": f"{gleich} von {gesamt}"}


def bericht_kette(erg):
    f = erg["fein"]
    z = [f"Kettenreaktion (Chemie 16): {KET_NPAAR} Paare, omega^2 = {KET_W2}, Zuendpaar d = {KET_DZUEND}, "
         f"Fusion = RMS-Breite < {KET_BREITE}, T = {f['t_end']}",
         f"  einzelnes Zuendpaar: Fusion bei t = {f['t_fusion_zuendpaar_allein']}"]
    for d, au in f["auswertung"].items():
        z.append(f"  d_in = {d}: einzelnes Paar t = {au['t_fusion_paar_allein']}; "
                 f"zuend {au['t_fusion_zuend']}; kalt {au['t_fusion_kalt']}")
        z.append(f"           gezuendet (Paar 1-4, t_zuend < 0,8 t_kalt): {au['gezuendet_paare_1_bis_4']}, "
                 f"Reichweite {au['reichweite_paare']} Paare, Frontgeschwindigkeit {au['v_front']}")
    z.append("  " + l3_zeile(erg["L3"]))
    return z


# ================================================================ Test 3: Chromatographie (Chemie 20)

CHR_W2 = [0.6, 0.7, 0.8]
CHR_V = 0.3
CHR_START = -60.0
CHR_ZONE = 40.0          # raue Zone |x| < 40, weiche Raender (tanh, Breite 2)
CHR_ELL = 1.0            # Korrelationslaenge: Gaussbuckel im Abstand 1 mit Breite 1
CHR_EPS = [0.01, 0.02, 0.03]
CHR_SEEDS = [1, 2, 3, 4]
CHR_T, CHR_L, CHR_RWIN = 420.0, 120.0, 20.0   # glatt: Austritt bei t = 333, Ende bei x = 66 (Daempfung ab 80)


def zufallspotential(x, eps, seed):
    """V(x) = eps * sum_j a_j exp(-(x - x_j)^2 / 2 ell^2) * Fenster, a_j ~ N(0, 1) aus festem Seed.

    Die 89 Zufallszahlen erzeugt der CPU-Generator (geraeteunabhaengig reproduzierbar); die Funktion ist stetig,
    also auf grobem und feinem Gitter dieselbe."""
    gen = torch.Generator(device="cpu")
    gen.manual_seed(seed)
    xs = torch.arange(-CHR_ZONE - 4.0, CHR_ZONE + 4.0 + 1e-9, CHR_ELL, dtype=F64)
    a = torch.randn(xs.shape[0], generator=gen, dtype=F64)
    xs, a = xs.to(DEV), a.to(DEV)
    eta = (a.view(1, -1) * torch.exp(-(x.view(-1, 1) - xs.view(1, -1)) ** 2 / (2.0 * CHR_ELL ** 2))).sum(1)
    fenster = 0.5 * (torch.tanh((x + CHR_ZONE) / 2.0) - torch.tanh((x - CHR_ZONE) / 2.0))
    return eps * eta * fenster


def test_chromatographie(dx, dt, rauch):
    x = gitter(dx, CHR_L)
    laeufe = []
    for w2 in CHR_W2:
        laeufe.append({"omega2": w2, "eps": 0.0, "seed": 0})
        laeufe += [{"omega2": w2, "eps": e, "seed": s} for e in CHR_EPS for s in CHR_SEEDS]
    nb = len(laeufe)
    psi = torch.zeros(nb, x.shape[0], dtype=C128, device=DEV)
    vel = torch.zeros_like(psi)
    pot = torch.zeros(nb, x.shape[0], dtype=F64, device=DEV)
    for n, r in enumerate(laeufe):
        a, b = ball(x, r["omega2"], CHR_START, CHR_V, 0.0)
        psi[n] = a
        vel[n] = b
        if r["eps"] > 0.0:
            pot[n] = zufallspotential(x, r["eps"], r["seed"])
    innen = x.abs() < CHR_ZONE - 10.0
    pot_rms = pot[:, innen].pow(2).mean(dim=1).sqrt()
    t_end = T_RAUCH if rauch else CHR_T
    x_start = torch.full((nb, 1), CHR_START, dtype=F64, device=DEV)
    t, daten, _, _ = entwickeln(psi, vel, x, dx, dt, t_end, CHR_L, verfolger(x, dx, CHR_RWIN, x_start), pot=pot)
    X, qw = daten[:, :, 0], daten[:, :, 1]
    t_ein, t_aus = durchgang(t, X, -CHR_ZONE), durchgang(t, X, CHR_ZONE)
    for n, r in enumerate(laeufe):
        te, ta = endlich(t_ein[n].item()), endlich(t_aus[n].item())
        r["t_ein"], r["t_aus"] = te, ta
        r["transit"] = ta - te if (te is not None and ta is not None) else None
        r["x_end"] = X[-1, n].item()
        r["reflektiert"] = bool(te is not None and ta is None and r["x_end"] < -CHR_ZONE)
        r["ladungsverlust"] = 1.0 - (qw[-1, n] / qw[0, n]).item()
        r["pot_rms"] = pot_rms[n].item()
    glatt = {r["omega2"]: r["transit"] for r in laeufe if r["eps"] == 0.0}
    for r in laeufe:
        tg = glatt[r["omega2"]]
        r["verzoegerung_rel"] = (r["transit"] - tg) / tg if (r["transit"] is not None and tg) else None
    trennung = {}
    for e in CHR_EPS:
        je_seed = []
        for s in CHR_SEEDS:
            tr = [next(r["transit"] for r in laeufe if r["omega2"] == w and r["eps"] == e and r["seed"] == s)
                  for w in CHR_W2]
            ok = all(v is not None for v in tr)
            je_seed.append({"seed": s, "transit": tr, "trennung_06_08": tr[0] - tr[-1] if ok else None,
                            "ordnung_06_07_08": bool(ok and tr[0] > tr[1] > tr[2])})
        werte = [j["trennung_06_08"] for j in je_seed if j["trennung_06_08"] is not None]
        mittel_verz = {}
        for w in CHR_W2:
            vz = [r["verzoegerung_rel"] for r in laeufe if r["omega2"] == w and r["eps"] == e
                  and r["verzoegerung_rel"] is not None]
            mittel_verz[str(w)] = sum(vz) / len(vz) if vz else None
        trennung[str(e)] = {"je_seed": je_seed, "mittel": sum(werte) / len(werte) if werte else None,
                            "spannweite": (max(werte) - min(werte)) if werte else None,
                            "seeds_in_ordnung": sum(1 for j in je_seed if j["ordnung_06_07_08"]),
                            "mittlere_verzoegerung_rel": mittel_verz,
                            "reflektiert_je_omega2": {str(w): sum(1 for r in laeufe if r["omega2"] == w and r["eps"] == e
                                                                  and r["reflektiert"]) for w in CHR_W2}}
    gw = [glatt[w] for w in CHR_W2 if glatt[w] is not None]
    return {"t_end": t_end, "laeufe": laeufe, "trennung": trennung,
            "transit_glatt": {str(w): glatt[w] for w in CHR_W2},
            "glatt_spannweite": (max(gw) - min(gw)) if len(gw) == len(CHR_W2) else None}


def l3_chromatographie(erg):
    aend = 0.0
    for a, b in zip(erg["grob"]["laeufe"], erg["fein"]["laeufe"]):
        if a["transit"] is not None and b["transit"] is not None:
            aend = max(aend, abs(a["transit"] - b["transit"]))
    eff = [abs(v["mittel"]) for v in erg["fein"]["trennung"].values() if v["mittel"] is not None]
    effekt = max(eff) if eff else 0.0
    gs = erg["fein"]["glatt_spannweite"]
    return {"effekt_max_mittlere_trennung": effekt, "aenderung_max_transit": aend,
            "bestanden": effekt >= L3_FAKTOR * aend, "gegenprobe_glatt_spannweite": gs,
            "gegenprobe_bestanden": bool(gs is not None and L3_FAKTOR * gs <= effekt)}


def bericht_chromatographie(erg):
    f = erg["fein"]
    z = [f"Chromatographie (Chemie 20): v = {CHR_V}, Zone |x| < {CHR_ZONE}, ell = {CHR_ELL}, T = {f['t_end']}",
         f"  glatte Zone (Gegenprobe): Durchlaufzeit je omega^2 {f['transit_glatt']}, Spannweite {f['glatt_spannweite']}"]
    for e, tr in f["trennung"].items():
        z.append(f"  eps = {e}: Trennung t(0,6) - t(0,8) Mittel {tr['mittel']}, Spannweite {tr['spannweite']}, "
                 f"Ordnung 0,6 > 0,7 > 0,8 in {tr['seeds_in_ordnung']} von {len(CHR_SEEDS)} Seeds")
        z.append(f"           mittlere relative Verzoegerung je omega^2: {tr['mittlere_verzoegerung_rel']}; "
                 f"reflektiert je omega^2: {tr['reflektiert_je_omega2']}")
        for j in tr["je_seed"]:
            z.append(f"           Seed {j['seed']}: Durchlaufzeiten {j['transit']}")
    verl = [r["ladungsverlust"] for r in f["laeufe"]]
    z.append(f"  Ladungsverlust im Fenster: hoechstens {max(verl):.2e}")
    z.append("  " + l3_zeile(erg["L3"]))
    return z


# ================================================================ Test 4: Neuron (Bio 13)

NEU_W2 = 0.7
NEU_DEHN = [0.01, 0.03, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0]
NEU_AMP = [0.03, 0.1, 0.3, 0.5]
NEU_T, NEU_L, NEU_RWIN = 300.0, 120.0, 20.0
NEU_S_KLUMPEN = 0.01     # niedriger als S_KLUMPEN: ein auf omega^2 ~ 0,98 entspannter Ball hat S_max ~ 0,02


def test_neuron(dx, dt, rauch):
    """Ruhender Ball, Stoss bei t = 0. dehnung: psi_t += -eps x f'(x) (Ladung unveraendert);
    amplitude: psi = (1 + eps) f bei gleichem omega (Ladung mal (1 + eps)^2). null: ungestoert (Bezug)."""
    x = gitter(dx, NEU_L)
    laeufe = [{"art": "null", "eps": 0.0}]
    laeufe += [{"art": "dehnung", "eps": vz * e} for e in NEU_DEHN for vz in (1.0, -1.0)]
    laeufe += [{"art": "amplitude", "eps": vz * e} for e in NEU_AMP for vz in (1.0, -1.0)]
    nb = len(laeufe)
    f, fs = anker(NEU_W2, x)
    om = math.sqrt(NEU_W2)
    psi = torch.zeros(nb, x.shape[0], dtype=C128, device=DEV)
    vel = torch.zeros_like(psi)
    for n, r in enumerate(laeufe):
        a = 1.0 + (r["eps"] if r["art"] == "amplitude" else 0.0)
        e = r["eps"] if r["art"] == "dehnung" else 0.0
        psi[n] = torch.complex(a * f, torch.zeros_like(f))
        vel[n] = torch.complex(-e * x * fs, -om * a * f)
    e_start = energie(psi, vel, dx)
    x_innen = NEU_L - SCHWAMM - 5.0
    fen = (x.abs() < NEU_RWIN).to(F64)
    innen = (x.abs() < x_innen).to(F64)

    def messen(p, q):
        s = p.real ** 2 + p.imag ** 2
        rho = 2.0 * (p * q.conj()).imag
        qw = (rho * fen).sum(1) * dx
        b2 = (x * x * rho * fen).sum(1) * dx / qw.clamp(min=1e-30)
        n_kl, top = klumpen(p, q, x, dx, x_innen, 2, NEU_S_KLUMPEN)
        return torch.stack([(s * innen).max(dim=1).values, qw, torch.sqrt(b2.clamp(min=0.0)), n_kl,
                            top[:, 0], top[:, 1]], dim=1)

    t_end = T_RAUCH if rauch else NEU_T
    t, daten, _, _ = entwickeln(psi, vel, x, dx, dt, t_end, NEU_L, messen)
    smax, qw = daten[:, :, 0], daten[:, :, 1]
    frueh = t <= 50.0 + 1e-9
    spitze = (smax[frueh] - smax[frueh][:, 0:1]).abs().max(dim=0).values / smax[0, 0]
    sp = t >= t_end - 100.0 - 1e-9
    s_sp = smax[sp]
    atmung = (s_sp.max(dim=0).values - s_sp.min(dim=0).values) / (2.0 * s_sp.mean(dim=0))
    s_end = s_sp.mean(dim=0)
    for n, r in enumerate(laeufe):
        r["reizenergie"] = (e_start[n] - e_start[0]).item()
        r["spitze"] = spitze[n].item()
        r["atmung_spaet"] = atmung[n].item()
        r["ladung_abgestrahlt"] = 1.0 - (qw[-1, n] / qw[0, n]).item()
        r["omega2_end_aus_smax"] = 0.5 * (1.0 + (1.0 - s_end[n].item()) ** 2)
        r["n_klumpen_end"] = int(daten[-1, n, 3].item())
        r["q_klumpen_end"] = [(daten[-1, n, 4] / qw[0, n]).item(), (daten[-1, n, 5] / qw[0, n]).item()]
    spruenge = []
    for art, liste in (("dehnung", NEU_DEHN), ("amplitude", NEU_AMP)):
        for vz in (1.0, -1.0):
            reihe = [next(r for r in laeufe if r["art"] == art and r["eps"] == vz * e) for e in liste]
            for a, b in zip(reihe[:-1], reihe[1:]):
                ra, rb = a["spitze"] / abs(a["eps"]), b["spitze"] / abs(b["eps"])
                if rb > 3.0 * ra or 3.0 * rb < ra or a["n_klumpen_end"] != b["n_klumpen_end"]:
                    spruenge.append({"art": art, "eps_a": a["eps"], "eps_b": b["eps"], "spitze_je_eps_a": ra,
                                     "spitze_je_eps_b": rb, "klumpen_a": a["n_klumpen_end"],
                                     "klumpen_b": b["n_klumpen_end"]})
    return {"t_end": t_end, "laeufe": laeufe, "spruenge": spruenge}


def l3_neuron(erg):
    g, f = erg["grob"]["laeufe"], erg["fein"]["laeufe"]
    aend = max(abs(a["spitze"] - b["spitze"]) for a, b in zip(g, f))
    effekt = max(b["spitze"] for b in f)
    gleich = sum(1 for a, b in zip(g, f) if a["n_klumpen_end"] == b["n_klumpen_end"])
    return {"effekt_max_spitze": effekt, "aenderung_max_spitze": aend, "bestanden": effekt >= L3_FAKTOR * aend,
            "klumpenzahl_gleich": f"{gleich} von {len(f)}"}


def bericht_neuron(erg):
    f = erg["fein"]
    z = [f"Neuron (Bio 13): omega^2 = {NEU_W2}, T = {f['t_end']}; Spitze = max |S_max - S_max(null)| / S_max(0) "
         f"bis t = 50; Atmung spaet = halbe Spannweite von S_max in den letzten 100 / Mittel",
         "  art        eps    Reizenergie  Spitze   Spitze/|eps|  Atmung   Q abgestrahlt  Klumpen  omega^2 Ende"]
    for r in f["laeufe"]:
        je = r["spitze"] / abs(r["eps"]) if r["eps"] != 0.0 else 0.0
        z.append(f"  {r['art']:9s} {r['eps']:+.2f}  {r['reizenergie']:.3e}  {r['spitze']:.3e}  {je:.3e}  "
                 f"{r['atmung_spaet']:.2e}  {r['ladung_abgestrahlt']:+.2e}  {r['n_klumpen_end']}  "
                 f"{r['omega2_end_aus_smax']:.4f}")
    z.append(f"  Spruenge (Faktor 3 in Spitze/|eps| oder Klumpenzahl aendert sich): {len(f['spruenge'])}")
    for s in f["spruenge"]:
        z.append(f"    {s}")
    z.append("  " + l3_zeile(erg["L3"]))
    return z


# ================================================================ Test 5: Wundheilung (Bio 27)

WUN_W2 = [0.7, 0.55]
WUN_P = [0.10, 0.25, 0.50]
WUN_BREITE = 0.5         # Schnittkante tanh((x - x_c) / 0,5)
WUN_T, WUN_L, WUN_RWIN, WUN_KERN = 400.0, 120.0, 20.0, 8.0


def schnitt_fenster(x, xc, sym):
    w = 0.5 * (1.0 - torch.tanh((x - xc) / WUN_BREITE))
    if sym:
        w = w * 0.5 * (1.0 + torch.tanh((x + xc) / WUN_BREITE))
    return w


def schnittstelle(w2, p, sym):
    """x_c, so dass psi = f w den Anteil p der Ladung verliert (Ladung ~ Int f^2 w^2), feines Hilfsgitter."""
    xf = torch.linspace(-30.0, 30.0, 60001, dtype=F64, device=DEV)
    f2 = anker(w2, xf)[0] ** 2
    ges = f2.sum()
    lo, hi = (0.0, 30.0) if sym else (-30.0, 30.0)
    for _ in range(60):
        mitte = 0.5 * (lo + hi)
        rest = ((f2 * schnitt_fenster(xf, mitte, sym) ** 2).sum() / ges).item()
        if rest > 1.0 - p:
            hi = mitte
        else:
            lo = mitte
    return 0.5 * (lo + hi)


def q_tabelle():
    """Q(omega^2) des 1D-Ankers, aufsteigend in Q (fuer die Umkehrung omega^2(Q))."""
    w2 = torch.linspace(0.5001, 0.9999, 20001, dtype=F64, device=DEV)
    q = 2.0 * torch.sqrt(w2) * math.sqrt(2.0) * torch.acosh(1.0 / torch.sqrt(2.0 * w2 - 1.0))
    return q.flip(0).contiguous(), w2.flip(0).contiguous()


def w2_aus_q(q, tab):
    q_auf, w2_auf = tab
    i = torch.searchsorted(q_auf, q.contiguous()).clamp(1, q_auf.shape[0] - 1)
    qa, qb = q_auf[i - 1], q_auf[i]
    a = ((q - qa) / (qb - qa)).clamp(0.0, 1.0)
    return w2_auf[i - 1] + a * (w2_auf[i] - w2_auf[i - 1])


def test_wunde(dx, dt, rauch):
    """Ball rechts um den Ladungsanteil p beschnitten (weiche Kante), dazu ungeschnitten (null) und symmetrisch
    25 % (je Seite 12,5 %) als Gegenproben. Schiefe = drittes Moment der Ladung um den Schwerpunkt (+-8);
    Form = L2-Abstand von |psi| zum Gleichgewichtsprofil derselben Fensterladung."""
    x = gitter(dx, WUN_L)
    laeufe = []
    for w2 in WUN_W2:
        laeufe.append({"omega2": w2, "schnitt": "null", "p": 0.0, "xc": None})
        for p in WUN_P:
            laeufe.append({"omega2": w2, "schnitt": "einseitig", "p": p, "xc": schnittstelle(w2, p, False)})
        laeufe.append({"omega2": w2, "schnitt": "symmetrisch", "p": 0.25, "xc": schnittstelle(w2, 0.25, True)})
    nb = len(laeufe)
    psi = torch.zeros(nb, x.shape[0], dtype=C128, device=DEV)
    vel = torch.zeros_like(psi)
    for n, r in enumerate(laeufe):
        f, _ = anker(r["omega2"], x)
        w = torch.ones_like(x) if r["xc"] is None else schnitt_fenster(x, r["xc"], r["schnitt"] == "symmetrisch")
        psi[n] = torch.complex(f * w, torch.zeros_like(f))
        vel[n] = torch.complex(torch.zeros_like(f), -math.sqrt(r["omega2"]) * f * w)
    tab = q_tabelle()
    zust = {"x_alt": torch.zeros(nb, 1, dtype=F64, device=DEV)}

    def messen(p, q):
        s = p.real ** 2 + p.imag ** 2
        rho = 2.0 * (p * q.conj()).imag
        fen = ((x - zust["x_alt"]).abs() < WUN_RWIN).to(F64)
        qw = (rho * fen).sum(1) * dx
        X = (x * rho * fen).sum(1) * dx / qw.clamp(min=1e-30)
        y = x - X.unsqueeze(1)
        kern = (y.abs() < WUN_KERN).to(F64)
        qk = ((rho * kern).sum(1) * dx).clamp(min=1e-30)
        var = ((y ** 2 * rho * kern).sum(1) * dx / qk).clamp(min=1e-30)
        schiefe = (y ** 3 * rho * kern).sum(1) * dx / qk / var ** 1.5
        f_gl, _ = anker(w2_aus_q(qw, tab).unsqueeze(1), y)
        form = torch.sqrt((((s.sqrt() - f_gl) ** 2) * kern).sum(1) / ((f_gl ** 2) * kern).sum(1).clamp(min=1e-30))
        zust["x_alt"] = X.unsqueeze(1)
        return torch.stack([X, qw, schiefe, form, (s * fen).max(dim=1).values], dim=1)

    t_end = T_RAUCH if rauch else WUN_T
    t, daten, _, _ = entwickeln(psi, vel, x, dx, dt, t_end, WUN_L, messen)
    X, qw, schiefe, form, smax = daten.unbind(dim=2)
    t_sch = dauerhaft_unter(t, schiefe.abs(), 0.1 * schiefe[0].abs())
    t_form = dauerhaft_unter(t, form, 0.1 * form[0])
    sp = t >= t_end - 100.0 - 1e-9
    w2_q = w2_aus_q(qw[-1].contiguous(), tab)
    w2_s = 0.5 * (1.0 + (1.0 - smax[sp].mean(dim=0)) ** 2)
    spaeter = t >= min(20.0, t_end)
    for n, r in enumerate(laeufe):
        q_voll, _ = anker_qe(r["omega2"])
        r["p_ist"] = 1.0 - qw[0, n].item() / q_voll
        r["schiefe_anfang"] = schiefe[0, n].item()
        r["schiefe_max_ab_t20"] = schiefe[spaeter, n].abs().max().item()
        r["form_anfang"] = form[0, n].item()
        r["form_end"] = form[-1, n].item()
        r["form_min"] = form[:, n].min().item()
        r["heilzeit_schiefe"] = endlich(t_sch[n].item())
        r["heilzeit_form"] = endlich(t_form[n].item())
        r["ladung_abgestrahlt"] = 1.0 - (qw[-1, n] / qw[0, n]).item()
        r["omega2_end_aus_q"] = w2_q[n].item()
        r["omega2_end_aus_smax"] = w2_s[n].item()
        r["x_end"] = X[-1, n].item()
    return {"t_end": t_end, "laeufe": laeufe}


def l3_wunde(erg):
    ok, vergleiche = True, []
    for a, b in zip(erg["grob"]["laeufe"], erg["fein"]["laeufe"]):
        if b["schnitt"] != "einseitig":
            continue
        for key in ("ladung_abgestrahlt", "heilzeit_schiefe"):
            u, w = a[key], b[key]
            if u is None or w is None:
                gut = (u is None) == (w is None)
            else:
                gut = L3_FAKTOR * abs(u - w) <= abs(w)
            ok = ok and gut
            vergleiche.append(f"{b['omega2']}/{b['p']}/{key}: grob {u}, fein {w}, {'ok' if gut else 'NEIN'}")
    return {"bestanden": ok, "vergleiche": "; ".join(vergleiche)}


def bericht_wunde(erg):
    f = erg["fein"]
    z = [f"Wundheilung (Bio 27): T = {f['t_end']}; Heilzeit = ab wann |Schiefe| bzw. Formfehler dauerhaft unter 10 % "
         f"des Anfangswerts bleibt",
         "  omega^2 Schnitt       p    p_ist  Schiefe0  |Schiefe|max(t>20)  Heilzeit_S  Form0   Form_end  Heilzeit_F  "
         "Q_abgestrahlt  omega^2_Ende(Q, Smax)"]
    for r in f["laeufe"]:
        z.append(f"  {r['omega2']:.2f}   {r['schnitt']:11s} {r['p']:.2f} {r['p_ist']:.3f}  {r['schiefe_anfang']:+.3e}  "
                 f"{r['schiefe_max_ab_t20']:.3e}  {r['heilzeit_schiefe']}  {r['form_anfang']:.3e}  {r['form_end']:.3e}  "
                 f"{r['heilzeit_form']}  {r['ladung_abgestrahlt']:+.3e}  {r['omega2_end_aus_q']:.4f}, "
                 f"{r['omega2_end_aus_smax']:.4f}")
    z.append("  " + l3_zeile(erg["L3"]))
    return z


# ================================================================ Test 6: Nervenfaser (Bio 41)

NER_W2 = 0.7
NER_N = 6
NER_D = [9.0, 12.0, 15.0, 40.0]
NER_V = 0.2              # stoss: Ball 0 laeuft mit v = 0,2 auf die Kette zu
NER_EPS = 0.3            # atem: Dehnungsstoss wie im Neuron-Test
NER_T, NER_L = 400.0, 180.0
NER_ANTEIL = 0.1         # Ankunft: Signal erreicht 10 % der Amplitude von Ball 0


def nerv_signal(t, sig, d):
    """Je Ball: Amplitude (Maximum des Signals), Ankunft (erste Zeit ueber NER_ANTEIL mal Amplitude von Ball 0)."""
    amp = sig.max(dim=0).values
    schwelle = NER_ANTEIL * amp[0]
    ankunft = [erste_zeit(t, sig[:, k], schwelle) for k in range(sig.shape[1])]
    amp_l = amp.tolist()
    daempfung = [amp_l[k + 1] / amp_l[k] if amp_l[k] > 0 else None for k in range(len(amp_l) - 1)]
    laufzeit = [None if (a is None or b is None or b <= a) else b - a for a, b in zip(ankunft[:-1], ankunft[1:])]
    return {"amplitude": amp_l, "ankunft": ankunft, "daempfung_je_glied": daempfung, "laufzeit_je_glied": laufzeit,
            "tempo_je_glied": [None if lz is None else d / lz for lz in laufzeit],
            "weiterleitung": ankunft[1] is not None}


def test_nerv(dx, dt, rauch):
    """Sechs Baelle mit wechselnder Phase (0, pi, ...) im Abstand d. ruhe: ungestoert; stoss: Ball 0 mit v = 0,2;
    atem: Ball 0 mit Dehnungsstoss. Signal = Differenz zu ruhe (Geschwindigkeit bzw. |Delta S_max|) je Ball."""
    x = gitter(dx, NER_L)
    laeufe = [{"d": d, "art": a} for d in NER_D for a in ("ruhe", "stoss", "atem")]
    nb, kk = len(laeufe), NER_N
    psi = torch.zeros(nb, x.shape[0], dtype=C128, device=DEV)
    vel = torch.zeros_like(psi)
    zentren = torch.zeros(nb, kk, dtype=F64, device=DEV)
    halb = torch.zeros(nb, 1, 1, dtype=F64, device=DEV)
    for n, r in enumerate(laeufe):
        xk = [(k - 0.5 * (kk - 1)) * r["d"] for k in range(kk)]
        zentren[n] = torch.tensor(xk, dtype=F64, device=DEV)
        halb[n, 0, 0] = min(0.5 * r["d"], 20.0)
        for k in range(kk):
            v = NER_V if (k == 0 and r["art"] == "stoss") else 0.0
            a, b = ball(x, NER_W2, xk[k], v, k * math.pi)
            psi[n] += a
            vel[n] += b
        if r["art"] == "atem":
            _, fs0 = anker(NER_W2, x - xk[0])
            vel[n] += torch.complex(-NER_EPS * (x - xk[0]) * fs0, torch.zeros_like(fs0))
    q0, _ = anker_qe(NER_W2)
    xv = x.view(1, 1, -1)
    zust = {"z": zentren.clone()}

    def messen(p, q):
        s = (p.real ** 2 + p.imag ** 2).unsqueeze(1)
        rho = (2.0 * (p * q.conj()).imag).unsqueeze(1)
        fen = ((xv - zust["z"].unsqueeze(2)).abs() < halb).to(F64)
        qk = (rho * fen).sum(2) * dx
        X = (rho * fen * xv).sum(2) * dx / qk.clamp(min=1e-30)
        smax = (s * fen).max(dim=2).values
        zust["z"] = torch.where(qk > 0.5 * q0, X, zust["z"])
        return torch.cat([zust["z"], smax, qk / q0], dim=1)

    t_end = T_RAUCH if rauch else NER_T
    t, daten, _, _ = entwickeln(psi, vel, x, dx, dt, t_end, NER_L, messen)
    X, S = daten[:, :, :kk], daten[:, :, kk:2 * kk]
    ausw = {}
    for d in NER_D:
        nr, ns, na = (next(i for i, r in enumerate(laeufe) if r["d"] == d and r["art"] == a)
                      for a in ("ruhe", "stoss", "atem"))
        dX = X[:, ns] - X[:, nr]
        dV = torch.zeros_like(dX)
        dV[1:-1] = (dX[2:] - dX[:-2]) / (2.0 * T_MEAS)
        dS = (S[:, na] - S[:, nr]).abs()
        ausw[str(d)] = {"stoss": nerv_signal(t, dV, d), "atem": nerv_signal(t, dS, d),
                        "ruhe_ausdehnung": (X[-1, nr, kk - 1] - X[-1, nr, 0] - (kk - 1) * d).item(),
                        "ladung_end_ruhe": daten[-1, nr, 2 * kk:].tolist()}
    return {"t_end": t_end, "auswertung": ausw}


def l3_nerv(erg):
    aend, eff = 0.0, float("inf")
    a_aend, a_eff = 0.0, 0.0
    for d, b in erg["fein"]["auswertung"].items():
        a = erg["grob"]["auswertung"][d]
        for u, w in zip(a["stoss"]["ankunft"][1:], b["stoss"]["ankunft"][1:]):
            if u is not None and w is not None:
                aend = max(aend, abs(u - w))
        for lz in b["stoss"]["laufzeit_je_glied"]:
            if lz is not None:
                eff = min(eff, lz)
        a_aend = max(a_aend, abs(a["atem"]["amplitude"][1] - b["atem"]["amplitude"][1]))
        a_eff = max(a_eff, b["atem"]["amplitude"][1])
    eff = 0.0 if math.isinf(eff) else eff
    return {"stoss_effekt_kuerzeste_laufzeit": eff, "stoss_aenderung_ankunft": aend,
            "atem_effekt_amplitude_ball1": a_eff, "atem_aenderung": a_aend,
            "bestanden": eff >= L3_FAKTOR * aend and a_eff >= L3_FAKTOR * a_aend}


def bericht_nerv(erg):
    f = erg["fein"]
    z = [f"Nervenfaser (Bio 41): {NER_N} Baelle, omega^2 = {NER_W2}, Phasen 0, pi, ...; stoss v = {NER_V}, "
         f"atem eps = {NER_EPS}; Ankunft = {NER_ANTEIL:.0%} der Amplitude von Ball 0; T = {f['t_end']}"]
    for d, au in f["auswertung"].items():
        z.append(f"  d = {d}: Ausdehnung der ruhenden Kette bis T: {au['ruhe_ausdehnung']:.2f}")
        for art in ("stoss", "atem"):
            s = au[art]
            z.append(f"    {art:5s} Amplitude {[round(a, 5) for a in s['amplitude']]}")
            z.append(f"          Ankunft {s['ankunft']}, Tempo je Glied {s['tempo_je_glied']}, "
                     f"Daempfung je Glied {[None if v is None else round(v, 3) for v in s['daempfung_je_glied']]}, "
                     f"Weiterleitung {s['weiterleitung']}")
    z.append("  " + l3_zeile(erg["L3"]))
    return z


# ================================================================ Zufallskarte Bio 18: Artbildung (radiales Schiessen)

ART_FAM = [(3, 0), (2, 0), (2, 1), (2, 2)]
ART_W2 = [round(0.51 + 0.01 * k, 2) for k in range(49)]
ART_H, ART_X, ART_NK, ART_RUNDEN, ART_RMAX = 0.04, 150.0, 256, 6, 400.0
ART_U_MIN, ART_C_MIN, ART_C_MAX = 1e-280, 1e-40, 10.0
ART_VIRIAL = 1e-3        # gueltig nur mit |(d-2) G + d (V - W)| / E < 1e-3 (Derrick-Identitaet)


def art_parameter(fam, w2s):
    """Zeilen (d, m, omega^2); Rueckgabe Tensoren (R, 1): d, m, Koeffizienten der Entwicklung um fr, ft, fr; w2.

    fr = f_t (oberer Gipfel, W'(f_t) = 0) fuer m = 0, sonst 0. Integriert wird g = f - fr."""
    zeilen = [(d, m, w) for d, m in fam for w in w2s]

    def spalte(i):
        return torch.tensor([float(z[i]) for z in zeilen], dtype=F64, device=DEV).unsqueeze(1)

    d, m, w2 = spalte(0), spalte(1), spalte(2)
    a0 = 1.0 - w2
    ft = torch.sqrt((2.0 + torch.sqrt(4.0 - 6.0 * a0)) / 3.0)
    fr = torch.where(m == 0, ft, torch.zeros_like(ft))
    # W'(fr + g) - W'(fr) = g (c1 + g (c2 + g (c3 + g (c4 + g c5)))), W'(f) = a0 f - 2 f^3 + 1,5 f^5
    c1 = a0 - 6.0 * fr ** 2 + 7.5 * fr ** 4
    c2 = -6.0 * fr + 15.0 * fr ** 3
    c3 = -2.0 + 15.0 * fr ** 2
    c4 = 7.5 * fr
    par = {"d1": d - 1.0, "m2": m * m, "c": (c1, c2, c3, c4), "fr": fr, "ft": ft, "null": m == 0,
           "a0": a0, "d": d, "m": m}
    return zeilen, par, w2


def art_wstrich(g, par):
    c1, c2, c3, c4 = par["c"]
    return g * (c1 + g * (c2 + g * (c3 + g * (c4 + 1.5 * g))))


def art_kraft(r, g, gp, par):
    """g'' = -((d-1)/r) g' + (m^2/r^2) (fr + g) + W'(fr + g) - W'(fr); W'(fr) = 0 exakt."""
    return -(par["d1"] / r) * gp + (par["m2"] / (r * r)) * (par["fr"] + g) + art_wstrich(g, par)


def art_rk4(r, g, gp, h, par):
    k1g, k1p = gp, art_kraft(r, g, gp, par)
    k2g, k2p = gp + 0.5 * h * k1p, art_kraft(r + 0.5 * h, g + 0.5 * h * k1g, gp + 0.5 * h * k1p, par)
    k3g, k3p = gp + 0.5 * h * k2p, art_kraft(r + 0.5 * h, g + 0.5 * h * k2g, gp + 0.5 * h * k2p, par)
    k4g, k4p = gp + h * k3p, art_kraft(r + h, g + h * k3g, gp + h * k3p, par)
    return (g + (h / 6.0) * (k1g + 2.0 * k2g + 2.0 * k3g + k4g),
            gp + (h / 6.0) * (k1p + 2.0 * k2p + 2.0 * k3p + k4p))


def art_start(s, par, r0):
    """Startwerte bei r0 aus der Reihe um r = 0. m = 0: s = ln(f_t - f(0)), f = f(0) + W'(f(0)) r^2 / (2 d).
    m >= 1: s = ln c, f = c r^m (1 + a0 r^2 / (4 (m + 1)))."""
    u = torch.exp(s)
    w = art_wstrich(-u, par)
    g_0 = -u + w * (r0 * r0) / (2.0 * par["d"])
    p_0 = w * r0 / par["d"]
    mm = par["m"].clamp(min=1.0)
    k2 = par["a0"] / (4.0 * (mm + 1.0))
    rm = torch.pow(torch.full_like(mm, r0), mm)
    g_m = u * rm * (1.0 + k2 * r0 * r0)
    p_m = u * rm / r0 * (mm + (mm + 2.0) * k2 * r0 * r0)
    return torch.where(par["null"], g_0, g_m), torch.where(par["null"], p_0, p_m)


def art_klammer(s, klasse, lo, hi):
    """Neue Klammer: erster Klassenwechsel zwischen benachbarten entschiedenen Kandidaten (Klassen +1 und -1)."""
    ent = (klasse == 1.0) | (klasse == -1.0)
    kk = s.shape[1]
    idx = torch.arange(kk, device=DEV).unsqueeze(0).expand(s.shape[0], kk)
    letzte = torch.cummax(torch.where(ent, idx, torch.full_like(idx, -1)), dim=1).values
    vorher = torch.cat([torch.full_like(letzte[:, :1], -1), letzte[:, :-1]], dim=1)
    kl_vorher = klasse.gather(1, vorher.clamp(min=0))
    wechsel = ent & (vorher >= 0) & (klasse != kl_vorher)
    hat = wechsel.any(dim=1, keepdim=True)
    j = torch.argmax(wechsel.to(torch.int64), dim=1, keepdim=True)
    jv = vorher.gather(1, j).clamp(min=0)
    return torch.where(hat, s.gather(1, jv), lo), torch.where(hat, s.gather(1, j), hi), hat


def art_schiessen(par, n_kand, runden, x_ode, h):
    """Einschachteln wie qg1.schiessen, alle Zeilen und Kandidaten gleichzeitig.

    Klassen: +1 f < 0 (kreuzt null), -1 f' > 0 nach dem Abstieg (kehrt um), +2 f > 1,5 f_t (entweicht), 0 offen."""
    null = par["null"]
    lo = torch.where(null, torch.full_like(par["d"], math.log(ART_U_MIN)), torch.full_like(par["d"], math.log(ART_C_MIN)))
    hi = torch.where(null, torch.log(par["ft"] - 1e-3), torch.full_like(par["d"], math.log(ART_C_MAX)))
    stufen = torch.linspace(0.0, 1.0, n_kand, dtype=F64, device=DEV)
    n_schritte = int(round(x_ode / h))
    gefunden = torch.zeros_like(null)
    for _ in range(runden):
        s = lo + (hi - lo) * stufen
        g, gp = art_start(s, par, h)
        klasse = torch.zeros_like(s)
        gefallen = null.expand(s.shape[0], s.shape[1]).clone()
        for i in range(n_schritte):
            g, gp = art_rk4(h * (i + 1), g, gp, h, par)
            f = par["fr"] + g
            nul = torch.zeros_like(s)
            neu = torch.where(gefallen & (gp > 0), nul - 1.0, nul)
            neu = torch.where(f > 1.5 * par["ft"], nul + 2.0, neu)
            neu = torch.where(f < 0, nul + 1.0, neu)
            klasse = torch.where(klasse == 0, neu, klasse)
            gefallen = gefallen | (gp < 0)
            lebt = (klasse == 0).to(F64)
            g = g * lebt
            gp = gp * lebt
            if i % 500 == 499 and not bool((klasse == 0).any()):
                break
        lo, hi, hat = art_klammer(s, klasse, lo, hi)
        gefunden = gefunden | hat
    return 0.5 * (lo + hi), hi - lo, gefunden


def art_bahn(s_mitte, par, x_ode, h):
    """Bahn ab dem Klammermittel bis f < SCHWANZ * f_max (nach dem Maximum); danach eingefroren.

    Bahnindex p gehoert zu r = h (p + 1). fehler: Bahn kreuzt null, entweicht oder kehrt vor der Schwelle um."""
    g, gp = art_start(s_mitte, par, h)
    n = int(round(x_ode / h))
    fmax = par["fr"] + g
    gefallen = par["null"].clone()
    erreicht = torch.zeros_like(gefallen)
    fehler = torch.zeros_like(gefallen)
    j_cut = torch.full(g.shape, n + 1, dtype=torch.int64, device=DEV)
    bahn_g, bahn_p = [g], [gp]
    for i in range(n):
        g_neu, p_neu = art_rk4(h * (i + 1), g, gp, h, par)
        weiter = ~(erreicht | fehler)            # nach Schwelle oder Fehler eingefroren
        g = torch.where(weiter, g_neu, g)
        gp = torch.where(weiter, p_neu, gp)
        f = par["fr"] + g
        fmax = torch.maximum(fmax, f)
        gefallen = gefallen | (gp < 0)
        fehler = fehler | (weiter & ((f < 0) | (f > 1.5 * par["ft"]) | (gefallen & (gp > 0))))
        neu = weiter & gefallen & (f < SCHWANZ * fmax)
        j_cut = torch.where(neu, torch.full_like(j_cut, i + 1), j_cut)
        erreicht = erreicht | neu
        bahn_g.append(g)
        bahn_p.append(gp)
    return torch.cat(bahn_g, dim=1), torch.cat(bahn_p, dim=1), j_cut, fehler | ~erreicht


def art_integrale(bahn_g, bahn_p, j_cut, par, w2, h, r_max):
    """Q, E, W, G, V, Virialrest, Ladungsradius auf dem Radialgitter r_p = h (p + 1), Simpson mit r = 0
    (Integrand dort null). Jenseits der Schwelle Schwanz f_cut exp(-kappa (r - r_cut)) (r_cut / r)^((d-1)/2)."""
    d, m, fr = par["d"], par["m"], par["fr"]
    n_r = 2 * int(round(0.5 * r_max / h))
    r = h * (torch.arange(n_r, dtype=F64, device=DEV) + 1.0)
    nbahn = bahn_g.shape[1]
    p = torch.arange(n_r, device=DEV).unsqueeze(0).expand(d.shape[0], n_r)
    pc = p.clamp(max=nbahn - 1)
    jc = j_cut.clamp(max=nbahn - 1)
    f_cut = fr + bahn_g.gather(1, jc)
    r_cut = h * (jc.to(F64) + 1.0)
    kappa = torch.sqrt(par["a0"])
    aussen = f_cut * torch.exp(-kappa * (r - r_cut).clamp(min=0.0)) * (r_cut / r) ** (0.5 * (d - 1.0))
    innen = p < jc
    f = torch.where(innen, fr + bahn_g.gather(1, pc), aussen)
    fs = torch.where(innen, bahn_p.gather(1, pc), aussen * (-kappa - 0.5 * (d - 1.0) / r))
    q_idx = torch.arange(1, n_r + 1, device=DEV)
    gew = torch.where(q_idx % 2 == 1, torch.full_like(r, 4.0), torch.full_like(r, 2.0))
    gew[-1] = 1.0
    gew = gew * (h / 3.0)
    raumwinkel = torch.where(d == 3, torch.full_like(d, 4.0 * math.pi), torch.full_like(d, 2.0 * math.pi))
    raum = raumwinkel * r ** (d - 1.0) * gew
    s = f * f
    i2 = (s * raum).sum(1, keepdim=True)
    w = w2 * i2
    g = ((fs * fs + m * m * s / (r * r)) * raum).sum(1, keepdim=True)
    v = ((s - s * s + 0.5 * s ** 3) * raum).sum(1, keepdim=True)
    e = w + g + v
    return {"Q": 2.0 * torch.sqrt(w2) * i2, "E": e, "W": w, "G": g, "V": v,
            "virial": ((d - 2.0) * g + d * (v - w)) / e,
            "r_ladung": torch.sqrt((s * r * r * raum).sum(1, keepdim=True) / i2),
            "f_max": f.max(dim=1, keepdim=True).values}


def art_rechnen(w2s, n_kand, runden, x_ode, h, r_max):
    zeilen, par, w2 = art_parameter(ART_FAM, w2s)
    s_mitte, breite, gefunden = art_schiessen(par, n_kand, runden, x_ode, h)
    bahn_g, bahn_p, j_cut, fehler = art_bahn(s_mitte, par, x_ode, h)
    integ = art_integrale(bahn_g, bahn_p, j_cut, par, w2, h, r_max)
    gueltig = gefunden & ~fehler & (integ["virial"].abs() < ART_VIRIAL)
    out = []
    for i, (d, m, w) in enumerate(zeilen):
        out.append({"d": d, "m": m, "omega2": w, "gueltig": bool(gueltig[i, 0]), "klammer_gefunden": bool(gefunden[i, 0]),
                    "bahn_fehler": bool(fehler[i, 0]), "s_parameter": s_mitte[i, 0].item(),
                    "klammerbreite": breite[i, 0].item(), "r_schwanz": h * (j_cut[i, 0].item() + 1),
                    **{k: integ[k][i, 0].item() for k in integ}})
    return out


def schnittpunkte(pa, pb):
    """Schnittpunkte zweier Polylinien pa (Na, 2), pb (Nb, 2) als Liste."""
    if pa.shape[0] < 2 or pb.shape[0] < 2:
        return []
    a1, da = pa[:-1].unsqueeze(1), (pa[1:] - pa[:-1]).unsqueeze(1)
    b1, db = pb[:-1].unsqueeze(0), (pb[1:] - pb[:-1]).unsqueeze(0)

    def kreuz(u, v):
        return u[..., 0] * v[..., 1] - u[..., 1] * v[..., 0]

    nenner = kreuz(da, db)
    sicher = torch.where(nenner.abs() > 1e-300, nenner, torch.ones_like(nenner))
    ta = kreuz(b1 - a1, db) / sicher
    tb = kreuz(b1 - a1, da) / sicher
    treffer = (nenner.abs() > 1e-300) & (ta >= 0) & (ta <= 1) & (tb >= 0) & (tb <= 1)
    ia, ib = torch.nonzero(treffer, as_tuple=True)
    punkte = a1[ia, 0] + ta[ia, ib].unsqueeze(1) * da[ia, 0]
    return [{"segment_a": i, "segment_b": j, "lnQ": pt[0], "E_durch_Q": pt[1]}
            for i, j, pt in zip(ia.tolist(), ib.tolist(), punkte.tolist())]


def art_familie(zeilen):
    """Q_min, Vorzeichenwechsel von dQ/domega, E/Q = 1, Probe dE = omega dQ (zentrale Differenzen)."""
    g = [z for z in zeilen if z["gueltig"]]
    if len(g) < 3:
        return {"gueltige_omega": len(g)}
    q = [z["Q"] for z in g]
    i_min = min(range(len(q)), key=lambda i: q[i])
    dq = [q[i + 1] - q[i] for i in range(len(q) - 1)]
    wechsel_dq = [g[i + 1]["omega2"] for i in range(len(dq) - 1) if dq[i] * dq[i + 1] < 0]
    eq = [z["E"] / z["Q"] - 1.0 for z in g]
    eq_eins = []
    for i in range(len(eq) - 1):
        if eq[i] * eq[i + 1] < 0:
            a = eq[i] / (eq[i] - eq[i + 1])
            eq_eins.append(g[i]["omega2"] + a * (g[i + 1]["omega2"] - g[i]["omega2"]))
    probe = []
    for i in range(1, len(g) - 1):
        if abs((g[i + 1]["omega2"] - g[i]["omega2"]) - (g[i]["omega2"] - g[i - 1]["omega2"])) < 1e-9:
            de = g[i + 1]["E"] - g[i - 1]["E"]
            dqq = g[i + 1]["Q"] - g[i - 1]["Q"]
            probe.append(abs(de - math.sqrt(g[i]["omega2"]) * dqq) / max(abs(de), 1e-300))
    probe_sort = sorted(probe)
    return {"gueltige_omega": len(g), "omega2_gueltig_von_bis": [g[0]["omega2"], g[-1]["omega2"]],
            "Q_min": q[i_min], "omega2_bei_Q_min": g[i_min]["omega2"],
            "Q_min_innen": 0 < i_min < len(g) - 1, "vorzeichenwechsel_dQ_bei_omega2": wechsel_dq,
            "E_gleich_Q_bei_omega2": eq_eins,
            "probe_dE_omega_dQ_median": probe_sort[len(probe_sort) // 2] if probe_sort else None,
            "probe_dE_omega_dQ_max": probe_sort[-1] if probe_sort else None,
            "virial_max_gueltig": max(abs(z["virial"]) for z in g)}


def test_artbildung(rauch):
    if rauch:
        w2s, nk, runden, x_ode, r_max = [0.6, 0.8, 0.95], 32, 2, 40.0, 60.0
    else:
        w2s, nk, runden, x_ode, r_max = ART_W2, ART_NK, ART_RUNDEN, ART_X, ART_RMAX
    erg = {"omega2": w2s, "n_kand": nk, "runden": runden, "x_ode": x_ode, "r_max": r_max}
    for stufe, h in (("fein", ART_H), ("grob", 2.0 * ART_H)):
        t0 = uhr()
        erg[stufe] = {"h": h, "zeilen": art_rechnen(w2s, nk, runden, x_ode, h, r_max)}
        erg[stufe]["dauer_s"] = uhr() - t0
        print(f"  Artbildung {stufe} (h = {h}) fertig nach {erg[stufe]['dauer_s']:.1f} s", flush=True)
    zeilen = erg["fein"]["zeilen"]
    familien = {}
    polylinien = {}
    for d, m in ART_FAM:
        fam = [z for z in zeilen if z["d"] == d and z["m"] == m]
        name = f"d{d}_m{m}"
        familien[name] = art_familie(fam)
        pts = [[math.log(z["Q"]), z["E"] / z["Q"]] for z in fam if z["gueltig"] and z["Q"] > 0]
        polylinien[name] = torch.tensor(pts, dtype=F64, device=DEV) if pts else torch.zeros(0, 2, dtype=F64, device=DEV)
    artgrenzen = {}
    namen_2d = [f"d2_m{m}" for m in (0, 1, 2)]
    for i in range(len(namen_2d)):
        for j in range(i + 1, len(namen_2d)):
            a, b = namen_2d[i], namen_2d[j]
            artgrenzen[a + "/" + b] = schnittpunkte(polylinien[a], polylinien[b])
    erg["familien"] = familien
    erg["artgrenzen_2d_in_Q_E"] = artgrenzen
    # L3: relative Aenderung von Q und E zwischen h und 2h gegen die Variation von Q ueber omega
    aend = 0.0
    for a, b in zip(erg["grob"]["zeilen"], erg["fein"]["zeilen"]):
        if a["gueltig"] and b["gueltig"]:
            aend = max(aend, abs(a["Q"] - b["Q"]) / abs(b["Q"]), abs(a["E"] - b["E"]) / abs(b["E"]))
    variation = []
    for d, m in ART_FAM:
        qs = [z["Q"] for z in zeilen if z["d"] == d and z["m"] == m and z["gueltig"]]
        if len(qs) >= 2:
            variation.append((max(qs) - min(qs)) / min(qs))
    effekt = min(variation) if variation else 0.0
    gueltig_gleich = sum(1 for a, b in zip(erg["grob"]["zeilen"], erg["fein"]["zeilen"]) if a["gueltig"] == b["gueltig"])
    erg["L3"] = {"effekt_min_relative_Q_variation": effekt, "aenderung_max_rel_Q_E_h_gegen_2h": aend,
                 "bestanden": effekt >= L3_FAKTOR * aend,
                 "gueltigkeit_gleich": f"{gueltig_gleich} von {len(zeilen)}"}
    return erg


def bericht_artbildung(erg):
    z = [f"Artbildung (Bio 18, Zufallskarte): radiales Schiessen, Familien {ART_FAM} (d, m), "
         f"{len(erg['omega2'])} Werte omega^2, h = {ART_H} (L3 gegen 2h), gueltig = Klammer gefunden, Bahn sauber, "
         f"|Virialrest| < {ART_VIRIAL}"]
    zeilen = erg["fein"]["zeilen"]
    for d, m in ART_FAM:
        name = f"d{d}_m{m}"
        z.append(f"  Familie {name}: {erg['familien'][name]}")
        z.append("    omega^2  gueltig  Q            E            E/Q       Virialrest  r_Ladung  f_max")
        fam = [r for r in zeilen if r["d"] == d and r["m"] == m]
        for k, r in enumerate(fam):
            if k % 4 == 0 or k == len(fam) - 1 or not r["gueltig"]:
                z.append(f"    {r['omega2']:.2f}     {'ja  ' if r['gueltig'] else 'NEIN'}     {r['Q']:.5e}  "
                         f"{r['E']:.5e}  {r['E'] / r['Q'] if r['Q'] else float('nan'):.6f}  {r['virial']:+.1e}  "
                         f"{r['r_ladung']:.3f}  {r['f_max']:.5f}")
    z.append(f"  Artgrenzen (Schnitte der E(Q)-Kurven der 2D-Familien, Ebene ln Q gegen E/Q): "
             f"{erg['artgrenzen_2d_in_Q_E']}")
    z.append("  3D und 2D sind nicht vergleichbar (verschiedene Raumdimension, 2D-Ladung je Laengeneinheit).")
    z.append("  " + l3_zeile(erg["L3"]))
    return z


# ================================================================ Kontrolle K0: 1D-Schuss gegen Anker

PROFIL_W2 = [0.55, 0.6, 0.7, 0.8]


def test_profil(rauch):
    """K0: qg1-Schiessen fuer die omega der 1D-Tests gegen den Anker (grob und fein); K0b: f' des Ankers gegen
    zentrale Differenzen. Im Rauchtest nur K0b."""
    erg = {"omega2": PROFIL_W2}
    x = gitter(DX / 2.0)
    abl = []
    for w2 in PROFIL_W2:
        _, fs = anker(w2, x)
        eps = 1e-5
        num = (anker(w2, x + eps)[0] - anker(w2, x - eps)[0]) / (2.0 * eps)
        abl.append((fs - num).abs().max().item())
    erg["K0b_max_abw_ableitung"] = max(abl)
    erg["K0b_bestanden"] = max(abl) <= 1e-7
    if rauch:
        return erg
    a0 = (1.0 - torch.tensor(PROFIL_W2, dtype=F64, device=DEV)).unsqueeze(1)
    t0 = uhr()
    f0, klammer = schiessen(a0)
    bahn, j_cut = profil_bahn(f0, a0)
    erg["schiessen_s"] = uhr() - t0
    abw = []
    for dx in (DX, DX / 2.0):
        f_om = profil_gitter(bahn, j_cut, a0, dx)
        xg = gitter(dx)
        for iw, w2 in enumerate(PROFIL_W2):
            abw.append((f_om[iw] - anker(w2, xg)[0]).abs().max().item())
    erg["f0_quadrat_schuss"] = (f0[:, 0] ** 2).tolist()
    erg["f0_quadrat_anker"] = [1.0 - math.sqrt(2.0 * w2 - 1.0) for w2 in PROFIL_W2]
    erg["K0_max_abw_profil"] = max(abw)
    erg["K0_bestanden"] = max(abw) <= TOL_PROFIL
    return erg


def bericht_profil(erg):
    z = [f"K0b: max |f'_Anker - zentrale Differenz| = {erg['K0b_max_abw_ableitung']:.2e} "
         f"({'bestanden' if erg['K0b_bestanden'] else 'NICHT bestanden'}, Grenze 1e-7)"]
    if "K0_max_abw_profil" in erg:
        z.append(f"K0: max |f_Schuss - f_Anker| = {erg['K0_max_abw_profil']:.2e} "
                 f"({'bestanden' if erg['K0_bestanden'] else 'NICHT bestanden'}, Grenze {TOL_PROFIL}); "
                 f"Schiessen {erg['schiessen_s']:.1f} s")
        z.append(f"   f0^2 Schuss {erg['f0_quadrat_schuss']}, Anker {erg['f0_quadrat_anker']}")
    return z


# ================================================================ Ablauf

EINDIM = {
    "katalyse": (test_katalyse, l3_katalyse, bericht_katalyse),
    "kette": (test_kette, l3_kette, bericht_kette),
    "chromatographie": (test_chromatographie, l3_chromatographie, bericht_chromatographie),
    "neuron": (test_neuron, l3_neuron, bericht_neuron),
    "wunde": (test_wunde, l3_wunde, bericht_wunde),
    "nerv": (test_nerv, l3_nerv, bericht_nerv),
}


def lauf(name, out, rauch):
    start = jetzt()
    print(f"R4-CB {name}: Start {start} auf {torch.cuda.get_device_name(0)}, torch {torch.__version__}, "
          f"Rauchtest {rauch}", flush=True)
    t0 = uhr()
    if name == "profil":
        erg = test_profil(rauch)
        zeilen = bericht_profil(erg)
    elif name == "artbildung":
        erg = test_artbildung(rauch)
        zeilen = bericht_artbildung(erg)
    else:
        test, l3, bericht = EINDIM[name]
        erg = {}
        for stufe, dx, dt in (("grob", DX, DT), ("fein", DX / 2.0, DT / 2.0)):
            t1 = uhr()
            erg[stufe] = test(dx, dt, rauch)
            erg[stufe]["dx_dt"] = [dx, dt]
            erg[stufe]["dauer_s"] = uhr() - t1
            print(f"  {name} {stufe} fertig nach {erg[stufe]['dauer_s']:.1f} s", flush=True)
        erg["L3"] = l3(erg)
        zeilen = bericht(erg)
    ende = jetzt()
    erg["start"], erg["ende"], erg["dauer_s"] = start, ende, uhr() - t0
    erg["geraet"], erg["torch"], erg["rauchtest"] = torch.cuda.get_device_name(0), torch.__version__, rauch
    erg["gpu_speicher_max_mb"] = torch.cuda.max_memory_allocated() / 2.0 ** 20
    praefix = ("rauch_" if rauch else "") + name
    with open(os.path.join(out, praefix + ".json"), "w") as fh:
        json.dump(erg, fh, indent=1)
    kopf = [f"R4-CB {name}. Start {start}, Ende {ende}, Dauer {erg['dauer_s']:.1f} s, Geraet {erg['geraet']}, "
            f"torch {erg['torch']}, GPU-Speicher max {erg['gpu_speicher_max_mb']:.0f} MB"
            + ("  RAUCHTEST: Zahlen ohne Bedeutung" if rauch else "")]
    text = "\n".join(kopf + zeilen)
    with open(os.path.join(out, praefix + "_bericht.txt"), "w") as fh:
        fh.write(text + "\n")
    print(text, flush=True)


def main():
    ap = argparse.ArgumentParser(description="R4-CB: 1D-Tests Chemie/Biologie mit Q-Baellen und Artbildung")
    ap.add_argument("test", choices=["profil", "rauch", "artbildung"] + list(EINDIM))
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "ausgabe"))
    ap.add_argument("--kat-v", default=None, help="Chem 8 dicht (R10): v-Liste mit Kommas, ersetzt KAT_V")
    ap.add_argument("--kat-t", type=float, default=None, help="Chem 8 dicht (R10): Laufzeit T, ersetzt KAT_T")
    args = ap.parse_args()
    global KAT_V, KAT_T
    if args.kat_v:
        KAT_V = [float(s) for s in args.kat_v.split(",")]
    if args.kat_t is not None:
        KAT_T = args.kat_t
    if not torch.cuda.is_available():
        raise SystemExit("Kein CUDA-Geraet: Abbruch (kein CPU-Ausweg).")
    os.makedirs(args.out, exist_ok=True)
    if args.test != "rauch":
        lauf(args.test, args.out, False)
        return
    fehler = []
    for name in ["profil"] + list(EINDIM) + ["artbildung"]:
        try:
            lauf(name, args.out, True)
        except Exception:                                    # Rauchtest: alle Teile pruefen, Fehler sammeln
            traceback.print_exc()
            fehler.append(name)
    print(f"Rauchtest Ende {jetzt()}: " + ("alle Teile durchgelaufen" if not fehler else f"FEHLER in {fehler}"),
          flush=True)
    if fehler:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
