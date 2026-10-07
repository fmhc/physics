#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DS-EICHUNG-2D-1: 1+1D-CDT (periodische Zeit T, fester Rauminhalt) mit unabhaengiger Abtastung der Schichtlaengen.

Gewicht der Schichtlaengen l_t (unmarkierte, bei einer Kante der Schicht 0 gewurzelte Triangulierungen):
  W(l) = prod_t binom(l_t + l_{t+1} - 1, l_t - 1)           (Herleitung in ERGEBNIS.md, Abschnitt Methoden)
Metropolis mit Paaraustausch (l_t + 1, l_s - 1) fuer beliebige Schichten t, s (Summe l fest, N = 2 Summe l).
Je Streifen: gleichfoermiges zyklisches Wort aus l_t Aufwaerts- und l_{t+1} Abwaertsdreiecken mit zufaelligen Anfangsecken.
Ergebnis wird mit netzdyn.Netz (unveraendert) als Komplex aufgebaut, gepruefft (Netz.pruefe) und per Netz.dual() zum
dualen Netz; Messung mit denselben Werkzeugen wie in NETZ-DYN-1 (dseich.Summe).
"""
import argparse, json, math, os, sys, time
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import dseich
import netzdyn as nd

LG = [0.0]   # LG[k] = lgamma(k) (Tabelle, in main gefuellt), LG[0] unbenutzt


def tabelle(maxk):
    global LG
    LG = [0.0] + [math.lgamma(k) for k in range(1, maxk + 1)]


def w(a, b):
    return LG[a + b] - LG[a] - LG[b + 1]


class LKette:
    def __init__(self, T, S, seed, lmin=3):
        self.T = T
        self.l = [S // T] * T
        for i in range(S - sum(self.l)):
            self.l[i] += 1
        import random
        self.rng = random.Random(seed)
        self.lmin = lmin
        self.versuche = 0
        self.angenommen = 0

    def bewegen(self, n):
        l, T, rr, lmin = self.l, self.T, self.rng.random, self.lmin
        acc = 0
        for _ in range(n):
            t = int(rr() * T)
            s = int(rr() * T)
            if s == t or l[s] <= lmin:
                continue
            strips = {(t - 1) % T, t, (s - 1) % T, s}
            alt = 0.0
            for k in strips:
                alt += w(l[k], l[(k + 1) % T])
            l[t] += 1
            l[s] -= 1
            neu = 0.0
            for k in strips:
                neu += w(l[k], l[(k + 1) % T])
            d = neu - alt
            if d >= 0 or rr() < math.exp(d):
                acc += 1
            else:
                l[t] -= 1
                l[s] += 1
        self.versuche += n
        self.angenommen += acc


def baue(l, rng):
    T = len(l)
    off = np.concatenate([[0], np.cumsum(l)]).astype(np.int64)
    sims = []
    for t in range(T):
        t1 = (t + 1) % T
        a, b = l[t], l[t1]
        word = np.array([0] * a + [1] * b)
        rng.shuffle(word)
        iu = int(rng.integers(a))
        idn = int(rng.integers(b))
        ot, o1 = int(off[t]), int(off[t1])
        for x in word.tolist():
            if x == 0:
                sims.append(tuple(sorted((ot + iu, ot + (iu + 1) % a, o1 + idn))))
                iu = (iu + 1) % a
            else:
                sims.append(tuple(sorted((ot + iu, o1 + idn, o1 + (idn + 1) % b))))
                idn = (idn + 1) % b
    vt = {}
    for t in range(T):
        for i in range(l[t]):
            vt[int(off[t]) + i] = t
    return sims, vt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--T', type=int, required=True)
    ap.add_argument('--N', type=int, required=True, help='Zahl der Dreiecke (2 mal Summe l)')
    ap.add_argument('--nsamp', type=int, default=100000)
    ap.add_argument('--therm_zuege', type=float, default=0.0, help='Zuege zur Thermalisierung (0: 40 l^2 T)')
    ap.add_argument('--gap_zuege', type=float, default=0.0, help='Zuege zwischen Proben (0: gap_faktor l^2 T)')
    ap.add_argument('--therm_faktor', type=float, default=10.0, help='Thermalisierung = Faktor * l^2 T Zuege')
    ap.add_argument('--gap_faktor', type=float, default=0.5, help='Abstand = Faktor * l^2 T Zuege (Relaxationszeit ~ 0,5 l^2 T)')
    ap.add_argument('--ds_starts', type=int, default=24)
    ap.add_argument('--ds_smax', type=int, default=600)
    ap.add_argument('--sch_starts', type=int, default=16)
    ap.add_argument('--sch_rmax', type=int, default=150)
    ap.add_argument('--ds_jede', type=int, default=1)
    ap.add_argument('--zeit', type=float, default=480.0)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--aus', required=True)
    args = ap.parse_args()
    t0 = time.time()
    S = args.N // 2
    tabelle(2 * S + 5)
    ch = LKette(args.T, S, args.seed)
    lm = S / args.T
    therm = int(args.therm_zuege or args.therm_faktor * lm * lm * args.T)
    gap = int(args.gap_zuege or args.gap_faktor * lm * lm * args.T)
    rng = np.random.default_rng(args.seed)
    Sm = dseich.Summe(args.sch_rmax, args.ds_smax)
    # Thermalisierung in Stuecken (Zeitgrenze beachten)
    done = 0
    chunk = 200000
    reihe_th = []
    while done < therm and time.time() - t0 < args.zeit * 0.6:
        n = min(chunk, therm - done)
        ch.bewegen(n)
        done += n
        lv = np.array(ch.l, dtype=float)
        reihe_th.append((done, float(lv.std() / lv.mean()), float(lv.max() / lv.mean())))
    print('Thermalisierung %d von %d Zuegen, t=%.0f, Annahme %.3f' % (done, therm, time.time() - t0,
                                                                        ch.angenommen / max(ch.versuche, 1)), flush=True)
    relstreu, maxmit, lmins = [], [], []
    pruef = None
    i = 0
    while i < args.nsamp and time.time() - t0 < args.zeit and done >= therm:
        if i > 0:
            ch.bewegen(gap)
        l = list(ch.l)
        lv = np.array(l, dtype=float)
        relstreu.append(float(lv.std() / lv.mean()))
        maxmit.append(float(lv.max() / lv.mean()))
        lmins.append(int(lv.min()))
        sims, vt = baue(l, rng)
        net = nd.Netz(2, args.T, True, args.seed + i, sims, vt)
        if i == 0:
            pruef = net.pruefe()
            prof = net.profil()
            assert prof == l, 'Profil stimmt nicht mit l ueberein'
        nb, _ = net.dual()
        ds_st = args.ds_starts if i % args.ds_jede == 0 else 0
        rm = Sm.messe(nb, rng, ds_st, args.sch_starts, args.sch_rmax, args.ds_smax)
        Sm.reihe.append((i, rm, round(time.time() - t0, 1)))
        i += 1
        if i % 5 == 0:
            print('probe %d rmean=%.3f relstreu=%.3f t=%.0f' % (i, rm, relstreu[-1], time.time() - t0), flush=True)
    extra = {'art': 'cdt-exakt', 'N': 2 * S, 'T': args.T, 'proben': i, 'pruefung': pruef,
             'profil_relstreu': float(np.mean(relstreu)) if relstreu else None,
             'profil_max_durch_mittel': float(np.mean(maxmit)) if maxmit else None, 'l_min_mittel': float(np.mean(lmins)) if lmins else None,
             'therm_reihe': reihe_th[-20:], 'annahme': ch.angenommen / max(ch.versuche, 1), 'therm_zuege': done,
             'gap_zuege': gap}
    out = dseich.ausgabe(Sm, args, extra, time.time() - t0)
    tmp = args.aus + '.json.neu'
    with open(tmp, 'w') as f:
        json.dump(out, f)
    os.replace(tmp, args.aus + '.json')
    print('fertig proben=%d t=%.0f' % (i, time.time() - t0), flush=True)


if __name__ == '__main__':
    main()
