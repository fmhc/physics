#!/usr/bin/env python3
"""LIN-WIRBEL-1: lineare Stabilitaet drehender 2D-Q-Baelle mit Windung m (NLS-Form gegen KG-Form).

Modell (unsere Einheiten): phi_tt - Laplace phi + U'(|phi|^2) phi = 0, U(S) = S - S^2 + S^3/2,
Welle phi = e^{i omega t} e^{i m theta} f(r), f'' + f'/r - m^2 f/r^2 = (1 - omega^2 - 2 f^2 + 1.5 f^4) f.
Stoerung mit Index J: a(r) (Winkelindex m+J), b(r) (Winkelindex m-J), lambda = i nu:
  NLS-Form (KG ohne lambda^2): (K - 2 omega nu sigma_3) v = 0
  KG-Form:                     (K - 2 omega nu sigma_3 - nu^2) v = 0
  K = [[-Delta_{m+J} + dp - omega^2, sp], [sp, -Delta_{m-J} + dp - omega^2]], dp = 1 - 4S + 4.5S^2, sp = -2S + 3S^2.
Wachstumsrate gamma = Re lambda = -Im nu; ausgegeben wird |Im nu| (Spektrum ist konjugationssymmetrisch).
NLS-Einheiten (Pego-Warchall): lambda_NLS = (3 omega / 4) * lambda, Omega = (3/8)(1 - omega^2).
Radial-FD 2. Ordnung, zellzentriert r_i = (i - 1/2) h, Flussform, symmetrisiert (v = sqrt(r) u), Dirichlet am Rand.
Aufruf ueber kleintest.sh (Spur cpu5):  lin_wirbel.py probe  |  lin_wirbel.py lauf M
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys
import json
import time
import hashlib
import platform
import numpy as np
import scipy
import scipy.linalg as sla
import scipy.sparse as sps
import scipy.sparse.linalg as spla
from scipy.integrate import solve_ivp

T0 = time.time()


def log(*a):
    print(f"[{time.time() - T0:8.1f}s]", *a, flush=True)


# ---------------------------------------------------------------- Gitter und Operatoren
def gitter(h, R):
    N = int(round(R / h))
    return (np.arange(1, N + 1) - 0.5) * h


def minus_lap(n, r, h, sym=True):
    """-Delta_n = -(1/r)(r u')' + n^2/r^2 u, Fluss bei r = 0 null, u = 0 hinter dem letzten Punkt."""
    rp = r + 0.5 * h
    rm = r - 0.5 * h
    rm[0] = 0.0
    dia = (rp + rm) / (h * h * r) + (n * n) / (r * r)
    if sym:
        off = -rp[:-1] / (h * h * np.sqrt(r[:-1] * r[1:]))
        return sps.diags([off, dia, off], [-1, 0, 1], format="csr")
    up = -rp[:-1] / (h * h * r[:-1])
    lo = -rp[:-1] / (h * h * r[1:])
    return sps.diags([lo, dia, up], [-1, 0, 1], format="csr")


# ---------------------------------------------------------------- Profil
def _schuss(m, w2, c, rend=80.0, r0=1e-2):
    k2 = 1.0 - w2

    def rhs(r, y):
        f, g = y
        return [g, -g / r + m * m * f / (r * r) + (k2 - 2.0 * f * f + 1.5 * f ** 4) * f]

    f0 = c * r0 ** m * (1.0 + k2 * r0 ** 2 / (4.0 * (m + 1)))
    g0 = c * (m * r0 ** (m - 1) + (m + 2) * k2 * r0 ** (m + 1) / (4.0 * (m + 1)))

    def e_null(r, y):
        return y[0]
    e_null.terminal = True
    e_null.direction = -1

    def e_hoch(r, y):
        return y[0] - 1.3
    e_hoch.terminal = True
    e_hoch.direction = 1

    def e_kehr(r, y):
        return y[1]
    e_kehr.terminal = True
    e_kehr.direction = 1

    sol = solve_ivp(rhs, (r0, rend), [f0, g0], method="DOP853", rtol=1e-12, atol=1e-300,
                    events=[e_null, e_hoch, e_kehr], dense_output=True)
    if len(sol.t_events[0]) or len(sol.t_events[1]):
        return +1, sol
    if len(sol.t_events[2]):
        return -1, sol
    return 0, sol


def profil_schuss(m, w2, r):
    lo = hi = None
    for c in np.logspace(-5, 1, 61):
        k, _ = _schuss(m, w2, c)
        if k == -1:
            lo = c
        elif k == +1 and lo is not None:
            hi = c
            break
    if lo is None or hi is None:
        raise RuntimeError(f"keine Klammer fuer m={m} w2={w2}")
    for _ in range(200):
        mid = np.sqrt(lo * hi)
        if not (lo < mid < hi):
            break
        k, _ = _schuss(m, w2, mid)
        if k == -1:
            lo = mid
        elif k == +1:
            hi = mid
        else:
            lo = mid
            break
    k, sol = _schuss(m, w2, lo)
    rk = sol.t_events[2][0] if len(sol.t_events[2]) else sol.t[-1]
    fk = abs(sol.sol(rk)[0])
    rr = np.linspace(1e-2, rk, 20001)
    ff = sol.sol(rr)[0]
    ip = int(np.argmax(ff))
    kand = np.nonzero(ff[ip:] <= 30.0 * fk)[0]
    rcut = rr[ip + kand[0]] if len(kand) else rk
    fcut = float(sol.sol(rcut)[0])
    kap = np.sqrt(1.0 - w2)
    f = np.empty_like(r)
    innen = r <= rcut
    f[innen] = sol.sol(np.maximum(r[innen], 1e-2))[0]
    klein = r < 1e-2
    f[klein] = lo * r[klein] ** m
    aus = ~innen
    f[aus] = fcut * np.sqrt(rcut / r[aus]) * np.exp(-kap * (r[aus] - rcut))
    return f, dict(c=float(lo), c_rel_breite=float(hi / lo - 1.0), r_schnitt=float(rcut))


def newton(m, w2, r, h, f, maxit=40):
    k2 = 1.0 - w2
    T = minus_lap(m, r, h, sym=False)
    it = 0
    for it in range(1, maxit + 1):
        S = f * f
        F = T @ f + (k2 - 2.0 * S + 1.5 * S * S) * f
        Jm = (T + sps.diags(k2 - 6.0 * S + 7.5 * S * S)).tocsc()
        df = spla.spsolve(Jm, -F)
        f = f + df
        if np.max(np.abs(df)) < 1e-14:
            break
    S = f * f
    F = T @ f + (k2 - 2.0 * S + 1.5 * S * S) * f
    return f, float(np.max(np.abs(F))), it


def profil_ok(f, r, R, res, w2):
    """Knotenloses Wirbelprofil: f_max unter dem zweiten Huegel f_2 (f_2^2 = (2 + sqrt(4 - 6 kappa^2))/3,
    fuer omega^2 nahe 1/2 knapp ueber 1) und kleiner Rand; das Plateau f = f_2 fuellt die Box und faellt am Rand durch."""
    S = f * f
    k2 = 1.0 - w2
    S2 = (2.0 + np.sqrt(max(4.0 - 6.0 * k2, 0.0))) / 3.0
    return bool(f.max() > 0.2 and f.min() > -1e-8 and res < 1e-8 and S.max() < S2
                and f[r > R - 5.0].max() / f.max() < 1e-2)


def profil(m, w2, h, R, start=None):
    """start = (r_alt, f_alt, w2_alt): Fortsetzung in Schritten <= 0,002 mit Newton, sonst Schiessen."""
    r = gitter(h, R)
    sinfo = {}
    f = None
    res, it = np.inf, 0
    if start is not None:
        rs, fs, w2s = start
        f = np.interp(r, rs, fs, right=0.0)
        n = max(1, int(np.ceil(abs(w2 - w2s) / 0.002 - 1e-12)))
        for k in range(1, n + 1):
            wk = w2s + (w2 - w2s) * k / n
            f, res, it = newton(m, wk, r, h, f)
            if not profil_ok(f, r, R, res, wk):
                f = None
                break
        quelle = f"fortsetzung({n})"
    if f is None:
        f0, sinfo = profil_schuss(m, w2, r)
        f, res, it = newton(m, w2, r, h, f0)
        quelle = "schuss"
        if not profil_ok(f, r, R, res, w2):
            raise RuntimeError(f"Profil nicht konvergiert m={m} w2={w2} res={res} fmax={f.max()}")
    S = f * f
    w = np.sqrt(w2)
    Q = float(2 * np.pi * w * np.sum(S * r) * h)
    info = dict(quelle=quelle, newton_it=it, residuum=res, f_max=float(f.max()),
                r_max=float(r[np.argmax(f)]), S_max=float(S.max()), Q=Q,
                f_rand_rel=float(f[r > R - 5.0].max() / f.max()), **sinfo)
    return r, f, info


# ---------------------------------------------------------------- Eigenwertprobleme
def K_matrix(m, J, w2, f, r, h):
    S = f * f
    dp = 1.0 - 4.0 * S + 4.5 * S * S
    spp = -2.0 * S + 3.0 * S * S
    A = minus_lap(m + J, r, h) + sps.diags(dp - w2)
    B = minus_lap(m - J, r, h) + sps.diags(dp - w2)
    C = sps.diags(spp)
    return sps.bmat([[A, C], [C, B]], format="csr")


def spektrum_dicht(K, w, form):
    n2 = K.shape[0]
    N = n2 // 2
    s3 = np.r_[np.ones(N), -np.ones(N)]
    Kd = K.toarray()
    if form == "nls":
        return sla.eigvals(s3[:, None] * Kd, check_finite=False, overwrite_a=True) / (2.0 * w)
    Z = np.zeros((2 * n2, 2 * n2))
    Z[:n2, n2:] = np.eye(n2)
    Z[n2:, :n2] = Kd
    Z[n2:, n2:] = np.diag(-2.0 * w * s3)
    return sla.eigvals(Z, check_finite=False, overwrite_a=True)


def op_sparse(K, w, form):
    n2 = K.shape[0]
    N = n2 // 2
    S3 = sps.diags(np.r_[np.ones(N), -np.ones(N)])
    if form == "nls":
        return (S3 @ K).tocsc()
    I = sps.identity(n2, format="csr")
    return sps.bmat([[None, I], [K, -2.0 * w * S3]], format="csc")


def eig_nahe(Op, w, form, nu0, k=8, vecs=False):
    s = 2.0 * w * nu0 if form == "nls" else nu0
    s = complex(s)
    if s.imag != 0.0:
        A = Op.astype(complex)
        sig = s
    else:
        A = Op
        sig = s.real
    if vecs:
        vals, V = spla.eigs(A, k=k, sigma=sig, which="LM")
    else:
        vals = spla.eigs(A, k=k, sigma=sig, which="LM", return_eigenvectors=False)
        V = None
    if form == "nls":
        vals = vals / (2.0 * w)
    return vals, V


def aussenanteil(Op, w, form, nu0, r, R):
    vals, V = eig_nahe(Op, w, form, complex(nu0) + 1e-9j, k=1, vecs=True)
    N = len(r)
    v = V[:, 0][:2 * N]
    wgt = np.abs(v[:N]) ** 2 + np.abs(v[N:]) ** 2
    return float(wgt[r > 0.75 * R].sum() / wgt.sum()), complex(vals[0])


GTOL_DICHT = 1e-6
NULLRADIUS = 0.01
LOKAL = 1e-3


def auswerten_dicht(nu, Op, w, w2, form, J, r, R, nmax_pruef=4):
    """Instabile Eigenwerte (ein Vertreter je konjugiertem Paar), Lokalisierung der groessten."""
    kand = nu[nu.imag > GTOL_DICHT]
    null = kand[np.abs(kand) < NULLRADIUS] if J in (0, 1) else kand[:0]
    if J in (0, 1):
        kand = kand[np.abs(kand) >= NULLRADIUS]
    kand = kand[np.argsort(-kand.imag)]
    liste = []
    for i, z in enumerate(kand):
        eintrag = dict(re=float(z.real), im=float(z.imag))
        if i < nmax_pruef:
            try:
                fr, zz = aussenanteil(Op, w, form, z, r, R)
                eintrag["aussen"] = fr
                eintrag["lokal"] = bool(fr < LOKAL)
            except Exception as ex:  # noqa: BLE001
                eintrag["aussen"] = None
                eintrag["lokal"] = None
                eintrag["fehler"] = str(ex)[:120]
        liste.append(eintrag)
    g_lok = max([e["im"] for e in liste if e.get("lokal")] + [0.0])
    g_box = max([e["im"] for e in liste if e.get("lokal") is False] + [0.0])
    g_alle = max([e["im"] for e in liste] + [0.0])
    gap = (1.0 - w2) / (2.0 * w) if form == "nls" else 1.0 - w
    reell = np.sort(nu[(np.abs(nu.imag) <= GTOL_DICHT) & (np.abs(nu.real) < gap)].real)
    return dict(gamma_lokal=g_lok, gamma_box=g_box, gamma_alle=g_alle, n_instabil=len(liste),
                instabil=liste[:8], null_max_im=float(max([z.imag for z in null] + [0.0])),
                gap=float(gap), gap_reell=[round(float(x), 7) for x in reell])


def gamma_fenster(m, J, w2, h, R, form, nu_ref, start, fenster=0.03, k=8):
    r, f, pinfo = profil(m, w2, h, R, start=start)
    K = K_matrix(m, J, w2, f, r, h)
    w = np.sqrt(w2)
    Op = op_sparse(K, w, form)
    vals, _ = eig_nahe(Op, w, form, nu_ref, k=k)
    sel = vals[np.abs(vals.real - nu_ref) < fenster]
    if len(sel) == 0:
        return 0.0, nu_ref, (r, f, w2), vals
    i = int(np.argmax(np.abs(sel.imag)))
    return float(abs(sel[i].imag)), float(sel[i].real), (r, f, w2), vals


def schwelle(m, J, h, R, form, lo, hi, nu_ref, start, gtol=1e-8, breite=2e-6):
    glo, _, st, _ = gamma_fenster(m, J, lo, h, R, form, nu_ref, start)
    n = 0
    while glo > gtol and n < 8:
        lo -= 0.004
        glo, _, st, _ = gamma_fenster(m, J, lo, h, R, form, nu_ref, st)
        n += 1
    ghi, nr, st_hi, _ = gamma_fenster(m, J, hi, h, R, form, nu_ref, st)
    n = 0
    while ghi <= gtol and n < 8:
        hi += 0.004
        ghi, nr, st_hi, _ = gamma_fenster(m, J, hi, h, R, form, nu_ref, st_hi)
        n += 1
    if glo > gtol or ghi <= gtol:
        return dict(ok=False, lo=lo, hi=hi, glo=glo, ghi=ghi)
    nu_ref = nr
    schritte = 0
    while hi - lo > breite:
        mid = 0.5 * (lo + hi)
        g, nr, st_m, _ = gamma_fenster(m, J, mid, h, R, form, nu_ref, st_hi)
        schritte += 1
        if g > gtol:
            hi, ghi, nu_ref, st_hi = mid, g, nr, st_m
        else:
            lo = mid
    w = np.sqrt(hi)
    return dict(ok=True, schwelle=0.5 * (lo + hi), lo=lo, hi=hi, gamma_hi=ghi, nu_c=nu_ref,
                nu_c_NLS_einheiten=float(0.75 * w * nu_ref), Omega_c=float(0.375 * (1.0 - 0.5 * (lo + hi))),
                schritte=schritte)


# ---------------------------------------------------------------- Laeufe
def meta():
    with open(os.path.abspath(__file__), "rb") as fh:
        sha = hashlib.sha256(fh.read()).hexdigest()
    return dict(skript_sha256=sha, numpy=np.__version__, scipy=scipy.__version__,
                python=platform.python_version(), rechner=platform.node(),
                start_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(T0)))


def probe():
    out = dict(meta=meta(), teile=[])
    for (m, w2) in [(1, 0.60), (1, 0.61)]:
        t = time.time()
        r, f, pinfo = profil(m, w2, 0.1, 40.0)
        log(f"Profil m={m} w2={w2}: {json.dumps(pinfo)} ({time.time() - t:.1f}s)")
        w = np.sqrt(w2)
        for J in (1, 2):
            K = K_matrix(m, J, w2, f, r, 0.1)
            for form in ("nls", "kg"):
                t = time.time()
                nu = spektrum_dicht(K, w, form)
                td = time.time() - t
                Op = op_sparse(K, w, form)
                aw = auswerten_dicht(nu, Op, w, w2, form, J, r, 40.0)
                log(f"m={m} w2={w2} J={J} {form}: dicht {td:.1f}s, gamma_lokal={aw['gamma_lokal']:.3e} "
                    f"gamma_box={aw['gamma_box']:.3e} n_inst={aw['n_instabil']} null={aw['null_max_im']:.2e} "
                    f"instabil={aw['instabil'][:3]} gap_reell={aw['gap_reell'][:12]}")
                out["teile"].append(dict(m=m, w2=w2, J=J, form=form, t_dicht=td, **aw))
    with open("PROBE.json", "w") as fh:
        json.dump(out, fh, indent=1)
    log("probe fertig")


SCAN = {1: [0.57, 0.58, 0.59, 0.595, 0.60, 0.605, 0.61, 0.62],
        2: [0.55, 0.56, 0.565, 0.57, 0.575, 0.58, 0.59, 0.60],
        3: [0.53, 0.535, 0.54, 0.545, 0.55, 0.555, 0.56, 0.57]}
ZEITPUNKTE = {1: [0.59, 0.60], 2: [0.57, 0.59], 3: []}


def lauf(m, zeitgrenze=480.0, Js=(1, 2, 3, 4, 5, 6), R=40.0, R_scan=32.0):
    out = dict(meta=meta(), m=m, R=R, R_scan=R_scan, h_dicht=0.1, scan=[], profile={}, schwellen=[], zeitpunkte=[])
    h = 0.1
    prev = None
    profile = {}
    for w2 in SCAN[m]:
        if time.time() - T0 > zeitgrenze * 0.68:
            log(f"Zeitgrenze Scan erreicht vor w2={w2}")
            out["scan_abgebrochen_vor"] = w2
            break
        r, f, pinfo = profil(m, w2, h, R_scan, start=prev)
        prev = (r, f, w2)
        profile[w2] = (r, f, w2)
        out["profile"][str(w2)] = pinfo
        log(f"Profil m={m} w2={w2}: fmax={pinfo['f_max']:.5f} rmax={pinfo['r_max']:.2f} Q={pinfo['Q']:.3f} "
            f"res={pinfo['residuum']:.1e} rand={pinfo['f_rand_rel']:.1e} ({pinfo['quelle']})")
        w = np.sqrt(w2)
        for J in Js:
            K = K_matrix(m, J, w2, f, r, h)
            for form in ("nls", "kg"):
                nu = spektrum_dicht(K, w, form)
                Op = op_sparse(K, w, form)
                aw = auswerten_dicht(nu, Op, w, w2, form, J, r, R_scan)
                out["scan"].append(dict(w2=w2, J=J, form=form, **aw))
                if aw["n_instabil"]:
                    log(f"  J={J} {form}: gamma_lokal={aw['gamma_lokal']:.4e} gamma_box={aw['gamma_box']:.2e} "
                        f"top={aw['instabil'][:2]}")
    # Schwellen: fuer jedes (J, Form) die erste lokalisierte Instabilitaet im Scan
    auftraege = []
    for J in Js:
        for form in ("nls", "kg"):
            zeilen = [z for z in out["scan"] if z["J"] == J and z["form"] == form]
            zeilen.sort(key=lambda z: z["w2"])
            for i in range(1, len(zeilen)):
                if zeilen[i]["gamma_lokal"] > 0 and zeilen[i - 1]["gamma_lokal"] == 0:
                    top = [e for e in zeilen[i]["instabil"] if e.get("lokal")]
                    top.sort(key=lambda e: -e["im"])
                    auftraege.append((J, form, zeilen[i - 1]["w2"], zeilen[i]["w2"], top[0]["re"]))
                    break
    auftraege.sort(key=lambda a: (a[0] != 2, a[0], a[1]))
    log(f"Schwellen-Auftraege: {auftraege}")
    for (J, form, lo, hi, nr) in auftraege:
        varianten = ((0.1, R), (0.05, R), (0.1, R + 10.0)) if J == 2 else ((0.1, R),)
        for (hh, RR) in varianten:
            if time.time() - T0 > zeitgrenze:
                log("Zeitgrenze vor Schwelle erreicht")
                out["schwellen_abgebrochen"] = True
                break
            st = profile.get(hi) or prev
            t = time.time()
            s = schwelle(m, J, hh, RR, form, lo, hi, nr, st)
            s.update(dict(J=J, form=form, h=hh, R=RR, t=round(time.time() - t, 1)))
            out["schwellen"].append(s)
            log(f"Schwelle m={m} J={J} {form} h={hh} R={RR}: {json.dumps(s)}")
    # Zeitentwicklungs-Stellen bei h = 0,05 (J = 2, Fenster um die Kollisionsfrequenz)
    for w2 in ZEITPUNKTE[m]:
        for form in ("nls", "kg"):
            kand = [s for s in out["schwellen"] if s.get("ok") and s["J"] == 2 and s["form"] == form]
            if not kand or time.time() - T0 > zeitgrenze + 30:
                continue
            nr = kand[0]["nu_c"]
            st = profile.get(w2) or prev
            g, re_, _, vals = gamma_fenster(m, 2, w2, 0.05, R, form, nr, st)
            out["zeitpunkte"].append(dict(w2=w2, form=form, h=0.05, gamma=g, re=re_))
            log(f"Zeitpunkt m={m} w2={w2} {form} h=0.05: gamma={g:.5f} re={re_:.5f}")
    out["ende_s"] = round(time.time() - T0, 1)
    with open(f"LIN-WIRBEL-m{m}.json", "w") as fh:
        json.dump(out, fh, indent=1)
    log(f"lauf m={m} fertig")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    if sys.argv[1] == "probe":
        probe()
    elif sys.argv[1] == "lauf":
        M = int(sys.argv[2]); lauf(M, R=(48.0 if M >= 3 else 40.0), R_scan=(36.0 if M >= 3 else 32.0))
    else:
        print("unbekannt", sys.argv[1])
        sys.exit(2)
