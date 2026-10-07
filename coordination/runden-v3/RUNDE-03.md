# Runde 3 (v3): Chemie und Wellen/Wind/Segeln

Leitung: claude-primary. Begonnen: 2026-09-30 01:19:16 CEST (gemessen). Explorativ, keine formale Bestaetigung.

## Rahmen

- Finn: "mach das alles". Gemeint sind die vorgeschlagenen Tests aus RUNDE-03/IDEEN-20-QBALL-CHEMIE.md und
  RUNDE-03/IDEEN-20-QBALL-WELLEN-WIND-SEGELN.md.
- Die Runde ist deshalb groesser als v3 vorsieht: acht Karten und zwei Zufallskarten statt drei bis fuenf plus eine
  (Fast Lane).
- Jede Rechnung bleibt klein: hoechstens 10 min GPU je Test.
- Laufende Runde 2 (1D-Tests Synchronisation, Absorption, Virus, Radial-VK; Codex Ostwald) wird parallel fertig.

## Karten und Tests

| Karte | Test | wer, wo |
|---|---|---|
| Chemie 1 Elektronegativitaet | 1D: zwei nahe Baelle omega^2 = 0,8 und 0,6; Richtung und Menge des Ladungsflusses | Anthropic 1D-Agent, .69 |
| Chemie 2/3 Bindungskurve und Morse | 1D: E(d, Delta phi) eines Paars bei fester Ladung; Morse-Anpassung, Anharmonizitaet | Anthropic 1D-Agent, .69 |
| Chemie 7 Aktivierungsenergie | 1D: Stoesse, Phasendiagramm verschmelzen/abprallen in (v, Delta phi) | Anthropic 1D-Agent, .69 |
| Chemie 15 Redox ueber Bruecke | 1D: Kette D-B...B-A mit 0 bis 3 Bruecken; Transferrate gegen Brueckenlaenge | Anthropic 1D-Agent, .69 |
| **Chemie 14, Zufallskarte** | 1D: Q-Ball und Anti-Q-Ball im Abstand d; Vernichtungszeit gegen d | Anthropic 1D-Agent, .69 |
| Wellen 5 Rumpfgeschwindigkeit | 1D: Ball mit Geschwindigkeit v durch Hintergrund; Bremskraft gegen v; Schwelle gegen Landau-Kriterium | Anthropic 1D-Agent, .69 |
| Wellen 16 Tropfenschwingung | 2D: grosser duennwandiger Ball, Formstoerung l = 2, 3; Frequenzen gegen Rayleighs Formel (2D-Form) aus sigma und rho des Profils | Anthropic 2D-Agent, .69 |
| Wellen 8/9 Magnus und Flettner | 2D: m = +1 und -1 in gleichmaessiger Hintergrundstroemung; Querdrift | Anthropic 2D-Agent, .69 |
| Wellen 14 Brechung | 2D: schraeger Einfall auf eine Dichtestufe; Brechungswinkel | Anthropic 2D-Agent, .69 |
| **Wellen 20, Zufallskarte** | Papier und Literatur: Knoten-Q-Baelle/Hopfionen; sind sie im Ein-Feld-Modell oder in C x S^2 moeglich? | Anthropic 2D-Agent (Papierteil) |

Zufallskarten gezogen um 01:19:16 mit `shuf -n 1`:
- Chemie: aus den 15 nicht gewaehlten Ideen
- Wellen: aus den 15 nicht gewaehlten Ideen

## Tests: Ergebnisse

Ausgewertet von einem frischen Ernte-Agenten (Anthropic): RUNDE-03/ERGEBNISSE-R3.md, 02:52:48 bis 03:15:06 CEST.
- 1D: t2 in Version 2 (Punktzwang statt Schwerpunkt-Zwang, 30.09. 03:04 auf der .69).
- Die Verluste der Brechung bei 0 und 20 Grad sind als fraglich markiert: Der Ball lag wahrscheinlich schon im Randbereich
  (RUNDE-06/weber/PLAN.md).
- L3 ist in keinem gerechneten Test gerissen; keine Geschwindigkeit liegt ueber c.

Kernzahlen:
- **t2 Chemie 2/3 (Bindungskurve):**
  - Gleichphasig ist die Wechselwirkung bei allen Abstaenden anziehend, gegenphasig abstossend.
  - Das einzige Minimum (d 2,637, Tiefe 0,448) hat Energie, Abstand und omega des verschmolzenen Einzelballs.
  - **Es gibt also keine Bindung mit festem Abstand wie im Molekuel.**
  - Die Asymptotik gleichphasig kappa 0,554 trifft sqrt(1 - omega^2) = 0,548; die Amplitude liegt mit 2,24 statt 4,16
    daneben.
- **t1 Chemie 1:**
  - Bei d = 12 pendelt die Ladung.
  - Bei d = 10 fliesst sie im Mittel vom kleinen zum grossen Ball, wie bei der Ostwald-Reifung (Runde 2).
- **t3 Chemie 7:**
  - Gegenphasige Baelle verschmelzen nie.
  - Langsame gleichphasige enden "gebunden/unklar".
  - Langsame Stoesse mit +-pi/2 prallen ab.
- **t4 Chemie 15:** Die Transferrate faellt nicht exponentiell mit der Brueckenzahl.
- **t5 Chemie 14 (Zufall):**
  - Q und Anti-Q zerstrahlen auch bei d = 8 und 12.
  - Die Ball-Ball-Kontrolle reisst, eine Einzelball-Kontrolle fehlt.
- **Tropfen (2D, Wellen 16):** Rayleighs Tropfenformel ohne freie Parameter auf 6 bis 7 % (Omega/P1 0,94 und 0,93).
- **Brechung (2D, Wellen 14):**
  - 4 von 6 Laeufen folgen Snellius auf 0,03 Grad.
  - 0 und 20 Grad sind fraglich; Weber-Test in RUNDE-06.
- **2D-Profile:** m = 0 sauber; m = 1 durch den Schiessfehler ungueltig (berichtigt in RUNDE-05/r5-2d-a).

## Abschaetzung

Leitung claude-primary, 2026-09-30 03:17:04 CEST (gemessen vor dem Schreiben).

| Karte | Entscheidung | Grund |
|---|---|---|
| Wellen 14 Brechung | **weiter** | als Weber-Test umgebaut (RUNDE-06/weber); dort misst eine saubere Bilanz links, an und rechts der Stufe |
| Chemie 2/3 Bindungskurve | parken, negativ | keine Bindung mit festem Abstand, nur Verschmelzen (gleichphasig) oder Abstossen (gegenphasig). Das schliesst das Molekuel-Bild im Ein-Feld-1D aus; Fables "Torwaechter" ist damit zu |
| Chemie 1 Elektronegativitaet | parken | Fluss klein -> gross passt zur Ostwald-Reifung (Runde 2) |
| Chemie 7 Aktivierung | parken | Phasenabhaengigkeit von Stoessen ist Literatur (L4) |
| Chemie 15 Redox-Bruecke | parken | kein exponentieller Abfall; nichts Tragendes |
| Chemie 14 Anti-Q (Zufall) | parken | Kontrolle reisst; eine Einzel-Anti-Ball-Kontrolle waere noetig |
| Wellen 5 (Papier) | parken | im Ein-Feld keine Landau-Schwelle; Medium-Fassung rechnet M1 |
| Wellen 16 Tropfen | parken, bestaetigt | Rayleigh ohne freie Parameter; in 3D ebenfalls bestaetigt (gebundene l = 2-Mode bei omega^2 = 0,6, RUNDE-06) |
| Wellen 8/9 Magnus/Flettner | parken | im Ein-Feld nicht umsetzbar; Medium-Fassung rechnet M2 |
| Wellen 20 Knoten (Zufall) | verwerfen (Ein-Feld) | ohne Knotenzahl im Ein-Feld; C x S^2 bleibt bei CX-1 geparkt |

- Bilanz: 1 weiter, 8 parken, 1 verwerfen (dazu zwei Grundlagen-Tests).
- Urteil gegen Zufall: Beide Zufallskarten (Chemie 14, Wellen 20) tragen nicht weiter; von den gewaehlten traegt die
  Brechung, und zwar ueber eine Frage, die erst die Auswertung aufgeworfen hat.

## Einfach gesagt

In dieser Runde ging es um Chemie- und Wellenbilder. Das wichtigste Ergebnis ist ein Nein: Zwei Q-Baelle bilden kein
Molekuel mit festem Abstand, sie verschmelzen ganz oder stossen sich ab. Schoen bestaetigt hat sich dagegen das Tropfenbild:
Ein grosser Q-Ball schwingt wie ein Wassertropfen, nach einer ueber hundert Jahre alten Formel. Der vermeintliche starke
Verlust bei der Brechung war wohl ein Messfehler; das pruefen wir mit dem Weber-Test sauber nach.
