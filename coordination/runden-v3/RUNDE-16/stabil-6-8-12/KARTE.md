# STABIL-6-8-12: Wo sind 6, 8, 12 wirklich stabil, und wo nur gezaehlt? (Runde 16)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 09:09:32 CEST (date), vor jeder Codezeile.
- Auftrag Finn (02.10., woertlich): "mach weiter. fokus auf die stabilen dingsda - 6er 8er 12er blabla wasgeht".
- Lesart der Leitung, ohne Rueckfrage: Finn meint die Zahlen 6, 8, 12 aus den letzten Ergebnissen und aus seinem Laufplan
  (Tetraeder, 6er, 8er, 11+1 = 12). Das sind:
  - Codex' Automatenperioden 6/8/12
  - Gebilde mit 6, 8 oder 12 Teilen
- Die Karte prueft beides mit vier Stabilitaetsbegriffen.
- Explorativ (v3). Die Leitung rechnet selbst, weil die drei Agentenplaetze belegt sind: kleine Laeufe auf der .69 ueber
  kleintest.sh, Spuren cpu und cpu2.
- Literaturwerte aus dem Gedaechtnis [L?]; sie werden erst nach dem Lauf verglichen.

## S5 Zaehlen statt Stabilitaet: die Perioden 6, 8, 12 (Schreibtisch, Kontrolle per Kurzlauf)

- Ein Rotor-Router mit einem Token hat auf einem zusammenhaengenden Graphen die Periode 2|E|: Jede gerichtete Kante
  wird je Zyklus einmal durchlaufen (Codex FSM-43; bekanntes Lemma).
- Dreieck 6, Quadrat 8, K4 12. Das sind Kantenzaehlungen, keine Stabilitaetsaussage.
- Vorhersage fuer Oktaeder (12 Kanten), Wuerfel (12 Kanten) und Ikosaeder (30 Kanten): 24, 24, 60.

## S1 Federnetze: Welche Nachbarzahl traegt? (gerechnet; Schreibtischwerte vorab)

- Unendliche Gitter mit Federn nur zu den naechsten Nachbarn (ohne Vorspannung, k = m = 1, kubische Kante a = 1).
- Akustischer Tensor A(n) = (1/2) Sum_b (n.R_b)^2 e_b e_b^T. Daraus folgen die elastischen Konstanten (Dichte
  rho = 1 / 2 / 4 fuer sc / bcc / fcc).
- Dazu das volle Spektrum D(q) entlang [110] und das kleinste omega^2/|q|^2 ueber viele Richtungen.

| Gitter | Nachbarn | Schreibtisch (Leitung) | Vorhersage |
|---|---|---|---|
| einfach kubisch (sc) | 6 | C11 = 1, C12 = 0, C44 = 0: Scherung kostet nichts, wackelig | wackelig (99 %) |
| kubisch raumzentriert (bcc) | 8 | C11 = C12 = C44 = 2/3, C' = (C11 - C12)/2 = 0; Nullmode auf der ganzen Linie [110] mit Polarisation [1-10] | wackelig (99 %) |
| kubisch flaechenzentriert (fcc) | 12 | C11 = 2, C12 = 1, C44 = 1, C' = 1/2 | starr (99 %) |
| bcc mit zweiten Nachbarn | 8 + 6 | C' > 0 | starr (95 %) |
| Quadratgitter 2D | 4 | C66 = 0 | wackelig (99 %) |
| Dreiecksgitter 2D | 6 | isotrop, positiv | starr (99 %) |

Deutung vorab [ES]:
- In der Ebene traegt "6 um 1" (Dreiecksgitter), im Raum "12 um 1" (fcc).
- Das sind zugleich die Kusszahlen in 2D (6) und 3D (12) [L?].
- Die 8 (bcc) ist mit reinen Nachbarfedern nicht stabil.
- Passt zu V3 (AUSPROBIEREN): Nur bei N = 6 liegt der Ring mit gleichen Kanten flach und spannungsfrei. Sechs gleichseitige
  Dreiecke um einen Punkt ergeben genau 360 Grad.
  - 3, 4 und 5 Dreiecke ergeben Kappen von Tetraeder, Oktaeder und Ikosaeder, also positive Kruemmung.
  - Ab 7 Dreiecken entsteht ein Sattel, also negative Kruemmung (Defizitwinkel 2 pi - N pi/3, wie im Regge-Kalkuel).

## S3 Ladungen auf der Kugel (Thomson-Problem): magische N

- N gleiche Ladungen auf der Einheitskugel, E = Sum 1/r_ij, globales Minimum fuer N = 2 bis 24.
- Viele Zufallsstarts, lokale Minimierung.
- Stabilitaetsmass: zweite Differenz D2(N) = E(N+1) - 2E(N) + E(N-1). Ein grosses D2 heisst: N ist stabiler als seine
  Nachbarn.
- Dazu: Ist der Wuerfel (N = 8) ein Minimum? Hesse-Matrix auf der Kugel.

Erinnerte Tabellenwerte [L?]: E(4) = 3,674234, E(6) = 9,985281, E(8) = 19,675288, E(11) = 40,596451,
E(12) = 49,165253. Daraus folgen nach Rechnung der Leitung D2(6) = 0,957, D2(8) = 0,862, D2(9) = 0,872, D2(11) = 0,689,
D2(12) = 1,119.

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| S3-1 | Staerkster D2-Gipfel in N = 3..23 bei N = 12 (Ikosaeder) | 90 % |
| S3-2 | N = 6 (Oktaeder) ist lokales D2-Maximum | 90 % |
| S3-3 | N = 8 ist KEIN lokales D2-Maximum. Der Wuerfel ist ein Sattel (negative Richtung); Minimum ist das quadratische Antiprisma | 75 % (Sattel: 98 %) |
| S3-4 | N = 11 ist ein lokales D2-Minimum ("anti-magisch") | 85 % |

## S4 Lennard-Jones-Cluster ("N Teilchen, die sich anziehen und nicht durchdringen"): magische N

- Globale Minima fuer N = 3 bis 24 per Basin-Hopping, dazu D2(N) wie oben (mit Vorzeichen so, dass gross = stabil):
  D2 = E(N+1) + E(N-1) - 2E(N).
- Erinnerte Werte (Cambridge Cluster Database) [L?]: E(13) = -44,326801, E(19) = -72,659782.

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| S4-1 | Lokale D2-Maxima bei 7, 13, 19 und 23 | 85 % |
| S4-2 | Staerkstes bei 13 = 12 + 1 (Ikosaeder mit Mittelteilchen) | 90 % |
| S4-3 | 12 und 20 sind keine lokalen Maxima, 11 auch nicht | 85 % |

## Bedeutung fuer Finns Frage (vorab festgelegt)

- **6:** stabil in der Ebene (Dreiecksgitter) und als Oktaeder auf der Kugel; im Raum als Nachbarzahl allein zu wenig.
- **8:** nirgends besonders. Der Wuerfel ist instabil, bcc wackelt, N = 8 ist nicht magisch.
- **12:** am stabilsten (Ikosaeder, fcc, Kusszahl), aber als 12 + 1 mit Mitte.
- **11:** eher anti-magisch.
- Treffen S1, S3 und S4 so ein, ist die Antwort: Besonders sind 6 (Ebene) und 12 (Raum), weil das die dichtesten
  Nachbarschaften um einen Punkt sind. Die 8 ist es nicht.
- Fallen sie anders aus, gilt die Rechnung, nicht diese Erwartung.

## Rahmen und Kontrollen

- Code: RUNDE-16/stabil-6-8-12/code/, von der Leitung geschrieben. Lauf ueber kleintest.sh (cpu, cpu2), je <= 10 min,
  OMP/BLAS ein Thread.
- S3/S4: Zufallsstarts mit festen Seeds; zwei Durchgaenge mit verschiedenen Seeds muessen dieselben Minima finden
  (auf 1e-6).
- S1: zwei Richtungsstichproben; die Schreibtischwerte muessen auf 1e-10 stimmen.
- Literaturabgleich erst nach dem Lauf.

## Nachtrag S6 (Leitung, geschrieben 2026-10-02 09:15:21 CEST, vor dem S6-Lauf; S1 und S5 waren da schon gerechnet, S3 und S4 liefen)

**S6 Feldklumpen auf Polyedern (unser Feldmodell, diskret):**
- Gleichung wie AUSPROBIEREN V5: Sum_j J (phi_i - phi_j) + (V'(phi_i^2) - omega^2) phi_i = 0, mit
  V' = 1 - 2S + 1,5 S^2. Der Code ist von dort uebernommen (newton, stab, s_branch), der Graph frei waehlbar.
- Graphen:
  - Tetraeder K4 (4 Ecken, Grad 3)
  - Oktaeder (6, Grad 4)
  - Wuerfel (8, Grad 3)
  - Ikosaeder (12, Grad 5)
  - Ring + Nabe fuer N = 4..12: Nabe mit Grad N, Ringknoten mit Grad 3
- Ein Knoten wird bei J = 0 besetzt (beide Aeste der Einzelplatzloesung) und in J fortgesetzt. J_max ist das groesste
  J, bis zu dem die Fortsetzung traegt (Bisektion). Dazu die Stabilitaet bei J_max/2; omega^2 in {0,6; 0,8; 0,9}.

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| S6-1 | Es zaehlt der Grad d des Knotens, nicht die Eckenzahl: J_max d ist je (omega^2, Ast) ueber alle Graphen bis auf 15 % gleich | 80 % |
| S6-2 | Tetraeder und Wuerfel (beide d = 3) haben J_max auf 15 % gleich, trotz 4 gegen 8 Ecken | 85 % |
| S6-3 | Kein Graph mit 6, 8 oder 12 Ecken faellt ueber den Grad hinaus auf | 85 % |
