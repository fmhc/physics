#!/bin/bash
# GLAS-STRAHLUNG-1 Rauchtest 2 (vor dem Einfrieren): Absturzprobe der geaenderten Auswertung auf den Rauchdateien von
# Rauchtest 1. Gelesen werden nur Rueckgabewert, Laufzeit und Schluessel.
set -u
cd /home/fmh/fmhc-physics-remote/glas-strahlung-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
bash $K cpu gs-r6 code-r2/gs.py aus --v rauch/r1-v.json --ein rauch/r2-N128-s901.json rauch/r2-N128-s902.json rauch/r3-N512-s901.json rauch/r4-N256-s901.json --out rauch/r6.json --bild rauch/r6.png > rauch/r6.log 2>&1; echo "r6 rc=$? $(date -u +%H:%M:%S)"
