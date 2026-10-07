"""KAUSAL-WELLE-4D: Kontinuum, Johnston-Erwartung bei endlicher Dichte, erwartete Linkzahl (KV0).

1) Kontinuum exakt im k-Raum (ungekappte Quelle): (Box + m^2) phi = J [S: Johnston (3.17), (3.18)], je Mode
   phi_k(t) = int_{-inf}^t sin(w (t - t'))/w J_k(t') dt' (Duhamel), w = sqrt(k^2 + m^2),
   J_k(t) = g(t) e^{-i om t} h(k), h(k) = (2 pi s^2)^{3/2} exp(-s^2 |k - p|^2/2), g(t) = exp(-t^2/(2 s^2)):
   phi_k(t) = h/(2 i w) [e^{i w t} I(t; om + w) - e^{-i w t} I(t; om - w)], I(t; W) = int_{-inf}^t g e^{-i W t'} (Faddeeva).
   phi(t, x) = (2 pi)^-2 int dk_z e^{i k_z z} int k_p dk_p J0(k_p r_p) phi_k (Achsensymmetrie um z).
2) Direkte Faltung mit K_m^(4) = (1/2pi) delta(tau^2) - (m/4pi) J1(m tau)/tau [S: (3.25)] am Pruefpunkt, Gauss-Legendre in
   (s, u, cos theta) und Trapez in phi; gekappte Quelle (r4 <= R_S, wie auf der Kausalmenge) und ungekappt.
3) Johnston-Erwartung bei endlichem rho [M]: E[phi] = K_P * J mit K_P~ = a mu~/(1 - a b rho mu~) [S: (3.32), (3.44)],
   a mu~(Z) = (4 pi a/Z) int tau^2 e^{-c tau^4} K1(Z tau) d tau, c = pi rho/24, Z = sqrt(|k|^2 - omega^2) (Re Z > 0),
   omega auf der Geraden Im omega = Gamma ueber allen Singularitaeten; zwei Gamma als Gegenprobe; rho -> inf ergibt
   1/(Z^2 + m^2) (dritter Weg zum Kontinuum).
4) Erwartete Linkzahl je Element fuer D [M]: E[L]/E[N] = (1/V_D) int_D d^4x (6/pi) int dOmega int dchi sinh^2 chi
   (1 - exp(-c tau_max^4)), tau_max = Austritt des Strahls x - tau (cosh chi, sinh chi n) aus J+(B).

Aufruf (nur ueber kleintest.sh): kontinuum4d.py <ausgabeordner> <rho1,rho2,...>
"""
import hashlib
import json
import os
import sys
import time

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import j0, j1, kv, wofz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kausal4d as kd  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
SQ2 = np.sqrt(2.0)
S = kd.SIGMA
M = kd.MASSE
KB = 9.0 / S


def gl(a, b, n):
    g, w = np.polynomial.legendre.leggauss(n)
    return 0.5 * (b - a) * g + 0.5 * (b + a), 0.5 * (b - a) * w


def I_int(t, W, s):
    t = np.asarray(t, dtype=float)
    W = np.asarray(W, dtype=float)
    with np.errstate(all="ignore"):
        pre = s * np.sqrt(np.pi / 2.0) * np.exp(-t ** 2 / (2 * s * s) - 1j * W * t)
        a = pre * wofz((W * s * s - 1j * t) / (s * SQ2))
        b = s * np.sqrt(2 * np.pi) * np.exp(-W ** 2 * s * s / 2.0) - pre * wofz((1j * t - W * s * s) / (s * SQ2))
    return np.where(t <= 0, a, b)


def k_knoten(c, nkp=128, nkz=192):
    kp, wp = gl(0.0, KB, nkp)
    kz, wz = gl(kd.PP[c] - KB, kd.PP[c] + KB, nkz)
    return kp, wp, kz, wz


def h3(kp, kz, c):
    return (2 * np.pi * S * S) ** 1.5 * np.exp(-S * S * (kp[None, :] ** 2 + (kz[:, None] - kd.PP[c]) ** 2) / 2.0)


def phik(t, kp, kz, c):
    """(nkz, nkp) Modenamplituden zur Zeit t (Duhamel, exakt)."""
    w = np.sqrt(kp[None, :] ** 2 + kz[:, None] ** 2 + M * M)
    h = h3(kp, kz, c)
    om = kd.OM[c]
    return h / (2j * w) * (np.exp(1j * w * t) * I_int(t, om + w, S) - np.exp(-1j * w * t) * I_int(t, om - w, S))


def feld_k(F, kp, wp, kz, wz, rp, z):
    """phi an Punkten (rp, z) aus Modenfeld F (nkz, nkp)."""
    A = np.exp(1j * z[:, None] * kz[None, :]) * wz[None, :]          # (n, nkz)
    G = A @ F                                                          # (n, nkp)
    B = j0(rp[:, None] * kp[None, :]) * (kp * wp)[None, :]
    return (G * B).sum(axis=1) / (2 * np.pi) ** 2


def kontinuum_punkte(pp, c):
    kp, wp, kz, wz = k_knoten(c)
    out = np.zeros(pp.shape[0], dtype=np.complex128)
    for tt in np.unique(pp[:, 0]):
        sel = pp[:, 0] == tt
        F = phik(tt, kp, kz, c)
        rp = np.sqrt(pp[sel, 1] ** 2 + pp[sel, 2] ** 2)
        out[sel] = feld_k(F, kp, wp, kz, wz, rp, pp[sel, 3])
    return out


def kontinuum_norm(c, nt=6, nr=48, nmu=48):
    """n_c,k = (1/w) int_Scheibe dt int_{|x| <= T_TOP - t} |phi|^2 d^3x, k = 0..N_SCHEIBEN-1."""
    kp, wp, kz, wz = k_knoten(c)
    mu, wmu = gl(-1.0, 1.0, nmu)
    out = np.zeros(kd.N_SCHEIBEN)
    for k in range(kd.N_SCHEIBEN):
        ta = kd.SCHEIBE_T0 + k * kd.SCHEIBE_W
        tn, wt = gl(ta, ta + kd.SCHEIBE_W, nt)
        acc = 0.0
        for tt, w_t in zip(tn, wt):
            Rt = kd.T_TOP - tt
            r, wr = gl(0.0, Rt, nr)
            R, MU = np.meshgrid(r, mu, indexing="ij")
            W = (2 * np.pi * R ** 2) * np.outer(wr, wmu)
            rp = (R * np.sqrt(1 - MU ** 2)).ravel()
            z = (R * MU).ravel()
            F = phik(tt, kp, kz, c)
            ph = feld_k(F, kp, wp, kz, wz, rp, z)
            acc += w_t * float((np.abs(ph) ** 2 * W.ravel()).sum())
        out[k] = acc / kd.SCHEIBE_W
    return out


def quelle_pkt(t, x, y, z, c, kappe):
    r2 = t * t + x * x + y * y + z * z
    J = np.exp(-r2 / (2 * S * S) - 1j * (kd.OM[c] * t - kd.PP[c] * z))
    if kappe:
        J = J * (r2 <= kd.R_S ** 2)
    return J


def faltung(tp, xp, yp, zp, c, kappe, ns=96, nu=32, nmu=64, nph=64):
    """Direkte Faltung am Punkt: delta-Anteil (Lichtkegel) und Bessel-Anteil (Inneres)."""
    smax = tp + (kd.R_S if kappe else 7.0 * S)
    # s in drei Stuecken
    s_list, ws_list = [], []
    for a_, b_ in [(0.0, smax / 3), (smax / 3, 2 * smax / 3), (2 * smax / 3, smax)]:
        s_, w_ = gl(a_, b_, ns // 3)
        s_list.append(s_)
        ws_list.append(w_)
    s = np.concatenate(s_list)
    ws = np.concatenate(ws_list)
    u, wu = gl(0.0, 1.0, nu)
    mu, wmu = gl(-1.0, 1.0, nmu)
    ph = 2 * np.pi * np.arange(nph) / nph
    wph = 2 * np.pi / nph
    st = np.sqrt(1 - mu ** 2)
    nx = (st[:, None] * np.cos(ph)[None, :]).ravel()
    ny = (st[:, None] * np.sin(ph)[None, :]).ravel()
    nz = np.repeat(mu, nph)
    wom = np.repeat(wmu, nph) * wph
    # delta-Anteil: (1/4pi) int s ds dOmega J(t - s, x - s n)
    Jd = quelle_pkt(tp - s[:, None], xp - s[:, None] * nx[None, :], yp - s[:, None] * ny[None, :],
                    zp - s[:, None] * nz[None, :], c, kappe)
    phi_d = (1 / (4 * np.pi)) * np.sum(ws[:, None] * s[:, None] * wom[None, :] * Jd)
    # Bessel-Anteil: -(m/4pi) int ds s^3 int du u^2 [J1(m tau)/tau] int dOmega J(t - s, x - s u n), tau = s sqrt(1-u^2)
    phi_b = 0.0 + 0.0j
    for i in range(s.size):
        si = s[i]
        tau = si * np.sqrt(1 - u ** 2)
        xx = M * tau
        kern = np.where(xx < 1e-8, 0.5 * M, M * j1(np.maximum(xx, 1e-300)) / np.maximum(xx, 1e-300))
        ru = si * u
        J = quelle_pkt(tp - si, xp - ru[:, None] * nx[None, :], yp - ru[:, None] * ny[None, :],
                       zp - ru[:, None] * nz[None, :], c, kappe)
        inner = (J * wom[None, :]).sum(axis=1)
        phi_b += ws[i] * si ** 3 * np.sum(wu * u ** 2 * kern * inner)
    phi_b *= -(M / (4 * np.pi))
    return complex(phi_d + phi_b)


# ---------- Johnston-Erwartung bei endlichem rho ----------
def amu(Z, rho, ntau=64):
    """a mu~(Z) = (4 pi a/Z) int tau^2 exp(-c tau^4) K1(Z tau) dtau, c = pi rho/24."""
    a = kd.a_hop(rho)
    c = np.pi * rho / 24.0
    tmax = (40.0 / c) ** 0.25
    tau, wt = gl(0.0, tmax, ntau)
    Zt = Z[..., None] * tau
    integ = (wt * tau ** 2 * np.exp(-c * tau ** 4)) * kv(1, Zt)
    return (4 * np.pi * a / Z) * integ.sum(axis=-1)


def F_rho(om, k, rho):
    """(nom, nk): retardierter Erwartungspropagator K_P~ (rho = inf: 1/(Z^2 + m^2))."""
    Z2 = k[None, :] ** 2 - om[:, None] ** 2
    if not np.isfinite(rho):
        return 1.0 / (Z2 + M * M)
    Z = np.sqrt(Z2)
    Z = np.where(Z.real < 0, -Z, Z)
    out = np.zeros(Z.shape, dtype=np.complex128)
    for i in range(Z.shape[0]):
        km = amu(Z[i], rho)
        out[i] = km / (1.0 + M * M * km)
    return out


def johnston_punkte(pp, c, rho, Gam, dom=0.05, dk=0.1):
    kp, wp, kz, wz = k_knoten(c)
    om_r = kd.OM[c] + np.arange(-int(round(9.0 / S / dom)), int(round(9.0 / S / dom)) + 1) * dom
    om = om_r + 1j * Gam
    kmax = np.sqrt(KB ** 2 + (abs(kd.PP[c]) + KB) ** 2) + 0.2
    kg = np.arange(0.0, kmax + dk, dk)
    Fg = F_rho(om, kg, rho)
    spl_r = CubicSpline(kg, Fg.real, axis=1)
    spl_i = CubicSpline(kg, Fg.imag, axis=1)
    kn = np.sqrt(kp[None, :] ** 2 + kz[:, None] ** 2).ravel()
    Fn = (spl_r(kn) + 1j * spl_i(kn))                                  # (nom, nkz*nkp)
    h = h3(kp, kz, c).ravel()
    Jt = S * np.sqrt(2 * np.pi) * np.exp(-S * S * (om - kd.OM[c]) ** 2 / 2.0)
    rp = np.sqrt(pp[:, 1] ** 2 + pp[:, 2] ** 2)
    z = pp[:, 3]
    A = (np.exp(1j * z[:, None] * kz[None, :]) * wz[None, :])          # (n, nkz)
    B = j0(rp[:, None] * kp[None, :]) * (kp * wp)[None, :]             # (n, nkp)
    P = (A[:, :, None] * B[:, None, :]).reshape(pp.shape[0], -1)       # (n, nkz*nkp)
    MK = (Fn * h[None, :]) @ P.T / (2 * np.pi) ** 2                    # (nom, n)
    ph = np.exp(-1j * om[:, None] * pp[None, :, 0]) * (Jt * dom / (2 * np.pi))[:, None]
    return (ph * MK).sum(axis=0)


def pol_k(rho, k, om0):
    """Nullstelle von 1 + m^2 a mu~ in omega (Newton, numerische Ableitung) bei festem |k|."""
    def g(om):
        Z = np.sqrt(np.array([k * k - om * om], dtype=np.complex128))
        Z = np.where(Z.real < 0, -Z, Z)
        return 1.0 + M * M * amu(Z, rho, ntau=96)[0]
    om = complex(om0) + 0.05j
    for _ in range(60):
        f = g(om)
        h = 1e-6
        d = (g(om + h) - f) / h
        st = f / d
        om -= st
        if abs(st) < 1e-12:
            break
    return om, abs(g(om))


# ---------- erwartete Linkzahl ----------
def tau_max(t, r, ch, sh, mu):
    """Austritt aus J+(B) entlang x - tau (cosh, sinh n); Felder gleicher Form, Bisektion."""
    lo = np.zeros(np.broadcast(t, ch, mu).shape)
    hi = (t + kd.R_S) / ch * (1 + 1e-12) + 1e-12 + lo
    for _ in range(55):
        mid = 0.5 * (lo + hi)
        ty = t - mid * ch
        ry = np.sqrt(np.maximum(r * r - 2 * r * mid * sh * mu + (mid * sh) ** 2, 0.0))
        ok = ty >= kd.f_unten(ry)
        lo = np.where(ok, mid, lo)
        hi = np.where(ok, hi, mid)
    return lo


def linkzahl_erwartung(rhos, nt=8, nr=24, nchi=60, nmu=24):
    """E[L]/E[N] je rho und Erwartung je Zeitklasse (Vergangenheitslinks je Element)."""
    kk = kd.R_S / SQ2
    tc = 0.5 * (kd.T_TOP - SQ2 * kd.R_S)
    kanten = sorted(set([kd.LZ_T0 + kd.LZ_W * i for i in range(kd.LZ_N + 1)] + [-kk, tc]))
    chi_l, wchi_l = [], []
    for a_ in range(7):
        x_, w_ = gl(2.0 * a_, 2.0 * a_ + 2.0, nchi // 6 if a_ < 6 else nchi // 6)
        chi_l.append(x_)
        wchi_l.append(w_)
    chi = np.concatenate(chi_l)
    wchi = np.concatenate(wchi_l)
    mu, wmu = gl(-1.0, 1.0, nmu)
    CH = np.cosh(chi)[:, None]
    SH = np.sinh(chi)[:, None]
    WI = (wchi * np.sinh(chi) ** 2)[:, None] * wmu[None, :] * 2 * np.pi
    zaehl = {r: 0.0 for r in rhos}
    vol = 0.0
    klasse_z = {r: np.zeros(kd.LZ_N) for r in rhos}
    klasse_v = np.zeros(kd.LZ_N)
    for ia in range(len(kanten) - 1):
        ta, tb = kanten[ia], kanten[ia + 1]
        if tb - ta < 1e-12:
            continue
        tn, wt = gl(ta, tb, nt)
        for tt, w_t in zip(tn, wt):
            rp = np.sqrt(max(kd.R_S ** 2 - tt ** 2, 0.0)) if tt <= -kk else tt + SQ2 * kd.R_S
            rD = min(rp, kd.T_TOP - tt)
            if rD <= 0:
                continue
            rn, wr = gl(0.0, rD, nr)
            kl = min(int(np.floor((tt - kd.LZ_T0) / kd.LZ_W)), kd.LZ_N - 1)
            for rr, w_r in zip(rn, wr):
                tm = tau_max(tt, rr, CH, SH, mu[None, :])
                wv = w_t * w_r * 4 * np.pi * rr * rr
                vol += wv
                klasse_v[kl] += wv
                for rho in rhos:
                    cc = np.pi * rho / 24.0
                    inner = (6.0 / np.pi) * float((WI * (1.0 - np.exp(-cc * tm ** 4))).sum())
                    zaehl[rho] += wv * inner
                    klasse_z[rho][kl] += wv * inner
    return ({str(r): zaehl[r] / vol for r in rhos}, vol,
            {str(r): (klasse_z[r] / np.maximum(klasse_v, 1e-300)).tolist() for r in rhos}, klasse_v.tolist())


def main():
    ordner = sys.argv[1]
    rhos = [float(x) for x in sys.argv[2].split(",")]
    os.makedirs(ordner, exist_ok=True)
    t00 = time.time()
    pp = kd.pruefpunkte()
    npkt = pp.shape[1]
    phi_k = np.zeros((kd.NC, npkt), dtype=np.complex128)
    quad_kappe = np.zeros((kd.NC, 9), dtype=np.complex128)
    quad_frei = np.zeros((kd.NC, 9), dtype=np.complex128)
    quad_frei_fein = np.zeros((kd.NC, 9), dtype=np.complex128)
    norm_c = np.zeros((kd.NC, kd.N_SCHEIBEN))
    zeiten = {}
    for c in range(kd.NC):
        tc = time.time()
        phi_k[c] = kontinuum_punkte(pp[c], c)
        norm_c[c] = kontinuum_norm(c)
        zeiten[f"k_raum_c{c}"] = round(time.time() - tc, 1)
        tc = time.time()
        for i in range(9):
            tp, xp, yp, zp = pp[c, i]
            quad_kappe[c, i] = faltung(tp, xp, yp, zp, c, True)
            quad_frei[c, i] = faltung(tp, xp, yp, zp, c, False)
            if i in (0, 3, 6):
                quad_frei_fein[c, i] = faltung(tp, xp, yp, zp, c, False, ns=144, nu=48, nmu=96, nph=96)
            else:
                quad_frei_fein[c, i] = quad_frei[c, i]
        zeiten[f"faltung_c{c}"] = round(time.time() - tc, 1)
        print(json.dumps({"c": c, "zeiten": zeiten}), flush=True)
    # Johnston-Erwartung und Konturweg zum Kontinuum
    gams = (0.8, 1.4)
    rho_liste = list(rhos) + [1e6, np.inf]
    jo = np.zeros((len(rho_liste), len(gams), kd.NC, npkt), dtype=np.complex128)
    tc = time.time()
    for ir, rho in enumerate(rho_liste):
        for ig, G in enumerate(gams):
            for c in range(kd.NC):
                jo[ir, ig, c] = johnston_punkte(pp[c], c, rho, G)
        print(json.dumps({"johnston_rho": str(rho), "zeit_s": round(time.time() - tc, 1)}), flush=True)
    zeiten["johnston"] = round(time.time() - tc, 1)
    # Pole (Wachstumsrate der Erwartung) bei k = 0 und k = p(eta = 0.5)
    pole = {}
    for rho in rhos:
        for k in (0.0, float(kd.PP[1])):
            om, res = pol_k(rho, k, np.sqrt(k * k + M * M))
            pole[f"rho{rho:g}_k{k:.4f}"] = {"omega_re": om.real, "omega_im": om.imag, "residuum": res}
    print(json.dumps(pole), flush=True)
    # erwartete Linkzahl, zwei Aufloesungen
    tc = time.time()
    lz, vol, lz_kl, vol_kl = linkzahl_erwartung(rhos)
    zeiten["linkzahl"] = round(time.time() - tc, 1)
    tc = time.time()
    lz_f, vol_f, _, _ = linkzahl_erwartung(rhos, nt=12, nr=36, nchi=90, nmu=36)
    zeiten["linkzahl_fein"] = round(time.time() - tc, 1)
    np.savez_compressed(os.path.join(ordner, "kontinuum.npz"), pruefpunkte=pp, phi_k=phi_k, quad_kappe=quad_kappe,
                        quad_frei=quad_frei, quad_frei_fein=quad_frei_fein, norm_c=norm_c, johnston=jo,
                        johnston_rhos=np.array(rho_liste), johnston_gammas=np.array(gams))
    rel = lambda a, b: (np.abs(a - b) / np.abs(b)).tolist()  # noqa: E731
    kopf = {"modus": "kontinuum", "rhos": rhos, "V_D_quadratur": vol, "V_D_quadratur_fein": vol_f,
            "V_D_grob": kd.volumen_D_grob(), "linkzahl_erwartung": lz, "linkzahl_erwartung_fein": lz_f,
            "linkzahl_erwartung_zeitklassen": lz_kl, "volumen_zeitklassen": vol_kl,
            "quad_frei_gegen_k_raum_rel": rel(quad_frei, phi_k[:, :9]),
            "quad_frei_fein_gegen_k_raum_rel": rel(quad_frei_fein, phi_k[:, :9]),
            "kappe_effekt_rel": rel(quad_kappe, quad_frei_fein),
            "kontur_inf_gegen_k_raum_rel": [rel(jo[-1, g], phi_k) for g in range(len(gams))],
            "johnston_1e6_gegen_k_raum_rel_max": [float(np.max(rel(jo[-2, g], phi_k))) for g in range(len(gams))],
            "johnston_gamma_gegenprobe_rel_max": {str(r): float(np.max(rel(jo[i, 0], jo[i, 1])))
                                                  for i, r in enumerate(rho_liste)},
            "pole": pole, "norm_c": norm_c.tolist(), "zeiten": zeiten, "zeit_gesamt_s": round(time.time() - t00, 1),
            "skript_sha256": SKRIPT_SHA, "kausal4d_sha256": kd.SKRIPT_SHA,
            "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    with open(os.path.join(ordner, "kontinuum.json"), "w") as fh:
        json.dump(kopf, fh, indent=1, default=str)
    print(json.dumps({k: kopf[k] for k in ("V_D_quadratur", "V_D_grob", "linkzahl_erwartung", "linkzahl_erwartung_fein",
                                            "zeit_gesamt_s")}), flush=True)


if __name__ == "__main__":
    main()
