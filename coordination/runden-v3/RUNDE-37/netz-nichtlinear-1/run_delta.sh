#!/bin/bash
SPUREN=(cpu2 cpu3 cpu4)
SI=0
for netz in glas-N128-s4 glas-N128-s2; do
  for arm in P R; do
    for delta in 1e-3 1e-2 1e-1; do
      spur=${SPUREN[$SI]}
      echo "Starte $netz arm $arm delta $delta auf $spur"
      # Extrahiere s2/s4
      suffix=${netz##*-}
      ssh fmh@192.168.178.69 "cd /home/fmh/fmhc-physics-remote/netz-nichtlinear-1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh $spur g1p-${suffix}-${arm}-d${delta} code/nn_delta.py lauf --netz $netz --arm b --lesart $arm --delta $delta --out lauf/g1p-${suffix}-${arm}-d${delta}" &
      sleep 1
      SI=$(( (SI + 1) % 3 ))
      if [ $SI -eq 0 ]; then
        wait
      fi
    done
  done
done
wait
echo "Alle fertig."
