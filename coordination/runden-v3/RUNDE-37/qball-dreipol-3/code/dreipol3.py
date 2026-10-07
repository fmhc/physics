#!/usr/bin/env python3
# QBALL-DREIPOL-3 (Runde 43, Fast Lane): Ab welcher Ladung gibt es den Dreifarben-Tropfen (g4 = -0,1) in 3D und 2D
# (Bisektion), ist der 3D-Tropfen bei Q1 = 800 ausserhalb des symmetrischen Unterraums ein Minimum, und ist der
# Schwellradius R* in 2D und 3D gleich?
# Modell, Fluss bei festen Ladungen und Messgroessen kommen unveraendert aus QBALL-DREIPOL-2 (code/dreipol2.py,
# eingefroren 20261004-182806; hier als Kopie importiert). Neu sind nur die Ablaeufe:
#   modus bisekt: Bisektion in Q1 mit Ableitbarkeitsprobe je Schritt (E_start gegen E_Misch und E_Tropfen, VOR dem
#                 Fluss vom beruehrenden Dreieck); E_Tropfen kommt aus einem Fluss vom Sektorstart.
#   modus stab3:  3D-Tropfen bei Q1 = 800, Stoerungen ausserhalb des symmetrischen Unterraums, Rueckkehr.
# Kein CPU-Fallback (dreipol2.geraet bricht ohne CUDA ab).
import sys, os, json, math, time, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import torch
import dreipol2 as d

OMEGA = {2: math.pi, 3: 4.0 * math.pi / 3.0}


def radien(G, n2tot):
    """Radien einer Dichte S (Summe der Komponenten) um ihren Schwerpunkt.
    R_eq  (Hauptmass): Ersatzradius, int S dV = S_max * Omega_D * R_eq^D.
    R_vol (beschreibend): Gebiet S > S_max/2 als Kugel bzw. Scheibe gleichen Volumens.
    R_rms (beschreibend): sqrt(<r^2>_S)."""
    tot = float(n2tot.sum())
    smax = float(n2tot.max())
    D = G.d
    R_eq = (G.dV * tot / (smax * OMEGA[D])) ** (1.0 / D)
    nhalb = int((n2tot > 0.5 * smax).sum())
    R_vol = (G.dV * nhalb / OMEGA[D]) ** (1.0 / D)
    c = [float((xx * n2tot).sum()) / tot for xx in G.X]
    r2 = sum((xx - ci) ** 2 for xx, ci in zip(G.X, c))
    R_rms = math.sqrt(float((r2 * n2tot).sum()) / tot)
    return dict(R_eq=R_eq, R_vol=R_vol, R_rms=R_rms, S_max=smax, schwerpunkt=c)


def gestalt(pa, R):
    # wie DREIPOL-2 (auswertung2.py): verschmolzen bei max D < 0,25 R, Dreieck bei min D > R, sonst Zwischenform
    if max(pa) < 0.25 * R:
        return "verschmolzen"
    if min(pa) > R:
        return "dreieck"
    return "zwischenform"


def ausgang(info, ende, R):
    """Ausgang eines Flusses (PLAN 4): Tropfen = konvergiert, Gestalt Dreieck, Reinheit je Farbe >= 0,5;
    verschmolzen = konvergiert, Gestalt verschmolzen; sonst offen."""
    g = gestalt(ende["paarabstand"], R)
    konv = info["status"] == "konvergiert"
    if konv and g == "dreieck" and min(ende["reinheit"]) >= 0.5:
        return "Tropfen", g
    if konv and g == "verschmolzen":
        return "verschmolzen", g
    return "offen", g


def sektor_start(G, rad, g4, Q1, beta, wand_rad=60.0):
    """Tropfenartiger Start: radiales Profil des Mischballs (Ladung 3 Q1, g_eff = g4/3), farbig geteilt in drei
    Sektoren um die z-Achse (Richtungen 90/210/330 Grad wie die Dreiecksecken): psi_a = f(r) sqrt(w_a),
    w_a = softmax_b(beta x.e_b)_a, also glatt und sum_a w_a = 1 (in der Mitte gemischt)."""
    Q = 3.0 * Q1
    f, ir = rad.fluss(rad.start(Q), Q, g4 / 3.0, wand=wand_rad)
    base = d.profil(G, rad, f)
    proj = torch.stack([G.X[0] * math.cos(w) + G.X[1] * math.sin(w) for w in d.WINKEL])
    w = torch.softmax(beta * proj, dim=0)
    P = base[None] * torch.sqrt(w).to(torch.complex128)
    return P, dict(E_radial=ir["E"], status_radial=ir["status"])


def kompakt(verlauf):
    # Fluss-Protokoll mit beobachter(G, None, R): [it, E, res, schwerpunkte, paarabstaende, reinheit]
    return [[r[0], r[1], r[2], r[4], r[5]] for r in verlauf]


def schritt(G, rad, a, Q1, t0, snaps, tag):
    """Ein Bisektionsschritt bei Ladung Q1 je Pol (PLAN 4, 5):
    (1) Einpolball, Mischball (3 Q1); (2) Sektorstart -> Fluss -> E_Tropfen; (3) Ableitbarkeitsprobe VOR dem Lauf:
    E_start (beruehrendes Dreieck, d0 = 2R) gegen E_Misch und E_Tropfen; (4) Fluss vom beruehrenden Dreieck."""
    g4 = a.g4
    ts = time.time()
    psi1, ball = d.ein_pol_ball(G, rad, g4, Q1, wand=a.wand_ball, tol=a.tol_ball, nmax=a.nmax_ball,
                                wand_rad=a.wand_rad)
    R = ball["R_halb"]
    ball["radien"] = radien(G, d.n2von(psi1))
    psim, mix = d.misch_ball(G, rad, g4, 3.0 * Q1, wand=a.wand_ball, tol=a.tol_ball, nmax=a.nmax_ball,
                             wand_rad=a.wand_rad)
    mix["radien"] = radien(G, d.n2von(psim).sum(0))
    del psim
    Q = [Q1, Q1, Q1]
    bo = d.beobachter(G, None, R)
    # (2) Sektorstart -> E_Tropfen
    Ps, sinfo = sektor_start(G, rad, g4, Q1, a.beta, wand_rad=a.wand_rad)
    s_start = d.zustand_info(G, Ps, Q, g4, R)
    Pse, infs = d.fluss(G, Ps, Q, g4, nmax=a.nfluss, tol=a.tol, alle=a.alle, wand=a.wand_fluss, beob=bo)
    s_ende = d.zustand_info(G, Pse, Q, g4, R)
    s_aus, s_g = ausgang(infs, s_ende, R)
    E_T = s_ende["E"] if s_aus == "Tropfen" else None
    snaps["%s_sektor_ende" % tag] = d.schnitt(G, d.n2von(Pse))
    s_rad = radien(G, d.n2von(Pse).sum(0))
    del Ps, Pse
    # (3) beruehrendes Dreieck und Ableitbarkeitsprobe vor dem Lauf
    F1 = G.fft(psi1)
    pos, rho = d.dreieck_pos(G, 2.0 * R)
    Pb = torch.stack([G.shiftF(F1, p) for p in pos])
    del F1
    b_start = d.zustand_info(G, Pb, Q, g4, R)
    E_start = b_start["E"]
    E_M = mix["E"]
    vorab = dict(E_start=E_start, E_Misch=E_M, E_Misch_radial=mix["radial"]["E"], E_Tropfen=E_T,
                 E_drei_getrennt=3.0 * ball["E"], start_minus_misch=E_start - E_M,
                 start_minus_tropfen=(E_start - E_T) if E_T is not None else None,
                 erzwungen_gegen_misch=bool(E_start < E_M),
                 erzwungen_gegen_tropfen=bool(E_T is not None and E_start < E_T),
                 sektorstart_E=s_start["E"], sektorstart_minus_misch=s_start["E"] - E_M,
                 sektorlauf_erzwungen=bool(s_start["E"] < E_M), protokolliert_utc=d.jetzt())
    vorab["erzwungen"] = bool(vorab["erzwungen_gegen_misch"] or vorab["erzwungen_gegen_tropfen"])
    print("vorab Q1=%g" % Q1, vorab, flush=True)
    snaps["%s_start" % tag] = d.schnitt(G, d.n2von(Pb))
    # (4) Fluss vom beruehrenden Dreieck
    Pbe, infb = d.fluss(G, Pb, Q, g4, nmax=a.nfluss, tol=a.tol, alle=a.alle, wand=a.wand_fluss, beob=bo)
    b_ende = d.zustand_info(G, Pbe, Q, g4, R)
    b_aus, b_g = ausgang(infb, b_ende, R)
    snaps["%s_ende" % tag] = d.schnitt(G, d.n2von(Pbe))
    b_rad = radien(G, d.n2von(Pbe).sum(0))
    del Pb, Pbe
    out = dict(Q1=Q1, tag=tag, R_halb=R, ball=ball, misch=mix, vorab=vorab,
               sektor=dict(start=s_start, status=infs["status"], it=infs["it"], sek=infs["sek"], ende=s_ende,
                           ausgang=s_aus, gestalt=s_g, radien=s_rad, info=sinfo, verlauf=kompakt(infs["verlauf"])),
               beruehrend=dict(start=b_start, status=infb["status"], it=infb["it"], sek=infb["sek"], ende=b_ende,
                               ausgang=b_aus, gestalt=b_g, radien=b_rad, verlauf=kompakt(infb["verlauf"])),
               ausgang=b_aus, gueltig=bool(b_aus in ("Tropfen", "verschmolzen") and not vorab["erzwungen"]),
               sek=time.time() - ts, t_seit_start=time.time() - t0)
    print("schritt Q1=%g: ausgang %s (%s, %s, it %d), sektor %s (%s, it %d), E_ende-E_Misch %.6g, t=%.0fs"
          % (Q1, b_aus, b_g, infb["status"], infb["it"], s_aus, s_g, infs["it"], b_ende["E"] - E_M,
             time.time() - t0), flush=True)
    torch.cuda.empty_cache()
    return out


def modus_bisekt(a):
    """Bisektion in Q1 (PLAN 4): obere Klammer Q_hi (Kontrolle), Abstieg ueber Q_abstieg bis zum ersten
    Verschmelzen, dann n_bisekt Halbierungen. Erzwungen oder offen -> Abbruch der Bisektion."""
    t0 = time.time()
    G = d.Gitter(a.N, a.L, a.dim)
    rad = d.Radial(a.dim, dr=a.dr, rmax=a.rmax)
    out = dict(modus="bisekt", geraet=d.GERAET, dim=a.dim, N=a.N, L=a.L, h=G.h, g4=a.g4, start_utc=d.jetzt(),
               args={k: v for k, v in vars(a).items()}, schritte=[])
    snaps = {}

    def lauf(Q1, rolle):
        s = schritt(G, rad, a, Q1, t0, snaps, "s%d" % len(out["schritte"]))
        s["rolle"] = rolle
        out["schritte"].append(s)
        d.schreibe(a.out, out)
        return s

    stop = None
    Q_hi, Q_lo = None, None
    s = lauf(a.Q_hi, "kontrolle_oben")
    if s["ausgang"] == "Tropfen" and not s["vorab"]["erzwungen"]:
        Q_hi = a.Q_hi
    else:
        stop = "obere Klammer Q1 = %g ohne gueltigen Tropfen (%s)" % (a.Q_hi, s["ausgang"])
    if stop is None:
        for q in a.Q_abstieg:
            if time.time() - t0 > a.zeitgrenze:
                stop = "zeitgrenze"
                break
            s = lauf(q, "klammer_unten")
            if s["vorab"]["erzwungen"] or s["ausgang"] == "offen":
                stop = "Klammerschritt Q1 = %g erzwungen oder offen" % q
                break
            if s["ausgang"] == "verschmolzen":
                Q_lo = q
                break
            Q_hi = q
        if stop is None and Q_lo is None:
            stop = "kein Verschmelzen bis Q1 = %g" % a.Q_abstieg[-1]
    k = 0
    while stop is None and k < a.n_bisekt:
        if time.time() - t0 > a.zeitgrenze:
            stop = "zeitgrenze"
            break
        q = 0.5 * (Q_lo + Q_hi)
        s = lauf(q, "bisektion")
        k += 1
        if s["vorab"]["erzwungen"]:
            stop = "erzwungen bei Q1 = %g" % q
            break
        if s["ausgang"] == "Tropfen":
            Q_hi = q
        elif s["ausgang"] == "verschmolzen":
            Q_lo = q
        else:
            stop = "offen bei Q1 = %g" % q
            break
    out["klammer"] = dict(Q_lo=Q_lo, Q_hi=Q_hi, n_bisekt=k, stop=stop if stop else "fertig",
                          Q_stern=(0.5 * (Q_lo + Q_hi) if (Q_lo is not None and Q_hi is not None) else None),
                          halbbreite=(0.5 * (Q_hi - Q_lo) if (Q_lo is not None and Q_hi is not None) else None))
    print("klammer", out["klammer"], flush=True)
    np.savez_compressed(a.out.replace(".json", "_bilder.npz"), x=(G.x if a.dim == 3 else G.x[::2]), **snaps)
    out["sek"] = time.time() - t0
    out["maxrss_mb"] = d.maxrss_mb()
    out["gpu_mb"] = d.gpu_mb()
    out["ende_utc"] = d.jetzt()
    d.schreibe(a.out, out)


# ------------------------------------------------------------------ Teil B: Stoerungen des 3D-Tropfens
def rauschfeld3(G, saat, kc=2.0):
    # wie dreipol2.rauschfeld, fuer beliebiges d (glattes komplexes Gaussfeld, k_c = 2, Effektivwert 1)
    rng = np.random.default_rng(saat)
    w = rng.standard_normal((6,) + (G.N,) * G.d)
    eta = torch.tensor(w[0:3] + 1j * w[3:6], dtype=torch.complex128, device=d.DEV)
    F = G.fft(eta) * torch.exp(-G.K2 / (2.0 * kc * kc))[None]
    eta = G.ifft(F)
    return eta / math.sqrt(float((eta.real ** 2 + eta.imag ** 2).mean()))


def stoerungen3(G, Pref, ref, R, amp_v, amp_l):
    """Stoerungen des 3D-Tropfens ausserhalb des symmetrischen Unterraums (PLAN 4, Teil B)."""
    sp = ref["schwerpunkte"]
    mitte = np.mean(np.array(sp), axis=0)
    Q = list(ref["Q"])
    F = G.fft(Pref)
    out = {}
    # V1: Pol 1 um amp_v R tangential (+x) und amp_v R aus der Ebene (+z)
    P = Pref.clone()
    P[0] = G.shiftF(F[0], [amp_v * R, 0.0, amp_v * R])
    out["V1"] = (P, Q, "Pol 1 um %.2f R tangential (+x) und %.2f R aus der Ebene (+z)" % (amp_v, amp_v))
    # V2: Pol 2 um amp_v R radial nach aussen (in der Ebene) und amp_v R aus der Ebene (+z)
    e = np.array(sp[1]) - mitte
    e[2] = 0.0
    e = e / np.linalg.norm(e)
    P = Pref.clone()
    P[1] = G.shiftF(F[1], [amp_v * R * e[0], amp_v * R * e[1], amp_v * R])
    out["V2"] = (P, Q, "Pol 2 um %.2f R radial nach aussen und %.2f R aus der Ebene (+z)" % (amp_v, amp_v))
    # L1: amp_l der Farbe 2 aus Klumpen 2 nach Klumpen 1, gleichphasig (alle Q_a bleiben)
    P = Pref.clone()
    d12 = list(np.array(sp[0]) - np.array(sp[1]))
    P[1] = math.sqrt(1.0 - amp_l) * Pref[1] + math.sqrt(amp_l) * G.shiftF(F[1], d12)
    out["L1"] = (P, Q, "%.0f %% der Farbe 2 von Klumpen 2 nach Klumpen 1" % (100 * amp_l))
    # L2: amp_l der Farbe 1 aus Klumpen 1 nach Klumpen 2
    P = Pref.clone()
    d21 = list(np.array(sp[1]) - np.array(sp[0]))
    P[0] = math.sqrt(1.0 - amp_l) * Pref[0] + math.sqrt(amp_l) * G.shiftF(F[0], d21)
    out["L2"] = (P, Q, "%.0f %% der Farbe 1 von Klumpen 1 nach Klumpen 2" % (100 * amp_l))
    # P1, P2: gleichfoermige Phasenversaetze (exakte Symmetrie, vorab ableitbar)
    P = Pref.clone()
    P[1] = P[1] * complex(math.cos(0.5 * math.pi), math.sin(0.5 * math.pi))
    out["P1"] = (P, Q, "Phase von Komponente 2 um pi/2 versetzt")
    P = Pref.clone()
    P[1] = P[1] * complex(math.cos(2 * math.pi / 3), math.sin(2 * math.pi / 3))
    P[2] = P[2] * complex(math.cos(4 * math.pi / 3), math.sin(4 * math.pi / 3))
    out["P2"] = (P, Q, "Phasen von Komponente 2 und 3 um 2pi/3 und 4pi/3 versetzt")
    # beschreibend (ohne Urteil): Z1 nur aus der Ebene; R5, R20 glattes Rauschen auf allen Komponenten
    P = Pref.clone()
    P[0] = G.shiftF(F[0], [0.0, 0.0, amp_v * R])
    out["Z1"] = (P, Q, "Pol 1 um %.2f R aus der Ebene (+z), beschreibend" % amp_v)
    env = torch.sqrt(d.n2von(Pref).sum(0))
    for name, eps, saat in (("R5", 0.05, 11), ("R20", 0.20, 12)):
        eta = rauschfeld3(G, saat)
        out[name] = (Pref + eps * eta * env[None], Q,
                     "glattes Rauschen %.0f %% der lokalen Feldstaerke, Saat %d, beschreibend" % (100 * eps, saat))
    del F
    return out


def seite(n2):
    # Seitenansicht: Projektion ueber y (Achsen: Komponente, x, y, z) -> (3, x, z)
    return n2.sum(dim=2).float().cpu().numpy()


def modus_stab3(a):
    t0 = time.time()
    G = d.Gitter(a.N, a.L, 3)
    rad = d.Radial(3, dr=a.dr, rmax=a.rmax)
    g4, Q1 = a.g4, a.Q1
    out = dict(modus="stab3", geraet=d.GERAET, N=a.N, L=a.L, h=G.h, g4=g4, Q1=Q1, start_utc=d.jetzt(),
               args={k: v for k, v in vars(a).items()})
    psi1, ball = d.ein_pol_ball(G, rad, g4, Q1, wand=a.wand_ball, tol=a.tol_ball, nmax=a.nmax_ball,
                                wand_rad=a.wand_rad)
    R = ball["R_halb"]
    out["ball"] = ball
    psim, mix = d.misch_ball(G, rad, g4, 3.0 * Q1, wand=a.wand_ball, tol=a.tol_ball, nmax=a.nmax_ball,
                             wand_rad=a.wand_rad)
    out["mischball"] = mix
    del psim
    Q = [Q1, Q1, Q1]
    F1 = G.fft(psi1)
    pos, rho = d.dreieck_pos(G, 2.0 * R)
    P = torch.stack([G.shiftF(F1, p) for p in pos])
    del F1
    out["start"] = d.zustand_info(G, P, Q, g4, R)
    # Referenz: Fluss vom beruehrenden Dreieck bis tol (wie DREIPOL-2 N1), dann weiter bis tol_ref
    Pf, i1 = d.fluss(G, P, Q, g4, nmax=a.nfluss, tol=a.tol, wand=a.wand_fluss)
    out["tropfen_tol"] = dict(status=i1["status"], it=i1["it"], sek=i1["sek"], **d.zustand_info(G, Pf, Q, g4, R))
    Pref, i2 = d.fluss(G, Pf, Q, g4, nmax=a.nmax_ref, tol=a.tol_ref, wand=a.wand_ref)
    ref = dict(status=i2["status"], it=i2["it"], sek=i2["sek"], Q=Q, **d.zustand_info(G, Pref, Q, g4, R))
    ref["gestalt"] = gestalt(ref["paarabstand"], R)
    ref["radien"] = radien(G, d.n2von(Pref).sum(0))
    out["referenz"] = ref
    print("referenz", {k: ref[k] for k in ("status", "it", "E", "res", "paarabstand_R", "reinheit", "gestalt")},
          "E-E_Misch", ref["E"] - mix["E"], f"t={time.time() - t0:.0f}s", flush=True)
    d.schreibe(a.out, out)
    snaps = {"referenz": d.schnitt(G, d.n2von(Pref)), "referenz_seite": seite(d.n2von(Pref))}
    out["stoerungen"] = {}
    st = stoerungen3(G, Pref, ref, R, a.amp_v, a.amp_l)
    for name in a.liste:
        if time.time() - t0 > a.zeitgrenze:
            out["stoerungen"][name] = dict(status="nicht gerechnet (zeitgrenze)")
            print(name, "nicht gerechnet (zeitgrenze)", flush=True)
            continue
        P0, Qs, text = st[name]
        start = d.zustand_info(G, P0, Qs, g4, R, ref=ref)
        bo = d.beobachter(G, ref["schwerpunkte"], R)
        Pe, info = d.fluss(G, P0, Qs, g4, nmax=a.nmax_st, tol=a.tol_st, wand=a.wand_st, beob=bo)
        ende = d.zustand_info(G, Pe, Qs, g4, R, ref=ref)
        vl = [[r[0], r[1] - ref["E"], r[2], r[-2], r[-1], r[5]] for r in info["verlauf"]]
        out["stoerungen"][name] = dict(text=text, Q=Qs, status=info["status"], it=info["it"], sek=info["sek"],
                                       start=start, ende=ende, verlauf=vl)
        snaps["%s_start" % name] = d.schnitt(G, d.n2von(P0))
        snaps["%s_ende" % name] = d.schnitt(G, d.n2von(Pe))
        snaps["%s_start_seite" % name] = seite(d.n2von(P0))
        snaps["%s_ende_seite" % name] = seite(d.n2von(Pe))
        print(f"{name}: {info['status']} it={info['it']} d_rms {start['d_rms_R']:.4f} -> {ende['d_rms_R']:.3e} "
              f"d_form {start['d_form_R']:.4f} -> {ende['d_form_R']:.3e} dE {start['dE']:.3e} -> {ende['dE']:.3e} "
              f"t={time.time() - t0:.0f}s", flush=True)
        d.schreibe(a.out, out)
        del P0, Pe
        torch.cuda.empty_cache()
    np.savez_compressed(a.out.replace(".json", "_bilder.npz"), x=G.x, **snaps)
    out["sek"] = time.time() - t0
    out["maxrss_mb"] = d.maxrss_mb()
    out["gpu_mb"] = d.gpu_mb()
    out["ende_utc"] = d.jetzt()
    d.schreibe(a.out, out)


def liste(s, typ=float):
    return [typ(v) for v in s.split(",")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("modus", choices=["bisekt", "stab3"])
    ap.add_argument("--out", required=True)
    ap.add_argument("--dim", type=int, default=3)
    ap.add_argument("--N", type=int, default=80)
    ap.add_argument("--L", type=float, default=48.0)
    ap.add_argument("--g4", type=float, default=-0.1)
    ap.add_argument("--dr", type=float, default=0.01)
    ap.add_argument("--rmax", type=float, default=60.0)
    ap.add_argument("--tol_ball", type=float, default=1e-6)
    ap.add_argument("--nmax_ball", type=int, default=20000)
    ap.add_argument("--wand_ball", type=float, default=90.0)
    ap.add_argument("--wand_rad", type=float, default=60.0)
    ap.add_argument("--tol", type=float, default=1e-6)
    ap.add_argument("--nfluss", type=int, default=60000)
    ap.add_argument("--alle", type=int, default=50)
    ap.add_argument("--wand_fluss", type=float, default=75.0)
    ap.add_argument("--zeitgrenze", type=float, default=330.0)
    # bisekt
    ap.add_argument("--Q_hi", type=float, default=800.0)
    ap.add_argument("--Q_abstieg", type=liste, default=[400.0])
    ap.add_argument("--n_bisekt", type=int, default=6)
    ap.add_argument("--beta", type=float, default=1.5)
    # stab3
    ap.add_argument("--Q1", type=float, default=800.0)
    ap.add_argument("--tol_ref", type=float, default=1e-9)
    ap.add_argument("--nmax_ref", type=int, default=20000)
    ap.add_argument("--wand_ref", type=float, default=90.0)
    ap.add_argument("--tol_st", type=float, default=1e-8)
    ap.add_argument("--nmax_st", type=int, default=30000)
    ap.add_argument("--wand_st", type=float, default=60.0)
    ap.add_argument("--amp_v", type=float, default=0.15)
    ap.add_argument("--amp_l", type=float, default=0.05)
    ap.add_argument("--liste", type=lambda s: s.split(","),
                    default=["V1", "V2", "L1", "L2", "P1", "P2", "Z1", "R5", "R20"])
    a = ap.parse_args()
    d.GERAET = d.geraet()
    print("geraet", d.GERAET, flush=True)
    t0 = time.time()
    {"bisekt": modus_bisekt, "stab3": modus_stab3}[a.modus](a)
    print("geschrieben", a.out, f"{time.time() - t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
