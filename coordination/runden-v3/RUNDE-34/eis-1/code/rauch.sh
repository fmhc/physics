#!/bin/bash
# EIS-1 Rauchlaeufe (Gittergroessen 2 und 6, nicht die echten), je Spur nacheinander ueber kleintest.sh.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=/home/fmh/fmhc-physics-remote/runde34-eis/code
D=/home/fmh/fmhc-physics-remote/runde34-eis/rauch
cd "$D" || exit 1
( bash "$K" cpu r34eis-rauch-eis6 "$C/eis_mc.py" 6 99 1e8 2e8 4 90 "$D/eis_L6_s99" > "$D/eis_L6_s99.log" 2>&1 ) &
( bash "$K" cpu2 r34eis-rauch-z2 "$C/stabnetz.py" zaehlen pyro 2 dicht "$D/zaehl_pyro_dicht.json" > "$D/zaehl_pyro_dicht.log" 2>&1
  bash "$K" cpu2 r34eis-rauch-zb2 "$C/stabnetz.py" zaehlen pyro 2,6 bloch "$D/zaehl_pyro_bloch.json" > "$D/zaehl_pyro_bloch.log" 2>&1
  bash "$K" cpu2 r34eis-rauch-zf2 "$C/stabnetz.py" zaehlen fcc 2 dicht "$D/zaehl_fcc_dicht.json" > "$D/zaehl_fcc_dicht.log" 2>&1
  bash "$K" cpu2 r34eis-rauch-ap6 "$C/stabnetz.py" antwort pyro 6 "$D/stab_pyro_L6.json" > "$D/stab_pyro_L6.log" 2>&1
  bash "$K" cpu2 r34eis-rauch-af6 "$C/stabnetz.py" antwort fcc 6 "$D/stab_fcc_L6.json" > "$D/stab_fcc_L6.log" 2>&1 ) &
wait
echo "rauch fertig $(date --iso-8601=seconds)" > "$D/rauch_fertig.txt"
