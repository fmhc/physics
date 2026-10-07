#!/bin/bash
# S6 Kette A (Spur p4000a): Netz-Fluss beta 3,41 (zwei Laeufe), dann 3,36
R=/home/fmh/fmhc-physics-remote/quant-3/run-s6-fn.sh
bash $R p4000a fn-a 20261601 "3.41" 8 45 540 10.0
bash $R p4000a fn-c 20261603 "3.41" 8 45 540 2.0
bash $R p4000a fn-lo 20261605 "3.36" 8 45 540 2.0
