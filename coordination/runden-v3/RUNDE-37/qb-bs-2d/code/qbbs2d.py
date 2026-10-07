#!/usr/bin/env python3
# QB-BS-2D (Runde 37): radiale Stufen S0-S2 des Modells B.5 (Codex, SPIN-KONSTRUKTION-codex.md) in 2+1 Dimensionen.
# Igel-Ansatz n = (sin f cos(th+Om t), sin f sin(th+Om t), cos f), phi = h(r) exp(i(l th + Om t)).
# P2-Finite-Elemente auf exponentiell gestrecktem Gitter [0, RBOX], 3-Punkt-Gauss je Element.
# Festladung: E_q = V + q^2/(2 Lambda) (astra L3, CXS2-TORE-astra-20260924.md Abschn. 5, sinngemaess 2D).
# Loeser: Newton-Levenberg-Marquardt, Hesse-Matrix von F_Om = V - Om^2/2 Lambda per gefaerbter Zentraldifferenz
# des analytischen Gradienten, Rang-1-Term (Om^2/Lambda) gL gL^T per Sherman-Morrison, Armijo-Liniensuche auf E_q.
import sys, os, json, time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

VV = 1.0      # v
MU = 1.0      # mu
RBOX = 60.0   # Rechengebiet [0, RBOX]
BETA = 3.5    # Streckung: Elementgroessen wachsen um exp(BETA) von innen nach aussen
RLOC = 45.0   # Delokalisierungsradius
TOL_DEC = 1e-20
EPS_FD = 1e-5

def U(s):
    return s - s * s + 0.5 * s * s * s

def dU(s):
    return 1.0 - 2.0 * s + 1.5 * s * s


class Mesh:
    def __init__(self, M, R=RBOX, beta=BETA):
        s = np.linspace(0.0, 1.0, M + 1)
        rv = R * np.expm1(beta * s) / np.expm1(beta)
        rv[0] = 0.0
        rv[-1] = R
        self.M = M
        self.N = 2 * M + 1
        rn = np.empty(self.N)
        rn[0::2] = rv
        rn[1::2] = 0.5 * (rv[:-1] + rv[1:])
        self.r = rn
        e = np.arange(M)
        self.conn = np.stack([2 * e, 2 * e + 1, 2 * e + 2], axis=1)
        self.connflat = self.conn.ravel()
        xi = np.array([-np.sqrt(0.6), 0.0, np.sqrt(0.6)])
        w = np.array([5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0])
        self.Nm = np.stack([0.5 * xi * (xi - 1.0), 1.0 - xi * xi, 0.5 * xi * (xi + 1.0)], axis=1)  # (G,3)
        self.dNm = np.stack([xi - 0.5, -2.0 * xi, xi + 0.5], axis=1)  # (G,3)
        J = 0.5 * (rv[1:] - rv[:-1])
        self.J = J
        self.rg = (0.5 * (rv[:-1] + rv[1:]))[:, None] + J[:, None] * xi[None, :]
        self.W = 2.0 * np.pi * w[None, :] * J[:, None] * self.rg
        self.outer = self.rg > RLOC
        # gelumpte Knotengewichte (fuer skaliertes Residuum)
        self.Wn = np.bincount(self.connflat, weights=(self.W @ np.abs(self.Nm)).ravel(), minlength=self.N)

    def scatter(self, A, B):
        loc = (A * self.W) @ self.Nm
        if B is not None:
            loc = loc + ((B * self.W) / self.J[:, None]) @ self.dNm
        return np.bincount(self.connflat, weights=loc.ravel(), minlength=self.N)

    def at_gauss(self, F):
        fe = F[self.conn]
        return fe @ self.Nm.T, (fe @ self.dNm.T) / self.J[:, None]


class Model:
    def __init__(self, mesh, kap, Gp=0.0, l=0, split=False):
        self.mesh = mesh
        self.kap = float(kap)
        self.Gp = float(Gp)
        self.l = int(l)
        self.split = bool(split)

    def evaluate(self, F, H, grad=True):
        m = self.mesh
        f, df = m.at_gauss(F)
        h, dh = m.at_gauss(H)
        r2 = m.rg * m.rg
        s = np.sin(f)
        c = np.cos(f)
        S2 = s * s
        s2f = 2.0 * s * c
        x = h * h
        a = 0.25 * VV * VV
        y = a * S2
        kap = self.kap
        Gp = self.Gp
        l2 = float(self.l * self.l)
        W = m.W
        d_hgrad = dh * dh + l2 * x / r2
        d_sig = a * (df * df + S2 / r2)
        d_fad = 0.5 * kap * df * df * S2 / r2
        if self.split:
            d_U = U(x) + U(y)
        else:
            d_U = U(x + y)
        d_pair = -Gp * x * y
        d_mass = MU * MU * VV * VV * (1.0 - c)
        lamn_pot = 2.0 * a * S2
        lamn_grad = kap * S2 * df * df
        lamp = 2.0 * x
        out = {
            'E_hgrad': float(np.sum(W * d_hgrad)),
            'E_sig': float(np.sum(W * d_sig)),
            'E_fad': float(np.sum(W * d_fad)),
            'E_U': float(np.sum(W * d_U)),
            'E_pair': float(np.sum(W * d_pair)),
            'E_mass': float(np.sum(W * d_mass)),
            'Lam_n_pot': float(np.sum(W * lamn_pot)),
            'Lam_n_grad': float(np.sum(W * lamn_grad)),
            'Lam_p': float(np.sum(W * lamp)),
            'Lam_p_out': float(np.sum((W * lamp)[m.outer])),
            'Lam_n_out': float(np.sum((W * (lamn_pot + lamn_grad))[m.outer])),
        }
        out['Lam_n'] = out['Lam_n_pot'] + out['Lam_n_grad']
        out['V'] = out['E_hgrad'] + out['E_sig'] + out['E_fad'] + out['E_U'] + out['E_pair'] + out['E_mass']
        if not grad:
            return out, None
        if self.split:
            Uf = dU(y) * a * s2f
            Uh = dU(x) * 2.0 * h
        else:
            dUs = dU(x + y)
            Uf = dUs * a * s2f
            Uh = dUs * 2.0 * h
        Vf = a * s2f / r2 + 0.5 * kap * df * df * s2f / r2 + Uf - Gp * x * a * s2f + MU * MU * VV * VV * s
        Vdf = 2.0 * a * df + kap * df * S2 / r2
        Vh = 2.0 * l2 * h / r2 + Uh - 2.0 * Gp * h * y
        Vdh = 2.0 * dh
        Lnf = 2.0 * a * s2f + kap * s2f * df * df
        Lndf = 2.0 * kap * S2 * df
        Lph = 4.0 * h
        g = {
            'VF': m.scatter(Vf, Vdf),
            'VH': m.scatter(Vh, Vdh),
            'LnF': m.scatter(Lnf, Lndf),
            'LpH': m.scatter(Lph, None),
        }
        return out, g

    def chi_max(self, F, Om):
        # chi = kap c^T G^-1 c (qball-hopf-3d ROTATIONSGRENZE.txt, ERGEBNIS.txt Abschn. 3), allgemein v, kappa:
        # G = (v^2/2) I + kap sum_i a_i a_i^T, a_i = (d_i n) x n, c = n x (Om e3 x n).
        # Igel: c = -Om sin f e_f, G_ff = v^2/2 + kap sin^2 f / r^2  ->  chi = kap Om^2 S2 / (v^2/2 + kap S2/r^2).
        m = self.mesh
        f, df = m.at_gauss(F)
        S2 = np.sin(f) ** 2
        chi = self.kap * Om * Om * S2 / (0.5 * VV * VV + self.kap * S2 / (m.rg * m.rg))
        k = int(np.argmax(chi))
        return float(chi.ravel()[k]), float(m.rg.ravel()[k])


class Problem:
    # mode: 'H' (h=0, Lambda=Lam_n), 'Q' (f=0, Lambda=Lam_p), 'M1' (f,h, Lambda=Lam_n+Lam_p), 'M0' (f,h, Lambda=Lam_p, Textur ruht)
    def __init__(self, mesh, kap, mode, l=0, Gp=0.0, split=False):
        self.mesh = mesh
        self.mode = mode
        self.l = l
        self.model = Model(mesh, kap, Gp, l, split)
        N = mesh.N
        self.freeF = np.zeros(N, bool)
        self.freeH = np.zeros(N, bool)
        if mode in ('H', 'M1', 'M0'):
            self.freeF[1:-1] = True
        if mode in ('Q', 'M1', 'M0'):
            self.freeH[:-1] = True
            if l == 1:
                self.freeH[0] = False
        self.nF = int(self.freeF.sum())
        self.nH = int(self.freeH.sum())
        self.n = self.nF + self.nH
        self.idxF = -np.ones(N, int)
        self.idxF[self.freeF] = np.arange(self.nF)
        self.idxH = -np.ones(N, int)
        self.idxH[self.freeH] = self.nF + np.arange(self.nH)
        self.Fbase = np.zeros(N)
        if mode in ('H', 'M1', 'M0'):
            self.Fbase[0] = np.pi
        self.Hbase = np.zeros(N)
        self.useLn = mode in ('H', 'M1')
        self.useLp = mode in ('Q', 'M1', 'M0')

    def unpack(self, x):
        F = self.Fbase.copy()
        H = self.Hbase.copy()
        F[self.freeF] = x[:self.nF]
        H[self.freeH] = x[self.nF:]
        return F, H

    def pack(self, F, H):
        return np.concatenate([F[self.freeF], H[self.freeH]])

    def lam(self, out):
        L = 0.0
        if self.useLn:
            L += out['Lam_n']
        if self.useLp:
            L += out['Lam_p']
        return L

    def gL_nodal(self, g):
        N = self.mesh.N
        gLF = g['LnF'] if self.useLn else np.zeros(N)
        gLH = g['LpH'] if self.useLp else np.zeros(N)
        return gLF, gLH

    def eq(self, x, q):
        F, H = self.unpack(x)
        out, g = self.model.evaluate(F, H, True)
        Lam = self.lam(out)
        if q == 0.0:
            Om = 0.0
            E = out['V']
        else:
            Om = q / Lam
            E = out['V'] + 0.5 * q * q / Lam
        gLF, gLH = self.gL_nodal(g)
        gF = g['VF'] - 0.5 * Om * Om * gLF
        gH = g['VH'] - 0.5 * Om * Om * gLH
        gx = self.pack(gF, gH)
        gL = self.pack(gLF, gLH)
        return E, gx, Om, Lam, gL, out

    def grad_FOm_nodal(self, x, Om):
        F, H = self.unpack(x)
        out, g = self.model.evaluate(F, H, True)
        gLF, gLH = self.gL_nodal(g)
        return g['VF'] - 0.5 * Om * Om * gLF, g['VH'] - 0.5 * Om * Om * gLH

    def hessian(self, x, Om):
        n = self.n
        N = self.mesh.N
        rows, cols, vals = [], [], []
        for free, idx in ((self.freeF, self.idxF), (self.freeH, self.idxH)):
            if not free.any():
                continue
            nodes = np.nonzero(free)[0]
            for col in range(5):
                P = nodes[nodes % 5 == col]
                if len(P) == 0:
                    continue
                cidx = idx[P]
                dx = np.zeros(n)
                dx[cidx] = EPS_FD
                gpF, gpH = self.grad_FOm_nodal(x + dx, Om)
                gmF, gmH = self.grad_FOm_nodal(x - dx, Om)
                dgF = (gpF - gmF) / (2.0 * EPS_FD)
                dgH = (gpH - gmH) / (2.0 * EPS_FD)
                for o in range(-2, 3):
                    i = P + o
                    ok = (i >= 0) & (i < N)
                    ii = i[ok]
                    jj = cidx[ok]
                    mF = self.freeF[ii]
                    rows.append(self.idxF[ii[mF]]); cols.append(jj[mF]); vals.append(dgF[ii[mF]])
                    mH = self.freeH[ii]
                    rows.append(self.idxH[ii[mH]]); cols.append(jj[mH]); vals.append(dgH[ii[mH]])
        Hs = sp.coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(n, n)).tocsr()
        return (0.5 * (Hs + Hs.T)).tocsr()

    def solve(self, x0, q, maxit=150):
        x = x0.copy()
        lam = 1e-6
        E, g, Om, Lam, gL, out = self.eq(x, q)
        conv = False
        dec = np.inf
        it = 0
        nfail = 0
        for it in range(1, maxit + 1):
            if not np.isfinite(E):
                break
            Hs = self.hessian(x, Om)
            dg = np.abs(Hs.diagonal())
            dg = np.maximum(dg, 1e-12 * max(dg.max(), 1e-300))
            a = (Om * Om / Lam) if q != 0.0 else 0.0
            accepted = False
            for _ in range(40):
                A = (Hs + lam * sp.diags(dg)).tocsc()
                try:
                    lu = spla.splu(A)
                    z1 = lu.solve(g)
                    if a != 0.0:
                        z2 = lu.solve(gL)
                        d = -(z1 - a * (gL @ z1) / (1.0 + a * (gL @ z2)) * z2)
                    else:
                        d = -z1
                except Exception:
                    lam = max(lam * 10.0, 1e-8)
                    continue
                slope = float(g @ d)
                if (not np.isfinite(slope)) or slope >= 0.0:
                    lam = max(lam * 10.0, 1e-8)
                    continue
                if -slope < 1e-12 * max(1.0, abs(E)):
                    t = 1.0
                    E2, g2, Om2, Lam2, gL2, out2 = self.eq(x + d, q)
                    accepted = np.isfinite(E2)
                    if accepted:
                        break
                    lam = max(lam * 10.0, 1e-8)
                    continue
                t = 1.0
                ok = False
                while t > 1e-3:
                    E2, g2, Om2, Lam2, gL2, out2 = self.eq(x + t * d, q)
                    if np.isfinite(E2) and E2 <= E + 1e-4 * t * slope:
                        ok = True
                        break
                    t *= 0.5
                if ok:
                    accepted = True
                    break
                lam = max(lam * 10.0, 1e-8)
            if not accepted:
                nfail += 1
                break
            dec = -slope
            x = x + t * d
            E, g, Om, Lam, gL, out = E2, g2, Om2, Lam2, gL2, out2
            if t == 1.0:
                lam = max(lam * 0.1, 1e-14)
            if t == 1.0 and dec < TOL_DEC * max(1.0, abs(E)):
                conv = True
                break
        return x, {'conv': bool(conv), 'it': int(it), 'dec': float(dec), 'lam': float(lam)}

    def diagnostics(self, x, q):
        E, g, Om, Lam, gL, out = self.eq(x, q)
        F, H = self.unpack(x)
        m = self.mesh
        d = dict(out)
        d['q'] = float(q)
        d['E'] = float(E)
        d['Lam'] = float(Lam)
        d['Om'] = float(Om)
        d['Om2'] = float(Om * Om)
        d['q_n'] = float(Om * out['Lam_n']) if self.useLn else 0.0
        d['q_p'] = float(Om * out['Lam_p']) if self.useLp else 0.0
        d['J'] = d['q_n'] + self.l * d['q_p']
        if self.useLn:
            cm, rc = self.model.chi_max(F, Om)
        else:
            cm, rc = 0.0, 0.0
        d['chi_max'] = cm
        d['r_chi_max'] = rc
        E0 = out['E_U'] + out['E_pair'] + out['E_mass']
        E4 = out['E_fad']
        Lpot = (out['Lam_n_pot'] if self.useLn else 0.0) + (out['Lam_p'] if self.useLp else 0.0)
        vir = E0 - E4 - 0.5 * Om * Om * Lpot
        d['virial_rel'] = float(abs(vir) / max(E0 + E4 + 0.5 * Om * Om * Lpot, 1e-300))
        d['E_sig_over_2pi'] = float(out['E_sig'] / (2.0 * np.pi * VV * VV))
        d['frac_p_out'] = float(out['Lam_p_out'] / out['Lam_p']) if out['Lam_p'] > 0 else 0.0
        d['frac_n_out'] = float(out['Lam_n_out'] / out['Lam_n']) if out['Lam_n'] > 0 else 0.0
        d['res_scaled'] = float(np.max(np.abs(g) / np.concatenate([m.Wn[self.freeF], m.Wn[self.freeH]]))) if self.n else 0.0
        if self.mode in ('H', 'M1', 'M0'):
            k = np.nonzero(F < 0.5 * np.pi)[0]
            if len(k) and k[0] > 0:
                j = k[0]
                r0, r1 = m.r[j - 1], m.r[j]
                f0, f1 = F[j - 1], F[j]
                d['r_ring'] = float(r0 + (0.5 * np.pi - f0) * (r1 - r0) / (f1 - f0))
            else:
                d['r_ring'] = None
        if self.mode in ('Q', 'M1', 'M0'):
            j = int(np.argmax(np.abs(H)))
            d['h_max'] = float(abs(H[j]))
            d['r_h_max'] = float(m.r[j])
        return d


def texture_guess(mesh, width=1.0):
    F = np.pi * np.exp(-mesh.r / width)
    F[0] = np.pi
    F[-1] = 0.0
    return F


def ball_guess(mesh, q, l, om=0.8):
    Rq = np.sqrt(max(q, 1.0) / (2.0 * np.pi * om))
    if l == 0:
        H = 1.0 / (1.0 + np.exp((mesh.r - Rq) / 0.8))
    else:
        Rq1 = np.sqrt(Rq * Rq + 4.0)
        H = np.tanh(mesh.r) / (1.0 + np.exp((mesh.r - Rq1) / 0.8))
    H[-1] = 0.0
    if l == 1:
        H[0] = 0.0
    return H


def transfer(mesh_from, mesh_to, V):
    W = np.interp(mesh_to.r, mesh_from.r, V)
    return W


def dump(path, obj):
    tmp = path + '.tmp'
    with open(tmp, 'w') as fh:
        json.dump(obj, fh, indent=1)
    os.replace(tmp, path)


def now():
    return time.strftime('%Y-%m-%dT%H:%M:%S%z')


# ---------------------------------------------------------------- Aeste

def run_refH(kap, Ms, out, du=0.5, umax_hard=400.0):
    thr = 0.95 * VV * VV / (2.0 * kap)
    res = {'task': 'refH', 'kappa': kap, 'Ms': Ms, 'du': du, 'Om2_stop': thr, 'start': now(), 'branches': {}}
    prev_mesh = None
    prev_sols = None
    for M in Ms:
        t0 = time.time()
        mesh = Mesh(M)
        prob = Problem(mesh, kap, 'H')
        pts = []
        sols = {}
        F0 = texture_guess(mesh)
        x = prob.pack(F0, np.zeros(mesh.N))
        u = 0.0
        stop = None
        while u <= umax_hard + 1e-9:
            if prev_sols is not None:
                key = round(u, 6)
                if key not in prev_sols:
                    stop = 'kein Grobpunkt'
                    break
                Fp, Hp = prev_sols[key]
                x = prob.pack(transfer(prev_mesh, mesh, Fp), np.zeros(mesh.N))
            xs, info = prob.solve(x, u)
            d = prob.diagnostics(xs, u)
            d.update(info)
            if not info['conv']:
                d['status'] = 'nicht konvergiert'
                pts.append(d)
                stop = 'Loeser versagt bei u=%g' % u
                break
            if d['Om2'] > thr:
                d['status'] = 'jenseits 0.95-Schwelle'
                pts.append(d)
                stop = 'Om2>0.95 v^2/(2 kappa) bei u=%g' % u
                break
            d['status'] = 'ok'
            pts.append(d)
            F, H = prob.unpack(xs)
            sols[round(u, 6)] = (F, H)
            x = xs
            u = round(u + du, 6)
            res['branches'][str(M)] = {'points': pts, 'stop': stop, 'sec': time.time() - t0}
            dump(out, res)
        res['branches'][str(M)] = {'points': pts, 'stop': stop, 'sec': time.time() - t0}
        dump(out, res)
        prev_mesh, prev_sols = mesh, sols
    res['ende'] = now()
    dump(out, res)
    return res


def run_refQ(l, Ms, out, qtop=100.0, dq=1.0):
    res = {'task': 'refQ', 'l': l, 'Ms': Ms, 'dq': dq, 'start': now(), 'branches': {}}
    prev_mesh = None
    prev_sols = None
    for M in Ms:
        t0 = time.time()
        mesh = Mesh(M)
        prob = Problem(mesh, 1.0, 'Q', l=l)
        pts = []
        sols = {}
        x = prob.pack(np.zeros(mesh.N), ball_guess(mesh, qtop, l, om=0.75))
        q = qtop
        stop = None
        while q > 0.5 * dq:
            if prev_sols is not None:
                key = round(q, 6)
                if key not in prev_sols:
                    stop = 'kein Grobpunkt'
                    break
                Fp, Hp = prev_sols[key]
                x = prob.pack(np.zeros(mesh.N), transfer(prev_mesh, mesh, Hp))
            xs, info = prob.solve(x, q)
            d = prob.diagnostics(xs, q)
            d.update(info)
            loc = d['frac_p_out'] < 1e-4
            if not info['conv']:
                d['status'] = 'nicht konvergiert'
                pts.append(d)
                stop = 'Loeser versagt bei q=%g' % q
                break
            if not loc:
                d['status'] = 'delokalisiert'
                pts.append(d)
                stop = 'delokalisiert bei q=%g' % q
                break
            if d['Om'] > 0.999:
                d['status'] = 'omega>0.999'
                pts.append(d)
                stop = 'omega>0.999 bei q=%g' % q
                break
            d['status'] = 'ok'
            pts.append(d)
            F, H = prob.unpack(xs)
            sols[round(q, 6)] = (F, H)
            x = xs
            q = round(q - dq, 6)
            res['branches'][str(M)] = {'points': pts, 'stop': stop, 'sec': time.time() - t0}
            dump(out, res)
        res['branches'][str(M)] = {'points': pts, 'stop': stop, 'sec': time.time() - t0}
        dump(out, res)
        prev_mesh, prev_sols = mesh, sols
    res['ende'] = now()
    dump(out, res)
    return res


def qualified_mix(d, G):
    if not d.get('conv'):
        return False
    if d['frac_p_out'] >= 1e-4:
        return False
    if d['q'] > 0 and d['q_p'] / d['q'] < 0.01:
        return False
    return True


def run_mix(kap, G, Ms, out, qs, nullqs=()):
    if G == 1:
        mode, l, Gp = 'M1', 1, 1.0
    else:
        mode, l, Gp = 'M0', 0, 0.0
    res = {'task': 'mix', 'kappa': kap, 'G': G, 'mode': mode, 'l': l, 'Ms': Ms, 'qs': list(qs), 'start': now(),
           'branches': {}, 'null': {}}
    prev_mesh = None
    prev_sel = None
    for M in Ms:
        t0 = time.time()
        mesh = Mesh(M)
        # statische Textur auf diesem Gitter
        probH = Problem(mesh, kap, 'H')
        xH, infoH = probH.solve(probH.pack(texture_guess(mesh), np.zeros(mesh.N)), 0.0)
        Fstat, _ = probH.unpack(xH)
        prob = Problem(mesh, kap, mode, l=l, Gp=Gp)
        pts = []
        sel = {}
        cont = None
        for q in qs:
            starts = []
            if prev_sel is not None:
                key = round(q, 6)
                if key in prev_sel:
                    Fp, Hp = prev_sel[key]
                    starts.append(('grob', prob.pack(transfer(prev_mesh, mesh, Fp), transfer(prev_mesh, mesh, Hp))))
            else:
                if cont is not None:
                    starts.append(('fortsetzung', cont))
                Hring = 0.8 * np.sin(Fstat)
                Hring[-1] = 0.0
                starts.append(('ring', prob.pack(Fstat, Hring)))
                starts.append(('ball', prob.pack(Fstat, ball_guess(mesh, q, l))))
            cand = []
            for name, x0 in starts:
                xs, info = prob.solve(x0, q)
                d = prob.diagnostics(xs, q)
                d.update(info)
                d['start'] = name
                d['qualifiziert'] = qualified_mix(d, G)
                cand.append((d, xs))
            conv = [c for c in cand if c[0]['conv']]
            if conv:
                qual = [c for c in conv if c[0]['qualifiziert']]
                pool = qual if qual else conv
                best = min(pool, key=lambda c: c[0]['E'])
                bd = dict(best[0])
                bd['alle_starts'] = [{'start': c[0]['start'], 'E': c[0]['E'], 'conv': c[0]['conv'],
                                      'qualifiziert': c[0]['qualifiziert'], 'q_p_anteil': (c[0]['q_p'] / q if q else 0.0),
                                      'Om2': c[0]['Om2']} for c in cand]
                pts.append(bd)
                F, H = prob.unpack(best[1])
                sel[round(q, 6)] = (F, H)
                cont = best[1]
            else:
                pts.append({'q': q, 'conv': False, 'qualifiziert': False, 'status': 'kein Start konvergiert',
                            'alle_starts': [{'start': c[0]['start'], 'E': c[0]['E'], 'conv': False} for c in cand]})
            res['branches'][str(M)] = {'points': pts, 'sec': time.time() - t0, 'E_H0': probH.diagnostics(xH, 0.0)['E'],
                                       'H0_conv': infoH['conv']}
            dump(out, res)
        # Nullprobe K4: G=0 und U(x)+U(y), ruhende Textur, Ballstart
        if nullqs:
            probN = Problem(mesh, kap, 'M0', l=0, Gp=0.0, split=True)
            nl = []
            for q in nullqs:
                xs, info = probN.solve(probN.pack(Fstat, ball_guess(mesh, q, 0)), q)
                d = probN.diagnostics(xs, q)
                d.update(info)
                nl.append(d)
            res['null'][str(M)] = nl
            dump(out, res)
        prev_mesh, prev_sel = mesh, sel
    res['ende'] = now()
    dump(out, res)
    return res


def run_smoke(out):
    t0 = time.time()
    log = {'start': now(), 'tests': []}
    for M in (200, 400):
        mesh = Mesh(M)
        for kap in (1.0, 0.25):
            prob = Problem(mesh, kap, 'H')
            t1 = time.time()
            xs, info = prob.solve(prob.pack(texture_guess(mesh), np.zeros(mesh.N)), 0.0)
            d = prob.diagnostics(xs, 0.0)
            d.update(info)
            d['sec'] = time.time() - t1
            d['test'] = 'H statisch M=%d kappa=%g' % (M, kap)
            log['tests'].append(d)
            dump(out, log)
            t1 = time.time()
            xs2, info2 = prob.solve(xs, 3.0)
            d = prob.diagnostics(xs2, 3.0)
            d.update(info2)
            d['sec'] = time.time() - t1
            d['test'] = 'H u=3 M=%d kappa=%g' % (M, kap)
            log['tests'].append(d)
            dump(out, log)
        for l in (0, 1):
            prob = Problem(mesh, 1.0, 'Q', l=l)
            t1 = time.time()
            xs, info = prob.solve(prob.pack(np.zeros(mesh.N), ball_guess(mesh, 60.0, l, 0.75)), 60.0)
            d = prob.diagnostics(xs, 60.0)
            d.update(info)
            d['sec'] = time.time() - t1
            d['test'] = 'Q l=%d q=60 M=%d' % (l, M)
            log['tests'].append(d)
            dump(out, log)
        # Mischaeste nur als Codepfadtest (q=20, ein Start), keine Bindungsauswertung im Rauchlauf
        probH = Problem(mesh, 1.0, 'H')
        xH, _ = probH.solve(probH.pack(texture_guess(mesh), np.zeros(mesh.N)), 0.0)
        Fstat, _ = probH.unpack(xH)
        for mode, l, Gp in (('M1', 1, 1.0), ('M0', 0, 0.0)):
            prob = Problem(mesh, 1.0, mode, l=l, Gp=Gp)
            Hring = 0.8 * np.sin(Fstat)
            Hring[-1] = 0.0
            t1 = time.time()
            xs, info = prob.solve(prob.pack(Fstat, Hring), 20.0)
            d = prob.diagnostics(xs, 20.0)
            d.update(info)
            d['sec'] = time.time() - t1
            d['test'] = '%s q=20 M=%d kappa=1 (Codepfad)' % (mode, M)
            # E und D werden im Rauchlauf bewusst nicht gegen Referenzen verglichen
            log['tests'].append(d)
            dump(out, log)
    log['sec'] = time.time() - t0
    log['ende'] = now()
    dump(out, log)


if __name__ == '__main__':
    task = sys.argv[1]
    if task == 'smoke':
        run_smoke(sys.argv[2])
    elif task == 'refH':
        kap = float(sys.argv[2]); Ms = [int(v) for v in sys.argv[3].split(',')]
        run_refH(kap, Ms, sys.argv[4], du=float(sys.argv[5]) if len(sys.argv) > 5 else 0.5)
    elif task == 'refQ':
        l = int(sys.argv[2]); Ms = [int(v) for v in sys.argv[3].split(',')]
        run_refQ(l, Ms, sys.argv[4], qtop=float(sys.argv[5]) if len(sys.argv) > 5 else 100.0,
                 dq=float(sys.argv[6]) if len(sys.argv) > 6 else 1.0)
    elif task == 'mix':
        kap = float(sys.argv[2]); G = int(sys.argv[3]); Ms = [int(v) for v in sys.argv[4].split(',')]
        qmax = float(sys.argv[6]) if len(sys.argv) > 6 else 100.0
        dqm = float(sys.argv[7]) if len(sys.argv) > 7 else 2.5
        qs = [round(dqm * k, 6) for k in range(1, int(round(qmax / dqm)) + 1)]
        nullqs = (30.0, 60.0, 90.0) if (G == 0 and kap == 1.0) else ()
        run_mix(kap, G, Ms, sys.argv[5], qs, nullqs)
    else:
        raise SystemExit('unbekannte Aufgabe')
