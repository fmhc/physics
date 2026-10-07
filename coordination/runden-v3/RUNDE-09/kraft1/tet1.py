#!/usr/bin/env python3
"""TET-1 (KRAFT-1, Runde 9, 2026-09-30): statische Wechselwirkungsenergie von vier Q-Baellen als Ueberlagerung der
Profile. Drei Baelle auf einem gleichseitigen Dreieck (Kante d, Phasen 0/120/240 Grad oder 0/0/0 als Gegenprobe), der
vierte an der Spitze des regulaeren Tetraeders mit Phase phi. E_int(phi) fuer n_phi Werte, Harmonische in phi.
Plan und Vorab-Kriterien: PLAN.md Abschnitt 5 (im selben Ordner).

- Profil f(r) und f'(r) aus kraft12.profil() (Kopie von KOLL-1, Schiessen, Schwanz A e^{-k0 r}/r).
- Energie E = Int (omega^2 |Phi|^2 + |grad Phi|^2 + U(|Phi|^2)), dazu F = E - omega Q = Int (-omega^2 |Phi|^2 + ...).
  E_int = E[Ueberlagerung] - Summe E[einzeln], die Einzelbaelle auf demselben Gitter.
- Quadratur: Zylinderkoordinaten um die C3-Achse (Spitze auf der Achse). Radius und Hoehe Mittelpunktregel,
  Azimut gleichabstaendig mit N_alpha durch 3 teilbar: die C3-Drehung bildet das Gitter exakt auf sich ab.
- Paaranteil der dritten Harmonischen: c3_paar = 2 beta Summe_k Int f_a^3 f_k^3 (PLAN Abschnitt 5).
Aufruf: python tet1.py --geraet cuda|cpu --abstaende 8,10,12,14 --h 0.08 --na 384 --out ORDNER
"""
import argparse
import datetime
import json
import math
import os
import sys
import time

import numpy as np
import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kraft12 as k12  # noqa: E402

F64 = torch.float64
C128 = torch.complex128
PI = math.pi
BETA = 0.5


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def upot(S):
    return S - S * S + BETA * S ** 3


def rechnen(d, prof, a, dev, log):
    w = prof["w"]
    w2 = w * w
    tab_r = prof["r"]
    Rt = d / math.sqrt(3.0)
    Hs = d * math.sqrt(2.0 / 3.0)
    ecken = [(Rt * math.cos(2 * PI * k / 3), Rt * math.sin(2 * PI * k / 3), 0.0) for k in range(3)]
    spitze = (0.0, 0.0, Hs)
    h = a.h
    nr = int(math.ceil((Rt + a.rand) / h))
    z0, z1 = -a.rand, Hs + a.rand
    nz = int(math.ceil((z1 - z0) / h))
    na = a.na
    assert na % 3 == 0
    rho = (torch.arange(nr, dtype=F64, device=dev) + 0.5) * h
    al = (torch.arange(na, dtype=F64, device=dev) + 0.5) * (2 * PI / na)
    zz = z0 + (torch.arange(nz, dtype=F64, device=dev) + 0.5) * h
    dA = 2 * PI / na
    P, Al = torch.meshgrid(rho, al, indexing="ij")
    X2, Y2 = P * torch.cos(Al), P * torch.sin(Al)
    vol2 = (P * h * dA * h)                                     # [nr, na]
    phis = [2 * PI * j / a.nphi for j in range(a.nphi)]
    saetze = {"neutral": [0.0, 2 * PI / 3, 4 * PI / 3], "gleich": [0.0, 0.0, 0.0]}
    E = {s: np.zeros(a.nphi) for s in saetze}
    Fr = {s: np.zeros(a.nphi) for s in saetze}
    Q = {s: np.zeros(a.nphi) for s in saetze}
    E1 = np.zeros(4)
    F1 = np.zeros(4)
    J33 = np.zeros(3)
    J11 = np.zeros(3)
    t0 = time.perf_counter()
    for kb in range(0, nz, a.block):
        Z = zz[kb:kb + a.block]
        nb = Z.numel()
        X = X2[..., None].expand(nr, na, nb)
        Y = Y2[..., None].expand(nr, na, nb)
        ZZ = Z.view(1, 1, nb).expand(nr, na, nb)
        vol = vol2[..., None]
        felder = []
        for (cx, cy, cz) in ecken + [spitze]:
            dx, dy, dz = X - cx, Y - cy, ZZ - cz
            r = torch.sqrt(dx * dx + dy * dy + dz * dz).clamp(min=1e-12)
            f = k12.tabelle_2d(tab_r, prof["f"], r)
            g = k12.tabelle_2d(tab_r, prof["g"], r) / r
            felder.append((f, g * dx, g * dy, g * dz))
        for i, (f, gx, gy, gz) in enumerate(felder):
            S = f * f
            dens = gx * gx + gy * gy + gz * gz + upot(S)
            E1[i] += float(((w2 * S + dens) * vol).sum())
            F1[i] += float(((-w2 * S + dens) * vol).sum())
        fa = felder[3][0]
        for k in range(3):
            J33[k] += float((fa ** 3 * felder[k][0] ** 3 * vol).sum())
            J11[k] += float((fa * felder[k][0] * vol).sum())
        for s, th in saetze.items():
            T = torch.zeros(nr, na, nb, dtype=C128, device=dev)
            Tg = [torch.zeros_like(T) for _ in range(3)]
            for k in range(3):
                e = complex(math.cos(th[k]), math.sin(th[k]))
                f, gx, gy, gz = felder[k]
                T = T + e * f
                Tg[0] = Tg[0] + e * gx
                Tg[1] = Tg[1] + e * gy
                Tg[2] = Tg[2] + e * gz
            fa, gax, gay, gaz = felder[3]
            for j, ph in enumerate(phis):
                e = complex(math.cos(ph), math.sin(ph))
                Ph = T + e * fa
                S = Ph.real ** 2 + Ph.imag ** 2
                G2 = torch.zeros_like(S)
                for c, gc in zip(range(3), (gax, gay, gaz)):
                    q = Tg[c] + e * gc
                    G2 = G2 + q.real ** 2 + q.imag ** 2
                dens = G2 + upot(S)
                E[s][j] += float(((w2 * S + dens) * vol).sum())
                Fr[s][j] += float(((-w2 * S + dens) * vol).sum())
                Q[s][j] += float((2 * w * S * vol).sum())
    dauer = time.perf_counter() - t0
    E1s, F1s = float(E1.sum()), float(F1.sum())
    ergebnis = dict(d=d, h=h, na=na, nr=nr, nz=nz, punkte=nr * na * nz, dauer_s=dauer, E_einzeln=E1.tolist(),
                    F_einzeln=F1.tolist(), J33=J33.tolist(), J11=J11.tolist(), phis=phis)
    for s in saetze:
        for name, arr, ref in (("E", E[s], E1s), ("F", Fr[s], F1s)):
            Ei = arr - ref
            harm = {}
            for m in range(0, a.nphi // 2 + 1):
                c = float(np.sum(Ei * np.cos(m * np.array(phis)))) * (1.0 if m in (0, a.nphi // 2) else 2.0) / a.nphi
                sn = float(np.sum(Ei * np.sin(m * np.array(phis)))) * 2.0 / a.nphi
                harm[m] = (c, sn)
            ergebnis[f"{s}_{name}"] = dict(E_int=Ei.tolist(), harm={str(m): v for m, v in harm.items()})
        ergebnis[f"{s}_Q"] = Q[s].tolist()
    ergebnis["c3_paar"] = 2 * BETA * float(J33.sum())
    log(f"  d = {d:g}: Gitter nr {nr} x na {na} x nz {nz} = {nr * na * nz / 1e6:.1f} Mio Punkte, {dauer:.1f} s; "
        f"Einzelbaelle E = {E1.round(5).tolist()} (Streuung {E1.max() - E1.min():.2e}); J33 = {J33[0]:.4e}, "
        f"c3_paar = 2 beta Sum J33 = {ergebnis['c3_paar']:.4e}")
    for s in saetze:
        hE = ergebnis[f"{s}_E"]["harm"]
        hF = ergebnis[f"{s}_F"]["harm"]
        log(f"    {s:7s} E: c0 {hE['0'][0]:+.6e} | c1 {hE['1'][0]:+.3e} (s1 {hE['1'][1]:+.1e}) | c2 {hE['2'][0]:+.3e} "
            f"(s2 {hE['2'][1]:+.1e}) | c3 {hE['3'][0]:+.6e} (s3 {hE['3'][1]:+.1e}) | c4 {hE['4'][0]:+.2e} | "
            f"c6 {hE['6'][0]:+.2e}")
        log(f"    {s:7s} F: c0 {hF['0'][0]:+.6e} | c1 {hF['1'][0]:+.3e} | c2 {hF['2'][0]:+.3e} | c3 {hF['3'][0]:+.6e}")
    return ergebnis


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--geraet", default="cuda")
    p.add_argument("--w2", type=float, default=0.76)
    p.add_argument("--abstaende", default="8,10,12,14")
    p.add_argument("--h", type=float, default=0.08)
    p.add_argument("--na", type=int, default=384)
    p.add_argument("--rand", type=float, default=12.0)
    p.add_argument("--nphi", type=int, default=12)
    p.add_argument("--block", type=int, default=16)
    p.add_argument("--profil-h", type=float, default=0.002)
    p.add_argument("--profil-rmax", type=float, default=36.0)
    p.add_argument("--out", default="aus-tet1")
    a = p.parse_args()
    torch.set_num_threads(1)
    dev = torch.device("cuda" if a.geraet == "cuda" and torch.cuda.is_available() else "cpu")
    if a.geraet == "cuda" and dev.type != "cuda":
        raise SystemExit("--geraet cuda, aber keine CUDA-Karte sichtbar: Abbruch (kein stiller CPU-Ausweg).")
    os.makedirs(a.out, exist_ok=True)
    log = k12.Log(os.path.join(a.out, "bericht.txt"))
    log(f"TET-1 Start {jetzt()}, Geraet {dev}" + (f" ({torch.cuda.get_device_name(dev)})" if dev.type == "cuda" else "")
        + f", torch {torch.__version__}")
    log("  Argumente: " + json.dumps(vars(a)))
    k12.PROFIL_H, k12.PROFIL_RMAX = a.profil_h, a.profil_rmax
    prof = k12.profil(a.w2, log=log)
    log(f"  k0 = {prof['k0']:.6f}, A = {prof['A']:.6f}, E_Ball = {prof['E']:.6f}")
    alle = dict(w2=a.w2, k0=prof["k0"], A=prof["A"], E_Ball=prof["E"], args=vars(a), laeufe=[])
    for d in [float(x) for x in a.abstaende.split(",") if x]:
        alle["laeufe"].append(rechnen(d, prof, a, dev, log))
        with open(os.path.join(a.out, "tet1.json"), "w") as fh:
            json.dump(alle, fh, indent=1)
    # Steigungen zwischen Nachbarabstaenden
    L = alle["laeufe"]
    k0 = prof["k0"]
    zeilen = []
    for x, y in zip(L[:-1], L[1:]):
        d1, d2 = x["d"], y["d"]
        z = dict(d1=d1, d2=d2)
        for s, m in (("neutral", 3), ("gleich", 1)):
            c1_, c2_ = x[f"{s}_E"]["harm"][str(m)][0], y[f"{s}_E"]["harm"][str(m)][0]
            z[f"{s}_c{m}"] = (c1_, c2_)
            z[f"{s}_steigung_k0"] = (-math.log(abs(c2_) / abs(c1_)) / (d2 - d1) / k0) if c1_ * c2_ > 0 else float("nan")
        c1p, c2p = x["c3_paar"], y["c3_paar"]
        z["paar_steigung_k0"] = -math.log(c2p / c1p) / (d2 - d1) / k0
        z["vorh_neutral_k0"] = 3.0 + 3.0 * math.log(d2 / d1) / (d2 - d1) / k0
        z["vorh_gleich_k0"] = 1.0 + math.log(d2 / d1) / (d2 - d1) / k0
        zeilen.append(z)
        log(f"  Steigung {d1:g}-{d2:g}: neutral c3 {z['neutral_steigung_k0']:.3f} k0 (eigene Vorhersage "
            f"{z['vorh_neutral_k0']:.3f}, Fenster der Leitung 2,5 bis 3,5), Paaranteil {z['paar_steigung_k0']:.3f} k0; "
            f"0/0/0 c1 {z['gleich_steigung_k0']:.3f} k0 (Vorhersage {z['vorh_gleich_k0']:.3f})")
    for x in L:
        c3 = x["neutral_E"]["harm"]["3"][0]
        log(f"  d = {x['d']:g}: c3 voll / c3_paar = {c3 / x['c3_paar']:.4f}; |c1|, |c2| neutral = "
            f"{abs(x['neutral_E']['harm']['1'][0]):.1e}, {abs(x['neutral_E']['harm']['2'][0]):.1e} bei |c0| "
            f"{abs(x['neutral_E']['harm']['0'][0]):.3e}")
    alle["steigungen"] = zeilen
    alle["ende"] = jetzt()
    with open(os.path.join(a.out, "tet1.json"), "w") as fh:
        json.dump(alle, fh, indent=1)
    log(f"Ende {jetzt()}")


if __name__ == "__main__":
    main()
