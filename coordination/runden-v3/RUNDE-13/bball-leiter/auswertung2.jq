# B-BALL-2 Auswertung nach KARTE-2-INTERPOLATION.md (Regel je t, Kontrollen K1/K2, Gesamt).
# Aufruf: jq -s -f auswertung2.jq lauf-69/aus2/*.json   (nur Familien-JSON von bball2.py)
def ziel($b):
  if $b == "K1" then {x: 0.797677, rho: 1.744618}
  elif $b == "K2" then {x: 0.925610, rho: 1.837996}
  elif $b == "t0.25" then {x: 0.8297, rho: 1.7680}
  elif $b == "t0.5" then {x: 0.8617, rho: 1.7913}
  elif $b == "t0.75" then {x: 0.8936, rho: 1.8147}
  else null end;
def kand: [.kandidaten[]? | select(.lokal != null and .rechteck.umlauf != null) |
  {x: .lokal.x_stern, rho: .lokal.rho_stern, klammer: .lokal.klammer_breite, u: .rechteck.umlauf,
   u_roh: .rechteck.umlauf_roh, kreuzung: .rechteck.umlauf_kreuzung, aufl: .rechteck.aufgeloest,
   sprung: .rechteck.max_sprung}];
def stufe($z):
  {h: .h, t: .argumente.t, datei: .argumente.name, laufzeit: .laufzeit, entfallen: (.budget_entfallen | length),
   zeilen_gueltig: ([.mitglieder[] | select(.gueltig)] | length),
   streifen: (.streifen | length), streifen_aufl_u0: ([.streifen[] | select(.umlauf == 0 and .aufgeloest)] | length),
   streifen_u_ne0: [.streifen[] | select(.umlauf != null and .umlauf != 0) | {i, x_lo, x_hi, umlauf, aufgeloest, max_sprung}],
   streifen_fehlend: ([.streifen[] | select(.umlauf == null)] | length),
   max_sprung_streifen: ([.streifen[].max_sprung | select(. != null)] | max),
   wechsel: [.vorzeichenwechsel[] | {x1, x2, rho1, rho2, s1, s2, richtung}],
   wechsel_im_fenster: [.vorzeichenwechsel[] | select(((((.x1 + .x2) / 2) - $z.x) | fabs) <= 0.04 and
                                                     ((((.rho1 + .rho2) / 2) - $z.rho) | fabs) <= 0.05)],
   kand: kand,
   gamma: [.mitglieder[] | select(.gueltig) | .x as $x | .wurzeln[] | select(.Gamma != null and .rho > 1.0) |
           {x: $x, rho, Gamma}]};
def kontrolle($s; $z): [$s.kand[]? | select(.aufl and .u == -1 and ((.x - $z.x) | fabs) <= 1e-4
                                            and ((.rho - $z.rho) | fabs) <= 1e-4)];
group_by(.band) | map(
  .[0].band as $b | ziel($b) as $z |
  (map(stufe($z)) | sort_by(-.h)) as $st |
  ($st | map(select(.h == 0.02)) | .[0]) as $a |
  ($st | map(select(.h == 0.01)) | .[0]) as $c |
  ([ $a.kand[]? as $p | $c.kand[]? as $q |
     select($p.aufl and $q.aufl and ($p.u | fabs) == 1 and ($q.u | fabs) == 1
            and (($p.x - $z.x) | fabs) <= 0.04 and (($p.rho - $z.rho) | fabs) <= 0.05
            and (($q.x - $z.x) | fabs) <= 0.04 and (($q.rho - $z.rho) | fabs) <= 0.05
            and (($p.x - $q.x) | fabs) <= 1e-4 and (($p.rho - $q.rho) | fabs) <= 1e-4) |
     {x_h002: $p.x, rho_h002: $p.rho, x_h001: $q.x, rho_h001: $q.rho, u_h002: $p.u, u_h001: $q.u,
      sprung_h002: $p.sprung, sprung_h001: $q.sprung, dx_stufen: (($p.x - $q.x) | fabs),
      drho_stufen: (($p.rho - $q.rho) | fabs), dx_vorhersage: ($p.x - $z.x), drho_vorhersage: ($p.rho - $z.rho)} ]) as $treffer |
  ($a != null and $c != null) as $beide |
  ($beide and ([$a, $c] | all(.wechsel_im_fenster == [] and .streifen == 16 and .streifen_aufl_u0 == 16
                               and .streifen_fehlend == 0 and ([.kand[] | select(.u != 0)] | length) == 0))) as $nicht |
  (if ($treffer | length) > 0 and $a != null then
     ($treffer[0].rho_h002 as $r | [$a.gamma[] | select(((.rho - $r) | fabs) < 0.05)] | min_by(.Gamma))
   else null end) as $gmin |
  {band: $b, ziel: $z,
   ausgang: (if ($b == "K1" or $b == "K2") then
               (if ($beide and (kontrolle($a; $z) | length) > 0 and (kontrolle($c; $z) | length) > 0)
                then "bestanden" else "VERFEHLT" end)
             elif ($treffer | length) > 0 then "Gefunden" elif $nicht then "Nicht gefunden" else "Unentschieden" end),
   treffer: $treffer, breitenminimum_h002: $gmin, stufen: $st}
) | . as $alle |
(map(select(.band == "K1" or .band == "K2")) | (length == 2 and all(.ausgang == "bestanden"))) as $kontrollen |
(map(select(.band | startswith("t")))) as $ts |
{kontrollen_bestanden: $kontrollen,
 gesamt: (if ($kontrollen | not) then "nicht auswertbar"
          elif ($ts | length) == 3 and ($ts | all(.ausgang == "Gefunden")) then "Kontinuitaet traegt"
          elif ($ts | any(.ausgang == "Nicht gefunden")) then "Kontinuitaet traegt nicht"
          else "Unentschieden" end),
 je_band: $alle}
