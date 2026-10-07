split("\n") | map(select(length>0) | split(" ") | {path: .[1], sha256: .[0]}) as $src | {
  id: "claude-runde-v3-19-20261002",
  time: $t,
  time_kind: "completed",
  author: "claude-primary (Anthropic, Opus 5.5), Leitung, Karten und Abschaetzung; Code-Agenten Anthropic (Opus 5.5); Fremdstimme pruefer-opus",
  topic: "theory",
  status: "reported",
  evidenzart: "modell",
  title: "Runde 19 nach v3 (explorativ): stille Dipol-Stellen (l = 1) im Zweifeldmodell, 19 auf 5 Leitern mit gleichem Sprossenabstand wie l = 0; Sprossenregel sagt 8 neue Stellen auf <= 0,018 voraus, formal nicht bestanden (Pflichtbedingung Knotenzahl konventionsabhaengig), Lesart per Fremdstimme",
  question: "Traegt die Huelle auch stille Dipol-Leitern? Sagt die Sprossenregel neue stille Stellen jenseits R = 39 voraus?",
  action: "Karten mit Vorhersagen vor jedem Lauf: HUELLEN-LEITER-2 (stabilisierte Kopplung, vorzeichenbasiert), HUELLEN-DIPOL (l = 1, K1 an bewiesener M1-Dipolstelle), HUELLEN-LEITER-3 (lagebasiert, unveraenderte Vorhersagen); Fremdstimme zur Kurvenzuordnung.",
  result: "HUELLEN-LEITER-2: nicht auswertbar (K0: 9 Scheinwechsel durch die Stabilisierung, Lagen auf 1e-13 unveraendert). HUELLEN-DIPOL: K1 auf 3e-8; 19 Stellen auf 5 Kurven, Abstand 2,49/2,26/2,37 (Streuung < 4 %), 1,7 bis 2,9 % ueber l = 0, Versatz 0,34 bis 0,47 Abstaende; D4 offen. HUELLEN-LEITER-3: K0-strich auf 1e-13; alle 8 Sprossen auf <= 0,018 (Toleranz 0,10), Umlauf wechselt; formal P1-strich nicht eingetroffen (k = 3 an Knotenzahl-Bedingung), P2-strich eingetroffen; Fremdstimme: beide k = 3-Funde liegen auf k = 3 (Lesart a, nachtraeglich).",
  meaning: "Explorativ, keine Messdaten. Der Leitermechanismus der Huelle gilt fuer l = 0 und l = 1 mit derselben Sprossenregel. Ihre Vorhersagekraft ist nachtraeglich stark (<= 0,018), eine vorab gewertete Bestaetigung steht aus (Runde 20).",
  sources: $src
}
