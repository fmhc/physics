# FLUSS-1 (Runde 34): mechanische Auswertung nach PLAN.md (Urteile F0 bis F3), nur ueber kleintest.sh.
# Aufruf: auswertung.py <laufordner> <ausgabe.json> <L_haupt> <L_kontrolle>
import sys, os, json, glob, time, hashlib
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import cg

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import gitter
import gitter_fluss as gf

ordner = sys.argv[1]; ausgabe = sys.argv[2]; L_H = int(sys.argv[3]); L_K = int(sys.argv[4])

# ---------------- feste Regeln (PLAN.md) ----------------
R1_PAAR = 1.0                 # F1: Ausgleich ueber r in [1,0; 0,19 L] (Zellkanten)
R2_PAAR_FAKTOR = 0.19
P_GITTER_POT = np.arange(0.05, 6.0 + 1e-9, 0.001)
F1_BEREICH = (0.8, 1.2)
R1_KORR = 1.0                 # F2/F3: Ausgleich ueber r in [1,0; L/4]
R2_KORR_FAKTOR = 0.25
P_GITTER_KORR = np.arange(0.05, 20.0 + 1e-9, 0.001)
LAMBDA_GITTER = np.arange(0.0, 40.0 + 1e-9, 0.001)
F2_BEREICH = (2.5, 3.5)
KANTE = np.sqrt(2.0) / 4.0    # Kantenlaenge beider Netze in Zellkanten
F3_XI_MAX = 3 * KANTE
F3_MIN_SIGNIFIKANT = 4        # Schalen mit R2 > 3 sigma im Bereich (nur berichtet, Schalenform)
JK_GRUPPEN = 10
# Ringform (Urteile F2, F3; nach dem Rauchlauf, PLAN Abschnitt 6): Ringe der Breite 0,25 Zellkanten von R1_RING bis L/4
RING_BREITE = 0.25
R1_RING = {"A": 1.0, "B": 0.8}
MIN_RINGE = 4


def gew_ausgleich_1par(y, w, f):
    """y ~ A f (f: Gitter x Schalen); A linear, gewichtete kleinste Quadrate. Rueckgabe chi2, A je Gitterpunkt."""
    Sy = (w * y * f).sum(1); Sf = (w * f * f).sum(1)
    A = Sy / np.where(Sf > 0, Sf, 1)
    chi2 = (w * y * y).sum() - A * Sy
    return chi2, A


def ausgleich_potenz(r, y, w, quadrat=False):
    if len(r) < 4:
        return dict(p=None, A=None, chi2=None, n=int(len(r)), grund="weniger als 4 Schalen")
    k = 2.0 if quadrat else 1.0
    f = r[None, :] ** (-k * P_GITTER_KORR[:, None])
    chi2, A = gew_ausgleich_1par(y, w, f)
    i = int(np.argmin(chi2))
    return dict(p=float(P_GITTER_KORR[i]), A=float(A[i]), chi2=float(chi2[i]), n=int(len(r)), dof=int(len(r) - 2),
                am_gitterrand=bool(i == 0 or i == len(P_GITTER_KORR) - 1))


def ausgleich_exp(r, y, w, quadrat=False):
    if len(r) < 4:
        return dict(xi=None, A=None, chi2=None, n=int(len(r)), grund="weniger als 4 Schalen")
    k = 2.0 if quadrat else 1.0
    f = np.exp(-k * LAMBDA_GITTER[:, None] * r[None, :])
    chi2, A = gew_ausgleich_1par(y, w, f)
    i = int(np.argmin(chi2))
    lam = float(LAMBDA_GITTER[i])
    return dict(xi=(1.0 / lam if lam > 0 else float("inf")), lam=lam, A=float(A[i]), chi2=float(chi2[i]),
                n=int(len(r)), dof=int(len(r) - 2), am_gitterrand=bool(i == 0 or i == len(LAMBDA_GITTER) - 1),
                xi_in_kanten=(1.0 / lam / KANTE if lam > 0 else float("inf")))


def ausgleich_pot(r, F, w):
    """F1: a - C r^-p, p auf festem Gitter, (a, C) linear (wie EIS-1)."""
    if len(r) < 4:
        return dict(chi2=None, p=float("nan"), a=float("nan"), C=float("nan"), n=int(len(r)),
                    grund="weniger als 4 Schalen im Bereich")
    best = None
    sw = np.sqrt(w)
    for p in P_GITTER_POT:
        X = np.column_stack([np.ones_like(r), -r ** (-p)])
        coef, *_ = np.linalg.lstsq(X * sw[:, None], F * sw, rcond=None)
        chi2 = float(np.sum(w * (F - X @ coef) ** 2))
        if best is None or chi2 < best[0]:
            best = (chi2, float(p), float(coef[0]), float(coef[1]))
    return dict(chi2=best[0], p=best[1], a=best[2], C=best[3], n=int(len(r)), dof=int(len(r) - 3))


# ---------------- F1: Paarpotential, Netz A ----------------
def lap_pyro(net):
    nv = net["nv"]
    i = net["kopf"]; j = net["schwanz"]
    A = sp.coo_matrix((np.ones(len(i)), (i, j)), shape=(nv, nv))
    A = (A + A.T).tocsr()
    return (sp.diags(np.asarray(A.sum(1)).ravel()) - A).tocsr()


def lap_loesen(Lap, b):
    x, info = cg(Lap, b - b.mean(), rtol=1e-12, maxiter=50000)
    x -= x.mean()
    return x, float(np.abs(Lap @ x - (b - b.mean())).max())


def paar_auswerten(L, net):
    dateien = sorted(glob.glob(os.path.join(ordner, "paar_L%d_s*.json" % L)))
    if not dateien:
        return None
    P = net["P"]; ecken = net["ecken"]; nv = net["nv"]
    r2max = 3 * (4 * L) ** 2
    gz = np.zeros(r2max + 1, dtype=np.int64)
    for ref in range(4):
        d = gitter.minbild(ecken - ecken[ref], P).astype(np.int64)
        r2 = np.delete((d ** 2).sum(1), ref)
        gz += np.bincount(r2, minlength=r2max + 1) * (nv // 4)
    paare = nv * (nv - 1)
    bloecke = []; laeufe = []
    for f in dateien:
        meta = json.load(open(f))
        hb = np.load(f.replace(".json", ".npz"))["hist_bloecke"]
        laeufe.append(dict(datei=os.path.basename(f), seed=meta["seed"], bloecke=meta["bloecke"],
                           zaehler=meta["zaehler"], voll_ok=meta["voll_pruefung_bloecke_ok"],
                           einlauf_voll_ok=meta["einlauf_voll_ok"], schritte_je_s=meta["schritte_je_s"],
                           gitter_ok=meta["gitter_pruefung"]["alles_ok"], dauer_s=meta["dauer_s"]))
        for h in hb:
            bloecke.append((meta["seed"], h))
    H = np.array([h for _, h in bloecke], dtype=float)
    nb = len(H)
    Pb = H / H.sum(1)[:, None]
    Pm = H.sum(0) / H.sum()
    Ps = Pb.std(0, ddof=1) / np.sqrt(nb)
    gn = gz / paare
    schalen = np.where((gz > 0) & (Pm > 0))[0]
    r = np.sqrt(schalen) / 8.0
    F = -np.log(Pm[schalen] / gn[schalen])
    sF = Ps[schalen] / Pm[schalen]
    R2 = R2_PAAR_FAKTOR * L
    sel = (r >= R1_PAAR) & (r <= R2)
    w = 1.0 / sF[sel] ** 2
    fit = ausgleich_pot(r[sel], F[sel], w)
    grp = np.array_split(np.arange(nb), JK_GRUPPEN)
    pj = []; Cj = []
    for gi in grp:
        m = np.ones(nb, dtype=bool); m[gi] = False
        Pj = H[m].sum(0) / H[m].sum()
        fj = ausgleich_pot(r[sel], -np.log(Pj[schalen][sel] / gn[schalen][sel]), w)
        pj.append(fj["p"]); Cj.append(fj["C"])
    pj = np.array(pj); Cj = np.array(Cj); k = len(grp)
    sp_ = float(np.sqrt((k - 1) / k * np.sum((pj - pj.mean()) ** 2)))
    sC = float(np.sqrt((k - 1) / k * np.sum((Cj - Cj.mean()) ** 2)))
    # Gauss-Referenz: F_G = 4 K (G(0) - G(r)), K = (E - V + 1)/E, G = Pseudo-Inverse des Ecken-Laplace
    Lap = lap_pyro(net)
    K = (net["ne"] - nv + 1) / net["ne"]
    summe = np.zeros(r2max + 1); anz = np.zeros(r2max + 1); reste = []
    for ref in range(4):
        b = np.zeros(nv); b[ref] = 1.0
        x, rest = lap_loesen(Lap, b); reste.append(rest)
        Fg = 4 * K * (x[ref] - x)
        d = gitter.minbild(ecken - ecken[ref], P).astype(np.int64)
        r2 = (d ** 2).sum(1); m = np.arange(nv) != ref
        summe += np.bincount(r2[m], weights=Fg[m], minlength=r2max + 1)
        anz += np.bincount(r2[m], minlength=r2max + 1)
    with np.errstate(invalid="ignore", divide="ignore"):
        FG = summe / anz
    fitG = ausgleich_pot(r[sel], FG[schalen][sel], w)
    # Lauf gegen Lauf
    lauf_fits = []
    for seed in sorted(set(s for s, _ in bloecke)):
        hs = np.array([h for s, h in bloecke if s == seed], dtype=float).sum(0)
        lauf_fits.append(dict(seed=seed, **ausgleich_pot(r[sel], -np.log(hs[schalen][sel] / hs.sum() / gn[schalen][sel]), w)))
    # nur berichtet: Bereich ab 0,8
    sel8 = (r >= 0.8) & (r <= R2)
    fit8 = ausgleich_pot(r[sel8], F[sel8], 1.0 / sF[sel8] ** 2)
    zs = {}
    for l in laeufe:
        for k2, v in l["zaehler"].items():
            if isinstance(v, list):
                zs[k2] = [a + b for a, b in zip(zs.get(k2, [0] * len(v)), v)]
            else:
                zs[k2] = zs.get(k2, 0) + v
    tab = [dict(r2_1_64=int(s), r=float(rr), g=int(gz[s]), P=float(Pm[s]), F=float(ff), sF=float(ss), FG=float(fg),
                im_bereich=bool(se)) for s, rr, ff, ss, fg, se in zip(schalen, r, F, sF, FG[schalen], sel)]
    return dict(L=L, laeufe=laeufe, bloecke=nb, zaehler_summe=zs, bereich=[R1_PAAR, R2], schalen_im_bereich=int(sel.sum()),
                ausgleich=fit, p_jackknife_sigma=sp_, C_jackknife_sigma=sC, K_gauss=K, cg_rest=reste,
                ausgleich_gauss_referenz=fitG, lauf_gegen_lauf=lauf_fits, nur_berichtet_ab_0_8=fit8, tabelle=tab)


# ---------------- F2/F3: Korrelationen ----------------
def gauss_D(net, schalen_r2, nsch):
    """Gauss-Naeherung fuer Netz A: <b_e b_e'> = -(x[kopf'] - x[schwanz'])/K mit x = Lap^+ (e_kopf - e_schwanz),
    K = Diagonale des Projektors auf divergenzfreie Felder. P2-Projektion je Schale wie im Monte Carlo."""
    Lap = lap_pyro(net); P = net["P"]
    num = np.zeros(nsch); den = np.zeros(nsch); Ks = []
    for c in range(6):
        sel = np.where(net["kl"] == c)[0]
        mi = net["mitte"][sel]
        d0 = gitter.minbild(mi - mi[0], P).astype(np.int64)
        typ = np.all(d0 % 4 == 0, axis=1) & ((d0 // 4).sum(1) % 2 == 0)
        refs = [sel[np.where(typ)[0][0]], sel[np.where(~typ)[0][0]]]
        for e in refs:
            b = np.zeros(net["nv"]); b[net["kopf"][e]] += 1.0; b[net["schwanz"][e]] -= 1.0
            x, _ = lap_loesen(Lap, b)
            Kd = 1.0 - (x[net["kopf"][e]] - x[net["schwanz"][e]])
            Ks.append(float(Kd))
            corr = -(x[net["kopf"][sel]] - x[net["schwanz"][sel]]) / Kd
            d = gitter.minbild(net["mitte"][sel] - net["mitte"][e], P).astype(np.int64)
            r2 = (d ** 2).sum(1)
            nc = gf.KLASSEN[c]
            dot = (d * nc[None, :]).sum(1).astype(float)
            with np.errstate(invalid="ignore", divide="ignore"):
                p2 = np.where(r2 > 0, 1.5 * dot ** 2 / (2.0 * r2) - 0.5, 0.0)
            m = r2 > 0
            num += np.bincount(r2[m], weights=(corr * p2)[m], minlength=nsch)
            den += np.bincount(r2[m], weights=(p2 * p2)[m], minlength=nsch)
    with np.errstate(invalid="ignore", divide="ignore"):
        DG = np.where(den > 0, num / np.where(den > 0, den, 1), np.nan)
    return DG, Ks


def korr_laden(netz, L):
    dateien = sorted(glob.glob(os.path.join(ordner, "korr_%s_L%d_s*.json" % (netz, L))))
    out = []
    for f in dateien:
        meta = json.load(open(f)); z = np.load(f.replace(".json", ".npz"))
        out.append((meta, {k: z[k] for k in z.files}))
    return out


def schalen_groessen(d):
    B = d["num_d"].shape[0]
    r2 = d["r2"]; r = np.sqrt(r2) / 8.0
    erg = {}
    for name, num, den in (("D", d["num_d"], d["den_d"]), ("Cbar", d["num_bar"], d["den_bar"]),
                           ("Cax", d["num_ax"], d["den_ax"]), ("Csenk", d["num_senk"], d["den_senk"])):
        ok = den > 1e-12
        vals = np.where(ok[None, :], num / np.where(ok, den, 1)[None, :], np.nan)
        erg[name] = (vals.mean(0), vals.std(0, ddof=1) / np.sqrt(B), ok)
    for name in ("R2_alle", "R2_abw"):
        if name in d:
            jk = d[name + "_jk"]
            s = np.sqrt((B - 1) / B * ((jk - jk.mean(0)) ** 2).sum(0))
            erg[name] = (d[name], s, d["den_bar"] > 0)
    return r, erg, B


def ring_kanten(L, netz):
    r1 = R1_RING[netz]; r2 = R2_KORR_FAKTOR * L
    k = np.arange(r1, r2 + 1e-9, RING_BREITE)
    if k[-1] < r2 - 1e-9:
        k = np.append(k, r2)
    return k


def ring_index(r, kanten):
    """Ring j fuer lo <= r < hi; der letzte Ring schliesst hi ein; ausserhalb -1."""
    j = np.searchsorted(kanten, r, side="right") - 1
    j[(r == kanten[-1])] = len(kanten) - 2
    j[(r < kanten[0]) | (r > kanten[-1])] = -1
    return j


def ring_log_ausgleich(rq, y, s, quadrat=False):
    """Ringform (Urteil): ln y linear gegen ln r (Potenz) bzw. gegen r (exponentiell), ungewichtet, nur Ringe mit
    y > 2 sigma. Vergleich der Restquadratsummen."""
    m = np.isfinite(y) & np.isfinite(s) & (y > 2 * s) & (y > 0)
    n = int(m.sum())
    aus = dict(ringe_signifikant=n, ringe_gesamt=int(len(y)))
    if n < MIN_RINGE:
        aus["grund"] = "weniger als %d signifikante Ringe" % MIN_RINGE
        return aus
    Y = np.log(y[m]); k = 2.0 if quadrat else 1.0
    out = {}
    for name, X in (("potenz", np.log(rq[m])), ("exponentiell", rq[m])):
        A = np.column_stack([np.ones_like(X), X])
        c, *_ = np.linalg.lstsq(A, Y, rcond=None)
        rss = float(np.sum((Y - A @ c) ** 2))
        out[name] = dict(steigung=float(c[1]), achse=float(c[0]), rss=rss)
    aus["potenz"] = dict(p=float(-out["potenz"]["steigung"] / k), rss=out["potenz"]["rss"])
    lam = -out["exponentiell"]["steigung"] / k
    aus["exponentiell"] = dict(xi=(1.0 / lam if lam > 0 else float("inf")), lam=float(lam),
                               xi_in_kanten=(1.0 / lam / KANTE if lam > 0 else float("inf")), rss=out["exponentiell"]["rss"])
    aus["ringe_r"] = [float(x) for x in rq[m]]; aus["ringe_y"] = [float(x) for x in y[m]]
    return aus


def ringe_bilden_quotient(r, num_bl, den, kanten):
    """Quotienten-Groessen (D, Cbar, ...): je Block Summe Zaehler / Summe Nenner im Ring."""
    j = ring_index(r, kanten); nr = len(kanten) - 1
    ok = (j >= 0) & (den > 1e-12)
    dsum = np.bincount(j[ok], weights=den[ok], minlength=nr)
    rq = np.bincount(j[ok], weights=(den * r)[ok], minlength=nr) / np.where(dsum > 0, dsum, 1)
    vals = np.array([np.bincount(j[ok], weights=nb[ok], minlength=nr) for nb in num_bl]) / np.where(dsum > 0, dsum, 1)
    B = len(num_bl)
    return rq, vals.mean(0), vals.std(0, ddof=1) / np.sqrt(B), dsum > 0


def ringe_bilden_quadrat(r, R2, R2jk, den, kanten):
    j = ring_index(r, kanten); nr = len(kanten) - 1
    ok = (j >= 0) & (den > 0)
    dsum = np.bincount(j[ok], weights=den[ok], minlength=nr)
    dn = np.where(dsum > 0, dsum, 1)
    rq = np.bincount(j[ok], weights=(den * r)[ok], minlength=nr) / dn
    y = np.bincount(j[ok], weights=(den * R2)[ok], minlength=nr) / dn
    jk = np.array([np.bincount(j[ok], weights=(den * x)[ok], minlength=nr) / dn for x in R2jk])
    B = len(R2jk)
    s = np.sqrt((B - 1) / B * ((jk - jk.mean(0)) ** 2).sum(0))
    return rq, y, s, dsum > 0


def ausgleiche(r, y, s, ok, L, quadrat=False):
    sel = ok & (r >= R1_KORR) & (r <= R2_KORR_FAKTOR * L) & np.isfinite(y) & (s > 0)
    rr, yy, ww = r[sel], y[sel], 1.0 / s[sel] ** 2
    sig = int(np.sum(yy > 3 * s[sel]))
    return dict(bereich=[R1_KORR, R2_KORR_FAKTOR * L], schalen=int(sel.sum()), signifikant_3sigma=sig,
                potenz=ausgleich_potenz(rr, yy, ww, quadrat), exponentiell=ausgleich_exp(rr, yy, ww, quadrat))


def korr_auswerten(netz, L, net):
    laeufe = korr_laden(netz, L)
    if not laeufe:
        return None
    einzel = []; pool = None
    for meta, d in laeufe:
        r, g, B = schalen_groessen(d)
        einzel.append((meta, r, g, B, d))
    # gepoolt: Mittel der Laeufe (gleiche Bauart), Fehler quadratisch
    r = einzel[0][1]
    pool = {}
    for name in einzel[0][2]:
        ys = np.array([e[2][name][0] for e in einzel]); ss = np.array([e[2][name][1] for e in einzel])
        oks = np.all(np.array([e[2][name][2] for e in einzel]), axis=0)
        pool[name] = (np.nanmean(ys, 0), np.sqrt((ss ** 2).sum(0)) / len(einzel), oks)
    aus = dict(netz=netz, L=L, laeufe=[], gepoolt={})
    for meta, rr, g, B, d in einzel:
        e = dict(datei="korr_%s_L%d_s%d" % (netz, L, meta["seed"]), seed=meta["seed"], start=meta["start"], bloecke=B,
                 messungen=meta["messungen"], tau_int_messabstaende=meta["tau_int_messabstaende"], mittel=meta["mittel"],
                 regel_fehler_lokal=meta["regel_fehler_lokal"], voll_pruefung_fehler=meta["voll_pruefung_fehler"],
                 gitter_ok=meta["gitter_pruefung"]["alles_ok"], start_info=meta["start_info"],
                 einheiten_je_messung=meta["einheiten_je_messung"], zaehler=meta["zaehler"])
        e["D"] = ausgleiche(rr, g["D"][0], g["D"][1], g["D"][2], L)
        if "R2_alle" in g:
            e["R2_alle"] = ausgleiche(rr, g["R2_alle"][0], g["R2_alle"][1], g["R2_alle"][2], L, quadrat=True)
        # Pinch-Kennzahl: S_xx bei kleinstem k entlang z gegen entlang x
        Sxx = d["Sxx"]; kx = d["kx_idx"]; kz = d["kz_idx"]
        ix1 = int(np.where(kx == 1)[0][0]); ix0 = int(np.where(kx == 0)[0][0])
        e["pinch_Sxx_kz_min"] = float(Sxx[ix0, 1]); e["pinch_Sxx_kx_min"] = float(Sxx[ix1, 0])
        e["pinch_verhaeltnis"] = float(Sxx[ix0, 1] / Sxx[ix1, 0]) if Sxx[ix1, 0] > 0 else None
        aus["laeufe"].append(e)
    for name, (y, s, ok) in pool.items():
        aus["gepoolt"][name] = ausgleiche(r, y, s, ok, L, quadrat=name.startswith("R2"))
    # Tabelle (gepoolt) bis L/2
    sel = pool["Cbar"][2] & (r > 0) & (r <= L / 2.0)
    tab = []
    for i in np.where(sel)[0]:
        row = dict(r2_1_64=int(i), r=float(r[i]))
        for name, (y, s, ok) in pool.items():
            row[name] = float(y[i]) if ok[i] and np.isfinite(y[i]) else None
            row["s_" + name] = float(s[i]) if ok[i] and np.isfinite(s[i]) else None
        tab.append(row)
    aus["tabelle"] = tab
    # Ringform (Urteilsform): Ringe gleicher Breite, je Lauf gebildet, dann ueber Laeufe gemittelt
    kanten = ring_kanten(L, netz)
    ringe = {}
    for name in ("D", "Cbar", "Cax"):
        rqs = []; ys = []; ss = []; oks = []
        for meta, rr, g, B, d in einzel:
            numk = {"D": "num_d", "Cbar": "num_bar", "Cax": "num_ax"}[name]
            denk = {"D": "den_d", "Cbar": "den_bar", "Cax": "den_ax"}[name]
            rq, y, s, ok = ringe_bilden_quotient(rr, d[numk], d[denk], kanten)
            rqs.append(rq); ys.append(y); ss.append(s); oks.append(ok)
        y = np.mean(ys, 0); s = np.sqrt((np.array(ss) ** 2).sum(0)) / len(ss); rq = rqs[0]; ok = np.all(oks, 0)
        y = np.where(ok, y, np.nan)
        ringe[name] = dict(r=[float(x) for x in rq], y=[float(x) for x in y], s=[float(x) for x in s],
                           ausgleich=ring_log_ausgleich(rq, y, s))
    if all("R2_alle" in e_[4] for e_ in einzel):
        rqs = []; ys = []; ss = []; oks = []
        for meta, rr, g, B, d in einzel:
            rq, y, s, ok = ringe_bilden_quadrat(rr, d["R2_alle"], d["R2_alle_jk"], d["den_bar"], kanten)
            rqs.append(rq); ys.append(y); ss.append(s); oks.append(ok)
        y = np.mean(ys, 0); s = np.sqrt((np.array(ss) ** 2).sum(0)) / len(ss); rq = rqs[0]; ok = np.all(oks, 0)
        y = np.where(ok, y, np.nan)
        ringe["R2_alle"] = dict(r=[float(x) for x in rq], y=[float(x) for x in y], s=[float(x) for x in s],
                                ausgleich=ring_log_ausgleich(rq, y, s, quadrat=True))
    aus["ringe"] = dict(kanten=[float(x) for x in kanten], **ringe)
    if netz == "A":
        DG, Ks = gauss_D(net, r, len(r))
        y, s, ok = pool["D"]
        sel = ok & (r >= R1_KORR) & (r <= R2_KORR_FAKTOR * L) & np.isfinite(DG) & (s > 0)
        ww = 1.0 / s[sel] ** 2
        # Ringform der Gauss-Referenz: dieselben Ringe, Gewicht Nenner der P2-Projektion
        okg = np.isfinite(DG) & (einzel[0][4]["den_d"] > 1e-12)
        dd = einzel[0][4]["den_d"]
        rqg, yg, sg_, okr = ringe_bilden_quotient(r, np.array([np.where(okg, DG * dd, 0.0)] * 2),
                                                   np.where(okg, dd, 0.0), kanten)
        sg_ = np.full_like(yg, 1e-30)
        aus["gauss_referenz_D"] = dict(K_diagonale=[min(Ks), max(Ks)],
                                       potenz=ausgleich_potenz(r[sel], DG[sel], ww),
                                       exponentiell=ausgleich_exp(r[sel], DG[sel], ww),
                                       ringform=dict(r=[float(x) for x in rqg], y=[float(x) for x in yg],
                                                     ausgleich=ring_log_ausgleich(rqg, np.where(okr, yg, np.nan), sg_)))
        for row in tab:
            row["D_gauss"] = float(DG[row["r2_1_64"]]) if np.isfinite(DG[row["r2_1_64"]]) else None
    aus["_pool"] = pool; aus["_r"] = r; aus["_einzel"] = einzel
    return aus


# ---------------- Hauptteil ----------------
t0 = time.time()
netA = {L: gf.netz_a(L) for L in (L_H, L_K)}
paar = {L: paar_auswerten(L, netA[L]) for L in (L_H, L_K)}
korrA = {L: korr_auswerten("A", L, netA[L]) for L in (L_H, L_K)}
korrB = {L: korr_auswerten("B", L, None) for L in (L_H, L_K)}

urteile = {}
# F0: Regeln und Gitterzahlen in allen echten Laeufen
f0 = dict(laeufe=[])
ok_all = True
for f in sorted(glob.glob(os.path.join(ordner, "*.json"))):
    if os.path.basename(f).startswith("auswertung"):
        continue
    m = json.load(open(f))
    if m.get("modus") == "paar":
        ok = (m["gitter_pruefung"]["alles_ok"] and m["eis_anfang_ok"] and m["paar_nach_umklapp_ok"]
              and m["einlauf_voll_ok"] and m["voll_pruefung_bloecke_ok"] and m["zaehler"]["eisregel_fehler_lokal"] == 0)
    elif m.get("modus") == "korr":
        st = m["start_info"]
        ok = (m["gitter_pruefung"]["alles_ok"] and m["regel_fehler_lokal"] == 0 and m["voll_pruefung_fehler"] == 0
              and (st.get("eis_anfang_ok", True)) and (st.get("anfang_q_pm1", True)))
    else:
        continue
    f0["laeufe"].append(dict(datei=os.path.basename(f), ok=bool(ok)))
    ok_all = ok_all and bool(ok)
urteile["F0"] = dict(urteil=("eingetroffen" if (ok_all and f0["laeufe"]) else "nicht eingetroffen"), **f0,
                     regel="alle echten Laeufe: Gitterzahlen ok, Regel-Fehler lokal 0, Vollpruefungen ok")
# F1
e = paar.get(L_H)
if e is None or e["ausgleich"]["chi2"] is None:
    urteile["F1"] = dict(urteil="nicht auswertbar")
else:
    p, C = e["ausgleich"]["p"], e["ausgleich"]["C"]
    ok = (C > 0) and (F1_BEREICH[0] <= p <= F1_BEREICH[1])
    urteile["F1"] = dict(urteil="eingetroffen" if ok else "nicht eingetroffen", L=L_H, p=p, C=C,
                         p_sigma_jackknife=e["p_jackknife_sigma"], regel="C > 0 und p in [0,8; 1,2] bei L = %d" % L_H)
# F2 (Ringform, D(r), Netz A)
k = korrA.get(L_H)
if k is None:
    urteile["F2"] = dict(urteil="nicht auswertbar")
else:
    a = k["ringe"]["D"]["ausgleich"]
    if "potenz" not in a:
        urteile["F2"] = dict(urteil="nicht auswertbar", grund=a.get("grund"), ringe_signifikant=a["ringe_signifikant"])
    else:
        po, ex = a["potenz"], a["exponentiell"]
        ok = (po["rss"] <= ex["rss"]) and (F2_BEREICH[0] <= po["p"] <= F2_BEREICH[1])
        urteile["F2"] = dict(urteil="eingetroffen" if ok else "nicht eingetroffen", L=L_H, p=po["p"],
                             rss_potenz=po["rss"], rss_exp=ex["rss"], xi_exp=ex["xi"],
                             ringe_signifikant=a["ringe_signifikant"], ringe_gesamt=a["ringe_gesamt"],
                             regel="Ringform von D(r) auf [1,0; L/4]: RSS(ln D gegen ln r) <= RSS(ln D gegen r) und "
                                   "p in [2,5; 3,5] bei L = %d" % L_H)
# F3 (Ringform, R2(r), Netz B)
k = korrB.get(L_H)
if k is None or "R2_alle" not in k["ringe"]:
    urteile["F3"] = dict(urteil="nicht auswertbar")
else:
    a = k["ringe"]["R2_alle"]["ausgleich"]
    if "potenz" not in a:
        urteile["F3"] = dict(urteil="nicht auswertbar", grund=a.get("grund"), ringe_signifikant=a["ringe_signifikant"])
    else:
        po, ex = a["potenz"], a["exponentiell"]
        ok = (ex["rss"] < po["rss"]) and (0 < ex["xi"] <= F3_XI_MAX)
        urteile["F3"] = dict(urteil="eingetroffen" if ok else "nicht eingetroffen", L=L_H, xi=ex["xi"],
                             xi_in_kanten=ex["xi_in_kanten"], rss_exp=ex["rss"], rss_potenz=po["rss"], p_potenz=po["p"],
                             ringe_signifikant=a["ringe_signifikant"], ringe_gesamt=a["ringe_gesamt"],
                             regel="Ringform von R2(r) auf [0,8; L/4]: RSS(ln R2 gegen r) < RSS(ln R2 gegen ln r) und "
                                   "0 < xi <= 3 Kanten (%.4f Zellkanten) bei L = %d" % (F3_XI_MAX, L_H))


def ohne_intern(x):
    return {k: v for k, v in x.items() if not k.startswith("_")} if x else x


aus = dict(karte="FLUSS-1", urteile=urteile, paar={str(k): v for k, v in paar.items()},
           korr_A={str(k): ohne_intern(v) for k, v in korrA.items()},
           korr_B={str(k): ohne_intern(v) for k, v in korrB.items()},
           regeln=dict(R1_PAAR=R1_PAAR, R2_PAAR_FAKTOR=R2_PAAR_FAKTOR, F1=F1_BEREICH, R1_KORR=R1_KORR,
                       R2_KORR_FAKTOR=R2_KORR_FAKTOR, F2=F2_BEREICH, F3_XI_MAX_zellkanten=F3_XI_MAX,
                       F3_MIN_SIGNIFIKANT=F3_MIN_SIGNIFIKANT, p_gitter_korr=[0.05, 20.0, 0.001],
                       lambda_gitter=[0.0, 40.0, 0.001], p_gitter_pot=[0.05, 6.0, 0.001]),
           skript_sha256=hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
           dauer_s=time.time() - t0, ende_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
json.dump(aus, open(ausgabe, "w"), indent=1)
print(json.dumps(urteile, indent=1))

# ---------------- kleine Bilder (nur Darstellung) ----------------
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    basis = ausgabe.replace(".json", "")
    # F(r)
    fig, ax = plt.subplots(figsize=(5, 3.6))
    for L, e in paar.items():
        if e is None:
            continue
        rr = np.array([t["r"] for t in e["tabelle"]]); FF = np.array([t["F"] for t in e["tabelle"]])
        ss = np.array([t["sF"] for t in e["tabelle"]]); FG = np.array([t["FG"] for t in e["tabelle"]])
        m = rr <= L / 2
        ax.errorbar(rr[m], FF[m] - e["ausgleich"]["a"], ss[m], fmt=".", ms=3, label="L=%d MC" % L)
        ax.plot(rr[m], FG[m] - e["ausgleich_gauss_referenz"]["a"], "x", ms=3, label="L=%d Gauss" % L)
        if L == L_H and e["ausgleich"]["chi2"] is not None:
            xx = np.linspace(e["bereich"][0], e["bereich"][1], 50)
            ax.plot(xx, -e["ausgleich"]["C"] * xx ** (-e["ausgleich"]["p"]), "k-", lw=1,
                    label="a - C r^-p, p=%.2f" % e["ausgleich"]["p"])
    ax.set_xlabel("r (Zellkanten)"); ax.set_ylabel("F(r) - a"); ax.legend(fontsize=7)
    ax.set_title("Netz A: Defektpaar q = +-2", fontsize=9)
    fig.tight_layout(); fig.savefig(basis + "-F.png", dpi=85); plt.close(fig)
    # Korrelationen
    fig, axs = plt.subplots(1, 2, figsize=(9, 3.6))
    for L, k in korrA.items():
        if k is None:
            continue
        r = k["_r"]; y, s, ok = k["_pool"]["D"]
        m = ok & (r >= 0.3) & (r <= L / 2) & (y > 0)
        axs[0].errorbar(r[m], y[m], s[m], fmt=".", ms=3, label="A L=%d D(r)" % L)
        if L == L_H:
            po = k["gepoolt"]["D"]["potenz"]
            if po["p"] is not None:
                xx = np.linspace(R1_KORR, R2_KORR_FAKTOR * L, 50)
                axs[0].plot(xx, po["A"] * xx ** (-po["p"]), "k-", lw=1, label="A r^-p, p=%.2f" % po["p"])
            tabr = np.array([t["r"] for t in k["tabelle"]]); dg = np.array([t.get("D_gauss") or np.nan for t in k["tabelle"]])
            mm = (tabr >= 0.3) & (dg > 0)
            axs[0].plot(tabr[mm], dg[mm], "x", ms=3, label="Gauss L=%d" % L)
    axs[0].set_xscale("log"); axs[0].set_yscale("log")
    axs[0].set_xlabel("r (Zellkanten)"); axs[0].set_ylabel("D(r)  (P2-Anteil von <s s'>)")
    axs[0].set_title("Netz A (Pyrochlor-Kanten)", fontsize=9); axs[0].legend(fontsize=6)
    for L, k in korrB.items():
        if k is None or "R2_alle" not in k["_pool"]:
            continue
        r = k["_r"]; y, s, ok = k["_pool"]["R2_alle"]
        m = ok & (r >= 0.3) & (r <= L / 2) & (y > 0)
        axs[1].errorbar(r[m], np.sqrt(y[m]), s[m] / (2 * np.sqrt(y[m])), fmt=".", ms=3, label="B L=%d" % L)
        if L == L_H:
            g = k["gepoolt"]["R2_alle"]
            xx = np.linspace(R1_KORR, R2_KORR_FAKTOR * L, 50)
            if g["exponentiell"]["A"] is not None and g["exponentiell"]["A"] > 0:
                axs[1].plot(xx, np.sqrt(g["exponentiell"]["A"]) * np.exp(-g["exponentiell"]["lam"] * xx), "k-", lw=1,
                            label="exp, xi=%.3f" % g["exponentiell"]["xi"])
            if g["potenz"]["A"] is not None and g["potenz"]["A"] > 0:
                axs[1].plot(xx, np.sqrt(g["potenz"]["A"]) * xx ** (-g["potenz"]["p"]), "k--", lw=1,
                            label="Potenz, p=%.2f" % g["potenz"]["p"])
    for L, k in korrA.items():
        if k is None or "R2_alle" not in k["_pool"]:
            continue
        r = k["_r"]; y, s, ok = k["_pool"]["R2_alle"]
        m = ok & (r >= 0.3) & (r <= L / 2) & (y > 0)
        axs[1].plot(r[m], np.sqrt(y[m]), ".", ms=2, alpha=0.5, label="A L=%d (Vergleich)" % L)
    axs[1].set_yscale("log"); axs[1].set_xlabel("r (Zellkanten)"); axs[1].set_ylabel("sqrt(R2(r)) = Schalen-RMS von C")
    axs[1].set_title("Netz B (srs, K4-Kristall)", fontsize=9); axs[1].legend(fontsize=6)
    fig.tight_layout(); fig.savefig(basis + "-korr.png", dpi=85); plt.close(fig)
    # Strukturfaktor-Schnitt
    fig, axs = plt.subplots(1, 2, figsize=(8, 3.6))
    for a_, (name, kk) in zip(axs, (("A", korrA.get(L_H)), ("B", korrB.get(L_H)))):
        if kk is None:
            continue
        meta, rr, g, B, d = kk["_einzel"][0]
        Sxx = d["Sxx"]; kx = d["kx_idx"]; kz = d["kz_idx"]
        o = np.argsort(kx)
        img = Sxx[o, :]
        full = np.concatenate([img[:, :0:-1], img], axis=1) if img.shape[1] > 1 else img
        a_.imshow(full.T, origin="lower", aspect="auto", cmap="viridis",
                  extent=[kx[o][0] / L - 0.5 / L, kx[o][-1] / L + 0.5 / L, -kz[-1] / L - 0.5 / L, kz[-1] / L + 0.5 / L])
        a_.set_xlabel("h (k_x in 2 pi / Zellkante)"); a_.set_ylabel("l (k_z)")
        a_.set_title("Netz %s, L=%d: S_xx(h,0,l)" % (name, L_H), fontsize=9)
    fig.tight_layout(); fig.savefig(basis + "-pinch.png", dpi=85); plt.close(fig)
except Exception as ex:
    print("Bild nicht erstellt:", repr(ex))
