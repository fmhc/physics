#!/bin/bash
# ZUS-10 Pruefung, Kette D2: Idee 7, t5k_zus7.py (Fassung 2: eigene Zeitmessung ohne CUDA-Sync auf der CPU; das
# Fremdmodul tests1d_r3.py bleibt unveraendert). Erst Rauchtest auf cpu6 (CPU, T = 60, grob), bei rc = 0 der Hauptlauf
# auf p4000a (wartet am Lock; hoechstens 10 min Laufzeit).
export LC_ALL=C
cd /home/fmh/fmhc-physics-remote/runde9-zus10 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
echo "Kette D2 Start $(date --iso-8601=seconds)"
bash $K cpu6 z7rauch2 t5k_zus7.py --geraet cpu --kurz --d 4,8 --d-theta 8 --out /home/fmh/fmhc-physics-remote/runde9-zus10/aus-t5k-zus7-rauch2 > LAUF-z7rauch2.log 2>&1
RC=$?
echo "Rauchtest rc=$RC $(date --iso-8601=seconds)"
if [ "$RC" = "0" ]; then
  bash $K p4000a z7gpu t5k_zus7.py --geraet cuda --d 4,6,8 --d-theta 8 --T 3000 --out /home/fmh/fmhc-physics-remote/runde9-zus10/aus-t5k-zus7 > LAUF-z7gpu.log 2>&1
  echo "GPU-Lauf rc=$? $(date --iso-8601=seconds)"
fi
echo "Kette D2 fertig $(date --iso-8601=seconds)"
