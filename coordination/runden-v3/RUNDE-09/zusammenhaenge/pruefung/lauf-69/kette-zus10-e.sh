#!/bin/bash
# ZUS-10 Pruefung, Kette E (Spur cpu6), Ergaenzungen nach Plan (optional): Idee 4 fehlender Punkt um 0,70 (0,69 und 0,71),
# Idee 9 Gegenprobe delta -> -delta (-0,05). Explizite Listen, LC_ALL=C.
export LC_ALL=C
cd /home/fmh/fmhc-physics-remote/runde9-zus10 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
S=cpu6
echo "Kette E Start $(date --iso-8601=seconds)"
bash $K $S z4pe bic2.py pole --geraet cpu --l 2 --omega2 0.69,0.71 --h 0.02 --bereich alles --out aus-pole-l2-rayl-e > LAUF-z4pe.log 2>&1
echo "z4pe rc=$? $(date --iso-8601=seconds)"
bash $K $S z9dm005 gfbic_delta.py spektrum --stellen P1 --g 0.2 --delta-m2 -0.05 --out aus-sp-P1-dm005 > LAUF-z9dm005.log 2>&1
echo "z9dm005 rc=$? $(date --iso-8601=seconds)"
echo "Kette E fertig $(date --iso-8601=seconds)"
