# NETZ-C-1 (Runde 35), Teil A: akustische Geschwindigkeiten und Nullmoden von Stabnetzen.
# Netze: fcc (Grad 12), Pyrochlor (Grad 6), Diamant (Grad 4), srs (Grad 3, K4-Kristall wie FLUSS-1).
# Modelle: Z = nur Zentralfedern (k = 1), W1 = Z + Winkelfedern ueber d(cos theta) = d(r_ij^ . r_il^),
#          W2 = Z + Keating-Form d(r_ij . r_il) (unnormiertes Skalarprodukt). k_theta = 0,1, Masse 1, Kante 1.
# Aufruf (nur ueber kleintest.sh auf der .69):  netz_a.py <ausgabe.json> [netze,kommagetrennt] [modelle] [nfib1,nfib2]
import sys, os, json, time, hashlib
import numpy as np
from scipy.optimize import minimize

KTHETA = 0.1
KS = (1e-3, 2e-3)          # |k| in 1/Kantenlaenge; Hauptwert KS[0], Probe KS[1]
CNULL = 1e-6               # Geschwindigkeit < CNULL gilt als null (Eigenwert < 1e-12 |k|^2)
NGITTER = (12, 16)         # k-Gitter n^3 in reduzierten Koordinaten der primitiven Zelle
NZUFALL = 64               # zufaellige (generische) k-Punkte
SEED = 20261003
TOL_NB = 1e-9
S0_GAMMA = 1e-9            # absolute Schwelle fuer Nullmoden genau bei k = 0
SYM = {"[100]": [1.0, 0.0, 0.0], "[110]": [1.0, 1.0, 0.0], "[111]": [1.0, 1.0, 1.0]}
LINIEN = [[1, 1, 0], [1, -1, 0], [1, 0, 1], [1, 0, -1], [0, 1, 1], [0, 1, -1]]   # <110>-Richtungen


def netz(name):
    s2 = np.sqrt(2.0)
    fccA = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]], float)
    if name == "fcc":
        a = s2; A = a / 2 * fccA; basis = np.zeros((1, 3))
    elif name == "pyro":
        a = 2 * s2; A = a / 2 * fccA
        basis = a / 8 * np.array([[0, 0, 0], [0, 2, 2], [2, 0, 2], [2, 2, 0]], float)
    elif name == "diamant":
        a = 4 / np.sqrt(3.0); A = a / 2 * fccA
        basis = a / 4 * np.array([[0, 0, 0], [1, 1, 1]], float)
    elif name == "srs":
        a = 2 * s2; A = a / 2 * np.array([[-1, 1, 1], [1, -1, 1], [1, 1, -1]], float)
        basis = a / 8 * np.array([[1, 1, 1], [5, 3, 7], [3, 7, 5], [7, 5, 3]], float)
    else:
        raise ValueError(name)
    n = len(basis)
    halb = []
    dmin = np.inf
    rng = range(-3, 4)
    for al in range(n):
        for be in range(n):
            for n1 in rng:
                for n2 in rng:
                    for n3 in rng:
                        nv = np.array([n1, n2, n3])
                        d = basis[be] + nv @ A - basis[al]
                        L = np.linalg.norm(d)
                        if L < 1e-12:
                            continue
                        dmin = min(dmin, L)
                        if abs(L - 1.0) < TOL_NB:
                            halb.append((al, be, nv, d / L))
    bonds = []
    for (al, be, nv, d) in halb:
        nz = nv[np.nonzero(nv)[0]]
        if al < be or (al == be and len(nz) > 0 and nz[0] > 0):
            bonds.append((al, be, nv, d))
    paare = []
    winkel = {}
    for al in range(n):
        he = [x for x in halb if x[0] == al]
        for i in range(len(he)):
            for j in range(i + 1, len(he)):
                paare.append((al, he[i], he[j]))
                c = float(np.dot(he[i][3], he[j][3]))
                w = int(round(np.degrees(np.arccos(np.clip(c, -1, 1)))))
                winkel[w] = winkel.get(w, 0) + 1
    grad = [sum(1 for x in halb if x[0] == al) for al in range(n)]
    B = 2 * np.pi * np.linalg.inv(A).T          # reziproke Basis: B[i] . A[j] = 2 pi delta_ij
    return dict(name=name, a=a, A=A, B=B, basis=basis, n=n, halb=halb, bonds=bonds, paare=paare,
                info=dict(knoten_je_zelle=n, bindungen_je_zelle=len(bonds), grad=grad, dmin=float(dmin),
                          winkelpaare_je_zelle=len(paare), winkel_grad_haeufigkeit={str(k): v for k, v in sorted(winkel.items())},
                          maxwell_3n_minus_b=3 * n - len(bonds), kubische_kante=float(a),
                          zellvolumen=float(abs(np.linalg.det(A)))))


def terme(net, modell):
    """Zeilen als Summen von Termen (zeile, knoten, koeff[3], R[3]); Eintrag = koeff * exp(i k.R)."""
    A = net["A"]
    T = []
    r = 0
    for (al, be, nv, d) in net["bonds"]:
        T.append((r, al, -d, np.zeros(3)))
        T.append((r, be, d, nv @ A))
        r += 1
    nb = r
    if modell in ("W1", "W2"):
        w = np.sqrt(KTHETA)
        for (al, h1, h2) in net["paare"]:
            d1, d2 = h1[3], h2[3]
            c = float(np.dot(d1, d2))
            if modell == "W1":
                g1 = d2 - c * d1; g2 = d1 - c * d2
            else:
                g1 = d2.copy(); g2 = d1.copy()
            T.append((r, h1[1], w * g1, h1[2] @ A))
            T.append((r, h2[1], w * g2, h2[2] @ A))
            T.append((r, al, -w * (g1 + g2), np.zeros(3)))
            r += 1
    zeile = np.array([t[0] for t in T]); knoten = np.array([t[1] for t in T])
    koeff = np.array([t[2] for t in T]); R = np.array([t[3] for t in T])
    return dict(nrow=r, nbond=nb, ncol=3 * net["n"], zeile=zeile, knoten=knoten, koeff=koeff, R=R)


def mat(tm, k):
    M = np.zeros((tm["nrow"], tm["ncol"]), complex)
    ph = np.exp(1j * (tm["R"] @ k))
    vals = tm["koeff"] * ph[:, None]
    for c in range(3):
        np.add.at(M, (tm["zeile"], 3 * tm["knoten"] + c), vals[:, c])
    return M


def sing(tm, k, uv=False):
    M = mat(tm, k)
    nc = tm["ncol"]
    if not uv:
        s = np.linalg.svd(M, compute_uv=False)
        return np.sort(np.concatenate([s, np.zeros(max(0, nc - len(s)))]))
    U, s, Vh = np.linalg.svd(M, full_matrices=True)
    s_full = np.concatenate([s, np.zeros(max(0, nc - len(s)))])
    idx = np.argsort(s_full, kind="stable")
    return s_full[idx], Vh[idx].conj()


def moden(tm, n, khat, kk):
    s, V = sing(tm, kk * khat, uv=True)
    c = s / kk
    tau = []; lamL = []; pol = []
    for i in range(min(6, len(s))):
        v = V[i].reshape(n, 3)
        m = v.mean(0)
        tau.append(float(n * np.vdot(m, m).real))
        mm = np.vdot(m, m).real
        if mm > 1e-30:
            lamL.append(float(abs(np.dot(m, khat)) ** 2 / mm))
            phi = 0.5 * np.angle(np.sum(m * m))
            mr = np.real(m * np.exp(-1j * phi)); mr = mr / (np.linalg.norm(mr) + 1e-300)
            j = np.argmax(np.abs(mr)); mr = mr * np.sign(mr[j])
            pol.append([float(x) for x in mr])
        else:
            lamL.append(None); pol.append(None)
    return c, tau, lamL, pol


def fibonacci(N):
    i = np.arange(N)
    z = 1 - (2 * i + 1) / N
    r = np.sqrt(1 - z * z)
    phi = i * np.pi * (3 - np.sqrt(5.0))
    return np.stack([r * np.cos(phi), r * np.sin(phi), z], 1)


def richtungen(N):
    sym = np.array([np.array(v) / np.linalg.norm(v) for v in SYM.values()])
    return np.vstack([sym, fibonacci(N)])


def speeds(tm, dirs, kk):
    out = np.zeros((len(dirs), 6))
    for i, d in enumerate(dirs):
        s = sing(tm, kk * d)
        out[i, :min(6, len(s))] = s[:6] / kk
    return out


def sph(x):
    th, ph = x
    return np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])


def zu_sph(d):
    return [float(np.arccos(np.clip(d[2], -1, 1))), float(np.arctan2(d[1], d[0]))]


def verfeinern(f, starts):
    best = None
    for d in starts:
        r = minimize(lambda x: f(sph(x)), zu_sph(d), method="Nelder-Mead",
                     options=dict(xatol=1e-7, fatol=1e-12, maxiter=600))
        if best is None or r.fun < best[0]:
            best = (float(r.fun), [float(x) for x in sph(r.x)])
    return best


def kmin_norm(net, red):
    B = net["B"]
    k = red @ B
    best = np.inf
    for m1 in (-1, 0, 1):
        for m2 in (-1, 0, 1):
            for m3 in (-1, 0, 1):
                G = np.array([m1, m2, m3]) @ B
                best = min(best, np.linalg.norm(k - G))
    return k, best


def linienvektoren(net):
    """Kuerzester Gittervektor T_e laengs jeder <110>-Richtung e (fuer die Ebenenpruefung)."""
    A = net["A"]
    out = []
    for e in LINIEN:
        e = np.array(e, float) / np.sqrt(2.0)
        best = None
        for n1 in range(-3, 4):
            for n2 in range(-3, 4):
                for n3 in range(-3, 4):
                    R = np.array([n1, n2, n3]) @ A
                    L = np.linalg.norm(R)
                    if L > 1e-9 and np.linalg.norm(np.cross(R, e)) < 1e-9 * L and (best is None or L < best[0]):
                        best = (L, R)
        out.append(best[1])
    return out


def ebenen(TL, k):
    """Zahl der <110>-Linienrichtungen e mit k.T_e in 2 pi Z."""
    z = 0
    for T in TL:
        ph = (k @ T) / (2 * np.pi)
        if abs(ph - np.round(ph)) < 1e-9:
            z += 1
    return z


def gitterzaehlung(net, tm, N):
    nc = tm["ncol"]; nr = tm["nrow"]
    TL = linienvektoren(net)
    hist = {}
    pkt_mit_null = 0; summe_null = 0
    max_null_rel = 0.0; min_nicht_rel = np.inf
    auf_ebene = 0; ebenen_gleich_null = 0
    gamma_null = None
    for m1 in range(N):
        for m2 in range(N):
            for m3 in range(N):
                red = np.array([m1, m2, m3], float) / N
                k, kn = kmin_norm(net, red)
                s = sing(tm, k)
                if kn < 1e-12:
                    gamma_null = int(np.sum(s < S0_GAMMA))
                    continue
                thr = CNULL * kn
                z = int(np.sum(s < thr))
                hist[z] = hist.get(z, 0) + 1
                if np.any(s < thr):
                    max_null_rel = max(max_null_rel, float(s[s < thr].max() / kn))
                if np.any(s >= thr):
                    min_nicht_rel = min(min_nicht_rel, float(s[s >= thr].min() / kn))
                if z > 0:
                    pkt_mit_null += 1; summe_null += z
                    if net["name"] in ("pyro", "fcc"):
                        ne = ebenen(TL, k)
                        if ne > 0:
                            auf_ebene += 1
                        if ne == z:
                            ebenen_gleich_null += 1
    return dict(N=N, punkte=N ** 3, nullmoden_bei_k0=gamma_null, histogramm_nullmoden_k_ungleich_0={str(k): v for k, v in sorted(hist.items())},
                punkte_mit_nullmode=pkt_mit_null, summe_nullmoden=summe_null,
                groesster_null_s_durch_k=max_null_rel, kleinster_nicht_null_s_durch_k=float(min_nicht_rel),
                nullpunkte_auf_110_ebene=auf_ebene if net["name"] in ("pyro", "fcc") else None,
                nullpunkte_zahl_gleich_ebenenzahl=ebenen_gleich_null if net["name"] in ("pyro", "fcc") else None)


def zufall(net, tm):
    rng = np.random.default_rng(SEED)
    nc = tm["ncol"]; nr = tm["nrow"]
    n0 = []; ns = []
    for _ in range(NZUFALL):
        red = rng.random(3)
        k, kn = kmin_norm(net, red)
        s = sing(tm, k)
        thr = CNULL * kn
        rang = int(np.sum(s >= thr))
        n0.append(nc - rang); ns.append(nr - rang)
    return dict(punkte=NZUFALL, nullmoden_min_max=[int(min(n0)), int(max(n0))],
                eigenspannungen_min_max=[int(min(ns)), int(max(ns))],
                index_n0_minus_ns=sorted(set(int(a - b) for a, b in zip(n0, ns))))


def auswerten_modell(net, modell, nfibs):
    t0 = time.time()
    tm = terme(net, modell)
    n = net["n"]
    erg = dict(zeilen=tm["nrow"], spalten=tm["ncol"], bindungszeilen=tm["nbond"],
               winkelzeilen=tm["nrow"] - tm["nbond"])
    # Symmetrierichtungen mit Polarisation
    sym = {}
    for name, v in SYM.items():
        kh = np.array(v) / np.linalg.norm(v)
        sym[name] = {}
        for kk in KS:
            c, tau, lamL, pol = moden(tm, n, kh, kk)
            sym[name][repr(kk)] = dict(c=[float(x) for x in c[:6]], tau=tau, lamL=lamL, pol=pol)
    erg["symmetrie"] = sym
    # Richtungssaetze
    roh = {}
    saetze = {}
    for nf in nfibs:
        dirs = richtungen(nf)
        for kk in KS:
            C = speeds(tm, dirs, kk)
            roh["c_nf%d_k%s" % (nf, repr(kk))] = C
            ak = C[:, :3]
            null_dir = np.any(ak < CNULL, axis=1)
            steif = bool(not np.any(null_dir))
            ratio = ak[:, 2] / np.maximum(ak[:, 0], 1e-300)
            imin = int(np.argmin(ratio))
            var = []
            for b in range(3):
                cb = ak[:, b]
                var.append(dict(min=float(cb.min()), max=float(cb.max()),
                                max_durch_min_minus_1=float(cb.max() / max(cb.min(), 1e-300) - 1),
                                spanne_durch_mittel=(float((cb.max() - cb.min()) / cb.mean()) if cb.mean() > 0 else None),
                                richtung_min=[float(x) for x in dirs[int(np.argmin(cb))]],
                                richtung_max=[float(x) for x in dirs[int(np.argmax(cb))]]))
            luecke = (C[:, 3] / np.maximum(C[:, 2], 1e-300)) if tm["ncol"] > 3 else None
            saetze["nf%d_k%s" % (nf, repr(kk))] = dict(
                richtungen=len(dirs), steif=steif, richtungen_mit_nullast=int(null_dir.sum()),
                nullast_in_symmetrierichtung={nm: bool(null_dir[i]) for i, nm in enumerate(SYM)},
                zahl_nullaeste_je_symmetrierichtung={nm: int(np.sum(ak[i] < CNULL)) for i, nm in enumerate(SYM)},
                min_ratio_groesste_durch_kleinste=float(ratio[imin]), richtung_min_ratio=[float(x) for x in dirs[imin]],
                aeste=var, min_luecke_c4_durch_c3=(float(luecke.min()) if luecke is not None else None))
    erg["saetze"] = saetze
    # Linearitaet: c(2e-3)/c(1e-3) je Ast, nur Aeste mit c >= CNULL
    a1 = roh["c_nf%d_k%s" % (nfibs[0], repr(KS[0]))][:, :3]
    a2 = roh["c_nf%d_k%s" % (nfibs[0], repr(KS[1]))][:, :3]
    ok = (a1 >= CNULL) & (a2 >= CNULL)
    erg["linearitaet_c_k2_durch_c_k1"] = dict(min=float((a2[ok] / a1[ok]).min()) if ok.any() else None,
                                             max=float((a2[ok] / a1[ok]).max()) if ok.any() else None)
    # Verfeinerung (Konvergenzprobe 3) fuer steife Modelle, Hauptwert KS[0]
    s_main = saetze["nf%d_k%s" % (nfibs[-1], repr(KS[0]))]
    if s_main["steif"]:
        dirs = richtungen(nfibs[-1]); C = roh["c_nf%d_k%s" % (nfibs[-1], repr(KS[0]))][:, :3]
        kk = KS[0]

        def ak3(d):
            s = sing(tm, kk * d / np.linalg.norm(d))
            return s[:3] / kk
        ratio = C[:, 2] / C[:, 0]
        st = dirs[np.argsort(ratio)[:5]]
        r = verfeinern(lambda d: ak3(d)[2] / ak3(d)[0], st)
        ver = dict(min_ratio=r[0], richtung=r[1])
        for b in range(2):
            st_min = dirs[np.argsort(C[:, b])[:3]]; st_max = dirs[np.argsort(-C[:, b])[:3]]
            rmin = verfeinern(lambda d: ak3(d)[b], st_min)
            rmax = verfeinern(lambda d: -ak3(d)[b], st_max)
            ver["ast%d" % b] = dict(min=rmin[0], max=-rmax[0], max_durch_min_minus_1=(-rmax[0]) / rmin[0] - 1,
                                    richtung_min=rmin[1], richtung_max=rmax[1])
        erg["verfeinerung"] = ver
    # Nullmoden: Gitter und generische Punkte
    erg["gitter"] = [gitterzaehlung(net, tm, N) for N in NGITTER]
    erg["generisch"] = zufall(net, tm)
    erg["dauer_s"] = time.time() - t0
    return erg, roh


def main():
    aus = sys.argv[1]
    netze = sys.argv[2].split(",") if len(sys.argv) > 2 else ["fcc", "pyro", "diamant", "srs"]
    modelle = sys.argv[3].split(",") if len(sys.argv) > 3 else ["Z", "W1", "W2"]
    if len(sys.argv) > 4 and sys.argv[4] == "bau":
        # Rauchmodus: nur Netzbau und Zeit je Matrix, keine Geschwindigkeiten
        bau = {}
        for nm in netze:
            net = netz(nm)
            bau[nm] = dict(info=net["info"])
            for md in modelle:
                tm = terme(net, md)
                t1 = time.time()
                for i in range(50):
                    sing(tm, np.array([0.3, 0.2, 0.1]) * (i + 1) / 50)
                bau[nm][md] = dict(zeilen=tm["nrow"], spalten=tm["ncol"], ms_je_svd=1000 * (time.time() - t1) / 50)
            print(nm, json.dumps(bau[nm]), flush=True)
        json.dump(bau, open(aus, "w"), indent=1)
        return
    nfibs = tuple(int(x) for x in sys.argv[4].split(",")) if len(sys.argv) > 4 else (400, 800)
    t0 = time.time()
    res = dict(teil="A", ktheta=KTHETA, ks=KS, cnull=CNULL, ngitter=NGITTER, nzufall=NZUFALL, nfibs=nfibs,
               netze={}, numpy=np.__version__,
               skript_sha256=hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest())
    roh_all = {}
    for nm in netze:
        net = netz(nm)
        res["netze"][nm] = dict(info=net["info"], modelle={})
        print(nm, json.dumps(net["info"]), flush=True)
        for md in modelle:
            e, roh = auswerten_modell(net, md, nfibs)
            res["netze"][nm]["modelle"][md] = e
            for k, v in roh.items():
                roh_all["%s_%s_%s" % (nm, md, k)] = v
            print(nm, md, "steif:", {k: v["steif"] for k, v in e["saetze"].items()}, "dauer %.1f s" % e["dauer_s"], flush=True)
    res["dauer_s"] = time.time() - t0
    res["ende_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    json.dump(res, open(aus, "w"), indent=1)
    np.savez_compressed(aus.replace(".json", ".npz"), **roh_all)


if __name__ == "__main__":
    main()
