#!/bin/bash
# V-1-PRAEZISION, Kette B (Spur cpu4). Aufruf auf der .69 in /home/fmh/fmhc-physics-remote/runde37-v1p.
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
lauf() { # name spur args...
  local n=$1; local sp=$2; shift 2
  bash $K $sp v1p-$n code/v1p.py "$@" > lauf/$n.log 2>&1
}
lauf K_G_m1e-2 cpu4 -0.01  133 64 3.2 70 karte 1.7734911003052063 lauf/K_G_m1e-2.json 5e-8
lauf K_G_m7e-3 cpu4 -0.007 133 64 3.2 70 karte 1.7734795760905477 lauf/K_G_m7e-3.json 5e-8
lauf K_G_m5e-3 cpu4 -0.005 133 64 3.2 70 karte 1.77347194781 lauf/K_G_m5e-3.json 5e-8
lauf K_G_m4e-3 cpu4 -0.004 133 64 3.2 70 karte 1.77346815133 lauf/K_G_m4e-3.json 5e-8
lauf K_G_m3e-3 cpu4 -0.003 133 64 3.2 70 karte 1.7734643656246454 lauf/K_G_m3e-3.json 5e-8
lauf K_G_m2e-3 cpu4 -0.002 133 64 3.2 70 karte 1.77346059029 lauf/K_G_m2e-3.json 5e-8
lauf K_S_m1e-2 cpu4 -0.01  200 64 2.2 70 karte 1.7734911003052063 lauf/K_S_m1e-2.json 5e-8
lauf K_S_m7e-3 cpu4 -0.007 200 64 2.2 70 karte 1.7734795760905477 lauf/K_S_m7e-3.json 5e-8
lauf K_S_m5e-3 cpu4 -0.005 200 64 2.2 70 karte 1.77347194781 lauf/K_S_m5e-3.json 5e-8
lauf K_S_m4e-3 cpu4 -0.004 200 64 2.2 70 karte 1.77346815133 lauf/K_S_m4e-3.json 5e-8
lauf D_G_p3e-3 cpu4 0.003  133 64 3.2 70 f0 1.7735094547 lauf/D_G_p3e-3.json 1e-7
lauf D_H_m4e-3 cpu4 -0.004 200 64 3.2 70 f0 1.7733774318 lauf/D_H_m4e-3.json 1e-7
lauf D_H_m3e-3 cpu4 -0.003 200 64 3.2 70 f0 1.7733963927597045 lauf/D_H_m3e-3.json 5e-8
lauf D_H_m2e-3 cpu4 -0.002 200 64 3.2 70 f0 1.7734153180 lauf/D_H_m2e-3.json 1e-7
echo "kette_b fertig $(date --iso-8601=seconds)" > lauf/kette_b.fertig
