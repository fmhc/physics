#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DS-EICHUNG-2D-1: Zufallskarten mit bekannter Antwort, gemessen mit den unveraenderten Werkzeugen aus NETZ-DYN-1
(netzdyn.schalen, netzdyn.rueckkehr, netzdyn.ds_kurve).

  --art quad : gleichfoermige Zufallsviereckskarten der Kugel, exakt (Cori-Vauquelin-Schaeffer), N = Zahl der Vierecke
  --art flip : Zufallstriangulierungen der Kugel (einfach) per Flip-Markov-Kette, N = Zahl der Dreiecke
Ausgabe: JSON mit Schalensumme, P-Summe, d_s-Kurve, lokale d_H, <r> je Probe.
"""
import argparse, json, math, os, pickle, random, sys, time, platform
import numpy as np

sys.path.insert(0, os.environ.get('NETZDYN_CODE', '/home/fmh/fmhc-physics-remote/netz-dyn-1/code'))
import netzdyn as nd  # unveraendert (sha256 siehe PRUEFSUMMEN)


# ---------------------------------------------------------------- Viereckskarten (CVS)
def quad_sample(n, rng):
    """Gibt (nb, info): nb = (n,4) duales Netz einer gleichfoermigen Viereckskarte der Kugel mit n Flaechen."""
    # 1. Dyck-Pfad der Laenge 2n (Zyklenlemma)
    steps = np.array([1] * n + [-1] * (n + 1))
    rng.shuffle(steps)
    cs = np.cumsum(steps)
    k = int(np.argmin(cs))               # erste Position des Minimums
    steps = np.concatenate([steps[k + 1:], steps[:k + 1]])
    assert steps[-1] == -1 and np.all(np.cumsum(steps)[:-1] >= 0)
    steps = steps[:-1]
    # 2. Baum, Etiketten, Ecken an den Ecken (Corners)
    nv = n + 1
    parent = np.zeros(nv, dtype=np.int64)
    lab = np.zeros(nv, dtype=np.int64)
    delta = rng.integers(-1, 2, size=nv)
    cur = 0
    nxt = 1
    stack = [0]
    corner_v = np.empty(2 * n, dtype=np.int64)
    for i in range(2 * n):
        if steps[i] == 1:
            v = nxt
            nxt += 1
            parent[v] = cur
            lab[v] = lab[cur] + delta[v]
            stack.append(v)
            cur = v
        else:
            stack.pop()
            cur = stack[-1]
        corner_v[i] = cur
    lab = lab - lab.min() + 1
    clab = lab[corner_v]
    # 3. Zusatzstelle Z (Ecke 0) hinter einer Ecke mit Etikett 1
    c1 = int(np.nonzero(clab == 1)[0][0])
    L = 2 * n + 1
    seq_lab = np.concatenate([clab[:c1 + 1], [0], clab[c1 + 1:]])
    seq_v = np.concatenate([corner_v[:c1 + 1], [n + 1], corner_v[c1 + 1:]])
    # 4. Nachfolger: naechste Stelle vorwaerts (zyklisch) mit Etikett - 1
    succ = np.full(L, -1, dtype=np.int64)
    last = {}
    ll = seq_lab.tolist()
    for i in range(2 * L - 1, -1, -1):
        j = i % L
        if i < L:
            if ll[j] >= 1:
                succ[j] = last[ll[j] - 1]
        last[ll[j]] = i % L
    # 5. Rotationssystem aus den Sehnen; Sehne q -> succ[q], Darts 2q (bei q) und 2q+1 (bei succ[q])
    arcs = [[] for _ in range(L)]
    zpos = c1 + 1
    for q in range(L):
        s = int(succ[q])
        if s < 0:
            continue
        cid = q if q < zpos else q - 1
        arcs[q].append(((s - q) % L, 2 * cid))
        arcs[s].append(((q - s) % L, 2 * cid + 1))
    # Ecke -> Stellen (in Konturreihenfolge); Rotation: Stellen rueckwaerts, je Stelle nach wachsender Vorwaertsdistanz
    pos_of = {}
    for p in range(L):
        pos_of.setdefault(int(seq_v[p]), []).append(p)
    sigma = np.empty(4 * n, dtype=np.int64)
    for v, ps in pos_of.items():
        ds = []
        for p in reversed(ps):
            a = arcs[p]
            a.sort()
            ds.extend(d for _, d in a)
        m = len(ds)
        for i in range(m):
            sigma[ds[i]] = ds[(i + 1) % m]
    # 6. Flaechen = Zyklen von d -> sigma[d ^ 1]
    nd_ = 4 * n
    fid = np.full(nd_, -1, dtype=np.int64)
    nf = 0
    flen = []
    sg = sigma.tolist()
    fl = [-1] * nd_
    for d0 in range(nd_):
        if fl[d0] >= 0:
            continue
        d = d0
        c = 0
        while fl[d] < 0:
            fl[d] = nf
            c += 1
            d = sg[d ^ 1]
        flen.append(c)
        nf += 1
    fid = np.array(fl, dtype=np.int64)
    nV = len(pos_of)
    chi = nV - 2 * n + nf
    ok = (chi == 2) and nf == n and all(x == 4 for x in flen)
    if not ok:
        return None, {'chi': chi, 'faces': nf, 'flen': sorted(set(flen)), 'ok': False}
    # 7. Duales Netz: je Flaeche vier Darts, Nachbar = Flaeche des Gegendarts
    nb = np.empty((n, 4), dtype=np.int64)
    cnt = np.zeros(n, dtype=np.int64)
    for d in range(nd_):
        f = fl[d]
        nb[f, cnt[f]] = fl[d ^ 1]
        cnt[f] += 1
    loops = int(np.sum(nb == np.arange(n)[:, None]))
    return nb, {'chi': chi, 'faces': nf, 'ok': True, 'schleifen': loops, 'max_label': int(lab.max())}


# ---------------------------------------------------------------- Triangulierung (Flips)
class Flip:
    def __init__(self, m, seed):
        """Bipyramide: Ring aus m Ecken plus zwei Pole -> N = 2 m Dreiecke."""
        self.rng = random.Random(seed)
        self.m = m
        N = 2 * m
        self.N = N
        # Ecken: Ring 0..m-1, Nordpol m, Suedpol m+1; Dreiecke ccw von aussen gesehen
        tri, nbr = [], []
        for i in range(m):
            j = (i + 1) % m
            tri.append([m, i, j])          # Nord: Dreieck i
        for i in range(m):
            j = (i + 1) % m
            tri.append([m + 1, j, i])      # Sued: Dreieck m + i
        for i in range(m):
            # Nord i = (N, i, j): gegenueber N: Kante (i,j) -> Sued i; gegenueber i: Kante (j,N) -> Nord i+1;
            # gegenueber j: Kante (N,i) -> Nord i-1
            nbr.append([m + i, (i + 1) % m, (i - 1) % m])
        for i in range(m):
            # Sued i = (S, j, i): gegenueber S: Kante (j,i) -> Nord i; gegenueber j: Kante (i,S) -> Sued i-1;
            # gegenueber i: Kante (S,j) -> Sued i+1
            nbr.append([i, m + (i - 1) % m, m + (i + 1) % m])
        self.tri, self.nbr = tri, nbr
        self.edges = set()
        V = m + 2
        self.V = V
        for t in tri:
            for x in range(3):
                a, b = t[x], t[(x + 1) % 3]
                self.edges.add(a * V + b if a < b else b * V + a)
        self.deg = [4] * m + [m, m]
        self.versuche = 0
        self.angenommen = 0

    def sweep(self):
        tri, nbr, rng, V, edges, deg = self.tri, self.nbr, self.rng, self.V, self.edges, self.deg
        N = self.N
        acc = 0
        rr = rng.random
        for _ in range(N):
            t = int(rr() * N)
            i = int(rr() * 3)
            u = nbr[t][i]
            tt = tri[t]
            a = tt[i]
            b = tt[(i + 1) % 3]
            c = tt[(i + 2) % 3]
            if deg[b] < 4 or deg[c] < 4:
                continue
            nu = nbr[u]
            j = nu.index(t)
            tu = tri[u]
            d = tu[j]
            if a == d:
                continue
            key = a * V + d if a < d else d * V + a
            if key in edges:
                continue
            # u = (d, c, b) in zyklischer Reihenfolge ab Index j: tu[j]=d, tu[j+1]=c, tu[j+2]=b
            nt = nbr[t]
            n_t1 = nt[(i + 1) % 3]      # Kante (c,a) gegenueber b
            n_t2 = nt[(i + 2) % 3]      # Kante (a,b) gegenueber c
            n_u1 = nu[(j + 1) % 3]      # gegenueber c: Kante (b,d)
            n_u2 = nu[(j + 2) % 3]      # gegenueber b: Kante (d,c)
            # neu t' = (a,b,d) (id t), u' = (a,d,c) (id u)
            tri[t] = [a, b, d]
            nbr[t] = [n_u1, u, n_t2]
            tri[u] = [a, d, c]
            nbr[u] = [n_u2, n_t1, t]
            # Rueckzeiger: n_u1 zeigte auf u -> jetzt t ; n_t1 zeigte auf t -> jetzt u
            x = nbr[n_u1]
            x[x.index(u)] = t
            x = nbr[n_t1]
            x[x.index(t)] = u
            ek = b * V + c if b < c else c * V + b
            edges.discard(ek)
            edges.add(key)
            deg[a] += 1
            deg[d] += 1
            deg[b] -= 1
            deg[c] -= 1
            acc += 1
        self.versuche += N
        self.angenommen += acc
        return acc

    def netz(self):
        return np.array(self.nbr, dtype=np.int64)

    def pruefe(self):
        N = self.N
        V = self.V
        # Nachbarschaft symmetrisch, Dreiecke genau zwei Nachbarn je Kante, Eulerzahl 2, einfach
        for t in range(N):
            for k in range(3):
                u = self.nbr[t][k]
                assert t in self.nbr[u]
                tt, uu = self.tri[t], self.tri[u]
                f = {tt[(k + 1) % 3], tt[(k + 2) % 3]}
                assert f <= set(uu), (t, u)
        E = len(self.edges)
        assert V - E + N == 2, (V, E, N)
        assert sum(self.deg) == 2 * E
        return {'V': V, 'E': E, 'F': N, 'chi': V - E + N, 'deg_max': max(self.deg), 'deg_min': min(self.deg)}


# ---------------------------------------------------------------- Messung (Methode wie NETZ-DYN-1)
class Summe:
    def __init__(self, rmax, smax):
        self.sch = np.zeros(rmax + 1)
        self.nsch = 0
        self.P = np.zeros(smax + 1)
        self.nP = 0
        self.rmean = []         # mittlerer Abstand je Probe (aus deren Schalen)
        self.reihe = []         # (Index, rmean, Zeit)

    def messe(self, nb, rng, ds_starts, sch_starts, rmax, smax):
        n = nb.shape[0]
        starts = rng.choice(n, size=min(ds_starts, n), replace=False)
        P = nd.rueckkehr(nb, starts, smax) if ds_starts > 0 else None
        if P is not None:
            self.P += P
            self.nP += 1
        sc_sum = np.zeros(rmax + 1)
        k = 0
        sts = rng.choice(n, size=min(sch_starts, n), replace=False)
        for st in sts:
            sc = np.array(nd.schalen(nb, int(st), rmax), dtype=float)
            if sc.size > sc_sum.size:
                raise ValueError('rmax zu klein')
            sc_sum[:sc.size] += sc
            k += 1
        self.sch += sc_sum
        self.nsch += k
        rs = np.arange(rmax + 1)
        rm = float((rs * sc_sum).sum() / sc_sum.sum())
        self.rmean.append(rm)
        return rm


def ausgabe(S, args, extra, t_lauf):
    out = {'karte': 'DS-EICHUNG-2D-1', 'args': vars(args), 'python': platform.python_version(), 'numpy': np.__version__,
           'laufzeit_s': t_lauf}
    out.update(extra)
    sch = S.sch / max(S.nsch, 1)
    out['schalen'] = sch.tolist()
    out['n_schalen'] = S.nsch
    out['rmean_proben'] = S.rmean
    if S.nP > 0:
        P = S.P / S.nP
        out['P_rueck'] = P.tolist()
        out['ds'] = nd.ds_kurve(P)
        out['n_P'] = S.nP
    loc = []
    for r in range(2, len(sch) - 1):
        if sch[r + 1] > 0 and sch[r - 1] > 0:
            loc.append((r, 1.0 + (math.log(sch[r + 1]) - math.log(sch[r - 1])) / (math.log(r + 1) - math.log(r - 1))))
    out['dH_lokal'] = loc
    out['reihe'] = S.reihe
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--art', choices=['quad', 'flip'], required=True)
    ap.add_argument('--N', type=int, required=True, help='Zahl der Flaechen (Vierecke bzw. Dreiecke)')
    ap.add_argument('--nsamp', type=int, default=100000)
    ap.add_argument('--ds_starts', type=int, default=24)
    ap.add_argument('--ds_smax', type=int, default=600)
    ap.add_argument('--sch_starts', type=int, default=16)
    ap.add_argument('--sch_rmax', type=int, default=150)
    ap.add_argument('--zeit', type=float, default=520.0)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--therm', type=int, default=200, help='flip: Thermalisierungs-Sweeps (nur beim ersten Abschnitt)')
    ap.add_argument('--gap', type=int, default=20, help='flip: Sweeps zwischen Proben')
    ap.add_argument('--ds_jede', type=int, default=1, help='d_s nur bei jeder k-ten Probe')
    ap.add_argument('--aus', required=True)
    ap.add_argument('--fort', default='')
    args = ap.parse_args()
    t0 = time.time()
    rng = np.random.default_rng(args.seed)
    S = Summe(args.sch_rmax, args.ds_smax)
    extra = {'art': args.art, 'N': args.N}
    if args.art == 'quad':
        nsok = 0
        fehler = []
        loops = []
        i = 0
        while i < args.nsamp and time.time() - t0 < args.zeit:
            nb, info = quad_sample(args.N, rng)
            if not info['ok']:
                fehler.append(info)
                print('FEHLER Pruefung', info, flush=True)
                break
            loops.append(info['schleifen'])
            ds_st = args.ds_starts if (i % args.ds_jede == 0) else 0
            rm = S.messe(nb, rng, ds_st, args.sch_starts, args.sch_rmax, args.ds_smax)
            S.reihe.append((i, rm, round(time.time() - t0, 1)))
            i += 1
            if i % 10 == 0 or args.N >= 30000:
                print('probe %d rmean=%.3f t=%.0f' % (i, rm, time.time() - t0), flush=True)
        extra.update({'proben': i, 'pruef_fehler': fehler, 'schleifen_mittel': float(np.mean(loops)) if loops else None})
    else:
        if args.fort and os.path.exists(args.fort):
            with open(args.fort, 'rb') as f:
                fl = pickle.load(f)
            print('fortgesetzt: Sweeps %d' % fl.sweeps, flush=True)
        else:
            fl = Flip(args.N // 2, args.seed)
            fl.sweeps = 0
            fl.therm_fertig = False
        fl.rng.seed(args.seed + 1000 * (fl.sweeps + 1))
        extra['pruefung_start'] = fl.pruefe()
        i = 0
        while time.time() - t0 < args.zeit and i < args.nsamp:
            n_sw = args.gap if fl.sweeps >= args.therm else min(args.gap, args.therm - fl.sweeps)
            for _ in range(n_sw):
                fl.sweep()
                fl.sweeps += 1
                if time.time() - t0 > args.zeit:
                    break
            if time.time() - t0 > args.zeit:
                break
            nb = fl.netz()
            # Zeitreihe von <r> auch in der Thermalisierung (nur Schalen, kein d_s)
            if fl.sweeps >= args.therm:
                ds_st = args.ds_starts if (i % args.ds_jede == 0) else 0
                rm = S.messe(nb, rng, ds_st, args.sch_starts, args.sch_rmax, args.ds_smax)
                S.reihe.append((fl.sweeps, rm, round(time.time() - t0, 1)))
                i += 1
            else:
                sc = np.zeros(args.sch_rmax + 1)
                for st in rng.choice(nb.shape[0], size=8, replace=False):
                    s_ = np.array(nd.schalen(nb, int(st), args.sch_rmax), dtype=float)
                    sc[:s_.size] += s_
                rm = float((np.arange(args.sch_rmax + 1) * sc).sum() / sc.sum())
                S.reihe.append((fl.sweeps, rm, round(time.time() - t0, 1), 'therm'))
            print('sweep %d rmean=%.3f t=%.0f' % (fl.sweeps, rm, time.time() - t0), flush=True)
        extra['pruefung_ende'] = fl.pruefe()
        extra.update({'proben': i, 'sweeps': fl.sweeps, 'annahme': fl.angenommen / max(fl.versuche, 1),
                      'deg_max': max(fl.deg)})
        if args.fort:
            tmp = args.fort + '.neu'
            with open(tmp, 'wb') as f:
                pickle.dump(fl, f, protocol=pickle.HIGHEST_PROTOCOL)
            os.replace(tmp, args.fort)
    out = ausgabe(S, args, extra, time.time() - t0)
    tmp = args.aus + '.json.neu'
    with open(tmp, 'w') as f:
        json.dump(out, f)
    os.replace(tmp, args.aus + '.json')
    print('fertig proben=%s t=%.0f' % (extra.get('proben'), time.time() - t0), flush=True)


if __name__ == '__main__':
    main()
