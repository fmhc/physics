#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NETZ-DYN-1: Herkunft der Superpunkte im letzten Zwischenstand (Startecke des V-Netzes oder durch Zuege entstanden)."""
import os, pickle, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import netzdyn  # noqa: E402
import __main__  # noqa: E402
__main__.Netz = netzdyn.Netz   # Zwischenstaende wurden aus netzdyn.py als __main__ gespeichert
__main__.Mess = netzdyn.Mess

for name in sys.argv[1:]:
    with open(name, 'rb') as f:
        net = pickle.load(f)
    g = net.grade()
    m = sum(g.values()) / len(g)
    sp = [v for v, x in g.items() if x > 5 * m]
    n_start = net.info.get('ecken_schicht', 0) * net.T if net.info.get('start') == 'V' else 0
    alt = [v for v in sp if v < n_start]
    top = sorted(g.items(), key=lambda kv: -kv[1])[:8]
    print('%s: N4=%d N0=%d Grad mittel=%.2f max=%d Schwelle=%.1f Superpunkte=%d davon Startecken=%d (Startecken-Ids < %d); '
          'hoechste Grade (Ecke, Grad, Startecke): %s' % (
              os.path.basename(name), len(net.slist), len(g), m, max(g.values()), 5 * m, len(sp), len(alt), n_start,
              [(v, x, v < n_start) for v, x in top]), flush=True)
