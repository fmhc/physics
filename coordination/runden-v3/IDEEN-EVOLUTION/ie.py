#!/usr/bin/env python3
"""Ideen-Evolution: Hilfsskript der Leitung, von Hand aufgerufen. Kein Dienst, kein Timer, kein Netz, nur Standardbibliothek.
  python3 ie.py pruefen | statistik
  python3 ie.py ziehen --gen N --saat S [--slots "mutation=3D-RES; kreuzung=R-2+Bio 46"] [--zufall 3] [--frisch 1]
                       [--reserve 2] [--eintragen]
  python3 ie.py setze ID feld=wert [feld=wert ...]
Nur "ziehen --eintragen" und "setze" schreiben pool.jsonl, vorher Sicherung pool.jsonl.bak-JJJJMMTT-HHMMSS.
Mehrere Eltern mit "+" trennen, weil Kennungen Leerzeichen enthalten ("Wel 16")."""
import argparse, json, random, shutil, sys, time
from collections import Counter, defaultdict
from pathlib import Path

POOL = Path(__file__).resolve().with_name("pool.jsonl")
ORT = "coordination/runden-v3/IDEEN-EVOLUTION"  # Kartenpfade relativ zu /home/fmh/fmhc-physics
PFLICHT = ("id", "titel", "quelle", "stand", "entscheidung", "modellbezug", "generation", "eltern", "operator", "arm",
           "testpfad", "ergebnis_kurz")
STAENDE = {"getestet", "teilweise", "ungetestet", "laeuft", "indirekt", "geplant"}
ENTSCHEIDUNGEN = {"weiter", "parken", "verwerfen", "offen", "ungetestet", "indirekt"}
ENTSCHIEDEN = ("weiter", "parken", "verwerfen")
OPERATOREN = {"research": 1, "analogie": 1, "mutation": 1, "kreuzung": 2}  # Arm E: Operator -> Zahl der Eltern
SONST = {"Z": ("zufall", 1), "F": ("ideation", 0)}                         # Arm Z und F: Operator, Zahl der Eltern
FAKTOR, ABSTAND, MIN_E, MIN_Z = 1.5, 0.20, 10, 6                         # Vorsprungsregel (README, Abschnitt 6)

def wort(text):  # erstes Wort einer Entscheidung: "parken (bekannt)" -> "parken"
    return str(text or "").split(" ")[0].strip(";,:").lower()

def lesen():
    return [json.loads(z) for z in POOL.read_text(encoding="utf-8").splitlines() if z.strip()]

def schreiben(karten):
    bak = POOL.with_name(POOL.name + time.strftime(".bak-%Y%m%d-%H%M%S"))
    shutil.copy2(POOL, bak)
    POOL.write_text("".join(json.dumps(k, ensure_ascii=False) + "\n" for k in karten), encoding="utf-8")
    print(f"geschrieben: {POOL.name}, {len(karten)} Zeilen; Sicherung {bak.name}")

def pruefen(_):
    try:
        karten = lesen()
    except ValueError as e:
        return print(f"FEHLER: eine Zeile ist kein gueltiges JSON ({e})") or 1
    fehler, ids = [], set()
    for nr, k in enumerate(karten, 1):
        wo, fehlt = f"Zeile {nr} ({k.get('id')})", [f for f in PFLICHT if f not in k]
        if fehlt:
            fehler.append(f"{wo}: Pflichtfeld fehlt: {', '.join(fehlt)}")
            continue
        gen_ok = isinstance(k["generation"], int) and k["generation"] >= 0 and isinstance(k["eltern"], list)
        fehler += [f"{wo}: {t}" for t, schlecht in (
            ("doppelte id", k["id"] in ids), (f"stand {k['stand']!r} unbekannt", k["stand"] not in STAENDE),
            (f"entscheidung {k['entscheidung']!r} unbekannt", wort(k["entscheidung"]) not in ENTSCHEIDUNGEN),
            ("generation (Zahl >= 0) oder eltern (Liste) falsch", not gen_ok)) if schlecht]
        ids.add(k["id"])
        if not gen_ok or k["generation"] < 1:
            continue
        soll = SONST.get(k["arm"]) or (k["operator"], OPERATOREN.get(k["operator"]) if k["arm"] == "E" else None)
        w = wort(k["entscheidung"])
        fehler += [f"{wo}: {t}" for t, schlecht in (
            (f"arm {k['arm']!r}, operator {k['operator']!r}, {len(k['eltern'])} Eltern passen nicht zusammen",
             k["operator"] != soll[0] or len(k["eltern"]) != soll[1]),
            ("entschieden, aber ohne testpfad", w in ENTSCHIEDEN and not k["testpfad"]),
            ("'weiter' ohne 'L1 ja' in latten (L1 schwach kann nicht weiter)",
             w == "weiter" and "L1 ja" not in str(k.get("latten", "")))) if schlecht]
    fehler += [f"{k.get('id')}: Elter {e!r} fehlt im Pool" for k in karten for e in k.get("eltern") or [] if e not in ids]
    zahl = Counter(wort(k.get("entscheidung")) for k in karten)
    print(f"{len(karten)} Karten: " + ", ".join(f"{w} {n}" for w, n in sorted(zahl.items())))
    print("".join(f"FEHLER: {f}\n" for f in fehler) + ("pruefen: ok" if not fehler else f"pruefen: {len(fehler)} Fehler"))
    return 1 if fehler else 0

def ziehen(a):
    karten = lesen()
    nach_id, slots = {k["id"]: k for k in karten}, []
    for teil in filter(None, (t.strip() for t in a.slots.split(";"))):
        op, _, rest = (s.strip() for s in teil.partition("="))
        eltern = [e.strip() for e in rest.split("+") if e.strip()]
        if OPERATOREN.get(op) != len(eltern) or any(e not in nach_id for e in eltern):
            sys.exit(f"Slot {teil!r}: unbekannter Elter oder falsche Elternzahl ({OPERATOREN}); nichts gezogen")
        for e in (e for e in eltern if wort(nach_id[e]["entscheidung"]) not in ("weiter", "parken")):
            print(f"Hinweis: Elter {e} steht auf '{nach_id[e]['entscheidung']}' (vorher abschaetzen)")
        slots.append(("E", op, eltern))
    slots += [("F", "ideation", [])] * a.frisch
    jetzt = {e for _, _, el in slots for e in el}
    schon = {e for k in karten if k["arm"] == "Z" and k["generation"] >= 1 for e in k["eltern"]}
    topf = sorted(k["id"] for k in karten if wort(k["entscheidung"]) in ("ungetestet", "parken") and k["stand"] != "laeuft"
                  and k["id"] not in jetzt | schon and not (k["arm"] == "Z" and k["generation"] >= 1))
    rng = random.Random(a.saat)
    gezogen = rng.sample(topf, min(len(topf), a.zufall + a.reserve))
    slots += [("Z", "zufall", [g]) for g in gezogen[:a.zufall]]
    folge = list(range(len(slots)))
    rng.shuffle(folge)  # neutrale Nummern: Ordnername und Ernte zeigen keinen Arm
    neu = []
    for nr, i in enumerate(folge, 1):
        (arm, op, eltern), kid = slots[i], f"G{a.gen}-{nr:02d}"
        alt = nach_id[eltern[0]] if arm == "Z" else {}
        neu.append(dict(zip(PFLICHT, (kid, alt.get("titel", "(vom Operator)"), f"{ORT}/GEN-{a.gen:02d}/{kid}/KARTE.md",
                   "geplant", "ungetestet", alt.get("modellbezug", ""), a.gen, eltern, op, arm, "", ""))))
    print(f"Generation {a.gen}, Saat {a.saat}: {len(neu)} Karten\n| id | arm | operator | eltern | titel |\n|---|---|---|---|---|\n"
          + "\n".join(f"| {k['id']} | {k['arm']} | {k['operator']} | {' + '.join(k['eltern'])} | {k['titel']} |" for k in neu)
          + f"\nZufallstopf: {len(topf)} Karten (ungetestet oder parken, nicht laufend, nicht Elter, nie gezogen)"
          + "\nReserve fuer Z, in dieser Reihenfolge: " + (" ; ".join(gezogen[a.zufall:]) or "keine")
          + "\nEltern-Kandidaten mit 'weiter': " + " ; ".join(k["id"] for k in karten if wort(k["entscheidung"]) == "weiter"))
    if a.eintragen:
        if a.gen < 1 or any(k["generation"] == a.gen for k in karten):
            sys.exit(f"Generation {a.gen} ist ungueltig oder steht schon im Pool; nichts geschrieben")
        schreiben(karten + neu)
    return 0

def setze(a):
    karten = lesen()
    k = next((k for k in karten if k["id"] == a.id), None)
    if k is None:
        k = {**{f: "" for f in PFLICHT}, "id": a.id, "eltern": [], "generation": -1}
        karten.append(k)
        print(f"neue Karte {a.id}: generation, arm und operator mitsetzen")
    for feld, gleich, wert in (p.partition("=") for p in a.felder):
        if not gleich:
            sys.exit(f"feld=wert erwartet, nicht {feld!r}; nichts geschrieben")
        k[feld] = int(wert) if feld == "generation" else (
            [e.strip() for e in wert.split("+") if e.strip()] if feld == "eltern" else wert)
    if wort(k["entscheidung"]) == "weiter" and "L1 ja" not in str(k.get("latten", "")):
        print("WARNUNG: 'weiter' ohne 'L1 ja' in latten; mit L1 schwach kann eine Karte nicht weiter (README)")
    schreiben(karten)
    return 0

def statistik(_):
    tab, offen, ops = defaultdict(lambda: [0, 0, 0, 0]), Counter(), defaultdict(lambda: [0, 0])
    for k in lesen():
        w, b, g = wort(k["entscheidung"]), wort(k.get("vorschlag_blind")), k["generation"]
        if w not in ENTSCHIEDEN:
            offen[g] += g >= 1
            continue
        z = tab[(g, k["arm"])]
        z[:] = z[0] + 1, z[1] + (w == "weiter"), z[2] + (b == "weiter"), z[3] + bool(b)
        if g >= 1:
            o = ops[k["operator"]]
            o[:] = o[0] + 1, o[1] + (w == "weiter")
    print("gen  arm        n  weiter (Leitung)  weiter (blind; Zahl der Vorschlaege)")
    for (g, arm), (n, wl, wb, nb) in sorted(tab.items()):
        print(f"{g:3d}  {arm:8s} {n:3d}  {wl:3d} = {wl / n:4.0%}       {wb:3d} ({nb} von {n})")
    print("".join(f"Generation {g}: {n} Karten noch ohne Entscheidung\n" for g, n in sorted(offen.items()) if n), end="")
    if ops:
        print("je Operator ab Generation 1 (beschreibend): " + "; ".join(f"{o} {w}/{n}" for o, (n, w) in sorted(ops.items())))
        print("Vorsprungsregel: q_E >= 1,5 q_Z und q_E - q_Z >= 0,20, mit Leitung und blind; n_E >= 10, n_Z >= 6")
    gens = sorted({g for g, _ in tab if g >= 1})
    for g in (g for g in gens if g + 1 in gens):
        (ne, we, be, nbe), (nz, wz, bz, nbz) = ([sum(tab[(h, arm)][i] for h in (g, g + 1)) for i in range(4)]
                                                for arm in ("E", "Z"))
        kopf = f"Vorsprungsregel Gen {g}+{g + 1}: E {we}/{ne}, Z {wz}/{nz} (Leitung); blind E {be}/{ne}, Z {bz}/{nz}"
        if offen[g] or offen[g + 1] or ne < MIN_E or nz < MIN_Z or nbe < ne or nbz < nz:
            print(kopf + " -> nicht entscheidbar (offene Karten, blinde Vorschlaege fehlen, n_E < 10 oder n_Z < 6)")
            continue
        vorn = lambda x, y: x / ne >= FAKTOR * y / nz and x / ne - y / nz >= ABSTAND
        print(kopf + (" -> Vorsprung der Evolution" if vorn(we, wz) and vorn(be, bz) else " -> kein Vorsprung"))
    return 0

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    u = p.add_subparsers(dest="befehl", required=True)
    u.add_parser("pruefen"), u.add_parser("statistik")
    z, s = u.add_parser("ziehen"), u.add_parser("setze")
    for name, typ, wert in (("--gen", int, None), ("--saat", int, None), ("--slots", str, ""), ("--zufall", int, 3),
                            ("--frisch", int, 1), ("--reserve", int, 2)):
        z.add_argument(name, type=typ, default=wert, required=wert is None)
    z.add_argument("--eintragen", action="store_true", help="gezogene Karten in pool.jsonl schreiben (mit .bak)")
    s.add_argument("id"), s.add_argument("felder", nargs="+", help="feld=wert; eltern mit + trennen")
    a = p.parse_args()
    return {"pruefen": pruefen, "ziehen": ziehen, "setze": setze, "statistik": statistik}[a.befehl](a)

if __name__ == "__main__":
    sys.exit(main())
