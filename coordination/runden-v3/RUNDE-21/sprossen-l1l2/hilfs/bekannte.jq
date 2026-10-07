# Bekannte Stellen einer l-Leiter: stellen.json (gezaehlt, Stufe 1: R, rho, w2, gap) + Newton-Lagen und Rechteck-Umlauf
# beider Stufen aus den Umlaufdateien der Vorlaeufer (Zuordnung ueber die Nummer im Namen).
def nrof: (.name | capture("nr(?<n>[0-9]+)").n | tonumber);
def kurz: {w2, rho, R: .Rchi, umlauf: .umlauf.umlauf, aufgeloest: .umlauf.aufgeloest, svr};
([ $n1[] | .punkte[] ] | map({key: (nrof | tostring), value: kurz}) | from_entries) as $m1 |
([ $n2[] | .punkte[] ] | map({key: (nrof | tostring), value: kurz}) | from_entries) as $m2 |
{ell: ($ell | tonumber), quelle: $quelle,
 stellen: [ $s[0].stellen[] | select(.gezaehlt and .bereich) |
   {ell: ($ell | tonumber), k, nr, R, rho, w2, gap, dw2_zeile, umlauf_zelle: [.umlauf_1, .umlauf_2],
    quelle: ($quelle + " Nr " + (.nr | tostring)),
    newton_st1: $m1[(.nr | tostring)], newton_st2: $m2[(.nr | tostring)]} ] }
