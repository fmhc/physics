#!/usr/bin/env python3
"""REGGE-4D-SCHIEF-1 (Runde 37, Code-Agent): schief abgebildetes periodisches 4D-Kuhn-Gitter, X -> A X.

A = diag(1, A_raum), A_raum = 1 + s B; B fest (Saat 20261004, Eintraege gleichverteilt in [-1, 1]); die Zeitachse
bleibt senkrecht. Kantenlaengenquadrate s_e = |A e|^2. Kombinatorik, Weg T und M(k) = A(k)^+ E(k)
(Mittelpunktskonvention) aus regge4d.py (REGGE-4D-1), Loesung, Fixierung und Kalibrierungsbausteine aus
regge_zeit.py (REGGE-ZEIT-1); beide unveraendert importiert. Reines numpy, float64.

  Teil 1: Nullmoden bei k = 0 und allgemeinem k (Schwelle |lambda| < 1e-6 * Mittel |lambda|), Spektren, BZ-Zaehlung,
          Schur-Form auf h in physikalischen Koordinaten: delta s_d = (A d)^T h (A d), k_phys = A^-T k_lat,
          Spinprojektoren mit k_phys, Normierung K / det(A) (Wirkung je physikalischem Volumen).
  Teil 2: ruhende Masse auf den Zeitkanten der Weltlinie x = 0 (statisch, k_tau = 0). Bei s = 0 Nullraum mit
          Hyperdiagonale und Fixierung (Projektion) wie REGGE-ZEIT-1, bei s != 0 Nullraum nur Eichmoden, keine
          Fixierung. Kalibrierung mit physikalischer konstanter Kruemmung; Achsen A e_a; Torus-Korrektur mit Bildern
          in einer physikalischen Kugel und Hintergrund aus dem Mittel ueber physikalische Achsenrichtungen.

Aufruf: python regge_schief.py rauch0 <aus.json>
        python regge_schief.py teil1 <aus.json> <s-Liste> [kurve] [test] [bz]
        python regge_schief.py teil2 <aus.json> <s | rot> <L-Liste>
"""
import hashlib
import itertools
import json
import os
import sys
import time

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import regge4d as R4  # noqa: E402
import regge_zeit as RZ  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
SAAT_B = 20261004          # Matrix B (PLAN [F1])
SAAT_RICHT = 20261005      # 8 zufaellige physikalische Richtungen (PLAN [F4])
SAAT_K = 20261006          # 64 allgemeine Gitterimpulse (PLAN [F3])
NULL_REL = 1e-6            # Nullmode: |lambda| < NULL_REL * Mittel(|lambda|) (Karte SC1, PLAN [F2])
PINV_RCOND = 1e-8          # Pseudoinverse im Schur-Komplement (wie REGGE-4D-1)
BETRAEGE = [0.05, 0.075, 0.1, 0.2, 0.4]
S_KURVE = [0.0, 0.025, 0.05, 0.1, 0.15, 0.2]
TAU = 0
R_BILD = 16.0              # Bildsumme: physikalische Kugel |A_raum n| <= R_BILD (Einheit L), PLAN [F9]
GM = RZ.GM
QUELLE = RZ.QUELLE
KAPPA = RZ.KAPPA
BATCH = 4096


def protokoll(log, s):
    print(s, flush=True)
    log.append(s)


# ======================================================================= Matrizen
def matrix_B():
    return np.random.default_rng(SAAT_B).uniform(-1.0, 1.0, size=(3, 3))


def matrix_A(s=None, A3=None):
    A = np.eye(4)
    if A3 is not None:
        A[1:, 1:] = A3
    else:
        A[1:, 1:] += s * matrix_B()
    return A


def drehung_test():
    """Nur Codeprobe: Drehung um (1,2,3) um 0,7 rad (Gitter isometrisch zu Kuhn, Hyperdiagonale bleibt tot)."""
    n = np.array([1.0, 2.0, 3.0]) / np.sqrt(14.0)
    K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    w = 0.7
    return np.eye(3) + np.sin(w) * K + (1 - np.cos(w)) * K @ K


def diagonal_test():
    """Nur Codeprobe: Streckung diag(1,15; 0,9; 1,05) (rechte Winkel an der Hyperdiagonale bleiben)."""
    return np.diag([1.15, 0.9, 1.05])


# ======================================================================= Gitter
class GitterSchief(R4.Gitter):
    """Kuhn-Gitter (Kombinatorik aus regge4d.py) mit Kantenvektoren A d."""

    def __init__(self, A, L=4):
        super().__init__(4, L)
        self.A = np.array(A, float)
        self.A3 = self.A[1:, 1:]
        self.Ad = self.dirs.astype(float) @ self.A.T
        self.s_dir = np.sum(self.Ad ** 2, axis=1)
        self.s0 = np.tile(self.s_dir, self.N)
        self.detA = float(np.linalg.det(self.A))
        self.tau_index = self.dir_index[(1, 0, 0, 0)]

    def gelenk_ableitung(self, t):
        sq = [float(self.s_dir[d]) for _, d in self.g_kanten[t]]
        A_ = self.gelenkvolumen(sq)
        out = []
        for x in range(3):
            y, z = [q for q in range(3) if q != x]
            out.append((sq[y] + sq[z] - sq[x]) / (16.0 * A_))
        return out

    def sq0_typen(self):
        return np.array([[float(self.s_dir[d]) for _, d in self.p_kanten[ip]] for ip in range(self.nP)])

    def jacobi_lokal(self, h=R4.H_STUFE):
        nEs = len(self.paare)
        sq0 = self.sq0_typen()
        stufen = [h, -h, h / 2, -h / 2]
        batch = []
        for ip in range(self.nP):
            for e in range(nEs):
                for st in stufen:
                    q = sq0[ip].copy()
                    q[e] += st
                    batch.append(q)
        ang = self.winkel(np.array(batch)).reshape(self.nP, nEs, 4, -1)
        D1 = (ang[:, :, 0] - ang[:, :, 1]) / (2 * h)
        D2 = (ang[:, :, 2] - ang[:, :, 3]) / h
        J = np.transpose((4 * D2 - D1) / 3.0, (0, 2, 1))
        return J, self.winkel(sq0), sq0

    def B0(self):
        """delta s_d = (A d)^T h (A d), h physikalisch, Frobenius-orthonormale Basis (15 x 10)."""
        basis, _ = self.sym_basis()
        return np.array([[float(a @ X @ a) for X in basis] for a in self.Ad])

    def eich_basis(self, k_lat):
        """Eckenverschiebung xi (physikalisch) exp(i k.X): u_d ~ sin(k.d/2) (A d).xi."""
        return np.sin(0.5 * (self.dirs @ k_lat))[:, None] * self.Ad


def jacobi_komplex(git):
    """d theta/d s je Simplextyp per komplexem Schritt (Gram-Inverse aus regge_zeit.py), schiefe Laengen."""
    sq0 = git.sq0_typen()
    nEs = len(git.paare)
    J = np.zeros((git.nP, len(git.lok_gelenke), nEs))
    for e in range(nEs):
        sq = sq0.astype(complex)
        sq[:, e] += 1j * RZ.H_KOMPLEX
        c = RZ.kosinus_gram(git, sq)
        J[:, :, e] = -(c.imag / RZ.H_KOMPLEX) / np.sqrt(1.0 - c.real ** 2)
    wdiff = float(np.max(np.abs(np.arccos(RZ.kosinus_gram(git, sq0)) - git.winkel(sq0))))
    return J, wdiff


def maxdiff(a, b):
    keys = set(a) | set(b)
    return float(max(abs(a.get(q, 0.0) - b.get(q, 0.0)) for q in keys))


# ======================================================================= Geometrie
def geometrie(git, mit_flach=True):
    out = {"A": git.A.tolist(), "detA": git.detA}
    sv = np.linalg.svd(git.A3, compute_uv=False)
    out["A_raum_singulaerwerte"] = sv.tolist()
    out["cond_A_raum"] = float(sv[0] / sv[-1])
    out["kantenlaengen_quadrat"] = git.s_dir.tolist()
    sq0 = git.sq0_typen()
    vol = []
    for ip in range(git.nP):
        S = np.zeros((5, 5))
        for k, (i, j) in enumerate(git.paare):
            S[i, j] = S[j, i] = sq0[ip, k]
        G = 0.5 * (S[0, 1:, None] + S[0, None, 1:] - S[1:, 1:])
        vol.append(float(np.sqrt(max(np.linalg.det(G), 0.0)) / 24.0))
    out["simplexvolumen_min_max"] = [min(vol), max(vol)]
    out["simplexvolumen_soll_detA_24"] = git.detA / 24.0
    ang = git.winkel(sq0)
    out["diederwinkel_min_max_grad"] = [float(np.degrees(ang.min())), float(np.degrees(ang.max()))]
    # Dreieckswinkel je Gelenktyp und die 14 Dreiecke an der Hyperdiagonale
    tw = []
    hd = []
    for t in range(git.nH):
        w = [git.A @ x.astype(float) for x in git.g_ecken[t]]
        winkel = []
        for i in range(3):
            u = w[(i + 1) % 3] - w[i]
            v = w[(i + 2) % 3] - w[i]
            winkel.append(float(np.degrees(np.arccos(u @ v / np.sqrt((u @ u) * (v @ v))))))
        tw.extend(winkel)
        dlist = [d for _, d in git.g_kanten[t]]
        if git.top in dlist:
            abl = git.gelenk_ableitung(t)
            a_vec = git.g_ecken[t][1]
            u = w[0] - w[1]
            v = w[2] - w[1]
            hd.append({"typ": int(t), "a": [int(x) for x in a_vec],
                       "cos_winkel_an_a": float(u @ v / np.sqrt((u @ u) * (v @ v))),
                       "winkel_an_a_grad": float(np.degrees(np.arccos(u @ v / np.sqrt((u @ u) * (v @ v))))),
                       "dA_ds_top": float(abl[dlist.index(git.top)])})
    out["dreieckswinkel_min_max_grad"] = [min(tw), max(tw)]
    out["hyperdiagonale_dreiecke"] = hd
    out["hyperdiagonale_rechte_winkel"] = int(sum(abs(x["cos_winkel_an_a"]) < 1e-12 for x in hd))
    if mit_flach:
        out["flach_max_abs_eps"] = float(np.max(np.abs(git.fehlwinkel(git.s0))))
        out["flach_skaliert_1_3"] = float(np.max(np.abs(git.fehlwinkel(1.69 * git.s0))))
    return out


def ableitungen(git, log, name):
    t0 = time.time()
    eT, fehler, betroffen = git.ableitung_T()
    J, _, sq0 = git.jacobi_lokal()
    Jk, wdiff = jacobi_komplex(git)
    dT = RZ.eT_dic(eT)
    out = {"weg_T_fehlerschaetzung": float(max(fehler)), "weg_T_betroffen": betroffen,
           "T_gegen_J": maxdiff(dT, git.eT_aus_J(J)), "T_gegen_K": maxdiff(dT, git.eT_aus_J(Jk)),
           "winkel_gram_gegen_winkel": wdiff, "weg_T_max_abs": float(max(abs(v) for v in dT.values()))}
    schl = 0.0
    for ip in range(git.nP):
        V = []
        for rest, _ in git.lok_gelenke:
            sq = [sq0[ip][git.paare.index((rest[a], rest[b]))] for a, b in itertools.combinations(range(len(rest)), 2)]
            V.append(git.gelenkvolumen(sq))
        schl = max(schl, float(np.max(np.abs(np.array(V) @ Jk[ip]))))
    out["schlaefli_je_simplex_max"] = schl
    protokoll(log, f"{name}: Ableitungen ({time.time() - t0:.1f} s): T-J {out['T_gegen_J']:.1e}, "
                   f"T-K {out['T_gegen_K']:.1e}")
    return eT, out


# ======================================================================= Teil 1
def richtungen_phys():
    R = dict(R4.richtungen(4))
    rng = np.random.default_rng(SAAT_RICHT)
    for i in range(8):
        v = rng.standard_normal(4)
        R[f"zufall_{i}"] = v / np.linalg.norm(v)
    return R


def schur(H, B, C):
    Khh = B.T @ H @ B
    Khw = B.T @ H @ C
    Kww = C.T @ H @ C
    ww, Uw = np.linalg.eigh(Kww)
    keep = np.abs(ww) > PINV_RCOND * np.max(np.abs(ww))
    Kp = (Uw[:, keep] / ww[keep]) @ Uw[:, keep].T
    K = Khh - Khw @ Kp @ Khw.T
    return 0.5 * (K + K.T), ww, int(np.sum(~keep))


def analyse(git, k_lat, k_phys, H, B, Cc, Corth, mit_form):
    lam, V = np.linalg.eigh(H)
    a = np.abs(lam)
    mittel = float(np.mean(a))
    Lam = float(np.max(a))
    null = a < NULL_REL * mittel
    order = np.argsort(a)
    out = {"k_lat": [float(x) for x in k_lat], "k_phys": [float(x) for x in k_phys],
           "betrag_phys": float(np.linalg.norm(k_phys)), "Lambda": Lam, "mittel": mittel,
           "eigenwerte": [float(x) for x in lam], "n_null": int(np.sum(null)),
           "n_pos": int(np.sum((~null) & (lam > 0))), "n_neg": int(np.sum((~null) & (lam < 0))),
           "kleinste_abs_rel_mittel": [float(x) for x in a[order[:8]] / mittel]}
    e_top = np.zeros(git.nE)
    e_top[git.top] = 1.0
    out["top_residuum_rel"] = float(np.linalg.norm(H @ e_top) / Lam)
    if np.linalg.norm(k_lat) > 0:
        G = git.eich_basis(np.asarray(k_lat))
        Qg, _ = np.linalg.qr(G)
        out["eich_residuum_rel"] = float(np.linalg.norm(H @ Qg, 2) / Lam)
        P = np.eye(git.nE) - Qg @ Qg.T
        w, U = np.linalg.eigh(P)
        Qc = U[:, 4:]
        ev = np.linalg.eigvalsh(Qc.T @ H @ Qc)
        out["nicht_eich_eigen_rel_mittel"] = [float(x) for x in np.sort(np.abs(ev))[:6] / mittel]
        out["kleinster_nicht_eich_rel_mittel"] = float(np.min(np.abs(ev)) / mittel)
        nullv = V[:, null]
        if nullv.shape[1] > 0:
            rest = nullv - Qg @ (Qg.T @ nullv)
            out["nullraum_ausserhalb_eich"] = [float(x) for x in np.linalg.svd(rest, compute_uv=False)]
    if not mit_form or np.linalg.norm(k_phys) == 0:
        return out
    kn = float(np.linalg.norm(k_phys))
    nhat = np.asarray(k_phys) / kn
    P2, P1, P0s, P0w, svec, wvec = git.projektoren(nhat)
    for name, C in (("schur", Cc), ("orth", Corth)):
        K, ww, verw = schur(H, B, C)
        f = R4.spin_zerlegung(git, K / git.detA, kn, P2, P1, P0s, P0w, svec, wvec, B, np.asarray(k_phys))
        f["Kww_eigenwerte"] = [float(x) for x in ww]
        f["Kww_verworfen"] = verw
        out["form_" + name] = f
    Kd = B.T @ H @ B
    out["form_direkt"] = R4.spin_zerlegung(git, Kd / git.detA, kn, P2, P1, P0s, P0w, svec, wvec, B,
                                           np.asarray(k_phys))
    return out


def teil1_matrix(A, name, log, mit_bz):
    t0 = time.time()
    git = GitterSchief(A)
    res = {"name": name, "geometrie": geometrie(git, mit_flach=True)}
    protokoll(log, f"{name}: Geometrie, flach {res['geometrie']['flach_max_abs_eps']:.1e}, "
                   f"rechte Winkel an der Hyperdiagonale {res['geometrie']['hyperdiagonale_rechte_winkel']}/14")
    eT, abl = ableitungen(git, log, name)
    res["ableitungen"] = abl
    B = git.B0()
    res["rang_B"] = int(np.linalg.matrix_rank(B))
    Cc, rang14 = R4.komplement(git, B)
    res["rang_B_ohne_top"] = rang14
    U, sv, _ = np.linalg.svd(B, full_matrices=True)
    Corth = U[:, 10:]
    # k = 0
    _, Em0, M0 = git.matrizen(np.zeros((1, 4)), eT)
    H0 = R4.h_von_M(M0)[0][0]
    lam0, V0 = np.linalg.eigh(H0)
    a0 = np.abs(lam0)
    m0 = float(np.mean(a0))
    order = np.argsort(a0)
    Qb, _ = np.linalg.qr(B)
    nullv = V0[:, a0 < NULL_REL * m0]
    rest0 = nullv - Qb @ (Qb.T @ nullv)
    v11 = V0[:, order[10]]
    res["k0"] = {"eigenwerte": [float(x) for x in lam0], "mittel": m0, "Lambda": float(a0.max()),
                 "n_null": int(np.sum(a0 < NULL_REL * m0)),
                 "kleinste_abs_rel_mittel": [float(x) for x in a0[order[:14]] / m0],
                 "elfter_eigenwert": float(lam0[order[10]]), "elfter_top_anteil": float(abs(v11[git.top])),
                 "affin_residuum_rel": float(np.linalg.norm(H0 @ Qb, 2) / a0.max()),
                 "top_residuum_rel": float(np.linalg.norm(H0 @ np.eye(git.nE)[git.top]) / a0.max()),
                 "nullraum_ausserhalb_affin": [float(x) for x in np.linalg.svd(rest0, compute_uv=False)]
                 if nullv.shape[1] else [],
                 "schlaefli_global": float(np.max(np.abs(
                     np.array([git.gelenkvolumen([float(git.s_dir[d]) for _, d in git.g_kanten[t]])
                               for t in range(git.nH)]) @ Em0[0].real)))}
    # allgemeine k: 64 Zufallsimpulse (Gitter), Hermitezitaet
    rng = np.random.default_rng(SAAT_K)
    ks_z = rng.uniform(-np.pi, np.pi, size=(64, 4))
    _, _, Mz = git.matrizen(ks_z, eT)
    herm_z = np.max(np.abs(Mz - np.conj(np.swapaxes(Mz, 1, 2))), axis=(1, 2)) / np.max(np.abs(Mz), axis=(1, 2))
    Hz, imag_z = R4.h_von_M(Mz)
    Ainv_T = np.linalg.inv(git.A).T
    res["zufall"] = [analyse(git, k, Ainv_T @ k, H, B, Cc, Corth, False) for k, H in zip(ks_z, Hz)]
    # Leiter in physikalischen Richtungen
    R = richtungen_phys()
    punkte = []
    for rn, nh in R.items():
        for b in BETRAEGE:
            kp = b * nh
            punkte.append((rn, b, git.A.T @ kp, kp))
    ks = np.array([p[2] for p in punkte])
    _, _, Mk = git.matrizen(ks, eT)
    herm_k = np.max(np.abs(Mk - np.conj(np.swapaxes(Mk, 1, 2))), axis=(1, 2)) / np.max(np.abs(Mk), axis=(1, 2))
    Hk, imag_k = R4.h_von_M(Mk)
    leiter = []
    for (rn, b, kl, kp), H in zip(punkte, Hk):
        a = analyse(git, kl, kp, H, B, Cc, Corth, True)
        a["richtung"] = rn
        a["betrag_nominal"] = b
        leiter.append(a)
    res["leiter"] = leiter
    res["hermitesch_max_rel"] = float(max(np.max(herm_z), np.max(herm_k)))
    res["imag_max_rel"] = float(max(imag_z, imag_k))
    protokoll(log, f"{name}: Leiter fertig ({time.time() - t0:.1f} s)")
    if mit_bz:
        qs = 2 * np.pi * np.array(list(itertools.product(range(8), repeat=4)), float) / 8
        qs = np.where(qs > np.pi, qs - 2 * np.pi, qs)
        zaehl = {}
        kleinst = 1e300
        for st in range(0, len(qs), 512):
            _, _, Mb = git.matrizen(qs[st:st + 512], eT)
            lb = np.linalg.eigvalsh(R4.h_von_M(Mb)[0])
            for q, l_ in zip(qs[st:st + 512], lb):
                m_ = np.mean(np.abs(l_))
                nn = int(np.sum(np.abs(l_) < NULL_REL * m_))
                key = f"{nn}/{int(np.sum(l_ >= NULL_REL * m_))}/{int(np.sum(l_ <= -NULL_REL * m_))}"
                zaehl[key] = zaehl.get(key, 0) + 1
                if np.linalg.norm(q) > 0:
                    kleinst = min(kleinst, float(np.sort(np.abs(l_))[4] / m_))
        res["bz_zaehlung_null_pos_neg"] = zaehl
        res["bz_kleinster_fuenfter_rel_mittel"] = kleinst
        protokoll(log, f"{name}: BZ {zaehl} ({time.time() - t0:.1f} s)")
    return res


def kurve(log):
    """Kleinste Eigenwerte gegen s (beschreibend, fuer das Bild)."""
    out = []
    rng = np.random.default_rng(SAAT_K)
    ks_z = rng.uniform(-np.pi, np.pi, size=(64, 4))
    for s in S_KURVE:
        t0 = time.time()
        git = GitterSchief(matrix_A(s))
        eT, fehler, _ = git.ableitung_T()
        _, _, M0 = git.matrizen(np.zeros((1, 4)), eT)
        l0, V0 = np.linalg.eigh(R4.h_von_M(M0)[0][0])
        a0 = np.abs(l0)
        o = np.argsort(a0)
        _, _, Mz = git.matrizen(ks_z, eT)
        lz = np.linalg.eigvalsh(R4.h_von_M(Mz)[0])
        az = np.abs(lz)
        mz = np.mean(az, axis=1)
        fuenf = np.sort(az, axis=1)[:, 4] / mz
        nh = R4.richtungen(4)["allg_1234"]
        kp = 0.1 * nh
        _, _, Mp = git.matrizen((git.A.T @ kp)[None, :], eT)
        lp = np.linalg.eigvalsh(R4.h_von_M(Mp)[0][0])
        ap = np.abs(lp)
        out.append({"s": s, "k0_kleinste_abs_rel_mittel": [float(x) for x in a0[o[:13]] / np.mean(a0)],
                    "k0_elfter_signiert": float(l0[o[10]]), "k0_elfter_top_anteil": float(abs(V0[git.top, o[10]])),
                    "zufall_fuenfter_rel_mittel_min": float(fuenf.min()),
                    "zufall_fuenfter_rel_mittel_median": float(np.median(fuenf)),
                    "zufall_n_neg": sorted(set(int(np.sum(l_ <= -NULL_REL * m_)) for l_, m_ in zip(lz, mz))),
                    "punkt_1234_0p1_kleinste_rel_mittel": [float(x) for x in np.sort(ap)[:8] / np.mean(ap)],
                    "weg_T_fehler": float(max(fehler))})
        protokoll(log, f"Kurve s={s}: k0 11. {out[-1]['k0_kleinste_abs_rel_mittel'][10]:.3e} "
                       f"({time.time() - t0:.1f} s)")
    return out


# ======================================================================= Teil 2: ruhende Masse
def nullbasis(git, ks, mit_top):
    G = np.sin(0.5 * ks @ git.dirs.T)[:, :, None] * git.Ad[None, :, :]
    if mit_top:
        et = np.zeros((len(ks), git.nE, 1))
        et[:, git.top, 0] = 1.0
        G = np.concatenate([G, et], axis=2)
    sv = np.linalg.svd(G, compute_uv=False)
    Qn, _ = np.linalg.qr(G)
    return Qn, sv[:, -1] / sv[:, 0]


def spektrum(git, eT, ks, mit_top, mit_kontrollen=False):
    Am, Em, M = git.matrizen(ks, eT)
    Mr = 0.5 * (M.real + np.swapaxes(M.real, 1, 2))
    s = np.zeros(git.nE)
    s[git.tau_index] = QUELLE
    Qn, svmin = nullbasis(git, ks, mit_top)
    P = np.eye(git.nE)[None] - np.einsum("kai,kbi->kab", Qn, Qn)
    w, V = np.linalg.eigh(P)
    nn = Qn.shape[2]
    Qc = V[:, :, nn:]
    Mc = np.einsum("kai,kab,kbj->kij", Qc, Mr, Qc)
    sc = np.einsum("kai,a->ki", Qc, s)
    yc = np.linalg.solve(Mc, sc[:, :, None])[:, :, 0]
    u0 = np.einsum("kai,ki->ka", Qc, yc)
    u = u0
    phase = np.exp(1j * ks @ git.g_mitte.T)
    eps = np.einsum("kta,ka->kt", Em, u0)
    if mit_top:
        eps, c = RZ.projiziere(Em[:, :, git.top], eps)
        u = u0.astype(complex)
        u[:, git.top] = c
    out = {"u": u, "eps": eps, "F": phase * eps}
    if mit_kontrollen:
        lam = np.linalg.eigvalsh(Mr)
        al = np.abs(lam)
        Lam = np.max(al, axis=1)
        mit = np.mean(al, axis=1)
        nnull = np.sum(al < NULL_REL * mit[:, None], axis=1)
        evc = np.abs(np.linalg.eigvalsh(Mc))
        proj = np.linalg.norm(np.einsum("kai,a->ki", Qn, s), axis=1) / np.linalg.norm(s)
        res = np.linalg.norm(np.einsum("kab,kb->ka", Mr, u0) - s[None], axis=1) / np.linalg.norm(s)
        nullres = np.linalg.norm(np.einsum("kab,kbi->kai", Mr, Qn), axis=(1, 2)) / Lam
        G = np.sin(0.5 * ks @ git.dirs.T)[:, :, None] * git.Ad[None, :, :]
        eich_eps = np.linalg.norm(np.einsum("kta,kai->kti", Em, G), axis=(1, 2)) / (
            np.linalg.norm(Em, axis=(1, 2)) * np.linalg.norm(G, axis=(1, 2)))
        out["kontrollen"] = {
            "n_null_min": int(nnull.min()), "n_null_max": int(nnull.max()),
            "kleinster_nicht_null_rel_mittel_min": float(np.min(np.min(evc, axis=1) / mit)),
            "quelle_auf_nullraum_rel_max": float(np.max(proj)),
            "residuum_gleichung_rel_max": float(np.max(res)),
            "nullraum_residuum_rel_max": float(np.max(nullres)),
            "nullbasis_min_singulaer_rel": float(np.min(svmin)),
            "M_imag_rel_max": float(np.max(np.abs(M.imag)) / np.max(np.abs(M.real))),
            "eps_eichmoden_rel_max": float(np.max(eich_eps)),
            "E_top_norm_min": float(np.min(np.linalg.norm(Em[:, :, git.top], axis=1)))}
    return out


def loese_torus(git, eT, L, mit_top, log):
    f = np.fft.fftfreq(L) * 2.0 * np.pi
    g = np.meshgrid(f, f, f, indexing="ij")
    ksp = np.stack([x.ravel() for x in g], 1)
    ks = np.column_stack([np.zeros(len(ksp)), ksp])
    Nk = len(ks)
    F = np.zeros((Nk, git.nH), complex)
    kon = []
    t0 = time.time()
    for a in range(1, Nk, BATCH):
        b = min(a + BATCH, Nk)
        sp = spektrum(git, eT, ks[a:b], mit_top, mit_kontrollen=True)
        F[a:b] = sp["F"]
        kon.append(sp["kontrollen"])
    kont = {}
    for key in kon[0]:
        vals = [c[key] for c in kon]
        kont[key] = float(min(vals)) if (key.endswith("_min") or "min_" in key) else float(max(vals))
    kont["n_null_min"] = int(min(c["n_null_min"] for c in kon))
    kont["n_null_max"] = int(max(c["n_null_max"] for c in kon))
    eps = np.empty((git.nH, L, L, L))
    imag_max = 0.0
    for t in range(git.nH):
        z = np.fft.ifftn(F[:, t].reshape(L, L, L))
        eps[t] = z.real
        imag_max = max(imag_max, float(np.max(np.abs(z.imag))))
    kont["eps_imag_max"] = imag_max
    kont["eps_real_max"] = float(np.max(np.abs(eps)))
    protokoll(log, f"L={L}: {Nk} k-Punkte geloest ({time.time() - t0:.1f} s), Nullmoden {kont['n_null_min']}"
                   f"..{kont['n_null_max']}")
    return eps, kont


def hintergrund(git, eT, mit_top):
    """Mittel von F ueber k_phys = +-kappa e_i (physikalische Raumachsen), Richardson in kappa."""
    werte = []
    for kap in KAPPA:
        ks = []
        for i in range(1, 4):
            for sg in (1.0, -1.0):
                kp = np.zeros(4)
                kp[i] = sg * kap
                ks.append(git.A.T @ kp)
        sp = spektrum(git, eT, np.array(ks), mit_top)
        werte.append(np.mean(sp["F"], axis=0).real)
    return (4.0 * werte[1] - werte[0]) / 3.0, float(np.max(np.abs(werte[1] - werte[0])))


def hd_gitter(Hd, A):
    """Hd in Gitterkoordinaten: h_lat(X) = A^T h(A X) A."""
    return np.einsum("mi,nj,mnab,ak,bl->ijkl", A, A, Hd, A, A)


class Kalibrierung:
    def __init__(self, git, eT, B, mit_top):
        self.git, self.eT, self.mit_top = git, eT, mit_top
        Am, Em, M = git.matrizen(np.zeros((1, 4)), eT)
        self.A0, self.E0 = Am[0].real, Em[0].real
        self.M0 = 0.5 * (M[0].real + M[0].real.T)
        C, _ = R4.komplement(git, B)
        self.Cs = C[:, 1:] if mit_top else C
        self.Kss = self.Cs.T @ self.M0 @ self.Cs

    def kinematisch(self, Hd, p0=None):
        return RZ.eps_kinematisch(self.git, self.eT, hd_gitter(Hd, self.git.A), p0)

    def antwort(self, Hd, versklavt=True):
        e = self.kinematisch(Hd)
        if versklavt:
            r = self.A0.T @ e
            w = -np.linalg.solve(self.Kss, self.Cs.T @ r)
            e = e + self.E0 @ (self.Cs @ w)
        if self.mit_top:
            e = RZ.projiziere(self.E0[:, self.git.top], e)[0]
        return e

    def basis(self, versklavt=True):
        out = {}
        for teil in ("N", "S"):
            cols = []
            for (a, b) in [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]:
                phi = np.zeros((3, 3))
                phi[a, b] = phi[b, a] = 1.0
                cols.append(self.antwort(RZ.hd_statisch(phi, teil), versklavt))
            out[teil] = np.array(cols).T
        return out


def bild_offsets(A3):
    smin = np.linalg.svd(A3, compute_uv=False)[-1]
    N = int(np.ceil(R_BILD / smin)) + 1
    r = np.arange(-N, N + 1)
    nn = np.array(list(itertools.product(r, r, r)), float)
    ph = nn @ A3.T
    m = (np.linalg.norm(ph, axis=1) <= R_BILD) & np.any(nn != 0, axis=1)
    return ph[m]


def phi_bilder(cen, L, offs):
    out = np.zeros((len(cen), 3, 3))
    for i, c in enumerate(cen):
        out[i] = np.sum(RZ.phi_punkt(c[None, :] + L * offs), axis=0)
    return out


def quadrate(git, eps, L, ebene, basen, bg, resp, resp_kin, offs):
    mu, nu = ebene
    t1, t2 = RZ.typ(git, mu, nu)
    basen = np.array(basen, dtype=np.int64)
    off = np.zeros(3)
    for a in (mu, nu):
        if a != TAU:
            off[a - 1] += 0.5
    cen = (basen + off[None, :]) @ git.A3.T
    roh = np.array([0.5 * (eps[t1][tuple(np.mod(p, L))] + eps[t2][tuple(np.mod(p, L))]) for p in basen])
    hg = 0.5 * (bg[t1] + bg[t2]) / L ** 3 * np.ones(len(basen))
    rN = 0.5 * (resp["N"][t1] + resp["N"][t2])
    rS = 0.5 * (resp["S"][t1] + resp["S"][t2])
    kN = 0.5 * (resp_kin["N"][t1] + resp_kin["N"][t2])
    kS = 0.5 * (resp_kin["S"][t1] + resp_kin["S"][t2])
    pv = RZ.phi_vektor(RZ.phi_punkt(cen))
    bv = RZ.phi_vektor(phi_bilder(cen, L, offs))
    return {"ebene": [int(mu), int(nu)], "zentren_phys": cen.tolist(), "r": np.linalg.norm(cen, axis=1).tolist(),
            "roh": roh.tolist(), "hintergrund": hg.tolist(), "bild": (bv @ (rN + rS)).tolist(),
            "PN": (pv @ rN).tolist(), "PS": (pv @ rS).tolist(), "PN_kin": (pv @ kN).tolist(),
            "PS_kin": (pv @ kS).tolist()}


def zwei_mal_zwei(a, b, kin=False):
    kN, kS = ("PN_kin", "PS_kin") if kin else ("PN", "PS")
    Mm = np.array([[a[kN], a[kS]], [b[kN], b[kS]]])
    al, be = np.linalg.solve(Mm, np.array([a["korr"], b["korr"]]))
    Mn = Mm / np.linalg.norm(Mm, axis=1)[:, None]
    return float(al), float(be), float(np.linalg.cond(Mm)), float(np.linalg.cond(Mn))


def auswertung_achse(git, eps, L, bg, resp, resp_kin, offs, a):
    b, c = [q for q in (1, 2, 3) if q != a]
    E3 = np.eye(3, dtype=np.int64)
    ea, eb, ec = E3[a - 1], E3[b - 1], E3[c - 1]
    laenge = float(np.linalg.norm(git.A3[:, a - 1]))
    pts = []
    for x0 in range(1, L // 2):
        qa = quadrate(git, eps, L, (TAU, a), [(x0 - 1) * ea, x0 * ea], bg, resp, resp_kin, offs)
        qb = quadrate(git, eps, L, (b, c), [x0 * ea, x0 * ea - eb, x0 * ea - ec, x0 * ea - eb - ec], bg, resp,
                      resp_kin, offs)
        ma, mb = RZ.mittel(qa), RZ.mittel(qb)
        al, be, cond, cond_n = zwei_mal_zwei(ma, mb)
        alk, bek, _, cond_nk = zwei_mal_zwei(ma, mb, kin=True)
        pts.append({"x0": x0, "r": x0 * laenge, "zeit_quadrate": ma, "quer_quadrate": mb, "alpha": al, "beta": be,
                    "gamma": be / al, "kondition": cond, "kondition_zeilennorm": cond_n,
                    "verhaeltnis_naiv": ma["korr"] / mb["korr"], "gamma_kin": bek / alk, "alpha_kin": alk,
                    "kondition_zeilennorm_kin": cond_nk})
    return {"achse": a, "laenge_A_e": laenge, "richtung_phys": (git.A3[:, a - 1] / laenge).tolist(), "punkte": pts}


def teil2(ziel, s_arg, Ls, log):
    t0 = time.time()
    if s_arg == "rot":
        A = matrix_A(A3=drehung_test())
        s = None
        mit_top = True
    else:
        s = float(s_arg)
        A = matrix_A(s)
        mit_top = (s == 0.0)
    git = GitterSchief(A)
    res = {"skript_sha256": SKRIPT_SHA, "numpy": np.__version__, "s": s_arg, "Ls": Ls, "mit_top_fixierung": mit_top,
           "zeit_utc_start": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    res["geometrie"] = geometrie(git, mit_flach=True)
    eT, abl = ableitungen(git, log, f"teil2 s={s_arg}")
    res["ableitungen"] = abl
    B = git.B0()
    res["typen"] = {k: list(map(int, RZ.typ(git, *v))) for k, v in
                    {"tx": (0, 1), "yz": (2, 3), "ty": (0, 2), "xz": (1, 3), "tz": (0, 3), "xy": (1, 2)}.items()}
    kal = Kalibrierung(git, eT, B, mit_top)
    resp = kal.basis(True)
    resp_kin = kal.basis(False)
    rng = np.random.default_rng(20261004)
    kk = {}
    for teil in ("N", "S"):
        M_ = rng.standard_normal((3, 3))
        phi = M_ + M_.T
        Hd = RZ.hd_statisch(phi, teil)
        R = RZ.riemann(Hd)
        e_stat = kal.kinematisch(Hd)
        e_rnc = kal.kinematisch(RZ.hd_rnc(R))
        e_versch = kal.kinematisch(Hd, p0=np.array([2, 3, -2, 1]))
        ev = kal.antwort(Hd, True)
        ek = kal.antwort(Hd, False)
        kk[teil] = {"rnc_gegen_statisch_rel": float(np.max(np.abs(e_rnc - e_stat)) / np.max(np.abs(e_stat))),
                    "verschiebung_rel": float(np.max(np.abs(e_versch - e_stat)) / np.max(np.abs(e_stat))),
                    "versklavung_rel": float(np.max(np.abs(ev - ek)) / np.max(np.abs(ek)))}
    ksw = np.linalg.eigvalsh(kal.Kss)
    res["kalibrierung"] = {"kontrollen": kk, "Kss_eigen": ksw.tolist(),
                           "Kss_kondition": float(np.max(np.abs(ksw)) / np.min(np.abs(ksw))),
                           "resp_N": resp["N"].tolist(), "resp_S": resp["S"].tolist(),
                           "resp_kin_N": resp_kin["N"].tolist(), "resp_kin_S": resp_kin["S"].tolist()}
    # Antwort der Quadrate auf die Achsenkruemmung (Einheit 2 G M / r^3) je physikalischer Achse
    ant = {}
    for a in (1, 2, 3):
        n = git.A3[:, a - 1] / np.linalg.norm(git.A3[:, a - 1])
        phi_ax = -(3.0 * np.outer(n, n) - np.eye(3)) / 2.0
        b, c = [q for q in (1, 2, 3) if q != a]
        ta, bc = RZ.typ(git, 0, a), RZ.typ(git, b, c)
        for teil in ("N", "S"):
            for nm, rr in (("versklavt", resp), ("kinematisch", resp_kin)):
                v = rr[teil] @ RZ.phi_vektor(phi_ax)
                ant[f"achse{a}_{teil}_{nm}"] = {"zeit": [float(v[ta[0]]), float(v[ta[1]])],
                                                "quer": [float(v[bc[0]]), float(v[bc[1]])]}
    res["kalibrierung"]["antwort_achse_einheit"] = ant
    protokoll(log, f"Kalibrierung ({time.time() - t0:.1f} s): {json.dumps(kk)}; Kss {ksw.round(5).tolist()}")
    bg, bgd = hintergrund(git, eT, mit_top)
    res["hintergrund"] = {"F0_mittel": bg.tolist(), "kappa_diff_max": bgd}
    offs = bild_offsets(git.A3)
    res["bild_zahl"] = int(len(offs))
    protokoll(log, f"Hintergrund max|F0| {np.max(np.abs(bg)):.4g}, kappa-Diff {bgd:.2e}; Bilder {len(offs)}")
    res["laeufe"] = []
    for L in Ls:
        eps, kont = loese_torus(git, eT, L, mit_top, log)
        aus = {"L": L, "kontrollen": kont}
        for a in (1, 2, 3):
            aus[f"achse_{a}"] = auswertung_achse(git, eps, L, bg, resp, resp_kin, offs, a)
        res["laeufe"].append(aus)
        g = [(p["x0"], round(p["r"], 3), round(p["gamma"], 4)) for p in aus["achse_1"]["punkte"] if 5 <= p["x0"] <= 7]
        protokoll(log, f"L={L}: Kontrollen {json.dumps(kont)} ({time.time() - t0:.1f} s); Achse 1 x0 5..7 "
                       f"{'(gesehen)' if s_arg in ('0', '0.0', 'rot') else '(nicht ausgegeben)'} "
                       f"{g if s_arg in ('0', '0.0', 'rot') else ''}")
        with open(ziel + ".teil", "w") as f_:
            json.dump(res, f_)
    res["laufzeit_s"] = time.time() - t0
    return res


# ======================================================================= Hauptprogramm
def main():
    modus, ziel = sys.argv[1], sys.argv[2]
    t0 = time.time()
    log = []
    out = {"skript_sha256": SKRIPT_SHA, "numpy": np.__version__, "modus": modus, "argv": sys.argv[1:],
           "zeit_utc_start": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    if modus == "rauch0":
        B = matrix_B()
        out["B"] = B.tolist()
        out["B_offdiag_summe_sym"] = float(np.sum(B + B.T) - 2 * np.trace(B))
        out["geometrie"] = {}
        for s in (0.0, 0.1, 0.2):
            git = GitterSchief(matrix_A(s))
            out["geometrie"][str(s)] = geometrie(git, mit_flach=False)
    elif modus == "teil1":
        sl = [float(x) for x in sys.argv[3].split(",")]
        extra = sys.argv[4:]
        out["s_liste"] = sl
        out["B"] = matrix_B().tolist()
        out["laeufe"] = [teil1_matrix(matrix_A(s), f"s={s}", log, "bz" in extra) for s in sl]
        if "test" in extra:
            out["test_drehung"] = teil1_matrix(matrix_A(A3=drehung_test()), "test_drehung", log, False)
            out["test_diagonal"] = teil1_matrix(matrix_A(A3=diagonal_test()), "test_diagonal", log, False)
        if "kurve" in extra:
            out["kurve"] = kurve(log)
    elif modus == "teil2":
        Ls = [int(x) for x in sys.argv[4].split(",")]
        out.update(teil2(ziel, sys.argv[3], Ls, log))
    out["laufzeit_s"] = time.time() - t0
    out["protokoll"] = log
    with open(ziel, "w") as f:
        json.dump(out, f, indent=1)
    print("geschrieben", ziel, f"{time.time() - t0:.1f} s", flush=True)


if __name__ == "__main__":
    main()
