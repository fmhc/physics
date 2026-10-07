split("\n") | map(select(length>0) | split(" ") | {path: .[1], sha256: .[0]}) as $src | {
  id: "claude-runde-v3-21-20261002",
  time: $t,
  time_kind: "completed",
  author: "claude-primary (Anthropic, Opus 5.5), Leitung, Karten und Abschaetzung; Code- und Literatur-Agenten Anthropic (Opus 5.5)",
  topic: "theory",
  status: "reported",
  evidenzart: "modell",
  title: "Runde 21 nach v3 (explorativ, Fast Lane): Sprossenregel fuer l = 1, 2 vorab bestanden (10 von 10, schrumpfender Abstand 2,6-mal genauer); Phasenregel nur auf reifen Leitern; stille FLS-Leitern nach Recherchestand nicht beschrieben; Klassifikator positiv geeicht; Bio 28 verworfen",
  question: "Sagt die Sprossenregel auch l = 1- und l = 2-Stellen vorab voraus? Erklaert die Phasenbedingung der Innenwelle alle Abstaende? Sind stille Leitern in FLS-Q-Baellen bekannt? Kann der Familien-Klassifikator 'auf' sagen? Teilt sich ein gewachsener Drehball?",
  action: "Karten mit Vorhersagen vor jedem Lauf bzw. Abruf: SPROSSEN-L1L2 (L4-Vorpruefung, P_lin gegen P2), LEITERFORMEL (Delta(k_innen R) = pi an 137 Paaren), FLS-STILLE (Literatur ueber APIs), KF-EICH (exakte Q-Baelle), Zufallskarte Bio 28 weiter.",
  result: "SPROSSEN-L1L2: W0-W4 eingetroffen, erste Sprossen 0,005-0,041, zweite 0,012-0,111; P2 0,015 gegen P_lin 0,039. LEITERFORMEL: LF0/LF1 (80,0 %)/LF3/LF4 eingetroffen, LF2 nicht (62,5 %); Rest positiv, faellt mit R; McMahon- und Versatzkorrektur nachtraeglich [H]. FLS-STILLE: F1-F4 eingetroffen; Abgrenzung Azatov 2412.13885, Zhang/Zhou/Zhu 2510.27064, Oszillon-Dips 2004.01202; Papier LITERATURE.tex zu Azatov berichtigen. KF-EICH: E0/E1 eingetroffen (48 von 48 'auf'), E2 nicht ('auf' heisst Q passt zu omega). Bio 28: verworfen nach Wortlaut, Y1 war ableitbar (Selbstanzeige), Y2 misst Randverlust, Folgefrage Bio 28b.",
  meaning: "Explorativ, keine Messdaten. Der Huellen-Leitermechanismus ist fuer l = 0, 1, 2 je vorab bestanden [H, im Modell gestuetzt] und nach Recherchestand in der FLS-Literatur nicht beschrieben; ob er als Aussage nach aussen ins Leiterpapier soll, entscheidet Finn (dann formaler Test nach v3).",
  sources: $src
}
