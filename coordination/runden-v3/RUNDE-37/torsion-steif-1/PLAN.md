# TORSION-STEIF-1: Plan (Code-Agent, Runde 45)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-05 04:19:11 CEST (date). Plantext ab 04:35:40 CEST (date),
  vor jeder Rechnung mit Werten.
- Bindend: KARTE.md (TS0 bis TS2, Wahrscheinlichkeiten, Bedeutung unveraendert). Dieser Plan legt nur fest, was die
  Karte offen laesst; solche Festlegungen heissen [F].
- Kennzeichen: [M] eigene Mathematik, [S] an der Quelle gelesen, [L] Gedaechtnis, [P] Projektdatei, [E] Rechnung,
  [H] Hypothese, [F] Festlegung. Alles ist synthetisch (Modellrechnung, keine Messdaten).
- Vor dem Plan gelaufen: ein Rauchtest auf der .69 (kleintest.sh, Spur cpu, 2,0 s), der nur Laufzeiten und Schluessel
  ausgibt; keine Werte gesehen.

## 1. Ableitbarkeitsprobe (Schritt 1)

### 1.1 Gl. 47 in Vektorform [M, S]

- Drehvektoren: [x] ist die schiefe Matrix mit [x] v = x cross v, also [x]_JK = -eps_JKL x_L.
  Dann gilt eps_IJK l^I [x]^JK = -2 l . x.
- Gl. 47 wird damit zu S = sum_B (1/m_B) sum_i l_B(i) . phi_B^(i), wobei phi_B^(i) der Drehvektor von h_B^(i) ist,
  also Ln h = [phi].
- Kontrolle an Gl. 74 bis 76: torsionsfrei ist h = exp(-eps U) mit U = -[l^]. Das ist eine Drehung um +eps um l^, also
  phi = eps l^ und S_B = eps L [S Gl. 76]. Stimmt.

### 1.2 BCH und Paargewichte der Startpunkt-Mittelung [M, vorab]

- Hintergrund: flach, alle Rahmen gleich ausgerichtet, h_e = exp([x_e]). Um das Gelenk B liegen die Durchgaenge
  a = 1..m in Umlaufrichtung, mit y_a = sigma_a x_t(a) (sigma = +1, wenn der Umlauf das Dreieck in Speicherrichtung
  A -> B quert).
- Start im Tetraeder i: Die zeitliche Reihenfolge ist i, i+1, ..., m, 1, ..., i-1. Nach BCH gilt
  phi^(i) = sum_a y_a + 1/2 sum_{spaeter k, frueher j} y_k x y_j + O(3).
- Fuer ein Paar a < b kommt b genau dann nach a, wenn i nicht in (a, b] liegt. Das sind m - (b - a) von m Starts.
- Mittelung: <phi> = sum_a y_a + 1/2 sum_{a<b} w(b - a) y_b x y_a mit **w(d) = 1 - 2 d / m**.
  - w haengt nur vom zyklischen Abstand ab und ist antisymmetrisch: w(m - d) = -w(d).
- Als zyklische schiefe Matrix W_ab = w((b - a) mod m) hat sie die Eigenwerte i cot(pi q / m) fuer q = 1..m-1 und 0
  fuer q = 0. Rechnung: sum_d (1 - 2d/m) z^d = -1 - 2/(z - 1) fuer z^m = 1, z != 1.
- **Folge:** Jedes Gelenk hat im Gewichtskreis die Nullrichtungen q = 0 (gleichfoermig) und, bei geradem m,
  q = m/2 (alternierend).
  - Auf dem Kuhn-Gitter sind alle m gerade: m = 6 an den Achsen- und Raumdiagonal-Kanten, m = 4 an den
    Flaechendiagonalen (Summe 36 = 6 Tetraeder x 6 Kanten).
  - Das ist der vorab sichtbare Kandidat fuer Gitter-Nullmoden. Ob die Summe ueber die Gelenke ihn erbt, ist nicht
    ableitbar (1.8).

### 1.3 Hesse-Bloecke [M]

- Erste Ordnung:
  - Nach x: sum_B l_B . sum_a y_a = sum_t x_t . (sum der Randkanten von t) = 0 wegen der Schliessung (Gl. 2).
  - Nach l: Ln 1 = 0.
  - Der Hintergrund ist also stationaer.
- **Kanten-Kanten-Block = 0 exakt**, denn S ist linear in l (bei h = 1 sogar S = 0 fuer jedes l).
- **Q (x gegen x):** S_XX(B) = 1/2 sum_{a<b} w(b-a) y_a^T [l_B] y_b, also der Block (t_a, t_b) = 1/2 sigma_a sigma_b W_ab [l_B].
  - Nur die Anteile senkrecht zur Gelenkkante zaehlen, da [l] l = 0.
  - Jeder Block ist ein Vielfaches von [l], also spurfrei. Damit ist **Q(k) spurfrei und an jedem k indefinit**
    (oder null). Positive "Steifigkeit" gibt es nicht; die Frage ist allein der Rang.
- **M (Geometrie gegen x):** S_lX = sum_B (1/m_B) sum_i (eps_i l_B) . F_B mit F_B = sum_a y_a und
  eps_i = 1/2 dg_i + [Omega_i].
  - Geometrievariablen je Zelle [F]: 7 Kantenquadrate ds_e und 6 x 3 Rahmendrehungen Omega_j.
  - dg_i ist die Metrikstoerung des Tetraeders aus seinen 6 ds. Dieselbe Parametrisierung wie REGGE-4D-1 (s = l^2).
- **Logarithmus:** Ln h und (h - h^T)/2 stimmen bis zur 2. Ordnung ueberein, denn exp(Phi) = 1 + Phi + Phi^2/2 + ...
  und Phi^2 ist symmetrisch. **Fuer die lineare Frage ist ein "Logarithmus-Artefakt" also vorab ausgeschlossen**;
  frei bleibt nur die Mittelung [M].

### 1.4 Torsionsfreier Sektor und Kopplung von TS1 und TS2 [M, vorab]

- Torsionsfreie Verbindung (Gl. 28 linearisiert): (eps_B - eps_A) d = x cross d fuer die Kanten d des gemeinsamen
  Dreiecks.
  - Das sind 6 Gleichungen fuer 3 Unbekannte. Sie sind vertraeglich, weil die Dreiecksmetrik in beiden Tetraedern
    gleich ist, und eindeutig loesbar.
  - Daraus folgt die Abbildung x = J(k) g, je Dreieck lokal.
- Torsionsfrei ist bei **jeder** Geometrie und **jedem** Startpunkt stationaer in h.
  - Grund: Fuer h parallel zu l gilt l . d(Ln h) = l . (h^-1 dh), danach greift die Schliessung, wie bei Gl. 113-115.
  - Linearisiert: **M^+ + Q J = 0** (Kontrolle KX).
- Daraus folgt [M]: **dim ker H(k) = dim ker R(k) + dim ker Q(k)** mit R = M J = -J^+ Q J.
  - R ist die Hesse-Matrix der torsionsfreien (Regge-)Wirkung, auf den Omega-Richtungen null.
  - Beweisskizze: x = J g + T. Dann gilt H(g, x) = 0 genau dann, wenn Q T = 0 und R g = -M T.
  - Die zweite Gleichung ist fuer jedes T in ker Q loesbar, denn M T steht senkrecht auf ker R.
- Mit REGGE-4D-1, 3D-Kontrolle [P], gilt dim ker R_ss = 3 (Translationen) bei k != 0. Damit ist dim ker R = 3 + 18 = 21
  = Zahl der Eichrichtungen.
- **Also: TS2 gilt an einem k genau dann, wenn Q(k) dort regulaer ist.** TS1 und TS2 sind keine unabhaengigen
  Vorhersagen.
  - Die Wahrscheinlichkeiten 45 % und 55 % der Leitung sind damit konsistent (komplementaer).
  - Geprueft wird die Identitaet trotzdem je k (Abschn. 5, Plan-Urteil TS2).

### 1.5 Eichbahnen [M]

- SO(3) je Tetraeder: Omega_j -> Omega_j + w_j, x_t -> x_t + w_B(t) - w_A(t). Das sind 18 je Zelle.
- Verschiebung je Ecke: ds_e = 2 d_e . (u(x + d_e) - u(x)), Omega_j = schiefer Teil von grad u im Tetraeder, x = 0.
  Das sind 3 je Zelle.
  - Exakt: S = 0 bei h = 1, und M^+ g_u = 0 folgt aus der Teleskopsumme ueber den Dreiecksrand.
- Bei k = 0 entfallen die Verschiebungen. Dafuer kommen 6 affine Moden hinzu (gleichfoermige Metrik), siehe
  REGGE-4D-1.
- Auf der Zwangsflaeche "fester Kantenvektor" gibt es keine Resteichung: Jede Nullmode von Q ist echt (Karte, [M]).

### 1.6 Literatur zuerst: Christiansen/Hu/Lin 2023, arXiv 2312.11709 [S]

- Abrufe B1 und B2 per WebFetch (quellen/B-abrufzeit.txt); Text in quellen/B2-2312.11709v1.txt; Erwartung vorher in
  quellen/ERWARTUNG-vor-Abruf.md (04:26:02).
- **Inhalt:**
  - Ein diskreter linearisierter Riemann-Cartan-**Komplex** (FEEC/BGG).
  - Die Verbindung liegt in Wh1 = Flaechendeltas c tensor n_f, also 3 je Flaeche; die Torsion in Vh2, ebenfalls 3 je
    Flaeche.
  - Der algebraische Operator S zwischen ihnen ist bijektiv: "S^-1 maps Vh2 to Wh1 (as S is bijective)" (Abschn. 4,
    Z. 550).
  - Bewiesen ist die Kohomologie, H_dR tensor RM (Satz 4.1, 5.1).
- **Nicht enthalten:**
  - keine Wirkung, keine Hesse-Matrix, keine Bewegungsgleichung (grep "action", "variational", "energy",
    "functional": nur ein Literaturtitel)
  - keine Startpunkt-Mittelung, kein Logarithmus, kein Fourier/Bloch, kein Kuhn-Gitter
  - Einstein-Cartan nur als Motivation; Torsion in Regge-Rechnung "beyond the scope" (Z. 140-144)
- **Folge:** Der kinematische Teil steht dort. "Torsionsfrei legt die Verbindung je Flaeche algebraisch fest" ist dort
  die Bijektivitaet von S, bei uns die lokale Abbildung J.
  - Der dynamische Teil (legt die Wirkung Gl. 47 die Torsion fest, also ist Q regulaer?) steht dort nicht.
  - Erwartungen E1 bis E4 eingetroffen; E4 so weit pruefbar.

### 1.7 Projekt-grep [P]

- Dossier (23:26) und hier um 04:35: Gesucht wurde nach "Torsions-Nullmode", "Holonomie-Hesse", "Startpunkt-Mittelung"
  und "Paargewicht", mit allen Ausschluessen.
- Einziger Fremdtreffer: RUNDE-34/fluss-1 ("paargewichtet", Statistik, sachfremd).
- Keine fruehere Rechnung dazu im Projekt.

### 1.8 Nicht ableitbar

- Ob Q(k) bei k != 0 einen Kern hat.
- Die hinreichende Bedingung "jedes Gelenk liegt in seinem Gewichtskern (q = 0, m/2)" ist ueberbestimmt: sum (2 m_B - 4)
  = 44 Bedingungen gegen 36 Unbekannte je Zelle. Q x = 0 verlangt aber nur, dass die Summe verschwindet.
- Also Numerik.

## 2. Gitter und Indizierung [M, F]

- Ecken: Z^3, eine je Zelle.
- **Tetraeder (j, R):** R, R + e_p0, R + e_p0 + e_p1, R + (1,1,1). p = PERMS[j], also itertools.permutations von
  (0,1,2) in dieser Reihenfolge, j = 0..5.
- **Kanten (e, R):** d_e in {0,1}^3 ohne 0, 7 Typen in itertools.product-Reihenfolge. Achsen m = 6, Flaechendiagonalen
  m = 4, Raumdiagonale m = 6.
- **Dreiecke (tau, R):** R, R + a, R + a + b mit a, b disjunkt und nicht null, 12 Typen.
  - Je Dreieck die zwei Tetraeder (A, B), sortiert nach (Zellversatz, j).
  - x_tau ist der Drehvektor von h_{A->B}.
- **Gelenk B = Kante (e, 0):**
  - Die dritten Ecken der Dreiecke um die Kante werden nach dem Winkel um d^ sortiert (Rechte-Hand-Regel).
  - Der Sektor zwischen zwei Nachbarn ist ein Tetraeder (assert).
  - Durchgang k fuehrt von Sektor k nach Sektor k+1, mit Vorzeichen sigma relativ zu A -> B.
- **Bloch:** f(R) = sum_k e^{ikR} f(k), Zellkonvention.
  - Variablen: z = (ds_0..6, Omega_{j,c} an 7 + 3j + c, x_{tau,c} an 25 + 3 tau + c), also 61.
  - Eintrag (Zeile, Spalte) += Koeffizient e^{ik (rho_Spalte - rho_Zeile)}.
  - S^(2) = 1/2 z^+ H(k) z je Zelle, H = [[0, M], [M^+, Q]]. Q ist 36 x 36, H ist 61 x 61.

## 3. k-Mengen [F]

- **Gitter:** k = 2 pi n / 12, n in {0..11}^3, also 1728 Punkte mit Gamma und Zonenrand.
- **Linien:** je 241 Punkte auf Gamma-X, Gamma-M, Gamma-R, X-M, M-R und zwei allgemeinen Richtungen von Gamma bis zum
  Rand, (1, 0.37, 0.61) und (-0.83, 0.29, 0.47), jeweils mal pi.
- **Zufall:** 500 Punkte in [-pi, pi)^3, Saat 20261005.
- **Klein:** |k| in {1e-3, 1e-2, 0.05, 0.1, 0.2, 0.4} in Richtung (1, 0.37, 0.61).
- Fuer die Urteile zaehlt "k != 0": Alle Punkte ausser Gamma = 0 (mod 2 pi).

## 4. Rechnung je k [F]

- Eigenwerte von Q(k) und H(k), jeweils aus eigvalsh.
- Eichvektoren: 21 Stueck, Rang per SVD, Residuum ||H Z|| / (||H|| ||Z||), getrennt nach Drehung und Verschiebung.
- J(k): Konsistenzresiduum; KX = ||M^+ + Q J|| / ||M||.
- R = M J: Hermitezitaet, Vergleich mit -J^+ Q J, Eigenwerte des ds-Blocks R_ss (7 x 7), Norm der Omega-Zeilen.
- **Variante E1 (beschreibend):** Q mit festem Start statt Mittelung, W_ab = sign(b - a) relativ zu Sektor 0. Gezaehlt
  werden Nullmoden.
- **Rahmenenergie (beschreibend):** kappa in {0, 0.25, 1}, auf den Linien ab Gamma und auf "klein".
  - Q_kappa = Q + 2 kappa 1, das ist sum_t 2 kappa (1 - cos |x_t|) zur 2. Ordnung, die Guertel-Bindungsenergie auf der
    Holonomie.
  - Gemessen werden Spektrum, Traegheit, Nullmoden von H_kappa und die Weitzenboeck-Form P^+ Q_kappa P mit
    P = x-Teil der Drehungseichung.

## 5. Urteilsregeln (vor jeder Rechnung mit Werten)

- Nullmode: |lambda| <= 1e-9 max|lambda| der jeweiligen Matrix am selben k.
- Traegheit: (Zahl negativ, null, positiv) mit dieser Schranke.

### TS0 (Kontrolle; Wortlaut: "Arm Linien gibt Rahmendrehung = Fehlwinkel auf 1e-8; ohne Torsion reproduziert der Code die Eichnullmoden (Verschiebung je Ecke)")

- **(a) Linien:** Gerechnet werden alle 7 Kantentypen mit 5 Einstellungen:
  - eta = 0
  - eta = +-0,05 auf dem Gelenkquadrat
  - eta = 0,05 und -0,08 mit 1 % bzw. 2 % Zufallsstoerung der uebrigen Sternkanten
  - Jeder Tetraeder hat dabei eine zufaellige Eichdrehung.
  - **Wortlaut:** ||psi| - |delta|| <= 1e-8 in allen 35 Faellen. Bei delta != 0 zusaetzlich: Drehachse parallel
    zur Gelenkkante auf 1e-8.
  - **Plan zusaetzlich:** Vorzeichen wie Gl. 74, also psi_signed = +delta (Drehung um +delta um l^ bei Umlauf nach der
    Rechten-Hand-Regel) auf 1e-8. Bei eta = 0 und ohne Stoerung muss delta = 0 auf 1e-12 sein (flacher Kuhn-Stern).
- **(b) Eichnullmoden:** An allen k != 0 aller Mengen gilt eich_res_trans <= 1e-9 und Rang 21.
  - Plan zusaetzlich: eich_res_rot <= 1e-9.
- **Urteil:** TS0 trifft ein, wenn (a) und (b) erfuellt sind; sonst verfehlt. Plan und Wortlaut werden getrennt
  angegeben.

### TS1 (Wortlaut: "Q(k) hat fuer k != 0 mindestens eine Nullmode; die Torsion ist auf dem Gitter dann nicht algebraisch festgelegt")

- N0(k) ist die Zahl der Nullmoden von Q(k).
- **Klassen:**
  - (i) **Nullband:** N0 >= 1 an allen ausgewerteten k != 0.
  - (ii) **Nullmenge:** N0 >= 1 an mindestens einem, aber nicht allen k != 0. Dazu zaehlt auch, wenn sich die Zahl
    negativer Eigenwerte zwischen zwei ausgewerteten k != 0 mit N0 = 0 unterscheidet. Dann liegt auf jedem Weg
    zwischen ihnen, der Gamma meidet, ein Nulldurchgang, also eine Nullmode bei einem k != 0.
  - (iii) **keine:** N0 = 0 ueberall und die Traegheit konstant.
- **Wortlaut-Urteil:** eingetroffen bei (i) oder (ii); verfehlt bei (iii).
- **Plan-Urteil:** eingetroffen bei (i), teilweise bei (ii), verfehlt bei (iii).
- Berichtet werden min_k min|lambda| / max|lambda| ueber alle k != 0 und der Wert bei Gamma.

### TS2 (Wortlaut: "Die volle Matrix hat ausser den Eichbahnen keine Nullmoden")

- **Wortlaut-Urteil:** eingetroffen, wenn an allen ausgewerteten k != 0 die Zahl der Nullmoden von H gleich dem
  Eichrang (21) ist, die Eichresiduen <= 1e-9 sind und die Traegheit von H ueber alle k != 0 konstant ist. Sonst
  verfehlt.
- **Plan zusaetzlich:** Die Identitaet N0_H = 18 + N0_Rss + N0_Q aus 1.4 gilt an jedem k (Abweichungen werden gezaehlt).
  KX <= 1e-9 an jedem k.

### Bedeutung

- Wie in der Karte, woertlich.
- **Plan-Zusatz:** Bei Klasse (ii) wird geprueft, ob die Nullmenge mit der Mittelung zusammenhaengt. Dazu dient der
  beschreibende Vergleich mit Variante E1. Ein Logarithmus-Artefakt ist fuer die lineare Frage nach 1.3 ausgeschlossen.

## 6. Kontrollen (L2/L3) [F]

- **KH:** Hermitezitaet von Q <= 1e-12 (relativ). KT: Spur von Q = 0 (<= 1e-12 absolut).
- **KN:** Gl. 47 exakt mit Matrixexponential und -logarithmus und Startpunkt-Mittelung auf dem 3^3-Torus, fuer 3
  zufaellige (g, x).
  - Zweite Differenz (S(t) + S(-t))/t^2 mit Richardson aus t = 2e-3 und 1e-3, verglichen mit z^T H z aus den
    Bloch-Matrizen.
  - Relativ <= 1e-6.
  - Damit sind Paargewichte, Orientierungen, M-Block und Bloch-Zusammenbau zugleich geprueft.
- **KG:** Erste Ordnung = 0, also (S(t) - S(-t))/(2t) skaliert wie t^2. Verhaeltnis zwischen t = 1e-3 und 2e-3 bei
  0,25 +- 0,01.
- **KE:** Eichresiduen und Rang wie TS0(b). **KJ:** J-Konsistenz <= 1e-9. **KX:** <= 1e-9.
- **KR (beschreibend, Bezug REGGE-4D-1 3D):** R_ss hat bei k != 0 3 Nullmoden. Bei kleinem k zwei Moden des einen und
  eine des anderen Vorzeichens ~ k^2, dazu eine Gittermode vom Betrag ~ 3,4 bis 3,5.
  - REGGE-4D-1 berichtet H = -Hess: 2 positiv, 1 negativ, Gittermode 3,41 bis 3,50.
  - Hier ist R = +Hess von S = sum eps L. Erwartet sind also 2 negativ, 1 positiv, Gittermode ~ -3,5.

## 7. Arm "Linien" [F]

- Stern einer Kuhn-Kante aus den m Tetraedern.
- Kantenquadrate: Kuhn-Werte. Das Gelenkquadrat mal (1 + eta), die uebrigen Sternkanten wahlweise mal (1 + stoer U(-1,1)).
- Jeder Tetraeder wird einzeln eingebettet (Gram plus Cholesky, Eckenreihenfolge P0, P1, W_{k-1}, W_k, positive
  Orientierung) und zufaellig gedreht (Eichung).
- **Fehlwinkel:** delta = 2 pi - Summe der Diederwinkel am Gelenk.
- **Holonomie je Grenzflaeche:** Die Drehung, die (d1, d2, d1 x d2) des gemeinsamen Dreiecks von Tetraeder k nach k+1
  abbildet (Gl. 28 mit Orientierungsbedingung).
- **Band:** Rahmen (Tangente = Linkkante in Tetraeder 0, markierte Seite = l^ x t) wird einmal um das Gelenk
  getragen. Gemessen werden der Drehwinkel psi von P = h_{m-1} ... h_0, die Achse gegen l^ und der Bandwinkel.

## 8. Arm "Rahmenenergie" (beschreibend) [F]

- Was vorab ableitbar ist [M]:
  - P^+ Q P = 0, denn M P = 0 und M^+ = -Q J. Die Weitzenboeck-Richtungen (x = D omega) haben in der EC-Wirkung keine
    Energie.
  - Mit Rahmenenergie wird daraus P^+ Q_kappa P = 2 kappa P^+ P ~ kappa k^2.
  - Gerechnet wird es trotzdem, als Kontrolle.
- **Nicht ableitbar:** Ob Q + 2 kappa fuer kappa > 0 an Wellenzahlen k != 0 singulaer wird. Q ist indefinit, eine
  Verschiebung kann Eigenwerte durch null schieben. Das waere eine Antwort mit grosser Reichweite, also
  Ausbreitungsfaehigkeit der Torsion im statischen Sinn.
- Berichtet werden Spektrumsbereiche, Traegheitswechsel auf den Linien und Nullmoden von H_kappa.

## 9. Laufzeit und Ablauf [F]

- Rauchtest: 2,0 s bei 34 k-Punkten und 1 KN-Zufallsvektor. Hauptlauf: etwa 3900 k-Punkte zu ~21 ms, also ~90 s.
  KN mit 3 Vektoren ~3 s. Gesamt unter 3 min auf Spur cpu, 1 Thread.
- Auswertung (code/auswertung.py, wendet Abschn. 5 und 6 an): Sekunden, Spur cpu11.
- **Ablauf:** einfrieren (PLAN.md und code/*, SHA256 lokal und auf der .69 gleich) -> haupt -> auswertung -> ERGEBNIS.md.
  Alles nach Sicht der Werte kommt in neue, als Nachtrag gekennzeichnete Dateien.

## 10. Selbstanzeigen bis hier

- Der Code (code/torsion_steif.py) ist vor dem Plantext entstanden. Plan und Code werden gemeinsam eingefroren.
- Der Rauchtest lief vor dem Einfrieren. Er gab nur Laufzeiten und Schluessel aus; die Ausgabedatei rauch.json enthaelt
  nur diese.
- Zweiter Rauchtest um 04:38 (Modus rauchvoll auf winzigen k-Mengen, dann auswertung.py auf Spur cpu11). Gesehen habe
  ich nur die Rueckgabecodes (0, 0), die Fehlerzahl im Log (0) und die Schluessel der Auswertedatei. Die Werte dort sind
  nicht angesehen. Fuer diesen Test kam der Modus "rauchvoll" in den Code (nur Moduswahl, sonst unveraendert).
