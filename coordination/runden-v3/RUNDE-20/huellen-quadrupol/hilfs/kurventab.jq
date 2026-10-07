# Markdown-Zeilen "Abstaende und Versatz je Kurve" aus aus/laeufe/auswertung.json (jq -r -f hilfs/kurventab.jq)
def g(x; n): if x == null then "-" else ((x * pow(10; n) | round) / pow(10; n) | tostring) end;
def km(vs): if (vs | length) == 0 then null else
  ([vs[] | . * 2 * 3.141592653589793] | {c: (map(cos) | add / length), s: (map(sin) | add / length)}) as $z
  | (($z.s | atan2(.; $z.c)) / (2 * 3.141592653589793)) as $m | ($m - ($m | floor)) end;
def zeile($l):
  . as $e | [$e.versatz[]? | select(. != null) | .v] as $vs
  | "| \($e.k) | \($l) | \($e.n) | \([$e.R[] | g(.; 2)] | join(" ")) | \([$e.dR[] | g(.; 3)] | join(" ")) | \(g($e.dR_mittel; 3)) (\(g($e.cv_dR; 3))) | \(g($e.l0_ref.mittel; 3)) (\($e.l0_ref.n // "-")) | \(g($e.q; 3)) | \(if $l == 0 then "0 (Def.)" else ([$vs[] | g(.; 3)] | join(" ")) end) | \(if $l == 0 then "0" else g(km($vs); 3) end) |";
([.kurven_l0[] | {k, l: 0, e: .}] + [.kurven_l1[] | {k, l: 1, e: .}] + [.kurven_l2[] | {k, l: 2, e: .}])
| sort_by(.k, .l) | .[] | select(.k <= 5) | . as $x | $x.e | zeile($x.l)
