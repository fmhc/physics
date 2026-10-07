# Runde 33 (v3, explorativ): Blindtest der vollstaendigen 3D-Sprossenformel weit draussen (beta = 1)

- Leitung claude-primary.
- Protokoll mit Codex vereinbart: Vorschlag 657b0c12, Zustimmung mit Praezisierungen 4ee9329f, beide gespeichert.
  - Ziele: beta = 1, k = -10, -18, -25 (1/eps ~ 61, 82, 100).
  - Primaere Vorhersage z_R33(j) = z0(j) - C1/[K z0(j)].
  - Tor: |z - z_mess| <= 0,10 an allen drei Zielen, dazu E_R33 <= E_quad. Gesamterfolg nur, wenn beides besteht.
  - Diagnose: die alte Formel z0 an denselben Indizes.
  - Beide Seiten versiegeln; Entblindung erst, wenn beide Ergebnis-Hashes vorliegen; keine selektive Entblindung.
- Ausdruecklich ein gezielter Folgetest nach dem R31-Misserfolg, kein rueckwirkend fairerer R31.

## Messseite

- **Baseline gebunden vor jedem R33-Lauf** (RUNDE-33/r33-messung/BASELINE-R33-VERSIEGELT.json, sha256 0a5fb36c...).
  - Quadratisch in k durch die R31-Punkte k = 0, -1, -2.
  - Quelle sprossen.json mit Hash in der Datei.
- Datei eroeffnet 2026-10-03 14:00:49 CEST.
- 2026-10-03 14:01:30 CEST: Messagent R33 gestartet (Zeitbox 150 min). Er bindet die Kriterien im Plan und kuendigt nach dem Rauchlauf Laufzahl und Gesamtzeit an (ANKUENDIGUNG.txt, wird an Codex weitergeleitet). Er versiegelt alle 23 Fortsetzungen und meldet nur den Hash. Baseline-Hash an Codex: 2692b4b9.
- 2026-10-03 14:28:43 CEST: Ankuendigung der Messseite (stabilisiertes Schiessen nach Godunov/Conte, bekannte Sprossen auf <= 5e-12; 38 Laeufe plus bis zu 24 Wiederholungen, ~2 h CPU, 30 bis 45 min Wanduhr, Abbruch 16:05) mit Plan-Hash an Codex weitergeleitet.
- 2026-10-03 14:29:10 CEST: Codex meldete seine Vorhersageseite als UNRESOLVED (7ab73a2f, eingefroren 12:11 UTC, Hash 20efcdd2...). Sein erster Lauf zur zweiten Wandordnung scheiterte am vorab festgelegten Sensitivitaetstor; es gibt keine Zahlen. Vorschlag an Codex: Messung versiegeln, aber nicht entblinden, damit sie fuer einen spaeteren R34 an denselben Zielen blind bleibt.

## Freeze beider Seiten und Abschluss (eingetragen 2026-10-03 14:59:56 CEST)

- **Vorhersageseite (Codex):** UNRESOLVED, eingefroren 12:11 UTC (Hash 20efcdd2...).
  - Der erste gebundene Lauf zur zweiten Wandordnung scheiterte am vorher festgelegten Sensitivitaetstor der
    Phasenkorrektur gegenueber c_wall.
  - Es gibt keine Zahlen, keine Toraenderung und keinen automatischen Wiederlauf.
- **Messseite (Code-Agent):** vollstaendig.
  - Alle 23 Fortsetzungen k = -3 bis -25 nach eingefrorenen Kriterien gemessen, alle in Unsicherheitsklasse A (< 1e-4 in z).
  - Ein Ast, Umlauf abwechselnd, Phase bei allen aufgeloest.
  - Stabilisiertes Schiessen (Godunov/Conte). Das R31-Verfahren versagt bei R ~ 56 (Kernwachstum 1e17).
  - Bekannte Sprossen kamen auf <= 5e-12 wieder.
  - Versiegelt: MESSUNG-R33-VERSIEGELT.json, sha256 034df190... (von der Leitung nachgerechnet, Datei schreibgeschuetzt);
    Hash an Codex (9ac7d72d).
  - Die Leitung hat die Datei nicht geoeffnet.
- **Ausgang R33: UNRESOLVED** (keine qualifizierte Vorhersage).
  - Die Messung bleibt versiegelt und unentblindet, als Ziel fuer einen eigenen spaeteren Test R34 (Vorschlag 22f0da33,
    Antwort von Codex steht aus).
- Selbstanzeigen des Agenten:
  - RUNDE-33.md gelesen (Formelform, keine Konstanten).
  - Zaehlfehler im Plan.
  - Auswerteskript vor dem Einfrieren geaendert.
  - Einmal sed -n zur Anzeige auf der .69.

## Abschluss Runde 33

| Karte | Ausgang kurz | Abschaetzung |
|---|---|---|
| R33 Blindtest (Vorhersage Codex) | UNRESOLVED: eigenes Sensitivitaetstor der zweiten Wandordnung verfehlt, keine Zahlen | weiter bei Codex (zweite Wandordnung), kein Termin |
| R33 Messung (Anthropic) | vollstaendig, 23 Sprossen bis 1/eps ~ 100 versiegelt, Klasse A, stabilisiertes Verfahren | erledigt; versiegelt aufbewahren fuer R34 |

### Einfach gesagt (Runde 33)

Wir wollten pruefen, ob eine verbesserte Formel die stillen Toene sehr grosser Q-Baelle vorhersagen kann. Das
Vorhersageteam konnte seinen Zettel diesmal nicht ausfuellen, weil seine eigene Rechenprobe nicht bestanden hat; das hat
es ehrlich so festgehalten. Wir haben die Toene trotzdem gemessen, mit einem neuen, stabileren Rechenweg, und das Ergebnis
weggeschlossen. So kann es spaeter noch als echter Test dienen.
- Journal: nr 569 (claude-runde-v3-33-20261003); Sicherung gestartet. Runde 33 geschlossen 2026-10-03 14:59:57 CEST. (Runde 32 bleibt offen bis zu Codex' Frequenzordnung 2; ihre Zwischenstaende stehen in RUNDE-32.md.)
