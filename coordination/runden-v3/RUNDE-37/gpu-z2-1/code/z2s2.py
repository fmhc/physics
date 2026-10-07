#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Z2-SCHUTZ-2 (Runde 49, RUNDE-37/z2-schutz-2): Barriere 360 -> 0 Grad bei getrennt variiertem Kern- und Kugelradius.

Synthetische Modellrechnung, keine Messdaten. Modell, Ablauf und Regeln: PLAN.md.
Unveraendert benutzt: finn.py (Netz, Energie, FIRE), guertel2.py (reparam_feld, schreibe_json), z2.py aus Z2-SCHUTZ-1
(CI-NEB z2.wegrechnung, Hesse, Lokalisierung, Kappenrichtung N_P).
Neu hier (PLAN Abschnitt 1): Startlauf mit Hesse S, korrigierte Bisektion in der ebenen Darstellung psi, Freigabe bis
zur Ruhe (Zwischenminimum erkennen), L10.

Modi:
  start   Startzustand S (360 Grad) und vier kleinste Eigenwerte der Riemannschen Hesse-Matrix von S.
  bisekt  Verfahren A: korrigierte Bisektion (psi-FIRE) und Freigabe.
  weg     Verfahren B: CI-NEB (z2.wegrechnung, unveraendert) auf dem Weg aus der Bisektion.
  pruef   Konsistenzprobe psi gegen Quaternion und Laufzeit je Schritt (nur Rauchtest).
Aufruf nur ueber kleintest.sh auf der .69.
"""
import argparse
import hashlib
import os
import resource
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import finn  # noqa: E402  (GUERTEL-FINN-NETZ-1, unveraendert)
import guertel2 as g2  # noqa: E402  (GUERTEL-2, unveraendert)
import z2  # noqa: E402  (Z2-SCHUTZ-1, unveraendert)

T_START = time.time()
START_UTC = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
N_P = z2.N_P


def sha_datei(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def kopf(args):
    return {"karte": "Z2-SCHUTZ-2 (Runde 49)", "modus": args.modus, "args": vars(args),
            "code_sha256": sha_datei(os.path.abspath(__file__)),
            "z2_sha256": sha_datei(os.path.abspath(z2.__file__)),
            "finn_sha256": sha_datei(os.path.abspath(finn.__file__)),
            "g2_sha256": sha_datei(os.path.abspath(g2.__file__)),
            "start_utc": START_UTC, "schreibzeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "numpy": np.__version__}


def maxrss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def gtag(r0, R):
    return "r%g-R%g" % (r0, R)


def wand():
    return time.time() - T_START


# ---------------------------------------------------------------- ebene Darstellung (PLAN 0.2)

class Eben:
    """q = cos(psi) + k sin(psi): c_b = cos(psi_a - psi_b), E = sum 4 sin^2, dE/dpsi_a = sum 8 sin cos."""

    def __init__(self, netz):
        self.a, self.b, self.frei = netz.a, netz.b, netz.frei
        self.Dm = (netz.inc_a - netz.inc_b).tocsr()

    def energie(self, p):
        d = p[self.a] - p[self.b]
        sd = np.sin(d)
        cd = np.cos(d)
        E = 4.0 * float((sd * sd).sum())
        G = self.Dm @ (8.0 * sd * cd)
        return E, G, float(cd.min())


def q_aus_psi(p, qS, netz):
    q = np.zeros((len(p), 4))
    q[:, 0] = np.cos(p)
    q[:, 3] = np.sin(p)
    q[~netz.frei] = qS[~netz.frei]
    return q


def fire_psi(eb, p, nmax, stopp, dtmax=0.1, dtstart=0.02, capw=0.05, nskip=30, merke=True, anstieg=np.inf):
    """FIRE in psi, Arithmetik wie finn.fire_feld fuer B = 1 (ein Skalar je Knoten, feste Knoten Kraft 0).
    stopp(it, E, p, fmax) -> (Klasse oder None, im_Sattelbereich), geprueft vor jedem Schritt (wie z2.fire_klasse).
    Merkt ab Schritt nskip den Zustand kleinster groesster Knotenkraft im Sattelbereich (PLAN Abschnitt 3)."""
    fr = eb.frei
    E, G, cmin = eb.energie(p)
    F = np.where(fr, -G, 0.0)
    v = np.zeros_like(p)
    dt, alpha, npos = dtstart, 0.1, 0
    fmax = float(np.abs(F).max())
    best = (np.inf, None, None, -1)
    klasse, it, Emax, cmin_lauf = None, 0, E, cmin
    gefroren = False
    for it in range(nmax):
        k, bereich = stopp(it, E, p, fmax)
        if merke and it >= nskip and not gefroren:
            # erster Durchgang (PLAN Abschnitt 3): Suche endet, sobald die Kraft das bisherige Minimum um den Faktor
            # anstieg uebersteigt
            if bereich and fmax < best[0]:
                best = (fmax, p.copy(), E, it)
            elif best[1] is not None and fmax > anstieg * best[0]:
                gefroren = True
        if k is not None:
            klasse = k
            break
        Pw = (F * v).sum()
        vn = np.sqrt((v * v).sum())
        fn = np.sqrt((F * F).sum()) + 1.0e-300
        if Pw > 0.0:
            v = (1.0 - alpha) * v + (alpha * vn / fn) * F
            if npos >= 5:
                dt = min(dt * 1.1, dtmax)
                alpha *= 0.99
            npos += 1
        else:
            v = np.zeros_like(v)
            dt = max(dt * 0.5, 1.0e-7)
            alpha = 0.1
            npos = 0
        v = v + F * dt
        dx = v * dt
        dn = float(np.abs(dx).max())
        if dn > capw:
            dx *= capw / dn
            v *= capw / dn
        p = p + dx
        E, G, cmin = eb.energie(p)
        F = np.where(fr, -G, 0.0)
        fmax = float(np.abs(F).max())
        Emax = max(Emax, E)
        cmin_lauf = min(cmin_lauf, cmin)
    else:
        it = nmax
    if best[1] is None:
        best = (fmax, p.copy(), E, -1)
    return klasse, p, int(it), best, E, fmax, Emax, cmin_lauf


def lokal2(netz, qs, qS):
    """z2.lokalisierung plus L10 (PLAN Abschnitt 5)."""
    L = z2.lokalisierung(netz, qs, qS)
    ca = (qs[netz.a] * qs[netz.b]).sum(-1)
    c0 = (qS[netz.a] * qS[netz.b]).sum(-1)
    D = 4.0 * (1.0 - ca * ca) - 4.0 * (1.0 - c0 * c0)
    B = float(D.sum())
    cs = np.cumsum(np.sort(D)[::-1])
    L["L10"] = float(cs[9] / B) if B > 0 else None
    L["n_bindungen"] = int(len(D))
    return L


def kappe_w(netz, args):
    rn = np.sqrt((netz.pos ** 2).sum(1))
    gam = np.arccos(np.clip((netz.pos @ N_P) / np.maximum(rn, 1e-300), -1.0, 1.0))
    w = np.clip((np.deg2rad(args.kappe_b) + np.deg2rad(args.d_grad) - gam) / np.deg2rad(args.d_grad), 0.0, 1.0)
    w[~netz.frei] = 0.0
    return w


# ---------------------------------------------------------------- start (PLAN 2, Aenderung 4)

def modus_start(args):
    t0 = time.time()
    netz = finn.Netz("diamant", args.r0, args.R, "so3")
    x = np.zeros((netz.N, 1, 4))
    x[:, 0, 0] = np.cos(np.pi * netz.h)
    x[:, 0, 3] = np.sin(np.pi * netz.h)
    x = netz.setze(x, 2.0 * np.pi)
    E0, _, mon0 = netz.energie(x, grad=False)
    # Kopie z2.modus_start: finn.fire_feld in Bloecken zu 1000 Schritten bis ftol, nmax oder Wandzeit
    it, ml_alle = 0, float(mon0[0])
    grund = "nmax"
    while True:
        x, E, fm, i1, mon, ml = finn.fire_feld(netz, x, min(1000, args.nmax - it), args.ftol, args.dtmax)
        it += int(i1) + (0 if fm[0] <= args.ftol else 1)
        ml_alle = min(ml_alle, float(ml[0]))
        if fm[0] <= args.ftol:
            grund = "konvergiert"
            break
        if it >= args.nmax:
            break
        if wand() > args.budget:
            grund = "wandzeit"
            break
    tag = "start-" + gtag(args.r0, args.R)
    q = x[:, 0].copy()
    np.savez_compressed(os.path.join(args.aus, tag + ".npz"), q=q)
    t_fire = time.time() - t0
    eb = Eben(netz)
    E_psi, _, _ = eb.energie(np.arctan2(q[:, 3], q[:, 0]))
    vorl = {"kopf": kopf(args), "netz_info": netz.info(), "E_anfang": float(E0[0]), "E_S": float(E[0]),
            "E_S_psi": E_psi, "eben_rest": float(np.abs(q[:, 1:3]).max()), "fmax": float(fm[0]), "schritte": int(it),
            "grund": grund, "sonde": float(mon[0]), "sonde_lauf": ml_alle, "hesse_S": None,
            "vorlaeufig": "Hesse laeuft noch", "laufzeit_fire_s": t_fire}
    g2.schreibe_json(os.path.join(args.aus, tag + ".json"), vorl)
    # Hesse von S (z2.hesse_matrix, z2.eigen_klein, z2.symmetriemoden unveraendert)
    t1 = time.time()
    H, Tb, idx = z2.hesse_matrix(netz, q)
    w, V, fehler = z2.eigen_klein(H, args.k, args.tol, args.maxiter)
    hs = {"eigenwerte": w, "fehler": fehler, "dim": int(H.shape[0]), "nnz": int(H.nnz),
          "zahl_negativ": int((w < -1e-5).sum()) if w is not None else None}
    if w is not None:
        sm = z2.symmetriemoden(netz, q, Tb)
        V2 = V[:, :2]
        hs["symmetrie_ueberlapp"] = [float(np.sqrt(((V2.T @ u) ** 2).sum())) for u in sm]
    hs["laufzeit_s"] = time.time() - t1
    aus = {"kopf": kopf(args), "netz_info": netz.info(), "E_anfang": float(E0[0]), "E_S": float(E[0]),
           "E_S_psi": E_psi, "eben_rest": float(np.abs(q[:, 1:3]).max()), "fmax": float(fm[0]), "schritte": int(it),
           "grund": grund, "sonde": float(mon[0]), "sonde_lauf": ml_alle, "struktur": finn.struktur(netz, x),
           "hesse_S": hs, "laufzeit_fire_s": t_fire, "laufzeit_s": time.time() - t0, "maxrss_mb": maxrss_mb()}
    g2.schreibe_json(os.path.join(args.aus, tag + ".json"), aus)
    print("start fertig %s laufzeit %.1f s" % (tag, aus["laufzeit_s"]))


# ---------------------------------------------------------------- Verfahren A (PLAN Abschnitt 3)

def modus_bisekt(args):
    t0 = time.time()
    netz = finn.Netz("diamant", args.r0, args.R, "so3")
    eb = Eben(netz)
    fr = netz.frei
    qS = np.load(args.start)["q"]
    ESq, _, _ = netz.energie(qS[:, None, :], grad=False)
    pS = np.arctan2(qS[:, 3], qS[:, 0])
    ES, _, _ = eb.energie(pS)
    w = kappe_w(netz, args)
    t_halb = args.halb_anteil * args.budget
    t_halb2 = args.halb2_anteil * args.budget
    t_halb3 = args.halb3_anteil * args.budget
    t_halb3b = args.halb3b_anteil * args.budget
    t_bahn = args.bahn_anteil * args.budget

    def stopp_klasse(it, E, p, fmax):
        d = np.sin(p[fr] - pS[fr])
        D = float((d * d).max())
        bereich = bool(D >= args.d_sattel and fmax > args.f_ruhe_bereich)
        if E < ES - args.delta_k:
            return "T", bereich
        if it >= args.nskip and D <= args.eps_s:
            return "S", bereich
        if it >= args.nskip and fmax <= args.ftol_m:
            return "M", bereich
        if wand() > t_bahn:
            return "offen", bereich
        return None, bereich

    def bahn(p0, lam):
        kl, p, it, best, E, fm, Emax, cl = fire_psi(eb, p0, args.nbis, stopp_klasse, dtmax=args.dtmax,
                                                    nskip=args.nskip)
        if kl is None:
            kl = "offen"
        d = np.sin(p[fr] - pS[fr])
        info = {"lambda": lam, "klasse": kl, "schritte": it, "fmin": best[0], "E_fmin": best[2], "it_fmin": best[3],
                "fmax_ende": fm, "E_ende": E, "D_ende": float((d * d).max()), "fmin_im_sattelbereich": bool(best[3] >= 0),
                "t": wand()}
        return kl, p, best, info

    def bisektion(zustand, nh, t_grenze, pruef0, ziel):
        """Halbierungen auf [0, 1]. ziel "S": Rand des Beckens von S (oben "T" oder "M", unten "S"); ziel "T": Rand des
        Beckens von T (oben "T", unten "S" oder "M"). Erst 1 (muss oben sein), bei pruef0 auch 0 (muss unten sein)."""
        oben, unten = (("T", "M"), ("S",)) if ziel == "S" else (("T",), ("S", "M"))
        lo, hi = 0.0, 1.0
        sch = []
        kl, p, best, info = bahn(zustand(1.0), 1.0)
        sch.append(info)
        letzte = {"o": (1.0, p, best, kl) if kl in oben else None, "u": None, "tmin": None}
        if kl == "T":
            letzte["tmin"] = (1.0, p.copy())
        if letzte["o"] is None:
            return lo, hi, sch, letzte, 0
        if pruef0:
            kl, p, best, info = bahn(zustand(0.0), 0.0)
            sch.append(info)
            if kl not in unten:
                return lo, hi, sch, letzte, 0
            letzte["u"] = (0.0, p, best, kl)
        n_h = 0
        for _ in range(nh):
            if wand() > t_grenze:
                break
            lam = 0.5 * (lo + hi)
            kl, p, best, info = bahn(zustand(lam), lam)
            sch.append(info)
            if kl == "T" and (letzte["tmin"] is None or lam < letzte["tmin"][0]):
                letzte["tmin"] = (lam, p.copy())
            if kl in oben:
                hi = lam
                letzte["o"] = (lam, p, best, kl)
                n_h += 1
            elif kl in unten:
                lo = lam
                letzte["u"] = (lam, p, best, kl)
                n_h += 1
            else:
                break
        return lo, hi, sch, letzte, n_h

    def nachschaerfen(letzte, ziel, t_grenze):
        """Stufe 2 (edge tracking): Strecke zwischen den Zustaenden kleinster Kraft der letzten unteren und oberen Bahn."""
        info = {"gerechnet": False}
        if not (letzte["o"] is not None and letzte["u"] is not None and letzte["o"][2][3] >= 0
                and letzte["u"][2][3] >= 0 and args.nbisekt2 > 0):
            return letzte, info
        pa, pb = letzte["u"][2][1].copy(), letzte["o"][2][1].copy()
        lo2, hi2, sch2, l2, n2 = bisektion(lambda mu: (1.0 - mu) * pa + mu * pb, args.nbisekt2, t_grenze, True, ziel)
        ok2 = bool(l2["o"] is not None and l2["u"] is not None and n2 >= args.nbisekt2_min
                   and l2["o"][2][3] >= 0 and l2["u"][2][3] >= 0)
        info = {"gerechnet": True, "gilt": ok2, "mu_lo": lo2, "mu_hi": hi2, "n_halb": n2, "schritte": sch2,
                "abstand_start": float(np.sqrt(((pb - pa) ** 2).sum()))}
        return (l2 if ok2 else letzte), info

    def sattel_info(letzte):
        bo, bu = letzte["o"][2], letzte["u"][2]
        info = {"E_fmin_oben": bo[2], "E_fmin_unten": bu[2], "fmin_oben": bo[0], "fmin_unten": bu[0],
                "klasse_oben": letzte["o"][3], "klasse_unten": letzte["u"][3],
                "sattelbereich": [bool(bo[3] >= 0), bool(bu[3] >= 0)],
                "genau": bool(bo[3] >= 0 and bu[3] >= 0 and max(bo[0], bu[0]) <= args.fmin_max),
                "E_sattel": float(max(bo[2], bu[2])), "barriere": float(max(bo[2], bu[2]) - ES)}
        return info, (bo[1] if bo[2] >= bu[2] else bu[1])

    def q_(p):
        return q_aus_psi(p, qS, netz)

    # Stufe 1: Kappenfamilie, Rand des Beckens von S (PLAN Abschnitt 3)
    lo, hi, schritte, letzte, n_halb = bisektion(lambda lam: pS * (1.0 - lam * w), args.nbisekt, t_halb, False, "S")
    aus = {"kopf": kopf(args), "netz_info": netz.info(), "E_S": ES, "E_S_quat": float(ESq[0]),
           "schritte": schritte, "lambda_lo": lo, "lambda_hi": hi, "n_halb": n_halb,
           "lambda1_klasse": schritte[0]["klasse"], "stufe2": {"gerechnet": False}, "stufe3": {"gerechnet": False}}
    gut = letzte["o"] is not None and letzte["u"] is not None
    aus["klammer"] = bool(gut)
    if gut:
        tmin1 = letzte["tmin"]
        letzte, aus["stufe2"] = nachschaerfen(letzte, "S", t_halb2)
        s1, sattel1 = sattel_info(letzte)
        aus["sattel1"] = s1
        pfad = [qS, q_(letzte["u"][2][1]), q_(letzte["o"][2][1])]
        ende, barriere, genau, sattel, pfad_ok = letzte["o"][1], s1["barriere"], s1["genau"], sattel1, True
        aus["weg_art"] = "S -> Sattel -> T"
        if letzte["o"][3] == "M":
            # Stufe 3 (PLAN Abschnitt 3): Zwischenminimum M an der Nicht-S-Seite; Rand des Beckens von T auf der Strecke
            # von M zum Endzustand der T-Bahn mit kleinstem lambda aus Stufe 1, dann Nachschaerfen.
            pM = letzte["o"][1].copy()
            pfad.append(q_(pM))
            info3 = {"gerechnet": False, "lambda_T": tmin1[0] if tmin1 is not None else None}
            pfad_ok = False
            if tmin1 is not None:
                pTe = tmin1[1].copy()
                lo3, hi3, sch3, l3, n3 = bisektion(lambda mu: (1.0 - mu) * pM + mu * pTe,
                                                   args.nbisekt, t_halb3, True, "T")
                info3.update({"gerechnet": True, "mu_lo": lo3, "mu_hi": hi3, "n_halb": n3, "schritte": sch3})
                if l3["o"] is not None and l3["u"] is not None and n3 >= args.nbisekt2_min:
                    l3, info3["stufe3b"] = nachschaerfen(l3, "T", t_halb3b)
                    s3, sattel3 = sattel_info(l3)
                    d = np.sin(l3["u"][1][fr] - pM[fr])
                    s3["unten_ende_D_zu_M"] = float((d * d).max())
                    s3["unten_ende_gleich_M"] = bool(l3["u"][3] == "M" and s3["unten_ende_D_zu_M"] <= args.eps_s)
                    info3["sattel2"] = s3
                    if l3["u"][3] == "S":
                        aus["weg_art"] = "S -> Sattel 2 -> T (unten S)"
                        pfad = [qS, q_(l3["u"][2][1]), q_(l3["o"][2][1])]
                        barriere, genau, sattel, pfad_ok = s3["barriere"], s3["genau"], sattel3, True
                    elif s3["unten_ende_gleich_M"]:
                        aus["weg_art"] = "S -> Sattel 1 -> M -> Sattel 2 -> T"
                        pfad += [q_(l3["u"][2][1]), q_(l3["o"][2][1])]
                        barriere = max(s1["barriere"], s3["barriere"])
                        sattel = sattel1 if s1["E_sattel"] >= s3["E_sattel"] else sattel3
                        genau, pfad_ok = bool(s1["genau"] and s3["genau"]), True
                    ende = l3["o"][1]
            aus["stufe3"] = info3
        aus["barriere"] = float(barriere)
        aus["genau"] = bool(genau)
        aus["pfad_ok"] = bool(pfad_ok)
        aus["lokalisierung"] = lokal2(netz, q_(sattel), qS)
        np.savez_compressed(os.path.join(args.aus, "bisekt-%s.npz" % gtag(args.r0, args.R)),
                            Z=np.stack(pfad + [q_(ende)]))

        def stopp_frei(it, E, p, fmax):
            if E < args.e_T:
                return "T", False
            if fmax <= args.ftol_ruhe:
                return "ruhe", False
            if wand() > args.budget:
                return "zeit", False
            return None, False

        kl2, p2, it2, _, E2, fm2, Emax2, cl2 = fire_psi(eb, ende.copy(), args.nfrei, stopp_frei,
                                                        dtmax=args.dtmax, merke=False)
        kl2 = kl2 if kl2 is not None else "nmax"
        c2 = np.cos(p2[netz.a] - p2[netz.b])
        aus["freigabe"] = {"klasse": kl2, "schritte": it2, "E_end": E2, "fmax_end": fm2, "E_max": Emax2,
                           "T_erreicht": kl2 == "T", "zwischenminimum": kl2 == "ruhe",
                           "E_max_unter_ES": bool(Emax2 < ES), "bindungen_c_le_0_ende": int((c2 <= 0).sum()),
                           "t": wand()}
        np.savez_compressed(os.path.join(args.aus, "freigabe-%s.npz" % gtag(args.r0, args.R)), q=q_(p2))
        aus["gueltig_A_ohne_S"] = bool(aus["lambda1_klasse"] in ("T", "M") and n_halb >= args.nbisekt_min
                                       and pfad_ok and genau and aus["freigabe"]["T_erreicht"]
                                       and aus["freigabe"]["E_max_unter_ES"])
    else:
        aus["gueltig_A_ohne_S"] = False
    alle_sch = (schritte + (aus["stufe2"].get("schritte") or []) + (aus["stufe3"].get("schritte") or [])
                + ((aus["stufe3"].get("stufe3b") or {}).get("schritte") or []))
    aus["zahl_M"] = int(sum(1 for s in alle_sch if s["klasse"] == "M"))
    aus["zahl_offen"] = int(sum(1 for s in alle_sch if s["klasse"] == "offen"))
    aus["laufzeit_s"] = time.time() - t0
    aus["maxrss_mb"] = maxrss_mb()
    g2.schreibe_json(os.path.join(args.aus, "bisekt-%s.json" % gtag(args.r0, args.R)), aus)
    print("bisekt fertig %s laufzeit %.1f s" % (gtag(args.r0, args.R), aus["laufzeit_s"]))


# ---------------------------------------------------------------- Verfahren B (PLAN Abschnitt 4)

def modus_weg(args):
    t0 = time.time()
    rng = np.random.default_rng([49, 1, int(round(args.R))])
    netz = finn.Netz("diamant", args.r0, args.R, "so3")
    qS = np.load(args.start)["q"]
    ES, _, _ = netz.energie(qS[:, None, :], grad=False)
    ES = float(ES[0])
    Z = np.load(args.zugpfad)["Z"]
    X = np.ascontiguousarray(g2.reparam_feld(Z, args.M + 2, netz.frei, z2.normP_fn(netz)))
    X[0] = Z[0]
    X[-1] = Z[-1]
    innen = np.ascontiguousarray(X[1:-1].transpose(1, 0, 2))
    innen = netz.rauschen(innen, rng, args.sigma)
    X[1:-1] = innen.transpose(1, 0, 2)
    del Z
    X, erg = z2.wegrechnung(netz, X, args, "neb")
    E = np.asarray(erg["E_profil"])
    tag = "weg-haupt-%s-neb" % gtag(args.r0, args.R)
    aus = {"kopf": kopf(args), "netz_info": netz.info(), "weg": erg, "E_S": ES, "E_0": float(E[0]),
           "E_ende": float(E[-1])}
    ki = erg["ki"]
    if ki > 0:
        aus["E_sattel"] = float(E[ki])
        aus["barriere"] = float(E[ki] - ES)
        aus["lokalisierung"] = lokal2(netz, X[ki], qS)
        aus["kletterbild_eben_rest"] = float(np.abs(X[ki][netz.frei][:, 1:3]).max())
        np.savez_compressed(os.path.join(args.aus, tag + "-kletterbild.npz"), q=X[ki])
    else:
        aus["E_sattel"] = None
        aus["barriere"] = None
    aus["laufzeit_s"] = time.time() - t0
    aus["maxrss_mb"] = maxrss_mb()
    g2.schreibe_json(os.path.join(args.aus, tag + ".json"), aus)
    print("weg fertig %s iterationen %d grund %s laufzeit %.1f s" % (tag, erg["iterationen"], erg["grund"],
                                                                      aus["laufzeit_s"]))


# ---------------------------------------------------------------- Konsistenzprobe (PLAN Abschnitt 8)

def modus_pruef(args):
    t0 = time.time()
    netz = finn.Netz("diamant", args.r0, args.R, "so3")
    eb = Eben(netz)
    fr = netz.frei
    if args.start:
        qS = np.load(args.start)["q"]
    else:
        x = np.zeros((netz.N, 1, 4))
        x[:, 0, 0] = np.cos(np.pi * netz.h)
        x[:, 0, 3] = np.sin(np.pi * netz.h)
        qS = netz.setze(x, 2.0 * np.pi)[:, 0]
    pS = np.arctan2(qS[:, 3], qS[:, 0])
    w = kappe_w(netz, args)
    p0 = pS * (1.0 - args.lam * w)
    q0 = q_aus_psi(p0, qS, netz)
    Eq, Gq, _ = netz.energie(q0[:, None, :])
    Fq = -netz.tang(Gq, q0[:, None, :])[:, 0]
    epsi = np.zeros_like(q0)
    epsi[:, 0] = -np.sin(p0)
    epsi[:, 3] = np.cos(p0)
    Fq_psi = (Fq * epsi).sum(-1)
    Ep, Gp, _ = eb.energie(p0)
    Fp = np.where(fr, -Gp, 0.0)
    aus = {"kopf": kopf(args), "netz_info": netz.info(),
           "rel_diff_E": abs(Ep - float(Eq[0])) / max(abs(float(Eq[0])), 1e-300),
           "max_diff_F": float(np.abs(Fp - Fq_psi).max()), "max_F": float(np.abs(Fp).max()),
           "max_F_quer": float(np.sqrt(((Fq - Fq_psi[:, None] * epsi) ** 2).sum(-1)).max())}
    # n Schritte Quaternion-FIRE (z2.fire_stopp, Arithmetik finn.fire_feld) gegen psi-FIRE
    n = args.nschritt
    t1 = time.time()
    xq, Eqn, fmq, itq, _, _, _, _ = z2.fire_stopp(netz, q0[:, None, :].copy(), n, 1e-12, args.dtmax, lambda e: False)
    tq = (time.time() - t1) / max(n, 1)
    t1 = time.time()
    _, pn, itp, _, Epn, fmp, _, _ = fire_psi(eb, p0.copy(), n, lambda it, E, p, f: (None, False), dtmax=args.dtmax,
                                             merke=False)
    tp = (time.time() - t1) / max(n, 1)
    pq = np.arctan2(xq[:, 0, 3], xq[:, 0, 0])
    aus.update({"schritte_quat": itq, "schritte_psi": itp, "max_abw_psi_sin": float(np.abs(np.sin(pq - pn)[fr]).max()),
                "rel_diff_E_nach": abs(Epn - Eqn) / max(abs(Eqn), 1e-300),
                "fmax_quat_nach": fmq, "fmax_psi_nach": fmp,
                "quat_eben_rest": float(np.abs(xq[:, 0, 1:3]).max()),
                "s_je_schritt_quat": tq, "s_je_schritt_psi": tp, "laufzeit_s": time.time() - t0,
                "maxrss_mb": maxrss_mb()})
    g2.schreibe_json(os.path.join(args.aus, "pruef-%s.json" % gtag(args.r0, args.R)), aus)
    print("pruef fertig %s laufzeit %.1f s" % (gtag(args.r0, args.R), aus["laufzeit_s"]))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("modus", choices=["start", "bisekt", "weg", "pruef"])
    p.add_argument("--aus", default=".")
    p.add_argument("--r0", type=float, default=10.0)
    p.add_argument("--R", type=float, default=20.0)
    p.add_argument("--start", default="")
    p.add_argument("--zugpfad", default="")
    # Start
    p.add_argument("--nmax", type=int, default=20000)
    p.add_argument("--ftol", type=float, default=1.0e-7)
    p.add_argument("--dtmax", type=float, default=0.1)
    p.add_argument("--budget", type=float, default=540.0)
    p.add_argument("--k", type=int, default=4)
    p.add_argument("--tol", type=float, default=1.0e-9)
    p.add_argument("--maxiter", type=int, default=200000)
    # Bisektion
    p.add_argument("--kappe_b", type=float, default=30.0)
    p.add_argument("--d_grad", type=float, default=30.0)
    p.add_argument("--delta_k", type=float, default=1.0)
    p.add_argument("--eps_s", type=float, default=1.0e-3)
    p.add_argument("--d_sattel", type=float, default=0.5)
    p.add_argument("--nskip", type=int, default=30)
    p.add_argument("--nbis", type=int, default=1500)
    p.add_argument("--nbisekt", type=int, default=14)
    p.add_argument("--nbisekt_min", type=int, default=10)
    p.add_argument("--halb_anteil", type=float, default=0.45)
    p.add_argument("--halb2_anteil", type=float, default=0.55)
    p.add_argument("--halb3_anteil", type=float, default=0.65)
    p.add_argument("--halb3b_anteil", type=float, default=0.72)
    p.add_argument("--nbisekt2", type=int, default=12)
    p.add_argument("--nbisekt2_min", type=int, default=6)
    p.add_argument("--fmin_max", type=float, default=0.05)
    p.add_argument("--ftol_m", type=float, default=1.0e-9)
    p.add_argument("--f_ruhe_bereich", type=float, default=1.0e-6)
    p.add_argument("--bahn_anteil", type=float, default=0.78)
    p.add_argument("--e_T", type=float, default=1.0e-3)
    p.add_argument("--ftol_ruhe", type=float, default=1.0e-6)
    p.add_argument("--nfrei", type=int, default=30000)
    # CI-NEB (Namen wie z2.main, weil z2.wegrechnung sie liest)
    p.add_argument("--M", type=int, default=6)
    p.add_argument("--sigma", type=float, default=1.0e-3)
    p.add_argument("--ks", type=float, default=1.0)
    p.add_argument("--nvor", type=int, default=50)
    p.add_argument("--ftol_ci", type=float, default=5.0e-3)
    p.add_argument("--ftol_band", type=float, default=1.0)
    p.add_argument("--dtstart", type=float, default=0.02)
    p.add_argument("--capw", type=float, default=0.05)
    # Pruefung
    p.add_argument("--lam", type=float, default=0.5)
    p.add_argument("--nschritt", type=int, default=60)
    args = p.parse_args()
    if args.modus == "weg" and args.budget == 540.0:
        args.budget = 480.0
    os.makedirs(args.aus, exist_ok=True)
    {"start": modus_start, "bisekt": modus_bisekt, "weg": modus_weg, "pruef": modus_pruef}[args.modus](args)


if __name__ == "__main__":
    main()
