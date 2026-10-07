# INDUZIERT-ZUFALL-2D: Plan (Code-Agent, Runde 38)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 06:18:44 CEST (date). Code ab 06:33:36 CEST, Plantext ab
  06:41:16 CEST (date).
- **Vor diesem Plantext gerechnet:** die Rauchlaeufe kontrolle-r1, zeit-N64000 und r2 (Abschnitt 11). Was sie zeigen,
  steht dort. Die Vorhersagen und Schwellen der Karte sind davon unberuehrt.
- **Grundlage:**
  - KARTE.md: IZ0 bis IZ4 mit Schwellen unveraendert uebernommen.
  - INDUZIERT-1: PLAN Teil A, ERGEBNIS, Code. code/induziert.py ist unveraendert kopiert (sha256 b3867eac...).
    Benutzt werden daraus die exakte Blasensumme (Koeff, Gitterintegrale, tadpole, pi_base), torus_K, torus_gamma und
    lokal_K_batch, alle nur fuer Kontrollen.
- **Kennzeichen:**
  - [M] eigene Mathematik
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher
  - [F] Festlegung dieses Plans (von der Karte offen gelassen)
  - [K] Kartenberichtigung
  - [H] Hypothese

## 1. Netze

- **Zufall [F]:**
  - N gleichverteilte Punkte in [0, L)^2 mit L = sqrt(N), also Dichte 1 und mittlerer Abstand etwa 1.
  - Die Anzahl ist fest (Binomialprozess). "Poisson" der Karte heisst hier: unabhaengig und gleichverteilt.
  - Saat: numpy default_rng([20261004, N, saat]).
- **Periodische Delaunay-Triangulierung:**
  - Die Punkte werden mit ihren 8 Nachbarkopien (9N Punkte) per scipy.spatial.Delaunay (Qhull) trianguliert.
  - Behalten werden die Dreiecke, deren Schwerpunkt im Grundbereich liegt [F]. Jedes Torusdreieck hat genau ein Bild
    mit Schwerpunkt im Grundbereich. Das ist gleichwertig zu "mindestens eine Ecke im Grundbereich, doppelte
    entfernen", braucht aber keine Duplikatsuche.
  - Danach: Ecken modulo N, Orientierung positiv, Kantenvektoren im minimalen Bild.
- **Netzpruefungen in jedem Lauf** (gehen ins Tor, Abschnitt 6):
  - V - E + F = 0, E = 3N, F = 2N; jede Kante in genau zwei Dreiecken; drei verschiedene Ecken je Dreieck
  - alle Orientierungen > 0; Flaechensumme = L^2 auf <= 1e-9 relativ
  - Delaunay: Summe der beiden Gegenwinkel je Kante <= pi + 1e-9, also Kotangens-Gewichte >= 0
  - laengste Kante < L/4, damit das minimale Bild eindeutig ist
  - Beschreibend: kleinster und groesster Winkel, Kantenlaengen.
- **Regelmaessig (Kontrolle):** wie INDUZIERT-1 Teil A, Quadrate mit (1,1)-Diagonale, Knotenindex x L + y wie
  induziert.vidx.
  - Das Netz wird direkt gebaut, nicht ueber Qhull, weil je vier Punkte kozirkular sind.
  - Danach laeuft es durch dieselbe Kette wie die Zufallsnetze.

## 2. Materie, Konvention, log det' [M]

- **K:** P1-Steifigkeit = Kotangens-Laplace, allein aus den Kantenlaengen.
  - w_e = 1/2 Summe cot(Gegenwinkel), cot = (b^2 + c^2 - a^2)/(4 A_T), A_T aus der stabilen Heron-Form (Kahan).
  - K_ij = -w_ij, K_ii = Summe_j w_ij.
  - Das ist dieselbe Matrix wie V P^T G^-1 P in INDUZIERT-1 (Kontrolle K1).
- **Gamma = 1/2 log det' K**, masselos, Nullmode entfernt. Das ist Variante P aus INDUZIERT-1 Teil A, dort die
  geurteilte Groesse c_P.
- **det' K exakt per Erdung [M]:**
  - Fuer symmetrisches K mit K 1 = 0 und Rang N - 1 gilt adj K = (det' K / N) 1 1^T.
  - Also ist det K_(0) = det' K / N, wobei K_(0) die Matrix K ohne Zeile und Spalte des Knotens 0 ist.
  - INDUZIERT-1 rechnete dicht det(K + 1 1^T/N) = det' K. Das ist dieselbe Groesse; geprueft in K2 und K3.
  - Die Brief-Variante "K + 1 1^T M/Flaeche" waere dicht und fuer N = 64 000 nicht als duenne LU machbar.
- **log det K_(0):**
  - scipy splu (SuperLU) mit MMD_AT_PLUS_A, SymmetricMode, diag_pivot_thresh = 0 und ohne Equilibrierung.
  - log det = Summe log U_ii, summiert mit math.fsum.
  - K_(0) ist symmetrisch positiv definit. Bei jedem Aufruf wird geprueft: alle U_ii > 0 und perm_r = perm_c.
- **Konforme Mode** [Karte; Fortsetzung wie INDUZIERT-1 F3]:
  - Ecken-Skalierung l_ij(s) = l_ij exp(s (sig_i + sig_j)/2) mit sig_i = cos(k.x_i). In erster Ordnung ist das
    delta l/l = (sigma_i + sigma_j)/2 (Karte).
  - Gamma''(0) ist dann genau die Hesse-Form in den Knoten-Skalenfaktoren u_i [M].
  - Ihre Zeilensummen sind null: Die Kotangens-Gewichte sind skaleninvariant, K aendert sich unter globaler Streckung
    also gar nicht. Deshalb tritt die zufaellige Vakuumspannung des Netzes hier nicht auf.
- **Messgroesse (Karte):** c_P = Gamma''(0)/(k^2 A) mit A = L^2 = N. Polyakov: -1/(24 pi) = -0,0132629.
- **Flaechenglied** (wie INDUZIERT-1 K1):
  - In 1/2 log det' K gibt es kein globales Flaechenglied. Es gehoert zu det'(M^-1 K) = det' K A/(N det M).
  - Die Karte nennt "dasselbe Flaechenglied bzw. det'(M^-1 K)". Deshalb wird beschreibend auch c_D gerechnet:
    c_D = c_P - 1/2 (Summe_i log m_i)''/(k^2 A).
  - Dabei ist m_i = Summe_{T an i} A_T/3 die konzentrierte Massenmatrix (Heron). c_D ist also
    Gamma_D - 1/2 log A_sigma, verglichen mit Polyakov ohne Flaechenglied, wie in INDUZIERT-1.
- **Nicht gerechnet [F]:** die Varianten "linear in l" und "linear in s" aus INDUZIERT-1.
  - Auf einem Zufallsnetz verlassen sie die Ecken-Skalierung in zweiter Ordnung.
  - Dadurch nehmen sie ueber die Vakuumspannung je Kante ein Zufallsglied der Groesse ~ sqrt(N) mit, das nicht mit
    k^2 A skaliert [M]. Sie waeren rauschbeherrscht.
- **Knotenverschiebungen (Karte, Brief):**
  - x_i(s) = x_i + s e cos(k.x_i), mit e = k/abs(k) (laengs) und e senkrecht dazu (quer).
  - Die neuen Laengen kommen aus den verschobenen Punkten. Gerechnet wird die volle zweite Ableitung, also mit dem
    Glied zweiter Ordnung der Laengen.
  - INDUZIERT-1 Teil A hatte beschreibend nur die Hesse-Form in s (mit und ohne Gegenterm). Hier gilt die Karte:
    Steifigkeit der Moden selbst.
- **Kantenlaengen-Norm [F; Karte: "bei gleicher Kantenlaengen-Norm"]:**
  - n_Mode = Summe_e (dl_e/ds)^2 und kappa_Mode = Gamma''/n_Mode, also die Steifigkeit je Einheit quadrierter
    Kantenlaengen-Aenderung (wie INDUZIERT-1 F10).
  - Konform: dl/ds = l (sig_i + sig_j)/2. Verschiebung: dl/ds = (e_ij/l_ij).e (cos k.x_j - cos k.x_i).
  - Beschreibend dazu c = Gamma''/(k^2 A) je Amplitude.
- **Nicht-analytischer Anteil [F]: nicht gerechnet.**
  - In INDUZIERT-1 kam er aus der 4phi-Harmonischen der vollen Metrik-Antwort ueber ~200 Richtungen bei festem
    abs(k) (Teil A2).
  - Auf Zufallsnetzen braeuchte das je Richtung 6 Polarisationen mit je 4 LU, dazu Saatmittel gegen das
    Richtungsrauschen. Das sind mehrere tausend LU je Netz; die Zeitbox reicht nicht.
  - Fuer die Urteile wird er nicht gebraucht. Im Ergebnis steht er als offener Punkt.

## 3. Differenzenschema

- Gamma wird bei s = 0, +-h und +-2h gerechnet. D(h) = (Gamma(h) - 2 Gamma(0) + Gamma(-h))/h^2; Richardson
  R = (4 D(h) - D(2h))/3, Fehler O(h^4).
- **Schritte [F]:** konform h = 0,01; Verschiebung h = 0,01/abs(k), also Dehnungsamplitude 1 %.
- **Rundung [M]:**
  - abs(Gamma) ist etwa 3e4 bei N = 64 000.
  - LU-Rundung von ~1e-10 in Gamma gibt ~4e-6 absolut in D(h) bei h = 0,01.
  - Bei Gamma'' ~ 1 bis 20 sind das <= 1e-5 relativ.
- **Fehler am bekannten Fall (Brief):** regelmaessiges Netz gegen die exakte Blasensumme aus INDUZIERT-1 (induziert.py
  unveraendert).
  - Konform: Qh + Qt wie dort.
  - Verschiebung [M]: (N/2) u^+ Pi u + 2N Summe_d Gamma'_d (1 - cos k.d) mit u_d = 2 (d.e)(e^{ik.d} - 1), in der
    Fusspunkt-Konvention von INDUZIERT-1. Das zweite Glied kommt aus d^2 s/ds^2 = 2 abs(xi_j - xi_i)^2.
  - Torusgroessen: L = 16 und 64 (Kontrolle K4) sowie L = 256 (N = 65 536, so gross wie das groesste Zufallsnetz).
- **Schrittprobe K5:** Zufallsnetz N = 4000 mit Saat 999, h und eta = 0,005 / 0,01 / 0,02.

## 4. Saaten, k-Werte, Richtungen [F]

- **Richtungen:** 0, 45, 90 und 135 Grad, also kint = n (1,0), n (1,1), n (0,1), n (-1,1) und k = 2 pi kint/L.
  - Die Diagonalen haben bei gleichem n das sqrt(2)-fache abs(k).

| N | L | n konform | n Verschiebung | abs(k) Achse | abs(k) Diagonale | Saaten | Bloecke |
|---|---|---|---|---|---|---|---|
| 4 000 | 63,25 | 1, 2 | 1, 2 | 0,0993 / 0,199 | 0,140 / 0,281 | 64 (0 bis 63) | 1 |
| 16 000 | 126,49 | 1, 2 | 1, 2 | 0,0497 / 0,0993 | 0,0702 / 0,140 | 24 (0 bis 23) | 2 zu 12 |
| 64 000 | 252,98 | 1, 2, 4 | 2 | 0,0248 / 0,0497 / 0,0993 | 0,0351 / 0,0702 / 0,140 | 12 (0 bis 11) | 3 zu 4 |

- Bei N = 64 000 gibt es Verschiebungen nur bei n = 2 (Rechenzeit; IZ3 braucht nur n = 2).
- **Regelmaessig:** L = 256 mit n = 1, 2, 4 (IZ0, Tor, Vergleichswerte) und L = 64 mit n = 1, 2 (Tor).
- **Fenster [F]:**
  - Die Karte verlangt 2 pi/L << k << 1. Festlegung: n >= 2 (mindestens zwei Wellenlaengen) und abs(k) <= 0,1.
  - Begruendung:
    - c_P hat kein Flaechenglied (Abschnitt 2).
    - Auf dem regelmaessigen Netz aendert sich c_P zwischen n = 1 und n = 8 (L = 1024) nur um 6e-4 relativ
      (INDUZIERT-1 Tabelle 3.1).
    - INDUZIERT-1 nahm n >= 8. Das ist bei N = 64 000 mit abs(k) <= 0,1 nicht moeglich.
  - n = 1 wird beschreibend berichtet.
- **Kleinstes ausgewertetes k im Fenster bei N = 64 000:** n = 2, abs(k) = 0,0497 auf den Achsen (0 und 90 Grad).
  Die Diagonalen haben bei n = 2 abs(k) = 0,0702, ebenfalls im Fenster.
- **Laufzeit (gemessen, Abschnitt 11):** LU 0,97 s bei N = 64 000, 0,14 s bei 16 000, 0,02 s bei 4 000; Netzbau 6,3 s
  bzw. 1,4 s bzw. 0,3 s. Je Saat bei N = 64 000 mit 81 LU also etwa 85 s, ein Block zu 4 Saaten etwa 340 s.

## 5. Vorhersagen der Karte (unveraendert)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| IZ0 | Kontrolle: Das regelmaessige Netz gibt die konforme Steifigkeit aus INDUZIERT-1 Teil A (+0,1249) auf 1e-3 wieder | 85 % |
| IZ1 | [H] Auf den Zufallsnetzen liegt das Saatmittel der konformen Steifigkeit pro Flaeche und k^2 beim kleinsten k und N = 64 000 innerhalb 20 % von Polyakovs -1/(24 pi) | 25 % |
| IZ2 | Isotropie: Die Richtungsstreuung des Saatmittels ist <= 5 % | 70 % |
| IZ3 | [H] Die Knotenverschiebungs-Moden sind weich: Steifigkeit <= 10 % des Betrags der konformen Steifigkeit beim kleinsten k | 30 % |
| IZ4 | Die Streuung ueber Saaten faellt mit N etwa wie N^(-1/2) (Steigung -0,5 +- 0,15) | 60 % |

## 6. Urteilsregeln (mechanisch durch code/zufall_auswertung.py nach lauf-69/auswertung.json)

- **Tor [F].** Alle drei Teile muessen gelten, sonst sind IZ1 bis IZ4 "nicht auswertbar":
  - (a) Alle Zufallsnetze bestehen die Netzpruefungen (Abschnitt 1). Jede LU hat U_ii > 0 und perm_r = perm_c.
  - (b) log det' gegen dichte Rechnung <= 1e-9 relativ: K2 (induziert.torus_gamma) sowie K3 (slogdet(K + 1 1^T/N) und
    Summe log der Eigenwerte ohne Nullmode).
  - (c) Differenzenschema gegen die exakte Blasensumme <= 1e-4 relativ in allen verglichenen Punkten (K4; regelmaessig
    L = 64 und 256; konform und beide Verschiebungen).
- **IZ0 eingetroffen,** wenn abs(c_P/c_ref - 1) <= 1e-3.
  - c_P: regelmaessiges Netz L = 256, 0 Grad, n = 2 (abs(k) = 0,0491), aus diesem Code.
  - c_ref = 0,12492171825863749 aus INDUZIERT-1 lauf-69/teilA.json (gleicher Torus, gleiches k).
  - [F] "auf 1e-3" ist relativ gelesen (strenger). Kartenwortlaut absolut gegen 0,1249 wird mitberichtet.
- **IZ1 eingetroffen,** wenn abs(cbar/(-1/(24 pi)) - 1) <= 0,20.
  - cbar ist das Saatmittel bei N = 64 000, n = 2, abs(k) = 0,0497 (kleinstes k im Fenster).
  - Je Saat wird ueber die zwei Achsenrichtungen gemittelt (0 und 90 Grad); nur sie haben dieses abs(k).
  - Mitberichtet: das Mittel ueber alle vier Richtungen bei n = 2.
- **IZ2:** Gewertet werden die Richtungsmittel cbar_d (Saatmittel je Richtung) bei N = 64 000, n = 2.
  - Streuung = Standardabweichung (ddof = 1) der vier cbar_d, geteilt durch abs(Mittel).
  - Eingetroffen, wenn die Streuung <= 0,05 ist.
  - Nicht auswertbar, wenn schon das Saatrauschen 5 % erreicht: Wurzel aus dem Mittel der quadrierten
    Standardfehler, relativ, > 0,05.
  - Beschreibend: Spanne/abs(Mittel) und chi^2 gegen ein gemeinsames Mittel.
- **IZ3:** bei N = 64 000, n = 2, je Richtung die Saatmittel von kappa_konf, kappa_laengs und kappa_quer.
  - R = max ueber die vier Richtungen und beide Moden von abs(kappa_versch)/abs(kappa_konf).
  - Eingetroffen, wenn R <= 0,10.
  - Kartenwortlaut mit Vorzeichen (max kappa_versch/abs(kappa_konf) <= 0,10) wird mitberichtet.
- **IZ4:** je N die Standardabweichung (ddof = 1) ueber die Saaten.
  - Gemessen wird das Achsenmittel von c_P (0 und 90 Grad) bei festem abs(k) = 2 pi/sqrt(4000) = 0,0993. Das ist
    n = 1, 2, 4 fuer N = 4 000, 16 000, 64 000.
  - Steigung b: kleinste Quadrate von log(Std) gegen log N ueber die drei N.
  - Eingetroffen, wenn abs(b + 0,5) <= 0,15.
  - Beschreibend: Bootstrap-Intervalle (68 % und 95 %), relative Streuung, Streuung bei n = 1 je N.
- **Abbruch und Teilmengen:** Wird ein Block bei N = 64 000 nicht fertig, wird mit den fertigen Saaten geurteilt
  (mindestens 8), offengelegt. Bei weniger als 8 Saaten sind IZ1 bis IZ4 "nicht auswertbar".

## 7. Kontrollen

- **K1:** Kotangens-Formel gegen Gram-Formel (lokal_K_batch aus induziert.py) auf 500 Zufallsdreiecken.
- **K2:** regelmaessig L = 16. Die Matrix wird gegen induziert.torus_K geprueft, log det' gegen induziert.torus_gamma
  (dicht, K + 1/N).
- **K3:** Zufallsnetze N = 400 (2 Saaten) und N = 900. LU gegen dichte slogdet(K + 1 1^T/N) und gegen die Summe log der
  Eigenwerte ohne Nullmode. Dazu Symmetrie und Zeilensummen.
- **K4:** Differenzenschema gegen die exakte Blasensumme (L = 16 und 64; vier Richtungen; n = 1, 2; konform und beide
  Verschiebungen).
- **K5:** Schrittprobe (Abschnitt 3).
- **Laufend:** Netzpruefungen je Netz, LU-Pruefungen je Aufruf. Regelmaessig L = 256: Differenzen gegen die Blasensumme
  in allen Punkten (Tor c).

## 8. Laeufe

- .69, /home/fmh/fmhc-physics-remote/runde38-induziert-zufall/ (code/, rauch/, lauf/), nur ueber kleintest.sh, Spuren
  cpu3 und cpu4, hoechstens zwei zugleich.
- **Haupt:**
  - kontrolle
  - regulaer L = 256 (n = 1, 2, 4) und L = 64 (n = 1, 2)
  - zufall N = 4 000 Saaten 0 bis 63
  - zufall N = 16 000 Saaten 0 bis 11 und 12 bis 23
  - zufall N = 64 000 Saaten 0 bis 3, 4 bis 7 und 8 bis 11
  - danach die Auswertung
- Jeder Lauf schreibt nach jeder Saat einen Zwischenstand. Laeuft ein Block in die 600 s, wird er mit denselben Saaten
  in kleinere Bloecke geteilt.
- Code nach dem Einfrieren nur bei echten Fehlern aendern, offengelegt.

## 9. Agenten-Vorhersagen (nach den Rauchlaeufen, vor den Hauptlaeufen)

Die Rauchlaeufe zeigten schon c_P- und c_D-Werte (Abschnitt 11). A3, A5 und A7 sind deshalb keine echten Vorhersagen
mehr; sie stehen hier zur Vollstaendigkeit.

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Tor besteht (Netze gueltig, log det' <= 1e-12 relativ, Differenzen <= 1e-7) | 95 % |
| A2 | IZ0 eingetroffen, Abweichung <= 1e-6 relativ | 95 % |
| A3 | IZ1 nicht eingetroffen; c_P(Zufall) liegt bei +0,15 bis +0,17, also etwa -12 mal Polyakov (absehbar) | - |
| A4 | IZ2 eingetroffen, Streuung <= 1 % | 85 % |
| A5 | IZ3 nicht eingetroffen; R > 100 bei abs(k) = 0,05, und R waechst wie 1/k^2 (absehbar, siehe [M] unten) | - |
| A6 | IZ4 eingetroffen | 45 % |
| A7 | Auch c_D verfehlt Polyakov um mehr als 20 % (absehbar: c_D ~ +0,05 in der Probe r2) | - |
| A8 | Das Zufallsnetz liegt in c_P ueber dem Richtungsmittel des regelmaessigen Netzes (0,125) | 90 % |

- **[M] zu A5:**
  - Eine Verschiebung mit Dehnung ~ s k kostet am Gitter elastische Energie der Vakuumenergie, je Flaeche ~ (s k)^2.
  - Je Einheit Kantenlaengen-Norm (~ (s k)^2 N) ist das O(1). Die konforme Mode kostet dagegen ~ c k^2 je Einheit
    ihrer Norm (~ s^2 N).
  - Das Verhaeltnis waechst also wie 1/k^2, solange der Schermodul des Netzes nicht null ist.
- **[H] zu A7, Schreibtisch:**
  - Auf einem festen Netz aendert die konforme Mode auch die physikalische Punktdichte: rho = rho_0 e^{-2 sigma}.
  - Lokale, kovariante Glieder in (g, rho) geben deshalb k^2-Steifigkeit, etwa Integral sqrt(g) R log rho und
    Integral sqrt(g) (grad log rho)^2.
  - Das erste waere ueber die lokale Weyl-Anomalie festgelegt, wenn das Netz lokal wie ein kovarianter Regulator mit
    Lambda^2 ~ rho wirkt [H; L Heat-Kernel-Koeffizient a_1 = R/(24 pi)]. Dann gilt
    1/2 log det enthaelt -(1/(24 pi)) Integral sqrt(g) R log Lambda = +(1/(12 pi)) Integral (grad sigma)^2.
  - Zusammen mit Polyakov gaebe das +1/(24 pi) statt -1/(24 pi), dazu einen nicht universellen Rest c3.
  - Selbst ein ideal isotropes Zufallsnetz liesse Polyakov in der konformen Mode also nicht allein stehen.

## 10. Kartenpunkte (vor dem Einfrieren offengelegt)

- **[K] Flaechenglied:**
  - Die Karte verlangt Konventionen "wie INDUZIERT-1 Teil A, also auch dasselbe Flaechenglied bzw. det'(M^-1 K)".
  - In der geurteilten Groesse c_P (1/2 log det' K) gibt es kein Flaechenglied (INDUZIERT-1 K1, exakt).
  - Gewertet wird deshalb c_P wie in INDUZIERT-1; c_D (mit Massenmatrix, ohne Flaechenglied) ist beschreibend.
  - Nach Kartenwortlaut ist das dieselbe Groesse; die Urteile haengen nicht an dieser Lesart.
- **[F] "beim kleinsten k":** Kleinstes abs(k) im Fenster bei N = 64 000, nur die Achsen (Abschnitt 6). Das
  Vier-Richtungen-Mittel wird mitberichtet.
- **[F] "Steifigkeit <= 10 %" (IZ3):** gewertet mit Betrag, weil eine negative Steifigkeit nicht weich, sondern instabil
  ist. Kartenwortlaut mit Vorzeichen wird mitberichtet.
- **[F] IZ4:** Die Karte nennt keine Groesse und kein k. Festgelegt: Achsenmittel von c_P bei festem
  abs(k) = 0,0993.
- **Kein Kartenfehler gefunden,** der ein Urteil aendern wuerde.

## 11. Rauchlaeufe (Protokoll, vor dem Einfrieren; .69-Zeiten in UTC)

- **kontrolle-r1** (04:35:45 bis 04:35:51, cpu3, rc 0):
  - K1: 2,4e-11 relativ (die Gram-Formel verliert bei duennen Zufallsdreiecken Stellen)
  - K2: Matrix 8,9e-16, Gamma 1,4e-13
  - K3: <= 2,8e-13 absolut
  - K4: <= 1,4e-8 (konform) und <= 3,0e-8 (Verschiebung)
  - K5 (Zufall N = 4000, Saat 999, nicht in den Hauptlaeufen), unabhaengig vom Schritt auf 7 bis 8 Stellen:
    - c_P = 0,156270 (0 Grad, n = 1, abs(k) = 0,0993) und 0,158717 (45 Grad)
    - Verschiebung je Amplitude: c_laengs 0,1709 und 0,1762, c_quer 0,1739 und 0,1743
- **zeit-N64000** (04:35:45 bis 04:36:39, cpu4, rc 0; Saat 900, n = 1, nicht in den Hauptlaeufen):
  - 53,7 s; Delaunay verletzt 0, Euler 0
  - c_P = 0,1598 / 0,1597 / 0,1590 / 0,1600 (0 / 45 / 90 / 135 Grad)
- **r2** (Probe der Auswertung, ab 04:38:52; Saaten 900 bis 902, nicht in den Hauptlaeufen):
  - regulaer L = 256, n = 2: c_P = 0,12492172 gleich der Blasensumme auf 8 Stellen. Das Verhaeltnis
    kappa_laengs/kappa_konf ist 1410 (0 Grad), 286 (45 Grad) und 2436 (135 Grad).
  - N = 4 000 (3 Saaten): c_P 0,153 bis 0,162
  - N = 16 000 (2 Saaten): 0,157 bis 0,159
  - N = 64 000 (Saat 901): 0,158 bis 0,159
  - Die Streuung faellt in diesen wenigen Saaten von N = 4 000 nach 16 000 eher schneller als N^(-1/2); bei 2 bis 3
    Saaten sagt das nichts Belastbares.
- **Probe p der Auswertung** (04:43:12 bis 04:43:17, cpu3, rc 0) auf den r2-Daten (3/2/2 Saaten):
  - Tor bestanden: log det' 1,0e-15 relativ, Differenzen 3,0e-8.
  - Probe-Urteile: IZ0 eingetroffen, IZ1 nicht, IZ2 eingetroffen, IZ3 nicht, IZ4 nicht (Steigung -0,03 aus 3/2/2
    Saaten, statistisch ohne Aussage).
  - Im Probebild gesehen: c_D ~ +0,05 auf den Zufallsnetzen.
  - Bilder und Probe liegen in rauch-69/r2/p/.
- **Damit vor dem Einfrieren absehbar:**
  - IZ1 nicht eingetroffen (c_P ~ +0,16, Faktor ~ -12)
  - IZ3 nicht eingetroffen (Verhaeltnis ~ 1e3)
  - IZ2 wahrscheinlich eingetroffen
- **Zeitfolge der Festlegungen:**
  - Die Schwellen sind die der Karte.
  - Die Festlegungen [F] der Urteilsregeln (Abschnitt 6: kleinstes k nur auf den Achsen, Fenster n >= 2, IZ4 bei festem
    abs(k) = 0,0993, Rauschgrenze bei IZ2, Betrag bei IZ3) standen im Auswertungscode, bevor r2 lief (Code auf der .69
    um 04:38:52 UTC). Gesehen hatte ich da schon kontrolle-r1 und zeit-N64000 (c_P ~ 0,16, in einer Saat isotrop).
  - Nach r2 und der Probe wurde an Code und Urteilsregeln nichts geaendert. Ergaenzt wurden nur dieser Abschnitt 11 und
    die Kennzeichnung "absehbar" in Abschnitt 9.
