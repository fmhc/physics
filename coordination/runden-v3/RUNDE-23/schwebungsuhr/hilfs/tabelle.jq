# Aufruf: jq -r --arg n NAME -f hilfs/tabelle.jq lauf/NAME.json
def r(n): if . == null then "-" elif (type == "number") then ((. * pow(10; n) | round) / pow(10; n) | tostring) else tostring end;
.analyse as $a
| [$n, (.D|tostring), (.dx|tostring), (.theta_durch_pi|tostring),
   ([$a.schwebung_mitte[] | (.dominant.re // null | if . == null then "-" else (fabs | r(5)) end)] | join(" / ")),
   ($a.frequenzen.anfang.omega1 | r(5)), ($a.frequenzen.ende.omega1 | r(5)),
   ($a.frequenzen.anfang.omega2 | r(5)), ($a.frequenzen.ende.omega2 | r(5)),
   ($a.frequenzen.anfang.betrag_delta | r(5)), ($a.frequenzen.ende.betrag_delta | r(5)),
   ($a.ladungen.anfang.Q1 | r(4)), ($a.ladungen.ende.Q1 | r(4)),
   ($a.ladungen.anfang.Q2 | r(4)), ($a.ladungen.ende.Q2 | r(4)),
   ($a.abstaende.schwerpunkt_anfang | r(3)), ($a.abstaende.schwerpunkt_ende | r(3)),
   ($a.abstaende.maxima_anfang | r(3)), ($a.abstaende.maxima_ende | r(3)),
   ($a.abstaende.erstmals_verschmolzen_t | r(1)), ($a.abstaende.verschmolzen_bei_T | tostring)]
| join(" | ")
