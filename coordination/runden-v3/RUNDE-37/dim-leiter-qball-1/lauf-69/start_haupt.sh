#!/bin/bash
# DIM-LEITER-QBALL-1: Hauptlaeufe, ein Lauf je D; Spur cpu11 (ungerade D) und cpu4 (gerade D), je Spur nacheinander (flock).
B=/home/fmh/fmhc-physics-remote/dim-leiter-qball-1
cd $B/lauf
(
for D in 1 3 5 7 9 11; do
  bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu11 dlq1d$D $B/code/dim_leiter.py rechne $D $B/lauf/d$D.json > $B/lauf/d$D.log 2>&1 < /dev/null
done
) > /dev/null 2>&1 < /dev/null &
(
for D in 2 4 6 8 10 12; do
  bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu4 dlq1d$D $B/code/dim_leiter.py rechne $D $B/lauf/d$D.json > $B/lauf/d$D.log 2>&1 < /dev/null
done
) > /dev/null 2>&1 < /dev/null &
date -u
