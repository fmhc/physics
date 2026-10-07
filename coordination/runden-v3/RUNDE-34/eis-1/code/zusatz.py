# EIS-1 (Runde 34): Zusatzauswertung NACH den echten Laeufen, nur berichtet (keine Urteile). Nur ueber kleintest.sh.
# Aufruf: zusatz.py <laufordner> <ausgabe.json>
#  1. fcc- und Pyrochlor-Netz: Stabkraefte neu (gleicher eingefrorener Loeser aus stabnetz.py), getrennt nach
#     Fehlpass-Linie und abseits; Exponenten ueber den eingefrorenen Bereich [1; L/4] und weiter aussen [3; 5,5].
#  2. Spin-Eis: F_MC gegen die Gauss-Gegenprobe F_G linear (F_MC = alpha + beta F_G) ueber den eingefrorenen Bereich.
import sys, os, json, time, hashlib
import numpy as np
from scipy.sparse.linalg import lsqr

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import gitter
import stabnetz

ordner = sys.argv[1]; ausgabe = sys.argv[2]


def steigung(r, t, lo, hi, schwelle=1e-9):
    m = (r >= lo) & (r <= hi) & (np.abs(t) > schwelle)
    if m.sum() < 3:
        return dict(exponent=None, n=int(m.sum()))
    x = np.log(r[m]); y = np.log(np.abs(t[m]))
    A = np.column_stack([np.ones_like(x), x])
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    return dict(exponent=float(-c[1]), n=int(m.sum()), streuung_log=float(np.sqrt(np.mean((y - A @ c) ** 2))))


def huelle(r, t, lo, hi, maske):
    """Maximum je Klasse (Breite 0,25) wie stabnetz.py, dann Steigung ueber Klassenmitten in [lo, hi]."""
    kanten = np.arange(0, r.max() + 0.25, 0.25)
    rr = []; tt = []
    for c in range(len(kanten) - 1):
        mid = 0.5 * (kanten[c] + kanten[c + 1])
        if not (lo <= mid <= hi):
            continue
        mk = maske & (r >= kanten[c]) & (r < kanten[c + 1]) & (r > 0)
        if not np.any(mk):
            continue
        ids = np.where(mk)[0]
        j = ids[np.argmax(np.abs(t[ids]))]
        rr.append(r[j]); tt.append(abs(t[j]))
    return steigung(np.array(rr), np.array(tt), 0, 1e9) if len(rr) else dict(exponent=None, n=0)


aus = dict(hinweis="nachtraeglich, nur berichtet, keine Urteile")
for art in ("fcc", "pyro"):
    for L in (8, 12):
        pos, st, pruef, je_zelle, basis, d0 = stabnetz.netz(art, L)
        C, nv = stabnetz.kompat(pos, st)
        b0 = int(np.where((st[:, 0] == 0) & np.all(st[:, 2:5] == d0, axis=1))[0][0])
        e0 = np.zeros(len(st)); e0[b0] = 1.0
        u = lsqr(C, e0, atol=1e-15, btol=1e-15, conlim=1e14, iter_lim=200000)[0]
        t = C @ u - e0
        mitte = pos[st[:, 0]] + st[:, 2:5] / 2.0
        rel = gitter.minbild(mitte - mitte[b0], 8 * L) / 8.0
        r = np.linalg.norm(rel, axis=1)
        quer = np.linalg.norm(np.cross(rel, stabnetz.N0), axis=1)
        linie = (quer < 1e-9) & (np.abs(np.abs(nv @ stabnetz.N0) - 1) < 1e-9)
        ab = ~linie
        e = dict(L=L, netz=art)
        e["linie_r_t"] = [[float(a), float(b)] for a, b in sorted(zip(r[linie], t[linie])) if a <= L / 2 + 1e-9]
        e["linie_exponent_1_L4"] = steigung(r[linie], t[linie], 1.0, L / 4)
        e["linie_exponent_3_55"] = steigung(r[linie], t[linie], 3.0, 5.5) if L == 12 else None
        e["abseits_kugel_max_1_L4"] = huelle(r, t, 1.0, L / 4, ab)
        e["abseits_kugel_max_3_55"] = huelle(r, t, 3.0, 5.5, ab) if L == 12 else None
        e["kugel_max_3_55"] = huelle(r, t, 3.0, 5.5, np.ones(len(t), dtype=bool)) if L == 12 else None
        e["abseits_max_abs_t"] = float(np.abs(t[ab]).max())
        # Kugelmittel (quadratisch) ueber weiter aussen liegende Klassen
        kanten = np.arange(0, r.max() + 0.25, 0.25)
        rm = []; rms = []
        for c in range(len(kanten) - 1):
            mk = (r >= kanten[c]) & (r < kanten[c + 1]) & (r > 0)
            if np.any(mk):
                rm.append(np.mean(r[mk])); rms.append(np.sqrt(np.mean(t[mk] ** 2)))
        rm = np.array(rm); rms = np.array(rms)
        e["kugel_rms_1_L4"] = steigung(rm, rms, 1.0, L / 4)
        e["kugel_rms_3_55"] = steigung(rm, rms, 3.0, 5.5) if L == 12 else None
        # Wechselwirkungsenergie zweier Fehlpaesse = -delta t_b (Reziprozitaet): Kontrolle mit zweitem Fehlpass
        b1 = int(np.argmax(np.where(linie & (r > 1.0), 1, 0))) if art == "pyro" else int(np.argmax(np.where(ab & (r > 1.0) & (r < 1.5), np.abs(t), 0)))
        e1 = np.zeros(len(st)); e1[b1] = 1.0
        def energie(eig):
            uu = lsqr(C, eig, atol=1e-15, btol=1e-15, conlim=1e14, iter_lim=200000)[0]
            tt = C @ uu - eig
            return 0.5 * float(np.sum(tt ** 2))
        E01 = energie(e0 + e1); E0_ = energie(e0); E1_ = energie(e1)
        e["zwei_fehlpaesse"] = dict(b1=b1, r=float(r[b1]), E_wechsel=E01 - E0_ - E1_, minus_t_b1=float(-t[b1]),
                                    E_einzel=E0_)
        aus["%s_L%d" % (art, L)] = e

# Spin-Eis gegen Gauss-Gegenprobe
f = os.path.join(ordner, "auswertung.json")
if os.path.exists(f):
    A = json.load(open(f))
    for Ls, e in A["spin_eis"].items():
        if e is None:
            continue
        tab = e["tabelle"]
        lo, hi = e["bereich"]
        T = [x for x in tab if lo <= x["r"] <= hi]
        F = np.array([x["F"] for x in T]); s = np.array([x["sF"] for x in T]); G = np.array([x["FG"] for x in T])
        w = 1 / s ** 2
        X = np.column_stack([np.ones_like(G), G])
        sw = np.sqrt(w)
        c, *_ = np.linalg.lstsq(X * sw[:, None], F * sw, rcond=None)
        chi2 = float(np.sum(w * (F - X @ c) ** 2))
        # auch ueber alle Schalen bis L/2 (nur berichtet)
        T2 = [x for x in tab if x["r"] <= float(Ls) / 2]
        F2 = np.array([x["F"] for x in T2]); s2 = np.array([x["sF"] for x in T2]); G2 = np.array([x["FG"] for x in T2])
        w2 = 1 / s2 ** 2
        X2 = np.column_stack([np.ones_like(G2), G2])
        c2, *_ = np.linalg.lstsq(X2 * np.sqrt(w2)[:, None], F2 * np.sqrt(w2), rcond=None)
        chi22 = float(np.sum(w2 * (F2 - X2 @ c2) ** 2))
        aus["spin_eis_L" + Ls] = dict(bereich=[lo, hi], beta=float(c[1]), alpha=float(c[0]), chi2=chi2, n=len(T),
                                      bis_L_halbe=dict(beta=float(c2[1]), chi2=chi22, n=len(T2),
                                                       max_abw=float(np.abs(F2 - X2 @ c2).max())))

aus["skript_sha256"] = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
aus["ende_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
json.dump(aus, open(ausgabe, "w"), indent=1)
print(json.dumps({k: (v if not isinstance(v, dict) else {kk: vv for kk, vv in v.items() if kk != "linie_r_t"})
                  for k, v in aus.items()}, indent=1))
