#!/usr/bin/env python3
"""BAD-TAKT (Runde 23). Code-Agent im Auftrag der Leitung claude-primary, 02.10.2026.
Karte: RUNDE-23/bad-takt/KARTE.md (mit Nachtrag 22:29:33). Plan: PLAN.md (vor dem ersten echten Lauf eingefroren).

Grundlage: RUNDE-23/schwebungsuhr/code/schwebung1d.py (unveraendert gelassen). Mit gleicher Rechenvorschrift
uebernommen: Modell M1 in 1D, psi_tt = psi_xx - U'(|psi|^2) psi, U(S) = S - S^2 + S^3/2; Leapfrog dt = 0,4 dx;
exakter Startschritt f exp(+i w_d dt), w_d = (2/dt) asin(w dt/2); diskrete Newton-Profile; Daempfungsschicht
SIGMA0 = 1 quadratisch, Breite 60; Ladungsdichte rho = -2 Im(conj(psi) psi_t) mit zentrierter Zeitableitung;
parabolische Lage des Dichtemaximums; lineare Interpolation von psi fuer die Phase.
Neu: drei Baelle, Amplitudenfaktor, Startphasen, Randwahl, Zeitlauf in Abschnitten mit Zwischenstand, Messreihen je
Ball, Badladung, Sonde im Bad, Fensterauswertung und Urteile BT1 bis BT4 nach PLAN.md.

Rand 'refl': Rechengebiet [-L, L], Dirichlet psi = 0 bei x = +-L, keine Daempfung (gemeinsames Bad).
Rand 'abs' : Rechengebiet [-(L + 60), L + 60], Daempfungsschicht fuer |x| > L; Innenbereich [-L, L] wie bei 'refl'.

Aufrufe:
  python badtakt1d.py neu <stand.npz> <rand> <w2_1> <w2_2> <w2_3> <D> <th1> <th2> <th3> <amp> <dx> <L>
  python badtakt1d.py weiter <stand.npz> <T_ziel> <max_sek>
  python badtakt1d.py auswerten <aus.json> <rolle>=<stand.npz> [...]
     Rollen fuer die Urteile: B1 (Bad, Phasen 0,0,0, dx 0,1), B1f (dasselbe, dx 0,05), B2 (Bad, Phasen 0,2/3,4/3, dx 0,1),
     K1 (Kontrolle absorbierend, Phasen 0,0,0, dx 0,1). Andere Rollennamen werden nur tabelliert.
Startphasen th in Einheiten von pi, auch als Bruch (z. B. 2/3).
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
from scipy.linalg import solve_banded  # noqa: E402

SIGMA0 = 1.0           # Daempfungsstaerke der Randschicht (wie Vorlage)
BREITE_ABS = 60.0      # Breite der Daempfungsschicht (wie Vorlage)
MESS = 0.2             # Messabstand in Zeiteinheiten (wie Vorlage)
R_BALL = 8.0           # Ballbereich: |x - p_i| <= R_BALL
SUCH = 3.0             # Suchbereich fuer das Dichtemaximum um die letzte gemessene Lage
BILD_DT = 100.0        # Dichtebild |psi|^2 alle 100 (Abstand 0,5)
ENERGIE_DT = 10.0      # Energie alle 10
FENSTER_START = 100.0  # erstes Fenster beginnt bei t = 100 (Nachtrag der Karte)
N_FENSTER = 8          # Fensterzahl in [FENSTER_START; T]
S_DA = 0.1             # Ball gilt als vorhanden, wenn das Fenstermittel seiner Zentrumsdichte >= 0,1 ist
REIHEN = ("t", "Q_gitter", "Q_box", "p0", "p1", "p2", "S0", "S1", "S2", "ph0", "ph1", "ph2", "Q0", "Q1", "Q2",
          "sonde_re", "sonde_im")
T_START = time.time()


def u(S):
    return S - S * S + 0.5 * S ** 3


def u1(S):
    return 1.0 - 2.0 * S + 1.5 * S * S


def u2(S):
    return -2.0 + 3.0 * S


def kontinuum(w2, x):
    k2 = 1.0 - w2
    k = math.sqrt(k2)
    s = math.sqrt(2.0 * w2 - 1.0)
    z = np.minimum(2.0 * k * np.abs(x), 700.0)
    return np.sqrt(2.0 * k2 / (1.0 + s * np.cosh(z)))


def ladung_kontinuum(w2):
    om = math.sqrt(w2)
    s = math.sqrt(2.0 * w2 - 1.0)
    return 4.0 * math.sqrt(2.0) * om * math.atanh(math.sqrt((1.0 - s) / (1.0 + s)))


def jsonfest(x):
    if isinstance(x, dict):
        return {str(k): jsonfest(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonfest(v) for v in x]
    if isinstance(x, np.ndarray):
        return jsonfest(x.tolist())
    if isinstance(x, (np.floating, np.integer, np.bool_)):
        x = x.item()
    if isinstance(x, complex):
        return [x.real, x.imag]
    if isinstance(x, float) and not math.isfinite(x):
        return str(x)
    return x


def schreiben(out, pfad):
    with open(pfad + ".tmp", "w") as fh:
        json.dump(jsonfest(out), fh, indent=1)
    os.replace(pfad + ".tmp", pfad)


def bruch(s):
    if "/" in s:
        a, b = s.split("/")
        return float(a) / float(b)
    return float(s)


# ================================================================ Profil (wie Vorlage)

def residuum(f, w2, dx):
    M = f.size - 1
    h2 = 1.0 / (dx * dx)
    lap = np.zeros(M + 1)
    lap[1:M] = (f[2:] - 2.0 * f[1:M] + f[:M - 1]) * h2
    lap[0] = 2.0 * (f[1] - f[0]) * h2
    return (lap + (w2 - u1(f * f)) * f)[:M]


def profil_diskret(w2, dx, M, iters=30, tol=1e-12):
    """Newton auf F_j = (f_{j+1} - 2 f_j + f_{j-1})/dx^2 + (w2 - U'(f_j^2)) f_j = 0, j = 0..M-1, f_{-1} = f_1, f_M = 0."""
    f = kontinuum(w2, np.arange(M + 1) * dx)
    f[M] = 0.0
    h2 = 1.0 / (dx * dx)
    verlauf = []
    for _ in range(iters):
        F = residuum(f, w2, dx)
        res = float(np.abs(F).max())
        verlauf.append(res)
        if res < tol:
            break
        Sm = f[:M] * f[:M]
        ab = np.zeros((3, M))
        ab[0, 1:] = h2
        ab[0, 1] = 2.0 * h2
        ab[1, :] = -2.0 * h2 + w2 - u1(Sm) - 2.0 * Sm * u2(Sm)
        ab[2, :-1] = h2
        f[:M] += solve_banded((1, 1), ab, -F)
    verlauf.append(float(np.abs(residuum(f, w2, dx)).max()))
    return f, verlauf


def platzieren(f, c, N):
    d = np.abs(np.arange(N + 1) - c)
    g = np.where(d < f.size, f[np.minimum(d, f.size - 1)], 0.0)
    g[0] = 0.0
    g[N] = 0.0
    return g


# ================================================================ Gitter, Energie

def gitter(rand, dx, L):
    if rand not in ("refl", "abs"):
        raise SystemExit("rand: refl | abs")
    Lw = L if rand == "refl" else L + BREITE_ABS
    N = int(round(2.0 * Lw / dx))
    if N % 2:
        N += 1
    j0 = N // 2
    x = (np.arange(N + 1) - j0) * dx
    Lw = j0 * dx
    if rand == "refl":
        x_sd = Lw
        gam = np.zeros(N + 1)
    else:
        x_sd = Lw - BREITE_ABS
        gam = np.where(np.abs(x) > x_sd, SIGMA0 * ((np.abs(x) - x_sd) / (Lw - x_sd)) ** 2, 0.0)
    jL = int(np.argmax(x >= -x_sd - 1e-9))          # erster Knoten im Innenbereich |x| <= x_sd
    jR = int(N - np.argmax(x[::-1] <= x_sd + 1e-9))  # letzter Knoten im Innenbereich
    return N, j0, x, Lw, x_sd, gam, jL, jR


def energie(psi, vel, dx):
    S = psi.real ** 2 + psi.imag ** 2
    grad = np.abs(np.diff(psi)) ** 2 / (dx * dx)
    return float(dx * ((np.abs(vel) ** 2 + u(S)).sum() + grad.sum()))


# ================================================================ Stand (Zwischenstand) lesen und schreiben

def stand_schreiben(pfad, psi, old, n, pos, meta, alt, neu_r, bilder, bild_t, e_t, e_v, bild_x):
    d = {"psi": psi, "old": old, "n": np.asarray(n, dtype=np.int64), "pos": np.asarray(pos, dtype=np.float64),
         "meta_json": np.asarray(json.dumps(jsonfest(meta)))}
    for k in REIHEN:
        a = alt.get("r_" + k, np.zeros(0))
        d["r_" + k] = np.concatenate([a, np.asarray(neu_r[k], dtype=np.float64)])
    nb = bild_x.size
    a = alt.get("bilder", np.zeros((0, nb), dtype=np.float32))
    d["bilder"] = np.concatenate([a, np.stack(bilder).astype(np.float32)]) if bilder else a
    d["bild_t"] = np.concatenate([alt.get("bild_t", np.zeros(0)), np.asarray(bild_t, dtype=np.float64)])
    d["bild_x"] = bild_x
    d["e_t"] = np.concatenate([alt.get("e_t", np.zeros(0)), np.asarray(e_t, dtype=np.float64)])
    d["e_v"] = np.concatenate([alt.get("e_v", np.zeros(0)), np.asarray(e_v, dtype=np.float64)])
    tmp = pfad[:-4] + ".tmp.npz" if pfad.endswith(".npz") else pfad + ".tmp.npz"
    np.savez(tmp, **d)
    os.replace(tmp, pfad)


def neu(pfad, rand, w2, D, th, amp, dx, L):
    if os.path.exists(pfad):
        raise SystemExit(f"Stand {pfad} existiert schon; nicht ueberschreiben")
    dt = 0.4 * dx
    N, j0, x, Lw, x_sd, gam, jL, jR = gitter(rand, dx, L)
    jD = D / dx
    if abs(jD - round(jD)) > 1e-9:
        raise SystemExit("D/dx muss ganzzahlig sein")
    jD = int(round(jD))
    zentren = [j0 - jD, j0, j0 + jD]
    if zentren[0] - R_BALL / dx < jL or zentren[2] + R_BALL / dx > jR:
        raise SystemExit("Baelle liegen nicht im Innenbereich")
    meta = {"version": "badtakt1d", "rand": rand, "w2": w2, "D": D, "theta_durch_pi": th, "amp": amp, "dx": dx,
            "dt": dt, "L": L, "L_rechen": Lw, "x_sd": x_sd, "N": N, "jL": jL, "jR": jR, "mess": MESS,
            "R_ball": R_BALL, "such": SUCH, "baelle": [], "abschnitte": []}
    psi = np.zeros(N + 1, dtype=np.complex128)
    old = np.zeros(N + 1, dtype=np.complex128)
    vel = np.zeros(N + 1, dtype=np.complex128)
    for i in range(3):
        om = math.sqrt(w2[i])
        om_d = 2.0 / dt * math.asin(0.5 * om * dt)
        f, res = profil_diskret(w2[i], dx, N)
        ph = complex(math.cos(math.pi * th[i]), math.sin(math.pi * th[i]))
        teil = platzieren(f, zentren[i], N) * amp * ph
        psi += teil
        old += teil * complex(math.cos(om_d * dt), math.sin(om_d * dt))
        vel += -1j * om * teil
        q_frei = float(2.0 * om * dx * (np.abs(platzieren(f, zentren[i], N)) ** 2).sum())
        meta["baelle"].append({"w2": w2[i], "omega": om, "omega_diskret": om_d, "x": float(x[zentren[i]]),
                               "theta_durch_pi": th[i], "newton": res, "f0": float(f[0]), "S0": float(f[0] ** 2),
                               "Q_kontinuum": ladung_kontinuum(w2[i]), "Q_diskret_frei": q_frei,
                               "Q_diskret_angeregt": q_frei * amp * amp})
    old[0] = 0.0
    old[N] = 0.0
    meta["start"] = {"Q_gesamt_kontinuierlich": float(-2.0 * dx * (np.conj(psi) * vel).imag.sum()),
                     "E_gesamt_kontinuierlich": energie(psi, vel, dx)}
    js = int(np.argmin(np.abs(x - 0.5 * (D + L))))
    meta["sonde_x"] = float(x[js])
    meta["sonde_j"] = js
    sub = max(1, int(round(0.5 / dx)))
    stand_schreiben(pfad, psi, old, 0, [float(x[c]) for c in zentren], meta, {}, {k: [] for k in REIHEN},
                    [], [], [], [], x[::sub])
    print(f"neu: {pfad} rand {rand} w2 {w2} D {D} th {th} amp {amp} dx {dx} L {L} N {N}", flush=True)


def weiter(pfad, T_ziel, max_sek):
    t_wand = time.time()
    z = np.load(pfad, allow_pickle=False)
    meta = json.loads(str(z["meta_json"]))
    psi = z["psi"].copy()
    old = z["old"].copy()
    n = int(z["n"])
    pos = [float(v) for v in z["pos"]]
    alt = {k: z[k] for k in z.files if k not in ("psi", "old", "n", "pos", "meta_json")}
    rand, dx, dt, L = meta["rand"], meta["dx"], meta["dt"], meta["L"]
    N, j0, x, Lw, x_sd, gam, jL, jR = gitter(rand, dx, L)
    absorb = rand == "abs"
    dmp = 0.5 * dt * gam
    fakp = 1.0 / (1.0 + dmp)
    jl1, jr0 = jL, jR + 1
    dmpL, fpL, dmpR, fpR = dmp[:jl1], fakp[:jl1], dmp[jr0:], fakp[jr0:]
    n_mess = int(round(MESS / dt))
    n_bild = int(round(BILD_DT / dt))
    n_en = int(round(ENERGIE_DT / dt))
    n_ziel = int(round(T_ziel / dt))
    dt2 = dt * dt
    h2 = 1.0 / (dx * dx)
    x0 = float(x[0])
    sub = max(1, int(round(0.5 / dx)))
    js = int(meta["sonde_j"])
    r = {k: [] for k in REIHEN}
    bilder, bild_t, e_t, e_v = [], [], [], []

    def interp(arr, p):
        uu = (p - x0) / dx
        k = int(math.floor(uu))
        w = uu - k
        return (1.0 - w) * arr[k] + w * arr[k + 1]

    def parab(Sv, k):
        a, b, c = Sv[k - 1], Sv[k], Sv[k + 1]
        den = a - 2.0 * b + c
        off = 0.5 * (a - c) / den if den < 0.0 else 0.0
        return x0 + (k + max(-0.5, min(0.5, off))) * dx

    def messen(t, old, psi, new, Sv):
        v = (new - old) * (0.5 / dt)
        rho = -2.0 * (psi.real * v.imag - psi.imag * v.real)
        r["t"].append(t)
        r["Q_gitter"].append(float(dx * rho.sum()))
        r["Q_box"].append(float(dx * rho[jL:jR + 1].sum()))
        for i in range(3):
            pv = pos[i]
            klo = max(1, int(math.floor((pv - SUCH - x0) / dx)))
            khi = min(N - 1, int(math.ceil((pv + SUCH - x0) / dx)))
            k = klo + int(np.argmax(Sv[klo:khi + 1]))
            k = max(1, min(N - 1, k))
            p = parab(Sv, k)
            pos[i] = p
            zz = interp(psi, p)
            a = max(0, int(math.ceil((p - R_BALL - x0) / dx - 1e-9)))
            b = min(N, int(math.floor((p + R_BALL - x0) / dx + 1e-9)))
            r[f"p{i}"].append(p)
            r[f"S{i}"].append(float(Sv[k]))
            r[f"ph{i}"].append(math.atan2(zz.imag, zz.real))
            r[f"Q{i}"].append(float(dx * rho[a:b + 1].sum()))
        r["sonde_re"].append(float(psi[js].real))
        r["sonde_im"].append(float(psi[js].imag))

    n_von = n
    t_schleife = time.time()
    unterbrochen = False
    while n <= n_ziel:
        Sv = psi.real * psi.real + psi.imag * psi.imag
        new = 2.0 * psi - old
        pc = psi[1:-1]
        new[1:-1] += dt2 * ((psi[2:] + psi[:-2] - 2.0 * pc) * h2 - u1(Sv[1:-1]) * pc)
        if absorb:
            new[:jl1] = (new[:jl1] + dmpL * old[:jl1]) * fpL
            new[jr0:] = (new[jr0:] + dmpR * old[jr0:]) * fpR
        new[0] = 0.0
        new[N] = 0.0
        if n % n_mess == 0:
            messen(n * dt, old, psi, new, Sv)
        if n % n_en == 0:
            e_t.append(n * dt)
            e_v.append(energie(psi, (new - old) * (0.5 / dt), dx))
        if n % n_bild == 0:
            bilder.append(Sv[::sub].astype(np.float32))
            bild_t.append(n * dt)
        old, psi = psi, new
        n += 1
        if n % 5000 == 0 and time.time() - t_wand > max_sek:
            unterbrochen = True
            break
    sek = time.time() - t_schleife
    meta["abschnitte"].append({"n_von": n_von, "n_bis": n, "t_letzte_messung": (n - 1) * dt, "T_ziel": T_ziel,
                               "sek_schleife": sek, "ms_je_schritt": 1e3 * sek / max(1, n - n_von),
                               "unterbrochen": unterbrochen})
    stand_schreiben(pfad, psi, old, n, pos, meta, alt, r, bilder, bild_t, e_t, e_v, x[::sub])
    zustand = "FORTSETZEN" if unterbrochen else "ZIEL_ERREICHT"
    print(f"weiter: {pfad} t bis {(n - 1) * dt:.2f} (Ziel {T_ziel}), {sek:.1f} s Schleife, "
          f"{1e3 * sek / max(1, n - n_von):.4f} ms je Schritt, gesamt {time.time() - T_START:.1f} s: {zustand}",
          flush=True)


# ================================================================ Auswertung

def lade(pfad):
    z = np.load(pfad, allow_pickle=False)
    meta = json.loads(str(z["meta_json"]))
    r = {k[2:]: z[k] for k in z.files if k.startswith("r_")}
    ex = {k: z[k] for k in ("bilder", "bild_t", "bild_x", "e_t", "e_v") if k in z.files}
    return meta, r, ex


def bereich(t, t0, t1, letzt):
    i0 = int(np.searchsorted(t, t0 - 1e-9, side="left"))
    i1 = int(np.searchsorted(t, t1 + 1e-9, side="right")) if letzt else int(np.searchsorted(t, t1 - 1e-9, side="left"))
    return i0, i1


def spektrum(z, dts, oben=6):
    z = z - z.mean()
    w = np.hanning(z.size)
    F = np.fft.fft(z * w)
    P = np.abs(F) ** 2
    om = -2.0 * math.pi * np.fft.fftfreq(z.size, dts)  # psi ~ exp(-i om t) liegt bei om > 0: positive Ladung
    ges = float(P.sum())
    if ges <= 0.0:
        return {"gesamt": 0.0}
    ii = [j for j in range(1, P.size - 1) if P[j] > P[j - 1] and P[j] >= P[j + 1]]
    ii.sort(key=lambda j: -P[j])
    return {"spitzen": [{"omega": float(om[j]), "anteil": float(P[j] / ges)} for j in ii[:oben]],
            "anteil_betrag_unter_1": float(P[np.abs(om) < 1.0].sum() / ges),
            "anteil_negativ": float(P[om < 0.0].sum() / ges),
            "mittel_omega": float((P * om).sum() / ges), "mittel_betrag_omega": float((P * np.abs(om)).sum() / ges)}


def analyse_lauf(meta, r, ex):
    t = r["t"]
    T = float(t[-1])
    W = (T - FENSTER_START) / N_FENSTER
    fen = [(FENSTER_START + k * W, FENSTER_START + (k + 1) * W) for k in range(N_FENSTER)]
    a = {"T": T, "fenster_laenge": W, "fenster": fen, "rand": meta["rand"], "dx": meta["dx"],
         "theta_durch_pi": meta["theta_durch_pi"], "w2": meta["w2"], "D": meta["D"], "L": meta["L"],
         "amp": meta["amp"], "omega_diskret": [b["omega_diskret"] for b in meta["baelle"]],
         "Q_angeregt_t0_formel": [b["Q_diskret_angeregt"] for b in meta["baelle"]]}
    ph = [np.unwrap(r[f"ph{i}"]) for i in range(3)]
    qbad = r["Q_box"] - r["Q0"] - r["Q1"] - r["Q2"]
    zeilen = []
    for k, (t0, t1) in enumerate(fen):
        i0, i1 = bereich(t, t0, t1, k == N_FENSTER - 1)
        z = {"t0": t0, "t1": t1, "n": i1 - i0, "omega": [], "Q": [], "S": [], "S_halbe_spanne": [], "p": [],
             "da": []}
        for i in range(3):
            z["omega"].append(float(-np.polyfit(t[i0:i1], ph[i][i0:i1], 1)[0]))
            z["Q"].append(float(r[f"Q{i}"][i0:i1].mean()))
            s = r[f"S{i}"][i0:i1]
            z["S"].append(float(s.mean()))
            z["S_halbe_spanne"].append(float(0.5 * (s.max() - s.min())))
            z["p"].append(float(r[f"p{i}"][i0:i1].mean()))
            z["da"].append(bool(s.mean() >= S_DA))
        om_da = [z["omega"][i] for i in range(3) if z["da"][i]]
        z["delta"] = float(max(om_da) - min(om_da)) if len(om_da) >= 2 else None
        if len(om_da) >= 2:
            dmin = min(abs(om_da[i] - om_da[j]) for i in range(len(om_da)) for j in range(i + 1, len(om_da)))
            z["schwebung_langsam"] = float(2.0 * math.pi / dmin) if dmin > 0 else float("inf")
            z["fensterregel_ok"] = bool(W >= 2.0 * z["schwebung_langsam"])
        else:
            z["schwebung_langsam"], z["fensterregel_ok"] = None, None
        z["Q_bad"] = float(qbad[i0:i1].mean())
        z["Q_box"] = float(r["Q_box"][i0:i1].mean())
        z["Q_gitter"] = float(r["Q_gitter"][i0:i1].mean())
        z["Q_verlust_innen"] = float(r["Q_gitter"][0] - z["Q_box"])   # bei 'abs': aus [-L; L] abgestrahlt
        zs_ = r["sonde_re"][i0:i1] ** 2 + r["sonde_im"][i0:i1] ** 2
        z["sonde_psi2"] = float(zs_.mean())
        zeilen.append(z)
    a["fenster_werte"] = zeilen
    # Drift gegen Pendeln: Steigung der Fenstermittel (je 1000) und Spanne
    tc = np.asarray([0.5 * (f[0] + f[1]) for f in fen])
    dr = {}
    for i in range(3):
        om = np.asarray([z["omega"][i] for z in zeilen])
        q = np.asarray([z["Q"][i] for z in zeilen])
        dr[f"ball{i}"] = {"omega_steigung_je_1000": float(1e3 * np.polyfit(tc, om, 1)[0]),
                          "Q_steigung_je_1000": float(1e3 * np.polyfit(tc, q, 1)[0]),
                          "omega_letzt_minus_erst": float(om[-1] - om[0]), "Q_letzt_minus_erst": float(q[-1] - q[0]),
                          "omega_rel_aenderung": float((om[-1] - om[0]) / om[0]),
                          "omega_rel_aenderung_gegen_omega_d": float((om[-1] - meta["baelle"][i]["omega_diskret"])
                                                                     / meta["baelle"][i]["omega_diskret"]),
                          "Q_streuung_folgefenster": float(np.std(np.diff(q)) / math.sqrt(2.0)),
                          "omega_streuung_folgefenster": float(np.std(np.diff(om)) / math.sqrt(2.0)),
                          "Q_vorzeichenwechsel_folgedifferenzen": int(np.sum(np.diff(np.sign(np.diff(q))) != 0))}
    de = [z["delta"] for z in zeilen]
    if all(v is not None for v in de):
        dr["delta_steigung_je_1000"] = float(1e3 * np.polyfit(tc, np.asarray(de), 1)[0])
    a["drift"] = dr
    # Zeitreihen am Start (t = 0 und Mittel [0; 100]) nur zur Information
    i0, i1 = bereich(t, 0.0, FENSTER_START, False)
    a["start"] = {"Q_t0": [float(r[f"Q{i}"][0]) for i in range(3)],
                  "Q_mittel_0_100": [float(r[f"Q{i}"][i0:i1].mean()) for i in range(3)],
                  "omega_0_100": [float(-np.polyfit(t[i0:i1], ph[i][i0:i1], 1)[0]) for i in range(3)],
                  "Q_bad_t0": float(qbad[0]), "Q_box_t0": float(r["Q_box"][0]), "Q_gitter_t0": float(r["Q_gitter"][0])}
    # Erhaltung
    qg = r["Q_gitter"]
    a["erhaltung"] = {"Q_gitter_t0": float(qg[0]), "Q_gitter_T": float(qg[-1]),
                      "Q_gitter_rel_max_abw": float(np.abs(qg - qg[0]).max() / abs(qg[0])),
                      "Q_box_T": float(r["Q_box"][-1])}
    if "e_v" in ex and ex["e_v"].size:
        ev = ex["e_v"]
        a["erhaltung"].update({"E_t0": float(ev[0]), "E_T": float(ev[-1]),
                               "E_rel_max_abw": float(np.abs(ev - ev[0]).max() / abs(ev[0]))})
    # Baelle: Lageaenderung, Mindestabstand zum Rand des Innenbereichs
    a["lagen"] = {"p_t0": [float(r[f"p{i}"][0]) for i in range(3)], "p_T": [float(r[f"p{i}"][-1]) for i in range(3)],
                  "p_betrag_max": float(max(np.abs(r[f"p{i}"]).max() for i in range(3)))}
    # Bad: Sondenspektrum im ersten und letzten Fenster
    zs = r["sonde_re"] + 1j * r["sonde_im"]
    a["sonde_x"] = meta.get("sonde_x")
    sp = {}
    for nm, k in (("erstes", 0), ("letztes", N_FENSTER - 1)):
        i0, i1 = bereich(t, fen[k][0], fen[k][1], k == N_FENSTER - 1)
        sp[nm] = spektrum(zs[i0:i1], MESS)
        sp[nm]["mittel_betrag_psi2"] = float(np.mean(np.abs(zs[i0:i1]) ** 2))
    a["sonde_spektrum"] = sp
    # Dichtebilder: Zahl der Maxima > S_DA je Bild, und Baddichte |psi|^2 ausserhalb der Ballbereiche
    if "bilder" in ex and ex["bilder"].shape[0]:
        bx = ex["bild_x"]
        info = []
        for b, tb in zip(ex["bilder"], ex["bild_t"]):
            S = b.astype(np.float64)
            ii = np.nonzero((S[1:-1] > S[:-2]) & (S[1:-1] >= S[2:]) & (S[1:-1] > S_DA))[0] + 1
            info.append({"t": float(tb), "maxima_x": [float(bx[j]) for j in ii], "maxima_S": [float(S[j]) for j in ii]})
        a["bilder_maxima"] = info[::5] + ([info[-1]] if (len(info) - 1) % 5 else [])
    return a


def urteile(A):
    u_ = {}
    if not all(k in A for k in ("B1", "B1f", "B2", "K1")):
        u_["hinweis"] = "Rollen B1, B1f, B2, K1 nicht vollstaendig: keine Urteile"
        return u_

    def de(a):
        return [z["delta"] for z in a["fenster_werte"]]

    def bt1(a):
        d = de(a)
        if d[0] is None or d[-1] is None:
            return None
        return bool(d[-1] > d[0])

    def bt4(a):
        d = de(a)
        if any(v is None for v in d):
            return None
        return bool(min(d) >= 0.5 * d[0])

    # nur berichtet: Badkorrektur. Abgestrahlte Ladung je Fenster aus der Kontrolle K1 (Verlust aus [-L; L]);
    # im Bad-Arm bleibt sie in der Box. Bei gleichmaessiger Verteilung liegt der Anteil 2 R_BALL / (2 L) davon in
    # jedem Ballbereich: Q_korr_i = Q_i - 2 R_BALL * Q_verlust_K1 / (2 L).
    kverl = [z["Q_verlust_innen"] for z in A["K1"]["fenster_werte"]]

    def bt2(a):
        z0, z1 = a["fenster_werte"][0], a["fenster_werte"][-1]
        ig = int(np.argmin(z0["omega"]))
        ik = int(np.argmax(z0["omega"]))
        f0 = 2.0 * R_BALL * kverl[0] / (2.0 * a["L"]) if a["rand"] == "refl" else 0.0
        f1 = 2.0 * R_BALL * kverl[-1] / (2.0 * a["L"]) if a["rand"] == "refl" else 0.0
        return {"groesster": ig, "kleinster": ik, "dQ_groesster": z1["Q"][ig] - z0["Q"][ig],
                "dQ_kleinster": z1["Q"][ik] - z0["Q"][ik],
                "erfuellt": bool(z1["Q"][ig] > z0["Q"][ig] and z1["Q"][ik] < z0["Q"][ik]),
                "badanteil_je_ball_erst_letzt": [f0, f1],
                "dQ_korr_groesster": (z1["Q"][ig] - f1) - (z0["Q"][ig] - f0),
                "dQ_korr_kleinster": (z1["Q"][ik] - f1) - (z0["Q"][ik] - f0),
                "erfuellt_badkorrigiert": bool(z1["Q"][ig] - f1 > z0["Q"][ig] - f0
                                               and z1["Q"][ik] - f1 < z0["Q"][ik] - f0)}

    def kat(v):
        return "offen" if v is None else ("eingetroffen" if v else "nicht eingetroffen")

    def und(*v):
        if any(x is None for x in v):
            return None
        return bool(all(v))

    for nm, f in (("BT1", bt1), ("BT4", bt4)):
        haupt = und(f(A["B1"]), f(A["B2"]))
        zweit = und(f(A["B1f"]), f(A["B2"]))
        e = {"B1": f(A["B1"]), "B1f": f(A["B1f"]), "B2": f(A["B2"]), "haupt": kat(haupt), "mit_B1f": kat(zweit)}
        e["urteil"] = kat(haupt) if kat(haupt) == kat(zweit) else "offen (Gitter uneinig)"
        u_[nm] = e
    b2 = {k: bt2(A[k]) for k in ("B1", "B1f", "B2")}
    b2["urteil"] = kat(all(b2[k]["erfuellt"] for k in ("B1", "B1f", "B2")))
    b2["nur_berichtet_badkorrigiert"] = kat(all(b2[k]["erfuellt_badkorrigiert"] for k in ("B1", "B1f", "B2")))
    u_["BT2"] = b2
    k1 = A["K1"]
    rel = [abs(v) for v in (k1["drift"][f"ball{i}"]["omega_rel_aenderung"] for i in range(3))]
    rel_d = [abs(v) for v in (k1["drift"][f"ball{i}"]["omega_rel_aenderung_gegen_omega_d"] for i in range(3))]
    u_["BT3"] = {"rel_aenderung": rel, "max": max(rel), "urteil": kat(max(rel) < 0.01),
                 "nur_berichtet_gegen_omega_d": {"rel_aenderung": rel_d, "kategorie": kat(max(rel_d) < 0.01)}}
    # nur berichtet: BT1/BT4 gegen den nominellen diskreten Startwert Delta_d = max omega_d - min omega_d
    for k in ("B1", "B1f", "B2"):
        od = A[k]["omega_diskret"]
        dd = max(od) - min(od)
        d = de(A[k])
        u_.setdefault("nur_berichtet_gegen_Delta_d", {})[k] = {
            "Delta_d": dd, "Delta_erst": d[0], "Delta_letzt": d[-1], "Delta_min": min(v for v in d if v is not None),
            "BT1_letzt_gt_Delta_d": bool(d[-1] is not None and d[-1] > dd),
            "BT4_min_ge_halb_Delta_d": bool(all(v is not None and v >= 0.5 * dd for v in d))}
    # L3: Effekt (letztes minus erstes Fenster) bei dx 0,1 gegen seine Aenderung bei dx 0,05 (halber Zeitschritt)
    l3 = {}
    for nm, g in (("delta", lambda a: de(a)[-1] - de(a)[0] if de(a)[0] is not None and de(a)[-1] is not None else None),
                  ("dQ_groesster", lambda a: bt2(a)["dQ_groesster"]), ("dQ_kleinster", lambda a: bt2(a)["dQ_kleinster"])):
        e1, e2 = g(A["B1"]), g(A["B1f"])
        if e1 is None or e2 is None:
            l3[nm] = {"B1": e1, "B1f": e2, "bestanden": None}
        else:
            l3[nm] = {"B1": e1, "B1f": e2, "faktor": abs(e1) / max(abs(e1 - e2), 1e-300),
                      "bestanden": bool(5.0 * abs(e1 - e2) <= abs(e1))}
    u_["L3"] = l3
    # L2: Bad gegen Kontrolle (gleiche Startlage, Phasen 0,0,0, dx 0,1)
    l2 = {}
    for nm, g in (("delta", lambda a: de(a)[-1] - de(a)[0] if de(a)[0] is not None and de(a)[-1] is not None else None),
                  ("dQ_groesster", lambda a: bt2(a)["dQ_groesster"]), ("dQ_kleinster", lambda a: bt2(a)["dQ_kleinster"])):
        eb, ek = g(A["B1"]), g(A["K1"])
        l2[nm] = {"B1": eb, "K1": ek, "bad_minus_kontrolle": (eb - ek) if (eb is not None and ek is not None) else None}
    u_["L2"] = l2
    return u_


def tabelle(name, a):
    z = a["fenster_werte"]
    out = [f"== {name}: rand {a['rand']}, dx {a['dx']}, theta/pi {a['theta_durch_pi']}, T {a['T']}, Fenster {a['fenster_laenge']:.1f}"]
    out.append("Fenster | omega_1 omega_2 omega_3 | Delta | Q_1 Q_2 Q_3 | Q_bad | S_1 S_2 S_3 | Atmung 1 2 3 | p_1 p_2 p_3 | Regel")
    for w in z:
        d = "-" if w["delta"] is None else f"{w['delta']:.6f}"
        out.append(f"[{w['t0']:.1f}; {w['t1']:.1f}] | " + " ".join(f"{v:.6f}" for v in w["omega"]) + f" | {d} | "
                   + " ".join(f"{v:.5f}" for v in w["Q"]) + f" | {w['Q_bad']:.5f} | "
                   + " ".join(f"{v:.4f}" for v in w["S"]) + " | " + " ".join(f"{v:.4f}" for v in w["S_halbe_spanne"])
                   + " | " + " ".join(f"{v:.2f}" for v in w["p"]) + f" | {w['fensterregel_ok']}")
    return "\n".join(out)


def auswerten(aus, paare):
    A = {}
    for rolle, pfad in paare:
        meta, r, ex = lade(pfad)
        a = analyse_lauf(meta, r, ex)
        a["stand"] = pfad
        A[rolle] = a
        print(tabelle(rolle, a), flush=True)
        print(f"   Erhaltung: {json.dumps(jsonfest(a['erhaltung']))}", flush=True)
        print(f"   Drift: {json.dumps(jsonfest(a['drift']))}", flush=True)
    u_ = urteile(A)
    print("URTEILE " + json.dumps(jsonfest(u_), indent=1), flush=True)
    schreiben({"laeufe": A, "urteile": u_, "sek": time.time() - T_START,
               "konstanten": {"FENSTER_START": FENSTER_START, "N_FENSTER": N_FENSTER, "R_BALL": R_BALL, "S_DA": S_DA,
                              "SUCH": SUCH, "MESS": MESS}}, aus)


def main():
    modus = sys.argv[1]
    if modus == "neu":
        pfad, rand = sys.argv[2], sys.argv[3]
        w2 = [float(v) for v in sys.argv[4:7]]
        D = float(sys.argv[7])
        th = [bruch(v) for v in sys.argv[8:11]]
        amp, dx, L = float(sys.argv[11]), float(sys.argv[12]), float(sys.argv[13])
        neu(pfad, rand, w2, D, th, amp, dx, L)
    elif modus == "weiter":
        weiter(sys.argv[2], float(sys.argv[3]), float(sys.argv[4]))
    elif modus == "auswerten":
        auswerten(sys.argv[2], [tuple(s.split("=", 1)) for s in sys.argv[3:]])
    else:
        raise SystemExit("modus: neu | weiter | auswerten")


if __name__ == "__main__":
    main()
