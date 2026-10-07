# Versatz v = (R - R0_unten) / (R0_oben - R0_unten), modulo 1 (Schreibtischprobe der Plan-Definition, Abschnitt 6).
# Aufruf: jq -n -c --slurpfile l0 ref/l0-stellen-r18.json --slurpfile lx ref/l1-stellen-r19.json -f hilfs/versatz.jq
def gez(d): [d.stellen[] | select(.gezaehlt and .bereich)];
def kurven(d): gez(d) | group_by(.k) | map({key: (.[0].k | tostring), value: (map(.R) | sort)}) | from_entries;
(kurven($l0[0])) as $K0
| gez($lx[0]) | sort_by(.k, .R)
| map(. as $s | ($K0[($s.k | tostring)] // []) as $R0
      | if ($R0 | length) < 2 then {nr: $s.nr, k: $s.k, R: $s.R, v: null}
        else ([range(0; $R0 | length) | select($R0[.] <= $s.R)] | last // -1) as $j0
          | (if $j0 < 0 then 0 elif $j0 >= (($R0 | length) - 1) then (($R0 | length) - 2) else $j0 end) as $j
          | (($s.R - $R0[$j]) / ($R0[$j + 1] - $R0[$j])) as $vr
          | {nr: $s.nr, k: $s.k, R: ($s.R * 1000 | round / 1000), R0u: ($R0[$j] * 1000 | round / 1000),
             abst: (($R0[$j + 1] - $R0[$j]) * 1000 | round / 1000), j0: $j0,
             v: (($vr - ($vr | floor)) * 10000 | round / 10000)}
        end)
| .[]
