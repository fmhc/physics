#!/bin/bash
# WEYL-LINEAR-2 (Runde 42): Laufkette auf Spur cpu10, einmalig von Hand gestartet (kein Dienst, kein Timer, kein Hook).
# Jeder Lauf ueber kleintest.sh (<= 600 s, 1 Thread, 4 GB). Kein neuer Lauf startet nach SCHLUSS (17:58:00 UTC).
# Netz und Operator: weyllinear.py/spinnetz.py unveraendert aus WEYL-LINEAR-1 (M = 2048, feste Skala a = 4).
set -u
R=/home/fmh/fmhc-physics-remote/weyl-linear-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$R/code/weyllinear.py
SCHLUSS=$(date -u -d "2026-10-04 17:58:00 UTC" +%s)
KL=$R/lauf/kette.log
run() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name uebersprungen (Schluss) $(date -u +%T)" >> "$KL"; return; fi
  echo "$name start $(date -u +%T)" >> "$KL"
  bash "$K" cpu10 "$name" "$@" > "$R/lauf/$name.log" 2>&1
  echo "$name ende rc=$? $(date -u +%T)" >> "$KL"
}
K6=0.06,0.12,0.18,0.24,0.30,0.36
echo "kette start $(date -u +%T)" >> "$KL"
# Rauch (winzige Netze, nur Struktur der Auswertung pruefen)
cd "$R/rauch"
run wl2R0 "$P" zweig 400 1,2,3 2048 $K6 x "$R/rauch/zweig-400-x.json" a=4
run wl2R1 "$P" zweig 800 1,2,3 2048 0.06,0.12,0.18,0.24 y "$R/rauch/zweig-800-y.json" a=4
# Kontrolle: altes Netz N = 32 000, Saat 1, eine Welle (k = 0,06 laengs x) neu rechnen; Vergleich mit WL1-Datei
cd "$R/kontrolle"
run wl2K1 "$P" zweig 32000 1 2048 0.06 x "$R/kontrolle/repro-32000-s1-x-k006.json" a=4
# Produktion
cd "$R/lauf"
run wl2P01 "$P" zweig 32000 5,8 2048 $K6 x "$R/lauf/zweig-32000-s5s8-x.json" a=4
run wl2P02 "$P" zweig 128000 1 2048 0.06,0.12 x "$R/lauf/zweig-128000-s1-x-a.json" a=4
run wl2P03 "$P" zweig 128000 1 2048 0.18,0.24 x "$R/lauf/zweig-128000-s1-x-b.json" a=4
run wl2P04 "$P" zweig 128000 2 2048 0.06,0.12 y "$R/lauf/zweig-128000-s2-y-a.json" a=4
run wl2P05 "$P" zweig 128000 2 2048 0.18,0.24 y "$R/lauf/zweig-128000-s2-y-b.json" a=4
run wl2P06 "$P" zweig 128000 3 2048 0.06,0.12 z "$R/lauf/zweig-128000-s3-z-a.json" a=4
run wl2P07 "$P" zweig 128000 3 2048 0.18,0.24 z "$R/lauf/zweig-128000-s3-z-b.json" a=4
run wl2P08 "$P" zweig 128000 4 2048 0.06,0.12 x "$R/lauf/zweig-128000-s4-x-a.json" a=4
run wl2P09 "$P" zweig 128000 4 2048 0.18,0.24 x "$R/lauf/zweig-128000-s4-x-b.json" a=4
run wl2P10 "$P" zweig 32000 6 2048 $K6 y "$R/lauf/zweig-32000-s6-y.json" a=4
run wl2P11 "$P" zweig 32000 7 2048 $K6 z "$R/lauf/zweig-32000-s7-z.json" a=4
run wl2P12 "$P" zweig 32000 9 2048 $K6 y "$R/lauf/zweig-32000-s9-y.json" a=4
run wl2P13 "$P" zweig 32000 10 2048 $K6 z "$R/lauf/zweig-32000-s10-z.json" a=4
run wl2P14 "$P" zweig 32000 11 2048 $K6 x "$R/lauf/zweig-32000-s11-x.json" a=4
echo "kette ende $(date -u +%T)" >> "$KL"
