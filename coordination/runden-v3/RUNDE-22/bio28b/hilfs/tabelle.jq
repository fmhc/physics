# Tabelle je Gitter, Lauf und Stueck aus lauf-69/ausgabe/bio28b_auswertung.json (nur Darstellung)
def r(x; n): if x == null then "-" else ((x * pow(10; n) | round) / pow(10; n) | tostring) end;
def kz(k): ({"auf": "auf", "neben": "neben", "unentschieden": "unent.", "ausserhalb": "ausserh.", "gestoert": "gestoert", "nicht rund": "nicht rund", "kein Tropfen": "kein Tropfen"}[k]) // (k // "-");
.laeufe as $L
| ["grob", "fein"][] as $st
| ["w60_nachbarn1", "w60_nachbarn2", "w75_nachbarn1", "w75_nachbarn2"][] as $n
| $L[$st][$n] as $x
| $x.stuecke[] as $s
| [ "100", "200", "300" ] as $Ts
| [ $Ts[] | $x.je_T[.].stuecke[$s.rang] ] as $z
| [ $z[] | (.klassifikator["0.3"] // {}) ] as $k
| "| \($st) | \($n) | \($s.rang) | \($x.K0.t_teilung) | \(r($s.Q_teil; 2)) (w \($s.windung)) | \(r($z[0].anteil; 3)) / \(r($z[1].anteil; 3)) / \(r($z[2].anteil; 3)) | \(r($z[2].v; 3)) | \($z[2].windung) (\(r($z[2].S_min_kreis; 2))) | \(r($k[0].rmax_zu_ra; 2)) / \(r($k[1].rmax_zu_ra; 2)) / \(r($k[2].rmax_zu_ra; 2)) | \(kz($k[0].klasse)) / \(kz($k[1].klasse)) / \(kz($k[2].klasse)) |"
