# -*- coding: utf-8 -*-
"""netzgpu, Q-Ball: Nachweis gegen SCHWERE-MASSE-V und Demo 3 (zwei Baelle fallen im Takt-Gefaelle).

Aufruf (nur ueber kleintest.sh auf der .69):
  python lauf_skalar.py nachweis <aus.json> [n]
  python lauf_skalar.py demo <datensatz-ordner> <aus.json> [phi0] [T] [bilder]
"""
import json
import math
import os
import sys
import time

import numpy as np
import torch

sys.path.insert(0, '/home/fmh/fmhc-physics-remote/netz-gpu/code')
from netzgpu import FASSUNG, kopplung, skalar  # noqa: E402
from netzgpu.datensatz import Datensatz, platte_frei_gb  # noqa: E402
from netzgpu.netz import Netz  # noqa: E402

T0 = time.time()
REF = {  # SCHWERE-MASSE-V, lauf/qb-o<om>-h1.0.json (Ball um C1, rhomboedrischer Torus L)
    0.85: {'E': 336.48907131507775, 'Q': 365.4533892533921, 'om': 0.8478796840223297, 'L': 20},
    0.9: {'E': 170.4381895094275, 'Q': 174.0396846665803, 'om': 0.898215015858707, 'L': 24},
    0.8: {'E': 995.8569308265704, 'Q': 1172.3411343349105, 'om': 0.7997367300986152, 'L': 20},
}


def log(*a):
    print('[%7.1f s]' % (time.time() - T0), *a, flush=True)


def schreibe(p, obj):
    obj['_meta'] = {'argv': sys.argv, 'torch': torch.__version__, 'gpu': torch.cuda.get_device_name(0),
                    'laufzeit_s': time.time() - T0, 'gpu_speicher_max_MB': torch.cuda.max_memory_allocated() / 1e6,
                    'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'fassung': FASSUNG}
    with open(p + '.tmp', 'w') as f:
        json.dump(obj, f, indent=1)
    os.replace(p + '.tmp', p)
    log('->', p)


def ball(sk, x0, om, h, gtol=1e-9, maxiter=4000):
    k = skalar.qball_kont(om)
    r = sk.abstand_Q(x0)
    f0 = torch.tensor(np.interp(r.cpu().numpy(), k['r'], k['f'], right=0.0), dtype=sk.netz.dtype, device=sk.netz.device)
    t1 = time.time()
    f, info = sk.relaxieren(f0, k['Q'], maxiter=maxiter, gtol=gtol)
    torch.cuda.synchronize()
    info['zeit_s'] = time.time() - t1
    tl = sk.teile(f, info['om'])
    info.update({'E_teile': tl['E'], 'Q_teile': tl['Q'], 'S_rel': tl['S'] / tl['E'], 'bind': (tl['Q'] - tl['E']) / tl['E'],
                 'E_kont': k['E'], 'Q_kont': k['Q']})
    return f, info, tl


def nachweis(aus, n=16):
    res = {}
    N = Netz('V', (n, n, n))
    x0 = torch.tensor([n / 2 - 0.25] * 3, dtype=N.dtype, device=N.device)     # C1-Platz nahe der Mitte
    i0 = int(torch.argmin(torch.linalg.norm(N.ecken_minbild(x0), dim=1)))
    log('Netz', N.N_e, 'Mitte-Ecke', i0, N.bahn[i0], N.x[i0].tolist())
    sk = skalar.Skalar(N, h=1.0)
    for om in (0.85, 0.9, 0.8):
        f, info, tl = ball(sk, x0, om, 1.0)
        ref = REF[om]
        info['E_ref'] = ref['E']
        info['E_rel_abw'] = (info['E_teile'] - ref['E']) / ref['E']
        info['om_rel_abw'] = (info['om'] - ref['om']) / ref['om']
        info['Q_rel_abw'] = (info['Q_teile'] - ref['Q']) / ref['Q']
        rr = sk.abstand_Q(x0)
        info['rand_anteil'] = float(tl['m'][rr > 0.85 * n * 2 * math.sqrt(2) / 2].sum() / tl['E'])
        res['om%.2f' % om] = info
        log(om, json.dumps(info))
    res['netz'] = {'zellen': n, 'N_e': N.N_e, 'inkreis_lP': n * math.sqrt(2)}
    schreibe(aus, res)


def demo(ordner, aus, phi0=0.004, T=200.0, bilder=40, nx=20, ny=10, nz=20, h=1.0, metrisch=1, om1=0.85, om2=0.9):
    log('Platte frei %.1f GB' % platte_frei_gb())
    N = Netz('V', (nx, ny, nz))
    log('Netz', N.N_e, N.N_k, N.N_d, N.N_t)
    sk0 = skalar.Skalar(N, h=h)
    # zwei Baelle auf C1-Plaetzen, gleiche Hoehe z0 = nz/2
    zc = nz / 2.0
    lagen = [(nx * 0.25, ny / 2.0, zc), (nx * 0.75, ny / 2.0, zc)]
    oms = (om1, om2)
    fs, infos = [], []
    for (x, y, z), om in zip(lagen, oms):
        x0 = torch.tensor([x - 0.25, y - 0.25, z - 0.25], dtype=N.dtype, device=N.device)
        f, info, tl = ball(sk0, x0, om, h)
        info['lage_a'] = x0.tolist()
        fs.append(f)
        infos.append(info)
        log('Ball', om, json.dumps(info))
    # Takt-Gefaelle Phi(z) = -phi0 sin(2 pi z / Lz): bei z0 = Lz/2 linear, Fall nach -z
    z = N.x[:, 2]
    phi = -phi0 * torch.sin(2 * math.pi * z / nz)
    Nl = 1.0 + phi
    l, w = kopplung.metrik_aus_takt(N, phi) if metrisch else (None, None)
    sk = skalar.Skalar(N, h=h, N=Nl, l=l, w=w)
    phi_f = (fs[0] + fs[1]).to(torch.complex128)
    pi_ = sk.m * (1j * (infos[0]['om'] * fs[0] + infos[1]['om'] * fs[1])).to(torch.complex128)
    wmax = sk.omega_max()
    dt0 = 0.5 * 2.0 / wmax
    nschritt = int(math.ceil(T / bilder / dt0))
    dt = T / bilder / nschritt
    log('omega_max %.3f dt %.4f Schritte je Bild %d' % (wmax, dt, nschritt))
    ds = Datensatz(ordner, 'Zwei Q-Baelle fallen im Takt-Gefaelle (Aequivalenzprinzip), V, metrisch gekoppelt', N,
                   quelle={'lauf': aus, 'hinweis': 'synthetisch, keine Messdaten; Takt-Gefaelle gesetzt, nicht aus Quelle'},
                   zeit_einheit='1/m (Q-Ball-Einheiten; h = l_P m = %.2f, a = %.4f Q-Einheiten)' % (h, h / skalar.LP),
                   mit_tetraeder=False)
    ds.groesse('skalar_betrag2', 'ecke', 1, '|phi|^2 des Q-Ball-Felds', vmin=0.0)
    ds.groesse('takt', 'ecke', 1, 'Lapse N - 1 = Phi(z) = -phi0 sin(2 pi z / L_z) (gesetzt)', symmetrisch=True)
    ds.setze('parameter', {'phi0': phi0, 'g_erwartet_Q': phi0 * 2 * math.pi / (nz / skalar.LP * h), 'h': h,
                           'baelle': [{'om': oms[i], 'om_gitter': infos[i]['om'], 'E': infos[i]['E_teile'],
                                       'Q': infos[i]['Q_teile'], 'bindung': infos[i]['bind'], 'lage_a': infos[i]['lage_a']}
                                      for i in range(2)], 'dt': dt, 'schritte_je_bild': nschritt})
    E0 = sk.energie(phi_f, pi_)
    Q0 = sk.ladung(phi_f, pi_)
    links = N.x[:, 0] < nx / 2.0
    dphi_dz = -phi0 * (2 * math.pi / nz) * torch.cos(2 * math.pi * z / nz)      # dPhi/dz in 1/a
    bahn = []
    tk = []
    for b in range(bilder + 1):
        if b > 0:
            torch.cuda.synchronize()
            t1 = time.time()
            phi_f, pi_ = sk.schritt(phi_f, pi_, dt, nschritt)
            torch.cuda.synchronize()
            tk.append((time.time() - t1) / nschritt)
        e = sk.energie_ecke(phi_f, pi_)
        zl = []
        gl = []
        for msk in (links, ~links):
            ww = e[msk]
            zl.append(float((ww * N.x[msk, 2]).sum() / ww.sum()))
            gl.append(float(-(skalar.LP / h) ** 2 * (ww * dphi_dz[msk]).sum() / ww.sum()))
        bahn.append([b * nschritt * dt] + zl + gl)
        E = sk.energie(phi_f, pi_)
        Qn = sk.ladung(phi_f, pi_)
        ds.bild(b * nschritt * dt, skalar_betrag2=(phi_f.abs() ** 2), takt=phi)
        ds.diagnose('energie_gesamt', E)
        ds.diagnose('ladung', Qn)
        if b % 5 == 0:
            log('Bild %d t=%.1f E rel %.2e Q rel %.2e z = %.4f / %.4f' % (b, b * nschritt * dt, E / E0 - 1, Qn / Q0 - 1,
                                                                        zl[0], zl[1]))
    bahn = np.array(bahn)
    # Fit z(t) = z0 + v0 t + a t^2 / 2 (z in a), Beschleunigung in Q-Einheiten
    t = bahn[:, 0]
    X = np.stack([np.ones_like(t), t, 0.5 * t * t], 1)
    fit = [np.linalg.lstsq(X, bahn[:, 1 + i], rcond=None)[0] for i in range(2)]
    acc_Q = [float(fi[2] / skalar.LP * h) for fi in fit]
    g_erw = -phi0 * 2 * math.pi / (nz / skalar.LP * h)
    # Vorhersage aus der Kraft auf die Energieverteilung (passive Masse = Energie): z'' = <-dPhi/dz>_e, doppelt integriert
    vorh, verh = [], []
    for i in range(2):
        g = bahn[:, 3 + i]
        v = np.concatenate([[0.0], np.cumsum(0.5 * (g[1:] + g[:-1]) * np.diff(t))])
        zp = bahn[0, 1 + i] + np.concatenate([[0.0], np.cumsum(0.5 * (v[1:] + v[:-1]) * np.diff(t))])
        vorh.append(zp)
        verh.append(float((bahn[-1, 1 + i] - bahn[0, 1 + i]) / (zp[-1] - bahn[0, 1 + i])))
    ds.setze('ergebnis', {'beschleunigung_Q': acc_Q, 'g_erwartet_Q': g_erw, 'verhaeltnis_a1_a2': acc_Q[0] / acc_Q[1],
                          'fallweg_gemessen_durch_vorhersage': verh})
    ds.schliessen()
    res = {'baelle': infos, 'beschleunigung_Q': acc_Q, 'g_erwartet_Q': g_erw,
           'fallweg_gemessen_durch_vorhersage': verh, 'fallweg_a': [float(bahn[-1, 1 + i] - bahn[0, 1 + i]) for i in range(2)],
           'vorhersage_z_a': [x.tolist() for x in vorh],
           'a_durch_g': [a / g_erw for a in acc_Q], 'verhaeltnis_a1_a2_minus_1': acc_Q[0] / acc_Q[1] - 1,
           'bahn_t_z1_z2_a': bahn.tolist(), 'energie_rel_max': float(max(abs(x / E0 - 1) for x in ds.manifest['diagnose']['energie_gesamt'])),
           'ladung_rel_max': float(max(abs(x / Q0 - 1) for x in ds.manifest['diagnose']['ladung'])),
           'zeit_je_schritt_ms': 1e3 * float(np.median(tk)), 'dt': dt, 'omega_max': wmax,
           'netz': [N.N_e, N.N_k, N.N_d, N.N_t], 'datensatz_MB': ds.bytes / 1e6}
    log(json.dumps({k: v for k, v in res.items() if k not in ('bahn_t_z1_z2_a', 'vorhersage_z_a', 'baelle')}))
    schreibe(aus, res)


if __name__ == '__main__':
    if sys.argv[1] == 'nachweis':
        nachweis(sys.argv[2], *(int(x) for x in sys.argv[3:4]))
    else:
        kw = {}
        for arg in sys.argv[4:]:
            k_, v_ = arg.split('=')
            kw[k_] = int(v_) if k_ in ('bilder', 'nx', 'ny', 'nz', 'metrisch') else float(v_)
        demo(sys.argv[2], sys.argv[3], **kw)
