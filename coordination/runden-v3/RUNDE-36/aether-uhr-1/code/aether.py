# AETHER-UHR-1 (Runde 36): Merkt eine Uhr aus zwei Wellensorten, dass sie sich durchs Netz bewegt?
# Zwei gekoppelte Felder in 1+1D auf einem kontinuumsnahen Gitter (Abstand h).
#   Feld A (M1, komplex, c_A = 1): L_A = |A_t|^2 - |D_x A|^2 - U(|A|^2), U(S) = S - S^2 + S^3/2 (beta = 1/2),
#     D_x = d_x - i a(t), a' = E(t): gleichmaessiges Feld auf die A-Ladung in zeitlicher Eichung, Peierls-Phase th = h a.
#   Feld B (reell, Grenzgeschwindigkeit c_B, Masse m_B): L_B = (B_t^2 - c_B^2 B_x^2)/2 - (m_B^2 - g |A|^2) B^2/2.
#   Gitter-Hamiltonfunktion (Geisterplaetze = 0 an beiden Fensterenden):
#     H = h sum(|p|^2 + U(S)) + (1/h) sum|e^{-i th} A_{n+1} - A_n|^2 + h sum(q^2/2 + (m_B^2 - g S) B^2/2)
#         + (c_B^2/(2h)) sum (B_{n+1} - B_n)^2,  S = |A|^2, p = A', q = B'.
#   Bewegung: p_n' = (e^{-i th} A_{n+1} + e^{i th} A_{n-1} - 2 A_n)/h^2 - U'(S_n) A_n + (g/2) B_n^2 A_n
#             q_n' = c_B^2 (B_{n+1} + B_{n-1} - 2 B_n)/h^2 - (m_B^2 - g S_n) B_n
#   Ladung Q = h sum rho, rho = 2 Im(conj(A) p); Strom J = -2 Im(e^{-i th} sum conj(A_n) A_{n+1}); dH/dt = E J.
# Integrator: Yoshida 4. Ordnung (Drift A, B; Stoss mit th(t) zur Stosszeit), Arbeit W = sum d_i dt E(t_i) J_i.
#   Schwamm an beiden Enden (p, q -> exp(-eta dt/2) vor und nach jedem Schritt), Abfluss exakt gebucht.
#   Mitlaufendes Fenster: exakte Gittertranslation um VERSCHUB, wenn der Beutelmittelpunkt so weit vom Fenstermittelpunkt
#   entfernt ist; was herausfaellt, wird gebucht.
# Start: stationaerer Gitterbeutel (Newton mit Randzeile: Norm fest, omega^2 frei; Kontinuumsform mit Halbwertsbreite
#   L_ZIEL als Startwert) und B in der untersten Eigenmode des linearisierten B-Problems im Beutelprofil, B = b f,
#   B' = 0 (max|f| = 1).
# Beschleunigungsprotokoll: Ruhe T_p, dann dreimal (Rampe T_r mit E(t) = E_k sin^2(pi s/T_r), Plateau T_p ohne Feld).
#   E_k = 2 M0 (gamma_k v_k - gamma_{k-1} v_{k-1})/(Q0 T_r), Zielschnellen V_ZIEL.
# Aufruf (nur ueber kleintest.sh):
#   aether.py <name> <c_B> <h> <dt> <T_r> <T_p> <b> [t_stop|-] [wand_s]
#   Ausgabe <name>.npz (Zeitreihen, Profile, Momentaufnahmen) und <name>.json (Kopf); Checkpoint <name>.ckpt.npz bei
#   Wandzeit-Abbruch; ein erneuter Aufruf mit denselben Argumenten setzt fort.
import sys, os, json, time, hashlib, math
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve
from scipy.linalg import eigh_tridiagonal

L_ZIEL = 21.0          # Halbwertsbreite von |A|^2 des ruhenden Kontinuumsbeutels (Karte: Laenge >= 20)
M_B = 1.0              # B-Masse aussen
G_K = 1.0              # Kopplung g = m_B^2: B ist im Beutelinneren (S ~ 1) masselos (Hohlraummode der Karte)
V_ZIEL = (0.2, 0.4, 0.6)
DS_MESS = 0.25         # Messabstand
DS_SNAP = 40.0         # Abstand der Momentaufnahmen
L_W = 160.0            # Fensterlaenge
L_ABS = 30.0           # Schwammlaenge je Ende
ETA_MAX = 1.0          # Schwammstaerke am Ende (quadratische Rampe)
VERSCHUB = 5.0         # Fenster wird um 5 Laengeneinheiten verschoben
R_B = 5.0              # halbe Breite des mitbewegten B-Fensters (cos^2-Gewicht)
L_HALB_NEWTON = 55.0   # halbe Laenge der Newton-Kette
W1 = 1.0 / (2.0 - 2.0 ** (1.0 / 3.0))
W0 = -(2.0 ** (1.0 / 3.0)) * W1
CS = (W1 / 2, (W0 + W1) / 2, (W0 + W1) / 2, W1 / 2)
DS = (W1, W0, W1)
CC = (CS[0], CS[0] + CS[1], CS[0] + CS[1] + CS[2])
FELDER = ["t", "X", "LS", "LR", "XR", "thc", "sB", "Bc", "Q", "Qabs", "Qdrop", "H", "HB", "Eabs", "Edrop", "W", "Smax",
          "Rmax", "a", "n0"]


def U(S):
    return S * (1.0 - S + 0.5 * S * S)


def Up(S):
    return 1.0 - 2.0 * S + 1.5 * S * S


def Upp(S):
    return -2.0 + 3.0 * S


def kontinuum_D(L):
    """Kontinuumsbeutel S = 2k^2/(1 + D cosh(2 k x)), k^2 = (1 - D^2)/2; D so, dass die Halbwertsbreite = L."""
    lo, hi = -60.0, -0.5
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        D = math.exp(mid)
        f = math.acosh((1.0 + 2.0 * D) / D) / math.sqrt((1.0 - D * D) / 2.0) - L
        if f > 0:
            lo = mid
        else:
            hi = mid
    return math.exp(0.5 * (lo + hi))


def beutel(h):
    """Stationaerer Gitterbeutel phi_n (reell, platzzentriert) auf n = 0..M-1 mit phi_{-1} = phi_1, phi_M = 0.
    Newton mit Randzeile: Gesamtnorm h sum phi^2 (ganze Kette) = Kontinuumswert, omega^2 als Unbekannte."""
    D = kontinuum_D(L_ZIEL)
    k2 = (1.0 - D * D) / 2.0
    k = math.sqrt(k2)
    M = int(round(L_HALB_NEWTON / h))
    x = np.arange(M) * h
    S_c = 2.0 * k2 / (1.0 + D * np.cosh(np.clip(2.0 * k * x, 0, 700)))
    phi = np.sqrt(S_c)
    om2 = 1.0 - k2
    wg = np.full(M, 2.0)
    wg[0] = 1.0
    N_ziel = h * float(np.sum(wg * S_c))
    h2 = 1.0 / (h * h)

    def rest(phi, om2):
        S = phi * phi
        up = np.empty(M + 1); up[:M] = phi; up[M] = 0.0
        lo = np.empty(M); lo[0] = phi[1]; lo[1:] = phi[:-1]
        R = (up[1:M + 1] + lo - 2.0 * phi) * h2 + (om2 - Up(S)) * phi
        C = h * float(np.sum(wg * S)) - N_ziel
        return R, C

    it = 0
    for it in range(80):
        S = phi * phi
        R, C = rest(phi, om2)
        diag = -2.0 * h2 + om2 - Up(S) - 2.0 * S * Upp(S)
        sup = np.full(M - 1, h2); sup[0] = 2.0 * h2
        sub = np.full(M - 1, h2)
        J = sp.diags([sub, diag, sup], [-1, 0, 1], shape=(M, M), format="csr")
        col = sp.csr_matrix(phi.reshape(-1, 1))
        row = sp.csr_matrix((2.0 * h * wg * phi).reshape(1, -1))
        K = sp.bmat([[J, col], [row, None]], format="csc")
        d = spsolve(K, -np.concatenate([R, [C]]))
        phi = phi + d[:M]
        om2 = om2 + float(d[M])
        if float(np.max(np.abs(d[:M]))) < 1e-13 and abs(float(d[M])) < 1e-15 and float(np.max(np.abs(R))) < 1e-11:
            break
    R, C = rest(phi, om2)
    return phi, om2, dict(newton_iter=it + 1, newton_rest=float(np.max(np.abs(R))), norm_rest=float(C),
                          phi0=float(phi[0]), M_halb=M, D_kont=D, om2_kont=1.0 - k2, N_ziel=N_ziel)


def b_moden(S, h, cB, anzahl=3):
    """Unterste Eigenmoden von -c_B^2 Lap_h + (m_B^2 - g S) mit Geisterplaetzen 0 (wie die Dynamik)."""
    c2 = cB * cB
    h2 = 1.0 / (h * h)
    d = 2.0 * c2 * h2 + M_B * M_B - G_K * S
    e = np.full(len(S) - 1, -c2 * h2)
    w, v = eigh_tridiagonal(d, e, select="i", select_range=(0, anzahl - 1))
    return w, v


def fahrplan(T_r, T_p):
    """Abschnitte (typ, t0, t1, k) und Gesamtdauer."""
    segs = [("ruhe", 0.0, T_p, 0)]
    t = T_p
    for k in range(1, 4):
        segs.append(("rampe", t, t + T_r, k)); t += T_r
        segs.append(("plateau", t, t + T_p, k)); t += T_p
    return segs, t


def main():
    a = sys.argv
    name = a[1]; cB = float(a[2]); h = float(a[3]); dt = float(a[4]); T_r = float(a[5]); T_p = float(a[6])
    bamp = float(a[7])
    t_stop_arg = a[8] if len(a) > 8 else "-"
    wand = float(a[9]) if len(a) > 9 else 500.0
    t_wand0 = time.time()
    nsub = int(round(DS_MESS / dt))
    assert abs(nsub * dt - DS_MESS) < 1e-12, "DS_MESS kein Vielfaches von dt"
    nsnap = int(round(DS_SNAP / DS_MESS))
    N = int(round(L_W / h))
    h2inv = 1.0 / (h * h)
    c2 = cB * cB
    m2 = M_B * M_B
    halbg = 0.5 * G_K

    # Startzustand (immer neu berechnet; deterministisch)
    phi, om2, newton = beutel(h)
    om = math.sqrt(om2)
    Mh = len(phi)
    i_c = N // 2
    assert i_c - Mh >= 0 and i_c + Mh < N, "Fenster zu kurz fuer den Startbeutel"
    psi_start = np.zeros(N, complex)
    psi_start[i_c:i_c + Mh] = phi
    psi_start[i_c - Mh + 1:i_c + 1] = phi[::-1]
    p_start = 1j * om * psi_start
    S_init = np.abs(psi_start) ** 2
    lam, vec = b_moden(S_init, h, cB, 3)
    f = vec[:, 0].copy()
    f = f / f[int(np.argmax(np.abs(f)))]
    B_start = bamp * f
    q_start = np.zeros(N)

    def H_teile(psi, p, Bv, qv, th):
        Sx = psi.real ** 2 + psi.imag ** 2
        em = complex(math.cos(th), -math.sin(th))
        HA = float(h * np.sum(p.real ** 2 + p.imag ** 2 + U(Sx)) + np.sum(np.abs(em * psi[1:] - psi[:-1]) ** 2) / h
                   + (Sx[0] + Sx[-1]) / h)
        HB = float(h * np.sum(0.5 * qv * qv + 0.5 * (m2 - G_K * Sx) * Bv * Bv)
                   + 0.5 * c2 / h * (np.sum((Bv[1:] - Bv[:-1]) ** 2) + Bv[0] ** 2 + Bv[-1] ** 2))
        return HA, HB

    HA0, HB0 = H_teile(psi_start, p_start, B_start, q_start, 0.0)
    M0 = HA0 + HB0
    Q0 = float(2.0 * h * np.sum(np.imag(np.conj(psi_start) * p_start)))
    segs, t_gesamt = fahrplan(T_r, T_p)
    gv = [0.0] + [v / math.sqrt(1.0 - v * v) for v in V_ZIEL]
    E_k = [2.0 * M0 * (gv[k] - gv[k - 1]) / (Q0 * T_r) for k in range(1, 4)]
    a_k = [0.0]
    for k in range(3):
        a_k.append(a_k[-1] + E_k[k] * T_r / 2.0)
    t_rampe = [None] + [s[1] for s in segs if s[0] == "rampe"]

    def E_von_t(t):
        for k in range(1, 4):
            t0 = t_rampe[k]
            if t0 <= t < t0 + T_r:
                return E_k[k - 1] * math.sin(math.pi * (t - t0) / T_r) ** 2
        return 0.0

    def a_von_t(t):
        if t < t_rampe[1]:
            return 0.0
        for k in range(1, 4):
            t0 = t_rampe[k]
            if t < t0 + T_r:
                s = t - t0
                return a_k[k - 1] + E_k[k - 1] * (0.5 * s - T_r / (4.0 * math.pi) * math.sin(2.0 * math.pi * s / T_r))
            if k == 3 or t < t_rampe[k + 1]:
                return a_k[k]
        return a_k[3]

    def theta(t):
        return h * a_von_t(t)

    t_end = t_gesamt if t_stop_arg == "-" else min(t_gesamt, float(t_stop_arg))
    k_ziel = int(math.ceil(t_end / DS_MESS - 1e-9))
    # Segmentende (fuer Profile): Zeitpunkte, an denen Ruhe/Plateaus enden
    t_profil = [s[2] for s in segs if s[0] in ("ruhe", "plateau")]
    k_profil = [int(round(tp / DS_MESS)) for tp in t_profil]

    # Schwamm
    xi = np.arange(N) * h
    nabs = int(round(L_ABS / h))
    eta_l = ETA_MAX * np.clip(1.0 - xi[:nabs] / L_ABS, 0, None) ** 2
    eta_r = eta_l[::-1].copy()
    fh_l = np.exp(-eta_l * dt / 2); fh_r = np.exp(-eta_r * dt / 2)
    fv_l = fh_l * fh_l; fv_r = fh_r * fh_r
    sl_l = slice(0, nabs); sl_r = slice(N - nabs, N)
    i_soll = float(i_c)
    s_ver = int(round(VERSCHUB / h))

    ckpt = name + ".ckpt.npz"
    Psi = np.zeros(N + 2, complex)
    psi = Psi[1:-1]
    BB = np.zeros(N + 2)
    Bv = BB[1:-1]
    profile = {}
    if os.path.exists(ckpt):
        z = np.load(ckpt)
        psi[:] = z["psi"]; p = z["p"].copy(); Bv[:] = z["B"]; q = z["q"].copy()
        k_mess = int(z["k_mess"]); n0 = int(z["n0_jetzt"])
        acc = z["acc"].copy()
        reihen = {fn: list(z[fn]) for fn in FELDER}
        snaps_S = list(z["snaps_S"]); snaps_B = list(z["snaps_B"]); snap_t = list(z["snap_t"]); snap_n0 = list(z["snap_n0"])
        for kk in z.files:
            if kk.startswith("prof_"):
                profile[kk] = z[kk]
        abschnitte = int(z["abschnitte"]) + 1
        print("fortgesetzt bei t = %.3f" % (k_mess * DS_MESS), flush=True)
    else:
        psi[:] = psi_start; p = p_start.copy(); Bv[:] = B_start; q = q_start.copy(); k_mess = 0; n0 = 0
        acc = np.zeros(6)   # W, EabsA+B, Qabs, Edrop, Qdrop, EabsB
        reihen = {fn: [] for fn in FELDER}
        snaps_S = []; snaps_B = []; snap_t = []; snap_n0 = []
        abschnitte = 1
    S = np.empty(N); T = np.empty(N); T2 = np.empty(N); R1 = np.empty(N); R2 = np.empty(N)
    Ac = np.empty(N, complex); Bc_ = np.empty(N, complex)

    def kick(coef, th):
        np.multiply(psi.real, psi.real, out=S)
        np.multiply(psi.imag, psi.imag, out=T)
        S.__iadd__(T)
        # A: p += coef [ (e^{-i th} A_{n+1} + e^{i th} A_{n-1})/h^2 - (U'(S) + 2/h^2 - (g/2) B^2) A ]
        np.multiply(Bv, Bv, out=T); T.__imul__(halbg)
        np.multiply(S, 1.5, out=T2); T2.__isub__(2.0); T2.__imul__(S); T2.__iadd__(1.0 + 2.0 * h2inv); T2.__isub__(T)
        T2.__imul__(coef)
        em = complex(math.cos(th), -math.sin(th))
        np.multiply(Psi[2:], em * (coef * h2inv), out=Ac)
        np.multiply(Psi[:-2], em.conjugate() * (coef * h2inv), out=Bc_)
        Ac.__iadd__(Bc_)
        np.multiply(psi, T2, out=Bc_)
        Ac.__isub__(Bc_)
        p.__iadd__(Ac)
        # B: q += coef [ c^2 (B_{n+1} + B_{n-1})/h^2 - (2 c^2/h^2 + m^2 - g S) B ]
        np.add(BB[2:], BB[:-2], out=R1); R1.__imul__(coef * c2 * h2inv)
        np.multiply(S, -G_K, out=R2); R2.__iadd__(2.0 * c2 * h2inv + m2); R2.__imul__(Bv); R2.__imul__(coef)
        R1.__isub__(R2)
        q.__iadd__(R1)

    def strom(th):
        z = np.vdot(psi[:-1], psi[1:])
        return -2.0 * (complex(math.cos(th), -math.sin(th)) * z).imag

    def daempfen(fl, fr):
        for sl, fa in ((sl_l, fl), (sl_r, fr)):
            ps = p[sl]; qs = psi[sl]; bs = q[sl]
            eb = np.vdot(ps, ps).real; qb = np.vdot(qs, ps).imag; ebb = float(np.dot(bs, bs))
            ps *= fa; bs *= fa
            ea = np.vdot(ps, ps).real; qa = np.vdot(qs, ps).imag; eab = float(np.dot(bs, bs))
            acc[1] += h * (eb - ea) + 0.5 * h * (ebb - eab); acc[2] += 2.0 * h * (qb - qa); acc[5] += 0.5 * h * (ebb - eab)

    def drift(c):
        np.multiply(p, c * dt, out=Ac); psi.__iadd__(Ac)
        np.multiply(q, c * dt, out=R1); Bv.__iadd__(R1)

    def schritt(k):
        t0 = k * dt
        w = 0.0
        drift(CS[0])
        tt = t0 + CC[0] * dt; th = theta(tt); w += DS[0] * E_von_t(tt) * strom(th); kick(DS[0] * dt, th)
        drift(CS[1])
        tt = t0 + CC[1] * dt; th = theta(tt); w += DS[1] * E_von_t(tt) * strom(th); kick(DS[1] * dt, th)
        drift(CS[2])
        tt = t0 + CC[2] * dt; th = theta(tt); w += DS[2] * E_von_t(tt) * strom(th); kick(DS[2] * dt, th)
        drift(CS[3])
        acc[0] += dt * w

    def halbwert(y, xg):
        im = int(np.argmax(y)); ym = float(y[im]); lev = 0.5 * ym
        lw = np.nonzero(y[:im] < lev)[0]
        rw = np.nonzero(y[im:] < lev)[0]
        if len(lw) == 0 or len(rw) == 0 or not ym > 0:
            return float("nan"), float("nan"), False, ym
        jl = int(lw[-1])
        xl = xg[jl] + h * (lev - y[jl]) / (y[jl + 1] - y[jl])
        jr = im + int(rw[0])
        xr = xg[jr - 1] + h * (y[jr - 1] - lev) / (y[jr - 1] - y[jr])
        return float(xl), float(xr), True, ym

    def messen(t):
        th = theta(t)
        aa = a_von_t(t)
        xg = (n0 + np.arange(N)) * h
        Sx = psi.real ** 2 + psi.imag ** 2
        rho = 2.0 * (psi.real * p.imag - psi.imag * p.real)
        xlS, xrS, okS, Sm = halbwert(Sx, xg)
        xlR, xrR, okR, Rm = halbwert(rho, xg)
        ok = okS and okR
        HA, HB = H_teile(psi, p, Bv, q, th)
        r = dict(t=t, Q=float(h * rho.sum()), Qabs=float(acc[2]), Qdrop=float(acc[4]), H=HA + HB, HB=HB,
                 Eabs=float(acc[1]), Edrop=float(acc[3]), W=float(acc[0]), Smax=Sm, Rmax=Rm, a=aa, n0=float(n0))
        if not ok:
            r.update(X=float("nan"), LS=float("nan"), LR=float("nan"), XR=float("nan"), thc=float("nan"),
                     sB=float("nan"), Bc=float("nan"))
            return r, False
        X = 0.5 * (xlS + xrS)
        j = int(math.floor((X - xg[0]) / h)); u = (X - xg[j]) / h
        ch0 = psi[j] * complex(math.cos(aa * xg[j]), -math.sin(aa * xg[j]))
        ch1 = psi[j + 1] * complex(math.cos(aa * xg[j + 1]), -math.sin(aa * xg[j + 1]))
        thc = math.atan2(((1.0 - u) * ch0 + u * ch1).imag, ((1.0 - u) * ch0 + u * ch1).real)
        i0 = max(0, int(math.floor((X - R_B - xg[0]) / h))); i1 = min(N - 1, int(math.ceil((X + R_B - xg[0]) / h)))
        xi_ = xg[i0:i1 + 1] - X
        wg = np.where(np.abs(xi_) < R_B, np.cos((0.5 * math.pi / R_B) * xi_) ** 2, 0.0)
        sB = float(np.sum(Bv[i0:i1 + 1] * wg) / np.sum(wg))
        Bcen = float((1.0 - u) * Bv[j] + u * Bv[j + 1])
        r.update(X=X, LS=xrS - xlS, LR=xrR - xlR, XR=0.5 * (xlR + xrR), thc=thc, sB=sB, Bc=Bcen)
        return r, True

    def verschieben(s, t):
        nonlocal n0
        th = theta(t)
        HA, HB = H_teile(psi, p, Bv, q, th); Hb = HA + HB
        Qb = float(2.0 * h * np.vdot(psi, p).imag)
        for arr in (psi, p, Bv, q):
            if s > 0:
                arr[:-s] = arr[s:].copy(); arr[-s:] = 0.0
            else:
                m = -s
                arr[m:] = arr[:-m].copy(); arr[:m] = 0.0
        n0 += s
        HA, HB = H_teile(psi, p, Bv, q, th)
        acc[3] += Hb - (HA + HB); acc[4] += Qb - float(2.0 * h * np.vdot(psi, p).imag)

    def profil_speichern(kidx):
        nr = k_profil.index(kidx)
        Sx = psi.real ** 2 + psi.imag ** 2
        rho = 2.0 * (psi.real * p.imag - psi.imag * p.real)
        profile["prof_S_%d" % nr] = Sx.copy(); profile["prof_rho_%d" % nr] = rho.copy()
        profile["prof_B_%d" % nr] = Bv.copy(); profile["prof_n0_%d" % nr] = np.array(n0)

    if k_mess == 0 and len(reihen["t"]) == 0:
        r, ok = messen(0.0)
        for fn in FELDER:
            reihen[fn].append(r[fn])
        snaps_S.append((np.abs(psi) ** 2).astype(np.float32)); snaps_B.append(Bv.astype(np.float32))
        snap_t.append(0.0); snap_n0.append(n0)
    status = "fertig"
    while k_mess < k_ziel:
        k0 = k_mess * nsub
        for jj in range(nsub):
            daempfen(fh_l if jj == 0 else fv_l, fh_r if jj == 0 else fv_r)
            schritt(k0 + jj)
        daempfen(fh_l, fh_r)
        k_mess += 1
        t = k_mess * DS_MESS
        r, ok = messen(t)
        for fn in FELDER:
            reihen[fn].append(r[fn])
        if k_mess in k_profil:
            profil_speichern(k_mess)
        if k_mess % nsnap == 0:
            snaps_S.append((np.abs(psi) ** 2).astype(np.float32)); snaps_B.append(Bv.astype(np.float32))
            snap_t.append(t); snap_n0.append(n0)
        if not (np.all(np.isfinite(p)) and np.all(np.isfinite(q))):
            status = "nan"; break
        if not ok:
            status = "verloren"; break
        il = r["X"] / h - n0
        if il > i_soll + s_ver:
            verschieben(s_ver, t)
        elif il < i_soll - s_ver:
            verschieben(-s_ver, t)
        if time.time() - t_wand0 > wand and k_mess < k_ziel:
            np.savez(ckpt, psi=psi.copy(), p=p, B=Bv.copy(), q=q, k_mess=k_mess, n0_jetzt=n0, acc=acc,
                     abschnitte=abschnitte, snaps_S=np.array(snaps_S), snaps_B=np.array(snaps_B),
                     snap_t=np.array(snap_t), snap_n0=np.array(snap_n0), **profile,
                     **{fn: np.array(reihen[fn], float) for fn in FELDER})
            status = "unterbrochen"
            break
    kopf = dict(name=os.path.basename(name), c_B=cB, h=h, dt=dt, T_r=T_r, T_p=T_p, b=bamp, t_stop=t_stop_arg,
                t_gesamt=t_gesamt, t_end=t_end, m_B=M_B, g=G_K, L_ziel=L_ZIEL, v_ziel=list(V_ZIEL), om2=om2, omega=om,
                M0=M0, HA0=HA0, HB0=HB0, Q0=Q0, E_k=E_k, a_k=a_k, segmente=[list(s) for s in segs],
                lambda_B=[float(x) for x in lam], Omega_B0=float(math.sqrt(lam[0])), N=N, i_c=i_c, L_w=L_W,
                L_abs=L_ABS, eta_max=ETA_MAX, verschub=VERSCHUB, R_B=R_B, ds_mess=DS_MESS, ds_snap=DS_SNAP,
                status=status, t_letzt=k_mess * DS_MESS, abschnitte=abschnitte, wandzeit_s=time.time() - t_wand0,
                numpy=np.__version__, newton=newton,
                skript_sha256=hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
                ende_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    if status != "unterbrochen":
        np.savez_compressed(name + ".npz", snaps_S=np.array(snaps_S), snaps_B=np.array(snaps_B),
                            snap_t=np.array(snap_t), snap_n0=np.array(snap_n0), S_init=S_init, B_init=B_start,
                            **profile, **{fn: np.array(reihen[fn], float) for fn in FELDER})
        if os.path.exists(ckpt):
            os.replace(ckpt, name + ".ckpt-verbraucht.npz")
    json.dump(kopf, open(name + ".json", "w"), indent=1)
    Hs = np.array(reihen["H"]); Qd = np.array(reihen["Q"])
    bil = Hs + np.array(reihen["Eabs"]) + np.array(reihen["Edrop"]) - Hs[0] - np.array(reihen["W"])
    qb = Qd + np.array(reihen["Qabs"]) + np.array(reihen["Qdrop"]) - Qd[0]
    print(json.dumps(dict(status=status, t=k_mess * DS_MESS, M0=M0, Q0=Q0, om2_minus_halb=om2 - 0.5,
                          Omega_B0=float(math.sqrt(lam[0])), lambda_B=[float(x) for x in lam], E_k=E_k,
                          X_end=float(reihen["X"][-1]), LS_end=float(reihen["LS"][-1]),
                          bilanz_E_max=float(np.max(np.abs(bil)) / M0), bilanz_Q_max=float(np.max(np.abs(qb)) / Q0),
                          newton=newton, wand_s=round(time.time() - t_wand0, 1))), flush=True)


if __name__ == "__main__":
    main()
