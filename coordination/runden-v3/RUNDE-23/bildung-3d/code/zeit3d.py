#!/usr/bin/env python3
"""BILDUNG-3D (Runde 23). Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary, 02.10.2026.
Karte: coordination/runden-v3/RUNDE-23/bildung-3d/KARTE.md; Regeln: PLAN.md (eingefroren vor dem ersten echten Lauf).

Radiale 3D-Zeitentwicklung (l = 0) des Einfeldmodells M1, U(S) = S - S^2 + S^3/2 (BETA = 1/2), nach dem Vorbild
RUNDE-22/bildung-leiter/code/zeit2d_v2.py (2D radial): exakter Startschritt (dort V2-1), Abschnitte bis=/weiter (V2-6),
JSON ueber m.jsonfest (V2-4). Aus bic2_2d_praez_v2.py (Runde 12, unveraendert importiert): profil (dim = 3), f_werte,
jsonfest, Konstanten F64, C128, PI, BETA, SIGMA0.

- Gitter r_j = j dr, j = 0..N (N = r_max/dr), Dirichlet bei r_max. Daempfungsschicht r > r_sd mit
  gamma = SIGMA0 ((r - r_sd)/(r_max - r_sd))^2, SIGMA0 = 1 (wie zeit2d_v2). Leapfrog, dt = 0,4 dr.
- 3D-Laplace: (p[j+1] - 2 p[j] + p[j-1])/dr^2 + (p[j+1] - p[j-1])/(r_j dr)  (= psi_rr + 2 psi_r/r, zentral),
  bei r = 0: 6 (p[1] - p[0])/dr^2. Fuer j >= 1 ist das algebraisch das u = r psi-Schema (u_rr/r).
- Profil: m.profil(w2, 3.0, BETA, dr) und m.f_werte, danach Newton auf der diskreten Gleichung
  lap f + (w2 - U'(f^2)) f = 0 desselben Gitters (f_N = 0). Dann ist f exp(-i w_d t), w_d = (2/dt) asin(w dt/2),
  exakte Loesung des Leapfrog-Schemas (K0).
- Start: phi(-dt) = phi - q dt vel + dt^2/2 a(phi), q = sqrt(1 - w0^2 dt^2/4) je Reihe (exakter Startschritt).
- Integrale: Trapezregel in r, Gewichte w_0 = 0, w_j = 4 pi r_j^2 dr. Ladung Q = sum w_j (-2 Im(conj(p_j) v_j)),
  v = (phi(t+dt) - phi(t-dt))/(2 dt). Energie E = sum w_j (|v_j|^2 + U(|p_j|^2))
  + sum_j 4 pi r_{j+1/2}^2 dr |p_{j+1} - p_j|^2/dr^2 (Gradient versetzt). Familie: dieselben Formeln mit v = -i w f.
- Klumpen psi = A exp(-r^2/(2 s^2)), psi_t = -i w0 psi; Q = 2 w0 A^2 pi^(3/2) s^3 = Q_F; rms-Radius von |psi|^2 ist
  s sqrt(3/2), also s = fak R_rms,F sqrt(2/3).

Befehle:
  familie <dr> <r_max> <r_sd> <aus.json> <w2> [<w2> ...]
  lauf <dr> <T> <r_sd> <r_max> <reihen> <aus.json> [bis=<t>] [weiter]
       reihen: Komma-Liste aus K0-0.60, K0-0.55, i, ii, iii, iv
  auswerten <gesamt.json> <familie.json,familie.json,...> <roh.pt> [<roh.pt> ...] [zeiten=<T1,T2,...>]
       (zeiten= nur fuer den Rauchlauf; Vorgabe 250, 500, 1000)
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import torch  # noqa: E402
from scipy.interpolate import CubicSpline  # noqa: E402
from scipy.linalg import solve_banded  # noqa: E402

torch.set_num_threads(1)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bic2_2d_praez_v2 as m  # noqa: E402

F64, C128, PI, BETA, SIGMA0 = m.F64, m.C128, m.PI, m.BETA, m.SIGMA0
VERSION = "zeit3d_v1"
DT_FAK = 0.4                          # dt = 0,4 dr (wie zeit2d_v2)
MESS = 0.2                            # Messabstand, ganzes Vielfaches von dt
FENSTER = 50.0                        # Fenster [T - 50, T] fuer omega_mess, Q_Ball, E/Q, Spanne
T_AUSWERT = (250.0, 500.0, 1000.0)
SCHWELLE_AUF = 0.10                   # |Q_Ball - Q_F(omega_mess)| / Q_F(omega_mess) < 10 %
SCHWELLE_K0 = 1e-8                    # K0: Zentraldichte relativ < 1e-8 bis T = 1000
SCHWELLE_ATMUNG = 0.05                # B3D-3: Spanne der Zentraldichte / Mittel > 5 %
R_SCHALEN = (10.0, 20.0, 30.0, 40.0)  # nur berichtet: Ladung/Energie in r < R
R_KERN = 30.0                         # nur berichtet: Anteil von Q_Ball in r < 30, R_rms in r < 30
SCHNAPP_ABSTAND = 50.0                # Dichteschnappschuesse (nur berichtet)
FREQ_FENSTER = 200.0                  # nur berichtet: Atmungsfrequenz aus [T - 200, T]
REIHEN = {"K0-0.60": ("exakt", 0.60, 1.0), "K0-0.55": ("exakt", 0.55, 1.0), "i": ("gauss", 0.60, 1.0),
          "ii": ("gauss", 0.60, 1.3), "iii": ("gauss", 0.60, 0.7), "iv": ("gauss", 0.55, 1.0)}


def sha(pfad):
    with open(pfad, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


CODE_SHA = {"zeit3d.py": sha(os.path.abspath(__file__)), "bic2_2d_praez_v2.py": sha(m.__file__)}


def uu(S):
    return S - S * S + BETA * S * S * S


def u1(S):
    return 1.0 - 2.0 * S + 3.0 * BETA * S * S


def u2(S):
    return -2.0 + 6.0 * BETA * S


def gitter(dr, r_max):
    N = int(round(r_max / dr))
    r = np.arange(N + 1) * dr
    w = 4.0 * PI * r * r * dr                       # Trapezregel; w_0 = 0, f_N = 0
    wh = 4.0 * PI * (r[:-1] + 0.5 * dr) ** 2 * dr   # Intervall [r_j, r_j+1], j = 0..N-1
    inv_rdr = np.zeros(N + 1)
    inv_rdr[1:] = 1.0 / (r[1:] * dr)
    return N, r, w, wh, inv_rdr


def lap_np(f, dr, inv_rdr):
    a = np.zeros_like(f)
    a[1:-1] = (f[2:] - 2.0 * f[1:-1] + f[:-2]) / dr ** 2 + (f[2:] - f[:-2]) * inv_rdr[1:-1]
    a[0] = 6.0 * (f[1] - f[0]) / dr ** 2
    return a


def diskretes_profil(f0, w2, dr, inv_rdr, iters=30):
    """Newton auf F_j = lap f + (w2 - U'(f^2)) f = 0, j = 0..N-1, f_N = 0 (tridiagonal, scipy solve_banded)."""
    f = np.array(f0, dtype=np.float64)
    N = len(f) - 1
    verlauf = []
    for _ in range(iters):
        S = f * f
        F = (lap_np(f, dr, inv_rdr) + (w2 - u1(S)) * f)[:N]
        res = float(np.abs(F).max())
        verlauf.append(res)
        if res < 1e-13:
            break
        Sn = S[:N]
        diag = -2.0 / dr ** 2 + w2 - u1(Sn) - 2.0 * Sn * u2(Sn)
        diag[0] = -6.0 / dr ** 2 + w2 - u1(S[0]) - 2.0 * S[0] * u2(S[0])
        ober = np.zeros(N)                         # ober[j] = dF_j/df_j+1, j = 0..N-2
        unter = np.zeros(N)                        # unter[j] = dF_j/df_j-1, j = 1..N-1
        ober[0] = 6.0 / dr ** 2
        ober[1:N - 1] = 1.0 / dr ** 2 + inv_rdr[1:N - 1]
        unter[1:N] = 1.0 / dr ** 2 - inv_rdr[1:N]
        ab = np.zeros((3, N))
        ab[0, 1:] = ober[:N - 1]
        ab[1, :] = diag
        ab[2, :-1] = unter[1:]
        f[:N] += solve_banded((1, 1), ab, -F)
    S = f * f
    rest = float(np.abs((lap_np(f, dr, inv_rdr) + (w2 - u1(S)) * f)[:N]).max())
    return f, verlauf, rest


def r_halb_np(S, dr):
    s0 = S[0]
    for j in range(1, len(S)):
        if S[j] < 0.5 * s0:
            a, b = S[j - 1] - 0.5 * s0, S[j] - 0.5 * s0
            return float((j - 1 + a / (a - b)) * dr)
    return float(len(S) * dr)


def familienwerte(f, w2, dr, r, w, wh, r_sd):
    om = math.sqrt(w2)
    S = f * f
    nS = float((w * S).sum())
    Q = 2.0 * om * nS
    R_rms = math.sqrt(float((w * r * r * S).sum()) / nS)
    grad = float((wh * ((f[1:] - f[:-1]) / dr) ** 2).sum())
    pot = float((w * uu(S)).sum())
    kin = w2 * nS
    E = kin + grad + pot
    j_sd = int(round(r_sd / dr))
    return {"w2": w2, "omega": om, "Q_F": Q, "E_F": E, "E_durch_Q": E / Q, "R_rms": R_rms, "S0": float(S[0]),
            "r_halb": r_halb_np(S, dr), "E_kin": kin, "E_grad": grad, "E_pot": pot,
            "virial_rest": (grad - 3.0 * (kin - pot)) / grad,          # Derrick 3D: E_grad = 3 (E_kin - E_pot)
            "S_bei_r_sd_rel": float(S[j_sd] / S[0]), "Q_ausserhalb_r_sd_rel": 2.0 * om * float((w[j_sd:] * S[j_sd:]).sum()) / Q,
            "f_min": float(f[:-1].min())}


def profil_diskret(w2, dr, r_max, r_sd):
    t0 = time.time()
    N, r, w, wh, inv_rdr = gitter(dr, r_max)
    prof = m.profil(w2, 3.0, BETA, dr, torch.device("cpu"))
    f_l, _ = m.f_werte(prof, N + 1)
    f_l[-1] = 0.0
    f, verlauf, rest = diskretes_profil(f_l, w2, dr, inv_rdr)
    fam = familienwerte(f, w2, dr, r, w, wh, r_sd)
    fam.update({"dr": dr, "r_max": r_max, "r_sd": r_sd, "N": N, "newton_residuen": verlauf, "newton_rest": rest,
                "f0_ode": prof["f0"], "f0_diskret": float(f[0]), "profil_ode_grund": prof["grund"],
                "profil_ode_r_cut": prof["r_cut"], "sek": time.time() - t0})
    fam["ok"] = bool(rest < 1e-8 and math.isfinite(fam["Q_F"]))
    return f, fam


def schreiben(out, pfad):
    with open(pfad + ".tmp", "w") as fh:
        json.dump(m.jsonfest(out), fh, indent=1)
    os.replace(pfad + ".tmp", pfad)


# ================================================================ Familie

def familie(dr, r_max, r_sd, pfad, w2_liste):
    t0 = time.time()
    erg = []
    for w2 in w2_liste:
        _, fam = profil_diskret(w2, dr, r_max, r_sd)
        erg.append(fam)
        print(f"  w2 {w2:.2f}: Q_F {fam['Q_F']:.6g}, E/Q {fam['E_durch_Q']:.6f}, R_rms {fam['R_rms']:.4f}, S0 "
              f"{fam['S0']:.5f}, Newton-Rest {fam['newton_rest']:.1e}, Virial {fam['virial_rest']:.1e}, "
              f"{fam['sek']:.1f} s", flush=True)
    schreiben({"version": VERSION, "code_sha256": CODE_SHA, "dr": dr, "r_max": r_max, "r_sd": r_sd, "familie": erg,
               "sek": time.time() - t0}, pfad)
    print(f"zeit3d familie fertig: dr {dr}, {len(erg)} Punkte, {time.time() - t0:.1f} s", flush=True)


# ================================================================ Zeitlauf

def lap3d(p, dr2, inv_rdr):
    a = torch.empty_like(p)
    a[:, 1:-1] = (p[:, 2:] - 2.0 * p[:, 1:-1] + p[:, :-2]) / dr2 + (p[:, 2:] - p[:, :-2]) * inv_rdr[1:-1]
    a[:, 0] = 6.0 * (p[:, 1] - p[:, 0]) / dr2
    a[:, -1] = 0.0                                   # Dirichlet bei r_max
    return a


def dichten(phi, v, w, wh_dr2):
    S = phi.real ** 2 + phi.imag ** 2
    qd = -2.0 * (phi.conj() * v).imag * w
    ed = (v.real ** 2 + v.imag ** 2 + uu(S)) * w
    dp = phi[:, 1:] - phi[:, :-1]
    gd = (dp.real ** 2 + dp.imag ** 2) * wh_dr2
    return qd, ed, gd


def rechnen(dr, T, r_sd, r_max, namen, bis=None, zustand=None):
    t_wand = time.time()
    N, r_np, w_np, wh_np, inv_rdr_np = gitter(dr, r_max)
    profile = {}
    for nm in namen:
        w2 = REIHEN[nm][1]
        if w2 not in profile:
            profile[w2] = profil_diskret(w2, dr, r_max, r_sd)
    r = torch.tensor(r_np, dtype=F64)
    w = torch.tensor(w_np, dtype=F64)
    wh_dr2 = torch.tensor(wh_np / (dr * dr), dtype=F64)
    inv_rdr = torch.tensor(inv_rdr_np, dtype=F64)
    dr2 = dr * dr
    j_sd = int(round(r_sd / dr))
    G, w0, info = [], [], []
    for nm in namen:
        art, w2, fak = REIHEN[nm]
        f, fam = profile[w2]
        om = math.sqrt(w2)
        e = {"reihe": nm, "art": art, "w2": w2, "w0": om, "Q_F": fam["Q_F"], "R_rms_F": fam["R_rms"],
             "E_durch_Q_F": fam["E_durch_Q"], "S0_F": fam["S0"]}
        if art == "exakt":
            g = torch.tensor(f, dtype=F64)
        else:
            s = fak * fam["R_rms"] * math.sqrt(2.0 / 3.0)
            A = math.sqrt(fam["Q_F"] / (2.0 * om * PI ** 1.5 * s ** 3))
            g = A * torch.exp(-(r * r) / (2.0 * s * s))
            g[-1] = 0.0
            e.update({"fak": fak, "s": s, "A": A, "R_rms_soll": fak * fam["R_rms"]})
        G.append(g)
        w0.append(om)
        info.append(e)
    G = torch.stack(G)
    w0t = torch.tensor(w0, dtype=F64).unsqueeze(1)
    phi = G.to(C128)
    vel = -1j * w0t * phi
    qd, ed, gd = dichten(phi, vel, w, wh_dr2)
    S_t0 = (G * G)
    for b, e in enumerate(info):
        e["Q_t0_formel"] = float(qd[b].sum())
        e["E_t0_formel"] = float(ed[b].sum() + gd[b].sum())
        e["E_durch_Q_t0"] = e["E_t0_formel"] / e["Q_t0_formel"]
        e["R_rms_t0"] = math.sqrt(float((w * r * r * S_t0[b]).sum() / (w * S_t0[b]).sum()))
        e["S_zentrum_t0"] = float(S_t0[b, 0])
        e["S_bei_r_sd_rel_t0"] = float(S_t0[b, j_sd] / S_t0[b, 0])
    dt = DT_FAK * dr
    om_d = [2.0 / dt * math.asin(0.5 * o * dt) for o in w0]
    q_start = torch.sqrt(1.0 - 0.25 * w0t * w0t * dt * dt)          # = cos(w_d dt/2) je Reihe
    n_mess = max(1, int(round(MESS / dt)))
    mess = n_mess * dt
    n_schritte = int(round(T / dt))
    n_schnapp = int(round(SCHNAPP_ABSTAND / dt))
    k_schnapp = max(1, int(round(0.2 / dr)))
    gam = torch.where(r > r_sd, SIGMA0 * ((r - r_sd) / (r_max - r_sd)) ** 2, torch.zeros_like(r))
    fak_p = 1.0 / (1.0 + 0.5 * dt * gam)
    fak_m = 1.0 - 0.5 * dt * gam
    radien = list(R_SCHALEN) + [r_sd, r_max]
    idx = torch.tensor([int(round(x / dr)) - 1 for x in radien])

    def beschl(p):
        a = lap3d(p, dr2, inv_rdr)
        S = p.real ** 2 + p.imag ** 2
        a = a - u1(S) * p
        a[:, -1] = 0.0
        return a

    phi_alt = phi - q_start * dt * vel + 0.5 * dt * dt * beschl(phi)
    sek_profil = time.time() - t_wand
    ts, zentrum, ladung, energie, schnapp_t, schnapp = [], [], [], [], [], []
    n_von, sek_vorher = 0, 0.0
    param = [dr, T, r_sd, r_max, list(namen)]
    if zustand is not None:
        if zustand["param"] != param or not torch.equal(zustand["G"], G):
            raise SystemExit("Zustand passt nicht zu diesem Aufruf (Parameter oder Anfangsdaten verschieden)")
        phi, phi_alt = zustand["phi"], zustand["phi_alt"]
        n_von, sek_vorher = zustand["n_naechster"], zustand["sek_schleife"]
        ts = list(zustand["ts"])
        zentrum, ladung, energie = (list(zustand[k].unbind(0)) for k in ("zentrum", "ladung", "energie"))
        schnapp_t = list(zustand["schnapp_t"])
        schnapp = list(zustand["schnapp"].unbind(0))
    n_bis = n_schritte + 1 if bis is None else min(n_schritte + 1, int(round(bis / dt)))
    t_schleife = time.time()
    for n in range(n_von, n_bis):
        t = n * dt
        a = beschl(phi)
        phi_neu = (2.0 * phi - fak_m * phi_alt + dt * dt * a) * fak_p
        if n % n_mess == 0:
            v = (phi_neu - phi_alt) / (2.0 * dt)
            qd, ed, gd = dichten(phi, v, w, wh_dr2)
            ts.append(t)
            zentrum.append(phi[:, 0].clone())
            ladung.append(torch.cumsum(qd, 1)[:, idx])
            energie.append(torch.cumsum(ed, 1)[:, idx] + torch.cumsum(gd, 1)[:, idx])
        if n % n_schnapp == 0:
            schnapp_t.append(t)
            schnapp.append((phi.real ** 2 + phi.imag ** 2)[:, ::k_schnapp].clone())
        if n == n_von + 2000:
            je = (time.time() - t_schleife) / 2000.0
            print(f"  nach 2000 Schritten: {je * 1e3:.3f} ms je Schritt, dieser Abschnitt geschaetzt "
                  f"{je * (n_bis - n_von):.0f} s", flush=True)
        phi_alt, phi = phi, phi_neu
    sek_schleife = sek_vorher + time.time() - t_schleife
    out = {"version": VERSION, "code_sha256": CODE_SHA, "dr": dr, "dt": dt, "mess": mess, "T": T, "r_sd": r_sd,
           "r_max": r_max, "N": N, "namen": list(namen), "reihen": info, "omega_diskret": om_d,
           "radien": radien, "k_sd": len(R_SCHALEN), "k_schnapp": k_schnapp,
           "profile": {str(k): v[1] for k, v in profile.items()},
           "sek_profil": sek_profil, "sek_schleife": sek_schleife, "n_schritte": n_schritte,
           "sek_je_schritt": sek_schleife / max(1, n_bis), "start": "exakt diskret (q = cos(w_d dt/2) je Reihe)",
           "abschnitt": {"n_von": n_von, "n_bis": n_bis, "fortsetzung": zustand is not None}}
    if n_bis < n_schritte + 1:
        zustand_neu = {"param": param, "G": G, "phi": phi, "phi_alt": phi_alt, "n_naechster": n_bis,
                       "sek_schleife": sek_schleife, "ts": ts, "zentrum": torch.stack(zentrum),
                       "ladung": torch.stack(ladung), "energie": torch.stack(energie), "schnapp_t": schnapp_t,
                       "schnapp": torch.stack(schnapp), "meta": out}
        return None, out, zustand_neu
    roh = {"ts": ts, "zentrum": torch.stack(zentrum), "ladung": torch.stack(ladung), "energie": torch.stack(energie),
           "schnapp_t": schnapp_t, "schnapp": torch.stack(schnapp)}
    sz = roh["zentrum"].abs() ** 2
    q = roh["ladung"][:, :, len(R_SCHALEN)]
    for b, e in enumerate(info):                       # Kurzbericht; gewertet wird mit "auswerten"
        e["S_zentrum_rel_abw_max"] = float(((sz[:, b] - sz[0, b]).abs() / sz[0, b]).max())
        e["Q_r_sd_anfang"] = float(q[0, b])
        e["Q_r_sd_ende"] = float(q[-1, b])
    return roh, out, None


# ================================================================ Auswertung

def familie_laden(pfade, dr, r_max):
    eintr = {}
    for p in pfade:
        with open(p) as fh:
            d = json.load(fh)
        if abs(d["dr"] - dr) < 1e-12 and abs(d["r_max"] - r_max) < 1e-9:
            for e in d["familie"]:
                if e["ok"]:
                    eintr[round(e["w2"], 6)] = e
    xs = sorted(eintr)
    if len(xs) < 4:
        raise SystemExit(f"Familie fuer dr {dr}, r_max {r_max} unvollstaendig ({len(xs)} Punkte)")
    x = np.array(xs)
    return {"x": x, "n": len(xs), "q": CubicSpline(x, np.log([eintr[k]["Q_F"] for k in xs])),
            "eq": CubicSpline(x, [eintr[k]["E_durch_Q"] for k in xs]), "s0": CubicSpline(x, [eintr[k]["S0"] for k in xs]),
            "rms": CubicSpline(x, [eintr[k]["R_rms"] for k in xs])}


def atmungsfrequenz(tt, sz):
    """Nur berichtet: Lage des groessten Periodogramm-Gipfels von S_zentrum - Mittel (Hann, 8-fach aufgefuellt)."""
    if len(tt) < 16:
        return None
    y = (sz - sz.mean()) * np.hanning(len(sz))
    n = 8 * len(y)
    p = np.abs(np.fft.rfft(y, n)) ** 2
    om = 2.0 * PI * np.fft.rfftfreq(n, tt[1] - tt[0])
    k = int(np.argmax(p[1:]) + 1)
    return float(om[k])


def auswerten_lauf(roh, fam, zeiten):
    out = roh["meta"]
    ts = np.array(roh["ts"])
    dt, r_sd = out["dt"], out["r_sd"]
    z = roh["zentrum"].numpy()
    lad = roh["ladung"].numpy()
    ene = roh["energie"].numpy()
    k_sd = out["k_sd"]
    k_kern = out["radien"].index(R_KERN)
    st = np.array(roh["schnapp_t"])
    sn = roh["schnapp"].numpy()                         # (n_s, B, n_r)
    r_s = np.arange(sn.shape[2]) * out["k_schnapp"] * out["dr"]
    w_s = 4.0 * PI * r_s * r_s
    erg = []
    for b, nm in enumerate(out["namen"]):
        p0 = z[:, b]
        sz = np.abs(p0) ** 2
        dphi = np.angle(p0[1:] / p0[:-1])
        phase = np.concatenate([[np.angle(p0[0])], np.angle(p0[0]) + np.cumsum(dphi)])
        q_sd, e_sd = lad[:, b, k_sd], ene[:, b, k_sd]
        e = {"reihe": nm, "S_zentrum_t0": float(sz[0]), "S_zentrum_rel_abw_max": float(np.abs(sz - sz[0]).max() / sz[0]),
             "dphi_max": float(np.abs(dphi).max()), "Q_t0": float(q_sd[0]), "E_t0": float(e_sd[0]),
             "E_durch_Q_t0": float(e_sd[0] / q_sd[0]), "zeiten": []}
        for Te in zeiten:
            if Te > out["T"] + 1e-9:
                e["zeiten"].append({"T": Te, "urteil": "offen (Lauf zu kurz)"})
                continue
            msk = (ts >= Te - FENSTER - 1e-9) & (ts <= Te + 1e-9)
            tt, ph = ts[msk], phase[msk]
            b1, b0 = np.polyfit(tt, ph, 1)
            om_d = -float(b1)
            om = 2.0 / dt * math.sin(0.5 * om_d * dt)
            qb, eb = float(q_sd[msk].mean()), float(e_sd[msk].mean())
            s_f = sz[msk]
            d = {"T": Te, "fenster": [float(tt[0]), float(tt[-1])], "n_punkte": int(msk.sum()), "omega_d": om_d,
                 "omega_mess": om, "phase_rest_max": float(np.abs(ph - (b0 + b1 * tt)).max()),
                 "dphi_max_fenster": float(np.abs(np.diff(ph)).max()),
                 "Q_Ball": qb, "Q_Anteil": qb / float(q_sd[0]), "E_Ball": eb, "E_durch_Q": eb / qb,
                 "Q_kern_anteil": float(lad[msk, b, k_kern].mean()) / qb,
                 "Q_schalen": [float(lad[msk, b, k].mean()) for k in range(len(out["radien"]))],
                 "S_zentrum_mittel": float(s_f.mean()), "S_zentrum_min": float(s_f.min()),
                 "S_zentrum_max": float(s_f.max()), "Spanne_abs": float(s_f.max() - s_f.min()),
                 "Spanne_rel": float((s_f.max() - s_f.min()) / s_f.mean())}
            mf = (ts >= Te - FREQ_FENSTER - 1e-9) & (ts <= Te + 1e-9)
            d["atmung_omega"] = atmungsfrequenz(ts[mf], sz[mf])
            js = np.where(np.abs(st - Te) < 1e-6)[0]
            if js.size:
                dn = sn[js[0], b]
                kk = r_s < R_KERN
                d["R_rms_kern"] = float(math.sqrt((w_s[kk] * r_s[kk] ** 2 * dn[kk]).sum() / (w_s[kk] * dn[kk]).sum()))
            w2m = om * om
            if d["dphi_max_fenster"] > 0.5 * PI:                      # Phasensprung je Messpunkt > pi/2: Abwicklung unsicher
                d.update({"w2_mess": w2m, "Q_F_mess": None, "abw": None, "urteil": "offen (Phase unsicher)"})
            elif om <= 0.0 or w2m <= 0.5 or w2m >= 1.0:
                d.update({"w2_mess": w2m, "Q_F_mess": None, "abw": None, "urteil": "nicht auf (keine Familie)"})
            elif w2m < fam["x"][0] or w2m > fam["x"][-1]:
                d.update({"w2_mess": w2m, "Q_F_mess": None, "abw": None, "urteil": "offen (ausserhalb der Tabelle)"})
            else:
                qf = float(math.exp(fam["q"](w2m)))
                abw = (qb - qf) / qf
                eqf = float(fam["eq"](w2m))
                d.update({"w2_mess": w2m, "Q_F_mess": qf, "abw": abw,
                          "urteil": "auf" if abs(abw) < SCHWELLE_AUF else "nicht auf",
                          "E_durch_Q_F_mess": eqf, "E_durch_Q_abw": (eb / qb) / eqf - 1.0,
                          "S0_F_mess": float(fam["s0"](w2m)), "R_rms_F_mess": float(fam["rms"](w2m))})
            e["zeiten"].append(d)
        erg.append(e)
    return {"dr": out["dr"], "T": out["T"], "r_sd": r_sd, "r_max": out["r_max"], "familie_punkte": fam["n"],
            "reihen": erg}


def urteil_bei(e, Te):
    for d in e["zeiten"]:
        if abs(d["T"] - Te) < 1e-9:
            return d
    return None


def wertung(ausw, dr):
    def finde(nm):
        for a in ausw:
            if abs(a["dr"] - dr) < 1e-12:
                for e in a["reihen"]:
                    if e["reihe"] == nm:
                        return e
        return None

    w = {}
    k0 = [finde("K0-0.60"), finde("K0-0.55")]
    if any(x is None for x in k0):
        w["B3D-0"] = {"ausgang": "offen", "grund": "K0-Lauf fehlt"}
    else:
        werte = [x["S_zentrum_rel_abw_max"] for x in k0]
        w["B3D-0"] = {"ausgang": "eingetroffen" if max(werte) < SCHWELLE_K0 else "nicht eingetroffen",
                      "K0-0.60": werte[0], "K0-0.55": werte[1]}

    def u(nm, Te):
        e = finde(nm)
        d = urteil_bei(e, Te) if e is not None else None
        return (d["urteil"] if d is not None else "offen (fehlt)"), d

    u1_, d1 = u("i", 500.0)
    w["B3D-1"] = {"ausgang": "eingetroffen" if u1_ == "auf" else ("nicht eingetroffen" if u1_.startswith("nicht auf")
                                                                   else "offen"), "urteil_i_500": u1_,
                  "abw": d1.get("abw") if d1 else None}
    u2a, d2a = u("ii", 1000.0)
    u2b, d2b = u("iii", 1000.0)
    if u2a == "auf" and u2b == "auf":
        a2 = "eingetroffen"
    elif u2a.startswith("nicht auf") or u2b.startswith("nicht auf"):
        a2 = "nicht eingetroffen"
    else:
        a2 = "offen"
    w["B3D-2"] = {"ausgang": a2, "urteil_ii_1000": u2a, "urteil_iii_1000": u2b,
                  "abw_ii": d2a.get("abw") if d2a else None, "abw_iii": d2b.get("abw") if d2b else None}
    u3, d3 = u("iv", 1000.0)
    sp = d3.get("Spanne_rel") if d3 else None
    if u3 == "auf":
        a3 = "nicht eingetroffen"
    elif u3.startswith("nicht auf"):
        a3 = "eingetroffen" if (sp is not None and sp > SCHWELLE_ATMUNG) else "nicht eingetroffen"
    else:
        a3 = "offen"
    w["B3D-3"] = {"ausgang": a3, "urteil_iv_1000": u3, "Spanne_rel_iv_1000": sp, "abw": d3.get("abw") if d3 else None}
    return w


def auswerten(gesamt, fam_pfade, roh_pfade, zeiten):
    t0 = time.time()
    ausw = []
    for p in roh_pfade:
        roh = torch.load(p, weights_only=False)
        fam = familie_laden(fam_pfade, roh["meta"]["dr"], roh["meta"]["r_max"])
        a = auswerten_lauf(roh, fam, zeiten)
        a["quelle"] = p
        a["quelle_sha256"] = sha(p)
        ausw.append(a)
        print(f"  ausgewertet: {p}", flush=True)
    erg = {"version": VERSION, "code_sha256": CODE_SHA, "zeiten": list(zeiten), "familien": fam_pfade,
           "familien_sha256": [sha(p) for p in fam_pfade], "laeufe": ausw,
           "wertung_dr_0.02": wertung(ausw, 0.02), "wertung_dr_0.04_berichtet": wertung(ausw, 0.04),
           "sek": time.time() - t0}
    schreiben(erg, gesamt)
    print(f"zeit3d auswerten fertig: {len(ausw)} Laeufe, {time.time() - t0:.1f} s", flush=True)


def main():
    if sys.argv[1] == "familie":
        dr, r_max, r_sd, pfad = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
        familie(dr, r_max, r_sd, pfad, [float(x) for x in sys.argv[6:]])
        return
    if sys.argv[1] == "auswerten":
        zeiten = T_AUSWERT
        rest = []
        for a in sys.argv[4:]:
            if a.startswith("zeiten="):
                zeiten = tuple(float(x) for x in a[7:].split(","))
            else:
                rest.append(a)
        auswerten(sys.argv[2], sys.argv[3].split(","), rest, zeiten)
        return
    if sys.argv[1] != "lauf":
        raise SystemExit("Befehl: familie | lauf | auswerten")
    dr, T, r_sd, r_max = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
    namen = sys.argv[6].split(",")
    pfad = sys.argv[7]
    opts = sys.argv[8:]
    for nm in namen:
        if nm not in REIHEN:
            raise SystemExit(f"unbekannte Reihe {nm}")
    bis = None
    for o in opts:
        if o.startswith("bis="):
            bis = float(o[4:])
    zustand = torch.load(pfad + ".zustand.pt", weights_only=False) if "weiter" in opts else None
    t_wand = time.time()
    roh, out, zustand_neu = rechnen(dr, T, r_sd, r_max, namen, bis, zustand)
    if zustand_neu is not None:
        torch.save(zustand_neu, pfad + ".zustand.pt.tmp")
        os.replace(pfad + ".zustand.pt.tmp", pfad + ".zustand.pt")
        print(f"zeit3d Abschnitt gesichert: dr {dr}, Schritte {out['abschnitt']['n_von']} bis "
              f"{out['abschnitt']['n_bis']} von {out['n_schritte'] + 1}, Schleife bisher {out['sek_schleife']:.1f} s",
              flush=True)
        return
    roh["meta"] = out
    torch.save(roh, pfad + ".roh.pt.tmp")
    os.replace(pfad + ".roh.pt.tmp", pfad + ".roh.pt")
    out["sek"] = time.time() - t_wand
    schreiben(out, pfad)
    kurz = ", ".join(f"{e['reihe']}: K0-Mass {e['S_zentrum_rel_abw_max']:.1e}, Q {e['Q_r_sd_anfang']:.6g} -> "
                     f"{e['Q_r_sd_ende']:.6g}" for e in out["reihen"])
    print(f"zeit3d lauf fertig: dr {dr}, T {T}, {out['sek']:.1f} s (Profil {out['sek_profil']:.1f}, Schleife "
          f"{out['sek_schleife']:.1f}); {kurz}", flush=True)


if __name__ == "__main__":
    main()
