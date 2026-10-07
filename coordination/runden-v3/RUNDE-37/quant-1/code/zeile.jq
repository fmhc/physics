def f(d): if . == null then "-" else (. * pow(10; d) | round / pow(10; d) | tostring) end;
def ef(k; t; d): (.eff[k][t] // [null, null]) as $e | if $e[0] == null then "-" else "\($e[0]|f(d))(\($e[1]|f(d)))" end;
def pl(k; d): (.plateau[k] // null) as $p | if $p == null then "-" else "\($p.wert|f(d))(\($p.fehler|f(d)))" end;
def b(k; q): (.eff[k][0] // [null, null]) as $e | if $e[0] == null then "-" else "\((-$e[0]/q)|f(4))(\(($e[1]/q)|f(4)))" end;
"| \(.par.graph | sub("netz/V-L4.npz"; "V L=4") | sub("kubisch:"; "kub L=")) | \(.par.lam) | \(.ntraj) | \(pl("m1_cosh"; 4)) / \(ef("m1_cosh"; 1; 4)) | \(ef("E2_pp"; 0; 4)) | \(ef("E3_pp"; 0; 4)) | \(ef("E4_pp"; 0; 4)) | \(ef("E5_pp"; 0; 4)) | \(b("dE2_pp"; 2)) | \(b("dE3_pp"; 3)) | \(b("dE4_pp"; 4)) | \(b("dE5_pp"; 5)) |",
"|   plateau: E2 \(pl("E2_pp"; 4)) dE2 \(pl("dE2_pp"; 4)) E3 \(pl("E3_pp"; 4)) dE3 \(pl("dE3_pp"; 4)) | dE2[t0] \(ef("dE2_pp"; 0; 4)) dE3[t0] \(ef("dE3_pp"; 0; 4)) dE4[t0] \(ef("dE4_pp"; 0; 4)) dE5[t0] \(ef("dE5_pp"; 0; 4)) | akz \(.akzeptanz|f(3)) eDH \(.exp_mdH|f(4))(\(.exp_mdH_fehler|f(4))) tau \([.tau_int[]|.[0]]|max|f(2)) phi2 \(.phi2|f(5))"
