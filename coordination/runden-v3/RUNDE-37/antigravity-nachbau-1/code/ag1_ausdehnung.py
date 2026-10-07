#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ANTIGRAVITY-NACHBAU-1, AG1 Nachtrag: Trennt Linien/Flaechen von quadratischen Punktknoten.
D aus Trefferzahlen mit tau ~ h ist fuer quadratische Punkte 1,5 und damit nicht trennscharf. Hier zusaetzlich:
  - Ausdehnung: Anteil der Zonenbreite, den die Treffermenge je Achse belegt (Linie/Flaeche: bleibt; Punkt: schrumpft)
  - smin auf versetztem Gitter bei N = 24, 48, 96 laengs der Klassen (Linie: smin ~ 0 schnell; Punkt: ~ h bzw. h^2)
  - schlichter Diamant (alle +1) als Bezugsklasse (bekannt: Knotenlinien X-W)
"""
import json, sys, itertools
import numpy as np
sys.path.insert(0, '/home/fmh/fmhc-physics-remote/antigravity-nachbau-1/code')
import ag_bloch as B  # noqa: E402

seite = np.pi / 2
klassen = {}
for bits in itertools.product((1, -1), repeat=9):
    sig = B.muster(bits)
    rep = min(B.eich_fix(sig * (B.windung(0) if wx else 1) * (B.windung(1) if wy else 1) * (B.windung(2) if wz else 1))
              for wx in (0, 1) for wy in (0, 1) for wz in (0, 1))
    klassen.setdefault(rep, []).append(bits)
plain_rep = min(B.eich_fix(np.ones(16, int) * (B.windung(0) if wx else 1) * (B.windung(1) if wy else 1) *
                           (B.windung(2) if wz else 1)) for wx in (0, 1) for wy in (0, 1) for wz in (0, 1))
res = []
for rep in sorted(klassen):
    sig = B.muster(rep)
    r = {'rep': [int(x) for x in rep], 'schlicht': rep == plain_rep, 'ausdehnung': {}, 'treffer': {}, 'smin': {}}
    for N in (24, 48, 96):
        K = B.kgitter(N, seite)
        s = B.smin_zelle(sig, K)
        m = (s < 3.0 * seite / N).reshape(N, N, N)
        r['treffer'][N] = int(m.sum())
        r['smin'][N] = float(s.min())
        if m.any():
            r['ausdehnung'][N] = [float(np.any(m, axis=tuple(a for a in range(3) if a != ax)).mean()) for ax in range(3)]
    res.append(r)
json.dump({'klassen': res, 'plain_rep': list(plain_rep)}, open(sys.argv[1], 'w'), indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
print('fertig', flush=True)
