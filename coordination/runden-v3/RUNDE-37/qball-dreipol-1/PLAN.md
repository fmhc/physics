# QBALL-DREIPOL-1: Plan (Code-Agent, Runde 42)

- Code-Agent fuer claude-primary. Start 2026-10-04 17:14:57 CEST (date). Plantext begonnen 17:36:08 CEST (date).
- Reihenfolge offen gelegt: Code zuerst geschrieben; Rauchlauf r1 (15:32 UTC), die volle QD0-Kontrolle (a) und
  Leitungstests der Modi b und c mit fremden Werten (Q1 = 25, unkonvergiert) liefen, waehrend dieser Text entstand.
  Aus dem Rauchlauf stammen nur Zeiten, Speicher, QD0-Kontrollwerte und Aufbauwerte des Einpolballs bei
  g4 = +0,1 (R_halb, omega). Keine Wechselwirkungsenergie, kein Dreierfluss, keine Dreierdynamik vor dem Einfrieren.
- Grundlagen [P]: KARTE.md (Vorhersagen QD0 bis QD3 und Wahrscheinlichkeiten unveraendert); Papier I
  (model-lab/papers/qball-bic-ladder-20260930/main.tex, Abschnitt "Field model", Gl. eq:action); QB-BS-2D
  (Festladungsverfahren E_q = V + q^2/(2 Lambda) nach astra L3, radiale Q-Baelle in 2+1); QBALL-PYRO-1
  (Zeitentwicklung, Messweise); RUNDE-42/FARBE-SCHREIBTISCH.md.
- Kennzeichen wie in der Karte: [M] Mathematik, [E] Messung im Modell, [P] Projektdatei, [L] Literatur aus dem
  Gedaechtnis, [H] Hypothese. Alles ist eine synthetische Rechnung im Modell, keine Messdatenbestaetigung.

## 1. Modell

**Papier I [P]:** Signatur (+,-,-,-), L = d_mu phi^* d^mu phi - U(|phi|^2), U(S) = S - S^2 + beta S^3, beta = 1/2.
Freie Masse 1, Duennwandschwelle omega_c^2 = 1/2, Ladung Q = 2 omega int f^2 > 0 fuer phi = e^{i omega t} f.

**Erweiterung nach Karte:** Phi = (phi_1, phi_2, phi_3) in C^3, in 2+1 Dimensionen:

    L = sum_a [ |d_t phi_a|^2 - |grad phi_a|^2 ] - V,   V = U(S) + g4 sum_a |phi_a|^4,   S = sum_a |phi_a|^2.

- **g4 relativ zur Selbstkopplung:** Der Quartterm von U hat den Koeffizienten -1 (Betrag 1). g4 in {-0,1; 0; +0,1}
  ist also plus/minus 10 % dieser Kopplung und wird absolut eingesetzt. Fuer einen Pol wird der Quartterm
  -(1 - g4) S^2.
- **Symmetrie [M]:** Gradiententerm und U(S) sind U(3)-invariant. g4 sum_a |phi_a|^4 laesst U(1)^3 (eigene
  Phasendrehung je Komponente) und die Vertauschungen der Komponenten. Fuer g4 != 0 sind die drei Ladungen
  Q_a = 2 int Im(conj(phi_a) d_t phi_a) einzeln erhalten.
- **Bewegung:** d_t^2 phi_a = Lap phi_a - (U'(S) + 2 g4 |phi_a|^2) phi_a. Energie E = int [sum_a (|d_t phi_a|^2 +
  |grad phi_a|^2) + V].
- **Feste Ladungen:** E_Q[psi] = W[psi] + sum_a Q_a^2/(2 Lambda_a), W = int [sum_a |grad psi_a|^2 + V],
  Lambda_a = 2 int |psi_a|^2, omega_a = Q_a/Lambda_a. Das ist astra L3 (QB-BS-2D Abschn. 4) mit getrennten
  Ladungen. Ein Minimum von E_Q bei festen Q_a ist ein stationaerer Zustand psi_a e^{i omega_a t}.
- **Pole:** "Pol a" heisst Q-Ball nur in Komponente a. Die "Richtung" ist die Drehung der inneren Phase je Komponente.

## 2. Ableitbarkeitsprobe (vor den Hauptlaeufen) [M]

1. **Feste innere Richtung n (reell, Betrag 1), phi_a = n_a f e^{i omega t}:** V = f^2 - (1 - g_eff) f^4 + beta f^6
   mit g_eff = g4 sum_a n_a^4.
   - Eine exakte Loesung der Feldgleichung ist das nur, wenn alle von null verschiedenen n_a gleich gross sind: ein Pol,
     zwei gleiche Pole, gleich gemischt (sum n_a^4 = 1, 1/2, 1/3). Fuer andere Richtungen ist es nur ein
     Variationsansatz.
   - Deshalb misst (a) genau diese drei Richtungen. QD0 ist eine reine Code- und Gitterkontrolle.
2. **Welcher Pol gewinnt:** E(Q; g) steigt mit g, weil das Potential punktweise waechst. Bei festem Gesamt-Q gewinnt
   fuer g4 < 0 ein Pol (g_eff = g4) und fuer g4 > 0 die gleiche Mischung (g_eff = g4/3).
   - "Die Anisotropie, die das Mischen beguenstigt" ist also g4 = +0,1. Die Auswertung bestimmt sie trotzdem aus (a).
   - Wegen der getrennten Ladungserhaltung sind das verschiedene Ladungssektoren. Ein Uebergang zwischen ihnen ist in
     der Zeitentwicklung nicht moeglich.
3. **Wechselwirkung verschiedener Pole:**
   - Mit a = |phi_1|^2 und b = |phi_2|^2 gilt U(a + b) - U(a) - U(b) = a b [-2 + 1,5 (a + b)]. Der g4-Term hat
     keinen Kreuzterm, und der Kreuzterm haengt nicht von den Phasen ab.
   - Er ist anziehend fuer a + b < 4/3 und abstossend bei starker Kernueberlappung. Im Schwanz faellt er wie
     e^{-2 kappa d} mit kappa = sqrt(1 - omega^2).
   - Gleiche Pole koppeln linear ueber die Schwanzueberlappung: ~ cos(alpha) e^{-kappa d}, in Phase anziehend
     [L, Standard].
   - Die Richtung von QD1 ist damit bei grossem d plausibel. Bei d = 2R (die Waende beruehren sich) gilt die
     Asymptotik nicht; der Faktor 3 ist nicht ableitbar.
4. **Verschmolzener Dreier:** Ein voll verschmolzener Dreier ist ein gleich gemischter Q-Ball mit den Ladungen
   (Q1, Q1, Q1).
   - Fuer g4 = +0,1 gilt E_mix(3 Q1; g4/3) <= E_mix(3 Q1; g4) < 3 E_1(Q1; g4), sofern E/Q laengs des Astes mit Q faellt.
     QB-BS-2D zeigt das bei g = 0: E/Q = 0,998 bei q = 13 und 0,821 bei q = 100 [P].
   - **Endet der Fluss in (c) im verschmolzenen Ball, ist QD2 (Plan) vorab ableitbar.** Neu ist dann nur der Betrag der
     Bindung. Informativ bleiben die Gestalt des Flussendes (verschmolzen, Dreieck oder Zwischenform), die Dynamik und
     QD3.
5. **Zerfall in einen Ein-Pol-Q-Ball:** Bei getrennter Ladungserhaltung wird der Dreier nur dann zu einem
   Ein-Pol-Klumpen, wenn zwei Pole ausgestossen oder abgestrahlt werden.
   - Kriterium (ii) von QD3 folgt aus Kriterium (i): Ein Anteil >= 0,9 je Pol im Klumpengebiet ergibt einen
     Hoechstanteil <= 1/(1 + 2 * 0,9) = 0,36 < 0,6. Es wird trotzdem gefuehrt.
6. Fuer g4 = 0 sind alle Richtungen gleichwertig (U(3)). (a) prueft dort nur die Umsetzung.

## 3. Numerik

- **Gitter:** periodisch, L = 64, N = 256 je Richtung (h = 0,25), Ursprung auf einem Knoten. Ableitungen spektral
  (scipy.fft, 1 Thread).
  - Gitterprobe (Rauchlauf, Einpolball g4 = +0,1, Q = 60): N = 320 bei gleichem L aendert E um 2,2e-16 relativ.
  - Bildwechselwirkung ueber den Rand: Abstand >= 64 - Dreiergroesse, Schwanz e^{-kappa * 40} < 1e-6 [Schaetzung].
- **Festladungsrelaxation (Gradientenfluss von E_Q):**

      psi_a <- F^{-1}[ F(psi_a + tau (c - U'(S) - 2 g4 |psi_a|^2 + omega_a^2) psi_a) / (1 + tau (k^2 + c)) ],

  mit omega_a = Q_a/Lambda_a nach jedem Schritt, tau = 0,5, c = 1. Der Fixpunkt ist die stationaere Gleichung.
  - Konvergenz: max |Residuum| < 1e-7 in (a) bzw. < 1e-8 beim Einpolball in (b) und (c). Hoechstens 8000 Schritte.
- **Eingespannte Relaxation ("relaxiert" in b):** derselbe Fluss. Nach jedem Schritt wird jede Komponente spektral so
  verschoben, dass ihr |psi_a|^2-Schwerpunkt auf ihrem Stift liegt.
  - Ende, wenn sich E_Q ueber 50 Schritte um < 1e-11 relativ aendert; hoechstens 4000 Schritte bzw. 80 s.
- **Radialer Bezug (a):** eine Komponente mit Kopplung g_eff. Zentrierte Zellen dr = 0,01 bis r = 60 (Dirichlet),
  Fluss-Laplace, gleiches E_Q-Verfahren (tau = 1, c = 1, tridiagonal), Residuum < 1e-10.
  - Kontrolle mit dr = 0,02.
  - Externer Abgleich bei g = 0, Q = 100 gegen QB-BS-2D: E_fein = 82,13970757077503 [P,
    qb-bs-2d/lauf-69/auswertung.json]. Im Rauchlauf -1,8e-7 relativ (dr = 0,01).
- **Startzustand in (a):** der radiale g = 0-Ball gleicher Gesamtladung, mit n_a auf die Komponenten verteilt. Der Fluss
  muss die Wirkung von g4 also selbst finden.
- **Einpolball in (b) und (c):** radialer g4-Ball als Start, danach 2D-Fluss bis Residuum < 1e-8.
- **Zeitentwicklung:** Stoermer-Verlet (Kick-Drift-Kick), spektraler Laplace, dt = 0,025, Messung alle 0,5.
  - Stabilitaetsgrenze grob 2/sqrt(max k^2 + 1) = 0,11.
  - Genauigkeitsprobe: c1 bei g4 = +0,1 zusaetzlich mit dt = 0,0125 (Lauf c1dt_p01, gleiche Saat), nur beschreibend.
  - Die Ladungen sind in diesem Verfahren bis auf Rundung erhalten [M]: Kick und Drift aendern Im(conj(phi) pi)
    jeweils nicht.
- **Rauschen:** phi_a += eps eta_a sqrt(S0) und pi_a += eps omega_1 eta'_a sqrt(S0).
  - eta ist ein glattes komplexes Gaussfeld (Filter exp(-k^2/(2 k_c^2)), k_c = 2, Effektivwert 1).
  - eps = 1e-3. S0 ist die Startdichte, das Rauschen sitzt also nur auf den Baellen.
  - Saat 1 im Hauptlauf, Saat 2 als Probe beim Mischungs-g4.
- **Zeit und Speicher (Rauchlauf r1):**
  - Zeitschritt 7,9 ms (ein Pol) bzw. 14,5 ms (drei Komponenten).
  - Flussschritt 6,7 bis 11,7 ms. Hoechster Speicher 115 MB.
  - Eine Zeitentwicklung bis T = 200 dauert also etwa 2 min.

## 4. Parameter (vorab gebunden)

- beta = 1/2; g4 in {-0,1; 0; +0,1}.
- **(a):**
  - Gesamtladung Q in {30, 60, 90, 120, 180}.
  - Richtungen: ein Pol (1, 0, 0), zwei Pole (1, 1, 0)/sqrt 2, gleich gemischt (1, 1, 1)/sqrt 3, mit Q_a = Q n_a^2.
  - QD0 wertet alle 45 Zustaende aus. Der Mischungs-g4 wird bei Q = 60 und 180 bestimmt.
- **(b), (c):**
  - Einpolball mit Q1 = 60 je Ball. Das liegt ueber der Townes-Grenze von etwa 12 und unter dem Duennwandbereich.
  - Rauchlauf bei g4 = +0,1: omega = 0,8306, R_halb = 3,193.
- **Radius R = R_halb des Einpolballs je g4:** Abstand vom Zentrum, bei dem |psi|^2 auf die Haelfte des Zentralwerts
  faellt, laengs der x-Achse linear interpoliert. R_rms = sqrt(int r^2 |psi|^2 / int |psi|^2) wird nur berichtet.
- **(b):** d/R in {0,5; 0,75; 1; 1,25; 1,5; 1,75; 2; 2,25; 2,5; 2,75; 3; 3,5; 4; 5; 6}. Relaxiert bei
  d/R in {1,5; 1,75; 2; 2,25; 2,5; 3; 4}.
- **(c):**
  - Dreieck mit Seite d0 = 2R und Umkreisradius rho = d0/sqrt 3. Pol a sitzt an Ecke a (Winkel 90, 210, 330 Grad).
  - Klumpengebiet: Kreis mit R_K = rho + 3R um den momentanen Gesamtladungsschwerpunkt.
  - Fluss ohne Stifte bis max abs(Residuum) < 1e-7, hoechstens 12000 Schritte bzw. 170 s.

## 5. Messgroessen

**(a) Kontrolle:**
- Je (Q, g4, Richtung): E_2D, omega_a, Residuum, E_rad(g_eff, Q) und delta = E_2D/E_rad - 1.
- Gewinner je (Q, g4) ist die Richtung mit kleinstem E.

**(b) Zwei Q-Baelle in Ruhe im Abstand d:** E_int = E_Q[Konfiguration] - (Summe der Einzelenergien) bei festen
Ladungen. "Eingespannt" heisst: Die Profile der Einzelbaelle (exakte Gitterloesung, spektral verschoben) bleiben fest,
die Ladungen auch, die Frequenz folgt aus Q/Lambda.
- gleicher Pol in Phase: eine Komponente psi_A + psi_B mit Ladung 2 Q1;
- gleicher Pol gegenphasig: psi_A - psi_B mit Ladung 2 Q1;
- verschiedene Pole: psi_A in Komponente 1, psi_B in Komponente 2, je Q1;
- Dreieck aus drei Polen mit Seite d, je Q1 (nur Einordnung fuer QD2);
- verschiedene Pole relaxiert: eingespannte Relaxation mit Schwerpunktstiften (Abschnitt 3).
- Fuer gleiche Pole gibt es keine Stiftrelaxation, weil beide Baelle in derselben Komponente liegen.

**(c) Dreier aus drei Polen:**
- **Fluss ohne Stifte** vom eingespannten Dreieck:
  - E_ende, Bindung B = 3 E_1 - E_ende, Paarabstaende D_ab der Komponentenschwerpunkte, Anteil jeder Komponente
    (|psi_a|^2) im Klumpengebiet.
  - Gestalt: verschmolzen bei max D_ab < 0,25 R, Dreieck bei min D_ab > R, sonst Zwischenform.
  - Vergleich mit dem gleich gemischten Ball Q = 180 aus (a).
- **Zeitentwicklung bis T = 200** mit Rauschen (Abschnitt 3):
  - c1 startet vom eingespannten Dreieck: Baelle in Ruhe, jeder mit eigener Drehung omega_1.
  - c2 startet vom Flussendzustand mit dessen omega_a.
  - Gemessen: E(t), Q_a(t) und Q_a,in(t), die Ladung von Pol a im Klumpengebiet.
  - Dazu Komponentenschwerpunkte, Paarabstaende und Bilder bei t = 0, 100, 200.
- c1 laeuft bei allen drei g4, c2 nur beim Mischungs-g4.

## 6. Urteilsregeln (vorab, in Zahlen)

Die Vorhersagen und Wahrscheinlichkeiten der Karte bleiben unveraendert.

| Nr | Plan (Hauptregel) | Kartenwortlaut |
|---|---|---|
| QD0 | eingetroffen, wenn alle 45 Zustaende aus (a) konvergiert sind (2D und radial) und max abs(delta) < 0,01; nicht eingetroffen, wenn ein konvergierter Zustand abs(delta) >= 0,01 hat; sonst nicht auswertbar | gleich (der Kartenwortlaut ist schon in Zahlen) |
| QD1 | je g4: A_gleich = abs(E_int(gleicher Pol, Phase, d = 2R)), A_versch = abs(E_int(verschiedene Pole, d = 2R)), beide eingespannt. Eingetroffen, wenn A_versch <= A_gleich/3 bei allen drei g4; sonst nicht eingetroffen | wie Plan, A_versch aber aus der relaxierten Stiftrechnung bei d = 2R ("aus relaxierten bzw. eingespannten Zustaenden") |
| QD2 | beim Mischungs-g4 (aus (a); erwartet +0,1): eingetroffen, wenn B >= 1e-3 * 3 E_1 und jede Komponente >= 0,98 ihres abs(psi_a)^2 im Klumpengebiet hat; sonst nicht eingetroffen. E_ende ist eine obere Schranke fuer das Flussende; der Flussstatus wird berichtet | eingetroffen, wenn E_ende < 3 E_1 (1 - 1e-6) (nur der Energievergleich) |
| QD3 | nur wenn QD2 (Plan) eingetroffen, sonst "entfaellt". Lauf c1 beim Mischungs-g4, Saat 1. Gueltig bei erreichtem T = 200, abs(dE/E) <= 1e-3 (Tor wie QBALL-PYRO-1) und abs(dQ_a/Q_a) <= 1e-8. Eingetroffen, wenn (i) Q_a,in(t)/Q_a(0) >= 0,9 fuer alle a und alle Messzeiten bis t = 200 und (ii) bei t = 200 max_a Q_a,in / sum_b Q_b,in <= 0,6; nicht eingetroffen, wenn (i) oder (ii) verletzt; ungueltig: nicht auswertbar | gleiche Regel fuer Lauf c2 ("der Dreier" ist der Zustand aus QD2) |

- Mischungs-g4 ist das g4 in {-0,1; +0,1}, bei dem die gleiche Mischung in (a) bei Q = 60 und Q = 180 das kleinste E
  hat. Erfuellen beide oder keines diese Bedingung, sind QD2 und QD3 nicht auswertbar.
- Vermerk: Ist das Flussende verschmolzen, war QD2 (Plan) vorab ableitbar (Abschnitt 2.4). Die Auswertung schreibt
  diesen Vermerk mechanisch.
- Nur beschreibend, ohne Urteil: Wechselwirkungskurven und gegenphasiger Kanal, c1 bei g4 = 0 und -0,1, Saat 2,
  Gestalt und Verschmelzzeit.

## 7. Laeufe (.69, kleintest.sh, Spuren p4000a und p4000b, numpy/scipy auf der CPU in der Einheit)

GPU-Nutzung entfaellt: Die Felder sind klein (3 x 256^2), ein Zeitschritt kostet auf einem Kern 15 ms.

| Lauf | Inhalt | Spur | geschaetzt |
|---|---|---|---|
| a | (a) alle 45 Zustaende, extern | p4000b | 3 min |
| b_m01, b_0, b_p01 | (b) je g4 | p4000a | je 3 bis 5 min |
| c_p01 | Fluss, c1 und c2 bei +0,1 | p4000b | 6 bis 7 min |
| c_0, c_m01 | Fluss und c1 bei 0 und -0,1 | p4000b | je 4 bis 5 min |
| c1s2_p01 | c1 mit Saat 2 bei +0,1 | p4000a | 3 min |
| c1dt_p01 | c1 mit dt = 0,0125 bei +0,1, Saat 1 | p4000a | 5 min |
| aw | auswertung.py | p4000a | < 1 min |

Laufskripte: code/laeufe-p4000a.sh und code/laeufe-p4000b.sh. Hauptdateien landen auf der .69 in
runde42-qball-dreipol/lauf/, danach per scp in lauf-69/.

## 8. Erwartungen des Agenten (vorab, ohne Urteil)

- E0: QD0 trifft ein mit abs(delta) ~ 1e-6 oder kleiner.
- E1: QD1 trifft ein; A_versch/A_gleich ~ 0,05 bis 0,3.
- E2: Der Fluss verschmilzt den Dreier zum gemischten Ball. QD2 (Plan) trifft dann ein, ist aber ableitbar.
- E3: In c1 ziehen sich die Pole langsam an und bleiben im Klumpengebiet. QD3 trifft ein.

## 9. Rauchlauf und Leitungstest (vor dem Einfrieren)

- r1 (rauch-69/r1.json): Zeiten, Speicher, externer Radialabgleich, QD0-Teilmenge (Q = 60, g4 = +-0,1), Einpolball
  g4 = +0,1 mit Gitterprobe N = 320, Zeitentwicklung eines Einpolballs bis t = 10 (Erhaltung).
- QD0-Kontrolle voll (rauch-69/a/): derselbe Modus a wie im Hauptlauf. Der Hauptlauf wiederholt ihn mit dem
  eingefrorenen Code.
- Leitungstest (rauch-69/pipe/): Modi b und c mit Q1 = 25, d/R in {2, 6}, 20 Relaxationsschritten, 30 Flussschritten
  und T = 2, dazu auswertung.py. Er prueft nur, dass der Weg durchlaeuft. Die Zahlen sind keine Hauptwerte und werden
  nicht gelesen.

## 9a. Aenderungen vor dem Einfrieren (offen gelegt)

1. Radialer Bezug: Der erste volle Kontrolllauf (a) brach bei Q = 180, g_eff = -0,1 mit Ueberlauf ab (tau = 1;
   rauch-69/a/a-erstlauf-abbruch.log). Danach tau = 0,5 und bei nicht endlichen Werten Neustart mit halbem tau.
   Der zweite Lauf (rauch-69/a/a.json): alle 45 Zustaende konvergiert, max abs(delta) = 5,3e-7.
2. Energietor fuer QD3 von 1e-4 auf 1e-3 gesetzt (wie QBALL-PYRO-1), dazu die dt/2-Probe c1dt_p01. Anlass: Im
   Leitungstest (Q1 = 25, T = 2) schwankte E um bis zu 4e-6. Das Tor prueft nur die Gueltigkeit, nicht den Ausgang.
3. Im Leitungstest habe ich zur Fehlersuche den Flussendzustand angesehen. Er war mechanisch als "verschmolzen"
   eingestuft, und ich wollte pruefen, ob die Schwerpunktmessung am periodischen Rand verfaelscht. Ergebnis: Bei
   Q1 = 25 (breite Baelle, d0 = 2R = 3,8 bis 4,1) rueckten die Schwerpunkte nach 30 Flussschritten von rho = 2,2 bis
   2,4 auf 0,27 bis 0,86 zusammen. Die Messung war also nicht verfaelscht.
   - Das ist kein Hauptwert (anderes Q1, ungeloester Fluss), zeigt aber die Richtung des Flusses bei breiten Baellen.
   - Regeln und Schwellen habe ich danach nicht geaendert.

## 10. Grenzen

- 2+1 statt 3+1. Kein Gitter mit Tetraederstruktur; die Anisotropie g4 steht stellvertretend fuer die
  Tetraedersymmetrie (Karte).
- Nur sum_a |phi_a|^4 als Anisotropie. Andere unter T_d erlaubte Terme fehlen, etwa phasenabhaengige Quartterme oder
  die kubische Invariante x y z aus FARBE-SCHREIBTISCH, Punkt 2.
- Kein Eichfeld, keine Quantenkorrektur.
- Gleiche Pole nur eingespannt, nicht relaxiert.
