"""WOLFRAM-KEV-SCAN Auswertung (Physik-venv, nur Standardbibliothek): Top 15 je Schicht, Leseliste 30 Seiten, Abdeckung,
Gegenprobe (blind, 25 Abschnitte) mit Stichwort-Vergleich und den Urteilsregeln WK0 bis WK2 aus PLAN.md.

Aufruf: python code/auswertung.py daten/abschnitte.jsonl 'lauf-69/kev-*.jsonl' gegenprobe-hand.json code/stichworte.json \
        seiten/INDEX.tsv 'lauf-69/lauf-*.log' lauf-69/
"""
import glob, json, math, os, re, sys

SCHICHTEN = ["S0", "S1", "S2", "S3", "S4"]
TOP = 15; LESE = 30; K_TOP = 10


def ranks(xs):
    """Mittlere Raenge (1 = kleinster Wert)."""
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs); i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        for t in range(i, j + 1):
            r[order[t]] = (i + j) / 2 + 1
        i = j + 1
    return r


def pearson(x, y):
    n = len(x)
    if n < 3: return None
    mx, my = sum(x) / n, sum(y) / n
    sxx = sum((a - mx) ** 2 for a in x); syy = sum((b - my) ** 2 for b in y)
    if sxx == 0 or syy == 0: return None
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / math.sqrt(sxx * syy)


def spearman(x, y):
    return pearson(ranks(x), ranks(y))


def auc(scores, labels):
    pos = [s for s, l in zip(scores, labels) if l]; neg = [s for s, l in zip(scores, labels) if not l]
    if not pos or not neg: return None
    g = sum((p > q) + 0.5 * (p == q) for p in pos for q in neg)
    return g / (len(pos) * len(neg))


def treffer_at_k(scores, labels, k=K_TOP):
    """Erwartete Zahl relevanter Abschnitte unter den Top k bei zufaelliger Aufloesung von Gleichstaenden."""
    k = min(k, len(scores))
    werte = sorted(set(scores), reverse=True); genommen = 0; treffer = 0.0
    for w in werte:
        gruppe = [l for s, l in zip(scores, labels) if s == w]
        platz = k - genommen
        if platz <= 0: break
        if len(gruppe) <= platz:
            treffer += sum(gruppe); genommen += len(gruppe)
        else:
            treffer += sum(gruppe) * platz / len(gruppe); genommen += platz
    return treffer


def quantil(xs, q):
    xs = sorted(xs)
    if not xs: return None
    return xs[min(len(xs) - 1, int(q * (len(xs) - 1) + 0.5))]


def main():
    abschnitte_pfad, kev_glob, hand_pfad, stich_pfad, index_pfad, log_glob, aus = sys.argv[1:8]
    abschnitte = [json.loads(z) for z in open(abschnitte_pfad, encoding="utf-8")]
    nach_id = {x["id"]: x for x in abschnitte}
    kev = {}
    for p in sorted(glob.glob(kev_glob)):
        for z in open(p, encoding="utf-8"):
            r = json.loads(z)
            kev.setdefault(r["id"], r)        # erster Eintrag gilt (Folgelaeufe setzen nur fort)
    stich = {k: re.compile(v, re.I) for k, v in json.load(open(stich_pfad)).items() if not k.startswith("_")}
    kw = {x["id"]: {s: len(stich[s].findall(x["text"])) for s in stich} for x in abschnitte}

    def kevwert(i, s):
        a = kev[i]["antworten"]
        if s in SCHICHTEN: return a[s]["score"]
        if s in ("konkret", "kausal"): return a[s]["noul"]
        raise KeyError(s)

    bewertet = [i for i in nach_id if i in kev]
    fehlend = [i for i in nach_id if i not in kev]
    nan = [i for i in bewertet if kev[i].get("nan")]
    gueltig = [i for i in bewertet if not kev[i].get("nan")]

    # Abdeckung
    idx = [z.split("\t") for z in open(index_pfad, encoding="utf-8").read().splitlines()[1:] if z.strip()]
    laeufe = []
    for p in sorted(glob.glob(log_glob)):
        ev = {}
        for z in open(p, encoding="utf-8", errors="replace"):
            z = z.strip()
            if z.startswith("{"):
                try:
                    d = json.loads(z); ev[d.get("ereignis")] = d
                except Exception: pass
            elif z.startswith("start ") or z.startswith("ende "):
                ev.setdefault("starter", []).append(z)
        laeufe.append({"log": os.path.basename(p), "geladen_s": (ev.get("geladen") or {}).get("ladezeit_s"),
                       "ende": ev.get("ende"), "starter": ev.get("starter")})
    ms = sorted(kev[i]["ms"] for i in bewertet)
    abdeckung = {"seiten_abgerufen": len(idx), "seiten_ok_html": sum(1 for z in idx if z[-1] == "ok"),
                 "seiten_mit_abschnitten": len({nach_id[i]["seite"] for i in nach_id}),
                 "abschnitte": len(abschnitte), "abschnitte_bewertet": len(bewertet), "fehlend": len(fehlend), "fehlend_ids": fehlend[:50],
                 "nan": len(nan), "kev_rechenzeit_s": round(sum(ms) / 1000, 1),
                 "ms_je_abschnitt": {"median": quantil(ms, 0.5), "p90": quantil(ms, 0.9), "max": ms[-1] if ms else None},
                 "laeufe": laeufe}

    def kurz(i):
        x = nach_id[i]
        t = x["text"]
        return {"id": i, "url": x["url"], "ueberschrift": x["ueberschrift"][:120], "auszug": (t[:220] + "...") if len(t) > 220 else t,
                "kev": {s: kevwert(i, s) for s in SCHICHTEN + ["konkret", "kausal"]} | {"art": kev[i]["antworten"]["art"]["choice"]},
                "stichwort": kw[i]}

    # Verteilungen
    vert = {}
    for s in SCHICHTEN + ["konkret", "kausal"]:
        v = [kevwert(i, s) for i in gueltig]
        m = sum(v) / len(v) if v else None
        vert[s] = {"mittel": round(m, 3) if v else None, "sd": round(math.sqrt(sum((x - m) ** 2 for x in v) / len(v)), 3) if v else None,
                   "min": min(v) if v else None, "q10": quantil(v, .1), "median": quantil(v, .5), "q90": quantil(v, .9), "max": max(v) if v else None}
    arten = {}
    for i in gueltig:
        c = kev[i]["antworten"]["art"]["choice"]; arten[c] = arten.get(c, 0) + 1
    vert["art"] = arten
    vert["kausal_anteil_ueber_0_5"] = round(sum(1 for i in gueltig if kevwert(i, "kausal") > .5) / max(1, len(gueltig)), 3)
    vert["konkret_anteil_ueber_0_5"] = round(sum(1 for i in gueltig if kevwert(i, "konkret") > .5) / max(1, len(gueltig)), 3)

    # Top 15 je Schicht (Kev) und Stichwort-Top 15 zum Vergleich
    top, top_kw, vergleich = {}, {}, {}
    for s in SCHICHTEN + ["kausal"]:
        reihe = sorted(gueltig, key=lambda i: (-kevwert(i, s), -kevwert(i, "konkret"), i))
        top[s] = [kurz(i) for i in reihe[:TOP]]
        reihe_kw = sorted(gueltig, key=lambda i: (-kw[i][s], -nach_id[i]["woerter"], i))
        top_kw[s] = [{"id": i, "url": nach_id[i]["url"], "ueberschrift": nach_id[i]["ueberschrift"][:120], "treffer": kw[i][s],
                      "kev": kevwert(i, s)} for i in reihe_kw[:TOP]]
        vergleich[s] = {"ueberlappung_top15": len(set(reihe[:TOP]) & set(reihe_kw[:TOP])),
                        "spearman_kev_gegen_stichwort_alle": (lambda r: round(r, 3) if r is not None else None)(
                            spearman([kevwert(i, s) for i in gueltig], [kw[i][s] for i in gueltig]))}

    # Leseliste: Seitenwert = Mittel ueber S0..S4 des besten Abschnittswerts der Seite
    seiten = {}
    for i in gueltig:
        seiten.setdefault(nach_id[i]["seite"], []).append(i)
    lese = []
    for nr, ids in seiten.items():
        maxima = {s: max(kevwert(i, s) for i in ids) for s in SCHICHTEN}
        wert = sum(maxima.values()) / len(SCHICHTEN)
        beste = sorted(ids, key=lambda i: -max(kevwert(i, s) for s in SCHICHTEN))[:2]
        x = nach_id[ids[0]]
        lese.append({"seite": nr, "url": x["url"], "titel": x["titel"][:120], "seitenwert": round(wert, 3),
                     "maxima": maxima, "staerkste_schicht": max(SCHICHTEN, key=lambda s: maxima[s]), "abschnitte": len(ids),
                     "konkret_max": max(kevwert(i, "konkret") for i in ids), "kausal_max": max(kevwert(i, "kausal") for i in ids),
                     "beste_abschnitte": [{"id": i, "ueberschrift": nach_id[i]["ueberschrift"][:100]} for i in beste]})
    lese.sort(key=lambda r: (-r["seitenwert"], -r["konkret_max"], r["seite"]))

    # Gegenprobe
    gp = {"vorhanden": os.path.exists(hand_pfad)}
    if gp["vorhanden"]:
        hand = json.load(open(hand_pfad, encoding="utf-8"))["labels"]
        ids = sorted(hand)
        gp["n"] = len(ids); gp["ids_ohne_kev"] = [i for i in ids if i not in kev or kev[i].get("nan")]
        ids = [i for i in ids if i in kev and not kev[i].get("nan")]
        je = {}
        for s in SCHICHTEN + ["kausal"]:
            lab = [int(hand[i][s]) for i in ids]
            k = sum(lab)
            sk = [kevwert(i, s) for i in ids]; sw = [kw[i][s] for i in ids]
            hk, hw = treffer_at_k(sk, lab), treffer_at_k(sw, lab)
            rnd = min(K_TOP, len(ids)) * k / len(ids) if ids else None
            je[s] = {"k_relevant": k, "kev_treffer_top10": round(hk, 2), "stichwort_treffer_top10": round(hw, 2),
                     "zufall_erwartet_top10": round(rnd, 2) if rnd is not None else None, "maximal_moeglich": min(K_TOP, k),
                     "spearman_kev": (round(spearman(sk, lab), 3) if spearman(sk, lab) is not None else None),
                     "spearman_stichwort": (round(spearman(sw, lab), 3) if spearman(sw, lab) is not None else None),
                     "auc_kev": (round(auc(sk, lab), 3) if auc(sk, lab) is not None else None),
                     "auc_stichwort": (round(auc(sw, lab), 3) if auc(sw, lab) is not None else None),
                     "wk1_gefordert": min(6, k) if k else None,
                     "wk1_erfuellt": (hk >= min(6, k)) if k else None}
        gp["je_schicht"] = je
        mit = [s for s in SCHICHTEN if je[s]["k_relevant"] >= 1]
        mk = sum(je[s]["kev_treffer_top10"] for s in mit) / len(mit) if mit else None
        mw = sum(je[s]["stichwort_treffer_top10"] for s in mit) / len(mit) if mit else None
        gp["schichten_mit_relevanten"] = mit
        gp["mittel_treffer_top10_kev"] = round(mk, 3) if mk is not None else None
        gp["mittel_treffer_top10_stichwort"] = round(mw, 3) if mw is not None else None
        gp["WK1"] = all(je[s]["wk1_erfuellt"] for s in mit) if mit else None
        gp["WK2"] = (mk > mw) if mit else None
        gp["einzelwerte"] = [{"id": i, "hand": {s: hand[i][s] for s in SCHICHTEN + ["kausal"]},
                              "kev": {s: kevwert(i, s) for s in SCHICHTEN + ["kausal"]}, "stichwort": kw[i]} for i in ids]
    wk0 = {"alle_abschnitte_bewertet": len(fehlend) == 0 and len(nan) == 0,
           "laeufe_hoechstens_600s": all(((l.get("ende") or {}).get("t_s") or 0) <= 600 for l in laeufe)}
    wk0["WK0"] = wk0["alle_abschnitte_bewertet"] and wk0["laeufe_hoechstens_600s"]

    erg = {"abdeckung": abdeckung, "verteilungen": vert, "top15": top, "top15_stichwort": top_kw, "vergleich_kev_stichwort": vergleich,
           "leseliste": lese[:LESE], "gegenprobe": gp, "urteile": {"WK0": wk0, "WK1": gp.get("WK1"), "WK2": gp.get("WK2")}}
    os.makedirs(aus, exist_ok=True)
    json.dump(erg, open(os.path.join(aus, "auswertung.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    # Tabellen fuer ERGEBNIS.md (Markdown)
    L = []
    for s in SCHICHTEN + ["kausal"]:
        L.append(f"\n### Top {TOP} {s}\n\n| # | Kev {s} | konkret | Art | Seite | Ueberschrift | Auszug |\n|---|---|---|---|---|---|---|")
        for n, r in enumerate(top[s], 1):
            ausz = r["auszug"][:140].replace("|", "/").replace("\n", " ")
            L.append(f"| {n} | {r['kev'][s]} | {r['kev']['konkret']} | {r['kev']['art']} | {r['url'].replace('https://www.wolframphysics.org', '')} | {r['ueberschrift'][:60].replace('|', '/')} | {ausz} |")
    L.append(f"\n### Leseliste ({LESE} Seiten)\n\n| # | Seitenwert | staerkste | S0 | S1 | S2 | S3 | S4 | Abschn. | URL |\n|---|---|---|---|---|---|---|---|---|---|")
    for n, r in enumerate(lese[:LESE], 1):
        mx = r["maxima"]
        L.append(f"| {n} | {r['seitenwert']} | {r['staerkste_schicht']} | {mx['S0']} | {mx['S1']} | {mx['S2']} | {mx['S3']} | {mx['S4']} | {r['abschnitte']} | {r['url'].replace('https://www.wolframphysics.org', '')} |")
    open(os.path.join(aus, "tabellen.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(json.dumps({"abdeckung": {k: v for k, v in abdeckung.items() if k not in ("laeufe", "fehlend_ids")},
                      "urteile": erg["urteile"], "gegenprobe_mittel": [gp.get("mittel_treffer_top10_kev"), gp.get("mittel_treffer_top10_stichwort")]},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
