#!/usr/bin/env python3
"""FADEN-DIM-1 (Runde 43): gewickelte Faeden (Windung +1 und -1 um Richtung 1) auf dem
hyperkubischen Torus Z_L^D, D = 2..6. Treffen = gemeinsamer Knoten (dann Vernichtung).

Modi (nur ueber kleintest.sh auf der .69):
  rauch                               kleine Zellen, gibt NUR Laufzeiten aus
  lauf --zellen Z1,Z2,... --out F     rechnet Zellen, haengt je Zelle eine JSON-Zeile an F an
  auswertung --ein F1,F2,... --out-json A --out-txt B
  bild --ein A --out PNG
Zelle: DYN:D:L:P:N, DYN in {G, RL, RP}; P = Ziel-Knickdichte (0 fuer G); N = Zahl der Paare.
  G  = glatt: starre gerade Faeden, je Schritt Verschiebung von A, dann von B in eine zufaellige Querrichtung.
  RL = rau, nur lokale Metropolis-Zuege (Kartenwortlaut); 1 Schritt = 1 Sweep (jede Spalte jedes Fadens 1 Versuch).
  RP = rau, wie RL plus je Schritt eine starre Verschiebung je Faden wie in G (Plan); P -> 0 ergibt G.

Faden-Darstellung (gerichtete RSOS-Faeden, Windung um Richtung 1):
  y[x] (x = 0..L-1): Querlage in Spalte x als flacher Index in Z_L^(D-1).
  c[x]: Schrittcode von Spalte x nach x+1 (0 = gerade, 1+m = Einheitsschritt m; m = 2j + (0: +e_j, 1: -e_j)).
  Weg: (x, y[x]) -> (x, y[x+1]) -> (x+1, y[x+1]); Knoten in Spalte x: y[x] und y[x+1].
  Treffen in Spalte x: {yA[x], yA[x+1]} und {yB[x], yB[x+1]} schneiden sich.
  Energie E = J * K (K = Zahl der Knicke, je Knick zwei 90-Grad-Biegungen, J = 2 kappa).
  Ziel-Knickdichte p: exp(-J) = p / (2 (D-1) (1-p)), also J = ln(2 (D-1) (1-p) / p).
"""
import sys
import json
import time
import math
import argparse
import numpy as np

SEED = 20261004
C_T = 4               # T = C_T * L^2 Schritte
T_GRENZE = 560.0      # Sekunden je Prozess; danach Zelle als abgebrochen markieren
DYN_CODE = {"G": 1, "RL": 2, "RP": 3}


def nb_table(dp, L):
    n = L ** dp
    idx = np.arange(n, dtype=np.int64)
    NB = np.empty((n, 2 * dp), dtype=np.int64)
    for j in range(dp):
        pj = L ** j
        yj = (idx // pj) % L
        NB[:, 2 * j] = idx + (((yj + 1) % L) - yj) * pj
        NB[:, 2 * j + 1] = idx + (((yj - 1) % L) - yj) * pj
    return NB.astype(np.int32)


def code_tables(dp):
    M = 2 * dp
    ADD = np.full((M + 1, M), -1, dtype=np.int8)
    for cc in range(M + 1):
        for m in range(M):
            if cc == 0:
                ADD[cc, m] = 1 + m
            elif (cc - 1) == (m ^ 1):
                ADD[cc, m] = 0
    SUB = np.empty_like(ADD)
    for m in range(M):
        SUB[:, m] = ADD[:, m ^ 1]
    return ADD, SUB


def sample_bridges(rng, n, L, dp, p):
    """n geschlossene RSOS-Bruecken (Schrittcodes, Summe der Schrittvektoren = 0); exakte Gleichgewichtsform."""
    out = np.empty((n, L), dtype=np.int8)
    if p <= 0:
        out[:] = 0
        return out
    M = 2 * dp
    got = 0
    while got < n:
        nb = int(min(max(4096, 200 * (n - got)), 4_000_000 // L + 1))
        kink = rng.random((nb, L)) < p
        m = rng.integers(0, M, size=(nb, L))
        codes = np.where(kink, 1 + m, 0).astype(np.int8)
        ok = np.ones(nb, dtype=bool)
        for j in range(dp):
            bal = (codes == 1 + 2 * j).sum(axis=1) - (codes == 2 + 2 * j).sum(axis=1)
            ok &= (bal == 0)
        acc = codes[ok][: n - got]
        out[got: got + acc.shape[0]] = acc
        got += acc.shape[0]
    return out


def build_y(codes, off, NB):
    n, L = codes.shape
    y = np.empty((n, L), dtype=np.int32)
    y[:, 0] = off
    for x in range(L - 1):
        cc = codes[:, x].astype(np.int64)
        nxt = NB[y[:, x], np.maximum(cc - 1, 0)]
        y[:, x + 1] = np.where(cc > 0, nxt, y[:, x])
    return y


def treffen(yA, yB):
    yA1 = np.roll(yA, -1, axis=1)
    yB1 = np.roll(yB, -1, axis=1)
    return ((yA == yB) | (yA == yB1) | (yA1 == yB)).any(axis=1)


def init_R(rng, n, L, dp, p, NB):
    nsite = L ** dp
    cA = sample_bridges(rng, n, L, dp, p)
    yA = build_y(cA, rng.integers(0, nsite, n), NB)
    cB = sample_bridges(rng, n, L, dp, p)
    yB = build_y(cB, rng.integers(0, nsite, n), NB)
    bad = treffen(yA, yB)
    nres = 0
    it = 0
    while bad.any():
        it += 1
        if it > 2000:
            raise RuntimeError("Startlage: Faeden ueberlappen zu oft")
        k = int(bad.sum())
        nres += k
        cB[bad] = sample_bridges(rng, k, L, dp, p)
        yB[bad] = build_y(cB[bad], rng.integers(0, nsite, k), NB)
        bad = treffen(yA, yB)
    return cA, yA, cB, yB, nres


def halbsweep(rng, y, c, q, L, M, NB, ADD, SUB, ACC):
    n = y.shape[0]
    xs = np.arange(q, L, 2)
    xl = (xs - 1) % L
    m = rng.integers(0, M, size=(n, xs.size))
    cl = c[:, xl]
    cr = c[:, xs]
    cl2 = ADD[cl, m]
    cr2 = SUB[cr, m]
    ok = (cl2 >= 0) & (cr2 >= 0)
    dK = ((cl2 != 0).astype(np.int8) + (cr2 != 0).astype(np.int8)
          - (cl != 0).astype(np.int8) - (cr != 0).astype(np.int8))
    acc = ok & (rng.random((n, xs.size)) < ACC[dK + 2])
    yx = y[:, xs]
    y[:, xs] = np.where(acc, NB[yx, m], yx)
    c[:, xl] = np.where(acc, cl2, cl)
    c[:, xs] = np.where(acc, cr2, cr)
    return int(acc.sum()), int(acc.size)


def starr(rng, y, M, NB):
    m = rng.integers(0, M, size=y.shape[0])
    y[:] = NB[y, m[:, None]]


def run_R(dyn, D, L, p, n, rng, t_start):
    assert L % 2 == 0 and L >= 4
    dp = D - 1
    M = 2 * dp
    NB = nb_table(dp, L)
    ADD, SUB = code_tables(dp)
    J = math.log(2 * dp * (1 - p) / p)
    ACC = np.array([min(1.0, math.exp(-J * d)) for d in range(-2, 3)])
    cA, yA, cB, yB, nres = init_R(rng, n, L, dp, p, NB)
    p_start = float(((cA != 0).mean() + (cB != 0).mean()) / 2)
    T = C_T * L * L
    nsub = 6 if dyn == "RP" else 4
    ids = np.arange(n)
    tmeet = np.full(n, np.nan)
    nacc = 0
    natt = 0
    abgebrochen = False
    t_done = 0
    for t in range(T):
        k = 0
        schritte = []
        if dyn == "RP":
            schritte += [("s", 0), ("s", 1)]
        schritte += [("h", 0, 0), ("h", 1, 0), ("h", 0, 1), ("h", 1, 1)]
        for sch in schritte:
            k += 1
            if sch[0] == "s":
                starr(rng, yA if sch[1] == 0 else yB, M, NB)
            else:
                if sch[1] == 0:
                    a, b = halbsweep(rng, yA, cA, sch[2], L, M, NB, ADD, SUB, ACC)
                else:
                    a, b = halbsweep(rng, yB, cB, sch[2], L, M, NB, ADD, SUB, ACC)
                nacc += a
                natt += b
            h = treffen(yA, yB)
            if h.any():
                tmeet[ids[h]] = t + k / nsub
                keep = ~h
                ids = ids[keep]
                yA = yA[keep]
                yB = yB[keep]
                cA = cA[keep]
                cB = cB[keep]
                if ids.size == 0:
                    break
        t_done = t + 1
        if ids.size == 0:
            break
        if (t & 63) == 0 and time.time() - t_start > T_GRENZE:
            abgebrochen = True
            break
    p_end = float(((cA != 0).mean() + (cB != 0).mean()) / 2) if ids.size else None
    extra = {"J": J, "kappa": J / 2, "p_start": p_start, "p_end_rest": p_end,
             "akzeptanz_lokal": nacc / max(natt, 1), "n_neu_gezogen_start": nres,
             "schritte_gerechnet": t_done}
    return tmeet, T, abgebrochen, extra


def run_G(D, L, n, rng, t_start):
    dp = D - 1
    T = C_T * L * L
    S = 2 * T
    off = rng.integers(0, L, size=(n, dp))
    z = (off == 0).all(axis=1)
    while z.any():
        off[z] = rng.integers(0, L, size=(int(z.sum()), dp))
        z = (off == 0).all(axis=1)
    pos = off.astype(np.int64)
    ids = np.arange(n)
    tmeet = np.full(n, np.nan)
    done = 0
    abgebrochen = False
    while done < S and ids.size:
        na = ids.size
        k = int(min(S - done, max(16, (1 << 23) // (na * dp))))
        dirs = rng.integers(0, dp, size=(na, k))
        sg = rng.integers(0, 2, size=(na, k)) * 2 - 1
        hit = np.ones((na, k), dtype=bool)
        newpos = np.empty_like(pos)
        for j in range(dp):
            st = np.where(dirs == j, sg, 0)
            pj = (pos[:, j:j + 1] + np.cumsum(st, axis=1)) % L
            hit &= (pj == 0)
            newpos[:, j] = pj[:, -1]
        h = hit.any(axis=1)
        first = hit.argmax(axis=1)
        tmeet[ids[h]] = (done + first[h] + 1) / 2.0
        pos = newpos[~h]
        ids = ids[~h]
        done += k
        if time.time() - t_start > T_GRENZE:
            abgebrochen = done < S and ids.size > 0
            break
    extra = {"J": None, "kappa": None, "p_start": 0.0, "p_end_rest": 0.0,
             "akzeptanz_lokal": None, "n_neu_gezogen_start": 0, "schritte_gerechnet": done / 2.0}
    return tmeet, T, abgebrochen, extra


def parse_zelle(z):
    dyn, D, L, p, n = z.split(":")
    return dyn, int(D), int(L), float(p), int(n)


def rechne_zelle(z, t_start):
    dyn, D, L, p, n = parse_zelle(z)
    rng = np.random.default_rng([SEED, DYN_CODE[dyn], D, L, int(round(p * 1000)), n])
    t0 = time.time()
    if dyn == "G":
        tmeet, T, ab, extra = run_G(D, L, n, rng, t_start)
    else:
        tmeet, T, ab, extra = run_R(dyn, D, L, p, n, rng, t_start)
    dt = time.time() - t0
    met = ~np.isnan(tmeet)
    tm = tmeet[met]
    rec = {"zelle": z, "dyn": dyn, "D": D, "L": L, "p": p, "n": n, "T": T, "c": C_T,
           "treffer": int(met.sum()), "abgebrochen": bool(ab), "laufzeit_s": round(dt, 3)}
    rec.update(extra)
    rec["t_treffen"] = [round(float(v), 3) for v in np.sort(tm)]
    return rec


def zeitprobe(z, nschritte):
    """Feste Schrittzahl ohne Entfernen getroffener Paare: misst nur Kosten, zeigt keine Treffer."""
    dyn, D, L, p, n = parse_zelle(z)
    rng = np.random.default_rng([SEED, 7, D, L, n])
    dp = D - 1
    M = 2 * dp
    t0 = time.time()
    if dyn == "G":
        pos = rng.integers(0, L, size=(n, dp)).astype(np.int64)
        k = 2 * nschritte
        dirs = rng.integers(0, dp, size=(n, k))
        sg = rng.integers(0, 2, size=(n, k)) * 2 - 1
        hit = np.ones((n, k), dtype=bool)
        for j in range(dp):
            st = np.where(dirs == j, sg, 0)
            pj = (pos[:, j:j + 1] + np.cumsum(st, axis=1)) % L
            hit &= (pj == 0)
        _ = hit.any(axis=1)
        return 0.0, (time.time() - t0) / (n * nschritte * dp) * 1e9
    NB = nb_table(dp, L)
    ADD, SUB = code_tables(dp)
    J = math.log(2 * dp * (1 - p) / p)
    ACC = np.array([min(1.0, math.exp(-J * d)) for d in range(-2, 3)])
    cA, yA, cB, yB, nres = init_R(rng, n, L, dp, p, NB)
    t_init = time.time() - t0
    t1 = time.time()
    for t in range(nschritte):
        if dyn == "RP":
            starr(rng, yA, M, NB)
            _ = treffen(yA, yB)
            starr(rng, yB, M, NB)
            _ = treffen(yA, yB)
        for (s, q) in [(0, 0), (1, 0), (0, 1), (1, 1)]:
            if s == 0:
                halbsweep(rng, yA, cA, q, L, M, NB, ADD, SUB, ACC)
            else:
                halbsweep(rng, yB, cB, q, L, M, NB, ADD, SUB, ACC)
            _ = treffen(yA, yB)
    return t_init, (time.time() - t1) / (n * nschritte * L) * 1e9


def modus_rauch():
    proben = [("G:6:10:0:65536", 200), ("G:2:1000:0:1024", 2000),
              ("RL:2:64:0.6:256", 200), ("RP:2:64:0.6:256", 200),
              ("RL:3:64:0.6:256", 200), ("RP:3:100:0.6:256", 100), ("RP:3:100:0.2:256", 100),
              ("RL:4:32:0.6:1024", 100), ("RP:4:32:0.6:1024", 100),
              ("RL:5:16:0.6:4096", 100), ("RP:5:16:0.6:4096", 100),
              ("RL:6:10:0.6:8192", 100), ("RP:6:10:0.6:8192", 100), ("RP:6:4:0.2:8192", 200)]
    t_start = time.time()
    for z, ns in proben:
        ti, ns_el = zeitprobe(z, ns)
        print(f"rauch {z}: start {ti:.2f} s, {ns_el:.1f} ns je (Paar*Schritt*Spalte) [G: je Paar*Schritt*Querrichtung]",
              flush=True)
    print(f"rauch gesamt {time.time() - t_start:.1f} s", flush=True)


def modus_lauf(zellen, out):
    t_start = time.time()
    for z in zellen:
        rec = rechne_zelle(z, t_start)
        with open(out, "a") as f:
            f.write(json.dumps(rec) + "\n")
        print(f"{z} fertig, {rec['laufzeit_s']:.1f} s, abgebrochen={rec['abgebrochen']}", flush=True)
        if rec["abgebrochen"]:
            print("Zeitgrenze erreicht, Rest nicht gerechnet", flush=True)
            break
    print(f"lauf gesamt {time.time() - t_start:.1f} s", flush=True)


# ---------------------------------------------------------------- Auswertung
S_PLAN = -0.25        # Plan: "faellt" heisst Steigung < -0,25 und obere 95-%-Grenze < 0
S_MIN_STRENG = -0.01  # Kartenwortlaut (streng): obere 95-%-Grenze < 0 und Steigung < -0,01
NBOOT = 2000


def wilson(h, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    ph = h / n
    den = 1 + z * z / n
    cen = (ph + z * z / (2 * n)) / den
    hw = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / den
    return (cen - hw, cen + hw)


def fit_steigung(Ls, hits, ns):
    X = np.log(np.asarray(Ls, float))
    n = np.asarray(ns, float)
    P = (np.asarray(hits, float) + 0.5) / (n + 1.0)
    w = n * P / (1.0 - P)
    W = w / w.sum()
    xm = (W * X).sum()
    Y = np.log(P)
    ym = (W * Y).sum()
    return float((W * (X - xm) * (Y - ym)).sum() / (W * (X - xm) ** 2).sum())


def steigung_mit_ci(Ls, hits, ns, rng):
    s0 = fit_steigung(Ls, hits, ns)
    n = np.asarray(ns)
    ph = np.asarray(hits, float) / n
    bs = np.array([fit_steigung(Ls, rng.binomial(n, ph), ns) for _ in range(NBOOT)])
    lo, hi = np.percentile(bs, [2.5, 97.5])
    return s0, float(lo), float(hi)


def dstern(faellt):
    Ds = sorted(faellt)
    ds = None
    for D in Ds:
        if all(faellt[E] for E in Ds if E >= D):
            ds = D
            break
    fall_set = [D for D in Ds if faellt[D]]
    monoton = (ds is None and not fall_set) or (ds is not None and fall_set == [E for E in Ds if E >= ds])
    return ds, monoton


def modus_auswertung(ein, out_json, out_txt):
    recs = []
    for f in ein:
        with open(f) as fh:
            for line in fh:
                line = line.strip()
                if line:
                    recs.append(json.loads(line))
    rng = np.random.default_rng([SEED, 99])
    zellen = {}
    for r in recs:
        key = (r["dyn"], r["p"], r["D"], r["L"])
        if key in zellen:
            raise RuntimeError(f"Zelle doppelt: {key}")
        zellen[key] = r
    serien = sorted({(k[0], k[1]) for k in zellen})
    erg = {"zellen": [], "serien": {}, "urteile": {}}
    for k in sorted(zellen):
        r = zellen[k]
        P = r["treffer"] / r["n"]
        lo, hi = wilson(r["treffer"], r["n"])
        tt = r["t_treffen"]
        erg["zellen"].append({"dyn": r["dyn"], "p": r["p"], "D": r["D"], "L": r["L"], "n": r["n"],
                              "treffer": r["treffer"], "P": P, "P_lo": lo, "P_hi": hi,
                              "t_median_durch_L2": (float(np.median(tt)) / r["L"] ** 2) if tt else None,
                              "t_mittel_durch_L2": (float(np.mean(tt)) / r["L"] ** 2) if tt else None,
                              "p_start": r["p_start"], "p_end_rest": r["p_end_rest"],
                              "akzeptanz_lokal": r["akzeptanz_lokal"], "kappa": r["kappa"],
                              "abgebrochen": r["abgebrochen"], "laufzeit_s": r["laufzeit_s"]})
    for (dyn, p) in serien:
        sd = {}
        for D in range(2, 7):
            ks = sorted(k for k in zellen if k[0] == dyn and k[1] == p and k[2] == D and not zellen[k]["abgebrochen"])
            if len(ks) < 2:
                continue
            Ls = [k[3] for k in ks]
            hits = [zellen[k]["treffer"] for k in ks]
            ns = [zellen[k]["n"] for k in ks]
            s0, lo, hi = steigung_mit_ci(Ls, hits, ns, rng)
            sd[D] = {"L": Ls, "treffer": hits, "n": ns, "steigung": s0, "s_lo": lo, "s_hi": hi,
                     "faellt_plan": bool(s0 < S_PLAN and hi < 0),
                     "faellt_streng": bool(s0 < S_MIN_STRENG and hi < 0)}
        ser = {"D": {str(D): v for D, v in sd.items()}}
        if sorted(sd) == [2, 3, 4, 5, 6]:
            dp_, mp = dstern({D: sd[D]["faellt_plan"] for D in sd})
            ds_, ms = dstern({D: sd[D]["faellt_streng"] for D in sd})
            ser["Dstern_fall_plan"] = dp_
            ser["Dgrenze_plan"] = (dp_ - 1) if dp_ is not None else ">=6"
            ser["monoton_plan"] = mp
            ser["Dstern_fall_streng"] = ds_
            ser["monoton_streng"] = ms
        else:
            ser["unvollstaendig"] = sorted(sd)
        erg["serien"][f"{dyn}:{p}"] = ser
    # ---------------- Urteile
    U = {}
    g = erg["serien"].get("G:0.0", {}).get("D", {})
    # F1 nach Plan: (a) D = 3: P_G >= 0,8 bei allen L; (b) D = 4: Steigung in [-1,3; -0,6]
    try:
        a = all(zellen[k]["treffer"] / zellen[k]["n"] >= 0.8 for k in zellen if k[0] == "G" and k[2] == 3)
        b = -1.3 <= g["4"]["steigung"] <= -0.6
        U["F1_plan"] = {"a_D3_alle_L_ge_0.8": a, "b_D4_steigung_in_-1.3_-0.6": b,
                        "urteil": "eingetroffen" if (a and b) else ("teilweise" if (a or b) else "nicht eingetroffen")}
    except KeyError as e:
        U["F1_plan"] = {"urteil": f"nicht auswertbar ({e})"}
    # F1 nach Kartenwortlaut: (a) D = 3, L = 100: P_G >= 0,8 ("~ 1"); (b) D = 4: P*L konstant bis Faktor 1,5 ("~ w/L")
    try:
        k3 = ("G", 0.0, 3, 100)
        a = zellen[k3]["treffer"] / zellen[k3]["n"] >= 0.8
        PL = [zellen[k]["treffer"] / zellen[k]["n"] * k[3] for k in sorted(zellen) if k[0] == "G" and k[2] == 4]
        b = (min(PL) > 0) and (max(PL) / min(PL) <= 1.5)
        U["F1_karte"] = {"a_D3_L100_ge_0.8": a, "b_D4_PL_faktor_le_1.5": b,
                         "PL_D4": PL,
                         "urteil": "eingetroffen" if (a and b) else ("teilweise" if (a or b) else "nicht eingetroffen")}
    except KeyError as e:
        U["F1_karte"] = {"urteil": f"nicht auswertbar ({e})"}
    # F2 nach Plan: RP, rauheste Stufe p = 0,6: D_grenze in {4, 5}
    def gr(key):
        s = erg["serien"].get(key, {})
        return s.get("Dgrenze_plan")
    rp = {key: gr(key) for key in erg["serien"] if key.startswith("RP:")}
    g06 = gr("RP:0.6")
    if g06 is None:
        f2p = "nicht auswertbar"
    elif g06 in (4, 5):
        f2p = "eingetroffen"
    elif all((v is not None and v != ">=6" and v <= 3) for v in rp.values()):
        f2p = "nicht eingetroffen"
    elif g06 == ">=6" or (isinstance(g06, int) and g06 >= 6):
        f2p = "nicht eingetroffen (Grenze ueber 5)"
    else:
        f2p = "uneindeutig"
    U["F2_plan"] = {"Dgrenze_RP": rp, "Dgrenze_G": gr("G:0.0"), "urteil": f2p}
    # F2 nach Kartenwortlaut: RL, p = 0,6: D* ("ab ihr faellt", streng) in {4, 5}; Bezug G (streng)
    srl = erg["serien"].get("RL:0.6", {})
    dsk = srl.get("Dstern_fall_streng", "fehlt")
    if dsk == "fehlt":
        f2k = "nicht auswertbar"
    elif dsk in (4, 5):
        f2k = "eingetroffen"
    else:
        f2k = "nicht eingetroffen"
    U["F2_karte"] = {"Dstern_streng_RL_0.6": dsk,
                     "Dstern_streng_G": erg["serien"].get("G:0.0", {}).get("Dstern_fall_streng"),
                     "urteil": f2k}
    erg["urteile"] = U
    with open(out_json, "w") as f:
        json.dump(erg, f, indent=1)
    # Textfassung
    lines = []
    lines.append("FADEN-DIM-1 Auswertung (eingefrorener Code)")
    lines.append("")
    lines.append("Treffanteil P je Zelle (Wilson-95-%), Median Treffzeit / L^2, Knickdichte Start/Ende, Akzeptanz")
    for z in erg["zellen"]:
        tm = z["t_median_durch_L2"]
        lines.append(f"{z['dyn']:>2} p={z['p']:.2f} D={z['D']} L={z['L']:>4} n={z['n']:>6} treffer={z['treffer']:>6} "
                     f"P={z['P']:.4f} [{z['P_lo']:.4f},{z['P_hi']:.4f}] tmed/L2={'-' if tm is None else f'{tm:.4f}'} "
                     f"p0={z['p_start']:.3f} pE={z['p_end_rest']} acc={z['akzeptanz_lokal']} ab={z['abgebrochen']}")
    lines.append("")
    lines.append("Steigung d lnP / d lnL je Serie und D (Bootstrap-95-%)")
    for key, ser in erg["serien"].items():
        for D, v in ser["D"].items():
            lines.append(f"{key:>8} D={D}: s={v['steigung']:+.3f} [{v['s_lo']:+.3f},{v['s_hi']:+.3f}] "
                         f"faellt_plan={v['faellt_plan']} faellt_streng={v['faellt_streng']}")
        lines.append(f"{key:>8} D*_fall_plan={ser.get('Dstern_fall_plan')} D_grenze_plan={ser.get('Dgrenze_plan')} "
                     f"monoton_plan={ser.get('monoton_plan')} D*_fall_streng={ser.get('Dstern_fall_streng')} "
                     f"monoton_streng={ser.get('monoton_streng')} unvollst={ser.get('unvollstaendig')}")
    lines.append("")
    lines.append("Urteile")
    for k, v in U.items():
        lines.append(f"{k}: {json.dumps(v)}")
    with open(out_txt, "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines[-6:]), flush=True)


def modus_bild(ein, out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    with open(ein) as f:
        erg = json.load(f)
    stil = {"G:0.0": ("G glatt", "#222222", "o"),
            "RP:0.2": ("RP rau p=0,2 (Plan)", "#6baed6", "s"),
            "RP:0.6": ("RP rau p=0,6 (Plan)", "#08519c", "s"),
            "RL:0.2": ("RL rau p=0,2 (Karte)", "#fdae6b", "^"),
            "RL:0.6": ("RL rau p=0,6 (Karte)", "#d94801", "^")}
    fig, axs = plt.subplots(2, 3, figsize=(15, 9))
    for i, D in enumerate(range(2, 7)):
        ax = axs.flat[i]
        for key, (lab, col, mk) in stil.items():
            dyn, p = key.split(":")
            zs = [z for z in erg["zellen"] if z["dyn"] == dyn and abs(z["p"] - float(p)) < 1e-9 and z["D"] == D]
            if not zs:
                continue
            zs.sort(key=lambda z: z["L"])
            L = np.array([z["L"] for z in zs], float)
            P = np.array([max(z["P"], 1e-4) for z in zs])
            lo = np.array([max(z["P_lo"], 1e-4) for z in zs])
            hi = np.array([z["P_hi"] for z in zs])
            ax.errorbar(L, P, yerr=[np.maximum(P - lo, 0), np.maximum(hi - P, 0)], color=col, marker=mk,
                        label=lab, capsize=2, lw=1.2, ms=4)
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_ylim(1e-4, 1.5)
        ax.set_title(f"D = {D}")
        ax.set_xlabel("Kantenlaenge L")
        ax.set_ylabel("Treffanteil bis T = 4 L^2")
        ax.grid(True, which="both", alpha=0.3)
        if i == 0:
            ax.legend(fontsize=8, loc="lower left")
    ax = axs.flat[5]
    for j, (key, (lab, col, mk)) in enumerate(stil.items()):
        ser = erg["serien"].get(key)
        if not ser:
            continue
        Ds = sorted(int(d) for d in ser["D"])
        s = [ser["D"][str(d)]["steigung"] for d in Ds]
        lo = [ser["D"][str(d)]["s_lo"] for d in Ds]
        hi = [ser["D"][str(d)]["s_hi"] for d in Ds]
        x = np.array(Ds) + (j - 2) * 0.07
        ax.errorbar(x, s, yerr=[np.array(s) - np.array(lo), np.array(hi) - np.array(s)], color=col, marker=mk,
                    label=lab, capsize=2, lw=1.2, ms=4)
    ax.axhline(0, color="#999999", lw=0.8)
    ax.axhline(S_PLAN, color="#999999", lw=0.8, ls="--")
    ax.set_xlabel("Raumdimension D")
    ax.set_ylabel("Steigung d ln P / d ln L")
    ax.set_title("Abfall mit L (gestrichelt: Planschwelle -0,25)")
    ax.grid(True, alpha=0.3)
    fig.suptitle("FADEN-DIM-1: Treffanteil gewickelter Faeden (+1/-1) auf dem D-Torus")
    fig.tight_layout()
    fig.savefig(out, dpi=110)
    print("bild geschrieben", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("modus", choices=["rauch", "lauf", "auswertung", "bild"])
    ap.add_argument("--zellen", default="")
    ap.add_argument("--out", default="")
    ap.add_argument("--ein", default="")
    ap.add_argument("--out-json", default="")
    ap.add_argument("--out-txt", default="")
    a = ap.parse_args()
    if a.modus == "rauch":
        modus_rauch()
    elif a.modus == "lauf":
        modus_lauf([z for z in a.zellen.split(",") if z], a.out)
    elif a.modus == "auswertung":
        modus_auswertung([f for f in a.ein.split(",") if f], a.out_json, a.out_txt)
    else:
        modus_bild(a.ein, a.out)


if __name__ == "__main__":
    main()
