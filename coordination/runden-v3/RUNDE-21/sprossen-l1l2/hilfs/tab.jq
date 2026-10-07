# Tabelle je Ziel aus der ausw-Ausgabe (l4 oder test); Zahlen roh, Formatierung im Bericht
def e(x): if x == null then "-" else (x|tostring) end;
def ab(x): if x == null then null else (x|length) end;
.sprossen[] | [
  .ell, .k, .R_ziel, e(.R_gefunden), e(.dR), e(.st1.w2), e(.st1.rho),
  (e(.st1.umlauf) + "/" + e(.st2.umlauf)), (e(.st1.aufgeloest) + "/" + e(.st2.aufgeloest)),
  e(.st1.sprung), e(.st1.punkte), e(.st1.hmax),
  e(if .d_stufen then ([ab(.d_stufen[0]), ab(.d_stufen[1])] | max) else null end),
  (e(.st1.rang) + "/" + e(.st2.rang)),
  e(.st1.fort_fehler), e(.st1.d_nb), e(.st1.verhaeltnis), e(.st2.verhaeltnis), e(.st1.fort_art),
  (e(.st1.absW) + "/" + e(.st2.absW)), (e(.st1.svr) + "/" + e(.st2.svr)),
  (e(.st1.versuch) + "/" + e(.st2.versuch)), (e(.st1.n_versuche) + "/" + e(.st2.n_versuche)),
  e(.st1.knoten_info), (e(.st1.it) + "/" + e(.st2.it)),
  (if .bekannt then ("dw2_N1=" + e(.bekannt.newton_st1.d_w2) + " drho_N1=" + e(.bekannt.newton_st1.d_rho) + " dw2_N2=" + e(.bekannt.newton_st2.d_w2) + " drho_N2=" + e(.bekannt.newton_st2.d_rho) + " uml_bek=" + e(.bekannt.newton_st1.umlauf) + "/" + e(.bekannt.newton_st2.umlauf) + " wie_bek=" + e(.umlauf_wie_bekannt)) else "" end),
  e(.dev_lin), e(.dev_p2), e(.treffer_lin), e(.angenommen),
  e(.st1.pruef), e(.st2.pruef)
] | @tsv
