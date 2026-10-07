#!/usr/bin/env python3
"""Abschluss: analyse_d1b.py und plots.py in einem Aufruf. Aufruf: python abschluss.py <aus> <abb>"""
import sys, runpy, os, traceback
hier = os.path.dirname(os.path.abspath(__file__))
aus, abb = sys.argv[1], sys.argv[2]
for skript, argv in (("analyse_d1b.py", [aus]), ("plots.py", [aus, abb])):
    sys.argv = [skript] + argv
    try:
        runpy.run_path(os.path.join(hier, skript), run_name="__main__")
    except Exception:
        traceback.print_exc()
