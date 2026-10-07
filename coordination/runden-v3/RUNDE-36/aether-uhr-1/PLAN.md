# AETHER-UHR-1: Plan (Code-Agent fuer die Leitung, Runde 36, explorativ)

- Start 2026-10-03 23:40:10 CEST (date). Code ab 23:52, Rauch 1 und 2 ab 21:56:41 UTC, Plan ab 2026-10-04 00:01:49 CEST.
- Karte: KARTE.md (Leitung, 23:39:12 CEST). Vorhersagen U0 bis U3 und ihre Schwellen sind unveraendert uebernommen.
- Kennzeichen: [M] vorab ableitbar, [L] Literatur aus dem Gedaechtnis, [H] Hypothese, [E] gerechnet (synthetisch),
  [F] von mir vor dem Einfrieren festgelegt (die Karte laesst es offen).
- Code: code/aether.py (Laeufe), code/auswertung.py (Urteile, mechanisch), code/bilder.py (nur Darstellung),
  code/laeufe.sh (Reihenfolge je Spur). Rechnen nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4.

## 1. Modell

- **Feld A** (M1, komplex, c_A = 1), U(S) = S - S^2 + S^3/2 (beta = 1/2), S = |A|^2:
  - A_tt = (d_x - i a)^2 A - U'(S) A + (g/2) B^2 A, mit a(t) = Integral E dt (zeitliche Eichung).
  - Das gleichmaessige Feld E(t) wirkt nur auf die A-Ladung; auf dem Gitter als Peierls-Phase th = h a (wie
    QBALL-GITTER-1).
- **Feld B** (reell): B_tt = c_B^2 B_xx - (m_B^2 - g |A|^2) B.
  - Die Rueckwirkung (g/2) B^2 A folgt aus derselben Lagrangedichte; Energie ist erhalten, bis auf die Feldarbeit.
  - Lagrangedichte: |A_t|^2 - |D_x A|^2 - U(S) + (B_t^2 - c_B^2 B_x^2)/2 - (m_B^2 - g S) B^2/2.
- **Werte [F]:**
  - m_B = 1 (gleich der A-Vakuummasse) und g = m_B^2 = 1.
  - Damit ist B im Beutelinneren (S ~ 1) praktisch masselos: m_in^2 = m_B^2 - g S_0 = 1 - S_0 ~ 7e-7.
  - Begruendung: Die Karte rechnet mit einer Hohlraummode "Wellengeschwindigkeit c_B, Frequenz ~ c_B/L'", also einer
    masselosen stehenden Welle. Aussen hat B die Masse 1 und propagiert nicht.
  - Rauch 2 ergab Omega_B(0) = 0,1508 (c_B = 1) und 0,2322 (c_B = 1,7), beide weit unter m_B = 1. Es gibt je drei
    gebundene Moden: lambda = 0,0227 / 0,0892 / 0,1950 bzw. 0,0539 / 0,2102 / 0,4526.
- **Gitter:**
  - h = 0,05, dt = 0,01, Yoshida 4. Ordnung, mitlaufendes Fenster der Laenge 160 (Verschub um 5).
  - Schwamm je 30 an beiden Enden fuer A und B; Abfluss, Feldarbeit und Herausgefallenes werden gebucht.
- **Kontinuumsnaehe:**
  - Wandbreite des Beutels ~ 1/sqrt(2) bis 1,4/gamma.
  - Die Phase im bewegten Inneren aendert sich je Gitterplatz um k h = omega gamma v h ~ 0,027 (v = 0,6).
  - Die lineare Gitterdispersion korrigiert um (k h)^2/12 ~ 6e-5 [M]. Pruefung durch die Gitterprobe (Abschnitt 5).

## 2. Ausgangszustand

- **Beutel:** stationaere Gitterloesung A = phi_n e^(i omega t), platzzentriert.
  - Newton mit Randzeile: Gesamtnorm h sum phi^2 fest, omega^2 als Unbekannte.
  - Grund: Der duennwandige Beutel hat bei festem omega eine fast freie Wandabstandsmode (omega^2 - 1/2 ~ 2,5e-13).
  - Startwert ist die Kontinuumsform S = 2k^2/(1 + D cosh(2 k x)), k^2 = (1 - D^2)/2. D ist so gewaehlt, dass die
    Halbwertsbreite von S genau 21 betraegt [F; Karte: Laenge >= 20].
  - Rauch 2: Newton-Rest 1,6e-13; Halbwertsbreite der Ladungsdichte 21,00006; M0 = 21,707, Q0 = 29,698,
    omega^2 - 1/2 = 2,49e-13.
- **B-Mode:**
  - unterste Eigenmode f des linearisierten B-Problems -c_B^2 Lap_h + (m_B^2 - g S) im Beutelprofil, mit denselben
    Gitterraendern wie die Dynamik
  - B = b f mit max|f| = 1, B_t = 0, Amplitude b = 1e-3 [F]
  - Rueckwirkung ~ (g/2) b^2 = 5e-7 relativ zu U' ~ 1 [M]; geprueft in Abschnitt 5

## 3. Beschleunigungsprotokoll [F]

- **Ablauf:**
  - Ruhephase T_p = 480 ohne Feld.
  - Dann dreimal: Rampe der Dauer T_r = 500 mit E(t) = E_k sin^2(pi s/T_r), danach Plateau T_p = 480 ohne Feld.
  - Das Feld ist am Rampenende glatt abgeschaltet (E und dE/dt = 0). Das Plateau ist der Nachlauf zum Messen.
  - Gesamtdauer 3420.
- **Feldstaerke:**
  - E_k = 2 M0 (gamma_k v_k - gamma_{k-1} v_{k-1})/(Q0 T_r) mit den Zielen v_k = 0,2 / 0,4 / 0,6 (Impulsbilanz
    gamma M v = Q Integral E dt).
  - Bei T_r = 500: E_k ~ 6,0e-4 / 6,8e-4 / 9,2e-4.
  - Hoechste Eigenbeschleunigung ~ Q0 E/M0 ~ 1,3e-3.
- **Wahl von T_r und T_p:**
  - Rauch 2 mit T_r = 150 und T_p = 120 zeigte Eigenschwingungen des Beutels nach den Rampen: Laengenschwankung bis 0,065
    (0,4 %), Schwerpunktrest 0,019, Phasenrest 0,03.
  - Fuer sin^2-Rampen faellt die Anregung einer Mode der Frequenz w wie (w T_r)^-3 [M]. T_r = 500 senkt sie also um
    etwa das 37-Fache.
  - Die langsamste Beutelmode hat w ~ pi c_s/L ~ 0,1 mit c_s^2 = 1/2 der Q-Materie [M]. Das gibt w T_r ~ 50.
  - Die Luecke zwischen B-Grundmode und zweiter Mode ist ~ 0,14 bis 0,25. Das gibt Delta w T_r ~ 70 bis 120.
  - T_p = 480 umfasst bei v = 0,6 und c_B = 1 neun B-Perioden.
  - Die Werte sind nach Rauch 2 und Zeitbudget gewaehlt, nicht nach Schwellen; keine Schwelle wurde geaendert.

## 4. Messvorschriften

- **Messabstand:** 0,25. Ausgewertet wird jede Ruhe- und Plateauphase ab ihrem Beginn plus T_EIN = 20 bis zu ihrem Ende
  [F].
- **Ort und Schnelle:**
  - X(t) ist die Mitte der beiden Halbwertsstellen von S = |A|^2 (lineare Interpolation).
  - v ist die Steigung einer Ausgleichsgeraden durch X(t) ueber das Plateau.
  - gamma_A = (1 - v^2)^(-1/2), gamma_B = (1 - v^2/c_B^2)^(-1/2).
- **Beutellaenge L:**
  - Halbwertsbreite der Ladungsdichte rho = 2 Im(conj(A) A_t) (Karte), gemittelt ueber das Plateau.
  - Kontrolle: Halbwertsbreite von S.
- **A-Uhr omega_A (Eigenzeit-Uhr) [F]:**
  - Gemessen wird die Phase des eichkovarianten Felds chi = e^(-i a x) A am Beutelmittelpunkt X(t), linear zwischen den
    Nachbarplaetzen interpoliert und abgewickelt.
  - omega_A ist die Steigung der Ausgleichsgeraden ueber das Plateau, also die Laborzeit-Rate der A-Phase entlang der
    Bahn des Mittelpunkts.
  - Begruendung [M]: Fuer den exakt geboosteten Beutel ist chi = phi(gamma(x - v t)) e^(i omega gamma (t - v x)). Am Ort
    x = v t ist die Phase omega t/gamma, die Rate also omega/gamma_A.
  - Die reine Zeitableitung am festen Ort gaebe omega gamma; der Unterschied ist der Dopplerbeitrag k v mit
    k = omega gamma v.
  - Der Faktor e^(-i a x) entfernt den Eichanteil a v, der in der zeitlichen Eichung nach dem Feld in der Phase steht.
  - Pruefung ueber die Kontrolle c_B = 1 (K1): Dort muss omega_A gamma_A/omega_A(0) = 1 herauskommen.
- **B-Uhr Omega_B:**
  - Signal s_B(t) = gewichtetes Mittel von B im mitbewegten Fenster |x - X(t)| < 5 mit cos^2-Gewicht.
  - Frequenz: FFT-Startwert, dann Anpassung von a cos(Omega t) + b sin(Omega t) + c mit Variablenprojektion.
  - Begruendung [M]: Im mitbewegten Fenster ist die Frequenz an jedem festen Abstand xi = x - X gleich Omega'/gamma_B
    (Omega' = Frequenz im B-Ruhesystem des Topfs). Das Fenstergewicht aendert die Frequenz nicht.
  - Kontrolle: B im Mittelpunkt allein (Bc).
- **Verhaeltnis:** R = Omega_B/omega_A je Plateau, ausgewertet als R(v)/R(0) mit R(0) aus der Ruhephase desselben Laufs.

## 5. Proben

- **Adiabatik-Probe (halbe Beschleunigung):** T_r = 1000 und halbe E_k, sonst gleich. Laeufe A-100, A-115, A-170.
- **Gitterprobe (halbes h):** h = 0,025, dt = 0,005, sonst gleich. Laeufe G-100, G-115, G-170.
- **Rueckwirkungsprobe (K2):**
  - Lauf R0 mit b = 0 (nur Ruhephase bis t = 480; ohne B ist c_B bedeutungslos).
  - Vergleich des Profils S bei t = 480 mit den drei Hauptlaeufen (gleiches h und dt).
  - Bedingung: max|S_b - S_0|/max S_0 < 1e-3 (Auftrag). Berichtet werden auch die Aenderung von L(0) und omega_A(0).
- **Bilanzen:**
  - Energie: H + Schwammabfluss + Herausgefallenes - H(0) - Feldarbeit, bezogen auf M0.
  - Ladung: Q + Abfluss + Herausgefallenes - Q(0), bezogen auf Q0. Nur berichtet.

## 6. Urteilsregeln (mechanisch, code/auswertung.py)

Die Urteile werden aus den Hauptlaeufen H-* gebildet; v ist jeweils die gemessene Schnelle des Plateaus.

| Nr | Regel (Schwellen aus der Karte) | Zusatz [F] |
|---|---|---|
| U0 | c_B = 1: fuer alle drei Plateaus abs(R(v)/R(0) - 1) <= 1e-3 und abs(L(v) gamma_A/L(0) - 1) <= 0,01 | L = Halbwertsbreite der Ladungsdichte |
| U1 | c_B = 1,15: fuer alle drei Plateaus abs((R/R0 - 1) - S)/S <= 0,20 mit S = v^2 (1 - 1/c_B^2) | S am gemessenen v (bei v_nom: 0,0098 / 0,039 / 0,088) |
| U2 | c_B = 1,70: dieselbe Regel | Sollwerte bei v_nom 0,026 / 0,105 / 0,235 |
| U3 | alle neun Plateaus (drei c_B, drei v): abs(L(v) gamma_A/L(0) - 1) <= 0,01 | "nicht mit gamma_B": wo gamma_A und gamma_B um mehr als 2 % auseinanderliegen, folgt das aus der 1-%-Regel |

- **"nicht auswertbar" [F], wenn:**
  - ein beteiligter Lauf nicht "fertig" ist,
  - ein Wert nicht endlich ist,
  - eine Plateauschnelle mehr als 0,02 von 0,2 / 0,4 / 0,6 abweicht oder die Ruhephase abs(v) > 1e-3 hat,
  - die Adiabatik-Probe oder die Gitterprobe fuer dieselbe Vorhersage ein anderes Urteil gibt, auch "nicht auswertbar"
    (Vermerk mit dem Probenurteil),
  - oder K2 nicht erfuellt ist.
- Wurde eine Probe gar nicht gerechnet (keine Dateien), bleibt das Haupturteil mit Vermerk.
- **Kontrollen, kein Kartenurteil [F]:**
  - **K1 Uhrwahl (c_B = 1):** abs(omega_A gamma_A/omega_A(0) - 1) <= 1e-3 und abs(Omega_B gamma_B/Omega_B(0) - 1) <= 1e-3
    auf allen Plateaus.
  - **Zusatz Z-K (c_B = 1,15 und 1,7):** Abweichung von der exakten Kinematik (Abschnitt 7) abs(R/R0 - 1 - K) <=
    0,05 abs(K) + 2e-4.
  - Beide werden berichtet, aendern aber kein Urteil.

## 7. Schreibtisch vor der Rechnung [M]: Die Karte rechnet mit der fuehrenden Ordnung

- **Kinematik:**
  - Im B-Ruhesystem (Lorentz-Transformation mit c_B) steht der Topf still. Er hat dort die Laenge L gamma_B/gamma_A,
    weil der Beutel im Labor mit gamma_A verkuerzt ist.
  - Seine Grundfrequenz ist Omega' = sqrt(lambda(c_B gamma_A/gamma_B)). Dabei ist lambda(c) der kleinste Eigenwert von
    -c^2 d_x^2 + V(x) im Ruheprofil V = m_B^2 - g S.
  - Im Labor zaehlt die mitbewegte Uhr Omega'/gamma_B, die A-Uhr omega/gamma_A.
  - Also R(v)/R(0) = (gamma_A/gamma_B) sqrt(lambda(c_B gamma_A/gamma_B)/lambda(c_B)) =: 1 + K(v).
- **Harter, masseloser Hohlraum** (lambda ~ c^2): R/R0 = gamma_A^2/gamma_B^2. Das ist die Formel der Karte, und exakt
  gilt R/R0 - 1 = v^2 (1 - 1/c_B^2)/(1 - v^2).
- **Folge fuer U1 und U2:** Die Sollwerte der Karte sind die fuehrende Ordnung v^2 (1 - 1/c_B^2). Selbst der harte
  Hohlraum liegt um den Faktor gamma_A^2 = 1,042 / 1,190 / 1,5625 darueber (v = 0,2 / 0,4 / 0,6).
- **Weiche Waende:**
  - Hier sind die Waende weich, der Gradientenanteil f = c^2 <-d_x^2>/lambda liegt unter 1. Rauch 2: f = 0,827
    (c_B = 1) und 0,796 (c_B = 1,7).
  - Fuer kleines v gilt K ~ (1 + f) (v^2/2)(1 - 1/c_B^2), also 0,90-mal der Kartenwert.
  - Im Ganzen liegt K bei v = 0,6 um etwa +37 % (c_B = 1,7) bzw. +40 % (c_B = 1,15) ueber dem Kartenwert.
- **Vorab-Erwartung [M]:** Folgt die Dynamik dieser Kinematik, verfehlen U1 und U2 die 20-%-Schranke bei v = 0,6 sicher,
  bei 0,2 und 0,4 nicht. Der Ausgang von U1/U2 steht also durch die Reihenentwicklung der Karte vorab fest.
- **Auch U0 und U3 sind vorab ableitbar:**
  - A ist exakt lorentzinvariant mit c = 1.
  - Fuer c_B = 1 ist das ganze System invariant.
- **Was die Rechnung prueft:** nur, ob die Dynamik (langsame Beschleunigung, Mitfuehrung der B-Mode, Gitter, Rueckwirkung)
  dieser Kinematik folgt. Deshalb die Zusatzprobe Z-K mit K(v) als schaerferer Sollkurve.
- K(v) wird in auswertung.py aus dem Ruheprofil jedes Laufs berechnet (Eigenwerte des Gitteroperators). Es ist keine
  Messgroesse, sondern Mathematik.

## 8. Rauchlaeufe (offengelegt)

- **Rauch 1** (21:56:41 bis 21:57:43 UTC): c_B = 1,7, T_r = 150, T_p = 120.
  - Fehler gefunden: In der Halbwertsbreite stand cosh = (2 + D)/D statt (1 + 2D)/D. Der Beutel war dadurch 20,0 statt 21
    lang.
  - Vor Rauch 2 berichtigt. Sonst lief alles: Energiebilanz 7,8e-10, Ladung 1e-14, 61 s Wandzeit.
- **Rauch 2** (21:58:24 bis 21:59:28 UTC): c_B = 1,0 und 1,7, T_r = 150, T_p = 120, ausgewertet mit auswertung.py.
  - Ich habe dabei folgende Werte gesehen (v = 0,2 / 0,4 / 0,6, gemessen 0,19998 / 0,39996 / 0,59979):

    | c_B | Groesse | v = 0,2 | v = 0,4 | v = 0,6 |
    |---|---|---|---|---|
    | 1,0 | R/R0 - 1 | -5,2e-4 | -1,26e-3 | -6,1e-3 |
    | 1,0 | L gamma_A/L0 - 1 | -1,5e-4 | -3,0e-4 | +3,2e-4 |
    | 1,7 | R/R0 - 1 | 0,02420 | 0,11103 | 0,32118 |
    | 1,7 | K(v) | 0,02443 | 0,11101 | 0,32306 |
    | 1,7 | Kartenwert | 0,02616 | 0,10462 | 0,23527 |

  - Die Abweichungen bei c_B = 1 gehen mit der Eigenschwingung des Beutels nach zu kurzen Rampen einher: Fit-Rest der
    B-Schwingung bis 6 %, Laengenschwankung 0,4 %.
  - Bei T_p = 120 deckt die Anpassung nur etwa zwei B-Perioden ab.
  - Folge: T_r und T_p der Hauptlaeufe wie in Abschnitt 3. Schwellen und Regeln blieben unveraendert.
- **Rauch 3** (22:02:23 bis 22:02:37 UTC): Gitter h = 0,025, c_B = 1,15, bis t = 60, nur zur Pruefung von Laufzeit und
  Fortsetzung.
  - Laufzeit 0,21 s je Zeiteinheit (h = 0,05: 0,067 s).
  - Ein Lauf mit Wandzeit-Abbruch bei t = 27 und Fortsetzung endete mit denselben Endwerten auf alle Stellen wie der
    durchgehende Lauf (X, L, Bilanzen).
  - Gitterwerte: Omega_B(0) = 0,16920, Newton-Rest 6,3e-13.
- auswertung.py und bilder.py liefen auf Rauch 2 fehlerfrei (rauch-69/a2/). Danach wurde in auswertung.py nur die Regel
  "Probe nicht gerechnet" eingefuegt (Abschnitt 6).
- Das Signal im mitbewegten Fenster (s_B) und der Mittelpunkt allein (Bc) gaben in Rauch 2 dieselben Frequenzen auf 1e-6.

## 9. Laufplan

- **Spuren:**
  - cpu3: H-100, H-115, H-170, R0, A-100, A-115, G-100
  - cpu4: G-115, G-170, A-170
  - je Spur nacheinander (code/laeufe.sh), also hoechstens zwei Laeufe zugleich
- **Laufzeiten:**
  - Hauptlauf etwa 230 s, Adiabatik-Probe etwa 330 s.
  - Gitterprobe etwa 4-mal so lang; sie wird in Wandzeit-Abschnitten von 500 s mit Checkpoint fortgesetzt.
- **Danach:** auswertung.py auf lauf/ -> lauf/auswertung.json, dann bilder.py.
