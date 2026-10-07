# -*- coding: utf-8 -*-
"""netzgpu, Licht: Nachweis c = 1 (Bloch-Reduktion des Ortsraum-Operators) und Demo 2 (Lichtpuls an einer Masse).

Aufruf (nur ueber kleintest.sh auf der .69):
  python lauf_licht.py nachweis <aus.json>
  python lauf_licht.py demo <datensatz-ordner> <aus.json> [nx ny nz] [phi_min] [bilder]
"""
import json
import math
import sys
import time

import numpy as np
import torch

sys.path.insert(0, '/home/fmh/fmhc-physics-remote/netz-gpu/code')
from netzgpu import FASSUNG, diagnose, kopplung, licht  # noqa: E402
from netzgpu.datensatz import Datensatz, platte_frei_gb  # noqa: E402
from netzgpu.netz import Netz  # noqa: E402

T0 = time.time()


def log(*a):
    print('[%7.1f s]' % (time.time() - T0), *a, flush=True)


def schreibe(p, obj):
    obj['_meta'] = {'argv': sys.argv, 'torch': torch.__version__, 'gpu': torch.cuda.get_device_name(0),
                    'laufzeit_s': time.time() - T0, 'gpu_speicher_max_MB': torch.cuda.max_memory_allocated() / 1e6,
                    'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'fassung': FASSUNG}
    with open(p + '.tmp', 'w') as f:
        json.dump(obj, f, indent=1)
    import os
    os.replace(p + '.tmp', p)
    log('->', p)


def nachweis(aus):
    res = {}
    for gew in ('mitte', 'null'):
        N = Netz('V', (2, 2, 2), gewichte='mitte' if gew == 'mitte' else np.zeros(1))
        if gew == 'null':
            N.w = torch.zeros(N.N_e, dtype=N.dtype, device=N.device)
        st = N.sterne()
        p = N.pruefung(st)
        R = diagnose.richtungen(60)
        tab = {}
        for kk in (0.005, 0.01, 0.02, 0.04):
            c2, herm = diagnose.licht_tempo(N, st, R * kk)
            s2 = diagnose.skalar_tempo(N, st, R * kk)
            tab[kk] = (c2.cpu().numpy(), s2.cpu().numpy(), herm)
        # Extrapolation k -> 0 (Richardson in k^2 aus 0,01 und 0,02)
        c0 = (4 * tab[0.01][0][:, :2] - tab[0.02][0][:, :2]) / 3.0
        s0 = (4 * tab[0.01][1][:, :1] - tab[0.02][1][:, :1]) / 3.0
        r = {'pruefung': p,
             'licht_c_k0.01_abw_max': float(np.abs(np.sqrt(tab[0.01][0][:, :2]) - 1).max()),
             'licht_c_k0.005_abw_max': float(np.abs(np.sqrt(tab[0.005][0][:, :2]) - 1).max()),
             'licht_c_extrapoliert_abw_max': float(np.abs(np.sqrt(c0) - 1).max()),
             'licht_c_extrapoliert_spanne': float(np.sqrt(c0).max() - np.sqrt(c0).min()),
             'licht_dritter_eigenwert_rel_k0.01': float(tab[0.01][0][:, 2].min()),
             'licht_herm_rest': float(tab[0.01][2]),
             'licht_c_k0.04_je_achse': {nm: [float(x) for x in np.sqrt(tab[0.04][0][i, :2])]
                                        for i, nm in enumerate(('100', '110', '111'))},
             'licht_dispersion_k0.04_mittel': float((np.sqrt(tab[0.04][0][:, :2]) - 1).mean() / 0.04 ** 2),
             'skalar_c_extrapoliert_abw_max': float(np.abs(np.sqrt(s0) - 1).max()),
             'skalar_c_k0.01_abw_max': float(np.abs(np.sqrt(tab[0.01][1][:, :1]) - 1).max())}
        # Fensterfit wie im Projekt: c^2(k) = c0^2 + a2 k^2 + a4 k^4 + a6 k^6 je Richtung und Zweig, k = 0,05 .. 0,4 / a
        kf = np.array([0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4])
        Y = np.stack([diagnose.licht_tempo(N, st, R * kk)[0][:, :2].cpu().numpy() for kk in kf], 0)   # (nk, nR, 2)
        Ys = np.stack([diagnose.skalar_tempo(N, st, R * kk)[:, :1].cpu().numpy() for kk in kf], 0)
        Xf = np.stack([kf ** 0, kf ** 2, kf ** 4, kf ** 6], 1)
        coef = np.linalg.lstsq(Xf, Y.reshape(len(kf), -1), rcond=None)[0].reshape(4, -1, 2)
        coefs = np.linalg.lstsq(Xf, Ys.reshape(len(kf), -1), rcond=None)[0].reshape(4, -1, 1)
        c0f = np.sqrt(coef[0])
        r['fenster_licht_c0_abw_max'] = float(np.abs(c0f - 1).max())
        r['fenster_licht_c0_spanne'] = float(c0f.max() - c0f.min())
        r['fenster_licht_a2_mittel_a2'] = float(coef[1].mean())
        r['fenster_licht_a2_spanne_a2'] = float(coef[1].max() - coef[1].min())
        r['fenster_licht_doppelbrechung_a2_max'] = float(np.abs(coef[1][:, 0] - coef[1][:, 1]).max())
        r['fenster_skalar_c0_abw_max'] = float(np.abs(np.sqrt(coefs[0]) - 1).max())
        r['fenster_skalar_a2_mittel_a2'] = float(coefs[1].mean())
        r['hinweis'] = 'a2 in a^2 (k in 1/a); in (k l_P)^2 mal 8 (l_P = a / 2 sqrt 2)'
        res[gew] = r
        log(gew, json.dumps(r))
    schreibe(aus, res)


def demo(ordner, aus, nx=20, ny=12, nz=12, phi_min=-0.12, bilder=36, T=15.0):
    frei = platte_frei_gb()
    log('Platte frei %.1f GB' % frei)
    if frei < 10:
        raise SystemExit('Platte < 10 GB')
    N = Netz('V', (nx, ny, nz))
    log('Netz', N.N_e, N.N_k, N.N_d, N.N_t, 'bau %.2f s' % N.bauzeit_s)
    xc = torch.tensor([nx / 2.0, ny / 2.0, nz / 2.0], dtype=N.dtype, device=N.device)
    m1, st0 = kopplung.gauss_masse(N, xc, 1.0, 1.0)
    phi1, info = kopplung.takt_poisson(N, st0, m1, G=1.0)
    M = phi_min / float(phi1.min())
    phi = phi1 * M
    log('Poisson', info, 'M =', M, 'phi min/max', float(phi.min()), float(phi.max()))
    Nl = 1.0 + phi
    l, w = kopplung.metrik_aus_takt(N, phi)
    L = licht.Licht(N, N=Nl, l=l, w=w)
    L0 = licht.Licht(N)
    log('Sterne gestoert: min *1 %.4g, min *2 %.4g, min *0 %.4g' % (float(L.st['s1'].min()), float(L.st['s2'].min()),
                                                                   float(L.st['s0'].min())))
    wmax = L.omega_max()
    dt = 0.9 * 2.0 / wmax
    nschritt = int(math.ceil(T / bilder / dt))
    dt = T / bilder / nschritt
    log('omega_max %.4f, dt %.5f, Schritte je Bild %d' % (wmax, dt, nschritt))
    # Anfangswelle: Ebene Front (Polarisation z), Huelle in x, laeuft nach +x
    x0, sig, k0 = 3.0, 1.0, math.pi
    def a_feld(x):
        u = x[:, 0] - x0
        env = torch.exp(-0.5 * u * u / sig ** 2)
        f = torch.zeros_like(x)
        f[:, 2] = env * torch.cos(k0 * u)
        return f
    def adot_feld(x):          # -d/dx a  (Welle a(x - t))
        u = x[:, 0] - x0
        env = torch.exp(-0.5 * u * u / sig ** 2)
        f = torch.zeros_like(x)
        f[:, 2] = -(-u / sig ** 2 * env * torch.cos(k0 * u) - k0 * env * torch.sin(k0 * u))
        return f
    A = licht.feld_auf_kanten(N, a_feld)
    P = L.m * licht.feld_auf_kanten(N, adot_feld)
    P, ginfo = L.gauss_projektion(P)
    log('Gauss-Projektion', ginfo, 'Rest', float(L.gauss(P).abs().max()))
    ds = Datensatz(ordner, 'Lichtpuls an einer Masse (Linse), DEC-Maxwell mit Takt und Laengen auf V', N,
                   quelle={'lauf': aus, 'hinweis': 'synthetisch, keine Messdaten; Feld ueberhoeht (Phi_min %.3f)' % phi_min},
                   zeit_einheit='a/c')
    ds.groesse('energie', 'ecke', 1, 'Lichtenergie je Ecke durch *0 (Dichte)', vmin=0.0)
    ds.groesse('takt', 'ecke', 1, 'Lapse N - 1 = Phi (Newton-Takt der Masse, Poisson auf dem Netz)')
    ds.setze('parameter', {'M': M, 'G': 1.0, 'masse_breite': 1.0, 'phi_min': float(phi.min()), 'x_masse': [nx / 2, ny / 2, nz / 2],
                           'welle_x0': x0, 'welle_sigma': sig, 'welle_k0': k0, 'dt': dt, 'schritte_je_bild': nschritt,
                           'gamma': 1.0})
    s0 = L.st['s0']
    E0 = L.energie(A, P)
    tk = []
    for b in range(bilder + 1):
        if b > 0:
            t1 = time.time()
            torch.cuda.synchronize()
            A, P = L.schritt(A, P, dt, nschritt)
            torch.cuda.synchronize()
            tk.append((time.time() - t1) / nschritt)
        e = L.energie_ecke(A, P) / s0
        E = L.energie(A, P)
        g = float(L.gauss(P).abs().max())
        ds.bild(b * nschritt * dt, energie=e, takt=phi)
        ds.diagnose('energie_gesamt', E)
        ds.diagnose('gauss_rest', g)
        if b % 6 == 0:
            log('Bild %d t=%.2f E=%.10g (rel %.2e) gauss %.2e' % (b, b * nschritt * dt, E, E / E0 - 1, g))
    ds.schliessen()
    # Auswertung: Front auf der Achse gegen Rand, Brennpunkt
    e = (L.energie_ecke(A, P) / s0)
    d = N.ecken_minbild(xc)
    ach = (d[:, 1].abs() < 0.6) & (d[:, 2].abs() < 0.6)
    rnd = (d[:, 1].abs() > ny / 2 - 0.6) & (d[:, 2].abs() > nz / 2 - 0.6)
    def schwerpunkt(msk):
        ww = e[msk] * s0[msk]
        xx = N.x[msk, 0]
        return float((ww * xx).sum() / ww.sum())
    x_achse, x_rand = schwerpunkt(ach), schwerpunkt(rnd)
    # Brennpunkt: Maximum der Energiedichte auf der Achse ueber die Bilder (aus den Dateien nicht noetig: letztes Bild)
    res = {'netz': [N.N_e, N.N_k, N.N_d, N.N_t], 'zellen': [nx, ny, nz], 'M': M, 'phi_min': float(phi.min()),
           'poisson': info, 'omega_max': wmax, 'dt': dt, 'schritte': bilder * nschritt,
           'zeit_je_schritt_ms': 1e3 * float(np.median(tk)), 'energie_rel_drift_max': float(
               max(abs(x / E0 - 1) for x in ds.manifest['diagnose']['energie_gesamt'])),
           'gauss_rest_max': float(max(ds.manifest['diagnose']['gauss_rest'])),
           'front_x_achse': x_achse, 'front_x_rand': x_rand, 'verzoegerung_achse_gegen_rand': x_rand - x_achse,
           'datensatz_MB': ds.bytes / 1e6, 'stern_min': [float(L.st['s0'].min()), float(L.st['s1'].min()),
                                                        float(L.st['s2'].min())]}
    log(json.dumps(res))
    schreibe(aus, res)


def shapiro(aus, nx=20, ny=12, nz=12, phi_min=-0.12, T=12.0):
    """Laufzeitprobe ohne Datensatz: Front auf der Achse (durch die Masse) gegen Front am Rand, fuer gamma = 1
    (Takt und Laengen), gamma = 0 (nur Takt) und ohne Masse; Erwartung aus n - 1 = -(1 + gamma) Phi, integriert."""
    N = Netz('V', (nx, ny, nz))
    xc = torch.tensor([nx / 2.0, ny / 2.0, nz / 2.0], dtype=N.dtype, device=N.device)
    m1, st0 = kopplung.gauss_masse(N, xc, 1.0, 1.0)
    phi1, info = kopplung.takt_poisson(N, st0, m1, G=1.0)
    phi = phi1 * (phi_min / float(phi1.min()))
    d = N.ecken_minbild(xc)
    ach = (d[:, 1].abs() < 0.6) & (d[:, 2].abs() < 0.6)
    rnd = (d[:, 1].abs() > ny / 2 - 0.6) & (d[:, 2].abs() > nz / 2 - 0.6)
    x0, sig, k0 = 3.0, 1.0, math.pi
    def a_feld(x):
        u = x[:, 0] - x0
        f = torch.zeros_like(x)
        f[:, 2] = torch.exp(-0.5 * u * u / sig ** 2) * torch.cos(k0 * u)
        return f
    def adot_feld(x):
        u = x[:, 0] - x0
        env = torch.exp(-0.5 * u * u / sig ** 2)
        f = torch.zeros_like(x)
        f[:, 2] = -(-u / sig ** 2 * env * torch.cos(k0 * u) - k0 * env * torch.sin(k0 * u))
        return f
    # Erwartung: Phi entlang x in beiden Roehren gemittelt (Bins 0,25 a), integriert von x0 bis zur Front
    xb = torch.arange(0, nx + 0.25, 0.25, dtype=N.dtype, device=N.device)
    def profil(msk):
        xs, ps = N.x[msk, 0], phi[msk]
        idx = torch.clamp((xs / 0.25).long(), 0, len(xb) - 2)
        s = torch.zeros(len(xb) - 1, dtype=N.dtype, device=N.device).index_add_(0, idx, ps)
        c = torch.zeros(len(xb) - 1, dtype=N.dtype, device=N.device).index_add_(0, idx, torch.ones_like(ps))
        return (s / torch.clamp(c, min=1)).cpu().numpy()
    pa, pr = profil(ach), profil(rnd)
    xm = (xb[:-1] + 0.125).cpu().numpy()
    res = {'phi_min': float(phi.min()), 'faelle': {}}
    for name, gam, mit in (('gamma1', 1.0, True), ('gamma0', 0.0, True), ('ohne_masse', 1.0, False)):
        if mit:
            l, w = kopplung.metrik_aus_takt(N, phi, gamma=gam)
            L = licht.Licht(N, N=1.0 + phi, l=l, w=w)
        else:
            L = licht.Licht(N)
        dt = 0.4 * 2.0 / L.omega_max()
        ns = int(math.ceil(T / dt))
        dt = T / ns
        A = licht.feld_auf_kanten(N, a_feld)
        P, _ = L.gauss_projektion(L.m * licht.feld_auf_kanten(N, adot_feld))
        A, P = L.schritt(A, P, dt, ns)
        e = L.energie_ecke(A, P)
        def sp(msk):
            return float((e[msk] * N.x[msk, 0]).sum() / e[msk].sum())
        xa, xr = sp(ach), sp(rnd)
        xf = 0.5 * (xa + xr)
        sel = (xm >= x0) & (xm <= xf)
        erw = float(np.sum(-(1.0 + gam) * (pa[sel] - pr[sel])) * 0.25) if mit else 0.0
        res['faelle'][name] = {'front_achse': xa, 'front_rand': xr, 'verzoegerung_gemessen': xr - xa,
                               'verzoegerung_erwartet_eikonal': erw, 'dt': dt, 'schritte': ns}
        log(name, res['faelle'][name])
    g1, g0, o = (res['faelle'][k]['verzoegerung_gemessen'] for k in ('gamma1', 'gamma0', 'ohne_masse'))
    res['verhaeltnis_gamma1_zu_gamma0_netto'] = (g1 - o) / (g0 - o)
    schreibe(aus, res)


if __name__ == '__main__':
    if sys.argv[1] == 'shapiro':
        shapiro(sys.argv[2])
        sys.exit(0)
    if sys.argv[1] == 'nachweis':
        nachweis(sys.argv[2])
    elif sys.argv[1] == 'demo':
        a = sys.argv[4:]
        kw = {}
        if len(a) >= 3:
            kw.update(nx=int(a[0]), ny=int(a[1]), nz=int(a[2]))
        if len(a) >= 4:
            kw['phi_min'] = float(a[3])
        if len(a) >= 5:
            kw['bilder'] = int(a[4])
        demo(sys.argv[2], sys.argv[3], **kw)
