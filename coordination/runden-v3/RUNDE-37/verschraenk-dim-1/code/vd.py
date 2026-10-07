#!/usr/bin/env python3
"""VERSCHRAENK-DIM-1 (Runde 42), Code-Agent fuer die Leitung claude-primary.

Halbraum-Verschraenkung des freien massiven Skalarfelds (Masse m in Gittereinheiten) auf Z^D,
Grundzustand, Schnitt x_1 < 0 gegen x_1 >= 0. Zerlegung in 1D-Ketten je Querimpuls k:
  m_eff^2 = m^2 + sum_{i=2..D} 4 sin^2(k_i/2),   S_D(m) = Mittel_k S_1(m_eff(k)).

Aufruf nur auf der .69 ueber kleintest.sh (1 Thread):
  vd.py s1 <ordner>          S_1(M) per Korrelationsmatrix (Peschel), Laengenprobe, Splineprobe, CTM-Gegenprobe
  vd.py direkt <ordner>      direkte 2D-/3D-Gitterrechnung gegen die Zerlegung auf demselben Gitter
  vd.py sd <ordner>          S_D(m): D = 2, 3 Gauss-Legendre (gestuft), D = 2..DMAX Monte Carlo (liest s1.json)
  vd.py auswertung <ordner>  S_tot, D*(N, m), Urteile VD0-VD2 nach Plan und Kartenwortlaut
  vd.py bild <ordner>        PNG aus auswertung.json
  vd.py rauch <ordner>       alle Modi mit Kleinstgroessen; gibt nur Laufzeiten aus, keine Werte
"""
import sys, os, json, time, math
import numpy as np
from scipy import linalg, special, integrate
from scipy.interpolate import CubicSpline

MASSEN = [0.01, 0.1, 1.0]
N_EXP = [3, 6, 9, 12, 80]           # N = 10^e
DTAB = 24                           # Tabellenbereich der Karte
DMAX = 200                          # Suchbereich fuer D* (Plan Abschn. 3, F1)
SEED = 20261004
X0, X1 = math.log(1e-4), math.log(1e3)   # x = ln(mu), mu = M^2

P = dict(nx=421, ell_faktor=16.0, ell_min=48, probe_schritt=20, probe_faktor=1.5,
         nb=32, npb=1 << 17, gl_grob=(40, 16), gl_fein=(60, 24), gl_kleinste=1e-4,
         direkt2=(48, 32), direkt3=(24, 10), nfein=200001, nboot=400)
RAUCH = dict(nx=29, ell_faktor=3.0, ell_min=8, probe_schritt=7, probe_faktor=1.5,
             nb=2, npb=256, gl_grob=(4, 4), gl_fein=(6, 4), gl_kleinste=1e-4,
             direkt2=(8, 4), direkt3=(6, 4), nfein=1001, nboot=10)


# ---------- Halbketten-Verschraenkung (Peschel) ----------

def s_von_nu2(ev):
    nu = np.sqrt(np.maximum(np.asarray(ev, float), 0.25))
    a = nu + 0.5
    b = nu - 0.5
    s = a * np.log(a)
    pos = b > 0
    s[pos] -= b[pos] * np.log(b[pos])
    return float(s.sum())


def s_block(XA, PA):
    """Entropie eines Gauss-Zustands aus <phi phi>_A und <pi pi>_A: nu^2 = eig(X P) = eig(L^T P L), X = L L^T."""
    L = linalg.cholesky(XA, lower=True, check_finite=False)
    Mm = L.T @ PA @ L
    Mm = 0.5 * (Mm + Mm.T)
    ev = linalg.eigvalsh(Mm, check_finite=False)
    return s_von_nu2(ev)


def kappa_von_mu(mu):
    return 2.0 * math.asinh(math.sqrt(mu) / 2.0)   # inverse Korrelationslaenge, cosh(kappa) = 1 + mu/2


def ell_regel(mu, p):
    return max(p['ell_min'], int(math.ceil(p['ell_faktor'] / kappa_von_mu(mu))))


def kette_korrelationen(mu, ell):
    """Unendliche Kette, omega_q^2 = mu + 4 sin^2(q/2): X_r, P_r fuer r < ell (Ring mit nq >= 64 ell Plaetzen)."""
    nq = 1 << max(14, int(math.ceil(math.log2(64 * ell))))
    q = 2.0 * np.pi * np.arange(nq) / nq
    om = np.sqrt(mu + 4.0 * np.sin(q / 2.0) ** 2)
    X = np.fft.rfft(0.5 / om).real[:ell] / nq
    Pc = np.fft.rfft(0.5 * om).real[:ell] / nq
    return X, Pc, nq


def s1_peschel(mu, ell):
    """Block aus ell Plaetzen in der unendlichen Kette hat zwei Raender: S_half = S_block / 2."""
    X, Pc, nq = kette_korrelationen(mu, ell)
    return 0.5 * s_block(linalg.toeplitz(X), linalg.toeplitz(Pc)), nq


def s1_ctm(mu):
    """Gegenprobe [M-Hypothese]: eps_j = (2j+1) eps, eps = pi K(k')/K(k), k = kleinere Wurzel von k + 1/k = 2 + M^2."""
    M = math.sqrt(mu)
    lam = ((math.sqrt(mu + 4.0) - M) / 2.0) ** 2
    kp2 = (1.0 - lam) * (1.0 + lam)
    Kk = special.ellipk(lam * lam) if lam < 0.5 else special.ellipkm1(kp2)
    Kkp = special.ellipk(kp2) if kp2 < 0.5 else special.ellipkm1(lam * lam)
    eps = math.pi * Kkp / Kk
    s, j = 0.0, 0
    while True:
        x = (2 * j + 1) * eps
        if x > 700:
            break
        term = x / math.expm1(x) - math.log1p(-math.exp(-x))
        s += term
        if term < 1e-17 * s:
            break
        j += 1
    return s, eps


def modus_s1(od, p):
    t0 = time.time()
    nx = p['nx']
    xs = np.linspace(X0, X1, nx)
    mus = np.exp(xs)
    S = np.empty(nx); ells = np.empty(nx, int); nqs = np.empty(nx, int); ctm = np.empty(nx); eps = np.empty(nx)
    for i, mu in enumerate(mus):
        ells[i] = ell_regel(mu, p)
        S[i], nqs[i] = s1_peschel(mu, int(ells[i]))
        ctm[i], eps[i] = s1_ctm(mu)
    t_gitter = time.time() - t0
    # Laengenprobe: jede probe_schritt-te Stuetzstelle mit probe_faktor-facher Laenge
    idx = list(range(0, nx, p['probe_schritt']))
    if idx[-1] != nx - 1:
        idx.append(nx - 1)
    probe = []
    for i in idx:
        ell2 = int(math.ceil(p['probe_faktor'] * ells[i]))
        s2, _ = s1_peschel(mus[i], ell2)
        probe.append(dict(i=i, mu=float(mus[i]), M=float(math.sqrt(mus[i])), ell=int(ells[i]), ell2=ell2,
                          S=float(S[i]), S2=float(s2), rel=float(abs(s2 - S[i]) / S[i])))
    # Kartenmassen genau
    karte = []
    for m in MASSEN:
        mu = m * m
        ell = ell_regel(mu, p)
        s, _ = s1_peschel(mu, ell)
        s2, _ = s1_peschel(mu, int(math.ceil(p['probe_faktor'] * ell)))
        c, e = s1_ctm(mu)
        karte.append(dict(m=m, S1=float(s), S1_lang=float(s2), ell=ell, ctm=float(c), eps=float(e)))
    # Splineprobe (ln S gegen ln mu): Mittelpunkte zwischen Stuetzstellen, direkt gerechnet
    cs = CubicSpline(xs, np.log(S))
    sp = []
    for i in range(5, nx - 1, 10):
        xm = 0.5 * (xs[i] + xs[i + 1])
        mu = math.exp(xm)
        s, _ = s1_peschel(mu, ell_regel(mu, p))
        sv = float(np.exp(cs(xm)))
        sp.append(dict(mu=mu, S=float(s), spline=sv, rel=float(abs(sv - s) / s)))
    # Steigung D = 1 gegen ln m
    sel = xs <= math.log(1e-2) + 1e-9            # M in [0,01; 0,1]
    lnM = xs[sel] / 2.0
    steig_lsq = float(np.polyfit(lnM, S[sel], 1)[0])
    steig_sek = float((karte[0]['S1'] - karte[1]['S1']) / (math.log(0.01) - math.log(0.1)))
    out = dict(x=xs.tolist(), mu=mus.tolist(), S=S.tolist(), ell=ells.tolist(), nq=nqs.tolist(),
               ctm=ctm.tolist(), eps=eps.tolist(),
               ctm_maxrel=float(np.max(np.abs(ctm - S) / S)), ctm_maxabs=float(np.max(np.abs(ctm - S))),
               laengenprobe=probe, laengenprobe_maxrel=float(max(q['rel'] for q in probe)),
               karte=karte, splineprobe=sp, splineprobe_maxrel=float(max(q['rel'] for q in sp)),
               steigung_lsq=steig_lsq, steigung_lsq_n=int(sel.sum()), steigung_sekante=steig_sek,
               parameter=p, zeit_gitter_s=t_gitter, zeit_s=time.time() - t0)
    json.dump(out, open(os.path.join(od, 's1.json'), 'w'), indent=1)
    return time.time() - t0


# ---------- direkte Gitterrechnung gegen Zerlegung ----------

def ring_K(Lp):
    K = 2.0 * np.eye(Lp)
    for i in range(Lp):
        K[i, (i + 1) % Lp] -= 1.0
        K[i, (i - 1) % Lp] -= 1.0
    return K


def kette_K(L1):
    """Dirichlet-Kette (Glieder zu festem phi = 0 an beiden Enden): tridiag(-1, 2, -1)."""
    return 2.0 * np.eye(L1) - np.eye(L1, k=1) - np.eye(L1, k=-1)


def gitter_K0(D, L1, Lp):
    K1, Kr, I1, Ip = kette_K(L1), ring_K(Lp), np.eye(L1), np.eye(Lp)
    if D == 2:
        return np.kron(K1, Ip) + np.kron(I1, Kr)
    if D == 3:
        return (np.kron(np.kron(K1, Ip), Ip) + np.kron(np.kron(I1, Kr), Ip) + np.kron(np.kron(I1, Ip), Kr))
    raise ValueError(D)


def s_aus_eig(e, V, nA):
    VA = V[:nA, :]
    XA = 0.5 * (VA * e ** -0.5) @ VA.T
    PA = 0.5 * (VA * e ** 0.5) @ VA.T
    return s_block(0.5 * (XA + XA.T), 0.5 * (PA + PA.T))


def modus_direkt(od, p):
    t0 = time.time()
    res = []
    for D, (L1, Lp) in [(2, p['direkt2']), (3, p['direkt3'])]:
        K0 = gitter_K0(D, L1, Lp)
        e0, V = linalg.eigh(K0)
        nA = (L1 // 2) * Lp ** (D - 1)          # Halbraum x_1 < L1/2 (x_1 ist der langsame Index)
        e1, U = linalg.eigh(kette_K(L1))
        ring = 2.0 - 2.0 * np.cos(2.0 * np.pi * np.arange(Lp) / Lp)
        Tk = ring if D == 2 else (ring[:, None] + ring[None, :]).ravel()
        for m in MASSEN:
            sdir = s_aus_eig(m * m + e0, V, nA)
            sk = np.array([s_aus_eig(m * m + T + e1, U, L1 // 2) for T in Tk])
            sdec = float(sk.sum())
            res.append(dict(D=D, L1=L1, Lp=Lp, m=m, S_direkt=float(sdir), S_zerlegung=sdec,
                            rel=float(abs(sdir - sdec) / sdir), je_randplatz=float(sdir / Lp ** (D - 1))))
    out = dict(ergebnisse=res, maxrel=float(max(r['rel'] for r in res)), parameter=p, zeit_s=time.time() - t0)
    json.dump(out, open(os.path.join(od, 'direkt.json'), 'w'), indent=1)
    return time.time() - t0


# ---------- S_D(m) ----------

def gl_gestuft(npan, nkn, kleinste):
    """Gauss-Legendre auf [0, pi], Paneele geometrisch zur 0 hin verfeinert (kleinstes Paneel = kleinste)."""
    q = (kleinste / np.pi) ** (1.0 / (npan - 1))
    b = np.concatenate([[0.0], np.pi * q ** np.arange(npan - 1, -1, -1)])
    xg, wg = np.polynomial.legendre.leggauss(nkn)
    kn = np.concatenate([0.5 * (c - a) * xg + 0.5 * (c + a) for a, c in zip(b[:-1], b[1:])])
    w = np.concatenate([0.5 * (c - a) * wg for a, c in zip(b[:-1], b[1:])])
    return kn, w


def modus_sd(od, p):
    t0 = time.time()
    s1 = json.load(open(os.path.join(od, 's1.json')))
    xs = np.array(s1['x']); ys = np.log(np.array(s1['S']))
    cs = CubicSpline(xs, ys)
    xf = np.linspace(xs[0], xs[-1], p['nfein']); yf = cs(xf)

    def f(mu):
        return np.exp(cs(np.log(mu)))

    gl = {}
    for name in ('gl_grob', 'gl_fein'):
        kn, w = gl_gestuft(p[name][0], p[name][1], p['gl_kleinste'])
        tk = 4.0 * np.sin(kn / 2.0) ** 2
        for m in MASSEN:
            s2 = float(np.sum(w * f(m * m + tk)) / np.pi)
            s3 = float(np.einsum('i,j,ij->', w, w, f(m * m + tk[:, None] + tk[None, :])) / np.pi ** 2)
            gl['%s_%g' % (name, m)] = [s2, s3]
    quad2 = {}
    for m in MASSEN:
        pts = [m, 10 * m] if 10 * m < math.pi else [m]
        val, err = integrate.quad(lambda k: float(f(m * m + 4.0 * math.sin(k / 2.0) ** 2)), 0.0, math.pi,
                                  points=pts, limit=400, epsabs=1e-14, epsrel=1e-12)
        quad2['%g' % m] = [val / math.pi, err / math.pi]
    t_det = time.time() - t0
    rng = np.random.default_rng(SEED)
    nb, npb = p['nb'], p['npb']
    bm = np.zeros((len(MASSEN), DMAX + 1, nb))
    for b in range(nb):
        k = rng.random((DMAX - 1, npb)) * np.pi
        np.cos(k, out=k); k *= -2.0; k += 2.0          # t_i = 2 - 2 cos k_i = 4 sin^2(k_i/2)
        np.cumsum(k, axis=0, out=k)                     # Zeile D-2: Summe der D-1 Querterme
        for im, m in enumerate(MASSEN):
            for D in range(2, DMAX + 1):
                y = np.interp(np.log(m * m + k[D - 2]), xf, yf)
                bm[im, D, b] = np.exp(y).mean()
    out = dict(gl=gl, quad2=quad2, batchmittel=bm.tolist(), nb=nb, npb=npb, seed=SEED, dmax=DMAX,
               parameter=p, zeit_det_s=t_det, zeit_s=time.time() - t0)
    json.dump(out, open(os.path.join(od, 'sd.json'), 'w'))
    return time.time() - t0


# ---------- Auswertung ----------

def affin_fit(x, y):
    A = np.vstack([np.ones_like(x), x]).T
    coef = np.linalg.lstsq(A, y, rcond=None)[0]
    fit = A @ coef
    return coef, fit, float(np.max(np.abs(y - fit) / y))


def dstern(y, Ds):
    j = int(np.argmax(y))
    Dst = int(Ds[j])
    rand = (j == 0) or (j == len(Ds) - 1)
    if not rand:
        ym, y0, yp = y[j - 1], y[j], y[j + 1]
        Dc = float(Dst + 0.5 * (ym - yp) / (ym - 2 * y0 + yp))
        r_minus, r_plus = float(math.exp(ym - y0)), float(math.exp(yp - y0))
    else:
        Dc, r_minus, r_plus = float('nan'), float('nan'), float('nan')
    band = Ds[y >= y[j] + math.log(0.9)]
    return dict(Dstern=Dst, Dstern_stetig=Dc, rand=bool(rand), S_tot_max=float(math.exp(y[j])),
                verh_minus1=r_minus, verh_plus1=r_plus, band90=[int(band.min()), int(band.max())],
                band90_zusammenhaengend=bool(len(band) == band.max() - band.min() + 1))


def modus_auswertung(od, p):
    t0 = time.time()
    s1 = json.load(open(os.path.join(od, 's1.json')))
    di = json.load(open(os.path.join(od, 'direkt.json')))
    sd = json.load(open(os.path.join(od, 'sd.json')))
    bm = np.array(sd['batchmittel']); nb = bm.shape[2]
    xs = np.array(s1['x']); cs = CubicSpline(xs, np.log(np.array(s1['S'])))
    nm = len(MASSEN)
    S = np.zeros((nm, DMAX + 1)); SE = np.zeros((nm, DMAX + 1)); quelle = {}
    mc = bm.mean(axis=2); mcse = bm.std(axis=2, ddof=1) / math.sqrt(nb) if nb > 1 else np.zeros_like(mc)
    kontrolle_mc = []
    for im, m in enumerate(MASSEN):
        S[im, 1] = s1['karte'][im]['S1']; SE[im, 1] = abs(s1['karte'][im]['S1_lang'] - s1['karte'][im]['S1'])
        gf = sd['gl']['gl_fein_%g' % m]; gg = sd['gl']['gl_grob_%g' % m]
        S[im, 2], S[im, 3] = gf; SE[im, 2], SE[im, 3] = abs(gf[0] - gg[0]), abs(gf[1] - gg[1])
        S[im, 4:] = mc[im, 4:]; SE[im, 4:] = mcse[im, 4:]
        for D in (2, 3):
            z = (mc[im, D] - S[im, D]) / mcse[im, D] if mcse[im, D] > 0 else float('nan')
            kontrolle_mc.append(dict(m=m, D=D, gl=S[im, D], mc=float(mc[im, D]), mc_se=float(mcse[im, D]), z=float(z)))
    quad_kontrolle = [dict(m=m, gl=float(S[im, 2]), quad=sd['quad2']['%g' % m][0],
                           rel=float(abs(S[im, 2] - sd['quad2']['%g' % m][0]) / S[im, 2])) for im, m in enumerate(MASSEN)]
    Ds = np.arange(1, DMAX + 1)
    mono = {}
    for im, m in enumerate(MASSEN):
        d = np.diff(S[im, 1:DTAB + 1])
        d_all = np.diff(S[im, 1:])
        mono['%g' % m] = dict(bis24=bool(np.all(d < 0)), bisDMAX=bool(np.all(d_all < 0)),
                              groesste_differenz_bis24=float(d.max()))
    # Schreibtisch-Vergleiche [D]: Gleichfoermigkeit (Jensen) und Grossmassen-Naeherung
    tab = []
    for im, m in enumerate(MASSEN):
        for D in range(1, DMAX + 1):
            w = m * m + 2.0 * D
            s_asym = (1.0 + math.log(16.0 * w * w)) / (16.0 * w * w)
            s_mittel = float(np.exp(cs(math.log(m * m + 2.0 * (D - 1))))) if D > 1 else S[im, 1]
            tab.append(dict(m=m, D=D, S=float(S[im, D]), SE=float(SE[im, D]), S_asym=s_asym,
                            verh_asym=float(S[im, D] / s_asym), verh_jensen=float(S[im, D] / s_mittel)))
    # S_tot und D*
    rng = np.random.default_rng(SEED + 1)
    boot_idx = [rng.integers(0, nb, nb) for _ in range(p['nboot'])]
    dst = []
    for im, m in enumerate(MASSEN):
        lnS = np.log(S[im, 1:])
        for e in N_EXP:
            lnN = e * math.log(10.0)
            y = (1.0 - 1.0 / Ds) * lnN + lnS
            r = dstern(y, Ds)
            gleich = 0
            for idx in boot_idx:
                Sb = S[im, 1:].copy()
                Sb[3:] = bm[im, 4:, :][:, idx].mean(axis=1)
                gleich += int(np.argmax((1.0 - 1.0 / Ds) * lnN + np.log(Sb)) + 1 == r['Dstern'])
            r.update(m=m, N_exp=e, lnN=lnN, boot_gleich=gleich, boot_n=len(boot_idx),
                     L_kante=float(10.0 ** (e / r['Dstern'])))
            dst.append(r)
    # Urteile
    lnNs = np.array([e * math.log(10.0) for e in N_EXP])
    fits = {}
    for im, m in enumerate(MASSEN):
        rr = [r for r in dst if r['m'] == m]
        di_int = np.array([r['Dstern'] for r in rr], float)
        di_c = np.array([r['Dstern_stetig'] for r in rr], float)
        c1, f1, mx1 = affin_fit(lnNs, di_int)
        fits['%g' % m] = dict(ganz=dict(a=float(c1[0]), b=float(c1[1]), fit=f1.tolist(), maxrel=mx1))
        if np.all(np.isfinite(di_c)):
            c2, f2, mx2 = affin_fit(lnNs, di_c)
            fits['%g' % m]['stetig'] = dict(a=float(c2[0]), b=float(c2[1]), fit=f2.tolist(), maxrel=mx2)
        fits['%g' % m]['prop_ganz_b'] = float(np.sum(di_int * lnNs) / np.sum(lnNs ** 2))
    vd0a = di['maxrel'] < 0.01
    sl, sk = s1['steigung_lsq'], s1['steigung_sekante']
    vd0b_plan = abs(sl / (-1.0 / 6.0) - 1.0) <= 0.05
    vd0b_karte = abs(sk / (-1.0 / 6.0) - 1.0) <= 0.05
    vd0c = all(v['bis24'] for v in mono.values())
    r106 = [r for r in dst if r['m'] == 0.1 and r['N_exp'] == 6][0]
    vd1 = r106['Dstern'] in (3, 4)
    f01 = fits['0.1']
    vd2_plan = ('stetig' in f01) and f01['stetig']['maxrel'] <= 0.10
    vd2_je_m = {k: v['ganz']['maxrel'] <= 0.10 for k, v in fits.items()}
    vals = list(vd2_je_m.values())
    vd2_karte = 'eingetroffen' if all(vals) else ('nicht eingetroffen' if not any(vals) else 'uneindeutig')
    jn = lambda b: 'eingetroffen' if b else 'nicht eingetroffen'
    urteile = dict(
        VD0=dict(plan=jn(vd0a and vd0b_plan and vd0c), karte=jn(vd0a and vd0b_karte and vd0c),
                 teil_a_zerlegung=vd0a, teil_a_maxrel=di['maxrel'], teil_b_plan=vd0b_plan, steigung_lsq=sl,
                 teil_b_karte=vd0b_karte, steigung_sekante=sk, teil_c_monoton=vd0c),
        VD1=dict(plan=jn(vd1), karte=jn(vd1), Dstern=r106['Dstern'], Dstern_stetig=r106['Dstern_stetig']),
        VD2=dict(plan=jn(vd2_plan), karte=vd2_karte, je_m_ganz=vd2_je_m))
    out = dict(S=S.tolist(), SE=SE.tolist(), tabelle=tab, monotonie=mono, kontrolle_mc=kontrolle_mc,
               quad_kontrolle=quad_kontrolle, dstern=dst, fits=fits, urteile=urteile,
               direkt=di['ergebnisse'], s1_kontrollen=dict(ctm_maxrel=s1['ctm_maxrel'], ctm_maxabs=s1['ctm_maxabs'],
               laengenprobe_maxrel=s1['laengenprobe_maxrel'], splineprobe_maxrel=s1['splineprobe_maxrel'],
               karte=s1['karte']), zeit_s=time.time() - t0)
    json.dump(out, open(os.path.join(od, 'auswertung.json'), 'w'), indent=1)
    # Textfassung
    L = []
    L.append('S_D(m), D = 1..%d (D=1 Peschel, D=2,3 GL gestuft, D>=4 MC; SE in Klammern)' % DTAB)
    for D in range(1, DTAB + 1):
        L.append('D=%2d  ' % D + '  '.join('m=%g: %.6e (%.1e)' % (m, S[im, D], SE[im, D]) for im, m in enumerate(MASSEN)))
    L.append('')
    L.append('D*(N, m):')
    for r in dst:
        L.append('m=%g N=1e%d D*=%d D*_stetig=%.3f rand=%s verh(-1)=%.5f verh(+1)=%.5f band90=%s L=%.3f boot=%d/%d'
                 % (r['m'], r['N_exp'], r['Dstern'], r['Dstern_stetig'], r['rand'], r['verh_minus1'], r['verh_plus1'],
                    r['band90'], r['L_kante'], r['boot_gleich'], r['boot_n']))
    L.append('')
    L.append('Fits: ' + json.dumps(fits))
    L.append('Urteile: ' + json.dumps(urteile))
    L.append('Monotonie: ' + json.dumps(mono))
    L.append('MC gegen GL: ' + json.dumps(kontrolle_mc))
    L.append('quad gegen GL (D=2): ' + json.dumps(quad_kontrolle))
    L.append('direkt: ' + json.dumps(di['ergebnisse']))
    L.append('S_1-Kontrollen: ' + json.dumps(out['s1_kontrollen']))
    open(os.path.join(od, 'auswertung.txt'), 'w').write('\n'.join(L) + '\n')
    return time.time() - t0


# ---------- Bild ----------

def modus_bild(od, p):
    t0 = time.time()
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    a = json.load(open(os.path.join(od, 'auswertung.json')))
    S = np.array(a['S']); SE = np.array(a['SE'])
    fig, ax = plt.subplots(1, 3, figsize=(17, 5.2))
    farben = {0.01: '#1f77b4', 0.1: '#d62728', 1.0: '#2ca02c'}
    Dt = np.arange(1, DTAB + 1)
    for im, m in enumerate(MASSEN):
        ax[0].errorbar(Dt, S[im, 1:DTAB + 1], yerr=SE[im, 1:DTAB + 1], fmt='o-', ms=3, color=farben[m], label='m = %g' % m)
    w = 0.01 + 2.0 * Dt
    ax[0].plot(Dt, (1 + np.log(16 * w * w)) / (16 * w * w), 'k--', lw=1, label='Grossmassen-Naeherung (m = 0,1)')
    ax[0].set_yscale('log'); ax[0].set_xlabel('Dimension D'); ax[0].set_ylabel('S_D(m) je Randplatz')
    ax[0].set_title('Verschraenkung je Randplatz (Halbraum)'); ax[0].legend(fontsize=8); ax[0].grid(alpha=0.3)
    Ds = np.arange(1, DMAX + 1)
    im01 = MASSEN.index(0.1)
    for e in N_EXP:
        y = (1.0 - 1.0 / Ds) * e * math.log(10.0) + np.log(S[im01, 1:])
        ax[1].plot(Ds, np.exp(y - y.max()), '-', lw=1.5, label='N = 10^%d' % e)
        j = int(np.argmax(y)); ax[1].plot([Ds[j]], [1.0], 'k.', ms=6)
    ax[1].set_xscale('log'); ax[1].set_xlabel('Dimension D'); ax[1].set_ylabel('S_tot(D) / S_tot(D*)')
    ax[1].set_title('Feste Punktzahl N, m = 0,1'); ax[1].set_ylim(0, 1.05); ax[1].legend(fontsize=8); ax[1].grid(alpha=0.3)
    lnNs = np.array([e * math.log(10.0) for e in N_EXP])
    for im, m in enumerate(MASSEN):
        rr = [r for r in a['dstern'] if r['m'] == m]
        ax[2].plot(lnNs, [r['Dstern'] for r in rr], 'o', color=farben[m], label='D* ganz, m = %g' % m)
        ax[2].plot(lnNs, [r['Dstern_stetig'] for r in rr], 'x', color=farben[m])
    xx = np.linspace(0, lnNs.max() * 1.03, 50)
    f01 = a['fits']['0.1']
    if 'stetig' in f01:
        ax[2].plot(xx, f01['stetig']['a'] + f01['stetig']['b'] * xx, '-', color='#d62728', lw=1,
                   label='affiner Fit (stetig, m = 0,1)')
    ax[2].plot(xx, xx / 2.0, 'k:', lw=1, label='(ln N)/2 (Karte, grob)')
    ax[2].set_xlabel('ln N'); ax[2].set_ylabel('D*'); ax[2].set_title('Lage des Maximums')
    ax[2].legend(fontsize=8); ax[2].grid(alpha=0.3)
    ins = ax[2].inset_axes([0.55, 0.08, 0.42, 0.35])
    for im, m in enumerate(MASSEN):
        rr = [r for r in a['dstern'] if r['m'] == m][:4]
        ins.plot(lnNs[:4], [r['Dstern'] for r in rr], 'o-', ms=3, color=farben[m])
    ins.set_title('N = 10^3 .. 10^12', fontsize=7); ins.tick_params(labelsize=7); ins.grid(alpha=0.3)
    fig.suptitle('VERSCHRAENK-DIM-1: freies Skalarfeld auf Z^D, Halbraum-Schnitt [E, .69]', fontsize=11)
    fig.tight_layout()
    fig.savefig(os.path.join(od, 'verschraenk-dim-1.png'), dpi=110)
    return time.time() - t0


def main():
    modus, od = sys.argv[1], sys.argv[2]
    os.makedirs(od, exist_ok=True)
    if modus == 'rauch':
        for name, fn in [('s1', modus_s1), ('direkt', modus_direkt), ('sd', modus_sd),
                         ('auswertung', modus_auswertung), ('bild', modus_bild)]:
            dt = fn(od, RAUCH)
            print('rauch %s ok, %.1f s' % (name, dt), flush=True)
        return
    fn = dict(s1=modus_s1, direkt=modus_direkt, sd=modus_sd, auswertung=modus_auswertung, bild=modus_bild)[modus]
    dt = fn(od, P)
    print('%s fertig, %.1f s' % (modus, dt), flush=True)


if __name__ == '__main__':
    main()
