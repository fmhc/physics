# NETZ-C-1 (Runde 35): mechanische Auswertung nach PLAN.md (eingefroren). Aufruf: auswertung.py <laufordner> <ausgabe.json>
import sys, os, json
import numpy as np

LAUF = sys.argv[1]; AUS = sys.argv[2]
ETA = 0.01
QS = [0.3, 1.0, 3.0, 10.0]
FK4 = 0.02
HK4 = [0.5, 0.25, 0.125]
W_FENSTER = 20.0          # Fensterlaenge fuer Schnelle und gamma-Mittel
SPAET = (800.0, 1000.0)   # spaetes Fenster fuer Endgeschwindigkeit und gamma (Teil B (1))
KA, KB = "0.001", "0.002"


def vsoll(q):
    return q / np.sqrt(1 + q * q)


def lade(name):
    p = os.path.join(LAUF, name)
    if not os.path.exists(p + ".npz"):
        return None, None
    z = np.load(p + ".npz")
    return {f: z[f] for f in z.files}, json.load(open(p + ".json"))


def zerstoerung(r):
    t = r["t"]; X = r["X"]
    dX = np.concatenate([[0.0], np.abs(np.diff(X))])
    bad = (r["ncross"] != 1) | (~np.isfinite(X)) | (dX > 2.0) | (r["Ewin"] < 4.0)
    if np.any(bad):
        i = int(np.argmax(bad))
        grund = [nm for nm, b in (("ncross", r["ncross"][i] != 1), ("X_nan", not np.isfinite(X[i])),
                                  ("sprung", dX[i] > 2.0), ("Ewin<4", r["Ewin"][i] < 4.0)) if b]
        return float(t[i]), i, grund
    return None, len(t), []


def fenster_schnelle(t, X, iend, W=W_FENSTER):
    ds = t[1] - t[0]
    m = int(round(W / ds)) + 1
    vs = []
    for i0 in range(0, iend - m + 1):
        tt = t[i0:i0 + m]; xx = X[i0:i0 + m]
        if not np.all(np.isfinite(xx)):
            continue
        vs.append(np.polyfit(tt, xx, 1)[0])
    return np.array(vs)


def gleitend(y, m):
    k = np.ones(m) / m
    out = np.full(len(y), np.nan)
    if len(y) >= m:
        c = np.convolve(y, k, mode="valid")
        h = m // 2
        out[h:h + len(c)] = c
    return out


def spaet(r, a=SPAET[0], b=SPAET[1]):
    t = r["t"]
    m = (t >= a - 1e-9) & (t <= b + 1e-9)
    return m


def lauf_b1(name):
    r, k = lade(name)
    if r is None:
        return None
    tZ, iZ, grund = zerstoerung(r)
    m = spaet(r)
    erg = dict(status=k["status"], t_letzt=k["t_letzt"], zerstoerung_t=tZ, zerstoerung_grund=grund,
               dt=k["dt"], F=k["F"], h=k["h"])
    ok = m & np.isfinite(r["X"])
    if ok.sum() >= 10 and (tZ is None or tZ > SPAET[1]):
        erg["v_end"] = float(np.polyfit(r["t"][ok], r["X"][ok], 1)[0])
        okc = m & np.isfinite(r["Xcm"])
        erg["v_end_cm"] = float(np.polyfit(r["t"][okc], r["Xcm"][okc], 1)[0])
        erg["gamma_steigung_parabel"] = float(np.nanmean(r["gsp"][m]))
        erg["gamma_steigung_roh"] = float(np.nanmean(r["gs"][m]))
        erg["gamma_energie"] = float(np.nanmean(r["gE"][m]))
        erg["E_ausserhalb_spaet"] = float(np.nanmean(r["E0"][m] - r["Ewin"][m]))
    else:
        erg["v_end"] = None
    vs = fenster_schnelle(r["t"], r["X"], iZ)
    vc = fenster_schnelle(r["t"], r["Xcm"], iZ)
    erg["max_fensterschnelle"] = float(vs.max()) if len(vs) else None
    erg["max_fensterschnelle_cm"] = float(vc.max()) if len(vc) else None
    dX = np.diff(r["X"][:iZ]) / np.diff(r["t"][:iZ])
    erg["max_zweipunkt_schnelle"] = float(np.nanmax(dX)) if len(dX) else None
    erg["H_drift_rel"] = float(np.max(np.abs(r["H"] - r["H"][0])) / abs(r["H"][0]))
    return erg


def lauf_k4(name, F=FK4):
    r, k = lade(name)
    if r is None:
        return None
    t = r["t"]
    tZ, iZ, grund = zerstoerung(r)
    ds = t[1] - t[0]
    mfen = int(round(W_FENSTER / ds)) + 1
    gE = gleitend(r["gE"], mfen); gS = gleitend(r["gsp"], mfen)
    vor = np.arange(len(t)) < iZ
    gEv = np.where(vor, gE, np.nan); gSv = np.where(vor, gS, np.nan)
    imax = int(np.nanargmax(gEv))
    t_stop = tZ if tZ is not None else float(t[-1])
    m = vor & (t >= 0.75 * t_stop) & np.isfinite(gE)
    steig = float(np.polyfit(t[m], gE[m], 1)[0]) if m.sum() > 5 else None
    rate_kont = np.pi * F / 4
    gesaettigt = steig is not None and steig < 0.25 * rate_kont
    grenze = (tZ is not None and tZ < k["t_end"]) or gesaettigt
    gk = lambda tt: float(np.sqrt(1 + (np.pi * F * tt / 4) ** 2))
    stichproben = {}
    for tt in (100, 200, 400, 800, 1600, 3200):
        if tt <= t[-1]:
            i = int(np.argmin(np.abs(t - tt)))
            stichproben[str(tt)] = dict(gE=float(gE[i]) if np.isfinite(gE[i]) else None,
                                        gS=float(gS[i]) if np.isfinite(gS[i]) else None,
                                        g_kontinuum=gk(tt), X=float(r["X"][i]) if np.isfinite(r["X"][i]) else None,
                                        E_ausserhalb=float(r["E0"][i] - r["Ewin"][i]), E0=float(r["E0"][i]))
    vs = fenster_schnelle(t, r["X"], iZ)
    return dict(h=k["h"], dt=k["dt"], status=k["status"], t_end=k["t_end"], t_letzt=k["t_letzt"],
                zerstoerung_t=tZ, zerstoerung_grund=grund,
                gamma_max_energie=float(gEv[imax]), t_gamma_max=float(t[imax]),
                gamma_max_energie_mal_h=float(gEv[imax] * k["h"]),
                gamma_max_steigung=float(np.nanmax(gSv)), gamma_max_steigung_mal_h=float(np.nanmax(gSv) * k["h"]),
                deckel_steigung_pi_durch_h=float(np.pi / k["h"]),
                steigung_gE_letztes_viertel=steig, rate_kontinuum=rate_kont, gesaettigt=bool(gesaettigt),
                grenze=bool(grenze), stichproben=stichproben,
                E_ausserhalb_ende=float(r["E0"][iZ - 1] - r["Ewin"][iZ - 1]), E0_ende=float(r["E0"][iZ - 1]),
                max_fensterschnelle=float(vs.max()) if len(vs) else None,
                H_drift_rel=float(np.max(np.abs(r["H"] - r["H"][0])) / abs(r["H"][0])))


def urteil_k4(L):
    """L: dict h -> lauf_k4-Ergebnis."""
    if any(L[h] is None for h in HK4):
        return "nicht auswertbar", "Lauf fehlt"
    gm = {h: L[h]["gamma_max_energie"] for h in HK4}
    gr = {h: L[h]["grenze"] for h in HK4}
    a = all(gr.values())
    b = gm[0.125] > gm[0.25] > gm[0.5]
    c = all(0.3 <= gm[h] * h <= 5 for h in HK4)
    if a:
        return ("eingetroffen" if (b and c) else "nicht eingetroffen"), None
    # nicht alle h mit Grenze: endgueltig nur, wenn ein Verstoss nicht mehr heilbar ist
    lim = [h for h in HK4 if gr[h]]
    verstoss = any(gm[h] * h > 5 for h in HK4) or any(gm[h] * h < 0.3 for h in lim)
    for i in range(len(HK4)):
        for j in range(i + 1, len(HK4)):
            hi, hj = HK4[i], HK4[j]          # hi > hj
            if hi in lim and hj in lim and not gm[hj] > gm[hi]:
                verstoss = True
    if verstoss:
        return "nicht eingetroffen", "nicht alle h mit Grenze, Verstoss aber endgueltig"
    return "nicht auswertbar", "nicht alle h erreichen bis Laufende eine Grenze"


def vg_max(h):
    k = np.linspace(1e-6, np.pi / h, 1000001)
    w = np.sqrt(1 + 4 * np.sin(k * h / 2) ** 2 / h ** 2)
    return float(np.max(np.sin(k * h) / (h * w)))


def teil_a():
    p = os.path.join(LAUF, "netz_a.json")
    if not os.path.exists(p):
        return None
    return json.load(open(p))


def satz(A, net, md, nf, kk):
    return A["netze"][net]["modelle"][md]["saetze"]["nf%d_k%s" % (nf, kk)]


def main():
    U = {}
    W = {}
    A = teil_a()
    # ---------------- Teil A ----------------
    if A is None:
        for p in ("P0", "P1", "P2", "P3"):
            U[p] = dict(urteil="nicht auswertbar", vermerk="Teil A nicht gerechnet", werte={})
    else:
        nf1, nf2 = A["nfibs"][0], A["nfibs"][1]
        c0 = np.sqrt(2.0) / 2
        ref = {"[100]": [1.0, 1.0, np.sqrt(2.0)], "[110]": [1 / np.sqrt(2.0), 1.0, np.sqrt(2.5)],
               "[111]": [np.sqrt(2 / 3.0), np.sqrt(2 / 3.0), np.sqrt(8 / 3.0)]}

        def p0(kk, gi):
            fz = A["netze"]["fcc"]["modelle"]["Z"]
            dev = {}
            for d, rv in ref.items():
                c = np.array(fz["symmetrie"][d][kk]["c"][:3]) / c0
                dev[d] = [float(x) for x in np.abs(c / np.array(rv) - 1)]
            maxdev = max(max(v) for v in dev.values())
            s110 = fz["symmetrie"]["[110]"][kk]
            pol = s110["pol"]
            p_t2 = abs(np.dot(pol[0], np.array([1, -1, 0]) / np.sqrt(2)))
            p_t1 = abs(pol[1][2])
            gen = {}
            gen_ok = True
            for nm in ("fcc", "pyro", "diamant", "srs"):
                g = A["netze"][nm]["modelle"]["Z"]["generisch"]
                soll = max(0, A["netze"][nm]["info"]["maxwell_3n_minus_b"])
                gen[nm] = dict(nullmoden_min_max=g["nullmoden_min_max"], soll=soll)
                gen_ok &= (g["nullmoden_min_max"] == [soll, soll])
            gz = A["netze"]["fcc"]["modelle"]["Z"]["gitter"][gi]
            fcc_gitter_ok = (list(gz["histogramm_nullmoden_k_ungleich_0"].keys()) == ["0"]) and gz["nullmoden_bei_k0"] == 3
            ok = maxdev <= 1e-4 and p_t2 >= 0.99 and p_t1 >= 0.99 and gen_ok and fcc_gitter_ok
            return ok, dict(max_rel_abweichung=maxdev, abweichungen=dev, pol_110_langsam_auf_1m10=float(p_t2),
                            pol_110_mitte_auf_001=float(p_t1), generisch=gen, fcc_gitter_N=gz["N"],
                            fcc_gitter_ok=bool(fcc_gitter_ok))
        ok_h, w_h = p0(KA, 1)
        ok_p, w_p = p0(KB, 0)
        U["P0"] = dict(urteil="eingetroffen" if ok_h else "nicht eingetroffen",
                       vermerk=None if ok_h == ok_p else "nicht konvergiert (|k| = 2e-3 bzw. Gitter 12^3 gibt anderes Urteil)",
                       werte=dict(haupt=w_h, probe=w_p))
        # P1
        def p1(nf, kk, verf=False):
            werte = {}; ok = True; menge = 0
            for nm in ("fcc", "pyro", "diamant", "srs"):
                for md in ("Z", "W1"):
                    s = satz(A, nm, md, nf, kk)
                    if not s["steif"]:
                        werte["%s-%s" % (nm, md)] = dict(steif=False)
                        continue
                    menge += 1
                    r = s["min_ratio_groesste_durch_kleinste"]
                    if verf:
                        v = A["netze"][nm]["modelle"][md].get("verfeinerung")
                        r = min(r, v["min_ratio"]) if v else r
                    werte["%s-%s" % (nm, md)] = dict(steif=True, min_ratio=r, richtung=s["richtung_min_ratio"])
                    ok &= r >= 1.15
            return (ok and menge > 0), werte
        o1, w1 = p1(nf1, KA)
        probes = [p1(nf2, KA), p1(nf1, KB), p1(nf2, KA, verf=True)]
        verm = None if all(o == o1 for o, _ in probes) else "nicht konvergiert (Probe gibt anderes Urteil)"
        w2 = {}
        for nm in ("fcc", "pyro", "diamant", "srs"):
            s = satz(A, nm, "W2", nf1, KA)
            w2["%s-W2" % nm] = dict(steif=s["steif"], min_ratio=s["min_ratio_groesste_durch_kleinste"])
        U["P1"] = dict(urteil="eingetroffen" if o1 else "nicht eingetroffen", vermerk=verm,
                       werte=dict(haupt=w1, probe_nf=probes[0][1], probe_k=probes[1][1], probe_verfeinert=probes[2][1],
                                  variante_W2=w2))
        # P2
        def p2(nf, kk):
            s = satz(A, "pyro", "Z", nf, kk)
            return s["richtungen_mit_nullast"] > 0, dict(richtungen_mit_nullast=s["richtungen_mit_nullast"],
                                                        nullaeste_je_symmetrierichtung=s["zahl_nullaeste_je_symmetrierichtung"])
        o2, w2a = p2(nf1, KA)
        pr2 = [p2(nf2, KA), p2(nf1, KB)]
        sym = A["netze"]["pyro"]["modelle"]["Z"]["symmetrie"]
        tau = {d: [sym[d][KA]["tau"][i] for i in range(3) if sym[d][KA]["c"][i] < A["cnull"]] for d in sym}
        U["P2"] = dict(urteil="eingetroffen" if o2 else "nicht eingetroffen",
                       vermerk=None if all(o == o2 for o, _ in pr2) else "nicht konvergiert (Probe gibt anderes Urteil)",
                       werte=dict(haupt=w2a, probe_nf=pr2[0][1], probe_k=pr2[1][1],
                                  translationsanteil_der_nullaeste=tau))
        # P3
        def p3(nf, kk, md="W1", verf=False):
            werte = {}; ok = True
            for nm in ("fcc", "pyro", "diamant", "srs"):
                s = satz(A, nm, md, nf, kk)
                e = dict(steif=s["steif"])
                ok &= s["steif"]
                for b in range(2):
                    v = s["aeste"][b]["max_durch_min_minus_1"]
                    if verf and A["netze"][nm]["modelle"][md].get("verfeinerung"):
                        vv = A["netze"][nm]["modelle"][md]["verfeinerung"]["ast%d" % b]
                        v = max(v, vv["max_durch_min_minus_1"])
                    e["querast%d_schwankung" % (b + 1)] = v
                    ok &= v >= 0.10
                werte[nm] = e
            return ok, werte
        o3, w3 = p3(nf1, KA)
        pr3 = [p3(nf2, KA), p3(nf1, KB), p3(nf2, KA, verf=True)]
        ow2, ww2 = p3(nf1, KA, md="W2")
        verm = []
        if not all(o == o3 for o, _ in pr3):
            verm.append("nicht konvergiert (Probe gibt anderes Urteil)")
        if ow2 != o3:
            verm.append("Variante W2 gibt anderes Urteil (%s)" % ("eingetroffen" if ow2 else "nicht eingetroffen"))
        U["P3"] = dict(urteil="eingetroffen" if o3 else "nicht eingetroffen", vermerk="; ".join(verm) if verm else None,
                       werte=dict(haupt=w3, probe_nf=pr3[0][1], probe_k=pr3[1][1], probe_verfeinert=pr3[2][1],
                                  variante_W2=ww2))
    # ---------------- Teil B ----------------
    vg = {str(h): vg_max(h) for h in (0.1, 1.0, 0.5, 0.25, 0.125)}
    W["vg_max"] = vg
    for tl in (1, 2):
        k0 = {}
        for hh in ("0.1", "1"):
            e = lauf_b1("k0_h%s_dt%d" % (hh, tl))
            k0[hh] = e
        W["k0_dt%d" % tl] = k0
        b1 = {}
        for hh in ("0.1", "1"):
            for q in QS:
                b1["h%s_q%s" % (hh, q)] = lauf_b1("r_h%s_q%s_dt%d" % (hh, q, tl))
        W["b1_dt%d" % tl] = b1
        k4 = {h: lauf_k4("f_h%s_dt%d" % (h, tl)) for h in HK4}
        W["k4_dt%d" % tl] = {str(h): v for h, v in k4.items()}

    def uk0(tl):
        k0 = W["k0_dt%d" % tl]
        if any(v is None for v in k0.values()):
            return None, {}
        drift = {hh: v["H_drift_rel"] for hh, v in k0.items()}
        ok = all(d <= 1e-6 for d in drift.values()) and all(v < 1 for v in vg.values())
        return ok, dict(H_drift_rel=drift, vg_max=vg)

    def uk1(tl):
        b1 = W["b1_dt%d" % tl]
        werte = {}; ok = True
        for q in QS:
            e = b1.get("h0.1_q%s" % q)
            if e is None:
                return None, {}
            vs = vsoll(q)
            if e["v_end"] is None:
                werte[str(q)] = dict(v_end=None, v_soll=vs, zerstoerung_t=e["zerstoerung_t"]); ok = False; continue
            rel = abs(e["v_end"] - vs) / vs
            werte[str(q)] = dict(v_end=e["v_end"], v_soll=vs, rel=rel)
            ok &= rel <= 0.02
        return ok, werte

    def uk2(tl):
        b1 = W["b1_dt%d" % tl]
        werte = {}; ok = True
        for q in QS[:3]:
            e = b1.get("h0.1_q%s" % q)
            if e is None:
                return None, {}
            if e["v_end"] is None:
                werte[str(q)] = dict(gamma=None); ok = False; continue
            gv = 1 / np.sqrt(1 - e["v_end"] ** 2)
            rel = abs(e["gamma_steigung_parabel"] / gv - 1)
            werte[str(q)] = dict(gamma_steigung=e["gamma_steigung_parabel"], gamma_aus_v=gv, rel=rel,
                                 gamma_energie=e["gamma_energie"], rel_energie=abs(e["gamma_energie"] / gv - 1))
            ok &= rel <= 0.03
        return ok, werte

    def uk3(tl):
        werte = {}; ok = True; n = 0
        for grp in ("k0_dt%d" % tl, "b1_dt%d" % tl, "k4_dt%d" % tl):
            for key, e in W[grp].items():
                if e is None:
                    continue
                n += 1
                v = e["max_fensterschnelle"]
                werte["%s/%s" % (grp, key)] = v
                if v is not None:
                    ok &= v <= 1.001
        return (ok if n > 0 else None), werte

    def uk4(tl):
        L = {h: W["k4_dt%d" % tl][str(h)] for h in HK4}
        u, v = urteil_k4(L)
        return u, v

    def uk5(tl):
        e = W["b1_dt%d" % tl].get("h1_q10.0")
        if e is None:
            return None, {}
        if e["v_end"] is None:
            return "na", dict(zerstoerung_t=e["zerstoerung_t"])
        grenze = 0.9 * vsoll(10.0)
        return e["v_end"] <= grenze, dict(v_end=e["v_end"], v_kontinuum=vsoll(10.0), grenze_90_prozent=grenze,
                                          rel_unter=(vsoll(10.0) - e["v_end"]) / vsoll(10.0))

    def wort(o):
        if o is None:
            return "nicht auswertbar"
        if o == "na":
            return "nicht auswertbar"
        if isinstance(o, str):
            return o
        return "eingetroffen" if o else "nicht eingetroffen"

    for nm, f in (("K0", uk0), ("K1", uk1), ("K2", uk2), ("K3", uk3), ("K4", uk4), ("K5", uk5)):
        oh, wh = f(1)
        op, wp = f(2)
        if nm == "K4":
            uh, vh = oh, wh
            up, vp = op, wp
            verm = [x for x in (vh,) if x]
            if up != uh:
                verm.append("nicht konvergiert (dt/2 gibt: %s)" % up)
            U[nm] = dict(urteil=uh, vermerk="; ".join(verm) if verm else None,
                         werte=dict(haupt=W["k4_dt1"], probe=W["k4_dt2"]))
            continue
        uh = wort(oh); up = wort(op)
        U[nm] = dict(urteil=uh, vermerk=None if uh == up else "nicht konvergiert (dt/2 gibt: %s)" % up,
                     werte=dict(haupt=wh, probe=wp))
    json.dump(dict(urteile=U, werte_b=W), open(AUS, "w"), indent=1, default=float)
    for k, v in U.items():
        print(k, v["urteil"], v["vermerk"] or "")


if __name__ == "__main__":
    main()
