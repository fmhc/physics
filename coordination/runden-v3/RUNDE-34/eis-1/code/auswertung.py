# EIS-1 (Runde 34): mechanische Auswertung nach PLAN.md (Urteile E0 bis E3), nur ueber kleintest.sh.
# Aufruf: auswertung.py <laufordner> <ausgabe.json> [L_haupt_eis L_kontrolle_eis L_haupt_stab L_kontrolle_stab L_zaehlen_csv]
import sys, os, json, glob, time, hashlib
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import cg

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import gitter

ordner = sys.argv[1]; ausgabe = sys.argv[2]
if len(sys.argv) > 3:
    L_EIS = int(sys.argv[3]); L_EIS_K = int(sys.argv[4]); L_STAB = int(sys.argv[5]); L_STAB_K = int(sys.argv[6])
    L_ZAEHL = [int(x) for x in sys.argv[7].split(",")]
else:
    L_EIS, L_EIS_K, L_STAB, L_STAB_K, L_ZAEHL = 12, 8, 12, 8, [3, 4, 5]

# ---------------- feste Regeln (PLAN.md) ----------------
R1_EIS = 1.15                # Ausgleichsbereich Spin-Eis: r in [1,15; 0,19 L] (Zellkanten); nach dem Rauchlauf, PLAN 6
R1_EIS_ALT = 0.8             # urspruengliche Untergrenze (vor dem Rauchlauf), nur berichtet
R2_EIS_FAKTOR = 0.19
P_GITTER = np.arange(0.05, 6.0 + 1e-9, 0.001)
E0_BEREICH = (0.8, 1.2)
R1_STAB = 1.0                # Ausgleichsbereich Stabnetze: Klassenmitte in [1,0; L/4]
R2_STAB_FAKTOR = 0.25
SCHWELLE = 1e-9
MIN_KLASSEN = 3
E1_BEREICH = (2.5, 3.5)
E2_GRENZE = 1.5
JK_GRUPPEN = 10


def ausgleich_pot(r, F, w):
    """a - C r^-p, gewichtete kleinste Quadrate; p auf festem Gitter, (a, C) linear."""
    if len(r) < 4:
        return dict(chi2=None, p=float("nan"), a=float("nan"), C=float("nan"), n=int(len(r)), dof=int(len(r) - 3),
                    grund="weniger als 4 Schalen im Bereich")
    best = None
    for p in P_GITTER:
        X = np.column_stack([np.ones_like(r), -r ** (-p)])
        sw = np.sqrt(w)
        coef, *_ = np.linalg.lstsq(X * sw[:, None], F * sw, rcond=None)
        chi2 = float(np.sum(w * (F - X @ coef) ** 2))
        if best is None or chi2 < best[0]:
            best = (chi2, float(p), float(coef[0]), float(coef[1]))
    return dict(chi2=best[0], p=best[1], a=best[2], C=best[3], n=int(len(r)), dof=int(len(r) - 3))


# ---------------- Teil 1: Spin-Eis ----------------
def abstaende_g(L):
    g = gitter.pyrochlor(L)
    nup, P = g["nup"], g["P"]
    tk = g["tkoord"]
    r2max = 3 * (4 * L) ** 2
    gz = np.zeros(r2max + 1, dtype=np.int64)
    for ref in (0, nup):
        d = np.abs(gitter.minbild(tk - tk[ref], P)).astype(np.int64)
        r2 = (d ** 2).sum(1)
        r2 = np.delete(r2, ref)
        gz += np.bincount(r2, minlength=r2max + 1) * nup
    return g, gz


def gauss_referenz(g, L):
    """Gitter-Coulomb (Gauss-Naeherung): F_G = 2 (G(0) - G(r)), G = Pseudo-Inverse des Diamant-Laplace auf dem Torus."""
    nup, P = g["nup"], g["P"]
    nt = 2 * nup
    i = g["tup"]; j = g["tdown"]
    A = sp.coo_matrix((np.ones(len(i)), (i, j)), shape=(nt, nt))
    A = (A + A.T).tocsr()
    Lap = sp.diags(np.asarray(A.sum(1)).ravel()) - A
    r2max = 3 * (4 * L) ** 2
    summe = np.zeros(r2max + 1); anz = np.zeros(r2max + 1)
    rest = []
    for ref in (0, nup):
        b = -np.ones(nt) / nt; b[ref] += 1.0
        x, info = cg(Lap, b, rtol=1e-12, maxiter=20000)
        x -= x.mean()
        rest.append(float(np.abs(Lap @ x - b).max()))
        Fg = 2 * (x[ref] - x)
        d = np.abs(gitter.minbild(g["tkoord"] - g["tkoord"][ref], P)).astype(np.int64)
        r2 = (d ** 2).sum(1)
        m = np.arange(nt) != ref
        summe += np.bincount(r2[m], weights=Fg[m], minlength=r2max + 1)
        anz += np.bincount(r2[m], minlength=r2max + 1)
    with np.errstate(invalid="ignore", divide="ignore"):
        FG = summe / anz
    return FG, rest


def eis_auswerten(L):
    dateien = sorted(glob.glob(os.path.join(ordner, "eis_L%d_s*.json" % L)))
    if not dateien:
        return None
    g, gz = abstaende_g(L)
    nt = 2 * g["nup"]
    paare = nt * (nt - 1)
    bloecke = []; laeufe = []; zaehler = {}
    for f in dateien:
        meta = json.load(open(f))
        hb = np.load(f.replace(".json", ".npz"))["hist_bloecke"]
        laeufe.append(dict(datei=os.path.basename(f), seed=meta["seed"], bloecke=meta["bloecke"],
                           stichproben=meta["zaehler"]["stichproben"], zaehler=meta["zaehler"],
                           eisregel_lokal=meta["zaehler"]["eisregel_fehler_lokal"],
                           voll_ok=meta["voll_pruefung_bloecke_ok"], einlauf_voll_ok=meta["einlauf_voll_ok"],
                           moment_anfang=meta["moment_anfang_betrag"], moment_ende=meta["moment_ende_betrag"],
                           moment_verlauf=meta["moment_verlauf"], schritte_je_s=meta["schritte_je_s"],
                           gitter=meta["gitter_pruefung"], dauer_s=meta["dauer_s"]))
        for h in hb:
            bloecke.append((meta["seed"], h))
    H = np.array([h for _, h in bloecke], dtype=float)
    n_je = H.sum(1)
    Pb = H / n_je[:, None]
    Pm = H.sum(0) / H.sum()
    nb = len(H)
    Ps = Pb.std(0, ddof=1) / np.sqrt(nb)
    gn = gz / paare
    shells = np.where((gz > 0) & (Pm > 0))[0]
    r = np.sqrt(shells) / 8.0
    F = -np.log(Pm[shells] / gn[shells])
    sF = Ps[shells] / Pm[shells]
    R2 = R2_EIS_FAKTOR * L
    sel = (r >= R1_EIS) & (r <= R2)
    w = 1.0 / sF[sel] ** 2
    fit = ausgleich_pot(r[sel], F[sel], w)
    # Jackknife ueber Blockgruppen
    grp = np.array_split(np.arange(nb), JK_GRUPPEN)
    pj = []; Cj = []
    for gi in grp:
        m = np.ones(nb, dtype=bool); m[gi] = False
        Pj = H[m].sum(0) / H[m].sum()
        Fj = -np.log(Pj[shells][sel] / gn[shells][sel])
        fj = ausgleich_pot(r[sel], Fj, w)
        pj.append(fj["p"]); Cj.append(fj["C"])
    pj = np.array(pj); Cj = np.array(Cj)
    k = len(grp)
    sp_ = float(np.sqrt((k - 1) / k * np.sum((pj - pj.mean()) ** 2)))
    sC = float(np.sqrt((k - 1) / k * np.sum((Cj - Cj.mean()) ** 2)))
    # erste gegen zweite Haelfte der Bloecke je Lauf, und Lauf gegen Lauf
    haelften = []
    for seed in sorted(set(s for s, _ in bloecke)):
        hs = np.array([h for s, h in bloecke if s == seed], dtype=float)
        a, b = hs[: len(hs) // 2].sum(0), hs[len(hs) // 2:].sum(0)
        Fa = -np.log(a[shells][sel] / a.sum() / gn[shells][sel]); Fb = -np.log(b[shells][sel] / b.sum() / gn[shells][sel])
        if sel.sum() == 0:
            continue
        da = (Fa - Fa.mean()) - (Fb - Fb.mean())
        haelften.append(dict(seed=seed, max_abw=float(np.abs(da).max()), chi2_je_schale=float(np.mean((da / (np.sqrt(2) * sF[sel] * np.sqrt(nb / max(len(hs), 1)))) ** 2))))
    # Gauss-Referenz durch dieselbe Ausgleichsroutine (gleiche Schalen, gleiche Gewichte)
    FG, cg_rest = gauss_referenz(g, L)
    FGs = FG[shells]
    fitG = ausgleich_pot(r[sel], FGs[sel], w)
    # nur berichtet: urspruengliche Untergrenze 0,8
    sel_alt = (r >= R1_EIS_ALT) & (r <= R2)
    w_alt = 1.0 / sF[sel_alt] ** 2
    fit_alt = ausgleich_pot(r[sel_alt], F[sel_alt], w_alt)
    fitG_alt = ausgleich_pot(r[sel_alt], FGs[sel_alt], w_alt)
    # Lauf gegen Lauf
    seeds = sorted(set(s for s, _ in bloecke))
    lauf_fits = []
    for seed in seeds:
        hs = np.array([h for s, h in bloecke if s == seed], dtype=float).sum(0)
        Fs = -np.log(hs[shells][sel] / hs.sum() / gn[shells][sel])
        lauf_fits.append(dict(seed=seed, **ausgleich_pot(r[sel], Fs, w)))
    # Art-Kontrolle: gleiche gegen verschiedene Tetraederart (r2 = 0 mod 16: gleiche Art)
    gleich_art = (shells % 16 == 0)
    tab = [dict(r2_1_64=int(s), r=float(rr), g=int(gz[s]), P=float(Pm[s]), F=float(ff), sF=float(ss), FG=float(fg),
                gleiche_art=bool(ga), im_bereich=bool(se))
           for s, rr, ff, ss, fg, ga, se in zip(shells, r, F, sF, FGs, gleich_art, sel)]
    ges = {k2: int(sum(l["zaehler"][k2] for l in laeufe)) for k2 in laeufe[0]["zaehler"]}
    return dict(L=L, laeufe=laeufe, bloecke=nb, zaehler_summe=ges,
                anteil_plus_auf_oben=ges["plus_auf_oben"] / ges["stichproben"],
                anteil_minus_auf_oben=ges["minus_auf_oben"] / ges["stichproben"],
                anteil_gleiche_art=ges["gleiche_art"] / ges["stichproben"],
                anteil_abgelehnt_orientierung=ges["abgelehnt_orientierung"] / (ges["angenommen"] + ges["abgelehnt_orientierung"] + ges["abgelehnt_vernichtung"]),
                bereich=[R1_EIS, R2], schalen_im_bereich=int(sel.sum()), ausgleich=fit, p_jackknife_sigma=sp_,
                C_jackknife_sigma=sC, ausgleich_gauss_referenz=fitG, cg_rest=cg_rest, haelften=haelften,
                nur_berichtet_bereich_ab_0_8=dict(bereich=[R1_EIS_ALT, R2], mc=fit_alt, gauss=fitG_alt),
                lauf_gegen_lauf=lauf_fits, tabelle=tab)


# ---------------- Teile 2 und 3: Stabnetze ----------------
def potenz(klassen, L, wert="max_t", rwert="r_max"):
    R2 = R2_STAB_FAKTOR * L
    pts = [(k[rwert], k[wert]) for k in klassen
           if R1_STAB <= 0.5 * (k["r_lo"] + k["r_hi"]) <= R2 and k[wert] > SCHWELLE]
    if len(pts) < MIN_KLASSEN:
        return dict(exponent=None, n=len(pts), grund="weniger als %d Klassen ueber der Schwelle" % MIN_KLASSEN)
    x = np.log([p[0] for p in pts]); y = np.log([p[1] for p in pts])
    A = np.column_stack([np.ones_like(x), x])
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    res = y - A @ c
    return dict(exponent=float(-c[1]), n=len(pts), streuung_log=float(np.sqrt(np.mean(res ** 2))),
                punkte=[[float(a), float(b)] for a, b in pts])


def stab_auswerten(netz, L):
    f = os.path.join(ordner, "stab_%s_L%d.json" % (netz, L))
    if not os.path.exists(f):
        return None
    d = json.load(open(f))
    erg = dict(netz=netz, L=L, gitter=d["gitter"], gleichgewicht_rest_max=d["gleichgewicht_rest_max"],
               lsqr_gegen_bloch_max=d["lsqr_gegen_bloch_max"], lsqr_istop=d["lsqr_istop"], lsqr_iter=d["lsqr_iter"],
               t_b0=d["t_b0"], t_b0_bloch=d["t_b0_bloch"], bloch_eigenspannungen=d["bloch_eigenspannungen"],
               linie_staebe=d["linie_staebe"], linie_t_min_max=d["linie_t_min_max"],
               abseits_linie_max_abs_t=d["abseits_linie_max_abs_t"], anteil_unter_schwelle=d["anteil_unter_schwelle"],
               anteil_unter_1e12=d["anteil_unter_1e12"], energie=d["energie"],
               bloch_max_null_sv=d["bloch_max_null_sv"], bloch_min_nicht_null_sv=d["bloch_min_nicht_null_sv"])
    erg["kugel_max"] = potenz(d["kugel"], L, "max_t", "r_max")
    erg["kugel_rms"] = potenz(d["kugel"], L, "rms_t", "r_mittel")
    erg["gruppen"] = {}
    for name, gr in d["gruppen"].items():
        erg["gruppen"][name] = dict(winkel_zu_stab_grad=gr["winkel_zu_stab_grad"], **potenz(gr["klassen"], L))
    # grobe Tabelle: Kugel-Maximum je Klasse bis L/2
    erg["kugel_tabelle"] = [[k["r_lo"], k["r_hi"], k["n"], k["max_t"], k["rms_t"]] for k in d["kugel"]
                            if k["r_hi"] <= L / 2 + 1e-9]
    return erg


def zaehl_auswerten():
    aus = {}
    for f in sorted(glob.glob(os.path.join(ordner, "zaehl_*.json"))):
        d = json.load(open(f))
        aus[os.path.basename(f)] = [dict(L=e["L"], methode=e["methode"], staebe=e["staebe"],
                                         freiheitsgrade=e["freiheitsgrade"], eigenspannungen=e["eigenspannungen"],
                                         nullmoden=e["nullmoden"], max_null_sv=e["max_null_sv"],
                                         min_nicht_null_sv=e["min_nicht_null_sv"], dauer_s=e["dauer_s"])
                                    for e in d["ergebnisse"]]
    return aus


t0 = time.time()
eis = {L: eis_auswerten(L) for L in (L_EIS, L_EIS_K)}
stab = {"%s_L%d" % (n, L): stab_auswerten(n, L) for n in ("pyro", "fcc") for L in (L_STAB, L_STAB_K)}
zaehl = zaehl_auswerten()

urteile = {}
# E0
e = eis.get(L_EIS)
if e is None:
    urteile["E0"] = dict(urteil="nicht auswertbar", grund="Lauf fehlt")
else:
    p, C = e["ausgleich"]["p"], e["ausgleich"]["C"]
    ok = (C > 0) and (E0_BEREICH[0] <= p <= E0_BEREICH[1])
    wort = "nicht auswertbar" if np.isnan(p) else ("eingetroffen" if ok else "nicht eingetroffen")
    urteile["E0"] = dict(urteil=wort, L=L_EIS, p=p, C=C,
                         p_sigma_jackknife=e["p_jackknife_sigma"], regel="C > 0 und p in [0,8; 1,2] bei L = %d" % L_EIS)
# E1
s = stab.get("fcc_L%d" % L_STAB)
if s is None or s["kugel_max"]["exponent"] is None:
    urteile["E1"] = dict(urteil="nicht auswertbar")
else:
    x = s["kugel_max"]["exponent"]
    urteile["E1"] = dict(urteil="eingetroffen" if E1_BEREICH[0] <= x <= E1_BEREICH[1] else "nicht eingetroffen",
                         L=L_STAB, exponent_kugel_max=x, regel="Kugel-Maximum, Exponent in [2,5; 3,5] bei L = %d" % L_STAB)
# E2
s = stab.get("pyro_L%d" % L_STAB)
if s is None:
    urteile["E2"] = dict(urteil="nicht auswertbar")
else:
    ex = {n: g["exponent"] for n, g in s["gruppen"].items() if g["exponent"] is not None}
    if not ex:
        urteile["E2"] = dict(urteil="nicht eingetroffen", grund="in keiner Richtung ausreichend Klassen ueber der Schwelle",
                             L=L_STAB)
    else:
        mn = min(ex, key=ex.get)
        urteile["E2"] = dict(urteil="eingetroffen" if ex[mn] <= E2_GRENZE else "nicht eingetroffen", L=L_STAB,
                             kleinster_exponent=ex[mn], richtung=mn, alle=ex,
                             regel="kleinster Kegel-Exponent (Maximum je Klasse) <= 1,5 bei L = %d" % L_STAB)
# E3
dichte = None
for k, v in zaehl.items():
    if k.startswith("zaehl_pyro_dicht"):
        dichte = {e2["L"]: e2["eigenspannungen"] for e2 in v}
if dichte is None or not all(L in dichte for L in L_ZAEHL):
    urteile["E3"] = dict(urteil="nicht auswertbar")
else:
    folge = [dichte[L] for L in L_ZAEHL]
    ok = all(folge[i] < folge[i + 1] for i in range(len(folge) - 1))
    urteile["E3"] = dict(urteil="eingetroffen" if ok else "nicht eingetroffen", L=L_ZAEHL, eigenspannungen=folge,
                         regel="Zahl der Eigenspannungen (dicht, Staebe - Rang) streng steigend ueber L = %s" % L_ZAEHL)

aus = dict(karte="EIS-1", urteile=urteile, spin_eis={str(k): v for k, v in eis.items()}, stabnetze=stab,
           eigenspannungen=zaehl, regeln=dict(R1_EIS=R1_EIS, R1_EIS_ALT_nur_berichtet=R1_EIS_ALT,
                                              R2_EIS_FAKTOR=R2_EIS_FAKTOR, E0=E0_BEREICH, R1_STAB=R1_STAB,
                                              R2_STAB_FAKTOR=R2_STAB_FAKTOR, SCHWELLE=SCHWELLE, MIN_KLASSEN=MIN_KLASSEN,
                                              E1=E1_BEREICH, E2=E2_GRENZE),
           skript_sha256=hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
           dauer_s=time.time() - t0, ende_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
json.dump(aus, open(ausgabe, "w"), indent=1)
print(json.dumps(urteile, indent=1))

# kleine Bilder (nur Darstellung)
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(9, 3.6))
    for L, e in eis.items():
        if e is None:
            continue
        rr = np.array([t["r"] for t in e["tabelle"]]); FF = np.array([t["F"] for t in e["tabelle"]])
        ss = np.array([t["sF"] for t in e["tabelle"]]); FG = np.array([t["FG"] for t in e["tabelle"]])
        m = rr <= L / 2
        ax[0].errorbar(rr[m], FF[m] - e["ausgleich"]["a"], ss[m], fmt=".", ms=3, label="L=%d MC" % L)
        ax[0].plot(rr[m], FG[m] - e["ausgleich_gauss_referenz"]["a"], "x", ms=3, label="L=%d Gauss-Ref." % L)
    ax[0].set_xlabel("r (Zellkanten)"); ax[0].set_ylabel("F(r) - a  (T)"); ax[0].legend(fontsize=7)
    ax[0].set_title("Spin-Eis: Defektpaar", fontsize=9)
    for key, s in stab.items():
        if s is None:
            continue
        tb = np.array(s["kugel_tabelle"])
        if len(tb):
            ax[1].loglog(0.5 * (tb[:, 0] + tb[:, 1]), np.maximum(tb[:, 3], 1e-16), ".-", ms=3, label=key)
    ax[1].set_xlabel("r (Zellkanten)"); ax[1].set_ylabel("max |t| je Klasse"); ax[1].legend(fontsize=7)
    ax[1].set_title("Stabnetze: Fehlpass delta = 1", fontsize=9)
    fig.tight_layout(); fig.savefig(ausgabe.replace(".json", ".png"), dpi=90)
except Exception as ex:
    print("Bild nicht erstellt:", ex)
