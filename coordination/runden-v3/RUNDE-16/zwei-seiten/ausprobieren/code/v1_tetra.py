#!/usr/bin/env python3
"""V1 Federtetraeder (Runde 16, ausprobieren).
Spektrum der Hesse-Matrix von E = k/2 sum (L - L0)^2 am regulaeren Tetraeder,
analytisch und per finiter Differenzen; dazu nichtlineare Zeitentwicklung
(Velocity-Verlet, vier Schrittweiten) mit Energiefehler und FFT-Spitzen.
Aufruf: python v1_tetra.py <ausgabeordner> [schnell]
"""
import json, os, sys, time
import numpy as np

OUT = sys.argv[1] if len(sys.argv) > 1 else "aus"
SCHNELL = len(sys.argv) > 2 and sys.argv[2] == "schnell"
os.makedirs(OUT, exist_ok=True)
T0 = time.time()

X0 = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float)
X0 /= np.linalg.norm(X0[0] - X0[1])          # Kantenlaenge 1
EDGES = np.array([(i, j) for i in range(4) for j in range(i + 1, 4)])
k, m, L0 = 1.0, 1.0, 1.0


def lengths(x):
    d = x[EDGES[:, 0]] - x[EDGES[:, 1]]
    return d, np.linalg.norm(d, axis=1)


def energy_pot(x):
    _, L = lengths(x)
    return 0.5 * k * np.sum((L - L0) ** 2)


def grad(xf):
    x = xf.reshape(4, 3)
    d, L = lengths(x)
    f = (k * (L - L0) / L)[:, None] * d
    g = np.zeros((4, 3))
    np.add.at(g, EDGES[:, 0], f)
    np.add.at(g, EDGES[:, 1], -f)
    return g.ravel()


def hess_analytic(xf):
    x = xf.reshape(4, 3)
    H = np.zeros((12, 12))
    for (i, j) in EDGES:
        d = x[i] - x[j]
        L = np.linalg.norm(d)
        u = d / L
        T = k * (L - L0)
        B = k * np.outer(u, u) + (T / L) * (np.eye(3) - np.outer(u, u))
        for a, b, s in ((i, i, 1), (j, j, 1), (i, j, -1), (j, i, -1)):
            H[3 * a:3 * a + 3, 3 * b:3 * b + 3] += s * B
    return H


def hess_fd(xf, h):
    n = xf.size
    H = np.zeros((n, n))
    for a in range(n):
        e = np.zeros(n)
        e[a] = h
        H[:, a] = (grad(xf + e) - grad(xf - e)) / (2 * h)
    return 0.5 * (H + H.T)


soll = np.array([0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 4], float) * k / m
res = {"versuch": "V1", "soll": soll.tolist()}
x0 = X0.ravel()
res["gradient_im_gleichgewicht"] = float(np.max(np.abs(grad(x0))))
mu_a = np.sort(np.linalg.eigvalsh(hess_analytic(x0)) / m)
res["eig_analytisch"] = mu_a.tolist()
res["abw_analytisch"] = float(np.max(np.abs(mu_a - soll)))
for h in (1e-4, 1e-5):
    mu = np.sort(np.linalg.eigvalsh(hess_fd(x0, h)) / m)
    res[f"eig_fd_h{h:g}"] = mu.tolist()
    res[f"abw_fd_h{h:g}"] = float(np.max(np.abs(mu - soll)))

# Eigenvektoren benennen: Projektion auf Translation und Rotation
w, V = np.linalg.eigh(hess_analytic(x0))
trans = np.zeros((12, 3))
rot = np.zeros((12, 3))
for a in range(4):
    trans[3 * a:3 * a + 3, :] = np.eye(3)
    for c in range(3):
        e = np.zeros(3)
        e[c] = 1
        rot[3 * a:3 * a + 3, c] = np.cross(e, X0[a])
S = np.linalg.qr(np.hstack([trans, rot]))[0]
res["nullraum_anteil_trans_rot"] = [float(np.linalg.norm(S.T @ V[:, n]) ** 2) for n in range(12)]

# Zeitentwicklung (nichtlinear), Velocity-Verlet
rng = np.random.default_rng(0)
dx = 1e-4 * rng.standard_normal(12)
T = 100.0 if SCHNELL else 400.0
zeit = []
for dt in (0.01, 0.005, 0.0025, 0.00125, 0.000625):
    t1 = time.time()
    nst = int(round(T / dt))
    x = x0 + dx
    v = np.zeros(12)
    a = -grad(x) / m
    E0 = energy_pot(x.reshape(4, 3)) + 0.5 * m * v @ v
    emax = 0.0
    keep = (dt == 0.01)
    if keep:
        sig = np.zeros((nst, 6))
    for n in range(nst):
        v += 0.5 * dt * a
        x += dt * v
        a = -grad(x) / m
        v += 0.5 * dt * a
        E = energy_pot(x.reshape(4, 3)) + 0.5 * m * v @ v
        emax = max(emax, abs(E - E0))
        if keep:
            sig[n] = lengths(x.reshape(4, 3))[1] - L0
    zeit.append({"dt": dt, "schritte": nst, "E0": float(E0), "rel_energiefehler_max": float(emax / E0),
                 "sekunden": time.time() - t1})
    if keep:
        sig -= sig.mean(axis=0)
        win = np.hanning(nst)[:, None]
        P = np.sum(np.abs(np.fft.rfft(sig * win, axis=0)) ** 2, axis=1)
        om = 2 * np.pi * np.fft.rfftfreq(nst, dt)
        peaks = []
        thr = 1e-3 * P[1:].max()
        for i in range(2, len(P) - 1):
            if P[i] > P[i - 1] and P[i] >= P[i + 1] and P[i] > thr:
                y0, y1, y2 = np.log(P[i - 1]), np.log(P[i]), np.log(P[i + 1])
                dlt = 0.5 * (y0 - y2) / (y0 - 2 * y1 + y2)
                peaks.append(float(om[i] + dlt * (om[1] - om[0])))
        res["fft_spitzen_rel_hoehe"] = [float(P[int(round(w / (om[1] - om[0])))] / P[1:].max()) for w in peaks]
        res["fft_spitzen_omega"] = sorted(peaks)
        res["fft_aufloesung"] = float(om[1] - om[0])
        res["fft_soll_omega"] = [1.0, float(np.sqrt(2)), 2.0]
        np.savez_compressed(os.path.join(OUT, "v1_fft.npz"), om=om, P=P)
res["zeitentwicklung"] = zeit
res["sekunden_gesamt"] = time.time() - T0
with open(os.path.join(OUT, "v1_tetra.json"), "w") as f:
    json.dump(res, f, indent=1)
print(json.dumps({k_: res[k_] for k_ in ("eig_analytisch", "abw_analytisch", "abw_fd_h0.0001", "abw_fd_h1e-05",
                                         "fft_spitzen_omega", "sekunden_gesamt")}, indent=1))
for z in zeit:
    print("dt", z["dt"], "rel_E_fehler", z["rel_energiefehler_max"])
