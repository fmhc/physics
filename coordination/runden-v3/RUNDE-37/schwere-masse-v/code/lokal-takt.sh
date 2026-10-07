#!/bin/bash
# SCHWERE-MASSE-V: Takt-Laeufe (Fernfeld) nacheinander auf cpu3, lokal nur ssh und Logs.
LOG=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-37/schwere-masse-v/lauf-69
R='cd /home/fmh/fmhc-physics-remote/schwere-masse-v && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh'
ssh -o BatchMode=yes fmh@192.168.178.69 "$R cpu3 sm-takt-h2 code/sm.py takt --LT 48 --band 16 24 --zusatzbaender 12 24 8 24 --ein lauf/qb-o0.75-h2.0.npz lauf/qb-o0.8-h2.0.npz lauf/qb-o0.85-h2.0.npz lauf/qb-o0.9-h2.0.npz lauf/qb-o0.95-h2.0.npz --out lauf/takt-h2.json" > $LOG/takt-h2.log 2>&1
ssh -o BatchMode=yes fmh@192.168.178.69 "$R cpu3 sm-takt-h1 code/sm.py takt --LT 56 --band 18 28 --zusatzbaender 14 28 22 28 --ein lauf/qb-o0.75-h1.0.npz lauf/qb-o0.8-h1.0.npz lauf/qb-o0.85-h1.0.npz lauf/qb-o0.9-h1.0.npz lauf/qb-o0.95-h1.0.npz --out lauf/takt-h1.json" > $LOG/takt-h1.log 2>&1
T=$(date '+%Y-%m-%d %H:%M:%S %Z')
printf 'takt fertig %s\n' "$T" >> $LOG/ketten-fertig.txt
