# WAND-BETA: Ergebnis (Leitung, Runde 24, explorativ)

- Gerechnet von der Leitung auf der .69 (kleintest.sh, CPU-Spuren):
  - sieben gewertete Laeufe 23:05:19 bis 23:14:54 UTC (01:05 bis 01:15 CEST), alle rc = 0, je 27 bis 232 s
  - danach drei nachtraegliche Gegenproben 23:16 bis 23:21 UTC: Feinabtastung, Sekante, diskretes Schiessen
- Karte und Code eingefroren 01:05:18 (KARTE.md.eingefroren-20261003-010518, code/wand_beta.py.eingefroren-...).
- Auswertung mit jq auf lauf-69/ und nach-69/. Geschrieben ab 01:21 CEST (date).

## Ergebnis zuerst

1. **Die ebene Q-Ball-Wand hat bei jedem gerechneten beta genau eine stille Frequenz** (WB1 eingetroffen).

| beta | omega_min | rho_z | E_z = (rho_z - omega)^2 | nackter Zustand E_0 | E_z - E_0 | k_in | b_inf = 2 sqrt(beta) pi/k_in |
|---|---|---|---|---|---|---|---|
| 0,5 | 0,70711 | 1,5241497621 | 0,66756 | 0,63883 | +0,0287 | 1,92332 | 2,3100 |
| 0,75 | 0,81650 | 1,6927204866 | 0,76777 | 0,75922 | +0,0085 | 2,24546 | 2,4233 |
| 1 | 0,86603 | 1,7734530718 | 0,82342 | 0,81942 | +0,0040 | 2,39943 | 2,6186 |
| 2 | 0,93541 | 1,8896237546 | 0,91052 | 0,90971 | +0,00081 | 2,62005 | 3,3914 |
| 4 | 0,96825 | 1,9455067381 | 0,95504 | 0,95485 | +0,00018 | 2,72572 | 4,6103 |

2. **Die Nullstelle sitzt knapp oberhalb des nackten Wandzustands.**
   - Der Abstand schrumpft mit wachsendem beta, am Ende etwa wie beta^-2 (Faktor 4,4 von beta = 2 auf 4).
   - Das passt zum Fano-Bild: Die Verschiebung waechst mit dem Quadrat der Kopplung C_in = 1/(2 beta) [H, nachtraeglich].
   - WB2 verlangte "unterhalb" und ist deshalb nicht eingetroffen (Abschnitt Vorab gegen Ausgang).
3. **Der Bereich um die Nullstelle wird mit wachsendem beta extrem schmal.**
   - Die Durchlaessigkeit faellt bei beta = 1 nur in einem Fenster der Breite ~1e-5 ab, bei beta = 2 ~5e-9, bei beta = 4
     unter 1e-9; ausserhalb ist die Wand fast durchsichtig.
   - Deshalb fanden die Minimierung von T (beta = 2, 4) und die Sekante (beta = 4) den Einbruch nicht.
   - Das diskrete Schiessen im Randwertmodell bestaetigt alle fuenf Nullstellen, mit Abstaenden der Ordnung h^2 zum
     Schiessen: -2,4e-8, -6,3e-9, -1,4e-9, -3,5e-10 und, bei h = 0,001, -8,7e-11.
4. **E_z steigt monoton mit beta** (WB3 eingetroffen) und naehert sich 1. Je nichtrelativistischer der Q-Ball, desto
   naeher liegt die Stille an der Schwelle des geschlossenen Kanals und desto schmaler ist sie. Das passt zu RUNDE-10: Die
   NLS-Naeherung schneidet den Antiteilchen-Zweig ab [H].
5. **Vorhersage fuer radiale Leitern** (aus der Ebene, ohne Eichung):
   - Abstaende in 1/eps: 2,4233 (beta = 0,75), 2,6186 (1), 3,3914 (2), 4,6103 (4).
   - Nach dem Mechanismus muessten radiale Duennwand-Leitern dort existieren [H]. Das beantwortet RUNDE-10s offene Frage
     auf ebener Stufe, nicht radial.

## Vorab gegen Ausgang

| Nr | Vorhersage | Ausgang |
|---|---|---|
| WB0 | rho_z(1/2) auf 1e-8 wie R23 und E_0 auf 1e-4 wie R12 (0,706247) | **nicht eingetroffen (E_0)**. rho_z stimmt auf < 1e-10, E_0 ist aber 0,63883. Der R12-Wert war kein ebener nackter Zustand (Selbstanzeige 1) |
| WB1 | beta = 0,75, 1, 2, 4: je genau eine Nullstelle | **eingetroffen** |
| WB2 | E_z < E_0 und E_0 - E_z < 0,06 | **nicht eingetroffen**: E_z liegt in allen Faellen oberhalb (Abstand +0,0287 bis +0,00018) |
| WB3 | E_z monoton steigend, < 1 | **eingetroffen**: 0,6676 < 0,7678 < 0,8234 < 0,9105 < 0,9550 < 1 |

**Bedeutung (vorab festgelegt):**
- Die Zeile "WB1 und WB2" ist nicht ausgeloest. Ausgeloest ist "WB2 trifft nicht ein: Die Nullstelle ist nicht eng an den
  nackten Zustand gebunden. Beschreiben."
- Beschreibend: Die Nullstelle ist sehr eng an den nackten Zustand gebunden (|E_z - E_0| <= 0,029, mit beta fallend),
  aber auf der anderen Seite als vorhergesagt.
- Das Vorzeichen der Vorhersage stammte aus dem falschen Bezugswert (WB0), nicht aus einer Rechnung.
- WB1 allein: Die ebene Stille gibt es bei allen gerechneten beta.

## Kontrollen

- K0:
  - Hintergrundrest <= 3,3e-16, Innen-Dispersion gegen die Papierformel <= 2,7e-15
  - W_min numerisch gleich 1 - 4/(9 beta) bis 1e-6, Flussbilanz <= 1,1e-9
- Gegenproben je Nullstelle (Schiessen): rtol 1e-9 und Gebiet +10 verschieben um <= 7e-14.
- Gegenprobe Randwertproblem:
  - Minimierer: Richardson trifft bei beta = 0,5, 0,75, 1 auf <= 1,3e-8.
  - Bei beta = 2 und 4 findet er den schmalen Einbruch nicht (nachtraeglich erklaert, Punkt 3).
  - Das diskrete Schiessen bestaetigt alle (nach-69/d*.json).
- Die Feinabtastung bei beta = 2 (+-2e-7, 401 Punkte) zeigt den Einbruch am geschossenen Ort; T faellt auf 5e-3 bei einem
  Abtastschritt von 1e-9.

## Latten (v3)

- L1: ja (WB0 und WB2 sind gescheitert).
- L2: ja (drei Verfahren).
- L3: ja (zwei Schrittweiten, Toleranzen, Gebiete).
- L4: teilweise.
  - Projekt: RUNDE-10 nackte Zustaende bei omega > omega_min, Papier I v0.40 bei beta = 1/2.
  - Literatur zur beta-Abhaengigkeit nicht gesucht (Websuche erschoepft).
- L5: teilweise. Ebene Stille fuer beta = 0,75 bis 4 und vorhergesagte Leiterabstaende sind im Projekt neu; der radiale
  Nachweis fehlt.

## Selbstanzeigen

1. **WB0:** Den Bezugswert 0,706247 habe ich aus RUNDE-12 (K2, "KG-Wandzustand ziffergleich zu R10") uebernommen, ohne
   zu pruefen, in welchem Aufbau er gerechnet war. Er gehoert nicht zur ebenen Wand bei omega_min. Daraus folgte auch das
   falsche Vorzeichen in WB2.
2. Die Gegenproben 2 und 3 (Sekante, diskretes Schiessen) entstanden nach den Laeufen und aendern keine Urteile. Sie
   sind als nachtraeglich gekennzeichnet; die Codes liegen in code/fd_fein.py, fd_sekante.py und fd_schiessen.py.
3. Der Rauchlauf bei beta = 0,6 zeigte vor dem Einfrieren einen nackten Zustand bei 0,699, aber keine Nullstelle (das
   Fenster war zu klein).

## Einfach gesagt

Die Wand eines Q-Balls wirft bei genau einer Frequenz alles zurueck, und zwar nicht nur fuer das bisher gerechnete Modell,
sondern fuer alle Varianten, die wir durchprobiert haben. Diese Frequenz liegt immer dicht neben einem Zustand, der an
der Wand "festsitzt". Je naeher das Modell an die langsame, nichtrelativistische Welt kommt, desto schmaler wird das
Fenster, in dem die Wand dicht ist: am Ende kleiner als ein Milliardstel. Daraus koennen wir vorhersagen, wo bei diesen
Varianten stille Sprossen liegen muessten; gerechnet sind diese Sprossen noch nicht.
