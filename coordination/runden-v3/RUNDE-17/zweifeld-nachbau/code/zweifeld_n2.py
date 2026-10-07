#!/usr/bin/env python3
"""zweifeld_n2.py - PLAN-NACHTRAG-2 (nachtraeglich). Eigener Code des Code-Agenten.

Grund: W1 aus zweifeld.py ist die Jost-Determinante mit auslaufender Welle (W1 = vol(Y_a, Y_b, Z_b, Z_aus) bei K1).
Ihr Umlauf um eine stille Stelle ist 0 (K1 gemessen). Ersatz fuer Lokalisierung und Umlauf:
  W2 = s~ + i m_a, mit s~ = det(B^T zeta0 ; Zeile a von G) und zeta0 = Spaltenrichtung von B am Rechteckmittelpunkt.
  Kofaktorform: W2 = zeta0_c c_1 - zeta0_b c_2 + i c_0.  Zwei Kanaele (K1): W2 = G_ab + i G_bb (wie LOG-NACHBAU).
Alles andere (Hintergrund, Kanaele, Zeilen, Detektoren, Rechteck, Verfeinerung) unveraendert aus zweifeld.py.

Aufruf: kand <modell> <stufe> <npz> <ausdatei> <zeilendateien ...>
"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
import json
import time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zweifeld as Z


def zeta0_aus(G, nch):
    """Einheitsvektor der Spaltenrichtung von B = G[Zeilen b, c; Spalten Z_b, Z_c]; groesste Komponente positiv."""
    K = G.shape[0]
    if nch == 2:
        return np.ones((K, 1))
    z = np.empty((K, 2))
    for k in range(K):
        B = G[k, 1:, :]
        cb, cc = B[:, 0], B[:, 1]
        col = cb if np.hypot(cb[0], cb[1]) >= np.hypot(cc[0], cc[1]) else cc
        col = col / np.hypot(col[0], col[1])
        if col[int(np.argmax(np.abs(col)))] < 0:
            col = -col
        z[k] = col
    return z


def W2_aus(res, zeta, nch):
    G, c = res['G'], res['c']
    if nch == 2:
        return G[:, 0, 0] + 1j * G[:, 1, 0]
    return (zeta[:, 1] * c[:, 1] - zeta[:, 0] * c[:, 2]) + 1j * c[:, 0]


def newton2d_n2(modell, lin, cache, w2, rho, iters=15, dw=1e-6, dr=1e-6):
    nch = Z.MODELLE[modell]['nch']
    w2 = np.array(w2, float)
    rho = np.array(rho, float)
    K = len(w2)
    verlauf = []
    ok = np.zeros(K, bool)
    for it in range(iters):
        W2p = np.concatenate([w2, w2 + dw, w2])
        RH = np.concatenate([rho, rho, rho + dr])
        res = Z.punkte(modell, lin, cache, W2p, RH)
        zeta = zeta0_aus(res['G'][:K], nch)
        zeta3 = np.concatenate([zeta, zeta, zeta])
        W = W2_aus(res, zeta3, nch)
        g0 = W[:K]
        Jw = (W[K:2 * K] - g0) / dw
        Jr = (W[2 * K:] - g0) / dr
        a11, a12, a21, a22 = Jw.real, Jr.real, Jw.imag, Jr.imag
        det = a11 * a22 - a12 * a21
        dx = -(a22 * g0.real - a12 * g0.imag) / det
        dy = -(-a21 * g0.real + a11 * g0.imag) / det
        dx = np.where(np.isfinite(dx), dx, 0.0)
        dy = np.where(np.isfinite(dy), dy, 0.0)
        schritt = np.maximum(np.abs(dx), np.abs(dy))
        fak = np.where(schritt > 0.01, 0.01 / np.maximum(schritt, 1e-300), 1.0)
        w2n = w2 + fak * dx
        rhon = rho + fak * dy
        for k in range(K):
            lo, hi = Z.e1_grenzen(modell, w2n[k])
            rhon[k] = min(max(rhon[k], lo + 1e-6), hi - 1e-6)
        w2, rho = w2n, rhon
        verlauf.append(schritt.tolist())
        ok = schritt < 1e-11
        if ok.all():
            break
    return w2, rho, ok, verlauf


def umlaeufe_n2(modell, lin, cache, w2c, rc):
    """Wie zweifeld.umlaeufe, aber Phase von W2 mit zeta0 aus dem Mittelpunkt (fest je Rechteck)."""
    nch = Z.MODELLE[modell]['nch']
    K = len(w2c)
    mitte = Z.punkte(modell, lin, cache, np.asarray(w2c, float), np.asarray(rc, float))
    zeta = zeta0_aus(mitte['G'], nch)
    werte = [dict() for _ in range(K)]
    neu = [np.arange(4 * Z.NKANTE) / Z.NKANTE for _ in range(K)]
    erg = [None] * K
    e1min = [np.inf] * K
    for rnd in range(Z.VERF_RUNDEN + 1):
        W2l, RH, wer, zl = [], [], [], []
        for k in range(K):
            if len(neu[k]):
                w, r = Z.rechteck(neu[k], w2c[k], rc[k])
                W2l.append(w)
                RH.append(r)
                wer += [(k, t) for t in neu[k].tolist()]
                zl.append(np.repeat(zeta[k:k + 1], len(w), axis=0))
                k2, kb2, kc2 = Z.energien(modell, w, r)
                mins = [np.min(k2), np.min(kb2)] + ([] if kc2 is None else [np.min(kc2)])
                e1min[k] = min(e1min[k], float(min(mins)))
        if wer:
            res = Z.punkte(modell, lin, cache, np.concatenate(W2l), np.concatenate(RH))
            W = W2_aus(res, np.concatenate(zl), nch)
            for (k, t), z in zip(wer, W.tolist()):
                werte[k][t] = z
        for k in range(K):
            tt = np.array(sorted(werte[k]))
            z = np.array([werte[k][t] for t in tt])
            ph = np.angle(z)
            d = (np.roll(ph, -1) - ph + np.pi) % (2 * np.pi) - np.pi
            groesst = float(np.max(np.abs(d)))
            n = float(np.sum(d) / (2 * np.pi))
            erg[k] = dict(umlauf=int(round(n)), umlauf_roh=n, groesster_sprung=groesst, punkte=int(len(tt)),
                          aufgeloest=bool(groesst < Z.SPRUNG), min_absW=float(np.min(np.abs(z))),
                          max_absW=float(np.max(np.abs(z))), runden=rnd, e1_min_schwelle=e1min[k],
                          zeta0=zeta[k].tolist())
            tneu = []
            if rnd < Z.VERF_RUNDEN:
                for i in np.nonzero(np.abs(d) >= Z.SPRUNG)[0]:
                    t1 = tt[i]
                    t2 = tt[(i + 1) % len(tt)]
                    if t2 <= t1:
                        t2 += 4.0
                    tneu.append((0.5 * (t1 + t2)) % 4.0)
            neu[k] = np.array(tneu)
        if all(len(x) == 0 for x in neu):
            break
    return erg


def kand_lauf_n2(modell, stufe, npz, ausdatei, dateien):
    t0 = time.time()
    cache = Z.ProfilCache(modell, stufe, npz)
    lin = Z.Lin(modell, cache.hp, cache.R_lin, cache.r_m)
    alle = [json.load(open(f)) for f in dateien]
    kand, paare_alle = [], {}
    for st in sorted(set(z['stufe'] for z in alle)):
        zs = sorted([z for z in alle if z['stufe'] == st], key=lambda d: d['w2'])
        k, p = Z.detektoren(zs)
        for x in k:
            x['stufe_detektor'] = st
        kand += k
        paare_alle[st] = p
        Z.log('Stufe %d: %d Zeilen, %d Rohkandidaten' % (st, len(zs), len(k)))
    uniq = []
    for k in kand:
        tr = [u for u in uniq if abs(k['w2'] - u['w2']) < 2e-3 and abs(k['rho'] - u['rho']) < 2e-3]
        tag = '%s@st%d' % (k['quelle'], k['stufe_detektor'])
        if tr:
            if tag not in tr[0]['quellen']:
                tr[0]['quellen'].append(tag)
        else:
            u = dict(k)
            u['quellen'] = [tag]
            uniq.append(u)
    Z.log('Kandidaten nach Zusammenlegen: %d %s' % (len(uniq), json.dumps(uniq)))
    erg = []
    if uniq:
        w2l, rl, ok, verl = newton2d_n2(modell, lin, cache, [u['w2'] for u in uniq], [u['rho'] for u in uniq])
        Z.log('Newton fertig %.1fs' % (time.time() - t0))
        zmin, zmax = min(Z.MODELLE[modell]['zeilen']), max(Z.MODELLE[modell]['zeilen'])
        for i in range(len(uniq)):
            e = dict(start=uniq[i], w2=float(w2l[i]), rho=float(rl[i]), konvergiert=bool(ok[i]),
                     newton=[v[i] for v in verl], im_fenster=bool(zmin - 1e-9 <= w2l[i] <= zmax + 1e-9),
                     in_e1=Z._in_e1(modell, float(w2l[i]), float(rl[i])), doppelt_von=None)
            for j, f in enumerate(erg):
                if f['konvergiert'] and e['konvergiert'] and abs(f['w2'] - e['w2']) < 1e-7 and \
                        abs(f['rho'] - e['rho']) < 1e-7:
                    e['doppelt_von'] = j
                    break
            erg.append(e)
        idx = [i for i, e in enumerate(erg) if e['doppelt_von'] is None]
        zc = [(erg[i]['w2'], erg[i]['rho']) if erg[i]['konvergiert'] else (uniq[i]['w2'], uniq[i]['rho'])
              for i in idx]
        if idx:
            ul = umlaeufe_n2(modell, lin, cache, np.array([z[0] for z in zc]), np.array([z[1] for z in zc]))
            pk = Z.punkte(modell, lin, cache, np.array([z[0] for z in zc]), np.array([z[1] for z in zc]))
            nch = Z.MODELLE[modell]['nch']
            zeta = np.array([u['zeta0'] for u in ul])
            W2c = W2_aus(pk, zeta, nch)
            for j, i in enumerate(idx):
                erg[i]['umlauf_um'] = 'newton' if erg[i]['konvergiert'] else 'start'
                erg[i].update(ul[j])
                erg[i]['W2_am_punkt'] = [float(W2c[j].real), float(W2c[j].imag)]
                erg[i]['W1_am_punkt'] = [float(pk['W1'][j].real), float(pk['W1'][j].imag)]
                erg[i]['ma_am_punkt'] = float(pk['ma'][j])
                inf = cache.info[round(float(zc[j][0]), 13)]
                erg[i]['chi0'] = inf['chi0']
                erg[i]['profil'] = inf
        for i, e in enumerate(erg):
            Z.log('kand %d %s' % (i, json.dumps({k: v for k, v in e.items() if k not in ('newton', 'profil')})))
    out = dict(modell=modell, stufe=stufe, nachtrag=2, dateien=len(dateien), paare=paare_alle, kandidaten=erg,
               R_lin=cache.R_lin, r_m=cache.r_m, sekunden=time.time() - t0)
    Z.speichere_json(ausdatei, out)
    Z.log('kand_n2 fertig %.1fs' % (time.time() - t0))


if __name__ == '__main__':
    if sys.argv[1] != 'kand':
        raise SystemExit('unbekannt: ' + sys.argv[1])
    kand_lauf_n2(sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6:])
