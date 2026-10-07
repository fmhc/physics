# REGGE-WELLE-1: Plan (Code-Agent, Runde 37)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 04:20:30 CEST (date). Plantext ab 04:43:08 CEST (date),
  vor jeder Rechnung zu dieser Karte.
- Grundlage: KARTE.md. Vorhersagen W0 bis W3 und ihre Schwellen sind unveraendert uebernommen. Was die Karte offen
  laesst, ist mit [F] festgelegt. Zwei Punkte der Karte berichtige ich vor dem Einfrieren (Abschnitt 2, K1 und P1).
- Codebasis: RUNDE-36/regge-4d-1/code/regge4d.py, unveraendert kopiert (sha256 2708f33b...); dazu code/regge_welle.py
  und code/regge_welle_auswertung.py.
- **Kennzeichen:**
  - [S] an der Quelle gelesen; hier kein Quellenabruf
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher
  - [M] eigene Mathematik (Schreibtisch)
  - [F] Festlegung dieses Plans
  - [H] Hypothese

## 1. Fortsetzung [M]

- **Form.** M(k) = A(k)^+ E(k) aus REGGE-4D-1 (Mittelpunktskonvention). Fuer reelles k ist conj(A(k)) = A(-k), weil
  die Flaechenableitungen reell sind. Die analytische Fortsetzung ist daher M(k) = A(-k)^T E(k).
- **Laurent-Form.** Die Dreiecksschwerpunkte heben sich im Produkt heraus. Danach hat jede Phase die Form
  exp(i k.r) mit Zeitanteil r_tau in Z/2. Also gilt
  M(k_tau, k_s) = sum_m C_m(k_s) z^m mit z = exp(i k_tau/2).
  - Bei k_tau = i omega ist z = exp(-omega/2).
  - Die Karte schreibt "Polynom in e^(i k_mu)". Das stimmt bis auf die diagonale Aehnlichkeit
    diag(exp(i k.d/2)) zwischen Mittelpunkts- und Eckenkonvention; Determinante und Nullstellen sind gleich.
- **[F1] Zeitachse = Gitterachse 0** (wie REGGE-ZEIT-1). Wegen der S4-Symmetrie ist jede Achse gleichwertig. Raeumlich
  k_s = (k_1, k_2, k_3) reell, k_tau = i omega mit omega reell (Suche: komplex, Abschnitt 3).
- **Symmetrien** [M]:
  - (a) M(k)* = M(k*), denn M ist bei reellem k reell.
  - (b) M(-k) = M(k) (Inversion).
  - Daraus folgt fuer reelles omega: M(-i omega, k_s) = conj M(i omega, k_s) = M(i omega, -k_s).
  - **Zeitumkehr-Pruefung:** F(-omega) = conj F(omega) bei reellem Komplement. Die Nullstellenmenge ist also
    symmetrisch unter omega -> -conj(omega) (Spiegelung an der imaginaeren Achse). Betrag von det und Singulaerwerte
    sind unter omega -> -omega symmetrisch.
  - Die vorwaerts laufenden Nullstellen bei -n sind die konjugierten derer bei n.
  - Eine reine Zeitspiegelung (tau -> -tau bei festem x) ist **keine** Symmetrie des Kuhn-Gitters. Sie bildet
    (1,1,1,1) auf (-1,1,1,1) ab, und das ist keine Gitterkante. Ebenso wenig ist es die raeumliche Paritaet allein.
    Die Folgen stehen unter P1.
- **Nullvektoren:**
  - Die Gitter-Eichmoden u_d = sin(k.d/2) d_mu (4) und e_top (Hyperdiagonale) sind Polynome in denselben Exponentialen.
  - M(k) N(k) ist analytisch und verschwindet fuer alle reellen k, also fuer alle komplexen k [M]. Geprueft wird das
    in W0.
  - e_top: Zeile und Spalte von M verschwinden identisch (Thales, REGGE-4D-1).

## 2. Schreibtisch zur Zaehlung; Kartenberichtigungen

- **Kontinuum auf einem regulaeren Komplement [M].** Rechnung mit der linearisierten EH-Form
  4K = k^2 h.h - 2 (k.h)^2 + 2 (k k h) tr h - k^2 (tr h)^2. Geprueft: Sie ergibt 1/4 k^2 auf TT, -1/2 k^2 auf dem
  konformen Modus und 0 auf den Eichmoden.
  - k = (i omega, 0, 0, kappa). Komplement Q0 = Orthogonalkomplement der Eichmoden bei omega = 0, das sind die sechs
    Komponenten ohne Index 3: h_00, h_01, h_02, h_11, h_12, h_22.
  - Ergebnis:
    - h_01 und h_02: Koeffizient 2 kappa^2, kein omega. Das sind Zwangsbedingungen (Shift).
    - h_12: 2 (kappa^2 - omega^2).
    - Block (h_00, h_11, h_22): Determinante -2 kappa^4 (kappa^2 - omega^2).
  - Also det = const * kappa^8 (kappa^2 - omega^2)^2: eine **doppelte** Nullstelle bei omega = kappa.
  - Der Kern bei omega = kappa ist {h_12, h_11 - h_22}, also die zwei raeumlichen TT-Polarisationen.
  - Q0 bleibt fuer alle omega ein Komplement, denn N(omega) ∩ Q0 = 0 fuer kappa != 0.
  - Allgemein gilt: Bei einem analytischen, regulaeren Komplement aendert ein Wechsel det nur um det(A)^2 != 0. Die
    Nullstellenordnung 2 ist also invariant.
- **K1 (Kartenfehler, Schreibtisch der Karte):** "Im Kontinuum fallen dort alle sechs Nicht-Eich-Werte zugleich auf
  null" gilt nur in der Projektorzerlegung c k^2 (P2 - 2 P0s).
  - Diese Projektoren enthalten 1/k^2 und sind am Lichtkegel singulaer.
  - Dort hat die Form Rang 4. Ihr Kern ist der de-Donder-Raum (6-dim.) = 4 Eichmoden + 2 Polarisationen. Die sechs
    Eigenwerte gehen nur deshalb gemeinsam gegen null, weil die Matrix dort nicht diagonalisierbar ist
    (Jordanbloecke mit den Eichmoden).
  - Auf jedem regulaeren Komplement, wie es die Karte verlangt, gibt es am Lichtkegel **genau zwei** Nullstellen. Die
    anderen vier Richtungen sind Zwangsbedingungen ohne Nullstelle.
  - Erwartung fuers Gitter: Je Richtung zwei Nullstellen nahe omega = abs(k) (vorwaerts) und dazu die vier Gittermoden
    O(1), die fuer kleines k keine Nullstelle haben.
  - **Folge fuer W3:** Die "Gruppen" der Karte reduzieren sich auf ein Paar. W3 prueft dann, ob dieses Paar auf 1e-3
    entartet bleibt. Das Urteil nach Kartenwortlaut (mindestens zwei Gruppen und eine Zweiergruppe) wird zusaetzlich
    genannt (Abschnitt 6).
  - Die Eigenwerte der unreduzierten 15 x 15-Form M haengen von der Metrik der Variablen ab (s = l^2). Ob dort sechs
    gegen null gehen, wird nur beschreibend gezeigt (bild-achse.png).
- **P1 (Praezisierung, "reelle omega"):** Das Kuhn-Gitter hat keine Zeitspiegelung, und die euklidische Form hat Terme
  ungerade in k_tau bei festem k_s.
  - REGGE-4D-1 belegt das: Die Spin-2-Werte unterscheiden sich in den Richtungen (1,1,0,0) und (1,-1,0,0) um 0,1 bis
    0,4 % bei abs(k) = 0,2.
  - Mit k_tau = i omega werden diese Terme imaginaer. det F ist dann auf der reellen Achse komplex, und die Nullstellen
    liegen allgemein **neben** der reellen Achse [M, H]. Grob gilt Im omega/abs(k) ~ O(abs(k)^2).
  - Reelle Nullstellen oder konjugierte Paare sind nur fuer Richtungen erzwungen, bei denen -n eine Permutation von n
    ist, also (1,-1,0) [M].
  - **Festlegung:** "Nullstelle" heisst Nullstelle der analytischen Funktion d(omega) = det F(omega) in der komplexen
    Ebene nahe der reellen Achse. Re omega ist die Frequenz, Im omega das Anwachsen bzw. die Daempfung.
  - Die Toleranzen der Karte gelten fuer den komplexen Abstand abs(omega/abs(k) - 1).
  - Die Kartenwortlaut-Lesart (nur Re omega) wird zusaetzlich genannt.
- **Zwangsbedingungen auf dem Gitter (Auftrag):**
  - Die regulaere Reduktion eliminiert sie selbst: Die Nullstellenordnung am Lichtkegel ist die Zahl laufender Moden.
  - Zusaetzlich identifiziere ich sie explizit (Tor fuer W3, [F9]):
    - (a) Kinetik-Matrix: der omega^2-Koeffizient K2 der direkten h-Form B0^T M B0, auf dem 6-dim. Raum V0 ohne
      Komponenten laengs n. Kontinuum: Rang 3 (h_ab transversal). Die 3 Richtungen ohne zweite Zeitableitung sind
      h_00, h_0a und h_0b (Lapse und Shift).
    - (b) Die Kernvektoren an den Lichtkegel-Nullstellen sind raeumliche TT-Tensoren.

## 3. Verfahren (code/regge_welle.py) [F]

- **[F2] Ableitungen:** Weg T aus REGGE-4D-1 (Torus L = 4, Richardson), damit "M(k) aus REGGE-4D-1" exakt dieselbe
  Form ist. Gegenprobe (beschreibend): Weg K (komplexer Schritt, aus REGGE-ZEIT-1) fuer 4 Richtungen bei abs(k) = 0,05
  und 0,8.
- **Komplement:**
  - Q0(k_s) ist die reelle Orthonormalbasis des Orthogonalkomplements von N(0, k_s) = span(4 Eichmoden bei k_tau = 0,
    e_top), 15 x 10.
  - F(omega) = Q0^T M(i omega, k_s) Q0 ist analytisch (Laurent in z).
  - Keine biorthogonale Basis (N^T v = 0): Ihre Gram-Matrix N^T N wird am Lichtkegel singulaer [M, Kontinuum
    k xi + xi k: Gram ~ k^2 delta + k k].
- **Nullstellen:**
  - Alle Nullstellen von det F als Eigenwerte des Polynom-Eigenwertproblems in z (Begleitmatrix 10 D x 10 D).
    Laurent-Koeffizienten unter 1e-10 relativ werden dort weggelassen und berichtet.
  - omega = -2 log z (Hauptzweig).
  - Verfeinerung aller Kandidaten in R' (R um 20 % vergroessert) mit Aberth-Iteration auf det F (analytische
    Ableitung).
- **[F4] Bereich R** = {0 <= Re omega <= 3 abs(k), abs(Im omega) <= 0,5 abs(k)}; die vorwaerts laufenden Moden bis zur
  dreifachen Lichtgeschwindigkeit.
  - Zaehlung unabhaengig davon per Windungszahl von det F laengs des Randes von R: 2 x 2000 + 2 x 400 Punkte, bei
    Phasenspruengen >= 0,5 rad Verdopplung (bis x4).
- **Beschreibend:**
  - Reelle Achse: s(omega) = sigma_min/sigma_max von F auf 1500 Punkten in (0, 3 abs(k)], lokale Minima per Brent
    verfeinert (Kenngroesse der Karte, Vergleich mit Re omega).
  - Geister: alle Nullstellen mit 3 abs(k) < Re omega <= 2,4 und abs(Im) <= 0,5 abs(k).
- **Je Nullstelle:**
  - Pruefwert s(omega_j); rho(omega_j) = sigma_min(Qn0^T Qn(omega_j)) (Regularitaet des Komplements).
  - Physikalitaet: Abstand des Kernvektors Q0 v von range N(omega_j).
  - h-Struktur, eichinvariant (Fassung nach Rauchlauf 1, Abschnitt 9):
    - Die Klasse u + range N(omega_j) wird mit dem Kantenbild T = B0 {h_+, h_x} der Kontinuums-TT-Moden verglichen.
      h_+ und h_x sind raeumlich, transversal zu n und spurfrei.
    - Vertreter w = u + N c mit c = argmin abs((I - P_T) w). TT-Anteil = abs(P_T w)/abs(w).
    - Dazu Zeitanteil (h_0mu) und Gitterrest abs(w - B0 h)/abs(w) der Anpassung w = B0 h.
- **[F5] Lichtkegel-Fenster:** 0,5 <= Re omega/abs(k) <= 1,5. Lichtkegel-Nullstellen (LK) sind die Nullstellen in R
  in diesem Fenster.
- **[F6] Aufspaltung und Gruppen:** Single-Linkage der LK-Nullstellen mit komplexem Abstand <= 1e-3 abs(k) (Karte W3).
  "Exakt entartet": Abstand <= 1e-6 abs(k) (beschreibend).

## 4. Richtungen und Betraege [F3]

- abs(k) = 0,05; 0,1; 0,2; 0,4; 0,8 (Karte).
- 24 raeumliche Richtungen (normiert):
  - (1,0,0), (-1,0,0), (1,1,0), (-1,-1,0), (1,-1,0), (1,1,1), (-1,-1,-1), (1,1,-1), (-1,-1,1), (1,2,3), (3,1,2),
    (-1,-2,-3).
  - Dazu 12 Fibonacci-Punkte: z_i = 1 - (2i+1)/12, Winkel i * pi (3 - sqrt 5), i = 0..11.
- Wegen der S3-Symmetrie (Permutation der Raumachsen) sind n und sigma(n) gleichwertig. (3,1,2) ist eine
  absichtliche S3-Kopie von (1,2,3) als Kontrolle.
- n und -n sind **nicht** gleichwertig (P1). Die Paare (n, -n) pruefen die Symmetrie aus Abschnitt 1.

## 5. Sperren (schlecht konditioniert -> "nicht auswertbar") [F7]

Ein Punkt (Richtung, Betrag) ist gesperrt, wenn eine dieser Bedingungen gilt:

1. Windungszahl mehr als 0,05 von einer ganzen Zahl entfernt, oder Phasensprung >= 0,5 rad auch bei vierfacher Dichte.
2. Windungszahl != Zahl der verfeinerten Nullstellen in R.
3. Eine Nullstelle in R mit s(omega_j) > 1e-9 (nicht verifiziert).
4. Eine Nullstelle in R mit rho < 0,05 (Komplement fast entartet) oder Physikalitaet < 0,1 (Scheinnullstelle aus dem
   Nullraum).
5. min rho auf dem Rand von R < 0,05.
6. Nullvektor-Residuum auf der reellen Achse > 1e-8.

Urteile sind dreiwertig. Ein Verstoss an einem ungesperrten Punkt ergibt "nicht eingetroffen". Sonst ergibt ein
gesperrter Punkt im Urteilsbereich "nicht auswertbar". Sonst "eingetroffen".

## 6. Urteilsregeln (vor jeder Rechnung)

- **W0 eingetroffen**, wenn (a) und (b) gelten:
  - (a) Laurent-Form bei reellem k gegen git.matrizen aus REGGE-4D-1: je Punkt max abs(dM)/max abs(M) <= 1e-12. Punkte:
    32 Leiterpunkte aus REGGE-4D-1 (8 4D-Richtungen x 0,05 bis 0,4) und 64 zufaellige reelle k.
  - (b) Nullvektoren bei komplexem k_tau: max_j abs(M n_j)/(abs(M)_2 abs(n_j)) <= 1e-10. Punkte: alle Punkte der
    reellen Achse aller 120 (Richtung, Betrag)-Paare (k_tau = i omega) und 64 zufaellige k mit
    k_tau = a + i b, a in [-pi, pi], b in [-2,4; 2,4], k_s in [-pi, pi]^3.
- **W1 eingetroffen**, wenn fuer abs(k) in {0,05; 0,1} in allen 24 Richtungen gilt:
  - Mindestens eine Nullstelle liegt in R.
  - Alle Nullstellen in R erfuellen abs(omega/abs(k) - 1) <= 0,005 (komplex, P1).
  - Kartenwortlaut-Lesart: dasselbe mit abs(Re omega/abs(k) - 1).
- **W2 eingetroffen**, wenn bei abs(k) = 0,8 gilt:
  - (a) Jede Richtung hat mindestens eine LK-Nullstelle, und alle LK-Nullstellen haben abs(omega/abs(k) - 1) >= 0,01
    (komplex).
  - (b) Die Streuung der Richtungsmittel v(n) = Mittel von Re omega/abs(k) ueber die LK-Nullstellen einer Richtung
    erfuellt (max - min)/Mittel >= 0,001.
  - [F8] "weicht ab" gilt fuer jede LK-Nullstelle in jeder Richtung, also die strenge Lesart.
  - Kartenwortlaut-Lesart: (a) mit abs(Re omega/abs(k) - 1).
- **W3:**
  - **[F9] Tor** "Polarisationen und Zwangsbedingungen identifiziert". Alle Bedingungen muessen gelten, sonst
    **"nicht auswertbar"**:
    - (i) Bei abs(k) = 0,05 und 0,1 hat jede Richtung genau 2 LK-Nullstellen (mit Vielfachheit).
    - (ii) Deren Kernvektoren haben einen TT-Anteil >= 0,95. Bei einem exakt entarteten Paar gilt das auch fuer den
      zweiten Kernvektor.
    - (iii) Bei abs(k) = 0,4 hat jede Richtung genau 2 LK-Nullstellen.
    - (iv) Bei 0,05 und 0,1 zeigt die Kinetik-Matrix in jeder Richtung 3 kleine Singulaerwerte (s4/s3 <= 0,1). Deren
      Vektoren haben einen Lapse/Shift-Anteil >= 0,9.
    - Kein Torpunkt ist gesperrt.
  - **[F10] Regel (bei offenem Tor):** W3 eingetroffen, wenn bei abs(k) = 0,4 in **jeder** Richtung unter den
    LK-Nullstellen eine Gruppe [F6] von genau zwei liegt.
    - Die Karte nennt keinen Quantor. "Kandidat fuer die zwei Polarisationen" verlangt die Paarung in jeder Richtung.
  - **Kartenwortlaut-Lesart:** Alle Nullstellen in R bilden mindestens zwei Gruppen, und eine davon hat genau zwei
    Elemente. Nach K1 erwarte ich hier "nicht eingetroffen", gleich wie die Physik ausgeht.
- Urteile mechanisch durch code/regge_welle_auswertung.py nach lauf-69/auswertung.json.

## 7. Agenten-Vorhersagen (Schreibtisch, vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | W0 eingetroffen: (a) <= 1e-15 (gleicher Stencil, andere Summierung), (b) <= 1e-11 | 85 % |
| A2 | Zeitumkehr: abs(F(-omega) - conj F(omega))/abs(F) <= 1e-12; Nullstellen bei -n = konjugierte bei n auf <= 1e-9 abs(k); S3-Kopie (3,1,2) gleich (1,2,3) auf <= 1e-9 abs(k) | 85 % |
| A3 | K1: Bei abs(k) <= 0,2 hat jede Richtung genau 2 Nullstellen in R, beide im LK-Fenster | 80 % |
| A4 | P1: Die Nullstellen sind nicht reell. Bei 0,8 ist max abs(Im omega)/abs(k) >= 1e-3. Entlang (1,-1,0) reell (abs(Im) <= 1e-9 abs(k)) oder ein konjugiertes Paar. Im omega/abs(k) waechst etwa wie abs(k)^2 | 60 % |
| A5 | W1 eingetroffen | 75 % |
| A6 | W2 eingetroffen, Re omega/abs(k) < 1 in allen Richtungen bei 0,8 (Gitter bremst) | 60 % |
| A7 | W3 auswertbar und nicht eingetroffen: Das Paar spaltet bei 0,4 um mehr als 1e-3 abs(k) (Doppelbrechung). Exakt entartet (<= 1e-6) nur entlang (1,1,1) und (-1,-1,-1), wo die S3-Untergruppe eine 2-dim. Darstellung hat | 65 % |
| A8 | Tor (ii) und (iv) halten: TT-Anteil >= 0,95 und 3 Zwangsrichtungen mit Lapse/Shift-Anteil >= 0,9 bei abs(k) <= 0,1 | 65 % |
| A9 | Beschreibend: Von den 10 nicht trivialen Eigenwerten der unreduzierten M (s = l^2) gehen am Lichtkegel nur etwa 2 gegen null, nicht 6 | 55 % |

## 8. Laeufe

- **Ort:** .69, /home/fmh/fmhc-physics-remote/runde37-welle/ (code/, rauch/, lauf/). Start nur ueber kleintest.sh, Spuren
  p4000b und cpu5 (nur CPU-Rechnung), hoechstens zwei zugleich.
- **Rauchlauf** (vor dem Einfrieren): `regge_welle.py rauch`.
  - Nur abs(k) = 0,3 und 0,6, beide nicht im Urteilsbereich, Richtungen (1,0,0), (1,1,1), fib05.
  - W0-Stichproben und Gegenprobe Weg K bei 0,3.
  - Dazu die Probe des Auswertungscodes auf diesen Daten (Modus probe).
- **Hauptlauf** `regge_welle.py haupt`, dann `regge_welle_auswertung.py`. Je Lauf deutlich unter 10 min erwartet.
- Code-Aenderungen nach dem Einfrieren nur bei echten Fehlern, offengelegt.

## 9. Rauchlaeufe (Protokoll, vor dem Einfrieren)

- Abschnitte 1 bis 8 sind nach den Rauchlaeufen unveraendert. Einzige Ausnahme ist die Messgroesse "TT-Anteil"
  (Abschnitt 3, Fehler unten). Alle Schwellen sind unveraendert, auch TT >= 0,95.
- **rauch1** (.69 02:44:39 bis 02:44:57 UTC, cpu5, rc = 0; Code-sha256 4fda6f4d...) und Probe der Auswertung (02:45:02
  bis 02:45:06 UTC, rc = 0). Nur abs(k) = 0,3 und 0,6, Richtungen (1,0,0), (1,1,1), fib05. Gesehen:
  - Geometrie: flach 1,8e-15, Weg T 7,5e-12.
  - W0-Stichproben: (a) 6,2e-16, (b) 1,2e-12. Achsenresiduen 7,9e-13 bis 8,3e-13. Zeitumkehr 7e-13 bis 2,2e-12.
  - **Je Punkt Windungszahl 2,000 und genau 2 Nullstellen in R, keine Geister.** Das bestaetigt K1 bei 0,3 und 0,6.
  - **Die beiden Nullstellen sind entartet** (Abstand <= 3e-10 abs(k)) und **reell** (abs(Im omega)/abs(k)
    <= 1,5e-10). Damit widerspricht der Rauchlauf meinen Vorhersagen A4 und A7 (beide vor dem Rauchlauf festgelegt
    und unveraendert).
  - Re omega/abs(k): (1,0,0) 0,99258 / 0,97127, (1,1,1) 0,99505 / 0,98079, fib05 0,99413 / 0,97724 (0,3 / 0,6).
  - Reelle Achse: s(omega) hat je ein Minimum bei Re omega mit s <= 8,4e-11.
  - Kinetik: drei Singulaerwerte um 0,25, drei unter 1,3e-3. Lapse/Shift-Anteil der kleinen drei >= 0,998.
  - Gegenprobe Weg K bei 0,3: <= 1,7e-10 abs(k).
- **Fehler gefunden (Messgroesse, nicht Schwelle):** Der TT-Anteil war auf dem Vertreter u = Q0 v gemessen. Das ist
  nicht eichinvariant: u enthaelt je nach Komplement einen Eichanteil N(omega) c.
  - Ergebnis im Rauchlauf: TT 0,58 bis 0,74, Zeitanteil 0,39 bis 0,66, Gitterrest 0,15 bis 0,30 in (1,0,0) und
    fib05; dagegen 0,985 in (1,1,1).
  - Der Kern ist nur modulo N bestimmt (Abschnitt 2), die Groesse muss also auf der Klasse u + range N gemessen
    werden. Ersetzt durch den eichinvarianten Vertreter (Abschnitt 3).
  - Die Schwelle 0,95 und das Tor [F9] sind unveraendert.
- **rauch2** (02:48:20 bis 02:48:38 UTC, cpu5, rc = 0; Code-sha256 3f5fe0f5...) und Probe (02:48:38 bis 02:48:42 UTC,
  rc = 0):
  - TT-Anteil (neu) 0,99998 (0,3) bzw. 0,9997 (0,6) in allen drei Richtungen; Zeitanteil <= 0,028; Gitterrest
    <= 0,025.
  - F ist auf der reellen Achse wirklich komplex: max abs(Im F)/max abs(F) = 0,009 bis 0,16. Die Phase von det F
    laeuft laengs der Achse um mehrere rad.
  - Die reellen, entarteten Nullstellen sind also keine Folge einer reellen Form [H, ungeklaert].
  - Die Probe der Auswertung (Betraege 0,3/0,6 statt der Karte) ergab: W0 und W2 eingetroffen, W3 eingetroffen
    (Kartenwortlaut: nicht eingetroffen). W1 "nicht eingetroffen", weil bei 0,3 die Toleranz 0,005 verfehlt wird
    (0,5 bis 0,75 %); bei 0,3 ist das keine Kartenaussage.
- **Selbstanzeige zum Vorwissen:** Die Rauchlaeufe bei 0,3 und 0,6 machen die Kartenurteile weitgehend vorhersehbar:
  - W1 ueber v - 1 ~ k^2;
  - W2 ueber 2 bis 3 % bei 0,6;
  - W3 ueber das entartete Paar.
  - Gerechnet ist bei 0,05 bis 0,8 noch nichts.
