# Tabelle je Ziel aus ausw-Ausgabe (l4 oder test); Zahlen roh, Formatierung im Bericht
def e(x): if x == null then "-" else (x|tostring) end;
def ab(x): if x == null then null else (x|length) end;
.sprossen[] | [
  .k, .R_ziel, e(.R_gefunden), e(.dR), e(.st1.w2), e(.st1.rho),
  (e(.st1.umlauf_F) + "/" + e(.st2.umlauf_F)), (e(.st1.aufgeloest_F) + "/" + e(.st2.aufgeloest_F)),
  (e(.st1.umlauf_S) + "/" + e(.st2.umlauf_S)),
  e(.st1.sprung_F), e(.st1.punkte_F),
  e(if .d_stufen then ([ab(.d_stufen[0]), ab(.d_stufen[1])] | max) else null end),
  (e(.st1.rang) + "/" + e(.st2.rang)),
  e(.st1.fort_fehler), e(.st2.fort_fehler), e(.st1.d_nb), e(.st1.verhaeltnis), e(.st2.verhaeltnis),
  (e(.st1.absW) + "/" + e(.st2.absW)), (e(.st1.svr) + "/" + e(.st2.svr)),
  (e(.st1.versuch) + "/" + e(.st2.versuch)), (e(.st1.n_versuche) + "/" + e(.st2.n_versuche)),
  e(.st1.knoten_info), e(.st1.it),
  (if .bekannt then (e(.bekannt.quelle) + " dw2=" + e(.bekannt.d_w2) + " drho=" + e(.bekannt.d_rho) + " uml=" + e(.bekannt.umlauf_bekannt)) else "" end),
  e(.nicht_blind), e(.treffer), e(.angenommen),
  e(.st1.pruef), e(.st2.pruef)
] | @tsv
