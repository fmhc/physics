# -*- coding: utf-8 -*-
"""netzgpu, Drehrahmen: Demo 4 (360-Grad-Kern auf V). Der Kern (r <= r0) wird schrittweise um die z-Achse gedreht
(0 bis 720 Grad), der Rand (r > R) bleibt die Eins, dazwischen relaxiert das Feld (FIRE). Danach Stoerprobe am 360- und
am 720-Grad-Zustand: Rauschen, neu relaxieren, Energie vergleichen (bleibt der Zustand haengen oder entwindet er sich?).

Aufruf (nur ueber kleintest.sh auf der .69):
  python lauf_rahmen.py demo <datensatz-ordner> <aus.json> [n r0 R schritt_grad]
"""
import json
import math
import os
import sys
import time

import numpy as np
import torch

sys.path.insert(0, '/home/fmh/fmhc-physics-remote/netz-gpu/code')
from netzgpu import FASSUNG, rahmen  # noqa: E402
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
    os.replace(p + '.tmp', p)
    log('->', p)


def demo(ordner, aus, n=12, r0=2.0, R=5.5, schritt=30.0, ftol=1e-6, winkel_max=360.0):
    log('Platte frei %.1f GB' % platte_frei_gb())
    N = Netz('V', (n, n, n))
    zent = torch.tensor([n / 2.0 - 0.25] * 3, dtype=N.dtype, device=N.device)   # Lochmitte C1 als Zentrum
    rh = rahmen.Rahmen(N, zent, r0, R)
    log('Netz', N.N_e, N.N_k, 'frei', int(rh.frei.sum()), 'kern', int(rh.kern.sum()), 'rand', int(rh.rand.sum()))
    ds = Datensatz(ordner, 'Drehrahmen mit 360-Grad-Kern auf V (Kern gedreht, Feld je Winkel aus dem harmonischen Profil relaxiert)', N,
                   quelle={'lauf': aus, 'hinweis': 'synthetisch, keine Messdaten; Modellfeld (Guertel-Energie 4(1-c^2))'},
                   zeit_einheit='Drehwinkel des Kerns in Grad (kein Zeitlauf)')
    ds.groesse('rahmen', 'ecke', 4, 'Einheitsquaternion (w, x, y, z) des Drehrahmens', vmin=-1.0, vmax=1.0)
    ds.groesse('energie', 'ecke', 1, 'Guertel-Energie je Ecke (halbe Kantenenergien)', vmin=0.0)
    ds.setze('parameter', {'r0_a': r0, 'R_a': R, 'zentrum_a': zent.tolist(), 'achse': [0, 0, 1], 'schritt_grad': schritt,
                           'ftol': ftol})
    tabelle = []
    nst = int(round(winkel_max / schritt))
    zust = {}
    for s in range(nst + 1):
        th = math.radians(s * schritt)
        # Start je Winkel aus dem harmonischen Profil q = exp(theta h(r) z/2) (wie z2s2 modus_start), dann FIRE
        q = rh.praediktor(rh.eins(), th)
        q = rh.setze(q, th)
        t1 = time.time()
        q, info = rh.fire(q, ftol=ftol)
        torch.cuda.synchronize()
        info['zeit_s'] = time.time() - t1
        info['grad'] = s * schritt
        tabelle.append(info)
        ds.bild(s * schritt, rahmen=q, energie=rh.energie_ecke(q))
        ds.diagnose('energie_gesamt', info['E'])
        if s * schritt in (360.0, 720.0):
            zust[int(s * schritt)] = q.clone()
        log('%5.0f Grad E=%.6f iter=%d fmax=%.2e c_min=%.4f (%.1f s)' % (s * schritt, info['E'], info['iter'], info['fmax'],
                                                                       info['c_min'], info['zeit_s']))
    # Stoerprobe: Rauschen sigma, neu relaxieren
    g = torch.Generator(device=N.device).manual_seed(5)
    probe = {}
    kz = 0
    for grad, q0 in zust.items():
        th = math.radians(grad)
        for sig in (0.3, 1.0):
            eta = torch.randn((N.N_e, 3), generator=g, device=N.device, dtype=N.dtype) * sig / math.sqrt(3)
            ang = torch.linalg.norm(eta, dim=1)
            ax = eta / ang[:, None]
            dq = torch.cat([torch.cos(0.5 * ang)[:, None], torch.sin(0.5 * ang)[:, None] * ax], 1)
            qn = torch.where(rh.frei[:, None], rahmen.qmul(dq, q0), q0)
            qn = rh.setze(qn, th)
            qr, inf = rh.fire(qn, ftol=ftol)
            probe["%d_sigma%.1f" % (grad, sig)] = inf
            kz += 1
            ds.bild(grad + 10 * kz, rahmen=qn, energie=rh.energie_ecke(qn))
            ds.diagnose("energie_gesamt", float(rh.energie(qn, grad=False)[0]))
            kz += 1
            ds.bild(grad + 10 * kz, rahmen=qr, energie=rh.energie_ecke(qr))
            ds.diagnose("energie_gesamt", inf["E"])
            log('Stoerprobe', grad, sig, inf)
    ds.setze("hinweis_bilder", "Bilder 0 bis 12: Kernwinkel 0 bis 360 Grad; danach Stoerprobe am 360-Grad-Zustand: je Rauschstaerke (0,3 und 1,0 rad) das verrauschte und das neu relaxierte Feld (zeit = 360 + 10 k)")
    ds.schliessen()
    res = {"tabelle": tabelle, "stoerprobe": probe, "netz": [N.N_e, N.N_k], "frei": int(rh.frei.sum()),
           'datensatz_MB': ds.bytes / 1e6}
    schreibe(aus, res)


if __name__ == '__main__':
    a = sys.argv[4:]
    kw = {}
    for arg in a:
        k_, v_ = arg.split('=')
        kw[k_] = int(v_) if k_ == 'n' else float(v_)
    demo(sys.argv[2], sys.argv[3], **kw)
