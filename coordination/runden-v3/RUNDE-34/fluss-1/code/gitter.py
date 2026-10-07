# EIS-1 (Runde 34): Pyrochlor- und fcc-Geometrie auf dem periodischen Torus aus L^3 kubischen Zellen.
# Ganzzahlige Koordinaten in Einheiten von 1/8 der Zellkante (Periode P = 8 L).
import numpy as np

F_FCC = np.array([[0, 0, 0], [0, 4, 4], [4, 0, 4], [4, 4, 0]])          # fcc-Verschiebungen in der Zelle
B_PYR = np.array([[0, 0, 0], [0, 2, 2], [2, 0, 2], [2, 2, 0]])          # Basis der 4 Ecken (Zellkante 8)
D_PYR = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]])    # Ecke -> Mitte des oberen Tetraeders


def fcc_punkte(L):
    c = np.array([(x, y, z) for x in range(L) for y in range(L) for z in range(L)])
    return ((c[:, None, :] * 8 + F_FCC[None, :, :]).reshape(-1, 3)) % (8 * L)


def minbild(d, P):
    """Minimales Bild komponentenweise, Ergebnis in [-P/2, P/2]."""
    return d - P * np.round(d / P)


def pyrochlor(L):
    """Ecken, Tetraeder (oben: 0..nup-1, unten: nup..2nup-1), Zuordnungen, Pruefungen."""
    P = 8 * L
    fcc = fcc_punkte(L)
    nup = len(fcc)
    idx = {tuple(p): n for n, p in enumerate(fcc)}
    ecken = ((fcc[:, None, :] + B_PYR[None, :, :]).reshape(-1, 3)) % P
    sub = np.tile(np.arange(4), nup)
    oben = (ecken + D_PYR[sub]) % P
    unten = (ecken - D_PYR[sub]) % P
    tup = np.array([idx[tuple((c - 1) % P)] for c in oben], dtype=np.int32)
    tdown = np.array([nup + idx[tuple((c + 1) % P)] for c in unten], dtype=np.int32)
    nt = 2 * nup
    tsite = -np.ones((nt, 4), dtype=np.int32)
    fuell = np.zeros(nt, dtype=int)
    for i in range(len(ecken)):
        for t in (tup[i], tdown[i]):
            tsite[t, fuell[t]] = i
            fuell[t] += 1
    tkoord = np.zeros((nt, 3), dtype=np.int32)
    tkoord[:nup] = (fcc + 1) % P
    tkoord[nup:] = (fcc - 1) % P
    # Pruefungen
    pr = {}
    pr["ecken"] = int(len(ecken)); pr["ecken_soll"] = 16 * L ** 3
    pr["tetraeder"] = int(nt); pr["tetraeder_soll"] = 8 * L ** 3
    pr["tetraeder_je_4_ecken"] = bool(np.all(fuell == 4))
    kanten = set()
    for t in range(nt):
        s = tsite[t]
        for a in range(4):
            for b in range(a + 1, 4):
                kanten.add((min(s[a], s[b]), max(s[a], s[b])))
    kanten = np.array(sorted(kanten))
    pr["kanten"] = int(len(kanten)); pr["kanten_soll"] = 48 * L ** 3
    d = minbild(ecken[kanten[:, 1]] - ecken[kanten[:, 0]], P)
    d2 = (d ** 2).sum(1)
    pr["kantenlaenge2_min_max_in_1_64"] = [int(d2.min()), int(d2.max())]
    grad = np.bincount(kanten.ravel(), minlength=len(ecken))
    pr["nachbarn_je_ecke_min_max"] = [int(grad.min()), int(grad.max())]
    # Tetraedermitte = Mittel der Ecken (minimales Bild) und Ecke -> Mitten-Abstand
    dm = minbild(ecken[tsite] - tkoord[:, None, :], P)
    pr["ecke_mitte_abstand2_min_max"] = [int((dm ** 2).sum(2).min()), int((dm ** 2).sum(2).max())]
    pr["mitte_ist_schwerpunkt"] = bool(np.all(dm.sum(1) == 0))
    return dict(L=L, P=P, ecken=ecken, sub=sub, tup=tup, tdown=tdown, tsite=tsite, tkoord=tkoord, nup=nup,
                kanten=kanten, pruef=pr)


def fcc_netz(L):
    """fcc-Knoten mit allen 12 naechsten Nachbarn als Staebe (Tetraeder-Oktaeder-Wabe)."""
    P = 8 * L
    knoten = fcc_punkte(L)
    idx = {tuple(p): n for n, p in enumerate(knoten)}
    richt = np.array([[4, 4, 0], [4, -4, 0], [4, 0, 4], [4, 0, -4], [0, 4, 4], [0, 4, -4]])
    staebe = []
    for i, p in enumerate(knoten):
        for r in richt:
            j = idx[tuple((p + r) % P)]
            staebe.append((i, j, r[0], r[1], r[2]))
    return knoten, np.array(staebe)


def pyrochlor_staebe(L):
    g = pyrochlor(L)
    P = g["P"]
    ecken = g["ecken"]
    st = []
    for (i, j) in g["kanten"]:
        d = minbild(ecken[j] - ecken[i], P).astype(int)
        st.append((i, j, d[0], d[1], d[2]))
    return g, ecken, np.array(st)
