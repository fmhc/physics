#!/bin/bash
# ZUS-10 Pruefung, Kette B (Spur cpu2, wartet am Lock hinter den laufenden Auftraegen): Idee 8 (Keimtabelle, Raster
# S0 = 0,95 / 1,05 / 1,2), Idee 4 (pole l = 2 Teil c, l = 3), Idee 1 (feineres Raster als Kontrolle).
# Aufruf auf der .69: cd /home/fmh/fmhc-physics-remote/runde9-zus10 && nohup bash kette-zus10-b.sh > KETTE-B.log 2>&1 &
cd /home/fmh/fmhc-physics-remote/runde9-zus10 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
S=cpu2
echo "Kette B Start $(date --iso-8601=seconds)"
bash $K $S z8kv r5f.py kavitation --geraet cpu --nur-vorhersage --teil raster --s0 0.68,0.70,0.72,0.75,0.80,0.85,0.90,0.95,0.98,0.99,1.05,1.2 --out aus-kav-vorhersage > LAUF-z8kv.log 2>&1
bash $K $S z8ka r5f.py kavitation --geraet cpu --teil raster --s0 0.95,1.05,1.2 --stufe beide --T 600 --out aus-kav-raster-hoch > LAUF-z8ka.log 2>&1
bash $K $S z4pc bic2.py pole --geraet cpu --l 2 --omega2 0.80,0.84,0.88 --h 0.02 --bereich resonanz --out aus-pole-l2-rayl-c > LAUF-z4pc.log 2>&1
bash $K $S z4pd bic2.py pole --geraet cpu --l 3 --omega2 0.60,0.63,0.66 --h 0.02 --bereich alles --out aus-pole-l3-rayl > LAUF-z4pd.log 2>&1
bash $K $S z1uc gfbic.py ueberlapp --xmin 0.548 --xmax 0.577 --dx 0.001 --hp 0.02 --g 0.2 --out aus-ueberlapp-fein-c > LAUF-z1uc.log 2>&1
echo "Kette B fertig $(date --iso-8601=seconds)"
