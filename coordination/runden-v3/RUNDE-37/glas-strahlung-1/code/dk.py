#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TT-GLAS-2 (Runde 46, fmhc-physics), Code-Agent fuer die Leitung claude-primary. Aufgaben 2 und 3, Kontrolle TG2-0.

Lange TT-Wellen bei |k| = 1e-2 in den 13 Wuerfelachsen (tg.richtungen13w), dicht wie tg.punkt (torch; GPU, falls
sichtbar, sonst CPU mit 1 Thread). Netz, B, A, M, c unveraendert aus tg.py. Varianten (PLAN.md Abschnitt 3):
  a  voll (wie TT-GLAS-1): R1, omega^2 = eig(A_red B_red), A_red = L L^+ (Cholesky), Eigenwerte von L^+ B_red L.
  b  affin eingefroren (nur Bewegungsenergie): Rayleigh-Ritz des R1-Modells auf z = S^+ a_h (affine TT-Wellen, auf P
     projiziert): Steifigkeit z^+ B_red z, Lagrange-Masse z^+ A_red^-1 z.
  c  isotrope Ersatzmasse (nur Relaxation): Lagrange-Masse K3 (A3), Reduktion R2: Paar (B_red, K3_red), K3_red = S^+ K3 S;
     mu = Eigenwerte von R^-1 K3_red R^-+ (B_red = R R^+), omega^2 = 1 / mu.
  d  Kontrolle zu c: Rayleigh-Ritz von c auf z.
  e  unprojiziert: a_h^+ B a_h und a_h^+ K3 a_h (vorab isotrop [M], Pruefung).
"""
import argparse, json, os, sys, time, hashlib, platform, resource
import numpy as np
import scipy
import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tg  # noqa: E402  (TT-GLAS-1, unveraendert)
import dz  # noqa: E402


def sha(path):
    with open(path, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def tri(L, Y):
    return torch.linalg.solve_triangular(L, Y, upper=False)


def klass_c(w2, eps):
    masse = (w2 > 0) & (w2 <= 30 * eps ** 2)
    neg = w2 < 0
    luecke = w2 >= 100 * eps ** 2
    unklar = ~(masse | neg | luecke)
    return masse, neg, luecke, unklar


def punkt(mod, K3t, kk, dev, varianten):
    t0 = time.time()
    eps = float(np.linalg.norm(kk))
    B, A, M, c = tg.ops(mod, kk)
    S, z = dz.basis(np.concatenate([M, c], 1), dev)
    del M, c
    z['eps'] = eps
    Ar = dz.reduziert(A, S, dev)
    Br = dz.reduziert(B, S, dev)
    Lc, info = torch.linalg.cholesky_ex(Ar)
    apd = int(info.item()) == 0
    z['A_red_pd'] = apd
    # ---------------------------------------------------------------- a
    if apd:
        w2 = torch.linalg.eigvalsh(dz.herm(Lc.conj().T @ Br @ Lc)).cpu().numpy()
        w2im = np.zeros_like(w2)
    else:
        wc = torch.linalg.eigvals(Ar @ Br).cpu().numpy()
        o = np.argsort(wc.real)
        w2, w2im = wc.real[o], wc.imag[o]
    s, tau, wachs, masse, luecke, unklar = tg.klassen(w2, w2im, eps)
    im = np.nonzero(masse & (w2 > tau))[0]
    im = im[np.argsort(np.abs(w2[im]))]
    z['a'] = {'w2k2_masselos': [float(w2[j] / eps ** 2) for j in sorted(im[:2], key=lambda j: w2[j])],
              'n_masselos': int(masse.sum()), 'n_luecke': int(luecke.sum()), 'n_wachsend': int(wachs.sum()),
              'n_unklar': int(unklar.sum()), 'skala': s, 'luecke_min': float(w2[luecke].min()) if luecke.any() else None,
              'w2_kleinste': [float(x) for x in w2[:6]], 'w2im_max': float(np.abs(w2im).max())}
    if varianten == {'a'}:
        z['t_s'] = time.time() - t0
        return z
    # ---------------------------------------------------------------- b
    ah = dz.affin_wellen(mod, kk)
    ah_t = torch.from_numpy(ah).to(dev)
    zt = S.conj().T @ ah_t
    nah = np.linalg.norm(ah, axis=0)
    nz_ = torch.linalg.norm(zt, dim=0).cpu().numpy()
    z['proj_anteil_weg'] = [float(np.sqrt(max(0.0, 1.0 - (b / a_) ** 2))) for a_, b in zip(nah, nz_)]
    Kb = (zt.conj().T @ (Br @ zt)).cpu().numpy()
    z['Bz_k2V'] = [float(x) for x in np.linalg.eigvalsh(0.5 * (Kb + Kb.conj().T)) / (eps ** 2 * mod['Vbox'])]
    if 'b' in varianten:
        if apd:
            Y = tri(Lc, zt)
            Gb = (Y.conj().T @ Y).cpu().numpy()
        else:
            Gb = (zt.conj().T @ torch.linalg.solve(Ar, zt)).cpu().numpy()
        w, wim, gev = dz.ritz(Kb, Gb)
        z['b'] = {'w2k2': [x / eps ** 2 for x in w], 'w2im_max': wim, 'masse_ev': gev}
    del Lc, Ar
    # ---------------------------------------------------------------- c, d, e
    K3 = dz.assemble(mod, K3t, kk)
    if 'c' in varianten or 'd' in varianten:
        K3r = dz.reduziert(K3, S, dev)
    del S
    if 'c' in varianten:
        eK = torch.linalg.eigvalsh(K3r)
        Rc, infoB = torch.linalg.cholesky_ex(Br)
        zc = {'K3_red_neg': int((eK < -1e-12 * eK.abs().max()).sum().item()), 'K3_red_min_rel': float((eK.min() / eK.abs().max()).item()),
              'B_red_pd': int(infoB.item()) == 0}
        if zc['B_red_pd']:
            T1 = tri(Rc, K3r)
            Y = tri(Rc, T1.conj().T)
            mu = torch.linalg.eigvalsh(dz.herm(Y)).cpu().numpy()
            mmax = np.abs(mu).max()
            gut = np.abs(mu) > 1e-12 * mmax
            w2c = np.sort(1.0 / mu[gut])
            zc['n_mu_null'] = int((~gut).sum())
            w2cim_max = 0.0
        else:
            wc = np.linalg.eigvals(np.linalg.solve(K3r.cpu().numpy(), Br.cpu().numpy()))
            o = np.argsort(wc.real)
            w2c = wc.real[o]
            w2cim_max = float(np.abs(wc.imag).max())
        m_, n_, l_, u_ = klass_c(w2c, eps)
        im = np.nonzero(m_)[0]
        im = im[np.argsort(w2c[im])][:2]
        zc.update({'w2k2_masselos': [float(w2c[j] / eps ** 2) for j in im], 'n_masselos': int(m_.sum()), 'n_negativ': int(n_.sum()),
                   'n_luecke': int(l_.sum()), 'n_unklar': int(u_.sum()), 'w2im_max': w2cim_max,
                   'w2_kleinste_pos': [float(x) for x in w2c[w2c > 0][:4]],
                   'w2_negativ': [float(x) for x in w2c[w2c < 0][:6]],
                   'luecke_min': float(w2c[l_].min()) if l_.any() else None})
        z['c'] = zc
    if 'd' in varianten:
        Gd = (zt.conj().T @ (K3r @ zt)).cpu().numpy()
        w, wim, gev = dz.ritz(Kb, Gd)
        z['d'] = {'w2k2': [x / eps ** 2 for x in w], 'w2im_max': wim, 'masse_ev': gev}
    if 'e' in varianten:
        Ke = ah.conj().T @ (B @ ah)
        Ge = ah.conj().T @ (K3 @ ah)
        w, wim, gev = dz.ritz(Ke, Ge)
        z['e'] = {'w2k2': [x / eps ** 2 for x in w], 'w2im_max': wim, 'masse_ev': gev,
                  'B_k2V': [float(x) for x in np.linalg.eigvalsh(0.5 * (Ke + Ke.conj().T)) / (eps ** 2 * mod['Vbox'])]}
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
    ap.add_argument('--saaten', default='1')
    ap.add_argument('--ridx', default='0-12')
    ap.add_argument('--varianten', default='a,b,c,d,e')
    ap.add_argument('--ohne_lin', action='store_true', help='ohne |k| = 2e-2 an [100], [110], [111]')
    ap.add_argument('--frist', type=float, default=540.0)
    ap.add_argument('--rauch', action='store_true')
    ap.add_argument('--out', required=True, help='Ausgabedatei (bei mehreren Saaten: Praefix)')
    a = ap.parse_args()
    t_start = time.time()
    dev = dz.geraet()
    varianten = set(a.varianten.split(','))
    if '-' in a.ridx:
        i0, i1 = a.ridx.split('-')
        ridx = list(range(int(i0), int(i1) + 1))
    else:
        ridx = [int(x) for x in a.ridx.split(',')]
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'torch': torch.__version__, 'python': platform.python_version(),
            'host': platform.node(), 'argv': sys.argv, 'geraet': str(dev),
            'gpu': torch.cuda.get_device_name(0) if dev.type == 'cuda' else None,
            'skript_sha256': sha(os.path.abspath(__file__)), 'dz_sha256': sha(os.path.abspath(dz.__file__)),
            'tg_sha256': sha(os.path.abspath(tg.__file__)), 'tp_sha256': sha(os.path.abspath(tg.tp.__file__)),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    saaten = [int(s) for s in a.saaten.split(',')]
    rl = tg.richtungen13w()
    abgebrochen = False
    for saat in saaten:
        if time.time() - t_start > a.frist:
            abgebrochen = True
            break
        t0 = time.time()
        LV, pos, G, O, pr = tg.zufallsnetz(a.N, saat)
        mod = tg.modell(LV, pos, G, O, pr)
        Xg = pos[G] + np.einsum('tai,ij->taj', O.astype(float), LV)
        K3t, k3pr = dz.k3_tetra(mod, Xg)
        zeilen = []
        for i in ridx:
            if time.time() - t_start > a.frist:
                abgebrochen = True
                break
            nm, dvec = rl[i]
            zl = {'ridx': i, 'richtung': nm, 'd': dvec.tolist(), 'eps1': punkt(mod, K3t, tg.EPS1 * dvec, dev, varianten)}
            if (not a.ohne_lin) and nm in tg.TT_RICHT:
                zl['eps2'] = punkt(mod, K3t, tg.EPS2 * dvec, dev, {'a'})
            zeilen.append(zl)
        erg = {'N': a.N, 'saat': saat, 'ridx_geplant': ridx, 'ridx_fertig': [z['ridx'] for z in zeilen], 'abgebrochen_frist': abgebrochen,
               'varianten': sorted(varianten), 'zeilen': zeilen, 'pruefung': mod['pruefung'], 'k3': k3pr,
               'E': mod['E'], 'nV': mod['nV'], 'T': mod['T'], 'Vbox': mod['Vbox']}
        res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
               'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
               'gpu_max_MB': (torch.cuda.max_memory_allocated() / 2 ** 20) if dev.type == 'cuda' else None,
               'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
        if a.rauch:
            res = {'info': info, 'schluessel': nur_schluessel(erg), 'laufzeit_s': res['laufzeit_s'], 'maxrss_MB': res['maxrss_MB'],
                   'gpu_max_MB': res['gpu_max_MB'], 't_punkt_s': [z['eps1']['t_s'] for z in zeilen],
                   't_eps2_s': [z['eps2']['t_s'] for z in zeilen if 'eps2' in z], 'weg': [z['eps1']['weg'] for z in zeilen],
                   'abgebrochen_frist': abgebrochen, 'E': mod['E'], 'nV': mod['nV'], 'T': mod['T']}
        pfad = a.out if len(saaten) == 1 else '%s-N%d-s%d.json' % (a.out, a.N, saat)
        schreibe(pfad, res)
        print('fertig dk N=%d saat=%d richtungen=%d laufzeit %.1f s geraet %s' % (a.N, saat, len(zeilen), time.time() - t0, dev),
              flush=True)
        if abgebrochen:
            break


if __name__ == '__main__':
    main()
