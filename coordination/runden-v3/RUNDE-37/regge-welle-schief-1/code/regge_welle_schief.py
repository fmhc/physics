#!/usr/bin/env python3
"""REGGE-WELLE-SCHIEF-1 (Runde 37, Code-Agent): Wellenmessung aus REGGE-WELLE-1 auf dem schiefen Netz aus
REGGE-4D-SCHIEF-1 (X -> A X, A = diag(1, 1 + s B), B aus Saat 20261004), s = 0; 0,1; 0,2.

Unveraendert importiert: regge4d.py (REGGE-4D-1), regge_zeit.py (REGGE-ZEIT-1), regge_schief.py (REGGE-4D-SCHIEF-1),
regge_welle.py (REGGE-WELLE-1).

  Physikalisch: x = A X; ebene Welle exp(i k_lat.X) = exp(i k_phys.x), also k_lat = A^T k_phys. A e_0 = e_0 (Zeitkante
  Laenge 1, senkrecht zum Raum), daher k_tau,lat = k_tau,phys = i omega; omega in physikalischen Einheiten.
  v = Re omega / |k_phys|.
  Nullraum: s = 0 wie REGGE-WELLE-1 (4 Gitter-Eichmoden + e_top, Komplement 10-dim., identischer Rechenweg);
  s != 0 nur die 4 Eichmoden (die Hyperdiagonale ist dort keine Nullmode), Komplement 11-dim.
  Je Punkt (Richtung n physikalisch, Betrag |k_phys|): Nullstellen in R (PEP + Aberth, wie REGGE-WELLE-1), Windung auf
  dem Rand von R, reelle Achse, Kern je Nullstelle (TT eichinvariant, Lapse/Shift, Diagonalanteil, Gitterrest),
  Zensus aller Wurzeln mit -1e-6 <= Re omega <= 2,4 und |Im omega| <= pi (Aberth, Pruefwerte), euklidische Linie
  k = (kappa, k_lat), kappa in [-pi, pi] (Signatur von H), Kinetik-Matrix, Wuerfelgitter-Formel.

Aufruf: python regge_welle_schief.py <modus: rauch | haupt> <s> <ausgabe.json>
"""
import hashlib
import json
import os
import sys
import time

import numpy as np
from scipy.optimize import minimize_scalar

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import regge4d as R4  # noqa: E402
import regge_welle as RW  # noqa: E402
import regge_schief as RS  # noqa: E402


def sha(name):
    return hashlib.sha256(open(os.path.join(HIER, name), "rb").read()).hexdigest()


SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
SHAS = {n: sha(n) for n in ("regge4d.py", "regge_zeit.py", "regge_schief.py", "regge_welle.py")}

TAU, SP = 0, [1, 2, 3]
BETRAEGE = [0.05, 0.1, 0.2, 0.4, 0.8]          # Karte
RAUCH_BETRAEGE = [0.3, 0.6]                     # Rauchlauf: nicht geurteilte Betraege
RAUCH_RICHTUNGEN = ("x+", "xyz+", "fib05")
ZENSUS_RE_MIN, ZENSUS_RE_MAX, ZENSUS_IM_MAX = -1e-6, 2.4, np.pi + 1e-3   # PLAN [F6]; +1e-3: beide Kopien
#                                                     omega, omega -+ 2 pi i am Rand sicher erfassen (Paarung in der Auswertung)
N_EUKL = 257                                    # euklidische Linie kappa in [-pi, pi] (PLAN [F7])
NULL_REL = RS.NULL_REL                          # 1e-6 * Mittel (REGGE-4D-SCHIEF-1 [F2])
EIGEN_R = ("x+", "xy+", "x-y", "xyz+", "123", "fib05")


def protokoll(log, s):
    print(s, flush=True)
    log.append(s)


def nullbasis_s(git, ktau, ks, mit_top):
    """Gitter-Eichmoden sin(k.d/2) d_mu (Spann gleich dem von sin(k.d/2) (A d)_mu, A invertierbar), bei s = 0 dazu
    e_top. Identisch mit regge_welle.nullbasis fuer mit_top = True."""
    N = RW.nullbasis(git, ktau, ks)
    return N if mit_top else N[:, :, :4]


def newton_einzeln(Fm, w0, kb, maxit=80):
    """Gedaempftes Newton auf det F (Schritt 1/(d log det/d omega)), je Wurzel einzeln; Schritt hoechstens
    0,05 max(abs(k), abs(omega)); Abbruch bei singulaerem F (Wurzel getroffen) oder nicht endlichem Schritt."""
    w = complex(w0)
    it = 0
    for it in range(maxit):
        try:
            L = RW.logabl(Fm, np.array([w]))[0]
        except np.linalg.LinAlgError:
            break
        if not np.isfinite(L) or L == 0:
            break
        st = 1.0 / L
        grenze = 0.05 * max(kb, abs(w))
        if abs(st) > grenze:
            st = st * (grenze / abs(st))
        w = w - st
        if abs(st) < 1e-14 * max(1.0, abs(w)):
            break
    return w, it + 1


def kern_info(git, Fm, Q0, Qn0, B, basis, Ckomp, QT, nhat, ks, mit_top, w):
    """Kern von F an der Nullstelle w: Physikalitaet, Regularitaet, Polarisationsanteile (PLAN Abschnitt 4)."""
    zw = np.exp(-0.5 * w)
    Fw = RW.laurent(Fm, zw)[0]
    _, svw, Vh = np.linalg.svd(Fw)
    v = np.conj(Vh[-1])
    u = Q0 @ v
    Nw = nullbasis_s(git, [1j * w], ks, mit_top)[0]
    Qn, _ = np.linalg.qr(Nw)
    wmin = u - Qn @ (np.conj(Qn).T @ u)
    phys = float(np.linalg.norm(wmin) / np.linalg.norm(u))
    tt, wv = RW.tt_klasse(u, Nw, QT)
    hv, *_ = np.linalg.lstsq(B.astype(complex), wv, rcond=None)
    gitter_rest = float(np.linalg.norm(wv - B @ hv) / np.linalg.norm(wv))
    _, zeitanteil = RW.tt_anteil(RW.h_tensor(basis, hv), nhat)
    BC = np.column_stack([B, Ckomp]).astype(complex)
    X = np.linalg.solve(BC, wv)
    nw = np.linalg.norm(wv)
    diag = float(abs(X[10]) / nw)
    c4 = float(np.linalg.norm(Ckomp[:, 1:] @ X[11:]) / nw)
    Xm = np.linalg.solve(BC, wmin)
    nm_ = max(np.linalg.norm(wmin), 1e-300)
    diag_min = float(abs(Xm[10]) / nm_)
    hm, *_ = np.linalg.lstsq(B.astype(complex), wmin, rcond=None)
    _, zeit_min = RW.tt_anteil(RW.h_tensor(basis, hm), nhat)
    tt_min = float(np.linalg.norm(QT.T @ wmin) / nm_)
    v2 = np.conj(Vh[-2])
    tt2, _ = RW.tt_klasse(Q0 @ v2, Nw, QT)
    return {"re": float(w.real), "im": float(w.imag), "s2_rel": float(svw[-2] / svw[0]),
            "rho": float(RW.rho(Qn0, Nw[None])[0]), "physikalisch": phys, "tt_anteil": tt,
            "zeit_anteil": zeitanteil, "gitter_rest": gitter_rest, "diag_anteil": diag, "c4_anteil": c4,
            "tt_anteil_2": tt2, "min_vertreter": {"tt": tt_min, "zeit": zeit_min, "diag": diag_min}}


def analyse_s(git, form, eT, B, basis, Ckomp, nm, nhat, kb, mit_top, mit_eigen=False, mit_extra=True):
    t0 = time.time()
    kp = kb * nhat                      # physikalisches k (raeumlich)
    ks = git.A3.T @ kp                  # Gitter-k (raeumlich), k_lat = A^T k_phys
    C = form.koeffizienten(ks)
    N0 = nullbasis_s(git, [0.0], ks, mit_top)[0].real
    nn = N0.shape[1]
    U, sv0, _ = np.linalg.svd(N0, full_matrices=True)
    Qn0, Q0 = U[:, :nn], U[:, nn:]
    Fm = {m: Q0.T @ Cm @ Q0 for m, Cm in C.items()}
    out = {"richtung": nm, "n": nhat.tolist(), "betrag": kb, "k_phys": kp.tolist(), "k_gitter": ks.tolist(),
           "betrag_gitter": float(np.linalg.norm(ks)), "null_dim": int(nn), "N0_sing_rel_min": float(sv0[-1] / sv0[0])}
    # --- reelle Achse (wie REGGE-WELLE-1)
    om = RW.R_RE * kb * np.arange(1, RW.N_ACHSE + 1) / RW.N_ACHSE
    z = np.exp(-0.5 * om)
    M = RW.laurent(C, z)
    F = np.einsum("ai,kab,bj->kij", Q0, M, Q0)
    svF = np.linalg.svd(F, compute_uv=False)
    s = svF[:, -1] / svF[:, 0]
    s2 = svF[:, -2] / svF[:, 0]
    Nn = nullbasis_s(git, 1j * om, ks, mit_top)
    MN = np.einsum("kab,kbj->kaj", M, Nn)
    normM = np.linalg.norm(M, 2, axis=(1, 2))
    res = np.max(np.linalg.norm(MN, axis=1) / np.linalg.norm(Nn, axis=1), axis=1) / normM
    sym = np.max(np.abs(M - np.swapaxes(M, 1, 2)), axis=(1, 2)) / np.max(np.abs(M), axis=(1, 2))
    Fneg = np.einsum("ai,kab,bj->kij", Q0, RW.laurent(C, np.exp(0.5 * om)), Q0)
    zeitumkehr = np.linalg.norm(Fneg - np.conj(F), axis=(1, 2)) / np.linalg.norm(F, axis=(1, 2))
    rho_achse = RW.rho(Qn0, Nn)
    lokmin = [int(i) for i in range(1, len(s) - 1) if s[i] < s[i - 1] and s[i] <= s[i + 1]]
    sgn_d, _ = np.linalg.slogdet(F)
    etop = np.zeros(git.nE)
    etop[git.top] = 1.0
    out["achse"] = {"omega": om[4::5].tolist(), "s": s[4::5].tolist(), "s2": s2[4::5].tolist(),
                    "phase_det": np.angle(sgn_d[4::5]).tolist(),
                    "imag_F_rel_max": float(np.max(np.abs(F.imag)) / np.max(np.abs(F))),
                    "lokale_minima": [{"omega": float(om[i]), "s": float(s[i])} for i in lokmin],
                    "null_residuum_max": float(np.max(res)), "symmetrie_max": float(np.max(sym)),
                    "zeitumkehr_max": float(np.max(zeitumkehr)), "rho_min": float(np.min(rho_achse)),
                    "etop_residuum_rel_min": float(np.min(np.linalg.norm(M @ etop, axis=1) / normM))}
    fein = []
    for i in lokmin:
        a, b = om[max(i - 1, 0)], om[min(i + 1, len(om) - 1)]
        r = minimize_scalar(lambda x: float(RW.s_wert(Fm, np.array([x]))[0][0]), bounds=(a, b), method="bounded",
                            options={"xatol": 1e-13 * kb})
        fein.append({"omega": float(r.x), "s": float(r.fun)})
    out["achse"]["minima_fein"] = fein
    # --- Nullstellen in R (PEP + Aberth in R', wie REGGE-WELLE-1)
    wurz, pep_info = RW.pep_wurzeln(Fm)
    out["pep"] = pep_info
    inR2 = (wurz.real >= -0.2 * kb) & (wurz.real <= 1.2 * RW.R_RE * kb) & (np.abs(wurz.imag) <= 1.2 * RW.R_IM * kb)
    kand = wurz[inR2]
    if len(kand):
        verf, nit, letzter = RW.aberth(Fm, kand, kb)
    else:
        verf, nit, letzter = kand, 0, 0.0
    out["aberth"] = {"iterationen": int(nit), "letzter_schritt": float(letzter),
                     "max_verschiebung_rel": float(np.max(np.abs(verf - kand)) / kb) if len(kand) else 0.0}
    inR = (verf.real > 0) & (verf.real <= RW.R_RE * kb) & (np.abs(verf.imag) <= RW.R_IM * kb)
    wR = verf[inR]
    wR = wR[np.argsort(wR.real)]
    sR, _ = RW.s_wert(Fm, wR) if len(wR) else (np.array([]), None)
    wd = RW.windung(Fm, kb)
    p = RW.randpunkte(kb, wd["faktor"])
    wd["rho_rand_min"] = float(np.min(RW.rho(Qn0, nullbasis_s(git, 1j * p, ks, mit_top))))
    out["windung"] = wd
    QT = RW.tt_kanten(git, B, nhat)
    nst = []
    for w, sw in zip(wR, sR):
        ki = kern_info(git, Fm, Q0, Qn0, B, basis, Ckomp, QT, nhat, ks, mit_top, w)
        ki.update({"v_re": float(w.real / kb), "v_im": float(w.imag / kb), "s": float(sw)})
        nst.append(ki)
    out["nullstellen"] = nst
    g = wurz[(wurz.real > RW.R_RE * kb) & (wurz.real <= RW.GEIST_RE_MAX) & (np.abs(wurz.imag) <= RW.R_IM * kb)]
    out["geister"] = [{"re": float(x.real), "im": float(x.imag)} for x in np.sort_complex(g)]
    out["pep_naechste_ausserhalb"] = [{"re": float(x.real), "im": float(x.imag)} for x in
                                      sorted(wurz[~inR2], key=lambda x: abs(x - kb))[:4]]
    # --- Kinetik-Matrix (omega^2-Koeffizient der direkten h-Form, physikalisches h)
    K2 = sum((m * m / 8.0) * (B.T @ Cm @ B) for m, Cm in C.items())
    V0 = RW.v0_basis(git, nhat)
    K2r = V0.T @ K2 @ V0
    imag_rel = float(np.max(np.abs(K2r.imag)) / np.max(np.abs(K2r)))
    _, sk, Vk = np.linalg.svd(K2r.real)
    W = Vk[3:].T
    out["kinetik"] = {"sing": sk.tolist(), "imag_rel": imag_rel,
                      "lapse_shift_anteil_klein3": float(np.sum(W[:3, :] ** 2) / 3.0),
                      "lapse_shift_anteil_gross3": float(np.sum(Vk[:3].T[:3, :] ** 2) / 3.0),
                      "luecke_s4_durch_s3": float(sk[3] / sk[2])}
    # --- Wuerfelgitter-Formel sinh^2(omega/2) = sum sin^2(k_i/2) (beschreibend)
    out["hyperkubisch"] = {"v_gitter_k": float(2 * np.arcsinh(np.sqrt(np.sum(np.sin(ks / 2) ** 2))) / kb),
                           "v_phys_k": float(2 * np.arcsinh(np.sqrt(np.sum(np.sin(kp / 2) ** 2))) / kb)}
    if mit_extra:
        # --- Zensus aller Wurzeln nahe der reellen Achse und auf der imaginaeren Achse (PLAN [F6])
        # Verfeinerung: Wurzeln in R' uebernehmen den Aberth-Wert von oben, alle anderen gedaempftes Newton je Wurzel
        # (Fassung nach Rauchlauf s = 0,1: die gemeinsame Aberth-Iteration ueber alle Zensuswurzeln brach ab).
        sel = (wurz.real >= ZENSUS_RE_MIN) & (wurz.real <= ZENSUS_RE_MAX) & (np.abs(wurz.imag) <= ZENSUS_IM_MAX)
        wver = wurz.copy()
        wver[inR2] = verf
        zen = []
        for i in np.nonzero(sel)[0]:
            w0 = wurz[i]
            w, nit_n = (wver[i], -1) if inR2[i] else newton_einzeln(Fm, w0, kb)
            try:
                sw = float(RW.s_wert(Fm, np.array([w]))[0][0])
                ki = kern_info(git, Fm, Q0, Qn0, B, basis, Ckomp, QT, nhat, ks, mit_top, w)
            except (np.linalg.LinAlgError, ValueError, FloatingPointError):
                ki, sw = {"re": float(w.real), "im": float(w.imag), "rho": 0.0, "physikalisch": 0.0,
                          "fehler": "Linalg"}, float("inf")
            ki.update({"pep_re": float(w0.real), "pep_im": float(w0.imag), "s": sw, "newton_iter": int(nit_n),
                       "in_R": bool((w.real > 0) and (w.real <= RW.R_RE * kb) and (abs(w.imag) <= RW.R_IM * kb))})
            zen.append(ki)
        out["zensus"] = sorted(zen, key=lambda x: (x["re"], x["im"]))
        # --- euklidische Linie k = (kappa, k_lat): Signatur von H (PLAN [F7])
        kap = np.linspace(-np.pi, np.pi, N_EUKL)
        kk = np.column_stack([kap, np.tile(ks, (N_EUKL, 1))])
        _, _, Me = git.matrizen(kk, eT)
        He, imag_e = R4.h_von_M(Me)
        le = np.linalg.eigvalsh(He)
        ae = np.abs(le)
        me = ae.mean(axis=1)
        nneg = np.sum(le <= -NULL_REL * me[:, None], axis=1)
        nnull = np.sum(ae < NULL_REL * me[:, None], axis=1)
        klein = np.sort(ae, axis=1)[:, nn] / me
        wechsel = [float(0.5 * (kap[i] + kap[i + 1])) for i in range(N_EUKL - 1) if nneg[i] != nneg[i + 1]]
        out["eukl_linie"] = {"n_neg_werte": sorted(set(int(x) for x in nneg)),
                             "n_null_werte": sorted(set(int(x) for x in nnull)),
                             "wechsel_kappa": wechsel, "kleinster_nichtnull_rel_min": float(klein.min()),
                             "kappa_bei_min": float(kap[int(np.argmin(klein))]), "imag_rel": float(imag_e),
                             "kleinster_nichtnull_rel": klein[::8].tolist(), "kappa": kap[::8].tolist(),
                             "n_neg": nneg[::8].tolist()}
    if mit_eigen:
        om2 = RW.R_RE * kb * np.arange(1, 201) / 200
        ev = np.linalg.eigvals(RW.laurent(C, np.exp(-0.5 * om2)))
        mod = np.sort(np.abs(ev), axis=1) / np.max(np.abs(ev), axis=1)[:, None]
        out["eigen_M"] = {"omega": om2.tolist(), "betrag_rel_sortiert": mod.tolist()}
    out["laufzeit_s"] = time.time() - t0
    return out


def stichproben(git, form, eT, rng, mit_top, log):
    """Kontrolle G: (a) Laurent-Form bei reellem Gitter-k gegen git.matrizen; (b) Nullvektoren bei komplexem k_tau;
    (c) e_top bei s != 0 kein Nullvektor (beschreibend)."""
    Rr = R4.richtungen(4)
    ks = [b * nh for nh in Rr.values() for b in [0.05, 0.1, 0.2, 0.4]]
    ks = np.array(ks + list(rng.uniform(-np.pi, np.pi, size=(64, 4))))
    _, _, M4 = git.matrizen(ks, eT)
    abw = []
    for k, Mref in zip(ks, M4):
        C = form.koeffizienten(k[SP])
        M = RW.laurent(C, np.exp(0.5j * k[TAU]))[0]
        abw.append(float(np.max(np.abs(M - Mref)) / np.max(np.abs(Mref))))
    res, etop_res = [], []
    et = np.zeros(git.nE)
    et[git.top] = 1.0
    for _ in range(64):
        ktau = rng.uniform(-np.pi, np.pi) + 1j * rng.uniform(-2.4, 2.4)
        kss = rng.uniform(-np.pi, np.pi, size=3)
        C = form.koeffizienten(kss)
        M = RW.laurent(C, np.exp(0.5j * ktau))[0]
        N = nullbasis_s(git, [ktau], kss, mit_top)[0]
        r = np.max(np.linalg.norm(M @ N, axis=0) / np.linalg.norm(N, axis=0)) / np.linalg.norm(M, 2)
        res.append(float(r))
        etop_res.append(float(np.linalg.norm(M @ et) / np.linalg.norm(M, 2)))
    protokoll(log, f"G: (a) max {max(abw):.2e}, (b) komplex max {max(res):.2e}, e_top-Residuum min {min(etop_res):.2e}")
    return {"a_abw_je_punkt": abw, "a_max": max(abw), "a_punkte": len(abw), "b_zufall_residuen": res,
            "b_zufall_max": max(res), "etop_residuum_min": min(etop_res), "etop_residuum_max": max(etop_res)}


def eK_schief(git):
    """Weg K (komplexer Schritt) mit den schiefen Laengen (regge_schief.jacobi_komplex), Aufbau wie
    regge_welle.eK_stencil."""
    J, _ = RS.jacobi_komplex(git)
    dic = git.eT_aus_J(J)
    eT = []
    for d in range(git.nE):
        keys = sorted((t, Rr) for (t, dd, Rr) in dic if dd == d)
        tau = np.array([q[0] for q in keys], dtype=np.int64)
        Rp = np.array([q[1] for q in keys], dtype=np.int64).reshape(len(keys), git.n)
        val = np.array([dic[(q[0], d, q[1])] for q in keys])
        eT.append((tau, Rp, val))
    return eT


def main():
    modus, s_arg, ziel = sys.argv[1], sys.argv[2], sys.argv[3]
    s = float(s_arg)
    mit_top = (s == 0.0)
    t0 = time.time()
    log = []
    res = {"skript_sha256": SKRIPT_SHA, "modul_sha256": SHAS, "numpy": np.__version__, "modus": modus, "s": s,
           "mit_top": mit_top, "zeit_utc_start": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "festlegungen": {"R_RE": RW.R_RE, "R_IM": RW.R_IM, "N_ACHSE": RW.N_ACHSE, "RHO_MIN": RW.RHO_MIN,
                            "S_WURZEL": RW.S_WURZEL, "PHYS_MIN": RW.PHYS_MIN, "PHASE_MAX": RW.PHASE_MAX,
                            "TRIM_REL": RW.TRIM_REL, "ZENSUS": [ZENSUS_RE_MIN, ZENSUS_RE_MAX, ZENSUS_IM_MAX],
                            "N_EUKL": N_EUKL}}
    A = RS.matrix_A(s)
    git = RS.GitterSchief(A)
    eps0 = git.fehlwinkel(git.s0)
    eT, fehler, _ = git.ableitung_T()
    form = RW.Form(git, eT)
    B = git.B0()
    basis, _ = git.sym_basis()
    Ckomp, rang14 = R4.komplement(git, B)
    _, _, M0 = git.matrizen(np.zeros((1, 4)), eT)
    l0, V0 = np.linalg.eigh(R4.h_von_M(M0)[0][0])
    o0 = np.argsort(np.abs(l0))
    res["geometrie"] = {"A": A.tolist(), "detA": float(np.linalg.det(A)), "flach_max_abs_eps": float(np.max(np.abs(eps0))),
                        "weg_T_fehlerschaetzung": float(max(fehler)), "rang_B_ohne_top": int(rang14),
                        "laurent_pe": sorted(set(form.pe.tolist())), "laurent_pa": sorted(set(form.pa.tolist())),
                        "k0_eigen_sortiert_betrag": [float(l0[i]) for i in o0],
                        "k0_elfter_top_anteil": float(abs(V0[git.top, o0[10]]))}
    protokoll(log, f"s={s}: flach {res['geometrie']['flach_max_abs_eps']:.1e}, Weg T {max(fehler):.1e}, "
                   f"k=0 11. Eigenwert {l0[o0[10]]:.4f} ({time.time() - t0:.1f} s)")
    rng = np.random.default_rng(20261004)
    res["g"] = stichproben(git, form, eT, rng, mit_top, log)
    R = RW.richtungen()
    betraege = BETRAEGE if modus == "haupt" else RAUCH_BETRAEGE
    if modus != "haupt":
        R = [r for r in R if r[0] in RAUCH_RICHTUNGEN]
    erg = []
    for nm, nh in R:
        for kb in betraege:
            a = analyse_s(git, form, eT, B, basis, Ckomp, nm, nh, kb, mit_top, mit_eigen=nm in EIGEN_R)
            erg.append(a)
            zi = [z for z in a["zensus"] if z["s"] <= RW.S_WURZEL and z["rho"] >= RW.RHO_MIN
                  and z["physikalisch"] >= RW.PHYS_MIN]
            protokoll(log, f"{nm:>7s} |k|={kb}: Windung {a['windung']['windung']:.3f}, in R {len(a['nullstellen'])}, "
                           f"Zensus {len(a['zensus'])} (intrinsisch {len(zi)}), eukl. n_neg {a['eukl_linie']['n_neg_werte']}"
                           f" ({a['laufzeit_s']:.1f} s)")
        with open(ziel + ".teil", "w") as f:
            json.dump(dict(res, punkte=erg), f)
    res["punkte"] = erg
    # Gegenprobe Weg K (beschreibend)
    formK = RW.Form(git, eK_schief(git))
    gk = []
    for nm, nh in [r for r in RW.richtungen() if r[0] in ("x+", "xyz+", "123", "fib05")]:
        for kb in ([0.05, 0.8] if modus == "haupt" else [0.3]):
            aK = analyse_s(git, formK, eT, B, basis, Ckomp, nm, nh, kb, mit_top, mit_extra=False)
            gk.append({"richtung": nm, "betrag": kb, "nullstellen": [[x["re"], x["im"]] for x in aK["nullstellen"]],
                       "windung": aK["windung"]["zahl"]})
    res["gegenprobe_weg_K"] = gk
    protokoll(log, f"Gegenprobe Weg K fertig ({time.time() - t0:.1f} s)")
    res["laufzeit_s"] = time.time() - t0
    res["protokoll"] = log
    with open(ziel, "w") as f:
        json.dump(res, f, indent=1)
    print("geschrieben", ziel, f"{time.time() - t0:.1f} s", flush=True)


if __name__ == "__main__":
    main()
