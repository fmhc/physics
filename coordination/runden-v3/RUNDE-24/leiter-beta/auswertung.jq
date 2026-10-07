# LEITER-BETA: mechanische Auswertung nach PLAN.md Abschnitt 7. Eingabe gesamt.json (von auswertung.sh):
# {"kand": [Kandidaten aus phase1.jq], "laeufe": {"c<k>-h004": {...}, "c<k>-h002": {...}}}
def rhoz: 1.7734530718;
def binf: 2.6186;
def pm1($u): $u != null and ((($u | fabs) - 1) | fabs) < 0.1;
def stufe($l):
  if $l == null then {da: false, ok: false, grund: "Lauf fehlt"}
  else
    ($l.p.ziel_wechsel // []) as $W
    | ([ ($l.p.rechtecke // [])[] | select(.art == "wechsel") ]) as $re
    | if ($W | length) == 0 then {da: true, ok: false, n_wechsel: 0, vollst: $l.p.profile_vollstaendig, grund: "kein Wechsel"}
      else
        ([ $W | to_entries[] | {j: .key, d: ((.value.x_stern - $l.x_pol) | fabs)} ] | min_by(.d) | .j) as $j
        | $W[$j] as $w | ($re[$j] // {}) as $r
        | {da: true, n_wechsel: ($W | length), vollst: $l.p.profile_vollstaendig,
           x_stern: $w.x_stern, rho_stern: $w.rho_stern, s_lo: $w.s_lo, s_hi: $w.s_hi, kw: $w.kernwachstum_kandidat,
           ausl: $w.ausloeschung_kandidat, ast_konsistent: $w.ast_konsistent,
           umlauf: ($r.umlauf // null), sprung: ($r.max_sprung // null), aufgeloest: ($r.aufgeloest // false),
           punkte: ($r.punkte // null), runden: ($r.runden_benutzt // null), fehler: ($r.fehler // null)}
        | . + {ok: (.vollst == true and .n_wechsel == 1 and .aufgeloest == true and pm1(.umlauf) and .kw <= 1e8)}
        | . + {grund: (if .ok then "" else ([ (if .vollst != true then "Profile unvollstaendig" else empty end),
                (if .n_wechsel != 1 then "\(.n_wechsel) Wechsel" else empty end),
                (if .aufgeloest != true then "Rechteck nicht aufgeloest" else empty end),
                (if pm1(.umlauf) | not then "Umlauf nicht +-1" else empty end),
                (if .kw > 1e8 then "Kernwachstum > 1e8" else empty end)] | join(", ")) end)}
      end
  end;
.laeufe as $L
| [ .kand[] as $c
    | stufe($L["c\($c.k)-h004"]) as $a | stufe($L["c\($c.k)-h002"]) as $b
    | ($a.ok and $b.ok
       and ((($a.x_stern - $b.x_stern) | fabs) <= 1e-4) and ((($a.rho_stern - $b.rho_stern) | fabs) <= 1e-4)
       and (($a.umlauf > 0) == ($b.umlauf > 0))) as $spr
    | {k: $c.k, ast: $c.ast, fenster: $c.fenster, x_grob: $c.x_stern, umlauf_grob: $c.umlauf_grob,
       sprosse: $spr,
       status: (if $spr then "Sprosse" elif ($a.da | not) or ($b.da | not) then "nicht gerechnet" else "unentschieden" end),
       x: ($b.x_stern // null), eps: (if $b.x_stern != null then $b.x_stern - 0.75 else null end),
       rho: ($b.rho_stern // null), umlauf: ($b.umlauf // null),
       d_x_stufen: (if $a.x_stern != null and $b.x_stern != null then $b.x_stern - $a.x_stern else null end),
       d_rho_stufen: (if $a.rho_stern != null and $b.rho_stern != null then $b.rho_stern - $a.rho_stern else null end),
       h004: $a, h002: $b}
    | . + {im_bereich: (.eps != null and .eps >= 0.03 and .eps <= 0.08),
           c_wert: (if .rho != null and .eps != null then (.rho - rhoz) / .eps else null end)}
  ] as $K
| (reduce $K[] as $c ([];
     if ($c.sprosse and $c.im_bereich) then
       if (length > 0) and ((.[-1] | .[-1]) as $p | ($p != null) and $p.k == $c.k - 1 and (($p.umlauf > 0) != ($c.umlauf > 0)))
       then .[-1] += [$c] else . + [[$c]] end
     else . + [[]] end) | map(select(length > 0))) as $F
| ($F | sort_by([(- length), .[0].eps]) | .[0] // []) as $f
| ([ range(0; ($f | length) - 1) as $i
     | {zwischen: [$f[$i].k, $f[$i + 1].k], eps: [$f[$i].eps, $f[$i + 1].eps],
        schritt: ((1 / $f[$i].eps) - (1 / $f[$i + 1].eps))} ]) as $S
| ([ $K[] | select(.sprosse and .im_bereich) ]) as $R
| {kandidaten: $K,
   folgen: [ $F[] | map(.k) ],
   folge: [ $f[] | {k, eps, x, rho, umlauf} ],
   schritte: $S,
   LB1: {eingetroffen: (($f | length) >= 4), laenge: ($f | length)},
   LB2: (if ($f | length) >= 3 then
           {auswertbar: true,
            alle_in_band: ([ $S[] | .schritt >= 2.45 and .schritt <= 2.80 ] | all),
            letzte_zwei: [ $S[0:2][] | .schritt ],
            letzte_zwei_in_3proz: ([ $S[0:2][] | .schritt >= 0.97 * binf and .schritt <= 1.03 * binf ] | all)}
           | . + {eingetroffen: (.alle_in_band and .letzte_zwei_in_3proz)}
         else {auswertbar: false, eingetroffen: false} end),
   LB3: (if ($R | length) > 0 then
           {auswertbar: true, n: ($R | length),
            je: [ $R[] | {k, eps, rho, c_wert, ok: (.rho > rhoz and .rho < rhoz + 1.5 * .eps)} ]}
           | . + {eingetroffen: ([ .je[] | .ok ] | all)}
         else {auswertbar: false, eingetroffen: false} end)}
