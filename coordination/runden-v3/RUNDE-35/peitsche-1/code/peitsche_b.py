#!/usr/bin/env python3
"""RUNDE-35, Karte PEITSCHE-1, Teil B: Energiefluss-Geschwindigkeit drehender Q-Baelle in M1 (2D).

Plan und Urteilsregeln: ../PLAN.md (eingefroren). Explorativ (v3), synthetisch.
Profile aus regge2d.py (RUNDE-06, RG-1; Kopie in code/, unveraendert, sha256 im Plan). Dieses Skript ruft dessen
Funktionen zeilen_bauen, parameter, schiessen, profile_bauen und gitterprobe auf; profile_bauen bekommt alle Zeilen
als "Gitterschluessel", damit es jedes Profil (f, f', h) zurueckgibt.

M1: U(S) = S - S^2 + S^3/2, L = |psi_t|^2 - |grad psi|^2 - U, psi = f(r) exp(i(omega t + m theta)).
    T^00 = omega^2 f^2 + f'^2 + m^2 f^2/r^2 + U(f^2),  |T^0theta| = 2 omega m f^2 / r,
    v_E(r) = |T^0theta| / T^00 (v_E(0) = 0),  Schranke v_E <= omega / sqrt(omega^2 + 1/2).
Kontrollen: Q, E gegen RG-1 (gleiches h0), J = m Q auf dem kartesischen Gitter (regge2d.gitterprobe), dazu v_E auf
demselben Gitter aus spektralen Ableitungen (T^0i = -2 Re(psi_t^* d_i psi)), verglichen mit dem radialen Wert.

Aufruf: python3 peitsche_b.py --h0 0.005 --out ORDNER [--m 1,2,3,5,8] [--w2 ...] [--rg1 RG1/ergebnis.json]
"""
import os

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse
import datetime
import json
import math
import platform
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import regge2d as rg  # noqa: E402

M_STANDARD = (1, 2, 3, 5, 8)
GITTER_W2 = (0.55, 0.70, 0.80, 0.95)
S_SCHWELLE_GITTER = 1e-6        # Vergleich radial/Gitter nur wo S >= 1e-6 S_max
OMEGA_MIN2 = 0.5


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def schranke(w2):
    return math.sqrt(w2) / math.sqrt(w2 + OMEGA_MIN2)


def v_e_radial(f, fp, h, m, w2):
    om = math.sqrt(w2)
    r = np.arange(f.size) * h
    S = f * f
    rs = np.where(r > 0.0, r, 1.0)
    num = np.where(r > 0.0, 2.0 * om * m * S / rs, 0.0)
    den = w2 * S + fp * fp + np.where(r > 0.0, m * m * S / (rs * rs), 0.0) + rg.upot(S)
    vE = np.where(den > 0.0, num / np.where(den > 0.0, den, 1.0), 0.0)
    return r, S, vE, num, den


def v_e_gitter(zeile, prof):
    """Wie regge2d.gitterprobe (gleiches Gitter), dazu |T^0i|/T^00 aus spektralen Ableitungen."""
    f_tab, fp_tab, h = prof
    m = zeile["m"]
    w2 = zeile["w2"]
    om = math.sqrt(w2)
    fmax = float(np.max(f_tab))
    r_tab = np.arange(f_tab.size) * h
    ueber = np.nonzero(f_tab > 1e-8 * fmax)[0]
    L = float(r_tab[ueber[-1]]) + 2.0
    skala = fmax / float(np.max(np.abs(fp_tab)))
    dx = min(0.25, skala / rg.GITTER_PUNKTE_JE_SKALA)
    N = int(math.ceil(2.0 * L / dx))
    N += N % 2
    if N > rg.GITTER_N_MAX:
        N = rg.GITTER_N_MAX
    dx = 2.0 * L / N
    x = -L + dx * np.arange(N)
    X, Y = np.meshgrid(x, x, indexing="ij")
    R = np.hypot(X, Y)
    fr = rg.hermite(f_tab, fp_tab, h, R)
    with np.errstate(invalid="ignore", divide="ignore"):
        ph = np.where(R > 0.0, (X + 1j * Y) / np.where(R > 0.0, R, 1.0), 0.0)
    psi = fr * ph ** m
    del fr
    k = 2.0 * math.pi * np.fft.fftfreq(N, d=dx)
    KX, KY = np.meshgrid(k, k, indexing="ij")
    psik = np.fft.fft2(psi)
    dpx = np.fft.ifft2(1j * KX * psik)
    dpy = np.fft.ifft2(1j * KY * psik)
    del psik, KX, KY
    s = (psi * np.conj(psi)).real
    T00 = w2 * s + (dpx * np.conj(dpx)).real + (dpy * np.conj(dpy)).real + rg.upot(s)
    jx = (np.conj(psi) * dpx).imag
    jy = (np.conj(psi) * dpy).imag
    T0 = 2.0 * om * np.sqrt(jx * jx + jy * jy)
    maske = s >= S_SCHWELLE_GITTER * float(np.max(s))
    v = np.where(maske, T0 / np.where(T00 > 0.0, T00, 1.0), 0.0)
    j = int(np.argmax(v))
    return dict(N=N, dx=dx, L=L, vE_max_gitter=float(v.flat[j]), r_bei_max_gitter=float(R.flat[j]))


def main():
    ap = argparse.ArgumentParser(description="PEITSCHE-1 Teil B")
    ap.add_argument("--h0", type=float, required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--m", default="")
    ap.add_argument("--w2", default="")
    ap.add_argument("--rg1", default=None, help="RG-1 ergebnis.json mit gleichem h0")
    ap.add_argument("--gitter-w2", default="")
    args = ap.parse_args()
    start = jetzt()
    t0 = time.perf_counter()
    m_liste = [int(x) for x in args.m.split(",") if x.strip()] or list(M_STANDARD)
    w2_liste = [float(x) for x in args.w2.split(",") if x.strip()] or list(rg.W2_STANDARD)
    g_w2 = [float(x) for x in args.gitter_w2.split(",") if x.strip()] or list(GITTER_W2)
    zeilen = rg.zeilen_bauen(m_liste, w2_liste, False)
    P = rg.parameter(zeilen, args.h0)
    print(f"Teil B: {P['n']} Zeilen, m = {m_liste}, {len(w2_liste)} Werte omega^2, h0 = {args.h0}", flush=True)
    sch = rg.schiessen(P, lambda s: print(s, flush=True))
    schl = set((z["m"], rg.w2_schluessel(z["w2"]), False) for z in zeilen)
    erg, profile = rg.profile_bauen(P, sch, zeilen, schl, print)
    t1 = time.perf_counter()
    rg1 = None
    if args.rg1:
        with open(args.rg1) as fh:
            rg1 = {(z["m"], rg.w2_schluessel(z["w2"])): z for z in json.load(fh)["tabelle"]["zeilen"] if not z["nls"]}
    zeilen_aus = []
    kurven = {}
    for z in erg:
        m, w2 = z["m"], z["w2"]
        k = (m, rg.w2_schluessel(w2), False)
        e = dict(m=m, w2=w2, h=z["h"], gueltig=z["gueltig"], grund=z["grund"], konvergiert=z["konvergiert"])
        if k not in profile or "Q" not in z:
            e["vE_max"] = None
            zeilen_aus.append(e)
            continue
        f, fp, h = profile[k]
        r, S, vE, T0, T00 = v_e_radial(f, fp, h, m, w2)
        j = int(np.argmax(vE))
        # beschreibend: energiegewichtetes Mittel (Simpson, 2 pi r dr) und Maximum im energietragenden Bereich
        wq = rg.simpson_gewichte(f.size, h) * r
        v_mittel = float(np.sum(wq * T0) / np.sum(wq * T00))
        tragend = T00 >= 1e-2 * float(np.max(T00))
        jt = int(np.argmax(np.where(tragend, vE, -1.0)))
        vb = schranke(w2)
        om = math.sqrt(w2)
        maske = S >= S_SCHWELLE_GITTER * float(np.max(S))
        jm = int(np.argmax(np.where(maske, vE, -1.0)))
        e.update(Q=z["Q"], E=z["E"], J=z["J"], R_max=z["R_max"], S_max=z["S_max"], R_innen=z["R_innen"],
                 R_aussen=z["R_aussen"], virial=z["virial"], vE_max=float(vE[j]), r_bei_vE_max=float(r[j]),
                 S_bei_vE_max=float(S[j]), fp_durch_f_bei_vE_max=float(fp[j] / f[j]) if f[j] != 0.0 else None,
                 vE_max_maske=float(vE[jm]), vE_mittel_energie=v_mittel, vE_max_tragend=float(vE[jt]),
                 r_bei_vE_max_tragend=float(r[jt]), schranke=vb, vE_durch_schranke=float(vE[j] / vb),
                 vE_minus_schranke_max=float(np.max(vE - vb)),
                 vE_bei_R_max=float(np.interp(z["R_max"], r, vE)),
                 schaetzung_m_durch_R_omega=float(m / (z["R_max"] * om)))
        if rg1 is not None:
            ref = rg1.get((m, rg.w2_schluessel(w2)))
            if ref is not None and ref.get("gueltig") and "Q" in ref:
                e["rg1"] = dict(Q_rel=z["Q"] / ref["Q"] - 1.0, E_rel=z["E"] / ref["E"] - 1.0, h_rg1=ref["h"],
                                rg1_gueltig=True)
            else:
                e["rg1"] = dict(rg1_gueltig=False)
        zeilen_aus.append(e)
        # Kurve v_E(r), ausgeduennt auf hoechstens 4000 Punkte
        st = max(1, r.size // 4000)
        kurven[f"m{m}_w{w2:.3f}_r"] = r[::st]
        kurven[f"m{m}_w{w2:.3f}_vE"] = vE[::st]
        kurven[f"m{m}_w{w2:.3f}_S"] = S[::st]
    t2 = time.perf_counter()
    proben = []
    for z in erg:
        if z["w2"] is None or not any(abs(z["w2"] - g) < 1e-9 for g in g_w2) or not z["gueltig"]:
            continue
        k = (z["m"], rg.w2_schluessel(z["w2"]), False)
        if k not in profile:
            continue
        tg = time.perf_counter()
        pr = rg.gitterprobe(z, profile[k])
        pv = v_e_gitter(z, profile[k])
        e = next(x for x in zeilen_aus if x["m"] == z["m"] and abs(x["w2"] - z["w2"]) < 1e-12)
        pr.update(pv)
        pr["vE_max_radial_maske"] = e["vE_max_maske"]
        pr["vE_gitter_minus_radial"] = pv["vE_max_gitter"] - e["vE_max_maske"]
        pr["dauer_s"] = time.perf_counter() - tg
        proben.append(pr)
        print(f"  Gitter m = {z['m']}, w2 = {z['w2']}: N = {pr['N']}, J/(mQ)-1 = {pr['J_durch_mQ_minus_1']:.1e}, "
              f"vE Gitter {pv['vE_max_gitter']:.6f} radial {e['vE_max_maske']:.6f}", flush=True)
    t3 = time.perf_counter()
    os.makedirs(args.out, exist_ok=True)
    ergebnis = dict(karte="PEITSCHE-1 Teil B", start=start, ende=jetzt(), h0=args.h0, m_liste=m_liste,
                    w2_liste=w2_liste, rg1_datei=args.rg1, host=platform.node(), numpy=np.__version__,
                    python=platform.python_version(),
                    dauer=dict(schiessen_profile_s=t1 - t0, vE_s=t2 - t1, gitter_s=t3 - t2),
                    zeilen=zeilen_aus, gitterprobe=proben)
    with open(os.path.join(args.out, "teil_b.json"), "w") as fh:
        json.dump(ergebnis, fh, indent=1, ensure_ascii=False, default=float)
    np.savez_compressed(os.path.join(args.out, "kurven.npz"), **kurven)
    # kurze Tabelle
    print("m  w2     gueltig  vE_max    r_bei   R_max   Schranke  vE/Schr  m/(R w)  vE(R_max) vE_tragend vE_mittel")
    for e in zeilen_aus:
        if e.get("vE_max") is None:
            print(f"{e['m']:<2} {e['w2']:.3f}  NEIN ({e['grund']})")
            continue
        print(f"{e['m']:<2} {e['w2']:.3f}  {'ja' if e['gueltig'] else 'NEIN'}      {e['vE_max']:.6f}  "
              f"{e['r_bei_vE_max']:7.3f} {e['R_max']:7.3f} {e['schranke']:.6f}  {e['vE_durch_schranke']:.4f}   "
              f"{e['schaetzung_m_durch_R_omega']:.4f}   {e['vE_bei_R_max']:.4f}    {e['vE_max_tragend']:.4f}     "
              f"{e['vE_mittel_energie']:.4f}")
    print(f"Dauer {time.perf_counter() - t0:.1f} s", flush=True)


if __name__ == "__main__":
    main()
