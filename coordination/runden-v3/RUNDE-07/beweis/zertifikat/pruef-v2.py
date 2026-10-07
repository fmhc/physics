# BEWEIS-1 Treiber: Startwerte, Newton (nicht streng), strenge Punkt- und Kastenauswertung, Krawczyk-Brouwer-Pruefung.
# Aufruf auf der .69 ueber kleintest.sh:  pruef.py <modus> [optionen]
#   frei      : Selbsttest am freien Modell (f = 0), geschlossene Loesungen bekannt
#   start     : Profil-Startwert a per float-Schiessen (nur Startwert, nicht streng)
#   newton    : Newton auf H_0 = 0 in (a, c, rho, om) mit Kugelarithmetik-Mittelpunkten (nicht streng) -> z0.json
#   profil    : M1 strenge Profilhuelle (2x2-Krawczyk in (a, c) bei festem om)
#   punkt     : M2 strenge Huelle von H_0(z0) und F(z0) (inkl. Schwanzfehler)
#   kasten    : M3 Jacobi-Huelle DH_0 ueber den Kasten Z und Krawczyk-Brouwer-Test
import sys, json, time, math, hashlib, argparse, os
from flint import arb, acb, arb_mat, acb_mat, ctx
import bewkern as K

T0 = time.time()


def log(*a):
    print("[%7.1fs]" % (time.time() - T0), *a, flush=True)


def dy_str(x):
    """exakter Mittelpunkt als (Mantisse, Exponent)-Strings"""
    m, e = x.mid().man_exp()
    return [str(int(m)), str(int(e))]


def dy_arb(p):
    m, e = int(p[0]), int(p[1])
    x = arb(m) * arb(2) ** e
    assert x.is_exact()
    return x


def dy_float(x, bits=60):
    """runde float/arb-Mittelpunkt auf dyadische Zahl mit bits Nachkommabits"""
    v = float(x) if not isinstance(x, arb) else float(x.mid())
    return arb(round(v * 2 ** bits)) / arb(2) ** bits


def arb_round(x, bits):
    """dyadische Rundung eines arb-Mittelpunkts auf bits Nachkommabits (exakt)"""
    m, e = x.mid().man_exp()
    m, e = int(m), int(e)
    if e >= -bits:
        return arb(m) * arb(2) ** e
    sh = -bits - e
    m2 = (m + (1 << (sh - 1))) >> sh
    return arb(m2) * arb(2) ** (-bits)


# ------------------------------------------------------------------ Auswertung H_0 und DH_0
def consts(L, khat_f, kap0_f, kapc_f):
    s1 = arb_round(arb(L) * (arb(kap0_f) * L).exp(), 20)
    s3 = arb_round((-arb(kapc_f) * L).exp(), 200)
    return s1, s3


def evalH(z, L, N, jets, s1, s3, khat, logf=None, N0=None, Rmax=1.0, qfac=4):
    a, c, rho, om = z
    par = K.Par(a, rho, om, khat)
    st, infos, _ = K.integrate(par, L, N, jets, N0=N0, Rmax=Rmax, qfac=qfac, log=logf)
    kap0 = par.kap0sq.sqrt()
    kapc = par.kapcsq.sqrt()
    E0 = (-kap0 * L).exp()
    Y = st['Y']
    H = [s1 * (st['f'] - c * E0 / L),
         s1 * (st['g'] + c * (kap0 + arb(1) / L) * E0 / L),
         s3 * (Y[3, 0] + kapc * Y[2, 0]),
         s3 * (Y[3, 1] + kapc * Y[2, 1])]
    DH = None
    if jets:
        dE0w = E0 * L * om / kap0
        dkap0w = -om / kap0
        dkcr = (om - rho) / kapc
        dkcw = -(om - rho) / kapc
        z0 = arb(0)
        DH = arb_mat([
            [s1 * st['pa'], -s1 * E0 / L, z0, s1 * (st['pw'] - c * dE0w / L)],
            [s1 * st['qa'], s1 * (kap0 + arb(1) / L) * E0 / L, z0,
             s1 * (st['qw'] + c * (dkap0w * E0 + (kap0 + arb(1) / L) * dE0w) / L)],
            [s3 * (Y[3, 2] + kapc * Y[2, 2]), z0, s3 * (Y[3, 4] + kapc * Y[2, 4] + dkcr * Y[2, 0]),
             s3 * (Y[3, 6] + kapc * Y[2, 6] + dkcw * Y[2, 0])],
            [s3 * (Y[3, 3] + kapc * Y[2, 3]), z0, s3 * (Y[3, 5] + kapc * Y[2, 5] + dkcr * Y[2, 1]),
             s3 * (Y[3, 7] + kapc * Y[2, 7] + dkcw * Y[2, 1])]])
    return H, DH, st, infos, par


# ------------------------------------------------------------------ Schwanzlemmata (streng)
def tail_E(z, L, s1, s3, st, khat):
    """Schranken fuer E = H - H_0 aus Lemma P (Profilschwanz) und Lemma J (Jost-Loesung).
    z: Kugeln ueber den Kasten; st: Zustand bei L (Kugeln ueber den Kasten)."""
    a, c, rho, om = z
    L = arb(L)
    kap0 = (1 - om * om).sqrt()
    E0 = (-kap0 * L).exp()
    E02 = (-2 * kap0 * L).exp()
    cab = abs(c).upper()
    # Lemma P
    fs0 = (cab * arb(101) / 100) * E0 / L                     # Kandidat fuer sup |f| auf [L, oo)
    Kc = (2 + K.C15 * fs0 * fs0) * E02 / (4 * kap0 * kap0 * L * L)
    eta = 2 * Kc * cab ** 3
    m = cab + eta
    fstar = m * E0 / L
    okP = bool((fstar <= fs0) and (Kc * m ** 3 <= eta))
    Lip = (6 + K.C75 * fs0 * fs0) * m * m * E02 / (4 * kap0 * kap0 * L * L)
    okP = okP and bool(Lip < 1) and bool(c.lower() > eta.upper())   # c > eta: Positivitaet des Schwanzes
    eta0 = Kc * m ** 3
    E1 = s1 * E0 * eta0 / L
    E2 = s1 * E0 * (2 * kap0 * eta0 / L + eta0 / (L * L))
    # Lemma J
    k = ((om + rho) ** 2 - 1).sqrt()
    kapc = (1 - (om - rho) ** 2).sqrt()
    QL = (6 + K.C75 * fs0 * fs0) * m * m * E02 / (2 * kap0 * L * L)
    mu = arb(max((1 / k).upper(), (1 / (2 * kapc)).upper()))
    eps = (mu * QL).exp() - 1
    EA = eps / (mu * k)
    EB = eps / (2 * mu * kapc)
    EAp = ((1 + kapc * kapc / (k * k)).sqrt() + kapc / k) * eps / mu
    EBp = K.C15 * eps / mu
    Y = st['Y']
    sL, cL = (khat * L).sin_cos()
    out = [E1, E2]
    for j in (0, 1):
        al, be, B, Bp = Y[0, j], Y[1, j], Y[2, j], Y[3, j]
        A = al * cL + be * sL
        Ap = khat * (-al * sL + be * cL)
        W = EA * abs(Ap) + EB * abs(Bp) + EAp * abs(A) + EBp * abs(B)
        out.append(s3 * W)
    info = {'Lemma_P_ok': okP, 'eta': eta.upper(), 'Lip': Lip.upper(), 'fstar': fstar.upper(), 'QL': QL.upper(),
            'eps_J': eps.upper(), 'EA': EA.upper(), 'EB': EB.upper(), 'EAp': EAp.upper(), 'EBp': EBp.upper(),
            'phibar_fs0': fs0.upper(), 'Km3_eta0': eta0.upper(), 'K': Kc.upper(), 'm': m.upper(),
            'c_minus_eta_lower': (c.lower() - eta.upper()).lower(), 'mu': mu,
            'K_J': (1 + eps / (mu * k) + eps / (2 * mu * kapc)).upper()}
    return [x.upper() for x in out], info


# ------------------------------------------------------------------ float-Startwert fuer a
def shoot_float(a, w2, rmax=30.0, h=0.005):
    k2 = 1 - w2

    def rhs(r, f, g):
        return g, f * (k2 - 2 * f * f + 1.5 * f ** 4) - 2 * g / r
    r = 1e-4
    N0 = a * (k2 - 2 * a * a + 1.5 * a ** 4)
    f = a + N0 * r * r / 6
    g = N0 * r / 3
    while r < rmax:
        k1 = rhs(r, f, g)
        k2_ = rhs(r + h / 2, f + h / 2 * k1[0], g + h / 2 * k1[1])
        k3 = rhs(r + h / 2, f + h / 2 * k2_[0], g + h / 2 * k2_[1])
        k4 = rhs(r + h, f + h * k3[0], g + h * k3[1])
        f += h / 6 * (k1[0] + 2 * k2_[0] + 2 * k3[0] + k4[0])
        g += h / 6 * (k1[1] + 2 * k2_[1] + 2 * k3[1] + k4[1])
        r += h
        if f < 0:
            return +1, r, f, g
        if g > 0:
            return -1, r, f, g
    return 0, r, f, g


def start_a(w2):
    lo, hi = 0.3, math.sqrt((2 + math.sqrt(4 - 6 * (1 - w2))) / 3) - 1e-9
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        s, r, f, g = shoot_float(mid, w2)
        if s > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def c_from_float(a, w2, r_eval=14.0, h=0.002):
    k2 = 1 - w2
    kap0 = math.sqrt(k2)

    def rhs(r, f, g):
        return g, f * (k2 - 2 * f * f + 1.5 * f ** 4) - 2 * g / r
    r = 1e-4
    N0 = a * (k2 - 2 * a * a + 1.5 * a ** 4)
    f = a + N0 * r * r / 6
    g = N0 * r / 3
    while r < r_eval:
        k1 = rhs(r, f, g)
        k2_ = rhs(r + h / 2, f + h / 2 * k1[0], g + h / 2 * k1[1])
        k3 = rhs(r + h / 2, f + h / 2 * k2_[0], g + h / 2 * k2_[1])
        k4 = rhs(r + h, f + h * k3[0], g + h * k3[1])
        f += h / 6 * (k1[0] + 2 * k2_[0] + 2 * k3[0] + k4[0])
        g += h / 6 * (k1[1] + 2 * k2_[1] + 2 * k3[1] + k4[1])
        r += h
    return f * r * math.exp(kap0 * r)


def mat_mid(M):
    return M.mid()


def solve_mid(DH, H):
    """Newton-Schritt mit Mittelpunkten"""
    A = DH.mid()
    b = arb_mat([[h.mid()] for h in H])
    return A.solve(b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus')
    ap.add_argument('--prec', type=int, default=256)
    ap.add_argument('--L', type=int, default=40)
    ap.add_argument('--N', type=int, default=64)
    ap.add_argument('--N0', type=int, default=0)
    ap.add_argument('--Rmax', type=float, default=1.0)
    ap.add_argument('--q', type=int, default=4)
    ap.add_argument('--z', default='z0.json')
    ap.add_argument('--out', default='')
    ap.add_argument('--iters', type=int, default=6)
    ap.add_argument('--delta', default='')
    ap.add_argument('--Ls', default='')
    ap.add_argument('--Nbox', type=int, default=40)
    ap.add_argument('--Lz', type=int, default=0)
    ap.add_argument('--kfak', default='8')
    args = ap.parse_args()
    ctx.prec = args.prec
    log("modus", args.modus, "prec", ctx.prec, "L", args.L, "N", args.N)
    N0 = args.N0 or None
    if args.modus == 'frei':
        # f = 0: R1 = (sin(k r)/k, 0), R2 = (0, sinh(kc r)/kc)
        rho = arb('1.7446175448365042')
        om = arb('0.8931275313')
        khat = dy_float(((om + rho) ** 2 - 1).sqrt(), 40)
        par = K.Par(arb(0), rho, om, khat)
        st, infos, _ = K.integrate(par, args.L, args.N, False, N0=N0, Rmax=args.Rmax, qfac=args.q, log=log)
        k = par.ksq.sqrt()
        kc = par.kapcsq.sqrt()
        L = arb(args.L)
        sL, cL = (khat * L).sin_cos()
        Y = st['Y']
        A = Y[0, 0] * cL + Y[1, 0] * sL
        Ap = khat * (-Y[0, 0] * sL + Y[1, 0] * cL)
        log("Schritte", len(infos))
        log("A1(L)  ", A.str(25, radius=True), " exakt", ((k * L).sin() / k).str(25))
        log("A1'(L) ", Ap.str(25, radius=True), " exakt", ((k * L).cos()).str(25))
        log("B2(L)  ", Y[2, 1].str(25, radius=True), " exakt", ((kc * L).sinh() / kc).str(25))
        log("B2'(L) ", Y[3, 1].str(25, radius=True), " exakt", ((kc * L).cosh()).str(25))
        log("B1(L)", Y[2, 0].str(5, radius=True), " A2(L)", (Y[0, 1] * cL + Y[1, 1] * sL).str(5, radius=True))
        ok = (A.overlaps((k * L).sin() / k) and Ap.overlaps((k * L).cos()) and Y[2, 1].overlaps((kc * L).sinh() / kc)
              and Y[3, 1].overlaps((kc * L).cosh()))
        log("FREI-TEST", "BESTANDEN" if ok else "NICHT BESTANDEN")
        return
    if args.modus == 'start':
        w2 = 0.7976767871108792
        a = start_a(w2)
        c = c_from_float(a, w2)
        log("a_float", repr(a), "c_float", repr(c))
        rho = 1.7446175448365042
        om = math.sqrt(w2)
        khat_f = math.sqrt((om + rho) ** 2 - 1)
        kap0_f = math.sqrt(1 - w2)
        kapc_f = math.sqrt(1 - (om - rho) ** 2)
        d = {'a': dy_str(dy_float(a, 55)), 'c': dy_str(dy_float(c, 50)), 'rho': dy_str(dy_float(rho, 55)),
             'om': dy_str(dy_float(om, 55)), 'khat': dy_str(dy_float(khat_f, 40)),
             'kap0_f': kap0_f, 'kapc_f': kapc_f, 'L': args.L, 'quelle': 'float-Schiessen + Codex-Punkt'}
        with open(args.out or 'z_start.json', 'w') as fh:
            json.dump(d, fh, indent=1)
        log("geschrieben", args.out or 'z_start.json')
        return
    d = json.load(open(args.z))
    z = [dy_arb(d[k]) for k in ('a', 'c', 'rho', 'om')]
    khat = dy_arb(d['khat'])
    L = args.L
    s1, s3 = consts(L, float(khat), d['kap0_f'], d['kapc_f'])
    if args.modus == 'newton':
        Ls = [int(x) for x in args.Ls.split(',')] if args.Ls else [L]
        for LL in Ls:
            s1, s3 = consts(LL, float(khat), d['kap0_f'], d['kapc_f'])
            for it in range(args.iters):
                t1 = time.time()
                H, DH, st, infos, par = evalH(z, LL, args.N, True, s1, s3, khat, N0=N0, Rmax=args.Rmax, qfac=args.q)
                dz = solve_mid(DH, H)
                log("L", LL, "it", it, "Schritte", len(infos), "Zeit %.1fs" % (time.time() - t1),
                    "H", [h.mid().str(5) for h in H])
                log("   dz", [dz[i, 0].str(5) for i in range(4)])
                log("   Radien H", [h.rad().str(3) for h in H], "tail_max", max(i["tail_max"] for i in infos).str(3), stepstats(infos))
                z = [arb_round(z[i] - dz[i, 0], 200) for i in range(4)]
                log("   z", [x.str(30) for x in z])
                if max(abs(dz[i, 0]).upper() for i in range(4)) < arb(10) ** -26:
                    break
        d2 = dict(d)
        for kk, x in zip(('a', 'c', 'rho', 'om'), z):
            d2[kk] = dy_str(x)
        d2['L'] = Ls[-1]
        d2['quelle'] = 'Newton (nicht streng) auf H_0, Ls=%s, N=%d, prec=%d' % (Ls, args.N, ctx.prec)
        with open(args.out or 'z0.json', 'w') as fh:
            json.dump(d2, fh, indent=1)
        log("geschrieben", args.out or 'z0.json', "x = om^2 =", (z[3] * z[3]).str(30))
        return
    if args.modus == 'zert':
        zert(args, d, z, khat, N0)
        return
    if args.modus == 'kontrolle':
        kontrolle(args, d, z, khat, N0)
        return
    if args.modus == 'satz':
        # Intervalle des Satzes aus einem Zertifikat (streng: Kasten Z = z0 +- delta, delta aufgerundet)
        zj = json.load(open(args.out))
        names = ('a', 'c', 'rho', 'om')
        dl = [arb(s).upper() for s in zj['delta']]
        Zb = [z[i] + arb(0, dl[i]) for i in range(4)]
        for i in range(4):
            log("%-4s in" % names[i], Zb[i].str(40, radius=True), " delta <=", dl[i].str(5))
        x = Zb[3] * Zb[3]
        log("om^2 in", x.str(40, radius=True))
        log("1 - om in", (1 - Zb[3]).str(12, radius=True), " 1 + om in", (1 + Zb[3]).str(12, radius=True))
        log("k = sqrt((om+rho)^2-1) in", ((Zb[3] + Zb[2]) ** 2 - 1).sqrt().str(20, radius=True))
        log("kappa_c in", (1 - (Zb[3] - Zb[2]) ** 2).sqrt().str(20, radius=True),
            " kappa0 in", (1 - x).sqrt().str(20, radius=True))
        return
    log("unbekannter Modus")


def stepstats(infos):
    Rs = [float(i["R"]) for i in infos]
    return "Fehlversuche=%d R_min=%.4f R_max=%.4f" % (sum(i.get("nfail", 0) for i in infos), min(Rs), max(Rs))


def ivec(v):
    return arb_mat([[x] for x in v])


def zeilenschranke(Mk, delta, n, gewichtet=True):
    """Streng: je Zeile obere Schranke (exakte Zahl) von sum_j |Mk_ij| delta_j / delta_i (bzw. ungewichtet);
    das Maximum wird ueber exakte Zahlen gebildet (Vergleiche entscheidbar), Auflage K5 der Code-Lesung."""
    werte = []
    for i in range(n):
        s = arb(0)
        for j in range(n):
            s += abs(Mk[i, j]).upper() * (delta[j] if gewichtet else 1)
        werte.append((s / delta[i]).upper() if gewichtet else s.upper())
    m = werte[0]
    for w in werte[1:]:
        if w > m:
            m = w
    return m


def sha256_datei(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def arb_fraction(x):
    """exakte Umwandlung eines exakten arb (Dyadik) in Fraction (nur Protokoll)"""
    from fractions import Fraction
    m, e = x.mid().man_exp()
    m, e = int(m), int(e)
    return Fraction(m * 2 ** e) if e >= 0 else Fraction(m, 2 ** (-e))


def erster_schritt(infs):
    """Angenommener erster Schritt (Reihe um 0) und die Folge der Startversuche, nachgebildet mit bewkern.dyf
    wie in bewkern.integrate (R0 = 1, je Fehlschlag R -> dyf(4/5 R, 8))."""
    from fractions import Fraction
    Racc = arb_fraction(infs[0]['R'])
    folge = [Fraction(1)]
    R = Fraction(1)
    while R > Racc:
        R = K.dyf(R * Fraction(4, 5), 8)
        folge.append(R)
    return {'R_angenommen': str(Racc), 'h0': str(infs[0]['r_end']), 'q': str(arb_fraction(infs[0]['h']) / Racc),
            'versuchsfolge_R': [str(x) for x in folge], 'verkleinerungen': len(folge) - 1,
            'folge_trifft_R_angenommen': folge[-1] == Racc, 'inflationsrunden': infs[0]['nit'],
            'rest': infs[0]['tail_max'].str(6)}


def positivity(infos, kap0sq):
    """Lemma Pos: f > 0 auf [0, Lp] aus A-priori-Huellen, danach |f| < sqrt(S_-) bis L."""
    from fractions import Fraction
    Sm = (2 - (4 - 6 * kap0sq).sqrt()) / 3
    thr = Sm.sqrt().lower()
    Lp = None
    prev_end = Fraction(0)
    ok_small = True
    for inf in infos:
        if Lp is None:
            if inf['f_lo'] > 0:
                prev_end = inf['r_end']
                continue
            Lp = prev_end
        if not (inf['f_hi'] < thr and inf['f_lo'] > -thr):
            ok_small = False
    return {'Lp': float(Lp) if Lp is not None else 'L', 'klein_danach': ok_small, 'schwelle': thr.str(10)}


def zert(args, d, z0, khat, N0):
    """M1-M3 in einem Lauf. z0 exakt dyadisch."""
    L = args.Lz or d['L']
    s1, s3 = consts(L, float(khat), d['kap0_f'], d['kapc_f'])
    out = {'L': L, 'prec': ctx.prec, 'z0': {k: dy_str(x) for k, x in zip(('a', 'c', 'rho', 'om'), z0)},
           'khat': dy_str(khat), 's1': dy_str(s1), 's3': dy_str(s3)}
    # Selbstbeschreibung (Auflage K3/K4 der Code-Lesung): Laufparameter und volle sha256
    import glob, flint as _fl
    out['parameter'] = {'L': L, 'Lz': args.Lz, 'N_punkt': args.N, 'N_kasten': args.Nbox,
                        'N0': (N0 if N0 else '2N (Standard in bewkern.integrate)'), 'q': '1/%d' % args.q,
                        'Rmax': args.Rmax, 'rfrac': '1/2 (Standard in bewkern.integrate)',
                        'R0_Startversuch': '1 (Standard in bewkern.integrate)', 'kfak': args.kfak,
                        'prec': ctx.prec, 'z_datei': args.z, 'kommandozeile': ' '.join(sys.argv)}
    hs = {'bewkern.py': sha256_datei(os.path.abspath(K.__file__)), 'pruef.py': sha256_datei(os.path.abspath(__file__)),
          args.z: sha256_datei(args.z)}
    exe = os.path.realpath(sys.executable)
    hs['interpreter ' + exe] = sha256_datei(exe)
    fdir = os.path.dirname(os.path.abspath(_fl.__file__))
    for p in sorted(glob.glob(os.path.join(fdir, '*.so')) +
                    glob.glob(os.path.join(os.path.dirname(fdir), 'python_flint.libs', '*'))):
        hs[os.path.basename(p)] = sha256_datei(p)
    out['sha256'] = hs
    log("sha256:", hs)
    # 1) strenge Punktauswertung H_0(z0)
    t1 = time.time()
    Hp, _, stp, infp, parp = evalH(z0, L, args.N, False, s1, s3, khat, N0=N0, Rmax=args.Rmax, qfac=args.q)
    out['zeit_punkt_s'] = time.time() - t1
    log("Punkt: Schritte", len(infp), "Zeit %.1fs" % out['zeit_punkt_s'])
    for i in range(4):
        log("  H0_%d(z0) =" % (i + 1), Hp[i].str(8, radius=True))
    # 2) Jacobi-Matrix am Punkt (fuer Y und Vorschaetzung), Jets, kleinere Ordnung
    t1 = time.time()
    _, DHp, stj, infj, _ = evalH(z0, L, args.Nbox, True, s1, s3, khat, N0=N0, Rmax=args.Rmax, qfac=args.q)
    out['zeit_jac_punkt_s'] = time.time() - t1
    log("Jacobi am Punkt: Zeit %.1fs" % out['zeit_jac_punkt_s'])
    Ym = DHp.mid().inv().mid()          # exakte dyadische Matrix (Mittelpunkte)
    Y = arb_mat([[arb_round(Ym[i, j], 300) for j in range(4)] for i in range(4)])
    for i in range(4):
        log("  DH row", i, [DHp[i, j].str(6) for j in range(4)])
    # 3) Vorschaetzung der Schwanzschranken mit Punktzustand, Kastenradien
    zb = [arb(z0[i]) for i in range(4)]
    eps0, einfo0 = tail_E(zb, L, s1, s3, stp, khat)
    YH = Y * ivec(Hp)
    absY = arb_mat([[abs(Y[i, j]) for j in range(4)] for i in range(4)])
    YE = absY * ivec([arb(e) for e in eps0])
    fac = arb(args.kfak)
    delta = []
    for i in range(4):
        r = abs(YH[i, 0]).upper() + YE[i, 0].upper()
        dl = arb_round(fac * r + abs(z0[i]) * arb(2) ** -180, 400)
        delta.append(dl.upper())
    if args.delta:
        delta = [arb(x) for x in args.delta.split(',')]
    log("Kastenradien delta", [x.str(4) for x in delta])
    out['delta'] = [x.str(20) for x in delta]
    out['eps_vorschaetzung'] = [e.str(6) for e in eps0]
    # 4) Kastenauswertung DH_0(Z)
    Zb = [z0[i] + arb(0, delta[i]) for i in range(4)]
    t1 = time.time()
    _, DHZ, stZ, infZ, parZ = evalH(Zb, L, args.Nbox, True, s1, s3, khat, N0=N0, Rmax=args.Rmax, qfac=args.q)
    out['zeit_kasten_s'] = time.time() - t1
    log("Kasten: Schritte", len(infZ), "Zeit %.1fs" % out['zeit_kasten_s'])
    for i in range(4):
        log("  DHZ row", i, [DHZ[i, j].str(6, radius=True) for j in range(4)])
    # 5) Schwanzschranken ueber Z
    eps, einfo = tail_E(Zb, L, s1, s3, stZ, khat)
    log("Lemma P/J ueber Z:", einfo)
    log("eps", [e.str(5) for e in eps])
    out['eps'] = [e.str(10) for e in eps]
    out['lemma_info'] = {k: (v.str(20) if isinstance(v, arb) else v) for k, v in einfo.items()}
    # 6) Krawczyk-Brouwer 4x4
    I4 = arb_mat([[1 if i == j else 0 for j in range(4)] for i in range(4)])
    Mk = I4 - Y * DHZ
    dZ = ivec([arb(0, delta[i]) for i in range(4)])
    Eb = ivec([arb(0, eps[i]) for i in range(4)])
    Kr = ivec(z0) - YH + Mk * dZ + absY * Eb
    rowsum = zeilenschranke(Mk, delta, 4, True)
    ok = True
    for i in range(4):
        inside = bool(Kr[i, 0].lower() > z0[i] - delta[i]) and bool(Kr[i, 0].upper() < z0[i] + delta[i])
        ok = ok and inside
        log("  K_%d" % i, Kr[i, 0].str(12, radius=True), "Kasten", (z0[i] + arb(0, delta[i])).str(12, radius=True),
            "innen" if inside else "NICHT innen")
    log("gewichtete Zeilensumme max_i sum_j |I - Y DH(Z)|_ij delta_j / delta_i <=", rowsum.str(6))
    ok = ok and bool(rowsum < 1)
    # Positivitaet und Kanalbedingungen
    pos = positivity(infZ, parZ.kap0sq)
    kan = {'k2>0': bool(parZ.ksq > 0), 'kapc2>0': bool(parZ.kapcsq > 0), 'om>1/sqrt2': bool(2 * Zb[3] ** 2 > 1),
           'om<1': bool(Zb[3] < 1)}
    log("Positivitaet:", pos, "Kanaele:", kan)
    okP = einfo['Lemma_P_ok']
    ok_all = ok and okP and pos['klein_danach'] and all(kan.values())
    out['M3'] = {'Krawczyk_in_Z': ok, 'rowsum': rowsum.str(8), 'Lemma_P_ok': okP, 'positiv': pos, 'kanaele': kan,
                 'K': [Kr[i, 0].str(25, radius=True) for i in range(4)], 'BESTANDEN': ok_all}
    log("M3 (Existenz 4x4):", "BESTANDEN" if ok_all else "NICHT BESTANDEN")
    # M1: 2x2 in (a, c) bei om = om0 (Unterkasten, Daten aus Z gelten weiter)
    Dp = arb_mat([[DHp[i, j].mid() for j in (0, 1)] for i in (0, 1)])
    Yp = Dp.inv().mid()
    Yp = arb_mat([[arb_round(Yp[i, j], 300) for j in range(2)] for i in range(2)])
    Hp2 = ivec([Hp[0], Hp[1]])
    D2 = arb_mat([[DHZ[i, j] for j in (0, 1)] for i in (0, 1)])
    I2 = arb_mat([[1, 0], [0, 1]])
    absYp = arb_mat([[abs(Yp[i, j]) for j in range(2)] for i in range(2)])
    Kp = ivec([z0[0], z0[1]]) - Yp * Hp2 + (I2 - Yp * D2) * ivec([arb(0, delta[0]), arb(0, delta[1])]) + \
        absYp * ivec([arb(0, eps[0]), arb(0, eps[1])])
    MI2 = I2 - Yp * D2
    rs2 = zeilenschranke(MI2, delta, 2, True)
    ok1 = all(bool(Kp[i, 0].lower() > z0[i] - delta[i]) and bool(Kp[i, 0].upper() < z0[i] + delta[i]) for i in range(2))
    ok1 = ok1 and bool(rs2 < 1) and okP and pos['klein_danach']
    out['M1'] = {'K': [Kp[i, 0].str(25, radius=True) for i in range(2)], 'rowsum': rs2.str(8), 'BESTANDEN': ok1}
    log("M1 (Profil bei om0):", "BESTANDEN" if ok1 else "NICHT BESTANDEN", out['M1']['K'])
    # M2: F(rho0, om0) fuer das Profil aus M1: F_i = (H0_{2+i}(a0) + dH/da (a - a0) + E) / s3
    Fv = []
    for i in (2, 3):
        a_dev = Kp[0, 0] - z0[0]
        val = (Hp[i] + DHZ[i, 0] * a_dev + arb(0, eps[i])) / s3
        Fv.append(val)
    out['M2'] = {'F1': Fv[0].str(10, radius=True), 'F2': Fv[1].str(10, radius=True)}
    log("M2: F(rho0, om0) =", out['M2'])
    # Empfindlichkeitskontrollen (nicht streng; D und eps vom Originalkasten uebernommen): Kastenmitte in rho um
    # delta/4, delta, 4 delta verschoben. Erwartung vorab: Kr hat Radius etwa delta/8 um die Nullstelle, der Test
    # kippt also bei einer Verschiebung von etwa 7/8 delta: delta/4 besteht, delta und 4 delta verfehlen.
    # Das zeigt Empfindlichkeit (wo der Test kippt), nicht Strenge.
    nk = []
    for zaehler, nenner in ((1, 4), (1, 1), (4, 1)):
        zs = list(z0)
        zs[2] = z0[2] + zaehler * delta[2] / nenner
        Hs, _, _, _, _ = evalH(zs, L, args.N, False, s1, s3, khat, N0=N0, Rmax=args.Rmax, qfac=args.q)
        Ks = ivec(zs) - Y * ivec(Hs) + Mk * dZ + absY * Eb
        ins = [bool(Ks[i, 0].lower() > zs[i] - delta[i]) and bool(Ks[i, 0].upper() < zs[i] + delta[i])
               for i in range(4)]
        nk.append({'verschiebung_rho': '%d/%d delta_rho' % (zaehler, nenner), 'innen_je_komponente': ins,
                   'test_bestanden': all(ins)})
        log("Empfindlichkeitskontrolle rho + %d/%d delta:" % (zaehler, nenner), ins,
            "besteht" if all(ins) else "verfehlt")
    out['empfindlichkeitskontrolle'] = {'art': 'nicht streng; zeigt Empfindlichkeit, nicht Strenge',
                                        'erwartung_vorab': '1/4 besteht, 1/1 und 4/1 verfehlen', 'ergebnisse': nk}
    # Protokoll fuer den Satz (Auflagen B1, W2, W5, W6, K5, K7 der Lesung)
    import platform, flint as _fl, sys as _sys
    names = ('a', 'c', 'rho', 'om')
    prot = {}
    prot['Z'] = {names[i]: {'z0_m_e': dy_str(z0[i]), 'delta_m_e': dy_str(delta[i]),
                            'untere_grenze': (z0[i] - delta[i]).str(45, radius=True),
                            'obere_grenze': (z0[i] + delta[i]).str(45, radius=True)} for i in range(4)}
    ab = []
    for i in range(4):
        lo = (Kr[i, 0].lower() - (z0[i] - delta[i])).lower()
        hi = ((z0[i] + delta[i]) - Kr[i, 0].upper()).lower()
        ab.append(((lo if lo < hi else hi) / delta[i]).lower().str(6))
    prot['innenabstand_rel_delta'] = dict(zip(names, ab))
    rs_unw = zeilenschranke(Mk, delta, 4, False)
    prot['zeilensumme_gewichtet'] = rowsum.str(20)
    prot['zeilensumme_ungewichtet'] = rs_unw.str(20)
    prot['D_relbreite'] = [[(DHZ[i, j].rad() / abs(DHZ[i, j].mid())).upper().str(3) if DHZ[i, j].mid() != 0 else '0'
                            for j in range(4)] for i in range(4)]
    om_b, rho_b = Zb[3], Zb[2]
    kap0_b = (1 - om_b * om_b).sqrt()
    kapc_b = (1 - (om_b - rho_b) ** 2).sqrt()
    prot['kanaele'] = {'k2_unten': ((om_b + rho_b) ** 2 - 1).lower().str(15),
                       'kapc2_unten': (1 - (om_b - rho_b) ** 2).lower().str(15),
                       'rho_minus_(1-om)_unten': (rho_b - (1 - om_b)).lower().str(12),
                       '(1+om)_minus_rho_unten': ((1 + om_b) - rho_b).lower().str(12),
                       '2kap0_minus_kapc_unten': (2 * kap0_b - kapc_b).lower().str(12),
                       '2om2_minus_1_unten': (2 * om_b * om_b - 1).lower().str(12)}
    prot['lemma_P'] = {'(i) fstar <= phibar': [einfo['fstar'].str(20), einfo['phibar_fs0'].str(20)],
                       '(ii) K m^3 <= eta': [einfo['Km3_eta0'].str(20), einfo['eta'].str(20)],
                       '(iii) Lambda < 1': einfo['Lip'].str(20),
                       '(iv) c - eta > 0 (untere Schranke)': einfo['c_minus_eta_lower'].str(20),
                       'K': einfo['K'].str(20), 'm': einfo['m'].str(20), 'ok': einfo['Lemma_P_ok']}
    prot['lemma_J'] = {k2: einfo[k2].str(20) for k2 in ('QL', 'mu', 'eps_J', 'EA', 'EB', 'EAp', 'EBp', 'K_J')}
    prot['K_J_minus_1_obere_schranke'] = (einfo['K_J'] - 1).upper().str(10)
    prot['eps_1_bis_4'] = [e.str(20) for e in eps]
    prot['H0_z0'] = [h.str(20, radius=True) for h in Hp]
    prot['regel_rundung'] = 'Schranken als exakte obere (upper) bzw. untere (lower) Werte; im Text Untergrenzen abrunden, Obergrenzen aufrunden'

    def schrittinfo(infs):
        return {'schritte': len(infs), 'fehlversuche': sum(i.get('nfail', 0) for i in infs),
                'R_min': min(float(i['R']) for i in infs), 'R_max': max(float(i['R']) for i in infs),
                'h_min': min(float(i['h']) for i in infs), 'h_max': max(float(i['h']) for i in infs),
                'inflationsrunden_max': max(i['nit'] for i in infs),
                'rest_max': max(i['tail_max'] for i in infs).str(4),
                'relw_f_bei_L': infs[-1].get('relw_f'), 'relw_Y_bei_L': infs[-1].get('relw_Y'),
                'R_kleiner_rj_alle': all((i['R'] < i['rj']) or i['rj'] == 0 for i in infs)}
    prot['schritte_punkt'] = schrittinfo(infp)
    prot['schritte_kasten'] = schrittinfo(infZ)
    prot['erster_schritt_punkt'] = erster_schritt(infp)
    prot['erster_schritt_kasten'] = erster_schritt(infZ)
    prot['einschlusstest'] = ('jeder angenommene Schritt hat den Test Y0 + Dt F(Dt, B) in B (acb_contains) bestanden; '
                              'sonst Fehler und kleineres R (bewkern.integrate); der Lauf endete ohne Fehler')
    prot['software'] = {'python': platform.python_version(), 'python_flint': _fl.__version__,
                        'interpreter': _sys.executable, 'praezision_bit': ctx.prec,
                        'float64_in_strenger_kette': 'nein (float nur fuer Startwerte, Y, Skalen s1/s3, khat, Gitterwahl)'}
    out['protokoll'] = prot
    def schrittliste(infs):
        return [{'r_j': str(i['rj'].mid()), 'R': str(i['R'].mid()), 'h': str(i['h'].mid()), 'r_ende': str(i['r_end']),
                 'inflationsrunden': i['nit'], 'fehlversuche': i.get('nfail', 0), 'rest': i['tail_max'].str(4),
                 'f_real_unten': i['f_lo'].str(6), 'f_real_oben': i['f_hi'].str(6),
                 'relw_f': i.get('relw_f'), 'relw_Y': i.get('relw_Y')} for i in infs]
    with open((args.out or 'ZERT.json').replace('.json', '-SCHRITTE-KASTEN.json'), 'w') as fh:
        json.dump(schrittliste(infZ), fh, indent=0)
    with open((args.out or 'ZERT.json').replace('.json', '-SCHRITTE-PUNKT.json'), 'w') as fh:
        json.dump(schrittliste(infp), fh, indent=0)
    log("Protokoll:", json.dumps(prot)[:3000])
    out['zeit_gesamt_s'] = time.time() - T0
    with open(args.out or 'ZERT.json', 'w') as fh:
        json.dump(out, fh, indent=1)
    log("geschrieben", args.out or 'ZERT.json')


def kontrolle(args, d, z0, khat, N0):
    """Nicht-strenge Kontrollen der Umsetzung:
    T1 A-priori-Rechte-Seite (acb) gegen Taylor-Rekursion (Ordnung 0) am Punkt,
    T2 Differenzenquotienten gegen die Jacobi-Matrix aus den Variationsgleichungen,
    (Die Empfindlichkeitskontrollen mit verschobenem Kasten laufen im Modus zert.)"""
    L = d['L']
    s1, s3 = consts(L, float(khat), d['kap0_f'], d['kapc_f'])
    par = K.Par(z0[0], z0[2], z0[3], khat)
    # T1: M_complex bei t = 0 gegen M_0 aus lin_M_series, Mp ebenso, an einer inneren Stelle
    st = K.initial_state(par, True)
    st2, _, _ = K.integrate(par, 3, 32, True, N0=64, Rmax=args.Rmax, qfac=args.q)
    rj = arb(3)
    Nn = 8
    f, g, S, T, w = K.prof_series(st2['f'], st2['g'], rj, par.kap0sq, Nn)
    trig = K.trig_series(khat, rj, Nn)
    Ms, _, _ = K.lin_M_series(S, T, trig, par, Nn)
    Np = [K.C75 * T[n] - 6 * S[n] for n in range(Nn)]
    Np[0] = Np[0] + par.kap0sq
    pa, qa = K.var_series(st2['pa'], st2['qa'], Np, w, None, Nn)
    pw, qw = K.var_series(st2['pw'], st2['qw'], Np, w, [par.src_w * x for x in f], Nn)
    Mps = K.lin_Mp_series(S, f, pa, pw, trig, par, Nn)
    kd = acb(khat * rj)
    Mc = K.M_complex(acb(st2['f']) ** 2, kd.cos(), kd.sin(), par)
    Mpc = K.Mp_complex(acb(st2['f']) ** 2, acb(st2['f']), acb(st2['pa']), acb(st2['pw']), kd.cos(), kd.sin(), par)
    dmax = max(abs(Mc[i, j] - acb(Ms[0][i, j])).upper() for i in range(4) for j in range(4))
    dpmax = max(abs(Mpc[i, j] - acb(Mps[0][i, j])).upper() for i in range(12) for j in range(4))
    # Profil: f' = g, g' = N(f) - 2g/r gegen Rekursion
    g1 = K.Nf(st2['f'], par.kap0sq) - 2 * st2['g'] / rj
    dprof = abs(g1 - g[1]).upper()
    # Taylor-Koeffizient 1 der linearen Loesung gegen M * Y
    Yb0 = arb_mat([[st2['Y'][r, 0], st2['Y'][r, 1]] for r in range(4)])
    Ys = K.lin_recursion(Ms, st2['Y'], Nn, Mps, Yb0)
    Yc = Mc * acb_mat(st2['Y'])
    Hc = Mpc * acb_mat(Yb0)
    dlin = max(abs(Ys[1][r, c] - Yc[r, c]).upper() for r in range(4) for c in range(2))
    dlin2 = max(abs(Ys[1][r, 2 + 2 * p + c] - Yc[r, 2 + 2 * p + c] - Hc[4 * p + r, c]).upper()
                for r in range(4) for p in range(3) for c in range(2))
    log("T1 |M_complex - M_0| <=", dmax.str(3), " |Mp_complex - Mp_0| <=", dpmax.str(3),
        " Profil g'", dprof.str(3), " Y'", dlin.str(3), " Y'_Jets", dlin2.str(3))

    # Auflage K6 der Code-Lesung: Mittelpunktsdifferenz und Radiensumme getrennt ausweisen
    def md_rs(paare):
        md = arb(0)
        rs = arb(0)
        for x, y in paare:
            d = abs(x.mid() - y.mid()).upper()
            r = (x.rad() + y.rad()).upper()
            md = d if d > md else md
            rs = r if r > rs else rs
        return md.str(3), rs.str(3)
    p_M = [(Mc[i, j], acb(Ms[0][i, j])) for i in range(4) for j in range(4)]
    p_Mp = [(Mpc[i, j], acb(Mps[0][i, j])) for i in range(12) for j in range(4)]
    p_g = [(g1, g[1])]
    p_Y = [(acb(Ys[1][r, c]), Yc[r, c]) for r in range(4) for c in range(2)]
    p_YJ = [(acb(Ys[1][r, 2 + 2 * p + c]), Yc[r, 2 + 2 * p + c] + Hc[4 * p + r, c])
            for r in range(4) for p in range(3) for c in range(2)]
    for name, paare in (('M', p_M), ('Mp', p_Mp), ("Profil g'", p_g), ("Y'", p_Y), ("Y'_Jets", p_YJ)):
        md, rs = md_rs(paare)
        log("T1 getrennt %-9s max |Mittelpunktsdifferenz| <= %s   max Radiensumme <= %s" % (name, md, rs))
    rY = max(st2['Y'][i, j].rad() for i in range(4) for j in range(8))
    log("T1 Eingangsradien bei r = 3: rad f", st2['f'].rad().str(3), " rad g", st2['g'].rad().str(3),
        " max rad Y (inkl. Jets)", rY.str(3), " rad phi_a", st2['pa'].rad().str(3), " rad phi_om",
        st2['pw'].rad().str(3))
    # T2: Differenzenquotienten
    H0, DH, _, _, _ = evalH(z0, L, args.Nbox, True, s1, s3, khat, N0=N0, Rmax=args.Rmax, qfac=args.q)
    epsj = [arb(10) ** -20, arb(10) ** -8, arb(10) ** -14, arb(10) ** -16]
    for j in range(4):
        zp = list(z0)
        zm = list(z0)
        zp[j] = z0[j] + epsj[j]
        zm[j] = z0[j] - epsj[j]
        Hp_, _, _, _, _ = evalH(zp, L, args.N, False, s1, s3, khat, N0=N0, Rmax=args.Rmax, qfac=args.q)
        Hm_, _, _, _, _ = evalH(zm, L, args.N, False, s1, s3, khat, N0=N0, Rmax=args.Rmax, qfac=args.q)
        rel = []
        for i in range(4):
            fd = (Hp_[i].mid() - Hm_[i].mid()) / (2 * epsj[j])
            dd = DH[i, j].mid()
            rel.append(((fd - dd) / (abs(dd) + arb(10) ** -30)).str(3))
        log("T2 Spalte", j, "rel. Abweichung Differenzenquotient/Jacobi je Zeile:", rel)
    log("fertig T1/T2")


if __name__ == '__main__':
    main()
