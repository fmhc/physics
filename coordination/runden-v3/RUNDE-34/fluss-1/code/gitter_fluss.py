# FLUSS-1 (Runde 34): Geometrie fuer Netz A (Pyrochlor-Kanten, Grad 6) und Netz B (srs-Netz = K4-Kristall, Grad 3).
# Ganzzahlige Koordinaten in Einheiten von 1/8 der kubischen Zellkante (Periode P = 8 L). Kantenlaenge beider Netze
# sqrt(2)/4 Zellkanten (Abstand^2 = 8 in Einheiten von 1/64).
import numpy as np
import gitter  # aus EIS-1 (RUNDE-34/eis-1/code/gitter.py), unveraendert uebernommen

KLASSEN = np.array([[1, 1, 0], [1, -1, 0], [1, 0, 1], [1, 0, -1], [0, 1, 1], [0, 1, -1]])
# srs-Netz: (1/8,1/8,1/8), (5/8,3/8,7/8), (3/8,7/8,5/8), (7/8,5/8,3/8) und diese um (1/2,1/2,1/2) verschoben
SRS_A = np.array([[1, 1, 1], [5, 3, 7], [3, 7, 5], [7, 5, 3]])
SRS = np.vstack([SRS_A, (SRS_A + 4) % 8])
NN_VEKT = np.array([(a, b, 0) for a in (2, -2) for b in (2, -2)] + [(a, 0, b) for a in (2, -2) for b in (2, -2)] +
                   [(0, a, b) for a in (2, -2) for b in (2, -2)])


def klasse_und_vorzeichen(d):
    """d: ganzzahlige Kantenvektoren vom Typ (+-2,+-2,0). Klasse c (Index in KLASSEN) und Vorzeichen (+1: d || +n_c)."""
    d = np.asarray(d, dtype=int)
    if not (np.all(np.isin(np.abs(d), (0, 2))) and np.all((d == 0).sum(1) == 1)):
        raise ValueError("Kantenvektor nicht vom Typ (+-2,+-2,0)")
    e = np.sign(d)
    erste = np.argmax(e != 0, axis=1)
    vz = e[np.arange(len(e)), erste]
    n = e * vz[:, None]
    tab = {tuple(k): i for i, k in enumerate(KLASSEN)}
    kl = np.array([tab[tuple(x)] for x in n], dtype=np.int32)
    return kl, vz.astype(int)


def _aufbau(name, L, P, ecken, kopf, schwanz, kl, G):
    nv = len(ecken); ne = len(kopf)
    inz = -np.ones((nv, G), dtype=np.int32); vz = np.zeros((nv, G), dtype=np.int8)
    nb = -np.ones((nv, G), dtype=np.int32)
    fuell = np.zeros(nv, dtype=int)
    for e in range(ne):
        for v, w, sg in ((kopf[e], schwanz[e], 1), (schwanz[e], kopf[e], -1)):
            k = fuell[v]
            if k >= G:
                raise ValueError("Grad groesser als %d" % G)
            inz[v, k] = e; vz[v, k] = sg; nb[v, k] = w
            fuell[v] += 1
    d = gitter.minbild(ecken[kopf] - ecken[schwanz], P).astype(int)
    mitte = (ecken[schwanz] + d // 2) % P
    pr = {}
    pr["ecken"] = int(nv); pr["kanten"] = int(ne)
    pr["grad_min_max"] = [int(fuell.min()), int(fuell.max())]
    d2 = (d ** 2).sum(1)
    pr["kantenlaenge2_min_max_in_1_64"] = [int(d2.min()), int(d2.max())]
    pr["kante_parallel_plus_n"] = bool(np.all(d == 2 * KLASSEN[kl]))
    pr["kanten_je_klasse"] = [int(x) for x in np.bincount(kl, minlength=6)]
    pr["mitten_eindeutig"] = bool(len(np.unique(mitte, axis=0)) == ne)
    return dict(name=name, L=L, P=P, ecken=ecken, kopf=np.ascontiguousarray(kopf, dtype=np.int32),
                schwanz=np.ascontiguousarray(schwanz, dtype=np.int32), kl=kl, d=d, mitte=mitte,
                inz=np.ascontiguousarray(inz.ravel()), vz=np.ascontiguousarray(vz.ravel()),
                nb=np.ascontiguousarray(nb.ravel()), nb2d=nb, G=G, nv=nv, ne=ne, pruef=pr)


def netz_a(L):
    """Pyrochlor-Ecken, Kanten = Tetraederkanten (6 je Tetraeder), Grad 6; dazu die geraden Ketten je Klasse."""
    g = gitter.pyrochlor(L)
    P = g["P"]; ecken = g["ecken"]; kanten = g["kanten"]
    d = gitter.minbild(ecken[kanten[:, 1]] - ecken[kanten[:, 0]], P).astype(int)
    kl, vzk = klasse_und_vorzeichen(d)
    kopf = np.where(vzk > 0, kanten[:, 1], kanten[:, 0])
    schwanz = np.where(vzk > 0, kanten[:, 0], kanten[:, 1])
    n = _aufbau("A", L, P, ecken, kopf, schwanz, kl, 6)
    pr = n["pruef"]
    pr["ecken_soll"] = 16 * L ** 3; pr["kanten_soll"] = 48 * L ** 3; pr["grad_soll"] = 6
    pr["kanten_je_klasse_soll"] = 8 * L ** 3
    pr["gitter_pyrochlor"] = g["pruef"]
    # gerade Ketten: Invariante senkrecht zur Klassenrichtung (ganzzahlig)
    x = ecken[n["schwanz"]]
    inv = np.zeros((len(kl), 3), dtype=np.int64)
    for c in range(6):
        nn = KLASSEN[c]
        z0 = int(np.where(nn == 0)[0][0]); i, j = [a for a in range(3) if a != z0]
        m = kl == c
        inv[m, 0] = c
        inv[m, 1] = (nn[j] * x[m, i] - nn[i] * x[m, j]) % P
        inv[m, 2] = x[m, z0] % P
    _, kette, laenge = np.unique(inv, axis=0, return_inverse=True, return_counts=True)
    kette = kette.ravel()
    pr["ketten"] = int(len(laenge)); pr["ketten_soll"] = 12 * L ** 2
    pr["kettenlaenge_min_max"] = [int(laenge.min()), int(laenge.max())]; pr["kettenlaenge_soll"] = 4 * L
    # Nachfolger auf der Kette (gleiche Klasse, Schwanz = eigener Kopf)
    tab = {(int(c), int(v)): e for e, (c, v) in enumerate(zip(kl, n["schwanz"]))}
    nachf = np.array([tab[(int(c), int(v))] for c, v in zip(kl, n["kopf"])], dtype=np.int64)
    pr["nachfolger_gleiche_kette"] = bool(np.all(kette[nachf] == kette))
    n["kette"] = kette; n["n_ketten"] = int(len(laenge)); n["nachfolger"] = nachf
    n["untergitter"] = g["sub"]
    ok = (pr["ecken"] == pr["ecken_soll"] and pr["kanten"] == pr["kanten_soll"] and pr["grad_min_max"] == [6, 6]
          and pr["kantenlaenge2_min_max_in_1_64"] == [8, 8] and pr["kante_parallel_plus_n"]
          and all(k == pr["kanten_je_klasse_soll"] for k in pr["kanten_je_klasse"]) and pr["mitten_eindeutig"]
          and pr["ketten"] == pr["ketten_soll"] and pr["kettenlaenge_min_max"] == [4 * L, 4 * L]
          and pr["nachfolger_gleiche_kette"])
    pr["alles_ok"] = bool(ok)
    return n


def netz_b(L):
    """srs-Netz (K4-Kristall), 8 Ecken je kubischer Zelle, naechste Nachbarn im Abstand sqrt(2)/4, Grad 3."""
    P = 8 * L
    c = np.array([(x, y, z) for x in range(L) for y in range(L) for z in range(L)]) * 8
    ecken = ((c[:, None, :] + SRS[None, :, :]).reshape(-1, 3)) % P
    basis = np.tile(np.arange(8), L ** 3)
    seite = (basis >= 4).astype(int)
    idx = {tuple(p): i for i, p in enumerate(ecken)}
    kanten = set()
    for i, p in enumerate(ecken):
        for v in NN_VEKT:
            j = idx.get(tuple((p + v) % P))
            if j is not None:
                kanten.add((min(i, j), max(i, j)))
    kanten = np.array(sorted(kanten))
    d = gitter.minbild(ecken[kanten[:, 1]] - ecken[kanten[:, 0]], P).astype(int)
    kl, vzk = klasse_und_vorzeichen(d)
    kopf = np.where(vzk > 0, kanten[:, 1], kanten[:, 0])
    schwanz = np.where(vzk > 0, kanten[:, 0], kanten[:, 1])
    n = _aufbau("B", L, P, ecken, kopf, schwanz, kl, 3)
    pr = n["pruef"]
    pr["ecken_soll"] = 8 * L ** 3; pr["kanten_soll"] = 12 * L ** 3; pr["grad_soll"] = 3
    pr["kanten_je_klasse_soll"] = 2 * L ** 3
    pr["zweiteilig_A_B"] = bool(np.all(seite[n["kopf"]] != seite[n["schwanz"]]))
    # ebene Dreierecke: die drei Kantenvektoren je Ecke (von der Ecke weg) summieren sich zu 0, paarweise 120 Grad
    nb = n["nb2d"]
    vek = gitter.minbild(ecken[nb] - ecken[:, None, :], P)
    pr["drei_vektoren_summe_null"] = bool(np.all(vek.sum(1) == 0))
    sk = [(vek[:, a] * vek[:, b]).sum(1) for a, b in ((0, 1), (0, 2), (1, 2))]
    pr["paarweise_120_grad"] = bool(all(np.all(x == -4) for x in sk))
    # K4-Quotient: Ecken modulo bcc-Gitter (A_i ~ B_i), je Ecken-Paar der Quotient genau eine Kantenklasse
    q4 = basis % 4
    a_, b_ = q4[n["kopf"]], q4[n["schwanz"]]
    pr["quotient_keine_schleife"] = bool(np.all(a_ != b_))
    paare = {}
    for x, y, c_ in zip(a_, b_, n["kl"]):
        key = (min(int(x), int(y)), max(int(x), int(y)))
        paare.setdefault(key, set()).add(int(c_))
    pr["quotient_paare"] = int(len(paare))
    pr["quotient_ist_K4"] = bool(len(paare) == 6 and all(len(v) == 1 for v in paare.values()))
    n["seite"] = seite; n["basis"] = basis
    ok = (pr["ecken"] == pr["ecken_soll"] and pr["kanten"] == pr["kanten_soll"] and pr["grad_min_max"] == [3, 3]
          and pr["kantenlaenge2_min_max_in_1_64"] == [8, 8] and pr["kante_parallel_plus_n"]
          and all(k == pr["kanten_je_klasse_soll"] for k in pr["kanten_je_klasse"]) and pr["mitten_eindeutig"]
          and pr["zweiteilig_A_B"] and pr["drei_vektoren_summe_null"] and pr["paarweise_120_grad"]
          and pr["quotient_ist_K4"])
    pr["alles_ok"] = bool(ok)
    return n


def bfs_kennzahlen(n, start, tiefe=10):
    """Koordinationsfolge, kuerzester Kreis (gefunden von start aus) und Zahl der kuerzesten Kreise durch start
    (bei Taillenweite 2t: Summe ueber Ecken im Abstand t von C(Zahl kuerzester Wege, 2))."""
    nb = n["nb2d"]; nv = n["nv"]
    dist = -np.ones(nv, dtype=int); sigma = np.zeros(nv, dtype=np.int64); vater = -np.ones(nv, dtype=int)
    dist[start] = 0; sigma[start] = 1
    front = [start]; folge = []; kreis = None
    for t in range(1, tiefe + 1):
        neu = []
        for u in front:
            for w in nb[u]:
                if dist[w] == -1:
                    dist[w] = t; vater[w] = u; neu.append(w); sigma[w] = sigma[u]
                elif dist[w] == t:
                    # zweiter kuerzester Weg nach w: geschlossener Weg der Laenge 2t
                    sigma[w] += sigma[u]
                    kreis = 2 * t if kreis is None else min(kreis, 2 * t)
                elif dist[w] == t - 1:
                    # Kante innerhalb einer Schale: ungerader Kreis
                    kreis = 2 * t - 1 if kreis is None else min(kreis, 2 * t - 1)
        folge.append(len(neu))
        front = neu
    halb = None if kreis is None or kreis % 2 else kreis // 2
    ringe = None
    if halb is not None and halb <= tiefe:
        w = np.where(dist == halb)[0]
        ringe = int(sum(int(x) * (int(x) - 1) // 2 for x in sigma[w]))
    return dict(koordinationsfolge=folge, kuerzester_kreis=kreis, kuerzeste_kreise_durch_start=ringe)
