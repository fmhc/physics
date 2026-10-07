#!/usr/bin/env python3
"""Runde 2, Folgeauftrag (Leitung 30.09. 01:41 und 01:48): Test 2F (Absorption feiner) und Test 3K (Verschmelzungskarte).

Neue Fassung neben tests1d.py; die alte Datei bleibt unveraendert und wird hier importiert (Profile, Baelle, Pakete,
Zeitschritt, Daempfung, Anker). Physik unveraendert. Ungetestet abgegeben (Interpreterverbot auf dem Laptop).
Plan, Aufrufe, Vorhersagen und Latten: PLAN-FEIN.md.

Test 2F: Ball omega^2 = 0,7, schwache Pakete wie Test 2. Gitterstufen k = 0, 1, 2, 3 mit dx = 0,1 / 2^k, dt = 0,05 / 2^k.
  Messung alle 0,1: Ladungs- und Energiefluss bei x = -30 und +30, Ladung in |x| < 30 und im Kern |x| < 4,78,
  Breite, psi an beiden Ebenen (Wiederabstrahlung). Auslesen bei t = 300, 500, 1000, 1500 (soweit T reicht).
Test 3K: grosser Ball 0,55 ruhend, kleiner Ball omega^2 in {0,55 ... 0,90} mit v in {0,02 ... 0,2}, Kontaktphase 0,
  dazu pi fuer 0,55 und 0,70. Ausgang verschmolzen, getrennt, durchgelaufen oder gebunden; Ladungsuebertrag.

Aufruf (im Ordner mit tests1d.py):
  python tests1d_fein.py --test 2f --stufen 0,1 --nu kern --T 1500 --probe --profil P --out O
  python tests1d_fein.py --test 2f --stufen 2 --nu kern --T 1500 --probe --profil P --vorher O/fein_ergebnis.json --out O2
  python tests1d_fein.py --test 3k --out O3 [--profil O3/profil_3k.pt]
  --nu kern | raster | Liste (z. B. 2.3,2.325,2.35); --rauch: Laufzeit x 0,05, nur Durchlaufprobe.
"""
import argparse
import json
import math
import os
import traceback

import torch

import tests1d as t1

DEV, F64, PI = t1.DEV, t1.F64, t1.PI
gf, teilen = t1.gf, t1.teilen

# ---- Test 2F ----
NU_LISTEN = {
    # zwei Kontrollen, Spitze (nahe omega + Omega_2 = 2,330), je ein Nachbar, zwei Frequenzen ueber 1 + 2 omega = 2,673
    "kern": [1.5, 1.9, 2.25, 2.325, 2.375, 2.75, 2.90],
    "raster": [1.5, 1.9] + [round(2.10 + 0.025 * i, 3) for i in range(21)],
    "g06": [1.5] + [round(1.80 + 0.05 * i, 2) for i in range(15)],   # Groessenprobe 0,6: 1,80 ... 2,50 (2 omega + 1 = 2,55)
    "g08": [1.5] + [round(1.80 + 0.05 * i, 2) for i in range(19)],   # Groessenprobe 0,8: 1,80 ... 2,70 (2 omega + 1 = 2,79)
}
NU_PROBE = 2.325                               # Amplitudenprobe (nur mit --probe)
EPS0, EPS_PROBE = 1e-3, [5e-4, 2e-3]
T2F_MESS = 0.1
AUSLESE = [300.0, 500.0, 1000.0, 1500.0]
T_SPAET = 300.0                                # danach nur noch Wiederabstrahlung (direkter Durchgang bei t ~ 70 bis 200)
BAND_OMEGA2 = (1.2, 1.8)                       # Suchband fuer die innere Mode Omega_2
BAND_NU = (1.0, 3.5)                           # Suchband fuer die wieder abgestrahlte Frequenz
NU_WELLE = 2.3                                 # Punkte je Wellenlaenge werden fuer dieses nu gemeldet

# ---- Test 3K ----
W2_GROSS3K = 0.55
W2_KLEIN3K = [0.55, 0.60, 0.65, 0.70, 0.80, 0.90]
V3K = [0.02, 0.05, 0.10, 0.20]
PI_KONTROLLE = [0.55, 0.70]
ANLAUF = 6.0                                   # Startabstand = Kontaktabstand + 6; freier Kontakt bei t = 6 / v
T3K, T3K_MESS = 600.0, 0.5
KLASS_NACH = 250.0                             # Einordnung 250 Zeiteinheiten nach dem freien Kontakt
ABSTAND_MIN = 3.0                              # zweites Maximum mindestens 3 vom hoechsten entfernt


# ---------------------------------------------------------------- Hilfen

def kumulativ(t, y):
    """Laufendes Trapezintegral ueber die Zeit (Achse 0)."""
    d = 0.5 * (y[1:] + y[:-1]) * (t[1:] - t[:-1]).reshape(-1, *([1] * (y.dim() - 1)))
    return torch.cat([torch.zeros_like(y[:1]), torch.cumsum(d, dim=0)], dim=0)


def index_bei(t, tt):
    return int(torch.argmin((t - tt).abs()).item())


def spitze_band(t, y, t_ab, lo, hi, pad=8):
    """Groesste Spitze der FFT von y (reell oder komplex, e^(-i nu t) zaehlt als +nu) ab t_ab im Band [lo, hi].
    Hann-Fenster, 8-fach mit Nullen aufgefuellt, Parabel durch die Spitze. Rueckgabe Omega und Amplitude."""
    wahl = t >= t_ab - 1e-9
    ts, ys = t[wahl], y[wahl]
    n = ys.shape[0]
    if n < 32:
        return {"Omega": float("nan"), "amplitude": float("nan")}
    fen = torch.hann_window(n, periodic=False, dtype=F64, device=DEV)
    ys = (ys - ys.mean()) * fen
    nf = pad * n
    spek = torch.fft.fft(ys.conj(), n=nf).abs()
    d_om = 2.0 * PI / (nf * (ts[1] - ts[0]).item())
    om = torch.arange(nf, device=DEV).to(F64) * d_om
    band = (om >= lo) & (om <= hi) & (torch.arange(nf, device=DEV) < nf // 2)
    k = int(torch.argmax(torch.where(band, spek, torch.zeros_like(spek))).item())
    if k < 1 or k >= nf - 1:
        return {"Omega": float("nan"), "amplitude": float("nan")}
    a, b, c = spek[k - 1].item(), spek[k].item(), spek[k + 1].item()
    nenner = a - 2.0 * b + c
    delta = 0.5 * (a - c) / nenner if nenner != 0.0 else 0.0
    return {"Omega": (k + delta) * d_om, "amplitude": 2.0 * b / fen.sum().item()}


def abklingrate(t, y, t_ab, om):
    """Amplitudenrate der Komponente om (reelles y) aus zwei Haelften ab t_ab: ln(A1/A2) / Abstand der Mitten."""
    wahl = t >= t_ab - 1e-9
    ts, ys = t[wahl], y[wahl]
    n = ys.shape[0]
    if n < 64 or not math.isfinite(om):
        return float("nan")
    werte = []
    for s in (slice(0, n // 2), slice(n // 2, n)):
        tt, yy = ts[s], ys[s]
        fen = torch.hann_window(yy.shape[0], periodic=False, dtype=F64, device=DEV)
        proj = ((yy - yy.mean()) * fen * torch.exp(-1j * om * tt)).sum().abs() * 2.0 / fen.sum()
        werte.append((proj.item(), tt.mean().item()))
    (a1, m1), (a2, m2) = werte
    return math.log(a1 / a2) / (m2 - m1) if a1 > 0.0 and a2 > 0.0 else float("nan")


def rms_rate(t, y, t_ab):
    """Amplitudenrate eines komplexen Signals aus dem Effektivwert in zwei Haelften ab t_ab."""
    wahl = t >= t_ab - 1e-9
    ts, ys = t[wahl], y[wahl]
    n = ys.shape[0]
    if n < 64:
        return float("nan")
    r1, r2 = ys[: n // 2].abs().pow(2).mean().sqrt().item(), ys[n // 2:].abs().pow(2).mean().sqrt().item()
    m1, m2 = ts[: n // 2].mean().item(), ts[n // 2:].mean().item()
    return math.log(r1 / r2) / (m2 - m1) if r1 > 0.0 and r2 > 0.0 else float("nan")


def gitter_verschiebung(nu, dx, dt):
    """Frequenzfehler eines Pakets mit Wellenzahl k(nu) auf dem Gitter: Ortsdispersion plus Verlet-Zeitschritt."""
    k = math.sqrt(nu * nu - 1.0)
    nu_d = math.sqrt(1.0 + (4.0 / dx ** 2) * math.sin(0.5 * k * dx) ** 2)
    return (2.0 / dt) * math.asin(0.5 * nu_d * dt) - nu


def zahl(v, fmt):
    return format(v, fmt) if isinstance(v, (int, float)) and math.isfinite(v) else "-"


def parabel3(xs, ys):
    """Parabel y = a x^2 + b x + c durch drei Punkte; Rueckgabe (x_Scheitel, y_Scheitel, a) oder None."""
    (x1, x2, x3), (y1, y2, y3) = xs, ys
    nenner = (x1 - x2) * (x1 - x3) * (x2 - x3)
    if nenner == 0.0:
        return None
    a = (x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / nenner
    b = (x3 * x3 * (y1 - y2) + x2 * x2 * (y3 - y1) + x1 * x1 * (y2 - y3)) / nenner
    c = (x2 * x3 * (x2 - x3) * y1 + x3 * x1 * (x3 - x1) * y2 + x1 * x2 * (x1 - x2) * y3) / nenner
    if a == 0.0:
        return None
    return -b / (2.0 * a), c - b * b / (4.0 * a), a


# ---------------------------------------------------------------- Test 2F

def paket_eps(x, nu, eps):
    psi, vel = t1.paket(x, nu)
    f = eps / t1.EPS_PAKET
    return f * psi, f * vel


def laeufe_2f(nus, probe):
    laeufe = [{"art": "ball+paket", "nu": nu, "eps": EPS0} for nu in nus]
    laeufe += [{"art": "paket", "nu": nu, "eps": EPS0} for nu in nus]
    laeufe += [{"art": "ball"}, {"art": "stoss_q"}, {"art": "stoss_alt"}]
    if probe:                                   # eps = 5e-4 an allen nu >= 2 (ohne Kontrollen), 2e-3 zusaetzlich an NU_PROBE
        laeufe += [{"art": "ball+paket", "nu": nu, "eps": EPS_PROBE[0]} for nu in nus if nu >= 2.0]
        if NU_PROBE in nus:
            laeufe += [{"art": "ball+paket", "nu": NU_PROBE, "eps": EPS_PROBE[1]}]
    return laeufe


def r_kern(w2):
    """Kernradius: halbe Halbwertsbreite + 3 (0,70: 4,78)."""
    return 0.5 * t1.fwhm(w2) + 3.0


def bauen_2f(prof, laeufe, x, w2):
    i_z = prof["w2"].index(w2)
    b0 = t1.ball(prof, i_z, x, 0.0)
    felder = []
    for r in laeufe:
        if r["art"] == "ball+paket":
            felder.append(t1.summe([b0, paket_eps(x, r["nu"], r["eps"])]))
        elif r["art"] == "paket":
            felder.append(paket_eps(x, r["nu"], r["eps"]))
        elif r["art"] == "ball":
            felder.append(b0)
        elif r["art"] == "stoss_q":                              # Stoss bei fester Ladung: psi x 1,01, psi_t / 1,01
            felder.append(((1.0 + t1.ETA_STOSS) * b0[0], b0[1] / (1.0 + t1.ETA_STOSS)))
        else:                                                   # alter Stoss aus tests1d (Ladung + 2 %)
            felder.append(t1.gestossen(b0))
    return t1.stapel(felder)


def messen_2f(x, dx, w2):
    i0, di = int(round(t1.L_BOX / dx)), int(round(t1.X_EBENE / dx))
    ebenen = (i0 - di, i0 + di)
    mitte = (x.abs() < t1.X_EBENE).to(F64)
    kern = (x.abs() < r_kern(w2)).to(F64)

    def messen(psi, vel):
        werte = []
        for i in ebenen:
            px = (psi[:, i + 1] - psi[:, i - 1]) / (2.0 * dx)
            werte.append(-2.0 * (psi[:, i] * px.conj()).imag)       # Ladungsfluss
            werte.append(-2.0 * (vel[:, i] * px.conj()).real)       # Energiefluss
        s = psi.real ** 2 + psi.imag ** 2
        rho = 2.0 * (psi * vel.conj()).imag
        werte += [(rho * mitte).sum(1) * dx, (rho * kern).sum(1) * dx, t1.breite_s(x, s, mitte)]
        for i in (ebenen[1], ebenen[0]):
            for d in (-1, 0, 1):
                werte += [psi[:, i + d].real, psi[:, i + d].imag]
        return torch.stack(werte, dim=1)
    return messen
# Spalten: 0 jL, 1 SL, 2 jR, 3 SR, 4 Q(|x|<30), 5 Q(Kern), 6 Breite,
#          7 bis 12 Re/Im psi bei x = +30 - dx, +30, +30 + dx; 13 bis 18 dasselbe bei x = -30


def ebene(daten, links):
    """psi an den drei Punkten einer Ebene als (M, B, 3) komplex."""
    a = 13 if links else 7
    return torch.stack([torch.complex(daten[:, :, a + 2 * d], daten[:, :, a + 2 * d + 1]) for d in range(3)], dim=2)


def kanalfluesse(t, p3, dx):
    """Integrierter Ladungsfluss getrennt nach Teilchen (e^(-i nu t), nu > 0) und Antiteilchen (e^(+i nu t)).
    p3: (M, 3) komplex an x - dx, x, x + dx. Zerlegung per FFT ueber die ganze Zeitreihe; Kreuzterme mitteln weg."""
    m = p3.shape[0]
    spek = torch.fft.fft(p3, dim=0)
    k = torch.arange(m, device=DEV)
    teil = (k > m // 2).to(F64).unsqueeze(1)                   # negative FFT-Frequenzen = e^(-i nu t)
    anti = ((k > 0) & (k < (m + 1) // 2)).to(F64).unsqueeze(1)
    aus = []
    for maske in (teil, anti):
        q = torch.fft.ifft(spek * maske, dim=0)
        qx = (q[:, 2] - q[:, 0]) / (2.0 * dx)
        j = -2.0 * (q[:, 1] * qx.conj()).imag
        aus.append(gf(t1.integral(t, j.unsqueeze(1))[0]))
    return aus


def test_2f(prof, nus, stufen, t_end, probe, w2):
    laeufe = laeufe_2f(nus, probe)
    aus, reihen = {}, {}
    for k in stufen:
        dx, dt = t1.DX / 2 ** k, t1.DT / 2 ** k
        x = t1.gitter(dx)
        psi, vel = bauen_2f(prof, laeufe, x, w2)
        t0 = t1.uhr()
        t, daten = t1.entwickeln(psi, vel, dx, dt, t_end, T2F_MESS, messen_2f(x, dx, w2))
        sek = t1.uhr() - t0
        print(f"Test 2F Stufe {k}: {psi.shape[0]} Laeufe x {psi.shape[1]} Punkte, dx = {dx}, T = {t_end}, {sek:.1f} s",
              flush=True)
        del psi, vel
        aus[str(k)] = auswertung_2f(laeufe, t, daten, dx, dt, w2)
        aus[str(k)]["sek"] = sek
        reihen[str(k)] = {"t": t.cpu(), "daten": daten.cpu()}
    return laeufe, aus, reihen


def auswertung_2f(laeufe, t, daten, dx, dt, w2):
    T = t[-1].item()
    idx = {(r["art"], r.get("nu"), r.get("eps")): i for i, r in enumerate(laeufe)}
    o = idx[("ball", None, None)]
    phi = kumulativ(t, daten[:, :, 0:4])
    qm, qk = daten[:, :, 4], daten[:, :, 5]
    ebene_r, ebene_l = ebene(daten, False), ebene(daten, True)
    psi_r, psi_l = ebene_r[:, :, 1], ebene_l[:, :, 1]
    zeiten = sorted(set([tt for tt in AUSLESE if tt < T - 1e-9] + [T]))
    # Randreflexion: nach T_SPAET nach innen laufender Fluss an beiden Ebenen (rechts j < 0, links j > 0)
    spaet = (t >= T_SPAET - 1e-9).to(F64).unsqueeze(1)
    rueck = t1.integral(t, spaet * (torch.relu(-daten[:, :, 2]) + torch.relu(daten[:, :, 0])))
    zeilen = []
    for i, r in enumerate(laeufe):
        if r["art"] != "ball+paket":
            continue
        p = idx[("paket", r["nu"], EPS0)]
        skal = (r["eps"] / EPS0) ** 2                          # Freipaket skaliert exakt mit eps^2
        ein_q, ein_e = skal * gf(phi[-1, p, 0]), skal * gf(phi[-1, p, 1])
        z = {"nu": r["nu"], "eps": r["eps"], "ein_Q": ein_q}
        fl, fr = gf(phi[-1, i, 0] - phi[-1, o, 0]), gf(phi[-1, i, 2] - phi[-1, o, 2])
        z["T_Q"], z["R_Q"] = teilen(fr, ein_q), teilen(ein_q - fl, ein_q)
        z["auslese"] = []
        for tt in zeiten:
            m = index_bei(t, tt)
            w = {"t": gf(t[m])}
            for g, cl, cr, ein in (("Q", 0, 2, ein_q), ("E", 1, 3, ein_e)):
                fl, fr = gf(phi[m, i, cl] - phi[m, o, cl]), gf(phi[m, i, cr] - phi[m, o, cr])
                fl0, fr0 = skal * gf(phi[m, p, cl]), skal * gf(phi[m, p, cr])
                w["dA_" + g] = teilen((fl - fr) - (fl0 - fr0), ein)   # gespeichert, ohne freien Durchlauf
            dq_m = gf((qm[m, i] - qm[m, o]) - (qm[0, i] - qm[0, o])) - skal * gf(qm[m, p] - qm[0, p])
            dq_k = gf((qk[m, i] - qk[m, o]) - (qk[0, i] - qk[0, o])) - skal * gf(qk[m, p] - qk[0, p])
            w["kern"], w["aussen"] = teilen(dq_k, ein_q), teilen(dq_m - dq_k, ein_q)
            w["bilanzrest"] = teilen(dq_m, ein_q) - w["dA_Q"]
            z["auslese"].append(w)
        z["dA500_Q"] = z["auslese"][min(range(len(zeiten)), key=lambda j: abs(zeiten[j] - 500.0))]["dA_Q"]
        z["dA_ende_Q"] = z["auslese"][-1]["dA_Q"]
        pos = [w for w in z["auslese"] if w["t"] >= 500.0 - 1e-6 and math.isfinite(w["dA_Q"])]
        if len(pos) >= 2 and pos[0]["dA_Q"] > 0.0 and pos[-1]["dA_Q"] > 0.0:
            z["speicher_rate"] = math.log(pos[0]["dA_Q"] / pos[-1]["dA_Q"]) / (pos[-1]["t"] - pos[0]["t"])
            z["speicher_verhaeltnis"] = pos[-1]["dA_Q"] / pos[0]["dA_Q"]
        else:
            z["speicher_rate"], z["speicher_verhaeltnis"] = float("nan"), float("nan")
        # Verzoegerung der durchgelassenen Welle: Schwerpunkt des Flusses bei x = +30 gegen das freie Paket
        jb, jp = daten[:, i, 2] - daten[:, o, 2], skal * daten[:, p, 2]
        z["tau_schwerpunkt"] = teilen(gf((t * jb).sum()), gf(jb.sum())) - teilen(gf((t * jp).sum()), gf(jp.sum()))
        # Phase der durchgelassenen Welle gegen das freie Paket (tau = d phi_T / d nu nach der Schleife)
        frei = psi_r[:, p] * (r["eps"] / EPS0)
        ueberlapp = ((psi_r[:, i] - psi_r[:, o]) * frei.conj()).sum()
        z["phase_T"] = gf(torch.angle(ueberlapp))
        z["betrag_T"] = teilen(gf(ueberlapp.abs()), gf((frei.abs() ** 2).sum()))
        # Randreflexion: nach innen zurueckkommender Fluss nach t = 300, ohne Ball und mit Ball (Ball allein abgezogen)
        z["rand_rueck_frei"] = teilen(skal * gf(rueck[p]), ein_q)
        z["rand_rueck_ball"] = teilen(gf(rueck[i] - rueck[o]), ein_q)
        # Flussbilanz nach Teilchen- und Antiteilchenkanal (Ball allein abgezogen; Vorzeichen: Fluss nach rechts)
        kan = {}
        for seite, eb in (("R", ebene_r), ("L", ebene_l)):
            kan[seite] = kanalfluesse(t, eb[:, i] - eb[:, o], dx) + kanalfluesse(t, eb[:, p] * (r["eps"] / EPS0), dx)
        z["kanal"] = {"teilchen_durch": teilen(kan["R"][0], ein_q),
                      "teilchen_reflektiert": teilen(kan["L"][2] - kan["L"][0], ein_q),
                      "antiteilchen_rechts": teilen(kan["R"][1], ein_q),
                      "antiteilchen_links": teilen(kan["L"][1], ein_q),
                      "frei_teilchen_durch": teilen(kan["R"][2], ein_q),
                      "frei_antiteilchen": teilen(kan["R"][3] + kan["L"][3], ein_q)}
        for seite, sig in (("rechts", psi_r), ("links", psi_l)):
            d = sig[:, i] - sig[:, o]
            sp = spitze_band(t, d, T_SPAET, BAND_NU[0], BAND_NU[1])
            z["abstrahlung_" + seite] = {"nu": sp["Omega"], "amplitude": sp["amplitude"],
                                         "amplitudenrate": rms_rate(t, d, T_SPAET)}
        zeilen.append(z)
    reihe = sorted([z for z in zeilen if z["eps"] == EPS0], key=lambda z: z["nu"])
    for z in zeilen:
        z["tau_phase"] = float("nan")
    for j in range(1, len(reihe) - 1):                          # tau = d phi_T / d nu, nur bei Rasterabstand <= 0,1
        h1, h2 = reihe[j]["nu"] - reihe[j - 1]["nu"], reihe[j + 1]["nu"] - reihe[j]["nu"]
        if max(h1, h2) <= 0.1 + 1e-9:
            d1 = (reihe[j]["phase_T"] - reihe[j - 1]["phase_T"] + PI) % (2.0 * PI) - PI
            d2 = (reihe[j + 1]["phase_T"] - reihe[j]["phase_T"] + PI) % (2.0 * PI) - PI
            reihe[j]["tau_phase"] = (d1 + d2) / (h1 + h2)
    breite = daten[:, :, 6]
    om_ball = math.sqrt(w2)
    moden = {}
    for name in ("stoss_q", "stoss_alt", "ball"):
        j = idx[(name, None, None)]
        sp = spitze_band(t, breite[:, j], T / 8.0, BAND_OMEGA2[0], BAND_OMEGA2[1])
        moden[name] = {"Omega_2": sp["Omega"], "amplitude": sp["amplitude"],
                       "ladungsrate": 2.0 * abklingrate(t, breite[:, j], T / 8.0, sp["Omega"]),
                       "schwelle": spitze_band(t, breite[:, j], T / 8.0, 0.1, 0.3)["Omega"]}
    om2 = moden["stoss_q"]["Omega_2"]
    nu_res = om_ball + om2 if math.isfinite(om2) else float("nan")
    aus = {"w2": w2, "dx": dx, "dt": dt, "T": T, "zeilen": zeilen, "moden": moden, "nu_res": nu_res,
           "punkte_je_wellenlaenge_nu_2_3": 2.0 * PI / (math.sqrt(NU_WELLE ** 2 - 1.0) * dx),
           "gitter_verschiebung_bei_nu_res": gitter_verschiebung(nu_res, dx, dt) if math.isfinite(nu_res) else float("nan"),
           "rand_rueck_frei_max": max([abs(z["rand_rueck_frei"]) for z in zeilen if math.isfinite(z["rand_rueck_frei"])]
                                      or [float("nan")])}
    # Spitzenlage: Parabel durch das groesste dA500 (eps0, ohne Kontrolle 1,5) und seine zwei Nachbarn
    rast = sorted([(z["nu"], z["dA500_Q"]) for z in zeilen if z["eps"] == EPS0 and z["nu"] > 1.55
                   and math.isfinite(z["dA500_Q"])])
    aus["nu_spitze"], aus["dA_spitze"], aus["sigma_nu"] = float("nan"), float("nan"), float("nan")
    if len(rast) >= 3:
        j = max(range(len(rast)), key=lambda q: rast[q][1])
        if 0 < j < len(rast) - 1:
            xs, ys = [rast[j + d][0] for d in (-1, 0, 1)], [rast[j + d][1] for d in (-1, 0, 1)]
            scheitel = parabel3(xs, ys)
            if scheitel is not None and scheitel[2] < 0.0:
                aus["nu_spitze"], aus["dA_spitze"] = scheitel[0], scheitel[1]
            if min(ys) > 0.0:
                log_scheitel = parabel3(xs, [math.log(y) for y in ys])
                if log_scheitel is not None and log_scheitel[2] < 0.0:
                    aus["sigma_nu"] = math.sqrt(-0.5 / log_scheitel[2])   # ln y = c - (nu - nu0)^2 / (2 sigma^2)
    basis = {z["nu"]: z["dA500_Q"] for z in zeilen if z["eps"] == EPS0}
    aus["amplitudenprobe"] = [{"nu": z["nu"], "eps": z["eps"],
                               "verhaeltnis": teilen(z["dA500_Q"], basis.get(z["nu"], float("nan")))}
                              for z in zeilen if z["eps"] != EPS0]
    return aus


def urteil_folge(folge):
    """Urteil ueber die letzten drei Stufen einer Folge dA500 (vorab festgelegt, PLAN-FEIN.md Abschnitt 3)."""
    a0, a1, a2 = folge[-3:]
    d0, d1 = a0 - a1, a1 - a2
    q = abs(d1) / abs(d0) if d0 != 0.0 else float("nan")
    a_inf = a2 - d1 / 3.0                                     # Richardson fuer Fehler ~ dx^2
    p_obs = math.log2(1.0 / q) if q > 0.0 and math.isfinite(q) else float("nan")
    if max(abs(a1), abs(a2)) < 1e-4:
        u = "kein Effekt"
    elif a2 > 0.0 and a_inf <= 0.2 * a2:
        u = "Artefakt"
    elif math.isfinite(q) and q <= 0.3 and a_inf >= 0.5 * a2:
        u = "konvergiert"
    else:
        u = "unklar"
    return {"q": q, "p_beob": p_obs, "richardson": a_inf, "urteil": u}


def vergleich_2f(alle):
    stufen = sorted(alle, key=int)
    tab = {}
    for k in stufen:
        for z in alle[k]["zeilen"]:
            if z["eps"] == EPS0:
                tab.setdefault(z["nu"], {})[k] = z["dA500_Q"]
    folgen = []
    for nu in sorted(tab):
        ks = sorted(tab[nu], key=int)
        f = {"nu": nu, "stufen": ks, "dA500_Q": [tab[nu][k] for k in ks]}
        if len(ks) >= 3:
            f.update(urteil_folge(f["dA500_Q"]))
        folgen.append(f)
    lage = [{"stufe": k, "nu_spitze": alle[k].get("nu_spitze"), "dA_spitze": alle[k].get("dA_spitze"),
             "nu_res": alle[k].get("nu_res"), "Omega_2": alle[k]["moden"]["stoss_q"]["Omega_2"],
             "gitter_verschiebung": alle[k].get("gitter_verschiebung_bei_nu_res")} for k in stufen]
    spitzen = [alle[k].get("dA_spitze") for k in stufen]
    spitzen = [s for s in spitzen if isinstance(s, float) and math.isfinite(s)]
    return {"folgen": folgen, "lage": lage,
            "spitzenhoehe": urteil_folge(spitzen) if len(spitzen) >= 3 else None}


def bericht_2f(ergebnis):
    w2 = ergebnis["w2"]
    zz = [f"Test 2F Absorption feiner, Ball omega^2 = {w2}, Kern |x| < {r_kern(w2):.2f}, Ebenen x = -30/+30. "
          "dA = gespeicherter Anteil des Einstroms (freier Durchlauf abgezogen)."]
    for k, st in sorted(ergebnis["stufen"].items(), key=lambda kv: int(kv[0])):
        mo = st["moden"]
        zz.append(f"  Stufe {k}: dx = {st['dx']}, dt = {st['dt']}, T = {st['T']:.0f}, {st.get('sek', float('nan')):.1f} s, "
                  f"Punkte je Wellenlaenge bei nu = {NU_WELLE}: {st['punkte_je_wellenlaenge_nu_2_3']:.1f}, "
                  f"Randrueckstrom ohne Ball max {zahl(st['rand_rueck_frei_max'], '.1e')}")
        zz.append(f"    Resonanzkandidat Omega_2 (nu - omega ~ 1,48), Stoss bei fester Ladung "
                  f"{zahl(mo['stoss_q']['Omega_2'], '.5f')}, Ladungsrate {zahl(mo['stoss_q']['ladungsrate'], '.2e')}; "
                  f"alter Stoss {zahl(mo['stoss_alt']['Omega_2'], '.5f')}; ruhender Ball {zahl(mo['ball']['Omega_2'], '.5f')}; "
                  f"Kante 1 - omega {1.0 - math.sqrt(st['w2']):.4f}, gemessen {zahl(mo['stoss_q']['schwelle'], '.4f')}")
        zz.append(f"    nu_res = omega + Omega_2 = {zahl(st['nu_res'], '.5f')}; Gitterverschiebung des Pakets dort "
                  f"{zahl(st['gitter_verschiebung_bei_nu_res'], '+.5f')}; Spitze nu = {zahl(st['nu_spitze'], '.5f')}, "
                  f"dA = {zahl(st['dA_spitze'], '.3e')}, Breite sigma_nu = {zahl(st['sigma_nu'], '.4f')}")
        if st.get("amplitudenprobe"):
            zz.append("    Amplitudenprobe dA500(eps)/dA500(1e-3) (linear 1; A ~ eps^2: 0,25 bzw. 4; A ~ 1/eps: 2 bzw. 0,5): "
                      + ", ".join(f"nu {a['nu']:.3f} eps {a['eps']:.0e}: {zahl(a['verhaeltnis'], '.3f')}"
                                  for a in st["amplitudenprobe"]))
        zz.append("    nu | eps | T_Q | R_Q | dA_Q(t) je Auslese [Kern, aussen] | dA_E Ende | Speicherverhaeltnis, Rate | "
                  "tau Schwerpunkt, tau Phase | Wiederabstrahlung rechts nu (Rate) | Randrueckstrom mit Ball")
        for z in st["zeilen"]:
            aus = "; ".join(f"t{w['t']:.0f}: {zahl(w['dA_Q'], '+.2e')} [{zahl(w['kern'], '+.1e')}, "
                            f"{zahl(w['aussen'], '+.1e')}]" for w in z["auslese"])
            ab = z["abstrahlung_rechts"]
            zz.append(f"    {z['nu']:.3f} | {z['eps']:.0e} | {zahl(z['T_Q'], '.6f')} | {zahl(z['R_Q'], '.2e')} | {aus} | "
                      f"{zahl(z['auslese'][-1]['dA_E'], '+.2e')} | {zahl(z['speicher_verhaeltnis'], '.3f')}, "
                      f"{zahl(z['speicher_rate'], '.2e')} | {zahl(z['tau_schwerpunkt'], '+.3f')}, "
                      f"{zahl(z['tau_phase'], '+.2f')} | {zahl(ab['nu'], '.4f')} ({zahl(ab['amplitudenrate'], '.2e')}) | "
                      f"{zahl(z['rand_rueck_ball'], '.1e')}")
            ka = z["kanal"]
            zz.append(f"      Kanaele: Teilchen durch {zahl(ka['teilchen_durch'], '.6f')}, reflektiert "
                      f"{zahl(ka['teilchen_reflektiert'], '.2e')}; Antiteilchen rechts {zahl(ka['antiteilchen_rechts'], '+.2e')}, "
                      f"links {zahl(ka['antiteilchen_links'], '+.2e')}; frei: Teilchen {zahl(ka['frei_teilchen_durch'], '.6f')}, "
                      f"Antiteilchen {zahl(ka['frei_antiteilchen'], '+.1e')}")
    v = ergebnis["vergleich"]
    zz.append("  Stufenvergleich dA_Q bei t = 500 (Urteil nach PLAN-FEIN.md; Richardson fuer dx^2):")
    for f in v["folgen"]:
        zeile = f"    nu {f['nu']:.3f}: " + " -> ".join(zahl(a, '.3e') for a in f["dA500_Q"]) + f" (Stufen {','.join(f['stufen'])})"
        if "urteil" in f:
            zeile += (f"; q = {zahl(f['q'], '.3f')}, p = {zahl(f['p_beob'], '.2f')}, Richardson "
                      f"{zahl(f['richardson'], '.3e')}: {f['urteil']}")
        zz.append(zeile)
    for la in v["lage"]:
        zz.append(f"    Stufe {la['stufe']}: Spitze {zahl(la['nu_spitze'], '.4f')} gegen nu_res {zahl(la['nu_res'], '.4f')} "
                  f"(Gitterverschiebung {zahl(la['gitter_verschiebung'], '+.4f')})")
    if v["spitzenhoehe"]:
        s = v["spitzenhoehe"]
        zz.append(f"    Spitzenhoehe (Parabel): q = {zahl(s['q'], '.3f')}, Richardson {zahl(s['richardson'], '.3e')}: "
                  f"{s['urteil']}")
    return zz


# ---------------------------------------------------------------- Test 3K

def laeufe_3k():
    wb = math.sqrt(W2_GROSS3K)
    laeufe = []
    for w2k in W2_KLEIN3K:
        d_k = 1.2 * 0.5 * (t1.fwhm(W2_GROSS3K) + t1.fwhm(w2k))
        for v in V3K:
            for dc in [0.0] + ([PI] if w2k in PI_KONTROLLE else []):
                gam = 1.0 / math.sqrt(1.0 - v * v)
                t_c = ANLAUF / v
                laeufe.append({"w2k": w2k, "v": v, "delta_soll": dc, "x0": -(d_k + ANLAUF), "d_kontakt": d_k,
                               "t_kontakt_frei": t_c, "phase_klein": (math.sqrt(w2k) / gam - wb) * t_c - dc})
    return laeufe


def test_3k(prof, faktor):
    iw = {w2: i for i, w2 in enumerate(prof["w2"])}
    laeufe = laeufe_3k()

    def bauen(x, dx):
        g0 = t1.ball(prof, iw[W2_GROSS3K], x, 0.0)
        felder = [t1.summe([g0, t1.ball(prof, iw[r["w2k"]], x, r["x0"], r["v"], r["phase_klein"])]) for r in laeufe]
        psi, vel = t1.stapel(felder)

        def messen(psi, vel):
            s = psi.real ** 2 + psi.imag ** 2
            rho = 2.0 * (psi * vel.conj()).imag
            e = vel.abs() ** 2 + (s - s * s + 0.5 * s ** 3)
            e[:, :-1] += ((psi[:, 1:] - psi[:, :-1]).abs() / dx) ** 2
            i1 = s.argmax(dim=1, keepdim=True)
            x1 = x[i1]
            lm = torch.zeros_like(s, dtype=torch.bool)
            lm[:, 1:-1] = (s[:, 1:-1] >= s[:, :-2]) & (s[:, 1:-1] >= s[:, 2:])
            kand = torch.where(lm & ((x - x1).abs() >= ABSTAND_MIN), s, torch.zeros_like(s))
            i2 = kand.argmax(dim=1, keepdim=True)
            x2 = x[i2]
            zwischen = (x > torch.minimum(x1, x2)) & (x < torch.maximum(x1, x2))
            tal = torch.where(zwischen, s, torch.full_like(s, 1e30)).min(dim=1, keepdim=True).values
            links = (x < 0.5 * (x1 + x2)).to(F64)
            fenster = ((x - x1).abs() < t1.W_KLUMPEN).to(F64)
            p1, p2 = psi.gather(1, i1), psi.gather(1, i2)
            return torch.cat([x1, x2, s.gather(1, i1), s.gather(1, i2), tal,
                              (rho * links).sum(1, keepdim=True) * dx, (rho * fenster).sum(1, keepdim=True) * dx,
                              rho.sum(1, keepdim=True) * dx, e.sum(1, keepdim=True) * dx,
                              -torch.angle(p1), -torch.angle(p2)], dim=1)
        return psi, vel, messen

    stufen = t1.stufen_rechnen("Test 3K", bauen, T3K * faktor, T3K_MESS)
    ergebnis = {s: auswertung_3k(laeufe, st["t"], st["daten"]) for s, st in stufen.items()}
    l3 = []
    for zg, zf in zip(ergebnis["grob"], ergebnis["fein"]):
        l3.append({"w2k": zg["w2k"], "v": zg["v"], "delta_soll": zg["delta_soll"],
                   "gleiche_klasse": zg["klasse"] == zf["klasse"],
                   "M": t1.l3(zg["M"], zf["M"], 0.0)})
    return {"laeufe": laeufe, "ergebnis": ergebnis, "L3": l3, "sek": {s: stufen[s]["sek"] for s in stufen}}, stufen


def auswertung_3k(laeufe, t, daten):
    T = t[-1].item()
    x1, x2, s1, s2, tal, ql, qk, qb, eb, th1, th2 = daten.unbind(dim=2)
    xl, xr = torch.minimum(x1, x2), torch.maximum(x1, x2)
    th_l = torch.where(x1 <= x2, th1, th2)
    th_r = torch.where(x1 <= x2, th2, th1)
    q_b0 = t1.anker_q_e(W2_GROSS3K)[0]
    h_b0 = 1.0 - math.sqrt(2.0 * W2_GROSS3K - 1.0)
    zeilen = []
    for b, r in enumerate(laeufe):
        q_s0 = t1.anker_q_e(r["w2k"])[0]
        h_min = min(h_b0, 1.0 - math.sqrt(2.0 * r["w2k"] - 1.0))
        zwei = (s2[:, b] >= 0.3 * h_min) & (tal[:, b] <= 0.5 * s2[:, b])
        abstand = xr[:, b] - xl[:, b]
        t_k = min(T, r["t_kontakt_frei"] + KLASS_NACH)
        m = index_bei(t, t_k)
        m0 = index_bei(t, max(0.0, t_k - 40.0))
        z = {"w2k": r["w2k"], "v": r["v"], "delta_soll": r["delta_soll"], "t_klass": gf(t[m]),
             "start_getrennt": bool(zwei[0].item()), "Q_box_0": gf(qb[0, b]), "Q_box_T": gf(qb[-1, b]),
             "E_box_0": gf(eb[0, b]), "E_box_T": gf(eb[-1, b])}
        kontakt = (~zwei) | (abstand < r["d_kontakt"])
        if bool(kontakt.any()):
            mc = int(torch.nonzero(kontakt)[0, 0].item())
            z["t_kontakt"] = gf(t[mc])
            z["dphi_kontakt"] = gf(t1.wrap(th_l[max(0, mc - 1), b] - th_r[max(0, mc - 1), b]))
        else:
            z["t_kontakt"], z["dphi_kontakt"] = float("nan"), float("nan")
        z["M"] = (gf(qk[m, b]) - q_b0) / q_s0
        dauer = gf(t[m] - t[m0])
        if not bool(zwei[m].item()):
            z["klasse"], z["q_klein_rel"] = "verschmolzen", float("nan")
        else:
            vl = gf(xl[m, b] - xl[m0, b]) / dauer if dauer > 0 else 0.0
            vr = gf(xr[m, b] - xr[m0, b]) / dauer if dauer > 0 else 0.0
            if vl < -0.25 * r["v"]:
                z["klasse"], z["q_klein_rel"] = "getrennt", gf(ql[m, b]) / q_s0
            elif vr > 0.25 * r["v"]:
                z["klasse"], z["q_klein_rel"] = "durchgelaufen", (gf(qb[m, b]) - gf(ql[m, b])) / q_s0
            else:
                z["klasse"], z["q_klein_rel"] = "gebunden", float("nan")
            z["v_links"], z["v_rechts"] = vl, vr
        z["uebertrag"] = 1.0 - z["q_klein_rel"] if math.isfinite(z["q_klein_rel"]) else (
            z["M"] if z["klasse"] == "verschmolzen" else float("nan"))
        zeilen.append(z)
    return zeilen


def bericht_3k(res):
    kurz = {"verschmolzen": "V", "getrennt": "G", "durchgelaufen": "D", "gebunden": "B"}
    zz = [f"Test 3K Verschmelzungskarte: gross {W2_GROSS3K} ruhend, klein laeuft von links an (Startabstand Kontakt + "
          f"{ANLAUF}). V verschmolzen, G getrennt (Abprall), D durchgelaufen, B gebunden ohne Verschmelzen."]
    for stufe in ("grob", "fein"):
        zeilen = res["ergebnis"][stufe]
        zz.append(f"  [{stufe}] Karte Kontaktphase 0 (Zeilen omega^2 klein, Spalten v = "
                  + ", ".join(str(v) for v in V3K) + "); in Klammern Kontaktphase pi")
        for w2k in W2_KLEIN3K:
            zellen = []
            for v in V3K:
                z0 = [z for z in zeilen if z["w2k"] == w2k and z["v"] == v and z["delta_soll"] == 0.0][0]
                zp = [z for z in zeilen if z["w2k"] == w2k and z["v"] == v and z["delta_soll"] != 0.0]
                zellen.append(kurz[z0["klasse"]] + (f"({kurz[zp[0]['klasse']]})" if zp else ""))
            zz.append(f"    {w2k:.2f} (d_omega {math.sqrt(w2k) - math.sqrt(W2_GROSS3K):+.4f}): " + "  ".join(zellen))
        zz.append("    omega^2 | v | Soll-Phase | Klasse | M | Uebertrag | t Kontakt | dphi Kontakt | t Einordnung | "
                  "Q Box 0 -> T | E Box 0 -> T | Start getrennt")
        for z in zeilen:
            zz.append(f"    {z['w2k']:.2f} | {z['v']:.2f} | {z['delta_soll']:.3f} | {z['klasse']} | {zahl(z['M'], '.3f')} | "
                      f"{zahl(z['uebertrag'], '+.3f')} | {zahl(z['t_kontakt'], '.1f')} | {zahl(z['dphi_kontakt'], '+.3f')} | "
                      f"{z['t_klass']:.0f} | {z['Q_box_0']:.4f} -> {z['Q_box_T']:.4f} | {z['E_box_0']:.4f} -> "
                      f"{z['E_box_T']:.4f} | {z['start_getrennt']}")
    n_kl = sum(1 for e in res["L3"] if e["gleiche_klasse"])
    n_m = sum(1 for e in res["L3"] if e["M"]["bestanden"])
    zz.append(f"  L3: gleiche Klasse grob/fein in {n_kl} von {len(res['L3'])} Laeufen; M-Latte in {n_m} von {len(res['L3'])}")
    return zz


# ---------------------------------------------------------------- Hauptprogramm

def schreiben(out, ausgabe, text, reihen):
    with open(os.path.join(out, "fein_bericht.txt"), "w") as fh:
        fh.write("\n".join(text) + "\n")
    torch.save(reihen, os.path.join(out, "fein_zeitreihen.pt"))
    with open(os.path.join(out, "fein_ergebnis.json"), "w") as fh:
        json.dump(ausgabe, fh, indent=1, default=str)


def main():
    ap = argparse.ArgumentParser(description="Runde 2 Folgeauftrag: 2F Absorption feiner, 3K Verschmelzungskarte")
    ap.add_argument("--test", choices=["2f", "3k"], required=True)
    ap.add_argument("--stufen", default="0,1", help="2F: Gitterstufen k (dx = 0,1/2^k), z. B. 0,1 oder 2 oder 3")
    ap.add_argument("--nu", default="kern", help="2F: kern, raster, g06, g08 oder Liste 2.3,2.325")
    ap.add_argument("--w2", type=float, default=0.70, help="2F: omega^2 des Balls (Groessenprobe 0.6 und 0.8)")
    ap.add_argument("--T", type=float, default=1500.0, help="2F: Laufzeit (Auslesen bei 300, 500, 1000, 1500)")
    ap.add_argument("--probe", action="store_true", help="2F: Amplitudenprobe eps = 5e-4 und 2e-3 bei nu = 2,325")
    ap.add_argument("--vorher", nargs="*", default=[], help="2F: fein_ergebnis.json frueherer Stufen fuer den Vergleich")
    ap.add_argument("--profil", default=None, help="gespeicherte 1D-Schiessbahnen")
    ap.add_argument("--rauch", action="store_true", help="Laufzeit x 0,05, nur Durchlaufprobe")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    if not torch.cuda.is_available():
        raise SystemExit("Kein CUDA-Geraet: Abbruch (kein CPU-Ausweg).")
    gesamt = torch.cuda.get_device_properties(0).total_memory
    torch.cuda.set_per_process_memory_fraction(min(1.0, t1.SPEICHER_GB * 2 ** 30 / gesamt))
    os.makedirs(args.out, exist_ok=True)
    faktor = 0.05 if args.rauch else 1.0
    t_start = t1.uhr()
    kopf = (f"Runde 2 tests1d_fein Start {t1.jetzt()} auf {torch.cuda.get_device_name(0)}, torch {torch.__version__}, "
            f"Test {args.test}, Rauchtest {args.rauch}, Argumente {vars(args)}")
    print(kopf, flush=True)
    ausgabe = {"start": t1.jetzt(), "geraet": torch.cuda.get_device_name(0), "argumente": vars(args), "fehler": None}
    text, reihen = [kopf, ""], {}
    try:
        if args.test == "2f":
            nus = NU_LISTEN[args.nu] if args.nu in NU_LISTEN else [float(v) for v in args.nu.split(",")]
            stufen = [int(s) for s in args.stufen.split(",")]
            prof = None
            if args.profil:
                prof = torch.load(args.profil, map_location=DEV, weights_only=False)
                if args.w2 not in prof["w2"]:
                    prof = None
            if prof is None:                                     # nur dieses omega schiessen (etwa 80 s)
                prof = t1.profile_1d([args.w2], None, os.path.join(args.out, "profil_2f.pt"))
            laeufe, aus, reihen = test_2f(prof, nus, stufen, args.T * faktor, args.probe, args.w2)
            alle = {}
            for pfad in args.vorher:
                with open(pfad) as fh:
                    frueher = json.load(fh)["2f"]["stufen"]
                alle.update({k: v for k, v in frueher.items() if abs(v.get("w2", -1.0) - args.w2) < 1e-12})
            alle.update(aus)
            ausgabe["2f"] = {"w2": args.w2, "laeufe": laeufe, "stufen": alle, "neu_gerechnet": sorted(aus, key=int),
                             "vergleich": vergleich_2f(alle)}
            text += bericht_2f(ausgabe["2f"])
        else:
            w2 = sorted(set([W2_GROSS3K] + W2_KLEIN3K))
            prof = t1.profile_1d(w2, args.profil, os.path.join(args.out, "profil_3k.pt"))
            x = t1.gitter(t1.DX)
            k0 = max(gf((t1.profil_an(prof, i, x) - t1.profil_anker(v, t1.DX)).abs().max()) for i, v in enumerate(w2))
            text.append(f"1D-Profile {w2}: K0 max |f - f_Anker| = {k0:.1e} "
                        f"({'bestanden' if k0 <= t1.TOL_PROFIL else 'NICHT bestanden'})")
            res, stufen = test_3k(prof, faktor)
            res["K0"] = k0
            ausgabe["3k"] = res
            reihen = {"laeufe": res["laeufe"],
                      "stufen": {s: {"t": st["t"].cpu(), "daten": st["daten"].cpu()} for s, st in stufen.items()}}
            text += bericht_3k(res)
    except Exception:
        ausgabe["fehler"] = traceback.format_exc()
        text += ["FEHLER:", ausgabe["fehler"]]
        print(ausgabe["fehler"], flush=True)
    ausgabe["ende"] = t1.jetzt()
    ausgabe["dauer_s"] = t1.uhr() - t_start
    ausgabe["torch_speicher_max_mb"] = torch.cuda.max_memory_allocated() / 2 ** 20
    text.append(f"Ende {ausgabe['ende']}, Dauer {ausgabe['dauer_s']:.1f} s, Torch-Speicher max "
                f"{ausgabe['torch_speicher_max_mb']:.0f} MB, Fehler: {'ja' if ausgabe['fehler'] else 'keine'}")
    schreiben(args.out, ausgabe, text, reihen)
    print("\n".join(text), flush=True)
    if ausgabe["fehler"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
