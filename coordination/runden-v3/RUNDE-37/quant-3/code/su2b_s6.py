#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-3 S6: Aufruf von su2b.py (unveraendert) mit expandable_segments gegen Speicherfragmentierung (GPU wird mit Fremddiensten geteilt).
Gleiche Argumente wie su2b.py."""
import os
os.environ.setdefault('PYTORCH_CUDA_ALLOC_CONF', 'expandable_segments:True')
import runpy
import sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
runpy.run_path(os.path.join(HIER, 'su2b.py'), run_name='__main__')
