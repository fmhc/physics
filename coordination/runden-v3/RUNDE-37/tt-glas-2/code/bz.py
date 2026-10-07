#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TT-GLAS-2 (Runde 46, fmhc-physics), Code-Agent fuer die Leitung claude-primary. Aufgabe 1 der Karte.

Stabilitaet ueber die ganze Brillouin-Zone der Superzelle. Modell unveraendert aus tg.py (TT-GLAS-1, eingefroren,
sha256 ec48a258...): Regge-Steifigkeit B, Eck-Eichung M, skalare Regel c, Bewegungsenergie A (J = 1), Reduktion R1.
Je Bloch-k: Zwangsflaeche S = orthonormales Komplement von Bild[M, c] (dz.basis); omega^2 = Eigenwerte von
(S^+ A S)(S^+ B S), alle Eigenwerte, dicht wie tg.punkt (torch; GPU, falls sichtbar, sonst CPU mit 1 Thread).
k-Gitter: k = (2 pi / L) m / n, m in {0..n-1}^3; je Paar (k, -k) nur ein Vertreter (omega^2(k) = omega^2(-k), weil die
Operatoren bei -k die komplex konjugierten sind). Dazu je Netz ein Kontrollpunkt [100], |k| = 1e-2 (TG2-0).
"""
import argparse, itertools, json, os, sys, time, hashlib, platform, resource
import numpy as np
import scipy
import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tg  # noqa: E402  (TT-GLAS-1, unveraendert)
import dz  # noqa: E402

TAU_REL = 1e-12     # wachsend: Re omega^2 < -tau oder |Im omega^2| > tau, tau = 1e-12 s (wie tg)
NULL_REL = 1e-9     # Nullmode: |omega^2| <= 1e-9 s (wie ew.py); Abgrenzung der Nullmoden (erwartet nur bei Gamma)


def kklassen(n):
    """Vertreter der Klassen {m, -m mod n} im Gitter {0..n-1}^3 (lexikographisch kleinerer)."""
    out = []
    for m in itertools.product(range(n), repeat=3):
        mm = tuple((-x) % n for x in m)
        if m <= mm:
            out.append(m)
    return out


def sha(path):
    with open(path, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def punkt(mod, k, dev, gamma=False, klein_eps=None):
    """Alle omega^2 bei Bloch-k (R1). klein_eps: Kontrollpunkt, dazu die masselosen Werte wie tg.punkt."""
    t0 = time.time()
    B, A, M, c = tg.ops(mod, k)
    S, z = dz.basis(np.concatenate([M, c], 1), dev, gamma=gamma)
    del M, c
    Ar = dz.reduziert(A, S, dev)
    Br = dz.reduziert(B, S, dev)
    del S
    eB = torch.linalg.eigvalsh(Br)
    eBmax = float(eB.abs().max().item())
    z.update({'eps': float(np.linalg.norm(k)), 'dim': int(Br.shape[0]), 'B_red_neg': int((eB < -1e-9 * eBmax).sum().item()),
              'B_red_min_rel': float(eB.min().item() / eBmax)})
    Lc, info = torch.linalg.cholesky_ex(Ar)
    if int(info.item()) == 0:
        z['A_red_pd'] = True
        w2 = torch.linalg.eigvalsh(dz.herm(Lc.conj().T @ Br @ Lc)).cpu().numpy()
        w2im = np.zeros_like(w2)
    else:
        z['A_red_pd'] = False
        eA = torch.linalg.eigvalsh(Ar)
        z['A_red_neg'] = int((eA < 0).sum().item())
        wc = torch.linalg.eigvals(Ar @ Br).cpu().numpy()
        o = np.argsort(wc.real)
        w2, w2im = wc.real[o], wc.imag[o]
    del Lc, Ar, Br
    s = max(float(np.max(np.abs(w2 + 1j * w2im))), 1e-300)
    tau = TAU_REL * s
    null = np.abs(w2 + 1j * w2im) <= NULL_REL * s
    wachs = (~null) & ((w2 < -tau) | (np.abs(w2im) > tau))
    rest = ~null
    z.update({'skala': s, 'tau': tau, 'n_null': int(null.sum()), 'n_wachsend': int(wachs.sum()),
              'w2_kleinste': [float(x) for x in w2[:10]], 'w2im_kleinste': [float(x) for x in w2im[:10]],
              'w2im_max': float(np.abs(w2im).max()),
              'w2_min_ohne_null': float(w2[rest].min()) if rest.any() else None,
              'w2_min_re_alle': float(w2.min()),
              'wachsend_werte': [[float(a), float(b)] for a, b in zip(w2[wachs][:10], w2im[wachs][:10])]})
    if klein_eps is not None:
        eps = klein_eps
        s_, tau_, wa_, masse, luecke, unklar = tg.klassen(w2, w2im, eps)
        im = np.nonzero(masse & (w2 > tau_))[0]
        im = im[np.argsort(np.abs(w2[im]))]
        z.update({'n_masselos': int(masse.sum()), 'n_luecke': int(luecke.sum()), 'n_unklar': int(unklar.sum()),
                  'n_wachsend_tg': int(wa_.sum()),
                  'w2k2_masselos': [float(w2[j] / eps ** 2) for j in sorted(im[:2], key=lambda j: w2[j])]})
    if dev.type == 'cuda':
        torch.cuda.synchronize()
    z['t_s'] = time.time() - t0
    return z


def nur_schluessel(x, tiefe=0):
    if isinstance(x, dict):
        return {k: nur_schluessel(v, tiefe + 1) for k, v in x.items()} if tiefe < 3 else sorted(x.keys())
    if isinstance(x, list) and x and isinstance(x[0], dict):
        return [nur_schluessel(x[0], tiefe + 1)]
    return type(x).__name__


def schreibe(pfad, res):
    with open(pfad + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(pfad + '.tmp', pfad)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--N', type=int, required=True)
    ap.add_argument('--saat', type=int, required=True)
    ap.add_argument('--n', type=int, default=6, help='k-Gitter n^3')
    ap.add_argument('--kteil', default='0/1', help='Teil i/m der k-Klassen (Index mod m == i)')
    ap.add_argument('--kmax', type=int, default=0, help='hoechstens so viele k-Klassen (0 = alle; nur Rauchtests)')
    ap.add_argument('--frist', type=float, default=540.0, help='keine neue Rechnung nach so vielen Sekunden')
    ap.add_argument('--ohne_kontrolle', action='store_true')
    ap.add_argument('--rauch', action='store_true', help='nur Schluessel und Laufzeiten speichern, keine Werte')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t_start = time.time()
    dev = dz.geraet()
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'torch': torch.__version__, 'python': platform.python_version(),
            'host': platform.node(), 'argv': sys.argv, 'geraet': str(dev),
            'gpu': torch.cuda.get_device_name(0) if dev.type == 'cuda' else None,
            'cuda_visible': os.environ.get('CUDA_VISIBLE_DEVICES'),
            'skript_sha256': sha(os.path.abspath(__file__)), 'dz_sha256': sha(os.path.abspath(dz.__file__)),
            'tg_sha256': sha(os.path.abspath(tg.__file__)), 'ew_sha256': sha(os.path.abspath(tg.ew.__file__)),
            'tp_sha256': sha(os.path.abspath(tg.tp.__file__)), 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    LV, pos, G, O, pr = tg.zufallsnetz(a.N, a.saat)
    mod = tg.modell(LV, pos, G, O, pr)
    L = float(LV[0, 0])
    alle = kklassen(a.n)
    i_teil, m_teil = [int(x) for x in a.kteil.split('/')]
    mein = [(j, m) for j, m in enumerate(alle) if j % m_teil == i_teil]
    if a.kmax > 0:
        mein = mein[:a.kmax]
    punkte = []
    abgebrochen = False
    kontrolle = None
    if not a.ohne_kontrolle:
        kontrolle = punkt(mod, tg.EPS1 * np.array([1.0, 0.0, 0.0]), dev, klein_eps=tg.EPS1)
    for j, m in mein:
        if time.time() - t_start > a.frist:
            abgebrochen = True
            break
        k = (2.0 * np.pi / L) * np.array(m, float) / a.n
        gamma = bool(m == (0, 0, 0))
        z = punkt(mod, k, dev, gamma=gamma)
        z.update({'klasse': j, 'm': list(m), 'gamma': gamma,
                  'selbstkonjugiert': bool(tuple((-x) % a.n for x in m) == m), 'k': k.tolist()})
        punkte.append(z)
    erg = {'N': a.N, 'saat': a.saat, 'n': a.n, 'L': L, 'n_klassen_gesamt': len(alle), 'kteil': a.kteil,
           'klassen_geplant': [j for j, m in mein], 'klassen_fertig': [z['klasse'] for z in punkte],
           'abgebrochen_frist': abgebrochen, 'punkte': punkte, 'kontrollpunkt_100': kontrolle,
           'pruefung': mod['pruefung'], 'E': mod['E'], 'nV': mod['nV'], 'T': mod['T']}
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t_start,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'gpu_max_MB': (torch.cuda.max_memory_allocated() / 2 ** 20) if dev.type == 'cuda' else None,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.rauch:
        res = {'info': info, 'schluessel': nur_schluessel(erg), 'laufzeit_s': res['laufzeit_s'], 'maxrss_MB': res['maxrss_MB'],
               'gpu_max_MB': res['gpu_max_MB'], 't_punkt_s': [z['t_s'] for z in punkte],
               't_kontrolle_s': kontrolle['t_s'] if kontrolle else None, 'weg': [z['weg'] for z in punkte],
               'n_punkte': len(punkte), 'abgebrochen_frist': abgebrochen, 'E': mod['E'], 'nV': mod['nV'], 'T': mod['T']}
    schreibe(a.out, res)
    print('fertig bz N=%d saat=%d punkte=%d laufzeit %.1f s geraet %s' % (a.N, a.saat, len(punkte), time.time() - t_start, dev),
          flush=True)


if __name__ == '__main__':
    main()
