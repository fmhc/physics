def r4: if . == null then "-" else (.*10000|round/10000|tostring) end;
def pv(k): (.plateau[k] // null) as $p | if $p == null then "-" else "\($p.wert|r4)(\($p.fehler|r4))[\($p.fenster[0])-\($p.fenster[1])]" end;
def e0(k): (.eff[k][0] // [null,null]) as $e | "\($e[0]|r4)(\($e[1]|r4))";
def e1(k): (.eff[k][1] // [null,null]) as $e | "\($e[0]|r4)(\($e[1]|r4))";
"\(.par.graph) T=\(.par.T) lam=\(.par.lam) n=\(.ntraj) akz=\(.akzeptanz|r4) eDH=\(.exp_mdH|r4)(\(.exp_mdH_fehler|r4)) phi2=\(.phi2|r4) tau=\([.tau_int[]|.[0]]|max|r4)",
"  m1=\(pv("m1_cosh")) m1c[t1]=\(e1("m1_cosh")) m1log[t0]=\(e0("m1_log"))",
"  E2=\(pv("E2_pp")) E2g=\(pv("E2_gevp0")) E2[t0]=\(e0("E2_pp"))  dE2=\(pv("dE2_pp")) dE2g=\(pv("dE2_gevp0")) dE2[t0]=\(e0("dE2_pp")) dE2[t1]=\(e1("dE2_pp"))",
"  E3=\(pv("E3_pp")) E3[t0]=\(e0("E3_pp")) dE3=\(pv("dE3_pp")) dE3[t0]=\(e0("dE3_pp"))",
"  E4=\(pv("E4_pp")) E4[t0]=\(e0("E4_pp")) dE4=\(pv("dE4_pp")) dE4[t0]=\(e0("dE4_pp"))  E5[t0]=\(e0("E5_pp")) dE5[t0]=\(e0("dE5_pp"))"
