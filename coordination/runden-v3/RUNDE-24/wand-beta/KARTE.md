# WAND-BETA: Hat die ebene Q-Ball-Wand auch bei anderem beta eine stille Frequenz? (Runde 24)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 01:01:42 CEST (date), vor jeder Rechnung.
- Herkunft: TROPFEN-LEITER (R23) und die blinde Codex-Nachrechnung.
  - Die ebene M1-Wand (beta = 1/2) hat bei rho_z = 1,5241497621 eine Transmissionsnullstelle. Daraus folgt der
    Sprossenabstand b_inf = 2,3100 (Papier I v0.40).
- **Offene Projektfrage:** RUNDE-10/nls-leiter, Abschnitt 7: "Gibt es die Leiter im Klein-Gordon-Modell auch bei beta = 1
  und 2?" Die Eck-Umlaeufe dort waren unzuverlaessig, die Frage blieb unentschieden.
- **Projekt-grep (fuenfte Probe, neu seit heute)** nach "Wandzustand", "ebene Wand", "transmission", "kanal-qb-beta":
  - RUNDE-10 und RUNDE-12: nackter Wandzustand im geschlossenen Kanal, E = 0,706247 bei beta = 1/2 (K2 in RUNDE-12).
    Fuer beta = 1, 2, 4 liegt er bei E = 0,84 bis 0,86, 0,92 bis 0,93 bzw. 0,96, jeweils bei Q-Baellen mit omega
    oberhalb omega_min, Kontinuum ab 1.
  - Eine Transmissionsrechnung der ebenen Wand bei beta ungleich 1/2 gibt es im Projekt nicht.
- **Schreibtisch der Leitung:**
  - Fuer U = S - S^2 + beta S^3 ist omega_min^2 = 1 - 1/(4 beta) und S_c = 1/(2 beta).
  - Ebener Knick: S(x) = S_c/(1 + exp(x/sqrt beta)).
  - Kanalpotential: W = 1 - 4S + 9 beta S^2, mit W_min = 1 - 4/(9 beta) und W_innen = 1 + 1/(4 beta). Kopplung:
    C = -2S + 6 beta S^2, innen 1/(2 beta).
  - Bei beta = 1/2 liegt die Nullstelle bei E_z = (rho_z - omega)^2 = 0,6676, also 0,0387 unter dem nackten Wandzustand
    (0,7062). Das passt zum Fano-Bild: Die Nullstelle sitzt neben dem Wandzustand, verschoben durch die Kopplung.
- Ableitbarkeitspruefung: Die Nullstellen bei beta ungleich 1/2 folgen aus keiner Datei. Die nackten Zustaende von
  RUNDE-10 sind bei omega > omega_min gerechnet; die ebenen werden hier neu gerechnet.

## Test (Leitung rechnet selbst; Code wand_beta.py, abgeleitet von wand_transmission_v3.py)

- beta aus {0,5 (Kontrolle); 0,75; 1; 2; 4}, jeweils ebene Wand bei omega_min(beta).
- **(i) Transmissionsnullstellen** im Fenster (1 - omega, 1 + omega):
  - Abtastung von c_in, Schritt 0,002; fuer die Kontrolle beta = 0,5 nur [1,40; 1,65].
  - Verfeinerung per brentq; Gegenprobe per Randwertproblem (zwei h, Richardson).
- **(ii) Nackte Wandzustaende** des geschlossenen Kanals: -A'' + W(x) A = E A, alle gebundenen E < 1 (Differenzen,
  Dirichlet, h = 0,005).
- Je beta berichtet: E_z = (rho_z - omega)^2, der Abstand zum tiefsten nackten Zustand E_0, k_in(rho_z) und
  b_inf = 2 sqrt(beta) pi/k_in.
- K0: Hintergrundrest analytisch, Innen-Dispersion gegen die Papierformel (D_c = 1 + 1/(4 beta), C_c = 1/(2 beta)),
  Flussbilanz.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| WB0 | Kontrolle beta = 1/2: rho_z auf 1e-8 wie R23 (1,5241497621), E_0 auf 1e-4 wie R12 (0,706247) | 90 % |
| WB1 | beta = 0,75, 1, 2, 4: je genau eine Nullstelle im Fenster | 55 % |
| WB2 | Fuer jedes beta mit Nullstelle: E_z < E_0 und E_0 - E_z < 0,06 | 50 % |
| WB3 | E_z steigt mit beta (ueber 0,5; 0,75; 1; 2; 4) monoton und bleibt < 1 | 65 % |

**Bedeutung (vorab):**
- WB1 und WB2 treffen ein:
  - Die ebene Stille ist fuer alle gerechneten beta eine Fano-Nullstelle neben dem nackten Wandzustand.
  - Radiale Leitern sollten dann im Duennwandgrenzfall auch bei beta = 0,75 bis 4 existieren [H]. Damit ist RUNDE-10s
    offene Frage auf ebener Stufe beantwortet.
  - b_inf(beta) ist die Vorhersage fuer eine spaetere radiale Pruefung.
- WB1 trifft fuer ein beta nicht ein (keine Nullstelle): Dort gibt es keine ebene Stille und damit keine
  Duennwand-Leiter [H].
- WB2 trifft nicht ein: Die Nullstelle ist nicht eng an den nackten Zustand gebunden. Beschreiben.

## Rahmen

- Explorativ (v3). Die Leitung rechnet auf der .69 (kleintest.sh, CPU-Spuren, je Lauf <= 10 min); grosse beta in zwei
  Teilfenstern.
- Rauchlauf mit beta = 0,6, das in keinem echten Lauf vorkommt.
- Danach Karte und Code einfrieren (*.eingefroren-<zeit>, schreibgeschuetzt).

## Laufplan (Nachtrag vor jedem echten Lauf, 2026-10-03 01:05:18 CEST)

- Rauchlauf beta = 0,6, [1,50; 1,52], n = 3: rc = 0, K0-Rest 1,9e-16, Dispersion 2,2e-15, Flussbilanz 4e-12, ein nackter
  Zustand.
- Laeufe (Schritt 0,002, Teilfenster ueberlappen am Rand):

| Name | beta | Fenster | n |
|---|---|---|---|
| b05 | 0,5 | [1,40; 1,65] | 126 |
| b075 | 0,75 | [0,185; 1,815] | 816 |
| b1 | 1 | [0,135; 1,865] | 866 |
| b2a / b2b | 2 | [0,066; 1,000] / [1,000; 1,934] | 468 / 468 |
| b4a / b4b | 4 | [0,033; 1,000] / [1,000; 1,967] | 484 / 484 |

- Auswerteregeln (mechanisch):
  - Nullstelle: Vorzeichenwechsel von c_in, verfeinert mit brentq. Doppelte Treffer an Teilfenster-Grenzen zaehlen
    einmal.
  - E_0 ist der tiefste nackte Zustand (E < 1).
  - WB0: |rho_z - 1,5241497621| < 1e-8 und |E_0 - 0,706247| < 1e-4.
  - WB1: genau eine Nullstelle je beta im gueltigen Fenster (die Abtastfenster reichen bis 0,002 an die Grenzen).
  - WB2: E_z < E_0 und E_0 - E_z < 0,06 je beta mit Nullstelle.
  - WB3: E_z(0,5) < E_z(0,75) < E_z(1) < E_z(2) < E_z(4) < 1. Bei mehreren Nullstellen je beta gilt die mit dem kleinsten
    E_0 - E_z >= 0.
