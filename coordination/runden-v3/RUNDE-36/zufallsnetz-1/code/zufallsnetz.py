# ZUFALLSNETZ-1 (Runde 36): Elastizitaetstensor periodischer Poisson-Delaunay-Federnetze mit nichtaffiner Relaxation,
# Christoffel-Geschwindigkeiten. Code-Agent fuer die Leitung claude-primary. Nur ueber kleintest.sh auf der .69 starten.
# Aufrufe:
#   zufallsnetz.py netz <N> <saat> <feder k1|kl> <ausgabe.json> [rauch]
#   zufallsnetz.py fcc <ausgabe.json> <netz_a.npz>                    (Gegenprobe Z0 gegen NETZ-C-1)
#   zufallsnetz.py kontrolle <N> <saat> <feder> <ausgabe.json> [rauch] (Direktloeser, Toleranzen, Born-Grenzwert)
# Einheiten: Punktdichte 1 (L = N^(1/3)), Masse 1 je Knoten, k = 1 (k1) oder k = 1/l (kl), Ruhelaenge = Kantenlaenge.
import sys, os, json, time, hashlib, itertools, resource
import numpy as np
import scipy
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.spatial import Delaunay

DICHTE = 1.0          # Punkte je Volumeneinheit
RAND = 5.0            # Rand m der Bildpunkt-Schale (Einheiten DICHTE^(-1/3)); Pruefung ueber Umkugeln
CG_RTOL = 1e-10       # ||H u + f|| <= CG_RTOL ||f||
CG_MAXITER = 50000
SAAT_BASIS = 20261003
NFIB = 400
VOIGT = ((0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1))   # Voigt 1..6 = 11, 22, 33, 23, 13, 12 (Ingenieur-Scherung)
SYM = {"[100]": [1.0, 0.0, 0.0], "[110]": [1.0, 1.0, 0.0], "[111]": [1.0, 1.0, 1.0]}
SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()


def jetzt():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def maxrss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


# ---------------------------------------------------------------- Richtungen (identisch zu NETZ-C-1 netz_a.py)
def fibonacci(N):
    i = np.arange(N)
    z = 1 - (2 * i + 1) / N
    r = np.sqrt(1 - z * z)
    phi = i * np.pi * (3 - np.sqrt(5.0))
    return np.stack([r * np.cos(phi), r * np.sin(phi), z], 1)


def richtungen(N=NFIB):
    sym = np.array([np.array(v) / np.linalg.norm(v) for v in SYM.values()])
    return np.vstack([sym, fibonacci(N)])


# ---------------------------------------------------------------- Netze
def punkte(N, saat):
    L = (N / DICHTE) ** (1.0 / 3.0)
    rng = np.random.default_rng(np.random.SeedSequence([SAAT_BASIS, 36, int(N), int(saat)]))
    return rng.random((N, 3)) * L, L


def periodisches_delaunay(X, L, m=RAND):
    """Delaunay des periodischen Punktsatzes: Bildpunkte in [-m, L+m)^3, Kanten mit mindestens einem Ende im Grundwuerfel,
    Duplikate ueber periodische Indizes (i, j, s) entfernt. Rueckgabe ei, ej, es (Kante i -> j + L s) und Pruefwerte."""
    N = len(X)
    sh = np.array(sorted(itertools.product((-1, 0, 1), repeat=3), key=lambda s: sum(abs(x) for x in s)), dtype=np.int64)
    P, I, S = [], [], []
    for s in sh:
        Y = X + L * s
        msk = np.all((Y >= -m) & (Y < L + m), axis=1)
        P.append(Y[msk]); I.append(np.nonzero(msk)[0]); S.append(np.repeat(s[None, :], int(msk.sum()), 0))
    P = np.vstack(P); I = np.concatenate(I).astype(np.int64); S = np.vstack(S).astype(np.int64)
    NP = len(P)
    t0 = time.time()
    tri = Delaunay(P)
    t_del = time.time() - t0
    simp = tri.simplices.astype(np.int64)
    orig = np.all(S == 0, axis=1)
    ib = orig[simp]
    keep = ib.any(1)
    sk = simp[keep]; ibk = ib[keep]
    # Umkugeln aller Tetraeder mit einer Ecke im Grundwuerfel: muessen ganz in [-m, L+m]^3 liegen
    p0 = P[sk[:, 0]]
    Am = 2.0 * (P[sk[:, 1:]] - p0[:, None, :])
    rh = (P[sk[:, 1:]] ** 2).sum(2) - (p0 ** 2).sum(1)[:, None]
    cc = np.linalg.solve(Am, rh[..., None])[..., 0]
    R = np.linalg.norm(cc - p0, axis=1)
    ueber = np.maximum((-m) - (cc - R[:, None]), (cc + R[:, None]) - (L + m)).max(1)   # > 0: Kugel ragt hinaus
    T4 = int(ibk.sum())
    # Kanten der behaltenen Tetraeder
    pa = np.array([0, 0, 0, 1, 1, 2]); pb = np.array([1, 2, 3, 2, 3, 3])
    ea = sk[:, pa].ravel(); eb = sk[:, pb].ravel()
    lo = np.minimum(ea, eb); hi = np.maximum(ea, eb)
    bk = np.unique(lo * NP + hi)
    lo = bk // NP; hi = bk % NP
    mit = orig[lo] | orig[hi]
    lo = lo[mit]; hi = hi[mit]
    i = I[lo]; j = I[hi]; s = S[hi] - S[lo]
    s_ok = bool(np.all(np.abs(s) <= 1))
    code = (s[:, 0] + 1) * 9 + (s[:, 1] + 1) * 3 + (s[:, 2] + 1)
    swap = (i > j) | ((i == j) & (code < 13))
    i2 = np.where(swap, j, i); j2 = np.where(swap, i, j); code2 = np.where(swap, 26 - code, code)
    key = (i2 * N + j2) * 27 + code2
    uk, cnt = np.unique(key, return_counts=True)
    ci = uk % 27; ij = uk // 27
    ei = ij // N; ej = ij % N
    es = np.stack([ci // 9 - 1, (ci // 3) % 3 - 1, ci % 3 - 1], 1).astype(np.int64)
    soll = np.where(np.all(es == 0, axis=1), 1, 2)
    grad = np.bincount(ei, minlength=N) + np.bincount(ej, minlength=N)
    E = len(ei)
    copl = tri.coplanar
    copl_orig = int(np.sum(orig[copl[:, 0]])) if len(copl) else 0
    kh = hashlib.sha256(np.stack([ei, ej, es[:, 0], es[:, 1], es[:, 2]], 1).astype(np.int64).tobytes()).hexdigest()
    diag = dict(punkte_erweitert=int(NP), delaunay_s=t_del, tetraeder_gesamt=int(len(simp)),
                tetraeder_mit_ecke_im_wuerfel=int(len(sk)),
                tetraeder_periodisch=T4 / 4.0, tetraeder_je_punkt=T4 / 4.0 / N, tetraeder_ganzzahlig=(T4 % 4 == 0),
                kanten=int(E), mittlerer_grad=2.0 * E / N, grad_min=int(grad.min()), grad_max=int(grad.max()),
                euler_E_gleich_N_plus_T=bool(T4 % 4 == 0 and E == N + T4 // 4),
                umkugel_max_ueberstand=float(ueber.max()), umkugeln_im_rand=bool(ueber.max() <= 0.0),
                umkugel_radius_max=float(R.max()),
                kanten_beidseitig_gefunden=bool(np.all(cnt == soll)), kanten_verschiebung_ok=s_ok,
                koplanar_ausgelassen_orig=copl_orig, selbstkanten=int(np.sum(ei == ej)), kanten_sha256=kh)
    return ei, ej, es, diag


def fcc_netz(nz=4):
    """fcc mit Kante 1 (a = sqrt 2), nz^3 kubische Zellen, Kanten = naechste Nachbarn (Abstand 1)."""
    a = np.sqrt(2.0)
    basis = np.array([[0, 0, 0], [0, .5, .5], [.5, 0, .5], [.5, .5, 0]])
    zellen = np.array(list(itertools.product(range(nz), repeat=3)), float)
    X = (zellen[:, None, :] + basis[None, :, :]).reshape(-1, 3) * a
    L = nz * a
    ei, ej, es = [], [], []
    for s in itertools.product((-1, 0, 1), repeat=3):
        s = np.array(s)
        D = X[None, :, :] + L * s - X[:, None, :]
        dist = np.linalg.norm(D, axis=2)
        ii, jj = np.nonzero(np.abs(dist - 1.0) < 1e-9)
        c = (s[0] + 1) * 9 + (s[1] + 1) * 3 + (s[2] + 1)
        for i_, j_ in zip(ii, jj):
            if i_ < j_ or (i_ == j_ and c > 13):
                ei.append(i_); ej.append(j_); es.append(s)
    return X, L, np.array(ei, np.int64), np.array(ej, np.int64), np.array(es, np.int64)


# ---------------------------------------------------------------- Elastizitaet
def geometrie(X, L, ei, ej, es, feder):
    d = X[ej] + L * es - X[ei]
    l = np.linalg.norm(d, axis=1)
    n = d / l[:, None]
    if feder == "k1":
        k = np.ones_like(l)
    elif feder == "kl":
        k = 1.0 / l
    else:
        raise ValueError(feder)
    return d, l, n, k


def kompatibilitaet(N, ei, ej, n, phase=None):
    """M (E x 3N): Zeile e = -n^T am Knoten i, +n^T (mal Phase) am Knoten j."""
    E = len(ei)
    rows = np.repeat(np.arange(E), 6)
    cols = np.concatenate([3 * ei[:, None] + np.arange(3), 3 * ej[:, None] + np.arange(3)], 1).ravel()
    if phase is None:
        vals = np.concatenate([-n, n], 1).ravel()
    else:
        vals = np.concatenate([-n.astype(complex), n * phase[:, None]], 1).ravel()
    return sp.csr_matrix((vals, (rows, cols)), shape=(E, 3 * N))


def elastizitaet(X, L, ei, ej, es, feder, rtol=CG_RTOL, direkt=False):
    """Voigt-Matrizen (6x6, Ingenieur-Scherung): affin und nach nichtaffiner Relaxation (CG, Block-Jacobi)."""
    N = len(X); V = L ** 3
    d, l, n, k = geometrie(X, L, ei, ej, es, feder)
    M = kompatibilitaet(N, ei, ej, n)
    H = (M.T @ sp.diags(k) @ M).tocsr()
    v6 = np.stack([n[:, 0] ** 2, n[:, 1] ** 2, n[:, 2] ** 2, n[:, 1] * n[:, 2], n[:, 0] * n[:, 2], n[:, 0] * n[:, 1]], 1)
    A = l[:, None] * v6                 # affine Dehnung je Kante fuer die sechs Einheitsverzerrungen
    KA = k[:, None] * A
    C_aff = A.T @ KA / V
    F = np.asarray(M.T @ KA)            # affine Knotenkraefte (bis aufs Vorzeichen)
    nn = k[:, None, None] * n[:, :, None] * n[:, None, :]
    B = np.zeros((N, 3, 3))
    for a_ in range(3):
        for b_ in range(3):
            B[:, a_, b_] = np.bincount(ei, nn[:, a_, b_], minlength=N) + np.bincount(ej, nn[:, a_, b_], minlength=N)
    Binv = np.linalg.inv(B)
    Pop = spla.LinearOperator((3 * N, 3 * N), dtype=np.float64,
                              matvec=lambda x: np.einsum("nij,nj->ni", Binv, x.reshape(N, 3)).ravel())
    skala = np.sqrt((KA * A).sum(0))
    U = np.zeros((3 * N, 6)); cginfo = []
    for b in range(6):
        fb = F[:, b]
        nf = float(np.linalg.norm(fb))
        t0 = time.time()
        if nf <= 1e-12 * skala[b]:
            cginfo.append(dict(verzerrung=b + 1, rechte_seite_null=True, f_norm=nf))
            continue
        it = [0]

        def cb(xk, it=it):
            it[0] += 1
        u, inf = spla.cg(H, -fb, rtol=rtol, atol=0.0, maxiter=CG_MAXITER, M=Pop, callback=cb)
        u = u.reshape(N, 3); u = (u - u.mean(0)).ravel()
        r = H @ u + fb
        U[:, b] = u
        cginfo.append(dict(verzerrung=b + 1, iterationen=it[0], cg_info=int(inf),
                           rel_residuum=float(np.linalg.norm(r) / nf), dauer_s=time.time() - t0))
    T = A + M @ U
    C = T.T @ (k[:, None] * T) / V              # Energieform, Fehler quadratisch im Loeserfehler
    C_alt = (A.T @ KA + F.T @ U) / V            # Kurzform, Fehler linear
    out = dict(C_aff=C_aff, C=C, C_alt=C_alt, cg=cginfo,
               kanten=int(len(l)), l_mittel=float(l.mean()), l_min=float(l.min()), l_max=float(l.max()),
               l2_mittel=float((l ** 2).mean()), k_mittel=float(k.mean()),
               asym_C_alt=float(np.abs(C_alt - C_alt.T).max() / np.abs(C).max()),
               diff_C_C_alt=float(np.abs(C - C_alt).max() / np.abs(C).max()),
               nichtaffin_u2_je_knoten=[float((U[:, b] ** 2).sum() / N) for b in range(6)],
               nnz_H=int(H.nnz))
    if direkt:
        t0 = time.time()
        lu = spla.splu(H[3:, 3:].tocsc(), permc_spec="MMD_AT_PLUS_A")
        Ud = np.zeros((3 * N, 6))
        for b in range(6):
            if np.linalg.norm(F[:, b]) <= 1e-12 * skala[b]:
                continue
            Ud[3:, b] = lu.solve(-F[3:, b])
            ud = Ud[:, b].reshape(N, 3); Ud[:, b] = (ud - ud.mean(0)).ravel()
        Td = A + M @ Ud
        Cd = Td.T @ (k[:, None] * Td) / V
        out["C_direkt"] = Cd
        out["direkt_s"] = time.time() - t0
        out["diff_C_direkt"] = float(np.abs(C - Cd).max() / np.abs(Cd).max())
        out["rel_residuum_direkt"] = [float(np.linalg.norm(H @ Ud[:, b] + F[:, b]) / max(np.linalg.norm(F[:, b]), 1e-300))
                                      for b in range(6)]
    return out


# ---------------------------------------------------------------- Tensor, Christoffel, isotrope Projektion
def tensor4(Cv):
    Cv = 0.5 * (np.asarray(Cv) + np.asarray(Cv).T)
    C4 = np.zeros((3, 3, 3, 3))
    for a, (i, j) in enumerate(VOIGT):
        for b, (k, l) in enumerate(VOIGT):
            for (ii, jj) in {(i, j), (j, i)}:
                for (kk, ll) in {(k, l), (l, k)}:
                    C4[ii, jj, kk, ll] = Cv[a, b]
    return C4


def christoffel(Cv, rho, dirs):
    """Geschwindigkeiten (n x 3, aufsteigend) aus Gamma_ik = C_ijkl n_j n_l / rho."""
    C4 = tensor4(Cv)
    G = np.einsum("ijkl,nj,nl->nik", C4, dirs, dirs)
    w = np.linalg.eigvalsh(G)
    return np.sqrt(np.maximum(w, 0.0) / rho), w / rho


def iso(Cv):
    """Isotrope Projektion (Voigt-Mittel): lambda, mu (= G_V), Kompressionsmodul K_V."""
    C4 = tensor4(Cv)
    a = np.einsum("iijj->", C4); b = np.einsum("ijij->", C4)
    mu = (3 * b - a) / 30.0; lam = (2 * a - b) / 15.0
    return float(lam), float(mu), float(a / 9.0)


def liste(A):
    return [[float(x) for x in row] for row in np.asarray(A)]


# ---------------------------------------------------------------- Modi
def modus_netz(N, saat, feder, aus, rauch=False):
    t0 = time.time()
    res = dict(modus="netz", N=N, saat=saat, feder=feder, rauch=rauch, start_utc=jetzt(), skript_sha256=SKRIPT_SHA,
               numpy=np.__version__, scipy=scipy.__version__, dichte=DICHTE, rand=RAND, cg_rtol=CG_RTOL)
    X, L = punkte(N, saat)
    res["L"] = L; res["V"] = L ** 3; res["rho"] = N / L ** 3
    ei, ej, es, diag = periodisches_delaunay(X, L)
    res["delaunay"] = diag
    print("delaunay", json.dumps(diag), flush=True)
    res["netz_s"] = time.time() - t0
    el = elastizitaet(X, L, ei, ej, es, feder)
    ev_aff = np.linalg.eigvalsh(0.5 * (el["C_aff"] + el["C_aff"].T)); ev = np.linalg.eigvalsh(0.5 * (el["C"] + el["C"].T))
    res["elast_diag"] = dict(cg=el["cg"], asym_C_alt=el["asym_C_alt"], diff_C_C_alt=el["diff_C_C_alt"],
                             nnz_H=el["nnz_H"], stabil=bool(ev.min() > 0), stabil_affin=bool(ev_aff.min() > 0))
    print("cg", json.dumps(el["cg"]), "asym", el["asym_C_alt"], "diffCalt", el["diff_C_C_alt"], flush=True)
    if not rauch:
        res["kanten"] = dict(zahl=el["kanten"], l_mittel=el["l_mittel"], l_min=el["l_min"], l_max=el["l_max"],
                             l2_mittel=el["l2_mittel"], k_mittel=el["k_mittel"])
        res["C_aff"] = liste(el["C_aff"]); res["C"] = liste(el["C"]); res["C_alt"] = liste(el["C_alt"])
        res["eig_C_aff"] = [float(x) for x in ev_aff]; res["eig_C"] = [float(x) for x in ev]
        res["nichtaffin_u2_je_knoten"] = el["nichtaffin_u2_je_knoten"]
    res["dauer_s"] = time.time() - t0; res["maxrss_mb"] = maxrss_mb(); res["ende_utc"] = jetzt()
    json.dump(res, open(aus, "w"), indent=1)
    print("fertig", res["dauer_s"], "s, maxrss", res["maxrss_mb"], "MB", flush=True)


def modus_fcc(aus, npz):
    t0 = time.time()
    X, L, ei, ej, es = fcc_netz(4)
    N = len(X)
    el = elastizitaet(X, L, ei, ej, es, "k1")
    rho = N / L ** 3
    dirs = richtungen(NFIB)
    c, _ = christoffel(el["C"], rho, dirs)
    ref_all = np.load(npz)
    schl = "fcc_Z_c_nf400_k0.001"
    ref = ref_all[schl][:, :3]
    rel = np.abs(c / ref - 1.0)
    c0 = 1 / np.sqrt(2.0)
    geschlossen = np.array([[c0, c0, c0 * np.sqrt(2)], [c0 / np.sqrt(2), c0, c0 * np.sqrt(2.5)],
                            [c0 * np.sqrt(2 / 3.), c0 * np.sqrt(2 / 3.), c0 * np.sqrt(8 / 3.)]])
    res = dict(modus="fcc", start_utc=jetzt(), skript_sha256=SKRIPT_SHA, npz=os.path.abspath(npz),
               npz_sha256=hashlib.sha256(open(npz, "rb").read()).hexdigest(), npz_schluessel=schl,
               knoten=N, kanten=int(len(ei)), grad=2.0 * len(ei) / N, L=L, rho=rho,
               C=liste(el["C"]), C_aff=liste(el["C_aff"]), cg=el["cg"],
               diff_C_C_aff=float(np.abs(el["C"] - el["C_aff"]).max()),
               C_soll=dict(C11=2 / np.sqrt(2), C12=1 / np.sqrt(2), C44=1 / np.sqrt(2)),
               max_rel_abw_netz_c_1=float(rel.max()), ort_max=[int(x) for x in np.unravel_index(rel.argmax(), rel.shape)],
               richtungen=int(len(dirs)),
               sym_c=liste(c[:3]), sym_ref=liste(ref[:3]),
               max_rel_abw_geschlossen=float(np.abs(c[:3] / geschlossen - 1).max()))
    res["dauer_s"] = time.time() - t0; res["ende_utc"] = jetzt()
    json.dump(res, open(aus, "w"), indent=1)
    print("fcc", res["max_rel_abw_netz_c_1"], res["max_rel_abw_geschlossen"], flush=True)


def modus_kontrolle(N, saat, feder, aus, rauch=False):
    t0 = time.time()
    res = dict(modus="kontrolle", N=N, saat=saat, feder=feder, rauch=rauch, start_utc=jetzt(), skript_sha256=SKRIPT_SHA)
    X, L = punkte(N, saat)
    V = L ** 3; rho = N / V
    ei, ej, es, diag = periodisches_delaunay(X, L)
    res["delaunay_kanten_sha256"] = diag["kanten_sha256"]
    # 1) Direktloeser gegen CG; 2) Toleranzen
    e10 = elastizitaet(X, L, ei, ej, es, feder, rtol=1e-10, direkt=True)
    res["direkt"] = dict(diff_C_cg_direkt=e10["diff_C_direkt"], direkt_s=e10["direkt_s"],
                         rel_residuum_direkt=e10["rel_residuum_direkt"], cg=e10["cg"])
    print("direkt", res["direkt"]["diff_C_cg_direkt"], flush=True)
    tol = {}
    for rt in (1e-6, 1e-8, 1e-12):
        e = elastizitaet(X, L, ei, ej, es, feder, rtol=rt)
        tol[repr(rt)] = dict(diff_C_gegen_direkt=float(np.abs(e["C"] - e10["C_direkt"]).max() / np.abs(e10["C_direkt"]).max()),
                             diff_C_alt_gegen_direkt=float(np.abs(e["C_alt"] - e10["C_direkt"]).max() / np.abs(e10["C_direkt"]).max()),
                             iterationen=[g.get("iterationen") for g in e["cg"]],
                             rel_residuum=[g.get("rel_residuum") for g in e["cg"]])
        print("rtol", rt, json.dumps(tol[repr(rt)]), flush=True)
    res["toleranzen"] = tol
    # 3) Born-Grenzwert langer Wellen: Dynamische Matrix bei kleinem Bloch-k gegen Christoffel aus dem relaxierten C
    d, l, n, k = geometrie(X, L, ei, ej, es, feder)
    dirs = richtungen(NFIB)
    auswahl = [(0, 1e-3), (1, 1e-3), (2, 1e-3), (203, 1e-3), (0, 2e-3)]
    cC, _ = christoffel(e10["C_direkt"], rho, dirs)
    born = []
    res["born"] = born
    for (idx, f) in auswahl:
        t1 = time.time()
        kap = f * 2 * np.pi / L
        kv = kap * dirs[idx]
        Mk = kompatibilitaet(N, ei, ej, n, phase=np.exp(1j * (d @ kv)))
        D = (Mk.conj().T @ sp.diags(k) @ Mk).tocsc()
        w = spla.eigsh(D, k=3, sigma=0, which="LM", return_eigenvectors=False, tol=1e-14)
        cdyn = np.sqrt(np.sort(np.real(w))) / kap
        rel = cdyn / cC[idx] - 1.0
        born.append(dict(richtung_index=idx, k_durch_2pi_L=f, rel_abw=[float(x) for x in rel], dauer_s=time.time() - t1))
        print("born", idx, f, [float(x) for x in rel], "%.1f s" % (time.time() - t1), flush=True)
        json.dump(res, open(aus, "w"), indent=1)     # Zwischenstand
    if not rauch:
        res["C_direkt"] = liste(e10["C_direkt"]); res["C_cg"] = liste(e10["C"])
    res["dauer_s"] = time.time() - t0; res["maxrss_mb"] = maxrss_mb(); res["ende_utc"] = jetzt()
    json.dump(res, open(aus, "w"), indent=1)
    print("fertig", res["dauer_s"], flush=True)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "netz":
        modus_netz(int(a[1]), int(a[2]), a[3], a[4], rauch=(len(a) > 5 and a[5] == "rauch"))
    elif a[0] == "fcc":
        modus_fcc(a[1], a[2])
    elif a[0] == "kontrolle":
        modus_kontrolle(int(a[1]), int(a[2]), a[3], a[4], rauch=(len(a) > 5 and a[5] == "rauch"))
    else:
        raise SystemExit("unbekannter Modus " + a[0])
