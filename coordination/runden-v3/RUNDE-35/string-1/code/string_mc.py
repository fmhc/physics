#!/usr/bin/env python3
"""STRING-1 (Runde 35): Treiber fuer Wurm (Strommodell), Villain-Winkelmodell, d = 1 exakt und Gauss-Referenz.

Nur auf der .69 ueber kleintest.sh starten. Der C-Kern string_kern.so liegt neben diesem Skript (vorher per gcc
uebersetzt). Unterbefehle:
  pruef   <ausgabe>
  wurm    <d> <L> <K> <seed> <zeit_s> <n_bloecke> <bias_b> <ausgabe>
  villain <d> <L> <K> <seed> <zeit_s> <n_bloecke> <delta> <muT oder -> <einlauf_durchgaenge> <ausgabe>
  wurm_paare <d> <L> <K> <muT> <seed> <zeit_s> <n_bloecke> <bias_b> <kappe> <ausgabe>
  pruef_paare <ausgabe>
  kette   <ausgabe>
  gauss   <ausgabe>
Ausgabe: <ausgabe>.json (Zusammenfassung) und <ausgabe>.npz (Bloecke).
Konventionen: F/T(r) = -ln[Z(r)/Z(0)] auf der Achse r e_mu; Abstand auf dem Torus komponentenweise min(c, L - c).
"""
import sys, os, json, time, ctypes, hashlib
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
SO = os.path.join(HIER, "string_kern.so")
QUELLE = os.path.join(HIER, "string_kern.c")
MM_VILLAIN = 3  # Abschnitt der m-Summe: m = -3..3


def sha(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def pruefsummen():
    return {"string_mc.py": sha(os.path.abspath(__file__)), "string_kern.c": sha(QUELLE), "string_kern.so": sha(SO)}


def kern():
    k = ctypes.CDLL(SO)
    I32 = np.ctypeslib.ndpointer(dtype=np.int32, flags="C_CONTIGUOUS")
    I64 = np.ctypeslib.ndpointer(dtype=np.int64, flags="C_CONTIGUOUS")
    U64 = np.ctypeslib.ndpointer(dtype=np.uint64, flags="C_CONTIGUOUS")
    F64 = np.ctypeslib.ndpointer(dtype=np.float64, flags="C_CONTIGUOUS")
    k.wurm_laufe.restype = ctypes.c_int64
    k.wurm_laufe.argtypes = [ctypes.c_int64, ctypes.c_int32, ctypes.c_int32, I32, I32, I32, ctypes.c_void_p,
                             ctypes.c_double, U64, I64, I64]
    k.gauss_pruefen.restype = ctypes.c_int64
    k.gauss_pruefen.argtypes = [ctypes.c_int32, ctypes.c_int32, I32, I32, ctypes.c_int32, ctypes.c_int32]
    I8 = np.ctypeslib.ndpointer(dtype=np.int8, flags="C_CONTIGUOUS")
    k.wurm_paare_laufe.restype = ctypes.c_int64
    k.wurm_paare_laufe.argtypes = [ctypes.c_int64, ctypes.c_int32, ctypes.c_int32, I32, I32, I8, I32, ctypes.c_void_p,
                                   ctypes.c_double, ctypes.c_double, ctypes.c_double, U64, I64, I64]
    k.gauss_pruefen_q.restype = ctypes.c_int64
    k.gauss_pruefen_q.argtypes = [ctypes.c_int32, ctypes.c_int32, I32, I32, I8, ctypes.c_int32, ctypes.c_int32]
    k.villain_ln_aussen.restype = ctypes.c_double
    k.villain_ln_aussen.argtypes = [ctypes.c_double, ctypes.c_double, F64, ctypes.c_int32]
    k.villain_laufe.restype = ctypes.c_int64
    k.villain_laufe.argtypes = [ctypes.c_int64, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, I32,
                                I32, F64, F64, ctypes.c_double, F64, ctypes.c_int32, ctypes.c_double, ctypes.c_double,
                                U64, F64, F64, F64, I64]
    return k


def gitter(d, L):
    V = L ** d
    x = np.arange(V, dtype=np.int64)
    koord = np.stack([(x // L ** mu) % L for mu in range(d)], axis=1)
    nb = np.empty((V, 2 * d), dtype=np.int64)
    for mu in range(d):
        st = L ** mu
        c = koord[:, mu]
        nb[:, 2 * mu] = x + (((c + 1) % L) - c) * st
        nb[:, 2 * mu + 1] = x + (((c - 1) % L) - c) * st
    # Bias-Norm: Maximumsnorm des Torus-Abstands (auf der Achse = r; abseits der Achsen kleiner als der Euklid-Abstand,
    # so dass die Achsen das groesste Nettogewicht behalten)
    dist = np.minimum(koord, L - koord).max(axis=1).astype(np.float64)
    return V, koord, np.ascontiguousarray(nb.reshape(-1).astype(np.int32)), dist


def achsen(d, L):
    """Je r = 0..L/2 die Indizes der verschiedenen Achsenvektoren +-r e_mu."""
    R = L // 2
    aus = []
    for r in range(R + 1):
        s = set()
        for mu in range(d):
            for sg in (1, -1):
                s.add(((sg * r) % L) * L ** mu)
        aus.append(np.array(sorted(s), dtype=np.int64))
    return aus


def rng_zustand(seed):
    return np.ascontiguousarray(np.random.SeedSequence(int(seed)).generate_state(4, dtype=np.uint64))


def speichern(aus, js, **arr):
    with open(aus + ".json", "w") as f:
        json.dump(js, f, indent=1)
    if arr:
        np.savez_compressed(aus + ".npz", **arr)


# ---------------------------------------------------------------- Wurm
def wurm_lauf(k, d, L, K, seed, zeit_s, n_bloecke, bias_b, protokoll=True, feste_schritte=None):
    t0 = time.time()
    V, koord, nb, dist = gitter(d, L)
    n = np.zeros(V * d, dtype=np.int32)
    zustand = np.zeros(3, dtype=np.int32)
    gew = None
    gp = None
    if bias_b > 0:
        gew = np.ascontiguousarray(np.exp(bias_b * dist))
        gp = gew.ctypes.data_as(ctypes.c_void_p)
    rng = rng_zustand(seed)
    z = np.zeros(5, dtype=np.int64)
    hist = np.zeros(V, dtype=np.int64)
    ax = achsen(d, L)
    R = L // 2
    # Einlauf (10 % der Zeit bzw. feste Zahl), Tempo messen
    schritte_ein = 0
    ts = time.time()
    if feste_schritte is None:
        while time.time() - ts < 0.1 * zeit_s or schritte_ein < 2_000_000:
            k.wurm_laufe(1_000_000, d, V, nb, n, zustand, gp, 0.5 * K, rng, hist, z)
            schritte_ein += 1_000_000
        tempo = schritte_ein / (time.time() - ts)
        rest = zeit_s - (time.time() - t0)
        block = max(100_000, int(tempo * rest * 0.95 / n_bloecke))
    else:
        schritte_ein = feste_schritte[0]
        k.wurm_laufe(schritte_ein, d, V, nb, n, zustand, gp, 0.5 * K, rng, hist, z)
        tempo = float("nan")
        block = feste_schritte[1]
    z[:] = 0
    axz = np.zeros((n_bloecke, R + 1), dtype=np.int64)
    gesamt = np.zeros(V, dtype=np.int64)
    fehler = np.zeros(n_bloecke, dtype=np.int64)
    n2 = np.zeros(n_bloecke, dtype=np.float64)
    zb = np.zeros((n_bloecke, 5), dtype=np.int64)
    fehler_start = int(k.gauss_pruefen(d, V, nb, n, int(zustand[0]), int(zustand[1])))
    for b in range(n_bloecke):
        hist[:] = 0
        zv = z.copy()
        k.wurm_laufe(block, d, V, nb, n, zustand, gp, 0.5 * K, rng, hist, z)
        zb[b] = z - zv
        zb[b, 3] = z[3]
        for r in range(R + 1):
            axz[b, r] = hist[ax[r]].sum()
        gesamt += hist
        fehler[b] = k.gauss_pruefen(d, V, nb, n, int(zustand[0]), int(zustand[1]))
        n2[b] = float((n.astype(np.int64) ** 2).sum()) / (V * d)
        if protokoll and (b % 10 == 0 or b == n_bloecke - 1):
            print("block %d/%d  t=%.1f s  annahme=%.4f  geschlossen=%.3e  gauss_fehler=%d" %
                  (b + 1, n_bloecke, time.time() - t0, zb[b, 1] / max(1, zb[b, 0]), zb[b, 2] / max(1, zb[b, 0]),
                   fehler[b]), flush=True)
    w_ax = np.array([gew[ax[r][0]] if gew is not None else 1.0 for r in range(R + 1)])
    nvec = np.array([len(ax[r]) for r in range(R + 1)])
    # G(r) = (sum Achse / (nvec w(r))) / (hist0 / w(0))
    S = axz.sum(axis=0).astype(np.float64)
    G = (S / (nvec * w_ax)) / (S[0] / w_ax[0])
    gw = gesamt / (gew if gew is not None else 1.0)
    chi = float(gw.sum() / gw[0])
    js = {"art": "wurm", "d": d, "L": L, "K": K, "seed": seed, "zeit_s": zeit_s, "n_bloecke": n_bloecke,
          "bias_b": bias_b, "block_schritte": int(block), "einlauf_schritte": int(schritte_ein),
          "tempo_schritte_s": tempo, "laufzeit_s": time.time() - t0, "versuche": int(zb[:, 0].sum()),
          "annahme": float(zb[:, 1].sum() / zb[:, 0].sum()), "anteil_geschlossen": float(zb[:, 2].sum() / zb[:, 0].sum()),
          "max_betrag_n": int(z[3]), "zuege_ausser_tabelle": int(zb[:, 4].sum()),
          "gauss_fehler_start": fehler_start, "gauss_fehler_bloecke": int(fehler.sum()),
          "n2_je_kante_mittel": float(n2.mean()), "chi": chi,
          "G_achse": G.tolist(), "F_T_achse": (-np.log(np.where(G > 0, G, np.nan))).tolist(),
          "achse_zaehler_gesamt": S.tolist(), "pruefsummen": pruefsummen()}
    arr = dict(axz=axz, nvec=nvec, w_ax=w_ax, gesamt=gesamt, fehler=fehler, n2=n2, zb=zb,
               gew=(gew if gew is not None else np.ones(1)))
    return js, arr


# ---------------------------------------------------------------- Wurm mit Paarbildung (S6)
def wurm_paare_lauf(k, d, L, K, muT, seed, zeit_s, n_bloecke, bias_b, kappe, pC=0.5, protokoll=True, feste_schritte=None):
    """Wie wurm_lauf, zusaetzlich dynamische Ladungen q in {-1,0,1} mit Fugazitaet z = exp(-muT) und Sprungzug C.
    Bias w(D) = exp(b min(|D|_max, kappe))."""
    t0 = time.time()
    V, koord, nb, dist = gitter(d, L)
    n = np.zeros(V * d, dtype=np.int32)
    q = np.zeros(V, dtype=np.int8)
    zustand = np.array([0, 0, 0, L], dtype=np.int32)
    gew = None
    gp = None
    if bias_b > 0:
        gew = np.ascontiguousarray(np.exp(bias_b * np.minimum(dist, kappe)))
        gp = gew.ctypes.data_as(ctypes.c_void_p)
    zf = float(np.exp(-muT))
    rng = rng_zustand(seed)
    z = np.zeros(7, dtype=np.int64)
    hist = np.zeros(V, dtype=np.int64)
    ax = achsen(d, L)
    R = L // 2
    schritte_ein = 0
    ts = time.time()
    if feste_schritte is None:
        while time.time() - ts < 0.1 * zeit_s or schritte_ein < 2_000_000:
            k.wurm_paare_laufe(1_000_000, d, V, nb, n, q, zustand, gp, 0.5 * K, zf, pC, rng, hist, z)
            schritte_ein += 1_000_000
        tempo = schritte_ein / (time.time() - ts)
        rest = zeit_s - (time.time() - t0)
        block = max(100_000, int(tempo * rest * 0.95 / n_bloecke))
    else:
        schritte_ein = feste_schritte[0]
        k.wurm_paare_laufe(schritte_ein, d, V, nb, n, q, zustand, gp, 0.5 * K, zf, pC, rng, hist, z)
        tempo = float("nan")
        block = feste_schritte[1]
    z[:] = 0
    axz = np.zeros((n_bloecke, R + 1), dtype=np.int64)
    gesamt = np.zeros(V, dtype=np.int64)
    fehler = np.zeros(n_bloecke, dtype=np.int64)
    nq = np.zeros(n_bloecke, dtype=np.float64)
    zb = np.zeros((n_bloecke, 7), dtype=np.int64)
    fehler_start = int(k.gauss_pruefen_q(d, V, nb, n, q, int(zustand[0]), int(zustand[1])))
    for b in range(n_bloecke):
        hist[:] = 0
        zv = z.copy()
        k.wurm_paare_laufe(block, d, V, nb, n, q, zustand, gp, 0.5 * K, zf, pC, rng, hist, z)
        zb[b] = z - zv
        for r in range(R + 1):
            axz[b, r] = hist[ax[r]].sum()
        gesamt += hist
        fehler[b] = k.gauss_pruefen_q(d, V, nb, n, q, int(zustand[0]), int(zustand[1]))
        nq[b] = float(np.abs(q).sum())
        if protokoll and (b % 10 == 0 or b == n_bloecke - 1):
            print("block %d/%d  t=%.1f s  spruenge=%d/%d  geschlossen=%.3e  ladungen=%d  gauss_fehler=%d" %
                  (b + 1, n_bloecke, time.time() - t0, zb[b, 6], zb[b, 5], zb[b, 2] / max(1, block), nq[b], fehler[b]),
                  flush=True)
    w_ax = np.array([gew[ax[r][0]] if gew is not None else 1.0 for r in range(R + 1)])
    nvec = np.array([len(ax[r]) for r in range(R + 1)])
    S = axz.sum(axis=0).astype(np.float64)
    G = (S / (nvec * w_ax)) / (S[0] / w_ax[0])
    js = {"art": "wurm_paare", "d": d, "L": L, "K": K, "muT": muT, "z": zf, "pC": pC, "seed": seed, "zeit_s": zeit_s,
          "n_bloecke": n_bloecke, "bias_b": bias_b, "kappe": kappe, "block_schritte": int(block),
          "einlauf_schritte": int(schritte_ein), "tempo_schritte_s": tempo, "laufzeit_s": time.time() - t0,
          "sprung_versuche": int(zb[:, 5].sum()), "spruenge": int(zb[:, 6].sum()), "kanten_versuche": int(zb[:, 0].sum()),
          "kanten_annahme": float(zb[:, 1].sum() / max(1, zb[:, 0].sum())),
          "gauss_fehler_start": fehler_start, "gauss_fehler_bloecke": int(fehler.sum()),
          "ladungen_mittel": float(nq.mean()), "G_achse": G.tolist(),
          "F_T_achse": (-np.log(np.where(G > 0, G, np.nan))).tolist(), "achse_zaehler_gesamt": S.tolist(),
          "pruefsummen": pruefsummen()}
    arr = dict(axz=axz, nvec=nvec, w_ax=w_ax, gesamt=gesamt, fehler=fehler, nq=nq, zb=zb,
               gew=(gew if gew is not None else np.ones(1)))
    return js, arr


def befehl_pruef_paare(aus):
    """Wurm mit Paarbildung gegen die exakte Spur (Ring d = 1, L = 8, K = 1, mu/T = 1), ohne und mit Bias."""
    t0 = time.time()
    k = kern()
    L, K, muT = 8, 1.0, 1.0
    l0 = kette_lnZ(L, None, None, K, muT, True, 20, ring=True)
    ex = np.array([1.0] + [np.exp(kette_lnZ(L, 0, r, K, muT, True, 20, ring=True) - l0) for r in range(1, L // 2 + 1)])
    erg = {"art": "pruef_paare", "G_exakt": ex.tolist()}
    for name, b, kap, seed in (("ohne_bias", 0.0, 0, 21), ("bias", 0.5, 2, 22)):
        js, arr = wurm_paare_lauf(k, 1, L, K, muT, seed, 0, 40, b, kap, protokoll=False, feste_schritte=(1_000_000, 1_000_000))
        g, e = jk(blockG(arr))
        erg[name] = {"G": g.tolist(), "f": e.tolist(), "z": ((g - ex) / np.where(e > 0, e, 1)).tolist(),
                     "gauss_fehler": js["gauss_fehler_start"] + js["gauss_fehler_bloecke"], "spruenge": js["spruenge"]}
    # d = 2, L = 6, K = 1, mu/T = 1,5: Wurm mit Paaren gegen Villain mit Platzfaktor (beides Monte Carlo)
    js, arr = wurm_paare_lauf(k, 2, 6, 1.0, 1.5, 23, 0, 40, 0.0, 0, protokoll=False, feste_schritte=(1_000_000, 1_000_000))
    jv, av = villain_lauf(k, 2, 6, 1.0, 24, 0, 40, 2.0, 1.5, 2000, protokoll=False, feste=5000)
    g, e = jk(blockG(arr))
    gv, ev = jk(av["Gb"])
    erg["d2_L6"] = {"G_wurm": g.tolist(), "f_wurm": e.tolist(), "G_villain": gv.tolist(), "f_villain": ev.tolist(),
                    "z": ((g - gv) / np.sqrt(e ** 2 + ev ** 2 + 1e-300)).tolist(),
                    "gauss_fehler": js["gauss_fehler_start"] + js["gauss_fehler_bloecke"]}
    erg["laufzeit_s"] = time.time() - t0
    erg["pruefsummen"] = pruefsummen()
    speichern(aus, erg)
    print(json.dumps(erg, indent=1))


# ---------------------------------------------------------------- Villain
def villain_cm(KV, MM):
    m = np.arange(MM + 1, dtype=np.float64)
    return np.ascontiguousarray(np.exp(-2.0 * np.pi ** 2 * KV * m ** 2))


def villain_abschnitt(k, KV, MM=MM_VILLAIN, MMref=12):
    """Groesster relativer Abschnittsfehler des Villain-Gewichts (MM gegen MMref) auf einem phi-Gitter."""
    cm, cr = villain_cm(KV, MM), villain_cm(KV, MMref)
    fmax = 0.0
    for phi in np.linspace(-np.pi, np.pi, 2001):
        a = k.villain_ln_aussen(phi, KV, cm, MM)
        b = k.villain_ln_aussen(phi, KV, cr, MMref)
        fmax = max(fmax, abs(np.expm1(a - b)))
    # analytische Schranke: groesster weggelassener Term (|m| = MM+1, phi = +-pi) relativ zum Term m = 0 bei phi = pi
    schranke = 2.0 * np.exp(-0.5 * KV * ((2 * MM + 1) * np.pi) ** 2) / np.exp(-0.5 * KV * np.pi ** 2)
    return fmax, float(schranke)


def villain_lauf(k, d, L, K, seed, zeit_s, n_bloecke, delta, muT, n_ein, protokoll=True, feste=None):
    t0 = time.time()
    V, koord, nb, dist = gitter(d, L)
    KV = 1.0 / K
    cm = villain_cm(KV, MM_VILLAIN)
    hz = 0.0 if muT is None else 2.0 * np.exp(-muT)
    stride = np.array([L ** mu for mu in range(d)], dtype=np.int32)
    th = np.zeros(V, dtype=np.float64)  # kalter Start
    lnv = np.zeros(V * d, dtype=np.float64)
    R = L // 2
    korr = np.zeros(d * (R + 1), dtype=np.float64)
    m2 = np.zeros(1, dtype=np.float64)
    cs = np.zeros(2 * V, dtype=np.float64)
    z = np.zeros(3, dtype=np.int64)
    rng = rng_zustand(seed)
    k.villain_laufe(n_ein, 0, d, L, V, nb, stride, th, lnv, KV, cm, MM_VILLAIN, hz, delta, rng, korr, m2, cs, z)
    if feste is None:
        ts = time.time()
        probe = 0
        while time.time() - ts < 2.0 or probe < 5:
            k.villain_laufe(5, 1, d, L, V, nb, stride, th, lnv, KV, cm, MM_VILLAIN, hz, delta, rng, korr, m2, cs, z)
            probe += 5
        tempo = probe / (time.time() - ts)
        rest = zeit_s - (time.time() - t0)
        je_block = max(1, int(tempo * rest * 0.95 / n_bloecke))
    else:
        tempo = float("nan")
        je_block = feste
    zein = z.copy()
    Gb = np.zeros((n_bloecke, R + 1), dtype=np.float64)
    Gbmu = np.zeros((n_bloecke, d, R + 1), dtype=np.float64)
    m2b = np.zeros(n_bloecke, dtype=np.float64)
    for b in range(n_bloecke):
        korr[:] = 0.0
        m2[:] = 0.0
        zv = z.copy()
        k.villain_laufe(je_block, 1, d, L, V, nb, stride, th, lnv, KV, cm, MM_VILLAIN, hz, delta, rng, korr, m2, cs, z)
        nm = z[2] - zv[2]
        km = korr.reshape(d, R + 1) / (V * nm)
        Gbmu[b] = km
        Gb[b] = km.mean(axis=0)
        m2b[b] = m2[0] / nm
        if protokoll and (b % 10 == 0 or b == n_bloecke - 1):
            print("block %d/%d  t=%.1f s  annahme=%.4f  G(1)=%.5f" %
                  (b + 1, n_bloecke, time.time() - t0, (z[1] - zv[1]) / max(1, z[0] - zv[0]), Gb[b, 1]), flush=True)
    fmax, schranke = villain_abschnitt(k, KV)
    G = Gb.mean(axis=0)
    js = {"art": "villain", "d": d, "L": L, "K": K, "KV": KV, "muT": muT, "hz": hz, "seed": seed, "zeit_s": zeit_s,
          "n_bloecke": n_bloecke, "durchgaenge_je_block": int(je_block), "einlauf_durchgaenge": int(n_ein),
          "delta": delta, "tempo_durchgaenge_s": tempo, "laufzeit_s": time.time() - t0,
          "annahme": float((z[1] - zein[1]) / max(1, z[0] - zein[0])), "MM": MM_VILLAIN,
          "abschnitt_rel_fehler_max": fmax, "abschnitt_schranke": schranke, "m2_mittel": float(m2b.mean()),
          "G_achse": G.tolist(), "F_T_achse": (-np.log(np.where(G > 0, G, np.nan))).tolist(),
          "pruefsummen": pruefsummen()}
    return js, dict(Gb=Gb, Gbmu=Gbmu, m2b=m2b)


# ---------------------------------------------------------------- d = 1 exakt (Uebertragungsmatrix ueber den Flusswert)
def kette_lnZ(N, A, B, K, muT, paare, nmax, ring=False):
    """ln Z einer Kette mit N Plaetzen. Externe Ladung +1 bei A, -1 bei B (None = keine). Gauss-Gesetz am Platz i:
    n_{i-1} - n_i = Q_i (Zufluss minus Abfluss), Q_i = extern + q_i, q_i in {-1, 0, 1} mit Gewicht exp(-muT |q|)
    (nur mit paare). Kantengewicht exp(-(K/2) n^2). Offen: n_{-1} = n_{N-1} = 0. Ring: Spur."""
    W = np.arange(-nmax, nmax + 1)
    m = len(W)
    kg = np.exp(-0.5 * K * W.astype(np.float64) ** 2)
    qs = [(-1, np.exp(-muT)), (0, 1.0), (1, np.exp(-muT))] if paare else [(0, 1.0)]

    def M_i(i):
        Qe = (1 if i == A else 0) + (-1 if i == B else 0)
        Mi = np.zeros((m, m))
        for q, g in qs:
            Q = Qe + q
            for j in range(m):  # j: Index von n_i; n_{i-1} = n_i + Q
                jj = j + Q
                if 0 <= jj < m:
                    Mi[jj, j] += g
        return Mi

    lnZ = 0.0
    if not ring:
        v = np.zeros(m)
        v[nmax] = 1.0
        for i in range(N):
            v = v @ M_i(i)
            if i < N - 1:
                v = v * kg
            s = v.sum()
            if s <= 0:
                return -np.inf
            v /= s
            lnZ += np.log(s)
        return lnZ + np.log(v[nmax]) if v[nmax] > 0 else -np.inf
    P = np.eye(m)
    for i in range(N):
        P = (P @ M_i(i)) * kg[None, :]
        s = np.abs(P).max()
        P /= s
        lnZ += np.log(s)
    return lnZ + np.log(np.trace(P))


def kette_brute(N, A, B, K, muT, paare):
    import itertools
    tot = 0.0
    for qq in itertools.product((-1, 0, 1) if paare else (0,), repeat=N):
        nprev = 0
        w = 1.0
        ok = True
        for i in range(N):
            Q = (1 if i == A else 0) + (-1 if i == B else 0) + qq[i]
            ni = nprev - Q
            w *= np.exp(-muT * abs(qq[i]))
            if i < N - 1:
                w *= np.exp(-0.5 * K * ni * ni)
            nprev = ni
        if nprev != 0:
            ok = False
        if ok:
            tot += w
    return np.log(tot)


def kette_FT(N, a0, rs, K, muT, paare, nmax):
    l0 = kette_lnZ(N, None, None, K, muT, paare, nmax)
    return np.array([-(kette_lnZ(N, a0, a0 + r, K, muT, paare, nmax) - l0) if r > 0 else 0.0 for r in rs])


def befehl_kette(aus):
    t0 = time.time()
    J, T, mu = 1.0, 0.5, 3.0
    K, muT = J / T, mu / T
    rs = np.arange(0, 61)
    ohne = kette_FT(400, 150, rs, K, muT, False, 8)
    mit = kette_FT(400, 150, rs, K, muT, True, 8)
    # Kontrollen: andere Kettenlaenge und Lage, anderer Flussabschnitt
    mit_b = kette_FT(600, 250, rs, K, muT, True, 8)
    mit_c = kette_FT(400, 150, rs, K, muT, True, 16)
    js = {"art": "kette", "J": J, "T": T, "mu": mu, "K": K, "muT": muT, "N": 400, "A": 150, "nmax": 8,
          "r": rs.tolist(), "F_T_ohne": ohne.tolist(), "F_T_mit": mit.tolist(),
          "kontrolle_max_abw_N600": float(np.abs(mit_b - mit).max()),
          "kontrolle_max_abw_nmax16": float(np.abs(mit_c - mit).max()),
          "ohne_max_abw_von_K2_r": float(np.abs(ohne - 0.5 * K * rs).max()),
          "laufzeit_s": time.time() - t0, "pruefsummen": pruefsummen()}
    speichern(aus, js)
    print(json.dumps({k: v for k, v in js.items() if not isinstance(v, list)}, indent=1))


# ---------------------------------------------------------------- Gauss-Referenz (Spinwellen ohne Wirbel)
def gauss_FT(d, L, K):
    kk = 2 * np.pi * np.fft.fftfreq(L)
    lam = np.zeros([L] * d)
    for mu in range(d):
        sh = [1] * d
        sh[mu] = L
        lam = lam + (2 - 2 * np.cos(kk)).reshape(sh)
    inv = np.zeros_like(lam)
    inv[lam > 1e-14] = 1.0 / lam[lam > 1e-14]
    Gam = np.real(np.fft.ifftn(inv))
    R = L // 2
    idx = [0] * d
    gr = []
    for r in range(R + 1):
        idx[0] = r
        gr.append(Gam[tuple(idx)])
    gr = np.array(gr)
    return K * (gr[0] - gr)


def befehl_gauss(aus):
    js = {"art": "gauss", "erklaerung": "F/T = K (Gamma_L(0) - Gamma_L(r e_1)), Gamma_L Gitter-Greenfunktion auf dem Torus ohne Nullmode",
          "faelle": []}
    for d, L, K in [(2, 64, 0.5), (2, 128, 0.5), (3, 24, 1.5), (3, 32, 1.5), (2, 64, 2.5), (3, 24, 4.5)]:
        js["faelle"].append({"d": d, "L": L, "K": K, "F_T": gauss_FT(d, L, K).tolist()})
    js["pruefsummen"] = pruefsummen()
    speichern(aus, js)
    print("gauss fertig")


# ---------------------------------------------------------------- Pruefungen
def befehl_pruef(aus):
    t0 = time.time()
    k = kern()
    erg = {"art": "pruef"}
    # 1. Wurm d = 1 auf dem Ring L = 8, K = 1: exakt Z(r)/Z(0) = sum_w exp(-K/2((w+1)^2 r + w^2 (L-r))) / sum_w exp(-K/2 w^2 L)
    L, K = 8, 1.0
    js, arr = wurm_lauf(k, 1, L, K, 11, 0, 40, 0.0, protokoll=False, feste_schritte=(1_000_000, 1_000_000))
    ws = np.arange(-30, 31)
    ex = np.array([np.exp(-0.5 * K * ((ws + 1) ** 2 * r + ws ** 2 * (L - r))).sum() for r in range(L // 2 + 1)])
    ex = ex / np.exp(-0.5 * K * ws ** 2 * L).sum()
    Gb = blockG(arr)
    Gm, Ge = jk(Gb)
    erg["wurm_ring1d"] = {"G_mc": Gm.tolist(), "fehler": Ge.tolist(), "G_exakt": ex.tolist(),
                          "z": ((Gm - ex) / np.where(Ge > 0, Ge, 1)).tolist(), "gauss_fehler": js["gauss_fehler_bloecke"]}
    # 2. Wurm d = 2, L = 6, K = 1 ohne und mit Bias; 3. Villain d = 2, L = 6, K = 1
    js0, a0 = wurm_lauf(k, 2, 6, 1.0, 12, 0, 40, 0.0, protokoll=False, feste_schritte=(1_000_000, 1_000_000))
    js1, a1 = wurm_lauf(k, 2, 6, 1.0, 13, 0, 40, 0.6, protokoll=False, feste_schritte=(1_000_000, 1_000_000))
    jv, av = villain_lauf(k, 2, 6, 1.0, 14, 0, 40, 2.0, None, 2000, protokoll=False, feste=5000)
    g0, e0 = jk(blockG(a0))
    g1, e1 = jk(blockG(a1))
    gv, ev = jk(av["Gb"])
    erg["wurm_bias_villain_2d"] = {"G_ohne": g0.tolist(), "f_ohne": e0.tolist(), "G_bias": g1.tolist(), "f_bias": e1.tolist(),
                                   "G_villain": gv.tolist(), "f_villain": ev.tolist(),
                                   "z_bias": ((g1 - g0) / np.sqrt(e0 ** 2 + e1 ** 2 + 1e-300)).tolist(),
                                   "z_villain": ((gv - g0) / np.sqrt(e0 ** 2 + ev ** 2 + 1e-300)).tolist(),
                                   "gauss_fehler": js0["gauss_fehler_bloecke"] + js1["gauss_fehler_bloecke"],
                                   "villain_annahme": jv["annahme"]}
    # 4. Uebertragungsmatrix gegen Abzaehlung (N = 6), mit und ohne Paare
    t = []
    for paare in (False, True):
        for (A, B) in [(None, None), (1, 4), (0, 5), (2, 3)]:
            a = kette_lnZ(6, A, B, 2.0, 6.0, paare, 10)
            b = kette_brute(6, A, B, 2.0, 6.0, paare)
            a2 = kette_lnZ(6, A, B, 0.7, 1.0, paare, 10)
            b2 = kette_brute(6, A, B, 0.7, 1.0, paare)
            t.append(max(abs(a - b), abs(a2 - b2)))
    erg["kette_gegen_abzaehlung_max_abw"] = float(max(t))
    # 5. Feld im Winkelmodell gegen Strommodell mit Paaren: Ring d = 1, L = 8, K = 1, muT = 1 (exakt per Spur)
    L, K, muT = 8, 1.0, 1.0
    l0 = kette_lnZ(L, None, None, K, muT, True, 20, ring=True)
    exf = np.array([1.0] + [np.exp(kette_lnZ(L, 0, r, K, muT, True, 20, ring=True) - l0) for r in range(1, L // 2 + 1)])
    jf, af = villain_lauf(k, 1, L, K, 15, 0, 40, 2.5, muT, 2000, protokoll=False, feste=20000)
    gf, ef = jk(af["Gb"])
    # ohne Paare auf dem Ring (Gegenprobe der Spurformel gegen die Formel aus 1.)
    ex0 = np.array([1.0] + [np.exp(kette_lnZ(L, 0, r, K, muT, False, 20, ring=True) - kette_lnZ(L, None, None, K, muT, False, 20, ring=True)) for r in range(1, L // 2 + 1)])
    erg["feld_ring1d"] = {"G_villain_feld": gf.tolist(), "f": ef.tolist(), "G_exakt_paare": exf.tolist(),
                          "z": ((gf - exf) / np.where(ef > 0, ef, 1)).tolist(), "hz": jf["hz"],
                          "spur_ohne_paare_gegen_formel_max_abw": float(np.abs(ex0 - ex).max())}
    # 6. Abschnitt Villain je K
    erg["villain_abschnitt"] = {str(Kx): villain_abschnitt(k, 1.0 / Kx) for Kx in (0.5, 1.5, 2.5, 4.5)}
    erg["laufzeit_s"] = time.time() - t0
    erg["pruefsummen"] = pruefsummen()
    speichern(aus, erg)
    print(json.dumps(erg, indent=1))


def blockG(arr):
    """Je Block G(r) = (Achse/(nvec w)) / (hist0/w0)."""
    axz = arr["axz"].astype(np.float64)
    return (axz / (arr["nvec"] * arr["w_ax"])) / (axz[:, :1] / arr["w_ax"][0])


def jk(Gb):
    """Mittel und Fehler aus Bloecken (Bloecke gleich gross): Standardfehler des Blockmittels."""
    Gb = np.asarray(Gb, dtype=np.float64)
    B = Gb.shape[0]
    return Gb.mean(axis=0), Gb.std(axis=0, ddof=1) / np.sqrt(B)


def main():
    a = sys.argv[1:]
    befehl = a[0]
    if befehl == "pruef":
        befehl_pruef(a[1])
    elif befehl == "wurm":
        d, L, K, seed, zeit_s, nbl, bias_b, aus = int(a[1]), int(a[2]), float(a[3]), int(a[4]), float(a[5]), int(a[6]), float(a[7]), a[8]
        k = kern()
        js, arr = wurm_lauf(k, d, L, K, seed, zeit_s, nbl, bias_b)
        speichern(aus, js, **arr)
        print(json.dumps({x: v for x, v in js.items() if not isinstance(v, list)}, indent=1))
    elif befehl == "villain":
        d, L, K, seed, zeit_s, nbl, delta = int(a[1]), int(a[2]), float(a[3]), int(a[4]), float(a[5]), int(a[6]), float(a[7])
        muT = None if a[8] == "-" else float(a[8])
        n_ein, aus = int(a[9]), a[10]
        k = kern()
        js, arr = villain_lauf(k, d, L, K, seed, zeit_s, nbl, delta, muT, n_ein)
        speichern(aus, js, **arr)
        print(json.dumps({x: v for x, v in js.items() if not isinstance(v, list)}, indent=1))
    elif befehl == "wurm_paare":
        d, L, K, muT, seed, zeit_s, nbl, bias_b, kappe, aus = (int(a[1]), int(a[2]), float(a[3]), float(a[4]), int(a[5]),
                                                              float(a[6]), int(a[7]), float(a[8]), float(a[9]), a[10])
        k = kern()
        js, arr = wurm_paare_lauf(k, d, L, K, muT, seed, zeit_s, nbl, bias_b, kappe)
        speichern(aus, js, **arr)
        print(json.dumps({x: v for x, v in js.items() if not isinstance(v, list)}, indent=1))
    elif befehl == "pruef_paare":
        befehl_pruef_paare(a[1])
    elif befehl == "kette":
        befehl_kette(a[1])
    elif befehl == "gauss":
        befehl_gauss(a[1])
    else:
        raise SystemExit("unbekannter Befehl " + befehl)


if __name__ == "__main__":
    main()
