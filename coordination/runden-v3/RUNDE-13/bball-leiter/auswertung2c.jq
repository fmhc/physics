# B-BALL-2c Auswertung nach KARTE-2C-LETZTES-ZEHNTEL.md.
# Aufruf: jq -s -f auswertung2c.jq lauf-69/aus2c/*.json   (12 Familien-JSON: 3 t x 2 Stufen x 2 Haelften)
def kand: [.kandidaten[]? | select(.lokal != null and .rechteck.umlauf != null) |
  {x: .lokal.x_stern, rho: .lokal.rho_stern, klammer: .lokal.klammer_breite, u: .rechteck.umlauf,
   u_roh: .rechteck.umlauf_roh, kreuzung: .rechteck.umlauf_kreuzung, aufl: .rechteck.aufgeloest,
   sprung: .rechteck.max_sprung}];
def stufe($fs):
  {h: $fs[0].h, t: $fs[0].argumente.t, dateien: [$fs[].argumente.name], laufzeit: ([$fs[].laufzeit] | add),
   haelften: ($fs | length), entfallen: ([$fs[].budget_entfallen | length] | add),
   zeilen_gueltig: ([$fs[].mitglieder[] | select(.gueltig) | .x] | unique | length),
   wechsel: [$fs[].vorzeichenwechsel[] | {x1, x2, rho1, rho2, s1, s2, richtung}] | sort_by(.x1),
   kand: ([$fs[] | kand[]] | sort_by(.x)),
   streifen: ([$fs[].streifen[]] | length),
   streifen_fehlend: ([$fs[].streifen[] | select(.umlauf == null)] | length),
   streifen_nicht_aufl: ([$fs[].streifen[] | select(.umlauf != null and (.aufgeloest | not))] | length),
   streifen_u_ne0: [$fs[].streifen[] | select(.umlauf != null and .umlauf != 0) | {x_lo, x_hi, umlauf, aufgeloest, max_sprung}],
   max_sprung_streifen: ([$fs[].streifen[].max_sprung | select(. != null)] | max),
   gamma: [$fs[] | select(.h == 0.02) | .mitglieder[] | select(.gueltig) | .x as $x | .wurzeln[] |
           select(.Gamma != null and .rho > 1.0) | {x: $x, rho, Gamma}]};
def eine($s):
  ($s.wechsel | length) == 1 and ($s.kand | length) == 1 and $s.kand[0].aufl and $s.kand[0].u == -1
  and $s.streifen_fehlend == 0 and $s.streifen_nicht_aufl == 0 and $s.streifen == 30 and $s.zeilen_gueltig == 31
  and ([$s.streifen_u_ne0[] | select(.umlauf != -1 or $s.kand[0].x < .x_lo or $s.kand[0].x > .x_hi)] | length) == 0;
def falte($s):
  ($s.wechsel | length) >= 3 and ($s.kand | length) == ($s.wechsel | length) and ($s.kand | all(.aufl))
  and ([$s.kand[].u] | (any(. == 1) and any(. == -1)));
group_by(.argumente.t) | map(
  .[0].argumente.t as $t |
  (map(select(.h == 0.02))) as $fa | (map(select(.h == 0.01))) as $fc |
  (if ($fa | length) > 0 then stufe($fa) else null end) as $a |
  (if ($fc | length) > 0 then stufe($fc) else null end) as $c |
  ($a != null and $c != null and $a.haelften == 2 and $c.haelften == 2) as $komplett |
  {t: $t, komplett: $komplett,
   n_wechsel: [($a.wechsel | length), ($c.wechsel | length)],
   eine: ($komplett and eine($a) and eine($c)),
   falte: ($komplett and falte($a) and falte($c)),
   lage_h002: (if $a != null and ($a.kand | length) > 0 then $a.kand[0] else null end),
   lage_h001: (if $c != null and ($c.kand | length) > 0 then $c.kand[0] else null end),
   stufen: [$a, $c]}
) | sort_by(.t) | . as $ts |
($ts | length == 3 and all(.eine)) as $alle_eine |
(if $alle_eine then [$ts[].lage_h002.x] else null end) as $xs |
(if $alle_eine then ($xs[0] < $xs[1] and $xs[1] < $xs[2]) else false end) as $steigt |
(if $alle_eine then ($xs | all(. >= 0.8679 and . <= 0.9256)) else false end) as $zwischen |
{ausgang: (if $alle_eine and $steigt and $zwischen then "Eine wandernde Nullstelle"
           elif ($ts | any(.falte)) then "Falte (zwei verschiedene Stellen)"
           elif $alle_eine and ($steigt | not) then "Falte (zwei verschiedene Stellen): der eine Wechsel springt nicht monoton"
           else "Unentschieden" end),
 lagen_steigen: $steigt, lagen_zwischen_08679_09256: $zwischen, je_t: $ts}
