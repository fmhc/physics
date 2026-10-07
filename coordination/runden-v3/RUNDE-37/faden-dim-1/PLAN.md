# FADEN-DIM-1: Plan des Code-Agenten (Runde 43)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 19:22:00 CEST (date), Zeitbox 90 min.
  Plan geschrieben ab 19:39:03 CEST (date), nach dem Rauchtest (nur Laufzeiten gesehen), vor jeder Rechnung zu
  Treffanteilen oder D*.
- Gelesen: KARTE.md (ganz); RUNDE-37/dim-auswahl-l/DOSSIER.md Z. 200-319 (Abschnitt 5.5 FADEN-DIM-1 ganz, dazu
  Abschn. 6 bis 8 in Auszuegen); AGENTS.md Z. 127-138 (Dimensionsvergleich); Laufform aus RUNDE-37/verschraenk-dim-1/
  (PLAN.md, EINGEFROREN-SHA256.txt, lauf-69/s1.log, PRUEFSUMMEN.txt).
- Ordner: lokal RUNDE-37/faden-dim-1/ (code/, lauf-69/); .69: /home/fmh/fmhc-physics-remote/faden-dim-1/ (code/, lauf/,
  rauch/).
- Kennzeichen: [E] gerechnet (.69), [M] eigene Mathematik von Hand (nicht gegengelesen), [L] Gedaechtnis/Literatur
  ohne Abruf, [S] an der Quelle gelesen, [H] Hypothese, [F] Festlegung dieses Plans (nicht aus der Karte), [D] Diagnose
  (beschreibend, ohne Urteil).
- Vorhersagen und Wahrscheinlichkeiten der Karte (F1 85 %, F2 35 %) bleiben unveraendert. Kein Literaturabruf.

## 1. Modell [F]

**Netz und Faeden.** Hyperkubischer Torus Z_L^D, D = 2 bis 6, Kantenlaenge L in allen Richtungen. Ein Paar
geschlossener Faeden A (Windung +1 um Richtung 1) und B (Windung -1). Darstellung als gerichteter Faden mit
RSOS-Bedingung:
- Je Spalte x = 0..L-1 eine Querlage y[x] in Z_L^(D-1); Nachbarspalten unterscheiden sich um hoechstens einen
  Einheitsschritt (|y[x+1] - y[x]|_1 <= 1). Der Gitterweg ist (x, y[x]) -> (x, y[x+1]) -> (x+1, y[x+1]); der Faden
  belegt also in Spalte x die Knoten y[x] und y[x+1]. Die Windung um Richtung 1 ist damit fest +1 bzw. -1; der Umlauf
  hat Querverschiebung 0.
- **Treffen** (Karte: "Teilen sie einen Knoten, vernichten sie sich"): Es gibt eine Spalte x, in der sich
  {yA[x], yA[x+1]} und {yB[x], yB[x+1]} schneiden. Geprueft wird nach jedem Teilzug. Ein Durchdringen ohne
  gemeinsamen Knoten ist nicht moeglich [M]: Ein lokaler Zug ueberstreicht genau eine Plakette, eine starre
  Verschiebung einen Plakettenstreifen; Gitterkanten schneiden das Innere einer Plakette nicht, also muesste der
  andere Faden einen alten (schon gemeldeten) oder neuen (dann gemeldeten) Knoten besitzen.
- Die Fadendicke w ist 1 Gitterabstand.

**Rauheit ueber Biegesteifigkeit.** Energie E = J K, K = Zahl der Knicke (Querschritte). Jeder Knick hat zwei
90-Grad-Biegungen, J = 2 kappa mit Biegesteifigkeit kappa je Biegung. Die Rauheit wird als Ziel-Knickdichte p gesetzt;
kappa folgt je D aus exp(-2 kappa) = p / (2 (D-1) (1-p)) (exakt fuer die freie RSOS-Kette) [M]. Grund: AGENTS.md
verlangt, Schwellen nicht unveraendert zwischen Dimensionen zu uebertragen; gleiches kappa gaebe in D = 6 eine viel
rauere Kette als in D = 2.

| p | kappa D=2 | D=3 | D=4 | D=5 | D=6 |
|---|---|---|---|---|---|
| 0,2 | 1,040 | 1,386 | 1,589 | 1,733 | 1,844 |
| 0,6 | 0,144 | 0,490 | 0,693 | 0,837 | 0,949 |

(Von Hand [M]; der Code rechnet und speichert kappa selbst.)

**Bewegungsarten.**
- **G (glatt, Karte):** starre gerade Faeden. Je Schritt wird A um einen Einheitsschritt in eine zufaellige
  Querrichtung (+-e_j, j = 2..D) verschoben, Treffpruefung, dann B ebenso, Treffpruefung.
- **RL (rau, Kartenwortlaut):** nur lokale Metropolis-Zuege. Zug an Spalte x: y[x] -> y[x] +- e_j, nur wenn die
  RSOS-Bedingung zu beiden Nachbarn haelt; Annahme min(1, exp(-J dK)). 1 Schritt = 1 Sweep: jede Spalte jedes Fadens
  bekommt genau einen Versuch, in Halbsweeps (gerade, dann ungerade Spalten; Reihenfolge A gerade, B gerade, A ungerade,
  B ungerade; Treffpruefung nach jedem Halbsweep). Die Halbsweep-Form ist eine gueltige Metropolis-Dynamik mit
  derselben Gleichgewichtsverteilung; Zuege derselben Paritaet beruehren getrennte Knotenmengen, ein Treffen innerhalb
  eines Halbsweeps kann also nicht wieder verschwinden [M]. Verlangt gerades L.
- **RP (rau, Plan):** je Schritt erst die starre Verschiebung von A und B wie in G (mit Treffpruefung), dann ein Sweep
  wie in RL. Fuer p -> 0 (kappa -> unendlich) ist RP exakt G.

**Abweichung von der Karte und Begruendung (RP).** Die Karte nennt fuer (R) nur lokale Metropolis-Zuege. Mit nur
lokalen Zuegen diffundiert der Schwerpunkt eines Fadens je Sweep nur um ~ 1/L (Rouse) [M]. In T = 4 L^2 Sweeps
kommt der Abstand der Schwerpunkte also nur um ~ L^(1/2) voran, die Faeden selbst sind ~ (p L)^(1/2) breit; bei
zufaelliger Startlage (Abstand ~ L) sollte der Treffanteil dann in jeder Dimension mit L fallen, auch in D = 2 [M].
Das waere ein Beweglichkeitseffekt, kein Rauheitseffekt. RP haelt die Schwerpunktsbewegung wie in G und fuegt nur die
Rauheit hinzu; damit trennt RP "rau gegen glatt" sauber. Bewertet wird deshalb **nach Plan mit RP** und **nach
Kartenwortlaut mit RL**.

**Startlage.** Form jedes Fadens: exakte Gleichgewichtsprobe der geschlossenen RSOS-Kette (Schritte unabhaengig: mit
Wahrscheinlichkeit p ein Knick in eine der 2(D-1) Querrichtungen, sonst gerade; verworfen, bis die Querschritte sich
aufheben). Querlagen von A und B gleichverteilt und unabhaengig. Treffen sie sich schon beim Start, werden Form und Lage
von B neu gezogen (Anzahl wird gespeichert). G: gerade Faeden, Startlagen verschieden.

**Laufzeit und Messgroessen.** T = c L^2 Schritte mit **c = 4** [F] (Karte laesst c offen; c = 4 macht den
G-Anteil in D = 3 bei L <= 100 nach Abschn. 2 gross, "~ 1"). Je Zelle (Bewegungsart, p, D, L):
Treffanteil P = Treffer / Paare bis T, Wilson-95-%-Intervall; Treffzeiten in Schritten (Median und Mittel, geteilt
durch L^2); Knickdichte beim Start und am Ende (nur ueberlebende Paare); lokale Annahmerate.

## 2. Was ich vorab weiss (Offenlegung, Ableitbarkeit) [M]

- **G ist ableitbar (K0).** Der Querabstand von A und B ist eine einfache Irrfahrt auf Z_L^(D-1) mit 2 Schritten je
  Schritt der Karte. P_G ~ 1 - exp(-2T/E[tau]) mit E[tau] ~ G_(D-1)(0) L^(D-1) fuer D >= 4 (G_3(0) = 1,516,
  G_4(0) = 1,239, G_5(0) = 1,156 [L]) und E[tau] ~ (2/pi) L^2 ln L + O(L^2) fuer D = 3 [L].
  Erwartung: D = 2: P ~ 1; D = 3: P ~ 0,98 (L = 16) bis 0,92 (L = 100), Steigung ~ -0,04 (logarithmischer Abfall, D = 3
  ist der Randfall); D = 4: Steigung ~ -0,8 ueber L = 8..32 (asymptotisch -1; P L ~ 3,9 bis 4,9); D = 5: ~ -1,9;
  D = 6: ~ -3. F1 erwarte ich als eingetroffen.
- **RL (Kartenwortlaut):** Nach dem Rouse-Argument oben erwarte ich P_RL ~ L^(-(D-1)/2) in allen D, also D* = 2 im
  strengen Sinn und F2 nach Kartenwortlaut als nicht eingetroffen, aus Beweglichkeitsgruenden. Das ist eine
  Abschaetzung, keine Messung.
- **RP (Plan), Abschaetzung [M, H]:** Der Schwerpunkt bewegt sich wie in G; die Faeden sind ~ r = (p L/(D-1))^(1/2)
  breit. Zielmenge fuer den Schwerpunktsabstand ist dann grob eine Kugel vom Radius r statt eines Punktes. Fuer
  D - 1 >= 3 (D >= 4) folgt P_RP ~ L^2 r^(D-3) / L^(D-1) ~ L^((3-D)/2): fallend, aber mit halber Steigung (D = 4:
  -1/2, D = 5: -1, D = 6: -3/2), sofern Schwerpunktsweg und Fadenform sich wie zwei Brownsche Wege schneiden (sicher
  fuer D - 1 <= 3, logarithmisch geschwaecht fuer D - 1 = 4, schwaecher fuer D - 1 = 5). Danach bliebe D_grenze = 3 und
  F2 nach Plan nicht eingetroffen. Gegenrichtung: Die Raum-Zeit-Flaeche einer Rouse-Kette (Hurst 1/2 in x, 1/4 in t)
  trifft lokal Punkte bis D - 1 < 6 [M, L]; das "Zittern in der Zeit" des Dossiers koennte also bei endlichem L
  mehr leisten, als die Kugelabschaetzung sagt. Endliche L flachen die Steigung zusaetzlich ab (Saettigung). Die
  Messung entscheidet; meine Erwartung fuer F2 (Plan): eher nicht eingetroffen.

## 3. Zellen [F]

| D | L (G) | L (RL, RP) | Paare G | Paare RL, RP |
|---|---|---|---|---|
| 2 | 16, 32, 64, 128, 256, 1000 | RL: 16, 32, 64; RP: 16, 32, 64, 128 | 4096 (L = 1000: 1024) | 256 |
| 3 | 16, 24, 32, 48, 64, 100 | 16, 24, 32, 48, 64, 100 | 4096 | 256 (RL bei L = 100: 128) |
| 4 | 8, 12, 16, 24, 32 | 8, 12, 16, 24, 32 | 16384 | 1024 |
| 5 | 4, 6, 8, 12, 16 | 4, 6, 8, 12, 16 | 65536 | 8192 |
| 6 | 4, 6, 8, 10 | 4, 6, 8, 10 | 65536 | 16384 |

- Rauheitsstufen: RP mit p = 0,2 und 0,6; RL nur mit p = 0,6 (Rechenzeit; RL dient nur der Kartenwortlaut-Wertung).
- **Abweichungen von den Netzgroessen der Karte, mit Grund:** Die Karten-L (D = 3: 100, D = 4: 32, D = 5: 16,
  D = 6: 10, D = 2: 1000) sind jeweils die groesste Stufe. Ausnahmen: D = 2 rau nur bis L = 64 (RL) bzw. 128 (RP),
  weil ein rauer Lauf ~ 4 L^3 Spaltenzuege je Paar kostet (Rauchtest: 0,21 bis 0,30 us je Paar, Schritt und Spalte; RL
  bei L = 1000 waere ~ 1e9 Zuege je Paar). D = 6 ohne L = 5 (Halbsweeps verlangen gerades L). Fuer "faellt mit L"
  braucht die Karte mehrere L je D; die Liste oben liefert 3 bis 6 Stufen je D.
- Saat: numpy default_rng([20261004, Bewegungsart, D, L, 1000 p, Paare]).

## 4. Auswertung und Urteile [F]

- Steigung s je (Bewegungsart, p, D): gewichtete Ausgleichsgerade von ln P gegen ln L ueber alle L der Zelle,
  P = (Treffer + 0,5)/(Paare + 1), Gewicht Paare P/(1 - P); 95-%-Intervall aus 2000 parametrischen Bootstrap-Ziehungen
  (Binomial). Abgebrochene Zellen zaehlen nicht.
- **"faellt mit L" nach Plan:** s < -0,25 und obere 95-%-Grenze < 0. **Nach Kartenwortlaut (streng):** obere
  95-%-Grenze < 0 und s < -0,01 (jeder gesicherte Abfall; dann ist D = 3 bei G wegen des logarithmischen Abfalls
  schon "fallend", passend zu "D* von 3" der Karte).
- **D*_fall** = kleinstes D, ab dem fuer alle groesseren D (bis 6) "faellt" gilt (nicht monoton wird gemeldet).
  **D_grenze = D*_fall - 1** = groesste Dimension, in der sich die Faeden bei wachsendem L noch zuverlaessig treffen
  (Brandenberger/Vafa: 3). Faellt nicht einmal D = 6: D_grenze ">= 6".
- **Lesart der Karte:** Die Karte schreibt "D*: ab ihr faellt der Treffanteil mit L" und "verschiebt D* von 3".
  Fuer glatte Faeden ist das nur im strengen Sinn (D = 3 faellt logarithmisch) dieselbe Zahl. Darum: nach Plan zaehlt
  D_grenze (Schwelle -0,25), nach Kartenwortlaut D*_fall im strengen Sinn.

| Nr | Karte | nach Plan | nach Kartenwortlaut |
|---|---|---|---|
| F1 | (G): D = 3 Anteil ~ 1, D = 4 Anteil ~ w/L | (a) P_G(D = 3) >= 0,8 bei allen L; (b) s_G(D = 4) in [-1,3; -0,6]. Beide: eingetroffen; eins: teilweise; keins: nicht eingetroffen | (a) P_G(D = 3, L = 100) >= 0,8; (b) P_G L bei D = 4 ueber L = 8..32 konstant bis Faktor 1,5 (w unbekannt, "~ w/L" heisst P L konstant). Wertung wie links |
| F2 | (R) verschiebt D* von 3 auf 4 oder 5 | RP, p = 0,6: D_grenze in {4, 5}: eingetroffen. D_grenze <= 3 bei beiden p: nicht eingetroffen. D_grenze ">= 6" bei p = 0,6: nicht eingetroffen (Grenze ueber 5). Sonst uneindeutig | RL, p = 0,6: D*_fall (streng) in {4, 5}: eingetroffen, sonst nicht eingetroffen. Bezug: D*_fall (streng) von G wird mit ausgegeben |

- Beschreibend [D], nicht Teil der Urteile: Steigungen bei D = 4 und 5 je Bewegungsart (Unterscheidungspunkt der
  Karte), Treffzeiten / L^2, Knickdichte Start/Ende (Kontrolle, dass die Dynamik die Rauheit haelt), Annahmeraten.
- Die Urteile rechnet der eingefrorene Code (Modus auswertung). Ich uebernehme sie und pruefe sie von Hand gegen die
  Tabelle.
- Jede Dimension wird getrennt ausgewiesen (AGENTS.md); kein Mittel ueber D.

## 5. Laeufe

- Nur .69 ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spuren cpu und cpu2, 1 Thread, je Lauf
  <= 10 min (RuntimeMaxSec = 600; im Code zusaetzlich Abbruch nach 560 s mit Kennzeichnung der Zelle).
- Rauchtest (erledigt, 19:37 CEST): Modus rauch, feste Schrittzahl ohne Entfernen getroffener Paare, Ausgabe nur
  Kosten je Paar, Schritt und Spalte (R: 206 bis 300 ns; G: 75 bis 101 ns je Paar, Schritt und Querrichtung).
- Laufplan (schlechtester Fall = kein Paar trifft; geschaetzt aus dem Rauchtest):
  - cpu: A = G (alle Zellen) + RL p = 0,6 D = 2, 4, 5, 6 (~ 340 s); dann C = RL p = 0,6 D = 3 (~ 210 s); dann
    E = RP p = 0,2 D = 3 (<= 350 s).
  - cpu2: B = RP p = 0,6 und 0,2 D = 4, 5, 6 (~ 290 s); dann D = RP p = 0,6 D = 3 (<= 350 s); dann F = RP p = 0,6 und
    0,2 D = 2 (L = 128 zuletzt; im schlechtesten Fall kann L = 128 abbrechen, dann bleiben 3 Stufen).
- Danach auswertung und bild auf der .69 (cpu), Dateien nach lauf-69/, sha256 auf beiden Seiten.
- Keine Aenderung an Plan, Urteilsregeln oder Code nach dem Einfrieren. Noetige Aenderungen nur als datierter Nachtrag
  am Ende dieses Plans mit Begruendung und neuem Hash, und nur vor der ersten Sicht auf Treffanteile; danach nur
  Selbstanzeige.
