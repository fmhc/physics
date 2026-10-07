#!/usr/bin/env python3
# QBALL-PYRO-1 (Runde 37): M1 auf dem Pyrochlor-Gitter. Lineares Spektrum, exakte Ringzustaende,
# Bogoliubov-Stabilitaet, Zeitentwicklung mit Rauschen und Stoss, Vergleichsball (h = 0,5, omega^2 = 0,7).
#
# Gitter: ganzzahlige Koordinaten in Einheiten a/8 (a = kubische Zellkante), Torus aus L^3 kubischen Zellen,
#   16 Knoten je Zelle (fcc mit Tetraeder-Basis). Naechster Nachbar |(0,2,2)| = 2 sqrt(2) Einheiten = h.
#   Physikalische Laenge x = Einheiten * h / (2 sqrt 2). Volumen je Knoten v_s = a^3/16 = sqrt(2) h^3.
# Modell: phi_tt = (A - 6) phi / h^2 - U'(|phi|^2) phi,  U(S) = S - S^2 + S^3/2.
# Energie E = v_s [ sum |phi_t|^2 + sum U + (1/h^2) sum_Kanten |phi_i - phi_j|^2 ],
# Ladung Q = v_s sum 2 Im(conj(phi) phi_t)  (phi ~ exp(+i omega t) hat Q > 0).
import sys, json, math, time, argparse
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

BETA = 0.5
SQ2 = math.sqrt(2.0)


def U(S):
    return S - S * S + BETA * S ** 3


def U1(S):
    return 1.0 - 2.0 * S + 3.0 * BETA * S * S


def U2(S):
    return -2.0 + 6.0 * BETA * S


FCC = np.array([[0, 0, 0], [0, 4, 4], [4, 0, 4], [4, 4, 0]])
BAS = np.array([[0, 0, 0], [0, 2, 2], [2, 0, 2], [2, 2, 0]])


def minbild(d, P):
    return d - P * np.round(d / P)


def gitter(L):
    """Pyrochlor-Torus aus L^3 kubischen Zellen. Gibt Knoten, Tetraeder, Nachbarn, Kanten, Pruefungen."""
    P = 8 * L
    cells = np.array([(x, y, z) for x in range(L) for y in range(L) for z in range(L)])
    fccp = (cells[:, None, :] * 8 + FCC[None, :, :]).reshape(-1, 3) % P
    pos = (fccp[:, None, :] + BAS[None, :, :]).reshape(-1, 3) % P
    sub = np.tile(np.arange(4), len(fccp))
    N = len(pos)

    def key(p):
        return (int(p[0]) * P + int(p[1])) * P + int(p[2])
    idx = {key(p): i for i, p in enumerate(pos)}
    up = np.array([[idx[key((f + b) % P)] for b in BAS] for f in fccp])
    dn = np.array([[idx[key((f - b) % P)] for b in BAS] for f in fccp])
    tet = np.vstack([up, dn])
    nb = [[] for _ in range(N)]
    tet_of = [[] for _ in range(N)]
    for t, s4 in enumerate(tet):
        for i in s4:
            tet_of[i].append(t)
            for j in s4:
                if j != i:
                    nb[i].append(int(j))
    pr = {}
    pr["knoten"] = N
    pr["knoten_soll"] = 16 * L ** 3
    pr["tetraeder"] = int(len(tet))
    pr["tetraeder_je_knoten_min_max"] = [min(len(t) for t in tet_of), max(len(t) for t in tet_of)]
    pr["tetraeder_4_verschiedene"] = bool(all(len(set(s4.tolist())) == 4 for s4 in tet))
    grad = [len(set(n)) for n in nb]
    pr["nachbarn_min_max"] = [min(grad), max(grad)]
    pr["nachbarn_ohne_doppel"] = bool(all(len(set(n)) == len(n) for n in nb))
    nb = np.array(nb, dtype=np.int64)
    tet_of = np.array(tet_of, dtype=np.int64)
    d = minbild(pos[nb] - pos[:, None, :], P)
    d2 = (d ** 2).sum(2)
    pr["nachbar_abstand2_min_max_einheiten"] = [int(d2.min()), int(d2.max())]  # Soll 8
    # Kanten (i < j)
    ii = np.repeat(np.arange(N), 6)
    jj = nb.ravel()
    m = ii < jj
    kanten = np.stack([ii[m], jj[m]], 1)
    pr["kanten"] = int(len(kanten))
    pr["kanten_soll"] = 48 * L ** 3
    rows = np.repeat(np.arange(N), 6)
    A = sp.csr_matrix((np.ones(6 * N), (rows, nb.ravel())), shape=(N, N))
    pr["A_symmetrisch"] = bool(abs(A - A.T).sum() == 0)
    # Inversionssymmetrie jedes Knotens: Nachbarn paarweise +-d
    dsum = d.sum(1)
    pr["knoten_inversionssymmetrisch"] = bool(np.all(dsum == 0))
    return dict(L=L, P=P, N=N, pos=pos, sub=sub, tet=tet, tet_of=tet_of, nb=nb, kanten=kanten, A=A, pruef=pr)


def phys(g, h):
    return g["pos"] * (h / (2.0 * SQ2))


def boxlaenge(g, h):
    return g["P"] * h / (2.0 * SQ2)


# ---------------------------------------------------------------- Hexagone
def kanten_tet(g, i, j):
    s = set(g["tet_of"][i].tolist()) & set(g["tet_of"][j].tolist())
    assert len(s) == 1
    return s.pop()


def sechserwege(g, s0):
    """Alle geschlossenen Wege der Laenge 6 ab s0; einfache Zyklen mit Tetraeder- und Eigenvektorpruefung."""
    nb = g["nb"]
    A = g["A"]
    wege = 0
    einfach = []
    stack = [(s0,)]
    while stack:
        w = stack.pop()
        if len(w) == 7:
            if w[-1] == s0:
                wege += 1
                if len(set(w[:6])) == 6:
                    einfach.append(w[:6])
            continue
        for j in nb[w[-1]]:
            stack.append(w + (int(j),))
    res = []
    for c in einfach:
        tets = [kanten_tet(g, c[k], c[(k + 1) % 6]) for k in range(6)]
        v = np.zeros(g["N"])
        for k in range(6):
            v[c[k]] = (-1) ** k
        r = A @ v + 2.0 * v
        res.append(dict(zyklus=list(map(int, c)), tetraeder_verschieden=len(set(tets)) == 6,
                        resid_inf=float(np.abs(r).max())))
    return wege, res


def ring_vektor(g, zyklus):
    v = np.zeros(g["N"])
    for k in range(6):
        v[zyklus[k]] = (-1) ** k
    return v


def ring_pruef(g, zyklus):
    """Pruefungen am Ring: keine Sehnen, jeder Aussennachbar sieht genau zwei Ringknoten mit entgegengesetztem Vorzeichen."""
    v = ring_vektor(g, zyklus)
    rs = set(zyklus)
    nb = g["nb"]
    sehnen = 0
    for k, i in enumerate(zyklus):
        rn = [j for j in nb[i] if j in rs]
        if len(rn) != 2:
            sehnen += 1
    aussen = {}
    for i in zyklus:
        for j in nb[i]:
            if j not in rs:
                aussen.setdefault(int(j), []).append(int(i))
    zwei = all(len(l) == 2 for l in aussen.values())
    summe0 = all(v[l[0]] + v[l[1]] == 0 for l in aussen.values() if len(l) == 2)
    tets = [kanten_tet(g, zyklus[k], zyklus[(k + 1) % 6]) for k in range(6)]
    # oben/unten-Wechsel: oben = Index < 4 L^3
    nup = 4 * g["L"] ** 3
    art = [int(t < nup) for t in tets]
    wechsel = all(art[k] != art[(k + 1) % 6] for k in range(6))
    r = g["A"] @ v + 2.0 * v
    return dict(ringknoten_mit_2_ringnachbarn=(sehnen == 0), aussennachbarn=len(aussen),
                aussen_je_genau_2_ringknoten=bool(zwei), aussen_summe_null=bool(summe0),
                tetraeder_verschieden=len(set(tets)) == 6, tetraeder_wechseln_oben_unten=bool(wechsel),
                resid_Av_plus_2v_inf=float(np.abs(r).max()))


def ring_nahe_mitte(g):
    """Hexagon mit Mittelpunkt nahe der Torusmitte."""
    P = g["P"]
    c = np.array([P / 2.0] * 3)
    d = minbild(g["pos"] - c, P)
    s0 = int(np.argmin((d ** 2).sum(1)))
    wege, res = sechserwege(g, s0)
    z = res[0]["zyklus"]
    pts = g["pos"][z].astype(float)
    m = pts[0] + minbild(pts - pts[0], P).mean(0)
    return z, m, s0, wege, res


# ---------------------------------------------------------------- lineares Spektrum
def bloch_eig(k):
    """k in 1/Einheit (a = 8 Einheiten), Form (n,3). A_st(k) = 2 cos(k.(b_t - b_s))."""
    D = BAS[None, :, :] - BAS[:, None, :]          # D[s,t] = b_t - b_s
    ph = np.einsum("nc,stc->nst", k, D.astype(float))
    H = 2.0 * np.cos(ph)
    idx = np.arange(4)
    H[:, idx, idx] = 0.0
    return np.linalg.eigvalsh(H)


def modus_linear(a):
    t0 = time.time()
    out = {"modus": "linear"}
    G = np.array([[-1, 1, 1], [1, -1, 1], [1, 1, -1]]) / 8.0
    n = a.nk
    m = np.array([(i, j, l) for i in range(n) for j in range(n) for l in range(n)], float) / n
    k = 2 * math.pi * m @ G
    rng = np.random.default_rng(12345)
    kz = 2 * math.pi * rng.random((a.nzufall, 3)) @ G
    ev = np.vstack([bloch_eig(k), bloch_eig(kz)])
    flach = ev[:, :2]
    out["k_punkte"] = int(len(ev))
    out["flach_abw_max"] = float(np.abs(flach + 2.0).max())
    out["band3_min"] = float(ev[:, 2].min())
    out["band4_max"] = float(ev[:, 3].max())
    out["band3_max"] = float(ev[:, 2].max())
    out["band4_min"] = float(ev[:, 3].min())
    # Pfad Gamma-X-W-L-Gamma-K (Einheiten 2 pi / a, a = 8)
    pkt = {"G": [0, 0, 0], "X": [0, 1, 0], "W": [0.5, 1, 0], "L": [0.5, 0.5, 0.5], "K": [0.75, 0.75, 0]}
    weg = ["G", "X", "W", "L", "G", "K"]
    ks = []
    marks = [0]
    for p, q in zip(weg[:-1], weg[1:]):
        P0 = np.array(pkt[p]) * 2 * math.pi / 8
        P1 = np.array(pkt[q]) * 2 * math.pi / 8
        for s in np.linspace(0, 1, 120, endpoint=False):
            ks.append(P0 + s * (P1 - P0))
        marks.append(len(ks))
    ks.append(np.array(pkt["K"]) * 2 * math.pi / 8)
    ks = np.array(ks)
    seg = np.r_[0, np.cumsum(np.linalg.norm(np.diff(ks, axis=0), axis=1))]
    evp = bloch_eig(ks)
    out["pfad"] = dict(s=seg.tolist(), ev=evp.tolist(), marken=[float(seg[min(i, len(seg) - 1)]) for i in marks],
                       namen=weg)
    # Realraum gegen k-Raum
    g = gitter(a.Lreal)
    out["gitter_pruef"] = g["pruef"]
    Ad = g["A"].toarray()
    evr = np.linalg.eigvalsh(Ad)
    Lr = a.Lreal
    nn = np.arange(2 * Lr)
    kc = np.array([(i, j, l) for i in nn for j in nn for l in nn], float) * 2 * math.pi / (8 * Lr)
    evk = np.sort(bloch_eig(kc).ravel())[::2]
    out["realraum_gegen_k_max"] = float(np.abs(np.sort(evr) - evk).max())
    out["realraum_anzahl_bei_minus2"] = int(np.sum(np.abs(evr + 2.0) < 1e-9))
    out["realraum_anzahl_soll"] = int(8 * Lr ** 3 + 1)
    out["realraum_min_max"] = [float(evr.min()), float(evr.max())]
    # Hexagon und Sechserwege
    z, m_, s0, wege, res = ring_nahe_mitte(g)
    out["sechserwege_ab_s0"] = dict(geschlossene_wege=wege, einfache_zyklen_gerichtet=len(res),
                                    alle_einfachen_tetraeder_verschieden=all(r["tetraeder_verschieden"] for r in res),
                                    alle_einfachen_eigenvektor=all(r["resid_inf"] == 0.0 for r in res),
                                    resid_max=max(r["resid_inf"] for r in res))
    # Gegenbeispiel: Dreieck zweimal durchlaufen (geschlossener Sechserweg, kein Ring)
    t = g["tet"][g["tet_of"][s0][0]]
    tri = [int(t[0]), int(t[1]), int(t[2])]
    v = np.zeros(g["N"])
    for kk, i in enumerate(tri * 2):
        v[i] += (-1) ** kk
    out["gegenbeispiel_dreieck_zweimal"] = dict(knoten=tri, vektor_null=bool(np.all(v == 0)))
    # Ringpruefung auf mehreren Gittern
    rp = {}
    for Lx in sorted(set([2, 3, 4, a.Lreal, 8])):
        gx = gitter(Lx)
        zx, mx, s0x, _, _ = ring_nahe_mitte(gx)
        rp[str(Lx)] = ring_pruef(gx, zx)
        rp[str(Lx)]["gitter_pruef"] = gx["pruef"]
    out["ring_pruef"] = rp
    out["zeit_s"] = time.time() - t0
    return out


# ---------------------------------------------------------------- Zeitentwicklung
class Mess:
    def __init__(self, g, h, ring, Rw, X0):
        self.x = phys(g, h)
        self.Lb = boxlaenge(g, h)
        self.vs = SQ2 * h ** 3
        self.h2 = 1.0 / (h * h)
        self.kanten = g["kanten"]
        self.ring = np.zeros(g["N"], bool)
        if ring is not None:
            self.ring[ring] = True
        self.Rw = Rw
        self.X = np.array(X0, float)

    def energie(self, phi, p):
        S = phi.real ** 2 + phi.imag ** 2
        d = phi[self.kanten[:, 0]] - phi[self.kanten[:, 1]]
        return self.vs * (float(np.sum(p.real ** 2 + p.imag ** 2)) + float(np.sum(U(S)))
                          + self.h2 * float(np.sum(d.real ** 2 + d.imag ** 2)))

    def schwerpunkt(self, q):
        X = self.X.copy()
        for it in range(200):
            d = minbild(self.x - X, self.Lb)
            r = np.sqrt((d ** 2).sum(1))
            w = np.where(r < self.Rw, np.cos(0.5 * math.pi * r / self.Rw) ** 2, 0.0)
            wq = w * q
            s = wq.sum()
            dX = (wq[:, None] * d).sum(0) / s
            X = X + dX
            if np.abs(dX).max() < 1e-12:
                break
        self.X = X
        return X, float(s), it

    def __call__(self, t, phi, p):
        S = phi.real ** 2 + phi.imag ** 2
        q = 2.0 * (phi.real * p.imag - phi.imag * p.real) * self.vs
        Ssum = float(S.sum())
        aus = ~self.ring
        X, qw, it = self.schwerpunkt(q)
        return [t, float(S[aus].sum()) / Ssum, float(q[aus].sum()) / float(q.sum()), self.energie(phi, p),
                float(q.sum()), X[0], X[1], X[2], qw, float(np.sqrt(S[aus].max())) if aus.any() else 0.0]


SPALTEN = ["t", "leck_N", "leck_Q", "E", "Q", "X", "Y", "Z", "Q_fenster", "max_abs_phi_aussen"]


def entwickle(A, phi, p, h, dt, T, dmess, mess, wand=560.0, t_start=None):
    h2 = 1.0 / (h * h)
    nsteps = int(round(T / dt))
    nsub = int(round(dmess / dt))
    assert abs(nsub * dt - dmess) < 1e-12

    def F(ph):
        S = ph.real ** 2 + ph.imag ** 2
        return (A @ ph - 6.0 * ph) * h2 - U1(S) * ph
    f = F(phi)
    rec = [mess(0.0, phi, p)]
    t0 = time.time() if t_start is None else t_start
    status = "fertig"
    for k in range(1, nsteps + 1):
        p += (0.5 * dt) * f
        phi += dt * p
        f = F(phi)
        p += (0.5 * dt) * f
        if k % nsub == 0:
            rec.append(mess(k * dt, phi, p))
            if time.time() - t0 > wand:
                status = "wandzeit"
                break
    return np.array(rec), status


def ring_start(g, h, a2, rauschen, saat, kick, richtung):
    z, m, s0, _, _ = ring_nahe_mitte(g)
    v = ring_vektor(g, z)
    a = math.sqrt(a2)
    om2 = 8.0 / h ** 2 + U1(a2)
    om = math.sqrt(om2)
    x = phys(g, h)
    c = m * (h / (2.0 * SQ2))
    d = minbild(x - c, boxlaenge(g, h))
    e = np.array(richtung, float)
    e = e / np.linalg.norm(e)
    ph = np.exp(-1j * kick * om * (d @ e))
    phi = (a * v) * ph
    p = 1j * om * a * v * ph
    if rauschen > 0:
        rng = np.random.default_rng(saat)
        n = g["N"]
        phi = phi + rauschen * a * (rng.standard_normal(n) + 1j * rng.standard_normal(n)) / SQ2
        p = p + rauschen * a * om * (rng.standard_normal(n) + 1j * rng.standard_normal(n)) / SQ2
    return phi.astype(complex), p.astype(complex), z, c, om2, v


def modus_ring(a):
    """Stationaeres Residuum (QP1) und Zeitentwicklungen fuer alle Amplituden."""
    t0 = time.time()
    g = gitter(a.L)
    h = a.h
    out = {"modus": "ring", "L": a.L, "h": h, "dt": a.dt, "T": a.T, "rauschen": a.rauschen, "saat": a.saat,
           "kick": a.kick, "richtung": a.richtung, "Rw": a.Rw, "gitter_pruef": g["pruef"], "laeufe": {}}
    A = g["A"]
    for a2 in a.a2:
        phi, p, z, c, om2, v = ring_start(g, h, a2, a.rauschen, a.saat, a.kick, a.richtung)
        am = math.sqrt(a2)
        f = am * v
        R = -om2 * f - (A @ f - 6.0 * f) / h ** 2 + U1(f * f) * f
        mess = Mess(g, h, z, a.Rw * h, c)
        X0 = mess.schwerpunkt(2.0 * (phi.real * p.imag - phi.imag * p.real) * mess.vs)[0]
        mess.X = X0.copy()
        rec, status = entwickle(A, phi, p, h, a.dt, a.T, a.dmess, mess, wand=a.wand, t_start=t0)
        lauf = dict(a2=a2, omega2=om2, omega=math.sqrt(om2), ring=list(map(int, z)), mitte=c.tolist(),
                    resid_inf=float(np.abs(R).max()), resid_rel=float(np.abs(R).max() / (om2 * am)),
                    status=status, spalten=SPALTEN, reihe=rec.tolist(), X0=X0.tolist())
        out["laeufe"][str(a2)] = lauf
        print(f"a2={a2} om2={om2:.6f} resid={lauf['resid_rel']:.2e} leckN_max={rec[:,1].max():.3e} "
              f"leckN_end={rec[-1,1]:.3e} dE={np.abs(rec[:,3]-rec[0,3]).max()/rec[0,3]:.2e} "
              f"dQ={np.abs(rec[:,4]-rec[0,4]).max()/rec[0,4]:.2e} dX={np.linalg.norm(rec[-1,5:8]-rec[0,5:8]):.3e} "
              f"t={time.time()-t0:.1f}s {status}", flush=True)
        if status != "fertig":
            break
    out["zeit_s"] = time.time() - t0
    return out


# ---------------------------------------------------------------- Bogoliubov
def modus_bogo(a):
    t0 = time.time()
    g = gitter(a.L)
    h = a.h
    N = g["N"]
    z, m, s0, _, _ = ring_nahe_mitte(g)
    v = ring_vektor(g, z)
    Lap = g["A"].toarray() - 6.0 * np.eye(N)
    out = {"modus": "bogo", "L": a.L, "h": h, "N": N, "ring": list(map(int, z)), "amplituden": {}}
    for a2 in a.a2:
        t1 = time.time()
        am = math.sqrt(a2)
        f = am * v
        S = f * f
        om2 = 8.0 / h ** 2 + U1(a2)
        om = math.sqrt(om2)
        L0 = -Lap / h ** 2 + np.diag(U1(S) - om2)
        Lp = L0 + np.diag(2.0 * U2(S) * S)
        M = np.zeros((4 * N, 4 * N))
        I = np.eye(N)
        M[0:N, 2 * N:3 * N] = I
        M[N:2 * N, 3 * N:4 * N] = I
        M[2 * N:3 * N, 0:N] = -Lp
        M[2 * N:3 * N, 3 * N:4 * N] = 2.0 * om * I
        M[3 * N:4 * N, N:2 * N] = -L0
        M[3 * N:4 * N, 2 * N:3 * N] = -2.0 * om * I
        lam = np.linalg.eigvals(M)
        o = np.argsort(-lam.real)
        top = lam[o[:12]]
        out["amplituden"][str(a2)] = dict(a2=a2, omega2=om2, re_max=float(lam.real.max()),
                                          anzahl_re_gt_1e5=int(np.sum(lam.real > 1e-5)),
                                          anzahl_re_gt_1e3=int(np.sum(lam.real > 1e-3)),
                                          top=[[float(x.real), float(x.imag)] for x in top],
                                          zeit_s=time.time() - t1)
        print(f"L={a.L} a2={a2} re_max={lam.real.max():.4e} n>1e-5={np.sum(lam.real>1e-5)} "
              f"top={top[:4]} t={time.time()-t1:.1f}s", flush=True)
    out["zeit_s"] = time.time() - t0
    return out


# ---------------------------------------------------------------- Vergleichsball
def radial3(om2, rmax=40.0, dr=0.002):
    """3D-Radialprofil per Schiessen (Bisektion auf f0), Schwanz analytisch C exp(-kappa r)/r."""
    from scipy.integrate import solve_ivp
    kap = math.sqrt(1.0 - om2)

    def rhs(r, y):
        return [y[1], -2.0 * y[1] / r + (U1(y[0] * y[0]) - om2) * y[0]]

    def ev_null(r, y):
        return y[0]
    ev_null.terminal = True

    def ev_umkehr(r, y):
        return y[1]
    ev_umkehr.terminal = True
    ev_umkehr.direction = 1

    def schiess(f0, dense=False):
        r0 = 1e-5
        c = (U1(f0 * f0) - om2) * f0 / 3.0
        sol = solve_ivp(rhs, (r0, rmax), [f0 + 0.5 * c * r0 * r0, c * r0], method="DOP853", rtol=1e-13,
                        atol=1e-15, events=[ev_null, ev_umkehr], dense_output=dense)
        if len(sol.t_events[0]):
            return +1, sol
        if len(sol.t_events[1]):
            return -1, sol
        return 0, sol
    Sp = (2.0 + math.sqrt(4.0 - 6.0 * (1.0 - om2))) / 3.0   # Maximum von V_eff: U'(S) = omega^2
    Smin = (2.0 - math.sqrt(4.0 - 6.0 * (1.0 - om2))) / 3.0   # Minimum von V_eff
    S_unter = 1.0 - math.sqrt(2.0 * om2 - 1.0)   # V_eff(f0) < V_eff(0): sicher zu kurz
    lo, hi = math.sqrt(0.5 * (Smin + S_unter)), math.sqrt(Sp * (1.0 - 1e-4))
    slo, _ = schiess(lo)
    shi, _ = schiess(hi)
    assert slo == -1 and shi == +1, (slo, shi)
    for it in range(200):
        mid = 0.5 * (lo + hi)
        if mid == lo or mid == hi:
            break
        s, _ = schiess(mid)
        if s > 0:
            hi = mid
        else:
            lo = mid
    s, sol = schiess(lo, dense=True)
    rend = sol.t[-1]
    # Anschluss des Schwanzes: dort, wo f erstmals < 1e-5 f0, hoechstens 0,8 rend
    rr = np.arange(1e-5, rend, dr)
    y = sol.sol(rr)
    f = y[0]
    i_a = np.argmax(f < 1e-5 * lo) if np.any(f < 1e-5 * lo) else int(0.8 * len(rr))
    i_a = min(i_a, int(0.8 * len(rr)))
    ra = rr[i_a]
    C = f[i_a] * ra * math.exp(kap * ra)
    r_t = np.arange(rr[i_a], rmax + 30.0, dr)
    f_t = C * np.exp(-kap * r_t) / r_t
    fp_t = -C * np.exp(-kap * r_t) * (kap * r_t + 1.0) / r_t ** 2
    r_all = np.r_[rr[:i_a], r_t]
    f_all = np.r_[f[:i_a], f_t]
    fp_all = np.r_[y[1][:i_a], fp_t]
    om = math.sqrt(om2)
    w = 4 * math.pi * r_all ** 2
    Q = 2 * om * np.trapezoid(f_all ** 2 * w, r_all)
    E = np.trapezoid((om2 * f_all ** 2 + fp_all ** 2 + U(f_all ** 2)) * w, r_all)
    S0 = lo * lo
    i_h = np.argmax(f_all ** 2 < 0.5 * S0)
    return dict(f0=lo, f0_2=S0, Q=float(Q), E=float(E), r_anschluss=float(ra), r_ende_schiessen=float(rend),
                R_halb=float(r_all[i_h]), kappa=kap), r_all, f_all


def modus_ball(a):
    t0 = time.time()
    h = a.h
    om2 = a.om2
    om = math.sqrt(om2)
    rad, r_all, f_all = radial3(om2)
    out = {"modus": "ball", "L": a.L, "h": h, "om2": om2, "radial": rad, "dt": a.dt, "T": a.T, "kick": a.kick,
           "richtung": a.richtung, "Rw": a.Rw}
    print("radial", rad, f"t={time.time()-t0:.1f}s", flush=True)
    g = gitter(a.L)
    out["gitter_pruef"] = g["pruef"]
    N = g["N"]
    x = phys(g, h)
    Lb = boxlaenge(g, h)
    # Mittelpunkt: Knoten nahe der Torusmitte (Inversionszentrum)
    c0 = np.array([g["P"] / 2.0] * 3)
    dd = minbild(g["pos"] - c0, g["P"])
    i0 = int(np.argmin((dd ** 2).sum(1)))
    c = x[i0].copy()
    d = minbild(x - c, Lb)
    r = np.sqrt((d ** 2).sum(1))
    f = np.interp(r, r_all, f_all)
    vs = SQ2 * h ** 3
    A = g["A"]
    Lap = (A - 6.0 * sp.identity(N, format="csr")).tocsr()
    h2 = 1.0 / h ** 2
    kanten = g["kanten"]

    def EQ(f):
        dfk = f[kanten[:, 0]] - f[kanten[:, 1]]
        Q = vs * 2 * om * float(np.sum(f * f))
        E = vs * (om2 * float(np.sum(f * f)) + float(np.sum(U(f * f))) + h2 * float(np.sum(dfk * dfk)))
        return E, Q
    E_abt, Q_abt = EQ(f)
    out["abgetastet"] = dict(E=E_abt, Q=Q_abt, box=Lb, r_halbe_box_f=float(np.interp(Lb / 2, r_all, f_all)))
    newt = []
    for it in range(30):
        S = f * f
        R = -(Lap @ f) * h2 + (U1(S) - om2) * f
        res = float(np.abs(R).max())
        newt.append(res)
        print(f"newton {it} res={res:.3e} t={time.time()-t0:.1f}s", flush=True)
        if res < a.newton_tol:
            break
        J = (-Lap * h2 + sp.diags(U1(S) + 2.0 * U2(S) * S - om2)).tocsr()
        delta, info = spla.minres(J, -R, rtol=1e-13, maxiter=20000)
        f = f + delta
    E_g, Q_g = EQ(f)
    # Symmetrie: Dipolmoment des Profils
    dip = (f[:, None] ** 2 * d).sum(0) / (f ** 2).sum()
    out["newton"] = dict(res=newt, iter=len(newt) - 1, E=E_g, Q=Q_g, f_max=float(f.max()),
                         dipol=dip.tolist(), f_min=float(f.min()))
    out["kontinuum_tabelle"] = dict(E=428.641, Q=473.413, quelle="RUNDE-02/tests1d Test 4, omega^2 = 0,70")
    out["abw"] = dict(E_tab=E_g / 428.641 - 1, Q_tab=Q_g / 473.413 - 1, E_rad=E_g / rad["E"] - 1,
                      Q_rad=Q_g / rad["Q"] - 1)
    print("ball", out["newton"]["E"], out["newton"]["Q"], out["abw"], flush=True)
    # Zeitentwicklung mit Stoss (Phasengradient)
    if a.T > 0:
        e = np.array(a.richtung, float)
        e /= np.linalg.norm(e)
        ph = np.exp(-1j * a.kick * om * (d @ e))
        phi = (f * ph).astype(complex)
        p = (1j * om * f * ph).astype(complex)
        mess = Mess(g, h, None, a.Rw, c)
        X0 = mess.schwerpunkt(2.0 * (phi.real * p.imag - phi.imag * p.real) * vs)[0]
        mess.X = X0.copy()
        rec, status = entwickle(A, phi, p, h, a.dt, a.T, a.dmess, mess, wand=a.wand, t_start=t0)
        out["lauf"] = dict(status=status, spalten=SPALTEN, reihe=rec.tolist(), X0=X0.tolist())
        print(f"ball kick={a.kick} dX_end={np.linalg.norm(rec[-1,5:8]-rec[0,5:8]):.4f} "
              f"dE={np.abs(rec[:,3]-rec[0,3]).max()/rec[0,3]:.2e} dQ={np.abs(rec[:,4]-rec[0,4]).max()/rec[0,4]:.2e} "
              f"Qw_end/Qw0={rec[-1,8]/rec[0,8]:.4f} {status} t={time.time()-t0:.1f}s", flush=True)
    out["zeit_s"] = time.time() - t0
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("modus", choices=["linear", "ring", "bogo", "ball"])
    ap.add_argument("--out", required=True)
    ap.add_argument("--nk", type=int, default=48)
    ap.add_argument("--nzufall", type=int, default=100000)
    ap.add_argument("--Lreal", type=int, default=4)
    ap.add_argument("--L", type=int, default=8)
    ap.add_argument("--h", type=float, default=1.0)
    ap.add_argument("--a2", type=lambda s: [float(x) for x in s.split(",")], default=[0.5, 1.0, 1.5, 2.0, 3.0])
    ap.add_argument("--dt", type=float, default=0.005)
    ap.add_argument("--T", type=float, default=200.0)
    ap.add_argument("--dmess", type=float, default=0.5)
    ap.add_argument("--rauschen", type=float, default=0.0)
    ap.add_argument("--saat", type=int, default=1)
    ap.add_argument("--kick", type=float, default=0.0)
    ap.add_argument("--richtung", type=lambda s: [float(x) for x in s.split(",")], default=[1.0, 0.0, 0.0])
    ap.add_argument("--Rw", type=float, default=2.5)
    ap.add_argument("--wand", type=float, default=540.0)
    ap.add_argument("--om2", type=float, default=0.7)
    ap.add_argument("--newton_tol", type=float, default=1e-10)
    a = ap.parse_args()
    t0 = time.time()
    fn = {"linear": modus_linear, "ring": modus_ring, "bogo": modus_bogo, "ball": modus_ball}[a.modus]
    out = fn(a)
    out["argv"] = sys.argv
    out["start_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t0))
    out["ende_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    tmp = a.out + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(out, fh)
    import os
    os.replace(tmp, a.out)
    print("geschrieben", a.out, f"{time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
