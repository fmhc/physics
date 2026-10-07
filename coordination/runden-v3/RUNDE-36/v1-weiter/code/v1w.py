#!/usr/bin/env python3
"""V-1-WEITER (Runde 36), Code-Agent fuer die Leitung claude-primary, 04.10.2026.
Karte: RUNDE-36/v1-weiter/KARTE.md, Plan: RUNDE-36/v1-weiter/PLAN.md.

Ebene M1-Wand (U = S - S^2 + beta S^3) bei omega_min mit Zusatzterm eps d^4/dx^4 in der Feldgleichung
  phi_tt - phi_xx + eps phi_xxxx + U'(|phi|^2) phi = 0.
Hintergrund f(x) (4. Ordnung, FD-Newton, 4. Ordnung genau), Schwankungen (A, B) mit
  eps Z'''' - Z'' + V(x) Z = 0,  V = [[W - (rho-om)^2, C], [C, W - (rho+om)^2]],
  W = 1 - 4S + 9 beta S^2, C = -2S + 6 beta S^2 (wie WAND-BETA, dort eps = 0).
Stille-Funktion E(rho) = det[Q_aus | Q_innen] im Wandmittelpunkt x = 0 (Evans-Determinante, reell):
  Q_aus  = Orthonormalbasis der aussen abklingenden Loesungen (kein laufender Anteil aussen),
  Q_innen = Orthonormalbasis der innen beschraenkten Loesungen (laufende Paare + nach -inf abklingende).
  Integration abschnittsweise mit QR-Neuorthonormierung (Godunov/Conte). Bei eps = 0 ist E = 0 genau die
  WAND-BETA-Bedingung c_in = 0.
Streuung: Einfall im alten Innenkanal (e1, kleines k), Ausgang in alle offenen Kanaele; Fluss ueber die erhaltene
  Form J(Y,Z) = Y.Z' - Y'.Z - eps (Y.Z''' - Y'.Z'' + Y''.Z' - Y'''.Z).

Aufruf: python v1w.py <eps> <h_bg> <rtol> <aus.json> [rho_mitte halbbreite n_scan [beta [xr_hintergrund]]]
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import scipy.sparse as sp  # noqa: E402
from scipy.integrate import solve_ivp  # noqa: E402
from scipy.interpolate import make_interp_spline  # noqa: E402
from scipy.optimize import brentq  # noqa: E402
from scipy.sparse.linalg import spsolve  # noqa: E402

BETA = 1.0
RHO_WB = 1.7734530718064692   # WAND-BETA lauf-69/b1.json, f_z (beta = 1)
ATOL_REL = 1e-3   # atol = ATOL_REL * rtol (Rahmenspalten sind orthonormiert, Betrag 1)
NEWTON_IT = 6


# ----------------------------------------------------------------------------------------------------------------
# Hintergrund
# ----------------------------------------------------------------------------------------------------------------
class Hintergrund:
    def __init__(self, beta, eps, h, schritte=5, xl=-40.0, xr=47.0):
        self.beta, self.eps, self.h = beta, eps, h
        self.OM = math.sqrt(1.0 - 1.0 / (4.0 * beta))
        self.Sc = 1.0 / (2.0 * beta)
        self.fc = math.sqrt(self.Sc)
        self.rate = 1.0 / math.sqrt(beta)
        self.info = {}
        self.spl = None
        if eps == 0.0:
            self.info = {"art": "analytisch f0"}
            return
        N = int(round((xr - xl) / h))
        LD = np.longdouble
        x = xl + h * np.arange(N + 1)
        j0 = int(round(-xl / h))
        assert abs(x[j0]) < 1e-12
        x[j0] = 0.0
        xL = LD(xl) + LD(h) * np.arange(N + 1, dtype=LD)
        xL[j0] = LD(0)
        fL = self.f0_vec(xL)                      # Newton-Zustand in erweiterter Genauigkeit (Residuum ebenso)
        delta = 0.0
        D1 = sp.diags([1.0, -8.0, 8.0, -1.0], [-2, -1, 1, 2], shape=(N + 1, N + 1), format="csr") / (12.0 * h)
        D2 = sp.diags([-1.0, 16.0, -30.0, 16.0, -1.0], [-2, -1, 0, 1, 2], shape=(N + 1, N + 1),
                      format="csr") / (12.0 * h * h)
        D4 = sp.diags([-1.0, 12.0, -39.0, 56.0, -39.0, 12.0, -1.0], [-3, -2, -1, 0, 1, 2, 3], shape=(N + 1, N + 1),
                      format="csr") / (6.0 * h ** 4)
        I = sp.identity(N + 1, format="csr")
        b, OM2 = beta, self.OM ** 2
        bL, OM2L, hL = LD(beta), LD(1) - LD(1) / (LD(4) * LD(beta)), LD(h)
        f_phase = self.f0_vec(np.array([LD(0)], dtype=LD))[0]
        fcL = np.sqrt(LD(1) / (LD(2) * LD(beta)))

        def residuum(fv, e, dl):
            # Innere Gleichung j = 3..N-3 in long double: e D4 f - D2 f + dl D1 f + (U'(f^2) - om^2) f
            j = slice(3, N - 2)
            fm3, fm2, fm1, f00 = fv[0:N - 5], fv[1:N - 4], fv[2:N - 3], fv[3:N - 2]
            fp1, fp2, fp3 = fv[4:N - 1], fv[5:N], fv[6:N + 1]
            d4 = (-fm3 + 12 * fm2 - 39 * fm1 + 56 * f00 - 39 * fp1 + 12 * fp2 - fp3) / (6 * hL ** 4)
            d2 = (-fm2 + 16 * fm1 - 30 * f00 + 16 * fp1 - fp2) / (12 * hL * hL)
            d1 = (fm2 - 8 * fm1 + 8 * fp1 - fp2) / (12 * hL)
            S_ = f00 * f00
            g = (LD(1) - 2 * S_ + 3 * bL * S_ * S_ - OM2L) * f00
            del j
            return LD(e) * d4 - d2 + LD(dl) * d1 + g, d1

        verlauf = []
        for s in range(1, schritte + 1):
            e = eps * s / schritte
            for it in range(NEWTON_IT):
                f = fL.astype(float)
                S = f * f
                Vp = 1.0 - OM2 - 6.0 * S + 15.0 * b * S * S
                Fi, d1L = residuum(fL, e, delta)
                F = np.zeros(N + 2)
                F[3:N - 2] = Fi.astype(float)
                F[0:3] = (fL[0:3] - fcL).astype(float)
                F[N - 2:N + 1] = fL[N - 2:N + 1].astype(float)
                F[N + 1] = float(fL[j0] - f_phase)
                L = (e * D4 - D2 + delta * D1 + sp.diags(Vp)).tocsr()
                A_f = sp.vstack([I[0:3, :], L[3:N - 2, :], I[N - 2:N + 1, :], I[j0:j0 + 1, :]])
                col = np.zeros(N + 2)
                col[3:N - 2] = d1L.astype(float)
                A = sp.hstack([A_f, sp.csr_matrix(col.reshape(-1, 1))]).tocsc()
                dz = spsolve(A, -F)
                fL = fL + dz[:N + 1].astype(LD)
                delta = delta + float(dz[N + 1])
                res = float(np.max(np.abs(F)))
                mdz = float(np.max(np.abs(dz[:N + 1])))
                if mdz < 1e-13 and it > 0:      # Rauschgrenze der Residuen (long double), sonst NEWTON_IT Schritte
                    break
            verlauf.append({"eps": e, "iter": it + 1, "res_vor_letztem": res, "delta": delta, "max_dz": mdz})
        Fi, _ = residuum(fL, eps, delta)
        f0L = self.f0_vec(xL)
        self.info = {"art": "FD-Newton 4. Ordnung (Residuum long double)", "N": N, "h": h, "xl": xl, "xr": xr,
                     "delta": float(delta), "rest_innen_max": float(np.max(np.abs(Fi))), "verlauf": verlauf,
                     "max_abw_f0": float(np.max(np.abs(fL - f0L))), "f_bei_0": float(fL[j0]),
                     "longdouble_eps": float(np.finfo(LD).eps)}
        self.x = x
        self.df = (fL - f0L).astype(float)
        self.spl = make_interp_spline(x, self.df, k=5)

    def f0_vec(self, x):
        if x.dtype == np.longdouble:
            LD = np.longdouble
            Sc = LD(1) / (LD(2) * LD(self.beta))
            return np.sqrt(Sc / (LD(1) + np.exp(x / np.sqrt(LD(self.beta)))))
        return np.sqrt(self.Sc / (1.0 + np.exp(self.rate * x)))

    def S(self, x):
        f = math.sqrt(self.Sc / (1.0 + math.exp(self.rate * x)))
        if self.spl is not None:
            f += float(self.spl(x))
        return f * f


# ----------------------------------------------------------------------------------------------------------------
# Modell der Schwankungen
# ----------------------------------------------------------------------------------------------------------------
class Modell:
    def __init__(self, bg, rtol):
        self.bg, self.eps, self.rtol = bg, bg.eps, rtol
        b = bg.beta
        self.OM, self.beta = bg.OM, b
        sb = math.sqrt(b)
        self.xa, self.xb, self.xm = -36.0 * sb, 43.0 * sb, 0.0
        self.n = 4 if self.eps == 0.0 else 8
        Sc = bg.Sc
        self.W_in, self.C_in = 1.0 - 4.0 * Sc + 9.0 * b * Sc * Sc, -2.0 * Sc + 6.0 * b * Sc * Sc
        if self.eps > 0.0:
            self.dseg = min(2.0, 12.0 * math.sqrt(self.eps))
        else:
            self.dseg = 2.0

    def koeff(self, x):
        S = self.bg.S(x)
        b = self.beta
        return 1.0 - 4.0 * S + 9.0 * b * S * S, -2.0 * S + 6.0 * b * S * S

    def rhs_fabrik(self, rho, m):
        am, ap = (rho - self.OM) ** 2, (rho + self.OM) ** 2
        eps, n = self.eps, self.n

        def rhs(x, y):
            Z = y.reshape(n, m)
            W, C = self.koeff(x)
            Y0, Y1 = Z[0], Z[1]
            v0 = (W - am) * Y0 + C * Y1
            v1 = C * Y0 + (W - ap) * Y1
            dZ = np.empty_like(Z)
            if n == 4:
                dZ[0:2] = Z[2:4]
                dZ[2] = v0
                dZ[3] = v1
            else:
                dZ[0:6] = Z[2:8]
                dZ[6] = (Z[4] - v0) / eps
                dZ[7] = (Z[5] - v1) / eps
            return dZ.reshape(-1)
        return rhs

    # ---- asymptotische Moden ---------------------------------------------------------------------------------
    def wurzeln(self, mu):
        """Liste von (typ, wert, zweig) fuer eps lam^4 - lam^2 + mu = 0; typ 'r' (lam = +-wert) oder 'i' (lam = +-i wert)."""
        eps = self.eps
        out = []
        if eps == 0.0:
            out.append(("r", math.sqrt(mu), "alt") if mu > 0 else ("i", math.sqrt(-mu), "alt"))
            return out
        D = 1.0 - 4.0 * eps * mu
        if D <= 0.0:
            raise ValueError(f"komplexe Wurzeln: eps={eps}, mu={mu}, D={D}")
        sD = math.sqrt(D)
        s_klein = 2.0 * mu / (1.0 + sD)          # ~ mu
        s_gross = (1.0 + sD) / (2.0 * eps)        # ~ 1/eps
        out.append(("r", math.sqrt(s_klein), "alt") if s_klein > 0 else ("i", math.sqrt(-s_klein), "alt"))
        out.append(("r", math.sqrt(s_gross), "neu") if s_gross > 0 else ("i", math.sqrt(-s_gross), "neu"))
        return out

    def modenvektor(self, u, lam):
        u = np.asarray(u, dtype=complex)
        if self.n == 4:
            return np.concatenate([u, lam * u])
        return np.concatenate([u, lam * u, lam ** 2 * u, lam ** 3 * u])

    def jform(self, y, z):
        if self.n == 4:
            return y[0:2] @ z[2:4] - y[2:4] @ z[0:2]
        Y0, Y1, Y2, Y3 = y[0:2], y[2:4], y[4:6], y[6:8]
        Z0, Z1, Z2, Z3 = z[0:2], z[2:4], z[4:6], z[6:8]
        return (Y0 @ Z1 - Y1 @ Z0) - self.eps * (Y0 @ Z3 - Y1 @ Z2 + Y2 @ Z1 - Y3 @ Z0)

    def fluss(self, v):
        return float((self.jform(np.conj(v), v) / 2j).real)

    def eigen(self, ende, rho):
        am, ap = (rho - self.OM) ** 2, (rho + self.OM) ** 2
        if ende == "aus":
            mus = [(1.0 - am, np.array([1.0, 0.0]), "A"), (1.0 - ap, np.array([0.0, 1.0]), "B")]
        else:
            P = np.array([[self.W_in - am, self.C_in], [self.C_in, self.W_in - ap]])
            lam, vec = np.linalg.eigh(P)
            e1, e2 = vec[:, 0].copy(), vec[:, 1].copy()
            if e1[0] < 0:
                e1 = -e1
            if e2[0] < 0:
                e2 = -e2
            if not (lam[0] < 0.0 < lam[1]):
                raise ValueError(f"Innenmatrix nicht ein laufend / ein abklingend: {lam}")
            mus = [(lam[0], e1, "e1"), (lam[1], e2, "e2")]
        moden = []
        for mu, u, kanal in mus:
            for typ, w, zweig in self.wurzeln(mu):
                moden.append({"kanal": kanal, "zweig": zweig, "typ": typ, "wert": w, "u": u, "mu": mu})
        return moden

    def rahmen_start(self, ende, rho, zweck):
        """zweck 'E' (reell, fuer die Stille-Funktion) oder 'S' (komplex, Streuung). Gibt Spalten (n x m), Etiketten,
        Zahl der laufenden Endspalten und Flusse zurueck."""
        moden = self.eigen(ende, rho)
        abkl, lauf, etik, fl = [], [], [], []
        # abklingende Spalten: aussen lam < 0 (abklingend nach +inf), innen lam > 0 (abklingend nach -inf)
        sgn = -1.0 if ende == "aus" else 1.0
        abk_liste = sorted([m for m in moden if m["typ"] == "r"], key=lambda m: -m["wert"])   # schnell zuerst
        for m in abk_liste:
            abkl.append(self.modenvektor(m["u"], sgn * m["wert"]))
            etik.append(f"{m['kanal']}-{m['zweig']}-abkl")
        laufend = [m for m in moden if m["typ"] == "i"]
        if zweck == "E":
            if ende == "innen":            # innen beschraenkt: laufende Paare (reelle Basis) dazu; aussen nur abklingend
                for m in laufend:
                    v = self.modenvektor(m["u"], 1j * m["wert"])
                    lauf += [v.real.astype(complex), v.imag.astype(complex)]
                    etik += [f"{m['kanal']}-{m['zweig']}-re", f"{m['kanal']}-{m['zweig']}-im"]
            cols = np.array(abkl + lauf).T.real.copy()
            return cols, etik, 0, []
        einfall = None
        for m in laufend:
            vp = self.modenvektor(m["u"], 1j * m["wert"])
            vm = self.modenvektor(m["u"], -1j * m["wert"])
            fp, fm = self.fluss(vp), self.fluss(vm)
            if ende == "aus":
                v, f_ = (vp, fp) if fp > 0 else (vm, fm)          # auslaufend nach rechts
                lauf.append(v)
                fl.append(f_)
                etik.append(f"{m['kanal']}-{m['zweig']}-aus")
            else:
                v, f_ = (vm, fm) if fm < 0 else (vp, fp)          # nach links laufend (reflektiert)
                lauf.append(v)
                fl.append(f_)
                etik.append(f"{m['kanal']}-{m['zweig']}-refl")
                if m["kanal"] == "e1" and m["zweig"] == "alt":
                    einfall = (vp, fp) if fp > 0 else (vm, fm)
        if ende == "innen":
            lauf.append(einfall[0])
            fl.append(einfall[1])
            etik.append("e1-alt-einfall")
        cols = np.array(abkl + lauf, dtype=complex).T.copy()
        return cols, etik, len(lauf), fl

    def integriere(self, cols, x0, x1, rho, rtol, n_trail):
        n, m = cols.shape
        komplex = np.iscomplexobj(cols)
        Q, R = np.linalg.qr(cols)
        d = np.diag(R)
        ph = d / np.abs(d)
        Q = Q * ph
        R = (R.T / ph).T if not komplex else (np.conj(ph)[:, None] * R)
        if not komplex:
            Q, R = Q.real, R.real
        trail = R[m - n_trail:, m - n_trail:].copy() if n_trail else None
        logs = 0.0
        if n_trail:
            sc = float(np.max(np.abs(trail)))
            trail /= sc
            logs += math.log(sc)
        rhs = self.rhs_fabrik(rho, m)
        richt = 1.0 if x1 > x0 else -1.0
        nseg = max(1, int(math.ceil(abs(x1 - x0) / self.dseg)))
        xs = np.linspace(x0, x1, nseg + 1)
        nfev = 0
        for i in range(nseg):
            sol = solve_ivp(rhs, (xs[i], xs[i + 1]), Q.reshape(-1), method="DOP853", rtol=rtol, atol=ATOL_REL * rtol)
            if not sol.success:
                raise RuntimeError(sol.message)
            nfev += sol.nfev
            Y = sol.y[:, -1].reshape(n, m)
            Q, R = np.linalg.qr(Y)
            d = np.diag(R)
            if komplex:
                ph = d / np.abs(d)
                Q = Q * ph
                R = np.conj(ph)[:, None] * R
            else:
                sg = np.sign(d)
                Q = Q * sg
                R = sg[:, None] * R
            if n_trail:
                trail = R[m - n_trail:, m - n_trail:] @ trail
                sc = float(np.max(np.abs(trail)))
                trail /= sc
                logs += math.log(sc)
        del richt
        return Q, trail, logs, nfev

    def E(self, rho, rtol=None):
        rtol = self.rtol if rtol is None else rtol
        co, _, _, _ = self.rahmen_start("aus", rho, "E")
        ci, _, _, _ = self.rahmen_start("innen", rho, "E")
        Qo, _, _, n1 = self.integriere(co, self.xb, self.xm, rho, rtol, 0)
        Qi, _, _, n2 = self.integriere(ci, self.xa, self.xm, rho, rtol, 0)
        return float(np.linalg.det(np.hstack([Qo, Qi]))), n1 + n2

    def streuung(self, rho, rtol=None):
        rtol = self.rtol if rtol is None else rtol
        co, eo, ro, flo = self.rahmen_start("aus", rho, "S")
        ci, ei, ri, fli = self.rahmen_start("innen", rho, "S")
        Qo, To, lo, n1 = self.integriere(co, self.xb, self.xm, rho, rtol, ro)
        Qi, Ti, li, n2 = self.integriere(ci, self.xa, self.xm, rho, rtol, ri)
        po, pi = co.shape[1], ci.shape[1]
        M = np.hstack([Qo, -Qi[:, :pi - 1]])
        c = np.linalg.solve(M, Qi[:, pi - 1])
        c_o = c[:po]
        c_i = np.concatenate([c[po:], [1.0]])
        # alpha = R^-1 c, nur die laufenden Endkomponenten (Endblock der Dreiecksmatrix)
        a_o = np.linalg.solve(To, c_o[po - ro:]) * math.exp(-lo)
        a_i = np.linalg.solve(Ti, c_i[pi - ri:]) * math.exp(-li)
        a_inc = a_i[-1]
        f_inc = fli[-1]
        out = {"rho": rho, "kanaele_aus": {}, "kanaele_innen": {}}
        T_aus, R_innen = 0.0, 0.0
        for k in range(ro):
            amp = a_o[k] / a_inc
            Tk = abs(amp) ** 2 * abs(flo[k]) / abs(f_inc)
            out["kanaele_aus"][eo[po - ro + k]] = {"amp_abs": float(abs(amp)), "T": float(Tk), "fluss": flo[k]}
            T_aus += Tk
        for k in range(ri - 1):
            amp = a_i[k] / a_inc
            Rk = abs(amp) ** 2 * abs(fli[k]) / abs(f_inc)
            out["kanaele_innen"][ei[pi - ri + k]] = {"amp_abs": float(abs(amp)), "R": float(Rk), "fluss": fli[k]}
            R_innen += Rk
        out["T_aus"] = float(T_aus)
        out["R_innen"] = float(R_innen)
        out["flussbilanz"] = float(T_aus + R_innen - 1.0)
        out["nfev"] = n1 + n2
        out["cond_M"] = float(np.linalg.cond(M))
        return out


def suche(mod, rho_m, hb, n_scan, rtol_scan=1e-8):
    rs = np.linspace(rho_m - hb, rho_m + hb, n_scan)
    werte = [mod.E(float(r), rtol_scan)[0] for r in rs]
    null = []
    for i in range(n_scan - 1):
        if werte[i] == 0.0 or werte[i] * werte[i + 1] < 0.0:
            a, b = float(rs[i]), float(rs[i + 1])
            # erst auf der Abtast-Toleranz klammern, dann mit voller Toleranz verfeinern
            try:
                z = brentq(lambda r: mod.E(r)[0], a, b, xtol=1e-14, rtol=1e-15, maxiter=200)
            except ValueError:
                # Korrektur nach dem Einfrieren (04.10. 00:36): Liegt ein Abtastpunkt praktisch auf der Nullstelle
                # (eps = 0: Fenstermitte = rho_WB), kann E dort bei voller Toleranz das Vorzeichen wechseln.
                # Dann mit den Nachbarpunkten klammern.
                a2, b2 = float(rs[max(i - 1, 0)]), float(rs[min(i + 2, n_scan - 1)])
                z = brentq(lambda r: mod.E(r)[0], a2, b2, xtol=1e-14, rtol=1e-15, maxiter=200)
            if any(abs(z - z0) < 1e-12 for z0 in null):
                continue
            null.append(z)
    return [float(r) for r in rs], werte, null


def main():
    eps, h_bg, rtol, pfad = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
    rho_m = float(sys.argv[5]) if len(sys.argv) > 5 else RHO_WB
    hb = float(sys.argv[6]) if len(sys.argv) > 6 else 0.15
    n_scan = int(sys.argv[7]) if len(sys.argv) > 7 else 61
    t0 = time.time()
    beta = float(sys.argv[8]) if len(sys.argv) > 8 else BETA   # nur fuer Rauchlauf des eps = 0-Pfads (beta = 0,6)
    # Korrektur nach dem Einfrieren (04.10. ~00:52): rechtes Hintergrundende als 9. Argument. Bei xr = 47 ist die wahre
    # Wand dort noch ~6e-11 (Abfall e^{-x/2}); f = 0 am Rand regt fuer eps < 0 stehende Schwanzwellen (k0) an.
    xr = float(sys.argv[9]) if len(sys.argv) > 9 else 47.0
    bg_modus = sys.argv[10] if len(sys.argv) > 10 else "fd"
    if bg_modus == "f0":       # Diagnose nach dem Einfrieren: eps nur in den Schwankungen, Hintergrund = f0 (ohne Schwanz)
        bg = Hintergrund(beta, 0.0, h_bg, xr=xr)
        bg.eps = eps
        bg.info = {"art": "Diagnose: analytisch f0, eps nur in den Schwankungen"}
    else:
        bg = Hintergrund(beta, eps, h_bg, xr=xr)
    mod = Modell(bg, rtol)
    out = {"version": 1, "beta": beta, "eps": eps, "h_bg": h_bg, "rtol": rtol, "omega": mod.OM,
           "xa": mod.xa, "xb": mod.xb, "xm": mod.xm, "dseg": mod.dseg, "hintergrund": bg.info,
           "rho_mitte": rho_m, "halbbreite": hb, "n_scan": n_scan, "xr_bg": xr}
    print(f"eps {eps} h {h_bg} rtol {rtol}: Hintergrund {json.dumps(bg.info)[:300]} ({time.time() - t0:.1f} s)",
          flush=True)
    # Kanalbild an der WAND-BETA-Stelle
    out["moden_aus"] = [{k: (v if k != "u" else list(map(float, v))) for k, v in m.items()}
                        for m in mod.eigen("aus", rho_m)]
    out["moden_innen"] = [{k: (v if k != "u" else list(map(float, v))) for k, v in m.items()}
                          for m in mod.eigen("innen", rho_m)]
    rs, werte, null = suche(mod, rho_m, hb, n_scan)
    if not null:                      # Rueckfall laut Plan: weites Fenster
        out["erste_abtastung"] = {"rho": rs, "E": werte}
        hb, n_scan = 0.15, 61
        out["halbbreite"], out["n_scan"] = hb, n_scan
        rs, werte, null = suche(mod, rho_m, hb, n_scan)
    out["abtastung"] = {"rho": rs, "E": werte}
    print(f"eps {eps}: Abtastung fertig, Nullstellen {null} ({time.time() - t0:.1f} s)", flush=True)
    erg = []
    for z in null:
        e = {"rho_z": z, "verschiebung": z - RHO_WB}
        e["E_bei_rho_z"] = mod.E(z)[0]
        e["streuung"] = {}
        for off in (0.0, -1e-6, 1e-6, -1e-5, 1e-5, -1e-3, 1e-3):
            e["streuung"][f"{off:+.0e}"] = mod.streuung(z + off)
        s0 = e["streuung"]["+0e+00"]
        ref = e["streuung"]["+1e-03"]["T_aus"]
        e["T_aus_bei_rho_z"] = s0["T_aus"]
        e["T_aus_rel"] = s0["T_aus"] / ref if ref > 0 else None
        neu = {k: v for k, v in s0["kanaele_aus"].items() if "-neu-" in k}
        e["P_neu_aus"] = float(sum(v["T"] for v in neu.values())) if neu else 0.0
        e["amp_neu_aus_max"] = float(max(v["amp_abs"] for v in neu.values())) if neu else 0.0
        neu_i = {k: v for k, v in s0["kanaele_innen"].items() if "-neu-" in k}
        e["P_neu_innen"] = float(sum(v["R"] for v in neu_i.values())) if neu_i else 0.0
        alt = {k: v for k, v in s0["kanaele_aus"].items() if "-alt-" in k}
        e["T_alt_aus"] = float(sum(v["T"] for v in alt.values()))
        e["flussbilanz"] = s0["flussbilanz"]
        # Aufloesungsprobe: dieselbe Streuung mit 10-fach groeberer Toleranz (numerisches Rauschen ~ rtol)
        sl = mod.streuung(z, 10.0 * rtol)
        neu_l = {k: v for k, v in sl["kanaele_aus"].items() if "-neu-" in k}
        e["lose_10rtol"] = {"T_aus": sl["T_aus"], "flussbilanz": sl["flussbilanz"],
                            "P_neu_aus": float(sum(v["T"] for v in neu_l.values())) if neu_l else 0.0,
                            "amp_neu_aus_max": float(max(v["amp_abs"] for v in neu_l.values())) if neu_l else 0.0,
                            "kanaele_aus": sl["kanaele_aus"]}
        erg.append(e)
        print(f"eps {eps}: rho_z = {z:.13f} (Verschiebung {z - RHO_WB:+.6e}), T_aus = {s0['T_aus']:.3e}, "
              f"T_alt = {e['T_alt_aus']:.3e}, P_neu_aus = {e['P_neu_aus']:.3e}, amp_neu = {e['amp_neu_aus_max']:.3e}, "
              f"P_neu_innen = {e['P_neu_innen']:.3e}, Fluss {s0['flussbilanz']:.1e} ({time.time() - t0:.1f} s)",
              flush=True)
    out["nullstellen"] = erg
    out["sek"] = time.time() - t0
    with open(pfad + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1, default=lambda o: float(o) if isinstance(o, (np.floating,)) else str(o))
    os.replace(pfad + ".tmp", pfad)
    print(f"eps {eps}: fertig, {len(erg)} Nullstellen, {out['sek']:.1f} s", flush=True)


if __name__ == "__main__":
    main()
