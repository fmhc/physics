# QBALL-GITTER-1 (Runde 35): Q-Ball von M1 auf einem 1D-Gitter unter gleichmaessigem Feld E, zeitliche Eichung.
#   L = h sum |psi_n'|^2 - h sum U(|psi_n|^2) - (1/h) sum |exp(-i th) psi_{n+1} - psi_n|^2,  th(t) = h a(t), a = E t,
#   U(S) = S - S^2 + S^3/2.  Bewegung (p = psi'):
#   p_n' = (e^{-i th} psi_{n+1} + e^{i th} psi_{n-1} - 2 psi_n)/h^2 - U'(|psi_n|^2) psi_n - eta_n p_n.
#   Rand: Geisterplaetze psi = 0 an beiden Fensterenden; Schwamm eta_n (quadratische Rampe) an beiden Enden.
#   Ladung Q = 2 h sum Im(conj(psi_n) p_n)  (psi ~ e^{+i omega t} hat Q > 0); Strom J = -2 sum Im(conj(psi_n) e^{-i th}
#   psi_{n+1}); dH/dt = E J (ohne Schwamm). Kinetischer Impuls P = -2 h sum Re(conj(p_n) (e^{-i th} psi_{n+1} -
#   e^{i th} psi_{n-1})/(2h)); Kontinuum: dP/dt = Q E.
# Integrator: Yoshida 4. Ordnung, Drift schiebt psi und t, Stoss mit th zur aktuellen Zeit (erweiterter Phasenraum);
#   Arbeit W = sum_Stoesse d_i dt E J_i (schema-treu). Schwamm exakt als p -> p exp(-eta dt/2) vor/nach jedem Schritt,
#   Energie- und Ladungsabfluss exakt gebucht.
# Mitlaufendes Fenster: Ist der Ladungsschwerpunkt mehr als VERSCHUB vom Sollort (Anteil FB der Fensterlaenge) entfernt,
#   wird um ganze Plaetze verschoben (exakte Gittertranslation); was hinten/vorn herausfaellt, wird gebucht.
# Start: stationaere Gitterloesung bei omega^2 = 0,7 (Newton auf der halben Kette mit Spiegelrand, platzzentriert).
# Aufruf (nur ueber kleintest.sh):
#   qgitter.py <name> <h> <a0> <t_end> <dt> <L_w> [wand_s]
#     a0 = Q0 E / M0 (E wird aus der Gitterloesung bestimmt); t_end als Zahl oder "<f>TB" (f mal Bloch-Periode) oder
#     "TB+<z>" (Bloch-Periode plus z).
#   Ausgabe <name>.npz (Zeitreihen, Momentaufnahmen) und <name>.json (Kopf); Checkpoint <name>.ckpt.npz bei
#   Wandzeit-Abbruch; ein erneuter Aufruf mit denselben Argumenten setzt fort.
import sys, os, json, time, hashlib, math
import numpy as np
from scipy.linalg import solve_banded

OMEGA2 = 0.7
W1 = 1.0 / (2.0 - 2.0 ** (1.0 / 3.0))
W0 = -(2.0 ** (1.0 / 3.0)) * W1
CS = (W1 / 2, (W0 + W1) / 2, (W0 + W1) / 2, W1 / 2)
DS = (W1, W0, W1)
CC = (CS[0], CS[0] + CS[1], CS[0] + CS[1] + CS[2])   # Zeitpunkte der Stoesse im Schritt (Anteil von dt)
DS_MESS = 0.5        # Messabstand
DS_SNAP = 25.0       # Abstand der Momentaufnahmen
R_WIN = 10.0         # halbe Breite des Ballfensters um X (hart fuer Q_win, E_win; cos^2-Gewicht fuer X, XE)
FB = 0.4             # Sollort des Balls im Fenster (Anteil der Fensterlaenge)
VERSCHUB = 10.0      # Fenster wird um 10 Laengeneinheiten verschoben, wenn X so weit vom Sollort weg ist
L_ABS = 60.0         # Schwammlaenge an jedem Ende
ETA_MAX = 1.0        # Schwammstaerke am Ende
L_HALB_NEWTON = 60.0 # halbe Laenge der Newton-Kette
Q_ZERFALL = 0.05     # Abbruch, wenn Q_win < Q_ZERFALL Q0
FELDER = ["t", "X", "XE", "Qdom", "Qwin", "Qabs", "Qdrop", "H", "Ewin", "Eabs", "Edrop", "W", "J", "P", "breite",
          "amax", "n0"]


def U(S):
    return S * (1.0 - S + 0.5 * S * S)


def Up(S):
    return 1.0 - 2.0 * S + 1.5 * S * S


def Upp(S):
    return -2.0 + 3.0 * S


def gitter_ball(h, om2):
    """Stationaere Gitterloesung phi_n (reell), platzzentriert; Newton auf n = 0..M-1 mit phi_{-1} = phi_1, phi_M = 0."""
    M = int(round(L_HALB_NEWTON / h))
    x = np.arange(M) * h
    k2 = 1.0 - om2
    k = math.sqrt(k2)
    D = math.sqrt(1.0 - 2.0 * k2)
    phi = np.sqrt(2.0 * k2 / (1.0 + D * np.cosh(np.clip(2.0 * k * x, 0, 700))))
    h2 = 1.0 / (h * h)
    rest = None
    for it in range(60):
        S = phi * phi
        up = np.empty(M + 1); up[:M] = phi; up[M] = 0.0
        lo = np.empty(M); lo[0] = phi[1]; lo[1:] = phi[:-1]
        R = (up[1:M + 1] + lo - 2.0 * phi) * h2 + (om2 - Up(S)) * phi
        rest = float(np.max(np.abs(R)))
        ab = np.zeros((3, M))
        ab[0, 1:] = h2
        ab[0, 1] = 2.0 * h2
        ab[1, :] = -2.0 * h2 + om2 - Up(S) - 2.0 * S * Upp(S)
        ab[2, :-1] = h2
        dphi = solve_banded((1, 1), ab, -R)
        phi = phi + dphi
        if float(np.max(np.abs(dphi))) < 1e-13 and rest < 1e-11:
            break
    S = phi * phi
    up = np.empty(M + 1); up[:M] = phi; up[M] = 0.0
    lo = np.empty(M); lo[0] = phi[1]; lo[1:] = phi[:-1]
    R = (up[1:M + 1] + lo - 2.0 * phi) * h2 + (om2 - Up(S)) * phi
    return phi, dict(newton_iter=it + 1, newton_rest=float(np.max(np.abs(R))), phi0=float(phi[0]), M_halb=M)


def main():
    a = sys.argv
    name = a[1]; h = float(a[2]); a0 = float(a[3]); t_end_s = a[4]; dt = float(a[5]); L_w = float(a[6])
    wand = float(a[7]) if len(a) > 7 else 500.0
    t_wand0 = time.time()
    nsub = int(round(DS_MESS / dt))
    assert abs(nsub * dt - DS_MESS) < 1e-12, "DS_MESS kein Vielfaches von dt"
    nsnap = int(round(DS_SNAP / DS_MESS))
    N = int(round(L_w / h))
    om = math.sqrt(OMEGA2)
    h2inv = 1.0 / (h * h)
    # Startball (immer neu berechnet; deterministisch)
    phi, newton = gitter_ball(h, OMEGA2)
    Mh = len(phi)
    i_c = int(round(FB * L_w / h))
    assert i_c - Mh >= 0 and i_c + Mh < N, "Fenster zu kurz fuer den Startball"
    psi_start = np.zeros(N, complex)
    psi_start[i_c:i_c + Mh] = phi
    psi_start[i_c - Mh + 1:i_c + 1] = phi[::-1]
    p_start = 1j * om * psi_start
    # Ruheenergie und Ladung des Gitterballs (th = 0)
    S0 = np.abs(psi_start) ** 2
    d0 = psi_start[1:] - psi_start[:-1]
    M0 = float(h * np.sum(np.abs(p_start) ** 2 + U(S0)) + np.sum(np.abs(d0) ** 2) / h
               + (abs(psi_start[0]) ** 2 + abs(psi_start[-1]) ** 2) / h)
    Q0 = float(2.0 * h * np.sum(np.imag(np.conj(psi_start) * p_start)))
    E = a0 * M0 / Q0
    TB = 2.0 * math.pi / (h * E) if E > 0 else float("inf")
    if t_end_s.endswith("TB"):
        t_end = float(t_end_s[:-2]) * TB
    elif t_end_s.startswith("TB+"):
        t_end = TB + float(t_end_s[3:])
    else:
        t_end = float(t_end_s)
    k_ziel = int(math.ceil(t_end / DS_MESS - 1e-9))
    # Schwamm
    xi = np.arange(N) * h
    nabs = int(round(L_ABS / h))
    eta_l = ETA_MAX * np.clip(1.0 - xi[:nabs] / L_ABS, 0, None) ** 2
    eta_r = eta_l[::-1].copy()
    fh_l = np.exp(-eta_l * dt / 2); fh_r = np.exp(-eta_r * dt / 2)
    fv_l = fh_l * fh_l; fv_r = fh_r * fh_r
    sl_l = slice(0, nabs); sl_r = slice(N - nabs, N)
    i_soll = FB * L_w / h
    s_ver = int(round(VERSCHUB / h))

    ckpt = name + ".ckpt.npz"
    Psi = np.zeros(N + 2, complex)
    psi = Psi[1:-1]
    if os.path.exists(ckpt):
        z = np.load(ckpt)
        psi[:] = z["psi"]; p = z["p"].copy(); k_mess = int(z["k_mess"]); n0 = int(z["n0_jetzt"])
        Xprev = float(z["Xprev"]); acc = z["acc"].copy()
        reihen = {f: list(z[f]) for f in FELDER}
        snaps = list(z["snaps"]); snap_t = list(z["snap_t"]); snap_n0 = list(z["snap_n0"])
        abschnitte = int(z["abschnitte"]) + 1
        print("fortgesetzt bei t = %.3f" % (k_mess * DS_MESS), flush=True)
    else:
        psi[:] = psi_start; p = p_start.copy(); k_mess = 0; n0 = 0
        Xprev = i_c * h
        acc = np.zeros(5)   # W, Eabs, Qabs, Edrop, Qdrop
        reihen = {f: [] for f in FELDER}
        snaps = []; snap_t = []; snap_n0 = []
        abschnitte = 1
    S = np.empty(N); T = np.empty(N); A = np.empty(N, complex); B = np.empty(N, complex)

    def theta(t):
        return math.fmod(h * E * t, 2.0 * math.pi)

    def kick(coef, th):
        np.multiply(psi.real, psi.real, out=S)
        np.multiply(psi.imag, psi.imag, out=T)
        S.__iadd__(T)
        np.multiply(S, 1.5, out=T); T.__isub__(2.0); T.__imul__(S); T.__iadd__(1.0 + 2.0 * h2inv); T.__imul__(coef)
        em = complex(math.cos(th), -math.sin(th))
        np.multiply(Psi[2:], em * (coef * h2inv), out=A)
        np.multiply(Psi[:-2], em.conjugate() * (coef * h2inv), out=B)
        A.__iadd__(B)
        np.multiply(psi, T, out=B)
        A.__isub__(B)
        p.__iadd__(A)

    def strom(th):
        z = np.vdot(psi[:-1], psi[1:])
        return -2.0 * (complex(math.cos(th), -math.sin(th)) * z).imag

    def daempfen(fl, fr):
        # exakte Buchung: Energie- und Ladungsabfluss durch den Schwamm
        for sl, f in ((sl_l, fl), (sl_r, fr)):
            ps = p[sl]; qs = psi[sl]
            eb = np.vdot(ps, ps).real; qb = np.vdot(qs, ps).imag
            ps *= f
            ea = np.vdot(ps, ps).real; qa = np.vdot(qs, ps).imag
            acc[1] += h * (eb - ea); acc[2] += 2.0 * h * (qb - qa)

    def schritt(k):
        t0 = k * dt
        w = 0.0
        np.multiply(p, CS[0] * dt, out=A); psi.__iadd__(A)
        th = theta(t0 + CC[0] * dt); w += DS[0] * strom(th); kick(DS[0] * dt, th)
        np.multiply(p, CS[1] * dt, out=A); psi.__iadd__(A)
        th = theta(t0 + CC[1] * dt); w += DS[1] * strom(th); kick(DS[1] * dt, th)
        np.multiply(p, CS[2] * dt, out=A); psi.__iadd__(A)
        th = theta(t0 + CC[2] * dt); w += DS[2] * strom(th); kick(DS[2] * dt, th)
        np.multiply(p, CS[3] * dt, out=A); psi.__iadd__(A)
        acc[0] += E * dt * w

    def H_gesamt(th):
        Sx = psi.real ** 2 + psi.imag ** 2
        em = complex(math.cos(th), -math.sin(th))
        l = np.abs(em * psi[1:] - psi[:-1]) ** 2
        return float(h * np.sum(p.real ** 2 + p.imag ** 2 + U(Sx)) + l.sum() / h
                     + (Sx[0] + Sx[-1]) / h)

    def Q_gesamt():
        return float(2.0 * h * np.vdot(psi, p).imag)

    def messen(t, Xprev):
        th = theta(t)
        em = complex(math.cos(th), -math.sin(th))
        rho = 2.0 * h * (psi.real * p.imag - psi.imag * p.real)
        Qdom = float(rho.sum())
        xg = (n0 + np.arange(N)) * h

        def schwerpunkt(dichte, Xs):
            # Schwerpunkt mit glattem Gewicht cos^2(pi xi/(2 R_WIN)), |xi| < R_WIN, bis zur Konvergenz iteriert
            for _ in range(200):
                j0 = max(0, int(math.floor((Xs - R_WIN) / h)) - n0); j1 = min(N - 1, int(math.ceil((Xs + R_WIN) / h)) - n0)
                if j1 < j0:
                    return float("nan"), False
                xi = xg[j0:j1 + 1] - Xs
                wg = np.where(np.abs(xi) < R_WIN, np.cos((0.5 * math.pi / R_WIN) * xi) ** 2, 0.0)
                qq = dichte[j0:j1 + 1] * wg; qs = float(qq.sum())
                if not qs > 0:
                    return float("nan"), False
                dX = float((xi * qq).sum() / qs)
                Xs = Xs + dX
                if abs(dX) < 1e-12 * max(1.0, abs(Xs)):
                    break
            return Xs, True

        X, ok = schwerpunkt(rho, Xprev)
        if ok:
            i0 = max(0, int(math.floor((X - R_WIN) / h)) - n0); i1 = min(N - 1, int(math.ceil((X + R_WIN) / h)) - n0)
            sel = (np.abs(xg[i0:i1 + 1] - X) <= R_WIN)
            q = rho[i0:i1 + 1] * sel
            Qwin = float(q.sum())
        else:
            i0 = i1 = 0; sel = np.zeros(1, bool); q = np.zeros(1); Qwin = 0.0
        Sx = psi.real ** 2 + psi.imag ** 2
        es = h * (p.real ** 2 + p.imag ** 2 + U(Sx))
        lnk = np.abs(em * psi[1:] - psi[:-1]) ** 2 / h
        H = float(es.sum() + lnk.sum() + (Sx[0] + Sx[-1]) / h)
        en = es.copy(); en[:-1] += 0.5 * lnk; en[1:] += 0.5 * lnk
        en[0] += Sx[0] / h; en[-1] += Sx[-1] / h
        if ok:
            ew = en[i0:i1 + 1] * sel
            Ewin = float(ew.sum())
            XE, okE = schwerpunkt(en, X)
            breite = float(math.sqrt(max(0.0, float(((xg[i0:i1 + 1] - X) ** 2 * q).sum()) / Qwin))) if Qwin > 0 else float("nan")
            amax = float(np.sqrt(Sx[i0:i1 + 1].max()))
            Dp = (em * Psi[i0 + 2:i1 + 3] - em.conjugate() * Psi[i0:i1 + 1]) / (2.0 * h)
            P = float(-2.0 * h * np.sum((np.conj(p[i0:i1 + 1]) * Dp).real * sel))
        else:
            Ewin = XE = breite = amax = P = float("nan")
        J = strom(th)
        r = dict(t=t, X=X if ok else float("nan"), XE=XE, Qdom=Qdom, Qwin=Qwin, Qabs=float(acc[2]), Qdrop=float(acc[4]),
                 H=H, Ewin=Ewin, Eabs=float(acc[1]), Edrop=float(acc[3]), W=float(acc[0]), J=J, P=P, breite=breite,
                 amax=amax, n0=float(n0))
        return r, (X if ok else Xprev), ok

    def verschieben(s, t):
        # s > 0: Fenster nach rechts (vorne Nullen), s < 0: nach links
        nonlocal n0
        th = theta(t)
        Hb = H_gesamt(th); Qb = Q_gesamt()
        if s > 0:
            psi[:-s] = psi[s:].copy(); psi[-s:] = 0.0
            p[:-s] = p[s:].copy(); p[-s:] = 0.0
        else:
            m = -s
            psi[m:] = psi[:-m].copy(); psi[:m] = 0.0
            p[m:] = p[:-m].copy(); p[:m] = 0.0
        n0 += s
        acc[3] += Hb - H_gesamt(th); acc[4] += Qb - Q_gesamt()

    if k_mess == 0 and len(reihen["t"]) == 0:
        r, Xprev, ok = messen(0.0, Xprev)
        for f in FELDER:
            reihen[f].append(r[f])
        rho = 2.0 * h * (psi.real * p.imag - psi.imag * p.real)
        snaps.append((rho / h).astype(np.float32)); snap_t.append(0.0); snap_n0.append(n0)
    status = "fertig"
    while k_mess < k_ziel:
        k0 = k_mess * nsub
        for j in range(nsub):
            daempfen(fh_l if j == 0 else fv_l, fh_r if j == 0 else fv_r)
            schritt(k0 + j)
        daempfen(fh_l, fh_r)
        k_mess += 1
        t = k_mess * DS_MESS
        r, Xprev, ok = messen(t, Xprev)
        for f in FELDER:
            reihen[f].append(r[f])
        if k_mess % nsnap == 0:
            rho = 2.0 * h * (psi.real * p.imag - psi.imag * p.real)
            snaps.append((rho / h).astype(np.float32)); snap_t.append(t); snap_n0.append(n0)
        if not np.all(np.isfinite(p)):
            status = "nan"; break
        if not ok or r["Qwin"] < Q_ZERFALL * Q0:
            status = "zerfallen"; break
        il = Xprev / h - n0
        if il > i_soll + s_ver:
            verschieben(s_ver, t)
        elif il < i_soll - s_ver:
            verschieben(-s_ver, t)
        if time.time() - t_wand0 > wand and k_mess < k_ziel:
            np.savez(ckpt, psi=psi.copy(), p=p, k_mess=k_mess, n0_jetzt=n0, Xprev=Xprev, acc=acc, abschnitte=abschnitte,
                     snaps=np.array(snaps), snap_t=np.array(snap_t), snap_n0=np.array(snap_n0),
                     **{f: np.array(reihen[f], float) for f in FELDER})
            status = "unterbrochen"
            break
    kopf = dict(name=os.path.basename(name), h=h, a0=a0, E=E, M0=M0, Q0=Q0, omega2=OMEGA2, TB=TB, t_end=t_end,
                t_end_arg=t_end_s, dt=dt, L_w=L_w, N=N, i_c=i_c, FB=FB, R_win=R_WIN, L_abs=L_ABS, eta_max=ETA_MAX,
                verschub=VERSCHUB, ds_mess=DS_MESS, ds_snap=DS_SNAP, q_zerfall=Q_ZERFALL, status=status,
                t_letzt=k_mess * DS_MESS, abschnitte=abschnitte, wandzeit_s=time.time() - t_wand0,
                numpy=np.__version__, newton=newton,
                skript_sha256=hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
                ende_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    if status != "unterbrochen":
        np.savez_compressed(name + ".npz", snaps=np.array(snaps), snap_t=np.array(snap_t), snap_n0=np.array(snap_n0),
                            **{f: np.array(reihen[f], float) for f in FELDER})
        if os.path.exists(ckpt):
            os.replace(ckpt, name + ".ckpt-verbraucht.npz")
    json.dump(kopf, open(name + ".json", "w"), indent=1)
    Hs = np.array(reihen["H"]); Qd = np.array(reihen["Qdom"]); X = np.array(reihen["X"])
    bil = Hs + np.array(reihen["Eabs"]) + np.array(reihen["Edrop"]) - Hs[0] - np.array(reihen["W"])
    qb = Qd + np.array(reihen["Qabs"]) + np.array(reihen["Qdrop"]) - Qd[0]
    print(json.dumps(dict(status=status, t=k_mess * DS_MESS, M0=M0, Q0=Q0, E=E, TB=TB, X_end=float(X[-1]),
                          Qwin_end=float(reihen["Qwin"][-1]), bilanz_E_max=float(np.max(np.abs(bil)) / M0),
                          bilanz_Q_max=float(np.max(np.abs(qb)) / Q0), newton=newton,
                          wand_s=round(time.time() - t_wand0, 1))), flush=True)


if __name__ == "__main__":
    main()
