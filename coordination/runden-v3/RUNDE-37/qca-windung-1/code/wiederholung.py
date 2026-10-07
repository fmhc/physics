#!/usr/bin/env python3
# QCA-WINDUNG-1 (Runde 41), Stufe B: wiederholt die eingefrorene Suche aus QCA-BCC-RUECK-1 mit denselben Saaten.
# qca_rueck.py liegt als unveraenderte Kopie daneben (sha256 a42239a2... wie RUECK-1/EINGEFROREN-SHA256.txt).
# Einziger Zusatz (PLAN.md Abschnitt 4): rueck_pruefung(A, s, rng) wird umhuellt und merkt sich A je Treffer;
# fall(...) wird umhuellt und haengt die gemerkten A als "A_zusatz" (Format cplx wie "repr") an die Treffer.
# Beide Huellen rufen die Originalfunktion mit denselben Argumenten auf; Zufallszahlen und Rechenweg bleiben gleich.
# Argumente wie qca_rueck.py (--teil 8 --modus haupt --formen ... --varianten ... --faelle ... --starts ... --maxit ...).
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import qca_rueck as Q  # noqa: E402

_rueck_orig = Q.rueck_pruefung
_fall_orig = Q.fall
_gemerkt = []


def rueck_mit_merken(A, s, rng):
    _gemerkt.append(np.array(A, copy=True))
    return _rueck_orig(A, s, rng)


def fall_mit_zusatz(*args, **kwargs):
    _gemerkt.clear()
    st = _fall_orig(*args, **kwargs)
    if len(_gemerkt) != len(st["hits"]):
        raise RuntimeError(f"gemerkte A ({len(_gemerkt)}) ungleich Treffer ({len(st['hits'])})")
    for h, A in zip(st["hits"], _gemerkt):
        h["A_zusatz"] = Q.cplx(A)
    return st


Q.rueck_pruefung = rueck_mit_merken
Q.fall = fall_mit_zusatz

if __name__ == "__main__":
    sys.exit(Q.main())
