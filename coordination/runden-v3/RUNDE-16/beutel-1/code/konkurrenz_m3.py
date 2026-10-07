#!/usr/bin/env python3
# Nachtrag N3, Wiederholung fuer M3: Gradientenfluss mit dt = 0.01 statt 0.05.
# Grund: Bei Q = 1e4 ist S(0) ~ 25, U_gg ~ 4S ~ 100; der explizite chi-Schritt ist bei dt = 0.05 instabil
# (dt * U_gg > 2), Start A lief in Lauf 2 auf NaN. Sonst unveraendert (beutel_v2.konkurrenz).
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import beutel_v2 as b

b.flow.__defaults__ = (0.01, 400.0, 1e-6)  # dt, tmax (konkurrenz uebergibt tmax = 600), tol
M = b.Model("M3")
res = b.konkurrenz(M, 0.04, [1e4, 1000.0])
with open(sys.argv[1], "w") as fh:
    json.dump(res, fh, indent=1)
