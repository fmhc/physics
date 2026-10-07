# BEWEIS-1 Kern: strenge Integration mit Kugelarithmetik (python-flint arb/acb).
# Autor: Beweis-Agent (Claude), 2026-09-30. Nur auf der .69 ueber kleintest.sh ausfuehren.
#
# Unbekannte z = (a, c, rho, om): a = f(0), c = Schwanzamplitude des Profils (f ~ c e^{-kap0 r}/r),
# rho = Stoerfrequenz, om = Q-Ball-Frequenz (x = om^2).
# Zustand vorwaerts von r = 0 bis L:
#   Profil (f, g = f'), Profilvariationen (phi_a, psi_a), (phi_om, psi_om),
#   zwei regulaere Loesungen R1 (A(0)=0, A'(0)=1, B(0)=B'(0)=0) und R2 (A(0)=A'(0)=0, B(0)=0, B'(0)=1)
#   in Variation-der-Konstanten-Koordinaten fuer den offenen Kanal mit fester Referenzwellenzahl khat:
#     A = al cos(khat r) + be sin(khat r),  A' = khat (-al sin + be cos),   (B, B') unveraendert.
#   Zeilen des linearen Zustands: (al, be, B, B'); Spalten: [R1 R2 | d_a | d_rho | d_om] (4x8 mit Ableitungen).
# Jeder Schritt: (1) komplexe A-priori-Huelle auf der Kreisscheibe |t| <= R (Picard-Selbstabbildung),
# (2) Taylor-Koeffizienten per Rekursion in Kugelarithmetik, (3) Auswertung bei t = h plus Cauchy-Rest
#     |Rest| <= beta (h/R)^N / (1 - h/R), beta = Radius der A-priori-Huelle je Komponente.
import math
from flint import arb, acb, arb_mat, acb_mat, arb_poly, ctx

C15 = arb(3) / 2
C45 = arb(9) / 2
C75 = arb(15) / 2


class Fehler(Exception):
    pass


def conv(u, v, n):
    s = u[0] * v[n]
    for i in range(1, n + 1):
        s += u[i] * v[n - i]
    return s


def sqc(u, n):
    # n-ter Koeffizient von u*u
    s = arb(0)
    for i in range((n + 1) // 2):
        s += u[i] * u[n - i]
    s = 2 * s
    if n % 2 == 0:
        s += u[n // 2] * u[n // 2]
    return s


def pmul(u, v, N):
    c = (arb_poly(u) * arb_poly(v)).coeffs()
    c = list(c[:N])
    while len(c) < N:
        c.append(arb(0))
    return c


class Par:
    """Parameter als Kugeln. khat: feste exakte Referenzwellenzahl."""

    def __init__(self, a, rho, om, khat):
        self.a, self.rho, self.om, self.khat = a, rho, om, khat
        self.kap0sq = 1 - om * om
        self.ksq = (om + rho) ** 2 - 1
        self.kapcsq = 1 - (om - rho) ** 2
        self.Pc = khat * khat - self.ksq
        self.dPr = -2 * (om + rho)       # d/drho von P
        self.dQr = 2 * (om - rho)        # d/drho von Q = d kapc^2/drho
        self.dPw = -2 * (om + rho)       # explizit d/dom von P (ohne Profil)
        self.dQw = -2 * (om - rho)       # explizit d/dom von Q
        self.src_w = -2 * om             # d/dom N(f) = -2 om f


def trig_series(khat, rj, N):
    s0, c0 = (khat * rj).sin_cos()
    s2, c2 = (2 * khat * rj).sin_cos()
    cs, sn, sc, ss, cc = [], [], [], [], []
    kp = arb(1)
    k2p = arb(1)
    fac = arb(1)
    for n in range(N):
        m = n % 4
        if m == 0:
            cn, snn, c2n, s2n = c0, s0, c2, s2
        elif m == 1:
            cn, snn, c2n, s2n = -s0, c0, -s2, c2
        elif m == 2:
            cn, snn, c2n, s2n = -c0, -s0, -c2, -s2
        else:
            cn, snn, c2n, s2n = s0, -c0, s2, -c2
        cs.append(kp * cn / fac)
        sn.append(kp * snn / fac)
        sc.append(k2p * s2n / (2 * fac))
        if n == 0:
            ss.append((1 - c2) / 2)
            cc.append((1 + c2) / 2)
        else:
            ss.append(-k2p * c2n / (2 * fac))
            cc.append(k2p * c2n / (2 * fac))
        kp = kp * khat
        k2p = k2p * 2 * khat
        fac = fac * (n + 1)
    return cs, sn, sc, ss, cc


# ---------------------------------------------------------------- Profilreihen
def prof_series(f0, g0, rj, kap0sq, N):
    """Taylor-Koeffizienten von f, g um rj > 0 (t = r - rj), Ordnungen 0..N-1; dazu S = f^2, T = S^2."""
    w = []
    p = 1 / rj
    for n in range(N):
        w.append(p if n % 2 == 0 else -p)
        p = p / rj
    f = [f0]
    g = [g0]
    S, T = [], []
    for n in range(N - 1):
        S.append(sqc(f, n))
        T.append(sqc(S, n))
        fS = conv(f, S, n)
        fT = conv(f, T, n)
        gw = conv(g, w, n)
        Nn = kap0sq * f[n] - 2 * fS + C15 * fT
        f.append(g[n] / (n + 1))
        g.append((Nn - 2 * gw) / (n + 1))
    S.append(sqc(f, N - 1))
    T.append(sqc(S, N - 1))
    return f, g, S, T, w


def prof_series0(a, kap0sq, N):
    """Reihe um r = 0: f = sum f_n r^n, f_1 = 0, f_{n+2} = N_n/((n+2)(n+3)); g_n = (n+1) f_{n+1}."""
    f = [a, arb(0)]
    S, T = [], []
    for n in range(N - 1):
        S.append(sqc(f, n))
        T.append(sqc(S, n))
        fS = conv(f, S, n)
        fT = conv(f, T, n)
        Nn = kap0sq * f[n] - 2 * fS + C15 * fT
        f.append(Nn / ((n + 2) * (n + 3)))
    # f hat jetzt N+1 Eintraege (0..N)
    S.append(sqc(f, N - 1))
    T.append(sqc(S, N - 1))
    g = [(n + 1) * f[n + 1] for n in range(N)]
    return f[:N], g, S, T


def var_series(phi0, psi0, Np, w, src, N):
    phi = [phi0]
    psi = [psi0]
    for n in range(N - 1):
        x = conv(Np, phi, n) - 2 * conv(psi, w, n)
        if src is not None:
            x += src[n]
        phi.append(psi[n] / (n + 1))
        psi.append(x / (n + 1))
    return phi, psi


def var_series0(phi0, Np, src, N):
    phi = [phi0, arb(0)]
    for n in range(N - 1):
        x = conv(Np, phi, n)
        if src is not None:
            x += src[n]
        phi.append(x / ((n + 2) * (n + 3)))
    psi = [(n + 1) * phi[n + 1] for n in range(N)]
    return phi[:N], psi


# ---------------------------------------------------------------- lineare Koeffizienten
def lin_M_series(S, T, trig, par, N):
    cs, sn, sc, ss, cc = trig
    dV = [C45 * T[n] - 4 * S[n] for n in range(N)]
    Cc = [3 * T[n] - 2 * S[n] for n in range(N)]
    P = list(dV)
    P[0] = P[0] + par.Pc
    Q = list(dV)
    Q[0] = Q[0] + par.kapcsq
    SCP = pmul(sc, P, N)
    SSP = pmul(ss, P, N)
    CCP = pmul(cc, P, N)
    snC = pmul(sn, Cc, N)
    csC = pmul(cs, Cc, N)
    ik = 1 / par.khat
    Ms = []
    for n in range(N):
        Ms.append(arb_mat([[-SCP[n] * ik, -SSP[n] * ik, -snC[n] * ik, 0],
                           [CCP[n] * ik, SCP[n] * ik, csC[n] * ik, 0],
                           [0, 0, 0, 1 if n == 0 else 0],
                           [csC[n], snC[n], Q[n], 0]]))
    return Ms, dV, Cc


def lin_Mp_series(S, f, phia, phiw, trig, par, N):
    """Gestapelte Ableitungsmatrizen [M_a; M_rho; M_om] (12x4) je Ordnung."""
    cs, sn, sc, ss, cc = trig
    dSa = [2 * x for x in pmul(f, phia, N)]
    dSw = [2 * x for x in pmul(f, phiw, N)]
    SdSa = pmul(S, dSa, N)
    SdSw = pmul(S, dSw, N)
    ddVa = [9 * SdSa[n] - 4 * dSa[n] for n in range(N)]
    dCa = [6 * SdSa[n] - 2 * dSa[n] for n in range(N)]
    ddVw = [9 * SdSw[n] - 4 * dSw[n] for n in range(N)]
    dCw = [6 * SdSw[n] - 2 * dSw[n] for n in range(N)]
    # a
    Pa, Qa, Ca = ddVa, ddVa, dCa
    # om
    Pw = list(ddVw)
    Pw[0] = Pw[0] + par.dPw
    Qw = list(ddVw)
    Qw[0] = Qw[0] + par.dQw
    Cw = dCw
    ik = 1 / par.khat
    SCPa, SSPa, CCPa = pmul(sc, Pa, N), pmul(ss, Pa, N), pmul(cc, Pa, N)
    snCa, csCa = pmul(sn, Ca, N), pmul(cs, Ca, N)
    SCPw, SSPw, CCPw = pmul(sc, Pw, N), pmul(ss, Pw, N), pmul(cc, Pw, N)
    snCw, csCw = pmul(sn, Cw, N), pmul(cs, Cw, N)
    out = []
    z = arb(0)
    for n in range(N):
        dq = par.dQr if n == 0 else z
        out.append(arb_mat([
            [-SCPa[n] * ik, -SSPa[n] * ik, -snCa[n] * ik, 0],
            [CCPa[n] * ik, SCPa[n] * ik, csCa[n] * ik, 0],
            [0, 0, 0, 0],
            [csCa[n], snCa[n], Qa[n], 0],
            [-sc[n] * par.dPr * ik, -ss[n] * par.dPr * ik, 0, 0],
            [cc[n] * par.dPr * ik, sc[n] * par.dPr * ik, 0, 0],
            [0, 0, 0, 0],
            [0, 0, dq, 0],
            [-SCPw[n] * ik, -SSPw[n] * ik, -snCw[n] * ik, 0],
            [CCPw[n] * ik, SCPw[n] * ik, csCw[n] * ik, 0],
            [0, 0, 0, 0],
            [csCw[n], snCw[n], Qw[n], 0]]))
    return out


def lin_recursion(Ms, Y0, N, Mps=None, Yb0=None):
    """Y_{n+1} = (sum_i M_i Y_{n-i} [+ Zusatz aus Mps * Yb]) / (n+1). Y0: 4 x m.
    Mit Ableitungen: Y0 = 4x8 = [Yb | Ya | Yr | Yw], Mps 12x4, Yb-Folge wird mitgefuehrt."""
    Y = [Y0]
    if Mps is None:
        for n in range(N - 1):
            acc = Ms[0] * Y[n]
            for i in range(1, n + 1):
                acc = acc + Ms[i] * Y[n - i]
            Y.append(acc * (1 / arb(n + 1)))
        return Y
    Yb = [Yb0]
    for n in range(N - 1):
        acc = Ms[0] * Y[n]
        hst = Mps[0] * Yb[n]
        for i in range(1, n + 1):
            acc = acc + Ms[i] * Y[n - i]
            hst = hst + Mps[i] * Yb[n - i]
        inv = 1 / arb(n + 1)
        new = arb_mat(4, 8)
        for r in range(4):
            for c in range(2):
                new[r, c] = acc[r, c] * inv
            for p in range(3):
                for c in range(2):
                    new[r, 2 + 2 * p + c] = (acc[r, 2 + 2 * p + c] + hst[4 * p + r, c]) * inv
        Y.append(new)
        Yb.append(arb_mat([[new[r, 0], new[r, 1]] for r in range(4)]))
    return Y


# ---------------------------------------------------------------- komplexe A-priori-Huelle
def acb_ball_arb(x):
    return acb(x)


def inflate_acb(z, fac, floor):
    re = z.real
    im = z.imag
    return acb(arb(re.mid(), re.rad() * fac + floor), arb(im.mid(), im.rad() * fac + floor))


def contains_all(big, small):
    for b, s in zip(big, small):
        if not b.contains(s):
            return False
    return True


def acb_beta(z):
    # obere Schranke fuer max |w - Mitte| ueber das Rechteck
    return z.real.rad() + z.imag.rad()


def M_complex(Sd, cd, sd, par):
    dV = C45 * Sd * Sd - 4 * Sd
    Cc = 3 * Sd * Sd - 2 * Sd
    P = dV + par.Pc
    Q = dV + par.kapcsq
    ik = 1 / par.khat
    sc = sd * cd
    ss = sd * sd
    cc = cd * cd
    return acb_mat([[-sc * P * ik, -ss * P * ik, -sd * Cc * ik, 0],
                    [cc * P * ik, sc * P * ik, cd * Cc * ik, 0],
                    [0, 0, 0, 1],
                    [cd * Cc, sd * Cc, Q, 0]])


def Mp_complex(Sd, fd, pad, pwd, cd, sd, par):
    dSa = 2 * fd * pad
    dSw = 2 * fd * pwd
    ddVa = 9 * Sd * dSa - 4 * dSa
    dCa = 6 * Sd * dSa - 2 * dSa
    ddVw = 9 * Sd * dSw - 4 * dSw
    dCw = 6 * Sd * dSw - 2 * dSw
    Pw = ddVw + par.dPw
    Qw = ddVw + par.dQw
    ik = 1 / par.khat
    sc = sd * cd
    ss = sd * sd
    cc = cd * cd
    return acb_mat([
        [-sc * ddVa * ik, -ss * ddVa * ik, -sd * dCa * ik, 0],
        [cc * ddVa * ik, sc * ddVa * ik, cd * dCa * ik, 0],
        [0, 0, 0, 0],
        [cd * dCa, sd * dCa, ddVa, 0],
        [-sc * par.dPr * ik, -ss * par.dPr * ik, 0, 0],
        [cc * par.dPr * ik, sc * par.dPr * ik, 0, 0],
        [0, 0, 0, 0],
        [0, 0, par.dQr, 0],
        [-sc * Pw * ik, -ss * Pw * ik, -sd * dCw * ik, 0],
        [cc * Pw * ik, sc * Pw * ik, cd * dCw * ik, 0],
        [0, 0, 0, 0],
        [cd * dCw, sd * dCw, Qw, 0]])


def Nf(f, kap0sq):
    S = f * f
    return f * (kap0sq - 2 * S + C15 * S * S)


def Npf(f, kap0sq):
    S = f * f
    return kap0sq - 6 * S + C75 * S * S


def mat_to_list(M):
    return [M[i, j] for i in range(M.nrows()) for j in range(M.ncols())]


def list_to_acbmat(L, nr, nc):
    return acb_mat([[L[i * nc + j] for j in range(nc)] for i in range(nr)])


def apriori(state, par, rj, R, jets, maxit=14):
    """Sucht komplexe Huellen B mit X0 + Dt * F(Dt, B) in B (bzw. Integralform bei rj = 0).
    Rueckgabe: Liste der acb-Huellen je Komponente in fester Reihenfolge oder Fehler."""
    Dt = acb(arb(0, R), arb(0, R))
    first = (rj == 0)
    if first:
        Dt2 = acb(arb(0, R * R), arb(0, R * R))
        WD = None
    else:
        if not (R < rj):   # Lemma T: Quadrat Dt darf 0 nicht enthalten (2/r analytisch), streng geprueft
            raise Fehler("R >= rj")
        WD = 1 / (acb(rj) + Dt)
    kd = acb(par.khat) * (acb(rj) + Dt)
    sd = kd.sin()
    cd = kd.cos()
    kap0 = acb(par.kap0sq)
    om2 = acb(par.src_w)
    # Anfangswerte als acb
    f0 = acb(state['f'])
    g0 = acb(state['g'])
    Y0 = [acb(x) for x in mat_to_list(state['Y'])]
    ncol = state['Y'].ncols()
    if jets:
        pa0, qa0, pw0, qw0 = [acb(state[k]) for k in ('pa', 'qa', 'pw', 'qw')]

    def rhs(B):
        Bf, Bg = B[0], B[1]
        out = []
        Nb = Nf(Bf, kap0)
        if first:
            nf = acb(state['f']) + Dt2 * Nb / 6
            ng = Dt * Nb / 3
        else:
            nf = f0 + Dt * Bg
            ng = g0 + Dt * (Nb - 2 * Bg * WD)
        out += [nf, ng]
        k = 2
        if jets:
            Bpa, Bqa, Bpw, Bqw = B[2], B[3], B[4], B[5]
            Np = Npf(Bf, kap0)
            if first:
                xa = Np * Bpa
                xw = Np * Bpw + om2 * Bf
                out += [pa0 + Dt2 * xa / 6, Dt * xa / 3, pw0 + Dt2 * xw / 6, Dt * xw / 3]
            else:
                out += [pa0 + Dt * Bqa, qa0 + Dt * (Np * Bpa - 2 * Bqa * WD),
                        pw0 + Dt * Bqw, qw0 + Dt * (Np * Bpw - 2 * Bqw * WD + om2 * Bf)]
            k = 6
        BY = list_to_acbmat(B[k:], 4, ncol)
        Sd = Bf * Bf
        Md = M_complex(Sd, cd, sd, par)
        FY = Md * BY
        if jets:
            BYb = acb_mat([[BY[r, 0], BY[r, 1]] for r in range(4)])
            Mpd = Mp_complex(Sd, Bf, B[2], B[4], cd, sd, par)
            H = Mpd * BYb
            FYl = mat_to_list(FY)
            for r in range(4):
                for p in range(3):
                    for c in range(2):
                        FYl[r * ncol + 2 + 2 * p + c] += H[4 * p + r, c]
        else:
            FYl = mat_to_list(FY)
        out += [Y0[i] + Dt * FYl[i] for i in range(len(Y0))]
        return out

    X0 = [f0, g0] + ([pa0, qa0, pw0, qw0] if jets else []) + Y0
    B = rhs(X0)
    B = [x.union(y) for x, y in zip(B, X0)]
    scale = [abs(x).abs_upper() for x in X0]
    B = [inflate_acb(b, 2, arb(2) ** -200 * (s + 1)) for b, s in zip(B, scale)]
    bad = []
    infl = arb(9) / 8
    r0 = max(acb_beta(b).upper() for b in B)
    for it in range(maxit):
        Bn = rhs(B)
        if contains_all(B, Bn):
            return B, it
        rn = max(acb_beta(b).upper() for b in Bn)
        if not rn.is_finite() or rn > 1000 * r0 + 1000:
            break
        bad = [(i, B[i].str(12, radius=True), Bn[i].str(12, radius=True)) for i in range(len(B))
               if not B[i].contains(Bn[i])][:3]
        # epsilon-Inflation: B_{k+1} = aufgeblaehtes rhs(B_k), ohne Vereinigung (sonst hinkt in gekoppelten
        # Ketten eine Komponente dauerhaft hinterher)
        B = [inflate_acb(y, infl, arb(2) ** -200 * (s + 1)) for y, s in zip(Bn, scale)]
    global LAST_B
    LAST_B = B
    raise Fehler("A-priori-Huelle nicht gefunden (rj=%s R=%s) %s" % (rj.str(6), R.str(6), bad))


# ---------------------------------------------------------------- ein Schritt
def horner(cs, h):
    acc = cs[-1]
    for c in reversed(cs[:-1]):
        acc = acc * h + c
    return acc


def horner_mat(Ys, h):
    acc = Ys[-1]
    for Y in reversed(Ys[:-1]):
        acc = acc * h + Y
    return acc


def step(state, par, rj, R, h, N, jets):
    """Ein strenger Schritt von rj nach rj + h. Liefert neuen Zustand und Protokoll."""
    B, nit = apriori(state, par, rj, R, jets)
    q = h / R
    tailfac = q ** N / (1 - q)
    ncol = state['Y'].ncols()
    first = (rj == 0)
    if first:
        f, g, S, T = prof_series0(state['f'], par.kap0sq, N)
        w = None
    else:
        f, g, S, T, w = prof_series(state['f'], state['g'], rj, par.kap0sq, N)
    trig = trig_series(par.khat, rj, N)
    Ms, dV, Cc = lin_M_series(S, T, trig, par, N)
    new = {}
    tails = [acb_beta(b) * tailfac for b in B]
    new['f'] = horner(f, h) + arb(0, tails[0].upper())
    new['g'] = horner(g, h) + arb(0, tails[1].upper())
    k = 2
    if jets:
        Np = [C75 * T[n] - 6 * S[n] for n in range(N)]
        Np[0] = Np[0] + par.kap0sq
        srcw = [par.src_w * x for x in f]
        if first:
            pa, qa = var_series0(state['pa'], Np, None, N)
            pw, qw = var_series0(state['pw'], Np, srcw, N)
        else:
            pa, qa = var_series(state['pa'], state['qa'], Np, w, None, N)
            pw, qw = var_series(state['pw'], state['qw'], Np, w, srcw, N)
        for key, ser, tl in (('pa', pa, tails[2]), ('qa', qa, tails[3]), ('pw', pw, tails[4]), ('qw', qw, tails[5])):
            new[key] = horner(ser, h) + arb(0, tl.upper())
        Mps = lin_Mp_series(S, f, pa, pw, trig, par, N)
        Yb0 = arb_mat([[state['Y'][r, 0], state['Y'][r, 1]] for r in range(4)])
        Ys = lin_recursion(Ms, state['Y'], N, Mps, Yb0)
        k = 6
    else:
        Ys = lin_recursion(Ms, state['Y'], N)
    Yh = horner_mat(Ys, h)
    tl = tails[k:]
    Tm = arb_mat([[arb(0, tl[r * ncol + c].upper()) for c in range(ncol)] for r in range(4)])
    new['Y'] = Yh + Tm
    # reelle Huelle von f auf [rj, rj+h] (fuer Positivitaet): Realteil der A-priori-Huelle
    fre = B[0].real
    info = {'rj': rj, 'R': R, 'h': h, 'nit': nit, 'tail_max': max(t.upper() for t in tails),
            'f_lo': fre.lower(), 'f_hi': fre.upper()}
    return new, info


def initial_state(par, jets):
    kh = par.khat
    st = {'f': par.a, 'g': arb(0)}
    # R1: A(0)=0, A'(0)=1 -> al = 0, be = 1/khat; R2: B'(0) = 1
    if jets:
        Y = arb_mat(4, 8)
        st.update({'pa': arb(1), 'qa': arb(0), 'pw': arb(0), 'qw': arb(0)})
    else:
        Y = arb_mat(4, 2)
    Y[1, 0] = 1 / kh
    Y[3, 1] = arb(1)
    st['Y'] = Y
    return st


def relw(x):
    """relative Breite rad/|mid| (0 fuer exakte Null) als float, nur Protokoll"""
    m = abs(x.mid())
    if m == 0:
        return 0.0
    return float((x.rad() / m).upper())


def dyf(x, bits):
    """groesste dyadische Zahl m 2^-bits <= x (x Fraction > 0), exakt"""
    from fractions import Fraction
    return Fraction(math.floor(x * 2 ** bits), 2 ** bits)


def fr_arb(x):
    """exakte Umwandlung eines dyadischen Bruchs in arb"""
    d = x.denominator
    assert d & (d - 1) == 0, "Nenner keine Zweierpotenz"
    return arb(x.numerator) / arb(d)


def integrate(par, L, N, jets, R0=1.0, N0=None, Rmax=1.0, qfac=4, rfrac=0.5, log=None, keep=None):
    """Integriert von 0 bis L (ganzzahlig oder dyadisch). Gitter exakt in dyadischen Bruechen (Fraction).
    keep: Liste dyadischer Radien (Fraction), an denen der Zustand gespeichert wird."""
    from fractions import Fraction
    L = Fraction(L)
    Rmax = dyf(Fraction(Rmax), 8)
    st = initial_state(par, jets)
    infos = []
    saved = {}
    # erster Schritt: Reihe um 0
    N0 = N0 or 2 * N
    R = dyf(Fraction(R0), 8)
    while True:
        h0 = R / 2
        try:
            st1, info = step(st, par, arb(0), fr_arb(R), fr_arb(h0), N0, jets)
            break
        except Fehler:
            R = dyf(R * Fraction(4, 5), 8)
            if R < Fraction(1, 20):
                raise
    st = st1
    info['r_end'] = h0
    infos.append(info)
    rjf = h0
    Rlast = None
    while rjf < L:
        Rt = min(Rmax, rfrac * rjf)
        if Rlast is not None:
            Rt = min(Rt, Rlast * Fraction(5, 4))
        Rt = dyf(Rt, 12)
        nf = 0
        while True:
            h = dyf(Rt / qfac, 14)
            if rjf + h > L:
                h = L - rjf
            try:
                st1, info = step(st, par, fr_arb(rjf), fr_arb(Rt), fr_arb(h), N, jets)
                break
            except Fehler:
                nf += 1
                Rt = dyf(Rt * Fraction(7, 10), 12)
                if Rt < Fraction(1, 1000):
                    raise
        Rlast = Rt
        st = st1
        info['r_end'] = rjf + h
        info['nfail'] = nf
        info['relw_f'] = relw(st['f'])
        info['relw_Y'] = max(relw(st['Y'][i, j]) for i in range(4) for j in range(st['Y'].ncols()))
        infos.append(info)
        rjf = rjf + h
        if log is not None and len(infos) % 40 == 0:
            log("  r=%.4f Schritte=%d R=%.4f tail=%s f=%s" % (float(rjf), len(infos), float(Rt),
                                                              info['tail_max'].str(3), st['f'].str(8, radius=True)))
        if keep is not None and rjf in keep:
            saved[rjf] = dict(st)
    assert rjf == L
    return st, infos, saved
