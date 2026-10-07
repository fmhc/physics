#!/usr/bin/env python3
"""D2 (Runde 16, drei-takt): zwei Schrittmacher A, B und ein Dritter C (Phasenmodell).

  theta_C' = omega_C + K [sin(theta_A - theta_C) + sin(theta_B - theta_C)] + F sin(Omega t + psi - theta_C)
D2a/D2b: theta_A = theta_B = t, phi = theta_C - t:
  phi' = Delta - 2K sin(phi) + F sin((Omega - 1) t + psi - phi)
D2c: theta_A = omega_A t, theta_B = omega_B t (explorativ).

Aufruf: python d2_phasen_teile.py <ausgabeordner> <teile: ab oder c> (PLAN-NACHTRAG-2: Aufteilung)
"""
import sys, os, json, time
import numpy as np


def rk4_phase(rate, phi0, t0, dt, nschritte, beob=None):
    phi = phi0.copy(); t = t0
    for _ in range(nschritte):
        k1 = rate(t, phi)
        k2 = rate(t + 0.5 * dt, phi + 0.5 * dt * k1)
        k3 = rate(t + 0.5 * dt, phi + 0.5 * dt * k2)
        k4 = rate(t + dt, phi + dt * k3)
        phi = phi + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t += dt
        if beob is not None:
            beob(t, phi)
    return phi, t


def d2a(rauch):
    Ks = [0.5, 1.0]
    abst = np.logspace(-4, 0, 9 if rauch else 21)
    K = np.repeat(Ks, abst.size); Dl = 2 * K + np.tile(abst, len(Ks))
    T_ad = 2 * np.pi / np.sqrt(Dl ** 2 - 4 * K ** 2)
    dt = 0.01
    # Integrationsdauer: mindestens 20 Spruenge der laengsten Periode, hoechstens 2e4 (rauch 2e3)
    T_end = min(20 * T_ad.max(), 2e3 if rauch else 2e4)
    n = int(T_end / dt)
    phi = np.zeros_like(K)
    # Sprungzeiten ueber Durchgaenge von phi durch pi + 2 pi k (lineare Interpolation)
    erste = np.full(K.size, np.nan); letzte = np.full(K.size, np.nan); zahl = np.zeros(K.size, int)
    k_alt = np.floor((phi - np.pi) / (2 * np.pi))
    t = 0.0
    rate = lambda t, p: Dl - 2 * K * np.sin(p)
    phi_alt = phi.copy()
    for i in range(n):
        k1 = rate(t, phi); k2 = rate(t, phi + 0.5 * dt * k1); k3 = rate(t, phi + 0.5 * dt * k2); k4 = rate(t, phi + dt * k3)
        phi_neu = phi + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        k_neu = np.floor((phi_neu - np.pi) / (2 * np.pi))
        sp = k_neu > k_alt
        if sp.any():
            ziel = np.pi + 2 * np.pi * k_neu[sp]
            frac = (ziel - phi[sp]) / (phi_neu[sp] - phi[sp])
            ts = t + frac * dt
            erste[sp] = np.where(np.isnan(erste[sp]), ts, erste[sp])
            letzte[sp] = ts
            zahl[sp] += 1
        phi = phi_neu; k_alt = k_neu; t += dt
    T_num = (letzte - erste) / np.maximum(zahl - 1, 1)
    rel = T_num / T_ad - 1
    zeilen = []
    for i in range(K.size):
        zeilen.append(dict(K=float(K[i]), abstand=float(Dl[i] - 2 * K[i]), Delta=float(Dl[i]), T_adler=float(T_ad[i]),
                           T_num=float(T_num[i]) if zahl[i] >= 2 else None, spruenge=int(zahl[i]),
                           rel_abw=float(rel[i]) if zahl[i] >= 2 else None))
    # Steigung im log-log fuer die 5 kleinsten Abstaende je K (mit mind. 2 Spruengen)
    steig = {}
    for Kv in Ks:
        sel = (K == Kv) & (zahl >= 2)
        a = (Dl - 2 * K)[sel]; Tn = T_num[sel]
        o = np.argsort(a)[:5]
        if o.size >= 2:
            steig[str(Kv)] = float(np.polyfit(np.log(a[o]), np.log(Tn[o]), 1)[0])
    ok = [abs(z["rel_abw"]) for z in zeilen if z["rel_abw"] is not None]
    return dict(zeilen=zeilen, steigung_kleinste5=steig, max_rel_abw=float(max(ok)) if ok else None,
                anzahl_mit_2_spruengen=len(ok), T_end=T_end)


def rastung(Delta, K, F, Om, psi, T_ein, T_mess, dt, phi0=0.0):
    """Gibt mittlere Rate <phi'> in der Messzeit und Anzahl Spruenge (Betrag) zurueck."""
    phi = np.full(np.broadcast(Delta, K, F, Om, psi).shape, phi0, float)

    def rate(t, p):
        return Delta - 2 * K * np.sin(p) + F * np.sin((Om - 1) * t + psi - p)

    phi, t = rk4_phase(rate, phi, 0.0, dt, int(T_ein / dt))
    p0 = phi.copy()
    mn = phi.copy(); mx = phi.copy()

    def beob(t, p):
        np.minimum(mn, p, out=mn); np.maximum(mx, p, out=mx)

    phi, t = rk4_phase(rate, phi, t, dt, int(T_mess / dt), beob)
    mittel = (phi - p0) / T_mess
    spanne = mx - mn
    return mittel, spanne


def d2b(rauch):
    K = 0.5; Delta = 1.1
    dt = 0.02
    T_ein, T_mess = (100.0, 400.0) if rauch else (500.0, 2000.0)
    psis = np.linspace(0, 2 * np.pi, 13 if rauch else 72, endpoint=False)
    Fs = np.linspace(0, 0.5, 11 if rauch else 51)
    PS, FF = np.meshgrid(psis, Fs, indexing="ij")
    mittel, spanne = rastung(Delta, K, FF, 1.0, PS, T_ein, T_mess, dt)
    gerastet = spanne < 2 * np.pi  # kein voller Phasensprung in der Messzeit
    R = np.sqrt(4 * K ** 2 + FF ** 2 + 4 * K * FF * np.cos(PS))
    theorie = R > Delta
    rand = np.abs(R - Delta) < 0.01
    uebereinst = float(((gerastet == theorie) | rand).mean())
    uebereinst_ohne_rand = float((gerastet == theorie)[~rand].mean())
    # psi = 0 und psi = pi: kleinstes F, ab dem gerastet
    def fmin(j):
        zz = np.nonzero(gerastet[j])[0]
        return float(Fs[zz.min()]) if zz.size else None
    j0 = 0; jpi = int(np.argmin(np.abs(psis - np.pi)))
    res = dict(K=K, Delta=Delta, uebereinstimmung_mit_zeigerformel=uebereinst,
               uebereinstimmung_ausserhalb_randstreifen=uebereinst_ohne_rand,
               anteil_gerastet=float(gerastet.mean()),
               F_min_rastung_psi0=fmin(j0), F_min_rastung_psipi=fmin(jpi),
               F_theorie_psi0=float(Delta - 2 * K),
               gerastet_psi_pi_irgendein_F=bool(gerastet[jpi].any()))
    # Karte (Omega, F), psi = 0
    Oms = np.linspace(0, 2, 21 if rauch else 101)
    OO, FF2 = np.meshgrid(Oms, Fs, indexing="ij")
    mittel2, spanne2 = rastung(Delta, K, FF2, OO, 0.0, T_ein, T_mess, dt)
    freqC = 1 + mittel2
    an_AB = spanne2 < 2 * np.pi
    am_Takt = (np.abs(freqC - OO) < 2 * np.pi / T_mess) & ~an_AB
    res["omega_karte"] = dict(anteil_an_AB=float(an_AB.mean()), anteil_am_Takt=float(am_Takt.mean()))
    # wo rastet C an A/B bei F > 0 (Omega-Bereich je F)
    zeilen = {}
    for k, Fv in enumerate(Fs):
        if Fv == 0:
            continue
        om = Oms[an_AB[:, k]]
        if om.size:
            zeilen[f"{Fv:.3f}"] = [float(om.min()), float(om.max()), int(om.size)]
    res["omega_bereich_rastung_AB_je_F"] = zeilen
    return res, dict(psis=psis, Fs=Fs, gerastet=gerastet, mittel=mittel, R=R, Oms=Oms, freqC=freqC, an_AB=an_AB,
                     am_Takt=am_Takt)


def d2c(rauch):
    wA, wB, wC, K = 0.8, 1.2, 1.1, 0.15
    dt = 0.02
    T_ein, T_mess = (100.0, 400.0) if rauch else (500.0, 2000.0)
    Oms = np.linspace(0.5, 1.5, 21 if rauch else 101)
    Fs = np.linspace(0, 0.5, 11 if rauch else 51)
    OO, FF = np.meshgrid(Oms, Fs, indexing="ij")

    def rate(t, th):
        return wC + K * (np.sin(wA * t - th) + np.sin(wB * t - th)) + FF * np.sin(OO * t - th)

    def ableitung(t, th):
        return -K * (np.cos(wA * t - th) + np.cos(wB * t - th)) - FF * np.cos(OO * t - th)

    th = np.zeros_like(OO)
    th, t = rk4_phase(rate, th, 0.0, dt, int(T_ein / dt))
    th0 = th.copy()
    lyap = np.zeros_like(OO)
    n = int(T_mess / dt)
    for i in range(n):
        lyap += ableitung(t, th) * dt
        k1 = rate(t, th); k2 = rate(t + 0.5 * dt, th + 0.5 * dt * k1); k3 = rate(t + 0.5 * dt, th + 0.5 * dt * k2)
        k4 = rate(t + dt, th + dt * k3)
        th = th + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4); t += dt
    lyap /= T_mess
    freq = (th - th0) / T_mess
    tolf = 2 * np.pi / T_mess
    klasse = np.full(OO.shape, "sonst", dtype=object)
    klasse[np.abs(freq - OO) < tolf] = "Takt"
    klasse[np.abs(freq - wA) < tolf] = "A"
    klasse[np.abs(freq - wB) < tolf] = "B"
    klasse[np.abs(freq - 0.5 * (wA + wB)) < tolf] = "Mitte"
    res = dict(wA=wA, wB=wB, wC=wC, K=K,
               F0_freq=float(freq[:, 0].mean()), F0_lyap=float(lyap[:, 0].mean()),
               anteil_lyap_neg=float((lyap < -0.005).mean()))
    # je Omega: kleinstes F mit lyap < -0.005 (C eingefangen)
    fmin = []
    for i, Om in enumerate(Oms):
        zz = np.nonzero(lyap[i] < -0.005)[0]
        fmin.append([float(Om), float(Fs[zz.min()]) if zz.size else None])
    res["F_min_eingefangen_je_Omega"] = fmin
    for kl in ("Takt", "A", "B", "Mitte", "sonst"):
        res[f"anteil_klasse_{kl}"] = float((klasse == kl).mean())
    return res, dict(Oms=Oms, Fs=Fs, lyap=lyap, freq=freq)


def main():
    aus = sys.argv[1]
    teile = sys.argv[2]
    rauch = len(sys.argv) > 3 and sys.argv[3] == "rauch"
    os.makedirs(aus, exist_ok=True)
    res = dict(teile=teile, sek={})
    tag = ("rauch_" if rauch else "voll_") + teile
    if "a" in teile:
        t0 = time.time(); res["d2a"] = d2a(rauch); res["sek"]["a"] = time.time() - t0
    if "b" in teile:
        t0 = time.time(); rb, fb = d2b(rauch); res["d2b"] = rb; res["sek"]["b"] = time.time() - t0
        np.savez_compressed(os.path.join(aus, f"d2_{tag}_b.npz"), b_psis=fb["psis"], b_Fs=fb["Fs"], b_gerastet=fb["gerastet"],
                            b_R=fb["R"], b_Oms=fb["Oms"], b_freqC=fb["freqC"], b_an_AB=fb["an_AB"], b_am_Takt=fb["am_Takt"])
    if "c" in teile:
        t0 = time.time(); rc, fc = d2c(rauch); res["d2c"] = rc; res["sek"]["c"] = time.time() - t0
        np.savez_compressed(os.path.join(aus, f"d2_{tag}_c.npz"), c_Oms=fc["Oms"], c_Fs=fc["Fs"], c_lyap=fc["lyap"], c_freq=fc["freq"])
    with open(os.path.join(aus, f"d2_{tag}.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    kurz = dict(res)
    if "d2a" in res:
        kurz["d2a"] = {k: v for k, v in res["d2a"].items() if k != "zeilen"}
    print(json.dumps(kurz, indent=1)[:5000])


if __name__ == "__main__":
    main()
