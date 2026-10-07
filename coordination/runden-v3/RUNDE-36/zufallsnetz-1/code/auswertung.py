# ZUFALLSNETZ-1 (Runde 36): mechanische Auswertung nach PLAN.md (eingefroren). Nur ueber kleintest.sh auf der .69.
# Aufruf: auswertung.py <laufordner> <auswertung.json>
import sys, os, json, hashlib, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.optimize import minimize
import zufallsnetz as zn
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

NS = (4000, 16000, 64000)
N_GROSS = 64000        # Z1, Z3: fest N = 64000 (Ersatzgroesse waere "nicht auswertbar")
TEST = False
SAATEN = (1, 2)
FEDERN = ("k1", "kl")
Z0_FCC = 1e-6
Z0_GRAD = (15.4, 15.6)
Z0_CAUCHY = 0.01
Z1_SCHWELLE = 0.03
Z2_P = (0.35, 0.65)
Z3_BEREICH = (1.75, 2.2)
Z4_BEREICH = (0.5, 0.9)
SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
FARBE = {"k1": "#2a78d6", "kl": "#eb6834", "s3": "#1baf7a"}


def sph(x):
    th, ph = x
    return np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])


def zu_sph(d):
    return [float(np.arccos(np.clip(d[2], -1, 1))), float(np.arctan2(d[1], d[0]))]


def nm_extrem(f, starts):
    """Minimum von f auf der Kugel per Nelder-Mead aus mehreren Starts (Konvergenzprobe wie NETZ-C-1)."""
    best = None
    for d in starts:
        r = minimize(lambda x: f(sph(x)), zu_sph(d), method="Nelder-Mead",
                     options=dict(xatol=1e-8, fatol=1e-14, maxiter=800))
        if best is None or r.fun < best:
            best = float(r.fun)
    return best


def kennzahlen(Cv, rho, verfeinern=True):
    dirs = zn.richtungen(zn.NFIB)
    c, w = zn.christoffel(Cv, rho, dirs)
    stabil = bool(np.all(w > 0))
    c = np.maximum(c, 1e-300)
    S = [float(c[:, b].max() / c[:, b].min() - 1) for b in range(3)]
    Dv = c[:, 1] / c[:, 0] - 1
    fib = c[3:]
    cl = float(fib[:, 2].mean()); cq = float(fib[:, :2].mean())
    lam, mu, K = zn.iso(Cv)
    out = dict(stabil_alle_richtungen=stabil,
               schwankung_ast=S, schwankung_quer=max(S[0], S[1]), doppelbrechung_max=float(Dv.max()),
               doppelbrechung_mittel=float(Dv[3:].mean()),
               c_min=[float(c[:, b].min()) for b in range(3)], c_max=[float(c[:, b].max()) for b in range(3)],
               c_mittel_fib=[float(fib[:, b].mean()) for b in range(3)],
               rms_rel_fib=[float(fib[:, b].std() / fib[:, b].mean()) for b in range(3)],
               cl_durch_cq=cl / cq, lam=lam, mu=mu, K=K, cl_durch_cq_iso=float(np.sqrt((lam + 2 * mu) / mu)),
               c_l_iso=float(np.sqrt((lam + 2 * mu) / rho)), c_q_iso=float(np.sqrt(mu / rho)))
    # dichte Richtungsprobe
    cd, _ = zn.christoffel(Cv, rho, zn.fibonacci(20000))
    out["dicht20000"] = dict(schwankung_ast=[float(cd[:, b].max() / cd[:, b].min() - 1) for b in range(3)],
                             doppelbrechung_max=float((cd[:, 1] / cd[:, 0] - 1).max()))
    if verfeinern:
        C4 = zn.tensor4(Cv)

        def ast(d, b):
            d = d / np.linalg.norm(d)
            G = np.einsum("ijkl,j,l->ik", C4, d, d)
            return float(np.sqrt(np.linalg.eigvalsh(G)[b] / rho))

        def dbr(d):
            d = d / np.linalg.norm(d)
            G = np.einsum("ijkl,j,l->ik", C4, d, d)
            ww = np.linalg.eigvalsh(G)
            return float(np.sqrt(ww[1] / ww[0]) - 1)
        ver = []
        for b in range(3):
            mn = nm_extrem(lambda d: ast(d, b), dirs[np.argsort(c[:, b])[:3]])
            mx = -nm_extrem(lambda d: -ast(d, b), dirs[np.argsort(-c[:, b])[:3]])
            ver.append(float(mx / mn - 1))
        dmax = -nm_extrem(lambda d: -dbr(d), dirs[np.argsort(-Dv)[:3]])
        out["verfeinert"] = dict(schwankung_ast=ver, schwankung_quer=max(ver[0], ver[1]), doppelbrechung_max=float(dmax))
    return out


def cauchy(Cv):
    lam, mu, K = zn.iso(Cv)
    C = np.asarray(Cv)
    paare = [(0, 1, 5, 5), (0, 2, 4, 4), (1, 2, 3, 3), (0, 3, 4, 5), (1, 4, 3, 5), (2, 5, 3, 4)]
    pmax = max(abs(C[a, b] - C[c, d]) for a, b, c, d in paare) / np.abs(C).max()
    # nicht gepaarte Vergleiche "C12-Typ" (C12, C13, C23) gegen "C44-Typ" (C44, C55, C66): enthalten die Restanisotropie
    ungepaart = [(0, 1, 3, 3), (0, 1, 4, 4), (0, 2, 3, 3), (0, 2, 5, 5), (1, 2, 4, 4), (1, 2, 5, 5)]
    umax = max(abs(C[a, b] / C[c, d] - 1) for a, b, c, d in ungepaart)
    return dict(lam_durch_mu_minus_1=float(lam / mu - 1),
                komponenten_C1122_durch_C2323_minus_1=float(C[0, 1] / C[3, 3] - 1),
                komponenten_ungepaart_max_rel=float(umax),
                paar_cauchy_max_rel=float(pmax))


def laden(ordner, name):
    p = os.path.join(ordner, name)
    if not os.path.exists(p):
        return None
    return json.load(open(p))


def fit_p(Nv, Sv):
    x = np.log(np.asarray(Nv, float)); y = np.log(np.asarray(Sv, float))
    A = np.vstack([np.ones_like(x), x]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    res = y - A @ coef
    return float(-coef[1]), float(coef[0]), [float(r) for r in res]


def main():
    global NS, N_GROSS, TEST
    ordner, aus = sys.argv[1], sys.argv[2]
    if len(sys.argv) > 3:          # nur Rauchtest des Auswertecodes mit kleinen Netzen, nie fuer Urteile
        NS = tuple(int(x) for x in sys.argv[3].split(",")); N_GROSS = NS[-1]; TEST = True
    t0 = time.time()
    netze = {}
    shas = set()
    for N in NS:
        for s in SAATEN:
            for f in FEDERN:
                r = laden(ordner, "netz_N%d_s%d_%s.json" % (N, s, f))
                if r is None or "C" not in r:
                    continue
                shas.add(r["skript_sha256"])
                rho = r["rho"]
                e = dict(N=N, saat=s, feder=f, rho=rho, delaunay=r["delaunay"], cg=r["elast_diag"]["cg"],
                         asym_C_alt=r["elast_diag"]["asym_C_alt"], diff_C_C_alt=r["elast_diag"]["diff_C_C_alt"],
                         stabil=r["elast_diag"]["stabil"], stabil_affin=r["elast_diag"]["stabil_affin"],
                         eig_C=r["eig_C"], dauer_s=r["dauer_s"], maxrss_mb=r["maxrss_mb"])
                e["relaxiert"] = kennzahlen(r["C"], rho)
                e["affin"] = kennzahlen(r["C_aff"], rho, verfeinern=False)
                e["cauchy_affin"] = cauchy(r["C_aff"])
                e["G_durch_G_affin"] = e["relaxiert"]["mu"] / e["affin"]["mu"]
                e["K_durch_K_affin"] = e["relaxiert"]["K"] / e["affin"]["K"]
                e["C"] = r["C"]; e["C_aff"] = r["C_aff"]
                netze["N%d_s%d_%s" % (N, s, f)] = e
                print("netz", N, s, f, "S_quer %.4g D %.4g cl/cq %.4f G/Gaff %.4f" % (
                    e["relaxiert"]["schwankung_quer"], e["relaxiert"]["doppelbrechung_max"],
                    e["relaxiert"]["cl_durch_cq"], e["G_durch_G_affin"]), flush=True)
    fcc = laden(ordner, "fcc.json")
    kon = laden(ordner, "kontrolle_N%d_s1_k1.json" % NS[0])
    urteile = {}
    # ---------------- Z0
    w0 = {}; ok0 = True; verm0 = []
    if fcc is None:
        urteile["Z0"] = dict(urteil="nicht auswertbar", vermerk="fcc-Gegenprobe fehlt", werte={}); ok0 = None
    else:
        w0["fcc_max_rel_abw_netz_c_1"] = fcc["max_rel_abw_netz_c_1"]
        w0["fcc_max_rel_abw_geschlossen"] = fcc["max_rel_abw_geschlossen"]
        ok0 = fcc["max_rel_abw_netz_c_1"] <= Z0_FCC
        grade = {}; cau = {}
        for N in NS:
            for s in SAATEN:
                e = netze.get("N%d_s%d_k1" % (N, s))
                if e is None:
                    verm0.append("Netz N=%d Saat %d fehlt" % (N, s)); continue
                g = e["delaunay"]["mittlerer_grad"]; grade["N%d_s%d" % (N, s)] = g
                ok0 = ok0 and (Z0_GRAD[0] <= g <= Z0_GRAD[1])
                e2 = netze.get("N%d_s%d_kl" % (N, s))
                if e2 is not None and e2["delaunay"]["kanten_sha256"] != e["delaunay"]["kanten_sha256"]:
                    verm0.append("k1/kl-Netz verschieden bei N=%d Saat %d" % (N, s)); ok0 = False
        for kname, e in netze.items():
            v = e["cauchy_affin"]["lam_durch_mu_minus_1"]; cau[kname] = v
            ok0 = ok0 and abs(v) <= Z0_CAUCHY
        w0["mittlerer_grad"] = grade; w0["cauchy_affin_lam_durch_mu_minus_1"] = cau
        w0["info_cauchy_affin_komponenten_C1122_durch_C2323_minus_1"] = {k: e["cauchy_affin"]["komponenten_C1122_durch_C2323_minus_1"] for k, e in netze.items()}
        w0["info_cauchy_affin_ungepaart_max_rel"] = {k: e["cauchy_affin"]["komponenten_ungepaart_max_rel"] for k, e in netze.items()}
        w0["info_stabil_alle"] = all(e["stabil"] and e["relaxiert"]["stabil_alle_richtungen"] for e in netze.values())
        urteile["Z0"] = dict(urteil="eingetroffen" if ok0 else "nicht eingetroffen", werte=w0)
        if verm0:
            urteile["Z0"]["vermerk"] = "; ".join(verm0)
    # ---------------- Z1
    e1 = [netze.get("N%d_s%d_k1" % (N_GROSS, s)) for s in SAATEN]
    if any(e is None for e in e1):
        urteile["Z1"] = dict(urteil="nicht auswertbar", vermerk="N = %d nicht fuer beide Saaten gerechnet" % N_GROSS, werte={})
    else:
        w1 = {"saat%d" % s: dict(schwankung_quer=e["relaxiert"]["schwankung_quer"], schwankung_ast=e["relaxiert"]["schwankung_ast"],
                                  doppelbrechung_max=e["relaxiert"]["doppelbrechung_max"])
              for s, e in zip(SAATEN, e1)}
        ok1 = all(e["relaxiert"]["schwankung_quer"] < Z1_SCHWELLE and e["relaxiert"]["doppelbrechung_max"] < Z1_SCHWELLE for e in e1)
        urteile["Z1"] = dict(urteil="eingetroffen" if ok1 else "nicht eingetroffen", werte=w1)
    # ---------------- Z2
    Ns = []; Sm = []; ok2 = True
    for N in NS:
        v = [netze.get("N%d_s%d_k1" % (N, s)) for s in SAATEN]
        if any(e is None for e in v):
            ok2 = False; continue
        Ns.append(N); Sm.append(float(np.mean([e["relaxiert"]["schwankung_quer"] for e in v])))
    if len(Ns) < 3:
        urteile["Z2"] = dict(urteil="nicht auswertbar", vermerk="nicht alle drei Groessen mit beiden Saaten", werte=dict(N=Ns, S_mittel=Sm))
    else:
        p, a, resid = fit_p(Ns, Sm)
        urteile["Z2"] = dict(urteil="eingetroffen" if Z2_P[0] <= p <= Z2_P[1] else "nicht eingetroffen",
                             werte=dict(N=Ns, schwankung_quer_mittel=Sm, p=p, achsenabschnitt=a, residuen_ln=resid))
    # ---------------- Z3
    if any(e is None for e in e1):
        urteile["Z3"] = dict(urteil="nicht auswertbar", vermerk="N = %d nicht fuer beide Saaten gerechnet" % N_GROSS, werte={})
    else:
        w3 = {"saat%d" % s: dict(cl_durch_cq=e["relaxiert"]["cl_durch_cq"], cl_durch_cq_iso=e["relaxiert"]["cl_durch_cq_iso"])
              for s, e in zip(SAATEN, e1)}
        ok3 = all(Z3_BEREICH[0] <= e["relaxiert"]["cl_durch_cq"] <= Z3_BEREICH[1] for e in e1)
        urteile["Z3"] = dict(urteil="eingetroffen" if ok3 else "nicht eingetroffen", werte=w3)
    # ---------------- Z4
    w4 = {}; ok4 = True; fehlt4 = []
    for N in NS:
        for s in SAATEN:
            e = netze.get("N%d_s%d_k1" % (N, s))
            if e is None:
                fehlt4.append("N%d_s%d" % (N, s)); continue
            w4["N%d_s%d" % (N, s)] = e["G_durch_G_affin"]
            ok4 = ok4 and (Z4_BEREICH[0] <= e["G_durch_G_affin"] <= Z4_BEREICH[1])
    if not w4:
        urteile["Z4"] = dict(urteil="nicht auswertbar", vermerk="keine Netze", werte={})
    else:
        urteile["Z4"] = dict(urteil="eingetroffen" if ok4 else "nicht eingetroffen", werte=w4)
        if fehlt4:
            urteile["Z4"]["vermerk"] = "fehlend: " + ", ".join(fehlt4)
    # ---------------- Zusatz (keine Urteile): Variante kl, Fits je Saat und je Groesse
    zusatz = {}
    for f in FEDERN:
        for groesse in ("schwankung_quer", "doppelbrechung_max"):
            for s in list(SAATEN) + ["mittel"]:
                xs = []; ys = []
                for N in NS:
                    if s == "mittel":
                        v = [netze.get("N%d_s%d_%s" % (N, ss, f)) for ss in SAATEN]
                        if any(e is None for e in v):
                            continue
                        xs.append(N); ys.append(float(np.mean([e["relaxiert"][groesse] for e in v])))
                    else:
                        e = netze.get("N%d_s%d_%s" % (N, s, f))
                        if e is None:
                            continue
                        xs.append(N); ys.append(e["relaxiert"][groesse])
                if len(xs) >= 2:
                    zusatz["p_%s_%s_saat%s" % (groesse, f, s)] = fit_p(xs, ys)[0]
        for b in range(3):
            xs = []; ys = []
            for N in NS:
                v = [netze.get("N%d_s%d_%s" % (N, ss, f)) for ss in SAATEN]
                if any(e is None for e in v):
                    continue
                xs.append(N); ys.append(float(np.mean([e["relaxiert"]["schwankung_ast"][b] for e in v])))
            if len(xs) >= 2:
                zusatz["p_ast%d_%s_mittel" % (b + 1, f)] = fit_p(xs, ys)[0]
    kontrollen = dict(fcc=fcc, kontrolle=kon)
    erg = dict(karte="ZUFALLSNETZ-1", runde=36, test_modus_kleine_netze=TEST, NS=list(NS), N_gross=N_GROSS,
               auswertung_sha256=SKRIPT_SHA, zufallsnetz_sha256_in_laeufen=sorted(shas),
               zufallsnetz_sha256_jetzt=zn.SKRIPT_SHA, urteile=urteile, zusatz=zusatz, netze=netze, kontrollen=kontrollen,
               ende_utc=zn.jetzt(), dauer_s=time.time() - t0)
    json.dump(erg, open(aus, "w"), indent=1)
    print(json.dumps({k: v["urteil"] for k, v in urteile.items()}), flush=True)
    bilder(ordner, netze, fcc)


def bilder(ordner, netze, fcc):
    plt.rcParams.update({"font.size": 9, "axes.edgecolor": "#888888", "axes.labelcolor": "#222222",
                         "xtick.color": "#444444", "ytick.color": "#444444"})
    # 1) Geschwindigkeitsflaechen als Karten: relative Abweichung vom Richtungsmittel
    zeilen = [k for k in ("N%d_s1_k1" % NS[0], "N%d_s1_k1" % N_GROSS) if k in netze]
    if zeilen:
        th = np.linspace(0.5, 179.5, 180) * np.pi / 180; ph = np.linspace(-179.5, 179.5, 360) * np.pi / 180
        TH, PH = np.meshgrid(th, ph, indexing="ij")
        dirs = np.stack([np.sin(TH) * np.cos(PH), np.sin(TH) * np.sin(PH), np.cos(TH)], -1).reshape(-1, 3)
        karten = {}
        for z in zeilen:
            e = netze[z]
            c, _ = zn.christoffel(e["C"], e["rho"], dirs)
            c = c.reshape(len(th), len(ph), 3)
            karten[z] = [100 * (c[..., b] / e["relaxiert"]["c_mittel_fib"][b] - 1) for b in range(3)] + [100 * (c[..., 1] / c[..., 0] - 1)]
        titel = ["langsame Querwelle c1", "schnelle Querwelle c2", "Laengswelle c3", "Doppelbrechung c2/c1 - 1"]
        fig, ax = plt.subplots(len(zeilen), 4, figsize=(16, 3.3 * len(zeilen) + 0.6), squeeze=False)
        for j in range(4):
            vm = max(np.abs(karten[z][j]).max() for z in zeilen)
            for i, z in enumerate(zeilen):
                if j < 3:
                    im = ax[i, j].imshow(karten[z][j], extent=[-180, 180, 180, 0], cmap="RdBu_r", vmin=-vm, vmax=vm, aspect="auto")
                else:
                    im = ax[i, j].imshow(karten[z][j], extent=[-180, 180, 180, 0], cmap="Blues", vmin=0, vmax=vm, aspect="auto")
                ax[i, j].set_title("%s, N = %s, Saat 1, k = 1" % (titel[j], z.split("_")[0][1:]), fontsize=8)
                ax[i, j].set_xlabel("Azimut phi [Grad]"); ax[i, j].set_ylabel("Polwinkel theta [Grad]")
                cb = fig.colorbar(im, ax=ax[i, j]); cb.set_label("Abweichung vom Richtungsmittel [%]" if j < 3 else "[%]")
        fig.suptitle("ZUFALLSNETZ-1: Geschwindigkeitsflaechen (Christoffel aus dem relaxierten Tensor), gleiche Farbskala je Spalte")
        fig.tight_layout()
        fig.savefig(os.path.join(ordner, "geschwindigkeitsflaechen.png"), dpi=120)
        plt.close(fig)
    # 2) Schwankung gegen N
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.4))
    groessen = [("schwankung_quer", "Richtungsschwankung Querwelle max(S1, S2)"), ("doppelbrechung_max", "groesste Doppelbrechung"),
                ("schwankung_l", "Richtungsschwankung Laengswelle S3")]
    for j, (g, tt) in enumerate(groessen):
        for f in FEDERN:
            xs = []; ms = []
            for N in NS:
                v = []
                for s in SAATEN:
                    e = netze.get("N%d_s%d_%s" % (N, s, f))
                    if e is None:
                        continue
                    val = e["relaxiert"]["schwankung_ast"][2] if g == "schwankung_l" else e["relaxiert"][g]
                    v.append(val)
                    ax[j].plot(N, 100 * val, "o", ms=4, mfc="none", color=FARBE[f], alpha=0.8)
                if len(v) == len(SAATEN):
                    xs.append(N); ms.append(np.mean(v))
            if len(xs) >= 2:
                p, a, _ = fit_p(xs, ms)
                xx = np.array([0.75 * NS[0], 1.4 * NS[-1]])
                ax[j].plot(xs, 100 * np.array(ms), "s", ms=8, color=FARBE[f], label="k = %s: Saatmittel, p = %.2f" % ("1" if f == "k1" else "1/l", p))
                ax[j].plot(xx, 100 * np.exp(a) * xx ** (-p), "-", lw=2, color=FARBE[f])
                if f == "k1":
                    ax[j].plot(xx, 100 * ms[0] * (xx / xs[0]) ** (-0.5), ":", lw=1.5, color="#666666", label="Steigung -1/2 (Bezug)")
        if j == 0:
            ax[j].axhline(100 * Z1_SCHWELLE, color="#999999", lw=1, ls="--", label="Z1-Schwelle 3 %")
        if j == 1:
            ax[j].axhline(100 * Z1_SCHWELLE, color="#999999", lw=1, ls="--", label="Z1-Schwelle 3 %")
        ax[j].set_xscale("log"); ax[j].set_yscale("log")
        ax[j].set_xlabel("Punktzahl N"); ax[j].set_ylabel("%s [%%]" % tt)
        ax[j].set_title(tt + " (offene Kreise: Einzelsaaten)", fontsize=8)
        ax[j].grid(True, which="both", color="#e5e5e5", lw=0.6)
        ax[j].legend(fontsize=7, frameon=False)
    fig.suptitle("ZUFALLSNETZ-1: Restanisotropie gegen Netzgroesse (403 Richtungen)")
    fig.tight_layout()
    fig.savefig(os.path.join(ordner, "schwankung_gegen_n.png"), dpi=120)
    plt.close(fig)
    # 3) Schnitt in der xy-Ebene: fcc-Z gegen Zufallsnetz N = 64000 (je auf das Mittel der Querwellen normiert)
    if fcc is not None and ("N%d_s1_k1" % N_GROSS) in netze:
        phi = np.linspace(0, 2 * np.pi, 721)
        dd = np.stack([np.cos(phi), np.sin(phi), np.zeros_like(phi)], 1)
        fig, ax = plt.subplots(1, 2, figsize=(11, 5.2), subplot_kw=dict(projection="polar"))
        for i, (tt, Cv, rho) in enumerate([("fcc, nur Zentralfedern (NETZ-C-1)", fcc["C"], fcc["rho"]),
                                          ("Delaunay-Zufallsnetz N = %d, Saat 1, k = 1" % N_GROSS, netze["N%d_s1_k1" % N_GROSS]["C"], netze["N%d_s1_k1" % N_GROSS]["rho"])]):
            c, _ = zn.christoffel(Cv, rho, dd)
            cq = zn.christoffel(Cv, rho, zn.fibonacci(4000))[0][:, :2].mean()
            for b, (lab, col) in enumerate([("c1 (langsame Querwelle)", "#2a78d6"), ("c2 (schnelle Querwelle)", "#eb6834"), ("c3 (Laengswelle)", "#1baf7a")]):
                ax[i].plot(phi, c[:, b] / cq, lw=2, color=col, label=lab)
            ax[i].set_title(tt + "\nGeschwindigkeit in der xy-Ebene / mittlere Querwelle", fontsize=9)
            ax[i].set_rlim(0, 2.2)
        ax[1].legend(loc="lower left", bbox_to_anchor=(0.75, -0.05), fontsize=8, frameon=False)
        fig.tight_layout()
        fig.savefig(os.path.join(ordner, "schnitt_xy_fcc_gegen_zufall.png"), dpi=120)
        plt.close(fig)


if __name__ == "__main__":
    main()
