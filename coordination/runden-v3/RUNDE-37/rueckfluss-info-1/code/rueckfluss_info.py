#!/usr/bin/env python3
# RUECKFLUSS-INFO-1, Runde 45 (fmhc-physics). Code-Agent fuer die Leitung claude-primary.
# Ergaenzung zu SPIEGEL-HAELFTE-1. Der Kern bleibt unveraendert: spiegel_haelfte.py (Kopie, sha256 gleich dem Original)
#   wird importiert. Gitter, Paket, Verschiebung, Muenze (P_2, alpha = 0, beta = pi) und die Takt-Erzeugung bei festen
#   Takten stammen von dort. 'schritt' wiederholt die Rechenoperationen von sh.lauf_unordnung in derselben Reihenfolge
#   (Rauchtest: w_2 bitgleich).
# Neu sind nur Messungen:
#   (1) Spurabstand D(t) zweier sichtbarer Startzustaende (Spin +z / -z im 2-Block, gleiches Paket), feste Takte
#       (exakt, 2x2-Gram) und in jedem Schritt neu gezogene Takte (M Ziehungen, Gram der 2M Vektoren);
#   (2) sigma-Leiter: w_2(t) und N_FJ(t) bei W = 2 pi, feste Takte (Rueckgabequote r in der Auswertung).
# Start nur auf der .69 ueber kleintest.sh (1 Thread).
# Aufruf: rueckfluss_info.py --modus fest|neu|leiter|kontrolle --out DATEI.json [--N N] [--sigma S] [--W w1,w2]
#         [--saaten n] [--saatbasis s] [--M M] [--schritte T] [--kraum]
import argparse
import json
import sys
import time

import numpy as np

import spiegel_haelfte as sh


# ---------------------------------------------------------------- Spurabstand
def spurabstand(G, iA, iB):
    """1/2 || mittel_A |y><y| - mittel_B |y><y| ||_1 aus der Gram-Matrix G_ij = <y_i|y_j>.
    Rueckgabe: Du (ohne Flagge), Spuren nA, nB und Dg = Du + |nA - nB|/2 (Verlustflagge)."""
    iA, iB = list(iA), list(iB)
    idx = iA + iB
    Gs = G[np.ix_(idx, idx)]
    Gs = 0.5 * (Gs + Gs.conj().T)
    lam, U = np.linalg.eigh(Gs)
    lam = np.clip(lam, 0.0, None)
    R = (U * np.sqrt(lam)) @ U.conj().T
    s = np.concatenate([np.full(len(iA), 1.0 / len(iA)), np.full(len(iB), -1.0 / len(iB))])
    X = R @ (s[:, None] * R)
    mu = np.linalg.eigvalsh(0.5 * (X + X.conj().T))
    nA = float(np.real(np.trace(Gs[:len(iA), :len(iA)]))) / len(iA)
    nB = float(np.real(np.trace(Gs[len(iA):, len(iA):]))) / len(iB)
    Du = 0.5 * float(np.abs(mu).sum())
    return {"Du": Du, "nA": nA, "nB": nB, "Dg": Du + 0.5 * abs(nA - nB)}


def d_rein(nA, nB, ab):
    """Zwei reine, unternormierte Zustaende: ||a a^+ - b b^+||_1 = sqrt((nA+nB)^2 - 4|<a|b>|^2).
    Rueckgabe (Du, Dg, Dn); Dn = Abstand der normierten Zustaende (beschreibend)."""
    x = (nA + nB) ** 2 - 4 * abs(ab) ** 2
    Du = 0.5 * float(np.sqrt(max(x, 0.0)))
    Dn = float(np.sqrt(max(1.0 - abs(ab) ** 2 / (nA * nB), 0.0))) if nA > 0 and nB > 0 else float("nan")
    return Du, Du + 0.5 * abs(nA - nB), Dn


def spin(v):
    # v: (2,N,N,N) sichtbarer Anteil im C^2-Rahmen von V; Erwartungswerte <sigma_x,y,z> mit Gewicht (unnormiert)
    c = np.vdot(v[0], v[1])
    return [float(2 * c.real), float(2 * c.imag), float(np.vdot(v[0], v[0]).real - np.vdot(v[1], v[1]).real)]


# ---------------------------------------------------------------- Schritt (wie sh.lauf_unordnung)
def schritt(psi, t, P2s, Er_r, ea):
    psi = sh.verschiebung(psi, t)
    P2psi = np.tensordot(P2s, psi, axes=(1, 0))
    w2 = float(np.vdot(P2psi, P2psi).real)
    psi -= P2psi
    psi *= Er_r[None]
    P2psi *= ea
    psi += P2psi
    return psi, P2psi, w2


def takte_fest(N, W, saat):
    # wie sh.lauf_unordnung: beta_x je Knoten (vier Nebenklassen-Felder) fest
    rng = np.random.default_rng(saat)
    beta = sh.BETA + W * (rng.random((4, N, N, N)) - 0.5)
    return np.exp(1j * beta)


class TakteNeu:
    # in jedem Schritt neu gezogen: ein frisches Feld fuer die Nebenklasse dieses Schritts, gleiche Verteilung
    def __init__(self, N, W, saat):
        self.rng = np.random.default_rng(saat)
        self.N, self.W = N, W

    def ziehe(self):
        beta = sh.BETA + self.W * (self.rng.random((self.N, self.N, self.N)) - 0.5)
        return np.exp(1j * beta)


def randmasken(g):
    return g.r2 > (0.75 * g.R_in) ** 2, g.r2 > (0.9 * g.R_in) ** 2


def randgew(psi, masken):
    p = (np.abs(psi) ** 2).sum(0)
    w = float(p.sum())
    return [float(p[m].sum()) / w for m in masken]


# ---------------------------------------------------------------- FJ-Referenz (wie sh.fj_referenz, beliebig viele Zustaende)
def fj_lauf(P2s, V, psis, T):
    ea = np.exp(1j * sh.ALPHA)
    phis = [p.copy() for p in psis]
    n = [[1.0] for _ in psis]
    ab = [[0.0, 0.0]]
    sp = [[spin(np.tensordot(V, p, axes=(1, 0)))] for p in psis]
    for t in range(T):
        for i in range(len(phis)):
            phi = sh.verschiebung(phis[i], t)
            phis[i] = ea * np.tensordot(P2s, phi, axes=(1, 0))
            n[i].append(float(np.vdot(phis[i], phis[i]).real))
            sp[i].append(spin(np.tensordot(V, phis[i], axes=(1, 0))))
        if len(phis) == 2:
            c = complex(np.vdot(phis[0], phis[1]))
            ab.append([c.real, c.imag])
    out = {"n": n, "spin": sp}
    if len(psis) == 2:
        D = [d_rein(n[0][t], n[1][t], complex(*ab[t])) for t in range(T + 1)]
        out.update({"ab": ab, "Du": [x[0] for x in D], "Dg": [x[1] for x in D], "Dn": [x[2] for x in D]})
    return out


# ---------------------------------------------------------------- feste Takte: A und B im Gleichschritt, exakt
def lauf_fest(g, P2s, V, psiA, psiB, T, W, saat, masken):
    Er = takte_fest(g.N, W, saat)
    ea = np.exp(1j * sh.ALPHA)
    A, B = psiA.copy(), psiB.copy()
    c0 = complex(np.vdot(psiA, psiB))
    nA, nB, ab = [1.0], [1.0], [[c0.real, c0.imag]]
    sA = [spin(np.tensordot(V, psiA, axes=(1, 0)))]
    sB = [spin(np.tensordot(V, psiB, axes=(1, 0)))]
    rand, normabw = [0.0, 0.0], 0.0
    t0 = time.time()
    for t in range(T):
        r = (t + 1) % 4
        A, PA, wA = schritt(A, t, P2s, Er[r], ea)
        B, PB, wB = schritt(B, t, P2s, Er[r], ea)
        c = complex(np.vdot(PA, PB))
        nA.append(wA)
        nB.append(wB)
        ab.append([c.real, c.imag])
        sA.append(spin(np.tensordot(V, PA, axes=(1, 0))))
        sB.append(spin(np.tensordot(V, PB, axes=(1, 0))))
        del PA, PB
        if (t + 1) % 10 == 0 or t + 1 == T:
            for X in (A, B):
                normabw = max(normabw, abs(float(np.vdot(X, X).real) - 1.0))
                rg = randgew(X, masken)
                rand = [max(rand[i], rg[i]) for i in range(2)]
    D = [d_rein(nA[t], nB[t], complex(*ab[t])) for t in range(T + 1)]
    return {"W": W, "saat": saat, "laufzeit_s": time.time() - t0, "nA": nA, "nB": nB, "ab": ab,
            "Du": [x[0] for x in D], "Dg": [x[1] for x in D], "Dn": [x[2] for x in D], "spinA": sA, "spinB": sB,
            "rand_gesamt_0.75_0.9": rand, "norm_abw_max": normabw}


# ---------------------------------------------------------------- neu gezogene Takte: M Ziehungen, Gram der 2M Vektoren
def lauf_neu(g, P2s, V, psiA, psiB, T, W, saatbasis, M, masken):
    ea = np.exp(1j * sh.ALPHA)
    n3 = g.N ** 3
    takte = [TakteNeu(g.N, W, [saatbasis, m]) for m in range(M)]
    zs = [psiA.copy() for _ in range(M)] + [psiB.copy() for _ in range(M)]
    Y = np.empty((2 * M, 2 * n3), dtype=complex)
    for j in range(2 * M):
        Y[j] = np.tensordot(V, zs[j], axes=(1, 0)).ravel()
    h = M // 2
    iA, iB = range(M), range(M, 2 * M)
    sets = {"M": (iA, iB), "haelfte1": (range(h), range(M, M + h)), "haelfte2": (range(h, M), range(M + h, 2 * M)),
            "null_A": (range(h), range(h, M)), "null_B": (range(M, M + h), range(M + h, 2 * M)),
            "getrennt": (range(h), range(M + h, 2 * M))}
    rec = {k: {"Du": [], "Dg": [], "nA": [], "nB": []} for k in sets}
    je_ziehung = {"Dg_mittel": [], "Dg_min": [], "Dg_max": []}
    w2 = [[1.0] for _ in range(2 * M)]
    spinm = {"A": [], "B": []}
    rand, normabw, gram_diag_abw = [0.0, 0.0], 0.0, 0.0
    t0 = time.time()

    def messen():
        G = np.conj(Y) @ Y.T
        for k, (a, b) in sets.items():
            d = spurabstand(G, a, b)
            for kk in rec[k]:
                rec[k][kk].append(d[kk])
        dz = [d_rein(G[m, m].real, G[M + m, M + m].real, G[m, M + m])[1] for m in range(M)]
        je_ziehung["Dg_mittel"].append(float(np.mean(dz)))
        je_ziehung["Dg_min"].append(float(np.min(dz)))
        je_ziehung["Dg_max"].append(float(np.max(dz)))
        return G

    messen()
    for nm, rg in (("A", range(M)), ("B", range(M, 2 * M))):
        spinm[nm].append(list(np.mean([spin(Y[j].reshape(2, g.N, g.N, g.N)) for j in rg], 0)))
    for t in range(T):
        r = (t + 1) % 4
        for m in range(M):
            Er_r = takte[m].ziehe()
            for j in (m, M + m):
                zs[j], P, w = schritt(zs[j], t, P2s, Er_r, ea)
                Y[j] = np.tensordot(V, P, axes=(1, 0)).ravel()
                w2[j].append(w)
                del P
            del Er_r
        G = messen()
        gram_diag_abw = max(gram_diag_abw, max(abs(G[j, j].real - w2[j][-1]) for j in range(2 * M)))
        for nm, rg in (("A", range(M)), ("B", range(M, 2 * M))):
            spinm[nm].append(list(np.mean([spin(Y[j].reshape(2, g.N, g.N, g.N)) for j in rg], 0)))
        if (t + 1) % 10 == 0 or t + 1 == T:
            for X in zs:
                normabw = max(normabw, abs(float(np.vdot(X, X).real) - 1.0))
                rgw = randgew(X, masken)
                rand = [max(rand[i], rgw[i]) for i in range(2)]
        print("  neu W=%.4f t=%d %.1fs" % (W, t + 1, time.time() - t0), flush=True) if (t + 1) % 25 == 0 else None
    return {"W": W, "M": M, "saatbasis": saatbasis, "laufzeit_s": time.time() - t0, "D": rec, "je_ziehung": je_ziehung,
            "w2": w2, "spin_mittel": spinm, "rand_gesamt_0.75_0.9": rand, "norm_abw_max": normabw,
            "gram_diag_gegen_w2_abw": gram_diag_abw}


# ---------------------------------------------------------------- sigma-Leiter: nur w_2 (A) und N_FJ
def lauf_leiter(g, P2s, psi0, T, W, saat, masken):
    Er = takte_fest(g.N, W, saat)
    ea = np.exp(1j * sh.ALPHA)
    psi = psi0.copy()
    w2, rand, normabw = [1.0], [0.0, 0.0], 0.0
    t0 = time.time()
    for t in range(T):
        psi, P, w = schritt(psi, t, P2s, Er[(t + 1) % 4], ea)
        del P
        w2.append(w)
        if (t + 1) % 10 == 0 or t + 1 == T:
            normabw = max(normabw, abs(float(np.vdot(psi, psi).real) - 1.0))
            rg = randgew(psi, masken)
            rand = [max(rand[i], rg[i]) for i in range(2)]
    return {"W": W, "saat": saat, "laufzeit_s": time.time() - t0, "w2": w2, "rand_gesamt_0.75_0.9": rand,
            "norm_abw_max": normabw}


# ---------------------------------------------------------------- k-Raum-Kontrolle bei W = 0 (wie sh.bloch_kontrolle)
def kraum_W0(g, P2s, psiA, psiB, T):
    C = np.exp(1j * sh.ALPHA) * P2s + np.exp(1j * sh.BETA) * (np.eye(4) - P2s)
    ph = {(c, a): g.phase(sh.E4[a] - sh.E4[c]) for c in range(4) for a in range(4)}
    hA = np.stack([np.fft.fftn(psiA[a]) for a in range(4)])
    hB = np.stack([np.fft.fftn(psiB[a]) for a in range(4)])
    nf = float(g.N ** 3)
    Dg = [1.0]
    for t in range(T):
        c = t % 4
        for a in range(4):
            hA[a] *= ph[(c, a)]
            hB[a] *= ph[(c, a)]
        hA = np.tensordot(C, hA, axes=(1, 0))
        hB = np.tensordot(C, hB, axes=(1, 0))
        xA = np.tensordot(P2s, hA, axes=(1, 0))
        xB = np.tensordot(P2s, hB, axes=(1, 0))
        Dg.append(d_rein(float(np.vdot(xA, xA).real) / nf, float(np.vdot(xB, xB).real) / nf,
                         complex(np.vdot(xA, xB)) / nf)[1])
    return Dg


def ru_maxrss_mb():
    return sh.ru_maxrss_mb()


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modus", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--N", type=int, default=96)
    ap.add_argument("--sigma", type=float, default=4.0)
    ap.add_argument("--W", default="")
    ap.add_argument("--saaten", type=int, default=1)
    ap.add_argument("--saatbasis", type=int, default=45000)
    ap.add_argument("--M", type=int, default=8)
    ap.add_argument("--schritte", type=int, default=100)
    ap.add_argument("--kraum", action="store_true")
    ap.add_argument("--repr", default="qcad4_repr_2p2s.json")
    args = ap.parse_args()
    t_start = time.time()
    res = {"modus": args.modus, "N": args.N, "sigma": args.sigma, "schritte": args.schritte, "alpha": sh.ALPHA,
           "beta": sh.BETA, "numpy": np.__version__, "argv": sys.argv[1:]}
    rng = np.random.default_rng(4242)
    ta, _, (P2s, V, Vs), sgn = sh.teil_a_repr(args.repr, "2+2'", rng)
    res["teil_A_kurz"] = {k: ta[k] for k in ("richtung", "haendigkeit_2_relativ_zu_h", "sauber_P2_projektor_abw",
                                             "sauber_VVdag_abw")}
    g = sh.Gitter(args.N, sgn * sh.TV)
    masken = randmasken(g)
    res["R_in_hop"] = g.R_in
    uA = V.conj().T @ np.array([1.0, 0.0], dtype=complex)   # Spin +z im 2-Block (wie SPIEGEL-HAELFTE-1)
    uB = V.conj().T @ np.array([0.0, 1.0], dtype=complex)   # Spin -z
    psiA = sh.paket(g, args.sigma, uA)
    psiB = sh.paket(g, args.sigma, uB)
    res["start_ueberlapp_AB"] = abs(complex(np.vdot(psiA, psiB)))
    res["start_P2_abw"] = max(sh.maxabs(np.tensordot(P2s, p, axes=(1, 0)) - p) for p in (psiA, psiB))
    Ws = [float(eval(x, {"pi": np.pi})) for x in args.W.split(",") if x]
    T = args.schritte

    if args.modus == "kontrolle":
        # (1) 'schritt' gegen sh.lauf_unordnung (w_2 bitgleich), (2) FJ gegen sh.fj_referenz (bitgleich),
        # (3) spurabstand gegen d_rein, (4) k-Raum bei W = 0, (5) FJ-Monotonie
        kc = 2.0 / args.sigma
        fjo, snaps = sh.fj_referenz(g, P2s, psiA, T, kc, schnapp=False)
        fjn = fj_lauf(P2s, V, [psiA, psiB], T)
        res["fj_bitgleich_abw"] = float(np.max(np.abs(np.array(fjo["N_FJ"]) - np.array(fjn["n"][0]))))
        res["fj_Dg"] = fjn["Dg"]
        res["fj_anstieg_summe"] = float(np.clip(np.diff(fjn["Dg"]), 0, None).sum())
        W = 2 * np.pi
        r0, _ = sh.lauf_unordnung(g, P2s, psiA, T, W, 4500, kc, {}, False)
        rf = lauf_fest(g, P2s, V, psiA, psiB, T, W, 4500, masken)
        res["schritt_bitgleich_w2_abw"] = float(np.max(np.abs(np.array(r0["w2"]) - np.array(rf["nA"]))))
        G = np.array([[rf["nA"][T], complex(*rf["ab"][T])], [np.conj(complex(*rf["ab"][T])), rf["nB"][T]]])
        d = spurabstand(G, [0], [1])
        res["gram_gegen_geschlossen_abw"] = abs(d["Dg"] - rf["Dg"][T]) + abs(d["Du"] - rf["Du"][T])
        rng2 = np.random.default_rng(7)
        Yt = rng2.normal(size=(6, 50)) + 1j * rng2.normal(size=(6, 50))
        Gt = np.conj(Yt) @ Yt.T
        Xop = sum(np.outer(Yt[i], Yt[i].conj()) for i in range(3)) / 3 - sum(np.outer(Yt[i], Yt[i].conj()) for i in range(3, 6)) / 3
        res["gram_gegen_voll_abw"] = abs(spurabstand(Gt, range(3), range(3, 6))["Du"]
                                         - 0.5 * float(np.abs(np.linalg.eigvalsh(Xop)).sum()))
        rw0 = lauf_fest(g, P2s, V, psiA, psiB, T, 0.0, 4501, masken)
        res["kraum_W0_Dg_abw"] = float(np.max(np.abs(np.array(kraum_W0(g, P2s, psiA, psiB, T)) - np.array(rw0["Dg"]))))
        rn = lauf_neu(g, P2s, V, psiA, psiB, min(T, 12), W, 4502, 4, masken)
        res["neu_kurz_gram_diag_abw"] = rn["gram_diag_gegen_w2_abw"]
        res["neu_kurz_schluessel"] = sorted(rn["D"].keys())
        res["laufzeit_fest_je_saat_s"] = rf["laufzeit_s"]
        res["laufzeit_neu_M4_T12_s"] = rn["laufzeit_s"]
    elif args.modus == "fest":
        res["fj"] = fj_lauf(P2s, V, [psiA, psiB], T)
        res["laeufe"] = []
        for iw, W in enumerate(Ws):
            nsaat = 1 if W == 0.0 else args.saaten
            for s in range(nsaat):
                saat = args.saatbasis + 100 * iw + s
                r = lauf_fest(g, P2s, V, psiA, psiB, T, W, saat, masken)
                if W == 0.0 and args.kraum:
                    r["kraum_W0_Dg_abw"] = float(np.max(np.abs(np.array(kraum_W0(g, P2s, psiA, psiB, T))
                                                              - np.array(r["Dg"]))))
                res["laeufe"].append(r)
                print("fest W=%.4f saat=%d %.1fs maxrss=%.0fMB" % (W, saat, r["laufzeit_s"], ru_maxrss_mb()), flush=True)
    elif args.modus == "neu":
        res["laeufe"] = []
        for iw, W in enumerate(Ws):
            r = lauf_neu(g, P2s, V, psiA, psiB, T, W, args.saatbasis + 100 * iw, args.M, masken)
            res["laeufe"].append(r)
            print("neu W=%.4f M=%d %.1fs maxrss=%.0fMB" % (W, args.M, r["laufzeit_s"], ru_maxrss_mb()), flush=True)
    elif args.modus == "leiter":
        res["fj"] = fj_lauf(P2s, V, [psiA], T)
        res["N_FJ"] = res["fj"]["n"][0]
        res["laeufe"] = []
        for iw, W in enumerate(Ws):
            for s in range(args.saaten):
                saat = args.saatbasis + 100 * iw + s
                r = lauf_leiter(g, P2s, psiA, T, W, saat, masken)
                res["laeufe"].append(r)
                print("leiter W=%.4f saat=%d %.1fs maxrss=%.0fMB" % (W, saat, r["laufzeit_s"], ru_maxrss_mb()),
                      flush=True)
    else:
        raise SystemExit("unbekannter modus")
    res["laufzeit_s"] = time.time() - t_start
    res["maxrss_MB"] = ru_maxrss_mb()
    with open(args.out, "w") as f:
        json.dump(res, f)
    print("fertig", args.out, "%.1fs" % res["laufzeit_s"], "maxrss %.0f MB" % res["maxrss_MB"], flush=True)


if __name__ == "__main__":
    main()
