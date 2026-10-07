#!/usr/bin/env python3
"""Runde 7 (runden-v3), Karte R5F: Folge-Tests zu Runde 5 (Bio 4 Tod, Bio 3/36 Fuettern, Kavitation). Explorativ.

Modell wie Runde 5: L = |psi_t|^2 - |grad psi|^2 - U(S), U = S - S^2 + S^3/2, S = |psi|^2.

Bausteine: r5a.py und r5b.py liegen als UNVERAENDERTE Kopien daneben (sha256 in PLAN.md) und werden importiert.
  aus r5a (3D radial): familie, fam_zeile (Schiessen wie tests1d), radial_gitter, ball_radial, entwickeln_radial
                       (Velocity-Verlet fuer chi = r psi, Schwamm ab r = 110, Bad -gamma psi_t bis t_stop),
                       erste_zeit, index_ab, entfalten, fz
  aus r5b (1D):        gitter, gitter_periodisch, ball (1D-Anker), summe, stapel, dichte, ladung, energie_dichte,
                       max_im_fenster, breite_s, entwickeln (Verlet; Schwamm oder periodisch), spektrum, om_fenster,
                       fenster_idx, mittel, ende, l3, rausch_basis, born_aq, M_KMAX
Neu in r5f.py (nichts in den Bausteinen geaendert):
  - eigene Messfunktionen mit mehr Spalten (werden an entwickeln_radial bzw. entwickeln uebergeben)
  - paket_sigma = r5b.paket mit Breite sigma und Startort x0 als Argument
  - Delle mit Tiefe d (r5b.mi kannte nur die volle Delle d = 1)
  - Modul-Konstanten von r5b werden nur umgestellt: Box L_BOX/X_SPONGE (fuettern) und M_L (kavitation)
  - Auswertungen, Plausibilitaetsschranken, L3, Rohdaten-Sicherung nach jeder Stufe, --nur-auswertung
Unterbefehle:
  tod          (a) Rest unter Q_min: Oszillon oder zerlaufen? 3D radial, lange Laeufe, Spektrum im Zentrum, E im Fenster
  fuettern     (b) Aufnahme unter der Schwelle: --teil mechanik | raster55 | raster70
  kavitation   (c) dichtes Kondensat S0 = 0,70 ... 0,80 mit Delle: --teil raster [--s0 0.72] | box [--sehrfein]
  rauch        alle drei verkleinert, dazu --nur-auswertung-Pfad und Hochrechnung der Laufzeiten
Aufruf: python r5f.py <befehl> [--geraet cuda|cpu] [--out ORDNER] [--stufe grob|fein|beide] [--teil ...] [--T ...]
        [--nur-auswertung]. float64 bzw. complex128; CPU mit genau einem Faden.
"""
import argparse
import datetime
import json
import math
import os
import sys
import time
import traceback

import torch

HIER = os.path.dirname(os.path.abspath(__file__))
if HIER not in sys.path:
    sys.path.insert(0, HIER)
import r5a  # noqa: E402  (unveraenderte Kopie aus RUNDE-05/r5a)
import r5b  # noqa: E402  (unveraenderte Kopie aus RUNDE-05/r5b)

F64 = torch.float64
PI = math.pi
NAN = float("nan")
INF = float("inf")
DEV = torch.device("cpu")
ZEIT_BUDGET = 540.0          # s je Aufruf; kleintest.sh bricht bei 600 s ab
T_START = [0.0]
SPEICHER_GB = 1.5
Q_MIN = r5a.Q_MIN_R2         # 111,8441 bei omega^2 = 0,9269 (Runde 2)
fz = r5a.fz
l3 = r5b.l3

# ---- (a) tod ----
TOD_W2_START = 0.80
TOD_T, TOD_MESS = 3000.0, 0.5
R_IN, R_KERN = r5a.R_MESS, 10.0
# (Name, Profil omega^2, eta (psi und psi_t mal 1 + eta), gamma, Stopp bei Q_erw = Faktor x Q_min oder None)
TOD_LAEUFE = [("stopp 1,05 Q_min", 0.80, 0.0, 1e-3, 1.05), ("stopp 0,95 Q_min", 0.80, 0.0, 1e-3, 0.95),
              ("stopp 0,9 Q_min", 0.80, 0.0, 1e-3, 0.90), ("stopp 0,8 Q_min", 0.80, 0.0, 1e-3, 0.80),
              ("Dauerabfluss 1e-3", 0.80, 0.0, 1e-3, None), ("ohne Abfluss 0,80", 0.80, 0.0, 0.0, None),
              ("ohne Abfluss 0,90", 0.90, 0.0, 0.0, None), ("Klumpen 0,927 x 0,95", 0.927, -0.05, 0.0, None)]
TOD_SPALTEN = ["Q_tot", "Q_in", "Q_kern", "E_tot", "E_in", "E_kern", "Re_psi_c", "Im_psi_c", "S_max", "R_E"]

# ---- (b) fuettern ----
FU_L, FU_XS, FU_X0 = 320.0, 280.0, -150.0     # Box [-320, 320], Schwamm ab |x| = 280, Paketmitte startet bei -150
FU_T, FU_MESS = 600.0, 0.5
FU_RHO = {0.55: (1.3767, 5.1e-3), 0.70: (1.4938, 6.7e-5)}   # 1D-Pol Re rho, Gamma (RUNDE-06.md, Bruecke dims 1)
FU_NU_RASTER = [round(1.90 + 0.025 * i, 3) for i in range(37)]
FU_SPALTEN = ["Q20", "Q10", "Q40", "E20", "E40", "Phase", "S_max", "x_max", "j_links", "j_rechts", "jE_links",
              "jE_rechts", "Q_box", "E_box", "Breite"]

# ---- (c) kavitation ----
KA_S0 = [0.70, 0.72, 0.75, 0.80]
KA_W = [1.0, 2.0, 4.0, 8.0]
KA_T, KA_MESS, KA_SNAP = 600.0, 1.0, 25.0
KA_DELTA, KA_SAAT = 1e-6, 21                  # Rauschen wie r5b.mi (bandbegrenzt |k| <= 1,5)
KA_SPALTEN = ["rms", "S_max", "S_min", "Q_box", "E_box", "leer", "luecken", "klumpen", "S_mitte", "spinodal"]
SPIN = 2.0 / 3.0


# ---------------------------------------------------------------- Hilfen

def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    if DEV.type == "cuda":
        torch.cuda.synchronize()
    return time.perf_counter()


def rest_sek():
    return ZEIT_BUDGET - (uhr() - T_START[0])


def endlich(*v):
    return all(isinstance(a, (int, float)) and math.isfinite(a) for a in v)


def teilen(a, b):
    return a / b if (endlich(a, b) and b != 0.0) else NAN


def mittel(t, y, a, b):
    return r5b.mittel(t, y, a, b) if (endlich(a, b) and b >= a) else NAN


def maximum(t, y, a, b):
    if not (endlich(a, b) and b >= a):
        return NAN
    idx = r5b.fenster_idx(t, a, b)
    return float(y[idx].max()) if idx.numel() > 0 else NAN


def log_steigung(t, y, a, b):
    """Steigung von ln y ueber t im Fenster [a, b]; nan, wenn y dort nicht ueberall > 0."""
    if not (endlich(a, b) and b > a):
        return NAN
    idx = r5b.fenster_idx(t, a, b)
    if idx.numel() < 5:
        return NAN
    yy, tt = y[idx], t[idx]
    if bool((yy <= 0.0).any()):
        return NAN
    ly = torch.log(yy)
    tm, ym = tt.mean(), ly.mean()
    return float(((tt - tm) * (ly - ym)).sum() / ((tt - tm) ** 2).sum())


def integral(t, y):
    return float(torch.trapezoid(y, t)) if t.shape[0] > 1 else NAN


def spektrum_komplex(t, z, t_a, t_b, n_spitzen=3):
    """Hann-gefensterte FFT der komplexen Reihe z(t) im Fenster [t_a, t_b]. Omega > 0 heisst z ~ exp(-i Omega t)
    (Teilchen, positive Ladung wie ein Q-Ball); ein reelles Oszillon hat beide Vorzeichen gleich stark.
    Leistungsanteile im Band 0,2 <= |Omega| <= 3: unter der Luecke (|Omega| < 1 - 2 dOmega), darueber, Asymmetrie."""
    if not endlich(t_a, t_b):
        return None
    idx = r5b.fenster_idx(t, t_a, t_b)
    n = int(idx.numel())
    if n < 64:
        return None
    dts = float(t[1] - t[0])
    fen = torch.hann_window(n, periodic=False, dtype=F64)
    x = torch.fft.fft(z[idx] * fen)
    p = x.real ** 2 + x.imag ** 2
    om = -2.0 * PI * torch.fft.fftfreq(n, d=dts, dtype=F64)
    ordn = om.argsort()
    om, p = om[ordn], p[ordn]
    amp = p.sqrt()
    d_om = 2.0 * PI / (n * dts)
    band = (om.abs() >= 0.2) & (om.abs() <= 3.0)
    p_band = float(p[band].sum())
    lok = (amp[1:-1] > amp[:-2]) & (amp[1:-1] >= amp[2:])
    kand = torch.nonzero(lok).squeeze(1) + 1
    kand = kand[band[kand]]
    kand = kand[p[kand].argsort(descending=True)][:n_spitzen]
    spitzen = []
    for k in kand.tolist():
        a, bb, c = float(amp[k - 1]), float(amp[k]), float(amp[k + 1])
        nen = a - 2.0 * bb + c
        delta = 0.5 * (a - c) / nen if nen != 0.0 else 0.0
        spitzen.append({"Omega": float(om[k]) + delta * d_om, "anteil": teilen(float(p[k]), p_band)})
    unter = band & (om.abs() < 1.0 - 2.0 * d_om)
    ueber = band & (om.abs() > 1.0 + 2.0 * d_om)
    pos, neg = band & (om > 0.0), band & (om < 0.0)
    return {"fenster": [t_a, t_b], "dOmega": d_om, "spitzen": spitzen,
            "P_unter": teilen(float(p[unter].sum()), p_band), "P_ueber": teilen(float(p[ueber].sum()), p_band),
            "asymmetrie": teilen(float(p[pos].sum()) - float(p[neg].sum()), p_band)}


def sp_text(sp):
    if not sp or not sp["spitzen"]:
        return "-"
    s0 = sp["spitzen"][0]
    return (f"{s0['Omega']:+.4f} ({s0['anteil']:.2f}); unter {fz(sp['P_unter'], '.2f')}, Asym "
            f"{fz(sp['asymmetrie'], '+.2f')}")


def roh_pfad(out, name, stufe):
    return os.path.join(out, f"{name}_{stufe}_roh.pt")


def roh_sichern(out, name, stufe, obj):
    pfad = roh_pfad(out, name, stufe)
    torch.save(obj, pfad)
    print(f"Rohdaten gesichert: {pfad}", flush=True)


def roh_laden(out, name, stufe):
    pfad = roh_pfad(out, name, stufe)
    if not os.path.exists(pfad):
        return None
    return torch.load(pfad, map_location="cpu", weights_only=False)


def zeit_eintrag(befehl, stufe, b, n, schritte, sek):
    return {"befehl": befehl, "stufe": stufe, "B": b, "N": n, "schritte": schritte, "sek": sek,
            "ms_je_schritt": 1000.0 * sek / max(1, schritte), "ns_je_punkt": 1e9 * sek / max(1, schritte * b * n)}


# ---------------------------------------------------------------- (a) tod: Rest unter Q_min

def messer_tod(r, dr):
    """Spalten wie TOD_SPALTEN: Q und E gesamt, im Fenster r < 25 und im Kern r < 10; psi im Zentrum (r = dr),
    max |psi|^2 und Energieradius (rms, r < 25). Energiedichte in chi wie r5a.messer."""
    r_s = r.clone()
    r_s[0] = 1.0
    innen = (r < R_IN).to(F64)
    kern = (r < R_KERN).to(F64)
    r2 = r * r

    def messen(chi, vel):
        a2 = chi.real ** 2 + chi.imag ** 2
        s = a2 / (r_s * r_s)
        w = (chi * vel.conj()).imag
        grad = torch.zeros_like(a2)
        grad[:, :-1] = ((chi[:, 1:] - chi[:, :-1]).abs() / dr) ** 2
        e = vel.real ** 2 + vel.imag ** 2 + grad + a2 * (1.0 - s + 0.5 * s * s)
        ei = e * innen
        psi_c = chi[:, 1] / dr
        sp = [8.0 * PI * w.sum(1) * dr, 8.0 * PI * (w * innen).sum(1) * dr, 8.0 * PI * (w * kern).sum(1) * dr,
              4.0 * PI * e.sum(1) * dr, 4.0 * PI * ei.sum(1) * dr, 4.0 * PI * (e * kern).sum(1) * dr,
              psi_c.real, psi_c.imag, s[:, 1:].max(dim=1).values,
              torch.sqrt((r2 * ei).sum(1) / ei.sum(1).clamp(min=1e-300))]
        return torch.stack(sp, dim=1)
    return messen


def tod_rechnen(opt, out, name, stufen):
    zeilen = sorted({z[1] for z in TOD_LAEUFE})
    fam = r5a.familie([(w2, 3, 0) for w2 in zeilen], r5a.H3, opt, "tod h")
    kenn = [r5a.fam_zeile(fam, i) for i in range(len(zeilen))]
    for z in kenn:
        if not z["gueltig"] and not opt.rauch:
            raise RuntimeError(f"Startprofil ungueltig: {z}")
    q_start = kenn[zeilen.index(TOD_W2_START)]["Q"]
    laeufe = []
    for nm, w2, eta, g, fak in TOD_LAEUFE:
        ts = INF if fak is None else math.log(q_start / (fak * Q_MIN)) / g
        laeufe.append({"name": nm, "w2": w2, "zeile": zeilen.index(w2), "eta": eta, "gamma": g, "stopp_faktor": fak,
                       "t_stop": ts, "Q_profil": kenn[zeilen.index(w2)]["Q"] * (1.0 + eta) ** 2})
    t_end = 40.0 if opt.rauch else (opt.T or TOD_T)
    gam = torch.tensor([[l["gamma"]] for l in laeufe], dtype=F64, device=DEV)
    omb = torch.zeros_like(gam)
    tst = torch.tensor([[l["t_stop"]] for l in laeufe], dtype=F64, device=DEV)
    roh, zeiten = {}, []
    for stufe in stufen:
        if stufe == "fein" and "grob" in roh and rest_sek() < 3.0 * roh["grob"]["sek"]:
            print(f"tod fein: entfaellt (Restzeit {rest_sek():.0f} s)", flush=True)
            continue
        dr, dt = (r5a.DR, r5a.DT) if stufe == "grob" else (r5a.DR * r5a.FEIN, r5a.DT * r5a.FEIN)
        r = r5a.radial_gitter(dr)
        teile = [r5a.ball_radial(fam, l["zeile"], r, eta=l["eta"]) for l in laeufe]
        chi = torch.stack([c for c, _ in teile])
        vel = torch.stack([v for _, v in teile])
        for a in (chi, vel):
            a[:, 0] = 0.0
            a[:, -1] = 0.0
        t0 = uhr()
        t, daten, gek = r5a.entwickeln_radial(chi, vel, dr, dt, t_end, TOD_MESS, messer_tod(r, dr), gam, omb, tst)
        sek = uhr() - t0
        schritte = int(round(float(t[-1]) / dt))
        ze = zeit_eintrag("tod", stufe, chi.shape[0], chi.shape[1], schritte, sek)
        zeiten.append(ze)
        print(f"tod {stufe}: {chi.shape[0]} Laeufe x {chi.shape[1]} Punkte, T = {float(t[-1]):.1f}"
              f"{' (gekuerzt)' if gek else ''}, {schritte} Schritte, {sek:.1f} s ({ze['ms_je_schritt']:.2f} ms je "
              f"Schritt)", flush=True)
        roh[stufe] = {"befehl": "tod", "stufe": stufe, "laeufe": laeufe, "t": t.cpu(), "daten": daten.cpu(),
                      "spalten": TOD_SPALTEN, "dr": dr, "dt": dt, "T_soll": t_end, "gekuerzt": gek, "sek": sek,
                      "profile": kenn, "zeit": ze}
        roh_sichern(out, name, stufe, roh[stufe])
    return roh, zeiten


def auswertung_tod(roh, t_cmp=None):
    t, d = roh["t"], roh["daten"]
    if t_cmp is not None:
        m = t <= t_cmp + 1e-9
        t, d = t[m], d[m]
    T = float(t[-1])
    dtm = float(t[1] - t[0])
    zeilen = []
    for b, l in enumerate(roh["laeufe"]):
        q_tot, q_in, e_tot, e_in, smax = d[:, b, 0], d[:, b, 1], d[:, b, 3], d[:, b, 4], d[:, b, 8]
        psi = torch.complex(d[:, b, 6], d[:, b, 7])
        g, ts = l["gamma"], l["t_stop"]
        q0 = float(q_tot[0])
        q_rel = q_in / (q0 * torch.exp(-g * t.clamp(max=ts)))
        z = {"name": l["name"], "gamma": g, "t_stop": ts, "T": T, "Q_tot_0": q0, "Q_in_0": float(q_in[0]),
             "E_in_0": float(e_in[0]), "S_max_0": float(smax[0])}
        z["t_Qmin"] = math.log(q0 / Q_MIN) / g if (g > 0.0 and q0 > Q_MIN) else NAN
        for key, s in (("t90", 0.9), ("t50", 0.5), ("t10", 0.1)):
            z[key] = r5a.erste_zeit(t, q_rel < s)
        z["dauer_90_10"] = z["t10"] - z["t90"]
        z["Q_in_bei_t90_durch_Qmin"] = (float(q_in[r5a.index_ab(t, z["t90"])]) / Q_MIN if endlich(z["t90"])
                                        else NAN)
        th = r5a.entfalten(-torch.angle(psi))
        w20 = max(1, int(round(20.0 / dtm)))

        def omega_bei(tt):
            i = r5a.index_ab(t, tt)
            i0 = max(0, i - w20)
            return teilen(float(th[i] - th[i0]), float(t[i] - t[i0]))
        z["omega_vor_tod"] = omega_bei(z["t90"] - 10.0) if endlich(z["t90"]) else omega_bei(T)
        # Kern r < 10 (Ladung relativ zum Anfangsanteil) und Laufzeitbild: Welle mit omega > 1 verlaesst das Fenster
        # mit v_g = sqrt(omega^2 - 1)/omega; erwartete Dauer (R_IN - R_E)/v_g
        qk = d[:, b, 2]
        qk_rel = qk / (float(qk[0]) * torch.exp(-g * t.clamp(max=ts)))
        z["t90_kern"], z["t10_kern"] = r5a.erste_zeit(t, qk_rel < 0.9), r5a.erste_zeit(t, qk_rel < 0.1)
        z["dauer_kern"] = z["t10_kern"] - z["t90_kern"]
        om_v = z["omega_vor_tod"]
        z["v_g_vor_tod"] = math.sqrt(om_v * om_v - 1.0) / om_v if (endlich(om_v) and om_v > 1.0) else NAN
        z["R_E_vor_tod"] = float(d[r5a.index_ab(t, z["t90"] - 10.0), b, 9]) if endlich(z["t90"]) else NAN
        z["dauer_vorhersage_vg"] = teilen(R_IN - z["R_E_vor_tod"], z["v_g_vor_tod"])
        z["spek_vor_tod"] = (spektrum_komplex(t, psi, z["t90"] - 210.0, z["t90"] - 10.0) if endlich(z["t90"])
                             else None)
        z["E_ref"] = (float(e_in[r5a.index_ab(t, z["t90"] - 10.0)]) if endlich(z["t90"]) else float(e_in[0]))
        if endlich(z["t10"]):
            td = z["t10"]
        elif endlich(z["t50"]):
            td = z["t50"] + 150.0
        else:
            td = NAN
        z["t_nach_tod"] = td
        if endlich(td):
            a1, b1 = td + 100.0, min(td + 500.0, T)
            a2, b2 = max(td + 100.0, T - 1000.0), T
        else:
            a1, b1 = NAN, NAN
            a2, b2 = max(0.5 * T, T - 1000.0), T
        z["fenster_frueh"], z["fenster_spaet"] = [a1, b1], [a2, b2]
        z["E_frueh"], z["E_spaet"] = mittel(t, e_in, a1, b1), mittel(t, e_in, a2, b2)
        z["E_frueh_rel"], z["E_spaet_rel"] = teilen(z["E_frueh"], z["E_ref"]), teilen(z["E_spaet"], z["E_ref"])
        z["E_rel_nach"] = {str(int(dd)): (teilen(mittel(t, e_in, td + dd - 5.0, td + dd + 5.0), z["E_ref"])
                                          if endlich(td) else NAN) for dd in (100.0, 500.0, 1000.0)}
        z["E_rel_T"] = teilen(mittel(t, e_in, T - 10.0, T), z["E_ref"])
        z["E_kern_spaet"] = mittel(t, d[:, b, 5], a2, b2)
        z["Q_in_spaet"] = mittel(t, q_in, a2, b2)
        z["S_max_spaet"], z["S_max_spaet_max"] = mittel(t, smax, a2, b2), maximum(t, smax, a2, b2)
        z["R_E_spaet"] = mittel(t, d[:, b, 9], a2, b2)
        z["lambda_E_spaet"] = -log_steigung(t, e_in, a2, b2)
        z["spek_frueh"] = spektrum_komplex(t, psi, a1, b1)
        z["spek_spaet"] = spektrum_komplex(t, psi, a2, b2)
        sp = z["spek_spaet"]
        unter = bool(sp and sp["spitzen"] and abs(sp["spitzen"][0]["Omega"]) < 1.0 - 2.0 * sp["dOmega"])
        if not endlich(z["t50"]):
            kl = "lebt"
        elif (z["E_spaet_rel"] >= 0.1 and teilen(z["E_spaet"], z["E_frueh"]) >= 0.5 and unter
              and z["S_max_spaet"] >= 0.01):
            kl = "Oszillon"
        elif z["E_spaet_rel"] < 0.02 or z["S_max_spaet"] < 1e-3:
            kl = "zerlaeuft"
        else:
            kl = "unklar"
        if g > 0.0 and not math.isfinite(ts) and kl != "lebt":
            kl += " (Abfluss laeuft weiter)"
        z["klasse"] = kl
        # eigenes Merkmal: kurzes Oszillon-Plateau im fruehen Fenster (lebt nicht bis T, war aber da)
        spf = z["spek_frueh"]
        z["S_max_frueh"] = mittel(t, smax, a1, b1)
        z["plateau_frueh"] = bool(endlich(z["E_frueh_rel"], z["S_max_frueh"]) and z["E_frueh_rel"] >= 0.1
                                  and z["S_max_frueh"] >= 0.01 and spf and spf["spitzen"]
                                  and abs(spf["spitzen"][0]["Omega"]) < 1.0 - 2.0 * spf["dOmega"])
        # Plausibilitaet: 0 <= E_in <= E_tot; E_tot steigt ohne Abfluss nicht; q_rel <= 1,02
        z["plaus_E_in_gt_E_tot"] = int((e_in - e_tot > 1e-9 * float(e_tot.abs().max())).sum())
        z["plaus_E_in_neg"] = int((e_in < 0.0).sum())
        i_s = 0 if g == 0.0 else (r5a.index_ab(t, ts) if math.isfinite(ts) and ts < T else None)
        z["plaus_E_tot_anstieg_rel"] = (float((e_tot[i_s:] - e_tot[i_s]).max()) / float(e_tot[i_s])
                                        if i_s is not None else NAN)
        z["plaus_q_rel_max"] = float(q_rel.max())
        if g == 0.0:
            z["gegenprobe_dQ_in"] = float(q_in[-1] / q_in[0] - 1.0)
            z["gegenprobe_dE_in"] = float(e_in[-1] / e_in[0] - 1.0)
        zeilen.append(z)
    return zeilen


def om1(sp):
    return abs(sp["spitzen"][0]["Omega"]) if (sp and sp["spitzen"]) else NAN


def l3_tod(zg, zf):
    liste = []
    for a, b in zip(zg, zf):
        e = {"name": a["name"], "klasse_grob": a["klasse"], "klasse_fein": b["klasse"],
             "klasse_gleich": a["klasse"] == b["klasse"]}
        if a["gamma"] > 0.0:
            e["t50"] = l3(a["t50"], b["t50"], a["t_Qmin"])
            e["dauer_90_10"] = l3(a["dauer_90_10"], b["dauer_90_10"], 0.0)
        e["E_spaet_rel"] = l3(a["E_spaet_rel"], b["E_spaet_rel"], 1.0)
        e["Omega_spaet"] = l3(om1(a["spek_spaet"]), om1(b["spek_spaet"]), 1.0)
        liste.append(e)
    return liste


def bericht_tod(ausw, l3_liste, t_cmp):
    zz = [f"(a) Tod unter Q_min, Folge: 3D radial, Start omega^2 = {TOD_W2_START}, gleichmaessiger Abfluss "
          f"-gamma psi_t bis t_stop; Q_min (Runde 2) = {Q_MIN}; Fenster r < {R_IN} (Kern r < {R_KERN}); "
          f"Messung alle {TOD_MESS}.",
          "  E_ref = E_in bei t90 - 10 (lebende Laeufe: t = 0); Fenster frueh [t10+100, t10+500], spaet "
          "[max(t10+100, T-1000), T].",
          "  Spektrum: psi im Zentrum, Omega > 0 = exp(-i Omega t) (Teilchen); 'unter' = Leistungsanteil |Omega| < 1 - "
          "2 dOmega; Asym = (P+ - P-)/P (Q-Ball +1, reelles Oszillon 0).",
          "  Klasse (vorab): Oszillon, wenn E_spaet >= 0,1 E_ref und >= 0,5 E_frueh und Hauptlinie unter 1 und "
          "S_max spaet >= 0,01; zerlaeuft, wenn E_spaet < 0,02 E_ref oder S_max spaet < 1e-3; sonst unklar."]
    for stufe, zeilen in ausw.items():
        zz.append(f"  [{stufe}]")
        zz.append("  Lauf | t_stop | t90 / t50 / t10 | Dauer | Q_in(t90)/Q_min | omega vor Tod (Phase) | Spektrum vor "
                  "Tod | E_ref | E_in/E_ref: +100 / +500 / +1000 / T | Spektrum spaet | S_max spaet (max) | "
                  "lambda_E spaet | Klasse")
        for z in zeilen:
            en = z["E_rel_nach"]
            zz.append(f"  {z['name']:22s} | {fz(z['t_stop'], '.1f')} | {fz(z['t90'], '.1f')} / {fz(z['t50'], '.1f')}"
                      f" / {fz(z['t10'], '.1f')} | {fz(z['dauer_90_10'], '.1f')} | "
                      f"{fz(z['Q_in_bei_t90_durch_Qmin'], '.4f')} | {fz(z['omega_vor_tod'], '.4f')} | "
                      f"{sp_text(z['spek_vor_tod'])} | {fz(z['E_ref'], '.3f')} | {fz(en['100'], '.3f')} / "
                      f"{fz(en['500'], '.3f')} / {fz(en['1000'], '.3f')} / {fz(z['E_rel_T'], '.3f')} | "
                      f"{sp_text(z['spek_spaet'])} | {fz(z['S_max_spaet'], '.2e')} ({fz(z['S_max_spaet_max'], '.2e')})"
                      f" | {fz(z['lambda_E_spaet'], '.2e')} | {z['klasse']}")
        zz.append("  Laufzeitbild: Lauf | Kern r < 10: t90 / t10 / Dauer | Fenster r < 25: Dauer | v_g(omega vor Tod) | "
                  "R_E vor Tod | Dauer-Vorhersage (25 - R_E)/v_g | frueh: E/E_ref, S_max, Spektrum, Plateau")
        for z in zeilen:
            zz.append(f"  {z['name']:22s} | {fz(z['t90_kern'], '.1f')} / {fz(z['t10_kern'], '.1f')} / "
                      f"{fz(z['dauer_kern'], '.1f')} | {fz(z['dauer_90_10'], '.1f')} | {fz(z['v_g_vor_tod'], '.4f')} | "
                      f"{fz(z['R_E_vor_tod'], '.2f')} | {fz(z['dauer_vorhersage_vg'], '.1f')} | "
                      f"{fz(z['E_frueh_rel'], '.3f')}, {fz(z['S_max_frueh'], '.2e')}, {sp_text(z['spek_frueh'])}, "
                      f"{'ja' if z['plateau_frueh'] else 'nein'}")
        zz.append("  Plausibilitaet: Lauf | E_in > E_tot (Anzahl) | E_in < 0 | E_tot-Anstieg nach Stopp (rel) | "
                  "q_rel max | Gegenprobe dQ_in, dE_in")
        for z in zeilen:
            gp = (f"{fz(z.get('gegenprobe_dQ_in', NAN), '+.1e')}, {fz(z.get('gegenprobe_dE_in', NAN), '+.1e')}"
                  if "gegenprobe_dQ_in" in z else "-")
            zz.append(f"  {z['name']:22s} | {z['plaus_E_in_gt_E_tot']} | {z['plaus_E_in_neg']} | "
                      f"{fz(z['plaus_E_tot_anstieg_rel'], '.1e')} | {fz(z['plaus_q_rel_max'], '.4f')} | {gp}")
    if l3_liste:
        n_ok = sum(1 for e in l3_liste for k, v in e.items() if isinstance(v, dict) and v["bestanden"])
        n_ges = sum(1 for e in l3_liste for v in e.values() if isinstance(v, dict))
        n_kl = sum(1 for e in l3_liste if e["klasse_gleich"])
        zz.append(f"  L3 (grob gegen fein bis T = {fz(t_cmp, '.0f')}): {n_ok} von {n_ges} Kenngroessen bestanden; "
                  f"Klasse gleich in {n_kl} von {len(l3_liste)} Laeufen")
        for e in l3_liste:
            teile = [f"{k} {'ok' if v['bestanden'] else 'NEIN'} ({fz(v['effekt'], '.3g')}/{fz(v['aenderung'], '.2g')})"
                     for k, v in e.items() if isinstance(v, dict)]
            zz.append(f"    {e['name']:22s}: Klasse {e['klasse_grob']} / {e['klasse_fein']}; " + "; ".join(teile))
    else:
        zz.append("  L3: nur eine Stufe vorhanden")
    return zz


def lauf_tod(opt, out):
    name = "tod"
    stufen = {"grob": ["grob"], "fein": ["fein"], "beide": ["grob", "fein"]}[opt.stufe]
    zeiten = []
    if opt.nur_auswertung:
        roh = {}
    else:
        roh, zeiten = tod_rechnen(opt, out, name, stufen)
    for s in ("grob", "fein"):
        if s not in roh:
            geladen = roh_laden(out, name, s)
            if geladen is not None:
                roh[s] = geladen
    if not roh:
        raise RuntimeError("keine Rohdaten vorhanden")
    ausw = {s: auswertung_tod(roh[s]) for s in ("grob", "fein") if s in roh}
    l3_liste, t_cmp = [], NAN
    if "grob" in roh and "fein" in roh:
        t_cmp = min(float(roh["grob"]["t"][-1]), float(roh["fein"]["t"][-1]))
        l3_liste = l3_tod(auswertung_tod(roh["grob"], t_cmp), auswertung_tod(roh["fein"], t_cmp))
    res = {"laeufe": next(iter(roh.values()))["laeufe"], "auswertung": ausw, "L3": l3_liste, "T_vergleich": t_cmp,
           "zeiten": zeiten, "profile": next(iter(roh.values()))["profile"]}
    return name, res, bericht_tod(ausw, l3_liste, t_cmp), zeiten


# ---------------------------------------------------------------- (b) fuettern: Aufnahme unter der Schwelle

def paket_sigma(x, nu, eps, vz, sigma, x0):
    """Wie r5b.paket (aus tests1d), nur mit sigma und x0 als Argument statt F_SIGMA = 8 und F_X0 = -55."""
    k = math.sqrt(nu * nu - 1.0)
    vg = k / nu
    psi = eps * torch.exp(-((x - x0) ** 2) / (2.0 * sigma ** 2)) * torch.exp(1j * k * (x - x0))
    vel = (-1j * nu + vg * (x - x0) / sigma ** 2) * psi
    if vz < 0:
        return torch.conj_physical(psi), torch.conj_physical(vel)
    return psi, vel


def fu_laeufe(teil):
    bp = []                                                  # (omega^2, nu, eps, sigma)
    if teil == "mechanik":
        for nu in (2.2, 2.8):
            for eps in (0.0025, 0.005, 0.01, 0.02, 0.05):
                bp.append((0.55, nu, eps, 8.0))
        for nu in (2.125, 2.2, 2.4):
            for sig in (4.0, 8.0, 16.0, 32.0):
                bp.append((0.55, nu, 0.01, sig))
    elif teil in ("raster55", "raster70"):
        w2 = 0.55 if teil == "raster55" else 0.70
        for sig in (8.0, 32.0):
            for nu in FU_NU_RASTER:
                bp.append((w2, nu, 0.01, sig))
    elif teil == "rauch":
        bp = [(0.55, 2.125, 0.01, 8.0), (0.55, 2.8, 0.01, 8.0)]
    else:
        raise SystemExit(f"fuettern: unbekannter Teil {teil} (mechanik, raster55, raster70)")
    bp = list(dict.fromkeys(bp))
    laeufe = [{"art": "ball+paket", "w2": w2, "nu": nu, "eps": eps, "sigma": sig} for w2, nu, eps, sig in bp]
    laeufe += [{"art": "paket", "w2": None, "nu": nu, "eps": eps, "sigma": sig}
               for nu, eps, sig in dict.fromkeys((nu, eps, sig) for _, nu, eps, sig in bp)]
    laeufe += [{"art": "ball", "w2": w2, "nu": None, "eps": 0.0, "sigma": None}
               for w2 in dict.fromkeys(b[0] for b in bp)]
    return laeufe


def messer_fu(x, dx):
    m20 = (x.abs() < 20.0).to(F64)
    m10 = (x.abs() < 10.0).to(F64)
    m40 = (x.abs() < 40.0).to(F64)
    i_l = int(round((-40.0 + r5b.L_BOX) / dx))
    i_r = int(round((40.0 + r5b.L_BOX) / dx))

    def fluss(psi, vel, ij):
        px = (psi[:, ij + 1] - psi[:, ij - 1]) / (2.0 * dx)
        return -2.0 * (psi[:, ij] * px.conj()).imag, -2.0 * (vel[:, ij].conj() * px).real

    def messen(psi, vel, t):
        s = r5b.dichte(psi)
        rho = r5b.ladung(psi, vel)
        e = r5b.energie_dichte(psi, vel, dx)
        i, p = r5b.max_im_fenster(psi, s, m20)
        jl, jel = fluss(psi, vel, i_l)
        jr, jer = fluss(psi, vel, i_r)
        return torch.stack([(rho * m20).sum(1) * dx, (rho * m10).sum(1) * dx, (rho * m40).sum(1) * dx,
                            (e * m20).sum(1) * dx, (e * m40).sum(1) * dx, -torch.angle(p[:, 0]), s.gather(1, i)[:, 0],
                            x[i[:, 0]], jl, jr, jel, jer, rho.sum(1) * dx, e.sum(1) * dx, r5b.breite_s(x, s, m20)],
                           dim=1)
    return messen


def fu_rechnen(opt, out, name, laeufe, stufen, t_end):
    roh, zeiten = {}, []
    alt = (r5b.L_BOX, r5b.X_SPONGE)
    r5b.L_BOX, r5b.X_SPONGE = FU_L, FU_XS
    try:
        for stufe in stufen:
            if stufe == "fein" and "grob" in roh and rest_sek() < 4.5 * roh["grob"]["sek"]:
                print(f"{name} fein: entfaellt (Restzeit {rest_sek():.0f} s)", flush=True)
                continue
            dx, dt = (r5b.DX, r5b.DT) if stufe == "grob" else (r5b.DX * r5b.FEIN, r5b.DT * r5b.FEIN)
            x = r5b.gitter(dx)
            felder = []
            for l in laeufe:
                teile = []
                if l["art"] in ("ball+paket", "ball"):
                    teile.append(r5b.ball(x, l["w2"]))
                if l["art"] in ("ball+paket", "paket"):
                    teile.append(paket_sigma(x, l["nu"], l["eps"], 1, l["sigma"], FU_X0))
                felder.append(r5b.summe(teile))
            psi, vel = r5b.stapel(felder)
            t0 = uhr()
            t, daten = r5b.entwickeln(psi, vel, dx, dt, t_end, FU_MESS, messer_fu(x, dx))
            sek = uhr() - t0
            schritte = int(round(t_end / dt))
            ze = zeit_eintrag("fuettern", stufe, psi.shape[0], psi.shape[1], schritte, sek)
            zeiten.append(ze)
            print(f"{name} {stufe}: {psi.shape[0]} Laeufe x {psi.shape[1]} Punkte, T = {t_end}, {sek:.1f} s "
                  f"({ze['ms_je_schritt']:.2f} ms je Schritt)", flush=True)
            roh[stufe] = {"befehl": "fuettern", "stufe": stufe, "laeufe": laeufe, "t": t.cpu(), "daten": daten.cpu(),
                          "spalten": FU_SPALTEN, "dx": dx, "dt": dt, "T_soll": t_end, "sek": sek, "zeit": ze,
                          "box": [FU_L, FU_XS, FU_X0]}
            roh_sichern(out, name, stufe, roh[stufe])
    finally:
        r5b.L_BOX, r5b.X_SPONGE = alt
    return roh, zeiten


def auswertung_fu(roh):
    t, d = roh["t"], roh["daten"]
    T = float(t[-1])
    sp = {n: d[:, :, k] for k, n in enumerate(FU_SPALTEN)}
    laeufe = roh["laeufe"]
    i_ball = {l["w2"]: b for b, l in enumerate(laeufe) if l["art"] == "ball"}
    i_pak = {(l["nu"], l["eps"], l["sigma"]): b for b, l in enumerate(laeufe) if l["art"] == "paket"}
    zeilen = []
    for b, l in enumerate(laeufe):
        if l["art"] != "ball+paket":
            continue
        ib, ip = i_ball[l["w2"]], i_pak[(l["nu"], l["eps"], l["sigma"])]

        def diff(n, ohne_paket=True):
            y = sp[n][:, b] - sp[n][:, ib]
            return y - sp[n][:, ip] if ohne_paket else y
        dq20, dq10, dq40, de20 = diff("Q20"), diff("Q10"), diff("Q40"), diff("E20")
        w2, nu, eps, sig = l["w2"], l["nu"], l["eps"], l["sigma"]
        om = math.sqrt(w2)
        k = math.sqrt(nu * nu - 1.0)
        vg = k / nu
        qp = abs(float(sp["Q_box"][0, ip]))
        ep = float(sp["E_box"][0, ip])
        t_c = abs(FU_X0) / vg
        t_n = t_c + (4.0 * sig + 20.0) / vg + 10.0
        a, bb = t_n, t_n + 20.0
        z = {"name": f"w2={w2} nu={nu} eps={eps} sigma={sig}", "w2": w2, "nu": nu, "eps": eps, "sigma": sig,
             "omega": om, "nu_schwelle": 2.0 * om + 1.0, "ueber": bool(nu > 2.0 * om + 1.0),
             "nu_r": om + FU_RHO[w2][0] if w2 in FU_RHO else NAN, "Gamma_1D": FU_RHO.get(w2, (NAN, NAN))[1],
             "Q_paket": qp, "E_paket": ep, "t_mitte": t_c, "t_nach": t_n}
        z["dQ_nach"] = mittel(t, dq20, a, bb)
        z["C_nach"] = teilen(z["dQ_nach"], qp)
        z["C_R5"] = teilen(mittel(t, dq20, t_c + 163.0, t_c + 188.0), qp)
        z["C_Ende"] = teilen(mittel(t, dq20, T - 25.0, T), qp)
        z["dE_dQ_nach"] = teilen(mittel(t, de20, a, bb), z["dQ_nach"])
        z["Ort_10_20"] = teilen(mittel(t, dq10, a, bb), z["dQ_nach"])
        z["Ort_40_20"] = teilen(mittel(t, dq40, a, bb), z["dQ_nach"])
        z["kappa"] = -log_steigung(t, dq20, t_n, min(t_n + 200.0, T - 5.0))
        # auf die Ankunft der Paketmitte zurueckgerechnet (breite Pakete werden spaeter gemessen)
        z["C_ankunft"] = (z["C_nach"] * math.exp(z["kappa"] * (t_n + 10.0 - t_c))
                          if (endlich(z["C_nach"], z["kappa"]) and z["kappa"] > 0.0) else NAN)
        jl = sp["j_links"][:, b] - sp["j_links"][:, ib]
        jr = sp["j_rechts"][:, b] - sp["j_rechts"][:, ib]
        jel = sp["jE_links"][:, b] - sp["jE_links"][:, ib]
        jer = sp["jE_rechts"][:, b] - sp["jE_rechts"][:, ib]
        q40 = sp["Q40"][:, b] - sp["Q40"][:, ib]
        e40 = sp["E40"][:, b] - sp["E40"][:, ib]
        ein, aus = integral(t, jl), integral(t, jr)
        z["R"] = 1.0 - teilen(ein, qp)
        z["T_durch"] = teilen(aus, qp)
        z["C40_Ende"] = teilen(float(q40[-1]), qp)
        z["Bilanz_Q"] = teilen((ein - aus) - (float(q40[-1]) - float(q40[0])), qp)
        z["Bilanz_E"] = teilen((integral(t, jel) - integral(t, jer)) - (float(e40[-1]) - float(e40[0])), ep)
        z["Paket_im_Fenster"] = teilen(mittel(t, sp["Q20"][:, ip], a, bb), qp)
        z["Atmung"] = (r5b.spektrum(t, sp["S_max"][:, b] - sp["S_max"][:, ib], t_n) if t_n < T - 50.0 else [])
        z["x_Ende"] = r5b.ende(sp["x_max"][:, b])
        z["d_omega"] = (r5b.om_fenster(t, sp["Phase"][:, b], 0.75 * T, T)
                        - r5b.om_fenster(t, sp["Phase"][:, ib], 0.75 * T, T))
        z["born_C_Q"] = r5b.born_aq(w2, nu, 1)
        # Plausibilitaet: -1 <= C <= 1, Bilanzen, Anteile
        z["plaus_ok"] = bool(all(not endlich(v) or -1.0 <= v <= 1.0 for v in (z["C_nach"], z["C_Ende"]))
                             and (not endlich(z["Bilanz_Q"]) or abs(z["Bilanz_Q"]) < 1e-3)
                             and (not endlich(z["Paket_im_Fenster"]) or abs(z["Paket_im_Fenster"]) < 1e-3)
                             and (not endlich(z["R"]) or -0.2 <= z["R"] <= 1.0)
                             and (not endlich(z["T_durch"]) or -0.2 <= z["T_durch"] <= 1.0 + 1e-3))
        zeilen.append(z)
    return {"zeilen": zeilen, "aggregat": fu_aggregat(zeilen)}


def steigung_xy(pts):
    if len(pts) < 2:
        return NAN
    mx = sum(p[0] for p in pts) / len(pts)
    my = sum(p[1] for p in pts) / len(pts)
    sxx = sum((p[0] - mx) ** 2 for p in pts)
    return sum((p[0] - mx) * (p[1] - my) for p in pts) / sxx if sxx > 0.0 else NAN


def fu_aggregat(zeilen):
    agg = {"amplitude": [], "breite": [], "raster": []}
    gr = {}
    for z in zeilen:
        gr.setdefault((z["w2"], z["nu"], z["sigma"]), []).append(z)
    for (w2, nu, sig), g in gr.items():
        if len({z["eps"] for z in g}) >= 3:
            pts = [(math.log(z["eps"]), math.log(z["dQ_nach"])) for z in g if endlich(z["dQ_nach"]) and z["dQ_nach"] > 0]
            agg["amplitude"].append({"w2": w2, "nu": nu, "sigma": sig, "p": steigung_xy(pts) if len(pts) >= 3 else NAN,
                                     "C_nach": {str(z["eps"]): z["C_nach"] for z in g}})
    gr = {}
    for z in zeilen:
        gr.setdefault((z["w2"], z["nu"], z["eps"]), []).append(z)
    for (w2, nu, eps), g in gr.items():
        sigs = sorted({z["sigma"] for z in g})
        if 3 <= len(sigs) <= 6:
            agg["breite"].append({"w2": w2, "nu": nu, "eps": eps,
                                  "C_nach": {str(z["sigma"]): z["C_nach"] for z in sorted(g, key=lambda q: q["sigma"])},
                                  "C_ankunft": {str(z["sigma"]): z["C_ankunft"]
                                                for z in sorted(g, key=lambda q: q["sigma"])},
                                  "kappa": {str(z["sigma"]): z["kappa"] for z in sorted(g, key=lambda q: q["sigma"])}})
    gr = {}
    for z in zeilen:
        gr.setdefault((z["w2"], z["sigma"], z["eps"]), []).append(z)
    for (w2, sig, eps), g in gr.items():
        if len(g) < 10:
            continue
        g = sorted(g, key=lambda q: q["nu"])
        schw = g[0]["nu_schwelle"]
        unter = [z for z in g if z["nu"] < schw - 0.05 and endlich(z["C_nach"])]
        e = {"w2": w2, "sigma": sig, "eps": eps, "nu_schwelle": schw, "nu_r_vorhersage": g[0]["nu_r"],
             "nu_peak": NAN, "C_peak": NAN, "fwhm": NAN, "C_min_zwischen": NAN, "C_erster_ueber": NAN}
        if unter:
            i = max(range(len(unter)), key=lambda q: unter[q]["C_nach"])
            e["C_peak"] = unter[i]["C_nach"]
            e["nu_peak"] = unter[i]["nu"]
            if 0 < i < len(unter) - 1:
                x1, x2, x3 = unter[i - 1]["nu"], unter[i]["nu"], unter[i + 1]["nu"]
                y1, y2, y3 = unter[i - 1]["C_nach"], unter[i]["C_nach"], unter[i + 1]["C_nach"]
                nen = (y1 - 2.0 * y2 + y3)
                if nen < 0.0:
                    e["nu_peak"] = x2 + 0.5 * (x2 - x1) * (y1 - y3) / nen
            halb = 0.5 * e["C_peak"]
            lo = hi = NAN
            for j in range(i, 0, -1):
                if unter[j - 1]["C_nach"] < halb <= unter[j]["C_nach"]:
                    lo = unter[j - 1]["nu"] + (halb - unter[j - 1]["C_nach"]) * (unter[j]["nu"] - unter[j - 1]["nu"]) / (
                        unter[j]["C_nach"] - unter[j - 1]["C_nach"])
                    break
            for j in range(i, len(unter) - 1):
                if unter[j + 1]["C_nach"] < halb <= unter[j]["C_nach"]:
                    hi = unter[j]["nu"] + (unter[j]["C_nach"] - halb) * (unter[j + 1]["nu"] - unter[j]["nu"]) / (
                        unter[j]["C_nach"] - unter[j + 1]["C_nach"])
                    break
            e["fwhm"] = hi - lo
            zw = [z["C_nach"] for z in unter if z["nu"] > e["nu_peak"] + 0.1]
            e["C_min_zwischen"] = min(zw) if zw else NAN
        ueber = [z for z in g if z["ueber"] and endlich(z["C_nach"])]
        if ueber:
            e["C_erster_ueber"] = ueber[0]["C_nach"]
        e["abweichung_peak_vorhersage"] = e["nu_peak"] - e["nu_r_vorhersage"]
        e["kurve"] = [[z["nu"], z["C_nach"], z["kappa"], z["dE_dQ_nach"]] for z in g]
        agg["raster"].append(e)
    return agg


def bericht_fu(name, ausw, l3_liste):
    zz = [f"(b) fuettern, Teil {name}: Box +-{FU_L} (Schwamm ab {FU_XS}), Paketmitte startet bei x0 = {FU_X0}, "
          f"Messung alle {FU_MESS}, Fenster |x| < 20 (Ort: 10 und 40).",
          "  C_nach = [Q20(Ball+Paket) - Q20(Ball) - Q20(Paket)] / |Q_Paket| im Fenster [t_nach, t_nach + 20], "
          "t_nach = Ankunft der Paketmitte + (4 sigma + 20)/v_g + 10;",
          "  C_R5 = dasselbe im Fenster der Runde 5 (163 bis 188 nach Ankunft); kappa = Abklingrate von dQ20 in "
          "[t_nach, t_nach + 200]; R, T aus den Fluessen bei x = -40 / +40;",
          "  Bilanz_Q = [Int (j(-40) - j(+40)) dt - dQ40] / Q_Paket (muss ~0 sein); nu_r = omega + Re rho (1D-Pol aus "
          "RUNDE-06): 0,55 -> 2,1183, 0,70 -> 2,3305."]
    for stufe, a in ausw.items():
        zz.append(f"  [{stufe}]")
        zz.append("  Lauf | ueber | C_nach | C_R5 | C_Ende | kappa (2 Gamma_1D) | dE/dQ (omega) | Ort 10/20, 40/20 | R | "
                  "T | Bilanz Q, E | Atmung Omega (Amp) | x Ende | born | plaus")
        for z in a["zeilen"]:
            atm = ", ".join(f"{s['Omega']:.4f} ({s['amplitude']:.1e})" for s in z["Atmung"][:2]) if z["Atmung"] else "-"
            zz.append(f"  {z['name']:34s} | {str(z['ueber']):5s} | {fz(z['C_nach'], '+.3e')} | {fz(z['C_R5'], '+.3e')}"
                      f" | {fz(z['C_Ende'], '+.2e')} | {fz(z['kappa'], '.2e')} ({fz(2.0 * z['Gamma_1D'], '.1e')}) | "
                      f"{fz(z['dE_dQ_nach'], '.3f')} ({z['omega']:.4f}) | {fz(z['Ort_10_20'], '.3f')}, "
                      f"{fz(z['Ort_40_20'], '.3f')} | {fz(z['R'], '.4f')} | {fz(z['T_durch'], '.4f')} | "
                      f"{fz(z['Bilanz_Q'], '+.1e')}, {fz(z['Bilanz_E'], '+.1e')} | {atm} | {fz(z['x_Ende'], '+.3f')} | "
                      f"{fz(z['born_C_Q'], '.2e')} | {'ok' if z['plaus_ok'] else 'NEIN'}")
        ag = a["aggregat"]
        for e in ag["amplitude"]:
            zz.append(f"  Amplitude w2 = {e['w2']}, nu = {e['nu']}, sigma = {e['sigma']}: dQ ~ eps^p, p = "
                      f"{fz(e['p'], '.3f')} (2 = linear, 4 = Zwei-Quanten); C_nach je eps: "
                      + ", ".join(f"{k}: {fz(v, '.3e')}" for k, v in e["C_nach"].items()))
        for e in ag["breite"]:
            zz.append(f"  Breite w2 = {e['w2']}, nu = {e['nu']}, eps = {e['eps']}: C_nach je sigma: "
                      + ", ".join(f"{k}: {fz(v, '.3e')}" for k, v in e["C_nach"].items()) + "; auf Ankunft: "
                      + ", ".join(f"{k}: {fz(v, '.3e')}" for k, v in e["C_ankunft"].items()) + "; kappa: "
                      + ", ".join(f"{k}: {fz(v, '.2e')}" for k, v in e["kappa"].items()))
        for e in ag["raster"]:
            zz.append(f"  Raster w2 = {e['w2']}, sigma = {e['sigma']}: Spitze unter der Schwelle bei nu = "
                      f"{fz(e['nu_peak'], '.4f')} (Vorhersage {fz(e['nu_r_vorhersage'], '.4f')}, Abweichung "
                      f"{fz(e['abweichung_peak_vorhersage'], '+.4f')}), C = {fz(e['C_peak'], '.3e')}, FWHM "
                      f"{fz(e['fwhm'], '.3f')}; kleinstes C zwischen Spitze + 0,1 und Schwelle {fz(e['C_min_zwischen'], '.2e')};"
                      f" erster Wert ueber der Schwelle ({fz(e['nu_schwelle'], '.3f')}) {fz(e['C_erster_ueber'], '.3e')}")
            zz.append("    nu: C_nach | kappa | dE/dQ -> " + "; ".join(
                f"{k[0]:.3f}: {fz(k[1], '.2e')} | {fz(k[2], '.1e')} | {fz(k[3], '.2f')}" for k in e["kurve"]))
    if l3_liste:
        n = sum(1 for e in l3_liste if e["C_nach"]["bestanden"])
        nk = sum(1 for e in l3_liste if e["kappa"]["bestanden"])
        nkd = sum(1 for e in l3_liste if endlich(e["kappa"]["effekt"]))
        zz.append(f"  L3 (grob gegen fein): C_nach {n} von {len(l3_liste)}; kappa {nk} von {nkd} definierten")
        for e in l3_liste:
            if e.get("nu_peak"):
                zz.append(f"    Raster {e['name']}: nu_peak {'ok' if e['nu_peak']['bestanden'] else 'NEIN'} "
                          f"({fz(e['nu_peak']['effekt'], '.3g')}/{fz(e['nu_peak']['aenderung'], '.2g')})")
    else:
        zz.append("  L3: nur eine Stufe vorhanden")
    return zz


def l3_fu(ag, af):
    liste = [{"name": a["name"], "C_nach": l3(a["C_nach"], b["C_nach"], 0.0), "kappa": l3(a["kappa"], b["kappa"], 0.0)}
             for a, b in zip(ag["zeilen"], af["zeilen"])]
    for a, b in zip(ag["aggregat"]["raster"], af["aggregat"]["raster"]):
        liste.append({"name": f"w2={a['w2']} sigma={a['sigma']}", "C_nach": l3(a["C_peak"], b["C_peak"], 0.0),
                      "kappa": l3(NAN, NAN, 0.0), "nu_peak": l3(a["nu_peak"], b["nu_peak"], a["nu_schwelle"])})
    return liste


def lauf_fuettern(opt, out):
    teil = "rauch" if opt.rauch else (opt.teil or "mechanik")
    name = f"fuettern_{teil}"
    stufen = {"grob": ["grob"], "fein": ["fein"], "beide": ["grob", "fein"]}[opt.stufe]
    t_end = 30.0 if opt.rauch else (opt.T or FU_T)
    zeiten = []
    roh = {}
    if not opt.nur_auswertung:
        roh, zeiten = fu_rechnen(opt, out, name, fu_laeufe(teil), stufen, t_end)
    for s in ("grob", "fein"):
        if s not in roh:
            geladen = roh_laden(out, name, s)
            if geladen is not None:
                roh[s] = geladen
    if not roh:
        raise RuntimeError("keine Rohdaten vorhanden")
    ausw = {s: auswertung_fu(roh[s]) for s in ("grob", "fein") if s in roh}
    l3_liste = l3_fu(ausw["grob"], ausw["fein"]) if len(ausw) == 2 else []
    res = {"teil": teil, "auswertung": ausw, "L3": l3_liste, "zeiten": zeiten}
    return name, res, bericht_fu(teil, ausw, l3_liste), zeiten


# ---------------------------------------------------------------- (c) kavitation: dichtes Kondensat mit Delle

def bounce(s0):
    """Kritischer Keim (1D, statisch bei festem omega^2 = U'(S0)): f'^2 = P0 - g(f^2), g(S) = omega^2 S - U(S).
    g(S) - g(S0) = -(S - S0)^2 (S - S_t)/2 mit S_t = 2 - 2 S0 (Minimum des Keims). Barriere
    F_b = sqrt(2) Int_{S_t}^{S0} (S0 - S) sqrt((S - S_t)/S) dS; Defizitflaeche A_b = 2 sqrt(2) ln((sqrt S0 +
    sqrt(S0 - S_t))/sqrt S_t); x_halb = Halbbreite bei halber Tiefe."""
    st = 2.0 - 2.0 * s0
    if not (0.0 < st < s0):
        return {"S_t": st, "F_b": NAN, "A_b": NAN, "x_halb": NAN, "kappa": NAN}
    a2 = s0 - st
    v = torch.linspace(0.0, math.sqrt(a2), 20001, dtype=F64)
    s = st + v * v
    f_b = math.sqrt(2.0) * float(torch.trapezoid((s0 - s) * (v / torch.sqrt(s)) * 2.0 * v, v))
    vh = torch.linspace(0.0, math.sqrt(0.5 * a2), 20001, dtype=F64)
    sh = st + vh * vh
    xh = float(torch.trapezoid(2.0 / ((s0 - sh) * torch.sqrt(2.0 * sh)), vh))
    a_b = 2.0 * math.sqrt(2.0) * math.log((math.sqrt(s0) + math.sqrt(a2)) / math.sqrt(st))
    return {"S_t": st, "F_b": f_b, "A_b": a_b, "x_halb": xh, "kappa": math.sqrt(2.0 * s0 * (3.0 * s0 - 2.0))}


def ka_tiefen(s0):
    return [("flach", s0 - 0.5 * (s0 - SPIN)), ("knapp", SPIN - 0.03), ("mittel", 0.5), ("tief", 0.3),
            ("sehr tief", 0.1), ("voll", 0.0)]


def ka_lauf(s0, name, smin, w):
    d = 0.0 if w == 0.0 else 1.0 - math.sqrt(max(smin, 0.0) / s0)
    return {"s0": s0, "name": name, "smin_soll": smin, "w": w, "d": d}


def ka_laeufe(teil, s0_liste):
    laeufe = []
    if teil == "raster":
        for s0 in s0_liste:
            laeufe.append(ka_lauf(s0, "Kontrolle", s0, 0.0))
            for nm, smin in ka_tiefen(s0):
                for w in KA_W:
                    laeufe.append(ka_lauf(s0, nm, smin, w))
    elif teil in ("box", "rauch"):
        for s0 in (0.72, 0.80):
            flach = s0 - 0.5 * (s0 - SPIN)
            laeufe.append(ka_lauf(s0, "Kontrolle", s0, 0.0))
            wahl = ((("voll", 0.0, 2.0), ("tief", 0.3, 4.0), ("knapp", SPIN - 0.03, 8.0), ("flach", flach, 8.0))
                    if teil == "box" else (("voll", 0.0, 2.0), ("knapp", SPIN - 0.03, 8.0)))
            for nm, smin, w in wahl:
                laeufe.append(ka_lauf(s0, nm, smin, w))
    else:
        raise SystemExit(f"kavitation: unbekannter Teil {teil} (raster, box)")
    return laeufe


def ka_stufen(teil, opt):
    if teil == "raster":
        st = [("L200_grob", 200.0, 0.1, 0.05), ("L200_fein", 200.0, 0.05, 0.025)]
    elif teil == "box":
        st = [("L200_grob", 200.0, 0.1, 0.05), ("L200_fein", 200.0, 0.05, 0.025), ("L400_grob", 400.0, 0.1, 0.05),
              ("L400_fein", 400.0, 0.05, 0.025)]
        if opt.sehrfein:
            st.append(("L200_sehrfein", 200.0, 0.025, 0.0125))
    else:
        st = [("L200_grob", 200.0, 0.1, 0.05), ("L200_fein", 200.0, 0.05, 0.025), ("L400_grob", 400.0, 0.1, 0.05)]
    if opt.stufe != "beide":
        st = [s for s in st if s[0].endswith("_" + opt.stufe)]
    return st


def messer_ka(x, dx, s0t, schnapp, schritt):
    s0v = s0t.unsqueeze(1)
    i0 = int(torch.nonzero(x.abs() < 0.5 * dx)[0, 0])
    null = torch.zeros_like(s0t)

    def messen(psi, vel, t):
        s = r5b.dichte(psi)
        rho = r5b.ladung(psi, vel)
        e = r5b.energie_dichte(psi, vel, dx, periodisch=True)
        leer_m = s < 0.5 * s0v
        smax = s.max(1).values
        lok = ((s > torch.roll(s, 1, dims=1)) & (s >= torch.roll(s, -1, dims=1))
               & (s > s0v + 0.5 * (smax.unsqueeze(1) - s0v)))
        klumpen = torch.where(smax - s0t >= 0.2 * s0t, lok.to(F64).sum(1), null)
        if abs(t / KA_SNAP - round(t / KA_SNAP)) < 1e-6:
            schnapp.append(s[:, ::schritt].to(torch.float32).cpu())
        return torch.stack([(s - s0v).pow(2).mean(1).sqrt(), smax, s.min(1).values, rho.sum(1) * dx, e.sum(1) * dx,
                            leer_m.to(F64).sum(1) * dx, (leer_m & ~torch.roll(leer_m, 1, dims=1)).to(F64).sum(1),
                            klumpen, s[:, i0], (s < SPIN).to(F64).sum(1) * dx], dim=1)
    return messen


def df_pfad(s0, w, d, x, dx, n=201):
    """Groesstes dF entlang der Dellenfamilie d' = 0 ... d bei festem w (ohne Rauschen). Liegt es unter der
    Keimbarriere F_b, ist die Delle mit dem homogenen Zustand unterhalb der Barriere verbunden und kann (dF erhalten)
    nicht kavitieren. Ein dF < 0 allein reicht nicht: volle Dellen liegen schon jenseits der Barriere."""
    if d == 0.0 or w == 0.0:
        return 0.0
    dd = torch.linspace(0.0, d, n, dtype=F64, device=x.device).unsqueeze(1)
    p = math.sqrt(s0) * (1.0 - dd * torch.exp(-x ** 2 / (2.0 * w ** 2)).unsqueeze(0))
    s = p * p
    g = (torch.roll(p, -1, dims=1) - p) / dx
    om2 = 1.0 - 2.0 * s0 + 1.5 * s0 * s0
    f = (g * g + s - s * s + 0.5 * s ** 3 - om2 * s).sum(1) * dx - (s0 - s0 * s0 + 0.5 * s0 ** 3 - om2 * s0) * dx * x.shape[0]
    return float(f.max())


def ka_start(psi, s0t, dx, laeufe=None, x=None):
    """Anfangswerte je Lauf: dF = Int (|psi_x|^2 + U(S) - omega^2 S) - dasselbe homogen (psi_t = -i omega psi, daher
    H - omega Q ohne kinetischen Rest), groesstes dF entlang der Dellenfamilie, Defizitflaeche A = Int (S0 - S),
    kleinste Dichte, Leerlaenge."""
    s = r5b.dichte(psi)
    om2 = (1.0 - 2.0 * s0t + 1.5 * s0t * s0t).unsqueeze(1)
    g = (torch.roll(psi, -1, dims=1) - psi) / dx
    u = s - s * s + 0.5 * s ** 3
    s0v = s0t.unsqueeze(1)
    u0 = s0v - s0v * s0v + 0.5 * s0v ** 3
    df = ((g.real ** 2 + g.imag ** 2 + u - om2 * s) - (u0 - om2 * s0v)).sum(1) * dx
    pfad = [df_pfad(l["s0"], l["w"], l["d"], x, dx) for l in laeufe] if laeufe is not None else None
    return {"dF": df.cpu().tolist(), "dF_pfad_max": pfad, "A": ((s0v - s).sum(1) * dx).cpu().tolist(),
            "S_min_0": s.min(1).values.cpu().tolist(), "leer_0": ((s < 0.5 * s0v).to(F64).sum(1) * dx).cpu().tolist()}


def ka_felder(laeufe, x, L):
    basis = r5b.rausch_basis(x, KA_SAAT, 0.5 * 2.0 * PI / L, r5b.M_KMAX, L)[0]
    felder = []
    for l in laeufe:
        s0 = l["s0"]
        om = math.sqrt(1.0 - 2.0 * s0 + 1.5 * s0 * s0)
        p = math.sqrt(s0) * (1.0 + KA_DELTA * basis)
        if l["d"] > 0.0:
            p = p * (1.0 - l["d"] * torch.exp(-x ** 2 / (2.0 * l["w"] ** 2)))
        felder.append((p, (-1j * om) * p))
    return r5b.stapel(felder, rand_null=False)


def ka_nur_vorhersage(opt, out):
    """Nur die Vorhersage je Lauf aus den Anfangsfeldern (keine Zeitentwicklung), Gitter L = 200, dx = 0,1."""
    teil = opt.teil or "raster"
    s0_liste = KA_S0 if not opt.s0 else [float(v) for v in opt.s0.split(",")]
    laeufe = ka_laeufe(teil, s0_liste)
    alt = r5b.M_L
    r5b.M_L = 200.0
    try:
        x = r5b.gitter_periodisch(0.1)
        psi, _ = ka_felder(laeufe, x, 200.0)
        s0t = torch.tensor([l["s0"] for l in laeufe], dtype=F64, device=DEV)
        st = ka_start(psi, s0t, 0.1, laeufe, x)
    finally:
        r5b.M_L = alt
    zz = [f"(c) Vorhersage vorab, Teil {teil} (nur Anfangsfelder, L = 200, dx = 0,1): Lauf | d | S_min(0) | S_t | "
          "dF/F_b | dF_Pfad_max/F_b | Vorhersage"]
    tab = []
    for b, l in enumerate(laeufe):
        bo = bounce(l["s0"])
        v = ka_vorhersage(l, st["dF_pfad_max"][b], st["S_min_0"][b], bo)
        tab.append({"s0": l["s0"], "tiefe": l["name"], "w": l["w"], "d": l["d"], "S_min_0": st["S_min_0"][b],
                    "dF": st["dF"][b], "dF_pfad_max": st["dF_pfad_max"][b], "F_b": bo["F_b"], "vorhersage": v})
        zz.append(f"  S0={l['s0']} {l['name']:9s} w={l['w']:.0f} | {l['d']:.4f} | {st['S_min_0'][b]:.4f} | "
                  f"{bo['S_t']:.3f} | {fz(teilen(st['dF'][b], bo['F_b']), '+.2f')} | "
                  f"{fz(teilen(st['dF_pfad_max'][b], bo['F_b']), '.2f')} | {v}")
    zaehl = {}
    for e in tab:
        zaehl[e["vorhersage"]] = zaehl.get(e["vorhersage"], 0) + 1
    zz.append("  Summe: " + ", ".join(f"{k} {v}" for k, v in sorted(zaehl.items())))
    return f"kavitation_vorhersage_{teil}", {"tabelle": tab}, zz, []


def ka_rechnen(opt, out, name, laeufe, stufen, t_end):
    roh, zeiten = {}, []
    sek_grob = {}
    for st_name, L, dx, dt in stufen:
        basis_name = st_name.split("_")[0] + "_grob"
        if st_name.endswith(("_fein", "_sehrfein")) and basis_name in sek_grob:
            faktor = 4.5 if st_name.endswith("_fein") else 18.0
            if rest_sek() < faktor * sek_grob[basis_name]:
                print(f"{name} {st_name}: entfaellt (Restzeit {rest_sek():.0f} s)", flush=True)
                continue
        alt = r5b.M_L
        r5b.M_L = L
        try:
            x = r5b.gitter_periodisch(dx)
            psi, vel = ka_felder(laeufe, x, L)
            s0t = torch.tensor([l["s0"] for l in laeufe], dtype=F64, device=DEV)
            start = ka_start(psi, s0t, dx, laeufe, x)
            schnapp = []
            schritt = max(1, int(round(0.1 / dx)))
            t0 = uhr()
            t, daten = r5b.entwickeln(psi, vel, dx, dt, t_end, KA_MESS, messer_ka(x, dx, s0t, schnapp, schritt),
                                      periodisch=True)
            sek = uhr() - t0
        finally:
            r5b.M_L = alt
        if st_name.endswith("_grob"):
            sek_grob[st_name] = sek
        schritte = int(round(t_end / dt))
        ze = zeit_eintrag("kavitation", st_name, psi.shape[0], psi.shape[1], schritte, sek)
        zeiten.append(ze)
        print(f"{name} {st_name}: {psi.shape[0]} Laeufe x {psi.shape[1]} Punkte, T = {t_end}, {sek:.1f} s "
              f"({ze['ms_je_schritt']:.2f} ms je Schritt)", flush=True)
        roh[st_name] = {"befehl": "kavitation", "stufe": st_name, "laeufe": laeufe, "t": t.cpu(), "daten": daten.cpu(),
                        "spalten": KA_SPALTEN, "L": L, "dx": dx, "dt": dt, "T_soll": t_end, "sek": sek, "start": start,
                        "schnapp": torch.stack(schnapp) if schnapp else None, "schnapp_dt": KA_SNAP, "zeit": ze}
        roh_sichern(out, name, st_name, roh[st_name])
    return roh, zeiten


def ka_vorhersage(l, df_pfad_max, smin0, bo):
    """Vorab festgelegt (PLAN.md): Minimum ueber der Spinodale oder dF entlang der ganzen Dellenfamilie unter der
    Keimbarriere F_b -> heilt; sonst Minimum unter S_t = 2 - 2 S0 -> kavitiert (S0 <= 0,75 zerfaellt in Klumpen,
    0,80 einzelne Kaverne); dazwischen unklar."""
    if l["d"] == 0.0:
        return "heilt"
    if smin0 > SPIN or df_pfad_max < bo["F_b"]:
        return "heilt"
    if smin0 < bo["S_t"]:
        return "zerfaellt" if l["s0"] <= 0.75 else "Kaverne"
    return "unklar"


def auswertung_ka(roh):
    t, d = roh["t"], roh["daten"]
    T = float(t[-1])
    L = roh["L"]
    n10 = max(1, t.shape[0] // 10)
    zweite = t >= 0.5 * T
    zeilen = []
    for b, l in enumerate(roh["laeufe"]):
        c = {n: d[:, b, k] for k, n in enumerate(KA_SPALTEN)}
        bo = bounce(l["s0"])
        df, a0 = roh["start"]["dF"][b], roh["start"]["A"][b]
        dfp = roh["start"]["dF_pfad_max"][b]
        smin0, leer0 = roh["start"]["S_min_0"][b], roh["start"]["leer_0"][b]
        leer, luecken = c["leer"], c["luecken"]
        max_leer2 = float(leer[zweite].max())
        luecken_end = float(luecken[-n10:].median())
        leer_end = float(leer[-n10:].mean())
        if max_leer2 == 0.0:
            kl = "heilt"
        elif luecken_end >= 3.0:
            kl = "zerfaellt"
        else:
            kl = "Kaverne"
        kav = torch.nonzero(leer >= max(10.0, leer0 + 5.0)).squeeze(1)
        im = t.shape[0] // 2
        z = {"name": f"S0={l['s0']} {l['name']} w={l['w']}", "s0": l["s0"], "tiefe": l["name"], "w": l["w"],
             "d": l["d"], "S_min_0": smin0, "A": a0, "dF": df, "S_t": bo["S_t"], "F_b": bo["F_b"], "A_b": bo["A_b"],
             "dF_durch_F_b": teilen(df, bo["F_b"]), "dF_pfad_durch_F_b": teilen(dfp, bo["F_b"]),
             "vorhersage": ka_vorhersage(l, dfp, smin0, bo), "klasse": kl,
             "t_kav": float(t[int(kav[0])]) if kav.numel() > 0 else NAN,
             "leer_0_mitte_ende": [leer0, float(leer[im]), leer_end], "leer_max": float(leer.max()),
             "luecken_ende": luecken_end, "klumpen_ende": float(c["klumpen"][-n10:].median()),
             "S_min_zweite": float(c["S_min"][zweite].min()), "S_mitte_ende": float(c["S_mitte"][-n10:].mean()),
             "spinodal_ende": float(c["spinodal"][-n10:].mean()), "rms_ende": float(c["rms"][-1]),
             "Q_drift": float((c["Q_box"][-1] - c["Q_box"][0]) / c["Q_box"][0]),
             "E_drift": float((c["E_box"][-1] - c["E_box"][0]) / c["E_box"][0])}
        z["treffer"] = z["vorhersage"] == kl
        z["treffer_grob"] = (z["vorhersage"] == "heilt") == (kl == "heilt") if z["vorhersage"] != "unklar" else None
        z["plaus_ok"] = bool(abs(z["Q_drift"]) < 1e-10 and abs(z["E_drift"]) < 1e-3
                             and 0.0 <= float(leer.min()) and float(leer.max()) <= L + 1e-9
                             and float(c["S_min"].min()) >= 0.0)
        if l["d"] == 0.0:
            z["kontrolle_rms_rel"] = z["rms_ende"] / l["s0"]
        zeilen.append(z)
    return zeilen


def bericht_ka(teil, roh, ausw, vergleiche):
    zz = [f"(c) Kavitation, Teil {teil}: periodische Box, T = Laufzeit, Rauschen {KA_DELTA} (Saat {KA_SAAT}), "
          "Delle psi -> psi (1 - d exp(-x^2/2w^2)), psi_t = -i omega_bg psi.",
          "  Kritischer Keim (Bounce bei festem omega): S0 | S_t = 2 - 2 S0 | x_halb | A_b | F_b | kappa"]
    for s0 in sorted({l["s0"] for r in roh.values() for l in r["laeufe"]}):
        bo = bounce(s0)
        zz.append(f"    {s0} | {bo['S_t']:.3f} | {fz(bo['x_halb'], '.3f')} | {fz(bo['A_b'], '.4f')} | "
                  f"{fz(bo['F_b'], '.3e')} | {fz(bo['kappa'], '.4f')}")
    zz.append("  Klasse: heilt = keine Stelle mit S < S0/2 in [T/2, T]; zerfaellt = >= 3 Luecken (Median letzte 10 %); "
              "sonst Kaverne. t_kav: Leerlaenge >= max(10, Anfang + 5).")
    for st, zeilen in ausw.items():
        zz.append(f"  [{st}] L = {roh[st]['L']}, dx = {roh[st]['dx']}, dt = {roh[st]['dt']}")
        zz.append("  Lauf | d | S_min(0) | A | dF (dF/F_b; Pfad-Max/F_b) | Vorhersage | Klasse | t_kav | Leer 0/Mitte/"
                  "Ende (max) | Luecken | Klumpen | S_min 2. Haelfte | Q-, E-Drift | plaus")
        for z in zeilen:
            lm = z["leer_0_mitte_ende"]
            zz.append(f"  {z['name']:28s} | {z['d']:.4f} | {z['S_min_0']:.4f} | {z['A']:.3f} | {z['dF']:+.3e} "
                      f"({fz(z['dF_durch_F_b'], '.2f')}; {fz(z['dF_pfad_durch_F_b'], '.2f')}) | {z['vorhersage']:9s} | "
                      f"{z['klasse']:9s} | "
                      f"{fz(z['t_kav'], '.0f')} | {lm[0]:.1f}/{lm[1]:.1f}/{lm[2]:.1f} ({z['leer_max']:.1f}) | "
                      f"{z['luecken_ende']:.0f} | {z['klumpen_ende']:.0f} | {z['S_min_zweite']:.3f} | "
                      f"{z['Q_drift']:+.1e}, {z['E_drift']:+.1e} | {'ok' if z['plaus_ok'] else 'NEIN'}")
        tr = [z for z in zeilen if z["d"] > 0.0]
        n_tr = sum(1 for z in tr if z["treffer"])
        grob = [z for z in tr if z["treffer_grob"] is not None]
        zz.append(f"  Vorhersage genau getroffen: {n_tr} von {len(tr)} Dellen; heilt/heilt-nicht getroffen: "
                  f"{sum(1 for z in grob if z['treffer_grob'])} von {len(grob)} (ohne 'unklar')")
        ko = [z for z in zeilen if z["d"] == 0.0]
        zz.append("  Kontrollen ohne Delle (rms/S0 am Ende): " + ", ".join(
            f"{z['s0']}: {z['kontrolle_rms_rel']:.1e} ({z['klasse']})" for z in ko))
    for v in vergleiche:
        zz.append(f"  Vergleich {v['art']} {v['a']} gegen {v['b']}:")
        n_ok = sum(1 for e in v["liste"] if e["klasse_gleich"])
        zz.append(f"    Klasse gleich in {n_ok} von {len(v['liste'])}; t_kav L3 "
                  f"{sum(1 for e in v['liste'] if e['t_kav']['bestanden'])} von "
                  f"{sum(1 for e in v['liste'] if endlich(e['t_kav']['effekt']))} definierten")
        for e in v["liste"]:
            if not e["klasse_gleich"] or (endlich(e["t_kav"]["effekt"]) and not e["t_kav"]["bestanden"]):
                zz.append(f"    abweichend: {e['name']}: {e['klasse_a']} / {e['klasse_b']}, t_kav "
                          f"{fz(e['t_kav_a'], '.0f')} / {fz(e['t_kav_b'], '.0f')}, Luecken je 100 "
                          f"{fz(e['luecken_je_100_a'], '.1f')} / {fz(e['luecken_je_100_b'], '.1f')}")
    return zz


def ka_vergleich(art, a, b, za, zb, la, lb):
    liste = []
    for x, y in zip(za, zb):
        liste.append({"name": x["name"], "klasse_a": x["klasse"], "klasse_b": y["klasse"],
                      "klasse_gleich": x["klasse"] == y["klasse"], "t_kav_a": x["t_kav"], "t_kav_b": y["t_kav"],
                      "t_kav": l3(x["t_kav"], y["t_kav"], 0.0),
                      "leer_ende": l3(x["leer_0_mitte_ende"][2], y["leer_0_mitte_ende"][2], 0.0),
                      "luecken_je_100_a": 100.0 * x["luecken_ende"] / la,
                      "luecken_je_100_b": 100.0 * y["luecken_ende"] / lb})
    return {"art": art, "a": a, "b": b, "liste": liste}


def lauf_kavitation(opt, out):
    if opt.nur_vorhersage:
        return ka_nur_vorhersage(opt, out)
    teil = "rauch" if opt.rauch else (opt.teil or "raster")
    s0_liste = KA_S0 if not opt.s0 else [float(v) for v in opt.s0.split(",")]
    name = f"kavitation_{teil}" + ("" if (teil != "raster" or not opt.s0) else "_" + opt.s0.replace(",", "_"))
    stufen = ka_stufen(teil, opt)
    t_end = 30.0 if opt.rauch else (opt.T or KA_T)
    zeiten, roh = [], {}
    if not opt.nur_auswertung:
        roh, zeiten = ka_rechnen(opt, out, name, ka_laeufe(teil, s0_liste), stufen, t_end)
    for st in ("L200_grob", "L200_fein", "L200_sehrfein", "L400_grob", "L400_fein"):
        if st not in roh:
            geladen = roh_laden(out, name, st)
            if geladen is not None:
                roh[st] = geladen
    if not roh:
        raise RuntimeError("keine Rohdaten vorhanden")
    ausw = {st: auswertung_ka(r) for st, r in roh.items()}
    vergleiche = []
    for art, a, b in (("L3", "L200_grob", "L200_fein"), ("L3", "L400_grob", "L400_fein"),
                      ("L3", "L200_fein", "L200_sehrfein"), ("Box", "L200_grob", "L400_grob"),
                      ("Box", "L200_fein", "L400_fein")):
        if a in ausw and b in ausw:
            vergleiche.append(ka_vergleich(art, a, b, ausw[a], ausw[b], roh[a]["L"], roh[b]["L"]))
    res = {"teil": teil, "auswertung": ausw, "vergleiche": vergleiche, "zeiten": zeiten,
           "bounce": {str(s0): bounce(s0) for s0 in sorted({l["s0"] for r in roh.values() for l in r["laeufe"]})}}
    return name, res, bericht_ka(teil, roh, ausw, vergleiche), zeiten


# ---------------------------------------------------------------- Rauchtest, Hochrechnung, Hauptprogramm

def hochrechnung(zeiten):
    """Zeit je Schritt = c0 + c1 * B * N, getrennt fuer radial (tod) und 1D, aus den Rauch-Stufen; dann die geplanten
    Aufrufe (Schritte und Groessen wie in PLAN.md). Nur grob: der Rauchtest ist kurz."""
    def fit(pkte):
        if not pkte:
            return NAN, NAN
        if len(pkte) == 1:
            return 0.0, pkte[0][1] / pkte[0][0]
        c1 = steigung_xy(pkte)
        c0 = sum(p[1] for p in pkte) / len(pkte) - c1 * sum(p[0] for p in pkte) / len(pkte)
        return max(c0, 0.0), max(c1, 0.0)
    rad = fit([(z["B"] * z["N"], z["sek"] / max(1, z["schritte"])) for z in zeiten if z["befehl"] == "tod"])
    eind = fit([(z["B"] * z["N"], z["sek"] / max(1, z["schritte"])) for z in zeiten if z["befehl"] != "tod"])
    plan = [("tod grob T=4000", rad, 8, 1501, 80000), ("tod fein T=2000", rad, 8, 3001, 80000),
            ("tod beide T=3000 (grob+fein)", rad, None, None, None),
            ("fuettern mechanik grob", eind, 43, 6401, 12000), ("fuettern mechanik fein", eind, 43, 12801, 24000),
            ("fuettern raster55/70 grob", eind, 149, 6401, 12000), ("fuettern raster55/70 fein", eind, 149, 12801, 24000),
            ("kavitation raster alle S0 grob", eind, 100, 2000, 12000),
            ("kavitation raster alle S0 fein", eind, 100, 4000, 24000),
            ("kavitation raster ein S0 grob", eind, 25, 2000, 12000),
            ("kavitation raster ein S0 fein", eind, 25, 4000, 24000),
            ("kavitation box L200 grob+fein", eind, None, None, None), ("kavitation box L400 grob", eind, 10, 4000, 12000),
            ("kavitation box L400 fein", eind, 10, 8000, 24000), ("kavitation box L200 sehrfein", eind, 10, 8000, 48000)]
    zz = [f"Hochrechnung (Schritt = c0 + c1 B N): radial c0 = {fz(rad[0] * 1e3, '.3f')} ms, c1 = {fz(rad[1] * 1e9, '.1f')} "
          f"ns; 1D c0 = {fz(eind[0] * 1e3, '.3f')} ms, c1 = {fz(eind[1] * 1e9, '.1f')} ns"]
    for nm, (c0, c1), b, n, s in plan:
        if nm.startswith("tod beide"):
            sek = 60000 * (c0 + c1 * 8 * 1501) + 120000 * (c0 + c1 * 8 * 3001)
        elif nm.startswith("kavitation box L200"):
            sek = 12000 * (c0 + c1 * 10 * 2000) + 24000 * (c0 + c1 * 10 * 4000)
        else:
            sek = s * (c0 + c1 * b * n)
        zz.append(f"  {nm:34s}: {fz(sek, '.0f')} s ({fz(sek / 60.0, '.1f')} min)")
    return zz


def lauf_rauch(opt, out):
    teile, fehler, zz, zeiten = {}, {}, [], []
    for nm, funk in (("tod", lauf_tod), ("fuettern", lauf_fuettern), ("kavitation", lauf_kavitation)):
        t0 = uhr()
        try:
            opt.nur_auswertung = False
            name, res, text, zt = funk(opt, out)
            zeiten += zt
            teile[nm] = res
            zz += text
            opt.nur_auswertung = True                       # zweiter Durchgang: nur aus den Rohdaten auswerten
            name2, _, text2, _ = funk(opt, out)
            zz.append(f"  --nur-auswertung {name2}: {len(text2)} Berichtszeilen, gleich lang wie oben: "
                      f"{len(text2) == len(text)}")
        except Exception:
            fehler[nm] = traceback.format_exc()
            zz += [f"{nm} FEHLER:", fehler[nm]]
            print(fehler[nm], flush=True)
        finally:
            opt.nur_auswertung = False
        zz += [f"  Rauchtest {nm}: {uhr() - t0:.1f} s", ""]
    try:
        _, res_v, text_v, _ = ka_nur_vorhersage(opt, out)
        teile["kavitation_vorhersage"] = res_v
        zz += text_v + [""]
    except Exception:
        fehler["kavitation_vorhersage"] = traceback.format_exc()
        zz += ["kavitation_vorhersage FEHLER:", fehler["kavitation_vorhersage"]]
    zz += hochrechnung(zeiten)
    return "rauch", {"teile": teile, "fehler_teile": fehler, "zeiten": zeiten}, zz, zeiten


BEFEHLE = {"tod": lauf_tod, "fuettern": lauf_fuettern, "kavitation": lauf_kavitation, "rauch": lauf_rauch}


def main():
    global DEV
    ap = argparse.ArgumentParser(description="Runde 7, Karte R5F: Tod, Fuettern, Kavitation (Folgen aus Runde 5)")
    ap.add_argument("befehl", choices=sorted(BEFEHLE))
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda")
    ap.add_argument("--out", default=None, help="Ausgabeordner (Voreinstellung ausgabe-<befehl> neben dem Skript)")
    ap.add_argument("--stufe", choices=["grob", "fein", "beide"], default="beide")
    ap.add_argument("--teil", default=None, help="fuettern: mechanik|raster55|raster70; kavitation: raster|box")
    ap.add_argument("--s0", default=None, help="kavitation raster: nur diese S0 (Komma-Liste), fuer CPU-Spuren")
    ap.add_argument("--T", type=float, default=None, help="Laufzeit (Voreinstellung tod 3000, fuettern 600, kav. 600)")
    ap.add_argument("--sehrfein", action="store_true", help="kavitation box: zusaetzlich dx = 0,025, dt = 0,0125")
    ap.add_argument("--nur-auswertung", dest="nur_auswertung", action="store_true",
                    help="nichts rechnen, vorhandene Rohdaten aus --out auswerten (auch L3 grob gegen fein)")
    ap.add_argument("--nur-vorhersage", dest="nur_vorhersage", action="store_true",
                    help="kavitation: nur die Vorhersage je Lauf aus den Anfangsfeldern (keine Zeitentwicklung)")
    ap.add_argument("--kand", type=int, default=None, help="Kandidaten je Schiessrunde (cuda 1024, cpu 256)")
    ap.add_argument("--runden", type=int, default=None, help="Schiessrunden (cuda 4, cpu 5)")
    opt = ap.parse_args()
    if opt.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("Kein CUDA-Geraet sichtbar: auf einer cpu-Spur mit --geraet cpu starten.")
        DEV = torch.device("cuda")
        gesamt = torch.cuda.get_device_properties(0).total_memory
        torch.cuda.set_per_process_memory_fraction(min(1.0, SPEICHER_GB * 2 ** 30 / gesamt))
        geraet = torch.cuda.get_device_name(0)
    else:
        DEV = torch.device("cpu")
        torch.set_num_threads(1)
        geraet = "CPU, 1 Faden"
    r5a.DEV = DEV
    r5b.DEV = DEV
    opt.rauch = opt.befehl == "rauch"
    if opt.kand is None:
        opt.kand = r5a.N_KAND3 if DEV.type == "cuda" else 256
    if opt.runden is None:
        opt.runden = r5a.RUNDEN3 if DEV.type == "cuda" else 5
    if opt.rauch:
        opt.runden = min(opt.runden, 2)
    out = opt.out or os.path.join(HIER, "ausgabe-" + opt.befehl)
    os.makedirs(out, exist_ok=True)
    T_START[0] = uhr()
    r5a.T_START[0] = r5a.uhr()
    r5a.ZEIT_BUDGET = ZEIT_BUDGET
    start = jetzt()
    kopf = (f"Runde 7 R5F {opt.befehl} Start {start} auf {geraet}, torch {torch.__version__}, Stufe {opt.stufe}, "
            f"Teil {opt.teil}, T {opt.T}, nur-auswertung {opt.nur_auswertung}")
    print(kopf, flush=True)
    ausgabe = {"start": start, "geraet": geraet, "torch": torch.__version__, "befehl": opt.befehl,
               "argumente": vars(opt), "ergebnis": None, "fehler": None}
    text = [kopf, ""]
    name = opt.befehl
    try:
        name, res, zz, _ = BEFEHLE[opt.befehl](opt, out)
        ausgabe["ergebnis"] = res
        text += zz
        if opt.rauch and res["fehler_teile"]:
            ausgabe["fehler"] = sorted(res["fehler_teile"])
    except Exception:
        ausgabe["fehler"] = traceback.format_exc()
        text += ["FEHLER:", ausgabe["fehler"]]
        print(ausgabe["fehler"], flush=True)
    ausgabe["ende"] = jetzt()
    ausgabe["dauer_s"] = uhr() - T_START[0]
    speicher = torch.cuda.max_memory_allocated() / 2 ** 20 if DEV.type == "cuda" else NAN
    ausgabe["torch_speicher_max_mb"] = speicher
    text += ["", f"Ende {ausgabe['ende']}, Dauer {ausgabe['dauer_s']:.1f} s, Torch-Speicher max {fz(speicher, '.0f')} MB, "
                 f"Fehler: {'keine' if not ausgabe['fehler'] else 'ja (siehe oben)'}"]
    with open(os.path.join(out, f"{name}_bericht.txt"), "w") as fh:
        fh.write("\n".join(text) + "\n")
    with open(os.path.join(out, f"{name}_ergebnis.json"), "w") as fh:
        json.dump(ausgabe, fh, indent=1, default=str)
    print("\n".join(text), flush=True)
    if ausgabe["fehler"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
