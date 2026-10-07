"""KAUSAL-4D-KERNMASSE-1 (Runde 41, Code-Agent), Teil A: Mittel mit der Masse im Kern (VK), Pole, Erwartung.

Ziel-Mittel (VORAB.md Abschnitt 2): G_K~(omega, k) = k~(Z_m), Z_m = sqrt(k^2 + m^2 - omega^2) (Re Z_m > 0), k~ = Johnstons
masseloser Linkkern (schicht2_kont.kt_gen mit Gewichten (1, 0, 0)). Ortsraum: g_K(tau) = a exp(-c tau^4) + T(tau^2).
Mittel der Realisierung auf der Kausalmenge (Mecke, Poisson): g_bar(tau) = a exp(-u) + sum_n t(n) u^n e^-u/n!, u = c tau^4.

Aufruf (nur ueber kleintest.sh):
  kernmasse_kont.py kern      <ausgabeordner> <rho1,rho2,...>   (Formelprobe: Fourier-Bild des Ortsraumkerns gegen
                                                                  k~(Z_m) bei reellem Z; Schranke; Splineprobe)
  kernmasse_kont.py pole      <ausgabeordner> <rho1,rho2,...> [datei]  (Windungszahlen von G_K~, Nullstellen, Pole,
                                                                  Residuum; datei Vorgabe pole-VK.json)
  kernmasse_kont.py erwartung <ausgabeordner> <rho1,...> <kontrolle 0/1> <name>  (E[phi_K], Realisierung
                                                                  und Ziel, Ziel bei rho = 1e6 gegen kc.faltung)
"""
import hashlib
import json
import os
import sys
import time

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import gammaln, kv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kausal4d as kd  # noqa: E402
import kontinuum4d as kc  # noqa: E402
import schicht2_kont as sk  # noqa: E402
import kernmasse_feld as kf  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
M = kd.MASSE
KS = sk.KS
NTAU_POL = sk.NTAU_POL
TAU_TAB = np.linspace(0.0, 7.6, 3801)


def tau_c(rho):
    return (40.0 / (np.pi * rho / 24.0)) ** 0.25


# ---------- Ziel-Mittel im Impulsraum ----------
def GK(om, k, rho, ntau=NTAU_POL):
    """G_K~ = k~(Z_m), Z_m = sqrt(k^2 + m^2 - omega^2), Re Z_m > 0."""
    om = np.atleast_1d(np.asarray(om, dtype=np.complex128))
    Zm = np.sqrt(k * k + M * M - om ** 2)
    Zm = np.where(Zm.real < 0, -Zm, Zm)
    return sk.kt_gen(Zm, rho, (1.0, 0.0, 0.0), ntau)


# ---------- Ortsraumkerne ----------
def g_ziel(tau, rho):
    tau = np.asarray(tau, dtype=float)
    c = np.pi * rho / 24.0
    return kd.a_hop(rho) * np.exp(-c * tau ** 4) + kf.T_sigma(tau ** 2, rho).reshape(tau.shape)


def tbar_direkt(tau, rho, tt=None):
    """sum_n t(n) Pois(n; c tau^4) (exakt bis auf Fenster +-15 sqrt(u) + 40)."""
    tau = np.atleast_1d(np.asarray(tau, dtype=float))
    c = np.pi * rho / 24.0
    u = c * tau ** 4
    umax = float(u.max())
    nmax = int(umax + 15.0 * np.sqrt(umax) + 60)
    if tt is None or tt.size < nmax + 1:
        tt = kf.t_tabelle(rho, nmax)
    out = np.zeros(tau.size)
    for i, ui in enumerate(u):
        if ui <= 0.0:
            continue
        lo = max(0, int(np.floor(ui - 15.0 * np.sqrt(ui) - 40)))
        hi = min(nmax, int(np.ceil(ui + 15.0 * np.sqrt(ui) + 40)))
        n = np.arange(lo, hi + 1)
        p = np.exp(n * np.log(ui) - ui - gammaln(n + 1.0))
        out[i] = float((p * tt[lo:hi + 1]).sum())
    return out


def tbar_spline(rho):
    tb = tbar_direkt(TAU_TAB, rho)
    return CubicSpline(TAU_TAB, tb), tb


def g_real_fun(rho, spl):
    c = np.pi * rho / 24.0
    a = kd.a_hop(rho)
    return lambda tau: a * np.exp(-c * tau ** 4) + spl(tau)


def ft_reell(gfun, Z, rho, tau_max=None, panel=1.0, npan=24):
    """(4 pi/Z) int_0^tau_max tau^2 g(tau) K1(Z tau) dtau fuer reelles Z > 0 (Gauss-Legendre-Panele)."""
    tc = tau_c(rho)
    if tau_max is None:
        tau_max = max(tc, 45.0 / Z)
    tn, wn = kc.gl(0.0, min(tc, tau_max), 64)
    teile_t, teile_w = [tn], [wn]
    x = min(tc, tau_max)
    while x < tau_max - 1e-12:
        b = min(x + panel, tau_max)
        t_, w_ = kc.gl(x, b, npan)
        teile_t.append(t_)
        teile_w.append(w_)
        x = b
    tau = np.concatenate(teile_t)
    w = np.concatenate(teile_w)
    return float((4 * np.pi / Z) * (w * tau ** 2 * gfun(tau) * kv(1, Z * tau)).sum())


# ---------- Modus kern (Formel- und Codeprobe, ohne Mittelwerte an Punkten) ----------
def modus_kern(ordner, rhos):
    t0 = time.time()
    out = {"modus": "kern", "rhos": rhos, "ergebnisse": {}}
    for rho in rhos:
        e = {}
        # Fourier-Bild des Ortsraum-Zielkerns gegen k~(sqrt(Z^2 + m^2)) bei reellem Z (Formel aus VORAB.md 2)
        fp = {}
        for Z in (0.5, 1.0, 2.0, 4.0):
            pos = ft_reell(lambda tau: g_ziel(tau, rho), Z, rho)
            mom = complex(sk.kt_gen(np.array([np.sqrt(Z * Z + M * M) + 0j]), rho, (1.0, 0.0, 0.0))[0])
            masselos = complex(sk.kt_gen(np.array([Z + 0j]), rho, (1.0, 0.0, 0.0))[0])
            fp[f"Z{Z:g}"] = {"ortsraum": pos, "k_tilde_Zm": mom.real, "rel_abw": abs(pos - mom.real) / abs(mom.real),
                             "k_tilde_Z_masselos": masselos.real, "kontinuum_1_durch_Z2_plus_m2": 1.0 / (Z * Z + M * M)}
        e["fourierprobe"] = fp
        # Schranke |t(n)| <= m^2/(8 pi)
        c = np.pi * rho / 24.0
        nn = np.unique(np.concatenate([np.arange(0, 20001), np.round(np.logspace(4.3, 7, 200)).astype(int)]))
        tt = kf.T_sigma(np.sqrt(nn / c), rho)
        e["schranke"] = {"max_abs_t": float(np.abs(tt).max()), "n_bei_max": int(nn[np.argmax(np.abs(tt))]),
                         "m2_durch_8pi": M * M / (8 * np.pi), "eingehalten": bool(np.abs(tt).max() <= M * M / (8 * np.pi) * (1 + 1e-9))}
        # Quadraturprobe T: 128 gegen 256 Knoten
        sg = np.linspace(0.0, 60.0, 601)
        e["T_quadratur_128_256_max_abs"] = float(np.abs(kf.T_sigma(sg, rho) - kf.T_sigma(sg, rho, nq=256)).max())
        # Splineprobe g_bar (nur Fehlergroesse)
        spl, _ = tbar_spline(rho)
        rng = np.random.default_rng(np.random.SeedSequence([20261004, 41, 7, int(rho * 1000)]))
        tz = np.sort(rng.uniform(0.0, 7.6, 300))
        e["tbar_spline_max_abs_fehler"] = float(np.abs(spl(tz) - tbar_direkt(tz, rho)).max())
        out["ergebnisse"][f"rho{rho:g}"] = e
        print(json.dumps({"rho": rho, "fourierprobe_rel_abw": [fp[k]["rel_abw"] for k in fp],
                          "schranke": e["schranke"]["eingehalten"], "zeit_s": round(time.time() - t0, 1)}), flush=True)
    out.update({"zeit_gesamt_s": round(time.time() - t0, 1), "skript_sha256": SKRIPT_SHA,
                "kernmasse_feld_sha256": kf.SKRIPT_SHA, "schicht2_kont_sha256": sk.SKRIPT_SHA,
                "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
    with open(os.path.join(ordner, "kern.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)


# ---------- Modus pole ----------
def newton_kurz(fun, om0, iters=30, rmax=12.0, ymin=-0.5):
    """Wie schicht2_kont.newton (Zentraldifferenz, Schritt <= 2), aber Abbruch, sobald die Iteration das Suchgebiet
    verlaesst (abs(omega) > rmax oder Im omega < ymin), und hoechstens 30 Schritte. G_K~ hat ausser bei echten
    Nullstellen keine Minima im Inneren (Maximumprinzip fuer 1/G_K~); fruchtlose Laeufe enden so frueh."""
    om = complex(om0)
    for _ in range(iters):
        f = fun(om)[0]
        h = 1e-6 * max(1.0, abs(om))
        d = (fun(om + h)[0] - fun(om - h)[0]) / (2 * h)
        if d == 0 or not np.isfinite(d):
            return om, np.inf
        st = f / d
        if abs(st) > 2.0:
            st = 2.0 * st / abs(st)
        om -= st
        if abs(om) > rmax or om.imag < ymin:
            return om, np.inf
        if abs(st) < 1e-13 * max(1.0, abs(om)):
            break
    return om, float(abs(fun(om)[0]))


def suche_kurz(fun, xs, ys, maske, region):
    """Wie schicht2_kont.suche (lokale Minima von abs(G) auf dem Gitter, hoechstens 60 Kandidaten), Newton per newton_kurz."""
    X, Y = np.meshgrid(xs, ys, indexing="ij")
    W = X + 1j * Y
    A = np.full(W.shape, np.inf)
    sel = maske(W)
    A[sel] = np.abs(fun(W[sel]))
    kand = []
    for i in range(1, W.shape[0] - 1):
        for j in range(1, W.shape[1] - 1):
            if not np.isfinite(A[i, j]):
                continue
            nb = A[i - 1:i + 2, j - 1:j + 2]
            if A[i, j] <= nb.min():
                kand.append((A[i, j], W[i, j]))
    kand.sort(key=lambda z: z[0])
    nullst = []
    for _, w0 in kand[:60]:
        om, res = newton_kurz(fun, w0)
        if res < 1e-9 and region(om) and all(abs(om - z) > 1e-6 for z in nullst):
            nullst.append(om)
    return nullst, len(kand)


def suche_S0_GK(f):
    out = []
    for x in np.arange(sk.S_X[0], sk.S_X[1] + 1e-9, 0.05):
        om, res = newton_kurz(f, complex(x, 0.001))
        if (res < 1e-9 and sk.S_X[0] <= om.real <= sk.S_X[1] and sk.S0_Y[0] <= om.imag <= sk.S0_Y[1]
                and all(abs(om - z) > 1e-6 for z in out)):
            out.append(om)
    return out

def pole_vk(rho, k):
    f = lambda om: GK(om, k, rho)  # noqa: E731
    in_A = lambda om: (abs(om) < sk.R_A) and (om.imag > sk.Y_A)  # noqa: E731
    in_S = lambda om: (sk.S_X[0] <= om.real <= sk.S_X[1]) and (sk.S_Y[0] <= om.imag <= sk.S_Y[1])  # noqa: E731
    zt = {}
    t0 = time.time()
    zA = sk.zaehle(f, sk.stuecke_A())
    zS = sk.zaehle(f, sk.stuecke_rechteck(sk.S_X[0], sk.S_X[1], sk.S_Y[0], sk.S_Y[1]))
    zS0 = sk.zaehle(f, sk.stuecke_rechteck(sk.S_X[0], sk.S_X[1], sk.S0_Y[0], sk.S0_Y[1]))
    zt["zaehlung"] = round(time.time() - t0, 1)
    t0 = time.time()
    nA, kA = suche_kurz(f, np.arange(-10.0, 10.0001, 0.1), np.arange(sk.Y_A, 10.0001, 0.1),
                        lambda W: (np.abs(W) < sk.R_A) & (W.imag > sk.Y_A), in_A)
    zt["suche_A"] = round(time.time() - t0, 1)
    t0 = time.time()
    nS, kS = suche_kurz(f, np.arange(sk.S_X[0], sk.S_X[1] + 1e-9, 0.01), np.arange(sk.S_Y[0], sk.S_Y[1] + 1e-9, 0.01),
                        lambda W: np.ones(W.shape, dtype=bool), in_S)
    zt["suche_S"] = round(time.time() - t0, 1)
    t0 = time.time()
    nS0 = suche_S0_GK(f)
    zt["suche_S0"] = round(time.time() - t0, 1)
    t0 = time.time()
    pol = {"A": len(nA) - zA["zahl"], "S": len(nS) - zS["zahl"], "S0": len(nS0) - zS0["zahl"]}
    w0 = float(np.sqrt(k * k + M * M))
    resid = {}
    for e in (1e-3, 1e-4, 1e-5):
        R = complex(-2.0 * w0 * 1j * e * f(w0 + 1j * e)[0])
        resid[f"{e:g}"] = [R.real, R.imag, abs(R - 1.0)]
    zI, rI = newton_kurz(lambda om: 1.0 / f(om), w0 + 0.001j, iters=60, ymin=-1e-3)
    th = np.linspace(0.001, np.pi - 0.001, 2001)
    bogen = {str(R): float(np.abs(f(R * np.exp(1j * th))).max()) for R in (10.0, 20.0)}
    pk = np.array([w0 + 1e-3j, w0 + 0.05j, 0.3 + 0.5j, 3.0 + 1.0j, 7.0 + 5.0j])
    quad = float(np.max(np.abs(f(pk) - GK(pk, k, rho, 256)) / np.abs(f(pk))))
    zt["rest"] = round(time.time() - t0, 1)
    return {"variante": "VK-Ziel", "rho": rho, "k": k, "zaehlung_A": zA, "zaehlung_S": zS, "zaehlung_S0": zS0,
            "nullstellen_A": [[z.real, z.imag] for z in nA], "nullstellen_S": [[z.real, z.imag] for z in nS],
            "nullstellen_S0": [[z.real, z.imag] for z in nS0], "kandidaten_gitter": {"A": kA, "S": kS}, "pole": pol,
            "alle_stabil": bool(zA["stabil"] and zS["stabil"] and zS0["stabil"]),
            "omega_0": w0, "residuum_probe": resid,
            "newton_auf_1_durch_G": {"omega_re": zI.real, "omega_im": zI.imag, "residuum": rI},
            "max_abs_G_bogen": bogen, "quadratur_128_256_rel_max": quad, "zeiten_s": zt}


def modus_pole(ordner, rhos, datei="pole-VK.json"):
    t0 = time.time()
    out = {"modus": "pole", "rhos": rhos, "ks": KS, "R_A": sk.R_A, "Y_A": sk.Y_A, "S_X": sk.S_X, "S_Y": sk.S_Y,
           "S0_Y": sk.S0_Y, "probe_windung": sk.probe_windung(), "ergebnisse": {}}
    for r in rhos:
        for k in KS:
            tt = time.time()
            e = pole_vk(r, k)
            e["zeit_s"] = round(time.time() - tt, 1)
            out["ergebnisse"][f"VK_rho{r:g}_k{k:.4f}"] = e
            print(json.dumps({"fertig": f"VK_rho{r:g}_k{k:.4f}", "zeit_s": e["zeit_s"]}), flush=True)
    out.update({"zeit_gesamt_s": round(time.time() - t0, 1), "skript_sha256": SKRIPT_SHA,
                "kernmasse_feld_sha256": kf.SKRIPT_SHA, "schicht2_kont_sha256": sk.SKRIPT_SHA,
                "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
    with open(os.path.join(ordner, datei), "w") as fh:
        json.dump(out, fh, indent=1, default=str)


# ---------- Modus erwartung (direkte Faltung im Ortsraum) ----------
def richtungen(nmu, nph):
    mu, wmu = kc.gl(-1.0, 1.0, nmu)
    ph = 2 * np.pi * np.arange(nph) / nph
    st = np.sqrt(1 - mu ** 2)
    nx = (st[:, None] * np.cos(ph)[None, :]).ravel()
    ny = (st[:, None] * np.sin(ph)[None, :]).ravel()
    nz = np.repeat(mu, nph)
    wom = np.repeat(wmu, nph) * (2 * np.pi / nph)
    return nx, ny, nz, wom


def faltung_kerne(p, c, kerne, tc, ns=96, ntau=32, nmu=64, nph=64):
    """E(x) = int_0^smax ds int_0^s dtau tau r g(tau) int dOmega J(t - s, x - r n), r = sqrt(s^2 - tau^2), fuer mehrere
    Kerne g zugleich; gekappte Quelle (kc.quelle_pkt, kappe = True)."""
    tp, xp, yp, zp = p
    smax = tp + kd.R_S
    sl, wl = [], []
    for a_, b_ in [(0.0, smax / 3), (smax / 3, 2 * smax / 3), (2 * smax / 3, smax)]:
        s_, w_ = kc.gl(a_, b_, ns // 3)
        sl.append(s_)
        wl.append(w_)
    s = np.concatenate(sl)
    ws = np.concatenate(wl)
    nx, ny, nz, wom = richtungen(nmu, nph)
    out = np.zeros(len(kerne), dtype=np.complex128)
    for si, wsi in zip(s, ws):
        t1 = min(si, tc)
        ta, wa = kc.gl(0.0, t1, ntau)
        if si > t1 + 1e-12:
            tb, wb = kc.gl(t1, si, ntau)
            tau = np.concatenate([ta, tb])
            wt = np.concatenate([wa, wb])
        else:
            tau, wt = ta, wa
        r = np.sqrt(np.maximum(si * si - tau * tau, 0.0))
        Jm = kc.quelle_pkt(tp - si, xp - r[:, None] * nx[None, :], yp - r[:, None] * ny[None, :],
                           zp - r[:, None] * nz[None, :], c, True)
        A = Jm @ wom
        basis = wsi * wt * tau * r * A
        for ik, g in enumerate(kerne):
            out[ik] += np.sum(basis * g(tau))
    return out


def modus_erwartung(ordner, rhos, kontrolle, name):
    """E[phi_K] (Ziel und Realisierung) an 9 Pruefpunkten und 19 Achsenpunkten je Konfiguration; mit kontrolle = 1
    zusaetzlich das Ziel bei rho = 1e6 gegen kc.faltung (gekapptes Kontinuum) und eine feinere Quadratur bei min(rhos)."""
    t0 = time.time()
    pp = kd.pruefpunkte()[:, :9]
    pa = sk.achsenpunkte()
    allp = np.concatenate([pp, pa], axis=1)              # (NC, 9 + 19, 4)
    npkt = allp.shape[1]
    quad_kappe = np.zeros((kd.NC, 9), dtype=np.complex128)
    for c in range(kd.NC):
        for i in range(9):
            quad_kappe[c, i] = kc.faltung(*pp[c, i], c, True)
    print(json.dumps({"faltung_s": round(time.time() - t0, 1)}), flush=True)
    E = {}
    real_fehler = {}
    liste = list(rhos) + ([1e6] if kontrolle else [])
    for rho in liste:
        tc = tau_c(rho)
        kerne = [lambda tau, r=rho: g_ziel(tau, r)]
        if rho < 1e5:
            spl, tb = tbar_spline(rho)
            kerne.append(g_real_fun(rho, spl))
            tz = TAU_TAB
            Tz = kf.T_sigma(tz ** 2, rho)
            real_fehler[f"rho{rho:g}"] = {"max_abs_tbar_minus_T": float(np.abs(tb - Tz).max()),
                                          "tau_bei_max": float(tz[np.argmax(np.abs(tb - Tz))]),
                                          "max_abs_T": float(np.abs(Tz).max()),
                                          "max_abs_diff_tau_ab_1": float(np.abs(tb - Tz)[tz >= 1.0].max()),
                                          "max_abs_diff_tau_ab_3": float(np.abs(tb - Tz)[tz >= 3.0].max()),
                                          "a": float(kd.a_hop(rho))}
            fz = {}
            for Z in (2.0, 3.0, 5.0):
                gz = ft_reell(kerne[0], Z, rho, tau_max=7.6)
                gr = ft_reell(kerne[1], Z, rho, tau_max=7.6)
                fz[f"Z{Z:g}"] = {"ziel": gz, "realisierung": gr, "rel_abw": abs(gr - gz) / abs(gz)}
            real_fehler[f"rho{rho:g}"]["fourier_reell"] = fz
        arr = np.zeros((len(kerne), kd.NC, npkt), dtype=np.complex128)
        for c in range(kd.NC):
            for i in range(npkt):
                arr[:, c, i] = faltung_kerne(allp[c, i], c, kerne, tc)
        E[f"ziel_rho{rho:g}"] = arr[0]
        if len(kerne) > 1:
            E[f"real_rho{rho:g}"] = arr[1]
        print(json.dumps({"erwartung_rho": rho, "zeit_s": round(time.time() - t0, 1)}), flush=True)
    kontrollen = {}
    if kontrolle:
        r0 = min(rhos)
        spl0, _ = tbar_spline(r0)
        k0 = [lambda tau: g_ziel(tau, r0), g_real_fun(r0, spl0)]
        fein = np.array([faltung_kerne(pp[0, i], 0, k0, tau_c(r0), ns=144, ntau=48, nmu=96, nph=96)
                         for i in range(9)]).T
        grob = np.stack([E[f"ziel_rho{r0:g}"][0, :9], E[f"real_rho{r0:g}"][0, :9]])
        rel6 = np.abs(E["ziel_rho1e+06"][:, :9] - quad_kappe) / np.abs(quad_kappe)
        kontrollen = {"quadratur_fein_gegen_grob_rel_max": float(np.max(np.abs(fein - grob) / np.abs(grob))),
                      "quadratur_rho": r0,
                      "ziel_rho1e6_gegen_faltung_rel": rel6.tolist(),
                      "ziel_rho1e6_gegen_faltung_rel_max": float(rel6.max())}
    np.savez_compressed(os.path.join(ordner, f"erwartung-VK-{name}.npz"), pruefpunkte=pp, achsenpunkte=pa,
                        quad_kappe=quad_kappe, **{f"E_{key}": a for key, a in E.items()})
    kopf = {"modus": "erwartung", "rhos": rhos, "kontrolle": bool(kontrolle), "kontrollen": kontrollen,
            "realisierungsfehler": real_fehler, "zeit_gesamt_s": round(time.time() - t0, 1), "skript_sha256": SKRIPT_SHA,
            "kernmasse_feld_sha256": kf.SKRIPT_SHA, "kontinuum4d_sha256": kc.SKRIPT_SHA,
            "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    with open(os.path.join(ordner, f"erwartung-VK-{name}.json"), "w") as fh:
        json.dump(kopf, fh, indent=1, default=str)
    print(json.dumps({"zeit_gesamt_s": kopf["zeit_gesamt_s"], "kontrollen_max": {k: v for k, v in kontrollen.items()
                                                                                if not isinstance(v, list)}}), flush=True)


def main():
    modus, ordner = sys.argv[1], sys.argv[2]
    rhos = [float(x) for x in sys.argv[3].split(",")]
    os.makedirs(ordner, exist_ok=True)
    if modus == "kern":
        modus_kern(ordner, rhos)
    elif modus == "pole":
        modus_pole(ordner, rhos, sys.argv[4] if len(sys.argv) > 4 else "pole-VK.json")
    elif modus == "erwartung":
        modus_erwartung(ordner, rhos, int(sys.argv[4]), sys.argv[5])


if __name__ == "__main__":
    main()
