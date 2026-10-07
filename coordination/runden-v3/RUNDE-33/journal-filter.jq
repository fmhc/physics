split("\n") | map(select(length>0) | split(" ") | {path: .[2], sha256: .[0]}) as $src | {
  id: "claude-runde-v3-33-20261003",
  time: $t,
  time_kind: "completed",
  author: "claude-primary (Anthropic, Opus 5.5), Leitung, Protokoll, Baseline; Code-Agent Anthropic (Opus 5.5) Messung; Codex (OpenAI) Vorhersageseite",
  topic: "theory",
  status: "reported",
  evidenzart: "modell",
  title: "Runde 33 nach v3 (explorativ): zweiseitig versiegelter Blindtest der 3D-Sprossenformel bei beta = 1 weit draussen UNRESOLVED (Codex' zweite Wandordnung verfehlte ihr eigenes Sensitivitaetstor); Messung von 23 Sprossen bis 1/eps ~ 100 mit stabilisiertem Verfahren vollstaendig und versiegelt aufbewahrt",
  question: "Trifft die um die naechste Ordnung ergaenzte parameterfreie Formel die Sprossen k = -10, -18, -25 (1/eps ~ 61, 82, 100) bei beta = 1 auf 0,10 und besser als eine quadratische Fortschreibung?",
  action: "Protokoll mit Codex vereinbart (Tore vorab, beidseitige Versiegelung, keine selektive Entblindung); Baseline vor jedem Lauf gebunden (0a5fb36c...); Messagent mit eingefrorenem Plan und stabilisiertem Schiessen (Godunov/Conte), alle Fortsetzungen k = -3 bis -25; beide Hashes per Peerbus.",
  result: "Vorhersageseite UNRESOLVED (eigenes Sensitivitaetstor verfehlt, keine Zahlen, eingefroren 12:11 UTC, Hash 20efcdd2...). Messseite vollstaendig: 23 Fortsetzungen in Unsicherheitsklasse A (< 1e-4 in z), bekannte Sprossen auf <= 5e-12 wiedergefunden, versiegelt (Hash 034df190...). Ausgang R33: UNRESOLVED.",
  meaning: "Explorativ, keine Messdaten. Kein Befund zur Formel. Die versiegelte Messung bleibt unentblindet als Ziel fuer einen eigenen spaeteren Test; methodisch neu ist das stabilisierte Schiessen, das die Leiter bis R ~ 50 traegt, wo das bisherige Verfahren versagt.",
  sources: $src
}
