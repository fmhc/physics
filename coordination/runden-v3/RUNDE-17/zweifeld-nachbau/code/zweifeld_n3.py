#!/usr/bin/env python3
"""zweifeld_n3.py - PLAN-NACHTRAG-3 (nachtraeglich). Programmfehler-Behebung ohne Verfahrensaenderung.

Befund: Die Hintergrund-Fortsetzung (zweifeld.laufe, Schritt 0,005 ohne Praediktor) scheitert bei grossen Baellen
(weicher Wandmodus) schon fuer Schritte ~1e-3 und brach die kand-Laeufe ab, sobald Newton w^2 < 0,83 ansteuerte.
Behebung (Monkeypatch, zweifeld.py und zweifeld_n2.py bleiben unveraendert):
  1. laufe: Schritt hoechstens 0,0005, Sekanten-Praediktor aus den letzten zwei Loesungen, bis zu 30 Halbierungen.
  2. ProfilCache.hole: scheitert die Fortsetzung trotzdem, liefert der Punkt NaN (statt Abbruch des ganzen Laufs).
  3. Newton (W2 bzw. W1): w^2 auf [w2_min - 0,002, w2_max + 0,002] begrenzt; NaN-Werte -> Kandidat nicht konvergiert.
Aufruf: kand <W2|W1> <modell> <stufe> <npz> <ausdatei> <zeilendateien ...>
"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
import math
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zweifeld as Z
import zweifeld_n2 as N2


def laufe_robust(modell, hp, w2a, u, v, ziele, maxschritt=0.0005):
    out = []
    it = 0
    for z in ziele:
        prev = None
        while abs(z - w2a) > 0.0:
            schritt = z - w2a if abs(z - w2a) <= maxschritt else math.copysign(maxschritt, z - w2a)
            for _ in range(30):
                w2n = z if schritt == z - w2a else w2a + schritt
                if prev is not None:
                    w2p, up_, vp_ = prev
                    t = (w2n - w2a) / (w2a - w2p)
                    u0 = u + t * (u - up_)
                    v0 = None if v is None else v + t * (v - vp_)
                else:
                    u0, v0 = u, v
                un, vn, it, sch, ok = Z.numerov_newton(modell, w2n, hp, u0, v0)
                if ok and float(np.min(un[1:-1])) > -1e-10 * float(np.max(un)):
                    break
                schritt *= 0.5
            else:
                raise RuntimeError('Fortsetzung gescheitert bei w2=%.10f (von %.10f)' % (w2n, w2a))
            prev = (w2a, u, v)
            w2a, u, v = w2n, un, vn
        out.append((z, u.copy(), None if v is None else v.copy(), it))
    return out


Z.laufe = laufe_robust
_hole_alt = Z.ProfilCache.hole


def hole_robust(self, w2):
    key = round(float(w2), 13)
    if key in self.tab:
        return self.tab[key]
    try:
        return _hole_alt(self, w2)
    except Exception as e:
        Z.log('Profil gescheitert w2=%.10f: %s' % (float(w2), e))
        ntab = 2 if self.modell == 'M1' else 4
        self.tab[key] = np.full((ntab, len(self.U[0])), np.nan)
        self.info[key] = dict(w2=float(w2), Q=float('nan'), E=float('nan'), f0=float('nan'), chi0=float('nan'),
                              R_half=float('nan'), virial=float('nan'), knoten=-1, f_R_rel=float('nan'),
                              fehler=str(e))
        return self.tab[key]


Z.ProfilCache.hole = hole_robust


def _begrenze(modell, w2):
    zl = Z.MODELLE[modell]['zeilen']
    return np.clip(w2, min(zl) - 0.002, max(zl) + 0.002)


def mache_newton(wfun):
    def newton(modell, lin, cache, w2, rho, iters=15, dw=1e-6, dr=1e-6):
        nch = Z.MODELLE[modell]['nch']
        w2 = np.array(w2, float)
        rho = np.array(rho, float)
        K = len(w2)
        verlauf = []
        aktiv = np.ones(K, bool)
        ok = np.zeros(K, bool)
        for it in range(iters):
            W2p = np.concatenate([w2, w2 + dw, w2])
            RH = np.concatenate([rho, rho, rho + dr])
            res = Z.punkte(modell, lin, cache, W2p, RH)
            W = wfun(res, K, nch)
            g0 = W[:K]
            Jw = (W[K:2 * K] - g0) / dw
            Jr = (W[2 * K:] - g0) / dr
            a11, a12, a21, a22 = Jw.real, Jr.real, Jw.imag, Jr.imag
            det = a11 * a22 - a12 * a21
            dx = -(a22 * g0.real - a12 * g0.imag) / det
            dy = -(-a21 * g0.real + a11 * g0.imag) / det
            bad = ~(np.isfinite(dx) & np.isfinite(dy))
            aktiv &= ~bad
            dx = np.where(aktiv, dx, 0.0)
            dy = np.where(aktiv, dy, 0.0)
            schritt = np.maximum(np.abs(dx), np.abs(dy))
            fak = np.where(schritt > 0.01, 0.01 / np.maximum(schritt, 1e-300), 1.0)
            w2n = _begrenze(modell, w2 + fak * dx)
            rhon = rho + fak * dy
            for k in range(K):
                lo, hi = Z.e1_grenzen(modell, w2n[k])
                rhon[k] = min(max(rhon[k], lo + 1e-6), hi - 1e-6)
            w2, rho = w2n, rhon
            verlauf.append(np.where(aktiv, schritt, np.nan).tolist())
            ok = aktiv & (schritt < 1e-11)
            if (ok | ~aktiv).all():
                break
        return w2, rho, ok, verlauf
    return newton


def _w2fun(res, K, nch):
    zeta = N2.zeta0_aus(res['G'][:K], nch)
    if not np.all(np.isfinite(zeta)):
        zeta = np.where(np.isfinite(zeta), zeta, 1.0)
    return N2.W2_aus(res, np.concatenate([zeta, zeta, zeta]), nch)


def _w1fun(res, K, nch):
    return res['W1']


if __name__ == '__main__':
    if sys.argv[1] != 'kand':
        raise SystemExit('unbekannt: ' + sys.argv[1])
    art = sys.argv[2]
    if art == 'W2':
        N2.newton2d_n2 = mache_newton(_w2fun)
        N2.kand_lauf_n2(sys.argv[3], int(sys.argv[4]), sys.argv[5], sys.argv[6], sys.argv[7:])
    elif art == 'W1':
        Z.newton2d = mache_newton(_w1fun)
        Z.kand_lauf(sys.argv[3], int(sys.argv[4]), sys.argv[5], sys.argv[6], sys.argv[7:])
    else:
        raise SystemExit('W2 oder W1')
