split("\n") | map(select(length>0) | split(" ") | {path: .[2], sha256: .[0]}) as $src | {
  id: "claude-runde-v3-35-20261003",
  time: $t,
  time_kind: "completed",
  author: "claude-primary (Anthropic, Opus 5.5), Leitung, Karten, Schreibtisch; Code-Agenten, pruefer-opus (Gegenleser) und feldforscher Anthropic (Opus 5.5)",
  topic: "theory",
  status: "reported",
  evidenzart: "modell",
  title: "Runde 35 nach v3 (explorativ): Peitsche im Feld (Wand bis Energiefluss 0,99983, Muster > c), Stabnetze mit mehreren Wellengeschwindigkeiten (abgestimmt isotrop moeglich), Strings entstehen und reissen (OZ 1/2 ln r), Tensor-Eis stoesst gleiche Ladungen ab, Q-Ball auf Gitter stoppt bei v_g,max; Literatur: Spin 2 aus Laengen (Regge) oder Tensorfluss, Anziehung braucht indefiniten Quellsektor (Gu/Wen N-Typ)",
  question: "Erreichen Peitschen bzw. Q-Baelle Lichtgeschwindigkeit? Hat ein Stabnetz eine Lichtgeschwindigkeit? Entstehen aus Punkten Strings, die reissen? Gibt ein Tensor-Eis Schwerkraft? Wie kommt man aus Punkten, Strichen, Dreiecken zur Spin-2-Kopplung (Finn)?",
  action: "Karten PEITSCHE-1, NETZ-C-1, STRING-1, TENSOR-EIS-0, QBALL-GITTER-1 mit Vorhersagen vor jeder Rechnung (Code-Agenten auf der .69); Schreibtisch QBALL-EIS, LAPSE-0, AEQ-0; frischer Gegenleser (27 Befunde) und Berichtigung; Literaturdossier GRAVITON-NETZ-L (feldforscher, 25 gezielte Abrufe, Websuche gesperrt).",
  result: "PEITSCHE-1: A0-A4, B0-B2 ja, A5, B3 nein; v(R) nach Duennwand, Nullstelle ab R ~ 0,8 sqrt(R0) superluminal (Muster); innerer Energiefluss drehender Q-Baelle 0,365 bis 0,498. NETZ-C-1: 7 von 10; Spanne >= 1,27 in vier Netzen, Kink-gamma 1,78/2,61/3,86 bei F = 0,02. STRING-1: S0-S2, S5, S6 ja; a = 0,4955 (2D), Bruch r_c = 10,47 (1D) und 4,57 (3D). TENSOR-EIS-0: Formeln auf 3e-15 bestaetigt, gleiche Vektorladungen stossen ab; T0, T2, T3 woertlich nein (Torus-Hintergrund, Kartenfehler). QBALL-GITTER-1: gamma_max = 1,609/2,133/2,913 = gamma(v_g,max), kraftunabhaengig, Ladung zerstrahlt. GEGENLESEN: 2 hoch, 9 mittel, 16 niedrig. Dossier: E1, E3, E4 ja, E2, E6 im Kern, E5 teilweise.",
  meaning: "Explorativ, keine Messdaten. In Finns Netzbild geben Fluss- und Tensorregeln mit positiv definitem Quellsektor Elektrostatik, keine Schwerkraft; Anziehung gleicher Quellen braucht einen indefiniten Quellsektor oder Geometrie (Regge, Laengen als Feld). Netzwellen als Licht sind nur unter Bedingungen moeglich (Laengswelle, Abstimmung, Dispersion). Auf einem Gitter sind Teilchen relativistisch nur bis zur schnellsten Gitterwelle [H: Bezug zu UHECR, Zusammensetzung offen].",
  sources: $src
}
