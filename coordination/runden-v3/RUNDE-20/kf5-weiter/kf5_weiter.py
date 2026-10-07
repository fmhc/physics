#!/usr/bin/env python3
"""KF-5 weiter (Runde 20, v3, Zufallskarte): die 2D-Geburt aus Runde 6 von T = 800 bis T = 2000 fortsetzen und mit dem
unveraenderten Klassifikator aus Runde 6 bei T = 1200, 1600 und 2000 einordnen.

Karte: coordination/runden-v3/RUNDE-20/kf5-weiter/KARTE.md; Plan (vor dem ersten Lauf eingefroren): PLAN.md daneben.
Importiert kf5_geburt.py aus Runde 6 unveraendert (/home/fmh/fmhc-physics-remote/runde6-kf5, wird nur gelesen): Gitter,
kraft_fn, dichten, analyse_arm, komponenten, eigenschaften, fenster_start, fenster_probe, fenster_auswerten, Familie
(familie_2d_m0.json daneben) und alle Konstanten (STUFEN, T_KON, T_AUS, FENSTER, DT_FENSTER, Schwellen).
Die Velocity-Verlet-Schleife steckt in kf5_geburt.lauf() und ist nicht einzeln aufrufbar; sie ist hier Zeile fuer Zeile
nachgebaut (gleiche Reihenfolge der Operationen, gleiche Schrittzaehlung t = Schritt * dt ab t = 0).

Unterbefehle (auf der .69 ueber kleintest.sh, GPU-Spur p4000a oder p4000b; zusammen auf einer CPU-Spur):
  k0      --stufe grob|fein --arm s03 [--rauch]
          K0a: analyse_arm auf dem gespeicherten T = 800-Zustand gegen die Runde-6-Zeile t = 800.
          K0b: derselbe Verlet mit -dt von 800 zurueck nach 760, dann vorwaerts 760 -> 800 mit Auswertung alle 10 und
               Messfenster [760, 800] wie Runde 6; Fensterurteile gegen Runde 6; Rueckkehrfehler gegen den 800-Zustand.
               Beginn der Abstammung (Wurzeln = Komponenten bei t = 760).
  weiter  --stufe grob|fein --arm s03 --von 800 --bis 1200 [--rauch]
          Fortsetzung ab dem gespeicherten Zustand (Runde-6-Datei bei 800, sonst eigener Zwischenspeicher bei --von),
          Auswertung alle 10 (auch bei --von), Messfenster [bis - 40, bis], Zwischenspeicher bei --bis.
  zusammen --arm s03 --stufen grob,fein --geraet cpu
          Tabelle je Tropfen bei 800, 1200, 1600, 2000 und Z0 bis Z4 nach den Regeln in PLAN.md.
--rauch: nur Durchlauf und Laufzeit (k0: 10 zurueck und vor; weiter: 800 -> 820, Fenster 10); keine Zustaende, keine
Tropfenzahlen in der Ausgabe.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"
import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import datetime  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402

R6 = "/home/fmh/fmhc-physics-remote/runde6-kf5"
sys.path.insert(0, R6)
import torch  # noqa: E402
import kf5_geburt as kg  # noqa: E402

HIER = os.path.dirname(os.path.abspath(__file__))
AUS = os.path.join(HIER, "lauf-69")
R6_AUS = os.path.join(R6, "lauf-69", "ausgabe")
T_R6 = 800.0
T_EVAL = (1200.0, 1600.0, 2000.0)
ABSCHNITTE = ((800.0, 1200.0), (1200.0, 1600.0), (1600.0, 2000.0))
ZEITGRENZE_S = 540.0
F64 = torch.float64
z7 = kg.z7


# ---------------------------------------------------------------- Hilfen

def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def sha(pfad):
    h = hashlib.sha256()
    with open(pfad, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def r6_name(stufe, arm):
    return "grob_box96_s03-s01-s08-frei-s03b-s01b" if stufe == "grob" else f"fein_box96_{arm}"


def frei_pfad(pfad):
    if os.path.exists(pfad) or os.path.exists(pfad + ".tmp"):
        raise SystemExit(f"{pfad} existiert schon: nichts ueberschreiben")
    return pfad


def schreibe_json(pfad, obj):
    frei_pfad(pfad)
    with open(pfad + ".tmp", "w") as fh:
        json.dump(obj, fh, indent=1)
    os.replace(pfad + ".tmp", pfad)


def herkunft():
    return {"kf5_geburt": os.path.join(R6, "kf5_geburt.py"), "kf5_geburt_sha256": sha(os.path.join(R6, "kf5_geburt.py")),
            "familie": kg.FAMILIE_DATEI, "familie_sha256": sha(kg.FAMILIE_DATEI),
            "kf5_weiter_sha256": sha(os.path.abspath(__file__)), "torch": torch.__version__,
            "geraet": kg.geraet_name()}


def lade_r6(stufe, arm):
    pfad = os.path.join(R6_AUS, r6_name(stufe, arm) + "_felder.pt")
    d = torch.load(pfad, map_location="cpu", weights_only=True)
    dx = kg.STUFEN[stufe][0]
    if (d["stufe"] != stufe or abs(float(d["dx"]) - dx) > 1e-12 or abs(float(d["t"]) - T_R6) > 1e-9
            or abs(float(d["box"]) - kg.BOX0) > 1e-9):
        raise SystemExit(f"Metadaten passen nicht: {pfad}")
    b = list(d["arme"]).index(arm)
    return {"psi": d["psi"][b:b + 1].clone(), "vel": d["vel"][b:b + 1].clone(), "t": float(d["t"]),
            "quelle": pfad, "quelle_sha256": sha(pfad), "arme_datei": list(d["arme"]), "index": b}


def lade_r6_json(stufe, arm):
    pfad = os.path.join(R6_AUS, r6_name(stufe, arm) + "_ergebnis.json")
    with open(pfad) as fh:
        d = json.load(fh)
    return d["arme"][arm], pfad


def aufbau(stufe, arm_name):
    dx, dt = kg.STUFEN[stufe]
    g = kg.Gitter(kg.BOX0, dx)
    arm = kg.ARME[arm_name]
    nl = torch.tensor([0.0 if arm["frei"] else 1.0], dtype=F64, device=kg.DEV).view(-1, 1, 1)
    return g, dt, arm, nl, kg.kraft_fn(g, nl)


# ---------------------------------------------------------------- Abstammung (Zusatz fuer Z3, nicht Teil des Klassifikators)

class Linie:
    """Abstammung der Komponenten der unteren Schwelle (Flaeche >= A_MIN, die Etiketten aus analyse_arm) ueber
    Maskenueberlapp zwischen zwei Auswertungen (dieselbe Ueberlappregel wie kf5_geburt.verknuepfung). Jede Komponente
    traegt die Menge ihrer Wurzeln; Wurzeln sind die Komponenten bei Beginn (t = 760, 'w<etikett>'), spaeter neu
    entstandene heissen 'n<t>:<etikett>'. Akte je Anfangswurzel: erste Verschmelzung mit fremder Wurzel, erste Teilung,
    Erloeschen."""

    def __init__(self, etik=None, wurzeln=None, akten=None):
        self.etik = etik
        self.wurzeln = wurzeln if wurzeln is not None else {}
        self.akten = akten if akten is not None else {}

    def start(self, neu, t):
        labels = torch.unique(neu[neu >= 0]).tolist()
        self.etik = neu
        self.wurzeln = {b: {f"w{b}"} for b in labels}
        self.akten = {f"w{b}": {"start_t": t, "verschmolzen": None, "partner": None, "geteilt": None, "erloschen": None}
                      for b in labels}

    def schritt(self, neu, t):
        labels = torch.unique(neu[neu >= 0]).tolist()
        eltern = {b: set() for b in labels}
        if self.etik is not None:
            beide = (self.etik >= 0) & (neu >= 0)
            if bool(beide.any()):
                kb = int(neu.max()) + 1
                for code in torch.unique(self.etik[beide] * kb + neu[beide]).tolist():
                    eltern[code % kb].add(code // kb)
        neu_w = {}
        for b in labels:
            w = set()
            for a in eltern[b]:
                w |= self.wurzeln[a]
            neu_w[b] = w if w else {f"n{t:g}:{b}"}
        traeger = {}
        for b, w in neu_w.items():
            for r in w:
                traeger.setdefault(r, []).append(b)
        for r, ak in self.akten.items():
            tb = traeger.get(r, [])
            if not tb and ak["erloschen"] is None:
                ak["erloschen"] = t
            if len(tb) >= 2 and ak["geteilt"] is None:
                ak["geteilt"] = t
            fremd = set()
            for b in tb:
                fremd |= neu_w[b] - {r}
            if fremd and ak["verschmolzen"] is None:
                ak["verschmolzen"] = t
                ak["partner"] = sorted(fremd)
        self.etik = neu
        self.wurzeln = neu_w

    def zu_json(self):
        return {"wurzeln": {str(b): sorted(w) for b, w in self.wurzeln.items()}, "akten": self.akten}

    @staticmethod
    def aus_json(etik, d):
        return Linie(etik, {int(b): set(w) for b, w in d["wurzeln"].items()}, d["akten"])


def tropfen_etiketten(g, s, rho, S0):
    """Etiketten der Tropfen (untere Schwelle), genau die Auswahl aus analyse_arm (gleiche Funktionen und Schwellen)."""
    maske = s >= kg.FAKTOREN[0] * S0
    etik, K, _ = kg.komponenten(maske)
    if K == 0:
        return [], []
    ei = kg.eigenschaften(g, etik, K, s, rho)
    gg = ei["flaeche"] >= kg.A_MIN
    tr = gg & ~ei["umspannt"] & (ei["rmax"] <= kg.KOMPAKT * ei["ra"])
    ids = tr.nonzero().flatten()
    return ids.tolist(), kg.liste(ei["x"][ids])


def familien_abstaende(fam, tr):
    """Zusatzgroessen je Fenstertropfen (vor dem Lauf festgelegt, PLAN.md): dQ* = Q_net / Q_fam(omega_ruhe) - 1 (dieselbe
    Groesse wie delta im Familientest, hier auch fuer 'nicht rund' und 'gestoert'), E/Q-Abstand und omega-Abstand."""
    q, om = tr.get("Q_net"), tr.get("omega_ruhe")
    dqs = None
    if q is not None and om is not None and q > 0.0:
        qf = fam.q(om)
        dqs = (q / qf - 1.0) if qf else None
    eq, eqf = tr.get("E_zu_Q"), tr.get("E_zu_Q_familie")
    of = tr.get("omega_familie_bei_Q")
    return {"dQ_stern": z7(dqs), "EQ_abstand": z7(eq / eqf - 1.0) if (eq is not None and eqf) else None,
            "omega_abstand": z7(om - of) if (om is not None and of is not None) else None}


# ---------------------------------------------------------------- Zeitentwicklung wie kf5_geburt.lauf()

def entwickeln(g, dt, kraft, nl, psi, vel, S0, fam, linie, alt_r6, n_von, n_bis, fenster, rauch=False):
    """Velocity-Verlet wie kf5_geburt.lauf() von Schritt n_von bis n_bis (globale Schrittzahl, t = Schritt * dt).
    analyse_arm bei jedem Vielfachen von T_AUS (auch bei n_von), Kontrast bei jedem Vielfachen von T_KON, Messfenster
    [t_bis - fenster, t_bis] mit fenster_start/fenster_probe/fenster_auswerten. psi, vel: (1, n, n), werden fortgeschrieben."""
    je_kon, je_aus, je_fen = (int(round(x / dt)) for x in (kg.T_KON, kg.T_AUS, kg.DT_FENSTER))
    s_fen = n_bis - int(round(fenster / dt))
    if s_fen < n_von or s_fen % je_aus != 0:
        raise SystemExit("Fensterbeginn muss im Abschnitt liegen und ein Vielfaches von T_AUS sein")
    reihe, kon_t, kon_k, kon_m = [], [], [], []
    fzs, f_info = None, None
    dauer = {"auswertung": 0.0, "fenster": 0.0, "linie": 0.0}
    n_aus = 0
    t_lauf = kg.uhr()
    F = kraft(psi)
    for schritt in range(n_von, n_bis + 1):
        if schritt > n_von:
            vel.add_(F, alpha=0.5 * dt)
            psi.add_(vel, alpha=dt)
            F = kraft(psi)
            vel.add_(F, alpha=0.5 * dt)
        t = round(schritt * dt, 6)
        if schritt % je_kon == 0:
            s = psi.real ** 2 + psi.imag ** 2
            mw = s.mean((1, 2))
            kon_t.append(t)
            kon_k.append(torch.sqrt(((s - mw.view(-1, 1, 1)) ** 2).mean((1, 2))) / mw)
            kon_m.append(s.amax((1, 2)))
        a_jetzt = schritt % je_aus == 0
        f_jetzt = schritt >= s_fen and (schritt - s_fen) % je_fen == 0
        if not (a_jetzt or f_jetzt):
            continue
        s, rho, e = kg.dichten(g, psi, vel, nl)
        if a_jetzt:
            ta = kg.uhr()
            zeile, alt_r6, tropfen = kg.analyse_arm(g, s[0], rho[0], e[0], psi[0], S0, fam, alt_r6)
            zeile["t"] = t
            zeile["Q_box"] = (rho[0].sum() * g.dA).item()
            zeile["E_box"] = (e[0].sum() * g.dA).item()
            tl = kg.uhr()
            neu = alt_r6 if alt_r6 is not None else torch.full((g.n, g.n), -1, dtype=torch.long, device=kg.DEV)
            if linie.etik is None and not linie.akten:
                linie.start(neu, t)
            else:
                linie.schritt(neu, t)
            dauer["linie"] += kg.uhr() - tl
            if schritt == s_fen:
                fzs = kg.fenster_start(tropfen)
                ids, xs = tropfen_etiketten(g, s[0], rho[0], S0)
                x_an = zeile.get("tropfen", {}).get("x", [])
                if len(xs) != len(x_an) or any(abs(u - w) > 1e-4 for u, w in zip(xs, x_an)):
                    raise RuntimeError(f"Tropfenauswahl bei t {t} nicht reproduziert: {xs} gegen {x_an}")
                f_info = {"t": t, "etiketten": ids, "wurzeln": [sorted(linie.wurzeln.get(i, set())) for i in ids],
                          "rmax_zu_ra_start": zeile.get("tropfen", {}).get("rmax_zu_ra", [])}
            reihe.append(zeile)
            n_aus += 1
            dauer["auswertung"] += kg.uhr() - ta
            if n_aus == 4 and schritt < n_bis:
                verg = kg.uhr() - t_lauf
                entw = verg - dauer["auswertung"] - dauer["fenster"] - dauer["linie"]
                rest = n_bis - schritt
                prognose = verg + entw / max(schritt - n_von, 1) * rest + (dauer["auswertung"] + dauer["linie"]) / n_aus \
                    * (rest // je_aus + 1) + 1.5 * (fenster / kg.DT_FENSTER + 1) * 0.1
                print(f"  Prognose Entwicklungsteil {prognose:.0f} s", flush=True)
                if prognose > ZEITGRENZE_S:
                    raise SystemExit(f"Abbruch vor der Zeitgrenze: Prognose {prognose:.0f} s > {ZEITGRENZE_S:.0f} s")
            if not rauch:
                z2 = zeile["schwellen"]["2"]
                print(f"  t {t:7.1f} ({kg.uhr() - t_lauf:5.0f} s): Tr {z2['N_tropfen']}/K {z2['N_komp']}"
                      + (" U" if z2["umspannt"] else ""), flush=True)
        if f_jetzt:
            tf = kg.uhr()
            if fzs is not None:
                kg.fenster_probe(g, fzs, s[0], rho[0], e[0], psi[0])
            dauer["fenster"] += kg.uhr() - tf
    dauer["entwicklung"] = kg.uhr() - t_lauf - dauer["auswertung"] - dauer["fenster"] - dauer["linie"]
    fen = kg.fenster_auswerten(fzs, round(s_fen * dt, 6), kg.DT_FENSTER, fam, g.box)
    for tr in fen["tropfen"]:
        k = tr["k"]
        tr["etikett_start"] = f_info["etiketten"][k]
        tr["wurzeln"] = f_info["wurzeln"][k]
        tr["rmax_zu_ra_start"] = f_info["rmax_zu_ra_start"][k]
        tr.update(familien_abstaende(fam, tr))
    kk = torch.stack(kon_k).cpu().flatten().tolist() if kon_k else []
    km = torch.stack(kon_m).cpu().flatten().tolist() if kon_m else []
    return {"reihe": reihe, "fenster": fen, "fenster_info": f_info, "dauer": dauer, "alt_r6": alt_r6,
            "kontrast": {"t": kon_t, "kontrast": [z7(v) for v in kk], "S_max": [z7(v) for v in km]}}


# ---------------------------------------------------------------- Vergleiche fuer K0

def nahe(a, b, rel, absol):
    if a is None or b is None:
        return a is None and b is None, 0.0
    d = abs(a - b)
    return d <= rel * abs(b) + absol, d / max(abs(b), 1e-300)


def vergleich_zeile(neu, alt, rel=2e-6, absol=1e-6):
    """K0a und K0b-Zeilen: ganzzahlige Groessen gleich, Zahlen bis auf die 7-Stellen-Rundung der Ausgabe."""
    fehler, maxrel = [], 0.0
    for f in ("2", "3"):
        a, b = neu["schwellen"][f], alt["schwellen"][f]
        for x in ("N_komp", "N_klein", "N_tropfen", "N_netz", "umspannt"):
            if a[x] != b[x]:
                fehler.append(f"Schwelle {f}: {x} {a[x]} gegen {b[x]}")
        for x in ("masken_anteil", "anteil_groesste", "anteil_tropfen"):
            ok, r = nahe(a[x], b[x], rel, absol)
            maxrel = max(maxrel, r)
            if not ok:
                fehler.append(f"Schwelle {f}: {x} {a[x]} gegen {b[x]}")
    ta, tb = neu.get("tropfen", {}), alt.get("tropfen", {})
    for x in ("x", "y", "A", "S_max", "Q_maske", "Q_roh", "Q_net", "E_net", "omega", "dQ_familie", "rmax_zu_ra"):
        la, lb = ta.get(x, []), tb.get(x, [])
        if len(la) != len(lb):
            fehler.append(f"Tropfen {x}: Anzahl {len(la)} gegen {len(lb)}")
            continue
        for i, (u, v) in enumerate(zip(la, lb)):
            ok, r = nahe(u, v, rel, absol)
            maxrel = max(maxrel, r)
            if not ok:
                fehler.append(f"Tropfen {i} {x}: {u} gegen {v}")
    return {"bestanden": not fehler, "fehler": fehler[:30], "max_rel": z7(maxrel)}


def vergleich_fenster(neu, alt, rel=1e-4):
    fehler, maxrel = [], 0.0
    for x in ("zaehlung", "urteil", "urteil_roh"):
        if neu[x] != alt[x]:
            fehler.append(f"{x}: {neu[x]} gegen {alt[x]}")
    if len(neu["tropfen"]) != len(alt["tropfen"]):
        fehler.append(f"Tropfenzahl im Fenster {len(neu['tropfen'])} gegen {len(alt['tropfen'])}")
    for a, b in zip(neu["tropfen"], alt["tropfen"]):
        for x in ("rund", "klasse", "klasse_roh", "verloren", "stoss"):
            if a[x] != b[x]:
                fehler.append(f"Tropfen {b['k']} {x}: {a[x]} gegen {b[x]}")
        for x in ("Q_net", "Q_roh", "E_ruhe_net", "E_zu_Q", "E_zu_Q_familie", "omega_rot", "omega_ruhe", "u_omega", "v",
                  "omega_inst_mittel", "S_max_mittel", "Q_schwankung", "dQ"):
            ok, r = nahe(a[x], b[x], rel, 1e-9)
            maxrel = max(maxrel, r)
            if not ok:
                fehler.append(f"Tropfen {b['k']} {x}: {a[x]} gegen {b[x]}")
    return {"bestanden": not fehler, "fehler": fehler[:30], "max_rel": z7(maxrel)}


# ---------------------------------------------------------------- Unterbefehle

def befehl_k0(args):
    start = jetzt()
    t_start = kg.uhr()
    fam = kg.Familie()
    st = lade_r6(args.stufe, args.arm)
    r6a, r6_pfad = lade_r6_json(args.stufe, args.arm)
    g, dt, arm, nl, kraft = aufbau(args.stufe, args.arm)
    if st["psi"].shape[-1] != g.n:
        raise SystemExit("Gitter passt nicht zum Zustand")
    psi = st["psi"].to(kg.DEV)
    vel = st["vel"].to(kg.DEV)
    S0 = arm["S0"]
    fenster = kg.RAUCH_FENSTER if args.rauch else kg.FENSTER
    # K0a: Schnappschuss bei 800
    s, rho, e = kg.dichten(g, psi, vel, nl)
    zeile800, _, _ = kg.analyse_arm(g, s[0], rho[0], e[0], psi[0], S0, fam, None)
    r6_800 = r6a["reihe_auswertung"][-1]
    if abs(r6_800["t"] - T_R6) > 1e-9:
        raise SystemExit("Runde-6-Zeile t = 800 fehlt")
    k0a = vergleich_zeile(zeile800, r6_800)
    # K0b: zurueck nach 800 - Fenster, dann vorwaerts mit Fenster wie Runde 6
    n800 = int(round(T_R6 / dt))
    n_back = int(round(fenster / dt))
    p, v = psi.clone(), vel.clone()
    tb = kg.uhr()
    F = kraft(p)
    for _ in range(n_back):
        v.add_(F, alpha=-0.5 * dt)
        p.add_(v, alpha=-dt)
        F = kraft(p)
        v.add_(F, alpha=-0.5 * dt)
    dauer_rueck = kg.uhr() - tb
    linie = Linie()
    erg = entwickeln(g, dt, kraft, nl, p, v, S0, fam, linie, None, n800 - n_back, n800, fenster, rauch=args.rauch)
    rueck = {"psi_max_rel": ((p - psi).abs().max() / psi.abs().max()).item(),
             "vel_max_rel": ((v - vel).abs().max() / vel.abs().max()).item()}
    dauer = {"rueckwaerts": dauer_rueck, **erg["dauer"], "gesamt": kg.uhr() - t_start}
    name = f"k0_{args.stufe}_{args.arm}" + ("_rauch" if args.rauch else "")
    ordner = os.path.join(AUS, "rauch" if args.rauch else "k0")
    os.makedirs(ordner, exist_ok=True)
    if args.rauch:
        aus = {"name": name, "start": start, "ende": jetzt(), "rauch": True, "dauer_s": dauer, "n": g.n, "dt": dt,
               "schritte": 2 * n_back, "herkunft": herkunft()}
        schreibe_json(os.path.join(ordner, name + ".json"), aus)
        print(f"RAUCH {name}: Durchlauf ok; Dauer [s] " + ", ".join(f"{x} {y:.1f}" for x, y in dauer.items())
              + f"; je Schritt vorwaerts {erg['dauer']['entwicklung'] / n_back * 1e3:.2f} ms, rueckwaerts "
              f"{dauer_rueck / n_back * 1e3:.2f} ms", flush=True)
        return
    r6_zeilen = {round(z["t"], 6): z for z in r6a["reihe_auswertung"]}
    k0b_zeilen = {f"{z['t']:g}": vergleich_zeile(z, r6_zeilen[round(z["t"], 6)]) for z in erg["reihe"]}
    k0b_fenster = vergleich_fenster(erg["fenster"], r6a["fenster"])
    eq = []
    for a, b in zip(erg["fenster"]["tropfen"], r6a["fenster"]["tropfen"]):
        eq.append({"k": b["k"], "E_zu_Q_neu": a["E_zu_Q"], "E_zu_Q_r6": b["E_zu_Q"], "klasse_neu": a["klasse"],
                   "klasse_r6": b["klasse"], "rund_neu": a["rund"], "rund_r6": b["rund"]})
    k0b_ok = (k0b_fenster["bestanden"] and all(x["bestanden"] for x in k0b_zeilen.values())
              and len(erg["fenster"]["tropfen"]) == len(r6a["fenster"]["tropfen"]))
    aus = {"name": name, "karte": "KF-5 weiter (R20)", "start": start, "ende": jetzt(), "stufe": args.stufe,
           "arm": args.arm, "dx": g.dx, "dt": dt, "n": g.n, "herkunft": herkunft(), "zustand": {
               k: st[k] for k in ("quelle", "quelle_sha256", "arme_datei", "index", "t")}, "r6_json": r6_pfad,
           "dauer_s": dauer,
           "K0a": {**k0a, "zeile_neu": zeile800},
           "K0b": {"bestanden": k0b_ok, "fenster": k0b_fenster, "zeilen": k0b_zeilen, "rueckkehr_800": rueck,
                   "EQ_klassen": eq},
           "K0_bestanden": bool(k0a["bestanden"] and k0b_ok),
           "rekonstruktion": {"reihe": erg["reihe"], "fenster": erg["fenster"], "fenster_info": erg["fenster_info"],
                              "kontrast": erg["kontrast"]},
           "linie": linie.zu_json()}
    schreibe_json(os.path.join(ordner, name + ".json"), aus)
    pt = frei_pfad(os.path.join(ordner, name + "_linie.pt"))
    torch.save({"etik": linie.etik.to(torch.int32).cpu(), "t": T_R6}, pt)
    print(f"K0 {name}: K0a {'bestanden' if k0a['bestanden'] else 'NICHT bestanden'} (max rel {k0a['max_rel']}); "
          f"K0b {'bestanden' if k0b_ok else 'NICHT bestanden'} (Fenster max rel {k0b_fenster['max_rel']}; Rueckkehr psi "
          f"{rueck['psi_max_rel']:.2e}, vel {rueck['vel_max_rel']:.2e})", flush=True)
    for f in k0a["fehler"] + k0b_fenster["fehler"]:
        print("   ", f, flush=True)
    for x in eq:
        print(f"    k {x['k']}: klasse {x['klasse_neu']} | R6 {x['klasse_r6']}; rund {x['rund_neu']} | {x['rund_r6']}; "
              f"E/Q {x['E_zu_Q_neu']} | {x['E_zu_Q_r6']}", flush=True)
    print("Dauer [s]: " + ", ".join(f"{x} {y:.1f}" for x, y in dauer.items()), flush=True)


def zw_name(stufe, arm, t):
    return os.path.join(AUS, "zwischen", f"zustand_{stufe}_{arm}_t{int(round(t))}.pt")


def befehl_weiter(args):
    start = jetzt()
    t_start = kg.uhr()
    fam = kg.Familie()
    g, dt, arm, nl, kraft = aufbau(args.stufe, args.arm)
    von, bis = float(args.von), float(args.bis)
    fenster = kg.RAUCH_FENSTER if args.rauch else kg.FENSTER
    if args.rauch:
        von, bis = T_R6, T_R6 + 20.0
    if abs(von - T_R6) < 1e-9:
        st = lade_r6(args.stufe, args.arm)
        quelle = {k: st[k] for k in ("quelle", "quelle_sha256", "arme_datei", "index", "t")}
        psi, vel = st["psi"].to(kg.DEV), st["vel"].to(kg.DEV)
        if args.rauch:
            linie, alt_r6, lin_quelle = Linie(), None, None
        else:
            kp = os.path.join(AUS, "k0", f"k0_{args.stufe}_{args.arm}")
            with open(kp + ".json") as fh:
                k0 = json.load(fh)
            if not k0["K0a"]["bestanden"]:
                raise SystemExit("K0a nicht bestanden: keine Fortsetzung (PLAN.md)")
            etik = torch.load(kp + "_linie.pt", map_location="cpu", weights_only=True)["etik"].to(torch.long).to(kg.DEV)
            linie = Linie.aus_json(etik, k0["linie"])
            alt_r6 = None           # Runde 6 hat das Etikettenbild von 790 nicht gespeichert; verknuepfung bei 800 = (0, 0)
            lin_quelle = kp + ".json"
    else:
        zp = zw_name(args.stufe, args.arm, von)
        d = torch.load(zp, map_location="cpu", weights_only=True)
        if abs(float(d["t"]) - von) > 1e-9 or d["stufe"] != args.stufe or d["arm"] != args.arm:
            raise SystemExit(f"Zwischenspeicher passt nicht: {zp}")
        quelle = {"quelle": zp, "quelle_sha256": sha(zp), "t": float(d["t"])}
        psi, vel = d["psi"].to(kg.DEV), d["vel"].to(kg.DEV)
        with open(zp[:-3] + "_linie.json") as fh:
            lj = json.load(fh)
        etik = d["etik"].to(torch.long).to(kg.DEV)
        linie = Linie.aus_json(etik, lj)
        alt_r6 = torch.where(etik >= 0, etik, torch.full_like(etik, -1))
        lin_quelle = zp[:-3] + "_linie.json"
    n_von, n_bis = int(round(von / dt)), int(round(bis / dt))
    print(f"KF-5 weiter {args.stufe} {args.arm}: {von:g} -> {bis:g}, Fenster {fenster:g}, n {g.n}, {n_bis - n_von} "
          f"Schritte, {kg.geraet_name()}, Start {start}", flush=True)
    erg = entwickeln(g, dt, kraft, nl, psi, vel, arm["S0"], fam, linie, alt_r6, n_von, n_bis, fenster, rauch=args.rauch)
    dauer = {**erg["dauer"], "gesamt": kg.uhr() - t_start}
    name = f"weiter_{args.stufe}_{args.arm}_{int(round(von))}-{int(round(bis))}" + ("_rauch" if args.rauch else "")
    if args.rauch:
        ordner = os.path.join(AUS, "rauch")
        os.makedirs(ordner, exist_ok=True)
        aus = {"name": name, "start": start, "ende": jetzt(), "rauch": True, "dauer_s": dauer, "n": g.n, "dt": dt,
               "schritte": n_bis - n_von, "n_auswertungen": len(erg["reihe"]), "herkunft": herkunft()}
        schreibe_json(os.path.join(ordner, name + ".json"), aus)
        print(f"RAUCH {name}: Durchlauf ok; Dauer [s] " + ", ".join(f"{x} {y:.1f}" for x, y in dauer.items())
              + f"; je Schritt {erg['dauer']['entwicklung'] / (n_bis - n_von) * 1e3:.2f} ms; je Auswertung "
              f"{(erg['dauer']['auswertung'] + erg['dauer']['linie']) / len(erg['reihe']):.2f} s", flush=True)
        return
    os.makedirs(os.path.join(AUS, "zwischen"), exist_ok=True)
    os.makedirs(os.path.join(AUS, "abschnitte"), exist_ok=True)
    zp = frei_pfad(zw_name(args.stufe, args.arm, bis))
    s = (psi.real ** 2 + psi.imag ** 2)[0]
    st_bild = max(1, int(round(0.5 / g.dx)))
    torch.save({"t": bis, "stufe": args.stufe, "arm": args.arm, "box": g.box, "dx": g.dx, "dt": dt,
                "psi": psi.cpu(), "vel": vel.cpu(), "etik": linie.etik.to(torch.int32).cpu(),
                "bild_S_dx0_5": s[::st_bild, ::st_bild].to(torch.float32).cpu()}, zp)
    schreibe_json(zp[:-3] + "_linie.json", linie.zu_json())
    aus = {"name": name, "karte": "KF-5 weiter (R20)", "start": start, "ende": jetzt(), "stufe": args.stufe,
           "arm": args.arm, "von": von, "bis": bis, "fenster": fenster, "dx": g.dx, "dt": dt, "n": g.n,
           "herkunft": herkunft(), "quelle": quelle, "linie_quelle": lin_quelle, "dauer_s": dauer,
           "zwischenspeicher": zp, "zwischenspeicher_sha256": sha(zp), "reihe_auswertung": erg["reihe"],
           "fenster_ergebnis": erg["fenster"], "fenster_info": erg["fenster_info"], "kontrast": erg["kontrast"],
           "linie": linie.zu_json()}
    schreibe_json(os.path.join(AUS, "abschnitte", name + ".json"), aus)
    fen = erg["fenster"]
    print(f"Fenster [{bis - fenster:g}, {bis:g}]: {json.dumps(fen['zaehlung'])}; Urteil {fen['urteil']}", flush=True)
    for tr in fen["tropfen"]:
        print(f"    k {tr['k']:2d} | Q {kg.fz(tr['Q_net'])} | E {kg.fz(tr['E_ruhe_net'])} | E/Q {kg.fz(tr['E_zu_Q'], '.4f')}"
              f" fam {kg.fz(tr['E_zu_Q_familie'], '.4f')} | omega {kg.fz(tr['omega_ruhe'], '.5f')} +- "
              f"{kg.fz(tr['u_omega'], '.1e')} fam(Q) {kg.fz(tr['omega_familie_bei_Q'], '.5f')} | rmax/ra "
              f"{kg.fz(tr['rmax_zu_ra_start'], '.3f')} | dQ* {kg.fz(tr['dQ_stern'], '+.3f')} | {tr['klasse']} | "
              f"Wurzeln {','.join(tr['wurzeln'])}", flush=True)
    print("Dauer [s]: " + ", ".join(f"{x} {y:.1f}" for x, y in dauer.items()), flush=True)


# ---------------------------------------------------------------- Zusammenfassung und Z0 bis Z4

def befehl_zusammen(args):
    fam = kg.Familie()
    stufen = [x for x in args.stufen.split(",") if x]
    arm = args.arm
    erg = {"zeit": jetzt(), "arm": arm, "stufen": {}, "herkunft": herkunft()}
    L = [f"KF-5 weiter, Zusammenfassung {arm} ({erg['zeit']})"]
    for st in stufen:
        with open(os.path.join(AUS, "k0", f"k0_{st}_{arm}.json")) as fh:
            k0 = json.load(fh)
        r6a, _ = lade_r6_json(st, arm)
        abschn = {}
        for von, bis in ABSCHNITTE:
            p = os.path.join(AUS, "abschnitte", f"weiter_{st}_{arm}_{int(von)}-{int(bis)}.json")
            if os.path.exists(p):
                with open(p) as fh:
                    abschn[bis] = json.load(fh)
        akten = abschn[max(abschn)]["linie"]["akten"] if abschn else k0["linie"]["akten"]
        t_akten = max(abschn) if abschn else T_R6
        zeilen = []
        r6_fen = r6a["fenster"]["tropfen"]
        rek_fen = k0["rekonstruktion"]["fenster"]["tropfen"]
        r6_760 = {round(z["t"], 6): z for z in r6a["reihe_auswertung"]}[T_R6 - kg.FENSTER]
        for i, b in enumerate(r6_fen):
            wurzeln = rek_fen[i]["wurzeln"] if i < len(rek_fen) else []
            r = wurzeln[0] if len(wurzeln) == 1 else None
            werte = {"800": {"Q_net": b["Q_net"], "E_ruhe_net": b["E_ruhe_net"], "E_zu_Q": b["E_zu_Q"],
                             "E_zu_Q_familie": b["E_zu_Q_familie"], "omega_ruhe": b["omega_ruhe"],
                             "u_omega": b["u_omega"], "omega_familie_bei_Q": b["omega_familie_bei_Q"],
                             "rmax_zu_ra_start": r6_760["tropfen"]["rmax_zu_ra"][i], "rund": b["rund"],
                             "klasse": b["klasse"], "v": b["v"], **familien_abstaende(fam, b), "status": "Runde 6"}}
            for te in T_EVAL:
                a = abschn.get(te)
                if a is None:
                    werte[f"{te:g}"] = {"status": "nicht gerechnet"}
                    continue
                rein = [tr for tr in a["fenster_ergebnis"]["tropfen"] if r is not None and tr["wurzeln"] == [r]]
                misch = [tr for tr in a["fenster_ergebnis"]["tropfen"] if r is not None and r in tr["wurzeln"]
                         and tr["wurzeln"] != [r]]
                if rein:
                    tr = max(rein, key=lambda x: x["Q_net"] or 0.0)
                    status = "rein" + (f", geteilt ({len(rein)} Tropfen)" if len(rein) > 1 else "")
                elif misch:
                    tr = max(misch, key=lambda x: x["Q_net"] or 0.0)
                    status = "verschmolzen mit " + ",".join(w for w in tr["wurzeln"] if w != r)
                else:
                    werte[f"{te:g}"] = {"status": "kein Tropfen im Fenster"}
                    continue
                werte[f"{te:g}"] = {x: tr.get(x) for x in ("k", "Q_net", "E_ruhe_net", "E_zu_Q", "E_zu_Q_familie",
                                                            "omega_ruhe", "u_omega", "omega_familie_bei_Q",
                                                            "rmax_zu_ra_start", "rund", "klasse", "v", "dQ_stern",
                                                            "EQ_abstand", "omega_abstand", "dQ", "stoss")}
                werte[f"{te:g}"]["status"] = status
            akte = akten.get(r) if r else None
            zeilen.append({"r6_k": b["k"], "wurzel": r, "akte": akte, "werte": werte})
        neue = {}
        for te in T_EVAL:
            a = abschn.get(te)
            if a is None:
                continue
            bekannt = {z["wurzel"] for z in zeilen if z["wurzel"]}
            neue[f"{te:g}"] = [{x: tr.get(x) for x in ("k", "Q_net", "E_zu_Q", "omega_ruhe", "rmax_zu_ra_start", "rund",
                                                       "klasse", "dQ_stern", "wurzeln")}
                               for tr in a["fenster_ergebnis"]["tropfen"] if not (set(tr["wurzeln"]) & bekannt)]
        ende = {}
        for te in T_EVAL:
            a = abschn.get(te)
            if a is None:
                continue
            fen = a["fenster_ergebnis"]
            z_end = a["reihe_auswertung"][-1]
            ende[f"{te:g}"] = {"N_fenster": len(fen["tropfen"]), "zaehlung": fen["zaehlung"], "urteil": fen["urteil"],
                               "N_rund": sum(1 for tr in fen["tropfen"] if tr["rund"]),
                               "N_auf": sum(1 for tr in fen["tropfen"] if tr["klasse"] == "auf"),
                               "N_tropfen_2": z_end["schwellen"]["2"]["N_tropfen"],
                               "N_tropfen_3": z_end["schwellen"]["3"]["N_tropfen"],
                               "N_komp_2": z_end["schwellen"]["2"]["N_komp"],
                               "umspannt_2": z_end["schwellen"]["2"]["umspannt"],
                               "klassen_nach_Q": [tr["klasse"] for tr in sorted(fen["tropfen"],
                                                                                 key=lambda x: -(x["Q_net"] or 0.0))],
                               "verschmelzungen_maske": sum(z["verschmelzungen"] for z in a["reihe_auswertung"][1:]),
                               "teilungen_maske": sum(z["teilungen"] for z in a["reihe_auswertung"][1:]),
                               "drift_Q_abschnitt": z7(max(abs(z["Q_box"] / a["reihe_auswertung"][0]["Q_box"] - 1.0)
                                                          for z in a["reihe_auswertung"])),
                               "drift_E_abschnitt": z7(max(abs(z["E_box"] / a["reihe_auswertung"][0]["E_box"] - 1.0)
                                                          for z in a["reihe_auswertung"]))}
        erg["stufen"][st] = {"K0": {"K0a": k0["K0a"]["bestanden"], "K0b": k0["K0b"]["bestanden"],
                                    "K0": k0["K0_bestanden"], "rueckkehr": k0["K0b"]["rueckkehr_800"]},
                             "tropfen": zeilen, "neue_tropfen": neue, "ende": ende, "akten_bis": t_akten}
    # Z0 bis Z4 (Regeln PLAN.md, Abschnitt 5)
    S = erg["stufen"]
    z = {}
    z["Z0"] = "eingetroffen" if all(S[st]["K0"]["K0"] for st in S) else "nicht eingetroffen"
    e20 = {st: S[st]["ende"].get("2000") for st in S}
    if all(e20.values()) and len(e20) == 2:
        z["Z1"] = "eingetroffen" if all(e["N_rund"] >= 2 for e in e20.values()) else "nicht eingetroffen"
        z["Z2"] = "eingetroffen" if all(e["N_auf"] >= 1 for e in e20.values()) else "nicht eingetroffen"
        a_, b_ = e20.get("grob"), e20.get("fein")
        z["Z4"] = ("eingetroffen" if (a_ and b_ and a_["N_fenster"] == b_["N_fenster"]
                                      and a_["klassen_nach_Q"] == b_["klassen_nach_Q"]) else "nicht eingetroffen")
    else:
        z["Z1"] = z["Z2"] = z["Z4"] = "offen (T = 2000 nicht auf beiden Gittern)"
    z3 = []
    for st in S:
        for zl in S[st]["tropfen"]:
            ak = zl["akte"]
            w8, w20 = zl["werte"]["800"], zl["werte"].get("2000", {})
            if ak is None:
                fall = "offen: keine eindeutige Wurzel"
            elif ak["verschmolzen"] is not None:
                fall = f"ausgeschlossen: verschmolzen bei t {ak['verschmolzen']:g}"
            elif ak["erloschen"] is not None:
                fall = f"ausgeschlossen: erloschen bei t {ak['erloschen']:g}"
            elif not str(w20.get("status", "")).startswith("rein"):
                fall = f"offen: {w20.get('status', 'kein Wert')}"
            elif w8.get("dQ_stern") is None or w20.get("dQ_stern") is None:
                fall = "offen: dQ* nicht definiert (omega ausserhalb der Tabelle)"
            else:
                fall = "kleiner" if abs(w20["dQ_stern"]) < abs(w8["dQ_stern"]) else "nicht kleiner"
            z3.append({"stufe": st, "r6_k": zl["r6_k"], "fall": fall, "dQ_stern_800": w8.get("dQ_stern"),
                       "dQ_stern_2000": w20.get("dQ_stern"), "EQ_abstand_800": w8.get("EQ_abstand"),
                       "EQ_abstand_2000": w20.get("EQ_abstand"), "omega_abstand_800": w8.get("omega_abstand"),
                       "omega_abstand_2000": w20.get("omega_abstand")})
    pop = [x for x in z3 if not x["fall"].startswith("ausgeschlossen")]
    if any(x["fall"] == "nicht kleiner" for x in pop):
        z["Z3"] = "nicht eingetroffen"
    elif pop and all(x["fall"] == "kleiner" for x in pop):
        z["Z3"] = "eingetroffen"
    else:
        z["Z3"] = "offen"
    z["Z3_einzeln"] = z3
    if z["Z3"] == "nicht eingetroffen":
        bed = "Z3 nicht eingetroffen: auf dieser Zeitskala keine Annaeherung; KF-5 verwerfen (Karte)"
    elif z.get("Z2") == "eingetroffen" and z["Z3"] == "eingetroffen":
        bed = "Z2 und Z3 eingetroffen: Tropfen laufen auf die Familie zu; M1 in 2D bildungsfaehig (Stufe 5) [H, im Modell]"
    else:
        bed = "sonst: parken mit Grund (Karte)"
    z["bedeutung"] = bed
    erg["vorhersagen"] = z
    pfad = os.path.join(AUS, f"zusammen_{arm}{args.zusatz}.json")
    if os.path.exists(pfad):
        raise SystemExit(f"{pfad} existiert schon")
    schreibe_json(pfad, erg)
    for st in S:
        L.append(f"== {st}: K0 {S[st]['K0']}")
        for zl in S[st]["tropfen"]:
            L.append(f"  R6-Tropfen k {zl['r6_k']} (Wurzel {zl['wurzel']}), Akte bis {S[st]['akten_bis']:g}: "
                     f"{json.dumps(zl['akte'])}")
            for te, w in zl["werte"].items():
                if "Q_net" not in w:
                    L.append(f"    T {te}: {w['status']}")
                    continue
                L.append(f"    T {te}: Q {kg.fz(w['Q_net'])} | E {kg.fz(w['E_ruhe_net'])} | E/Q {kg.fz(w['E_zu_Q'], '.4f')}"
                         f" (fam {kg.fz(w['E_zu_Q_familie'], '.4f')}) | omega {kg.fz(w['omega_ruhe'], '.5f')} +- "
                         f"{kg.fz(w['u_omega'], '.1e')} (fam(Q) {kg.fz(w['omega_familie_bei_Q'], '.5f')}) | rmax/ra "
                         f"{kg.fz(w['rmax_zu_ra_start'], '.3f')} | {w['klasse']} | dQ* {kg.fz(w['dQ_stern'], '+.3f')} | "
                         f"E/Q-Abst {kg.fz(w['EQ_abstand'], '+.4f')} | {w['status']}")
        for te, lst in S[st]["neue_tropfen"].items():
            for tr in lst:
                L.append(f"  neu T {te}: Q {kg.fz(tr['Q_net'])} | E/Q {kg.fz(tr['E_zu_Q'], '.4f')} | omega "
                         f"{kg.fz(tr['omega_ruhe'], '.5f')} | rmax/ra {kg.fz(tr['rmax_zu_ra_start'], '.3f')} | "
                         f"{tr['klasse']} | dQ* {kg.fz(tr['dQ_stern'], '+.3f')} | Wurzeln {','.join(tr['wurzeln'])}")
        for te, e in S[st]["ende"].items():
            L.append(f"  Ende T {te}: {json.dumps(e)}")
    for x in ("Z0", "Z1", "Z2", "Z3", "Z4"):
        L.append(f"{x}: {z[x]}")
    for x in z3:
        L.append(f"  Z3 {x['stufe']} k {x['r6_k']}: {x['fall']} (dQ* {x['dQ_stern_800']} -> {x['dQ_stern_2000']}; "
                 f"E/Q-Abst {x['EQ_abstand_800']} -> {x['EQ_abstand_2000']})")
    L.append(f"Bedeutung: {bed}")
    with open(frei_pfad(os.path.join(AUS, f"zusammen_{arm}{args.zusatz}.txt")), "w") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L), flush=True)


def main():
    ap = argparse.ArgumentParser(description="KF-5 weiter (Runde 20, v3)")
    ap.add_argument("befehl", choices=["k0", "weiter", "zusammen"])
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda")
    ap.add_argument("--stufe", choices=list(kg.STUFEN), default="grob")
    ap.add_argument("--stufen", default="grob,fein")
    ap.add_argument("--arm", default="s03")
    ap.add_argument("--von", type=float, default=T_R6)
    ap.add_argument("--bis", type=float, default=1200.0)
    ap.add_argument("--rauch", action="store_true")
    ap.add_argument("--zusatz", default="", help="Namenszusatz fuer zusammen (nichts ueberschreiben)")
    args = ap.parse_args()
    if args.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("--geraet cuda, aber kein CUDA-Geraet sichtbar: Abbruch (kein stiller CPU-Ausweg).")
        kg.DEV = torch.device("cuda")
    else:
        if args.befehl != "zusammen":
            raise SystemExit("Rechnungen nur auf der GPU (PLAN.md)")
        kg.DEV = torch.device("cpu")
        torch.set_num_threads(1)
    if args.befehl != "zusammen" and args.arm not in ("s03", "s01"):
        raise SystemExit("Arm nur s03 oder s01")
    if args.befehl == "weiter" and not args.rauch:
        if (args.von, args.bis) not in ABSCHNITTE:
            raise SystemExit(f"Abschnitt nur aus {ABSCHNITTE}")
    print(f"kf5_weiter {args.befehl}: Start {jetzt()}", flush=True)
    {"k0": befehl_k0, "weiter": befehl_weiter, "zusammen": befehl_zusammen}[args.befehl](args)
    print(f"kf5_weiter {args.befehl}: Ende {jetzt()}", flush=True)


if __name__ == "__main__":
    main()
