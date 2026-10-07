# ZUFALLS-REIBUNG-1 (Runde 36): Q-Ball von M1 mit Startschnelle v in einer Kette mit zufaelliger oertlicher Masse.
#   1D-Gitter (Abstand H = 0,1), komplexes psi_n, p_n = d psi_n/dt, kein aeusseres Feld.
#   H = h sum(|p_n|^2 + U_n(S_n)) + (1/h) sum |psi_{n+1} - psi_n|^2,  S = |psi|^2,
#   U_n(S) = (1 + s(t) eta_n) S - S^2 + S^3/2,  eta_n unabhaengig normalverteilt (Saat fest, globaler Platzindex),
#   s(t) = sigma f(t/T_R), f(u) = u - sin(2 pi u)/(2 pi) (C^2-Einschalten), s = sigma fuer t >= T_R.
#   Bewegung: p_n' = (psi_{n+1} + psi_{n-1} - 2 psi_n)/h^2 - U_n'(S_n) psi_n  (im Schwamm zusaetzlich - a_n p_n).
#   Ladung Q = 2 h sum Im(conj(psi) p) (psi ~ e^{+i omega t}: Q > 0); jeder Teilschritt erhaelt Q exakt.
#   dH/dt = s'(t) h sum eta_n S_n (nur waehrend des Einschaltens); Arbeit W schema-treu an den Stoessen summiert.
# Integrator: Yoshida 4. Ordnung (Drift psi, Stoss mit s(t) zur Stosszeit). Schwamm exakt p -> p exp(-a dt/2) vor und
#   nach jedem Schritt, Abfluss gebucht. Mitlaufendes Fenster mit exakter Gittertranslation (Unordnung haengt am
#   globalen Platz); was herausfaellt, wird gebucht.
# Start: stationaere Gitterloesung bei omega^2 = 0,7 (Newton, platzzentriert), als kubischer Spline phi(x) gelesen und
#   Lorentz-geboostet: psi_n = phi(g xi) e^{-i om g v xi}, p_n = g(-v phi'(g xi) + i om phi(g xi)) e^{-i om g v xi},
#   xi = x_n - X0, g = gamma(v). Fuer v = 0 ist das exakt die Gitterloesung.
# Familie M(Q): Gitter-Q-Baelle bei omega^2 = 0,66 ... 0,94 (Ruheenergie und Ladung) fuer die Auswertung.
# Aufruf (nur ueber kleintest.sh):
#   reibung.py <name> <v> <sigma> <saat> <t_end> <dt> [wand_s]
#   Ausgabe <name>.npz (Zeitreihen) und <name>.json (Kopf).
import sys, os, json, time, hashlib, math
import numpy as np
from scipy.linalg import solve_banded
from scipy.interpolate import CubicSpline

H_GITTER = 0.1
OMEGA2 = 0.7
T_R = 200.0           # Einschaltdauer der Unordnung
T_A = 400.0           # Beginn des Messfensters (fuer die Auswertung, im Kopf vermerkt)
W1 = 1.0 / (2.0 - 2.0 ** (1.0 / 3.0))
W0 = -(2.0 ** (1.0 / 3.0)) * W1
CS = (W1 / 2, (W0 + W1) / 2, (W0 + W1) / 2, W1 / 2)
DS = (W1, W0, W1)
CC = (CS[0], CS[0] + CS[1], CS[0] + CS[1] + CS[2])
DS_MESS = 0.5          # Messabstand
R_X = 10.0             # cos^2-Gewicht fuer den Ladungsschwerpunkt (wie QBALL-GITTER-1)
R1 = 14.0              # Ballfenster: Gewicht 1 fuer |xi| <= R1, C^2-Abfall bis R2
R2 = 20.0
L_W = 240.0            # Fensterlaenge
FB = 0.5               # Sollort des Balls im Fenster
VERSCHUB = 10.0        # Fensterverschiebung (ganze Plaetze)
L_ABS = 50.0           # Schwammlaenge je Ende
ETA_MAX = 1.0          # Schwammstaerke am Ende (quadratische Rampe)
L_HALB_NEWTON = 60.0
NMIN = -30000          # globaler Platzbereich der Unordnung [NMIN, NMAX)
NMAX = 60000
FAMILIE_OM2 = (0.66, 0.68, 0.69, 0.70, 0.71, 0.72, 0.74, 0.76, 0.78, 0.80, 0.82, 0.84, 0.86, 0.88, 0.90, 0.92, 0.94)
FELDER = ["t", "X", "Qwin", "Ewin", "Vwin", "Pwin", "Qdom", "H", "Eabs", "Qabs", "Edrop", "Qdrop", "W", "amax", "n0",
          "sig"]


def U0(S):
    return S * (1.0 - S + 0.5 * S * S)


def Up0(S):
    return 1.0 - 2.0 * S + 1.5 * S * S


def Upp0(S):
    return -2.0 + 3.0 * S


def gitter_ball(h, om2, L_halb):
    """Stationaere Gitterloesung phi_n (reell), platzzentriert; Newton auf n = 0..M-1 mit phi_{-1} = phi_1, phi_M = 0."""
    M = int(round(L_halb / h))
    x = np.arange(M) * h
    k2 = 1.0 - om2
    k = math.sqrt(k2)
    D = math.sqrt(1.0 - 2.0 * k2)
    phi = np.sqrt(2.0 * k2 / (1.0 + D * np.cosh(np.clip(2.0 * k * x, 0, 700))))
    h2 = 1.0 / (h * h)
    it = 0
    for it in range(80):
        S = phi * phi
        up = np.empty(M + 1); up[:M] = phi; up[M] = 0.0
        lo = np.empty(M); lo[0] = phi[1]; lo[1:] = phi[:-1]
        R = (up[1:M + 1] + lo - 2.0 * phi) * h2 + (om2 - Up0(S)) * phi
        ab = np.zeros((3, M))
        ab[0, 1:] = h2
        ab[0, 1] = 2.0 * h2
        ab[1, :] = -2.0 * h2 + om2 - Up0(S) - 2.0 * S * Upp0(S)
        ab[2, :-1] = h2
        dphi = solve_banded((1, 1), ab, -R)
        phi = phi + dphi
        if float(np.max(np.abs(dphi))) < 1e-13 and float(np.max(np.abs(R))) < 1e-11:
            break
    S = phi * phi
    up = np.empty(M + 1); up[:M] = phi; up[M] = 0.0
    lo = np.empty(M); lo[0] = phi[1]; lo[1:] = phi[:-1]
    R = (up[1:M + 1] + lo - 2.0 * phi) * h2 + (om2 - Up0(S)) * phi
    return phi, dict(newton_iter=it + 1, newton_rest=float(np.max(np.abs(R))), phi0=float(phi[0]), M_halb=M)


def ruhe_QM(phi, h, om2):
    """Ladung und Ruheenergie der symmetrischen Gitterloesung (volle Kette)."""
    full = np.concatenate([phi[::-1], phi[1:]])
    om = math.sqrt(om2)
    S = full * full
    Q = 2.0 * h * om * float(np.sum(S))
    d = np.diff(full)
    M = float(h * np.sum(om2 * S + U0(S)) + np.sum(d * d) / h + (full[0] ** 2 + full[-1] ** 2) / h)
    return Q, M


def fenster_c2(xi):
    """Gewicht 1 fuer |xi| <= R1, Abfall f(s) = 1 - s + sin(2 pi s)/(2 pi) bis R2 (C^2), 0 danach."""
    a = np.abs(xi)
    s = np.clip((a - R1) / (R2 - R1), 0.0, 1.0)
    return 1.0 - s + np.sin(2.0 * math.pi * s) / (2.0 * math.pi)


def main():
    a = sys.argv
    name = a[1]; v = float(a[2]); sigma = float(a[3]); saat = int(a[4]); t_end = float(a[5]); dt = float(a[6])
    wand = float(a[7]) if len(a) > 7 else 540.0
    t_wand0 = time.time()
    h = H_GITTER
    nsub = int(round(DS_MESS / dt))
    assert abs(nsub * dt - DS_MESS) < 1e-12, "DS_MESS kein Vielfaches von dt"
    N = int(round(L_W / h))
    om = math.sqrt(OMEGA2)
    h2inv = 1.0 / (h * h)

    # Familie M(Q) (Ruhe, Gitter)
    fam = []
    for om2 in FAMILIE_OM2:
        ph, nw = gitter_ball(h, om2, 150.0)
        Qf, Mf = ruhe_QM(ph, h, om2)
        fam.append(dict(om2=om2, Q=Qf, M=Mf, newton_rest=nw["newton_rest"], newton_iter=nw["newton_iter"]))

    # Startball: Gitterloesung, Spline, Lorentz-Boost
    phi, newton = gitter_ball(h, OMEGA2, L_HALB_NEWTON)
    Mh = len(phi)
    xs = (np.arange(2 * Mh - 1) - (Mh - 1)) * h
    prof = np.concatenate([phi[::-1], phi[1:]])
    spl = CubicSpline(xs, prof, bc_type="natural")
    dspl = spl.derivative()
    xmax = xs[-1]
    g = 1.0 / math.sqrt(1.0 - v * v)
    i_c = int(round(FB * L_W / h))
    X0 = i_c * h
    x_loc = np.arange(N) * h
    xi = x_loc - X0
    u = g * xi
    inn = np.abs(u) < xmax
    f = np.zeros(N); fp = np.zeros(N)
    f[inn] = spl(u[inn]); fp[inn] = dspl(u[inn])
    ph_tr = np.exp(-1j * om * g * v * xi)
    psi_start = f * ph_tr
    p_start = g * (-v * fp + 1j * om * f) * ph_tr
    Q_ruhe, M_ruhe = ruhe_QM(phi, h, OMEGA2)

    # Unordnung (globaler Platz n in [NMIN, NMAX), lokaler Platz j <-> n = n0 + j)
    rng = np.random.default_rng(saat)
    ETA = rng.standard_normal(NMAX - NMIN)

    def eta_lokal(n0):
        j0 = n0 - NMIN
        assert j0 >= 0 and j0 + N <= NMAX - NMIN, "Unordnung zu kurz"
        return ETA[j0:j0 + N]

    def s_von_t(t):
        if t >= T_R:
            return sigma
        uu = t / T_R
        return sigma * (uu - math.sin(2.0 * math.pi * uu) / (2.0 * math.pi))

    def sp_von_t(t):
        if t >= T_R:
            return 0.0
        return sigma * (1.0 - math.cos(2.0 * math.pi * t / T_R)) / T_R

    t_mess_ende = t_end
    k_ziel = int(math.ceil(t_end / DS_MESS - 1e-9))

    # Schwamm
    nabs = int(round(L_ABS / h))
    eta_l = ETA_MAX * np.clip(1.0 - x_loc[:nabs] / L_ABS, 0, None) ** 2
    eta_r = eta_l[::-1].copy()
    fh_l = np.exp(-eta_l * dt / 2); fh_r = np.exp(-eta_r * dt / 2)
    fv_l = fh_l * fh_l; fv_r = fh_r * fh_r
    sl_l = slice(0, nabs); sl_r = slice(N - nabs, N)
    i_soll = float(i_c)
    s_ver = int(round(VERSCHUB / h))

    Psi = np.zeros(N + 2, complex)
    psi = Psi[1:-1]
    psi[:] = psi_start
    p = p_start.copy()
    n0 = 0
    el = eta_lokal(n0).copy()
    acc = np.zeros(5)   # W, Eabs, Qabs, Edrop, Qdrop
    reihen = {fn: [] for fn in FELDER}
    S = np.empty(N); T = np.empty(N); A = np.empty(N, complex); B = np.empty(N, complex)
    wk = [0.0]

    def kick(coef, tt):
        st = s_von_t(tt)
        np.multiply(psi.real, psi.real, out=S)
        np.multiply(psi.imag, psi.imag, out=T)
        S.__iadd__(T)
        spt = sp_von_t(tt)
        if spt != 0.0:
            wk[0] += coef * spt * h * float(np.dot(el, S))
        np.multiply(S, 1.5, out=T); T.__isub__(2.0); T.__imul__(S); T.__iadd__(1.0 + 2.0 * h2inv)
        if st != 0.0:
            T.__iadd__(st * el)
        T.__imul__(coef)
        np.add(Psi[2:], Psi[:-2], out=A); A.__imul__(coef * h2inv)
        np.multiply(psi, T, out=B)
        A.__isub__(B)
        p.__iadd__(A)

    def schritt(k):
        t0 = k * dt
        np.multiply(p, CS[0] * dt, out=A); psi.__iadd__(A)
        kick(DS[0] * dt, t0 + CC[0] * dt)
        np.multiply(p, CS[1] * dt, out=A); psi.__iadd__(A)
        kick(DS[1] * dt, t0 + CC[1] * dt)
        np.multiply(p, CS[2] * dt, out=A); psi.__iadd__(A)
        kick(DS[2] * dt, t0 + CC[2] * dt)
        np.multiply(p, CS[3] * dt, out=A); psi.__iadd__(A)

    def daempfen(fl, fr):
        for sl, ff in ((sl_l, fl), (sl_r, fr)):
            ps = p[sl]; qs = psi[sl]
            eb = np.vdot(ps, ps).real; qb = np.vdot(qs, ps).imag
            ps *= ff
            ea = np.vdot(ps, ps).real; qa = np.vdot(qs, ps).imag
            acc[1] += h * (eb - ea); acc[2] += 2.0 * h * (qb - qa)

    def H_gesamt(st):
        Sx = psi.real ** 2 + psi.imag ** 2
        l = np.abs(psi[1:] - psi[:-1]) ** 2
        return float(h * np.sum(p.real ** 2 + p.imag ** 2 + U0(Sx) + st * el * Sx) + l.sum() / h
                     + (Sx[0] + Sx[-1]) / h)

    def Q_gesamt():
        return float(2.0 * h * np.vdot(psi, p).imag)

    def messen(t, Xprev):
        st = s_von_t(t)
        rho = 2.0 * (psi.real * p.imag - psi.imag * p.real)
        Qdom = float(h * rho.sum())
        xg = (n0 + np.arange(N)) * h
        Xs = Xprev
        ok = True
        for _ in range(200):
            j0 = max(0, int(math.floor((Xs - R_X) / h)) - n0); j1 = min(N - 1, int(math.ceil((Xs + R_X) / h)) - n0)
            if j1 < j0:
                ok = False; break
            xx = xg[j0:j1 + 1] - Xs
            wg = np.where(np.abs(xx) < R_X, np.cos((0.5 * math.pi / R_X) * xx) ** 2, 0.0)
            qq = rho[j0:j1 + 1] * wg; qs = float(qq.sum())
            if not qs > 0:
                ok = False; break
            dX = float((xx * qq).sum() / qs)
            Xs = Xs + dX
            if abs(dX) < 1e-12 * max(1.0, abs(Xs)):
                break
        Sx = psi.real ** 2 + psi.imag ** 2
        es = h * (p.real ** 2 + p.imag ** 2 + U0(Sx) + st * el * Sx)
        lnk = np.abs(psi[1:] - psi[:-1]) ** 2 / h
        Htot = float(es.sum() + lnk.sum() + (Sx[0] + Sx[-1]) / h)
        if ok:
            X = Xs
            i0 = max(1, int(math.floor((X - R2) / h)) - n0); i1 = min(N - 2, int(math.ceil((X + R2) / h)) - n0)
            w = fenster_c2(xg[i0:i1 + 1] - X)
            Qwin = float(h * np.sum(rho[i0:i1 + 1] * w))
            en = es[i0:i1 + 1] + 0.5 * (lnk[i0 - 1:i1] + lnk[i0:i1 + 1])
            Ewin = float(np.sum(en * w))
            Vwin = float(st * h * np.sum(el[i0:i1 + 1] * Sx[i0:i1 + 1] * w))
            Dp = (psi[i0 + 1:i1 + 2] - psi[i0 - 1:i1]) / (2.0 * h)
            Pwin = float(-2.0 * h * np.sum((np.conj(p[i0:i1 + 1]) * Dp).real * w))
            amax = float(np.sqrt(Sx[i0:i1 + 1].max()))
        else:
            X = float("nan"); Qwin = Ewin = Vwin = Pwin = amax = float("nan")
        r = dict(t=t, X=X, Qwin=Qwin, Ewin=Ewin, Vwin=Vwin, Pwin=Pwin, Qdom=Qdom, H=Htot, Eabs=float(acc[1]),
                 Qabs=float(acc[2]), Edrop=float(acc[3]), Qdrop=float(acc[4]), W=float(acc[0]), amax=amax,
                 n0=float(n0), sig=st)
        return r, (X if ok else Xprev), ok

    def verschieben(s, t):
        nonlocal n0, el
        st = s_von_t(t)
        Hb = H_gesamt(st); Qb = Q_gesamt()
        if s > 0:
            psi[:-s] = psi[s:].copy(); psi[-s:] = 0.0
            p[:-s] = p[s:].copy(); p[-s:] = 0.0
        else:
            m = -s
            psi[m:] = psi[:-m].copy(); psi[:m] = 0.0
            p[m:] = p[:-m].copy(); p[:m] = 0.0
        n0 += s
        el = eta_lokal(n0).copy()
        acc[3] += Hb - H_gesamt(st); acc[4] += Qb - Q_gesamt()

    Xprev = X0
    r, Xprev, ok = messen(0.0, Xprev)
    for fn in FELDER:
        reihen[fn].append(r[fn])
    E_start = r["Ewin"]; P_start = r["Pwin"]; Q_start = r["Qwin"]
    status = "fertig"
    k_mess = 0
    nmin_used = n0; nmax_used = n0 + N
    while k_mess < k_ziel:
        k0 = k_mess * nsub
        for j in range(nsub):
            daempfen(fh_l if j == 0 else fv_l, fh_r if j == 0 else fv_r)
            schritt(k0 + j)
        daempfen(fh_l, fh_r)
        acc[0] = wk[0]
        k_mess += 1
        t = k_mess * DS_MESS
        r, Xprev, ok = messen(t, Xprev)
        for fn in FELDER:
            reihen[fn].append(r[fn])
        if not np.all(np.isfinite(p)):
            status = "nan"; break
        if not ok:
            status = "verloren"; break
        il = Xprev / h - n0
        if il > i_soll + s_ver:
            verschieben(s_ver, t)
        elif il < i_soll - s_ver:
            verschieben(-s_ver, t)
        nmin_used = min(nmin_used, n0); nmax_used = max(nmax_used, n0 + N)
        if time.time() - t_wand0 > wand and k_mess < k_ziel:
            status = "unterbrochen"
            break
    j_lo = nmin_used - NMIN; j_hi = nmax_used - NMIN
    min_masse = float(np.min(1.0 + sigma * ETA[j_lo:j_hi]))
    kopf = dict(name=os.path.basename(name), v=v, gamma=g, sigma=sigma, saat=saat, h=h, omega2=OMEGA2, t_end=t_end,
                dt=dt, T_R=T_R, T_A=T_A, L_w=L_W, N=N, i_c=i_c, X0=X0, FB=FB, R_X=R_X, R1=R1, R2=R2, L_abs=L_ABS,
                eta_max=ETA_MAX, verschub=VERSCHUB, ds_mess=DS_MESS, NMIN=NMIN, NMAX=NMAX,
                Q_ruhe=Q_ruhe, M_ruhe=M_ruhe, E_start=E_start, P_start=P_start, Q_start=Q_start,
                Kontinuum_EP=[g * M_ruhe, g * M_ruhe * v], familie=fam,
                status=status, t_letzt=k_mess * DS_MESS, wandzeit_s=time.time() - t_wand0,
                n_global_bereich=[int(nmin_used), int(nmax_used)], min_1_plus_sigma_eta=min_masse,
                numpy=np.__version__, newton=newton,
                skript_sha256=hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
                ende_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    np.savez_compressed(name + ".npz", **{fn: np.array(reihen[fn], float) for fn in FELDER})
    json.dump(kopf, open(name + ".json", "w"), indent=1)
    Hs = np.array(reihen["H"]); Qd = np.array(reihen["Qdom"])
    bil = Hs + np.array(reihen["Eabs"]) + np.array(reihen["Edrop"]) - Hs[0] - np.array(reihen["W"])
    qb = Qd + np.array(reihen["Qabs"]) + np.array(reihen["Qdrop"]) - Qd[0]
    X = np.array(reihen["X"]); Qw = np.array(reihen["Qwin"])
    print(json.dumps(dict(status=status, t=k_mess * DS_MESS, Q_ruhe=Q_ruhe, M_ruhe=M_ruhe, E_start=E_start,
                          P_start=P_start, Q_start=Q_start, gM=g * M_ruhe, gMv=g * M_ruhe * v,
                          X_end=float(X[-1]), Qwin_end=float(Qw[-1]),
                          bilanz_E_max=float(np.max(np.abs(bil)) / M_ruhe), bilanz_Q_max=float(np.max(np.abs(qb)) / Q_ruhe),
                          min_masse=min_masse, newton=newton, wand_s=round(time.time() - t_wand0, 1))), flush=True)


if __name__ == "__main__":
    main()
