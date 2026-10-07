"""KAUSAL-SWERVE-1: Auswertung nach PLAN.md (Abschnitte 4 bis 6). Aufruf: auswertung.py <laufordner> <ausgabeordner>

Liest laeufer-N<N>-b<block>.npz/.json, links-N<N>-s<saat>.json und bulk-s<saat>.npz/.json und schreibt
auswertung.json sowie die Bilder drift_n.png, var_n.png, cosh_n.png und kontrollen.png.
"""
import glob
import hashlib
import json
import os
import sys
import time

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
N_HAUPT = 64000
N_NEBEN = 16000
ETA0S = (-1.0, 0.0, 1.0)
NMAX = 100
N_KS1 = 50
N_FIT = (5, 50)
N_KS3 = (5, 50)
MIN_AKTIV = 100
KS0_TOL = 0.15
KS2_R2 = 0.98
KS2_VERH = 1.15
SIGMA2_BULK = 0.25          # Schreibtisch [M], PLAN Abschnitt 3
PHI_BULK = 4.0 * (1.0 / 1.5 ** 2 - 1.0 / 2.5 ** 2)   # E[cosh d eta] = 1,1378 [M]
FARBEN = {-1.0: "#2a78d6", 0.0: "#eb6834", 1.0: "#1baf7a"}
TINTE, TINTE2, FLAECHE = "#0b0b0b", "#52514e", "#fcfcfb"
KANTEN = np.arange(-4.0, 4.0 + 1e-9, 0.5)


def lade_laeufer(ordner, N):
    dateien = sorted(glob.glob(os.path.join(ordner, "laeufer-N%d-b*.npz" % N)))
    if not dateien:
        return None
    teile = {k: [] for k in ("eta0", "eta", "bulk", "tau", "uu", "vv", "nl_alle", "nl_zul", "schritte", "grund",
                             "block")}
    koepfe = []
    for pfad in dateien:
        kopf = json.load(open(pfad[:-4] + ".json"))
        koepfe.append(kopf)
        z = np.load(pfad)
        ok = z["fertig"]
        for k in teile:
            if k == "block":
                teile[k].append(np.full(int(ok.sum()), kopf["block"]))
            else:
                teile[k].append(z[k][ok])
    d = {k: np.concatenate(v) for k, v in teile.items()}
    d["koepfe"] = koepfe
    return d


def erster_nicht_bulk(bulk):
    """T = erster Schritt k >= 1, der nicht bulk-exakt ist (oder fehlt); NMAX + 1, wenn alle 100 bulk-exakt."""
    nb = bulk[:, 1:] != 1
    return np.where(nb.any(axis=1), nb.argmax(axis=1) + 1, NMAX + 1)


def populationen(d):
    M = d["eta"].shape[0]
    T = erster_nicht_bulk(d["bulk"])
    n = np.arange(NMAX + 1)[None, :]
    haupt = n < T[:, None]
    naiv = n <= d["schritte"][:, None]
    idx = np.minimum(n, (T - 1)[:, None])
    eingefroren = np.take_along_axis(d["eta"], idx, axis=1)
    return T, haupt, naiv, eingefroren, np.ones((M, NMAX + 1), dtype=bool)


def reihe(eta, eta0, aktiv):
    dd = eta - eta0[:, None]
    zeilen = []
    for n in range(NMAX + 1):
        a = aktiv[:, n] & np.isfinite(eta[:, n])
        k = int(a.sum())
        if k < 2:
            zeilen.append({"n": n, "anzahl": k})
            continue
        x = dd[a, n]
        c = np.cosh(eta[a, n])
        zeilen.append({"n": n, "anzahl": k, "mittel": float(x.mean()), "se": float(x.std(ddof=1) / np.sqrt(k)),
                       "var": float(x.var(ddof=1)), "cosh": float(c.mean()),
                       "cosh_se": float(c.std(ddof=1) / np.sqrt(k)), "cosh_median": float(np.median(c))})
    return zeilen


def reihen_je_eta0(eta, eta0, aktiv):
    return {e0: reihe(eta[eta0 == e0], eta0[eta0 == e0], aktiv[eta0 == e0]) for e0 in ETA0S}


def urteil_ks1(r):
    werte, ok, auswertbar = {}, True, True
    for e0 in ETA0S:
        z = r[e0][N_KS1]
        werte[str(e0)] = {k: z.get(k) for k in ("anzahl", "mittel", "se")}
        if z["anzahl"] < MIN_AKTIV:
            auswertbar = False
            continue
        werte[str(e0)]["abweichung_in_se"] = z["mittel"] / z["se"]
        if abs(z["mittel"]) > 3.0 * z["se"]:
            ok = False
    if not auswertbar:
        return "nicht auswertbar", werte
    return ("eingetroffen" if ok else "nicht eingetroffen"), werte


def urteil_ks2(r):
    werte, auswertbar, steigungen, r2s = {}, True, [], []
    for e0 in ETA0S:
        if r[e0][N_FIT[1]]["anzahl"] < MIN_AKTIV:
            auswertbar = False
            werte[str(e0)] = {"anzahl_bei_50": r[e0][N_FIT[1]]["anzahl"]}
            continue
        n = np.arange(N_FIT[0], N_FIT[1] + 1, dtype=float)
        y = np.array([r[e0][int(k)]["var"] for k in n])
        b, a = np.polyfit(n, y, 1)
        rest = y - (a + b * n)
        r2 = 1.0 - float((rest ** 2).sum() / ((y - y.mean()) ** 2).sum())
        steigungen.append(float(b))
        r2s.append(r2)
        werte[str(e0)] = {"steigung_sigma2": float(b), "achsenabschnitt": float(a), "R2": r2,
                          "anzahl_bei_50": r[e0][N_FIT[1]]["anzahl"], "var_bei_5": float(y[0]),
                          "var_bei_50": float(y[-1])}
    if not auswertbar:
        return "nicht auswertbar", werte
    verh = max(steigungen) / min(steigungen) if min(steigungen) > 0 else float("inf")
    werte["max_durch_min_steigung"] = verh
    ok = all(x > KS2_R2 for x in r2s) and min(steigungen) > 0 and verh <= KS2_VERH
    return ("eingetroffen" if ok else "nicht eingetroffen"), werte


def urteil_ks3(r):
    z5, z50 = r[0.0][N_KS3[0]], r[0.0][N_KS3[1]]
    werte = {"anzahl_bei_5": z5["anzahl"], "anzahl_bei_50": z50["anzahl"]}
    if z5["anzahl"] < MIN_AKTIV or z50["anzahl"] < MIN_AKTIV:
        return "nicht auswertbar", werte
    diff = z50["cosh"] - z5["cosh"]
    se = float(np.hypot(z50["cosh_se"], z5["cosh_se"]))
    werte.update({"cosh_bei_5": z5["cosh"], "se_5": z5["cosh_se"], "cosh_bei_50": z50["cosh"],
                  "se_50": z50["cosh_se"], "differenz": diff, "se_differenz": se, "differenz_in_se": diff / se,
                  "median_bei_5": z5["cosh_median"], "median_bei_50": z50["cosh_median"]})
    return ("eingetroffen" if diff > 3.0 * se else "nicht eingetroffen"), werte


def alle_urteile(r):
    return {"KS1": urteil_ks1(r), "KS2": urteil_ks2(r), "KS3": urteil_ks3(r)}


def ks1_block_se(d, aktiv):
    werte = {}
    for e0 in ETA0S:
        m = d["eta0"] == e0
        mittel = []
        for b in sorted(set(d["block"][m].tolist())):
            s = m & (d["block"] == b) & aktiv[:, N_KS1]
            if s.sum() >= 2:
                mittel.append(float((d["eta"][s, N_KS1] - e0).mean()))
        if len(mittel) >= 2:
            se = float(np.std(mittel, ddof=1) / np.sqrt(len(mittel)))
            werte[str(e0)] = {"blockmittel": mittel, "mittel_der_bloecke": float(np.mean(mittel)), "se_bloecke": se,
                              "abweichung_in_se": float(np.mean(mittel) / se) if se > 0 else None}
    return werte


def schritte_tabelle(eta_vor, deta):
    zeilen = []
    for lo, hi in zip(KANTEN[:-1], KANTEN[1:]):
        s = (eta_vor >= lo) & (eta_vor < hi)
        k = int(s.sum())
        z = {"eta_von": float(lo), "eta_bis": float(hi), "anzahl": k}
        if k >= 2:
            z.update({"mittel": float(deta[s].mean()), "se": float(deta[s].std(ddof=1) / np.sqrt(k)),
                      "quadrat_mittel": float((deta[s] ** 2).mean())})
        zeilen.append(z)
    aus = {"anzahl_gesamt": int(eta_vor.size), "ausserhalb_kanten": int(((eta_vor < KANTEN[0]) |
                                                                         (eta_vor >= KANTEN[-1])).sum()),
           "klassen": zeilen}
    if eta_vor.size >= 3:
        X = np.vstack((np.ones_like(eta_vor), eta_vor)).T
        koef, *_ = np.linalg.lstsq(X, deta, rcond=None)
        rest = deta - X @ koef
        s2 = float((rest ** 2).sum() / (eta_vor.size - 2))
        kov = s2 * np.linalg.inv(X.T @ X)
        aus.update({"steigung_beta": float(koef[1]), "steigung_se": float(np.sqrt(kov[1, 1])),
                    "achse_alpha": float(koef[0]), "achse_se": float(np.sqrt(kov[0, 0])),
                    "deta_mittel": float(deta.mean()), "deta_se": float(deta.std(ddof=1) / np.sqrt(deta.size)),
                    "deta_quadrat_mittel": float((deta ** 2).mean())})
    return aus


def schritte(d, T):
    """Bulk-exakte Schritte vor dem Ende (Hauptregel) und Schritte ab dem ersten nicht bulk-exakten (Fortsetzung)."""
    eta = d["eta"]
    M = eta.shape[0]
    k = np.arange(1, NMAX + 1)[None, :]
    ausgefuehrt = d["bulk"][:, 1:] >= 0
    innen = ausgefuehrt & (k < T[:, None])
    rand = ausgefuehrt & (k >= T[:, None])
    vor = eta[:, :-1]
    deta = eta[:, 1:] - eta[:, :-1]
    e0 = np.repeat(d["eta0"][:, None], NMAX, axis=1)
    _ = M
    return {"innen": (vor[innen], deta[innen], e0[innen], d["tau"][:, 1:][innen]),
            "rand": (vor[rand], deta[rand], e0[rand], d["tau"][:, 1:][rand])}


def beschreibung(d, N, T, r_haupt):
    aus = {"laeufer_je_eta0": {str(e0): int((d["eta0"] == e0).sum()) for e0 in ETA0S}}
    aus["aktiv_anteil"] = {str(e0): {str(n): r_haupt[e0][n]["anzahl"] / int((d["eta0"] == e0).sum())
                                     for n in (1, 5, 10, 20, 30, 50, 100)} for e0 in ETA0S}
    aus["ende_grund"] = {"kein_zulaessiger_link": int((d["grund"] == 1).sum()),
                         "100_schritte": int((d["grund"] == 0).sum())}
    aus["erster_nicht_bulk_median"] = float(np.median(T))
    st = schritte(d, T)
    vor, deta, e0s, tau = st["innen"]
    aus["sigma2_je_schritt_innen"] = {str(e0): float((deta[e0s == e0] ** 2).mean()) for e0 in ETA0S}
    aus["sigma2_je_schritt_innen"]["alle"] = float((deta ** 2).mean())
    aus["betrag_deta_mittel_innen"] = float(np.abs(deta).mean())
    aus["tau_sqrtN_mittel_innen"] = float((tau * np.sqrt(N)).mean())
    aus["tau_sqrtN_mittel_rand"] = float((st["rand"][3] * np.sqrt(N)).mean()) if st["rand"][3].size else None
    ausg = d["bulk"][:, 1:] >= 0
    nla, nlz = d["nl_alle"][:, 1:], d["nl_zul"][:, 1:]
    gueltig = nla >= 0
    aus["tau_schnitt"] = {"links_gesamt": int(nla[gueltig].sum()), "davon_tau_gross": int((nla - nlz)[gueltig].sum()),
                          "anteil": float((nla - nlz)[gueltig].sum() / max(nla[gueltig].sum(), 1)),
                          "punkte_mit_schnitt": int(((nla - nlz) > 0)[gueltig].sum()),
                          "punkte": int(gueltig.sum()),
                          "zulaessige_links_mittel": float(nlz[gueltig].mean())}
    # Zukunftslinks an besuchten Punkten gegen die Ortsformel H_{N-1} + ln((1-u)(1-v)) [M], fuer c N > 100
    H = float(np.sum(1.0 / np.arange(1, N, dtype=np.float64)))
    u_vor, v_vor = d["uu"][:, :-1], d["vv"][:, :-1]
    c = (1.0 - u_vor) * (1.0 - v_vor)
    s = gueltig & np.isfinite(c) & (c * N > 100.0)
    diff = nla[s] - (H + np.log(c[s]))
    aus["linkzahl_besuchte_punkte"] = {"punkte": int(s.sum()), "mittel_minus_erwartung": float(diff.mean()),
                                       "se": float(diff.std(ddof=1) / np.sqrt(diff.size))}
    aus["schritte_innen"] = schritte_tabelle(vor, deta)
    aus["schritte_rand"] = schritte_tabelle(st["rand"][0], st["rand"][1])
    return aus, st


def ks0(ordner):
    dateien = sorted(glob.glob(os.path.join(ordner, "links-N%d-s*.json" % N_HAUPT)))
    laeufe = [json.load(open(p)) for p in dateien]
    laeufe = [x for x in laeufe if x.get("status") == "fertig"]
    werte = {"saaten": len(laeufe)}
    if not laeufe:
        return "nicht auswertbar", None, werte
    ziel = float(np.log(N_HAUPT) - 1.42)
    alle = float(np.mean([x["links_je_punkt_alle"] for x in laeufe]))
    zp = sum(x["zentrum_punkte"] for x in laeufe)
    zs = sum(x["zentrum_summe"] for x in laeufe)
    zq = sum(x["zentrum_quadratsumme"] for x in laeufe)
    zm = zs / zp
    zse = float(np.sqrt((zq / zp - zm * zm) * zp / (zp - 1) / zp))
    werte.update({
        "ziel_ln_N_minus_1_42": ziel,
        "berichtigt_alle_punkte_mittel": alle,
        "berichtigt_abweichung": alle - ziel,
        "berichtigt_je_saat": [x["links_je_punkt_alle"] for x in laeufe],
        "exakt_L_durch_N": laeufe[0]["erwartung_exakt_L_durch_N"],
        "wortlaut_zentrum_punkte": zp, "wortlaut_zentrum_mittel": zm, "wortlaut_zentrum_se": zse,
        "wortlaut_abweichung": zm - ziel,
        "zentrum_erwartung_ortsabhaengig": float(np.average([x["zentrum_erwartung_ortsabhaengig"] for x in laeufe],
                                                            weights=[x["zentrum_punkte"] for x in laeufe])),
        "alle_cN_gross_mittel_minus_erwartung": [x["alle_cN_gross_mittel_minus_erwartung"] for x in laeufe],
        "anteil_links_tau_gross_alle": [x["anteil_links_tau_gross_alle"] for x in laeufe],
        "anteil_links_tau_gross_zentrum": [x["anteil_links_tau_gross_zentrum"] for x in laeufe],
    })
    berichtigt = "eingetroffen" if abs(alle - ziel) <= KS0_TOL else "nicht eingetroffen"
    wortlaut = "eingetroffen" if abs(zm - ziel) <= KS0_TOL else "nicht eingetroffen"
    return berichtigt, wortlaut, werte


def lade_bulk(ordner):
    dateien = sorted(glob.glob(os.path.join(ordner, "bulk-s*.npz")))
    if not dateien:
        return None
    z = [np.load(p) for p in dateien]
    k = [json.load(open(p[:-4] + ".json")) for p in dateien]
    return {"eta0": np.concatenate([x["eta0"] for x in z]), "eta": np.concatenate([x["eta"] for x in z]),
            "deta": np.concatenate([x["deta"] for x in z]), "tau_sqrtN": np.concatenate([x["tau_sqrtN"] for x in z]),
            "koepfe": k}


def kompakt(r, n_liste=(0, 1, 5, 10, 20, 30, 50, 75, 100)):
    return {str(e0): [r[e0][n] for n in n_liste] for e0 in ETA0S}


def bilder(ausgabe, R, bulk_r):
    plt.rcParams.update({"font.size": 10, "axes.edgecolor": TINTE2, "axes.labelcolor": TINTE, "xtick.color": TINTE2,
                         "ytick.color": TINTE2, "axes.facecolor": FLAECHE, "figure.facecolor": FLAECHE,
                         "lines.linewidth": 2.0})
    n = np.arange(NMAX + 1)

    def spalte(r, e0, feld):
        return np.array([z.get(feld, np.nan) if z["anzahl"] >= MIN_AKTIV else np.nan for z in r[e0]])

    # 1. Drift
    fig, achsen = plt.subplots(1, 3, figsize=(13, 4.2), sharey=True)
    for ax, e0 in zip(achsen, ETA0S):
        f = FARBEN[e0]
        m, se = spalte(R["haupt64"], e0, "mittel"), spalte(R["haupt64"], e0, "se")
        ax.fill_between(n, m - se, m + se, color=f, alpha=0.25, lw=0)
        ax.plot(n, m, color=f, label="Hauptregel, N = 64 000 (+-1 SE)")
        ax.plot(n, spalte(R["haupt16"], e0, "mittel"), color=f, lw=1.0, alpha=0.8, label="Hauptregel, N = 16 000")
        ax.plot(n, spalte(R["eingefroren64"], e0, "mittel"), color=TINTE, ls="--", lw=1.2,
                label="eingefroren (alle Laeufer), N = 64 000")
        ax.plot(n, spalte(R["naiv64"], e0, "mittel"), color=TINTE2, ls=":", lw=1.5,
                label="bis zum Rand (ohne Randregel), N = 64 000")
        ax.axhline(0.0, color=TINTE2, lw=0.8)
        ax.axvline(N_KS1, color=TINTE2, lw=0.6, ls="-.")
        ax.set_title("eta_0 = %+.0f" % e0, color=TINTE)
        ax.set_xlabel("Schritt n")
        ax.grid(alpha=0.25)
    achsen[0].set_ylabel("<eta_n - eta_0>")
    achsen[0].legend(fontsize=7.5, loc="lower left")
    fig.suptitle("KAUSAL-SWERVE-1: mittlere Aenderung der Rapiditaet (Kurven nur bei >= %d aktiven Laeufern)"
                 % MIN_AKTIV, color=TINTE)
    fig.tight_layout()
    fig.savefig(os.path.join(ausgabe, "drift_n.png"), dpi=130)
    plt.close(fig)

    # 2. Varianz
    fig, achsen = plt.subplots(1, 2, figsize=(12, 4.4))
    for ax, schluessel, titel in ((achsen[0], "haupt64", "Hauptregel, N = 64 000"),
                                  (achsen[1], "haupt16", "Hauptregel, N = 16 000")):
        for e0 in ETA0S:
            ax.plot(n, spalte(R[schluessel], e0, "var"), color=FARBEN[e0], label="eta_0 = %+.0f" % e0)
        if bulk_r is not None:
            ax.plot(n, [z["var"] for z in bulk_r[0.0]], color=TINTE2, ls=":", lw=1.5,
                    label="unbegrenzte Streuung (Kontrolle), eta_0 = 0")
        ax.plot(n, SIGMA2_BULK * n, color=TINTE, ls="--", lw=1.0, label="Schreibtisch n/4")
        ax.axvspan(N_FIT[0], N_FIT[1], color=TINTE2, alpha=0.06, lw=0)
        ax.set_ylim(0, 14)
        ax.set_xlabel("Schritt n")
        ax.set_ylabel("Var(eta_n - eta_0)")
        ax.set_title(titel, color=TINTE)
        ax.grid(alpha=0.25)
        ax.legend(fontsize=8, loc="upper left")
    fig.suptitle("KAUSAL-SWERVE-1: Streuung der Rapiditaet (grau hinterlegt: Fitbereich n = 5 bis 50)", color=TINTE)
    fig.tight_layout()
    fig.savefig(os.path.join(ausgabe, "var_n.png"), dpi=130)
    plt.close(fig)

    # 3. Energie
    fig, ax = plt.subplots(figsize=(8, 4.8))
    for e0 in ETA0S:
        f = FARBEN[e0]
        m, se = spalte(R["haupt64"], e0, "cosh"), spalte(R["haupt64"], e0, "cosh_se")
        ax.fill_between(n, m - se, m + se, color=f, alpha=0.25, lw=0)
        ax.plot(n, m, color=f, label="eta_0 = %+.0f, Hauptregel N = 64 000" % e0)
    if bulk_r is not None:
        ax.plot(n, [z["cosh"] for z in bulk_r[0.0]], color=TINTE2, ls=":", lw=1.5,
                label="unbegrenzte Streuung, eta_0 = 0 (Stichprobenmittel)")
    ax.plot(n, PHI_BULK ** n, color=TINTE, ls="--", lw=1.0, label="Schreibtisch 1,138^n (eta_0 = 0)")
    ax.set_yscale("log")
    ax.set_ylim(0.8, 2e3)
    ax.set_xlabel("Schritt n")
    ax.set_ylabel("<cosh eta_n>")
    ax.grid(alpha=0.25, which="both")
    ax.legend(fontsize=8, loc="upper left")
    ax.set_title("KAUSAL-SWERVE-1: mittlere Energie je Masse", color=TINTE)
    fig.tight_layout()
    fig.savefig(os.path.join(ausgabe, "cosh_n.png"), dpi=130)
    plt.close(fig)

    # 4. Kontrollen: aktiver Anteil und Drift je Schritt
    fig, achsen = plt.subplots(1, 2, figsize=(12, 4.4))
    ax = achsen[0]
    for e0 in ETA0S:
        for schluessel, ls, txt in (("haupt64", "-", "N = 64 000"), ("haupt16", "--", "N = 16 000")):
            gesamt = R[schluessel][e0][0]["anzahl"]
            ax.plot(n, [z["anzahl"] / gesamt for z in R[schluessel][e0]], color=FARBEN[e0], ls=ls,
                    lw=1.6 if ls == "-" else 1.1, label="eta_0 = %+.0f, %s" % (e0, txt))
    ax.set_xlabel("Schritt n")
    ax.set_ylabel("Anteil noch aktiv (Hauptregel)")
    ax.set_ylim(0, 1.02)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=7.5)
    ax = achsen[1]
    mitte = 0.5 * (KANTEN[:-1] + KANTEN[1:])
    for schluessel, farbe, txt, ver in (("innen", TINTE, "bulk-exakte Schritte (Hauptregel)", -0.04),
                                        ("rand", TINTE2, "Schritte nach dem Randkontakt", 0.04)):
        z = R["schritte64"][schluessel]["klassen"]
        m = np.array([x.get("mittel", np.nan) if x["anzahl"] >= 30 else np.nan for x in z])
        se = np.array([x.get("se", np.nan) if x["anzahl"] >= 30 else np.nan for x in z])
        ax.errorbar(mitte + ver, m, yerr=se, fmt="o", ms=4, color=farbe, label=txt, capsize=2)
    ax.axhline(0.0, color=TINTE2, lw=0.8)
    ax.set_xlabel("Rapiditaet vor dem Schritt")
    ax.set_ylabel("mittlere Aenderung je Schritt")
    ax.set_title("N = 64 000, Klassen 0,5 (nur Klassen mit >= 30 Schritten)", color=TINTE)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(ausgabe, "kontrollen.png"), dpi=130)
    plt.close(fig)


def main():
    global N_HAUPT, N_NEBEN
    ordner, ausgabe = sys.argv[1], sys.argv[2]
    if len(sys.argv) > 4:  # nur fuer den Rauch (Pfadprobe mit kleinen N); Hauptauswertung ohne diese Argumente
        N_HAUPT, N_NEBEN = int(sys.argv[3]), int(sys.argv[4])
    os.makedirs(ausgabe, exist_ok=True)
    t0 = time.time()
    d64, d16 = lade_laeufer(ordner, N_HAUPT), lade_laeufer(ordner, N_NEBEN)
    T64, haupt64, naiv64, eing64, _ = populationen(d64)
    T16, haupt16, naiv16, eing16, _ = populationen(d16)
    R = {"haupt64": reihen_je_eta0(d64["eta"], d64["eta0"], haupt64),
         "naiv64": reihen_je_eta0(d64["eta"], d64["eta0"], naiv64),
         "eingefroren64": reihen_je_eta0(eing64, d64["eta0"], np.ones_like(haupt64)),
         "haupt16": reihen_je_eta0(d16["eta"], d16["eta0"], haupt16),
         "naiv16": reihen_je_eta0(d16["eta"], d16["eta0"], naiv16),
         "eingefroren16": reihen_je_eta0(eing16, d16["eta0"], np.ones_like(haupt16))}
    b = lade_bulk(ordner)
    bulk_r = reihen_je_eta0(b["eta"], b["eta0"], np.ones(b["eta"].shape, dtype=bool)) if b is not None else None
    besch64, _ = beschreibung(d64, N_HAUPT, T64, R["haupt64"])
    besch16, _ = beschreibung(d16, N_NEBEN, T16, R["haupt16"])
    R["schritte64"] = {"innen": besch64["schritte_innen"], "rand": besch64["schritte_rand"]}

    haupt = alle_urteile(R["haupt64"])
    gegen = {"N16000_hauptregel": alle_urteile(R["haupt16"]),
             "N64000_eingefroren": alle_urteile(R["eingefroren64"]),
             "N64000_bis_zum_rand": alle_urteile(R["naiv64"]),
             "N16000_eingefroren": alle_urteile(R["eingefroren16"]),
             "N16000_bis_zum_rand": alle_urteile(R["naiv16"])}
    if bulk_r is not None:
        gegen["unbegrenzte_streuung"] = alle_urteile(bulk_r)
    gegen_kurz = {k: {kk: vv[0] for kk, vv in v.items()} for k, v in gegen.items()}

    ks0_b, ks0_w, ks0_werte = ks0(ordner)
    urteile = {
        "KS0": {"urteil": ks0_b,
                "vermerk": "Kartenfehler (PLAN Abschnitt 1.1): ln N - 1,42 ist das Mittel ueber alle Punkte des "
                           "Diamanten (L/N), nicht der Wert fern vom Rand. Urteil hier berichtigt (alle Punkte). "
                           "Urteil nach Kartenwortlaut (Zentrumspunkte u, v in [0,4; 0,6]): %s." % ks0_w,
                "werte": dict(ks0_werte, urteil_kartenwortlaut=ks0_w)},
        "KS1": {"urteil": haupt["KS1"][0],
                "werte": dict(haupt["KS1"][1], se_ueber_bloecke=ks1_block_se(d64, haupt64))},
        "KS2": {"urteil": haupt["KS2"][0], "werte": haupt["KS2"][1]},
        "KS3": {"urteil": haupt["KS3"][0], "werte": haupt["KS3"][1]},
    }
    for k in ("KS1", "KS2", "KS3"):
        urteile[k]["vermerk"] = ("Hauptregel (PLAN Abschnitt 4): N = 64 000, Laeufer bis zum ersten nicht "
                                 "bulk-exakten Schritt. Gegenproben ohne Urteilskraft: " +
                                 "; ".join("%s: %s" % (g, gegen_kurz[g][k]) for g in gegen_kurz))
    aus = {
        "karte": "KAUSAL-SWERVE-1", "plan": "PLAN.md (eingefroren)", "skript_sha256": SKRIPT_SHA,
        "laufkoepfe_sha": sorted(set(kk["skript_sha256"] for kk in d64["koepfe"] + d16["koepfe"])),
        "urteile": urteile,
        "gegenproben": {k: {kk: {"urteil": vv[0], "werte": vv[1]} for kk, vv in v.items()} for k, v in gegen.items()},
        "beschreibung": {"N64000": besch64, "N16000": besch16,
                         "bulk": ({"koepfe": b["koepfe"],
                                   "sigma2_je_schritt": float((b["deta"] ** 2).mean()),
                                   "betrag_mittel": float(np.abs(b["deta"]).mean()),
                                   "cosh_deta_mittel": float(np.cosh(b["deta"]).mean()),
                                   "tau_sqrtN_mittel": float(b["tau_sqrtN"].mean()),
                                   "schritte": int(b["deta"].size)} if b is not None else None),
                         "reihen_N64000_hauptregel": kompakt(R["haupt64"]),
                         "reihen_N64000_eingefroren": kompakt(R["eingefroren64"]),
                         "reihen_N64000_bis_zum_rand": kompakt(R["naiv64"]),
                         "reihen_N16000_hauptregel": kompakt(R["haupt16"]),
                         "reihen_unbegrenzt": kompakt(bulk_r) if bulk_r is not None else None},
        "laufzeit_s": round(time.time() - t0, 2),
        "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    with open(os.path.join(ausgabe, "auswertung.json"), "w") as fh:
        json.dump(aus, fh, indent=1)
    bilder(ausgabe, R, bulk_r)
    print(json.dumps({k: v["urteil"] for k, v in urteile.items()}))
    print(json.dumps(gegen_kurz))


if __name__ == "__main__":
    main()
