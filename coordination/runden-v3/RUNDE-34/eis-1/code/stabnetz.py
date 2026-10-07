# EIS-1 (Runde 34), Teile 2 und 3: lineare Stabnetze (k = 1) auf dem Torus aus L^3 kubischen Zellen.
# Aufrufe (nur ueber kleintest.sh):
#   stabnetz.py antwort <pyro|fcc> <L> <ausgabe.json>    Fehlpass delta = 1 in einem Stab, Stabkraefte, Messung
#   stabnetz.py zaehlen <pyro|fcc> <L1,L2,...> <dicht|bloch> <ausgabe.json>   Zahl der Eigenspannungen
import sys, os, json, time, hashlib
import numpy as np
import scipy
import scipy.sparse as sp
from scipy.sparse.linalg import lsqr

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import gitter

TOL_REL = 1e-9          # Rang-Schwelle: Singulaerwert < TOL_REL * groesster Singulaerwert gilt als null
SCHWELLE = 1e-9         # Messschwelle fuer |t| (delta = 1)
KEGEL_GRAD = 10.0       # halber Oeffnungswinkel der Richtungskegel
BIN = 0.25              # Breite der Abstandsklassen (Zellkanten)
N0 = np.array([0.0, 1.0, 1.0]) / np.sqrt(2.0)   # Richtung des Fehlpass-Stabs
GRUPPEN = {
    "110_par": [[0, 1, 1]],
    "110_senk": [[0, 1, -1]],
    "110_60": [[1, 1, 0], [1, -1, 0], [1, 0, 1], [1, 0, -1]],
    "100_senk": [[1, 0, 0]],
    "100_45": [[0, 1, 0], [0, 0, 1]],
    "111_35": [[1, 1, 1], [-1, 1, 1]],
    "111_90": [[1, 1, -1], [1, -1, 1]],
}


def netz(art, L):
    if art == "pyro":
        g, pos, st = gitter.pyrochlor_staebe(L)
        pruef = g["pruef"]
        je_zelle = 16
        basis = (gitter.F_FCC[:, None, :] + gitter.B_PYR[None, :, :]).reshape(-1, 3)
        d0 = np.array([0, 2, 2])
    else:
        pos, st = gitter.fcc_netz(L)
        je_zelle = 4
        basis = gitter.F_FCC.copy()
        d0 = np.array([0, 4, 4])
        grad = np.bincount(st[:, :2].ravel(), minlength=len(pos))
        d2 = (st[:, 2:5] ** 2).sum(1)
        pruef = dict(knoten=int(len(pos)), knoten_soll=4 * L ** 3, staebe=int(len(st)), staebe_soll=24 * L ** 3,
                     nachbarn_je_knoten_min_max=[int(grad.min()), int(grad.max())],
                     stablaenge2_min_max_in_1_64=[int(d2.min()), int(d2.max())],
                     doppelte_staebe=int(len(st) - len({(min(a, b), max(a, b)) for a, b in st[:, :2]})))
    # kanonische Orientierung: erste von null verschiedene Komponente des Stabvektors positiv
    st = st.copy()
    for b in range(len(st)):
        d = st[b, 2:5]
        nzk = d[np.nonzero(d)[0][0]]
        if nzk < 0:
            st[b] = [st[b, 1], st[b, 0], -d[0], -d[1], -d[2]]
    return pos, st, pruef, je_zelle, basis, d0


def kompat(pos, st):
    nb = len(st); n = len(pos)
    d = st[:, 2:5].astype(float)
    nv = d / np.linalg.norm(d, axis=1)[:, None]
    rows = np.repeat(np.arange(nb), 6)
    cols = np.empty((nb, 6), dtype=int)
    vals = np.empty((nb, 6))
    for k in range(3):
        cols[:, k] = 3 * st[:, 0] + k; vals[:, k] = -nv[:, k]
        cols[:, 3 + k] = 3 * st[:, 1] + k; vals[:, 3 + k] = nv[:, k]
    C = sp.csr_matrix((vals.ravel(), (rows, cols.ravel())), shape=(nb, 3 * n))
    return C, nv


def bloch_typen(pos, st, je_zelle, basis, L):
    """Stabtypen der kubischen Zelle (Stab beginnt in Zelle 0): (a, a', Zellversatz m, Einheitsvektor)."""
    idx_basis = {tuple(b % 8): a for a, b in enumerate(basis)}
    typen = []
    for (i, j, dx, dy, dz) in st:
        if i // je_zelle != 0:
            continue
        a = i % je_zelle
        p = pos[i] + np.array([dx, dy, dz])
        m = np.floor_divide(p, 8)
        a2 = idx_basis[tuple(p % 8)]
        d = np.array([dx, dy, dz], dtype=float)
        typen.append((a, a2, m, d / np.linalg.norm(d), (int(dx), int(dy), int(dz))))
    return typen


def bloch_C(typen, je_zelle, qv):
    nb = len(typen)
    C = np.zeros((nb, 3 * je_zelle), dtype=complex)
    for b, (a, a2, m, nv, dk) in enumerate(typen):
        C[b, 3 * a:3 * a + 3] -= nv
        C[b, 3 * a2:3 * a2 + 3] += nv * np.exp(1j * np.dot(qv, m))
    return C


def bloch_lauf(typen, je_zelle, L, b0_typ=None):
    """Eigenspannungen je q zaehlen; optional Spalte b0_typ des Eigenspannungs-Projektors je q."""
    nb = len(typen)
    zahl = 0
    s_max = 0.0
    sv = []
    spalte = None if b0_typ is None else np.zeros((nb, L, L, L), dtype=complex)
    for n1 in range(L):
        for n2 in range(L):
            for n3 in range(L):
                qv = 2 * np.pi * np.array([n1, n2, n3]) / L
                Cq = bloch_C(typen, je_zelle, qv)
                U, s, Vh = np.linalg.svd(Cq, full_matrices=True)
                sv.append(s)
                s_max = max(s_max, s.max())
    tol = TOL_REL * s_max
    max_null = 0.0; min_nicht = np.inf
    k = 0
    for n1 in range(L):
        for n2 in range(L):
            for n3 in range(L):
                s = sv[k]; k += 1
                nn = int(np.sum(s < tol)) + (nb - len(s))
                zahl += nn
                if np.any(s < tol):
                    max_null = max(max_null, float(s[s < tol].max()))
                if np.any(s >= tol):
                    min_nicht = min(min_nicht, float(s[s >= tol].min()))
                if spalte is not None and nn > 0:
                    qv = 2 * np.pi * np.array([n1, n2, n3]) / L
                    Cq = bloch_C(typen, je_zelle, qv)
                    U, s2, Vh = np.linalg.svd(Cq, full_matrices=True)
                    maske = np.concatenate([s2 < tol, np.ones(nb - len(s2), dtype=bool)])
                    U0 = U[:, maske]
                    spalte[:, n1, n2, n3] = U0 @ np.conj(U0[b0_typ, :])
    return zahl, tol, max_null, min_nicht, spalte


def zaehlen(art, Ls, methode):
    erg = []
    for L in Ls:
        t0 = time.time()
        pos, st, pruef, je_zelle, basis, d0 = netz(art, L)
        if methode == "dicht":
            C, nv = kompat(pos, st)
            s = np.linalg.svd(C.toarray(), compute_uv=False)
            tol = TOL_REL * s.max()
            rang = int(np.sum(s > tol))
            nb, ndof = C.shape
            erg.append(dict(L=L, methode="dicht", staebe=nb, freiheitsgrade=ndof, rang=rang,
                            eigenspannungen=nb - rang, nullmoden=ndof - rang,
                            max_null_sv=float(s[s <= tol].max()) if np.any(s <= tol) else None,
                            min_nicht_null_sv=float(s[s > tol].min()), gitter=pruef, dauer_s=time.time() - t0))
        else:
            typen = bloch_typen(pos, st, je_zelle, basis, L)
            zahl, tol, mx0, mn1, _ = bloch_lauf(typen, je_zelle, L)
            nb = len(st); ndof = 3 * len(pos)
            erg.append(dict(L=L, methode="bloch", staebe=nb, freiheitsgrade=ndof, eigenspannungen=zahl,
                            nullmoden=zahl - (nb - ndof), rang=nb - zahl, max_null_sv=mx0, min_nicht_null_sv=mn1,
                            stabtypen_je_zelle=len(typen), gitter=pruef, dauer_s=time.time() - t0))
        print(json.dumps(erg[-1]))
    return erg


def antwort(art, L):
    t0 = time.time()
    pos, st, pruef, je_zelle, basis, d0 = netz(art, L)
    P = 8 * L
    C, nv = kompat(pos, st)
    nb = len(st)
    b0 = int(np.where((st[:, 0] == 0) & np.all(st[:, 2:5] == d0, axis=1))[0][0])
    e0 = np.zeros(nb); e0[b0] = 1.0
    # Hauptweg: kleinste Quadrate ohne Regularisierung (lsqr), t = C u - e0
    r = lsqr(C, e0, atol=1e-15, btol=1e-15, conlim=1e14, iter_lim=200000)
    u = r[0]
    t = C @ u - e0
    gleich = C.T @ t
    t_lsqr_s = time.time() - t0
    # Gegenweg: exakte Projektion auf die Eigenspannungen ueber Bloch-Zerlegung der kubischen Zelle
    t1 = time.time()
    typen = bloch_typen(pos, st, je_zelle, basis, L)
    typ_idx = {}
    for k, (a, a2, m, nvt, dk) in enumerate(typen):
        typ_idx[(a, dk)] = k
    b0_typ = typ_idx[(0, tuple(int(x) for x in d0))]
    zahl, tol, mx0, mn1, spalte = bloch_lauf(typen, je_zelle, L, b0_typ)
    T = np.real(np.fft.ifftn(spalte, axes=(1, 2, 3)))  # (P e_b0)(R, beta)
    # Zuordnung Stab -> (Typ, Zelle)
    t_bloch = np.zeros(nb)
    for b in range(nb):
        i = st[b, 0]
        zelle = i // je_zelle
        cx, cy, cz = zelle // (L * L), (zelle // L) % L, zelle % L
        k = typ_idx[(i % je_zelle, tuple(int(x) for x in st[b, 2:5]))]
        t_bloch[b] = -T[k, cx, cy, cz]
    t_bloch_s = time.time() - t1
    # Messung
    mitte = pos[st[:, 0]] + st[:, 2:5] / 2.0
    rel = gitter.minbild(mitte - mitte[b0], P) / 8.0
    r_ = np.linalg.norm(rel, axis=1)
    at = np.abs(t)
    rmax = np.sqrt(3) * L / 2
    kanten = np.arange(0, rmax + BIN, BIN)
    klasse = np.digitize(r_, kanten) - 1
    cosk = np.cos(np.radians(KEGEL_GRAD))
    einheit = np.zeros_like(rel)
    nz = r_ > 0
    einheit[nz] = rel[nz] / r_[nz, None]

    def klassen(maske):
        aus = []
        for c in range(len(kanten) - 1):
            mk = maske & (klasse == c) & nz
            if not np.any(mk):
                continue
            ids = np.where(mk)[0]
            jm = ids[np.argmax(at[ids])]
            aus.append(dict(r_lo=float(kanten[c]), r_hi=float(kanten[c + 1]), n=int(mk.sum()),
                            max_t=float(at[jm]), r_max=float(r_[jm]), rms_t=float(np.sqrt(np.mean(t[ids] ** 2))),
                            r_mittel=float(np.mean(r_[ids]))))
        return aus

    gruppen = {}
    for name, achsen in GRUPPEN.items():
        m = np.zeros(nb, dtype=bool)
        for a in achsen:
            a = np.array(a, float) / np.linalg.norm(a)
            m |= np.abs(einheit @ a) >= cosk
        gruppen[name] = dict(winkel_zu_stab_grad=float(np.degrees(np.arccos(abs(np.dot(np.array(achsen[0], float) / np.linalg.norm(achsen[0]), N0))))),
                             klassen=klassen(m))
    kugel = klassen(np.ones(nb, dtype=bool))
    # Linie durch den Fehlpass-Stab (kollinear, gleiche Richtung)
    quer = np.linalg.norm(np.cross(rel, N0), axis=1)
    parallel = np.abs(np.abs(nv @ N0) - 1) < 1e-9
    linie = (quer < 1e-9) & parallel
    aus = dict(
        teil="Stabnetz", netz=art, L=L, gitter=pruef, staebe=int(nb), knoten=int(len(pos)), b0=b0,
        b0_typ=b0_typ, lsqr_istop=int(r[1]), lsqr_iter=int(r[2]), lsqr_s=t_lsqr_s,
        gleichgewicht_rest_max=float(np.abs(gleich).max()), t_b0=float(t[b0]),
        bloch_eigenspannungen=int(zahl), bloch_max_null_sv=mx0, bloch_min_nicht_null_sv=mn1, bloch_s=t_bloch_s,
        lsqr_gegen_bloch_max=float(np.abs(t - t_bloch).max()), t_b0_bloch=float(t_bloch[b0]),
        energie=float(0.5 * np.sum(t ** 2)), summe_t2=float(np.sum(t ** 2)),
        linie_staebe=int(linie.sum()), linie_t_min_max=[float(t[linie].min()), float(t[linie].max())],
        abseits_linie_max_abs_t=float(at[~linie].max()) if np.any(~linie) else None,
        anteil_unter_schwelle=float(np.mean(at < SCHWELLE)),
        anteil_unter_1e12=float(np.mean(at < 1e-12)),
        kugel=kugel, gruppen=gruppen,
        dauer_s=time.time() - t0, scipy=scipy.__version__, numpy=np.__version__,
        skript_sha256=hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
        ende_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    )
    return aus


if __name__ == "__main__":
    modus = sys.argv[1]
    if modus == "antwort":
        aus = antwort(sys.argv[2], int(sys.argv[3]))
        json.dump(aus, open(sys.argv[4], "w"), indent=1)
        print(json.dumps({k: aus[k] for k in ("netz", "L", "lsqr_istop", "lsqr_iter", "gleichgewicht_rest_max", "t_b0",
                                              "bloch_eigenspannungen", "lsqr_gegen_bloch_max", "linie_staebe",
                                              "linie_t_min_max", "abseits_linie_max_abs_t", "dauer_s")}, indent=1))
    else:
        Ls = [int(x) for x in sys.argv[3].split(",")]
        erg = zaehlen(sys.argv[2], Ls, sys.argv[4])
        json.dump(dict(teil="Eigenspannungen", netz=sys.argv[2], methode=sys.argv[4], ergebnisse=erg,
                       skript_sha256=hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
                       ende_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())),
                  open(sys.argv[5], "w"), indent=1)
