#!/bin/bash
# S6 Kette B (Spur p4000b): wartet auf fh-a (Lock), dann Netz-Fluss beta 3,41, 3,46; Hyperkubus 2,38 / 2,48
R=/home/fmh/fmhc-physics-remote/quant-3/run-s6-fn.sh
H=/home/fmh/fmhc-physics-remote/quant-3/run-s6-fh.sh
bash $R p4000b fn-b 20261602 "3.41" 8 45 540 2.0
bash $R p4000b fn-hi 20261606 "3.46" 8 45 540 2.0
bash $H p4000b fh-b 20261502 "2.38 2.48" 14 540
