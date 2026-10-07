#!/bin/bash
# ZUS-10 Pruefung, Kette A (Spur cpu6): Idee 1 (ueberlapp fein), Idee 3 (bruecke l = 1, zwei Teile), Idee 4 (pole l = 2, Teile a, b).
# Aufruf auf der .69: cd /home/fmh/fmhc-physics-remote/runde9-zus10 && nohup bash kette-zus10-a.sh > KETTE-A.log 2>&1 &
# Kein Dienst, kein Timer: einfache Folge von kleintest.sh-Aufrufen (je hoechstens 10 min).
cd /home/fmh/fmhc-physics-remote/runde9-zus10 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
S=cpu6
echo "Kette A2 Start $(date --iso-8601=seconds)"
bash $K $S z1ub gfbic.py ueberlapp --xmin 0.5625 --xmax 0.580 --dx 0.0025 --hp 0.02 --g 0.2 --out aus-ueberlapp-fein-b > LAUF-z1ub.log 2>&1
bash $K $S z3ba bic2.py bruecke --geraet cpu --omega2 0.7 --l 1 --start 1.7777169-1.328e-5j --dims 1,1.25,1.5,1.75,2,2.1,2.2,2.3 --h 0.02 --budget 540 --out aus-bruecke-l1-070-a > LAUF-z3ba.log 2>&1
# Teil b startet am letzten Punkt der Spur aus Teil a
J=aus-bruecke-l1-070-a/bruecke.json
DL=$(jq -r '.ergebnisse["0.7_l1"] | last | .dim' "$J")
ST=$(jq -r '.ergebnisse["0.7_l1"] | last | .rho | "\(.[0])\(if .[1] < 0 then "" else "+" end)\(.[1])j"' "$J")
DIMS=$(seq -s, "$DL" 0.1 3.0)
echo "Teil b: Start dim $DL, rho $ST, dims $DIMS ($(date --iso-8601=seconds))"
bash $K $S z3bb bic2.py bruecke --geraet cpu --omega2 0.7 --l 1 --start "$ST" --dims "$DIMS" --h 0.02 --budget 540 --out aus-bruecke-l1-070-b > LAUF-z3bb.log 2>&1
bash $K $S z4pa bic2.py pole --geraet cpu --l 2 --omega2 0.64,0.67,0.70 --h 0.02 --bereich alles --out aus-pole-l2-rayl-a > LAUF-z4pa.log 2>&1
bash $K $S z4pb bic2.py pole --geraet cpu --l 2 --omega2 0.73,0.76 --h 0.02 --bereich alles --out aus-pole-l2-rayl-b > LAUF-z4pb.log 2>&1
echo "Kette A2 fertig $(date --iso-8601=seconds)"
