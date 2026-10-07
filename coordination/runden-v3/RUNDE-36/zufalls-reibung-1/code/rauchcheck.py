# ZUFALLS-REIBUNG-1: Kurzauskunft ueber Rauchlaeufe (nur Rauch, keine Urteile).
# Aufruf (ueber kleintest.sh): rauchcheck.py <ordner> <name> [<name> ...]
import sys, os, json, math
import numpy as np

TAU = 10.0


def schnelle(t, X, tau=TAU):
    ds = float(t[1] - t[0]); m = int(round(tau / ds))
    j = np.arange(-m, m + 1, dtype=float); w = j / (ds * np.sum(j * j))
    v = np.full(len(X), np.nan)
    if len(X) > 2 * m:
        v[m:len(X) - m] = np.correlate(X, w, mode="valid")
    return v


ordner = sys.argv[1]
for name in sys.argv[2:]:
    k = json.load(open(os.path.join(ordner, name + ".json")))
    z = np.load(os.path.join(ordner, name + ".npz"))
    t = z["t"]; X = z["X"]; Qw = z["Qwin"]; Ew = z["Ewin"]; Vw = z["Vwin"]; Pw = z["Pwin"]
    v = schnelle(t, X)
    print("==", name, "status", k["status"], "t_letzt", k["t_letzt"], "wand", round(k["wandzeit_s"], 1),
          "min(1+s eta)", k["min_1_plus_sigma_eta"])
    print("  E_start %.8f gM %.8f  P_start %.8f gMv %.8f  Q_start %.10f Q_ruhe %.10f" % (
        k["E_start"], k["Kontinuum_EP"][0], k["P_start"], k["Kontinuum_EP"][1], k["Q_start"], k["Q_ruhe"]))
    for tt in (20, 50, 100, 150, 200, 250, 300, 400, 600, 800, 1000, 1500, 2000, 2500, 3000):
        i = int(round(tt / 0.5))
        if i < len(t) and np.isfinite(v[i]):
            print("  t=%6.0f X=%11.5f v=%.9f Qw=%.12f Ew=%.9f Vw=%+.3e Pw=%.9f amax=%.7f" % (
                t[i], X[i], v[i], Qw[i], Ew[i], Vw[i], Pw[i], z["amax"][i]))
    ia = int(round(k["T_A"] / 0.5))
    ok = np.isfinite(v); ok[:ia] = False
    if ok.any():
        va = v[ia]
        print("  ab T_A: max|v-v(T_A)|/v(T_A) = %.3e ; max|Qw-Qw(T_A)|/Q = %.3e ; Qw(T_A)-min Qw = %.3e" % (
            np.max(np.abs(v[ok] - va)) / abs(va), np.max(np.abs(Qw[ia:] - Qw[ia])) / k["Q_ruhe"],
            (Qw[ia] - np.min(Qw[ia:])) / k["Q_ruhe"]))
        tt = t[ia:]; y = Qw[ia:]
        if len(tt) > 10:
            sl = np.polyfit(tt, y, 1)[0]
            print("  Steigung Qw ab T_A: %.3e /Q je Zeit" % (sl / k["Q_ruhe"]))
            gv = 1.0 / np.sqrt(1.0 - v[ok] ** 2)
            y2 = np.log(gv * np.abs(v[ok]))
            print("  Steigung ln(gamma v) ab T_A: %.3e je Zeit" % np.polyfit(t[ok], y2, 1)[0])
    Hs = z["H"]; bil = Hs + z["Eabs"] + z["Edrop"] - Hs[0] - z["W"]
    qb = z["Qdom"] + z["Qabs"] + z["Qdrop"] - z["Qdom"][0]
    print("  Bilanz E max %.3e (rel M), Q max %.3e ; W_end %.4e Eabs %.3e Qabs %.3e" % (
        np.max(np.abs(bil)) / k["M_ruhe"], np.max(np.abs(qb)) / k["Q_ruhe"], z["W"][-1], z["Eabs"][-1], z["Qabs"][-1]))
    fam = k["familie"]
    print("  Familie (om2, Q, M):", [(f["om2"], round(f["Q"], 6), round(f["M"], 6), "%.1e" % f["newton_rest"]) for f in fam])
