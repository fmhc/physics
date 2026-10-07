# LADUNG-MONOPOL-1, Teil A: Plan (Code-Agent, Runde 38)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 06:02:30 CEST, Plantext ab 06:22:42 CEST (date).
  Die .69 laeuft in UTC (CEST = UTC + 2).
- Gelesen vor dem Plan: KARTE.md; Dossier LADUNG-MONOPOL-L Abschnitte 5, 9, 12; ARBEITSFELD Abschnitt 6 (D1 bis D6);
  SPIN1.md Abschnitt 6 "Weg B" (und B-V1 bis B-V5).
- **Kennzeichen:** [M] eigene Mathematik (Schreibtisch), [F] Festlegung dieses Plans (von der Karte offen gelassen),
  [K] Kartenberichtigung bzw. Anmerkung, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [S] an der Quelle gelesen
  (hier kein neuer Abruf), [H] Hypothese, [E] gerechnet.
- Alles ist eine synthetische Gitterrechnung, keine Messdaten.

## 1. Konstruktion

### 1.1 Gitter und Fluss

- Offene Box mit L Plaetzen je Richtung, L in {12, 16, 24}; Koordinaten relativ zur Boxmitte c = (L-1)/2, also
  halbzahlig. Der Monopol sitzt im Mittelpunkt des Mittelwuerfels (Ecken bei +-1/2). [F]
- Plakette p mit Normale +e_nu (Umlauf in der Ebene e_a, e_b mit e_a x e_b = e_nu):
  Phi_p = Omega_p/2, Omega_p = vorzeichenbehafteter Raumwinkel vom Monopol, als Summe der zwei Dreiecke (v1,v2,v3) und
  (v1,v3,v4) nach Van Oosterom-Strackee: tan(Omega/2) = r1.(r2 x r3) / (r1 r2 r3 + (r1.r2) r3 + (r1.r3) r2 +
  (r2.r3) r1), ausgewertet mit atan2.
- Pruefungen (Code, je L): Auswaertssumme ueber jeden Elementarwuerfel <= 1e-12, im Mittelwuerfel 2 pi +- 1e-12;
  max |Phi_p| = pi/3 (Flaechen des Mittelwuerfels), also alle Werte in (-pi, pi].

### 1.2 Eichfeld

- n_p: String vom Mittelwuerfel zum Rand.
  - +z: n = +1 auf den z-Plaketten der Mittelsaeule von der Deckflaeche des Mittelwuerfels bis zum oberen Rand.
  - -z: n = -1 auf den z-Plaketten der Mittelsaeule von der Bodenflaeche bis zum unteren Rand.
  - +x: n = +1 auf den x-Plaketten der Mittelzeile ab der +x-Flaeche.
  - Vorzeichen so, dass F = Phi - 2 pi n in jedem Wuerfel quellenfrei ist (Code prueft "schliessung" <= 1e-12).
- A auf den Kanten aus rot A = F mit scipy.sparse.linalg.lsqr (atol = btol = 1e-15, bis 50 000 Iterationen) plus
  hoechstens drei Nachbesserungen auf dem Rest. Rest = max_p |(rot A)_p - F_p|, gefordert <= 1e-10 (Karte).
- Hamilton: H = -sum_<ij> (e^{i q A_ij} c_i^+ c_j + h.c.) - V0 sum_{8 Ecken} n_i, also H_ij = -exp(i q A_ij).
  Das Vorzeichen von q ist fuer das Spektrum gleichgueltig (H_{-q} = conj H_q).

### 1.3 Magnetische Drehungen und Kommutatorzeichen

- Zu einer Drehung R des Wuerfels um den Monopol: (P_R v)(x) = v(R^-1 x). P_R H P_R^-1 hat die Phasen
  K^R_ij = K_{R^-1 i, R^-1 j}, also denselben Fluss Phi (Raumwinkel ist drehinvariant), aber den gedrehten String.
- Eichfunktion g mit g_i conj(g_j) = K_ij / K^R_ij auf jeder Kante: aufgebaut entlang eines Breitensuch-Baums ab Platz 0
  (scipy.sparse.csgraph), dann auf **allen** Kanten geprueft ("Defekt" = max |g_i K^R_ij conj(g_j) - K_ij| <= 1e-10).
  Das geht, weil K und K^R sich nur um eine 2-pi-Flusslinie unterscheiden, die fuer ganzes q unsichtbar ist.
- U_R = D_g P_R vertauscht dann mit H (der Topf sitzt auf den 8 Ecken und ist drehinvariant).
- Verwendet: R_x = pi um x, R_y = pi um y, C3 = 2 pi/3 um (1,1,1), C4z = pi/2 um z.
- C = U_x U_y U_x^-1 U_y^-1. Als Platzpermutation ist C die Identitaet, also eine Diagonalphase, die mit H vertauscht:
  auf dem zusammenhaengenden Gitter eine Konstante c. Aus U_x^2 = a (Konstante) folgt c^2 = 1. Phasenwahlen von U_x und
  U_y kuerzen sich. Gemessen wird c zweifach:
  - als Operator auf einem Zufallsvektor (c und Rest ||Cv - c v||),
  - als s = Tr(P C P)/m auf jeder Stufe P der Dimension m.
- **Herleitung s = (-1)^q [M]:**
  - C = D_h mit h(x) = g_x(x) g_y(R_x x) / (g_y(x) g_x(R_y x)) (R^-1 = R fuer pi-Drehungen).
  - Mit g_R(x)/g_R(y) = exp(i q Summe_{y->x} (A - A^R)) wird h(x) = exp(i q Umlauf von A ueber die geschlossene
    Schleife Gamma = gamma1 + gamma2 - R_x gamma1 - R_y gamma2), gamma1 von R_y x nach x, gamma2 von x nach R_x x.
  - Umlauf von A = Fluss durch eine aufgespannte Flaeche = Omega(Gamma)/2 mod 2 pi; der String zaehlt fuer ganzes q nicht.
  - h haengt nicht von den Wegen ab: Wegaenderungen geben delta - R delta, und Omega(R delta) = Omega(delta).
  - Waehlt man die Wege symmetrisch (Gerade durch die y- bzw. x-Achse), dann gilt R_x Gamma = -Gamma, also
    Omega = -Omega mod 4 pi, also Omega in {0, 2 pi}. Gamma umlaeuft die z-Achse einmal (Projektion: Rechteck um den
    Ursprung) und teilt die Richtungskugel in zwei gleich grosse Haelften. Also Omega = 2 pi und h = e^{i q pi} = (-1)^q.
  - Kontinuum zum Vergleich: g_x, g_y = e^{i q (phi + const)} (Wu-Yang A_N - A_S = d phi [L]); dieselbe Rechnung gibt
    e^{-i q pi}.
- Folge [M]: Bei q = 1 ist U_x U_y = -U_y U_x auf jeder Stufe, also ist jede Stufe gerade entartet. Damit sind die
  s-Teile von LM0 und LM1 vorab ableitbar (Karte: "ja").

## 2. Schreibtisch vor jeder Rechnung: Grenzfall tiefer Topf [M]

- Fuer V0 -> unendlich sitzen die tiefsten Zustaende auf den 8 Ecken des Mittelwuerfels. Jede Flaeche traegt dort den
  Fluss q pi/3 (Raumwinkel 2 pi/3).
- Der Wuerfelgraph ist bipartit: H_Wuerfel = -[[0, T], [T^+, 0]], T eine 4 x 4-Matrix (gerade gegen ungerade Ecken).
  - (T^+ T)_oo = 3.
  - (T^+ T)_oo' = Summe der zwei Zweischritt-Wege ueber eine Flaechendiagonale, Betrag 2 |cos(q pi/6)|, Phase
    e^{i q pi/6} gegen den Weg ueber die gemeinsame Ecke.
  - Die vier ungeraden Ecken bilden ein Tetraeder. Jedes seiner Dreiecke traegt die Phase 3 q pi/6 = q pi/2
    (C3-Symmetrie um die Raumdiagonale).
- **Ergebnis:**
  - q = 0: Wuerfelspektrum -3 (1), -1 (3), 1 (3), 3 (1).
  - q = 1: Tetraeder mit Fluss pi/2 je Dreieck. Dort heben sich die Zweischritt-Wege weg, M^2 = 3 m^2, also
    T^+T in {6, 6, 0, 0}. Spektrum -sqrt6 (**2**), 0 (4), +sqrt6 (2).
  - q = 2: Fluss pi je Dreieck, M + 1 ist eine Hadamard-Matrix, T^+T in {4, 4, 4, 0}. Spektrum -2 (**3**), 0 (2),
    +2 (3).
- **Ableitbarkeitsprobe [K1]:**
  - Fuer grosse V0 sind LM2 (Dublett) und LM3 (Triplett) **vorab ableitbar**: Die Wuerfel-Grundstufe ist bei q = 1
    zweifach und bei q = 2 dreifach. Die Entartung ist durch die Drehgruppe geschuetzt und bleibt bei Kopplung nach
    aussen.
  - Die Karte nennt LM2 und LM3 "nein (Gitterkern)". Echt offen ist nur der Bereich nahe der Schwelle: Kann dort eine
    andere Stufe (etwa das Quartett aus der Wuerfelstufe 0) unter das Dublett rutschen?
  - Das Kontinuum sagt nein (kleinste Zentrifugalzahl bei j = q/2, D4). Der Wuerfel sagt auch nein.
  - Ein Kartentreffer bei LM2/LM3 belegt also vor allem: keine Kreuzung zwischen Schwelle und tiefem Topf.
- Folge fuer die Energieverschiebung [M]: Kato auf dem Gitter (Dreiecksungleichung je Kante) gibt E_0(q, V0) >= E_0(0, V0)
  fuer jedes V0, auch in der offenen Box. Der Wuerfel zeigt die Groesse dieser "Gitter-Zentrifugalkosten" im tiefen
  Topf: 0; 3 - sqrt6 = 0,551; 1,0.

## 3. Raster und Messgroessen

- q in {0, 1, 2}, L in {12, 16, 24}, V0 in {0, 1, 2, 3, 4, 6, 8, 12} (Karte). Hauptstring +z.
- **Spektrum [F]:**
  - eigsh(which='SA', tol=0, ncv=64, Startvektor aus festem Zufallssamen) mit k = 16 Eigenwerten.
  - Berichtet werden die tiefsten 12 (Karte). Mit 16 sind Stufen, die in den tiefsten 12 beginnen, bei Entartung bis 4
    vollstaendig.
  - Eine Stufe, die den 16. Eigenwert beruehrt, gilt als "nicht voll" und wird nicht geurteilt.
  - **Vervollstaendigung (nach Rauchlauf 1 eingefuehrt, Abschnitt 8):**
    - Je eigsh-Stufe wird der Raum unter U_x, U_y, U_C3, U_C4z abgeschlossen; die Raeume werden vereinigt
      (SVD, Rangschwelle 1e-8).
    - Dann wird H im vereinigten Raum exakt diagonalisiert (Rayleigh-Ritz).
    - Ritz-Paare mit relativem Residuum > 1e-6 werden verworfen.
    - Die Stufen werden danach wie oben aus den Eigenwerten gebildet (Kartenkriterium 1e-8).
    - Die Zahl der ergaenzten Vektoren wird je Punkt berichtet.
- **Stufe [F]:** Kette benachbarter Eigenwerte mit |E_b - E_a| <= 1e-8 max(|E_a|, |E_b|). Energie = Mittelwert.
- **Gebunden (Karte):** E < -6 - 1e-3 und Gewicht in r <= 3 mindestens 0,9.
  - r ist der Abstand vom Monopol (Wuerfelmittelpunkt) [F]. Kein Platz liegt genau bei r = 3 (r^2 = n + 3/4).
  - Gewicht der Stufe = Tr(P Pi_{r<=3})/m, also basisunabhaengig [F].
- **Tiefste gebundene Stufe [F]:** die tiefste volle Stufe, die das Kriterium erfuellt (wortlich; ob sie zugleich die
  tiefste Stufe ueberhaupt ist, wird berichtet).
- **Kommutatorzeichen:** s je Stufe (1.3). "s = -1" heisst |s + 1| <= 1e-8 [F]; ebenso fuer +1.
- **Symmetrie-Vollstaendigkeit (Kontrolle) [F]:** Je Stufe max |U V - V (V^+ U V)| fuer U in {U_x, U_y, U_C3, U_C4z}.
  Hat eigsh eine Kopie einer entarteten Stufe verpasst, ist das gross. Grenze 1e-6.
  - Beschreibend dazu |chi(C3)| und |chi(C4z)|: phasenunabhaengig.
  - q = 1: |chi(C4)| = sqrt2 fuer zweidimensionale Stufen (Gamma6/Gamma7), 0 fuer Gamma8 (Quartett).
  - q = 2: |chi(C3)| = 0 fuer Tripletts (T1/T2), 1 fuer A und E.
  - T1 gegen T2 und Gamma6 gegen Gamma7 sind ohne Festlegung der Drehphase nicht unterscheidbar; ich behaupte das nicht.
- **Schwelle V0c je q [F]:**
  - Klammer aus dem Raster (groesstes ungebundenes V0, naechstes gebundenes darueber). Ohne Bindung bei 12 wird bis 48
    verdoppelt (ausserhalb des Kartenrasters).
  - Bisektion auf Breite <= 1e-3; V0c = Mitte der Endklammer.
  - Fuer das Urteil gilt L = 24. L = 16 und 12 sind beschreibend (Groessenkonvergenz der Schwelle).
  - Beschreibend daneben die reine Energieschwelle (nur E_0 < -6 - 1e-3).
- **Gegenproben:**
  - String-Richtung: +z gegen -z und +x bei q in {0, 1, 2}, alle L, V0 in {0, 4, 12}; max |Delta E| der tiefsten 12.
  - Dicht bei L = 12: numpy eigvalsh gegen eigsh bei V0 in {0, 4, 12}; Eigenwerte und Stufengroessen.
  - Zweitlauf L = 24: q = 1, 2, alle Raster-V0 ueber der Schwelle, anderer Startvektor, ncv = 96.
  - Oberes Bisektionsende bei L = 24: Entartung und s direkt an der Schwelle (beschreibend).
  - Kato: E_0(q) >= E_0(0) an allen Rasterpunkten.
- **Beschreibend fuers Bild:** feines Raster V0 = 0 bis 12 in Schritten von 0,25 bei L = 16, alle q.

## 4. Urteilsregeln (mechanisch, code/auswertung.py)

Die Vorhersagen und Schwellen der Karte gelten unveraendert. [F] markiert, was die Karte offen laesst.

- **LM0** (q = 0 und Eichkonstruktion). Eingetroffen, wenn alle vier Teile gelten:
  - (a) q = 0: Operator-c = +1 und s = +1 auf allen vollen Stufen an allen (L, V0).
  - (b) q = 0: An allen (L, V0) mit gebundener Stufe ist die tiefste gebundene Stufe einfach; mindestens ein solcher
    Punkt muss existieren, sonst nicht auswertbar.
  - (c) lsqr-Rest <= 1e-10 fuer alle L und alle drei Strings.
  - (d) String-Unabhaengigkeit max |Delta E| <= 1e-10 an allen Punkten aus Abschnitt 3.
  - [K2] Fuer q = 0 ist (d) trivial (kein Feld). Darum werden q = 1, 2 mitgeprueft; das Urteil schliesst sie ein [F].
  - Nach Kartenwortlaut (nur q = 0) wird (d) zusaetzlich getrennt berichtet.
- **LM1:** Eingetroffen, wenn
  - bei q = 1 an allen (L, V0) Operator-c = -1 und s = -1 auf jeder vollen Stufe gelten und jede volle Stufe gerade
    entartet ist,
  - und bei q = 2 Operator-c = +1 und s = +1 auf jeder vollen Stufe gelten.
- **LM2:**
  - Punkte: q = 1, L = 24, alle Raster-V0 > V0c(1, L = 24) [F: "jedes V0" = Kartenraster].
  - Eingetroffen, wenn an jedem Punkt die tiefste gebundene Stufe genau 2-fach ist und die Symmetrie-Kontrolle besteht.
  - Nicht eingetroffen, wenn sie an einem Punkt eine andere Groesse hat.
  - Nicht auswertbar, wenn es keinen Punkt gibt, an einem Punkt keine gebundene Stufe vorliegt (Schwelle nicht
    monoton) oder die Symmetrie-Kontrolle an einem Punkt scheitert.
  - Der Zweitlauf muss die Stufengroessen bestaetigen, sonst ebenfalls nicht auswertbar.
- **LM3:** wie LM2 mit q = 2 und genau 3-fach.
- **LM4:** Eingetroffen, wenn V0c(1) > V0c(0) und 1,3 <= V0c(1)/V0c(0) <= 3,0 (L = 24, Kartenkriterium).
  - Liegt der Quotient innerhalb der Bisektionsunsicherheit an einer Bandgrenze, wird das vermerkt; geurteilt wird
    mit der Mitte.
  - Nicht auswertbar, wenn eine der beiden Schwellen fehlt.
- **LM5:**
  - Punkte: alle Raster-(q, V0) mit gebundener tiefster Stufe bei L = 24 [F].
  - Verglichen werden alle vollen gebundenen Stufen von L = 24 mit der Stufe gleichen Index bei L = 16 (Stufen nach
    Energie geordnet) [F].
  - Eingetroffen, wenn ueberall die Stufengroesse gleich ist und |Delta E| <= 1e-6 gilt.
  - Berichtet wird auch, ab welchem V0 die Gleichheit je q haelt.

## 5. Kartenberichtigungen und Anmerkungen (vor dem Einfrieren)

- **K1 (Ableitbarkeit):** LM2 und LM3 sind im tiefen Topf vorab ableitbar (Abschnitt 2). Offen ist nur die Schwellennaehe.
  Die Urteilsregel bleibt die der Karte.
- **K2 (LM0, String-Probe bei q = 0 trivial):** Mitgeprueft bei q = 1, 2 (Abschnitt 4).
- **K3 (LM4, Vorzeichen):**
  - "Vorzeichen ja (Kato)" gilt streng nur fuer die Energieschwelle, denn Kato vergleicht Energien.
  - Das Kartenkriterium enthaelt zusaetzlich das Gewicht in r <= 3. Fuer diese Schwelle folgt das Vorzeichen nicht
    zwingend aus Kato.
  - Ich urteile nach Kartenkriterium und berichte die Energieschwelle daneben.
- **K4 (Schwelle ist operativ):**
  - Das Gewichtskriterium (90 % in r <= 3) verlangt eine Bindung, deren Abklinglaenge deutlich unter 3 liegt.
  - Grob [M, Kontinuum]: Gewicht ausserhalb ~ e^{-2 kappa 3} = 0,1, also kappa ~ 0,38 und Bindung ~ 0,15 unter der
    Bandkante.
  - V0c ist also nicht die Bindungsschwelle des unendlichen Gitters (bei q = 0 grob 1,4 nach der Gitter-Greenfunktion
    [L?]).
- **Nach Kartenwortlaut** (falls sie von der Plan-Lesart abweichen) werden die Urteile in ERGEBNIS.md getrennt genannt.

## 6. Agenten-Vorhersagen (vor jeder Rechnung, 06:22 bis 06:35 CEST)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Tiefer Topf: bei L = 24, V0 = 12 gilt E_0 + 12 - eps_q in [-0,30; -0,15], mit eps_q = -3; -sqrt6; -2 (zweite Ordnung ~ 3 G_aussen(E) ~ -0,21) | 75 % |
| A2 | Operator-c = (-1)^q an allen (L, q) mit Rest <= 1e-12; Drehdefekte <= 1e-12 | 90 % |
| A3 | lsqr-Rest <= 1e-10 erreicht (notfalls mit Nachbesserung); String-Differenzen <= 1e-11 | 85 % |
| A4 | LM2 und LM3 eingetroffen, auch am oberen Bisektionsende; keine Kreuzung | 85 % |
| A5 | V0c(0, 24) in [1,6; 2,8]; V0c(1, 24) in [2,4; 4,5]; Quotient in [1,25; 2,0]; LM4 eingetroffen | 55 % |
| A6 | V0c(2, 24) > V0c(1, 24), Quotient V0c(2)/V0c(0) in [1,6; 3,0] | 70 % |
| A7 | LM5 nicht eingetroffen: am kleinsten gebundenen Raster-V0 je q |Delta E| zwischen 1e-6 und 1e-3; bei V0 >= 8 <= 1e-9 | 60 % |
| A8 | Bei q = 1 ist die erste angeregte gebundene Stufe im tiefen Topf das Quartett (|chi(C4)| = 0), bei q = 2 die Zweierstufe (|chi(C3)| = 1) | 75 % |

## 7. Ablauf

- .69, Ordner /home/fmh/fmhc-physics-remote/runde38-ladung-monopol/ (code/, rauch/, lauf/), nur ueber kleintest.sh,
  Spur p4000a. Die Rechnung ist CPU-scipy, wie im Auftrag vorgegeben (eigsh); die GPU der Spur bleibt ungenutzt.
- Rauchlauf: Modus rauch (L = 12, V0 in {0, 4, 12}) plus Zeitprobe L = 24.
- Einfrieren: PLAN.md.eingefroren-JJJJMMTT-HHMMSS, Code-Kopien, EINGEFROREN-SHA256.txt.
- Hauptlaeufe:
  - gitter fuer L = 12 und 16, dann L = 24
  - schwelle (liest beide gitter-JSON)
  - scan (L = 16)
  - auswertung (Urteile, auswertung.json, Bild)
- Abbruchregel: Laeuft ein Teil nach zwei ernsthaften Versuchen nicht, gilt er als "nicht gerechnet" mit Grund.

## 8. Rauchlauf-Befunde (vor dem Einfrieren offengelegt, geschrieben ab 06:31:46 CEST)

- **Laeufe:**
  - rauch1: 04:24:20 bis 04:25:05 UTC, rc = 0.
  - rauch2: 04:29:05 bis 04:29:51 UTC, rc = 0, mit Vervollstaendigung.
  - Beide: L = 12 mit q = 0, 1, 2 und V0 = 0, 4, 12, dazu ein Zeitpunkt L = 24 (q = 1, V0 = 4).
- **Codefehler gefunden (rauch1) und behoben:**
  - eigsh rechnet komplexe hermitesche Matrizen intern mit eigs (Arnoldi).
  - Bei q = 1, L = 12, V0 = 4 fehlte eine Kopie einer Vierer-Stufe: Stufen [2,2,4,2,3,2,1] gegen dicht [2,2,4,2,4,2],
    die Eigenwertliste war dadurch um bis 0,13 verschoben.
  - In entarteten Stufen lieferte eigsh nicht orthogonale Vektoren; die Symmetrie-Kontrolle ergab Reste bis 0,06.
  - Behoben durch die Vervollstaendigung (Abschnitt 3).
  - rauch2: dicht gegen eigsh an allen 9 Punkten <= 5e-14, Stufengroessen gleich; Symmetrie-Reste voller Stufen ~1e-14.
- **Kontrollen (rauch2):**
  - Wuerfelsummen 1e-16, Mittelwuerfel 2 pi auf 9e-16, max |Phi| = pi/3.
  - lsqr-Rest <= 3e-14 (L = 12, 49 bis 50 Iterationen), 1,6e-14 (L = 24, 107 Iterationen).
  - Drehdefekte <= 1e-13. Operator-c = +1, -1, +1 (q = 0, 1, 2) mit Rest <= 2e-14.
  - String-Differenzen <= 2e-14.
- **Gesehen, was die Urteile vorwegnimmt (Selbstanzeige; daran wurde nichts geaendert):**
  - L = 12, V0 = 4: tiefste Stufe q = 0 einfach bei -7,639; q = 1 zweifach bei -7,132; q = 2 dreifach bei -6,721.
    Alle drei gebunden, Gewicht >= 0,99.
  - L = 12, V0 = 12: q = 0 bei -15,233, q = 1 bei -14,686 (zweifach, darueber vierfach). Fuer A1 heisst das
    -0,233 bzw. -0,237 bei L = 12.
  - L = 24, q = 1, V0 = 4: -7,1320763, wie bei L = 12 auf ~1e-5.
  - |chi(C4)| = sqrt2 an allen Zweierstufen und 0 an den Viererstufen (q = 1); |chi(C3)| = 0 an den Dreierstufen
    (q = 2).
  - V0 = 0: keine gebundene Stufe.
  - Die Schwellen lagen damit fuer alle q zwischen 0 und 4; ihre genaue Lage habe ich nicht gesehen.
- **rauch3** (04:32:26 bis 04:32:53 UTC, rc = 0): Modus schwelle bei L = 12 auf den rauch2-Daten, nur als
  Funktionsprobe. Angesehen habe ich nur die Schluessel und die Schrittzahlen (12 je Bisektion), nicht die
  Schwellenwerte.
- **Zeit:** L = 24 ein Punkt 3,2 s (eigsh), L = 12 0,2 bis 0,3 s, dicht L = 12 3,7 s.
- **auswertung.py** ist vor dem Einfrieren nicht gelaufen (es braucht die Hauptdaten). Zeigt sich dort ein echter
  Fehler, wird er nach dem Einfrieren behoben und offengelegt.
- **Nicht geaendert:** Vorhersagen, Schwellen der Karte, Urteilsregeln, Agenten-Vorhersagen.
- **Geaendert:** nur der Code (Vervollstaendigung), dazu dieser Abschnitt und der Spektrum-Absatz in Abschnitt 3.
