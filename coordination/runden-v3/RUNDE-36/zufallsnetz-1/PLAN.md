# ZUFALLSNETZ-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 36, explorativ)

- Start des Code-Agenten 22:52:03 CEST (date). Plan geschrieben ab 23:12:49 CEST (date), vor jeder Hauptrechnung.
- Grundlage: KARTE.md (Vorhersagen Z0 bis Z4, Schwellen und Wahrscheinlichkeiten unveraendert uebernommen).
- Code: code/zufallsnetz.py (Netz, Elastizitaet, Christoffel, Kontrollen), code/auswertung.py (Urteile, Bilder),
  code/laeufe.sh (Hauptlaeufe), code/rauch.sh (Rauch).
- Kennzeichen: [M] vorab ableitbar, [L] Literatur aus dem Gedaechtnis, [L?] unsicher erinnert, [H] Hypothese,
  [F] von mir vor dem Einfrieren festgelegt, wo die Karte offen ist.

## 1. Messvorschriften

### 1.1 Netz

- **Punkte:** N unabhaengig gleichverteilte Punkte im periodischen Wuerfel [0, L)^3, L = N^(1/3) (Dichte 1).
  - Das ist der Poisson-Prozess bei fester Punktzahl (Binomialprozess) [F].
  - Saat: numpy default_rng(SeedSequence([20261003, 36, N, saat])), saat = 1 und 2.
- **Periodisches Delaunay:**
  - Bildpunkte x_i + L s mit s in {-1, 0, 1}^3, behalten, wenn sie in [-m, L + m)^3 liegen; Rand m = 5.
  - Triangulierung mit scipy.spatial.Delaunay (Qhull, Standardoptionen).
  - Behalten werden alle Tetraeder mit mindestens einer Ecke im Grundwuerfel (s = 0).
- **Kantenzuordnung:**
  - Je behaltenem Tetraeder sechs Kanten. Bildkanten ohne Ende im Grundwuerfel fallen weg.
  - Periodische Kante (i, j, s) mit Vektor d = x_j + L s - x_i, kanonisch i < j (bei i = j: s lexikographisch
    positiv). Duplikate entfernt (eine Kante ueber den Rand wird von beiden Enden gefunden).
- **Pruefungen je Netz (berichtet; bei Verletzung ist das Netz fehlerhaft und wird nicht geurteilt):**
  - (a) Die Umkugel jedes behaltenen Tetraeders liegt ganz in [-m, L + m]^3. Dann sind diese Tetraeder genau die
    periodischen Delaunay-Tetraeder (leere Kugel, vollstaendiger Stern um jede Ecke) [M].
  - (b) Jede Kante ueber den Rand wurde von beiden Enden gefunden, jede innere genau einmal.
  - (c) Tetraeder je Punkt = (Summe der Ecken im Grundwuerfel)/4/N; Literaturwert 24 pi^2/35 = 6,768 [L].
  - (d) Euler fuer den 3-Torus: E = N + T [M].
  - (e) Kein Originalpunkt von Qhull ausgelassen (coplanar), keine Selbstkante.
  - (f) Mittlerer Grad 2E/N; Literaturwert 2 + 48 pi^2/35 = 15,535 [L].
- **Federn:** Ruhelaenge = Kantenlaenge (spannungsfrei). k_e = 1 (Hauptfall "k1") oder k_e = 1/l_e (Variante
  "kl"). Masse 1 je Knoten, rho = N/V = 1.

### 1.2 Elastizitaetstensor mit nichtaffiner Relaxation

- **Sechs Verzerrungen:** Einheitsverzerrungen in Voigt-Form mit Ingenieur-Scherung, b = 1 bis 6 fuer 11, 22, 33,
  23, 13, 12 (bei b = 4 bis 6 ist gamma = 2 eps = 1).
  - Affin: jeder Kantenvektor d -> (1 + eps) d, auch ueber den Rand (der periodische Rahmen L s wird mitverzerrt).
  - Affine Laengenaenderung a_e = l_e n_e . eps n_e = l_e v_b(n_e), v = (n1^2, n2^2, n3^2, n2 n3, n1 n3, n1 n2).
- **Energie** (lineare Ordnung, spannungsfreie Federn): E(eps, u) = 1/2 Sum_e k_e (a_e + n_e . (u_j - u_i))^2.
- **Relaxation:** H u = -f mit H = M^T K M (3N x 3N, duenn), f = M^T K a. M = Kompatibilitaetsmatrix.
  - Loeser: konjugierte Gradienten (scipy.sparse.linalg.cg), Vorkonditionierer Block-Jacobi (invertierte
    3x3-Diagonalbloecke von H), Start 0.
  - Toleranz: ||H u + f|| <= 1e-10 ||f||, hoechstens 50000 Iterationen. Danach Translation (Mittelwert von u)
    entfernt. f summiert sich zu null, das System ist also loesbar.
- **Tensor:** C_V[b, c] = (1/V) (a^b + M u^b)^T K (a^c + M u^c) (Energieform; ihr Fehler ist quadratisch im
  Loeserfehler). Affin: C_V,aff = (1/V) Sum k l^2 v v^T.
- **Konvergenz je Lauf (offengelegt):** Iterationen, End-Residuen, Abstand zur Kurzform (1/V)(a^T K a + f^T u)
  (Fehler linear), Symmetrie der Kurzform, Eigenwerte von C_V (Stabilitaet: alle > 0).
- **Kontrolllauf N = 4000, Saat 1, k1:**
  - Direktloeser (splu, Knoten 0 festgehalten) gegen CG.
  - CG mit rtol 1e-6, 1e-8, 1e-12 gegen den Direktloeser.
  - Born-Probe langer Wellen: dynamische Matrix D(k) = M(k)^H K M(k) mit Bloch-Phase exp(i k . d_e),
    |k| = 1e-3 x 2 pi/L in [100], [110], [111] und Index 203 von R403 (0-basiert, Fibonacci-Index 200), dazu
    |k| = 2e-3 x 2 pi/L in [100].
    Drei kleinste Eigenwerte (eigsh, shift-invert um 0), c = omega/|k|, verglichen mit Christoffel aus dem relaxierten
    C. Nach dem Born-Huang-Satz muessen beide gleich sein [L], bis auf O(k^2).

### 1.3 Christoffel-Gleichung

- C_ijkl aus C_V (Voigt-Abbildung, symmetrisiert). Gamma_ik(n) = C_ijkl n_j n_l / rho mit rho = N/V.
- Eigenwerte aufsteigend = c1^2, c2^2, c3^2. Ast 1 = langsame Querwelle, Ast 2 = schnelle Querwelle,
  Ast 3 = Laengswelle; je Richtung nach Groesse sortiert wie in NETZ-C-1.
- **Richtungsmenge R403:** [100], [110], [111] und 400 Fibonacci-Richtungen, identisch mit NETZ-C-1
  (netz_a.py, richtungen(400)). Fib400 = nur die 400 Fibonacci-Richtungen (fast gleichmaessig auf der Kugel).

### 1.4 Messgroessen

- **Richtungsschwankung je Ast:** S_b = max_R403 c_b / min_R403 c_b - 1 (wie NETZ-C-1).
- **Richtungsschwankung der Querwelle:** S_T = max(S_1, S_2) [F].
- **Doppelbrechung:** D = max_R403 (c_2/c_1 - 1) [F].
- **c_l/c_q:** Mittel_Fib400 c_3 / Mittel_Fib400 (c_1 + c_2)/2 [F]. Als Information auch aus der isotropen
  Projektion: sqrt((lambda + 2 mu)/mu).
- **Isotrope Projektion** (Voigt-Mittel = naechster isotroper Tensor in der Frobenius-Norm): a = C_iijj,
  b = C_ijij; mu = (3b - a)/30 = G_V; lambda = (2a - b)/15; K_V = a/9.
- **G/G_affin** = mu(C)/mu(C_aff) [F]. K/K_affin nur als Information.
- **Nur Information (keine Urteile):**
  - RMS-Anisotropie je Ast (Std/Mittel ueber Fib400)
  - dichte Richtungsprobe mit 20000 Fibonacci-Richtungen und Nelder-Mead-Verfeinerung der Extremwerte
  - alle Groessen fuer die Variante kl und fuer den affinen Tensor
  - Exponentenfits je Saat, je Ast und fuer D

## 2. Groessen, Saaten, Laeufe

- N = 4000, 16000, 64000; Saaten 1 und 2; Federn k1 und kl: zwoelf Netzlaeufe.
  - k1 und kl laufen je Netz getrennt. Das Netz ist dasselbe; geprueft ueber die sha256 der Kantenliste.
- **fcc-Gegenprobe:** fcc mit Kante 1 (a = sqrt 2), 4 x 4 x 4 kubische Zellen = 256 Knoten, Kanten = naechste
  Nachbarn (1536), k = 1, Masse 1. Gleicher Code (elastizitaet, christoffel) wie fuer die Zufallsnetze.
- **Kontrolllauf** N = 4000, Saat 1, k1 (Abschnitt 1.2).
- Alle Laeufe auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4, je Spur nacheinander, hoechstens zwei zugleich.
  - Rauchzeiten: N = 64000 38 s (542 MB), N = 4000 2 s.
- Danach code/auswertung.py ueber kleintest.sh (cpu3). Ergebnisse nach lauf-69/ kopieren.

## 3. Urteilsregeln (mechanisch in code/auswertung.py)

- Grenzen einschliesslich ("zwischen a und b" = [a, b]); "< 3 %" streng.
- **Z0 (85 %)** eingetroffen, wenn (a), (b) und (c) gelten:
  - (a) fcc-Gegenprobe: max ueber R403 und drei Aeste |c_hier/c_NETZ-C-1 - 1| <= 1e-6.
    - Bezug: NETZ-C-1 lauf-69/netz_a.npz (sha256 1605fa21...), Schluessel fcc_Z_c_nf400_k0.001.
    - [F] Verglichen werden alle 403 Richtungen, nicht die gerundete Tabelle A1. Die Abweichung von den
      geschlossenen Formen wird als Information berichtet.
  - (b) Mittlerer Grad 2E/N jedes der sechs Netze in [15,4; 15,6].
  - (c) Affiner Tensor: |lambda_aff/mu_aff - 1| <= 0,01 fuer alle zwoelf affinen Tensoren (sechs Netze, k1 und kl).
    - [F] "C12 = C44" lese ich als Cauchy-Beziehung lambda = mu der isotropen Projektion, wie im Schreibtisch der
      Karte. Fuer Zentralfedern gilt sie identisch [M]: Der affine Tensor ist in allen vier Indizes symmetrisch.
      (c) prueft damit nur den Code (etwa Voigt-Faktoren).
    - Die woertliche Komponentenlesart C1122 = C2323 enthaelt zusaetzlich die Restanisotropie, erwartet etwa 1 %
      bei N = 4000 (Abschnitt 5). Sie wird nur als Information berichtet.
  - Fehlt ein Netz, wird ueber die vorhandenen geurteilt, mit Vermerk. Fehlt fcc: nicht auswertbar.
- **Z1 (70 %)**, Hauptfall k1 [F], N = 64000: eingetroffen, wenn fuer beide Saaten S_T < 0,03 und D < 0,03.
  - Fehlt N = 64000 fuer eine Saat (auch bei Ersatz durch 32000): nicht auswertbar.
- **Z2 (60 %)**, k1 [F]:
  - S_T gemittelt (arithmetisch) ueber die zwei Saaten je N [F].
  - p = -Steigung der ungewichteten Ausgleichsgeraden von ln(S_T-Mittel) gegen ln N ueber die drei Groessen [F].
  - Eingetroffen, wenn 0,35 <= p <= 0,65. Fehlt eine Groesse: nicht auswertbar.
- **Z3 (65 %)**, k1, N = 64000: eingetroffen, wenn c_l/c_q (Richtungsmittel) fuer beide Saaten in [1,75; 2,2]
  liegt.
- **Z4 (60 %)**, k1: eingetroffen, wenn G/G_affin fuer alle sechs Netze (drei Groessen, zwei Saaten) in [0,5; 0,9]
  liegt [F: alle sechs, weil die Karte keine Groesse nennt].
- Bedeutung: wie in KARTE.md, unveraendert.
- Konvergenzproben (dichte Richtungen, Verfeinerung) aendern kein Urteil. Wuerde eine Probe das Urteil Z1 drehen,
  steht das als Selbstanzeige im Ergebnis.

## 4. Kontrollen (keine eigenen Urteile)

- Je Netz: Pruefungen (a) bis (f) aus 1.1, CG-Konvergenz, Stabilitaet, k1/kl-Netzgleichheit.
- Kontrolllauf: Direktloeser, Toleranzreihe, Born-Probe.
- fcc: affiner gleich relaxierter Tensor (jeder fcc-Knoten ist Inversionszentrum, f = 0 [M]);
  C11 = 2k/a = 1,41421, C12 = C44 = k/a = 0,70711 [M, GEGENLESEN-R35 4b].

## 5. Schreibtisch vorab (Erwartung, keine Regel)

- Affines Rauschen der Komponenten: Die relative Streuung von C1122 - C2323 ist etwa
  15 sqrt(<w^2>/<w>^2) sqrt(4/315)/sqrt(E) ~ 1,9/sqrt(7,77 N) [M, mit unabhaengigen Kanten genaehert].
  Das sind ~1,1 % bei N = 4000 und ~0,3 % bei N = 64000.
- Faellt die Restanisotropie wie ein Volumenmittel kurz korrelierter Beitraege, ist p = 0,5 [H].
- Mit 2 Saaten und 3 Groessen schaetze ich die Streuung von p auf etwa +-0,1 [H].

## 6. Rauchlaeufe vor dem Einfrieren (offengelegt)

- 21:09:11 bis 21:16:57 UTC: N = 4000 und N = 64000 mit Saat 9 im Rauchmodus (keine Tensoren gespeichert oder
  gedruckt), fcc-Gegenprobe, Kontrolllauf N = 4000 Saat 9 im Rauchmodus.
  - Auswertetest mit N = 500, 1000, 2000 (Saaten 1, 2; k1, kl). Dessen Ausgaben habe ich nur auf
    Rueckgabewert und Schluessel geprueft, Zahlen nicht angesehen.
- **Gesehen:**
  - Netzpruefungen (a) bis (e) alle erfuellt; Umkugeln mindestens 2,27 innerhalb des Rands.
  - Mittlerer Grad 15,5545 (N = 4000) und 15,5440 (N = 64000); Tetraeder je Punkt 6,777 und 6,772.
  - CG: 95 und 197 bis 199 Iterationen, Residuen < 1e-10, Abstand zur Kurzform 1e-12; 0,1 s bzw. 4,7 s je
    Verzerrung.
  - fcc: Abweichung von NETZ-C-1 3,5e-8 (das ist der Rest von |k| = 1e-3 in NETZ-C-1), von den geschlossenen
    Formen 2e-16.
  - Kontrolle: Direkt gegen CG 4e-16; CG mit rtol 1e-6 gibt C auf 1,5e-12; Born-Probe [100] und [110] auf 1e-8 bis
    4e-8.
- **Nicht gesehen:** Tensoren, G/G_affin, c_l/c_q, Richtungsschwankungen.
  - Born-Probe bei |k| = 2e-3 x 2 pi/L: -6e-8 (quer) und -1,4e-7 (laengs), also das Vierfache des Werts bei 1e-3.
    Die Abweichung ist damit die erwartete O(k^2)-Dispersion; der Grenzwert k -> 0 trifft Christoffel.
  - Der Kontrolllauf mit sieben Born-Punkten brauchte 451 s (Grenze 600 s).
- **Code nach dem Rauch geaendert (vor dem Einfrieren):**
  - Born-Probe mit fuenf statt sieben Punkten, Zwischenspeicher nach jedem Punkt.
  - Ein zweiter Rauch (21:17:15 bis 21:25:06 UTC, Saat 9) mit eigener Faktorisierung (Ordnung MMD_AT_PLUS_A) war
    langsamer (86 s je Punkt, 471 s gesamt). Deshalb bleibt die Standard-Faktorisierung von eigsh (etwa 60 s je
    Punkt). Gesehen dort: dieselben Kontrollzahlen wie im ersten Rauch.
  - Keine Schwelle und keine Urteilsregel geaendert.

## 7. Abbruch, Zeitbox, Ablage

- Laeuft etwas nach zwei ernsthaften Versuchen nicht: "nicht gerechnet" mit Grund; Rest fertig machen.
- Zeitbox 120 min ab 22:52 CEST.
- Ablage: lauf-69/ (Laufausgaben, auswertung.json, Bilder), rauch-69/ (Rauch), code/ (eingefroren mit Datumsendung).
- Nach dem Einfrieren: Plan und Urteilsregeln unveraendert; Code nur bei echten Fehlern, offengelegt.
