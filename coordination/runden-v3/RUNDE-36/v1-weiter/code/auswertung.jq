# V-1-WEITER: mechanische Auswertung nach PLAN.md Abschnitt 7 (eingefroren 2026-10-04 00:30:57 CEST).
# Aufruf: jq -s -f auswertung.jq lauf-69/A_*.json lauf-69/B_*.json > lauf-69/auswertung.json
# Variante A = rtol 1e-11 (h_bg 0,0025), Variante B = rtol 1e-10 (h_bg 0,005).
def RWB: 1.7734530718064692;
def zsel: (.nullstellen | min_by((.rho_z - RWB) | fabs));
def lauf($e; $r): (map(select(.eps == $e and .rtol == $r)) | if length > 0 then .[0] else null end);
def z($e; $r): (lauf($e; $r) | if . == null then null elif (.nullstellen | length) == 0 then null else zsel end);
def aufg($e): (z($e; 1e-11) as $a | z($e; 1e-10) as $b
  | if $a == null or $b == null then false
    else ($a.amp_neu_aus_max) as $x | ($a.lose_10rtol.amp_neu_aus_max) as $xl | ($b.amp_neu_aus_max) as $xb
      | ($x > 0) and ((($xl - $x) | fabs) <= 0.2 * $x) and ((($xb - $x) | fabs) <= 0.3 * $x)
    end);
def P($e): (z($e; 1e-11) | if . == null then null else .P_neu_aus end);

{
  urteile: {
    V0: ([z(0; 1e-11), z(0; 1e-10)] as $zz
      | {urteil: (if ($zz[0] != null and $zz[1] != null
                       and (($zz[0].rho_z - RWB) | fabs) < 1e-8 and (($zz[1].rho_z - RWB) | fabs) < 1e-8)
                   then "eingetroffen" else "nicht eingetroffen" end),
         werte: {rho_z_A: $zz[0].rho_z, rho_z_B: $zz[1].rho_z,
                 abw_A: (if $zz[0] != null then $zz[0].rho_z - RWB else null end),
                 abw_B: (if $zz[1] != null then $zz[1].rho_z - RWB else null end),
                 T_aus_A: $zz[0].T_aus_bei_rho_z, flussbilanz_A: $zz[0].flussbilanz}}),
    V1: ([[0.001, 0.003, 0.01][] as $e | [1e-11, 1e-10][] as $r | {eps: $e, rtol: $r, z: z($e; $r)}] as $l
      | {urteil: (if ($l | all(.z != null and .z.T_aus_rel < 1e-10)) then "eingetroffen" else "nicht eingetroffen" end),
         werte: ($l | map({eps, variante: (if .rtol == 1e-11 then "A" else "B" end), rho_z: .z.rho_z,
                           restgroesse_rel: .z.T_aus_rel, T_aus: .z.T_aus_bei_rho_z, flussbilanz: .z.flussbilanz}))}),
    V2: ([z(0; 1e-11).rho_z, z(0.001; 1e-11).rho_z, z(0.003; 1e-11).rho_z] as $a
      | [z(0; 1e-10).rho_z, z(0.001; 1e-10).rho_z, z(0.003; 1e-10).rho_z] as $b
      | (if ($a | all(. != null)) then (($a[2] - $a[0]) / ($a[1] - $a[0])) else null end) as $rA
      | (if ($b | all(. != null)) then (($b[2] - $b[0]) / ($b[1] - $b[0])) else null end) as $rB
      | ($rA != null and $rA >= 2.7 and $rA <= 3.3) as $okA
      | ($rB != null and $rB >= 2.7 and $rB <= 3.3) as $okB
      | {urteil: (if $okA then "eingetroffen" else "nicht eingetroffen" end),
         vermerk: (if $rB == null then "Variante B fehlt" elif $okB != $okA then "Variante B gibt ein anderes Urteil" else null end),
         werte: {verhaeltnis_A: $rA, verhaeltnis_B: $rB,
                 d1e3_A: (if $rA != null then $a[1] - $a[0] else null end), d3e3_A: (if $rA != null then $a[2] - $a[0] else null end),
                 d1e3_B: (if $rB != null then $b[1] - $b[0] else null end), d3e3_B: (if $rB != null then $b[2] - $b[0] else null end)}}),
    V3: (. as $alle | [-0.001, -0.003, -0.01] as $es
      | [$es[] | . as $e | ($alle | z($e; 1e-11)) as $za | ($alle | z($e; 1e-10)) as $zb
         | {eps: $e, aufgeloest: ($alle | aufg($e)), P_neu: ($alle | P($e)), amp_A: $za.amp_neu_aus_max,
            amp_A_10rtol: $za.lose_10rtol.amp_neu_aus_max, amp_B: $zb.amp_neu_aus_max,
            T_alt: $za.T_alt_aus, T_aus: $za.T_aus_bei_rho_z, rho_z_A: $za.rho_z}] as $w
      | ([$w[] | select(.aufgeloest)] | sort_by(-.eps)) as $res
      | ([range(0; ($res | length) - 1) as $i | ($res[$i].P_neu < $res[$i + 1].P_neu)] | all) as $mono
      | {urteil: (if (($w | all(.aufgeloest)) and $mono and ($w | all(.P_neu > 0))) then "eingetroffen"
                  elif ($mono | not) then "nicht eingetroffen"
                  else "nicht auswertbar" end),
         vermerk: (if ($w | all(.aufgeloest)) then null
                   else "aufgeloest nur: " + ([$w[] | select(.aufgeloest) | .eps | tostring] | join(", ")) end),
         werte: $w}),
    V4: (. as $alle | [-0.001, -0.003, -0.01] as $es
      | if ([$es[] | . as $e | ($alle | aufg($e))] | all) then
          (P(-0.01) / P(-0.003) | log) as $l1 | (P(-0.003) / P(-0.001) | log) as $l2
          | ($l1 / ((10 / 3) | log)) as $p1 | ($l2 / (3 | log)) as $p2
          | ($l1 / (1 / (0.003 | sqrt) - 1 / (0.01 | sqrt))) as $c1
          | ($l2 / (1 / (0.001 | sqrt) - 1 / (0.003 | sqrt))) as $c2
          | {urteil: (if ($p2 > $p1 and $p1 > 0 and (($c1 - $c2) | fabs) <= 0.3 * ($c1 + $c2) / 2)
                      then "eingetroffen" else "nicht eingetroffen" end),
             werte: {p1: $p1, p2: $p2, c1: $c1, c2: $c2}}
        else {urteil: "nicht auswertbar", vermerk: "weniger als drei aufgeloeste Werte",
              werte: {aufgeloest: [$es[] | . as $e | {eps: $e, aufgeloest: ($alle | aufg($e))}]}}
        end)
  },
  kontrollen: {
    laeufe: [.[] | {eps, rtol, h_bg, n_null: (.nullstellen | length), sek,
                    bg_delta: .hintergrund.delta, bg_rest: .hintergrund.rest_innen_max,
                    bg_max_abw_f0: .hintergrund.max_abw_f0,
                    flussbilanz_max: ([.nullstellen[].streuung[].flussbilanz | fabs] | max),
                    E_bei_rho_z: [.nullstellen[].E_bei_rho_z], alle_rho_z: [.nullstellen[].rho_z]}]
  }
}
