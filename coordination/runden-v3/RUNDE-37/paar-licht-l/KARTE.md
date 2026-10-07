# PAAR-LICHT-L: Bekommen Licht und Teilchen von selbst dasselbe Tempo, wenn das Licht aus Paaren der Teilchen gebaut ist? (Runde 45, Literatur und Schreibtisch, Luecke L2 "Ein Tempo fuer alle Felder")

- Leitung claude-primary. Karte und Erwartungen geschrieben ab 2026-10-05 04:28:38 CEST (date), vor jedem Abruf.
- **Finn (05.10., gegen 04:15):** "Führe alle Themen weiter ... teste herum, was richtig ist".
- **Herkunft:**
  - LICHT-GLEICH-L (RUNDE-37/licht-gleich-l/DOSSIER.md):
    - Ein gemeinsames c entsteht von selbst nur durch eine Symmetrie, entweder zwischen den Sorten oder zwischen Zeit und Raum (Abschn. 1).
    - Gegensweep G7 ist ungeprueft geblieben: "Parameterfreie Quanten-Zellularautomaten (D'Ariano/Perinotti/Bisio: Licht aus Weyl-Paaren) haetten kein freies Tempo je Sorte [L?]. Kein Abruf mehr frei".
    - Offene Frage O2: Bekommt ein zusammengesetztes Photon Potenz-Annaeherung?
  - Warteschlange EIN-TEMPO-2 ("Licht und FKM-Fermion auf Finns Netz: gleiches langwelliges Tempo? Erst Ableitbarkeitsprobe, die Normierungen sind frei"). Die Probe steht unten; sie ersetzt EIN-TEMPO-2 in dieser Form.
- Kennzeichen: [S], [S Abstract], [L], [L?], [M], [ES], [H].

## Ableitbarkeitsprobe (vor der Karte, Leitung)

- **EIN-TEMPO-2 in der alten Form ist vorab entschieden [P, M]:**
  - Eis-Licht (Maxwell auf Finns Netz) hat das Tempo 2,8284 in Code-Einheiten (LICHT-FINN-NETZ-1).
  - Das FKM-Fermion hat das Tempo t a = 2,8284 (DIAMANT-NULLSTELLEN-1).
  - Der Wilson-Dirac-Operator auf demselben Netz hat 0,8165 (DIAMANT-FERMION-L, G7).
  - Das Tempo haengt also an der Diskretisierung und an der freien Kopplung. Die Gleichheit FKM = Maxwell ist eine Wahl der Einheiten, keine Vorhersage.
  - Damit gilt LICHT-GLEICH-L: Ohne Symmetrie gibt es keine Gleichheit. Keine Rechnung dazu.
- **Paarbau, vorab ableitbar [M]:** Ist das Photon ein Paar zweier Fermionen mit je halbem Impuls und scharfer Verschmierung, dann gilt omega_gamma(k) = 2 omega_F(k/2).
  - Langwellig ist das Tempo damit gleich, schon kinematisch.
  - Im k^2-Glied gilt a2_gamma(n) = a2_F(n)/4.
- **Form der Richtungsabhaengigkeit [M, Leitung, Schreibtisch, gegenzulesen]:**
  - Fuer die 12 normierten fcc-Vektoren d gilt Summe (n.d)^4 = 3 - S4. Eine einzelne fcc-Schale gibt daher a2 proportional zu (S4 - 3).
    - Andere Schalen geben andere Formen, etwa die bcc-Schale (3 - 2 S4).
    - Eine allgemeine Regel fuer Mehrband-Modelle ist das nicht.
  - Aus den Projektzahlen folgt dieselbe Form (S4 - 3):
    - Eis-Licht: a2 = -1/8 + S4/24 = (S4 - 3)/24
    - FKM-Kegel r: a2_r = -3/8 + S4/24 + n_r^4/4 (je Kegel nur tetragonal); ueber die drei Kegel gemittelt (S4 - 3)/8
  - Paarbau je Kegel r: a2_r/4, also tetragonal. Ob es dann ein Photon oder drei gibt (eines je Kegel), ist offen.
    - Nur das kubisch gemittelte Muster waere (S4 - 3)/32.
  - Folge, soweit gemittelt: Die Himmelsrichtung allein unterscheidet "Licht aus Eis" nicht von "Licht aus Paaren". Nur die Groesse relativ zum Fermion tut es (Paarbau: genau 1/4). Gibt es drei Photonen, waere das anders.
  - Diesen Punkt nicht neu rechnen, nur gegenlesen.
- **Nicht ableitbar (Literatur):**
  - ob der Paarbau ein echtes Maxwell-Feld gibt (quer, zwei Polarisationen, Eichinvarianz)
  - wie gross die Abweichung von der Bose-Statistik ist und woran sie haengt (Pryce 1938 bzw. Perkins zum Neutrino-Photon [L?])
  - welche Messungen sie begrenzen (Bose-Symmetrie-Tests an Photonen, etwa DeMille u. a. 1999 und English u. a. 2010 [L?])
  - ob die Gleichheit Wechselwirkungen, also Schleifen, uebersteht
- **Projektsuche:** "Bisio" nur als ungelesene Angabe (qca-tetra-1, licht-gleich-l G7). "Pryce", "composite photon" und "Neutrinotheorie" kommen nicht vor. Der Weyl-Automat lebt auf BCC mit c = 1/sqrt3 und nur mit der Klein-Gruppe kovariant (QCA-TETRA-1) [S, P].

## Auftrag (feldforscher)

1. **Lesen:** Bisio, D'Ariano, Perinotti zum Licht aus Weyl-Automaten (Quanten-Zellularautomaten-Theorie des Lichts, um 2014 bis 2016; per arXiv-API suchen, Volltext lesen).
   - Wie wird das Photon gebaut?
   - Gilt langwellig Maxwell, und mit welchem Tempo?
   - Wie gross ist die Abweichung von der Bose-Statistik, und was legt sie fest?
   - Welche Messungen nennen die Autoren (Laufzeit, Statistik)?
2. **Klassische Einwaende:** Pryce bzw. Perkins zum Neutrino-Photon, soweit die Quelle sie zitiert oder frei abrufbar ist.
3. **Messdaten:** Schranken auf die Verletzung der Bose-Symmetrie bei Photonen (Primaerquelle bzw. Abstract). Reicht die Abweichung des Paarbaus heran?
4. **Schreibtisch:**
   - Die Formabschnitte der Ableitbarkeitsprobe gegenlesen, nicht neu herleiten.
   - Uebertraegt sich der Paarbau auf Finns Diamant-Netz (FKM-Kegel an X; Paare aus einem Kegel und seinem Gegenstueck haben Gesamtimpuls nahe 0)?
   - Was hiesse das fuer die Tempo-Gleichheit Elektron gegen Licht bei hoher Energie (Vorzeichen, Photonzerfall bzw. Cherenkov)?

## Erwartungen (vor jedem Abruf)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| PL1 | [L?] Bisio/D'Ariano/Perinotti bauen das Photon aus zwei Weyl-Automaten; langwellig folgt Maxwell mit dem Tempo der Fermionen; die Bose-Statistik gilt nur naeherungsweise | 75 % |
| PL2 | [H] Die Literatur zeigt nicht, dass die Gleichheit Wechselwirkungen (Schleifen) uebersteht; sie ist dort kinematisch | 60 % |
| PL3 | [H] Die Abweichung von der Bose-Statistik haengt an einem freien Verschmierungsparameter, und die Labor-Schranken schliessen den Paarbau nicht aus | 55 % |
| PL4 | Kontrolle [M, vorab ableitbar]: Gegenlesen bestaetigt Summe (n.d)^4 = 3 - S4 und a2_gamma = a2_F/4 im Paarbau (je Kegel) | 85 % |

**Bedeutung (vorab):**
- **PL1 und PL3 treffen ein:** Es gibt einen dritten Weg zu "einem Tempo fuer alle": ohne Symmetrie und ohne Abstimmung, dafuer mit naeherungsweiser Bose-Statistik des Lichts.
  - Fuer Finns Netz hiesse das: Licht nicht aus dem Eis, sondern aus Teilchenpaaren. Das waere eine echte Weiche fuer Finn.
- **PL1 verfehlt** (kein konsistentes Maxwell-Feld) **oder PL3 verfehlt** (die Daten schliessen den Bau aus): Fuer das gleiche Tempo bleiben nur die Symmetrie-Wege aus LICHT-GLEICH-L.
- **PL2 trifft ein:** Die Gleichheit ist nur klassisch gesichert. Die Collins-Gefahr bleibt offen wie in LICHT-GLEICH-L, Ergebnis 5.

## Rahmen

- feldforscher, Zeitbox 50 min, hoechstens 6 Abrufe (arXiv-API oder arxiv.org per WebFetch, Verlagsseiten nur frei), keine Websuche.
- Erwartung mit date-Zeit vor jedem Abruf in ARBEITSFELD.md.
- Schreiben nur in RUNDE-37/paar-licht-l/.
