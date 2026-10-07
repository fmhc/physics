# L1-Tabelle aus auswertung-final.json
def sci: if . == null then "-" elif . == 0 then "0" else (. as $x | ($x|fabs|log10|floor) as $e | ((($x / pow(10; $e)) * 10 | round / 10 | tostring) + "e" + ($e|tostring))) end;
def f(n): (. * pow(10; n) | round / pow(10; n) | tostring);
"| Nr (R17) | omega^2 St1 (Newton) | rho St1 | Abstand zur Tabelle St1 (omega^2 / rho) | Abstand St2 | Umlauf St1 / St2 | groesster Sprung St1 / St2 | Randpunkte | sigma2/sigma1 St1 / St2 | Zellen-Umlauf |",
"|---|---|---|---|---|---|---|---|---|---|",
(.L1.je_stelle | to_entries | sort_by(.key|tonumber)[] | .key as $n | .value as $v |
 "| \($n) | \($v.st1.w2|f(10)) | \($v.st1.rho|f(10)) | \($v.st1.dw2|fabs|sci) / \($v.st1.drho|fabs|sci) | \($v.st2.dw2|fabs|sci) / \($v.st2.drho|fabs|sci) | \($v.st1.umlauf) / \($v.st2.umlauf) | \($v.st1.sprung|f(3)) / \($v.st2.sprung|f(3)) | \($v.st1.punkte) / \($v.st2.punkte) | \($v.st1.svr|sci) / \($v.st2.svr|sci) | \($v.st1.umlauf_zelle) / \($v.st2.umlauf_zelle) |")
