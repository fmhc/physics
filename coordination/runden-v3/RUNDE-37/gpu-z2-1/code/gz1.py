#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GPU-Z2-1 (Runde 49, RUNDE-37/gpu-z2-1): GPU-Fassung (torch, FP64) der Spin-Schwellenrechnung aus Z2-SCHUTZ-2.

Synthetische Modellrechnung an einem Modellfeld (Einheitsquaternion-Feld, Energie 4(1 - c^2) je Bindung, Finns
Diamant-Netz); keine Messdaten.
Netz: finn.Netz (CPU, unveraendert kopiert). Auf der GPU: Energie, Gradient, FIRE (Quaternion und ebene Darstellung psi),
Bisektion (Port von z2s2.modus_bisekt, gleiche Regeln und Parameter), CI-NEB (Port von z2.wegrechnung, Bilder in einem
Tensor gebuendelt; hier in der ebenen Darstellung psi, ohne Rauschen aus der Ebene).
Nachbarsummen ohne Atomics: je freiem Knoten die vier Bindungsenden (Indexliste eidx), Gradient = Summe der Beitraege.

Modi:
  pruef   GPU gegen CPU: Energie und Gradient an Zufallszustaenden (Quaternion und psi), E_S aus der CPU-npz,
          Zeit je Gradient (GPU, Median; CPU, Median) in derselben Unit.
  start   Startzustand S (FIRE bis Knotenkraft 1e-7 ab dem harmonischen Profil; --darst quat wie z2s2, oder psi).
  bisekt  Verfahren A: Port von z2s2.modus_bisekt (Stufen 1, 2, 3, 3b; Klassen T, S, M, offen; Freigabe).
  weg     Verfahren B: CI-NEB in psi auf dem Weg aus der Bisektion (Port von z2.wegrechnung, verfahren neb).
Aufruf nur ueber kleintest.sh auf der .69 (Spuren p4000a, p4000b).
"""
import argparse
import hashlib
import math
import os
import resource
import sys
import time

import numpy as np
import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import finn  # noqa: E402  (unveraendert)
import guertel2 as g2  # noqa: E402  (unveraendert)
import z2  # noqa: E402  (unveraendert)
import z2s2  # noqa: E402  (unveraendert)

T_START = time.time()
START_UTC = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
DEV = torch.device("cuda")
DT = torch.float64
PI = math.pi


def sha_datei(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def kopf(args):
    frei, ges = torch.cuda.mem_get_info()
    return {"karte": "GPU-Z2-1 (Runde 49)", "modus": args.modus, "args": vars(args),
            "code_sha256": sha_datei(os.path.abspath(__file__)),
            "z2s2_sha256": sha_datei(os.path.abspath(z2s2.__file__)),
            "z2_sha256": sha_datei(os.path.abspath(z2.__file__)),
            "finn_sha256": sha_datei(os.path.abspath(finn.__file__)),
            "start_utc": START_UTC, "schreibzeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "numpy": np.__version__, "torch": torch.__version__, "geraet": torch.cuda.get_device_name(0),
            "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES"),
            "gpu_speicher_frei_mib_jetzt": frei / 2**20, "gpu_speicher_gesamt_mib": ges / 2**20,
            "gpu_speicher_spitze_mib": torch.cuda.max_memory_allocated() / 2**20}


def maxrss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def gtag(r0, R):
    return "r%g-R%g" % (r0, R)


def wand():
    return time.time() - T_START


def sync():
    torch.cuda.synchronize()


# ---------------------------------------------------------------- Netz auf der GPU

class GNetz:
    def __init__(self, r0, R, ch=2):
        t0 = time.time()
        self.netz = finn.Netz("diamant", r0, R, "so3")
        nz = self.netz
        self.t_netz_cpu = time.time() - t0
        self.N, self.nbond, self.ch = int(nz.N), int(nz.nbond), int(ch)
        self.a = torch.as_tensor(nz.a, dtype=torch.int64, device=DEV)
        self.b = torch.as_tensor(nz.b, dtype=torch.int64, device=DEV)
        self.frei = torch.as_tensor(nz.frei, device=DEV)
        self.frei_f = self.frei.to(DT)
        self.fi = torch.nonzero(self.frei).squeeze(1)
        self.Nf = int(self.fi.numel())
        ende = torch.cat([self.a, self.b])
        o = torch.sort(ende, stable=True).indices
        cnt = torch.bincount(ende, minlength=self.N)
        anf = torch.cumsum(cnt, 0) - cnt
        if not bool((cnt[self.fi] == 4).all()):
            raise SystemExit("freier Knoten ohne Grad 4")
        self.eidx = o[anf[self.fi][:, None] + torch.arange(4, device=DEV)[None]].contiguous()
        del ende, o, cnt, anf
        sync()
        self.t_netz = time.time() - t0

    # ebene Darstellung psi: c_b = cos(psi_a - psi_b), E = sum 4 sin^2, dE/dpsi_a = sum 8 sin cos (z2s2.Eben)
    def psi_eg(self, P, grad=True):
        """P (B, N) -> E (B,), G (B, N) (0 an festen Knoten), cmin (B,)."""
        B = P.shape[0]
        E = torch.empty(B, dtype=DT, device=DEV)
        cmin = torch.empty(B, dtype=DT, device=DEV)
        G = torch.zeros_like(P) if grad else None
        for s in range(0, B, self.ch):
            Ps = P[s:s + self.ch]
            d = Ps[:, self.a] - Ps[:, self.b]
            sd = torch.sin(d)
            cd = torch.cos(d)
            E[s:s + self.ch] = 4.0 * (sd * sd).sum(1)
            cmin[s:s + self.ch] = cd.min(1).values
            if grad:
                g = 8.0 * sd * cd
                del sd, cd, d
                gg = torch.cat([g, -g], 1)
                del g
                G[s:s + self.ch, self.fi] = gg[:, self.eidx].sum(2)
                del gg
        return E, G, cmin

    # Quaternion (finn.Netz.energie fuer B = 1, Feld so3)
    def q_eg(self, X, grad=True):
        xa = X[self.a]
        xb = X[self.b]
        c = (xa * xb).sum(1)
        E = (4.0 * (1.0 - c * c)).sum()
        mon = c.min()
        if not grad:
            return E, None, mon
        f = (-8.0 * c)[:, None]
        gg = torch.cat([f * xb, f * xa], 0)
        del xa, xb, f
        G = torch.zeros_like(X)
        G[self.fi] = gg[self.eidx].sum(1)
        return E, G, mon

    def q_tang(self, G, X):
        G = G - (G * X).sum(1, keepdim=True) * X
        return G * self.frei_f[:, None]


# ---------------------------------------------------------------- FIRE (Arithmetik wie finn.fire_feld, B = 1)

def fire_q(gn, x, nmax, ftol, dtmax, dtstart=0.02, capw=0.05):
    """Port von finn.fire_feld fuer B = 1 (Quaternion). Ein Abgleich mit dem Wirt je Schritt."""
    E, G, mon = gn.q_eg(x)
    F = -gn.q_tang(G, x)
    v = torch.zeros_like(x)
    dt, alpha, npos = dtstart, 0.1, 0
    st = torch.stack([(F * F).sum(1).max(), E, mon]).tolist()
    fmax, Ev, monv = math.sqrt(st[0]), st[1], st[2]
    mon_lauf = monv
    Pw, vv, FF = 0.0, 0.0, float((F * F).sum())
    it = 0
    for it in range(nmax):
        if not fmax > ftol:
            break
        vn = math.sqrt(vv)
        fn = math.sqrt(FF) + 1.0e-300
        if Pw > 0.0:
            v = (1.0 - alpha) * v + (alpha * vn / fn) * F
            if npos >= 5:
                dt = min(dt * 1.1, dtmax)
                alpha *= 0.99
            npos += 1
        else:
            v = torch.zeros_like(v)
            dt = max(dt * 0.5, 1.0e-7)
            alpha = 0.1
            npos = 0
        v = v + F * dt
        dx = v * dt
        dn = (dx * dx).sum(1).max().sqrt()
        sc = torch.where(dn > capw, capw / torch.clamp(dn, min=1.0e-300), torch.ones_like(dn))
        dx = dx * sc
        v = v * sc
        x = x + dx
        x = x / torch.sqrt((x * x).sum(1, keepdim=True))
        v = gn.q_tang(v, x)
        E, G, mon = gn.q_eg(x)
        F = -gn.q_tang(G, x)
        st = torch.stack([(F * F).sum(1).max(), E, mon, (F * v).sum(), (v * v).sum(), (F * F).sum()]).tolist()
        fmax, Ev, monv, Pw, vv, FF = math.sqrt(st[0]), st[1], st[2], st[3], st[4], st[5]
        mon_lauf = min(mon_lauf, monv)
    return x, Ev, fmax, it, monv, mon_lauf


def fire_psi(gn, p, nmax, stopp, dtmax=0.1, dtstart=0.02, capw=0.05, nskip=30, merke=True, pS=None):
    """Port von z2s2.fire_psi (anstieg = inf). stopp(it, E, fmax, D) -> (Klasse oder None, im_Sattelbereich);
    D = max sin^2(p - pS) ueber freie Knoten (feste Knoten haben p = pS). Ein Abgleich mit dem Wirt je Schritt."""
    def werte(p, v):
        E, G, cmin = gn.psi_eg(p[None])
        F = -G[0]
        teile = [E[0], F.abs().max(), cmin[0], (F * v).sum(), (v * v).sum(), (F * F).sum()]
        if pS is not None:
            sd = torch.sin(p - pS)
            teile.append((sd * sd).max())
        st = torch.stack(teile).tolist()
        return F, st

    v = torch.zeros_like(p)
    F, st = werte(p, v)
    E, fmax, cmin, Pw, vv, FF = st[:6]
    D = st[6] if pS is not None else 0.0
    dt, alpha, npos = dtstart, 0.1, 0
    best = (math.inf, None, None, -1)
    klasse, it, Emax, cmin_lauf = None, 0, E, cmin
    for it in range(nmax):
        k, bereich = stopp(it, E, fmax, D)
        if merke and it >= nskip:
            if bereich and fmax < best[0]:
                best = (fmax, p.clone(), E, it)
        if k is not None:
            klasse = k
            break
        vn = math.sqrt(vv)
        fn = math.sqrt(FF) + 1.0e-300
        if Pw > 0.0:
            v = (1.0 - alpha) * v + (alpha * vn / fn) * F
            if npos >= 5:
                dt = min(dt * 1.1, dtmax)
                alpha *= 0.99
            npos += 1
        else:
            v = torch.zeros_like(v)
            dt = max(dt * 0.5, 1.0e-7)
            alpha = 0.1
            npos = 0
        v = v + F * dt
        dx = v * dt
        dn = dx.abs().max()
        sc = torch.where(dn > capw, capw / torch.clamp(dn, min=1.0e-300), torch.ones_like(dn))
        dx = dx * sc
        v = v * sc
        p = p + dx
        F, st = werte(p, v)
        E, fmax, cmin, Pw, vv, FF = st[:6]
        D = st[6] if pS is not None else 0.0
        Emax = max(Emax, E)
        cmin_lauf = min(cmin_lauf, cmin)
    else:
        it = nmax
    if best[1] is None:
        best = (fmax, p.clone(), E, -1)
    return klasse, p, int(it), best, E, fmax, Emax, cmin_lauf


# ---------------------------------------------------------------- Hilfen

def lade_S(gn, pfad):
    qS = np.load(pfad)["q"]
    pS_np = np.arctan2(qS[:, 3], qS[:, 0])
    return qS, pS_np, torch.as_tensor(pS_np, dtype=DT, device=DEV)


def q_np(p, qS, netz):
    return z2s2.q_aus_psi(p.detach().cpu().numpy(), qS, netz)


def E_quat(gn, q_np_arr):
    X = torch.as_tensor(q_np_arr, dtype=DT, device=DEV)
    E, _, _ = gn.q_eg(X, grad=False)
    return float(E)


# ---------------------------------------------------------------- pruef

def modus_pruef(args):
    t0 = time.time()
    gn = GNetz(args.r0, args.R, ch=args.ch)
    netz = gn.netz
    eb = z2s2.Eben(netz)
    rng = np.random.default_rng([49, 7, int(round(args.R))])
    aus = {"kopf": None, "netz_info": netz.info(), "t_netz_s": gn.t_netz, "t_netz_cpu_s": gn.t_netz_cpu}
    # Zufallszustaende: Quaternion (normiert, feste Knoten gesetzt) und psi
    abw = []
    for j in range(args.nzufall):
        x = rng.normal(size=(netz.N, 1, 4))
        x = x / np.sqrt((x * x).sum(-1, keepdims=True))
        x = netz.setze(x, 2.0 * np.pi)
        Ec, Gc, monc = netz.energie(x)
        Fc = -netz.tang(Gc, x)[:, 0]
        X = torch.as_tensor(x[:, 0], dtype=DT, device=DEV)
        Eg, Gg, mong = gn.q_eg(X)
        Fg = (-gn.q_tang(Gg, X)).cpu().numpy()
        p = rng.uniform(-np.pi, np.pi, size=netz.N)
        p[netz.kern] = np.pi
        p[netz.rand] = 0.0
        Ep, Gp, _ = eb.energie(p)
        Fp = np.where(netz.frei, -Gp, 0.0)
        Epg, Gpg, _ = gn.psi_eg(torch.as_tensor(p, dtype=DT, device=DEV)[None])
        Fpg = (-Gpg[0]).cpu().numpy()
        abw.append({"quat_rel_E": abs(float(Eg) - float(Ec[0])) / abs(float(Ec[0])),
                    "quat_max_abw_F": float(np.abs(Fg - Fc).max()), "quat_max_F": float(np.abs(Fc).max()),
                    "quat_sonde_abw": abs(float(mong) - float(monc[0])),
                    "psi_rel_E": abs(float(Epg[0]) - Ep) / abs(Ep),
                    "psi_max_abw_F": float(np.abs(Fpg - Fp).max()), "psi_max_F": float(np.abs(Fp).max())})
    aus["zufall"] = abw
    # E_S aus der CPU-npz (Z2-SCHUTZ-2), auf der GPU nachgerechnet
    if args.start and os.path.exists(args.start):
        qS, pS_np, pS = lade_S(gn, args.start)
        Ecpu, _, _ = netz.energie(qS[:, None, :], grad=False)
        Eg = E_quat(gn, qS)
        Epg, _, _ = gn.psi_eg(pS[None], grad=False)
        aus["E_S_cpu_neu"] = float(Ecpu[0])
        aus["E_S_gpu_quat"] = Eg
        aus["E_S_gpu_psi"] = float(Epg[0])
        aus["E_S_rel_quat"] = abs(Eg - float(Ecpu[0])) / float(Ecpu[0])
    # Zeit je Gradient: GPU (Median ueber nzeit Aufrufe, je mit Synchronisation) und CPU (Median ueber nzeit_cpu)
    X = torch.as_tensor(netz.setze(np.tile(np.array([1.0, 0, 0, 0]), (netz.N, 1, 1)).astype(float), 2 * np.pi)[:, 0],
                        dtype=DT, device=DEV)
    p1 = torch.as_tensor(np.where(netz.kern, np.pi, 0.0) + 0.3 * netz.h, dtype=DT, device=DEV)
    zeiten = {}
    for name, fn in (("gpu_quat_B1", lambda: gn.q_eg(X)),
                     ("gpu_psi_B1", lambda: gn.psi_eg(p1[None])),
                     ("gpu_psi_B6", lambda: gn.psi_eg(p1[None].expand(6, -1).contiguous()))):
        for _ in range(3):
            fn()
        sync()
        ts = []
        for _ in range(args.nzeit):
            t1 = time.time()
            fn()
            sync()
            ts.append(time.time() - t1)
        zeiten[name + "_ms_median"] = float(np.median(ts) * 1e3)
        zeiten[name + "_ms_min"] = float(np.min(ts) * 1e3)
    x1 = X.cpu().numpy()[:, None, :]
    pc = p1.cpu().numpy()
    for name, fn in (("cpu_quat_B1", lambda: netz.energie(x1)), ("cpu_psi_B1", lambda: eb.energie(pc))):
        fn()
        ts = []
        for _ in range(args.nzeit_cpu):
            t1 = time.time()
            fn()
            ts.append(time.time() - t1)
        zeiten[name + "_ms_median"] = float(np.median(ts) * 1e3)
    aus["zeiten"] = zeiten
    aus["laufzeit_s"] = time.time() - t0
    aus["maxrss_mb"] = maxrss_mb()
    aus["kopf"] = kopf(args)
    g2.schreibe_json(os.path.join(args.aus, "pruef-%s.json" % gtag(args.r0, args.R)), aus)
    print("pruef fertig %s laufzeit %.1f s" % (gtag(args.r0, args.R), aus["laufzeit_s"]))


# ---------------------------------------------------------------- start

def modus_start(args):
    t0 = time.time()
    gn = GNetz(args.r0, args.R, ch=args.ch)
    netz = gn.netz
    x = np.zeros((netz.N, 1, 4))
    x[:, 0, 0] = np.cos(np.pi * netz.h)
    x[:, 0, 3] = np.sin(np.pi * netz.h)
    x = netz.setze(x, 2.0 * np.pi)
    E0 = E_quat(gn, x[:, 0])
    it, grund = 0, "nmax"
    if args.darst == "quat":
        X = torch.as_tensor(x[:, 0], dtype=DT, device=DEV)
        ml_alle = 1.0
        while True:
            X, E, fm, i1, mon, ml = fire_q(gn, X, min(1000, args.nmax - it), args.ftol, args.dtmax)
            it += int(i1) + (0 if fm <= args.ftol else 1)
            ml_alle = min(ml_alle, ml)
            if fm <= args.ftol:
                grund = "konvergiert"
                break
            if it >= args.nmax:
                break
            if wand() > args.budget:
                grund = "wandzeit"
                break
        q = X.cpu().numpy()
    else:
        p = torch.as_tensor(np.arctan2(x[:, 0, 3], x[:, 0, 0]), dtype=DT, device=DEV)
        ftol = args.ftol

        def stopp(it_, E_, fmax_, D_):
            if fmax_ <= ftol:
                return "konvergiert", False
            if wand() > args.budget:
                return "wandzeit", False
            return None, False
        kl, p, it, _, E, fm, _, ml_alle = fire_psi(gn, p, args.nmax, stopp, dtmax=args.dtmax, merke=False)
        grund = kl if kl is not None else "nmax"
        q = z2s2.q_aus_psi(p.cpu().numpy(), x[:, 0], netz)
        mon = ml_alle
    sync()
    t_fire = time.time() - t0
    tag = "start-" + gtag(args.r0, args.R)
    np.savez(os.path.join(args.aus, tag + ".npz"), q=q)
    ES_q = E_quat(gn, q)
    pS = torch.as_tensor(np.arctan2(q[:, 3], q[:, 0]), dtype=DT, device=DEV)
    ES_p, _, _ = gn.psi_eg(pS[None], grad=False)
    aus = {"kopf": kopf(args), "netz_info": netz.info(), "t_netz_s": gn.t_netz, "E_anfang": E0, "E_S": ES_q,
           "E_S_psi": float(ES_p[0]), "eben_rest": float(np.abs(q[:, 1:3]).max()), "fmax": float(fm),
           "schritte": int(it), "grund": grund, "sonde_lauf": float(ml_alle), "darst": args.darst,
           "laufzeit_fire_s": t_fire, "laufzeit_s": time.time() - t0, "maxrss_mb": maxrss_mb()}
    g2.schreibe_json(os.path.join(args.aus, tag + ".json"), aus)
    print("start fertig %s E_S %.10f schritte %d laufzeit %.1f s" % (tag, ES_q, it, aus["laufzeit_s"]))


# ---------------------------------------------------------------- Verfahren A (Port von z2s2.modus_bisekt)

def modus_bisekt(args):
    t0 = time.time()
    gn = GNetz(args.r0, args.R, ch=args.ch)
    netz = gn.netz
    qS, pS_np, pS = lade_S(gn, args.start)
    ESq = E_quat(gn, qS)
    ESt, _, _ = gn.psi_eg(pS[None], grad=False)
    ES = float(ESt[0])
    w = torch.as_tensor(z2s2.kappe_w(netz, args), dtype=DT, device=DEV)
    t_halb = args.halb_anteil * args.budget
    t_halb2 = args.halb2_anteil * args.budget
    t_halb3 = args.halb3_anteil * args.budget
    t_halb3b = args.halb3b_anteil * args.budget
    t_bahn = args.bahn_anteil * args.budget
    nschritte = {"n": 0}

    def stopp_klasse(it, E, fmax, D):
        bereich = bool(D >= args.d_sattel and fmax > args.f_ruhe_bereich)
        if E < ES - args.delta_k:
            return "T", bereich
        if it >= args.nskip and D <= args.eps_s:
            return "S", bereich
        if it >= args.nskip and fmax <= args.ftol_m:
            return "M", bereich
        if wand() > t_bahn:
            return "offen", bereich
        return None, bereich

    def Dmax(p, ref):
        sd = torch.sin(p - ref)
        return float((sd * sd * gn.frei_f).max())

    def bahn(p0, lam):
        kl, p, it, best, E, fm, Emax, cl = fire_psi(gn, p0, args.nbis, stopp_klasse, dtmax=args.dtmax,
                                                    nskip=args.nskip, pS=pS)
        nschritte["n"] += it
        if kl is None:
            kl = "offen"
        info = {"lambda": lam, "klasse": kl, "schritte": it, "fmin": best[0], "E_fmin": best[2], "it_fmin": best[3],
                "fmax_ende": fm, "E_ende": E, "D_ende": Dmax(p, pS), "fmin_im_sattelbereich": bool(best[3] >= 0),
                "t": wand()}
        return kl, p, best, info

    def bisektion(zustand, nh, t_grenze, pruef0, ziel):
        oben, unten = (("T", "M"), ("S",)) if ziel == "S" else (("T",), ("S", "M"))
        lo, hi = 0.0, 1.0
        sch = []
        kl, p, best, info = bahn(zustand(1.0), 1.0)
        sch.append(info)
        letzte = {"o": (1.0, p, best, kl) if kl in oben else None, "u": None, "tmin": None}
        if kl == "T":
            letzte["tmin"] = (1.0, p.clone())
        if letzte["o"] is None:
            return lo, hi, sch, letzte, 0
        if pruef0:
            kl, p, best, info = bahn(zustand(0.0), 0.0)
            sch.append(info)
            if kl not in unten:
                return lo, hi, sch, letzte, 0
            letzte["u"] = (0.0, p, best, kl)
        n_h = 0
        for _ in range(nh):
            if wand() > t_grenze:
                break
            lam = 0.5 * (lo + hi)
            kl, p, best, info = bahn(zustand(lam), lam)
            sch.append(info)
            if kl == "T" and (letzte["tmin"] is None or lam < letzte["tmin"][0]):
                letzte["tmin"] = (lam, p.clone())
            if kl in oben:
                hi = lam
                letzte["o"] = (lam, p, best, kl)
                n_h += 1
            elif kl in unten:
                lo = lam
                letzte["u"] = (lam, p, best, kl)
                n_h += 1
            else:
                break
        return lo, hi, sch, letzte, n_h

    def nachschaerfen(letzte, ziel, t_grenze):
        info = {"gerechnet": False}
        if not (letzte["o"] is not None and letzte["u"] is not None and letzte["o"][2][3] >= 0
                and letzte["u"][2][3] >= 0 and args.nbisekt2 > 0):
            return letzte, info
        pa, pb = letzte["u"][2][1].clone(), letzte["o"][2][1].clone()
        lo2, hi2, sch2, l2, n2 = bisektion(lambda mu: (1.0 - mu) * pa + mu * pb, args.nbisekt2, t_grenze, True, ziel)
        ok2 = bool(l2["o"] is not None and l2["u"] is not None and n2 >= args.nbisekt2_min
                   and l2["o"][2][3] >= 0 and l2["u"][2][3] >= 0)
        info = {"gerechnet": True, "gilt": ok2, "mu_lo": lo2, "mu_hi": hi2, "n_halb": n2, "schritte": sch2,
                "abstand_start": float(torch.sqrt(((pb - pa) ** 2).sum()))}
        return (l2 if ok2 else letzte), info

    def sattel_info(letzte):
        bo, bu = letzte["o"][2], letzte["u"][2]
        info = {"E_fmin_oben": bo[2], "E_fmin_unten": bu[2], "fmin_oben": bo[0], "fmin_unten": bu[0],
                "klasse_oben": letzte["o"][3], "klasse_unten": letzte["u"][3],
                "sattelbereich": [bool(bo[3] >= 0), bool(bu[3] >= 0)],
                "genau": bool(bo[3] >= 0 and bu[3] >= 0 and max(bo[0], bu[0]) <= args.fmin_max),
                "E_sattel": float(max(bo[2], bu[2])), "barriere": float(max(bo[2], bu[2]) - ES)}
        return info, (bo[1] if bo[2] >= bu[2] else bu[1])

    lo, hi, schritte, letzte, n_halb = bisektion(lambda lam: pS * (1.0 - lam * w), args.nbisekt, t_halb, False, "S")
    aus = {"kopf": None, "netz_info": netz.info(), "E_S": ES, "E_S_quat": ESq,
           "schritte": schritte, "lambda_lo": lo, "lambda_hi": hi, "n_halb": n_halb,
           "lambda1_klasse": schritte[0]["klasse"], "stufe2": {"gerechnet": False}, "stufe3": {"gerechnet": False}}
    gut = letzte["o"] is not None and letzte["u"] is not None
    aus["klammer"] = bool(gut)
    if gut:
        tmin1 = letzte["tmin"]
        letzte, aus["stufe2"] = nachschaerfen(letzte, "S", t_halb2)
        s1, sattel1 = sattel_info(letzte)
        aus["sattel1"] = s1
        pfad = [pS, letzte["u"][2][1], letzte["o"][2][1]]
        ende, barriere, genau, sattel, pfad_ok = letzte["o"][1], s1["barriere"], s1["genau"], sattel1, True
        aus["weg_art"] = "S -> Sattel -> T"
        if letzte["o"][3] == "M":
            pM = letzte["o"][1].clone()
            pfad.append(pM)
            info3 = {"gerechnet": False, "lambda_T": tmin1[0] if tmin1 is not None else None}
            pfad_ok = False
            if tmin1 is not None:
                pTe = tmin1[1].clone()
                lo3, hi3, sch3, l3, n3 = bisektion(lambda mu: (1.0 - mu) * pM + mu * pTe,
                                                   args.nbisekt, t_halb3, True, "T")
                info3.update({"gerechnet": True, "mu_lo": lo3, "mu_hi": hi3, "n_halb": n3, "schritte": sch3})
                if l3["o"] is not None and l3["u"] is not None and n3 >= args.nbisekt2_min:
                    l3, info3["stufe3b"] = nachschaerfen(l3, "T", t_halb3b)
                    s3, sattel3 = sattel_info(l3)
                    s3["unten_ende_D_zu_M"] = Dmax(l3["u"][1], pM)
                    s3["unten_ende_gleich_M"] = bool(l3["u"][3] == "M" and s3["unten_ende_D_zu_M"] <= args.eps_s)
                    info3["sattel2"] = s3
                    if l3["u"][3] == "S":
                        aus["weg_art"] = "S -> Sattel 2 -> T (unten S)"
                        pfad = [pS, l3["u"][2][1], l3["o"][2][1]]
                        barriere, genau, sattel, pfad_ok = s3["barriere"], s3["genau"], sattel3, True
                    elif s3["unten_ende_gleich_M"]:
                        aus["weg_art"] = "S -> Sattel 1 -> M -> Sattel 2 -> T"
                        pfad += [l3["u"][2][1], l3["o"][2][1]]
                        barriere = max(s1["barriere"], s3["barriere"])
                        sattel = sattel1 if s1["E_sattel"] >= s3["E_sattel"] else sattel3
                        genau, pfad_ok = bool(s1["genau"] and s3["genau"]), True
                    ende = l3["o"][1]
            aus["stufe3"] = info3
        aus["barriere"] = float(barriere)
        aus["genau"] = bool(genau)
        aus["pfad_ok"] = bool(pfad_ok)
        aus["lokalisierung"] = z2s2.lokal2(netz, q_np(sattel, qS, netz), qS)
        np.savez(os.path.join(args.aus, "bisekt-%s.npz" % gtag(args.r0, args.R)),
                 P=np.stack([t.detach().cpu().numpy() for t in pfad + [ende]]))

        def stopp_frei(it, E, fmax, D):
            if E < args.e_T:
                return "T", False
            if fmax <= args.ftol_ruhe:
                return "ruhe", False
            if wand() > args.budget:
                return "zeit", False
            return None, False

        kl2, p2, it2, _, E2, fm2, Emax2, cl2 = fire_psi(gn, ende.clone(), args.nfrei, stopp_frei,
                                                        dtmax=args.dtmax, merke=False)
        nschritte["n"] += it2
        kl2 = kl2 if kl2 is not None else "nmax"
        c2 = torch.cos(p2[gn.a] - p2[gn.b])
        aus["freigabe"] = {"klasse": kl2, "schritte": it2, "E_end": E2, "fmax_end": fm2, "E_max": Emax2,
                           "T_erreicht": kl2 == "T", "zwischenminimum": kl2 == "ruhe",
                           "E_max_unter_ES": bool(Emax2 < ES), "bindungen_c_le_0_ende": int((c2 <= 0).sum()),
                           "t": wand()}
        np.savez(os.path.join(args.aus, "freigabe-%s.npz" % gtag(args.r0, args.R)), p=p2.cpu().numpy())
        aus["gueltig_A_ohne_S"] = bool(aus["lambda1_klasse"] in ("T", "M") and n_halb >= args.nbisekt_min
                                       and pfad_ok and genau and aus["freigabe"]["T_erreicht"]
                                       and aus["freigabe"]["E_max_unter_ES"])
    else:
        aus["gueltig_A_ohne_S"] = False
    alle_sch = (schritte + (aus["stufe2"].get("schritte") or []) + (aus["stufe3"].get("schritte") or [])
                + ((aus["stufe3"].get("stufe3b") or {}).get("schritte") or []))
    aus["zahl_M"] = int(sum(1 for s in alle_sch if s["klasse"] == "M"))
    aus["zahl_offen"] = int(sum(1 for s in alle_sch if s["klasse"] == "offen"))
    aus["zahl_bahnen"] = len(alle_sch)
    aus["fire_schritte_gesamt"] = int(nschritte["n"])
    aus["laufzeit_s"] = time.time() - t0
    aus["maxrss_mb"] = maxrss_mb()
    aus["kopf"] = kopf(args)
    g2.schreibe_json(os.path.join(args.aus, "bisekt-%s.json" % gtag(args.r0, args.R)), aus)
    print("bisekt fertig %s barriere %s laufzeit %.1f s" % (gtag(args.r0, args.R), aus.get("barriere"),
                                                             aus["laufzeit_s"]))


# ---------------------------------------------------------------- Verfahren B: CI-NEB in psi (Port von z2.wegrechnung)

def reparam_psi(pfad, M, frei):
    """g2.reparam_feld ohne Normierung (psi)."""
    d = pfad[1:, frei] - pfad[:-1, frei]
    seg = np.sqrt((d * d).sum(1))
    s = np.concatenate([[0.0], np.cumsum(seg)])
    ziel = np.linspace(0.0, s[-1], M)
    out = np.empty((M,) + pfad.shape[1:])
    j = np.clip(np.searchsorted(s, ziel, side="right") - 1, 0, len(s) - 2)
    for m in range(M):
        jj = j[m]
        ww = 0.0 if seg[jj] <= 0 else min(max((ziel[m] - s[jj]) / seg[jj], 0.0), 1.0)
        out[m] = (1.0 - ww) * pfad[jj] + ww * pfad[jj + 1]
    out[0] = pfad[0]
    out[-1] = pfad[-1]
    return out


def ausrichten_psi(X):
    """z2.ausrichten in psi: Bild k je Knoten um ein Vielfaches von pi zum Bild k-1 (q -> -q ist psi -> psi + pi).
    Geschwindigkeiten bleiben (d psi aendert sich unter psi -> psi + pi nicht)."""
    for k in range(1, X.shape[0]):
        X[k] = X[k] - PI * torch.round((X[k] - X[k - 1]) / PI)
    return X


def wegrechnung_psi(gn, X, args):
    t0 = time.time()
    P = X.shape[0]
    fr = gn.frei_f
    X = ausrichten_psi(X)
    Ee, _, me = gn.psi_eg(X[[0, P - 1]], grad=False)
    E_end = Ee.tolist()
    m_end = me.tolist()
    v = torch.zeros_like(X)
    dt = torch.full((P,), args.dtstart, dtype=DT, device=DEV)
    alpha = torch.full((P,), 0.1, dtype=DT, device=DEV)
    npos = torch.zeros(P, dtype=torch.int64, device=DEV)

    def roh(X):
        E_in, G_in, m_in = gn.psi_eg(X[1:-1])
        F = torch.zeros_like(X)
        F[1:-1] = -G_in
        E = [E_end[0]] + E_in.tolist() + [E_end[1]]
        mon = [m_end[0]] + m_in.tolist() + [m_end[1]]
        return E, F, mon

    def komponiere(X, E, F, ki):
        wp, wm = [], []
        for k in range(1, P - 1):
            Ep, E0, Em = E[k + 1], E[k], E[k - 1]
            if Ep > E0 > Em:
                wp.append(1.0)
                wm.append(0.0)
            elif Ep < E0 < Em:
                wp.append(0.0)
                wm.append(1.0)
            else:
                dmax = max(abs(Ep - E0), abs(Em - E0))
                dmin = min(abs(Ep - E0), abs(Em - E0))
                if Ep > Em:
                    wp.append(dmax)
                    wm.append(dmin)
                else:
                    wp.append(dmin)
                    wm.append(dmax)
        wp = torch.tensor(wp, dtype=DT, device=DEV)[:, None]
        wm = torch.tensor(wm, dtype=DT, device=DEV)[:, None]
        dp = X[2:] - X[1:-1]
        dm = X[1:-1] - X[:-2]
        t = (wp * dp + wm * dm) * fr
        tn = t / torch.clamp(torch.sqrt((t * t).sum(1, keepdim=True)), min=1.0e-300)
        Fi = F[1:-1]
        fp = (Fi * tn).sum(1)
        lp = torch.sqrt((dp * dp).sum(1))
        lm = torch.sqrt((dm * dm).sum(1))
        kl = torch.zeros(P - 2, dtype=torch.bool, device=DEV)
        if ki > 0:
            kl[ki - 1] = True
        coef = torch.where(kl, -2.0 * fp, -fp + args.ks * (lp - lm))
        Fn = torch.zeros_like(X)
        Fn[1:-1] = Fi + coef[:, None] * tn
        return Fn

    ki = -1
    E, F, mon = roh(X)
    Fn = komponiere(X, E, F, ki)
    lauf = min(mon)
    verlauf = []
    E_anf = list(E)
    konv, grund, it = False, "nmax", 0
    kl_moeglich = False
    fk = [0.0] * P
    for it in range(args.nmax):
        if it >= args.nvor:
            km = int(np.argmax(E[1:-1])) + 1
            kl_moeglich = bool(E[km] > max(E[0], E[-1]))
            ki_neu = km if kl_moeglich else -1
            if ki_neu != ki:
                ki = ki_neu
                Fn = komponiere(X, E, F, ki)
        fk = Fn.abs().max(1).values.tolist()
        fb = max([fk[k] for k in range(1, P - 1) if k != ki] + [0.0])
        fki = fk[ki] if ki > 0 else None
        if it % 20 == 0:
            verlauf.append({"it": it, "E_max": float(max(E[1:-1])), "imax": int(np.argmax(E[1:-1])) + 1,
                            "ki": int(ki), "E_ki": float(E[ki]) if ki > 0 else None, "fband": fb, "fki": fki,
                            "dt": float(dt.max()), "sonde_min": float(min(mon)), "t": time.time() - t0})
        if it >= args.nvor:
            if ki > 0 and fki < args.ftol_ci and fb < args.ftol_band:
                konv, grund = True, "konvergiert"
                break
            if ki < 0 and fb < args.ftol_band:
                konv, grund = True, "konvergiert (ohne Klettern)"
                break
        if wand() > args.budget:
            grund = "wandzeit"
            break
        Pw = (Fn * v).sum(1)
        vn = torch.sqrt((v * v).sum(1))
        fnn = torch.sqrt((Fn * Fn).sum(1)) + 1.0e-300
        pos = Pw > 0.0
        v = torch.where(pos[:, None], (1.0 - alpha)[:, None] * v + (alpha * vn / fnn)[:, None] * Fn,
                        torch.zeros_like(v))
        hoch = pos & (npos >= 5)
        dt = torch.where(hoch, torch.clamp(dt * 1.1, max=args.dtmax), torch.where(pos, dt, torch.clamp(dt * 0.5,
                                                                                                    min=1.0e-7)))
        alpha = torch.where(hoch, alpha * 0.99, torch.where(pos, alpha, torch.full_like(alpha, 0.1)))
        npos = torch.where(pos, npos + 1, torch.zeros_like(npos))
        v = v + Fn * dt[:, None]
        dx = v * dt[:, None]
        dn = dx.abs().max(1).values
        sc = torch.where(dn > args.capw, args.capw / torch.clamp(dn, min=1.0e-300), torch.ones_like(dn))
        dx = dx * sc[:, None]
        v = v * sc[:, None]
        X = X + dx
        X = ausrichten_psi(X)
        v = v * fr
        v[0] = 0.0
        v[-1] = 0.0
        E, F, mon = roh(X)
        Fn = komponiere(X, E, F, ki)
        lauf = min(lauf, min(mon))
    fk = Fn.abs().max(1).values.tolist()
    fb = max([fk[k] for k in range(1, P - 1) if k != ki] + [0.0])
    fki = fk[ki] if ki > 0 else None
    verlauf.append({"it": it, "E_max": float(max(E[1:-1])), "imax": int(np.argmax(E[1:-1])) + 1, "ki": int(ki),
                    "E_ki": float(E[ki]) if ki > 0 else None, "fband": fb, "fki": fki, "dt": float(dt.max()),
                    "sonde_min": float(min(mon)), "t": time.time() - t0})
    abst = [float(torch.sqrt(((X[k + 1] - X[k]) ** 2).sum())) for k in range(P - 1)]
    nachbar = [float((torch.cos(X[k + 1] - X[k]) + 2.0 * (1.0 - fr)).min()) for k in range(P - 1)]
    erg = {"verfahren": "neb (psi)", "iterationen": int(it), "grund": grund, "konvergiert": bool(konv),
           "ki": int(ki), "klettern_moeglich": bool(kl_moeglich), "E_profil": E, "E_profil_anfang": E_anf,
           "sonde_bilder": mon, "sonde_lauf": lauf, "fband": fb, "fki": fki, "fmax_bild": fk,
           "abstand": abst, "nachbar_min_cos": nachbar, "verlauf": verlauf, "laufzeit_weg_s": time.time() - t0}
    return X, erg


def modus_weg(args):
    t0 = time.time()
    gn = GNetz(args.r0, args.R, ch=args.ch)
    netz = gn.netz
    qS, pS_np, pS = lade_S(gn, args.start)
    ES = E_quat(gn, qS)
    Z = np.load(args.zugpfad)["P"]
    X = reparam_psi(Z, args.M + 2, netz.frei)
    X[0] = Z[0]
    X[-1] = Z[-1]
    del Z
    X = torch.as_tensor(X, dtype=DT, device=DEV)
    X, erg = wegrechnung_psi(gn, X, args)
    E = erg["E_profil"]
    tag = "weg-%s-neb" % gtag(args.r0, args.R)
    aus = {"kopf": None, "netz_info": netz.info(), "weg": erg, "E_S": ES, "E_0": float(E[0]), "E_ende": float(E[-1])}
    ki = erg["ki"]
    if ki > 0:
        aus["E_sattel"] = float(E[ki])
        aus["barriere"] = float(E[ki] - ES)
        qk = q_np(X[ki], qS, netz)
        aus["E_sattel_quat"] = E_quat(gn, qk)
        aus["lokalisierung"] = z2s2.lokal2(netz, qk, qS)
        np.savez(os.path.join(args.aus, tag + "-kletterbild.npz"), p=X[ki].cpu().numpy())
    else:
        aus["E_sattel"] = None
        aus["barriere"] = None
    np.savez(os.path.join(args.aus, tag + "-weg.npz"), X=X.cpu().numpy())
    aus["laufzeit_s"] = time.time() - t0
    aus["maxrss_mb"] = maxrss_mb()
    aus["kopf"] = kopf(args)
    g2.schreibe_json(os.path.join(args.aus, tag + ".json"), aus)
    print("weg fertig %s iterationen %d grund %s barriere %s laufzeit %.1f s" % (
        tag, erg["iterationen"], erg["grund"], aus["barriere"], aus["laufzeit_s"]))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("modus", choices=["pruef", "start", "bisekt", "weg"])
    p.add_argument("--aus", default=".")
    p.add_argument("--r0", type=float, default=10.0)
    p.add_argument("--R", type=float, default=20.0)
    p.add_argument("--start", default="")
    p.add_argument("--zugpfad", default="")
    p.add_argument("--ch", type=int, default=2)
    p.add_argument("--darst", default="quat", choices=["quat", "psi"])
    # pruef
    p.add_argument("--nzufall", type=int, default=2)
    p.add_argument("--nzeit", type=int, default=50)
    p.add_argument("--nzeit_cpu", type=int, default=5)
    # Start
    p.add_argument("--nmax", type=int, default=20000)
    p.add_argument("--ftol", type=float, default=1.0e-7)
    p.add_argument("--dtmax", type=float, default=0.1)
    p.add_argument("--budget", type=float, default=540.0)
    # Bisektion (Werte wie z2s2.main)
    p.add_argument("--kappe_b", type=float, default=30.0)
    p.add_argument("--d_grad", type=float, default=30.0)
    p.add_argument("--delta_k", type=float, default=1.0)
    p.add_argument("--eps_s", type=float, default=1.0e-3)
    p.add_argument("--d_sattel", type=float, default=0.5)
    p.add_argument("--nskip", type=int, default=30)
    p.add_argument("--nbis", type=int, default=1500)
    p.add_argument("--nbisekt", type=int, default=14)
    p.add_argument("--nbisekt_min", type=int, default=10)
    p.add_argument("--halb_anteil", type=float, default=0.45)
    p.add_argument("--halb2_anteil", type=float, default=0.55)
    p.add_argument("--halb3_anteil", type=float, default=0.65)
    p.add_argument("--halb3b_anteil", type=float, default=0.72)
    p.add_argument("--nbisekt2", type=int, default=12)
    p.add_argument("--nbisekt2_min", type=int, default=6)
    p.add_argument("--fmin_max", type=float, default=0.05)
    p.add_argument("--ftol_m", type=float, default=1.0e-9)
    p.add_argument("--f_ruhe_bereich", type=float, default=1.0e-6)
    p.add_argument("--bahn_anteil", type=float, default=0.78)
    p.add_argument("--e_T", type=float, default=1.0e-3)
    p.add_argument("--ftol_ruhe", type=float, default=1.0e-6)
    p.add_argument("--nfrei", type=int, default=30000)
    # CI-NEB (Werte wie die Hauptlaeufe von Z2-SCHUTZ-2)
    p.add_argument("--M", type=int, default=6)
    p.add_argument("--ks", type=float, default=1.0)
    p.add_argument("--nvor", type=int, default=50)
    p.add_argument("--ftol_ci", type=float, default=5.0e-3)
    p.add_argument("--ftol_band", type=float, default=1.0)
    p.add_argument("--dtstart", type=float, default=0.02)
    p.add_argument("--capw", type=float, default=0.05)
    args = p.parse_args()
    if args.modus == "weg" and args.budget == 540.0:
        args.budget = 480.0
    os.makedirs(args.aus, exist_ok=True)
    {"pruef": modus_pruef, "start": modus_start, "bisekt": modus_bisekt, "weg": modus_weg}[args.modus](args)


if __name__ == "__main__":
    main()
