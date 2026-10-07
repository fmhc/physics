#!/usr/bin/env python3
"""RUNDE-35, Karte PEITSCHE-1, Teil A: zusammenfallende phi^4-Wand, radial in d = 2 und d = 3.

Plan, Messvorschriften und Urteilsregeln: ../PLAN.md (eingefroren). Explorativ (v3). Synthetische Rechnung,
keine Messdatenbestaetigung.

Modell: L = phi_t^2/2 - (grad phi)^2/2 - V, V = (phi^2 - 1)^2/4, also phi_tt = phi_rr + (d-1)/r phi_r - (phi^3 - phi).
Anfang: phi = tanh((r - R0)/sqrt 2), phi_t = 0 (innen -1, aussen +1).
Gitter: Zellmitten r_i = (i + 1/2) dr (i = 0..N-1), Flaechen r_f = (i + 1) dr, Zellmass W_i = (r_{i+1/2}^d - r_{i-1/2}^d)/d.
Halbdiskret hamiltonsch, daher ist
    E = Omega_d [ sum_i W_i (p_i^2/2 + V(phi_i)) + sum_f r_f^(d-1) (phi_{i+1} - phi_i)^2 / (2 dr) ]
eine exakte Erhaltungsgroesse der Ortsdiskretisierung. Bei r = 0 kein Fluss (regulaer, keine 1/r-Division),
bei r_max kein Fluss (reflektierend; r_max so gross, dass vor Laufende nichts in den Messbereich zurueckkommt).
Zeit: Yoshida/Forest-Ruth, 4. Ordnung, symplektisch, dt = cfl * dr.

Ausgaben (--out): zeitreihe.npz (alle Ausgabezeiten), zusammenfassung.json (Messgroessen nach PLAN.md), lauf.log.
Lange Laeufe: Zeitbudget --budget; bei Ueberschreitung Zwischenstand checkpoint.npz, Fortsetzung mit --fortsetzen.
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
import torch

torch.set_num_threads(1)

SQ2 = math.sqrt(2.0)
LEMNISKATE = 1.3110287771460599          # Int_0^1 dx / sqrt(1 - x^4)
_K = 2.0 ** (1.0 / 3.0)
_W1 = 1.0 / (2.0 - _K)
_W0 = -_K / (2.0 - _K)
C_DRIFT = (0.5 * _W1, 0.5 * (_W0 + _W1), 0.5 * (_W0 + _W1), 0.5 * _W1)
D_KICK = (_W1, _W0, _W1)

# Messvorschriften (PLAN.md, Abschnitt A.2)
R_LOKAL = 10.0              # Energie in r < 10
A4_FENSTER = 1.0            # Fenster [t_c - 1, t_c + 1] fuer die Musterschnelle
A3_R_MIN = 2.0              # groesste Wandschnelle fuer R >= 2
NACH_E_FENSTER = (490.0, 500.0)    # Mittel von E(r < 10) ueber t_c + 490 .. t_c + 500
NACH_F_FENSTER = (400.0, 500.0)    # Frequenz am Ursprung aus t_c + 400 .. t_c + 500
NACH_F_FRUEH = ((10.0, 110.0), (100.0, 200.0), (200.0, 300.0), (300.0, 400.0))   # beschreibend


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def tc_duenn(d, R0):
    return 0.5 * math.pi * R0 if d == 2 else LEMNISKATE * R0


def v_duenn(d, R, R0):
    x = R / R0
    return math.sqrt(max(0.0, 1.0 - x * x)) if d == 2 else math.sqrt(max(0.0, 1.0 - x ** 4))


class Gitter:
    def __init__(self, d, dr, rmax, geraet):
        self.d = d
        self.dr = dr
        self.N = int(math.ceil(rmax / dr))
        N = self.N
        i = np.arange(N, dtype=np.float64)
        rc = (i + 0.5) * dr
        rf_innen = i * dr                      # r_{i-1/2}
        rf_aussen = (i + 1.0) * dr             # r_{i+1/2}
        W = (rf_aussen ** d - rf_innen ** d) / d
        Af = rf_aussen[:-1] ** (d - 1)         # Flaechen zwischen Zelle i und i+1
        self.omega = 2.0 * math.pi if d == 2 else 4.0 * math.pi
        self.rc_np = rc
        dev = geraet
        self.rc = torch.tensor(rc, device=dev)
        self.W = torch.tensor(W, device=dev)
        self.invW = torch.tensor(1.0 / W, device=dev)
        self.Af_dr = torch.tensor(Af / dr, device=dev)        # Fluss = Af/dr * (phi_{i+1} - phi_i)
        self.Af_2dr = torch.tensor(Af / (2.0 * dr), device=dev)
        self.null1 = torch.zeros(1, device=dev, dtype=torch.float64)
        self.n_lok = int(np.sum(rc < R_LOKAL))
        self.n_lok_f = int(np.sum(rf_aussen[:-1] < R_LOKAL))
        self.idx = torch.arange(N, device=dev)

    def kraft(self, phi):
        fl = self.Af_dr * (phi[1:] - phi[:-1])
        div = torch.diff(torch.cat((self.null1, fl, self.null1)))
        return div * self.invW - phi * (phi * phi - 1.0)

    def schritt(self, phi, p, dt):
        phi.add_(p, alpha=C_DRIFT[0] * dt)
        p.add_(self.kraft(phi), alpha=D_KICK[0] * dt)
        phi.add_(p, alpha=C_DRIFT[1] * dt)
        p.add_(self.kraft(phi), alpha=D_KICK[1] * dt)
        phi.add_(p, alpha=C_DRIFT[2] * dt)
        p.add_(self.kraft(phi), alpha=D_KICK[2] * dt)
        phi.add_(p, alpha=C_DRIFT[3] * dt)

    def diagnose(self, phi, p):
        """Skalare je Ausgabezeit: E, E(r<10), max |T0r|/T00, Lage, phi_c, phi_0, R, v_inst, Index der Nullstelle."""
        dr = self.dr
        V = 0.25 * (phi * phi - 1.0) ** 2
        dphi = phi[1:] - phi[:-1]
        e_zelle = self.W * (0.5 * p * p + V)
        e_fl = self.Af_2dr * dphi * dphi
        E = self.omega * (e_zelle.sum() + e_fl.sum())
        E_lok = self.omega * (e_zelle[:self.n_lok].sum() + e_fl[:self.n_lok_f].sum())
        # zentrale Ableitung an den Zellmitten, Spiegel bei r = 0 (phi_{-1} = phi_0) und bei r_max (Neumann)
        phr = torch.empty_like(phi)
        phr[1:-1] = (phi[2:] - phi[:-2]) / (2.0 * dr)
        phr[0] = (phi[1] - phi[0]) / (2.0 * dr)
        phr[-1] = (phi[-1] - phi[-2]) / (2.0 * dr)
        T00 = 0.5 * p * p + 0.5 * phr * phr + V
        T0r = -p * phr
        ratio = torch.where(T00 > 0.0, T0r.abs() / torch.where(T00 > 0.0, T00, torch.ones_like(T00)),
                            torch.zeros_like(T00))
        imax = torch.argmax(ratio)
        # beschreibend: Verhaeltnis nur im energietragenden Bereich (T00 >= 1e-3 max T00) und energiegewichtetes Mittel
        wand = T00 >= 1e-3 * T00.max()
        ratio_wand = torch.max(torch.where(wand, ratio, torch.zeros_like(ratio)))
        v_mittel = (self.W * T0r.abs()).sum() / (self.W * T00).sum()
        phi_c = (9.0 * phi[0] - phi[1]) / 8.0
        # innerste Nullstelle (Vorzeichenwechsel - nach +, von innen gesucht)
        neg = phi < 0.0
        sc = neg[:-1] & (~neg[1:])
        N = self.N
        iz = torch.min(torch.where(sc, self.idx[:-1], torch.full_like(self.idx[:-1], N)))
        izc = torch.clamp(iz, max=N - 2).view(1)
        izc1 = izc + 1
        im = imax.view(1)

        def nimm(x, i):          # index_select statt x[tensor]: ohne Host-Synchronisation (CUDA-Graph-tauglich)
            return x.index_select(0, i).view(())

        f0 = nimm(phi, izc)
        f1 = nimm(phi, izc1)
        p0 = nimm(p, izc)
        p1 = nimm(p, izc1)
        fr = -f0 / (f1 - f0)
        R = nimm(self.rc, izc) + dr * fr
        pt = p0 + (p1 - p0) * fr
        v_inst = -pt / ((f1 - f0) / dr)
        werte = torch.stack((E, E_lok, nimm(ratio, im), nimm(self.rc, im), phi_c, phi[0], R, v_inst,
                             iz.to(torch.float64), nimm(T0r, im), nimm(T00, im), ratio_wand, v_mittel))
        return werte


SPALTEN = ("E", "E_lok", "ratio_max", "r_ratio_max", "phi_c", "phi_0", "R_roh", "v_inst_roh", "iz", "T0r_bei_max",
           "T00_bei_max", "ratio_wand", "v_mittel")


def zusammenfassen(meta, t, Z):
    """Messgroessen nach PLAN.md Abschnitt A.2 aus der Zeitreihe."""
    d, R0 = meta["d"], meta["R0"]
    N = meta["N"]
    col = {k: Z[:, j] for j, k in enumerate(SPALTEN)}
    phi_c = col["phi_c"]
    phi_0 = col["phi_0"]
    # R_k: innen (phi_0 < 0) und Nullstelle vorhanden -> R_roh; phi_0 >= 0 -> 0; sonst NaN
    R = np.where(phi_0 >= 0.0, 0.0, np.where(col["iz"] < N, col["R_roh"], np.nan))
    v_inst = np.where((phi_0 < 0.0) & (col["iz"] < N), col["v_inst_roh"], np.nan)
    E0 = float(col["E"][0])
    aus = dict(E0=E0, E_duenn=(2.0 * math.pi * 2.0 * SQ2 / 3.0 * R0) if d == 2 else
               (4.0 * math.pi * 2.0 * SQ2 / 3.0 * R0 * R0), tc_duenn=tc_duenn(d, R0))
    # t_c: erstes phi_c >= 0 nach phi_c < 0
    k_c = None
    for k in range(1, t.size):
        if phi_c[k - 1] < 0.0 <= phi_c[k]:
            k_c = k
            break
    if k_c is None:
        aus["t_c"] = None
        aus["grund"] = "phi_c erreicht 0 nicht bis Laufende"
        return aus, R, v_inst
    tc = float(t[k_c - 1] + (t[k_c] - t[k_c - 1]) * (-phi_c[k_c - 1]) / (phi_c[k_c] - phi_c[k_c - 1]))
    aus["t_c"] = tc
    aus["t_c_rel_abw"] = tc / aus["tc_duenn"] - 1.0
    # Wandschnelle (zentrale Differenz, einwaerts positiv) fuer k mit t_{k+1} < t_c und R_{k-1}, R_k, R_{k+1} > 0
    v = np.full(t.size, np.nan)
    for k in range(1, t.size - 1):
        if t[k + 1] < tc and R[k - 1] > 0.0 and R[k] > 0.0 and R[k + 1] > 0.0:
            v[k] = -(R[k + 1] - R[k - 1]) / (t[k + 1] - t[k - 1])
    # v bei R0/2, R0/4, R0/10 (erstes Unterschreiten vor t_c, linear in R interpoliert)
    vR = {}
    for name, frac in (("R0/2", 0.5), ("R0/4", 0.25), ("R0/10", 0.1)):
        Rz = frac * R0
        wert = None
        for k in range(2, t.size - 1):
            if t[k + 1] >= tc:
                break
            if R[k - 1] > Rz >= R[k] and np.isfinite(v[k - 1]) and np.isfinite(v[k]):
                wert = float(v[k - 1] + (v[k] - v[k - 1]) * (Rz - R[k - 1]) / (R[k] - R[k - 1]))
                break
        soll = v_duenn(d, Rz, R0)
        vR[name] = dict(R=Rz, v=wert, v_duenn=soll, rel_abw=(wert / soll - 1.0) if wert is not None else None,
                        dr_soll_d2=SQ2 * Rz / (5.0 * R0), dr_soll_d3=SQ2 * (Rz / R0) ** 2 / 5.0)
    aus["v_bei_R"] = vR
    # groesste Wandschnelle fuer R >= 2 (alle drei Stuetzstellen >= 2) vor t_c
    ok = np.zeros(t.size, bool)
    for k in range(1, t.size - 1):
        ok[k] = np.isfinite(v[k]) and min(R[k - 1], R[k], R[k + 1]) >= A3_R_MIN
    if ok.any():
        kk = int(np.nanargmax(np.where(ok, v, -np.inf)))
        aus["v_max_R_ab_2"] = dict(v=float(v[kk]), R=float(R[kk]), t=float(t[kk]),
                                   v_duenn=v_duenn(d, float(R[kk]), R0))
    else:
        aus["v_max_R_ab_2"] = None
    vv = np.where(np.isfinite(v), v, -np.inf)
    kk = int(np.argmax(vv))
    aus["v_max_vor_tc"] = dict(v=float(v[kk]), R=float(R[kk]), t=float(t[kk])) if np.isfinite(v[kk]) else None
    # Musterschnelle: |R_{k+1} - R_k| / (t_{k+1} - t_k) fuer Paare im Fenster [t_c - 1, t_c + 1]
    best = None
    for k in range(t.size - 1):
        if t[k] >= tc - A4_FENSTER and t[k + 1] <= tc + A4_FENSTER and np.isfinite(R[k]) and np.isfinite(R[k + 1]):
            s = abs(R[k + 1] - R[k]) / (t[k + 1] - t[k])
            if best is None or s > best["s"]:
                best = dict(s=float(s), t0=float(t[k]), t1=float(t[k + 1]), R0_paar=float(R[k]), R1_paar=float(R[k + 1]))
    aus["musterschnelle"] = best
    inst = [(abs(v_inst[k]), k) for k in range(t.size) if tc - A4_FENSTER <= t[k] <= tc + A4_FENSTER
            and np.isfinite(v_inst[k])]
    if inst:
        s, k = max(inst)
        aus["v_inst_max_fenster"] = dict(v=float(s), t=float(t[k]), R=float(R[k]))
    else:
        aus["v_inst_max_fenster"] = None
    # A0: Energie bis t_c, Verhaeltnis ueberall und jederzeit (an allen Ausgabezeiten)
    E = col["E"]
    bis = t <= tc
    aus["E_fehler_bis_tc"] = float(np.max(np.abs(E[bis] / E0 - 1.0)))
    aus["E_fehler_gesamt"] = float(np.max(np.abs(E / E0 - 1.0)))
    aus["ratio_max_jederzeit"] = float(np.max(col["ratio_max"]))
    kr = int(np.argmax(col["ratio_max"]))
    aus["ratio_max_ort"] = dict(t=float(t[kr]), r=float(col["r_ratio_max"][kr]), T0r=float(col["T0r_bei_max"][kr]),
                                T00=float(col["T00_bei_max"][kr]))
    # beschreibend: Energiefluss-Geschwindigkeit im energietragenden Bereich und energiegewichtet, bis t_c
    rw = col["ratio_wand"]
    vm = col["v_mittel"]
    kw = int(np.argmax(np.where(bis, rw, -1.0)))
    aus["ratio_wand_max_bis_tc"] = dict(wert=float(rw[kw]), t=float(t[kw]), R=float(R[kw]))
    km = int(np.argmax(np.where(bis, vm, -1.0)))
    aus["v_mittel_max_bis_tc"] = dict(wert=float(vm[km]), t=float(t[km]), R=float(R[km]))
    for name, eintrag in aus["v_bei_R"].items():
        Rz = eintrag["R"]
        kz = [k for k in range(1, t.size) if t[k] < tc and R[k - 1] > Rz >= R[k]]
        eintrag["ratio_wand"] = float(rw[kz[0]]) if kz else None
        eintrag["v_mittel"] = float(vm[kz[0]]) if kz else None
    # Nachlauf (nur wenn die Zeitreihe bis t_c + 500 reicht)
    if t[-1] >= tc + NACH_E_FENSTER[1] - 1e-9:
        sel = (t >= tc + NACH_E_FENSTER[0]) & (t <= tc + NACH_E_FENSTER[1])
        aus["nach_E_lok_anteil"] = float(np.mean(col["E_lok"][sel]) / E0)
        aus["nach_E_lok_max_anteil_ab_tc_plus_100"] = float(np.max(col["E_lok"][t >= tc + 100.0]) / E0)
        aus["nach_frequenz"] = frequenz(t, phi_c, tc + NACH_F_FENSTER[0], tc + NACH_F_FENSTER[1])
        aus["nach_frequenz_frueh"] = [frequenz(t, phi_c, tc + a, tc + b) for a, b in NACH_F_FRUEH]
    else:
        aus["nach_E_lok_anteil"] = None
        aus["nach_frequenz"] = None
    # Zeitpunkte, an denen der Ursprung wieder innen liegt (Rueckprall), beschreibend
    nach = t > tc
    rueck = np.nonzero(nach & (phi_c < 0.0))[0]
    aus["rueckprall_erste_zeit"] = float(t[rueck[0]]) if rueck.size else None
    aus["phi_c_max_nach_tc"] = float(np.max(phi_c[nach])) if nach.any() else None
    return aus, R, v_inst


def frequenz(t, x, ta, tb):
    sel = (t >= ta) & (t <= tb)
    if sel.sum() < 64:
        return None
    tt = t[sel]
    y = x[sel] - np.mean(x[sel])
    dt = float(np.mean(np.diff(tt)))
    n = y.size
    w = np.hanning(n)
    nfft = 8 * int(2 ** math.ceil(math.log2(n)))
    Y = np.abs(np.fft.rfft(y * w, nfft))
    om = 2.0 * math.pi * np.fft.rfftfreq(nfft, d=dt)
    Y[0] = 0.0
    k = int(np.argmax(Y))
    omk = float(om[k])
    if 0 < k < Y.size - 1:
        a, b, c = Y[k - 1], Y[k], Y[k + 1]
        den = a - 2.0 * b + c
        if den < 0.0:
            omk = float(om[k] + 0.5 * (a - c) / den * (om[1] - om[0]))
    return dict(von=float(ta), bis=float(tb), omega_peak=omk, mittel=float(np.mean(x[sel])),
                amplitude=float(0.5 * (np.max(x[sel]) - np.min(x[sel]))), aufloesung=float(2.0 * math.pi / (tt[-1] - tt[0])))


def main():
    ap = argparse.ArgumentParser(description="PEITSCHE-1 Teil A: radiale phi^4-Wand")
    ap.add_argument("--d", type=int, required=True)
    ap.add_argument("--R0", type=float, required=True)
    ap.add_argument("--dr", type=float, required=True)
    ap.add_argument("--cfl", type=float, default=0.4)
    ap.add_argument("--nach", type=float, default=10.0, help="Laufende = t_c(duenn) + nach")
    ap.add_argument("--dtaus", type=float, default=0.02)
    ap.add_argument("--rmax", type=float, default=None)
    ap.add_argument("--out", required=True)
    ap.add_argument("--budget", type=float, default=480.0, help="Sekunden bis zum Zwischenstand")
    ap.add_argument("--fortsetzen", action="store_true")
    ap.add_argument("--geraet", default="auto")
    ap.add_argument("--graph", type=int, default=1, help="1: CUDA-Graph je Ausgabeblock (nur auf cuda)")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    logf = open(os.path.join(args.out, "lauf.log"), "a")

    def log(s):
        print(s, flush=True)
        logf.write(s + "\n")
        logf.flush()

    geraet = ("cuda" if torch.cuda.is_available() else "cpu") if args.geraet == "auto" else args.geraet
    d, R0, dr = args.d, args.R0, args.dr
    dt = args.cfl * dr
    t_end = tc_duenn(d, R0) + args.nach
    rmax = args.rmax if args.rmax else max(R0 + 0.5 * t_end, 0.5 * (t_end + R0 + R_LOKAL)) + 20.0
    n_aus = max(1, int(round(args.dtaus / dt)))
    n_ges = int(math.ceil(t_end / dt / n_aus)) * n_aus
    G = Gitter(d, dr, rmax, geraet)
    meta = dict(d=d, R0=R0, dr=dr, cfl=args.cfl, dt=dt, t_end=n_ges * dt, rmax=G.N * dr, N=G.N, n_aus=n_aus,
                dt_aus=n_aus * dt, geraet=geraet, integrator="Yoshida/Forest-Ruth 4. Ordnung",
                torch=torch.__version__, numpy=np.__version__, python=platform.python_version(), host=platform.node(),
                gpu=(torch.cuda.get_device_name(0) if geraet == "cuda" else None), nach=args.nach)
    ck = os.path.join(args.out, "checkpoint.npz")
    t0 = time.perf_counter()
    if args.fortsetzen and os.path.exists(ck):
        C = np.load(ck, allow_pickle=False)
        phi = torch.tensor(C["phi"], device=geraet)
        p = torch.tensor(C["p"], device=geraet)
        schritt = int(C["schritt"])
        T = list(C["t"])
        ZZ = [row for row in C["Z"]]
        log(f"Fortsetzung {jetzt()} bei Schritt {schritt} von {n_ges}, t = {schritt * dt:.4f}")
    else:
        phi = torch.tanh((G.rc - R0) / SQ2)
        p = torch.zeros_like(phi)
        schritt = 0
        T = [0.0]
        ZZ = [G.diagnose(phi, p).cpu().numpy()]
        log(f"Start {jetzt()} {json.dumps(meta, ensure_ascii=False)}")

    def block_direkt():
        for _ in range(n_aus):
            G.schritt(phi, p, dt)
        return G.diagnose(phi, p)

    graph_an = geraet == "cuda" and args.graph == 1
    if graph_an:
        # CUDA-Graph: n_aus Schritte plus Diagnose als ein Graph (nur Startkosten; Rechnung identisch)
        phi_s, p_s = phi.clone(), p.clone()
        strom = torch.cuda.Stream()
        strom.wait_stream(torch.cuda.current_stream())
        with torch.cuda.stream(strom):
            for _ in range(2):
                block_direkt()
        torch.cuda.current_stream().wait_stream(strom)
        phi.copy_(phi_s)
        p.copy_(p_s)
        del phi_s, p_s
        graph = torch.cuda.CUDAGraph()
        with torch.cuda.graph(graph):
            res_fest = block_direkt()

        def block():
            graph.replay()
            return res_fest
    else:
        block = block_direkt
    meta["cuda_graph"] = graph_an
    PUFFER = 200
    puf = torch.empty((PUFFER, len(SPALTEN)), dtype=torch.float64, device=geraet)
    nb = 0
    fertig = False
    leerungen = 0
    while schritt < n_ges:
        res = block()
        puf[nb].copy_(res)
        nb += 1
        schritt += n_aus
        T.append(schritt * dt)
        if nb == PUFFER or schritt >= n_ges:
            ZZ.extend(list(puf[:nb].cpu().numpy()))
            nb = 0
            leerungen += 1
            if leerungen % 10 == 0:
                z = ZZ[-1]
                log(f"  t = {T[-1]:9.4f}  E/E0-1 = {z[0] / ZZ[0][0] - 1.0:+.2e}  R = {z[6]:.4f}  phi_c = {z[4]:+.4f}  "
                    f"ratio_max = {z[2]:.6f}  ratio_wand = {z[11]:.6f}  {time.perf_counter() - t0:.1f} s")
            if time.perf_counter() - t0 > args.budget and schritt < n_ges:
                np.savez(ck, phi=phi.cpu().numpy(), p=p.cpu().numpy(), schritt=schritt, t=np.array(T),
                         Z=np.array(ZZ))
                log(f"Zwischenstand {jetzt()} bei Schritt {schritt} von {n_ges} (t = {schritt * dt:.4f}), "
                    f"{time.perf_counter() - t0:.1f} s; weiter mit --fortsetzen")
                break
    else:
        fertig = True
    if not fertig:
        logf.close()
        return
    t = np.array(T)
    Z = np.array(ZZ)
    aus, R, v_inst = zusammenfassen(meta, t, Z)
    np.savez_compressed(os.path.join(args.out, "zeitreihe.npz"), t=t, Z=Z, spalten=np.array(SPALTEN), R=R,
                        v_inst=v_inst)
    erg = dict(karte="PEITSCHE-1 Teil A", ende=jetzt(), meta=meta, rechenzeit_s_letzter_abschnitt=time.perf_counter() - t0,
               messung=aus)
    with open(os.path.join(args.out, "zusammenfassung.json"), "w") as fh:
        json.dump(erg, fh, indent=1, ensure_ascii=False)
    if os.path.exists(ck):
        os.replace(ck, ck + ".erledigt")
    log(f"Ende {jetzt()} {time.perf_counter() - t0:.1f} s")
    log(json.dumps(aus, ensure_ascii=False, indent=1))
    logf.close()


if __name__ == "__main__":
    main()
