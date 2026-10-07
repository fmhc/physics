# KAUSAL-4D-KERNMASSE-1: Vorab-Datei (Mittel mit der Masse im Kern, vor jeder Rechnung des Mittels)

- Code-Agent fuer die Leitung (claude-primary), Runde 41. Text ab 2026-10-04 14:47:26 CEST (date vor dem Schreiben).
- Vor diesem Text liefen nur Code- und Formelproben (rauch-69/, PLAN Abschnitt 10): Codeprobe, Repro VJ/V0 und die
  Fourierprobe des Ortsraumkerns bei reellem Z. Keine Pole, keine Erwartung an Punkten, keine VK-Feldwerte.
- Kennzeichen: [S] an der Quelle gelesen (lokale Kopie in quellen/, sha256 in quellen/QUELLEN-SHA256.txt); [M] eigene
  Mathematik; [E] gerechnet (synthetisch); [H] Hypothese; [L?] Gedaechtnis, unsicher.
- Abrufe: **0 von 3**. Alle Quellen sind PDFs frueherer Abrufe dieses Projekts (KAUSAL-WELLE-4D, KAUSAL-4D-STABIL-L),
  nach quellen/ kopiert und mit pdftotext gelesen.

## 1. Was die Literatur sagt [S]

- **BBL 2015** (Belenchia, Benincasa, Liberati, arXiv:1411.6513v2; quellen/bbl-1411.6513v2.txt Z. 332-379, 548-552):
  - Die naive Form (3.1) "(f(-Box) - m^2) phi = 0 ... does not admit plane wave solutions (for finite rho) with
    k^2 = -m^2".
  - Stattdessen (3.2) "f(-Box + m^2) phi(x) = 0. We call this the non-local KG equation"; dann gilt
    "f(k^2 + m^2) = 0 if k^2 = -m^2 for any rho", der Verzweigungspunkt liegt bei k^2 = -m^2, und die komplexen
    Nullstellen werden nur verschoben (Tabelle 2: zeta_4 - m^2).
  - Fussnote 8: "An interesting problem for the causal set community is to determine the inverse Laplace transform of
    this function, which would correspond to the massive version of Equation (2.1) in position space. This would lead to
    a definition of the KG equation on a causal set."
  - Fussnote 10: "It remains an interesting open issue as to how one should include a massive term in the causal set".
- **Johnston 2008** (arXiv:0806.3083v2; quellen/johnston-0806.3083v2.txt Z. 205-217, 470-491): K = I + Phi (I - b Phi)^-1
  (3.5); in 3+1 a = sqrt(rho)/(2 pi sqrt 6), b = -m^2/rho (3.44); der Erwartungswert ist das Kontinuum nur "with the
  infinite density limit being taken in the 3+1 case".
- **Dossier KAUSAL-4D-STABIL-L** (Z. 37-43, 209, 241-258; Arbeitsfeld Z. 253-254): Die Masse sitzt bei Johnston
  ausserhalb des Kerns; "Fuer Johnstons Form waere das k~(Z^2 + m^2) statt k~/(1 + m^2 k~)".

## 2. Bauweise: die Masse im Kern fuer Johnstons Form [M]

**Bezeichnungen** (wie SCHICHT-2): c = pi rho/24, u = c tau^4 = rho V(tau), sigma = tau^2, a wie oben,
eps = sqrt 6/(2 pi sqrt rho), Z^2 = |k|^2 - omega^2 (Re Z > 0), k~(Z) = (4 pi/Z) int tau^2 a e^(-c tau^4) K1(Z tau) dtau
(Johnstons masseloser Linkkern, der Code ist schicht2_kont.kt_gen mit Gewichten (1, 0, 0)).

- **Masse aussen (VJ, Johnston):** E[K]~ = k~/(1 + m^2 k~). Pol bei 1 + m^2 k~ = 0, mit Im omega > 0 (Dossier, SCHICHT-1/-2).
- **Masse im Kern (VK, Ziel):** G_K~(Z) := k~(Z_m), Z_m = sqrt(Z^2 + m^2). Das ist BBL (3.2) fuer den Propagator
  f^-1 = k~: Der masselose nichtlokale Kern wird an der verschobenen Stelle Z^2 + m^2 ausgewertet.

**Ortsraumform (BBL Fussnote 8) [M]:**
- Schwinger-Darstellung: K1(Z tau)/Z = (1/tau) int_0^inf exp(-lambda Z^2 - tau^2/(4 lambda)) dlambda. Damit ist fuer
  jeden retardierten, lorentzinvarianten Kern f(sigma) in 4D
  f~(Z) = 2 pi int_0^inf dlambda e^(-lambda Z^2) F(1/(4 lambda)), F = Laplace-Transformierte von f in sigma.
- Die Verschiebung Z^2 -> Z^2 + m^2 multipliziert mit e^(-lambda m^2) = e^(-m^2/(4 beta)). Rueckwaerts gilt
  L^-1[e^(-m^2/(4 beta))] = delta(sigma) - h_m(sigma), h_m(sigma) = (m/(2 sqrt sigma)) J1(m sqrt sigma).
- **Ergebnis:** g(sigma) = f(sigma) - int_0^sigma f(s) h_m(sigma - s) ds, d. h. eine Volterra-Faltung in der
  Eigenzeit des Paares selbst. Das gilt in jeder Dimension (die sigma-Transformation haengt nicht von d ab).
  - Probe: f = (1/2 pi) delta(sigma) ergibt (1/2 pi) delta(tau^2) - (m/4 pi) J1(m tau)/tau, Johnstons (3.25).
  - In 2D ergibt f = 1/2 den Kern (1/2) J0(m tau).
- **Fuer Johnstons Linkkern:** g_K(sigma) = a e^(-c sigma^2) + T(sigma), mit
  T(sigma) = -a int_0^sigma e^(-c s^2) h_m(sigma - s) ds. T(0) = 0. Fuer kleine sigma gilt T ~ -a m^2 sigma/4.
  Fuer sigma >> c^(-1/2) gilt T ~ -(1/2 pi) h_m(sigma - delta_sigma), mit delta_sigma = 1/sqrt(pi c) (0,780 / 0,551 / 0,390 bei
  rho = 4 / 8 / 16).
- **Schranke:** |h_m| <= m^2/4 und a int_0^inf e^(-c s^2) ds = 1/(2 pi), also |T| <= m^2/(8 pi) = 0,0398 fuer alle sigma.

**Warum keine exakte Schichtform:** Ein Kern, der nur von der Intervallzahl n abhaengt, hat das Mittel
e^(-u) sum_n w_n u^n/n!. Das ist e^(-u) mal eine Potenzreihe in u. g_K enthaelt dagegen ungerade Potenzen von sigma, also
sqrt(u). Darum gibt es keine Gewichtsfolge w_n, auch keine unendliche, deren Mittel g_K exakt ist [M]. Das beantwortet
BBL Fussnote 10 fuer reine Schichtkerne negativ.

**Bauweise auf der Kausalmenge (VK):**
- Ein Schritt, kein Halt (b = 0): phi_K(x) = (1/rho) sum_{y vor x} W(y, x) J(y), W = a [n = 0] + t(n), n = Elemente im
  offenen Intervall.
- t(n) = T(sigma_n) mit sigma_n = sqrt(n/c), also n = rho V als Schaetzer der Eigenzeit. Damit gilt t(0) = 0, und Links
  tragen genau Johnstons masselosen Sprung a.
- **Begruendung:**
  - Johnstons Pfadsumme mit b = 0 ist ein Ein-Schritt-Kern. "Masse im Kern" heisst also: Der masselose Linkkern
    bekommt die Masse durch die Verschiebung im Argument, nicht durch Halt-Amplituden.
  - Die Bauweise erbt die masselose Stabilitaet von Johnstons Kern.
- **Verworfen:**
  - Der BD-Operator mit der Masse im Argument: Seine Green-Funktion 1/B~(Z_m) erbt die komplexen Nullstellen von B~
    (BBL Tabelle 2: zeta_4 - m^2), also das ASS-Anwachsen, schon masselos (Dossier V4).
  - Eigenzeit aus der laengsten Kette: Deren Mittel ist nicht exakt rechenbar.
- **Mittel der Realisierung (Mecke, Poisson) [M]:** g_bar(tau) = a e^(-u) + sum_n t(n) u^n e^(-u)/n!. Das ist exakt
  rechenbar und nicht gleich g_K; die Abweichung heisst "Realisierungsfehler".
- **Rauchprobe der Formel** (rauch-69/kern.json, vor diesem Text): Das Fourier-Bild von g_K bei reellem Z = 0,5 / 1 /
  2 / 4 trifft k~(sqrt(Z^2 + m^2)) auf <= 2e-11 relativ, bei allen drei Dichten. max abs(t(n)) = 0,032 / 0,034 / 0,035
  < 0,0398.

## 3. Erwartetes Mittel (Formel, vorab)

**Ziel G_K~ [M]:**
- k~ ist als Funktion von Z^2 analytisch in C ohne (-inf, 0]. Fuer Im omega > 0 liegt Z_m^2 = k^2 + m^2 - omega^2 in
  C ohne (-inf, k^2 + m^2], also im Analytizitaetsgebiet. **G_K~ hat in Im omega > 0 keine Singularitaet, bei keiner
  Dichte.**
- Die Singularitaet liegt auf der reellen Achse bei omega_0 = sqrt(k^2 + m^2): k = 0 bei 1, k = p bei cosh 0,5 = 1,12763.
  - Dort sitzt ein Pol mit Residuum -1/(2 omega_0), also R = -2 omega_0 i e G_K~(omega_0 + i e) -> 1 fuer e -> 0.
  - Am selben Ort liegt ein log-Verzweigungspunkt (eps ln Z_m^2).
- **Masse genau m**, ohne Verschiebung. Bei V-0 war M^2 = m^2/(1 - eps m^2), bei V-00 m^2/(1 - eps m^2/2).
- **Vorhersage fuer die Zaehlung:** In A, S und S0 gilt N_pol = N_lok - W = 0 bei rho = 4, 8, 16 und k = 0, p.
- **Vergleich der Massenschalen-Pole** (k = 0, rho = 4 / 8 / 16):

  | Variante | Im omega | Quelle |
  |---|---|---|
  | VJ (Masse aussen) | 0,246 / 0,198 / 0,152 | SCHICHT-2 Tab. 3.1 |
  | V-0 | 0,0701 / 0,0322 / 0,0147 | SCHICHT-2 |
  | V-00 | 0,00422 / 0,00132 / 0,000436 | SCHICHT-2 |
  | **VK (Masse im Kern)** | **0 / 0 / 0, exakt, Pol auf der reellen Achse** | [M] |

- **Nullstellen von G_K~ [H, 50 %]:**
  - Falls B~ = Z^4 k~ gilt (Dossier V3) und die ASS-Wurzel Z^2 ~ rho^(1/2) (3,8 - 25,4 i) fuer diesen Kern zutrifft,
    liegen sie bei omega ~ sqrt(k^2 + m^2 - Z^2).
  - k = 0: 4,72 + 5,38 i (abs 7,2), 5,60 + 6,41 i (8,5), 6,65 + 7,64 i (10,1); dazu das Spiegelpaar.
  - Erwartete Windungszahl in A: 2 / 2 / 0.
  - Nullstellen des Propagators erzeugen keine Moden. Fuer die Zaehlung muessen sie lokalisiert werden, sonst ist
    N_lok - W < 0.
- **Realisierung g_bar [M]:**
  - |t(n)| <= m^2/(8 pi), also ist der Kern beschraenkt. Das Fourier-Integral konvergiert fuer Im omega > 0 absolut
    (Kegelvolumen ~ t^4, Daempfung e^(-Im omega t)). Damit hat **g_bar~ in Im omega > 0 keine Singularitaet**,
    unabhaengig von der Wahl der t(n).
  - **Keine Feinabstimmung noetig:** Jede beschraenkte Gewichtsfolge gibt ein stabiles Mittel. Ein Amplitudenfehler
    aendert nur das Residuum, nicht Im omega (Gegensatz zu SCHICHT-1/-2: dort eine exakte Bedingung je Ordnung).
  - Grossskalig gilt g_bar - g_K ~ T m^2/(32 c tau^2): 1,5 % bzw. 0,4 % von T bei tau = 2 (rho = 4 bzw. 16). Die
    Frequenz bleibt genau m, ohne Exponentialfaktor. Damit bleibt die Singularitaet von g_bar~ bei omega_0 auf der
    reellen Achse, mit demselben Residuum.
  - Nahe am Lichtkegel (u ~ 1) ist der Realisierungsfehler groesser; seine Groesse liefert Teil A, ohne Urteilskraft.
- **Ableitbarkeit:** KM1 ist ableitbar. Fuer das Ziel und fuer jede beschraenkte Realisierung gilt "kein Pol mit
  Im omega > 0". Die Rechnung prueft hier nur den Bau. Ein Pol mit Im omega > 0 waere ein Baufehler, kein Befund.
- **Grobe Erwartung im Zeitbereich [H, ohne Urteilskraft]:**
  - Die nichtlokale Korrektur ist bei diesen Dichten nicht klein. Rauchprobe: k~(Z_m)/(1/(Z^2 + m^2)) bei Z = 0,5 ist
    0,65 / 0,71 / 0,76 (rho = 4 / 8 / 16).
  - Ich erwarte abs(E_VK)/abs(K) an den Pruefpunkten zwischen 0,6 und 1,3, und flach in t.
  - Der Zuwachs von t = 2,0 bis 3,2 sollte <= 1,05 sein. Zum Vergleich der Zuwachs der Erwartung bei rho = 16 (SCHICHT-2
    Tab. 3.6): VJ 1,247, V-0 1,064, V-00 1,014.
  - Der Realisierungsfehler an den Pruefpunkten sollte <= 5 % von abs(K) bei rho = 16 sein, <= 10 % bei rho = 4.

## 4. Rauschen (nicht ableitbar, nur grob geschaetzt) [H]

- **Linkanteil:** Var ~ (a^2/rho) (1/4) sqrt(pi/c) Q, Q = int s ds dOmega abs(J)^2 auf dem Vergangenheitskegel des Punktes.
  - Bei (t = 2, Paketmitte, rho = 16): Q ~ 2,1, also sd ~ 0,05, relativ zu abs(K) = 0,37 rund 0,14.
  - Bei t = 3,2 verfehlt der Kegel die Quelle weitgehend: sd ~ 0,014, relativ ~ 0,05.
  - Gang ~ rho^(-1/4).
- **Schweifanteil:** Monte-Carlo-Summe eines glatten Kerns: Var ~ (1/rho) int T^2 abs(J)^2, sd ~ 0,03 bei rho = 16
  (relativ ~ 0,1). Gang ~ rho^(-1/2), dazu Schwankung von n bei festem tau.
- **Schaetzung:** s_VK(16) ~ 0,1 bis 0,2, also unter s_VJ = 0,310. Steigung zwischen -0,25 (Linkanteil) und -0,5
  (Schweifanteil).
- **Risiken:** Korrelationen ueber gemeinsame Intervallelemente; Spruenge von t(n) bei kleinem n nahe am Lichtkegel.
  Beides kann die Steigung abflachen.
- **Meine Wahrscheinlichkeit fuer KM2:** 75 % (Karte 55 %). Fuer KM0: 97 % (Repro im Rauch bitgleich). Fuer KM1: 97 %
  (ableitbar; Rest = Baurisiko der Zaehlung).

## 5. Baufehler gegen Befund (vorab festgelegt)

| Fall | Einordnung | Folge |
|---|---|---|
| Codeprobe (Block gegen dicht, Zuschauer gegen Schleife) > 1e-12 | Bau | kein Hauptlauf |
| KM0 verfehlt (VJ-Pole oder VJ/V0/V00-Felder nicht bitgleich) | Bau (Code oder Umgebung) | KM1, KM2 werden geurteilt, Vermerk "Bau unsicher" |
| Fourierprobe > 1e-6 oder Schranke abs(t) <= m^2/(8 pi) verletzt | Bau (Formel) | KM1 nicht auswertbar |
| Ziel: Zaehlung instabil, Residuumprobe abs(R - 1) > 1e-3 bei e = 1e-5, oder N_pol != 0 | Bau (Numerik; widerspricht 3) | KM1 nicht auswertbar |
| Saatmittel VK trifft das eigene Mittel (g_bar) an < 15 von 18 Pruefpunkten in 3 SE, bei einer Dichte | Bau (Feld oder Mittel) | KM2 nicht auswertbar |
| rho = 1e6-Ziel gegen kc.faltung oder feine gegen grobe Quadratur > 1e-2 | Bau (Quadratur der Erwartung) | Vermerk; Treffer-Bedingung fraglich |
| **Steigung der Streuung > -0,2 bei gueltigem Bau** | **Befund** | K-B traegt massive Materie so nur mit Glaettungsskala |
| s_VK > 1 bei rho = 16 | Befund (beschreibend) | Einzelnetz unbrauchbar |
| abs(E)/abs(K) weit von 1, aber flach | Befund (beschreibend) | fester Abstand bei endlicher Dichte, kein Anwachsen |
| Realisierungsfehler gross (> 10 % von abs(K)) | Befund ueber die Bauweise (beschreibend) | Schaetzer sigma_n verbessern |

- Ein Fehlschlag von KM1 ist nach Abschnitt 3 immer ein Baufehler.
- Ein Fehlschlag von KM2 ist ein Befund ueber diese Bauweise, nicht ueber jede Kausalmengen-Form von f(Box + m^2).
