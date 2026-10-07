#!/bin/bash
# LEITER-BETA: erzeugt den Starter fuer Phase 2 mechanisch aus kandidaten.json (PLAN.md Abschnitt 6).
# Lokal (nur bash und jq): bash gen2.sh kandidaten.json > start2.sh
# Reihenfolge: Kandidaten mit omega*^2 in [0,78; 0,83] nach omega*^2 aufsteigend, danach die uebrigen; je Kandidat erst
# h = 0,02, dann h = 0,04. Die Laeufe gehen reihum auf die Spuren cpu, cpu2, cpu3, cpu4, cpu6, je Spur nacheinander.
# Je Kandidat: X = omega*^2 (grob) auf 6 Stellen, S = Steigung des Zielasts auf 4 Stellen, R = rho* + S_roh (X - omega*^2)
# auf 7 Stellen.
set -eu
KJ=${1:-kandidaten.json}
cat <<'EOF'
#!/bin/bash
# LEITER-BETA (Runde 24), Phase 2 (Kandidaten, Stufen h = 0,04 und 0,02); erzeugt von gen2.sh aus kandidaten.json.
# Einmal von Hand per nohup auf der .69 gestartet; kein Dienst, kein Timer.
cd /home/fmh/fmhc-physics-remote/runde24-leiter-beta || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/runde24-leiter-beta
P=bic2_3d_praez.py
G2="--beta 1.0 --n-zeilen 7 --zeilen-dx 3e-4 --n-rho 5000 --n-dicht 2001 --dicht-halb 0.002 --u-n 60 --u-runden 30 --pr-drho 0.01 --pr-drho-max 0.03 --pr-u-halb 3 --iter-wurzel 80 --tol-wurzel 1e-13 --budget 480 --reserve 150 --pole ja --art leiter"
lauf() {   # spur name argumente...
  local s=$1 n=$2
  shift 2
  bash $K $s r24lb-$n $P praez $G2 "$@" --out lauf/$n > $D/LAUF-$n.log 2>&1
}
echo "PHASE2-START $(date -Is)" > $D/KETTE2.log
EOF
jq -r '
  ["cpu", "cpu2", "cpu3", "cpu4", "cpu6"] as $spuren
  | [ .[] | . + {innen: (.x_stern >= 0.78 and .x_stern <= 0.83)} ]
  | (map(select(.innen)) | sort_by(.x_stern)) + (map(select(.innen | not)) | sort_by(.x_stern))
  | [ .[] as $c | (2, 4) as $hh
      | ($c.x_stern * 1e6 | round / 1e6) as $X
      | "lauf SPUR c\($c.k)-h00\($hh) --h \(if $hh == 2 then "0.02" else "0.04" end) --x0 \($X) --rho0 \(($c.rho_stern + $c.steigung * ($X - $c.x_stern)) * 1e7 | round / 1e7) --rho-steig \($c.steigung * 1e4 | round / 1e4) --x-pol \($X)" ]
  | to_entries
  | group_by(.key % 5)
  | map(. as $g | "( " + ([ $g[] | .value | sub("SPUR"; $spuren[$g[0].key % 5]) ] | join(" ; ")) + " ) &")
  | .[]
' "$KJ"
cat <<'EOF'
wait
echo "PHASE2-ENDE $(date -Is)" >> $D/KETTE2.log
EOF
