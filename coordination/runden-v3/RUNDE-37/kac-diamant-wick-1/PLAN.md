# KAC-DIAMANT-WICK-1: PLAN (vor jeder Rechnung)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-05 07:54:25 CEST (date). Plantext ab 08:04:43 CEST (date).
- Bindend: KARTE.md. KW0 bis KW3 und ihre Bedeutung bleiben unveraendert.
- Gelesen (nur lesen): KARTE.md; unschaerfe-kante-l/DOSSIER.md Abschn. 9 bis 11; Ghose 2609.29248 lokal
  (unschaerfe-kante-l/quellen/A9-ghose-2609.29248-20261005-060017.txt, Gl. 60 bis 80 und der Text danach), kein
  Web-Abruf; qca-tetra-1/ERGEBNIS.md und PLAN.md Punkt 4 (Eichung) sowie code/qca_tetra.py (fib_dirs, speeds);
  dunkel-flip-l/DOSSIER.md Abschn. 1; diamant-fermion-l/DOSSIER.md (Kopf und Tabelle).
- Kennzeichen: [S] an der Quelle gelesen, [M] eigene Mathematik (hier am Schreibtisch, vor der Rechnung), [P] Projekt,
  [H] Hypothese, [F] eigene Festlegung.

## 1. Ghose, Gl. 61 bis 77: was wird rotiert? [S]

- Gl. 61: dP/dt = -v sigma_z dP/dx + lambda (sigma_x - I) P (reeller Kac-Prozess, zwei Richtungen).
- Gl. 63/64: Der Verlustterm -lambda I wird vor der Rotation abgespalten, P = e^{-lambda t} Phi.
- Gl. 66: Die Zeit wird rotiert, tau = i t (tau = reeller Parameter des stochastischen Prozesses).
- Gl. 69 bis 71: Die Geschwindigkeit folgt daraus, v_E = dx/dtau -> -i c. Ghose: "not an additional prescription".
- Gl. 73 bis 77: d/dtau = -i d/dt; Einsetzen und Multiplikation mit -hbar gibt
  i hbar dPsi/dt = -i hbar c sigma_z dPsi/dx - hbar lambda sigma_x Psi, mit hbar lambda = m c^2 (Gl. 76).
- **Die Rate lambda bleibt reell.** Ghose zieht das ausdruecklich der GJKS-Variante mit imaginaerer Rate vor (Text nach
  Gl. 80). Rotiert werden also Zeit und Geschwindigkeit, nicht die Rate.

**Uebertragung auf 8 Zustaende [M]:** reeller Erzeuger L = -v_s . grad + lambda (M - I). Mit d/dtau = -i d/dt,
v_s -> -i v_s und ebener Welle e^{i k.x} folgt H(k) = -hbar L|_{v -> -i v} = hbar [ T(k) + lambda (I - M) ].

- 1D-Probe: zwei Zustaende, v = +-c, M = sigma_x gibt H = hbar [c k sigma_z + lambda (I - sigma_x)], also
  E = hbar lambda +- hbar Wurzel(lambda^2 + c^2 k^2). Das ist Ghoses Gl. 77 mit behaltenem Verlustterm (E0 = hbar lambda).
- **Lesart (gebunden):** Ghose woertlich, Verlustterm behalten (er erscheint als E0).
- **Mehrdeutigkeit, vorab geprueft [M]:**
  - GJKS mit imaginaerer Rate (t, v reell, lambda -> i lambda, H = i hbar G): ergibt **dieselbe Matrix**
    T(k) + lambda (I - M). Die zweite Lesart rechne ich als Nebenarm "gjks" mit (Erwartung: Spektren gleich bis 1e-12).
  - Verlustterm abgespalten oder behalten: nur E0 verschiebt sich. Vorzeichen von i (t -> -i t): Spiegelung E -> -E.
    Beides aendert die Form E0 +- Wurzel(...) nicht.
  - Nur t rotieren, v reell lassen, gaebe i G(k): nicht hermitesch, das ist die reelle Fassung mal i. Ghose verwirft das
    (Gl. 70/71); kein eigener Arm.

## 2. Der 8x8-Erzeuger, ausgeschrieben

- Einheiten [F]: c = lambda = hbar = 1. Die mittlere Fluglaenge je Umklapp ist l = c/lambda = 1 = Bindungslaenge
  (jeder Wahlschritt wechselt das Untergitter, also ein Bindungsschritt). \|k\| in Einheiten 1/l, wie in QCA-TETRA-1
  (dort Schrittlaenge \|h\| = 1). Nebenzahl, nur beschreibend: kubische Gitterkonstante a = 4 l/Wurzel(3); \|k\| a = 0,05
  entspricht \|k\| l = 0,02165.
- Tetraederrichtungen: e_1 = (1,1,1)/Wurzel3, e_2 = (1,-1,-1)/Wurzel3, e_3 = (-1,1,-1)/Wurzel3, e_4 = (-1,-1,1)/Wurzel3.
- Basis (A1, A2, A3, A4, B1, B2, B3, B4). Zustand (A,i) laeuft mit +c e_i, (B,i) mit -c e_i.
- T(k) = diag(c e_1.k, ..., c e_4.k, -c e_1.k, ..., -c e_4.k).
- M = [[0, P], [P, 0]], P_gleich = J/4, P_ohne = (J - I)/3 (J = 4x4-Einsmatrix).
- **Reell (Kac):** dP/dt = -v.grad P + lambda (M - I) P, also G(k) = -i T(k) + lambda (M - I). Komplex symmetrisch.
- **Wick (Ghose):** H(k) = T(k) + lambda (I - M). Reell symmetrisch, reelles Spektrum.
- Identitaet [M]: H(k) = -G(-i k). Die reelle Fassung ist die Wick-Fassung bei imaginaerem k (Telegraphenform).

## 3. Schreibtisch vor der Rechnung [M]

### 3.1 Niveaus bei k = 0

| Regel | Eigenwerte P | reell lambda(M - I) | Wick lambda(I - M) |
|---|---|---|---|
| gleich J/4 | 1, 0 (3x) | 0, -2, -1 (6x) | 0, 2, 1 (6x) |
| ohne (J - I)/3 | 1, -1/3 (3x) | 0, -2, -2/3 (3x), -4/3 (3x) | 0, 2, 2/3 (3x), 4/3 (3x) |

### 3.2 Symmetrien (vorab ableitbar)

- Permutationen der e_i (T_d) und der Tausch A <-> B mit k -> -k sind Symmetrien. Zusammen ist das O_h.
- **Folge 1: Das 8x8-Spektrum ist gerade in k. Eine lineare Kippung gibt es im 8x8 nicht.** Die Karte nennt die
  Aufhebung der Kippung "nicht ableitbar". Sie folgt aus dem A <-> B-Tausch (X T(k) X = T(-k), X M X = M).
- **Folge 2:** Fuer ein bei k = 0 nicht entartetes Band ist der k^2-Koeffizient isotrop (O_h-invarianter Tensor 2. Stufe).
  Die erste Anisotropie steht bei k^4 und ist proportional zu K4 = n_x^4 + n_y^4 + n_z^4, mit Extremen bei [100] (K4 = 1)
  und [111] (K4 = 1/3).
- **Folge 3 (chiral):** U = (sigma_z sigma_x) auf dem Untergitter gibt U (H - lambda) U^+ = -(H - lambda). Das Spektrum
  ist fuer jedes k symmetrisch um lambda: E_j + E_(9-j) = 2 lambda.

### 3.3 Struktur

- Singulett s = (1,1,1,1)/2 und Triplett t_a, (t_a)_i = (Wurzel3/2)(e_i)_a. Mit S+-, tau+- = (A +- B)/Wurzel2:
  - Niveaus: S+ = 0, tau- = lambda(1 + p) (3x), tau+ = lambda(1 - p) (3x), S- = 2 lambda; p = 0 (gleich), -1/3 (ohne).
  - Kopplungen: S+ - tau- und S- - tau+ mit c k/Wurzel3 (isotrop); tau+ - tau- mit (c/Wurzel3) Q(k),
    Q = [[0, k_z, k_y], [k_z, 0, k_x], [k_y, k_x, 0]] (anisotrop); S+ - S- null.
- **[100] exakt:** (1+p)/2 +- Wurzel((1+p)^2/4 + k^2/3); (3-p)/2 +- Wurzel((1+p)^2/4 + k^2/3); 1 +- Wurzel(p^2 + k^2/3) (2x).
- **[111] exakt:** quer 1 +- Wurzel(p^2 + k^2/9) (2x); laengs 1 +- Wurzel(x), x = [B +- Wurzel(B^2 - 4C)]/2,
  B = 1 + p^2 + 10k^2/9, C = (p + k^2/3)^2 + 4k^2/9.
  - Fuer p = -1/3 ist B^2 - 4C ein Quadrat: laengs 1 +- Wurzel(1 + k^2) und 1 +- (1/3) Wurzel(1 + k^2).
    **Ohne Ruecksprung ist das aeussere Paar laengs [111] exakt Ghoses 1D-Dirac** (Delta = lambda, c_eff = c).

### 3.4 Kandidat: das aeussere Paar (Baender 1 und 8, aus S+ und S-)

- E0 = lambda, Delta = lambda (exakt, aus k = 0 und Folge 3).
- k^2-Ordnung: unteres Band E_1 = -D k^2 mit D = c^2/(3 lambda (1 + p)) (gleich: 1/3, ohne: 1/2). Das ist der
  Diffusionskoeffizient der reellen Fassung (Persistenz gamma = -p).
- Daraus c_eff^2 = 2 lambda D = 2c^2/(3(1 + p)) und m = Delta/c_eff^2 = hbar/(2D) (Nelsons D = hbar/2m, Ghose Gl. 58).
- k^4-Ordnung von h^2 = ((E_8 - E_1)/2)^2 = Delta^2 + c_eff^2 k^2 + beta k^4:
  beta_100 = -(1 - p)/(9(1 + p)^3), beta_111 = [16(1 + p)^2 - (1 - 5p)^2]/(81 (1 - p)(1 + p)^3),
  beta_111 - beta_100 = 8/(27 (1 - p)(1 + p)^2).
- Lokale Geschwindigkeit c_loc(k) = Wurzel((h^2 - Delta^2)/k^2). Spannweite/Mittel bei \|k\| = 0,05:
  2k^2/(9(1 - p^2)); Std/Mittel ueber die gleichverteilte Kugel = Spannweite x Std(K4)/(2/3) = Spannweite x 0,2619.

| Groesse (Schreibtisch, fuehrende Ordnung) | gleich J/4 | ohne (J - I)/3 |
|---|---|---|
| E0, Delta | 1, 1 (hbar lambda) | 1, 1 (hbar lambda) |
| c_eff (k -> 0) | Wurzel(2/3) = 0,8164966 | 1 |
| m = Delta/c_eff^2 (KW3) | 3/2 = 1,5 (hbar lambda/c^2) | 1 (hbar lambda/c^2) |
| D (reell) | 1/3 | 1/2 |
| beta_100, beta_111 | -1/9, 5/27 | -1/2, 0 |
| Spannweite/Mittel von c_loc bei 0,05 | 5,56e-4 | 6,25e-4 |
| Std/Mittel (Kugel) bei 0,05 | 1,46e-4 | 1,64e-4 |
| groesste relative Formabweichung von c_loc bei 0,05 / 0,1 | 3,5e-4 / 1,4e-3 ([111]) | 6,3e-4 / 2,5e-3 ([100]) |

- Grosse k (nur beschreibend): Die Grenzgeschwindigkeit des aeusseren Bandes ist max_i \|e_i . n\|, also c laengs [111],
  c Wurzel(2/3) laengs [110], c/Wurzel3 laengs [100]. Der "Lichtkegel" der Kantenwahl ist tetraedrisch, nicht rund.
- Triplett-Paare (zur Abgrenzung): ohne Ruecksprung laengs [100] Delta = 1/3, c_eff = 1/Wurzel3; laengs [111]
  Delta = 1/3, c_eff = 1/3. Richtungsstreuung O(1). Gleichverteilt sind die Triplettbaender bei k = 0 sechsfach
  entartet und spalten linear (masselose, anisotrope Kegel).

### 3.5 Vorab ableitbare Urteile (keine Messung)

- **KW0:** eingetroffen, aus 3.1 und Folge 2.
- **KW1 (Hauptlesart, Abschn. 5):** eingetroffen fuer beide Regeln; aeusseres Paar, Std/Mittel ~ 1,5e-4 bis 1,6e-4
  gegen 2,8e-3; Formabweichung bei \|k\| <= 0,05 hoechstens ~ 6e-4.
- **KW1 (strenge Nebenlesart, exakte Dirac-Form):** nicht eingetroffen. Exakt ist das aeussere Paar nur ohne Ruecksprung
  und nur laengs [111].
- **KW2:** nicht eingetroffen. Ohne Ruecksprung ist die Streuung des besten Paars um den Faktor 9/8 groesser.
- **KW3:** eingetroffen; Delta = 1 x hbar lambda; m = 3/2 bzw. 1 (in hbar lambda/c^2).
- Die Rechnung prueft also meine Herleitung, die hoeheren Ordnungen und den Code. Sie ist keine unabhaengige Messung
  einer offenen Groesse.

## 4. Richtungen und \|k\|

- Kartenliste (Formtest, KW3): die 26 Gitterrichtungen (6 vom Typ 100, 12 vom Typ 110, 8 vom Typ 111), dazu 400
  Zufallsrichtungen, numpy default_rng(20261005), normierte Gauss-Vektoren.
- Streuungsliste (wie QCA-TETRA-1): 400 Fibonacci-Richtungen, fib_dirs(400) woertlich aus qca_tetra.py.
- \|k\| (Karte): 0,0125, 0,025, 0,05, 0,1. Beschreibend zusaetzlich 0,0216506 (a-Einheit) und 1,0 (c k = lambda).
- Bild: \|k\| von 0 bis 3 laengs [100], [110], [111].

## 5. Fitregel "Bandpaar der Dirac-Form" [F]

- Wick: Eigenwerte aufsteigend E_1 ... E_8 (eigvalsh). Kandidaten: alle 28 Paare (i < j).
- Je Paar und Richtung:
  - E0 = (E_i(0) + E_j(0))/2 und Delta = (E_j(0) - E_i(0))/2 aus den Niveaus bei k = 0 (kein Fit).
  - Mitte m(k) = (E_i + E_j)/2, Halbabstand h(k) = (E_j - E_i)/2, c_loc^2(k) = (h^2 - Delta^2)/k^2.
  - c_eff^2 = Grenzwert k -> 0 per Richardson aus den Kartenwerten 0,0125 und 0,025:
    c_eff^2 = (4 c_loc^2(0,0125) - c_loc^2(0,025))/3.
  - **Formrest** = Maximum ueber \|k\| in {0,0125; 0,025; 0,05} von max(\|c_loc(k) - c_eff\|/c_eff, \|m(k) - E0\|/(c_eff k)).
    Bei \|k\| = 0,1 nur beschreibend.
  - **Form verfehlt**, wenn c_loc^2 <= 0 bei einem Kartenwert oder der Formrest in einer Richtung der Kartenliste
    ueber 2,8e-3 liegt. Begruendung: dieselbe Zahl und dieselbe Art Groesse (relative Geschwindigkeitsabweichung) wie die
    Eichung, ausgewertet bis zum Auswertepunkt \|k\| = 0,05 der Karte. Die Schwelle ist nach der Schreibtischrechnung
    gesetzt; das Urteil ist vorab ableitbar (3.5).
- **Richtungsstreuung (wie QCA-TETRA-1):** v(n) = c_loc(0,05 n), Std/Mittel ueber die 400 Fibonacci-Richtungen.
  Beschreibend dazu Spannweite/Mittel und dieselben Werte ueber die Kartenliste.
- **Bestes Paar je Regel:** unter den Paaren ohne "Form verfehlt" das mit der kleinsten Richtungsstreuung; gibt es keines,
  das kleinste ueber alle Paare mit c_loc^2 > 0, markiert.
- **Strenge Nebenlesart:** exakte Dirac-Form, \|h^2 - Delta^2 - c_eff^2 k^2\| <= 1e-9 c_eff^2 k^2 und
  \|m - E0\| <= 1e-12 bei allen vier Kartenwerten. Gezaehlt wird, in wie vielen Richtungen das gilt.
- **Reelle Fassung:** aeusseres Paar = Eigenwerte von G mit groesstem und kleinstem Realteil (aus 0 und -2 lambda).
  Telegraphenform g = -E0 -+ Wurzel(Delta^2 - c_eff^2 k^2); E0 = -(g_a(0) + g_b(0))/2, Delta = (g_a(0) - g_b(0))/2,
  c_loc^2 = (Delta^2 - h^2)/k^2; Formrest und Streuung wie oben. Imaginaerteile werden mitgeschrieben.
- **KW0, k^2-Koeffizient:** D(n) = u_0^T T(n) (-G_0)^+ T(n) u_0 (exakte zweite Stoerungsordnung, Pseudoinverse), Spannweite/
  Mittel ueber alle 826 Richtungen < 1e-9. Gegenprobe beschreibend: Richardson aus dem langsamen Eigenwert bei
  k = 0,0125/0,025 (erwartet ~1e-7 Abweichung durch k^6) und Kruemmung des Wick-Bandes E_1.
- **KW3:** gilt KW1, dann Delta/hbar lambda rational (Toleranz 1e-12 gegen 1) und max ueber die Kartenliste
  \|m - m_Schreibtisch\|/m_Schreibtisch <= 1e-6 mit m = Delta/c_eff^2 (Richardson).
- **Kontrollen:** Niveaus gegen 3.1 (1e-12); [100]- und [111]-Formeln aus 3.3 gegen Numerik (1e-12); H(k) = -G(-i k)
  (1e-12); Nebenarm gjks gegen Wick (1e-12); chirale Symmetrie E_j + E_(9-j) = 2 (1e-12).

## 6. Laeufe

- R0 Rauchtest (<= 120 s, Spur cpu7): Umgebung (numpy, matplotlib), Niveaus, eine Richtung.
- Danach Plan und Code einfrieren (Kopien mit Zeitstempel, sha256 in EINGEFROREN-SHA256.txt).
- H1 Hauptlauf (cpu7): alles aus Abschn. 5, Ausgabe haupt.json mit den Urteilen nach dieser Regel.
- B1 Bild (cpu7): Baender ueber \|k\| fuer [100], [110], [111], beide Regeln, Wick und reell (Re und Im).
- Je Lauf hoechstens 10 min, ein Thread, ueber kleintest.sh. Arbeitsordner .69: /home/fmh/fmhc-physics-remote/kac-diamant-wick-1/.
- **Rauchtests vor dem Einfrieren (cpu7, UTC = CEST - 2 h):**
  - R0 06:08:54 UTC, Modus rauch: numpy 2.4.4, matplotlib 3.11.2; Niveaus und [100]-Baender bei \|k\| = 0,05 gegen die
    Formeln aus 3.3 (Kontrolle, sichtbar: Abweichung ~1e-16).
  - R0b 06:10:19 UTC, Modus rauchhaupt: nur Codepfad mit 30 + 10 Richtungen, keine Zahlen in der Ausgabe.
  - R0c 06:10:19 bis 06:10:21 UTC: Bild mit 31 Punkten. Danach eine Aenderung: dritte Zeile zeigt \|Im g\| statt Im g,
    weil konjugierte Paare beim Sortieren nach Realteil die Reihenfolge tauschen (Zickzack).
