# AETHER-UHR-1 (Runde 36): mechanische Auswertung nach PLAN.md.
# Aufruf (nur ueber kleintest.sh): auswertung.py <lauf-ordner> <ausgabe.json>
# Laeufe im Ordner: H-100, H-115, H-170 (Haupt), A-* (Adiabatik-Probe, halbe Beschleunigung), G-* (Gitterprobe, h/2),
#   R0 (b = 0, nur Ruhephase; Rueckwirkungsprobe). Fehlende Laeufe werden vermerkt.
import sys, os, json, math, hashlib
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import minimize_scalar

T_EIN = 20.0           # Einschwingzeit am Anfang jeder Ruhe-/Plateauphase (nicht ausgewertet)
CB = [(1.0, "100"), (1.15, "115"), (1.7, "170")]
V_NOM = [0.2, 0.4, 0.6]
S_U0_R = 1e-3          # U0: |R(v)/R(0) - 1| <= 1e-3
S_L = 0.01             # U0/U3: |L(v) gamma_A/L(0) - 1| <= 1 %
S_U12 = 0.20           # U1/U2: |(R/R0 - 1) - v^2 (1 - 1/c_B^2)| <= 20 % des Sollwerts
V_TOL = 0.02           # [F] erreichte Schnelle |v - v_nom| <= 0,02, sonst nicht auswertbar
S_K1 = 1e-3            # [F] Kontrolle Uhrwahl (c_B = 1): omega_A gamma_A/omega_A(0) und Omega_B gamma_B/Omega_B(0) auf 1e-3
S_K2 = 1e-3            # Rueckwirkung: max|S_b - S_0|/max S_0 < 1e-3 (Karte/Auftrag)
Z_REL, Z_ABS = 0.05, 2e-4   # [F] Zusatz Z-K (kein Kartenurteil): Abweichung von der exakten Kinematik


def lam0(S, h, c, mB, g):
    d = 2.0 * c * c / (h * h) + mB * mB - g * S
    e = np.full(len(S) - 1, -c * c / (h * h))
    return float(eigh_tridiagonal(d, e, select="i", select_range=(0, 0), eigvals_only=True)[0])


def kin_anteil(S, h, c, mB, g):
    """f = c^2 <-Lap> / lambda fuer die unterste Mode (Anteil der Gradientenenergie)."""
    d = 2.0 * c * c / (h * h) + mB * mB - g * S
    e = np.full(len(S) - 1, -c * c / (h * h))
    w, v = eigh_tridiagonal(d, e, select="i", select_range=(0, 0))
    f = v[:, 0]
    lap = (np.concatenate([f[1:], [0.0]]) + np.concatenate([[0.0], f[:-1]]) - 2.0 * f) / (h * h)
    return float(-c * c * np.dot(f, lap) / np.dot(f, f) / w[0])


def sinus_fit(tt, s):
    """Frequenz einer Sinusschwingung: FFT-Startwert, dann Variablenprojektion (cos, sin, 1)."""
    t0 = tt - tt[0]
    n = len(s)
    dts = t0[1] - t0[0]
    nfft = 1 << (int(math.ceil(math.log2(n))) + 4)
    F = np.abs(np.fft.rfft((s - s.mean()) * np.hanning(n), nfft))
    fr = np.fft.rfftfreq(nfft, dts) * 2.0 * math.pi
    k = int(np.argmax(F[1:])) + 1
    Om0 = float(fr[k])

    def rest(Om):
        A = np.column_stack([np.cos(Om * t0), np.sin(Om * t0), np.ones_like(t0)])
        c, *_ = np.linalg.lstsq(A, s, rcond=None)
        r = s - A @ c
        return float(r @ r), c

    dOm = 2.0 * math.pi / t0[-1]
    res = minimize_scalar(lambda Om: rest(Om)[0], bounds=(Om0 - 0.5 * dOm, Om0 + 0.5 * dOm), method="bounded",
                          options=dict(xatol=1e-13, maxiter=500))
    Om = float(res.x)
    r2, c = rest(Om)
    amp = float(math.hypot(c[0], c[1]))
    return Om, amp, float(math.sqrt(r2 / n) / amp) if amp > 0 else float("nan"), Om0


def plateaus(kopf, z):
    t = z["t"]
    out = []
    for typ, t0, t1, k in kopf["segmente"]:
        if typ not in ("ruhe", "plateau"):
            continue
        if t[-1] < t1 - 1e-9:
            break
        sel = (t >= t0 + T_EIN - 1e-9) & (t <= t1 + 1e-9)
        tt = t[sel]
        X = z["X"][sel]
        pv = np.polyfit(tt, X, 1)
        v = float(pv[0])
        th = np.unwrap(z["thc"][sel])
        pa = np.polyfit(tt, th, 1)
        omA = float(pa[0])
        omA_res = float(np.sqrt(np.mean((th - np.polyval(pa, tt)) ** 2)))
        if np.any(z["sB"][sel] != 0.0):
            OmB, ampB, resB, Om0B = sinus_fit(tt, z["sB"][sel])
            OmBc, ampBc, resBc, _ = sinus_fit(tt, z["Bc"][sel])
        else:
            OmB = ampB = resB = Om0B = OmBc = ampBc = resBc = float("nan")
        out.append(dict(k=int(k), typ=typ, t0=float(tt[0]), t1=float(tt[-1]), n=int(len(tt)), v=v,
                        X_res=float(np.sqrt(np.mean((X - np.polyval(pv, tt)) ** 2))),
                        LR=float(np.mean(z["LR"][sel])), LR_std=float(np.std(z["LR"][sel])),
                        LS=float(np.mean(z["LS"][sel])), LS_std=float(np.std(z["LS"][sel])),
                        omA=omA, omA_res=omA_res, OmB=OmB, OmB_amp=ampB, OmB_res=resB, OmB_fft=Om0B,
                        OmBc=OmBc, OmBc_res=resBc, Q_mittel=float(np.mean(z["Q"][sel]))))
    return out


def lauf_auswerten(kopf, z):
    cB = kopf["c_B"]; h = kopf["h"]; mB = kopf["m_B"]; g = kopf["g"]
    S0 = z["S_init"]
    pl = plateaus(kopf, z)
    e = dict(name=kopf["name"], c_B=cB, h=h, dt=kopf["dt"], T_r=kopf["T_r"], T_p=kopf["T_p"], b=kopf["b"],
             status=kopf["status"], t_letzt=kopf["t_letzt"], plateaus=pl)
    lam_r = lam0(S0, h, cB, mB, g)
    e["lambda_ruhe"] = lam_r
    e["f_kin"] = kin_anteil(S0, h, cB, mB, g)
    if len(pl) == 0:
        e["ok"] = False
        return e
    p0 = pl[0]
    R0 = p0["OmB"] / p0["omA"]
    e["R0"] = R0
    for p in pl:
        v = p["v"]
        gA = 1.0 / math.sqrt(1.0 - v * v)
        gB = 1.0 / math.sqrt(1.0 - v * v / (cB * cB))
        p["gamma_A"] = gA; p["gamma_B"] = gB
        p["R"] = p["OmB"] / p["omA"]
        p["R_rel"] = p["R"] / R0 - 1.0
        p["Rc_rel"] = (p["OmBc"] / p["omA"]) / (p0["OmBc"] / p0["omA"]) - 1.0
        p["L_rel"] = p["LR"] * gA / p0["LR"] - 1.0
        p["L_rel_S"] = p["LS"] * gA / p0["LS"] - 1.0
        p["L_rel_gB"] = p["LR"] * gB / p0["LR"] - 1.0
        p["omA_dil"] = p["omA"] * gA / p0["omA"] - 1.0
        p["OmB_dil_B"] = p["OmB"] * gB / p0["OmB"] - 1.0
        p["soll_karte"] = v * v * (1.0 - 1.0 / (cB * cB))
        p["soll_kin"] = (gA / gB) * math.sqrt(lam0(S0, h, cB * gA / gB, mB, g) / lam_r) - 1.0
        p["soll_hart"] = (gA / gB) ** 2 - 1.0
        p["abw_karte"] = (p["R_rel"] - p["soll_karte"]) / p["soll_karte"] if p["soll_karte"] != 0 else float("nan")
        p["abw_kin"] = p["R_rel"] - p["soll_kin"]
    e["ok"] = bool(kopf["status"] == "fertig" and len(pl) == 4
                   and all(np.isfinite([p["R_rel"], p["L_rel"], p["v"]]).all() for p in pl)
                   and all(abs(pl[i]["v"] - V_NOM[i - 1]) <= V_TOL for i in range(1, 4)) and abs(pl[0]["v"]) <= 1e-3)
    return e


def urteile_satz(ev):
    """ev: dict cB-Kennung -> Auswertung (oder None). Urteile U0..U3 nach der Karte."""
    u = {}

    def da(x):
        return x is not None and x.get("ok", False)

    e = ev.get("100")
    if not da(e):
        u["U0"] = ("nicht auswertbar", "Lauf c_B = 1 fehlt oder unvollstaendig")
    else:
        bad = [p for p in e["plateaus"][1:] if abs(p["R_rel"]) > S_U0_R or abs(p["L_rel"]) > S_L]
        u["U0"] = ("nicht eingetroffen" if bad else "eingetroffen", "")
    for nr, kenn in (("U1", "115"), ("U2", "170")):
        e = ev.get(kenn)
        if not da(e):
            u[nr] = ("nicht auswertbar", "Lauf fehlt oder unvollstaendig")
        else:
            bad = [p for p in e["plateaus"][1:] if abs(p["abw_karte"]) > S_U12]
            u[nr] = ("nicht eingetroffen" if bad else "eingetroffen", "")
    if not all(da(ev.get(k)) for _, k in CB):
        u["U3"] = ("nicht auswertbar", "mindestens ein Lauf fehlt oder unvollstaendig")
    else:
        bad = [p for _, k in CB for p in ev[k]["plateaus"][1:] if abs(p["L_rel"]) > S_L]
        u["U3"] = ("nicht eingetroffen" if bad else "eingetroffen", "")
    # fehlt: ein benoetigter Lauf wurde gar nicht gerechnet (keine Dateien)
    noetig = {"U0": ["100"], "U1": ["115"], "U2": ["170"], "U3": ["100", "115", "170"]}
    return {nr: (u[nr][0], u[nr][1], any(ev.get(k) is None for k in noetig[nr])) for nr in u}


def lade(ordner, name):
    j = os.path.join(ordner, name + ".json"); n = os.path.join(ordner, name + ".npz")
    if not (os.path.exists(j) and os.path.exists(n)):
        return None, None
    return json.load(open(j)), np.load(n)


def main():
    ordner = sys.argv[1]; aus = sys.argv[2]
    saetze = {}
    roh = {}
    for satz in ("H", "A", "G"):
        ev = {}
        for cB, kenn in CB:
            kopf, z = lade(ordner, "%s-%s" % (satz, kenn))
            if kopf is None:
                ev[kenn] = None
                continue
            ev[kenn] = lauf_auswerten(kopf, z)
            roh["%s-%s" % (satz, kenn)] = (kopf, z)
        saetze[satz] = ev
    # Bilanzen
    bilanzen = {}
    for nm, (kopf, z) in roh.items():
        H = z["H"]; Q = z["Q"]
        bE = H + z["Eabs"] + z["Edrop"] - H[0] - z["W"]
        bQ = Q + z["Qabs"] + z["Qdrop"] - Q[0]
        bilanzen[nm] = dict(E_rel_max=float(np.max(np.abs(bE)) / kopf["M0"]), Q_rel_max=float(np.max(np.abs(bQ)) / kopf["Q0"]),
                            W_ende=float(z["W"][-1]), Eabs_ende=float(z["Eabs"][-1]), Qabs_ende=float(z["Qabs"][-1]),
                            Edrop_ende=float(z["Edrop"][-1]), Qdrop_ende=float(z["Qdrop"][-1]),
                            skript_sha256=kopf["skript_sha256"], status=kopf["status"], wandzeit_s=kopf["wandzeit_s"],
                            abschnitte=kopf["abschnitte"])
    # Rueckwirkung (K2): Ruhephase mit b gegen b = 0 (R0), gleiche Gitterwerte
    k2 = {}
    kopf0, z0 = lade(ordner, "R0")
    if kopf0 is not None and "prof_S_0" in z0.files:
        S_ref = z0["prof_S_0"]
        pl0 = plateaus(kopf0, z0)
        for cB, kenn in CB:
            if ("H-" + kenn) not in roh:
                continue
            kopf, z = roh["H-" + kenn]
            if "prof_S_0" not in z.files or kopf["h"] != kopf0["h"] or kopf["dt"] != kopf0["dt"]:
                continue
            dS = float(np.max(np.abs(z["prof_S_0"] - S_ref)) / np.max(S_ref))
            p = saetze["H"][kenn]["plateaus"][0]
            k2[kenn] = dict(verformung=dS, dL_rel=p["LR"] / pl0[0]["LR"] - 1.0, domA_rel=p["omA"] / pl0[0]["omA"] - 1.0,
                            erfuellt=bool(dS < S_K2))
    k2_ok = len(k2) == 3 and all(v["erfuellt"] for v in k2.values())
    # Urteile
    uH = urteile_satz(saetze["H"])
    uA = urteile_satz(saetze["A"])
    uG = urteile_satz(saetze["G"])
    urteile = {}
    for nr in ("U0", "U1", "U2", "U3"):
        ur, verm, _ = uH[nr]
        vermerke = [verm] if verm else []
        if ur != "nicht auswertbar":
            for pn, up in (("Adiabatik-Probe", uA), ("Gitterprobe", uG)):
                if up[nr][0] == "nicht auswertbar" and up[nr][2]:
                    # Probe nicht gerechnet: Haupturteil bleibt, mit Vermerk
                    vermerke.append("%s nicht gerechnet (%s)" % (pn, up[nr][1]))
                elif up[nr][0] != ur:
                    vermerke.append("%s gibt '%s'%s" % (pn, up[nr][0], (" (%s)" % up[nr][1]) if up[nr][1] else ""))
                    ur = "nicht auswertbar"
            if not k2_ok:
                vermerke.append("Rueckwirkungsprobe K2 nicht erfuellt oder fehlt")
                ur = "nicht auswertbar"
        werte = {}
        for satz in ("H", "A", "G"):
            for cB, kenn in CB:
                e = saetze[satz].get(kenn)
                if e is None or "R0" not in e:
                    continue
                if nr in ("U1", "U2") and kenn != {"U1": "115", "U2": "170"}[nr]:
                    continue
                if nr == "U0" and kenn != "100":
                    continue
                werte["%s-%s" % (satz, kenn)] = [dict(v=p["v"], R_rel=p["R_rel"], L_rel=p["L_rel"],
                                                      soll_karte=p["soll_karte"], abw_karte=p["abw_karte"],
                                                      soll_kin=p["soll_kin"]) for p in e["plateaus"][1:]]
        urteile[nr] = dict(urteil=ur, werte=werte, saetze=dict(H=uH[nr][0], A=uA[nr][0], G=uG[nr][0]))
        if vermerke:
            urteile[nr]["vermerk"] = "; ".join(vermerke)
    # Kontrolle K1 (Uhrwahl, c_B = 1) und Zusatz Z-K (exakte Kinematik, c_B != 1)
    kontrollen = {}
    for satz in ("H", "A", "G"):
        e = saetze[satz].get("100")
        if e is not None and e.get("ok"):
            m = max(max(abs(p["omA_dil"]), abs(p["OmB_dil_B"])) for p in e["plateaus"][1:])
            kontrollen["K1-" + satz] = dict(max_abw=m, erfuellt=bool(m <= S_K1))
        for cB, kenn in CB[1:]:
            e = saetze[satz].get(kenn)
            if e is None or not e.get("ok"):
                continue
            ok = all(abs(p["abw_kin"]) <= Z_REL * abs(p["soll_kin"]) + Z_ABS for p in e["plateaus"][1:])
            kontrollen["Z-K-%s-%s" % (satz, kenn)] = dict(
                abw=[p["abw_kin"] for p in e["plateaus"][1:]], soll_kin=[p["soll_kin"] for p in e["plateaus"][1:]],
                erfuellt=bool(ok))
    # Sollkurven fuer Bilder (aus dem Ruheprofil des Hauptlaufs)
    kurven = {}
    vg = np.linspace(0.0, 0.65, 66)
    for cB, kenn in CB:
        if ("H-" + kenn) not in roh:
            continue
        kopf, z = roh["H-" + kenn]
        S0 = z["S_init"]; lr = lam0(S0, kopf["h"], cB, kopf["m_B"], kopf["g"])
        kin = []
        for v in vg:
            gA = 1.0 / math.sqrt(1.0 - v * v); gB = 1.0 / math.sqrt(1.0 - v * v / (cB * cB))
            kin.append((gA / gB) * math.sqrt(lam0(S0, kopf["h"], cB * gA / gB, kopf["m_B"], kopf["g"]) / lr) - 1.0)
        kurven[kenn] = dict(v=vg.tolist(), karte=(vg ** 2 * (1.0 - 1.0 / cB ** 2)).tolist(), kin=kin,
                            hart=((1.0 - vg ** 2 / cB ** 2) / (1.0 - vg ** 2) - 1.0).tolist())
    out = dict(urteile=urteile, kontrollen=kontrollen, rueckwirkung_K2=k2, K2_erfuellt=k2_ok, bilanzen=bilanzen,
               saetze=saetze, kurven=kurven,
               auswertung_sha256=hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest())
    json.dump(out, open(aus, "w"), indent=1, default=float)
    kurz = {nr: (urteile[nr]["urteil"], urteile[nr].get("vermerk", "")) for nr in urteile}
    print(json.dumps(dict(urteile=kurz, K2=k2_ok, kontrollen={k: v["erfuellt"] for k, v in kontrollen.items()}),
                     indent=1), flush=True)
    for satz in ("H", "A", "G"):
        for cB, kenn in CB:
            e = saetze[satz].get(kenn)
            if e is None or "R0" not in e:
                continue
            for p in e["plateaus"]:
                print("%s-%s k=%d v=%.5f R_rel=%+.6f karte=%.6f kin=%.6f L_rel=%+.2e omA_dil=%+.2e OmB=%.6f omA=%.6f "
                      "resB=%.1e" % (satz, kenn, p["k"], p["v"], p.get("R_rel", 0), p.get("soll_karte", 0),
                                     p.get("soll_kin", 0), p.get("L_rel", 0), p.get("omA_dil", 0), p["OmB"], p["omA"],
                                     p["OmB_res"]), flush=True)


if __name__ == "__main__":
    main()
